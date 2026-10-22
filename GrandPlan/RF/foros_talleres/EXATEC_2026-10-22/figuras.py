"""Gráficas del 3er Encuentro EXATEC (22-oct-2026), derivadas de las de SobreMéxico 2026.
Cifras nuevas: tabla de la sección 2 de BUILD-20261022-EXATEC-BEAMER v1."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent / "fig"
GRIS = "#2F3A40"; GRIS_CLARO = "#9AA5AB"; PETROLEO = "#1F6672"; FONDO = "#FFFFFF"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15, "pdf.fonttype": 42,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": GRIS_CLARO, "text.color": GRIS,
                     "axes.labelcolor": GRIS, "xtick.color": GRIS, "ytick.color": GRIS})

def guarda(fig, nombre):
    fig.savefig(OUT / nombre, bbox_inches="tight", metadata={"Creator": None, "Producer": None})
    plt.close(fig)

# Lámina 2: ingresos frente a gasto, LIF 2027 aprobada por la Cámara de Diputados
# Ingresos presupuestarios 9.16 bdp (23.2 % del PIB); ingresos totales LIF con financiamiento 10.64 bdp,
# que por identidad presupuestaria igualan al gasto neto total.
fig, ax = plt.subplots(figsize=(7.2, 4.2))
vals = [9.16, 10.64]
b = ax.bar(["Ingresos\npresupuestarios", "Gasto neto total,\nPPEF 2027"], vals,
           color=[GRIS_CLARO, PETROLEO], width=0.55)
for r, v in zip(b, vals):
    ax.text(r.get_x() + r.get_width()/2, v + 0.15, f"{v:.2f}", ha="center", fontsize=20, fontweight="bold")
ax.text(b[0].get_x() + b[0].get_width()/2, 4.6, "23.2 %\ndel PIB", ha="center", va="center", fontsize=14, color="white")
ax.annotate("", xy=(1.42, 10.64), xytext=(1.42, 9.16), arrowprops=dict(arrowstyle="<->", color=GRIS, lw=1.6))
ax.plot([0.28, 1.42], [9.16, 9.16], ls=":", color=GRIS, lw=1)
ax.text(1.48, 9.90, "≈ 1.5", va="center", fontsize=17, fontweight="bold", color=GRIS)
ax.set_ylim(0, 12); ax.set_xlim(-0.5, 1.8); ax.set_ylabel("Billones de pesos")
ax.set_title("LIF 2027 aprobada por la Cámara de Diputados", loc="left", fontsize=15, color=GRIS)
guarda(fig, "l2_ingresos_gasto_lif2027.pdf")

# Lámina 3: cascada, % del PIB (Contabilidad de la muerte, actualización 2026)
pasos = [("Ingresos\ndisponibles", 20.7, "total"),
         ("Costo\nfinanciero", -3.8, "resta"),
         ("Participa-\nciones", -4.2, "resta"),
         ("Adefas\ny otros", -0.3, "resta"),
         ("Pensiones", -6.3, "resta"),
         ("Operación de\nIMSS, ISSSTE\ny CFE (con\ningresos propios)", -2.1, "resta"),
         ("Bolsa", 4.0, "bolsa")]
fig, ax = plt.subplots(figsize=(12.5, 4.3))
nivel = 0.0
for i, (lab, v, tipo) in enumerate(pasos):
    if tipo == "total":
        ax.bar(i, v, color=GRIS, width=0.62); nivel = v; y = v
        txt = f"{v:.1f}"
    elif tipo == "resta":
        ax.bar(i, -v, bottom=nivel + v, color=GRIS_CLARO, width=0.62)
        ax.plot([i - 1 + 0.31, i - 0.31], [nivel, nivel], color=GRIS_CLARO, lw=1, ls=":")
        nivel += v; y = nivel - v
        txt = f"−{-v:.1f}"
    else:
        ax.plot([i - 1 + 0.31, i - 0.31], [nivel, nivel], color=GRIS_CLARO, lw=1, ls=":")
        ax.bar(i, v, color=PETROLEO, width=0.62); y = v
        txt = f"{v:.1f}"
    ax.text(i, y + 0.4, txt, ha="center", fontsize=20, fontweight="bold",
            color=PETROLEO if tipo == "bolsa" else GRIS)
ax.set_xticks(range(len(pasos)), [p[0] for p in pasos], fontsize=15)
ax.set_ylim(0, 23.5); ax.set_ylabel("% del PIB")
ax.set_title("Actualización 2026 (cierre 2026)", loc="left", fontsize=14, color=GRIS)
guarda(fig, "l3_cascada_2026.pdf")

# Lámina 4: inversión pública, % del PIB (CIEP 2026, Paquete Económico 2027)
fig, ax = plt.subplots(figsize=(5.4, 3.9))
anios = ["2025", "2026", "2027"]; inv = [3.9, 3.3, 2.9]
b = ax.bar(anios, inv, color=[GRIS_CLARO, GRIS_CLARO, PETROLEO], width=0.55)
for r, v in zip(b, inv):
    ax.text(r.get_x() + r.get_width()/2, v + 0.08, f"{v:.1f}", ha="center", fontsize=19, fontweight="bold")
ax.set_ylim(0, 4.6); ax.set_ylabel("% del PIB")
ax.set_title("Inversión pública\nPaquete Económico 2027", loc="left", fontsize=14, color=GRIS)
guarda(fig, "l4_inversion_2027.pdf")

# Lámina 5: reforma clásica frente a brecha con América Latina y el Caribe
fig, ax = plt.subplots(figsize=(7.4, 4.2))
lab = ["Reforma fiscal\nclásica", "Brecha de México\nfrente a ALC (2023)"]
vals = [1.5, round(21.3 - 17.7, 1)]
b = ax.bar(lab, vals, color=[GRIS_CLARO, PETROLEO], width=0.55)
for r, v, t in zip(b, vals, ["≈ 1.5", "3.6"]):
    ax.text(r.get_x() + r.get_width()/2, v + 0.08, t, ha="center", fontsize=21, fontweight="bold")
ax.set_ylim(0, 4.3); ax.set_ylabel("Puntos del PIB")
ax.set_title("Recaudación: México 17.7 % vs. promedio ALC 21.3 % del PIB, 2023", loc="left", fontsize=12.5, color=GRIS)
guarda(fig, "l5_reforma_brecha.pdf")

# Lámina 5 (nueva): la deuda ya compite por la Bolsa, % del PIB
fig, ax = plt.subplots(figsize=(11.5, 3.9))
etq = ["Bolsa de gasto discrecional\n(actualización 2026)",
       "Costo financiero de la deuda\n(PPEF 2027)",
       "Inversión pública\n(PPEF 2027)"]
vals = [4.0, 4.0, 2.9]
y = [2, 1, 0]
ax.barh(y, vals, color=[PETROLEO, GRIS, GRIS_CLARO], height=0.6)
for yi, v in zip(y, vals):
    ax.text(v + 0.06, yi, f"{v:.1f}", va="center", fontsize=21, fontweight="bold",
            color=PETROLEO if yi == 2 else GRIS)
ax.set_yticks(y, etq, fontsize=15)
ax.set_xlim(0, 4.7); ax.set_xlabel("% del PIB")
ax.spines["left"].set_visible(False); ax.tick_params(axis="y", length=0)
guarda(fig, "l5_deuda_bolsa_2027.pdf")

# Lámina 15: techo frente a programado, Gobierno Federal, % del PIB (LIF 2027; PIB de SHCP)
# Techo: 1.7 bdp internos + 13,500 mdd externos ≈ 1.94 bdp ≈ 4.9 %; programado: 1.57 bdp ≈ 4.0 %.
fig, ax = plt.subplots(figsize=(9.0, 1.7))
etq = ["Techo autorizado\n(LIF 2027, art. 2o)", "Endeudamiento programado\n(LIF 2027, art. 1o)"]
vals = [4.9, 4.0]
y = [1, 0]
ax.barh(y, vals, color=[PETROLEO, GRIS], height=0.6)
for yi, v in zip(y, vals):
    ax.text(v + 0.06, yi, f"{v:.1f}", va="center", fontsize=21, fontweight="bold",
            color=PETROLEO if yi == 1 else GRIS)
ax.set_yticks(y, etq, fontsize=15)
ax.set_xlim(0, 5.6); ax.set_xlabel("% del PIB")
ax.spines["left"].set_visible(False); ax.tick_params(axis="y", length=0)
guarda(fig, "l15_regla_fiscal_2027.pdf")
