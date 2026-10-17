"""Tablas de reporte, sensibilidades y figuras; registra las cifras de resultados para NUMBERS.md."""

from __future__ import annotations

import matplotlib
import numpy as np
import pandas as pd

from common import FIGURES, H, load, record, table

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

AZUL, NARANJA, AQUA, GRIS = "#2a78d6", "#eb6834", "#1baf7a", "#8a8984"
TINTA, TINTA2 = "#0b0b0b", "#52514e"
REP = H["anios_reporte"]
FUENTE = "Ejercicio preliminar ITED; no es una proyección del IMSS. Fuentes: Informe IMSS 2025-2026; libro de Finanzas 07/09/2026; ENIGH 2024; CONAPO 2023."
NOMBRES = {"base": "Base (S1·G1·U1·T2·C1·F0·π_m 0·perfil 3.0)", "S2": "S2 focalizado", "S3": "S3 amplio",
           "T1": "T1 voluntario", "G2": "G2 aportación federal universal", "U2": "U2 individual (h_b ENIGH)",
           "U2_hInforme": "U2 individual (h_b Informe)", "pim1": "π_m = 1 %", "pim2": "π_m = 2 %",
           "C2": "C2 residuo ocupados − cotizantes", "F1": "F1 +3 M cotizantes", "plano": "Perfil plano",
           "estilizado_2": "Perfil 65+/20-64 = 2", "estilizado_4": "Perfil 65+/20-64 = 4"}


def _estilo(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color("#d6d5d0")
    ax.tick_params(colors=TINTA2, labelsize=8)
    ax.grid(axis="y", color="#ebeae6", lw=0.8)
    ax.set_axisbelow(True)


def tablas(r):
    b = r[(r.corrida == "base") & r.anio.isin(REP)].copy()
    cols = ["anio", "bloque", "personas_cubiertas", "titulares_o_formales"]
    for c in ("pagos_privados", "pagos_GF", "costo", "saldo"):
        cols += [f"{c}_pts_sbc", f"{c}_pct_sem", c, f"{c}_pct_pib_2026"]
    table(b[cols], "resultados_base_anios_reporte")
    t = r[r.bloque == "Total"].set_index(["corrida", "anio"])
    fis = r[r.bloque != "Total"].groupby(["corrida", "anio"]).pagos_GF.sum()
    rows = []
    for c in r.corrida.unique():
        row = {"corrida": c, "descripcion": NOMBRES[c]}
        for y in (2030, 2054):
            row[f"saldo_pts_sbc_{y}"] = t.loc[(c, y), "saldo_pts_sbc"]
            row[f"saldo_mdp_{y}"] = t.loc[(c, y), "saldo"]
            row[f"pagos_GF_pts_sbc_{y}"] = t.loc[(c, y), "pagos_GF_pts_sbc"]
            row[f"pagos_GF_mdp_{y}"] = fis.loc[(c, y)]
            row[f"costo_mdp_{y}"] = t.loc[(c, y), "costo"]
            row[f"personas_cubiertas_{y}"] = t.loc[(c, y), "personas_cubiertas"]
        rows.append(row)
    s = pd.DataFrame(rows)
    base = s.set_index("corrida").loc["base"]
    s["delta_saldo_pts_sbc_2054"] = s.saldo_pts_sbc_2054 - base.saldo_pts_sbc_2054
    s["delta_saldo_pts_sbc_2030"] = s.saldo_pts_sbc_2030 - base.saldo_pts_sbc_2030
    s["delta_GF_pts_sbc_2054"] = s.pagos_GF_pts_sbc_2054 - base.pagos_GF_pts_sbc_2054
    s["orden_impacto_saldo_2054"] = s.delta_saldo_pts_sbc_2054.abs().rank(ascending=False, method="first").astype(int)
    table(s, "sensibilidades")
    bB = r[(r.bloque == "B") & (r.pagos_GF > 0)][["corrida", "anio", "titulares_o_formales", "pagos_GF", "pagos_GF_pts_sbc"]]
    table(bB, "bloque_B_anios_con_costo")
    f1 = t.loc["F1"][["saldo", "pagos_GF"]] - t.loc["base"][["saldo", "pagos_GF"]]
    c = r[(r.corrida == "F1") & (r.bloque == "C")].set_index("anio")
    f1 = f1.join(c[["titulares_o_formales", "personas_cubiertas"]]).rename(
        columns={"saldo": "efecto_neto_SEM_mdp", "pagos_GF": "costo_federal_adicional_mdp",
                 "titulares_o_formales": "cotizantes_F1", "personas_cubiertas": "derechohabientes_F1"})
    f1["efecto_neto_SEM_pts_sbc"] = f1.efecto_neto_SEM_mdp / t.loc["base"].masa_sbc * 100
    table(f1.reset_index(), "bloque_C_efecto_neto_F1")
    return s, f1


def registrar(r, s, f1):
    t = r[r.bloque.isin(["A", "Total"])].set_index(["corrida", "bloque", "anio"])
    for y in REP:
        a = t.loc[("base", "A", y)]
        src = f"resultados_malla.csv, corrida base, Bloque A, {y}"
        record(f"base_A_personas_{y}", round(a.personas_cubiertas), src)
        record(f"base_A_titulares_{y}", round(a.titulares_o_formales), src)
        for c in ("pagos_privados", "pagos_GF", "costo", "saldo", "ingreso"):
            record(f"base_A_{c}_mdp_{y}", round(a[c]), src)
            record(f"base_A_{c}_pts_sbc_{y}", round(a[f"{c}_pts_sbc"], 3), src)
            record(f"base_A_{c}_pct_sem_{y}", round(a[f"{c}_pct_sem"], 2), src)
        record(f"masa_sbc_mdp_{y}", round(a.masa_sbc), "Cotizantes del libro × SBC 627.21 × 1.037 × crecimiento real (Sup_Inc) × 365")
        record(f"ingreso_SEM_mdp_{y}", round(a.ingreso_sem), "Libro, Ingresos IMSS: SEM-A + SEM-GMP")
    a26 = t.loc[("base", "A", 2026)]
    record("base_A_costo_por_persona_2026", round(a26.costo * 1e6 / a26.personas_cubiertas, 2), "Costo Bloque A 2026 / personas cubiertas 2026, pesos de 2026")
    record("base_A_poblacion_objetivo_2026", round(a26.personas_cubiertas / 0.9), "Personas cubiertas 2026 / adopción T2 (0.90)")
    es = load("enigh_edad_sexo")
    es["g"] = np.minimum(es.edad, 90)
    pop = load("conapo_pob").query("anio == 2025")
    pop["g"] = np.minimum(pop.edad, 90)
    e = es.groupby(["g", "sexo"])[["imss", "pob"]].sum()
    imss25 = (pop.groupby(["g", "sexo"]).pob.sum() * e.imss / e.pob).sum()
    record("ENIGH_IMSS_escalado_CONAPO_2025", round(imss25), "Tasa IMSS (inst_1) por edad y sexo de la ENIGH 2024 × CONAPO 2025 (mismo método que el Anexo I del Núcleo 13)")
    record("base_A_costo_pct_pib_2026", round(a26.costo_pct_pib_2026, 3), "Costo Bloque A 2026 / PIB 2026 (nota 51)")
    record("base_A_saldo_pct_pib_2026", round(a26.saldo_pct_pib_2026, 3), "Saldo Bloque A 2026 / PIB 2026")
    record("base_A_pagos_GF_pct_pib_2026", round(a26.pagos_GF_pct_pib_2026, 3), "Pagos federales Bloque A 2026 / PIB 2026")
    for _, x in s.iterrows():
        for y in (2030, 2054):
            record(f"sens_{x.corrida}_saldo_pts_sbc_{y}", round(x[f"saldo_pts_sbc_{y}"], 3), "sensibilidades.csv")
            record(f"sens_{x.corrida}_saldo_mdp_{y}", round(x[f"saldo_mdp_{y}"]), "sensibilidades.csv")
            record(f"sens_{x.corrida}_GF_mdp_{y}", round(x[f"pagos_GF_mdp_{y}"]), "sensibilidades.csv (pagos federales A + B + C)")
            record(f"sens_{x.corrida}_GF_pts_sbc_{y}", round(x[f"pagos_GF_pts_sbc_{y}"], 3), "sensibilidades.csv")
            record(f"sens_{x.corrida}_personas_{y}", round(x[f"personas_cubiertas_{y}"]), "sensibilidades.csv")
    bB = r[(r.corrida == "S3") & (r.bloque == "B")].set_index("anio")
    for y in (2026, 2027, 2028, 2029):
        record(f"S3_B_costo_mdp_{y}", round(bB.loc[y, "pagos_GF"]), "resultados_malla.csv, corrida S3, Bloque B")
        record(f"S3_B_formales_{y}", round(bB.loc[y, "titulares_o_formales"]), "Idem, formales con m < m1")
    for y in (2026, 2030, 2054):
        record(f"F1_efecto_neto_SEM_mdp_{y}", round(f1.loc[y, "efecto_neto_SEM_mdp"]), "bloque_C_efecto_neto_F1.csv")
        record(f"F1_costo_federal_adicional_mdp_{y}", round(f1.loc[y, "costo_federal_adicional_mdp"]), "Idem")
        record(f"F1_derechohabientes_{y}", round(f1.loc[y, "derechohabientes_F1"]), "Idem")
    record("F1_DH_por_cotizante_2030", round(f1.loc[2030, "derechohabientes_F1"] / f1.loc[2030, "cotizantes_F1"], 3), "Idem")


def figuras(r, s):
    FIGURES.mkdir(parents=True, exist_ok=True)
    a = r[(r.corrida == "base") & (r.bloque == "A")].set_index("anio")
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    for col, color, lab in (("costo", NARANJA, "Costo de atención"), ("pagos_privados", AZUL, "Pagos de afiliados"),
                            ("pagos_GF", AQUA, "Pagos federales")):
        y = a[col] / 1000
        ax[0].plot(a.index, y, color=color, lw=2, label=lab)
        ax[0].text(a.index[-1] + 0.4, y.iloc[-1], lab, color=TINTA2, fontsize=8, va="center")
    ax[0].set_title("Bloque A, escenario base (miles de millones de pesos de 2026)", fontsize=10, color=TINTA, loc="left")
    ax[0].set_xlim(2026, 2061)
    ax[0].set_ylim(0, None)
    ax[0].legend(fontsize=8, frameon=False, loc="upper left")
    y = a.saldo_pts_sbc
    ax[1].bar(a.index, y, color=GRIS, width=0.8)
    ax[1].axhline(0, color=TINTA2, lw=0.8)
    ax[1].set_ylim(min(y.min() * 1.2, -0.05), 0.02)
    ax[1].set_title("Saldo del Bloque A (puntos del SBC)", fontsize=10, color=TINTA, loc="left")
    for yr in (2026, 2030, 2040, 2054):
        ax[1].text(yr, y.loc[yr] - 0.02, f"{y.loc[yr]:.2f}", ha="center", va="top", fontsize=7.5, color=TINTA2)
    for x in ax:
        _estilo(x)
    fig.text(0.01, 0.01, FUENTE, fontsize=7, color=TINTA2)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(FIGURES / "bloque_A_base.png", dpi=160)
    plt.close(fig)

    d = s.set_index("corrida").sort_values("saldo_pts_sbc_2054")
    fig, ax = plt.subplots(figsize=(8.5, 5))
    yy = np.arange(len(d))
    base = d.loc["base", "saldo_pts_sbc_2054"]
    ax.axvline(base, color=GRIS, lw=1, ls="--")
    ax.axvline(0, color=TINTA2, lw=0.8)
    ax.hlines(yy, base, d.saldo_pts_sbc_2054, color="#cde2fb", lw=2)
    ax.scatter(d.saldo_pts_sbc_2054, yy, color=[AZUL if i != "base" else TINTA for i in d.index], s=40, zorder=3)
    ax.set_yticks(yy, [NOMBRES[i] for i in d.index], fontsize=8)
    for i, v in zip(yy, d.saldo_pts_sbc_2054):
        ax.text(v + (0.06 if v >= base else -0.06), i, f"{v:+.2f}", va="center", ha="left" if v >= base else "right",
                fontsize=7.5, color=TINTA2)
    lo, hi = d.saldo_pts_sbc_2054.min(), d.saldo_pts_sbc_2054.max()
    ax.set_xlim(lo - 0.35, hi + 0.35)
    ax.set_xlabel("Saldo total para el SEM en 2054 (puntos del SBC)", fontsize=8, color=TINTA2)
    ax.set_title("Sensibilidad del saldo de 2054 (A + B + C)", fontsize=10, color=TINTA, loc="left")
    _estilo(ax)
    ax.grid(axis="x", color="#ebeae6", lw=0.8)
    ax.grid(axis="y", visible=False)
    fig.text(0.01, 0.01, FUENTE, fontsize=6.5, color=TINTA2)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(FIGURES / "sensibilidades_saldo_2054.png", dpi=160)
    plt.close(fig)


def main():
    r = load("resultados_malla")
    s, f1 = tablas(r)
    registrar(r, s, f1)
    figuras(r, s)


if __name__ == "__main__":
    main()
