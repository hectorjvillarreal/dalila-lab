---
type: build_instruction
build_type: delivery_and_corrections
status: queued
project_scope: [DFD, BDH]
date_added: 2026-09-23
added_by: Anne
endorsed_by: Anne
executor: Claude Code (Dalila)
governing_instructions:
  - _crossrefs/protocols/PROTO-RAG-001.md
  - _crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md (v1.5)
authorizes: "2026-09-24_EIC-rebased-scenarios_Anne-record.md (execution note) and Anne's response of 2026-09-23"
title: "Regenerate the Anne delivery bundle after corrections; date hygiene on Anne records; §3.3 taper range and watch-item wording; BID2 manuscript attribution fix and provenance audit; PROTO-RAG-001 candidate"
---

# Build instruction — Anne delivery bundle, corrections, BID2 attribution fix

Six sequential steps. Steps 1–3 are demographics-corpus hygiene; step 4 is the BID2
manuscript fix (cross-project, BDH/BID2 tree); step 5 the audit; step 6 the bundle.
**Order matters: the bundle is built last, from the corrected tree.** Standing constraints
apply throughout (§Not to do). Each step has a done-when test; report against it.

Date convention for this instruction: use the system clock at execution and write
`YYYY-MM-DD` literally; do not infer dates from record titles.

---

## Step 1 — Date hygiene on Anne records

Three Anne-authored files carry a date that postdates their own execution note (09-24
vs execution 09-23):

- `_pending/2026-09-24_EIC-rebased-scenarios_Anne-record.md`
- `_pending/2026-09-24_argentina-renaper-tfr_source-discrepancy.md` (if committed)
- any inbox lines referencing either

**Action:** rename both files to the execution date `2026-09-23_…`; correct the `date:` /
`**Date:**` fields to match; update every path reference (inbox, cross-references, the
execution note's own header line, the watch item opened from §3.3). Record the rename in
the corrected record's execution note as one line: "renamed 09-24 → 09-23, date-hygiene,
per this instruction".

**Done when:** `git grep -n "2026-09-24_"` returns no hits in `_crossrefs/`; both records'
dates equal the execution note's date.

## Step 2 — §3.3 taper range and watch-item wording

**2a. Taper target as a range, not a point.** In the "Queued for v1.6" block of
`DFD_TFR_forecast_instructions.md` (v1.5 trailer) and in `mex_scenarios_eic2025.md`,
the Central migration taper target reads as the 2015–20 net pace. Rewrite as:
*"taper to the 2015–20 net pace, bounded 107–161 k/yr (CPV 2020 ampliado: 802,807 gross
emigrants Mar 2015–Mar 2020 ≈ 161 k/yr; national return share pending the ampliado
tabulado); carry the range until the point is sourced."* Source line: INEGI comunicado
378/21. Do not substitute the CDMX 32.5% return share for the national figure.

**2b. Watch-item wording.** In
`watch_items/2026-09-24_emigration-sex-ratio-marriage-market.md` (renamed per Step 1),
add after the opening statement: *"The 2015–20 outflow was already ≈67% male (537,149 of
802,807); the 2020–25 outflow at 70.4% male and ≈60% higher gross volume is an
intensification of an existing skew, not a new phenomenon. Read the marriage-market
effect as a level that steepened, not as a regime that began in 2020."*

**Done when:** both edits present verbatim; instructions version remains v1.5 (trailer
only); graphs not re-run.

## Step 3 — Record the Benzell correction is closed

Confirm the 2026-09-23 record §3.1 mechanism sentence is struck and replaced by the rule
("burden direction is not a valid proxy for population-revision direction; read the
vintage tables"), marked with the corrected record's name. If already done per the
execution note, no action; state "verified".

**Done when:** `git grep -n "heavier payroll burden"` in `_pending/` returns only the
struck line (or nothing).

## Step 4 — BID2 manuscript: WPP 2024 attribution fix (cross-project; BID2 tree)

**Finding of record:** the claim "peak ~2042 at 152 M, 150.6 M by 2050", attributed to
WPP 2024, originates in `Missions/Funded/BID2/draft_june/CC_instrucciones_Draft-June_v2.md`
(commit a5b3e24), asserted with no table reference, and appears verbatim in every
Draft-June `.tex`. No UN medium series matches it. `demographics_2050.jl` header already
corrected 2026-09-23. **The manuscript is not yet corrected.**

**4a. Pull the series.** Retrieve the WPP 2024 medium-variant total population series for
Mexico, 2024–2100, from the UN WPP 2024 download (Standard Projections, Total Population,
Medium). Record: file name, table/sheet, download date, the 2050 value, the peak year and
value. Do not use the 2026-09-23 inbox figures (148.9 M at 2050; peak ≈149.9 M ~2058) as
the citation — re-pull and cite; use them only to check the pull.

**4b. Correct every `.tex`.** In each Draft-June `.tex` under `Missions/Funded/BID2/`,
replace the sentence with the pulled values and an explicit citation *(United Nations,
World Population Prospects 2024, medium variant, [table/sheet], accessed [date])*. If the
sentence's role in the paragraph is narrative framing that no longer needs a number, delete
the number and keep the framing. Do not paraphrase around the old figure.

**4c. Build-instruction hygiene.** Append to `CC_instrucciones_Draft-June_v2.md` (do not
edit the original text): a dated note stating the figure was unsourced, the corrected
values, and a pointer to this instruction. Provenance is retained, not erased.

**4d. Notify.** One line each to Beth (BDH lead) and Fina (publication strategy) in their
inbox/brief files: attribution corrected; audit (Step 5) running; do not circulate the
Draft-June `.tex` externally until Step 5 closes.

**Done when:** `git grep -n "152" Missions/Funded/BID2/draft_june/*.tex` and
`git grep -n "2042"` return no population-related hits; each `.tex` cites the pulled
table; the notification lines exist.

## Step 5 — Provenance audit of BID2 numerical claims

**Scope:** every numerical claim in the Draft-June `.tex` files that entered via a build
instruction (`CC_instrucciones_*`) rather than via a script output or a cited table.

**Method:** for each `.tex`, list every number that is not (a) generated by a script in the
repo with a traceable output file, or (b) accompanied by a citation to a table/series.
For each listed number, locate its first appearance in the build-instruction history
(`git log -S"<number>" -- Missions/Funded/BID2/`). Classify: *sourced* (table reference
found upstream), *derivable* (script exists; add the output reference), *unsourced*
(no reference anywhere).

**Output:** `Missions/Funded/BID2/draft_june/_provenance_audit_2026-09.md` — one table:
number | file | first appearance | classification | action. **Unsourced items are
corrected or removed before external circulation; none are left "narrative only".**

**Done when:** the audit file exists; every row has a classification; Beth and Fina are
pointed to it; count of *unsourced* rows reported back to Anne and Héctor.

## Step 6 — Regenerate and deliver the Anne bundle

Build **after** Steps 1–5 so the bundle reflects the corrected tree. Concatenate, in this
order, with a one-line `=== FILE: <path> ===` separator before each:

1. `_crossrefs/corpus/demographics/2026-08-13_fernandez-villaverde-norrick_terra-incognita.md`
   (reconstructed cornerstone; `endorsed_by:` blank)
2. `GrandPlan/DFD/aging_macro_nber_2609/2026-09-17_global-transition-demographics-ai.md`
3. `…/2026-09-17_dividend-to-drag-kotschy-bloom.md`
4. `…/2026-09-17_costs-of-building-walls.md`
5. `…/2026-09-17_aging-realignment-world-trade.md`
6. `…/2026-09-17_baby-busts-growth-booms.md`
7. `…/2026-09-17_endogenous-technical-change-demographic-transition.md`
8. `…/2026-09-17_demographic-cliff-higher-education.md`
9. `…/2026-09-17_ghost-town-geography-depopulation-aging.md`
10. `…/2026-09-17_spatial-consequences-depopulation.md`
11. the batch synthesis (as listed in the session summary)
12. `_pending/2026-09-17_tar-candidates.md`

Write to a working path outside the corpus (e.g. `~/anne_delivery_YYYY-MM-DD.md`);
**do not commit** (would duplicate corpus text). Report file size and a line count per
section. Héctor uploads it to the Demographics chat.

**Done when:** the file exists with twelve `=== FILE:` separators; size reported; nothing
under `_crossrefs/` or `GrandPlan/` changed by this step.

---

## PROTO-RAG-001 candidate — logged, not executed

Flag to the Architecture workspace (Debb), with Step 4 as the concrete failure case:

> **Candidate rule:** a build instruction may not assert a statistic (a level, a rate, a
> date, a projection value) without a series/table reference or a script-output path on
> the same line. An unsourced number in a build instruction is a blocking defect at
> execution, not a narrative convenience.

Record in the next Architecture inbox line; do not amend PROTO-RAG-001 here.

## Not to do (standing)

- No v1.6 of `DFD_TFR_forecast_instructions.md` — trailer edits only.
- Graphs (`mex_scenarios_eic2025.py`) not re-run.
- No endorsed artifact amended (Q2/Q3 replicates, `scenario_anchors.md`).
- No `endorsed_by:` set on the reconstructed cornerstone or any NBER note.
- The 65+ reconciliation (Q4 gate) is not attempted in this instruction; if the CONAPO
  server or datos.gob.mx mirror is reachable during Step 4a, download the conciliación
  file and record its path — do not run the reconciliation.

## Report back

One message: per-step done-when result; Step 5 unsourced count; bundle size and path;
any step blocked and why. Inbox lines for Anne (Steps 1–3, 6) and for Beth/Fina (Steps
4–5) as separate entries.

---

*Filing note (Claude Code, 2026-09-23, under `2026-09-23_demographics_commit-endorsements_nota-v0.2.md`
Step 1):* this is the copy executed on 2026-09-23, uncommitted until now. The inbox showed it both as
executed and as absent from the tree. Both were true: it was executed from the working tree and never
committed. Committed as found, with only this note appended.
