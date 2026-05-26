################################################################################
# run_aging_ssvs.jl
#
# Comparative-steady-state driver for the IDB June 5 seminar — implements
# CC_instrucciones_aging_steady_state.md §5. Reuses ge_model_gender.jl
# without editing it: overrides demographic primitives and fiscal-closure
# functions at runtime via Core.eval / const redefinition.
#
# Runs (all share whatever gender_gap mode ge_model_gender.jl is in):
#   RUN 1      2020 baseline                  joint closure (τp endog, B residual)
#   CONTROL    2020 via override              should match RUN 1 within tol
#   RUN 2 / C1 2050 joint closure             τp and B both endogenous
#   RUN 3 / C2 2050 τp pinned at 2020         B absorbs (debt channel)
#   RUN 4 / C3 2050 B pinned at 2020          τω absorbs (tax channel)  [opt]
#
# Toggles below. RUN_C3 is off by default — see §4 of CC_instrucciones.
#
# Outputs:
#   results/aging_comparison{_gap}.csv   (one row per run)
#   results/welfare_panel{_gap}.png      (welfare-at-birth 2×2 grid)
#   stdout                               (per-run summary + seminar table)
################################################################################

using Printf, Statistics

const GE_SRC      = joinpath(@__DIR__, "..", "ge_model_gender.jl")
const DEMOG_2050  = joinpath(@__DIR__, "demographics_2050.jl")
const RESULTS_DIR = joinpath(@__DIR__, "results")

# `include` brings the GE solver into Main without firing its main() (guarded
# at line 1172 of ge_model_gender.jl by abspath(PROGRAM_FILE) == @__FILE__).
include(GE_SRC)
include(DEMOG_2050)
isdir(RESULTS_DIR) || mkpath(RESULTS_DIR)

# ── Toggles ──────────────────────────────────────────────────────────────────
const RUN_CONTROL = true   # smoke-test the override pattern (§7 of CC_instrucciones)
const RUN_C3      = false  # debt-pinned; turn on after C1+C2 validated

# Run-tag mirrors ge_model_gender.jl's output suffix convention.
const RUN_TAG = gender_gap ? "_gap" : ""

# ── active_τω shim ───────────────────────────────────────────────────────────
# Single mutable holder read by labor_supply and available_resources. In
# :residual_B mode it stays at τw (the constant from ge_model_gender.jl);
# in :residual_τω mode compute_debt! updates it each GE iter to clear the
# general budget. Using a Ref avoids re-declaring globals on every closure
# switch and keeps the dispatch type-stable.
const active_τω = Ref{Float64}(τw)

# One-time redefinition of the two household-side functions that depend on
# the labor-tax rate. After this, both read active_τω[] instead of τw.
@eval Main begin
    function labor_supply(j::Int, h::Float64, η::Float64,
                          ig::Int, iθ::Int)::Float64
        if j >= j_R
            return 0.0
        end
        ν_j = productivity(j, h, η, ig, iθ)
        ν_j <= 0.0 && return 0.0
        numer = w_now * ν_j * (1.0 - active_τω[] - τp_now)
        denom = (1.0 + τc) * Ψ_labor
        ℓ_star = (numer / denom) ^ (1.0 / ν_pref)
        return clamp(ℓ_star, 0.0, 1.0)
    end

    function available_resources(a::Float64, h::Float64, η::Float64,
                                  ig::Int, iθ::Int, j::Int)::Float64
        if j < j_R
            ℓ   = labor_supply(j, h, η, ig, iθ)
            ν_j = productivity(j, h, η, ig, iθ)
            labor_income = w_now * ν_j * ℓ * (1.0 - active_τω[] - τp_now)
            return (1.0 + rn_now) * a + labor_income
        else
            return (1.0 + rn_now) * a + pen_now
        end
    end
end

# ── Override helpers ─────────────────────────────────────────────────────────

# Replace n_p and ψ_base. ge_model_gender.jl declares both as TYPED GLOBALS
# (n_p::Float64, ψ_base::Matrix{Float64}) — was const, switched to typed
# global precisely because Julia 1.x const redefinition allows the binding
# to change but compiled methods keep the inlined value (RUN 2 in the first
# attempt got identical equilibrium to RUN 1, confirming this). Typed
# globals are not inlined, so the override propagates.
function set_demographics!(n_p_new::Float64,
                           ψ_m_new::AbstractVector{<:Real},
                           ψ_f_new::AbstractVector{<:Real})
    @assert length(ψ_m_new) == J "ψ_male must have length J = $J"
    @assert length(ψ_f_new) == J "ψ_female must have length J = $J"
    new_ψ = vcat(reshape(Float64.(collect(ψ_m_new)), 1, :),
                 reshape(Float64.(collect(ψ_f_new)), 1, :))
    setglobal!(Main, :n_p, n_p_new)
    setglobal!(Main, :ψ_base, new_ψ)
    return nothing
end

# Pension closure: :endogenous (PAYG balance) or :fixed at τp_fixed.
function set_pension_closure!(mode::Symbol, τp_fixed::Float64 = 0.0)
    if mode === :endogenous
        @eval Main begin
            function update_pension_taxes!(L_eff::Float64)
                global τp_now, pen_now, wn_now
                if N_W_now > 0.0
                    τp_now  = κ_rep * N_R_now / N_W_now
                    pen_now = κ_rep * w_now * L_eff / N_W_now
                end
                wn_now = w_now * (1.0 - active_τω[] - τp_now)
            end
        end
    elseif mode === :fixed
        τp_val = τp_fixed
        @eval Main begin
            function update_pension_taxes!(L_eff::Float64)
                global τp_now, pen_now, wn_now
                τp_now = $(τp_val)
                if N_W_now > 0.0
                    pen_now = κ_rep * w_now * L_eff / N_W_now
                end
                wn_now = w_now * (1.0 - active_τω[] - τp_now)
            end
        end
    else
        error("Unknown pension closure: $mode (expected :endogenous or :fixed)")
    end
    return nothing
end

# Debt closure: :residual_B (default) or :residual_τω with B pinned at B_fixed.
# :residual_τω drives active_τω each GE iter from the budget-clearing condition;
# damping on K,L (damp_ge=0.5) is expected to carry the τω fixed point along.
# If C3 fails to converge, drop it per §4 / §6 of CC_instrucciones.
function set_debt_closure!(mode::Symbol, B_fixed::Float64 = 0.0)
    if mode === :residual_B
        active_τω[] = τw   # household sees the constant tax rate
        @eval Main begin
            function compute_debt!(C::Float64, L::Float64, K::Float64,
                                   M::Float64, Y::Float64)
                global B_debt_now
                G = gy * Y
                primary = τc*C + τw*w_now*L + τk*r_now*K + τm*M - G
                B_debt_now = primary / (rn_now - n_p)
            end
        end
    elseif mode === :residual_τω
        active_τω[] = τw   # initial guess for the C3 fixed point
        B_val = B_fixed
        @eval Main begin
            function compute_debt!(C::Float64, L::Float64, K::Float64,
                                   M::Float64, Y::Float64)
                global B_debt_now
                B_debt_now = $(B_val)
                G = gy * Y
                # Primary surplus needed to service the pinned B at (rn − n_p).
                primary_req = (rn_now - n_p) * $(B_val)
                # Linear solve for τω given current (C, L, K, M):
                #   τc·C + τω·w·L + τk·r·K + τm·M − G = primary_req
                if abs(w_now * L) > 1e-12
                    active_τω[] = (primary_req + G - τc*C - τk*r_now*K - τm*M) /
                                  (w_now * L)
                end
            end
        end
    else
        error("Unknown debt closure: $mode (expected :residual_B or :residual_τω)")
    end
    return nothing
end

# ── Per-run driver ───────────────────────────────────────────────────────────

mutable struct RunResult
    label::String
    K::Float64; L::Float64; Y::Float64
    r_annual::Float64; w::Float64
    τp::Float64; τω::Float64
    B::Float64; B_over_Y::Float64
    C_over_Y::Float64; M_over_Y::Float64
    N_W::Float64; N_R::Float64; depratio::Float64
    W_MθL::Float64; W_MθH::Float64; W_FθL::Float64; W_FθH::Float64
    DIFF::Float64; euler_max::Float64
    reportable::Bool
end

function run_one(label::String)
    println("\n", "="^72)
    println("  RUN: $label")
    println("="^72)
    hist, A_dom, L_new, C, M, Λvoid, Y, K, L = solve_ge!()
    W = welfare_at_birth()
    r_annual = ((1.0 + r_now)^0.2 - 1.0) * 100
    res = euler_residual_stats()
    eulmax = isempty(res) ? -Inf : maximum(log10.(max.(res, 1e-16)))
    # Spec §6 gates for reportability — looser than diagnostic_gates() which
    # would abort the script if it fired.
    reportable = abs(hist.DIFF[end]) < 1e-3 && eulmax < -3.0
    @printf "  → K=%.4f  L=%.4f  r(ann)=%.3f%%  τp=%.4f  τω=%.4f  B/Y=%.4f\n" K L r_annual τp_now active_τω[] (B_debt_now/Y)
    @printf "    DIFF/Y=%+.2e  Euler max log10=%.2f  reportable=%s\n" hist.DIFF[end] eulmax reportable
    return RunResult(
        label, K, L, Y, r_annual, w_now,
        τp_now, active_τω[],
        B_debt_now, B_debt_now / Y,
        C / Y, M / Y,
        N_W_now, N_R_now, N_R_now / N_W_now,
        W[1,1], W[1,2], W[2,1], W[2,2],
        hist.DIFF[end], eulmax, reportable,
    )
end

# ── Output: CSV, table, welfare plot ─────────────────────────────────────────

function write_comparison_csv(results::Vector{RunResult})
    path = joinpath(RESULTS_DIR, "aging_comparison$(RUN_TAG).csv")
    open(path, "w") do io
        println(io, "label,K,L,Y,r_annual_pct,w,taup,tauomega,B,B_over_Y," *
                    "C_over_Y,M_over_Y,N_W,N_R,depratio," *
                    "W_MthetaL,W_MthetaH,W_FthetaL,W_FthetaH," *
                    "DIFF_over_Y,euler_max_log10,reportable")
        for r in results
            @printf(io, "%s,%.6f,%.6f,%.6f,%.5f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.3e,%.3f,%s\n",
                r.label, r.K, r.L, r.Y, r.r_annual, r.w,
                r.τp, r.τω, r.B, r.B_over_Y, r.C_over_Y, r.M_over_Y,
                r.N_W, r.N_R, r.depratio,
                r.W_MθL, r.W_MθH, r.W_FθL, r.W_FθH,
                r.DIFF, r.euler_max, r.reportable)
        end
    end
    println("\nWrote $(path)")
    return path
end

# Shorthand label for the seminar table column.
function _short(label::String)
    startswith(label, "RUN 1")  && return "2020"
    startswith(label, "CONTROL") && return "CTRL"
    startswith(label, "RUN 2")  && return "C1"
    startswith(label, "RUN 3")  && return "C2"
    startswith(label, "RUN 4")  && return "C3"
    return label
end

function print_seminar_table(results::Vector{RunResult})
    display = [r for r in results if !startswith(r.label, "CONTROL")]
    cols = [_short(r.label) for r in display]
    nc   = length(display)

    println("\n", "="^72)
    println("  SEMINAR TABLE — Aging comparative steady state, Mexico" *
            (RUN_TAG == "_gap" ? " (gender_gap)" : " (symmetric)"))
    println("="^72)

    header = @sprintf "  %-26s" ""
    for c in cols; header *= @sprintf "%11s" c; end
    println(header)
    println("  " * "─"^(26 + 11*nc))

    function row(name, getter, fmt_str)
        # @sprintf needs a literal format at parse time; Printf.Format wraps
        # a runtime string so we can pass formats through this helper.
        fmt = Printf.Format(fmt_str)
        s = @sprintf "  %-26s" name
        for r in display
            s *= Printf.format(fmt, getter(r))
        end
        println(s)
    end

    row("K (capital)",        r->r.K,            "%11.3f")
    row("Y (output)",         r->r.Y,            "%11.3f")
    row("r (annual, %)",      r->r.r_annual,    "%10.2f%%")
    row("τp (%)",             r->100*r.τp,       "%10.2f%%")
    row("τω (%)",             r->100*r.τω,       "%10.2f%%")
    row("B/Y (%)",            r->100*r.B_over_Y, "%10.2f%%")
    row("Dep. ratio N^R/N^W", r->r.depratio,     "%11.4f")

    println("\n  Welfare at birth W₁(g,θ):")
    row("  M, θL", r->r.W_MθL, "%11.4f")
    row("  M, θH", r->r.W_MθH, "%11.4f")
    row("  F, θL", r->r.W_FθL, "%11.4f")
    row("  F, θH", r->r.W_FθH, "%11.4f")

    println("\n  Diagnostics & reportability (spec §6: DIFF/Y < 1e-3, Euler < -3):")
    for r in results
        flag = r.reportable ? "✔ REPORT  " : "⚠ DO NOT  "
        @printf "    %s  %-50s  DIFF/Y=%+.2e  Euler=%.2f\n" flag r.label r.DIFF r.euler_max
    end
end

# Welfare panel: 2×2 grid (one subplot per agent type), 4 bars per subplot
# (one per scenario in display order). Uses Plots.jl, already loaded by
# ge_model_gender.jl.
function plot_welfare_panel(results::Vector{RunResult})
    display = [r for r in results if !startswith(r.label, "CONTROL")]
    labels  = [_short(r.label) for r in display]
    types   = [("M, θL", r->r.W_MθL), ("M, θH", r->r.W_MθH),
               ("F, θL", r->r.W_FθL), ("F, θH", r->r.W_FθH)]
    panels = []
    for (tname, getter) in types
        vals = [getter(r) for r in display]
        p = bar(labels, vals;
                ylabel = "W₁", title = tname, label = "",
                color = :steelblue, legend = false)
        push!(panels, p)
    end
    p = plot(panels...; layout = (2, 2), size = (900, 700),
             plot_title = "Welfare at birth — aging comparative SS$(RUN_TAG)")
    out = joinpath(RESULTS_DIR, "welfare_panel$(RUN_TAG).png")
    savefig(p, out)
    println("Wrote $(out)")
    return out
end

# ── main ─────────────────────────────────────────────────────────────────────

function main()
    println("="^72)
    println("  Aging comparative-steady-state experiment — IDB seminar 2026-06-05")
    println("="^72)
    println("  Source : $(GE_SRC)")
    println("  J = $J  ·  4 agent types  ·  gender_gap = $(gender_gap)  ·  tag = '$(RUN_TAG)'")
    println("  Toggles: RUN_CONTROL = $(RUN_CONTROL)  ·  RUN_C3 = $(RUN_C3)")

    # Grid + Markov-chain initialization. Normally done inside
    # ge_model_gender.jl::main(), but we bypass that via the include
    # guard (PROGRAM_FILE check) so we have to do it here. Without
    # this, π_η_erg stays at the const-init zeros → forward_distribution!
    # seeds Φ as all-zero → aggregates are zero → solve_ge! diverges
    # within one iter.
    println("\nInitializing grids and Rouwenhorst chain …")
    grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
    grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
    π_mat, η_vec = rouwenhorst(Nη, ρ_AR, σ_ε, 0.0)
    π_η .= π_mat
    η_grid .= η_vec
    compute_ergodic!()

    # Snapshot the 2020 calibration BEFORE any override fires.
    n_p_2020      = n_p
    ψ_base_2020_m = copy(ψ_base[1, :])
    ψ_base_2020_f = copy(ψ_base[2, :])
    @printf "  2020 saved : n_p = %.6f   ψ_male[1..3] = %s\n" n_p_2020 ψ_base_2020_m[1:3]

    results = RunResult[]

    # ── RUN 1: 2020 baseline ────────────────────────────────────────────────
    set_pension_closure!(:endogenous)
    set_debt_closure!(:residual_B)
    r_baseline = run_one("RUN 1 · 2020 baseline (joint closure)")
    push!(results, r_baseline)

    τp_2020 = r_baseline.τp
    B_2020  = r_baseline.B
    @printf "  → captured: τp_2020 = %.6f   B_2020 = %.4f   B/Y_2020 = %.4f\n" τp_2020 B_2020 r_baseline.B_over_Y

    # ── CONTROL: override pattern smoke-test ────────────────────────────────
    if RUN_CONTROL
        set_demographics!(n_p_2020, ψ_base_2020_m, ψ_base_2020_f)
        set_pension_closure!(:endogenous)
        set_debt_closure!(:residual_B)
        r_control = run_one("CONTROL · 2020 via override (gate: ≈ RUN 1)")
        push!(results, r_control)
        ΔK  = abs(r_control.K  - r_baseline.K)
        Δτp = abs(r_control.τp - r_baseline.τp)
        @printf "  → smoke-test residuals  |ΔK| = %.3e   |Δτp| = %.3e\n" ΔK Δτp
        if ΔK > 1e-3 || Δτp > 1e-4
            @warn "CONTROL diverges from RUN 1 — override pattern may not propagate. 2050 results are suspect."
        end
    end

    # ── RUN 2 (C1): 2050 joint closure ──────────────────────────────────────
    set_demographics!(n_p_2050, ψ_base_male_2050, ψ_base_female_2050)
    set_pension_closure!(:endogenous)
    set_debt_closure!(:residual_B)
    r_C1 = run_one("RUN 2 · 2050 C1 — joint (τp and B endogenous)")
    push!(results, r_C1)

    # ── RUN 3 (C2): 2050 with τp pinned at 2020 ─────────────────────────────
    set_pension_closure!(:fixed, τp_2020)
    set_debt_closure!(:residual_B)
    r_C2 = run_one("RUN 3 · 2050 C2 — τp pinned at 2020, B absorbs")
    push!(results, r_C2)
    @printf "  → pin check: τp − τp_2020 = %.3e (gate: 0)\n" (r_C2.τp - τp_2020)

    # ── RUN 4 (C3): 2050 with B pinned at 2020 ──────────────────────────────
    if RUN_C3
        set_pension_closure!(:endogenous)
        set_debt_closure!(:residual_τω, B_2020)
        r_C3 = run_one("RUN 4 · 2050 C3 — B pinned at 2020, τω absorbs")
        push!(results, r_C3)
        @printf "  → pin check: B − B_2020 = %.3e (gate: 0)\n" (r_C3.B - B_2020)
        @printf "  → C3 implied τω = %.5f (vs τω_2020 = %.5f)\n" r_C3.τω τw
    end

    # ── Outputs ─────────────────────────────────────────────────────────────
    write_comparison_csv(results)
    print_seminar_table(results)
    try
        plot_welfare_panel(results)
    catch e
        @warn "Welfare panel plot failed (continuing): $e"
    end
    println("\nDone.")
    return results
end

# Run main() only when invoked directly — keeps the file safely include-able
# from an audit script.
if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
