################################################################################
# diagnose_gender_gap_euler.jl
#
# Locate where the gender-gap Euler-residual spike (log10 max ≈ -1.18 in
# Diego's production run) lives in the (j, ig, iθ, ia, ih, is) state space.
#
# Why this script exists. The source comment at ge_model_gender.jl:938-942
# already flags that "rare near-corner old-age cells on the kinked bilinear
# surface can spike to ~10⁻¹". The hard gate is < -1; the seminar bar
# (spec §6) is < -3. Either we move the goalposts (mass-weighted max) or we
# fix the underlying numerics (interpolate uc directly, finer m grid, etc.).
# Either path needs to know WHERE the bad cells are.
#
# Shortcut. The household-side numerics depend on primitives, prices, and
# grids — not on whether (K, L) sit at the GE fixed point. So we plug in
# the SYMMETRIC equilibrium prices (from ge_summary.csv, gender_gap=false)
# and run ONE solve_household! under gender_gap = true. ~12 min vs ~2.5 h.
#
# Hypothesis to test:
#   spike cells concentrate at (j ≥ J-2, ig=2 [female], low-η, near-corner
#   a' or m) with near-zero mass. If confirmed, fix is a mass-weighted max
#   statistic; the welfare aggregates are unaffected.
#
# Run from GE-now with Gender/:
#   julia --project=. demographic_experiment/diagnose_gender_gap_euler.jl
#
# Outputs:
#   diagnostics/euler_cells_gap.csv       per-cell residuals + state + mass
#   diagnostics/euler_summary_gap.txt     console log copy
#   stdout                                summary tables (raw + mass-weighted)
################################################################################

using Printf, Statistics

const GE_SRC  = joinpath(@__DIR__, "..", "ge_model_gender.jl")
const OUT_DIR = joinpath(@__DIR__, "diagnostics")
isdir(OUT_DIR) || mkpath(OUT_DIR)

include(GE_SRC)

@assert gender_gap "Set gender_gap = true in ge_model_gender.jl before running this diagnostic."

# ── Symmetric-equilibrium prices (from ge_summary.csv) ───────────────────────
# Gender_gap = false GE run, J = 17, 4-type, converged 13 iters.
const r_sym   = 0.2820500440564091
const w_sym   = 0.9726505799955998
const τp_sym  = 0.1387247530090478
const pen_sym = 1.1624960178500605

println("="^72)
println("  Gender-gap Euler-residual diagnostic (household solve at sym prices)")
println("="^72)
@printf "  gender_gap = %s    J = %d    grid = NA×NH×Nη = %d×%d×%d\n" gender_gap J (NA+1) (NH+1) Nη
@printf "  symmetric prices: r=%.4f  w=%.4f  τp=%.4f  pen=%.4f\n" r_sym w_sym τp_sym pen_sym

# ── Initialize grids and Markov chain ────────────────────────────────────────
println("\nInitializing grids and Rouwenhorst chain …")
grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
π_mat, η_vec = rouwenhorst(Nη, ρ_AR, σ_ε, 0.0)
π_η .= π_mat
η_grid .= η_vec
compute_ergodic!()

# Pin globals to symmetric values (solve_household reads these typed globals).
global r_now   = r_sym
global w_now   = w_sym
global rn_now  = r_sym * (1.0 - τk)
global wn_now  = w_sym * (1.0 - τw - τp_sym)
global τp_now  = τp_sym
global pen_now = pen_sym

# ── Household solve ──────────────────────────────────────────────────────────
println("\nSolving household block (4 types × backward induction over J) …")
t0 = time()
solve_household!()
solve_min = (time() - t0) / 60
@printf "  household solve: %.1f min  (parabolic refinement: %d cells)\n" solve_min n_refined[]

# ── Forward distribution for mass weighting ─────────────────────────────────
println("\nPropagating forward distribution …")
forward_distribution!()
compute_population!()
@printf "  Σ Φ = %.6f   N_W = %.4f   N_R = %.4f   N_R/N_W = %.4f\n" sum(Φ) N_W_now N_R_now (N_R_now/N_W_now)

# ── Per-cell Euler residuals ─────────────────────────────────────────────────
struct CellResid
    j::Int; ig::Int; iθ::Int; ia::Int; ih::Int; is::Int
    a::Float64; h::Float64; η::Float64
    aprime::Float64; m::Float64; c::Float64; ℓ::Float64
    uc::Float64; resid::Float64; rel::Float64; mass::Float64
    a_corner::Bool; m_zero::Bool; m_top::Bool
end

println("\nComputing per-cell Euler residuals …")
cells = CellResid[]
sizehint!(cells, (J-1) * Ng * Nθ * (NA+1) * (NH+1) * Nη)

for j in 1:(J-1), ig in 1:Ng, iθ in 1:Nθ
    for ia in 0:NA, ih in 0:NH, is in 1:Nη
        ap = aplus_pol[j, ig, ia, ih, is, iθ]
        mm = m_pol[j, ig, ia, ih, is, iθ]
        cc = c_pol[j, ig, ia, ih, is, iθ]
        ℓℓ = l_pol[j, ig, ia, ih, is, iθ]
        h_now = h_grid[ih]
        η_now = η_grid[is]

        r  = euler_residual(ap, j, ia, ih, is, ig, iθ, mm, h_now)
        uc = marginal_utility_c(cc, ℓℓ, h_now)
        rel = uc > 1e-12 ? abs(r) / uc : NaN

        X = available_resources(a_grid[ia], h_now, η_now, ig, iθ, j)
        avail_after_m = X - (1.0 + τm) * mm
        a_hi = max(avail_after_m - 1e-6, a_l)
        m_top_thr = max(m_max_frac * X, m_min * 2.0)

        push!(cells, CellResid(
            j, ig, iθ, ia, ih, is,
            a_grid[ia], h_now, η_now,
            ap, mm, cc, ℓℓ,
            uc, r, rel, Φ[j, ig, ia, ih, is, iθ],
            ap <= a_l + 1e-9 || ap >= a_hi - 1e-6,
            mm <= 1.001 * m_min,
            mm >= 0.999 * m_top_thr,
        ))
    end
end
println("  $(length(cells)) cells")

# ── Summary statistics ───────────────────────────────────────────────────────

function logstats(vals::Vector{Float64})
    isempty(vals) && return (NaN, NaN, NaN, NaN, NaN)
    lv = log10.(vals)
    return (mean(lv), maximum(lv), quantile(lv, 0.50),
            quantile(lv, 0.95), quantile(lv, 0.99))
end

function mw_logstats(cs::Vector{CellResid})
    mw = filter(c -> c.mass > 1e-15 && !isnan(c.rel) && c.rel > 0.0, cs)
    isempty(mw) && return (NaN, NaN, 0.0, 0)
    total = sum(c.mass for c in mw)
    mean  = sum(c.mass * log10(c.rel) for c in mw) / total
    mx    = maximum(log10(c.rel) for c in mw)
    return (mean, mx, total, length(mw))
end

println("\n", "="^72)
println("  Summary statistics — Euler residual log10 |r| / u_c")
println("="^72)

all_pos = [c.rel for c in cells if !isnan(c.rel) && c.rel > 0.0]
m, mx, p50, p95, p99 = logstats(all_pos)
@printf "  All cells (n = %d):\n" length(all_pos)
@printf "    mean = %.3f    max = %.3f    p50 = %.3f    p95 = %.3f    p99 = %.3f\n" m mx p50 p95 p99

interior = [c for c in cells if !c.a_corner && !isnan(c.rel) && c.rel > 0.0]
m, mx, p50, p95, p99 = logstats([c.rel for c in interior])
@printf "  Interior (a' not at boundary, n = %d):\n" length(interior)
@printf "    mean = %.3f    max = %.3f    p50 = %.3f    p95 = %.3f    p99 = %.3f\n" m mx p50 p95 p99

mw_mean, mw_max, mw_total, mw_n = mw_logstats(cells)
@printf "  Mass-weighted (mass > 1e-15, n = %d, Σmass = %.4e):\n" mw_n mw_total
@printf "    mass-weighted mean = %.3f    max = %.3f\n" mw_mean mw_max

mw_int_mean, mw_int_max, mw_int_total, mw_int_n = mw_logstats(interior)
@printf "  Mass-weighted interior (n = %d, Σmass = %.4e):\n" mw_int_n mw_int_total
@printf "    mass-weighted mean = %.3f    max = %.3f\n" mw_int_mean mw_int_max

# ── Worst cells ──────────────────────────────────────────────────────────────
sort!(cells, by = c -> -c.rel)
println("\n", "="^72)
println("  Top 20 worst cells (any mass)")
println("="^72)
@printf "  %3s %3s %3s %4s %4s %3s %8s %6s %7s %9s %8s %7s %7s %10s %3s %3s %3s\n" "j" "ig" "iθ" "ia" "ih" "is" "a" "h" "η" "log10rel" "aprime" "m" "c" "mass" "ac" "mt" "mz"
for c in cells[1:min(20, end)]
    ig_lbl = c.ig == 1 ? "M" : "F"
    iθ_lbl = c.iθ == 1 ? "L" : "H"
    @printf "  %3d  %s   %s  %4d %4d %3d %8.2f %6.3f %+7.3f %9.3f %8.2f %7.4f %7.3f %10.2e  %s   %s   %s\n" c.j ig_lbl iθ_lbl c.ia c.ih c.is c.a c.h c.η log10(max(c.rel,1e-16)) c.aprime c.m c.c c.mass (c.a_corner ? "Y" : "·") (c.m_top ? "Y" : "·") (c.m_zero ? "Y" : "·")
end

println("\nTop 20 worst cells with mass > 1e-10:")
mass_filt = filter(c -> c.mass > 1e-10, cells)
@printf "  %3s %3s %3s %4s %4s %3s %8s %6s %7s %9s %8s %7s %7s %10s %3s %3s %3s\n" "j" "ig" "iθ" "ia" "ih" "is" "a" "h" "η" "log10rel" "aprime" "m" "c" "mass" "ac" "mt" "mz"
for c in mass_filt[1:min(20, end)]
    ig_lbl = c.ig == 1 ? "M" : "F"
    iθ_lbl = c.iθ == 1 ? "L" : "H"
    @printf "  %3d  %s   %s  %4d %4d %3d %8.2f %6.3f %+7.3f %9.3f %8.2f %7.4f %7.3f %10.2e  %s   %s   %s\n" c.j ig_lbl iθ_lbl c.ia c.ih c.is c.a c.h c.η log10(max(c.rel,1e-16)) c.aprime c.m c.c c.mass (c.a_corner ? "Y" : "·") (c.m_top ? "Y" : "·") (c.m_zero ? "Y" : "·")
end

# ── Per-(j, ig, iθ) breakdown ────────────────────────────────────────────────
println("\n", "="^72)
println("  Max log10 |r|/uc by (j, ig, iθ)  — flags cells with log10 > -3")
println("="^72)
@printf "  %3s  %2s   %2s   %12s  %10s  %10s  %12s\n" "j" "ig" "iθ" "max log10" "n_>-3" "n_>-1" "Σmass(>-3)"
for j in 1:(J-1), ig in 1:Ng, iθ in 1:Nθ
    grp = filter(c -> c.j == j && c.ig == ig && c.iθ == iθ && !isnan(c.rel) && c.rel > 0, cells)
    isempty(grp) && continue
    log_vals = log10.([c.rel for c in grp])
    mx = maximum(log_vals)
    n_bad = count(>(-3.0), log_vals)
    n_terr = count(>(-1.0), log_vals)
    mass_bad = sum(c.mass for c in grp if log10(c.rel) > -3.0; init=0.0)
    ig_lbl = ig == 1 ? "M" : "F"
    iθ_lbl = iθ == 1 ? "θL" : "θH"
    @printf "  %3d  %s    %s    %12.3f  %10d  %10d  %12.4e\n" j ig_lbl iθ_lbl mx n_bad n_terr mass_bad
end

# ── Hypothesis verdict ───────────────────────────────────────────────────────
println("\n", "="^72)
println("  Hypothesis verdict")
println("="^72)

if !isempty(cells)
    worst = cells[1]
    println("  Worst cell:")
    @printf "    (j, ig, iθ, ia, ih, is) = (%d, %d, %d, %d, %d, %d)\n" worst.j worst.ig worst.iθ worst.ia worst.ih worst.is
    @printf "    log10 |r|/uc = %.3f    mass = %.3e\n" log10(max(worst.rel, 1e-16)) worst.mass
    @printf "    a_corner = %s   m_top = %s   m_zero = %s\n" worst.a_corner worst.m_top worst.m_zero

    near_terminal = count(c -> c.j >= J - 2 && log10(max(c.rel, 1e-16)) > -3.0, cells)
    female_bad    = count(c -> c.ig == 2  && log10(max(c.rel, 1e-16)) > -3.0, cells)
    male_bad      = count(c -> c.ig == 1  && log10(max(c.rel, 1e-16)) > -3.0, cells)
    @printf "  Cells with log10 > -3:  total = %d   near-terminal (j ≥ J-2) = %d   female = %d   male = %d\n" (female_bad + male_bad) near_terminal female_bad male_bad

    if mw_int_max < -3.0
        println("  → Mass-weighted interior max < -3: spike is cosmetic;")
        println("    fix is to switch the reported statistic to mass-weighted.")
    else
        println("  → Mass-weighted interior max ≥ -3: spike is real, not cosmetic.")
        println("    Candidate fixes: interpolate uc directly (not c),")
        println("    finer m grid at old ages, midpoint a' refinement.")
    end
end

# ── CSV dump ─────────────────────────────────────────────────────────────────
csv_path = joinpath(OUT_DIR, "euler_cells_gap.csv")
open(csv_path, "w") do io
    println(io, "j,ig,itheta,ia,ih,is,a,h,eta,aprime,m,c,l,uc,resid,rel,log10_rel,mass,a_corner,m_zero,m_top")
    for c in cells
        log_rel_val = !isnan(c.rel) && c.rel > 0 ? log10(c.rel) : NaN
        @printf(io, "%d,%d,%d,%d,%d,%d,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6e,%.6e,%.6e,%.6f,%.6e,%d,%d,%d\n",
            c.j, c.ig, c.iθ, c.ia, c.ih, c.is,
            c.a, c.h, c.η, c.aprime, c.m, c.c, c.ℓ,
            c.uc, c.resid, c.rel, log_rel_val, c.mass,
            c.a_corner ? 1 : 0, c.m_zero ? 1 : 0, c.m_top ? 1 : 0)
    end
end
println("\nWrote $(csv_path)  ($(length(cells)) cells)")

# Run-tag echo so the post-run README log section is easy to fill in.
println("\nRun complete.  Use the per-(j, ig, iθ) table above to spot whether the")
println("spike concentrates in the predicted (j ≥ J-2, female, near-corner) slice.")
