################################################################################
# run0.jl — C2 interp-1 gate check (gate sequence, CC_instrucciones_gate_runs.md §2)
#
# THE decision run. Same calibrated parameters as run1.jl, but:
#   1. Demographics → Mexico 2050 (demographics_2050.jl: n_p_2050,
#      ψ_base_male_2050, ψ_base_female_2050), installed via set_demographics!
#      on the solver's TYPED GLOBALS n_p / ψ_base (these are not inlined).
#   2. Closure → C2 interpretation 1:
#        • τp PINNED at the Run 1 baseline value (read from run1_summary.csv).
#        • Pension benefits at the calibrated PAYG formula pen = κ·w·L/N^W
#          (NOT scaled to balance) — update_pension_taxes! :fixed mode.
#        • The PAYG deficit (pen_paid − pen_collected) is routed into the
#          general government budget; residual B closes it. This is the
#          interp-1 compute_debt! from C2_interp1_no_finite_SS.md.
#
# Two outcomes (gate doc §2):
#   A  GE fails to converge; rⁿ crosses n_p; B explodes. EXPECTED/DESIRED —
#      confirms §5.5.3 survives calibration → green-light Runs 2-4.
#   B  GE converges with rⁿ > n_p. Would invalidate v3 §5.5.3 → stop & report.
#
# To make Outcome A fast and unambiguous (and to bound compute) the
# instrumented compute_debt! throws C2Infeasible the first GE iteration that
# rⁿ − n_p < 0 — exactly the dynamic-inefficiency crossing the writeup
# identifies as the point where B = primary/(rⁿ−n_p) becomes ill-conditioned.
# Natural convergence of solve_ge! (no throw) is Outcome B.
#
# Does NOT edit ge_model_gender.jl. Outputs:
#   run0_history.csv (per-iter trace), run0.log (via shell redirect).
################################################################################

using Printf, Statistics

const HERE        = @__DIR__
const GE_SRC      = abspath(joinpath(HERE, "..", "..", "ge_model_gender.jl"))
const DEMOG_2050  = abspath(joinpath(HERE, "..", "..", "demographic_experiment",
                                     "demographics_2050.jl"))
const RESULTS_DIR = joinpath(HERE, "results")
isdir(RESULTS_DIR) || mkpath(RESULTS_DIR)

include(GE_SRC)
include(DEMOG_2050)

# ── Calibrated SMM scalars + first-step (identical to run1.jl) ────────────────
const PSI_CAL    = 13.452490
const XI_CAL     = 0.274472
const XICURV_CAL = 0.500000
const H0_CAL     = 0.247474
const HSLOPE_CAL = -0.035807
const ZETAH_CAL  = 0.579138
const E_AGE_MALE = [1.0000, 1.2718, 1.3665, 1.3941, 1.4904, 1.5084, 1.4335,
                    1.3469, 1.2277, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
const E_AGE_FEM  = [0.8350, 0.9726, 1.0615, 1.0268, 1.0755, 1.1222, 1.0945,
                    1.0331, 0.8640, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
const THETA_L_CAL = -0.3726
const THETA_H_CAL =  0.3726

function apply_calibration!()
    @assert length(E_AGE_MALE) == J
    @assert length(E_AGE_FEM)  == J
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
    return nothing
end

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

# Replace n_p and ψ_base (typed globals) — same helper as run_aging_ssvs.jl.
function set_demographics!(n_p_new, ψ_m_new, ψ_f_new)
    @assert length(ψ_m_new) == J
    @assert length(ψ_f_new) == J
    new_ψ = vcat(reshape(Float64.(collect(ψ_m_new)), 1, :),
                 reshape(Float64.(collect(ψ_f_new)), 1, :))
    setglobal!(Main, :n_p, n_p_new)
    setglobal!(Main, :ψ_base, new_ψ)
    return nothing
end

# ── C2 interp-1 closure ───────────────────────────────────────────────────────
# Per-iteration trace; compute_debt! pushes one row per GE iter.
const C2LOG = NamedTuple[]
# Sentinel thrown at the dynamic-inefficiency crossing (Outcome A).
struct C2Infeasible <: Exception
    iter::Int
    rn_minus_np::Float64
end

function install_c2_interp1_closure!(τp_pin::Float64)
    empty!(C2LOG)
    # Pension closure :fixed — τp pinned, benefits at calibrated PAYG formula.
    @eval Main begin
        function update_pension_taxes!(L_eff::Float64)
            global τp_now, pen_now, wn_now
            τp_now = $(τp_pin)
            if N_W_now > 0.0
                pen_now = κ_rep * w_now * L_eff / N_W_now   # calibrated, NOT scaled
            end
            wn_now = w_now * (1.0 - τw - τp_now)
        end
    end
    # Debt closure: interp-1 — pension deficit routed into general budget, B residual.
    @eval Main begin
        function compute_debt!(C::Float64, L::Float64, K::Float64,
                               M::Float64, Y::Float64)
            global B_debt_now
            G = gy * Y
            pen_paid        = κ_rep * w_now * L * N_R_now / N_W_now
            pen_collected   = τp_now * w_now * L
            pension_deficit = pen_paid - pen_collected
            primary = τc*C + τw*w_now*L + τk*r_now*K + τm*M - G - pension_deficit
            denom   = rn_now - n_p
            B_debt_now = primary / denom
            push!(C2LOG, (iter = length(C2LOG) + 1, K = K, L = L,
                          r_5yr = r_now, rn = rn_now, n_p = n_p,
                          rn_minus_np = denom, primary = primary,
                          pension_deficit = pension_deficit,
                          B = B_debt_now, B_over_Y = B_debt_now / Y,
                          tau_p = τp_now, Y = Y))
            if denom < 0.0
                throw(C2Infeasible(length(C2LOG), denom))
            end
        end
    end
    return nothing
end

# ── Read τp from Run 1 summary (strict serial; gate doc §3 recommendation) ────
function read_run1_taup()
    path = joinpath(RESULTS_DIR, "run1_summary.csv")
    isfile(path) || error("run1_summary.csv not found — run Run 1 first (strict serial).")
    for line in readlines(path)
        parts = split(strip(line), ',')
        length(parts) == 2 || continue
        if parts[1] == "tau_p"
            return parse(Float64, parts[2])
        end
    end
    error("tau_p row not found in run1_summary.csv")
end

function write_history(diff_by_iter::Dict{Int,Float64})
    path = joinpath(RESULTS_DIR, "run0_history.csv")
    open(path, "w") do io
        println(io, "iter,K,L,r_5yr,r_annual_pct,n_p,rn_minus_np,primary," *
                    "pension_deficit,B,B_over_Y,tau_p,DIFF_over_Y")
        for row in C2LOG
            r_ann = ((1.0 + row.r_5yr)^0.2 - 1.0) * 100
            diffv = get(diff_by_iter, row.iter, NaN)
            @printf(io, "%d,%.6f,%.6f,%.6f,%.5f,%.6f,%.6e,%.6f,%.6f,%.6e,%.6e,%.6f,%.6e\n",
                    row.iter, row.K, row.L, row.r_5yr, r_ann, row.n_p,
                    row.rn_minus_np, row.primary, row.pension_deficit,
                    row.B, row.B_over_Y, row.tau_p, diffv)
        end
    end
    println("Wrote $path  ($(length(C2LOG)) iterations)")
    return nothing
end

function main()
    println("="^72)
    println("  RUN 0 — C2 interp-1 gate check (2050 demographics, τp pinned, debt absorbs)")
    println("="^72)
    println("  Source : $GE_SRC")
    println("  Demog  : $DEMOG_2050")
    println("  J=$J  gender_gap=$gender_gap  threads=$(Threads.nthreads())")

    τp_pin = read_run1_taup()
    @printf "  τp pinned at Run 1 baseline = %.6f\n" τp_pin

    apply_calibration!()
    init_model!()
    set_demographics!(n_p_2050, ψ_base_male_2050, ψ_base_female_2050)
    @printf "  2050 demog installed: n_p=%.6f  ψ_m[10]=%.4f ψ_f[10]=%.4f\n" n_p ψ_base[1,10] ψ_base[2,10]
    install_c2_interp1_closure!(τp_pin)
    @printf "  CHECK θ_grid=%.4f,%.4f  e_age[2,1:3]=%.4f,%.4f,%.4f\n" θ_grid[1] θ_grid[2] e_age[2,1] e_age[2,2] e_age[2,3]

    println("\nSolving GE (C2 interp-1; will throw at rⁿ−n_p<0 if infeasible) …")
    flush(stdout)
    outcome = :unknown
    hist = nothing
    local A_dom, L_new, C, M, Λvoid, Y, K, L
    try
        hist, A_dom, L_new, C, M, Λvoid, Y, K, L = Base.invokelatest(solve_ge!)
        # No throw → solve_ge! returned. Converged?
        if abs(hist.DIFF[end]) < sig_ge && length(hist.iter) < itermax_ge
            outcome = :B_converged
        else
            outcome = :A_noconverge   # ran to itermax without converging, never crossed
        end
    catch e
        if e isa C2Infeasible
            outcome = :A_crossing
            @printf "\n  *** C2Infeasible: rⁿ−n_p = %+.6e < 0 at iter %d ***\n" e.rn_minus_np e.iter
        else
            rethrow(e)
        end
    end

    # Merge per-iter DIFF from GEHistory (available iters only).
    diff_by_iter = Dict{Int,Float64}()
    if hist !== nothing
        for (k, it) in enumerate(hist.iter)
            diff_by_iter[it] = hist.DIFF[k]
        end
    end
    write_history(diff_by_iter)

    println("\n", "="^72)
    println("  RUN 0 GATE RESULT")
    println("="^72)
    if outcome === :A_crossing
        last = C2LOG[end]
        println("  OUTCOME A — infeasibility HOLDS (rⁿ crossed n_p).")
        println("  → §5.5.3 survives the calibration. GREEN LIGHT for Runs 2-4.")
        @printf "    crossing iter=%d  rⁿ−n_p=%+.3e  B=%.3e  K=%.3f  primary=%.4f\n" last.iter last.rn_minus_np last.B last.K last.primary
        @printf "    pension_deficit at crossing = %.4f\n" last.pension_deficit
    elseif outcome === :A_noconverge
        println("  OUTCOME A (weak) — did NOT converge within $itermax_ge iters, but rⁿ stayed > n_p.")
        println("  → Infeasibility-by-nonconvergence; inspect run0_history.csv before deciding.")
        @printf "    final DIFF/Y=%+.3e  K=%.3f\n" hist.DIFF[end] K
    elseif outcome === :B_converged
        last = C2LOG[end]
        println("  OUTCOME B — GE CONVERGED. Debt fixed-point EXISTS at calibrated params.")
        println("  → Would invalidate v3 §5.5.3. STOP and report (demote to footnote).")
        @printf "    converged iter=%d  rⁿ−n_p=%+.3e (>0)  B=%.3f  B/Y=%.4f  K=%.3f\n" length(hist.iter) last.rn_minus_np last.B (last.B/Y) K
        @printf "    DIFF/Y=%+.3e  τp(pinned)=%.4f\n" hist.DIFF[end] τp_now
    else
        println("  OUTCOME UNKNOWN — inspect run0_history.csv and run0.log.")
    end
    println("\nRUN 0 done.")
    flush(stdout)   # defeat block-buffering on exit (Run 1's tail was lost to it)
    return nothing
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
