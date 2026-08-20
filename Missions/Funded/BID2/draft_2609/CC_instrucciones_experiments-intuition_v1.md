# CC INSTRUCTIONS — BID2 · Section 6 (Experiments): intuition and justification pass

**Version:** v1 · **Date:** 2026-08-18 · **Mission:** BID2 (IADB Fiscal Division)
**Target file:** `Draft-August-v2.tex`
**Edit mode:** in-place, additive and substitutive. Not a rewrite.
**Scope:** `\section{Experiments}` (lines ~1123–1314) and nothing else.

---

## 0. What this pass is for

Section 6 is technically solid and its analytical apparatus is not in question.
Two things are thin, and both matter most for the audience this paper is written
for — the IADB Fiscal Division, who will read this section and skim the rest.

**First, the selection of policies is never justified as a selection.** The three
experiments are well motivated individually, but the section never says why these
three and not others, nor what lies outside them. A policy reader will ask about
general-revenue financing, about combinations, about coverage. Answering
pre-emptively converts an apparently arbitrary set into a closed taxonomy, which
is a stronger claim.

**Second, the welfare results are stated precisely and explained thinly.** The
metric subsection is rigorous and almost entirely formal; the reader is told what
$\lambda$ is defined to be and not what it means, why a newborn gains from a
benefit cut, why aging leaves newborns nearly unharmed, or why the old-age numbers
are large. These intuitions all exist in the paper's own logic — they are simply
not written down.

**Governing constraint on length.** The body is 28,586 words. Net growth of this
section is capped at **700 words**, landing it at approximately 6,250. Prefer
converting dense technical prose into prose that is both technical and intuitive
over adding paragraphs alongside it. Where an addition would push past the cap,
compress the `Cost of Inaction` subsection, which at 1,675 words is the longest in
the section and carries the most restatable detail.

**What must not change.** No number, no table value, no result, no ordering of
subsections, and no caveat. The pre-registered-predictions paragraph, the
"What the household sees" paragraph, and the two rules governing how the
$\lambda_j$ profiles may be read are among the best writing in the paper and are
to be preserved in substance.

---

## 1. Non-negotiable constraints

1. Edit only inside Section 6. Sections 1–5, 7 and the appendices must end
   byte-identical.
2. **No new numerals**, with the single exception in §4 below, which is
   conditional and may block. Every figure in new prose must already appear in
   Section 6.
3. **No new `\cite` keys.**
4. **No `\label{}` renamed, added, or removed.**
5. Continuous prose. No bullets, no enumerated lists. `\paragraph{}` headings may
   be added where the subsection already uses them.
6. Do not compile. The document builds on Overleaf.

---

## 2. Justifying the selection (add ≈200 words to `\subsection{Design}`)

Add a short paragraph, placed after the `\paragraph{The two reforms.}` block and
before `\paragraph{What the household sees.}`. It should establish three things.

**The selection is exhaustive within the system.** The PAYG identity
$\tau^p = \kappa\,N^R/N^W$ has three arguments and no others. A pension system
facing a doubling dependency ratio can raise the contribution rate, cut the
replacement rate, or move the boundary between contributors and beneficiaries.
Each experiment moves exactly one and holds the rest, which is what makes their
incidence attributable. The set is therefore a closed taxonomy of within-system
responses rather than a sample of interesting policies.

**What lies outside it, and why it is outside.** Financing the pension deficit
from general revenue does not move any argument of the identity; it relocates the
obligation to a different budget constraint and raises a fiscal-sustainability
question this paper's closure does not address. Changing the structure of the
benefit rule — linking benefits to individual contribution histories, or altering
indexation — changes the object rather than the margin, and would be a different
model; the model's benefit is flat and wage-indexed, as Section 2 discloses.
Coverage expansion through formalization is designed and left as an extension.

**Why the three are studied singly.** The fiscal arithmetic of combinations is
additive and can be read straight off the identity. Their incidence is not, since
each reform changes the prices through which the others operate. Studying them
one at a time is what allows the incidence of each to be attributed; combinations
are left aside for that reason and not for lack of interest.

Keep this to one paragraph, or two short ones. Do not restate the magnitudes of
CF1 and CF2 — the preceding paragraph already justifies them, and it does so well.

---

## 3. Making the welfare results intuitive

This is the larger half of the pass. Five specific additions, none of which
changes a result.

### 3.1 Say what $\lambda$ means before saying what it solves (≈80 words)

`\subsection{The Welfare Metric}` opens directly with the compensating-variation
definition and the equation. Precede the equation with two or three sentences of
plain statement: the number reports the constant share of consumption that a
newborn in the better economy would give up, in every period of life and every
state, to be as well off as a newborn in the other; a $\lambda$ of five per cent
means giving up one twentieth of consumption at every age. State that it is a
lifetime object, not a period one, and that it is computed along the newborn's
own equilibrium path rather than a hypothetical one.

### 3.2 State the organizing welfare intuition once (≈120 words)

Add a paragraph at the end of the metric subsection, or at the start of
`The Cost of Inaction`, giving the principle that explains every welfare number in
the section. A pay-as-you-go pension delivers an implicit return equal to the
growth rate of the contribution base, while saving delivers the market return.
Where the market return exceeds the growth rate, mandatory participation
transfers resources away from the participant, and the size of the gap is what
every welfare comparison in this section is ultimately measuring. Reforms that
shrink the mandatory pillar move newborns toward the higher return; reforms that
change prices move the gap itself. Cite `Aaron1966`, which is already keyed and
already used in the section.

This paragraph is what makes the benefit-cut result stop being surprising.

### 3.3 Explain why aging leaves newborns nearly unharmed (≈150 words)

This is the section's most counterintuitive result and it currently receives a
mechanical account. Add the economic one, in `The Cost of Inaction`: when the
population grows more slowly, labour becomes scarce relative to capital, so the
wage rises and the return falls. A newborn faces a higher contribution rate but
earns a higher wage for a full working life, and because the pension is indexed
to the contemporaneous wage bill the benefit rises with the wage as well. Both
sides of the newborn's lifetime budget move up together, and the two effects
nearly cancel. The newborn is not protected by policy; it is protected by the
factor-price movement that the same demographic change produces.

**Required disclosure in the same paragraph.** Part of the capital deepening is
not a savings response at all. Gross investment absorbs $(n_p+\delta)K$ each
period, so a lower population growth rate frees resources that were previously
being used to equip new workers. This widening dividend is a consequence of the
stationary-demography device disclosed in the Design subsection, and it is part of
why the aged economy is richer per worker. State it plainly. It is better
volunteered than extracted by a referee, and the finding survives it.

### 3.4 Make the incidence mirror-image explicit (≈150 words)

The three reforms have a common structure that the section states result by
result but never as a pattern. Add it — most naturally in `The Policy Menu`, which
at 315 words is thin for what it carries.

Each reform repricess a stock that somebody already holds and cannot re-optimize.
Inaction lowers the return, which reprices the remaining lifetime of anyone
holding assets, so it falls hardest on older savers. The benefit cut lowers the
pension, which reprices the claims of anyone already retired and dependent on
them. The retirement rise extends the work band, which falls on those whose
late-life productivity is lowest and who must now supply labour at ages when they
would not have. Newborns rank the three identically because newborns hold no
stock and can adjust to any of them from the start; the rankings diverge with age
precisely because the old cannot.

Then the conclusion the section already reaches: the choice among the three is a
choice of whose old age pays, not a choice of how much welfare to have.

### 3.5 Make the old-age amplification plain (≈60 words)

The second reading rule in the metric subsection is correct and dense. Add one
plain sentence beside it: near the end of life, much of what remains valuable is
simply being alive, and scaling consumption cannot buy that, so closing even a
small value gap requires a large consumption adjustment. This is why old-age
$\lambda_j$ levels are large and why only the gradient is read.

### 3.6 Restate the steady-state caveat in plain terms (≈40 words)

The first reading rule says $\lambda_j$ compares residents of different steady
states and is not transition incidence. Add the plain version: these comparisons
price destinations, not journeys, and no person alive at a reform date
experiences the numbers reported here. Keep the existing formal statement.

---

## 4. Two table additions — conditional, may block

**4.1 $\Lambda_{\mathrm{void}}$ in the aggregates table.** The voided-asset flow is
defined in the model section as a use of output in the goods-market identity, and
it is reported in no experiment column. It moves with the age distribution and
with the asset hump, so it differs across all four economies, and it matters most
for CF1: cutting the pension by more than half forces households to self-insure
longevity through a non-annuitized asset whose unspent balance is destroyed.

Add a row reporting $\Lambda_{\mathrm{void}}/Y$ in all four columns of
`tab:cf_aggregates`.

**This requires four values that are not in the document.** If they are not
available in the solver output in the working directory, **do not compute,
estimate, or infer them — report as blocked and stop this item.** Do not add the
row with placeholder values.

**4.2 If and only if 4.1 succeeds**, add two sentences in `The Benefit Margin`
noting that the model contains no annuity market, that the pension is therefore
the economy's only longevity insurance, and that the reported gain from CF1 is
computed with the resulting bequest waste visible in the table. Do not editorialize
about whether this overturns the result. It does not; it qualifies it.

---

## 5. What must not happen

- No new result, no new interpretation that the equilibria do not support.
- No softening of any existing caveat, and no removal of one because an added
  intuition seems to cover it.
- No claim that health improvements offset the fiscal cost of aging. Retirement is
  exogenous and the contribution rate contains no productivity term.
- No transition claims. No cohort alive at a reform date appears in these results.
- No new figure.
- No reordering of subsections.

---

## 6. Verification before reporting complete

1. Word count of Section 6 before and after, and per subsection. Net growth must
   be at or under 700 words; report if it is not, and say where compression was
   taken.
2. `grep -o "[0-9][0-9.,]*"` over Section 6 — every hit must have been present
   before the edit, except any added under §4.1. Report the list and any
   exceptions.
3. Confirm no `\cite` key was added and no `\label{}` changed.
4. Confirm Sections 1–5, 7 and the appendices are byte-identical.
5. Report whether §4.1 executed or blocked, and on what evidence.
6. Report every added paragraph verbatim, grouped by the item of §2 or §3 it
   implements.

---

## 7. Reporting

Report the word counts, the numeral audit, the status of §4, and the added prose
in full. Where this specification asks for an intuition the document does not
actually support, say so and do not write it — a wrong intuition is worse than a
missing one, because it reads as authoritative and is harder for a reviewer to
catch than a missing paragraph.
