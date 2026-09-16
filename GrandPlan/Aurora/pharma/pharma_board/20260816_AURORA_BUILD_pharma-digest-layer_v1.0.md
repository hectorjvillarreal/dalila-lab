---
doc_id: 20260816_AURORA_BUILD_pharma-digest-layer_v1.0
title: "Build instruction — digest layer, pharma instance"
project: Aurora
type: build instruction
version: 1.0
date: 2026-08-16
added_by: Nina
endorsed_by: Elle
status: active — additive to both pharma build instructions
related:
  - 20260816_AURORA_BUILD_pharma-feed-harness_v1.0
  - 20260816_AURORA_BUILD_pharma-ratio-panel_v1.0
---

# Build instruction — digest layer

**Addressed to:** Claude Code instance, Dalila.
**Additive.** Neither existing build instruction is modified. This adds one
directory and one file.

---

## 0. Scope arrest

This builds a **concatenation and a counter**. Nothing else.

The digest **must not summarise, rank, highlight, or characterise** any feed item
or panel figure. It copies text and computes arithmetic over counts and dates.

The reason is structural, not stylistic. The feed's entire calibration loop trains
on one input — Héctor's promote flags — and those require him to read the items
themselves. A digest that summarises becomes an editorial layer he reads *instead
of* the items, and the promote signal degrades toward the summariser's judgment
while continuing to look like human input. If a summary appears anywhere in the
output, the build has failed.

Repo fence: writes confined to `GrandPlan/Aurora/pharma/`. Specifically
`pharma/DIGEST.md` and `pharma/_digest/`.

---

## 1. Layout

```
GrandPlan/Aurora/pharma/
├── DIGEST.md          ← the single surface; overwritten each run
├── _digest/           ← archived DIGEST vintages, append-only
├── feed/              ← unchanged
└── ratios/            ← unchanged
```

`DIGEST.md` is overwritten. The previous version is copied to
`_digest/YYYYMMDD_HHMM_digest.md` before overwriting, so the surface stays single
while the record stays complete.

Source reports in `feed/_reports/` and `ratios/_reports/` remain authoritative and
untouched. The digest never edits them.

---

## 2. DIGEST.md structure

Three blocks, in this order. Order is load-bearing — the state block must be
readable without scrolling.

### Block 1 — state

Computed, not written. Every field is arithmetic over files.

```
PHARMA INSTANCE — state as of <timestamp>

items awaiting promote flag ......... N
oldest unflagged item ............... N days
cycles since last promote flag ...... N
feed calibration .................... <cold start, cycle N of 3 | active | starved>
provisional queries pending ......... N
roster size ......................... N
panel last refreshed ................ N days ago
```

**`starved`** is set when the harness has completed three or more cycles with zero
promote flags recorded. It is the only evaluative word in the digest and it
describes the *system*, never the industry. When starved, the block carries one
fixed line beneath it:

> Calibration is inert. Query retirement, source weighting, entity counting and
> cadence are all frozen until promote flags are recorded.

### Block 2 — feed

The most recent `feed/_reports/` cycle report, copied verbatim, followed by the
unflagged items from `items.yaml` rendered as a plain list — headline, one-clause
`why`, date, URL, lane, item id. Newest first. Provisional and exploration lanes
labelled but not separated.

Cap at 40 items. When capped, say so and give the count withheld.

### Block 3 — panel

The most recent `ratios/_reports/` panel report, copied verbatim. Including its
§5 warning in full — the warning is not deduplicated, abbreviated, or replaced with
a reference.

---

## 3. Cadence

Regenerated after every feed cycle and after every panel refresh, whichever fires.
The digest has no schedule of its own.

---

## 4. No notifications

No email, no webhook, no desktop notice, no message to any external service. The
digest is a file at a known path. Anything that pushes is out of scope and must be
reported rather than built.

---

## 5. Out of scope — stop and report if reached

- summarising, paraphrasing, ranking, or flagging any item or figure
- any evaluative language beyond the single `starved` state
- writing to `feed/`, `ratios/`, or any human-owned file
- inferring promote flags, or pre-filling any `promote` field
- reading `ratios/readings.md`
- notifications of any kind

---

## 6. Acceptance

Complete when: `DIGEST.md` generates from a live feed cycle and a live panel run;
the state block computes correctly against a hand-checked `items.yaml`; the
previous digest is archived to `_digest/` before overwrite; the panel warning
appears in full; a simulated three-cycle run with zero promotes produces the
`starved` state and its fixed line; and the output contains no sentence not copied
verbatim from a source report or generated from the fixed templates above.
