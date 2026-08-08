# Fixture archetypes (orphan-slug variant) — the registry's `active` list contains one
# slug that the prose never names. Expected: pass, with a Rule D warning for that slug.

Poles in prose: `[pure-diffusion-integrator]`, `[multi-path-hedger]`, `[tempo-skeptic]`.

<!-- SLUG-REGISTRY-BEGIN -->
```yaml
active:
  - pure-diffusion-integrator
  - multi-path-hedger
  - tempo-skeptic
  - ghost-pole
retired:
  - transition-tempo-skeptic   # split 2026-07-24 → multi-path-hedger + tempo-skeptic
```
<!-- SLUG-REGISTRY-END -->
