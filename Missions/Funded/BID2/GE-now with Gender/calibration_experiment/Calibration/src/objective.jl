################################################################################
#  objective.jl
#
#  SMM objective wrapper around the PE solver and the moment functions.
#
#  Mathematical form (modelwithgender.tex eq. smm_objective, restricted to the
#  6 moments we keep in PE):
#
#       Q(Θ) = [m^sim(Θ) - m^dat]' W [m^sim(Θ) - m^dat]
#
#  with W diagonal, W_ii = 1 / SE_i^2  (entries from targets.csv).
#
#  Bounds enforcement: parameters are stored unconstrained (`x` vector) and
#  mapped to economic values via per-parameter transforms (log / logit /
#  identity) declared in theta_init.csv.
#
#  Failure-safe wrapper: if `solve_pe_at!` throws or any moment is non-finite,
#  the objective returns 1e10 — the Nelder-Mead simplex moves elsewhere.
#  Each evaluation is appended to `outputs/eval_log.csv` for inspection.
#
#  Requires: pe_solver_for_smm.jl, moments.jl, load_inputs.jl already included.
################################################################################

# ─── Bounds-respecting parameter transforms ─────────────────────────────────
"""
    to_unconstrained(θ_econ, lb, ub, transform) -> Float64

Map an economic parameter value to the unconstrained x-coordinate Nelder-Mead
optimizes over. Inverse of `from_unconstrained`.

transform ∈ (:log, :logit, :identity):
    :log      — for strictly-positive params, lb expected to be > 0
    :logit    — for (lb, ub)-bounded params; x = log((θ-lb)/(ub-θ))
    :identity — no transform; param can be unbounded
"""
function to_unconstrained(θ::Float64, lb::Float64, ub::Float64, t::Symbol)
    if t === :log
        θ > 0 || error("log-transform requires θ > 0; got θ = $θ")
        return log(θ)
    elseif t === :logit
        (θ > lb) && (θ < ub) || error("logit-transform requires lb < θ < ub; got θ = $θ ∈ [$lb, $ub]")
        return log((θ - lb) / (ub - θ))
    elseif t === :identity
        return θ
    else
        error("unknown transform: $t")
    end
end

"""
    from_unconstrained(x, lb, ub, transform) -> Float64

Inverse of `to_unconstrained`. Always returns a value in [lb, ub] (logit) or
(0, ∞) (log) or (-∞, ∞) (identity); no clamping needed.
"""
function from_unconstrained(x::Float64, lb::Float64, ub::Float64, t::Symbol)
    if t === :log
        return exp(x)
    elseif t === :logit
        z = exp(x)
        return lb + (ub - lb) * z / (1.0 + z)
    elseif t === :identity
        return x
    else
        error("unknown transform: $t")
    end
end

# Vector versions
function vec_to_unconstrained(θ_vec::Vector{Float64}, ti::NamedTuple)
    return [to_unconstrained(θ_vec[i], ti.lb[i], ti.ub[i], ti.transform[i])
            for i in eachindex(θ_vec)]
end
function vec_from_unconstrained(x_vec::Vector{Float64}, ti::NamedTuple)
    return [from_unconstrained(x_vec[i], ti.lb[i], ti.ub[i], ti.transform[i])
            for i in eachindex(x_vec)]
end

# ─── Build a θ NamedTuple from a vector in the order of theta_init.names ────
function theta_nt_from_vector(θ_vec::Vector{Float64}, ti::NamedTuple)
    @assert length(θ_vec) == length(ti.names)
    # The PE solver's apply_theta! expects fields (Ψ, Ξ, ξ, H_0, h_slope, ζ_h);
    # theta_init.csv's `param` column carries the same six names.
    name_to_field = Dict("Psi" => :Ψ, "Xi" => :Ξ, "xi" => :ξ,
                          "H_0" => :H_0, "h_slope" => :h_slope, "zeta_h" => :ζ_h)
    pairs = Pair{Symbol,Float64}[]
    for (i, n) in enumerate(ti.names)
        haskey(name_to_field, n) || error("theta_init.csv has unknown param name '$n'")
        push!(pairs, name_to_field[n] => θ_vec[i])
    end
    return NamedTuple(pairs)
end

# ─── Weighted-distance objective ────────────────────────────────────────────
"""
    smm_distance(m_sim_vec, m_dat_vec, ses) -> Float64

(m_sim - m_dat)' W (m_sim - m_dat) with W = diag(1 / ses^2). Robust to NaN —
returns 1e10 if any simulated moment is non-finite.
"""
function smm_distance(m_sim_vec::Vector{Float64},
                       m_dat_vec::Vector{Float64},
                       ses::Vector{Float64})
    @assert length(m_sim_vec) == length(m_dat_vec) == length(ses)
    any(!isfinite, m_sim_vec) && return 1e10
    Q = 0.0
    for i in eachindex(m_sim_vec)
        d = m_sim_vec[i] - m_dat_vec[i]
        Q += (d * d) / (ses[i] * ses[i])
    end
    return Q
end

# ─── Eval log: append a row each evaluation ─────────────────────────────────
mutable struct EvalLog
    path::String
    n::Ref{Int}
end

function open_eval_log(path::String, ti::NamedTuple, target_names::Vector{String})
    mkpath(dirname(path))
    open(path, "w") do io
        params = join(ti.names, ",")
        moms   = join(target_names, ",")
        println(io, "eval_idx,objective,$(params),$(moms),wall_seconds,status")
    end
    return EvalLog(path, Ref(0))
end

function log_eval!(log::EvalLog, θ_vec::Vector{Float64}, m_sim::Vector{Float64},
                    Q::Float64, secs::Float64, status::String)
    log.n[] += 1
    open(log.path, "a") do io
        θ_str = join((@sprintf("%.8g", x) for x in θ_vec), ",")
        m_str = join((@sprintf("%.8g", x) for x in m_sim), ",")
        println(io, "$(log.n[]),$(Q),$(θ_str),$(m_str),$(secs),$(status)")
    end
end

# ─── The objective callable ─────────────────────────────────────────────────
"""
    SmmObjective(io, eval_log; verify=false)

A callable struct: `obj(x)` takes an unconstrained vector `x`, transforms it
to economic params, runs `solve_pe_at!`, computes the six moments, returns
the weighted distance, and appends a row to `eval_log`. Errors during the PE
solve return Q = 1e10 with status = "PE_ERROR".
"""
mutable struct SmmObjective
    io          ::NamedTuple
    eval_log    ::EvalLog
    verify      ::Bool
    target_vec  ::Vector{Float64}
    target_ses  ::Vector{Float64}
    target_names::Vector{String}
end

function SmmObjective(io::NamedTuple, eval_log::EvalLog; verify::Bool=false)
    return SmmObjective(io, eval_log, verify,
                        copy(io.targets.values),
                        copy(io.targets.ses),
                        copy(io.targets.names))
end

# Make it callable
function (obj::SmmObjective)(x::Vector{Float64})
    t0 = time()
    # Transform x → economic params → NamedTuple in apply_theta! field order
    θ_econ = vec_from_unconstrained(x, obj.io.theta_init)
    θ_nt   = theta_nt_from_vector(θ_econ, obj.io.theta_init)

    Q       = 1e10
    m_sim   = fill(NaN, length(obj.target_names))
    status  = "OK"
    try
        solve_pe_at!(θ_nt, obj.io.anchor, obj.io.first_step; verify=obj.verify)
        m_nt = compute_moments(obj.io.usd_scale)
        m_sim = moments_vector(m_nt, obj.target_names)
        Q = smm_distance(m_sim, obj.target_vec, obj.target_ses)
    catch e
        status = "ERROR: $(typeof(e))"
    end
    secs = time() - t0
    log_eval!(obj.eval_log, θ_econ, m_sim, Q, secs, status)
    return Q
end
