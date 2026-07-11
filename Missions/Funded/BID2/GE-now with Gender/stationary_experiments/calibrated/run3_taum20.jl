################################################################################
# run3_taum20.jl — Run 3: τm health subsidy (0 → −0.20) from the harmonized
# calibrated baseline (CC_instrucciones_runs_2to4.md §3 Run 3).
#
# = Run 1' (harmonized calibrated 2020 baseline) with the single perturbation
#   τm: 0.00 → −0.20, joint closure (τp endogenous, B residual).
#
# FRESH PROCESS, load-bearing order (cf. run_taum.jl): τm is a `const` consumed
# directly by the cell solver (c = (X − a′ − (1+τm)m)/(1+τc)), which compiles
# once. Redefining a const after that does NOT propagate on Julia 1.11. So:
#   1. include lib (brings in solver; const τm=0.0 defined; NOTHING solved yet)
#   2. override τm → −0.20  (const redef, BEFORE any τm-reading method compiles)
#   3. apply_calibration! + init_model!  (no τm-reading method compiled here)
#   4. solve  (cell solver + compute_debt! compile now, reading τm=−0.20)
################################################################################

include(joinpath(@__DIR__, "calibrated_lib.jl"))

# Override τm BEFORE anything that reads it is compiled or solved.
Core.eval(@__MODULE__, :(const τm = -0.20))
@assert abs(τm - (-0.20)) < 1e-12 "τm override did not take (τm=$(τm))."

println("="^72)
println("  RUN 3 — τm health subsidy 0→−0.20 (harmonized calibrated baseline)")
println("="^72)
println("  J=$J  gender_gap=$gender_gap  threads=$(Threads.nthreads())  τm=$(τm)")

apply_calibration!()
init_model!()
@printf "  CHECK π_birth=[%.4f %.4f; %.4f %.4f]  θ_grid=%.4f,%.4f  τm=%.4f\n" π_birth[1,1] π_birth[1,2] π_birth[2,1] π_birth[2,2] θ_grid[1] θ_grid[2] τm

# κ stays at baseline 0.50; joint closure is the solver default. τm already set.
r = run_and_report!("run3_taum20", "RUN 3 (τm=−0.20)")

# §5 gates 7-9: M/Y rises (subsidized medical), τp rises slightly (survival channel).
const RUN1PRIME_MY = 0.027280   # results/run1prime_summary.csv
@printf "\n[gate 7] M/Y: Run 1' %.5f → τm=−0.20 %.5f  (%s — expect rise)\n" RUN1PRIME_MY r.MY (r.MY > RUN1PRIME_MY + 1e-5 ? "PASS" : "⚠ CHECK")
@printf "[gate 9] τp: Run 1' %.4f → τm=−0.20 %.4f  (%s — expect slight rise via survival)\n" RUN1PRIME_TAUP r.τp (r.τp > RUN1PRIME_TAUP - 1e-4 ? "≈/PASS" : "⚠ CHECK")
println("(gate 8 — progressive welfare incidence — assessed in assemble step vs run1prime_welfare.csv)")
