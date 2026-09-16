---
type: skill_invocation
project_scope: [DFD, BDH]
workspace: "demographics corpus (cross-project)"
title: "Mexico demographics update — ENR 2024 definitive (INEGI Comunicado 129/25)"
target: Claude Code (Dalila)
date_added: 2026-08-03
added_by: Héctor (in-session request)
endorsed_by:                      # note is pending-anne on production
skill: dfd-demographics-monitor
status: executed
---

# Mexico demographics update — ENR 2024 definitive
# Target: Claude Code (Dalila) · Skill: dfd-demographics-monitor

## 0. What this is

Héctor asked in-session (2026-08-03) to update the Mexican demographics. The
2026-Q2 replicate left four Mexico data follow-ups targeted for July 15, 2026
(Q3), all overdue at invocation. This run swept for post-Q2 publications,
found the ENR 2024 definitive release, and produced a Tier-1 monitoring note.

## 1. Discriminator ruling (applied)

**DATA RELEASE (registered-birth tabulation), not a TFR release and not a
projection revision.** Consequences:

- Tier-1 `corpus_entry`, `tier: data_source`, routed to `_pending/` per the
  skill's routing table. Pending Anne.
- `scenario_anchors.md` is **untouched**. The MEX anchor row (TFR 1.60,
  vintage 2023, ENADID 2023) already carries the note "ENR 2024 reports
  registered-birth rates but does not retabulate TGF" — the definitive
  comunicado confirms that note verbatim. The anchors file's open follow-up
  "Confirm Mexico's TGF for vintage 2024" is resolved **negative** for this
  release cycle: no 2024 TGF exists yet.
- No Revision Transition Protocol; no re-baseline; WPP 2024 / CELADE OD 2025
  remain the projection references.

## 2. The source (verified 2026-08-03)

- INEGI, **Comunicado de prensa 129/25**, "Estadística de Nacimientos
  Registrados (ENR) 2024", 25 de septiembre de 2025 (cifras definitivas).
  Companion Reporte de Resultados 34/25.
- Headline: **1,672,227 registered births in 2024**; rate **47.7** per 1,000
  women 15–49 (−4.5 vs. 2023).

## 3. What the run produced

| Artifact | Path |
|---|---|
| Corpus entry (Tier-1, pending) | `_crossrefs/corpus/demographics/_pending/2026-08-03_inegi-enr2024-mex-births.md` |
| Anne inbox line | `_crossrefs/corpus/demographics/_pending/_anne_inbox.md` |
| Tier-2 acquisition-queue entry (CONAPO mid-2026 projections press) | `_crossrefs/corpus/demographics/_acquisition_queue.md` |
| This build instruction | `_crossrefs/_build_instructions/2026-08-03_demographics_mex_enr2024_update.md` |

## 4. Load-bearing finding for DFD

The 2026-Q2 replicate §10 set an explicit trigger: *"If 2024 INEGI SINAC
reports annual births below 1.7 M (a >7% drop from 2023), the long-run
stationary population falls into the 120–135 M range, materially below the
central-scenario 2050 projection."* **The trigger fired**: 1.672 M is a
−8.2% drop. Details and Rule-of-85 recomputation in the corpus entry §DFD.

## 5. Still open after this run (carried to the Q3 replicate)

1. CELADE OD 2025 Excel extraction — MEX 2024 comparator (also COL, PAN).
2. INEGI ENOE coupling rate among 20–39 (carried from Q2).
3. CONAPO life tables to replace stylized Coale-Demeny West.
4. Mexico 2024/2025 TGF — no INEGI publication yet; anchor stays 1.60 (2023).
5. The Q3 quarterly replicate itself (target was 2026-07-15; overdue).

## 6. Cross-references

- → Produced corpus entry: `_crossrefs/corpus/demographics/_pending/2026-08-03_inegi-enr2024-mex-births.md`
- → Q2 baseline replicate: `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q2_demographic_replicate.md`
- → Scenario anchors (unchanged by this run): `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Governing skill: `_crossrefs/_skills/dfd-demographics-monitor/SKILL.md`
- → Governing protocol: `_crossrefs/protocols/PROTO-RAG-001.md`
