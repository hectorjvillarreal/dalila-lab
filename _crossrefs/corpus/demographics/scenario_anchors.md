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
endorsed_by: Anne
build_instruction: "_crossrefs/_build_instructions/2026-05-16_demographics_corpus_initial.md"
workflow_status: endorsed
---

# Scenario anchors — observed recent TFR for LAC priority countries

## Purpose

Single source of anchor values for the scenario classification dimension of the
`dfd-demographics-monitor` skill. Entries here are cited by individual corpus
entries rather than duplicated; revisions flow through this file.

## Anchors

CELADE comparator column reports the CELADE Demographic Observatory 2025
(October 2025; CELADE estimate for 2024, embedding UN WPP 2024 revision) value
for the country, where published. See §CELADE baseline below for the revision
choice rationale.

| ISO-3 | Country | Observed TFR | Vintage | Source | CELADE OD 2025 (2024) | Status |
|---|---|---|---|---|---|---|
| MEX | Mexico      | 1.60 | 2023 | INEGI, ENADID 2023 (Comunicado 305/24, 22 mayo 2024). Survey-based; ENR 2024 reports registered-birth rates but does not retabulate TGF. | n/p in press release; OD 2025 Excel tables | confirmed |
| CRI | Costa Rica  | 1.12 | 2024 | INEC Costa Rica, Indicadores demográficos 2024 (Año 26, noviembre 2025). Ultra-low; below the 1.5 threshold since 2020. | 1.32 | confirmed |
| COL | Colombia    | 1.1  | 2024 preliminar | DANE, Boletín técnico EEVV Nacimientos 2024pr (26 marzo 2025). Historical minimum; final release pending. | n/p in press release; OD 2025 Excel tables | confirmed |
| CHL | Chile       | 1.03 | 2024 provisional | INE Chile, Boletín Demográfico Anual Provisional de Estadísticas Vitales 2024 (15 mayo 2025). 11.3% drop in births vs. 2023. | 1.14 | confirmed |
| PAN | Panama      | 1.8  | 2023 | INEC Panamá / Contraloría General, Estadísticas Vitales Vol. II — Nacimientos Vivos y Defunciones Fetales 2023 (publicado enero 2025). 2024 figure available in the INEC fertility-indicators dashboard but not yet in a tabulated release. | n/p in press release; OD 2025 Excel tables | confirmed |

`n/p in press release` = not published as a named country figure in the 2025
press release; the underlying CELADE OD 2025 Excel tables tabulate every
country and should be consulted directly when the skill produces a
classification that cites the comparator for MEX, COL, or PAN.

## CELADE baseline

The comparator column uses **CELADE Demographic Observatory 2025** (CEPAL,
released 29 October 2025; "Low fertility in Latin America and the Caribbean:
emerging trends and dynamics"). Underlying estimates align with the UN WPP
2024 revision and present a CELADE 2024 estimate for every country in the
region.

Rationale:

1. Most recent CELADE publication available at endorsement time.
2. Reports 2024 as the most recent CELADE estimate year, aligning with the
   vintage of the observed-TFR column for CRI, COL, and CHL. For MEX (2023)
   and PAN (2023), the optimism gap can still be read against the CELADE 2024
   figure with one-year offset noted in the source line.
3. Will be in force as the baseline reference until OD 2026 or a CELADE
   methodological note supersedes it.

The optimism-gap pattern is visible where comparators are present: CHL
observed 1.03 vs. CELADE 1.14 (gap ~0.11); CRI observed 1.12 vs. CELADE 1.32
(gap ~0.20). Confirms the standing principle that CELADE medium-variant
estimates are optimistic for LAC priority countries; fast-transition is the
empirical baseline.

## Operational status

First-pass source-pinning complete (5 of 5 rows confirmed). Endorsed by Anne
on 2026-05-16. The skill may cite this file as the canonical anchor reference
for fast-transition and baseline-revision classifications under §Step 2a.
In-note citation remains acceptable as a provenance practice.

Open follow-ups (not gating):

- Pull MEX, COL, PAN comparator values directly from CELADE OD 2025 Excel
  tables when the skill first fires a classification that needs them; update
  the comparator column then.
- Confirm Mexico's TGF for vintage 2024 if INEGI publishes a successor to
  ENADID 2023 or retabulates TGF in a 2024 ENR follow-up.
- Confirm Panama's TGF for vintage 2024 when INEC publishes the 2024
  Estadísticas Vitales volume (expected late 2025 / early 2026).

## Endorsement workflow

Completed.

1. Rows populated with TGF, vintage, and specific institutional source.
   Status `confirmed` for all five.
2. Frontmatter updated: `endorsed_by: Anne`, `workflow_status: endorsed`.
3. Follow-up build instruction
   (`2026-05-16_demographics_scenario_anchors_sourced.md`, sequence_position
   2_of_2) records the population and endorsement as `build_type: expansion`.

## Cross-references

- → Build instruction (initial scaffold): `_crossrefs/_build_instructions/2026-05-16_demographics_corpus_initial.md`
- → Build instruction (source-pinning): `_crossrefs/_build_instructions/2026-05-16_demographics_scenario_anchors_sourced.md`
- → Source brief: `_crossrefs/corpus/demographics/_pending/anne_scenario_anchors_brief.md`
- → Governing skill: `_crossrefs/_skills/dfd-demographics-monitor/SKILL.md` §Scenario Discipline
- → Fernández-Villaverde (2026) "The Demographic Future of Humanity" (standing reference for fast-transition framing)
