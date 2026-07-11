---
type: corpus_entry
tier: data_source
project_scope: [DFD]
authors: [DANE; INE Chile; DEIS-MINSAL Argentina; INDEC; INEC Costa Rica; INEGI; CONAPO; World Bank]
year: 2026
title: "Stage 1 data product — Rapid Fertility Collapse in Latin America (TFR, births, covariates, 5 countries)"
venue: "DFD parallel research data product; national statistical offices + World Bank WDI"
doi: "see per-source URLs below"
date_added: 2026-06-17
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE1_data_acquisition_fertility_collapse.md"
---

# Stage 1 Data Provenance Log

Provenance for every data product under `data/`. This single PROTO-RAG-001 `data_source`
entry, together with the per-directory `README.md` sidecars, covers all CSVs (Debb
requirement: data lands conformant, not retrofitted). Acquired 2026-06-17.

## Acquisition tooling
- `data/_acquire_worldbank.py` — World Bank WDI v2 REST API (programmatic).
- `data/_build_national.py` — national-source values transcribed from the documents below.
- `data/_crosscheck_and_charts.py` — Check 4 cross-check + per-country TFR charts.
- `data/_births_implied_charts.py` — implied TFR (`{ISO}_tfr_implied.csv`) + dual-panel charts
  (`charts/{ISO}_panel.png`). Implied TFR is a derived proxy (births / WB women 15–49, anchored to
  national TFR); not an official series. Mexico's implied TFR is distorted by registration lag (do not use).

## World Bank backbone — `data/worldbank/`
WB WDI v2 API, format=json, per_page=400. Endpoint template:
`https://api.worldbank.org/v2/country/{ISO3}/indicator/{CODE}?format=json`.
Countries: COL, ARG, CHL, CRI, MEX. lastupdated 2026-04-08. Full per-file inventory
(indicator code, n_obs, year span, exact URL, status) in `data/worldbank/_fetch_log.csv`.

| Indicator | WDI code | Series |
|---|---|---|
| Total fertility rate | SP.DYN.TFRT.IN | tfr (1960–2024) |
| Crude birth rate | SP.DYN.CBRT.IN | crude_birth_rate |
| Population total / female | SP.POP.TOTL / SP.POP.TOTL.FE.IN | denominators |
| Net migration | SM.POP.NETM | migration |
| Urban population % | SP.URB.TOTL.IN.ZS | covariate |
| Female labor force participation | SL.TLF.CACT.FE.ZS | covariate (Calles-Vogl non-dominant control) |
| Employment in agriculture % | SL.AGR.EMPL.ZS | covariate (Calles-Vogl dominant) |
| Agriculture value added % GDP | NV.AGR.TOTL.ZS | covariate (sectoral composition) |
| Female educational attainment (primary/upper-sec/bachelors) | SE.PRM.CUAT.FE.ZS / SE.SEC.CUAT.UP.FE.ZS / SE.TER.CUAT.BA.FE.ZS | covariate (Calles-Vogl dominant) |
| Female pop by 5-yr age 15–49 | SP.POP.{1519..4549}.FE.5Y | Check-4 denominator reconstruction |

**Forensic note:** WB TFR is WPP-derived, model-smoothed, lagged. It does NOT capture the
2020–2024 national collapse tail (e.g., Colombia WB 2024 = 1.63 vs DANE 1.1). Backbone/covariate use only.

## National sources — `data/national/`

### Colombia (DANE)
- TFR + GFR + births: DANE Estadísticas Vitales (EEVV) bulletins.
  - https://www.dane.gov.co/files/operaciones/EEVV/2025/25-sep-2025/bol-EEVV-Isem2025pr.pdf (TFR, Gráfico 7) — **verified directly via pdftotext: 2024 TGF = 1,1, "valor más bajo de la serie"**
  - https://www.dane.gov.co/files/operaciones/EEVV/2026/20-mar-2026/bol-EEVV-IIsem2025pr.pdf (births + revised GFR)
  - https://www.dane.gov.co/files/operaciones/EEVV/2025/26-mar-2025/bol-EEVV-2024pr.pdf (superseded 2024pr births 445,011)
- Migration: https://www.migracioncolombia.gov.co/infografias-migracion-colombia/informe-de-migrantes-venezolanos-en-colombia-en-febrero (Feb-2024 stock 2,845,706)

### Chile (INE / DEIS-MINSAL)
- Births 2010–2022: INE Anuario de Estadísticas Vitales 2022, Tabla 10 — https://www.ine.gob.cl/docs/default-source/nacimientos-matrimonios-y-defunciones/publicaciones-y-anuarios/anuarios-de-estad%C3%ADsticas-vitales/anuario-de-estad%C3%ADsticas-vitales-2022.pdf
- TFR 2023 + births 2023 (provisional): https://www.ine.gob.cl/docs/default-source/nacimientos-matrimonios-y-defunciones/publicaciones-y-anuarios/anuarios-de-estad%C3%ADsticas-vitales/estad%C3%ADsticas-vitales-cifras-provisionales-2023-(versi%C3%B3n-marzo-2025).pdf
- TFR 2024 = 1.03 + births 2024 (provisional): https://www.ine.gob.cl/docs/default-source/nacimientos-matrimonios-y-defunciones/publicaciones-y-anuarios/anuarios-de-estad%C3%ADsticas-vitales/estad%C3%ADsticas-vitales-cifras-provisionales-2024.pdf
- Foreign population (denominator context): INE-SERMIG EPE 2022/2023 reports.

### Argentina (DEIS / INDEC)
- Births 2005–2022 (microdata, summed by year): http://datos.salud.gob.ar/dataset/d1350588-d8bb-4892-b21c-48738311e218/resource/5a68ea36-03fe-4b38-b590-d7cf2a13b821/download/nacidos-vivos-registrados-en-la-republica-argentina-entre-los-anos-2005-2022.csv
- Births 2024 (provisional): https://datos.salud.gob.ar/dataset/d1350588-d8bb-4892-b21c-48738311e218/resource/ace82479-4659-4788-9609-5b98bc9081bd/download/nacimientos2024-.csv
- Births 2023 + GFR 38.6: DEIS Síntesis Estadística N°10 (jun-2025) — https://www.argentina.gob.ar/sites/default/files/31-10-sintesis-estadistica2023.pdf
- TFR 2010–2021: AEPA 2023 Tabla 1 — https://www.aacademica.org/xvii.jornadas.aepa/2.pdf ; INDEC Anuario 2023 precise endpoints — https://www.indec.gob.ar/ftp/cuadros/sociedad/030902_2023.xlsx
- Censo 2022 projections: https://www.indec.gob.ar/ftp/cuadros/publicaciones/proyecciones_nacionales_2022_2040.pdf
- **Female 15–49 denominator (for implied-TFR pin)** — `ARG_women1549_indec.csv`:
  - Censo-2010 vintage, annual 2010–2024: INDEC Cuadro 2, https://www.indec.gob.ar/ftp/cuadros/poblacion/c2_proyecciones_nac_2010_2040.xls
    (downloaded + parsed cell-by-cell with xlrd; Mujeres block rows 73–79; **independently reproduces** the agent's 2010–2022 figures exactly; 2023=11,631,314, 2024=11,695,576).
  - Censo-2022 vintage, 2022–2025: INDEC, https://www.indec.gob.ar/ftp/cuadros/poblacion/proyecciones_nacionales_2022_2040_base.csv (female single ages summed; +3.21% vs Censo-2010 at 2022).
  - Companion (not yet used): INDEC ASFR by 5-yr group 2010–2040, c4_proyecciones_nac_2010_2040.xls — available for a future ASFR-based Check 5.
  - Pinned implied TFR: `ARG_tfr_implied_indec.csv`; script `_argentina_indec_pin.py`; chart `charts/ARG_panel_indec.png`.

### Costa Rica (INEC)
- TFR 2010–2023: INEC Panorama Demográfico 2023, Cuadro 2.2 — https://admin.inec.cr/sites/default/files/2024-12/repoblacEV-Panorama%20demogr%C3%A1fico-2023A.pdf
- TFR 2024 = 1.12: INEC news release — https://inec.cr/noticias/fecundidad-continua-descendiendo-112-hijos-e-hijas-mujer-2024
- Births + crude birth rate 2010–2024: INEC Estadísticas Vitales 2024, Cuadro 3.21 — https://admin.inec.cr/sites/default/files/2025-11/repoblacEV-Estad%C3%ADsticas%20vitales-2024A.pdf
- Coupling endpoints: CCP-UCR "Patrones históricos de nupcialidad" — https://ccp.ucr.ac.cr/sites/default/files/2023-04/Patrones_hist%C3%B3ricos_nupcialidad_estado_conyugal.PDF

### Mexico (CONAPO / INEGI)
- CONAPO modeled TFR + births 2010–2024: ConDem 1950-2019 + Proy 2020-2070 (2023 base), sheet 5_Indicadores — https://conapo.segob.gob.mx/work/models/CONAPO/pry23/DB/ConDem50a19_ProyPob20a70.zip
- ENADID survey TGF (2014/2018/2023): https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2024/ENADID/ENADID2023.pdf ; https://www.inegi.org.mx/contenidos/programas/enadid/2014/doc/resultados_enadid14.pdf
- INEGI registered births (ENR) 2023/2024: https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enr/enr2024_RR.pdf ; https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enr/enr2024_CP.pdf

## ASFR (Check 5) and coupling endpoints
- **ASFR** (`{ISO}_asfr.csv`): Argentina — AEPA 2023 *Bathory, Muhafra & Grushka, "El descenso de la fecundidad
  en Argentina 2010–2021", XVII Jornadas AEPA*, Tabla 1 (OBSERVED: DEIS births / INDEC-2013 projection);
  https://www.aacademica.org/xvii.jornadas.aepa/2.pdf . Mexico — INEGI ENADID 2023 presentation,
  https://www.inegi.org.mx/contenidos/programas/enadid/2023/doc/resultados_enadid23.pdf . Chile — INE
  provisional bulletins EV2023/EV2024, Gráfico 4. Colombia — DANE EEVV Boletín Isem-2025pr, Gráfico 6 (TEFE
  2015/2020/2023/2024; partial — grouped bar chart, ~24/32 bars resolved; pdftotext -layout). Modeled ASFR
  companion: INDEC c4_proyecciones_nac_2010_2040.xls.
- **Coupling endpoints** (`{ISO}_coupling.csv`): Mexico ENADID 2018/2023 (15–49 partnered, VERIFIED);
  Costa Rica CCP-UCR (cohabitation 1990/2019); Chile CASEN via ICSO-UDP (dated); Argentina Dirección de
  Estadística CABA (CABA city only). All ENDPOINTS — annual 20–39 path deferred to Stage 2 microdata.

## Verification pass (2026-06-17/18)
All five countries' headline figures independently re-verified against primary sources; **zero material
discrepancies**. Colombia TFR verified by direct pdftotext of the DANE bulletin; Argentina female-15–49
denominator verified by direct xlrd parse of the INDEC .xls (reproduced the agent's integers exactly);
Chile/Costa Rica/Mexico/Argentina-TGF verified against primary PDFs/xlsx by a second research pass.
Footnotes: Chile 2023 births 174,067 = revised Mar-2025 vintage (earlier provisional 171,992); Costa Rica
2023 TGF 1.22 (Cuadro 2.2, authoritative) vs 1.19 (INEC press release). CONAPO TFR matched to 4 decimals.

## Access notes / caveats
- Colombia DANE TGF transcribed from chart labels (Gráfico 7), 1-decimal; 2024=1.1 verified in PDF text.
- Argentina births independently recomputed from DEIS microdata (2023 sum matched published 460,902).
- Mexico CONAPO/ENADID/INEGI are three non-identical series; never spliced (see memo).
- Values flagged NOT FOUND by the acquisition pass (annual coupling paths, ASFR, Chile TGF 2010–21,
  Argentina period TGF 2022–24) are deliberately absent from the CSVs — no estimation was performed.

## Build-instruction archival (follow-up for Debb)
This work was executed against `STAGE1_data_acquisition_fertility_collapse.md`, which functions as the
build instruction. A formal `_crossrefs/_build_instructions/` archival entry (build_type: expansion) and a
`mission-project-map.md` cross-reference are flagged as a Debb follow-up per PROTO-RAG-001 §Provenance.
