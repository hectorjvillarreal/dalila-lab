---
type: review
stage: "Draft-1 model-section review"
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper → modeling seam (Nina)"
title: "Draft 1 §5 + ODD — Nina's model-section review (the open gate)"
target: "Claude Code (Draft 2) · workspace record"
date_added: 2026-07-12
added_by: Claude
reviews: "fertility_collapse_draft1_overleaf.pdf §5, Algorithm 1, eqs (1)–(6), Appendix A"
status: "CONDITIONAL sign-off. One eq-vs-algorithm inconsistency must be reconciled against code before the transparency claim is signed."
---

# Draft 1 — Model Section: Nina's Review

## GATE-BLOCKING — reconcile against the code

**N1 — C→M transition: equation (2) contradicts Algorithm 1.**
Eq (2): Pr(C→M) = c₀·κ(b) (marginal). Algorithm 1 (lines 5–6): "with prob δc → S; **else** with
prob c₀κ → M" — sequential, so realized Pr(C→M) = (1−δc)·c₀·κ. With δc ≈ 0.06–0.07 that is a
~6–7% gap. At least one of {eq (2), Algorithm 1} does not match `stage3a_norefl_abm.jl`, and the
transparency claim is precisely that they do. Reconcile against the code (authoritative); correct
whichever is wrong. S→union and M→S are consistent (no competing risk); only the cohabiting state,
where dissolution and conversion compete, diverges. **One-line fix, not a re-run — but it blocks my
sign-off on the transparency claim until squared.**

## RECOMMENDED ADDITIONS

**N2 — State the parameter-to-moment ratio.** Nine free parameters per country vs ~120 (CRI) / 136
(COL) target moments (4 bands × 2 shares × years). The single most legible anti-overfitting
statistic, currently absent. "Nine parameters, over a hundred moments" does more against the
black-box reflex than the whole of §5.4.

**N3 — Sharpen the ENDS framing (regime relocation).** A no-reflexivity model sufficing at the
annual cell level does not close the amplification question — it *relocates* it. A coordination
dynamic in first-union *timing*, sub-annual, among the 15–19 entrants the 20–39 floor never sees,
is where a run structure would live if anywhere, and only ENDS transitions can see it. Frame ENDS
as *the test of sub-annual amplification the annual data are blind to*, not merely as resolving the
M3 kink. This is the honest content of "reflexivity not disproven."

## SCOPE NOTES (minor; consistent with what the paper reports)

**N4 — φ(b) is monotone in cohort**, so it structurally cannot produce a flat-then-drop total-union
path — the same smoothing that surfaces as the COL M3 residual. One sentence tying them together.

**N5 — Closed-cohort replacement assumes constant inflow**, which would matter under 18–47% birth
declines — except the metrics are on the *equal-band-mean* married share, which insulates against
it. State this; it is a strength currently reading as an unexamined assumption.

## CONFIRMED GOOD (do not reopen)

- κ–φ separability cleanly constructed; the perturbation ratios (11.6/102 vs 0.32/0.05) prove it,
  not just assert it.
- Sufficiency ≠ necessity handled correctly: the paper states band-level composition cannot
  discriminate and sends identification to §4. No overreach.
- Ensemble reporting (50k × 16 seeds, mean±sd; deterministic given seeds) is the right presentation.
- The regime verdict is right and disciplined: a fast collapse that is *not* a reflexive-
  amplification process — a mechanical cohort flow. The pre-registered sign test is what earned it.

## Gate status

**Conditional.** Sign the model section on: N1 reconciled against code (the transparency claim);
N2 added; N3 sharpened. N4/N5 strengthen. The 3a conditions (non-fit convergence, κ param count,
κ–φ separability, period reconciliation, M3 phrasing) are all present and correct.

*Nina, 2026-07-12. Model section sound in construction; one eq-vs-code reconciliation stands between it and my signature.*
