---
doc_id: 20260816_AURORA_BUILD_pharma-ratio-panel_v1.0
title: "Build instruction — back-office ratio panel, pharma firms"
project: Aurora
type: build instruction
version: 1.0
date: 2026-08-16
added_by: Nina
endorsed_by: Elle
status: active — back office, deliberately crude
supersedes: none
related:
  - 20260816_AURORA_HANDOFF_pharma-instance-port_v1.0
  - 20260816_AURORA_BUILD_pharma-feed-harness_v1.0
---

# Build instruction — pharma ratio panel

**Addressed to:** Claude Code instance, Dalila.

---

## 0. Scope arrest

This builds a **standard financial ratio panel** over a human-supplied firm roster.
It is deliberately unsophisticated and is meant to stay that way.

It does **not** build a DCF, a sum-of-the-parts pipeline valuation, a risk-adjusted
NPV model, a peer-regression fair value, or any forecast. If execution appears to
require any of these, **stop and report**.

The panel's output is a **set of deviations**, never a verdict. A tool that emits
"overvalued", "undervalued", "buy", or a target price has failed the brief and
should be reported as failed rather than shipped.

Repo fence: writes confined to `GrandPlan/Aurora/pharma/ratios/`.

---

## 1. What this builds

For each firm on the roster: a panel of standard ratios, each expressed twice —
against the roster's cross-sectional median, and against the firm's own trailing
five-year band. Both deviations are reported. Neither is aggregated into a score.

The analytical content is in the **disagreement between the two comparisons**, and
that reading is Héctor's, not the tool's. See §6.

---

## 2. Boundary

| Path | Owner | Tool access |
|---|---|---|
| `ratios/roster.md` | Human (Héctor) | **read-only** |
| `ratios/panel.csv` | Tool | read/write |
| `ratios/history/` | Tool | write (append-only) |
| `ratios/_reports/` | Tool | write (append-only) |
| `ratios/readings.md` | Human (Héctor) | **no tool access at all** |

`readings.md` is where any judgment about a deviation is written. The tool has no
read path to it either — it must not condition future output on prior readings.

---

## 3. The firm roster

`roster.md` lists tickers, human-supplied. **The tool never adds a firm.**

This preserves the board → monitor direction. The panel evaluates firms the board
has justified; it does not discover firms by screening. A screen would rank by
size or by cheapness, and either would rebuild a leaderboard through the back door.

Until the board exists, the roster is whatever Héctor puts in it. Note in the
report when the roster has fewer than eight firms, since the cross-sectional median
is close to meaningless below that.

---

## 4. Ratios

Standard set. No custom constructions.

**Valuation** — P/E trailing, P/E forward, EV/EBITDA, EV/Sales, EV/FCF,
price/book, dividend yield.

**Profitability** — gross margin, operating margin, net margin, ROE, ROIC.

**Leverage and liquidity** — net debt/EBITDA, interest coverage, current ratio.

**Intensity** — R&D/sales, capex/sales, FCF conversion (FCF/net income).

**Growth** — revenue CAGR 3y, EPS growth 3y.

Where a ratio is undefined (negative earnings, no dividend), record `NA`. **`NA` is
not zero** and must never be averaged as zero — the same rule that governs grids in
the board apparatus.

**Data source.** `yfinance` is acceptable and requires no key. Record the retrieval
timestamp and the source field name for every value. Where a figure is
restated between refreshes, keep both in `history/` — restatements are themselves
informative and deleting them destroys that.

---

## 5. Two distortions that make these ratios lie in pharma

The panel must print this warning in every report. It is not boilerplate; both
distortions bite hard in this industry and a reader who forgets them will misread
the output in a predictable direction.

**Trailing earnings overstate durable earnings near a patent cliff.** A firm two
years from a major loss of exclusivity has earnings that are scheduled to fall. Its
low P/E is not cheapness — it is the market pricing a known extinction. This is the
single most common way a pharma ratio screen misleads, and it will misfire in
exactly the cases the Aurora board cares most about.

**R&D is expensed, not capitalised.** Book value, margins, and ROIC are therefore
not comparable across firms with different R&D intensity. A research-heavy firm
looks less profitable and less asset-rich than a scale player running the same
economics. Do not compare P/B across firms whose R&D/sales differ by more than
roughly half.

**One adjustment, and only one.** Print a `years_to_major_LOE` column beside the
valuation ratios — a date, human-supplied in `roster.md`, not estimated by the
tool. It is a column, not a model. Its only job is to sit next to the P/E so the
cliff is visible at the moment the P/E is read.

---

## 6. The two comparisons

Each ratio is reported as:

- **Cross-sectional** — the firm against the roster median, as a percentage
  deviation.
- **Own-history** — the firm against its own trailing five-year median, as a
  z-score over that window. Report the window's standard deviation alongside; a
  z-score over a narrow band means something different from one over a wide band.

Both are printed. Neither is combined into a composite. Composites destroy exactly
the information the pairing exists to expose:

- Cheap cross-sectionally **and** cheap against its own history → something has
  changed at the firm.
- Cheap cross-sectionally **but** normal against its own history → the peer set
  re-rated, not this firm.
- Normal cross-sectionally **but** expensive against its own history → the whole
  sector moved together.

Those readings are Héctor's to make. The tool prints the pair and stops.

---

## 7. Output

`panel.csv` — the current panel, one row per firm, one column per ratio-comparison.

`_reports/YYYYMMDD_panel.md` — short, machine-authored, containing: the roster and
its size, the retrieval timestamp, the §5 warning in full, any `NA` fields and why,
any restatement detected since last refresh, and any deviation beyond ±2σ on the
own-history comparison flagged as **notable** — not as significant, and not with a
direction attached.

---

## 8. Refresh

Weekly, and on demand. Quarterly figures change slowly; a daily refresh would
manufacture the appearance of movement in a panel built from stale accounting data.

Append every refresh to `history/`. The panel's value grows with its vintages, and
that is the only sense in which this back-office tool compounds.

---

## 9. Out of scope — stop and report if reached

- any forecast, target, or fair-value estimate
- pipeline or asset-level valuation
- composite scores, rankings, or ordering firms by any metric
- adding firms to the roster
- reading `readings.md`
- connecting to the feed harness, the board, DFD, or the OLG core
- intraday or daily price data beyond what a weekly ratio refresh requires

---

## 10. Acceptance

Complete when: the panel runs against a roster of at least three test tickers;
`NA` fields are present and demonstrably excluded from median computation rather
than zero-filled; both comparisons print for every defined ratio; the §5 warning
appears in the report; `years_to_major_LOE` reads from `roster.md` and is blank
when unsupplied rather than estimated; and the tool is shown to have no write path
to `roster.md` and no read path to `readings.md`.

Report with the first panel attached.
