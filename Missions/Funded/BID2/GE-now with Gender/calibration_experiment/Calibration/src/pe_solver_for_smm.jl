################################################################################
#  pe_solver_for_smm.jl
#
#  SMM-callable variant of `Household-Gender/household_problem_gender.jl`.
#  Mathematically identical to the PE reference solver; differs only in:
#
#    1. The 6 SMM parameters and the 4 fixed-price anchors are `Ref{Float64}`
#       so the SMM driver can rewrite them between solves without redefining
#       constants:  Ψ_labor, Ξ_amenity, ξ_curv, H_scale, h_slope, H_curv,
#                   r_price, w_price, τp, pen_flow.   Read sites use `X[]`.
#       β stays `const` — fixed externally in this PE calibration (paper §4
#       K/Y target is dropped; see plan staged-drifting-clover.md).
#
#    2. First-step inputs (e_age, ψ_base, δh, π_birth, θ_grid, ϱ_pen, ρ_AR,
#       σ_ε) are pre-allocated zero arrays; `apply_first_step!(fs)` writes
#       them from a NamedTuple (loaded from CSVs in load_inputs.jl).
#
#    3. New entry points at the bottom:
#         apply_first_step!, apply_anchor!, apply_theta!, init_grids!,
#         solve_pe_at!(θ, anchor, first_step; verify=false)
#       `solve_pe_at!` returns a NamedTuple of policies + Φ — no CSV / plots.
#
#    4. `diagnostic_gates(verify::Bool=true)` is callable but skipped on the
#       SMM hot path so a pathological trial doesn't crash the optimizer.
#       CSV-write / plot helpers from the reference solver are dropped.
#
#  All other content — helpers, inline Brent root-finder, m* parabolic
#  refinement, forward-distribution sweep — is byte-identical to the
#  reference solver. The parity smoke test (run_calibration.jl) diffs the
#  cohort-mean CSV against `Household-Gender/household_lifecycle_gap.csv`
#  and expects ≲ 1e-11.
#
#  Build switch — the single line `const J` selects the build:
#    J = 16  → Tier A collapse check. With men ≡ women and symmetric birth
#              shares this reproduces DraftApril exactly.
#    J = 17  → gender deliverable (modelwithgender.tex §4: ages 20–100).
#
#  Stub status — men ≡ women until calibration §4 plugs in real data:
#    e_age, ψ_base  : 2×J matrices, both rows identical            [STUB]
#    π_birth        : 2×2, all four (g,θ) types = 0.25             [STUB]
#    h_slope = 0    : age-invariant health production (= DraftApril) [STUB]
#    ψ_base[·,17],
#    δh[17]         : terminal entries extrapolated (J=17 build)   [STUB-extrap]
#
#  Index conventions:
#    • Time periods are 5 years. Ages j = 1..J, j = 1 ↔ age 20.
#    • Retirement at j = j_R. ψ^g_{J+1} ≡ 0 (death after age J).
#    • Sex   ig ∈ {1, 2}: 1 = male, 2 = female.
#    • Skill iθ ∈ {1, 2}: 1 = θ_L, 2 = θ_H.
#    • Policy/value/distribution arrays are indexed (j, ig, ia, ih, is, iθ).
#    • Bequests are voided: bq ≡ 0 in the budget.
#    • Productivity sign follows the audited modelwithgender.tex (positive slope
#      in h — healthier ⇒ more productive):
#         ν_j(h, η; g, θ) = e^g_j · exp(θ + η + ϱ(θ) · h)
#
#  Numerical-Audit (2026-05-22):
#    • Inner root-find ported to an inline Brent (`brent_aprime`, copied from
#      GE-Fast) — kills per-cell closure allocations; deterministic, no
#      try/catch failure path.
#    • `diagnostic_gates()` adds hard @assert gates (budget residual,
#      consumption positivity, borrowing constraint, distribution sanity,
#      terminal condition, Euler residual, two-sex identity, cohort-share
#      invariant, health bounds) so a bad solve fails loudly.
#    • m* parabolic refinement (toggle `refine_m`): after the m-grid search a
#      parabola is fitted through the winning m-node and its two neighbours and
#      its vertex is taken as m* — removes most of the m-grid discretization
#      bias at one extra a'-solve. Set `refine_m = false` to recover the exact
#      DraftApril grid-search method.
#    • m-grid widened: m_max_frac 1/3 → 0.90, Nm 30 → 40. This removes the
#      ARBITRARY part of the m-grid cap; m*-at-top fell 3.2% → 2.2%. The
#      residual ~2.2% is a GENUINE near-budget corner — those agents optimally
#      spend ~all resources on medical care, because GHH preferences have no
#      consumption Inada (u_c finite as c→0) while health production does
#      (H'(m)→∞ as m→0). It is an economic corner, not a numerical artifact,
#      and SMM calibration of the health/amenity parameters will discipline it.
#  Known limitations (documented):
#    • The inner a' solve roots the Euler residual; on the kinked bilinear
#      continuation surface this is not cross-checked against the value.
#    • Single-threaded; the four (g,θ) type-solves are embarrassingly parallel.
################################################################################

using OffsetArrays
using DynamicProgrammingUtils
using Roots
using Printf
using Statistics
using Plots

# ─── Structural dimensions (truly fixed) ─────────────────────────────────────
const γ_pref     = 2.0                  # [PDF] GHH risk-aversion exponent
const ν_pref     = 2.0                  # [PDF] inverse Frisch elasticity (ν_ℓ)
const β_pref     = 0.998^5              # [PDF] discount factor, 5-yr period — FIXED externally

const J          = 17                   # [PDF] max age (ages 20..100 with 5-yr periods)
const j_R        = 10                   # [PDF] retirement age (period index)
const Nη         = 7                    # [PDF] productivity nodes
const Ng         = 2                    # 1 = male, 2 = female
const Nθ         = 2                    # 1 = θ_L, 2 = θ_H

const τc         = 0.16                 # [PDF] consumption tax (Mexico VAT)
const τm         = 0.00                 # [PDF] medical-spending tax (baseline)
const κ_rep      = 0.50                 # [PDF] pension replacement rate
const τw         = 0.20                 # [introduced] labor tax
const τk         = 0.20                 # [introduced] capital tax

const surv_floor = 0.70                 # [introduced] survival adjustment floor
const surv_slope = 1.0 - surv_floor     # [introduced] = 0.30

const h_init     = 1.00                 # [PDF-open] initial health h_0 = h̄
const n_p        = 1.01^5 - 1.0         # [introduced] population growth (5-yr)

# ─── Grid sizes (kept const — match Household-Gender; edit here if needed) ──
const NA         = 100                  # asset grid points
const a_l        = 0.0
const a_u        = 300.0
const a_grow     = 0.05
const NH         = 15                   # health grid points
const h_l        = 0.01
const h_u        = 1.00
const h_grow     = 0.05
const Nm         = 40                   # m-grid points (incl. m=0)
const m_min      = 1e-3
const m_max_frac = 0.90                 # m-grid upper bound as fraction of available resources
const refine_m   = Ref(true)            # parabolic refinement of m* (mutable for grids.csv override)

# ─── 6 SMM parameters (mutable; written by apply_theta!) ─────────────────────
const Ψ_labor    = Ref(14.0)            # labor-disutility scale (paper §4: Ψ)
const Ξ_amenity  = Ref(0.50)            # health-amenity scale  (paper §4: Ξ)
const ξ_curv     = Ref(0.50)            # health-amenity curvature (paper §4: ξ)
const H_scale    = Ref(0.30)            # health-production scale H̄_0
const h_slope    = Ref(0.00)            # health-production age-decline (paper: h^slope)
const H_curv     = Ref(0.50)            # health-production curvature ζ_h

# ─── 4 fixed-price anchors (mutable; written by apply_anchor!) ───────────────
const r_price    = Ref(1.03^5 - 1.0)    # PE interest rate (5-yr)
const w_price    = Ref(1.00)            # PE wage
const τp         = Ref(0.10)            # PE pension contribution
const pen_flow   = Ref(0.30)            # PE pension flow for retirees
const rn         = Ref(0.0)             # after-tax return = r_price[]·(1-τk); refreshed in apply_anchor!

# ─── First-step inputs (mutable; written by apply_first_step!) ───────────────
# Pre-allocated zero arrays; CSVs populate them at startup or per SMM trial.
const ρ_AR       = Ref(0.98)            # AR(1) persistence
const σ_ε        = Ref(0.05)            # AR(1) innovation s.d.
const e_age      = zeros(Ng, J)         # age-efficiency profile [sex, age]
const ψ_base     = zeros(Ng, J)         # baseline survival [sex, age]
const δh         = zeros(J)             # health depreciation by age
const π_birth    = zeros(Ng, Nθ)        # birth shares (must sum to 1)
const θ_grid     = zeros(Nθ)            # skill fixed effects
const ϱ_pen      = zeros(Nθ)            # health-productivity elasticity by skill

# ─── Grids (allocated as offset arrays) ──────────────────────────────────────
const a_grid    = OffsetArray(zeros(NA+1), 0:NA)
const h_grid    = OffsetArray(zeros(NH+1), 0:NH)
const η_grid    = zeros(Nη)
const π_η       = zeros(Nη, Nη)
const π_η_erg   = zeros(Nη)   # ergodic distribution of η

# Scratch buffers required by linint_Grow (length-1 mutable arrays).
const ial_buf      = Array{Int64}(undef, 1)
const iar_buf      = Array{Int64}(undef, 1)
const varphi_a_buf = zeros(1)
const ihl_buf      = Array{Int64}(undef, 1)
const ihr_buf      = Array{Int64}(undef, 1)
const varphi_h_buf = zeros(1)

# Count of cells where the m* parabolic refinement improved on the grid node.
const n_refined    = Ref(0)

# ─── Policy storage (j, ig, ia, ih, is, iθ) ──────────────────────────────────
const aplus_pol = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const m_pol     = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const c_pol     = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const l_pol     = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const hnext_pol = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const V_pol     = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)

# ─── Helper functions ────────────────────────────────────────────────────────

# modelwithgender.tex eq. health amenity s(h).
function health_amenity(h::Float64)::Float64
    h_safe = max(h, 1e-12)
    if abs(ξ_curv[] - 1.0) < 1e-10
        return Ξ_amenity[] * log(h_safe)
    else
        return Ξ_amenity[] * h_safe^(1.0 - ξ_curv[]) / (1.0 - ξ_curv[])
    end
end

# Disutility of labor v(ℓ).
disutility_of_labor(ℓ::Float64)::Float64 = Ψ_labor[] * ℓ^(1.0 + ν_pref) / (1.0 + ν_pref)

# GHH composite z = c + s(h) - v(ℓ).
ghh_z(c::Float64, ℓ::Float64, h::Float64)::Float64 =
    c + health_amenity(h) - disutility_of_labor(ℓ)

# Per-period utility u(c, ℓ, h).
function utility(c::Float64, ℓ::Float64, h::Float64)::Float64
    z = max(ghh_z(c, ℓ, h), 1e-12)
    return (z^(1.0 - γ_pref) - 1.0) / (1.0 - γ_pref)
end

# u_c = ∂u/∂c = z^{-γ}.
function marginal_utility_c(c::Float64, ℓ::Float64, h::Float64)::Float64
    z = max(ghh_z(c, ℓ, h), 1e-12)
    return z^(-γ_pref)
end

# Productivity ν_j(h, η; g, θ) = e^g_j · exp(θ + η + ϱ(θ)·h)  [modelwithgender.tex §3.4].
# Sex enters through the age-efficiency profile e^g_j; ϱ(θ) is skill-specific.
function productivity(j::Int, h::Float64, η::Float64, ig::Int, iθ::Int)::Float64
    if j >= j_R
        return 0.0
    end
    return e_age[ig, j] * exp(θ_grid[iθ] + η + ϱ_pen[iθ] * h)
end

# Survival ψ^g_j(h) — sex-specific baseline modulated by health.
# §4.1.1 placeholder modulation (surv_floor + surv_slope·h); the actual spec
# survival is the mortality probit (deferred to calibration).
function survival(j::Int, h::Float64, ig::Int)::Float64
    if j < 1 || j > J + 1
        return 0.0
    end
    if j == J + 1
        return 0.0
    end
    return ψ_base[ig, j] * (surv_floor + surv_slope * h)
end

# Health production H_j(m) = H̄_0·exp(-h_slope·j)·m^ζ_h  [modelwithgender.tex §4].
# With the stub h_slope = 0 this is the DraftApril age-invariant H_scale·m^H_curv
# (exp(-0·j) ≡ 1 exactly, so the Tier A collapse is bit-exact).
function health_production(m::Float64, j::Int)::Float64
    if m <= 0.0
        return 0.0
    end
    H_j = H_scale[] * exp(-h_slope[] * j)
    return H_j * m^H_curv[]
end

# Health law of motion h' = min{(1-δ^h_j)·h + H_j(m), h̄}.
function health_next(h::Float64, m::Float64, j::Int)::Float64
    return min((1.0 - δh[j]) * h + health_production(m, j), h_u)
end

# GHH labor-supply FOC: closed-form, no wealth effects.
#   ℓ* = ( w · ν_j(h,η;g,θ) · (1-τw-τp) / ((1+τc) · Ψ) )^{1/ν}
function labor_supply(j::Int, h::Float64, η::Float64, ig::Int, iθ::Int)::Float64
    if j >= j_R
        return 0.0
    end
    ν_j = productivity(j, h, η, ig, iθ)
    if ν_j <= 0.0
        return 0.0
    end
    numer = w_price[] * ν_j * (1.0 - τw - τp[])
    denom = (1.0 + τc) * Ψ_labor[]
    ℓ_star = (numer / denom) ^ (1.0 / ν_pref)
    return clamp(ℓ_star, 0.0, 1.0)
end

# Available resources X given pre-computed labor supply.
function available_resources(a::Float64, h::Float64, η::Float64,
                              ig::Int, iθ::Int, j::Int)::Float64
    if j < j_R
        ℓ = labor_supply(j, h, η, ig, iθ)
        ν_j = productivity(j, h, η, ig, iθ)
        labor_income = w_price[] * ν_j * ℓ * (1.0 - τw - τp[])
        return (1.0 + rn[]) * a + labor_income
        # NB: bq ≡ 0 (voiding), pen = 0 for workers.
    else
        return (1.0 + rn[]) * a + pen_flow[]
    end
end

# Solve budget identity for c given (a', m): c = (X - a' - (1+τm)m)/(1+τc).
function consumption_from_choices(j::Int, a::Float64, h::Float64, η::Float64,
                                   ig::Int, iθ::Int, a_prime::Float64, m::Float64)::Float64
    X = available_resources(a, h, η, ig, iθ, j)
    c = (X - a_prime - (1.0 + τm) * m) / (1.0 + τc)
    return max(c, 1e-12)
end

# ─── Bilinear interpolation of policies on (a, h) at fixed (is, ig, iθ) ───────

# Returns (ial, iar, φ_a) for asset a_prime.
function asset_interp(a_prime::Float64)
    ial, iar, φ_a = linint_Grow(a_prime, a_l, a_u, a_grow, NA, ial_buf, iar_buf, varphi_a_buf)
    ial = max(min(ial, NA - 1), 0)
    iar = max(min(iar, NA), 1)
    φ_a = clamp(φ_a, 0.0, 1.0)
    return ial, iar, φ_a
end

# Returns (ihl, ihr, φ_h) for h.
function health_interp(h::Float64)
    ihl, ihr, φ_h = linint_Grow(h, h_l, h_u, h_grow, NH, ihl_buf, ihr_buf, varphi_h_buf)
    ihl = max(min(ihl, NH - 1), 0)
    ihr = max(min(ihr, NH), 1)
    φ_h = clamp(φ_h, 0.0, 1.0)
    return ihl, ihr, φ_h
end

# Interpolate a stored 6-D policy at (a', h_next) for fixed (j_next, is, ig, iθ).
# Sex is discrete and fixed at birth: ig is a pure passthrough index.
function interp_pol(P::OffsetArray, j_next::Int, a_prime::Float64,
                    h_next::Float64, is::Int, ig::Int, iθ::Int)::Float64
    ial, iar, φ_a = asset_interp(a_prime)
    ihl, ihr, φ_h = health_interp(h_next)
    return φ_a       * φ_h       * P[j_next, ig, ial, ihl, is, iθ] +
           φ_a       * (1.0-φ_h) * P[j_next, ig, ial, ihr, is, iθ] +
           (1.0-φ_a) * φ_h       * P[j_next, ig, iar, ihl, is, iθ] +
           (1.0-φ_a) * (1.0-φ_h) * P[j_next, ig, iar, ihr, is, iθ]
end

# Expected marginal utility next period, conditional on (is_now, ig, iθ).
function expected_uc_next(j_next::Int, a_prime::Float64, h_next::Float64,
                          is_now::Int, ig::Int, iθ::Int)::Float64
    s = 0.0
    for is_p in 1:Nη
        c_p  = interp_pol(c_pol, j_next, a_prime, h_next, is_p, ig, iθ)
        ℓ_p  = interp_pol(l_pol, j_next, a_prime, h_next, is_p, ig, iθ)
        uc_p = marginal_utility_c(c_p, ℓ_p, h_next)
        s += π_η[is_now, is_p] * uc_p
    end
    return s
end

# Euler residual at the candidate (a', m). LHS−RHS in u_c units.
function euler_residual(a_prime::Float64, j::Int, ia::Int, ih::Int, is::Int,
                        ig::Int, iθ::Int, m::Float64, h_now::Float64)::Float64
    a_now = a_grid[ia]
    η_now = η_grid[is]
    ℓ_now = labor_supply(j, h_now, η_now, ig, iθ)
    c_now = consumption_from_choices(j, a_now, h_now, η_now, ig, iθ, a_prime, m)
    uc_now = marginal_utility_c(c_now, ℓ_now, h_now)

    h_nxt = health_next(h_now, m, j)
    Euc_nxt = expected_uc_next(j + 1, a_prime, h_nxt, is, ig, iθ)
    rhs = β_pref * survival(j + 1, h_nxt, ig) * (1.0 + rn[]) * Euc_nxt
    return uc_now - rhs
end

# Value at the candidate (a', m).
function value_at(a_prime::Float64, j::Int, ia::Int, ih::Int, is::Int,
                  ig::Int, iθ::Int, m::Float64, h_now::Float64)::Float64
    a_now = a_grid[ia]
    η_now = η_grid[is]
    ℓ_now = labor_supply(j, h_now, η_now, ig, iθ)
    c_now = consumption_from_choices(j, a_now, h_now, η_now, ig, iθ, a_prime, m)
    h_nxt = health_next(h_now, m, j)

    u_now = utility(c_now, ℓ_now, h_now)
    if j == J
        # ψ_{J+1} = 0 → no continuation
        return u_now
    end
    EV = 0.0
    for is_p in 1:Nη
        Vp = interp_pol(V_pol, j + 1, a_prime, h_nxt, is_p, ig, iθ)
        EV += π_η[is, is_p] * Vp
    end
    return u_now + β_pref * survival(j + 1, h_nxt, ig) * EV
end

# ─── Inline Brent root-finder for the Euler residual ─────────────────────────
# Ported from GE-Fast/ge_model_fast.jl (DraftApril's performance variant) with
# the sex index `ig` threaded through. Replaces Roots.find_zero with an
# anonymous closure, which allocated a closure + solver state per cell (the
# dominant cost). The math is identical; the inline version is deterministic —
# it always returns, so no try/catch failure path is needed.
# Pre-condition: f_lo and f_hi have opposite signs (the caller checks).
@inline function brent_aprime(a_lo::Float64, a_hi::Float64,
                              f_lo::Float64, f_hi::Float64,
                              j::Int, ia::Int, ih::Int, is::Int,
                              ig::Int, iθ::Int, m::Float64, h_now::Float64;
                              xtol::Float64 = 1e-10, ftol::Float64 = 1e-12,
                              maxiter::Int = 100)
    a  = a_lo;  b  = a_hi
    fa = f_lo;  fb = f_hi
    if abs(fa) < abs(fb)
        a, b   = b, a
        fa, fb = fb, fa
    end
    c  = a
    fc = fa
    d  = b - a
    mflag = true
    for _ in 1:maxiter
        if abs(fb) < ftol
            return b
        end
        local s::Float64
        if fa != fc && fb != fc
            s = a*fb*fc/((fa-fb)*(fa-fc)) + b*fa*fc/((fb-fa)*(fb-fc)) + c*fa*fb/((fc-fa)*(fc-fb))
        else
            s = b - fb*(b - a)/(fb - fa)
        end
        cond1 = (s - (3a + b)/4.0) * (s - b) > 0.0
        cond2 = mflag  && abs(s - b) >= abs(b - c)/2.0
        cond3 = !mflag && abs(s - b) >= abs(c - d)/2.0
        cond4 = mflag  && abs(b - c) < xtol
        cond5 = !mflag && abs(c - d) < xtol
        if cond1 || cond2 || cond3 || cond4 || cond5
            s = (a + b)/2.0
            mflag = true
        else
            mflag = false
        end
        fs = euler_residual(s, j, ia, ih, is, ig, iθ, m, h_now)
        d = c
        c = b;  fc = fb
        if fa * fs < 0.0
            b = s;  fb = fs
        else
            a = s;  fa = fs
        end
        if abs(fa) < abs(fb)
            a, b   = b, a
            fa, fb = fb, fa
        end
        if abs(b - a) < xtol
            return b
        end
    end
    return b
end

# Build the m-grid for a given cell. m=0 always included; the remaining Nm−1
# points are log-spaced from m_min to m_max = m_max_frac · X.
function build_m_grid(j::Int, ia::Int, ih::Int, is::Int, ig::Int, iθ::Int)
    a_now = a_grid[ia]
    h_now = h_grid[ih]
    η_now = η_grid[is]
    X = available_resources(a_now, h_now, η_now, ig, iθ, j)
    m_max = max(m_max_frac * X, m_min * 2.0)
    if m_max <= m_min
        return Float64[0.0]
    end
    logs = range(log(m_min), log(m_max); length = Nm - 1)
    pts = vcat(0.0, exp.(logs))
    return pts
end

# Solve for the optimal a' at a FIXED m (Euler root + Kuhn-Tucker corners).
# X is the cell's available resources (cell-constant; passed in to avoid
# recomputation). Returns (a', feasible) — feasible = false when this m leaves
# no resources for positive consumption.
function solve_aprime_given_m(j::Int, ia::Int, ih::Int, is::Int, ig::Int, iθ::Int,
                              m::Float64, h_now::Float64, X::Float64)
    avail_after_m = X - (1.0 + τm) * m
    if avail_after_m <= 0.0
        return (a_l, false)
    end
    a_hi = max(avail_after_m - 1e-6, a_l)
    if a_hi <= a_l
        return (a_l, true)
    end
    f_lo = euler_residual(a_l,  j, ia, ih, is, ig, iθ, m, h_now)
    f_hi = euler_residual(a_hi, j, ia, ih, is, ig, iθ, m, h_now)
    if f_lo * f_hi > 0.0
        # No interior root: the borrowing constraint or the upper cap binds.
        # f_lo > 0 ⇒ corner a' = a_l; f_lo < 0 ⇒ corner a' = a_hi.
        return (f_lo > 0.0 ? a_l : a_hi, true)
    end
    return (brent_aprime(a_l, a_hi, f_lo, f_hi, j, ia, ih, is, ig, iθ, m, h_now), true)
end

# Solve the household problem for one (j, ia, ih, is, ig, iθ) cell.
# Returns optimal (a', m, c, ℓ, h_next, V).
#
# Medical spending m: a grid search over the log-spaced m-grid, then (if
# `refine_m`) a parabolic refinement — a parabola is fitted through the winning
# m-node and its two neighbours and its vertex is taken as m*. This removes most
# of the m-grid discretization bias at the cost of one extra a'-solve. The
# refinement is skipped at the m = 0 corner, the node adjacent to it, and the
# grid-top cap node, where there is no safe two-sided bracket.
function solve_cell(j::Int, ia::Int, ih::Int, is::Int, ig::Int, iθ::Int)
    a_now = a_grid[ia]
    h_now = h_grid[ih]
    η_now = η_grid[is]

    if j == J
        # Terminal: a' = 0, m = 0, ℓ = 0; consume all resources.
        ℓ_term = 0.0
        c_term = consumption_from_choices(j, a_now, h_now, η_now, ig, iθ, 0.0, 0.0)
        V_term = utility(c_term, ℓ_term, h_now)
        return (0.0, 0.0, c_term, ℓ_term, h_now, V_term)
    end

    m_grid = build_m_grid(j, ia, ih, is, ig, iθ)
    nM = length(m_grid)
    X  = available_resources(a_now, h_now, η_now, ig, iθ, j)

    # ── Grid search over the m-candidates ──
    V_nodes = fill(-Inf, nM)
    best_idx = 1
    best_V = -Inf
    best_aprime = 0.0
    best_m = 0.0
    for k in 1:nM
        m_cand = m_grid[k]
        aprime_star, feasible = solve_aprime_given_m(j, ia, ih, is, ig, iθ, m_cand, h_now, X)
        feasible || continue
        V_here = value_at(aprime_star, j, ia, ih, is, ig, iθ, m_cand, h_now)
        V_nodes[k] = V_here
        if V_here > best_V
            best_V = V_here
            best_idx = k
            best_aprime = aprime_star
            best_m = m_cand
        end
    end

    # ── Parabolic refinement of m* around an interior winning node ──
    if refine_m[] && best_idx >= 3 && best_idx <= nM - 1 &&
       isfinite(V_nodes[best_idx-1]) && isfinite(V_nodes[best_idx+1])
        x1, x2, x3 = m_grid[best_idx-1], m_grid[best_idx], m_grid[best_idx+1]
        y1, y2, y3 = V_nodes[best_idx-1], V_nodes[best_idx], V_nodes[best_idx+1]
        num = (x2-x1)^2 * (y2-y3) - (x2-x3)^2 * (y2-y1)
        den = (x2-x1)   * (y2-y3) - (x2-x3)   * (y2-y1)
        if abs(den) > 1e-300
            m_ref = x2 - 0.5 * num / den
            if x1 < m_ref < x3
                aprime_ref, feasible = solve_aprime_given_m(j, ia, ih, is, ig, iθ,
                                                            m_ref, h_now, X)
                if feasible
                    V_ref = value_at(aprime_ref, j, ia, ih, is, ig, iθ, m_ref, h_now)
                    if V_ref > best_V
                        best_V = V_ref
                        best_aprime = aprime_ref
                        best_m = m_ref
                        n_refined[] += 1
                    end
                end
            end
        end
    end

    best_ℓ     = labor_supply(j, h_now, η_now, ig, iθ)
    best_c     = consumption_from_choices(j, a_now, h_now, η_now, ig, iθ, best_aprime, best_m)
    best_hnext = health_next(h_now, best_m, j)
    return (best_aprime, best_m, best_c, best_ℓ, best_hnext, best_V)
end

# Backward induction over ages for one (sex, skill) type.
function solve_household_for_type(ig::Int, iθ::Int)
    # Terminal age J first.
    for ia in 0:NA, ih in 0:NH, is in 1:Nη
        ap, m, c, ℓ, hn, V = solve_cell(J, ia, ih, is, ig, iθ)
        aplus_pol[J, ig, ia, ih, is, iθ] = ap
        m_pol[J, ig, ia, ih, is, iθ]     = m
        c_pol[J, ig, ia, ih, is, iθ]     = c
        l_pol[J, ig, ia, ih, is, iθ]     = ℓ
        hnext_pol[J, ig, ia, ih, is, iθ] = hn
        V_pol[J, ig, ia, ih, is, iθ]     = V
    end
    # Backward sweep j = J-1 down to 1.
    for j in (J-1):-1:1
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            ap, m, c, ℓ, hn, V = solve_cell(j, ia, ih, is, ig, iθ)
            aplus_pol[j, ig, ia, ih, is, iθ] = ap
            m_pol[j, ig, ia, ih, is, iθ]     = m
            c_pol[j, ig, ia, ih, is, iθ]     = c
            l_pol[j, ig, ia, ih, is, iθ]     = ℓ
            hnext_pol[j, ig, ia, ih, is, iθ] = hn
            V_pol[j, ig, ia, ih, is, iθ]     = V
        end
    end
end

# Driver for all four (sex, skill) types.
function solve_household(; verbose::Bool=false)
    n_refined[] = 0
    for iθ in 1:Nθ, ig in 1:Ng
        if verbose
            sexname = ig == 1 ? "male  " : "female"
            @printf "Solving household for (%s, skill %d, θ = %+.3f)\n" sexname iθ θ_grid[iθ]
            flush(stdout)
        end
        solve_household_for_type(ig, iθ)
    end
end

# ─── Ergodic distribution of the AR(1) η-grid by power iteration ─────────────
function compute_ergodic!()
    p = fill(1.0 / Nη, Nη)
    pn = similar(p)
    for _ in 1:5000
        fill!(pn, 0.0)
        for is in 1:Nη, is_p in 1:Nη
            pn[is_p] += p[is] * π_η[is, is_p]
        end
        if maximum(abs.(pn .- p)) < 1e-12
            copyto!(p, pn)
            break
        end
        copyto!(p, pn)
    end
    copyto!(π_η_erg, p)
end

# ─── Forward distribution simulation ─────────────────────────────────────────
# Tracks the joint distribution Φ_j(g, a, h, η, θ) over (j, ig, ia, ih, is, iθ).
# Initial (a=0, h=h_init) degenerate; η drawn from the ergodic distribution.
const Φ = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)

function forward_distribution!()
    Φ .= 0.0
    # Initial mass at (a=0, h=h_init, η ~ ergodic) for each (sex, skill) type.
    ih_init_l, ih_init_r, φh_init = health_interp(h_init)
    for iθ in 1:Nθ, ig in 1:Ng, is in 1:Nη
        Φ[1, ig, 0, ih_init_l, is, iθ] += π_birth[ig, iθ] * π_η_erg[is] * φh_init
        Φ[1, ig, 0, ih_init_r, is, iθ] += π_birth[ig, iθ] * π_η_erg[is] * (1.0 - φh_init)
    end

    # Forward iteration j = 1, ..., J-1.
    for j in 1:(J-1)
        for ia in 0:NA, ih in 0:NH, is in 1:Nη, ig in 1:Ng, iθ in 1:Nθ
            mass = Φ[j, ig, ia, ih, is, iθ]
            if mass < 1e-18
                continue
            end
            a_prime = aplus_pol[j, ig, ia, ih, is, iθ]
            h_n     = hnext_pol[j, ig, ia, ih, is, iθ]
            ial, iar, φ_a = asset_interp(a_prime)
            ihl, ihr, φ_h = health_interp(h_n)

            ψ_next = survival(j + 1, h_n, ig)   # sex-specific survival
            mass_alive = mass * ψ_next          # PE: death share leaves the system
            for is_p in 1:Nη
                πη = π_η[is, is_p]
                Φ[j+1, ig, ial, ihl, is_p, iθ] += mass_alive * πη * φ_a       * φ_h
                Φ[j+1, ig, ial, ihr, is_p, iθ] += mass_alive * πη * φ_a       * (1.0 - φ_h)
                Φ[j+1, ig, iar, ihl, is_p, iθ] += mass_alive * πη * (1.0 - φ_a) * φ_h
                Φ[j+1, ig, iar, ihr, is_p, iθ] += mass_alive * πη * (1.0 - φ_a) * (1.0 - φ_h)
            end
        end
    end
end

# ─── Diagnostics ─────────────────────────────────────────────────────────────

# Fraction of mass at each (age, sex, skill) with m* > 0.
function m_positivity_by_age()
    out = zeros(J, Ng, Nθ)
    for j in 1:J, ig in 1:Ng, iθ in 1:Nθ
        mass_total = 0.0
        mass_pos = 0.0
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            w = Φ[j, ig, ia, ih, is, iθ]
            mass_total += w
            if m_pol[j, ig, ia, ih, is, iθ] > m_min * 1.0001
                mass_pos += w
            end
        end
        out[j, ig, iθ] = mass_total > 0.0 ? mass_pos / mass_total : 0.0
    end
    return out
end

# Cohort means weighted by Φ, indexed [j, ig, iθ].
function cohort_means()
    cm_c = zeros(J, Ng, Nθ)
    cm_l = zeros(J, Ng, Nθ)
    cm_a = zeros(J, Ng, Nθ)
    cm_m = zeros(J, Ng, Nθ)
    cm_h = zeros(J, Ng, Nθ)
    for j in 1:J, ig in 1:Ng, iθ in 1:Nθ
        wsum = 0.0
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            w = Φ[j, ig, ia, ih, is, iθ]
            if w < 1e-18; continue; end
            wsum += w
            cm_c[j, ig, iθ] += w * c_pol[j, ig, ia, ih, is, iθ]
            cm_l[j, ig, iθ] += w * l_pol[j, ig, ia, ih, is, iθ]
            cm_a[j, ig, iθ] += w * a_grid[ia]
            cm_m[j, ig, iθ] += w * m_pol[j, ig, ia, ih, is, iθ]
            cm_h[j, ig, iθ] += w * h_grid[ih]
        end
        if wsum > 0.0
            cm_c[j, ig, iθ] /= wsum
            cm_l[j, ig, iθ] /= wsum
            cm_a[j, ig, iθ] /= wsum
            cm_m[j, ig, iθ] /= wsum
            cm_h[j, ig, iθ] /= wsum
        end
    end
    return cm_c, cm_l, cm_a, cm_m, cm_h
end

# Detect whether the saved policy at (j, ig, ia, ih, is, iθ) is a corner choice.
function is_corner_cell(j::Int, ia::Int, ih::Int, is::Int, ig::Int, iθ::Int)::Bool
    ap = aplus_pol[j, ig, ia, ih, is, iθ]
    if ap <= a_l + 1e-9
        return true
    end
    a_now = a_grid[ia]; h_now = h_grid[ih]; η_now = η_grid[is]
    m_chosen = m_pol[j, ig, ia, ih, is, iθ]
    X = available_resources(a_now, h_now, η_now, ig, iθ, j)
    avail_after_m = X - (1.0 + τm) * m_chosen
    a_hi = max(avail_after_m - 1e-6, a_l)
    return ap >= a_hi - 1e-6
end

# Euler residual statistics across interior cells only (excludes corners).
function euler_residual_stats()
    residuals = Float64[]
    for j in 1:(J-1), ig in 1:Ng, iθ in 1:Nθ
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            if is_corner_cell(j, ia, ih, is, ig, iθ)
                continue
            end
            ap = aplus_pol[j, ig, ia, ih, is, iθ]
            mm = m_pol[j, ig, ia, ih, is, iθ]
            h_now = h_grid[ih]
            r = euler_residual(ap, j, ia, ih, is, ig, iθ, mm, h_now)
            c_now = c_pol[j, ig, ia, ih, is, iθ]
            ℓ_now = l_pol[j, ig, ia, ih, is, iθ]
            uc = marginal_utility_c(c_now, ℓ_now, h_now)
            if uc > 1e-12
                push!(residuals, abs(r) / uc)
            end
        end
    end
    return residuals
end

# Cohort-share invariant: φ_{j+1}/φ_j vs ψ̄_{j+1}/(1+n_p), per (sex, skill).
# (n_p does not appear in PE forward_distribution!, so the audit gate here is
#  φ_{j+1}/φ_j == ψ̄_{j+1}; ψ̄ is the mass-weighted survival into age j+1.)
function cohort_share_invariant()
    max_dev = 0.0
    for ig in 1:Ng, iθ in 1:Nθ
        for j in 1:(J-1)
            φj  = sum(Φ[j,   ig, :, :, :, iθ])
            φj1 = sum(Φ[j+1, ig, :, :, :, iθ])
            if φj < 1e-18; continue; end
            # Mass-weighted survival ψ̄_{j+1} implied by the policies at age j.
            ψbar_num = 0.0
            for ia in 0:NA, ih in 0:NH, is in 1:Nη
                w = Φ[j, ig, ia, ih, is, iθ]
                if w < 1e-18; continue; end
                h_n = hnext_pol[j, ig, ia, ih, is, iθ]
                ψbar_num += w * survival(j + 1, h_n, ig)
            end
            ψbar = ψbar_num / φj
            max_dev = max(max_dev, abs(φj1 / φj - ψbar))
        end
    end
    return max_dev
end

# A small CSV-writer kept for the parity smoke test; the SMM loop does NOT
# call this. Output filename matches Household-Gender's so they can be diffed.
function write_parity_csv(out_dir::String; suffix::String="_fromsmm")
    cm_c, cm_l, cm_a, cm_m, cm_h = cohort_means()
    pos = m_positivity_by_age()
    open(joinpath(out_dir, "household_lifecycle$(suffix).csv"), "w") do io
        println(io, "age_period,sex_idx,theta_idx,theta_value,c,l,a,m,h,m_positive_share")
        for j in 1:J, ig in 1:Ng, iθ in 1:Nθ
            println(io, "$j,$ig,$iθ,$(θ_grid[iθ]),$(cm_c[j,ig,iθ]),$(cm_l[j,ig,iθ]),$(cm_a[j,ig,iθ]),$(cm_m[j,ig,iθ]),$(cm_h[j,ig,iθ]),$(pos[j,ig,iθ])")
        end
    end
end

# ─── Audit-gate diagnostics ──────────────────────────────────────────────────
# Returns a NamedTuple of metrics; optionally prints them and/or asserts the
# hard gates. SMM hot path: `assert_gates=false, verbose=false`.
# Parity smoke test: `assert_gates=true, verbose=true`.
# Two-sex identity is informational only here — the CSV-driven first-step
# inputs can be asymmetric, so an asymmetric solve is correct behavior.
function diagnostic_gates(; assert_gates::Bool=false, verbose::Bool=true)
    if verbose
        println("\n─── Diagnostic gates ────────────────────────────────────────")
    end

    # Per-cell scan.
    max_budget = 0.0
    min_c = Inf
    n_c_floor = 0
    max_aprime = 0.0
    min_aprime = Inf
    min_hnext = Inf
    max_hnext = -Inf
    n_hnext_below = 0
    m_at_top_mass = 0.0
    scan_mass = 0.0
    max_m_ratio = 0.0
    for j in 1:J, ig in 1:Ng, ia in 0:NA, ih in 0:NH, is in 1:Nη, iθ in 1:Nθ
        a_now = a_grid[ia]; h_now = h_grid[ih]; η_now = η_grid[is]
        cc = c_pol[j,ig,ia,ih,is,iθ]
        mm = m_pol[j,ig,ia,ih,is,iθ]
        ap = aplus_pol[j,ig,ia,ih,is,iθ]
        hn = hnext_pol[j,ig,ia,ih,is,iθ]
        X  = available_resources(a_now, h_now, η_now, ig, iθ, j)
        max_budget = max(max_budget, abs((1.0+τc)*cc + (1.0+τm)*mm + ap - X))
        min_c = min(min_c, cc)
        cc <= 1e-9 && (n_c_floor += 1)
        max_aprime = max(max_aprime, ap); min_aprime = min(min_aprime, ap)
        min_hnext = min(min_hnext, hn);   max_hnext = max(max_hnext, hn)
        hn < h_l && (n_hnext_below += 1)
        m_top = max(m_max_frac * X, m_min * 2.0)
        w = Φ[j,ig,ia,ih,is,iθ]
        scan_mass += w
        mm >= 0.999 * m_top && (m_at_top_mass += w)
        max_m_ratio = max(max_m_ratio, mm / m_top)
    end

    min_Φ = minimum(Φ)
    all_finite_Φ = all(isfinite, Φ)
    newborn_mass = sum(Φ[1, :, :, :, :, :])
    top_share = sum(Φ[:, :, NA, :, :, :]) / sum(Φ)

    term = max(maximum(abs.(aplus_pol[J,:,:,:,:,:])),
               maximum(abs.(m_pol[J,:,:,:,:,:])),
               maximum(abs.(l_pol[J,:,:,:,:,:])))

    res = euler_residual_stats()
    euler_max = isempty(res) ? -Inf : maximum(log10.(max.(res, 1e-16)))

    max_sex = 0.0
    for j in 1:J, ia in 0:NA, ih in 0:NH, is in 1:Nη, iθ in 1:Nθ
        max_sex = max(max_sex,
            abs(c_pol[j,1,ia,ih,is,iθ]     - c_pol[j,2,ia,ih,is,iθ]),
            abs(aplus_pol[j,1,ia,ih,is,iθ] - aplus_pol[j,2,ia,ih,is,iθ]),
            abs(V_pol[j,1,ia,ih,is,iθ]     - V_pol[j,2,ia,ih,is,iθ]))
    end
    cs_inv = cohort_share_invariant()

    mono_viol = 0.0
    for j in 1:(J-1), ig in 1:Ng, ih in 0:NH, is in 1:Nη, iθ in 1:Nθ, ia in 0:(NA-1)
        mono_viol = min(mono_viol,
            aplus_pol[j,ig,ia+1,ih,is,iθ] - aplus_pol[j,ig,ia,ih,is,iθ])
    end

    if verbose
        @printf "  budget residual      max = %.3e   (gate < 1e-8)\n" max_budget
        @printf "  consumption          min = %.3e   floored cells = %d\n" min_c n_c_floor
        @printf "  savings a'           min = %.3e   max = %.3e\n" min_aprime max_aprime
        @printf "  distribution Φ       min = %.3e   all finite = %s\n" min_Φ all_finite_Φ
        @printf "  newborn mass ΣΦ[1]       = %.12f   (gate ≈ 1)\n" newborn_mass
        @printf "  asset-top mass share     = %.3e   (gate < 1e-3)\n" top_share
        @printf "  terminal |a',m,ℓ| at j=J = %.3e   (gate = 0)\n" term
        @printf "  Euler residual log10 max = %.3f       (gate < -3)\n" euler_max
        @printf "  two-sex max |male-female|= %.3e   (soft: first-step CSVs drive any asymmetry)\n" max_sex
        @printf "  cohort-share invariant   = %.3e   (gate < 1e-8)\n" cs_inv
        @printf "  health h' range          = [%.4f, %.4f]   below-h_l cells = %d (soft)\n" min_hnext max_hnext n_hnext_below
        @printf "  medical m* at grid top   = %.3f%% of mass   max m*/m_max = %.4f (soft)\n" (100.0*m_at_top_mass/scan_mass) max_m_ratio
        @printf "  m* parabolic refinement  = %d cells refined   (refine_m = %s)\n" n_refined[] refine_m[]
        @printf "  a' monotonicity worst Δ  = %.3e   (soft: ≥ 0 ideal)\n" mono_viol
    end

    if assert_gates
        @assert max_budget < 1e-8                          "budget residual exceeds 1e-8"
        @assert n_c_floor == 0                             "consumption hit the 1e-12 floor"
        @assert min_c > 0.0                                "non-positive consumption"
        @assert min_aprime >= a_l - 1e-9                   "savings below the borrowing constraint"
        @assert min_Φ >= -1e-14                            "negative mass in the distribution"
        @assert all_finite_Φ                               "non-finite mass in the distribution"
        @assert isapprox(newborn_mass, 1.0; atol = 1e-12)  "newborn cohort mass ≠ 1"
        @assert top_share < 1e-3                           "mass piles up at a_max — grid too small"
        @assert term == 0.0                                "terminal condition a'=m=ℓ=0 violated"
        @assert euler_max < -3.0                           "Euler residual above the -3 gate"
        @assert cs_inv < 1e-8                              "cohort-share invariant violated"
        @assert min_hnext >= 0.0                           "negative next-period health"
        @assert max_hnext <= h_u + 1e-9                    "next-period health exceeds h̄"
        verbose && println("  ✔ all hard gates passed")
    end

    return (; max_budget, min_c, n_c_floor, min_aprime, max_aprime,
            min_Φ, all_finite_Φ, newborn_mass, top_share, term,
            euler_max, max_sex, cs_inv, min_hnext, max_hnext,
            n_hnext_below, m_at_top_mass, scan_mass, max_m_ratio,
            mono_viol, n_refined=n_refined[])
end

# ─── SMM entry points ────────────────────────────────────────────────────────

"""
    apply_first_step!(fs)

Populate first-step inputs from `fs`, a NamedTuple produced by
`load_inputs.jl`. Required fields:
    fs.e_age   (Ng × J)         fs.ψ_base  (Ng × J)
    fs.δh      (J)              fs.π_birth (Ng × Nθ)
    fs.θ_grid  (Nθ)             fs.ϱ_pen   (Nθ)
    fs.ρ       (Float64)        fs.σ_ε     (Float64)

Side effect: rewrites the module's mutable arrays + Refs, rebuilds the η-grid
via Rouwenhorst, and refreshes the ergodic distribution.
"""
function apply_first_step!(fs)
    @assert size(fs.e_age)   == (Ng, J)  "fs.e_age must be $(Ng)×$(J)"
    @assert size(fs.ψ_base)  == (Ng, J)  "fs.ψ_base must be $(Ng)×$(J)"
    @assert length(fs.δh)    == J        "fs.δh must have length $(J)"
    @assert size(fs.π_birth) == (Ng, Nθ) "fs.π_birth must be $(Ng)×$(Nθ)"
    @assert length(fs.θ_grid) == Nθ      "fs.θ_grid must have length $(Nθ)"
    @assert length(fs.ϱ_pen) == Nθ       "fs.ϱ_pen must have length $(Nθ)"
    copyto!(e_age,   fs.e_age)
    copyto!(ψ_base,  fs.ψ_base)
    copyto!(δh,      fs.δh)
    copyto!(π_birth, fs.π_birth)
    copyto!(θ_grid,  fs.θ_grid)
    copyto!(ϱ_pen,   fs.ϱ_pen)
    ρ_AR[] = fs.ρ
    σ_ε[]  = fs.σ_ε
    π_mat, η_vec = rouwenhorst(Nη, ρ_AR[], σ_ε[], 0.0)
    π_η .= π_mat
    η_grid .= η_vec
    compute_ergodic!()
    return nothing
end

"""
    apply_anchor!(an)

Write the four fixed-price anchors from a NamedTuple `an`. Required fields
`an.r, an.w, an.τp, an.pen`. Also refreshes `rn[] = an.r·(1-τk)`.
"""
function apply_anchor!(an)
    r_price[]  = an.r
    w_price[]  = an.w
    τp[]       = an.τp
    pen_flow[] = an.pen
    rn[]       = an.r * (1.0 - τk)
    return nothing
end

"""
    apply_theta!(θ)

Write the 6 SMM parameters from a NamedTuple `θ`. Required fields
`θ.Ψ, θ.Ξ, θ.ξ, θ.H_0, θ.h_slope, θ.ζ_h`.
"""
function apply_theta!(θ)
    Ψ_labor[]   = θ.Ψ
    Ξ_amenity[] = θ.Ξ
    ξ_curv[]    = θ.ξ
    H_scale[]   = θ.H_0
    h_slope[]   = θ.h_slope
    H_curv[]    = θ.ζ_h
    return nothing
end

"""
    init_grids!(; refine_m_flag::Bool=true)

One-time grid initialization: a_grid and h_grid. Call once at startup, not
per SMM trial. (η-grid is rebuilt by `apply_first_step!`.) The `refine_m_flag`
keyword globally toggles m* parabolic refinement.
"""
function init_grids!(; refine_m_flag::Bool=true)
    grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
    grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
    refine_m[] = refine_m_flag
    return nothing
end

"""
    solve_pe_at!(θ, anchor, first_step; verify=false, verbose=false)

Apply (θ, anchor, first_step), solve the PE household problem and the
forward distribution, and return a NamedTuple of the policy arrays plus Φ
and the η machinery. SMM hot path uses `verify=false`; the parity smoke
test uses `verify=true`.
"""
function solve_pe_at!(θ, anchor, first_step;
                       verify::Bool=false, verbose::Bool=false)
    apply_first_step!(first_step)
    apply_anchor!(anchor)
    apply_theta!(θ)
    solve_household(; verbose=verbose)
    forward_distribution!()
    if verify
        diagnostic_gates(assert_gates=true, verbose=verbose)
    end
    return (; V_pol, c_pol, l_pol, m_pol, aplus_pol, hnext_pol, Φ,
            π_η_erg, η_grid, π_η)
end
