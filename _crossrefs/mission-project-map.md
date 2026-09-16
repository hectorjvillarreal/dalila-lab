# Mission × Project Cross-Reference Map

**Purpose:** Authoritative register of how Missions, shared corpora, and Grand Plan projects (DFD, BDH, RF, Aurora) connect. Maintained alongside `Missions/_index.md` (master mission register) and the Dalila root `CLAUDE.md`.

**Last updated:** 2026-08-08

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

## BID2 Motivation Build — health expenditure by sex, income, and age (Mission: BID2)

**Location:** `Missions/Funded/BID2/motivation/`
**Owner:** Héctor; executed by Claude Code; coauthor briefings filed in `_crossrefs/team/` (Anne, Beth, Fina, Judy)
**Date registered:** 2026-08-08
**Build instruction:** `Missions/Funded/BID2/draft_2609/CC_instrucciones_motivation-health-profiles_v2.md`

| Project | Connection |
|---|---|
| BID2 (mission) | Empirical base of the health-refocused paper's motivation section: ENIGH 2018–2024 + ENSANUT 2018/2024 + ENASEM 2018–2024 triangulation; 12 figures, NUMBERS/VERIFICATION/provenance; empirical m_j counterpart for `ge_model_gender.jl`; 2050 composition experiment consumes Anne's `demographics_2050.jl` primitives verbatim (implied 65+/20–64 = 0.747 vs her 0.744 anchor) |
| BDH | Old-age health-financing evidence for Mexico: OOP age-sex profiles, catastrophic-spending gradients, forgone-care-by-insurance (Seguro Popular→IMSS-Bienestar transition visible), unmet-need measurement on four independent lines |
| DFD | NTA-style age-sex utilization schedule derived from ENSANUT (`output/tables/ensanut_util_weights_2024.csv`) — candidate demographics-corpus entry pending Anne's endorsement; morbidity/mortality asymmetry (gender frailty paradox) reproduced in ENASEM microdata |
| Demographics corpus | Composition arithmetic links the corpus' dependency-ratio anchors to health-spending aggregation (per-adult OOP ×1.47 under 2050 stationary structure); September WPP single-age swap will convert the stationary bound to a transitional number |
| RF | Candidate fiscal-narrative event: the 2020 OOP surge (universal, participation-margin, poorest decile +76% real; fig 12) as a provision-shock episode inside RF's 2000–2025 window |

**Status:** Build complete and committed 2026-08-08 (branch `p3-correcciones-tex`); scripts 00–11 re-run end to end. Open loops: Judy's confirmation of the reconstructed frailty index (provisional flag on fig 10); Beth's ratification of the curative/preventive classification and placement of the 2020 natural-experiment finding; Anne's September WPP swap triggers a `scripts/10` rerun. Standing rules: ENIGH shapes-not-levels (22–34% of GHED OOP); preventive share quoted as the 2%–46% bracket; ages 5–14 Tier-3 cell embargoed.

---

## Infrastructure (cross-cutting)

**Location:** `_crossrefs/protocols/`, `_crossrefs/_build_instructions/`
**Owner:** Debb
**Date registered:** 2026-04-28

| Artifact | Connection |
|---|---|
| PROTO-RAG-001 | Corpus entry and build instruction protocol; governs all corpus subdomains and project-scoped corpora |
| _build_instructions/ archive | Provenance layer for the team's intellectual infrastructure; retained indefinitely |
