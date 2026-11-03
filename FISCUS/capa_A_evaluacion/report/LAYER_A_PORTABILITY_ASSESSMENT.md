---
type: assessment_report
tier: assessment
project_scope: [FISCUS]
title: "Layer A — CIEP Fiscal Simulator (Stata): portability assessment for a Python implementation"
date: 2026-11-03
prepared_by: Claude Code (Debb/Cath lane), on the instruction 20261103_FISCUS_buildinstr_layerA-python-portability_v1
build_instruction: ../../RC_simulador/20261103_FISCUS_buildinstr_layerA-python-portability_v1.md
source_assessed: SimuladorCIEP-master.zip (GitHub rcantuc/SimuladorCIEP, manifest version v8.15.3, CHANGELOG dated 2026-11-03, data_updated 2026-10-31, baseline v8.15.0)
confidentiality: strict — FISCUS standing rule; nothing leaves the machine
tags: "[observed] = seen in a file at the cited lines; [inferred] = my reading, with the reasoning; NDS = not determinable from source"
---

# Layer A portability assessment: CIEP Fiscal Simulator (Stata) → Python

Companion files in this folder: `manifest.csv` (2,542 files with SHA-256), `inventory.csv`, `loc.csv`,
`call_graph.md`, `callgraph_edges.csv`, `parameter_surface.csv`, `data_inputs.csv`, `outputs.csv`,
`hazard_counts.csv`, `hardcoding_audit.csv`, `io_grep.txt`; scripts in `../scripts/`.

---

## 1. Executive verdict

**Verdict: moderate-to-hard, and not advisable as a line-by-line transliteration of the whole repository. Advisable as a two-phase hybrid that starts from the web run.** [inferred]

What the code is. [observed] A 23k-line Stata system (18k lines in the computational core, the rest
graphs, side products and scripts) whose single entry point `SIM.do` (i) downloads and freezes
official data (INEGI BIE/CSI, SHCP open data, Cuenta Pública/PEF spreadsheets, CONAPO), (ii)
harmonises the ENIGH 2024 household survey person by person to the household sector of the national
accounts (`Expenditure.do`, `Households.do`), (iii) allocates every tax and every spending item to
persons and builds age×sex profiles with a Mata engine (`PerfilesSim.do`, `Simulador.ado`,
`GastoPC.ado`), and (iv) projects revenue, spending and debt year by year to 2032 (`FiscalGap.ado`,
`SHRFSP.ado`, `PIBDeflactor.ado`). The public website does **not** use pre-computed tables: PHP
substitutes the form into a template (`Web.Stata.do`) and runs a licensed Stata/MP 17 for every
click, ~17–20 s, reading artefacts that the batch run left behind (`master/perfiles2027.dta`,
`users/ricardo/bootstraps/250/*RECprom.dta`, `users/ricardo/cache/`).

Three facts drive the verdict.

1. **The action space FISCUS cares about is small and already isolated.** [observed] The whole
   parameter surface a user can move (`parameter_surface.csv`: ~150 named inputs, 142 of them web
   placeholders) enters only the scenario tail: `TasasEfectivas §7`, `GastoPC §3–8`, `Simulador`
   (B=1), `FiscalGap`, `SankeySF`, `output.do`, plus the optional `ISR_Mod`/`IVA_Mod`. That tail is
   ~5,000 code lines, mostly arithmetic on annual series and weighted sums over one 308,598-row
   micro file. Porting it against frozen Stata-produced inputs gives a `run(parameters)` that
   reproduces `output.txt` for the entire web action space.
2. **The heavy part is a calibration pipeline, not a model.** [observed/inferred] `Households.do`
   (3,006 lines) and `Expenditure.do` (1,354) encode the Ley del ISR article by article, three probits
   with ranking cut-offs, a fixed-point intra-household allocation in Mata, and nine signed
   "cuadratura" switches anchored to specific cells of INEGI's institutional-sector tables. It is
   re-run only when the ENIGH vintage or the national-accounts anchors change (not per scenario).
   A faithful transliteration is possible but expensive to verify; a re-implementation from a
   specification is the right form, and that specification half exists (`02_governance/CUAD-0.md`,
   module headers, `03_help/*.md`).
3. **Bit-identity is not a meaningful target, even for the authors.** [observed] The runbook records
   that Stata 17 and StataNow 19.5 already differ in ~52 of ~5,000 published values
   (`xtile`/`probit`/Mata) and that `collapse (sum)` under Stata/MP depends on the number of threads
   (`runbook-deploys-ciep.md:529-530`). The project's own gate is byte-identity of `output.txt` at
   3 decimals of % GDP plus 1e-9 relative on Sankey links (`05_scripts/gate-numeros.sh`). A Python
   port should be verified at the precision of the published contract (3 decimals of % GDP, integer
   pesos per capita), not at the bit.

Two structural findings for FISCUS that are independent of the language question:

- **There is no intertemporal closure.** [observed] The present-value balance and the generational
  accounts were retired on 2026-09-12 (`FiscalGap.ado:412-416, 1101-1102, 1122-1125`); the engine
  projects revenue and spending annually to anioPE+5 and lets **debt absorb** the gap
  (`FiscalGap.ado:864-893`). `CuentasGeneracionales.ado` exists but is commented out (`SIM.do:524`).
- **Macro is exogenous and the revenue projection is not tied to GDP growth.** [observed] After the
  anchor year, each revenue item grows with its own historical per-capita trend (capped at ±5 %)
  times the growth of its demographic base (`FiscalGap.ado:154-198`); the GDP-growth inputs
  (`CRECPIB*`) change the denominator and the peso value of the 2027 anchor, nothing else.

**Effort (one experienced Python developer plus a domain expert, see §8.2):** phase 1 (scenario tail as
`run(parameters)`, verified against `output.txt` and the Sankey JSONs): **6–10 person-weeks**. Phase 2
(micro pipeline from an extracted specification, verified against the `.dta` checkpoints): **14–24
person-weeks**, of which 4–6 are specification writing. Licensed Stata is required at least once to
regenerate the golden masters (§7).

---

## 2. Inventory summary

Source assessed [observed]: `SimuladorCIEP-master.zip`, 47.06 MB; extracted 2,542 files, 76.9 MB
(`manifest.csv`). Top of `02_governance/CHANGELOG.md` is `[v8.15.3] — 2026-11-03`; `05_scripts/manifest.json`
says `version v8.15.3`, `data_updated 2026-10-31`, `baseline v8.15.0`, `enigh_vintage 2024`.
`README.md` says "Versión: 13 de mayo de 2026" (stale header) [observed].

### 2.1 Files by type [observed, `inventory.csv`]

| Type | Files | Bytes | Comment |
|---|---:|---:|---|
| `.ado` | 36 | 785,736 | all at repository root |
| `.do` | 30 | 605,355 | `SIM.do`, `profile.do`, templates, `01_modulos/`, `05_scripts/` |
| `.sthlp` | 11 | 103,394 | Stata help files |
| `.scheme` | 7 | 37,863 | graph schemes |
| `.mata` | 0 | — | Mata lives inside `.ado` files |
| `.dta` / `.xlsx` / `.csv` (data) | 0 / 0 / 0 | — | **no data in the zip**: data is gitignored and travels as GitHub-Release assets listed in `manifest.json` (27 assets) |
| `.log` / `.smcl` | 0 | — | no logs |
| `.json` | 54 | 3.7 MB | `manifest.json` + 44 fixtures (golden masters, §7) + site JSON |
| `.php` | 53 | 565,789 | web back end (`04_1_simuladorfiscal.ciep.mx/`): 10,420 lines |
| `.js` | 227 | 16.2 MB | 7,145 lines of site JS outside vendored plugins (`stataCalcula.js` 2,071); the rest is Bootstrap/Highcharts etc. |
| `.sh` | 29 | 455,514 | 7,940 lines of publication/gate scripts |
| `.py` | 6 | 100,046 | 1,700 lines (`generar-entidades.py`, `perfilar-web.py`, …) |
| `.md` | 43 | 1.35 MB | governance and help (CHANGELOG 3,910 lines; `arquitectura.md` 811; `CUAD-0.md` 364) |
| images, fonts, css | ~1,900 | ~41 MB | site assets |

### 2.2 Lines of Stata code [observed, `loc.csv`]

66 `.do`/`.ado` files: 34,083 total lines, 29,601 non-blank, **23,148 code lines**. The 32 files on the
`SIM.do`/`Web.Stata.do` path hold 18,010 code lines. Largest: `SCN.ado` 2,165, `Households.do` 1,780,
`NTA.do` 1,333, `GastoPC.ado` 1,300, `PEF.ado` 1,136, `Expenditure.do` 1,071, `Simulador.ado` 1,069,
`FiscalGap.ado` 961, `PIBDeflactor.ado` 895, `SHRFSP.ado` 814, `DatosAbiertos.ado` 775. A large share
is presentation: 1,129 `display` statements and 54 graph commands with multi-line options [observed,
`hazard_counts.csv`]; I estimate [inferred] that 25–30 % of the code lines have no computational
content.

### 2.3 Stata version [observed]

- No `version` statement in `SIM.do`, `Web.Stata.do` or the `01_modulos/*.do` files. `.ado` files declare
  13.1 (legacy profile programs), 14 (`escalar`, `scalarjson`, `SIMentidad`, `TasasEfectivasMicro`), 16
  (`ensure_asset`, `sim_changelog`), 17 (`AccesoBIE`, `perfilpc`, `Precache*`, `PEF._PEF_cachekey`)
  (`io_grep.txt`, "VERSION statements").
- Version-specific features: `python:` blocks (Stata ≥ 16) in six files; `frame`-free; `ustrregexm`
  (≥ 14); `saveold … version(13)` for `master/*.dta`.
- Production web: Stata/MP 17 on the VPS (`config.php:314`, perf report l.62). Development: StataNow
  19.5 SE with `set processors 1` (runbook §9, l.86, l.530). The two differ in ~52 of ~5,000 values
  (`runbook-deploys-ciep.md:529`).

### 2.4 Entry points and execution order [observed]

See `call_graph.md` (Mermaid). `SIM.do` sections: §0 parameters → §1 `Poblacion` → §2 `PIBDeflactor`,
`SCN` → §3 `Expenditure.do`, `Households.do`, `NTA.do`, `PerfilesSim.do` → §4 `LIF`, revenue scalars and
matrices, `TasasEfectivas` → §5 `PEF`, spending scalars, `Precache`, `GastoPC` → §6 debt matrices,
`SHRFSP` → §7 life-cycle merge + `Simulador` → §8 `FiscalGap`, `SankeySF.do` ×5 → `output.do`. Measured
wall time ≈ 32–35 min single-threaded (`runbook-deploys-ciep.md:852`; `perf/perfil-web-2026-10-18.md:39`).
`Web.Stata.do` runs only §3.1 (`LIF`), the scalars/matrices, optional `ISR_Mod`/`IVA_Mod`,
`TasasEfectivas`, `GastoPC, cache`, `Simulador` (B=1), `FiscalGap`, `SankeySF` ×5, `cuadratura.do`,
`output.do`: 17–20 s (`perf/README.md`).

### 2.5 User-written / SSC dependencies [observed]

| Dependency | Where | Purpose | Python equivalent |
|---|---|---|---|
| `labutil` (`labmask`) | `LIF.ado:627-631`, `PEF.ado:809` (`net install` on the fly) | value labels from a variable | trivial (pandas categorical) |
| `grc1leg2` | `FiscalGap.ado:344-347` (installed; the call that used it is commented, l.348) | combined graph legend | n/a (graphics) |
| Python packages `requests`, `beautifulsoup4` | `AccesoBIE.ado:299-305`, `AccesoINPCEntidad.ado`, `ensure_asset.ado:54-60` | INEGI API / HTML export scraping; SHA-256 asset check | already Python |
| Everything else | — | base Stata (`xtile`, `probit`, `tabstat`, `collapse`, `reshape`, `bsample`, `putexcel`, `import excel`, `lpoly`) | pandas/numpy/statsmodels; see §5 |

The repository ships its own 36 `.ado` programs; none is from SSC.

### 2.6 Data inputs and outputs

Full tables: `data_inputs.csv` (28 rows) and `outputs.csv` (16 rows). In one paragraph [observed]: the
raw inputs are the ENIGH tables for 2014–2024 (INEGI, repackaged with a CIEP-built `clave_iva.dta` and a
Censos Económicos extract inside each zip), CONAPO pry23 population by single age, sex and state
(served by DGIS), 525 BIE national-accounts series frozen in `scn-congelado-2024.zip`, seven INEGI CSI
institutional-sector spreadsheets read by cell range, the SHCP Estadísticas Oportunas open-data CSVs
(≥ 60 concept codes), `LIFs.xlsx` (CIEP compilation of the Ley de Ingresos), Cuenta Pública / PEF /
PPEF spreadsheets 2013–2027, `ISRInformesTrimestrales.xlsx`, `CuotasISSSTE.xlsx`. All raw assets are
pinned by SHA-256 in `manifest.json` and fetched by `ensure_asset.ado` from the GitHub Release. The
pipeline writes ~40 intermediate `.dta` files under `master/` and `users/<id>/`, JSON for the site,
and the 47-key `users/<id>/output.txt` that the web parses (`calculaStata.php:146-181`).

### 2.7 Hard-coded paths [observed, `io_grep.txt` "PATHS"]

`SIM.do:15` (`global SIMROOT "/Users/ricardo/Library/CloudStorage/Dropbox-CIEP/…"`), `SIM.do:47`
(export path), `Web.Stata.do:20,23` (`/Users/ricardo/…` vs `/SIM/OUT/current/` chosen by username),
`SankeyCFE.do:8`, `SankeyPemex.do:8`, `sysprofile-template.do:27-33`, `config.php:303-314`
(`/SIM/OUT/current/users/`, `/usr/local/stata17/stata-mp`). Everything else is relative to
`${SIMROOT}`; `profile.do:10-17` derives it from the location of `profile.do`.

---

## 3. Pipeline reconstruction and answers to Q1–Q6

### 3.1 Stage map (the expected eight stages, corrected)

| # | Expected stage | What the code does | Files (main lines) |
|---|---|---|---|
| 1 | Ingestion and harmonisation | ENIGH expenditure → 19 SNA categories, 11 IVA regimes, 12 IEPS categories; household spending split among members by an age-sex fixed point; scale factors per category to the SCN household-consumption cells. ENIGH income → LISR concepts, exemptions, social contributions (gross-up of net wages), ISR, formality (3 probits + ranking), Altimir factors to S.14 cells (D.1, B.3n, B.2n, D.4). | `Expenditure.do` (§2–§4, l.142-1153), `perfilpc.ado`, `Households.do` (§1–§12), `SCN.ado` |
| 2 | Age (and sex) profiles | Per-person tax/transfer variables are summed by (sex, single age 0–109); profile = cell mean ÷ per-capita of 40-year-old men; participation = contributors ÷ population. | `Simulador.ado:1459-1481` (Mata), legacy `PERF.ado` |
| 3 | Scaling to macro totals ("cuadre") | Every variable is re-anchored to the LIF/PEF/SCN total of anioPE by `Distribucion` (y_i = x_i·MACRO/Σ w x); population weights rescaled ENIGH→CONAPO of anioPE. | `PerfilesSim.do:178-179, 184-525`, `Distribucion.ado:20-35`, `TasasEfectivas.ado:325-336`, `GastoPC.ado` |
| 4 | Demographic projection input | CONAPO pry23 (1970–2070), national = Σ states; matrices HOM/MUJ age×year feed the projection. | `Poblacion.ado:647-788`, `Simulador.ado:401-411` |
| 5 | Macro projection | Exogenous growth/deflator/inflation 2026–2032; afterwards GDP = output per working-age person × WorkingAge(15–65) × (1+λ)^t; deflator/INPC by geometric mean; FX by CGPE then mean depreciation; effective interest = 5-year mean or user scalar. | `PIBDeflactor.ado:198-237, 295-364`, `FiscalGap.ado:764-807` |
| 6 | Revenue and expenditure projection by item | REC_t = REC_2027 × Π(contribuyentes_t/contribuyentes_{t−1}) × (1+trend)^(t−2027), trend = historical growth − demographic growth, capped ±5. Anchor = scenario scalar × GDP (or LIF/PEF/micro total). | `FiscalGap.ado:154-202, 460-506`; base `*RECprom` from `Simulador.ado:1509-1510` |
| 7 | Debt dynamics | Annual nominal iteration 2028→2032 of cost, balance, RFSP, internal/external SHRFSP with FX effect and a geometric "actualización" factor. | `FiscalGap.ado:734-907` |
| 8 | Intertemporal closure | **None.** PV blocks retired 2026-09-12; generational accounts commented out. Debt is the residual. | `FiscalGap.ado:412-417, 1101-1125, 1166-1234`; `SIM.do:524` |
| + | NTA account | Separate module building a Lee–Mason NTA per person closed on S.14 (identity gate 1e-9); feeds the `/NTA` page only. | `NTA.do` |
| + | Effective tax rates | Macro/macro effective rates per tax (revenue ÷ SCN base) for display and web. | `TasasEfectivas.ado:50-307` |

### Q1. Closure rule

[observed] There is no intertemporal government budget constraint in the running code.

- `FiscalGap` is called with `end(anioPE+5)` = 2032 and `discount(8)` (`SIM.do:528`, `Web.Stata.do:420`);
  the program defaults are `END(int 2100)` and `DIScount(real 5)` (`FiscalGap.ado:8-9`).
- The present-value sums of revenue and spending ("VP/infinito") were removed on 2026-09-12 and the
  PV balance and intergenerational-inequity blocks are gated on a local that is never set
  (`estimacionINF`), so they are skipped (`FiscalGap.ado:412-417, 1101-1102, 1122-1125, 1218-1234`).
- What remains of the discount rate: a present-value population series (`poblacionVP`,
  `FiscalGap.ado:1177`) and a perpetuity population (`poblacionINF`, l.1206) used only in displays, and
  `pibYVP`/`pibINF` in `PIBDeflactor.ado:370, 413-421` (computed, not consumed by the projection).
- Terminal condition: none; the horizon ends at the last year with GDP, SHRFSP and bootstrap series
  (`FiscalGap.ado:736-739, 995-997`) and the last SHRFSP ratio is printed (`PROYSHRFSP2`).
- **The gap is absorbed by debt**: `rfspBalance = −revenue + (spending − deferrals)`, `rfsp = rfspBalance +
  rfspAdecuaciones` (other RFSP components commented out), and SHRFSP accumulates (`FiscalGap.ado:879-892`).
- Generational-accounting residual: `CuentasGeneracionales.ado` computes GA_edad = Σ_t PERFIL×Pop×PC×(1+λ)^t/(1+r)^t
  by cohort in Mata (l.88-115) with `discount(3)` default, but its only call is commented
  (`SIM.do:524`) and it reads an obsolete path layout (`users/$pais/$id/…`, l.51, 66). **Unused.**

[inferred] For FISCUS this means Layer A is an **annual projection engine with a debt residual**, not a
fiscal-gap or GA model in the Auerbach–Kotlikoff sense, despite the program name. Any closure (tax
rule, spending rule, debt target) would have to be added, which is easier in a port than in the
original.

### Q2. Debt arithmetic

[observed] `FiscalGap.ado` §5.6–§5.9 works in nominal pesos on annual series:

- Effective rate: `tasaEfectiva_t = cost_t / SHRFSP_{t−1} × 100`; projected value = arithmetic mean of the
  last five observed years (l.764-769), overridden by `scalar tasaEfectiva` (web `DEUDA0`, l.786-790);
  the 2027 cost may be re-anchored to `gascosto` % GDP (l.777-783).
- Exchange rate: CGPE path to 2032 via `SHRFSP` globals; beyond, last mean annual depreciation in pesos
  (l.799-807). FX effect = external debt in USD × Δe (l.810, 884-885).
- Revaluation: `actualizacion_geo` = geometric rate solving ΔSHRFSP_{2009→last} = Σ FX effects + Σ RFSP
  (l.840-847), applied to both internal and external stocks (l.887-890). This is a residual "other
  flows" factor estimated from history, not an interest term.
- Iteration (l.868-893): cost_t = rate × SHRFSP_{t−1}; spending_t += cost_t; deferrals_t = ratio × spending;
  balance_t = −rev + (spend − deferrals); rfsp_t = balance + adecuaciones; ext_t = ext_{t−1}(1+g_act) +
  FX_t + rfsp_t·share_ext; int_t similarly; SHRFSP_t = ext + int. Ratios to GDP are formed afterwards
  (l.895-901).

So it is **neither** the textbook primary-balance/(r−g) rule **nor** an explicit four-variable
decomposition in the projection. A four-way **descriptive** decomposition (real growth, inflation,
interest, exchange rate, primary balance, residual) exists in `SHRFSP.ado:690-719` for the historical
display only. Debt concept: **SHRFSP** total/internal/external from SHCP open data (`SHRF5000`,
`SHRF5100`, `SHRF5200`; `SHRFSP.ado:803-816`), RFSP flows `RF000000SPFCS…RF000007SPFCS` (l.890-935),
costs `XAC21`, `XOA0155/0156`, FX implied by `XET30/XET40` (l.1049-1102, 1161). Gross debt and
government-only concepts are computed for display (`SHRFSP.ado:158-166`). [inferred] A port can
reproduce this arithmetic exactly; the modelling questions (why the revaluation factor, why other RFSP
components are frozen but excluded) belong to Ricardo (§9).

### Q3. Age profiles

**Construction** [observed, `Simulador.ado:1389-1396, 1450-1481`]: cells (sex, age 0..109, ages >109
collapsed to 109); `recC` = Σ w·y·cond, `forC` = Σ w·cond, `pobC` = Σ w; `perfil = recC/forC/pc` with
`pc` = per-capita of 40-year-old men (or the overall mean if that cell is empty, l.1455-1457);
`pcont = forC/pobC×100` (100 if the cell has no population). Projection
`REC_t = pc × Σ_age (perfil·pcont/100 · Pop_{age,t})` and `contribuyentes_t = Σ pcont/100 · Pop` (l.1509-1510).
No smoothing in production (`lpoly` only draws graphs, l.594-632). The 40-year-old normalisation cancels
in `REC_t` [inferred: perfil×pc = cell mean].

**Allocation rules per item** [observed; relative = the micro variable passed to `Distribucion`]:

| Item | Allocated ∝ | Where |
|---|---|---|
| ISR asalariados | `ISR_asalariados` (LISR tariff on grossed-up wages, formality by probit ranking) | `PerfilesSim.do:218`; `Households.do:1830-1879, 2432-2439` |
| ISR personas físicas | `ISR_PF` | `PerfilesSim.do:224`; `Households.do:2455-2462` |
| Cuotas IMSS | `cuotasTP` (worker + employer) of `formal2==1` | `PerfilesSim.do:230`; `Households.do:1614-1695` |
| ISR personas morales | `ISR_PM` = 30 % × (own-business income + imputed depreciation − exemptions) − employment subsidy | `PerfilesSim.do:250`; `Households.do:2477-2489` |
| Productos, derechos, aprovechamientos (OTROSK) | `ISR_PM` | `PerfilesSim.do:256` |
| IVA | micro IVA from `Expenditure.do` §5 (regime by category; exempt goods pay IVA on the VA share of inputs) | `PerfilesSim.do:273`; `Expenditure.do:1196-1209, 265-268` |
| ISAN | `gas_pc_Vehi` | `Households.do:2855`; `PerfilesSim.do:282` |
| IEPS no petrolero | `gas_pc_BebA` (alcoholic beverages only) | `PerfilesSim.do:288` |
| IEPS petrolero | `gas_pc_Vehi` | `PerfilesSim.do:294` |
| Importaciones | total spending, then re-anchored | `Households.do:2856`; `PerfilesSim.do:300` |
| FMP, Pemex, CFE, IMSS, ISSSTE own revenue | per capita (`relativo(pob)`) | `PerfilesSim.do:319-351` |
| Education | per student by level (enrolment × `nivel` × `edad≤15` for básica) | `GastoPC.ado:127-151, 361-534`; `PerfilesSim.do:366-436` |
| Health | per affiliated person by institution (`inst_*`), incidence weight ∝ household health spending share | `GastoPC.ado:158-232, 727-939` |
| Pensions IMSS/ISSSTE/Pemex/other | per pensioner (`ing_jubila≠0 & formal==k & jubilado`) | `GastoPC.ado:236-255, 1045-1135` |
| Pensión Bienestar (PAM) | all persons ≥65 in `GastoPC` (l.236) vs recipients ≥65 or disabled with `ing_pam≠0` in `PerfilesSim.do:452-460` | two conventions |
| Energy, Otros gastos, Participaciones, debt cost | per capita (every person) | `GastoPC.ado:1235-1308, 1369-1394, 1459-1463` |
| Otras inversiones, Federalizado (profiles) | by state of residence ∝ PEF by state | `PerfilesSim.do:484-497`; `GastoPC.ado:1374, 1414` |
| Cuidados / madres trabajadoras / ingreso básico | potential care population; children <4; universal or age-restricted | `GastoPC.ado:1442-1444, 1551-1553, 1565-1619` |

**Life-cycle net** [observed, `SIM.do:473-488`]: `ImpuestosAportaciones` = ISRPM + ISRAS + ISRPF + CUOTAS +
IVA + IEPSNP + IEPSP + ISAN + IMPORT (FMP and OTROSK excluded, l.479 comment); `Transferencias` =
Pensiones (+PAM) + IngBasico + Educación + Salud + OtrasInversiones (Otros gastos and Energía excluded).

**NTA compatibility** [observed/inferred]: a dedicated `NTA.do` builds a Lee–Mason account per person
(C − YL − ImpProd = τ⁺ − τ⁻ + YA − S, gate 1e-9; `NTA.do:17-20`) anchored to S.14 cells, with public
in-kind consumption by enrolment/affiliation and collective consumption per capita (`NTA.do:40-50`).
That is NTA-conformant in structure. The **fiscal** engine departs from NTA in: (i) ISR PM and OTROSK
are allocated to households with own-business income — the author flags this as incorrect and
schedules a fix for 8.16 (`Households.do:41-43, 2305-2308`); (ii) private consumption is split within
the household by a data-driven fixed point (`perfilpc.ado:1-85`), not by the NTA a-priori equivalence
scale (the scale `alfa` is defined in `Expenditure.do:865-867` and, as far as I can see, never used
afterwards); (iii) profiles are unsmoothed single-year cells; (iv) the normalisation is the 40-year-old
male, not the 30–49 average (immaterial for projections); (v) FMP and SOE revenue are per-capita
lump sums and excluded from the net.

### Q4. Incidence

[observed] Statutory incidence with simple attribution rules and no behavioural response:

- Wage ISR: borne by the employee; net wages are grossed up through the tariff with employment
  subsidy (`Households.do:1830-1874`) and employer and federal contributions are added to the worker's
  gross labour income (`cuotasTPF`, l.1686-1695; `Yl` anchored to D.1 which includes employer
  contributions, l.2245, 2270).
- Consumption taxes (IVA, IEPS, ISAN, import duties): borne fully by the consumer in proportion to
  spending; IVA on exempt goods = rate × input value-added share `prop` (`Expenditure.do:1202-1207`).
  IVA informality is a uniform haircut `IVAT[13]` (`IVA_Mod.do:305`; 23.1 % in `SIM.do:288`, 7.77 % in
  `Expenditure.do:1176`); the `informal` purchase-place flag is built (`Expenditure.do:478`) but not used.
- Corporate ISR: to households with business income (flagged as wrong, see Q3).
- Oil revenue (FMP) and SOE own revenue: per-capita lump sums, outside the life-cycle net.
- Informality/evasion of ISR: three `xi: probit … [pw=factor]` on formality (`Households.do:2384-2421`),
  then persons are ranked by predicted probability and declared formal until the cumulative simulated
  tax reaches the LIF total (`l.2432-2499`): a calibration device, not a behavioural margin.
- Web ISR module multiplies its results by fixed ratios (`ISR_Mod.do:176, 184, 193, 208, 213`:
  `×3.793/3.255`, `×0.241/0.553`, `×4.176/2.781`, `×1.675/1.525`, `×.1492/.098`) that are not documented
  in the source and are absent from the batch path.
- Elasticities: none found (`grep -i elastic` matches only two display labels, `LIF.ado:342`,
  `PEF.ado:408`). No price or labour-supply response anywhere.

### Q5. Macro block

[observed] Fully exogenous: GDP growth, GDP-deflator growth and INPC inflation 2026–2032 are globals
(`SIM.do:107-131`; web `CRECPIB*`/`CRECDEF*`; inflation hard-coded in `Web.Stata.do:75-81`). Beyond the
last exogenous year GDP grows with working-age population (CONAPO, 15–65) at historical productivity
growth λ (`PIBDeflactor.ado:338-364`); the deflator and INPC follow geometric means of their history
(l.213-217, 232-236). Interest and FX as in Q2. There is **no feedback** from fiscal variables to any
macro variable, and — importantly — **no feedback from GDP growth to revenue growth** after the anchor
year (Q1/Q2, `FiscalGap.ado:154-198`): `CRECPIB` moves `pibY` (denominators and the peso value of the
2027 anchors `kPIB/100×pibY`) only.

### Q6. The public web simulator

[observed] `calculaStata.php` reads 142 form keys (`l.12-48`), validates them as numeric (`config.php:347-359`;
security review v8.11a), substitutes `{{key}}` into a copy of `01_modulos/Web.Stata.do` written to
`users/<idSession>/<idSession>.do` (`l.114-132`), runs `stata-mp -b do` synchronously (`l.143-144`,
executable `/usr/local/stata17/stata-mp`, `config.php:314`), then parses `output.txt` with a regex into
JSON (`l.156-180`). Admission control: 3 concurrent Stata processes, 100 runs per IP per 10 minutes
(`config.php:407-412`). The default scenario shown on load comes from Ricardo's batch `output.txt`
(`cargaDefault.php`; perf report l.45-54). Sankeys are served from JSON files written by Stata
(`jsonSankey*.php`). The `/NTA` and `/entidades/<ABREV>` pages are static, generated offline by
`generar-entidades.py` from JSON that Stata wrote; CI (`.github/workflows/gates-sin-stata.yml`) runs
only gates that need no Stata. Governance principle: "Stata produce todos los números… la página no
calcula" (`arquitectura.md:458-466`). **So: the web runs the model live; there are no pre-computed
coefficient tables except the base-scenario artefacts the template reads** (`master/perfiles2027.dta`,
`users/ricardo/bootstraps/250/*RECprom.dta`, `users/ricardo/cache/*`, `master/2024/cuadratura.do`).

---

## 4. Parameter surface summary

Full table: `parameter_surface.csv` (≈150 rows). Grouped [observed]:

| Group | Count | Mechanism | Web-facing | Consumed by |
|---|---:|---|---|---|
| Run control (`aniovp`, `anioPE`, `anioenigh`, `bootstrap`, `seed`, `idbase`, `algebra`, flags) | 15 | `scalar`/`global` in `SIM.do` §0 / `Web.Stata.do` §0 | no | everything |
| Cuadratura switches (CUAD-0) | 10 | globals validated in `Households.do:140-166` | no | micro pipeline (batch only) |
| NTA switches | 9 | globals `nta_*` | no | `NTA.do` |
| Macro paths 2026–2032 (growth, deflator, inflation) | 21 | globals (positional) | 14 yes (`CRECPIB*`, `CRECDEF*`), 7 no | `PIBDeflactor` |
| Revenue levels % GDP | 15 | `escalar pctpib` / `{{INGRESOS*}}` | yes | `TasasEfectivas` §7, `FiscalGap` anchors, `output.do` |
| ISR tariff rates, SE table, DED, PM | 11 + 11 + 4 + 2 | `matrix` cells | yes (ISR module) | `ISR_Mod.do` |
| Contribution rates IMSS/ISSSTE | 21 + 24 | `matrix` cells (two copies, one inconsistent) | yes (ISR module) | `ISR_Mod.do`; `Households.do` (own copy) |
| IVA rate, regimes, informality | 1 + 11 + 1 | `matrix` cells | yes (IVA module) | `IVA_Mod.do`; `Expenditure.do` (own copy) |
| IEPS rates/quotas | 17×2 | `matrix` (three divergent copies) | no | `Expenditure.do` only |
| Spending levels % GDP + basic-income switches | 34 + 3 | `scalar` / `{{…}}` | yes | `GastoPC` → `gastos.dta` → `FiscalGap` HH anchors |
| CGPE debt frame 2026–2032 (SHRFSP, RFSP components, FX, primary balance, cost, revenue, spending) | 7×(3+8+1+1+1+1+1) = 112 cells | `matrix` → 112 globals | no | `SHRFSP` §4; `FiscalGap` (2027 anchor) |
| Effective interest rate | 1 | `scalar tasaEfectiva` | yes (`DEUDA0`) | `FiscalGap` §5.6 |
| Projection options (`end`, `discount`, `desde`, `aniomin`, caps ±5, 5-year windows, 2009, 2013) | ~10 | options and literals in `FiscalGap.ado` | no | `FiscalGap` |
| Year-specific legal constants (UMA/SM, UDIs, exemption multiples, deduction caps, SBC caps, Infonavit 5 %) | ~25 | locals/literals in `Households.do`, `ISR_Mod.do` | no | micro pipeline |
| Calibration anchors (Pemex/ISSFAM splits, FAM shares, cost share of fees, ISR_Mod ratios) | ~10 | literals | no | `GastoPC`, `Households`, `ISR_Mod` |

**Separation of parameters and computation** [observed]: good at the top (all scenario inputs are
declared in `SIM.do` §0–§6 and mirrored one-to-one in `Web.Stata.do`; the `escalar` registry gives every
exported number a type, `escalar.ado:10-33`), poor below: tariffs, contribution matrices, IEPS tables
and the IVA informality rate exist in two or three copies with different values (`parameter_surface.csv`
rows CSS_ISSSTE, IEPST, IVAT[13]); legal constants are typed per ENIGH vintage inside `Households.do`;
calibration ratios are literals inside `ISR_Mod.do` and `GastoPC.ado`.

**Is a run a function?** [observed] Not today. Obstacles, in order of weight:

1. **State on disk between stages**: `ingresos.dta`, `gastos.dta`, `aportaciones.dta`, `LIF.dta`,
   `isr_mod.dta`, `iva_mod.dta` are written and re-read within one run (`TasasEfectivas.ado:340`,
   `GastoPC.ado:1674`, `SIM.do:462-512`, `Web.Stata.do:98,383-411`); `FiscalGap` reads them back (l.98-99).
2. **Globals as the parameter bus**: 1,331 global reads in 56 files; `SHRFSP` discovers the CGPE path by
   probing for globals named `shrfsp<year>` (`SHRFSP.ado:107-138`), `PIBDeflactor` probes `pib<year>`
   (l.295-305); `capture confirm scalar` decides between scenario and observed anchors in `FiscalGap`
   (l.185-191) and `GastoPC` (every section).
3. **`preserve`/`restore` and `tempfile` chains**: 78/79 and 162 occurrences; `FiscalGap` §4–5 loops
   `preserve → collapse → save tempfile → restore → merge` per item (l.151-208, 460-506).
4. **Sort-order and position dependence**: `in 1`/`in -1`/`[_N]` 174 times; running sums after `gsort`
   decide formality (`Households.do:2391-2394, 2432-2439`); `continue, break` loops locate years by
   scanning rows (`PIBDeflactor.ado:97-112`, `Simulador.ado:76-82`).
5. **r()-class side channels**: 960 `r(…)` reads; `LIF`/`PEF` return per-group totals as `r(name)` built
   with `strtoname` from Spanish labels (`FiscalGap.ado:142-145, 445-448`; `PerfilesSim.do:52-104`).
6. The author has already pushed toward functional form where it mattered for speed: `$algebra` replaces
   micro passes by closed-form sums of scalars (`FiscalGap.ado:63-96`, `GastoPC.ado:1691-1728`) and
   `Precache` isolates scenario-invariant work (`Precache.ado:1-39`). [inferred] That is exactly the
   seam a Python `run(parameters)` should follow.

**Runtime proxy** [observed unless noted]:

| Block | Data touched | Loop structure | Measured / inferred weight |
|---|---|---|---|
| `Expenditure.do` | ENIGH spending rows (several million line items) → 308,598 persons × 19+11+12 categories | 42 `perfilpc` fixed points, each 100–600 Mata iterations (`perfilpc.ado:21-24`); 42+ `Simulador` calls with B=250 | part of the ~32 min batch; the v8.4 non-Mata version took ~10 h per ENIGH (`perfilpc.ado:88-91`) |
| `Households.do` | 308,598 persons × ~220 variables; 3 probits | mostly vectorised `gen/replace`; ISR loops 11×11 brackets over the whole file (l.1842-1871, 2332-2343) | minutes [inferred] |
| `PerfilesSim.do` | same micro × 41 variables | 41 `Simulador` runs × 250 bootstrap replicas in Mata (ms each) | minutes [inferred] |
| `PEF`/`LIF`/`SCN` builders | `master/PEF.dta` 3.56 M rows (perf l.17) | `collapse`, `import excel` of 16 workbooks | one-off; `PEF` history collapse ≈ 8 s per web click before Precache (perf l.18) |
| Web tail | `perfiles2027.dta` 308,598 × 152; 41 `REC_*` tables | `tabstat` ×477, `collapse` ×69, `egen total` on 3.56 M rows | 31.5 s before Precache, 17–20 s after (perf README) |
| `FiscalGap` projection proper | ~20 annual rows × 24 items | `forvalues` over years | ≈ 1.7 s (perf l.20) |

[inferred] In Python with pandas/numpy the web tail is sub-second except `Simulador` (groupby over 300k
rows: tens of ms) and the Sankeys; the micro pipeline is minutes; nothing needs a GPU.

---

## 5. Translation hazard map

Counts from `hazard_counts.csv` (regex over code lines of all 66 files; approximate). Classification:
**easy** = direct pandas/numpy idiom; **moderate** = needs care or a helper to match Stata semantics;
**hard** = cannot be made bit-identical or requires reproducing a Stata-specific algorithm.

### 5.1 Data manipulation

| Construct | n | Files | Class | Reason / example |
|---|---:|---:|---|---|
| `gen`/`replace` | 814 / 1,111 | 40 / 34 | easy | vectorised; but 517 `gen` have no type (see 5.4) |
| `egen rowtotal/rsum` | 112 | 13 | moderate | missing treated as 0; all-missing row → 0 (`SIM.do:474-484`) |
| `egen total/sum` (by group) | 63 | 17 | easy | `groupby().transform('sum')` |
| `collapse` (81 with `(sum)`) | 93 | 27 | moderate | `(sum)` of all-missing group = 0 in Stata; `(mean)`, `(max)`, `(last)` after sort (`PIBDeflactor.ado:141-142`) |
| `reshape wide/long` | 53 | 16 | moderate | string `j()` with `strtoname` labels (`Expenditure.do:541, 568`) |
| `merge 1:1 / m:1 / 1:m` | 122 / 30 / 1 | 18 / 11 / 1 | moderate | 134 `nogen` and 0 `assert(match)`: unmatched rows silently kept; 13 use `update replace` (`FiscalGap.ado:99, 207, 213`) whose precedence rules must be replicated |
| `append using` | 30 | 7 | easy | |
| `joinby` | 1 | 1 | moderate | `LIF.ado:669` with `unmatched(both) update` |
| `expand` | 2 | 2 | easy | |
| `xtile/pctile/_pctile` | 12 | 6 | **hard** | weighted deciles with `[pw=factor/tot_integ]` (`Households.do:2799-2802`); Stata's definition (ties and `W_i == P` midpoint rule) is re-implemented in Mata in `Simulador.ado:1312-1334` — use that as the spec |
| `tabstat … save` / `r(StatTotal)` | 239 / 332 | 32 | easy | weighted sums; `tabstat [aw=]` vs `[fw=]` mixed (28 `aw`, 114 `fw`) |
| `preserve/restore`, `tempfile` | 78/79, 162 | 25, 28 | easy | disappears in a functional port |

### 5.2 Sort-dependent logic

| Construct | n | Class | Reason |
|---|---:|---|---|
| `sort`/`gsort` (2 `stable`) | 67 | moderate | Stata `sort` is not stable; ties broken by RNG. Author fixed one case by sorting on a unique key (`Households.do:661-665`) and `gsort -prob … folioviv foliohog numren` (l.2391, 2408, 2424) makes rankings deterministic. Replicate with full-key sorts. |
| `[_n-1]`, `[_N]`, `in 1`/`in -1`/`in k` | 1,466 (subscripts incl. `[`k']` loops) ; 174 positional | moderate | `forvalues k=1/_N` scans to find a year (`PIBDeflactor.ado:97-112`) — replace by lookups |
| `by …:` | 13 | easy | |
| `L.`/`F.`/`D.` after `tsset anio` | 234 | easy | shift on a complete yearly index; gaps matter (`FiscalGap.ado:195-198`) |
| running `sum()` in `gen` | 11 | moderate | cumulative sums after `gsort` decide formality cut-offs (`Households.do:2392, 2438, 2460, 2487`) |
| `continue, break` scans | 15 | easy | |

### 5.3 Missing-value semantics

| Construct | n | Class | Reason |
|---|---:|---|---|
| `if x > c` / `>=` comparisons with variables | 175 | **moderate/hard to audit** | Stata missing = +∞: `g agri = ing_agri/ing_exclusivo > .9` (`Households.do:722`) is true when the ratio is missing; `replace sbc = 25 if sbc > 25 & …` (l.1601) etc. Each must be read individually. |
| explicit `== .`/`!= .`/`< .` | 339 | easy | author is aware; many guards |
| `replace x = 0 if x == .` | 112 | easy | shows the intended convention (missing→0) |
| `rsum` / `collapse (sum)` of missing | 112 / 81 | moderate | see 5.1 |
| `editmissing`/`missing()`/`cond()` | 25 | easy | |

### 5.4 Numeric precision

| Construct | n | Class | Reason |
|---|---:|---|---|
| `gen` without type | 517 | **hard for bit-identity** | Stata default is 4-byte float unless `set type double`. `profile.do:27` sets it `permanently` on researcher machines; whether the VPS batch (`stata-mp -b`, `Web.Stata.do`) inherits it is **NDS**. Many money variables are created untyped (`Households.do:456 g ing_anual`, `GastoPC.ado:1050 g Pensión_AM`). At 3-decimal % GDP outputs this is invisible; at 1e-9 Sankey gates it is not. |
| `gen double` | 243 | easy | |
| `round()`, `floor()` | 73, 20 | moderate | `round(factor*adj,1)` on weights (`PerfilesSim.do:178-179`); `floor(sbc)` (`Households.do:1609`); `round(ISR_AS_Mod, 0.001)` before re-use (`SIM.do:265`) — replicable, must not be skipped |
| `string()`/`%fmt` → number | 307 | moderate | `output.do` formats (`%8.3f`, `%12.0g`, `%20.0g`) define the published precision; `scalar deudageneINI = string(…)` stores strings as scalars (`FiscalGap.ado:1215`) |
| `%21x` hex doubles | `Households.do:2759-2762` | easy | the author already serialises exact doubles |
| `collapse (sum)` thread dependence | runbook l.530 | **hard** | MP vs SE differ at 16 digits |
| `saveold version(13)` | 4 | easy | pyreadstat reads 113–118 |

### 5.5 Survey design

| Construct | n | Class | Reason |
|---|---:|---|---|
| `[fw=factor]` | 114 | easy | integer weights (after `round(factor,1)`) |
| `[aw=factor]` | 28 | easy | sums identical to fw; means identical |
| `[pw=factor]` in probit; `[pw=factor/tot_integ]` in `xtile` | 10 | moderate | pweights change SEs only; `xtile` with non-integer weights needs the exact rule |
| `svyset`/`svy:` | 0 | — | design variables `upm`, `est_dis` used only by the cluster bootstrap (`Simulador.ado:347-388`) |

### 5.6 Macro programming

| Construct | n | Class | Reason |
|---|---:|---|---|
| names built from macros (`` `k'PIB ``, `` ``k'' ``) | 1,575 | **hard to read, easy to port** | the port must enumerate them explicitly (e.g. the 15 revenue items, 9 spending items) |
| `` `=expr' `` inline evaluation | 1,208 | easy | |
| nested macros `` ``x'' `` | 52 | moderate | `PerfilesSim.do:122-127`, `Expenditure.do:909-920` (locals named after SCN scalars) |
| `foreach`/`forvalues`/`while` | 258/162/25 | easy | |
| `levelsof` | 37 | easy | |
| extended macro functions | 139 | easy | `: variable label`, `: word`, `: colnames` |
| `strtoname`/accent stripping | 64 | moderate | names like `Educaci_n`, `Pensi_n_AM`, `r(Ciudad_de_México)` (`Households.do:287`) |
| `global` reads/defines | 1,331 / 189 | moderate | implicit interface; see §4 |
| `gettoken`/`tokenize` | 38 | easy | |

### 5.7 Programs

| Construct | n | Class |
|---|---:|---|
| `program define` | 106 (42 files) | easy to map to functions; 50 `syntax`, 29 `args` |
| `return scalar/local/matrix`, `r()` reads | 106, 960 | moderate (implicit return bus) |
| `capture` (error swallowing) / `capture confirm` / `_rc` | 649 / 234 / 381 | **moderate** — control flow by existence of scalars/files/variables (`GastoPC.ado:341-358` falls back to PEF when a scalar is missing; `Simulador.ado:339-345` branches on `sexo` being string) |
| `exit <code>` | 75 | easy |

### 5.8 Estimation and statistics

| Construct | n | Class | Reason |
|---|---:|---|---|
| `xi: probit … [pw=factor]` + `predict` + `estimates save` | 3 | **hard (bit), moderate (tolerance)** | `Households.do:2384-2421`. statsmodels `Probit` with frequency weights gives the same MLE; defaults differ (Stata: Newton–Raphson, tol 1e-6 on coefficients; `xi:` drops a base category by lowest value). Predicted probabilities feed a ranking cut-off, so 1e-6 differences can flip marginal persons' formality; totals are re-anchored to LIF so the aggregate effect is bounded, the distribution is not identical. |
| `lpoly` | 0 in computation (graphs only) | — | |
| `ci means`, `_pctile` | 14, in `simci` | easy | bootstrap summaries |
| `reg`, `nl`, `ml`, `ipolate` | 0 | — | |

### 5.9 Mata and matrices

| Construct | n | Class | Reason |
|---|---:|---|---|
| Mata inline / blocks / functions | 51 / 5 / 11 | moderate | `simboot_run` (`Simulador.ado:1349-1565`) is clean linear algebra: `panelsum` = groupby sum; matrix products for the projection; easy in numpy. `perfilpc` fixed point (`perfilpc.ado:405+`, 6-significant-digit rounding of cell means, tolerance 1e-6, up to 1000 iterations) is replicable but its stopping rule must be copied exactly. |
| `st_data/st_matrix/st_local` | 73 | easy | |
| Stata `matrix` | 89 | easy | parameter tables and `J(1,1,…)` accumulators |
| `mkmat`/`svmat` | 14 | easy | |

### 5.10 Randomness

| Construct | n | Class | Reason |
|---|---:|---|---|
| `set seed 1111`, `rseed()`, `runiform`, `bsample` | 4, 1, 1, 2 | **hard** | Bootstrap of UPM within strata in Mata (`Simulador.ado:1433-1447`). Not reproducible across RNGs. **Consequence**: the base-scenario projections `*RECprom.dta` are means over B=250 replicas (`PerfilesSim.do:604-622`) and feed `FiscalGap` (`_FGreccol`). A port cannot regenerate them bit-identically; it must either take them as frozen inputs or accept O(1/√250) differences in the base growth paths. The web run itself uses B=1 (deterministic). |

### 5.11 Excel coupling

| Construct | n | Class | Reason |
|---|---:|---|---|
| `import excel … cellrange()` | 25 (21 with cellrange) | moderate | CSI tabulados by fixed cell ranges (`SCN.ado:2177-2688`); CP/PEF workbooks with column homologation (`PEF.ado:719-770`, `1331-1578`) — fragile but pure parsing (openpyxl) |
| `putexcel` | 43 | easy / not in pipeline | only with option `excel` (`GastoPC.ado:610-641`) and `Perfiles.ado`; values only, no formulas → **no computation lives in Excel** [observed] |
| `export excel` | 0 | — | |

### 5.12 Labels and encodings

| Construct | n | Class | Reason |
|---|---:|---|---|
| value labels used in logic (`decode` + string compare, `: label`) | 30 + 40 | moderate | `divSIM`/`divCIEP` are decoded to strings and compared (`FiscalGap.ado:147-150, 449-455`); `label define deciles … 11 "Nac"` |
| string flags `== "1"` | 250 | easy | ENIGH codes are strings (`inst_1 == "1"`, `asis_esc == "1"`) |
| Spanish accents in identifiers/labels | 1,205 | moderate | variable `Pensión_AM`, labels `Educación`, `r(Ciudad_de_México)`; `set charset latin1` (`profile.do:28`) vs UTF-8 files (Stata 14+ is UTF-8): confirm the on-disk `.dta` encodings with `pyreadstat` metadata before trusting string keys |
| `{c o'}` SMCL escapes | 195 | easy (display only) | |
| `destring`/`tostring` | 56 | easy | |

### 5.13 I/O, side effects and the output contract

| Construct | n | Class |
|---|---:|---|
| `save` / `use` | 263 / 187 | moderate (replace by in-memory objects; keep checkpoints optional) |
| `file open/write` (JSON by hand) | 386 | easy (`json.dump`) but formats must match the fixtures byte-for-byte if the gate is reused |
| `log using/on/off` + `filefilter` to build `output.txt` | 47 + 15 | **moderate**: the web contract is a log file post-processed by `filefilter` (`output.do:381-392`: strip `\n>` continuations, spaces, `_`→space, `.,`→`0`); keys with 22 values are split in two by Stata's 255-char linesize (`output.do:198-204`) |
| `python:` blocks, `shell` | 14, 1 | easy (already Python) |
| `escalar` / `Distribucion` | 882 / 98 | easy — two small helpers |

---

## 6. Hard-coding audit

Full list with locations and recommendations: `hardcoding_audit.csv` (≈55 rows). The substantive groups
[observed]:

- **Base-year and horizon literals**: `aniovp`/`anioPE` = 2027, `anioenigh` = 2024, the 2026–2032 vectors
  in `SIM.do`, `Web.Stata.do`, `output.do` and the HTML ids (`output.do:3-5` documents the positional
  contract), `aniomax(2032)`, `aniofinal(2070)`, history start 2013, RFSP base 2009. Moving the base
  year forward touches four files and the DOM in lockstep.
- **Scenario levels typed from official documents**: the 15 revenue and 34 spending `% GDP` defaults
  (`SIM.do:176-193, 339-379`) and the 112-cell CGPE debt frame (`SIM.do:403-428`). These are data, and
  the engine already knows how to derive the first two from LIF/PEF when the scalars are absent
  (`TasasEfectivas.ado:32-45`, `GastoPC.ado:341-358`).
- **Legal parameters as literals, in several copies**: ISR tariff and employment-subsidy tables (2025 in
  `SIM.do`/`Web.Stata.do`; 2017/2018–20/2022+ in `Households.do:342-421`), contribution matrices
  (`SIM.do:241-260` vs `Households.do:1572-1592`, **not identical**: ISSSTE federal cells 391.0/13.9 vs
  13.90/13.90 and a different row split), IEPS tables (three copies with 17, 17 and 10 rows), UMA/SM by
  year (`smdf`: 248.93 for 2024 equals the 2024 general minimum wage, while 96.22 for 2022 equals the
  2022 UMA — the concept is not consistent, NDS which is intended), UDI values, exemption multiples
  from LISR art. 93/74, deduction caps 14,200…24,500, SBC caps 25/10 UMA, Infonavit 5 %, 700,000 UDIs.
- **Calibration constants without provenance**: `602513/1169476` and `110000/181290` (Pemex vs ISSFAM
  splits, marked `TODO(Ricardo)` in `GastoPC.ado:176-180, 240-242`), `FAM_cuidados` .65/.81,
  `0.634768962` (cost share of fees, Censo 2019), `24.30` in the ISSSTE federal quota formula
  (`Households.do:1649-1677`), the five ratio factors in `ISR_Mod.do`, `IVAT[13]` 23.1 vs 7.77, the IVA
  rate 0.16 inside the IEPS computation (`Expenditure.do:1288, 1295`), the `±5` trend cap, the 5-year
  windows, the 2/3–1/3 mixed-income split, the `in -111/-1` tail block (inactive).
- **Environment**: Ricardo's Dropbox path and `/SIM/OUT/current/`, `idbase "ricardo"`, Stata executable
  paths in `config.php`.

[inferred] None of this blocks a port; it dictates the shape of the Python parameter object: a
year-indexed legal table (tariffs, contribution rates, UMA, UDI, caps), a scenario block (levels,
macro paths, debt frame), a calibration block with provenance fields, and run metadata. The duplicated
copies should be unified **before** porting, with Ricardo deciding which copy is canonical (§9).

---

## 7. Verification feasibility

### 7.1 Golden masters present in the zip [observed]

| Artefact | What it pins | Tolerance used by CIEP |
|---|---|---|
| `05_scripts/fixtures/output-default.txt` (51 KB, 509 key lines, 47 distinct keys) | the complete web contract for the default scenario (batch `SIM.do` with `nographs + output`) | byte-identical (`gate-numeros.sh`); values printed at `%8.3f` (% GDP), `%8.0f`/`%12.0f` (pesos, persons), `%10.1f`/`%10.3f` (projections), `%20.0g` (effective rate), `%21x`-derived `CUADRATURA` |
| `fixtures/sankeys-default/SankeySF/sankey-{decil,grupoedad,sexo,rural,escol}.json` and `SankeyNTA/…` (10 files) | micro aggregates by cut (links from→to→value) | 1e-9 relative per link |
| `fixtures/nta-grupoedad.json`, `nta-panel-grupoedad-sexo.json`, `sankey-nta-grupoedad.json`, `nta-identidad.txt` | NTA account by age group and group×sex, identity report | identity gate 1e-9 (`test-nta-identidad.do`) |
| `fixtures/entidades/{NL,Col,Jal}/*.json` (9 each), `entidades.json`, `statajson_entidad-nl.json` | three states' Sankeys, life cycle, effective rates | contract tests |
| `02_governance/scalarlatex-baseline.txt` (239 names) | audited list of scalar names | drift alert only |

No `.dta`, `.log`/`.smcl`, Excel results or graphs ship in the zip [observed]. The GitHub Release for
each version adds `datos-<version>.zip` (306 files: `output.txt`, the 10 Sankeys, `NTA/*` JSON, the 32
state folders) and `manifest-datos.json` (`runbook-deploys-ciep.md:363-392`) — outputs, not microdata.

### 7.2 Checkpointable stage boundaries [observed as files; feasibility inferred]

| Boundary | File(s) | Compare |
|---|---|---|
| Builders → master | `master/Poblacion.dta`, `PIBDeflactor.dta`, `SCN.dta`, `LIF.dta`, `PEF.dta`, `SHRFSP.dta`, `DatosAbiertos.dta`, `Deflactor.dta` | exact for integer/identifier columns; 1e-12 relative for sums; these are pure imports and collapses |
| Expenditure | `master/2024/consumption_categ{,_iva,_ieps}_pc.dta`, `expenditures.dta`, `categ_iva.dta`, `consumption_categ_iva.dta`, `consumption_categ_ieps.dta`, `deducciones.dta` | per-person values; the `perfilpc` fixed point will differ at the 6th significant digit unless the rounding/stopping rule is copied |
| Households | `master/2024/households.dta` (≈220 vars), `cuadratura.do` (exact doubles in hex), `formal_*.ster` | anchored sums exact to 1e-9 by construction (gates l.2766-2780); per-person ISR and formality flags are the sensitive part (probit) |
| PerfilesSim | `master/perfiles2027.dta`, `users/<id>/bootstraps/250/*{PC,PERF,INCI,CICLO,REC,PT}.dta`, `*RECprom.dta` | PERF/PC exact (weighted sums); REC with B>1 not reproducible (RNG) — freeze or use B=1 |
| Web inputs | `users/ricardo/cache/*`, `master/2024/cuadratura.do` | exact |
| Scenario tail | `users/<id>/{ingresos,gastos,aportaciones}.dta`, `output.txt`, 5 Sankey JSON | `output.txt` at printed precision; Sankeys 1e-9 relative is achievable for weighted sums in double if the summation order is controlled |

### 7.3 Realistic tolerances per stage [inferred]

- Annual projection (`FiscalGap`, `PIBDeflactor`, `SHRFSP` arithmetic): 1e-12 relative on doubles;
  identical at printed precision.
- Weighted sums over the micro file (profiles, Sankeys, anchors): 1e-9 relative if both sides use
  doubles and pairwise/compensated summation is avoided on one side only; CIEP's own gate is 1e-9 and
  they report MP/SE differences at the 16th digit.
- Fixed points (`perfilpc`): 1e-6 relative per cell (their stopping rule), amplified into per-person
  values; aggregates by category exact.
- Probit + ranking: expect a handful of persons out of 308,598 to flip formality; ISR totals anchored;
  distribution by decile/age differs in the 4th significant digit [inferred from the author's own
  cross-version note, runbook l.529].
- Bootstrap means (`RECprom`): not reproducible; differences O(0.1 %) in base growth paths [inferred
  from B=250 and typical sampling CVs; no measurement available in the zip].
- Published contract: 3 decimals of % GDP and integer pesos — achievable exactly for the deterministic
  parts once the inputs above are frozen.

### 7.4 Does verification need a licensed Stata? [observed/inferred]

**Yes, at least once, and ideally during the whole port.** The zip contains no intermediate `.dta`;
every checkpoint in 7.2 must be regenerated by running `SIM.do` (≈32–35 min, StataNow 19.5 SE,
`set processors 1`, with the 27 raw assets downloaded by `ensure_asset` from the Release and the INEGI
token for anything that is not frozen). What has to be run: `SIM.do` with `global nographs` and
`global output` (the baseline recipe in `gate-numeros.sh` header and runbook §9), which leaves
`master/`, `users/ricardo/bootstraps/250/`, `users/ricardo/cache/`, `output.txt` and the JSON; then
`test-web-batch.sh` to confirm the web path reproduces the batch (47/47 keys). Without Stata the only
verifiable layer is the scenario tail against the shipped fixtures, **and only if CIEP supplies**
`master/perfiles2027.dta`, `master/2024/*.dta`, `users/ricardo/bootstraps/250/*RECprom.dta`,
`users/ricardo/cache/*` and `master/2024/cuadratura.do` (a few hundred MB) — these are not in the
release sidecar. The ENIGH is public, but `clave_iva.dta` and `censo_eco_municipios.dta` inside the
ENIGH zips are CIEP-built [observed: only in the asset, no builder in the repo].

---

## 8. Opinion: strategy, effort, risks

### 8.1 Verdict

**Moderate-to-hard; not advisable as posed if "posed" means a full faithful transliteration of the
repository.** Advisable, and attractive for FISCUS, as a **two-phase hybrid** (option d below): port the
scenario tail first as a pure function over frozen Stata artefacts, then re-implement the micro
pipeline from a specification. Reasons: the parameter surface is confined to the tail; the tail is
small and deterministic; the micro pipeline is large, calibration-heavy, still moving (CUAD-0 was
signed 2026-10-31, 8.16 is announced to change ISR PM, informality and the IVA/Expenditures anchors,
`CUAD-0.md:156-159`), and its verification needs Stata anyway.

### 8.2 Effort estimate (one experienced Python developer working with a domain expert)

Assumptions [inferred]: developer fluent in pandas/numpy and able to read Stata; domain expert available
~1 day/week; CIEP provides a frozen set of `.dta` artefacts for one release tag (or FISCUS has a Stata
licence to generate them); target precision = the published contract (not bits); no web front end;
Python 3.12, pandas, numpy, pyreadstat, statsmodels.

| Component | Range (person-weeks) | What is included |
|---|---:|---|
| **(a1) Port of the scenario tail** as `run(parameters)` — `TasasEfectivas §7`, `GastoPC §3–8` (algebra form), `Simulador` B=1 (profiles, incidence, life cycle, projection), `FiscalGap`, `SHRFSP` arithmetic, `PIBDeflactor §3–5`, `ISR_Mod`, `IVA_Mod`, `SankeySF` aggregation, `output` contract | 4–6 | ~5,000 Stata lines → ~2,500 Python; parameter schema; readers for the frozen inputs |
| **(b1) Verification of (a1)** against `output-default.txt`, the 10 Sankeys, and 10–20 perturbed scenarios generated with Stata (`perfilar-web.py` already builds scenarios) | 2–4 | needs CIEP/Stata to produce the perturbed `output.txt` files |
| **(c) Interface design** (`run(parameters) → results`, JSON schema, provenance, no disk state) | 1–2 | cheap if designed before (a1); 3–5 if retrofitted onto a transliteration |
| **(a2) Micro pipeline from specification** — `Expenditure.do`, `Households.do`, `PerfilesSim.do`, `perfilpc`, `Simulador` B>1, builders for `master/*` from raw assets | 10–16 | 4–6 of these are writing the specification (CUAD-0 + module headers + 03_help are 60 % of it); Excel/CSI parsers 2–3; LISR/exemptions/CSS 2–3; probits + ranking 1; `perfilpc` 1; `Simulador` bootstrap 1 |
| **(b2) Verification of (a2)** stage by stage against regenerated `.dta` checkpoints | 4–8 | requires Stata runs for each ENIGH vintage used; the probit and fixed-point stages consume most of the time |
| **Total phase 1 (a1+b1+c)** | **7–12** | gives FISCUS a working Layer A for its whole action space |
| **Total phase 2 (a2+b2)** | **14–24** | makes Layer A self-contained from raw public data |

Option (a) full transliteration of everything, verified against Stata checkpoints: **22–34 person-weeks**
plus a permanent coupling to Stata for regeneration; option (c) wrapping Stata: 2–4 person-weeks of
plumbing plus the licence problem below.

### 8.3 Strategy comparison

**(a) Faithful transliteration, stage by stage, verified against Stata checkpoints.**
Pros: lowest intellectual risk; every number has a Stata counterpart; CUAD-0 gates reusable. Cons: carries
over 25–30 % dead/presentation code, three copies of tariff tables, globals-as-interface, disk state, and
Stata-specific idioms that have no reason to exist in Python; verification needs a Stata licence for the
whole duration and every time CIEP changes the method (weekly in October 2026); bit-identity is impossible
(RNG, probit, MP threads) so the team spends time explaining 1e-9 noise. Risk: a port that is faithful to
the artefacts of v8.15.3 and unmaintainable against v8.16.

**(b) Re-implementation from an extracted specification, Stata outputs only as tests.**
Pros: produces the artefact FISCUS lacks most — a written model specification (closure, incidence rules,
anchors, parameter schema) that a language model can be grounded on; clean `run(parameters)`; unifies the
duplicated tables; makes the missing closure addable. Cons: specification writing is real work (CUAD-0
shows it took CIEP a month for one module), and some rules exist only in code (exemption rules in
`Households.do` §3, the IVA regime catalogue `clave_iva.dta`, PEF classification `PEF.ado:1145-1273`);
divergence from CIEP's numbers must be explained line by line. Risk: scope creep into redesigning the
method rather than porting it.

**(c) Keep Stata and wrap it (`pystata`).**
Pros: zero methodological risk; fastest to a working interface (the web already does this via PHP); CIEP's
governance principle ("Stata produce los números") is respected. Cons for a self-contained machine
delivered to a ministry: a Stata/MP or SE licence per machine (annual, named or site), 17–20 s per
evaluation and one evaluation at a time per licence (CIEP caps at 3 concurrent on one MP licence),
~1.3 GB of assets plus `master/` and `users/ricardo/` artefacts that must be regenerated by a 35-minute
batch whenever data change, Stata version pinning (17 vs 19.5 differences), and an LLM loop that cannot
run thousands of evaluations. Maintainability: every CIEP release changes the template keys and the
`output.txt` contract positionally. Acceptable as a **bridge** during phase 1 and as the generator of
golden masters; not acceptable as the delivered Layer A.

**(d) Recommended hybrid.**
1. Pin a release tag (v8.15.3, baseline v8.15.0) and obtain from CIEP, or generate once with Stata, the
   frozen artefact set listed in §7.4. Treat `*RECprom.dta` as data (do not try to reproduce the
   bootstrap).
2. Phase 1: Python `run(parameters)` over those artefacts, verified on the default scenario and on a
   perturbation grid produced by Stata through `perfilar-web.py`/`test-web-batch.sh`. This gives
   FISCUS the full web action space (142 inputs) in weeks and exposes the closure problem (Q1)
   explicitly, so a FISCUS closure rule can be added as a Python option without touching CIEP's method.
3. Phase 2: specification first (one document per module, in CUAD-0's format, co-signed by Ricardo),
   then Python re-implementation of the micro pipeline against regenerated `.dta` checkpoints, with the
   probit/ranking and fixed-point stages verified at tolerance, not bit.
4. Keep CIEP's `gate-numeros.sh` logic as the regression test of the Python package (same fixtures,
   same 1e-9 rule for Sankeys, exact string match for the 47 keys at printed precision).

### 8.4 Python vs R (side note)

[inferred] The choice of Python changes little technically: weighted sums, groupby and the fixed point
are equivalent in pandas/numpy and data.table/dplyr; weighted quantiles with Stata's rule must be
hand-written in either; `survey`/`srvyr` in R are richer than Python's offerings but the code never uses
`svy` (only fw/aw sums and one cluster bootstrap), so that advantage is moot. Reading `.dta`: `haven`
(R) and `pyreadstat` (Python) are both fine, including value labels and Stata-13 files. Probit: `glm`
in R reproduces Stata more closely out of the box than statsmodels (same Fisher scoring family), a minor
point. Interoperability with the R NTA layer: the natural interface is files (parquet/JSON of profiles by
age×sex), not in-process calls; the `NTA.do` outputs are already JSON. Team skills visible in the code:
the author writes Python inside Stata (`AccesoBIE`, `ensure_asset`, `profile.do`) and Bash; there is no
R in the repository; Python is the lower-friction choice for CIEP collaboration and for an LLM harness.

### 8.5 Top five risks (ranked) with mitigation

1. **Moving target / governance.** [observed] 13 versions between 2026-10-06 and 2026-11-03; CUAD-0
   re-anchored the whole income side on 2026-10-31; 8.16 announces further changes to ISR PM,
   informality and IVA anchors. A port of v8.15.3 is obsolete on arrival unless it is a port of the
   **specification** plus a thin layer that re-reads CIEP's frozen artefacts per release. *Mitigation*:
   pin tags and `baseline`; design phase 1 to consume CIEP artefacts; agree with Ricardo that FISCUS's
   Layer A is a documented fork with its own baseline, not a mirror.
2. **Hidden inputs not in the public release.** [observed] `clave_iva.dta`, `censo_eco_municipios.dta`
   (inside the ENIGH assets), `LIFs.xlsx` mappings, and all `master/` and `users/ricardo/` artefacts are
   CIEP-built and not in the repo; the ENIGH assets are repackaged by CIEP. *Mitigation*: obtain the
   27 raw assets (they are on the GitHub Release, SHA-pinned) and the artefact set of one release;
   verify SHAs against `manifest.json`.
3. **No closure and no macro feedback** (Q1, Q5). [observed] Layer A as it stands answers "what debt
   path follows from these levels" to 2032 only; FISCUS experiments on sustainability need a rule
   (tax/spending/debt target) and a longer horizon, which the code does not have (and `end(2100)` would
   just extrapolate trends with the `±5` cap). *Mitigation*: implement the closure as an explicit Python
   option in phase 1 and label results as FISCUS extensions.
4. **Non-reproducible pieces**: bootstrap means in `*RECprom`, probit+ranking formality, `perfilpc`
   fixed point, MP-thread summation order, float-vs-double default on the VPS (NDS). *Mitigation*:
   freeze `*RECprom` as data; verify probit stage at tolerance with a documented count of flipped
   persons; copy the fixed-point rule; set tolerances per stage as in §7.3; ask CIEP for the VPS
   `set type` status.
5. **Parameter duplication and undocumented constants** (§6): CSS_ISSSTE copies differ, IEPS tables
   differ, IVA informality 23.1 vs 7.77, ISR_Mod ratios, Pemex splits, `smdf` concept. A port must
   choose; a wrong choice silently changes numbers. *Mitigation*: parameter schema with provenance
   fields; a reconciliation table signed by Ricardo before coding (see §9).

Secondary risks: Spanish/accents in identifiers and `latin1` charset vs UTF-8 `.dta`; missing-value
comparisons (175 sites to audit); positional contracts (2026–2032 vectors, `GASTOS[i]` by DOM order);
the `$pais` leftovers in `IVA_Mod.do:336` and `output.do:385-392` (paths `users/$pais/$id` with `$pais`
empty work on POSIX only by accident of `//`).

---

## 9. Questions for Ricardo Cantú

Blocking for the assessment / for phase 1:

1. **Artefacts.** Can CIEP provide, for one tagged release (v8.15.3), the frozen set the web run reads:
   `master/perfiles2027.dta`, `master/2024/{households,expenditures,categ_iva,consumption_*}.dta`,
   `master/2024/cuadratura.do`, `master/{Poblacion,PIBDeflactor,SCN,LIF,PEF,SHRFSP,DatosAbiertos,Deflactor}.dta`,
   `users/ricardo/bootstraps/250/*.dta` (at least the 41 `*RECprom`), `users/ricardo/cache/`? Without
   them nothing can be verified on Dalila (no Stata here).
2. **Precision regime on the VPS.** Does the batch/web Stata run with `set type double` (as `profile.do:27`
   sets permanently on researcher machines) and `set processors 1`? Which exact Stata version produced
   `fixtures/output-default.txt`?
3. **Which copy is canonical** when the code disagrees: `CSS_ISSSTE` in `SIM.do:251-260` vs
   `Households.do:1583-1592`; `IEPST` 17-row vs 10-row; `IVAT[13]` 23.1 vs 7.77; `smdf` (UMA vs minimum
   wage by year).
4. **Provenance of calibration constants**: `ISR_Mod.do` ratios (176, 184, 193, 208, 213), `602513/1169476`,
   `110000/181290`, `24.30` in the ISSSTE federal quota, `0.634768962`, `FAM_cuidados`.
5. **Closure intent.** The PV balance and generational accounts were retired on 2026-09-12 "pending the
   restructuring of the long-term projection" (`FiscalGap.ado:413-416`). What is the intended closure
   and horizon, and is `CuentasGeneracionales.ado` to be revived or deleted?

Important but not blocking:

6. Is the revenue projection meant to be independent of the GDP-growth inputs after the anchor year
   (`FiscalGap.ado:154-198`), or is an elasticity to GDP planned?
7. `actualizacion_geo` (`FiscalGap.ado:840-847`): what economic content does the geometric revaluation
   factor carry, and why are PIDIREGAS/IPAB/FONADIN/Deudores/Banca frozen but excluded from projected
   RFSP (l.880-881)?
8. ISR PM incidence: the planned 8.16 rule (∝ `d4_relativo`) — timing, so phase 2 targets the new rule.
9. `clave_iva.dta` and `censo_eco_municipios.dta`: are the builders available, and can the IVA regime
   catalogue be published as a CSV?
10. Is the fixed-point intra-household allocation (`perfilpc`) the intended default versus the NTA
    equivalence scale `alfa` (`Expenditure.do:865-867`, apparently unused)?
11. Governance: would CIEP accept a Python re-implementation as a documented fork with its own baseline,
    given `arquitectura.md §6.3.1` ("Stata produce todos los números")? Would Ricardo co-sign the module
    specifications of phase 2?
12. Licensing of the data assets (ENIGH repackaging, CSI spreadsheets) for redistribution inside a
    machine delivered to a ministry.

---

### Appendix A. Method of this assessment

Read-only extraction (`chmod -R a-w source/`); no code executed from the zip; no network; Python 3
(standard library only) for counting scripts (`../scripts/`). Files read in full: `SIM.do`,
`Web.Stata.do`, `profile.do`, `FiscalGap.ado`, `SHRFSP.ado`, `Simulador.ado`, `PIBDeflactor.ado`,
`Poblacion.ado`, `GastoPC.ado`, `PerfilesSim.do`, `Households.do`, `Expenditure.do`, `TasasEfectivas.ado`,
`ISR_Mod.do`, `IVA_Mod.do`, `output.do`, `CuentasGeneracionales.ado`, `Precache.ado`, `_precache_*.ado`,
`escalar.ado`, `Distribucion.ado`, `Gini.ado`, `REC/PC/PERF/INCI/CICLO.ado`, `calculaStata.php`,
`checkStataStatus.php`, `config.php`, `gate-numeros.sh`, `CITATION.cff`; read in part: `SCN.ado`
(§0–1.3, update routines via grep), `LIF.ado` (UpdateLIF), `PEF.ado` (classification), `NTA.do` (§0–§4),
`perfilpc.ado` (header), `SankeySF.do` (header), `AccesoBIE.ado`, `DatosAbiertos.ado`, `ensure_asset.ado`
(headers), `arquitectura.md` (§1, §4, §6.3, §7), `CUAD-0.md` (§1–§5), runbook (§4c, §9, §13), perf
reports, `FiscalGap.md` help, `index.php` (input tags), `stataCalcula.js` (key mapping). Not read:
`04_3_anteriores/` (previous site versions), vendored JS/CSS, `scalarjson.ado`, `nodos/*`,
`Sankey{CFE,Pemex}.do`, `TarjetaRFSP.do`, `Perfiles.ado` body.

### Appendix B. Note on `03_help/FiscalGap.md`

The help file describes formulas that are no longer in the code (PV balance `balanceVP`, `tabout` CSV
tables, `shrfsp_externo*(1+0.03)^t`, `tasaEfectiva [fw=deuda]`): [observed] none of these appear in
`FiscalGap.ado` v8.15.3. Treat `03_help/*.md` as historical, and the module headers plus `CUAD-0.md`
as the current method.
