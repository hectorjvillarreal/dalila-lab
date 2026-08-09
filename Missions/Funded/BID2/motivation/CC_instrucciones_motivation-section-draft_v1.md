# Claude Code — Write the BID2 motivation section (standalone `.tex` for Overleaf)

**Mission:** BID2 · health-refocused paper
**Working folder:** `~/Dalila/Missions/Funded/BID2/motivation/`
**Branch:** `p3-correcciones-tex`
**Output:** `draft/motivation_section.tex` (new file)

## What this task is, and what it is not

The motivation build produced twelve figures and enough findings for several
papers. This task produces **one section**. The hardest part is not writing —
it is leaving things out.

Read first, in this order: `output/READTHIS.md`, then `output/NUMBERS.md`, then
`output/VERIFICATION.md`, then `provenance.md` for any decision you need to
check. The coauthor briefings in `_crossrefs/team/{anne,beth,judy,fina}/` are
context, not content to transcribe.

**Do not modify `Draft-June-v6.tex` or any other paper file.** Produce one new
standalone `.tex` containing a single `\section{...}` and its subsections, which
Héctor and Diego will place into the paper later. Do not renumber anything, do
not create a v7, do not touch the preamble.

**Scope ceiling: 1,400–1,800 words of body prose, at most four figures in the
section.** If the draft runs longer, cut rather than compress — a motivation
section earns its place by making the reader want the model, not by exhausting
the evidence. Everything omitted stays available in the build outputs and can be
pointed to in a footnote or a data appendix.

---

## What the section must accomplish

The paper's argument is that health belongs at the analytical center: medical
spending in Mexico is overwhelmingly a *response to a realized health shock*
rather than smooth investment in a health stock, and because the capacity to
respond is unequal, a transitory shock becomes a persistent one through the
budget constraint. The section's job is to establish, from data, the premises
that argument needs, and then hand off to the model.

Structure it as three facts and a corollary, closing with the bridge to the
model:

1. **Age gradient and sex differences** — the empirical counterpart of the
   model's $m_j$. Lead with the estimated age-sex profile, the agreement of the
   two independent allocation methods (correlation 0.959 across the 18 cells),
   and the shape's stability across waves. The agreement between methods is the
   evidence the profile is real; say so explicitly, because a reader's first
   objection is that the profile is an artifact of the allocation rule.
2. **Unequal capacity to spend** — the flat unconditional budget share is an
   artifact of zeros; conditional on spending, poor households devote a larger
   share; catastrophic incidence falls from roughly 4–5% in the poorest deciles
   to about 1% in the richest; and the age gradient itself is several times
   steeper in the top income tercile. That last point is the one the model needs
   most: inequality lives *inside* the age profile.
3. **Curative dominance** — under the stated classification, unambiguously
   preventive items are about 2% of out-of-pocket spending, unambiguously
   curative 52–66%, with 38–44% genuinely ambiguous. ENSANUT's direct
   observation of the *motive* of care is consistent. Present the classification
   as a stated, auditable judgment with a bracket, not as a measured share.
4. **The corollary — low spending among the poor is unmet need, not good
   health** — on four independent lines: excess zeros among poor households;
   ENSANUT's direct forgone-care gradient (about 19% to 9% across wellbeing
   terciles, with cost-attributed forgone care collapsing from about 3.5% to
   0.1%); the ENASEM panel response to frailty decline; and the 2020 episode.
5. **The bridge to the model** — a short closing that names what the model must
   contain to reproduce these facts: health as a stock subject to shocks, medical
   spending as restoration rather than smooth investment, and a budget constraint
   that binds differently by type. Do not restate the model; point to it.

---

## The 2020 episode — its own subsection, tightly fenced

Héctor's ruling: this is a **subsection, not a footnote**. It is the strongest
single piece of evidence in the section, because the collapse of the zeros when
public provision failed converts "zeros indicate unmet need" from an
interpretation of a cross-section into an observation in time.

Report: real household out-of-pocket spending rose in every decile (+76% in the
poorest, +29% in the richest); the margin was **participation, not intensity**
(zero-spending fell 13–15 pp in every decile while conditional-on-positive
amounts rose far less); the shift never reversed through 2024; and the food
placebo was flat to negative. Quote growth rates and peso contributions together
or neither — the top two deciles still financed about 36% of the aggregate jump,
and the two framings tell opposite stories.

Fence it. Keep causal language soft: two waves and one placebo cannot fully
exclude a health-specific reporting change, and the section must say so. Include
**one sentence** stating that the episode merits separate treatment which this
paper does not pursue. Then stop. No event study, no external utilization
series, no welfare accounting, no heterogeneity by insurance — those belong to a
different project and must not grow inside this section.

---

## Standing rules the prose must not violate

These are not stylistic preferences; each corresponds to something the data
cannot support.

1. **ENIGH gives shapes and gradients, never levels.** It captures 22–34% of
   GHED out-of-pocket per capita and sits 3–4× below ENASEM's observed 50+
   spending. No peso figure may be presented as a national total or a level.
   Ratios, gradients, and shapes only.
2. **The preventive share is a bracket (2%–46%), not a number.** The licensed
   phrase is **"majority curative."** "Overwhelmingly curative" holds only under
   the base and curative-leaning assignments and must not appear unqualified.
3. **The ages 5–14 Tier-3 cell is embargoed.** Do not quote it. Tier-3 results
   are always "estimated," never "observed."
4. **No composition trend across waves.** The 2024 COICOP recode drops
   prescription status, so the 2018-vs-2024 curative/preventive split is *not*
   comparable. Quote the composition cross-sectionally only. **Note:** the
   direction currently stated in `READTHIS.md` is backwards — it says the recode
   shifts items from ambiguous to curative, but the tables show the ambiguous
   block *growing* from 38.0% to 44.5%, which is what dropping prescription
   status would do. Correct that sentence in `READTHIS.md` and `provenance.md`,
   and never reproduce the wrong direction in the draft.
5. **ENASEM patterns are descriptive, not causal.** Wealth bundles insurance,
   education, prior health, and access. Use "is associated with," not "causes"
   or "leads to." State the caveat in the text, not only in a figure note.
6. **The frailty index is a reconstruction, provisional pending Judy.** Any
   sentence resting on it carries that qualification. It reproduces her
   published results qualitatively, not numerically.
7. **All profiles are out-of-pocket only.** The IMSS/ISSSTE/SSA in-kind
   component is absent throughout; say this once, clearly, in the section.

---

## One analytical caution on fig 10

The mortality panel of `fig10_enasem_dynamics.png` is **not age-adjusted**, and
unconditional mortality by wealth tercile in `VERIFICATION.md` is flat to
inverted (5.1% / 6.7% / 6.6%), which is very likely age composition — wealth
accumulates, so higher terciles are older in a 50+ panel.

Therefore, in this draft:
- **Use the spending-response result** (response roughly doubles from bottom to
  top wealth tercile) as the main ENASEM evidence. It is the finding the model's
  mechanism needs.
- **Treat the survival gradient cautiously.** Either state it with an explicit
  sentence that it is not age-adjusted and that wealth terciles differ in age
  composition, or omit it from the section. Do not present it as a clean result.
  Flag this choice at the top of the file for Héctor's decision.

Do not attempt the age adjustment as part of this task — that is a separate,
scripted rerun.

---

## Figures

At most four in the section. Recommended set, but propose alternatives at the
top of the file if the prose argues otherwise:

- `fig01_age_sex_profile.png` — the headline profile (Fact 1).
- `fig07_composition.png` — curative/ambiguous/preventive composition (Fact 3).
- `fig06_forgone_care.png` — the direct unmet-need measurement (corollary).
- `fig12_pandemic_jump.png` — the 2020 episode.

Reference the others (fig 2 validation, fig 3 tercile gradients, fig 5 zeros,
fig 8 catastrophic, fig 10 dynamics, fig 11 stability) in the text or footnotes
without reproducing them; note that they are available for an appendix if
Héctor wants one.

Use `\includegraphics` with the `.pdf` versions where available. Every figure
needs a caption stating source, wave, and — where applicable — that the profile
is estimated under an allocation rule. Follow the label conventions already used
in `Draft-June-v6.tex` (`fig:`, `tab:`, `sec:`), and choose label names that
cannot collide with existing labels in that file.

Write a **figure manifest** at the end of the file, as a LaTeX comment: the exact
list of image files that must be uploaded to the Overleaf project for the
section to compile.

---

## Numbers, citations, and register

Every number in the prose comes from `output/NUMBERS.md` or the per-figure
tables. Never read a value off a figure. If a number the prose wants is not in
`NUMBERS.md`, do not invent or recompute it inline — leave a clearly marked
`% MISSING:` comment and continue.

Cite the three surveys, GHED, and the frailty-index sources (Searle et al. 2008;
Hosseini et al. 2021). **Check `references.bib` first.** If the keys exist, use
them. If they do not, follow the convention already in the paper and write those
citations as plain text in the prose rather than adding new `.bib` keys, so the
section compiles against the existing bibliography without edits. Record in the
file header which route was taken.

Register: continuous economic prose, no bullet lists in the body, machinery kept
out of the text. This is a section a busy reader must be able to read straight
through. Method detail (allocation tiers, classification mechanics, design-based
estimation) belongs in a compact methods footnote or a pointer to the build
outputs, not in the body.

---

## File header

Open the file with a LaTeX comment block recording: build date; source of every
number (`NUMBERS.md`, branch `p3-correcciones-tex`); the fig 10 decision flagged
for Héctor; the citation route taken; candidate placement in the paper (this is
a new section following the introduction — state it as a suggestion, since
Héctor and Diego will decide); and the figure manifest.

## Verification before commit

1. Word count of body prose is within 1,400–1,800; at most four figures.
2. Every numeral in the prose traces to `NUMBERS.md` or a per-figure table. Grep
   your own draft and check them one by one.
3. Forbidden content absent: no 5–14 age cell; no peso level presented as a
   total; no unqualified "overwhelmingly curative"; no 2018-vs-2024 composition
   trend; no causal verb attached to an ENASEM result; no frailty-based claim
   without the provisional qualifier.
4. Brace balance zero; `\begin`/`\end` balanced; no label that collides with
   `Draft-June-v6.tex`.
5. `READTHIS.md` and `provenance.md` COICOP direction corrected.
6. The section reads end to end as prose, and a reader who stops after it knows
   what the model has to explain.

## Commit

Commit `draft/motivation_section.tex` and the two corrected documentation files
on `p3-correcciones-tex` with a message such as:
`BID2: draft motivation section from the multi-source build; correct COICOP direction in build docs`
