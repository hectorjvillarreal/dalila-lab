# READ THIS FIRST — BID2 motivation: health expenditure by sex, income, and age

Written 2026-08-08, after all scripts ran end to end. Build instruction:
`draft_2609/CC_instrucciones_motivation-health-profiles_v2.md`. Figures are in
`output/figures/`, every plotted value in `output/NUMBERS.md` and
`output/tables/`; sources and decisions in `provenance.md`; cross-source checks
in `output/VERIFICATION.md`.

## The three facts, as the data show them

**Fact 1 — age gradient and sex differences: strongly supported.**
Estimated individual OOP health spending rises monotonically from adolescence
to the oldest ages; the 85+ level is roughly five to seven times the
young-adult level (fig 1). Women spend more than men through the reproductive
and midlife years (30–59); the sex gap narrows or reverses at the oldest ages
depending on method. The two independent allocation methods — household
regression on age-sex composition, and NTA-style allocation with
ENSANUT-derived utilization weights — agree closely (correlation 0.959 across
the 18 age-sex cells in 2024) everywhere except ages 5–14, where the
regression turns slightly negative while the allocation stays positive; that
cell is method-fragile and should not be quoted. The profile shape is stable
across all four ENIGH waves (fig 11; 2020 is pandemic-marked and flagged).
This is the empirical counterpart of the model's $m_j$.

**Fact 2 — unequal capacity to spend: strongly supported.**
The budget share of health is roughly flat across deciles *unconditionally*,
but that flatness is an artifact of zeros: poor households are far more likely
to spend nothing at all (fig 5), and conditional on spending, their share of
the budget is higher (fig 4). Catastrophic spending (WHO capacity-to-pay,
40%) falls from ~4–5% of households in the poorest deciles to ~1% in the
richest, robust to the 25%-of-total threshold (fig 8). The age gradient
itself is much steeper for richer households: in the top income tercile the
old-age spending level is several times the bottom tercile's (fig 3) — the
inequality premise, visible inside the age profile.

**Fact 3 — curative dominance: supported, with an honest bracket.**
Under the stated classification (every rubro mapped in
`output/tables/curative_preventive_classification.csv`), unambiguously
preventive items are ~2% of OOP health spending in every wave and every
decile; unambiguously curative items are 52–66%; the remaining 38–44% is
genuinely ambiguous (OTC medicines, dental, optical, chronic-disease
maintenance, unqualified diagnostics, insurance premiums). Assigning all
ambiguous spending to preventive still leaves curative the majority; assigning
it to curative makes spending ~98% curative. So: **"majority curative" is
robust to the coin flip; "overwhelmingly curative" holds under the base and
curative-leaning assignments only** (fig 7 + sensitivity table). ENSANUT 2024,
which observes the *motive* of the last health need directly, gives a
consistent picture: preventive motives (vaccination, check-up, prenatal
control) are a minority of needs and *decline* toward the poorest wellbeing
tercile. The 2018 ENSANUT utilizadores module conditions on illness and cannot
yield a preventive share at all — an instructive measurement asymmetry, noted
rather than smoothed. Note also a scheme discontinuity: the 2024 COICOP rubros
drop prescription status, so items the 2018 scheme could identify as prescribed
(and therefore classify as curative) become unidentifiable and fall into the
ambiguous block, which grows from 38.0% of OOP spending in 2018 to 44.5% in
2024 (`fig7_ambiguous_sensitivity.csv`). The curative/preventive split is
therefore **not comparable across waves**; quote the composition
cross-sectionally only.

## The corollary — low spending among the poor is unmet need, not good health

All three planned lines agree — and a fourth, unplanned one emerged from the
2020 wave (see below).

1. *ENIGH (indirect):* zero health spending is concentrated in poor
   households and remains elevated there even when the household contains a
   member 65+ (fig 5).
2. *ENSANUT (direct):* among people with a health need, forgone care runs
   ~19% in the poorest wellbeing tercile vs ~9% in the richest (2024), and
   *cost-attributed* forgone care collapses from ~3.5% to ~0.1% across the
   same gradient; the uninsured are worst off on both (figs 6, 6b). The 2018
   12-month cost battery shows the same shape. Cost-related unmet need is a
   measured fact here, not an inference.
3. *ENASEM (dynamic):* following a frailty increase between 2018 and 2021,
   out-of-pocket spending responds in every wealth tercile, but the response
   roughly doubles from the bottom to the top tercile (~24k vs ~42k pesos in
   2021; fig 10 left). Conditional on a comparable decline, death by 2024 is
   ~17–20% in the lower two terciles vs ~10.5% in the top (fig 10 right) —
   with the caveat that the tercile-1 vs tercile-2 ordering is not monotone
   and the confidence intervals are wide. Descriptive, not causal, and labeled
   as such everywhere.

**A fourth line, found along the way (fig 12).** The pandemic wave is itself
evidence. Real household OOP health spending jumped between 2018 and 2020 in
*every* decile — +76% in the poorest, +29% in the richest — while food
spending (the placebo) was flat to negative everywhere, and the shift never
reversed in 2022–2024. The margin was participation, not intensity: the share
of households spending zero on health fell 13–15 pp in every decile, while
conditional-on-positive amounts rose far less (+36% bottom decile, +7.5%
top). When the free public option failed, the zeros emptied out — poor
households were conscripted into out-of-pocket payment, not priced out of
responding. In peso terms the top two deciles still financed 36% of the
aggregate jump (growth rates and contributions tell opposite stories; quote
both or neither). This is time-series support for the cross-sectional
identification in fig 5: the zeros among poor households encode access to
in-kind provision plus unmet need, because they collapsed the moment public
provision did. Caveat: two waves and one placebo cannot fully exclude a
health-specific reporting change in ENIGH 2020 (the same J-code instrument
was used in both waves, which helps); keep causal language soft.
Table: `pandemic_jump_by_decile.csv`.

## Validation of the estimated profile (the single most valuable check)

The ENIGH Tier 3 profile and the ENASEM observed profile **agree on shape and
disagree on level** (fig 2). Both rise with age over 50+; ENASEM levels are
roughly 3–4× the ENIGH-based estimates. This is coherent with the external
benchmark: ENIGH's weighted health spending is only **22–34% of GHED's
out-of-pocket per capita** for Mexico (ratio 0.22 in 2018, 0.31–0.34 in
2020–2024; `verification_ghed_benchmark.csv`). Two independent comparisons
point at the same conclusion: **use ENIGH for shapes and distributional
gradients; do not use its levels as totals without benchmarking.** The ENASEM
side has its own upward-leaning quirks (a normal-month medication amount
×12 dominates its total), so truth is likely between the two.

## The frailty index (Judy's) — rung 2/3 of the ladder

No construction code exists in the BID2 tree; only `mortality_enasem.tex`.
That write-up documents the convention (21 deficits over five categories,
Searle 2008 / Hosseini 2021) but **not the itemized deficit list**, so the
index built here is a reconstruction: 5 ADL + 4 IADL + 2 mental (CES-D 5+
symptoms, poor self-rated memory) + 8 diagnoses + obesity (BMI≥30 from
self-reported height/weight) + current smoking, itemized in `provenance.md`.
The published checks reproduce *qualitatively*: median frailty 0.095 vs
published p50 0.10; probit pseudo-R² 0.167 full / 0.137 men / 0.192 women vs
published 0.142 / 0.118 / 0.159 — same ordering, same sign pattern, similar
coefficients — but my estimation sample is larger (16,702 vs 14,867; 1,525 vs
1,229 deaths) and neither of two candidate restrictions reproduces her counts
exactly. **The check passed qualitatively, not numerically. The index is
provisional pending Judy's confirmation**, and every figure using it says so.
Reassuringly, the Task C pattern (spending response and survival gradients by
wealth) does not hinge on fine index details — the decline threshold (0.10) is
a full decile of the index range.

## Robust vs. allocation-dependent claims

Robust (Tier 1, no assumptions): budget-share and zero-spending gradients,
catastrophic incidence, right-tail distribution (fig 9), the ENSANUT
forgone-care gradients, the ENASEM dynamic patterns.
Conditional on an allocation rule (Tier 3, both methods agreeing): the
age-sex profile shape, the tercile-specific age gradients. Never quote Tier 3
levels as observed data, and never quote the 5–14 cell.
Assignment-dependent: the precise preventive share (2%–46% bracket).

## What did not work / gaps to know about

- **ENIGH levels** undercapture health spending by ~3× vs GHED (reported, not
  adjusted).
- **Self-rated health does not exist** in the shipped ENSANUT files of either
  wave — a planned crosswalk variable that simply is not there.
- **2018 ENSANUT has no wellbeing index**; SES gradients for 2018 use the
  survey's sociodemographic stratum (1–4), which is coarser, and the 2018
  forgone-any gradient is non-monotone at stratum 4 (report as is).
- **ENASEM wealth** is assembled from raw J/K components (no constructed
  net-worth variable ships); bracket follow-ups for NR/NS amounts were not
  interval-imputed in this pass — wealth terciles are based on point amounts
  (~60% of households report enough components).
- **2020 ENIGH** is pandemic-affected and flagged in every note that uses it —
  though the disruption is also informative in its own right (fig 12 and the
  fourth evidence line above).
- The ENIGH↔ENASEM level gap means fig 2 validates shape only; that is stated
  on the figure itself.

## Reproducibility

`scripts/00–09` run end to end with R 4.4.3 (conda env `renv`); raw microdata
in `data/` (not committed) re-download from the URLs in `provenance.md`.
Every figure's plotted values: `output/NUMBERS.md`.
