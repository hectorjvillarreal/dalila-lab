# Total population 2025–2050: Mexico, Brazil, United States, from national data

Projection charts made on request (2026-10-24), revised the same day because the first version
relied on UN WPP 2024. This version sets every level from the latest national data and shows the
UN medium only as a reference line. It is a communication product: not a DFD scenario, not IM-6,
and nothing here feeds the corpus.

## Results (millions)

| | 2025 base | Peak (central) | 2050 central | 2050 range (fertility ±0.2) | UN medium 2050 |
|---|---|---|---|---|---|
| Mexico | 130.9 | ≈132.0 in 2035 | **128.9** | 125.1–132.8 | 148.9 |
| Brazil | 213.4 | ≈218.4 in 2040 | **215.6** | 210.0–221.3 | 217.5 |
| United States | 341.8 | ≈345.6 in 2035 | **340.9** | 332.4–349.5 | 380.8 |

US sensitivity: with net migration of 1 M/yr instead of 321k, the 2050 total is 361.0 M.
Peaks are read off 5-year steps, so their years are approximate.

## Inputs

| | Mexico | Brazil | United States |
|---|---|---|---|
| Base population | INEGI EIC 2025 count, 130.9 M (15 Oct 2025); UN age-sex structure rescaled to EIC shares (0–14 = 21.6 %, 65+ = 10.1 %) | IBGE estimate, 213.4 M (1 Jul 2025); UN age-sex structure rescaled | Census Bureau Vintage 2025, 341.8 M (1 Jul 2025), by single age and sex |
| Fertility (held flat) | 1.23: INEGI EIC 2025, TGF for 2024 | 1.48: IBGE TFR 2023 (1.57) scaled by the 2024 fall in births (−5.8 %, IBGE Registro Civil 2024) | 1.576: CDC/NCHS final 2025 age-specific rates (Data Brief 571) |
| Life expectancy anchor (M / F) | 72.75 / 79.24, CONAPO 2026 | 73.3 / 79.9, IBGE 2024 | 76.5 / 81.4, CDC 2024 |
| Net migration | INEGI EIC: −230k/yr to 2030, tapering to −134k/yr by 2040; EIC age-sex profile | **UN path (exception)**: no national estimate is published | Census Bureau: 321k/yr (its 2026 figure "if current trends continue"), held |

The UN supplies only age patterns: the age pattern of fertility, the age pattern of mortality
and its improvement path. The UN's age structure is also used where no national one is loaded
(Mexico, Brazil). Mortality is UN abridged mx scaled by one factor per sex to hit the national
life expectancy in the anchor year. The factors are in `results/assumptions.json`.

## Caveats

- **Mexico.** The 1.23 is a survey direct estimate. Registry-based figures run higher (≈1.5 by
  the crude occurrence-basis proxy), and the high edge of the range, about 1.43, does not fully
  cover that. The EIC emigration figure is a lower bound for outflows and ignores foreign
  inflows.
- **Brazil.** Fertility of 1.48 is a crude scaling, not an IBGE rate. Migration follows the UN
  path because IBGE publishes no annual net-migration series. IBGE's own 2024 projection
  (peak 220.4 M in 2041) is shown as a marker.
- **United States.** The result depends mostly on migration. 321k/yr reflects the 2025–26
  collapse in net immigration. If flows recover, the path moves toward the 1 M sensitivity
  line, and further still toward the UN.
- **All three.** These are projections of what happens if current conditions hold, not forecasts.
  5-year steps; base dates differ by a few months (Oct vs Jul 2025) and are treated as 2025.

## Validation

With UN base, fertility, mortality and migration, the engine reproduces the UN 2050 totals:
Mexico −0.16 %, Brazil −0.10 %, United States −0.71 % (`results/validation.txt`).

## Files

- `projection_observed.py` (SHA-256 `604766f4…`): engine; writes `results/`.
- `charts_observed.py` (SHA-256 `ab0216dd…`): figures from `results/projections.csv`.
- `figures/`: one chart per country, `population_index_2025_2050.png` (central paths, 2025 = 100), and `population_overview_2025_2050.png` (2×2).
- `data/census_nc-est2025-agesex-res.csv`: Census Bureau Vintage 2025 national age-sex file (SHA-256 in `results/inputs_sha256.txt`).
- `data/un_extract_mex_bra_usa.json`: cached UN WPP 2024 extract for the three countries, so the
  run works without the 290 MB UN downloads in `../2026-09_mexico_2050/data/`.

```
cd GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa
~/miniforge3/envs/dalila/bin/python projection_observed.py && ~/miniforge3/envs/dalila/bin/python charts_observed.py
```

## Sources

INEGI, Encuesta Intercensal 2025 (RR 37/26). CONAPO, life expectancy 2026. IBGE, population
estimate 1 Jul 2025 (28 Aug 2025); Estatísticas do Registro Civil 2024 (10 Dec 2025); Tábuas
Completas de Mortalidade 2024; Projeções da População, revisão 2024. US Census Bureau, Vintage 2025
estimates and the Jan 2026 blog on net international migration. CDC/NCHS Data Brief 571 (21 Oct 2026)
and Mortality in the United States 2024. UN, World Population Prospects 2024.

The earlier UN-only version of this folder (commit `eae76db`) and its private dashboard
(https://claude.ai/artifact/AjhwcMqtEHTno71EoNdwdU) are superseded.
