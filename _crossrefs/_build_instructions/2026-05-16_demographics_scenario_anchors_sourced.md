---
type: build_instruction
build_type: expansion
date: 2026-05-16
corpus_affected:
  - _crossrefs/corpus/demographics/scenario_anchors.md
  - _crossrefs/mission-project-map.md
triggered_by: "Anne's first-pass source-pinning of scenario_anchors.md per anne_scenario_anchors_brief.md (2026-05-16)."
agents_involved: [Anne, Claude Code, Héctor]
status: executed
sequence_position: "2_of_2"
notes: "Lifts the load-bearing dependency on Anne for the dfd-demographics-monitor skill v0.2 §Step 2a fast-transition / baseline-revision classifications. All five priority-country rows confirmed against primary sources. CELADE Observatorio Demográfico 2025 designated as the comparator baseline."
---

# Demographics scenario anchors — source-pinning expansion

**To:** Claude Code (Dalila session)
**From:** Anne (population economics, Core Team)
**Date:** 2026-05-16
**Re:** Record the first-pass source-pinning of `_crossrefs/corpus/demographics/scenario_anchors.md` and lift the load-bearing gate on the `dfd-demographics-monitor` skill v0.2 §Step 2a.

---

## 1. Scope and rationale

This is the sequence-position 2_of_2 follow-up to
`2026-05-16_demographics_corpus_initial.md`. That build created the
demographics corpus scaffold with `scenario_anchors.md` as a skeleton
(priority-country rows listed; values, vintages, and sources blank). Until
this expansion build executed, the skill was required to cite anchor sources
in-note rather than by reference to the anchor file.

Anne completed the source-pinning on 2026-05-16. Five of five priority-country
rows are confirmed against primary references. The file's frontmatter is
updated to `endorsed_by: Anne` and `workflow_status: endorsed`. The skill may
now cite the anchor file directly.

---

## 2. Anchor rows filed (verbatim)

| ISO-3 | Country | Observed TFR | Vintage | Source | CELADE OD 2025 (2024) | Status |
|---|---|---|---|---|---|---|
| MEX | Mexico      | 1.60 | 2023 | INEGI, ENADID 2023 (Comunicado 305/24, 22 mayo 2024). Survey-based; ENR 2024 reports registered-birth rates but does not retabulate TGF. | n/p in press release; OD 2025 Excel tables | confirmed |
| CRI | Costa Rica  | 1.12 | 2024 | INEC Costa Rica, Indicadores demográficos 2024 (Año 26, noviembre 2025). Ultra-low; below the 1.5 threshold since 2020. | 1.32 | confirmed |
| COL | Colombia    | 1.1  | 2024 preliminar | DANE, Boletín técnico EEVV Nacimientos 2024pr (26 marzo 2025). Historical minimum; final release pending. | n/p in press release; OD 2025 Excel tables | confirmed |
| CHL | Chile       | 1.03 | 2024 provisional | INE Chile, Boletín Demográfico Anual Provisional de Estadísticas Vitales 2024 (15 mayo 2025). 11.3% drop in births vs. 2023. | 1.14 | confirmed |
| PAN | Panama      | 1.8  | 2023 | INEC Panamá / Contraloría General, Estadísticas Vitales Vol. II — Nacimientos Vivos y Defunciones Fetales 2023 (publicado enero 2025). 2024 figure available in the INEC fertility-indicators dashboard but not yet in a tabulated release. | n/p in press release; OD 2025 Excel tables | confirmed |

`n/p in press release` indicates the country was not named in the OD 2025
press release (29 October 2025) with a specific comparator figure. The
underlying OD 2025 Excel tables tabulate every regional country and should be
consulted directly when the skill produces a classification that cites the
comparator for MEX, COL, or PAN.

---

## 3. CELADE revision decision

The CELADE comparator column in `scenario_anchors.md` uses the **CELADE
Demographic Observatory 2025** ("Low fertility in Latin America and the
Caribbean: emerging trends and dynamics," CEPAL/CELADE, released 29 October
2025). Underlying estimates align with the UN WPP 2024 revision and present a
CELADE 2024 estimate for every country in the region.

Rationale:

1. Most recent CELADE publication available at endorsement time.
2. Reports 2024 as the most recent CELADE estimate year. This aligns with the
   vintage of the observed-TFR column for CRI, COL, and CHL. For MEX (vintage
   2023) and PAN (vintage 2023), the optimism gap can still be read against
   the CELADE 2024 figure with a one-year offset noted in the row's source
   field.
3. Will be in force as the baseline reference until OD 2026 or a CELADE
   methodological note supersedes it. When a successor publication is
   released, a small expansion build will update the column.

Alternative considered and rejected: country-by-country revision choice
(e.g., MEX against CELADE OD 2022 because of the CELADE-CONAPO joint
projection cycle). Rejected because the cross-country comparability of the
optimism gap is more valuable than per-country revision fit, and because the
OD 2025 supersedes prior revisions on the same methodological basis.

The optimism-gap pattern in the two comparators visible from the press
release confirms the standing principle: CHL observed 1.03 vs. CELADE 1.14
(gap ~0.11); CRI observed 1.12 vs. CELADE 1.32 (gap ~0.20). CELADE
medium-variant estimates remain optimistic for LAC priority countries;
fast-transition is the empirical baseline, not a stress test.

---

## 4. Rows left missing

None. All five priority-country rows are `confirmed`.

Two open follow-ups, **not gating** the skill:

- Pull MEX, COL, PAN comparator values directly from CELADE OD 2025 Excel
  tables when the skill first fires a classification that needs them. Update
  the comparator column then via a small expansion build.
- Confirm Mexico's TGF for vintage 2024 if INEGI publishes a successor to
  ENADID 2023 or retabulates TGF in a 2024 ENR follow-up.
- Confirm Panama's TGF for vintage 2024 when INEC publishes the 2024
  Estadísticas Vitales volume (expected late 2025 / early 2026).

---

## 5. Per-artifact changes

### 5.1 — `_crossrefs/corpus/demographics/scenario_anchors.md`

Frontmatter updates:

- `endorsed_by: Anne` (was empty)
- `workflow_status: endorsed` (was `pending-endorsement`)

Body updates:

- §Anchors: five-row table replaced from the skeleton with the values in §2
  above; CELADE comparator column added per §11 of the 1_of_2 build
  instruction; status column transitions `missing → confirmed` for all five
  rows.
- §CELADE baseline: new section recording the OD 2025 choice and the gap
  pattern.
- §Operational status: replaced the "empty of values at scaffold creation"
  caveat with the current state.
- §Endorsement workflow: marked completed.
- §Cross-references: added back-link to this build instruction and to the
  source brief.

### 5.2 — `_crossrefs/mission-project-map.md`

Demographics Corpus block status line updated. The previous closing sentence
("Scenario anchors awaiting Anne's source-pinning ...") is replaced with a
status line reflecting completion. The block's headline status (Initial
scaffold (2026-05-16)) is preserved.

---

## 6. Execution checklist

- [x] Confirm `scenario_anchors.md` exists at expected path
- [x] Source the five priority-country TFR rows from primary references
- [x] Make CELADE revision decision (OD 2025) and document rationale
- [x] Update `scenario_anchors.md` frontmatter and body
- [x] Update `mission-project-map.md` Demographics Corpus block
- [x] File this build instruction at the expected path
- [x] Commit with the message format specified in the brief

---

## 7. Notes

- Anne's brief left three open judgment calls (CELADE revision choice;
  whether to add a sixth row for a non-priority country; whether to add a
  multi-year-average column). Resolution: (a) OD 2025 chosen per §3; (b) keep
  the anchor table strictly to the five priority countries — other countries
  cite source in-note indefinitely; (c) do not add a multi-year-average
  column at this pass — vintage clarity is more valuable than smoothing
  pandemic-year deflation, and none of the five confirmed values are
  obviously pandemic-distorted in the source publisher's own framing. Revisit
  if pandemic-year distortion shows up in a downstream classification.
- The asymmetry between MEX/PAN (vintage 2023) and CRI/COL/CHL (vintage 2024)
  reflects publication cadence, not data anomaly. MEX's most recent
  TGF-bearing release is the ENADID 2023 survey; the 2024 ENR is a
  registered-birth tabulation that does not retabulate TGF. PAN's most
  recent named-figure publication is the 2023 Estadísticas Vitales volume,
  released January 2025.
- Per Anne: the Costa Rica figure (1.12) and Chile figure (1.03) are
  load-bearing for the "ultra-low fertility" stratum that the skill's
  fast-transition scenario must recognize. These are below the 1.5
  ultra-low threshold conventionally used in CELADE's own framing.
- Build instruction sequence is closed. No further expansion anticipated
  unless a successor CELADE publication or a country-level TGF release
  triggers a small expansion build.

---

## 8. Cross-references

- → 1_of_2 (this build's antecedent): `_crossrefs/_build_instructions/2026-05-16_demographics_corpus_initial.md`
- → Source brief addressed to Anne: `_crossrefs/corpus/demographics/_pending/anne_scenario_anchors_brief.md`
- → Target file (updated by this build): `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Governing protocol: `_crossrefs/protocols/PROTO-RAG-001.md`
- → Governing skill: `_crossrefs/_skills/dfd-demographics-monitor/SKILL.md`
- → Cross-reference register: `_crossrefs/mission-project-map.md` Demographics Corpus block
