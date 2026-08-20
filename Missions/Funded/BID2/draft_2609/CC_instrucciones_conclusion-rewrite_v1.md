# CC INSTRUCTIONS — BID2 · Section 7 (Conclusion): rewrite

**Version:** v1 · **Date:** 2026-08-18 · **Mission:** BID2 (IADB Fiscal Division)
**Target file:** `Draft-August-v2.tex`
**Edit mode:** in-place rewrite of one section.
**Scope:** `\section{Conclusion}` (lines ~1323–1341) and nothing else.

---

## 0. What this pass does

The conclusion is 957 words and is the weakest section in the paper. Its opening
paragraph is current and good. **Paragraphs two, three and four are stale** — they
describe results the paper no longer contains and assert a mechanism the estimation
refutes. Nothing in the section states the paper's health contribution, and there
is no policy reading for the audience the paper was commissioned by.

This is a rewrite, not a repair. Three of six paragraphs must go entirely, and the
section grows to roughly **1,600–1,800 words**. Growth is expected and sanctioned.

Everything the new conclusion says must already be established in Sections 1–6.
**A conclusion introduces no findings.** If a claim below cannot be traced to a
result in the body, do not write it — report it instead.

---

## 1. Non-negotiable constraints

1. Edit only inside Section 7. Sections 1–6 and the appendices must end
   byte-identical.
2. **No new numerals.** Every figure must already appear in the body of the paper.
   Registry in §5.
3. **No new `\cite` keys.**
4. **No `\label{}` renamed or removed.** `sec:conclusion` stays.
5. Continuous prose. No bullets, no enumerated lists, no `\paragraph{}` headings.
6. Cross-references must resolve. The section already references
   `subsec:vsl_structural`, `subsec:roadmap`, `subsubsec:health_risk`,
   `subsec:health_block_evidence`, `sec:experiments`. All still exist. Add
   `sec:healthblock` and `subsec:capacity_result` where the specification calls
   for them.
7. Do not compile. The document builds on Overleaf.

---

## 2. What must be removed

| Paragraph | Disposition |
|---|---|
| **P2**, beginning "The model's central analytical contribution is the identification of a fiscal amplification loop" | **Delete in full.** It claims health investment "extends working lives" — retirement is exogenous at $j_R$, which is precisely why CF2 has to move it by fiat. It claims the net fiscal effect of improved health is "ambiguous in sign" — the contribution rate is $\kappa N^R/N^W$ and contains no productivity or wage term, so better health can only raise it. And it calls this the paper's central analytical contribution, which it is not. This paragraph is the single most damaging surviving passage in the document. |
| **P4**, beginning "The model's architecture supports a natural extension toward gender-differentiated fiscal analysis" | **Delete in full.** It proposes expanding the type space from two to four as future work. The model has four types throughout and every table in Section 6 reports them. |
| **P3**, the extensions sentence naming the formalization threshold $\alpha^*$ and the four-channel operation of $\tau^m$ | **Compress.** The identity material at the start of P3 is good and stays. The extensions clause is over-specified for work that was not run; reduce to a clause each. |

Do **not** delete the fiscal-gap logic, the identity paragraph's opening, the
stochastic-health settlement in P5, or the closing principle in P6.

---

## 3. Target structure

Nine paragraphs. Where material exists, it is reused rather than rewritten.

**C1 — What was built and estimated (≈220 w).** Reuse the existing P1 opening
through the estimation description. Trim the VSL narrative to two sentences and
point to `subsec:vsl_structural`; the result now has its own home in Section 5 and
does not need retelling here.

**C2 — The health apparatus and what the estimation measured (≈220 w). NEW.**
This replaces the deleted P2 and carries the paper's methodological contribution.
The apparatus is a general-equilibrium economy in which health capital
simultaneously drives survival, labour productivity and the amenity value of
consumption, disciplined by classical minimum distance rather than assumed. It
solves and clears. The measurement result follows: at parameters that fit the
spending profile, both income elasticities, the skill premium and the survival
anchors, the investment block generates almost none of the observed
education–survival gradient, and the estimator drives the auxiliary channels to
corners. State this as a finding about the apparatus, not as a shortfall of the
calibration. Reference `subsec:capacity_result`.

**C3 — The diagnosis (≈180 w). NEW.** Medical spending in the model is committed
before the health shock and is therefore preventive by construction; measured
Mexican spending is predominantly restoration conditioned on a realized draw. A
block containing only the first, disciplined on moments generated largely by the
second, holds health near its ceiling and leaves no room for a spending-driven
survival gradient to open. Say what this contributes: the Grossman-descended
investment block, taken to emerging-economy micro-data, meets a limit that only a
fully disciplined estimation exposes. Reference `sec:healthblock`.

**Scope discipline.** Do not claim liquidity-constrained restoration, poverty
traps, persistence of transitory shocks, or unmet need. The model contains none of
these and the paper does not estimate them.

**C4 — The three fiscal results (≈260 w).** Reuse the existing three-result
passage from P1 nearly verbatim: aging under unchanged policy as a cohort
redistribution rather than an aggregate welfare event; the capital stock governed
first by income-risk persistence and only second by skill composition; the two
pension margins differing less in aggregate welfare than in incidence. Keep the
steady-state qualification sentence.

**C5 — The identity, the menu, and the bridge (≈240 w).** Reuse the identity
opening of P3. Then add what the paper has never said and should: **the incidence
results are structured by the estimated health and mortality apparatus even though
the health stock barely moves.** Low-education men are the newborn losers under
inaction because their education–survival gradient opens two decades earlier, so
they pay the higher contribution over a full working life and collect the raised
pension for fewer years. Low-education women bear the retirement reform because
their late-life efficiency is the lowest of the four types. Neither result is
available in a model without sex- and education-specific survival and efficiency
profiles. This is the sentence that explains why a health apparatus belongs in a
paper about pension margins; write it plainly.

**C6 — What this implies for policy (≈220 w). NEW.** For the audience this paper
was written for. Four things, each traceable to a result and no further:

- The menu is closed within the pension system. The identity has three arguments;
  everything else either relocates the obligation to a different budget or changes
  the benefit rule's structure.
- The three margins differ far more in incidence than in aggregate welfare, so the
  choice among them is a distributional decision presented as a fiscal one.
- Under a flat benefit indexed to the contemporaneous wage bill and a fixed
  retirement age, improvements in population health raise the contribution rate
  and do not lower it. That is a property of the benefit rule, not of health, and
  it means the fiscal case for health investment cannot be made through the
  pension block as currently designed.
- The model's dependency ratio is demographic rather than contributor-based, and
  the baseline is calibrated to the formal-sector population, so the fiscal
  pressure reported here is the favourable case.

**Do not recommend a reform.** Do not rank the three margins as policy advice; the
paper ranks them for newborns and shows the ranking reverses with age.

**C7 — What the paper does not establish (≈200 w). NEW.** Honest, not apologetic,
and drawn from caveats already in Section 6: no transition is computed, so nothing
here is incidence on any cohort alive at a reform date and no Pareto claim is
licensed; the economy has no informality margin and no annuity market; the
comparisons are between stationary equilibria; and the health block's inability to
generate the survival gradient is a measured result whose resolution requires the
specification decision, not a defect that qualifies the fiscal findings. State that
last point explicitly — the fiscal results do not depend on the health channel
being active.

**C8 — Extensions and roadmap (≈150 w).** Compress from the existing P3 tail and
P5. The specification decision on the health block, the transition analysis, the
formalization programme, the health-side instruments, and Costa Rica and Panamá —
a clause each. Keep the stochastic-health settlement from P5, which is well
written and belongs here. Reference `subsec:roadmap`.

**C9 — Closing principle (≈70 w).** Keep the existing final paragraph. Its claim —
that the question is not whether to spend more but when to spend, through which
channels, and with what consequences for the contributory architecture — now lands
much harder than when it was written, because the paper has just shown that *when*
you spend is exactly what distinguishes the model's object from the data's. One
clause connecting it to that finding is worth adding; do not rewrite the sentence.

---

## 4. Ordering note

C2 and C3 come before C4 deliberately. The paper's health contribution is the
methodological one and it is stated first; the fiscal results are what the
apparatus delivers. Do not reorder to put the fiscal findings first.

---

## 5. Number registry

Every numeral must already appear in the body. Permitted, with source:

| Quantity | Value | Body location |
|---|---|---|
| Contribution rate, baseline → inaction | $5.66\%$ → $12.26\%$ | Section 6 |
| Replacement rate under CF1 | $0.40$ → $0.185$ | Section 6 |
| Newborn gain, CF1 against inaction | $8.3\%$ | Section 6 |
| Retirement age under CF2 | seventy | Section 6 |
| Targeted moments | ten, nine from Mexican micro-data | Section 5 |

Any other numeral requires verification against the body before use. If a value
the specification implies is not in the body, write the claim without the number
or report it. **Do not import a figure from Section 5's health evidence or from
the calibration tables that does not already appear elsewhere in prose.**

---

## 6. Verification before reporting complete

1. Word count before and after. Target 1,600–1,800; report if outside.
2. `grep -o "[0-9][0-9.,]*"` over Section 7 — every hit must be in §5's registry
   or verified in the body. Report the list with sources.
3. `grep -n "ambiguous in sign\|extends working lives\|expanding the agent-type space\|alpha^\*"` over
   Section 7 — must return nothing.
4. `grep -n "poverty trap\|liquidity\|unmet need"` over Section 7 — must return
   nothing.
5. Confirm every `\ref{}` in the section resolves to an existing label. Report the
   list.
6. Confirm no `\cite` key added.
7. Confirm Sections 1–6 and the appendices are byte-identical.
8. Report the three deleted passages by their opening phrases, confirming removal.

---

## 7. Reporting

Report word counts, the numeral audit, the cross-reference audit, confirmation of
the three deletions, and the new paragraphs C2, C3, C5's bridge, C6 and C7
verbatim — those five are the ones carrying claims that did not exist in the
previous version and they need reading before the abstract is written against them.

Where the specification asks for a claim the body does not support, do not write
it. Report the gap. The conclusion is the last thing a referee reads and the first
place an overclaim is fatal.
