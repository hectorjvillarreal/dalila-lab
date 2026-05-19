---
type: working_note
tier: working_note
project_scope: [DFD, BDH]
authors: [Claude Code]
year: 2026
title: "2026-Q2 demographic replicate — México (baseline)"
venue: "Internal — DFD calibration / demographics corpus"
doi: "n/a"
date_added: 2026-05-19
added_by: Claude Code
endorsed_by: "(pending — Anne, Cath)"
governing_instructions: "_crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md (v1.2)"
build_instruction: "(see §Promotion recommendation — PROTO-RAG-001 conformance pending)"
workflow_status: pending_endorsement
quarter: 2026-Q2
country: MEX
---

# 2026-Q2 demographic replicate — México (baseline)

**Quarter:** 2026-Q2 (reference period: April–June 2026)
**Status:** Baseline replicate. Establishes the calibration anchor for
subsequent quarterly runs under v1.2 of the governing instructions.
**Date produced:** 2026-05-19
**Scope:** México only (per v1.2 scope narrowing).

---

## 1. Data vintage table

| Indicator | Value used | Vintage | Source | Notes |
|---|---|---|---|---|
| Period TFR (anchor) | 1.60 | 2023 | INEGI, ENADID 2023 (Comunicado 305/24, 22 mayo 2024) | Survey-based; ENR 2024 reports registered-birth rates but does not retabulate TGF. Pinned in `scenario_anchors.md`. |
| Population age structure (baseline) | 129.74 M total, 21 × 5-yr groups | 2023 | OWID, "Population by 5-year age group" (UN WPP 2024 medium variant) | Used for cohort-component 2023 starting state. INEGI 2020 census not yet re-tabulated to 5-yr groups for this replicate. |
| Annual births (Rule of 85) | ~1.82 M | 2023 | INEGI SINAC / ENR 2023 (preliminary; 2024 figure pending release) | Used as central anchor for §10 long-run computation. 2024 SINAC release expected later in 2026; flagged for next quarter. |
| Coupling rate proxy | not retrieved this quarter | n/a | INEGI ENOE | **Data acquisition item.** Q2 baseline does not include a fresh ENOE-derived marriage+cohabitation rate among 20–39. Carried to Q3. |
| Life expectancy at birth | e₀ ≈ 75 (stylized, fixed) | n/a | Coale-Demeny West model, both sexes averaged | CONAPO life-table extraction not done this quarter. Stylized constant used in projection. Flagged for Q3. |
| Mortality schedule | 5-yr cohort survival ratios from Coale-Demeny West e₀ ≈ 75 | n/a | Same | No mortality improvement assumed to 2050; UN WPP assumes ~3–5 yr gain. Conservative on dying side. |
| Net migration | 0 | n/a | (assumption) | UN WPP assumes net outflow ~0.5/1000/yr. Zero-migration is mildly optimistic on the leaving side. |
| ASFR shape | Mexico-like, peak 25–29 | n/a | Stylized; not refitted from registered-birth microdata this quarter | Shape held fixed across scenarios. |
| Sex ratio at birth | 1.05 M : 1 F (i.e. 0.485 female at birth) | n/a | Standard biological constant | |
| CELADE comparator (2024) | n/p in OD 2025 press release; pending Excel | 2024 (CELADE estimate) | CELADE Demographic Observatory 2025 (29 Oct 2025) | Per `scenario_anchors.md`: pull MEX comparator from OD 2025 Excel tables when first needed. **Pending.** |
| UN WPP comparator | TFR ≈ 1.6 → 1.7 by 2050; 2050 pop ≈ 148.9 M (medium) | 2024 revision | UN WPP 2024 medium variant via OWID | Used as optimistic-scenario comparator. |

**Source-hierarchy compliance (v1.2 §3):** Anchor TFR uses INEGI (top of
hierarchy). Age-structure baseline uses UN WPP 2024 via OWID (tier 5,
bottom of hierarchy) — flagged because INEGI census-derived 5-yr groups
should replace this in Q3. Mortality uses stylized model (not CONAPO
life tables) — flagged.

---

## 2. TFR update

| Measure | Value | Source / vintage |
|---|---|---|
| Mexico observed period TFR | **1.60** | INEGI ENADID 2023 |
| Change vs. last quarter | n/a (baseline replicate) | — |
| CELADE OD 2025 estimate for Mexico, 2024 | not yet extracted from Excel | CELADE Demographic Observatory 2025 |
| Implied optimism gap (observed vs. CELADE) | pending Excel extraction | — |

The 2023 observed value of 1.60 is below CELADE OD 2025's modeled
trajectory family for Mexico (which embeds the UN WPP 2024 medium-variant
recovery to ~1.7). The exact comparator value is pending Excel
extraction; the optimism gap is qualitatively confirmed by the LAC
pattern (CHL: observed 1.03 vs. CELADE 1.14; CRI: observed 1.12 vs.
CELADE 1.32 — see `scenario_anchors.md`).

---

## 3. Coupling rate update

**Not retrieved this quarter.** Carried to Q3 as a data-acquisition
priority. The instructions identify the coupling rate (INEGI ENOE
marriage + cohabitation among 20–39) as a Mexico priority indicator
because of its load-bearing role in the standing analytical
considerations §1 (item 1: falling coupling rate implies permanent
fertility loss, not postponement). The FT (2024) coverage cited in the
governing instructions is the working reference for the regional pattern.

**Q3 acquisition target:** ENOE 2026-Q1 microdata or summary tabulation
showing marriage + cohabitation rate among 20–39, sex-disaggregated.

---

## 4. Dependency ratio update — current

| Ratio | 2023 (per 100 working-age) | Computation |
|---|---|---|
| Youth dependency (YDR) = pop(0–14) / pop(15–64) × 100 | **37.1** | From 2023 age structure |
| Old-age dependency (OADR) = pop(65+) / pop(15–64) × 100 | **11.9** | From 2023 age structure |
| Total dependency (TDR) = YDR + OADR | **49.0** | |

Mexico is currently near its historical TDR minimum approach from above:
the youth share is declining as fertility falls, and old-age share is
rising slowly. The structural transition into the fiscal window has not
yet occurred — TDR is still ~49.

---

## 5. Scenario comparison table (2023 → 2050)

Cohort-component projection, 5-year age groups × 5-year time steps,
Mexico-shape ASFR rescaled per scenario, mortality fixed at Coale-Demeny
West e₀ ≈ 75, zero migration. Baseline 2023 = 129.74 M.

**Four scenarios reported.** Optimistic / Central / Stress are the three
operational scenarios from instructions v1.2 §2. **Tempo-corrected** is
added as a defensive fourth column (see §6 for rationale) representing
the central scenario with TFR=1.60 stable rather than 1.50 — i.e., the
Fischer-Dattani tempo correction applied as an explicit projection rather
than a qualitative caveat. It is reported but not operational: the Central
column (TFR=1.50) remains the DFD baseline.

### Total population (millions)

| Year | Optimistic (TFR=1.65 UN-like) | **Central (TFR=1.50 stable)** | Tempo-corrected (TFR=1.60 stable) | Stress (TFR→1.0 by 2030) |
|---|---|---|---|---|
| 2023 | 129.74 | 129.74 | 129.74 | 129.74 |
| 2028 | 133.96 | 133.20 | 133.71 | 132.70 |
| 2033 | 137.78 | 136.26 | 137.28 | 133.28 |
| 2038 | 140.99 | 138.69 | 140.22 | 133.12 |
| 2043 | 143.36 | 140.30 | 142.34 | 132.16 |
| 2048 | 144.60 | 140.75 | 143.31 | 130.17 |
| **2050** | **144.59** | **140.40** | **143.19** | **128.86** |

**2050 gaps vs. Central (TFR=1.50):**
- Optimistic: **+4.19 M above** (+3.0%)
- Tempo-corrected: **+2.79 M above** (+2.0%) — the "tempo lift"
- Stress: **–11.54 M below** (–8.2%)

**Note on tempo-corrected vs. optimistic.** The tempo-corrected scenario
(143.19 M) lands close to but below the optimistic (144.59 M). The two
arise from different mechanisms: optimistic assumes a fertility rebound
that lifts TFR back toward 1.65 in the period statistics; tempo-corrected
assumes the period TFR is artificially depressed and that the structural
fertility level is closer to 1.60. The dependency-ratio paths differ
slightly (see below) because the optimistic and tempo-corrected
trajectories embed different birth cohorts at different times.

*Note on UN WPP comparator:* the optimistic column here uses TFR=1.65
stable as a UN-like approximation. UN WPP 2024 medium variant's actual
2050 figure for Mexico is ~148.9 M (TFR drifting 1.6→1.7). The TFR=1.65
stable approximation lands ~4.3 M below UN WPP 2024 because it does not
embed UN's mortality improvement and assumes flat-not-rising TFR.

### Dependency ratios (per 100 working-age 15–64)

**Optimistic (TFR=1.65):**

| Year | YDR | OADR | TDR |
|---|---|---|---|
| 2023 | 37.1 | 11.9 | 49.0 |
| 2028 | 31.7 | 13.8 | 45.5 |
| 2033 | 28.1 | 16.1 | **44.1** ← min |
| 2038 | 25.8 | 18.5 | 44.4 |
| 2043 | 26.3 | 21.2 | 47.5 |
| 2048 | 26.2 | 23.7 | 49.8 |
| 2050 | 25.9 | 24.7 | 50.6 |

**Central (TFR=1.50):**

| Year | YDR | OADR | TDR |
|---|---|---|---|
| 2023 | 37.1 | 11.9 | 49.0 |
| 2028 | 30.9 | 13.8 | 44.7 |
| 2033 | 26.5 | 16.1 | 42.6 |
| 2038 | 23.5 | 18.5 | **42.0** ← min |
| 2043 | 24.1 | 21.4 | 45.4 |
| 2048 | 24.1 | 24.1 | 48.2 |
| 2050 | 23.9 | 25.2 | 49.1 |

**Tempo-corrected (TFR=1.60 stable, Fischer-Dattani sensitivity):**

| Year | YDR | OADR | TDR |
|---|---|---|---|
| 2023 | 37.1 | 11.9 | 49.0 |
| 2028 | 31.4 | 13.8 | 45.2 |
| 2033 | 27.6 | 16.1 | 43.6 |
| 2038 | 25.1 | 18.5 | **43.6** ← min (tied with 2033) |
| 2043 | 25.6 | 21.3 | 46.8 |
| 2048 | 25.5 | 23.8 | 49.3 |
| 2050 | 25.2 | 24.9 | 50.1 |

**Stress (TFR→1.0 by 2030):**

| Year | YDR | OADR | TDR |
|---|---|---|---|
| 2023 | 37.1 | 11.9 | 49.0 |
| 2028 | 30.3 | 13.8 | 44.1 |
| 2033 | 23.4 | 16.1 | 39.4 |
| 2038 | 17.8 | 18.5 | **36.3** ← min |
| 2043 | 16.2 | 21.5 | 37.7 |
| 2048 | 16.6 | 24.8 | 41.4 |
| 2050 | 16.5 | 26.3 | 42.8 |

### Fiscal window (v1.2 §4 — mandatory output)

| Scenario | Year of TDR minimum | TDR at minimum | Window duration (years within +2.0 of min) |
|---|---|---|---|
| Optimistic | ~2033 | 44.1 | 2028–2038 (≈10 yr) |
| **Central** | **~2038** | **42.0** | **2033–2038 (≈5 yr)** |
| Tempo-corrected | ~2033–2038 (tied) | 43.6 | 2028–2038 (≈10 yr) |
| Stress | ~2038 | 36.3 | 2038–2043 (≈5 yr) |

**Tempo-correction effect on the fiscal window:** Lifting TFR from 1.50
to 1.60 raises the TDR minimum by ~1.6 points (42.0 → 43.6) and widens
the window from ~5 to ~10 years. The reform-feasibility interval is
qualitatively similar in either case (2030s decade); the tempo correction
does not relocate the window, only smooths and slightly elevates it.

> **This is the reform window. Policy interventions that require fiscal
> space are most feasible during this interval.**
>
> Under the central scenario, the window is shorter than the v1.1
> reference (which gave 8–10 years at TDR ≈ 39–40). The fresh replicate
> gives TDR_min = 42.0 at 2038, with a ~5-year window of TDR ≤ 44.0. The
> v1.1 reference values were placeholder estimates; **this replicate
> supersedes them as the authoritative Q2 baseline.**

**Refinement vs. v1.1 instructions:**

| | v1.1 reference | 2026-Q2 replicate (this run) |
|---|---|---|
| Year of TDR min (central) | 2038–2043 | 2038 |
| TDR at min | ~39–40 | 42.0 |
| Window duration | ~8–10 yr | ~5 yr |

The instructions document should be updated in v1.3 to carry these
refined reference values.

---

## 6. Tempo-correction note (Fischer-Dattani caution)

No fresh evidence this quarter that completed cohort fertility for
Mexican women now ages 30–45 will materially exceed the 2023 period TFR
of 1.60. The standing DFD position (instructions §1) is unchanged:

1. **Coupling rate.** No 2026-Q2 ENOE update retrieved (carried to Q3).
   The FT (2024) regional evidence stands.
2. **Overshooting.** Regional pattern continues: CHL 1.03, CRI 1.12,
   COL 1.10 (2024 values per `scenario_anchors.md`). Mexico's 1.60 (2023)
   is the higher end of the LAC priority group; the trajectory under the
   central scenario assumes Mexico converges down rather than recovers up.
3. **Structural drivers.** No reversal signal observed this quarter.

### Tempo-corrected scenario added (Q2 baseline)

**Rationale for inclusion.** The DFD position is that the Fischer-Dattani
tempo correction does not materially change the central trajectory for
Mexico (see standing considerations in instructions §1). However, the
period-TFR-vs-completed-cohort-fertility distinction is the most likely
methodological objection a reviewer or coauthor will raise against the
central scenario. Reporting the tempo-corrected column explicitly —
rather than only as a qualitative caveat — closes that objection
defensively. The column shows the magnitude of the disagreement, not a
re-pricing of the baseline.

**Construction.** TFR=1.60 stable from 2024 onward, i.e., the same
cohort-component machinery as the central scenario but with the period
TFR lifted by +0.10 to approximate the completed-cohort fertility level
that a Fischer-Dattani correction would impute for Mexican women now in
their late 20s and 30s. The +0.10 magnitude is the moderate correction
implied by Dattani's England-and-Wales and Sweden charts; LAC-specific
correction magnitudes are not yet available.

**Result.** The tempo correction lifts 2050 population by **2.79 M
(+2.0%)** and the TDR minimum by 1.6 points (42.0 → 43.6), widening the
fiscal window from ~5 to ~10 years. The reform-feasibility window
remains in the 2030s under either reading. **The DFD operational
baseline remains the Central scenario (TFR=1.50);** the tempo-corrected
column is reported as a defensive sensitivity and is not promoted to
operational status.

**What would change this position.** If (i) Mexico-specific completed
cohort fertility data (e.g., from a future HFD update or CONAPO cohort
analysis) shows the correction exceeds +0.15, or (ii) the coupling-rate
collapse argument in instructions §1 item 1 fails to hold for Mexico
(e.g., ENOE shows partnership formation stabilizing), the tempo-corrected
column should be promoted to a co-operational baseline alongside Central.
Neither condition is met as of Q2 2026.

---

## 7. Calibration flag

**IM-6 demographic inputs require updating before next model run: YES.**

Specifically:

- **Cohort weights / age structure:** The 2023 age-structure baseline
  from OWID/UN WPP 2024 (129.74 M total) should be the next IM-6
  starting state, with the central-scenario projection (TFR=1.5 stable)
  as the IM-6 baseline demographic block.
- **Dependency ratio path N^R/N^L:** The central-scenario TDR series
  (49.0 → 42.0 → 49.1, with min at 2038) replaces any earlier
  placeholder used in IM-6 calibration.
- **Survival probabilities:** Stylized Coale-Demeny West e₀ ≈ 75. Flag
  for replacement with CONAPO life-table-derived survival ratios in Q3.
- **Fiscal window for reform-feasibility analysis:** Approximately
  2033–2038, TDR_min ≈ 42.0 in 2038. Pension-reform fiscal-space
  calculations should anchor to this interval.

---

## 8. Promotion recommendation

**Recommendation:** Promote this replicate to the demographics corpus
after Anne's endorsement of items 1–7 and Cath's endorsement of the
dependency-ratio path and fiscal-window characterization (item 5).

**PROTO-RAG-001 conformance note (flag for Anne / Debb):**

The current artifact carries `governing_instructions:
DFD_TFR_forecast_instructions.md` rather than a `build_instruction:`
pointing to `_crossrefs/_build_instructions/`. PROTO-RAG-001 §3 requires
every corpus entry to back-link a build instruction. Two ways to
conform:

- (a) **Create a dated build instruction per quarter** —
  `_crossrefs/_build_instructions/2026-05-19_demographics_MEX_2026Q2_replicate.md`
  documenting this run; update this file's frontmatter to reference it.
  Future quarters each get their own build instruction.
- (b) **Amend PROTO-RAG-001** to allow a `governing_instructions:`
  field for recurring artifacts produced under a standing instructions
  document (the current case). The standing instructions document then
  effectively *is* the templated build instruction.

Option (a) is closer to the letter of PROTO-RAG-001. Option (b) is
cleaner operationally for the quarterly cadence. Decision deferred to
Anne / Debb.

---

## 9. Additional item (2026-Q2 baseline only) — CELADE retrospective

**Requested by v1.2 §"First Replicate":** retrospective comparison of
CELADE 2022 medium-variant projections against observed 2024 TFR for
Mexico.

**Status this quarter: partially complete.** The 2024 observed TFR for
Mexico (vital-statistics base) has not yet been published as a national
TGF figure — INEGI's ENR 2024 reports registered-birth rates but does
not retabulate the synthetic TGF (per the note in `scenario_anchors.md`).
The 2023 ENADID anchor is 1.60.

**Available LAC comparators (from `scenario_anchors.md`) showing CELADE
optimism for 2024:**

| Country | Observed 2024 TFR | CELADE OD 2025 (2024 estimate) | Gap |
|---|---|---|---|
| Chile | 1.03 | 1.14 | +0.11 (CELADE 11% higher) |
| Costa Rica | 1.12 | 1.32 | +0.20 (CELADE 18% higher) |
| Mexico | n/p (2023: 1.60) | n/p in OD 2025 press release | pending Excel |
| Colombia | 1.10 | n/p in press release | pending Excel |
| Panama | n/p (2023: 1.8) | n/p in press release | pending Excel |

**Inference for Mexico:** Given the regional pattern (CELADE 10–20%
above observed in the two countries where both are pinned), CELADE's
2024 estimate for Mexico is likely in the range 1.70–1.80 vs. an
observed value likely below 1.60. The full retrospective will be
completed in Q3 once (i) INEGI publishes a 2024 TGF figure or successor
to ENADID 2023, and (ii) the CELADE OD 2025 Excel value for Mexico is
extracted.

---

## 10. Additional item (2026-Q2 baseline only) — Rule of 85 long-run population

**Requested by v1.2 §"First Replicate":** "Rule of 85" long-run
population implied by current annual births for Mexico (following
Fernández-Villaverde 2026, slide 27).

**Method:** Stationary-population long-run identity:
pop_long_run ≈ annual_births × e₀.

**Mexico central anchor (births = 1.82 M, e₀ = 75):**
**pop_long_run ≈ 136.5 M.**

**Sensitivity:**

| Annual births | e₀ = 75 | e₀ = 80 |
|---|---|---|
| 1.60 M (low) | 120.0 M | 128.0 M |
| 1.70 M | 127.5 M | 136.0 M |
| **1.82 M (2023 INEGI SINAC, ≈ central)** | **136.5 M** | **145.6 M** |
| 1.90 M | 142.5 M | 152.0 M |
| 2.00 M (high) | 150.0 M | 160.0 M |

**Interpretation.** The cohort-component central scenario (TFR=1.5)
puts Mexico at 140.4 M in 2050 — *higher* than the 136.5 M
long-run-stationary anchor. This indicates Mexico in 2050 will still
carry transitional age-structure inertia (more workers than the
stationary equilibrium implies), and will continue declining toward the
stationary value over subsequent decades. With mortality improvement
(e₀ → 80), the stationary value rises toward 145.6 M, narrowing the gap.

**Key sensitivity:** If 2024 INEGI SINAC reports annual births below
1.7 M (a >7% drop from 2023), the long-run stationary population falls
into the 120–135 M range, materially below the central-scenario 2050
projection. Q3 should refresh this calculation with 2024 SINAC data
when available.

---

## Cross-references

- → Governing instructions (v1.2): `_crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md`
- → Scenario anchors: `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Demographics corpus README: `_crossrefs/corpus/demographics/README.md`
- → PROTO-RAG-001: `_crossrefs/protocols/PROTO-RAG-001.md`
- → Companion projection scripts (this folder):
  - `mex_population_2050.py` — UN WPP 2024 medium-variant reference plot
  - `mex_population_tfr15.py` — central scenario (TFR=1.5) cohort-component
  - `mex_population_tfr_decline.py` — stress scenario (TFR→1.0)
  - `mex_dependency_ratio_decline.py` — dependency-ratio comparison
- → Standing reference: Fernández-Villaverde (2026), "The Demographic
  Future of Humanity" (GrandPlan/DFD/docs/corpus/JFV_260401.pdf)

---

## Outstanding follow-ups for Q3 (target: July 15, 2026)

1. **CELADE OD 2025 Excel extraction** — pull Mexico 2024 estimate to
   close the optimism-gap retrospective.
2. **INEGI ENOE 2026-Q1** — coupling rate among 20–39. *Also relevant
   for the tempo-corrected scenario:* if partnership formation
   stabilizes, the tempo-corrected column may need promotion to
   co-operational status (see §6).
3. **CONAPO life tables** — replace stylized Coale-Demeny West with
   2025-vintage CONAPO survival ratios.
4. **INEGI SINAC 2024 / ENR 2024 final** — refresh annual births for
   Rule of 85; check whether INEGI publishes a 2024 TGF.
5. **PROTO-RAG-001 conformance decision** — resolve (a) vs. (b) in
   §8 before next quarterly run.
6. **Instructions v1.3** — update central-scenario fiscal-window
   reference values (TDR_min, year, duration) to match this replicate;
   add the tempo-corrected fourth column to the standing scenario table
   in instructions §2.
7. **Mexico-specific tempo correction magnitude** — open as a watch
   item if not already: is +0.10 the right Fischer-Dattani magnitude
   for Mexico, or does the LAC overshooting dynamic warrant a smaller
   correction? Dattani's published charts are EW and Sweden; an LAC
   analogue would close the methodological loop.
