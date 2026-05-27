################################################################################
# assemble_comparison.jl  — combine the per-run CSVs into the seminar table.
#
# Reads results/{baseline,kappa30,taum20}_results.csv (field,value format
# written by write_single), emits results/stationary_comparison.csv, prints the
# three-column seminar table, and evaluates the §5 sanity gates. The baseline
# column here is the run_kappa.jl baseline (which the gate confirmed reproduces
# aging RUN 1); aging RUN 1 welfare cells are also printed for cross-check.
################################################################################

using Printf

const RESULTS_DIR = joinpath(@__DIR__, "results")

# Parse a field,value CSV into a Dict (label kept as String, rest as Float64).
function load_run(name::String)
    d = Dict{String,Any}()
    for (i, line) in enumerate(eachline(joinpath(RESULTS_DIR, name)))
        i == 1 && continue                       # header
        k, v = split(line, ',', limit = 2)
        d[k] = k == "label" ? v : parse(Float64, v)
    end
    return d
end

base = load_run("baseline_results.csv")
kap  = load_run("kappa30_results.csv")
tau  = load_run("taum20_results.csv")

# Aging RUN 1 welfare cells (cross-check only) — from aging_comparison_gap.csv.
const AGING = (W_MθL = 3.482, W_MθH = 4.143, W_FθL = 3.321, W_FθH = 3.965)

# ── Comparison CSV ───────────────────────────────────────────────────────────
const COLS = ["K","L","Y","r_annual","w","τp","pen","B","B_over_Y",
              "C_over_Y","M_over_Y","N_W","N_R","depratio",
              "W_MθL","W_MθH","W_FθL","W_FθH","DIFF","euler_max"]

open(joinpath(RESULTS_DIR, "stationary_comparison.csv"), "w") do io
    println(io, "label,K,L,Y,r_annual_pct,w,taup,pen,B,B_over_Y," *
                "C_over_Y,M_over_Y,N_W,N_R,depratio," *
                "W_MθL,W_MθH,W_FθL,W_FθH,DIFF_over_Y,euler_max_log10")
    for r in (base, kap, tau)
        @printf(io, "%s", r["label"])
        for c in COLS
            @printf(io, ",%g", r[c])
        end
        println(io)
    end
end
println("Wrote results/stationary_comparison.csv")

# ── Seminar table ────────────────────────────────────────────────────────────
println("\n" * "="^70)
println("  SEMINAR TABLE — Stationary policy experiments, Mexico baseline")
println("="^70)
@printf "  %-24s  %12s  %12s  %12s\n" "" "Baseline" "κ=0.30" "τm=−0.20"
function row(name, k, fmt)
    print(@sprintf("  %-24s  ", name))
    f = Printf.Format(fmt)
    for r in (base, kap, tau); print(Printf.format(f, r[k])); end
    println()
end
function pct(name, k)
    print(@sprintf("  %-24s  ", name))
    for r in (base, kap, tau); print(@sprintf("%11.2f%%", 100*r[k])); end
    println()
end
row("K (capital)",  "K", "%12.3f")
row("Y (output)",   "Y", "%12.3f")
row("r (annual, %)","r_annual", "%11.2f%%")
row("w (wage)",     "w", "%12.3f")
pct("τp", "τp")
row("pen",          "pen", "%12.3f")
pct("B/Y", "B_over_Y")
pct("C/Y", "C_over_Y")
pct("M/Y", "M_over_Y")

println("\n  Welfare at birth W₁(g,θ):")
row("  M, θL", "W_MθL", "%12.4f"); row("  M, θH", "W_MθH", "%12.4f")
row("  F, θL", "W_FθL", "%12.4f"); row("  F, θH", "W_FθH", "%12.4f")
@printf "  (aging RUN 1 cross-check: M,θL=%.3f M,θH=%.3f F,θL=%.3f F,θH=%.3f)\n" AGING.W_MθL AGING.W_MθH AGING.W_FθL AGING.W_FθH

# ── §5 sanity gates ──────────────────────────────────────────────────────────
g(ok) = ok ? "PASS" : "⚠ FAIL"
sgap(r) = max(abs(r["W_MθL"]-r["W_FθL"]), abs(r["W_MθH"]-r["W_FθH"]))
println("\n  Sanity gates (§5):")
@printf "    [1] DIFF/Y < 1e-3      : base %+.1e %s | κ %+.1e %s | τm %+.1e %s\n" base["DIFF"] g(abs(base["DIFF"])<1e-3) kap["DIFF"] g(abs(kap["DIFF"])<1e-3) tau["DIFF"] g(abs(tau["DIFF"])<1e-3)
@printf "    [2] Euler log10 < -3   : base %.2f %s | κ %.2f %s | τm %.2f %s\n" base["euler_max"] g(base["euler_max"]<-3) kap["euler_max"] g(kap["euler_max"]<-3) tau["euler_max"] g(tau["euler_max"]<-3)
@printf "    [4] κ=0.30 → τp falls  : %.2f%% → %.2f%% %s\n" 100*base["τp"] 100*kap["τp"] g(kap["τp"] < base["τp"]-0.01)
@printf "    [5] τm=−0.20 → M/Y rises: %.3f%% → %.3f%% %s\n" 100*base["M_over_Y"] 100*tau["M_over_Y"] g(tau["M_over_Y"] > base["M_over_Y"])
@printf "    [6] symmetric |M-F|<1e-6: base %.1e %s | κ %.1e %s | τm %.1e %s\n" sgap(base) g(sgap(base)<1e-6) sgap(kap) g(sgap(kap)<1e-6) sgap(tau) g(sgap(tau)<1e-6)

allok = abs(base["DIFF"])<1e-3 && abs(kap["DIFF"])<1e-3 && abs(tau["DIFF"])<1e-3 &&
        base["euler_max"]<-3 && kap["euler_max"]<-3 && tau["euler_max"]<-3 &&
        kap["τp"] < base["τp"]-0.01 && tau["M_over_Y"] > base["M_over_Y"] &&
        sgap(base)<1e-6 && sgap(kap)<1e-6 && sgap(tau)<1e-6
println("\n", allok ? "✔ ALL GATES PASSED" : "⚠ ONE OR MORE GATES FAILED — inspect above")
