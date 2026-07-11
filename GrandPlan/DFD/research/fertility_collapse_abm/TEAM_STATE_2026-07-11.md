---
type: handoff_note
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led) → modeling seam (Nina)"
title: "Team state — fertility-collapse ABM as of 2026-07-11 (post Stage 3a)"
target: "Nina (action: gate). Anne (informed: three demographic observations). Debb (provenance + queue)."
date_added: 2026-07-11
added_by: "Claude Code (Stage 3a execution session)"
status: "Current state of record. Supersedes CLAUDECODE_handoff_2026-06-21.md as the orientation entry point."
---

# Fertility-Collapse ABM — Team State, 2026-07-11

## The one-liner

The collapse is **cohort-replacement, no reflexive cascade** (2b + 2c-i, Anne-endorsed) —
and as of today the paper's model matches that verdict: **a no-reflexivity ABM
(cohort-entry heterogeneity + exogenous period shock) reproduces the CR and COL
composition collapse — magnitude and late-loading — on pre-registered gates.**
Stage 3a sufficiency: **established on magnitude and late-loading (§4 row 1), one
unreproduced shape residual (COL M3 → ENDS)**. Nina endorsed (five conditions, applied);
Anne confirmed the COL 2008-seed decision. **Endorsements complete — feeds Fina M2/M4.**

## Stage ledger

| stage | question | verdict | endorsement |
|---|---|---|---|
| 1 / 1.5 | data forensics; identification gate; coupling series | collapse real, not artifact; invariants frozen | done (June) |
| 2 | threshold skeleton (CRI) | PARTIAL — ~55% TFR magnitude, glide, no locus slide | superseded by 2b |
| 2b | compositional vs cascade | **no cascade** — β>0 every spec, both countries; COL cohort-dominant + exogenous period; CRI cohort-by-residual | **Anne ✓** |
| 2c-i | ecological objection (COL individual-level) | **aggregation cleared** (H_confirm) | **Anne ✓** |
| **3a** | **sufficiency of what survived** | **established on magnitude + late-loading** (cohort-only headline spec; COL M3 shape residual → ENDS) | **Nina ✓** (5 conditions, applied — `STAGE3a_Nina_signoff.md`) · **Anne ✓** (COL 2008 seed, 2026-07-11) |
| 3b | TFR-magnitude sufficiency | — | gated on `w` (ENDS / CR married-ASFR) |
| 2c-ii | true union transitions (ENDS) | — the only thing that can reopen (B) | data-gated |
| — | ARG/CHL external validity (channel-absent prediction) | — | data-gated |

## Stage 3a in five lines (full read: `model/STAGE3a_sufficiency_memo.md`)

1. Skeleton respecified: coordination threshold **removed**; κ(b) cohort decline on
   marriage entry + φ(b) formation tilt + π(t) calendar-time shifter added; calibrated
   per country to composition only (TFR wall intact, 11/11 checks per country).
2. **M1 magnitude capture 0.975 (CRI) / 1.044 (COL); M2 late-share within 0.04 both** —
   and N1 losses (0.0351 / 0.0266) *beat* the rejected threshold skeleton (0.0855).
3. **Ablations reproduce the 2b ordering independently:** COL without the cohort gradient
   is +63% loss; the period shock is dispensable in both countries.
4. **Convergence check:** calibrated κ(b) inflects at birth cohorts ~1988–90 in both
   countries — the 2b APC crossover it was never fit to (fig 2).
5. Residual: **COL M3** (Δ²-sign, the 2019–22 kink) — the one shape feature outside the
   model; routes to ENDS. Reported, not papered over.

---

## Nina — gate PASSED (2026-07-11; conditions applied same day)

Adjudication: `STAGE3a_Nina_signoff.md` — build + read endorsed with five binding
conditions, all applied to the memo the same day (see memo §8 application record;
condition 2 satisfied with `outputs/stage3a/kphi_separability.csv`, condition 3 by
promoting the cohort-only spec to headline). Original verification order, kept for
reference:

1. `model/STAGE3a_sufficiency_memo.md` — §4 verdict, §3 ablations, §5 seed decision, §7 limits
2. `model/stage3a_norefl_abm.jl` — the no-reflexivity claim is a 5-minute code read:
   `agent_step!` has no cross-agent read; `model_step!` advances the calendar only
3. `model/outputs/stage3a/_assert_no_tfr.log` — wall checks (static + runtime registry)
4. `model/outputs/stage3a/sufficiency_metrics{,_noperiod,_nocohort}.csv` — pre-registered
   M1–M3 + ablation decomposition
5. `model/outputs/stage3a/figures/fig1_{CRI,COL}.png`, `fig2_*.png` — eye-test + κ-vs-APC

**Design calls that are the session's, not the instruction's — your scrutiny wanted:**
- cohort gradient rides the **marriage-entry margins** (`marry_share_of_form`,
  `cohab_to_marr`) plus a formation tilt; period shock hits **marriage entry only**
  (both placed where 2b localized the effects);
- pre-registered thresholds M1 ≥ 0.85, M2 |Δ| ≤ 0.10, fixed in `calibrate_3a.jl`
  before the full run;
- reproducibility: CRI calibration re-ran to identical digits (0.035104) — pipeline
  deterministic given seeds.

On endorsement, the result feeds the paper's model section (Fina's M2/M4).

## Anne — informed (your verdicts were inputs; nothing re-litigated)

Three observations from the run that touch demographics — flags, not claims:

1. **COL 2019–22 kink.** Married and cohab both break trend around the pandemic years;
   no smooth cohort+period mechanism reproduces it (the M3 residual). Plausibly partly
   GEIH pandemic-era collection. Worth your eye before it gets narrated as behavior.
2. **CRI period effect: the model agrees with you twice.** The free calibration kept a
   small period shifter, but the ablation shows it carries ~nothing (+6% loss when
   pinned to zero) — converging with your 2b read (CRI period not statistically present).
3. **Seed decision of record:** COL seeds **2008**, not 2007 — resting on the Stage 1.5
   companion's documented 2007 frame outlier (`data/coupling/COL_coupling_annual.md`).
   The degenerate 2007-seed run is archived intact
   (`model/outputs/stage3a/_superseded_col2007seed/`). **Confirmed by Anne 2026-07-11
   (via Héctor); recorded on the memo's endorsement line.**

## Debb — provenance + queue

- **Build record filed:** `_crossrefs/_build_instructions/2026-07-11_fertility_collapse_abm_stage3a.md`
  (PROTO-RAG-001; cross-refs to instruction, memo, 2b record, COL data caveat).
- **Write-back queue (your 2026-06-21 handoff):** item 1 — **CLOSED today**: branch
  `dfd-fertility-collapse-stage1.5` merged to `main` (merge commit `98b92ee`), both
  pushed to `dalila-lab`. Items 2–4 were closed in the June commit chain (`a5a5263`).
  **Item 5 still open:** CLAUDE.md + mission-project-map do not yet reflect the
  collapse-paper state (DFD primary; working-paper stage; 3a verdict).
- June carry-overs committed (`adcba3e`): SDT framing note + your handoff note.
- Future work should branch off `main`; the stage1.5 branch can be retired.
- Standing acquisition flags unchanged: **ENDS** (2c-ii + `w` for 3b), **CR married-ASFR**
  (A3), ARG/CHL series.

## Key files (all repo-relative to `GrandPlan/DFD/research/fertility_collapse_abm/`)

| file | what it is |
|---|---|
| `model/STAGE3a_sufficiency_memo.md` | **the gate deliverable** (Nina) |
| `STAGE3a_sufficiency_instruction.md` | originating instruction (Debb, 2026-07-11) |
| `model/stage3a_norefl_abm.jl` · `model/calibrate_3a.jl` | model + calibration/metrics/wall harness |
| `model/make_figures_3a.jl` · `model/_render_figures_3a.py` | figures pipeline |
| `model/outputs/stage3a/` | metrics, ablations, traces, figures, wall logs, superseded-run archive |
| `model/STAGE2b_compositional_cascade_memo.md` | the no-cascade verdict (Anne ✓) |
| `model/STAGE2c_col_individual_memo.md` | ecological objection discharged (Anne ✓) |
| `model/SDT_framing_note_for_Anne.md` | channel-assisted compression framing (endorsed) |
| `data/coupling/COL_coupling_annual.md` | COL data provenance incl. the 2007 outlier note |
| `_crossrefs/_build_instructions/2026-07-11_fertility_collapse_abm_stage3a.md` | build record (repo root `_crossrefs/`) |

## Frozen discipline (unchanged, for the record)

Composition {single, cohabiting, married} is the state variable · TFR never in any loss ·
`w`/fertility intensity gated to ENDS (3b) · **(B) reflexivity stays deferred-not-closed
regardless of the 3a outcome — only ENDS can reopen it** · Anne's demographic verdicts
are inputs downstream, not open questions.

*Claude Code, 2026-07-11. Orientation entry point until the next stage moves.*
