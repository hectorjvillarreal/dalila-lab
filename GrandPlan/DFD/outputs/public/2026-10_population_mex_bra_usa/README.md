# Population 2025–2050: Mexico, Brazil, United States, from national data

Charts made on request on 2026-10-24: total population and the share aged 65+. They were revised
twice that day: first from UN-only, then from UN age patterns to an engine that uses national data
only. The UN WPP 2024 medium appears only as a reference line. This is a communication product: not
a DFD scenario, not IM-6, and nothing here feeds the corpus.

Interactive version (private dashboard, same results): https://claude.ai/artifact/AjhwcMqtEHTno71EoNdwdU

## Results

| | 2025 | Peak (central) | 2050 central | 2050 range (fertility ±0.2) | Official 2050 | UN medium 2050 |
|---|---|---|---|---|---|---|
| Mexico, M | 130.9 | 132.5 in 2038 | **129.4** | 125.8–133.1 | — (CONAPO excluded) | 148.9 |
| Brazil, M | 213.4 | 220.5 in 2042 | **218.5** | 213.0–224.0 | IBGE 2024: 218.4 | 217.5 |
| United States, M | 341.8 | 345.6 in 2036 | **339.3** | 331.0–347.6 | — | 380.8 |

| % aged 65+ | 2025 | 2030 | 2040 | 2050 central | 2050 range | Official 2050 |
|---|---|---|---|---|---|---|
| Mexico | 10.1 | 12.5 | 17.7 | **22.6** | 22.0–23.3 | — (CONAPO excluded) |
| Brazil | 11.6 | 13.7 | 17.9 | **23.1** | 22.5–23.7 | IBGE 2024: 23.2 |
| United States | 18.9 | 20.8 | 22.4 | **23.8** | 23.3–24.4 | — |

US sensitivity: with net migration of 1 M/yr instead of 321k, the 2050 population is 359.6 M and
the 65+ share 22.7 %.

## Method and inputs (`projection_national.py`)

Cohort-component projection by single year of age (0–89, 90+ open) and sex, in annual steps from
mid-2025. There is no UN input, and no CONAPO input for Mexico (excluded at Héctor's request on
2026-10-24 as unreliable).

| | Mexico | Brazil | United States |
|---|---|---|---|
| Base 2025 | INEGI EIC 2025: 5-year bands plus the 517,925 complementary population, split to single ages by following each INEGI CPV 2020 cohort five years forward (census smoothed for age heaping; ages 0–4 uniform) | IBGE 2024 revision, 2025 by single age (213.4 M) | Census Bureau Vintage 2025, by single age (341.8 M) |
| Mortality | IBGE's 2025 age pattern (assumption), rescaled by sex to two INEGI anchors on the EIC 2025 structure: registered deaths in 2024 at 65+ (57.9 %) and in total (819,672); falling 1 % a year | IBGE 2024 life tables, its year-by-year path | CDC/NCHS 2024 life tables; death rates fall 1 % a year (assumption) |
| Fertility level, held | 1.23: INEGI EIC 2025 (2024) | 1.48: IBGE TFR 2023 (1.57) scaled by the −5.8 % fall in 2024 births | 1.576: CDC final 2025 rates (Data Brief 571) |
| Fertility schedule | INEGI ENR 2025 mothers' ages over EIC 2025 women by age | IBGE 2025 | CDC 2025 |
| Net migration | INEGI EIC: −230k/yr to 2030, tapering to −134k by 2040; EIC age-sex profile | Implied by IBGE's projection (population change minus births plus deaths) | 321k/yr (Census Bureau 2026 figure) |

Life expectancy implied by these tables (M / F): Mexico 73.8 / 80.4 (2024), Brazil 73.5 / 80.0,
United States 76.7 / 81.6. Brazil and the US use a young-adult migration profile (assumption). The
fertility schedule by age is held fixed.

**Validation.** Fed each agency's own inputs (base, fertility path, mortality, migration), the engine
reproduces IBGE's Brazil in 2050: 218.28 vs 218.37 M, and 65+ at 23.13 vs 23.21 %
(`results/validation.txt`). With CONAPO excluded, Mexico has no agency projection to validate
against. Instead, its mortality is fitted to INEGI's 2024 registered deaths, and the fit returns
819k against 820k. There is no national US projection on file either.

## Caveats

- **Mexico.**
  - The 1.23 is a survey direct estimate. Registry-based figures run higher, about 1.5, above the
    high edge of the band.
  - Mexico has no INEGI life table, so the mortality age pattern is Brazil's, rescaled to INEGI
    death counts.
  - The INEGI EIC 2025 counts 13.2 M people aged 65+. INEGI's own 2024 death rates imply about
    10.7 M (the unresolved 65+ gap).
  - Anchoring to INEGI's 65+ death rate instead of its death counts gives 21.6 % aged 65+ in 2050,
    not 22.6 %. The share is therefore uncertain by about a point, depending on which count of
    older people is right.
- **Brazil.** 1.48 is a crude scaling, not an IBGE rate. Everything else is IBGE's, and the result
  is close to IBGE's own projection.
- **United States.** The result depends mostly on migration. The 1 % a year mortality decline is our
  assumption.
- **All three.** These are projections of what happens if current conditions hold, not forecasts.
  The fertility band barely moves the 2050 65+ share, because everyone who will be 65+ in 2050 is
  already alive.

## Files

- `projection_national.py`: engine; writes `results/projections_national.csv` (country, scenario,
  year, population, 65+ share; reference paths `ibge_2024` and `un_medium`),
  `results/validation.txt`, `results/assumptions.json` and `results/inputs_sha256.txt`.
- `charts_observed.py`: population figures `figures/population_*_2025_2050.png`.
- `share65_chart.py`: `figures/share65_2025_2050.png`.
- `data/census_nc-est2025-agesex-res.csv`: Census Bureau Vintage 2025.
- `data/cdc/nvsr75-05.txt`: text of NVSR 75(5), US life tables 2024 (pdftotext). The PDF itself is
  ignored by git.
- `data/un_extract_mex_bra_usa.json`: UN WPP 2024 extract, used only for the reference line.
- `data/ibge_2024/` (ignored by git, 30 MB): fetch before running:
  ```
  cd data/ibge_2024 && for f in tab1_idade_simples tab4_indicadores tab5_tabuas_mortalidade; do
    curl -O https://ftp.ibge.gov.br/Projecao_da_Populacao/Projecao_da_Populacao_2024/projecoes_2024_$f.xlsx; done
  ```
  The SHA-256 hashes are in `results/inputs_sha256.txt`.
- The Mexico inputs come from `../../briefs/2026-09_EIC2025_nota/data/` (EIC 2025 bands, CPV 2020
  non-household population, EIC emigrant profile; already committed).
- `data/inegi_cpv2020_single_age_prorated.csv`: INEGI CPV 2020 by single age and sex, age not
  specified prorated. Extracted from `cpv2020_b_eum_01_poblacion.xlsx`, tab. 03.
- `data/inegi_edr/EDR2024-def_RR.pdf` and `EDR2024-def_CP.pdf`: INEGI 2024 registered deaths,
  definitive (the mortality anchors).

```
cd GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa
~/miniforge3/envs/dalila/bin/python projection_national.py
~/miniforge3/envs/dalila/bin/python charts_observed.py && ~/miniforge3/envs/dalila/bin/python share65_chart.py
```

## Sources

INEGI, Encuesta Intercensal 2025 (RR 37/26); Censo de Población y Vivienda 2020; Estadística de
Nacimientos Registrados 2025 (RR 38/26); Estadística de Defunciones Registradas 2024, definitive
(Comunicado 142/25). IBGE, Projeções da População, revisão 2024 (tables 1, 4 and 5); Estatísticas do
Registro Civil 2024 (10 Dec 2025). US Census Bureau, Vintage 2025 estimates; blog on net
international migration (Jan 2026). CDC/NCHS, Data Brief 571 (21 Oct 2026); United States Life
Tables 2024 (NVSR 75(5)). UN, World Population Prospects 2024 (reference line only).

Superseded versions: UN-only (commit `eae76db`); UN age patterns with national levels (`991e4fe`,
`2004b48`).
