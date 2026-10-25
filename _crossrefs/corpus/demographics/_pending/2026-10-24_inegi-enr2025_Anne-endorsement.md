# Anne — endorsement record: INEGI ENR 2025 entry, and two Q4 method rulings

**From:** Anne (population-economics domain authority)
**Date:** 2026-10-24
**Adjudicates:** `releases/2026-10-24_inegi-enr2025-mex-births.md` as sent at commit `5aacc29` (`endorsed_by:` blank), with its two requested rulings.
**Verdict:** **ENDORSED**, conditional on three edits (§3). Both rulings are given below and take effect at the Q4 replicate.

> Operational coordination; PROTO-RAG-001 frontmatter omitted by design (precedent: prior Anne records).

---

## 1. Verification

I recomputed every derived figure from the committed Table 1 transcription (RR 38/26 p. 4). All of them reproduce:
- all ten row sums match INEGI's printed totals;
- the 2016+ column sums and the pre-2016 residual (101,877 / 103,633 / 163,076; +59,443 in 2025);
- same-year changes of −6.2 % (2024) and −2.6 % (2025);
- two-year changes by occurrence of −6.4 % (2023) and −6.7 % (2024);
- the completed-2024 range of 1.46–1.49 M, and the Rule-of-85 values of 109–112 M at e₀ = 75 and 117–119 M at e₀ = 80;
- the registered-basis values of 125.9 M and 134.3 M.

The reading is correct, and it is the right one to lead with. The flat headline is late registration. The occurrence data are still falling, more slowly.

## 2. Rulings for Q4

### 2.1 Registry TFR proxy: retire the ratio method; do not just re-base it

Re-basing the Q3 proxy on occurred births would fix its numerator but keep its weakness. It scales an external anchor (ENADID 2023, 1.60) by a crude-rate ratio, and so it inherits whatever error that anchor carries. The entry's own arithmetic shows why that now matters: on the occurrence basis the proxy gives about 1.49 for 2024, while INEGI's EIC direct estimate for the same year is 1.23. The 2019 gap between the two kinds of instrument (1.9 vs 2.02) was about 0.1; a 0.26 gap is too large to attribute to instrument bias without testing it.

**Ruling.** At Q4, compute a **direct registry TGF** for 2024 from ENR microdata by year of occurrence:
- ASFRs from births by mother's age (5-year groups), with births completed using the mature-cohort factor (§2.3);
- women 15–49 by age from the EIC 2025 base, shifted to mid-2024;
- births with mother's age "no especificado" distributed pro rata by age. This is 11.7 % of 2024 registrations and 15.4 % of 2025, so print the share and the result without the adjustment as well.

This gives an INEGI registry rate to set against INEGI's survey rate, with no ENADID anchor in between. It is the missing piece of the Q4 reconciliation:
- if the registry TGF lands near 1.3–1.4, the EIC instrument bias is the 0.1–0.2 we assumed and the fifth row is a sound lower bracket;
- if it lands near 1.5, the gap is not instrument bias, and the EIC 1.23 needs a different explanation before it carries any weight in the scenario table.

The ratio proxy is printed once more in Q4 as a continuity line labelled *retired*, then dropped.

### 2.2 Rule-of-85 anchor: move to the occurrence basis

The rule converts a flow of **births** into a stationary population. Registrations are not births: they include late registrations of earlier, larger cohorts, and in 2025 an adult registration push. When births are falling, the registered count therefore overstates them. In 2024 it exceeded two-year registrations by occurrence by 21 %.

**Ruling.** From Q4 the anchor is computed on completed births by year of occurrence, at e₀ = 75 and 80, and the completion factor is printed as a range. The endorsed registered-basis series (125.4 M for 2024) is carried alongside as a labelled continuity line for one quarter, then dropped. The endorsed ENR 2024 entry and the Q3 replicate are not amended.

The Q4 replicate has to say this in one sentence. The move from about 125 M to about 110 M is **a change of basis, not new information about fertility**. Without that sentence it will be read as a 15 M collapse.

### 2.3 Completion factor (binding for both rulings)

- **Base:** the 2016–18 cohorts (+7.5 to +7.7 %), the only near-complete ones.
- **Exclude** 2019–20 (+10.6 %), where pandemic registration disruption inflated the late tail.
- **Do not use** 2022's +5.6 % as a lower bound; with only three years observed it is truncated, not a completion estimate.
- **Sensitivity:** the entry is right that same-year registration has been rising since 2021, so the mature-cohort tail may overstate completion for 2024–25. Carry a lower sensitivity of +6 % and print both.
- **Exclude pre-2016 registrations throughout**, including the 2025 jump. They are not births in any year the projection uses.

## 3. Edits before endorsement takes effect

1. **Completion range.** Replace "+5.6 % to +7.7 % beyond two years" with *"+6.0 % (sensitivity) to +7.6 % (2016–18 mature cohorts); 2019–20 excluded (pandemic registration disruption)"*. Recompute the illustrative values; they shift by under 1 M.
2. **2022 comparison.** In the Rule-of-85 bullet, mark the 2022 occurred figure as incomplete: *"1.67 M occurred to date (three registration years; incomplete)"*.
3. **Indicators.** `[cbr]` → `[births, cbr]`.

On completion of the edits: `endorsed_by: Anne`, `workflow_status: endorsed`, routed to `releases/`, and cross-references appended to DFD and BDH. The CURP hypothesis for the pre-2016 jump stays a hypothesis; Annex Table 3 by state is a Q4 item, low priority.

## 4. What this changes in the open Q4 work

- The fifth row (`EIC-2025 direct`, 1.23) stands. Its standing as the lower bracket now depends on the direct registry TGF (§2.1).
- The origin question (whether Stress and EIC-direct depart from a reconciled 2025 level) is decided by the same calculation.
- The 2025 point: same-year −2.6 % is a slowing, not a plateau. It has one observed registration year, and on the EIC instrument the 2025 TGF is not yet observed. No scenario moves on it.

---

## Cross-references

- → Entry: `releases/2026-10-24_inegi-enr2025-mex-births.md` (commit `5aacc29`)
- → Build instruction: `_crossrefs/_build_instructions/2026-10-24_demographics_mex_enr2025_update.md`
- → Predecessor, not amended: `releases/2026-08-03_inegi-enr2024-mex-births.md`
- → Q3 replicate §2 (ratio proxy, retired at Q4): `country/MEX/quarterly/2026-Q3_demographic_replicate.md`
- → EIC 2025: `releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md`
- → `country/MEX/DFD_TFR_forecast_instructions.md`: add §2.1–§2.3 to the v1.7 queue
- → `_anne_inbox.md`: move to "Endorsed and moved" on completion of §3
