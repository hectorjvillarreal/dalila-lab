# Brief for Claude Code — Crypto Brunnermeier-Reis Regime Monitor (BTC, ETH) and a separate Nina ABM

*Document type: Build specification / Knowledge File · Aurora Project*
*Author: drafted by Claude Code at Héctor's request, for Nina (portfolio management & crypto strategy)*
*Date: 16 November 2026*
*Status: Part A APPROVED and built 2026-11-16 (rulings Q1–Q5, §7); Part B not started — B0 design note waits for Héctor's go. Nina's review pending.*
*Companion to: `Aurora_Nina_SPCX_BR_Spec_ClaudeCode_202606.md` (the SPCX brief) and `Aurora_Nina_MonetaryFoundation_202604.md` §10 (Nina's ABM agenda)*

---

## 0. Scope discipline — read first

This brief covers **two separate things**, and the separation is the main point of the document.

- **Part A — a regime board for bitcoin and ether.** It is built on the same discipline as the SPCX monitor. Its only outputs are mechanism states (GREEN / AMBER / RED / INERT), the observable that drove each state, and the next escalation trigger. It has no price target, no fair value, no direction and no expected return. Daily automation carries values forward and renders; only Héctor, or an analyst he explicitly delegates, classifies.
- **Part B — an agent-based model (ABM) that Nina develops outside the board.** It is a laboratory for mechanisms: it asks under what conditions a run or a liquidation cascade emerges. It does not forecast prices.

**The firewall between A and B:**

1. No ABM output is ever written into a board state file, and no ABM number appears on the board's dashboard.
2. An ABM result can affect the board only through a **ruling by Héctor**: for example, "adopt a funding-rate threshold of X as the AMBER leg, motivated by ABM run B1-07". The ruling is recorded with provenance, as the SPCX rulings (a)–(k) are.
3. The ABM produces conditional statements ("given these agent shares and this leverage, a cascade occurs in N % of runs"), never "BTC will be at P".
4. Neither part connects to the DSGE-OLG core. The OLG-ABM interface stays Cath's design problem (SPCX brief §0; Monetary Foundation §10).

Why the split matters: a calibrated model always seems more authoritative than a board of filed facts. If the model fed the board directly, the board would start reporting the model's beliefs as if they were observations.

---

## 1. Why crypto, and why now

- **Bitcoin is already the canary.** The SPCX brief names "narrative assets (bitcoin) vs. cash-flow assets" as the capital-rotation signal. Ether was added to the gauge on 2026-11-16 at Héctor's request. As of 11-16, bitcoin is −24.2 % and ether −32.6 % since the 10-06 Nasdaq high, while SCHD is +9.2 %.
- **There is a filed edge to SPCX.** The SpaceX Q3 10-Q (acc. 0001628280-26-066880) reports 18,712 units of Bitcoin, cost $661M, fair value $1,573M at 09-30-2026, marked through other income. It is now an observable on the SPCX Fire Sales panel (`issuer_crypto_holdings`, added 11-16). It is small, an earnings mark and not a forced-sale channel.
- **Crypto shows the Brunnermeier-Reis mechanisms almost in pure form.** Stablecoins are redeemable claims (runs). Perpetual futures liquidate automatically at known margins (fire sales). One exchange is custodian for most US spot ETFs, and stablecoin issuers hold large T-bill books (interconnections). That makes it a good second object for the board, and a natural ABM target.

---

## 2. Part A — the five mechanisms for BTC/ETH

The board must encode all five mechanisms and grey out the inert ones, as the SPCX board does.

### 2.1 Runs (LIVE)

**Run objects.** (i) Spot-ETF holders (IBIT, ETHA and peers), who can redeem faster than the underlying absorbs. (ii) Stablecoin holders (USDT, USDC), whose redemptions force the issuer to sell reserves. (iii) Exchange depositors.

**Observables:**
- ETF net flows, derived from the issuers' daily shares-outstanding files.
- Stablecoin supply changes and peg deviations.
- Issuer reserve attestations (filed or published, dated).
- Exchange reserve changes (aggregator-grade, see §3).

**Threshold logic (to be ruled):**
- GREEN: flows mixed, pegs at par.
- AMBER: persistent ETF outflows on falling price, or a peg deviation beyond a ruled band.
- RED: outflows accelerating together with a peg break or a halt on redemptions.

### 2.2 Fire sales / leverage (LIVE)

**Channels.** (i) Perpetual-futures leverage: open interest, funding rates, liquidation volume. (ii) Digital-asset treasury companies (corporate holders financed with convertibles or preferred stock). These are filed: 10-Q, 8-K, and the weekly purchase 8-Ks some of them publish. The key observable is the market value relative to holdings, and whether it forces a seller when financing comes due. (iii) Miners' debt and hashprice. (iv) Ether staking and liquid-staking leverage (staking-token discount to ETH).

**Threshold logic (to be ruled):**
- GREEN: leverage moderate and no treasury company near a financing wall.
- AMBER: elevated open interest with stretched funding, or a treasury company trading below its holdings with debt coming due.
- RED: a liquidation cascade in progress (ruled volume bar), or a filed forced sale by a treasury company.

### 2.3 Interconnections (LIVE)

**Nodes.** Exchange-custodians of the ETFs; stablecoin issuers and their T-bill books (the link to Nina's Duffie-Reis money-market framework); miners moving into AI hosting (links to the Nvidia/CoreWeave/SPCX web already on the SPCX node map); corporate holders (SpaceX 18,712 BTC, filed; others by filing only).

**Threshold logic (to be ruled):**
- GREEN: no node under stress.
- AMBER: stress at one node (custodian incident, issuer attestation delay, miner default).
- RED: simultaneous stress at connected nodes.

### 2.4 Currency mismatch (INERT at asset level — LatAm hook proposed)

BTC and ETH are not issuers and carry no liabilities, so there is no asset-level mismatch. **Proposed hook (question Q2):** dollar-stablecoin use as a dollarization channel in Latin America (Argentina, Mexico), where households hold USD claims against peso incomes. This sits close to Héctor's fiscal-demographic work. Display it greyed out unless the ruling activates it.

### 2.5 Inflation-deflation (INERT at asset level; macro hook)

This is the same macro panel as SPCX: TIPS 10y, VIX, the rotation gauge and broad risk-on/off, plus one proposed crypto-specific context field: stablecoin T-bill holdings as a share of the bill market (Duffie-Reis link). It is context only and never an escalation trigger.

---

## 3. Data discipline

- **No fabricated numbers.** An unavailable value renders as "unset / manual", exactly as in `spcx_monitor.py`.
- **Grades of source**, each recorded in the field text:
  - FILED: SEC filings, issuer attestations.
  - MARKET: Coinbase UTC daily closes; ETF shares outstanding from the issuer.
  - AGGREGATOR: derivatives data such as open interest, funding and liquidations, and on-chain exchange reserves.
  - PRESS.

  Under the 10-08 SPCX ruling, press items escalate nothing until filed. **Question Q3:** can AGGREGATOR-grade derivatives data drive a Fire Sales leg? It is the only source for perpetual-futures leverage.
- **Crypto trades 24/7.** The daily reading uses the Coinbase UTC daily close, the convention already used for the rotation gauge. A weekend move is read on the next pass and never backfilled.

---

## 4. Part A — what to build (after the rulings)

- **Folder:** `GrandPlan/Aurora/crypto_monitor/`, with the same pattern as `spcx_monitor/`: `taxonomy.py` (five mechanisms, observables, thresholds), `state/YYYY-MM-DD.json`, a `render` that writes `dashboard.html` and rebuilds `run_log.md`, and a README with a manual-pass checklist. Reuse the SPCX code by copying and adapting it, not by importing across folders. The two boards must be able to change independently.
- **Wiring:** run it as an extra step inside `~/.local/bin/spcx_render.sh`, as `nvda_watch` does, **not** on a second timer. A second timer would race the SPCX job for the git index on boot catch-up (the 10-03 and 10-07 repo crashes). The `reset --hard main` / `new` guard and the 600 s `ExecStartPre` apply unchanged. The sparse worktree needs the folder added to its sparse-checkout.
- **Cross-link:** SPCX's `issuer_crypto_holdings` stays on the SPCX board. The crypto board may cite it as an interconnections node but does not own it.
- **Non-goals encoded in the UI:** the same as SPCX §4. No price target field, no buy/sell, no expected return.

---

## 5. Part B — Nina's ABM (outside the board)

### 5.1 Purpose

The ABM is a mechanism laboratory. It reproduces the stylized facts of crypto returns from agent behaviour and then asks conditional questions: what mix of leverage, ETF ownership and treasury-company financing makes a liquidation cascade or a stablecoin run self-fulfilling. This is the same target as Nina's monetary agenda, an emergent coordination failure with no exogenous shock (Monetary Foundation §10, September 2019 repo spike).

### 5.2 Candidate agent types (for the design note to choose from)

| Agent | Behavioural rule (sketch) | Mechanism it carries |
|---|---|---|
| Conviction holders | Rarely trade; sell only on large drawdowns | Holder-base stability (Runs) |
| Trend / momentum traders | Buy on past returns, sell on reversals | Amplification |
| Leveraged perpetual traders | Margin with known liquidation prices; forced exit | Fire sales |
| Market makers | Quote depth that shrinks with volatility | Price impact / liquidity |
| ETF investors + authorized participants | Flow-performance response; creations and redemptions hit spot | Runs |
| Treasury companies | Issue equity when market value > holdings, buy coin; forced sellers when financing comes due and value < holdings | Fire sales (filed analogue) |
| Stablecoin holders + issuer | Redemptions force T-bill sales; peg confidence is a belief | Runs, interconnections |
| Miners | Sell production when hashprice falls; switch capacity to AI hosting | Interconnections |

**Market clearing:** start with a simple price-impact rule (Kyle-λ type) before any order book.

### 5.3 Calibration targets: stylized facts, not price paths

- Fat tails (kurtosis of daily returns)
- Volatility clustering (autocorrelation of |r|)
- Near-zero autocorrelation of raw returns
- The BTC–ETH co-movement and ETH's higher beta (ETH −32.6 % vs BTC −24.2 % since 10-06 is one observation, not a target)
- The frequency and size of documented liquidation episodes, to be sourced in the design note and never quoted from memory

**Method:** simulated method of moments. Moment uncertainty could later use the Bayesian bootstrap already mapped in Research (Andrews–Moon–Shapiro 2026), but only as a separate, later step under the piecewise rule.

### 5.4 Implementation

- Agents.jl in Julia, consistent with Nina's monetary agenda and the Dalila stack.
- GPU: profile first (DFD GPU strategy). Agent-step loops in Agents.jl are usually CPU-bound. A GPU path (CUDA.jl over agent-state arrays) is worth it only for large agent counts or big calibration sweeps, and the trade-off must be stated either way.
- Long calibration runs go inside Zellij. Don't kill runs mid-flight to tweak.

### 5.5 What the ABM must say about itself

Every result states how it can mislead:
- **Equifinality:** many parameter sets reproduce the same stylized facts.
- **Sensitivity** to the market-clearing rule.
- **Regime dependence:** a model calibrated on 2024–26 data may not hold after a structural change such as a new ETF wave or a stablecoin law.

### 5.6 Phases (each phase waits for Héctor's go)

| Phase | Deliverable | Code? |
|---|---|---|
| B0 | **Design note**: agent types chosen, rules, parameter space, calibration targets with sources, firewall restated | No |
| B1 | Minimal model: 3 agent types (conviction, momentum, leveraged), reproduces fat tails and clustering | Yes |
| B2 | Adds ETF and treasury-company agents; cascade experiments | Yes |
| B3 | Calibration by simulated moments; report of what does not fit | Yes |
| B4 | Stablecoin + miner agents; Duffie-Reis link to Nina's monetary ABM | Yes |

*Amendment 2026-11-16 (design note B0 v1.1, §3.4, after the Cath and Fina reviews): B1 splits into B1a (CPU engine, targets, parameter recovery) and B1b (batched CPU/GPU timing gate, may move to B3); the regime-shift test and a recalibration move to B2; B3 is SMM calibration plus the two-asset and perp/spot extension. The design note's phase table supersedes this one where they differ.*

### 5.7 Design for reuse: sovereign debt as the intended second instance

*(Added 2026-11-16 at Héctor's request.)* Crypto is the proving ground, not the destination. The B0 design note must build the engine around **generic agents**, each with a balance sheet, beliefs and constraints such as margins, mandates and rating floors, and around a **market-clearing rule that does not care what the asset is**. Then a sovereign bond market can be a second instance without a rewrite. Nothing crypto-specific (UTC closes, perpetual-futures funding, on-chain data) may live in the engine core; it belongs in the crypto instance's adapters.

**Why sovereign debt.** All five Brunnermeier-Reis mechanisms are live for a Latin American sovereign, where crypto and SPCX grey out two of them:
- Rollover runs (Calvo 1988; Cole & Kehoe 2000).
- The bank-sovereign doom loop (Brunnermeier, Garicano, Lane, Pagano, Reis, Santos, Thesmar, Van Nieuwerburgh & Vayanos 2016; Farhi & Tirole 2018).
- Holder interconnections.
- Original sin.
- Fiscal dominance.

**The intended agent map:**

| Crypto agent | Sovereign counterpart |
|---|---|
| Conviction holders | Captive long-horizon holders (pension funds; in Mexico, the AFOREs) |
| Leveraged traders | Foreign carry-trade money |
| ETF holders | Index and rating-constrained funds forced to sell on exclusion or downgrade |
| Stablecoin issuers | T-bill buyers |
| Treasury companies | Quasi-sovereigns borrowing on implicit backing (e.g. Pemex) |

**The link to the Grand Plan.** A sovereign instance is a candidate for the **OLG-ABM interface** that the SPCX brief (§0) and the Monetary Foundation (§10) leave undesigned. The DFD OLG core supplies the debt path that aging implies; the ABM asks whether holders' beliefs finance that path or flip to a run. That is the multiple-equilibrium zone a structural model, by construction, cannot see. The interface design stays Cath's.

**Discipline.** The sovereign instance is a later research programme, **not** a phase of this build. It waits until the crypto instance has passed B3. It needs its own spec, with holdings data by sector (e.g. Banxico holdings of government securities, sourced and dated), Cath on the fiscal side and Gina on external shocks. The firewall of §0 applies to it unchanged: no forecast of spreads or ratings, only conditional mechanism statements.

---

## 6. Deliverables back to the team

1. Part A: the board, its run log and a README checklist, after rulings Q1–Q5.
2. Part B: design note B0 only, until Héctor approves it.
3. Any cross-mechanism RED on the crypto board goes to Nina, as on SPCX.
4. Elle: the board is a second TD-frontier barometer. Crypto is the purest narrative asset, so the board shows when narrative capital leaves.

---

## 7. Questions for Héctor (proposed defaults in brackets)

**RULED 2026-11-16 (Héctor): all five proposed defaults accepted.** Part A was built the same day in `crypto_monitor/`, with every mechanism UNSET until the first manual pass. Numeric threshold bands are still open; see `crypto_monitor/README.md`. The ABM design note (B0) follows the board, per Q5.

- **Q1 — Scope.** BTC and ETH only? [Yes; no other tokens.]
- **Q2 — Currency-mismatch hook.** Activate the LatAm stablecoin-dollarization hook? [Keep it greyed out with the hook written; activate only by ruling.]
- **Q3 — Aggregator data.** Can perpetual-futures open interest, funding and liquidation data drive a Fire Sales leg? [Yes, as AGGREGATOR-grade with two independent sources; press still escalates nothing.]
- **Q4 — Wiring.** Run as a step inside the SPCX cycle, not its own timer? [Yes.]
- **Q5 — Order.** Build Part A first and write the ABM design note after? Or the design note first? [Part A first: the board defines which mechanisms the ABM must explain.]

---

*Draft by Claude Code for Nina · Aurora · GrandPlan · November 2026*
*Standalone exercise — not for integration into DSGE-OLG core pending OLG-ABM interface design. Build instruction: `_crossrefs/_build_instructions/2026-11-16_aurora_crypto_board_and_abm_b0.md` (filed 2026-11-16).*
