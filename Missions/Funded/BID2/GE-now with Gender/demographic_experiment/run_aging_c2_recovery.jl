################################################################################
# run_aging_c2_recovery.jl
#
# Recover RUN 3 (C2 closure: 2050 demographics, τp pinned at 2020).
#
# The spec said "B absorbs". Two interpretations:
#   (1) Pension benefits stay at calibrated rate (pen = κ·w·L/N^W);
#       deficit flows into general budget; B absorbs. NO FINITE SS at
#       2050 calibration — see C2_interp1_no_finite_SS.md.
#   (2) Pension benefits scale to balance PAYG at the pinned τp
#       (pen = τp·w·L/N^R); retirees absorb. This is what this script
#       implements. Clean SS, headline number for the seminar table.
#
# Implementation notes:
#   - run_aging_ssvs.jl's first attempt silently kept the :endogenous
#     update_pension_taxes! because Julia 1.x method-dispatch caching
#     didn't pick up the :fixed redefinition inside the already-compiled
#     solve_ge! call site. Fix: wrap solve_ge! in Base.invokelatest,
#     which forces a fresh world-age lookup for every callee.
#   - Pre-baked from the prior full-run log:
#       τp_2020 = 0.145002   (from RUN 1's converged equilibrium)
#       B_2020  = 6.9354     (would be the C3 pin)
#
# Wall budget: ~2-3 h threaded.
#
# Outputs: results/aging_c2_recovery_gap.csv  +  console log.
################################################################################

using Printf, Statistics

const GE_SRC      = joinpath(@__DIR__, "..", "ge_model_gender.jl")
const DEMOG_2050  = joinpath(@__DIR__, "demographics_2050.jl")
const RESULTS_DIR = joinpath(@__DIR__, "results")

include(GE_SRC)
include(DEMOG_2050)
isdir(RESULTS_DIR) || mkpath(RESULTS_DIR)

@assert gender_gap "gender_gap must be true (matches the prior runs to combine with)"

# ── Pre-baked from the prior full-run log ───────────────────────────────────
const τp_2020 = 0.145002

# ── active_τω shim (same as run_aging_ssvs.jl) ──────────────────────────────
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

# ── Pension closure: :fixed at τp_2020 with BENEFIT SCALING ─────────────────
# Interpretation 2 of the spec's "C2": pin τp at the 2020 contribution rate
# AND scale benefits to balance PAYG at that contribution rate. With pinned
# τp, pension contributions per worker = τp · w · L_eff, so per-retiree
# benefits become pen = τp · w · L_eff / N_R (instead of the calibrated
# κ · w · L / N^W). Aging incidence falls on retirees as a benefit cut.
#
# Interpretation 1 (debt absorbs the deficit; κ unchanged, B funds gap)
# was tried first and admits no finite steady state at 2050 demographics
# under our calibration — see C2_interp1_no_finite_SS.md.
@eval Main begin
    function update_pension_taxes!(L_eff::Float64)
        global τp_now, pen_now, wn_now
        τp_now = $(τp_2020)
        if N_R_now > 0.0
            pen_now = τp_now * w_now * L_eff / N_R_now
        end
        wn_now = w_now * (1.0 - active_τω[] - τp_now)
    end
end

# ── Debt closure: :residual_B (original spec) ───────────────────────────────
# With the benefit-scaling update_pension_taxes! above, PAYG balances at
# the pinned τp by construction (pen scales to absorb the shortfall via
# retirees, not general budget). The general-government primary therefore
# does NOT need to carry a pension term, so compute_debt! matches the
# spec's default exactly.
active_τω[] = τw
@eval Main begin
    function compute_debt!(C::Float64, L::Float64, K::Float64,
                           M::Float64, Y::Float64)
        global B_debt_now
        G = gy * Y
        primary = τc*C + τw*w_now*L + τk*r_now*K + τm*M - G
        B_debt_now = primary / (rn_now - n_p)
    end
end

# ── Grid + Markov init (same as run_aging_ssvs.jl main()) ───────────────────
println("="^72)
println("  C2 recovery (interp 2: benefit-scaling)")
println("  2050 demographics, τp pinned at 2020 = $(τp_2020)")
println("  pen = τp·w·L/N^R  (benefits scale to balance PAYG)")
println("="^72)
@printf "  nthreads = %d   J = %d   damp_ge = %.2f\n" Threads.nthreads() J damp_ge

println("\nInitializing grids and Rouwenhorst chain …")
grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
π_mat, η_vec = rouwenhorst(Nη, ρ_AR, σ_ε, 0.0)
π_η .= π_mat
η_grid .= η_vec
compute_ergodic!()

# ── Override demographics to 2050 ───────────────────────────────────────────
println("Setting 2050 demographics (Anne / WPP 2024 medium variant) …")
new_ψ = vcat(reshape(Float64.(ψ_base_male_2050),   1, :),
             reshape(Float64.(ψ_base_female_2050), 1, :))
setglobal!(Main, :n_p, n_p_2050)
setglobal!(Main, :ψ_base, new_ψ)
@printf "  n_p  : %.6f → %.6f\n" 0.051010 n_p_2050
@printf "  ψ_male[10] : %.4f → %.4f  ψ_female[10] : %.4f → %.4f\n" 0.95530594 ψ_base_male_2050[10] 0.95530594 ψ_base_female_2050[10]

# ── Solve! ─────────────────────────────────────────────────────────────────
# Base.invokelatest forces the most-recent method lookup for update_pension_taxes!
# and compute_debt! inside solve_ge!. Without it, solve_ge!'s already-compiled
# call sites would bind to the previously-cached :endogenous methods.
println("\n", "="^72)
println("  Solving GE — Base.invokelatest forces fresh world-age dispatch")
println("="^72)
t0 = time()
hist, A_dom, L_new, C, M, Λvoid, Y, K, L = Base.invokelatest(solve_ge!)
solve_min = (time() - t0) / 60
@printf "\nsolve_ge! wall: %.1f min\n" solve_min

# Welfare + residuals
W = welfare_at_birth()
res = euler_residual_stats()
eulmax = isempty(res) ? -Inf : maximum(log10.(max.(res, 1e-16)))
r_annual = ((1.0 + r_now)^0.2 - 1.0) * 100
reportable = abs(hist.DIFF[end]) < 1e-3 && eulmax < -3.0

# Pin check
τp_drift = abs(τp_now - τp_2020)

println("\n", "="^72)
println("  RESULT — RUN 3 · C2 (2050, τp pinned at $(τp_2020))")
println("="^72)
@printf "  K        = %.4f\n"   K
@printf "  L        = %.4f\n"   L
@printf "  Y        = %.4f\n"   Y
@printf "  r (ann)  = %.4f%%\n" r_annual
@printf "  w        = %.4f\n"   w_now
@printf "  τp       = %.6f      (pin = %.6f, drift = %.3e)\n" τp_now τp_2020 τp_drift
@printf "  τω       = %.4f\n"   active_τω[]
@printf "  B        = %.4f      B/Y = %.4f\n" B_debt_now (B_debt_now / Y)
@printf "  C/Y      = %.4f      M/Y = %.4f\n" (C/Y) (M/Y)
@printf "  N_W      = %.4f      N_R = %.4f      dep ratio = %.4f\n" N_W_now N_R_now (N_R_now/N_W_now)
@printf "  DIFF/Y   = %+.3e   Euler max log10 = %.2f   reportable = %s\n" hist.DIFF[end] eulmax reportable
@printf "  Welfare W₁(g,θ): M_θL=%.4f  M_θH=%.4f  F_θL=%.4f  F_θH=%.4f\n" W[1,1] W[1,2] W[2,1] W[2,2]

if τp_drift > 1e-6
    @error "τp pin FAILED — drift = $(τp_drift) > 1e-6. invokelatest didn't fix the dispatch."
end

# ── Write C2-only CSV (combine manually with the prior log) ─────────────────
csv_path = joinpath(RESULTS_DIR, "aging_c2_recovery_gap.csv")
open(csv_path, "w") do io
    println(io, "label,K,L,Y,r_annual_pct,w,taup,tauomega,B,B_over_Y," *
                "C_over_Y,M_over_Y,N_W,N_R,depratio," *
                "W_MthetaL,W_MthetaH,W_FthetaL,W_FthetaH," *
                "DIFF_over_Y,euler_max_log10,reportable")
    @printf(io, "RUN 3 · 2050 C2 (recovery),%.6f,%.6f,%.6f,%.5f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.3e,%.3f,%s\n",
        K, L, Y, r_annual, w_now,
        τp_now, active_τω[], B_debt_now, B_debt_now / Y,
        C / Y, M / Y,
        N_W_now, N_R_now, N_R_now / N_W_now,
        W[1,1], W[1,2], W[2,1], W[2,2],
        hist.DIFF[end], eulmax, reportable)
end
println("\nWrote $(csv_path)")
println("Done.")
