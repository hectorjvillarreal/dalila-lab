"""share65_chart.py — chart of the 65+ share from results/projections_national.csv (run projection_national.py first).

One panel, three countries (central path, fertility ±0.2 band), with IBGE's own projection
as a dashed reference line. Labels in Spanish. Palette as in
charts_observed.py; color follows the country.
"""
import csv, os
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
RES, FIG = os.path.join(HERE, "results"), os.path.join(HERE, "figures")
COLORS = {"Mexico": "#2a78d6", "Brazil": "#eb6834", "United States": "#1baf7a"}
ES = {"Mexico": "México", "Brazil": "Brasil", "United States": "Estados Unidos"}
REFS = {"Brazil": ("ibge_2024", "IBGE 2024")}
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e0", "#fcfcfb"
SRC = ("Proyección por componentes con datos nacionales, sin insumos de la ONU: INEGI (México); "
       "IBGE, revisión 2024 (Brasil);\nCensus Bureau Vintage 2025 y CDC (Estados Unidos). Fecundidad reciente sin cambio, "
       "banda ±0.2. Línea discontinua: proyección oficial del IBGE.")

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.edgecolor": GRID,
                     "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                     "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE})


def main():
    d = defaultdict(dict)
    for r in csv.DictReader(open(os.path.join(RES, "projections_national.csv"))):
        if r["share_65plus_pct"]: d[(r["country"], r["scenario"])][int(r["year"])] = float(r["share_65plus_pct"])
    ser = lambda k: (sorted(d[k]), [d[k][y] for y in sorted(d[k])])
    fig, ax = plt.subplots(figsize=(9.6, 5.8))
    ends = []
    for c, col in COLORS.items():
        x, cen = ser((c, "central")); _, lo = ser((c, "low")); _, hi = ser((c, "high"))
        ax.fill_between(x, lo, hi, color=col, alpha=0.15, linewidth=0)
        ax.plot(x, cen, color=col, linewidth=2.2, solid_capstyle="round", label=ES[c])
        ax.plot([x[0]], [cen[0]], "o", color=col, markersize=6, markeredgecolor=SURFACE, markeredgewidth=1.5, zorder=5)
        ax.plot([x[-1]], [cen[-1]], "o", color=col, markersize=6, markeredgecolor=SURFACE, markeredgewidth=1.5, zorder=5)
        ends.append([cen[-1], f"{ES[c]} {cen[-1]:.1f} %", INK, "bold"])
        if c in REFS:
            rx, rv = ser((c, REFS[c][0]))
            ax.plot(rx, rv, color=col, linewidth=1.3, linestyle=(0, (4, 3)), alpha=0.9)
            ends.append([rv[-1], f"{REFS[c][1]} {rv[-1]:.1f} %", INK2, "normal"])
    # 2025 starting values, labelled at the left
    starts = sorted(((d[(c, "central")][2025], c) for c in COLORS), reverse=True)
    for v, c in starts:
        ax.annotate(f"{v:.1f} %", (2025, v), xytext=(-9, 0), textcoords="offset points",
                    ha="right", va="center", fontsize=10, color=INK2)
    ax.set_xlim(2021.3, 2050.4); ax.set_ylim(6, 26)
    ax.set_xticks(range(2025, 2051, 5)); ax.set_yticks(range(6, 27, 2)); ax.tick_params(length=0)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f} %"))
    ax.grid(axis="y", color=GRID, linewidth=0.8); ax.set_axisbelow(True)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    # end labels pushed apart
    ends.sort(key=lambda t: t[0]); gap = 0.75
    for i in range(1, len(ends)):
        if ends[i][0] - ends[i - 1][0] < gap: ends[i][0] = ends[i - 1][0] + gap
    for (y, txt, col, w) in ends:
        ax.annotate(txt, (2050.6, y), xytext=(2050.9, y), va="center", fontsize=10, color=col, fontweight=w,
                    annotation_clip=False)
    ax.set_ylabel("Población de 65 años y más, % del total")
    ax.set_title("Población de 65 años y más, 2025–2050", loc="left", fontsize=15, fontweight="bold", color=INK, pad=24)
    ax.text(0, 1.02, "Porcentaje de la población total, si se mantienen las tendencias actuales", transform=ax.transAxes,
            fontsize=10.5, color=INK2)
    ax.legend(loc="upper left", frameon=False, fontsize=10, labelcolor=INK2)
    fig.text(0.01, 0.012, SRC, fontsize=8, color=MUTED)
    fig.tight_layout(rect=(0, 0.06, 0.8, 1))
    os.makedirs(FIG, exist_ok=True)
    fig.savefig(os.path.join(FIG, "share65_2025_2050.png"), dpi=200)


if __name__ == "__main__":
    main()
