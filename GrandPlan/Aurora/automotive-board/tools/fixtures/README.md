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

Dangling and retired fail with **distinct messages** — a checker that only ever
passes is indistinguishable from one that does nothing.

The `no-registry` and `retired` prose deliberately mentions valid-looking and retired
slugs in backticks/brackets: if the validator ever regressed to scanning prose, those
cases would go green. They must stay red.

A test never mutates the artifact under protection (v1.1 §1). New rule → new fixture
case here, not a temporary edit to a real entry.
