################################################################################
# recover_welfare_all.jl
#
# Capture welfare W₁(g, θ) at the already-known equilibria of RUN 1, C1, C2
# WITHOUT re-running the full GE outer loop. Idea: at each scenario's
# converged (K, L), the firm FOC pins (r, w); a few inner-loop iters of
# solve_household + forward_distribution + update_pension_taxes! lock τp/pen
# to their self-consistent values; then welfare_at_birth() reads V_pol.
#
# Cost: ~3 solve_household calls per scenario × 3 scenarios = ~50 min wall
# (vs ~7.5 h for a full 3-scenario re-run). The K, L, τp, B/Y values we
# already have from the prior logs are taken as given; only welfare-by-sex
# is the new artifact this script produces.
#
# Output:
#   results/aging_comparison_gap.csv      one row per scenario (RUN 1 / C1 / C2)
#   results/welfare_panel_gap.png         2×2 grouped bar chart, W₁ by (g, θ)
#                                          across scenarios
#   results/recover_welfare_all.log       captured via tee at the call site
################################################################################

using Printf, Statistics, Plots
gr()

const GE_SRC      = joinpath(@__DIR__, "..", "ge_model_gender.jl")
const DEMOG_2050  = joinpath(@__DIR__, "demographics_2050.jl")
const RESULTS_DIR = joinpath(@__DIR__, "results")

include(GE_SRC)
include(DEMOG_2050)
isdir(RESULTS_DIR) || mkpath(RESULTS_DIR)

@assert gender_gap "gender_gap must be true (to match prior runs)"

# ─── active_τω shim + household function redefs (same as run_aging_ssvs.jl) ──
const active_τω = Ref{Float64}(τw)

@eval Main begin
    function labor_supply(j::Int, h::Float64, η::Float64,
                          ig::Int, iθ::Int)::Float64
        if j >= j_R; return 0.0; end
        ν_j = productivity(j, h, η, ig, iθ)
        ν_j <= 0.0 && return 0.0
        numer = w_now * ν_j * (1.0 - active_τω[] - τp_now)
        denom = (1.0 + τc) * Ψ_labor
        ℓ_star = (numer / denom) ^ (1.0 / ν_pref)
        return clamp(ℓ_star, 0.0, 1.0)
    end

    function available_resources(a::Float64, h::Float64, η::Float64,
                                  ig::Int, iθ::Int, j::Int)::Float64
        if j < j_R
            ℓ   = labor_supply(j, h, η, ig, iθ)
            ν_j = productivity(j, h, η, ig, iθ)
            labor_income = w_now * ν_j * ℓ * (1.0 - active_τω[] - τp_now)
            return (1.0 + rn_now) * a + labor_income
        else
            return (1.0 + rn_now) * a + pen_now
        end
    end
end
active_τω[] = τw

# ─── Pension closures ───────────────────────────────────────────────────────
function set_pension_endogenous!()
    @eval Main begin
        function update_pension_taxes!(L_eff::Float64)
            global τp_now, pen_now, wn_now
            if N_W_now > 0.0
                τp_now  = κ_rep * N_R_now / N_W_now
                pen_now = κ_rep * w_now * L_eff / N_W_now
            end
            wn_now = w_now * (1.0 - active_τω[] - τp_now)
        end
    end
end

function set_pension_fixed_scaled!(τp_pin::Float64)
    @eval Main begin
        function update_pension_taxes!(L_eff::Float64)
            global τp_now, pen_now, wn_now
            τp_now = $(τp_pin)
            if N_R_now > 0.0
                pen_now = τp_now * w_now * L_eff / N_R_now   # benefit-scaling
            end
            wn_now = w_now * (1.0 - active_τω[] - τp_now)
        end
    end
end

# ─── Grid + Markov init (always run once) ───────────────────────────────────
println("="^72)
println("  Welfare recovery (option 3) — 3 scenarios at known equilibria")
println("="^72)
@printf "  nthreads = %d   J = %d\n" Threads.nthreads() J

println("\nInitializing grids and Rouwenhorst chain …")
grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
π_mat, η_vec = rouwenhorst(Nη, ρ_AR, σ_ε, 0.0)
π_η .= π_mat
η_grid .= η_vec
compute_ergodic!()

# ─── Inner-loop equilibrium consolidation at fixed (K, L) ───────────────────
# Run solve_household + forward_distribution + update_pension_taxes! until
# τp/pen stop moving. K, L stay pinned — we trust the prior logs that these
# are the right equilibrium values.
function lock_at_equilibrium!(K::Float64, L::Float64;
                              τp_init::Float64, pen_init::Float64 = 1.0,
                              max_iter::Int = 6, tol::Float64 = 1e-5)
    update_prices!(K, L)
    global τp_now, pen_now, wn_now
    τp_now  = τp_init
    pen_now = pen_init
    wn_now  = w_now * (1.0 - active_τω[] - τp_now)

    for it in 1:max_iter
        old_τp  = τp_now
        old_pen = pen_now

        Base.invokelatest(solve_household!)
        Base.invokelatest(forward_distribution!)
        compute_population!()
        Base.invokelatest(update_pension_taxes!, L)

        Δτp  = abs(τp_now  - old_τp)
        Δpen = abs(pen_now - old_pen)
        @printf "    inner iter %d: τp=%.6f (Δ=%.2e)  pen=%.4f (Δ=%.2e)  N_W=%.4f  N_R=%.4f\n" it τp_now Δτp pen_now Δpen N_W_now N_R_now

        if Δτp < tol && Δpen < tol && it > 1
            println("    → locked")
            return it
        end
    end
    println("    → max_iter reached without tight lock; using current state")
    return max_iter
end

# Compute aggregates + Euler stats at the current state (sanity check).
function snapshot()
    A_dom, L_eff, C, M, Λvoid = aggregate_all()
    Y = A_TFP * (A_dom - B_debt_now)^α * L_eff^(1-α)  # not used; will use known K,L below
    Y_from_K = nothing  # set by caller
    W = welfare_at_birth()
    res = euler_residual_stats()
    eulmax = isempty(res) ? -Inf : maximum(log10.(max.(res, 1e-16)))
    return (A_dom=A_dom, L_eff=L_eff, C=C, M=M, Λvoid=Λvoid, W=W, eulmax=eulmax)
end

# ─── Scenario definitions ────────────────────────────────────────────────────
# Values are from the prior converged runs:
#   RUN 1:    run_aging_ssvs_gap.log  (the attempt-6 successful baseline pass)
#   C1:       run_aging_ssvs_gap.log  (RUN 2 of that attempt)
#   C2:       run_aging_c2_recovery_interp2.log  (the benefit-scaling recovery)
const SCENARIOS = [
    (label = "RUN 1 · 2020 baseline",          demog = :y2020, K = 14.3779, L = 15.8705,
     τp = 0.145002,  pension = :endogenous,                B_log = 6.9354,  r_ann = 4.805),
    (label = "RUN 2 · C1 (2050 joint)",        demog = :y2050, K = 21.0353, L = 20.3878,
     τp = 0.263791,  pension = :endogenous,                B_log = 4.8104,  r_ann = 3.980),
    (label = "RUN 3 · C2 (2050 τp pinned)",    demog = :y2050, K = 27.7031, L = 22.6294,
     τp = 0.145002,  pension = :fixed_scaled,              B_log = 9.8599,  r_ann = 2.958),
]

# Snapshot of pristine 2020 demographics so we can restore between scenarios.
const n_p_2020      = n_p
const ψ_base_2020   = copy(ψ_base)

# ─── Driver loop ─────────────────────────────────────────────────────────────
results = []
for s in SCENARIOS
    println("\n", "="^72)
    println("  ", s.label)
    println("="^72)

    # demographics
    if s.demog === :y2020
        setglobal!(Main, :n_p, n_p_2020)
        setglobal!(Main, :ψ_base, ψ_base_2020)
    elseif s.demog === :y2050
        new_ψ = vcat(reshape(Float64.(ψ_base_male_2050), 1, :),
                     reshape(Float64.(ψ_base_female_2050), 1, :))
        setglobal!(Main, :n_p,    n_p_2050)
        setglobal!(Main, :ψ_base, new_ψ)
    end

    # pension closure
    if s.pension === :endogenous
        set_pension_endogenous!()
        τp_init = s.τp
    elseif s.pension === :fixed_scaled
        set_pension_fixed_scaled!(s.τp)
        τp_init = s.τp
    end

    @printf "  Inputs: K=%.4f  L=%.4f  τp(target)=%.6f  demog=%s  pension=%s\n" s.K s.L s.τp s.demog s.pension

    t0 = time()
    lock_at_equilibrium!(s.K, s.L; τp_init = τp_init)
    snap_min = (time() - t0) / 60
    @printf "  lock_at_equilibrium! wall: %.1f min\n" snap_min

    A_dom, L_eff, C, M, Λvoid = aggregate_all()
    Y = A_TFP * s.K^α * s.L^(1.0 - α)
    W = welfare_at_birth()
    res = euler_residual_stats()
    eulmax = isempty(res) ? -Inf : maximum(log10.(max.(res, 1e-16)))

    # Cross-check: A_dom − B (recomputed) should equal K
    B_check = 0.0  # not recomputing B here; use s.B_log as authoritative
    capital_consistency = abs(A_dom - s.B_log - s.K) / max(abs(s.K), 1e-12)
    @printf "  Aggregates: A_dom=%.4f  L_eff=%.4f  C=%.4f  M=%.4f  Λvoid=%.4f\n" A_dom L_eff C M Λvoid
    @printf "  Welfare W₁(g,θ): M_θL=%.4f  M_θH=%.4f  F_θL=%.4f  F_θH=%.4f\n" W[1,1] W[1,2] W[2,1] W[2,2]
    @printf "  Euler max log10 = %.2f   |A_dom−B−K|/K = %.3e\n" eulmax capital_consistency

    push!(results, (
        label = s.label, K = s.K, L = s.L, Y = Y, r_annual = s.r_ann,
        w = w_now, τp = τp_now, τω = active_τω[],
        B = s.B_log, B_over_Y = s.B_log / Y,
        C_over_Y = C / Y, M_over_Y = M / Y,
        N_W = N_W_now, N_R = N_R_now, depratio = N_R_now / max(N_W_now, 1e-12),
        W_MθL = W[1,1], W_MθH = W[1,2], W_FθL = W[2,1], W_FθH = W[2,2],
        euler_max = eulmax, A_dom = A_dom,
    ))
end

# ─── Write unified CSV ───────────────────────────────────────────────────────
csv_path = joinpath(RESULTS_DIR, "aging_comparison_gap.csv")
open(csv_path, "w") do io
    println(io, "label,K,L,Y,r_annual_pct,w,taup,tauomega,B,B_over_Y," *
                "C_over_Y,M_over_Y,N_W,N_R,depratio," *
                "W_MthetaL,W_MthetaH,W_FthetaL,W_FthetaH,euler_max_log10,A_dom")
    for r in results
        @printf(io, "%s,%.6f,%.6f,%.6f,%.5f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.3f,%.6f\n",
            r.label, r.K, r.L, r.Y, r.r_annual, r.w,
            r.τp, r.τω, r.B, r.B_over_Y, r.C_over_Y, r.M_over_Y,
            r.N_W, r.N_R, r.depratio,
            r.W_MθL, r.W_MθH, r.W_FθL, r.W_FθH,
            r.euler_max, r.A_dom)
    end
end
println("\nWrote $(csv_path)")

# ─── Welfare panel PNG ──────────────────────────────────────────────────────
short_labels = ["RUN 1", "C1", "C2"]
type_labels  = ["M, θL", "M, θH", "F, θL", "F, θH"]
type_getters = [r->r.W_MθL, r->r.W_MθH, r->r.W_FθL, r->r.W_FθH]

panels = []
for (tlabel, getter) in zip(type_labels, type_getters)
    vals = Float64[getter(r) for r in results]
    push!(panels, bar(short_labels, vals;
                      ylabel = "W₁", title = tlabel, label = "",
                      color = :steelblue, legend = false))
end
p = plot(panels...; layout = (2, 2), size = (900, 700),
         plot_title = "Welfare at birth by (sex, skill) — three-column aging comparison",
         plot_titlefontsize = 12)
png_path = joinpath(RESULTS_DIR, "welfare_panel_gap.png")
savefig(p, png_path)
println("Wrote $(png_path)")

println("\nDone.")
