# Stage 1 — Data Acquisition and Forensic Memo
# Project: Rapid Fertility Collapse in Latin America (ABM paper, parallel research within DFD)
# Author: Anne (DFD Core Team), with Nina (ABM lead)
# Date: 2026-06-17
# For: Claude Code on Dalila
# Location: GrandPlan/DFD/research/fertility_collapse_abm/data/

---

## Context and Purpose

This is Stage 1 of a four-stage pipeline to produce a standalone working paper on
rapid fertility collapses in Latin America — TFR falling from approximately 2.0 to
approximately 1.0 within roughly six years in Colombia, Argentina, Chile, and Costa
Rica. The paper proposes a threshold-coupling agent-based model (ABM) as the mechanism,
because standard demographic transition theory and OLG frameworks cannot generate such
a rapid, nonlinear collapse endogenously.

**Stage 1 is data acquisition and forensic quality assessment ONLY.** No modeling
occurs in this stage. The deliverable is clean, documented data plus a forensic memo
that flags every data-quality concern before any modeling begins. This stage exists
precisely because demographic data forensics requires care: spliced series, provisional
vital statistics, methodology breaks, and census level-effects can produce artifacts
that *look like* collapses but are not.

**This is a hard gate.** Anne and Nina review the forensic memo before Stage 2 begins.
Do not proceed to modeling.

---

## Target Countries and the Empirical Fact to Document

Primary collapse countries:
- **Colombia** — TFR approximately 2.0 (c. 2015) → approximately 1.06 (2024)
- **Argentina** — comparable collapse trajectory
- **Chile** — comparable, slightly earlier onset (2024 TFR approximately 1.03)
- **Costa Rica** — comparable (2024 TFR approximately 1.12)

Reference / comparator country (do NOT include in collapse set; use for contrast):
- **Mexico** — slower decline, 2024 TFR approximately 1.55. Mexico is the diagnostic
  target, not a collapse case. Acquire its data for later tipping-point comparison.

---

## Data to Acquire

For each of the five countries, retrieve the longest consistent annual series available
for each of the following. Annual resolution is required — not 5-year averages — because
the entire phenomenon is the *speed* of the collapse, and 5-year smoothing destroys it.

### Core series (mandatory)

| Series | Preferred source (descending priority) | Notes |
|--------|---------------------------------------|-------|
| Period TFR, annual | National statistics office → CELADE → World Bank → UN WPP | The headline series |
| Annual births (count) | National vital registry | For independent cross-check of TFR |
| Crude birth rate (CBR) | National vital registry → World Bank | For Rule-of-85 consistency check |
| Age-specific fertility rates (ASFR) | National statistics office | If available — critical for tempo vs. quantum decomposition |
| Female population by 5-year age group | National census + intercensal estimates | Denominator for fertility rates |

### Coupling / partnership series (mandatory — this is the key ABM input)

| Series | Preferred source | Notes |
|--------|-----------------|-------|
| Marriage rate, annual | National vital registry | |
| Cohabitation / union rate | National household survey (see below) | Critical — informal unions dominate in LAC |
| Share partnered, women 20–39 | National household survey | **PRIORITY SERIES — annual resolution, longest span available.** The ABM's core state variable proxy. Nina flag: acquire the annual *time-path*, not just endpoint levels — the tipping-point mechanism is a statement about the velocity of partnership decline relative to TFR decline. If coupling falls gradually while TFR collapses suddenly, that is evidence for the threshold mechanism. This series is mandatory, not best-effort. |
| Mean age at first union | National household survey / census | Distinguishes postponement from non-formation |

National household surveys to target:
- Colombia: GEIH (Gran Encuesta Integrada de Hogares), ENDS
- Argentina: EPH (Encuesta Permanente de Hogares)
- Chile: CASEN
- Costa Rica: ENAHO
- Mexico: ENOE, ENADID

### Structural covariate series (mandatory — Calles-Vogl drivers)

These are the independent calibration inputs. They MUST be acquired separately from the
TFR series, because the identification discipline of the whole paper depends on
calibrating the ABM to these inputs and treating the TFR match as an *output*, never
a target.

| Series | Preferred source | Notes |
|--------|-----------------|-------|
| Female educational attainment distribution | Census + household survey | Dominant Calles-Vogl driver |
| Sectoral composition (agriculture share) | National accounts / labor survey | Dominant Calles-Vogl driver |
| Urbanization rate | Census + intercensal | |
| Female labor force participation | Labor survey | Calles-Vogl found this NON-dominant — acquire for control |

### Migration series (mandatory for Colombia specifically)

| Series | Preferred source | Notes |
|--------|-----------------|-------|
| Net migration, annual | National statistics office → CELADE | Colombia: high emigration to US/Spain may mechanically depress TFR |
| Emigration by age group | National statistics office | Young-adult emigration affects fertility denominator |

Colombia's migration is flagged as a specific confound: Fernández-Villaverde noted
Colombia's population is already declining due to emigration. Young-adult emigration
mechanically lowers the TFR of the residual population. The forensic memo MUST assess
whether Colombia's measured collapse is partly a migration artifact rather than a pure
behavioral collapse. This is a first-order question for the paper.

---

## Forensic Quality Assessment — The Core of Stage 1

For every series acquired, Claude Code must produce a forensic assessment. This is not
optional metadata — it is the deliverable. The following checks are mandatory.

### Check 1 — Series splicing and methodology breaks
Identify whether the series is constructed from a single consistent methodology or
spliced across multiple. Flag any year where the data source or methodology changes.
A methodology break can produce an apparent discontinuity that mimics a collapse.

**Argentina specific flag:** INDEC (Argentina's statistics institute) experienced a
documented credibility crisis affecting official series during roughly 2007–2015.
Assess whether Argentine TFR/vital series cross this period and whether the collapse
signal is contaminated by the data-quality break. This is a known, serious confound.

### Check 2 — Provisional vs. final vital statistics
Recent years of vital statistics are often provisional and revised upward later
(late registration of births). A provisional final year can *exaggerate* an apparent
collapse. Flag which years are provisional for each country. Colombia and Chile 2023–2024
are likely provisional.

### Check 3 — Census level-effects
Following the Brazil (203M not 212M) and Paraguay (6.1M not 6.9M) corrections that
Fernández-Villaverde documented, assess whether recent census results have revised
the population denominators. A denominator revision changes the TFR even with unchanged
births. Flag any country where a recent census has not yet been incorporated into the
fertility denominators.

### Check 4 — Independent cross-check: births vs. TFR
For each country, check whether the reported TFR is consistent with reported annual
births and the female age structure. If TFR fell sharply but absolute births did not,
the collapse may be a denominator artifact (e.g., migration) rather than a fertility
behavior change. Compute the implied births from TFR × age structure and compare to
reported births. Flag discrepancies.

### Check 5 — Tempo vs. quantum (if ASFR available)
Where age-specific fertility rates are available, assess whether the TFR decline is
concentrated in younger ages (consistent with postponement/tempo — the Fischer-Dattani
caution) or spread across all ages (consistent with genuine quantum decline). This
distinction is central to whether the collapse is "real." Do not attempt a full
tempo-adjustment (Bongaarts-Feeney) in Stage 1 — just flag the qualitative pattern.

---

## Deliverables

Produce the following, all under
`GrandPlan/DFD/research/fertility_collapse_abm/data/`:

1. **Clean data files** — one tidy CSV per country per series category, with explicit
   columns: `year`, `value`, `source`, `methodology_flag`, `provisional_flag`.
   Long format, machine-readable, ready for Stage 2.
   **Debb requirement:** CSVs do not carry frontmatter, so every CSV must have either
   (a) a sidecar `.md` metadata file with the full PROTO-RAG-001 header, or (b) a
   complete PROTO-RAG-001 frontmatter entry in the provenance log covering that data
   product. Data must land conformant — do not leave frontmatter to be retrofitted.

2. **Forensic memo** — `STAGE1_forensic_memo.md` — the primary deliverable. Structure:
   - One section per country
   - Within each: a table of every series acquired, its source, vintage, and the
     results of Checks 1–5
   - A bottom-line assessment per country: *Is the measured collapse credible as a
     behavioral phenomenon, or is it partly/wholly a data artifact?*
   - A cross-country summary: which countries have the cleanest collapse signal
     (best candidates for the ABM), and which are contaminated (Argentina INDEC,
     Colombia migration)

3. **Data provenance log** — `STAGE1_provenance.md` — every URL, access date, and
   file retrieved, per PROTO-RAG-001 provenance discipline.

4. **A single summary chart per country** — period TFR with provisional years marked
   distinctly and methodology breaks annotated. Visual confirmation of the collapse
   and its data-quality caveats.

---

## Identification Discipline — Read Before Starting

The entire paper's credibility rests on one principle, and Stage 1 sets it up:

**The structural covariate series (education, sectoral composition, urbanization,
coupling rates) are the ABM's calibration inputs. The TFR path is the ABM's output
to be matched. These two sets of series must NEVER be conflated.** Acquire them as
strictly separate data products. Do not, at any stage, adjust a covariate series to
improve TFR fit. If Stage 1 keeps these cleanly separated, Stage 2 can enforce the
identification discipline. If they are muddled now, the paper fails later.

---

## Hard Gate

On completion, STOP. Do not begin ABM specification or modeling. Anne and Nina review
`STAGE1_forensic_memo.md` and confirm:
- Which countries have a credible collapse signal
- Whether Colombia's migration confound is manageable or disqualifying
- Whether Argentina's INDEC break is manageable or disqualifying
- That covariate and TFR series are cleanly separated

Only after this review does Stage 2 (Nina's ABM specification) begin.

---

## Placement and Provenance (Debb)

Primary location: `GrandPlan/DFD/research/fertility_collapse_abm/` — keeps this as
DFD parallel research, discoverable alongside the demographics corpus, with the
provenance chain inside DFD. Once the work reaches draft stage, cross-reference (or
symlink) from `Research/working-papers/` so the publication pipeline sees it without
breaking the DFD provenance chain. Record the dual home in `_crossrefs/mission-project-map.md`.

---

## Open Question for Héctor / Anne (does not block Stage 1)

When the household-survey microdata (GEIH, EPH, CASEN, ENAHO) is not directly
machine-accessible, should Claude Code (a) use published tabulations only, or
(b) flag the microdata as a manual-acquisition task for a later stage? Default
assumption unless told otherwise: use published tabulations in Stage 1, flag
microdata for Stage 2 if the ABM needs finer resolution.

---

*Stage 1 of 4. Version 1.1, 2026-06-17.*
*v1.0 → v1.1: (1) share-partnered series elevated to annual priority with velocity
emphasis (Nina); (2) PROTO-RAG-001 frontmatter requirement added to data deliverables
(Debb); (3) placement/provenance dual-home resolved (Debb).*
*Next: Stage 2 — Nina's ABM specification, after the forensic gate.*

---

## Forward note from Nina (shapes Stage 4, recorded now)

The paper's defensible core is the **mechanism** — replicating the rapid collapse
from independent covariate inputs. The **Mexico tipping-point diagnostic is a
speculative coda**, not the central claim. Four countries that have already crossed
the threshold give limited information about where the threshold lies — only that it
is above where they ended. Frame results accordingly from the start: strong mechanism
claim, clearly-flagged speculative application to Mexico. Overselling the Mexico
prediction is the most likely cause of referee rejection. This does not affect Stage 1
data work, but it is recorded here so the framing is consistent across all stages.
