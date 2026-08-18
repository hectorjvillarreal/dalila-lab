# CC INSTRUCTIONS — BID2 · Rewrite of Section 2 (Literature Review)

**Version:** v1 · **Date:** 2026-08-18 · **Mission:** BID2 (IADB Fiscal Division)
**Target file:** `Draft-August-v2.tex`
**Edit mode:** in-place, targeted `str_replace`. Do **not** regenerate the file.
**Scope:** the `\section{Literature Review}` block only (lines ~136–204).
**Prerequisite:** the Section 1 rewrite (`CC_instrucciones_introduction-rewrite_v1.md`) is complete.

---

## 0. One-line statement of the job

Rebalance the literature review from a five-strand survey of adjacent fields
into an argument that sets up the paper's measurement result, and cut it from
2,438 words to roughly 1,800–2,000. Two subsections shrink substantially, one is
rewritten, and one false claim about the paper's own findings is removed.

---

## 1. Non-negotiable constraints

1. **Edit only between `\section{Literature Review}` and the `\bigskip` that
   precedes `\section{Model}`.** Everything else in the file is out of scope,
   including Section 1, which was just rewritten and is settled.
2. **Preserve all five `\label{}` commands** — `sec:lit`, `subsec:lit_health`,
   `subsec:lit_olg`, `subsec:lit_longevity`, `subsec:lit_informality`,
   `subsec:lit_gender`. Subsection titles may change; labels may not.
3. **No new `\cite` keys.** Twenty-six keys currently appear in this section.
   Keys may be dropped from the prose as material is cut; none may be added. If
   the rewrite seems to need a work that is not already keyed, name it in prose
   without `\cite`, following the file's existing convention.
4. **No new numerals.** Every number in the rewritten section must already
   appear in the current Section 2 text. Deleting numbers is expected; adding
   them is not. This includes numbers about the paper's own model — Section 2
   should carry none.
5. **Continuous prose. No bullets, no enumerated lists, no bold lead-ins.**
6. Match the file's existing typographic conventions, including `M\'exico`.
7. Do not attempt to compile. The document builds on Overleaf.

---

## 2. Context — what changed and why this section must follow

The paper has been repositioned. The health apparatus is the methodological
contribution; the pension experiments are the demonstration; and the central
finding is a **measurement result**: at parameters that fit the Mexican data, the
endogenous health investment block generates almost none of the observed
education–survival gradient, because medical spending in the model is committed
before the health shock and is therefore prevention by construction, while
measured Mexican spending is predominantly restoration conditioned on a realized
draw.

Section 2's job is therefore not to survey five fields at equal depth. It is to
establish **what the Grossman-descended investment block has been asked to carry
in this literature, and on what evidence**, so that the capacity result reads as
an answer to a known open question rather than as a problem the authors ran into.

Two further changes the section has not absorbed: the formalization experiment
has been **removed from the paper**, and the four-type sex-by-skill structure is
**already implemented**, not proposed.

---

## 3. Target structure

Retain five subsections. Rebalance as follows.

**Opening paragraph (≈70 words, currently 63).** Keep in substance, but the five
strands should be named in the order the section now treats them, and the
sentence should signal that the third strand is where the paper's contribution
sits rather than presenting all five as equals.

---

**§2.1 — Health Financing, Social Insurance, and the Tax Wedge**
*(currently 607 words → target ≈320)*

Keep: the Arrow pooling premise; the Bismarck/Beveridge hybrid framing with
`Levy2008`; the `Summers1989` valuation logic and its consequence — that
contributions function as a tax precisely when workers do not value the benefit;
the `WorldBankInformalizing2025` FTR concept in one or two sentences; and the
`BaezaPackard2006` asymmetry between health and pension benefit valuation, which
is the paragraph most relevant to this paper's flat-benefit pension design.

**Cut hard: the entire `OECDTaxingWages2026` paragraph.** It runs eleven
numbers — the 21.7 percent Mexican wedge and its components, the OECD average,
Costa Rica's 9.8 percent, the graduated *Cesantía en Edad Avanzada y Vejez*
schedule, the progressivity indicator — about an object this paper does not
model. There is no formal/informal margin in the economy and no tax-wedge
experiment. Reduce to at most one sentence retaining the key, or drop the key
entirely. Keeping the detail is the clearest surviving instance of the overload
the repositioning was meant to fix.

Add one sentence, drawn from the material already present, connecting the
valuation literature to this paper's pension design: benefits here are flat and
indexed to the contemporaneous wage bill, so the model contains no
benefit–contribution link at the individual level — a Beveridgean benefit inside
a Bismarckian financing shell, which is a deliberate simplification with
consequences for what the paper can say about formalization.

---

**§2.2 — OLG Models of Fiscal Sustainability, Health, and Aging**
*(currently 440 words → target ≈380; light edit only)*

Substantially keep. `AuerbachKotlikoff1987`, `DeNardi2010`, `KuhnFeichtinger2015`,
`Fioroni2010`, `FrankovicWrzaczek2020`, `YewZhang2018`, `Lim2020` all stay.

One required change. The paragraph on `CortesEtAl2024` currently says its
results — the consumption gaps and the twenty-year gap in healthy longevity by
skill — "form the empirical backbone of the present paper." Under the
repositioning the twenty-year gap is **the target the estimated model fails to
generate**, which is the paper's finding. Reframe it as the empirical target the
model is disciplined against and tested on, not as backbone. Do not state the
result here; Section 1 and the health-block section carry it.

---

**§2.3 — Endogenous Health Investment and the Longevity Channel**
*(currently 306 words → target ≈450; this subsection is rewritten, not edited)*

This is the load-bearing subsection and the one that most needs work. Consider
retitling to something like *Health as Capital: What the Investment Block Is
Asked to Carry*, keeping `\label{subsec:lit_longevity}`.

Three things to establish, in this order.

First, what the Grossman-descended block assumes. Health is a depreciable stock;
medical spending is forward-looking investment in that stock; the stock governs
survival, and in richer versions productivity as well. `DalgaardStrulik2014` and
the health-deficit line, `Carrasco2026` on the longevity channel through
aggregate saving and the interest rate, and the models named in §2.2 all rest on
this. State the assumption explicitly as an assumption.

Second, the evidentiary base. These models are estimated or calibrated
overwhelmingly on high-income data, chiefly United States panels, where insurance
coverage is broad and out-of-pocket spending is a smaller share of the total. The
question of whether the same block survives contact with an economy in which
health spending is largely out of pocket and largely triggered by realized
illness has not been settled.

Third, the unreconciled gap, stated as an open question rather than as this
paper's finding: the empirical literature on health expenditure in developing
economies measures spending as a response to illness, while the macroeconomic
literature models it as forward-looking investment. The two literatures have not
been reconciled, and no estimated general-equilibrium model has been forced to
confront the difference. Close by saying that this paper's estimation is where
the collision becomes measurable — **without stating the result**, which belongs
to Section 1 and the health-block section.

**The second paragraph of the current subsection is deleted in full.** See §4.

---

**§2.4 — Informality, Formalization Incentives, and Social Security**
*(currently 577 words → target ≈300)*

Keep the core empirical finding — the negative relationship between contribution
rates and formal employment, `Kugler2017` and the vesting-period evidence — and
the `WorldBankInformalizing2025` three-dimension framework with the compressed
timeline, which is where the seventy-versus-twenty-five comparison lives and
which Section 1 now cites.

Compress the non-contributory benefit channel to two or three sentences.
`BoschCampos2014`, `AteridoEtAl2011`, `AzuaraMarinescu2013`,
`CamachoConoverHoyos2013`, `CalderonMarinescu2012` currently receive a sentence
each with individual point estimates; one sentence noting that the estimated
informality effects of non-contributory health coverage expansions in Mexico and
Colombia range from substantial to negligible, with the keys grouped, does the
same work. `PerryEtAl2007` and `BoschMelguizoPages2013` may be kept or dropped at
the drafter's discretion; if kept, one clause each.

**Required change.** The closing paragraph currently reads "Our model contributes
to this literature by calibrating the baseline to the formal-sector population
and studying informality through a structured policy experiment: a formalization
program that incorporates a fraction of the informal population…". The
formalization experiment is not in the paper. Replace with a short statement that
the baseline is calibrated to the formal-sector population — which is true and
material, since the model's dependency ratio is demographic rather than
contributor-based — and that the formalization program is designed and left as an
extension.

---

**§2.5 — Gender Heterogeneity in Lifecycle Fiscal Models**
*(currently 447 words → target ≈220)*

Compress three paragraphs to one, or at most two. Keep `FehrKindermann2018` as
the reference point, the computational argument against embedding household
bargaining in general equilibrium in one sentence, and the paper's actual
approach.

**Required tense correction.** The current text says "By expanding the agent-type
space from two skill types to four…the model can decompose fiscal sustainability
pressures by sex." The model **has** four types throughout and every table in the
experiments section reports them. Write it in the present indicative as a
property of the model, not as a prospective design.

---

**Closing bridge paragraph.** Update to reflect the new structure: it should point
forward to the model section and to the health-block section, and should retain
the `CortesEtAl2024` lineage sentence. Reference the health-block section in
prose only, and place immediately after it:

```
% TODO: replace with \ref{sec:healthblock} once the health-block section lands.
```

---

## 4. Claims that must be removed

| Locate | Reason |
|---|---|
| "reinforcing the health-income poverty trap that our simulations identify" | **False.** The simulations identify no poverty trap. This is the single most damaging sentence in the document — it is a claim about the paper's own results that the calibration refutes, sitting in the section a health-macro referee reads most closely. |
| "the premature health crossing point documented in Section~\ref{sec:intro}" | Section 1 no longer documents this; the claim that it is the fact the model is built around has been removed. |
| "This feedback loop---from health investment to longevity to pension costs to the fiscal wedge---is the channel through which spending smarter on health can yield fiscal dividends" | **False and directionally wrong.** In this model retirement is exogenous and the contribution rate contains no productivity term, so the loop can only *raise* the contribution rate. Health yields no fiscal dividend through this channel. Do not restate the loop as ambiguous in sign either; that formulation has been removed from Sections 1 and 8. |
| the formalization experiment described as something this paper does | Removed from the paper; it is an extension. |
| the four-type expansion described as prospective | Already implemented. |
| the `OECDTaxingWages2026` numerical paragraph | Detail about an object the model does not contain. |

The second paragraph of §2.3 contains three of these six and should be deleted
in full and rewritten from the specification in §3 above rather than repaired
sentence by sentence.

---

## 5. What must **not** be added

- No statement of the paper's own results. Section 2 sets up questions; Sections 1,
  6 and 8 answer them. In particular, do not state the education–survival capacity
  result, the VSL result, or any experiment outcome here.
- No new numerals, including model outputs.
- No claim that the model contains a restoration or liquidity-constrained margin.
  It does not. The gap between prevention and restoration is posed here as an open
  question in the literature and is resolved as a finding in the health-block
  section.
- No forward reference to a `\ref` label that does not yet exist.

---

## 6. Verification before reporting complete

Run and report the result of each, over the Section 2 range only:

1. `grep -n "poverty trap"` — must return nothing.
2. `grep -n "crossing point"` — must return nothing.
3. `grep -n "fiscal dividend\|dividends"` — must return nothing.
4. `grep -n "formaliz"` — every hit must be either literature description or the
   extension sentence; none may describe an experiment this paper runs.
5. `grep -o "cite[tp]*{[^}]*}"` — report the full list of keys retained and the
   list dropped relative to the twenty-six currently present. Confirm no key is
   present that was not there before.
6. `grep -o "[0-9][0-9.,]*"` — every hit must have been present in the section
   before the edit. Report the list.
7. Word count of the section, total and by subsection. Target 1,800–2,000 total;
   report if outside.
8. Confirm all six `\label{}` commands survive with unchanged names.
9. Confirm Section 1 and Section 3 are byte-identical to their pre-edit state.
10. Report the diff line range touched.

---

## 7. Reporting

Report: word counts before and after, total and by subsection; the citation keys
retained and dropped; the numerals retained; the results of checks 1–4; the
placeholder comment inserted; and any place where this specification and the
state of the file conflicted, with what you did about it. Where the specification
is ambiguous, prefer the smaller edit and flag it rather than resolving it
silently.
