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
