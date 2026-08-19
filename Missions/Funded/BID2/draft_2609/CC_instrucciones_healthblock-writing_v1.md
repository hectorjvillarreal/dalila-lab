# CC INSTRUCTIONS — BID2 · Section 5 (Health Block): writing pass

**Version:** v1 · **Date:** 2026-08-18 · **Mission:** BID2 (IADB Fiscal Division)
**Target file:** `Draft-August-v2.tex`
**Source file for new material:** `motivation_section.tex` (read-only; do not edit)
**Edit mode:** in-place. Adds new prose; relocated text is not rewritten.
**Scope:** `\section{The Health Block: What the Estimated Apparatus Delivers}`
(lines ~1042–1086) and nothing else.
**Prerequisite:** the relocation pass (`CC_instrucciones_calibration-relocation_v1.md`)
is complete. Section 5 currently holds four relocated blocks and a drafting note.

---

## 0. What this pass does

The relocation pass assembled Section 5 out of material moved from the
calibration section. It is currently 1,692 words of adjacent blocks with no
connective tissue, no empirical opening, no diagnosis, and no heading for its
most important content. This pass completes it to roughly 3,000–3,200 words.

Four jobs, in order of importance:

1. Write the **opening movement** — the evidence on Mexican medical spending.
2. Give the **capacity result its own subsection**, since it is currently buried.
3. Write the **closing diagnosis** — prevention versus restoration.
4. Write **connective prose** between the relocated blocks.

**Relocated text is not to be rewritten.** Its arguments, hedges and disclosures
stand as they are. Add around it; do not edit inside it. The one permitted
exception is noted in §4.

---

## 1. Non-negotiable constraints

1. Edit only inside Section 5, plus the two `% TODO` lines identified in §6.
   Everything else in the file must end byte-identical.
2. **Every number must come from the registry in §7.** No number may be
   introduced from any other source, including recollection of the calibration
   section. If the draft seems to require an unregistered number, stop and report.
3. **No new `\cite` keys.** A separate pass is auditing the bibliography; do not
   add to the problem. If a source needs naming, name it in prose.
4. Continuous prose. No bullets, no enumerated lists.
5. One new figure only, per §3. No other floats.
6. Match the file's typographic conventions, including `M\'exico` and `per cent`
   where the surrounding text uses it.
7. Do not compile. The document builds on Overleaf.

---

## 2. Target structure

Section 5 should read in five movements. Three exist; two are written here.

| Movement | Status | Target |
|---|---|---|
| **A. What Mexican households buy** | **write** | ≈700 w, new subsection, opens the section |
| **B. What the estimated block delivers** | relocated (`subsec:vsl_structural`) | untouched; add lead-in |
| **C. Why the baseline is stochastic** | relocated (`subsec:health_block_evidence`) | untouched; add lead-in |
| **D. What the block does not deliver** | relocated (M2 capacity paragraphs) | **needs its own subsection heading** |
| **E. The diagnosis, then the roadmap** | **write** + relocated (`subsec:roadmap`) | ≈400 w new, placed before the roadmap |

Delete the `% DRAFTING NOTE` comment block when the pass is complete.

---

## 3. Movement A — the empirical opening (≈700 words, new)

Create a subsection before the VSL subsection. Suggested title: *What Mexican
Households Buy When They Buy Medical Care*. Give it
`\label{subsec:health_evidence}`.

Four paragraphs, drawn **only** from the registry in §7.

**Paragraph 1 — the measurement convention, stated once and for the record.**
ENIGH records out-of-pocket medical spending and captures between 22 and 34 per
cent of the out-of-pocket total recorded in the national health accounts.
Consequently the survey is used throughout this paper for **shapes, gradients and
composition, and never for levels**; no peso figure from it is reported as a
national total. State this plainly. It is a rule the paper has been following and
has not yet written down.

**Paragraph 2 — composition.** Classifying out-of-pocket spending by whether the
item is preventive or restorative in intent gives an honest bracket rather than a
point: 2.0 per cent unambiguously preventive, 53.6 per cent unambiguously
curative, and 44.5 per cent that cannot be assigned either way from the
expenditure classification alone. The licensed verbal summary is **"majority
curative"** under any assignment of the ambiguous block. Do **not** write
"overwhelmingly curative".

**Paragraph 3 — the independent corroboration.** The expenditure classification
is corroborated from the individual side by a direct survey question on the motive
of care: preventive motives account for 11.2 per cent of last reported health
needs in the poorest wellbeing tercile and 15.9 per cent in the richest. Two
instruments, different in construction and in unit of observation, agree that
Mexican medical spending is predominantly a response to realized illness.

**Paragraph 4 — unequal capacity.** Catastrophic health expenditure incidence
runs at 3.9 per cent of households in the poorest decile against 1.4 to 1.9 per
cent in deciles four through ten. State the implication for the model: the
capacity to finance a response to a health draw is distributed very unequally, so
a specification in which restoration is unconstrained is a strong assumption
rather than a neutral one.

**Closing sentence of the movement.** One sentence stating what the section will
now do: report what the estimated block delivers, what it does not, and why. Do
**not** state the finding here — the section discharges it in movements D and E.

**Figure.** Include exactly one, the composition panel. Copy the float from
`motivation_section.tex` — file `fig07_composition.pdf`, label
`fig:mot_composition` — with its caption and figure note as written there.
Report the caption verbatim in your output. Do not include the other three figures
from that file.

---

## 4. Movement D — a heading for the capacity result

The three relocated paragraphs beginning *"The education--survival gradient: a
qualified success, disclosed"*, *"The retirement of the education survival
shifter rests on a capacity result worth recording"*, and *"Read constructively,
the estimation delivers a measured statement about capacity"* currently sit
inside the stochastic-health subsection with no heading of their own. The paper's
central measurement result is filed under a specification note.

Insert a `\subsection{}` immediately before the first of them. Suggested title:
*What the Investment Block Cannot Generate*. Give it
`\label{subsec:capacity_result}`.

**Permitted exception to the no-rewriting rule.** The first of the three
paragraphs opens with a `\paragraph{}` heading that will now sit directly under
the new subsection heading and duplicate it. Removing that `\paragraph{}` command
while leaving its sentence text intact is permitted, and only that.

**Title clash.** The section is titled *The Health Block: What the Estimated
Apparatus Delivers* and contains a subsection titled *The Health Block: Why the
Baseline Is Stochastic*. Rename the subsection to remove the duplication —
*Why the Baseline Carries Health Risk* or similar — **keeping
`\label{subsec:health_block_evidence}` unchanged**, since three cross-references
in Section 4 point at it.

---

## 5. Movement E — the diagnosis (≈400 words, new)

Place immediately before the roadmap subsection. Give it its own
`\subsection{}`; suggested title *A Mismatch of Objects*, with
`\label{subsec:diagnosis}`.

The argument, in three or four paragraphs, in this order.

**The two objects.** Medical spending in the model is committed before the health
shock is realized — the timing convention is stated in the model section — and is
therefore a preventive object by construction: it builds the stock in advance of
illness. Measured Mexican spending, on the evidence of movement A, is
predominantly restoration conditioned on a realized draw. These are not two
descriptions of one thing. They differ in timing, in exposure to expenditure risk,
and in how they connect spending gradients to survival gradients.

**Why the mismatch produces the result.** A block containing only the preventive
object, disciplined on moments generated largely by the restorative one, is
required to fit the level and age profile of spending using an instrument that
operates on a different margin. The estimation resolves this by holding the health
stock near its ceiling for every type, which fits the spending moments while
leaving no room for a spending-driven survival gradient to open. Connect this to
what the relocated capacity paragraphs already report; do not restate their
numbers.

**What the result is and is not.** State it as a measurement result about the
Grossman-descended investment block taken to emerging-economy micro-data, not as
a defect of implementation and not as a failure of the calibration. It could not
have been obtained from a partially calibrated model: only a fully disciplined
estimation forces the collision.

**Scope discipline — read this before writing.** The evidence in movement A
supports one proposition and one only: that measured spending is predominantly a
response to realized illness. It does **not** license claims about
liquidity-constrained restoration, health-specific poverty traps, persistence of
transitory shocks, or unmet need — the model contains none of these mechanisms
and this paper does not estimate them. Do not argue them. The constructive
sequel belongs in the roadmap subsection that follows, which already exists.

---

## 6. Connective prose and the TODO placeholders

Between the movements, add at most **two sentences each** of lead-in. Their job is
to say what the next block does, not to summarize it. Do not add transitions
inside relocated blocks.

Two `% TODO: replace with \ref{sec:healthblock}` comments exist, at line ~131 in
the introduction roadmap and line ~186 in the literature-review bridge. In both,
the surrounding prose says "the health-block section". Replace that phrase with
`Section~\ref{sec:healthblock}` and delete the TODO comment. These are the only
two edits permitted outside Section 5.

---

## 7. Number registry

**No numeral may appear in new prose unless it is on this list.** Relocated text
keeps whatever numbers it already carries.

| Quantity | Value | Source |
|---|---|---|
| ENIGH capture of national-accounts out-of-pocket | 22–34 per cent | motivation build |
| Unambiguously preventive share | 2.0 per cent | motivation build |
| Unambiguously curative share | 53.6 per cent | motivation build |
| Ambiguous share | 44.5 per cent | motivation build |
| Preventive motive, poorest → richest wellbeing tercile | 11.2 → 15.9 per cent | motivation build |
| Catastrophic incidence, poorest decile | 3.9 per cent | motivation build |
| Catastrophic incidence, deciles 4–10 | 1.4–1.9 per cent | motivation build |

Verify each against `motivation_section.tex` before use. If any fails, stop and
report rather than substituting.

**Explicitly not licensed in this pass:** the 2020 pandemic episode and its
figures, the forgone-care gradient, the age-sex profile ratios, the ENASEM
spending-response result, and any mortality-by-wealth figure. These belong to a
separate research line and must not appear.

---

## 8. Verification before reporting complete

1. Word count of Section 5 before and after. Target 3,000–3,200.
2. `grep -o "[0-9][0-9.,]*"` over new prose only — every hit must be in §7's
   registry. Report the list.
3. Confirm no `\cite` key was added anywhere in the file.
4. Confirm `subsec:vsl_structural`, `subsec:health_block_evidence` and
   `subsec:roadmap` retain their exact names, and report the three new labels.
5. Confirm the nine cross-references from Section 4 into Section 5 still resolve.
   Report them.
6. `grep -n "poverty trap\|unmet need\|liquidity"` over Section 5 — must return
   nothing.
7. `grep -n "overwhelmingly curative"` — must return nothing.
8. Confirm the `% DRAFTING NOTE` block is gone and both `% TODO` comments are
   resolved.
9. Confirm Sections 1–4, 6, 7 and the appendices are byte-identical apart from
   the two TODO edits of §6.
10. Report the figure caption inserted, verbatim.

---

## 9. Reporting

Report the word count before and after; the numerals used with registry status;
the new labels; the cross-reference audit; the connective sentences added,
verbatim; and anything in the file or in `motivation_section.tex` that
contradicted this specification.

Where the specification is ambiguous, write less and flag it. An under-written
movement is a paragraph to add next round; an over-claimed one is a referee
problem.
