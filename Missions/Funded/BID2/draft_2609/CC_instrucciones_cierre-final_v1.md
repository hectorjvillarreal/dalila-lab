# CC INSTRUCTIONS — BID2 · Closing pass: introduction fixes and abstract trim

**Version:** v1 · **Date:** 2026-08-18 · **Mission:** BID2 (IADB Fiscal Division)
**Target file:** `Draft-August-v2.tex`
**Edit mode:** in-place, six targeted `str_replace` edits.
**Scope:** the `abstract` environment, `\section{Introduction}` (lines ~112–135),
and one word in Section 5. Nothing else.

This closes the last open writing items before external review. Every edit below
is small and specified. **Nothing else in the document is to be touched.**

---

## Constraints

1. Sections 2, 3, 4, 6, 7 and the appendices must end byte-identical. Section 5
   changes only by Edit 4.
2. **No new numerals anywhere.** Every figure used already appears in the
   document.
3. No new `\cite` keys, no `\label{}` added or renamed.
4. Continuous prose. No bullets.
5. Do not compile. The document builds on Overleaf.

---

## EDIT 1 — Abstract trim (267 → approximately 254 words)

Two cuts, no rewriting.

**1a.** In the third sentence, delete the trailing clause
`, including earnings profiles from household expenditure surveys` in full. The
preceding clause — ten moments, nine of them from Mexican micro-data — already
carries the point, and the sources are documented in Section 5.

**1b.** In the penultimate sentence, shorten the moment list. Replace

> At parameters that fit the observed spending profile, both income elasticities,
> the skill premium and the survival anchors,

with

> At parameters that fit the observed spending profile, the income elasticities
> and the skill premium,

Keep the rest of the sentence exactly as it stands, including the second
occurrence of "observed" before "education--survival gradient". The list is there
to show that the result is not a failure of fit; a shorter list does that just as
well.

**Do not touch** "The model is fully estimated", "the choice is whose old age
pays", the aging passage, or the final sentence.

Target 250–256 words. Report the count.

---

## EDIT 2 — "Level and age gradient of medical spending" (two occurrences)

**This is a correction of fact, not of style.** There is no level moment. The
three medical-spending targets in `tab:targeted_moments` are medical-spending
**shares of household expenditure** by age band. Section 5 opens by stating that
the expenditure survey is used for shapes, gradients and composition and never
for levels. As written, the introduction contradicts the paper's own
methodological rule twice.

Both occurrences are in Section 1:

- in the paragraph describing the estimation: "…health-technology, and
  health-risk parameters disciplined by the level and age gradient of medical
  spending, its income elastic…"
- in the paragraph reporting the capacity result: "…it was expected to succeed:
  at parameter values that fit the level and age gradient of medical spending,
  both income elasti…"

In each, replace `the level and age gradient of medical spending` with
`the age profile of medical-spending budget shares`, or another formulation that
is accurate about shares rather than levels. Use the **same** formulation in both
places.

---

## EDIT 3 — Two small repairs in Section 1

**3a.** In the policy-menu paragraph, the sentence reading "…worth 8.3 and 3.1
percent of lifetime consumption against inaction respectively, and both dominate
inaction" says the same thing twice. Delete `, and both dominate inaction` and
close the sentence at `respectively`.

**3b.** In the extensions paragraph, delete the clause
`, and one paragraph suffices for them`. It is the paper commenting on its own
layout. Recast the opening as a plain statement that the results suggest four
extensions.

---

## EDIT 4 — Section 5, one phrase

Section 5 (`sec:healthblock`) contains the same "level and age gradient" or
equivalent level-language if it was carried across from the calibration section.
**Search Section 5 for the phrase `level and age gradient` and for any other
claim that a spending level was targeted.**

- If found, apply the same replacement as Edit 2.
- If not found, report that and make no change.

Do not search or edit outside Section 5 for this. Section 4's own description of
its moments is out of scope for this pass; if it contains level language, **report
it with line numbers and do not edit it.**

---

## EDIT 5 — The bridge in the introduction

The introduction sets out the fiscal findings and the health findings and never
connects them. The connection exists and is well written in the conclusion, in the
paragraph containing:

> Low-education men emerge as the only meaningful newborn losers under inaction
> because their education--survival gradient opens roughly two decades earlier
> than women's, so they pay the doubled contribution over a full working life and
> collect the raised, wage-indexed pension for the fewest years---a sign pattern
> the paper reports with its fragility explicitly flagged. Low-education women
> bear the retirement-age reform because their estimated late-life efficiency is
> the lowest of the four types, so the extended work band compels them to work at
> wages that barely compensate the disutility.

**Adapt this into two sentences at the end of the policy-menu paragraph of Section
1** (the paragraph edited in 3a), or at the start of the paragraph reporting the
health results — whichever reads better; report which you chose and why.

Requirements:

- **Do not copy verbatim.** An identical passage in the introduction and the
  conclusion reads as padding. Compress to roughly two sentences.
- The point to land: the incidence results are structured by the estimated
  survival and efficiency profiles even though the health stock itself barely
  moves — which is why the health apparatus belongs in an analysis of pension
  margins.
- **Carry the fragility flag.** The conclusion qualifies the low-education-male
  sign pattern explicitly. If the compressed version states that result, it must
  carry the qualification. If there is no room for both, state only the
  low-education-women result, which is not flagged, plus the general claim.
- No new numerals. "Two decades" already appears in the conclusion and may be
  reused.

This is the most important edit in the pass. It answers the only structural
question a reviewer will have about the paper — why a health apparatus sits in a
paper about pension margins — and the introduction currently offers no answer.

---

## EDIT 6 — Nothing

`\tau^k r K` in the government budget is **not** to be touched. It is blocked
pending Diego's confirmation of what the solver does, and a guess here would
change a reported quantity. Leave it. Report that it remains open.

---

## Verification before reporting complete

1. Abstract word count. Report; target 250–256.
2. `grep -n "level and age gradient"` over the whole file — report every remaining
   hit with its section. Sections 1 and 5 must return nothing.
3. `grep -n "one paragraph suffices\|and both dominate inaction"` — must return
   nothing.
4. Section 1 word count before and after. Expect a small net increase from Edit 5.
5. Confirm Sections 2, 3, 4, 6, 7 and the appendices are byte-identical.
6. Confirm no numeral was added anywhere; report the numeral set of Section 1
   before and after.
7. Confirm `\tau^k r K` is unchanged and still present.
8. Report Edit 5's two sentences verbatim, and where they were placed.

---

## Reporting

Report each edit as executed, skipped or blocked, with the verification results.
Report Edit 5 in full — it is the only one carrying a claim, and it should be read
before the draft goes to review.

Where this specification is ambiguous, make the smaller edit and flag it.
