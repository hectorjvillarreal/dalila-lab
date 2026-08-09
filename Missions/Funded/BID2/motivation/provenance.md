# Provenance — BID2 motivation: Mexican health expenditure by sex, income, and age

Build instruction: `Missions/Funded/BID2/draft_2609/CC_instrucciones_motivation-health-profiles_v2.md` (v2, supersedes v1 ENIGH-only).
Analyst: Claude Code (Fable 5), directed by Héctor J. Villarreal.
All downloads performed **2026-08-08** from Dalila.

## Estimation environment

R 4.4.3 in conda env `renv` (conda-forge: r-base 4.4, r-survey, r-srvyr, r-ggplot2,
r-haven, r-data.table, r-readr), created 2026-08-08. R was not previously installed on
Dalila; installed rather than falling back to Python, per team convention in the build
instruction. Activate with `conda activate renv`.

## Data sources

### ENIGH — Nueva Serie, waves 2018, 2020, 2022, 2024 (INEGI)

Program pages (`https://www.inegi.org.mx/programas/enigh/nc/<year>/`) are a JS
application with no static links; the file layer under `contenidos/` was verified by
HTTP HEAD (200) and by zip signature after download. URLs, all accessed 2026-08-08:

`https://www.inegi.org.mx/contenidos/programas/enigh/nc/<year>/microdatos/enigh<year>_ns_<table>_csv.zip`

for `<year>` ∈ {2018, 2020, 2022, 2024} × `<table>` ∈ {concentradohogar, gastoshogar,
poblacion, hogares, gastospersona}. All 20 files downloaded successfully (sizes logged
in download log; e.g. 2024 gastoshogar 54.4 MB). Stored under `data/enigh/<year>/`
(not committed).

### ENSANUT 2018-19 and ENSANUT Continua 2024 (INSP)

Index navigated at `https://ensanut.insp.mx/encuestas/index.php`. Downloads on
`descargas.php` are form POSTs whose button `name` attribute is `ArchId` + base64 of
the file path; replicated with `curl --data-urlencode "<token>="` against
`https://ensanut.insp.mx/encuestas/<wave>/descargas.php`. Full page manifests
(file path ↔ token) preserved in the session scratchpad and reproducible from the
descargas pages. Accessed 2026-08-08.

Wave selection: ENSANUT 2018-19 (matches ENIGH 2018) and ENSANUT Continua 2024
(matches ENIGH 2024).

Files downloaded (each with its Catálogo .xlsx codebook):
- 2018: `CS_SERV_SALUD` (utilizadores de servicios de salud — utilization + motive),
  `CS_ADULTOS`, `CS_RESIDENTES` (roster: age, sex, insurance, forgone-care screening),
  `CS_HOGARES`, `CS_VIVIENDAS`; questionnaire PDF for utilizadores module.
- 2024: `hogar_ensanut2024_w_ICB`, `integrantes_ensanut2024_w_ICB` (roster),
  `NSE_Hogar_ENSANUT_2024` + `NSE_Integrantes` (socioeconomic index),
  `adultos_ensanut2024_w` (**Stata .dta only** — no plain CSV published for this
  table; read with `haven`), `utilizadores_ensanut2024_w`; questionnaire PDF.

Stored under `data/ensanut/<wave>/` (not committed).

### ENASEM 2018, 2021, 2024 (INEGI open data)

The MHAS project site (mhasweb.org) requires registered login; INEGI's open-data
mirror does not. The INEGI program page is a JS shell, but its embedded JSON-LD
(`schema.org/Dataset` → `distribution.contentUrl`) exposes the direct file:

`https://www.inegi.org.mx/contenidos/programas/enasem/<year>/datosabiertos/conjunto_de_datos_enasem_<year>_csv.zip`

for years 2018 (12.5 MB), 2021 (12.1 MB), 2024 (16.6 MB); zip signatures verified
before download. Accessed 2026-08-08. The 2021 URL was read directly from the page's
JSON-LD; 2018 and 2024 follow the same pattern and were verified by content
(PK signature + coherent table index inside). Stored under `data/enasem/<year>/`
(not committed). Each wave unpacks to per-section table folders with
`conjunto_de_datos/`, `catalogos/`, and `diccionario_de_datos/` layers plus a
`0_indice_tablas` index.

Note: probes of `microdatos/enasem_<year>_csv.zip` return an HTML soft-404 with
HTTP 200 — INEGI serves 200 for nonexistent `contenidos` paths; verify by content,
not status code.

## Judy's frailty index — availability ladder (build instruction §ENASEM)

Rung 1 (search for construction code): **not found.** The only ENASEM artifact in the
BID2 tree is `GE-now with Gender/calibration_experiment/Calibration/draft_junev3/mortality_enasem.tex`
(searched 2026-08-08 for *enasem*, *mhas*, *frailty*, *mortality*, `.do`, `.R`, `.jl`,
`.dta`, `.sav` under `Missions/Funded/BID2/`).

Rung 2 (reconstruct from the write-up): **partially available.** The .tex documents the
convention — 21 deficits over five categories (ADLs, IADLs, mental/cognitive health,
medical diagnoses, health behaviors: obesity and smoking), Searle et al. (2008) /
Hosseini et al. (2021) fraction-of-deficits form, identical construction across waves
2018/2021/2024 — and the checks: Model B probit (frailty 2018 → mortality 2018–21,
n = 14,867, 1,229 deaths) with deviance pseudo-R² **0.142** full sample, **0.159**
women (Table 2 reports 0.159; build instruction says ≈0.16), svyglm with complex
design. But it does **not** itemize the 21 deficits.

Therefore the index built here is a **rung 2/3 hybrid**: a 21-item Searle-convention
index over the five documented categories, with every item listed below (§frailty
items, filled in by the construction script), checked against the published
pseudo-R². **The index is provisional pending Judy's confirmation** and is flagged as
such in READTHIS.md and in the note of every figure that uses it. It is a
reconstruction, not Judy's estimate.

## Decisions log

- 2026-08-08 · R over Python: installed R 4.4.3 via conda rather than using Python,
  keeping team convention (`survey`/`srvyr` + `ggplot2`).
- 2026-08-08 · ENSANUT waves: 2018-19 + Continua 2024, bracketing the ENIGH window;
  Continua 2025 exists but 2024 is the latest complete-release wave with the
  utilizadores module and NSE files.
- 2026-08-08 · ENASEM via INEGI open data (no registration) instead of mhasweb.org
  (login wall). Same microdata program (INEGI/UTMB collaboration).

(Variable code lists per survey are appended by the preparation scripts as they
select variables from the shipped dictionaries — see §code lists below.)

- 2026-08-08 · INPC: general national index (base 2a q. julio 2018), INEGI open data
  `https://www.inegi.org.mx/contenidos/programas/inpc/2018a/datosabiertos/conjunto_de_datos_inpc_indicador_mensual_csv.zip`
  (monthly, 2003-01 – 2025-12, accessed 2026-08-08). The open-data indicator file
  carries no health subindex, so the **general** index is used; stated in every
  figure note. ENIGH money variables (quarterly, referenced to Aug–Nov of the survey
  year) are deflated by Aug–Nov INPC means to **Aug–Nov 2024 pesos**.
- 2026-08-08 · ENIGH health claves are selected from each wave's shipped
  `catalogos/gastos.csv`, never from memory: 2018/2020/2022 = J001–J072 (72 codes);
  2024 (COICOP recode) = division 06 (71 codes) **plus 1212xx** health-insurance
  premiums, because COICOP moved premiums out of 06 while the old J set includes
  them (J071/J072). Verified against the concentrado `salud` aggregate: weighted
  detail/aggregate = 0.996 / 0.998 / 0.997 / 0.998 for 2018/2020/2022/2024
  (06-only for 2024 gives 0.892). Monetary out-of-pocket only (`tipo_gasto == G1`).
- 2026-08-08 · Income deciles: households ranked by quarterly current income
  (`ing_cor`), weighted by `factor`, ten equal weighted-household groups (INEGI
  tabulados convention). Design-based estimation uses `est_dis` strata × `upm`
  PSUs × `factor` weights, lonely PSUs certainty-adjusted.

- 2026-08-08 · Benchmark sources: GHED OOP per capita US$ for Mexico via the WHO
  GHO API (indicator `GHED_OOP_pc_US_SHA2011`, saved to
  `data/benchmark/ghed_oop_mex.csv`, latest year 2023); MXN/USD annual average
  via World Bank API `PA.NUS.FCRF` (`data/benchmark/wb_fx_mxn.csv`). Both
  accessed 2026-08-08.
- 2026-08-08 · Figure palette validated with the dataviz six-checks validator
  (light mode, all pass; aqua contrast WARN covered by visible labels + tables).

## Frailty index items (reconstruction — provisional pending Judy's confirmation)

21 deficits, Searle et al. (2008) fraction-of-deficits form, identical stems
across waves (`_18/_21/_24`), all but obesity taken from the shipped
`variables_creadas` constructed 0/1 dummies:

1–5 ADL: `abvd_caminar`, `abvd_banar`, `abvd_comer`, `abvd_cama`, `abvd_bano`
6–9 IADL: `aivd_comidas`, `aivd_comprar`, `aivd_medicina`, `aivd_dinero`
10–11 mental/cognitive: `cesd_deprimido` (5+ of 9 CES-D symptoms), poor
  self-rated memory (`memoria` ∈ {4,5})
12–19 diagnoses: `hipertension`, `diabetes`, `cancer`, `enf_pulm`, `infarto`,
  `prob_card`, `embolia`, `artritis`
20 obesity: BMI ≥ 30 from self-reported `c66` (kg) and `c67_1/c67_2` (m/cm) —
  computed from raw items because the shipped `imc_cat` category bounds are
  undocumented
21 current smoking: `tabaco`

Index = deficits present / deficits observed, requiring ≥ 15 of 21 observed.
Checks vs `mortality_enasem.tex`: median 0.095 (published p50 0.10); probit
pseudo-R² 0.167/0.137/0.192 (full/men/women) vs published 0.142/0.118/0.159 —
qualitative pass, numeric mismatch traced to an unobservable sample
restriction (published n = 14,867, 1,229 deaths; ours 16,702, 1,525; two
candidate restrictions tested in `enasem_probit_check_variants.csv`).

## Code lists

Per-wave health clave lists (code + official descriptor) are written by
`scripts/01_enigh_prepare.R` to `output/tables/enigh_health_claves_<year>.csv`
and combined in `enigh_health_claves_all.csv`; the Task B classification is
built on top of these in `output/tables/curative_preventive_classification.csv`.
ENSANUT variable selections (verbatim labels and answer codes, both waves):
`data/ensanut_varmap.md`. ENASEM variable selections (all sections, three
waves): `data/enasem_varmap.md`. Both maps were built by reading the shipped
codebooks/dictionaries, never from memory.
