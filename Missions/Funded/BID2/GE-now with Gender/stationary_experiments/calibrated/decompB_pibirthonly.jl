################################################################################
# decompB_pibirthonly.jl — §7 K-change decomposition, leg B: π_birth ONLY.
#
# Companion to decompA_aronly.jl. This leg: asymmetric π_birth (calibrated_lib
# apply_calibration!) but AR(1) REVERTED to the GE stub (ρ=0.98, σ_ε=0.05).
# Compared against gate Run 1 (stub AR + symmetric π, K=10.488), the K gap
# isolates the π_birth cohort-composition effect. Joint closure, calibrated SMM.
#
# AR(1) revert: re-run rouwenhorst with the STUB literals AFTER init_model!
# (which built the harmonized chain), overwriting π_η / η_grid / ergodic.
################################################################################

include(joinpath(@__DIR__, "calibrated_lib.jl"))

println("="^72)
println("  DECOMP B — π_birth asymmetric ONLY (AR(1) reverted to stub ρ=0.98 σ_ε=0.05)")
println("="^72)
println("  J=$J  gender_gap=$gender_gap  threads=$(Threads.nthreads())")

apply_calibration!()        # sets asymmetric π_birth (kept) + harmonized leaf fns
init_model!()               # builds harmonized chain — overwritten just below

# Revert AR(1) to the GE stub (isolate the π_birth channel).
π_mat, η_vec = rouwenhorst(Nη, 0.98, 0.05, 0.0)
π_η .= π_mat
η_grid .= η_vec
compute_ergodic!()
@printf "  REVERTED AR(1) to stub: η_grid range = [%.4f, %.4f]  (ρ=0.98 σ_ε=0.05)\n" minimum(η_grid) maximum(η_grid)
@printf "  (π_birth stays asymmetric: [%.4f %.4f; %.4f %.4f])\n" π_birth[1,1] π_birth[1,2] π_birth[2,1] π_birth[2,2]

r = run_and_report!("decompB_pibirthonly", "DECOMP B (π_birth-only)")
@printf "\n[decomp B] K = %.4f   (gate Run 1 stub baseline = 10.488; Run 1' full = 4.960)\n" r.K
