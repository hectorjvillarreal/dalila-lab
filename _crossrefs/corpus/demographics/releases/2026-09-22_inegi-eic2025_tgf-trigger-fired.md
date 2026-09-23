---
title: "INEGI Encuesta Intercensal 2025 (Reporte de Resultados 37/26) — TGF 1.2 (2024): Q3 §2 re-anchor trigger FIRES; fifth scenario row per pre-committed frame; population, aging and migration anchors"
date: 2026-09-22
added_by: Claude
endorsed_by: Anne
projects: [DFD, BDH, Aurora]
indicators: [tfr, births, population, median_age, dependency_ratio, migration]
geography: [mexico, subnational]
scenario_implication: [fast-transition, baseline-revision]
source_reliability: primary   # INEGI official results report, published 2026-09-22
data_vintage: 2025   # reference date 15 Oct 2025; TGF refers to births in the 12 months before enumeration, labelled 2024
promotion_status: ready
corpus_path: _crossrefs/corpus/demographics/releases/
trigger_status: FIRED   # Q3 §2 re-anchor trigger; frame branch "below 1.45"
supersedes: "(none — first INEGI TGF publication for vintage 2024; extends 2026-08-03_inegi-enr2024-mex-births.md)"
---

## Summary

INEGI's Encuesta Intercensal 2025 (enumerated 6 Oct–14 Nov 2025, ~7.33 M dwellings,
reference date 15 Oct 2025) reports total population **130,911,314** (130,393,389 in
private dwellings + 517,925 complementary), average annual growth **0.7%** for 2020–25
against 1.0% for 2015–20, median age **32** (29 in 2020), about **10% aged 65+**, and a
**Tasa Global de Fecundidad of 1.2 for 2024**, down from 1.9 in 2019 (CPV 2020, same
method). All 32 entities are below 2.0: Chiapas 1.8, Guerrero 1.6, Durango and Zacatecas
1.5; Querétaro 1.1, Baja California 1.0, **Ciudad de México 0.8**. Average children ever
born to women 12+ fell 2.1 → 1.9 (4.9 for no schooling; 1.2 for upper-secondary or
higher). International emigration Oct 2020–Oct 2025 was ~1.3 M (802.8 k in 2015–20),
70.4% male, concentrated at ages 20–29; return migrants 150.8 k, down from 2020.
Foreign-born residents 1,170,030 (57.1% US-born; 50.7% hold Mexican nationality).

## Trigger of record — Q3 §2: FIRES

Q3 armed: *if INEGI publishes a TGF ≤ 1.50 for vintage 2024 or 2025, the Central anchor
goes to Anne.* Both legs met: INEGI publication; vintage 2024; **1.2 ≤ 1.50.**

Anne's pre-committed frame (2026-08-03): published TGF in [1.45, 1.50] → re-pin Central
at the published value; **below 1.45 → do not chase the point estimate; open a fifth
scenario row; keep Central at 1.50 as the upper bracket.** The "below 1.45" branch
applies. **Ruling: fifth scenario row opens; Central stays 1.50 as upper bracket; the
Q3 replicate is not amended (endorsed; PROTO-RAG-001 standing principle 5). Execution
lands in the Q4 replicate. Ratification of the row: Héctor.**

## Instrument caveat — why the frame says "don't chase"

The EIC TGF is a **survey direct estimate** (births in the 12 months before enumeration,
women 15–49 resident in private dwellings), not a vital-registration rate. Direct
estimates of recent births are known to under-report (omission, reference-period error)
and are conventionally reconciled against registration (Brass P/F). The calibration check
is internal to INEGI's own series: the same method gave **1.9 for 2019** in CPV 2020,
against a registry-based 2019 rate on the order of 2.0–2.1 (**to be confirmed from ENR
definitive 2019 births**). If the instrument runs ~0.1–0.2 low, the bias-adjusted 2024
value sits around **1.3–1.4** — still below the [1.45, 1.50] re-pin band, below Q3's
registry-implied ≈1.46 (ENADID 2023 scaled by the ENR rate decline), and below F-V's
1.51/2025 extrapolation. The three readings now span **1.2 – 1.46 – 1.51**; none is
registry-clean. **The reconciled 2024 value is unlikely to be 1.2 and unlikely to be
1.5.** Anne does not assert a point value here.

## DFD Calibration Implications

**Fast-transition TFR scenario for Mexico.** Fifth row opens. Proposed specification, for
Héctor: `EIC-2025 direct` — TFR 1.2 stable from 2024, labelled *unreconciled survey
direct estimate*, positioned between Central (1.5 stable) and Stress (→1.0 by 2030).
The row's first task is its own reconciliation; it is a bracket, not a forecast. Note the
consequence for the Stress column: a path to 1.0 by 2030 no longer reads as a tail
scenario. The stress-floor decision escalated on 2026-09-15 (Chile 0.99; floor
unidentified, 0.9 working) is now the more urgent of the two.

**Dependency-ratio path feeding IM-6's pension contribution rate.** Three level anchors
to check against the CONAPO conciliación and the WPP 2024 base — Cath ruled the base
difference load-bearing for the Q3 TDR wedge:
- population 130.91 M at Oct 2025 (growth 0.7%/yr);
- median age 32 and 65+ share ~10% — if ahead of CONAPO's projected 2025 values, aging
  is running ahead of the projection base;
- net international migration: emigration 1.3 M / returns 0.15 M in 2020–25, a regime
  shift relative to 2015–20 and a **lower bound** (fully-emigrated households are not
  captured). Working-age, male, 20–29. Feeds TDR directly. Route to Cath.

**Survival probabilities in the OLG demographic block.** Not directly affected.

**Coupling/partnership formation as upstream fertility driver.** No union-status
tabulations in this release; the microdata (tabulados, Nov 2026 per §VII) should carry
conjugal status by age and sex and would give an ENOE-independent 2025 coupling point
for Mexico. Flag for acquisition.

## Open-data addendum (2026-09-23, added by Claude — not yet endorsed by Anne)

INEGI published an open-data bundle alongside the report: *Principales resultados
por localidad de 50 000 y más habitantes* (identifier NTMPPIEG_INEGI_UES-EIC-2025,
modified 2026-09-22; 349 indicators at national, entity, municipal and 50k+ locality
level, each with five estimator rows: value, standard error, lower and upper
confidence limit, coefficient of variation). It is a tabulado with precision
measures, **not microdata**. Local copy:
`sources/INEGI_2026-09-22_EIC2025_datos-abiertos_105_localidad50k.zip`
(sha256 e6ad7e8f…defa182; the CSV inside is Latin-1 encoded, 27 MB). National and
entity rows with the demographic indicators are extracted to
`country/MEX/eic2025_entity_indicators.csv` (165 rows, five estimator rows per
entity). Four points bear on the entry above.

1. **The 1.2 is 1.23, and sampling error is not the caveat.** National TGF 1.23,
   standard error 0.01, confidence interval [1.22, 1.24], CV 0.47%. The report's
   1.2 is rounding. Whatever gap exists between 1.23 and a reconciled registry
   value is instrument bias (omission, reference-period error), not sampling noise
   — the §Instrument-caveat argument stands and the reconciliation task is
   unchanged. Entity CIs are also tight where it matters: Ciudad de México 0.79
   [0.76, 0.82]; Chiapas 1.75 [1.72, 1.78]; Guerrero 1.59; Durango 1.51 [1.42, 1.59];
   Zacatecas 1.49; Baja California 1.04 [0.95, 1.13]; Querétaro 1.06; México 1.07.
   No entity's upper confidence limit reaches 1.8.

2. **Dependency ratio observed directly, Oct 2025: total 46.40 [46.28, 46.52];
   child 31.58; old-age 14.82** (0–14 and 65+ over 15–64, private dwellings). The Q3
   replicate §4 wedge set the CONAPO-share-implied TDR at ≈49.3 against the Central
   path's ≈46–47 for 2026. The EIC observation falls on the Central/WPP side of that
   wedge, not the CONAPO side. This is a survey estimate on a private-dwelling base
   and a different reference date, so it does not close the wedge by itself —
   **route to Cath with the Q4 retabulation**, where it becomes the third base.
   Median age 31.89 [31.83, 31.94]; 65+ population 13.19 M, 10.1% of the
   private-dwelling total; aging index (60+/0–14) also available by entity.

3. **Correction to §DFD calibration implications, item 4:** the release *does*
   carry union-status tabulations, at national and entity level, for population
   12+. National: married or in unión libre **50.22%** [50.15, 50.29] (women 48.42,
   men 52.19); never-married 36.19% (women 33.53, men 39.11); separated, divorced
   or widowed 13.49% (women 17.93, men 8.59). Ciudad de México partnered share
   43.39% (women 40.80), the lowest entity; Chiapas 54.31%, the highest. This is an
   EIC-anchored 2025 coupling point, independent of the ENOE-based 53.9% carried in
   Q3 §3 — but the two are **not directly comparable** (12+ versus adults; survey
   versus labour-force instrument). The 20–39 sex-disaggregated cut still needs
   microdata; the acquisition flag for that stays open.

4. Children ever born, women 12+: 1.93 [1.93, 1.94], consistent with the report's
   1.9.

Municipal and 50k+-locality rows (all 349 indicators, with CIs) are in the bundle for
any subnational work; not extracted here.

## Implications for the fertility-collapse paper (routed)

1.9 → 1.2 in five years on a consistent instrument is LAC-collapse speed. Mexico was the
paper's lagging core country and biennial comparator; on this evidence it is not lagging.
CDMX at 0.8 is Puerto-Rico-level. The extensive-vs-intensive question is testable in the
EIC microdata once released (parity distribution by age of women 15–49).

## Project Routing Notes

- **BDH** — 65+ share ~10%; median age 32; the education gradient (4.9 vs 1.2) and the
  emigration profile bear on health-financing capacity and the informality mix.
- **Aurora** — the emigration regime shift (1.3 M, male, 20–29) as a structural force.

## Actions (ordered)

1. **Reconciliation (Anne + Debb, Q4, load-bearing):** EIC methodology (question wording,
   reference period, any P/F adjustment); registry-based 2024 TGF from ENR definitive
   2024 births (1,672,227) over the EIC 2025 women-15–49 denominator; CPV-2020/ENR
   2019 comparison for the instrument bias; produce a reconciled 2024 range.
2. **Fifth scenario row** — Héctor ratifies; Anne specifies; executed in the Q4
   replicate; `DFD_TFR_forecast_instructions.md` bumps to v1.5 on execution.
3. **Level / aging / migration checks** vs CONAPO conciliación and WPP 2024 base → Cath.
4. **Corpus:** this entry to `releases/`; source PDF to `sources/INEGI_2026-09-22_EIC2025_RR-37-26.pdf`;
   inbox line at production time (produced in chat, awaiting commit — the 2026-09-15
   filing-gap lesson).
5. **Paper chat** flag (above).
6. **Stress-floor decision** (2026-09-15) — upgraded in urgency; decide with item 2.

## Source

INEGI, *Encuesta Intercensal (EIC) 2025 — Reporte de Resultados 37/26*, 22 September
2026, 39 pp. URL: https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/ei/EIC2025-def_RR.pdf
(acquired 2026-09-23, sha256 e450d060…cdde66). Local copy:
`sources/INEGI_2026-09-22_EIC2025_RR-37-26.pdf`. Open-data bundle: https://www.inegi.org.mx/contenidos/programas/eic/2025/datosabiertos/conjunto_de_datos_eic2025_105_csv.zip
(acquired 2026-09-23) → `sources/INEGI_2026-09-22_EIC2025_datos-abiertos_105_localidad50k.zip`; entity extract `country/MEX/eic2025_entity_indicators.csv`. Fertility: p. 9–10 (Gráfica 5, note: rates
computed from births in the year before enumeration, presented for 2019 and 2024).
Population: p. 5–6. Age structure: p. 7–9. Migration: p. 11–13.
