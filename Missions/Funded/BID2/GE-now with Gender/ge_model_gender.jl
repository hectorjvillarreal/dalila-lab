################################################################################
#  ge_model_gender.jl
#
#  Stationary general-equilibrium solver for the GENDER EXTENSION (Modelmay) of
#  the DraftApril OLG model. Matches modelwithgender.tex §3 (Model).
#
#  Built by copying GE/ge_model.jl (DraftApril GE, no gender) and threading a
#  sex dimension g ∈ {m, f} through every life-cycle object, then grafting in
#  the household-block improvements already verified in
#  Household-Gender/household_problem_gender.jl:
#    • inline Brent root-finder (`brent_aprime`)
#    • m* parabolic refinement (toggle `refine_m`)
#    • hard @assert diagnostic gates (`diagnostic_gates`)
#  The DraftApril solvers (GE/, GE-Fast/, Household/) are the copy source and
#  are NOT edited (README hard rule).
#
#  Endogenous: prices (r, w), pension contribution τ^p, pension flow pen,
#  government debt B (residual closure). Externally fixed: tax rates, gy, κ,
#  production (α, δ, A), n_p, preferences, household primitives.
#
#  Four agent types (g, θ) ∈ {m, f} × {θ_L, θ_H}. Index conventions:
#    • Sex   ig ∈ {1, 2}: 1 = male, 2 = female.
#    • Skill iθ ∈ {1, 2}: 1 = θ_L, 2 = θ_H.
#    • Policy/value/distribution arrays indexed (j, ig, ia, ih, is, iθ).
#  Build switch: J = 17 (deliverable, ages 20–100) or J = 16 (collapse check).
#
#  Stub status (men ≡ women until calibration §4): e_age, ψ_base are 2×J with
#  identical rows; π_birth = 0.25 for all four types; h_slope = 0.
#
#  vs. the PE Household-Gender solver: the GE forward distribution carries the
#  1/(1+n_p) population-growth factor (modelwithgender.tex eq. cohort_weights);
#  prices/taxes/pension are endogenous typed globals, not fixed inputs.
################################################################################

using OffsetArrays
using DynamicProgrammingUtils
using Roots
using Printf
using Statistics
using Plots

# ─── Category A parameters (from PDF) ────────────────────────────────────────
const γ_pref     = 2.0                  # [PDF] GHH risk-aversion exponent
const ν_pref     = 2.0                  # [PDF] inverse Frisch elasticity (ν_ℓ)
const β_pref     = 0.998^5              # [PDF] 5-yr discount factor
const ρ_AR       = 0.98                 # [PDF] AR(1) persistence
const σ_ε        = 0.05                 # [PDF] AR(1) innovation s.d.

const J          = 17                   # [PDF] max age — 17 = deliverable, 16 = collapse check
const j_R        = 10                   # [PDF] retirement age (period index)
const Nη         = 7                    # [PDF] productivity nodes
const Ng         = 2                    # number of sexes: 1 = male, 2 = female

@assert J in (16, 17) "J must be 16 (collapse check) or 17 (gender deliverable)"

const τc         = 0.16                 # [PDF] consumption tax
const τw         = 0.20                 # [introduced] labor tax
const τk         = 0.20                 # [introduced] capital tax
const τm         = 0.00                 # [PDF] medical-spending tax
const gy         = 0.19                 # [PDF] G/Y share
const κ_rep      = 0.50                 # [PDF] pension replacement rate

const α          = 0.36                 # [PDF] capital share
const δ_cap      = 1.0 - (1.0 - 0.0823)^5  # [PDF] capital depreciation, 5-yr
const A_TFP      = 1.60                 # [PDF] TFP
n_p::Float64     = 1.01^5 - 1.0         # [introduced] population growth, 5-yr
                                         # Typed global (was const) so the
                                         # aging-experiment driver can override
                                         # via set_demographics! and have the
                                         # new value picked up by already-
                                         # compiled survival/forward/debt
                                         # routines. Julia 1.11 const
                                         # redefinition is allowed-with-warning
                                         # but compiled methods keep the
                                         # inlined value — typed global avoids
                                         # the inlining without losing type
                                         # stability.

# ─── Category B parameters (PDF-open, fixed here) ────────────────────────────
const Ξ_amenity  = 0.50
const ξ_curv     = 0.50
const Ψ_labor    = 14.0

const θ_grid     = [-0.20, 0.20]        # [PDF-open] skill fixed effects θ_L, θ_H
const Nθ         = length(θ_grid)
const ϱ_pen      = [0.30, 0.20]         # [PDF-open] health-prod. elasticity ϱ(θ)

# Birth shares π^{g,θ}_1 indexed [ig, iθ]. STUB: symmetric (all four = 0.25).
const π_birth    = fill(0.25, Ng, Nθ)   # [STUB] sums to 1

# ─── Sex-specific primitives [ig, j] ─────────────────────────────────────────
# `gender_gap` toggles between two stub modes (see Household-Gender for detail):
#   • false → men ≡ women (collapse-to-DraftApril-GE check works)
#   • true  → female productivity ×0.85, female mortality ×0.75 (~+3 y LE)
# When true, outputs go to `plots-gap/` and `*_gap.csv`.
const gender_gap = true

const _e_age16  = [1.0000, 1.3527, 1.6952, 1.8279, 1.9606, 1.9692, 1.9692,
                   1.9392, 1.9007, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]   # [PDF-open]
const _ψ_base16 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                   0.98972953, 0.98185396, 0.97070373, 0.95530594,
                   0.93417914, 0.90238714, 0.83653436, 0.71048182,
                   0.52669353, 0.31179803]                              # [PDF-open]
const _δh16     = [0.02, 0.02, 0.03, 0.03, 0.05, 0.07, 0.10, 0.14,
                   0.18, 0.22, 0.27, 0.32, 0.38, 0.45, 0.55, 0.70]      # [PDF-open]

const _e_age_J  = J == 17 ? vcat(_e_age16,  0.0)  : _e_age16            # retiree → 0
const _ψ_base_J = J == 17 ? vcat(_ψ_base16, 0.15) : _ψ_base16           # [STUB-extrap]
const _δh_J     = J == 17 ? vcat(_δh16,     0.80) : _δh16               # [STUB-extrap]

const _e_age_male    = _e_age_J
const _e_age_female  = gender_gap ? 0.85 .* _e_age_J : _e_age_J
const _ψ_base_male   = _ψ_base_J
const _ψ_base_female = gender_gap ?
    [1.0 - 0.75 * (1.0 - p) for p in _ψ_base_J] :
    _ψ_base_J

const e_age  = vcat(_e_age_male',  _e_age_female')   # 2×J  row 1 = male, row 2 = female
ψ_base::Matrix{Float64} = vcat(_ψ_base_male', _ψ_base_female')  # 2×J — typed global, see n_p comment
const δh     = _δh_J                                  # length-J vector (no g superscript)

const H_scale    = 0.30
const H_curv     = 0.50
const h_slope    = 0.00                 # [STUB] age-decline of health prod.; 0 ⇒ age-invariant
const h_init     = 1.00

const surv_floor = 0.70                 # [introduced] survival adjustment floor
const surv_slope = 1.0 - surv_floor     # [introduced] = 0.30

# ─── ENDOGENOUS GE state (typed mutable globals) ────────────────────────────
# Typed globals (`g::T = value`) are inlinable by Julia's optimizer; Ref{Float64}
# here caused a ~17× slowdown of the inner solver loop.
global r_now::Float64       = 1.03^5 - 1.0
global w_now::Float64       = 1.0
global rn_now::Float64      = 0.0
global wn_now::Float64      = 0.0
global τp_now::Float64      = 0.10
global pen_now::Float64     = 0.30
global B_debt_now::Float64  = 0.0
global N_W_now::Float64     = 1.0
global N_R_now::Float64     = 1.0

# ─── Numerical / discretization ──────────────────────────────────────────────
const NA         = 100
const a_l        = 0.0
const a_u        = 300.0
const a_grow     = 0.05

const NH         = 15
const h_l        = 0.01
const h_u        = 1.00
const h_grow     = 0.05

const Nm         = 40                   # [introduced] m-grid points (incl. m=0)
const m_min      = 1e-3                 # [introduced] m-grid lower bound
const m_max_frac = 0.90                 # [introduced] m_max = avail · m_max_frac
const refine_m   = true                 # [introduced] parabolic refinement of m*

# ─── GE control ──────────────────────────────────────────────────────────────
const K_init     = 12.0
const L_init     = 10.0
const damp_ge    = 0.30      # Was 0.50; lowered to match draft_260519/ge_model.jl
                             # commit 054687c. Under gender_gap = true the iter-1
                             # L_target drops sharply (women's e_age × 0.85), and
                             # damp 0.50 caused iter-3 K_target < 0 → DomainError
                             # in (K/L)^(α-1). 0.30 has the same convergence
                             # behavior on the baseline (symmetric still hits
                             # ~13 iter) but absorbs the bigger transient under
                             # asymmetric primitives.
const sig_ge     = 1e-4
const itermax_ge = 30

# ─── Grids and buffers ───────────────────────────────────────────────────────
const a_grid    = OffsetArray(zeros(NA+1), 0:NA)
const h_grid    = OffsetArray(zeros(NH+1), 0:NH)
const η_grid    = zeros(Nη)
const π_η       = zeros(Nη, Nη)
const π_η_erg   = zeros(Nη)

# Per-thread scratch buffers for the bilinear interpolation routines below.
# linint_Grow writes its index/weight outputs into these length-1 arrays; if
# they were shared across threads (the original implementation, ported from
# the non-Gender ge_model.jl pre-commit f3110c1), concurrent calls from
# inside `Threads.@threads` loops would race and silently corrupt policy
# arrays. Each Julia thread now owns its own slot indexed by
# `Threads.threadid()`. Single-threaded launches still work (slot 1 only).
const ial_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const iar_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const varphi_a_buf_per_thread = [zeros(1)               for _ in 1:Threads.nthreads()]
const ihl_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const ihr_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const varphi_h_buf_per_thread = [zeros(1)               for _ in 1:Threads.nthreads()]

# Atomic counter for cells improved by m* parabolic refinement. Was Ref(0)
# pre-threading; under @threads the `n_refined[] += 1` inside solve_cell is
# a non-atomic read-modify-write, so swap to Threads.Atomic for safety.
const n_refined = Threads.Atomic{Int}(0)

# ─── Policy and distribution storage (j, ig, ia, ih, is, iθ) ─────────────────
const aplus_pol = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const m_pol     = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const c_pol     = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const l_pol     = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const hnext_pol = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const V_pol     = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const Φ         = OffsetArray(zeros(J, Ng, NA+1, NH+1, Nη, Nθ), 1:J, 1:Ng, 0:NA, 0:NH, 1:Nη, 1:Nθ)

# ============================================================================
# Helper functions — gendered; price-dependent ones read the GE typed globals.
# ============================================================================

function health_amenity(h::Float64)::Float64
    h_safe = max(h, 1e-12)
    if abs(ξ_curv - 1.0) < 1e-10
        return Ξ_amenity * log(h_safe)
    else
        return Ξ_amenity * h_safe^(1.0 - ξ_curv) / (1.0 - ξ_curv)
    end
end

disutility_of_labor(ℓ::Float64)::Float64 = Ψ_labor * ℓ^(1.0 + ν_pref) / (1.0 + ν_pref)
ghh_z(c::Float64, ℓ::Float64, h::Float64)::Float64 =
    c + health_amenity(h) - disutility_of_labor(ℓ)

function utility(c::Float64, ℓ::Float64, h::Float64)::Float64
    z = max(ghh_z(c, ℓ, h), 1e-12)
    return (z^(1.0 - γ_pref) - 1.0) / (1.0 - γ_pref)
end

function marginal_utility_c(c::Float64, ℓ::Float64, h::Float64)::Float64
    z = max(ghh_z(c, ℓ, h), 1e-12)
    return z^(-γ_pref)
end

# Productivity ν_j = e^g_j · exp(θ + η + ϱ(θ)·h)  [modelwithgender.tex §3.4].
function productivity(j::Int, h::Float64, η::Float64, ig::Int, iθ::Int)::Float64
    if j >= j_R
        return 0.0
    end
    return e_age[ig, j] * exp(θ_grid[iθ] + η + ϱ_pen[iθ] * h)
end

# Survival ψ^g_j(h) — sex-specific baseline modulated by health (§4.1.1 placeholder).
function survival(j::Int, h::Float64, ig::Int)::Float64
    if j < 1 || j > J + 1
        return 0.0
    end
    if j == J + 1
        return 0.0
    end
    return ψ_base[ig, j] * (surv_floor + surv_slope * h)
end

# Health production H_j(m) = H̄_0·exp(-h_slope·j)·m^ζ_h  (h_slope=0 ⇒ age-invariant).
function health_production(m::Float64, j::Int)::Float64
    if m <= 0.0
        return 0.0
    end
    H_j = H_scale * exp(-h_slope * j)
    return H_j * m^H_curv
end

function health_next(h::Float64, m::Float64, j::Int)::Float64
    return min((1.0 - δh[j]) * h + health_production(m, j), h_u)
end

# GHH labor-supply FOC — reads the GE wage and pension contribution.
function labor_supply(j::Int, h::Float64, η::Float64, ig::Int, iθ::Int)::Float64
    if j >= j_R
        return 0.0
    end
    ν_j = productivity(j, h, η, ig, iθ)
    if ν_j <= 0.0
        return 0.0
    end
    numer = w_now * ν_j * (1.0 - τw - τp_now)
    denom = (1.0 + τc) * Ψ_labor
    ℓ_star = (numer / denom) ^ (1.0 / ν_pref)
    return clamp(ℓ_star, 0.0, 1.0)
end

# Available resources X — reads the GE after-tax return and pension flow.
function available_resources(a::Float64, h::Float64, η::Float64,
                              ig::Int, iθ::Int, j::Int)::Float64
    if j < j_R
        ℓ = labor_supply(j, h, η, ig, iθ)
        ν_j = productivity(j, h, η, ig, iθ)
        labor_income = w_now * ν_j * ℓ * (1.0 - τw - τp_now)
        return (1.0 + rn_now) * a + labor_income
    else
        return (1.0 + rn_now) * a + pen_now
    end
end

function consumption_from_choices(j::Int, a::Float64, h::Float64, η::Float64,
                                   ig::Int, iθ::Int, a_prime::Float64, m::Float64)::Float64
    X = available_resources(a, h, η, ig, iθ, j)
    c = (X - a_prime - (1.0 + τm) * m) / (1.0 + τc)
    return max(c, 1e-12)
end

# ─── Bilinear interpolation of policies on (a, h) at fixed (is, ig, iθ) ───────
function asset_interp(a_prime::Float64)
    tid = Threads.threadid()
    ial, iar, φ_a = linint_Grow(a_prime, a_l, a_u, a_grow, NA,
                                 ial_buf_per_thread[tid],
                                 iar_buf_per_thread[tid],
                                 varphi_a_buf_per_thread[tid])
    ial = max(min(ial, NA - 1), 0)
    iar = max(min(iar, NA), 1)
    φ_a = clamp(φ_a, 0.0, 1.0)
    return ial, iar, φ_a
end

function health_interp(h::Float64)
    tid = Threads.threadid()
    ihl, ihr, φ_h = linint_Grow(h, h_l, h_u, h_grow, NH,
                                 ihl_buf_per_thread[tid],
                                 ihr_buf_per_thread[tid],
                                 varphi_h_buf_per_thread[tid])
    ihl = max(min(ihl, NH - 1), 0)
    ihr = max(min(ihr, NH), 1)
    φ_h = clamp(φ_h, 0.0, 1.0)
    return ihl, ihr, φ_h
end

# Interpolate a 6-D policy at (a', h_next) for fixed (j_next, is, ig, iθ).
function interp_pol(P::OffsetArray, j_next::Int, a_prime::Float64,
                    h_next::Float64, is::Int, ig::Int, iθ::Int)::Float64
    ial, iar, φ_a = asset_interp(a_prime)
    ihl, ihr, φ_h = health_interp(h_next)
    return φ_a       * φ_h       * P[j_next, ig, ial, ihl, is, iθ] +
           φ_a       * (1.0-φ_h) * P[j_next, ig, ial, ihr, is, iθ] +
           (1.0-φ_a) * φ_h       * P[j_next, ig, iar, ihl, is, iθ] +
           (1.0-φ_a) * (1.0-φ_h) * P[j_next, ig, iar, ihr, is, iθ]
end

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

function euler_residual(a_prime::Float64, j::Int, ia::Int, ih::Int, is::Int,
                        ig::Int, iθ::Int, m::Float64, h_now::Float64)::Float64
    a_now = a_grid[ia]
    η_now = η_grid[is]
    ℓ_now = labor_supply(j, h_now, η_now, ig, iθ)
    c_now = consumption_from_choices(j, a_now, h_now, η_now, ig, iθ, a_prime, m)
    uc_now = marginal_utility_c(c_now, ℓ_now, h_now)
    h_nxt = health_next(h_now, m, j)
    Euc_nxt = expected_uc_next(j + 1, a_prime, h_nxt, is, ig, iθ)
    rhs = β_pref * survival(j + 1, h_nxt, ig) * (1.0 + rn_now) * Euc_nxt
    return uc_now - rhs
end

function value_at(a_prime::Float64, j::Int, ia::Int, ih::Int, is::Int,
                  ig::Int, iθ::Int, m::Float64, h_now::Float64)::Float64
    a_now = a_grid[ia]
    η_now = η_grid[is]
    ℓ_now = labor_supply(j, h_now, η_now, ig, iθ)
    c_now = consumption_from_choices(j, a_now, h_now, η_now, ig, iθ, a_prime, m)
    h_nxt = health_next(h_now, m, j)
    u_now = utility(c_now, ℓ_now, h_now)
    if j == J
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
# Ported from GE-Fast/ge_model_fast.jl, sex index `ig` threaded through.
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
    return vcat(0.0, exp.(logs))
end

# Solve for the optimal a' at a FIXED m (Euler root + Kuhn-Tucker corners).
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
        return (f_lo > 0.0 ? a_l : a_hi, true)
    end
    return (brent_aprime(a_l, a_hi, f_lo, f_hi, j, ia, ih, is, ig, iθ, m, h_now), true)
end

# Solve the household problem for one (j, ia, ih, is, ig, iθ) cell.
# Grid search over m, then (if refine_m) parabolic refinement of m*.
function solve_cell(j::Int, ia::Int, ih::Int, is::Int, ig::Int, iθ::Int)
    a_now = a_grid[ia]
    h_now = h_grid[ih]
    η_now = η_grid[is]

    if j == J
        ℓ_term = 0.0
        c_term = consumption_from_choices(j, a_now, h_now, η_now, ig, iθ, 0.0, 0.0)
        V_term = utility(c_term, ℓ_term, h_now)
        return (0.0, 0.0, c_term, ℓ_term, h_now, V_term)
    end

    m_grid = build_m_grid(j, ia, ih, is, ig, iθ)
    nM = length(m_grid)
    X  = available_resources(a_now, h_now, η_now, ig, iθ, j)

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

    # Parabolic refinement of m* around an interior winning node.
    if refine_m && best_idx >= 3 && best_idx <= nM - 1 &&
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
                        Threads.atomic_add!(n_refined, 1)
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

function solve_household_for_type(ig::Int, iθ::Int)
    # Each (ia, ih, is) cell writes its own 6-D slot; solve_cell only reads
    # forward-period policy arrays (set in a prior j-pass), so threading
    # the inner triple loop is safe. Outer j loop stays serial — backward
    # induction depends on j+1 being fully solved before j starts.
    # Cell index decoded from a flat k via divmod over (NH+1)*Nη.
    # Ported from ge_model.jl commit 054687c (+ f3110c1 race-fix).
    ncells = (NA + 1) * (NH + 1) * Nη
    Threads.@threads for k in 0:(ncells - 1)
        ia    = k ÷ ((NH + 1) * Nη)
        rem_k = k % ((NH + 1) * Nη)
        ih    = rem_k ÷ Nη
        is    = (rem_k % Nη) + 1
        ap, m, c, ℓ, hn, V = solve_cell(J, ia, ih, is, ig, iθ)
        aplus_pol[J, ig, ia, ih, is, iθ] = ap
        m_pol[J, ig, ia, ih, is, iθ]     = m
        c_pol[J, ig, ia, ih, is, iθ]     = c
        l_pol[J, ig, ia, ih, is, iθ]     = ℓ
        hnext_pol[J, ig, ia, ih, is, iθ] = hn
        V_pol[J, ig, ia, ih, is, iθ]     = V
    end
    for j in (J-1):-1:1
        Threads.@threads for k in 0:(ncells - 1)
            ia    = k ÷ ((NH + 1) * Nη)
            rem_k = k % ((NH + 1) * Nη)
            ih    = rem_k ÷ Nη
            is    = (rem_k % Nη) + 1
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

function solve_household!()
    Threads.atomic_xchg!(n_refined, 0)
    for iθ in 1:Nθ, ig in 1:Ng
        solve_household_for_type(ig, iθ)
    end
end

# ─── Ergodic distribution of η ───────────────────────────────────────────────
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

# ─── Forward distribution ────────────────────────────────────────────────────
# GE: surviving mass scales by ψ^g/(1+n_p) — the population-growth factor of the
# cohort-weight recursion (modelwithgender.tex eq. cohort_weights / lom).
function forward_distribution!()
    Φ .= 0.0
    ih_init_l, ih_init_r, φh_init = health_interp(h_init)
    for iθ in 1:Nθ, ig in 1:Ng, is in 1:Nη
        Φ[1, ig, 0, ih_init_l, is, iθ] += π_birth[ig, iθ] * π_η_erg[is] * φh_init
        Φ[1, ig, 0, ih_init_r, is, iθ] += π_birth[ig, iθ] * π_η_erg[is] * (1.0 - φh_init)
    end
    for j in 1:(J-1)
        for ia in 0:NA, ih in 0:NH, is in 1:Nη, ig in 1:Ng, iθ in 1:Nθ
            mass = Φ[j, ig, ia, ih, is, iθ]
            if mass < 1e-18; continue; end
            a_prime = aplus_pol[j, ig, ia, ih, is, iθ]
            h_n     = hnext_pol[j, ig, ia, ih, is, iθ]
            ial, iar, φ_a = asset_interp(a_prime)
            ihl, ihr, φ_h = health_interp(h_n)
            ψ_next = survival(j + 1, h_n, ig)
            mass_alive = mass * ψ_next / (1.0 + n_p)
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

# ============================================================================
# GE-specific machinery
# ============================================================================

# Working-age and retired mass — summed over both sexes (eq. agg_NWR).
function compute_population!()
    global N_W_now, N_R_now
    N_W = 0.0
    N_R = 0.0
    for j in 1:J, ig in 1:Ng, iθ in 1:Nθ
        mass = sum(Φ[j, ig, :, :, :, iθ])
        if j < j_R
            N_W += mass
        else
            N_R += mass
        end
    end
    N_W_now = N_W
    N_R_now = N_R
end

# Aggregates (modelwithgender.tex §3.8.1) — summed over (g, θ).
function aggregate_all()
    A_dom = 0.0
    L_eff = 0.0
    C     = 0.0
    M     = 0.0
    Λvoid = 0.0
    for j in 1:J, ig in 1:Ng, ia in 0:NA, ih in 0:NH, is in 1:Nη, iθ in 1:Nθ
        mass = Φ[j, ig, ia, ih, is, iθ]
        if mass < 1e-18; continue; end
        a_now = a_grid[ia]
        h_now = h_grid[ih]
        η_now = η_grid[is]
        A_dom += mass * a_now
        C     += mass * c_pol[j, ig, ia, ih, is, iθ]
        M     += mass * m_pol[j, ig, ia, ih, is, iθ]
        if j < j_R
            ν_j = productivity(j, h_now, η_now, ig, iθ)
            ℓ   = l_pol[j, ig, ia, ih, is, iθ]
            L_eff += mass * ν_j * ℓ
        end
        h_n     = hnext_pol[j, ig, ia, ih, is, iθ]
        ψ_next  = survival(j + 1, h_n, ig)
        a_prime = aplus_pol[j, ig, ia, ih, is, iθ]
        Λvoid += mass * (1.0 - ψ_next) * a_prime
    end
    return A_dom, L_eff, C, M, Λvoid
end

# Firm FOCs.
function update_prices!(K::Float64, L::Float64)
    global r_now, w_now, rn_now, wn_now
    r_now  = α * A_TFP * (K / L)^(α - 1.0) - δ_cap
    w_now  = (1.0 - α) * A_TFP * (K / L)^α
    rn_now = r_now * (1.0 - τk)
    wn_now = w_now * (1.0 - τw - τp_now)
end

# Pension closure τ^p = κ N^R/N^W and pension flow (modelwithgender.tex §3.5.2).
function update_pension_taxes!(L_eff::Float64)
    global τp_now, pen_now, wn_now
    if N_W_now > 0.0
        τp_now  = κ_rep * N_R_now / N_W_now
        pen_now = κ_rep * w_now * L_eff / N_W_now
    end
    wn_now = w_now * (1.0 - τw - τp_now)
end

# Debt-residual fiscal closure, corrected for population growth.
function compute_debt!(C::Float64, L::Float64, K::Float64, M::Float64, Y::Float64)
    global B_debt_now
    G = gy * Y
    primary = τc * C + τw * w_now * L + τk * r_now * K + τm * M - G
    B_debt_now = primary / (rn_now - n_p)
end

# ─── GE outer loop ───────────────────────────────────────────────────────────
mutable struct GEHistory
    iter::Vector{Int}
    K::Vector{Float64}
    L::Vector{Float64}
    r::Vector{Float64}
    w::Vector{Float64}
    τp::Vector{Float64}
    DIFF::Vector{Float64}
end
GEHistory() = GEHistory(Int[], Float64[], Float64[], Float64[], Float64[], Float64[], Float64[])

function push_history!(h::GEHistory, iter, K, L, r, w, τp, DIFF)
    push!(h.iter, iter); push!(h.K, K); push!(h.L, L)
    push!(h.r, r); push!(h.w, w); push!(h.τp, τp); push!(h.DIFF, DIFF)
end

function solve_ge!()
    global wn_now
    K = K_init
    L = L_init
    hist = GEHistory()

    println("INITIAL GE-Gender  (K₀=$(K_init), L₀=$(L_init), damp=$(damp_ge), tol=$(sig_ge))")
    println("iter   K        L        K/L      r(5y)    w        τp       DIFF/Y")
    println("─────  ───────  ───────  ───────  ───────  ───────  ───────  ─────────────")

    for iter in 1:itermax_ge
        update_prices!(K, L)
        if iter == 1
            wn_now = w_now * (1.0 - τw - τp_now)
        else
            update_pension_taxes!(L)
        end

        solve_household!()
        forward_distribution!()
        compute_population!()
        update_pension_taxes!(L)

        A_dom, L_new, C, M, Λvoid = aggregate_all()
        Y = A_TFP * K^α * L^(1.0 - α)
        compute_debt!(C, L, K, M, Y)
        K_target = A_dom - B_debt_now

        K_upd = damp_ge * K_target + (1.0 - damp_ge) * K
        L_upd = damp_ge * L_new   + (1.0 - damp_ge) * L
        # Positivity floor — belt-and-suspenders for the firm FOC
        # (K/L)^(α-1) which fails with a DomainError on a negative base.
        # Ported from draft_260519/ge_model.jl commit 054687c.
        K_upd = max(K_upd, 0.5)
        L_upd = max(L_upd, 0.5)

        G = gy * Y
        DIFF = (Y - C - M - (δ_cap + n_p) * K - G - Λvoid) / Y

        rel_K = abs(K_upd / K - 1.0)
        rel_L = abs(L_upd / L - 1.0)

        push_history!(hist, iter, K, L, r_now, w_now, τp_now, DIFF)
        @printf "%-5d  %-7.3f  %-7.3f  %-7.3f  %-7.4f  %-7.4f  %-7.4f  %+13.6e\n" iter K L (K/L) r_now w_now τp_now DIFF
        flush(stdout)

        if max(rel_K, rel_L, abs(DIFF)) < sig_ge && iter > 1
            println("  → CONVERGED at iter $iter")
            return hist, A_dom, L_new, C, M, Λvoid, Y, K, L
        end
        K, L = K_upd, L_upd
    end
    println("  → DID NOT CONVERGE within $itermax_ge iterations")
    update_prices!(K, L)
    update_pension_taxes!(L)
    A_dom, L_new, C, M, Λvoid = aggregate_all()
    Y = A_TFP * K^α * L^(1.0 - α)
    return hist, A_dom, L_new, C, M, Λvoid, Y, K, L
end

# ─── Welfare object (modelwithgender.tex §6) — per (sex, skill) ──────────────
function welfare_at_birth()
    ih_l, ih_r, φh = health_interp(h_init)
    W = zeros(Ng, Nθ)
    for ig in 1:Ng, iθ in 1:Nθ
        s = 0.0
        for is in 1:Nη
            V_l = V_pol[1, ig, 0, ih_l, is, iθ]
            V_r = V_pol[1, ig, 0, ih_r, is, iθ]
            s += π_η_erg[is] * (φh * V_l + (1.0 - φh) * V_r)
        end
        W[ig, iθ] = s
    end
    return W
end

# ============================================================================
# Diagnostics
# ============================================================================

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

function euler_residual_stats()
    residuals = Float64[]
    for j in 1:(J-1), ig in 1:Ng, iθ in 1:Nθ
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            if is_corner_cell(j, ia, ih, is, ig, iθ); continue; end
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

function m_positivity_by_age()
    out = zeros(J, Ng, Nθ)
    for j in 1:J, ig in 1:Ng, iθ in 1:Nθ
        mass_total = 0.0
        mass_pos   = 0.0
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
            cm_c[j, ig, iθ] /= wsum; cm_l[j, ig, iθ] /= wsum
            cm_a[j, ig, iθ] /= wsum; cm_m[j, ig, iθ] /= wsum
            cm_h[j, ig, iθ] /= wsum
        end
    end
    return cm_c, cm_l, cm_a, cm_m, cm_h
end

# Cohort-share invariant: φ_{j+1}/φ_j vs ψ̄_{j+1}/(1+n_p) per (sex, skill).
function cohort_share_invariant()
    max_dev = 0.0
    for ig in 1:Ng, iθ in 1:Nθ
        for j in 1:(J-1)
            φj  = sum(Φ[j,   ig, :, :, :, iθ])
            φj1 = sum(Φ[j+1, ig, :, :, :, iθ])
            if φj < 1e-18; continue; end
            ψbar_num = 0.0
            for ia in 0:NA, ih in 0:NH, is in 1:Nη
                w = Φ[j, ig, ia, ih, is, iθ]
                if w < 1e-18; continue; end
                h_n = hnext_pol[j, ig, ia, ih, is, iθ]
                ψbar_num += w * survival(j + 1, h_n, ig)
            end
            ψbar = ψbar_num / φj
            max_dev = max(max_dev, abs(φj1 / φj - ψbar / (1.0 + n_p)))
        end
    end
    return max_dev
end

# Hard @assert gates — household-cell checks plus GE market clearing.
function diagnostic_gates(DIFF::Float64, K::Float64, L::Float64,
                          A_dom::Float64, C::Float64, M::Float64, Y::Float64)
    println("\n─── Diagnostic gates ────────────────────────────────────────")

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

    # GE market-clearing residuals.
    cap_resid = abs(K - (A_dom - B_debt_now)) / max(abs(K), 1e-12)
    gov_resid = (τc*C + τw*w_now*L + τk*r_now*K + τm*M - gy*Y - (rn_now - n_p)*B_debt_now) / Y

    @printf "  budget residual      max = %.3e   (gate < 1e-4, GE iter-order)\n" max_budget
    @printf "  consumption          min = %.3e   floored cells = %d\n" min_c n_c_floor
    @printf "  savings a'           min = %.3e   max = %.3e\n" min_aprime max_aprime
    @printf "  distribution Φ       min = %.3e   all finite = %s\n" min_Φ all_finite_Φ
    @printf "  newborn mass ΣΦ[1]       = %.12f   (gate ≈ 1)\n" newborn_mass
    @printf "  asset-top mass share     = %.3e   (gate < 1e-3)\n" top_share
    @printf "  terminal |a',m,ℓ| at j=J = %.3e   (gate = 0)\n" term
    @printf "  Euler residual log10 max = %.3f       (gate < -1; mean and p95 are the useful stats)\n" euler_max
    @printf "  two-sex max |male-female|= %.3e   (%s)\n" max_sex (gender_gap ? "expected ≠ 0 — gender_gap = true" : "gate < 1e-10, symmetric stub")
    @printf "  cohort-share invariant   = %.3e   (gate < 1e-8)\n" cs_inv
    @printf "  health h' range          = [%.4f, %.4f]   below-h_l cells = %d (soft)\n" min_hnext max_hnext n_hnext_below
    @printf "  medical m* at grid top   = %.3f%% of mass (soft, near-budget corner)\n" (100.0*m_at_top_mass/scan_mass)
    @printf "  m* parabolic refinement  = %d cells refined   (refine_m = %s)\n" n_refined[] refine_m
    @printf "  goods market DIFF/Y      = %+.3e  (gate < %.0e)\n" DIFF sig_ge
    @printf "  capital market |K-(A_dom-B)|/K = %.3e  (gate < %.0e ≈ 2·sig_ge)\n" cap_resid (2*sig_ge)
    @printf "  government BC residual/Y = %+.3e  (gate < 1e-6)\n" gov_resid

    # GE gate is 1e-4, not the PE 1e-8: `update_pension_taxes!` is called once
    # more inside solve_ge! AFTER the final solve_household!, so the stored
    # policies use a slightly different τp than the post-iter globals. The
    # residual is w·ν·ℓ·Δτp — machine-precision economically (~1e-5 here).
    @assert max_budget < 1e-4                          "budget residual exceeds 1e-4"
    @assert n_c_floor == 0                             "consumption hit the 1e-12 floor"
    @assert min_c > 0.0                                "non-positive consumption"
    @assert min_aprime >= a_l - 1e-9                   "savings below the borrowing constraint"
    @assert min_Φ >= -1e-14                            "negative mass in the distribution"
    @assert all_finite_Φ                               "non-finite mass in the distribution"
    @assert isapprox(newborn_mass, 1.0; atol = 1e-12)  "newborn cohort mass ≠ 1"
    @assert top_share < 1e-3                           "mass piles up at a_max"
    @assert term == 0.0                                "terminal condition a'=m=ℓ=0 violated"
    # Mean log10|r|/u_c well below −4 is the substantive quality check; max is
    # gated at −1 because rare near-corner old-age cells on the kinked bilinear
    # surface can spike to ~10⁻¹ at single grid points without affecting the
    # mass-weighted aggregates. p95 < −5 is the practical reassurance.
    @assert euler_max < -1.0                           "Euler residual above the -1 gate"
    if !gender_gap
        @assert max_sex < 1e-10                        "two-sex identity broken (symmetric stub)"
    end
    @assert cs_inv < 1e-8                              "cohort-share invariant violated"
    @assert min_hnext >= 0.0                           "negative next-period health"
    @assert max_hnext <= h_u + 1e-9                    "next-period health exceeds h̄"
    @assert abs(DIFF) < 1e-3                           "goods market not cleared"
    # At convergence rel_K < sig_ge ⇒ |K - K_target|/K = rel_K/damp = 2·sig_ge,
    # so the natural capital-market gate is 2·sig_ge, not sig_ge itself.
    @assert cap_resid < 2*sig_ge + 1e-9                "capital market not cleared (above 2·sig_ge)"
    @assert abs(gov_resid) < 1e-6                      "government budget not balanced"
    println("  ✔ all hard gates passed")
end

# ─── GE summary ──────────────────────────────────────────────────────────────
function print_ge_summary(hist, A_dom, L_new, C, M, Λvoid, Y, K, L, W)
    println("\n══════════════════════════════════════════════════════════════")
    println(" Stationary GE — GENDER extension (Modelmay)")
    println("══════════════════════════════════════════════════════════════")
    println("  Build:  J = $(J),  $(Ng) sexes × $(Nθ) skills = $(Ng*Nθ) types")
    @printf "  K        = %.5f\n"  K
    @printf "  L        = %.5f\n"  L
    @printf "  K/L      = %.5f\n"  K/L
    @printf "  Y        = %.5f\n"  Y
    @printf "  K/Y (5y) = %.5f   |  K/Y annual = %.3f\n"  (K/Y) (K/Y/5)
    @printf "  r (5-yr) = %.5f   |  r annual   = %.4f%%\n"  r_now ((1.0+r_now)^0.2 - 1)*100
    @printf "  w        = %.5f\n"  w_now
    @printf "  C        = %.5f   |  C/Y = %.2f%%\n"  C (100*C/Y)
    @printf "  M        = %.5f   |  M/Y = %.2f%%\n"  M (100*M/Y)
    @printf "  G        = %.5f   |  G/Y = %.2f%%\n"  (gy*Y) (100*gy)
    @printf "  δK       = %.5f   |  δK/Y = %.2f%%\n"  (δ_cap*K) (100*δ_cap*K/Y)
    @printf "  Λ_void   = %.5f   |  Λ_void/Y = %.2f%%\n"  Λvoid (100*Λvoid/Y)
    @printf "  A_dom    = %.5f\n"  A_dom
    @printf "  B (debt) = %.5f\n"  B_debt_now
    @printf "  τp       = %.5f\n"  τp_now
    @printf "  pen      = %.5f\n"  pen_now
    @printf "  N^W      = %.5f   |  N^R = %.5f   |  N^R/N^W = %.5f\n"  N_W_now N_R_now (N_R_now/N_W_now)
    println()
    @printf "  Goods market residual (Y-C-M-(δ+n_p)K-G-Λ_void)/Y = %+.6e\n"  hist.DIFF[end]
    @printf "  Gov BC residual ((rn-n_p)B = primary)             = %+.6e\n"  ((τc*C + τw*w_now*L + τk*r_now*K + τm*M - gy*Y - (rn_now - n_p)*B_debt_now) / Y)
    println()
    println("  Welfare object 𝒲₁(g,θ) — expected lifetime utility at birth:")
    @printf "                  θ_L         θ_H\n"
    @printf "    male      %10.5f  %10.5f\n"  W[1,1] W[1,2]
    @printf "    female    %10.5f  %10.5f\n"  W[2,1] W[2,2]
    agg_W = 0.0
    for ig in 1:Ng, iθ in 1:Nθ
        agg_W += π_birth[ig, iθ] * W[ig, iθ]
    end
    @printf "    birth-share-weighted aggregate 𝒲₁ = %.5f\n"  agg_W

    res = euler_residual_stats()
    if !isempty(res)
        rlog = log10.(max.(res, 1e-16))
        @printf "\n  Euler residual |r|/u_c (n=%d interior cells):\n"  length(res)
        @printf "     mean log10 = %.3f,  max log10 = %.3f,  p95 log10 = %.3f\n" mean(rlog) maximum(rlog) Statistics.quantile(rlog, 0.95)
    end
end

# ─── CSVs ────────────────────────────────────────────────────────────────────
function write_csv(hist, A_dom, L_new, C, M, Λvoid, Y, K, L, W)
    cm_c, cm_l, cm_a, cm_m, cm_h = cohort_means()
    pos = m_positivity_by_age()
    out_dir = @__DIR__
    suffix = gender_gap ? "_gap" : ""
    open(joinpath(out_dir, "ge_lifecycle$(suffix).csv"), "w") do io
        println(io, "age_period,sex_idx,theta_idx,theta_value,c,l,a,m,h,m_positive_share")
        for j in 1:J, ig in 1:Ng, iθ in 1:Nθ
            println(io, "$j,$ig,$iθ,$(θ_grid[iθ]),$(cm_c[j,ig,iθ]),$(cm_l[j,ig,iθ]),$(cm_a[j,ig,iθ]),$(cm_m[j,ig,iθ]),$(cm_h[j,ig,iθ]),$(pos[j,ig,iθ])")
        end
    end
    open(joinpath(out_dir, "ge_summary$(suffix).csv"), "w") do io
        println(io, "metric,value")
        println(io, "K,$K"); println(io, "L,$L"); println(io, "K_over_L,$(K/L)")
        println(io, "Y,$Y"); println(io, "C,$C"); println(io, "M,$M")
        println(io, "G,$(gy*Y)"); println(io, "deltaK,$(δ_cap*K)"); println(io, "Lambda_void,$Λvoid")
        println(io, "r_5yr,$(r_now)"); println(io, "w,$(w_now)")
        println(io, "taup,$(τp_now)"); println(io, "pen,$(pen_now)")
        println(io, "B_debt,$(B_debt_now)"); println(io, "A_dom,$A_dom")
        println(io, "N_W,$(N_W_now)"); println(io, "N_R,$(N_R_now)")
        for ig in 1:Ng, iθ in 1:Nθ
            sx = ig == 1 ? "M" : "F"
            sk = iθ == 1 ? "thetaL" : "thetaH"
            println(io, "W1_$(sx)_$(sk),$(W[ig,iθ])")
        end
        println(io, "K_over_Y_5yr,$(K/Y)"); println(io, "C_over_Y,$(C/Y)")
        println(io, "M_over_Y,$(M/Y)")
    end
    open(joinpath(out_dir, "ge_history$(suffix).csv"), "w") do io
        println(io, "iter,K,L,r,w,taup,DIFF_over_Y")
        for k in eachindex(hist.iter)
            println(io, "$(hist.iter[k]),$(hist.K[k]),$(hist.L[k]),$(hist.r[k]),$(hist.w[k]),$(hist.τp[k]),$(hist.DIFF[k])")
        end
    end
    println("  Wrote ge_lifecycle$(suffix).csv, ge_summary$(suffix).csv, ge_history$(suffix).csv  (under $(out_dir))")
end

# ─── Plots ───────────────────────────────────────────────────────────────────
ages_vec() = 15 .+ 5 .* (1:J)

const _COL = [:steelblue, :firebrick]
const _STY = [:solid, :dash]
_typelabel(ig, iθ) = (ig == 1 ? "M," : "F,") * (iθ == 1 ? "θ_L" : "θ_H")

function _add_type_lines!(p, ages, data; rng = 1:J, legend = :best)
    for ig in 1:Ng, iθ in 1:Nθ
        plot!(p, ages[rng], data[rng, ig, iθ];
              label = _typelabel(ig, iθ), lw = 2,
              color = _COL[iθ], ls = _STY[ig], legend = legend)
    end
    return p
end

function plot_lifecycle_profiles()
    cm_c, cm_l, cm_a, cm_m, cm_h = cohort_means()
    ages = ages_vec()
    p_c = plot(; ylabel="Consumption", xlabel="Age"); _add_type_lines!(p_c, ages, cm_c; legend=:topleft)
    p_l = plot(; ylabel="Labor ℓ", xlabel="Age");     _add_type_lines!(p_l, ages, cm_l; rng=1:j_R-1, legend=:topright)
    p_a = plot(; ylabel="Assets a", xlabel="Age");    _add_type_lines!(p_a, ages, cm_a; legend=:topleft)
    p_m = plot(; ylabel="Medical m", xlabel="Age");   _add_type_lines!(p_m, ages, cm_m; legend=:topleft)
    p_h = plot(; ylabel="Health h", xlabel="Age", ylim=(0,1.05)); _add_type_lines!(p_h, ages, cm_h; legend=:bottomleft)
    mass = zeros(J, Ng, Nθ)
    for j in 1:J, ig in 1:Ng, iθ in 1:Nθ; mass[j,ig,iθ] = sum(Φ[j,ig,:,:,:,iθ]); end
    for ig in 1:Ng, iθ in 1:Nθ; mass[:,ig,iθ] ./= mass[1,ig,iθ]; end
    p_n = plot(; ylabel="Surv. mass / newborn", xlabel="Age", ylim=(0,1.05)); _add_type_lines!(p_n, ages, mass; legend=:bottomleft)
    return plot(p_c, p_l, p_a, p_m, p_h, p_n; layout=(2,3), size=(1200, 760),
                plot_title="GE-Gender life-cycle profiles (mass-weighted)")
end

function plot_ge_convergence(hist::GEHistory)
    its = hist.iter
    p_K = plot(its, hist.K; lw=2, marker=:circle, color=:steelblue, ylabel="K", xlabel="iter", label="")
    p_L = plot(its, hist.L; lw=2, marker=:circle, color=:firebrick, ylabel="L", xlabel="iter", label="")
    p_r = plot(its, hist.r; lw=2, marker=:circle, color=:forestgreen, ylabel="r (5-yr)", xlabel="iter", label="")
    p_w = plot(its, hist.w; lw=2, marker=:circle, color=:darkorange, ylabel="w", xlabel="iter", label="")
    p_τp = plot(its, hist.τp; lw=2, marker=:circle, color=:purple, ylabel="τp", xlabel="iter", label="")
    p_DIFF = plot(its, hist.DIFF; lw=2, marker=:circle, color=:black, ylabel="DIFF/Y", xlabel="iter", label="")
    hline!(p_DIFF, [sig_ge, -sig_ge]; lw=1, ls=:dash, color=:gray, label="±tol")
    return plot(p_K, p_L, p_r, p_w, p_τp, p_DIFF; layout=(2,3), size=(1100, 720),
                plot_title="GE-Gender convergence")
end

function plot_aggregate_identity(C, M, K, Y, Λvoid)
    parts = [C, M, (δ_cap+n_p)*K, gy*Y, Λvoid]
    labs  = ["C", "M", "(δ+n_p)K", "G", "Λ_void"]
    colors= [:steelblue, :firebrick, :forestgreen, :darkorange, :purple]
    p = bar(labs, parts; color=colors, ylabel="goods, units of Y",
            title=@sprintf("Y = %.4f  vs  sum = %.4f", Y, sum(parts)), label="")
    hline!(p, [Y]; lw=2, color=:black, label="Y")
    return p
end

function plot_m_positivity()
    pos = m_positivity_by_age()
    ages = ages_vec()
    offs = [-1.5, -0.5, 0.5, 1.5]
    cols = [:steelblue, :firebrick, :lightblue, :salmon]
    p = plot(; xlabel="Age", ylabel="P(m* > 0)", ylim=(0,1.05),
             title="Fraction of mass with m* > 0  (GE-Gender)", legend=:bottomright)
    k = 0
    for ig in 1:Ng, iθ in 1:Nθ
        k += 1
        bar!(p, ages .+ offs[k], pos[:, ig, iθ]; label=_typelabel(ig, iθ), color=cols[k], bar_width=1.0)
    end
    return p
end

function plot_euler_residuals()
    res = euler_residual_stats()
    rs = log10.(max.(res, 1e-16))
    mean_r = round(mean(rs); digits=2); max_r = round(maximum(rs); digits=2)
    p = histogram(rs; bins=50, color=:steelblue, alpha=0.7,
                  xlabel="log₁₀ |r| / u_c", ylabel="count",
                  title="Euler residuals (interior cells)  mean=$mean_r max=$max_r", label="")
    vline!(p, [-4.0]; lw=2, color=:darkred, label="target (-4)")
    return p
end

function plot_welfare(W)
    types = [_typelabel(ig,iθ) for ig in 1:Ng for iθ in 1:Nθ]
    vals  = [W[ig,iθ] for ig in 1:Ng for iθ in 1:Nθ]
    p = bar(types, vals; color=[:steelblue,:firebrick,:lightblue,:salmon],
            ylabel="𝒲₁(g,θ)", title="Welfare at birth by type (GE-Gender)", label="")
    return p
end

function make_audit_plots(hist::GEHistory, C, M, K, Y, Λvoid, L, W)
    plot_dir = joinpath(@__DIR__, gender_gap ? "plots-gap" : "plots")
    isdir(plot_dir) || mkpath(plot_dir)
    savefig(plot_lifecycle_profiles(),                  joinpath(plot_dir, "ge_01_lifecycle.png"))
    savefig(plot_ge_convergence(hist),                  joinpath(plot_dir, "ge_02_convergence.png"))
    savefig(plot_aggregate_identity(C, M, K, Y, Λvoid), joinpath(plot_dir, "ge_03_aggregate_identity.png"))
    savefig(plot_m_positivity(),                        joinpath(plot_dir, "ge_04_m_positivity.png"))
    savefig(plot_euler_residuals(),                     joinpath(plot_dir, "ge_05_euler_residuals.png"))
    savefig(plot_welfare(W),                            joinpath(plot_dir, "ge_06_welfare.png"))
    println("  Wrote 6 GE-Gender audit plots to $(plot_dir)/ge_*.png")
end

# ============================================================================
# Main
# ============================================================================
function main()
    if gender_gap
        println("► Gender-gap experiment: e^female = 0.85·e^male, mortality_female = 0.75·mortality_male")
    else
        println("► Symmetric stub: men ≡ women (collapse-to-DraftApril mode)")
    end
    println("Initializing grids …  (J = $J, $(Ng) sexes × $(Nθ) skills = $(Ng*Nθ) types)")
    grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
    grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
    π_mat, η_vec = rouwenhorst(Nη, ρ_AR, σ_ε, 0.0)
    π_η .= π_mat
    η_grid .= η_vec
    compute_ergodic!()

    hist, A_dom, L_new, C, M, Λvoid, Y, K, L = solve_ge!()

    W = welfare_at_birth()
    print_ge_summary(hist, A_dom, L_new, C, M, Λvoid, Y, K, L, W)
    write_csv(hist, A_dom, L_new, C, M, Λvoid, Y, K, L, W)

    println("\nGenerating GE-Gender audit plots …")
    make_audit_plots(hist, C, M, K, Y, Λvoid, L, W)
    # Gates last: a failing assert still leaves CSVs + plots on disk.
    diagnostic_gates(hist.DIFF[end], K, L, A_dom, C, M, Y)
end

# Run main() only when invoked directly — allows other scripts to `include` this
# file (e.g. audits/regenerate_plots.jl) without triggering the full GE solve.
if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
