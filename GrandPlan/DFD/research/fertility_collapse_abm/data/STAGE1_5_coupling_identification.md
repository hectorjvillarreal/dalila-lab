# Stage 1.5 — Coupling Microdata Acquisition and Identification Forensics
# Project: Rapid Fertility Collapse in Latin America (ABM paper, DFD parallel research)
# Author: Nina (ABM lead) and Anne (population economics), DFD Core Team
# Date: 2026-06-18
# For: Claude Code on Dalila (work already in progress)
# Location: GrandPlan/DFD/research/fertility_collapse_abm/data/coupling/

---

## Why this stage exists

The Stage 1 forensic memo established that the fertility collapse is behavioral in all
four countries, and that the ASFR decline is **tempo-dominant** — concentrated in ages
under 30 (83% in Mexico, 72% in Argentina). This finding does not refute the
threshold-coupling thesis; it sharpens it. If the collapse is socially-reinforced
postponement of partnership and first birth, then the **annual coupling time-path is
not merely a priority input — it is the dependent phenomenon the ABM exists to explain.**

Stage 1 found coupling data at endpoints only. Stage 1.5 acquires the annual path from
household-survey microdata and — critically — determines whether that path can
*identify* the model before Nina invests in the ABM build. This is a gate, not a
build. The question Stage 1.5 answers is binary: **is the central mechanism
identifiable from the available data, yes or no?**

---

## Target series — the precise object

For each country, construct the longest possible **annual** series of:

**Primary:** Share of women aged 20–39 currently in a co-residential union
(married OR cohabiting), by single year.

**Why 20–39 and not 15–49:** the mechanism is partnership formation among
prime-entry cohorts. The 15–19 tail adds noise (few unions, measurement
sensitivity) and the 40–49 tail adds inertia (mostly stable existing unions).
The 20–39 window is where the postponement cascade, if it exists, will show.

**Disaggregations required (not optional):**
- By 5-year age band: 20–24, 25–29, 30–34, 35–39. The cascade hypothesis makes a
  specific prediction — the decline should appear *first and largest in 20–24*, then
  propagate to older bands with a lag. Without the age bands we cannot test this.
- Married vs. cohabiting separately. LAC has high and rising cohabitation; the
  marriage-to-cohabitation substitution (documented for Mexico in Stage 1: casada
  34.2→28.5, unión libre 23.3→24.8) must not be allowed to masquerade as a coupling
  decline. The ABM cares about *any* co-residential union, but we must see the
  composition to interpret the total.

**Country sources (microdata):**
- Colombia: GEIH (continuous, monthly→annual), ENDS (2005, 2010, 2015, 2025)
- Argentina: EPH (continuous urban, quarterly→annual)
- Chile: CASEN (2006, 2009, 2011, 2013, 2015, 2017, 2020, 2022)
- Costa Rica: ENAHO (continuous, annual since 2010)
- Mexico: ENADID (2014, 2018, 2023) + ENOE (continuous, for annual interpolation)

---

## The identification questions — Stage 1.5's actual deliverable

The data is a means. These four questions are the end. The Stage 1.5 memo must answer
each one explicitly, because each one determines whether Stage 2 can proceed.

### Q1 — Does the coupling path lead the TFR path?
Plot annual coupling share (20–39) against TFR for each country on a common timeline.
The threshold mechanism predicts coupling turns down *before* TFR. If coupling and TFR
fall simultaneously, the "coupling drives fertility" causal story is weaker and the
model needs a different state variable. **If coupling lags TFR, the thesis is in
serious trouble and we need to know now.**

### Q2 — Is the decline velocity nonlinear?
The whole premise is that a threshold produces a *sudden* collapse, not a gradual
glide. Compute the year-over-year change in coupling share. Is there an inflection —
a year where the rate of decline sharply accelerates — or is it a smooth linear
drift? A smooth drift in coupling that maps to a sudden TFR collapse would imply the
nonlinearity is in the coupling→fertility map, not in coupling itself. A sudden drop
in coupling itself would imply the threshold is in partnership formation. **These are
two different models. The data decides which one we build.**

### Q3 — Does the age-band propagation match the cascade prediction?
Under the cascade hypothesis, the decline starts in 20–24 (entry cohort), then 25–29,
then older. Check whether the timing of the inflection in each age band is ordered
youngest-first. If all bands turn down simultaneously, it is an aggregate shock, not
a propagating cascade — again, a different model.

### Q4 — Is there enough independent variation to calibrate without circularity?
The identification discipline requires calibrating the ABM to coupling and covariate
data, then matching TFR as an *output*. For this to be non-circular, the coupling
series must be measured *independently* of the fertility series — not derived from the
same vital registration. Confirm the microdata coupling measure is survey-based
(household roster) and not back-derived from birth records. **If coupling is
contaminated by the fertility data, the identification collapses.**

---

## Forensic checks (same discipline as Stage 1)

- **Survey comparability over time:** household survey definitions of "union" change.
  Flag any redefinition of marital/union status categories across waves. EPH and CASEN
  have known questionnaire revisions.
- **Geographic coverage:** EPH is urban-only (31 agglomerations). Flag that Argentina's
  coupling series is not nationally representative and assess whether the urban
  restriction biases the level or the trend.
- **Interpolation honesty:** CASEN and ENADID are periodic, not annual. Where annual
  values are interpolated between waves, mark interpolated points distinctly from
  observed points. Never present interpolated values as observations.
- **Cohabitation measurement:** informal unions are systematically under-measured in
  older waves. If measurement improved over time, a *rising* measured cohabitation
  could mask a *falling* true union rate, or vice versa. Assess direction.

---

## Deliverables

Under `GrandPlan/DFD/research/fertility_collapse_abm/data/coupling/`:

1. **Annual coupling CSVs** — one per country: `{ISO}_coupling_annual.csv` with columns
   `year`, `age_band`, `union_total`, `married`, `cohabiting`, `observed_or_interpolated`,
   `source`, `coverage_flag`. PROTO-RAG-001 sidecar or provenance entry per Debb's rule.

2. **Identification memo** — `STAGE1_5_identification_memo.md` — the primary deliverable.
   One section per country, then a cross-country synthesis that answers Q1–Q4 with a
   clear verdict: **IDENTIFIABLE / PARTIALLY IDENTIFIABLE / NOT IDENTIFIABLE** for each
   country, and an overall recommendation on whether Stage 2 proceeds.

3. **Lead-lag and velocity charts** — coupling vs. TFR on a common timeline per country,
   plus the year-over-year velocity panel. These are the visual evidence for Q1 and Q2.

---

## The gate — what Nina needs to hear

Stage 1.5 succeeds if it can state, for at least two of the four collapse countries:

> "The annual coupling path is measured independently, it leads the TFR decline, the
> decline has a nonlinear inflection, and there is enough variation to calibrate the
> threshold without circularity."

If that statement holds for two or more countries, Nina freezes the Stage 2 ABM spec
with confidence. If it holds for fewer, we have a decision to make before building:
narrow the paper to the identifiable cases, or reconsider whether the mechanism is
the right one. **Either way, we learn it before the model is built, not after.**

---

## One open question for Héctor (does not block the work)

If the annual coupling path turns out to be cleanly identifiable in only one country
(say Costa Rica, the cleanest signal), do you want the paper to (a) become a deep
single-country case study with the others as supporting context, or (b) hold for
broader cross-country identification even if that delays it? Nina's lean: a clean
single-country mechanism paper is more valuable than a four-country paper with weak
identification. But that is a strategic call, not a methodological one — yours and
Fina's to make.

---

*Stage 1.5 of 4. Version 1.0, 2026-06-18.*
*Gate: identification memo reviewed by Anne and Nina before Stage 2 ABM spec is frozen.*
