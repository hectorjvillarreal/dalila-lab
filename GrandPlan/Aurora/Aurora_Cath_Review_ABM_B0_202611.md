# Cath — Review of Nina's crypto ABM design note B0

*Scope (D6): §2 and §9, plus §3–§5 and §8 where they bear on them. On the OLG side I read BID2 `ge_model_gender.jl` and `run_aging_ssvs.jl`, read-only. 2026-11-16.*
*Filed verbatim by Claude Code, 2026-11-16.*

## Verdict

**Approve B1 with required changes.** The split between a generic engine and adapters is right, and the cascade loop is the right home for the mechanism. But §2 leaves three things open: the units of the clearing rule, what the cascade loop does, and what happens when its cap binds. The core is also still one perpetual asset, with no issuer, calendar or primary market. R1–R5 go into §2 as an amendment before the first core commit. R6 can wait until the sovereign instance, which comes after B3.

## Required changes

**R1. §2, units.** λ₀ and D enter only as the ratio λ₀/D, so they cannot be told apart. Measure X_s in coins as a share of the float, fix D = 1, and make the rule independent of the price level. With X in dollars, the same coin flow moves the price more at $120k than at $60k, which is an artefact. σ_ε and λ₀ also move together for noise flow, so normalise one of them.

**R2. §2, λ_s.** Define σ̂_s: its window, and whether it is measured per sub-step or per year. Use λ_s = λ₀·exp(κ(σ̂_s/σ̄ − 1)), capped at λ_max, and freeze σ̂_s during the cascade loop. Without a cap, volatility raises impact and impact raises volatility, so simulated paths can explode at parameters SMM will visit.

**R3. §2, cascade loop.** State three rules:
- (a) Only forced orders act inside the loop. Momentum and noise orders act once per sub-step.
- (b) Each constraint fires once per crossing. A liquidation closes the position, and a conviction sale sets a flag that resets only when the agent re-enters.
- (c) Each round's forced orders clear as one batch.

With these rules, forced flow has one sign and grows as the price falls. The loop then ends within N rounds, where N is the number of constrained agents. While λ is frozen, log impact is additive, so the final price does not depend on the order in which forced sales execute. The loop picks the fixed point closest to p_s, as in Cifuentes-Shin-Ferrucci (2005). Record this choice: the deeper fixed points are the run equilibria a sovereign instance needs.

**R4. §2, the cap.** "The event is recorded" does not say which price results. Under R3 the cap cannot bind before N rounds, so a binding cap is a bug. Abort the draw and log it; do not keep it as data. If cascades are meant to take time, which may be what §1.3's intraday gap needs, say so: at most M rounds per sub-step, with the remaining forced orders carried to the next sub-step.

**R5. §2, minimal core abstractions.** Stubs are enough, with one of each in B1:
- (a) Instruments with a cash-flow schedule; a coin is the perpetual case with no cash flows. Holdings are an agents × instruments array.
- (b) Several markets with linked prices. B3 needs this, and so do perp vs. spot and bonds vs. FX.
- (c) An event calendar for maturities, coupons, auctions, rating reviews and financing walls. Nothing is hard-coded to K = 24, √365 or 1,040 days.
- (d) An issuer agent with a gross financing need, and a pluggable primary-market clearing rule: an auction with a reservation price, where failure means issuance not covered. B2 needs this anyway, since ETF creations and treasury-company issuance are primary-market operations and E3 is a rollover problem.
- (e) Constraints that can test any state variable (price, equity, rating, issuer status), with parameters that depend on state. A margin m(σ̂) is the missing half of the Brunnermeier-Pedersen spiral.
- (f) The liquidity provider as an agent with inventory, so that conservation of coins and cash can be a unit test. At present nobody is on the other side of forced sales or of net perp positions.
- (g) A loss-allocation hook (insurance fund, auto-deleveraging, sovereign haircut) and a setting for which fixed point the solver selects.

**R6. §9.** Rewrite it against what the OLG actually produces (Q3).

## Recommended changes

1. §3.1: say explicitly that one price for perp and spot assumes instant arbitrage between them.
2. §1.3/§6.2: price impact is fully permanent. Nothing can bring a −12.1 % intraday low back to a −7.2 % close, so the intraday target cannot be met. Add a parameter for how fast impact decays, or mean reversion in the liquidity provider's inventory.
3. §5: liquidation thresholds make the moments jump in steps as parameters change. Smooth the triggers or use derivative-free search, run the recovery test with the same optimiser, and use at least 10 replications per draw.
4. §5–§6: B1 calibrates on post-ETF moments without ETF agents (they arrive in B2), so plan to recalibrate. The phase labels also clash: B3 is SMM calibration in the spec but the two-asset engine in the note.
5. §6.1: fix the leverage change from data before running the regime-shift test. Leaving it free makes the test easy to pass.

## Answers

**Q1. Is the core asset-agnostic?** Not yet. The core is still crypto-shaped in five ways: one perpetual asset, no cash flows or maturities, no issuer or primary market, constraints triggered only by price, and a liquidity provider with no balance sheet. Each sovereign mechanism hits one of these:
- Cole-Kehoe runs happen at auctions, when holders decline to roll over, rather than through sales.
- The doom loop marks bank capital to bond prices and adds bailout costs to the issuer's debt.
- Rating floors are cliffs on a categorical variable.
- The central bank is an agent with no margin constraint that buys according to a rule.

R5 is the minimum that lets each of these be written as an adapter. "Gaussian noise is the only input" is a crypto choice, not a core rule.

**Q2. Is the clearing rule well posed?** Not as written. With R1–R4 it is.

**Q3. Does §9 make sense from the OLG side?** Only in part. The BID2 OLG has these features:
- It is a stationary solver with five-year periods.
- The economy is closed (K = A_dom − B).
- There is one riskless bond, and debt is the residual B = primary/(r_n − n_p).
- It gives comparative steady states for 2020 and 2050. Under closure C2 with debt absorbing the gap, no finite steady state exists.
- It has no transition path, maturity, currency, holder split or spread.

What can flow between the two models:
- **OLG → ABM:** by scenario and closure, annually once a transition solver exists: debt/GDP, the primary balance, r − n, and domestic asset demand by age. The last of these, the capacity of captive holders such as the AFOREs, is what only the OLG can supply.
- **Exogenous inputs:** maturity, currency and foreign share come from debt-management data, sourced and dated. A closed-economy OLG implies zero foreign financing, so it needs an open-economy closure first.
- **Timing:** the ABM runs one-year slices with fundamentals held fixed.
- **ABM → OLG:** no spread path and no fixed-point coupling. At most, a boundary the closure must respect, or a crisis branch solved as a separate scenario.

The frequency of rollover failure is the wrong headline. Inside the multiple-equilibrium zone, it is set by the coordination shock the modeller assumes, so it reads like a probability it is not. Better objects:
- the crisis-zone boundary: the states where a self-fulfilling run exists, in the space of debt, maturity, holder mix and backstop;
- the minimum coordinated shock z* that makes an auction fail.

Index either by state, never by date. Overlay the OLG path ("under S and C, the path enters the zone at debt d"), and name the equilibrium-selection rule.

**Q4. Other errors that matter for §2/§9.** R1 is an exact identification failure. Recommended changes 2–4 matter next. The OLG's riskless r and the ABM's market yield will diverge in the crisis zone. Keep r as the fundamental rate and never feed ABM yields back.

## What I could not check

I ran no code and did not recompute §1; that is Fina's remit. I found no DFD transition solver. I did not source whether perp-specific dislocations occurred on 2025-10-10.
