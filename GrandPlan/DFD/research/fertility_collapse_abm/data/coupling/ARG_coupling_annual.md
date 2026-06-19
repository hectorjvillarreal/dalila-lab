---
type: corpus_entry
tier: data_source
project_scope: [DFD]
authors: [INDEC Argentina]
year: 2026
title: "Argentina annual coupling series — share of women 20-39 in co-residential union (EPH continua 2017-2025, urban)"
venue: "INDEC EPH continua person microdata via direct download (indec.gob.ar EPH microdata zips)"
doi: "https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos"
date_added: 2026-06-19
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE2_skeleton_abm_spec.md (ARG/CHL parallel track)"
---

# Argentina annual coupling series (EPH continua 2017-2025, urban)

Stage 2 parallel-track series (non-gating): share of women aged 20-39 in a co-residential
union (cohabiting OR married), by single year and 5-year age band, married vs. cohabiting
split preserved. File: `ARG_coupling_annual.csv` (9 years, 36 rows). Built to extend the
collapse-country coupling panel beyond Costa Rica + Colombia.

## Provenance & method
- **Source:** INDEC EPH continua person microdata, downloaded directly as per-quarter zips
  (`EPH_usu_{q}_Trim_{year}_txt.zip`), **no login, no REDATAM**. Per the Colombia lesson,
  the microdata-download door works where the REDATAM processing engine (which blocked the
  Stage 1.5 attempt) does not — `_extract_redatam_arg.py` is superseded by
  `_extract_eph_arg.py`.
- **Tabulation:** weighted share of women (CH04==2) aged 20-39 with CH07 (situación
  conyugal) in {1}=cohabiting (unido/a) / {2}=married (casado/a); `union_total = cohabiting
  + married`, as fractions of all women in the band. EPH is quarterly; each annual value
  pools all available quarters (summing PONDERA-weighted counts).
- **Extractor:** `_extract_eph_arg.py` (reproducible). Run 2026-06-19. Variable map
  (CH07/CH04/CH06/PONDERA) reused from the REDATAM extractor's reconnaissance.
- **Window:** 2017-2024 observed (2017 pools 3 quarters — T1 not published; rest pool 4) +
  **2025 provisional**. The download door maps reliably to **2017 T2 → 2025**; 2016 and
  pre-2016 are on a different path.

## Forensic flags (load-bearing)

### ⚠ Flag 1 — coverage is URBAN ONLY
EPH covers **31 urban agglomerates**, not national. Argentina is ~92% urban, so the
national distortion is smaller than it would be elsewhere, but it is real and **must be
carried in any cross-country comparison**: CRI and COL are national (urban+rural), ARG is
urban. A census cross-check (Censo 2010/2022 union status) is the way to bound the
urban-vs-national gap and is flagged as a refinement.

### ⚠ Flag 2 — Argentina is HIGH-cohabitation, NOT the "marriage-dominant regime" the spec assumed
The Stage 2 skeleton spec motivated the ARG acquisition as a *different, marriage-dominant
Southern-Cone nuptiality regime* that would **extend the cohabitation-share range** and
discipline the structural parameter `w`. **The data contradict this premise.**
Cohabitation share of unions (women 20-39):

| | cohab-share-of-unions | total union | married |
|---|---|---|---|
| **ARG 2017** | **68%** | 49.6% | 16.0% |
| **ARG 2024** | **75%** | 47.2% | 11.7% |
| COL 2017 | 74% | 59.4% | 15.6% |
| CRI 2017 | **48%** | 48.5% | 25.1% |

Urban Argentina is **high-cohabitation, sitting with Colombia** (Argentina has among the
world's highest consensual-union rates, well-documented). **Costa Rica is the relatively
marriage-leaning case of the three.** Consequence for Stage 2: ARG does **not** extend the
cohabitation range toward the marriage-dominant end — it is a *third high-cohabitation
collapse case*. It strengthens the *generality* of the high-cohabitation / map-side-at-total
pattern, but it does **not** provide the regime contrast needed to identify `w` at the
low-cohabitation end. The contrast we actually hold is CRI (48%) vs COL/ARG (74-75%); a
genuinely marriage-dominant LAC case (Chile? Mexico is more marriage-oriented) would be
needed to widen it. **This is for Anne/Nina to weigh — the ARG external-validity rationale
in the skeleton spec should be revised.**

### ⚠ Flag 3 — 2020 is a pandemic-collection year
2020 EPH ran under strict lockdown with phone-based collection; treat the 2020 point with
the same caution as the COL/CRI 2020 points. (Its T4 base file is named `usu_personas_*`
rather than `usu_individual_*` — an INDEC naming variant the extractor handles.)

### Note — INDEC intervention era (2007-2015) deliberately excluded
The intervened-INDEC period is not in this series. Estado civil is a roster fact less
exposed to the intervention than prices/poverty, but the sample frame/weights are suspect,
and the download path differs; excluded rather than carry the data-quality fight on a
non-gating track. The series is the clean post-normalization continua (2017+).

## The series (20-39 aggregate)
Total union ~49.6% (2017) → 47.2% (2024) → 46.0% (2025 prov.): a **modest, Colombia-like
near-plateau**, declining ~2.4 pts over the observed window. Marriage erodes steadily
(16.0% → 11.7%), cohabitation substituting. The young band declines most (20-24: 25.1% →
19.6%). Pairs with the INDEC-pinned implied annual TFR (`national/ARG_tfr_implied.csv`,
2.38→1.15) — but note that TFR is a *reconstruction* (anchored to 2015, stable-age-pattern),
so an ARG lead test inherits the Mexico-style caveat (modeled, not pure observed
registration) and is weaker than the COL/CRI observed-TFR tests.

## Columns
`year, age_band, union_total, married, cohabiting` (fractions 0-1) `, n_women_weighted,
observed_or_interpolated, source, coverage_flag, note`.
