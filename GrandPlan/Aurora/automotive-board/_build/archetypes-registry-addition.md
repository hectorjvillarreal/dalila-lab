# ADDITION TO `archetypes.md` — apply by hand

**Where:** insert immediately before the `## Standing repairs` section.
**Why by hand:** `archetypes.md` is human-owned; the tool may read it, never write it
(build doc §8, prohibition 9). This block is the single source of truth for slug
validation — kept inside the archetype file rather than a separate registry so the prose
and the machine-readable list cannot drift apart.

---

## Slug registry — machine-readable

*Human-maintained. `validate.py` parses the block below and nothing else in this file.
Retired slugs appear in the prose above as documentation of what was split; **the prose
is not the registry** and must not be parsed for validity.*

<!-- SLUG-REGISTRY-BEGIN -->
```yaml
active:
  - pure-diffusion-integrator
  - segment-span-conglomerate      # 2a, from the 2026-07-24 split of pole 2
  - acquired-legitimacy            # 2b, from the 2026-07-24 split of pole 2
  - compute-first-entrant
  - multi-path-hedger              # 4a, from the 2026-07-24 split of pole 4
  - tempo-skeptic                  # 4b, from the 2026-07-24 split of pole 4
  - declining-span-adapting-incumbent   # flagged 2026-07-24: may not be a pole
  - frontier-disruptor
  - mixture
retired:
  - span-legitimacy-conglomerate   # split 2026-07-24 → segment-span-conglomerate + acquired-legitimacy
  - transition-tempo-skeptic       # split 2026-07-24 → multi-path-hedger + tempo-skeptic
```
<!-- SLUG-REGISTRY-END -->

**Maintenance rule.** When a pole is split, renamed, or retired: move its slug from
`active` to `retired` in the same edit that changes the prose. A retired slug is **never
reused** — reuse would make two different meanings share one pointer across git history,
and the history is the provenance chain.
