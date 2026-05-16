# Anne — TFR scenario anchors source-pinning brief

**To:** Anne (population-economics domain authority)
**From:** Claude Code, on Héctor's instruction
**Date opened:** 2026-05-16
**Target file:** `_crossrefs/corpus/demographics/scenario_anchors.md`
**Upstream build instruction:** `_crossrefs/_build_instructions/2026-05-16_demographics_corpus_initial.md` (sequence_position 1_of_2, executed)
**Drives:** sequence_position 2_of_2 expansion build instruction (filed by Anne on completion)
**Project scope:** DFD, BDH, Aurora
**Priority:** load-bearing — gates the `dfd-demographics-monitor` skill's fast-transition / baseline-revision classifications under §Step 2a

> This file is operational coordination, not a corpus artifact. PROTO-RAG-001
> frontmatter is omitted by design (matches the `_anne_inbox.md` precedent).

## What's needed

Populate `_crossrefs/corpus/demographics/scenario_anchors.md` priority-country
rows (MEX, CRI, COL, CHL, PAN) with **recent observed TFR**, **vintage year**,
and **institutional source**. Then update the file's frontmatter to record
your endorsement, and a sequence_position 2_of_2 build instruction is filed
to record the population.

Until this completes, the `dfd-demographics-monitor` skill's fast-transition
and baseline-revision classifications must cite anchor sources in-note rather
than by reference to the anchor file (per §5 of
`2026-05-16_demographics_corpus_initial.md` and §Operational status of the
target file).

## Sourcing rules (from build instruction §11 and skill §Scenario Discipline)

1. **CELADE medium-variant projections are the optimistic scenario** for LAC
   priority countries, not the central one. Observed recent TFR is the
   empirical baseline. The fast-transition scenario is increasingly the
   baseline, not a stress test.
2. **Primary sources only** for the anchor row itself: vital registries,
   census, UN WPP, CELADE, CONAPO, INE. Examples of acceptable source
   specificity:
   - "CONAPO Proyecciones 2018–2070, revisión 2023"
   - "INE Chile, Estadísticas Vitales 2024 preliminar"
   - "UN WPP 2024 medium variant"
   - "INEGI Estadísticas de Natalidad 2024"
   Avoid bare "UN data" or "OWiD" as the row source. Secondary aggregators
   may corroborate but should not be the primary citation.
3. **Vintage matters.** Use the most recent observation that the source itself
   labels as observed (not projected). Provisional / preliminary releases are
   acceptable if flagged in the source — note that in the row.
4. **Per-country judgment.** If a country's most recent observation is
   anomalous (pandemic-year deflation, partial vital-registration coverage),
   prefer a multi-year average and note the choice in the row's source field.
5. **CELADE comparator column.** Once primary rows are confirmed, add a
   second column for the CELADE medium-variant value for the *same vintage
   year* to make the optimism gap visible. Specify which CELADE revision is
   in force as the baseline reference (e.g., "Revisión 2022", "Revisión 2024").

## Endorsement workflow (from §5 of the build instruction)

1. Populate each row. Status column transitions `missing → confirmed`.
2. Update frontmatter: `endorsed_by: Anne`, `workflow_status: endorsed`.
3. File a follow-up build instruction at
   `_crossrefs/_build_instructions/2026-MM-DD_demographics_scenario_anchors_sourced.md`
   with `build_type: expansion`, `sequence_position: "2_of_2"`, and
   `triggered_by: "Anne's first-pass source-pinning of scenario_anchors.md
   per anne_scenario_anchors_brief.md (2026-05-16)."` It should record the
   five anchor rows verbatim and reference this brief.
4. Update the mission-project-map.md Demographics Corpus block to drop the
   "scenario anchors awaiting Anne's source-pinning" caveat once the
   follow-up build instruction is filed.

## Open judgment calls for Anne

- Which CELADE revision to designate as the baseline comparator (2022? 2024?
  Country-by-country?)
- Whether to add a sixth row for a non-priority country that shows up
  frequently in monitoring (e.g., Argentina, Brazil) — or keep the anchor
  table strictly to the five priority countries and let other countries
  cite source in-note indefinitely.
- Whether multi-year averages (e.g., 2022–2024 mean) deserve their own column
  alongside the single most-recent observation.

## Cross-references

- → Target file: `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Build instruction: `_crossrefs/_build_instructions/2026-05-16_demographics_corpus_initial.md`
- → Governing skill: `_crossrefs/_skills/dfd-demographics-monitor/SKILL.md` §Scenario Discipline
- → Standing reference for fast-transition framing: Fernández-Villaverde (2026), "The Demographic Future of Humanity"
- → Inbox log: `_crossrefs/corpus/demographics/_pending/_anne_inbox.md`
