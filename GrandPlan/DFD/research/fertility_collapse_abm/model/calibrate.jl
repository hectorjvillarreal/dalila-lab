# =============================================================================
# calibrate.jl
# Stage 2 CALIBRATION HARNESS + N3 LOCUS GRID — Rapid Fertility Collapse ABM (DFD)
# =============================================================================
#
# PURPOSE
#   Calibrate the 8 Process-A free parameters (N2) to the N1 COMPOSITION loss
#   (bands 20-39, married & cohab trajectory, 2010-2024), per w in {0.4,0.6,0.8},
#   then run a FINAL confirmation ensemble at the best params (50k x 16), and the
#   N3 2x2 locus grid (site A x site B). TFR is loaded for COMPARISON ONLY and
#   NEVER enters the loss or tunes any parameter (identification wall, Stage 1).
#
# DESIGN (per STAGE2_calibration_instruction.md)
#   - Free params (8): form_base, marry_share_of_form, cohab_to_marr,
#       dissolve_cohab, dissolve_marr, norm_strength, norm_threshold, norm_steepness.
#     All probabilities are kept in valid ranges via a logistic transform on a box;
#     norm_steepness is kept positive via an exp/affine transform.
#   - PINNED: marriage_drift = 0 (N2), w (swept not fitted), the ASFR primitive
#     (A3 placeholder), backgrounds.
#   - Optimizer: a dependency-free Nelder-Mead (no Optim.jl) with random restarts.
#     Capped at ~150 loss evaluations total per w.
#   - INNER (loss) ensemble: CHEAP — 12_000 agents x 4 seeds (tractable per eval).
#   - FINAL confirmation: 50_000 agents x 16 seeds, mean +- sd.
#
# INVOCATION
#   JULIA_NUM_THREADS=8 julia --project=. calibrate.jl
#   # optional: restrict the w sweep, e.g. only 0.6:
#   JULIA_NUM_THREADS=8 julia --project=. calibrate.jl 0.6
#
# OUTPUTS (model/outputs/)
#   calibration_best_w{NN}.csv     best free params + final loss, per w
#   tfr_path_w{NN}.csv             final confirmation TFR path (mean+-sd), per w
#   composition_path_w{NN}.csv     final confirmation national composition, per w
#   composition_bands_w{NN}.csv    final per-band sim-vs-obs trajectory, per w
#   locus_grid_w{NN}.csv           N3 2x2 grid TFR endpoints + collapse verdict
#   calibration_log.csv            per-eval optimizer trace (w, loss, params)
#
# Author: Claude Code (Stage 2 calibration), DFD Core Team
# Date: 2026-06-19
# =============================================================================

include("cri_skeleton_abm.jl")

using Random
using Printf

# -----------------------------------------------------------------------------
# Inner / outer ensemble sizes (N5)
# -----------------------------------------------------------------------------
# Budgets are ENV-overridable (defaults = the real calibration sizes). This lets a
# seconds-scale pipeline self-test run without editing the science, e.g.
#   CAL_INNER_AGENTS=2000 CAL_INNER_SEEDS=2 CAL_FINAL_AGENTS=3000 CAL_FINAL_SEEDS=2 \
#   CAL_MAX_EVALS=8 CAL_N_RESTARTS=1 julia --project=. calibrate.jl 0.6
const INNER_AGENTS = parse(Int, get(ENV, "CAL_INNER_AGENTS", "12000"))  # cheap inner loop
const INNER_SEEDS  = parse(Int, get(ENV, "CAL_INNER_SEEDS",  "4"))
const FINAL_AGENTS = parse(Int, get(ENV, "CAL_FINAL_AGENTS", "50000"))  # reported confirmation
const FINAL_SEEDS  = parse(Int, get(ENV, "CAL_FINAL_SEEDS",  "16"))
const MAX_EVALS    = parse(Int, get(ENV, "CAL_MAX_EVALS",    "150"))     # optimizer budget per w
const N_RESTARTS   = parse(Int, get(ENV, "CAL_N_RESTARTS",   "3"))       # random restarts (best-of)
const NYEARS       = YEAR_END - YEAR_START

# -----------------------------------------------------------------------------
# Free-parameter space: bounded box + transforms
# -----------------------------------------------------------------------------
# Each free param p_i lives in [lo_i, hi_i]. The optimizer works in an
# UNCONSTRAINED coordinate x_i mapped into the box by a logistic squash, so
# Nelder-Mead can roam freely while every evaluated parameter is always valid.
#
# order is fixed (vector index -> name):
const FREE_NAMES = (:form_base, :marry_share_of_form, :cohab_to_marr,
                    :dissolve_cohab, :dissolve_marr,
                    :norm_strength, :norm_threshold, :norm_steepness)
# (lo, hi) box per free param. Probabilities in [0,1]-ish ranges; steepness wide.
const FREE_BOX = (
    (0.02, 0.60),    # form_base
    (0.05, 0.90),    # marry_share_of_form
    (0.00, 0.30),    # cohab_to_marr
    (0.00, 0.25),    # dissolve_cohab
    (0.00, 0.10),    # dissolve_marr
    (0.00, 0.95),    # norm_strength
    (0.10, 0.80),    # norm_threshold
    (2.00, 30.0),    # norm_steepness
)
const NFREE = length(FREE_NAMES)

logistic(x) = 1.0 / (1.0 + exp(-x))
logit(p)    = log(p / (1.0 - p))

# unconstrained x -> bounded params NamedTuple
function unpack(x::AbstractVector{<:Real})
    vals = ntuple(NFREE) do i
        lo, hi = FREE_BOX[i]
        lo + (hi - lo) * logistic(x[i])
    end
    return NamedTuple{FREE_NAMES}(vals)
end

# bounded value -> unconstrained coordinate (for seeding the simplex)
function pack(nt)
    x = zeros(NFREE)
    for i in 1:NFREE
        lo, hi = FREE_BOX[i]
        v = clamp(Float64(nt[FREE_NAMES[i]]), lo + 1e-6, hi - 1e-6)
        x[i] = logit((v - lo) / (hi - lo))
    end
    return x
end

# A sensible starting point (the current Params defaults, in-box).
default_free() = NamedTuple{FREE_NAMES}((0.16, 0.45, 0.05, 0.06, 0.015, 0.55, 0.42, 14.0))

# -----------------------------------------------------------------------------
# Loss evaluation (cheap inner ensemble). TFR is NEVER touched here.
# -----------------------------------------------------------------------------
function eval_loss(x, w, seedcomp, obs_band; agents = INNER_AGENTS, seeds = INNER_SEEDS)
    nt = unpack(x)
    sim = run_ensemble(; w = w, nseeds = seeds, nyears = NYEARS, n_agents = agents,
                         seedcomp = seedcomp, params_override = nt, seed0 = 7000)
    return composition_loss(sim, obs_band)   # N1, composition only
end

# -----------------------------------------------------------------------------
# Dependency-free Nelder-Mead (Lagarias et al. standard coefficients) with an
# eval cap. Minimizes f(x) over R^NFREE.
# -----------------------------------------------------------------------------
function nelder_mead(f, x0; maxevals = MAX_EVALS, step = 0.8,
                     α = 1.0, γ = 2.0, ρ = 0.5, σ = 0.5, log_cb = nothing)
    n = length(x0)
    # build initial simplex
    simplex = [copy(x0)]
    for i in 1:n
        xi = copy(x0); xi[i] += step
        push!(simplex, xi)
    end
    fvals = Float64[]; evals = 0
    for s in simplex
        push!(fvals, f(s)); evals += 1
        log_cb !== nothing && log_cb(s, fvals[end])
    end
    while evals < maxevals
        order = sortperm(fvals)
        simplex = simplex[order]; fvals = fvals[order]
        # centroid of all but worst
        xc = sum(simplex[1:end-1]) ./ n
        # reflection
        xr = xc .+ α .* (xc .- simplex[end])
        fr = f(xr); evals += 1; log_cb !== nothing && log_cb(xr, fr)
        if fr < fvals[1]
            # expansion
            xe = xc .+ γ .* (xr .- xc)
            fe = f(xe); evals += 1; log_cb !== nothing && log_cb(xe, fe)
            if fe < fr
                simplex[end] = xe; fvals[end] = fe
            else
                simplex[end] = xr; fvals[end] = fr
            end
        elseif fr < fvals[end-1]
            simplex[end] = xr; fvals[end] = fr
        else
            # contraction
            if fr < fvals[end]
                xk = xc .+ ρ .* (xr .- xc)     # outside
            else
                xk = xc .+ ρ .* (simplex[end] .- xc)  # inside
            end
            fk = f(xk); evals += 1; log_cb !== nothing && log_cb(xk, fk)
            if fk < min(fr, fvals[end])
                simplex[end] = xk; fvals[end] = fk
            else
                # shrink toward best
                x1 = simplex[1]
                for i in 2:length(simplex)
                    simplex[i] = x1 .+ σ .* (simplex[i] .- x1)
                    fvals[i] = f(simplex[i]); evals += 1
                    log_cb !== nothing && log_cb(simplex[i], fvals[i])
                    evals >= maxevals && break
                end
            end
        end
    end
    order = sortperm(fvals)
    return simplex[order[1]], fvals[order[1]], evals
end

# -----------------------------------------------------------------------------
# Calibrate one w: random-restart Nelder-Mead. Returns (best_nt, best_loss).
# -----------------------------------------------------------------------------
function calibrate_w(w, seedcomp, obs_band; logio = nothing)
    f = x -> eval_loss(x, w, seedcomp, obs_band)
    best_x = nothing; best_f = Inf
    rng = Xoshiro(20260619 + round(Int, 1000w))
    starts = Vector{Vector{Float64}}()
    push!(starts, pack(default_free()))                       # restart 0: defaults
    for _ in 1:(N_RESTARTS - 1)                               # random restarts
        push!(starts, [4.0 * (rand(rng) - 0.5) for _ in 1:NFREE])  # ~N(0) in x-space
    end
    evals_per = max(20, MAX_EVALS ÷ length(starts))
    for (k, x0) in enumerate(starts)
        cb = nothing
        if logio !== nothing
            cb = (xx, ff) -> begin
                nt = unpack(xx)
                @printf(logio, "%.2f,%d,%.6f", w, k, ff)
                for nm in FREE_NAMES
                    @printf(logio, ",%.6f", nt[nm])
                end
                println(logio)
            end
        end
        xb, fb, ev = nelder_mead(f, x0; maxevals = evals_per, log_cb = cb)
        @printf("  [w=%.2f restart %d] best loss = %.6f after %d evals\n", w, k, fb, ev)
        # keep the best; also retain the first result unconditionally so best_x is
        # never `nothing` even if every loss is NaN/Inf (degenerate guard).
        if best_x === nothing || (fb < best_f)
            best_f = fb; best_x = xb
        end
    end
    return unpack(best_x), best_f
end

# -----------------------------------------------------------------------------
# N3 — 2x2 locus grid for one w at the calibrated params.
# Provisional map_depth for the site-B "on" cell. [FLAGGED]
# -----------------------------------------------------------------------------
const MAP_DEPTH_ON = 0.6   # [PROVISIONAL — flagged. site-B "on" suppression depth.]

function locus_grid(w, best_nt, seedcomp; agents = FINAL_AGENTS, seeds = FINAL_SEEDS)
    cells = (
        ("A_on_B_off",  true,  false, 0.0),           # baseline
        ("A_on_B_on",   true,  true,  MAP_DEPTH_ON),  # both thresholds
        ("A_off_B_off", false, false, 0.0),           # neither
        ("A_off_B_on",  false, true,  MAP_DEPTH_ON),  # map-only
    )
    rows = NamedTuple[]
    for (label, son, mon, md) in cells
        sim = run_ensemble(; w = w, nseeds = seeds, nyears = NYEARS, n_agents = agents,
                             social_norm_on = son, map_nonlinearity_on = mon,
                             map_depth = md, seedcomp = seedcomp,
                             params_override = best_nt, seed0 = 9000)
        iv = findfirst(!isnan, sim.tfr_m)
        t0 = sim.tfr_m[iv]; t1 = sim.tfr_m[end]
        pct = 100 * (t1 - t0) / t0
        push!(rows, (cell = label, social_norm_on = son, map_on = mon, map_depth = md,
                     tfr_start = t0, tfr_end = t1, pct_change = pct,
                     tfr_end_sd = sim.tfr_s[end]))
        @printf("    [%s] TFR %.3f -> %.3f (%.0f%%)\n", label, t0, t1, pct)
    end
    return rows
end

# -----------------------------------------------------------------------------
# Driver
# -----------------------------------------------------------------------------
function main_calibrate(; ws = (0.4, 0.6, 0.8))
    mkpath(OUT_DIR)
    @printf("\n=== STAGE 2 CALIBRATION + N3 LOCUS GRID (threads=%d) ===\n", Threads.nthreads())
    @printf("inner: %d agents x %d seeds; final: %d agents x %d seeds; budget %d evals/w\n",
            INNER_AGENTS, INNER_SEEDS, FINAL_AGENTS, FINAL_SEEDS, MAX_EVALS)
    println("IDENTIFICATION: TFR is loaded for COMPARISON ONLY; it never enters the loss.")

    seedcomp = load_seed_composition_2010()
    obs_band = load_observed_composition_bands()
    obs_tfr  = load_observed_tfr()

    logf = joinpath(OUT_DIR, "calibration_log.csv")
    open(logf, "w") do io
        print(io, "w,restart,loss")
        for nm in FREE_NAMES; print(io, ",", nm); end
        println(io)

        for w in ws
            @printf("\n--- CALIBRATING w = %.2f ---\n", w)
            best_nt, best_loss = calibrate_w(w, seedcomp, obs_band; logio = io)
            @printf("  >> best loss(w=%.2f) = %.6f\n", w, best_loss)
            for nm in FREE_NAMES
                @printf("     %-22s = %.5f\n", nm, best_nt[nm])
            end

            # ---- write best params ----
            bdf = DataFrame(param = collect(String.(FREE_NAMES)),
                            value = [best_nt[nm] for nm in FREE_NAMES])
            push!(bdf, ("final_loss", best_loss))
            push!(bdf, ("marriage_drift_PINNED", 0.0))
            CSV.write(joinpath(OUT_DIR, @sprintf("calibration_best_w%02d.csv", round(Int, 100w))), bdf)

            # ---- FINAL confirmation run at best params (50k x 16) ----
            @printf("  Running FINAL confirmation (%d x %d) ...\n", FINAL_AGENTS, FINAL_SEEDS)
            base = run_ensemble(; w = w, nseeds = FINAL_SEEDS, nyears = NYEARS,
                                  n_agents = FINAL_AGENTS, seedcomp = seedcomp,
                                  params_override = best_nt, seed0 = 1000)
            fals = run_ensemble(; w = w, nseeds = FINAL_SEEDS, nyears = NYEARS,
                                  n_agents = FINAL_AGENTS, social_norm_on = false,
                                  seedcomp = seedcomp, params_override = best_nt, seed0 = 1000)
            write_tfr_csv(w, base, fals, obs_tfr)
            write_composition_csv(w, base)
            write_bands_csv(w, base, obs_band)
            iv = findfirst(!isnan, base.tfr_m)
            @printf("  FINAL TFR (norm ON):  %.3f -> %.3f\n", base.tfr_m[iv], base.tfr_m[end])
            @printf("  FINAL TFR (norm OFF): %.3f -> %.3f\n", fals.tfr_m[iv], fals.tfr_m[end])

            # ---- N3 locus grid at best params ----
            @printf("  N3 locus grid (w=%.2f):\n", w)
            grid = locus_grid(w, best_nt, seedcomp)
            CSV.write(joinpath(OUT_DIR, @sprintf("locus_grid_w%02d.csv", round(Int, 100w))),
                      DataFrame(grid))
        end
    end
    println("\nCalibration complete. Outputs in: ", OUT_DIR)
end

if abspath(PROGRAM_FILE) == @__FILE__
    if length(ARGS) >= 1
        ws = Tuple(parse(Float64, a) for a in ARGS)
        main_calibrate(; ws = ws)
    else
        main_calibrate()
    end
end
