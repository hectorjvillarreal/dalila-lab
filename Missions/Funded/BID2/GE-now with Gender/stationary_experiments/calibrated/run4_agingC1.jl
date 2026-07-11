################################################################################
# run4_agingC1.jl — Run 4: Aging C1 (2050 demographics, joint closure) from the
# harmonized calibrated baseline (CC_instrucciones_runs_2to4.md §3 Run 4).
#
# = Run 1' (harmonized calibrated 2020 baseline) with demographics substituted
#   to Mexico 2050 (demographics_2050.jl: n_p_2050, ψ_base_male_2050,
#   ψ_base_female_2050) installed via set_demographics! on the solver's TYPED
#   GLOBALS n_p / ψ_base.
#
# Closure: C1 = JOINT (τp endogenous via update_pension_taxes!, B residual via
# compute_debt!) — the solver default. This is the FEASIBLE aging response where
# τp rises to clear PAYG as the dependency ratio climbs (§5.5 headline). It is
# NOT the C2 interp-1 of Run 0 (τp pinned, debt absorbs, infeasible). So we do
# NOT override the closure here.
#
# Top-level statements so set_demographics! is visible to solve_ge! at latest
# world age.
################################################################################

include(joinpath(@__DIR__, "calibrated_lib.jl"))
const DEMOG_2050 = abspath(joinpath(HERE, "..", "..", "demographic_experiment",
                                    "demographics_2050.jl"))
include(DEMOG_2050)

println("="^72)
println("  RUN 4 — Aging C1: 2050 demographics, joint closure (harmonized baseline)")
println("="^72)
println("  Demog  : $DEMOG_2050")
println("  J=$J  gender_gap=$gender_gap  threads=$(Threads.nthreads())")

apply_calibration!()
init_model!()
# Substitute 2050 demographics (typed globals n_p, ψ_base — not inlined).
set_demographics!(n_p_2050, ψ_base_male_2050, ψ_base_female_2050)
@printf "  CHECK π_birth=[%.4f %.4f; %.4f %.4f]  θ_grid=%.4f,%.4f  n_p=%.6f\n" π_birth[1,1] π_birth[1,2] π_birth[2,1] π_birth[2,2] θ_grid[1] θ_grid[2] n_p

r = run_and_report!("run4_agingC1", "RUN 4 (aging C1, 2050)")

# §5 gates 10-12 vs Run 1' (dep 0.1857, τp 0.0929, K 4.960, r_5yr 0.2289).
const RUN1PRIME_DEP   = 0.185718
const RUN1PRIME_R5YR  = 0.228900
@printf "\n[gate 10] dep_ratio: Run 1' %.4f → aging %.4f  (×%.2f — expect ~2×)\n" RUN1PRIME_DEP r.dep (r.dep / RUN1PRIME_DEP)
@printf "[gate 11] τp: Run 1' %.4f → aging %.4f  (%s — expect substantial rise)\n" RUN1PRIME_TAUP r.τp (r.τp > RUN1PRIME_TAUP + 1e-3 ? "PASS" : "⚠ CHECK")
@printf "[gate 12] K: Run 1' %.4f → aging %.4f  (%s — expect rise);  r_5yr %.4f → %.4f (%s — expect fall)\n" RUN1PRIME_K r.K (r.K > RUN1PRIME_K ? "PASS" : "⚠ CHECK") RUN1PRIME_R5YR r.r_5yr (r.r_5yr < RUN1PRIME_R5YR ? "PASS" : "⚠ CHECK")
