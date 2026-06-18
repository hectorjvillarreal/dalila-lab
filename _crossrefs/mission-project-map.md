# Mission × Project Cross-Reference Map

**Purpose:** Authoritative register of how Missions, shared corpora, and Grand Plan projects (DFD, BDH, RF, Aurora) connect. Maintained alongside `Missions/_index.md` (master mission register) and the Dalila root `CLAUDE.md`.

**Last updated:** 2026-04-28

---

## Inequality Corpus (cross-cutting)

**Location:** `_crossrefs/corpus/inequality/`
**Owner:** Anne (initial scaffold); shared across DFD, BDH, RF
**Date registered:** 2026-04-28

| Project | Connection |
|---|---|
| DFD | OLG/DSGE government budget constraint calibration; capital share and effective tax rate parameters; demographic-fiscal interaction with top-share evolution |
| Fiscal Dominance Paper 1 | Proposition 2 wealth-concentration mechanism; Fagereng et al. (2024) framework |
| Fiscal Dominance Paper 2 | λ distribution calibration under ENIGH constraints |
| BDH | Health-financing distributional analysis; IRMAA-style mechanisms for IMSS/ISSSTE |
| RF | Fiscal policy event incidence classification |
| IM-6 | Watch item: capital cohort structure (long-horizon theoretical extension) |

**Status:** Initial scaffold complete (3 methodology entries, 1 watch item, LAC placeholder). Vector store integration pending Debb's installation. LAC entries pending acquisition.

---

## Demographics Corpus (cross-cutting)

**Location:** `_crossrefs/corpus/demographics/`
**Governing skill:** `_crossrefs/_skills/dfd-demographics-monitor/SKILL.md` (v0.2)
**Owner:** Anne (domain authority); drafted by Claude Code; executed by Debb
**Date registered:** 2026-05-16

| Project | Connection |
|---|---|
| DFD     | Fast-transition TFR scenario; dependency-ratio path for IM-6 pension contribution rate; OLG survival-probability block; coupling/partnership formation as fertility driver |
| BDH     | Old-age health-expenditure projections; morbidity-compression vs. expansion under life-expectancy gains; health-system financing pressure from age-structure shifts |
| Aurora  | Long-run structural demographic forces (population decline, labor-force contraction, intergenerational asset transmission); Four Pillars demographic-transmission channels |

**Status:** Initial scaffold (2026-05-16). Folder tree, README, acquisition queue, provisional scenario_anchors, Anne's inbox, and project cross-reference stubs created. Scenario anchors sourced and endorsed 2026-05-16 (5 of 5 rows confirmed; CELADE Observatorio Demográfico 2025 designated as comparator baseline; see seq 2_of_2 build instruction `2026-05-16_demographics_scenario_anchors_sourced.md`).

---

## Fertility-Collapse ABM (DFD parallel research)

**Location:** `GrandPlan/DFD/research/fertility_collapse_abm/`
**Owner:** Anne (population economics) + Nina (ABM lead); executed by Claude Code; archived by Debb
**Date registered:** 2026-06-17
**Build instruction:** `_crossrefs/_build_instructions/2026-06-17_fertility_collapse_abm_stage1.md`

| Project | Connection |
|---|---|
| DFD | Threshold-coupling ABM of rapid TFR collapse (COL/ARG/CHL/CRI) with Mexico tipping-point diagnostic; complements the OLG/DSGE demographic microfoundation; coupling/partnership formation as the core ABM state variable |
| Demographics corpus | Shares LAC TFR anchors and the fast-transition framing; national-source collapse tails (DANE/INE/DEIS/INEC/CONAPO) feed `_crossrefs/corpus/demographics/` |

**Status:** Stage 1 of 4 (data acquisition + forensic memo) executed 2026-06-17/18 — World Bank backbone (61 CSVs) + national collapse-tail series (26 CSVs), forensic Checks 1–5, all five countries source-verified. Hard gate: Anne + Nina review `STAGE1_forensic_memo.md` before Stage 2 (ABM specification). Stages 2–4 (ABM spec, calibration, write-up) pending.

---

## Infrastructure (cross-cutting)

**Location:** `_crossrefs/protocols/`, `_crossrefs/_build_instructions/`
**Owner:** Debb
**Date registered:** 2026-04-28

| Artifact | Connection |
|---|---|
| PROTO-RAG-001 | Corpus entry and build instruction protocol; governs all corpus subdomains and project-scoped corpora |
| _build_instructions/ archive | Provenance layer for the team's intellectual infrastructure; retained indefinitely |
