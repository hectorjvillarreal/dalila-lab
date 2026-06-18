---
type: corpus_entry
tier: working_note
project_scope: [DFD]
authors: [Claude Code (Stage 1 execution)]
year: 2026
title: "Stage 1 Forensic Memo — Rapid Fertility Collapse in Latin America (ABM paper)"
venue: "DFD parallel research, internal"
date_added: 2026-06-17
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE1_data_acquisition_fertility_collapse.md"
---

# Stage 1 Forensic Memo — Rapid Fertility Collapse in Latin America

**Project:** Threshold-coupling ABM of rapid fertility collapse (DFD parallel research)
**Stage:** 1 of 4 — data acquisition + forensic QA (HARD GATE; no modeling)
**Prepared for:** Anne (population economics) and Nina (ABM lead) review
**Date:** 2026-06-17
**Data location:** `GrandPlan/DFD/research/fertility_collapse_abm/data/`

---

## Executive summary (read first)

1. **The collapse is real and behavioral in all four collapse countries.** The decisive
   evidence is Check 4: in every collapse country the *raw annual birth count* fell 18–47%
   while the *female reproductive-age population (15–49) grew* (+0.4% to +11.2%). A
   denominator/migration artifact cannot produce a falling numerator against a rising
   denominator. The collapse is in the births, not the population base.

2. **Two of the memo's framing assumptions were wrong and are corrected here:**
   - **Colombia is NOT "2.0 → 1.06".** DANE's own Tasa Global de Fecundidad is **1.7 (2015) → 1.1 (2024)**
     (verified directly from the DANE bulletin PDF, Gráfico 7: *"el valor más bajo de la serie, con 1,1 hijos"*).
     The "2.0→1.06" figures appear in no DANE source. The collapse is genuine but ~35% in TFR, not ~47%.
   - **Argentina's INDEC credibility break does NOT contaminate the fertility signal.** Vital
     statistics are produced by **DEIS (Ministerio de Salud)**, an institution entirely separate
     from INDEC. The 2007–2015 intervention hit prices/poverty/GDP/EPH — not civil-registration births.
     The fertility break is 2015→2016, nine years after the intervention began and *outside* it.

3. **World Bank / UN WPP series materially understate the collapse** and must not be used for the
   collapse tail. WB 2024 TFR vs national 2024: Colombia 1.63 vs 1.1, Costa Rica 1.32 vs 1.12,
   Chile 1.14 vs 1.03, Mexico 1.89 vs ~1.6–1.9. WB is retained only as the long consistent
   historical backbone and for covariates.

4. **Cleanest collapse signals (best ABM candidates):** **Costa Rica** and **Chile** (full
   national TFR + births series, single statistical office, minor caveats). **Argentina** is
   clean on births (recomputed from DEIS microdata) but lacks a published period TGF after 2021.
   **Colombia** is clean and behavioral but carries a residual (small, downward) migration caveat
   on the *level*. No country is disqualified.

5. **All five countries' headline figures are independently source-verified.** Colombia (DANE PDF) and the
   Argentina denominator (INDEC .xls) were verified by direct extraction; Chile, Costa Rica, Mexico, and the
   Argentina TGF were verified against primary PDFs/spreadsheets by a second pass — **zero material
   discrepancies**. Two footnotes: Chile 2023 births = 174,067 is the *revised* (Mar-2025) figure (earlier
   vintage 171,992); Costa Rica 2023 TGF 1.22 (authoritative Cuadro 2.2) vs 1.19 (press release) — both real.

6. **Mexico (comparator) is suitable** as the slow-descent foil, with three handling rules:
   use one TFR series at a time (CONAPO-modeled ≈1.89 *or* ENADID-survey 1.60 for 2023 — they
   differ by ~0.3 and must never be spliced); never use registered-births-by-registration-year
   as an occurrence series; treat 2020 as a COVID registry anomaly, not a fertility event.

---

## Cross-check results table (Check 4 — the core forensic test)

Raw birth count vs TFR vs reconstructed women 15–49 (WB 5-yr age shares × WB female total),
over each country's common data window. Machine-readable: `data/STAGE1_crosscheck_check4.csv`.

| Country | Window | Δ TFR | Δ births (count) | Δ women 15–49 | Δ implied GFR | Verdict |
|---|---|---|---|---|---|---|
| Colombia | 2016–2024 | −35.3% | −29.9% | **+11.2%** | −37.0% | Behavioral — denom grew |
| Argentina | 2010–2021 | −34.6% | −29.9% | **+10.7%** | −36.7% | Behavioral — denom grew |
| Chile | 2022–2024 | −17.6% | −18.4% | +0.4% | −18.8% | Behavioral |
| Costa Rica | 2010–2024 | −38.8% | −35.4% | +6.2% | −39.2% | Behavioral — denom grew |
| Mexico | 2014–2019 | −7.4% | −15.1% | +4.5% | −18.7% | Slow decline (see caveat) |

*Note:* full ASFR-based implied-births reconciliation (the strict version of Check 4) is
**deferred to Stage 2**, which requires age-specific fertility rates not yet acquired. The
count-vs-denominator concordance above is the Stage-1 directional test and it is unambiguous.

### Implied TFR reconstruction (Check 4 in TFR units; extends truncated series)

To express Check 4 in TFR units I back-derive an implied TFR from births and the
reconstructed women 15–49, rescaled to the published national TFR in one clean anchor year:
`implied_TFR(t) = TFR(anchor) × [GFR(t)/GFR(anchor)]`, `GFR = births/women15-49×1000`.
This assumes a roughly stable age-pattern of fertility (tempo shifts cause drift), so it is a
**consistency proxy and an extension**, not a replacement. Files: `data/national/{ISO}_tfr_implied.csv`;
dual-panel charts `data/charts/{ISO}_panel.png` (TFR top, births bottom). Results:

- **Colombia / Costa Rica:** implied TFR tracks the published DANE/INEC series closely → Check 4 holds in TFR units.
- **Argentina (key, now pinned to INDEC):** implied TFR matches the official series 2010–2021 (validating
  the method), then **extends it to ≈1.15–1.19 in 2024** — far below WB's flat ~1.50. This is now pinned to
  the **real INDEC female-15–49 denominator** (not WB age shares): anchored at the last official year
  (2021 TGF = 1.558), the extension gives **1.19 on the Censo-2010 projection** (vintage-consistent with the
  official series) and **1.15 on the more recent Censo-2022 base** (which recounted +3.21% more reproductive-age
  women, pulling the rate down). The WB-shares first pass (1.15) sat right on the official line, so the estimate
  is robust. Argentina's true current TFR is ~1.15–1.19; the official period-TGF gap after 2021 is the only
  reason it isn't published. Files: `national/ARG_women1549_indec.csv`, `national/ARG_tfr_implied_indec.csv`,
  chart `charts/ARG_panel_indec.png`.
- **Chile:** implied TFR **fills the 2010–2021 official gap**, reconstructing the full 1.81→1.03 glide that
  INE publishes only as a chart, connecting smoothly to the 2022–24 definitive/provisional points.
- **Mexico (cautionary):** implied TFR from *registered* births is erratic — spikes 2014, **crashes to ~1.5
  in 2020 (COVID registry-closure artifact)** — while CONAPO glides smoothly. This is a visual proof of why
  registered-births-by-registration-year must NOT be used as an occurrence series (the rule in Mexico's section).

### Check 5 — Tempo vs Quantum (ASFR by age; qualitative flag per spec)

ASFR by 5-year age group acquired and verified for Argentina (observed, AEPA), Mexico (ENADID 2014/18/23)
and Chile (2023/24). Files: `data/national/{ISO}_asfr.csv`; decomposition `data/STAGE1_check5_tempo_quantum.csv`.
**Validation:** ASFR×5 reproduces the published TFR almost exactly (ARG 2.38→1.55, MEX 2.21→1.60, CHL 1.16→1.03),
confirming the age detail is consistent with the headline series.

| Country | Window | ASFR decline | Share from ages <30 | Read |
|---|---|---|---|---|
| Mexico | 2014–2023 | −121/1000 | **83.3%** | Tempo-dominant (postponement), with quantum component |
| Argentina | 2010–2021 | −164/1000 | **72.5%** | Tempo-dominant (AEPA's own attribution ≈72%) |
| Chile | 2023–2024 | −25/1000 | 52.4% | Recent single-year drop is ~uniform across ages → quantum-wide |
| Costa Rica | 2003–2023 | (rates n/a) | — | Mean age at first birth 21.3→25.3; under-20 share 20.5%→9.1% → postponement signature |
| Colombia | 2015–2024 | partial vector | young-concentrated | 20–24 −55.6 pts (largest); 40–44 −20.4%, 45+ smallest; DANE: 10–14 & 15–19 largest relative drops → tempo signature |

**Interpretation (flag, not adjustment):** the multi-year declines are concentrated in younger ages — a
**postponement/tempo** signature (the Fischer-Dattani caution applies), but *every* age group fell, so there
is a genuine quantum component. Two things this does NOT undermine: (1) the **raw birth-count collapse**
(Check 4) is tempo-agnostic — postponement still produces real missing births in the period; (2) a
postponement *cascade* is exactly the kind of mechanism the threshold-coupling ABM is meant to generate, so
a large tempo share is consistent with, not fatal to, the paper's thesis. A formal Bongaarts-Feeney
tempo-adjustment is deferred to Stage 2 (per spec, Stage 1 only flags the pattern).

---

## Colombia — DANE

**Series acquired** (`data/national/COL_*.csv`): national TFR (TGF) 2015–2024; registered births
2016–2025; general fertility rate (GFR) 2016–2025. WB backbone 1960–2024.

| Series | Span | 2024 value | Source |
|---|---|---|---|
| TFR (TGF) | 2015–2024 | **1.1** | DANE EEVV Boletín Isem-2025pr (25-sep-2025), Gráfico 7 |
| Births | 2016–2025 | 453,901 (2025: 433,678 prov) | DANE EEVV Boletín IIsem-2025pr (20-mar-2026) |
| GFR | 2016–2025 | 32.6 | DANE IIsem-2025pr, Gráfico 4 (revised vintage) |

- **Check 1 (splicing/methodology):** GFR vintage break — 2018 GFR is 50.6 (Mar-2025 series) vs 51.8
  (Mar-2026 revised series); 2019 moved 49.0→50.0. Publication-calendar change from 2025 (Resolution
  25-oct-2024). DIVIPOLA + cause-of-death recoding from Dec-2024. Rates are *crudas*.
- **Check 2 (provisional):** Per the Mar-2026 bulletin, **2016–2024 are definitivas; only 2025 is preliminar.**
  2024 was revised UP 445,011pr → 453,901 (+2.0%) by late registration — the exact pattern the memo warned of.
- **Check 3 (census level-effect):** Denominator built on **CNPV 2018** via conciliación censal (corrects
  coverage omission). CNPV-2018 revised population *downward* vs pre-census projections → a *smaller*
  denominator → mechanically *raises* TFR. So the observed decline is **conservative** w.r.t. this revision.
- **Check 4 (births vs TFR):** **Behavioral.** Births −29.9% (2016–24) while women 15–49 **+11.2%**.
  Numerator falling against a rising denominator cannot be a denominator artifact.
- **Check 5 (tempo/quantum):** ASFR extracted from DANE Gráfico 6 (`COL_asfr.csv`, partial — grouped bar
  chart, ~24/32 bars cleanly resolved). Decline is **young-concentrated**: 20–24 fell −55.6 pts (largest
  absolute, 94.2→~38.6), while 40–44 fell only −20.4% and 45+ least; DANE states 10–14 and 15–19 show the
  largest *relative* decreases. → **tempo/postponement signature** (with quantum component, all groups fell),
  matching Argentina/Mexico. Full 2024 vector → Stage 2 (DANE anexo).
- **Migration confound:** Venezuelan stock ≈2.89M (Jun-2023) → 2.85M (Feb-2024) — **flat-to-declining**
  while births fell 13.7% in 2024 alone. DANE models Venezuelan inflow as transitory (net migration →0
  by 2070). Residual risk: if high-fertility-age Venezuelan women are in the denominator while a share of
  their births is under-registered, measured TFR is biased *down* — a small **level** effect, not the trend driver.

**Bottom line:** **Credible behavioral collapse, magnitude corrected to DANE's 1.7→1.1.** Migration is a
small downward level caveat, not the cause. Manageable, not disqualifying.

---

## Chile — INE / DEIS-MINSAL

**Series acquired** (`data/national/CHL_*.csv`): national TFR 2022–2024 (text-confirmed); births 2010–2024.

| Series | Span | 2024 value | Source |
|---|---|---|---|
| TFR (TGF) | 2022–2024 | **1.03** | INE Boletín EV provisional 2024 (15-may-2025): *"la TGF para 2024 fue de 1,03"* |
| Births | 2010–2024 | 154,441 | INE Anuario EV 2022 Tabla 10 (2010–22); provisional bulletins (2023–24) |

- **Check 1 (methodology break — material):** TGF computed with **corrected births for 1992–2022 but
  OBSERVED (uncorrected) births for 2023–2024.** Corrections historically raise counts, so the
  provisional 1.16/1.03 may be marginally *understated*, slightly **exaggerating** the 2022→24 drop.
  This is a genuine discontinuity at the collapse tail.
- **Check 2 (provisional):** 2023 and 2024 are explicitly *cifras provisionales* ("pueden diferir…").
  2022 and earlier are definitive.
- **Check 3 (census):** Denominators use **Estimaciones y Proyecciones base Censo 2017**. **Censo 2024**
  (de derecho) is **not yet incorporated** → no denominator re-basing for 2023/24 figures yet. Flag for Stage 2.
- **Check 4:** **Behavioral.** Births fell 250,643 (2010) → 154,441 (2024), −38% overall; −18.4% in the
  2022–24 TGF window while women 15–49 essentially flat (+0.4%).
- **Check 5:** ASFR not extracted (INE TGF is chart-only for 2010–21). Deferred.
- **Migration:** Large 2017–2023 wave (foreign pop 1.30M→1.92M, concentrated ages 30–34). Inflates the
  15–49 denominator; if projections lag the inflow, TGF is *overstated* (true collapse even sharper);
  if they capture it, denominator grows faster than immigrant births and depresses TGF. **Denominator-
  sensitivity flag**, direction depends on projection vintage.

**Bottom line:** **Credible behavioral collapse**; 2024 = 1.03 confirmed. Two caveats: provisional
observed-vs-corrected births break at the tail; immigration denominator sensitivity. **Gap: annual TGF
2010–2021 is chart-only in INE sources and was not extracted** — needs the underlying INE table for Stage 2.

---

## Argentina — DEIS / INDEC

**Series acquired** (`data/national/ARG_*.csv`): births 2010–2024 (recomputed from DEIS microdata);
period TGF 2010–2021 (AEPA/INDEC).

| Series | Span | Latest value | Source |
|---|---|---|---|
| Births | 2010–2024 | 413,135 (2024, prov) | DEIS open microdata (summed by year); 2023 = 460,902 matches Síntesis N°10 |
| TFR (TGF) | 2010–2021 | 1.558 (2021) | AEPA 2023 Tabla 1 (DEIS births + INDEC-2013 Censo-2010 denom) |

- **Check 1 — INDEC credibility break (THE headline confound): NOT contaminating.** The 2007–2015
  intervention manipulated **IPC, poverty, GDP, EPH employment** — economic series produced by INDEC.
  **Vital statistics are DEIS (Min. Salud), continuous civil registration, a separate institution**, not
  part of the intervention. No DEIS/AEPA source flags any vital-series break across 2007–2015. The
  fertility trend break is **2015→2016**, on the downside, outside the intervention window.
- **Check 2 (provisional):** 2010–2023 final (2023 in "version_final" Anuario + Síntesis N°10, Jun-2025).
  **2024 provisional** (newest open-data release).
- **Check 3 (census):** Published TGF 2010–2021 uses **Censo-2010 (INDEC-2013) denominators**, NOT yet
  rebased to Censo 2022. The census "1.4 children per woman" is a **cohort children-ever-born** measure —
  **do NOT splice into the period series.**
- **Check 4:** **Behavioral.** Births −29.9% over 2010–2021 (and −46.8% peak-to-latest: 777,012 in 2014 →
  413,135 in 2024) while women 15–49 +10.7%.
- **Check 5:** ASFR not acquired; deferred.

**Gap (important):** **No published national period TGF for 2022–2024.** Only the count series, GFR 38.6
(2023), and the cohort 1.4 exist. The post-2021 TFR tail must be reconstructed (births / age structure)
in Stage 2 or sourced from a future INDEC release.

**Bottom line:** **Collapse credible; INDEC confound resolved as NOT disqualifying.** The signal lives in
clean DEIS administrative births. The missing official post-2021 TGF is now **filled by an INDEC-pinned
reconstruction: 2024 TFR ≈ 1.15–1.19** (Censo-2022 vs Censo-2010 denominator), vs WB's 1.50. Remaining caveat
is only the denominator-vintage break (+3.21% at 2022) and the stable-age-pattern assumption of the proxy.

---

## Costa Rica — INEC

**Series acquired** (`data/national/CRI_*.csv`): national TFR 2010–2024; births 2010–2024.

| Series | Span | 2024 value | Source |
|---|---|---|---|
| TFR (TGF) | 2010–2024 | **1.12** | INEC Panorama Demográfico 2023 Cuadro 2.2 (2010–23); INEC news release (2024) |
| Births | 2010–2024 | 45,821 | INEC Estadísticas Vitales 2024 Cuadro 3.21 |

- **Check 1 (methodology):** Clean single-office series. Minor: 2023 TGF = 1.22 (Cuadro 2.2) vs 1.19 (a news
  release) — a denominator-vintage difference, not a numerator error.
- **Check 2 (provisional):** No provisional flag on 2023/24; CR births are near-complete civil registry,
  effectively final. Only revisable component is the population denominator. (2024 births: Cuadro = 45,821;
  press snippet said 45,825 — use 45,821.)
- **Check 3 (census — material on level):** Denominators are **INEC-CCP julio-2024 projections, re-based on
  Censo 2022.** This causes the 1.22-vs-1.19 wobble: same numerator, different denominator vintage. Trend
  robust; treat any single TGF *level* as ±~0.03.
- **Check 4:** **Behavioral.** Births 70,922 (2010) → 45,821 (2024), −35.4%, while women 15–49 +6.2%.
  TGF decline (1.83→1.12) corroborated by crude birth rate (15.6→8.9).
- **Check 5:** ASFR not extracted; deferred.
- **Migration:** Nicaraguan immigration **raises the numerator** — 19.3% of 2024 births are to foreign-born
  mothers. The collapse is *despite* immigrant childbearing; native-born collapse is even sharper.

**Bottom line:** **Cleanest collapse signal of the set.** Full TFR + births series, single office, behavioral,
migration works against (not for) the collapse. Only caveat is denominator-vintage level sensitivity.

---

## Mexico — CONAPO / INEGI (COMPARATOR, not a collapse case)

**Series acquired** (`data/national/MEX_*.csv`): CONAPO modeled TFR 2010–2024; ENADID survey TGF 2014/18/23;
INEGI registered births 2014–2024.

| Series | Span | Latest | Source |
|---|---|---|---|
| TFR — CONAPO modeled | 2010–2024 | 1.888 (2024, projection) | CONAPO ConDem 1950-2019 + Proy 2020-2070, 5_Indicadores xlsx |
| TFR — ENADID survey | 2014/18/23 | 1.60 (2023) | INEGI ENADID 2023 boletín |
| Births — INEGI registered | 2014–2024 | 1,672,227 (2024, prov) | INEGI ENR 2023/2024 |

- **The "1.55" in the memo is NOT a national figure** — likely WB/UN. National options are CONAPO-modeled
  1.89 (2024) or ENADID-survey 1.60 (2023). They differ ~0.3 and **must never be spliced.**
- **Check 1/4 (methodology):** Two breaks. (a) CONAPO re-based after **Censo 2020** (conciliación demográfica).
  (b) **Registration-lag:** INEGI births are by *año de registro*; only **64.9%** of births *registered* in
  2024 *occurred* in 2024. Recent years undercount true occurrence → the 2023→24 drop **overstates** the real
  decline. Do not treat registered-by-registration-year as an occurrence series.
- **Check 2 (provisional):** 2024 registered births provisional. **2020 is a COVID registry-office anomaly**
  (dip to 1.63M, rebound 1.91M in 2021 = catch-up), NOT a fertility event. CONAPO 2020–2024 are projections.
- **Check 4:** Slow decline. In the clean 2014–2019 window CONAPO TFR −7.4%; births fell more (−15.1%) partly
  due to registration lag. Women 15–49 +4.5%. Consistent with a *gradual* descent, not a collapse.
- **Coupling (diagnostic-relevant):** ENADID partnered share (women 15–49) fell 57.5% (2018) → 53.3% (2023),
  with marriage→cohabitation substitution (casada 34.2→28.5; unión libre 23.3→24.8); "soltera" now modal.

**Bottom line:** **Suitable comparator** for the tipping-point diagnostic — smooth monotone descent,
corroborated across three independent methods, and a *declining* coupling share that makes it a meaningful
threshold-distance test case. Handle with the three rules above.

---

## Cross-country summary

| Country | Collapse credible? | Cleanest evidence | Principal caveat | ABM suitability |
|---|---|---|---|---|
| **Costa Rica** | Yes — behavioral | Full TFR+births, single office | Denominator level ±0.03 (Censo 2022) | **Best** |
| **Chile** | Yes — behavioral | 2024=1.03 confirmed; full births | Observed-vs-corrected births break at tail; **TGF 2010–21 gap** | **Strong** |
| **Colombia** | Yes — behavioral (1.7→1.1) | Births vs rising denom | Small downward migration level bias | **Strong** |
| **Argentina** | Yes — behavioral | DEIS microdata births | **No period TGF post-2021**; INDEC denom vintage | Strong on births; TFR tail to reconstruct |
| **Mexico** | N/A — slow decline | 3 corroborating methods | Series must not be spliced; registration lag; COVID-2020 | **Comparator** |

**Identification-discipline status:** Covariate series (education, agriculture share, urbanization, female
LFP — `data/worldbank/`) were acquired as **strictly separate data products** from the TFR series, from
World Bank WDI, and have not been touched to fit any TFR. Coupling/partnership series (the priority ABM
state variable) are **largely NOT FOUND at annual resolution** — only endpoints (Mexico 2018/2023; Chile,
Costa Rica census/survey endpoints). **This is the most important Stage-2 acquisition gap** (see below).

---

## Open gaps carried to the gate / Stage 2

1. **Coupling time-path (PRIORITY, per Nina):** endpoint values are now encoded (`{ISO}_coupling.csv`:
   Mexico 2018/2023 partnered 15–49; Costa Rica cohabitation 1990/2019; Chile CASEN; Argentina CABA-only) —
   but the *annual* share-partnered women 20–39 series the ABM needs exists for no country at that resolution.
   Requires household-survey microdata (GEIH/ENDS, EPH, CASEN, ENAHO, ENADID) — manual Stage-2 acquisition.
2. **ASFR / Check 5:** DONE (flag) for all five — Argentina, Mexico, Chile (full ASFR), Costa Rica
   (qualitative), Colombia (partial vector + DANE prose). Full Bongaarts-Feeney tempo-adjustment and the
   complete Colombia 2024 ASFR vector (DANE anexo) deferred to Stage 2.
3. **Chile TGF 2010–2021:** chart-only in INE; obtain the underlying table (implied series fills it meanwhile).
4. **Argentina period TGF 2022–2024:** confirmed not published by INDEC; reconstructed via the INDEC-pinned
   implied series (2024 ≈ 1.15–1.19). A future official INDEC release would supersede.
5. **Census-2022 re-based denominators** (Argentina, Costa Rica, Chile-2024) not yet folded into fertility rates.
6. **Colombia full 2024 ASFR vector + general-population coupling** (vs the mothers'-union-status proxies found) — Stage 2.

---

## Hard gate — questions for Anne & Nina

- **Colombia migration:** the residual confound is a *small downward level* bias, not the trend driver
  (births fall against a rising denominator; Venezuelan stock flat). **Manageable** — confirm?
- **Argentina INDEC:** confound **resolved as not disqualifying** (DEIS ≠ INDEC; break outside window). Confirm?
- **Covariate/TFR separation:** maintained. Confirm acceptable.
- **Memo number correction:** Colombia 1.7→1.1 (not 2.0→1.06) and Mexico ~1.6–1.9 (not 1.55) — confirm these
  replace the spec's figures in all downstream stages.

**STOP — no ABM specification until this memo is reviewed.**

*Stage 1 forensic memo v1.0, 2026-06-17. Companion: STAGE1_provenance.md, STAGE1_crosscheck_check4.csv,
data/charts/*.png, data/worldbank/, data/national/.*
