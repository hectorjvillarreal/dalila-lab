# `model/` — Stage 2 ABM build (Rapid Fertility Collapse ABM)

Home of the agent-based model that generates the rapid LAC fertility collapse
endogenously. Created 2026-06-19 when Stage 1.5 cleared the identification gate and
Stage 2 (model build) opened. Stage 1 / 1.5 data and forensics live in `../data/`;
the model code, calibration, and results live here.

## Lineage (how we got here)

- **Stage 1** (`../data/STAGE1_forensic_memo.md`) — data acquisition + forensic QA;
  collapse confirmed behavioral, not artifact; tempo/postponement-dominant.
- **Stage 1.5 gate** (`../data/coupling/STAGE1_5_identification_memo.md`, v3.0) — coupling
  microdata (CRI, MEX, COL) + Q1–Q4 identification. Addendum A (Colombia GEIH) made the
  gate decidable; Addendum B (marriage-margin rerun) identified the nonlinearity locus as
  **`w`-determined**. Gate cleared.
- **Stage 2 skeleton** (`STAGE2_skeleton_abm_spec.md`) — *this section*. Single-country
  (Costa Rica), CPU-parallel, mechanism-first. Proves the threshold mechanism end-to-end
  before the four-country nesting model and the GPU sweep.

## Governing spec

`STAGE2_skeleton_abm_spec.md` (Nina + Anne, v1.0, 2026-06-19) is authoritative for this
section. It declares this directory as its home. `endorsed_by` is blank pending Anne;
treat the spec as provisional below its frozen invariants.

## Frozen invariants (from the Stage 1.5 gate — do not deviate without Anne + Nina sign-off)

1. **State variable is union *composition*** — agent state distinguishes {single,
   cohabiting, married}, never just "partnered / not". A total-partnered-share model is
   wrong by construction.
2. **`w` is a nested structural parameter** — `w` = cohabiting/married fertility-intensity
   ratio (0 ≤ w ≤ 1). Do not hard-code; sweep {0.4, 0.6, 0.8} until the Colombia ENDS
   differential pins it.
3. **The nonlinearity locus is `w`-determined, not assumed** — the model must not hard-code
   whether the threshold sits in partnership formation (Process A, coupling-side) or in the
   coupling→fertility map (Process B, map-side); the locus emerges from `w` and the
   cohabitation-share initial condition.

Identification discipline (from Stage 1): **observed TFR is the OUTPUT to match, never a
calibration target.**

## Compute

CPU-parallel Agents.jl (Julia), per the Dalila compute envelope: the agent step is
CPU-native; the GPU is reserved for the later nesting-phase parameter sweep
(embarrassingly-parallel `(w, threshold, cohabitation-share)` runs across four countries),
not the skeleton. See `[[project_dfd_olg_gpu_strategy]]` — GPU payoff is conditional;
profile before porting.

## Planned deliverables (per the spec)

- `cri_skeleton_abm.jl` — the skeleton model (Agents.jl, CPU-parallel ensemble), documented
  to PROTO-RAG-001 code standards (Purpose / Inputs / Outputs / Assumptions / Dependencies).
- calibration notebook — independent-input → parameter map, with explicit confirmation TFR
  is not a target.
- `STAGE2_skeleton_results.md` — the four success criteria (collapse emerges; nonlinear;
  `w`-locus dependence appears; **falsification check** — remove the threshold, collapse
  must not reproduce), plus what the skeleton revealed the spec got wrong.
- figures — generated vs observed TFR; nonlinearity; with/without-threshold falsification.

## Open review notes (Claude Code consistency check, 2026-06-19 — pending Anne/Nina)

The spec was checked against the gate recommendation and found consistent (and sharper in
places — the composition state variable and the falsification check). Three items carried
for the review, none blocking:

- **Skeleton calibrates to Costa Rica, the *easier* case.** Colombia is the map-side extreme
  where total coupling barely moves (~6 pts) against a 35% TFR collapse; "can a coupling
  threshold generate that?" is the hard test, and the CRI skeleton cannot answer it.
  Demonstrating the mechanism on **Colombia** should be a required test of the nesting phase.
- **Skeleton-first (vs immediate full-spec freeze)** is a prudent deviation from the gate
  memo's "freeze the nesting spec" — endorsed; validate before scaling.
- **Tempo-adjusted / first-birth-ASFR lead test** (gate memo enrichment item 4) is not an
  explicit Stage 2 criterion; parity-from-the-start enables it, but the paper's causal-timing
  claim still needs it — keep on the nesting-phase radar.

## Parallel track (non-gating) — ARG + CHL acquired 2026-06-19; findings revise the spec premise

The Argentina and Chile coupling series are now built (`../data/coupling/ARG_coupling_annual.csv`
via INDEC EPH continua 2017-2025 urban; `../data/coupling/CHL_coupling_annual.csv` via MDS CASEN
2006-2022 national). The data **revise the spec's external-validity rationale** (§"Parallel track"
in the spec assumed ARG is a marriage-dominant Southern-Cone contrast):

- **Argentina is NOT the marriage-dominant contrast the spec assumed.** Urban ARG is
  high-cohabitation throughout (cohab-share of unions 68→75%, sitting with Colombia, 74%). It
  does **not** extend the `w`-identifying cohabitation range. It is a third high-cohabitation
  collapse case (strengthens generality of the high-cohab / map-side-at-total pattern).
- **Chile supplies the missing range — temporally, within one country.** CASEN 2006-2022 shows a
  marriage→cohabitation flip: marriage halves (36.1→16.7%), cohab-share of unions **35%(2006) →
  67%(2022)**. **Chile 2006 (35%) is the most marriage-dominant point in the whole
  CRI/MEX/COL/ARG/CHL panel** (more than CRI's ~48%); 2022 sits with ARG/COL. So Chile alone
  traverses the cohabitation-share range that identifies `w`, if cohab-share is treated as a
  time-varying initial condition — **this rescues the `w`-identification goal ARG could not
  deliver**, and is a stronger external-validity contribution than the spec anticipated.
- **Caveats:** ARG urban-only (vs national CRI/COL/CHL); CHL periodic (8 waves/16yr, coarse lead
  test); both have implied/reconstructed TFR (Mexico-style lead caveat); 2020 pandemic waves.
  Per-country detail + flags in the respective `*_coupling_annual.md` sidecars.

**For the nesting phase:** the panel's cohabitation-share span is CHL-2006 (35%) → CRI (48%) →
COL/ARG/CHL-2022 (67-75%). Use Chile's 2006-2022 trajectory as the primary `w`-identifying
variation. The spec's "Argentina marriage-dominant" line should be corrected at the next revision.

---

*Section opened 2026-06-19. Governing spec: `STAGE2_skeleton_abm_spec.md`. Gate of record:
`../data/coupling/STAGE1_5_identification_memo.md` (v3.0). Build-instruction archival flagged
for Debb.*
