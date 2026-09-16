# CC INSTRUCTIONS — BID2 · Appendices: recovery, consolidation, and pointer repair

**Version:** v1 · **Date:** 2026-08-18 · **Mission:** BID2 (IADB Fiscal Division)
**Target file:** `Draft-August-v2.tex`
**Recovery source:** `Draft-August-v2_1_.tex` (dated 2026-08-16; **read-only**, never edit)
**Edit mode:** in-place. Mostly verbatim recovery, one consolidation, one class of repair.

---

## 0. What this pass does, in three parts

**Part A — Recovery.** The computational appendix currently runs 369 words. Its own
opening paragraph promises six things — the objective and weighting, the
identification analysis, the multistart convergence record, the parity and Euler
diagnostics, the override mechanics, and the first-step provenance — and delivers
the first only. Five subsections and an entire second appendix section were lost in
an earlier pass. **They exist intact in `Draft-August-v2_1_.tex` and are recovered
verbatim.** This is not writing.

**Part B — Consolidation.** Section 4 carries a subsection,
`\subsection{Reproducibility of the Superseded Solve}` (`subsec:repro`, 222 words),
whose content belongs with the recovered first-step provenance material in the
appendix. Héctor has decided to consolidate: the superseded apparatus gets one home,
in the appendix, and Section 4 loses the subsection.

**Part C — Pointer repair.** Both the appendix and `subsec:repro` contain
cross-references that were correct when written and are now wrong. They point at
`subsec:calibration_results` and describe it as the *superseded* estimation. That
label now names the paper's **current** ten-moment estimates. As written, the paper
tells a referee that its headline calibration cannot be regenerated. This is the
oldest surviving defect in the document and it must be fixed in this pass.

---

## 1. Non-negotiable constraints

1. `Draft-August-v2_1_.tex` is a read-only recovery source. Never edit it. Nothing
   else is recovered from it — Sections 1 through 7 of the target file are current
   and the older file's versions of them are obsolete.
2. Recovered text is inserted **verbatim**, except for pointer repairs made under
   Part C and reported individually.
3. **No new numerals.** No number is to be computed, updated, or inferred. If a
   recovered passage reports a figure, it reports it as it did.
4. **No new `\cite` keys.**
5. Every `\label{}` in recovered material keeps its exact original name.
6. Sections 1, 2, 3, 5, 6 and 7 must end byte-identical. Section 4 changes only by
   the removal specified in Part B.
7. Do not compile. The document builds on Overleaf.

---

## 2. Part A — Recovery

In `Draft-August-v2_1_.tex`, the material to recover runs from the line beginning
`\subsection{Identification}` (line ~1412) to the line immediately preceding
`\end{appendices}` (line ~1699). It comprises:

| Block | Source line (approx.) |
|---|---|
| `\subsection{Identification}` | 1412 |
| `\subsection{Multistart Protocol and Convergence}` | 1426 |
| `\subsection{Parity and Euler Diagnostics}` | 1441 |
| `\subsection{Override Mechanics}` | 1446 |
| `\subsection{First-Step Provenance of the Superseded Solve}` (`app:provenance`) | 1451 |
| `\section{Supplementary Tables and Data}` and its five subsections — Demographic and Health-Status Indicators, Health Expenditure Indicators, Fiscal Indicators, Labour Market Indicators, Life Table for Mexico | 1537–1698 |

**Insertion point.** Immediately after the existing `\paragraph{A caveat on the
Jacobian.}` block in `\section{Calibration and Computational Appendix}`, and before
`\end{appendices}`, preserving the source order above.

**Before inserting**, confirm that none of the recovered blocks already exists in
the target file, in whole or in part. If any does, report it and do not duplicate.

---

## 3. Part B — Consolidation of the superseded-solve material

1. In Section 4, locate `\subsection{Reproducibility of the Superseded Solve}` with
   `\label{subsec:repro}`.
2. Move its full prose into the recovered `\subsection{First-Step Provenance of the
   Superseded Solve}` (`app:provenance`), placing it at the **end** of that
   subsection.
3. **Carry `\label{subsec:repro}` with the moved text** and place it inside the
   appendix subsection. There is exactly one inbound `\ref{subsec:repro}` elsewhere
   in the document; keeping the label preserves it. Report where that reference sits
   and confirm it still reads sensibly now that its target is in the appendix — if
   the sentence around it says "above" or "in this section" or similar, report the
   sentence; do not rewrite it in this pass.
4. Delete the now-empty subsection heading from Section 4.
5. Read the two passages together after the merge. They overlap in subject and may
   repeat a fact. **Do not deduplicate by deleting.** If there is redundancy, report
   the overlapping sentences verbatim and leave both in place.
6. Consider whether the merged subsection's title should change now that it carries
   both the provenance and the reproducibility material. Propose a title; **do not
   change it** without approval. Keep `app:provenance` and `subsec:repro` regardless.

Section 4 should fall from 10,032 words to approximately 9,810.

---

## 4. Part C — Pointer repair

Two passages misdirect, and the recovered material may contain more.

**C1 — In the appendix objective paragraph.** The sentence reading, in substance,
that the diagonal weighting "is the form used in the superseded six-moment
estimation reported in Section~\ref{subsec:calibration_results} and in
Table~\ref{tab:moment_match}" points at the current estimates.

**C2 — In the moved `subsec:repro` prose.** The sentence beginning "First, the
estimates of Section~\ref{subsec:calibration_results}, the moment fit of
Table~\ref{tab:moment_match} and the baseline equilibrium of
Table~\ref{tab:calibrated_baseline} have no producing artifact" points at the
current estimates and the current fit table, and asserts they cannot be
regenerated. This is the most damaging single sentence in the document as it now
stands.

**Procedure — diagnose before editing.**

1. Determine where the superseded material actually lives. For each of
   `tab:moment_match` and `tab:calibrated_baseline`, report the label's location,
   the caption verbatim, and whether the caption identifies it as the current or
   the superseded solve.
2. Then repair:
   - **If a superseded table exists under a different label**, retarget the
     references to it.
   - **If the superseded estimates now have no table of their own** and only the
     recovered `app:provenance` material describes them, replace the references to
     `subsec:calibration_results` with a reference to `app:provenance`, or with
     prose naming "the superseded six-moment estimation" without a `\ref`.
   - **Under no circumstances leave a reference that describes
     `subsec:calibration_results` as superseded.**
3. **Audit the recovered blocks for the same fault.** They were written when
   `subsec:calibration_results` held the superseded estimates. Every `\ref{}` inside
   recovered text must be checked against what its target now contains. Report every
   one, with the sentence it sits in, and repair only those that assert something
   false about the current estimates. Where a repair is not obvious, report and
   leave it.

Report every pointer repair verbatim, before and after. This is the part of the pass
most likely to go wrong quietly.

---

## 5. Verification before reporting complete

1. Word counts before and after: the computational appendix, the Supplementary
   Tables section, Section 4, and the whole document.
2. **Full cross-reference audit.** Extract every `\label{}` in the document and
   every `\ref{}` and `\eqref{}`. Report: any reference with no matching label; any
   duplicate label; and the complete list of labels introduced by the recovery.
3. Confirm every recovered `\label{}` retains its original name.
4. Report every table and figure environment recovered, by label and caption.
5. Confirm no numeral was altered anywhere.
6. Confirm no `\cite` key was added, and report any key appearing in recovered text
   that is not cited elsewhere in the document — these must exist in
   `references.bib` and may interact with the open bibliography audit.
7. Confirm Sections 1, 2, 3, 5, 6, 7 are byte-identical, and that Section 4 differs
   only by the Part B removal.
8. Confirm `\end{appendices}`, `\bibliography{references}` and `\end{document}`
   remain in that order at the end of the file, each exactly once.

---

## 6. Reporting

Report, in order: the blocks recovered with word counts; the consolidation including
the proposed merged title and any redundancy found; every pointer repair verbatim
before and after; the full cross-reference audit; and the location and surrounding
sentence of the single inbound `\ref{subsec:repro}`.

Where recovered text and the current document conflict on a matter of fact, the
current document wins and the conflict is reported, not silently resolved.
