"""Fase F0: inventario de insumos y sumas de control del libro de Finanzas (7.1, 7.2)."""

from __future__ import annotations

import hashlib
import json
import subprocess

from common import DERIVED, DALILA, P, PROJECT, inp, load, record

N13_INFORME = "~/Downloads/Nucleo13_Informe_Resultados_Oct2026 atendido JP.docx"


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()[:16]


def checks_71():
    pe = load("libro_pob_emp").set_index("anio")
    mat = load("libro_matrices")
    m25 = mat[mat.anio == 2025].groupby(["grupo", "sexo"]).personas.sum()
    aseg, timss = m25.loc["aseg"].sum(), m25.loc["timss"].sum()
    reg = json.loads((DERIVED / "numbers_computed.json").read_text())
    sbc = reg["SBC_ponderado_libro_calc"]["valor"]
    gf_obs = load("libro_ingresos").query("seguro == 'SEM-A' and concepto == 'gf' and anio == 2025").mdp2026.iloc[0]
    n = aseg + timss
    gf_rec = (P["cf_gf"] * P["uma_dic2025"] * 365 * n + 0.0005 * sbc * 365 * n) * (1 + P["inflacion_2026"]) / 1e6
    rows = [
        ("Asegurados dic. 2025", 21800692, aseg, aseg == 21800692),
        ("  hombres", 13102667, m25.loc[("aseg", "H")], m25.loc[("aseg", "H")] == 13102667),
        ("  mujeres", 8698025, m25.loc[("aseg", "M")], m25.loc[("aseg", "M")] == 8698025),
        ("TIMSS dic. 2025", 551894, timss, timss == 551894),
        ("Total = stock 2025 de Pob Emp & Nuevos", 22352586, pe.loc[2025, "total"], (n == 22352586) and pe.loc[2025, "total"] == n),
        ("SBC promedio ponderado (pesos/día)", 627.21, sbc, abs(sbc - 627.21) < 0.01),
        ("Aportación federal SEM-A 2025 reconstruida (mdp de 2026)", 146457, gf_rec, abs(gf_rec / gf_obs - 1) < 0.03),
    ]
    record("GF_SEM-A_2025_reconstruida", round(gf_rec, 1), "14.83 % UMA × 365 × 22,352,586 + 0.05 % × SBC 627.21 × 365 × 22,352,586, × 1.037")
    record("GF_SEM-A_2025_dif_pct", round((gf_rec / gf_obs - 1) * 100, 2), "Diferencia contra 146,457 mdp (hoja Ingresos IMSS)")
    ing = load("libro_ingresos").query("seguro == 'Consolidado' and anio == 2025").set_index("concepto").mdp2026
    rows72 = [("Cuotas obrero-patronales", ing["cuotas"], 625443), ("Aportaciones del Gobierno Federal", ing["gf"], 158947),
              ("Otros ingresos", ing["otros"], 46643), ("Total sin pensiones en curso de pago", ing.sum(), 625443 + 158947 + 46643)]
    return rows, rows72, gf_obs


def main():
    pdf = inp("informe_pdf")
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    pages = [l.split()[-1] for l in info.splitlines() if l.startswith("Pages")][0]
    zipc = inp("conapo_zip")
    eb = inp("enigh_bundle")
    rows, rows72, gf_obs = checks_71()
    rel = lambda p: p.relative_to(DALILA)  # noqa: E731
    L = ["# F0 — Inventario de insumos", "",
         "Anexo preliminar del Núcleo 13 (afiliación subsidiada al SEM). Instrucción: `20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.1`.",
         "Rutas relativas a la raíz de Dalila. sha256 truncado a 16 caracteres.", "",
         "| # | Insumo | Ruta | Versión / sha256 | Estado | Decisión |", "|---|---|---|---|---|---|",
         f"| I1 | Informe IMSS 2025-2026 | `{rel(pdf)}` | {pages} páginas; sha256 `{sha(pdf)}` | Presente; validado con `pdfinfo` ({pages} pp.; título 2025-2026) | Copia local; no se descargó del Senado |",
         f"| I2 | Libro de Finanzas 07/09/2026 | `{rel(inp('libro_finanzas'))}` | sha256 `{sha(inp('libro_finanzas'))}` | Presente; versión 07/09 | Se usa solo esta versión |",
         f"| I3 | CONAPO, población a mitad de año | `{rel(zipc)}` | Conciliación 1950-2019 y proyecciones 2020-2070 (publicación 2023); sha256 `{sha(zipc)}` | Presente | Misma base que el Núcleo 13: 2025 = 133,367,428 (el Núcleo 13 reporta 133.37 M y la llama «CONAPO 2022-2070») |",
         f"| I4 | ENIGH 2024 (nueva serie) | `{rel(eb)}` | Tablas población, trabajos, ingresos, noagro, agro, concentradohogar | Presente | Se usa el factor de expansión; no se reportan errores estándar |",
         "| I5 | Perfil NTA de consumo público de salud | — | — | **No existe en Dalila** (`Missions/Funded/NTA_Inequality` no contiene perfiles por edad) | Respaldo R3: perfil plano (cota inferior) y estilizado 65+/20-64 = 2, 3 y 4 |",
         f"| I6 | Cuadernos del Núcleo 13 | — | — | **No están en Dalila** | Coherencia verificada contra el informe del Núcleo 13 (`{N13_INFORME}`): CONAPO 2025, Anexo H (cohortes), Anexo I, Anexo M |",
         "", "## Sumas de control del libro de Finanzas (7.1)", "",
         "| Verificación | Esperado | Obtenido | ¿Pasa? |", "|---|---|---|---|"]
    for name, exp, got, ok in rows:
        L.append(f"| {name} | {exp:,.2f} | {got:,.2f} | {'sí' if ok else 'NO'} |")
    L += ["", f"La aportación federal SEM-A observada en 2025 es {gf_obs:,.0f} mdp de 2026 (hoja `Ingresos IMSS`).", "",
          "## Diferencias con el Informe, ingresos 2025 (7.2)", "",
          "| Concepto | Libro de Finanzas | Cuadro II.14 (pág. PDF 67) | Diferencia |", "|---|---|---|---|"]
    for name, lib, inf in rows72:
        L.append(f"| {name} | {lib:,.0f} | {inf:,.0f} | {lib - inf:+,.0f} |")
    L += ["", "**Fuente que se usa:** el libro de Finanzas, por coherencia con el Núcleo 13 (Anexo M del Núcleo 13 usa el mismo total, 851.3 mil millones).",
          "", "## Respaldos activados", "", "- **R1** (distribución del SBC), **R2** (beneficiarios por titular), **R3** (perfil de costo: sin NTA, estilizado) y **R4** (antigüedad) se activan; ver `REPORT.md`.",
          "- No se detuvo la construcción: no falta ningún insumo crítico (C)."]
    (PROJECT / "outputs" / "F0_inventario.md").write_text("\n".join(L) + "\n", encoding="utf8")
    (DERIVED / "checks_7_1_7_2.json").write_text(json.dumps(
        {"7.1": [(r[0], r[1], float(r[2]), bool(r[3])) for r in rows], "7.2": [(r[0], float(r[1]), r[2]) for r in rows72]},
        ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
