# NVDA watch — Nvidia's financial bets

Aurora · companion to the [SPCX monitor](../spcx_monitor/README.md). Opened
2026-10-03 at Héctor's request ("keep some monitor of NVIDIA").

## Why

Nvidia has moved from selling chips to **financing its own demand**: equity in
its customers, credit guarantees on their data-center leases, capacity
backstops, and stakes in the firms that finance GPU buildouts. In
Brunnermeier-Reis terms it has made itself a lender of last resort to AI
demand, so its losses would arrive late and together (fire-sales pattern), and
its earnings move with its customers' valuations (interconnections).

It is also a three-way node in the SPCX web: **GPU supplier** to Colossus
(~325,000 NVIDIA GPUs in the Anthropic contract, SPCX 424B4), **SPCX holder**
(122,764,805 sh at 06-30, 13F acc. 0001045810-26-000065; new in Q2, likely the
ex-xAI stake; that last step is our inference), and **investor in Anthropic**
(up to $10B, press), SpaceX's main compute customer.

## What it is (and is not)

An **alarm over EDGAR filings**, not a classifier. Same discipline as the SPCX
monitor: no price target, no directional field, no fabricated numbers. A
variable the extractor cannot find is printed `unset / manual`. Readings and
any escalation belong to the analyst, recorded in the SPCX monitor's
Interconnections observables.

## Files

| File | Role |
| --- | --- |
| `nvda_watch.py` | The tool (stdlib only). `run` polls; `baseline` seeds; `render` rebuilds the tracker. |
| `ledger.json` | Seen accessions, latest 13F holdings, latest 10-Q/10-K variables, Section 16 counts. |
| `tracker.md` | Generated view of the ledger. Do not edit by hand. |
| `digests/YYYY-MM-DD.md` | Written only when Nvidia files something new. This is the alarm. |

## What it watches

- **13F-HR**: full holdings diff vs the prior quarter; desktop notification if
  the SPCX line changes (CUSIP 84615Q103).
- **10-Q / 10-K**: balance-sheet and footnote variables (non-marketable and
  marketable equity, receivables, inventories, YTD equity gains, AI-cloud lease
  guarantees, warrants, equity-method stakes in infrastructure financiers), the
  **future-commitments table** totals (supply, cloud services, leases, equity
  investments, capex, total), capped guarantees, and customer concentration.
- **8-K, 13D/13G, S-3/S-4, 424B, proxy**: listed in the digest with a link;
  8-K and 13D/G trigger a desktop notification.
- **Form 3/4/5/144**: counted only (executive 10b5-1 sales would flood it).

## Baseline (10-Q for the quarter ended 2026-07-26, acc. 0001045810-26-000075)

Non-marketable equity $47.9B (was $3.8B a year earlier); marketable equity
$42.8B; receivables $63.1B (from $38.5B in January); H1 equity gains $23.7B;
AI-cloud lease guarantees $3.5B; OpenAI/SB Energy Ohio guarantees capped at
$105B (August 2026, 20-year leases, exclusive NVIDIA hosting); future
commitments $366B, of which supply $279B (from $119B a quarter earlier) and
equity investments $25B; one direct customer = 16% of Q2 revenue.

## Calendar

- Q3 13F-HR (holdings at 2026-09-30): due by **2026-11-14**. Shows whether
  Nvidia sold SPCX after the lockup tranches.
- Q3 FY2027 10-Q: expected late November after earnings.

## Open items for the analyst

Who the large direct customers are; what triggers payment under the
guarantees; how much of the CoreWeave capacity backstop remains (press: $6.3B
through 2032); whether Nvidia's SPCX shares are under lockup.

## Automation

Runs as step 3b of `~/.local/bin/spcx_render.sh` (the 18:00 SPCX cycle), not on
its own timer: a second timer would race the SPCX job for the git index on
boot catch-up. The step is non-fatal. Its output is committed with the SPCX
cycle. Log: `~/.spcx_render.log`.
