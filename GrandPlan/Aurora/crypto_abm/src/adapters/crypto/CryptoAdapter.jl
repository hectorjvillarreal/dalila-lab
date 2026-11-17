"""
    CryptoAdapter

Bitcoin adapter for the Aurora mechanism laboratory (design note B0 v1.2, §3.1, §4).
B1 classes: conviction holders, momentum traders, leveraged perp traders, noise order flow;
the liquidity provider lives in the core. Perp and spot trade at one price (instant
arbitrage assumed; note §2). Units: holdings and orders in units of BTC as a share of the
float; cash in the numéraire with p₀ = 1.

Firewall (note §0): nothing here reads or writes the crypto regime board.
"""
module CryptoAdapter

using Random, Statistics
using ..ABMCore
import ..ABMCore: ordinary_flow!, forced_flow!, settle!, substep_end!, n_constrained,
                  units_held, cash_held, reset_counters!

export Params, build_world, Conviction, Momentum, Leveraged, NoiseFlow, load_coinbase_csv

# ----------------------------------------------------------------------------
# Parameters (note §4; initial search ranges, not estimates)
# ----------------------------------------------------------------------------
Base.@kwdef struct Params
    K::Int = 24
    # class shares of the float
    w_c::Float64 = 0.50
    w_m::Float64 = 0.20
    w_l::Float64 = 0.10
    N_c::Int = 200
    N_m::Int = 100
    N_l::Int = 200
    # conviction holders
    D_median::Float64 = 0.25
    s_D::Float64 = 0.50
    sell_frac::Float64 = 0.50
    reentry::Float64 = 0.02          # share of the gap bought back per sub-step once drawdown < D/2
    # momentum traders
    β::Float64 = 1.5
    h_min::Int = 3
    h_max::Int = 60
    θ::Float64 = 1 / 24              # adjustment speed per sub-step
    # leveraged perp traders
    L_median::Float64 = 8.0
    s_L::Float64 = 0.50
    m0::Float64 = 0.01
    m1::Float64 = 0.0                # margin slope on σ̂ (per-sub-step units)
    close_hazard::Float64 = 1 / (24 * 5)
    reopen_delay::Int = 24
    β_l::Float64 = 1.0
    funding_c::Float64 = 0.0005      # funding per 8h per unit of normalised long−short imbalance
    funding_max::Float64 = 0.0075
    # noise and market
    σ_ε::Float64 = 0.01              # daily noise order flow, share of float (ε_s ~ N(0, 1/K))
    λ0::Float64 = 2.0
    κ::Float64 = 0.5
    λmax_mult::Float64 = 4.0
    φ::Float64 = 0.3
    ρ::Float64 = 0.2
    σbar::Float64 = 0.005            # replaced by the hourly-snapshot constant (targets/)
    impact::Symbol = :linear         # :sqrt = square-root impact alternative (note §6.3)
    q0::Float64 = 0.002              # reference flow for :sqrt (≈ per-sub-step noise scale), share of float
end

# ----------------------------------------------------------------------------
# Conviction holders: hold; sell a fraction once drawdown from own peak ≥ D_i
# (fires once per crossing: sets a flag reset only on full re-entry)
# ----------------------------------------------------------------------------
mutable struct Conviction <: AgentClass
    hold::Vector{Float64}
    cash::Vector{Float64}
    target::Vector{Float64}
    D::Vector{Float64}
    peak::Vector{Float64}
    flagged::BitVector
    pending::Vector{Float64}
    sell_frac::Float64
    reentry::Float64
    sold_units::Float64     # counter (forced sales), for diagnostics
end
function Conviction(p::Params, rng)
    n = p.N_c
    h = fill(p.w_c / n, n)
    D = exp.(log(p.D_median) .+ p.s_D .* randn(rng, n))
    Conviction(copy(h), zeros(n), copy(h), clamp.(D, 0.02, 0.95), ones(n), falses(n), zeros(n),
               p.sell_frac, p.reentry, 0.0)
end
function ordinary_flow!(c::Conviction, ctx)
    s = 0.0
    @inbounds for i in eachindex(c.hold)
        if c.flagged[i] && (1.0 - ctx.p / c.peak[i]) < c.D[i] / 2
            q = c.reentry * (c.target[i] - c.hold[i])
            c.pending[i] = q; s += q
        else
            c.pending[i] = 0.0
        end
    end
    s
end
function forced_flow!(c::Conviction, ctx)
    s = 0.0
    @inbounds for i in eachindex(c.hold)
        c.pending[i] = 0.0
        if !c.flagged[i] && (1.0 - ctx.p / c.peak[i]) >= c.D[i]
            q = -c.sell_frac * c.hold[i]
            c.pending[i] = q; s += q
            c.flagged[i] = true
            c.sold_units -= q
        end
    end
    s
end
function settle!(c::Conviction, p, ctx)
    @inbounds for i in eachindex(c.hold)
        q = c.pending[i]
        if q != 0.0
            c.hold[i] += q; c.cash[i] -= q * p; c.pending[i] = 0.0
        end
    end
    nothing
end
function substep_end!(c::Conviction, ctx)
    p = ctx.p
    @inbounds for i in eachindex(c.hold)
        if c.flagged[i]
            if c.hold[i] >= 0.999 * c.target[i]
                c.flagged[i] = false; c.peak[i] = p
            end
        else
            c.peak[i] = max(c.peak[i], p)
        end
    end
    nothing
end
n_constrained(c::Conviction) = length(c.hold)
units_held(c::Conviction) = sum(c.hold)
cash_held(c::Conviction) = sum(c.cash)
reset_counters!(c::Conviction) = (c.sold_units = 0.0; nothing)

# ----------------------------------------------------------------------------
# Momentum traders: target = (w_m/N_m)·tanh(β·z_h), z_h = h-day log return / (σday·√h)
# ----------------------------------------------------------------------------
mutable struct Momentum <: AgentClass
    q::Vector{Float64}
    cash::Vector{Float64}
    h::Vector{Int}
    cap::Float64
    β::Float64
    θ::Float64
    pending::Vector{Float64}
end
function Momentum(p::Params, rng)
    n = p.N_m
    Momentum(zeros(n), zeros(n), rand(rng, p.h_min:p.h_max, n), p.w_m / n, p.β, p.θ, zeros(n))
end
@inline function _trend(ctx, h)
    d = ctx.day
    d <= h && return 0.0
    (log(ctx.p) - ctx.logcloses[d-h]) / (ctx.σday * sqrt(h))
end
function ordinary_flow!(c::Momentum, ctx)
    s = 0.0
    @inbounds for i in eachindex(c.q)
        tgt = c.cap * tanh(c.β * _trend(ctx, c.h[i]))
        q = c.θ * (tgt - c.q[i])
        c.pending[i] = q; s += q
    end
    s
end
function forced_flow!(c::Momentum, ctx)
    fill!(c.pending, 0.0); 0.0
end
function settle!(c::Momentum, p, ctx)
    @inbounds for i in eachindex(c.q)
        q = c.pending[i]
        if q != 0.0
            c.q[i] += q; c.cash[i] -= q * p; c.pending[i] = 0.0
        end
    end
    nothing
end
substep_end!(c::Momentum, ctx) = nothing
n_constrained(c::Momentum) = 0
units_held(c::Momentum) = sum(c.q)
cash_held(c::Momentum) = sum(c.cash)

# ----------------------------------------------------------------------------
# Leveraged perp traders: open with equity E injected (|q| = w_l/N_l), leverage L_i,
# direction from a trend signal plus noise; liquidated when equity < m(σ̂)·|q|·p;
# random closes; pay/receive funding every K/3 sub-steps against the liquidity provider.
# ----------------------------------------------------------------------------
mutable struct Leveraged <: AgentClass
    q::Vector{Float64}
    cash::Vector{Float64}
    L::Vector{Float64}
    h::Vector{Int}
    open::BitVector
    countdown::Vector{Int}
    pending::Vector{Float64}
    closing::BitVector        # position closes at the next settle (withdraw equity after)
    size::Float64
    m0::Float64
    m1::Float64
    close_hazard::Float64
    reopen_delay::Int
    β_l::Float64
    funding_c::Float64
    funding_max::Float64
    funding_every::Int
    liq_units::Float64        # counter
    liq_count::Int
end
function Leveraged(p::Params, rng)
    n = p.N_l
    L = clamp.(exp.(log(p.L_median) .+ p.s_L .* randn(rng, n)), 1.1, 100.0)
    Leveraged(zeros(n), zeros(n), L, rand(rng, p.h_min:p.h_max, n), falses(n),
              rand(rng, 0:p.reopen_delay, n), zeros(n), falses(n), p.w_l / n,
              p.m0, p.m1, p.close_hazard, p.reopen_delay, p.β_l, p.funding_c, p.funding_max,
              max(1, p.K ÷ 3), 0.0, 0)
end
@inline _equity(c::Leveraged, i, p) = c.cash[i] + c.q[i] * p
@inline _margin(c::Leveraged, σ) = c.m0 + c.m1 * σ
function ordinary_flow!(c::Leveraged, ctx)
    s = 0.0
    @inbounds for i in eachindex(c.q)
        c.pending[i] = 0.0
        if c.open[i]
            if rand(ctx.rng) < c.close_hazard
                c.pending[i] = -c.q[i]; c.closing[i] = true
                s -= c.q[i]
            end
        elseif c.countdown[i] <= 0
            sig = c.β_l * _trend(ctx, c.h[i]) + randn(ctx.rng)
            d = sig >= 0 ? 1.0 : -1.0
            E = c.size * ctx.p / c.L[i]          # equity injected so that |q| = size
            c.cash[i] += E; ctx.ledger.cash_in += E
            c.pending[i] = d * c.size; c.open[i] = true
            s += d * c.size
        end
    end
    s
end
function forced_flow!(c::Leveraged, ctx)
    s = 0.0
    p = ctx.p
    mreq = _margin(c, ctx.σhat)
    @inbounds for i in eachindex(c.q)
        c.pending[i] = 0.0
        if c.open[i] && !c.closing[i] && _equity(c, i, p) < mreq * abs(c.q[i]) * p
            c.pending[i] = -c.q[i]; c.closing[i] = true
            c.liq_units += abs(c.q[i]); c.liq_count += 1
            s -= c.q[i]
        end
    end
    s
end
function settle!(c::Leveraged, p, ctx)
    @inbounds for i in eachindex(c.q)
        q = c.pending[i]
        if q != 0.0
            c.q[i] += q; c.cash[i] -= q * p; c.pending[i] = 0.0
        end
        if c.closing[i] && abs(c.q[i]) < 1e-15
            c.q[i] = 0.0
            e = c.cash[i]
            if e >= 0
                ctx.ledger.cash_in -= e            # equity withdrawn
            else
                allocate_loss!(ctx.fund, -e)       # shortfall absorbed by the fund
            end
            c.cash[i] = 0.0
            c.open[i] = false; c.closing[i] = false
            c.countdown[i] = c.reopen_delay
        end
    end
    nothing
end
function substep_end!(c::Leveraged, ctx)
    @inbounds for i in eachindex(c.q)
        c.open[i] || (c.countdown[i] -= 1)
    end
    if ctx.step % c.funding_every == 0
        long = 0.0; short = 0.0
        @inbounds for i in eachindex(c.q)
            c.q[i] > 0 ? (long += c.q[i]) : (short -= c.q[i])
        end
        tot = long + short
        tot > 0 || return nothing
        rate = clamp(c.funding_c * (long - short) / tot, -c.funding_max, c.funding_max)
        p = ctx.p
        @inbounds for i in eachindex(c.q)
            if c.q[i] != 0.0
                pay = rate * c.q[i] * p
                c.cash[i] -= pay; ctx.lp.cash += pay
            end
        end
    end
    nothing
end
n_constrained(c::Leveraged) = length(c.q)
units_held(c::Leveraged) = sum(c.q)
cash_held(c::Leveraged) = sum(c.cash)
reset_counters!(c::Leveraged) = (c.liq_units = 0.0; c.liq_count = 0; nothing)

# ----------------------------------------------------------------------------
# Noise order flow: σ_ε·ε_s, ε_s ~ N(0, 1/K) (the adapter's only exogenous input)
# ----------------------------------------------------------------------------
mutable struct NoiseFlow <: AgentClass
    q::Float64
    cash::Float64
    σ::Float64
    pending::Float64
end
NoiseFlow(p::Params) = NoiseFlow(0.0, 0.0, p.σ_ε / sqrt(p.K), 0.0)
ordinary_flow!(c::NoiseFlow, ctx) = (c.pending = c.σ * randn(ctx.rng); c.pending)
forced_flow!(c::NoiseFlow, ctx) = (c.pending = 0.0; 0.0)
function settle!(c::NoiseFlow, p, ctx)
    c.q += c.pending; c.cash -= c.pending * p; c.pending = 0.0; nothing
end
substep_end!(c::NoiseFlow, ctx) = nothing
n_constrained(c::NoiseFlow) = 0
units_held(c::NoiseFlow) = c.q
cash_held(c::NoiseFlow) = c.cash

# ----------------------------------------------------------------------------
"Build a one-market world from parameters. Classes with zero share are left out."
function build_world(p::Params, rng::AbstractRNG)
    m = Market(consol(:BTC); λ0 = p.λ0, κ = p.κ, λmax = p.λmax_mult * p.λ0, σbar = p.σbar,
               φ = p.φ, ρ = p.ρ, window = p.K, impact = p.impact, q0 = p.q0)
    cls = Any[]
    p.w_c > 0 && push!(cls, Conviction(p, rng))
    p.w_m > 0 && push!(cls, Momentum(p, rng))
    p.w_l > 0 && push!(cls, Leveraged(p, rng))
    push!(cls, NoiseFlow(p))
    World(m, Tuple(cls))
end

"Read a Coinbase candle CSV written by targets/fetch_snapshot.py → (unix, low, high, open, close)."
function load_coinbase_csv(path::AbstractString)
    lines = readlines(path)
    n = length(lines) - 1
    t = Vector{Int}(undef, n); lo = similar(t, Float64); hi = similar(lo); op = similar(lo); cl = similar(lo)
    for (k, ln) in enumerate(@view lines[2:end])
        f = split(ln, ',')
        t[k] = parse(Int, f[2]); lo[k] = parse(Float64, f[3]); hi[k] = parse(Float64, f[4])
        op[k] = parse(Float64, f[5]); cl[k] = parse(Float64, f[6])
    end
    (unix = t, low = lo, high = hi, open = op, close = cl)
end

end # module
