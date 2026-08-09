# Overleaf project — BID2 draft motivation section

Self-contained. Everything needed to compile is in this folder; nothing else
has to be uploaded.

## To use

Upload `overleaf_motivation.zip` (one level up) via **New Project → Upload
Project** in Overleaf. `main.tex` is the main document. Compile with pdfLaTeX.
No bibliography run is needed.

Use the zip rather than dragging files from this folder: everything here except
`main.tex` and this README is a **symlink** into the repo (see *Sync* below),
and the zip is where those symlinks are resolved into real files.

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

## Sync

There are no copies to keep in step. `motivation_section.tex` and the four PDFs
in this folder are symlinks:

    motivation_section.tex     -> ../draft/motivation_section.tex
    fig01_age_sex_profile.pdf  -> ../output/figures/fig01_age_sex_profile.pdf
    fig07_composition.pdf      -> ../output/figures/fig07_composition.pdf
    fig06_forgone_care.pdf     -> ../output/figures/fig06_forgone_care.pdf
    fig12_pandemic_jump.pdf    -> ../output/figures/fig12_pandemic_jump.pdf

Edit `../draft/motivation_section.tex` or re-run the figure scripts, and this
folder follows automatically. `main.tex` and this README are the only real
files here, and neither travels into the paper.

The one artifact that *can* fall behind is `../overleaf_motivation.zip`, since
a zip is a snapshot by nature. Two things keep it honest:

- `../scripts/build_overleaf_project.py` rebuilds it from the symlink targets.
  It is deterministic, so rebuilding without a content change produces no diff.
  `--check` reports staleness without writing, exit 1 if stale.
- A pre-commit hook (`../scripts/pre-commit-hook.sh`) runs that rebuild and
  stages the result whenever a commit touches `draft/`, `output/figures/` or
  `overleaf_motivation/`. So a committed zip always matches the committed
  sources.

The hook lives in `.git/hooks/pre-commit`, which git does not version. That file
also carries the automotive-board hook, and **re-running the board's install
line replaces the whole file**, removing the two-line dispatch to this one. If
the zip ever starts drifting, that is the first thing to check; the lines to
re-add are in the header of `../scripts/pre-commit-hook.sh`.

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
