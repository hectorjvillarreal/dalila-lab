# Automotive archetypes (instance)

*Human-owned. Tools treat `archetype_ref` as a read-only pointer into this file. Text
below is verbatim from the source board (loaded 2026-06-21 onward) except where a pole
has been repaired; repairs are dated and record what they replaced. Slugs in brackets
are the anchors entry YAML points at.*

*Schema note (2026-07-24): after unbundling, a player routinely holds more than one pole.
`archetype_ref` accepts a **list**. `validate.py` must accept list-or-string.*

1. **Pure diffusion integrator** `[pure-diffusion-integrator]` — cost / scale / vertical integration; "good enough" deployed wide. *Setter: BYD.*
2. **~~Span / legitimacy conglomerate~~ — SPLIT 2026-07-24.** The original pole `[span-legitimacy-conglomerate]` (*"house of brands across tiers and geographies", setter: Geely*) bundled two properties that H1-2026 drove in opposite directions in the same quarter: Geely **won China on segment span** (Galaxy, in a market down 20.2%) while its **legitimacy assets were being selectively denied** in Washington (Polestar out, Volvo in). One property rose as the other was revoked. The slug `span-legitimacy-conglomerate` is retired; do not reuse.
    - **2a · Segment-span conglomerate** `[segment-span-conglomerate]` — product breadth across price bands, carried on shared architecture. A **portfolio** property, owned outright and exercised at will. *Falsifiable content:* whether breadth actually buys resilience when a market contracts. *Exemplars:* **Geely** (Galaxy → Lynk & Co → Zeekr → Volvo/Lotus, on SEA) · **VW Group** (Škoda/Cupra → Audi → Porsche/Bentley) — *note VW sits here too; see the standing repair on pole 5*.
    - **2b · Acquired legitimacy** `[acquired-legitimacy]` — market access obtained by *buying* foreign marques, plants and standards position, where the player's own nationality would otherwise gate it. **Not owned — conferred, per-marque, revocable, adjudicated.** *Falsifiable content:* whether an authorization is granted, survives, and covers the marques that carry volume. *Exemplars:* **Geely** (Volvo authorized US May 2026; **Polestar denied** MY2027; Lotus/smart untested) · **SAIC/MG** *(candidate second exemplar — a British marque as the European access vehicle; see standing repairs)*. *Negative exemplar:* **BYD** — deliberately holds none, betting cost dominance makes legitimacy unnecessary.

    **2b has a restricted domain — this is not a defect.** The pole applies only to players whose **nationality gates their market access** (`findings.md#integration--legitimacy--for-chinese-capital-only`). For a Western incumbent, acquired legitimacy is not *low*, it is **not applicable**; for Hyundai it is not applicable for the opposite reason — its legitimacy is **native, not acquired**. Hence **no 2a×2b grid**: the axes do not share a domain, and forcing one would read "not applicable" as "zero". *(Contrast 4a×4b, where both axes are defined for every player and the grid is therefore legitimate.)*
3. **Compute-first entrant** `[compute-first-entrant]` — comes at the car from the software/AI side. Two faces: stack-supplier (Huawei) vs ecosystem-OEM (Xiaomi). *Western, vertically-integrated version: Tesla.*
4. **~~Transition-tempo skeptic~~ — SPLIT 2026-07-24.** The original pole `[transition-tempo-skeptic]` (*"incumbent betting the transition is slower than the challengers assume", setter: Toyota*) was defined by a single exemplar and inherited that exemplar's incidental correlations. Two contacts with data separated the components: **2026-07-14** (Hyundai holds the hedge without the skepticism) and **2026-07-20** (JAMA — Toyota's answer to competitive pressure is a cost-structure move, not a tempo claim). **Resolved as two firm-level axes and one cross-level variable — not three poles.** The slug `transition-tempo-skeptic` is retired; do not reuse.
    - **4a · Multi-path hedger** `[multi-path-hedger]` — maintains genuine capability across several powertrain paths rather than committing to one. A **capability** property, observable in product lines and R&D allocation. *Falsifiable content:* portfolio breadth, and the share of profit that survives any single path failing. *Exemplars:* **Toyota** (HEV/PHEV/BEV/hydrogen) · **Hyundai** (multi-path plus a real BEV platform, E-GMP). **Born with two exemplars** — the anti-bundling cure applied at creation rather than after the crack.
    - **4b · Tempo skeptic** `[tempo-skeptic]` — holds that the BEV transition is slower, messier and more infrastructure-bound than the challengers price, and **allocates accordingly**. A **belief** property, observable in where capital and capacity actually go, not in what is said. *Exemplars:* **Toyota** (high — Toyoda's ~30% BEV ceiling, deliberate ramp, solid-state slipped 2020→23→26→27-28) · **Great Wall** (high, and **eliminated** — NEV ~30% of domestic sales against an industry level >63%; out of China's top-ten domestic retail, H1-2026) · **Hyundai** (low — hedges without disbelieving).
5. **Declining span / adapting incumbent** `[declining-span-adapting-incumbent]` — incumbent house-of-brands on the back foot, restructuring under the wave. *Setter: VW Group.* **⚠ Flagged 2026-07-24, not repaired:** post-2a this may not be an archetype at all — it may be **2a plus a trajectory plus incumbent status**. VW would then be a segment-span conglomerate in decline, not a distinct kind of player. See standing repairs.
6. **Frontier disruptor** `[frontier-disruptor]` — software/autonomy-first; changing the battlefield off unit-cost. *Setter / board origin: Tesla.*

## The 4a × 4b grid (2026-07-24)

The split adds no players. It re-reads existing entries — and produces a discrimination
the bundled pole could not make: **Toyota and Hyundai were indistinguishable under the
old pole 4; they are now one cell apart.**

|  | **Hedge high (4a)** | **Hedge low** |
|---|---|---|
| **Skeptic (4b high)** | **Toyota** — buffered; the wager has paid once | **Great Wall** — *eliminated in a fast-transition market* |
| **Non-skeptic (4b low)** | **Hyundai** — the un-cornered middle (007) | **Tesla / BYD** — committed to one path |

All four cells are occupied by entries already on the board.

**The prediction the grid carries:** *hedge-low + skeptic-high is the failure cell* —
disbelieving the transition without the portfolio to survive being wrong. Great Wall
confirms it. This is the first predictive structure the archetype set has produced, and
it is falsifiable: **a hedge-low skeptic that survives a fast-transition market would
break it.**

*No equivalent grid exists for 2a×2b — see the domain-restriction note under pole 2.
**Grids are legitimate only where both axes are defined for every player.***

## Cross-level variables — not archetypes

Recorded here so they are not mistakenly entered as poles (cf. the rejected
"export-channel pole", and `findings.md#the-level-limitation`).

- **Coordination capacity** *(surfaced 2026-07-20 as the third component of old pole 4;
  filed here 2026-07-24)* — the capacity to restructure at **industry or national**
  level rather than firm level. **Environmentally gated**: Japan has an association
  tradition and gets JAMA standardisation; Germany has co-determination and gets
  paralysis presented as a model-range cut; China has state standard-setting; the US has
  regulatory power over market access. The *act* is firm-level — Toyota placed its
  former CEO in the JAMA role — but its *availability* is not. Filing it as a firm
  archetype would attribute an institutional endowment to a corporate strategy, which is
  the category error the VW finding warns against (`findings.md#shakeouts-have-institutional-forms`).
  **Strongest evidence yet for opening a coalition register.**

## Mixtures `[mixture]`

Entry 007 (Hyundai Motor Group) is *not a corner — the board's first genuine mixture.
Control case for the incumbent axis.* Mixtures carry qualitative loadings **in prose
only** (see the entry's prose file); loadings are never computed, stored numerically, or
suggested by a tool (build doc §8; cf. `scaffold/discipline.md#poles-unbundle`).

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

## Standing repairs (human backlog — not tool work)

- ~~Split the Toyota pole three ways.~~ **Done 2026-07-24** — resolved as **two axes
  plus one cross-level variable**, not three poles. Recorded because the correction
  matters: a component that operates at a different level must not be entered as a pole.
- ~~Split the Geely pole.~~ **Done 2026-07-24** — resolved as **two axes with different
  domains**. Recorded because this too was unanticipated: a repair can yield axes that
  are not jointly defined, and the honest output is *no grid* rather than a grid with
  "not applicable" scored as zero.
- **NEW — pole 5 may not be a pole.** Post-2a, "declining span / adapting incumbent"
  looks like *2a + trajectory + incumbent status*. Do not repair in the same pass as the
  splits that raised it; wait for a player that forces the question. *Note the pattern:
  each repair has surfaced the next one.*
- **2b is single-exemplar and therefore vulnerable to exactly the defect just repaired.**
  Priority second exemplar: **SAIC/MG** — same pole, different player, and already on the
  pair-completion list. This is now a specific reason to prioritise it, not a general one.
- Pair-completion cohort — a second exemplar per pole. *Single-exemplar poles inherit
  their setter's incidental correlations; entry 003 is the only original two-exemplar
  pole and the only one that never cracked — 4a is now the second, by construction.*
  Candidates: Leapmotor; Chery + SAIC as an SOE / stack-partner pair.
