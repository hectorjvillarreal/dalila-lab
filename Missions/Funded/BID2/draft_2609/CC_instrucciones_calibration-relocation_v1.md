# CC INSTRUCTIONS — BID2 · Section 4 (Calibration): relocation pass

**Version:** v1 · **Date:** 2026-08-18 · **Mission:** BID2 (IADB Fiscal Division)
**Target file:** `Draft-August-v2.tex`
**Edit mode:** in-place. This is a **move** operation, not a rewrite.
**Scope:** Section 4 (`\section{Calibration}`, lines ~659–1072) and the insertion
of a new Section 5 stub immediately after it.

---

## 0. What this pass is, and what it is not

Section 4 is 11,621 words — 42 per cent of the body, against 5,555 words for the
experiments that follow it. The imbalance is not caused by anything being wrong
inside it. It is caused by four blocks of material that are **findings, not
calibration**, having accumulated at its tail because there was nowhere else for
them to live.

This pass gives them somewhere: a new **Section 5, the health block**, sitting
between calibration and experiments. This file moves the material there. A
**second, later pass** writes the connective prose, the empirical evidence from
the motivation build, and the diagnosis. Do not attempt any of that here.

**The governing rule of this pass: text that moves, moves verbatim.** Word counts
across the two sections should be conserved to within the small number of words
added by §3 below. If you find yourself improving a sentence, stop — that is the
next pass, not this one.

### Preserve the spirit

Section 4 is the most rigorously self-disclosing part of the paper. Every
restriction is stated as a restriction; every parameter at a boundary is called a
diagnosis rather than a measurement; every diagnostic that was not repeated at the
current estimates says so. That character is the section's value and it is not
negotiable. Two consequences:

- **Do not remove a disclosure because the relocation makes it look isolated.**
  If a caveat is stranded by a move, flag it in the report; do not delete it.
- **Do not soften anything.** No hedge is to be strengthened, weakened, or
  tidied. The prose that moves arrives in Section 5 exactly as it left.

---

## 1. Non-negotiable constraints

1. Edit only within Section 4 and the new Section 5 stub. Sections 1, 2, 3, and
   everything from `\section{Experiments}` onward are out of scope and must end
   byte-identical.
2. **No new numerals anywhere.** Not one.
3. **No new `\cite` keys.**
4. **Every `\label{}` that moves keeps its exact name.** Cross-references
   elsewhere in the document point at these labels and must continue to resolve.
   Do not renumber, rename, or regularize any label.
5. Tables and figures move with their surrounding text, floats intact, captions
   and `\label{}` unchanged.
6. Continuous prose. No bullets introduced.
7. Do not compile; the document builds on Overleaf.

---

## 2. What moves

Move the following out of Section 4, **in this order**, into the new Section 5
stub created per §3. Move the full text of each, including its `\paragraph{}`
headings, floats, table notes and figure notes.

| # | What | Current location | Notes |
|---|---|---|---|
| M1 | `\subsection{The Value of a Statistical Life}` | line ~932, 296 w | Move whole subsection, label intact. |
| M2 | The education–survival capacity material | inside `\subsection{Calibration Results}`, the three paragraphs beginning at lines ~917, ~919, ~921 | See §2.1 below — this is the only surgical extraction in the pass. |
| M3 | `\subsection{The Health Block: Why the Baseline Is Stochastic}` | line ~944, 322 w | Move whole subsection, label intact. |
| M4 | `\subsection{Refinements Reserved for the Next Stage}` | line ~1006, 397 w | Move whole subsection, label intact. It is a roadmap and it belongs at the end of the health-block section, not in the middle of the empirical core. |

Approximate total moved: 1,700–1,800 words.

### 2.1 The surgical extraction (M2)

Inside `\subsection{Calibration Results}`, three consecutive paragraphs carry the
capacity finding:

- the paragraph headed `\paragraph{The education--survival gradient: a qualified
  success, disclosed.}` (line ~917);
- the paragraph beginning "The retirement of the education survival shifter rests
  on a capacity result worth recording" (line ~919);
- the paragraph beginning "Read constructively, the estimation delivers a
  measured statement about capacity" (line ~921).

Move all three, verbatim, in order.

**Do not move** the paragraphs before them (`The interior estimates`, `Two
parameters at the boundary`, `Reading the fit`) or the paragraph after them
(`Figure~\ref{fig:lifecycle_baseline}` and its float). Those are calibration and
they stay.

**Required repair at the seam.** Removing three paragraphs from the middle of a
subsection will leave `Reading the fit` running directly into the life-cycle
figure paragraph. Read both and confirm the join is coherent. If a transition
sentence is needed, add **one**, and report it verbatim in your output. If the
`Two parameters at the boundary` discussion refers forward to the capacity
material that has now moved, add at most one clause pointing to
Section~\ref{sec:healthblock} — the label exists once §3 below is executed.

---

## 3. The new Section 5 stub

Immediately after the end of Section 4 and before `\section{Experiments}`, insert:

```latex
%% ====================================================================
\section{The Health Block: What the Estimated Apparatus Delivers}
\label{sec:healthblock}

% DRAFTING NOTE — pass 2 of 2. This section was assembled by relocation.
% Still to be written, in a separate pass:
%   (a) opening movement: evidence on Mexican medical spending
%       (composition bracket, ENSANUT motive corroboration, unequal
%       capacity, the ENIGH shapes-not-levels convention) — approx. 700 words;
%   (b) connective prose between the relocated blocks;
%   (c) the closing diagnosis: prevention vs. restoration — approx. 400 words.
% Order of movements: evidence → what the block delivers (VSL) →
% what it does not (capacity) → why (diagnosis) → roadmap.
```

Then place the moved blocks in this order: **M1, M3, M2, M4.**

That order is deliberate. The apparatus succeeds where it was expected to fail
(the VSL result), the stochastic health block is explained, the apparatus fails
where it was expected to succeed (the capacity result), and the roadmap closes.
The empirical opening and the diagnosis are inserted at their marked positions in
the next pass.

Do **not** write any connective prose between the blocks in this pass. Leave them
adjacent. A later pass joins them.

---

## 4. What stays in Section 4, and why

Do not touch any of the following. They are calibration and they belong here:

- the section preamble (736 w);
- `First-Step Inputs` (2,511 w);
- `Second-Step Estimation` including the Identification and Inference paragraphs
  (2,822 w);
- `Calibration Results` minus the three paragraphs of M2 — the parameter table,
  the interior estimates, the two boundary diagnoses, the fit table, `Reading the
  fit`, and the life-cycle figure;
- `Validation` (1,070 w);
- `The Calibrated Baseline Equilibrium` (961 w);
- `Units and Normalization` (242 w);
- `Reproducibility of the Superseded Solve` (222 w).

Two of these were candidates for relocation in earlier discussion and are
**deliberately excluded from this pass**: `Units and Normalization`, and the
identification and inference material. Leaving them costs little and moving them
risks the cross-references. Do not move them.

Section 4 should land at approximately 9,800–9,900 words.

---

## 5. Cross-reference integrity — the main risk in this pass

Moved text carries labels that are referenced from elsewhere in the document, and
moved text contains references to material that has stayed behind. Both directions
must survive.

Before reporting complete:

1. Extract every `\label{}` inside the moved blocks. For each, `grep` the whole
   file for `\ref{}` and `\eqref{}` citations of it. Report the list: label,
   number of references, and where they now sit relative to the label.
2. Extract every `\ref{}` and `\eqref{}` inside the moved blocks. Confirm each
   target still exists in the file. Report any that do not.
3. Report any reference that now points **backwards from Section 4 into Section
   5** — that is, calibration text referring to material that has moved after it.
   Do not fix these by rewriting; report them, with line numbers, for review.
4. Confirm the three existing `% TODO: replace with \ref{sec:healthblock}`
   comments — in the introduction roadmap and the literature-review bridge — and
   report their line numbers. **Do not act on them in this pass**; the prose
   around them belongs to the sections that own them.

---

## 6. Verification before reporting complete

1. Word count of Section 4 before and after, and of the new Section 5. Report all
   three. The sum after should equal the before within the small number of words
   added by any seam sentence under §2.1.
2. Confirm no numeral was added: report the set of numerals in Section 5 and
   confirm each was present in Section 4 before the move.
3. Confirm no `\cite` key was added.
4. Confirm every moved `\label{}` retains its exact original name.
5. Confirm Sections 1, 2, 3 and the Experiments section onward are byte-identical.
6. Report every table and figure environment that moved, by label.
7. Report the seam sentence under §2.1 verbatim, if one was added.
8. Report the diff line ranges touched.

---

## 7. Reporting

Report: the four blocks moved and their word counts; the cross-reference audit
from §5 in full; the seam repair; the three word counts from §6.1; and anything
in the file that contradicted this specification.

**Where this specification is ambiguous, move less rather than more, and flag
it.** A block left behind is a one-line fix in the next pass; a block moved
wrongly, or improved in transit, is not.
