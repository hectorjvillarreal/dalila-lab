# Cath — Sign-off check of B1a

*Checkout `~/Dalila-abm`, branch `aurora-crypto-abm`, commit 999b613. I read the B1a report, `ABMCore.jl` and its `.md`, `CryptoAdapter.jl`, `fit.jl`, `ablations_bestfit.jl` and `runtests.jl`. I ran the tests (413 of 413 pass, 5.8 s) and one 300-day conservation check from the scratchpad. I edited no files. 2026-11-17.*
*Filed verbatim by Claude Code, 2026-11-17. Code fixes 1–5 were applied in the commit that filed this memo. Report fixes 6–8 were applied after the full rerun.*

## Verdict

**Sign off with minor fixes (listed; no re-check needed).** The linear-impact engine does what note §2 asks for. The fixes concern the square-root option, the accounting in the no-cascade ablation, a silent catch in the fit, and wording. Fix 1 needs a 20-minute rerun of the square-root fit. Until that rerun, findings 1 and 2 should be marked provisional (fix 6).

## Per-item findings

- **R1, units: correct.** Order flow is a share of the float, p₀ = 1, and noise is σ_ε/√K per sub-step (`CryptoAdapter.jl:314`). Recovery finds σ_ε weakly identified, which fits the fact that only agent flows separate it from λ₀.
- **R2, cap and frozen σ̂: correct.** `impact_lambda` includes the λ_max cap (`ABMCore.jl:127`), and σ̂ does not change inside the loop (`:267–286`). Small slip: the return fed into σ̂ is taken *before* the transient decay (`:291` vs `:296`), so price moves caused by the decay never enter σ̂ (fix 4).
- **Transient impact: correct.** Each move splits into a permanent part f and a transient part u (`:158–159`), and u decays only between sub-steps (`:296`). It is a price-resilience term, not mean reversion of the liquidity provider's inventory; that is fine, and the `.md` says it correctly.
- **Loop rules (a)–(c) and the cap: correct.** Rule (b) holds through `flagged` (`CryptoAdapter.jl:104–107`) and `closing` (`:249`). One long and one short that entered at different prices can breach margin at the same price, so a round's forced flow can carry both signs. The N + 1 bound still holds, because every round fires at least one new constraint. A binding cap throws an error (`ABMCore.jl:273`).
- **Cap as a bug, in the fit: not fully applied.** `objective` catches every exception and turns it into J = Inf (`fit.jl:89–94`), and in the search and Nelder–Mead stages it logs nothing. A binding cap would therefore silently steer the optimiser. The report's "no draw aborted; the cascade cap never bound" (report l.36) is verified only for the random-search stage (fix 3).
- **Fixed-point selection: correct.** Only `:nearest` is implemented; anything else is an error (`:243`).
- **Core stubs (a)–(g): mostly present.**
  - (c) The calendar is not consulted by `simulate!`, which is acceptable for a stub. The auction stub (d) is correct.
  - (b) The docstring claims "several markets are allowed by the World", but `World` has a single `market::Market` field (`:12`, `:211–218`). Holdings are not an agents × instruments array either (fix 5).
  - (e) m(σ̂) exists, but m₁ = 0 by default (`CryptoAdapter.jl:47`) and is not in the search box (`fit.jl:46–49`). So the margin half of the Brunnermeier-Pedersen spiral is off in every fit. Say so.
  - (f) The liquidity provider is the counterparty to every trade. Funding signs are right: longs pay when longs dominate, and the provider receives the net (`:289–295`). With the cascade loop on, conservation holds (units 8e-15, cash 1e-12).
- **No-cascade ablation: conservation breaks.** Deferred forced flow is booked at the provider at `:282`, then booked again when it is cleared in the next sub-step (`:261–263`). My check with `cascade = false` gives a units residual of 0.86 and a cash residual of −0.82. Prices are unaffected, because the provider's state does not feed back into them, so the ablation's moments stand. Criterion 7 is only tested with the loop on (fix 2).
- **Square-root option: modelling error.** `clear!` applies √ to each batch separately (`:157`). Ordinary flow and each cascade round are cleared one at a time, so the total impact depends on how many rounds the iteration takes: √a + √b > √(a+b). This breaks the order-invariance result of R3. One liquidation (w_l/N_l ≈ 0.0013, below q₀ = 0.002) moves the price 1.26 times more than under linear impact, and two in separate rounds 1.42 times more than together. Under √, cascade amplification therefore partly comes from the round count.
- **Leveraged equity: an unstated assumption.** Equity is injected at entry and withdrawn at close (`:235–236`, `:265–268`), so the leveraged traders' size never responds to their gains or losses. That removes a persistence channel and may explain the weak ACF of |r| at lags 5 and 20. State it as a limitation.

## The two findings

1. **"κ not robust to the impact law": the direction is fair, but the support is contaminated.** The √ fit includes the round-count artefact, which can stand in for κ's amplification. The stated mechanism (l.123: diminishing impact of large flows "stands in for" withdrawal) also points the wrong way. Concave impact *damps* large flows, while κ *raises* impact in stress, so they are not obvious substitutes. The κ = 0 ablation at a fitted κ of 0.011 carries no information.
2. **Parameter values depend on the impact law: fair.** But the linear 18× sits at the edge of the search box, so it is a bound, not a value. And λ₀ is not comparable across the two laws.

## Fixes

1. **`ABMCore.jl:157`, square-root impact.** Make total impact depend only on the sub-step's cumulative flow. Add the field `Xcum::Float64 = 0` to `Market`, reset it with `m.Xcum = 0.0` at the start of each sub-step (`:258`), and use:
   ```julia
   g(m, X) = m.impact === :sqrt ? sign(X) * sqrt(abs(X) * m.q0) : X
   X1 = m.Xcum + x
   d  = impact_lambda(m) * (g(m, X1) - g(m, m.Xcum)); m.Xcum = X1
   ```
   Linear impact is unchanged by this. Then rerun `run_sqrt.sh` and the √ ablations.
2. **`ABMCore.jl:261–263`, ablation accounting.** Replace with:
   ```julia
   xo = _sum(ordinary_flow!, cls, ctx); dflow = deferred; deferred = 0.0
   p = clear!(m, lp, xo + dflow)
   lp.inventory += dflow; lp.cash -= dflow * p   # deferred flow already booked (ablation)
   ```
   Add a conservation test with `cascade = false`.
3. **`fit.jl:91`.** Add `e isa CascadeCapError && rethrow()` as the first line of the `catch` block.
4. **`ABMCore.jl:291–296`.** Move `m.u *= (1.0 - m.ρ)` above `r = logprice(m) - lp0`.
5. **`ABMCore.jl:12–13`.** Replace with: "(b) `Market` (log price = permanent f + transient u). B1's `World` holds one market and holdings are per-class vectors; several markets and an agents × instruments holdings array enter at the start of B3."
6. **Report, l.123.** Replace with: "**Provisional.** Under square-root impact the fit sets κ ≈ 0. The implementation tested applied √ to each cascade round separately, which adds impact that depends on the round count and may stand in for κ. The κ statement is pending the rerun with cumulative impact (fix 1). Until then, any statement about liquidity withdrawal must name the impact law."
7. **Report, l.36.** Replace with: "No random-search draw aborted. Nelder–Mead evaluations did not log aborts (`fit.jl:92`, fixed afterwards)."
8. **Report, Limitations.** Add: "8. m₁ = 0 throughout, so the margin channel is off. 9. Leveraged traders re-enter with fixed size and fresh equity, so there are no wealth dynamics. 10. λ₀ is not comparable across impact laws, and the linear median L of 18× is at the box edge."

## Not checked

I did not check targets, moment conventions or the 3σ convention (Fina's remit). I did not rerun any fit.
