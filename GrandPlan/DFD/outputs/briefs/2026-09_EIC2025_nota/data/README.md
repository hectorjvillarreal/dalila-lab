# Inputs — Nota EIC 2025

Build instructions: `_crossrefs/_build_instructions/2026-09-23_DFD_nota-EIC2025_build-instruction.md` (v0.1) and
`_crossrefs/_build_instructions/2026-09-23_demographics_commit-endorsements_nota-v0.2.md` (v0.2).
The CSVs in this folder are written by `../scripts/00_prepare_inputs.py` from the raw downloads in
`raw/`. `raw/` is git-ignored (≈160 MB); each file can be re-fetched from the URL below and checked
against its sha256.

| Raw file (`raw/`) | Source | sha256 | Bytes |
|---|---|---|---|
| `CONAPO_2023_ConDem50a19_ProyPob20a70.zip` | CONAPO, *Conciliación demográfica 1950–2019 y Proyecciones de la población de México 2020–2070* (July 2023 release). The original path `conapo.segob.gob.mx/work/models/CONAPO/pry23/DB/ConDem50a19_ProyPob20a70.zip` now redirects to gob.mx and returns 404 (gob.mx sits behind a bot challenge). Retrieved 2026-09-23 from the Internet Archive capture `https://web.archive.org/web/20241110075122id_/https://conapo.segob.gob.mx/work/models/CONAPO/pry23/DB/ConDem50a19_ProyPob20a70.zip` (archive dates inside the zip 2023-07-21 / 2023-08-01) | `ddcf182a05888672806f43113cf9405f17ef4cb410e8f5e4017067d160b1c19b` | 80,454,093 |
| `WPP2024_Demographic_Indicators_Medium.csv.gz` | UN WPP 2024, `https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20(Standard)/CSV_FILES/WPP2024_Demographic_Indicators_Medium.csv.gz` | `286ac36bb1415e2e1ade03acfef0a29f0e4c087e2f78e38c48f50c5df89082bc` | 16,557,272 |
| `WPP2024_PopulationBySingleAgeSex_Medium_1950-2023.csv.gz` | UN WPP 2024, same folder | `f84c75789ccbd385122ad19bac70026d6306878442afbaa24e8e50a23b4bee2f` | 62,082,217 |
| `cpv2020_b_eum_01_poblacion.xlsx` | INEGI CPV 2020, cuestionario básico tabulados, `https://www.inegi.org.mx/contenidos/programas/ccpv/2020/tabulados/cpv2020_b_eum_01_poblacion.xlsx` (tab. 02) | `387965e04fa3aa0494fdd35a6e6fd16f2da02f35a87289955f2f9df8a6c5f39d` | 495,180 |
| `cpv2020_b_eum_13_hogares_censales.xlsx` | same folder (tab. 08) | `e98a90b72c9775850405e69af5402d34205c060882632ef8db14923d7f2af615` | 713,869 |
| `cpv2020_b_eum_16_vivienda.xlsx` | same folder (tab. 02; check total only) | `939a5143ffa27306074f75aee23472275df5a7240da40f3963bf7ac3dd601923` | 803,163 |
| `WPP2024_Demographic_Indicators_OtherVariants.csv.gz` | UN WPP 2024, same folder as the indicators file (low-variant TFR only) | `a860504df54877e4c19788bf6e16920d6017d021b4c149eaf8b5662674180a54` | 75,342,445 |
| `enoe_2026_trim2_csv.zip` | INEGI ENOE 2026-Q2 microdata, `https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/microdatos/enoe_2026_trim2_csv.zip` (table `ENOE_SDEMT226.csv`), accessed 2026-09-23 | `020811fa989a3e4e3e0daae39b32df6bb055f3ca59653b76ecc454f9b231d91e` | 35,213,597 |
| `CONAPO_official_datosgob_05_indicadores_demograficos_proyecciones.csv` | CONAPO indicators, official copy from datos.gob.mx dataset `proyecciones-de-poblacion`, accessed 2026-09-23; used only to verify the Wayback zip | `e0407d1640f38232023cf97656a0cb7be46049b1cb2344198c7e4aaec7cae6cd` | 1,689,266 |

EIC 2025 comes from the committed corpus source
`_crossrefs/corpus/demographics/sources/INEGI_2026-09-22_EIC2025_datos-abiertos_105_localidad50k.zip`
(national row, `ESTIMADOR = Valor`).

## Derived CSVs

| File | Content |
|---|---|
| `eic2025_mex_private_by_band_sex.csv` | EIC 2025 private-dwelling population by sex and 5-yr band (75+ open). The published `PCN_P_*_F/_M` are percentages **of the total population** (F sums to 51.91, M to 48.11), at two decimals; counts = sex total × band pct / sex pct sum |
| `eic2025_mex_national_indicators.csv` | EIC national totals and indicators (POBTOT, 6–14, 65+, TDR 46.40, TGF 1.23) |
| `cpv2020_mex_nonhousehold_by_band_sex.csv` | CPV 2020 total population (01-02) minus population in hogares censales (13-08), by sex and 5-yr band to 85+, age not specified dropped. Residual 499,090 = 490,995 collective-dwelling occupants (16-02) + ≈8,100 without dwelling. Stands in for the "collective-dwelling age-sex shares" |
| `conapo2023_mex_pop_midyear.csv`, `conapo2023_mex_deaths.csv` | CONAPO national mid-year population and deaths, single age 0–109, by sex, 2020–2050 |
| `conapo2023_mex_asfr.csv` | CONAPO national ASFR by 5-yr group 15–49, 2020–2050 |
| `conapo2023_mex_indicators.csv` | CONAPO national indicators (population, 65+, births, deaths, net migration, TGF, e0, dependency) |
| `wpp2024_mex_indicators_medium.csv` | WPP 2024 medium: population, TFR, SRB, net migration, e0, 2020–2050 |
| `wpp2024_mex_pop_single_age_2023.csv` | WPP 2024 mid-2023 population by single age and sex (thousands) |
| `wpp2024_mex_tfr_low_variant.csv` | WPP 2024 low-variant TFR, Mexico, 2024–2050 |
| `eic2025_emigrants_age_sex_grafica9.csv` | EIC 2025 emigrants Oct 2020–Oct 2025 by 5-yr age and sex, % of 1.3 M. **Transcribed by hand** from RR 37/26 Gráfica 9, p. 14 (chart labels, one decimal; men sum to 70.3, women to 29.7) |
| `enoe2026q2_employment_rate.csv` | ENOE 2026-Q2: population and employed 15–64 and 15+, and e = employed/population 15–64 (0.6322) |

CONAPO verification (2026-09-23): the official indicators file matches the Wayback zip exactly on population,
deaths, births, net migration and 65+ for 2020–2050. TGF and e0 differ only in the third decimal.

Note: WPP 2024's net-migration series for Mexico equals CONAPO's to the unit for 2020–2024
(e.g. 2020 −147,456 vs −147,457); WPP took CONAPO's migration estimate for the recent past.
