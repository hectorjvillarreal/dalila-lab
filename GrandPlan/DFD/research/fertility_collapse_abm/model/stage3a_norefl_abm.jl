# =============================================================================
# stage3a_norefl_abm.jl
# Stage 3a NO-REFLEXIVITY agent-based model — Rapid Fertility Collapse ABM (DFD)
# =============================================================================
#
# PURPOSE
#   Test SUFFICIENCY of the mechanism that SURVIVED Stages 2b/2c:
#     cohort-entry heterogeneity (cohort-replacement channel)
#     + an EXOGENOUS calendar-time period shock.
#   Question (STAGE3a_sufficiency_instruction.md §1): can this no-reflexivity
#   model reproduce the observed marriage-share (composition) collapse in
#   CR (ENAHO 2010-2024) and COL (GEIH 2007-2024) — magnitude AND 2015-2024
#   shape, including the late acceleration?
#
# RESPECIFICATION vs cri_skeleton_abm.jl (Stage 2 skeleton):
#   REMOVED — the coordination/social-threshold mechanism (site A) and the
#     map-side nonlinearity (site B). Both were state-dependent feedback terms;
#     2b/2c rejected within-cohort self-reinforcement (β>0 everywhere). The
#     transition rule below contains NO term that reads any other agent's state:
#     agent_step! never calls allagents() and carries no population-share input.
#     model_step! advances the calendar only. Grep-provable discipline; checked
#     by assert_no_reflexivity() in calibrate_3a.jl.
#   ADDED —
#     (1) Cohort-entry heterogeneity: each woman carries her birth_year b; a
#         cohort multiplier kappa(b) in (0,1], DECLINING across birth cohorts,
#         scales both marriage-entry margins (marry_share_of_form, cohab_to_marr).
#         Parametric (3 free params), calibrated to observed composition — the
#         across-cohort decline is NOT hard-coded (instruction §3).
#         A log-linear cohort tilt phi(b) on form_base (1 free param) lets the
#         union-total decline in young bands come through formation, not only
#         the marriage split.
#     (2) Exogenous period shock: pi(t), a calendar-time logistic multiplier on
#         the same marriage-entry margins, common across live cohorts, NOT
#         state-dependent. For CRI (2b: period insignificant) its depth is free
#         to calibrate toward zero; for COL (2b: p≈3e-6) it should come out
#         positive. The loss decides.
#   TWO-COUNTRY — CountryConfig {CRI, COL}; same bands, same A2-style seeding
#     (CRI seeds 2010, COL seeds 2007), same N1 composition loss.
#
# INHERITED DISCIPLINE (frozen invariants, Stage 1.5 / 2b / 2c):
#   (1) State variable is union COMPOSITION {single, cohabiting, married}.
#   (2) TFR is COMPARISON-ONLY overlay: never in the loss, never tunes any
#       parameter. `w` fixed at 0.6 for the overlay only (composition dynamics
#       are w-invariant by construction — Stage 2 finding). assert_no_tfr
#       carried over; log written to outputs/stage3a/.
#   (3) Fertility intensity / `w` is NOT a 3a object (gated to ENDS, Stage 3b);
#       married-ASFR remains the MEX-shape PLACEHOLDER — the overlay TFR LEVEL
#       is provisional and makes no claim.
#
# INVOCATION
#   # single confirmation run for one country (uses Params defaults or a
#   # calibration_best CSV if present), writes outputs/stage3a/:
#   JULIA_NUM_THREADS=8 julia --project=. stage3a_norefl_abm.jl CRI [nseeds]
#   # calibration (both countries): see calibrate_3a.jl
#
# INPUTS (read-only; NEVER written by this script)
#   data/coupling/CRI_coupling_annual.csv   composition target, CR 2010-2024
#   data/coupling/COL_coupling_annual.csv   composition target, COL 2007-2024
#   data/national/{CRI,COL}_tfr_national.csv  OUTPUT COMPARISON ONLY (overlay)
#
# OUTPUTS (written under model/outputs/stage3a/ — created if absent)
#   {CC}_composition_path.csv    simulated national shares, ensemble mean
#   {CC}_composition_bands.csv   per-band 20-39 sim-vs-obs trajectory (mean±sd)
#   {CC}_tfr_overlay.csv         overlay TFR path (mean±sd) vs observed [caveated]
#   {CC}_cohort_multiplier.csv   calibrated kappa(b) and phi(b) profiles
#   {CC}_period_multiplier.csv   calibrated pi(t) path
#
# DEPENDENCIES
#   Julia 1.11.7; Agents.jl v6 (pinned), CSV.jl, DataFrames.jl,
#   Distributions =0.25.116 (Agents precompile pin). CPU-parallel over seeds
#   via Threads. Agents v6 API: model properties via abmproperties(model).
#
# DOCUMENTED TO: PROTO-RAG-001 code standards.
# Build instruction: STAGE3a_sufficiency_instruction.md (Debb, 2026-07-11).
# endorsed_by: blank pending Nina (build).
#
# Author: Claude Code (Stage 3a sufficiency), DFD Core Team
# Date: 2026-07-11
# =============================================================================

using Agents
using CSV
using DataFrames
using Random
using Statistics
using Printf

# -----------------------------------------------------------------------------
# Paths (absolute; data is READ-ONLY)
# -----------------------------------------------------------------------------
const MODEL_DIR = @__DIR__
const DATA_DIR  = normpath(joinpath(MODEL_DIR, "..", "data"))
const OUT_DIR   = joinpath(MODEL_DIR, "outputs", "stage3a")

# -----------------------------------------------------------------------------
# Country configuration (two-country: CRI seeds 2010, COL seeds 2007)
# -----------------------------------------------------------------------------
struct CountryConfig
    code::String
    coupling_csv::String
    tfr_csv::String          # overlay ONLY — see identification wall
    year_start::Int          # seed year (first observed composition year)
    year_end::Int
end

const COUNTRIES = Dict(
    "CRI" => CountryConfig("CRI",
        joinpath(DATA_DIR, "coupling", "CRI_coupling_annual.csv"),
        joinpath(DATA_DIR, "national", "CRI_tfr_national.csv"),
        2010, 2024),
    # COL seeds 2008, NOT 2007: the coupling companion doc (COL_coupling_annual.md)
    # flags 2007 as a frame/questionnaire outlier (union 47.5% vs the 2008-2020
    # plateau ~59-60%) — "treat the plateau as 2008-2020". Seeding 2008 drops the
    # artifact year from both the A2 seed and the N1 loss (sim years start 2008).
    "COL" => CountryConfig("COL",
        joinpath(DATA_DIR, "coupling", "COL_coupling_annual.csv"),
        joinpath(DATA_DIR, "national", "COL_tfr_national.csv"),
        2008, 2024),
)

# Calibration bands (A4 carried over): loss scored on 20-39 only.
const CALIB_BANDS = ("20-24" => (20, 24), "25-29" => (25, 29),
                     "30-34" => (30, 34), "35-39" => (35, 39))

# N1 loss weights (carried over; ω_m = ω_c = 1).
const OMEGA_M = 1.0
const OMEGA_C = 1.0

# -----------------------------------------------------------------------------
# CSV load registry — every data file read at runtime is recorded here so the
# assert_no_tfr check can verify WHICH files were touched during calibration.
# -----------------------------------------------------------------------------
const LOADED_CSVS = String[]
function tracked_read(path::String)
    push!(LOADED_CSVS, basename(path))
    return CSV.read(path, DataFrame)
end

# -----------------------------------------------------------------------------
# Background distributions  [PROVISIONAL — carried from skeleton; structural
# context only, never tuned]
# -----------------------------------------------------------------------------
const EDU_LEVELS = (:low, :med, :high)
const EDU_SHARES = (0.35, 0.40, 0.25)
const LOC_LEVELS = (:urban, :rural)
const LOC_SHARES = (0.80, 0.20)

# -----------------------------------------------------------------------------
# Age / fertility schedule  [PLACEHOLDER — overlay only, carried verbatim from
# the skeleton. The overlay TFR LEVEL is provisional; 3a makes NO TFR claim.]
# -----------------------------------------------------------------------------
const AGE_MIN = 15
const AGE_MAX = 49
const NAGE    = AGE_MAX - AGE_MIN + 1

function married_birth_hazard(age::Int)
    μ = 27.0; σ = 6.5; peak = 0.165
    h = peak * exp(-0.5 * ((age - μ) / σ)^2)
    return clamp(h, 0.0, 0.6)
end
single_birth_hazard(age::Int) = 0.10 * married_birth_hazard(age)

# Overlay fertility weight (Invariant 2): FIXED for the overlay, not swept in 3a
# (composition dynamics are w-invariant; Stage 2 established this by construction).
const W_OVERLAY = 0.6

# -----------------------------------------------------------------------------
# Agent — birth_year added (the cohort-replacement channel's carrier)
# -----------------------------------------------------------------------------
@agent struct Woman(NoSpaceAgent)
    age::Int
    birth_year::Int       # entry cohort b — drives kappa(b), phi(b)
    edu::Symbol
    loc::Symbol
    union::Symbol         # :single :cohabiting :married  (composition state)
    parity::Int
end

# -----------------------------------------------------------------------------
# Model parameters
# -----------------------------------------------------------------------------
# FREE (12, calibrated per country in calibrate_3a.jl):
#   form_base, marry_share_of_form, cohab_to_marr, dissolve_cohab, dissolve_marr,
#   kappa_floor, kappa_mid, kappa_steep, form_tilt,
#   period_depth, period_mid, period_steep
# PINNED: the ASFR primitive (overlay placeholder), backgrounds, W_OVERLAY.
Base.@kwdef mutable struct Params
    year::Int = 2010                     # calendar year (set from CountryConfig)
    # ----- base Process-A rates (cohort-/period-invariant components) -----
    form_base::Float64 = 0.16            # base prob a single woman forms ANY union / yr
    marry_share_of_form::Float64 = 0.30  # of formed unions, share married (before kappa, pi)
    dissolve_cohab::Float64 = 0.06       # cohabiting -> single annual hazard
    dissolve_marr::Float64 = 0.015       # married -> single annual hazard
    cohab_to_marr::Float64 = 0.05        # cohabiting -> married annual hazard (before kappa, pi)
    # ----- cohort-entry heterogeneity kappa(b): logistic decline across birth cohorts -----
    kappa_floor::Float64 = 0.30          # asymptotic marriage-propensity floor for latest cohorts
    kappa_mid::Float64 = 1990.0          # birth-cohort midpoint of the decline
    kappa_steep::Float64 = 0.15          # per-birth-year logistic steepness
    # ----- formation cohort tilt phi(b): log-linear in birth year -----
    form_tilt::Float64 = 0.0             # >0 => younger cohorts form unions LESS
    # ----- exogenous period shock pi(t): calendar-time logistic, NOT state-dependent -----
    period_depth::Float64 = 0.0          # 0 => no period shock (CRI free to sit here)
    period_mid::Float64 = 2018.0         # calendar-year midpoint of the shock
    period_steep::Float64 = 0.8          # per-year logistic steepness
    # ----- bookkeeping -----
    n_agents::Int = 50_000
    # ----- per-run scratch accumulators (overlay TFR only; mutated each tick) -----
    births_by_age::Vector{Int} = zeros(Int, NAGE)
    exposure_by_age::Vector{Int} = zeros(Int, NAGE)
end

# Cohort multiplier on MARRIAGE ENTRY: kappa(b) in (kappa_floor, 1], declining
# across birth cohorts b. Old cohorts (b << kappa_mid) sit near 1; the latest
# approach kappa_floor. Applied to marry_share_of_form and cohab_to_marr.
function kappa_cohort(p::Params, b::Int)
    z = p.kappa_steep * (b - p.kappa_mid)
    return p.kappa_floor + (1.0 - p.kappa_floor) / (1.0 + exp(z))
end

# Cohort tilt on UNION FORMATION: phi(b), log-linear in birth year around a
# fixed reference cohort. Clamped to a sane multiplier range.
const FORM_TILT_REF = 1985
phi_cohort(p::Params, b::Int) = clamp(exp(-p.form_tilt * (b - FORM_TILT_REF)), 0.2, 3.0)

# Exogenous period multiplier on MARRIAGE ENTRY: pi(t), calendar time only.
# period_depth = 0 => identically 1 (no shock).
function pi_period(p::Params, t::Real)
    z = p.period_steep * (t - p.period_mid)
    return 1.0 - p.period_depth / (1.0 + exp(-z))
end

# =============================================================================
# A2-style observed-seed-year composition loader (generalized to CountryConfig)
# =============================================================================
struct SeedComposition
    married::Vector{Float64}   # length NAGE, indexed age-AGE_MIN+1
    cohab::Vector{Float64}
end

function load_seed_composition(cfg::CountryConfig)
    df = tracked_read(cfg.coupling_csv)
    d0 = df[df.year .== cfg.year_start, :]
    obs = Dict{String,Tuple{Float64,Float64}}()
    for row in eachrow(d0)
        obs[String(row.age_band)] = (Float64(row.married), Float64(row.cohabiting))
    end
    @assert haskey(obs, "20-24") && haskey(obs, "35-39") "$(cfg.code) coupling CSV missing seed-year bands"

    m = zeros(Float64, NAGE); c = zeros(Float64, NAGE)
    for (label, (lo, hi)) in CALIB_BANDS
        mm, cc = obs[label]
        for age in lo:hi
            m[age - AGE_MIN + 1] = mm
            c[age - AGE_MIN + 1] = cc
        end
    end
    # 15-19 tail: age-graded ramp below the 20-24 band (carried from skeleton).
    m20, c20 = obs["20-24"]
    for age in AGE_MIN:19
        frac = (age - AGE_MIN) / 5.0
        m[age - AGE_MIN + 1] = m20 * frac
        c[age - AGE_MIN + 1] = c20 * (0.4 + 0.6 * frac)
    end
    # 40-49 tail: hold at the 35-39 level.
    m39, c39 = obs["35-39"]
    for age in 40:AGE_MAX
        m[age - AGE_MIN + 1] = m39
        c[age - AGE_MIN + 1] = c39
    end
    return SeedComposition(m, c)
end

# =============================================================================
# Model construction
# =============================================================================
function build_model(cfg::CountryConfig; seed::Int, n_agents::Int = 50_000,
                       seedcomp::SeedComposition, params_override = nothing)
    rng = Xoshiro(seed)
    p = Params(; year = cfg.year_start, n_agents = n_agents)
    if params_override !== nothing
        apply_params!(p, params_override)
    end
    model = StandardABM(Woman; properties = p, rng = rng,
                        agent_step! = agent_step!, model_step! = model_step!)
    for _ in 1:n_agents
        age   = rand(abmrng(model), AGE_MIN:AGE_MAX)
        by    = cfg.year_start - age            # pre-seed cohorts get kappa(b) via the same form
        edu   = sample_categorical(abmrng(model), EDU_LEVELS, EDU_SHARES)
        loc   = sample_categorical(abmrng(model), LOC_LEVELS, LOC_SHARES)
        union = seed_union(abmrng(model), age, seedcomp)
        parity = seed_parity(abmrng(model), age, union)
        add_agent!(model, age, by, edu, loc, union, parity)
    end
    return model
end

# Apply a NamedTuple of free parameters (calibration) onto Params in place.
function apply_params!(p::Params, nt)
    for (k, v) in pairs(nt)
        setfield!(p, k, Float64(v))
    end
    return p
end

function sample_categorical(rng, levels, shares)
    u = rand(rng); c = 0.0
    @inbounds for i in eachindex(levels)
        c += shares[i]
        u <= c && return levels[i]
    end
    return levels[end]
end

function seed_union(rng, age::Int, sc::SeedComposition)
    i = age - AGE_MIN + 1
    pm = sc.married[i]; pc = sc.cohab[i]
    u = rand(rng)
    u < pm && return :married
    u < pm + pc && return :cohabiting
    return :single
end

function seed_parity(rng, age, union)
    base = union === :married ? 0.10 : union === :cohabiting ? 0.07 : 0.02
    expected = base * max(0, age - 18)
    return rand(rng) < (expected - floor(expected)) ? Int(ceil(expected)) : Int(floor(expected))
end

# =============================================================================
# Steps
# =============================================================================
# model_step!: advance the calendar. NOTHING ELSE — no population snapshot, no
# shared state feeding the transition rule. (Contrast with the skeleton, which
# recomputed reference-group shares here; that channel is REMOVED.)
function model_step!(model)
    abmproperties(model).year += 1
    return
end

# agent_step!: Process A (union transitions — cohort + exogenous period drivers
# ONLY, no cross-agent reads) then the overlay fertility accumulation, then
# ageing + cohort replacement (closed cohort, carried from skeleton N6).
function agent_step!(a::Woman, model)
    p = abmproperties(model)
    rng = abmrng(model)
    age0 = a.age
    ai = age0 - AGE_MIN + 1
    # The tick stepping FROM p.year produces outcomes labelled p.year+1
    # (model_step! increments after agents step). Use the produced year.
    tyear = p.year + 1
    κ = kappa_cohort(p, a.birth_year)
    π = pi_period(p, tyear)

    # ---------- Process A: union transitions ----------
    if a.union === :single
        form_p = clamp(p.form_base * phi_cohort(p, a.birth_year), 0.0, 0.95)
        if rand(rng) < form_p
            marry_p = clamp(p.marry_share_of_form * κ * π, 0.0, 1.0)
            a.union = rand(rng) < marry_p ? :married : :cohabiting
        end
    elseif a.union === :cohabiting
        if rand(rng) < p.dissolve_cohab
            a.union = :single
        elseif rand(rng) < clamp(p.cohab_to_marr * κ * π, 0.0, 0.9)
            a.union = :married
        end
    else # :married
        if rand(rng) < p.dissolve_marr
            a.union = :single
        end
    end

    # ---------- overlay fertility (COMPARISON ONLY — never in any loss) ----------
    base_h = a.union === :married    ? married_birth_hazard(age0) :
             a.union === :cohabiting ? W_OVERLAY * married_birth_hazard(age0) :
                                       single_birth_hazard(age0)
    @inbounds p.exposure_by_age[ai] += 1
    if rand(rng) < clamp(base_h, 0.0, 0.9)
        a.parity += 1
        @inbounds p.births_by_age[ai] += 1
    end

    # ---------- ageing + cohort replacement (closed cohort) ----------
    a.age += 1
    if a.age > AGE_MAX
        a.age = AGE_MIN
        a.birth_year = tyear - AGE_MIN      # NEW ENTRY COHORT — carries its own kappa/phi
        a.edu = sample_categorical(rng, EDU_LEVELS, EDU_SHARES)
        a.loc = sample_categorical(rng, LOC_LEVELS, LOC_SHARES)
        a.union = :single
        a.parity = 0
    end
    return
end

# =============================================================================
# Overlay TFR from single-year ΣASFR accumulators (carried from skeleton A1)
# =============================================================================
function tfr_from_accumulators(p::Params)
    tfr = 0.0
    @inbounds for ai in 1:NAGE
        e = p.exposure_by_age[ai]
        e > 0 && (tfr += p.births_by_age[ai] / e)
    end
    return tfr
end

# =============================================================================
# Running one ensemble member
# =============================================================================
function run_path!(model; nyears::Int)
    years    = Int[]
    tfr      = Float64[]
    f_single = Float64[]; f_cohab = Float64[]; f_marr = Float64[]
    nbands   = length(CALIB_BANDS)
    band_m   = [Float64[] for _ in 1:nbands]
    band_c   = [Float64[] for _ in 1:nbands]

    p = abmproperties(model)

    # ---- year 0 (seed year, seeded state): composition only, TFR = NaN ----
    push!(years, p.year); push!(tfr, NaN)
    s, c, m = composition_shares(model)
    push!(f_single, s); push!(f_cohab, c); push!(f_marr, m)
    record_band_composition!(model, band_m, band_c)

    # ---- stepped years ----
    for _ in 1:nyears
        fill!(p.births_by_age, 0)
        fill!(p.exposure_by_age, 0)
        step!(model, 1)
        push!(tfr, tfr_from_accumulators(p))
        push!(years, p.year)
        s, c, m = composition_shares(model)
        push!(f_single, s); push!(f_cohab, c); push!(f_marr, m)
        record_band_composition!(model, band_m, band_c)
    end
    return (; years, tfr, f_single, f_cohab, f_marr, band_m, band_c)
end

# Measurement (read-only, OUTSIDE the transition rule): population composition.
function composition_shares(model)
    n = 0; s = 0; c = 0; m = 0
    for a in allagents(model)
        n += 1
        a.union === :single     && (s += 1)
        a.union === :cohabiting && (c += 1)
        a.union === :married    && (m += 1)
    end
    n == 0 && return (0.0, 0.0, 0.0)
    return (s / n, c / n, m / n)
end

function record_band_composition!(model, band_m, band_c)
    nbands = length(CALIB_BANDS)
    cnt = zeros(Int, nbands); mar = zeros(Int, nbands); coh = zeros(Int, nbands)
    for a in allagents(model)
        for (bi, (_label, (lo, hi))) in enumerate(CALIB_BANDS)
            if lo <= a.age <= hi
                cnt[bi] += 1
                a.union === :married    && (mar[bi] += 1)
                a.union === :cohabiting && (coh[bi] += 1)
                break
            end
        end
    end
    for bi in 1:nbands
        if cnt[bi] == 0
            push!(band_m[bi], 0.0); push!(band_c[bi], 0.0)
        else
            push!(band_m[bi], mar[bi] / cnt[bi]); push!(band_c[bi], coh[bi] / cnt[bi])
        end
    end
    return
end

# =============================================================================
# Ensemble driver (CPU-parallel over seeds via Threads)
# =============================================================================
function run_ensemble(cfg::CountryConfig; nseeds::Int = 16, n_agents::Int = 50_000,
                        seedcomp::SeedComposition, params_override = nothing,
                        seed0::Int = 1000)
    nyears = cfg.year_end - cfg.year_start
    results = Vector{Any}(undef, nseeds)
    Threads.@threads for i in 1:nseeds
        model = build_model(cfg; seed = seed0 + i, n_agents = n_agents,
                              seedcomp = seedcomp, params_override = params_override)
        results[i] = run_path!(model; nyears = nyears)
    end
    return aggregate_ensemble(results)
end

function aggregate_ensemble(results)
    years = results[1].years
    M = length(years)
    nbands = length(results[1].band_m)

    function agg(field)
        A = hcat([getfield(r, field) for r in results]...)
        mn = [let v = filter(!isnan, A[i, :]); isempty(v) ? NaN : mean(v) end for i in 1:M]
        sd = [let v = filter(!isnan, A[i, :]); length(v) > 1 ? std(v) : 0.0 end for i in 1:M]
        return (mn, sd)
    end
    tfr_m, tfr_s = agg(:tfr)
    s_m, _ = agg(:f_single); c_m, _ = agg(:f_cohab); m_m, _ = agg(:f_marr)

    band_m_mean = [zeros(M) for _ in 1:nbands]
    band_c_mean = [zeros(M) for _ in 1:nbands]
    band_m_sd   = [zeros(M) for _ in 1:nbands]
    band_c_sd   = [zeros(M) for _ in 1:nbands]
    for bi in 1:nbands
        Am = hcat([r.band_m[bi] for r in results]...)
        Ac = hcat([r.band_c[bi] for r in results]...)
        for i in 1:M
            band_m_mean[bi][i] = mean(Am[i, :]); band_c_mean[bi][i] = mean(Ac[i, :])
            band_m_sd[bi][i]   = size(Am, 2) > 1 ? std(Am[i, :]) : 0.0
            band_c_sd[bi][i]   = size(Ac, 2) > 1 ? std(Ac[i, :]) : 0.0
        end
    end
    return (; years, tfr_m, tfr_s, single = s_m, cohab = c_m, married = m_m,
              band_m_mean, band_c_mean, band_m_sd, band_c_sd)
end

# =============================================================================
# Observed series
# =============================================================================
# OVERLAY ONLY — never a calibration target, never tunes a parameter. NOT loaded
# during calibration (calibrate_3a.jl loads it only AFTER the optimizer finishes
# and verifies via LOADED_CSVS — the assert_no_tfr runtime check).
function load_observed_tfr(cfg::CountryConfig)
    df = tracked_read(cfg.tfr_csv)
    return (year = df.year, tfr = df.value)
end

# Per-band observed married/cohab trajectory (the N1 calibration target).
function load_observed_composition_bands(cfg::CountryConfig)
    df = tracked_read(cfg.coupling_csv)
    years = sort(unique(df.year))
    nbands = length(CALIB_BANDS)
    band_m = [fill(NaN, length(years)) for _ in 1:nbands]
    band_c = [fill(NaN, length(years)) for _ in 1:nbands]
    yidx = Dict(y => i for (i, y) in enumerate(years))
    for row in eachrow(df)
        for (bi, (label, _)) in enumerate(CALIB_BANDS)
            if String(row.age_band) == label
                yi = yidx[row.year]
                band_m[bi][yi] = Float64(row.married)
                band_c[bi][yi] = Float64(row.cohabiting)
                break
            end
        end
    end
    return (; years, band_m, band_c)
end

# Weighted national 20-39 married/cohab (summaries and metrics).
function load_observed_composition_2039(cfg::CountryConfig)
    df = tracked_read(cfg.coupling_csv)
    g = combine(groupby(df, :year)) do sub
        wt = sub.n_women_weighted
        (married = sum(sub.married .* wt) / sum(wt),
         cohab   = sum(sub.cohabiting .* wt) / sum(wt))
    end
    sort!(g, :year)
    return g
end

# =============================================================================
# N1 — calibration loss (COMPOSITION ONLY, bands 20-39; TFR NEVER enters)
# =============================================================================
function composition_loss(sim, obs)
    nbands = length(CALIB_BANDS)
    loss = 0.0
    sidx = Dict(y => i for (i, y) in enumerate(sim.years))
    for bi in 1:nbands
        for (oj, y) in enumerate(obs.years)
            haskey(sidx, y) || continue
            si = sidx[y]
            mo = obs.band_m[bi][oj]; co = obs.band_c[bi][oj]
            (isnan(mo) || isnan(co)) && continue
            ms = sim.band_m_mean[bi][si]; cs = sim.band_c_mean[bi][si]
            loss += OMEGA_M * (ms - mo)^2 + OMEGA_C * (cs - co)^2
        end
    end
    return loss
end

# =============================================================================
# Output writers (all under outputs/stage3a/, {CC}_ prefixed)
# =============================================================================
function write_composition_csv(cfg, base)
    df = DataFrame(year = base.years, single = base.single,
                   cohabiting = base.cohab, married = base.married)
    CSV.write(joinpath(OUT_DIR, "$(cfg.code)_composition_path.csv"), df)
end

function write_bands_csv(cfg, base, obs)
    rows = DataFrame(year = Int[], age_band = String[],
                     married_sim = Float64[], married_sim_sd = Float64[],
                     cohab_sim = Float64[], cohab_sim_sd = Float64[],
                     married_obs = Union{Float64,Missing}[],
                     cohab_obs = Union{Float64,Missing}[])
    oidx = Dict(y => j for (j, y) in enumerate(obs.years))
    for (bi, (label, _)) in enumerate(CALIB_BANDS)
        for (si, y) in enumerate(base.years)
            mo = haskey(oidx, y) ? obs.band_m[bi][oidx[y]] : missing
            co = haskey(oidx, y) ? obs.band_c[bi][oidx[y]] : missing
            mo = (mo isa Float64 && isnan(mo)) ? missing : mo
            co = (co isa Float64 && isnan(co)) ? missing : co
            push!(rows, (y, label,
                         base.band_m_mean[bi][si], base.band_m_sd[bi][si],
                         base.band_c_mean[bi][si], base.band_c_sd[bi][si], mo, co))
        end
    end
    CSV.write(joinpath(OUT_DIR, "$(cfg.code)_composition_bands.csv"), rows)
end

function write_tfr_overlay_csv(cfg, base, obs_tfr)
    df = DataFrame(year = base.years,
                   tfr_overlay_mean = base.tfr_m, tfr_overlay_sd = base.tfr_s)
    df.tfr_observed = [ (oi = findfirst(==(y), obs_tfr.year);
                          oi === nothing ? missing : obs_tfr.tfr[oi]) for y in df.year ]
    CSV.write(joinpath(OUT_DIR, "$(cfg.code)_tfr_overlay.csv"), df)
end

# Calibrated mechanism profiles (for figures and the cohort-gradient fit check).
function write_mechanism_csvs(cfg, p::Params)
    bs = (cfg.year_start - AGE_MAX):(cfg.year_end - AGE_MIN)   # all birth cohorts alive in-span
    dfk = DataFrame(birth_year = collect(bs),
                    kappa = [kappa_cohort(p, b) for b in bs],
                    phi = [phi_cohort(p, b) for b in bs])
    CSV.write(joinpath(OUT_DIR, "$(cfg.code)_cohort_multiplier.csv"), dfk)
    ts = cfg.year_start:cfg.year_end
    dfp = DataFrame(year = collect(ts), pi = [pi_period(p, t) for t in ts])
    CSV.write(joinpath(OUT_DIR, "$(cfg.code)_period_multiplier.csv"), dfp)
end

# =============================================================================
# Main: single confirmation run for one country (defaults or best-params CSV)
# =============================================================================
function load_best_params(cfg::CountryConfig)
    f = joinpath(OUT_DIR, "calibration_best_$(cfg.code).csv")
    isfile(f) || return nothing
    df = CSV.read(f, DataFrame)
    d = Dict(Symbol(r.param) => r.value for r in eachrow(df) if !startswith(String(r.param), "final_"))
    return NamedTuple(d)
end

function main(country::String; nseeds::Int = 16, n_agents::Int = 50_000)
    cfg = COUNTRIES[country]
    mkpath(OUT_DIR)
    best = load_best_params(cfg)
    @printf("\n=== STAGE 3a NO-REFLEXIVITY ABM — %s, %d seeds, %d agents, threads=%d, params=%s ===\n",
            cfg.code, nseeds, n_agents, Threads.nthreads(),
            best === nothing ? "DEFAULTS" : "calibration_best")

    seedcomp = load_seed_composition(cfg)
    obs_band = load_observed_composition_bands(cfg)
    obs_comp = load_observed_composition_2039(cfg)

    base = run_ensemble(cfg; nseeds = nseeds, n_agents = n_agents,
                          seedcomp = seedcomp, params_override = best)

    # overlay LAST (comparison only)
    obs_tfr = load_observed_tfr(cfg)
    write_composition_csv(cfg, base)
    write_bands_csv(cfg, base, obs_band)
    write_tfr_overlay_csv(cfg, base, obs_tfr)
    p = Params(; year = cfg.year_start)
    best !== nothing && apply_params!(p, best)
    write_mechanism_csvs(cfg, p)

    L = composition_loss(base, obs_band)
    @printf("\nComposition (sim 20-39 eq-band, %d)  married=%.3f cohab=%.3f\n",
            cfg.year_end, mean(base.band_m_mean[bi][end] for bi in 1:4),
            mean(base.band_c_mean[bi][end] for bi in 1:4))
    @printf("Composition (obs 20-39 wt,   %d)  married=%.3f cohab=%.3f\n",
            cfg.year_end, obs_comp.married[end], obs_comp.cohab[end])
    @printf("N1 composition loss: %.5f\n", L)
    println("Outputs written to: ", OUT_DIR)
    return (; base, obs_band, obs_comp, loss = L)
end

if abspath(PROGRAM_FILE) == @__FILE__
    country = length(ARGS) >= 1 ? uppercase(ARGS[1]) : "CRI"
    ns      = length(ARGS) >= 2 ? parse(Int, ARGS[2]) : 16
    main(country; nseeds = ns)
end
