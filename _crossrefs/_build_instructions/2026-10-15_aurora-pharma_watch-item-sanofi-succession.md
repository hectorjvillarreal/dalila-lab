---
type: build_instruction
build_type: expansion
date: 2026-10-15
corpus_affected: [GrandPlan/Aurora/pharma/watch_items/]
triggered_by: "Héctor, after a conversational Sanofi check ('Sanofi is not doing well, or so it seems... tough'): 'yes, add the Sanofi watch item'"
agents_involved: [Héctor, Claude Code]
status: executed
notes: "Second watch item in the pharma instance. No feed candidate staged: the July pipeline events predate the current feed window and are recorded in the watch item, not ingested."
---

# Aurora pharma — Sanofi Dupixent-succession watch item

## Scope and rationale

A watch item on `SNY` (roster #11) after the Q2 2026 removal of three
pipeline programmes (amlitelimab AD, itepekimab, balinatunfib) while
Dupixent reached about half of group sales ahead of its March 2031 US
patent expiry. Conforms to the PROTO-RAG-001 watch-item schema, using the
olpasiran item (2026-10-03) as template.

Corrections recorded against the conversational check that preceded this
instruction (it relied on search summaries):

- The €952 M impairment was amlitelimab only. Itepekimab was not part of it.
  The total impairment line was €1,031 M (Q2 release).
- Balinatunfib was also discontinued in Q2. The check missed it.
- Sanofi did raise 2026 guidance (sales ~+10% CER). A secondary source said
  it was "not amending" guidance; the primary source overrides it.
- The celiac trial NCT06557772 reached primary completion on 2026-08-05
  (ACTUAL). Its 2029-04-10 date is study completion, not the readout.

## Folder scaffold

None (`watch_items/` exists).

## Per-artifact creation instructions

- `GrandPlan/Aurora/pharma/watch_items/2026-10-15_sanofi-dupixent-succession.md`:
  as written; `endorsed_by` left empty pending Elle.

## Cross-reference register updates

None.

## Execution checklist

- [x] Q2 2026 press release read (primary) for Dupixent, guidance, pipeline decisions, impairment
- [x] Registry checked (ClinicalTrials.gov API v2) for NCT06557772
- [x] Q3 2026 results date confirmed (Sanofi press release 2026-10-06: 2026-10-30)
- [x] File written
- [ ] Elle endorsement of the watch item
- [ ] Check at Q3 release (2026-10-30)

## Notes

Share prices in the watch item come from a secondary source (InvestSmart) and
are marked unverified. No successor asset is named as "next" because none
was verified in this pass.
