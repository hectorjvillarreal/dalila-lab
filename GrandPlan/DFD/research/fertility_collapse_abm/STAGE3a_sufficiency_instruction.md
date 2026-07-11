---
type: build_instruction
stage: 3a
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led) → modeling seam (Nina)"
title: "Collapse paper — resume & advance: Stage 3a sufficiency (no-reflexivity, composition target)"
target: "Claude Code — run on Claude Fable 5"
date_added: 2026-07-11
added_by: "Claude (Debb, carrying Anne's verdicts + Nina's remit)"
endorsed_by:                      # pending Nina (build) — Anne's demographic verdicts are INPUTS, not re-litigated here
depends_on:
  - "STAGE2b_compositional_cascade_memo.md + STAGE2b_Anne_read_signoff.md (no-cascade; cohort-replacement)"
  - "STAGE2c_col_individual_memo.md + STAGE2c_Anne_read_signoff.md (aggregation-cleared)"
  - "STAGE2_calibration_results.md (the skeleton this respecifies; ~55% magnitude, glide)"
  - "SDT_framing_note_for_Anne.md (channel-assisted compression framing)"
compute: "Julia / Agents.jl, CPU-parallel (as the skeleton). GPU only if a parameter sweep is added. Session model: Claude Fable 5."
status: "ACTIONABLE NOW (in-hand CR/COL composition data). The one ungated forward thread."
---

# Collapse Paper — Resume & Advance
# Stage 3a: Sufficiency of the surviving mechanism
# Run on Claude Fable 5

## 0. Catch-up — state after the 3-week gap (as of 2026-07-11)

- **Verdict (settled, endorsed):** no within-cohort reflexive cascade. The collapse is
  **cohort-replacement** — COL cohort-dominant with a secondary *exogenous* period overlay;
  CRI cohort-by-residual (underpowered). Endorsed by Anne across 2b (cell-level) and 2c-i
  (individual-outcome; ecological objection discharged).
- **(B) reflexive feedback:** DEFERRED, aggregation-cleared, pending ENDS — **not closed, not
  warranted.** Do not add reflexivity to any model here.
- **Framing:** SDT frame endorsed — *channel-assisted compression* (pre-existing consensual-union
  base as the speed mechanism); cohort-diffusion ↔ cohort-dominance convergence is the lead.
- **Three forward threads:** (i) ENDS 2c-ii — data-gated; (ii) ARG/CHL external validity —
  data-gated; (iii) **Stage 3 sufficiency — buildable now.** This file advances (iii).
- **Identification wall** and **frozen invariants** carry over unchanged.

## 1. What Stage 3a asks

The 2b skeleton (with a coordination threshold) hit only ~55% of observed magnitude and produced
a **glide**, not the observed acceleration. The threshold is now empirically rejected. So the
question is sufficiency of what *survived*:

> **Can a no-reflexivity model — cohort-entry heterogeneity + an exogenous period shock —
> reproduce the observed marriage-share (composition) collapse in CR and COL: its magnitude and
> its 2015–2024 shape, including the late acceleration?**

3a targets **composition** (the state variable, in-hand). It does **not** target TFR magnitude —
that needs `w` and rides with ENDS (Stage 3b, gated). Keep the two separate.

## 2. Inherited discipline (do not violate)

- **No reflexivity.** The transition rule must contain **no** reference-group self-reinforcement.
  2b/2c rejected it. A model that reintroduces it is off-spec.
- **Identification wall.** TFR is comparison-only overlay; never enters the loss; `assert_no_tfr()`
  carried over, log to `outputs/stage3a/`.
- **Composition state** {single, cohabiting, married}. `w` / fertility intensity is **not** a 3a
  object (gated to ENDS).
- **Anne's verdicts are inputs, not decisions to revisit here.** The demographic structure
  (cohort-replacement + exogenous overlay, no cascade) is given.

## 3. The model — respecify the skeleton

Start from `cri_skeleton_abm.jl`. Two changes:
1. **Remove** the coordination-norm threshold mechanism entirely.
2. **Implement the surviving structure:**
   - **Cohort-entry heterogeneity** — successive entry cohorts arrive with a declining baseline
     marriage propensity (the cohort-replacement channel the 2b APC identified). Parameterize the
     across-cohort decline; do not hard-code its magnitude — calibrate to the observed cohort
     gradient in ENAHO/GEIH composition.
   - **Exogenous period shock** — a calendar-time shifter common across live cohorts, **not**
     state-dependent (COL's significant non-reflexive period component; for CRI, period was
     insignificant — allow it to calibrate toward zero).

Calibrate the marriage-share (and cohabitation-share) trajectory to observed CR (ENAHO 2010–2024)
and COL (GEIH 2007–2024). Same band/base as Stage 1.5 / 2b.

## 4. The sufficiency test + decision

| Outcome | Reading |
|---|---|
| Model reproduces observed composition magnitude AND the late acceleration | **Sufficiency established.** No-reflexivity cohort-replacement + exogenous shock is enough; the paper's model matches the empirical verdict. Clean result. |
| Model reaches magnitude but stays a glide (misses the acceleration) | **Partial.** Cohort-replacement explains the level, not the tempo. The acceleration may live below the annual/cell resolution → routes to ENDS individual transitions. Report as a tension, do not paper over. |
| Model cannot reach magnitude without reflexivity | **Real tension:** the data reject reflexivity, yet no-reflexivity underperforms. This is itself a finding — flag prominently; it sharpens the ENDS question and the sub-annual-process hypothesis. |

All three are publishable; organize around the sufficiency question, not a hoped-for outcome
(same outcome-robust discipline as the methodology plan).

## 5. Explicitly NOT in Stage 3a (gated / out of scope)

- **Stage 3b — TFR-magnitude sufficiency.** Needs `w` (cohabiting-vs-married fertility differential)
  → ENDS / CR married-ASFR. Gated. Do not attempt on placeholder ASFR.
- **ENDS 2c-ii** (true transitions) and **ARG/CHL** external validity — data-gated, separate.
- Any reflexive / reference-group feedback term — rejected by 2b/2c.

## 6. Deliverables

- `STAGE3a_sufficiency_memo.md` — the read; §4 decision applied; magnitude & shape vs observed.
- `stage3a_norefl_abm.jl` (respecified model) · `calibrate_3a.jl` · `make_figures_3a.jl`.
- `outputs/stage3a/` — calibrated composition trajectories vs observed (CR, COL), cohort-gradient
  fit, period-shock estimate, `_assert_no_tfr.log`.
- PROTO-RAG-001 documentation (Nina's standard). `endorsed_by` blank pending Nina (build) + Anne
  (if the read touches the demographic verdict).

## 7. Gate

Nina endorses the build and the sufficiency read. The result feeds the paper's model section
(Fina's M2/M4). It does **not** reopen (B) — reflexivity stays out regardless of the 3a outcome;
only ENDS can reopen it.

## 8. Provenance

Working location: `GrandPlan/DFD/research/fertility_collapse_abm/STAGE3a_sufficiency_instruction.md`.
Archive to `_crossrefs/_build_instructions/`. Reconcile against the distributed demographic half
(orientation, 2b/2c memos, SDT note, JFV cornerstone). Run on Claude Fable 5.

*Resume-and-advance handoff. Debb, 2026-07-11, carrying Anne's verdicts and Nina's remit. For Claude Code on Fable.*
