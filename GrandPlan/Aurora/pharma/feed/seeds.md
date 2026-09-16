# seeds.md — pharma feed

**Owner:** Héctor. Human-owned, tool-read-only.
**Drafted by:** Nina, 2026-08-16. Draft for correction, not a specification.
**Read by:** the pharma feed harness (`20260816_AURORA_BUILD_pharma-feed-harness_v1.0`).

This file holds the two things the harness may not decide for itself: **what counts
as a promote**, and **where to start looking**. Everything else in the feed is a
fact about yield and belongs to the machine.

---

## 1. The promote test

**Promote an item if it moves something. Reject it if it only asserts something.**

A thing that moves is a capability, a date, a constraint, a price, or a counterparty
relationship that is different after the item than before it. An assertion is a
claim about the world that leaves the world where it was — a forecast, a strategy
statement, an analyst view, an expression of intent.

The distinction is not about importance. A CEO announcing a pivot to AI-driven
discovery may matter enormously and still fails the test, because nothing has moved
yet. When the same firm signs a compute contract with a stated term and value, that
passes — the assertion has acquired a schedule and a counterparty.

### Passes

- A regulatory decision, with its date: approval, rejection, complete response,
  label change, withdrawal.
- An exclusivity date confirmed, extended, or lost — including litigation outcomes
  that move one.
- A signed transaction: acquisition, licensing deal, option exercise, collaboration
  with disclosed terms.
- A capacity commitment: plant, CDMO contract, fill-finish line, API facility, with
  location and scale.
- A pricing or reimbursement rule that binds: formulary decision, HTA outcome,
  negotiated price, tariff, procurement rule.
- A supply constraint that materialises: shortage, export restriction, plant
  suspension, precursor disruption.
- A trial readout with a stated endpoint result — pass or fail. Failure is a move.
- A policy instrument entering force, or a draft one with a comment deadline.

### Fails

- Analyst notes, price targets, upgrades, downgrades.
- Strategy announcements, pipeline optimism, "we intend to" statements.
- Conference presentations without data.
- Market-size projections and industry forecasts.
- Anything whose news value is that someone said it.

### Hard calls, resolved in advance

**A rumoured deal.** Fails until signed — but if the rumour itself moves a
counterparty (a rival bid, a regulatory comment), the *response* passes and the
rumour rides along as context.

**A level restated.** A firm reporting that its LOE exposure is $12bn has not moved
anything if that was already known. If the figure has changed, the change is the
item, not the level. Record what moved, not what was reported.

**A policy proposal.** Passes only when it carries a date — entry into force, a
comment deadline, a vote scheduled. Undated proposals decay into assumptions and
should be left in the noise.

**An item that fails the test but bothers you.** Promote it and say so in a note.
A criterion that never produces discomfort is not being tested. But do this rarely
— the harness reads promotes as ground truth and cannot see your hesitation.

---

## 2. Seed queries — main lane

Short by design. The harness composes variants; these set the direction.

**Rent extinction**
- q001 `patent cliff pharma`
- q002 `loss of exclusivity`
- q003 `biosimilar launch`
- q004 `generic entry approval`
- q005 `patent litigation pharma ruling`

**Rent replacement**
- q006 `pharma acquisition biotech`
- q007 `pharma licensing deal`
- q008 `in-licensing China biotech`
- q009 `pharma pipeline failure phase 3`
- q010 `pharma restructuring layoffs R&D`

**The diffusion layer**
- q011 `India generics export`
- q012 `China API production`
- q013 `pharmaceutical precursor supply`
- q014 `CDMO capacity expansion`
- q015 `drug shortage cause`

**Frontier cost**
- q016 `AI drug discovery deal`
- q017 `AI pharma partnership compute`
- q018 `machine learning clinical trial design`

**The payer**
- q019 `drug price negotiation`
- q020 `HTA reimbursement decision`
- q021 `formulary exclusion`
- q022 `pharmaceutical tariff`

**The gate**
- q023 `FDA approval decision`
- q024 `EMA CHMP opinion`
- q025 `NMPA approval`
- q026 `PMDA approval Japan`
- q027 `CDSCO India approval`

**Instruments and walls**
- q028 `pharmaceutical export control`
- q029 `biosecurity legislation pharma`
- q030 `pharmaceutical industrial policy`
- q031 `onshoring drug manufacturing`

---

## 3. Exploration set

Zero promotes to date, by construction. Exempt from yield pressure. Rotating — the
harness draws a subset each cycle rather than running all of them.

These exist because the main lane encodes what I currently think matters, and the
main lane will get better at finding exactly that. This set is where the feed's
capacity to be surprised lives.

- x001 `Brazil pharmaceutical policy`
- x002 `Indonesia drug manufacturing`
- x003 `Nigeria pharmaceutical production`
- x004 `Gulf sovereign fund biotech`
- x005 `compulsory licensing medicine`
- x006 `pandemic treaty stockpile`
- x007 `veterinary pharmaceutical market`
- x008 `CDMO acquires drug asset`
- x009 `insurer acquires manufacturer`
- x010 `pharmacy benefit manager reform`
- x011 `hospital compounding scale`
- x012 `biologics licence transfer`
- x013 `pharmaceutical counterfeiting enforcement`
- x014 `pharmaceutical waste regulation`
- x015 `state owned pharmaceutical enterprise`

---

## 4. Deliberately absent

Noted so their absence is legible as a choice rather than an oversight.

**No market-cap, price, or valuation queries.** The back-office capitalisation
model is blocked on the board's firm set. Letting price data into the feed now
would let the monitor layer nominate its own objects, which is the failure the
board/monitor separation exists to prevent.

**No firm names.** Naming the big ten in the seed set would produce a feed about the
big ten, and entry is by basis gap, not by size. Firms should arrive because
something they did surfaced through a mechanism query.

**No archetype or classification language.** There is no archetype set yet and the
feed must not invent one by vocabulary.

**No therapeutic-area queries.** Oncology, immunology, and metabolic would each
generate volume, but they sort by biology rather than by strategy, and the board
sorts firms by what they do about rent. If a therapeutic area turns out to be
strategically load-bearing, it should emerge from promoted items — and the entity
counter will show it.
