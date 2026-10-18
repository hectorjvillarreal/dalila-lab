"""Figuras de la sección 10 del Núcleo 13 (10a: afiliación subsidiada; 10b: seguro solidario de salud y cuidados).
Solo lee tablas ya guardadas de los dos experimentos; no hay supuestos ni corridas nuevas.
Cada figura se guarda en PNG (300 ppp), SVG y CSV con sus datos."""

from __future__ import annotations

from pathlib import Path

import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

AQUI = Path(__file__).resolve().parents[1]
E1 = AQUI.parent / "e_1_imss_subsidiado" / "anexo_afiliacion_subsidiada" / "outputs" / "tables"
E2 = AQUI.parent / "e_2_imss_nuevoseguro" / "tablas"
FIG = AQUI / "figuras"
ANCHO = 6.0          # pulgadas: se inserta a este ancho en el documento (ancho útil 6.4 in)

plt.rcParams.update({"font.family": ["Noto Sans", "DejaVu Sans"], "font.size": 9, "axes.titlesize": 9,
                     "axes.labelsize": 9, "xtick.labelsize": 9, "ytick.labelsize": 9, "legend.fontsize": 9,
                     "svg.fonttype": "none"})
TINTA, GRIS_T = "#1a1a1a", "#555555"
# escenarios de 10b: mismo color y tipo de línea en todas las figuras (legibles en escala de grises)
ESC = {"base": ("Formalización de la proyección del IMSS", "#1f5fa8", "-", "o"),
       "M3": ("Mitad de esa formalización", "#d9822b", "--", "s"),
       "M2": ("Formalidad constante", "#6b6b6b", "-.", "^"),
       "MH": ("Ritmo histórico", "#2e8b57", ":", "D")}
# componentes de 10a: mismos colores en F10a.3 y F10a.4
COMP = {"cobrado": "#1f5fa8", "federal": "#7fb3e0", "costo": "#d9822b", "saldo": "#1a1a1a"}


def _estilo(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color("#bbbbbb")
    ax.spines["bottom"].set_color("#bbbbbb")
    ax.tick_params(colors=GRIS_T)
    ax.grid(axis="y", color="#e6e6e6", lw=0.8)
    ax.set_axisbelow(True)


def _guardar(fig, nombre: str, datos: pd.DataFrame):
    FIG.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG / f"{nombre}.png", dpi=300, bbox_inches="tight")
    fig.savefig(FIG / f"{nombre}.svg", bbox_inches="tight")
    plt.close(fig)
    datos.to_csv(FIG / f"{nombre}.csv", index=False)


def _caja(ax, x, y, w, h, texto, color="#eef3fa", borde="#1f5fa8", fs=9, peso="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.02", fc=color, ec=borde, lw=1))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=TINTA, weight=peso, wrap=True)


def _flecha(ax, p, q, texto="", dx=0.0, dy=0.0, color=GRIS_T):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=10, lw=1.1, color=color))
    if texto:
        ax.text((p[0] + q[0]) / 2 + dx, (p[1] + q[1]) / 2 + dy, texto, ha="center", va="center", fontsize=8.5, color=GRIS_T,
                bbox=dict(fc="white", ec="none", pad=0.5))


# ---------------------------------------------------------------- 10a
def f10a_1():
    """Esquema de la afiliación subsidiada."""
    fig, ax = plt.subplots(figsize=(ANCHO, 3.3))
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.3, 5.5)
    ax.axis("off")
    _caja(ax, 0.1, 3.5, 2.7, 1.3, "Hogar sin seguridad\nsocial contributiva\n(titular informal)")
    _caja(ax, 0.1, 0.4, 2.7, 1.3, "Trabajador formal\ny su patrón")
    _caja(ax, 3.35, 1.85, 3.2, 1.5, "Gobierno Federal:\naportación fija por titular\ny subsidio a ingresos bajos", color="#f4f4f4", borde=GRIS_T, fs=8.5)
    _caja(ax, 7.2, 1.6, 2.7, 2.0, "SEM del IMSS\n\nCobertura médica\npara el hogar", color="#fff4e8", borde="#d9822b", peso="bold")
    _flecha(ax, (2.8, 4.15), (7.2, 3.3))
    _flecha(ax, (2.8, 1.05), (7.2, 1.9))
    _flecha(ax, (6.55, 2.6), (7.2, 2.6))
    ax.text(5.6, 5.2, "Cuota proporcional al ingreso (menos el subsidio)", ha="center", va="center", fontsize=8.5, color=GRIS_T)
    ax.text(5.6, 0.0, "Misma cuota proporcional por el mismo ingreso", ha="center", va="center", fontsize=8.5, color=GRIS_T)
    datos = pd.DataFrame([{"actor": "Hogar informal", "aporta": "cuota proporcional al ingreso menos subsidio", "recibe": "cobertura médica del SEM"},
                          {"actor": "Formal y patrón", "aporta": "misma cuota proporcional por el mismo ingreso", "recibe": "cobertura médica del SEM"},
                          {"actor": "Gobierno Federal", "aporta": "aportación fija por titular y subsidio a ingresos bajos", "recibe": ""}])
    _guardar(fig, "F10a_1_esquema", datos)


def f10a_2():
    """Asequibilidad: pago anual como % del ingreso laboral del titular, por percentil."""
    a = pd.read_csv(E1 / "asequibilidad.csv")
    a = a[a.percentil.isin([10, 20, 30, 50, 70, 90])]
    fig, ax = plt.subplots(figsize=(ANCHO, 2.9))
    x = range(len(a))
    w = 0.38
    ax.bar([i - w / 2 for i in x], a.pct_ingreso_laboral_D2_G2, w, color="#1f5fa8", label="Cuota proporcional con subsidio")
    ax.bar([i + w / 2 for i in x], a.pct_ingreso_laboral_D1_G1, w, color="#c9c9c9", hatch="//", edgecolor="#8a8a8a", lw=0,
           label="Cuota fija vigente (precio único)")
    for i, (u, v) in enumerate(zip(a.pct_ingreso_laboral_D2_G2, a.pct_ingreso_laboral_D1_G1)):
        ax.text(i - w / 2, u + 0.3, f"{u:.1f}", ha="center", fontsize=8.5, color=TINTA)
        ax.text(i + w / 2, v + 0.3, f"{v:.1f}", ha="center", fontsize=8.5, color=GRIS_T)
    ax.set_xticks(list(x), [f"P{p}" for p in a.percentil])
    ax.set_xlabel("Percentil del ingreso laboral del titular informal")
    ax.set_ylabel("% del ingreso laboral anual")
    ax.set_ylim(0, 17)
    ax.legend(frameon=False, loc="upper left")
    _estilo(ax)
    _guardar(fig, "F10a_2_asequibilidad", a[["percentil", "ingreso_laboral_anual", "prima_D2_G2", "pct_ingreso_laboral_D2_G2",
                                            "prima_D1_G1", "pct_ingreso_laboral_D1_G1"]])


def f10a_3():
    """Saldo para el SEM, puntos del salario: cuotas cobradas, aportación federal, costo de atención y saldo."""
    r = pd.read_csv(E1 / "resultados_v12.csv")
    r = r[(r.corrida == "base") & (r.bloque == "Total") & (r.anio.isin([2026, 2030, 2040, 2054]))].set_index("anio")
    d = pd.DataFrame({"anio": r.index, "cuotas_cobradas": r.pagos_privados_pts_sbc.values, "aportacion_federal": r.pagos_GF_pts_sbc.values,
                      "costo_atencion": r.costo_pts_sbc.values, "saldo": r.saldo_pts_sbc.values})
    fig, ax = plt.subplots(figsize=(ANCHO, 2.9))
    x = range(len(d))
    w = 0.36
    ax.bar([i - w / 2 for i in x], d.cuotas_cobradas, w, color=COMP["cobrado"], label="Cuotas cobradas")
    ax.bar([i - w / 2 for i in x], d.aportacion_federal, w, bottom=d.cuotas_cobradas, color=COMP["federal"], label="Aportación federal")
    ax.bar([i + w / 2 for i in x], d.costo_atencion, w, color=COMP["costo"], label="Costo de atención")
    for i, s in enumerate(d.saldo):
        top = max(d.cuotas_cobradas[i] + d.aportacion_federal[i], d.costo_atencion[i])
        ax.text(i, top + 0.12, f"Saldo: {s:.1f}".replace("-", "−"), ha="center", fontsize=8.5, color=TINTA, weight="bold")
    ax.set_xticks(list(x), [str(a) for a in d.anio])
    ax.set_ylabel("Puntos del salario")
    ax.set_ylim(0, max(d.costo_atencion) * 1.25)
    ax.legend(frameon=False, ncol=3, loc="upper right", bbox_to_anchor=(1, 1.02))
    _estilo(ax)
    _guardar(fig, "F10a_3_saldo_SEM", d)


def f10a_4():
    """Formalización de 3 millones de cotizantes a 2030 frente al status quo: efecto neto para el SEM."""
    b = pd.read_csv(E1 / "bloque_C_vs_status_quo.csv")
    b = b[b.anio.isin([2030, 2040, 2054])]
    p = b.pivot(index="anio", columns="cuota", values="efecto_neto_SEM") / 1000
    fig, ax = plt.subplots(figsize=(ANCHO, 2.6))
    x = range(len(p))
    w = 0.36
    ax.bar([i - w / 2 for i in x], p["D2"], w, color=COMP["cobrado"], label="Cuota proporcional")
    ax.bar([i + w / 2 for i in x], p["vigente"], w, color="#c9c9c9", hatch="//", edgecolor="#8a8a8a", lw=0, label="Cuota fija vigente")
    for i, (u, v) in enumerate(zip(p["D2"], p["vigente"])):
        ax.text(i - w / 2, u - 0.5, f"{u:.0f}".replace("-", "−"), ha="center", va="top", fontsize=8.5, color=TINTA)
        ax.text(i + w / 2, v - 0.5, f"{v:.0f}".replace("-", "−"), ha="center", va="top", fontsize=8.5, color=GRIS_T)
    ax.axhline(0, color="#888888", lw=0.8)
    ax.set_xticks(list(x), [str(a) for a in p.index])
    ax.set_ylabel("Miles de millones de pesos de 2026")
    ax.set_ylim(-15, 2)
    ax.set_yticks([-15, -10, -5, 0], ["−15", "−10", "−5", "0"])
    ax.legend(frameon=False, loc="lower right")
    _estilo(ax)
    _guardar(fig, "F10a_4_formalizacion", b[["anio", "cuota", "ingresos_SEM", "costo", "efecto_neto_SEM", "efecto_neto_pts_sbc"]])


# ---------------------------------------------------------------- 10b
def f10b_1():
    """Esquema: del 5 % actual al nuevo seguro."""
    fig, ax = plt.subplots(figsize=(ANCHO, 3.2))
    ax.set_xlim(-0.3, 10.2)
    ax.set_ylim(0, 5.4)
    ax.axis("off")
    _caja(ax, 0.0, 2.0, 2.5, 1.4, "Aportación\npatronal al\nInfonavit hoy:\n5 % del salario", color="#f4f4f4", borde=GRIS_T, peso="bold", fs=8.5)
    _caja(ax, 3.2, 3.6, 2.6, 1.1, "3 puntos que se\ndejan de cobrar", color="#f4f4f4", borde=GRIS_T, fs=8.5)
    _caja(ax, 3.2, 0.7, 2.6, 1.1, "2 puntos al nuevo\nseguro solidario", color="#eef3fa", borde="#1f5fa8", peso="bold", fs=8.5)
    _caja(ax, 6.55, 3.6, 3.4, 1.2, "1.º Déficit de gastos\nmédicos de pensionados", color="#fff4e8", borde="#d9822b", fs=8.5)
    _caja(ax, 6.55, 1.9, 3.4, 1.2, "2.º Reserva\n(lo que sobra, hasta 2034)", color="#eef3fa", borde="#1f5fa8", fs=8.5)
    _caja(ax, 6.55, 0.2, 3.4, 1.2, "3.º Cuidados en la vejez\n(lo que sobra, desde 2035)", color="#eef8f1", borde="#2e8b57", fs=8.5)
    _flecha(ax, (2.5, 2.9), (3.2, 4.15))
    _flecha(ax, (2.5, 2.5), (3.2, 1.25))
    _flecha(ax, (5.8, 1.25), (6.55, 4.2))
    _flecha(ax, (8.25, 3.6), (8.25, 3.1))
    _flecha(ax, (8.25, 1.9), (8.25, 1.4))
    ax.text(4.5, 2.65, "El Infonavit conserva\nsu patrimonio", ha="center", va="center", fontsize=8.5, color=GRIS_T, style="italic")
    datos = pd.DataFrame([{"paso": 1, "destino": "Déficit de GMP", "regla": "primero"},
                          {"paso": 2, "destino": "Reserva al 3 % real", "regla": "excedente hasta 2034"},
                          {"paso": 3, "destino": "Cuidados en la vejez", "regla": "remanente desde 2035 y retiro fijo de 1/20 de la reserva en años sin faltante"}])
    _guardar(fig, "F10b_1_esquema", datos)


def f10b_2():
    """Ingreso del nuevo seguro (continua) frente al déficit de GMP (punteada), por escenario."""
    d = pd.read_csv(E2 / "ingreso_vs_GMP.csv")
    fig, ax = plt.subplots(figsize=(ANCHO, 3.6))
    filas = []
    for e in ("base", "M3", "M2"):
        x = d[d.escenario_masa == e].set_index("anio")
        nom, col, _, mk = ESC[e]
        ax.plot(x.index, x.ingreso_NS / 1000, color=col, lw=2, ls="-", label=f"{nom}: ingreso")
        ax.plot(x.index, x.deficit_GMP / 1000, color=col, lw=1.6, ls=(0, (4, 2)), label=f"{nom}: déficit de GMP")
        cruce = x.index[(x.deficit_GMP > x.ingreso_NS)]
        if len(cruce):
            t = int(cruce.min())
            ax.plot([t], [x.deficit_GMP[t] / 1000], marker=mk, color=col, ms=6, ls="none")
            xy = (2027.6, 185) if e == "M2" else (2037.5, 60)
            ax.annotate(f"{nom.lower()}: desde {t}\nel déficit rebasa el ingreso", (t, x.deficit_GMP[t] / 1000), xytext=xy,
                        fontsize=8.5, color=col, arrowprops=dict(arrowstyle="-", color=col, lw=0.8))
        for t in x.index:
            filas.append({"escenario": nom, "anio": t, "ingreso_nuevo_seguro_mdp": x.ingreso_NS[t], "deficit_GMP_mdp": x.deficit_GMP[t]})
    ax.set_xlim(2027, 2054)
    ax.set_xticks([2027, 2030, 2035, 2040, 2045, 2050, 2054])
    ax.set_ylim(0, None)
    ax.set_ylabel("Miles de millones de pesos de 2026")
    from matplotlib.lines import Line2D
    h = [Line2D([], [], color=ESC[e][1], lw=2.5, label=ESC[e][0]) for e in ("base", "M3", "M2")]
    h += [Line2D([], [], color=GRIS_T, lw=1.8, ls="-", label="Ingreso del nuevo seguro"),
          Line2D([], [], color=GRIS_T, lw=1.6, ls=(0, (4, 2)), label="Déficit de GMP")]
    ax.legend(handles=h, frameon=False, fontsize=8.5, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.12))
    _estilo(ax)
    _guardar(fig, "F10b_2_ingreso_deficit", pd.DataFrame(filas))


def f10b_3():
    """Saldo de la reserva por escenario, con el agotamiento en formalidad constante."""
    d = pd.read_csv(E2 / "ingreso_vs_GMP.csv")
    fig, ax = plt.subplots(figsize=(ANCHO, 2.9))
    filas = []
    for e in ("base", "M3", "M2"):
        x = d[d.escenario_masa == e].set_index("anio")
        nom, col, ls, mk = ESC[e]
        ax.plot(x.index, x.k2_reserva_fin / 1000, color=col, lw=2, ls=ls, label=nom)
        for t in x.index:
            filas.append({"escenario": nom, "anio": t, "reserva_cierre_mdp": x.k2_reserva_fin[t]})
        post = x.loc[2035:]
        ago = post.index[(post.k2_reserva_fin <= 0) & (post.k2_reserva_inicio > 0)]
        if len(ago):
            t = int(ago.min())
            ax.plot([t], [0], marker=mk, color=col, ms=7)
            ax.annotate(f"se agota en {t}", (t, 0), xytext=(t + 1.2, 35), fontsize=8.5, color=col,
                        arrowprops=dict(arrowstyle="-", color=col, lw=0.8))
    ax.axvline(2034.5, color="#999999", lw=0.8, ls=":")
    ax.text(2034.7, ax.get_ylim()[1] * 0.97, "desde 2035: retiros", fontsize=8.5, color=GRIS_T, va="top")
    ax.set_xlim(2027, 2054)
    ax.set_xticks([2027, 2030, 2035, 2040, 2045, 2050, 2054])
    ax.set_ylim(0, None)
    ax.set_ylabel("Miles de millones de pesos de 2026")
    ax.legend(frameon=False, ncol=2, fontsize=8.5, loc="upper center", bbox_to_anchor=(0.5, -0.12))
    _estilo(ax)
    _guardar(fig, "F10b_3_reserva", pd.DataFrame(filas))


def f10b_4():
    """Cuña legal a cargo del patrón por nivel de salario, 2030."""
    t = pd.read_csv(E2 / "cuna_legal_por_salario.csv")
    t = t[(t.anio == 2030) & (t.componente == "Total a cargo del patrón (incidencia legal)") & (~t.debajo_del_SM)
          & (t.nivel != "1.01 SM, primer tramo tras el mínimo")]
    etq = {"Salario mínimo": "Salario\nmínimo", "1.01 SM, lectura por UMA": "1.01 SM", "4 UMA": "4 UMA", "5.55 UMA": "5.55 UMA\n(promedio)",
           "10 UMA": "10 UMA", "25 UMA": "25 UMA"}
    t = t[t.nivel.isin(etq)]
    fig, ax = plt.subplots(figsize=(ANCHO, 3.0))
    x = list(range(len(t)))
    for col, nom, c, ls, mk in (("a_ley_vigente", "Ley vigente", "#1a1a1a", "-", "o"),
                                ("b_experimento2", "Seguro solidario", "#1f5fa8", "--", "s"),
                                ("c_experimento2_mas_D2", "Seguro solidario y cuota proporcional", "#d9822b", "-.", "^")):
        ax.plot(x, t[col], color=c, ls=ls, marker=mk, lw=1.6, ms=5, label=nom)
    ax.annotate("escalón justo arriba\ndel salario mínimo", (1, t.a_ley_vigente.iloc[1]), xytext=(1.6, t.a_ley_vigente.iloc[1] + 2.0),
                fontsize=8.5, color=GRIS_T, arrowprops=dict(arrowstyle="-", color=GRIS_T, lw=0.8))
    ax.set_xticks(x, [etq[n] for n in t.nivel])
    ax.set_ylabel("% del salario base de cotización")
    ax.set_ylim(15, max(t.a_ley_vigente) + 4)
    ax.legend(frameon=False, loc="lower right", fontsize=8.5)
    _estilo(ax)
    _guardar(fig, "F10b_4_cuna_legal_2030", t[["nivel", "sbc_uma", "a_ley_vigente", "b_experimento2", "c_experimento2_mas_D2"]])


def main():
    for f in (f10a_1, f10a_2, f10a_3, f10a_4, f10b_1, f10b_2, f10b_3, f10b_4):
        f()


if __name__ == "__main__":
    main()
