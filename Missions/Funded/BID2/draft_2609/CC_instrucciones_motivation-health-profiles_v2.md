# Claude Code — Motivation figures: Mexican health expenditure by sex, income, and age (multi-source)

**Mission:** BID2 · **Purpose:** motivation section of the health-refocused paper
**Working folder (create):** `~/Dalila/Missions/Funded/BID2/motivation/`
**Supersedes:** `CC_instrucciones_motivation-health-profiles_v1.md` (ENIGH-only)

## What this is for

The paper is being repositioned so that health is the analytical center rather
than one fiscal pressure among several. The motivation section must establish
three empirical facts, because each is a premise the model later formalizes:

1. Health spending has a steep **age gradient** and differs by **sex** — the
   empirical counterpart of the model's $m_j$.
2. The capacity to spend on health is **sharply unequal by income** — the
   premise behind the paper's inequality mechanism.
3. Observed spending is overwhelmingly **curative rather than preventive** —
   it responds to a realized health shock rather than smoothly accumulating a
   health stock. This is the central interpretive claim of the new draft.

Fact 3 has a corollary that is probably the most valuable result available here:
**low health spending among poor households may indicate unmet need, not good
health.** Test it directly; do not infer it.

Do not tune the analysis toward these expectations. Which of these holds
determines the model's specification, so a null result is genuinely informative
and must be reported plainly rather than smoothed over.

---

## Division of labor across sources

No single survey answers the question. Each source is strong exactly where the
others are weak, and the triangulation is itself part of the contribution.

**ENIGH** (2018, 2020, 2022, 2024) — *the money and its distribution.*
Out-of-pocket expenditure, household income deciles, budget shares, catastrophic
spending. Strongest source for the inequality claims. Weak on age (household
level) and silent on health status.

**ENSANUT** — *individuals, health status, utilization, and unmet need.*
Individual-level records with age, sex, insurance affiliation, self-reported
health, chronic conditions, and utilization by type of service. Critically, it
carries **direct questions on forgone or delayed care and the reasons for it**,
including cost. This converts the unmet-need corollary from an inference into a
measurement. It also supports the preventive/curative split at the level of
*service used* rather than *rubro purchased*, which is a cleaner classification
than ENIGH's expenditure codes.

**ENASEM / MHAS** — *the dynamics, for ages 50+.* A longitudinal panel with
individual-level health status, functional limitation, out-of-pocket spending,
insurance, wealth, and mortality follow-up. This is the only source that can
observe the sequence the model describes: health declines between waves,
spending responds (or does not), and health and survival at the next wave
follow. **This is the direct test of the restorative-spending mechanism.**

Coordinate with Judy's existing ENASEM work rather than rebuilding it. Her
frailty–mortality probit already constructs a deficit-accumulation frailty index
on ENASEM 2018–2024; reuse that index construction and cite it, do not
re-derive a competing one. Reconcile any difference explicitly.

**If the index construction is not available, do not block.** Its availability
in the tree is uncertain — the write-up `mortality_enasem.tex` exists under the
BID2 data folder, but the underlying code may not. Work down this ladder and
record in `provenance.md` which rung was used:

1. Search the BID2 tree for the construction (scripts, `.do`, `.R`, `.jl`, or a
   saved index variable). If found, use it unchanged.
2. If only `mortality_enasem.tex` is present, reconstruct the index from the
   specification documented there — the deficit list, the coding of each
   deficit, and the normalization — and reproduce the reported pseudo-$R^2$
   (0.14 full sample, 0.16 for women) as a check. State whether the check
   passed.
3. If neither is usable, build a standard deficit-accumulation index (share of
   available health-deficit items present, following the Mitnitski–Rockwood
   convention), document every item included, and **flag the index as
   provisional pending Judy's confirmation** in `provenance.md`, in
   `READTHIS.md`, and in the note of every figure that uses it.

Under rungs 2 and 3, the index is a reconstruction rather than Judy's estimate,
and any figure using it carries that qualification until she confirms it. Do not
present a reconstructed index as her result. Task C's qualitative pattern —
whether spending responds to health decline and whether the response differs by
wealth — should be robust to the exact index construction; if it is not, that
fragility is itself worth reporting.

Optional if time permits: SHA / Cuentas en Salud or GHED for the public-spending
benchmark. ENIGH and ENASEM capture out-of-pocket only, so none of these
profiles describe total health resources by age — the IMSS/ISSSTE in-kind
component is missing throughout and every figure note must say so.

---

## The three analytical tasks

### Task A — Age and sex profile of health spending

The obstacle is that ENIGH records expenditure at the **household** level while
the profile the paper needs is **individual**. This gap cannot be closed by
assumption. Work in tiers and keep them visibly separate.

- *Tier 1 (ENIGH, household).* Household health expenditure and budget share by
  income decile and by household composition (no member 65+, one, two or more;
  similarly for children). No allocation assumption. Carries the main inequality
  claims.
- *Tier 2 (ENIGH, per capita / adult equivalent).* State the equivalence scale.
- *Tier 3 (ENIGH, estimated individual profile).* Two independent methods —
  (i) regression of household expenditure on counts of members in each age-sex
  cell, reporting coefficients with confidence intervals; (ii) NTA-style
  allocation using age-sex utilization weights. **Derive the weights from
  ENSANUT utilization rather than importing published weights**, and record the
  derivation. Agreement between the two methods is itself the evidence that the
  profile is real; disagreement must be reported, not averaged away.
- *Validation (ENASEM, ages 50+).* ENASEM observes individual out-of-pocket
  spending directly. Compare the ENIGH Tier 3 estimated profile against the
  ENASEM observed profile over the overlapping age range. **This is the single
  most valuable check in the whole exercise:** it tells the reader whether the
  allocation rule recovers something real. Report the comparison as a figure and
  state the agreement or disagreement in plain terms.

Tier 3 results are estimates conditional on an allocation rule and every figure
and note must say so. Never present a Tier 3 profile as observed data.

### Task B — Curative versus preventive

The analytically important classification and the most fragile, so treat it as a
stated, auditable judgment rather than a neutral data operation.

*In ENIGH,* build the classification from the rubro descriptors: curative covers
consultations for illness, hospitalization, surgery, emergency care, prescribed
medicines; preventive covers check-ups, screening, vaccination, dental cleaning.
Many rubros are genuinely ambiguous — over-the-counter medicines, optical,
dental, chronic-disease maintenance.

*In ENSANUT,* classify by **type of service used and its stated motive**, which
is a cleaner split than expenditure rubros because the survey distinguishes
care sought for illness from preventive visits and screening. Where the two
sources disagree about the preventive share, that disagreement is a finding
about measurement and should be reported.

Requirements:
- Write the full mapping (every code → curative / preventive / ambiguous, for
  each source) to `output/tables/curative_preventive_classification.csv`. This
  file is the auditable object; the figures are downstream of it.
- Keep "ambiguous" as its own category. Do not force a binary.
- Run the composition figures **twice**, assigning ambiguous items to curative
  and then to preventive, and report whether the qualitative conclusion changes.
  If it does, say so prominently — that is a real finding about the data's
  limits and more useful than a clean figure resting on a coin flip.
- If a source or wave cannot support a defensible split, say so and omit that
  figure. A missing figure is recoverable; a misleading classification presented
  as fact is not.

### Task C — Unmet need and the restoration constraint

Three independent lines of evidence, and they should be presented together
because each alone is contestable.

- *ENIGH (indirect).* Share of households reporting **zero** health expenditure
  by income decile, split by whether the household contains a member 65+. Excess
  mass at zero among poor households with older members is consistent with
  constrained restoration.
- *ENSANUT (direct).* Prevalence of forgone or delayed care, and the share of
  those citing **cost** as the reason, by income group, insurance status, age,
  and sex. This is the measurement that the ENIGH pattern only implies.
- *ENASEM (dynamic).* Following a health decline between waves — use Judy's
  frailty index or an equivalent transition measure — does out-of-pocket
  spending respond, and does the response differ across the wealth
  distribution? Then: conditional on a comparable decline, do subsequent health
  status and survival differ by wealth? This is the mechanism the model
  formalizes, observed directly.

On the ENASEM analysis: report it as **descriptive conditional patterns, not
causal estimates.** Wealth correlates with insurance, education, prior health,
and access, none of which are controlled by a panel difference. Say this in the
text and in the figure note. The descriptive pattern is enough to motivate a
model; an unearned causal claim in front of the IDB Fiscal Division is not worth
the exposure.

---

## Figures

English labels (the draft is in English), 300 dpi `.png` plus `.pdf`,
colorblind-safe palette, weighted estimates with design-based or bootstrapped
uncertainty, and a note on every figure stating source, wave, tier, deflator,
and allocation assumption where one applies.

1. Age profile of per-capita OOP health spending by sex (ENIGH Tier 3, both
   allocation methods shown). Headline motivation figure.
2. **ENIGH Tier 3 versus ENASEM observed profile, ages 50+.** The validation
   figure described in Task A.
3. Age profile by income group (ENIGH Tier 3, terciles or quintiles). Whether
   the profiles diverge only in old age or throughout is itself the finding.
4. Health budget share by income decile (ENIGH Tier 1), unconditional mean and
   mean conditional on positive spending shown together.
5. Zero health expenditure by decile, split by presence of a member 65+
   (ENIGH Tier 1).
6. **Forgone care and cost-related forgone care, by income group and insurance
   status** (ENSANUT). The direct unmet-need figure.
7. Curative / preventive / ambiguous composition by income decile (ENIGH), and
   by age where Tier 3 supports it; alongside the ENSANUT service-type split.
8. Catastrophic health expenditure incidence by decile (ENIGH Tier 1), WHO
   capacity-to-pay definition, with sensitivity to at least one alternative
   threshold.
9. Distribution of positive health spending by decile (ENIGH Tier 1) — the right
   tail is the shock-response object, so show the distribution, not only means.
10. **ENASEM: spending response to health decline, by wealth tercile**, and the
    subsequent health/survival gradient. The dynamic figure.
11. Stability across ENIGH waves for figure 1 or 3. Flag 2020 as
    pandemic-affected in every note rather than dropping it silently.

---

## Data handling rules

Obtain microdata from the official portals (INEGI for ENIGH and ENSANUT; the
ENASEM/MHAS project site for ENASEM). **Verify URLs by navigating the sites
rather than constructing paths from memory** — these get reorganized between
waves. Record the exact URL and access date for every file. If a source cannot
be downloaded, record the failure and proceed with what succeeded rather than
blocking.

**Do not hardcode variable names or codes from memory for any of the three
surveys.** Read the descriptor and codebook files shipped with each wave, select
variables programmatically, and write the resulting code lists into
`provenance.md` so the selection is auditable.

Each survey has its own complex sample design — use the design variables
supplied with each (strata, PSU, weights) and estimate accordingly. ENASEM
additionally requires attention to panel attrition; report attrition and whether
it correlates with health and wealth, since differential attrition by health is
exactly the dimension that would bias Task C.

Deflate ENIGH and ENASEM monetary values to a common base year with the INPC,
stating whether the general or health-specific subindex was used.

---

## Outputs

```
~/Dalila/Missions/Funded/BID2/motivation/
  data/                  # raw downloads (not committed)
  scripts/               # numbered, re-runnable, one per source plus a merge step
  output/figures/        # .png and .pdf
  output/tables/         # classification CSV and the plotted values for every figure
  output/NUMBERS.md      # every number appearing in any figure, with source
  provenance.md          # sources, URLs, access dates, code lists, decisions
  output/READTHIS.md     # prose summary, written last
```

Language: **R** (`survey` / `srvyr` for design-based estimation, `ggplot2` for
figures), consistent with team convention. Python is acceptable if R is
unavailable; note the choice in `provenance.md`.

Every figure needs a machine-readable table of its plotted values. The draft
cites `NUMBERS.md`, never values read off a figure.

---

## Verification

1. ENIGH weighted health expenditure totals reconcile in order of magnitude with
   an external benchmark (GHED OOP for México, or SHA). ENIGH is expected to
   **under**capture — report the ratio openly rather than adjusting silently. If
   it is wildly off, stop and report.
2. The ENIGH Tier 3 profile and the ENASEM observed profile are compared over
   the overlapping ages, with the result stated plainly either way.
3. The two Tier 3 allocation methods are compared; material disagreement is
   reported, not averaged.
4. ENSANUT and ENIGH preventive shares are compared; disagreement is reported.
5. ENASEM attrition is quantified and its correlation with health and wealth
   reported.
6. Every figure has its table, its note, and entries in `NUMBERS.md`.
7. Scripts re-run end to end from a clean directory.

## Report back

Write `output/READTHIS.md` in prose covering: what the data show for each of the
three facts; whether the unmet-need pattern appears in each of the three
independent lines of evidence and whether they agree; how much the
curative/preventive conclusion depends on the ambiguous-item assignment; whether
the ENIGH-estimated age profile survives validation against ENASEM; and which
claims are robust versus allocation-dependent. Be direct about what did not
work. This file is read first.

## Commit

Commit scripts, tables, figures, `NUMBERS.md`, `provenance.md`, and
`READTHIS.md`. Do not commit raw microdata.
