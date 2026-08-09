# Overleaf project — BID2 draft motivation section

Self-contained. Everything needed to compile is in this folder; nothing else
has to be uploaded.

## To use

Upload `overleaf_motivation.zip` (one level up) via **New Project → Upload
Project** in Overleaf, or drag the five files below into an empty project.
`main.tex` is the main document. Compile with pdfLaTeX. No bibliography run is
needed.

| File | Role |
|---|---|
| `main.tex` | preamble + `\input{motivation_section}`; mirrors `Draft-June-v6.tex` |
| `motivation_section.tex` | the section itself — the only file that moves into the paper |
| `fig01_age_sex_profile.pdf` | Figure 1 — age–sex profile, both allocation methods |
| `fig07_composition.pdf` | Figure 2 — curative / ambiguous / preventive composition |
| `fig06_forgone_care.pdf` | Figure 3 — forgone care by socioeconomic tercile and insurance |
| `fig12_pandemic_jump.pdf` | Figure 4 — the 2018→2020 jump, with the food placebo |

## When the section goes into the paper

Discard `main.tex`. Move `motivation_section.tex` and the four PDFs to the
`Draft-June-v6.tex` project root and add, after the introduction:

```latex
\input{motivation_section}
```

`Draft-June-v6.tex` already loads everything the section needs (`graphicx`,
`float` for the `[H]` specifiers, `caption`, `hyperref`), and the section's
labels all use a `mot_` prefix, which collides with nothing in that file. Two
things in `main.tex` exist only for the preview and must not travel with the
section: the `\newlabel` stub for `\ref{sec:model}`, which has a real target in
the paper, and the title block.

## Canonical copy

The section is maintained at `../draft/motivation_section.tex`. The copy here
is a snapshot for upload — edit the canonical file and re-copy rather than
editing this one, or the two will drift.

## Reading the section

Decisions, caveats and the number provenance are in the comment header of
`motivation_section.tex`. Two are worth knowing before you read:

- The fig 10 survival gradient is **omitted** from the body. It is not
  age-adjusted and is non-monotone across the lower two wealth terciles; the
  spending-response result carries the ENASEM evidence instead. The drafted
  sentence is parked as a comment in `\subsection{Low spending among the poor
  is unmet need}` if it should come back.
- Catastrophic incidence is quoted from the tables (3.9% in decile 1 against
  1.4–1.9% in deciles 4–10, 2024), not from the "4–5% to 1%" paraphrase in
  `output/READTHIS.md`, which overstates the spread.

Every numeral traces to `../output/NUMBERS.md` or a per-figure table in
`../output/tables/`.
