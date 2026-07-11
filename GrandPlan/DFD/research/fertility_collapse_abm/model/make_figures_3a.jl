# =============================================================================
# make_figures_3a.jl
# Stage 3a FIGURE-DATA EMITTER — no-reflexivity sufficiency run (DFD)
# =============================================================================
#
# PURPOSE
#   Assemble tidy figure-data CSVs from the Stage 3a calibration outputs (and
#   the Stage 2b APC cohort effects, for the cohort-gradient fit check). Performs
#   NO estimation and NO simulation of its own — reads artifacts only.
#   PNG rendering is done by _render_figures_3a.py (matplotlib Agg, headless),
#   which reads ONLY the figdata CSVs written here.
#
# INPUTS (read-only)
#   outputs/stage3a/{CC}_composition_bands.csv     fig 1 (sim-vs-obs by band)
#   outputs/stage3a/{CC}_cohort_multiplier.csv     fig 2 (kappa(b), phi(b))
#   outputs/stage2b/apc_cohort_effects_{CC}_married.csv   fig 2 (2b empirical gradient)
#   outputs/stage3a/{CC}_period_multiplier.csv     fig 3 (pi(t))
#   outputs/stage3a/{CC}_tfr_overlay.csv           fig 4 (overlay ONLY — see wall note)
#
# OUTPUTS (outputs/stage3a/figdata/)
#   fig1_bands_{CC}.csv    fig2_cohort_{CC}.csv    fig3_period.csv    fig4_tfr_{CC}.csv
#
# IDENTIFICATION WALL
#   fig4 is the ONLY figure touching a TFR series, strictly as the comparison
#   overlay (placeholder-ASFR level; 3a makes no TFR claim). Nothing here feeds
#   back into calibration.
#
# INVOCATION
#   julia --project=. make_figures_3a.jl
#
# DOCUMENTED TO: PROTO-RAG-001 code standards.
# Build instruction: STAGE3a_sufficiency_instruction.md (Debb, 2026-07-11).
# Author: Claude Code (Stage 3a sufficiency), DFD Core Team — 2026-07-11
# =============================================================================

using CSV
using DataFrames

const MODEL_DIR = @__DIR__
const S3A     = joinpath(MODEL_DIR, "outputs", "stage3a")
const S2B     = joinpath(MODEL_DIR, "outputs", "stage2b")
const FIGDATA = joinpath(S3A, "figdata")

const CODES = ("CRI", "COL")

mkpath(FIGDATA)

for cc in CODES
    # ---- fig 1: per-band sim-vs-obs composition trajectories (pass-through) ----
    bands = CSV.read(joinpath(S3A, "$(cc)_composition_bands.csv"), DataFrame)
    CSV.write(joinpath(FIGDATA, "fig1_bands_$(cc).csv"), bands)

    # ---- fig 2: calibrated kappa(b) against the 2b APC cohort effects ----
    kap = CSV.read(joinpath(S3A, "$(cc)_cohort_multiplier.csv"), DataFrame)
    apc = CSV.read(joinpath(S2B, "apc_cohort_effects_$(cc)_married.csv"), DataFrame)
    # APC bins are 5-yr birth-cohort starts; evaluate kappa at the bin midpoint.
    kmap = Dict(r.birth_year => r.kappa for r in eachrow(kap))
    apc.kappa_at_bin_mid = [get(kmap, c + 2, missing) for c in apc.cohort_start]
    CSV.write(joinpath(FIGDATA, "fig2_cohort_$(cc).csv"),
              select(apc, :cohort_start, :effect, :kappa_at_bin_mid))
    # full kappa/phi profile alongside (long form, for the line trace)
    CSV.write(joinpath(FIGDATA, "fig2_cohort_profile_$(cc).csv"), kap)

    # ---- fig 4: TFR overlay (comparison only; caveated in the renderer) ----
    tfr = CSV.read(joinpath(S3A, "$(cc)_tfr_overlay.csv"), DataFrame)
    CSV.write(joinpath(FIGDATA, "fig4_tfr_$(cc).csv"), tfr)
end

# ---- fig 3: exogenous period multiplier pi(t), both countries in one file ----
per = vcat([let d = CSV.read(joinpath(S3A, "$(cc)_period_multiplier.csv"), DataFrame)
                d.country .= cc; d
            end for cc in CODES]...)
CSV.write(joinpath(FIGDATA, "fig3_period.csv"), per)

println("figdata written to: ", FIGDATA)
