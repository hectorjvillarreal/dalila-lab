# Total population 2026–2050: Mexico, Brazil, United States

Simple projection charts made on request (2026-10-24). This is a communication product: not a DFD
scenario, not IM-6, and nothing here feeds the corpus.

Interactive version (private dashboard, same data): https://claude.ai/artifact/AjhwcMqtEHTno71EoNdwdU

## Figures (`figures/`)

| File | Content |
|---|---|
| `population_mexico_2026_2050.png` | UN WPP 2024 medium + 80% PI; INEGI EIC 2025-based range (TFR 1.23–1.5) |
| `population_brazil_2026_2050.png` | UN WPP 2024 medium + 80% PI |
| `population_united_states_2026_2050.png` | UN WPP 2024 medium + 80% PI |
| `population_index_2026_2050.png` | The three medium paths indexed to 2026 = 100 |
| `population_overview_2026_2050.png` | All four in one 2×2 figure |

## Numbers (UN WPP 2024 medium, mid-year)

| | 2026 | 2050 | 80% PI 2050 | Peak |
|---|---|---|---|---|
| Mexico | 133.0 M | 148.9 M | 137.3–161.0 | none before 2050 (UN: ≈149.9 M in 2058) |
| Brazil | 213.6 M | 217.5 M | 204.3–229.2 | 219.3 M in 2042 |
| United States | 349.0 M | 380.8 M | 355.4–404.3 | none before 2050 |

## Caveats

- **Mexico.** WPP 2024 overstates Mexico by the corpus's own reading. Starting from the INEGI EIC 2025
  count (130.9 M, Oct 2025) at TFR 1.23–1.5, the 2050 population is 130.1–136.9 M, against UN 148.9 M.
  The range comes from `../2026-09_mexico_2050/results/scenarios.csv` (verified public chart,
  5-year steps). It is not the v1.6 DFD scenario table.
- **Brazil.** IBGE's 2024 revision (2022 Census base) puts the peak at 220.4 M in 2041, close to WPP's
  219.3 M in 2042.
- **United States.** The Census Bureau's 2023 main series peaks near 370 M around 2080. WPP's 2050
  medium (380.8 M) is therefore above the Census path. The gap is mainly assumed net immigration,
  which has fallen since 2025.

## Reproduction

```
cd GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa
~/miniforge3/envs/dalila/bin/python population_2026_2050.py
```

- Script `population_2026_2050.py`, SHA-256 `c0d8ed9f…d362`.
- Data `data/WPP2024_TotalPopulationBySex_MEX-BRA-USA_2024-2050.csv` (SHA-256 `9e9c3c0e…dd14`).
  Extracted from the UN file `WPP2024_TotalPopulationBySex.csv.gz`, sha256 `66b84489…925b9`, the same
  download as `_crossrefs/corpus/demographics/sources/UN_2026-09-23_WPP2024_TotalPopulationBySex_MEX.README.md`.
  All variants for LocID 484 / 76 / 840, 2024–2050, thousands.
- Palette: dataviz reference categorical slots 1–3, validated all-pairs in light mode. Aqua is below
  3:1 contrast, so the charts carry direct value labels.
