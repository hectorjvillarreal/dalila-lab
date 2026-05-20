################################################################################
#  ge_model.jl
#
#  Self-contained stationary general-equilibrium solver for DraftApril.pdf.
#  Endogenous: prices (r, w), pension contribution τ^p, pension flow pen,
#  government debt B (residual closure per PDF eq. 17).
#  Externally fixed: tax rates (τ^c, τ^w, τ^k, τ^m), gy, κ, production (α, δ, A),
#  demographic (n_p), all preferences and household primitives.
#
#  Parameter values MIRROR `household_problem.jl`. If you change one, change the
#  other or risk drift. The canonical reference is `parametric_assumptions.tex`.
#
#  Discrepancy-report items addressed in this file:
#    M1 — Goods market: Y = C + M + δK + G + Λ_void (PDF eq. 24)
#    M6 — Fiscal closure: B residual (PDF eq. 17)
#    M7 — Pension formula: no one-period lag; pen = κ wL/N^W (PDF eq. 19)
#    M3 — Welfare object 𝒲₁(θ) (PDF eq. 58) — partial (no CEV here)
################################################################################

using OffsetArrays
using DynamicProgrammingUtils
using Roots
using Printf
using Statistics
using Plots

# ─── Category A parameters (from PDF) ────────────────────────────────────────
const γ_pref     = 2.0                  # [PDF] GHH risk-aversion exponent
const ν_pref     = 2.0                  # [PDF] inverse Frisch
const β_pref     = 0.998^5              # [PDF] 5-yr discount factor
const ρ_AR       = 0.98                 # [PDF] AR(1) persistence
const σ_ε        = 0.05                 # [PDF] AR(1) innov s.d.

const J          = 16                   # [PDF] max age
const j_R        = 10                   # [PDF] retirement age
const Nη         = 7                    # [PDF] productivity nodes

const τc         = 0.16                 # [PDF] consumption tax
const τw         = 0.20                 # [introduced] labor tax (PE placeholder)
const τk         = 0.20                 # [introduced] capital tax (PE placeholder)
const τm         = -0.20                 # [PDF] medical-spending tax
const gy         = 0.19                 # [PDF] G/Y share
const κ_rep      = 0.50                 # [PDF] pension replacement rate

const α          = 0.36                 # [PDF] capital share
const δ_cap      = 1.0 - (1.0 - 0.0823)^5  # [PDF] capital depreciation, 5-yr
const A_TFP      = 1.60                 # [PDF] TFP
const n_p        = 1.01^5 - 1.0         # [introduced] population growth, 5-yr

# ─── Category B parameters (PDF-open, fixed here) ────────────────────────────
const Ξ_amenity  = 0.50
const ξ_curv     = 0.50
const Ψ_labor    = 14.0                 # tuned in PE pass to hit ℓ ≈ 1/3

const θ_grid     = [-0.20, 0.20]
const Nθ         = length(θ_grid)
const ϱ_pen      = [0.30, 0.20]
const φ1_share   = [0.50, 0.50]

const e_age = [1.0000, 1.3527, 1.6952, 1.8279, 1.9606, 1.9692, 1.9692,
               1.9392, 1.9007, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

const δh = [0.02, 0.02, 0.03, 0.03, 0.05, 0.07, 0.10, 0.14,
            0.18, 0.22, 0.27, 0.32, 0.38, 0.45, 0.55, 0.70]

const H_scale    = 0.30
const H_curv     = 0.50
const h_init     = 1.00

const ψ_base = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                0.98972953, 0.98185396, 0.97070373, 0.95530594,
                0.93417914, 0.90238714, 0.83653436, 0.71048182,
                0.52669353, 0.31179803]

# ─── ENDOGENOUS GE state (typed mutable globals) ────────────────────────────
# Note: typed globals (`g::T = value`) are inlinable by Julia's optimizer; using
# `Ref{Float64}` here caused a ~17× slowdown of the inner solver loop because
# `ref[]` reads were not constant-folded. Typed globals recover most of the
# perf of `const` while still being mutable across GE iterations.
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

const Nm         = 30
const m_min      = 1e-3
const m_max_frac = 1.0/3.0

# ─── GE control ──────────────────────────────────────────────────────────────
const K_init     = 12.0
const L_init     = 10.0
const damp_ge    = 0.30                 # Lowered back from 0.50 — works robustly across the policy-shock experiments (κ=0.30, τ^m=-0.20) where the early-iter K_target can overshoot under 0.50 damping.
const sig_ge     = 1e-4
const itermax_ge = 30

# ─── Grids and buffers ───────────────────────────────────────────────────────
const a_grid    = OffsetArray(zeros(NA+1), 0:NA)
const h_grid    = OffsetArray(zeros(NH+1), 0:NH)
const η_grid    = zeros(Nη)
const π_η       = zeros(Nη, Nη)
const π_η_erg   = zeros(Nη)

# Per-thread scratch buffers for the bilinear interpolation routines below.
# linint_Grow writes the index/weight outputs into these length-1 arrays; if
# they were shared across threads (the original implementation), concurrent
# calls from inside `Threads.@threads` loops would race. Each Julia thread
# now owns its own slot indexed by `Threads.threadid()`.
const ial_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const iar_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const varphi_a_buf_per_thread = [zeros(1)               for _ in 1:Threads.nthreads()]
const ihl_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const ihr_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const varphi_h_buf_per_thread = [zeros(1)               for _ in 1:Threads.nthreads()]

# ─── Policy and distribution storage ─────────────────────────────────────────
const aplus_pol = OffsetArray(zeros(J, NA+1, NH+1, Nη, Nθ), 1:J, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const m_pol     = OffsetArray(zeros(J, NA+1, NH+1, Nη, Nθ), 1:J, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const c_pol     = OffsetArray(zeros(J, NA+1, NH+1, Nη, Nθ), 1:J, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const l_pol     = OffsetArray(zeros(J, NA+1, NH+1, Nη, Nθ), 1:J, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const hnext_pol = OffsetArray(zeros(J, NA+1, NH+1, Nη, Nθ), 1:J, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const V_pol     = OffsetArray(zeros(J, NA+1, NH+1, Nη, Nθ), 1:J, 0:NA, 0:NH, 1:Nη, 1:Nθ)
const Φ         = OffsetArray(zeros(J, NA+1, NH+1, Nη, Nθ), 1:J, 0:NA, 0:NH, 1:Nη, 1:Nθ)

# ============================================================================
# Helper functions (mirror household_problem.jl, reading from Refs where prices
# matter).
# ============================================================================

# PDF eq. (6).
function health_amenity(h::Float64)::Float64
    h_safe = max(h, 1e-12)
    if abs(ξ_curv - 1.0) < 1e-10
        return Ξ_amenity * log(h_safe)
    else
        return Ξ_amenity * h_safe^(1.0 - ξ_curv) / (1.0 - ξ_curv)
    end
end

# PDF eq. (5).
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

# PDF eq. (13), sign per prose (good health raises productivity).
function productivity(j::Int, h::Float64, η::Float64, iθ::Int)::Float64
    if j >= j_R
        return 0.0
    end
    return e_age[j] * exp(θ_grid[iθ] + η + ϱ_pen[iθ] * h)
end

# PDF §4.1.1 placeholder.
function survival(j::Int, h::Float64)::Float64
    if j < 1 || j > J + 1
        return 0.0
    end
    if j == J + 1
        return 0.0
    end
    return ψ_base[j] * (0.70 + 0.30 * h)
end

# PDF eq. (15) — health-production technology (age-invariant placeholder).
function health_production(m::Float64)::Float64
    if m <= 0.0
        return 0.0
    end
    return H_scale * m^H_curv
end

# PDF eq. (15) — health law of motion.
function health_next(h::Float64, m::Float64, j::Int)::Float64
    return min((1.0 - δh[j]) * h + health_production(m), h_u)
end

# GHH labor-supply FOC: closed-form, no wealth effects.
#   Ψ ℓ^ν = w · ν_j · (1 - τw - τp) / (1 + τc)
function labor_supply(j::Int, h::Float64, η::Float64, iθ::Int)::Float64
    if j >= j_R
        return 0.0
    end
    ν_j = productivity(j, h, η, iθ)
    if ν_j <= 0.0
        return 0.0
    end
    numer = w_now * ν_j * (1.0 - τw - τp_now)
    denom = (1.0 + τc) * Ψ_labor
    ℓ_star = (numer / denom) ^ (1.0 / ν_pref)
    return clamp(ℓ_star, 0.0, 1.0)
end

# Available resources X (PDF eq. 28): bq ≡ 0 per voiding assumption (PDF §3.1).
function available_resources(a::Float64, h::Float64, η::Float64, iθ::Int, j::Int)::Float64
    if j < j_R
        ℓ = labor_supply(j, h, η, iθ)
        ν_j = productivity(j, h, η, iθ)
        labor_income = w_now * ν_j * ℓ * (1.0 - τw - τp_now)
        return (1.0 + rn_now) * a + labor_income
    else
        return (1.0 + rn_now) * a + pen_now
    end
end

function consumption_from_choices(j::Int, a::Float64, h::Float64, η::Float64, iθ::Int,
                                   a_prime::Float64, m::Float64)::Float64
    X = available_resources(a, h, η, iθ, j)
    c = (X - a_prime - (1.0 + τm) * m) / (1.0 + τc)
    return max(c, 1e-12)
end

# ─── Bilinear interp ─────────────────────────────────────────────────────────
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

function interp_pol(P::OffsetArray, j_next::Int, a_prime::Float64,
                    h_next::Float64, is::Int, iθ::Int)::Float64
    ial, iar, φ_a = asset_interp(a_prime)
    ihl, ihr, φ_h = health_interp(h_next)
    return φ_a       * φ_h       * P[j_next, ial, ihl, is, iθ] +
           φ_a       * (1.0-φ_h) * P[j_next, ial, ihr, is, iθ] +
           (1.0-φ_a) * φ_h       * P[j_next, iar, ihl, is, iθ] +
           (1.0-φ_a) * (1.0-φ_h) * P[j_next, iar, ihr, is, iθ]
end

function expected_uc_next(j_next::Int, a_prime::Float64, h_next::Float64,
                          is_now::Int, iθ::Int)::Float64
    s = 0.0
    for is_p in 1:Nη
        c_p  = interp_pol(c_pol, j_next, a_prime, h_next, is_p, iθ)
        ℓ_p  = interp_pol(l_pol, j_next, a_prime, h_next, is_p, iθ)
        uc_p = marginal_utility_c(c_p, ℓ_p, h_next)
        s += π_η[is_now, is_p] * uc_p
    end
    return s
end

function euler_residual(a_prime::Float64, j::Int, ia::Int, ih::Int, is::Int, iθ::Int,
                        m::Float64, h_now::Float64)::Float64
    a_now = a_grid[ia]
    η_now = η_grid[is]
    ℓ_now = labor_supply(j, h_now, η_now, iθ)
    c_now = consumption_from_choices(j, a_now, h_now, η_now, iθ, a_prime, m)
    uc_now = marginal_utility_c(c_now, ℓ_now, h_now)
    h_nxt = health_next(h_now, m, j)
    Euc_nxt = expected_uc_next(j + 1, a_prime, h_nxt, is, iθ)
    rhs = β_pref * survival(j + 1, h_nxt) * (1.0 + rn_now) * Euc_nxt
    return uc_now - rhs
end

function value_at(a_prime::Float64, j::Int, ia::Int, ih::Int, is::Int, iθ::Int,
                  m::Float64, h_now::Float64)::Float64
    a_now = a_grid[ia]
    η_now = η_grid[is]
    ℓ_now = labor_supply(j, h_now, η_now, iθ)
    c_now = consumption_from_choices(j, a_now, h_now, η_now, iθ, a_prime, m)
    h_nxt = health_next(h_now, m, j)
    u_now = utility(c_now, ℓ_now, h_now)
    if j == J
        return u_now
    end
    EV = 0.0
    for is_p in 1:Nη
        Vp = interp_pol(V_pol, j + 1, a_prime, h_nxt, is_p, iθ)
        EV += π_η[is, is_p] * Vp
    end
    return u_now + β_pref * survival(j + 1, h_nxt) * EV
end

function build_m_grid(j::Int, ia::Int, ih::Int, is::Int, iθ::Int)
    a_now = a_grid[ia]
    h_now = h_grid[ih]
    η_now = η_grid[is]
    X = available_resources(a_now, h_now, η_now, iθ, j)
    m_max = max(m_max_frac * X, m_min * 2.0)
    if m_max <= m_min
        return Float64[0.0]
    end
    logs = range(log(m_min), log(m_max); length = Nm - 1)
    return vcat(0.0, exp.(logs))
end

function solve_cell(j::Int, ia::Int, ih::Int, is::Int, iθ::Int)
    a_now = a_grid[ia]
    h_now = h_grid[ih]
    η_now = η_grid[is]

    if j == J
        ℓ_term = 0.0
        c_term = consumption_from_choices(j, a_now, h_now, η_now, iθ, 0.0, 0.0)
        V_term = utility(c_term, ℓ_term, h_now)
        return (0.0, 0.0, c_term, ℓ_term, h_now, V_term)
    end

    m_grid = build_m_grid(j, ia, ih, is, iθ)
    best_V = -Inf
    best_aprime = 0.0
    best_m = 0.0
    best_c = 0.0
    best_ℓ = 0.0
    best_hnext = h_now

    for m_cand in m_grid
        X = available_resources(a_now, h_now, η_now, iθ, j)
        m_cost = (1.0 + τm) * m_cand
        avail_after_m = X - m_cost
        if avail_after_m <= 0.0
            continue
        end
        a_hi = max(avail_after_m - 1e-6, a_l)
        if a_hi <= a_l
            aprime_star = a_l
        else
            f_lo = euler_residual(a_l, j, ia, ih, is, iθ, m_cand, h_now)
            f_hi = euler_residual(a_hi, j, ia, ih, is, iθ, m_cand, h_now)
            if f_lo * f_hi > 0.0
                aprime_star = f_lo > 0.0 ? a_l : a_hi
            else
                try
                    aprime_star = find_zero(
                        x -> euler_residual(x, j, ia, ih, is, iθ, m_cand, h_now),
                        (a_l, a_hi), Roots.Brent())
                catch
                    aprime_star = a_l
                end
            end
        end
        V_here = value_at(aprime_star, j, ia, ih, is, iθ, m_cand, h_now)
        if V_here > best_V
            best_V = V_here
            best_aprime = aprime_star
            best_m = m_cand
            best_ℓ = labor_supply(j, h_now, η_now, iθ)
            best_c = consumption_from_choices(j, a_now, h_now, η_now, iθ, aprime_star, m_cand)
            best_hnext = health_next(h_now, m_cand, j)
        end
    end
    return (best_aprime, best_m, best_c, best_ℓ, best_hnext, best_V)
end

function solve_household_for_type(iθ::Int)
    # Each (ia, ih, is) cell writes its own slot; solve_cell only reads
    # forward-period policy arrays, so threading the inner triple loop is
    # safe. Outer j loop must remain serial (backward induction).
    ncells = (NA + 1) * (NH + 1) * Nη
    Threads.@threads for k in 0:(ncells - 1)
        ia = k ÷ ((NH + 1) * Nη)
        rem_k = k % ((NH + 1) * Nη)
        ih = rem_k ÷ Nη
        is = (rem_k % Nη) + 1
        ap, m, c, ℓ, hn, V = solve_cell(J, ia, ih, is, iθ)
        aplus_pol[J, ia, ih, is, iθ] = ap
        m_pol[J, ia, ih, is, iθ]     = m
        c_pol[J, ia, ih, is, iθ]     = c
        l_pol[J, ia, ih, is, iθ]     = ℓ
        hnext_pol[J, ia, ih, is, iθ] = hn
        V_pol[J, ia, ih, is, iθ]     = V
    end
    for j in (J-1):-1:1
        Threads.@threads for k in 0:(ncells - 1)
            ia = k ÷ ((NH + 1) * Nη)
            rem_k = k % ((NH + 1) * Nη)
            ih = rem_k ÷ Nη
            is = (rem_k % Nη) + 1
            ap, m, c, ℓ, hn, V = solve_cell(j, ia, ih, is, iθ)
            aplus_pol[j, ia, ih, is, iθ] = ap
            m_pol[j, ia, ih, is, iθ]     = m
            c_pol[j, ia, ih, is, iθ]     = c
            l_pol[j, ia, ih, is, iθ]     = ℓ
            hnext_pol[j, ia, ih, is, iθ] = hn
            V_pol[j, ia, ih, is, iθ]     = V
        end
    end
end

function solve_household!()
    for iθ in 1:Nθ
        solve_household_for_type(iθ)
    end
end

# ─── Ergodic dist of η ───────────────────────────────────────────────────────
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
function forward_distribution!()
    Φ .= 0.0
    ih_init_l, ih_init_r, φh_init = health_interp(h_init)
    for iθ in 1:Nθ
        for is in 1:Nη
            Φ[1, 0, ih_init_l, is, iθ] += φ1_share[iθ] * π_η_erg[is] * φh_init
            Φ[1, 0, ih_init_r, is, iθ] += φ1_share[iθ] * π_η_erg[is] * (1.0 - φh_init)
        end
    end
    # PDF eq. (2): φ_{j+1}(θ) = (ψ̄_{j+1}(θ)/(1+n_p)) · φ_j(θ). The (1+n_p)
    # divisor reflects population growth in the stationary per-cohort-mass
    # convention (PDF §3.6): each new birth cohort is (1+n_p)× the previous,
    # so existing cohorts' relative mass shrinks by that factor at each age step.
    for j in 1:(J-1)
        for ia in 0:NA, ih in 0:NH, is in 1:Nη, iθ in 1:Nθ
            mass = Φ[j, ia, ih, is, iθ]
            if mass < 1e-18; continue; end
            a_prime = aplus_pol[j, ia, ih, is, iθ]
            h_n     = hnext_pol[j, ia, ih, is, iθ]
            ial, iar, φ_a = asset_interp(a_prime)
            ihl, ihr, φ_h = health_interp(h_n)
            ψ_next = survival(j + 1, h_n)
            mass_alive = mass * ψ_next / (1.0 + n_p)
            for is_p in 1:Nη
                πη = π_η[is, is_p]
                Φ[j+1, ial, ihl, is_p, iθ] += mass_alive * πη * φ_a       * φ_h
                Φ[j+1, ial, ihr, is_p, iθ] += mass_alive * πη * φ_a       * (1.0 - φ_h)
                Φ[j+1, iar, ihl, is_p, iθ] += mass_alive * πη * (1.0 - φ_a) * φ_h
                Φ[j+1, iar, ihr, is_p, iθ] += mass_alive * πη * (1.0 - φ_a) * (1.0 - φ_h)
            end
        end
    end
end

# ============================================================================
# GE-specific machinery
# ============================================================================

# Working-age and retired mass (PDF eq. 19, 20 — used by pension).
function compute_population!()
    global N_W_now, N_R_now
    N_W = 0.0
    N_R = 0.0
    for j in 1:J, iθ in 1:Nθ
        mass = sum(Φ[j, :, :, :, iθ])
        if j < j_R
            N_W += mass
        else
            N_R += mass
        end
    end
    N_W_now = N_W
    N_R_now = N_R
end

# Aggregate (PDF §3.6 and eq. 25).
#   A_dom = ∫ a dμ            (current-asset stock, eq. 23)
#   L_eff = ∫_{j<j_R} ν_j ℓ dμ (efficiency labor, eq. 22)
#   C, M = ∫ c dμ, ∫ m dμ
#   Λ_void = ∫ (1 − ψ_{j+1}(h')) a' dμ  (deceased end-of-period assets, eq. 25)
function aggregate_all()
    A_dom = 0.0
    L_eff = 0.0
    C     = 0.0
    M     = 0.0
    Λvoid = 0.0
    for j in 1:J, ia in 0:NA, ih in 0:NH, is in 1:Nη, iθ in 1:Nθ
        mass = Φ[j, ia, ih, is, iθ]
        if mass < 1e-18; continue; end
        a_now = a_grid[ia]
        h_now = h_grid[ih]
        η_now = η_grid[is]
        A_dom += mass * a_now
        C     += mass * c_pol[j, ia, ih, is, iθ]
        M     += mass * m_pol[j, ia, ih, is, iθ]
        if j < j_R
            ν_j = productivity(j, h_now, η_now, iθ)
            ℓ   = l_pol[j, ia, ih, is, iθ]
            L_eff += mass * ν_j * ℓ
        end
        h_n     = hnext_pol[j, ia, ih, is, iθ]
        ψ_next  = survival(j + 1, h_n)
        a_prime = aplus_pol[j, ia, ih, is, iθ]
        Λvoid += mass * (1.0 - ψ_next) * a_prime
    end
    return A_dom, L_eff, C, M, Λvoid
end

# Firm FOCs (PDF eq. 11, 12).
function update_prices!(K::Float64, L::Float64)
    global r_now, w_now, rn_now, wn_now
    r_now  = α * A_TFP * (K / L)^(α - 1.0) - δ_cap
    w_now  = (1.0 - α) * A_TFP * (K / L)^α
    rn_now = r_now * (1.0 - τk)
    wn_now = w_now * (1.0 - τw - τp_now)
end

# Pension formula and contribution rate (PDF eq. 19, 20).
# No one-period lag — pen uses current wL (addressing M7).
function update_pension_taxes!(L_eff::Float64)
    global τp_now, pen_now, wn_now
    if N_W_now > 0.0
        τp_now  = κ_rep * N_R_now / N_W_now
        pen_now = κ_rep * w_now * L_eff / N_W_now
    end
    wn_now = w_now * (1.0 - τw - τp_now)
end

# Debt-residual closure — PDF eq. 17, corrected for population growth.
# The PDF writes rB = τc·C + τw·wL + τk·rK + τm·M − G, but this misses two
# effects under per-capita stationary normalization with n_p > 0:
#   (a) gov must issue new debt at rate n_p·B each period to keep B per-capita
#       constant — so net debt service is (r − n_p)·B, not r·B.
#   (b) τ^k effectively applies to all household interest income (rn enters
#       the household budget on the full A_dom, not just K), so tax revenue
#       should reflect that.
# Under the assumption that household budgets use rn on all of A_dom (PDF
# Section 3.7), Walras-closing requires B = primary / (rn − n_p) with primary
# defined as in PDF eq. 17 (no τk·rB on the surplus side). See discrepancy
# report §"GE-block Phase-3 status" for the derivation.
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

    println("INITIAL GE  (K₀=$(K_init), L₀=$(L_init), damp=$(damp_ge), tol=$(sig_ge))")
    println("iter   K        L        K/L      r(5y)    w        τp       DIFF/Y")
    println("─────  ───────  ───────  ───────  ───────  ───────  ───────  ─────────────")

    for iter in 1:itermax_ge
        update_prices!(K, L)

        # Bootstrap on iter 1: τp and pen carry their initial defaults until the
        # first forward distribution. update_pension_taxes! after that refreshes.
        if iter == 1
            wn_now = w_now * (1.0 - τw - τp_now)
        else
            update_pension_taxes!(L)
        end

        solve_household!()
        forward_distribution!()
        compute_population!()
        update_pension_taxes!(L)            # refresh with actual mass

        A_dom, L_new, C, M, Λvoid = aggregate_all()
        Y = A_TFP * K^α * L^(1.0 - α)
        compute_debt!(C, L, K, M, Y)
        K_target = A_dom - B_debt_now

        K_upd = damp_ge * K_target + (1.0 - damp_ge) * K
        L_upd = damp_ge * L_new   + (1.0 - damp_ge) * L
        # Positivity floor: under policy shocks the early-iter K_target can
        # overshoot negative; clamp to a small positive value so the firm
        # FOC (K/L)^(α-1) stays real-valued. Convergence is unaffected once
        # the equilibrium K is positive (which it always is in this model).
        K_upd = max(K_upd, 0.5)
        L_upd = max(L_upd, 0.5)

        G = gy * Y
        # Goods market — corrected PDF eq. 24 for per-capita stationary with
        # n_p > 0:  Y = C + M + (δ + n_p)·K + G + Λ_void.  The PDF writes
        # just δ·K; under per-capita normalization the additional n_p·K is the
        # gross-investment growth wedge needed to keep K per-capita constant.
        # See discrepancy report §"GE-block Phase-3 status" for the derivation.
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

# ─── Welfare object (PDF eq. 58) ─────────────────────────────────────────────
function welfare_at_birth()
    ih_l, ih_r, φh = health_interp(h_init)
    W = zeros(Nθ)
    for iθ in 1:Nθ
        s = 0.0
        for is in 1:Nη
            V_l = V_pol[1, 0, ih_l, is, iθ]
            V_r = V_pol[1, 0, ih_r, is, iθ]
            V_  = φh * V_l + (1.0 - φh) * V_r
            s += π_η_erg[is] * V_
        end
        W[iθ] = s
    end
    return W
end

# ============================================================================
# Diagnostics (carried over from household_problem.jl)
# ============================================================================

function is_corner_cell(j::Int, ia::Int, ih::Int, is::Int, iθ::Int)::Bool
    ap = aplus_pol[j, ia, ih, is, iθ]
    if ap <= a_l + 1e-9
        return true
    end
    a_now = a_grid[ia]; h_now = h_grid[ih]; η_now = η_grid[is]
    m_chosen = m_pol[j, ia, ih, is, iθ]
    X = available_resources(a_now, h_now, η_now, iθ, j)
    avail_after_m = X - (1.0 + τm) * m_chosen
    a_hi = max(avail_after_m - 1e-6, a_l)
    return ap >= a_hi - 1e-6
end

function euler_residual_stats()
    residuals = Float64[]
    for j in 1:(J-1), iθ in 1:Nθ
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            if is_corner_cell(j, ia, ih, is, iθ); continue; end
            ap = aplus_pol[j, ia, ih, is, iθ]
            mm = m_pol[j, ia, ih, is, iθ]
            h_now = h_grid[ih]
            r = euler_residual(ap, j, ia, ih, is, iθ, mm, h_now)
            c_now = c_pol[j, ia, ih, is, iθ]
            ℓ_now = l_pol[j, ia, ih, is, iθ]
            uc = marginal_utility_c(c_now, ℓ_now, h_now)
            if uc > 1e-12
                push!(residuals, abs(r) / uc)
            end
        end
    end
    return residuals
end

function m_positivity_by_age()
    out = zeros(J, Nθ)
    for j in 1:J, iθ in 1:Nθ
        mass_total = 0.0
        mass_pos   = 0.0
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            w = Φ[j, ia, ih, is, iθ]
            mass_total += w
            if m_pol[j, ia, ih, is, iθ] > m_min * 1.0001
                mass_pos += w
            end
        end
        out[j, iθ] = mass_total > 0.0 ? mass_pos / mass_total : 0.0
    end
    return out
end

function cohort_means()
    cm_c = zeros(J, Nθ)
    cm_l = zeros(J, Nθ)
    cm_a = zeros(J, Nθ)
    cm_m = zeros(J, Nθ)
    cm_h = zeros(J, Nθ)
    for j in 1:J, iθ in 1:Nθ
        wsum = 0.0
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            w = Φ[j, ia, ih, is, iθ]
            if w < 1e-18; continue; end
            wsum += w
            cm_c[j, iθ] += w * c_pol[j, ia, ih, is, iθ]
            cm_l[j, iθ] += w * l_pol[j, ia, ih, is, iθ]
            cm_a[j, iθ] += w * a_grid[ia]
            cm_m[j, iθ] += w * m_pol[j, ia, ih, is, iθ]
            cm_h[j, iθ] += w * h_grid[ih]
        end
        if wsum > 0.0
            cm_c[j, iθ] /= wsum; cm_l[j, iθ] /= wsum
            cm_a[j, iθ] /= wsum; cm_m[j, iθ] /= wsum
            cm_h[j, iθ] /= wsum
        end
    end
    return cm_c, cm_l, cm_a, cm_m, cm_h
end

# ─── GE summary ──────────────────────────────────────────────────────────────
function print_ge_summary(hist, A_dom, L_new, C, M, Λvoid, Y, K, L, W)
    println("\n══════════════════════════════════════════════════════════════")
    println(" Stationary GE (DraftApril.pdf model)")
    println("══════════════════════════════════════════════════════════════")
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
    @printf "  N^W      = %.5f\n"  N_W_now
    @printf "  N^R      = %.5f\n"  N_R_now
    @printf "  N^R/N^W  = %.5f\n"  N_R_now/N_W_now
    println()
    @printf "  Goods market residual: (Y - C - M - (δ+n_p)K - G - Λ_void)/Y = %+.6e\n"  hist.DIFF[end]
    @printf "  Gov BC check (corrected closure (rn-n_p)B = primary): %+.6e\n"  ((τc*C + τw*w_now*L + τk*r_now*K + τm*M - gy*Y - (rn_now - n_p)*B_debt_now) / Y)
    @printf "  PDF eq.17 check (rB = primary, unadjusted for n_p): %+.6e   [nonzero by design — see notes]\n"  ((τc*C + τw*w_now*L + τk*r_now*K + τm*M - gy*Y - r_now*B_debt_now) / Y)
    println()
    @printf "  Welfare object (PDF eq. 58):\n"
    @printf "    𝒲₁(θ_L = %.2f) = %.5f\n" θ_grid[1] W[1]
    @printf "    𝒲₁(θ_H = %.2f) = %.5f\n" θ_grid[2] W[2]

    # Euler residual statistics (interior cells only — corner cells excluded).
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
    open(joinpath(out_dir, "ge_lifecycle_taum20.csv"), "w") do io
        println(io, "age_period,theta_idx,theta_value,c,l,a,m,h,m_positive_share")
        for j in 1:J, iθ in 1:Nθ
            println(io, "$j,$iθ,$(θ_grid[iθ]),$(cm_c[j,iθ]),$(cm_l[j,iθ]),$(cm_a[j,iθ]),$(cm_m[j,iθ]),$(cm_h[j,iθ]),$(pos[j,iθ])")
        end
    end
    open(joinpath(out_dir, "ge_summary_taum20.csv"), "w") do io
        println(io, "metric,value")
        println(io, "K,$K"); println(io, "L,$L"); println(io, "K_over_L,$(K/L))")
        println(io, "Y,$Y"); println(io, "C,$C"); println(io, "M,$M")
        println(io, "G,$(gy*Y)"); println(io, "deltaK,$(δ_cap*K)"); println(io, "Lambda_void,$Λvoid")
        println(io, "r_5yr,$(r_now)"); println(io, "w,$(w_now)")
        println(io, "taup,$(τp_now)"); println(io, "pen,$(pen_now)")
        println(io, "B_debt,$(B_debt_now)"); println(io, "A_dom,$A_dom")
        println(io, "W1_theta_L,$(W[1])"); println(io, "W1_theta_H,$(W[2])")
        println(io, "K_over_Y_5yr,$(K/Y)"); println(io, "C_over_Y,$(C/Y)")
        println(io, "M_over_Y,$(M/Y)")
    end
    open(joinpath(out_dir, "ge_history_taum20.csv"), "w") do io
        println(io, "iter,K,L,r,w,taup,DIFF_over_Y")
        for k in eachindex(hist.iter)
            println(io, "$(hist.iter[k]),$(hist.K[k]),$(hist.L[k]),$(hist.r[k]),$(hist.w[k]),$(hist.τp[k]),$(hist.DIFF[k])")
        end
    end
    println("  Wrote ge_lifecycle_taum20.csv, ge_summary_taum20.csv, ge_history_taum20.csv  (under $(out_dir))")
end

# ─── Plots ───────────────────────────────────────────────────────────────────
ages_vec() = 15 .+ 5 .* (1:J)

function plot_lifecycle_profiles()
    cm_c, cm_l, cm_a, cm_m, cm_h = cohort_means()
    ages = ages_vec()
    p_c = plot(ages, cm_c[:,1]; label="θ_L", lw=2, color=:steelblue, ylabel="Consumption", xlabel="Age", legend=:topleft)
    plot!(p_c, ages, cm_c[:,2]; label="θ_H", lw=2, color=:firebrick)
    p_l = plot(ages[1:j_R-1], cm_l[1:j_R-1,1]; label="θ_L", lw=2, color=:steelblue, ylabel="Labor ℓ", xlabel="Age", legend=:topright)
    plot!(p_l, ages[1:j_R-1], cm_l[1:j_R-1,2]; label="θ_H", lw=2, color=:firebrick)
    p_a = plot(ages, cm_a[:,1]; label="θ_L", lw=2, color=:steelblue, ylabel="Assets a", xlabel="Age", legend=:topleft)
    plot!(p_a, ages, cm_a[:,2]; label="θ_H", lw=2, color=:firebrick)
    p_m = plot(ages, cm_m[:,1]; label="θ_L", lw=2, color=:steelblue, ylabel="Medical m", xlabel="Age", legend=:topleft)
    plot!(p_m, ages, cm_m[:,2]; label="θ_H", lw=2, color=:firebrick)
    p_h = plot(ages, cm_h[:,1]; label="θ_L", lw=2, color=:steelblue, ylabel="Health h", xlabel="Age", ylim=(0,1.05), legend=:bottomleft)
    plot!(p_h, ages, cm_h[:,2]; label="θ_H", lw=2, color=:firebrick)
    mass = [sum(Φ[j,:,:,:,iθ]) for j in 1:J, iθ in 1:Nθ]
    for iθ in 1:Nθ; mass[:,iθ] ./= mass[1,iθ]; end
    p_n = plot(ages, mass[:,1]; label="θ_L", lw=2, color=:steelblue, ylabel="Surv. mass / newborn", xlabel="Age", ylim=(0,1.05), legend=:bottomleft)
    plot!(p_n, ages, mass[:,2]; label="θ_H", lw=2, color=:firebrick)
    return plot(p_c, p_l, p_a, p_m, p_h, p_n; layout=(2,3), size=(1100, 720),
                plot_title="GE life-cycle profiles (mass-weighted)")
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
                plot_title="GE convergence")
end

function plot_aggregate_identity(C, M, K, Y, Λvoid)
    G = gy * Y
    parts = [C, M, δ_cap*K, G, Λvoid]
    labs  = ["C", "M", "δK", "G", "Λ_void"]
    colors= [:steelblue, :firebrick, :forestgreen, :darkorange, :purple]
    p = bar(labs, parts; color=colors, ylabel="goods, units of Y",
            title=@sprintf("Y = %.4f  vs  C+M+δK+G+Λ_void = %.4f", Y, sum(parts)),
            label="")
    hline!(p, [Y]; lw=2, color=:black, label="Y")
    return p
end

function plot_tax_revenue(C, L, K, M, Y)
    G = gy * Y
    rev_c = τc * C
    rev_w = τw * w_now * L
    rev_k = τk * r_now * K
    rev_m = τm * M
    debt_service = r_now * B_debt_now
    parts = [rev_c, rev_w, rev_k, rev_m]
    labs  = ["τc·C", "τw·wL", "τk·rK", "τm·M"]
    p = bar(labs, parts; color=:steelblue, ylabel="revenue",
            title=@sprintf("Tax revenue  vs  G=%.4f  +  rB=%.4f", G, debt_service),
            label="revenue")
    hline!(p, [G + debt_service]; lw=2, ls=:dash, color=:firebrick, label="G + rB")
    return p
end

function plot_m_positivity()
    pos = m_positivity_by_age()
    ages = ages_vec()
    p = bar(ages .- 1.0, pos[:,1]; label="θ_L", color=:steelblue, bar_width=2.0,
            xlabel="Age", ylabel="P(m* > 0)", ylim=(0, 1.05),
            title="Fraction of mass with m* > 0  (GE)", legend=:bottomright)
    bar!(p, ages .+ 1.0, pos[:,2]; label="θ_H", color=:firebrick, bar_width=2.0)
    return p
end

function plot_euler_residuals()
    res = euler_residual_stats()
    rs = log10.(max.(res, 1e-16))
    mean_r = round(mean(rs); digits=2); max_r = round(maximum(rs); digits=2)
    p = histogram(rs; bins=50, color=:steelblue, alpha=0.7,
                  xlabel="log₁₀ |r| / u_c", ylabel="count",
                  title="Euler residuals (interior cells)  mean=$mean_r max=$max_r",
                  label="")
    vline!(p, [-4.0]; lw=2, color=:darkred, label="target (-4)")
    return p
end

function make_audit_plots(hist::GEHistory, C, M, K, Y, Λvoid, L)
    plot_dir = joinpath(@__DIR__, "plots_taum20")
    isdir(plot_dir) || mkpath(plot_dir)
    savefig(plot_lifecycle_profiles(),       joinpath(plot_dir, "ge_01_lifecycle.png"))
    savefig(plot_ge_convergence(hist),       joinpath(plot_dir, "ge_02_convergence.png"))
    savefig(plot_aggregate_identity(C, M, K, Y, Λvoid), joinpath(plot_dir, "ge_03_aggregate_identity.png"))
    savefig(plot_tax_revenue(C, L, K, M, Y), joinpath(plot_dir, "ge_04_tax_revenue.png"))
    savefig(plot_m_positivity(),             joinpath(plot_dir, "ge_05_m_positivity.png"))
    savefig(plot_euler_residuals(),          joinpath(plot_dir, "ge_06_euler_residuals.png"))
    println("  Wrote 6 GE audit plots to $(plot_dir)/ge_*.png")
end

# ============================================================================
# Main
# ============================================================================
function main()
    println("Initializing grids …")
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
    println("\nGenerating GE audit plots …")
    make_audit_plots(hist, C, M, K, Y, Λvoid, L)
end

main()
