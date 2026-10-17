"""Esquemas de pago (tabla única π), regla de no arbitraje (7.6), brecha GMP,
cuota fija como % del salario mínimo e indicador de incentivos (sección 4.3)."""

from __future__ import annotations

import json

import matplotlib
import numpy as np
import pandas as pd

from common import (CFG, DERIVED, DIAS, E_RATE, F_G, F_P, FIGURES, NUMBERS_JSON, P, P_STAR, UMA, YEARS,
                    excedente, load, record, subsidio, table)

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

S = CFG["escenarios"]["S"]


def crec_ingreso():
    """Factor de crecimiento del ingreso en múltiplos de la UMA, base dic. 2025 (Sup_Inc, SBC total)."""
    g = load("libro_sup_inc").set_index("anio").crec_sbc_total
    out = {2025: 1.0}
    for t in YEARS:
        out[t] = out[t - 1] * (1 + g.loc[t])
    return out


def sm_en_uma():
    """Salario mínimo en múltiplos de la UMA (la UMA sigue a la inflación; el SM crece en términos reales)."""
    g = load("libro_sup_fin").set_index("anio").sm_real
    out = {2025: P["sm_2025"] / P["uma_dic2025"]}
    for t in YEARS:
        out[t] = out[t - 1] * (1 + g.loc[t])
    return out


def umbrales():
    """m0 y m1 en múltiplos de la UMA de 2026: percentiles de la ENIGH llevados a 2026 y fijos después."""
    reg = json.loads(NUMBERS_JSON.read_text())
    k = (1 + P["sbc_crec_uma_2025"]) * crec_ingreso()[2026]
    out = {}
    for s, q in S.items():
        out[("tit", s)] = (reg[f"m_tit_p{q['p0']}"]["valor"] * k, reg[f"m_tit_p{q['p1']}"]["valor"] * k)
        out[("pc", s)] = (reg[f"m_pc_p{q['p0']}"]["valor"] * k, reg[f"m_pc_p{q['p1']}"]["valor"] * k)
    return out, k


def pagos(m, s, G):
    """Pago anual por titular: (privado del informal, federal por el informal, privado del formal reformado,
    federal por el formal reformado, privado del formal vigente)."""
    e = excedente(m)
    pi = (1 - s) * F_P + e
    if G == "G1":
        pi_i, gf_i = (1 - s) * P_STAR + e, s * P_STAR
    else:
        pi_i, gf_i = pi, F_G + s * F_P
    return pi_i, gf_i, pi, F_G + s * F_P, F_P + e


def verificar_no_arbitraje(th):
    m = np.round(np.arange(0, 25.0001, 0.1), 1)
    rows = []
    for s_id in S:
        for G in ("G1", "G2"):
            for U in ("U1", "U2"):
                m0, m1 = th[("tit" if U == "U1" else "pc", s_id)]
                s = subsidio(m, m0, m1)
                # En U2 el precio por persona × (1 + h_b) es el componente fijo por titular, así que la
                # comparación por titular equivalente coincide con U1; cambian los umbrales (ingreso per cápita).
                pi_i, gf_i, pi_f, gf_f, pi_v = pagos(m, s, G)
                dif = pi_i - pi_f
                esperado = np.zeros_like(m) if G == "G2" else (1 - s) * F_G
                cost_b = s * F_P
                for k in range(len(m)):
                    rows.append({"S": s_id, "G": G, "U": U, "m": m[k], "s": s[k], "pi_I": pi_i[k], "pi_F_reforma": pi_f[k],
                                 "pi_F_vigente": pi_v[k], "dif_I_menos_F": dif[k], "dif_esperada": esperado[k],
                                 "costo_B_por_formal": cost_b[k], "ingreso_total_I": pi_i[k] + gf_i[k],
                                 "P_star_mas_E": P_STAR + excedente(m[k]), "viol_vigente": pi_i[k] < pi_v[k] - 1e-9,
                                 "viol_reforma": pi_i[k] < pi_f[k] - 1e-9, "m1": m1})
    d = pd.DataFrame(rows)
    chk = {
        "7.6.1 no arbitraje (violaciones tras la reforma)": int(d.viol_reforma.sum()),
        "7.6.2 diferencia esperada (casos fuera de ±1 peso)": int((abs(d.dif_I_menos_F - d.dif_esperada) > 1).sum()),
        "7.6.3a Costo_B > 0 con m ≥ m1": int(((d.m >= d.m1) & (d.costo_B_por_formal > 1e-9)).sum()),
        "7.6.3b Costo_B > F_p": int((d.costo_B_por_formal > F_P + 1e-9).sum()),
        "7.6.4 afiliado + GF ≠ P* + E(m)": int((abs(d.ingreso_total_I - d.P_star_mas_E) > 1).sum()),
        "7.6.5 violaciones contra el pago vigente, sin Bloque B": int(d.viol_vigente.sum()),
    }
    table(d.drop(columns=["viol_vigente", "viol_reforma"]).assign(
        viol_vigente=d.viol_vigente, viol_reforma=d.viol_reforma), "no_arbitraje_antes_despues")
    return chk, d


def brecha_gmp():
    m = np.array([1, 2, 2.5, 3, 4, 5, 6, 8, 10, 15, 20, 25], dtype=float)
    d = pd.DataFrame({"m": m, "brecha_GMP_anual": P["gmp_privado"] * m * UMA * DIAS})
    table(d, "brecha_GMP")
    return d


def cuota_fija_sm():
    r = sm_en_uma()
    d = pd.DataFrame({"anio": list(r), "sm_en_uma": list(r.values())})
    d["cuota_fija_pct_sm"] = (P["cf_patron"] + P["cf_gf"]) / d.sm_en_uma * 100
    d["cuota_patronal_pct_sm"] = P["cf_patron"] / d.sm_en_uma * 100
    table(d, "cuota_fija_pct_sm")
    for t in (2025, 2026, 2030, 2054):
        x = d.set_index("anio").loc[t]
        record(f"SM_en_UMA_{t}", round(float(x.sm_en_uma), 4), "SM 2025 / UMA dic. 2025 × Π(1 + SM real, Sup_Fin)")
        record(f"CF_pct_SM_{t}", round(float(x.cuota_fija_pct_sm), 2), "35.23 % UMA / SM del año")
        record(f"CFpat_pct_SM_{t}", round(float(x.cuota_patronal_pct_sm), 2), "20.40 % UMA / SM del año")
    return r


def incentivos(th, sm):
    m = np.array([sm[2026], 2.75, 3.0, 3.25, 3.5, 4, 5, 6, 8, 10])
    rows = []
    for s_id in S:
        m0, m1 = th[("tit", s_id)]
        s = subsidio(m, m0, m1)
        antes = (P["cf_patron"] + P["excedente_patron"] * np.maximum(0, m - 3)) / m * 100
        despues = ((1 - s) * P["cf_patron"] + P["excedente_patron"] * np.maximum(0, m - 3)) / m * 100
        rows += [{"S": s_id, "m": round(float(a), 3), "cuota_patronal_pct_salario_antes": b, "despues": c}
                 for a, b, c in zip(m, antes, despues)]
    table(pd.DataFrame(rows), "indicador_incentivos_2026")


def figura(th, sm):
    m = np.linspace(0, 8, 801)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
    for a, G in zip(ax, ("G1", "G2")):
        m0, m1 = th[("tit", "S1")]
        s = subsidio(m, m0, m1)
        pi_i, _, pi_f, _, pi_v = pagos(m, s, G)
        a.plot(m, pi_v, color="#8a8984", lw=1.6, ls="--", label="Formal vigente π_F^vig")
        a.plot(m, pi_f, color="#2a78d6", lw=2, label="Formal con Bloque B π_F")
        a.plot(m, pi_i, color="#eb6834", lw=2, label="Informal afiliado π_I")
        a.axvspan(0, sm[2026], color="0.92", zorder=0)
        a.text(sm[2026] / 2, 15500, "debajo del SM 2026\n(sin formales)", ha="center", fontsize=8, color="0.35")
        for v, lab in ((m0, "m0"), (m1, "m1")):
            a.axvline(v, color="0.3", lw=0.8, ls=":")
            a.text(v, 300, lab, fontsize=8)
        a.set_title(f"{G} · S1 · pesos de 2026 por titular al año", fontsize=10)
        a.set_xlabel("m (ingreso diario en múltiplos de la UMA)")
        a.grid(alpha=0.25)
    ax[0].set_ylabel("Pago privado anual (pesos de 2026)")
    ax[1].legend(fontsize=8, loc="lower right", frameon=False)
    fig.text(0.01, 0.005, "Ejercicio preliminar ITED. Fuente: Informe IMSS 2025-2026, Cuadro A.3; ENIGH 2024; libro de Finanzas 07/09/2026.",
             fontsize=7, color="0.4")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / "pagos_pi_I_pi_F.png", dpi=160)
    plt.close(fig)


def main():
    th, k = umbrales()
    record("UMA_2026_real", round(UMA, 4), "UMA dic. 2025 × (1 + inflación 2026 de Sup_Fin)")
    record("F_p", round(F_P, 2), "0.2040 × UMA × 365, pesos de 2026")
    record("F_g", round(F_G, 2), "0.1483 × UMA × 365, pesos de 2026")
    record("P_star", round(P_STAR, 2), "0.3523 × UMA × 365, pesos de 2026")
    record("E_por_UMA", round(E_RATE, 2), "0.015 × UMA × 365, pesos de 2026 por UMA sobre 3")
    record("factor_ingreso_2024_2026", round(k, 4), "(1 + 2.6 %) × (1 + crec. real SBC 2026, Sup_Inc)")
    for (base, s_id), (m0, m1) in th.items():
        record(f"umbral_{base}_{s_id}_m0", round(m0, 4), "Percentil ENIGH × factor_ingreso_2024_2026; fijo en UMA después")
        record(f"umbral_{base}_{s_id}_m1", round(m1, 4), "Idem")
    sm = cuota_fija_sm()
    chk, _ = verificar_no_arbitraje(th)
    brecha_gmp()
    incentivos(th, sm)
    figura(th, sm)
    for k, v in chk.items():
        record("chk_" + k.split()[0], v, k)
    (DERIVED / "checks_7_6.json").write_text(json.dumps(chk, ensure_ascii=False, indent=1))
    print(json.dumps(chk, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
