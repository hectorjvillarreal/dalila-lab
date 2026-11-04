---
type: briefing
to: Debb
from: Claude (for Héctor)
date: 2026-11-03
subject: "Layer A portability assessment delivered: filing, confidentiality, data contract between layers, and five rulings on infrastructure"
report: FISCUS/capa_A_evaluacion/report/LAYER_A_PORTABILITY_ASSESSMENT.md
instruction: FISCUS/RC_simulador/20261103_FISCUS_buildinstr_layerA-python-portability_v1.md
related: [FISCUS/capa_A_evaluacion/scripts/README.md, FISCUS/capa_A_evaluacion/report/data_inputs.csv, FISCUS/capa_A_evaluacion/report/outputs.csv, GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa/projection_national.py, _crossrefs/corpus/demographics/README.md]
commit_at_send: 7635b33
---

# Debb — Layer A assessed; what the workspace must now hold

**Why you're getting this.** Cath's instruction asked for an opinion on porting the CIEP Fiscal
Simulator (Stata, 23k lines) to Python. The opinion is in the report (§1–§9); Héctor then extended it
to how Layer A fits with Dalila's NTA, the BID2 OLG and the DFD demographic engine (§10), and to
whether FISCUS needs simplified models (§11). The infrastructure, filing and knowledge-base
consequences are yours. Five rulings at the end.

**Verdict in one line.** Moderate-to-hard; port the scenario tail first as `run(parameters)` over
frozen CIEP artefacts (7–12 person-weeks), re-implement the micro pipeline later from a specification
and as an extension of Dalila's own NTA (14–24). Complete models as arbiters, cheap evaluations of the
same models as the LLM's playground, a typed interface between them.

## Where things are

| Item | Location | Git |
|---|---|---|
| Report, CSVs, call graph | `FISCUS/capa_A_evaluacion/report/` | committed (bada5bc … 7635b33), **not pushed** |
| Counting scripts (reproducible) | `FISCUS/capa_A_evaluacion/scripts/` | committed |
| Cath's instruction | `FISCUS/RC_simulador/…buildinstr…v1.md` | committed |
| CIEP source, read-only extraction | `FISCUS/capa_A_evaluacion/source/` | **ignored** (`.gitignore`) |
| CIEP zip and a second extracted copy | `FISCUS/RC_simulador/` | **ignored** |

## Confidentiality and the public repo

The FISCUS rule is "nothing leaves the machine". The CIEP repository itself is public on GitHub, but
the instruction treats the zip as confidential and the assessment describes the code at file:line
resolution. `dalila-lab` is public (your 11-02 finding). I committed locally and did not push; two
`.gitignore` files keep the source out. **Ruling needed (1):** does the assessment folder stay on this
branch of the public repo unpushed, move to a private FISCUS repo, or get a `FISCUS/` ignore rule at
the root? Today the branch cannot be pushed without leaking the report.

## Artefacts FISCUS will depend on and does not own

- From CIEP, per release tag: `master/perfiles2027.dta`, `master/2024/*.dta`, `master/2024/cuadratura.do`,
  `users/ricardo/bootstraps/250/*RECprom.dta`, `users/ricardo/cache/`. Not in the GitHub Release
  sidecar (which holds outputs only). Without them nothing is verifiable on Dalila (no Stata here).
- The 27 raw assets (ENIGH zips with CIEP-built `clave_iva.dta` and a census extract, CONAPO zip,
  frozen SCN series, LIF/PEF spreadsheets) are on the Release, SHA-pinned in `05_scripts/manifest.json`.
- The golden masters that do ship: `05_scripts/fixtures/output-default.txt` (47 keys), 10 Sankey JSON
  (1e-9 rule), NTA fixtures, three state folders. **Ruling needed (2):** where do CIEP artefacts live
  in Dalila when they arrive (size: hundreds of MB; candidates `datos/raw/` which is already ignored,
  or a FISCUS-specific ignored tree), and how do we pin them (their `manifest.json` SHA discipline is
  good; I suggest adopting the same `manifest.json` + `sello.txt` pattern for every FISCUS run).

## Knowledge-base gaps found along the way

1. **The Dalila NTA has no code in the repo.** `Missions/Funded/NTA_Inequality/` holds `paper_final.tex`,
   `resumen_ejecutivo.tex`, `presentacion.tex` and two instructions; the R code and the annex tables
   (`tables/tab_lambda.tex`, `tab_scale_map`, `tab_supuestos`, `tab_limitaciones`, `tab_muestra`) that
   the paper `\input`s are absent, so the paper does not compile from the repo. §10.6 compares paper
   against CIEP code; it cannot compare code against code. **Ruling needed (3):** who holds the R code
   (JP?), and does it enter Dalila under the mission folder with a README and SHA of inputs.
2. **The demographic engine is a "communication product".** `projection_national.py` (DFD, 2026-10-24)
   is the producer Héctor wants for all three layers (§10.8), but its README says it does not feed the
   corpus and it publishes aggregates only. It needs a matrix exporter (scenario × sex × single age ×
   year), decisions on the 90+ open group and the 2050 horizon, and promotion through the
   `dfd-demographics-monitor` `_pending/` → Anne workflow with a build instruction. **Ruling needed
   (4):** is that promotion filed as a corpus entry (tier `data_source`?) or as a DFD output with its
   own protocol? PROTO-RAG-001 does not obviously cover a reproducible engine.
3. **Build-instruction provenance.** Cath's instruction lives in `FISCUS/RC_simulador/`, not in
   `_crossrefs/_build_instructions/`, and the report cites it by that path. The archive README says every
   build instruction is retained there. **Ruling needed (5):** copy or move it to the archive (my
   default: copy, keep the FISCUS path canonical as the team README does for briefings), and whether
   the four extensions Héctor requested in conversation (§10.6–§11) need a v1.1 of the instruction or an
   addendum file, since they were never written as instructions.

## The data contract (§10.4) — the part you will have to police

File-based, no in-process calls (Python ↔ R ↔ Julia): `profiles_<year>.parquet` (item × sex × single
age, with `producer` ∈ {ciep, dalila_nta} and `convention`), `effective_rates_<year>.json` (with
`base_concept`, `pension_split`), `benefit_schedules_<year>.parquet`, `fiscal_state_<year>.json`,
`population.parquet` (scenario × sex × age × year, from the DFD engine), `macro_paths.parquet` (two
producers: CGPE/Layer A defaults 2026–2032, OLG steady states as long-run anchors), `scenario.json`
(the ≈150 parameters of `parameter_surface.csv` grouped: legal table by year, scenario levels,
calibration with provenance, run metadata), `results.json`. One `manifest.json` per run with SHA-256
of every input and output. Units fixed once: pesos of `aniovp`, % of GDP, single ages with the open
group declared, sex 1/2 as ENIGH, CIEP's item catalogue.

## Operational notes for whoever builds phase 1

- The CIEP web run is the template: `calculaStata.php` validates 142 numeric keys, substitutes
  `{{key}}` into `Web.Stata.do`, runs `stata-mp -b`, parses a 47-key log. The Python `run()` should keep
  that key set as its regression contract (`gate-numeros.sh` logic: byte-identical `output.txt`,
  1e-9 on Sankey links).
- Non-reproducible pieces to freeze, not emulate: the 250-replica bootstrap means (`*RECprom`), the
  three probits with ranking cut-offs, the `perfilpc` fixed point (copy its stopping rule), MP-thread
  summation order, and the float-vs-double default on the VPS (not determinable from source).
- Runtime budget for the LLM loop (§11.1): Layer A tail seconds; OLG 12 min per steady state threaded
  on Dalila's 16 cores, so OLG exploration goes through a precomputed library plus emulator, with the
  full solve as arbiter. Zellij for anything over five minutes, as usual.
