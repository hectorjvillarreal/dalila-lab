################################################################################
#  run_calibration.jl
#
#  Top-level driver for the SMM calibration scaffold. Loads everything, runs
#  the 7 verification smoke tests, then (optionally) launches the multistart
#  Nelder-Mead. Mode is selected by the first CLI argument:
#
#      julia --project=. -t 4 Calibration/run_calibration.jl smoke
#          → solve PE at theta_init, compute 6 moments, eval objective, do
#            3 trial evaluations, one finite-difference step. ~60 min.
#
#      julia --project=. -t 4 Calibration/run_calibration.jl parity
#          → solve PE with Household-Gender's *hardcoded* prices (r=0.159,
#            w=1.00, τp=0.10, pen=0.30) and verify the cohort-mean CSV
#            matches Household-Gender/household_lifecycle_gap.csv to ~1e-10.
#            Validates the Ref-refactor is algorithm-identity. ~15 min.
#
#      julia --project=. -t 4 Calibration/run_calibration.jl jacobian
#          → smoke + one full Jacobian computation at theta_init. ~30 min
#            on top of smoke.
#
#      julia --project=. -t 4 Calibration/run_calibration.jl multistart
#          → full Nelder-Mead, 8 starts × ~50 iters each. ~12+ hours.
#          (Use this only with real first-step inputs and real target moments.)
#
#      julia --project=. -t 4 Calibration/run_calibration.jl
#          → defaults to "smoke".
#
#  Outputs land in Calibration/outputs/.
################################################################################

using Printf

const CAL_DIR = @__DIR__

# Order matters: pe_solver_for_smm before moments/vsl (they reference its names).
include(joinpath(CAL_DIR, "src", "pe_solver_for_smm.jl"))
include(joinpath(CAL_DIR, "src", "load_inputs.jl"))
include(joinpath(CAL_DIR, "src", "vsl.jl"))
include(joinpath(CAL_DIR, "src", "moments.jl"))
include(joinpath(CAL_DIR, "src", "objective.jl"))
include(joinpath(CAL_DIR, "src", "optimizer.jl"))
include(joinpath(CAL_DIR, "src", "diagnostics.jl"))

# ─── Smoke tests ────────────────────────────────────────────────────────────
function smoke_tests(io::NamedTuple; out_dir::String=joinpath(CAL_DIR, "outputs"))
    mkpath(out_dir)
    println("\n════════════════════════════════════════════════════════════")
    println(" SMM scaffold smoke tests")
    println("════════════════════════════════════════════════════════════")

    # 1 — Inputs already loaded; report dimensions
    println("\n[1] Inputs loaded")
    @printf "    first_step: e_age %s, ψ_base %s, δh %s, π_birth %s\n" size(io.first_step.e_age) size(io.first_step.ψ_base) size(io.first_step.δh) size(io.first_step.π_birth)
    @printf "    anchor: r=%.4f, w=%.4f, τp=%.4f, pen=%.4f\n" io.anchor.r io.anchor.w io.anchor.τp io.anchor.pen
    @printf "    targets: %d moments\n" length(io.targets.names)
    @printf "    theta_init: %d params %s\n" length(io.theta_init.names) io.theta_init.names

    # 2 — Initialize grids and call PE solver at the init parameter values
    println("\n[2] Initializing grids and solving PE at theta_init …")
    init_grids!(refine_m_flag = io.grids.refine_m)
    θ0 = theta_nt_from_vector(copy(io.theta_init.init), io.theta_init)
    t0 = time()
    solve_pe_at!(θ0, io.anchor, io.first_step; verify=io.grids.verify, verbose=true)
    @printf "    PE solve completed in %.1f sec\n" (time() - t0)

    # 3 — Compute the 6 moments, print them
    println("\n[3] Computing the 6 simulated moments at theta_init …")
    m_nt = compute_moments(io.usd_scale)
    for n in io.targets.names
        sym = Symbol(n)
        val = getfield(m_nt, sym)
        dat = io.targets.values[findfirst(==(n), io.targets.names)]
        @printf "    %-20s  model = %12.6g   data = %12.6g\n" n val dat
    end
    open(joinpath(out_dir, "moments_at_stub.csv"), "w") do io_out
        println(io_out, "name,model,data")
        for n in io.targets.names
            sym = Symbol(n)
            val = getfield(m_nt, sym)
            dat = io.targets.values[findfirst(==(n), io.targets.names)]
            println(io_out, "$n,$val,$dat")
        end
    end

    # 4 — Objective smoke test
    println("\n[4] Computing the SMM objective at theta_init …")
    m_sim_vec = moments_vector(m_nt, io.targets.names)
    Q0 = smm_distance(m_sim_vec, io.targets.values, io.targets.ses)
    @printf "    Q(theta_init) = %.6e\n" Q0
    @assert isfinite(Q0) && Q0 > 0 "Objective at theta_init is non-finite or non-positive"

    # 5 — Brief eval-log run (3 trials) to exercise SmmObjective
    println("\n[5] Exercising SmmObjective with 3 trial evaluations …")
    log_path = joinpath(out_dir, "eval_log_smoke.csv")
    eval_log = open_eval_log(log_path, io.theta_init, io.targets.names)
    obj = SmmObjective(io, eval_log; verify=false)
    x0 = vec_to_unconstrained(copy(io.theta_init.init), io.theta_init)
    println("    Trial 1 (init): Q = ", obj(x0))
    println("    Trial 2 (+5% Ψ): Q = ", obj(x0 .+ 0.05 .* [1.0, 0, 0, 0, 0, 0]))
    println("    Trial 3 (-5% Ψ): Q = ", obj(x0 .- 0.05 .* [1.0, 0, 0, 0, 0, 0]))
    println("    eval_log written to: ", log_path)

    # 6 — Numerical Jacobian smoke test (just one column)
    println("\n[6] Numerical Jacobian smoke test: one finite-difference column …")
    x_plus = copy(x0); x_plus[1] += 1e-4
    Q_plus = obj(x_plus)
    @printf "    Q(x0 + h·e1) = %.6e   (vs Q0 = %.6e)\n" Q_plus Q0
    @assert isfinite(Q_plus) "Jacobian smoke test produced non-finite objective"

    println("\n════════════════════════════════════════════════════════════")
    println(" All 6 smoke tests completed.")
    println("════════════════════════════════════════════════════════════")
    println(" For algorithm-identity verification against Household-Gender,")
    println(" run `julia --project=. -t 4 Calibration/run_calibration.jl parity`.")
end

# ─── Parity test (own mode) ─────────────────────────────────────────────────
# Solves PE with Household-Gender's *hardcoded* PE prices AND first-step
# values constructed by the EXACT same Julia formulas as Household-Gender
# (rather than from the CSV — the CSV rounds to 8 sig figs, which would
# perturb the ψ_base values by ~2.5e-9 per cell and amplify to ~1e-4 over
# the iteration). Then diffs the cohort-mean CSV against
# ../Household-Gender/household_lifecycle_gap.csv. Must match to ~1e-10
# (Ref-refactor = algorithm-identity).
function build_householdgender_first_step()
    # Replicates Household-Gender/household_problem_gender.jl lines 117-144
    # at full Float64 precision (no CSV round-trip loss).
    _e_age16  = [1.0000, 1.3527, 1.6952, 1.8279, 1.9606, 1.9692, 1.9692,
                 1.9392, 1.9007, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    _ψ_base16 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                 0.98972953, 0.98185396, 0.97070373, 0.95530594,
                 0.93417914, 0.90238714, 0.83653436, 0.71048182,
                 0.52669353, 0.31179803]
    _δh16     = [0.02, 0.02, 0.03, 0.03, 0.05, 0.07, 0.10, 0.14,
                 0.18, 0.22, 0.27, 0.32, 0.38, 0.45, 0.55, 0.70]
    _e_age_J  = vcat(_e_age16,  0.0)
    _ψ_base_J = vcat(_ψ_base16, 0.15)
    _δh_J     = vcat(_δh16,     0.80)
    # gender_gap = true (matches the reference CSV's name "_gap")
    _e_age_female  = 0.85 .* _e_age_J
    _ψ_base_female = [1.0 - 0.75 * (1.0 - p) for p in _ψ_base_J]
    e_age_mat  = vcat(_e_age_J',  _e_age_female')        # 2 × J
    ψ_base_mat = vcat(_ψ_base_J', _ψ_base_female')       # 2 × J
    return (; e_age   = e_age_mat,
              ψ_base  = ψ_base_mat,
              δh      = _δh_J,
              π_birth = fill(0.25, 2, 2),
              θ_grid  = [-0.20, 0.20],
              ϱ_pen   = [0.30, 0.20],
              ρ       = 0.98,
              σ_ε     = 0.05,
              J       = 17)
end

function parity_test(io::NamedTuple; out_dir::String=joinpath(CAL_DIR, "outputs"))
    mkpath(out_dir)
    println("\n════════════════════════════════════════════════════════════")
    println(" Parity test: Ref-refactored solver ≡ Household-Gender reference")
    println("════════════════════════════════════════════════════════════")

    parity_anchor = (; r   = 1.03^5 - 1.0,
                       w   = 1.00,
                       τp  = 0.10,
                       pen = 0.30)
    @printf "Parity anchor (Household-Gender hardcoded): r=%.5f, w=%.5f, τp=%.5f, pen=%.5f\n" parity_anchor.r parity_anchor.w parity_anchor.τp parity_anchor.pen
    println("First-step values: built inline (NOT from CSV) — bit-identical to Household-Gender.")

    init_grids!(refine_m_flag = io.grids.refine_m)
    θ0 = theta_nt_from_vector(copy(io.theta_init.init), io.theta_init)
    parity_first_step = build_householdgender_first_step()
    t0 = time()
    solve_pe_at!(θ0, parity_anchor, parity_first_step; verify=false, verbose=true)
    @printf "PE solve completed in %.1f sec.\n" (time() - t0)

    write_parity_csv(out_dir; suffix="_parity")
    parity_csv = joinpath(out_dir, "household_lifecycle_parity.csv")
    ref_csv = joinpath(CAL_DIR, "..", "Household-Gender", "household_lifecycle_gap.csv")
    isfile(ref_csv) || error("reference CSV not found: $ref_csv. Run Household-Gender first.")
    max_diff = parity_diff(parity_csv, ref_csv)
    @printf "\nMax |abs| difference vs reference: %.3e   (gate ≤ 1e-10)\n" max_diff
    if max_diff > 1e-10
        @warn "Parity test exceeds gate ($max_diff > 1e-10). Ref-refactor may have introduced numerical drift."
    else
        println("✔ PASS — Ref-refactored solver is algorithm-identity with Household-Gender.")
    end
    return max_diff
end

# ─── Parity diff helper ─────────────────────────────────────────────────────
function parity_diff(my_csv::String, ref_csv::String)
    # Both CSVs have the same column structure (10 columns starting with
    # age_period). We compare numeric columns row by row.
    isfile(my_csv) || error("parity CSV missing: $my_csv")
    isfile(ref_csv) || error("reference CSV missing: $ref_csv")
    my_lines = readlines(my_csv)
    ref_lines = readlines(ref_csv)
    length(my_lines) == length(ref_lines) || return Inf
    max_diff = 0.0
    for k in 2:length(my_lines)
        my_fields = split(my_lines[k], ',')
        ref_fields = split(ref_lines[k], ',')
        length(my_fields) == length(ref_fields) || return Inf
        # Skip the first 4 columns (age_period, sex_idx, theta_idx, theta_value)
        for j in 5:length(my_fields)
            a = parse(Float64, my_fields[j])
            b = parse(Float64, ref_fields[j])
            max_diff = max(max_diff, abs(a - b))
        end
    end
    return max_diff
end

# ─── Full Jacobian + sandwich SEs at theta_init ─────────────────────────────
function jacobian_at_init(io::NamedTuple; out_dir::String=joinpath(CAL_DIR, "outputs"))
    init_grids!(refine_m_flag = io.grids.refine_m)
    log_path = joinpath(out_dir, "eval_log_jacobian.csv")
    eval_log = open_eval_log(log_path, io.theta_init, io.targets.names)
    obj = SmmObjective(io, eval_log; verify=false)
    x0 = vec_to_unconstrained(copy(io.theta_init.init), io.theta_init)

    println("\n──── Computing numerical Jacobian at theta_init (≈ $(2*length(x0)+1) PE solves) ────")
    res = full_diagnostics_report(obj, x0, io, out_dir)
    println("\nJacobian, moment_match, theta_hat written to $(out_dir)/")
    println("Note: theta_hat here is theta_init (no optimization). For the post-")
    println("convergence diagnostic, run mode = multistart first.")
    return res
end

# ─── Full multistart ────────────────────────────────────────────────────────
function full_calibration(io::NamedTuple; out_dir::String=joinpath(CAL_DIR, "outputs"),
                           n_starts::Int=8, maxiter::Int=500)
    init_grids!(refine_m_flag = io.grids.refine_m)
    log_path = joinpath(out_dir, "eval_log_multistart.csv")
    eval_log = open_eval_log(log_path, io.theta_init, io.targets.names)
    obj = SmmObjective(io, eval_log; verify=false)

    println("\n──── Multistart Nelder-Mead: $n_starts starts × maxiter=$maxiter ────")
    t0 = time()
    ms = run_multistart(obj, io; n_starts=n_starts, maxiter=maxiter, verbose=true)
    @printf "\nMultistart complete in %.1f hours.   Best Q = %.6e\n" (time()-t0)/3600 ms.best.Q_hat

    x_hat = ms.best.x_hat
    println("\n──── Full diagnostics at Θ̂ ────")
    res = full_diagnostics_report(obj, x_hat, io, out_dir)

    return (; multistart=ms, diagnostics=res)
end

# ─── CLI dispatch ───────────────────────────────────────────────────────────
function main()
    mode = length(ARGS) >= 1 ? ARGS[1] : "smoke"
    println("Mode: $mode")
    io = load_all_inputs()
    if mode == "smoke"
        smoke_tests(io)
    elseif mode == "parity"
        parity_test(io)
    elseif mode == "jacobian"
        smoke_tests(io)
        jacobian_at_init(io)
    elseif mode == "multistart"
        full_calibration(io)
    else
        error("unknown mode '$mode' — expected one of: smoke, parity, jacobian, multistart")
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
