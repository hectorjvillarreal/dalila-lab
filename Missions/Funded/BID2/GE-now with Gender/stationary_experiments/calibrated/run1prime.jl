################################################################################
# run1prime.jl — Harmonized calibrated 2020 baseline (CC_instrucciones_runs_2to4.md §2)
#
# Supersedes the gate's run1.jl. Identical calibrated SMM scalars + Milo e_age +
# θ_grid, but ALSO re-anchors the three first-step inputs the SMM saw at the PE
# anchor and that gate Run 1 deliberately held at the GE solver's 2020 stubs:
#
#   • ρ_AR  : 0.98  → 0.782   (inputs_mxdata/first_step/ar1_params.csv)
#   • σ_ε   : 0.05  → 0.265   (inputs_mxdata/first_step/ar1_params.csv)
#   • π_birth: symmetric 0.25 → INEGI asymmetric (pi_birth.csv):
#       M-low 0.3927  M-high 0.1173  F-low 0.3822  F-high 0.1078  (sums to 1)
#
# Closure, demographics, and all other primitives are unchanged from run1.jl:
# joint closure (τp endogenous via PAYG, B residual), 2020 demographics.
#
# This driver does NOT edit ge_model_gender.jl. Override mechanics:
#
#   • ρ_AR, σ_ε are `const` SCALARS (ge_model_gender.jl:46-47), consumed only at
#     the rouwenhorst() call. Julia INLINES const scalars into compiled methods,
#     so a const-redef would silently not propagate (the 1.x trap). We therefore
#     write the harmonized values as LITERALS directly into the rouwenhorst call
#     in init_model! below — no const read, no inlining hazard, contained to the
#     driver. The log echoes ρ=0.782, σ=0.265 to confirm the chain rebuilt.
#   • π_birth is a `const` ARRAY (ge_model_gender.jl:89); array element reads are
#     NOT inlined, so in-place mutation propagates without recompilation —
#     identical idiom to the e_age / θ_grid overrides inherited from run1.jl.
#   • 6 SMM scalars + e_age + θ_grid: same override pattern as run1.jl.
#
# Gate anchor: gate Run 1 K = 10.488 (results/run1_summary.csv). Check #7 below
# reports ΔK and flags if |ΔK| > 15% (§2 / §7 decision point).
#
# Outputs (stationary_experiments/calibrated/results/):
#   run1prime_summary.csv, run1prime_welfare.csv, run1prime_lifecycle.csv
#   (+ run1prime.log via shell)
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

# ── Harmonized first-step AR(1) inputs (inputs_mxdata/first_step/ar1_params.csv)
const RHO_AR_CAL = 0.782        # ρ_AR  (PE-anchor; GE stub was 0.98)
const SIGMA_EPS_CAL = 0.265     # σ_ε   (PE-anchor; GE stub was 0.05)

# ── First-step ENOE inputs (inputs_mxdata/first_step) ─────────────────────────
# e_age 2×J: row 1 male, row 2 female (Milo ENOE; female is the genuine profile,
# NOT a flat 0.85 multiple). Bands 10–17 are zero (retirement). θ_L,θ_H ∓0.3726.
const E_AGE_MALE = [1.0000, 1.2718, 1.3665, 1.3941, 1.4904, 1.5084, 1.4335,
                    1.3469, 1.2277, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
const E_AGE_FEM  = [0.8350, 0.9726, 1.0615, 1.0268, 1.0755, 1.1222, 1.0945,
                    1.0331, 0.8640, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
const THETA_L_CAL = -0.3726
const THETA_H_CAL =  0.3726

# ── Harmonized birth shares π^{g,θ} (inputs_mxdata/first_step/pi_birth.csv) ────
# INEGI Census asymmetric set, indexed [ig, iθ]: ig 1=male 2=female, iθ 1=θ_L 2=θ_H.
const PI_BIRTH_CAL = [0.3927 0.1173;   # row 1: male  (θ_L, θ_H)
                      0.3822 0.1078]   # row 2: female(θ_L, θ_H)

function apply_calibration!()
    @assert length(E_AGE_MALE) == J "E_AGE_MALE length $(length(E_AGE_MALE)) ≠ J=$J"
    @assert length(E_AGE_FEM)  == J "E_AGE_FEM length $(length(E_AGE_FEM)) ≠ J=$J"
    @assert abs(sum(PI_BIRTH_CAL) - 1.0) < 1e-9 "π_birth must sum to 1, got $(sum(PI_BIRTH_CAL))"

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

    # --- (c) HARMONIZATION: mutate π_birth in place to the INEGI asymmetric set
    for ig in 1:Ng, iθ in 1:Nθ
        π_birth[ig, iθ] = PI_BIRTH_CAL[ig, iθ]
    end
    return nothing
end

# ── Grid + Markov-chain init (ge_model_gender.jl::main does this; we bypass
#    main() via the include guard, so replicate it — cf. run_aging_ssvs.jl). ───
#    HARMONIZATION: rouwenhorst is called with LITERAL ρ=0.782, σ=0.265 (NOT the
#    const ρ_AR/σ_ε globals, which inline to the 0.98/0.05 stubs). This rebuilds
#    the discretized productivity chain at the PE-anchor persistence/variance.
function init_model!()
    println("\nInitializing grids and Rouwenhorst chain …")
    @printf "  HARMONIZED AR(1): rebuilding Rouwenhorst chain with ρ=%.4f σ_ε=%.4f (stubs were ρ=%.2f σ_ε=%.2f)\n" RHO_AR_CAL SIGMA_EPS_CAL ρ_AR σ_ε
    grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
    grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
    π_mat, η_vec = rouwenhorst(Nη, RHO_AR_CAL, SIGMA_EPS_CAL, 0.0)
    π_η .= π_mat
    η_grid .= η_vec
    compute_ergodic!()
    @printf "  CHECK η_grid range = [%.4f, %.4f]  (wider with σ_ε=0.265 than the 0.05 stub)\n" minimum(η_grid) maximum(η_grid)
    return nothing
end

# ── Output writers ────────────────────────────────────────────────────────────
function write_summary(K, L, Y, C, M, A_dom)
    r_annual = ((1.0 + r_now)^0.2 - 1.0) * 100
    B   = B_debt_now
    dep = N_R_now / N_W_now
    path = joinpath(RESULTS_DIR, "run1prime_summary.csv")
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
    path = joinpath(RESULTS_DIR, "run1prime_welfare.csv")
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
    path = joinpath(RESULTS_DIR, "run1prime_lifecycle.csv")
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
const GATE_RUN1_K = 10.488013   # gate Run 1 K (results/run1_summary.csv), §2 check #7 anchor

function main()
    println("="^72)
    println("  RUN 1' — Harmonized calibrated 2020 baseline (runs 2-4 sequence)")
    println("="^72)
    println("  Source     : $GE_SRC")
    println("  J=$J  gender_gap=$gender_gap  threads=$(Threads.nthreads())")
    @printf "  Calibrated : Ψ=%.6f Ξ=%.6f ξ=%.4f H̄₀=%.6f h_slope=%.6f ζ_h=%.6f\n" PSI_CAL XI_CAL XICURV_CAL H0_CAL HSLOPE_CAL ZETAH_CAL
    @printf "  θ_L=%.4f θ_H=%.4f  e_age: Milo ENOE 2×J (female genuine profile)\n" THETA_L_CAL THETA_H_CAL
    @printf "  Harmonized : ρ_AR=%.4f σ_ε=%.4f  π_birth=[%.4f %.4f; %.4f %.4f] (INEGI asym)\n" RHO_AR_CAL SIGMA_EPS_CAL PI_BIRTH_CAL[1,1] PI_BIRTH_CAL[1,2] PI_BIRTH_CAL[2,1] PI_BIRTH_CAL[2,2]

    apply_calibration!()
    init_model!()

    # Sanity echo of what the overrides actually installed.
    @printf "  CHECK e_age[1,1:3]=%.4f,%.4f,%.4f  e_age[2,1:3]=%.4f,%.4f,%.4f\n" e_age[1,1] e_age[1,2] e_age[1,3] e_age[2,1] e_age[2,2] e_age[2,3]
    @printf "  CHECK θ_grid=%.4f,%.4f\n" θ_grid[1] θ_grid[2]
    @printf "  CHECK π_birth=[%.4f %.4f; %.4f %.4f]  sum=%.6f\n" π_birth[1,1] π_birth[1,2] π_birth[2,1] π_birth[2,2] sum(π_birth)
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

    # Gate summary (§5 checks 1-4, §2 check 7)
    println("\n", "="^72)
    println("  RUN 1' GATE SUMMARY")
    println("="^72)
    @printf "  [1] goods DIFF/Y          = %+.3e   (gate < 1e-3)   %s\n" DIFF (abs(DIFF) < 1e-3 ? "PASS" : "FAIL")
    @printf "  [2] capital |K-(A-B)|/K   = %.3e    (gate < 2e-4)   %s\n" cap_resid (cap_resid < 2e-4 ? "PASS" : "FAIL")
    @printf "  [3] Euler max log10       = %.3f      (gate < -3, mass-bulk)  mean=%.3f\n" eulmax eulmean
    wgapL = abs(W[1,1] - W[2,1]) / max(abs(W[1,1]), 1e-12) * 100
    @printf "  [4] two-sex W gap (θ_L)   = %.2f%%     (M≠F)  M=%.4f F=%.4f\n" wgapL W[1,1] W[2,1]
    @printf "  [5] τp                    = %.4f      (joint closure; gate Run 1 was 0.1083)\n" τp_now
    ΔK_pct = (K - GATE_RUN1_K) / GATE_RUN1_K * 100
    @printf "  [7] K                     = %.4f      (gate Run 1 K=%.3f, ΔK=%+.2f%%) %s\n" K GATE_RUN1_K ΔK_pct (abs(ΔK_pct) > 15.0 ? "*** |ΔK|>15%: HARMONIZATION MATERIAL — see §7 ***" : "(within 15%)")
    @printf "      dep_ratio=%.4f  Y=%.4f  r_ann=%.3f%%  B/Y=%.4f  w=%.4f  pen=%.4f\n" dep Y r_annual (B_debt_now/Y) w_now pen_now

    @printf "\n  GE iterations: %d (itermax=%d)   final DIFF/Y=%+.3e\n" hist.iter[end] itermax_ge DIFF
    if any(!isfinite, (K, L, Y, C, M))
        println("  *** NaN/Inf in aggregates — STOP, do not proceed to Runs 2-4. ***")
    end
    println("\nRUN 1' done.")
    return nothing
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
