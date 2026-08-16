# HARNESS.md — companion to harness.py

**Build instruction:** `20260816_AURORA_BUILD_pharma-feed-harness_v1.0` (in `pharma_board/`).
**Layer 1 only.** No board, no archetypes, no valuation, no price data.

## Division of labour

Retrieval needs live web search, which only the executing Claude Code instance
has; everything deterministic lives in `harness.py`. A cycle is therefore:

1. `python harness.py plan` — prints this cycle's query selection
   (rotation over main + provisional, plus the 25% exploration reserve).
2. The instance runs each query as a web search and writes candidates to a
   scratch file (list of `{query_id, headline, url, source_domain,
   date_published, entities, why}`). Headline verbatim as published; `why` is
   one clause, a guess, and carries no calibration weight. Prefer items
   published in the last ~14 days. The instance does **not** apply the promote
   test — intake is loose by design.
3. `python harness.py cycle <candidates.yaml>` — dedup (URL + near-identical
   headline), append to `items.yaml` with `promote: null`, run calibration,
   write the cycle report to `_reports/`, advance rotation.

Requires the `dalila` conda env (PyYAML). Default cadence 48h, adaptive within
24–168h once calibration is active.

## Ownership

`seeds.md` and `rules.md` are Héctor's: chmod `a-w` on disk, and refused by
`guarded_open()` — the module's only write path. `promote` is the only judgment
field; ingest forces it to `null` and no code path ever sets it. Héctor edits
`items.yaml` directly to set `promote: true | false` (restore write permission
is not needed — items.yaml is tool-owned and writable).

`rules.md` does not exist yet; each report notes this until it does.

## Calibration (active from cycle 4 AND ≥10 promote flags)

- **Retire** (main + provisional): ≥15 *flagged* items in a query's rolling
  20-item window with zero promotes → moved to `_graveyard/queries_retired.yaml`
  with full record. Interpretation choice: unflagged items do not count toward
  the 15, so Héctor's reading lag can't retire a query. Exploration is exempt.
- **Propose**: term (unigram/bigram over promoted headlines + entities)
  recurring across ≥3 promoted items and absent from every active query → new
  provisional query, cap 3/cycle. Provisional items are lane-tagged and the
  query graduates to main only after one of its items is promoted.
- **Sources**: Laplace-smoothed promote rate relative to the overall rate,
  clipped to [0.2, 1.0]. Down-weight only; blocking is Héctor's.
- **Entities**: recounted from promoted items only; reported, never nominated.
- **Cadence**: >6 promotes/cycle → −12h; three consecutive cycles below 1 →
  +24h; bounds 24h/168h.

## Never calibrated

Promote criteria, any classification structure, the `why` field's influence
(none, permanently), source blocking, board entry.

## Verification

- `python harness.py selftest-boundary` — demonstrates refusal of writes to
  seeds.md / rules.md / outside the fence, and append-only enforcement.
- `simulate_calibration.py` (scratch, run under `PHARMA_FEED_DIR` override) —
  synthetic promote flags shown to move query, source, entity and cadence
  state as specified, with provisional queries withheld until graduated.
