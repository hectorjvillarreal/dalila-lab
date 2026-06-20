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
# INPUTS  (read-only; NEVER written by this script)
#   data/coupling/CRI_coupling_annual.csv
#       Process A CALIBRATION TARGET. Observed annual union composition of women
#       20-39 in Costa Rica, by 5-yr band, married vs cohabiting (2010-2024).
#       This is the ONLY series Process A is calibrated to.
#   data/national/CRI_tfr_national.csv
#       OUTPUT COMPARISON ONLY (1.83 -> 1.12). Loaded solely to score the model's
#       GENERATED TFR against observation. NEVER a calibration target. (Identification
#       discipline, non-negotiable, from Stage 1.)
#
#   Agent background distributions (education low/med/high x location urban/rural):
#       PROVISIONAL plausible Costa Rica values — see BACKGROUND_* constants below
#       and the [PROVISIONAL] flags. Flagged for Anne to pin to CR census / WB.
#
# OUTPUTS  (written under model/outputs/ — created if absent)
#   tfr_path_w{W}.csv        generated annual TFR path, ensemble mean +/- sd
#   composition_path_w{W}.csv simulated single/cohabiting/married national shares
#   (printed) first-look generated-vs-observed TFR comparison
#   The falsification run is invoked by setting `social_norm_on = false`.
#
# ASSUMPTIONS  (all PROVISIONAL below the frozen invariants; the skeleton is
#   expected to teach us where these are wrong — surfacing that is a SUCCESS):
#   - Closed cohort-aging population: a fixed number of women, each ageing one
#     year per tick; women turning 50 are replaced by a new 15-year-old single
#     nullipara drawn from the same background distribution (stationary inflow).
#     This is a skeleton simplification, NOT a demographic projection.
#   - Background (education, location) is FIXED at birth and NOT tuned to TFR.
#   - Process A drift + social-norm threshold are calibrated ONLY to the CRI
#     coupling composition series.
#   - Process B birth intensities (married baseline ASFR shape) come from an
#     external age-fertility schedule (MEX ENADID shape as a regional prior),
#     scaled by union status and `w`. The LEVEL is NOT fitted to CR TFR.
#   - One tick = one year; 2010..2024 (15 years).
#
# DEPENDENCIES
#   Julia 1.11.7; Agents.jl, CSV.jl, DataFrames.jl, Random, Statistics, Printf.
#   CPU-parallel ONLY: the ENSEMBLE over seeds is parallelised with Threads;
#   the agent step itself is serial per the Dalila compute envelope (GPU is
#   reserved for the later nesting-phase sweep, NOT this skeleton).
#
# DOCUMENTED TO: PROTO-RAG-001 code standards (Purpose/Inputs/Outputs/
#   Assumptions/Dependencies header). endorsed_by: blank pending Anne.
#
# Author: Claude Code (Stage 2 skeleton execution), DFD Core Team
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
const MODEL_DIR   = @__DIR__
const DATA_DIR    = normpath(joinpath(MODEL_DIR, "..", "data"))
const COUPLING_CSV = joinpath(DATA_DIR, "coupling", "CRI_coupling_annual.csv")
const TFR_CSV      = joinpath(DATA_DIR, "national", "CRI_tfr_national.csv")
const OUT_DIR      = joinpath(MODEL_DIR, "outputs")

# -----------------------------------------------------------------------------
# Background distributions  [PROVISIONAL — flagged for Anne to pin to CR data]
# -----------------------------------------------------------------------------
# Education shares (women of reproductive age, Costa Rica, approximate).
# [PROVISIONAL] Plausible values; CR has high secondary completion and rising
# tertiary. Replace with CR Censo 2022 / WB EdStats. Held as structural context,
# NOT tuned to TFR.
const EDU_LEVELS = (:low, :med, :high)
const EDU_SHARES = (0.35, 0.40, 0.25)          # [PROVISIONAL]

# Location shares: Costa Rica is ~80% urban (WB ~81% 2020). [PROVISIONAL] level.
const LOC_LEVELS = (:urban, :rural)
const LOC_SHARES = (0.80, 0.20)                # [PROVISIONAL]

# -----------------------------------------------------------------------------
# Age / fertility schedule  [PROVISIONAL regional prior — NOT fitted to CR TFR]
# -----------------------------------------------------------------------------
# MARRIED-union per-woman annual birth probability by single year of age, a
# regional age-fertility SHAPE prior (MEX ENADID-like, late-20s peak). The LEVEL
# here sets married-union fertility intensity; it is a structural primitive, not
# tuned to reproduce CR TFR. Single-age probabilities, married full intensity.
# [PROVISIONAL] — Anne to replace with a CR-specific married-ASFR schedule.
const AGE_MIN = 15
const AGE_MAX = 49

# Gaussian-ish bump centred at 27, married-union annual birth hazard.
function married_birth_hazard(age::Int)
    # peak ~0.165/yr at 27; integrates over a union career to a completed
    # married fertility well above replacement (as observed pre-collapse).
    μ = 27.0; σ = 6.5; peak = 0.165
    h = peak * exp(-0.5 * ((age - μ) / σ)^2)
    return clamp(h, 0.0, 0.6)
end

# Single-woman baseline birth hazard: low but non-zero (out-of-union births).
# [PROVISIONAL] small fraction of the married hazard.
single_birth_hazard(age::Int) = 0.10 * married_birth_hazard(age)

# -----------------------------------------------------------------------------
# Agent
# -----------------------------------------------------------------------------
# Union status encoded as a Symbol in {:single, :cohabiting, :married}
# (INVARIANT 1: composition, never just partnered/not).
@agent struct Woman(NoSpaceAgent)
    age::Int
    edu::Symbol           # :low :med :high   (fixed background)
    loc::Symbol           # :urban :rural     (fixed background)
    union::Symbol         # :single :cohabiting :married  (dynamic; the composition state)
    parity::Int           # number of children (dynamic; from the start)
end

ispartnered(a::Woman) = a.union !== :single

# -----------------------------------------------------------------------------
# Model parameters
# -----------------------------------------------------------------------------
# All transition primitives live in `abmproperties(model)`. Process A is calibrated
# to the CRI composition series; Process B carries the `w` weight and the
# (provisional) map-side nonlinearity.
Base.@kwdef mutable struct Params
    # ----- structural -----
    w::Float64 = 0.6                  # INVARIANT 2: cohabiting/married fertility ratio
    year::Int = 2010
    # ----- Process A: partnership formation/dissolution (COUPLING-side site) -----
    # Baseline single-year hazards (calibrated to CR composition series).
    form_base::Float64 = 0.16         # base prob a single woman forms ANY union / yr
    marry_share_of_form::Float64 = 0.45  # of formed unions, share that are marriages (declines over time)
    dissolve_cohab::Float64 = 0.06    # cohabiting -> single annual hazard
    dissolve_marr::Float64 = 0.015    # married -> single annual hazard
    cohab_to_marr::Float64 = 0.05     # cohabiting -> married annual hazard (declines over time)
    # social-norm / reference-group term (the THRESHOLD at site A):
    social_norm_on::Bool = true       # falsification switch (criterion 4)
    norm_strength::Float64 = 0.55     # how strongly ref-group partnered-share moves formation
    norm_threshold::Float64 = 0.42    # reference-group partnered-share threshold
    norm_steepness::Float64 = 14.0    # logistic steepness of the threshold
    # secular drift in the marriage margin (the observed marriage collapse):
    marriage_drift::Float64 = 0.020   # per-yr decline in marriage propensity (CR marriage collapse)
    # ----- Process B: coupling -> fertility map (MAP-side site) -----
    map_nonlinearity_on::Bool = false # provisional map-side threshold (OFF by default; site B candidate)
    map_threshold::Float64 = 0.45     # fertility-weighted-union share threshold (map-side)
    map_steepness::Float64 = 10.0
    map_depth::Float64 = 0.0          # extra fertility suppression below threshold (0 => no map nonlinearity)
    # ----- bookkeeping -----
    n_agents::Int = 20_000
    # ----- per-run scratch accumulators (mutated each tick; not parameters) -----
    births_this_year::Int = 0
    exposure_this_year::Int = 0
    fw_union_share::Float64 = 0.0
    refshares::Vector{Float64} = Float64[]
end

# -----------------------------------------------------------------------------
# Reference-group partnered share (the social-norm term feeding Process A)
# -----------------------------------------------------------------------------
# Minimal reference group: same-age-band agents. (Education/location homophily
# is a provisional extension — flagged, not implemented in the skeleton.)
ageband(age::Int) = clamp((age - AGE_MIN) ÷ 5, 0, (AGE_MAX - AGE_MIN) ÷ 5)

function refgroup_partnered_shares(model)
    # returns Dict{band => partnered share}
    nb = (AGE_MAX - AGE_MIN) ÷ 5 + 1
    cnt = zeros(Int, nb); part = zeros(Int, nb)
    for a in allagents(model)
        b = ageband(a.age) + 1
        cnt[b] += 1
        part[b] += ispartnered(a) ? 1 : 0
    end
    shares = [cnt[b] == 0 ? 0.0 : part[b] / cnt[b] for b in 1:nb]
    return shares
end

# Logistic threshold response: below `threshold` the formation incentive drops
# sharply (the social-norm collapse). This is the COUPLING-side nonlinearity.
function norm_multiplier(p::Params, ref_share::Float64)
    p.social_norm_on || return 1.0          # FALSIFICATION: norm off => flat multiplier
    # multiplier in roughly (1 - norm_strength .. 1 + small); logistic in ref_share
    z = p.norm_steepness * (ref_share - p.norm_threshold)
    lo = 1.0 - p.norm_strength
    return lo + (1.0 - lo) * (1.0 / (1.0 + exp(-z)))
end

# Map-side (Process B) nonlinearity multiplier on fertility, keyed to the
# fertility-weighted-union share. OFF unless map_nonlinearity_on & map_depth>0.
function map_multiplier(p::Params, fw_union_share::Float64)
    (p.map_nonlinearity_on && p.map_depth > 0.0) || return 1.0
    z = p.map_steepness * (fw_union_share - p.map_threshold)
    suppression = p.map_depth * (1.0 - 1.0 / (1.0 + exp(-z)))  # large below threshold
    return clamp(1.0 - suppression, 0.0, 1.0)
end

# =============================================================================
# Model construction
# =============================================================================
function build_model(; w::Float64, seed::Int, n_agents::Int = 20_000,
                       social_norm_on::Bool = true,
                       map_nonlinearity_on::Bool = false, map_depth::Float64 = 0.0,
                       start_married::Float64 = 0.34, start_cohab::Float64 = 0.22)
    rng = Xoshiro(seed)
    p = Params(; w = w, n_agents = n_agents, social_norm_on = social_norm_on,
                 map_nonlinearity_on = map_nonlinearity_on, map_depth = map_depth)
    model = StandardABM(Woman; properties = p, rng = rng,
                        agent_step! = agent_step!, model_step! = model_step!)

    # ---- seed the initial population at the 2010 composition ----
    # Background drawn from provisional CR distributions; union status seeded so
    # that the 20-39 married/cohabiting shares match the 2010 observed values.
    for _ in 1:n_agents
        age = rand(abmrng(model), AGE_MIN:AGE_MAX)
        edu = sample_categorical(abmrng(model), EDU_LEVELS, EDU_SHARES)
        loc = sample_categorical(abmrng(model), LOC_LEVELS, LOC_SHARES)
        union = seed_union(abmrng(model), age, start_married, start_cohab)
        parity = seed_parity(abmrng(model), age, union)
        add_agent!(model, age, edu, loc, union, parity)
    end
    return model
end

function sample_categorical(rng, levels, shares)
    u = rand(rng); c = 0.0
    @inbounds for i in eachindex(levels)
        c += shares[i]
        u <= c && return levels[i]
    end
    return levels[end]
end

# Seed union status with age-graded partnered share rising with age (younger
# women less partnered), centred to hit the observed 20-39 composition.
function seed_union(rng, age, start_married, start_cohab)
    # age gradient: scale partnered propensity up with age
    g = clamp((age - 15) / 25, 0.0, 1.3)
    pm = start_married * g
    pc = start_cohab  * (0.6 + 0.4 * g)   # cohabitation flatter across age
    u = rand(rng)
    u < pm && return :married
    u < pm + pc && return :cohabiting
    return :single
end

# Seed parity roughly consistent with age & union (provisional, keeps the model
# from starting every woman at parity 0; not a calibration target).
function seed_parity(rng, age, union)
    base = union === :married ? 0.10 : union === :cohabiting ? 0.07 : 0.02
    expected = base * max(0, age - 18)
    return rand(rng) < (expected - floor(expected)) ? Int(ceil(expected)) : Int(floor(expected))
end

# =============================================================================
# Steps
# =============================================================================
# model_step!: advance the year, apply secular drift in the marriage margin,
# and recompute the reference-group partnered shares once per tick (so the
# agent step reads a consistent within-year snapshot).
function model_step!(model)
    p = abmproperties(model)
    p.year += 1
    # secular marriage-margin erosion (the observed CR marriage collapse), bounded:
    p.marry_share_of_form = max(0.05, p.marry_share_of_form - p.marriage_drift)
    p.cohab_to_marr       = max(0.005, p.cohab_to_marr - 0.15 * p.marriage_drift)
    # cache reference-group shares + the current fertility-weighted-union share
    abmproperties(model).refshares = refgroup_partnered_shares(model)
    abmproperties(model).fw_union_share = fertility_weighted_union_share(model)
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
    refshares = abmproperties(model).refshares
    ref = refshares[ageband(a.age) + 1]
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
    base_h = a.union === :married    ? married_birth_hazard(a.age) :
             a.union === :cohabiting ? p.w * married_birth_hazard(a.age) :
                                       single_birth_hazard(a.age)
    mm = map_multiplier(p, abmproperties(model).fw_union_share)   # MAP-side threshold (site B)
    birth_p = clamp(base_h * mm, 0.0, 0.9)
    if rand(rng) < birth_p
        a.parity += 1
        abmproperties(model).births_this_year += 1
    end

    # ---------- ageing + cohort replacement ----------
    a.age += 1
    if a.age > AGE_MAX
        a.age = AGE_MIN
        a.edu = sample_categorical(rng, EDU_LEVELS, EDU_SHARES)
        a.loc = sample_categorical(rng, LOC_LEVELS, LOC_SHARES)
        a.union = :single
        a.parity = 0
    end
    # count exposure (woman-years 15-49) for TFR denominator handled at year end
    abmproperties(model).exposure_this_year += 1
    return
end

# =============================================================================
# Running one ensemble member, collecting the annual TFR + composition paths
# =============================================================================
# We define TFR per tick as the sum over single-year ASFRs implied by that
# year's births. With cohort replacement keeping a stationary age structure,
# (annual births / women 15-49) * 35 (years of exposure) approximates a period
# TFR. This is a SKELETON TFR estimator; it is the model OUTPUT, never a target.
function run_path!(model; nyears::Int)
    years = Int[]; tfr = Float64[]
    f_single = Float64[]; f_cohab = Float64[]; f_marr = Float64[]
    # initialise per-year accumulators
    abmproperties(model).refshares = refgroup_partnered_shares(model)
    abmproperties(model).fw_union_share = fertility_weighted_union_share(model)
    for t in 1:nyears
        abmproperties(model).births_this_year = 0
        abmproperties(model).exposure_this_year = 0
        step!(model, 1)                      # one tick = one year
        # period-TFR proxy: (births / woman-years) * reproductive span
        gfr = abmproperties(model).exposure_this_year == 0 ? 0.0 :
              abmproperties(model).births_this_year / abmproperties(model).exposure_this_year
        push!(tfr, gfr * (AGE_MAX - AGE_MIN + 1))
        push!(years, abmproperties(model).year)
        s, c, m = composition_shares(model)
        push!(f_single, s); push!(f_cohab, c); push!(f_marr, m)
    end
    return (; years, tfr, f_single, f_cohab, f_marr)
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

# =============================================================================
# Ensemble driver (CPU-parallel over seeds via Threads)
# =============================================================================
function run_ensemble(; w::Float64, nseeds::Int = 8, nyears::Int = 14,
                        n_agents::Int = 20_000, social_norm_on::Bool = true,
                        map_nonlinearity_on::Bool = false, map_depth::Float64 = 0.0)
    results = Vector{Any}(undef, nseeds)
    Threads.@threads for i in 1:nseeds
        model = build_model(; w = w, seed = 1000 + i, n_agents = n_agents,
                              social_norm_on = social_norm_on,
                              map_nonlinearity_on = map_nonlinearity_on,
                              map_depth = map_depth)
        results[i] = run_path!(model; nyears = nyears)
    end
    # aggregate (mean +/- sd across seeds, by year)
    years = results[1].years
    M = length(years)
    function agg(field)
        A = hcat([getfield(r, field) for r in results]...)  # M x nseeds
        return (mean(A; dims = 2)[:], std(A; dims = 2)[:])
    end
    tfr_m, tfr_s = agg(:tfr)
    s_m, _ = agg(:f_single); c_m, _ = agg(:f_cohab); m_m, _ = agg(:f_marr)
    return (; years, tfr_m, tfr_s, single = s_m, cohab = c_m, married = m_m)
end

# =============================================================================
# Observed series (OUTPUT COMPARISON ONLY — never a calibration target)
# =============================================================================
function load_observed_tfr()
    df = CSV.read(TFR_CSV, DataFrame)
    return (year = df.year, tfr = df.value)
end

function load_observed_composition_2039()
    # Average married / cohabiting shares across bands 20-24..35-39 by year,
    # weighted by n_women_weighted. This is the Process A calibration reference.
    df = CSV.read(COUPLING_CSV, DataFrame)
    g = combine(groupby(df, :year)) do sub
        wt = sub.n_women_weighted
        (married = sum(sub.married .* wt) / sum(wt),
         cohab   = sum(sub.cohabiting .* wt) / sum(wt),
         total   = sum(sub.union_total .* wt) / sum(wt))
    end
    sort!(g, :year)
    return g
end

# =============================================================================
# Main: skeleton first-look run
# =============================================================================
function main(; w::Float64 = 0.6, nseeds::Int = 8)
    mkpath(OUT_DIR)
    @printf("\n=== CRI SKELETON ABM — w=%.2f, %d seeds, threads=%d ===\n",
            w, nseeds, Threads.nthreads())

    obs_tfr = load_observed_tfr()
    obs_comp = load_observed_composition_2039()
    nyears = length(obs_tfr.year) - 1   # 2010 is the seeded start; sim 2011..2024

    # ---- baseline run (social norm ON) ----
    @info "Running BASELINE ensemble (social_norm_on = true) ..."
    base = run_ensemble(; w = w, nseeds = nseeds, nyears = nyears)

    # ---- falsification run (social norm OFF) ----
    @info "Running FALSIFICATION ensemble (social_norm_on = false) ..."
    fals = run_ensemble(; w = w, nseeds = nseeds, nyears = nyears,
                          social_norm_on = false)

    # ---- write outputs ----
    base_years = vcat(obs_tfr.year[1], base.years)   # prepend 2010 start
    write_tfr_csv(w, base, fals, obs_tfr)
    write_composition_csv(w, base)

    # ---- first-look comparison ----
    @printf("\n--- GENERATED vs OBSERVED TFR (w=%.2f) ---\n", w)
    @printf("%-6s  %-10s  %-10s  %-10s\n", "year", "obs", "gen(norm)", "gen(falsif)")
    for (i, yr) in enumerate(base.years)
        oi = findfirst(==(yr), obs_tfr.year)
        ov = oi === nothing ? NaN : obs_tfr.tfr[oi]
        @printf("%-6d  %-10.3f  %-10.3f  %-10.3f\n",
                yr, ov, base.tfr_m[i], fals.tfr_m[i])
    end
    # endpoint summary
    o0 = obs_tfr.tfr[1]; o1 = obs_tfr.tfr[end]
    g0 = base.tfr_m[1];  g1 = base.tfr_m[end]
    f1 = fals.tfr_m[end]
    @printf("\nObserved   2010->2024: %.2f -> %.2f  (%.0f%%)\n",
            o0, o1, 100*(o1-o0)/o0)
    @printf("Generated  (norm ON)  : %.2f -> %.2f  (%.0f%%)\n",
            g0, g1, 100*(g1-g0)/g0)
    @printf("Generated  (norm OFF) : %.2f -> %.2f  (%.0f%%)  [falsification]\n",
            g0, f1, 100*(f1-g0)/g0)
    @printf("\nComposition (sim, final year)  single=%.2f cohab=%.2f married=%.2f\n",
            base.single[end], base.cohab[end], base.married[end])
    @printf("Composition (obs 20-39, 2024)  married=%.3f cohab=%.3f\n",
            obs_comp.married[end], obs_comp.cohab[end])
    println("\nOutputs written to: ", OUT_DIR)
    return (; base, fals, obs_tfr, obs_comp)
end

function write_tfr_csv(w, base, fals, obs_tfr)
    df = DataFrame(year = base.years,
                   tfr_generated_mean = base.tfr_m,
                   tfr_generated_sd = base.tfr_s,
                   tfr_falsification_mean = fals.tfr_m)
    # attach observed where available (comparison only)
    df.tfr_observed = [ (oi = findfirst(==(y), obs_tfr.year);
                          oi === nothing ? missing : obs_tfr.tfr[oi]) for y in df.year ]
    CSV.write(joinpath(OUT_DIR, @sprintf("tfr_path_w%02d.csv", round(Int,100w))), df)
end

function write_composition_csv(w, base)
    df = DataFrame(year = base.years, single = base.single,
                   cohabiting = base.cohab, married = base.married)
    CSV.write(joinpath(OUT_DIR, @sprintf("composition_path_w%02d.csv", round(Int,100w))), df)
end

# -----------------------------------------------------------------------------
# Entry point: `julia --project=. cri_skeleton_abm.jl [w] [nseeds]`
# -----------------------------------------------------------------------------
if abspath(PROGRAM_FILE) == @__FILE__
    w  = length(ARGS) >= 1 ? parse(Float64, ARGS[1]) : 0.6
    ns = length(ARGS) >= 2 ? parse(Int, ARGS[2])     : 8
    main(; w = w, nseeds = ns)
end
