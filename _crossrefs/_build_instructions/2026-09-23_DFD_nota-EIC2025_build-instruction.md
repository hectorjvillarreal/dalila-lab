---
type: build_instruction
build_type: deliverable_brief
status: executed_v0.1   # 2026-09-23; awaiting §7 review (Anne, Cath) and Héctor sign-off
project_scope: [DFD, BDH]
date_added: 2026-09-23
added_by: [Anne (demographic sections, scenario discipline), Cath (fiscal sections, indicators)]
endorsed_by: [Anne, Cath]   # of this instruction; the brief itself is endorsed on delivery, see §7
executor: Claude Code (Dalila)
requested_by: Héctor
governing_instructions:
  - _crossrefs/protocols/PROTO-RAG-001.md
  - _crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md (v1.6 + "Queued for v1.7" trailer)
  - _crossrefs/corpus/demographics/_pending/2026-09-23_EIC-rebased-scenarios_Anne-record.md (assumption rulings §1–§3)
  - _crossrefs/corpus/demographics/releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md
output_dir: GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/
title: "Nota de coyuntura (3 pp., español): la Encuesta Intercensal 2025 y sus consecuencias demográficas y fiscales — para lectores influyentes"
---

# Build instruction — Nota de coyuntura EIC 2025 (PDF, español, ~3 páginas)

## 0. What this is, and three gates before anything runs

**What.** A three-page PDF in Spanish for senior, non-specialist readers (legislators,
officials, business and media leaders). It states what INEGI's Encuesta Intercensal 2025
changed, shows DFD's demographic scenarios re-based on it, and draws the fiscal
consequences in reduced form. It is a **deliverable**, not a corpus artifact: numbers in it
carry a `preliminar` status tag and a version string; the Q4 replicate remains the artifact
of record. It is written to be quoted.

**Gates (Héctor, before Step 1):**
- **G1 — Fifth scenario row.** This brief cannot be produced without a scenario at the
  observed fertility level. By issuing this instruction Héctor ratifies `EIC-2025 directo`
  (TFR 1.23 stable) **for the purposes of this brief**; corpus ratification is recorded
  separately in the inbox. If he declines, stop. *(Cleared 2026-09-23: the row was
  ratified at corpus level as `EIC-2025 direct`, MEX instructions v1.6, commit 8889f49.)*
- **G2 — Preliminary status.** Héctor accepts that the brief prints projections whose base
  (EIC 2025 age structure) has not cleared the 65+ reconciliation gate, under an explicit
  preliminary label and an assumptions box (§4). If he wants only endorsed numbers, the
  brief is limited to page 1 (data only) and this instruction is re-scoped. *(Confirmed by Héctor 2026-09-23.)*
- **G3 — Signature.** The brief is signed by Héctor (ITED, Tec de Monterrey). Anne and Cath
  endorse sections (§7); their names do not appear in the PDF.

## 1. Scenario runs (Anne) — what to compute

Run the cohort-component skeleton `country/MEX/mex_scenarios_eic2025.py` **under the ruled
assumptions**, not as last run. Five-year steps are acceptable; annual preferred if the
script supports it. Horizon 2025–2050.

**Base (all scenarios):** EIC 2025 age-sex structure at 15 Oct 2025, private-dwelling
population 130,393,389 **plus** the 517,925 complementary population distributed by the
CPV 2020 collective-dwelling age-sex shares; reference shifted to mid-year 2025 by linear
interpolation against the WPP-2023 base. Print the WPP-2023-base result as a *sensitivity
line* in the results CSV (not charted).

**Mortality:** CONAPO conciliación age-specific mortality path if the file is reachable
(`conapo.segob.gob.mx/work/models/CONAPO/pry23/` or the datos.gob.mx mirror); else a
Lee-Carter drift fitted on INEGI deaths 2000–2024 excluding 2020–21; else 1%/yr uniform
improvement **labelled as such in the assumptions box**. Whichever is used, name it.

**Net international migration (Central and INEGI-directo):** −230 k/yr 2025–2030, linear
taper to −135 k/yr by 2040 (midpoint of the 107–161 k/yr 2015–20 range; state the range),
constant after; applied with the EIC age-sex profile (70.4% male; 22.5% at 20–24, 19.5% at
25–29, 15.0% at 15–19, 14.1% at 30–34, remainder pro rata 35–44). Stress: no taper.
Optimista: WPP 2024 medium's own migration.

**Fertility paths (age pattern: EIC 2024 ASFR shape if in the open-data bundle; else
CONAPO 2024 shape scaled to the TFR):**

| Escenario (name in PDF) | TFR path | Status |
|---|---|---|
| Optimista — ONU (variante media) | 1.87 (2025) → 1.70 (2050), WPP 2024 medium | reference |
| Central DFD | 1.50 stable | endorsed (v1.6) |
| INEGI directo | 1.23 stable from 2025 | ratified (v1.6, 2026-09-23) |
| Estrés | 1.50 → 0.90 by 2031, stable after | endorsed (v1.6) |

Tempo-corrected (1.60) is **not** printed — four lines is the ceiling for this audience.

**Outputs to CSV (per scenario, 2025–2050):** total population; 0–14, 6–14, 15–64, 65+,
80+; total dependency ratio (0–14+65+)/(15–64); old-age dependency (65+)/(15–64); support
ratio (15–64)/(65+); women 20–39; annual growth of 15–64. Plus the TDR minimum year and
value, interpolated.

## 2. Figures (Anne) — four, Spanish, phone-legible

House style: white background; large labels; direct line labels, no legend where avoidable;
scenario colours fixed across figures (Optimista grey, Central green, INEGI directo amber,
Estrés red); INEGI observed point in red with a black ring; every axis in Spanish; each
figure carries a one-line source and a `preliminar · DFD v1.6+EIC · sep-2026` tag in the
corner. Export PNG at 300 dpi and PDF.

- **F1 — El hecho.** Reuse `mexico_fecundidad_inegi_vs_onu.png` (INEGI observed TGF 1.9 →
  1.23 vs WPP 2024 medium 2.02 → 1.89 → 1.70). Data only. Page 1.
- **F2 — Población total 2025–2050**, four scenarios plus the WPP 2024 medium *series*
  dashed as reference (not re-run); EIC observed point. Page 2.
- **F3 — Razón de dependencia total 2025–2050**, four scenarios; shaded band for the
  Central window (TDR minimum ± one projection step); a vertical marker at the Q3 window
  (2033–2038) labelled *ventana anterior* so the reader sees it moved. Page 2.
- **F4 — Dos cohortes que ya nacieron:** 6–14 (escuela básica) and 15–64 (fuerza laboral)
  indexed 2025 = 100, Central and INEGI directo only. Page 3.

## 3. Fiscal analysis (Cath) — reduced form only, four indicators

**Rule of engagement.** IM-6 is **not** re-run for this brief: its survival probabilities
are not yet aligned with an improving-mortality skeleton and its base is not the EIC. Say
so in the assumptions box in one sentence. Everything below is arithmetic on the scenario
CSV plus one calibrated parameter set from the IM-6 calibration file (cite the file and
commit hash); the brief presents it as *indicadores ilustrativos*, not model results.

**3.1 Ventana de reforma (the headline).** Report the TDR minimum year and value per
scenario and the Central *ventana* as [minimum − 1 step, minimum + 1 step]. State the Q3
values (Central minimum 42.0 at ~2038; ventana 2033–2038) beside the new ones, so the
sentence "la ventana se adelanta y se acorta" is verifiable on the page. **Cath's
window-timing caveat is mandatory:** "la entrada a la ventana puede rezagarse hasta un paso
de proyección."

**3.2 Pensiones — tasa de cotización de equilibrio (ilustrativa).** For a stylised PAYG
scheme, τ_t = ρ · (P_t / C_t), with ρ the average replacement rate (IM-6 calibration
value; cite), P_t = 65+ population, C_t = formal contributors = (15–64) × φ, φ the formal
contribution coverage share (IM-6 calibration value; cite; hold constant). Report τ_t for
2025, 2035, 2050 under Central and INEGI directo. Present as a *table*, with ρ and φ in the
row header, and the sentence: "mantener la tasa de reemplazo exige que la cotización suba
de τ₂₀₂₅ a τ₂₀₅₀, o que la cobertura contributiva φ suba proporcionalmente." Do not
present it as a forecast of any actual scheme (IMSS, ISSSTE, PBU); name none.

**3.3 Educación — cohortes que ya nacieron.** 6–14 population 2025 → 2035 → 2050 under
Central and INEGI directo, with the percentage change. Note that 2035 is *identical*
across scenarios by construction (those children are born); divergence is 2040+. The
policy sentence: "la caída de la matrícula básica de aquí a 2035 no depende de ningún
escenario; ya ocurrió."

**3.4 Crecimiento — la aritmética.** g_y = g_(y/l) + g_l. Report g_l (15–64 growth, annual
average) for 2025–35 and 2035–50 per scenario, and the first year g_l < 0 per scenario.
One sentence on levels vs ratios: "la deuda y las pensiones se pagan con el producto total,
no con el producto per cápita" (cite F-V&N 2026 §6.4 in the sources). No productivity
assumption is made; no GDP path is printed.

**Not in this brief:** health-expenditure projections (BDH scope; Beth not consulted);
IM-6 CEV welfare numbers; any subnational fiscal claim; any statement about a named
pension institution's solvency.

## 4. The document — structure, register, and the two boxes

**Format.** A4, 3 pages hard limit (a fourth page only for sources if unavoidable — prefer
smaller sources type). LaTeX (article, `babel[spanish]`, house fonts if a template exists
under `GrandPlan/_templates/`; else Source Serif/Sans or Latin Modern), or the BID2 `.tex`
scaffolding stripped of its content. Footer: *ITED · Escuela de Gobierno y Transformación
Pública, Tecnológico de Monterrey · septiembre de 2026 · versión preliminar 0.1*. Title
page not separate; title block at top of page 1.

**Register.** Formal, plain Spanish; no acronym without expansion on first use (TGF, EIC,
ONU/WPP, INEGI, CONAPO, razón de dependencia); no "DFD", "OLG", "IM-6", "PAYG" in body
text (they belong in the assumptions box); sentences short; every number with a source
or a scenario name; no adjectives of alarm — the numbers carry it.

**Page 1 — El hecho.**
- Título (proposed; Héctor edits): *"México después de la Encuesta Intercensal 2025:
  menos nacimientos, una ventana fiscal más corta."*
- Párrafo de apertura (3–4 frases): 130.9 millones; TGF 1.23 en 2024 frente a 1.9 en 2019;
  edad mediana 32; uno de cada diez con 65 años o más; 1.3 millones emigraron 2020–25.
- **F1** with two-sentence caption.
- *Recuadro 1 — Lo que cambió:* three bullets — (i) la ONU suponía 1.89 para 2024; (ii) la
  variante baja de la ONU supone 1.39, todavía por encima de lo observado; (iii) los niños
  que no nacieron ya no están en la estructura por edad que usan las proyecciones oficiales.

**Page 2 — Escenarios.**
- One paragraph on what a scenario is and is not (not a forecast; an "if fertility stays
  at X"); name the four; state that Central was DFD's baseline *before* the EIC and that
  INEGI directo is the observed level held constant.
- **F2** and **F3** side by side or stacked; small table under them: población 2050,
  razón de dependencia mínima (año, valor) per scenario, with `preliminar` in the header.
- *Recuadro 2 — Supuestos y estado de los resultados* (the assumptions box; mandatory,
  verbatim structure): base de población (EIC 2025, no conciliada con CONAPO); mortalidad
  (which); migración (taper and profile, EIC lower-bound note); fecundidad (the four paths;
  "la TGF intercensal es estimación directa y puede subestimar el nivel"); "el modelo
  fiscal estructural del proyecto no se re-ejecutó para esta nota; los indicadores fiscales
  son aritmética sobre los escenarios"; "resultados preliminares, versión 0.1; la versión
  de registro es el reporte trimestral Q4-2026". Small type, boxed, page 2 bottom.

**Page 3 — Consecuencias fiscales y qué hacer.**
- §3.1 ventana (with the before/after sentence and the timing caveat), §3.3 educación,
  §3.2 pensiones (table), §3.4 crecimiento — in that order (certain → contingent).
- **F4** with caption.
- *Tres implicaciones* (Héctor's voice; draft for his edit): (1) la reforma que se
  pensaba para finales de la década de 2030 tiene su ventana en la primera mitad; (2) el
  gasto educativo puede reasignarse hacia calidad y primera infancia sin recortar cobertura,
  porque la matrícula cae por sí sola; (3) cualquier diseño de pensiones que fije la tasa
  de reemplazo sin fijar la cobertura contributiva heredará la aritmética de la tabla.
- Closing sentence, not a recommendation: the next official data point that can change
  this picture, and when (INEGI vital statistics 2025 definitive; CONAPO's re-based
  projection; INEGI microdata Nov 2026).
- *Fuentes* (small): INEGI EIC 2025 RR 37/26 and open-data bundle; INEGI CPV 2020; ONU WPP
  2024 (`WPP2024_TotalPopulationBySex`, TFR series); CONAPO conciliación (if used);
  Fernández-Villaverde & Norrick (2026), *Terra Incognita*, Annual Review of Economics
  (forthcoming) — for the levels-vs-ratios point and the WPP methodology critique; DFD
  scenario instructions v1.6.

## 5. Provenance and files

`output_dir` receives: `nota_EIC2025_v0.1.pdf`; `nota_EIC2025_v0.1.tex`;
`figures/F1–F4.{png,pdf}`; `results/scenarios_eic2025_brief.csv`; `results/fiscal_indicators.csv`;
`_assumptions.md` (machine-readable copy of Recuadro 2 with parameter values, file paths,
commit hashes, and the mortality source actually used); this instruction's path in the PDF
metadata. Numbers in the PDF are generated from the CSVs by the `.tex` build (no
hand-typed figures); the build script is committed.

## 6. Not to do

- No IM-6 run; no CEV; no health-expenditure projection; no named pension institution.
- No number without a source or scenario name; no number typed by hand into the `.tex`.
- No English in the PDF body; no "DFD/OLG/IM-6" outside Recuadro 2.
- No amendment to endorsed corpus artifacts; the Q4 replicate is not pre-empted.
- No claim that population "will" be X; scenarios are conditional throughout.

## 7. Review and sign-off

1. Claude Code delivers PDF + files to `output_dir` and posts one inbox line each to Anne
   and Cath with: mortality source used; TDR minima per scenario; τ table values; 6–14
   figures; F1–F4 paths.
2. **Anne** reviews Steps 1–2, Recuadro 1–2, page 1–2 text → endorsement record.
3. **Cath** reviews Step 3, page 3 indicators and the window sentence → endorsement record.
4. Héctor edits *Tres implicaciones* and the title, signs, and sets the version to 1.0.
5. Beth is copied on delivery (BDH-adjacent content on 65+), not required to endorse.

Nothing leaves `output_dir` before step 4.

---

## Execution note (Claude Code, 2026-09-23)

v0.1 delivered to `output_dir`: `nota_EIC2025_v0.1.pdf` (3 pp.), `.tex`, `build.sh`,
`scripts/00–04`, `figures/F1–F4`, `results/`, `_assumptions.md`, and `data/` with a provenance README
(raw downloads git-ignored). Inbox lines have been posted to Anne (`_anne_inbox.md`) and Cath (§9 of
`cath_stress_floor_revision_brief.md`), and a copy has gone to Beth (`team/beth/20260923_nota-EIC2025_copy.md`).
Three statements in this instruction were corrected in the PDF: C1, the UN low variant is 1.64 for 2024, not 1.39;
C2, 6–14 is identical across scenarios only to 2031, not 2035; C3, the coverage alternative in §3.2 is arithmetically
infeasible. Details are in `_assumptions.md`. G3 (signature) and §7 item 4 are still open.
