---
type: build_instruction
build_type: expansion
date: 2026-07-11
corpus_affected:
  - GrandPlan/DFD/research/fertility_collapse_abm/model/
  - GrandPlan/DFD/research/fertility_collapse_abm/model/outputs/stage3a/
triggered_by: "Stage 3a of the rapid-fertility-collapse ABM paper (Anne-led, modeling seam Nina): sufficiency test of the mechanism that SURVIVED 2b/2c — cohort-entry heterogeneity + exogenous period shock, NO reflexivity. Originating instruction: GrandPlan/DFD/research/fertility_collapse_abm/STAGE3a_sufficiency_instruction.md (Debb, 2026-07-11, resume-and-advance handoff carrying Anne's endorsed verdicts and Nina's remit; run on Claude Fable 5). The one ungated forward thread after the 3-week gap (ENDS 2c-ii and ARG/CHL remain data-gated)."
agents_involved: [Debb, Nina, Anne (verdicts as inputs), Claude Code, Héctor]
status: executed
sequence_position: "3a_of_4 (Stage 3 sufficiency; 3b TFR-magnitude remains ENDS-gated on w)"
notes: "Verdict: SUFFICIENCY ESTABLISHED (§4 row 1) in both countries on the pre-registered gates — M1 magnitude capture 0.975 (CRI) / 1.044 (COL), M2 late-share within 0.04 of observed; N1 composition losses 0.0351 / 0.0266 vs the rejected threshold skeleton's 0.0855 on its own target. COL M3 (curvature sign, 2015-24 second difference) FAILS — the 2019-22 kink (plausibly GEIH pandemic-era collection) is the residual routed to ENDS; reported, not papered over. Ablations with full recalibration: COL no-cohort +63% loss (cohort-dominant, independently reproducing the 2b APC ordering); the period shock is dispensable in BOTH countries (CRI +6%, consistent with 2b's insignificant CRI period effect). Convergence check: calibrated kappa(b) inflects at birth cohorts ~1988-90 in both countries, matching the 2b APC married cohort-effect crossover it was never fit to. DATA DECISION OF RECORD: COL seeds 2008, not the instruction's nominal 2007 — COL_coupling_annual.md documents 2007 as a frame/questionnaire outlier; the first (2007-seed) run produced degenerate metrics and is archived intact in outputs/stage3a/_superseded_col2007seed/. Identification wall held: 11 PASS / 0 VIOLATION per country (static + runtime-registry checks, _assert_no_tfr.log); no-reflexivity is grep-provable (agent_step! reads no other agent's state). CRI calibration reproduced to all printed digits on rerun. endorsed_by on the memo blank pending Nina (build + read). Per instruction §7 the outcome does NOT reopen (B) — only ENDS can. Committed b1e153f on branch dfd-fertility-collapse-stage1.5."
---

# Fertility-Collapse ABM — Stage 3a No-Reflexivity Sufficiency (Build Record)

**To:** provenance archive (Debb)
**From:** Claude Code (execution), on the Stage 3a instruction (Debb's resume-and-advance
handoff, carrying Anne's endorsed 2b/2c verdicts as inputs and Nina's modeling remit)
**Date:** 2026-07-11 (build, calibration, ablations, memo — single session on Claude Fable 5)
**Re:** Record the Stage 3a sufficiency build and its provenance for the parallel DFD
paper on rapid fertility collapse.

---

## 1. Scope and rationale

Stages 2b/2c settled that the marriage-composition collapse is **cohort-replacement**
(no within-cohort reflexive cascade; β > 0 everywhere; COL cohort-dominant with an
exogenous period overlay; ecological objection discharged at the individual level).
The Stage 2 skeleton's coordination threshold was thereby empirically rejected — but the
skeleton had also shown that *something* was missing (~55% of TFR magnitude, glide shape).
Stage 3a asks the sufficiency question about what **survived**: can cohort-entry
heterogeneity plus an exogenous calendar-time shock — with **no reflexivity anywhere** —
reproduce the observed composition collapse (magnitude AND late-loaded shape) in CR and COL?

Composition {single, cohabiting, married} is the only target; `w`/fertility intensity and
TFR magnitude remain gated to ENDS (Stage 3b). All three §4 outcomes were publishable by
design (outcome-robust discipline).

## 2. What was built

- `model/stage3a_norefl_abm.jl` — two-country respecification of the skeleton. Threshold
  and map-side feedback removed (transition rule reads no other agent's state; the model
  step advances the calendar only). Added: `birth_year` on the agent; κ(b) logistic
  cohort decline on both marriage-entry margins (3 free params); φ(b) log-linear formation
  tilt (1); π(t) calendar-time logistic shifter, state-independent (3); country configs
  CRI (ENAHO, seed 2010) and COL (GEIH, seed 2008 — see data decision).
- `model/calibrate_3a.jl` — 12-free-parameter boxed Nelder-Mead per country (600 evals ×
  4 restarts; inner 12k×4, final 50k×16); N1 composition-only loss; **pre-registered**
  sufficiency metrics M1 (magnitude ≥ 0.85), M2 (late-share |Δ| ≤ 0.10), M3 (Δ² sign)
  fixed in code before the full run; identification-wall checks (static source checks +
  a runtime CSV-load registry) written to `_assert_no_tfr.log`; ablation pins
  (`CAL3A_PIN=period|cohort`) for the mechanism decomposition.
- `model/make_figures_3a.jl` + `model/_render_figures_3a.py` — figdata CSVs and PNGs
  (per-band sim-vs-obs; κ(b) vs 2b APC cohort effects; π(t); caveated TFR overlay).
- `model/STAGE3a_sufficiency_memo.md` — the read; §4 rule applied mechanically.

## 3. Execution and verdict

See frontmatter `notes` for the complete result set. Headline: **§4 row 1 — sufficiency
established** on M1+M2 in both countries; the no-reflexivity model beats the rejected
threshold skeleton on the skeleton's own composition target; the ablation loss landscape
independently reproduces the 2b cohort-vs-period ordering; COL's second-order curvature
(M3) is the residual that routes to ENDS. Band-level composition alone cannot discriminate
cohort from period structure (the no-cohort ablations still pass M1/M2) — 3a claims
sufficiency only; identification rests on 2b/2c, as designed.

## 4. Cross-references

- Originating instruction: `GrandPlan/DFD/research/fertility_collapse_abm/STAGE3a_sufficiency_instruction.md`
- Read memo (gate deliverable): `GrandPlan/DFD/research/fertility_collapse_abm/model/STAGE3a_sufficiency_memo.md`
- Upstream verdicts: `2026-06-20_fertility_collapse_abm_stage2b.md` (this archive);
  Stage 2c-i memo + Anne sign-offs (repo, commits 35fc1e6 / a5a5263)
- Data caveat of record: `data/coupling/COL_coupling_annual.md` (2007 outlier)
- Protocol: `_crossrefs/protocols/PROTO-RAG-001.md`

## 5. Gate at close of build

Nina endorses the build and the sufficiency read → feeds the paper's model section
(Fina's M2/M4). (B) reflexive feedback stays deferred-not-closed, ENDS-gated, regardless
of this outcome. Stage 3b (TFR magnitude) waits on `w` via ENDS / CR married-ASFR.

*Build record filed by Claude Code, 2026-07-11, per PROTO-RAG-001 retention discipline.*
