"""
Step 2 of the EIC-2025 nota: figures F1-F4 (build instruction §2), Spanish,
white background, direct labels, fixed scenario colours, PNG 300 dpi + PDF.

Palette (validated with the dataviz validator on #ffffff, all pairs):
grey Optimista is a deliberate neutral (the UN reference line, fails the chroma
floor by design); red/green CVD ΔE 7.2 and amber contrast 2.2:1 are covered by
secondary encoding — every line is direct-labelled in ink, each scenario has its
own marker shape, and the page carries a table of the same numbers.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA, RESULTS, FIG = ROOT / "data", ROOT / "results", ROOT / "figures"

TAG = "preliminar · DFD v1.6+EIC · sep-2026"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#dcdbd6"
OBS = "#e34948"
STYLE = {  # key: (label, colour, marker)
    "optimista": ("Optimista — ONU", "#8a8984", "o"),
    "central": ("Central DFD", "#008300", "s"),
    "inegi": ("INEGI directo", "#eda100", "D"),
    "estres": ("Estrés", "#e34948", "^"),
}
ORDER = ["optimista", "central", "inegi", "estres"]

mpl.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12, "axes.titlesize": 13, "axes.labelsize": 11,
    "xtick.labelsize": 11, "ytick.labelsize": 11, "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white", "pdf.fonttype": 42,
})


def style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, length=0, pad=6)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def finish(fig, name, source):
    fig.text(0.01, 0.012, source, fontsize=8.5, color=INK2, ha="left", va="bottom")
    fig.text(0.99, 0.985, TAG, fontsize=8.5, color=INK2, ha="right", va="top", style="italic")
    FIG.mkdir(exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(FIG / f"{name}.{ext}", dpi=300)
    plt.close(fig)


def place_labels(ends, lo, hi, gap):
    """Nudge end-label y positions apart (keeps order)."""
    items = sorted(ends, key=lambda t: t[1])
    ys = [y for _, y in items]
    for i in range(1, len(ys)):
        ys[i] = max(ys[i], ys[i - 1] + gap)
    over = ys[-1] - hi
    if over > 0:
        ys = [y - over for y in ys]
    return [(k, y0, y) for (k, y0), y in zip(items, ys)]


def observed(ax, x, y):
    ax.plot(x, y, marker="o", markersize=9, color=OBS, markeredgecolor=INK, markeredgewidth=1.8, zorder=6,
            linestyle="none")


# ---------------------------------------------------------------- F1
def f1():
    w = pd.read_csv(DATA / "wpp2024_mex_indicators_medium.csv")
    low = pd.read_csv(DATA / "wpp2024_mex_tfr_low_variant.csv")
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    style(ax)
    est, proj = w[w.year <= 2023], w[w.year >= 2023]
    ax.plot(est.year, est.TFR, color=INK2, linewidth=2)
    ax.plot(proj.year, proj.TFR, color=INK2, linewidth=2, linestyle=(0, (4, 2.5)))
    lw = pd.concat([w[w.year == 2023][["year", "TFR"]].rename(columns={"TFR": "TFR_low"}), low])
    ax.plot(lw.year, lw.TFR_low, color=INK2, linewidth=1.2, linestyle=(0, (1, 2)))
    ax.text(2050.8, float(proj.TFR.iloc[-1]), "ONU, variante media\n(proyección 2024)", fontsize=10, color=INK2, va="center")
    ax.text(2050.8, float(low.TFR_low.iloc[-1]), "ONU, variante baja", fontsize=10, color=INK2, va="center")
    for yr, v in ((2019, 2.02), (2024, 1.89)):
        ax.plot(yr, v, marker="o", markersize=5, color=INK2, zorder=5)
    ax.annotate("ONU 2019: 2.02", (2019, 2.02), xytext=(4, 12), textcoords="offset points", ha="left", fontsize=10, color=INK2)
    ax.annotate("ONU 2024: 1.89", (2024, 1.89), xytext=(6, 9), textcoords="offset points", ha="left", fontsize=10, color=INK2)
    observed(ax, [2019, 2024], [1.90, 1.23])
    ax.annotate("INEGI 2019: 1.9\n(Censo 2020)", (2019, 1.90), xytext=(-10, -30), textcoords="offset points", ha="right",
                fontsize=10.5, color=INK, fontweight="bold")
    ax.annotate("INEGI 2024: 1.23\n(Encuesta Intercensal 2025)", (2024, 1.23), xytext=(-16, -2), textcoords="offset points",
                ha="right", va="center", fontsize=10.5, color=INK, fontweight="bold")
    ax.axhline(2.1, color=GRID, linewidth=1.2)
    ax.text(2050.8, 2.1, "reemplazo ≈ 2.1", fontsize=9.5, color=INK2, va="center")
    ax.set_xlim(2000, 2061)
    ax.set_ylim(1.0, 2.9)
    ax.set_xticks([2000, 2010, 2020, 2030, 2040, 2050])
    ax.set_ylabel("Hijos por mujer (tasa global de fecundidad)", color=INK2)
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    finish(fig, "F1_fecundidad_inegi_vs_onu",
           "Fuentes: INEGI, Censo 2020 y Encuesta Intercensal 2025 (estimación directa); ONU, World Population Prospects 2024.")


# ---------------------------------------------------------------- F2
def f2(res):
    w = pd.read_csv(DATA / "wpp2024_mex_indicators_medium.csv")
    w = w[w.year.between(2025, 2050)]
    fig, ax = plt.subplots(figsize=(6.0, 4.6))
    style(ax)
    ax.plot(w.year, w.TPopulation1July / 1e3, color=INK2, linewidth=1.4, linestyle=(0, (4, 2.5)))
    ends = [("onu", float(w.TPopulation1July.iloc[-1]) / 1e3)]
    for k in ORDER:
        g = res[res.scenario == k]
        lab, col, mk = STYLE[k]
        ax.plot(g.year, g.population / 1e6, color=col, linewidth=2.2)
        g5 = g[g.year % 5 == 0]
        ax.plot(g5.year, g5.population / 1e6, color=col, marker=mk, markersize=6, linestyle="none",
                markeredgecolor="white", markeredgewidth=1)
        ends.append((k, float(g.population.iloc[-1]) / 1e6))
    for k, y0, y in place_labels(ends, 115, 152, 2.6):
        txt = "Proyección ONU\n(no re-estimada)" if k == "onu" else STYLE[k][0]
        ax.text(2050.8, y, f"{txt}  {y0:.0f}" if k != "onu" else f"{txt}  {y0:.0f}", fontsize=10, color=INK, va="center")
    observed(ax, [2025], [130.9])
    ax.annotate("INEGI 2025:\n130.9 millones", (2025, 130.9), xytext=(4, -40), textcoords="offset points", fontsize=10, color=INK)
    ax.set_xlim(2024, 2062)
    ax.set_xticks([2025, 2030, 2035, 2040, 2045, 2050])
    ax.set_ylabel("Millones de personas", color=INK2)
    ax.set_title("Población total, 2025–2050", loc="left", color=INK, fontsize=13)
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    finish(fig, "F2_poblacion_total", "Fuente: escenarios propios sobre la Encuesta Intercensal 2025; ONU WPP 2024.")


# ---------------------------------------------------------------- F3
def f3(res, fis):
    """Two panels (review record §3.2): total dependency and old-age dependency."""
    q3 = fis[fis.base == "q3"].set_index("indicator").value
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.6), sharex=True)
    for ax, col, title, lim in ((axes[0], "tdr", "Razón de dependencia total", (38, 61)),
                                (axes[1], "oadr", "Razón de vejez (65 y más)", (10, 38))):
        style(ax)
        ends = []
        for k in ORDER:
            g = res[res.scenario == k]
            lab, colr, mk = STYLE[k]
            ax.plot(g.year, g[col], color=colr, linewidth=2.2)
            g5 = g[g.year % 5 == 0]
            ax.plot(g5.year, g5[col], color=colr, marker=mk, markersize=6, linestyle="none",
                    markeredgecolor="white", markeredgewidth=1)
            if col == "tdr":
                i = int(g.tdr.values.argmin())
                ax.plot(g.year.iloc[i], g.tdr.iloc[i], marker="v", markersize=9, color=colr, markeredgecolor=INK,
                        markeredgewidth=1, zorder=5)
            ends.append((k, float(g[col].iloc[-1])))
        gap = 1.9 if col == "tdr" else 1.6
        for k, y0, y in place_labels(ends, *lim, gap):
            ax.text(2050.8, y, f"{STYLE[k][0]}  {y0:.0f}", fontsize=9.5, color=INK, va="center")
        ax.set_xlim(2024, 2064)
        ax.set_ylim(*lim)
        ax.set_xticks([2025, 2030, 2035, 2040, 2045, 2050])
        ax.set_title(title, loc="left", color=INK, fontsize=12.5)
    axes[0].set_ylabel("Por cada 100 personas de 15 a 64 años", color=INK2)
    observed(axes[0], [2025], [46.4])
    axes[0].annotate("INEGI 2025:\n46.4", (2025, 46.4), xytext=(-2, 14), textcoords="offset points", fontsize=9.5, color=INK)
    y_q3, v_q3 = q3["q3_central_tdr_min_year"], q3["q3_central_tdr_min"]
    axes[0].plot(y_q3, v_q3, marker="s", markersize=8, color="white", markeredgecolor=INK2, markeredgewidth=1.6, zorder=6)
    axes[0].annotate(f"mínimo estimado\nantes de la Encuesta\n({int(y_q3)}: {v_q3:.0f})", (y_q3, v_q3), xytext=(8, -34),
                     textcoords="offset points", fontsize=9, color=INK2)
    fig.text(0.01, 0.055, "▼ mínimo de cada escenario", fontsize=9, color=INK2)
    fig.tight_layout(rect=[0, 0.08, 1, 0.97])
    finish(fig, "F3_razon_dependencia", "Fuente: escenarios propios sobre la Encuesta Intercensal 2025. "
           "Total: (0–14 + 65 y más) / 15–64. Vejez: 65 y más / 15–64.")


# ---------------------------------------------------------------- F4
def f4(res):
    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    style(ax)
    ends = []
    for k in ("central", "inegi"):
        g = res[res.scenario == k].set_index("year")
        lab, col, mk = STYLE[k]
        for colname, ls, grp in (("pop_15_64", "-", "15–64 (fuerza laboral)"), ("pop_6_14", (0, (5, 2.5)), "6–14 (escuela básica)")):
            idx = 100 * g[colname] / g.loc[2025, colname]
            ax.plot(idx.index, idx.values, color=col, linewidth=2.2, linestyle=ls)
            i5 = idx[idx.index % 5 == 0]
            ax.plot(i5.index, i5.values, color=col, marker=mk, markersize=6, linestyle="none", markeredgecolor="white",
                    markeredgewidth=1)
            ends.append((f"{grp} · {lab}", float(idx.iloc[-1])))
    for k, y0, y in place_labels(ends, 50, 108, 4.2):
        ax.text(2050.8, y, f"{k}  {y0:.0f}", fontsize=9.5, color=INK, va="center")
    ax.axhline(100, color=GRID, linewidth=1.2)
    ax.axvline(2031, color=INK2, linewidth=1, linestyle=(0, (2, 2)))
    ax.text(2031.5, 91, "hasta 2031 todos los\nniños de 6–14 ya nacieron", ha="left", fontsize=9.5, color=INK2)
    ax.set_xlim(2024, 2072)
    ax.set_ylim(50, 108)
    ax.set_xticks([2025, 2030, 2035, 2040, 2045, 2050])
    ax.set_ylabel("Índice, 2025 = 100", color=INK2)
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    finish(fig, "F4_dos_cohortes", "Fuente: escenarios propios sobre la Encuesta Intercensal 2025. Línea continua 15–64; discontinua 6–14.")


def main():
    res = pd.read_csv(RESULTS / "scenarios_eic2025_brief.csv")
    res = res[res.base == "eic2025"]
    fis = pd.read_csv(RESULTS / "fiscal_indicators.csv")
    f1()
    f2(res)
    f3(res, fis)
    f4(res)
    print("Wrote F1-F4 to", FIG)


if __name__ == "__main__":
    main()
