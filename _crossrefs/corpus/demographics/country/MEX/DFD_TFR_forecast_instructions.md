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

**Three-scenario structure for Mexico forecasts:**

| Scenario | TFR anchor — Mexico | Rationale |
|----------|---------------------|-----------|
| Optimistic | CELADE medium-variant (TFR ≈ 1.6→1.7) | Fertility stabilization and partial rebound |
| Central (fast-transition) | TFR = 1.5, stable from ~2026 | Structural drivers unabated; coupling rate decline embedded |
| Stress | TFR → 1.0 by 2030, stable thereafter | Overshooting accelerates; current LAC floor anchored to Chile 1.03 (2024) |

**Central scenario note (Mexico):** TFR = 1.5 stable is the DFD central scenario,
confirmed by the 2026-Q2 replicate. It implies a Mexico population of ~140.4M by
2050 — 8.5M below the UN medium-variant. The dominant driver of the gap is TFR,
not mortality or migration assumptions.

**Stress scenario note:** TFR → 1.0 by 2030 is a stress scenario, not a forecast.
Chile at 1.03 (2024) is the current observed LAC floor. The stress scenario is
anchored to this floor, not to an arbitrary assumption. It implies ~128.9M by 2050
— a 20.1M gap (13.5%) relative to the UN medium-variant.

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

**2026-Q2 reference values (Mexico, central scenario TFR=1.5):**
- Fiscal window minimum: approximately 2038–2043
- TDR at minimum: approximately 39–40 per 100 working-age
- Window duration: approximately 8–10 years
- After 2043: TDR rises sharply as old-age dependency accumulates

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

*These instructions are versioned. This is v1.2, May 2026.*
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
*Next review: 2026-Q3 replicate, July 2026.*
