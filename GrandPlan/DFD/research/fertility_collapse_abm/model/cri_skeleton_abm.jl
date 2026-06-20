# =============================================================================
# cri_skeleton_abm.jl
# Stage 2 SKELETON agent-based model — Rapid Fertility Collapse ABM (DFD)
# =============================================================================
#
# PURPOSE
#   Prove, mechanism-first, that a THRESHOLD in the coupling dynamics can
#   generate the observed Costa Rica TFR collapse (1.83 -> 1.12, 2010-2024)
#   ENDOGENOUSLY, from independent inputs, WITHOUT ever fitting to TFR.
#   This is the single-country (Costa Rica), CPU-parallel skeleton that must
#   pass before the four-country nesting model and the GPU sweep are built.
#
#   The skeleton operationalises the three FROZEN INVARIANTS from the
#   Stage 1.5 identification gate (STAGE1_5_identification_memo.md, v3.0):
#     (1) State variable is union COMPOSITION: each agent is one of
#         {single, cohabiting, married} — never just "partnered/not".
#     (2) `w` (cohabiting/married fertility-intensity ratio, 0..1) is a NESTED
#         STRUCTURAL PARAMETER, not a hard-coded constant. Swept over {0.4,0.6,0.8}.
#     (3) The nonlinearity locus is `w`-DETERMINED, not assumed. The model carries
#         TWO candidate threshold sites and lets behaviour, not a flag, decide:
#           - Process A: partnership formation, social-norm / reference-group
#             threshold  -> COUPLING-side locus.
#           - Process B: the coupling->fertility map, a (provisional) nonlinearity
#             -> MAP-side locus.
#
# STAGE 2 CALIBRATION CHANGES (per STAGE2_calibration_instruction.md, Anne+Nina):
#   A1  Proper period-TFR via single-year ΣASFR (births_by_age / exposure_by_age).
#   A2  Seed the 2010 population from the OBSERVED 2010 composition (coupling CSV),
#       age-band-specific, with an age-graded gradient on the 15-19 / 40-49 tails.
#   A3  Married-ASFR kept as the MEX-shape Gaussian [PLACEHOLDER — CR acquisition
#       flagged for Debb]; cohab = w*married; single = 0.10*married [PROVISIONAL].
#   A4  Keep 15-49 for the TFR level; calibrate Process A on the 20-39 bands only.
#   A5  Parity-independent hazard. The skeleton makes NO tempo claim.
#   N1  Loss = Σ_bands Σ_years [ ω_m(m_sim-m_obs)^2 + ω_c(c_sim-c_obs)^2 ],
#       composition ONLY, bands 20-39. TFR is NEVER in the loss.
#   N2  marriage_drift = 0, PINNED. The model_step! drift decay is a no-op. The
#       social-norm threshold must GENERATE the marriage collapse endogenously.
#       Free params: norm_strength, norm_threshold, norm_steepness, form_base,
#       marry_share_of_form, cohab_to_marr, dissolve_cohab, dissolve_marr.
#   N3  Locus 2x2 grid (site A x site B) per w — see calibrate.jl.
#   N5  Calibration inner loop cheap (12k x 4); reported runs 50k x 16, mean+-sd.
#
# INVOCATION
#   # single confirmation run (baseline + falsification), writes outputs/:
#   JULIA_NUM_THREADS=8 julia --project=. cri_skeleton_abm.jl <w> <nseeds>
#   # e.g.  JULIA_NUM_THREADS=8 julia --project=. cri_skeleton_abm.jl 0.6 16
#
#   # full calibration + N3 locus grid sweep (EXPENSIVE — separate script):
#   JULIA_NUM_THREADS=8 julia --project=. calibrate.jl
#
#   # figures / figure-data CSVs:
#   JULIA_NUM_THREADS=8 julia --project=. make_figures.jl
#
# INPUTS  (read-only; NEVER written by this script)
#   data/coupling/CRI_coupling_annual.csv
#       Process A CALIBRATION TARGET. Observed annual union composition of women
#       20-39 in Costa Rica, by 5-yr band, married vs cohabiting (2010-2024).
#       This is the ONLY series Process A is calibrated to. Also the A2 seed source.
#   data/national/CRI_tfr_national.csv
#       OUTPUT COMPARISON ONLY (1.83 -> 1.12). Loaded solely to score the model's
#       GENERATED TFR against observation. NEVER a calibration target, NEVER tunes
#       any parameter. (Identification discipline, non-negotiable, from Stage 1.)
#
# OUTPUTS  (written under model/outputs/ — created if absent)
#   tfr_path_w{NN}.csv          generated annual TFR path, ensemble mean +/- sd
#   composition_path_w{NN}.csv  simulated single/cohabiting/married national shares
#   composition_bands_w{NN}.csv simulated per-band 20-39 married/cohab trajectory
#   (printed) first-look generated-vs-observed TFR + composition comparison
#
# DEPENDENCIES
#   Julia 1.11.7; Agents.jl v6 (pinned), CSV.jl, DataFrames.jl, Distributions
#   (=0.25.116 pin, Agents precompile constraint), Random, Statistics, Printf.
#   CPU-parallel ONLY: the ENSEMBLE over seeds is parallelised with Threads.
#
# Agents v6 API note: model properties are accessed via abmproperties(model),
#   NOT model.properties.
#
# DOCUMENTED TO: PROTO-RAG-001 code standards. endorsed_by: blank pending Anne+Nina.
#
# Author: Claude Code (Stage 2 calibration), DFD Core Team
# Date: 2026-06-19
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
const MODEL_DIR    = @__DIR__
const DATA_DIR     = normpath(joinpath(MODEL_DIR, "..", "data"))
const COUPLING_CSV = joinpath(DATA_DIR, "coupling", "CRI_coupling_annual.csv")
const TFR_CSV      = joinpath(DATA_DIR, "national", "CRI_tfr_national.csv")
const OUT_DIR      = joinpath(MODEL_DIR, "outputs")

# Calendar span: one tick = one year, 2010 (seed) .. 2024.
const YEAR_START = 2010
const YEAR_END   = 2024

# Calibration bands (A4): Process A loss is scored on 20-39 only.
# Band label -> (age_lo, age_hi).
const CALIB_BANDS = ("20-24" => (20, 24), "25-29" => (25, 29),
                     "30-34" => (30, 34), "35-39" => (35, 39))

# N1 loss weights (exposed as constants; ω_m = ω_c = 1).
const OMEGA_M = 1.0
const OMEGA_C = 1.0

# -----------------------------------------------------------------------------
# Background distributions  [PROVISIONAL — flagged for Anne to pin to CR data]
# -----------------------------------------------------------------------------
const EDU_LEVELS = (:low, :med, :high)
const EDU_SHARES = (0.35, 0.40, 0.25)          # [PROVISIONAL]
const LOC_LEVELS = (:urban, :rural)
const LOC_SHARES = (0.80, 0.20)                # [PROVISIONAL]

# -----------------------------------------------------------------------------
# Age / fertility schedule  [PLACEHOLDER regional prior — NOT fitted to CR TFR]
# -----------------------------------------------------------------------------
const AGE_MIN = 15
const AGE_MAX = 49
const NAGE    = AGE_MAX - AGE_MIN + 1          # single-year age bins, 15..49

# MARRIED-union per-woman annual birth probability by single year of age.
# [PLACEHOLDER — CR married-ASFR acquisition flagged for Debb; criterion-1 verdict
#  PROVISIONAL until the CR INEC married-specific schedule replaces this MEX-shape
#  Gaussian. This LEVEL is a structural primitive, NEVER tuned to reproduce CR TFR.]
function married_birth_hazard(age::Int)
    μ = 27.0; σ = 6.5; peak = 0.165
    h = peak * exp(-0.5 * ((age - μ) / σ)^2)
    return clamp(h, 0.0, 0.6)
end

# Single-woman (out-of-union) baseline birth hazard.
# [PROVISIONAL, likely understated — CR has high non-marital fertility; set from CR
#  data once A3 is acquired.]
single_birth_hazard(age::Int) = 0.10 * married_birth_hazard(age)

# -----------------------------------------------------------------------------
# Agent
# -----------------------------------------------------------------------------
# Union status as a Symbol in {:single, :cohabiting, :married} (INVARIANT 1).
@agent struct Woman(NoSpaceAgent)
    age::Int
    edu::Symbol           # :low :med :high   (fixed background)
    loc::Symbol           # :urban :rural     (fixed background)
    union::Symbol         # :single :cohabiting :married  (dynamic composition state)
    parity::Int           # number of children (parity tracked; A5: hazard parity-INDEPENDENT)
end

ispartnered(a::Woman) = a.union !== :single

# -----------------------------------------------------------------------------
# Model parameters
# -----------------------------------------------------------------------------
Base.@kwdef mutable struct Params
    # ----- structural -----
    w::Float64 = 0.6                  # INVARIANT 2: cohabiting/married fertility ratio
    year::Int = YEAR_START
    # ----- Process A: partnership formation/dissolution (COUPLING-side site A) -----
    form_base::Float64 = 0.16            # base prob a single woman forms ANY union / yr
    marry_share_of_form::Float64 = 0.45  # of formed unions, share that are marriages
    dissolve_cohab::Float64 = 0.06       # cohabiting -> single annual hazard
    dissolve_marr::Float64 = 0.015       # married -> single annual hazard
    cohab_to_marr::Float64 = 0.05        # cohabiting -> married annual hazard
    # social-norm / reference-group THRESHOLD (site A):
    social_norm_on::Bool = true          # falsification switch (criterion 4)
    norm_strength::Float64 = 0.55        # how strongly ref-group partnered-share moves formation
    norm_threshold::Float64 = 0.42       # reference-group partnered-share threshold
    norm_steepness::Float64 = 14.0       # logistic steepness of the threshold
    # secular drift in the marriage margin:
    # N2: PINNED to 0.0. The marriage collapse must be GENERATED by the threshold,
    # NOT assumed via an exogenous drift. model_step! makes the decay a no-op.
    marriage_drift::Float64 = 0.0        # PINNED 0.0 (N2). Do not free this.
    # ----- Process B: coupling -> fertility map (MAP-side site B) -----
    map_nonlinearity_on::Bool = false    # provisional map-side threshold (OFF by default)
    map_threshold::Float64 = 0.45        # fertility-weighted-union share threshold (map-side)
    map_steepness::Float64 = 10.0
    map_depth::Float64 = 0.0             # extra suppression below threshold (0 => no map nonlinearity)
    # ----- bookkeeping -----
    n_agents::Int = 50_000
    # ----- per-run scratch accumulators (mutated each tick; NOT parameters) -----
    # A1: single-year-age births and exposure for the proper ΣASFR estimator.
    births_by_age::Vector{Int} = zeros(Int, NAGE)
    exposure_by_age::Vector{Int} = zeros(Int, NAGE)
    fw_union_share::Float64 = 0.0
    refshares::Vector{Float64} = Float64[]
end

# -----------------------------------------------------------------------------
# Reference-group partnered share (social-norm term feeding Process A) — N4: same
# age-band only for the skeleton.
# -----------------------------------------------------------------------------
ageband5(age::Int) = clamp((age - AGE_MIN) ÷ 5, 0, (AGE_MAX - AGE_MIN) ÷ 5)

function refgroup_partnered_shares(model)
    nb = (AGE_MAX - AGE_MIN) ÷ 5 + 1
    cnt = zeros(Int, nb); part = zeros(Int, nb)
    for a in allagents(model)
        b = ageband5(a.age) + 1
        cnt[b] += 1
        part[b] += ispartnered(a) ? 1 : 0
    end
    return [cnt[b] == 0 ? 0.0 : part[b] / cnt[b] for b in 1:nb]
end

# Logistic threshold response (COUPLING-side, site A): below `threshold` the
# formation incentive drops sharply (the social-norm collapse).
function norm_multiplier(p::Params, ref_share::Float64)
    p.social_norm_on || return 1.0          # FALSIFICATION: norm off => flat multiplier
    z = p.norm_steepness * (ref_share - p.norm_threshold)
    lo = 1.0 - p.norm_strength
    return lo + (1.0 - lo) * (1.0 / (1.0 + exp(-z)))
end

# Map-side (site B) nonlinearity multiplier on fertility, keyed to the
# fertility-weighted-union share. OFF unless map_nonlinearity_on & map_depth>0.
function map_multiplier(p::Params, fw_union_share::Float64)
    (p.map_nonlinearity_on && p.map_depth > 0.0) || return 1.0
    z = p.map_steepness * (fw_union_share - p.map_threshold)
    suppression = p.map_depth * (1.0 - 1.0 / (1.0 + exp(-z)))
    return clamp(1.0 - suppression, 0.0, 1.0)
end

# =============================================================================
# A2 — observed-2010 seed composition loader
# =============================================================================
# Returns, for each single-year age 15..49, the (married, cohab) seeding
# probabilities for 2010. Bands 20-39 come straight from the observed 2010
# composition in the coupling CSV. The 15-19 and 40-49 tails (not in the CSV) are
# extrapolated with an age-graded gradient from the nearest observed band:
#   - 15-19: lower than 20-24 (younger women less partnered) — scaled down.
#   - 40-49: ~ 35-39 (held flat at the oldest observed band level).
struct SeedComposition
    married::Vector{Float64}   # length NAGE, indexed age-AGE_MIN+1
    cohab::Vector{Float64}     # length NAGE
end

function load_seed_composition_2010()
    df = CSV.read(COUPLING_CSV, DataFrame)
    d10 = df[df.year .== YEAR_START, :]
    # band label -> observed (married, cohab) in 2010
    obs = Dict{String,Tuple{Float64,Float64}}()
    for row in eachrow(d10)
        obs[String(row.age_band)] = (Float64(row.married), Float64(row.cohabiting))
    end
    @assert haskey(obs, "20-24") && haskey(obs, "35-39") "coupling CSV missing 2010 bands"

    m = zeros(Float64, NAGE); c = zeros(Float64, NAGE)
    # fill observed bands 20-39 (constant within band)
    for (label, (lo, hi)) in CALIB_BANDS
        mm, cc = obs[label]
        for age in lo:hi
            m[age - AGE_MIN + 1] = mm
            c[age - AGE_MIN + 1] = cc
        end
    end
    # 15-19 tail: age-graded gradient below the 20-24 band (younger -> less partnered).
    # Linear ramp from a low floor at 15 up to the 20-24 level at 19.
    m20, c20 = obs["20-24"]
    for age in AGE_MIN:19
        # frac runs 0 (age 15) .. ~0.8 (age 19); 15-19 strictly below 20-24
        frac = (age - AGE_MIN) / 5.0          # 0.0, 0.2, 0.4, 0.6, 0.8
        m[age - AGE_MIN + 1] = m20 * frac
        c[age - AGE_MIN + 1] = c20 * (0.4 + 0.6 * frac)  # cohab tail flatter than marriage
    end
    # 40-49 tail: hold at the 35-39 (oldest observed) band level.
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
function build_model(; w::Float64, seed::Int, n_agents::Int = 50_000,
                       social_norm_on::Bool = true,
                       map_nonlinearity_on::Bool = false, map_depth::Float64 = 0.0,
                       seedcomp::SeedComposition,
                       params_override = nothing)
    rng = Xoshiro(seed)
    p = Params(; w = w, n_agents = n_agents, social_norm_on = social_norm_on,
                 map_nonlinearity_on = map_nonlinearity_on, map_depth = map_depth)
    # apply calibrated free parameters (NamedTuple) if supplied
    if params_override !== nothing
        apply_params!(p, params_override)
    end
    model = StandardABM(Woman; properties = p, rng = rng,
                        agent_step! = agent_step!, model_step! = model_step!)

    # ---- A2: seed the initial population at the OBSERVED 2010 composition ----
    for _ in 1:n_agents
        age   = rand(abmrng(model), AGE_MIN:AGE_MAX)
        edu   = sample_categorical(abmrng(model), EDU_LEVELS, EDU_SHARES)
        loc   = sample_categorical(abmrng(model), LOC_LEVELS, LOC_SHARES)
        union = seed_union(abmrng(model), age, seedcomp)
        parity = seed_parity(abmrng(model), age, union)
        add_agent!(model, age, edu, loc, union, parity)
    end
    return model
end

# Apply a NamedTuple of free parameters (calibration) onto Params in place.
# Only the N2 free set is writable here; marriage_drift stays pinned at 0.0.
function apply_params!(p::Params, nt)
    for (k, v) in pairs(nt)
        k === :marriage_drift && continue   # PINNED — refuse to set
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

# A2: seed union status directly from the observed 2010 age-specific (married,
# cohab) probabilities. No flat start_married/start_cohab anymore.
function seed_union(rng, age::Int, sc::SeedComposition)
    i = age - AGE_MIN + 1
    pm = sc.married[i]; pc = sc.cohab[i]
    u = rand(rng)
    u < pm && return :married
    u < pm + pc && return :cohabiting
    return :single
end

# Seed parity roughly consistent with age & union (provisional; NOT a target).
function seed_parity(rng, age, union)
    base = union === :married ? 0.10 : union === :cohabiting ? 0.07 : 0.02
    expected = base * max(0, age - 18)
    return rand(rng) < (expected - floor(expected)) ? Int(ceil(expected)) : Int(floor(expected))
end

# =============================================================================
# Steps
# =============================================================================
# model_step!: advance the year and recompute the reference-group snapshot once
# per tick. N2: marriage_drift is PINNED 0.0, so the drift decay below is a
# NO-OP — kept explicit so the pin is visible and auditable. The marriage
# collapse must be GENERATED by the social-norm threshold, not drifted in.
function model_step!(model)
    p = abmproperties(model)
    p.year += 1
    if p.marriage_drift != 0.0
        # N2-PINNED path: never taken in the calibrated runs (drift == 0).
        p.marry_share_of_form = max(0.05, p.marry_share_of_form - p.marriage_drift)
        p.cohab_to_marr       = max(0.005, p.cohab_to_marr - 0.15 * p.marriage_drift)
    end
    p.refshares      = refgroup_partnered_shares(model)
    p.fw_union_share = fertility_weighted_union_share(model)
    return
end

function fertility_weighted_union_share(model)
    p = abmproperties(model)
    n = 0; s = 0.0
    for a in allagents(model)
        n += 1
        s += a.union === :married ? 1.0 : a.union === :cohabiting ? p.w : 0.0
    end
    return n == 0 ? 0.0 : s / n
end

# agent_step!: Process A (union transitions w/ social-norm threshold) then
# Process B (fertility w/ `w` weight and optional map-side nonlinearity), then
# ageing + cohort replacement.
function agent_step!(a::Woman, model)
    p = abmproperties(model)
    rng = abmrng(model)
    age0 = a.age                            # A1: capture age BEFORE ageing
    ai = age0 - AGE_MIN + 1
    ref = p.refshares[ageband5(age0) + 1]
    nm = norm_multiplier(p, ref)            # COUPLING-side threshold (site A)

    # ---------- Process A: partnership formation / dissolution ----------
    if a.union === :single
        form_p = clamp(p.form_base * nm, 0.0, 0.95)
        if rand(rng) < form_p
            a.union = rand(rng) < p.marry_share_of_form ? :married : :cohabiting
        end
    elseif a.union === :cohabiting
        if rand(rng) < p.dissolve_cohab
            a.union = :single
        elseif rand(rng) < p.cohab_to_marr
            a.union = :married
        end
    else # :married
        if rand(rng) < p.dissolve_marr
            a.union = :single
        end
    end

    # ---------- Process B: coupling -> fertility map ----------
    base_h = a.union === :married    ? married_birth_hazard(age0) :
             a.union === :cohabiting ? p.w * married_birth_hazard(age0) :
                                       single_birth_hazard(age0)
    mm = map_multiplier(p, p.fw_union_share)        # MAP-side threshold (site B)
    birth_p = clamp(base_h * mm, 0.0, 0.9)

    # A1: accumulate exposure (one woman-year at age0) and births BY SINGLE-YEAR AGE.
    @inbounds p.exposure_by_age[ai] += 1
    if rand(rng) < birth_p
        a.parity += 1
        @inbounds p.births_by_age[ai] += 1
    end

    # ---------- ageing + cohort replacement (closed cohort, N6) ----------
    a.age += 1
    if a.age > AGE_MAX
        a.age = AGE_MIN
        a.edu = sample_categorical(rng, EDU_LEVELS, EDU_SHARES)
        a.loc = sample_categorical(rng, LOC_LEVELS, LOC_SHARES)
        a.union = :single
        a.parity = 0
    end
    return
end

# =============================================================================
# A1 — proper period-TFR from single-year ΣASFR
# =============================================================================
# TFR(t) = Σ_a births_by_age[a] / exposure_by_age[a]  over ages with exposure>0,
# a = 15..49. Exposure is woman-years lived at each single age during the year
# (one per agent per year at her age0, captured in agent_step!).
function tfr_from_accumulators(p::Params)
    tfr = 0.0
    @inbounds for ai in 1:NAGE
        e = p.exposure_by_age[ai]
        e > 0 && (tfr += p.births_by_age[ai] / e)
    end
    return tfr
end

# =============================================================================
# Running one ensemble member: annual TFR + national + per-band composition paths
# =============================================================================
# The seeded 2010 state is recorded as the year-0 composition point (so the path
# spans 2010..2024, 15 points, aligned with the observed series). TFR is recorded
# from 2011 onward (a TFR needs a year of accumulated births/exposure); the 2010
# TFR slot is the seed and left as NaN (no exposure accumulated for the seed year).
function run_path!(model; nyears::Int)
    years    = Int[]
    tfr      = Float64[]
    f_single = Float64[]; f_cohab = Float64[]; f_marr = Float64[]
    # per-band (20-39) married/cohab trajectories — the N1 calibration target
    nbands   = length(CALIB_BANDS)
    band_m   = [Float64[] for _ in 1:nbands]
    band_c   = [Float64[] for _ in 1:nbands]

    p = abmproperties(model)
    p.refshares      = refgroup_partnered_shares(model)
    p.fw_union_share = fertility_weighted_union_share(model)

    # ---- year 0 (2010, seeded state): composition only, TFR = NaN ----
    push!(years, YEAR_START); push!(tfr, NaN)
    s, c, m = composition_shares(model)
    push!(f_single, s); push!(f_cohab, c); push!(f_marr, m)
    record_band_composition!(model, band_m, band_c)

    # ---- stepped years (2011..2024) ----
    for t in 1:nyears
        fill!(p.births_by_age, 0)
        fill!(p.exposure_by_age, 0)
        step!(model, 1)                       # one tick = one year
        push!(tfr, tfr_from_accumulators(p))  # A1 proper ΣASFR
        push!(years, p.year)
        s, c, m = composition_shares(model)
        push!(f_single, s); push!(f_cohab, c); push!(f_marr, m)
        record_band_composition!(model, band_m, band_c)
    end
    return (; years, tfr, f_single, f_cohab, f_marr, band_m, band_c)
end

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

# Per-band (20-39) married/cohab shares, pushed onto the trajectory accumulators.
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
function run_ensemble(; w::Float64, nseeds::Int = 16, nyears::Int = 14,
                        n_agents::Int = 50_000, social_norm_on::Bool = true,
                        map_nonlinearity_on::Bool = false, map_depth::Float64 = 0.0,
                        seedcomp::SeedComposition, params_override = nothing,
                        seed0::Int = 1000)
    results = Vector{Any}(undef, nseeds)
    Threads.@threads for i in 1:nseeds
        model = build_model(; w = w, seed = seed0 + i, n_agents = n_agents,
                              social_norm_on = social_norm_on,
                              map_nonlinearity_on = map_nonlinearity_on,
                              map_depth = map_depth, seedcomp = seedcomp,
                              params_override = params_override)
        results[i] = run_path!(model; nyears = nyears)
    end
    return aggregate_ensemble(results)
end

# Aggregate mean ± sd across seeds, by year. NaN-aware for the TFR seed slot.
function aggregate_ensemble(results)
    years = results[1].years
    M = length(years)
    nbands = length(results[1].band_m)

    function agg(field)
        A = hcat([getfield(r, field) for r in results]...)   # M x nseeds
        mn = [let v = filter(!isnan, A[i, :]); isempty(v) ? NaN : mean(v) end for i in 1:M]
        sd = [let v = filter(!isnan, A[i, :]); length(v) > 1 ? std(v) : 0.0 end for i in 1:M]
        return (mn, sd)
    end
    tfr_m, tfr_s = agg(:tfr)
    s_m, _ = agg(:f_single); c_m, _ = agg(:f_cohab); m_m, _ = agg(:f_marr)

    # per-band: mean over seeds at each (band, year)
    band_m_mean = [zeros(M) for _ in 1:nbands]
    band_c_mean = [zeros(M) for _ in 1:nbands]
    band_m_sd   = [zeros(M) for _ in 1:nbands]
    band_c_sd   = [zeros(M) for _ in 1:nbands]
    for bi in 1:nbands
        Am = hcat([r.band_m[bi] for r in results]...)   # M x nseeds
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
# OUTPUT COMPARISON ONLY — never a calibration target, never tunes a parameter.
function load_observed_tfr()
    df = CSV.read(TFR_CSV, DataFrame)
    return (year = df.year, tfr = df.value)
end

# Per-band observed married/cohab trajectory (the N1 calibration target). Returns
# a NamedTuple of (years, band_m, band_c) where band_* are Vector{Vector} indexed
# [band][year], aligned to CALIB_BANDS order and YEAR_START..YEAR_END.
function load_observed_composition_bands()
    df = CSV.read(COUPLING_CSV, DataFrame)
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

# Weighted national 20-39 married/cohab (for the print summary only).
function load_observed_composition_2039()
    df = CSV.read(COUPLING_CSV, DataFrame)
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
# Loss = Σ_bands Σ_years [ ω_m (m_sim - m_obs)^2 + ω_c (c_sim - c_obs)^2 ].
# `sim` is an aggregate_ensemble result; `obs` is load_observed_composition_bands().
# Years are matched by value; the seed year (2010) is included.
function composition_loss(sim, obs)
    nbands = length(CALIB_BANDS)
    loss = 0.0
    # map sim years -> index
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
# Output writers
# =============================================================================
function write_tfr_csv(w, base, fals, obs_tfr; suffix = "")
    df = DataFrame(year = base.years,
                   tfr_generated_mean = base.tfr_m,
                   tfr_generated_sd = base.tfr_s,
                   tfr_falsification_mean = fals === nothing ? fill(missing, length(base.years)) : fals.tfr_m)
    df.tfr_observed = [ (oi = findfirst(==(y), obs_tfr.year);
                          oi === nothing ? missing : obs_tfr.tfr[oi]) for y in df.year ]
    CSV.write(joinpath(OUT_DIR, @sprintf("tfr_path_w%02d%s.csv", round(Int, 100w), suffix)), df)
end

function write_composition_csv(w, base; suffix = "")
    df = DataFrame(year = base.years, single = base.single,
                   cohabiting = base.cohab, married = base.married)
    CSV.write(joinpath(OUT_DIR, @sprintf("composition_path_w%02d%s.csv", round(Int, 100w), suffix)), df)
end

function write_bands_csv(w, base, obs; suffix = "")
    rows = DataFrame(year = Int[], age_band = String[],
                     married_sim = Float64[], married_sim_sd = Float64[],
                     cohab_sim = Float64[], cohab_sim_sd = Float64[],
                     married_obs = Union{Float64,Missing}[],
                     cohab_obs = Union{Float64,Missing}[])
    sidx = Dict(y => i for (i, y) in enumerate(base.years))
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
    CSV.write(joinpath(OUT_DIR, @sprintf("composition_bands_w%02d%s.csv", round(Int, 100w), suffix)), rows)
end

# =============================================================================
# Main: single confirmation run (baseline + falsification)
# =============================================================================
function main(; w::Float64 = 0.6, nseeds::Int = 16, n_agents::Int = 50_000,
                params_override = nothing)
    mkpath(OUT_DIR)
    @printf("\n=== CRI SKELETON ABM — w=%.2f, %d seeds, %d agents, threads=%d ===\n",
            w, nseeds, n_agents, Threads.nthreads())

    seedcomp = load_seed_composition_2010()
    obs_tfr  = load_observed_tfr()
    obs_band = load_observed_composition_bands()
    obs_comp = load_observed_composition_2039()
    nyears   = YEAR_END - YEAR_START          # 14 stepped years (2011..2024)

    @info "Running BASELINE ensemble (social_norm_on = true) ..."
    base = run_ensemble(; w = w, nseeds = nseeds, nyears = nyears, n_agents = n_agents,
                          seedcomp = seedcomp, params_override = params_override)

    @info "Running FALSIFICATION ensemble (social_norm_on = false) ..."
    fals = run_ensemble(; w = w, nseeds = nseeds, nyears = nyears, n_agents = n_agents,
                          social_norm_on = false, seedcomp = seedcomp,
                          params_override = params_override)

    write_tfr_csv(w, base, fals, obs_tfr)
    write_composition_csv(w, base)
    write_bands_csv(w, base, obs_band)

    # ---- first-look comparison ----
    @printf("\n--- GENERATED vs OBSERVED TFR (w=%.2f) ---\n", w)
    @printf("%-6s  %-10s  %-12s  %-12s\n", "year", "obs", "gen(norm)", "gen(falsif)")
    for (i, yr) in enumerate(base.years)
        oi = findfirst(==(yr), obs_tfr.year)
        ov = oi === nothing ? NaN : obs_tfr.tfr[oi]
        gv = base.tfr_m[i]; fv = fals.tfr_m[i]
        @printf("%-6d  %-10.3f  %-12.3f  %-12.3f\n", yr, ov, gv, fv)
    end
    # Endpoints: first valid (2011) -> last (2024).
    iv = findfirst(!isnan, base.tfr_m)
    o0 = obs_tfr.tfr[1]; o1 = obs_tfr.tfr[end]
    g0 = base.tfr_m[iv]; g1 = base.tfr_m[end]; f1 = fals.tfr_m[end]
    @printf("\nObserved   2010->2024: %.2f -> %.2f  (%.0f%%)\n", o0, o1, 100*(o1-o0)/o0)
    @printf("Generated  (norm ON)  : %.2f -> %.2f  (%.0f%%)\n", g0, g1, 100*(g1-g0)/g0)
    @printf("Generated  (norm OFF) : %.2f -> %.2f  (%.0f%%)  [falsification]\n",
            g0, f1, 100*(f1-g0)/g0)
    @printf("\nComposition (sim 20-39 weighted, 2024)  married=%.3f cohab=%.3f\n",
            band_weighted_share(base, :married, :end), band_weighted_share(base, :cohab, :end))
    @printf("Composition (obs 20-39, 2024)           married=%.3f cohab=%.3f\n",
            obs_comp.married[end], obs_comp.cohab[end])
    L = composition_loss(base, obs_band)
    @printf("\nN1 composition loss (bands 20-39, all years): %.5f\n", L)
    println("\nOutputs written to: ", OUT_DIR)
    return (; base, fals, obs_tfr, obs_band, obs_comp, loss = L)
end

# Equal-band-weighted (simple mean across the 4 calibration bands) sim share at a
# year index for the print summary (`yi == end` allowed).
function band_weighted_share(sim, which::Symbol, yi)
    nbands = length(CALIB_BANDS)
    acc = 0.0
    for bi in 1:nbands
        v = which === :married ? sim.band_m_mean[bi] : sim.band_c_mean[bi]
        acc += v[yi == :end ? end : yi]
    end
    return acc / nbands
end

# -----------------------------------------------------------------------------
# Entry point: single confirmation run.
#   julia --project=. cri_skeleton_abm.jl [w] [nseeds]
# The EXPENSIVE calibration + N3 grid lives in calibrate.jl (not triggered here).
# -----------------------------------------------------------------------------
if abspath(PROGRAM_FILE) == @__FILE__
    w  = length(ARGS) >= 1 ? parse(Float64, ARGS[1]) : 0.6
    ns = length(ARGS) >= 2 ? parse(Int, ARGS[2])     : 16
    main(; w = w, nseeds = ns)
end
