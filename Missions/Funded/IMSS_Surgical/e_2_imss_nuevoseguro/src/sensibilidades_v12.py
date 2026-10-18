"""Instrucción v1.2: sensibilidades sin provisiones y S-masa (secciones 1 y 2), orden de usos y trayectoria de la reserva
en K2 (sección 3), y verificaciones 8.1 a 8.4."""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from comun import CFG, P, PROJECT, YEARS, descuento, record, table
from insumos import cargar
from nuevo_seguro import _max_dif, calcular, corrida, identidad_reserva, simular

ESCS = ("base", "M3", "M2")
ANIOS_R = [2035, 2040, 2045, 2050, 2054]


def _indicadores(d: pd.DataFrame) -> dict:
    x = d.set_index("anio")
    df = descuento(YEARS)
    k1 = x.index[x.k1_deficit_no_cubierto > 0]
    k2 = x.index[x.k2_deficit_no_cubierto > 0]
    m = x.ingreso_NS - x.deficit_GMP
    return {"k1_primer_anio_sin_cobertura": int(k1.min()) if len(k1) else None,
            "k2_primer_anio_sin_cobertura": int(k2.min()) if len(k2) else None,
            "vp_k1_deficit_no_cubierto": float((x.k1_deficit_no_cubierto * df).sum()),
            "vp_k2_deficit_no_cubierto": float((x.k2_deficit_no_cubierto * df).sum()),
            "margen_min": float(m.min()), "margen_min_anio": int(m.idxmin()),
            "margen_2036": float(m[2036]), "margen_2040": float(m[2040])}


def grilla(ins) -> tuple[pd.DataFrame, dict]:
    """Base, M3 y M2 × con/sin provisiones × masa del libro / S-masa, con la regla K2 de la v1.2."""
    rows, sims = [], {}
    for e in ESCS:
        for sp in (False, True):
            for sm in (False, True):
                d = simular(ins, e, True, "v1.2", sin_prov=sp, s_masa=sm)
                sims[(e, sp, sm)] = d
                rows.append({"escenario_masa": e, "provisiones": "sin" if sp else "con", "masa": "S-masa" if sm else "libro",
                             **_indicadores(d)})
    return pd.DataFrame(rows), sims


def razon_ingreso_gmp(ins) -> pd.DataFrame:
    m = ins.masa_esc("base")
    r = ins.gmp_ing.loc[YEARS] / m * 100
    return pd.DataFrame({"anio": YEARS, "ingreso_GMP_V24": ins.gmp_ing.loc[YEARS].values, "masa_propia_base": m.values,
                         "r_pct": r.values})


def reserva_k2(sims: dict) -> pd.DataFrame:
    rows = []
    for e in ESCS:
        x = sims[(e, False, False)].set_index("anio")
        post = x.loc[P["k2_inicio"]:]
        ago = post.index[(post.k2_reserva_fin <= 1e-9) & (post.k2_reserva_inicio > 1e-9)]
        row = {"escenario_masa": e}
        for t in ANIOS_R:
            row[f"saldo_inicio_{t}"] = x.k2_reserva_inicio[t]
        row["retiros_GMP_2035_2054"] = post.k2_retiro_gmp.sum()
        row["retiros_cuidados_2035_2054"] = post.k2_retiro_cuidados.sum()
        row["anio_agotamiento"] = int(ago.min()) if len(ago) else None
        row["saldo_cierre_2054"] = x.k2_reserva_fin[2054]
        rows.append(row)
    return pd.DataFrame(rows)


def k2_v11_faltantes(v11: dict) -> pd.DataFrame:
    """Sección 3.1: lo que hacía el código v1.1 en los años con faltante de GMP desde 2035."""
    rows = []
    for e, d in v11.items():
        x = d.set_index("anio")
        for t in x.index[(x.index >= P["k2_inicio"]) & (x.ingreso_NS < x.deficit_GMP)]:
            rows.append({"escenario_masa": e, "anio": int(t), "faltante_GMP": x.deficit_GMP[t] - x.ingreso_NS[t],
                         "reserva_inicio": x.k2_reserva_inicio[t], "pago_a_cuidados_v11": x.k2_cuidados[t],
                         "deficit_no_cubierto_v11": x.k2_deficit_no_cubierto[t]})
    return pd.DataFrame(rows)


def k2_cambios(v11: dict, v12: dict) -> pd.DataFrame:
    df = descuento(YEARS)
    rows = []
    for e in ESCS:
        a, b = v11[e].set_index("anio"), v12[e].set_index("anio")
        def met(x):
            k2 = x.index[x.k2_deficit_no_cubierto > 0]
            return {"K2: primer año sin cobertura": int(k2.min()) if len(k2) else None,
                    "K2: cuidados, VP 2027-2054": float((x.k2_cuidados * df).sum()),
                    "K2: déficit no cubierto, VP 2027-2054": float((x.k2_deficit_no_cubierto * df).sum()),
                    "K2: reserva al cierre de 2054": float(x.k2_reserva_fin[2054]),
                    "K2: cuidados en 2040": float(x.k2_cuidados[2040]), "K2: cuidados en 2054": float(x.k2_cuidados[2054])}
        ma, mb = met(a), met(b)
        for k in ma:
            va, vb = ma[k], mb[k]
            dif = (vb - va) if isinstance(va, (int, float)) and isinstance(vb, (int, float)) else None
            rows.append({"escenario_masa": e, "concepto": k, "antes_v11": va, "despues_v12": vb, "diferencia": dif})
    return pd.DataFrame(rows)


def verificaciones(ins, sims: dict, v11: dict) -> dict:
    chk = {}
    # 8.1 regresión v1.1
    r = calcular("v1.1")
    v = PROJECT / "data" / "v11"
    for name in ("ingreso_vs_GMP", "valor_presente", "remanente_por_mayor", "resumen"):
        f = "resumen_escenarios" if name == "resumen" else name
        chk[f"8.1 regresión v1.1: {f} (máx. desviación)"] = _max_dif(r[name], pd.read_csv(v / f"{f}.csv"))
    # 8.2 sin provisiones ≤ con provisiones; con provisiones = v1.1
    viol, dev = 0, 0.0
    for e in ESCS:
        for sm in (False, True):
            c, s_ = sims[(e, False, sm)].set_index("anio"), sims[(e, True, sm)].set_index("anio")
            viol += int((s_.deficit_GMP > c.deficit_GMP + 1e-9).sum())
        dev = max(dev, float((sims[(e, False, False)].deficit_GMP.values - v11[e].deficit_GMP.values).__abs__().max()))
    chk["8.2 años con déficit sin provisiones > con provisiones"] = viol
    chk["8.2 déficit con provisiones frente a la v1.1 (máx. desviación, mdp)"] = dev
    # 8.3 S-masa
    b, s_ = sims[("base", False, False)].set_index("anio"), sims[("base", False, True)].set_index("anio")
    chk["8.3 S-masa: ingreso 2027 = ingreso base 2027 (desviación, mdp)"] = float(abs(s_.ingreso_NS[2027] - b.ingreso_NS[2027]))
    q = s_.ingreso_NS / s_.ingreso_GMP_informe
    chk["8.3 S-masa: razón ingreso nuevo / ingreso GMP constante en la base (rango)"] = float(q.max() - q.min())
    # 8.4 K2: sin retiro para cuidados en años con faltante; identidad de la reserva
    n, idt = 0, 0.0
    for key, d in sims.items():
        x = d
        n += int(((x.ingreso_NS < x.deficit_GMP) & (x.k2_retiro_cuidados > 0)).sum())
        lhs = x.k2_reserva_inicio + x.k2_deposito + x.k2_intereses - x.k2_retiro_gmp - x.k2_retiro_cuidados
        idt = max(idt, float((lhs - x.k2_reserva_fin).abs().max()), identidad_reserva(d))
    chk["8.4 K2: años con faltante de GMP y retiro para cuidados"] = n
    chk["8.4 K2: identidad de la reserva (máx. desviación, mdp)"] = idt
    return chk


def main():
    ins = cargar()
    g, sims = grilla(ins)
    table(g, "sensibilidad_provisiones_masa")
    rz = razon_ingreso_gmp(ins)
    table(rz, "razon_ingresoGMP_masa")
    rk = reserva_k2(sims)
    table(rk, "reserva_K2")
    v11 = {e: simular(ins, e, True, "v1.1") for e in ESCS}
    v12 = {e: sims[(e, False, False)] for e in ESCS}
    kf = k2_v11_faltantes(v11)
    table(kf, "k2_v11_anios_con_faltante")
    kc = k2_cambios(v11, v12)
    table(kc, "k2_cambios_v11_v12")
    chk = verificaciones(ins, sims, v11)

    # ---- registro ----
    for _, r in g.iterrows():
        k = f"{r.escenario_masa}_{r.provisiones}prov_{'smasa' if r.masa == 'S-masa' else 'libro'}"
        for c in ("k1_primer_anio_sin_cobertura", "k2_primer_anio_sin_cobertura"):
            v = r[c]
            record(f"{k}_{c}", "ninguno" if v is None or (isinstance(v, float) and np.isnan(v)) else int(v), "sensibilidad_provisiones_masa.csv")
        for c in ("vp_k1_deficit_no_cubierto", "vp_k2_deficit_no_cubierto", "margen_min", "margen_2036", "margen_2040"):
            record(f"{k}_{c}", round(r[c]), "sensibilidad_provisiones_masa.csv, mdp de 2026")
        record(f"{k}_margen_min_anio", int(r.margen_min_anio), "sensibilidad_provisiones_masa.csv")
    rzi = rz.set_index("anio")
    for t in (2027, 2030, 2036, 2040, 2054):
        record(f"r_ingresoGMP_masa_{t}", round(rzi.r_pct[t], 3), "Ingreso de GMP (Cuadro V.24) / masa propia base (%)")
    record("r_ingresoGMP_masa_caida_pct", round((rzi.r_pct[2054] / rzi.r_pct[2027] - 1) * 100, 2), "Caída porcentual de r(t), 2027-2054")
    for _, r in rk.iterrows():
        for t in ANIOS_R:
            record(f"{r.escenario_masa}_k2v12_saldo_inicio_{t}", round(r[f"saldo_inicio_{t}"]), "reserva_K2.csv, mdp de 2026")
        record(f"{r.escenario_masa}_k2v12_retiros_GMP", round(r.retiros_GMP_2035_2054), "reserva_K2.csv, Σ 2035-2054")
        record(f"{r.escenario_masa}_k2v12_retiros_cuidados", round(r.retiros_cuidados_2035_2054), "reserva_K2.csv, Σ 2035-2054")
        a = r.anio_agotamiento
        record(f"{r.escenario_masa}_k2v12_agotamiento", "no se agota" if a is None or (isinstance(a, float) and np.isnan(a)) else int(a), "reserva_K2.csv")
        record(f"{r.escenario_masa}_k2v12_saldo_cierre_2054", round(r.saldo_cierre_2054), "reserva_K2.csv")
    for e in ESCS:
        x = kf[kf.escenario_masa == e] if len(kf) else kf
        record(f"{e}_k2v11_anios_faltante_con_pago", int((x.pago_a_cuidados_v11 > 0).sum()) if len(x) else 0, "k2_v11_anios_con_faltante.csv")
        record(f"{e}_k2v11_pago_cuidados_con_faltante", round(float(x.pago_a_cuidados_v11.sum())) if len(x) else 0, "Σ pagos a cuidados de la v1.1 en años con faltante")
    for _, r in kc.iterrows():
        slug = {"K2: primer año sin cobertura": "primer", "K2: cuidados, VP 2027-2054": "vp_cuidados",
                "K2: déficit no cubierto, VP 2027-2054": "vp_no_cubierto", "K2: reserva al cierre de 2054": "reserva_2054",
                "K2: cuidados en 2040": "cuidados_2040", "K2: cuidados en 2054": "cuidados_2054"}[r.concepto]
        for col in ("antes_v11", "despues_v12"):
            v = r[col]
            record(f"{r.escenario_masa}_k2cambio_{slug}_{col}", "ninguno" if v is None or (isinstance(v, float) and np.isnan(v)) else (int(v) if slug == "primer" else round(v)),
                   "k2_cambios_v11_v12.csv")
    for i, (k, v) in enumerate(chk.items()):
        record(f"chk12_{i:02d}", round(v, 9) if isinstance(v, float) else v, k)
    return chk


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
