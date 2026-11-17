"""
    ABMCore

Asset-agnostic engine core of the Aurora mechanism laboratory (design note B0 v1.2, §2).

Nothing in this module may refer to a particular asset class: a grep test
(`test/runtests.jl`, criterion 1) enforces it. Asset-specific behaviour lives in
adapters, which implement the agent-class interface below.

Objects (note §2, Cath R5):
  (a) `Instrument` with a cash-flow schedule (`consol` = no cash flows)
  (b) `Market` (log price = permanent f + transient u); several markets are allowed by
      the `World`, B1 uses one
  (c) `EventCalendar`
  (d) `Issuer` and `primary_auction` (stub, unit-tested, unused by the first adapter)
  (e) `StateConstraint` (any state variable) and state-dependent parameters
  (f) `LiquidityProvider` with inventory and cash (counterparty to every trade)
  (g) `LossFund` (loss-allocation hook) and `SimConfig.fixed_point` (:nearest only)

Clearing (note §2, R1, R2, R4b):
  ln p moves by λ_s·x_s, x_s in units of the asset as a share of the float,
  λ_s = min(λ₀·exp(κ(σ̂_s/σ̄ − 1)), λ_max), σ̂ frozen inside the cascade loop.
  (1−φ) of each move is permanent (f), φ is transient (u); between sub-steps only,
  u ← (1−ρ)·u.

Cascade loop (note §2, R3, R4): only forced orders act inside it; each constraint
fires once per crossing; each round clears as one batch; the cap is N + 1 rounds
(N = constrained agents) and a binding cap throws `CascadeCapError` (a bug, never data).
"""
module ABMCore

using Random

export Instrument, consol, Event, EventCalendar, events_at, Issuer, primary_auction,
       StateConstraint, breached, Market, LiquidityProvider, LossFund, allocate_loss!,
       Ledger, AgentClass, Ctx, SimConfig, World, PathResult, CascadeCapError,
       impact_lambda, logprice, price, simulate!,
       ordinary_flow!, forced_flow!, settle!, substep_end!, n_constrained,
       units_held, cash_held, reset_counters!

# ----------------------------------------------------------------------------
# (a) Instruments
# ----------------------------------------------------------------------------
"An instrument with a cash-flow schedule: (sub-step index, amount per unit)."
struct Instrument
    name::Symbol
    cashflows::Vector{Tuple{Int,Float64}}
end
"An instrument with no cash flows and no maturity."
consol(name::Symbol) = Instrument(name, Tuple{Int,Float64}[])

# ----------------------------------------------------------------------------
# (c) Event calendar
# ----------------------------------------------------------------------------
struct Event
    step::Int          # global sub-step index
    kind::Symbol       # e.g. :maturity, :coupon, :auction, :review, :financing_wall
    target::Int        # agent or instrument index, adapter-defined
    amount::Float64
end
struct EventCalendar
    events::Vector{Event}
end
EventCalendar() = EventCalendar(Event[])
events_at(cal::EventCalendar, step::Int) = filter(e -> e.step == step, cal.events)

# ----------------------------------------------------------------------------
# (d) Issuer and primary market (stub)
# ----------------------------------------------------------------------------
mutable struct Issuer
    need::Float64              # gross financing need, units of the instrument
    reservation_price::Float64
end
"""
    primary_auction(iss, bids) -> (filled, clearing_price)

Uniform-price auction: fills bids from the highest price down, never below the
reservation price, until the need is met. `filled < iss.need` is an uncovered auction.
"""
function primary_auction(iss::Issuer, bids::Vector{Tuple{Float64,Float64}})
    filled = 0.0
    px = NaN
    for (p, q) in sort(bids; by = b -> -b[1])
        p < iss.reservation_price && break
        take = min(q, iss.need - filled)
        take <= 0 && break
        filled += take
        px = p
    end
    return filled, px
end

# ----------------------------------------------------------------------------
# (e) Constraints on any state variable
# ----------------------------------------------------------------------------
"A constraint that tests any state through a predicate; breached when `test(state)` is true."
struct StateConstraint{F}
    test::F
end
breached(c::StateConstraint, state) = c.test(state)

# ----------------------------------------------------------------------------
# (b) Market and clearing
# ----------------------------------------------------------------------------
mutable struct Market
    instrument::Instrument
    f::Float64          # permanent log price
    u::Float64          # transient log price
    λ0::Float64
    κ::Float64
    λmax::Float64
    σbar::Float64       # fixed constant (per sub-step), computed once from data, not estimated
    φ::Float64          # transient share of each move
    ρ::Float64          # decay of the transient part per sub-step
    window::Vector{Float64}   # trailing per-sub-step log returns for σ̂
    widx::Int
    σhat::Float64
    impact::Symbol            # :linear (λ·x) or :sqrt (λ·sign(x)·√(|x|·q0)), note §6.3 alternative
    q0::Float64               # reference flow at which the two forms coincide
end
function Market(instr::Instrument; λ0, κ, λmax, σbar, φ, ρ, window::Int, impact::Symbol = :linear, q0::Float64 = 1.0)
    impact in (:linear, :sqrt) || error("unknown impact form $impact")
    Market(instr, 0.0, 0.0, λ0, κ, λmax, σbar, φ, ρ, fill(σbar, window), 1, σbar, impact, q0)
end
logprice(m::Market) = m.f + m.u
price(m::Market) = exp(m.f + m.u)
impact_lambda(m::Market) = min(m.λ0 * exp(m.κ * (m.σhat / m.σbar - 1.0)), m.λmax)

# (f) Liquidity provider: counterparty to every trade
mutable struct LiquidityProvider
    inventory::Float64
    cash::Float64
end
LiquidityProvider() = LiquidityProvider(0.0, 0.0)

# (g) Loss allocation
mutable struct LossFund
    balance::Float64     # negative = losses absorbed
end
LossFund() = LossFund(0.0)
"Default loss-allocation hook: the fund absorbs a shortfall (an adapter may override)."
allocate_loss!(fund::LossFund, loss::Float64) = (fund.balance -= loss; nothing)

"External flows into the system (equity injected, equity withdrawn), for conservation."
mutable struct Ledger
    cash_in::Float64
end
Ledger() = Ledger(0.0)

"""
    clear!(m, lp, x) -> price

Clear net agent flow `x` (share of float; buy > 0) against the liquidity provider,
which takes −x into inventory. All fills of the batch execute at the post-impact price.
"""
function clear!(m::Market, lp::LiquidityProvider, x::Float64)
    d = m.impact === :sqrt ? impact_lambda(m) * sign(x) * sqrt(abs(x) * m.q0) : impact_lambda(m) * x
    m.f += (1.0 - m.φ) * d
    m.u += m.φ * d
    p = price(m)
    lp.inventory -= x
    lp.cash += x * p
    return p
end

# ----------------------------------------------------------------------------
# Agent-class interface (implemented by adapters)
# ----------------------------------------------------------------------------
abstract type AgentClass end

"Context passed to agent classes. `σhat` is frozen during the cascade loop."
mutable struct Ctx{R<:AbstractRNG}
    p::Float64
    σhat::Float64
    K::Int
    step::Int                    # global sub-step
    day::Int
    sub::Int
    logcloses::Vector{Float64}   # log close by day (days < current are filled)
    σday::Float64                # σbar·√K, a fixed scale for normalising signals
    lp::LiquidityProvider
    ledger::Ledger
    fund::LossFund
    calendar::EventCalendar
    rng::R
end

# Required methods (each returns the class's summed order, share of float):
function ordinary_flow! end    # (cls, ctx) -> Float64   ordinary orders, once per sub-step
function forced_flow! end      # (cls, ctx) -> Float64   constraint-triggered orders only
function settle! end           # (cls, p, ctx) -> nothing  apply pending fills at price p
function substep_end! end      # (cls, ctx) -> nothing   bookkeeping between sub-steps
function n_constrained end     # (cls) -> Int            agents that can be forced
function units_held end        # (cls) -> Float64
function cash_held end         # (cls) -> Float64
reset_counters!(::AgentClass) = nothing

struct CascadeCapError <: Exception
    step::Int
    rounds::Int
end

Base.@kwdef struct SimConfig
    K::Int = 24
    days::Int = 1040
    burnin::Int = 120
    cascade::Bool = true          # false = ablation: forced orders execute as ordinary next sub-step
    fixed_point::Symbol = :nearest
end

struct World{C<:Tuple}
    market::Market
    lp::LiquidityProvider
    classes::C
    ledger::Ledger
    fund::LossFund
    calendar::EventCalendar
end
World(m::Market, classes::Tuple) =
    World(m, LiquidityProvider(), classes, Ledger(), LossFund(), EventCalendar())

struct PathResult
    close::Vector{Float64}   # daily close (price level), after burn-in
    low::Vector{Float64}     # daily low over all cleared prices, incl. cascade rounds
    high::Vector{Float64}
    max_rounds::Int
    substep_rounds::Vector{Int}
end

# summed calls over a tuple of classes (type-stable recursion)
_sum(f, cls::Tuple, ctx) = isempty(cls) ? 0.0 : f(first(cls), ctx) + _sum(f, Base.tail(cls), ctx)
_each(f, cls::Tuple, args...) = (foreach(c -> f(c, args...), cls); nothing)

"""
    simulate!(world, cfg, rng) -> PathResult

Run `cfg.burnin + cfg.days` days of `cfg.K` sub-steps. Within each sub-step:
ordinary orders clear once; then the cascade loop clears forced orders in batches
until none remain (cap N + 1, else `CascadeCapError`); then classes update; then σ̂
is refreshed and the transient price part decays.
"""
function simulate!(w::World, cfg::SimConfig, rng::AbstractRNG)
    cfg.fixed_point === :nearest || error("only :nearest fixed-point selection is implemented")
    m, lp, cls = w.market, w.lp, w.classes
    K = cfg.K
    T = cfg.burnin + cfg.days
    N = sum(n_constrained, cls)
    cap = N + 1
    logcloses = zeros(T)
    ctx = Ctx(price(m), m.σhat, K, 0, 1, 1, logcloses, m.σbar * sqrt(K), lp, w.ledger, w.fund, w.calendar, rng)
    closes = Float64[]; lows = Float64[]; highs = Float64[]
    maxr = 0
    rounds_log = Int[]
    deferred = 0.0
    for day in 1:T
        dlo = Inf; dhi = -Inf
        for sub in 1:K
            ctx.step += 1; ctx.day = day; ctx.sub = sub
            lp0 = logprice(m)
            # ordinary orders
            x = _sum(ordinary_flow!, cls, ctx) + deferred
            deferred = 0.0
            p = clear!(m, lp, x)
            ctx.p = p
            _each(settle!, cls, p, ctx)
            dlo = min(dlo, p); dhi = max(dhi, p)
            # cascade loop (σ̂ frozen: ctx.σhat and m.σhat unchanged inside)
            rounds = 0
            while true
                F = _sum(forced_flow!, cls, ctx)
                F == 0.0 && break
                rounds += 1
                rounds > cap && throw(CascadeCapError(ctx.step, rounds))
                if cfg.cascade
                    p = clear!(m, lp, F)
                    ctx.p = p
                    _each(settle!, cls, p, ctx)
                    dlo = min(dlo, p); dhi = max(dhi, p)
                else
                    # ablation: forced orders are booked at the current price and their
                    # market impact is deferred to the next sub-step's ordinary batch
                    lp.inventory -= F; lp.cash += F * p
                    _each(settle!, cls, p, ctx)
                    deferred += F
                end
            end
            maxr = max(maxr, rounds)
            day > cfg.burnin && push!(rounds_log, rounds)
            _each(substep_end!, cls, ctx)
            # σ̂ update and transient decay, between sub-steps only
            r = logprice(m) - lp0
            m.window[m.widx] = r
            m.widx = m.widx == length(m.window) ? 1 : m.widx + 1
            m.σhat = sqrt(sum(abs2, m.window) / length(m.window))
            ctx.σhat = m.σhat
            m.u *= (1.0 - m.ρ)
            ctx.p = price(m)
            dlo = min(dlo, ctx.p); dhi = max(dhi, ctx.p)
        end
        logcloses[day] = logprice(m)
        if day > cfg.burnin
            push!(closes, ctx.p); push!(lows, dlo); push!(highs, dhi)
        end
    end
    return PathResult(closes, lows, highs, maxr, rounds_log)
end

end # module
