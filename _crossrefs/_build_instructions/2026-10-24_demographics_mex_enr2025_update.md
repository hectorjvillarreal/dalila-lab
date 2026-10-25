---
type: skill_invocation
project_scope: [DFD, BDH]
workspace: "demographics corpus (cross-project)"
title: "Mexico demographics update — ENR 2025 (INEGI Comunicado 87/26)"
target: Claude Code (Dalila)
date_added: 2026-10-24
added_by: Héctor (in-session request)
endorsed_by:                      # note is pending-anne on production
skill: dfd-demographics-monitor
status: executed
---

# Mexico demographics update — ENR 2025
# Target: Claude Code (Dalila) · Skill: dfd-demographics-monitor

## 0. What this is

Héctor asked in-session (2026-10-24) whether demographics needed updating. A
sweep found INEGI's ENR 2025 (25 Sep 2026), released two days after the last
corpus cycle (09-23) and not yet filed. Héctor authorized filing it the same
day.

## 1. Discriminator ruling (applied)

**DATA RELEASE (registered-birth tabulation), not a TFR release and not a
projection revision.** Consequences:

- Tier-1 `corpus_entry`, `tier: data_source`, routed to `_pending/`. Pending Anne.
- `scenario_anchors.md` untouched; MEX instructions untouched (v1.6 stands,
  v1.7 queue unchanged); no trigger defined on this series fires.
- Endorsed predecessors (ENR 2024 entry, Q3 replicate) are **not amended**.
  The methodological flag goes to Anne through the entry.

## 2. The source (verified 2026-10-24)

- INEGI, **Comunicado de prensa 87/26** and **Reporte de Resultados 38/26**,
  "Estadística de Nacimientos Registrados (ENR) 2025", 25 de septiembre de 2026.
- Headline: **1,678,532 registered births in 2025** (+0.4%); rate **47.7** per
  1,000 women 15–49 (unchanged).
- Load-bearing table: RR Table 1, registration year × year of occurrence,
  2016–2025. Same-year registrations 1,058,332 (−2.6%).

## 3. What the run produced

| Artifact | Path |
|---|---|
| Corpus entry (Tier-1, pending) | `_crossrefs/corpus/demographics/_pending/2026-10-24_inegi-enr2025-mex-births.md` |
| Source PDFs | `_crossrefs/corpus/demographics/sources/INEGI_2026-09-25_ENR2025_CP-87-26.pdf`, `…_RR-38-26.pdf` |
| Table 1 transcription (row sums and column totals verified) | `_crossrefs/corpus/demographics/sources/INEGI_2026-09-25_ENR2025_RR-38-26_tabla1.csv` |
| Anne inbox line | `_crossrefs/corpus/demographics/_pending/_anne_inbox.md` |
| This build instruction | `_crossrefs/_build_instructions/2026-10-24_demographics_mex_enr2025_update.md` |

## 4. Load-bearing finding for DFD

The flat headline is composition. Registrations of people born before 2016
rose from 103,633 to 163,076, while every occurrence-based margin kept
falling: same-year −2.6%, born-2016-or-later −3.4%. Two Q4 consequences go to
Anne: (a) do not roll the Q3 registered-rate proxy forward, and rebuild it on
occurrence; (b) the Rule-of-85 anchor depends on the registration basis. The
occurrence basis gives an illustrative ≈109–112 M at e₀ = 75 against
125.4–125.9 M registered. Nothing is re-pinned.

## 5. Still open after this run (carried to the Q4 replicate)

1. Anne's ruling on the occurrence vs registered basis (proxy and Rule-of-85).
2. RR annex Table 3: state concentration of the pre-2016 registration jump.
3. INEGI EDR 2025 definitive deaths (due November 2026). Feeds the v1.7
   mortality item.
4. CELADE Observatorio Demográfico 2026 (expected ~end Oct). MEX comparator,
   fourth carry.
5. The v1.7 queue items as listed in the MEX instructions.

## 6. Cross-references

- → Produced corpus entry: `_crossrefs/corpus/demographics/_pending/2026-10-24_inegi-enr2025-mex-births.md`
- → Predecessor build instruction: `_crossrefs/_build_instructions/2026-08-03_demographics_mex_enr2024_update.md`
- → Q3 replicate: `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q3_demographic_replicate.md`
- → Governing skill: `_crossrefs/_skills/dfd-demographics-monitor/SKILL.md`
- → Governing protocol: `_crossrefs/protocols/PROTO-RAG-001.md`
