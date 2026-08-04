---
type: skill_invocation
project_scope: [DFD, BDH]
workspace: "demographics corpus — country/MEX quarterly replicates"
title: "2026-Q3 demographic replicate — México (quarterly protocol run)"
target: Claude Code (Dalila)
date_added: 2026-08-03
added_by: Héctor (in-session request)
endorsed_by:                      # replicate is pending Anne + Cath on production
skill: dfd-demographics-monitor
status: executed
---

# 2026-Q3 demographic replicate — build instruction of record

## 0. What this is

Héctor requested the Q3 quarterly replicate in-session on 2026-08-03,
immediately following the ENR 2024 update run
(`2026-08-03_demographics_mex_enr2024_update.md`). The replicate was
produced early in the Q3 reference period (protocol target: October 15,
2026) under governing instructions v1.3.

This file exists per **option (a)** of the Q2 replicate's §8 conformance
note (per-quarter build instruction), adopted **provisionally** — the
(a)-vs-(b) policy decision remains with Anne / Debb.

## 1. What the run retrieved (data cutoff 2026-08-03)

| Input | Outcome |
|---|---|
| Annual births | ENR 2024 definitive, 1,672,227 (−8.2%) — from the same-day ENR corpus entry |
| Period TFR | Anchor unchanged (1.60/2023); new registered-births proxy ≈1.46 (2024) |
| Coupling proxy | Partial: ENOE-based situación conyugal 2005→2025 + EAP Juventud 2025 |
| e₀ | CONAPO 2026: 75.63 (F 79.24 / M 72.75) — validates stylized 75 |
| WPP revision check | No WPP 2026; next revision postponed to 2027; WPP 2024 stands |
| CELADE comparator | Still pending — OD 2025 annex retrieval attempted, not completed |
| Net migration, life tables, 5-yr age structure | Not retrieved; carried to Q4 |

## 2. What the run produced

- `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q3_demographic_replicate.md`
  (pending Anne + Cath)
- Anne inbox line in `_crossrefs/corpus/demographics/_pending/_anne_inbox.md`
- This build instruction

## 3. Decisions taken in-run (flagged for endorsement)

1. **No re-anchor.** The ≈1.46 implied-TFR proxy is reported as directional
   signal only; an explicit re-anchor trigger (published TGF ≤ 1.50) is
   armed and routed to Anne.
2. **Scenario tables carried forward unchanged** — no cohort-component
   input changed this quarter.
3. **Rule-of-85 anchor superseded**: 136.5 M (Q2) → 125.4–126.5 M on 2024
   births.
4. **Tempo-corrected column stays non-operational** — both promotion
   conditions unmet; this quarter's evidence points the other way.

## 4. Cross-references

- → Produced replicate: `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q3_demographic_replicate.md`
- → Same-day antecedent: `_crossrefs/_build_instructions/2026-08-03_demographics_mex_enr2024_update.md`
- → Governing instructions: `_crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md` (v1.3)
- → Governing skill: `_crossrefs/_skills/dfd-demographics-monitor/SKILL.md`
- → Governing protocol: `_crossrefs/protocols/PROTO-RAG-001.md`
