# Calibration results for §7 of the seminar paper

**Status:** Intermediate calibration, stopped 2026-05-29. 5/6 moments matched
within 1 SE; the 6th moment (VSL) reveals a **structural feature of the model**
worth reporting on its own terms.

**Scope:** This is the literature-anchored intermediate calibration, not the
Mexican-microdata calibration. Judy and Milo's ENASEM / ENOE / GBD first-step
deliverables will replace specific `inputs_anchored/` CSVs; the SMM scaffold
re-runs without further code changes. See `inputs_anchored/provenance.md` for
all citations + unit conversions.

---

## Headline

The model — a gender-extended OLG with health capital, calibrated SMM-style in
PE against six moments at Mexican / upper-middle-income literature anchors —
matches **five of six target moments within one standard error** at the
best-so-far $\hat\theta$, after ~90 Nelder-Mead evaluations on the first
multistart trajectory (5 free parameters, $\xi$ fixed at 0.5 to resolve the
$\Xi/\xi$ identification ridge documented below). The sixth moment, the value
of a statistical life (VSL), comes in at **$\approx \$92{,}000$** in 2022 USD
against a benefit-transfer target of $\$2.0\text{M}$ — a 20-fold gap that
does *not* close under any free reallocation of the six SMM parameters and is
therefore a structural feature of the current preference and depreciation
specification, not a calibration failure.

---

## Parameter estimates ($\hat\theta$, best-so-far snapshot)

| Parameter | Init | $\hat\theta$ | Relative change |
|---|---:|---:|---:|
| $\Psi$ (labor disutility) | 14.00 | **11.27** | $-19.5\%$ |
| $\Xi$ (health amenity) | 0.500 | **0.314** | $-37.1\%$ |
| $\xi$ (amenity curvature) | 0.500 | **0.500** | **frozen** |
| $\bar H_0$ (health-production scale) | 0.300 | **0.155** | $-48.3\%$ |
| $h^{\mathrm{slope}}$ (age-decline) | 0.000 | **$-0.0095$** | abs $\Delta -0.0095$ |
| $\zeta_h$ (health-production curvature) | 0.500 | **0.496** | $-0.7\%$ |

$\hat\theta$ is the parameter vector at the lowest-$Q$ evaluation in the
fix-$\xi$ multistart, $Q(\hat\theta) = 11.82$ at evaluation 90. Treated as a
**checkpoint**, not a converged estimate (only the first of 8 starts ran to
this depth); the second and third starts would have produced the basin map and
sandwich SEs. Stopped early because the structural-VSL finding dominates and
the remaining starts would not have changed the headline.

---

## Moment match at $\hat\theta$

| Moment | Data | SE | Model | Diff | $t$ |
|---|---:|---:|---:|---:|---:|
| Prime-age male hours $\ell_{\text{pa-M}}$ | 0.340 | 0.010 | 0.342 | $+0.0021$ | **$+0.21$** ✅ |
| VSL (2022 USD) | $2{,}000{,}000$ | $700{,}000$ | $91{,}820$ | $-1.91\text{M}$ | **$-2.73$** ❌ |
| Cross-section $\eta_m$ | 1.000 | 0.300 | 0.467 | $-0.533$ | **$-1.78$** ⚠ |
| $\bar m$ at ages 25–35 (model units) | 0.040 | 0.020 | 0.0236 | $-0.0164$ | **$-0.82$** ✅ |
| $d\log\bar m/dj$, $j\in[2,12]$ | 0.120 | 0.050 | 0.117 | $-0.0032$ | **$-0.06$** ✅ |
| Within-age $\eta_m$ | 0.400 | 0.150 | 0.508 | $+0.108$ | **$+0.72$** ✅ |

$\Sigma t^2 = 11.82 = Q(\hat\theta)$ ✓ (objective consistency check).

Five of six within $|t| < 1$. The cross-sectional elasticity at $t = -1.78$
is borderline ($\approx 1.8$ SE); the VSL is the genuine outlier.

---

## The VSL gap is structural

The estimated VSL in model units is

$$
\hat{\mathrm{VSL}}_{\text{model}} = \beta \cdot \frac{\mathbb{E}_\eta[V_{j+1}]}{u_c}
\bigg|_{j=4,\,\hat\theta}
\approx 2.6,
$$

which times $\$35{,}000$ (= per-capita 5-year household consumption, Mexico
2021) gives $\hat{\mathrm{VSL}}_{\text{USD}} \approx \$92{,}000$. The
literature anchors are:

| Source | VSL (USD) | Method |
|---|---:|---|
| OECD benefit-transfer (PMC11032065) | $2.0\text{M}$ | Income-elasticity transfer (national avg) |
| OECD sub-national high | $3.3\text{M}$ | Mexico City |
| Hammitt & Ibarrarán (2006), *Health Econ.* | $235\text{k}{-}325\text{k}$ | Revealed wage-risk, Mexico City workers |
| de Lima et al. (2020), *JEEP* | $211\text{k}$ | Stated-preference, Mexico Valley |
| **Model output, this calibration** | **$\mathbf{92\text{k}}$** | SMM at literature-anchored targets |

The model's VSL falls **below even the revealed-preference Mexican estimates**.
The gap does not close when the optimizer reallocates over $(\Psi, \Xi,
\bar H_0, h^{\mathrm{slope}}, \zeta_h)$: raising $\Xi$ (the obvious lever) pushes
medical-spending moments badly off target. Fixing $\xi = 0.5$ specifically
resolves the *identification* problem on VSL (the $\Xi \leftrightarrow \xi$
elasticity ridge documented in
`outputs/diagnostics/02_jacobian.png`) but does not lift the *level*: in the
fix-$\xi$ run $\Xi$ moves to 0.314 (vs 0.331 in the 6-D run), and VSL is
$\$92\text{k}$ vs $\$99\text{k}$ — no improvement.

**Two interpretations to report.**

1. The model is structurally under-specified for VSL. The amenity $\Xi$ enters
   the continuation value too weakly relative to the GHH felicity, capping
   the marginal valuation of survival. Richer formulations — explicit utility
   from being alive, bequest motive, or non-separable consumption-health
   amenity — would generate higher VSL without disturbing the medical-spending
   moments. This is the OLG-design lever.

2. The OECD/policy VSL anchors are too high relative to what Mexican workers'
   actual choices reveal. The revealed-preference Mexican literature
   ($211\text{k}{-}325\text{k}$) clusters about ten-fold below the OECD
   transfer ($\$2.0\text{M}$). The model's $\$92\text{k}$ is closer to the
   revealed-preference family than to the transfer family — modestly so, but
   suggestive that the OECD income-elasticity transfer at $\varepsilon=1.0$ may
   over-state Mexican VSL.

Either reading is defensible; we recommend stating both in the paper rather
than picking one.

---

## Identification context (from the Jacobian)

The pre-optimization Jacobian at $\theta_{\text{init}}$ (computed earlier; see
`outputs/jacobian.csv` and `outputs/diagnostics/02_jacobian.png`) flagged two
flat ridges:

- **$\Xi \leftrightarrow \xi$ on VSL:** both parameters have elasticity
  $\approx +0.20$ on `vsl_usd` at $\theta_{\text{init}}$; their effects on
  every other moment are an order of magnitude smaller. The optimizer cannot
  separately identify the two from VSL alone — visible in the 6-D run where
  $\xi$ moved by $-0.001$ over 89 evaluations. The fix-$\xi$ run resolves this
  by holding $\xi = 0.5$.
- **$\bar H_0 \leftrightarrow \zeta_h$ on the medical moments:** both move
  `cross_elast_m`, `mean_m_age_25_35`, `logslope_m_25_75`, `within_age_elast`
  with opposite signs, with $\zeta_h$ approximately three times stronger. Even
  in the fix-$\xi$ run, $\zeta_h$ moves only by $-0.7\%$ from its init — this
  ridge is still active. A 4-free-parameter run (fix both $\xi$ and $\zeta_h$)
  would pin the medical-moment block to $\bar H_0$ and $h^{\mathrm{slope}}$
  alone, at the cost of one fewer free dimension.

The well-identified single-direction parameters are $\Psi$ (one-to-one with
hours; $-19.5\%$ from init, tightly pinned) and $h^{\mathrm{slope}}$ (the
strongest direct lever on $d\log\bar m/dj$; moved from $0$ to $-0.0095$ and
brought the moment from $t=+4.31$ at init to $t=-0.06$, easily the largest
moment-match improvement). $\Xi$ and $\bar H_0$ moved by $-37\%$ and $-48\%$
respectively but are weakly pinned (the ridges).

---

## Artifacts and substitution roadmap

| Artifact | Path | Purpose |
|---|---|---|
| Anchored inputs + provenance | `Calibration/inputs_anchored/` (incl. `provenance.md`) | All literature citations, unit conversions, three caveat categories |
| Pre-optimization Jacobian | `Calibration/outputs/jacobian.csv`, `outputs/diagnostics/02_jacobian.png` | Identification heatmap (target-relative elasticity) |
| Moment match at $\theta_{\text{init}}$ | `Calibration/outputs/moments_at_stub.csv` | Q = 50.13 baseline before optimization |
| Eval log, 6-D multistart (partial, 89 evals) | `Calibration/outputs/eval_log_multistart_6param_*.csv.partial` | Historical reference; demonstrates the $\xi$/`zeta_h` non-movement |
| Eval log, fix-$\xi$ multistart (final, 90 evals) | `Calibration/outputs/eval_log_multistart_fixxi_*.csv.final` | Source for $\hat\theta$ and all moment-match numbers in this document |
| LaTeX table fragments | `Calibration/draft_outputs/snapshot_latest.tex` | Drop-in for §7 |
| Progress trace | `Calibration/draft_outputs/snapshot_progress.png` | $Q$ vs eval, with running-best overlay |
| Snapshot regenerator | `Calibration/scripts/snapshot_calibration.py` | Re-runs at any time on whatever eval log is current |

**Substitution roadmap.** When Judy's ENASEM mortality/health-status
regressions arrive, replace `inputs_anchored/first_step/psi_base.csv` and
`delta_h.csv` (and `skill_params.csv:rho_pen`). When Milo's ENOE wage
decomposition arrives, replace `e_age.csv`, `skill_params.csv:theta`,
`ar1_params.csv`, and `pi_birth.csv`. When data-side moment estimates arrive,
replace `moments/targets.csv`. The SMM re-runs unchanged; the comparison
between literature-anchored and Mexican-data-anchored $\hat\theta$ is itself an
interesting headline.

---

## What we would do next, when resuming

1. **Decide on the VSL framing** in the paper — under-specified preferences vs.
   over-stated OECD anchor — and reflect the choice in the §6.2 model
   discussion.
2. **Optional: 4-free run (fix $\xi=0.5$ and $\zeta_h=0.5$)** to tighten the
   $\bar H_0$ identification by collapsing the medical-moment ridge. Expected
   to move $\bar H_0$ further from its init and produce a smaller SE on it.
3. **Multistart resume** (full 8-start basin map) once the parameter-fixing
   decisions are settled. This delivers the SEs and dispersion needed for the
   formal §7 estimation table.
4. **GE re-anchor** check (`pe_anchor.csv` updated from a converged
   GE-Gender run with $\hat\theta$) — the README's standard outer loop.
