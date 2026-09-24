# Scripts — Nota EIC 2025

Companion to the build scripts for the brief (build instruction
`_crossrefs/_build_instructions/2026-09-23_DFD_nota-EIC2025_build-instruction.md`).
Run from any directory in the `dalila` env; paths resolve relative to the script.

| Script | Step | Reads | Writes |
|---|---|---|---|
| `00_prepare_inputs.py` | 0 | `../data/raw/*` (git-ignored) and the EIC zip in the demographics corpus | `../data/*.csv` |
| `01_scenarios.py` | 1 | `../data/*.csv` | `../results/scenarios_eic2025_brief.csv`, `tdr_minima.csv`, `base_reconciliation_gate.csv` |
| `02_figures.py` | 2 | results + data | `../figures/F1…F4.{png,pdf}` |
| `03_fiscal.py` | 3 | results + `../data/enoe2026q2_employment_rate.csv` | `../results/fiscal_indicators.csv` (τ = ρ·OADR/e) |
| `04_numbers.py` | 4 | results, data, `_crossrefs/corpus/demographics/country/MEX/eic2025_65plus_check*.csv` | `../build/numbers.tex` (every `\N{key}` in the PDF) |

`../build.sh` runs 01 → 03 → 02 → 04 → LaTeX. Step 0 is run by hand when the raw inputs change.

`01_scenarios.py` is a two-sex, single-year-of-age, annual cohort-component projection. It is
the corpus skeleton `country/MEX/mex_scenarios_eic2025.py` rebuilt under the ruled assumptions.
The corpus script is left as run on 2026-09-23. Functions:

- `eic_oct2025` builds the base from the EIC private-dwelling bands plus the complementary population,
  split to single years. `time_shift` then moves it to mid-2025 (v0.2: pure time shift).
  `base_conapo65` and `base_wpp23` build the sensitivity bases.
- `mortality` builds CONAPO life tables by year and sex.
- `tfr_path` and `migration_path` hold the scenario definitions.
- `step` and `project` run the projection. Rates are averaged over the two calendar years a
  step spans, and births use mean female exposure.
- `indicators` and `tdr_minimum` produce the CSV outputs.

Every assumption, validation, and open flag is in `../_assumptions.md`.

`results/scenarios_eic2025_brief.csv` columns: `base` (`eic2025`, `eic2025_conapo65_sensitivity` or `wpp2023_sensitivity`),
`scenario`, `scenario_name`, `year`, `population`, `pop_0_14`, `pop_6_14`, `pop_15_64`,
`pop_65plus`, `pop_80plus`, `women_20_39`, `tdr`, `ydr`, `oadr`, `support_ratio`, `growth_15_64_pct`
(vs previous year), `tfr`, `net_migration`, `births_next_12m`.
