# Fixture archetypes — self-contained; never references the real archetypes.md.

Poles for fixture use: `[pure-diffusion-integrator]`, `[multi-path-hedger]`,
`[tempo-skeptic]`. The retired pole `[transition-tempo-skeptic]` is deliberately
mentioned here in prose — the prose is not the registry, and a parser that scanned
it would wrongly accept the retired slug (the §3 trap).

<!-- SLUG-REGISTRY-BEGIN -->
```yaml
active:
  - pure-diffusion-integrator
  - multi-path-hedger
  - tempo-skeptic
retired:
  - transition-tempo-skeptic   # split 2026-07-24 → multi-path-hedger + tempo-skeptic
```
<!-- SLUG-REGISTRY-END -->
