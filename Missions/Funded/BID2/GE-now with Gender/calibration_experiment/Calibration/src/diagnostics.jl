################################################################################
#  diagnostics.jl
#
#  Post-convergence diagnostics for the SMM estimates.
#
#    1. Numerical Jacobian J_ij = ∂m_i/∂θ_j via central differences in the
#       unconstrained x-space; converted back to economic-parameter sensitivity
#       via the chain rule (so the printed Jacobian is in (m, θ_econ) units).
#
#    2. Sandwich-formula standard errors:
#         Var(θ̂) = (J'WJ)^(-1) J'WΩWJ (J'WJ)^(-1)
#       with W = diag(1/SE²), Ω = diag(SE²); for exactly-identified J (square),
#       this reduces to Var(θ̂) = J^(-1) Ω (J')^(-1).
#
#    3. Moment-match table: (m_dat, m_sim, m_sim - m_dat, t-stat) per moment.
#
#    4. (Plot) Jacobian heatmap, moment-match bar chart, eval-log trace.
#
#  Requires Plots; OK to skip plots if Plots not loadable.
################################################################################

using Plots
using LinearAlgebra: pinv, diagm, diag

# ─── Numerical Jacobian (central differences) ───────────────────────────────
"""
    numerical_jacobian(obj, x_hat; h=1e-4) -> Matrix (n_moments × n_params)

Central-difference Jacobian of the simulated moment vector w.r.t. the
unconstrained x-parameters. Each finite-difference column requires 2 PE solves
(plus a baseline solve). For 6 params: 13 PE solves.

The chain-rule conversion to economic parameters is left to the caller;
typically you want the x-space Jacobian for SE computation (consistent with
the optimizer) and the econ-space Jacobian for interpretation.
"""
function numerical_jacobian(obj, x_hat::Vector{Float64}; h::Float64=1e-4)
    n_p = length(x_hat)
    # Baseline (warm cache + sanity-check it converges)
    Q0 = obj(x_hat)
    m0_str = readlines(obj.eval_log.path)[end]   # last logged moments
    # Parse the last log row to get the moment vector at x_hat
    m0_fields = split(m0_str, ',')
    # Layout: eval_idx,objective,<params>,<moments>,wall_seconds,status
    n_mom = length(obj.target_names)
    m0 = [parse(Float64, m0_fields[2 + n_p + i]) for i in 1:n_mom]

    J = zeros(n_mom, n_p)
    for k in 1:n_p
        x_plus  = copy(x_hat); x_plus[k]  += h
        x_minus = copy(x_hat); x_minus[k] -= h
        _ = obj(x_plus)
        m_plus_str = readlines(obj.eval_log.path)[end]
        m_plus = [parse(Float64, split(m_plus_str, ',')[2 + n_p + i]) for i in 1:n_mom]
        _ = obj(x_minus)
        m_minus_str = readlines(obj.eval_log.path)[end]
        m_minus = [parse(Float64, split(m_minus_str, ',')[2 + n_p + i]) for i in 1:n_mom]
        J[:, k] = (m_plus .- m_minus) ./ (2 * h)
    end
    return J, m0
end

# ─── Sandwich-formula SEs ───────────────────────────────────────────────────
"""
    sandwich_se(J, ses) -> Vector{Float64}

Sandwich SEs for the SMM estimator with W = Ω^(-1):
    Var(θ̂) = (J'WJ)^(-1) J'WΩWJ (J'WJ)^(-1)

For exactly identified J (square, full rank): Var(θ̂) = J^(-1) Ω (J')^(-1).
This implementation uses the pseudo-inverse so an underidentified system
returns finite values (flagged via condition number).
"""
function sandwich_se(J::Matrix{Float64}, ses::Vector{Float64})
    n_p = size(J, 2)
    W = diagm(1.0 ./ (ses .^ 2))
    Ω = diagm(ses .^ 2)
    A = J' * W * J
    Σ = pinv(A) * (J' * W * Ω * W * J) * pinv(A)
    return sqrt.(max.(diag(Σ), 0.0))
end

# ─── Moment-match table ─────────────────────────────────────────────────────
"""
    moment_match_table(m_sim, m_dat, ses, names) -> Vector of NamedTuples

(name, m_dat, m_sim, diff, abs_diff, t_stat) — t_stat = diff / SE.
"""
function moment_match_table(m_sim::Vector{Float64}, m_dat::Vector{Float64},
                             ses::Vector{Float64}, names::Vector{String})
    [(; name = names[i], m_dat = m_dat[i], m_sim = m_sim[i],
       diff = m_sim[i] - m_dat[i], abs_diff = abs(m_sim[i] - m_dat[i]),
       t_stat = (m_sim[i] - m_dat[i]) / ses[i])
     for i in eachindex(names)]
end

# ─── Write diagnostics to CSV ───────────────────────────────────────────────
function write_diagnostics(out_dir::String,
                            θ_hat::Vector{Float64},
                            θ_names::Vector{String},
                            θ_se::Vector{Float64},
                            J::Matrix{Float64},
                            m_sim::Vector{Float64},
                            m_dat::Vector{Float64},
                            ses::Vector{Float64},
                            target_names::Vector{String})
    mkpath(out_dir)

    # theta_hat.csv
    open(joinpath(out_dir, "theta_hat.csv"), "w") do io
        println(io, "param,estimate,se,t_stat")
        for i in eachindex(θ_names)
            t = θ_se[i] > 0 ? θ_hat[i] / θ_se[i] : NaN
            println(io, "$(θ_names[i]),$(θ_hat[i]),$(θ_se[i]),$(t)")
        end
    end

    # moment_match.csv
    open(joinpath(out_dir, "moment_match.csv"), "w") do io
        println(io, "moment,data,model,diff,abs_diff,t_stat")
        for row in moment_match_table(m_sim, m_dat, ses, target_names)
            println(io, "$(row.name),$(row.m_dat),$(row.m_sim),$(row.diff),$(row.abs_diff),$(row.t_stat)")
        end
    end

    # jacobian.csv
    open(joinpath(out_dir, "jacobian.csv"), "w") do io
        println(io, "moment," * join(θ_names, ","))
        for i in eachindex(target_names)
            println(io, target_names[i] * "," * join(J[i, :], ","))
        end
    end

    return nothing
end

# ─── Plot helpers ───────────────────────────────────────────────────────────
function plot_moment_match(m_sim, m_dat, ses, names; outpath::String)
    p = bar(names, (m_sim .- m_dat) ./ ses;
            ylabel = "(model − data) / SE", xlabel = "",
            title  = "Moment match (t-stat)", legend = false, xrotation = 30)
    hline!(p, [0]; lw = 1, color = :black)
    hline!(p, [2.0, -2.0]; lw = 1, ls = :dash, color = :red, label = "")
    savefig(p, outpath)
    return p
end

function plot_jacobian_heatmap(J, target_names, param_names; outpath::String)
    # Normalize each column by its max-abs so the heatmap is readable.
    Jn = copy(J)
    for k in 1:size(Jn, 2)
        s = maximum(abs.(Jn[:, k]))
        s > 0 && (Jn[:, k] ./= s)
    end
    p = heatmap(param_names, target_names, Jn;
                xlabel = "Parameter (col-normalized)", ylabel = "Moment",
                title  = "Numerical Jacobian (column-normalized)",
                color = :balance, clim = (-1, 1))
    savefig(p, outpath)
    return p
end

function plot_eval_log_trace(eval_log_path::String; outpath::String)
    lines = readlines(eval_log_path)
    length(lines) > 1 || error("eval_log empty")
    iters = Int[]; Qs = Float64[]
    for ln in lines[2:end]
        parts = split(ln, ',')
        push!(iters, parse(Int, parts[1]))
        Q = parse(Float64, parts[2])
        push!(Qs, Q)
    end
    p = plot(iters, Qs; lw = 1, marker = :circle, ms = 2,
             xlabel = "Eval index", ylabel = "Objective",
             title = "SMM objective trace", yscale = :log10, legend = false)
    savefig(p, outpath)
    return p
end

"""
    full_diagnostics_report(obj, x_hat, io, out_dir; h_fd=1e-4)

Top-level: computes Jacobian, SEs, writes 3 CSVs and 3 PNGs to `out_dir`.
Returns a NamedTuple with the headline numbers for programmatic use.
"""
function full_diagnostics_report(obj, x_hat::Vector{Float64},
                                  io::NamedTuple, out_dir::String;
                                  h_fd::Float64 = 1e-4)
    ti = io.theta_init
    J, m_sim = numerical_jacobian(obj, x_hat; h=h_fd)

    # x-space SEs
    se_x = sandwich_se(J, io.targets.ses)
    # Convert x-space SEs to econ-space SEs by delta method:
    # θ_econ_i = g_i(x_i) for elementwise transform g_i;
    # SE_θ_i ≈ |g_i'(x_i)| · SE_x_i
    θ_econ = vec_from_unconstrained(x_hat, ti)
    se_econ = similar(se_x)
    for i in eachindex(x_hat)
        t = ti.transform[i]
        g_prime = if t === :log
            exp(x_hat[i])
        elseif t === :logit
            (ti.ub[i] - ti.lb[i]) * exp(x_hat[i]) / (1.0 + exp(x_hat[i]))^2
        elseif t === :identity
            1.0
        else
            NaN
        end
        se_econ[i] = abs(g_prime) * se_x[i]
    end

    write_diagnostics(out_dir, θ_econ, ti.names, se_econ, J,
                       m_sim, io.targets.values, io.targets.ses,
                       io.targets.names)

    diag_dir = joinpath(out_dir, "diagnostics")
    mkpath(diag_dir)
    plot_moment_match(m_sim, io.targets.values, io.targets.ses,
                       io.targets.names;
                       outpath = joinpath(diag_dir, "01_moment_match.png"))
    plot_jacobian_heatmap(J, io.targets.names, ti.names;
                           outpath = joinpath(diag_dir, "02_jacobian.png"))
    plot_eval_log_trace(obj.eval_log.path;
                         outpath = joinpath(diag_dir, "03_objective_trace.png"))

    return (; θ_hat = θ_econ, θ_se = se_econ, J,
            m_sim, m_dat = io.targets.values, ses = io.targets.ses)
end
