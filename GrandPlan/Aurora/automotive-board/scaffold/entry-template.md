# Entry template — invariant

Every board entry is a **pair of files** in `instances/<industry>/board/`:

- `NNN-<player-slug>.md` — **prose, human-owned.** The tool has no write path here.
- `NNN-<player-slug>.yaml` — **facts, tool-writable** (writable fields only; see
  `slot-registry.yaml`).

---

## Prose file structure

```markdown
# Entry NNN — <Player>  ·  *<archetype label, or "mixture">*

**Structure:** <corporate/organisational facts as narrative>
**Span / position:** <where the player sits in the space>
**Distinctive asset:** <what it holds that others cannot easily originate>
**The bet (falsifiable):** <the wager, stated so data can kill it; name the counter-player>
**Loadings (qualitative):** <mixtures only — per-pole nearness, in prose, with reasons.
  Human judgment. Never computed, never numeric.>
**Watch items:** <open questions; geopolitical items tagged to their watcher>
**Data slots — judgment retained:** <the judgment halves of mixed slot lines, kept
  verbatim when facts moved to YAML>
**Status (dated):** <current reading, date-stamped; the field moves fast>
```

Slots are **derived from the bet** — each falsifiable claim names the variables that
confirm or kill it. Those variables become slots in the YAML file, and the ones the bet
hinges on are marked `decisive: true` **by hand**.

## Facts file structure

```yaml
id: "NNN"
player: "<name>"
archetype_ref: "<slug>"        # READ-ONLY pointer into the instance's archetypes.md
slots:
  <slot_name>:
    value: ...                 # tool-writable
    unit: ...                  # tool-writable
    delta: ...                 # tool-writable
    date: ...                  # tool-writable — as-of / log date
    source: ...                # tool-writable — URL or null
    source_type: ...           # tool-writable — primary | secondary
    confidence: ...            # tool-writable — reported | confirmed (upgrade only)
    decisive: false            # READ-ONLY — set by hand from the entry's bet
    notes: ...                 # READ-ONLY — human-set factual remainder
```

## Rules

1. Prose is never rewritten, summarised, tidied, or re-ordered by a tool.
2. A number, date, proper noun, event, or source URL is a fact → YAML. An
   interpretation → prose. Mixed lines split; the judgment half stays in prose.
3. When in doubt, leave it in prose. Under-extraction is recoverable; over-extraction
   silently converts judgment into data.
4. `decisive` is the hinge of the design: it lets the bet-check tool report on a bet
   without ever interpreting one.
5. Every `.md` has exactly one matching `.yaml`, and vice versa.
