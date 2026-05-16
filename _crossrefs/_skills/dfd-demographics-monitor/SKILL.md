---
name: dfd-demographics-monitor
version: 0.2
revises: 0.1
date_revised: 2026-05-16
revised_by: Claude Code
description: >
  Cross-project demographics monitoring skill for DFD, BDH, and Aurora. Activate
  when demographically-relevant material arrives — charts, papers, data releases,
  news, or casual references — involving fertility (TFR, CBR, cohort fertility),
  mortality, life expectancy, migration, coupling, household formation,
  age structure / dependency ratios, education attainment, socialization trends,
  or population projections. Activate also when Héctor flags a demographic
  observation, shares a UN WPP / CELADE / CONAPO update, or asks about scenario
  calibration. Do NOT wait for an explicit request — but apply the Tier-1 / Tier-2
  salience gate (§Activation). Outputs are PROTO-RAG-001-conformant artifacts
  (`corpus_entry` or `research_watch_item`) routed to
  `_crossrefs/corpus/demographics/`.
---

# DFD Demographics Monitoring Skill (v0.2)

## Purpose

Standing analytical protocol for identifying, classifying, and routing
demographically-relevant material across the three demographic-sensitive Grand
Plan projects: **DFD**, **BDH**, and **Aurora**. All outputs land in the shared
corpus at `_crossrefs/corpus/demographics/` and conform to PROTO-RAG-001
(`_crossrefs/protocols/PROTO-RAG-001.md`) for frontmatter schema, authorship
discipline, and provenance back-links.

This skill is a *workflow*; it does not introduce new artifact types. Every
output is one of the artifact types PROTO-RAG-001 already authorizes.

---

## Prerequisites (scaffold gate)

The skill REQUIRES the demographics corpus to be scaffolded before it can fire.
Scaffold artifacts:

```
_crossrefs/corpus/demographics/
├── README.md
├── _pending/                 # endorsement-pending holding
├── _acquisition_queue.md     # Tier-2 brief entries
├── methodology/              # methodological references (papers on demographic measurement / projection)
├── releases/                 # institutional data releases (UN WPP, CELADE, CONAPO, INE)
├── country/                  # country-specific notes, organized by ISO-3166 alpha-3 subfolder
├── watch_items/              # open methodological threads
└── scenario_anchors.md       # sourced anchor values for scenario classification
```

If this scaffold does not exist when the skill activates, the skill HALTS and
emits a request for a build instruction with the canonical filename
`_crossrefs/_build_instructions/2026-MM-DD_demographics_corpus_initial.md`.
Scaffold creation is a build-instruction-level action under PROTO-RAG-001, not a
within-skill action.

---

## Activation Triggers

Activate on any of the following:

- Incoming visual material (charts, graphs, maps) with demographic content
- References to TFR, CBR, cohort fertility, replacement rate, coupling rate
- UN WPP, CELADE, CONAPO, Birth Gauge, INE, or national vital-statistics updates
- Mortality, life expectancy, or survival-curve data
- Migration flows relevant to LAC countries
- Age-structure, dependency-ratio, household-formation, or education-attainment data
- Socialization or partnership-formation trends with fertility implications
- Population-projection revisions (any WPP / CELADE revision)
- Any statement by Héctor flagging demographic significance ("this is important
  for DFD", "this is striking", "this graph is...")

### Salience gate (Tier-1 vs Tier-2)

To prevent corpus noise from casual mentions, the skill applies a two-tier gate:

- **Tier 1 — full artifact** (corpus_entry or research_watch_item). Triggered when
  the material is empirical or analytical: a chart, paper, dataset, projection
  revision, or substantive analytical claim. The skill produces the full
  PROTO-RAG-001-conformant output below.
- **Tier 2 — acquisition queue entry**. Triggered when the material is a casual
  reference, a passing mention, or a forward link to a source not yet read. The
  skill appends a one-line entry to
  `_crossrefs/corpus/demographics/_acquisition_queue.md` and stops. No full
  artifact is produced.

The gate is conservative: when in doubt, Tier-2.

---

## Classification Protocol

On a Tier-1 activation, classify along four dimensions:

### 1. Indicator type
- `tfr` — total fertility rate (period or cohort)
- `cbr` — crude birth rate
- `mortality` — life expectancy, survival curves, death rates
- `migration` — net migration flows, emigration pressure
- `coupling` — partnership formation, marriage, cohabitation rates
- `household-formation` — household size, headship, multigenerational structure
- `age-structure` — population pyramid, dependency ratios, median age
- `education-attainment` — schooling distribution as a fertility / labor-supply channel
- `socialization` — time-use data with fertility implications
- `projection` — WPP / CELADE / national revision, scenario update
- `composite` — multiple indicators in one source

### 2. Geographic scope (ISO-3166 alpha-3)
Record specific country codes. Use these aggregates only when the source itself
aggregates: `WLD` (global), `LAC` (Latin America and Caribbean), `OECD`.

DFD calibration priority countries: `MEX` (primary), `CRI` and `PAN` (IM-6
calibration peers). Other LAC codes: `ARG`, `BRA`, `CHL`, `COL`, `PER`, etc.

### 3. Scenario implication
- `fast-transition` — supports or strengthens the fast-transition TFR scenario
- `baseline-revision` — warrants revision of CELADE medium-variant baseline
- `stress` — extreme low-fertility or mortality-shock scenario
- `neutral` — informative but no immediate scenario implication

### 4. Project routing
Assess which projects are affected (any non-empty subset of `DFD`, `BDH`, `Aurora`):
- **DFD** — almost always relevant for demographic content
- **BDH** — relevant when mortality, aging, morbidity, or health-system pressure implied
- **Aurora** — relevant when long-run structural demographic forces are at stake

---

## Analytical Steps

After classification, execute in order:

### Step 1 — Summarize the material
Two to four sentences. What does the source show? What is the key empirical
finding? Do not reproduce figures verbatim — paraphrase and synthesize.

### Step 2 — Project-specific calibration implications

Answer the questions for each project flagged in classification dimension 4. If
a project is not flagged, omit its sub-block.

**Step 2a — DFD** (when `DFD` is flagged)
- Does this affect the **fast-transition TFR scenario** for Mexico?
- Does this affect the **dependency-ratio path** feeding IM-6's pension contribution rate?
- Does this affect **survival probabilities** used in the OLG's demographic block?
- Does this affect **coupling / partnership formation** as an upstream fertility driver?

**Step 2b — BDH** (when `BDH` is flagged)
- Does this affect **old-age health-expenditure projections** in Mexico or LAC peers?
- Does this affect the **morbidity-compression vs. expansion** assumption for life-expectancy gains?
- Does this affect **health-system financing pressure** through age-structure shifts?

**Step 2c — Aurora** (when `Aurora` is flagged)
- Does this affect long-run **structural demographic forces** (population
  decline, labor-force contraction, intergenerational asset transmission)?
- Does this connect to a **Four Pillars** thesis (post-LLM intelligence,
  genomics, fusion, strategic reasoning) through demographic transmission?

### Step 3 — Flag source quality
- **Reliability**: `primary` (vital registries, census, UN WPP, CELADE, CONAPO,
  national statistical institutes) / `secondary` (FT, Our World in Data, academic
  aggregation, journalism) / `preliminary` (preprints, blog estimates).
- **Recency**: data vintage year (distinct from publication year; record both
  when they differ).

### Step 4 — Decide artifact type and workflow status

Two decisions, independently:

**Artifact type** (per PROTO-RAG-001):
- `corpus_entry`, `tier: methodological_reference` — full paper on a demographic
  measurement / projection method
- `corpus_entry`, `tier: data_source` — a data release, projection revision, or
  dataset
- `corpus_entry`, `tier: working_note` — synthesis of an observation, news item,
  or chart that does not itself constitute a primary source but is worth recording
- `research_watch_item` — an open methodological thread surfaced by the material,
  not the material itself

**Workflow status** (skill-internal, recorded in frontmatter as `workflow_status`):
- `pending-endorsement` — Anne's review required before the entry leaves `_pending/`
- `endorsed` — Anne (or appropriate domain authority) has endorsed; entry sits
  in its topical subfolder
- `superseded` — later material has displaced this entry

---

## Output Artifacts

The skill produces one of two artifact templates, both fully PROTO-RAG-001-conformant.

### Template A — corpus_entry

```markdown
---
type: corpus_entry
tier: [methodological_reference | data_source | working_note]
project_scope: [DFD, BDH, Aurora — subset]
authors: [Last, First; Last, First]   # or institution if no individual author (e.g., [UN DESA])
year: YYYY
title: "Full title in quotes"
venue: "Journal / working paper series / institutional release / URL"
doi: "10.xxxx/yyyy or URL"
date_added: YYYY-MM-DD
added_by: Claude Code
endorsed_by:                          # blank until Anne (or other domain authority) endorses
build_instruction: "_crossrefs/_build_instructions/YYYY-MM-DD_demographics_{slug}.md"

# Skill-specific extension fields (authorized by this skill, recorded for retrieval):
indicators: [from §Classification dim 1]
geography: [ISO-3166 alpha-3 codes; or aggregate WLD / LAC / OECD]
scenario_implication: [fast-transition | baseline-revision | stress | neutral]
source_reliability: [primary | secondary | preliminary]
data_vintage: YYYY
workflow_status: [pending-endorsement | endorsed | superseded]
---

# [Title]

## One-line summary
[Single sentence capturing the contribution.]

## Core content
[2–4 sentences synthesizing the source. Paraphrase; do not reproduce figures.]

## Project calibration implications
[Step 2a / 2b / 2c output, only for projects in `project_scope`.]

## Open questions surfaced
[Candidate watch items, if any. Each gets a one-line gloss; the actual watch
item is created as a separate `research_watch_item` artifact via Step 4.]

## Citation
[Full bibliographic citation.]

## Cross-references
- → Build instruction: `_crossrefs/_build_instructions/YYYY-MM-DD_demographics_{slug}.md`
- → Related corpus entries: [paths]
- → Related watch items: [paths]
- → Project corpus cross-refs:
    - DFD: `GrandPlan/DFD/docs/corpus/_cross_references.md`
    - BDH: `GrandPlan/BDH/docs/corpus/_cross_references.md`
    - Aurora: `GrandPlan/Aurora/docs/corpus/_cross_references.md`
  (Only the projects in `project_scope` get a back-link entry; see §Routing.)
```

### Template B — research_watch_item

```markdown
---
type: research_watch_item
status: open
date_opened: YYYY-MM-DD
opened_by: [Claude Code]
endorsed_by:                          # blank until Anne endorses tracking
promoted_by:                          # blank until promoted
date_promoted:                        # blank until promoted
related_corpus: [paths to corpus entries that surfaced this thread]
related_projects: [DFD, BDH, Aurora — subset]
build_instruction: "_crossrefs/_build_instructions/YYYY-MM-DD_demographics_{slug}.md"
---

# [Thread title]

## Origin
[Who flagged it, when, what conversation or source.]

## The thread
[The substantive idea.]

## Modeling implication
[Concrete connection to active or planned work.]

## Open questions
[Gating conditions for development.]

## Status
Watch item, not active commitment.

## Triggers for promotion
[Explicit conditions for elevation to active research.]

## Cross-references
- → Build instruction: `_crossrefs/_build_instructions/YYYY-MM-DD_demographics_{slug}.md`
- → Surfacing corpus entry: [path]
```

---

## Routing and Filing

**Filing path by artifact type and status:**

| Artifact | Status | Path |
|---|---|---|
| `corpus_entry` | `pending-endorsement` | `_crossrefs/corpus/demographics/_pending/YYYY-MM-DD_{slug}.md` |
| `corpus_entry`, `tier: methodological_reference` | `endorsed` | `_crossrefs/corpus/demographics/methodology/YYYY-MM-DD_{slug}.md` |
| `corpus_entry`, `tier: data_source` | `endorsed` | `_crossrefs/corpus/demographics/releases/YYYY-MM-DD_{slug}.md` |
| `corpus_entry`, `tier: working_note` (country-specific) | `endorsed` | `_crossrefs/corpus/demographics/country/{iso3}/YYYY-MM-DD_{slug}.md` |
| `corpus_entry`, `tier: working_note` (multi-country / cross-cutting) | `endorsed` | `_crossrefs/corpus/demographics/observations/YYYY-MM-DD_{slug}.md` |
| `research_watch_item` | `open` (pending endorsement) | `_crossrefs/corpus/demographics/_pending/watch_YYYY-MM-DD_{slug}.md` |
| `research_watch_item` | `open` (endorsed) | `_crossrefs/corpus/demographics/watch_items/YYYY-MM-DD_{slug}.md` |

**Project cross-reference mechanism:**
For each project in `project_scope`, append a one-line entry to that project's
`_cross_references.md` index:

```
- YYYY-MM-DD — [Title](../../../_crossrefs/corpus/demographics/{path}) — [indicator(s)], [iso3], [scenario_implication]
```

If `_cross_references.md` does not exist in `GrandPlan/{Project}/docs/corpus/`, the
skill creates it on first use with a brief header explaining its role.

**Endorsement workflow:**
1. Drafts land in `_pending/` with `endorsed_by:` blank and
   `workflow_status: pending-endorsement`.
2. Anne (or another agent with documented domain authority for the specific
   indicator) reviews. Endorsement may be batched.
3. On endorsement: drafter (Claude Code) fills `endorsed_by: Anne`, updates
   `workflow_status: endorsed`, and moves the file from `_pending/` to the
   subfolder dictated by the routing table above.
4. Routine endorsement does **not** require a new build instruction (this would
   be too heavyweight for high-frequency monitoring). Endorsement is recorded
   in-frontmatter; the build instruction of record is the one that *created* the
   entry.
5. Watch-item **promotion** (status `open` → `promoted`) does require a build
   instruction per PROTO-RAG-001. The promoting agent (named in `promoted_by`)
   files the build instruction under
   `_crossrefs/_build_instructions/YYYY-MM-DD_demographics_promotion_{slug}.md`.

**Notification to Anne:**
On any new `_pending/` arrival, the skill appends a one-line entry to
`_crossrefs/corpus/demographics/_pending/_anne_inbox.md`. Anne's review cadence
is set outside this skill; the inbox file is the canonical queue.

---

## Scenario Discipline (standing reference)

The DFD fast-transition scenario discipline:

- Recent observed TFR values for LAC priority countries are the empirical baseline.
  **Anchor values and their sources are maintained in
  `_crossrefs/corpus/demographics/scenario_anchors.md`** and are not duplicated
  here, so revisions do not require editing this skill.
- CELADE medium-variant projections are **insufficient** as the Mexico OLG
  baseline — they are the optimistic scenario, not the central one.
- The fast-transition scenario is increasingly the baseline, not a stress test.
- Any incoming material that pushes observed TFR further below CELADE
  medium-variant strengthens the case for fast-transition calibration; classify
  it as `scenario_implication: fast-transition` or `baseline-revision`.

**Operational TODO:** `scenario_anchors.md` must be populated as part of the
corpus scaffold build instruction, with sourced values for at minimum `MEX`,
`CRI`, `COL`, `CHL`. Until then, classifications under §Step 2a referring to the
fast-transition scenario must explicitly cite the anchor source used in-note.

---

## Domain Authority

- **Anne** — domain authority for demographic classification, endorsement, and
  watch-item promotion decisions. All Tier-1 outputs route through Anne's
  endorsement queue.
- **Cath** — endorsement required when fiscal calibration implications are
  explicitly asserted (Step 2a's pension contribution rate question).
- **Beth** — endorsement required when BDH health-financing implications are
  explicitly asserted (Step 2b).
- **Debb** — executes corpus commit and knowledge-base integration on endorsed
  entries; also responsible for scaffold creation via build instruction.
- **Claude Code** — drafter of record (`added_by` / `opened_by`). Future
  automation of data retrieval from CELADE, CONAPO, UN WPP, Birth Gauge, INE.

---

## Key Standing References

- Fernández-Villaverde (2026): "The Demographic Future of Humanity" — primary
  scenario-discipline reference for fast-transition TFR framing
- UN WPP 2024 — official projection baseline (treat medium-variant as optimistic)
- CELADE — LAC-specific projections (treat medium-variant as optimistic for Mexico)
- Birth Gauge — high-frequency TFR tracking; useful for vintage comparison
- CONAPO — Mexico-specific demographic authority
- PROTO-RAG-001 (`_crossrefs/protocols/PROTO-RAG-001.md`) — governing protocol

---

## Cross-references

- → Governing protocol: `_crossrefs/protocols/PROTO-RAG-001.md`
- → Required scaffold build instruction (canonical filename, to be filed):
  `_crossrefs/_build_instructions/2026-MM-DD_demographics_corpus_initial.md`
- → Parallel corpus (template): `_crossrefs/corpus/inequality/README.md`
- → CLAUDE.md §7 (Scientific computing stack — Protocols and Corpus subsections)
- → CLAUDE.md §8 (Core Team — agent vocabulary)

## Revision history

- **v0.1** (initial, undated) — first draft. Did not conform to PROTO-RAG-001
  frontmatter schema; conflated artifact type with workflow status; assumed
  corpus scaffold without explicit prerequisite; DFD-centric Step 2; used
  `Claude` rather than `Claude Code`.
- **v0.2** (2026-05-16) — full audit pass. Conforms to PROTO-RAG-001 artifact
  types (`corpus_entry` and `research_watch_item`); adds prerequisite scaffold
  gate; resolves path contradiction via subfolder routing table; adds project
  cross-reference mechanism; splits Step 2 into per-project sub-blocks; adds
  Tier-1 / Tier-2 salience gate; adopts ISO-3166 alpha-3 geography; moves
  scenario anchors to a sourced separate file; standardizes drafter as
  `Claude Code`; adds explicit endorsement workflow.
