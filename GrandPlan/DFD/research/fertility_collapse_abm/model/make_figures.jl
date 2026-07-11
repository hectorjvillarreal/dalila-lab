# =============================================================================
# make_figures.jl
# Stage 2 FIGURE-DATA builder — Rapid Fertility Collapse ABM (DFD)
# =============================================================================
#
# PURPOSE
#   Consolidate the calibration/confirmation outputs into tidy, plot-ready CSVs.
#   NO plotting package is in the pinned environment (Agents v6 + Distributions
#   =0.25.116; adding a plotting dep is NOT allowed per the Stage 2 instruction).
#   So this script writes figure-DATA CSVs in long/tidy form; the operator plots
#   them with whatever they prefer (matplotlib, gnuplot, Plots.jl in a separate
#   env). Each output below maps 1:1 to a required figure.
#
#   If UnicodePlots happens to be available (it is NOT a declared dep), a terminal
#   sparkline is printed as a convenience; absence is handled silently.
#
# REQUIRED FIGURES (instruction deliverable 3) and their data files:
#   (1) generated vs observed TFR ............ fig_tfr_w{NN}.csv
#   (2) generated vs observed married/cohab .. fig_bands_w{NN}.csv
#   (3) falsification comparison ............. fig_falsification_w{NN}.csv
#   (4) the w-locus 2x2 grid ................. fig_locus_grid.csv
#
# INVOCATION
#   JULIA_NUM_THREADS=1 julia --project=. make_figures.jl
#   # reads model/outputs/*.csv produced by calibrate.jl (or cri_skeleton_abm.jl)
#
# Author: Claude Code (Stage 2 calibration), DFD Core Team
# Date: 2026-06-19
# =============================================================================

using CSV
using DataFrames
using Printf

const MODEL_DIR = @__DIR__
const OUT_DIR   = joinpath(MODEL_DIR, "outputs")
const WS        = (40, 60, 80)   # w*100 suffixes

wfile(stem, ww) = joinpath(OUT_DIR, @sprintf("%s_w%02d.csv", stem, ww))
exists(p) = isfile(p)

# -----------------------------------------------------------------------------
# (1) TFR: generated (norm ON), falsification (norm OFF), observed — long form.
# (3) Falsification is the same file (norm ON vs OFF columns), also split out.
# -----------------------------------------------------------------------------
function build_tfr_figs()
    for ww in WS
        src = wfile("tfr_path", ww)
        exists(src) || (@printf("  [skip] %s not found\n", src); continue)
        df = CSV.read(src, DataFrame)
        # tidy long: one row per (year, series)
        long = DataFrame(year = Int[], series = String[], value = Union{Float64,Missing}[],
                         sd = Union{Float64,Missing}[])
        for r in eachrow(df)
            push!(long, (r.year, "generated_norm_on", r.tfr_generated_mean, r.tfr_generated_sd))
            push!(long, (r.year, "generated_norm_off", get(r, :tfr_falsification_mean, missing), missing))
            push!(long, (r.year, "observed", get(r, :tfr_observed, missing), missing))
        end
        CSV.write(wfile("fig_tfr", ww), long)
        # falsification-only convenience file (criterion 4)
        fdf = select(df, :year, :tfr_generated_mean => :norm_on,
                     :tfr_falsification_mean => :norm_off)
        CSV.write(wfile("fig_falsification", ww), fdf)
        @printf("  [ok] fig_tfr_w%02d.csv, fig_falsification_w%02d.csv\n", ww, ww)
        try_sparkline("TFR gen ON w=$(ww/100)", skipmissing_vec(df.tfr_generated_mean))
    end
end

# -----------------------------------------------------------------------------
# (2) Married/cohab trajectory: sim vs observed, per band, long form.
# -----------------------------------------------------------------------------
function build_band_figs()
    for ww in WS
        src = wfile("composition_bands", ww)
        exists(src) || (@printf("  [skip] %s not found\n", src); continue)
        df = CSV.read(src, DataFrame)
        long = DataFrame(year = Int[], age_band = String[], margin = String[],
                         series = String[], value = Union{Float64,Missing}[],
                         sd = Union{Float64,Missing}[])
        for r in eachrow(df)
            push!(long, (r.year, r.age_band, "married", "sim", r.married_sim, r.married_sim_sd))
            push!(long, (r.year, r.age_band, "married", "obs", r.married_obs, missing))
            push!(long, (r.year, r.age_band, "cohab", "sim", r.cohab_sim, r.cohab_sim_sd))
            push!(long, (r.year, r.age_band, "cohab", "obs", r.cohab_obs, missing))
        end
        CSV.write(wfile("fig_bands", ww), long)
        @printf("  [ok] fig_bands_w%02d.csv\n", ww)
    end
end

# -----------------------------------------------------------------------------
# (4) w-locus 2x2 grid: stack the per-w locus_grid files into one tidy CSV.
# -----------------------------------------------------------------------------
function build_locus_fig()
    frames = DataFrame[]
    for ww in WS
        src = wfile("locus_grid", ww)
        exists(src) || continue
        d = CSV.read(src, DataFrame)
        d.w .= ww / 100
        push!(frames, d)
    end
    if isempty(frames)
        println("  [skip] no locus_grid_w*.csv found (run calibrate.jl first)")
        return
    end
    all = vcat(frames...)
    CSV.write(joinpath(OUT_DIR, "fig_locus_grid.csv"), all)
    println("  [ok] fig_locus_grid.csv")
    # quick verdict table: which cell, removed, kills the collapse, per w
    println("\n  --- w-locus collapse summary (pct TFR change per cell) ---")
    @printf("  %-5s  %-12s %-12s %-12s %-12s\n", "w", "A_on_B_off", "A_on_B_on", "A_off_B_off", "A_off_B_on")
    for ww in WS
        sub = all[all.w .== ww/100, :]
        isempty(sub) && continue
        getp(c) = (i = findfirst(==(c), sub.cell); i === nothing ? NaN : sub.pct_change[i])
        @printf("  %-5.2f  %-12.0f %-12.0f %-12.0f %-12.0f\n", ww/100,
                getp("A_on_B_off"), getp("A_on_B_on"), getp("A_off_B_off"), getp("A_off_B_on"))
    end
end

# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------
skipmissing_vec(v) = collect(skipmissing(v))

function try_sparkline(label, vals)
    isempty(vals) && return
    try
        @eval import UnicodePlots
        plt = UnicodePlots.lineplot(1:length(vals), Float64.(vals); title = label,
                                    width = 50, height = 6)
        show(plt); println()
    catch
        # UnicodePlots not available — silent; the CSV is the deliverable.
    end
end

function main_figs()
    isdir(OUT_DIR) || (println("No outputs/ dir; run calibrate.jl or cri_skeleton_abm.jl first."); return)
    println("=== Building figure-data CSVs from ", OUT_DIR, " ===")
    println("(no plotting dep in the pinned env; emitting tidy CSVs for the operator to plot)")
    build_tfr_figs()
    build_band_figs()
    build_locus_fig()
    println("\nFigure-data CSVs written to: ", OUT_DIR)
    println("Plot recipe (operator): fig_tfr_w*.csv (TFR gen vs obs vs falsif),")
    println("  fig_bands_w*.csv (married/cohab sim vs obs by band),")
    println("  fig_falsification_w*.csv (norm ON vs OFF), fig_locus_grid.csv (2x2 grid).")
end

if abspath(PROGRAM_FILE) == @__FILE__
    main_figs()
end
