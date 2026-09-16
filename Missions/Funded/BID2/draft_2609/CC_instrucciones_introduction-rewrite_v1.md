# CC INSTRUCTIONS — BID2 · Rewrite of Section 1 (Introduction)

**Version:** v1 · **Date:** 2026-08-18 · **Mission:** BID2 (IADB Fiscal Division)
**Target file:** `Draft-August-v2.tex`
**Edit mode:** in-place, targeted `str_replace`. Do **not** regenerate the file.
**Scope:** the `\section{Introduction}` block only.

---

## 0. One-line statement of the job

Replace the thirteen paragraphs of Section 1 with eight paragraphs, roughly
1,500–1,700 words, that describe the paper the document currently *is* rather
than the paper it was in June.

---

## 1. Non-negotiable constraints

1. **Edit only between `\section{Introduction}` (line ~112) and the blank line
   preceding `%% SECTION 2 — LITERATURE REVIEW` (line ~141).** Every other byte
   of the file is out of scope, including the abstract, which is handled in a
   separate later pass. Do not touch it even though it is stale.
2. **No number may appear in the new text unless it is in the registry of
   §5 below.** If the draft you are writing seems to require a number that is
   not registered, stop and report rather than supplying one.
3. **Every registered number must be verified against its stated location in
   `Draft-August-v2.tex` before use.** If a verification fails, do not silently
   correct it and do not use the number — stop and report the mismatch with the
   line number. This registry was assembled by reading the file, but the file is
   authoritative.
4. **Continuous prose. No bullets, no enumerated lists, no bold lead-ins.** The
   paragraph is the unit of structure.
5. **No new `\cite` keys.** Reuse only citation keys already present in the
   file. `CONAPO2023` and `Aaron1966` are known to exist; verify any other.
6. **British/American spelling and the existing typographic conventions of the
   file are to be matched, not changed.** Accented characters follow the file's
   existing convention (`M\'exico`).
7. **Preserve `\label{sec:intro}`.**

---

## 2. Why the rewrite is needed (context — do not paraphrase into the text)

The document has moved substantially since the introduction was written. Three
things changed and the introduction did not follow:

- The non-existence result under debt-financed inaction has been **removed from
  the paper**. There is no `proposition` environment anywhere in the body.
- The formalization experiment has been **removed** and replaced by a
  retirement-age experiment.
- The estimation **has** been run; the experiments are computed at the estimated
  baseline. The introduction still says the opposite.

The paper's contribution has also been repositioned. The health apparatus is the
methodological contribution; the pension experiments are the demonstration that
the apparatus solves, clears, and produces disciplined incidence; and the finding
that the health investment block cannot generate the observed education–survival
gradient is a **measurement result**, not a limitation. The introduction must
carry that structure.

---

## 3. Target structure — eight paragraphs

Write in this order. Word counts are guides, not targets to hit exactly.

**P1 — Stakes (≈130 words).** Latin America ages before it has grown rich, under
rapid fertility decline, incomplete formal labour markets, tight fiscal space and
chronically underfunded public health systems. Retain whatever
speed-of-transition comparison the current opening paragraph makes, together with
its existing citation, if one is present. Compress the current first two
paragraphs into this one. The three-country design reduces to a single clause;
this version reports the Mexican calibration.

**P2 — What the data say about health spending (≈150 words).** Mexican
out-of-pocket medical spending is predominantly a response to realized illness
rather than forward-looking prevention, and the capacity to finance that response
is deeply unequal. Use only the composition bracket from the registry. State that
the evidence is presented in the health-block section. Three to four sentences —
this paragraph sets up P6 and does not argue the case.

**P3 — What we build (≈180 words).** A stochastic OLG economy for M\'exico:
continuous endogenous health capital that raises survival, labour productivity and
the amenity value of consumption; agents heterogeneous in sex and skill;
endogenous factor prices; and a PAYG pension system whose contribution rate clears
endogenously. Estimated by classical minimum distance on ten moments, nine of them
the paper's own estimates from Mexican micro-data, with the labour-efficiency
profile and skill premium from ENIGH and the health-depreciation and
education- and sex-specific survival schedules from ENASEM. This paragraph
replaces roughly four paragraphs of the current draft; keep it to one.

**P4 — The inaction finding (≈200 words).** Under 2050 demographics and unchanged
policy the contribution rate more than doubles, yet newborn welfare is essentially
unchanged, because slower population growth deepens capital and the induced wage
and pension gains nearly offset the wedge. The cost is borne by cohorts already
holding assets, whose remaining lifetimes are repriced at a lower return, and it
rises steeply with age. State that aging under unchanged policy is a redistribution
across cohorts rather than an aggregate welfare event.

**P5 — The policy menu (≈220 words).** The PAYG identity leaves exactly three
margins — the contribution rate, the replacement rate, or the boundary between
contributors and beneficiaries — and the paper prices all three in general
equilibrium. The fiscal arithmetic on each is exact and predictable in advance;
what general equilibrium adds is the welfare and incidence content. For newborns
the benefit cut dominates the retirement-age rise, which dominates inaction, for
every type. The reforms differ most in whose old age pays: inaction taxes
wealth-holders through the return, the benefit cut taxes pension claims, the
retirement rise taxes the extended work band. Close on the planner choosing an
incidence rather than a welfare level. **Include the steady-state qualification in
this paragraph** — the comparisons price destinations, not journeys, and the
transition generations of a benefit cut are not modelled.

**P6 — The health block: what it delivers and what it does not (≈250 words).**
The apparatus succeeds where it was expected to fail: once the felicity carries an
estimated flow value of being alive, the model's willingness to pay for survival
comes in close to an external benefit-transfer target, having been off by orders of
magnitude without it. It fails where it was expected to succeed: at parameters
that fit spending levels, both income elasticities, the skill premium and the
survival anchors, the investment block generates almost none of the observed
education–survival gradient, and the estimator drives the auxiliary channels to
corners. Then the diagnosis: medical spending in the model is committed before the
health shock is realized and is therefore prevention by construction, while measured
spending is predominantly restoration conditioned on a realized draw; a block
containing only the first, disciplined on moments generated by the second, cannot
hold health away from its ceiling. State this as a measurement result about the
Grossman-descended investment block taken to emerging-economy micro-data.

**P7 — Positioning (≈180 words).** Locate the paper against the macro literature
on health in OLG and DSGE settings — Jung and Tran, and the Dalgaard–Strulik and
Zhao lineage — using **only citation keys already present in the file**; if a key
is absent, name the work in prose without `\cite`, following the file's existing
convention for unkeyed sources. What is distinctive is the combination: an emerging
economy, health capital carrying survival, productivity and the fiscal loop at once,
and a negative result that only a fully disciplined calibration can produce. Add
one sentence noting that the empirical literature measures health spending as
response to illness while the macro literature models it as forward-looking
investment, and that the two have not been reconciled.

**P8 — Extensions and roadmap (≈180 words).** One paragraph absorbing everything
the current draft spends five paragraphs on: the transition path, the formalization
programme, the extension to Costa Rica and Panam\'a, and the health-block
respecification. Then the roadmap sentence, rewritten per §6 below.

---

## 4. Sentences and claims that must not survive

Search for and remove each of the following. These are quoted from the current
text; match on the distinctive phrase, not the whole sentence.

| Locate | Reason |
|---|---|
| "That estimation has not yet been run under the specification this paper describes" | False. The estimation has been run and the experiments are computed at the estimated baseline. |
| any claim that the VSL result "revealed a structural divergence" | There is no divergence at the current estimates. The finding is that the felicity could not price survival without a flow value, and that adding one works. |
| "the central empirical fact around which our model is built", referring to the health crossing point or the skill gap in healthy longevity | The calibration shows the investment channel does not generate this gap. |
| "the net fiscal effect of improved population health is ... ambiguous in sign" | Retirement is exogenous and the contribution rate contains no productivity term, so health cannot offset the dependency effect in this model. Do not restate the ambiguity anywhere. |
| "a replacement-rate cut is regressive" | The benefit cut is welfare-improving for newborns of every type. The correct claim is about incidence by age and pension reliance. |
| any mention of the non-existence result or Proposition | Removed from the paper. |
| any mention of the formalization experiment as a result of this paper | Removed. It is an extension in P8. |
| "designed for M\'exico, Costa Rica, and Panam\'a" as a present-tense design claim | Reduce to one clause noting the extension is ahead. |
| the enumerated battery of counterfactuals (i)–(iv) | Not in the paper. |
| the four-type gender expansion described as a proposed extension | Already implemented; the model has four types throughout. |
| the contribution rate rising "by roughly seventy percent" or "from 9.3\% to 15.9\%" | Superseded numbers. |

---

## 5. Number registry

**No other numeral may appear in Section 1.** Verify each against the stated
location before use. Where a range is given, either endpoint or the range may be
used, but not a value inside it.

### From Section 7 (Experiments) — verify in `\section{Experiments}`

| Quantity | Value | Where to verify |
|---|---|---|
| Old-age dependency ratio, 2020 → 2050 | 0.141 → 0.307 | §7 opening paragraph; `CONAPO2023` |
| Contribution rate, baseline → inaction | 5.66\% → 12.26\% | Table `tab:cf_aggregates`; "Aggregates" paragraph |
| Replacement rate under the benefit margin | 0.40 → 0.185 (a 54\% cut) | "The Benefit Margin" opening |
| Retirement age and its contribution rate | 65 → 70; 8.78\% | "The Retirement Margin" opening |
| Annual return, baseline → inaction | 8.58\% → 6.82\% | "Aggregates" paragraph |
| Wage under inaction | +12.4\% | "Aggregates" paragraph |
| Pension under inaction | +20\% | "Aggregates" paragraph |
| Newborn CEV, inaction vs 2020 | +0.14\% (aggregate) | Table `tab:cf_welfare` |
| Newborn CEV, benefit cut vs inaction | +8.3\% | Table `tab:cf_welfare` |
| Newborn CEV, retirement vs inaction | +3.1\% | Table `tab:cf_welfare` |
| Age gradient of the cost of inaction | 1–2\% at 25–29; 6–8\% at 40–44; 12–21\% at 65–69 | "Where the cost of inaction actually sits" |

### From Section 5 (Calibration) — **verify before use; if any fails, stop**

| Quantity | Expected value | Where to verify |
|---|---|---|
| Targeted moments | ten, nine from Mexican micro-data | "Targets" paragraph, `tab:targeted_moments` |
| VSL, model vs benefit-transfer target | 179× vs 152× income | `subsec:vsl_structural` |
| Education–survival gradient generated by the investment channel | +0.06 pp of a +2.09 pp gap | `subsec:calibration_results` |
| Range of the health stock across types and ages | [0.990, 1.000] | `subsec:calibration_results` |

### From `motivation_section.tex` — **not yet in the target file**

Only the composition bracket is licensed for Section 1:

- unambiguously preventive 2.0\%; unambiguously curative 53.6\%; ambiguous 44.5\%.

The licensed verbal form is **"majority curative"**. Do **not** write
"overwhelmingly curative". Do not use any other number from that file in this
pass — the unequal-capacity, forgone-care and 2020-episode figures belong to the
health-block section and enter with it. Attach an inline LaTeX comment at the
paragraph noting the source section is pending:
`% source: health-block section, pending`

---

## 6. The roadmap sentence

Section 6 does not exist yet. Write the roadmap for the target structure:
Section 2 literature, Section 3 model, Section 4 calibration, Section 5 the health
block, Section 6 experiments, Section 7 conclusion — **but reference only labels
that currently exist** (`sec:lit`, `sec:model`, `sec:calibration`,
`sec:experiments`, `sec:conclusion`). For the health-block section, write the
clause in prose without a `\ref`, and place immediately after it the comment:

```
% TODO: replace with \ref{sec:healthblock} once the health-block section lands.
```

The roadmap must not promise the non-existence result or the formalization
experiment.

---

## 7. Verification before reporting complete

Run and report the result of each:

1. `grep -n "non-existence\|Proposition\|proposition"` over the introduction
   range — must return nothing.
2. `grep -n "formaliz"` over the introduction range — any hit must sit in P8 and
   be framed as an extension.
3. `grep -n "ambiguous"` over the introduction range — must return nothing that
   refers to the sign of the fiscal effect of health.
4. `grep -o "[0-9][0-9.,]*"` over the introduction range — every hit must appear
   in the registry of §5. Report the full list.
5. Word count of the new Section 1. Report it. Target 1,500–1,700; if the draft
   exceeds 1,800, cut from P3 and P7 first.
6. Confirm the abstract is byte-identical to its pre-edit state.
7. Confirm no `\cite` key was introduced that does not already appear elsewhere
   in the file.
8. Report the diff line range touched.

Do **not** attempt to compile; the document builds on Overleaf, not locally.
Report any construct you are unsure will compile rather than simplifying it.

---

## 8. Reporting

On completion, report: the word count before and after; the list of numerals
found by check 4 with their registry status; any registry verification that
failed; the placeholder comment inserted per §6; and any place where the
specification above and the state of the file conflicted, with what you did
about it. Where the specification is ambiguous, prefer the smaller edit and flag
it rather than resolving it silently.
