# CHANGELOG — Draft-November.tex — IDB working-paper edition

Build instruction: `CC_instrucciones_BID2_WP-edicion-literatura_v1.md` (2026-11-07).
Source: `Draft-October.tex` = `~/Downloads/Draft-October.tex` dated 2026-11-06 17:03
(sha256 `2bbd5448…9b63`), frozen here as `Draft-October_source_20261106.tex`.
**This is not the `Draft-October.tex` in `../draft_october/`** (the 11-01 page-by-page
edit of the Overleaf zip, sha256 `de4b75d4…efa4`); none of the instruction's quoted
anchors exist in that file. Assets (`references.bib`, `Figures/`,
`MainDraft/paper_style_preamble.tex`) copied from `IADB_SpendingSmarter_action_plan.zip`.

Baseline compile of the untouched source: 62 pages, no errors, no undefined citations or references.

## Pass 1 — mechanical cleanup (2026-11-07)

Line numbers are those of the source before editing.

| # | Line | Before | After |
|---|---|---|---|
| M1 | 107 | Paragraph "Our first experiment examines demographic aging under the contribution-rate adjustment … at ages 65--69." (879 chars) | Deleted. The paragraph "Using the calibrated model, we first examine …" (109) is kept. No number changed. |
| M2 | 1340 | Second version of the aggregate-effects paragraph: "Relative to CF0, reducing the replacement rate lowers pension benefits per retiree … The reduction in pension benefits encourages households … \$12.82 …" (810 chars) | Deleted, including the stray `\$12.82`. Its sentence "The combination of higher wages and lower pension contributions increases after-tax labor income, while the larger capital stock reduces the return on savings." moved into the first paragraph (1336), after the interest-rate sentence. |
| M3 | 1573 | "…as the life tables used in the first step,  The UN World Population Prospects is the natural robustness alternative and changes only the target number." | "…as the life tables used in the first step. The UN World Population Prospects provide an alternative demographic benchmark; using them would change the target dependency ratio but not the method used to construct the stationary economy." |
| M4 | 115 | `\citet{CortesEtAl2024} examines` | `\citet{CortesEtAl2024} examine`. Whole-file search `EtAl[0-9]*\} [a-z]+s ` finds no other case. (`\citet{Fioroni2010} shows`, `\citet{Lim2020} shows`, `\citet{Ozkan2025} builds` are single-author and correct.) |
| M5 | 963, 1013, 1065, 1066, 1099, 1180, 1577 | `Labour` ×4, `labour` ×2, `behaviour` ×1 | `Labor`, `labor`, `behavior`. `references.bib` untouched. |
| M6 | 1303–1306 | Table `tab:cf_welfare` rows "Men, low skill", "Men, high skill", "Women, low skill", "Women, high skill" | "Men, low education", "Men, high education", "Women, low education", "Women, high education" |
| M6 | 1322, 1353 | Figure notes of `fig:cf_lambda_cf0` and `fig:cf_lambda_menu`: "High-skill individuals are represented by \serone{high skill} and low-skill individuals by \sertwo{low skill}" | "High-education individuals are represented by \serone{high education} and low-education individuals by \sertwo{low education}" (both notes) |
| M6 | — | No other "skill" in Sections 5–6 prose. | **Figure PDFs:** `Figures/cf_lambda_age_cf0.pdf` and `Figures/cf_lambda_age_menu.pdf` print "Men, high skill / Men, low skill / Women, high skill / Women, low skill" in their legends. Not regenerated. `fig07_composition.pdf` has no "skill". |
| M7 | 1350 | `\caption{Age-Specific Welfare Effects of Benefit Reduction and Later Retirement}` | `\caption{Age-specific welfare effects of benefit reduction and later retirement}` |
| M8 | 102 (end of intro para 2) | — | Added sentence: "The pension block is a stylized pay-as-you-go benchmark rather than a representation of the full Mexican system, which also includes individual accounts (Section~\ref{subsec:government})." |
| M9 | 104 | Last sentence "We calibrate the model using patterns of medical spending over the life cycle, earnings differences by sex and education, and survival probabilities across demographic groups." | Deleted. "We discipline the model using Mexican data …" kept. |
| M10 | 6, 37–42, 44 | `%% --- Draft tools ---`, `\usepackage{xcolor}`, `\todo`, `\note`, comment "Paper style (splice review copy): Carrasco-2026 look", `\TODO`; comment "disabled for review copy: newpx loaded by paper_style_preamble" | All removed; comment now `%% --- Paper style ---`; line 6 comment now "newpx is loaded by paper_style_preamble". `xcolor` dropped from the main file because `paper_style_preamble.tex` loads it and no `\textcolor` remains. `\input{MainDraft/paper_style_preamble}` kept. |

Result: 1,599 → 1,589 lines; 22,169 → 21,947 words (wc). Compile after Pass 1: 62 pages, no errors,
no undefined citations or references. `Draft-October.tex` byte-identical to the source.

### Not changed, noted for Héctor
- Section 4.8 (line 1204) still says "high-skilled men" / "low-skilled men"; M6 is scoped to Sections 5–6 and captions.
- Section 2 (lines 271, 274, 278) still says "by skill"; Pass 3 rewrites that section.
- Section 3 formal type definition "(low-skilled, high-skilled)" and the Section 4 terms "skill premium" / "skill intercepts" left as the instruction requires.

## Pass 2 — title, abstract, health passages (2026-11-07)

Number checks before replacing text (all passed):
- $5.66$ / $12.26$ / $5.66$ / $8.78$ = $\tau^p$ row of `tab:cf_aggregates`; $+8.29$ / $+3.11$ / $+0.14$ = aggregate row of `tab:cf_welfare`.
- $\kappa = 0.185$ in `tab:cf_aggregates`, $0.1846$ in Section 5.4 prose ($0.1846 \approx 18.5\%$).
- $53.6\%$ curative / $2.0\%$ preventive in Appendix `subsec:health_evidence` (line 1575).
- $0.30$ vs $2.09$ percentage points: Section 4.6 prose (line 1147); `tab:validation` shows the same gap as $+0.003$ vs $+0.021$.

| # | Location | Before | After |
|---|---|---|---|
| T | `\title{}` (52–54) | "Fiscal Efficiency, Health, and Gender Dynamics\\ in Latin America" | "Pension Reform, Health, and Household Welfare in Mexico". Bold first line, `\\[6pt]` and `\thanks{…}` unchanged. |
| A | `abstract` (77) | 175-word abstract ("This paper examines the macroeconomic and welfare consequences …") | Instruction §3.2 text verbatim, numbers typeset as `$5.66\%$`, `$12.26\%$`, `$40\%$`, `$18.5\%$`, `$8.29\%$`, `$3.11\%$`. **209 words** (limit 250). |
| I | Introduction, end of contribution paragraph (107) | — | Added: "The estimated health block reproduces only a small part of the observed education gap in survival, generating a gap of $0.30$ percentage points in five-year survival at ages 50--64 against $2.09$ in the data. Section~\ref{subsec:health_block_evidence} shows that health remains close to its upper bound in the calibrated equilibrium, and Appendix~\ref{subsec:health_evidence} documents that most out-of-pocket medical spending in Mexico is curative, whereas the model treats medical spending as chosen before the health shock is realized." (first sentence rephrased without the colon; both numbers kept) |
| C | Conclusion, final paragraph (1417) | "Our findings are subject to several limitations. First, … Finally, the model abstracts from informal employment, …" (3 limitations) | Instruction §3.4 text verbatim ("These results are subject to several limitations. … and not only on the fiscal arithmetic of the pay-as-you-go system."). First three conclusion paragraphs untouched. |

Word counts: introduction 1,002 → 954; conclusion 392 → 487; abstract 175 → 209.
Register grep over abstract + two new passages: one hit, "and not only on the fiscal arithmetic" (Héctor's verbatim text, no "but also"; kept).
Front matter: author block, affiliations, date, `\thanks`, keywords and JEL line identical to the source (diff from `\thanks{` to `\maketitle` shows only the title line).
One-story check: 5.66→12.26 (CF0 vs 2020, τ^p), 0.14 (newborn, CF0 vs 2020), 8.29 and 3.11 (newborn, CF1/CF2 vs CF0), 0.185/0.1846/18.5 (κ under CF1) state the same comparison in abstract, introduction, Section 5 and conclusion.
Compile after Pass 2: 62 pages, no errors, no undefined citations or references.

### Noted, not changed (out of scope)
- Title page still prints "Preliminary draft -- August 2026 / Please do not cite or circulate without permission" and "Prepared for the Inter-American Development Bank, Fiscal Division". Front matter other than the title is out of scope.

## Pass 3 — literature review rewrite (2026-11-07)

Section 2 (source lines 114–358, 2,558 words) replaced by a fresh rewrite (now lines 114–154, 1,482 words
excluding comment separators). Drafted in `scratch/sec2_new.tex`, reported to Héctor in full, approved
("sixty words above is fine" for the two long subsections), then spliced. Héctor's approval covers the text as is.

| Part | Old | New | Target |
|---|---|---|---|
| Opening | 123 | 55 | ~50 |
| `subsec:lit_pension` → "Demographic Aging and Pension Reform" | 816 | 513 | ~450 |
| `subsec:lit_longevity` → "Health Capital and the Life Cycle" | 812 | 521 | ~450 |
| `subsec:lit_health` → "Health Financing and Social Insurance in Latin America" | 364 | 193 | ~150 |
| `subsec:lit_gender` → "Heterogeneity by Sex and Education" | 362 | 167 | ~200 |
| Bridge | 72 | 32 | ~50 |
| **Total** | **2,550** | **1,482** | 1,300–1,500 |

- All 40 citation keys retained; none added; none dropped. `HosseiniKopeckyZhao` resolves (references.bib line 821).
- Numerals: {3.51, 5.89, 8.58} + citation years; a subset of the old set. Dropped: 20, 40, 70 (Cortés et al. magnitudes).
- Labels `sec:lit`, `subsec:lit_pension`, `subsec:lit_longevity`, `subsec:lit_health`, `subsec:lit_gender` kept with exact names.
- Cortés et al. (2024) described once in the health-capital subsection (Mexico, partial equilibrium, education heterogeneity) and cited again in the bridge.
- No claim about what others have not done; the contribution sentence uses the §4.2 substance verbatim.

## Verification (§6), whole file, after Pass 3

1. **Register** over new Section 2 + abstract + intro/conclusion passages: hits are "factor-price" ×3 and "factor prices" ×1 (nouns), and "and not only on the fiscal arithmetic" (Héctor's verbatim conclusion text, no "but also"). The `---` hits are the `%% ----` comment separators. No Moreover/Furthermore, no em-dash in prose, no *inaction*, *price* (verb), *journey*, *apparatus*, *shell*, *landscape*, *has not been attempted*, *to our knowledge*, *we claim*.
2. **Word counts**: Section 2 1,482 (above); abstract 209 (≤250); introduction 1,002 → 954; conclusion 392 → 487.
3. **Citations**: 40/40 retained in Section 2; nothing dropped.
4. **Numerals**: new set ⊂ old set (above).
5. **Labels/refs**: all five Section 2 labels present once; log reports no undefined references and no undefined citations.
6. **Agreement**: `grep -nE "EtAl[0-9]*\} [a-z]+s "` → none.
7. **One story**: 5.66→12.26 is τ^p, CF0 vs 2020 (abstract, intro, Section 5, conclusion); 0.14 is newborn welfare CF0 vs 2020 (intro, Section 5, conclusion; abstract says "nearly unchanged"); 8.29 and 3.11 are newborn welfare CF1 and CF2 vs CF0 (abstract, intro, Section 5, conclusion); κ 0.185 / 0.1846 / "about 18.5%" is the CF1 replacement rate (abstract, intro, Section 5, conclusion). None of these appear in Section 2.
8. **Compile** (pdflatex → bibtex → pdflatex ×2, TinyTeX, assets from the zip): no errors, no undefined citations or references, **60 pages** (62 before Pass 3). BibTeX: 2 pre-existing warnings on `Arrow1963` (volume+number, empty publisher), same as the baseline; `references.bib` untouched. Overfull boxes: 4, same as the baseline.
9. **Separation**: `grep -inE "FISCUS|SHCP|Hacienda|Open Society|OSF|Reforma Fiscal"` → nothing.
10. **Untouched**: `Draft-October.tex` sha256 `2bbd5448…9b63`, identical to `~/Downloads/Draft-October.tex`. In `Draft-November.tex` the block from `\thanks{` to `\end{abstract}` minus the abstract differs from the source only on the title line; the whole Government subsection, including `eq:gov_budget`, `eq:gov_stationary` and `eq:pension_contribution`, is identical to the source. `\tau^k r K` untouched.

Output: `Draft-November.pdf` (60 pp.) copied from `build_nov/`.

## Contradictions with the specification, and what was done
- The instruction's source is not the `Draft-October.tex` in `../draft_october/` (see header). Worked from the 11-06 Downloads file in a new `draft_november/` folder.
- The instruction's working directory `Missions/BID2/` does not exist; assets copied from the zip into `draft_november/`.
- §4.2 asks the health-capital subsection to end with the Section/Appendix reference; the Cortés et al. sentence and the contribution sentence were placed just before it so the paragraph still ends on the reference.
- Section 4.8 (now line ~1,000) still says "high-skilled men / low-skilled men"; outside M6 scope, left for Héctor.
- Title page still prints "Preliminary draft -- August 2026" and "Prepared for the Inter-American Development Bank, Fiscal Division"; front matter beyond the title is out of scope.

## Post-pass edit (2026-11-07, Héctor's instruction)
| Location | Before | After |
|---|---|---|
| `\date{}` (67) | `\textit{Preliminary draft -- August 2026}\\` | Line removed. "Prepared for the Inter-American Development Bank, Fiscal Division" and "Please do not cite or circulate without permission" kept. |

## Pre-delivery review (`IDB_November_Final_PreDelivery_Review.md`), 2026-11-07 — items applied and declined

Applied (Héctor: "consider yourself if the minor changes should be done"):

| Item | Location | Before | After |
|---|---|---|---|
| A1 | Appendix B, `\paragraph{Optimizer and state space.}` | "The two grids differ in the levels of some moments, so reported levels carry the caveat while cross-economy comparisons, which the paper's results rest on, do not. A polish on the finer grid awaits the health-block specification decision of Section~\ref{sec:conclusion}." | "The two grids produce different levels for some model moments. All reported estimates and counterfactuals use the same estimation grid; finer-grid convergence of the welfare comparisons has not been established." (reviewer's text; removes an obsolete cross-reference and an unsupported inference) |
| B1 | §4.3 (757), §4.8 (992) | "low-skilled men" / "high-skilled men" ×2 each | "low-education men" / "high-education men". No "skilled" left outside the Section 3 type definition. |
| B2 | §4.1 Data, paras 2–3 | Repeated full survey names | "ENIGH, conducted by INEGI, …" and "ENASEM, harmonized as MHAS, is a panel survey …" |
| B3 | Appendix D, first paragraph | — | Added: "The 2024 wave is used for this descriptive analysis only and does not enter the baseline calibration, which uses the pooled 2016 and 2018 waves." (consistent with §4.3 and `tab:targeted_moments`) |
| B4 | §3.5 pension stylization (411) | "the object this paper prices" | "the mechanism analyzed in this paper" |
| B5 | Appendix C | `\paragraph{Two arms not run.}` | `\paragraph{Demographic dimensions held fixed.}` |
| B6 | Appendix D figure | Long caption with method note | Short caption "Composition of out-of-pocket medical spending by household income decile, ENIGH 2018 and 2024"; method note moved to `\fignote{0.95}{…}` after the label, matching the other figures. Text unchanged. |

Declined or deferred:
- **A2** (hedge the curative-spending explanation in abstract and conclusion): not applied. Both passages are Héctor's verbatim text and already say "a result we relate to" / "which we relate to", the wording the build instruction licenses; the reviewer's "may partly reflect" adds no information.
- **A3** (no-citation notice; cover date): Héctor's call, depends on whether this copy is confidential or the public WP.
- **A4** (production package): already in this folder; compiled PDF ships alongside the source.
- **B7** (0.145% in §5.3 prose vs 0.14 in table/intro/conclusion): not applied; changing numbers in Section 5 is outside the build instruction, and the table note already states the bracket [0.1448, 0.1450].
- **B8**: no action requested.
- **C** (government budget with population growth): untouched, blocked pending Diego per the build instruction. Same issue as Héctor's note to Diego of 2026-11-01 (`../draft_october/nota_Diego_gov_budget.html`), which goes further: the code form is $(r-n_p)B = \text{surplus}$ with $\tau^k r(K+B)$ on the revenue side, and that form fits all four columns of `tab:cf_aggregates` within 0.0001 while the printed form does not.

Compile after these edits: 60 pages, no errors, no undefined citations or references, 4 overfull boxes (unchanged).
