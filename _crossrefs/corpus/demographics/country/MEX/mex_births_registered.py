"""
Mexico registered births, 2015-2024 (ENR definitive) — 2026-Q3 companion plot.

Data: INEGI, Estadistica de Nacimientos Registrados (ENR), series as
published in Comunicado de prensa 129/25 (25 sep 2025), grafica 1.
Registered (not occurred) births; the 2020 trough is dominated by
pandemic registration disruption, and the 2021-2022 rebound includes
late registrations of 2020 births.

The dashed reference line marks the 1.70 M Rule-of-85 trigger set by the
2026-Q2 replicate §10: below it, the long-run stationary population
(births x e0) falls materially under the Central-scenario 2050
projection. The 2024 definitive figure (1.672 M) breached it — the
load-bearing finding of the 2026-Q3 replicate.

Run from the dalila env:
    ~/miniforge3/envs/dalila/bin/python mex_births_registered.py
"""

from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).parent
OUT_PNG = HERE / "mex_births_registered.png"

# INEGI ENR, Comunicado 129/25, grafica 1 (registered births)
YEARS = list(range(2015, 2025))
BIRTHS = [
    2_353_596, 2_293_708, 2_234_039, 2_162_535, 2_092_214,
    1_629_211, 1_912_178, 1_891_388, 1_820_888, 1_672_227,
]

TRIGGER_M = 1.70  # Q2 replicate §10 Rule-of-85 sensitivity threshold

SERIES = "#2a78d6"     # single-series blue (light surface)
INK = "#1f1f1e"        # primary text
MUTED = "#6b6b68"      # secondary text / reference elements
GRID = "#e4e4e1"


def main() -> None:
    births_m = [b / 1e6 for b in BIRTHS]

    fig, ax = plt.subplots(figsize=(9, 5.4), dpi=150)

    ax.axhline(TRIGGER_M, color=MUTED, lw=1.2, ls=(0, (5, 4)), zorder=1)
    ax.annotate("Rule-of-85 trigger: 1.70 M  (2026-Q2 replicate §10)",
                xy=(2015.0, TRIGGER_M), xytext=(0, 6),
                textcoords="offset points", color=MUTED, fontsize=8.5)

    ax.plot(YEARS, births_m, color=SERIES, lw=2, zorder=3,
            marker="o", ms=5, mfc=SERIES, mec="white", mew=1.2)

    # Selective direct labels: endpoints + the breach year only.
    ax.annotate(f"{births_m[0]:.2f} M", xy=(YEARS[0], births_m[0]),
                xytext=(0, 10), textcoords="offset points",
                ha="center", color=INK, fontsize=9)
    ax.annotate(f"{births_m[-1]:.2f} M\n(definitive, −8.2% vs 2023)",
                xy=(YEARS[-1], births_m[-1]), xytext=(4, -30),
                textcoords="offset points", ha="right",
                color=INK, fontsize=9, fontweight="bold")
    ax.annotate("pandemic\nregistration trough", xy=(2020, births_m[5]),
                xytext=(0, -28), textcoords="offset points",
                ha="center", color=MUTED, fontsize=8.5)

    ax.set_title("Mexico — registered births, 2015–2024",
                 loc="left", fontsize=13, color=INK, pad=14)
    ax.text(0, 1.015, "INEGI ENR, Comunicado 129/25 (definitive 2024) · registered ≠ occurred",
            transform=ax.transAxes, color=MUTED, fontsize=9)

    ax.set_ylabel("Births (millions)", color=INK, fontsize=10)
    ax.set_xticks(YEARS)
    ax.set_ylim(1.45, 2.5)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.grid(axis="y", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)

    fig.text(0.01, 0.01,
             "1.672 M births × e₀ 75.63 (CONAPO 2026) → stationary population ≈ 126.5 M, "
             "vs. Central-scenario 2050: 140.4 M.",
             color=MUTED, fontsize=8.5)

    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(OUT_PNG, facecolor="white")
    print(f"Wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
