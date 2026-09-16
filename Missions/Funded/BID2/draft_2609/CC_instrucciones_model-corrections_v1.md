# CC INSTRUCTIONS — BID2 · Section 3 (Model): three targeted corrections

**Version:** v1 · **Date:** 2026-08-18 · **Mission:** BID2 (IADB Fiscal Division)
**Target file:** `Draft-August-v2.tex`
**Edit mode:** in-place `str_replace`, three edits only.
**Scope:** Section 3 (`\section{Model}`) — and nothing else.

Section 3 is not being rewritten. It is the strongest section in the paper and
its structure, argument, and length are settled. This file makes two corrections
of fact and adds one clause. Do not improve, reorganize, condense, or otherwise
touch anything else in the section.

---

## EDIT 1 — Capital-income tax base (line ~415 and line ~423)

**Status: BLOCKED pending confirmation from Diego. Do not execute Edit 1 until
told which branch applies.**

**The problem.** Households hold a single non-contingent asset $a$ earning $r$
and pay $\tau^k$ on all of it: line 515 gives working-age resources as
$\bigl(1 + r(1-\tau^k)\bigr)a$ and line 543 gives the retired analogue. The
asset-market condition sets $A_{\mathrm{dom}} = K + B$. Aggregate capital-income
tax payments are therefore $\tau^k r (K + B)$.

The government budget records only $\tau^k r K$:

- line 415, `\tau^c C + \tau^m M + \tau^\omega w L + \tau^k r K + B' = G + (1+r)B`
- line 423, `r B = \tau^c C + \tau^\omega w L + \tau^k r K + \tau^m M - G`

The revenue $\tau^k r B$ is collected from households and never appears on the
government's side. This is not a rounding matter: $5B/Y$ runs between 107 and 124
percent across the experiment columns, and $B$ is the residual that closes the
budget, so the discrepancy is absorbed by the object the paper reports.

**Branch A — the solver taxes all household assets.** Replace `\tau^k r K` with
`\tau^k r (K + B)` in both equations, or equivalently `\tau^k r A_{\mathrm{dom}}`
if that symbol is already defined at that point in the text; check which
convention the surrounding prose uses and match it. Add one sentence after the
flow budget noting that capital-income tax is levied on all household asset
income, including holdings of government debt.

**Branch B — the solver taxes only the return on physical capital.** The
equations are right and the household problem is wrong. Report this and stop; the
fix is not a one-line edit and requires Héctor's decision.

Under either branch, do not silently adjust any reported number.

---

## EDIT 2 — The flow value of being alive is not separately identified (line 274)

**The problem.** Period utility is
$u = \Omega(h)\bigl[\frac{(c-v)^{1-\gamma}-1}{1-\gamma} + \chi\bigr]$.
The $-1$ in the numerator contributes a constant $\frac{1}{\gamma-1}$ to the
bracket, which is the same role the text assigns to $\chi$ alone. Only the sum
$\chi + \frac{1}{\gamma-1}$ is identified and only the sum is the flow value of
being alive. The paragraph at line 274 currently argues that the $-1$ is a
normalization *and* that $\chi$ is not a normalization, without noticing that
they are the same object.

This is now an internal inconsistency, not a subtlety: the welfare metric in the
experiments section already derives its bound using the combined constant.

**The edit.** In the paragraph beginning "The constant $\chi$ is not a free
normalization either", revise so that:

- the flow value of being alive is identified as $\chi + \frac{1}{\gamma-1}$, not
  as $\chi$ alone;
- the claim that $\chi$ is not a free normalization is preserved — it is correct,
  because the combined constant is economically meaningful once death carries a
  continuation value of zero — but restated in terms of the sum;
- the condition for a state being ranked below not being alive is stated in terms
  of the bracket, as it already is, which remains correct;
- the remaining argument of the paragraph is untouched: separating $\chi$ from
  $\Omega(h)$ assigns distinct roles to distinct parameters, and $\chi$ is absent
  from $u_c$ so it shifts the value function without disturbing the Euler
  equation or the labour margin. All of that stands.

Keep the edit to the minimum needed. Do not rewrite the paragraph.

**Consistency check, report only — do not edit outside Section 3.** Verify
whether the welfare-metric derivation in the experiments section writes the
bound using $\chi + 1/(\gamma-1)$. Report what it uses. If the two now disagree
after this edit, report the mismatch; do not fix it in this pass.

---

## EDIT 3 — One clause on the timing convention (line 237)

**Context.** Section 2.3 now poses the prevention-versus-restoration distinction
as an open question in the literature and names *timing* as what separates the
two. Section 3 states the timing convention and says nothing about what it
implies, so a reader primed three pages earlier has to make the connection
unaided.

**The edit.** Line 237 currently reads, in the timing list:

> Medical spending is committed before the health shock is realized, so
> investment cannot condition on the shock's arrival.

Append one clause, or at most one short sentence, noting that this makes medical
spending in the model a preventive object by construction — spending that builds
the stock in advance of illness rather than restoring it afterwards.

**Constraints on this edit, which matter more than the edit itself:**

- State it as a property of the specification, nothing more. Do **not** say the
  convention is a limitation, do **not** anticipate the estimation result, do
  **not** mention the education–survival gradient, the ceiling, or the corner
  estimates.
- Do **not** add a `\ref` to the health-block section; it does not exist yet.
- Do **not** add a footnote.
- The timing list is a numbered `enumerate` of within-period order. Keep the item
  the length of a list item; if the addition would run past two lines, shorten it.

---

## What must not happen

- No other edit anywhere in Section 3. In particular: no closing subsection, no
  commentary on the $\min\{1,\cdot\}$ cap, no note on exogenous retirement, no
  forward pointers, no "what the calibration tests" material. These were
  considered and deliberately excluded.
- No changes to Sections 1, 2, 4, 5, 6, 7 or the appendices.
- No new numerals anywhere.
- No new `\cite` keys.
- No renaming of any `\label{}`.

---

## Verification before reporting complete

1. Report the diff: every hunk, with line numbers. There should be at most three
   hunks, and at most two if Edit 1 is blocked.
2. `grep -n "tau\^k" Draft-August-v2.tex` — report all hits and confirm the
   household resource lines (~515, ~543) are unchanged.
3. Confirm that Sections 1, 2 and 4 onward are byte-identical to their pre-edit
   state.
4. Report what the experiments-section welfare metric uses for the flow value
   constant.
5. Report the word count of Section 3 before and after. The change should be
   under 60 words.

Do not compile; the document builds on Overleaf. Report any construct you are
unsure will compile rather than simplifying it.

---

## Reporting

Report the three edits as executed or blocked, the diff hunks, the results of
checks 2–5, and anything in the file that contradicted this specification. Where
the specification is ambiguous, make the smaller edit and flag it.
