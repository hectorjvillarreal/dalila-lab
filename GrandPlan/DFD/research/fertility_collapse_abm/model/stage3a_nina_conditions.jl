# =============================================================================
# stage3a_nina_conditions.jl
# Stage 3a — Nina gate conditions 2 & 3: kappa-phi separability + cohort-only
# headline artifacts (DFD)
# =============================================================================
#
# PURPOSE (per STAGE3a_Nina_signoff.md, conditions 2 and 3)
#   Condition 3: the COHORT-ONLY model (period shifter pinned to zero; params
#     from the _noperiod ablation calibration) becomes the HEADLINE
#     specification. This script renders its headline artifacts — final
#     confirmation ensembles (50k x 16) at the already-calibrated
#     calibration_best_{CC}_noperiod.csv params. NO recalibration happens here.
#   Condition 2: kappa-phi separability — show the two cohort terms are pinned
#     by DIFFERENT data moments. Structural claim: kappa(b) multiplies the two
#     marriage-ENTRY margins (formation split married-vs-cohab; cohab->married
#     conversion), both of which leave union status unchanged -> kappa is
#     union-total-neutral by construction (up to the second-order differential-
#     dissolution channel). phi(b) multiplies form_base -> it moves the union
#     total directly. The numeric check perturbs each at the headline params
#     (paired seeds, same seed0) and reports the 2024 responses of the two
#     moments: eq-band married share vs eq-band union-total share.
#
# OUTPUTS (model/outputs/stage3a/)
#   {CC}_composition_bands_noperiod.csv   headline per-band sim-vs-obs (mean±sd)
#   {CC}_composition_path_noperiod.csv    headline national shares
#   {CC}_cohort_multiplier_noperiod.csv   headline kappa(b), phi(b) profiles
#   {CC}_tfr_overlay_noperiod.csv         overlay [COMPARISON ONLY, caveats carry]
#   kphi_separability.csv                 condition-2 moment-sensitivity table
#
# INVOCATION
#   JULIA_NUM_THREADS=8 julia --project=. stage3a_nina_conditions.jl
#
# IDENTIFICATION NOTE: no loss is evaluated and no parameter is tuned anywhere
# in this script; the TFR overlay is written last, comparison-only, as ever.
#
# DOCUMENTED TO: PROTO-RAG-001. Build instruction: STAGE3a_sufficiency_instruction.md;
# adjudication: STAGE3a_Nina_signoff.md (conditions 2-3).
# Author: Claude Code (Stage 3a sufficiency), DFD Core Team — 2026-07-11
# =============================================================================

include("stage3a_norefl_abm.jl")

using Printf

const FINAL_AGENTS = 50_000
const FINAL_SEEDS  = 16
const SENS_AGENTS  = 20_000
const SENS_SEEDS   = 8
const SENS_SEED0   = 4000          # common across baseline & perturbed (paired)

# Perturbation sizes (condition 2). kappa side: the floor (latest-cohort level);
# phi side: the tilt. Both displacements are large enough that the paired-seed
# response dwarfs MC noise at 20k x 8.
const DKAPPA = 0.10
const DTILT  = 0.005

# -----------------------------------------------------------------------------
function load_noperiod_best(cfg::CountryConfig)
    f = joinpath(OUT_DIR, "calibration_best_$(cfg.code)_noperiod.csv")
    isfile(f) || error("missing $(f) — run CAL3A_PIN=period calibrate_3a.jl first")
    df = CSV.read(f, DataFrame)
    d = Dict(Symbol(r.param) => r.value for r in eachrow(df) if !startswith(String(r.param), "final_"))
    @assert d[:period_depth] == 0.0 "noperiod best should carry the pin (period_depth = 0)"
    return NamedTuple(d)
end

# 2024 (final-year) equal-band moments from an ensemble result.
function final_moments(sim)
    nb = length(CALIB_BANDS)
    m = mean(sim.band_m_mean[bi][end] for bi in 1:nb)
    c = mean(sim.band_c_mean[bi][end] for bi in 1:nb)
    return (married = m, union_total = m + c)
end

# Tagged writers (headline spec artifacts; baseline full-model files untouched).
function write_bands_csv_tagged(cfg, base, obs, tag)
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
    CSV.write(joinpath(OUT_DIR, "$(cfg.code)_composition_bands$(tag).csv"), rows)
end

function main_conditions()
    mkpath(OUT_DIR)
    @printf("\n=== STAGE 3a — Nina conditions 2 & 3 (threads=%d) ===\n", Threads.nthreads())
    sens_rows = NamedTuple[]

    for code in ("CRI", "COL")
        cfg = COUNTRIES[code]
        best = load_noperiod_best(cfg)
        seedcomp = load_seed_composition(cfg)
        obs_band = load_observed_composition_bands(cfg)

        # ---- condition 3: headline (cohort-only) final confirmation ----
        @printf("\n[%s] headline cohort-only final (%d x %d) ...\n", code, FINAL_AGENTS, FINAL_SEEDS)
        base = run_ensemble(cfg; nseeds = FINAL_SEEDS, n_agents = FINAL_AGENTS,
                              seedcomp = seedcomp, params_override = best, seed0 = 1000)
        write_bands_csv_tagged(cfg, base, obs_band, "_noperiod")
        df = DataFrame(year = base.years, single = base.single,
                       cohabiting = base.cohab, married = base.married)
        CSV.write(joinpath(OUT_DIR, "$(cfg.code)_composition_path_noperiod.csv"), df)
        p = Params(; year = cfg.year_start); apply_params!(p, best)
        bs = (cfg.year_start - AGE_MAX):(cfg.year_end - AGE_MIN)
        CSV.write(joinpath(OUT_DIR, "$(cfg.code)_cohort_multiplier_noperiod.csv"),
                  DataFrame(birth_year = collect(bs),
                            kappa = [kappa_cohort(p, b) for b in bs],
                            phi = [phi_cohort(p, b) for b in bs]))

        # ---- condition 2: kappa-phi moment sensitivity (paired seeds) ----
        @printf("[%s] kappa-phi separability (%d x %d, paired seed0=%d) ...\n",
                code, SENS_AGENTS, SENS_SEEDS, SENS_SEED0)
        runs = Dict{String,Any}()
        variants = (
            ("baseline",     best),
            ("kappa_floor+", merge(best, (kappa_floor = min(1.0, best.kappa_floor + DKAPPA),))),
            ("kappa_floor-", merge(best, (kappa_floor = max(0.01, best.kappa_floor - DKAPPA),))),
            ("form_tilt+",   merge(best, (form_tilt = best.form_tilt + DTILT,))),
            ("form_tilt-",   merge(best, (form_tilt = best.form_tilt - DTILT,))),
        )
        for (label, nt) in variants
            sim = run_ensemble(cfg; nseeds = SENS_SEEDS, n_agents = SENS_AGENTS,
                                 seedcomp = seedcomp, params_override = nt, seed0 = SENS_SEED0)
            runs[label] = final_moments(sim)
        end
        b = runs["baseline"]
        for (side, hi, lo, dsize) in (("kappa", "kappa_floor+", "kappa_floor-", DKAPPA),
                                      ("phi",   "form_tilt+",   "form_tilt-",   DTILT))
            dm = (runs[hi].married - runs[lo].married) / 2
            du = (runs[hi].union_total - runs[lo].union_total) / 2
            push!(sens_rows, (country = code, term = side, perturbation = dsize,
                              d_married_2024 = dm, d_union_total_2024 = du,
                              ratio_married_over_union = abs(dm) / max(abs(du), 1e-9),
                              baseline_married = b.married, baseline_union = b.union_total))
            @printf("  %-6s ±%.3f: Δmarried=%+.4f  Δunion_total=%+.4f  |ratio|=%.1f\n",
                    side, dsize, dm, du, abs(dm) / max(abs(du), 1e-9))
        end

        # ---- overlay LAST (comparison only; tagged — baseline overlay untouched) ----
        obs_tfr = load_observed_tfr(cfg)
        dft = DataFrame(year = base.years,
                        tfr_overlay_mean = base.tfr_m, tfr_overlay_sd = base.tfr_s)
        dft.tfr_observed = [ (oi = findfirst(==(y), obs_tfr.year);
                              oi === nothing ? missing : obs_tfr.tfr[oi]) for y in dft.year ]
        CSV.write(joinpath(OUT_DIR, "$(cfg.code)_tfr_overlay_noperiod.csv"), dft)
    end

    CSV.write(joinpath(OUT_DIR, "kphi_separability.csv"), DataFrame(sens_rows))
    println("\nCondition 2-3 artifacts written to: ", OUT_DIR)
end

main_conditions()
