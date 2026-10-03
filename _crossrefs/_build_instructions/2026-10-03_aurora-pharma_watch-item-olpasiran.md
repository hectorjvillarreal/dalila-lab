---
type: build_instruction
build_type: expansion
date: 2026-10-03
corpus_affected: [GrandPlan/Aurora/pharma/watch_items/, GrandPlan/Aurora/pharma/feed/_staged/]
triggered_by: "Héctor, after the ad hoc Amgen news sweep: 'add dazodalibep as a candidate and olpasiran as watch item'"
agents_involved: [Héctor, Claude Code]
status: executed
notes: "First watch item in the pharma instance; watch_items/ folder created. The dazodalibep candidate is staged, not ingested: harness.py only ingests through `cycle`, and running an off-cycle cycle would advance rotation and calibration."
---

# Aurora pharma — olpasiran watch item + staged dazodalibep candidate

## Scope and rationale

Two outputs from the 2026-10-03 Amgen sweep, at Héctor's instruction:

1. A watch item on olpasiran's OCEAN(a)-Outcomes trial after pelacarsen's
   Lp(a)HORIZON miss (2026-09-04). Conforms to PROTO-RAG-001 watch-item schema.
2. Dazodalibep OASIZ 301 (Amgen, 2026-09-22) as a feed candidate.

Correction recorded: the sweep reported an OCEAN(a)-Outcomes completion of
"~Dec 2026" from a search summary. The registry (NCT05581303, updated
2026-02-27) gives an estimated primary completion of 2028-03-31. The watch
item uses the registry date.

## Folder scaffold

- `GrandPlan/Aurora/pharma/watch_items/` (new)
- `GrandPlan/Aurora/pharma/feed/_staged/` (new; holds manual candidates
  between cycles, emptied by the next cycle)

## Per-artifact creation instructions

- `watch_items/2026-10-03_olpasiran-lpa-outcomes.md`: as written; `endorsed_by`
  left empty pending Elle.
- `feed/_staged/cycle10_manual_candidates.yaml`: one candidate (q009,
  amgen.com primary). At cycle 10, append it to the cycle's candidates file,
  run `harness.py cycle`, and delete the staged file in the same commit.

## Cross-reference register updates

None.

## Execution checklist

- [x] Registry checked (ClinicalTrials.gov API v2) for NCT05581303
- [x] Dazodalibep date verified against the Amgen press release (2026-09-22)
- [x] Files written
- [ ] Elle endorsement of the watch item
- [ ] Candidate ingested at cycle 10

## Notes

The harness fence (`guarded_open`) governs harness writes only; `_staged/` is
written by the instance, not the harness, and nothing in harness.py reads it.
