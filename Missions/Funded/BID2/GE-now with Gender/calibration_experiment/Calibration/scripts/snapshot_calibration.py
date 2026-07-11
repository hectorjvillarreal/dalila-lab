#!/usr/bin/env python3
"""
snapshot_calibration.py — draft-ready snapshot of the SMM calibration state.

Reads an eval_log produced by run_calibration.jl (smoke / jacobian / multistart
modes) and produces:

  draft_outputs/snapshot_latest.md   — markdown report (best-so-far θ̂,
                                       moment match, identification notes)
  draft_outputs/snapshot_latest.tex  — LaTeX table fragments for the paper
  draft_outputs/snapshot_progress.png — Q over evaluation index (PNG)
  draft_outputs/snapshot_<UTC_TS>.md/.tex — timestamped frozen copies

Usage:
    python3 Calibration/scripts/snapshot_calibration.py [eval_log_path]

If no path is given, the script tries (in order):
    outputs/eval_log_multistart.csv
    outputs/eval_log_jacobian.csv
    outputs/eval_log_smoke.csv

The script reads the *current* file contents — safe to run at any time during
a live multistart; it never modifies the eval_log itself. The "best-so-far" is
the row with the minimum finite objective. Treat its θ̂ as a CHECKPOINT, not as
a converged estimate, unless the run completed.

Citations / context for the draft sections produced here live in
inputs_anchored/provenance.md (the literature anchors for the moment targets
and first-step inputs).
"""

from __future__ import annotations
import csv
import sys
import datetime
from pathlib import Path

# ───────────────────────── Locate roots ─────────────────────────────────────
CAL = Path(__file__).resolve().parent.parent           # .../Calibration
OUT = CAL / "outputs"
ANC = CAL / "inputs_anchored"
STUB = CAL / "inputs"
DRAFT = CAL / "draft_outputs"
DRAFT.mkdir(exist_ok=True)


def read_csv(path: Path) -> list[dict]:
    return list(csv.DictReader(open(path)))


def f(row: dict, key: str) -> float | None:
    try:
        return float(row[key])
    except (KeyError, TypeError, ValueError):
        return None


# ───────────────────────── Pick the eval_log ────────────────────────────────
def pick_eval_log(argv: list[str]) -> tuple[Path, str]:
    if len(argv) > 1:
        p = Path(argv[1]).resolve()
        return p, _mode_from_name(p.name)
    candidates = [
        ("multistart", OUT / "eval_log_multistart.csv"),
        ("jacobian",   OUT / "eval_log_jacobian.csv"),
        ("smoke",      OUT / "eval_log_smoke.csv"),
    ]
    for mode, p in candidates:
        if p.exists() and p.stat().st_size > 200:  # > header
            return p, mode
    # fall back to whatever exists
    for mode, p in candidates:
        if p.exists():
            return p, mode
    raise SystemExit("no eval_log_*.csv found under outputs/")


def _mode_from_name(name: str) -> str:
    for m in ("multistart", "jacobian", "smoke"):
        if m in name:
            return m
    return "unknown"


# ───────────────────────── Read targets + theta_init ────────────────────────
def read_targets_and_init() -> tuple[dict, list[str], dict, list[str]]:
    tgt_path = (ANC / "moments" / "targets.csv")
    if not tgt_path.exists():
        tgt_path = STUB / "moments" / "targets.csv"
    targets = read_csv(tgt_path)
    tgt = {r["name"]: r for r in targets}
    moment_names = [r["name"] for r in targets]

    ti_path = (ANC / "config" / "theta_init.csv")
    if not ti_path.exists():
        ti_path = STUB / "config" / "theta_init.csv"
    ti_rows = read_csv(ti_path)
    init = {r["param"]: r for r in ti_rows}
    param_names = [r["param"] for r in ti_rows]

    return tgt, moment_names, init, param_names


# ───────────────────────── Build the snapshot ───────────────────────────────
def main() -> None:
    eval_log_path, mode = pick_eval_log(sys.argv)
    rows = read_csv(eval_log_path)
    tgt, moment_names, init, param_names = read_targets_and_init()
    n_evals = len(rows)

    finite = [r for r in rows
              if f(r, "objective") is not None
              and 0 < f(r, "objective") < 1e10]
    n_finite = len(finite)
    best = min(finite, key=lambda r: f(r, "objective")) if finite else None

    utc_now = datetime.datetime.now(datetime.timezone.utc)
    ts_human = utc_now.strftime("%Y-%m-%d %H:%M UTC")
    ts_file = utc_now.strftime("%Y%m%dT%H%M%SZ")

    md = _markdown(mode, eval_log_path, ts_human, n_evals, n_finite, best,
                    tgt, moment_names, init, param_names)
    tex = _latex(mode, ts_human, best, tgt, moment_names, init, param_names)

    (DRAFT / "snapshot_latest.md").write_text(md)
    (DRAFT / "snapshot_latest.tex").write_text(tex)
    (DRAFT / f"snapshot_{ts_file}.md").write_text(md)
    (DRAFT / f"snapshot_{ts_file}.tex").write_text(tex)

    _maybe_plot_progress(rows, mode, ts_human)

    print("=" * 72)
    print(md)
    print("=" * 72)
    print(f"wrote: {(DRAFT / 'snapshot_latest.md').relative_to(CAL.parent)}")
    print(f"wrote: {(DRAFT / 'snapshot_latest.tex').relative_to(CAL.parent)}")
    print(f"wrote: {(DRAFT / f'snapshot_{ts_file}.md').relative_to(CAL.parent)}")
    print(f"wrote: {(DRAFT / f'snapshot_{ts_file}.tex').relative_to(CAL.parent)}")


# ───────────────────────── Markdown report ──────────────────────────────────
def _markdown(mode, eval_log_path, ts_human, n_evals, n_finite, best,
              tgt, moment_names, init, param_names) -> str:
    lines: list[str] = []
    lines.append(f"# Calibration snapshot — {ts_human}")
    lines.append("")
    lines.append(f"**Source:** `{eval_log_path.relative_to(CAL.parent)}`  "
                 f"(mode: `{mode}`)")
    lines.append(f"**Evaluations recorded:** {n_evals}   |   "
                 f"**finite (0 < Q < 1e10):** {n_finite}")
    if best:
        lines.append(f"**Best Q so far:** **`{f(best, 'objective'):.6f}`** "
                     f"(eval `{best['eval_idx']}`, "
                     f"wall `{f(best, 'wall_seconds'):.0f}s`)")
    else:
        lines.append("**No finite evaluations yet — nothing to report.**")
    lines.append("")
    lines.append("> **Treat θ̂ as a checkpoint, not as a converged estimate, "
                 "unless the multistart completed (8 starts × Nelder-Mead "
                 "termination).**")
    lines.append("")

    if not best:
        return "\n".join(lines)

    # θ̂ table
    lines.append("## θ̂ (best-so-far)")
    lines.append("")
    lines.append("| param | init | θ̂ | rel. change |")
    lines.append("|---|---:|---:|---:|")
    for p in param_names:
        i = float(init[p]["init"])
        e = f(best, p)
        if e is None:
            lines.append(f"| `{p}` | {i:.4g} | — | — |")
        else:
            if abs(i) < 1e-9:
                rel = "—" if abs(e) < 1e-9 else f"abs Δ {e:+.3g}"
            else:
                rel = f"{(e - i) / abs(i) * 100:+.1f}%"
            lines.append(f"| `{p}` | {i:.4g} | **{e:.4g}** | {rel} |")
    lines.append("")

    # Moment match
    lines.append("## Moment match at θ̂")
    lines.append("")
    lines.append("| moment | data | SE | model | diff | t-stat |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    Q_recompute = 0.0
    for m in moment_names:
        data = float(tgt[m]["value"])
        se = float(tgt[m]["se"])
        model = f(best, m)
        if model is None:
            lines.append(f"| `{m}` | {data:.4g} | {se:.4g} | — | — | — |")
            continue
        diff = model - data
        t = diff / se
        Q_recompute += t * t
        lines.append(f"| `{m}` | {data:.4g} | {se:.4g} | {model:.4g} | "
                     f"{diff:+.4g} | **{t:+.2f}** |")
    lines.append("")
    lines.append(f"Σ t² (objective consistency check): "
                 f"`{Q_recompute:.4f}` "
                 f"(eval-logged Q: `{f(best, 'objective'):.4f}`)")
    lines.append("")

    # Identification reminder (from the jacobian we already have)
    lines.append("## Identification context")
    lines.append("")
    lines.append("- **Psi → hours_pa_males:** tight one-to-one (clean ID).")
    lines.append("- **Xi ↔ xi:** flat ridge on `vsl_usd` "
                 "(elasticities ≈ +0.20 each); the SMM may settle anywhere "
                 "along it. SEs on Xi and xi should be inspected jointly.")
    lines.append("- **H_0 ↔ zeta_h:** opposite-sign competition on "
                 "`cross_elast_m`, `mean_m_age_25_35`, `logslope_m_25_75`, "
                 "`within_age_elast`; zeta_h is the stronger lever "
                 "(elasticity ~3× H_0).")
    lines.append("- See `outputs/diagnostics/02_jacobian.png` for the "
                 "target-relative elasticity heatmap.")
    lines.append("")

    lines.append("## Provenance for the anchored inputs and targets")
    lines.append("")
    lines.append("Full citations + unit conversions: "
                 "`inputs_anchored/provenance.md`.")
    lines.append("")
    return "\n".join(lines)


# ───────────────────────── LaTeX fragments ──────────────────────────────────
def _latex(mode, ts_human, best, tgt, moment_names, init, param_names) -> str:
    out = []
    out.append(f"% Auto-generated by snapshot_calibration.py — {ts_human}")
    out.append(f"% Eval log mode: {mode}")
    out.append(f"% Best Q so far: {f(best, 'objective'):.6f}"
               if best else "% No finite evaluations.")
    out.append("")

    if not best:
        out.append("% (No finite evaluations to render.)")
        return "\n".join(out)

    # θ̂ table
    out.append(r"\begin{table}[ht]")
    out.append(r"  \centering")
    out.append(r"  \caption{Parameter estimates: best-so-far snapshot "
               r"($\hat\theta$ from the lowest-$Q$ eval; treat as "
               r"checkpoint pending multistart convergence).}")
    out.append(r"  \label{tab:theta_hat_snapshot}")
    out.append(r"  \begin{tabular}{lrr}")
    out.append(r"    \toprule")
    out.append(r"    Parameter & Init & $\hat\theta$ \\")
    out.append(r"    \midrule")
    pretty = {
        "Psi": r"$\Psi$", "Xi": r"$\Xi$", "xi": r"$\xi$",
        "H_0": r"$\bar H_0$", "h_slope": r"$h^{\mathrm{slope}}$",
        "zeta_h": r"$\zeta_h$",
    }
    for p in param_names:
        i = float(init[p]["init"])
        e = f(best, p)
        name = pretty.get(p, p.replace("_", r"\_"))
        out.append(f"    {name} & {i:.4g} & {e:.4g} \\\\")
    out.append(r"    \bottomrule")
    out.append(r"  \end{tabular}")
    out.append(r"\end{table}")
    out.append("")

    # Moment match
    out.append(r"\begin{table}[ht]")
    out.append(r"  \centering")
    out.append(r"  \caption{SMM moment match at $\hat\theta$ "
               r"(best-so-far snapshot).}")
    out.append(r"  \label{tab:moment_match_snapshot}")
    out.append(r"  \begin{tabular}{lrrrrr}")
    out.append(r"    \toprule")
    out.append(r"    Moment & Data & SE & Model & Diff & $t$ \\")
    out.append(r"    \midrule")
    pretty_m = {
        "hours_pa_males":   r"$\ell_{\text{prime-age M}}$",
        "vsl_usd":          r"VSL (2022 USD)",
        "cross_elast_m":    r"$\eta_m^{\text{cross}}$",
        "mean_m_age_25_35": r"$\bar m_{25\text{--}35}$ (model units)",
        "logslope_m_25_75": r"$d\log\bar m/dj$, $j\in[2,12]$",
        "within_age_elast": r"$\eta_m^{\text{within}}$",
    }
    for m in moment_names:
        data = float(tgt[m]["value"])
        se = float(tgt[m]["se"])
        model = f(best, m)
        diff = model - data if model is not None else None
        t = diff / se if diff is not None else None
        name = pretty_m.get(m, m.replace("_", r"\_"))
        if model is None:
            out.append(f"    {name} & {data:.3g} & {se:.3g} & --- & --- & --- \\\\")
        else:
            out.append(f"    {name} & {data:.3g} & {se:.3g} & {model:.3g} & "
                       f"{diff:+.3g} & {t:+.2f} \\\\")
    out.append(r"    \bottomrule")
    out.append(r"  \end{tabular}")
    out.append(r"\end{table}")
    out.append("")

    return "\n".join(out)


# ───────────────────────── Progress trace plot ──────────────────────────────
def _maybe_plot_progress(rows, mode, ts_human):
    if not rows:
        return
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return  # matplotlib not available; skip silently

    Qs = []
    for r in rows:
        q = f(r, "objective")
        if q is not None and 0 < q < 1e10:
            Qs.append(q)
    if not Qs:
        return

    running_best = []
    cur = Qs[0]
    for q in Qs:
        cur = min(cur, q)
        running_best.append(cur)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(range(1, len(Qs) + 1), Qs, "o-", ms=2, lw=0.7,
            color="#888", label="per-eval Q")
    ax.plot(range(1, len(running_best) + 1), running_best,
            lw=1.5, color="C3", label="running best Q")
    ax.set_yscale("log")
    ax.set_xlabel("evaluation index")
    ax.set_ylabel("SMM objective Q (log scale)")
    ax.set_title(f"Calibration progress ({mode}) — {ts_human}")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(loc="best", fontsize=9)
    fig.tight_layout()
    fig.savefig(DRAFT / "snapshot_progress.png", dpi=140)
    plt.close(fig)


if __name__ == "__main__":
    main()
