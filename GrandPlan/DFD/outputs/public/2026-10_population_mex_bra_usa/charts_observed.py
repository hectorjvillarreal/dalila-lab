"""charts_observed.py — draw the figures (labels in Spanish) from results/projections.csv (run projection_observed.py first).

One chart per country (central path, fertility range, UN medium as a reference line), an index
comparison (2025 = 100, central paths) and a 2x2 overview. Palette: dataviz reference
categorical slots 1-3, validated all-pairs in light mode; color follows the country.
"""
import csv, os
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
RES, FIG = os.path.join(HERE, "results"), os.path.join(HERE, "figures")
COLORS = {"Mexico": "#2a78d6", "Brazil": "#eb6834", "United States": "#1baf7a"}
INK, INK2, MUTED, GRID, SURFACE, REF = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e0", "#fcfcfb", "#8a8984"
# National statistics office figures shown as reference markers (sources in README)
NATIONAL_REF = {"Brazil": (2041, 220.4, "Proyección IBGE 2024: máximo 220.4 M (2041)")}
ES = {"Mexico": "México", "Brazil": "Brasil", "United States": "Estados Unidos"}
SRC = ("Proyección con los datos nacionales más recientes: INEGI, EIC 2025; IBGE, estimación 2025 y nacimientos 2024; "
       "US Census Bureau, Vintage 2025, y CDC, nacimientos 2025.\nRango de fecundidad ±0.2. ONU, WPP 2024 (variante media), como referencia.")

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.edgecolor": GRID,
                     "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                     "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE})


def load():
    d = defaultdict(dict)
    for r in csv.DictReader(open(os.path.join(RES, "projections.csv"))):
        d[(r["country"], r["scenario"])][int(r["year"])] = float(r["pop_millions"])
    return d


def ser(d):
    ys = sorted(d); return ys, [d[y] for y in ys]


def style(ax, right_pad=0.5):
    ax.grid(axis="y", color=GRID, linewidth=0.8); ax.set_axisbelow(True)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.set_xlim(2024.5, 2050 + right_pad); ax.set_xticks(range(2025, 2051, 5)); ax.tick_params(length=0)


def label_ends(ax, items):
    """items: (y, text, color, weight); pushes labels apart vertically, in data units."""
    lo, hi = ax.get_ylim(); gap = (hi - lo) * 0.055
    items = sorted(items, key=lambda t: t[0])
    ys = [t[0] for t in items]
    for i in range(1, len(ys)):
        if ys[i] - ys[i - 1] < gap: ys[i] = ys[i - 1] + gap
    for (y0, txt, col, w), y in zip(items, ys):
        ax.annotate(txt, (2050, y0), xytext=(2050.6, y), textcoords="data", va="center", fontsize=10,
                    color=col, fontweight=w, annotation_clip=False)


def country(ax, d, name):
    c = COLORS[name]
    x, cen = ser(d[(name, "central")]); _, lo = ser(d[(name, "low")]); _, hi = ser(d[(name, "high")])
    ux, un = ser(d[(name, "un_medium")])
    ax.fill_between(x, lo, hi, color=c, alpha=0.15, linewidth=0, label="Fecundidad ±0.2")
    ax.plot(ux, un, color=REF, linewidth=1.5, linestyle=(0, (4, 3)), label="ONU, WPP 2024 variante media (referencia)")
    ax.plot(x, cen, color=c, linewidth=2, marker="o", markersize=5, markeredgecolor=SURFACE, markeredgewidth=1.5,
            label="Datos nacionales recientes, sin cambio")
    items = [(cen[-1], f"{cen[-1]:.1f} M", INK, "bold"), (un[-1], f"ONU {un[-1]:.1f}", INK2, "normal")]
    if (name, "central_mig_1M") in d:
        mx, mv = ser(d[(name, "central_mig_1M")])
        ax.plot(mx, mv, color=c, linewidth=1.5, linestyle=(0, (1, 2)), label="Migración neta de 1 M/año en vez de 321 mil")
        items.append((mv[-1], f"{mv[-1]:.1f}", INK2, "normal"))
    if name in NATIONAL_REF:
        ry, rv, rt = NATIONAL_REF[name]
        ax.plot([ry], [rv], marker="D", markersize=7, color=SURFACE, markeredgecolor=INK2, markeredgewidth=1.5, zorder=6)
        ax.annotate(rt, (ry, rv), xytext=(0, 10), textcoords="offset points", ha="center", fontsize=9, color=INK2)
    pk = max(range(len(cen)), key=cen.__getitem__)
    ax.annotate(f"{x[0]}: {cen[0]:.1f} M", (x[0], cen[0]), xytext=(6, -16), textcoords="offset points",
                fontsize=9.5, color=INK2)
    if 0 < pk < len(cen) - 1:
        ax.annotate(f"máximo ≈{cen[pk]:.1f} M ({x[pk]})", (x[pk], cen[pk]), xytext=(0, -18), textcoords="offset points",
                    ha="center", fontsize=9.5, color=INK2)
    allv = lo + hi + un + cen + ([v for v in d.get((name, "central_mig_1M"), {}).values()])
    if name in NATIONAL_REF: allv.append(NATIONAL_REF[name][1] + 0.6)
    span = max(allv) - min(allv); ax.set_ylim(min(allv) - span * 0.12, max(allv) + span * 0.12)
    style(ax, right_pad=0.5)
    label_ends(ax, items)
    ax.set_title(ES[name], loc="left", fontsize=13, fontweight="bold", pad=10, color=INK)
    ax.set_ylabel("Población, millones")
    ax.legend(loc="lower left" if name == "Brazil" else "upper left", frameon=False, fontsize=8.5, labelcolor=INK2)


def index(ax, d):
    items = []
    for name, c in COLORS.items():
        x, v = ser(d[(name, "central")]); iv = [100 * a / v[0] for a in v]
        ax.plot(x, iv, color=c, linewidth=2, marker="o", markersize=4, label=ES[name])
        items.append((iv[-1], f"{iv[-1]:.1f}", INK, "normal"))
    ax.axhline(100, color=MUTED, linewidth=0.8)
    style(ax, right_pad=0.5)
    lo, hi = ax.get_ylim(); ax.set_ylim(lo - 0.5, hi + 0.5)
    label_ends(ax, items)
    ax.set_title("Crecimiento comparado (2025 = 100, trayectorias centrales)", loc="left", fontsize=13, fontweight="bold", pad=10, color=INK)
    ax.set_ylabel("Índice, 2025 = 100")
    ax.legend(loc="lower left", frameon=False, fontsize=9, labelcolor=INK2)


def save(fig, name, src_size=8):
    fig.text(0.01, 0.01, SRC, fontsize=src_size, color=MUTED, wrap=True)
    fig.tight_layout(rect=(0, 0.07, 0.97, 1)); fig.savefig(os.path.join(FIG, name), dpi=200); plt.close(fig)


def main():
    d = load(); os.makedirs(FIG, exist_ok=True)
    for name in COLORS:
        fig, ax = plt.subplots(figsize=(8.4, 5)); country(ax, d, name)
        save(fig, f"population_{name.lower().replace(' ', '_')}_2025_2050.png")
    fig, ax = plt.subplots(figsize=(8.4, 5)); index(ax, d); save(fig, "population_index_2025_2050.png")
    fig, axs = plt.subplots(2, 2, figsize=(15, 9.6))
    for ax, name in zip(axs.flat, COLORS): country(ax, d, name)
    index(axs.flat[3], d)
    fig.suptitle("Población total 2025–2050, si se mantienen las tendencias actuales", x=0.01, ha="left", fontsize=16, fontweight="bold", color=INK)
    fig.text(0.01, 0.01, SRC, fontsize=9, color=MUTED)
    fig.tight_layout(rect=(0, 0.045, 0.975, 0.97)); fig.savefig(os.path.join(FIG, "population_overview_2025_2050.png"), dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    main()
