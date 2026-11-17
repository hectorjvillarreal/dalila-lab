# Cath — Endorsement check of design note B0 v1.1

*Read in full: `Aurora_Nina_CRYPTO_ABM_DesignNote_B0_202611.md` at 3edcb0d. Read only. 2026-11-16.*
*Filed verbatim by Claude Code, 2026-11-16. Fixes 1–4 are applied in design note v1.2.*

## Endorsement

**Endorse with minor fixes (listed; no re-review needed).** All six required changes and all five recommended changes are in. Four fixes remain: two wording problems, one missing equation, and a null test that is wrong as written. Each can be made in place without a fresh review.

## Per-item check

| Item | Status | Note |
|---|---|---|
| R1 units | Applied, with a problem | Flow is measured as a share of the float, depth is normalised to 1, and the rule no longer depends on the price level. All correct. But the sentence "Noise flow has a fixed unit scale, which leaves σ_ε and λ₀ identified separately" contradicts §4, which lists σ_ε as free. See fix 1. |
| R2 cap, frozen σ̂ | Applied | min{·, λ_max} and the freeze are both right. σ̄ should be stated as a fixed constant, not a parameter (fix 1). |
| R3 loop rules, selection | Applied | Rules (a)–(c), the nearest fixed point (Cifuentes-Shin-Ferrucci), and deeper fixed points as setting (g) are all right. The new transient decay must not run inside the loop (fix 2). |
| R4 binding cap | Applied | The cap of N + 1 is right, a binding cap is treated as a bug, and carry-over is kept as a named variant. |
| R5 (a)–(g) | Applied | All seven are there, plus the external-stress hook in §0 and the grep test in §11.1. |
| R6 §9 | Applied, with a problem | It reports my OLG facts and uses the crisis-zone boundary and z*. It is right that no spread is fed back and that §10 is not yet met. One wording slip on C2 (fix 3). |
| Rec. 1 perp = spot | Applied | §2 and §6.3. |
| Rec. 2 transient impact | Applied, with a problem | φ, ρ, the φ = 0 ablation and the parameter ranges are in. The way the decay moves the price is never written down (fix 2). |
| Rec. 3 optimiser, replications | Applied | §5 now has a derivative-free optimiser, the same optimiser in the recovery test, and S ≥ 10 replications. |
| Rec. 4 recalibration, phases | Applied | §5 recalibrates in B2, and the §3.4 phase map is reconciled with the spec. |
| Rec. 5 leverage from data | Applied | §6.1 sets leverage from data and changes one factor at a time. |
| New in v1.1: §11.3 null test | Wrong | With noise only but κ > 0, λ_s = λ₀·exp(κ(σ̂/σ̄ − 1)) is itself GARCH-like. Simulated returns would then show fat tails and clustering, and the test fails by construction. More importantly, κ can produce the stylized facts without any agents, which undercuts §0's "from agent behaviour alone" (fix 4). |
| New in v1.1: m(σ̂) = m₀ + m₁σ̂ | Minor | §4 gives m₁ no range (fix 1). |

## Minor fixes

1. **§2, R1 bullet.** Replace "Noise flow has a fixed unit scale, which leaves σ_ε and λ₀ identified separately" with: "Noise flow is σ_ε·ε_s, with ε_s ~ N(0, 1/K) in float-share units. λ₀ and σ_ε are separately identified only through agent flows, whose scale is fixed because holdings and demands are fractions of each class's float share. Momentum demand is w_m·tanh(β·trend_h), with no free proportionality constant." In the **R2 bullet**, add: "σ̄ is a fixed constant computed once from the hourly data snapshot; it is not estimated." In the **§4 table**, add "m₁ ≥ 0, range to be scaled in B1a, with σ̂ in per-sub-step units."

2. **§2, R4b bullet.** Add: "Log price is f_s + u_s. Each clearing adds (1−φ)·λ_s·x_s to the permanent part f and φ·λ_s·x_s to the transient part u. Between sub-steps, never inside the cascade loop, u_{s+1} = (1−ρ)·u_s. The liquidity provider's inventory unwind is the accounting counterpart of this decay and is not routed back through λ." This keeps R3's result that the end price does not depend on execution order.

3. **§9, last bullet of "What the OLG produces today".** Replace with: "under the 'debt absorbs' reading of closure C2 (pension deficit routed to the general budget), it has no finite steady state; the C2 that was shipped uses benefit scaling."

4. **§11.3.** Replace with: "**Null test.** With noise only and κ = 0, excess kurtosis and the ACF of |r| are about zero." Add to **§11.5**: "and, separately, setting κ = 0, so that the share of clustering and tails due to liquidity withdrawal alone is reported."

## Not checked

I did not check the §1 figures (Fina's remit), the build instruction, or the branch setup.
