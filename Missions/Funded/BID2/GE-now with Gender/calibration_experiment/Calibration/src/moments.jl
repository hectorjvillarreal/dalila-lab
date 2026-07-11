################################################################################
#  moments.jl
#
#  Six simulated moments computed directly from (Φ, policy arrays) — no panel
#  sampling, no Monte Carlo noise. Each moment is the population value the
#  paper's panel-sim approach (N_sim = 50,000 per type) would converge to.
#
#  Moment ↔ parameter map (matches modelwithgender.tex §4.2.3 table, minus
#  K/Y which we drop in PE):
#
#    Parameter   Moment (model object)                              Notation
#    ──────────  ─────────────────────────────────────────────────  ──────────
#    Ψ           Φ-weighted mean of l_pol over (j<jR, ig=1)         m_hours_pa_males
#    Ξ           VSL at reference age (USD)                          m_vsl_usd
#    ξ           cross-sectional income elasticity of m              m_cross_elast
#    H̄_0         Φ-weighted mean of m for j ∈ {2,3} (age 25–35)      m_mean_m_25_35
#    h^slope     OLS slope of log(mean m by age) on age, j ∈ 2..11   m_logslope_m_25_75
#    ζ_h         mean over working ages of within-age income         m_within_age_elast
#                elasticity of m
#
#  Permanent income per state (used by the income elasticities):
#    working age (j < jR): y = w·ν_j(h, η; g, θ) · ℓ_pol         (gross labor income)
#    retiree   (j ≥ jR):   y = pen_flow                          (constant)
#
#  Cells with m ≤ M_EPS are excluded from log-elasticities (log undefined);
#  cells with Φ < Φ_EPS or y ≤ Y_EPS are also dropped.
#
#  Requires pe_solver_for_smm.jl + vsl.jl included.
################################################################################

const M_EPS = 1e-6
const Φ_EPS = 1e-18
const Y_EPS = 1e-9

# ─── Helper: weighted-OLS slope of y on x ────────────────────────────────────
"""
    weighted_ols_slope(x, y, w) -> Float64

Standard weighted least-squares slope β̂ = Σw·(x-x̄)(y-ȳ) / Σw·(x-x̄)²
with weighted means. Returns NaN if denominator is zero.
"""
function weighted_ols_slope(x::AbstractVector{Float64},
                             y::AbstractVector{Float64},
                             w::AbstractVector{Float64})
    @assert length(x) == length(y) == length(w)
    W = sum(w)
    W > 0 || return NaN
    x̄ = sum(w .* x) / W
    ȳ = sum(w .* y) / W
    num = 0.0; den = 0.0
    for i in eachindex(x)
        dx = x[i] - x̄
        num += w[i] * dx * (y[i] - ȳ)
        den += w[i] * dx * dx
    end
    return den > 0 ? num / den : NaN
end

# ─── Permanent income (per cell, working OR retired) ────────────────────────
function permanent_income(j::Int, h::Float64, η::Float64,
                          ig::Int, iθ::Int, ℓ::Float64)
    if j < j_R
        return w_price[] * productivity(j, h, η, ig, iθ) * ℓ
    else
        return pen_flow[]
    end
end

# ─── Moment 1: hours of prime-age males ─────────────────────────────────────
function m_hours_pa_males()
    num = 0.0; den = 0.0
    for j in 1:(j_R-1), iθ in 1:Nθ
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            w = Φ[j, 1, ia, ih, is, iθ]   # ig = 1 (male)
            w < Φ_EPS && continue
            num += w * l_pol[j, 1, ia, ih, is, iθ]
            den += w
        end
    end
    return den > 0 ? num / den : NaN
end

# ─── Moment 2: VSL (delegates to vsl.jl) ────────────────────────────────────
m_vsl_usd(usd_scale) = vsl_at(usd_scale).vsl_usd

# ─── Moment 3: cross-sectional income elasticity of medical spending ────────
# Pooled weighted OLS of log m on log y across all cells with m > M_EPS.
function m_cross_elast_m_income()
    logm = Float64[]; logy = Float64[]; ws = Float64[]
    for j in 1:J, ig in 1:Ng, iθ in 1:Nθ
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            w = Φ[j, ig, ia, ih, is, iθ]
            w < Φ_EPS && continue
            m = m_pol[j, ig, ia, ih, is, iθ]
            m > M_EPS || continue
            ℓ = l_pol[j, ig, ia, ih, is, iθ]
            y = permanent_income(j, h_grid[ih], η_grid[is], ig, iθ, ℓ)
            y > Y_EPS || continue
            push!(logm, log(m)); push!(logy, log(y)); push!(ws, w)
        end
    end
    isempty(logm) && return NaN
    return weighted_ols_slope(logy, logm, ws)
end

# ─── Moment 4: mean m, age 25–35 (j = 2, 3) ─────────────────────────────────
function m_mean_m_age_25_35(; age_range::UnitRange{Int}=2:3)
    num = 0.0; den = 0.0
    for j in age_range, ig in 1:Ng, iθ in 1:Nθ
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            w = Φ[j, ig, ia, ih, is, iθ]
            w < Φ_EPS && continue
            num += w * m_pol[j, ig, ia, ih, is, iθ]
            den += w
        end
    end
    return den > 0 ? num / den : NaN
end

# Mean of m at age j, mass-weighted over all (g, θ, a, h, η).
function _mean_m_at_age(j::Int)
    num = 0.0; den = 0.0
    for ig in 1:Ng, iθ in 1:Nθ
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            w = Φ[j, ig, ia, ih, is, iθ]
            w < Φ_EPS && continue
            num += w * m_pol[j, ig, ia, ih, is, iθ]
            den += w
        end
    end
    return den > 0 ? num / den : NaN
end

# ─── Moment 5: log-slope of mean m by age, j = 2..11 (ages 25–70) ───────────
# Paper says age 25–75 but in the J=17 grid j=11 corresponds to age 70 and
# j=12 to age 75. Configurable via age_range kwarg.
function m_logslope_m_25_75(; age_range::UnitRange{Int}=2:12)
    js = collect(age_range)
    means = [_mean_m_at_age(j) for j in js]
    # drop ages with NaN or m ≤ M_EPS
    keep = [isfinite(m) && m > M_EPS for m in means]
    sum(keep) >= 2 || return NaN
    x = Float64.(js[keep])
    y = log.(means[keep])
    w = ones(length(x))      # equal weight across age bins (paper convention)
    return weighted_ols_slope(x, y, w)
end

# ─── Moment 6: within-age income elasticity, averaged over working ages ─────
function m_within_age_elast(; working_ages::UnitRange{Int}=1:(j_R-1))
    slopes = Float64[]
    age_masses = Float64[]
    for j in working_ages
        logm = Float64[]; logy = Float64[]; ws = Float64[]
        for ig in 1:Ng, iθ in 1:Nθ
            for ia in 0:NA, ih in 0:NH, is in 1:Nη
                w = Φ[j, ig, ia, ih, is, iθ]
                w < Φ_EPS && continue
                m = m_pol[j, ig, ia, ih, is, iθ]
                m > M_EPS || continue
                ℓ = l_pol[j, ig, ia, ih, is, iθ]
                y = permanent_income(j, h_grid[ih], η_grid[is], ig, iθ, ℓ)
                y > Y_EPS || continue
                push!(logm, log(m)); push!(logy, log(y)); push!(ws, w)
            end
        end
        if !isempty(logm) && sum(ws) > 0
            β̂ = weighted_ols_slope(logy, logm, ws)
            if isfinite(β̂)
                push!(slopes, β̂); push!(age_masses, sum(ws))
            end
        end
    end
    isempty(slopes) && return NaN
    # Mass-weighted average over ages
    W = sum(age_masses)
    return W > 0 ? sum(slopes .* age_masses) / W : NaN
end

# ─── Top-level: compute all six moments in the order expected by targets.csv ─
"""
    compute_moments(usd_scale) -> NamedTuple

Returns the six simulated moments as a NamedTuple with the same field names
as `io.targets.names`:
    (hours_pa_males, vsl_usd, cross_elast_m, mean_m_age_25_35,
     logslope_m_25_75, within_age_elast)

`usd_scale` must be the NamedTuple loaded from `usd_scale.csv` (needed by VSL).
"""
function compute_moments(usd_scale)
    return (; hours_pa_males   = m_hours_pa_males(),
              vsl_usd          = m_vsl_usd(usd_scale),
              cross_elast_m    = m_cross_elast_m_income(),
              mean_m_age_25_35 = m_mean_m_age_25_35(),
              logslope_m_25_75 = m_logslope_m_25_75(),
              within_age_elast = m_within_age_elast())
end

# Reorder a moments NamedTuple to a vector matching the order in targets.names.
function moments_vector(m::NamedTuple, target_names::Vector{String})
    syms = Symbol.(target_names)
    return [getfield(m, s) for s in syms]
end
