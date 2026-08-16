# DIGESTER.md — companion to digest.py

**Build instruction:** `20260816_AURORA_BUILD_pharma-digest-layer_v1.0` (in `pharma_board/`).
**A concatenation and a counter. Nothing else.**

`python digest.py build` regenerates `DIGEST.md` — run it after every feed
cycle and after every panel refresh; the digest has no schedule of its own and
sends no notifications. The previous digest is archived to
`_digest/YYYYMMDD_HHMM_digest.md` before overwrite, so the surface stays single
while the record stays complete.

## What DIGEST.md contains — and provably nothing more

1. **State block** — pure arithmetic over `feed/items.yaml`,
   `feed/queries.yaml`, `ratios/roster.md`, and report filenames. The only
   evaluative word in the whole surface is `starved` (three or more completed
   cycles with zero promote flags recorded); it describes the system, never
   the industry, and carries the fixed frozen-calibration line beneath it.
2. **Feed block** — the latest `feed/_reports/` cycle report copied verbatim,
   then the unflagged items rendered from their `items.yaml` fields (headline,
   why, date, URL, lane, id), newest first, provisional and exploration
   labelled but not separated. Capped at 40 with the withheld count stated.
3. **Panel block** — the latest `ratios/_reports/` panel report copied
   verbatim, §5 warning included in full, never abbreviated.

No sentence in the output is authored at digest time: every line is verbatim
source text, a verbatim item field, or a fixed template filled with counts and
dates. The digest never summarises, ranks, highlights, or characterises, and
never touches a promote field.

## Boundary

Writes only `DIGEST.md` (overwrite) and `_digest/` (create-new). Writing into
`feed/`, `ratios/`, human-owned files, or outside `pharma/` is refused, as is
reading `ratios/readings.md` in any mode. `python digest.py selftest-boundary`
demonstrates all of it. Source reports remain authoritative and untouched.
