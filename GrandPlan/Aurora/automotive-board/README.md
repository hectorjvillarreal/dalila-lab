# Automotive Player Board — maintenance repo

**"Automotive" means cars — the motor vehicle industry. It has never meant *automated*.**
(The word "auto" is retired from this project's vocabulary; if you meet it in an older
document it is ambiguous — stop and ask, do not infer.)

> **The one rule: facts are mechanical and basis-independent → automate.**
> **Classification is judgment and basis-dependent → never automate.**

Enforced structurally: every board entry is a **prose `.md`** (archetype, loadings, the
bet, the reading, watch items, status — human-owned, no tool write path) plus a
**facts `.yaml`** (slot values, dates, sources, confidence — tool-writable). The tool
cannot cross the line because the format gives it nowhere to write.

Built 2026-07-24 per `20260724_AURORA_BUILD_automotive-board-tooling_v1.1.md`.

---

## Layout

```
automotive-board/
├── README.md
├── CLAUDE.md                     # session fence — provided, do not edit
├── scaffold/                     # INVARIANT. Portable to other industries.
│   ├── entry-template.md
│   ├── slot-registry.yaml
│   ├── pipeline.md
│   └── discipline.md
├── instances/
│   └── automotive/
│       ├── archetypes.md         # the six poles + the mixture note (human-owned)
│       ├── findings.md           # instance findings, verbatim from the board
│       ├── board/                # 7 entries × (prose .md + facts .yaml)
│       ├── feed/
│       │   ├── inbox.md
│       │   ├── absorbed.yaml     # dedupe ledger
│       │   └── promoted/
│       └── thresholds.yaml
└── tools/
    ├── validate.py               # schema, pairing, boundary check, scaffold purity
    ├── thresholds.py             # overdue / due-soon report; due_passed maintenance
    ├── betcheck.py               # decisive-slot movement flags (never verdicts)
    ├── feed.py                   # Job 1 (dedupe/absorb) + Job 2 (slot writes; --fetch off by default)
    ├── reconstruct.py            # migration completeness pass (acceptance §9)
    └── requirements.txt
```

## The three jobs

1. **Feed maintenance** (`tools/feed.py`) — one-line items (date · why it might matter ·
   URL) in `feed/inbox.md`. Dedupe against `feed/absorbed.yaml` (URLs normalised before
   comparison). The tool may flag a watch-item string match; **promotion is a human call.**
   The feed is deliberately looser than the wider corpus protocol and explicitly
   **outside PROTO-RAG-001 scope** — no corpus frontmatter here, ever.
2. **Slot maintenance** (`tools/feed.py slot-update`) — writes only the writable fields
   (`value, unit, delta, date, source, source_type, confidence`) inside `slots.*`.
   Network fetching exists behind `--fetch`, **off by default** (activation is Héctor's
   open decision). One slot write = one commit, once git is wired (see below).
3. **Thresholds & bet-status** (`tools/thresholds.py`, `tools/betcheck.py`) —
   mechanical date checks and decisive-slot movement flags. **Output is a flag, never a
   verdict.** The tool detects movement; Elle adjudicates meaning.

## Hard prohibitions (build doc §8)

The tooling never: assigns/normalises archetypes · computes loadings, weights, scores or
coordinates · declares a bet alive/dead/stressed · ranks players (**tournament, not
leaderboard**) · writes prose or read-only keys · resolves thresholds · applies corpus
frontmatter to the feed · adds/merges/retires players · "improves" the archetype set,
slot registry, or `discipline.md`.

`validate.py --check-boundary` enforces the write boundary mechanically (fails if any
read-only key changed vs the baseline). Wire it as a pre-commit hook once git is set up.

## Git status of this build

This session was instructed to run **no git commands**; the tree is uncommitted for
Héctor's review. Post-acceptance: `git init` (local only, no remote), commit conventions
per build doc §7 (`slot(NNN):` · `feed:` · `threshold(TH-NNN):` · `prose(NNN):` ·
`scaffold:` · `tool:`), and `validate.py --check-boundary` as pre-commit hook. Until git
exists, the boundary check compares against `.boundary-baseline.json`
(refresh with `validate.py --snapshot` after each *intended* human change).

## Migration conventions (recorded for audit)

- Prose copied verbatim; the "Data slots" block of each entry moved to the paired
  `.yaml`; judgment halves of mixed slot lines retained verbatim in the prose file under
  "Data slots — judgment retained".
- Slot `date` is the board's log/as-dated stamp, not the underlying publication date.
- No source URLs existed in the v1 board: migrated slots carry `source: null`,
  `source_type: null` with a note, and `confidence: reported` (promotion to `confirmed`
  is a later, sourced act). Slots the board marked "(feed)" have `value: null`.
- `notes` fields in YAML are **read-only** (human-set at migration): factual remainders
  of multi-fact slot lines. Nothing was discarded; the completeness pass
  (`tools/reconstruct.py`) verifies token-level coverage against the source board.
