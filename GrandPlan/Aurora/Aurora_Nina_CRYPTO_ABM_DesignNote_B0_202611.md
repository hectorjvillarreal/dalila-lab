# Design note B0 — Crypto agent-based model (mechanism laboratory)

*Document type: Design note (phase B0 of Part B) · Aurora Project*
*Author: Nina (portfolio management & crypto strategy) — drafted by Claude Code in Nina's role at Héctor's request, 2026-11-16*
*Status: B0 APPROVED 2026-11-16 — decisions D1–D6 ruled (§10; D6 amended: Fina helps Cath). No code is written in B0; B1 waits for Héctor's go and the Cath/Fina review.*
*Parent spec: `Aurora_Nina_CRYPTO_BR_Spec_ClaudeCode_202611.md`, Part B (§5) and §5.7 (design for reuse)*
*Precedent: `Aurora_Nina_MonetaryFoundation_202604.md` §10 (design note before code)*

---

## 0. What this model is for, and the firewall

The model is a **laboratory for mechanisms**. It must reproduce the statistical signature of crypto returns from agent behaviour alone, with only plain Gaussian noise as input. Then it asks **conditional** questions, for example: with this share of leveraged traders at this leverage, how often does a liquidation cascade turn a 3 % day into a 12 % day?

It never says where bitcoin or ether will trade.

The firewall from the spec (§0) applies without exception:
- No model output enters the crypto board's state files.
- A model result reaches the board only as a **question for Héctor's ruling**. For example, "experiment E1 suggests a liquidation-volume RED bar of X; adopt it?"
- The model is not connected to the DSGE-OLG core. §9 only sketches what an interface could carry, for Cath to design.

The target is the same kind Nina set for the monetary model: a crisis that **emerges from coordination**, without an exogenous shock large enough to explain it. There it was the September 2019 repo spike; here it is a liquidation cascade or a holder run.

---

## 1. What the data says the model must reproduce

I computed these from Coinbase daily UTC closes for BTC-USD and ETH-USD, 2019-01-01 to 2026-11-16: 2,877 closes each and no missing days. Moments use log returns; the worst-day and episode figures (§1.1 last rows, §1.3, §1.4) are simple price changes. The method is in Appendix A so that B1 can recompute every figure. Grade: MARKET data, our computation.

### 1.1 Two regimes, not one

The launch of US spot bitcoin ETFs (2024-01-11) splits the sample cleanly:

| Moment | BTC 2019–2023 | BTC post-ETF (2024-01-11 → 2026-11-16) | ETH 2019–2023 | ETH post-ETF |
|---|---|---|---|---|
| Daily s.d. (annualised) | 3.63 % (69.5 %) | **2.45 % (46.9 %)** | 4.65 % (88.9 %) | **3.50 % (67.0 %)** |
| Skewness | −1.32 | **+0.11** | −1.23 | **+0.29** |
| Excess kurtosis | 20.7 | **3.44** | 15.6 | **3.88** |
| ACF of returns, lag 1 | −0.078 | −0.046 | −0.099 | −0.011 |
| ACF of \|r\|, lag 1 / 5 / 20 | 0.158 / 0.098 / 0.044 | **0.156 / 0.100 / 0.038** | 0.166 / 0.117 / 0.053 | **0.140 / 0.058 / −0.009** |
| Share of days with \|log r\| > 0.10 | 2.19 % | 0.28 % | 3.94 % | 2.01 % |
| Worst day | −38.8 % (2020-03-12) | −14.0 % (2026-02-05) | −43.3 % (2020-03-12) | −14.9 % |
| BTC–ETH correlation; ETH beta to BTC | 0.84; 1.07 | **0.83; 1.18** | | |

Post-ETF maximum drawdowns: BTC −53.1 % ($124,720 on 2025-10-06 to $58,524 on 2026-06-30); ETH −67.6 % ($4,831 on 2025-08-22 to $1,565 on 2026-06-25). On 2026-11-16, BTC is 48.0 % and ETH 62.3 % below their post-ETF closing highs.

**Design consequence.** The model is **calibrated on the post-ETF window**, and the pre-ETF window is a **regime-shift test** (§6). This is a natural experiment the model should pass: lowering the ETF holder share and raising leverage, with no other change, should move the simulated moments toward the pre-ETF column. If the model can do that, the ETF share is doing mechanism work. If it can't, the model is missing something.

### 1.2 Raw kurtosis is too fragile to calibrate on

A single day, 2020-03-12, accounts for almost all of the full-sample kurtosis. Removing it lowers BTC excess kurtosis from 21.1 to 4.1, and ETH's from 14.7 to 4.7. A moment that one observation can move fivefold is a poor calibration target.

**Design consequence.** The model uses **robust tail moments**: a Hill tail index on the top 5 % of |r|, and the frequency of days beyond 3 rolling standard deviations. Raw kurtosis is reported but not targeted (decision D3).

### 1.3 Daily closes hide the cascades

On 2025-10-10, BTC's daily close was −7.2 %, while the Coinbase daily candle ran from a $121,714.51 open to a $107,000 low, −12.1 % intraday. ETH closed −12.2 % that day. A model that steps once a day cannot represent a cascade that starts and partly reverses within hours.

**Design consequence.** Each simulated day has **intraday sub-steps** (decision D4), and the daily close is the last sub-step. B1 adds an intraday target: the gap between the intraday low and the close on the largest down days. It needs hourly candles (Coinbase granularity 3600), to be fetched in B1.

### 1.4 Episodes to be sourced in B1

These are the largest daily drops in the sample. The usual explanations are listed only to orient B1, which must source each cause before it is used:

| Date | BTC | ETH | Usually attributed to |
|---|---|---|---|
| 2020-03-12 | −38.8 % | −43.3 % | Pandemic liquidity crash |
| 2021-05-19 | −14.3 % | −27.6 % | Leverage unwind / mining-ban news |
| 2022-06-13 | −15.4 % | | Lender freezes (Celsius) |
| 2022-11-09 | −14.4 % | −17.6 % | FTX collapse |
| 2025-10-10 | −7.2 % close, −12.1 % intraday | −12.2 % | Large leveraged deleveraging |
| 2026-02-05 | −14.0 % | | **Not known to us — source in B1** |
| 2026-11-13/14 | −4.4 %, −6.0 % | −4.4 %, −8.3 % | Press: ETF outflows, hike bets, $1–2B liquidations (totals disagree) |

---

## 2. Architecture: a generic engine and a crypto adapter

As the spec requires (§5.7), the **core knows nothing about crypto**. A sovereign bond market should be a second adapter, not a rewrite.

**Core objects:**
- **Agent class.** A population of agents sharing a behavioural rule. Each agent has a balance sheet (cash, units of the asset, debt), a belief state (a signal it reads and a confidence level) and constraints: margin, redemption rules, mandate.
- **Constraint.** A test that can turn into a *forced* order: margin breach → liquidation; redemption → sale; mandate breach (a rating floor in the sovereign case) → sale.
- **Market.** One asset per instance in B1. Net order flow clears through a price-impact rule. Market depth shrinks when volatility rises, because the liquidity provider withdraws. That is the liquidity spiral of Brunnermeier and Pedersen, written as one equation.
- **Cascade loop.** After each price move, all constraints are re-checked, forced orders are added, and the market clears again. This repeats until no new forced order appears, or until a cap on iterations is reached and the event is recorded. **This loop is the fire-sale mechanism made explicit**, and the place where runs and cascades emerge.

**Clearing rule (initial):**

  p_{s+1} = p_s · exp(λ_s · X_s / D),  with λ_s = λ₀ · exp(κ · σ̂_s)

Here X_s is net order flow at sub-step s, D is a depth scale and σ̂_s is recent realised volatility.

**What the crypto adapter adds:** the funding rate, computed inside the model from the long/short imbalance of leveraged agents and charged to their equity; ETF creations and redemptions; treasury-company equity issuance; and the data interfaces (Coinbase closes, venue open interest).

---

## 3. Agents

### 3.1 B1 — the minimal model (three classes plus noise)

| Class | Rule | What it carries |
|---|---|---|
| **Conviction holders** (share w_c) | Hold. Each agent sells a fraction once the drawdown from its own reference price passes its threshold D_i, and re-enters slowly. **Thresholds differ across agents**, drawn from a distribution. | Runs: Granovetter-style thresholds. When one agent's exit pushes the price past the next agent's threshold, the run becomes self-fulfilling. |
| **Momentum traders** (w_m) | Demand ∝ tanh(β · trend_h), with trend horizons h that differ across agents. | Amplification and volatility clustering |
| **Leveraged perp traders** (w_ℓ) | Take a direction from a momentum signal plus noise, with leverage L_i drawn from a distribution and maintenance margin m. They are liquidated at the liquidation price: a long becomes a forced sell, a short a forced buy. They pay or receive the endogenous funding rate. | Fire sales and cascades |
| **Noise order flow** | Gaussian, independent day to day | **The only exogenous input.** Fat tails and clustering must come from the agents, not from the noise. |

The liquidity provider is part of the clearing rule, not a fourth class.

### 3.2 Later phases

- **B2:** ETF investors and authorized participants, with flows = a + b · past returns + noise, converted into same-day spot orders. Treasury companies issue equity and buy coin when mNAV > 1 + θ. When debt comes due and mNAV < 1 they sell coin, and mNAV itself moves with coin returns.
- **B4:** stablecoin holders and issuer, where redemptions on falling peg confidence force T-bill sales (the exit to Nina's Duffie-Reis model). Also miners, who sell production as hashprice falls and switch capacity to AI hosting above a threshold.

### 3.3 One asset first

B1 models **BTC alone** (decision D5). The BTC–ETH correlation and ETH's higher beta (0.83; 1.18) need agents trading both assets. That becomes a B3 extension of the engine: a second market sharing the momentum and leveraged populations.

---

## 4. Parameters (initial ranges to explore, not estimates)

| Parameter | Meaning | Initial range |
|---|---|---|
| w_c, w_m, w_ℓ | Class shares (sum to 1 with noise weight) | simplex, w_ℓ ∈ [0.02, 0.30] |
| D_i ~ LogNormal(μ_D, s_D) | Conviction drawdown thresholds | median 15–50 % |
| β, h ~ U | Momentum intensity, horizons | h ∈ [3, 60] days |
| L_i ~ LogNormal(μ_L, s_L), m | Leverage, maintenance margin | median L 3–20×, m 0.5–2 % |
| λ₀, κ, D | Price impact, liquidity withdrawal, depth | to be scaled in B1 |
| σ_ε | Noise order-flow scale | free |
| K | Intraday sub-steps per day | 24 (D4) |

These ranges are design choices for search, labelled as such. None of them is a finding.

---

## 5. Calibration

- **Method:** simulated method of moments (SMM).
- **Moment vector:** s.d.; ACF of r at lag 1; ACF of |r| at lags 1, 5 and 20; Hill tail index (top 5 %); frequency of 3σ days; skewness. In B1, add the gap between intraday low and close on large down days.
- **Weighting matrix:** from a moving-block bootstrap of the data moments (block about 20 days). The Bayesian bootstrap already mapped in Research (Andrews–Moon–Shapiro 2026) is a later, separate option, under the one-method-at-a-time rule.
- **Simulation:** each draw runs 1,040 days, matching the post-ETF sample, with common random numbers across draws.
- **Parameter-recovery test first.** Simulate data from known parameters and check that the procedure recovers them. If it can't, the moments don't identify the model, and real calibration would only produce numbers.
- **Report a set, not a point.** Because of equifinality, report every parameter vector inside the J-test acceptance region, and say which experiment conclusions hold across that whole set.

---

## 6. Validation

1. **Regime-shift test (§1.1).** Calibrate post-ETF, then lower the ETF share and raise leverage. Do the simulated moments move toward the 2019–2023 column, especially the tail index and the frequency of 10 % days?
2. **Intraday realism (§1.3).** Does the cascade loop produce intraday-to-close gaps like 2025-10-10 (−12.1 % intraday vs −7.2 % at the close)?
3. **What it cannot do, stated with each result:**
   - Equifinality.
   - Sensitivity to the clearing rule (re-run key experiments with a linear-impact alternative).
   - Regime dependence: the post-ETF calibration may not survive the next structural change, such as a stablecoin law or a second ETF wave.

---

## 7. Experiments, each stated as a conditional result

| | Question | Output form |
|---|---|---|
| E1 | Leveraged share × leverage distribution → frequency and size of cascade days | Frequency of days below −X % as a surface over (w_ℓ, median L) |
| E2 | ETF holder share and flow sensitivity b → drawdown amplification | Ratio of drawdown depth with vs. without flow feedback |
| E3 | Treasury-company financing wall: debt due when mNAV < 1 → forced coin sales | Threshold of mNAV and debt size at which forced sales enter the cascade loop |
| E4 | Spread of conviction thresholds → run emergence | Critical dispersion s_D at which a moderate shock tips a run |

**Bridge to the board:** E1 and E4 are the natural sources of the numeric bands the crypto board still lacks: the liquidation-volume bar and the drawdown-run leg. Each reaches the board only as a ruling question to Héctor.

---

## 8. Implementation (for B1, after approval)

- **Folder:** `GrandPlan/Aurora/crypto_abm/` with its own `Project.toml` (Julia 1.11.7), `src/core/` (asset-agnostic), `src/adapters/crypto/`, `targets/` (the Appendix A computation as a script) and `experiments/`. Every module gets a `.md` companion, per the Dalila convention.
- **Agents.jl or plain Julia arrays (decision D2).** Agents.jl is installed and good for prototyping and visual checks. For the engine core I recommend **plain struct-of-arrays Julia**, one vector per agent class, for three reasons:
  - SMM needs millions of agent-steps per draw times thousands of draws.
  - Arrays carry over to the sovereign adapter without Agents.jl's grid and space abstractions.
  - The GPU path is direct.

  This departs from the Monetary Foundation's "Agents.jl" line, so it is your call.
- **CPU or GPU: both, for different jobs, decided by profiling (DFD GPU strategy).**
  - *One simulation → CPU.* A single run is a sequential chain: day → 24 sub-steps → a cascade loop that repeats until no new liquidation. Each step depends on the last, the loop is branchy, and agent arrays are small (thousands, not millions). On a GPU, every sub-step would pay kernel-launch and synchronisation costs larger than the work. Single runs, debugging and the experiments' individual paths stay on the CPU, threaded across replications.
  - *Calibration → GPU (the default heavy path).* SMM needs thousands of parameter draws × replications, all independent. That is embarrassingly parallel: one simulation per GPU thread (or per block), written as a CUDA.jl kernel over struct-of-arrays state, with the moment computation on the device too. This is where the model's compute actually goes, and where the GPU should pay.
  - *Gate before committing to the GPU path.* B1 ships a timing table: CPU single-run time, CPU threaded batch, GPU batch at 1k and 10k draws. It verifies the GPU is actually used (nvidia-smi utilisation during the batch, not just a CUDA call that falls back to the CPU). The GPU path is kept only if it wins by a stated margin. If not, the note records why and the batch stays on CPU threads.
  - *Memory.* Dalila's 8 GB holds about 10k simultaneous BTC simulations if per-simulation state stays in the low hundreds of KB (to be measured in B1). Larger sweeps, and the two-asset and sovereign instances, move to Ester (24 GB) once the infrastructure is ready, about two months out.
- **Runs:** long calibration jobs inside Zellij; never killed mid-run to tweak.

---

## 9. Sketch for Cath: what an OLG-ABM interface could carry

This is only a sketch, to show the engine can bear it; the design is Cath's. In a sovereign instance:
- **The OLG core supplies:** the debt-to-GDP path implied by aging, the primary balance, maturity and currency composition.
- **The ABM's holder classes:** captive pension funds (AFOREs), domestic banks under a doom loop, foreign carry money, rating-constrained index funds, and the central bank.
- **The interface object:** a map from (debt path, holder composition) to the *conditional frequency of rollover failure*. That marks where the multiple-equilibrium zone begins along the OLG path.

It is a conditional statement, never a forecast of spreads, under the same firewall.

---

## 10. Decisions for Héctor (proposed defaults in brackets)

**RULED 2026-11-16 (Héctor): defaults D1–D5 accepted; D6 accepted with an amendment — Fina helps Cath with the review of §2 and §9.** B1 (code) still waits for Héctor's go.

- **D1 — Calibration window.** [Post-ETF (2024-01-11 → present) for calibration; 2019–2023 as the regime-shift test.]
- **D2 — Engine technology.** [Plain Julia struct-of-arrays for the core, with Agents.jl only for B1 prototyping and visual checks.]
- **D3 — Tail moments.** [Hill index and 3σ-day frequency targeted; raw kurtosis reported, not targeted.]
- **D4 — Intraday sub-steps.** [K = 24 per day, with hourly Coinbase candles as the intraday target data.]
- **D5 — First asset.** [BTC alone in B1; two-asset engine in B3.]
- **D6 — Review.** [Cath reviews §2 and §9 before B1 starts.] → RULED: Cath reviews, **with Fina's help** (cross-project coherence).

---

## Appendix A — How the §1 figures were computed (reproduce in B1)

- **Data:** Coinbase Exchange public candles, `https://api.exchange.coinbase.com/products/{BTC-USD,ETH-USD}/candles?granularity=86400`, fetched 2026-11-16 in 299-day windows from 2019-01-01. Close = index 4 of `[time, low, high, open, close, volume]`. Only UTC days closed by 2026-11-16 are kept (2,877 per product, consecutive days, no gaps).
- **Returns:** r_t = ln(C_t / C_{t−1}) for all moments; episode and worst-day figures are reported as simple changes exp(r_t) − 1.
- **Moments:** s.d. with ddof = 1, annualised × √365. Skewness and excess kurtosis are the 3rd and 4th standardized moments (minus 3). ACF at lag k is Σ(x_t − x̄)(x_{t+k} − x̄) / Σ(x_t − x̄)². Correlation and beta (cov(ETH, BTC) / var(BTC)) are on daily log returns.
- **Drawdown:** on closes, from the running maximum within the window.
- **Windows:** 2019-01-01..2026-11-16; 2019-01-01..2023-12-31; 2024-01-11..2026-11-16.
- **Kurtosis sensitivity:** recomputed on the full sample excluding the 2020-03-12 return.
- **2025-10-10 intraday:** from that day's Coinbase daily candle (open $121,714.51, low $107,000, close $112,980.28).

*Nina · Aurora · GrandPlan · November 2026 — design note only; no code written in B0.*
