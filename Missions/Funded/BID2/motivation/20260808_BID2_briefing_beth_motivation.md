# Briefing for Beth — BID2 motivation section: health expenditure by sex, income, and age

**From:** Héctor (analysis run on Dalila, 2026-08-08)
**Mission:** BID2 · health-refocused paper, motivation section
**Full detail:** `Missions/Funded/BID2/motivation/output/READTHIS.md` (prose),
`provenance.md` (sources and decisions), `output/NUMBERS.md` (every plotted value)

---

## What happened

The paper is being repositioned with health as the analytical center, and the
motivation section needed three empirical facts established from Mexican
microdata: (1) health spending has a steep age gradient and differs by sex,
(2) capacity to spend is sharply unequal by income, and (3) observed spending
is curative rather than preventive — with the corollary, tested directly, that
low spending among the poor signals unmet need rather than good health.

No single survey can do this, so three were triangulated, all downloaded from
official portals on 2026-08-08:

- **ENIGH 2018–2024** (INEGI, four waves) — the money and its distribution;
- **ENSANUT 2018-19 + Continua 2024** (INSP) — individuals, utilization,
  motive of care, and the *direct* forgone-care-because-of-cost questions;
- **ENASEM 2018/2021/2024** (INEGI open data) — the 50+ panel: health decline,
  spending response, and mortality follow-up.

Everything is scripted (R, `survey`-based design estimation, INPC-deflated to
constant Aug–Nov 2024 pesos) and re-runs end to end from `scripts/00–09`.
Individual-level profiles from ENIGH were built two independent ways — a
household regression on age-sex composition, and an NTA-style allocation using
utilization weights derived from ENSANUT (not imported) — and validated
against ENASEM's directly observed spending for ages 50+.

## Results

**Fact 1 — age gradient: strong.** Individual OOP spending at 85+ is ~5–7×
the young-adult level; women outspend men through ages 30–59. The two
allocation methods agree closely (correlation 0.959 across the 18 age-sex
cells), which is the evidence the profile is real and not an artifact of one
rule. The shape is stable across all four ENIGH waves (2020 pandemic-flagged).
This is the empirical counterpart of the model's $m_j$.

**Fact 2 — unequal capacity: strong.** The unconditional health budget share
looks flat across deciles, but only because poor households so often spend
*zero*; conditional on spending, their budget share is higher. Catastrophic
spending (WHO capacity-to-pay, 40%) falls from ~4–5% of households in the
poorest deciles to ~1% at the top. And the age gradient itself is several
times steeper for high-income households — inequality lives inside the age
profile, which is exactly what the model's mechanism needs.

**Fact 3 — curative dominance: supported, with an honest bracket.**
Unambiguously preventive rubros are ~2% of OOP spending everywhere. But
38–44% of spending sits in genuinely ambiguous rubros (OTC medicines, dental,
optical, chronic-disease maintenance, diagnostics, insurance premiums), so the
preventive share brackets between ~2% and ~46% depending on where the
ambiguous block is assigned. **"Majority curative" is robust; "overwhelmingly
curative" is assignment-dependent.** ENSANUT 2024, which observes the motive
of care directly, is consistent: preventive motives are a minority of health
needs and decline toward the poorest tercile. The full rubro-by-rubro mapping
is an auditable CSV (below), not a buried judgment.

**The corollary — unmet need, three independent lines, all agreeing:**
1. ENIGH: excess zero-spending among poor households, including those with a
   member 65+;
2. ENSANUT 2024: among people with a health need, forgone care runs 19% → 9%
   from poorest to richest wellbeing tercile, and *cost-attributed* forgone
   care collapses 3.5% → 0.1%; the uninsured fare worst on both;
3. ENASEM panel: after a frailty increase (2018→2021), spending responds in
   every wealth tercile but roughly doubles from bottom to top (~24k vs ~42k
   pesos/yr), and conditional on a comparable decline, death by 2024 is
   ~17–20% in the lower terciles vs ~10.5% at the top.

That third line is the restorative-spending mechanism the model formalizes,
observed directly — reported as descriptive conditional patterns, explicitly
not causal (wealth bundles insurance, education, prior health, access).

## Worth a second look: 2020 as a natural experiment

The build treats ENIGH 2020 as a pandemic-affected wave to flag — but the flag
hides something substantive. Real per-capita OOP health spending (constant
Aug–Nov 2024 pesos) jumped **~43% between 2018 and 2020** (1,259 → 1,799
pesos/year) and never came back down (1,715 in 2022, 1,915 in 2024). The same
break shows in the external benchmark: ENIGH's capture of GHED out-of-pocket
rises from 0.22 in 2018 to 0.31–0.34 from 2020 onward
(`output/tables/verification_ghed_benchmark.csv`).

The reading: when the public system saturated in 2020, households that could
pay bought care out of pocket — and the shift persisted after the emergency.
That is the restoration constraint binding on cash *in the aggregate time
series*, not just in the cross-section: an in-kind provision shock forcing
exactly the private spending response the model formalizes, with the poor
(who could not respond — see the forgone-care evidence) absorbing it as unmet
need instead. If you think it earns more than a footnote in the motivation, a
decile-split of the 2018→2020 spending jump would show who financed the surge;
the data and scripts are already in place, so it is an afternoon, not a
project. Caveat before leaning on it: part of the 2018→2020 step could be
survey-instrument improvement rather than behavior (capture ratio and spending
jump together), so any serious use should difference against a placebo
category with no pandemic exposure.

## Limitations — read before citing anything

1. **ENIGH levels are not usable as totals.** ENIGH captures only **22–34% of
   GHED's out-of-pocket per capita** for Mexico, and independently sits ~3–4×
   below ENASEM's observed 50+ spending. Shapes and gradients are solid;
   levels need external benchmarking. Reported openly, not adjusted.
2. **Tier 3 profiles are estimates conditional on an allocation rule** — never
   observed data. The ages 5–14 cell is method-fragile (the regression turns
   negative there): do not quote it.
3. **The ENASEM frailty index is a reconstruction, provisional pending Judy.**
   Her construction code is not in the tree; only `mortality_enasem.tex`
   exists, which documents the convention (21 Searle-type deficits) but not
   the item list. My 21 items are itemized in `provenance.md`; her published
   checks reproduce qualitatively (median 0.095 vs 0.10; probit pseudo-R²
   0.167/0.192 full/women vs 0.142/0.159) but her exact sample (n=14,867,
   1,229 deaths) is not recoverable from the shipped files. Every figure using
   the index carries the provisional flag.
4. **The preventive share is an interval, not a number** (2%–46%); any
   sentence in the draft should say "majority curative" and cite the
   sensitivity table.
5. All profiles are **out-of-pocket only** — the IMSS/ISSSTE/SSA in-kind
   component is absent throughout, and every figure note says so.
6. Smaller: ENSANUT ships no self-rated health item in either wave; ENSANUT
   2018 has no wellbeing index (SES there = 4-stratum classifier, and its
   forgone-care gradient is non-monotone at stratum 4); ENASEM wealth is
   built from raw components without bracket imputation; ENIGH 2020 is
   pandemic-affected; the 2024 COICOP recode drops prescription status, which
   mechanically shifts items from ambiguous to curative relative to 2018.

## Where to find things on Dalila

Base: `~/Dalila/Missions/Funded/BID2/motivation/`
(committed on branch `p3-correcciones-tex`; raw microdata not committed but
re-downloadable from the URLs in `provenance.md`)

**The five graphs to look at first** (`output/figures/`, each as .png and .pdf):

| File | What it shows |
|---|---|
| `fig01_age_sex_profile.png` | Headline: age-sex OOP profile, both allocation methods, 2024 |
| `fig02_validation_enigh_vs_enasem.png` | The validation: ENIGH-estimated vs ENASEM-observed, 50+ — shape agrees, level ~3–4× apart |
| `fig06_forgone_care.png` (+ `fig06b`) | Direct unmet-need measurement by SES and by insurance, both waves |
| `fig07_composition.png` | Curative/ambiguous/preventive composition by decile, 2018 vs 2024 |
| `fig10_enasem_dynamics.png` | The mechanism: spending response to frailty decline and subsequent mortality, by wealth |

Also there: `fig03` (profile by income tercile), `fig04`/`fig05` (budget
share, zero-spending), `fig08` (catastrophic), `fig09` (right tail),
`fig11` (wave stability).

**Key tables** (`output/tables/`):
- `curative_preventive_classification.csv` — the auditable rubro mapping
  (145 codes, with rationale per code); `fig7_ambiguous_sensitivity.csv` is
  the two-way bracket.
- `enasem_probit_reproduction_check.csv` — the frailty-index check against
  Judy's published numbers.
- `verification_ghed_benchmark.csv` — the ENIGH/GHED capture ratios.
- Every figure has a matching `fig*_....csv` with its plotted values; the
  draft should cite `output/NUMBERS.md`, never values read off a figure.

Questions on the classification judgments (childbirth = curative, prenatal =
preventive, premiums = ambiguous, etc.): each code's rationale is in the
classification CSV, and the decision log is in `provenance.md`.
