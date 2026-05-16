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
