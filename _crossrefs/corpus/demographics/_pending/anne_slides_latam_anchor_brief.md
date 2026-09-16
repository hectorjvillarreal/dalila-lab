# Anne — anchor decisions arising from the Fernández-Villaverde LAC deck

**To:** Anne (population-economics domain authority)
**From:** Claude Code, on Héctor's instruction
**Date opened:** 2026-09-15
**Source entry:** `_crossrefs/corpus/demographics/_pending/2026-09-15_fernandez-villaverde-slides-latam.md`
**Build instruction:** `_crossrefs/_build_instructions/2026-09-15_demographics_fv_slides_latam.md`
**Project scope:** DFD, BDH, Aurora
**Priority:** normal — nothing is blocked. Héctor has already ruled that no
projection is updated on this deck. These are the two anchor judgments it raises,
plus one routing call.

> This file is operational coordination, not a corpus artifact. PROTO-RAG-001
> frontmatter is omitted by design (matches the `anne_scenario_anchors_brief.md`
> and `_anne_inbox.md` precedent).

---

## 1. Re-anchor trigger reading — Mexico 1.51 (2025)

**Our reading: the trigger does not fire. Confirm or overturn.**

Q3 §2 armed it: *if INEGI publishes a TGF ≤ 1.50 for vintage 2024 or 2025, the
Central anchor is re-examined.* Your pre-committed frame (2026-08-03): published
TGF in [1.45, 1.50] → re-pin Central at the published value; below 1.45 → do not
chase the point estimate, open a fifth scenario row, keep Central at 1.50 as the
upper bracket.

The deck reports **Mexico TFR 1.51, vintage 2025**, attributed to the country's own
registry. It misses on both legs:

1. **Threshold.** 1.51 > 1.50 — one hundredth above a stated threshold.
2. **Source.** It is Fernández-Villaverde's tabulation, not an INEGI publication.
   `secondary` under the corpus reliability rule; absent from the top of the
   Mexico source hierarchy (INEGI registries → INEGI census → CONAPO → CELADE →
   WPP). Your own sourcing rule 2 says secondary aggregators corroborate but are
   not the citation.

**The tension we did not resolve.** The deck's 1.51 (2025) sits *above* Q3's
registry-implied ≈ 1.46 (2024). Different bases — Q3 scaled the ENADID 2023 survey
anchor by the ENR fertile-age rate decline (52.2 → 47.7); the deck is presumably
registered births over a projected denominator. We read the inconsistency as an
argument for waiting on INEGI rather than moving now, and as a sharpener for Q4
follow-ups 5 (watch INEGI for a 2024/2025 TGF) and 7 (occurred-vs-registered
wedge).

**What we did *not* do, deliberately:** nothing was written into the Q3 replicate.
It carries your endorsement and Cath's, and PROTO-RAG-001 §Standing principles 5
forbids silent amendment of endorsed artifacts. The observation is logged in the
new corpus entry and in your inbox only.

**Decision needed:** confirm the non-fire, or rule that a credible secondary
reading at 1.51/2025 is itself grounds to re-examine Central ahead of an INEGI
publication.

---

## 2. BRA anchor pin

**This attaches to an open judgment call already standing in your May brief** —
whether a sixth, non-priority row (Argentina or Brazil) joins
`scenario_anchors.md`, or whether non-priority countries cite source in-note
indefinitely.

**What prompted it.** `Missions/Funded/CAF_DEM/proj_TFR_stable_6countries.py`
carries, as the only un-pinned row in the file:

```
BRA  tfr_obs 1.50  year 2023  src "IBGE estimación 2023 (pendiente source-pin Anne)"
```

Every other country in that script pulls a confirmed anchor from
`scenario_anchors.md` (CRI 1.12, COL 1.10, CHL 1.03, PAN 1.80). Brazil is the
outlier, and the annotation names you.

**What the deck adds.** Brazil **1.52, vintage 2025**, registry-based — and, on the
slide-16 out-of-sample test, Brazil actual 2,376,901 births against a WPP
projection of 2,572,000, −7.6%. So the deck **corroborates the level** (1.50 →
1.52 is within noise) and offers a **two-year newer vintage**, but per your
sourcing rule 2 it cannot be the citation. A pin still needs IBGE primary.

**Decision needed:**

- (a) Add BRA as a sixth anchor row, pinned to an IBGE primary release, with the
  deck as corroboration only; or
- (b) Keep the anchor table strictly to the five priority countries and let the
  CAF script cite BRA in-note, with the vintage updated to whatever IBGE primary
  supports.

Either way the practical question for the script is whether the row moves from
1.50/2023 to a 2025 vintage. **Note the constraint:** CAF_DEM P3 shipped 5 August
under an absolute no-recalculation freeze (`CAF_DEM_P3_instrucciones_tex.md` §0),
so nothing regenerates there. P4 is the live product (contract CW29884 runs to
22 October) and carries the aging-conditioned projection plus the forecast
intervals P3 deferred — that is where a changed anchor would land. The CAF
deliverable is CAF IP; this brief records only the anchor value, not deliverable
content.

---

## 3. Routing call for the new entry

The April deck sits at the **corpus root** carrying `cornerstone: true`. That
predates the routing table now in force, under which a multi-country
`working_note` endorses to `observations/`.

**Decision needed:** does this entry follow the routing table to `observations/`,
or is it filed alongside its predecessor at the root as a second cornerstone? We
drafted it as `tier: working_note` and left the destination to you.

---

## 4. For information — no decision sought

- **No projection updated, no calibration flag closed.** Héctor's ruling. The
  scenario definitions, 2050 population implications, and fiscal-window values are
  untouched; the Q3 window-timing caveat still applies downstream.
- **BID2 exposure assessed and left alone.** `demographics_2050.jl` hard-codes WPP
  2024 medium (Mexico TFR 2050 = 1.70) — the optimistic scenario by our own rule,
  inside a funded paper. Deliberately unchanged: the aging experiment is a
  comparative steady state explicitly documented as "not a fiscal forecast", so
  optimistic demography makes the result *conservative* and the paper understates
  the pressure it documents. It wants an acknowledging sentence, not a
  recalibration.
- **`calibration_flags.md` is stale.** Last updated 2026-05-10, zero closed flags,
  and F-2026-05-01 still carries a 1.55 fast-transition anchor superseded by two
  endorsed replicates. Its action is substantially done. Héctor folded the cleanup
  into Q4.
- **Candidate watch item, not opened.** Goldin (2026) gender-mismatch implies a
  paradoxical reversal — the most gender-unequal societies start highest and end
  lowest. If that holds it is a structural argument for LAC overshooting *below*
  East Asia rather than stabilising with it, which would bear on the Stress
  column's floor (currently anchored to Chile 1.03). Your call whether it rises to
  a `research_watch_item`.

---

## Cross-references

- → Source entry: `_crossrefs/corpus/demographics/_pending/2026-09-15_fernandez-villaverde-slides-latam.md`
- → Build instruction: `_crossrefs/_build_instructions/2026-09-15_demographics_fv_slides_latam.md`
- → Prior brief this extends: `_crossrefs/corpus/demographics/_pending/anne_scenario_anchors_brief.md`
- → Trigger of record: `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q3_demographic_replicate.md` §2, §7
- → Anchor file: `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Inbox log: `_crossrefs/corpus/demographics/_pending/_anne_inbox.md`
