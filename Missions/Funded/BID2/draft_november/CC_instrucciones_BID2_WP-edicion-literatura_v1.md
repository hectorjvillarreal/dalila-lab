# CC INSTRUCTIONS — BID2 · IDB working-paper edition: literature review, abstract, title, cleanup

**Version:** v1 · **Date:** 2026-11-07 · **Mission:** BID2
**Working directory:** `Missions/BID2/` (the draft and the full Overleaf zip, with
`references.bib`, `Figures/` and `MainDraft/paper_style_preamble.tex`)
**Source file:** `Draft-October.tex`. **Do not edit it.** Copy it to
`Draft-November.tex` and make every edit in the copy.
**Outlet:** Inter-American Development Bank Working Paper Series. This is **not** a
journal version. It needs no new computation, no new results and no new research
agenda.

---

## 0. What this pass does

There are three parts, done in this order:

1. **Pass 1 — mechanical cleanup.** Duplicated paragraphs, broken sentences, spelling
   and labels. Small and exact.
2. **Pass 2 — title, abstract, and the health sentence.** Replace the title text and
   the abstract with the versions given below. Add one matching health sentence to
   the introduction and to the conclusion, so that all four places tell the same
   story.
3. **Pass 3 — rewrite of the literature review.** This is the main task. Section 2
   goes from 2,558 words to about 1,300–1,500 words, written in the neutral voice of
   the rest of the paper.

The register rules in §1 apply to every sentence you write or rewrite. They matter
as much as the content.

**Out of scope:** the rest of the front matter (author list, affiliations, date,
`\thanks`, keywords, JEL codes); Sections 3, 4 and 5 apart from the Pass 1 items; the
model equations; all numbers in tables. The capital-income tax base
(`\tau^k r K` in the government budget) is blocked pending Diego. Do not touch it.

**Separation.** Nothing about FISCUS, SHCP, Hacienda, OSF or Reforma Fiscal may enter
the file. §7 checks this.

---

## 1. Register: write like an economist, not like an AI

The paper's voice is the voice of the experiments section. **Read
`\subsection{Retirement-Age Increase}` (CF2) before writing anything.** It is plain,
declarative, specific and unhurried, and it is the model for every sentence in this
pass. Sentences there state what the model does, what changes, by how much, and why.
They do not dramatize, and they do not comment on themselves.

### 1.1 Words and phrases that must not appear in any sentence you write or rewrite

*delve, crucial, crucially, pivotal, paramount, key* (as an adjective), *notably,
importantly, it is important to note, it is worth noting, worth noting, underscore,
underscores, highlight* (as a verb), *shed light, pave the way, landscape, realm,
tapestry, interplay, intricate, multifaceted, nuanced, holistic, seamless, robust*
(except in its statistical sense), *leverage* (as a verb), *foster, navigate, a
testament to, novel, unique, groundbreaking, comprehensive, in essence, in summary,
overall* (to open a sentence), *taken together, this underscores, plays a crucial
role, a growing body of literature, not only … but also.*

*Moreover* and *Furthermore* may open at most one sentence each in the whole of
Section 2.

### 1.2 Sentence patterns that must not appear

- **No "not X but Y" reversals** written for effect ("The question is not whether …
  but how …"). State Y.
- **No triplets for rhythm.** Use a list of three only when there are actually three
  items.
- **No colon reveals** ("The answer is simple: …").
- **No closing summary sentence** that repeats the paragraph ("Thus, …", "In this
  sense, …"). End a paragraph on its last piece of substance.
- **No em-dashes (`---`) in new or rewritten prose.** Use commas, parentheses or a
  new sentence. Em-dashes elsewhere in the paper stay as they are.
- **No self-description.** No sentence about what a subsection does, establishes or
  argues ("What this subsection establishes is a boundary …", "The paper's position
  rests on three qualifiers …"). Say the substance directly.
- **No priority or novelty claims.** Remove "has not been attempted", "to our
  knowledge no published model …", "we claim the combination and not any of its
  parts", "the first …". Describe what this paper does. Make no claim about what
  others have not done.
- **No metaphors.** Specifically: *prices* (as a verb for what a model or paper does
  to a policy), *price life itself, close a loop, carry expenditure risk, apparatus,
  shell, journey, destination, with room to spare, menu, wears … clothes, decided
  by, the newborn's near-indifference.* Use literal verbs: *quantifies, compares,
  values, models, represents, depends on.*
- **No previewing of this paper's numerical results** inside Section 2. The results
  belong to Section 5.

### 1.3 Positive rules

- Mostly subject–verb–object sentences of 15–30 words.
- Cited findings in the present tense: "\citet{X} show that …".
- Subject–verb agreement with *et al.*: "\citet{CortesEtAl2024} examine", plural.
- Terminology identical to the body:
  - the scenarios are **contribution-rate adjustment (CF0)**, **benefit reduction
    (CF1)** and **retirement-age increase (CF2)**, never "inaction";
  - groups are **low-education / high-education**, never "low/high skill", in prose
    and captions;
  - the model is **calibrated and estimated in two stages**, never "estimated rather
    than calibrated" or "fully estimated";
  - American English throughout.
- Restraint about the health result. The licensed description is that the health
  block **reproduces only a small part of the observed education gap in survival**,
  and that this is **related to** the predominance of curative spending in the data.
  Do not write *fails, failure, cannot identify, defect, measurement result,* or
  *overwhelmingly curative.*

---

## 2. Pass 1 — mechanical cleanup

Line numbers refer to `Draft-October.tex` and will drift. Match on the quoted text.

| # | Location | Edit |
|---|---|---|
| M1 | Introduction | Two consecutive paragraphs both describe CF0. **Delete** the paragraph beginning "Our first experiment examines demographic aging under the contribution-rate adjustment". Keep the one beginning "Using the calibrated model, we first examine". Change no number. |
| M2 | `\subsection{Benefit Reduction}` | The paragraph under `\paragraph{Aggregate and welfare effects.}` is followed, after the Aaron paragraph, by a second version of itself beginning "Relative to CF0, reducing the replacement rate lowers pension benefits per retiree by approximately $47\%$ … The reduction in pension benefits encourages households". **Delete the second version.** Its sentence on after-tax labor income ("The combination of higher wages and lower pension contributions increases after-tax labor income …") may be moved into the first paragraph as one sentence. The deletion also removes the stray `\$12.82`. |
| M3 | Appendix `app:demog2050` | Replace "…as the life tables used in the first step,  The UN World Population Prospects is the natural robustness alternative…" with two sentences: "…as the life tables used in the first step. The UN World Population Prospects provide an alternative demographic benchmark; using them would change the target dependency ratio but not the method used to construct the stationary economy." Report the before and after. |
| M4 | Introduction | `\citet{CortesEtAl2024} examines` → `examine`. Then search the whole file for any other `et al.` citation with a singular verb and fix each one. |
| M5 | Whole file | `Labour` / `labour` → `Labor` / `labor` (tables, `\tgroup`, `\paragraph` headings, prose); `behaviour` → `behavior`. Leave `references.bib` and bibliography titles alone. |
| M6 | Sections 5 and 6, figure captions and figure notes | In prose and captions, "low skill"/"high skill" → "low education"/"high education" (including "low-skilled"/"high-skilled"). Leave equations and the formal type definition in Section 3 as they are. Report each caption changed. **Report** whether the figure PDFs themselves print "skill" in their legends. Do not regenerate figures. |
| M7 | Caption case | Figure~\ref{fig:cf_lambda_menu} uses title case ("Age-Specific Welfare Effects of Benefit Reduction and Later Retirement"). Change it to sentence case to match the other captions. |
| M8 | Introduction, paragraph 2 | After the sentence introducing the pay-as-you-go pension system, add one clause or short sentence saying the pension block is a stylized pay-as-you-go benchmark rather than the full Mexican system, which also includes individual accounts (Section~\ref{sec:model} already says this in the pension subsection). |
| M9 | Introduction, paragraph 3 | "We discipline the model using Mexican data …" and "We calibrate the model using patterns of …" summarize the same exercise twice. Delete the second. |
| M10 | Preamble | Remove the unused `\todo`, `\note` and `\TODO` definitions and the "review copy" / "Carrasco-2026 look" comments. **Keep** `\input{MainDraft/paper_style_preamble}`. Keep `xcolor` only if it is still used after the removal. |

---

## 3. Pass 2 — title, abstract, and the health sentence

### 3.1 Title

Replace only the title text inside `\title{…}`, and keep the `\thanks{…}` attached to
it exactly as it is:

> **Spending Smarter under Demographic Pressure:** Pension Reform, Health, and
> Household Welfare in Mexico

Use the existing two-line layout (bold first line, `\\[6pt]`).

### 3.2 Abstract — replace the whole environment with this text

Use it verbatim, typesetting numbers as `$5.66\%$` and so on, matching the body:

> This paper examines how demographic aging affects pension financing, macroeconomic
> outcomes, and household welfare in Mexico. We use a stochastic
> overlapping-generations general-equilibrium model with endogenous health investment
> and heterogeneity by sex and education, calibrated and estimated in two stages on
> Mexican data. We compare stationary equilibria calibrated to Mexico's 2020 old-age
> dependency ratio and to its projected 2050 value. If the replacement rate and the
> retirement age remain unchanged, the pay-as-you-go contribution rate rises from
> 5.66% to 12.26%. Capital deepening raises wages and lowers the interest rate,
> leaving aggregate newborn welfare nearly unchanged relative to the 2020 baseline,
> while welfare comparisons become increasingly negative for older residents.
> Relative to this contribution-rate adjustment, reducing the replacement rate from
> 40% to about 18.5% raises newborn welfare by 8.29% of lifetime consumption, and
> raising the retirement age from 65 to 70 raises it by 3.11%. The reforms differ in
> their effects across ages, sex, and education, particularly for households that rely
> more on pension income. The model's health block reproduces only a small part of the
> observed education gap in survival, a result we relate to the predominance of
> curative spending in Mexican out-of-pocket health expenditure. All results compare
> stationary economies and do not include the transition costs of implementing the
> reforms.

Before replacing, check every number against the body: $5.66$, $12.26$, $8.29$ and
$3.11$ in `tab:cf_aggregates` and `tab:cf_welfare`; $0.1846$ for the replacement
rate; the 2.0 / 53.6 per cent composition in Appendix `subsec:health_evidence`. If any
check fails, stop and report. Do not adjust the text to fit.

The abstract must stay at or under 250 words. Report the count.

### 3.3 Introduction — one matching health passage

At the end of the contribution paragraph (the one beginning "Our paper contributes
to the quantitative literature on demographic aging and pension reform"), add two
sentences in this substance:

> The estimated health block reproduces only a small part of the observed education
> gap in survival: the model generates a gap of $0.30$ percentage points in five-year
> survival at ages 50--64, against $2.09$ in the data. Section~\ref{subsec:health_block_evidence}
> shows that health remains close to its upper bound in the calibrated equilibrium,
> and Appendix~\ref{subsec:health_evidence} documents that most out-of-pocket medical
> spending in Mexico is curative, whereas the model treats medical spending as
> chosen before the health shock is realized.

Rephrase the first sentence to avoid the colon if it reads better, but keep both
numbers exactly. Check both against `tab:validation` first.

### 3.4 Conclusion — replace the final (limitations) paragraph

Replace the paragraph beginning "Our findings are subject to several limitations"
with this text:

> These results are subject to several limitations. The comparisons concern
> alternative stationary equilibria rather than the transition to a reformed pension
> system, so they do not measure the welfare consequences for generations alive when
> a reform is introduced. The model assumes a closed economy, abstracts from informal
> employment, and represents the pension system as a stylized pay-as-you-go benchmark
> rather than the full Mexican system. The health block also reproduces only a small
> part of the observed education gap in survival, which we relate to the difference
> between medical spending in the model, chosen before the health shock, and the
> largely curative spending recorded in the data. Natural extensions include
> transition paths, an endogenous formalization margin, and a health block that
> distinguishes preventive from curative spending. Within these limits, the results
> show that pension reforms which lower long-run contribution requirements and raise
> newborn welfare can still impose large welfare losses on particular age and
> education groups. The choice among pension adjustments therefore depends on how
> these costs are distributed across households, and not only on the fiscal
> arithmetic of the pay-as-you-go system.

Leave the first three paragraphs of the conclusion unchanged.

---

## 4. Pass 3 — the literature review (the critical part)

### 4.1 Targets and fixed points

| Part | Now (words) | Target (words) |
|---|---|---|
| Opening paragraph | 125 | about 50 |
| `subsec:lit_pension` (aging and pension reform) | 818 | about 450 |
| `subsec:lit_longevity` (health capital) | 814 | about 450 |
| `subsec:lit_health` (health financing and social insurance) | 366 | about 150 |
| `subsec:lit_gender` (sex and education) | 435 | about 200 |
| Closing bridge paragraph | about 90 | about 50 |
| **Total** | **2,558** | **1,300–1,500** |

**Fixed points:**

- Keep `\label{sec:lit}` and all four subsection labels with their exact names.
  Subsection titles may be shortened, for example "Demographic Aging and Pension
  Reform", "Health Capital and the Life Cycle", "Health Financing and Social
  Insurance in Latin America", "Heterogeneity by Sex and Education".
- **No new `\cite` keys.** The 40 keys currently cited in Section 2 are listed in
  §4.3. Keep every one if possible. A key may be dropped only if keeping it would
  need a sentence that adds nothing. Report each dropped key and say whether it is
  still cited elsewhere in the paper (an uncited `.bib` entry is harmless; do not
  edit `references.bib`).
- **No new numerals.** If a number in the current Section 2 no longer has a place,
  drop it. Do not introduce one.
- This is a **rewrite**, not a sentence-by-sentence trim. Write each paragraph fresh,
  following §4.2 and the register rules in §1.

### 4.2 Paragraph-by-paragraph specification

**Opening (one short paragraph).** Name the four strands in one sentence: OLG models
of demographic aging and pension reform; life-cycle models with endogenous health
capital; health financing and social insurance in Latin America; heterogeneity by sex
and education. The second sentence says the review concentrates on the first, second
and fourth. Nothing more.

**Demographic aging and pension reform (three or four paragraphs).**

- *Factor prices.* `AuerbachKotlikoff1987` as the workhorse. `KruegerLudwig2007`: aging
  raises the capital–labor ratio, so wages rise, returns fall, and welfare effects
  depend on whether a household's resources are mainly labor income or assets.
  `CarvalhoFerreroNechio2016` separate longevity and dependency-ratio channels; note in
  one clause that this paper's experiments change population growth only and hold
  survival schedules fixed. `AuclertEtAl2021` for cross-country magnitudes. One
  sentence stating that this paper studies the same channels in a Mexican calibration
  in which the pay-as-you-go contribution rate adjusts endogenously. No results.
- *Policy options and their distribution.* `Kitao2014` compares higher payroll taxes,
  lower replacement rates, a higher retirement age and means-testing; this paper
  considers the first three, because the flat benefit cannot represent means-testing.
  `HuggettVentura1999` as the precedent for comparing stationary economies.
  `ConesaKrueger1999` and `NishiyamaSmetters2007` on the insurance value of an
  unfunded pillar and the cost of transitional generations. This supports reading
  steady-state newborn gains as an upper bound on what a reform is worth once
  transitions are included. State that once, plainly.
- *Differential mortality.* `SanchezRomeroEtAl2020` (socioeconomic longevity gaps
  redistribute through pension systems) and `Bagchi2019` (optimal progressivity
  insensitive to wealth-dependent mortality). No sentence about what "decides" this
  paper's incidence.
- *Conditions and scope.* `Aaron1966` and `AbelEtAl1989` on the return condition,
  stated as a condition, with no "room to spare". The existing sentence giving the
  annual return range against base growth may be kept once, plainly worded.
  `AttanasioKitaoViolante2007`: capital mobility mitigates the factor-price effects of
  aging, so this paper's closed-economy assumption matters for its factor-price
  results. Remove the claim that the paper "flags it where the results depend on it".
  `PessinoTerMinassian2021` for regional fiscal scale, one clause.

**Health capital and the life cycle (three paragraphs).**

- *Lineage.* The model adopts the health-capital approach of `Grossman1972`: health is
  a depreciable stock, medical spending is investment in it, and the stock affects
  survival and, here, labor productivity. In compact form: `DalgaardStrulik2014`
  (aging and death from investment and depreciation), `KuhnFeichtinger2015` (health and
  retirement with partial restoration), `Fioroni2010` (precautionary saving and health
  investment), and `HallJones2007` with `MurphyTopel2006` (valuation of longevity and
  an income elasticity of health spending above one). One clause linking the last two
  to the model's multiplicative health amenity.
- *General equilibrium, fiscal links and risk.* `JungTran2016` and
  `JungTranChambers2017` (stochastic GE OLG with endogenous health capital and
  insurance; aging experiments for the United States: the closest existing model).
  `Zhao2014` (social security affects health investment and longevity).
  `FrankovicWrzaczek2020`, `YewZhang2018`, `Lim2020`, `Carrasco2026` in one or two
  sentences. On risk: `DeNardi2010` (medical expenses and late-life saving),
  `HosseiniKopeckyZhao` (health-deficit process estimated on United States panels),
  `GertlerGruber2002` (major illness as a poorly insured shock in a developing economy,
  with the note that in this model the shocks hit the health stock rather than the
  household budget).
- *Prevention and repair.* These models are calibrated or estimated mostly on
  high-income data, where out-of-pocket payments are a small share of health spending,
  so the data do not separate spending that builds health from spending that restores
  it after a shock. `Ozkan2025` separates preventive and curative spending in a
  life-cycle model on United States data; `GalamaVanKippersluis2013` discuss
  reformulations of the Grossman model. In this paper medical spending is chosen
  before the health shock, so it is preventive in timing, while Mexican out-of-pocket
  spending is mostly curative. End with a reference to Section~\ref{subsec:health_block_evidence}
  and Appendix~\ref{subsec:health_evidence}. **No claim** about what has or has not
  been attempted. If a contribution sentence is needed, use this substance: the paper
  combines endogenous health capital, heterogeneity by sex and education, and an
  endogenously balanced pay-as-you-go system in a general-equilibrium model calibrated
  to Mexico.

**Health financing and social insurance in Latin America (one paragraph, two at
most).** `Arrow1963` (health risk is poorly insurable privately). `Levy2008` (hybrid
Bismarck–Beveridge systems with fragmentation). `Summers1989` (contributions act as a
tax when workers do not value the benefits). `WorldBankInformalizing2025` (the
formalization tax rate, highest for low-income workers). `BaezaPackard2006` (workers
value health coverage more than distant pension benefits). Then the model's position,
directly: pension benefits are a flat transfer indexed to average earnings and
financed by payroll contributions, with no individual benefit–contribution link and
no formal/informal margin; the results therefore concern pension financing under a
stylized pay-as-you-go system, not formalization incentives. The remark that the
contribution rate here is set by the system's budget rather than imposed may stay as
one clause. **No** "boundary rather than a contribution", **no** "shell", **no**
"landscape".

**Heterogeneity by sex and education (one or two paragraphs).**
`BorellaDeNardiYang2023` (couples and singles, survival risk, medical expenses and US
Social Security spousal provisions, with unequal effects on women) and
`FehrKindermann2018` (two-person household with childcare and taxation, without health
or endogenous survival). Combining such a household with continuous health capital,
health-dependent survival and endogenous prices would raise the computational burden
considerably. Say this in one plain sentence, with **no** "curse of dimensionality",
**no** "to our knowledge", **no** "implemented rather than proposed". This paper uses
four types (two education groups for each sex), each with its own measured
age-efficiency profile and baseline survival schedule, which capture in reduced form
differences that a structural household model would generate. Welfare results are
reported for all four groups. Do **not** say the schedules "decide" or "determine"
who bears each reform. The body says their separate contributions are not
quantified.

**Closing bridge (two sentences).** Section~\ref{sec:model} presents the model, which
extends \citet{CortesEtAl2024} to general-equilibrium factor prices, a continuous
health stock with age-dependent depreciation, and an endogenously balanced
pay-as-you-go system. Section~\ref{sec:calibration} describes the calibration and
Section~\ref{sec:experiments} the experiments. No "is where … meets", no "price".

### 4.3 Citation inventory (all 40 keys currently cited in Section 2)

Aaron1966, AbelEtAl1989, Arrow1963, AttanasioKitaoViolante2007, AuclertEtAl2021,
AuerbachKotlikoff1987, BaezaPackard2006, Bagchi2019, BorellaDeNardiYang2023,
Carrasco2026, CarvalhoFerreroNechio2016, ConesaKrueger1999, CortesEtAl2024,
DalgaardStrulik2014, DeNardi2010, FehrKindermann2018, Fioroni2010,
FrankovicWrzaczek2020, GalamaVanKippersluis2013, GertlerGruber2002, Grossman1972,
HallJones2007, HosseiniKopeckyZhao, HuggettVentura1999, JungTran2016,
JungTranChambers2017, Kitao2014, KruegerLudwig2007, KuhnFeichtinger2015, Levy2008,
Lim2020, MurphyTopel2006, NishiyamaSmetters2007, Ozkan2025, PessinoTerMinassian2021,
SanchezRomeroEtAl2020, Summers1989, WorldBankInformalizing2025, YewZhang2018, Zhao2014.

Check that `HosseiniKopeckyZhao` (no year in the key) resolves in `references.bib`.
Report if it does not. Do not rename it.

### 4.4 How to work

1. Write the new Section 2 into a separate scratch file first.
2. Run the §6 checks on the scratch file.
3. Report the full new text to Héctor before splicing it into `Draft-November.tex`.
   **Wait for approval.**
4. Splice and recompile.

---

## 5. What must not happen

- No change to any number in Sections 3–5 or the appendices, and no new number in
  Section 2.
- No new citation key, and no edit to `references.bib`.
- No softening or removal of a caveat in Sections 3–5.
- No new claims about results that the body does not report.
- No edit to the model equations, including the government budget.
- No change to the front matter other than the title text.
- No mention of FISCUS, SHCP, Hacienda, OSF or Reforma Fiscal.

---

## 6. Verification

Run all of these before reporting the pass complete:

1. **Register check** over the new Section 2, the abstract, and the sentences added to
   the introduction and conclusion: `grep -inE` for every word and phrase in §1.1, plus
   `inaction|fully estimated|estimated rather than calibrated|price[sd]? |prices |journey|apparatus|shell|landscape|has not been attempted|to our knowledge|we claim|---`.
   Every hit must be zero or explained. Report the list.
2. **Word counts:** Section 2 in total and per subsection (target 1,300–1,500); the
   abstract (at most 250); the introduction and the conclusion, before and after.
3. **Citations:** the keys retained and dropped from §4.3, and for each dropped key
   whether it is still cited elsewhere.
4. **Numerals:** the set of numerals in the new Section 2 must be a subset of those in
   the old one. Report both sets.
5. **Labels and references:** all five Section 2 labels present with their exact
   names; no undefined `\ref` anywhere in the file.
6. **Agreement:** `grep -nE "EtAl[0-9]*\} [a-z]+s "` reports no `et al.` citation with
   a singular verb.
7. **One story:** list every occurrence of 5.66, 12.26, 8.29, 3.11, 0.14 and 0.185 /
   0.1846 / 18.5 in the abstract, introduction, Section 5 and conclusion, and confirm
   that each states the same comparison (who, relative to which equilibrium).
8. **Compile** from the zip's assets, run BibTeX, compile twice more. Report errors,
   undefined citations, undefined references and the page count.
9. **Separation:** `grep -inE "FISCUS|SHCP|Hacienda|Open Society|OSF|Reforma Fiscal"`
   returns nothing.
10. **Untouched:** confirm `Draft-October.tex` is byte-identical to its original, and
    that the author block, date, `\thanks`, keywords, JEL line, and both
    government-budget equations in `Draft-November.tex` are identical to the source.

---

## 7. Reporting

Report in this order:

1. The Pass 1 edits, each with before and after.
2. The title and abstract as inserted, and the two new passages in the introduction
   and conclusion.
3. The full new Section 2, before splicing (§4.4), with word counts.
4. The verification results from §6.
5. Anything in the file that contradicted this specification, and what you did about
   it.

If a sentence can be written either plainly or elegantly, write it plainly. If a
passage seems to need a claim this specification does not license, leave the claim
out and say so in the report.
