---
type: working_note
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led) → paper assembly (Fina M2/M4)"
title: "Results synthesis for Fina — everything the first draft can draw on (Stages 1 → 3a)"
target: "Fina (cross-project coherence): input for her build instruction on Draft 1"
date_added: 2026-07-12
added_by: "Claude Code (Stage 3a execution session)"
depends_on:
  - "TEAM_STATE_2026-07-11.md (routing; stage ledger)"
  - "model/STAGE3a_sufficiency_memo.md (Nina+Anne endorsed, conditions applied)"
  - "model/STAGE2b_compositional_cascade_memo.md · model/STAGE2c_col_individual_memo.md (Anne endorsed)"
  - "data/STAGE1_forensic_memo.md · data/coupling/STAGE1_5_identification_memo.md"
  - "model/SDT_framing_note_for_Anne.md (endorsed framing)"
status: "Results inventory for drafting. Fina designs the draft instruction; nothing here pre-empts her structure."
---

# Results Synthesis for Draft 1 — Rapid Fertility Collapse ABM

**Purpose.** Everything established, endorsed, and quotable as of 2026-07-12, in one
place, so you can design the Draft-1 build instruction (M2/M4). Organized as: the finding,
the evidence chain behind it, the assets on disk, and the claims discipline (what the
draft may and may not assert). Structure of the paper is yours; this note is raw material.

---

## 1. The five results the paper has in hand

### R1 — The collapse is real, fast, and invisible in smoothed international series
Stage 1 forensics (national vital registries, not WB/WPP): raw births fell 18–47%
(2010–2024) across CRI/COL/ARG/CHL while women 15–49 *grew* — behavioral, not
denominator artifact. Corrected national anchors: **CRI TFR 1.83 → 1.12 (−39%)**;
**COL 1.7 → 1.1 (DANE EEVV** — not the folklore "2.0 → 1.06"); ARG has no official
period TGF after 2021 — reconstructed, INDEC-pinned, **2024 ≈ 1.15–1.19**; MEX is the
slow-decline comparator (CONAPO-modeled 1.89 vs ENADID-survey 1.60 — "1.55" is not
national). WB/WPP smoothing erases the acceleration; the paper's empirical base is
vital-registry + microdata throughout. *(Assets: `data/STAGE1_forensic_memo.md`,
`data/STAGE1_provenance.md`, `data/charts/*.png`, `data/national/*.csv` with per-row
source/methodology flags.)*

### R2 — The state variable is union composition, and the marriage margin collapses secularly
Stage 1.5 built annual union-composition series (women 20–39, four 5-yr bands,
married/cohabiting split): CRI ENAHO/REDATAM 2010–2024; **COL GEIH microdata 2007–2024
(18 years, weights + estado-civil coding verified across the 2021–22 redesign — the
downturn is not a recode)**; MEX comparator series; ARG/CHL partial. The COL signature:
total union flat ~59–60% (2008–2020) then −6pts to 2024, while **marriage halves
(20.7% → 11.9%) with cohabitation substituting**. CRI equal-band married falls
0.324 → 0.166. *(Assets: `data/coupling/{CRI,COL,MEX}_coupling_annual.csv` + PROTO-RAG
sidecars, identification memos + addenda.)*

### R3 — No reflexive cascade: the collapse is cohort-replacement (the paper's central empirical verdict)
Stage 2b (birth-year pseudo-cohorts, APC curvature + state dependence, Anne-adjudicated
methodology; Anne-endorsed): **β > 0 in every specification, both countries** — within-
cohort marriage decline is *smaller* where the reference not-married share is already
high: stabilizing, the opposite of the cascade signature. Localization: **COL
cohort-dominant** with a real but *small* exogenous period component (F-test p≈3e-6;
curvature RMS 0.007 vs 0.014 cohort); **CRI cohort-leaning** (period not present,
p=0.18). Stage 2c-i re-ran COL at the individual-outcome level from GEIH microdata —
**the ecological objection is discharged** (verdict H_confirm). Standing caveats the
draft must carry: both βs are pseudo-panel (no true individual transitions until ENDS);
the 20–39 floor excludes the 15–19 entry margin; high-cohabitation regimes only.
*(Assets: 2b + 2c-i memos with Anne sign-offs, `model/outputs/stage2b/` full APC/state-dep
result set incl. MEX, `model/outputs/stage2c/`.)*

### R4 — A parsimonious no-reflexivity model is SUFFICIENT for the composition collapse (Stage 3a, Nina+Anne endorsed)
**Headline specification is cohort-only** (Nina condition 3): baseline Process-A rates +
a **three-parameter logistic cohort gradient κ(b)** on marriage entry + a one-parameter
formation tilt φ(b). No period shock, no feedback of any kind. Pre-registered gates:

| (married, 20–39 eq-band) | CRI | COL |
|---|---|---|
| M1 magnitude capture | **0.954** | **0.999** |
| M2 late-share (sim vs obs) | 0.490 / 0.581 | 0.468 / 0.459 |
| M3 Δ²-sign 2015–24 | pass | **fail** (the 2019–22 kink) |
| N1 loss (vs threshold skeleton 0.0855) | 0.0372 | 0.0246 |

**Verdict phrasing of record (Nina condition 4): "sufficiency on magnitude and
late-loading, with one unreproduced shape residual."** The credibility structure —
and this should shape how the model section argues — is **three non-fit convergences**,
not the fit itself:
1. κ(b)'s midpoint, a *single recovered parameter*, lands at birth cohorts **1991.7
   (CRI) / 1988.8 (COL)** — the same window where the independently-estimated 2b APC
   married cohort effects cross zero. The model never saw the APC estimates.
2. Full-recalibration ablations reproduce the 2b decomposition: COL without the cohort
   term is +63% loss; the period shifter is dispensable in *both* countries.
3. The no-reflexivity model beats the rejected Stage-2 threshold skeleton on the
   skeleton's own composition target.

Supporting discipline, all quotable: κ–φ separately identified (κ is union-total-neutral
by construction; perturbation ratios 11.6/102 vs 0.32/0.05 — `kphi_separability.csv`);
identification wall held (TFR never in any loss, 11/11 checks per country); deterministic
reproduction of the calibration; COL seeded 2008 per the documented GEIH 2007 frame
outlier (Anne-confirmed; superseded run archived). *(Assets: `model/STAGE3a_sufficiency_
memo.md`, `STAGE3a_Nina_signoff.md`, `model/outputs/stage3a/` incl. figures fig1–fig4.)*

### R5 — The framing: SDT channel-assisted compression (endorsed)
The endorsed frame (SDT note, amended): the pre-existing **consensual-union base is the
speed mechanism** — Second Demographic Transition change compresses fastest where the
cohabitation channel is already wide. The lead convergence for the paper:
**cohort-diffusion (demography) ↔ cohort-dominance (our APC + ABM)** — two independent
lenses landing on the same object. "Two faces" is a contribution, Esteve is the primary
literature anchor, JFV cornerstone note is part of the distributed demographic half.
This frame makes ARG/CHL a **falsifiable out-of-sample prediction** (see §3).

## 2. The negative results that discipline the paper (report, don't bury)

- **The threshold/coordination mechanism is rejected twice**: Stage 2 skeleton
  (glide, ~55–60% of TFR magnitude, no locus slide even though falsification passed) and
  Stage 2b (β > 0 everywhere). The paper's honest arc is *"we built the fashionable
  reflexive-threshold model and the data killed it; what survived is simpler."* This is
  a strength — outcome-robust methodology was pre-committed at every stage.
- **Band-level composition cannot discriminate cohort vs period structure by itself**
  (3a no-cohort ablations still pass M1/M2). Identification rests on 2b/2c; the ABM
  answers *sufficiency*. Draft must not claim the ABM identifies the mechanism.
- **The COL 2019–22 kink (M3)** is the one unreproduced shape feature — provisionally
  pandemic-era GEIH collection or a discrete shock; explicitly **not cascade evidence**;
  ENDS-resolvable.

## 3. Claims discipline for Draft 1 (hard constraints, all endorsed)

1. **No TFR-magnitude claim.** 3a targets composition; the TFR overlay rides a
   placeholder MEX-shape married-ASFR (level provisional by construction). TFR
   sufficiency is Stage 3b, gated on `w` (ENDS / CR married-ASFR). The draft may show
   the overlay as comparison-only with the caveat verbatim.
2. **No reflexivity claim in either direction.** (B) is deferred-not-closed,
   aggregation-cleared, pending ENDS. The draft says "not warranted on this evidence,"
   never "disproven."
3. **No tempo claim** (parity-independent hazards, A5). Fischer–Dattani handling: LAC
   tempo correction treated as immaterial but a tempo-corrected column is reported
   defensively where TFR anchors appear (+0.10 TFR ≈ ~2% population lift for Mexico).
4. **External validity is bounded**: two high-cohabitation regimes. ARG/CHL is the
   channel-absent prediction — collapse should be slower / differently structured where
   the consensual-union channel is narrow. Frame as *testable implication*, data-gated.
5. **Ecological honesty**: 2b βs are cell-level; 2c-i cleared aggregation for COL
   outcomes; true transitions await ENDS. The B7 correction (logged, Anne-ruled) is part
   of the record.
6. **Provenance style**: every series in the paper already has per-row source +
   methodology flags; the draft should inherit that standard (PROTO-RAG-001 spirit).

## 4. Figure and table inventory (paper-ready or near)

- **Stage 3a (headline spec, regenerated):** fig1_{CRI,COL} per-band sim-vs-obs
  (2×4 small multiples); fig2_{CRI,COL} κ(b) vs 2b APC cohort effects (the convergence
  figure — likely the paper's signature exhibit); fig3 π(t) robustness; fig4 TFR overlay
  (caveated). Figdata CSVs alongside for any re-styling.
- **Stage 2b:** cohort-line pseudo-panels, APC curvature (period vs cohort), β-CI by
  spec — `model/outputs/stage2b/figdata+figures` (CRI, COL, **MEX comparator included**).
- **Stage 1:** country panels (births, implied TFR, WB-vs-registry contrast)
  `data/charts/`.
- **Candidate tables:** 3a metrics table (§1 of the memo); ablation loss table;
  κ–φ separability; 2b β matrix (4 specs × 2 countries); Stage-1 corrected-anchors table.

## 5. What is NOT available to Draft 1 (so the instruction scopes around it)

- ENDS microdata (2c-ii): true union transitions; the 15–19 entry margin; reopening or
  closing (B); `w` for Stage 3b.
- CR INEC married-specific ASFR (A3, flagged to Debb since Stage 2).
- ARG/CHL series sufficient for the 2b-style test (EPH/CASEN partials exist).
- Census-2022 denominator rebasing; full Bongaarts–Feeney.

## 6. Suggested contribution stack (raw material — yours to arrange)

C1. Measurement: the fastest LAC fertility collapse documented against vital registries,
    with the WB/WPP smoothing failure shown explicitly.
C2. Empirical verdict: cohort-replacement, no reflexive cascade — β>0 across every
    specification, ecological objection discharged.
C3. Model: a 3-parameter cohort gradient is *sufficient* for the composition collapse;
    validated by non-fit convergence with the APC estimates, not curve-fit quality.
C4. Frame: SDT channel-assisted compression; cohort-diffusion ↔ cohort-dominance.
C5. Prediction: the channel-absent ARG/CHL implication, stated falsifiably.

The arc that holds these together — and that the stage record genuinely supports — is
methodological: *pre-registered, outcome-robust discrimination that rejected the
exciting mechanism and validated the parsimonious one.*

## 7. Practical notes for your build instruction

- Naming: 2c-i `pop_all` (15–39) = 2b `pop2039` (20–39) extended to the 15–19 floor —
  document the mapping wherever βs are compared across stages (standing flag from Debb's
  June handoff).
- The distributed demographic half lives across: orientation, 2b/2c memos, SDT note,
  JFV cornerstone. Reconcile draft framing against those four; there is no separate
  points document.
- All endorsements current: 2b, 2c-i, SDT (Anne); 3a build+read (Nina, conditions
  applied) + COL seed (Anne). Nothing in this note awaits a gate.
- Compute for any draft-support runs is trivial (full 3a calibration ≈ minutes on
  Dalila, deterministic); re-styling figures needs no re-simulation (figdata CSVs).

*Claude Code, 2026-07-12. For Fina's Draft-1 build instruction. The stage record, not
this summary, is authoritative — every number above traces to an endorsed memo or an
outputs CSV.*
