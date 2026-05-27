################################################################################
# run_taum.jl  — §6.2 health subsidy (τm: 0 → −0.20).
#
# FRESH PROCESS, ONE SOLVE. τm is a `const` consumed directly by the cell
# solver (household budget c = (X − a′ − (1+τm)m)/(1+τc)), which compiles once.
# Redefining a const after that does NOT propagate on Julia 1.11. The robust
# route is to set τm BEFORE the first solve so it is baked at first compile —
# which requires its own process (this one) that does no prior solve.
#
# Order is load-bearing:
#   1. include lib (defines const τm=0.0; nothing compiled/solved yet)
#   2. override τm → −0.20  (const redef, BEFORE any compile)
#   3. init grids
#   4. configure closures (compute_debt! compiled now, reads τm=−0.20)
#   5. warm-start + solve once (cell solver compiled now, reads τm=−0.20)
################################################################################

include(joinpath(@__DIR__, "stationary_lib.jl"))

# Override τm before anything is compiled or solved.
Core.eval(@__MODULE__, :(const τm = -0.20))

set_initial_guess!(K_AGING_RUN1, L_AGING_RUN1)
init_model!()                       # prints τm to confirm = -0.20

@assert abs(τm - (-0.20)) < 1e-12 "τm override did not take (τm=$(τm))."

# κ stays at baseline 0.50; debt closure :residual_B as in RUN 1.
set_pension_kappa!(0.50)
set_debt_residual_B!()

r_taum = run_one("τm=−0.20 (health subsidy)")
write_single("taum20_results.csv", r_taum)

println("run_taum.jl done.")
