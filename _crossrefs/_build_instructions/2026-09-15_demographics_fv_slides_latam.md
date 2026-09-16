---
type: build_instruction
build_type: expansion
date: 2026-09-15
corpus_affected:
  - _crossrefs/corpus/demographics/_pending/2026-09-15_fernandez-villaverde-slides-latam.md
  - _crossrefs/corpus/demographics/_pending/anne_slides_latam_anchor_brief.md
  - _crossrefs/corpus/demographics/_pending/_anne_inbox.md
triggered_by: "Héctor deposited `Slides_Latam.pdf` in the demographics corpus root (2026-09-15), asked Claude Code to read it, then asked whether DFD projections should be updated. Ruling: no projection update. Three narrower actions authorised — file the corpus entry, log the Mexico 1.51/2025 reading against the Q3 re-anchor trigger, and put the BRA anchor pin to Anne."
agents_involved: [Claude Code, Héctor]
status: executed
sequence_position: "1_of_1"
notes: "No projection re-run, no cohort-component input moved, no calibration flag closed. Neither the endorsed Q3 replicate nor scenario_anchors.md is edited by this build — both carry Anne's endorsement and may be amended only by her ruling or an explicit retrofit build (PROTO-RAG-001 §Standing principles 5)."
---

# Build instruction — Fernández-Villaverde, "A Recent Population History of Latin America and the Caribbean" (2026-09-15)

## 1. Scope and rationale

A second Fernández-Villaverde presentation deck entered the demographics corpus
folder on 2026-09-15 (`Slides_Latam.pdf`, Beamer, dated 15 September 2026,
48 pages / 40 numbered slides). It is the LAC-specific successor to the April
deck already filed as the corpus cornerstone
(`2026-06-20_fernandez-villaverde-demographic-future.md`).

Héctor's question on reading it was whether the DFD projections should be
updated. The assessment recorded in the entry is **no**, on three grounds:

1. The deck argues for the scenario discipline DFD already holds. CELADE/UN WPP
   medium is already the *optimistic* column by rule (`DFD_TFR_forecast_instructions.md`
   v1.4 §2); Central is already fast-transition at TFR 1.50; the corpus README's
   standing principle already states that fast-transition is the baseline rather
   than a stress test. The April entry reached the same verdict for the same
   reason ("strengthens the standing discipline rather than revising it").
2. The one figure capable of moving an operational anchor — Mexico **1.51 (2025)** —
   does not fire the armed Q3 re-anchor trigger. It misses on both legs (above the
   ≤ 1.50 threshold; not an INEGI publication).
3. The inputs that would genuinely move the numbers are the Q4 acquisition items
   (age-structure retabulation, CONAPO life tables, ENOE 20–39 cut,
   occurred-vs-registered wedge). Re-projecting ahead of those spends effort on
   the least informative available input.

This build therefore files the reference and routes two judgment calls to Anne.
It commits no calibration change.

## 2. Folder scaffold

None. All three artifacts land in existing folders.

## 3. Per-artifact creation instructions

### 3.1 `_crossrefs/corpus/demographics/_pending/2026-09-15_fernandez-villaverde-slides-latam.md`

`type: corpus_entry`, `tier: working_note` (multi-country / cross-cutting),
`added_by: Claude Code`, `endorsed_by:` blank,
`workflow_status: pending-endorsement`. Routed to `_pending/` per the
`dfd-demographics-monitor` §Routing and Filing endorsement workflow step 1.

Structure follows PROTO-RAG-001 §Entry structural conventions. The entry carries
a **discriminator ruling** (REPORT, not REVISION — a conference deck is not a WPP
revision; the Revision Transition Protocol does not fire), the **re-anchor trigger
check** against Q3 §2, and the **BRA anchor discrepancy**.

**Open routing question flagged for Anne, not decided here.** The April deck sits
at the corpus root carrying `cornerstone: true`, which predates the routing table
now in force. Under that table a multi-country `working_note` endorses to
`observations/`. Anne decides whether this entry follows the routing table or is
filed alongside its predecessor at the root as a second cornerstone.

### 3.2 `_crossrefs/corpus/demographics/_pending/anne_slides_latam_anchor_brief.md`

Operational coordination, not a corpus artifact. PROTO-RAG-001 frontmatter is
omitted by design, matching the `anne_scenario_anchors_brief.md` and
`_anne_inbox.md` precedent. Carries the two Anne-domain decisions: the re-anchor
trigger reading, and the BRA anchor pin (which attaches to an open judgment call
already standing in her May brief).

### 3.3 `_crossrefs/corpus/demographics/_pending/_anne_inbox.md`

Two lines appended to `## Pending`, which was cleared 2026-08-03.

## 4. Cross-reference register updates

**Deferred to endorsement, by design.** Project cross-refs
(`GrandPlan/{DFD,BDH,Aurora}/docs/corpus/_cross_references.md`) are appended when
Anne endorses and the entry moves out of `_pending/`, per the skill's
§Routing and Filing workflow step 3 and the UNFPA entry's precedent
("append on endorsement, per §Routing"). Nothing is appended by this build.

## 5. CLAUDE.md updates

None. No change to corpus organisation, protocol status, or project structure.

## 6. Acquisition list updates

None filed. The deck's own primary sources (national vital registries per
country, the July-2024 WPP projection vintage used in its slide-16 test) are
already reachable through the standing Q4 acquisition items; no new Tier-2 entry
is warranted until Anne rules on the BRA row.

## 7. Execution checklist

- [x] Corpus entry drafted to `_pending/`, `endorsed_by:` blank
- [x] Anne brief drafted to `_pending/`
- [x] Two lines appended to `_anne_inbox.md` §Pending
- [x] This build instruction filed and back-linked from both artifacts
- [ ] Anne: re-anchor trigger reading (§1 of the brief)
- [ ] Anne: BRA anchor pin decision (§2 of the brief)
- [ ] Anne: routing decision — `observations/` vs corpus root (§3 of the brief)
- [ ] On endorsement: fill `endorsed_by`, set `workflow_status: endorsed`, move
      out of `_pending/`, append project cross-refs

## 8. Notes

**What this build deliberately does not touch.**

- `scenario_anchors.md` — endorsed by Anne 2026-05-16. The MEX row (1.60/2023)
  does not move on a secondary source, per her own sourcing rule 2 (primary
  sources only for the anchor row; secondary aggregators corroborate but are not
  the citation).
- `country/MEX/quarterly/2026-Q3_demographic_replicate.md` — fully endorsed
  (Anne §§1–3,5–6; Cath §4/§5/§7). The trigger observation is logged in the new
  entry and the inbox, **not** written into the endorsed replicate.
- `DFD_TFR_forecast_instructions.md` v1.4 — no version bump. No scenario
  definition, population implication, or fiscal-window value changes.
- `GrandPlan/DFD/docs/calibration_flags.md` — noted in-session as stale
  (last updated 2026-05-10, zero closed flags, F-2026-05-01 still carrying a
  1.55 fast-transition anchor superseded by two endorsed replicates). Héctor's
  ruling was to fold that cleanup into Q4 rather than this build. Recorded here
  so the observation is not lost.

**Downstream exposure assessed, no action taken.** `Missions/Funded/BID2/GE-now
with Gender/demographic_experiment/demographics_2050.jl` hard-codes UN WPP 2024
medium (Mexico TFR 2050 = 1.70; entry cohort derived from TFR ≈ 1.85) — the
optimistic scenario under DFD's own rule. Left as is deliberately: the experiment
is a comparative steady state explicitly documented as "not a fiscal forecast",
so optimistic demography makes the aging result *conservative* and the paper
understates the pressure it documents. That is referee-proof and wants a sentence
of acknowledgement, not a recalibration.
