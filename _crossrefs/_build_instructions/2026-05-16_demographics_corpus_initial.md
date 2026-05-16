---
type: build_instruction
build_type: initial_scaffold
date: 2026-05-16
corpus_affected:
  - _crossrefs/corpus/demographics/
  - _crossrefs/mission-project-map.md
  - CLAUDE.md
  - GrandPlan/DFD/docs/corpus/_cross_references.md
  - GrandPlan/BDH/docs/corpus/_cross_references.md
  - GrandPlan/Aurora/docs/corpus/_cross_references.md
triggered_by: "dfd-demographics-monitor SKILL.md v0.2 audit (2026-05-16). The skill's prerequisite gate halts activation until the demographics corpus scaffold exists. This build instruction creates the scaffold so the skill can fire."
agents_involved: [Héctor, Claude Code, Debb, Anne]
status: executed
sequence_position: "1_of_2"
notes: "Anne follow-up required: source-pin the scenario_anchors.md TFR values before the skill produces any fast-transition or baseline-revision classifications. Follow-up sequence_position 2_of_2 is the anchor sourcing build instruction, to be filed once Anne completes the review."
---

# Demographics Corpus — Initial Scaffold Build Instructions

**To:** Claude Code (Dalila session, Debb mode for execution)
**From:** Claude Code (drafter, on Héctor's instruction following the SKILL.md v0.2 audit)
**Date:** 2026-05-16
**Re:** Scaffold the cross-project demographics corpus so the `dfd-demographics-monitor` skill can leave its prerequisite gate.

---

## 1. Scope and rationale

This task creates the **demographics** corpus at `_crossrefs/corpus/demographics/`
as a cross-cutting resource shared across DFD, BDH, and Aurora. The motivation
is operational: the `dfd-demographics-monitor` skill (`_crossrefs/_skills/dfd-demographics-monitor/SKILL.md`,
v0.2 2026-05-16) declares a prerequisite scaffold gate. Until the corpus folder
tree, README, and supporting files exist, the skill halts on activation and emits
this build-instruction reference. Creating the scaffold lifts that gate.

The skill itself is workflow logic. This build instruction is the *infrastructure*
it requires. Monitoring content (Tier-1 corpus entries and watch items) is not
embedded here — it is generated as the skill fires.

The demographics corpus is structurally analogous to the inequality corpus
(`_crossrefs/corpus/inequality/`, scaffolded by
`2026-04-28_inequality_corpus_initial.md` and retrofitted by
`2026-04-29_inequality_corpus_retrofit.md`). It uses PROTO-RAG-001 frontmatter
throughout.

A standalone demographics corpus, rather than scattering entries across DFD,
BDH, and Aurora subfolders, reflects the cross-cutting nature of demographic
content (every demographic observation has implications for at least two of the
three projects) and resolves with the shared `_crossrefs/` corpus architecture
already endorsed for inequality.

---

## 2. Folder scaffold

Create the following directory structure under Dalila root:

```
_crossrefs/corpus/demographics/
├── README.md
├── _acquisition_queue.md
├── scenario_anchors.md
├── _pending/
│   └── _anne_inbox.md
├── methodology/                 (empty; entries to follow as skill fires)
├── releases/                    (empty; entries to follow)
├── country/                     (empty; ISO-3166 alpha-3 subfolders created on first use)
├── observations/                (empty; multi-country working notes)
└── watch_items/                 (empty; entries to follow)
```

In addition, create stub files at the project-side cross-reference targets:

```
GrandPlan/DFD/docs/corpus/_cross_references.md
GrandPlan/BDH/docs/corpus/_cross_references.md
GrandPlan/Aurora/docs/corpus/_cross_references.md
```

If parent directories `GrandPlan/{BDH,Aurora}/docs/corpus/` do not exist, create
them. `GrandPlan/DFD/docs/corpus/` already exists per current working-tree state.

---

## 3. Top-level README — `_crossrefs/corpus/demographics/README.md`

Create with the following content:

```markdown
# Demographics Corpus

**Scope:** Empirical and methodological references on demographic dynamics —
fertility, mortality, migration, age structure, household formation, education
attainment, socialization, and population projections — with priority on Latin
America and Mexico-specific calibration material. Cross-cutting across DFD,
BDH, and Aurora.

**Status:** Initial scaffold (May 2026). Populated incrementally by the
`dfd-demographics-monitor` skill (v0.2) on activation. No entries at scaffold
creation; `scenario_anchors.md` carries provisional values pending Anne's
source-pinning review.

## Organization

- `methodology/` — methodological references on demographic measurement and
  projection (full papers on TFR / cohort-fertility estimation, life-table
  construction, projection-revision methodology)
- `releases/` — institutional data releases (UN WPP, CELADE, CONAPO, INE,
  Birth Gauge, national vital-statistics agencies); tier `data_source`
- `country/` — country-specific notes, organized by ISO-3166 alpha-3 subfolder
  (`MEX`, `CRI`, `PAN`, `COL`, `CHL`, etc.)
- `observations/` — multi-country / cross-cutting working notes that do not
  belong to a single-country subfolder; tier `working_note`
- `watch_items/` — open methodological threads connecting demographic material
  to active modeling work
- `_pending/` — endorsement-pending holding area; entries move to their
  topical subfolder on Anne's (or appropriate domain authority's) endorsement
- `_acquisition_queue.md` — Tier-2 brief entries (casual references and
  forward-links to sources not yet read); per the skill's salience gate
- `scenario_anchors.md` — sourced anchor values for scenario classification
  (TFR by country, vintage, source); load-bearing for fast-transition vs.
  baseline-revision classification

## Standing principles

- CELADE medium-variant projections are treated as the **optimistic** scenario
  for LAC priority countries, not the central one. Observed recent TFR values
  are the empirical baseline. The fast-transition scenario is increasingly the
  baseline, not a stress test.
- Anchor values are maintained in `scenario_anchors.md`, not duplicated in
  individual entries; entries cite the anchor.
- Source reliability is recorded explicitly: `primary` (vital registries,
  census, UN WPP, CELADE, CONAPO, INE) / `secondary` (FT, OWiD, journalism,
  academic aggregation) / `preliminary` (preprints, blog estimates).
- The `dfd-demographics-monitor` skill governs activation, classification, and
  routing. Manual additions are permitted but must still conform to PROTO-RAG-001
  frontmatter and pass through `_pending/` for endorsement.

## Cross-references

- → Governing protocol: `_crossrefs/protocols/PROTO-RAG-001.md`
- → Governing skill: `_crossrefs/_skills/dfd-demographics-monitor/SKILL.md`
- → Initial scaffold build instruction: `_crossrefs/_build_instructions/2026-05-16_demographics_corpus_initial.md`
- → Parallel cross-cutting corpus: `_crossrefs/corpus/inequality/README.md`

## Cross-project register

This corpus is registered in `_crossrefs/mission-project-map.md` as a shared
resource. Entries here are referenced (via each project's
`_cross_references.md`) but not duplicated across DFD/BDH/Aurora docs folders.
```

---

## 4. Acquisition queue — `_crossrefs/corpus/demographics/_acquisition_queue.md`

Create with the following content:

```markdown
---
type: acquisition_queue
corpus: demographics
date_opened: 2026-05-16
maintained_by: Claude Code
---

# Demographics Corpus — Acquisition queue

Tier-2 brief entries per the `dfd-demographics-monitor` skill salience gate.
Each line: one casual reference, passing mention, or forward link to a source
not yet read at sufficient depth for a Tier-1 artifact.

Format:
- YYYY-MM-DD — [short reference] — [indicator(s)] — [iso3 or aggregate] — [link or pointer]

## Entries

*(none at scaffold creation)*
```

---

## 5. Scenario anchors — `_crossrefs/corpus/demographics/scenario_anchors.md`

Create with the following content. The file is created as a **skeleton only** —
priority-country rows are listed but values, vintages, and sources are left
blank for Anne to populate from primary references. No provisional values are
inherited from SKILL.md v0.1.

```markdown
---
type: working_note
tier: data_source
project_scope: [DFD, BDH, Aurora]
authors: [Anne]
year: 2026
title: "Scenario anchors — observed recent TFR for LAC priority countries"
venue: "Internal — demographics corpus"
doi: "n/a"
date_added: 2026-05-16
added_by: Claude Code
endorsed_by:
build_instruction: "_crossrefs/_build_instructions/2026-05-16_demographics_corpus_initial.md"
workflow_status: pending-endorsement
---

# Scenario anchors — observed recent TFR for LAC priority countries

## Purpose

Single source of anchor values for the scenario classification dimension of the
`dfd-demographics-monitor` skill. Entries here are cited by individual corpus
entries rather than duplicated; revisions flow through this file.

## Anchors (skeleton — pending Anne's first-pass population)

| ISO-3 | Country | Recent observed TFR | Vintage | Source | Status |
|---|---|---|---|---|---|
| MEX | Mexico      | TODO | TODO | **TODO — Anne** | missing |
| CRI | Costa Rica  | TODO | TODO | **TODO — Anne** | missing |
| COL | Colombia    | TODO | TODO | **TODO — Anne** | missing |
| CHL | Chile       | TODO | TODO | **TODO — Anne** | missing |
| PAN | Panama      | TODO | TODO | **TODO — Anne** | missing |

CELADE medium-variant comparator for the same vintages is the next column to
add once Anne confirms which CELADE revision is in force as the baseline
reference.

## Operational status

⚠️ **This file is empty of values at scaffold creation.** Until Anne completes
the first-pass population AND a sequence_position 2_of_2 build instruction
records the endorsement, all classifications under §Step 2a of the skill that
invoke the fast-transition or baseline-revision scenarios must cite their own
anchor source in-note. This file becomes the canonical reference only once
endorsed; in-note citation continues to be acceptable thereafter as a
provenance practice.

## Endorsement workflow

1. Anne populates each row with the recent observed TFR, vintage year, and
   specific institutional source (e.g., "CONAPO Proyecciones 2018–2070,
   revisión 2023"; "INE Chile, Estadísticas Vitales 2024 preliminar"; "UN
   WPP 2024 medium variant"). The **Status** column updates from `missing`
   to `confirmed`.
2. Anne fills `endorsed_by: Anne` in this file's frontmatter and updates
   `workflow_status: endorsed`.
3. A follow-up build instruction
   (`2026-MM-DD_demographics_scenario_anchors_sourced.md`, sequence_position
   2_of_2 to this one) records the population and endorsement as
   `build_type: expansion`.

## Cross-references

- → Build instruction: `_crossrefs/_build_instructions/2026-05-16_demographics_corpus_initial.md`
- → Governing skill: `_crossrefs/_skills/dfd-demographics-monitor/SKILL.md` §Scenario Discipline
- → Fernández-Villaverde (2026) "The Demographic Future of Humanity" (standing reference for fast-transition framing)
```

---

## 6. Anne's pending-review inbox — `_crossrefs/corpus/demographics/_pending/_anne_inbox.md`

Create with the following content:

```markdown
# Anne's inbox — demographics corpus pending review

Per `dfd-demographics-monitor` SKILL.md v0.2 §Routing and Filing, the skill
appends a one-line entry here on every new arrival in `_pending/`. Anne
reviews on her own cadence (set outside this skill).

Format:
- YYYY-MM-DD — [filename in _pending/] — [project_scope] — [indicators] — [iso3]

## Pending

*(none at scaffold creation)*

## Endorsed and moved (recent — last 30 days)

*(none at scaffold creation)*
```

---

## 7. Project cross-reference stubs

Create the following three files. Each is a thin index that the skill appends
to whenever it produces an entry whose `project_scope` includes the project.

### 7a. `GrandPlan/DFD/docs/corpus/_cross_references.md`

```markdown
# DFD corpus — cross-references to shared corpora

Pointers to entries in shared `_crossrefs/corpus/` subdomains that bear on DFD
work. Maintained by the skills that produce the upstream entries (currently:
`dfd-demographics-monitor` for the demographics corpus).

## Demographics (`_crossrefs/corpus/demographics/`)

*(none at scaffold creation)*

## Inequality (`_crossrefs/corpus/inequality/`)

See `_crossrefs/corpus/inequality/README.md` §Cross-references for the
project-level connection notes (Cath: government budget constraint
calibration; Anne: demographic-fiscal interaction with top-share evolution).
Itemized back-references to specific inequality entries can be added in a
subsequent retrofit.
```

### 7b. `GrandPlan/BDH/docs/corpus/_cross_references.md`

```markdown
# BDH corpus — cross-references to shared corpora

Pointers to entries in shared `_crossrefs/corpus/` subdomains that bear on BDH
work. Maintained by the skills that produce the upstream entries (currently:
`dfd-demographics-monitor` for the demographics corpus).

## Demographics (`_crossrefs/corpus/demographics/`)

*(none at scaffold creation)*

## Inequality (`_crossrefs/corpus/inequality/`)

See `_crossrefs/corpus/inequality/README.md` §Cross-references for the
project-level connection notes (Beth: health-financing distributional analysis;
Auerbach 2025 IRMAA precedent for IMSS/ISSSTE).
```

### 7c. `GrandPlan/Aurora/docs/corpus/_cross_references.md`

```markdown
# Aurora corpus — cross-references to shared corpora

Pointers to entries in shared `_crossrefs/corpus/` subdomains that bear on
Aurora / TetraDevelopment foresight work. Maintained by the skills that
produce the upstream entries (currently: `dfd-demographics-monitor` for the
demographics corpus).

## Demographics (`_crossrefs/corpus/demographics/`)

*(none at scaffold creation)*

## Inequality (`_crossrefs/corpus/inequality/`)

No standing cross-references at scaffold creation. Add as Four Pillars
analysis surfaces inequality-channel connections.
```

---

## 8. Cross-reference register update — `_crossrefs/mission-project-map.md`

Append (or create section if absent) the following block. **Do not overwrite
existing content.** If a similar section structure for inequality already exists
in the file, mirror it.

```markdown
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

**Status:** Initial scaffold (2026-05-16). Folder tree, README, acquisition queue,
provisional scenario_anchors, Anne's inbox, and project cross-reference stubs
created. Scenario anchors awaiting Anne's source-pinning (follow-up build
instruction sequence_position 2_of_2).
```

---

## 9. CLAUDE.md update

In the Dalila root `CLAUDE.md`, under §7 "Scientific computing stack" (or the
"Inequality corpus" subsection, immediately after it), add:

```markdown
### Demographics corpus (`_crossrefs/corpus/demographics/`)

Cross-cutting demographics corpus shared across DFD, BDH, and Aurora. Initial
scaffold May 2026. Populated incrementally by the `dfd-demographics-monitor`
skill (v0.2) on activation; manual additions also conform via `_pending/`
endorsement workflow. Scenario anchors (`scenario_anchors.md`) carry
provisional TFR values pending Anne's source-pinning. See
`_crossrefs/corpus/demographics/README.md` for organization and standing
principles.
```

Do not disturb other CLAUDE.md content.

---

## 10. Execution checklist for Claude Code (Debb mode)

- [ ] Create folder structure under `_crossrefs/corpus/demographics/` per §2
- [ ] Create project-side stub directories where missing
      (`GrandPlan/BDH/docs/corpus/`, `GrandPlan/Aurora/docs/corpus/`)
- [ ] Write top-level README per §3
- [ ] Write `_acquisition_queue.md` per §4
- [ ] Write `scenario_anchors.md` per §5 (mark provisional values clearly)
- [ ] Write `_pending/_anne_inbox.md` per §6
- [ ] Write three project cross-reference stub files per §7a–c
- [ ] Update `_crossrefs/mission-project-map.md` per §8
      (append; do not overwrite)
- [ ] Update Dalila root `CLAUDE.md` per §9 (insert after Inequality corpus
      subsection; do not disturb other content)
- [ ] Confirm Git working tree state; commit with message:
      `demographics corpus: initial scaffold (gate for dfd-demographics-monitor v0.2)`
- [ ] Mark this build instruction `status: executed` in its frontmatter
- [ ] Report back to Héctor: scaffold complete, skill gate lifted; Anne
      follow-up flagged for `scenario_anchors.md` source-pinning

---

## 11. Notes

- **No corpus entries are created by this build.** The scaffold provides the
  landing zone; the skill produces content on activation. This matches the
  inequality corpus model only in shape — inequality's initial build embedded
  three full RAG entries because Anne had drafted them in advance. Demographics
  has no equivalent pre-staged batch.
- **Anne follow-up is load-bearing.** `scenario_anchors.md` is created as a
  skeleton — priority-country rows present, but values, vintages, and sources
  blank. Per Héctor's call (2026-05-16), no provisional values are inherited
  from SKILL.md v0.1. Anne must complete the first-pass population, and a
  sequence_position 2_of_2 build instruction (`expansion` build_type) must
  record the endorsement, before any classification under the skill's §Step 2a
  invokes the fast-transition scenario by reference to this file. Until then,
  in-note citation is required.
- **`observations/` subfolder is a skill-level convention.** It does not appear
  in the inequality corpus structure. Justification: demographic working notes
  spanning multiple countries (e.g., a CEPAL regional bulletin) fit poorly into
  a per-country `country/{iso3}/` structure. If a future audit prefers
  structural parity with inequality, fold `observations/` into a `regional/`
  subfolder analogous to inequality's `latam/`.
- **Vector store integration is out of scope.** Debb's installation, when
  available, will ingest the corpus. Frontmatter is designed for that ingestion.
- This build instruction is itself the artifact PROTO-RAG-001 requires every
  corpus entry to back-link to. The `scenario_anchors.md` entry created by §5
  carries this filename in its `build_instruction:` field; future corpus entries
  filed by the skill will back-link to their own (skill-fire-time) build
  instructions, not to this one.
