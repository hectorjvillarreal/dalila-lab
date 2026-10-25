"""Total population 2026-2050: Mexico, Brazil, United States (UN WPP 2024).

Simple charts: one panel per country (medium variant + 80% prediction interval),
plus an indexed comparison (2026 = 100). Mexico's panel adds the EIC-2025-based
range from ../2026-09_mexico_2050/results/scenarios.csv (TFR 1.23 to 1.5).
"""
import csv
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).parent
DATA = HERE / "data" / "WPP2024_TotalPopulationBySex_MEX-BRA-USA_2024-2050.csv"
EIC = HERE.parent / "2026-09_mexico_2050" / "results" / "scenarios.csv"
FIG = HERE / "figures"

# Palette: dataviz reference categorical slots 1-3 (validated all-pairs, light mode).
# Color follows the country in every chart.
COUNTRIES = [
    ("Mexico", "Mexico", "#2a78d6"),
    ("Brazil", "Brazil", "#eb6834"),
    ("United States of America", "United States", "#1baf7a"),
]
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e0", "#fcfcfb"
ALT = "#52514e"  # Mexico EIC-based range: neutral ink, not a series hue
Y0, Y1 = 2026, 2050

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.edgecolor": GRID, "axes.labelcolor": INK2, "axes.titlecolor": INK,
    "xtick.color": INK2, "ytick.color": INK2, "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
})


def load_wpp():
    out = {}
    with open(DATA, newline="") as f:
        for r in csv.DictReader(f):
            t = int(r["Time"])
            if Y0 <= t <= Y1:
                out.setdefault((r["Location"], r["Variant"]), {})[t] = float(r["PopTotal_thousands"]) / 1e3
    return out


def load_eic():
    s = {}
    with open(EIC, newline="") as f:
        for r in csv.DictReader(f):
            if r["scenario"] in ("sube_1.5", "observada_1.23"):
                s.setdefault(r["scenario"], {})[int(r["year"])] = float(r["pop_millions"])
    return s


def series(d):
    yrs = sorted(d)
    return yrs, [d[y] for y in yrs]


def style(ax):
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.set_xlim(Y0 - 0.5, Y1 + 0.5)
    ax.set_xticks([2026, 2030, 2035, 2040, 2045, 2050])
    ax.tick_params(length=0)


def country_panel(ax, wpp, eic, loc, name, color):
    yrs, med = series(wpp[(loc, "Medium")])
    _, lo = series(wpp[(loc, "Lower 80 PI")])
    _, hi = series(wpp[(loc, "Upper 80 PI")])
    ax.fill_between(yrs, lo, hi, color=color, alpha=0.14, linewidth=0, label="UN 80% prediction interval")
    ax.plot(yrs, med, color=color, linewidth=2, label="UN WPP 2024 medium")
    ax.plot([yrs[0], yrs[-1]], [med[0], med[-1]], "o", color=color, markersize=6,
            markeredgecolor=SURFACE, markeredgewidth=2, zorder=5)
    ax.annotate(f"{med[0]:.1f} M", (yrs[0], med[0]), xytext=(10, 12), textcoords="offset points",
                color=INK2, fontsize=10, bbox=dict(boxstyle="round,pad=0.15", fc=SURFACE, ec="none", alpha=0.85))
    ax.annotate(f"{med[-1]:.1f} M", (yrs[-1], med[-1]), xytext=(-6, 8), textcoords="offset points",
                ha="right", color=INK, fontsize=10, fontweight="bold")
    pk = max(range(len(med)), key=med.__getitem__)
    if 0 < pk < len(med) - 1:
        ax.plot(yrs[pk], med[pk], "o", color=color, markersize=6, markeredgecolor=SURFACE,
                markeredgewidth=2, zorder=5)
        ax.annotate(f"peak {med[pk]:.1f} M ({yrs[pk]})", (yrs[pk], med[pk]), xytext=(0, 9),
                    textcoords="offset points", ha="center", color=INK2, fontsize=10)
    if eic:
        ey, e15 = series(eic["sube_1.5"])
        _, e123 = series(eic["observada_1.23"])
        ax.fill_between(ey, e123, e15, color=ALT, alpha=0.10, linewidth=0)
        ax.plot(ey, e15, color=ALT, linewidth=1.5, linestyle=(0, (4, 2)))
        ax.plot(ey, e123, color=ALT, linewidth=1.5, linestyle=(0, (4, 2)),
                label="INEGI EIC 2025 base, TFR 1.23–1.5 (DFD)")
        ax.annotate(f"{e123[-1]:.1f}–{e15[-1]:.1f} M", (ey[-1], e123[-1]), xytext=(-6, -16),
                    textcoords="offset points", ha="right", color=INK2, fontsize=10)
        ax.set_ylim(bottom=126)
    ax.set_title(name, loc="left", fontsize=13, fontweight="bold", pad=10)
    ax.set_ylabel("Population, millions")
    style(ax)
    ax.legend(loc="upper left", frameon=False, fontsize=9, labelcolor=INK2)


def index_panel(ax, wpp):
    for loc, name, color in COUNTRIES:
        yrs, med = series(wpp[(loc, "Medium")])
        idx = [100 * v / med[0] for v in med]
        ax.plot(yrs, idx, color=color, linewidth=2, label=name)
        ax.annotate(f"{idx[-1]:.1f}", (yrs[-1], idx[-1]), xytext=(6, 0),
                    textcoords="offset points", ha="left", va="center", color=INK, fontsize=10)
    ax.axhline(100, color=MUTED, linewidth=0.8)
    ax.set_title("Growth compared (2026 = 100, UN medium)", loc="left", fontsize=13,
                 fontweight="bold", pad=10)
    ax.set_ylabel("Index, 2026 = 100")
    style(ax)
    ax.set_xlim(Y0 - 0.5, Y1 + 2.5)  # room for end labels
    ax.legend(loc="upper left", frameon=False, fontsize=9, labelcolor=INK2)


def main():
    wpp, eic = load_wpp(), load_eic()
    FIG.mkdir(exist_ok=True)
    src = "Source: UN World Population Prospects 2024 (medium variant, 80% PI); Mexico range: INEGI EIC 2025 base, DFD public chart (Sept 2026)."
    # one file per chart
    for loc, name, color in COUNTRIES:
        fig, ax = plt.subplots(figsize=(8, 4.8))
        country_panel(ax, wpp, eic if name == "Mexico" else None, loc, name, color)
        fig.text(0.01, 0.01, src, fontsize=8, color=MUTED)
        fig.tight_layout(rect=(0, 0.03, 1, 1))
        fig.savefig(FIG / f"population_{name.lower().replace(' ', '_')}_2026_2050.png", dpi=200)
        plt.close(fig)
    fig, ax = plt.subplots(figsize=(8, 4.8))
    index_panel(ax, wpp)
    fig.text(0.01, 0.01, src, fontsize=8, color=MUTED)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(FIG / "population_index_2026_2050.png", dpi=200)
    plt.close(fig)
    # overview 2x2
    fig, axs = plt.subplots(2, 2, figsize=(14, 9))
    for ax, (loc, name, color) in zip(axs.flat, COUNTRIES):
        country_panel(ax, wpp, eic if name == "Mexico" else None, loc, name, color)
    index_panel(axs.flat[3], wpp)
    fig.suptitle("Total population, 2026–2050", x=0.01, ha="left", fontsize=16, fontweight="bold", color=INK)
    fig.text(0.01, 0.01, src, fontsize=9, color=MUTED)
    fig.tight_layout(rect=(0, 0.025, 1, 0.97))
    fig.savefig(FIG / "population_overview_2026_2050.png", dpi=200)
    plt.close(fig)
    for loc, name, _ in COUNTRIES:
        yrs, med = series(wpp[(loc, "Medium")])
        print(f"{name}: {med[0]:.2f} M (2026) -> {med[-1]:.2f} M (2050); 80% PI 2050 "
              f"{wpp[(loc, 'Lower 80 PI')][2050] / 1:.2f}-{wpp[(loc, 'Upper 80 PI')][2050]:.2f}")


if __name__ == "__main__":
    main()
