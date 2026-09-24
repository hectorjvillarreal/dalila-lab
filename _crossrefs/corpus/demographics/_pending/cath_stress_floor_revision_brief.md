# Cath — revised Stress dependency-ratio trajectory (stress-floor ruling)

**To:** Cath (public finance and modeling; fiscal transmission authority)
**From:** Claude Code, on Héctor's ruling
**Date opened:** 2026-09-15
**Routing basis:** Anne's endorsement record of 2026-09-15 §4 — *"Once decided,
the revised stress dependency-ratio trajectory routes to Cath."* The decision
has been made; this is that routing.
**Governing instructions:** `country/MEX/DFD_TFR_forecast_instructions.md` (now v1.5)

> Operational coordination, not a corpus artifact. PROTO-RAG-001 frontmatter
> omitted by design, matching the `anne_scenario_anchors_brief.md` precedent.

---

## 1. The ruling

The Stress column was anchored to **Chile 1.03 (2024)** as the observed LAC
floor. That anchor has been overtaken — the September 2026 registry table puts
Chile at **0.99 (2025)**, down from 1.54 in 2018, while WPP projects a recovery
to 1.12 by 2028 against that fall.

Anne escalated two options: (a) re-anchor to ~0.9; (b) declare the floor
**unidentified** and carry 0.9 as a working value. **Héctor ruled (b)**, Anne's
recommendation. Puerto Rico 0.87 was explicitly ruled out as a substitute
anchor — US-linked, emigration-driven, not comparable.

The distinction matters for how you report it downstream: 0.9 is **not** a
claim about where LAC fertility bottoms out. It is a working value chosen so
the stress column stops being a moving function of whichever registry printed
most recently.

## 2. The revised trajectory

TFR path, −0.10/yr glide unchanged, running one year further:

> 1.60 (2024) → 1.50 → 1.40 → 1.30 → 1.20 → 1.10 (2029) → 1.00 (2030) →
> **0.90 from 2031**, stable to 2050.

**The stress and prior-stress paths are identical through 2030** and diverge
only afterwards. That is the useful property for your purposes: nothing inside
the fiscal window's approach changes.

## 3. Revised dependency-ratio path (the deliverable)

Recomputed 2026-09-15, same cohort-component machinery — 5-year age groups ×
5-year steps, Mexico-shape ASFR, Coale-Demeny West e₀ ≈ 75 fixed, zero
migration, 2023 base 129.74 M.

| Year | YDR | OADR | **TDR** | TDR (prior, TFR→1.0) | Δ |
|---|---|---|---|---|---|
| 2023 | 37.1 | 11.9 | 49.0 | 49.0 | — |
| 2028 | 30.3 | 13.8 | 44.1 | 44.1 | — |
| 2033 | 23.0 | 16.1 | 39.1 | 39.4 | −0.3 |
| 2038 | 16.9 | 18.5 | **35.5** ← min | 36.3 | −0.8 |
| 2043 | 14.8 | 21.5 | 36.3 | 37.7 | −1.4 |
| 2048 | 14.9 | 24.9 | 39.8 | 41.4 | −1.6 |
| 2050 | 14.9 | 26.4 | 41.4 | 42.8 | −1.4 |

**Total population 2050: 126.85 M** (prior 128.86 M). Gap to the optimistic
approximation 17.7 M (12.3%); gap to UN WPP 2024 medium's actual 148.95 M is
**22.10 M (14.8%)**.

## 4. Fiscal window — level moves, timing does not

| | v1.4 (TFR→1.0) | **v1.5 (TFR→0.9)** |
|---|---|---|
| Year of TDR min | ~2038 | ~2038 |
| TDR at min | 36.3 | **35.5** |
| Window, grid convention | 2038–2043 (≈5 yr) | **2038–2043 (≈5 yr)** |
| Window, interpolated | ~2035–2044 (~9 yr) | **~2035–2045 (~9.5 yr)** |

The stress window neither moves nor lengthens materially. Only the level of the
minimum falls, by 0.8 points. Per your v1.4 endorsement condition, both
conventions are stated and any downstream citation must say which it uses.

## 5. The composition point, which is the part worth your attention

The stress column's 2050 TDR (41.4) is *lower* than every other scenario's —
and that is arithmetically misleading. Beneath it:

- **OADR 26.4 — the highest of any scenario** (optimistic: 24.7). The 65+
  population in 2050 is already alive today; fertility cannot touch it.
- **YDR 14.9 — barely over half the optimistic 25.9.** The total only looks
  favourable because the youth numerator has collapsed.

So the stress scenario shows a *better* total dependency ratio alongside a
*worse* old-age ratio. For pension contribution rates and health financing —
which load on the old-age side — the stress column is unambiguously worse than
its headline TDR suggests. I have added a note to v1.5 §4 making this explicit,
because the total is the number most likely to be quoted.

## 6. What this does and does not change

**Does not change.** Central, Optimistic and Tempo-corrected columns — all
untouched. The Central fiscal window (TDR_min 42.0 at ~2038, grid 2033–2038)
and the IM-6 anchor are unaffected. The Q3 window-timing caveat still applies
wherever Central fiscal-space numbers are cited.

**Does change.** The Stress columns of the **2026-Q2 and 2026-Q3 replicates are
superseded** and must not be quoted. Both are endorsed artifacts, so they have
been deliberately left unamended (PROTO-RAG-001 standing principle 5); v1.5
carries the supersession notice instead.

**Needs your call.** Whether any IM-6 stress-side calibration currently keys to
the old 36.3 / 128.9 M figures, and whether the revised path warrants a rerun
on your side or simply a reference update.

## 7. One specification choice flagged

The ruling fixed the floor's value and epistemic status but not the glide. I
extended the existing −0.10/yr glide by one year (floor at 2031) rather than
steepening it to hold the 2030 arrival date, on the grounds that it changes one
constant rather than the scenario's character. Anne owns scenario structure and
should confirm. If she prefers a 2030 arrival, the numbers above shift slightly
and I will rerun.

**Closed 2026-09-23.** Anne had already confirmed this in
`2026-09-23_EIC-addendum_stress-glide_NBER-triage_Anne-endorsement.md` §2; the closure is recorded in
`2026-09-23_nota-EIC2025-v0.1_Anne-Cath-review.md` §6.

## Cross-references

- → Governing instructions (v1.5, §2 scenario table and §4 fiscal window): `_crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md`
- → Ruling of record (§4): `_crossrefs/corpus/demographics/_pending/2026-09-15_FV-LAC-deck_Anne-endorsement.md`
- → Evidence that retired the 1.03 anchor: `_crossrefs/corpus/demographics/observations/2026-09-15_fernandez-villaverde-slides-latam.md` §3
- → Chile 1.54 (2018) → 1.17 (2023) and the projected WPP recovery: `_crossrefs/corpus/demographics/2026-08-13_fernandez-villaverde-norrick_terra-incognita.md` §8 (Table A3)
- → Superseded Stress columns (endorsed; left unamended): `quarterly/2026-Q2_demographic_replicate.md` §5, `quarterly/2026-Q3_demographic_replicate.md` §5
- → Recomputation scripts: `country/MEX/mex_population_tfr_decline.py`, `country/MEX/mex_dependency_ratio_decline.py`
- → Related watch item (whether the floor exists at all): `_crossrefs/corpus/demographics/watch_items/2026-09-15_goldin-gender-mismatch-stress-floor.md`

---

## 8. Additions from Anne's EIC-graphs record of 2026-09-23 (appended by Claude Code, 2026-09-23)

Anne's record on the EIC-rebased scenario graphs
(`_pending/2026-09-23_EIC-rebased-scenarios_Anne-record.md`) routes two items
to you. Both are **not citable** until your Q4 retabulation; the graphs behind
them (`country/MEX/mex_scenarios_eic2025.md`) are working products, not
endorsed artifacts.

### 8.1 The TDR minimum comes earlier than Q3 stated (record §2)

On the EIC-2025 age structure (3.4 M fewer 0–14 and 2.6 M more 65+ than the
WPP-2023 base implied), the Central total-dependency minimum moves forward to
2030–2035 (interpolated window ≈2027–2037) and becomes shallower. Net emigration
of working-age adults pushes the same way. **Anne endorses the direction as
robust**: the Q3 statement (Central TDR_min 42.0 at ~2038, window 2033–2038) is
known to be *late*, so the reform window is closer than Q3 stated.

What she leaves to you:
- the **magnitude** (it depends on the 65+ reconciliation against CONAPO's
  conciliación and on the migration assumption below) and
- whether the **IM-6 anchor 2033–2038 now sits at the end of the window** rather
  than inside it — your call on the Q4 retabulation.

Note the interaction with the Q3 §4 wedge: observed TDR 46.40 (WPP side) and the
earlier minimum are the same fact seen from level and from timing.

Working values (Central, EIC base, full assumption set): TDR_min 43.8 at 2035,
grid window 2030–2035, TDR 2050 56.7, OADR 2050 32.8, population 2050 131.5 M.
Sensitivity on the old skeleton (fixed mortality, zero migration) on the same
base: TDR_min 42.7 at 2035, population 2050 135.6 M. The 135.6 → 131.5
difference is the mortality-plus-migration term and must be labelled as such.

### 8.2 Mortality improvement vs IM-6 fixed survival (record §3.2)

The graphs carry a uniform 1 %/yr decline in age-specific mortality. Anne rules
it **sensitivity only, not Central until sourced** (source order: CONAPO
conciliación mortality assumptions; a Lee-Carter drift on INEGI deaths
2000–2024 excluding 2020–21; failing both, keep 1 %/yr as sensitivity).

**Interface issue she assigns to you:** IM-6 carries fixed survival
probabilities. An improving-mortality demographic skeleton feeding a
fixed-survival OLG is inconsistent, and the pension cost effect runs directly
through survival. You rule on alignment before improving mortality becomes
Central.

### 8.3 Migration assumption entering the Q4 skeleton (record §3.3, for information)

Central: −230 k/yr net held through 2030, tapering linearly to the 2015–20 net
pace by 2040, constant after; sensitivity: no taper. EIC age-sex profile applied
(70.4 % male; 22.5 % at 20–24, 19.5 % at 25–29, 15.0 % at 15–19, 14.1 % at
30–34). The EIC flow is a lower bound. The taper target from CPV 2020 is in
progress (gross 802,807 emigrants 2015–20 ≈ 161 k/yr; national return share
pending, so net ≈ 107–161 k/yr).

## Cross-references (additions)

- → Anne's record: `_pending/2026-09-23_EIC-rebased-scenarios_Anne-record.md` §2, §3.2, §3.3
- → Working graphs: `country/MEX/mex_scenarios_eic2025.md` (+ `.py`, results CSV)

## 9. Nota EIC 2025 v0.1 — delivered for your review (appended by Claude Code, 2026-09-23)

Build instruction `_crossrefs/_build_instructions/2026-09-23_DFD_nota-EIC2025_build-instruction.md`
§7 item 3: you review Step 3, the page-3 indicators and the window sentence. Files are in `GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/`
(PDF `nota_EIC2025_v0.1.pdf`; numbers in `results/fiscal_indicators.csv`; assumptions and flags in
`_assumptions.md`).

- **Mortality used:** CONAPO 2023 conciliación, age- and sex-specific, 2025–2050 (improving).
  IM-6 still carries fixed survival (§8.2); the PDF says IM-6 was not re-run.
- **TDR minima (annual grid):** Optimista 46.5 (2027), Central 45.2 (2031), INEGI directo 42.6 (2035),
  Estrés 41.0 (2035). Q3 Central was 42.0 at ~2038. The minimum comes earlier *and sits higher*.
- **Ventana:** minimum ± 5 years (v0.1 choice, one constant). Central 2026–2036 against Q3 2033–2038.
  Your timing caveat is printed verbatim.
- **τ table** (ρ = 0.50 from IM-6 `κ_rep`, `ge_model_gender.jl:61` @ 5368693; φ = 0.45 = 1 − informality,
  Integrated_6.tex §data, untracked): Central 16.0 / 22.6 / 36.6 %, INEGI directo 16.0 / 22.6 / 37.8 %
  (2025 / 2035 / 2050). Holding τ at its 2025 level through coverage alone needs φ = 103 % / 106 % in 2050, so the
  PDF says coverage alone does not suffice.
- **g_l:** +0.37 % a.a. 2025–35 in every scenario; 2035–50 −0.45 (Central), −0.66 (INEGI directo);
  15–64 starts falling in 2036 in all four.
- **For your ruling:** F2 (the ventana step on an annual model), F3 (the window is earlier but shallower; the draft
  sentence "se acorta" was dropped), F5 (φ is a share of employed workers but is applied to the 15–64
  population, so τ is on the low side).

## 10. Rulings of 2026-09-23 (appended by Claude Code, 2026-09-23)

Anne and Cath reviewed the nota v0.1 and the open items of this brief. The rulings are in `2026-09-23_nota-EIC2025-v0.1_Anne-Cath-review.md`
§3 and are not restated here. In brief:
- §3.1: the headline is the TDR minimum (year and level) before and after, and any span goes in the Recuadro with its definition.
- §3.2: the OADR is printed beside the TDR, and this is binding.
- §3.3: τ = ρ · OADR / e, and φ is dropped.
- §3.4: the growth arithmetic is endorsed.
- §3.5: IM-6 is rerun once, at Q4.
- §3.6: IM-6 is aligned to the CONAPO improving survival path.

The v0.2 revision is executed under `_crossrefs/_build_instructions/2026-09-23_demographics_commit-endorsements_nota-v0.2.md` Step 5.

## 11. Nota EIC 2025 v0.2 — for your one-pass review (appended by Claude Code, 2026-09-23)

Your §3 rulings are applied in `GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/nota_EIC2025_v0.2.pdf`:
- The headline is the minimum, before and after.
- The span (within 1 point of the minimum) is in Recuadro 2 with its definition, and your timing caveat is verbatim.
- F3 has TDR and OADR panels.
- τ = ρ·OADR/e, with e from ENOE 2026-Q2 microdata (0.6322, 15–64). The coverage parameter is removed everywhere.
- Implication 3 is replaced with your text.

**v0.2 headline (Central / INEGI directo):** 2050 population 135.5 / 128.7 M; TDR minimum 45.0 in 2030 / 42.3 in 2035 (Q3 said 42.0 at ~2038; today 46.4, so it falls only 1.4 points); OADR 2025 → 2050 14.6 → 33.1 / 34.2; 6–14 18.8 → 15.5 M by 2031 (−17.7 %, whatever the fertility path); 15–64 starts falling in 2036 in all four scenarios. **τ = ρ·OADR/e** (ρ 0.50; e 0.63 from ENOE 2026-Q2): Central 11.6 / 16.2 / 26.2 %, INEGI directo 11.6 / 16.2 / 27.1 %, Central with CONAPO 65+ 10.4 / 15.4 / 26.0 % (2025 / 2035 / 2050). **Step 4 reading — AMBIGUOUS, not chosen:** the CPV 2020 aged forward gives 12.51 M aged 65+ on 15 Oct 2025, against 13.23 M in the EIC and ≈11.84 M in CONAPO. The gap splits about in half: CONAPO is 0.67 M below the aged census, and the EIC is 0.73 M (+5.8 %) above it, concentrated at 65–69 (+8.3 %). The EIC part cannot be separated from CONAPO's own mortality. v0.2 is on the EIC base, and the check is at `../country/MEX/eic2025_65plus_check.md`.

The τ path to 2035 is identical in Central and INEGI directo (16.2 %), as you noted. The CONAPO-65+ sensitivity lowers
2025 by 1.2 points and 2050 by 0.2.

## 12. Review of v0.2 (appended by Claude Code, 2026-09-23)

You and Anne endorsed v0.2 subject to four edits; see `2026-09-23_nota-EIC2025-v0.2_Anne-Cath-review.md`. They are applied, and the result is
`GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/nota_EIC2025_v1.0.pdf`:
- **Edit 1:** the 65+ range sentence.
- **Edit 2:** the 6–14 split, 17.5 + 0.2 points.
- **Edit 3:** your benchmark sentence under the τ table.
- **Edit 4:** the public-chart method note.

Per your §3, the pensions paragraph now comes first after the minimum. v1.0 is with Héctor.
