################################################################################
# run_kappa.jl  — §6.1 pension reform, plus baseline warm-start verification.
#
# One process, two solves:
#   1. Baseline (κ=0.50): warm-started from RUN 1; gate asserts K ≈ 14.378.
#      This both verifies the corrected setup reproduces the aging RUN 1
#      baseline AND supplies the baseline M/Y the τm experiment needs for its
#      "M rises" gate (the aging summary doesn't carry M/Y).
#   2. κ=0.30: replacement rate lowered via set_pension_kappa!(0.30), which
#      redefines update_pension_taxes! with κ baked in (const-safe).
#
# Written as top-level statements (no main() wrapper) so each @eval'd
# redefinition is visible to the subsequent run_one call at latest world age.
################################################################################

include(joinpath(@__DIR__, "stationary_lib.jl"))

set_initial_guess!(K_AGING_RUN1, L_AGING_RUN1)   # warm start; baked at 1st compile
init_model!()

# ── 1. Baseline (κ=0.50) — warm-start verification / reproduces aging RUN 1 ──
set_pension_kappa!(0.50)
set_debt_residual_B!()
r_base = run_one("Baseline κ=0.50 (warm-start verify vs aging RUN 1)")
write_single("baseline_results.csv", r_base)

@assert abs(r_base.K - K_AGING_RUN1) < 0.1 "Baseline does not reproduce aging RUN 1 (got K=$(r_base.K), expected $K_AGING_RUN1). Setup still wrong — diagnose before trusting κ run."
println("✔ Baseline reproduces aging RUN 1 (K=$(r_base.K), expected $K_AGING_RUN1)")
flush(stdout)

# ── 2. Pension reform κ=0.30 ─────────────────────────────────────────────────
set_pension_kappa!(0.30)
r_kappa = run_one("κ=0.30 (pension reform)")
write_single("kappa30_results.csv", r_kappa)

# Sanity (§5 gate 4): lower κ ⇒ lower PAYG contribution ⇒ τp falls.
@printf "\n[gate 4] κ=0.30 → τp: %.2f%% → %.2f%%  (%s)\n" 100*r_base.τp 100*r_kappa.τp (r_kappa.τp < r_base.τp - 0.01 ? "PASS" : "⚠ FAIL")
println("run_kappa.jl done.")
