# CC INSTRUCTIONS — BID2 · Replication package for the composition figure

**Version:** v1 · **Date:** 2026-08-30 · **Mission:** BID2 (IADB Fiscal Division)
**Working base:** `~/Dalila/Missions/Funded/BID2/motivation/`
**Deliverable:** a self-contained directory that regenerates
`fig07_composition.pdf` from cleaned data, offline, on a machine that has never
seen the survey microdata.
**Edit mode:** creates new files. **Does not modify** the paper, the draft, or
any existing build artifact.

---

## 0. What is being built and why

The paper reports three numbers from this build — 2.0 per cent unambiguously
preventive, 53.6 per cent unambiguously curative, 44.5 per cent ambiguous — and
one figure. A reader must be able to reproduce both without INEGI credentials,
without a network connection, and without the multi-gigabyte raw survey files.

The package therefore ships **derived, aggregated data only**, plus the code that
turns it into the figure, plus enough provenance to trace every cell back to the
build that produced it.

**This is a packaging task. Nothing is re-estimated, re-derived, or recomputed
from raw microdata.** The published numbers are the published numbers.

---

## 1. Phase 1 — Discovery. Report before building anything.

Do not create a single file until this phase is reported.

1. **Identify the generator.** Find the script that produced
   `output/figures/fig07_composition.pdf`. Report its path, its language, and its
   version requirement. The build documentation describes scripts `00–11` under R
   4.4.3, and the figure's styling is consistent with `ggplot2`. **Héctor has
   asked for Python.** Determine and report which of these is true:
   - the generator is R, and a Python version does not exist;
   - the generator is Python;
   - both exist.

   **Do not port anything in this pass.** Report the finding; the language
   decision is Héctor's and is discussed in §6.

2. **Identify the minimal data the figure needs.** The figure shows the
   preventive / ambiguous / curative composition share by household income decile,
   for 2018 and 2024. That is at most sixty cells. Report the exact input the
   generator reads — file path, format, columns, row count — and whether it reads
   a prepared aggregate or does its own aggregation from a larger derived file.

3. **Identify the classification table.** The figure note cites
   `output/tables/curative_preventive_classification.csv`. Report its path, its
   size, its columns, and whether it contains item-level rubro codes and labels
   only, or anything household-level.

4. **Report the provenance chain** for the three headline percentages: which
   entry in `output/NUMBERS.md` carries each, and which script wrote it.

5. **Report anything upstream that is not redistributable** — raw ENIGH, ENSANUT
   or ENASEM extracts, intermediate files containing household identifiers, or
   any file above roughly 10 MB.

**Stop and report.** Wait for approval before Phase 2.

---

## 2. Phase 2 — Package layout

Build under `~/Dalila/Missions/Funded/BID2/motivation/replication/`. Do not build
inside `output/` or `draft/`.

```
replication/
  README.md
  MANIFEST.md
  run_all.sh
  data/
    composition_by_decile.csv
    curative_preventive_classification.csv
    headline_shares.csv
  code/
    make_fig07_composition.<ext>
  environment/
    <lockfile>
  output/
    fig07_composition.pdf        # produced by run_all.sh, not committed by hand
```

Exact filenames may differ if the discovery phase shows better ones; report any
deviation.

---

## 3. Data rules — the part that matters most

1. **Derived and aggregated only.** No raw survey microdata. No household-level or
   individual-level records. No identifiers of any kind. If a candidate file
   contains one row per household, it does not go in the package.
2. **No suppression risk.** The figure's cells are decile-by-year composition
   shares, which are large aggregates. Report the minimum unweighted cell count
   behind any published cell. If any cell rests on fewer than roughly thirty
   observations, report it and do not ship that cell without instruction.
3. **CSV, UTF-8, with a header row.** No `.rds`, no `.parquet`, no pickles — the
   package must be readable by someone with neither R nor the original toolchain.
4. **Every column documented** in `README.md`: name, type, units, and what a row
   is.
5. **Values are copied, never recomputed.** If a value in the shipped CSV differs
   in any digit from the value in the build output, that is a defect. Report it;
   do not reconcile it silently.
6. **Licensing and attribution.** ENIGH and ENSANUT are INEGI products and ENASEM
   has its own access terms. The package redistributes derived aggregates, not
   source microdata. `README.md` must state the source surveys, the years, that
   only derived aggregates are distributed, and where a reader obtains the
   originals — as a citation, **not as a download script**.

---

## 4. Offline and determinism rules

1. **No network access at any point in `run_all.sh`.** No downloads, no package
   installation from a remote index, no API calls, no font fetching. If the
   generator currently downloads anything, report it.
2. **Pin the environment.** Ship a lockfile — `renv.lock` for R, or
   `requirements.txt` with exact pinned versions for Python — and record the
   interpreter version used. Do **not** vendor the packages themselves unless the
   total stays small; report the size if you consider it.
3. **Deterministic output.** The figure must not depend on a random seed, a
   locale, or a system date. If the generator sets a seed, keep it and document
   it. If it depends on locale for decimal or thousands separators, set the locale
   explicitly in the script.
4. **`run_all.sh` runs from a clean checkout in one command**, reads only from
   `data/`, writes only to `output/`, and exits non-zero on any failure. It must
   not require the working directory to be anything in particular — resolve paths
   relative to the script's own location.

---

## 5. Verification — this is the acceptance test

1. Copy the `replication/` directory to a scratch location outside the repository,
   with no access to `output/` or the raw data.
2. Run `run_all.sh` there.
3. Compare the produced PDF with the published `output/figures/fig07_composition.pdf`.
   Report: whether they are byte-identical; if not, whether they are visually
   identical; and if not, exactly what differs. Rasterize both with
   `pdftoppm -jpeg -r 150` and compare if a byte comparison fails, which it may
   for benign reasons such as an embedded timestamp.
4. Report the run time and the peak memory.
5. Confirm the run made no network calls. If the environment permits, run with
   networking disabled and report the result.

**A package that does not pass step 3 is not delivered.** Report the failure
rather than adjusting the figure to match.

---

## 6. The language question — report, do not decide

Héctor asked for Python. If the discovery phase finds the generator is R, there
are three options and **the choice is his**:

- **Ship the R generator as it is.** The safest: it is the code that produced the
  published figure, so the package is exact by construction.
- **Ship a Python reimplementation.** Requires that the Python figure be verified
  visually identical to the published one under §5. A reimplementation that
  produces a *slightly* different figure is worse than no reimplementation,
  because the package would then not reproduce the paper.
- **Ship both**, with the R script designated as canonical and the Python script
  as a convenience, both verified.

Report the options with an estimate of the porting effort and any feature of the
plot that would be awkward to reproduce in `matplotlib`. **Do not begin a port
without approval.**

---

## 7. MANIFEST.md

One table listing every file in the package with: path, SHA-256, size in bytes,
what it is, and where it came from — the script and the repository path that
produced it. Include the commit hash of the build repository at packaging time,
and the branch. State plainly that the manifest covers the package only and that
the raw microdata is not included.

---

## 8. README.md

Written for someone outside the project, in English. It must cover: what the
package reproduces and which figure and numbers in the paper it corresponds to;
the software required and the exact versions; how to run it in one command; what
each data file contains, column by column; the source surveys, their years, and
how to obtain them; the statement that only derived aggregates are redistributed;
the classification rule behind the preventive / ambiguous / curative split and a
pointer to the classification table; and the honest caveat the paper itself
carries — that the ambiguous block is reported rather than allocated, that
assigning it wholly one way or the other brackets the preventive share between
roughly 2 and 46 per cent, and that the 2024 rubros do not record prescription
status, so composition is not comparable across waves.

That last caveat is not optional. Shipping the figure without it invites exactly
the cross-wave comparison the build documentation forbids.

---

## 9. What must not happen

- No raw microdata in the package, at any size.
- No file containing household or individual records.
- No recomputation of any published number. No re-estimation. No re-weighting.
- No network access in any shipped script.
- No modification of `Draft-August-v2.tex`, `motivation_section.tex`, or anything
  under `output/` or `draft/`.
- No invented data. If a cell needed for the figure cannot be located in the build
  output, **report it as missing** — do not reconstruct it from the figure, from
  the PDF, or from the paper's prose.
- No language port without approval.

---

## 10. Reporting

Phase 1: report the five discovery items and stop.

Phase 2, after approval: report the package tree; the manifest; the verification
results from §5 in full, including the figure comparison; the run time; the
environment lockfile contents; and every deviation from this specification with
its reason.

If any part of the build cannot be made reproducible offline, say so plainly and
describe what is missing. A package that honestly documents one gap is far more
useful than one that appears complete and fails on a reviewer's machine.
