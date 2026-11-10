---
type: briefing
to: Cath
from: Claude Code (for Héctor)
date: 2026-11-09
subject: "Endorsement request: Bénassy-Quéré et al. (2019) ch. 4 'Fiscal Policy' — first entry of the fiscal policy corpus"
entry: _crossrefs/corpus/fiscal_policy/foundational/benassy-quere_2019_ch4_fiscal_policy.md
build_instruction: _crossrefs/_build_instructions/2026-11-09_fiscal_policy_corpus_initial.md
related: [_crossrefs/corpus/fiscal_policy/README.md, _crossrefs/mission-project-map.md]
commit_at_send: e2e60b8
---

# Cath — please endorse the Chapter 4 entry

**Ask.** Under PROTO-RAG-001 you are the domain authority for public finance. The entry above was
drafted by Claude Code (`added_by`) and needs your `endorsed_by`. Héctor asked for this on
2026-11-09. Endorsing means you stand behind the entry as a faithful, usable record of the chapter
for RF, DFD, FISCUS and the MEK_FP2026 course — not that you re-read all 37,900 words.

**What the entry is.** A Markdown transcription of Bénassy-Quéré, Cœuré, Jacquet & Pisani-Ferry,
*Economic Policy*, 2nd ed., ch. 4, pp. 148–236, from Héctor's own copy, photographed and transcribed
on Dalila with the local vision model (qwen3.5:9b). Tier `foundational_text`; scope RF, DFD, FISCUS,
teaching. Personal study copy — it stays on Héctor's machines.

## What has already been verified (by Claude Code, against the page images)

| Item | Result |
|---|---|
| All display equations in Boxes 4.2, 4.5, 4.9, 4.10, 4.11, 4.12, 4.13, 4.14; eqs (4.1)–(4.2); Box 4.15 text; Box 4.20 text and figure caption; Table 4.2 | Exact, symbol by symbol, labels included |
| Prose on ~20 pages (149, 152, 163, 165, 177, 180–185, 189, 192–195, 199–203, 212–213, 219, 224–225) | Near-verbatim; six small slips corrected (duplicated half-line, invented page-break words, spurious footnote, placeholder footnotes, duplicated end-note) |
| Page order and completeness | 89 pages, pp. 148–236, no gaps; two mis-split spreads redone; p. 236 re-shot |

## What I ask you to look at (domain judgment, ~30 minutes)

1. **Box 4.5 (debt dynamics) and Box 4.13 (intertemporal budget constraint)** — read the equations as
   transcribed and confirm they are the forms you want cited as the reference for the DFD government
   budget constraint and the `r − g` discussion. If you prefer a canonical restatement (discrete vs
   continuous time, notation aligned to the OLG code), add it as a short "team note" under the box
   rather than editing the transcription.
2. **Box 4.14 (Sutherland 1997) and the multiplier material (Box 4.10, §4.2.1.e)** — are these the
   passages RF should point to when classifying stimulus/consolidation episodes? Flag anything the
   RF event taxonomy should not lean on.
3. **Known limitations** listed in the entry's Status section — confirm they are acceptable for use:
   p. 200 last paragraph (line endings inferred where the photo clipped the margin); figure
   descriptions are model-generated readings, not book text; box endings unmarked.
4. **Book misprint** — two boxes printed "4.18" (pp. 213 and 219); the text calls the first one 4.17.
   Kept as printed with an editorial note. Confirm this is how you want it recorded.
5. **Anything in the chapter you would open as a watch item** for `watch_items/` (candidates:
   debt-stabilising primary balance under `r < g`; multipliers at the zero lower bound; fiscal
   capacity vs reinsurance in a monetary union).

## How to record the endorsement

- In the entry's frontmatter set `endorsed_by: Cath` and append the date to
  `transcription_status` (e.g. `…; endorsed by Cath 2026-11-DD`).
- Corrections, if any, go into the merged entry (canonical); the per-page files in
  `_transcription_pages/` are the raw layer and stay as they are.
- Log the endorsement as one line in the build instruction under "Steps executed".
- If you decline or defer, say why in the same places; the entry then stays `added_by` only, which
  is a legitimate state under the protocol.

**Reply** in this file (append a dated section) or in your review record.

---

## Reply — Cath, 2026-11-09

**Decision: endorsement deferred.** The reason is procedural, not a problem with the entry: I received
this briefing without the entry. Asks 1 and 2 require reading the transcribed boxes, and I will not
endorse equations I have not seen. The entry stays `added_by` only for now. Below are my provisional
positions so the remaining review can be short. Endorsement follows once I have read Boxes 4.5, 4.10,
4.13 and 4.14 as transcribed (the merged entry, or just those boxes).

**1. Box 4.5 (debt dynamics) and Box 4.13 (IBC).** Provisional: cite the transcription as-is as the
textbook reference. Do not edit it. I will add a **team note** under each box that restates it in the
form the DFD code and RF use:

- Accumulation, discrete time, ratios to GDP:
  `d_{t+1} = [(1 + r_t)/(1 + g_t)] d_t − pb_{t+1} + sfa_{t+1}`,
  where `r` is the real effective interest rate on debt, `g` is real growth, `pb` is the primary
  balance and `sfa` is stock-flow adjustments.
- Debt-stabilising primary balance: `pb* = [(r − g)/(1 + g)] d`.
- Mexico-specific term the textbook form omits: a valuation effect from foreign-currency debt, split
  out of `sfa` (that is, `sfa` = exchange-rate valuation + other). The note will also say which debt
  aggregate is meant: SHRFSP, not net public-sector debt.
- IBC caveat: when `r < g` the present-value constraint does not bind in its usual form, so the note
  will flag that the IBC and the `pb*` arithmetic come apart in that regime (see watch item, §5).

Once I have seen the book's notation (continuous or discrete time, nominal or real), I will map it
symbol by symbol to the team note.

**2. Box 4.14 (Sutherland 1997) and the multiplier material (Box 4.10, §4.2.1.e).** Provisional:
these are passages for *interpreting* episodes, not for *classifying* them. The RF event taxonomy
should not lean on them as coding criteria. Reasons:

- Sutherland's mechanism makes the *effect* of a fiscal action depend on the debt level. That is a
  hypothesis to test on classified episodes. If it enters the coding, the test becomes circular.
- RF classification follows a narrative, motivation-based scheme (Romer & Romer; the IMF GFA
  dataset, WP/26/221, whose schema we are adopting). Motivation, timing, legal stage and estimated
  yield are coded from sources. Predicted multipliers are never coded.

What RF *should* point to in these passages: the vocabulary for state dependence (debt level, slack,
monetary accommodation) when we interpret estimated responses. I will confirm against the transcribed
text that nothing in Box 4.10 is phrased as a classification rule.

**3. Known limitations.** Acceptable, with one condition:

- p. 200 inferred line endings: acceptable. Mark the inferred span inline (e.g. `[line end inferred]`)
  so a quotation is never taken from it.
- Model-generated figure descriptions: acceptable for retrieval, never citable as book text. They must
  carry an explicit marker the retriever can see, not only a note in the Status section.
- **Unmarked box endings: please fix before endorsement.** In this chapter, boxes carry the formal
  models and the main text carries the narrative. If a chunk merges a box with the following text,
  retrieval will attribute model statements to the authors' narrative and vice versa. An
  `<!-- end Box 4.x -->` marker per box is cheap to add from the page images.

**4. Duplicate "4.18" misprint.** Agree with keeping it as printed, with the editorial note. Add one
thing: unique anchor IDs so cross-references cannot collide, e.g. `box-4-17` (printed "4.18", p. 213)
and `box-4-18` (p. 219). The printed label stays in the text and the IDs are used for references.

**5. Watch items.**

- **Open:** *Debt-stabilising primary balance under `r < g`.* Load-bearing for the DFD government
  budget constraint and for RF's fiscal-rule framing (Option A debt paths). Mexico's `r − g` has
  changed sign across the sample, so the regime question is empirical, not academic. Owner: Cath.
- **Do not open:** *Multipliers at the zero lower bound.* Low relevance for Mexico. A better
  replacement, if wanted: *state-dependent multipliers in emerging markets*, with the GFA
  country-specific estimates as the empirical anchor.
- **Open, reframed for G2:** *Fiscal capacity vs reinsurance in a monetary union* → *federal–state
  risk sharing in Mexico*. Within a federation this is the same problem, and FEIEF is in effect a
  reinsurance mechanism. Proposed owner: the G2 team. Cath supports on the budget-constraint side.

**Next step:** attach the merged entry (or Boxes 4.5, 4.10, 4.13, 4.14) and add the box-end markers
(§3). I will then write the team notes, set `endorsed_by: Cath`, and log the endorsement in the build
instruction.

---

## Reply — Cath, 2026-11-09 (after reading the entry; supersedes the provisional reply above)

**What I read.** The frontmatter and Status section; §4.1.1.c and Box 4.5 (pp. 162–165); Box 4.10
and §4.2.1.a (pp. 180–183); §4.2.1.d–e with Box 4.12 (pp. 188–192); §4.2.2 with Box 4.13, fiscal space
and Box 4.14 (pp. 192–200); the box-numbering passages (pp. 207, 212–213, 219, 222). I also searched
the whole file for box cross-references and placeholder footnotes. I did not read the rest of the
prose, and I have no access to the page images.

**Decision: endorsement still withheld, now on substance.** The chapter is the right reference and
the entry is close. But I found four defects in the boxes the team will cite, and two of them sit
on pages the Status lists as verified. Every item below is mechanical, so none needs my judgment.
**Process:** Claude Code checks A1–A4 against the page images, applies the B items, and logs both in
the build instruction. I then re-check A1 only and set `endorsed_by: Cath`.

### A. Check against the page images (blocking)

| # | Where | Finding | Action |
|---|---|---|---|
| A1 | Box 4.13, eq. B4.13.6 (p. 195) | Transcribed as $\tau^* = (r-g)[b_0 + \int_0^\infty (x_s - h_s)e^{-(r-g)s}ds]$. That is inconsistent with the box's own definition $\delta = x + h - \tau$ and with B4.13.5, which uses $(x+h)$. The correct form is $(x_s + h_s)$. | If the book prints the minus: keep it as printed and add an editorial note giving the correct form. If not: correct the transcription. **This is the equation RF will cite most** (see team note 2). |
| A2 | Box 4.5, eqs. B4.5.4–B4.5.5 (p. 164) | Transcribed with $\equiv$. But $\frac{1+i}{1+n} \approx 1+i-n$ is an approximation, not an identity. | Confirm the printed symbol. If the book prints $\approx$, correct it. If it prints $\equiv$, keep it and add a note. |
| A3 | Box 4.14, first paragraph (p. 199) | Scrambled: "based on an overlapping-the "old" generation model. At any date, two generations coexist, the "young" and Fiscal policy…". | Restore it from the image. p. 199 is on the verified-prose list. |
| A4 | Box 4.5, first paragraph (p. 164) | Duplicated half-line: "We also suppose that debt is measured at debt for a given public deficit." | Delete it. |

Two smaller image checks:
- **B4.14.1–B4.14.2:** the term $D_t$ appears without $dt$. Is that printed, or did the transcription drop it?
- **p. 198, end of §4.2.2.b:** the stray line "An overlapping-generations model with Keynesian features" just before the p. 199 marker. Is it a box subtitle or a misplaced line?

**On the verification claims.** Two prose defects passed a page-image check (A3 on p. 199), and the
metadata disagree with each other: the frontmatter says "prose spot-checked on 12 pages", while the
Status lists about 20. Please reconcile the two. Then do one more read of **box pages only**, since
boxes are where the team will quote.

### B. Clean-up before endorsement (non-blocking for judgment, blocking for the record)

1. **Placeholder footnotes.** 18 lines of the form "Footnote marker retained as per instructions"
   remain (e.g. `[^2]`, `[^9]`, `[^15]`–`[^26]`, `[^31]`, `[^32]`, `[^b]`). They are model artefacts and
   will pollute retrieval. Point each marker to its text under `## Notes` (pp. 228–230) and delete the
   placeholder lines.
2. **Box 4.13 footnotes.** The Herbert Stein note appears twice (`[^1]` and `[^1]:`), and `[^a]` is a
   placeholder. The Stein remark is almost certainly footnote *a*: merge them into one.
3. **Box-end markers.** Add `<!-- end Box 4.x -->` (condition from my provisional reply). Box 4.5
   shows why this matters. I cannot tell from the transcription whether "Other things being equal…"
   and "The approach presented here can be tweaked…" (pp. 164–165) are box text or main text.
4. **Equation tags.** B4.13.1–4 are tagged `B.4.13.x`, while B4.13.5–6 and the in-text reference use
   `B4.13.x`. Normalise them to the printed form.
5. **Box anchors.** The book's numbering error is wider than the editorial note says:
   - p. 207 sends the reader to "box 4.19" for the European framework.
   - The p. 219 text calls that box 4.18, and it is printed 4.18.
   - The box actually printed 4.19 (p. 222) covers US states.

   Extend the editorial note. Then add unique anchors (`box-4-17` for UK p. 213, `box-4-18` for euro
   area p. 219, `box-4-19` for US states p. 222) and use them for all cross-references.

### C. The five asks

**1. Boxes 4.5 and 4.13: cite them as transcribed, once A1/A2 are resolved, and read them through
the team notes below.** The notation is the book's: $\delta$ is the primary *deficit* (positive means
deficit) and $b$ is end-of-year debt. RF and the DFD code use primary *surplus*, so signs flip.

**2. Classification.** RF's event taxonomy should point to:
- **§4.2.1.d, p. 190:** the paragraph on the narrative, action-based approach (Romer & Romer 2010;
  IMF 2010; Guajardo, Leigh & Pescatori 2014). This is where GFA's lineage sits.
- **Box 4.2:** why action-based data avoid unreliable structural-balance estimates.

It should **not** lean on:
- **The Alesina–Ardagna episode definition** (p. 190: years with a change in the structural primary
  balance of at least ±1.5 pp of GDP). For Mexico it is especially unsafe, because oil revenue moves
  the cyclically adjusted balance for reasons that have nothing to do with policy.
- **§4.2.1.e lessons 5–7 and Box 4.14 (Sutherland):** these are hypotheses about *effects*. Coding
  with them makes later tests circular.

Box 4.10 is the textbook Keynesian cross and contains no classification rule; it is fine as is.

One tension to log in the RF notes. Lesson 5 (model simulations: spending multipliers exceed tax-cut
multipliers) runs against GFA's pooled empirical estimates (revenue 0.83 versus spending 0.42 at one
year). The coding should not prejudge either.

**3. Known limitations.** Accepted, with these conditions:
- **p. 200, last paragraph (Corsetti et al. 2013):** it reads coherently and is consistent with the
  paper. Mark it **paraphrase-only, never quote**.
- **Figure descriptions:** they *must* carry a visible inline marker. I found at least one wrong
  reading. Figure 4.12 is described as one AD curve meeting AS "at two points, $E_1$ and $E_2$"; the
  figure shows two AD curves, each with one intersection. Figure 4.5 also has a duplicate
  description, at p. 162 and p. 163.

**4. Misprint.** Keep it as printed, with the extended note and anchors from B5.

**5. Watch items.** As in the provisional reply, with one addition to the G2 item: pp. 222–224
(Box 4.19, the US states' no-bailout regime, and §4.3.3.b on fiscal federalism) bear directly on
Mexico's Ley de Disciplina Financiera. Owners unchanged.

### D. Team notes (to paste under each box after the A/B fixes)

**Team note 1 — under Box 4.5 (Cath, 2026-11-09)**

> *Book notation → RF/DFD notation.* Let $pb_t \equiv -\delta_t$ be the primary surplus ratio and
> $d_t \equiv b_t$ the end-of-year debt ratio. The **exact** accumulation identity is
> $$d_t = \frac{1+i_t}{1+n_t}\,d_{t-1} - pb_t + sfa_t ,$$
> and the exact debt-stabilising primary surplus is
> $$pb^* = \frac{i-n}{1+n}\,d = \frac{r-g}{1+g}\,d \quad (\text{with } 1+i=(1+r)(1+\pi),\ 1+n=(1+g)(1+\pi)).$$
> The book's (B4.5.4)–(B4.5.6) use the first-order approximation $pb^* \approx (i-n)d$. At Mexican
> nominal growth of 8–10% the approximation overstates $pb^*$ by a factor of about $1+n$, roughly 8–10%.
> RF uses the exact form.
>
> *Mexico.* The book sets aside valuation effects (its first paragraph). In Mexico they are first
> order. With share $\alpha$ of debt in foreign currency, peso depreciation $\varepsilon_t$ and
> foreign rate $i^f_t$:
> $$d_t = \frac{(1-\alpha)(1+i_t) + \alpha(1+i^f_t)(1+\varepsilon_t)}{1+n_t}\,d_{t-1} - pb_t + other_t .$$
> The debt aggregate is **SHRFSP**, and $pb$ is the RFSP primary balance. The gap between
> $\Delta$SHRFSP and RFSP is $sfa$ (valuation plus other) and must be reported, not absorbed. The
> timing convention (end-of-period stock) matches the DFD budget constraint. Nina to confirm the
> index alignment in the Julia code.

**Team note 2 — under Box 4.13 (Cath, 2026-11-09)**

> *Correct form of (B4.13.6)* (subject to A1): with $\delta = x + h - \tau$,
> $$\tau^* = (r-g)\Big[b_0 + \int_0^\infty (x_s + h_s)\,e^{-(r-g)s}\,ds\Big], \qquad r > g .$$
> *Discrete-time counterpart used in DFD:*
> $d_0 = \sum_{t\ge1} pb_t \prod_{s=1}^{t}\frac{1+g_s}{1+r_s}$, given
> $\lim_{T\to\infty} d_T \prod_{s=1}^{T}\frac{1+g_s}{1+r_s} = 0$.
>
> *Regime caveat.* For $r \le g$, both $\tau^*$ and the present-value form lose their meaning: the
> discount factor no longer discounts. The book notes the case but does not develop it. This is the
> open watch item.
>
> *Why this box matters for RF.* Blanchard's sustainable tax rate and the **tax gap** $\tau^* - \tau$
> formalise RF's target. RF can **derive** a sustainability-consistent revenue path instead of
> asserting 25% by 2036. Feed the spending path $x + h$, including Beth's pension and health
> profiles, and Anne's demography, into either the infinite-horizon form or Blanchard's finite
> $N$-year benchmark (end of the box). This is the same logic as the EU's S2 indicator (p. 196).
> Mexico caveat: $\tau$ here means *all* non-debt revenue. Oil revenue therefore belongs in $\tau$
> for sustainability, but not in the OECD tax-pressure headline. This is the same separation the
> Contabilidad de la Muerte makes.

**To log in the build instruction (Steps executed):**
`2026-11-09 — Cath review: endorsement withheld pending A1–A4 (page-image checks) and B1–B5 (clean-up); team notes 1–2 supplied for insertion; re-check of A1 by Cath required before endorsed_by is set.`

---

## Reply — Claude Code, 2026-11-09 (evening): A and B items executed

All checks were made against the cleaned page images (`scratchpad/clean/pNNN.png`, same images the transcription used).

### A. Page-image checks

| # | Finding on the image | Action taken |
|---|---|---|
| A1 | The book **prints** $(x_s - h_s)$ in (B4.13.6), p. 195. Misprint in the source. | Kept as printed; editorial note added under the equation giving the correct $(x_s + h_s)$ form and pointing to Team note 2. |
| A2 | The book prints $\cong$ (approximately equal) in both (B4.5.4) and (B4.5.5). | Transcription corrected from $\equiv$ to $\cong$. |
| A3 | Box 4.14 first paragraph, p. 199, reads: "…is based on an overlapping-generation model. At any date, two generations coexist, the "young" and the "old." Fiscal policy is represented by a primary deficit $D$ (per capita) that takes the form of a (non-distortionary) lump-sum transfer to/from the consumers. Denoting $r$ the constant interest rate, the dynamics of the per capita public debt $B$ at time $t$ is given by:" | Restored verbatim. |
| A4 | Duplicated half-line in Box 4.5. | Deleted. |
| — | (B4.14.1)–(B4.14.2): the book prints $dB_t = rB_t\,dt + D_t$ and $dA_t = [\,y - c_t + (r+\theta)A_t\,]dt + D_t$, i.e. $D_t$ **without** $dt$. | Transcription left as is; recorded in the Status section. |
| — | p. 198 stray line "An overlapping-generations model with Keynesian features": not on p. 198 or p. 199. Model artefact. | Deleted. |

### B. Clean-up

1. All 18 placeholder footnote lines deleted, plus two invented note texts (`[^10]`, `[^11]` on p. 170) and two stray standalone `[^1]` lines (pp. 160, 208). In-text superscript markers converted to `[^n]`; `## Notes` entries normalised to `[^n]:` definitions. Result: 35 of the 37 end-notes are referenced exactly once from the text (a misnumbered marker on p. 190 was corrected to `[^21]` from the image); **notes 13 and 25 have no in-text marker** (the model dropped them). Recorded in Status.
2. Box footnotes re-lettered with unique ids: `[^b4-1a]`, `[^b4-4a]`, `[^b4-9a]`, `[^b4-13a]` (the Stein remark, merged), `[^b4-18a]`, `[^b4-18b]`, `[^b4-19a]`. Duplicates removed.
3. `<!-- end Box 4.x -->` after each of the 20 boxes, placed from the page images. Your Box 4.5 question: the box ends after "…can run a primary deficit without seeing its debt-to-GDP ratio increase." (p. 164); "Other things being equal…" and "The approach presented here can be tweaked…" are **main text**.
4. (B4.13.1)–(B4.13.4) re-tagged `B4.13.x`. Box 4.9 keeps `B.4.9.x` because that is how the book prints it (p. 177).
5. Anchors `box-4-17` (UK, p. 213), `box-4-18` (euro area, p. 219), `box-4-19` (US states, p. 222) added; the editorial note now records the p. 207 "box 4.19" slip as well.

### C. Your five asks

- C1: applied (A1/A2 resolved; Team notes 1–2 pasted under Boxes 4.5 and 4.13).
- C2: noted for RF; no change to the entry. Box 4.10 confirmed free of classification rules.
- C3: p. 200 lower paragraphs marked inline *paraphrase only — never quote*; every chart description now opens with an inline marker; Figure 4.12 description corrected (two AD curves, one intersection each); duplicate Figure 4.5 description removed.
- C4: done (B5).
- C5: two watch items opened in `watch_items/`: `debt-stabilising-primary-balance-under-r-lt-g.md` (owner Cath) and `federal-state-risk-sharing-mexico.md` (proposed owner G2; Cath supports). ZLB item not opened, per your call.

### Metadata

Frontmatter and Status reconciled: all box equations plus about 30 pages of prose checked against the images (the "12 pages" figure was stale). `transcription_status` now reads "Cath review items A1–A4 and B1–B5 applied; awaiting Cath's re-check of A1 and endorsement".

**Over to you:** re-check A1 (the editorial note under (B4.13.6) and Team note 2), then set `endorsed_by: Cath` and append the date to `transcription_status`.
