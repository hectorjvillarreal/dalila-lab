# Brief for Claude Code (Fable) — SPCX Brunnermeier-Reis Regime Monitor

*Document type: Build specification / Knowledge File · Aurora Project*
*Author: Nina (macro-financial strategy)*
*Date: June 2026*
*Status: Active — build brief, standalone exercise (NOT integrated into DSGE-OLG core)*
*Addressed to: Claude Code instance running Fable on Dalila*

---

## 0. Scope discipline — read first

This is a **standalone analytical exercise**. It is **not** to be connected to the DSGE-OLG fiscal core, the DFD simulation engine, or any OLG calibration. SPCX price dynamics are a high-frequency, confidence-equilibrium object; the OLG core is a structural, steady-state, long-horizon object. They converge only later, through a deliberately designed OLG-ABM interface that does not yet exist. Keep this artifact self-contained.

The objective is **not** to predict the SPCX share price. It is to build a disciplined **regime-identification dashboard** that forces structured reasoning about which Brunnermeier-Reis amplification mechanisms are active, dormant, or inert at any given time, and what observable would escalate each one. The discipline — regime identification *before* any directional judgment — is the entire point. An artifact that outputs a price target has failed the brief.

---

## 1. Analytical foundation

The diagnostic is built on the five amplification mechanisms from Brunnermeier and Reis, *A Crash Course on Crises* (Princeton University Press, 2023). The framing principle: crises are the expression of vulnerabilities that accumulate and then tip — not tail events appended to smooth equilibria. The taxonomy is used to identify *which* mechanism is active before drawing conclusions.

SPCX is an unusually clean object for this taxonomy because it is a **confidence/narrative asset, not a cash-flow asset**. There is no discounted-cash-flow anchor acting as a restoring force, which makes belief-driven amplification the dominant price dynamic. (Context: IPO June 12, 2026; priced at $135, settled first day at $160.95, +19.22%; ~$2T+ valuation; largest IPO in history; folds in xAI; operates as a neocloud renting compute to Anthropic; dense web of stock-collateralized obligations.)

---

## 2. The five-element taxonomy — exact specification

The artifact must encode all five mechanisms. For each, the specification below gives: the definition, whether it is structurally live for SPCX, the observable inputs to monitor, and the escalation threshold logic. Two of the five are **inert** for this asset — the artifact must display them as inert and greyed out, not omit them. Knowing which mechanisms do *not* apply is half the discipline.

### Mechanism 1 — RUNS (LIVE)

**Definition.** A coordination failure in which holders rush to exit because they expect others to exit, making the exit self-fulfilling. Applies to any claim that can be redeemed or sold faster than the underlying can absorb.

**Status for SPCX: LIVE.** The relevant "run" is a coordinated exit by belief-driven holders. The vulnerability is the composition of the holder base — how much is fast, sentiment-driven capital versus locked-up or conviction-held.

**Observable inputs to monitor:**
- Share of float held by lockup-restricted insiders (Class B, founder, employee) vs. freely tradable Class A float
- Lockup expiry schedule and dates (step-changes in free float are escalation events)
- Daily trading volume relative to free float (turnover ratio)
- ETF / passive inclusion status (index inclusion changes the holder base abruptly)
- Concentration of holdings (retail vs. institutional vs. crossover/belief capital)

**Escalation threshold logic:**
- GREEN: high lockup share, low turnover, stable holder base
- AMBER: approaching a lockup expiry; turnover rising; sentiment indicators softening
- RED: lockup expiry coincident with negative sentiment shift; turnover spike on falling price

### Mechanism 2 — FIRE SALES / BALANCE-SHEET CHANNEL (LIVE)

**Definition.** Asset price declines force deleveraging by holders who financed positions with debt or who have obligations collateralized by the asset; forced selling depresses prices further, in a reflexive loop.

**Status for SPCX: LIVE.** SPCX carries an unusually concrete version of this through stock-denominated obligations. If SPCX falls, obligations priced in SPCX stock reprice simultaneously and can force selling or trigger contingent payments.

**Observable inputs to monitor:**
- Stock-collateralized obligations in the corporate web: the Cursor acquisition structure (large Class A stock component; termination/deferred-service fees payable in stock or cash), Valor equipment leases, any vendor or acquisition financing denominated in SPCX shares
- Margin lending against SPCX (broker margin availability, any disclosed pledged-share arrangements by insiders)
- Whether key counterparties hold SPCX as a balance-sheet asset
- Convertible or stock-settled instruments tied to SPCX value

**Escalation threshold logic:**
- GREEN: obligations well-covered at current price; ample headroom above any stock-price triggers
- AMBER: price approaching levels where stock-settled obligations or margin become strained
- RED: price below trigger levels forcing contingent payments, margin calls, or pledged-share liquidation

### Mechanism 3 — INTERCONNECTIONS (LIVE)

**Definition.** The network of cross-exposures through which distress at one node propagates to others. The vulnerability is not any single balance sheet but the topology of dependencies.

**Status for SPCX: LIVE.** SPCX sits at the center of a dense web: xAI (absorbed subsidiary), Anthropic (compute customer at Colossus/Memphis), Valor (board-linked equipment lessor with ~$20B exposure), Cursor (pending acquisition), and the broader "TD-frontier IPO pipeline" (OpenAI, Anthropic reportedly watching SPCX as the door-opener).

**Observable inputs to monitor:**
- Map of counterparties holding or depending on SPCX value
- The compute-revenue dependency chain (SPCX neocloud revenue depends on AI-sector demand, which depends on the same sentiment cycle pricing SPCX itself — a reflexive loop)
- Status of the follow-on IPO pipeline (a failed OpenAI/Anthropic listing would reprice the whole TD-frontier-equity narrative, feeding back to SPCX)
- Vendor/customer concentration in the AI-compute business

**Escalation threshold logic:**
- GREEN: counterparty web stable; no node under stress
- AMBER: stress at one node (e.g., AI-sector capex slowdown, a wobble in the IPO pipeline)
- RED: simultaneous stress across multiple connected nodes; reflexive compute-revenue/sentiment loop turning negative

### Mechanism 4 — CURRENCY MISMATCH (INERT)

**Definition.** Vulnerability from holding liabilities in one currency and assets/revenue in another; original-sin dynamics, dollar-denominated debt against local-currency revenue.

**Status for SPCX: INERT.** SPCX is a USD-denominated, USD-listed, USD-revenue entity. No first-order currency mismatch at the asset level. **Display as greyed-out / inert.** Retain it in the dashboard so the reasoning record is explicit that it was considered and ruled out, not overlooked. (Note for completeness: any future international-revenue or FX-denominated obligation could reactivate this; the monitor should leave a dormant hook but flag nothing absent that.)

### Mechanism 5 — INFLATION-DEFLATION SPIRAL (INERT AT ASSET LEVEL; MACRO HOOK)

**Definition.** The fiscal-monetary channel — monetization, fiscal theory of the price level, the debt-deflation interaction.

**Status for SPCX: INERT at the asset level.** A single equity does not generate an inflation-deflation spiral. **Display as greyed-out / inert at the asset level.** However, retain a **macro-liquidity input hook**: the broader backdrop that conditions belief-driven assets — real rates, capital rotation, liquidity appetite — belongs here as context, not as an active SPCX mechanism. This is the bridge to the wider monetary regime Nina tracks (the Duffie-Reis balance-sheet transition, real-rate level), supplied as a backdrop gauge rather than an asset-level trigger.

**Macro-backdrop observables (context panel, not an escalation trigger):**
- 10-year TIPS (real) yield level — the opportunity cost anchor for non-cash-flow assets
- VIX level and trend
- Capital-rotation signal: relative performance of narrative assets (bitcoin) vs. cash-flow assets — the canary we already use
- Broad risk-on / risk-off indicator

---

## 3. Daily monitoring instructions

The artifact is intended for **daily** refresh. Each daily cycle should:

1. **Ingest** the day's observable inputs for each LIVE mechanism (Sections 2.1–2.3) plus the macro-backdrop panel (2.5). Inert mechanisms (2.4, 2.5-asset-level) require no daily input but remain visible as inert.
2. **Classify** each live mechanism GREEN / AMBER / RED against its threshold logic.
3. **Record** the classification with date and the specific observable that drove any change — so the dashboard accumulates a time series of regime states, not just a snapshot. The provenance chain matters (PROTO-RAG-001 discipline): every state change should be timestamped and attributed to its triggering observable.
4. **Surface** a single top-line regime read: which mechanisms are live and at what level, and — critically — what observable would escalate each one next. The output is "here is the current regime and here is what would flip it," never "here is where the price is going."
5. **Flag** any cross-mechanism coincidence. The dangerous configurations are not single-mechanism RED but *simultaneous* escalation across runs + fire sales + interconnections — that is the self-reinforcing crash configuration the taxonomy exists to catch.

Daily data can be sourced from public market data, the macro series (FRED for TIPS yields, standard sources for VIX), and event-driven updates to the obligation web and lockup schedule (from filings). Where a clean automated feed is unavailable, the artifact should accept manual entry for that input rather than fabricate a value — an empty/manual field is acceptable; an invented number is not.

---

## 4. Artifact design — what to build

Yes, an artifact is well-suited to this. Build a **regime-identification dashboard**, not a pricing model. Suggested structure:

**Layout.** A five-panel dashboard, one panel per mechanism, in taxonomy order (Runs, Fire Sales, Interconnections, Currency Mismatch, Inflation-Deflation). Live panels are interactive and colour-coded by state; inert panels are visibly greyed with a one-line "considered, ruled out" rationale. A sixth context panel holds the macro backdrop. A top strip shows the consolidated regime read and the cross-mechanism coincidence flag.

**Per-panel content.** Mechanism name; current state (GREEN/AMBER/RED or INERT); the observable inputs with their current values; the escalation threshold the panel is measured against; and the "next escalation trigger" — the specific observable move that would change the state.

**State persistence.** The dashboard should retain a daily history of regime states so the user can see the trajectory of the regime over time, not just today's reading. (If built as a browser artifact, use in-session state or the artifact persistent-storage pattern; if built in Claude Code as a local tool on Dalila, persist to a dated local file consistent with corpus conventions.)

**Explicit non-goals, encoded in the UI.** No price target field. No buy/sell/hold output. No expected-return calculation. The artifact should make it structurally impossible to read a trading recommendation off it — its only outputs are regime states and escalation triggers.

**Provenance.** Each state change carries a timestamp and the triggering observable, so the artifact's history doubles as a corpus-admissible reasoning record under PROTO-RAG-001.

---

## 5. Deliverables back to the team

1. The artifact itself (dashboard).
2. A short run-log convention so daily readings accumulate into a reviewable regime time series.
3. On any cross-mechanism RED coincidence, a flag routed to Nina for interpretation — this is the configuration where the Brunnermeier-Reis machinery says a self-reinforcing move is possible, and it warrants a human-judgment layer rather than an automated conclusion.

---

## 6. Why this belongs in Aurora

SPCX is the first liquid, public, pure-play **TD-convergence asset** — it bundles AI, compute infrastructure, and frontier engineering into one ticker, and it is reportedly the door-opener for an OpenAI/Anthropic listing pipeline. Its price dynamics are, in effect, the public market's real-time referendum on the TD compounding thesis that Aurora exists to track. The monitor is therefore not a trading tool but a **TD-frontier market barometer** — Aurora's instrument for reading how public markets are pricing the convergence Elle's framework is built around, with Nina's Brunnermeier-Reis discipline ensuring the reading is regime-identification rather than narrative.

---

*Specification by Nina · Aurora · GrandPlan · June 2026*
*Standalone exercise — not for integration into DSGE-OLG core pending OLG-ABM interface design*
