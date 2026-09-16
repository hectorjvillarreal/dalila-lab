# DFD Demographic Forecasting — Claude Code Instructions
# TFR Scenario Discipline and Quarterly Replication Protocol — MEXICO
# Author: Héctor / Anne (DFD Core Team)
# Date: 2026-05-19
# Location: _crossrefs/corpus/demographics/country/MEX/

---

## Scope

**Current scope: México only.** All work governed by these instructions is
restricted to Mexico and lives in this folder
(`_crossrefs/corpus/demographics/country/MEX/`). Costa Rica, Panamá, and other
LAC calibration countries will be added in subsequent versions of this document
once the Mexico replicate is stable. The analytical framework below is written
generically where useful for future extension, but all current outputs target
Mexico exclusively.

---

## Purpose

These instructions govern how Claude Code constructs and updates TFR-based demographic
forecasts for **México**. They encode the scenario discipline established by the
Core Team in May 2026, including the explicit rejection of the CELADE medium-variant
as a central scenario and the analytical resolution of the tempo-correction debate
with respect to LAC countries.

All forecasts produced under these instructions feed directly into:
- IM-6 demographic block (cohort weights, survival probabilities, dependency ratio path)
- NTA layer age profile updates
- Mechanical fiscal simulator dependency ratio inputs

---

## Standing Analytical Considerations

Before constructing any forecast, Claude Code must apply the following considerations.
These are not optional checks — they are constitutive of what a DFD forecast is.

### 1. Period TFR vs. Completed Cohort Fertility

The period TFR (TFR by year) and completed cohort fertility (by birth year of woman)
are distinct measures and must not be conflated.

- **Period TFR** is a synthetic measure: it aggregates age-specific fertility rates
  observed in a single calendar year across all cohorts present. It is sensitive to
  tempo effects — postponement of births compresses the period TFR below the level
  that cohorts will ultimately complete.
- **Completed cohort fertility** measures the actual average number of children born
  to women who have finished their reproductive years (~age 45). It is smoother and
  typically higher than period TFR troughs.

**Fischer-Dattani caution (registered May 2026):** The very low period TFR values
observed in LAC in 2024–2026 (Mexico ~1.55, Costa Rica ~1.12, Colombia ~1.06,
Chile ~1.03) partly reflect collapse of fertility among the youngest age cohorts
(15–25 years). Completed fertility for these cohorts will likely be higher than
current period TFR implies. This must be acknowledged in any forecast documentation.

**However — DFD position (Héctor, May 2026):** The tempo-correction argument does
not materially alter the fast-transition scenario for LAC for three reasons:

1. **Coupling rate collapse.** Falling partnership formation rates in Mexico, Peru,
   Colombia, and other LAC countries (FT data, 2024) imply permanent fertility loss,
   not postponement. Postponement assumes partnerships eventually form; a falling
   coupling rate implies a fraction never form.

2. **Overshooting dynamic.** Middle- and low-income LAC countries are transitioning
   faster than advanced economies and overshooting them in fertility decline
   (Fernández-Villaverde 2026). This is not a tempo effect — older cohorts in these
   countries already completed at low levels.

3. **No reversal signal in structural drivers.** Socialization collapse among 15–29
   year-olds (US, UK, Europe, South Korea — FT data, 2024), housing costs, and
   education opportunity costs show no reversal trend. A tempo recovery at scale
   would require structural conditions not currently in evidence. Something really
   strange would be needed.

**Conclusion for forecasting:** Period TFR is the correct input for the DFD baseline
and fast-transition scenarios. Completed cohort fertility adjustments may be explored
as a sensitivity scenario but must not replace the period TFR-based central scenario.

---

### 2. CELADE Medium-Variant is the Optimistic Scenario

The UN WPP and CELADE medium-variant projections assume a fertility rebound for
low-fertility countries, justified by expected gender equality progress and improved
economic conditions for young families (WPP 2024, Box II.1). This justification is
not empirically grounded for LAC in the current context.

**DFD rule:** CELADE medium-variant = optimistic scenario, not central scenario.

The fast-transition scenario — anchored to observed 2024 TFR values and the
coupling rate decline — is the DFD central scenario.

**Four-scenario structure for Mexico forecasts:**

| Scenario | TFR anchor — Mexico | Status | Rationale |
|----------|---------------------|--------|-----------|
| Optimistic | CELADE medium-variant (TFR ≈ 1.6→1.7) | operational | Fertility stabilization and partial rebound |
| **Central (fast-transition)** | **TFR = 1.5, stable from ~2026** | **operational (baseline)** | Structural drivers unabated; coupling rate decline embedded |
| Tempo-corrected | TFR = 1.6 stable (Central + 0.10 Fischer-Dattani lift) | reported, not operational | Defensive sensitivity against the period-TFR-vs-completed-cohort objection (see §1) |
| Stress | TFR → 0.9 by 2031, stable thereafter | operational | Overshooting accelerates; **the empirical floor is declared unidentified** — 0.9 is a working value, not an observed minimum (Héctor ruling 2026-09-15, Anne option (b)) |

**Central scenario note (Mexico):** TFR = 1.5 stable is the DFD central scenario,
confirmed by the 2026-Q2 replicate. It implies a Mexico population of **140.4 M
by 2050** — 4.2 M below the optimistic (TFR=1.65 UN-like) approximation. The
dominant driver of the gap is TFR, not mortality or migration assumptions.

**Tempo-corrected scenario note:** TFR = 1.60 stable approximates the
Fischer-Dattani correction (+0.10 on Central) for completed cohort fertility.
2026-Q2 replicate gives **143.2 M by 2050** — a +2.79 M (+2.0%) lift over
Central. Reported defensively against the most likely reviewer objection;
not promoted to operational. Promotion conditions: Mexico-specific Fischer-
Dattani correction > +0.15, or ENOE evidence of coupling-rate stabilization
(see standing considerations §1).

**Stress scenario note (revised v1.5):** TFR → 0.9 by 2031 is a stress scenario,
not a forecast.

**The empirical floor is declared unidentified.** Earlier versions anchored the
stress path to Chile 1.03 (2024) as the observed LAC minimum. That anchor no
longer holds: the September 2026 registry table puts Chile at **0.99 (2025)**,
down from 1.54 in 2018, and the cornerstone paper documents WPP projecting a
*recovery* to 1.12 by 2028 against that fall. Rather than chase the observed
minimum downward each time a registry prints — which would make the stress
column a moving function of the latest release — the floor is stated as
**unknown**, the *terra incognita* position, and **0.9 is carried as a working
value**. Anchoring to Puerto Rico 0.87 was explicitly ruled out: US-linked,
emigration-driven, not comparable. (Héctor ruling 2026-09-15 on Anne's
escalation; Anne's recommended option (b).)

**Glide specification.** The −0.10/yr glide shape is unchanged from v1.4; it
simply runs one year further, so the floor is reached in 2031 rather than 2030:
1.60 (2024) → 1.50 → 1.40 → 1.30 → 1.20 → 1.10 (2029) → 1.00 (2030) → 0.90
from 2031. The stress and prior-stress paths are therefore **identical through
2030** and diverge only afterwards. *This one-year extension is a specification
choice made in execution, not dictated by the ruling — flagged for Anne's
confirmation.*

**Recomputed implications (2026-09-15 run):** **126.85 M by 2050** — a 17.7 M
gap (12.3%) relative to the optimistic approximation (144.59 M), and a 22.10 M
gap (14.8%) against UN WPP 2024 medium's actual 148.95 M. This supersedes the
v1.4 figure of 128.9 M, which was computed at TFR → 1.0.

---

### 3. UN WPP Data Quality Caveat

UN WPP 2024 data contains documented discrepancies with national vital registries
for several LAC countries (Fernández-Villaverde 2026). Specifically:

- Brazil census: 203 million, not 212 million as per WPP
- Paraguay census: 6.1 million, not 6.9 million
- Similar level effects suspected in other LAC countries

**Rule:** When national vital statistics or recent census data are available, they
take precedence over UN WPP estimates. Document the source hierarchy explicitly
in every forecast output.

**Source hierarchy for Mexico (descending priority):**
1. INEGI vital registries
2. Recent national census (INEGI)
3. CONAPO projections
4. CELADE projections
5. UN WPP 2024

---

### 4. Dependency Ratio Path — Fiscal Transmission and the Fiscal Window

The demographic forecast feeds IM-6's pension contribution rate through the
endogenous dependency ratio N^R/N^L. Small errors in the TFR path compound
over the model's horizon into large errors in the fiscal sustainability analysis.

**Rule:** Always produce the dependency ratio path implied by each scenario
alongside the TFR path. Do not report TFR forecasts in isolation.

**Fiscal window — mandatory output item.** The total dependency ratio (TDR)
follows a U-shaped path under the central scenario: declining as large youth
cohorts age into the working-age population, reaching a minimum, then rising
as old-age dependency accumulates. The period of minimum TDR is the **fiscal
window** — the interval during which the demographic structure is most favorable
for reform. Claude Code must identify and report:

- The approximate year of minimum TDR under each scenario
- The TDR value at the minimum
- The duration of the window (years within 2 points of the minimum)
- An explicit flag: *"This is the reform window. Policy interventions that
  require fiscal space are most feasible during this interval."*

**2026-Q2 reference values (Mexico, all four scenarios; refined v1.3):**

| Scenario | Year of TDR min | TDR at min | Window (years within +2.0 of min) |
|----------|----------------|------------|------------------------------------|
| Optimistic (TFR=1.65) | ~2033 | 44.1 | 2028–2038 (≈10 yr) |
| **Central (TFR=1.50)** | **~2038** | **42.0** | **2033–2038 (≈5 yr)** |
| Tempo-corrected (TFR=1.60) | ~2033–2038 (tied) | 43.6 | 2028–2038 (≈10 yr) |
| Stress (TFR→0.9, working floor) | ~2038 | 35.5 | 2038–2043 (≈5 yr) |

Source: `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q2_demographic_replicate.md`.

**Duration-convention footnote (v1.4, per Cath's 2026-08-03 endorsement
condition).** Window durations in the table above are **grid-year counts on
5-year projection steps** — the span of table years satisfying
TDR ≤ TDR_min + 2.0 — not annual-resolution measurements. Linear
interpolation of the same threshold gives approximately: Optimistic
~2027–2041 (~14 yr), Central ~2030–2041 (~11 yr), Tempo-corrected
~2028–2041 (~14 yr), Stress ~2035–2045 (~9.5 yr). The cross-scenario ordering
(Central and Stress tighter than Optimistic and Tempo-corrected) is robust
to convention; absolute durations are not, and duration comparisons across
replicate vintages or against pre-v1.3 placeholder values are not
resolution-comparable. Every downstream citation of a window duration must
state its convention. IM-6 fiscal-space work anchors to the grid interval
2033–2038 — interior to the Central window under either convention, so
fiscal space is not overstated. Until the Q4 retabulation resolves the
observed-TDR wedge (Q3 replicate §4), citations of the fiscal-space numbers
also carry the Q3 §5 window-timing caveat (entry may shift later by up to
~5 years).

After the TDR minimum (in all scenarios), the ratio rises sharply as old-age
dependency accumulates — reaching ~49–51 by 2050 in the upper three scenarios
and **~41** in the stress scenario (where old-age dependency is partially
offset by collapsed youth share). Note the composition beneath that lower
stress total: by 2050 the stress column carries a *higher* old-age ratio than
any other scenario (OADR 26.4 against 24.7 optimistic) and a youth ratio barely
over half the optimistic one (YDR 14.9 against 25.9). The favourable-looking
total is arithmetic, not relief. The Central scenario's window is the operational
reference for reform-feasibility analysis.

*v1.2 placeholder values (2038–2043, TDR ≈ 39–40, 8–10 yr) are superseded by
the refined values above.*

---

## Quarterly Replication Protocol

Claude Code will produce a quarterly demographic monitoring replicate for
**México** on a three-month cycle.

### Inputs to retrieve each quarter

Retrieve the most recent available vintage of:

| Indicator | Source | Notes |
|-----------|--------|-------|
| Period TFR | INEGI / national registry | Prefer vital statistics over WPP |
| Annual births | INEGI vital registry | For CBR computation and Rule of 85 |
| Coupling rate proxy | INEGI ENOE | Marriage + cohabitation rate among 20–39 |
| Life expectancy at birth | CONAPO life tables | Sex-disaggregated |
| Net migration | CONAPO / CELADE | Flag if emigration pressure significant |
| CELADE projection update | CELADE website | Check for revision since last quarter |
| UN WPP update | UN Population Division | Check for revision since last quarter |

### Output structure per quarter

Produce a markdown file at:
```
_crossrefs/corpus/demographics/country/MEX/quarterly/YYYY-QN_demographic_replicate.md
```

Each quarterly replicate must contain:

1. **Data vintage table** — what was retrieved, from which source, for which reference year
2. **TFR update** — current observed value vs. last quarter vs. CELADE medium-variant
3. **Coupling rate update** — current observed value vs. last quarter (Mexico priority)
4. **Dependency ratio update** — current N^R/N^L implied by observed age structure
5. **Scenario comparison table** — optimistic / central / stress TFR paths, updated
6. **Tempo-correction note** — brief assessment of whether completed cohort fertility
   evidence has changed the Fischer-Dattani caution's implications this quarter
7. **Calibration flag** — explicit statement of whether IM-6 demographic inputs
   require updating before next model run
8. **Promotion recommendation** — should this replicate be promoted to the
   `_crossrefs/corpus/demographics/` corpus? Flag for Anne's review.

### Quarterly schedule

| Quarter | Reference period | Target completion |
|---------|-----------------|-------------------|
| Q1 | January–March | April 15 |
| Q2 | April–June | July 15 |
| Q3 | July–September | October 15 |
| Q4 | October–December | January 15 |

---

## First Replicate — Immediate Action

On first execution of these instructions, Claude Code should produce the
**2026-Q2 baseline replicate** using all currently available data, treating
it as the calibration anchor for subsequent quarters.

The 2026-Q2 replicate should additionally include:

- A retrospective comparison of CELADE 2022 medium-variant projections against
  observed 2024 TFR values for Mexico — to quantify the medium-variant optimism
  bias.
- The "Rule of 85" long-run population implied by current annual births for
  Mexico (following Fernández-Villaverde 2026, slide 27).

---

## Key References

- Fernández-Villaverde, J. (2026). "The Demographic Future of Humanity: Facts
  and Consequences." University of Pennsylvania / NBER / CEPR. April 1, 2026.
  [Filed at: GrandPlan/DFD/docs/corpus/JFV_260401.pdf]

- Fischer, A. (2026). X exchange with Héctor Villarreal, May 2026. Methodological
  caution on period TFR vs. completed cohort fertility for LAC.

- Dattani, S. (2024). TFR vs. completed cohort fertility charts, England and Wales
  and Sweden. Our World in Data / Human Fertility Database.

- UN WPP 2024. Summary of Results. [Treat medium-variant as optimistic for LAC.]

- CELADE projections. [Treat medium-variant as optimistic for Mexico.]

- FT (2024). "Birth rates have steeply declined in the past 15 years." Financial
  Times. [Coupling rate and socialization data.]

---

## Domain Authority

- **Anne** — approves all scenario structure decisions and calibration flags
- **Cath** — reviews dependency ratio path and fiscal transmission implications
- **Debb** — commits quarterly replicates to knowledge base
- **Héctor** — final authority on scenario discipline and DFD positioning

---

*These instructions are versioned. This is v1.5, September 2026.*
*v1.0 → v1.1 changes: (1) central scenario pinned to TFR=1.5 stable for Mexico
with confirmed 2026-Q2 population implied values; (2) stress scenario floor
anchored to Chile 1.03 (2024) as current LAC observed minimum; (3) fiscal window
added as mandatory output item in the dependency ratio rule, with 2026-Q2
reference values for Mexico.*
*v1.1 → v1.2 changes: scope narrowed to Mexico only. Costa Rica and Panamá
references removed from the operational protocol (scenario table, source
hierarchy, quarterly inputs, output path, 2026-Q2 additional items). Output
path relocated to `_crossrefs/corpus/demographics/country/MEX/quarterly/`.
Other LAC countries will be reintroduced in a later version after the Mexico
replicate stabilizes.*
*v1.2 → v1.3 changes: (1) fourth scenario column added — Tempo-corrected
(TFR=1.60 stable), reported defensively against the Fischer-Dattani
period-vs-cohort objection but not promoted to operational; (2) fiscal-window
reference values refined to match the 2026-Q2 replicate (Central: TDR_min=42.0
at 2038, ≈5-yr window) — supersedes the v1.1/v1.2 placeholder values; (3)
population implications for all four scenarios pinned to the replicate output
(140.4M central / 143.2M tempo-corrected / 128.9M stress at 2050).*
*v1.3 → v1.4 changes (2026-08-03, authorized by Héctor): duration-convention
footnote added to the §4 fiscal-window reference table per Cath's 2026-08-03
endorsement condition on the Q2/Q3 replicates — grid-year vs. interpolated
window durations distinguished (Central ≈5 yr grid / ~11 yr interpolated);
cross-scenario ordering noted as convention-robust, absolute durations not;
IM-6 anchor 2033–2038 documented as conservative interior; Q3 window-timing
caveat (entry may lag up to ~5 yr pending Q4 retabulation) referenced
wherever fiscal-space numbers are cited.*
*v1.4 → v1.5 changes (2026-09-15, Héctor ruling on Anne's stress-floor
escalation, option (b)): (1) the Stress column's empirical floor is declared
**unidentified** rather than re-anchored, with 0.9 carried as a working value —
the Chile 1.03 (2024) anchor is retired, having been overtaken by 0.99 (2025);
Puerto Rico 0.87 explicitly ruled out as a substitute. (2) The stress path runs
TFR → 0.9 by **2031** on the unchanged −0.10/yr glide, identical to the prior
path through 2030; the one-year extension is a specification choice made in
execution and is flagged for Anne's confirmation. (3) Stress reference values
recomputed (run 2026-09-15): 2050 population **126.85 M** (was 128.9 M),
TDR_min **35.5** at ~2038 (was 36.3), 2050 TDR **41.4** (was 42.8); grid window
unchanged at 2038–2043, interpolated window ~2035–2045. (4) Consequently the
**Stress columns of the 2026-Q2 and 2026-Q3 replicates are superseded** and
must not be quoted; those entries are endorsed artifacts and are deliberately
left unamended (PROTO-RAG-001 standing principle 5). Central, Optimistic and
Tempo-corrected columns are untouched throughout.*
*Next review: 2026-Q4 replicate, January 2027.*
