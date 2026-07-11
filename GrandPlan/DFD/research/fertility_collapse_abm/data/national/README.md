---
type: corpus_entry
tier: data_source
project_scope: [DFD]
authors: [DANE; INE Chile; DEIS-MINSAL Argentina; INDEC; INEC Costa Rica; INEGI; CONAPO]
year: 2026
title: "National-source fertility series (collapse tail) — Colombia, Chile, Argentina, Costa Rica, Mexico"
venue: "National statistical offices (vital registries / population councils)"
date_added: 2026-06-17
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE1_data_acquisition_fertility_collapse.md"
---

# National-source CSVs (collapse tail)

Tidy long format: `year, value, source, methodology_flag, provisional_flag`. These carry the
2020–2024 collapse tail that World Bank/WPP smooths away. Full URLs + access notes in
`../STAGE1_provenance.md`; forensic assessment in `../STAGE1_forensic_memo.md`.

| File | Series | Span | Notes |
|---|---|---|---|
| COL_tfr_national.csv | DANE TGF | 2015–2024 | 1.7→1.1 (NOT 2.0→1.06); chart-label, 1dp |
| COL_births_national.csv | DANE births | 2016–2025 | 2025 provisional |
| COL_gfr_national.csv | DANE GFR | 2016–2025 | revised vintage |
| CHL_tfr_national.csv | INE TGF | 2022–2024 | 2024=1.03; 2023/24 prov (observed-births break) |
| CHL_births_national.csv | INE births | 2010–2024 | 2023/24 provisional |
| ARG_births_national.csv | DEIS births | 2010–2024 | recomputed from microdata; 2024 prov |
| ARG_tfr_national.csv | AEPA/INDEC TGF | 2010–2021 | Censo-2010 denom; no period TGF post-2021 |
| CRI_tfr_national.csv | INEC TGF | 2010–2024 | 1.83→1.12; level ±0.03 (Censo 2022) |
| CRI_births_national.csv | INEC births | 2010–2024 | near-complete registry (final) |
| MEX_tfr_conapo_modeled.csv | CONAPO modeled TFR | 2010–2024 | ≥2020 projection; do NOT splice |
| MEX_tfr_enadid_survey.csv | ENADID survey TGF | 2014/18/23 | survey years; ≠ CONAPO |
| MEX_births_registered_inegi.csv | INEGI registered births | 2014–2024 | by registration year; 2020 COVID anomaly |
| {ISO}_tfr_implied.csv | Implied TFR from births | varies | back-derived: TFR(anchor)×GFR(t)/GFR(anchor); proxy/extension, NOT official; MEX distorted by registration lag |
| ARG_women1549_indec.csv | INDEC female 15–49 denominator | 2010–2025 | Censo-2010 + Censo-2022 vintages; +3.21% break at 2022 |
| ARG_tfr_implied_indec.csv | Argentina implied TFR (INDEC-pinned) | 2010–2024 | anchor 2021=1.558; 2024 ≈ 1.15–1.19 |
| {ISO}_asfr.csv | Age-specific fertility (Check 5) | ARG/MEX/CHL | per 1,000 by 5-yr age group; tempo-vs-quantum; Colombia pending |
| {ISO}_coupling.csv | Partnered-share endpoints | MEX/CRI/CHL/ARG | ENDPOINTS only; annual 20–39 path = Stage 2; ARG is CABA-only |

**Identification discipline:** these are the TFR *output* series to be matched. Covariate *input*
series live separately in `../worldbank/`. Do not conflate.
