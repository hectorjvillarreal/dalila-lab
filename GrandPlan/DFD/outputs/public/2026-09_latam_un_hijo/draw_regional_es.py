"""draw_regional_es.py — public chart «¿Y si en América Latina cada mujer tuviera un solo hijo?» from results/."""
import os, pandas as pd, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__))
A = pd.read_csv(os.path.join(HERE, "results", "lac_tfr1_aggregate.csv"), index_col=0); yrs = A.index.values
INK, INK2, MUTED, GRID, RED, GREY, BG = "#0b0b0b", "#52514e", "#8a8983", "#ececea", "#e34948", "#8a8983", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "axes.edgecolor": MUTED, "xtick.color": INK2, "ytick.color": INK2})
fig = plt.figure(figsize=(10, 8.2), dpi=150); fig.patch.set_facecolor(BG)
ax = fig.add_axes([.09, .25, .83, .54]); ax.set_facecolor(BG); ax.grid(axis="y", color=GRID, lw=.8)
ax.spines[["top","right"]].set_visible(False); ax.tick_params(labelsize=11)
ax.plot(yrs, A.un_published, color=GREY, lw=2.2, ls=(0,(5,2.5)))
ax.plot(yrs, A.tfr1, color=RED, lw=2.8, marker="o", ms=5)
now, pk, end, unend, unpk = A.tfr1[2025], A.tfr1.idxmax(), A.tfr1[2100], A.un_published[2100], A.un_published.idxmax()
ax.text(2101.5, unend, f"{unend:.0f}", va="center", fontsize=14, color=INK2, fontweight="bold")
ax.text(2101.5, end, f"{end:.0f}", va="center", fontsize=14, color=INK, fontweight="bold")
ax.text(2062, A.un_published[2060]+14, "Lo que calcula la ONU", fontsize=11, color=INK2)
ax.text(2064, 600, "Si cada mujer tuviera\nun solo hijo a partir de 2030", fontsize=11.5, color=INK, fontweight="bold")
ax.plot([2025], [now], "o", color=BG, mec=INK, mew=2, ms=11, zorder=6)
ax.annotate(f"Hoy: {now:.0f} millones", (2025, now), xytext=(2029, 580), fontsize=11, color=INK, fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=INK, lw=1))
ax.set_xlim(2022, 2108); ax.set_ylim(300, 770); ax.set_xticks(range(2025, 2101, 15))
ax.set_ylabel("Millones de habitantes", fontsize=11, color=INK2)
fig.text(.06, .965, "¿Y si en América Latina cada mujer tuviera un solo hijo?", fontsize=18, fontweight="bold", color=INK, va="top")
fig.text(.06, .918, f"Hoy somos {now:.0f} millones y cada mujer tiene, en promedio, 1.5 hijos. Si desde 2030 tuviera uno solo,\n"
         f"creceríamos apenas unos años más y luego empezaríamos a bajar. A fines de siglo seríamos\n"
         f"{end:.0f} millones: la mitad que hoy y {unend-end:.0f} millones menos de lo que calcula la ONU.",
         fontsize=11.5, color=INK2, va="top", linespacing=1.5)
k50, k00 = A.tfr1_0_14[2050], A.tfr1_0_14[2100]
fig.text(.06, .185, f"Lo que más cambia es el número de niños: hoy hay {A.tfr1_0_14[2025]:.0f} millones de menores de 15 años; en 2050 serían {k50:.0f} millones\n"
         f"y en 2100, {k00:.0f} millones. Desde {next(y for y in yrs if A.tfr1_65p[y] > A.tfr1_0_14[y])} habría más personas de 65 años o más que niños.",
         fontsize=10.5, color=INK, va="top", linespacing=1.5, bbox=dict(boxstyle="round,pad=0.7", fc="#f3f1ec", ec="none"))
fig.text(.06, .012, "Cómo se hizo: partimos de la población de 2025 de los 49 países y territorios de América Latina y el Caribe y la proyectamos cada cinco años. "
         "En cada país, los hijos\npor mujer pasan poco a poco de su nivel actual a uno en 2030 y se quedan ahí. La mortalidad y la migración son las que supone la ONU; sólo cambia cuántos hijos\n"
         "tiene cada mujer. Con los supuestos completos de la ONU, este método reproduce sus cifras. Es un escenario hipotético, no un pronóstico.\n"
         "Fuentes: ONU, World Population Prospects 2024. Hijos por mujer hoy: registros civiles de 18 países, años 2022 a 2025 (recopilados por J. Fernández-Villaverde, 2026);\n"
         "para México, INEGI, Encuesta Intercensal 2025, que también da la población de México hoy. Elaboración propia, septiembre de 2026.",
         fontsize=7.6, color=MUTED, va="bottom", linespacing=1.45)
fig.savefig(os.path.join(HERE, "figures", "latam_un_hijo_regional.png"), facecolor=BG)
print(A.loc[[2025,2030,2050,2075,2100],["un_published","tfr1","tfr1_0_14","tfr1_65p"]].round(1))
