# Briefing for Anne — demographic implications of the new health-spending age profiles

**From:** Héctor (analysis run on Dalila, 2026-08-08)
**Mission:** BID2 · health-refocused paper, motivation section
**Context:** the motivation build estimated individual age-sex profiles of
out-of-pocket (OOP) health spending for Mexico from ENIGH 2018–2024, with
ENSANUT-derived utilization weights and ENASEM validation. This note reads
those profiles demographically and runs one concrete experiment with **your**
2050 primitives. Full build: `motivation/output/READTHIS.md`.

---

## The estimated m_j, in demographic terms

The profile (fig 1, `output/figures/fig01_age_sex_profile.png`) is the
empirical counterpart of the model's $m_j$. Three features matter for the
demographic block:

1. **Steepness.** Quarterly OOP spending at 85+ is ~5–7× the young-adult
   level, rising monotonically from age 15 on. Two independent allocation
   methods agree (correlation 0.959 across 18 age-sex cells), and the shape —
   though not the level — validates against ENASEM's directly observed 50+
   spending. The gradient is real, not an allocation artifact.
2. **The sex pattern is age-dependent.** Women outspend men by a wide margin
   at ages 30–59 (reproductive and midlife care); the gap narrows after 65
   and flips male-ward at 85+ in the regression method. So aggregate health
   spending depends not just on how many old people there are, but on the
   *sex composition* of old age — which your ψ schedules govern: with your
   2050 sex gap (α_f = −0.696 vs α_m = −0.158), the oldest bands become
   increasingly female, weighting the aggregate toward the female profile.
3. **Stability.** The shape is essentially unchanged across ENIGH 2018–2024
   (fig 11), including through the pandemic wave. For comparative-statics use,
   treating m_j as a fixed primitive is empirically defensible over a 6-year
   window — with the endogeneity caveat below for anything longer.

There is also a within-profile inequality result you should know: the age
gradient is several times steeper for the top income tercile than the bottom
(fig 3). The poor do not have a flatter *need* profile — ENSANUT shows their
unmet need is highest — they have a flatter *spending* profile. In the
aggregate arithmetic below, that means population aging raises measured OOP
much more where resources permit a response.

## The experiment: your 2050 primitives × my 2024 profile

Pure composition, no behavior, no prices: hold the 2024 estimated age-sex
profile fixed and reweight from the observed ENIGH 2024 adult (20+) age
structure to the **stationary structure implied by your
`demographics_2050.jl`** (ψ_male/ψ_female Brass-2050, n_p_2050 = −0.4%/yr,
50/50 sex split at entry; J=17 bands, 20–24 … 100+).

| Quantity (adults 20+) | 2024 structure | Your 2050 stationary | Lift |
|---|---|---|---|
| Aggregate OOP per adult (quarterly, Aug–Nov 2024 pesos) | 580 | 854 | **×1.47** |
| Share of adults 65+ | 15.0% | 42.7% | ×2.85 |
| Share of OOP absorbed by 65+ | 30.7% | 66.4% | ×2.16 |

Script: `scripts/10_anne_composition.R`; tables
`output/tables/anne_composition_2050.csv` (+ `_detail.csv` per band × sex).

Internal consistency check you'll appreciate: the implied old-age ratio in my
calculation, 65+/(20–64) = 0.427/0.573 = **0.747**, reproduces the 0.744
stationary dependency ratio your file validates against the ECLAC 2× anchor —
so the two artifacts are speaking the same demographic language without any
tuning on my side.

Reading: **demographic composition alone raises per-adult OOP health spending
by ~47%**, and re-concentrates it — two-thirds of all OOP would be spent by
the 65+ under your 2050 stationary structure, up from a bit under a third
today. This is the motivation-section bridge from your dependency-ratio
doubling to the paper's health-financing question: the same aging that
doubles N^R/N^W shifts health financing onto exactly the ages where the
model's restoration mechanism (and its wealth gradient) bites.

## Limits of that number — read before quoting

- **Stationary upper bound, not a 2050 forecast.** Your file flags the
  stationary dependency ratio as the demographic-only upper bound; my ×1.47
  inherits that status. The 2050 *transitional* age pyramid is younger than
  the stationary one, so the true composition lift at 2050 is smaller. When
  you replace the Brass pipeline with WPP single-age life tables for the
  September three-country deliverable, the same script becomes a
  load-real-pyramid operation and gives the transitional number.
- **Fixed profile = no morbidity dynamics.** Healthy-aging / compression of
  morbidity would flatten m_j as longevity rises; expansion of morbidity
  would steepen it. This is the m_j analog of the caveat in your own header
  (the Brass shift preserves mortality shape); the two assumptions should be
  relaxed together if we ever do a serious projection.
- **The profile is not truly exogenous.** ENASEM shows spending responds to
  health decline about twice as strongly in the top wealth tercile (fig 10) —
  m_j partly reflects resources, not need. A composition calc holding m_j
  fixed embeds today's rationing.
- **OOP only, levels low.** ENIGH captures 22–34% of GHED OOP per capita
  (reported openly in `output/VERIFICATION.md`); the in-kind IMSS/ISSSTE/SSA
  component is absent. Ratios and shapes are the usable objects, never peso
  levels.
- 50/50 sex split at age 20 and cohort-invariant profiles are simplifications;
  cohort effects (education, insurance history) are not modeled.

## Two smaller items relevant to your desk

- **Gender frailty paradox, reproduced.** In the ENASEM reconstruction
  (provisional pending Judy — see her briefing), women carry more deficits
  than men at every age yet die less: mortality-probit pseudo-R² 0.192 women
  vs 0.137 men, same sign pattern as the published version. This is the
  morbidity-mortality asymmetry your sex-specific ψ schedules imply, visible
  in the microdata that feed m_j.
- **ENSANUT-derived utilization weights** (`output/tables/
  ensanut_util_weights_2024.csv`) are an age-sex utilization schedule in
  their own right — attended-care rates by 5-cell age groups and sex, rising
  from ~14% (boys 5–14) to ~50% (women 75–84), women above men at every
  adult age. If you ever want an NTA-style health-utilization profile as a
  demographic input, it exists and is design-based.

## Where everything lives on Dalila

Base: `~/Dalila/Missions/Funded/BID2/motivation/` (branch `p3-correcciones-tex`)

- The profiles: `output/figures/fig01_age_sex_profile.png` (headline),
  `fig03_profile_by_income.png` (tercile-specific gradients),
  `fig11_wave_stability.png` (stability), with plotted values in
  `output/tables/fig1_*.csv`, `fig3_*.csv`, `fig11_*.csv`.
- The composition experiment: `scripts/10_anne_composition.R`,
  `output/tables/anne_composition_2050.csv`.
- Your primitives, used verbatim: `GE-now with Gender/demographic_experiment/
  demographics_2050.jl`.
- Validation and caveats: `output/VERIFICATION.md`, `output/READTHIS.md`.
