# PANEL.md — companion to panel.py

**Build instruction:** `20260816_AURORA_BUILD_pharma-ratio-panel_v1.0` (in `pharma/pharma_board/`).
**Deliberately crude, and meant to stay that way.** Deviations only — no
composite, no ranking, no forecast, no verdict.

## Running

Requires the `dalila` conda env (yfinance, PyYAML, pandas).

- `python panel.py run` — full roster refresh: fetch, compute, write
  `panel.csv`, append vintage to `history/`, write report to `_reports/`.
- `python panel.py run LLY,PFE,TEVA` — subset (testing).
- `python panel.py selftest-boundary` / `selftest-na` — acceptance checks.

Cadence: weekly, and on demand. Daily would manufacture movement out of stale
accounting data.

## What each ratio carries

For every ratio, five columns in `panel.csv`: the value, the cross-sectional
% deviation from the roster median (NA excluded from the median, never
zero-filled), the own-history z-score against the firm's earlier annual
vintages, that band's std, and its n. Both comparisons print; neither is
combined. The reading of their disagreement is Héctor's and is written in
`readings.md`, which this tool can neither read nor write.

## Construction choices (crude on purpose)

- **Current values**: valuation ratios from Yahoo's own fields
  (`info.trailingPE` etc.); fundamental ratios from the latest annual
  statements. Source field for every value is recorded in
  `history/<stamp>_raw.yaml` with the retrieval timestamp.
- **Own-history bands**: annual statement vintages (yfinance provides ~5
  years, so bands are typically n=3-4 after excluding the latest year).
  Valuation bands are reconstructed as year-end close × that year's shares
  against same-year statements. A z over 3-4 points is coarse; the report says
  so and prints std and n alongside.
- **ADR currency mismatch** (`NVO`, `SNY`: USD price vs DKK/EUR statements):
  computed valuation history is NA rather than wrong; Yahoo's own current
  fields are used where present.
- **NA is not zero.** Undefined ratios (negative earnings, no dividend,
  missing statement rows under a given GAAP) are NA, listed in the report with
  reasons, and excluded from every median.
- **`years_to_major_LOE`**: arithmetic on the human-supplied date in
  `roster.md` only; `?` (unverified) is carried through, `n/a` and blank stay
  as-is. The tool never estimates a date.
- **Restatements**: each refresh's raw statement values are compared to the
  previous vintage; differences > 0.5% are reported and both vintages are kept
  in `history/`.

## Boundary

`roster.md`: read-only (chmod a-w + guard). `readings.md`: no tool access in
any mode — the panel must not condition on prior readings. `history/` and
`_reports/`: append-only. All file access goes through the guard.

## Known limits (report, don't fix)

Mixed accounting regimes across the roster (US GAAP / IFRS / Ind AS / PRC
GAAP) make P/B, ROIC and margin cross-sections unreliable across regime
boundaries — roster.md says to lean on own-history for firms 14-20. Growth
CAGRs need year t and t-3, so their own-history bands are mostly empty.
Forward P/E has no history by construction.
