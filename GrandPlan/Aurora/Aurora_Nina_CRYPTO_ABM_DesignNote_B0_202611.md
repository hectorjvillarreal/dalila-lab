# Design note B0 — Crypto agent-based model (mechanism laboratory) · v1.2

*Document type: Design note (phase B0 of Part B) · Aurora Project*
*Author: Nina (portfolio management & crypto strategy). Drafted by Claude Code in Nina's role at Héctor's request, 2026-11-16.*
*Status: **v1.2, 2026-11-16.** Decisions D1–D6 ruled by Héctor (§10). v1.1 applied the required changes of both reviews (`Aurora_Cath_Review_ABM_B0_202611.md`, `Aurora_Fina_Review_ABM_B0_202611.md`). **Cath endorsed v1.1 with minor fixes, 2026-11-16** (`Aurora_Cath_Endorsement_ABM_B0_v1.1_202611.md`). **Fina endorsed v1.1 with minor fixes, 2026-11-16** (`Aurora_Fina_Endorsement_ABM_B0_v1.1_202611.md`). Both say no re-review is needed; v1.2 applies all their fixes. No code is written in B0. **B1 waits only for Héctor's go.** Branch ruled (§8).*
*Parent spec: `Aurora_Nina_CRYPTO_BR_Spec_ClaudeCode_202611.md`, Part B (§5) and §5.7 (design for reuse). Precedent: `Aurora_Nina_MonetaryFoundation_202604.md` §10.*
*Provenance: build instruction `_crossrefs/_build_instructions/2026-11-16_aurora_crypto_board_and_abm_b0.md` (filed 2026-11-16 on main; B1 gets build instruction 2_of_2, filed on main before the first commit on `aurora-crypto-abm`).*

### Amendments from B1a (2026-11-17)

*Dated amendments required by build instruction 2_of_2, §1. They came from the B1a build and from the Cath and Fina sign-off checks (`crypto_abm/reviews/` on branch `aurora-crypto-abm`).*

- **(a) R2, σ̄.** σ̄ is the RMS of hourly BTC log returns over the post-ETF window, **0.502 %/h**, not the mean of σ̂ (which would be 0.445 %/h).
- **(b) §5, 3σ share.** For calibration, the 3σ share uses a *within-window* trailing s.d. for both data and model: **1.58 %** for post-ETF BTC. The full-history value in §1.1 (1.92 %) is descriptive only.
- **(c) §6.3 and §11.10, clearing-rule alternative.** The base rule is already linear in log price, so the alternative run is **square-root impact**, Δln p = λ·sign·(√(\|X₁\|q₀) − √(\|X₀\|q₀)) on the sub-step's *cumulative* flow X. q₀ = 0.002 of the float per sub-step is a normalisation choice. Impact depends only on cumulative flow, so splitting a batch into cascade rounds never changes the total move (Cath, sign-off fix 1).
- **(d) §2, implementation details.**
  - The transient decay is applied before the sub-step return enters σ̂.
  - The "cascade loop off" ablation books forced orders at the current price and defers their impact to the next sub-step.
  - A binding cascade cap aborts the evaluation in the fit too (R4).
- **(e) Implementation limits in B1a**, to keep in mind when reading results:
  - m₁ = 0 throughout, so the margin channel of the spiral is off.
  - Leveraged traders re-enter with fixed size and fresh equity, so there are no wealth dynamics.
  - The calendar and the primary-market stub are not yet used by the simulation.
  - Holdings are per-class vectors in one market; agents × instruments arrives in B3.

### What changed in v1.2 (2026-11-16, endorsement fixes)

- **Cath:**
  - noise and identification wording (R1);
  - σ̄ is a fixed constant (R2);
  - the transient-impact equation, kept outside the cascade loop (R4b);
  - a range for m₁;
  - C2 wording in §9;
  - the null test with κ = 0, plus a κ = 0 ablation (§11).
- **Fina:**
  - the 3σ-day convention is stated, with its alternatives (Appendix A, §1.1);
  - wording in §0 and the §1 intro;
  - where build instruction 2_of_2 is filed;
  - common random numbers restored in criterion 7;
  - endorsement recorded here, in the spec and in the build instruction.

### What changed from v1 (2026-11-16)

- **§1** The regime story is corrected. Removing one day (2020-03-12) erases the pre/post-ETF contrast in tail shape. The ETF era differs in the *level* of volatility and the *frequency* of large days, not in tail shape (Fina). Rounding is fixed, the conventions are stated, and the episode table no longer carries attributions from memory.
- **§2** The engine is re-specified (Cath R1–R5):
  - units and normalisation;
  - capped impact, frozen inside the cascade loop;
  - loop rules and what a binding cap means;
  - transient impact;
  - minimal core abstractions so a sovereign adapter is not blocked.
- **§6** The regime-shift test moves to B2 and changes one factor at a time.
- **§7** The bridge to the board is reworded so the firewall holds (Fina).
- **§8** Location, CPU/GPU and the GPU check are made explicit.
- **§9** Rewritten against what the BID2 OLG actually produces. The interface object is now a crisis-zone boundary, not a rollover-failure frequency (Cath R6).
- **§3.4 (new)** Phase map reconciled with the spec.
- **§11 (new)** B1 acceptance criteria.
- **§12 (new)** Cadence.

---

## 0. What this model is for, and the firewall

The model is a **laboratory for mechanisms**. It must reproduce the statistical signature of crypto returns from agent behaviour alone. Then it asks **conditional** questions. For example: with this share of leveraged traders at this leverage, how often does a liquidation cascade turn a −3 % day into a −12 % intraday low? Returns in examples, worst days and episodes are simple, measured from the prior close; moments use log returns (§1).

It never says where bitcoin or ether will trade.

The firewall from the spec (§0) applies without exception:
- No model output enters the crypto board's state files, and **no model number appears on the board's dashboard**.
- A model result reaches the board only as a question for Héctor's ruling, under the rules in §7.
- `crypto_abm/` never reads from or writes into `crypto_monitor/`. A test enforces this (§11).
- The model is not connected to the DSGE-OLG core. §9 states what an interface could carry, for Cath to design.

The target is an emergent coordination failure, the same kind Nina set for the monetary model with the September 2019 repo spike. In the **crypto adapter**, plain Gaussian order-flow noise is the only exogenous input. That is a crypto-instance choice, not a core rule. The core keeps a hook for external stress inputs (Gina's layer) for later instances.

---

## 1. What the data says the model must reproduce

These figures come from Coinbase daily UTC closes for BTC-USD and ETH-USD, 2019-01-01 to 2026-11-16: 2,877 closes each, with no missing days. They are MARKET data, our computation, and were reproduced independently by Fina (review and endorsement check, 2026-11-16). Conventions:
- Moments use log returns, formed *within* each window. The post-ETF window gives 1,040 returns and drops the 2024-01-11 return.
- Standard deviations use ddof = 1. Skewness and kurtosis are standardised with that s.d.
- Figures are rounded, not truncated.
- The "3σ day" counts |r_t| above 3 times the s.d. of the previous 90 daily returns, on the full return history (Appendix A).
- Worst days and episodes are **simple** price changes.

The method is in Appendix A.

### 1.1 Two periods, and what actually differs between them

| Moment | BTC 2019–2023 | BTC 2019–2023 excl. 2020-03-12 | BTC post-ETF (2024-01-11 → 2026-11-16) | ETH 2019–2023 | ETH 2019–2023 excl. 2020-03-12 | ETH post-ETF |
|---|---|---|---|---|---|---|
| Daily s.d. (annualised) | 3.64 % (69.5 %) | 3.45 % (65.9 %) | **2.46 % (47.0 %)** | 4.65 % (88.9 %) | 4.46 % (85.2 %) | **3.51 % (67.0 %)** |
| Skewness | −1.32 | +0.03 | +0.11 | −1.23 | −0.28 | +0.29 |
| Excess kurtosis | 20.7 | 3.56 | 3.44 | 15.6 | 4.52 | 3.88 |
| **Hill tail index (top 5 % of \|r\|)** | 3.25 | 3.43 | 3.45 | 2.91 | 3.07 | 3.23 |
| **Share of 3σ days (90-day trailing s.d.)** | 1.96 % | 1.90 % | 1.92 % | 1.73 % | 1.67 % | 1.73 % |
| ACF of \|r\|, lag 1 | 0.16 | 0.14 | 0.16 | 0.17 | 0.14 | 0.14 |
| Share of days with \|log r\| > 0.10 (simple > 10 %) | 2.19 % (2.25 %) | 2.14 % (2.19 %) | **0.29 % (0.38 %)** | 3.95 % (4.05 %) | 3.89 % (4.00 %) | **2.02 % (2.12 %)** |
| Worst day (simple) | −38.8 % (2020-03-12) | −15.4 % (2022-06-13) | −14.0 % (2026-02-05) | −43.3 % (2020-03-12) | −27.6 % (2021-05-19) | −14.9 % (2026-02-05) |

The BTC–ETH correlation is 0.84 before and 0.83 after. ETH's beta to BTC rises from 1.07 to **1.18**.

Post-ETF maximum drawdowns: BTC −53.1 % ($124,720 on 2025-10-06 to $58,524 on 2026-06-30); ETH −67.6 % ($4,831 on 2025-08-22 to $1,565 on 2026-06-25). On 2026-11-16, BTC is 48.0 % and ETH 62.3 % below their post-ETF closing highs.

**Reading (corrected in v1.1).** v1 said the ETF launch "splits the sample cleanly", including in tail shape. That was wrong. Without one day, 2020-03-12, the pre-ETF skewness and kurtosis are close to the post-ETF values. Neither robust tail measure moves materially across the periods: the Hill index is 3.43 vs 3.45 for BTC, and the 3σ-day share is 1.9–2.0 % for BTC and about 1.7 % for ETH in both periods (convention in Appendix A; with a within-window trailing s.d. the post-ETF shares are 1.58 % and 1.68 %, and the Hill index carries the conclusion under every variant). Volatility clustering (ACF of |r|) is also unchanged.

What does differ:
- the **level of volatility** (BTC annualised s.d. 65.9 % → 47.0 % excluding the crash day);
- the **frequency of 10 % days** (BTC about 7× lower, ETH about 2× lower);
- **ETH's beta** to BTC.

The ETF launch is not the only change between the periods. The pre-ETF window holds the 2021 bubble and the 2022 lender and exchange failures, and the April 2024 halving falls just after the launch. The contrast is evidence about *volatility level and large-day frequency*, with confounders. It is not evidence about tail shape.

**Design consequences.**
1. The model is calibrated on the post-ETF window (D1).
2. The robust tail measures are targets because they are stable across periods. A model that matches them has the right *shape* of tails, and the regime question is about *scale and frequency*.
3. The regime-shift test (§6.1) moves to B2, changes one factor at a time, and targets the s.d. and the 10 %-day frequency, not the tail index.

### 1.2 Raw kurtosis is too fragile to calibrate on

Removing 2020-03-12 cuts full-sample BTC excess kurtosis about fivefold (21.1 → 4.1) and ETH's about threefold (14.7 → 4.7). The Hill index and the 3σ-day share are targeted; raw kurtosis is reported only (D3).

### 1.3 Daily closes hide the cascades

On 2025-10-10, BTC closed −7.2 % (simple, close to close). From the prior close ($121,714.51, equal to that day's open) to the intraday low ($107,000) it fell −12.1 %. ETH closed −12.2 %.

The intraday target is defined as **prior close to intraday low**, against prior close to close, on the largest down days. B1 fetches hourly candles (granularity 3600) for this and checks that the open equals the prior close on each day used. This target also needs **transient impact** in the engine (§2, R4b). With permanent impact, an intraday low can never recover to a higher close.

### 1.4 Selected large down days (simple returns)

This is **not** a ranking of the largest drops. Rows were chosen to cover the largest drops and the episodes discussed in the spec. Causes are **unsourced** and are not used as targets. B1 sources any cause it relies on, with two independent sources, or leaves it blank.

| Date | BTC | ETH | Cause |
|---|---|---|---|
| 2019-06-27 | −13.7 % | −12.4 % | unsourced |
| 2020-03-12 | −38.8 % | −43.3 % | unsourced |
| 2021-01-21 | −13.1 % | −19.3 % | unsourced |
| 2021-05-19 | −14.3 % | −27.6 % | unsourced |
| 2022-06-13 | −15.4 % | −15.7 % | unsourced |
| 2022-11-09 | −14.3 % | −17.6 % | unsourced |
| 2025-10-10 | −7.2 % close; −12.1 % to intraday low | −12.2 % close | unsourced |
| 2026-02-05 | −14.0 % | −14.9 % | unsourced |
| 2026-11-13 / 11-14 | −4.4 %, −6.0 % | −4.4 %, −8.3 % | press 11-14..16 cites ETF outflows, rate-hike bets and $1–2 B liquidations (totals disagree); see crypto board state 2026-11-16 |

---

## 2. Architecture: a generic engine and adapters

The **core knows nothing about crypto** (spec §5.7). A grep test enforces this (§11). The core holds the objects below. B1 implements one of each as a stub; the crypto adapter uses the perpetual, single-market case.

**Core objects (Cath R5):**
- **(a) Instruments** with a cash-flow schedule. A coin is the perpetual case with no cash flows; a bond has coupons and a maturity. Holdings are an agents × instruments array.
- **(b) Markets**, possibly several, with linked prices: perp vs. spot (B3), two coins (B3), bonds vs. FX (sovereign).
- **(c) An event calendar** for maturities, coupons, auctions, rating reviews and financing walls. Nothing is hard-coded to K = 24 sub-steps, √365 annualisation or a 1,040-day sample; these are instance parameters.
- **(d) An issuer agent** with a gross financing need, and a pluggable **primary-market clearing** rule: an auction with a reservation price, where failure means issuance not covered. B2 needs it for ETF creations and treasury-company issuance, and E3 is a rollover problem.
- **(e) Constraints** that test any state variable (price, equity, rating, issuer status), with state-dependent parameters. Margin m(σ̂) rises with volatility; that is the margin half of the Brunnermeier-Pedersen spiral.
- **(f) A liquidity provider** as an agent with inventory and cash. Every trade has a counterparty, so conservation of units and cash becomes a unit test.
- **(g) A loss-allocation hook** (insurance fund, auto-deleveraging, haircut) and an explicit **fixed-point selection** setting for the cascade solver.

**Clearing rule (Cath R1, R2).** The rule is a reduced-form stand-in for the Brunnermeier-Pedersen liquidity spiral:

  ln p_{s+1} − ln p_s = λ_s · x_s,  with λ_s = min{ λ₀ · exp(κ·(σ̂_s/σ̄ − 1)), λ_max }

- **R1 (units).** x_s is net order flow in **units of the asset as a share of the float**. Depth is normalised to 1, so λ₀ alone carries price impact and the rule does not depend on the price level. Noise flow is σ_ε·ε_s, with ε_s ~ N(0, 1/K) in float-share units. λ₀ and σ_ε are separately identified only through agent flows, whose scale is fixed because holdings and demands are fractions of each class's float share. Momentum demand is w_m·tanh(β·trend_h), with no free proportionality constant.
- **R2 (volatility input).** σ̂_s is realised volatility over the trailing 24 sub-steps, in per-sub-step units, and σ̄ is a fixed constant computed once from the hourly data snapshot (its post-ETF mean); it is not estimated. λ is capped at λ_max, and σ̂_s is **frozen during the cascade loop**, so impact and volatility cannot feed each other without bound.
- **R4b (transient impact).** A fraction φ of each sub-step's impact decays at rate ρ per sub-step, implemented as mean reversion in the liquidity provider's inventory. φ = 0 gives permanent impact, the v1 case, and is kept as an ablation. Without decay, the §1.3 intraday target cannot be met. Formally, log price is f_s + u_s. Each clearing adds (1−φ)·λ_s·x_s to the permanent part f and φ·λ_s·x_s to the transient part u. Between sub-steps, and never inside the cascade loop, u_{s+1} = (1−ρ)·u_s. The liquidity provider's inventory unwind is the accounting counterpart of this decay and is not routed back through λ, which preserves R3's order-independence.

**Cascade loop (Cath R3, R4).** After each sub-step's ordinary clearing:
- (a) **only forced orders act inside the loop**; momentum and noise orders act once per sub-step;
- (b) **each constraint fires once per crossing**: a liquidation closes the position, and a conviction sale sets a flag that resets only on re-entry;
- (c) **each round's forced orders clear as one batch**.

Under (a)–(c), forced flow has one sign and grows as the price falls. The loop ends within N rounds, where N is the number of constrained agents. With λ frozen, log impact is additive, so the end price does not depend on the order of execution. The solver selects the **fixed point nearest p_s**, as in Cifuentes-Shin-Ferrucci (2005). The deeper fixed points are the run equilibria a sovereign instance will need; selecting them is setting (g).

The iteration cap is N + 1. **A binding cap is a bug**: the draw is aborted and logged, never kept as data.

If B1 finds that cascades need *time* within the day to match §1.3, the variant "at most M rounds per sub-step, remaining forced orders carried to the next sub-step" is declared and tested as a named alternative.

**What the crypto adapter adds:**
- the funding rate, computed from the long/short imbalance of leveraged agents and charged to their equity;
- ETF creations and redemptions, and treasury-company issuance, through the primary-market rule (B2);
- the data interfaces (Coinbase closes, venue open interest).

**Single price for perp and spot (Cath rec. 1).** Until B3 adds a second market, perp and spot trade at one price. That assumes instant arbitrage between them, and the assumption is stated wherever results are reported.

---

## 3. Agents and phases

### 3.1 B1 — the minimal model (three classes, noise, liquidity provider)

| Class | Rule | What it carries |
|---|---|---|
| **Conviction holders** (share w_c) | Hold. Each agent sells a fraction once the drawdown from its own reference price passes its threshold D_i, and re-enters slowly. **Thresholds differ across agents**, drawn from a distribution. | Runs: Granovetter-style thresholds |
| **Momentum traders** (w_m) | Demand ∝ tanh(β · trend_h), with horizons h that differ across agents | Amplification, volatility clustering |
| **Leveraged perp traders** (w_ℓ) | Take a direction from a momentum signal plus noise, with leverage L_i drawn from a distribution and margin m(σ̂). They are liquidated at the liquidation price and pay or receive the endogenous funding rate. | Fire sales and cascades |
| **Noise order flow** | Gaussian, independent | The crypto adapter's only exogenous input |
| **Liquidity provider** | Clears net flow against inventory; inventory mean-reverts (φ, ρ) | Price impact; conservation; transient impact |

### 3.2 Later classes

- **B2:** ETF investors and authorized participants, with flows = a + b · past returns + noise, cleared through the primary market. Treasury companies issue equity and buy coin when mNAV > 1 + θ, and sell coin when debt falls due on the event calendar and mNAV < 1.
- **B4:** stablecoin holders and issuer, where redemptions force T-bill sales (the link to Nina's Duffie-Reis model). Also miners, who sell production on falling hashprice and switch capacity to AI hosting.

### 3.3 One asset first

B1 models **BTC alone** (D5). Matching the BTC–ETH correlation (0.83) and ETH's beta (1.18) needs agents trading both assets, which comes in B3.

### 3.4 Phase map, reconciled with spec §5.6 (Fina req. 3)

| Phase | Content | Spec §5.6 |
|---|---|---|
| B0 | This note (v1, v1.1) and the reviews | B0 |
| **B1a** | CPU engine with the R5 core stubs, BTC adapter, targets recomputed from a committed data snapshot, null and ablation tests, **parameter recovery**, a rough fit to post-ETF moments | B1 |
| **B1b** | Batched-simulation timing gate, CPU threads vs GPU (§8). It may move to B3 if B1a runs long. | B1 (part) |
| B2 | ETF and treasury-company agents (primary market, event calendar); cascade experiments E1–E3; regime-shift test (§6.1); recalibration now that ETF agents exist | B2 |
| B3 | **SMM calibration** on the full moment vector; two-asset engine (BTC + ETH) and perp/spot markets | B3, plus the two-asset extension |
| B4 | Stablecoin and miner agents; Duffie-Reis link | B4 |

The spec carries a dated amendment line pointing to this table.

---

## 4. Parameters (initial search ranges, not estimates)

| Parameter | Meaning | Initial range |
|---|---|---|
| w_c, w_m, w_ℓ | Class shares | simplex, w_ℓ ∈ [0.02, 0.30] |
| D_i ~ LogNormal(μ_D, s_D) | Conviction drawdown thresholds | median 15–50 % |
| β, h | Momentum intensity, horizons | h ∈ [3, 60] days |
| L_i ~ LogNormal(μ_L, s_L), m₀, m₁ | Leverage; margin m(σ̂) = m₀ + m₁·σ̂ | median L 3–20×; m₀ 0.5–2 %; m₁ ≥ 0, range to be scaled in B1a (σ̂ in per-sub-step units) |
| λ₀, κ, λ_max | Impact per unit of float, volatility sensitivity, cap | to be scaled in B1a |
| φ, ρ | Transient share of impact, decay per sub-step | φ ∈ [0, 0.8], ρ ∈ [0.05, 0.5] |
| σ_ε | Noise order-flow scale | free (unit scale fixed by R1). *Amendment 2026-11-17 (B1a): searched on [0.002, 0.05]; the fit sits at the upper bound under both impact laws. RULED 2026-11-17 (Héctor): the bound stays and is noted; widening it is a separate recorded decision.* |
| K | Sub-steps per day | 24 (D4), an instance parameter |

---

## 5. Calibration

- **Method:** simulated method of moments, with full SMM in **B3**. B1a only checks that some parameter vector reaches the bootstrap bands, and runs the recovery test.
- **Moment vector:** s.d.; ACF of r at lag 1; ACF of |r| at lags 1, 5 and 20; Hill tail index (top 5 %); share of 3σ days (90-day trailing s.d.); skewness; share of days with simple |r| > 10 %. From B1a, add the gap between the prior-close-to-low and close-to-close returns on the largest down days.
- **Weighting matrix:** from a moving-block bootstrap of the data moments (block of 20 days). The Bayesian bootstrap (Andrews–Moon–Shapiro 2026, mapped in Research) is a later, separate option.
- **Simulation:** 1,040 days per path, at least **10 replications per draw**, with common random numbers.
- **Optimiser:** liquidation thresholds make the moments jump in steps as parameters move. Use a derivative-free optimiser (CMA-ES or Nelder–Mead on the common-random-numbers objective), or smoothed triggers, declared up front. The parameter-recovery test uses the **same optimiser**.
- **Recovery first:** simulate from known parameters and recover at least w_ℓ, median L, s_D and κ with stated coverage. Name the parameters that are not identified.
- **Report a set, not a point:** every vector inside the J-test acceptance region, and which conclusions hold across all of it.
- **Recalibration:** B1a fits post-ETF moments without ETF agents, so the fit is provisional and is redone in B2.

---

## 6. Validation

1. **Regime-shift test, in B2.** After ETF agents exist, change **one factor at a time** from the post-ETF calibration: first the ETF holder share alone, then leverage alone. Leverage changes are **taken from data**, such as sourced open-interest-to-market-cap ratios for the two periods, not fitted freely. Targets are the s.d. and the share of simple 10 % days, per §1.1. The tail index is not a target here, because it does not move.
2. **Intraday realism.** Does the model, with transient impact, produce prior-close-to-low vs close-to-close gaps like 2025-10-10 (−12.1 % vs −7.2 %)? With φ = 0 it should fail; that is the ablation.
3. **Limitations, stated with each result:**
   - Equifinality.
   - Sensitivity to the clearing rule (re-run key experiments with a linear-impact alternative).
   - The perp = spot assumption.
   - Regime dependence: a post-ETF calibration may not survive the next structural change.

---

## 7. Experiments, and the bridge to the board

| | Question | Output form |
|---|---|---|
| E1 | Leveraged share × leverage distribution → cascade days | Frequency of days with a prior-close-to-low below −X %, as a surface over (w_ℓ, median L) |
| E2 | ETF holder share and flow sensitivity b → drawdown amplification (B2) | Ratio of drawdown depth with vs. without flow feedback |
| E3 | Treasury-company financing wall: debt due when mNAV < 1 (B2) | mNAV and debt-size threshold at which forced sales enter the cascade loop |
| E4 | Spread of conviction thresholds → run emergence | Critical dispersion s_D at which a moderate shock tips a run |

**Bridge to the board (Fina req. 5).** The board's unruled bands are the stablecoin peg band, the liquidation-volume bar and the funding/open-interest "stretched" levels (crypto_monitor README). The board has no drawdown leg, and this note does not propose one. Rules:
1. Board bands are ruled on **observed data now**. They do not wait for the model.
2. An experiment may motivate a question to Héctor **only when stated in board-observable units**, such as a funding rate per 8 h, an open-interest share, or a liquidation volume. The question gives the range across the accepted parameter set (§5) and the model run id. The model has no dollar scale until B2/B3 adds one from data (§2, R1); until then, E1 can speak only to funding and open-interest *shares*, not to dollar liquidation volumes.
3. Any ruling is recorded in the board README and the state text, with the run id. No model number appears on the dashboard.

---

## 8. Implementation

- **Location (Fina req. 7):** B1 is **not** developed or run in the sparse `Dalila-spcx` worktree. That worktree covers only the three monitor folders, has no `tests/`, and is `reset --hard main` daily at 18:00. **Branch and checkout (ruled 2026-11-16, option C):** B1 code goes on a new branch `aurora-crypto-abm` cut from main, in its own full checkout `~/Dalila-abm`. It is merged into main when the §11 criteria are met. This note, the spec, the board and the build instruction stay on main.
- **Folder:** `GrandPlan/Aurora/crypto_abm/` with its own `Project.toml` (Julia 1.11.7), `src/core/`, `src/adapters/crypto/`, `targets/` (the Appendix A computation plus a committed data snapshot with a SHA-256 checksum) and `experiments/`. Every module gets a `.md` companion.
- **Technology (D2):** the engine core is plain Julia struct-of-arrays. Agents.jl is used only for prototyping and visual checks in B1a.
- **CPU or GPU:**
  - *One simulation runs on the CPU.* It is a sequential chain of 24 sub-steps and a cascade loop, branchy and with small arrays. Replications are spread across CPU threads.
  - *Batches of simulations are the GPU candidate.* Thousands of independent draws × replications can run one simulation per thread with CUDA.jl, with moments computed on the device. This is gated in B1b by a timing table: CPU single run, CPU threaded batch, GPU batch at 1k and 10k draws, with `nvidia-smi` showing the GPU working. The GPU path is kept only if it wins by a stated margin; otherwise the batch stays on CPU threads and the note says why.
  - *GPU check.* When CUDA.jl enters the `Project.toml`, `tests/gpu_check.jl` is run in that environment (CLAUDE.md §9).
  - *Memory.* Dalila's 8 GB is enough for B1. Larger sweeps go to Ester in B3, once Ester has its NVIDIA driver and the infrastructure is ready.
- **Runs:** long jobs inside Zellij, never killed mid-run to tweak.

---

## 9. What an OLG-ABM interface could carry (rewritten in v1.1, Cath R6)

This is for Cath to design. It records what the reviews established.

**What the OLG produces today.** The BID2 OLG (`ge_model_gender.jl`, `run_aging_ssvs.jl`):
- is a stationary solver with five-year periods;
- is closed (K = A_dom − B), with one riskless bond;
- treats debt as a residual (B = primary / (r_n − n_p));
- yields comparative steady states for 2020 and 2050;
- under the "debt absorbs" reading of closure C2 (pension deficit routed to the general budget), has no finite steady state; the C2 that was shipped uses benefit scaling.

It has no transition path, maturity structure, currency composition, holder split or spread. No DFD transition solver was found.

**What could flow, once a transition solver exists:**
- **OLG → ABM**, by scenario and closure, annually: debt/GDP, primary balance, r − n, and **domestic asset demand by age**. That last item is the capacity of captive holders such as the AFOREs, which only the OLG can supply.
- **Exogenous to both:** maturity, currency and foreign share, from sourced and dated debt-management data. Using them consistently requires an **open-economy closure** first; a closed OLG implies zero foreign financing.
- **ABM timing:** one-year slices with fundamentals held fixed.
- **ABM → OLG:** no spread path and no fixed-point coupling. At most, a boundary the closure must respect, or a crisis branch solved as a separate scenario. The OLG's r stays the fundamental rate, and model yields are never fed back.

**The interface object.** The headline is **not** a frequency of rollover failure. Inside the multiple-equilibrium zone, that frequency is set by the coordination shock the modeller assumes, so it would read like a probability it is not. The objects are instead:
- the **crisis-zone boundary**: the set of states (debt, maturity, holder mix, backstop) where a self-fulfilling run exists;
- the **minimum coordinated shock z*** that makes an auction fail.

Both are indexed by **state, never by date**. The OLG path is overlaid on them: "under scenario S and closure C, the path enters the zone at debt d". The equilibrium-selection rule (§2, g) is always named.

This does **not** yet meet the Monetary Foundation §10 aim of an interface specification delivered with the design note. It is a sketch of requirements. The sovereign instance itself waits until the crypto instance has passed B3 (spec §5.7).

---

## 10. Decisions (ruled 2026-11-16 by Héctor)

- **D1 — Calibration window.** Post-ETF for calibration; 2019–2023 as the regime-shift test. *v1.1 note: per §1.1, the test is about volatility level and large-day frequency, run in B2.*
- **D2 — Engine technology.** Plain Julia struct-of-arrays for the core; Agents.jl only for B1a prototyping and visual checks.
- **D3 — Tail moments.** Hill index and 3σ-day share targeted; raw kurtosis reported, not targeted.
- **D4 — Intraday sub-steps.** K = 24 per day, an instance parameter, with hourly Coinbase candles as intraday target data.
- **D5 — First asset.** BTC alone in B1; two-asset engine in B3.
- **D6 — Review.** Cath reviews §2 and §9, **with Fina's help** (amended by Héctor). Both reviews are filed; v1.1 applied their required changes; Cath and Fina each endorsed v1.1 with minor fixes on 2026-11-16, applied in v1.2.

**Branch (ruled 2026-11-16):** option C — build record and documents on main; B1 on branch `aurora-crypto-abm` in `~/Dalila-abm` (§8).

---

## 11. B1 acceptance criteria (Fina, adopted)

1. **Layout.** The §8 layout under Julia 1.11.7, with a `.md` companion per module. A grep test finds no crypto terms (funding, perp, BTC, Coinbase, UTC) in `src/core/`.
2. **Reproducible targets.** `targets/` recomputes §1 from the committed snapshot, conventions stated, and matches this note.
3. **Null test.** With noise only and κ = 0, excess kurtosis and the ACF of |r| are about zero.
4. **Stylized facts.** At least one parameter vector puts post-ETF BTC moments inside block-bootstrap 95 % bands: ACF of r, ACF of |r| at lags 1/5/20, Hill index, 3σ share. Misses are listed.
5. **Ablation.** Switching off the cascade loop, and separately setting φ = 0, moves the tail and intraday moments materially; and, separately, setting κ = 0, so that the share of clustering and tails due to liquidity withdrawal alone is reported.
6. **Parameter recovery.** On synthetic data, recover at least w_ℓ, median L, s_D and κ with stated coverage, using the §5 optimiser. Parameters that are not identified are named.
7. **Determinism and conservation.** A fixed seed gives bit-identical runs, with common random numbers across draws, and units and cash are conserved across all agents, including the liquidity provider, to machine precision.
8. **Timing and GPU.** The B1b timing table, plus `gpu_check.jl` if CUDA is used, or an explicit CPU-only statement.
9. **Firewall.** A test that nothing under `crypto_abm/` reads or writes `crypto_monitor/`; the README restates the firewall.
10. **Limitations.** Equifinality, a run with the linear-impact alternative, the perp = spot assumption, and regime dependence.
11. **Sign-off.** The build instruction is filed; Cath and Fina sign off.

---

## 12. Cadence (Fina, adopted as the plan of record)

- **By mid-January 2027:** B1a done, B1b done or moved to B3, B2 under way.
- **B3** once Ester is ready, which matches the deferral of the CIEP/ITED research group.
- **B4** not before Q1 2027. It depends on a Duffie-Reis monetary ABM that has no design note yet.

---

## Appendix A — How the §1 figures were computed (reproduce in B1a)

- **Data:** Coinbase Exchange public candles, `https://api.exchange.coinbase.com/products/{BTC-USD,ETH-USD}/candles?granularity=86400`, fetched 2026-11-16 in 299-day windows from 2019-01-01. Close = index 4 of `[time, low, high, open, close, volume]`. Only UTC days closed by 2026-11-16 are kept: 2,877 per product, consecutive days, no gaps. B1a commits this snapshot with a SHA-256 checksum.
- **Returns:** r_t = ln(C_t / C_{t−1}), formed within each window; the window's first day contributes no return. Episodes and worst days are reported as exp(r_t) − 1.
- **Moments:**
  - s.d. with ddof = 1, annualised × √365;
  - skewness and excess kurtosis = mean(z³) and mean(z⁴) − 3, with z standardised by the ddof = 1 s.d.;
  - ACF at lag k = Σ(x_t − x̄)(x_{t+k} − x̄) / Σ(x_t − x̄)²;
  - Hill index = 1 / mean(ln(a_(i) / a_(k+1))) over the k = ⌊0.05·n⌋ largest |r|;
  - 3σ day: |r_t| > 3 × s.d.(r_{t−90..t−1}), where the trailing s.d. uses the full return history, including returns before the window opens. In the column that excludes 2020-03-12, that day is removed from the count but kept in the trailing s.d. Alternatives, reported for transparency: with a within-window trailing s.d., post-ETF BTC is 1.58 % and ETH 1.68 %; with 2020-03-12 dropped from the series, pre-ETF BTC is 2.08 % and ETH 1.79 %;
  - correlation and beta (cov(ETH, BTC) / var(BTC)) on daily log returns.
- **Drawdown:** on closes, from the running maximum within the window.
- **Windows:** 2019-01-01..2023-12-31 (1,825 returns; 1,824 excluding 2020-03-12) and 2024-01-11..2026-11-16 (1,040 returns).
- **2025-10-10:** that day's Coinbase daily candle: open $121,714.51 = prior close; low $107,000; close $112,980.28.

*Nina · Aurora · GrandPlan · November 2026 · design note v1.2; no code written in B0.*
