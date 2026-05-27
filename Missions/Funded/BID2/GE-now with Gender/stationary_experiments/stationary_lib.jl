################################################################################
# stationary_lib.jl
#
# Shared setup + helpers for the two stationary policy experiments
# (§6.1 pension reform κ:0.50→0.30, §6.2 health subsidy τm:0→−0.20).
#
# This is the corrected foundation after the first attempt (a bare
# include + solve_ge!()) diverged. Two root causes, both learned from the
# proven aging driver demographic_experiment/run_aging_ssvs.jl:
#
#   (1) include() skips ge_model_gender.jl::main() (PROGRAM_FILE guard), so the
#       grids / Rouwenhorst chain / ergodic dist are never built. Without
#       init_model!() below, π_η_erg stays zero → Φ seeds all-zero → aggregates
#       degenerate → solve_ge! diverges. (Aging driver lines 326–337.)
#
#   (2) RUN 1 is a *configured* solve, not a bare one. It installs an active_τω
#       shim + redefined labor_supply / available_resources, and the
#       :endogenous pension + :residual_B debt closures (which supply the
#       correct update_pension_taxes! with `global τp_now` and κ_rep·N_R/N_W).
#       A bare solve left τp pinned at its 0.10 init. (Aging driver lines 43–170.)
#
# Const-override hazard (aging driver lines 82–87): κ_rep and τm are `const`,
# and on Julia 1.11 redefining a const does NOT propagate into already-compiled
# methods (the n_p/ψ_base lesson). Handling differs by parameter:
#   • κ_rep enters ONLY update_pension_taxes! → override by REDEFINING that
#     function with κ baked in (set_pension_closure_kappa!). Proven-safe pattern.
#   • τm enters the cell solver directly (household budget) → cannot redefine
#     that safely. τm is overridden in a FRESH process, set BEFORE the first
#     solve so it is baked at first compile. See run_taum.jl.
################################################################################

using Printf, Statistics

const GE_SRC      = joinpath(@__DIR__, "..", "ge_model_gender.jl")
const RESULTS_DIR = joinpath(@__DIR__, "results")

# include brings the solver into Main without firing its main() (guarded by
# abspath(PROGRAM_FILE) == @__FILE__ in ge_model_gender.jl).
include(GE_SRC)
isdir(RESULTS_DIR) || mkpath(RESULTS_DIR)

# Aging-experiment RUN 1 (the §5 baseline) — used for cross-checks and the
# comparison column. Source of truth: demographic_experiment/results/
# aging_comparison_gap.csv, RUN 1 row.
const K_AGING_RUN1 = 14.378
const L_AGING_RUN1 = 15.870

# ── active_τω shim (verbatim from run_aging_ssvs.jl lines 49–78) ─────────────
# In :residual_B mode active_τω stays at τw, so these reproduce RUN 1 exactly.
const active_τω = Ref{Float64}(τw)

@eval Main begin
    function labor_supply(j::Int, h::Float64, η::Float64,
                          ig::Int, iθ::Int)::Float64
        if j >= j_R
            return 0.0
        end
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

# ── Pension closure with κ baked in (const-safe override of κ_rep) ───────────
# Mirrors set_pension_closure!(:endogenous) from the aging driver but takes the
# replacement rate as a literal so the override does NOT rely on const-κ_rep
# propagation. update_pension_taxes! is the sole consumer of the replacement
# rate (ge_model_gender.jl lines 698–699), so this captures every use.
function set_pension_kappa!(κ_val::Float64)
    @eval Main begin
        function update_pension_taxes!(L_eff::Float64)
            global τp_now, pen_now, wn_now
            if N_W_now > 0.0
                τp_now  = $(κ_val) * N_R_now / N_W_now
                pen_now = $(κ_val) * w_now * L_eff / N_W_now
            end
            wn_now = w_now * (1.0 - active_τω[] - τp_now)
        end
    end
    return nothing
end

# ── Debt closure :residual_B (verbatim from run_aging_ssvs.jl lines 137–146) ─
function set_debt_residual_B!()
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
    return nothing
end

# ── Warm-start: override the GE initial guess (K_init/L_init, read at entry of
# solve_ge!). Safe at first compile in each process (set before any solve). ────
function set_initial_guess!(K0::Float64, L0::Float64)
    Core.eval(@__MODULE__, :(const K_init = $K0))
    Core.eval(@__MODULE__, :(const L_init = $L0))
    return nothing
end

# ── Grid + Markov-chain init (verbatim from run_aging_ssvs.jl lines 331–337) ─
function init_model!()
    println("Initializing grids and Rouwenhorst chain …")
    grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
    grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
    π_mat, η_vec = rouwenhorst(Nη, ρ_AR, σ_ε, 0.0)
    π_η .= π_mat
    η_grid .= η_vec
    compute_ergodic!()
    @printf "  init done: n_p = %.6f   gender_gap = %s   τm = %.4f\n" n_p gender_gap τm
    return nothing
end

# ── Result struct + per-run solve ────────────────────────────────────────────
mutable struct RunResult
    label::String
    K::Float64; L::Float64; Y::Float64
    r_annual::Float64; w::Float64
    τp::Float64; pen::Float64
    B::Float64; B_over_Y::Float64
    C_over_Y::Float64; M_over_Y::Float64
    N_W::Float64; N_R::Float64; depratio::Float64
    W_MθL::Float64; W_MθH::Float64; W_FθL::Float64; W_FθH::Float64
    DIFF::Float64; euler_max::Float64
end

# NOTE: solve_ge!() called directly (no invokelatest) — this matches the proven
# aging driver, which redefines closures via @eval Main between runs in one
# process and produces distinct C1/C2 equilibria, confirming redefinitions
# propagate through solve_ge!'s internal calls in this codebase.
function run_one(label::String)
    println("\n" * "="^70)
    println("  RUN: $label")
    println("="^70)
    flush(stdout)
    hist, A_dom, L_new, C, M, Λvoid, Y, K, L = solve_ge!()
    W = welfare_at_birth()
    r_annual = ((1.0 + r_now)^0.2 - 1.0) * 100
    res = euler_residual_stats()
    eulmax = isempty(res) ? -Inf : maximum(log10.(max.(res, 1e-16)))

    sex_gap_θL = abs(W[1,1] - W[2,1])
    sex_gap_θH = abs(W[1,2] - W[2,2])
    @printf "  → K=%.4f L=%.4f Y=%.4f r(ann)=%.3f%% τp=%.4f B/Y=%.4f\n" K L Y r_annual τp_now (B_debt_now/Y)
    @printf "  DIFF/Y=%+.2e  Euler max log10=%.2f  M/Y=%.4f\n" hist.DIFF[end] eulmax (M/Y)
    @printf "  Symmetric-primitives identity: |M-F| at θL=%.2e, at θH=%.2e\n" sex_gap_θL sex_gap_θH
    flush(stdout)

    return RunResult(
        label, K, L, Y, r_annual, w_now,
        τp_now, pen_now, B_debt_now, B_debt_now / Y,
        C / Y, M / Y, N_W_now, N_R_now, N_R_now / N_W_now,
        W[1,1], W[1,2], W[2,1], W[2,2],
        hist.DIFF[end], eulmax
    )
end

function write_single(filename::String, r::RunResult)
    isdir(RESULTS_DIR) || mkpath(RESULTS_DIR)
    open(joinpath(RESULTS_DIR, filename), "w") do io
        println(io, "field,value")
        for f in fieldnames(RunResult)
            @printf(io, "%s,%s\n", f, string(getfield(r, f)))
        end
    end
    println("  → wrote results/$filename")
    flush(stdout)
end
