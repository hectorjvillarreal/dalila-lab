"""Genera la versión Markdown del documento desde los capítulos LaTeX.

Los capítulos se escriben una sola vez, en LaTeX, con un subconjunto acotado de
comandos. Este script los traduce. No es un conversor general de LaTeX: solo
entiende lo que este documento usa, y falla ruidosamente si aparece algo más.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CAPS = os.path.join(AQUI, "capitulos")
MD_CUADROS = os.path.join(AQUI, "markdown", "cuadros")
SALIDA = os.path.join(AQUI, "markdown", "documento_2025.md")
os.makedirs(os.path.dirname(SALIDA), exist_ok=True)

ORDEN = ["00_nota_metodo", "00_resumen", "01_macro", "02_ingresos", "03_energeticos",
         "04_gasto", "05_pensiones", "06_salud", "07_educacion", "08_inversion",
         "09_energia", "10_seguridad", "11_federalizado", "12_deuda", "13_horizonte",
         "14_implicaciones", "99_anexo"]

# El bloque de ecuacion del capitulo 12 se sustituye entero: en Markdown no hay
# matematicas garantizadas, asi que se escribe la identidad en texto.
ECUACION = (
    "> `d_t = d_(t-1) / (1+n)  +  rfspf  +  fx  +  otros`,   con   "
    "`n = (1+g)(1+pi) - 1`\n")

SUSTITUCIONES = [
    (r"\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}", ""),
    (r"\\chapter\*?\{([^}]*)\}", r"\n## \1\n"),
    (r"\\section\*?\{([^}]*)\}", r"\n### \1\n"),
    (r"\\subsection\*?\{([^}]*)\}", r"\n#### \1\n"),
    (r"\\textbf\{([^{}]*)\}", r"**\1**"),
    (r"\\emph\{([^{}]*)\}", r"*\1*"),
    (r"\\textit\{([^{}]*)\}", r"*\1*"),
    (r"\\marginal\{([^{}]*)\}", r""),
    (r"\\label\{[^}]*\}", ""),
    (r"\\ref\{tab:([^}]*)\}", r"\1"),
    (r"\\ref\{fig:([^}]*)\}", r"\1"),
    (r"\\begin\{itemize\}", ""), (r"\\end\{itemize\}", ""),
    (r"\\begin\{enumerate\}", ""), (r"\\end\{enumerate\}", ""),
    (r"^\s*\\item\s+", "- "),
    (r"\\clearpage", ""), (r"\\newpage", ""), (r"\\noindent", ""),
    (r"\\%", "%"), (r"\\&", "&"), (r"\\_", "_"), (r"\\#", "#"), (r"\\\$", "$"),
    (r"~", " "), (r"---", "—"), (r"--", "–"),
    (r"``", '"'), (r"''", '"'),
]

def convertir(texto: str) -> str:
    # La ecuacion en display se reemplaza antes de todo lo demas.
    texto = re.sub(r"\\\[.*?\\\]", ECUACION, texto, flags=re.DOTALL)
    # \textbf y \emph pueden abarcar saltos de linea: se normalizan primero.
    for cmd, marca in (("textbf", "**"), ("emph", "*"), ("textit", "*")):
        texto = re.sub(r"\\" + cmd + r"\{([^{}]*)\}",
                       lambda m, k=marca: k + " ".join(m.group(1).split()) + k,
                       texto, flags=re.DOTALL)
    # Matematica en linea: se pasa a codigo y se limpian los comandos.
    def _mat(m):
        t = m.group(1)
        for a, b in [(r"\\pi", "pi"), (r"\\,", " "), (r"\\mathrm{", "{"),
                     (r"\\text{", "{"), (r"\\frac", "")]:
            t = re.sub(a, b, t)
        return "`" + re.sub(r"[{}]", "", t).strip() + "`"
    texto = re.sub(r"\$([^$]+)\$", _mat, texto)
    salida = []
    for linea in texto.split("\n"):
        m = re.match(r"\s*\\input\{(?:capitulos/)?cuadros/([A-Za-z0-9_]+)\}", linea)
        if m:
            ruta = os.path.join(MD_CUADROS, m.group(1) + ".md")
            if os.path.exists(ruta):
                salida.append("\n" + open(ruta, encoding="utf-8").read() + "\n")
            else:
                salida.append(f"*(falta el cuadro {m.group(1)})*")
            continue
        if linea.strip().startswith("%"):
            continue
        for pat, rep in SUSTITUCIONES:
            linea = re.sub(pat, rep, linea, flags=re.MULTILINE)
        salida.append(linea)
    t = "\n".join(salida)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t

def main():
    partes = ["# Implicaciones del Paquete Económico 2025",
              "",
              "**Instituto Tecnológico y de Estudios superiores — ITED**  ",
              "**Proyecto FISCUS**",
              "",
              "> Documento de análisis del Paquete Económico 2025, elaborado por el ITED a "
              "partir de los Criterios Generales de Política Económica, la Ley de Ingresos, "
              "el decreto de Presupuesto de Egresos y los analíticos presupuestarios del "
              "Presupuesto de Egresos aprobado.",
              ">",
              "> Este documento es de autoría del ITED. No es una publicación del Centro de "
              "Investigación Económica y Presupuestaria ni de ninguna otra institución. "
              "Donde se cita trabajo de terceros, se cita con documento y página.",
              ""]
    faltan = []
    for nombre in ORDEN:
        ruta = os.path.join(CAPS, nombre + ".tex")
        if not os.path.exists(ruta):
            faltan.append(nombre)
            continue
        partes.append(convertir(open(ruta, encoding="utf-8").read()))
    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(partes))
    n = len(ORDEN) - len(faltan)
    print(f"markdown/documento_2025.md: {n} de {len(ORDEN)} capítulos")
    if faltan:
        print("  faltan:", ", ".join(faltan))
    # Comandos que el conversor no entiende: se reportan, no se ignoran.
    texto = open(SALIDA, encoding="utf-8").read()
    sueltos = sorted(set(re.findall(r"\\[a-zA-Z]+", texto)))
    if sueltos:
        print("  AVISO, comandos LaTeX sin traducir:", ", ".join(sueltos[:12]))

if __name__ == "__main__":
    main()
