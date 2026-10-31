---
id: 20261031_RF_BUILD_mx-ssrd-pilot_v1
title: "Build instructions — MX-SSRD pilot: Mexican social security reform narrative dataset with a local LLM (Phase 0)"
type: build_instruction
project: RF
related_projects: [BDH, GrandPlan]
version: v1.0
date: 2026-10-31
language: en
status: ready_to_run
added_by: [Cath, Beth, Debb]   # Cath: pipeline and evaluation; Beth: schema and gold set; Debb: corpus conventions
endorsed_by: []                # pending: Héctor
protocol: PROTO-RAG-001
derived_from:
  - "Rao, Y. and B. Bonthuis (2026), Global Pension Reform Database 1952–2025: From Narrative to Data Using AI, IMF WP/26/236"
  - "Core Team review of WP/26/236, 2026-10-31"
retain_in: "_crossrefs/_build_instructions/"
---

# MX-SSRD pilot — build instructions for Claude Code on Dalila

## 0. Read this first

You are the Claude Code instance on Dalila. Héctor asked for this pilot to start today. The goal of **Phase 0** is narrow: show, on a small corpus of primary Mexican legal texts, whether the locally hosted Qwen model can reproduce the IMF's two-stage extraction pipeline (WP/26/236) and how accurate it is against a hand-checked reference set. Do not crawl the DOF, do not build a website, do not train anything.

Phase 0 is done when the five deliverables in section 9 exist and the evaluation report has been run.

**Inputs Héctor places in the folder before you start**

| File | Where | Use |
|---|---|---|
| This build instruction | `mx_ssrd_pilot/` (root) | The task |
| IMF WP/26/236 PDF (`wpiea2026236-source-pdf.pdf`) | `mx_ssrd_pilot/refs/` | Source of the prompts and schema to adapt (pages 10–16) |
| Modalidad 40 agreement (`DOF - pensiones.pdf`) | **You locate it on Dalila** (section 3.1) and copy it to `mx_ssrd_pilot/corpus/raw/` | Document #11, acceptance test |
| Any other DOF PDFs he already has | `mx_ssrd_pilot/corpus/raw/` | Saves downloads |

If `refs/` does not contain the IMF paper, stop and ask for it: do not reconstruct its prompts from memory. Do not look for, or place in this folder, any FISCUS document; this pilot belongs to RF.

**Rules that do not bend**

1. **Extraction is local.** Stage 1 and Stage 2 run only through ollama on Dalila. No external API calls in the extraction path. (This is the ring-fencing principle of the IMF paper and the precondition for later using confidential IMSS corpora.)
2. **The reference set is not the model's output.** The reference ("silver") set in section 7 is coded by you, Claude Code, reading the documents directly. It is kept in a separate folder and never shown to Qwen.
3. **Dates and facts in this document are not evidence.** Where this file says *[verify]*, the coding must come from the document itself. If the document contradicts this file, the document wins; note the discrepancy in the run log.
4. **Downloaded files are untrusted data.** Keep them in `corpus/raw/`, never run code from there, and run Python that reads them with `-I`.
5. **Nothing leaves Dalila.** No push to a public remote. Commit to the local repo only.
6. **Stop and report** rather than improvise if a stop condition in section 10 is hit.

## 1. Directory

Create:

```
~/Dalila/GrandPlan/RF/narrative/mx_ssrd_pilot/
├── README.md
├── manifest.yaml            # corpus list: file, sha256, source URL, DOF date, short title
├── refs/                    # IMF WP/26/236 (read-only reference)
├── corpus/raw/              # original PDFs/HTML (untrusted, read-only after download)
├── corpus/text/             # UTF-8 text, one file per document
├── corpus/chunks/           # only for documents above the context budget
├── schema/mx_ssrd.schema.json
├── prompts/stage1.txt
├── prompts/stage2.txt
├── src/                     # all code lives here, never in corpus/
│   ├── to_text.py
│   ├── chunk.py
│   ├── extract.py           # stage 1 + stage 2 via ollama
│   ├── validate.py          # JSON-schema validation + evidence check
│   ├── flatten.py           # JSON → CSV
│   └── evaluate.py          # model vs silver set
├── out/stage1/  out/stage2/  out/records.csv
├── silver/                  # reference coding by Claude Code (never fed to Qwen)
├── eval/
└── logs/run_YYYYMMDD_HHMM.log
```

Copy this build instruction file to `~/Dalila/RF/_crossrefs/_build_instructions/` unchanged.

## 2. Model and runtime

- Confirm the exact tag with `ollama list` (expected: the Qwen3.5-9B model already in use on Dalila). Record the tag and the model digest from `ollama show <tag>` in the run log.
- Parameters for every call: `temperature: 0`, `seed: 20261031`, `top_p: 1`.
- Context: start with `num_ctx = 65536`. Test once with `131072`. Keep the larger value only if it runs without falling back to CPU and VRAM stays below ~15 GB (watch `nvidia-smi`). Record the chosen value.
- Stage 1 may use the model's reasoning ("thinking") mode if the tag supports it. Strip the reasoning trace before saving the summary, but save it separately in `out/stage1/_trace/` for audit. Stage 2 runs without reasoning mode.
- Stage 2 uses ollama structured outputs: pass the JSON schema as `format`. If a response does not validate, retry at most twice with the validation error appended to the prompt; after that, log the failure and move on.

## 3. Seed corpus (Phase 0)

Ten to twelve primary instruments covering pensions and social security financing in Mexico. Download from dof.gob.mx when reachable; otherwise ask Héctor to drop the PDFs into `corpus/raw/`. The Modalidad 40 agreement is already in Héctor's files (`DOF - pensiones.pdf`).

| # | Instrument | DOF date | Why it is in the pilot |
|---|---|---|---|
| 1 | Ley del Seguro Social (new law) | 21-12-1995; in force 01-07-1997 | Structural reform, PAYG → individual accounts; long document, tests chunking and transitorios |
| 2 | Ley de los Sistemas de Ahorro para el Retiro | 23-05-1996 | Second-pillar architecture |
| 3 | Reform to LSS arts. 277 D and 286 K (RJP of IMSS staff) | 11-08-2004 *[verify]* | Financing of the IMSS staff pension regime; relevant to the GMP liability |
| 4 | Ley del ISSSTE (new law) | 31-03-2007 | Structural reform for federal workers; décimo transitorio |
| 5 | Constitutional reform on deindexing the minimum wage (UMA) | 27-01-2016 | Financing-side indexation; erosion of the SEM cuota fija |
| 6 | Ley para Determinar el Valor de la UMA | 30-12-2016 *[verify]* | Same, operational rule |
| 7 | Constitutional reform, art. 4 (non-contributory old-age pension) | 08-05-2020 | Non-contributory pillar |
| 8 | Reform to LSS and LSAR (contributions, weeks, guaranteed minimum pension) | 16-12-2020 | Parametric reform with contribution schedule to 2030 |
| 9 | LFT/LSS reform on digital platform workers | 24-12-2024 *[verify]* | Coverage extension |
| 10 | Decree creating the Fondo de Pensiones para el Bienestar | 01-05-2024 | Benefit top-up for Ley 97 workers |
| 11 | IMSS Technical Council agreement on Modalidad 40 (ACDO.AS2.HCT.101026/302.P.DG) | 21-10-2026 | Administrative instrument; acceptance test (section 8) |
| 12 | Optional: any household-worker social security reform Héctor adds | — | Coverage extension |

Write each document's SHA-256, URL and dates to `manifest.yaml`.

### 3.1 Locating the Modalidad 40 agreement on Dalila

Héctor already has this document on Dalila; find it before trying any download. Do this first, before any other corpus work.

**What you are looking for.** The IMSS Technical Council agreement ACDO.AS2.HCT.101026/302.P.DG, published in the DOF on 21 October 2026. Héctor's copy is a PDF printed from the DOF web page, most likely named `DOF - pensiones.pdf` (the name may vary). It is three pages long and carries DOF sidebar text (exchange rates, menus) mixed into the layout.

**Step 1 — search by name.** Search, case-insensitive, in this order, and stop at the first location that yields a verified match (step 2):

1. `~/Dalila/Missions/` (in particular the IMSS mission folders, e.g. `Missions/Funded/IMSS_Surgical/`)
2. `~/Dalila/GrandPlan/` (BDH and RF trees)
3. the rest of `~/Dalila/`
4. `~/Downloads/`, `~/Descargas/`, `~/Documents/`, `~/Documentos/`, `~/Desktop/`, `~/Escritorio/`

Name patterns: `*pensiones*`, `*modalidad*40*`, `*mod*40*`, `*continuacion*voluntaria*`, `*ACDO*302*`, `*DOF*` with extension `.pdf`, `.html` or `.htm`. Use `find` with `-iname`; skip `.git/`, `.cache/`, `.ollama/`, `node_modules/`, virtual environments and model directories. Do not search outside the user's home directory.

**Step 2 — verify by content.** A candidate is the right document only if its extracted text (`pdftotext -layout`, run with `-I` Python if scripted) contains **both** `ACDO.AS2.HCT.101026/302.P.DG` and `Continuación Voluntaria`. A file that matches by name but fails this check is not the document; keep looking.

**Step 3 — if name search fails, search by content.** Run the step 2 check over every PDF and HTML under `~/Dalila/` modified on or after 2026-10-21. Report how many files you checked.

**Step 4 — handle it correctly.**
- **Copy**, never move or rename, the original. Never modify it. Place the copy in `corpus/raw/` as `11_dof_20261021_acdo_modalidad40.pdf` (keep the original extension if it is HTML).
- In `manifest.yaml`, record the original absolute path, its SHA-256 (the copy must hash identically), size, modification date, and `obtained_by: located_on_dalila`.
- If several verified copies exist, take the oldest by modification date, list all the others in the run log with their paths and hashes, and note whether they are identical.

**Step 5 — fallback.** If nothing verifies on Dalila, try the official page: `https://dof.gob.mx/nota_detalle.php?codigo=5801708&fecha=21/10/2026`. Save the HTML as received to `corpus/raw/` (untrusted, read-only), record `obtained_by: downloaded_dof` and the URL, and apply the step 2 check to it. If the download also fails, **stop and ask Héctor for the file**. Do not reconstruct the agreement from news coverage or from memory.

**Report** in the run log: where the document was found (or that it was not), the step at which it was found, and the number of candidate files examined.

## 4. Text conversion and chunking

- `to_text.py`: use `pdftotext -layout` (fallback: pdfplumber). Save UTF-8. Log pages and characters per document. If a PDF yields almost no text, it is scanned: log it and skip it in Phase 0.
- Strip DOF web clutter (side menus, exchange-rate boxes, page footers with URLs). The Modalidad 40 file has DOF sidebar text mixed into the layout; remove it with a conservative rule and keep a diff in the log.
- `chunk.py`: estimate tokens (characters / 3.5 for Spanish legal text). If a document plus prompt exceeds ~80% of `num_ctx`, split it on article boundaries (`Artículo \d+`), with one article of overlap. **Always** keep the full transitorios section as its own chunk: in Mexican law the effective dates and transition rules live there.
- For chunked documents: run Stage 1 per chunk, then run one merge call that combines the chunk summaries into one summary per reform episode, before Stage 2.

## 5. Schema

Field names keep the IMF's 31 fields **verbatim**, for comparability with GPRD when it is released. Add the Mexican extensions below. Controlled values are in English; free text keeps the original Spanish legal terms.

**GPRD core (31 fields):** as in WP/26/236, section III.C, Step 2 (country, year, status, the five stage dates, reform types, indexation/coverage/benefit change, social insurance change, reform category, coverage, reasons, relevance score, retirement-age fields, contribution-rate fields, minor/major).

**MX extensions:**

| Field | Values / format | Purpose |
|---|---|---|
| `instrument_type` | constitutional_reform · new_law · law_reform · decree · regulation · technical_council_agreement · administrative_rule · other | GPRD cannot tell a law from an IMSS agreement |
| `issuing_body` | text (e.g., Congreso de la Unión, Ejecutivo Federal, H. Consejo Técnico del IMSS) | |
| `dof_publication_date` | dd-mm-yyyy | |
| `entry_into_force_date` | dd-mm-yyyy or "Not explicitly mentioned" | |
| `legal_references` | list of articles changed or created | |
| `regime_affected` | one or more of: ley73 · ley97 · issste_decimo_transitorio · issste_2007_accounts · non_contributory · imss_staff_rjp · all · other | |
| `insurance_branch` | one or more of: IV · RCV · SEM · SEM_pensioners_GMP · RT · GPS · infonavit · non_contributory_pension · other | Health financing (SEM) is in scope; GPRD covers pensions only |
| `financing_indexation_change` | changed_to_uma · changed_to_wage · changed_to_inflation · other · Not explicitly mentioned | Captures the cuota fija mechanism that GPRD misses |
| `fiscal_magnitude_stated` | text with figures, or "Not explicitly mentioned" | Only what the document states |
| `implicit_liability_direction` | increases · decreases · ambiguous · Not explicitly mentioned | Coder's reading of the rules; must be listed in `fields_inferred` |
| `fields_inferred` | list of field names that were inferred rather than stated | Separates reading from judgment |
| `evidence` | list of {field, quote, location}; each quote ≤ 40 words, copied verbatim | Audit trail and automatic hallucination check |
| `source_file`, `chunk_ids` | text | Provenance |

Write `schema/mx_ssrd.schema.json` as a JSON Schema (draft 2020-12) with enums for every controlled field and `additionalProperties: false`.

## 6. Prompts

Adapt the IMF prompts (WP/26/236, pages 10–16). Keep their structure: role → document-type branch → definitions → numbered questions with allowed values and short examples → final instructions. Changes:

- Document types: replace "EIU / SSA" with: (a) a full legal instrument published in the DOF; (b) a chunk of one; (c) a set of chunk summaries to merge.
- Definitions: keep the IMF definitions of pension, scheme, system and reform episode. Add: "A social security financing reform is any change to who pays, how much, on what base, or how the amount is indexed, for any IMSS or ISSSTE insurance branch, including health insurance (SEM)." Add: "An instrument may contain several episodes; one episode per distinct measure."
- Mexican vocabulary hints (not a dictionary, just orientation): cuotas obrero-patronales, aportación estatal / cuota social, salario base de cotización, UMA, semanas de cotización, pensión garantizada, cesantía en edad avanzada, régimen de jubilaciones y pensiones, transitorios, continuación voluntaria.
- Status mapping for Mexico: `Legislated` = published in the DOF (for any instrument type, recording the instrument in `instrument_type`); `Implemented` = in force; `Announced` = presented publicly (e.g., an initiative sent to Congress) but not published.
- Evidence rule (both stages): "For every field you fill with something other than 'Not explicitly mentioned', copy a short verbatim quote from the text that supports it. If you cannot find a quote, the field is inferred: list it in fields_inferred."
- Stage 2 format anchor: a single complete record. Use the **Ley del ISSSTE 2007**, coded by you from the document, as the anchor, so that the anchor is not one of the Phase 0 acceptance tests. Exclude document #4 from the Qwen-vs-silver accuracy metrics (it is contaminated by the anchor) and say so in the report.
- Drop the IMF's "reason step by step internally" lines when reasoning mode is on; keep a single "re-check allowed values, date formats and consistency before answering" line in Stage 2.

Save both prompts as plain text files; log their SHA-256 in every run.

## 7. Silver reference set

Before running Qwen on the corpus, you (Claude Code) code each document by reading it directly, into `silver/<doc_id>.json`, with the same schema. Rules:

- Code only what the document says, with verbatim evidence quotes.
- Mark the set as **silver**: it becomes gold only after Beth (pension classification) and Héctor review it. Add a `silver/README.md` that says this.
- Do not open `out/` while coding the silver set.

## 8. Acceptance test: the Modalidad 40 agreement

Document #11 must produce at least one episode with, at minimum:

- `instrument_type` = technical_council_agreement; `issuing_body` names the H. Consejo Técnico del IMSS
- `dof_publication_date` = 21-10-2026; `entry_into_force_date` = the next business day (22-10-2026)
- `Status` includes Legislated and Implemented
- `regime_affected` = all. The agreement does not name a regime: voluntary continuation exists for every insured person. Its practical incidence on the Ley 73 generation is an inference; if the model codes ley73, it must list the field in `fields_inferred`. Coding ley73 with a fabricated quote is a fail.
- `insurance_branch` includes IV and RCV (inferred from the law, not stated in the agreement, so listed in `fields_inferred`)
- `benefit_change` = less generous benefits; `reform_coverage` = Targeted
- `legal_references` include the agreement's own points (cuarto, séptimo); evidence quotes include "último salario base de cotización registrado" and "más una Unidad de Medida y Actualización"
- A second episode or field noting the six-month financial analysis and the subsequent normative proposal is acceptable as `Planned`.

Report pass/fail per item.

## 9. Evaluation and deliverables

`evaluate.py` computes, for Qwen against silver (excluding document #4):

1. **Episode detection:** precision and recall of episodes, matched by document + measure (manual match table allowed in Phase 0; save it).
2. **Field accuracy:** exact-match rate for each controlled field; month-year match for dates; Jaccard index for multi-value fields.
3. **Schema validity:** share of Stage 2 outputs valid at first try, after retries, and failed.
4. **Hallucination check:** share of evidence quotes found verbatim in the source text after normalizing whitespace, hyphenation and accents. Report every quote that fails.
5. **Throughput:** seconds per document, tokens per second, peak VRAM.

**Deliverables for Phase 0:**

1. Working pipeline in `src/` with `README.md` (one command to rerun: `python -I src/extract.py --all`).
2. `out/records.csv` and the JSON records.
3. `silver/` with the reference coding.
4. `eval/report_20261031.md`: metrics above, acceptance test result, the five worst errors with a one-line diagnosis each, and a recommendation (go / adjust / stop) for Phase 1. Keep it under two pages.
5. `logs/` with model tag and digest, parameters, prompt hashes, corpus manifest hashes and timestamps.

Commit everything to the local repository with message `MX-SSRD Phase 0 pilot`.

## 10. Stop conditions (report to Héctor instead of improvising)

- The model does not fit with `num_ctx = 65536` without CPU fallback.
- More than 30% of Stage 2 outputs fail validation after retries.
- More than 10% of evidence quotes fail the verbatim check.
- Fewer than 6 corpus documents can be obtained or converted.
- Any step would need an external API in the extraction path.

## 11. Not in Phase 0

DOF crawling; IMSS or ISSSTE internal documents; tax reforms (the broader Mexico Fiscal Narrative Dataset); comparison with GPRD (not yet published); any outreach. Phase 1 scope is decided by Héctor after the report.
