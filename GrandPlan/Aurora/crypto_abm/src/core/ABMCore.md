# ABMCore — asset-agnostic engine core

Companion to `ABMCore.jl`. It implements design note B0 v1.2, §2. A grep test keeps every asset-class term out of this module.

## Objects
- `Instrument`: an instrument with a cash-flow schedule. `consol` builds one with no cash flows.
- `Market`: log price = f (permanent) + u (transient), plus the impact parameters.
- `EventCalendar` and `Event`: scheduled maturities, coupons, auctions, reviews.
- `Issuer` and `primary_auction`: a uniform-price auction with a reservation price. A stub in B1a.
- `StateConstraint`: a predicate on any state variable.
- `LiquidityProvider`: counterparty to every trade, holding inventory and cash.
- `LossFund`: the loss-allocation hook (`allocate_loss!`).
- `Ledger`: external cash injected or withdrawn, so conservation can be checked.

## Clearing and the cascade loop (note §2, R1–R4)
- `clear!` moves the log price by λ·x. x is net flow as a share of the float. λ = min(λ₀·exp(κ(σ̂/σ̄ − 1)), λ_max).
- A share φ of each move is transient and decays by (1 − ρ) between sub-steps, never inside the cascade loop.
- Inside a sub-step, ordinary orders clear once. Then forced orders clear in batches until none remain.
- σ̂ is frozen inside the loop.
- The cap is N + 1 rounds. A binding cap throws `CascadeCapError`: it is a bug, never data.
- `SimConfig(cascade = false)` is the "no cascade loop" ablation. Forced orders are booked at the current price, and their impact is deferred to the next sub-step.

## Agent-class interface
An adapter implements `ordinary_flow!`, `forced_flow!`, `settle!`, `substep_end!`, `n_constrained`, `units_held` and `cash_held`. All fills in a batch execute at the post-impact price.
