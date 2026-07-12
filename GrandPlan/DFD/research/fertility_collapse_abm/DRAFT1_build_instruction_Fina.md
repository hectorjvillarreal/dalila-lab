---
type: build_instruction
stage: "Draft-1"
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led) → paper assembly (Fina)"
title: "Draft 1 — build instruction for the rapid-fertility-collapse paper"
target: "Claude Code (Dalila) — Overleaf-ready LaTeX draft"
date_added: 2026-07-12
added_by: "Claude (Fina)"
endorsed_by: "Fina (design). Venue confirmed demography-led (Héctor, 2026-07-12)."
amended: "2026-07-12 — added anti-black-box/transparency mandate, four clarity mandates, Overleaf/LaTeX spec (Héctor). See amendment log."
depends_on:
  - "FINA_results_for_draft1_2026-07-12.md (results inventory — authoritative numbers)"
  - "STAGE4_methodology_plan_v1.md (outcome-robust M1–M5 architecture)"
  - "2b/2c/3a memos + sign-offs; SDT note; JFV cornerstone (distributed demographic half)"
compute: "Trivial. Figures re-style from figdata CSVs; no re-simulation."
status: "Ready to draft. Venue confirmed demography-led (PDR first). Produce Overleaf-ready LaTeX."
---

# Draft 1 — Build Instruction
# Rapid Fertility Collapse in Latin America

## 0. Purpose

Write Draft 1 as an **Overleaf-ready LaTeX project** from the endorsed result set. The results
synthesis is authoritative for every number. Draft 1 is a complete paper on the composition
collapse + discrimination + sufficiency; it does not wait for ENDS or ARG/CHL.

## A. Four clarity mandates (Héctor, 2026-07-12) — discharge each explicitly

The draft must be unambiguous on four things; a "black-box" impression on any is a referee risk.

1. **The model** — full specification, not prose. Equations + algorithm box in main text, ODD
   appendix (§5, §Transparency). Every parameter given a demographic interpretation.
2. **The empirical strategy** — state plainly *what identifies the discrimination*: APC curvature +
   the sign of state-dependence β, under a pre-registered decision rule (§4). Identification is
   econometric; the ABM is downstream (§Transparency, division of labor).
3. **Data limitations** — a signposted subsection, honest and complete (§2 measurement limits, §7
   inferential limits). No buried caveats.
4. **Use of the ABM** — a dedicated statement of what it is *for* (sufficiency of the surviving
   mechanism) and what it is *not* (identification; a fit-anything box), with its discipline (wall,
   falsification, pre-registered gates, non-fit convergence). §5 + §Transparency.

## 1. Venue — confirmed

**Demography-led. First target: Population and Development Review; fallback Demographic Research.**
Identification is demographic-econometric; ABM is sufficiency; framing is SDT/Esteve. Not an econ
venue (no fiscal/OLG content). Write §4 (discrimination) and §5 (model) to carry balanced weight,
§4 slightly ahead as the identification.

## 2. The arc (thread intro → conclusion)

*Pre-registered, outcome-robust discrimination: we built the fashionable reflexive-threshold model,
the data rejected it, and what survived is simpler and independently validated.* Negative results
reported prominently — they make the discrimination credible.

## 3. Structure — eight sections (R1–R5 / M1–M5)

Include a **roadmap paragraph** in §1 stating the division of labor: registries+microdata measure
the phenomenon; APC+state-dependence identify the mechanism; the ABM tests sufficiency; SDT frames.

**§1 Introduction** — phenomenon (R1); puzzle (too fast for classical theory; SDT gives direction,
not tempo); contribution stack C1–C5; the arc; the roadmap paragraph.
**§2 Phenomenon & measurement** (M1/R1+R2) — registry collapse; WB/WPP smoothing failure shown
explicitly; union composition as state variable; marriage-margin collapse (COL 20.7→11.9; CRI
0.324→0.166). **Data-limitations subsection (measurement)** here. *Figs:* Stage-1 panels; composition series.
**§3 Candidate mechanisms** (M2) — three separable hypotheses; why a smooth model can't generate a
fast nonlinear collapse; ABM introduced as the device that makes predictions separable.
**§4 Discrimination — identification** (M3/R3) — **β>0 every spec, both countries** (stabilizing,
not cascade); COL cohort-dominant + small exogenous period; CRI cohort-leaning; 2c-i individual
confirmation (ecological objection discharged); ecological caveats. State the identification
strategy explicitly. *Figs:* cohort-line pseudo-panels; APC curvature; β-CI by spec.
**§5 Model & sufficiency** (M4/R4) — see §Transparency for the full requirement. Cohort-only
headline spec; sufficiency on magnitude + late-loading, COL M3 kink reported; credibility via the
three non-fit convergences (fig2 signature); falsification; wall; κ–φ separability. **ABM =
sufficiency, not identification.** *Figs:* fig1 sim-vs-obs; **fig2 κ(b) vs APC (signature)**; fig4 TFR overlay (caveated).
**§6 Interpretation — the frame** (R5) — SDT channel-assisted compression; consensual-union base as
speed mechanism; cohort-diffusion ↔ cohort-dominance; Esteve anchor; ARG/CHL channel-absent
prediction (falsifiable). Keep R5 non-load-bearing: the paper stands on R1–R4.
**§7 Scope & limitations** (M5) — **data-limitations subsection (inferential)** here: pseudo-panel
(no true transitions until ENDS); high-cohabitation only; 15–19 excluded; no TFR-magnitude claim;
(B) deferred-not-disproven; tempo; ecological honesty.
**§8 Conclusion** — arc restated; ARG/CHL prediction as forward hook; light policy resonance; ENDS
as resolving next step.

## 4. The signature exhibit

**fig2 — κ(b) vs the 2b APC cohort effects.** A single calibrated parameter recovering an
independently-estimated feature the model never saw. §5 is built toward it. High-res / vector.

## 5. TRANSPARENCY — the anti-black-box requirement (§5 + appendix)

The model section must read as a **glass box**. Requirements:

- **Reframe the object honestly.** A parsimonious cohort microsimulation — **four interpretable
  parameters** (κ midpoint/slope/floor; φ tilt), rate-based, no free-form adaptive dynamics. Say so
  early; it pre-empts the black-box reflex.
- **Equations in the main text.** State the baseline Process-A rates; κ(b) (logistic, 3 params,
  each interpreted); φ(b) (1 param); the update/scheduling. Not prose.
- **Algorithm box** (`algorithm`/`algpseudocode`): per-period agent update + model step, enough to
  reimplement.
- **ODD protocol appendix** (Grimm et al., 2020 update; ODD+D optional given union-formation
  decisions) — Overview, Design concepts, Details. This is the community transparency standard and
  the direct answer to "black box."
- **Division of labor, stated explicitly:** identification is econometric (§4); the ABM is *never*
  asked to identify — it tests whether the surviving mechanism *suffices*. Repeat at the head of §5.
- **Calibration in the open:** targets (composition trajectory), loss (N1), optimizer,
  **pre-registered gates** (M1≥0.85, M2|Δ|≤0.10, M3 Δ²-sign — fixed before the run), free vs fixed
  parameters, the identification wall (TFR never in any loss; 11/11 checks/country), κ–φ
  separability (perturbation ratios).
- **The two things a black box can't do:** falsification (threshold removal flips collapse→rise)
  and the three non-fit convergences (esp. κ(b) midpoint = APC crossover). Frame these as the
  positive glass-box evidence.
- **Reproducibility statement:** deterministic given seeds; code + figdata available (repository
  ref); ODD appendix. A data/code availability statement near the end.

## 6. Claims discipline — HARD constraints (endorsed; non-negotiable)

1. No TFR-magnitude claim (composition only; overlay comparison-only, caveat verbatim; 3b gated on w).
2. No reflexivity claim either direction ("not warranted," never "disproven").
3. No tempo claim; defensive tempo-corrected column where TFR anchors appear (+0.10 TFR ≈ ~2% pop, MEX).
4. External validity bounded (two high-cohabitation regimes); ARG/CHL a testable implication.
5. Ecological honesty (2b cell-level; 2c-i cleared aggregation for COL; transitions await ENDS; B7 in record).
6. ABM = sufficiency, not identification.
7. Provenance style — per-row source+methodology flags (PROTO-RAG-001 spirit).

## 7. Scope of Draft 1

Complete on composition + discrimination + sufficiency. Future work / predictions (out of scope):
ENDS 2c-ii; Stage 3b TFR magnitude; ARG/CHL test; census-2022 rebasing; full Bongaarts–Feeney.
ENDS landing = revision, not restructure.

## 8. Overleaf / LaTeX project spec (Héctor: "be specific")

Produce a self-contained Overleaf-ready project under
`GrandPlan/DFD/research/fertility_collapse_abm/paper/`:

```
paper/
├── main.tex            % \documentclass[11pt]{article}; \input section files
├── preamble.tex        % packages + macros
├── sections/           % 01_intro.tex … 08_conclusion.tex, appendix_odd.tex
├── references.bib      % natbib author-year
├── figures/            % fig1_*, fig2_* (vector/high-res), fig3, fig4, stage1 panels
└── README.md           % Overleaf upload + compile notes
```

- **Class:** neutral `article` (portable; PDR is Word-side, reformat at submission).
- **Packages:** `natbib` (author-year, demography convention), `booktabs`, `subcaption`
  (small multiples), `graphicx`, `amsmath`, `algorithm`+`algpseudocode` (ABM box), `siunitx`,
  `hyperref`, `geometry`, `csquotes`. Keep the preamble minimal and portable.
- **Paths:** relative only — **no absolute Dalila paths** (Overleaf will break on them).
- **Figures:** export PDF (vector) where possible, esp. fig2; PNG at ≥300dpi otherwise; from figdata CSVs.
- **Bib starter** (verify all fields before submission — do NOT invent page/DOI): Lesthaeghe & van
  de Kaa (1986); van de Kaa (1987); Lesthaeghe (2010, PDR); Esteve, Lesthaeghe & López-Gay (2012,
  PDR); Fernández-Villaverde (2026); Grimm et al. (2020, ODD); Bongaarts & Feeney (1998, PDR);
  Manski (1993, reflection problem); Calles & Vogl (2026).
- **Compile:** pdflatex → bibtex → pdflatex ×2. Note in README.

## 9. Deliverable + gate

The `paper/` project compiling to `main.pdf`. Gate: **Fina** (structure/clarity/claims-discipline
+ the four clarity mandates + transparency), **Anne** (demographic claims), **Nina** (model
section + ODD accuracy). Then venue-template conversion.

## Amendment log

- **2026-07-12 — Héctor requirements applied.** Added §A four clarity mandates; §5 rewritten as the
  TRANSPARENCY / anti-black-box requirement (parsimony reframing, equations + algorithm box, ODD
  appendix, explicit econometric-vs-ABM division of labor, calibration in the open, falsification +
  non-fit convergence as glass-box evidence, reproducibility statement); §8 Overleaf/LaTeX project
  spec added; venue marked confirmed (demography-led). Data limitations elevated to signposted
  subsections in §2 and §7.

*Fina, 2026-07-12. Overleaf-ready, glass-box model, demography-led. For Claude Code.*
