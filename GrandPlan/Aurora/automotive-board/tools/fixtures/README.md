# Fixtures — archetype_ref rules (build doc 20260726_AURORA_BUILD_validate-archetype-refs_v1.1 §4)

Each case is a self-contained mini-tree; none references the real `archetypes.md`.
Run any case with:

    python3 tools/validate.py --root tools/fixtures/<case>

| Case | `archetype_ref` | Expected |
|---|---|---|
| `valid-string/` | `"pure-diffusion-integrator"` | pass (exit 0) |
| `valid-list/` | `["multi-path-hedger", "tempo-skeptic"]` | pass (exit 0) |
| `dangling/` | `"not-a-real-pole"` | fail — dangling pointer (Rule B) |
| `retired/` | `"transition-tempo-skeptic"` | fail — RETIRED, quoting the registry comment (Rule C) |
| `empty-list/` | `[]` | fail — must be non-empty (Rule A) |
| `no-registry/` | valid slug, but `archetypes.md` has no SLUG-REGISTRY markers | fail loudly — no prose fallback (§3 trap) |
| `orphan-slug/` | valid slug; registry lists `ghost-pole`, prose never names it | pass with Rule D warning |
| `null-ref/` | `null` | **passes (exit 0) — characterisation, not endorsement.** See below. |

Dangling and retired fail with **distinct messages** — a checker that only ever
passes is indistinguishable from one that does nothing.

## `null-ref/` — a documented gap, not a passing rule

`archetype_ref: null` currently validates clean. Two checks each assume the other
covers it:

- `check_entry_schema` tests `ENTRY_TOP_KEYS - set(data)`, which asks only whether the
  **key** is present. `archetype_ref: null` has the key, so nothing fires.
- `check_archetype_ref` returns early on `if ref is None`, commented *"absence already
  reported by the schema check"* — which is true for a missing key and false for a
  null value.

So an entry can carry no archetype pointer at all and the board still reports green.
Compare `empty-list/`, where `[]` is a hard error: the two express the same thing and
are treated oppositely.

This fixture pins the **current** behaviour so that a future change is visible as a
change. It does **not** assert that null should pass. Whether null becomes an error
(Rule A) or stays legal is a rule decision for the build doc's author, not a tool fix —
if the rule changes, this row moves to *fail* and the fixture keeps earning its place.

Found 2026-08-08 while reading the `tools/validate.py` diff during the v1.1 §8
independent check — i.e. by the check specifically designed not to route through the
agent's self-report.

The `no-registry` and `retired` prose deliberately mentions valid-looking and retired
slugs in backticks/brackets: if the validator ever regressed to scanning prose, those
cases would go green. They must stay red.

A test never mutates the artifact under protection (v1.1 §1). New rule → new fixture
case here, not a temporary edit to a real entry.
