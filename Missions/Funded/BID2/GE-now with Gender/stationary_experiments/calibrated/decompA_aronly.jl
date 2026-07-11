################################################################################
# decompA_aronly.jl — §7 K-change decomposition, leg A: AR(1) harmonization ONLY.
#
# Run 1' moved K −52.7% vs gate Run 1 (10.488 → 4.960). §7 requires decomposing
# how much is the AR(1) re-anchoring (ρ:0.98→0.782, σ_ε:0.05→0.265, precautionary
# channel) vs the asymmetric π_birth (cohort-composition channel).
#
# This leg: harmonized AR(1) (calibrated_lib init_model!) but π_birth REVERTED to
# the symmetric 0.25 stub. Compared against gate Run 1 (stub AR + symmetric π,
# K=10.488), the K gap isolates the AR(1) effect. Joint closure, calibrated SMM.
################################################################################

include(joinpath(@__DIR__, "calibrated_lib.jl"))

println("="^72)
println("  DECOMP A — AR(1) harmonized ONLY (π_birth reverted to symmetric 0.25)")
println("="^72)
println("  J=$J  gender_gap=$gender_gap  threads=$(Threads.nthreads())")

apply_calibration!()        # sets asymmetric π_birth + harmonized leaf fns
init_model!()               # harmonized AR(1) ρ=0.782 σ_ε=0.265

# Revert π_birth to the symmetric stub (isolate the AR(1) channel).
for ig in 1:Ng, iθ in 1:Nθ
    π_birth[ig, iθ] = 0.25
end
@printf "  REVERTED π_birth to symmetric: [%.4f %.4f; %.4f %.4f]  sum=%.4f\n" π_birth[1,1] π_birth[1,2] π_birth[2,1] π_birth[2,2] sum(π_birth)
@printf "  (AR(1) stays harmonized: η_grid range = [%.4f, %.4f])\n" minimum(η_grid) maximum(η_grid)

r = run_and_report!("decompA_aronly", "DECOMP A (AR-only)")
@printf "\n[decomp A] K = %.4f   (gate Run 1 stub baseline = 10.488; Run 1' full = 4.960)\n" r.K
