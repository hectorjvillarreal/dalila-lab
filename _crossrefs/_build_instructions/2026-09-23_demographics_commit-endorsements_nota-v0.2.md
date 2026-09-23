---
type: build_instruction
build_type: commit_and_revise
status: queued
project_scope: [DFD, BDH, Aurora]
date_added: 2026-09-23
added_by: [Anne, Cath]
endorsed_by: [Anne, Cath]
executor: Claude Code (Dalila)
governing_instructions:
  - _crossrefs/protocols/PROTO-RAG-001.md
  - _crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md (v1.6)
embeds: [2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md, 2026-09-23_nota-EIC2025-v0.1_Anne-Cath-review.md, 2026-09-23_argentina-renaper-tfr_source-discrepancy.md]
title: "Commit the three records embedded below verbatim; apply the cornerstone endorsement; revise the Nota EIC 2025 to v0.2; run the 65+ gate check"
---

# Build instruction — commit endorsements, apply them, revise the nota to v0.2

## Why the records are embedded

Four times since June, records produced in the Demographics chat have not reached the tree.
The cornerstone is still `endorsed_by:` blank on Dalila although Anne endorsed it today. To
close that gap, **the three records this instruction depends on are embedded in full in
§Appendix**, byte-for-byte as produced. Executing this instruction commits them; nothing
depends on a separate upload.

**Verbatim rule.** Write each appendix block to its target path exactly as it appears between
its `~~~~` fences (fences excluded). Do not edit an embedded record's text. Where a record is
out of date against the tree, the correction is made **in the target file it governs**, per the
overrides below, and noted in that file's execution note — never in the record itself.

## Step 1 — Commit the three records

| Appendix | Target path |
|---|---|
| A | `_crossrefs/corpus/demographics/_pending/2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md` |
| B | `_crossrefs/corpus/demographics/_pending/2026-09-23_nota-EIC2025-v0.1_Anne-Cath-review.md` |
| C | `_crossrefs/corpus/demographics/observations/2026-09-23_argentina-renaper-tfr_source-discrepancy.md` |

Record C was drafted as `2026-09-24_…`; it is embedded already renamed and with its `date:` set
to 2026-09-23 (the date-hygiene step skipped it because it was untracked). If an untracked
`2026-09-24_argentina-…` copy exists anywhere in the working tree, delete it after C is committed.

Also commit, if not already tracked, `_crossrefs/_build_instructions/2026-09-23_demographics_anne-delivery-and-corrections.md`
— from the copy Claude Code executed on 2026-09-23. The inbox records it both as executed and as
absent from the tree; resolve by committing the executed copy and noting that in its trailer.

**Done when:** `git ls-files` lists all four; SHA-256 of A, B, C on the tree match the embedded
blocks; commit message references this instruction.

## Step 2 — Apply the cornerstone endorsement (Appendix A)

In `_crossrefs/corpus/demographics/2026-08-13_fernandez-villaverde-norrick_terra-incognita.md`:

1. Frontmatter: `endorsed_by: Anne`; `workflow_status: endorsed`; add
   `endorsement_record: _pending/2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md`.
2. Apply Appendix A §2 conformance edits 1–7, **with two overrides** (the record predates
   Héctor's ratification of the fifth row):
   - edit 2: "ratification by Héctor pending" → *"ratified by Héctor 2026-09-23; instructions v1.6"*;
   - edit 3: "v1.5 (2026-09-15)" → *"v1.6 (2026-09-23)"*.
3. Add the teen-pregnancy citation note (Appendix A §1) to §Source quality.
4. Routing on completion: corpus root (cornerstone); April deck retired to `_build_instructions/`
   if not already; DFD + BDH + Aurora cross-refs appended; inbox line moved to "Endorsed and
   moved" with a pointer to Appendix A.

**Done when:** `git grep -n "endorsed_by: Anne" -- _crossrefs/corpus/demographics/2026-08-13_*`
returns one hit; `workflow_status: endorsed`; edits 1–7 present.

## Step 3 — Close the items Appendix B resolves

Move to "Endorsed and moved" in `_anne_inbox.md`, each with a pointer to Appendix B: the nota
v0.1 line (as *reviewed, revise to v0.2*); the delivery-and-corrections line; the EIC-graphs
record line (fifth row confirmed as carried); the stress-glide item in
`cath_stress_floor_revision_brief.md` §7 (closed — confirmed 2026-09-23). Append to the Cath
brief a §10 "Rulings of 2026-09-23" pointing to Appendix B §3. Batch 1 and the NBER staging
block stay pending.

## Step 4 — 65+ gate check (Appendix B §2) — run before Step 5

Age CPV 2020 forward: population by sex, 5-year groups 50+, at 15 Mar 2020 (INEGI CPV 2020,
cite the tabulado and access date), survived to 15 Oct 2025 with the CONAPO 2023 conciliación
life tables, net of EIC-measured 60+ international emigration. Compare with EIC 2025 65+ by sex
and 5-year group. Write `country/MEX/eic2025_65plus_check.md`: both totals, the difference by
group, and the reading — *aged-CPV ≈ EIC* (gap is CONAPO's; EIC base stands) or *EIC > aged-CPV*
(EIC age overstatement; replace the base 65+ by aged-CPV). Do not choose between the readings
if the difference is ambiguous; report it and stop for Anne.

Provenance: record the SHA-256 and archive URL of the Internet Archive copy of the CONAPO
conciliación used in v0.1; retry the official CONAPO and datos.gob.mx endpoints and record the
response codes.

## Step 5 — Revise the nota to v0.2 (Appendix B §4)

Apply items 1–7 of Appendix B §4 in `GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/`:
C1/C2/F1 corrections; base rebuilt with a pure time shift; Recuadro 2 additions; page-3
headline as the TDR minimum before/after (Appendix B §3.1 text); F3 with OADR beside TDR
(§3.2); τ recomputed as **τ = ρ · OADR / e** with e from INEGI ENOE (latest quarter, 15–64
employment/population, table reference and access date), φ removed everywhere (§3.3); CONAPO-65+
sensitivity row; education sentence to 2031; growth sentence; implication 3 replaced. If Step 4
concludes *EIC > aged-CPV*, build v0.2 on the corrected 65+. Version string `0.2`; all numbers
from CSV.

**Done when:** v0.2 PDF, CSVs and `_assumptions.md` in `output_dir`; `git grep -n "1.39"` and
`git grep -n "φ"` return no hits in the nota sources; one inbox line each to Anne and Cath with
the v0.2 headline values, the τ table, and the Step 4 reading.

## Step 6 — Public chart correction

`mexico_poblacion_2050_variantes_onu.png` (produced in chat, not on the tree) carries the C1
error. If it exists anywhere in the tree or in a shared folder, delete it and log the deletion.
Do not regenerate it. Report to Héctor whether it was published.

## Not to do

- No `endorsed_by:` set on v0.2 — Anne and Cath review it (Appendix B §5).
- No IM-6 rerun (Appendix B §3.5).
- No edit to any embedded record's text.
- Nothing leaves `output_dir` before v1.0.

## Report back

One message: per-step done-when; Step 4 totals and reading; v0.2 headline values; any step
blocked and why.

---

# Appendix


## A — `_pending/2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md`

~~~~markdown
# Anne — endorsement record: reconstructed cornerstone, Fernández-Villaverde & Norrick (2026) *Terra Incognita*

**From:** Anne (population-economics domain authority)
**Date:** 2026-09-23
**Adjudicates:** `_crossrefs/corpus/demographics/2026-08-13_fernandez-villaverde-norrick_terra-incognita.md` (reconstructed 2026-09-15 from the primary source; `endorsed_by:` blank)
**Verdict:** **ENDORSED.** Text checked against the paper; no factual defect found. Set `endorsed_by: Anne`, `workflow_status: endorsed`; `cornerstone: true` stands. Seven catch-up conformance edits below (Debb / Claude Code), none substantive.

> Operational coordination; PROTO-RAG-001 frontmatter omitted by design.

---

## 1. Verification

Checked against the paper (main text §§1–7, Supplemental A–C): replacement-rate derivations; factor-model estimates (λ̂ path, 219/236, −0.0622, loading shares, U-shape 55%/4%, dispersion 0.86/0.29/1.60, R² 0.967, bandwidth and bootstrap); §5.1 arithmetic; Dettling–Kearney, Fazio, Couillard, Taiwan/China, Cohen, Myers–Hooper, Italy, Guatemala figures; Hungary/Czechoslovakia; Table 1 and the counterfactual swap; Korea cohort and tail figures; Acemoglu floors; Tables A1, A2 (4/37; −9.3%; 1,646,502; LAC rows), A3; B.3 revision series; footnote 3 (72%); B.4 Mexico mention. **All correct.**

The entry improves on my 2026-08-13 account by carrying the authors' own factor-model caveats (§Open questions, last bullet). Keep.

**Citation note (add to §Source quality):** the paper states the US teen-pregnancy decline two ways — 71% over 2007–2024 (introduction) and 74% over 2004–2024 (§6.1, attributed to Hudson & Moscoso Boedo 2026). The entry uses the §6.1 figure, which is the sourced one; cite that, not the introduction's.

## 2. Conformance edits (catch-up to the tree as of 2026-09-23)

1. **Stress floor — ruled, not escalated.** §Relevance/DFD, "Chile is the row that moves": replace "escalated to Héctor in Anne's 2026-09-15 record" with *"Héctor ruled option (b) on 2026-09-15: the LAC empirical floor is declared unidentified; 0.9 carried as a working value; Chile 1.03 retired; Puerto Rico 0.87 ruled out. Instructions v1.5."*
2. **LAC ~1.2 landing zone — now a scenario row.** §Open questions, second bullet: replace with *"Addressed 2026-09-22: INEGI EIC 2025 published TGF 1.23 (2024), firing the Q3 §2 trigger; a fifth scenario row `EIC-2025 direct` (1.23 stable) opened per Anne's pre-committed frame, Central held at 1.50 as upper bracket; ratification by Héctor pending."* Cross-reference `releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md`.
3. **Governing instructions version.** Cross-references: "unchanged at v1.4" → "v1.5 (2026-09-15)".
4. **Trigger of record — fired.** Cross-references, Q3 §2/§7 line: append "trigger fired 2026-09-22; see releases entry".
5. **Path — LAC deck entry.** `_pending/2026-09-15_fernandez-villaverde-slides-latam.md` → `observations/2026-09-15_fernandez-villaverde-slides-latam.md` (routed 2026-09-15).
6. **Path — Acemoglu note.** `2026-07-11_baby-busts-growth-booms.md` does not match the batch naming; the Acemoglu note is `GrandPlan/DFD/aging_macro_nber_2609/2026-09-17_baby-busts-growth-booms.md` (staging, pending-anne). Verify and correct; if a 07-11 file genuinely exists, reconcile the duplicate.
7. **Local copy provenance — canonical pull required, non-blocking.** Change "replace when convenient" to a queued Debb item: pull the PDF from the Penn listing (manual browser fetch if automated fetch is refused), record the SHA-256 in the build instruction, and note whether the bytes match the mirror copy. Endorsement does not wait on this; the text verified here is the text of record.

**Frontmatter:** `endorsed_by: Anne`; `workflow_status: endorsed`; add `endorsement_record: 2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md`. Debb to confirm `tier: methodological_reference` is a registered tier in the PROTO schema; if not, `briefing_note`/`working_note` are the fallbacks and the choice is hers.

**Routing on execution:** corpus root (cornerstone); April deck to `_build_instructions/` if not already retired; DFD + BDH + Aurora cross-refs appended; inbox item moved to "Endorsed and moved".

## 3. Record of the reconstruction

The reconstruction was the correct response to the filing gap: drafted from the primary, filed under the name of record so the chain resolves, `endorsed_by` left blank pending review of the actual text. That standard — no endorsement asserted over unseen text — is the one to keep.

---

## Cross-references

- → entry endorsed: `_crossrefs/corpus/demographics/2026-08-13_fernandez-villaverde-norrick_terra-incognita.md`
- → build instruction: `_crossrefs/_build_instructions/2026-09-15_demographics_terra_incognita_reconstruction.md`
- → `2026-09-15_FV-LAC-deck_Anne-endorsement.md` §0 (precondition, now closed)
- → `releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md` (edit 2)
- → `_anne_inbox.md` — move to "Endorsed and moved"
~~~~

## B — `_pending/2026-09-23_nota-EIC2025-v0.1_Anne-Cath-review.md`

~~~~markdown
# Anne & Cath — review record: Nota EIC 2025 v0.1, and open inbox items of 2026-09-23

**From:** Anne (population economics; Steps 1–2, Recuadros 1–2, pp. 1–2) and Cath (public finance; Step 3, p. 3, the window sentence)
**Date:** 2026-09-23
**Adjudicates:** `GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/` v0.1 (PDF, `_assumptions.md`, `results/*.csv`); `cath_stress_floor_revision_brief.md` §6–§9; the four open inbox lines of 2026-09-23.
**Verdict on the nota:** **v0.1 not releasable; revise to v0.2** (§4). The machinery is sound — the WPP-2023-base sensitivity reproduces the endorsed Central (140.3 vs 140.4 M) and the CONAPO life tables reproduce e0 within 0.15 yr. The defects are in *our* specification and in one fiscal formula, not in the execution. Release to Héctor for signature (v1.0) is gated on §5.

> Operational coordination; PROTO-RAG-001 frontmatter omitted by design (precedent: prior Anne records).

---

## 1. Anne — errors that were mine, corrected by the executor

Claude Code caught three specification errors in the 2026-09-23 build instruction. All three are accepted; credit recorded.

**C1 — UN low variant for 2024 is 1.64, not 1.39.** The low/high variants are medium ∓0.5 *phased in* over the first projection years, not from the first year. My figure was medium − 0.5 applied at 2024. Correct Recuadro 1 (ii) to: *"la variante baja de la ONU supone 1.64 para 2024 y llega a 1.20 hacia 2050; lo observado (1.23) ya está en el piso de largo plazo de esa variante."* **The same error is on the public chart `mexico_poblacion_2050_variantes_onu.png`** (labels "TGF 1.39 → 1.20" and "2.39 → 2.20"). That chart must not be used; if it was posted anywhere, a correction is owed. The later chart `mexico_2050_fecundidad_realista.png` makes no low-variant claim and stands.

**C2 — the 6–14 cohort is scenario-independent only to 2031, not 2035.** Children aged 6 in 2031 were born in 2025, the first projected year. The certain result is therefore: *6–14 cae de 18.8 a 15.7 millones entre 2025 y 2031 (−16 %) en todos los escenarios; esos niños ya nacieron.* It is still the strongest sentence in the nota; it just ends in 2031.

**F1 — the mid-year shift imported WPP levels.** I specified the Oct→mid-year shift "by linear interpolation against the WPP-2023 base". That pulls the EIC structure toward WPP's overcount (+0.52 M children vs +0.08 M for a pure time shift) — the opposite of the reason for re-basing. **Ruling:** pure time shift (EIC structure moved back 3.5 months using the scenario's own 2025 components); WPP enters nowhere in the base.

## 2. Anne — the 65+ gate is measured, not cleared

EIC 65+ exceeds CONAPO's conciliación by **+1.2 M at mid-2025** (+1.5 M unshifted) — ~9–10 % of the group. Smaller than the +2.6 M against WPP-2023, still too large to wave through. Two readings, observationally distinguishable:
- CONAPO/WPP understate the elderly (carried from CPV 2020); or
- the EIC overstates older ages (age exaggeration is a known feature of Mexican survey data above 60).

**Check (Debb/Claude Code, ~1 day, gates v1.0):** age CPV 2020 forward — population 55+ and 60+ by sex at 15 Mar 2020, survived to 15 Oct 2025 with CONAPO life tables, net of the small EIC-measured 60+ emigration. If aged-CPV ≈ EIC, the gap is CONAPO's and the EIC base stands. If EIC ≫ aged-CPV, the excess is EIC age overstatement and the base's 65+ is replaced by aged-CPV. Report both numbers in `_assumptions.md`.

**Until then (v0.2):** Recuadro 2 states the gap and its two readings in one sentence; the τ table carries a sensitivity row with CONAPO 65+.

## 3. Cath — fiscal rulings

**3.1 The window — report the minimum, not a span.** v0.1 used minimum ± 5 years on an annual grid; Q3 used a different convention ([min − 5, min] on a 5-year grid). A before/after span comparison across two conventions is not a finding, and "se acorta" was rightly dropped. **Ruling:** the headline is convention-free — the year and level of the TDR minimum, before and after:
> *Central: el mínimo de la razón de dependencia llega hacia 2031 en 45.2, no hacia 2038 en 42.0. La razón hoy es 46.4 (EIC 2025). Entre hoy y su mínimo sólo baja un punto.*

That is the fiscal message for this audience: **the demographic dividend in total-dependency terms is essentially exhausted.** Any span goes in Recuadro 2 with its definition (proposed: years with TDR within 1 point of its minimum), and my timing caveat stays verbatim.

**3.2 The TDR alone misleads — print the old-age ratio beside it (Anne concurs; binding).** In v0.1 the Estrés scenario shows the *lowest* TDR minimum (41.0), which a reader takes as good news; its old-age ratio is the highest of any scenario (the composition point in brief §5). A flat TDR also hides a shift from cheaper dependents (children) to costlier ones (older adults). **F3 becomes two panels or two line sets: TDR and OADR.** One sentence under it: *"La razón total casi no baja porque la caída de niños compensa el aumento de adultos mayores; el costo fiscal de un adulto mayor es mayor que el de un niño."* (Anne: cite the NTA public-transfer age profile for Mexico if in the corpus; otherwise state it without a number.)

**3.3 The contribution-rate formula is wrong as specified — reformulate (τ).** v0.1 computed τ = ρ · P/(φ · N₁₅₋₆₄): coverage φ on contributors, none on beneficiaries. That is internally inconsistent, and it is why holding τ via coverage "required φ = 103–106 %". In a stylised PAYG where beneficiary coverage equals contributor coverage in steady state, coverage cancels:

> **τ_t = ρ · OADR_t / e**, with e the employment-to-population ratio at 15–64.

- ρ = 0.50 (IM-6 `κ_rep`, `ge_model_gender.jl:61` @ 5368693) — stays.
- **φ drops out.** Its source (`Integrated_6.tex`, *untracked*) was a provenance defect anyway — same class as the BID2 attribution.
- **e** from INEGI ENOE, latest quarter, 15–64 employment/population, with table reference and access date. Held constant; say so.
- Recompute for 2025 / 2035 / 2050, Central and INEGI directo, plus the CONAPO-65+ sensitivity row (§2).

**Policy sentence replaced** (my 09-23 draft of implication 3 was wrong under this formula): *"Ampliar la formalidad alivia la cuenta sólo mientras los nuevos cotizantes no se jubilan; en el largo plazo, con reemplazo fijo, la cotización depende de la razón de vejez y de la tasa de empleo."* Note also, for the text: **to 2035 the τ path is identical across scenarios** (16.0 / 22.6 in v0.1 terms) — pension arithmetic for the next decade is already written by who is alive.

**3.4 Growth arithmetic — endorsed.** g_l = +0.37 % a.a. 2025–35 in every scenario; 15–64 starts falling in **2036 in all four**. Another scenario-independent result; say so.

**3.5 IM-6 stress-side keys (brief §6).** Reference update only; no rerun now. IM-6 is rerun **once**, at Q4, on the EIC base with aligned survival — not twice.

**3.6 Survival alignment (brief §8.2).** Align IM-6 to the CONAPO improving path, not the skeleton to fixed survival. If IM-6 cannot carry time-varying survival at Q4, use CONAPO period survival fixed at 2035 as the documented compromise.

## 4. Required revisions → v0.2

1. C1, C2, F1 corrections (§1) in text, Recuadros and figures.
2. Base rebuilt with the pure time shift; all CSVs regenerated.
3. Recuadro 2: 65+ gap sentence (§2); window definition if any span is printed (§3.1); τ formula and e source (§3.3).
4. Page-3 headline per §3.1; F3 with OADR (§3.2).
5. τ recomputed per §3.3; φ removed from every table and sentence.
6. Education sentence per C2; growth sentence per §3.4; implication 3 replaced per §3.3.
7. Every number still generated from CSV; no hand-typed figures.

## 5. Gates for v1.0 (to Héctor for signature)

- the CPV-aging 65+ check run and recorded (§2);
- v0.2 reviewed by Anne and Cath (one pass, both records);
- CONAPO conciliación provenance fixed: the Internet Archive copy used for v0.1 is acceptable **with its SHA-256 and archive URL recorded**; replace with the official download when CONAPO answers.

## 6. Other open inbox items

**Fifth row as carried — confirmed.** `EIC-2025 direct`, 1.23 stable from 2025, v1.6. Origin question (whether Stress and INEGI directo depart from a reconciled 2025 level) stays with Q4.

**v1.6 vs "no v1.6" — resolved correctly.** Héctor's ratification post-dates the constraint; v1.6 stands and the queue is v1.7.

**Stress glide (brief §7) — already confirmed** in `2026-09-23_EIC-addendum_stress-glide_NBER-triage_Anne-endorsement.md` §2; close the item. **Composition point (brief §5) — endorsed** and made binding for the nota in §3.2.

**Contradiction in the inbox, and three filing gaps.** One line says `2026-09-23_demographics_anne-delivery-and-corrections.md` executed Steps 1–5; another says the same file is not on the tree. Both can be true only if it was executed from paste and never committed. Commit it. Also commit, from this chat's outputs:
- `2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md` — **the cornerstone stays `endorsed_by:` blank until this record is on the tree**; I endorsed it today, over the reconstructed text;
- `2026-09-23_argentina-renaper-tfr_source-discrepancy.md` (renamed from 09-24 per the date-hygiene step; it was untracked, so the rename was skipped);
- this record.

Fourth occurrence of the same failure mode. The production-time inbox line (proposed 09-15) should now be ratified by Architecture, not left as practice.

**Batch 1** (Benzell, Kotschy-Bloom, Bernardino, TAR candidates) — built, not yet received here. Send it.

---

## Cross-references

- → `GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/` (v0.1 reviewed; v0.2 per §4)
- → `_crossrefs/_build_instructions/2026-09-23_DFD_nota-EIC2025_build-instruction.md` (superseded in part: §1 base shift, Recuadro 1 (ii), §3.2 formula, implication 3)
- → `cath_stress_floor_revision_brief.md` §5–§9 (items closed or ruled here)
- → `country/MEX/DFD_TFR_forecast_instructions.md` v1.6 (fifth row confirmed; queue v1.7)
- → `_anne_inbox.md` — move the nota, delivery-and-corrections, EIC-graphs and stress-glide lines to "Endorsed and moved" with a pointer here; keep batch-1 and the NBER staging block pending
~~~~

## C — `observations/2026-09-23_argentina-renaper-tfr_source-discrepancy.md`

~~~~markdown
---
title: "Argentina TFR 2024 — RENAPER 1.05 vs DEIS-based 1.23: same vintage, different source; registration-lag reading; acquisition ordered, no anchor entered"
date: 2026-09-23
added_by: Claude
endorsed_by: Anne
projects: [DFD]
indicators: [tfr, births, tempo]
geography: [comparator, argentina]
scenario_implication: [fast-transition]
source_reliability: secondary   # screenshot of the RENAPER dashboard relayed via social media; underlying registry primary once pulled
data_vintage: 2024
promotion_status: ready
corpus_path: _crossrefs/corpus/demographics/observations/
supersedes: "(none — adds to the ARG line in 2026-09-15_fernandez-villaverde-slides-latam.md §4 and the ARG sixth-row ruling in 2026-09-15_FV-LAC-deck_Anne-endorsement.md §2)"
---

## Summary

Fernández-Villaverde (X, 2026-09-23) posts a RENAPER (Dirección Nacional de Población,
Sistema Estadístico de Población) dashboard series for Argentina's Tasa Global de
Fecundidad, total país, 2012–2024: ≈2.2 (2012–13), peak ≈2.3 (2014), 2.0 (2018), ≈1.8
(2019), ≈1.6 (2020), ≈1.5 (2021), ≈1.4 (2022), ≈1.3 (2023), **≈1.05 (2024)**. His 15
September deck tabulated Argentina at **1.23 for 2024** (registry-based) and "2.13 → 1.23
in 8 years." Two values for the same vintage from two Argentine sources.

## Reading

**The 2024 RENAPER point is most likely registration-incomplete.** The 2023→2024 step
(≈−0.25) is the largest in the series and falls at the year where registry data are least
complete; the 2018–2023 steps run −0.1 to −0.2. Cross-check against DEIS: 2024 births
413,135 (F-V&N 2026, Table A2) against ≈777 k at the 2014 peak (TFR 2.3) scales to a TFR
near 1.2, consistent with the deck's 1.23; a TFR of 1.05 would imply ≈355 k births,
well below the DEIS count. **Working read: 1.05 is a lower bound; reconciled 2024 ≈ 1.2,
pending the pulled series.** Same pattern as the Mexican 72% same-year registration
issue (F-V&N fn. 3) — treat the latest registry year as provisional everywhere in LAC.

**Substance unaffected.** Argentina is in lowest-low fertility at collapse speed
(−0.9 to −1.1 in a decade). Series shape matches Colombia and Costa Rica: plateau to
2017, **inflection 2018**, acceleration after. Three core/comparator countries with the
same kink year argues for a mechanism with common timing and country-specific levels.
Period TFR; tempo caveat applies.

## DFD Calibration Implications

**Fast-transition scenario for Mexico:** no change; Argentina is a comparator. The
regional 2018 inflection is a scenario-discipline observation — the acceleration is not
Mexico-idiosyncratic — and the Mexico EIC series (1.9/2019 → 1.23/2024) is consistent with
it.

**Anchor table:** no ARG row; the 2026-09-15 ruling stands (five priority rows; ARG the
sixth if ever added, pinned to DEIS/INDEC primary). This discrepancy is exactly why the
pin must be primary. **No anchor is entered from a screenshot.**

**Coupling/partnership formation:** the 2018 common inflection is an input to the
compositional-vs-cascade adjudication — a period kink shared across countries weighs
toward a period (cascade/accelerant) component over pure cohort replacement, but does
not settle it; the APC decomposition on ENAHO/GEIH still runs.

## Collapse-paper routing

- The common-2018-inflection observation → paper chat, as support for a common-timing
  mechanism (union composition with a regional accelerant) and against country-specific
  political explanations. F-V's 219/236 point is the *Terra Incognita* single-factor
  result and can be cited as such.
- Argentina's role as the third cohabitation regime for `w` identification is unchanged
  and more urgent.

## Acquisition (Debb — priority)

1. RENAPER dashboard: TGF, nacimientos registrados, and **edad mediana de la madre**,
   total país and by province, 2012–2024 (the median-age series is a free first tempo
   read for Argentina).
2. DEIS vital statistics: births by year of *occurrence*, 2012–2024, with the 2024
   completeness note; INDEC women 15–49 denominators.
3. Reconcile the two 2024 values; record the reconciled figure and the completeness
   caveat in the ARG line of the anchors brief.
4. Already queued: census 2010/2022 union status (for `w`).

## Source

Fernández-Villaverde, X post, 2026-09-23, with screenshot of RENAPER — Dirección Nacional
de Población, "Nacimientos en Argentina (2012–2024)", Nivel Provincial › Evolución › Tasa
Global de Fecundidad, total país. Local copy: 1790192894587_image.png. Values read from
the chart; to be replaced by the pulled series.
~~~~
