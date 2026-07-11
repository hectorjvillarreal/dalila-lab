# =============================================================================
# calibrate_3a.jl
# Stage 3a CALIBRATION HARNESS + SUFFICIENCY METRICS — no-reflexivity model (DFD)
# =============================================================================
#
# PURPOSE
#   Calibrate the 12 free parameters of stage3a_norefl_abm.jl (cohort-entry
#   heterogeneity + exogenous period shock) to the N1 COMPOSITION loss, PER
#   COUNTRY (CRI on ENAHO 2010-2024; COL on GEIH 2007-2024), then run a final
#   confirmation ensemble (50k x 16) and evaluate the PRE-REGISTERED sufficiency
#   metrics (§4 of the build instruction). TFR is NEVER loaded during
#   calibration; the runtime + static checks are logged to _assert_no_tfr.log.
#
# PRE-REGISTERED SUFFICIENCY METRICS (fixed BEFORE the full run; §4 discipline)
#   M1 magnitude: sim captures >= 85% of the observed equal-band-mean married-
#      share fall (seed year -> 2024), per country.
#   M2 late acceleration: the observed late-window share of the total married
#      decline, share_late = [m(2017)-m(2024)] / [m(seed)-m(2024)], matched by
#      the sim within +-0.10, per country.
#   M3 shape sign: mean second difference of the married series over 2015-2024
#      has the same sign in sim as observed (accelerating vs decelerating).
#   Verdict mapping (instruction §4):
#     M1 & M2 pass          -> sufficiency established
#     M1 pass, M2 fail      -> partial (level without tempo -> ENDS)
#     M1 fail               -> real tension (no-reflexivity underperforms)
#   The period-shock estimate (depth, midpoint) and the kappa(b) gradient are
#   REPORTED against the 2b APC verdicts (CRI period ~ 0 expected), not gated.
#
# DESIGN
#   - Free params (12): form_base, marry_share_of_form, cohab_to_marr,
#       dissolve_cohab, dissolve_marr, kappa_floor, kappa_mid, kappa_steep,
#       form_tilt, period_depth, period_mid, period_steep.
#   - Boxed logistic transform + dependency-free Nelder-Mead with random
#     restarts (carried from Stage 2 calibrate.jl).
#   - INNER (loss) ensemble: 12k agents x 4 seeds. FINAL: 50k x 16.
#   - Loss: N1 composition only (bands 20-39, married & cohab, all obs years).
#
# INVOCATION
#   JULIA_NUM_THREADS=8 julia --project=. calibrate_3a.jl            # both countries
#   JULIA_NUM_THREADS=8 julia --project=. calibrate_3a.jl COL        # one country
#   # seconds-scale self-test:
#   CAL3A_INNER_AGENTS=2000 CAL3A_INNER_SEEDS=2 CAL3A_FINAL_AGENTS=3000 \
#   CAL3A_FINAL_SEEDS=2 CAL3A_MAX_EVALS=15 CAL3A_N_RESTARTS=1 \
#   JULIA_NUM_THREADS=8 julia --project=. calibrate_3a.jl CRI
#
# OUTPUTS (model/outputs/stage3a/)
#   calibration_best_{CC}.csv      best free params + final loss
#   calibration_log_3a.csv         per-eval optimizer trace
#   {CC}_composition_path.csv, {CC}_composition_bands.csv, {CC}_tfr_overlay.csv
#   {CC}_cohort_multiplier.csv, {CC}_period_multiplier.csv
#   sufficiency_metrics.csv        M1-M3 sim vs obs vs criterion, per country
#   _assert_no_tfr.log             identification-wall checks (static + runtime)
#
# DOCUMENTED TO: PROTO-RAG-001 code standards.
# Build instruction: STAGE3a_sufficiency_instruction.md (Debb, 2026-07-11).
# endorsed_by: blank pending Nina (build).
#
# Author: Claude Code (Stage 3a sufficiency), DFD Core Team
# Date: 2026-07-11
# =============================================================================

include("stage3a_norefl_abm.jl")

using Random
using Printf

# -----------------------------------------------------------------------------
# Budgets (ENV-overridable; defaults = the real calibration sizes)
# -----------------------------------------------------------------------------
# Ablation pins (mechanism decomposition for the memo):
#   CAL3A_PIN=period -> period_depth pinned 0   (cohort-replacement only)
#   CAL3A_PIN=cohort -> kappa == 1, form_tilt 0 (exogenous period shock only)
# Pinned runs write to *_no{pin} filenames; headline artifacts are untouched.
const PIN = get(ENV, "CAL3A_PIN", "")
@assert PIN in ("", "period", "cohort") "CAL3A_PIN must be empty, 'period', or 'cohort'"
const TAG = PIN == "" ? "" : "_no" * PIN

const INNER_AGENTS = parse(Int, get(ENV, "CAL3A_INNER_AGENTS", "12000"))
const INNER_SEEDS  = parse(Int, get(ENV, "CAL3A_INNER_SEEDS",  "4"))
const FINAL_AGENTS = parse(Int, get(ENV, "CAL3A_FINAL_AGENTS", "50000"))
const FINAL_SEEDS  = parse(Int, get(ENV, "CAL3A_FINAL_SEEDS",  "16"))
const MAX_EVALS    = parse(Int, get(ENV, "CAL3A_MAX_EVALS",    "600"))   # per country
const N_RESTARTS   = parse(Int, get(ENV, "CAL3A_N_RESTARTS",   "4"))

# Pre-registered metric constants (do NOT tune after seeing results)
const M1_THRESHOLD   = 0.85     # magnitude capture
const M2_TOLERANCE   = 0.10     # late-share |sim - obs|
const LATE_Y0        = 2017     # late-window start (both countries)
const ACCEL_WINDOW   = (2015, 2024)

# -----------------------------------------------------------------------------
# Free-parameter space: bounded box + logistic transforms (Stage 2 pattern)
# -----------------------------------------------------------------------------
const FREE_NAMES = (:form_base, :marry_share_of_form, :cohab_to_marr,
                    :dissolve_cohab, :dissolve_marr,
                    :kappa_floor, :kappa_mid, :kappa_steep, :form_tilt,
                    :period_depth, :period_mid, :period_steep)
const FREE_BOX = (
    (0.02, 0.60),        # form_base
    (0.02, 0.90),        # marry_share_of_form (base, pre-kappa/pi)
    (0.00, 0.30),        # cohab_to_marr
    (0.00, 0.25),        # dissolve_cohab
    (0.00, 0.10),        # dissolve_marr
    (0.01, 1.00),        # kappa_floor
    (1955.0, 2010.0),    # kappa_mid (birth cohort)
    (0.01, 1.20),        # kappa_steep (per birth-year)
    (-0.05, 0.05),       # form_tilt (log-linear per birth-year)
    (0.00, 0.95),        # period_depth (0 => no shock; CRI free to sit here)
    (2000.0, 2028.0),    # period_mid (calendar year)
    (0.05, 3.00),        # period_steep (per year)
)
const NFREE = length(FREE_NAMES)

logistic(x) = 1.0 / (1.0 + exp(-x))
logit(p)    = log(p / (1.0 - p))

function unpack(x::AbstractVector{<:Real})
    vals = ntuple(NFREE) do i
        lo, hi = FREE_BOX[i]
        lo + (hi - lo) * logistic(x[i])
    end
    nt = NamedTuple{FREE_NAMES}(vals)
    # ablation pins applied at the transform boundary: every evaluated (and
    # reported) parameter vector honours the pin; the optimizer's pinned
    # coordinates become inert.
    PIN == "period" && return merge(nt, (period_depth = 0.0,))
    PIN == "cohort" && return merge(nt, (kappa_floor = 1.0, form_tilt = 0.0))
    return nt
end

function pack(nt)
    x = zeros(NFREE)
    for i in 1:NFREE
        lo, hi = FREE_BOX[i]
        v = clamp(Float64(nt[FREE_NAMES[i]]), lo + 1e-9, hi - 1e-9)
        x[i] = logit((v - lo) / (hi - lo))
    end
    return x
end

default_free() = NamedTuple{FREE_NAMES}((
    0.16, 0.30, 0.05, 0.06, 0.015,          # base rates
    0.30, 1990.0, 0.15, 0.005,              # cohort: floor, mid, steep, tilt
    0.15, 2018.0, 0.8))                     # period: depth, mid, steep

# -----------------------------------------------------------------------------
# Loss evaluation (cheap inner ensemble). TFR is NEVER touched here.
# -----------------------------------------------------------------------------
function eval_loss(x, cfg, seedcomp, obs_band; agents = INNER_AGENTS, seeds = INNER_SEEDS)
    nt = unpack(x)
    sim = run_ensemble(cfg; nseeds = seeds, n_agents = agents,
                         seedcomp = seedcomp, params_override = nt, seed0 = 7000)
    return composition_loss(sim, obs_band)
end

# -----------------------------------------------------------------------------
# Dependency-free Nelder-Mead (carried from Stage 2 calibrate.jl)
# -----------------------------------------------------------------------------
function nelder_mead(f, x0; maxevals = MAX_EVALS, step = 0.8,
                     α = 1.0, γ = 2.0, ρ = 0.5, σ = 0.5, log_cb = nothing)
    n = length(x0)
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
        xc = sum(simplex[1:end-1]) ./ n
        xr = xc .+ α .* (xc .- simplex[end])
        fr = f(xr); evals += 1; log_cb !== nothing && log_cb(xr, fr)
        if fr < fvals[1]
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
            if fr < fvals[end]
                xk = xc .+ ρ .* (xr .- xc)
            else
                xk = xc .+ ρ .* (simplex[end] .- xc)
            end
            fk = f(xk); evals += 1; log_cb !== nothing && log_cb(xk, fk)
            if fk < min(fr, fvals[end])
                simplex[end] = xk; fvals[end] = fk
            else
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
# Calibrate one country: random-restart Nelder-Mead
# -----------------------------------------------------------------------------
function calibrate_country(cfg, seedcomp, obs_band; logio = nothing)
    f = x -> eval_loss(x, cfg, seedcomp, obs_band)
    best_x = nothing; best_f = Inf
    rng = Xoshiro(20260711 + sum(Int, collect(cfg.code)))
    starts = Vector{Vector{Float64}}()
    push!(starts, pack(default_free()))
    for _ in 1:(N_RESTARTS - 1)
        push!(starts, [4.0 * (rand(rng) - 0.5) for _ in 1:NFREE])
    end
    evals_per = max(NFREE + 8, MAX_EVALS ÷ length(starts))
    for (k, x0) in enumerate(starts)
        cb = nothing
        if logio !== nothing
            cb = (xx, ff) -> begin
                nt = unpack(xx)
                @printf(logio, "%s,%d,%.6f", cfg.code, k, ff)
                for nm in FREE_NAMES
                    @printf(logio, ",%.6f", nt[nm])
                end
                println(logio)
            end
        end
        xb, fb, ev = nelder_mead(f, x0; maxevals = evals_per, log_cb = cb)
        @printf("  [%s restart %d] best loss = %.6f after %d evals\n", cfg.code, k, fb, ev)
        if best_x === nothing || (fb < best_f)
            best_f = fb; best_x = xb
        end
    end
    return unpack(best_x), best_f
end

# =============================================================================
# Pre-registered sufficiency metrics (M1-M3)
# =============================================================================
# Equal-band mean married/cohab series on the observed year grid, sim + obs.
function eqband_series(sim, obs)
    nb = length(CALIB_BANDS)
    sidx = Dict(y => i for (i, y) in enumerate(sim.years))
    years = [y for y in obs.years if haskey(sidx, y)]
    m_obs = [mean(obs.band_m[bi][findfirst(==(y), obs.years)] for bi in 1:nb) for y in years]
    c_obs = [mean(obs.band_c[bi][findfirst(==(y), obs.years)] for bi in 1:nb) for y in years]
    m_sim = [mean(sim.band_m_mean[bi][sidx[y]] for bi in 1:nb) for y in years]
    c_sim = [mean(sim.band_c_mean[bi][sidx[y]] for bi in 1:nb) for y in years]
    return (; years, m_obs, c_obs, m_sim, c_sim)
end

function mean_second_diff(years, v, y0, y1)
    idx = [i for i in eachindex(years) if y0 <= years[i] <= y1]
    length(idx) < 3 && return NaN
    d2 = [v[idx[i+1]] - 2v[idx[i]] + v[idx[i-1]] for i in 2:(length(idx)-1)]
    return mean(d2)
end

function sufficiency_metrics(cfg, sim, obs)
    s = eqband_series(sim, obs)
    y = s.years
    i0 = 1; iN = length(y)
    iL = findfirst(==(LATE_Y0), y)
    rows = NamedTuple[]

    # M1 magnitude capture (married; cohab reported, not gated)
    fall_obs = s.m_obs[i0] - s.m_obs[iN]
    fall_sim = s.m_sim[i0] - s.m_sim[iN]
    m1 = fall_sim / fall_obs
    push!(rows, (country = cfg.code, metric = "M1_magnitude_capture_married",
                 sim = m1, obs = 1.0, criterion = ">=$(M1_THRESHOLD)", pass = m1 >= M1_THRESHOLD))
    rise_obs = s.c_obs[iN] - s.c_obs[i0]
    rise_sim = s.c_sim[iN] - s.c_sim[i0]
    push!(rows, (country = cfg.code, metric = "magnitude_capture_cohab_reported",
                 sim = rise_obs == 0 ? NaN : rise_sim / rise_obs, obs = 1.0,
                 criterion = "reported", pass = true))

    # M2 late-window share of total married decline
    if iL === nothing
        push!(rows, (country = cfg.code, metric = "M2_late_share_married",
                     sim = NaN, obs = NaN, criterion = "window missing", pass = false))
    else
        ls_obs = (s.m_obs[iL] - s.m_obs[iN]) / fall_obs
        ls_sim = (s.m_sim[iL] - s.m_sim[iN]) / fall_sim
        push!(rows, (country = cfg.code, metric = "M2_late_share_married",
                     sim = ls_sim, obs = ls_obs, criterion = "|diff|<=$(M2_TOLERANCE)",
                     pass = abs(ls_sim - ls_obs) <= M2_TOLERANCE))
    end

    # M3 acceleration sign (mean second difference, 2015-2024)
    d2_obs = mean_second_diff(y, s.m_obs, ACCEL_WINDOW...)
    d2_sim = mean_second_diff(y, s.m_sim, ACCEL_WINDOW...)
    push!(rows, (country = cfg.code, metric = "M3_accel_sign_married_d2",
                 sim = d2_sim, obs = d2_obs, criterion = "same sign",
                 pass = sign(d2_sim) == sign(d2_obs)))
    return rows
end

# =============================================================================
# Identification-wall checks -> _assert_no_tfr.log
# =============================================================================
# Static checks read THIS harness and the model source; runtime check inspects
# the LOADED_CSVS registry (which files were actually opened) at the moment
# calibration finishes, BEFORE any overlay load.
function extract_function_block(src::String, fname::String)
    i = findfirst(Regex("^function $(fname)", "m"), src)
    i === nothing && return ""
    j = findnext(r"^end$"m, src, last(i))
    j === nothing && return src[first(i):end]
    return src[first(i):last(j)]
end

function run_wall_checks(io, loaded_during_calibration)
    model_src   = read(joinpath(MODEL_DIR, "stage3a_norefl_abm.jl"), String)
    harness_src = read(joinpath(MODEL_DIR, "calibrate_3a.jl"), String)
    npass = 0; nviol = 0
    check(name, ok, detail) = begin
        println(io, (ok ? "PASS      " : "VIOLATION "), name, " — ", detail)
        ok ? (npass += 1) : (nviol += 1)
    end

    # --- no-TFR (identification wall) ---
    loss_blk = extract_function_block(model_src, "composition_loss")
    check("loss_no_tfr", !occursin(r"tfr"i, loss_blk),
          "composition_loss body contains no TFR token")
    check("free_params_no_tfr", !any(occursin("tfr", String(nm)) for nm in FREE_NAMES),
          "no free parameter references TFR")
    step_blk = extract_function_block(model_src, "agent_step!") *
               extract_function_block(model_src, "model_step!")
    check("transitions_no_obs_tfr", !occursin("load_observed_tfr", step_blk) &&
                                    !occursin("tfr_csv", step_blk),
          "transition rules never read the observed TFR series")
    evalloss_blk = extract_function_block(harness_src, "eval_loss") *
                   extract_function_block(harness_src, "calibrate_country")
    check("calibration_no_tfr", !occursin(r"tfr"i, evalloss_blk),
          "eval_loss / calibrate_country reference no TFR object")
    check("runtime_no_tfr_load",
          !any(occursin("tfr", lowercase(f)) for f in loaded_during_calibration),
          "files loaded during calibration: " * join(unique(loaded_during_calibration), ", "))

    # --- no-reflexivity (2b/2c verdict carried into the code) ---
    agent_blk = extract_function_block(model_src, "agent_step!")
    check("agent_step_no_cross_agent_reads",
          !occursin("allagents", agent_blk) && !occursin("nearby_agents", agent_blk),
          "agent_step! reads no other agent's state")
    modelstep_blk = extract_function_block(model_src, "model_step!")
    check("model_step_calendar_only",
          !occursin("allagents", modelstep_blk),
          "model_step! computes no population snapshot feeding transitions")
    for tok in ("refgroup", "norm_multiplier", "map_multiplier", "fw_union_share")
        check("token_absent_$(tok)", !occursin(tok, model_src),
              "skeleton feedback identifier `$(tok)` absent from 3a model")
    end

    println(io, "----")
    @printf(io, "%d PASS / %d VIOLATION\n", npass, nviol)
    return nviol == 0
end

# =============================================================================
# Driver
# =============================================================================
function main_calibrate(codes)
    mkpath(OUT_DIR)
    @printf("\n=== STAGE 3a CALIBRATION — no-reflexivity model (threads=%d) ===\n", Threads.nthreads())
    @printf("inner: %d agents x %d seeds; final: %d agents x %d seeds; budget %d evals/country x %d restarts\n",
            INNER_AGENTS, INNER_SEEDS, FINAL_AGENTS, FINAL_SEEDS, MAX_EVALS, N_RESTARTS)
    PIN != "" && @printf("ABLATION PIN: %s (outputs tagged %s)\n", PIN, TAG)
    println("IDENTIFICATION: TFR is never loaded during calibration; checks -> _assert_no_tfr$(TAG).log")

    all_metrics = NamedTuple[]
    logf = joinpath(OUT_DIR, "calibration_log_3a$(TAG).csv")
    open(logf, "w") do io
        print(io, "country,restart,loss")
        for nm in FREE_NAMES; print(io, ",", nm); end
        println(io)

        for code in codes
            cfg = COUNTRIES[code]
            @printf("\n--- CALIBRATING %s (%d-%d) ---\n", code, cfg.year_start, cfg.year_end)
            mark = length(LOADED_CSVS)   # registry scope: THIS country's calibration only
            seedcomp = load_seed_composition(cfg)
            obs_band = load_observed_composition_bands(cfg)

            best_nt, best_loss = calibrate_country(cfg, seedcomp, obs_band; logio = io)
            @printf("  >> best loss(%s) = %.6f\n", code, best_loss)
            for nm in FREE_NAMES
                @printf("     %-22s = %.5f\n", nm, best_nt[nm])
            end

            # ---- identification-wall checks at the calibration/overlay boundary ----
            wall_ok = open(joinpath(OUT_DIR, "_assert_no_tfr$(TAG).log"),
                           code == codes[1] ? "w" : "a") do wio
                println(wio, "== $(code) — checks at end of calibration ($(FINAL_AGENTS)x$(FINAL_SEEDS) final pending) ==")
                run_wall_checks(wio, LOADED_CSVS[(mark + 1):end])
            end
            wall_ok || error("identification-wall VIOLATION for $(code) — see _assert_no_tfr.log")

            # ---- write best params ----
            bdf = DataFrame(param = collect(String.(FREE_NAMES)),
                            value = [best_nt[nm] for nm in FREE_NAMES])
            push!(bdf, ("final_loss", best_loss))
            CSV.write(joinpath(OUT_DIR, "calibration_best_$(code)$(TAG).csv"), bdf)

            # ---- FINAL confirmation at best params ----
            @printf("  Running FINAL confirmation (%d x %d) ...\n", FINAL_AGENTS, FINAL_SEEDS)
            base = run_ensemble(cfg; nseeds = FINAL_SEEDS, n_agents = FINAL_AGENTS,
                                  seedcomp = seedcomp, params_override = best_nt, seed0 = 1000)
            if PIN == ""     # headline artifacts: baseline (unpinned) run only
                write_composition_csv(cfg, base)
                write_bands_csv(cfg, base, obs_band)
                p = Params(; year = cfg.year_start); apply_params!(p, best_nt)
                write_mechanism_csvs(cfg, p)
            end

            # ---- pre-registered metrics ----
            rows = sufficiency_metrics(cfg, base, obs_band)
            append!(all_metrics, rows)
            println("  Sufficiency metrics:")
            for r in rows
                @printf("    %-38s sim=%8.4f obs=%8.4f  %-16s %s\n",
                        r.metric, r.sim, r.obs, r.criterion, r.pass ? "PASS" : "FAIL")
            end

            # ---- overlay LAST (comparison only; loaded AFTER the wall check) ----
            if PIN == ""
                obs_tfr = load_observed_tfr(cfg)
                write_tfr_overlay_csv(cfg, base, obs_tfr)
                iv = findfirst(!isnan, base.tfr_m)
                @printf("  Overlay TFR (placeholder-ASFR, comparison only): %.3f -> %.3f\n",
                        base.tfr_m[iv], base.tfr_m[end])
            end
        end
    end
    CSV.write(joinpath(OUT_DIR, "sufficiency_metrics$(TAG).csv"), DataFrame(all_metrics))
    println("\nStage 3a calibration complete. Outputs in: ", OUT_DIR)
end

if abspath(PROGRAM_FILE) == @__FILE__
    codes = isempty(ARGS) ? ["CRI", "COL"] : [uppercase(a) for a in ARGS]
    main_calibrate(codes)
end
