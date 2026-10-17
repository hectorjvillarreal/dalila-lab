"""Lee el libro de la Dirección de Finanzas (07/09/2026) y lo guarda en formato largo."""

from __future__ import annotations

import openpyxl
import pandas as pd
from openpyxl.utils import column_index_from_string as ci

from common import inp, save

AGES = list(range(15, 101))


def _sheet(wb, name):
    return [list(r) for r in wb[name].iter_rows(values_only=True)]


def _cell(rows, row, col):
    return rows[row - 1][ci(col) - 1]


def ingresos(wb):
    rows = _sheet(wb, "Ingresos IMSS")
    years = [v for v in rows[3][2:34]]
    blocks = {"Consolidado": 5, "SRT": 10, "SEM-A": 15, "SEM-GMP": 20, "SIV": 25, "SGPS": 30, "SSFAM": 35}
    concepts = ["cuotas", "gf", "otros"]
    out = []
    for seguro, r0 in blocks.items():
        for k, c in enumerate(concepts):
            vals = rows[r0 - 1 + k][2:34]
            out += [(seguro, c, int(y), float(v)) for y, v in zip(years, vals)]
    return pd.DataFrame(out, columns=["seguro", "concepto", "anio", "mdp2026"])


def sup_fin(wb):
    rows = _sheet(wb, "Sup_Fin")
    out = [(int(r[0]), float(r[1]), float(r[2])) for r in rows[3:] if isinstance(r[0], (int, float))]
    return pd.DataFrame(out, columns=["anio", "sm_real", "inflacion"])


def sup_inc(wb):
    rows = _sheet(wb, "Sup_Inc_Aseg&Sal")
    out = []
    for r in rows[5:]:
        if isinstance(r[1], (int, float)):
            out.append((int(r[1]), r[ci("E") - 1], r[ci("I") - 1], r[ci("M") - 1], r[ci("Q") - 1]))
    return pd.DataFrame(out, columns=["anio", "crec_aseg", "crec_total", "crec_sbc_aseg", "crec_sbc_total"])


def pob_emp(wb):
    rows = _sheet(wb, "Pob Emp & Nuevos")
    cols = {"aseg_H": "C", "aseg_M": "D", "timss_H": "F", "timss_M": "G", "total": "I",
            "nvo_aseg_H": "J", "nvo_aseg_M": "K", "nvo_timss_H": "M", "nvo_timss_M": "N", "nvo_total": "P"}
    out = []
    for r in rows[7:]:
        if isinstance(r[1], (int, float)):
            out.append({"anio": int(r[1]), **{k: r[ci(c) - 1] for k, c in cols.items()}})
    return pd.DataFrame(out)


def salarios(wb, name):
    rows = _sheet(wb, name)
    cols = {("aseg", "H", "trans"): "C", ("aseg", "H", "actual"): "D", ("aseg", "M", "trans"): "E",
            ("aseg", "M", "actual"): "F", ("timss", "H", "trans"): "H", ("timss", "H", "actual"): "I",
            ("timss", "M", "trans"): "J", ("timss", "M", "actual"): "K"}
    out = []
    for r in range(8, 94):
        edad = _cell(rows, r, "B")
        for (grupo, sexo, gen), c in cols.items():
            out.append((grupo, sexo, gen, int(edad), float(_cell(rows, r, c) or 0.0)))
    df = pd.DataFrame(out, columns=["grupo", "sexo", "generacion", "edad", "sbc"])
    return df, float(_cell(rows, 94, "G"))


def matriz(wb, name, grupo):
    """Matriz por antigüedad (0-50) y edad (15-100); bloques de generación en transición y actual."""
    rows = _sheet(wb, name)
    starts = {"trans": ci("CN"), "actual": ci("FY")}
    out = []
    for sexo, r0 in (("H", 5), ("M", 61)):
        for k in range(51):
            r = rows[r0 - 1 + k]
            assert r[1] == k, (name, sexo, k, r[1])
            for gen, c0 in starts.items():
                for j, edad in enumerate(AGES):
                    v = r[c0 - 1 + j] or 0
                    if v:
                        out.append((grupo, sexo, gen, k, edad, float(v)))
    return pd.DataFrame(out, columns=["grupo", "sexo", "generacion", "antiguedad", "edad", "personas"])


def salidas(wb, name, grupo, last_col):
    rows = _sheet(wb, name)
    out = []
    for sexo, r0 in (("H", 7), ("M", 99)):
        for k, edad in enumerate(AGES):
            r = rows[r0 - 1 + k]
            assert r[1] == edad
            q = sum(float(v or 0) for v in r[2:ci(last_col)])
            out.append((grupo, sexo, edad, min(q, 1.0)))
    return pd.DataFrame(out, columns=["grupo", "sexo", "edad", "q_salida"])


def vector_nuevos(wb):
    rows = _sheet(wb, "Sup_Vect_NvosIng")
    out = []
    for r in rows[5:]:
        if isinstance(r[1], (int, float)):
            e = int(r[1])
            out += [("aseg", "H", e, r[ci("D") - 1]), ("aseg", "M", e, r[ci("E") - 1]),
                    ("timss", "H", e, r[ci("H") - 1]), ("timss", "M", e, r[ci("I") - 1])]
    return pd.DataFrame(out, columns=["grupo", "sexo", "edad", "share"])


def main():
    wb = openpyxl.load_workbook(inp("libro_finanzas"), read_only=True, data_only=True)
    save(ingresos(wb), "libro_ingresos")
    save(sup_fin(wb), "libro_sup_fin")
    save(sup_inc(wb), "libro_sup_inc")
    save(pob_emp(wb), "libro_pob_emp")
    sal25, prom25 = salarios(wb, "Sal SEM-Emp_dic25")
    sal25["prom_hoja"] = prom25
    save(sal25, "libro_sbc_dic25")
    mats = []
    for anio in (24, 25):
        mats.append(matriz(wb, f"Mat_Aseg SEM_dic{anio}", "aseg").assign(anio=2000 + anio))
        mats.append(matriz(wb, f"Mat_TIMSS_SEM_dic{anio}", "timss").assign(anio=2000 + anio))
    save(pd.concat(mats, ignore_index=True), "libro_matrices")
    q = pd.concat([salidas(wb, "Salidas de actividad Asegurados", "aseg", "K"),
                   salidas(wb, "Salida de actividad TIMSS", "timss", "H")], ignore_index=True)
    save(q, "libro_salidas")
    save(vector_nuevos(wb), "libro_vector_nuevos")


if __name__ == "__main__":
    main()
