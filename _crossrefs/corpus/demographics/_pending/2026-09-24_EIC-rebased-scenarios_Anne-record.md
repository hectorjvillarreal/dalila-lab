# Anne — record: EIC-2025 re-based scenario graphs (`mex_scenarios_eic2025.md`), skeleton assumptions, Benzell correction

**From:** Anne (population-economics domain authority)
**Date:** 2026-09-24
**Adjudicates:** `country/MEX/mex_scenarios_eic2025.md` (+ `.py`, 4 PNG, results CSV) — three questions posed; Benzell 3.1 premise correction; outstanding files.
**Status of the artifact:** working graphs, **not endorsed as a citable artifact** (not a replicate; nothing endorsed amended — correct). The *decisions* below carry into the Q4 replicate; the graphs do not.

> Operational coordination; PROTO-RAG-001 frontmatter omitted by design (precedent: prior Anne endorsement records).

---

## 1. Question (1) — the EIC base: **finding endorsed; adoption conditional**

**Endorsed as a finding.** Central 2050 = 135.6 M on the EIC-2025 base with the *unchanged* fertility path, against 140.4 M on the WPP-2023 base, is a pure base effect: EIC shows ~3.4 M fewer 0–14 (21.6% vs 24.9%) and ~2.6 M more 65+ (10.1% vs 8.0%) than WPP-2023 implied. The child deficit propagates mechanically through every subsequent cohort.

**Reporting rule for Q4 (binding):** the replicate reports **base effect** and **path effect** on separate lines, and the 2050 headline is decomposed accordingly. The projection is not to be described as "moved on the EIC survey TGF"; the base moved on the EIC *age structure*, which is a count, not a rate.

**Two gaps, two different confidence levels.**
- *Child gap (~3.4 M):* well explained. Registry births fell ~2.09 M (2019) → 1.672 M (2024, definitive), and WPP overstated Mexican births even before 2019 (F-V&N Table A1 pattern). Adopt.
- *65+ gap (~2.6 M):* **not obviously explained.** Candidates: elderly undercount in the CPV 2020 base carried into WPP; age misstatement in the EIC; a genuine survival gap. **Reconcile against CONAPO's conciliación 65+ count before the base is adopted.** If the gap survives reconciliation, it is a survival-probability finding and goes to Cath (IM-6 interface) as well.

**Adoption ruling:** the EIC-2025 age structure **replaces the WPP-2023 base in the Q4 operational skeleton**, as a documented departure from the WPP-base convention justified by primary observation, subject to three adjustments recorded in the replicate: (i) add the 517,925 complementary population (collective dwellings, foreign service, unhoused) with an age-sex distribution taken from CPV 2020 collective-dwelling shares; (ii) shift the 15 Oct 2025 reference to the projection's mid-year convention; (iii) the 65+ reconciliation above. Until (iii) clears, the EIC base runs as the *primary* and WPP-2023 as the *documented alternative*, both printed.

## 2. Question (2) — the earlier TDR minimum: **direction endorsed; magnitude and IM-6 anchor to Cath**

An older, lower-fertility base brings the total-dependency minimum forward and makes it shallower; net emigration of working-age adults pushes the same way. **Direction is robust.** The Q3 statement (Central TDR_min 42.0 at ~2038, window 2033–2038) is therefore known to be *late*; **the reform window is closer than Q3 stated** — that is the demographic finding for Héctor.

Magnitude (minimum in 2030–2035; interpolated window ≈2027–2037) depends on the 65+ reconciliation and on the migration assumption (§3.3) and is not stable yet. Whether the IM-6 anchor 2033–2038 now sits at the end of the window is Cath's call on the Q4 retabulation. **Not citable until then; agreed with the digest.** Note the interaction with the Q3 §4 wedge: observed TDR 46.40 (WPP side) and the earlier minimum are the same fact seen from level and from timing.

## 3. Question (3) — what enters the operational skeleton

**3.1 EIC base — yes** (§1, conditional on the three adjustments).

**3.2 Mortality improvement, 1%/yr — sensitivity only; not Central until sourced.** A uniform 1%/yr decline in age-specific mortality is a reasonable placeholder but is currently unsourced. Mexico's recent mortality is not a smooth drift: pre-2020 improvement stalled (homicide, diabetes/obesity), 2020–21 carried large excess mortality, 2022–24 recovered. Source options, in order: CONAPO conciliación mortality assumptions; a Lee-Carter drift fitted on INEGI deaths 2000–2024 excluding 2020–21; failing both, keep 1%/yr as sensitivity. **Interface issue for Cath:** IM-6 carries fixed survival probabilities; an improving-mortality demographic skeleton feeding a fixed-survival OLG is inconsistent, and the pension cost effect runs directly through survival. Cath rules on alignment before this becomes Central.

**3.3 Net emigration, −230 k/yr — enters, with a taper and an age-sex profile.** The EIC pace (≈1.3 M out, 0.15 M return, 2020–25) is observed and primary; but migration is the one component whose driver is exogenous (US policy) rather than persistent structure, so the fast-transition logic (observed = central) does not transfer unmodified. Ruling:
- **Central:** −230 k/yr held through 2030, tapering linearly to the 2015–20 net pace by 2040, constant after. (Debb: compute the 2015–20 net pace from CPV 2020 emigration and return counts.)
- **Sensitivity:** no taper (−230 k/yr throughout) — printed alongside.
- **Profile (binding):** apply the EIC age-sex profile of emigrants (70.4% male; 22.5% at 20–24, 19.5% at 25–29, 15.0% at 15–19, 14.1% at 30–34), not a proportional removal. The TDR effect and the marriage-market effect both depend on it.
- **Lower-bound note:** the EIC cannot capture households that emigrated entirely, so −230 k/yr understates the true 2020–25 net outflow.
- **Paper-chat flag:** a male-skewed 20–29 outflow tightens the sex ratio in the marriage market for women 20–29 — a coupling-channel input to the union-composition mechanism, distinct from fertility per se. Log; do not model yet.

**3.4 Fifth row `EIC-2025 direct` at 1.23** — correctly carried in the graphs; still **awaiting Héctor's ratification**. The origin question (whether Stress and EIC-direct depart from a reconciled 2025 level rather than 1.5) rides with the Q4 reconciliation, as ruled on 2026-09-23.

**Scenario-set headline for Q4 (provisional, not citable):** Central (EIC base, full assumption set) 131.5 M; EIC-direct 125.2 M; Stress 119.1 M at 2050. The Central-to-EIC-base-only difference (135.6 → 131.5) is the mortality-plus-migration term and must be labelled as such.

## 4. Benzell, Kotlikoff & Ye — correction to my 3.1 of 2026-09-23

My 3.1 argued from the digest's premise that the payroll burden *rises* under WPP 2024 vs 2017; the note and paper report it *falling*. The conclusion — Mexico revised **down**, 165 → 149 M at 2050 — holds because the drafter checked the paper's Table 5 directly, not because of my mechanism argument. **Replace my mechanism sentence with the rule the check actually established: burden direction is not a valid proxy for population-revision direction (it depends on age composition and benefit rules, not on level); read the vintage tables.** Scenario-discipline section RESOLVED as stated; BID2's 1.70 confirmed against WPP 2024 (1.701); Table 6's 1.67 is the outlier. The June-appendix "peak ~2042 at 152 M" is not WPP 2024 — Debb to trace provenance; narrative only until then.

## 5. Outstanding for Anne — files still not received

Requested 2026-09-23; not yet sent:
- reconstructed cornerstone `2026-08-13_fernandez-villaverde-norrick_terra-incognita.md`;
- the nine NBER notes (priority order in the 09-23 record);
- `2026-09-17_tar-candidates.md`.

None can be endorsed from digests. Please attach.

## 6. Outstanding for Héctor

- Ratify the fifth scenario row (`EIC-2025 direct`, 1.23 stable).
- Note for planning: the reform window is closer than Q3 stated (§2), pending Cath's retabulation.

---

## Cross-references

- → `country/MEX/mex_scenarios_eic2025.md` (working; not endorsed as artifact)
- → `releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md` (base source; addendum endorsed 09-23)
- → `country/MEX/quarterly/2026-Q3_demographic_replicate.md` §4 (wedge; window — known late)
- → `country/MEX/DFD_TFR_forecast_instructions.md` v1.5 (v1.6 on Q4 execution: base convention, migration assumption, mortality sensitivity)
- → `2026-09-23_EIC-addendum_stress-glide_NBER-triage_Anne-endorsement.md` §3.1 (corrected here, §4)
- → `cath_stress_floor_revision_brief.md` — append §2 and §3.2 for Cath
- → `_anne_inbox.md` — move `mex_scenarios_eic2025.md` to "Endorsed and moved" as *decisions endorsed / artifact working*; Benzell line updated

---

## Execution note (Claude, 2026-09-23; committed with this record)

- **§1 — recorded, not yet adopted.** The reporting rule (base effect / path effect on
  separate lines; count, not rate) and the three base adjustments are queued for v1.6 in the
  instructions' version trailer and written into the graphs note. **65+ reconciliation not
  done:** CONAPO's projection server (`conapo.segob.gob.mx/work/models/CONAPO/pry23/`) did not
  answer on 2026-09-23; the datos.gob.mx mirror is the fallback. It stays the Q4 gate exactly as
  ruled; the EIC base runs as primary with WPP-2023 as documented alternative only once it clears.
- **§2 — routed to Cath** as `cath_stress_floor_revision_brief.md` §8 (direction endorsed;
  magnitude and IM-6 anchor position hers; not citable).
- **§3.2 — routed to Cath** in the same §8 (IM-6 fixed-survival alignment). Mortality stays
  sensitivity-only in the queue.
- **§3.3 — taper target (Debb):** CPV 2020 (cuestionario ampliado, INEGI comunicado 378/21):
  **802,807** international emigrants March 2015–March 2020 (537,149 men, 265,658 women), i.e.
  ≈161 k/yr **gross**. The national return share is not in the press release; the 32.5 % that
  surfaces in searches is Ciudad de México's own *Principales resultados* volume, not national.
  Net 2015–20 pace therefore bounded ≈107–161 k/yr; the exact figure needs the national
  ampliado tabulado (INEGI's tabulado links are JavaScript-rendered; direct URLs soft-404).
  Same construct caveat as the EIC: households that emigrated entirely are not captured.
  Profile and taper are v1.6 items; the graphs were **not re-run** (decisions carry, graphs do
  not). Marriage-market flag logged: `watch_items/2026-09-24_emigration-sex-ratio-marriage-market.md`
  (opened_by Anne + Claude Code, endorsed_by Anne per the record; no separate build instruction,
  precedent 2026-09-23).
- **§3.4 —** unchanged; Héctor's ratification still open.
- **§4 — applied.** The mechanism sentence in the 2026-09-23 record §3.1 is struck and replaced
  by the rule, marked with this record's name; the Benzell note carries the rule as a standing
  ruling. **Provenance traced:** the "peak ~2042 at 152 M, 150.6 M by 2050" claim originates in
  the BID2 build instruction `Missions/Funded/BID2/draft_june/CC_instrucciones_Draft-June_v2.md`
  (commit a5b3e24), asserted there as WPP 2024 "accessed 2026-05-24" with no table reference,
  and copied verbatim into every Draft-June `.tex`. No UN medium series matches it. Narrative
  only; `demographics_2050.jl` header already corrected 2026-09-23.
- **§5 — delivery bundle built** (cornerstone, nine notes in Anne's priority order, synthesis,
  TAR candidates; 157 KB, one file) for Héctor to paste into Anne's session. It is not
  committed (it would duplicate corpus text); regenerate with the concatenation listed in the
  session summary.
- **Inbox:** graphs line moved to "Endorsed and moved" as *decisions endorsed / artifact
  working*; Benzell line updated; this record added under Pending for the two outstanding
  items (files to Anne; fifth-row ratification).
- **Instructions:** v1.5 unchanged operationally; a "Queued for v1.6" block added to the version
  trailer listing items (1)–(6) of this record.
- **Not done, by design:** no v1.6 issued; graphs not re-run; nothing endorsed amended.
- **§6 — fifth row RATIFIED by Héctor 2026-09-23** (same session, after this note was first
  written). Executed as: instructions v1.5 → **v1.6** (five-row structure; `EIC-2025 direct`
  1.23 stable from 2025, unreconciled survey direct estimate; reference values deliberately
  left to Q4 execution on the Q4 base; the queued Q4 block renumbered to v1.7); ratification
  addendum on the 2026-09-22 entry; graphs note and inbox updated. **Back to Anne:** the
  specification is yours to confirm as carried (1.23 stable from 2025) or to vary at the Q4
  reconciliation (origin question). Second outstanding item for Héctor (§6) closed;
  the reform-window planning note stands pending Cath.
