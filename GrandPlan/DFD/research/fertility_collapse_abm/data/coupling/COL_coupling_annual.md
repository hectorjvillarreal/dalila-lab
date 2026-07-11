---
type: corpus_entry
tier: data_source
project_scope: [DFD]
authors: [DANE Colombia]
year: 2026
title: "Colombia annual coupling series — share of women 20-39 in co-residential union (GEIH 2007-2024)"
venue: "DANE GEIH person microdata via Catálogo Central de Datos (microdatos.dane.gov.co, NADA instance)"
doi: "https://microdatos.dane.gov.co/index.php/catalog/GEIH"
date_added: 2026-06-18
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE1_5_addendumA_colombia_geih.md"
---

# Colombia annual coupling series (GEIH 2007-2024)

Stage 1.5 Addendum A series: share of women aged 20-39 in a co-residential union
(married OR cohabiting), by single year and 5-year age band, married vs. cohabiting
split preserved. File: `COL_coupling_annual.csv` (18 years, 72 rows).

Colombia is the gate's decisive case: the ONLY collapse country with an OBSERVED
annual national TFR (DANE EEVV, `national/COL_tfr_national.csv`) to pair against the
coupling path, so the Q1 lead test is properly evaluable here (Check B of the addendum).

## Provenance & method
- **Source:** DANE GEIH person microdata downloaded directly from the DANE Catálogo
  Central de Datos (NADA instance), **no login** — the `auth/login` wall that blocked
  the original Stage 1.5 attempt was the wrong door. Per-year national-annual catalog
  ids (resolved live 2026-06 from the catalog search API; supplementary samples —
  Ciudades Intermedias, Nuevos Departamentos, San Andrés — excluded):
  2007→317, 2008→206, 2009→207, 2010→205, 2011→182, 2012→77, 2013→68, 2014→328,
  2015→356, 2016→427, 2017→458, 2018→547, 2019→599, 2020→780, 2021→701, 2022→771,
  2023→782, 2024→819.
- **Tabulation:** weighted share of women (sex==2) aged 20-39 with P6070 (estado civil)
  in {1,2}=cohabiting (unión libre), {3}=married; `union_total = cohabiting + married`,
  as fractions of all women in the band. GEIH is monthly continuous; each annual value
  pools **all 12 months** with the survey expansion factor.
- **Extractor:** `_extract_geih_col_v2.py` (reproducible; auto-detects schema per
  vintage). Run 2026-06-18. Identification analysis: `_col_identification.py`.
- **Coverage:** national (urban + rural). Pre-redesign vintages split the person
  module into Cabecera (urban) + Resto (rural) + Área (metro); the extractor pools
  **Cabecera + Resto** (the non-overlapping national partition) and DROPS Área (a
  redundant subset already inside Cabecera) to avoid double-counting metros.

## Forensic flags (load-bearing for Colombia)
- **CHECK A — 2021-2022 "Marco 2018" redesign is NOT a coupling recode.** From DANE's
  own value labels, P6070 (estado civil) is **identically coded on both sides** of the
  redesign (1,2 = vive en pareja <2y / ≥2y → cohabiting; 3 = casado; 4 sep, 5 viudo,
  6 soltero). What changed across the break is only the **sex** variable name
  (P6020 → P3271) and the **weight** name (Fex_c_2011 → FEX_C18), both auto-detected.
  The coupling definition does not move, so the post-2020 downturn is real, not an
  artifact. Series carries `coverage_flag = national-splice` for 2021-2022.
- **2020 pandemic sample.** 2020 ships as a single national file (FEX_C weight) with a
  smaller weighted-n (~17M vs ~26M); confirmed national (urban + rural present via
  CLASE 1/2). The *share* is a ratio and is unaffected by the weight base; flagged in
  the `note` column.
- **2007 outlier.** Earliest year (union 47.5% vs the 2008-2020 plateau ~59-60%);
  likely a frame/questionnaire difference. Treat the plateau as 2008-2020.
- **Marriage/cohabitation substitution.** Total union sits on a flat ~59-60% plateau
  2008-2020 while **marriage halves** (20.7%→11.9%); cohabitation substitutes. The
  split columns let downstream work test the marriage-weighted coupling variable
  (Anne's caution) without mistaking substitution for coupling decline.

## Extraction caveats fixed during the run (audit trail)
The v1 extractor was rebuilt as v2 after a forensic pass on real files exposed:
(1) download links live in an `onclick="mostrarModal(...)"` handler, not anchor text;
(2) sex/weight variables renamed across the redesign (auto-detected);
(3) geographic-domain double-count (Cabecera+Resto pooled, Área dropped);
(4) the frame name "Marco 2018" collided with the "mar"/marzo month token, collapsing
2022 to 3 months (fixed by stripping the frame token + full-name-first matching);
(5) 2023/2024 package some months as NESTED zips (CSV.zip/SAV.zip) rather than folders
(fixed by recursing into nested format zips). All 18 years pool a full 12 months
(except 2020's pandemic sample), 0 read failures after the fix.

## Columns
`year, age_band, union_total, married, cohabiting` (fractions 0-1) `, n_women_weighted,
observed_or_interpolated, source, coverage_flag, note`.
