---
type: build_instruction
build_type: expansion
date: 2026-06-17
corpus_affected:
  - GrandPlan/DFD/research/fertility_collapse_abm/
  - _crossrefs/mission-project-map.md
triggered_by: "Stage 1 of the four-stage rapid-fertility-collapse ABM paper (Anne + Nina). Originating instruction: GrandPlan/DFD/research/fertility_collapse_abm/STAGE1_data_acquisition_fertility_collapse.md (v1.1, 2026-06-17). Data acquisition + forensic QA only; hard gate before any modeling."
agents_involved: [Anne, Nina, Claude Code, Debb]
status: executed
sequence_position: "1_of_1"
notes: "Hard gate: Anne + Nina review STAGE1_forensic_memo.md before Stage 2 (ABM specification) begins. Two memo-assumption corrections surfaced and are load-bearing downstream: (1) Colombia DANE TFR is 1.7->1.1, NOT the spec's 2.0->1.06; (2) Argentina's INDEC 2007-15 break does NOT contaminate the fertility signal (vital stats are DEIS, a separate institution). Stage-2 follow-ups: annual coupling 20-39 path (microdata), full Bongaarts-Feeney, Colombia 2024 ASFR vector, Census-2022 denominator rebasing."
---

# Fertility-Collapse ABM — Stage 1 Data Acquisition & Forensic Memo (Build Record)

**To:** provenance archive (Debb)
**From:** Claude Code (execution), on the Stage 1 instruction authored by Anne + Nina
**Date:** 2026-06-17 (execution completed 2026-06-18)
**Re:** Record the Stage 1 data product and forensic memo for the parallel DFD research
paper on rapid fertility collapse in Latin America.

---

## 1. Scope and rationale

Standalone working paper (parallel DFD research): a threshold-coupling agent-based model
of rapid fertility collapse (TFR ~2.0 → ~1.0 in ~6 years) in Colombia, Argentina, Chile,
and Costa Rica, with Mexico as the slower-decline comparator. **Stage 1 is data acquisition
and forensic quality assessment ONLY** — no modeling. This build records what was executed
against the Stage 1 instruction and registers the data product per PROTO-RAG-001.

The data product lives at `GrandPlan/DFD/research/fertility_collapse_abm/` to keep the
provenance chain inside DFD (per the instruction's placement note). A draft-stage
cross-reference from `Research/working-papers/` is deferred until the paper reaches draft.

## 2. What was executed

- **World Bank WDI backbone** (`data/worldbank/`, 61 CSVs + fetch log): long consistent
  TFR, CBR, population, migration, and Calles-Vogl covariates (education, agriculture share,
  urbanization, female LFP) for 5 countries, 1960–2024. Flagged: WB/WPP smooths away the
  2020–24 collapse tail.
- **National-source series** (`data/national/`, 26 CSVs): national TFR, births, GFR, ASFR,
  coupling endpoints, and the INDEC female-15–49 denominator — from DANE, INE Chile,
  DEIS/INDEC, INEC-CR, INEGI/CONAPO. The collapse tail invisible in WB.
- **Forensic Checks 1–5** executed per country (splicing, provisional, census level-effects,
  births-vs-TFR cross-check, tempo-vs-quantum). Implied-TFR reconstruction + INDEC-pinned
  Argentina extension (2024 ≈ 1.15–1.19).
- **Deliverables:** `STAGE1_forensic_memo.md` (primary), `STAGE1_provenance.md`,
  `STAGE1_crosscheck_check4.csv`, `STAGE1_check5_tempo_quantum.csv`, 11 charts, reproducible
  scripts (`_acquire_worldbank.py`, `_build_national.py`, `_crosscheck_and_charts.py`,
  `_births_implied_charts.py`, `_argentina_indec_pin.py`, `_build_asfr_coupling.py`,
  `_colombia_asfr.py`). PROTO-RAG-001 frontmatter via the provenance log + per-directory READMEs.

## 3. Findings of record (for the gate)

- Collapse is **behavioral, not artifact** in all four collapse countries: raw births fell
  18–47% while women 15–49 grew (Check 4). Tempo/postponement-dominant decline (Check 5).
- All five countries' headline figures independently source-verified; zero material discrepancies.
- See §1 notes (frontmatter) for the two memo-assumption corrections.

## 4. Provenance discipline

- Identification discipline maintained: covariate **inputs** (`data/worldbank/`) kept strictly
  separate from the TFR **output** series (`data/national/`); no covariate tuned to fit TFR.
- Every value carries a source; NOT-FOUND items left as gaps (no estimation). Full URL/access
  log in `STAGE1_provenance.md`.

## 5. Status

`status: executed`. Awaiting Anne + Nina gate review of `STAGE1_forensic_memo.md`. No Stage 2
(ABM specification) work has begun.
