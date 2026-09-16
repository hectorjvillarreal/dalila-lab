# Anne — endorsement record: Fernández-Villaverde LAC deck entry and anchor brief

**Adjudicates:**
- `_pending/2026-09-15_fernandez-villaverde-slides-latam.md` (entry)
- `_pending/anne_slides_latam_anchor_brief.md` (brief, §§1–3 decisions; §4 for information)

**From:** Anne (population-economics domain authority)
**Date:** 2026-09-15
**Verdict:** **Conditional endorsement.** Endorsement takes effect when the precondition in §0 is resolved and the conformance edits in §6 are applied. Executor: Debb / Claude Code. Nothing in this record updates a projection, a scenario definition, or a fiscal-window value (Héctor's ruling, respected throughout).

> Operational coordination, not a corpus artifact; PROTO-RAG-001 frontmatter omitted by design, per the `2026-07-11_UNFPA-note_Anne-endorsement.md` precedent.

---

## 0. Precondition — corpus-state discrepancy (resolve first)

The entry treats `2026-06-20_fernandez-villaverde-demographic-future.md` (April deck) as the standing cornerstone and documents as new the AR(1) mean-reversion mechanism, the 37-country 2024 out-of-sample test, the Japan/US growth-accounting counterfactual, the Pareto-tail cohort argument, and the political-economy-of-aging section.

All of that material is the substance of **`2026-08-13_fernandez-villaverde-norrick_terra-incognita.md`** — Fernández-Villaverde & Norrick (2026), *Annual Review of Economics*, DOI 10.1146/annurev-economics-081026-024323 — which I endorsed `ready`, filed `source_reliability: primary`, marked `cornerstone: true`, and which **superseded the April deck** (deck retained in `_build_instructions/` as provenance). That entry does not appear in the inbox's endorsed list and is absent from this entry's cross-references.

**Debb to determine which of two things happened:** (a) the 13 August entry was never committed to Dalila, or (b) it exists and Claude Code drafted from a stale tree. If (a), commit it first — it is the cornerstone of record and this entry's chain depends on it. If (b), the build instruction for this entry should record the omission.

**Same check for `2026-09-15_lac-registry-tfr_stress-anchor.md`** (Anne, this morning, on the slide-8 image alone). I **withdraw it as a standalone entry** — one deck, one entry. Its content is absorbed into §4 below and into the conformance edits. If it was committed, retire it to `_build_instructions/` with a pointer to this record.

---

## 1. Ruling — re-anchor trigger (brief §1): **confirmed, does not fire**

Concur on both legs, and add a third that strengthens the reading:

3. **The 1.51 is not a registry figure.** F-V&N (2026) footnote 3: only ~72% of Mexican births are registered in the year they occur; the 2025 value **extrapolates** births registered within 2025 to an expected final tally. It is a secondary *extrapolation*, one step further from an INEGI publication than the brief allows. This also explains the recorded tension with Q3's registry-implied ≈1.46 (2024): the two are not on comparable bases, and the deck's figure is the weaker of the two.

On the brief's alternative question — whether a credible secondary reading at 1.51 is itself grounds to re-examine Central ahead of INEGI — **no.** The pre-committed frame keys on a published TGF precisely so that Central is not chased around point estimates. It stands. Note for the record that Q3's own registry-implied 1.46 already sits inside the [1.45, 1.50] re-pin band; if INEGI publishes in that neighbourhood, Central re-pins at the published value with no further deliberation. Q4 follow-ups 5 and 7 are the right vehicles.

**Required addition to the entry** (§6, edit 4): the 72% registration-lag caveat, attached to the Mexico row and to the recorded tension.

---

## 2. Ruling — BRA pin (brief §2): **option (b)**

`scenario_anchors.md` stays at the five DFD priority countries. Brazil is required by the CAF deliverable, not by DFD scope; adding rows for deliverable convenience blurs the corpus/deliverable boundary (and the CAF product is CAF IP). The CAF script cites BRA in-note, vintage updated to whatever **IBGE primary** supports; the deck's 1.52/2025 is corroboration only. Whether the row moves from 1.50/2023 in P4 is a P4 question (Beth / Héctor), not a corpus one; P3's freeze is unaffected.

**Closing the May open call:** if a sixth row is ever added, it should be **Argentina**, on DFD grounds — the collapse paper needs it as the third cohabitation regime for `w` identification, and its acquisition (census 2010/2022 union status + DEIS registrations) is already on Debb's list. Pin to INDEC/DEIS primary when that lands; the deck's 1.23/2024 corroborates. Not opened now.

---

## 3. Ruling — routing (brief §3): **`observations/`, `tier: working_note`**

Not a second cornerstone. Cornerstone status transferred from the April deck to the *Terra Incognita* paper on 13 August; a LAC-specific presentation of the same material, `secondary`, with one genuinely new asset (the registry table and the regional rail), is a multi-country working note and follows the routing table.

**Source artifact:** `Slides_Latam.pdf` should not sit at the corpus root. Move to `_crossrefs/corpus/demographics/sources/FV_2026-09-15_LAC-population-history.pdf` and update the entry's `doi:` local-copy line. (The April deck should already be in `_build_instructions/` per the August supersession; verify.)

---

## 4. Anchor-file observations the entry must carry (the substantive miss)

The entry's slide-8 table contains values that bear on three of the five anchor rows. The entry records none of them beyond BRA. **These are facts of record and scheduled decisions — not projection updates.**

| Row | `scenario_anchors.md` | Deck (registry) | Implication |
|---|---|---|---|
| CHL | 1.03 | **0.99 / 2025** | **Stress-column empirical floor no longer holds.** Chile fell 1.54 → 0.99 over 2018–2025. Decision escalated to Héctor (below). |
| COL | 1.10 | 1.01 / 2025 | Full tenth lower; DANE primary needed for re-pin. |
| CRI | 1.12 | 1.12 / 2025 | Same value two vintages — **plateau hypothesis**, verify against INEC before reading anything into it. Deck slide 6 gives CR 2025 births **45,384** (long-run 3.86 M vs 5.2 M current) — a checkable INEC figure. |
| PAN | 1.80 | 1.79 / 2024 | Within noise. |
| MEX | 1.60 / 2023 | 1.51 / 2025 (extrapolated) | Trigger non-fire, §1. |

**Stress-floor decision — for Héctor.** The Stress path (TFR → 1.0 by 2030) was anchored to Chile 1.03 as the empirical floor. Two options: (a) re-anchor to ~0.9; (b) state the floor as unidentified — the *Terra Incognita* position — and carry 0.9 as a working stress value. **Anne recommends (b).** Do not anchor to Puerto Rico 0.87 (US-linked, emigration-driven, not comparable). Once decided, the revised stress dependency-ratio trajectory routes to Cath. Scheduled, not executed here.

**Q4 item — anchor vintage-refresh pass.** All five rows against primaries (INEGI, INEC, DANE, INE Chile, INEC Panamá), the deck as corroboration. Source-of-record maintenance; folds naturally into the `calibration_flags.md` cleanup Héctor already assigned to Q4.

---

## 5. Watch items

- **Goldin (2026) gender mismatch — OPEN as `research_watch_item`.** Two independent grounds: (i) the paradoxical-reversal implication bears on the Stress floor (brief §4); (ii) it is the closest rival mechanism to the collapse paper's union-composition channel and was already the priority acquisition in the 13 August entry. Tie the watch item to the §4 stress-floor decision and to the paper chat's positioning task.
- **Costa Rica plateau — watch, not evidence.** If it survives INEC verification, it is potentially discriminating for the compositional-vs-cascade question (cohort-replacement predicts a plateau once low-marriage cohorts fill the 20–29 band; a cascade with reflexive feedback predicts continued momentum). One vintage is noise. Action: INEC 2025 annual TFR + 2025 ENAHO wave.
- **Mexico out-of-sample test — endorse as Q4 item.** The entry's observation that Mexico is absent from the slide-16 table is correct and useful; INEGI definitive 2024 births (1,672,227) against the July-2024 WPP projection for 2024 is checkable and would put our own country inside the deck's strongest exhibit.

---

## 6. Required conformance edits (Debb / Claude Code)

1. **Chain.** `supersedes:` → "(none — extends `2026-08-13_fernandez-villaverde-norrick_terra-incognita.md`)"; replace the predecessor cross-reference accordingly; drop "sharper than in the April deck" framing.
2. **Condense §§2, 4, 5, 6** to pointers into the 13 August entry, retaining only what the LAC deck adds (the Colombia 2023 registry-vs-UNPD exhibit is fine to keep as the deck's own example). The entry's substance is §1 (registry table + speed claims + the "only four above replacement" statement) and §3 (regional Rule-of-85 rail, ECLAC 730 M rejection). Debb has latitude on how far to condense.
3. **Add the §4 anchor-observation table** (or equivalent prose) under "Anchor-file observation," extending the BRA note to CHL, COL, CRI; state explicitly that no projection moves and that the stress-floor decision is escalated.
4. **Mexico row:** add the 72% registration-lag / extrapolation caveat; attach it to the recorded tension paragraph.
5. **Correct the Goldin watch-item text** from "currently anchored to Chile 1.03" to reflect §4; mark the watch item as opened.
6. **Source-quality section:** the discipline flag ("trace to primaries before citation inside IM-6") now applies only to the LAC-specific material — everything duplicated from *Terra Incognita* is already primary-sourced there.
7. **Routing:** file to `observations/`; move `Slides_Latam.pdf` to `sources/`; append DFD + BDH + Aurora cross-refs on execution.
8. **Frontmatter:** `endorsed_by: Anne`; `workflow_status: endorsed` on completion of 1–7; `data_vintage` note may keep "2026" but should say registry vintages 2022–2025, CR births 2025.

---

## 7. What is not changed (for the record)

Scenario definitions; the 2050 population implications (140.4 / 143.2 / 128.9 M); Central TDR_min 42.0 at ~2038 and the 2033–2038 grid window; the Q3 window-timing caveat; the BID2 `demographics_2050.jl` WPP-medium hard-code (concur with the brief: an acknowledging sentence, not a recalibration — optimistic demography makes the aging experiment conservative); WPP 2024 as the standing UN reference (discriminator ruling REPORT-not-REVISION: concur). `DFD_TFR_forecast_instructions.md` stays at v1.4.

---

## Cross-references

- → Entry adjudicated: `_crossrefs/corpus/demographics/_pending/2026-09-15_fernandez-villaverde-slides-latam.md`
- → Brief adjudicated: `_crossrefs/corpus/demographics/_pending/anne_slides_latam_anchor_brief.md`
- → Cornerstone of record (verify presence): `_crossrefs/corpus/demographics/2026-08-13_fernandez-villaverde-norrick_terra-incognita.md`
- → Withdrawn standalone (absorbed here): `2026-09-15_lac-registry-tfr_stress-anchor.md`
- → Anchor file: `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Trigger of record: `.../country/MEX/quarterly/2026-Q3_demographic_replicate.md` §2, §7
- → Paper chat briefing (Goldin positioning, ARG acquisition): `2026-06-20_fertility-collapse-paper_anne-briefing.md`
- → Inbox: `_crossrefs/corpus/demographics/_pending/_anne_inbox.md` — move both items to "Endorsed and moved" on execution, with a pointer to this record
