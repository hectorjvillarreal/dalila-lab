# Paper — Rapid Fertility Collapse in Latin America (Draft 1)

Overleaf-ready LaTeX project. Built per `../DRAFT1_build_instruction_Fina.md`
(Fina, 2026-07-12); every number traces to `../FINA_results_for_draft1_2026-07-12.md`
and the endorsed stage memos.

## Overleaf upload

Zip this `paper/` directory (or drag it in whole) — it is self-contained:
`main.tex`, `preamble.tex`, `references.bib`, `sections/`, `figures/`.
All paths are relative; `\graphicspath{{figures/}}` is set in the preamble.

## Compile

pdflatex → bibtex → pdflatex → pdflatex (Overleaf's default latexmk does this
automatically; set the compiler to **pdfLaTeX**).

Note (Dalila convention): LaTeX compiles in Overleaf, not locally — only static
checks are run on Dalila.

## Structure

- `sections/01_intro.tex` … `08_conclusion.tex` — the eight sections (Fina §3)
- `sections/appendix_odd.tex` — ODD protocol appendix (Grimm et al. 2020)
- `figures/` — vector PDFs for all model/econometric figures; PNG for the
  Stage-1 registry charts. Regenerate from figure data:
  - Stage 3a: `model/_render_figures_3a.py` (reads `outputs/stage3a/figdata/`)
  - Stage 2b: `model/stage2b_figures.py` (reads `outputs/stage2b/figdata/`)
  No re-simulation needed for re-styling.

## Bib discipline

`references.bib` entries marked `VERIFY` carry incomplete fields on purpose —
complete them against the sources before submission; do not invent pages/DOIs.

## Gate

Fina (structure/clarity/claims discipline + transparency mandates) → Anne
(demographic claims) → Nina (model section + ODD accuracy) → venue template
conversion (PDR first target; fallback Demographic Research).
