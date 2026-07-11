################################################################################
# run2_kappa30.jl — Run 2: κ pension reform (0.50 → 0.30) from the harmonized
# calibrated baseline (CC_instrucciones_runs_2to4.md §3 Run 2).
#
# = Run 1' (harmonized calibrated 2020 baseline) with the single perturbation
#   κ_rep: 0.50 → 0.30, joint closure (τp endogenous, B residual).
#
# Top-level statements (no main() wrapper) so the set_pension_kappa! @eval
# redefinition is visible to solve_ge! at latest world age.
################################################################################

include(joinpath(@__DIR__, "calibrated_lib.jl"))

println("="^72)
println("  RUN 2 — κ pension reform 0.50→0.30 (harmonized calibrated baseline)")
println("="^72)
println("  J=$J  gender_gap=$gender_gap  threads=$(Threads.nthreads())")

apply_calibration!()
init_model!()
@printf "  CHECK π_birth=[%.4f %.4f; %.4f %.4f]  θ_grid=%.4f,%.4f\n" π_birth[1,1] π_birth[1,2] π_birth[2,1] π_birth[2,2] θ_grid[1] θ_grid[2]

# Perturbation: lower replacement rate to 0.30 (κ_rep stub is 0.50).
set_pension_kappa!(0.30)

r = run_and_report!("run2_kappa30", "RUN 2 (κ=0.30)")

# §5 gate 5: lower κ ⇒ lower PAYG contribution ⇒ τp falls vs Run 1'.
@printf "\n[gate 5] τp: Run 1' %.4f → κ=0.30 %.4f  (%s — expect fall)\n" RUN1PRIME_TAUP r.τp (r.τp < RUN1PRIME_TAUP - 1e-4 ? "PASS" : "⚠ CHECK")
println("(gate 6 — regressive welfare incidence — assessed in assemble step vs run1prime_welfare.csv)")
