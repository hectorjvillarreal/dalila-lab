"""Construye los .csv del capítulo de ingresos, desde el artículo 1o. de la Ley de
Ingresos APROBADA de 2024 y 2025, y de la iniciativa (ILIF) de 2025.

Objeto: aprobado contra aprobado, como manda la convención. La ILIF 2025 se
carga aparte para poder decir qué cambió la Cámara, que es información que el
género nunca da porque publica antes de que ocurra.
"""
import sys, os, re, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiscus import emitir, mdp

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = "/tmp/claude-1000/fiscus_cache"
os.makedirs(TMP, exist_ok=True)
DEF = 1.043

# Renglon del art. 1o.: numeracion jerarquica al inicio y el importe al final.
LINEA = re.compile(r"^(\s*)(\d{1,2})\.\s+(.+?)\s{2,}([\d,]+\.\d)\s*$")


def texto(pdf, destino):
    if not os.path.exists(destino):
        subprocess.run(["pdftotext", "-layout", pdf, destino], check=True)
    return open(destino, encoding="utf-8").read()


def art1o(ruta_pdf, etiqueta):
    """Devuelve {clave jerarquica: (nombre, mdp)} del articulo 1o."""
    t = texto(ruta_pdf, os.path.join(TMP, etiqueta + ".txt"))
    out, pila = {}, []
    for linea in t.split("\n"):
        m = LINEA.match(linea)
        if not m:
            continue
        sangria, num, nombre, importe = len(m.group(1)), m.group(2), m.group(3), m.group(4)
        nivel = 0 if sangria < 4 else (1 if sangria < 18 else 2)
        pila = pila[:nivel] + [num]
        clave = ".".join(pila)
        nombre = re.sub(r"\s+", " ", nombre).strip(" .:")
        val = float(importe.replace(",", ""))
        # El PDF repite encabezados de pagina; nos quedamos con la primera aparicion.
        if clave not in out:
            out[clave] = (nombre, val)
    return out


a24 = art1o(os.path.join(RAIZ, "2024", "2024_lif_aprobada.pdf"), "lif2024_art1")
a25 = art1o(os.path.join(RAIZ, "2025", "2025_lif_aprobada.pdf"), "lif2025_art1")
i25 = art1o(os.path.join(RAIZ, "2025", "2025_ilif_iniciativa.pdf"), "ilif2025_art1")

# ------------------------------------------------ C2.1 renglones del art. 1o. ---
# Se emiten los diez renglones de primer nivel y los subrenglones que el capitulo
# usa. Clave jerarquica para que el lector pueda rehacerlo contra el documento.
CLAVES = ["1", "1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18",
          "2", "2.22", "3", "4", "5", "6", "7", "8", "9", "0"]
filas = []
for c in CLAVES:
    n24, v24 = a24.get(c, ("", float("nan")))
    n25, v25 = a25.get(c, ("", float("nan")))
    _, vi = i25.get(c, ("", float("nan")))
    nombre = n25 or n24 or c
    if v24 != v24 or v25 != v25:
        continue
    dif_nom = round(v25 - v24, 1)
    dif_re = round(v25 - v24 * DEF, 1)
    var = round(100 * (v25 / (v24 * DEF) - 1), 1) if v24 else ""
    camara = round(v25 - vi, 1) if vi == vi else ""
    filas.append([c, nombre, v24, v25, dif_nom, dif_re, var, vi if vi == vi else "", camara])
emitir("ingresos_art1o.csv", filas,
       ["clave", "concepto", "mdp_2024_aprobado", "mdp_2025_aprobado",
        "dif_nominal_mdp", "dif_real_mdp", "var_real_pct",
        "mdp_2025_iniciativa", "cambio_de_la_camara_mdp"],
       {"cuadro": "C2.1", "documento": "LIF aprobada 2024 y 2025; ILIF 2025",
        "ubicacion": "articulo 1o., renglones de primer y segundo nivel",
        "tier": "oficial_primaria",
        "nota": "Aprobado contra aprobado. Deflactor 1.043 (CGPE 2025 Anexo II.5). "
                "dif_real en pesos de 2025. La columna de la Camara es la diferencia "
                "entre la ley aprobada y la iniciativa, que el genero no puede dar "
                "porque publica antes de que ocurra."})

# ------------------------------------ serie de cuotas del IMSS para el cap. 5 ---
# Renglon 2.22.01 "Cuotas para el Seguro Social a cargo de patrones y trabajadores".
cuotas = []
for anio, d in (("2022", None), ("2023", None), ("2024", a24), ("2025", a25)):
    if d is None:
        continue
    n, v = d.get("2.22", ("", float("nan")))
    cuotas.append([anio, v])
emitir("cuotas_imss.csv", cuotas, ["ejercicio", "mdp"],
       {"cuadro": "insumo de F5.1", "documento": "LIF aprobada",
        "ubicacion": "articulo 1o., renglon 2.22 Cuotas para la Seguridad Social",
        "tier": "oficial_primaria",
        "nota": "Denominador de la serie aprobada pensiones IMSS / cuotas IMSS. "
                "Los puntos de 2022 (411,852.5) y 2023 (470,845.4) vienen de la corrida 2024."})

print("art. 1o. 2024:", len(a24), "renglones | 2025:", len(a25), "| ILIF 2025:", len(i25))
for c in ["1", "2", "6", "7", "9", "0"]:
    print(f"  {c}: {a24.get(c,('',0))[1]:>12,.1f} -> {a25.get(c,('',0))[1]:>12,.1f}   {a25.get(c,('',''))[0][:52]}")
print("emitidos: ingresos_art1o, cuotas_imss")
