---
type: build_instruction
tier: assessment
project_scope: [FISCUS]
title: "Layer A (CIEP Fiscal Simulator, Stata) — portability assessment for a Python implementation"
date_added: 2026-11-03
added_by: Cath
endorsed_by:
status: ready for Claude Code
confidentiality: strict — FISCUS standing rule; nothing leaves the machine
---

# Instruction for Claude Code
# Layer A portability assessment: CIEP Fiscal Simulator (Stata) → Python

## 0. Read this first: what this task is and is not

You are receiving the complete Stata source of the **CIEP Fiscal Simulator**. Within
FISCUS (an integrated fiscal policy laboratory for Mexico) this is **Layer A**.

**Your task is to give an informed, candid OPINION on how easily, and how safely, this
code could be re-implemented in Python.** You are **not** being asked to translate it.

Hard rules:

1. **Do not translate the code.** Short illustrative snippets (≤ 20 lines) to show a specific
   hazard are fine. A partial port is not.
2. **Read-only on the source.** Never modify, reformat, or "clean" any original file.
3. **Do not execute Stata code.** Stata is not assumed to be installed, and you must not
   try to install it or emulate it.
4. **No network use for this task.** Don't upload, paste or send any part of the code or
   data to any external service, website or API. Installing standard Python packages from
   PyPI to *read* files (e.g. `pandas`, `pyreadstat`) is allowed. This code is confidential.
5. **Observed vs. inferred.** Every claim in your report is tagged **[observed]** (you saw it
   in a file, with path and line numbers) or **[inferred]** (your reading, with the reasoning).
   If something can't be determined from the code, write **"not determinable from source"**.
   Do not guess.
6. **Cite locations.** Use `path/to/file.do:LINE` (or a line range) for every substantive
   claim about what the code does.

---

## 1. Setup

1. Ask Héctor for the path to the zip if it is not given here: `<RUTA_AL_ZIP>`.
2. Create a fresh, empty working directory, e.g. `FISCUS/capa_A_evaluacion/`, with:
   - `source/` — extract the zip here, then make it read-only (`chmod -R a-w source/`).
   - `scripts/` — any helper scripts you write (grep counters, parsers). Keep them
     **outside** `source/`, and pass paths as arguments.
   - `report/` — your outputs.
3. Write `report/manifest.csv`: relative path, size, SHA-256, extension, for every file
   extracted. This fixes exactly which version of the code you assessed.

---

## 2. Inventory (quantitative)

Produce `report/inventory.csv` and a summary table in the report:

- File counts and total size by type: `.do`, `.ado`, `.mata`, `.dta`, `.xlsx/.xls`, `.csv`,
  `.log`, `.smcl`, `.sthlp`, graphs, and anything else (including any non-Stata code such as
  JS, Python, R or HTML).
- Lines of code per `.do`/`.ado`/`.mata` file: total, non-blank, non-comment.
- **Stata version** declared (`version` statements) and any version-specific features.
- **Entry point(s):** the master do-file(s). Reconstruct the **execution order** and **call
  graph** from `do`, `run`, `include`, `quietly do`, and program calls. Deliver it as a
  Mermaid diagram in `report/call_graph.md`.
- **User-written / SSC dependencies:** every command not in base Stata (look for `ssc
  install`, `net install`, `.ado` files shipped in the zip, and commands that are not
  official Stata). For each one, give its purpose and say whether a mature Python
  equivalent exists.
- **Data inputs:** every file the code reads (`use`, `import excel`, `import delimited`,
  `insheet`, `infile`, `merge using`, `append using`). For each: path as written, format,
  likely source (ENIGH, CONAPO, SHCP Estadísticas Oportunas, Cuenta Pública, PEF/PPEF, INEGI
  national accounts, other), year(s), and which do-file reads it. For `.dta` files that are
  present, you may read **metadata only** (variable names, labels, number of observations)
  with `pandas.read_stata(..., iterator=True)` or `pyreadstat`. Don't copy microdata into the
  report.
- **Outputs:** everything the code writes (`save`, `export`, `putexcel`, `outsheet`,
  `graph export`, `file write`, `log`), with destination and apparent purpose.
- **Hard-coded paths:** every `cd`, absolute path, and path `global`.

---

## 3. Reconstruct the model

Describe the pipeline stage by stage, mapping each stage to its files. The structure we
expect is below. Confirm it, correct it, or replace it with what the code actually does:

1. Data ingestion and harmonization (household microdata, macro aggregates).
2. Construction of age (and sex?) profiles of taxes paid and transfers/spending received.
3. Scaling of microdata profiles to macro / public-account totals ("cuadre" with official
   aggregates).
4. Demographic projection input (population by age and sex, and its source).
5. Macro projection (GDP growth, real interest rate, inflation, exchange rate).
6. Revenue and expenditure projection by item.
7. Debt dynamics.
8. Intertemporal closure (generational accounting acting as a residual).

Then answer these **six questions explicitly**, each with file:line evidence or "not
determinable from source":

- **Q1. Closure rule.** How is the intertemporal government budget constraint closed? Which
  variable absorbs the gap? What are the discount rate, the projection horizon, and the
  terminal condition? How exactly is the generational-accounting residual computed?
- **Q2. Debt arithmetic.** Which decomposition is used for the evolution of the debt ratio?
  Specifically: is it a four-variable decomposition (growth, real interest rate, inflation,
  exchange rate, with foreign-currency debt treated separately), or a textbook
  primary-balance / (r − g) rule? Which debt concept is used (e.g. SHRFSP / SHRFSPF)?
- **Q3. Age profiles.** How are taxes and transfers allocated to individuals by age? Which
  survey variables, which allocation rules for each tax (ISR, IVA, IEPS, social security
  contributions, oil revenue, other) and each spending category (education, health,
  pensions, transfers, other)? Is the method compatible with National Transfer Accounts
  (NTA) conventions? Note any departures.
- **Q4. Incidence.** For each tax, who is assumed to bear it? Is there any shifting, or does
  statutory incidence stand in for economic incidence? Are there behavioural responses or
  elasticities anywhere?
- **Q5. Macro block.** Are growth, interest rates, inflation and the exchange rate exogenous
  parameters, or does the code tie any of them to fiscal variables?
- **Q6. The public web simulator.** Does the code show how the public online simulator
  relates to this Stata code? For example: does the web tool run the model live, or does it
  use tables or coefficients that Stata pre-computes? If there is front-end code in the zip,
  describe the interface between the two.

---

## 4. Parameter surface (the most important deliverable)

In FISCUS a language model will interact **only** with Layer A, by setting parameters and
reading results. Layer A's exposed parameters are therefore the model's entire action space.

Produce `report/parameter_surface.csv` and a summary table with one row per parameter a user
or analyst could change. Columns:

`name | where defined (file:line) | mechanism (global / local / scalar / matrix / Excel cell / hard-coded literal) | default value | units | plausible range if stated | which stages use it | user-facing in the web tool? (yes / no / unknown)`

Also report on:

- **Separation of parameters and computation:** are parameters set in one place, or scattered
  through the code?
- **Is a run a function?** Could one complete simulation be expressed as
  `results = run(parameters)` without side effects? Name the obstacles: globals, files written
  and re-read mid-pipeline, `preserve/restore` chains, dependence on sort order.
- **Runtime proxy:** with no execution, estimate relative computational weight from the data
  sizes and the loop structure (e.g. "per-household loops over N years").

---

## 5. Translation hazard map

Use counting scripts (in `scripts/`) to give the number of occurrences of each construct, plus
example locations. Classify each as **easy / moderate / hard** to port faithfully, with a
one-line reason.

Constructs to check, at minimum:

- **Data manipulation:** `gen`/`replace`, `egen` (by function: `total`, `rowtotal`, `mean`,
  `group`, `tag`, `cut`, …), `collapse`, `reshape`, `merge` (1:1 / m:1 / 1:m / m:m, plus
  `assert(match)` and other `_merge` handling), `append`, `expand`, `fillin`, `xtile`/`pctile`.
- **Sort-dependent logic:** `by …: gen x = x[_n-1]`, `_n`, `_N`, `sort` vs `sort, stable`,
  running sums (`sum()` inside `gen`).
- **Missing-value semantics:** comparisons such as `if x > c`, where Stata treats missing as
  larger than any number (a classic silent-error source when ported). Also `rowtotal`
  treating missing as zero, and `collapse (sum)` of all-missing groups returning 0.
- **Numeric precision:** variables created without `double` (Stata's default is 4-byte
  float), `float()`, `round()`, `floor()`, `int()`. Flag any place where float precision
  could change aggregates at the reported number of decimals.
- **Survey design:** `[pw=]`, `[fw=]`, `[aw=]`, `[iw=]`, `svyset`, `svy:` (ENIGH design
  variables), and how weights enter aggregation.
- **Macro programming:** nested local/global expansion, variable names built from strings,
  `foreach`/`forvalues`/`while`, `tempvar`/`tempfile`/`tempname`, `levelsof`, extended macro
  functions (`:word`, `:list`, …), `ds`, `unab`.
- **Programs:** `program define`, `syntax`, `args`, `return`/`ereturn`, `.ado` files.
- **Estimation and statistics:** `reg`, `logit`/`probit`, `predict`, `ipolate`, `nl`, `ml`,
  any optimizer. Note Stata defaults that a Python library would not reproduce by default.
- **Mata and matrices:** any Mata code, `matrix` operations, `st_*` functions.
- **Randomness:** `set seed`, `runiform`, `rnormal`, `bsample`. Note that bit-for-bit
  replication across Stata and Python RNGs is not possible.
- **Excel coupling:** `putexcel`, and formatting or formulas written to Excel. Note whether
  any computation lives in Excel rather than in Stata.
- **Labels and encodings:** value labels used in logic (not just display), and string
  encoding (Spanish accents, `unicode` commands).

---

## 6. Hard-coding audit

List the literal numbers that encode substantive information: tax rates, GDP figures,
deflators, budget amounts typed in from official documents, base years, and similar. For each,
say whether it looks like a parameter that should be exposed, a data value that should come
from an input file, or a genuine constant. Flag hard-coded years that would break when the
base year moves forward.

---

## 7. Verification feasibility

A port is only as good as our ability to show that it reproduces the original. Assess:

- What reference outputs exist in the zip (logs, saved `.dta`, Excel results, graphs) that
  could serve as a **golden master**.
- Which stage boundaries could be checkpointed (intermediate datasets) for stage-by-stage
  numerical comparison.
- Realistic tolerances per stage, given float/double issues and survey weighting.
- Whether verification needs a **licensed Stata installation** to regenerate reference
  outputs. If so, say what has to be run.

---

## 8. Your opinion

This is the section Héctor asked for. Be candid. If the honest answer is "this should not be
ported line by line", say so and explain why.

1. **Verdict:** easy / moderate / hard / not advisable as posed, with a short justification.
2. **Effort estimate:** a range in person-weeks for one experienced Python developer working
   with a domain expert. State the assumptions behind the range. Separate the effort for
   (a) the port itself, (b) verification, and (c) refactoring into a callable
   `run(parameters)` interface.
3. **Strategy comparison.** Evaluate at least these options, with pros, cons and risks:
   - (a) Faithful transliteration, stage by stage, verified against Stata checkpoints.
   - (b) Re-implementation from an extracted specification (document the model first, then
     write clean Python against that spec, using Stata outputs only as tests).
   - (c) Keep Stata and wrap it (e.g. `pystata`). Comment on the licensing and
     maintainability implications for a self-contained machine delivered to a government
     ministry.
   - (d) Any hybrid you consider better.
4. **Python vs. R.** The record notes that a port to R had been contemplated. Elsewhere in the
   laboratory, the NTA layer is written in R. Comment briefly on whether the Python choice
   changes anything important (libraries for survey weights, interoperability with the R
   layer, team skills as far as the code reveals them). This is a side note, not the main
   question.
5. **Top five risks**, ranked, each with a mitigation.
6. **Questions for the original author (Ricardo Cantú):** the things only he can answer. Put
   first the ones that block the assessment.

---

## 9. Deliverables

In `report/`:

- `LAYER_A_PORTABILITY_ASSESSMENT.md` — the main report, sections in this order:
  1. Executive verdict (≤ 1 page)
  2. Inventory summary
  3. Pipeline reconstruction + answers to Q1–Q6
  4. Parameter surface summary
  5. Translation hazard map
  6. Hard-coding audit
  7. Verification feasibility
  8. Opinion: strategy, effort, risks
  9. Questions for Ricardo Cantú
- `manifest.csv`, `inventory.csv`, `parameter_surface.csv`, `call_graph.md`
- `scripts/` — the helper scripts you used, so the counts can be reproduced.

When finished, report back with: the executive verdict, the effort range, the three biggest
risks, and the blocking questions for Ricardo. Nothing else needs to go in the summary.
