---
type: research_watch_item
status: open
date_opened: 2026-10-15
opened_by: [Héctor, Claude Code]
endorsed_by:   # pending Elle (Aurora domain authority)
promoted_by:
date_promoted:
related_corpus: [GrandPlan/Aurora/pharma/feed/items.yaml#20260826-0002, GrandPlan/Aurora/pharma/ratios/roster.md]
related_projects: [Aurora]
build_instruction: "_crossrefs/_build_instructions/2026-10-15_aurora-pharma_watch-item-sanofi-succession.md"
---

# Sanofi Dupixent succession: what replaces half the company's sales before 2031?

## Origin

Opened by Héctor on 2026-10-15 after a conversational check on Sanofi
(`SNY`, roster #11) ("Sanofi is not doing well, or so it seems"). The
check found that revenue is strong but the pipeline is thin: Sanofi is
not losing sales, it is losing the drugs meant to succeed Dupixent.

## The thread

Facts below are verified against the Q2 2026 press release (2026-07-30)
unless marked otherwise:

- **Concentration.** Dupixent sales grew 37.6% to €5.2 B in Q2 2026, the
  first quarter above €5 B. That is about half of group sales (€11.6 B,
  +17.8%). Sanofi now guides Dupixent to about €25 B in 2030, at CER.
- **Cliff.** The roster anchors `SNY` on the Dupixent US composition patent,
  March 2031 (company base case). The 2030 guidance is therefore the peak
  year before the cliff.
- **Successors removed in one quarter.**
  - *Amlitelimab* (OX40L, from the $1.1 B Kymab deal) will not be filed in
    atopic dermatitis, even though the ESTUARY phase 3 maintenance study was
    positive: it "would not represent a meaningful improvement to the
    standard of care". There was a €952 M impairment on the amlitelimab
    intangible.
  - *Itepekimab* (IL-33, with Regeneron) dropped in COPD and in chronic
    rhinosinusitis.
  - *Balinatunfib* (oral TNF) dropped after the Crohn's and UC phase 2
    interim analyses missed internal efficacy thresholds.
  - *Dupixent* in lichen simplex chronicus: STYLE 1/2 missed their primary
    endpoints. This is a label expansion lost, not a successor.
- **Integration.** About 229 Massachusetts layoffs, a year after the $9.1 B
  Blueprint Medicines acquisition (feed item 20260826-0002, STAT).
- **Leadership.** CEO Belén Garijo has framed the work as an "accelerated
  transformation roadmap" with pipeline prioritisation and external growth.
- **Market.** The shares traded roughly €71–75 through September (€72.64 on
  2026-10-02; secondary source, InvestSmart). The cliff does not look priced
  in yet. Not verified against Euronext.

## Remaining amlitelimab exposure

**NCT06557772** (ClinicalTrials.gov API v2, last update posted 2026-08-31):
phase 2a/b in non-responsive celiac disease. 229 enrolled (actual). Status
ACTIVE_NOT_RECRUITING. **Primary completion 2026-08-05 (ACTUAL)**; study
completion est. 2029-04-10. Primary endpoint: change in Vh:Cd ratio, baseline
to week 28. The primary endpoint is complete, so a topline readout can come
at any time. The Q3 release is a natural place for it.

## Modeling implication

For the pharma board, not DFD. `SNY` sits in the roster as "vaccines plus
branded; different rent structure from the small-molecule majors". This item
tests whether that structure protects Sanofi from single-asset rent
concentration. The evidence so far says it does not: one biologic carries
the firm, and the in-house successors failed on *relative* value (the
standard of care set by Dupixent itself), not on safety. Sanofi has to
replace a franchise it dominates, and its own drug is the comparator.
The likely response is buying the successor (Blueprint, Dynavax), which
moves `SNY` toward the `4502.T` pattern (debt-financed acquisition of
frontier rent).

## Open questions

- What is the next named Dupixent-adjacent successor in immunology? Not
  verified in this pass; check the Q3 pipeline appendix before citing any
  asset.
- Will Sanofi give a post-2031 Dupixent erosion curve, or only the €25 B 2030
  number?
- Does the "external growth" language turn into a large immunology deal, and
  how is it financed?
- Is the €10 B 2030 "Pharma launches" target organic, or does it depend on
  the acquired assets?

## Status

Watch item, not active commitment. Cadence: low. Check at each Sanofi
quarterly release (next: **Q3 2026 on 2026-10-30**, webcast 12:30 CET) and on
any ClinicalTrials.gov update to NCT06557772.

## Triggers for promotion

1. Topline readout of NCT06557772 (amlitelimab in celiac disease), positive
   or negative.
2. Sanofi announces an immunology acquisition or in-licensing above
   ~$5 B, or explicitly names it as a Dupixent successor.
3. Dupixent 2030 guidance or the 2031 LOE base case changes (earlier at-risk
   biosimilar entry, a patent settlement, IRA price selection).
4. Another late-stage immunology discontinuation.

## Cross-references

- → Feed item: `GrandPlan/Aurora/pharma/feed/items.yaml` (20260826-0002, Blueprint layoffs)
- → Roster: `GrandPlan/Aurora/pharma/ratios/roster.md` (`SNY`, Dupixent, 2031)
- → Sibling watch item: `watch_items/2026-10-03_olpasiran-lpa-outcomes.md` (same pattern: successor risk ahead of an LOE cliff, `AMGN`)
- → Primary: Sanofi Q2 2026 press release, https://www.sanofi.com/assets/dotcom/pressreleases/2026/2026-07-30-05-30-00-3335767-en.pdf
- → Registry: https://clinicaltrials.gov/study/NCT06557772
- → Q3 date: https://www.sanofi.com/en/media-room/press-releases/2026/2026-10-06-05-30-00-3375120
- → Build instruction: `_crossrefs/_build_instructions/2026-10-15_aurora-pharma_watch-item-sanofi-succession.md`
