---
type: corpus_entry
tier: data_source
project_scope: [DFD]
authors: [MDS Chile (CASEN)]
year: 2026
title: "Chile coupling series — share of women 20-39 in co-residential union (CASEN 2006-2022, national, periodic)"
venue: "Chile MDS Observatorio Social CASEN microdata via direct download"
doi: "https://observatorio.ministeriodesarrollosocial.gob.cl/encuesta-casen"
date_added: 2026-06-19
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE2_skeleton_abm_spec.md (ARG/CHL parallel track)"
---

# Chile coupling series (CASEN 2006-2022, national, periodic)

Stage 2 parallel-track series (non-gating): share of women aged 20-39 in a co-residential
union (cohabiting OR married), by 5-year age band, married vs. cohabiting split preserved.
File: `CHL_coupling_annual.csv` (8 waves, 32 rows). The `year` column is the CASEN **wave**
year — this is a **periodic** series (a cross-section every 2-3 years), not annual.

## Provenance & method
- **Source:** Chile MDS Observatorio Social CASEN national microdata, downloaded directly
  as STATA `.dta.zip` files (`storage/docs/casen/{year}/...`), **no login**. Per the
  Colombia/Argentina lesson, the microdata-download door works where the ECLAC REDATAM
  host (which carried only old CASEN waves and blocked the Stage 1.5 attempt) did not.
  `_extract_casen_chl.py`; the REDATAM route is abandoned.
- **Coverage:** **NATIONAL (urban + rural)** — `expr` (factor de expansión) sums to ~19.9M
  (Chile's population) in 2022. This is better coverage than Argentina's urban-only EPH and
  matches CRI/COL.
- **Waves:** 2006, 2009, 2011, 2013, 2015, 2017, 2020, 2022 (8 cross-sections, 16-year span).
- **Tabulation:** weighted share of women (`sexo`==mujer) aged 20-39 by 5-year band, `expr`
  weight. `married = ecivil "Casado(a)"`, `cohabiting = ecivil "Conviviente / pareja"`
  (with or without acuerdo de unión civil). **`ecivil` is classified BY LABEL, not numeric
  code** — codes drift across waves (the AUC "conviviente civil" category exists only from
  2015), so label matching ("casado" / "conviviente"|"pareja") is wave-stable.

## Headline finding — Chile spans the cohabitation-share range WITHIN one country over time

| wave | union% | married% | cohabiting% | cohab-share-of-unions |
|---|---|---|---|---|
| 2006 | 55.5 | **36.1** | 19.4 | **35%** |
| 2009 | 52.3 | 31.4 | 20.9 | 40% |
| 2011 | 49.8 | 26.6 | 23.2 | 47% |
| 2013 | 48.4 | 23.7 | 24.7 | 51% |
| 2015 | 49.5 | 22.4 | 27.1 | 55% |
| 2017 | 48.8 | 19.8 | 29.0 | 59% |
| 2020 | 46.3 | 17.1 | 29.2 | 63% |
| 2022 | 51.1 | **16.7** | 34.4 | **67%** |

(women 20-39, n-weighted.)

Chile **flips from marriage-dominant to cohabitation-dominant within the observation window**:
marriage **halves** (36.1% → 16.7%), cohabitation **nearly doubles** (19.4% → 34.4%), while
**total union is comparatively stable** (~55% → 51%, dipping to 46% in the 2020 pandemic
wave then rebounding). Cohab-share-of-unions rises **35% → 67%**.

### Why this matters for the spec's `w`-identification (FLAG for Anne/Nina)
The skeleton spec wanted a *different cohabitation regime* to discipline the structural
parameter `w`. **Argentina did not provide it** (it is high-cohabitation throughout 2017-2024,
sitting with Colombia — see `ARG_coupling_annual.md` Flag 2). **Chile does** — but
*temporally rather than cross-nationally*. **Chile 2006 (cohab-share 35%) is the most
marriage-dominant point in the entire CRI/MEX/COL/ARG/CHL panel** (more marriage-leaning
than CRI's ~48%); Chile 2022 (67%) sits with ARG/COL. So Chile alone traverses the range
that identifies `w`, if cohabitation share is treated as a time-varying initial condition.
**This rescues the `w`-identification goal that ARG could not deliver**, and is a stronger
external-validity contribution than the spec anticipated.

### Relation to the Addendum B locus result
Total union is comparatively flat while marriage halves and the Chile TFR collapses
(implied 1.81→1.02, `national/CHL_tfr_implied.csv`): **map-side on total union, coupling-side
on the marriage margin** — the same `w`-determined locus pattern as Addendum B (COL/CRI),
now with an explicit within-country cohabitation-share trajectory underneath it.

## Forensic flags / caveats
- **Periodic, not annual.** 8 waves over 16 years; lead-lag tests on this are coarse (far
  fewer points than the annual CRI/COL/ARG series). Treat as periodic anchors.
- **2020 is a pandemic wave** ("Casen en Pandemia", reduced/adapted fieldwork) — the 2020
  union dip (46%) carries the same caution as the COL/CRI/ARG 2020 points. Its `.dta` is
  latin-1-encoded and broke pandas' utf-8 assumption; read via a pyreadstat LATIN1 fallback
  in the extractor.
- **AUC grouped with cohabiting.** "Conviviente civil con acuerdo de unión civil" (Chile's
  civil union, since 2015) is a legal partnership distinct from marriage; grouped with
  cohabiting (small share). The married/cohabiting split is about formal marriage vs
  consensual/registered partnership.
- **Implied TFR weakens any lead test.** `CHL_tfr_implied.csv` is a reconstruction (anchored
  to 2022, stable-age-pattern), so an ARG/CHL-style lead test inherits the Mexico caveat
  (modeled, not pure observed registration) — and the periodic coupling series makes it
  coarser still.
- **ecivil label-classified** (wave-stable) rather than code-based.

## Columns
`year, age_band, union_total, married, cohabiting` (fractions 0-1) `, n_women_weighted,
observed_or_interpolated, source, coverage_flag, note`.
