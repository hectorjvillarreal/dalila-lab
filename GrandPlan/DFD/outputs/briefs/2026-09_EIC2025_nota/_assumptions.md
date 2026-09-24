---
type: deliverable_assumptions
deliverable: nota_EIC2025 v0.2 (preliminar)
build_instructions:
  - _crossrefs/_build_instructions/2026-09-23_DFD_nota-EIC2025_build-instruction.md (v0.1)
  - _crossrefs/_build_instructions/2026-09-23_demographics_commit-endorsements_nota-v0.2.md (v0.2, Step 5)
review_record: _crossrefs/corpus/demographics/_pending/2026-09-23_nota-EIC2025-v0.1_Anne-Cath-review.md
governing_instructions: _crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md v1.6
status: v0.2 delivered 2026-09-23; awaiting Anne/Cath review of v0.2 (record §5) and Héctor sign-off; no endorsed_by
---

# Supuestos y estado de los resultados — v0.2

Machine-readable copy of Recuadro 2 plus everything behind it. `./build.sh` rebuilds the deliverable
(scenarios → fiscal → figures → numbers → PDF). Every number in the PDF is a `\N{key}` macro written
by `scripts/04_numbers.py` into `build/numbers.tex`; none is typed into the `.tex`. The v0.1 PDF that
Anne and Cath reviewed is kept at `_archive/nota_EIC2025_v0.1.pdf`. The v0.1 sources were superseded in
place and cannot rebuild it.

## What changed from v0.1 (review record §4, items 1–7)

| Item | v0.2 |
|---|---|
| 1 C1 | Recuadro 1 (ii): the UN low variant is 1.64 for 2024 and reaches 1.20 by 2050; the observed 1.23 is already at that variant's long-run floor (record §1 wording) |
| 1 C2 | The education sentence ends in 2031 |
| 1 F1 + 2 | Base moved 15 Oct → 1 Jul 2025 by a **pure time shift**. Each age-sex group goes back 0.288 yr at its own annual rate of change under the observed 2025 components (TFR 1.23, net migration −229,840/yr, CONAPO 2025 mortality). WPP enters nowhere in the base. All CSVs regenerated |
| 3 | Recuadro 2 adds: the 65+ gap sentence with the Step 4 check numbers; the window span with its definition (years within 1 point of the minimum); the τ formula and the source of e |
| 4 | The page-3 headline is the TDR minimum before and after (record §3.1). F3 is two panels, TDR and OADR (record §3.2), with the sentence on the composition of dependents in the caption. No number for the cost of an older adult versus a child, because no NTA profile for Mexico is in the corpus |
| 5 | **τ = ρ · OADR / e**. The coverage parameter is removed from every table and sentence. Sensitivity row: base 65+ replaced by CONAPO mid-2025 |
| 6 | Education sentence per C2; growth sentence per §3.4; implication 3 replaced per §3.3 |
| 7 | All numbers from CSV |

**One change beyond items 1–7, flagged for Anne (F7).** The emigration age-sex profile is now the full EIC
profile from RR 37/26 Gráfica 9: emigrants Oct 2020–Oct 2025 by 5-year age and sex, transcribed to
`data/eic2025_emigrants_age_sex_grafica9.csv`. It replaces the v0.1 approximation that spread the remaining
28.9 % pro rata over ages 35–44. Anne's binding ruling was "EIC age-sex shares". Gráfica 9 shows the remaining
share is actually spread over 35–39 (9.1), 40–44 (5.4), 45+ (≈9) and children 0–14 (5.1). The effect in the
nota: 6–14 falls to 2031 by −17.7 %, where the record's figure was −16 %, because children now emigrate too.
The −17.7 % does not depend on fertility; Optimista differs by 22 k in 2031 because it uses WPP's migration
totals.

## Step 1 — scenario runs (v0.2)

| Item | Value used | Source / note |
|---|---|---|
| Model | Two-sex cohort-component, single ages 0–99 + 100+, annual mid-year steps 2025→2050 | `scripts/01_scenarios.py` |
| Base, private dwellings | 130,393,389 by sex × 5-yr band (75+ open) | EIC 2025 open data, national row |
| Base, complementary | 517,925 at CPV 2020 non-household age-sex shares | CPV 2020 tab. 01-02 minus 13-08 |
| Single-year split | CONAPO 2025 mid-year within-band proportions by sex | |
| Reference date | Pure time shift, dt = 0.288 yr (see table above) | review record §1 F1 |
| Base result | 130.91 M; 0–14 28.51 M; 15–64 89.32 M; 65+ 13.08 M; TDR 46.57 (EIC published 46.4 on private dwellings, 15 Oct) | |
| Mortality | CONAPO 2023 conciliación, m = deaths / mid-year population by age, sex, year; e0 2025/2050 F 79.11/83.58, M 72.64/77.23 (CONAPO published F 79.04/83.47, M 72.57/77.07) | provenance below |
| Fertility pattern | CONAPO 2024 ASFR shape, scaled | EIC bundle has no ASFR |
| TFR paths | Optimista WPP 2024 medium (1.87 → 1.70); Central 1.50; INEGI directo 1.23; Estrés 1.50 − 0.10/yr → 0.90 from 2031 | v1.6 |
| SRB | WPP 2024 medium | |
| Net migration | Central, INEGI directo: −229,840/yr to 2030, linear to −135,000 by 2040, constant. Estrés: no taper. Optimista: WPP 2024 medium | EIC lower bound; the 2015–20 range is 107–161 k/yr |
| Migration profile | EIC Gráfica 9 by 5-yr age × sex, uniform within band | **F7** |
| Sensitivities (CSV only) | `eic2025_conapo65_sensitivity`: base ages 65+ replaced by CONAPO mid-2025 single ages. `wpp2023_sensitivity`: WPP mid-2023 base | the WPP-base Central 2050 is 140.34 M, reproducing the endorsed 140.4 M |

### Results (base EIC 2025)

| Escenario | Pob. 2050 (M) | TDR min (year) | Within 1 pt of min | OADR 2025 → 2050 | 15–64 first falls |
|---|---|---|---|---|---|
| Optimista | 144.2 | 46.4 (2027) | 2025–2032 | 14.6 → 31.5 | 2036 |
| Central | 135.5 | 45.0 (2030) | 2027–2035 | 14.6 → 33.1 | 2036 |
| INEGI directo | 128.7 | 42.3 (2035) | 2031–2036 | 14.6 → 34.2 | 2036 |
| Estrés | 121.2 | 40.7 (2035) | 2034–2037 | 14.6 → 35.4 | 2036 |

With the CONAPO 65+ base, Central's TDR minimum is 43.8 in 2030 and its OADR in 2025 is 13.1.

## Step 3 — fiscal indicators (v0.2)

| Parameter | Value | Source |
|---|---|---|
| ρ | 0.50 | IM-6 `κ_rep`, `Missions/Funded/BID2/GE-now with Gender/ge_model_gender.jl:61`, commit `5368693`; j_R = 10 = age 65 (line 50) |
| e | 0.6322 | Employed / population 15–64, INEGI ENOE 2026-Q2 microdata `enoe_2026_trim2_csv.zip`, table `ENOE_SDEMT226.csv` (INEGI filter r_def = 0, c_res ∈ {1, 3}; clase2 = 1; weight fac_tri). Accessed 2026-09-23, sha256 `020811fa…1d91e`. Check: employed 15+ 60.04 M; population 15–64 89.11 M (EIC 89.06 M). Held constant |

| τ (% of wage bill) | 2025 | 2035 | 2050 |
|---|---|---|---|
| Central | 11.6 | 16.2 | 26.2 |
| INEGI directo | 11.6 | 16.2 | 27.1 |
| Central, CONAPO 65+ | 10.4 | 15.4 | 26.0 |

6–14 (Central / INEGI directo): 18.8 M (2025) → 15.5 M (2031, −17.7 %, fertility-invariant) → 13.8 / 12.7 M (2035)
→ 12.9 / 10.6 M (2050; −31.2 % / −43.8 %). g_l: +0.37 %/yr 2025–35 in every scenario; 2035–50 −0.48 (Central),
−0.69 (INEGI directo).

## Step 4 — the 65+ gate (reading not chosen)

See `_crossrefs/corpus/demographics/country/MEX/eic2025_65plus_check.md`. At 15 Oct 2025, 65+ is 13.23 M in the
EIC, 12.51 M in the CPV 2020 aged forward (net of emigration) and ≈ 11.84 M in CONAPO. The EIC−CONAPO gap
of ≈ 1.4 M splits roughly in half. About 0.67 M is CONAPO below the aged census, which was already −0.48 M in
2020. About 0.73 M (+5.8 %) is the EIC above the aged census, concentrated at 65–69 (+8.3 %). This part is not
separable from CONAPO's mortality: a 10 % error in the 3.25 M cohort deaths would move the aged figure by
~0.32 M. The difference is ambiguous, so it is reported and stopped for Anne. v0.2 stays on the EIC base, with
the CONAPO-65+ sensitivity row.

## CONAPO provenance

The Internet Archive copy of the official zip, sha256 `ddcf182a05888672806f43113cf9405f17ef4cb410e8f5e4017067d160b1c19b`,
archived at `https://web.archive.org/web/20241110075122id_/https://conapo.segob.gob.mx/work/models/CONAPO/pry23/DB/ConDem50a19_ProyPob20a70.zip`.
The official endpoints were retried on 2026-09-23; response codes are in the 65+ check file. It was verified
against the official `05_indicadores_demograficos_proyecciones.csv` from datos.gob.mx (sha256 `e0407d16…ae6cd`).
Population, deaths, births, net migration and 65+ are identical for 2020–2050; TGF and e0 differ only in the
third decimal.

## Open flags

- **F7 (Anne)** — emigration profile from Gráfica 9, described above.
- **F2/F3 (Cath)** — closed by record §3.1: the headline is the minimum, and the span is in Recuadro 2 with its
  definition.
- **F5 (Cath)** — closed by record §3.3: the formula has been replaced.
- **Title (Héctor)** — "una ventana fiscal más corta" is still the proposed title. The page-3 headline now reads
  "La ventana de reforma ya está abierta". Héctor edits both.
- **Implication 1** — kept as drafted; the Central minimum is now 2030, with the within-1-point span 2027–2035.
  Héctor edits.
