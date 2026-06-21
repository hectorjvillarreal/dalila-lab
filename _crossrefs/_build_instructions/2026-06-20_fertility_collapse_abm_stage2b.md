---
type: build_instruction
build_type: expansion
date: 2026-06-20
corpus_affected:
  - GrandPlan/DFD/research/fertility_collapse_abm/model/
  - GrandPlan/DFD/research/fertility_collapse_abm/model/outputs/stage2b/
triggered_by: "Stage 2b of the rapid-fertility-collapse ABM paper (Anne-led): the demographic-measurement leg of question (A), compositional-vs-cascade discrimination. Originating instruction: GrandPlan/DFD/research/fertility_collapse_abm/model/STAGE2b_compositional_cascade_instruction.md (drafted by Claude 2026-06-20 on Héctor's instruction, following Anne's mandate; §5 amended per Anne's adjudication 2026-06-20). Gated by STAGE2b_Anne_endorsement.md (conditions 1-6)."
agents_involved: [Anne, Nina, Claude Code, Debb, Héctor]
status: executed
sequence_position: "2b_of_4 (Stage 2 parallel track; gates Stage 3 + question B)"
notes: "Calibrated verdict: NOT H_cascade in either CR or COL. β > 0 (stabilizing) under every reference spec, both countries — no amplifying state-dependence. CRI H_cohort-leaning (period effect insignificant, p=0.18); COL H_shock + cohort component (period effect present p≈3e-6 but non-reflexive). (B) reflexive self-reinforcement NOT warranted. TWO load-bearing items for Anne's endorsement: (1) the read (STAGE2b_compositional_cascade_memo.md) is pending her sign-off — instruction's endorsed_by stays blank until then; (2) B7 CORRECTION surfaced and logged, not silently absorbed — both βs are ECOLOGICAL (Task C is a within-cohort cell test on repeated cross-sections; neither country observes individual transitions), deviating from Anne's 'COL individual-level' wording; awaits her ruling. Standing caveat that could overturn the non-cascade read: the 20-39 floor excludes the 15-19 entry margin (the cascade vanguard)."
---

# Fertility-Collapse ABM — Stage 2b Compositional-vs-Cascade Discrimination (Build Record)

**To:** provenance archive (Debb)
**From:** Claude Code (execution), on the Stage 2b instruction (Héctor's instruction,
Anne's demographic mandate; §5 amended per Anne's adjudication)
**Date:** 2026-06-20 (conditions 1-6 implemented + calibrated run 2026-06-20/21)
**Re:** Record the Stage 2b demographic-measurement read and its provenance for the
parallel DFD paper on rapid fertility collapse.

---

## 1. Scope and rationale

The Stage 2 skeleton ABM reproduces the marriage collapse but cannot say *why*. Stage 2b
is the **demographic measurement** that discriminates a within-cohort reflexive **cascade**
(H_cascade) from **cohort-replacement** (H_cohort) and an **exogenous period shock**
(H_shock) — the answer determining whether Nina's (B) reflexive-feedback build is
structurally warranted. Pseudo-panel work on in-hand series only (CR ENAHO REDATAM
aggregates 2010-2024; COL GEIH 2007-2024; MEX comparator). CPU/Python. **Does not build,
alter, or calibrate the ABM.**

## 2. What was executed

- **Instruction + pre-registration** (`STAGE2b_compositional_cascade_instruction.md`):
  hypotheses §2, pre-registered decision rule §5, identification wall (TFR comparison-only).
- **Anne's adjudication** (`STAGE2b_Anne_endorsement.md`): §2 endorsed; §5 amended (sign-based
  bar; `peer_older` added; substantive cuts); six execution conditions set.
- **Conditions 1-6 implemented (Claude):**
  - `stage2b_apc_composition.py` — Task A birth-year-bin pseudo-cohorts (year − band_lower,
    not midpoint); Task B curvature within fixed bands (Lexis) + net of age FE; windows
    2015-24 & 2018-24; entry cohorts birth ≥ 1990.
  - `stage2b_state_dependence.py` — Task C sharp test; `peer_younger` (primary), `peer_older`
    (clean), `pop2039` (robustness), `own_lag` (comparator); full β matrix; ecological tag.
  - `stage2b_b6_repro_diff.py` — B6 reproduction diff vs Stage 1.5 coupling series (halts on
    mismatch).
  - `stage2b_figures.py` — within-band-segmented fig-1 (sawtooth removed) + APC curvature +
    β-CI; TFR overlay comparison-only (fig-1).
- **Deliverables:** `STAGE2b_compositional_cascade_memo.md` (the read, §5 applied),
  `outputs/stage2b/` (composition panels, APC/Lexis contrasts, β matrix, regression tables,
  figure data + PNGs, `_assert_no_tfr.log`). Reader aids on `main`: handoff, endorsement,
  read-pointer.

## 3. Findings of record (for the gate)

- **Not H_cascade.** β > 0 (stabilizing) for every clean spec and both countries; lag-2
  collapses to ≈0; no amplifying (β<0) state-dependence anywhere. (B) not warranted.
- **Per country:** CRI H_cohort-leaning (period-effect F-test insignificant); COL H_shock +
  cohort component (significant period effect, but non-reflexive).
- **B7 correction:** both βs ecological (cell-level on repeated cross-sections); CR/COL
  asymmetry is in cell construction (REDATAM aggregates vs DANE microdata), not estimator
  level. Logged for Anne's ruling; does not change the sign-based verdict.

## 4. Provenance discipline

- **Identification wall** maintained and machine-verified: TFR never a regressor/weight/tuner;
  `assert_no_tfr()` audit trail filed (`_assert_no_tfr.log`, 25 PASS / 0 VIOLATION); TFR read
  only for the fig-1 comparison overlay.
- **Band/base consistency** (B6) proven: 2b composition reproduces the Stage 1.5 coupling
  series on all overlapping cells (married/cohabiting exact; union_total within rounding).
- `w` (fertility-intensity ratio) untouched; intensity leg deferred to 2c (gated on
  acquisitions). No data acquired — in-hand series only.

## 5. Status

`status: executed`. Calibrated run complete on the Anne-adjudicated methodology. The
instruction's `endorsed_by` stays **blank** pending Anne's endorsement of the read and her
ruling on the B7 correction; Debb writes `endorsed_by: Anne` once both clear. Endorsement
unblocks Stage 3 (four-country nesting + GPU sweep) and **closes** (B) reflexive feedback
unless the 15-19 entry-margin caveat or Southern Cone (ARG/CHL) identification overturns the
non-cascade read. No Stage 3 or (B) work has begun.
