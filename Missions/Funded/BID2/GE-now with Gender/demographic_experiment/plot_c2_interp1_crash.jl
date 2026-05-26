################################################################################
# plot_c2_interp1_crash.jl
#
# Visualize the C2 interp-1 instability (debt-absorbs pension deficit; no
# finite SS at 2050 demographics) alongside the clean RUN 1 baseline.
# Three figures, one of them combined as a 1×3 panel.
#
# Reads iter tables from the on-disk logs:
#   results/run_aging_c2_recovery.log     — C2 interp-1 crash
#   results/run_aging_ssvs_gap.log        — full driver (RUN 1 is first block)
#
# Writes: results/c2_interp1_crash_*.png
################################################################################

using Printf, Plots
gr()

const RESULTS_DIR = joinpath(@__DIR__, "results")
const C2_LOG    = joinpath(RESULTS_DIR, "run_aging_c2_recovery.log")
const FULL_LOG  = joinpath(RESULTS_DIR, "run_aging_ssvs_gap.log")

# ─── Parse iter tables from a log ────────────────────────────────────────────
# Iter lines look like:
#   "1      12.000   10.000   1.200    0.1634   1.0935   0.1450   -7.933228e-01"
# Columns: iter, K, L, K/L, r_5yr, w, τp, DIFF/Y
function parse_iter_block(path::String; block_start_marker::String, max_lines::Int = 60)
    out = (iter=Int[], K=Float64[], L=Float64[], r5=Float64[], w=Float64[], τp=Float64[], DIFF=Float64[])
    in_block = false
    seen_header = false
    open(path) do io
        for line in eachline(io)
            if occursin(block_start_marker, line)
                in_block = true
                seen_header = false
                continue
            end
            in_block || continue
            # The iter table starts after a "iter   K ..." header + a separator
            if occursin(r"^iter\s+K", line)
                seen_header = true
                continue
            end
            seen_header || continue
            m = match(r"^\s*(\d+)\s+([-+]?[\d.]+)\s+([-+]?[\d.]+)\s+([-+]?[\d.]+)\s+([-+]?[\d.]+)\s+([-+]?[\d.]+)\s+([-+]?[\d.]+)\s+([-+]?[\d.eE+\-]+)\s*$", line)
            if m === nothing
                # Hit non-iter line (e.g., CONVERGED, blank, next section) → end of block
                length(out.iter) > 0 && break
                continue
            end
            push!(out.iter, parse(Int,     m.captures[1]))
            push!(out.K,    parse(Float64, m.captures[2]))
            push!(out.L,    parse(Float64, m.captures[3]))
            push!(out.r5,   parse(Float64, m.captures[5]))
            push!(out.w,    parse(Float64, m.captures[6]))
            push!(out.τp,   parse(Float64, m.captures[7]))
            push!(out.DIFF, parse(Float64, m.captures[8]))
            length(out.iter) >= max_lines && break
        end
    end
    return out
end

# ─── Load both trajectories ──────────────────────────────────────────────────
println("Parsing logs …")
c2_crash = parse_iter_block(C2_LOG;   block_start_marker = "Solving GE")
run1     = parse_iter_block(FULL_LOG; block_start_marker = "RUN 1 · 2020 baseline")

@printf "  C2 interp-1 crash: %d iters parsed\n" length(c2_crash.iter)
@printf "  RUN 1 baseline:    %d iters parsed\n" length(run1.iter)

# Convert 5-year r to annual percent
r_annual_pct(r5)   = ((1.0 + r5)^(1/5) - 1) * 100
n_p_2050_5yr       = (1.0 - 0.004)^5 - 1.0       # ≈ -0.01984
n_p_2050_ann_pct   = ((1.0 + n_p_2050_5yr)^(1/5) - 1) * 100   # ≈ -0.40

# ─── Panel 1: K trajectory, log-y ────────────────────────────────────────────
p1 = plot(c2_crash.iter, c2_crash.K;
          yscale = :log10, lw = 2.5, marker = :circle, color = :firebrick,
          label  = "C2 interp 1 (debt absorbs)",
          xlabel = "GE iter", ylabel = "K (log scale)",
          title  = "Capital trajectory — interp 1 explodes at iter 9",
          legend = :topleft)
plot!(p1, run1.iter, run1.K;
      lw = 2, marker = :diamond, color = :steelblue,
      label = "RUN 1 (2020 baseline, converges)")
# Annotate the blowup
ix_max = argmax(c2_crash.K)
annotate!(p1, c2_crash.iter[ix_max], c2_crash.K[ix_max],
          text(@sprintf("K = %.0f", c2_crash.K[ix_max]), 9, :firebrick, :left, :bottom))

savefig(p1, joinpath(RESULTS_DIR, "c2_interp1_crash_K.png"))
println("Wrote c2_interp1_crash_K.png")

# ─── Panel 2: r annual with n_p line — THE MECHANISM PANEL ───────────────────
p2 = plot(c2_crash.iter, r_annual_pct.(c2_crash.r5);
          lw = 2.5, marker = :circle, color = :firebrick,
          label  = "r (annual, %), C2 interp 1",
          xlabel = "GE iter", ylabel = "annual rate, %",
          title  = "Mechanism: r drops below n_p at iter 8 → B diverges",
          legend = :bottomright)
hline!(p2, [n_p_2050_ann_pct];
       lw = 2, ls = :dash, color = :darkgreen,
       label = @sprintf("n_p 2050 annual = %.2f%%", n_p_2050_ann_pct))
# Shade dynamic-inefficiency region (r < n_p)
plot!(p2, c2_crash.iter, fill(n_p_2050_ann_pct, length(c2_crash.iter));
      fillrange = -30, fillalpha = 0.10, fillcolor = :red, linealpha = 0,
      label = "r < n_p (dynamic inefficiency)")
# Annotate the crossing iter
ix_cross = findfirst(i -> r_annual_pct(c2_crash.r5[i]) < n_p_2050_ann_pct, eachindex(c2_crash.r5))
if ix_cross !== nothing
    vline!(p2, [c2_crash.iter[ix_cross]];
           lw = 1.5, ls = :dot, color = :black,
           label = "first iter with r < n_p")
end

savefig(p2, joinpath(RESULTS_DIR, "c2_interp1_crash_r_vs_np.png"))
println("Wrote c2_interp1_crash_r_vs_np.png")

# ─── Panel 3: |DIFF/Y| on log scale, both runs ───────────────────────────────
p3 = plot(c2_crash.iter, abs.(c2_crash.DIFF);
          yscale = :log10, lw = 2.5, marker = :circle, color = :firebrick,
          label  = "C2 interp 1 (oscillates)",
          xlabel = "GE iter", ylabel = "|DIFF/Y| (log scale)",
          title  = "Goods-market residual — converges vs oscillates",
          legend = :bottomleft)
plot!(p3, run1.iter, abs.(run1.DIFF);
      lw = 2, marker = :diamond, color = :steelblue,
      label = "RUN 1 baseline (geometric decay)")
hline!(p3, [1e-4]; lw = 1.5, ls = :dash, color = :darkgreen,
       label = "convergence gate (1e-4)")

savefig(p3, joinpath(RESULTS_DIR, "c2_interp1_crash_DIFF.png"))
println("Wrote c2_interp1_crash_DIFF.png")

# ─── Combined 1×3 panel for the paper ────────────────────────────────────────
# Strip per-subplot titles in the combined view so they don't clash with
# the plot_title; standalone PNGs keep their own titles.
title!(p1, ""); title!(p2, ""); title!(p3, "")
combined = plot(p1, p2, p3; layout = (1, 3), size = (1500, 460),
                plot_title = "C2 closure with debt-absorbing pension deficit admits no finite SS at 2050",
                plot_titlefontsize = 12, bottom_margin = 4Plots.mm, left_margin = 4Plots.mm)
savefig(combined, joinpath(RESULTS_DIR, "c2_interp1_crash_panel.png"))
println("Wrote c2_interp1_crash_panel.png")

println("\nDone.")
