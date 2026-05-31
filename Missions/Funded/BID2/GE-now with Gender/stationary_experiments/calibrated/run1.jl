################################################################################
# run1.jl — Calibrated 2020 baseline (gate sequence, CC_instrucciones_gate_runs.md §2)
#
# Standard stationary GE solve on ge_model_gender.jl at the inputs_mxdata SMM
# estimates. Joint closure: τp endogenous (PAYG balance), B residual.
# Demographics: 2020 baseline (the GE solver's default ψ_base / n_p stubs —
# NOT demographics_2050.jl). See gate doc §2 "Demographics: 2020 baseline".
#
# This driver does NOT edit ge_model_gender.jl. It overrides the calibrated
# parameters at runtime:
#
#   • 6 SMM scalars (Ψ, Ξ, ξ[frozen], H̄₀, h_slope, ζ_h) — these are `const`
#     in the solver and Julia INLINES const scalars into compiled methods, so
#     a bare const-redef would silently not propagate (the known 1.x trap,
#     cf. demographic_experiment RUN-2 first attempt). We instead re-`@eval`
#     the 4 leaf functions that read them with the calibrated values baked in
#     as literals — identical idiom to run_aging_ssvs.jl's closure overrides.
#       - Ψ_labor   → disutility_of_labor, labor_supply
#       - Ξ_amenity, ξ_curv → health_amenity
#       - H_scale (=H̄₀), h_slope, H_curv (=ζ_h) → health_production
#   • e_age (2×J Milo ENOE) and θ_grid (∓0.3726) — these are `const` ARRAYS;
#     array element reads are not inlined, so in-place mutation propagates
#     without recompilation.
#
# Everything else (ψ_base, δh, ρ_AR, σ_ε, π_birth, ϱ_pen, taxes, α, δ, A, κ,
# n_p) is left at the ge_model_gender.jl 2020 values. NOTE: the calibration's
# inputs_mxdata retains ψ_base/δh/π_birth identical to the GE stubs and ϱ_pen
# identical; only ρ_AR (0.782 vs 0.98) and σ_ε (0.265 vs 0.05) and π_birth
# (asymmetric in mxdata) differ — those are first-step inputs the SMM saw at
# PE-anchor but are deliberately NOT propagated here, to keep this run's
# baseline comparable to the v3 symmetric-stub K=14.378 per gate-doc check #6.
# Flagged in gate_notes.md.
#
# Outputs (stationary_experiments/calibrated/results/):
#   run1_summary.csv, run1_welfare.csv, run1_lifecycle.csv  (+ run1.log via shell)
################################################################################

using Printf, Statistics

const HERE        = @__DIR__
const GE_SRC      = abspath(joinpath(HERE, "..", "..", "ge_model_gender.jl"))
const RESULTS_DIR = joinpath(HERE, "results")
const INPUTS_MX   = abspath(joinpath(HERE, "..", "..", "calibration_experiment",
                                     "Calibration", "inputs_mxdata"))
isdir(RESULTS_DIR) || mkpath(RESULTS_DIR)

# `include` pulls the solver into Main without firing its main() (guarded by
# the PROGRAM_FILE check at the bottom of ge_model_gender.jl).
include(GE_SRC)

# ── Calibrated SMM scalars (inputs_mxdata, best of 4 starts, Q = 13.283) ──────
# Verified against outputs/eval_log_multistart_mxdata.csv min-Q row 2026-05-31.
const PSI_CAL    = 13.452490    # Ψ_labor
const XI_CAL     = 0.274472     # Ξ_amenity
const XICURV_CAL = 0.500000     # ξ_curv (frozen at literature value)
const H0_CAL     = 0.247474     # H_scale  (H̄₀)
const HSLOPE_CAL = -0.035807    # h_slope
const ZETAH_CAL  = 0.579138     # H_curv   (ζ_h)

# ── First-step ENOE inputs (inputs_mxdata/first_step) ─────────────────────────
# e_age 2×J: row 1 male, row 2 female (Milo ENOE; female is the genuine profile,
# NOT a flat 0.85 multiple). Bands 10–17 are zero (retirement). θ_L,θ_H ∓0.3726.
const E_AGE_MALE = [1.0000, 1.2718, 1.3665, 1.3941, 1.4904, 1.5084, 1.4335,
                    1.3469, 1.2277, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
const E_AGE_FEM  = [0.8350, 0.9726, 1.0615, 1.0268, 1.0755, 1.1222, 1.0945,
                    1.0331, 0.8640, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
const THETA_L_CAL = -0.3726
const THETA_H_CAL =  0.3726

function apply_calibration!()
    @assert length(E_AGE_MALE) == J "E_AGE_MALE length $(length(E_AGE_MALE)) ≠ J=$J"
    @assert length(E_AGE_FEM)  == J "E_AGE_FEM length $(length(E_AGE_FEM)) ≠ J=$J"

    # --- (a) override the 6 const scalars by re-eval'ing their reader functions
    #         with calibrated values as literals (defeats const-inlining trap) ---
    @eval Main begin
        function health_amenity(h::Float64)::Float64
            h_safe = max(h, 1e-12)
            if abs($XICURV_CAL - 1.0) < 1e-10
                return $XI_CAL * log(h_safe)
            else
                return $XI_CAL * h_safe^(1.0 - $XICURV_CAL) / (1.0 - $XICURV_CAL)
            end
        end

        disutility_of_labor(ℓ::Float64)::Float64 =
            $PSI_CAL * ℓ^(1.0 + ν_pref) / (1.0 + ν_pref)

        function labor_supply(j::Int, h::Float64, η::Float64, ig::Int, iθ::Int)::Float64
            if j >= j_R
                return 0.0
            end
            ν_j = productivity(j, h, η, ig, iθ)
            if ν_j <= 0.0
                return 0.0
            end
            numer = w_now * ν_j * (1.0 - τw - τp_now)
            denom = (1.0 + τc) * $PSI_CAL
            ℓ_star = (numer / denom) ^ (1.0 / ν_pref)
            return clamp(ℓ_star, 0.0, 1.0)
        end

        function health_production(m::Float64, j::Int)::Float64
            if m <= 0.0
                return 0.0
            end
            H_j = $H0_CAL * exp(-$HSLOPE_CAL * j)
            return H_j * m^$ZETAH_CAL
        end
    end

    # --- (b) mutate the const ARRAYS in place (reads aren't inlined) ---
    for j in 1:J
        e_age[1, j] = E_AGE_MALE[j]
        e_age[2, j] = E_AGE_FEM[j]
    end
    θ_grid[1] = THETA_L_CAL
    θ_grid[2] = THETA_H_CAL
    return nothing
end

# ── Grid + Markov-chain init (ge_model_gender.jl::main does this; we bypass
#    main() via the include guard, so replicate it — cf. run_aging_ssvs.jl). ───
function init_model!()
    println("\nInitializing grids and Rouwenhorst chain …")
    grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
    grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
    π_mat, η_vec = rouwenhorst(Nη, ρ_AR, σ_ε, 0.0)
    π_η .= π_mat
    η_grid .= η_vec
    compute_ergodic!()
    return nothing
end

# ── Output writers ────────────────────────────────────────────────────────────
function write_summary(K, L, Y, C, M, A_dom)
    r_annual = ((1.0 + r_now)^0.2 - 1.0) * 100
    B   = B_debt_now
    dep = N_R_now / N_W_now
    path = joinpath(RESULTS_DIR, "run1_summary.csv")
    open(path, "w") do io
        println(io, "metric,value")
        @printf(io, "K,%.6f\n", K)
        @printf(io, "L,%.6f\n", L)
        @printf(io, "Y,%.6f\n", Y)
        @printf(io, "r_annual_pct,%.6f\n", r_annual)
        @printf(io, "r_5yr,%.6f\n", r_now)
        @printf(io, "w,%.6f\n", w_now)
        @printf(io, "tau_p,%.6f\n", τp_now)
        @printf(io, "pen,%.6f\n", pen_now)
        @printf(io, "B,%.6f\n", B)
        @printf(io, "B_over_Y,%.6f\n", B / Y)
        @printf(io, "C_over_Y,%.6f\n", C / Y)
        @printf(io, "M_over_Y,%.6f\n", M / Y)
        @printf(io, "A_dom,%.6f\n", A_dom)
        @printf(io, "N_W,%.6f\n", N_W_now)
        @printf(io, "N_R,%.6f\n", N_R_now)
        @printf(io, "dep_ratio,%.6f\n", dep)
    end
    println("Wrote $path")
    return r_annual, dep
end

function write_welfare(W)
    path = joinpath(RESULTS_DIR, "run1_welfare.csv")
    open(path, "w") do io
        println(io, "sex,skill,W1")
        @printf(io, "M,theta_L,%.8f\n", W[1, 1])
        @printf(io, "M,theta_H,%.8f\n", W[1, 2])
        @printf(io, "F,theta_L,%.8f\n", W[2, 1])
        @printf(io, "F,theta_H,%.8f\n", W[2, 2])
    end
    println("Wrote $path")
    return nothing
end

function write_lifecycle()
    cm_c, cm_l, cm_a, cm_m, cm_h = cohort_means()
    sexlab  = ["M", "F"]
    skilllab = ["theta_L", "theta_H"]
    path = joinpath(RESULTS_DIR, "run1_lifecycle.csv")
    open(path, "w") do io
        println(io, "sex,skill,age_period,c,l,a,m,h")
        for ig in 1:Ng, iθ in 1:Nθ, j in 1:J
            @printf(io, "%s,%s,%d,%.8f,%.8f,%.8f,%.8f,%.8f\n",
                    sexlab[ig], skilllab[iθ], j,
                    cm_c[j, ig, iθ], cm_l[j, ig, iθ], cm_a[j, ig, iθ],
                    cm_m[j, ig, iθ], cm_h[j, ig, iθ])
        end
    end
    println("Wrote $path")
    return nothing
end

# ── main ──────────────────────────────────────────────────────────────────────
function main()
    println("="^72)
    println("  RUN 1 — Calibrated 2020 baseline (gate sequence)")
    println("="^72)
    println("  Source     : $GE_SRC")
    println("  J=$J  gender_gap=$gender_gap  threads=$(Threads.nthreads())")
    @printf "  Calibrated : Ψ=%.6f Ξ=%.6f ξ=%.4f H̄₀=%.6f h_slope=%.6f ζ_h=%.6f\n" PSI_CAL XI_CAL XICURV_CAL H0_CAL HSLOPE_CAL ZETAH_CAL
    @printf "  θ_L=%.4f θ_H=%.4f  e_age: Milo ENOE 2×J (female genuine profile)\n" THETA_L_CAL THETA_H_CAL

    apply_calibration!()
    init_model!()

    # Sanity echo of what the overrides actually installed.
    @printf "  CHECK e_age[1,1:3]=%.4f,%.4f,%.4f  e_age[2,1:3]=%.4f,%.4f,%.4f\n" e_age[1,1] e_age[1,2] e_age[1,3] e_age[2,1] e_age[2,2] e_age[2,3]
    @printf "  CHECK θ_grid=%.4f,%.4f\n" θ_grid[1] θ_grid[2]
    @printf "  CHECK disutility_of_labor(1.0)=%.6f (= Ψ/(1+ν)=%.6f)\n" Base.invokelatest(disutility_of_labor, 1.0) (PSI_CAL/(1.0+ν_pref))
    @printf "  CHECK health_amenity(1.0)=%.6f (= Ξ/(1-ξ)=%.6f)\n" Base.invokelatest(health_amenity, 1.0) (XI_CAL/(1.0-XICURV_CAL))

    # Joint closure is the ge_model_gender.jl default: update_pension_taxes!
    # (τp = κ N^R/N^W) + compute_debt! (B residual). No closure override needed.
    println("\nSolving GE (joint closure: τp endogenous, B residual) …")
    hist, A_dom, L_new, C, M, Λvoid, Y, K, L = Base.invokelatest(solve_ge!)

    W = Base.invokelatest(welfare_at_birth)

    # Diagnostics
    res = Base.invokelatest(euler_residual_stats)
    eulmax  = isempty(res) ? -Inf : maximum(log10.(max.(res, 1e-16)))
    eulmean = isempty(res) ? -Inf : mean(log10.(max.(res, 1e-16)))
    cap_resid = abs(K - (A_dom - B_debt_now)) / max(abs(K), 1e-12)
    DIFF = hist.DIFF[end]

    r_annual, dep = write_summary(K, L, Y, C, M, A_dom)
    write_welfare(W)
    write_lifecycle()

    # Gate summary (gate doc §4, checks 1-6)
    println("\n", "="^72)
    println("  RUN 1 GATE SUMMARY")
    println("="^72)
    @printf "  [1] goods DIFF/Y          = %+.3e   (gate < 1e-3)   %s\n" DIFF (abs(DIFF) < 1e-3 ? "PASS" : "FAIL")
    @printf "  [2] capital |K-(A-B)|/K   = %.3e    (gate < 2e-4)   %s\n" cap_resid (cap_resid < 2e-4 ? "PASS" : "FAIL")
    @printf "  [3] Euler max log10       = %.3f      (gate < -3, mass-bulk)  mean=%.3f\n" eulmax eulmean
    wgapL = abs(W[1,1] - W[2,1]) / max(abs(W[1,1]), 1e-12) * 100
    @printf "  [4] two-sex W gap (θ_L)   = %.2f%%     (expect 5-10%%, M≠F)  M=%.4f F=%.4f\n" wgapL W[1,1] W[2,1]
    @printf "  [5] τp                    = %.4f      (expect ≈0.1450 = κ·dep)\n" τp_now
    @printf "  [6] K                     = %.4f      (v3 stub baseline 14.378; report Δ)\n" K
    @printf "      dep_ratio=%.4f  Y=%.4f  r_ann=%.3f%%  B/Y=%.4f  w=%.4f  pen=%.4f\n" dep Y r_annual (B_debt_now/Y) w_now pen_now

    converged = (hist.iter[end] < itermax_ge) || (max(abs(DIFF)) < sig_ge)
    @printf "\n  GE iterations: %d (itermax=%d)   final DIFF/Y=%+.3e\n" hist.iter[end] itermax_ge DIFF
    if any(!isfinite, (K, L, Y, C, M))
        println("  *** NaN/Inf in aggregates — STOP, do not proceed to Run 0. ***")
    end
    println("\nRUN 1 done.")
    return nothing
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
