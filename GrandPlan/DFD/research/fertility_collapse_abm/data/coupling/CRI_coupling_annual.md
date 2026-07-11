---
type: corpus_entry
tier: data_source
project_scope: [DFD]
authors: [INEC Costa Rica]
year: 2026
title: "Costa Rica annual coupling series — share of women 20-39 in co-residential union (ENAHO 2010-2024)"
venue: "INEC ENAHO via ECLAC/INEC REDATAM online processing (RpWebStats web engine)"
doi: "https://sistemas.inec.cr:8443/bininec/RpWebEngine.exe/Portal?BASE=ENAHO2024"
date_added: 2026-06-18
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE1_5_coupling_identification.md"
---

# Costa Rica annual coupling series (ENAHO 2010-2024)

Stage 1.5 priority series: share of women aged 20-39 in a co-residential union
(married OR cohabiting), by single year and 5-year age band, with the married vs.
cohabiting split preserved. File: `CRI_coupling_annual.csv`.

## Provenance & method
- **Source:** INEC ENAHO person microdata, tabulated server-side via the INEC/ECLAC
  **REDATAM** web engine (`RpWebStats.exe/CrossTab`) — no microdata download, no login.
- **Tabulation:** weighted crosstab of estado conyugal (POBLACIO.A6; A26 in 2010-2012)
  × 5-year age band (POBLACIO.EDADQ), filtered to women (POBLACIO.A4 = 2), weighted by
  the expansion factor (VIVIENDA.FACTOR). `union_total = unión libre + casado`, as
  fractions of all women in the band.
- **Extractor:** `_extract_redatam_cri.py` (reproducible; introspects each year's
  conyugal variable code, position-aligns the result table). Run 2026-06-18.
- **Coverage:** national (urban + rural) — unlike Argentina's urban-only EPH.
- **Frequency:** annual, **observed** (no interpolation). ENAHO is annual since 2010;
  the EHPM predecessor (2000-2009, separate CCSS REDATAM portal, different variable
  names) is a candidate backfill not yet extracted.

## Forensic flags (per Stage 1.5)
- **Methodology break:** ENAHO replaced EHPM in 2010 (new frame/questionnaire); this
  series is ENAHO-only, so internally comparable 2010-2024.
- **Variable-code shift:** estado conyugal is `A26` in 2010-2012, `A6` from 2013 — the
  extractor resolves this per year from the dictionary (not a data break, just naming).
- **Marriage/cohabitation substitution:** total union decline is driven by collapsing
  marriage with flat/rising cohabitation; the split columns let downstream work avoid
  mistaking substitution for coupling decline. Total co-residential union still falls
  11-20 pts across bands 2010-2024.

## Columns
`year, age_band, union_total, married, cohabiting` (fractions 0-1) `, n_women_weighted,
observed_or_interpolated, source, coverage_flag`.
