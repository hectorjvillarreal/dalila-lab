# Briefing for Judy — reconstruction of your ENASEM frailty index (please confirm)

**From:** Héctor (analysis run on Dalila, 2026-08-08)
**Mission:** BID2 · health-refocused paper, motivation section
**Bottom line:** for the new motivation analysis I needed your frailty index on
ENASEM 2018/2021/2024, could not find your construction code in the BID2 tree,
and rebuilt it from the specification in `mortality_enasem.tex`. It reproduces
your published results **qualitatively but not exactly**, so everything that
uses it is flagged *provisional pending your confirmation*. This note tells you
exactly what I built, where it deviates, and the specific questions that would
let me either match your estimate or adopt yours directly.

---

## Why a reconstruction

The working instruction was: use your index, don't re-derive a competitor. I
searched `Missions/Funded/BID2/` for any construction artifact (scripts, `.do`,
`.R`, `.jl`, saved index variables, `.dta`/`.sav` files); the only ENASEM
artifact present is the write-up
`GE-now with Gender/calibration_experiment/Calibration/draft_junev3/mortality_enasem.tex`.
That document specifies the convention — 21 deficits over five categories
(ADLs, IADLs, mental/cognitive, diagnoses, behaviors: obesity and smoking),
Searle et al. (2008) / Hosseini et al. (2021) fraction-of-deficits form,
identical construction across waves — but **does not itemize the 21 deficits**.
So the rebuild is a best-effort reading of your spec against the shipped
ENASEM constructed files, not your code.

## What I built

Data: INEGI's ENASEM open-data packages, 2018/2021/2024. All items below come
from the `variables_creadas` constructed files (0/1 dummies, identical stems
across waves) except obesity, computed from raw self-reported weight/height.

| # | Category | Items (variable stems) |
|---|---|---|
| 1–5 | ADL (5) | `abvd_caminar`, `abvd_banar`, `abvd_comer`, `abvd_cama`, `abvd_bano` |
| 6–9 | IADL (4) | `aivd_comidas`, `aivd_comprar`, `aivd_medicina`, `aivd_dinero` |
| 10–11 | Mental/cognitive (2) | `cesd_deprimido` (5+ of 9 CES-D items); poor self-rated memory (`memoria` ∈ {4,5}) |
| 12–19 | Diagnoses (8) | `hipertension`, `diabetes`, `cancer`, `enf_pulm`, `infarto`, `prob_card`, `embolia`, `artritis` |
| 20 | Obesity | BMI ≥ 30 from raw `c66` (kg) and `c67_1`/`c67_2` (m/cm) — the shipped `imc_cat` has undocumented category bounds, so I did not use it |
| 21 | Smoking | `tabaco` (currently smokes) |

Index = deficits present / deficits **observed**, requiring ≥ 15 of 21
observed (Searle denominator convention). A sixth ADL (`abvd_vestirse`)
exists and was deliberately left out to hit your count of 21.

## How it checks against your published numbers

Your Model B (frailty 2018 → death 2018–21, probit, svyglm with complex
design). Mine: same specification — frailty + frailty² + age + age² +
male + upper-secondary-or-more (education ≥ 10 years) — with the 2018 design
(`est_dis` strata × `upm_dis` PSU × `factori_18`), deviance pseudo-R².

| Quantity | Yours (tex) | Reconstruction |
|---|---|---|
| Median frailty (p50) | 0.10 | 0.095 (all three waves) |
| Pseudo-R², full sample | 0.142 | 0.167 |
| Pseudo-R², men | 0.118 | 0.137 |
| Pseudo-R², women | 0.159 | 0.192 |
| Frailty coefficient | 4.417 | 3.756 |
| Frailty² coefficient | −4.158 | −2.473 |
| n | 14,867 | 16,702 |
| Deaths 2018–21 | 1,229 | 1,525 |

Signs, curvature, the women > full > men R² ordering, and the gender frailty
paradox all reproduce. What does not: your sample size. My estimation sample
is everyone in the 2018 constructed file with nonmissing frailty, age, and a
positive weight, with deaths = `fallecido_21` ∈ {1, 2} from the 2024 master
follow-up. I tested two candidate restrictions to close the gap
(`output/tables/enasem_probit_check_variants.csv`):

- **age ≥ 50 at baseline:** n = 15,819, 1,509 deaths, pseudo-R² 0.168 — closer
  in n, not in deaths;
- **deaths from the ENASEM fieldwork only** (`fallecido_21` = 2, excluding the
  Mex-Cog Jul–Aug 2021 reports): 661 deaths — far too few.

Neither reproduces (14,867; 1,229), so some restriction in your sample is not
visible from the .tex — my leading suspects are listed in the questions below.

## What would resolve it — five questions

1. **The 21 items.** Does the table above match yours? Specifically: (a) is
   the 5-ADL set right, or did you use `vestirse` in place of one of mine;
   (b) is poor self-rated memory one of your two mental/cognitive items, and
   with which cutoff; (c) which 8 diagnoses — the tex says "hypertension,
   diabetes, cancer, among others," and the constructed file offers exactly 8;
   (d) obesity: BMI ≥ 30 from raw items, or an `imc_cat` category (which)?
   (e) smoking: current (`tabaco`) or ever-smoked?
2. **Denominator rule.** Fraction of *observed* deficits with a minimum-15
   rule, or complete-case over all 21?
3. **Sample for Model B.** What restriction produces n = 14,867 / 1,229
   deaths? (Age floor? direct interviews only, excluding proxy? excluding the
   2021 Mex-Cog death reports but not as crudely as my code-2-only variant?
   listwise deletion on a wider covariate set?)
4. **Education.** Is "upper secondary or more" `educacion` ≥ 10 years, or an
   `edu_gru` category?
5. **Design pair.** For the 2018 baseline I used the unsuffixed
   `est_dis`/`upm_dis` from the 2018 constructed file (the 2021/2024-suffixed
   pair is on a different coding). Same as yours?

If you still have the construction script (Stata/R), that answers everything
at once and I will swap it in verbatim and rerun; scripts are set up so the
substitution is one file.

## What depends on this, and how much

The index feeds one figure in the motivation set —
`output/figures/fig10_enasem_dynamics.png`: after a frailty increase ≥ 0.10
between 2018 and 2021, out-of-pocket spending response roughly doubles from
the bottom to the top wealth tercile (~24k vs ~42k pesos in 2021), and
conditional on a comparable decline, death by 2024 is ~17–20% in the lower two
terciles vs ~10.5% at the top. The decline threshold is a full decile of the
index range, so the qualitative pattern should be robust to the item-level
details in question — but per protocol it is presented as a reconstruction,
never as your estimate, and the provisional flag sits in the figure note,
`provenance.md`, and `output/READTHIS.md` until you confirm.

## Where everything lives on Dalila

Base: `~/Dalila/Missions/Funded/BID2/motivation/`

- Index construction: `scripts/05_enasem_prepare.R` (items, cleaning rules,
  special codes) — the one file to replace with your code if you have it.
- Probit check + variants: `scripts/06_enasem_analysis.R`;
  results in `output/tables/enasem_probit_reproduction_check.csv` and
  `enasem_probit_check_variants.csv`.
- Item list and decision log: `provenance.md`, §"Frailty index items".
- Variable map for all ENASEM sections/waves (verified against the shipped
  dictionaries): `data/enasem_varmap.md` — includes where your raw source
  items live (`h15a`–`h19a`, `c49_1–9`, `c4`/`c6`/`c12`/…, `c66`/`c67`).
- The figure using the index: `output/figures/fig10_enasem_dynamics.png`
  (+ plotted values in `output/tables/fig10_*.csv`).
