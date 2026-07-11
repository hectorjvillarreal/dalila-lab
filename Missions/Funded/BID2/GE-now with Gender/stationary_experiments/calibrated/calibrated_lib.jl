################################################################################
# calibrated_lib.jl — shared machinery for Runs 2-4 (CC_instrucciones_runs_2to4.md)
#
# Factors the harmonized-baseline setup out of run1prime.jl so Runs 2, 3, 4 are
# thin perturbation drivers. Identical calibration + harmonization as run1prime:
#   • 6 SMM scalars (Ψ, Ξ, ξ frozen, H̄₀, h_slope, ζ_h) via @eval leaf-fn redef
#   • Milo e_age 2×J + θ_grid ∓0.3726 via in-place array mutation
#   • HARMONIZED ρ_AR=0.782, σ_ε=0.265 as LITERALS in the rouwenhorst call
#   • HARMONIZED π_birth INEGI asymmetric via in-place array mutation
#
# Perturbation hooks (each run calls the ones it needs BEFORE run_and_report!):
#   • set_pension_kappa!(κ)  — Run 2 (κ:0.50→0.30). Re-evals update_pension_taxes!
#                              with κ as a literal (const-κ_rep is inlined).
#   • set_demographics!(…)   — Run 4 (2050 aging). Overrides typed globals n_p, ψ_base.
#   • τm (Run 3) is NOT set here — it is a `const` woven through the cell solver,
#     so it must be redefined in the driver via Core.eval BEFORE this lib's
#     init_model!/solve compiles those methods. See run3_taum20.jl.
#
# Default closure is the ge_model_gender.jl joint closure (τp endogenous via
# update_pension_taxes!, B residual via compute_debt!) — this is the C1 closure
# for Run 4 and the baseline closure for Runs 2-3. No closure override needed.
#
# Does NOT edit ge_model_gender.jl.
################################################################################

using Printf, Statistics

const HERE        = @__DIR__
const GE_SRC      = abspath(joinpath(HERE, "..", "..", "ge_model_gender.jl"))
const RESULTS_DIR = joinpath(HERE, "results")
isdir(RESULTS_DIR) || mkpath(RESULTS_DIR)

include(GE_SRC)

# ── Calibrated SMM scalars (inputs_mxdata, best of 4 starts, Q = 13.283) ──────
const PSI_CAL    = 13.452490
const XI_CAL     = 0.274472
const XICURV_CAL = 0.500000
const H0_CAL     = 0.247474
const HSLOPE_CAL = -0.035807
const ZETAH_CAL  = 0.579138

# ── Harmonized first-step inputs (inputs_mxdata/first_step) ───────────────────
const RHO_AR_CAL    = 0.782      # ar1_params.csv (GE stub was 0.98)
const SIGMA_EPS_CAL = 0.265      # ar1_params.csv (GE stub was 0.05)
const E_AGE_MALE = [1.0000, 1.2718, 1.3665, 1.3941, 1.4904, 1.5084, 1.4335,
                    1.3469, 1.2277, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
const E_AGE_FEM  = [0.8350, 0.9726, 1.0615, 1.0268, 1.0755, 1.1222, 1.0945,
                    1.0331, 0.8640, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
const THETA_L_CAL = -0.3726
const THETA_H_CAL =  0.3726
const PI_BIRTH_CAL = [0.3927 0.1173;   # row 1 male  (θ_L, θ_H)  — pi_birth.csv
                      0.3822 0.1078]   # row 2 female(θ_L, θ_H)

# Run 1' baseline anchors (results/run1prime_summary.csv, this session).
const RUN1PRIME_K   = 4.960011
const RUN1PRIME_TAUP = 0.092859

function apply_calibration!()
    @assert length(E_AGE_MALE) == J "E_AGE_MALE length ≠ J=$J"
    @assert length(E_AGE_FEM)  == J "E_AGE_FEM length ≠ J=$J"
    @assert abs(sum(PI_BIRTH_CAL) - 1.0) < 1e-9 "π_birth must sum to 1"
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
            j >= j_R && return 0.0
            ν_j = productivity(j, h, η, ig, iθ)
            ν_j <= 0.0 && return 0.0
            numer = w_now * ν_j * (1.0 - τw - τp_now)
            denom = (1.0 + τc) * $PSI_CAL
            ℓ_star = (numer / denom) ^ (1.0 / ν_pref)
            return clamp(ℓ_star, 0.0, 1.0)
        end
        function health_production(m::Float64, j::Int)::Float64
            m <= 0.0 && return 0.0
            H_j = $H0_CAL * exp(-$HSLOPE_CAL * j)
            return H_j * m^$ZETAH_CAL
        end
    end
    for j in 1:J
        e_age[1, j] = E_AGE_MALE[j]
        e_age[2, j] = E_AGE_FEM[j]
    end
    θ_grid[1] = THETA_L_CAL
    θ_grid[2] = THETA_H_CAL
    for ig in 1:Ng, iθ in 1:Nθ
        π_birth[ig, iθ] = PI_BIRTH_CAL[ig, iθ]
    end
    return nothing
end

# HARMONIZED rouwenhorst: literal ρ=0.782, σ=0.265 (const ρ_AR/σ_ε inline to stubs).
function init_model!()
    println("\nInitializing grids and Rouwenhorst chain …")
    @printf "  HARMONIZED AR(1): ρ=%.4f σ_ε=%.4f (stubs were ρ=%.2f σ_ε=%.2f)\n" RHO_AR_CAL SIGMA_EPS_CAL ρ_AR σ_ε
    grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
    grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
    π_mat, η_vec = rouwenhorst(Nη, RHO_AR_CAL, SIGMA_EPS_CAL, 0.0)
    π_η .= π_mat
    η_grid .= η_vec
    compute_ergodic!()
    @printf "  CHECK η_grid range = [%.4f, %.4f]\n" minimum(η_grid) maximum(η_grid)
    return nothing
end

# ── Perturbation hooks ────────────────────────────────────────────────────────

# Run 2: κ baked as literal (const-κ_rep is inlined into update_pension_taxes!).
function set_pension_kappa!(κ_val::Float64)
    @eval Main begin
        function update_pension_taxes!(L_eff::Float64)
            global τp_now, pen_now, wn_now
            if N_W_now > 0.0
                τp_now  = $(κ_val) * N_R_now / N_W_now
                pen_now = $(κ_val) * w_now * L_eff / N_W_now
            end
            wn_now = w_now * (1.0 - τw - τp_now)
        end
    end
    @printf "  set_pension_kappa!: update_pension_taxes! re-evaled with κ=%.4f\n" κ_val
    return nothing
end

# Run 4: replace typed globals n_p, ψ_base (not inlined) — same as run0.jl.
function set_demographics!(n_p_new, ψ_m_new, ψ_f_new)
    @assert length(ψ_m_new) == J
    @assert length(ψ_f_new) == J
    new_ψ = vcat(reshape(Float64.(collect(ψ_m_new)), 1, :),
                 reshape(Float64.(collect(ψ_f_new)), 1, :))
    setglobal!(Main, :n_p, n_p_new)
    setglobal!(Main, :ψ_base, new_ψ)
    @printf "  set_demographics!: n_p=%.6f  ψ_m[10]=%.4f ψ_f[10]=%.4f\n" n_p ψ_base[1,10] ψ_base[2,10]
    return nothing
end

# ── Output writers (parameterized by run tag → no rename errors) ──────────────
function write_summary(tag, K, L, Y, C, M, A_dom)
    r_annual = ((1.0 + r_now)^0.2 - 1.0) * 100
    dep = N_R_now / N_W_now
    path = joinpath(RESULTS_DIR, "$(tag)_summary.csv")
    open(path, "w") do io
        println(io, "metric,value")
        @printf(io, "K,%.6f\n", K);              @printf(io, "L,%.6f\n", L)
        @printf(io, "Y,%.6f\n", Y);              @printf(io, "r_annual_pct,%.6f\n", r_annual)
        @printf(io, "r_5yr,%.6f\n", r_now);      @printf(io, "w,%.6f\n", w_now)
        @printf(io, "tau_p,%.6f\n", τp_now);     @printf(io, "pen,%.6f\n", pen_now)
        @printf(io, "B,%.6f\n", B_debt_now);     @printf(io, "B_over_Y,%.6f\n", B_debt_now / Y)
        @printf(io, "C_over_Y,%.6f\n", C / Y);   @printf(io, "M_over_Y,%.6f\n", M / Y)
        @printf(io, "A_dom,%.6f\n", A_dom);      @printf(io, "N_W,%.6f\n", N_W_now)
        @printf(io, "N_R,%.6f\n", N_R_now);      @printf(io, "dep_ratio,%.6f\n", dep)
    end
    println("Wrote $path")
    return r_annual, dep
end

function write_welfare(tag, W)
    path = joinpath(RESULTS_DIR, "$(tag)_welfare.csv")
    open(path, "w") do io
        println(io, "sex,skill,W1")
        @printf(io, "M,theta_L,%.8f\n", W[1, 1]);  @printf(io, "M,theta_H,%.8f\n", W[1, 2])
        @printf(io, "F,theta_L,%.8f\n", W[2, 1]);  @printf(io, "F,theta_H,%.8f\n", W[2, 2])
    end
    println("Wrote $path")
    return nothing
end

function write_lifecycle(tag)
    cm_c, cm_l, cm_a, cm_m, cm_h = cohort_means()
    sexlab = ["M", "F"]; skilllab = ["theta_L", "theta_H"]
    path = joinpath(RESULTS_DIR, "$(tag)_lifecycle.csv")
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

# ── Solve + gates + write (shared across Runs 2-4) ────────────────────────────
# Returns NamedTuple of headline scalars. Prints the §5 self-contained gates
# (1-4) plus τp, K, M/Y, dep_ratio and the Δ-vs-Run-1' lines for the run.
function run_and_report!(tag, title)
    println("\nSolving GE (joint closure: τp endogenous, B residual) …")
    hist, A_dom, L_new, C, M, Λvoid, Y, K, L = Base.invokelatest(solve_ge!)
    W   = Base.invokelatest(welfare_at_birth)
    res = Base.invokelatest(euler_residual_stats)
    eulmax  = isempty(res) ? -Inf : maximum(log10.(max.(res, 1e-16)))
    eulmean = isempty(res) ? -Inf : mean(log10.(max.(res, 1e-16)))
    cap_resid = abs(K - (A_dom - B_debt_now)) / max(abs(K), 1e-12)
    DIFF = hist.DIFF[end]

    r_annual, dep = write_summary(tag, K, L, Y, C, M, A_dom)
    write_welfare(tag, W)
    write_lifecycle(tag)

    MY = M / Y
    println("\n", "="^72)
    println("  $title — GATE SUMMARY")
    println("="^72)
    @printf "  [1] goods DIFF/Y          = %+.3e   (gate < 1e-3)   %s\n" DIFF (abs(DIFF) < 1e-3 ? "PASS" : "FAIL")
    @printf "  [2] capital |K-(A-B)|/K   = %.3e    (gate < 2e-4)   %s\n" cap_resid (cap_resid < 2e-4 ? "PASS" : "FAIL")
    @printf "  [3] Euler max log10       = %.3f      (gate < -3)  mean=%.3f\n" eulmax eulmean
    wgapL = abs(W[1,1] - W[2,1]) / max(abs(W[1,1]), 1e-12) * 100
    @printf "  [4] two-sex W gap (θ_L)   = %.2f%%     (M≠F)  M=%.4f F=%.4f\n" wgapL W[1,1] W[2,1]
    @printf "  τp    = %.4f   (Run 1' = %.4f, Δ=%+.4f)\n" τp_now RUN1PRIME_TAUP (τp_now - RUN1PRIME_TAUP)
    @printf "  K     = %.4f   (Run 1' = %.4f, Δ=%+.2f%%)\n" K RUN1PRIME_K ((K-RUN1PRIME_K)/RUN1PRIME_K*100)
    @printf "  M/Y   = %.5f   dep_ratio=%.4f  Y=%.4f  r_ann=%.3f%%  B/Y=%.4f  w=%.4f  pen=%.4f\n" MY dep Y r_annual (B_debt_now/Y) w_now pen_now
    @printf "  W: M_θL=%.4f M_θH=%.4f F_θL=%.4f F_θH=%.4f\n" W[1,1] W[1,2] W[2,1] W[2,2]
    @printf "\n  GE iterations: %d (itermax=%d)   final DIFF/Y=%+.3e\n" hist.iter[end] itermax_ge DIFF
    if any(!isfinite, (K, L, Y, C, M))
        println("  *** NaN/Inf in aggregates — solve is bad, do not trust. ***")
    end
    println("\n$title done.")
    flush(stdout)
    return (K=K, L=L, Y=Y, r_5yr=r_now, r_annual=r_annual, w=w_now, τp=τp_now,
            pen=pen_now, B=B_debt_now, MY=MY, dep=dep, W=W, DIFF=DIFF,
            eulmax=eulmax, cap_resid=cap_resid)
end
