#!/usr/bin/env python3
"""Genera la versión Markdown desde el MISMO contenido LaTeX. Misma sustancia."""
import re
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent
ORDEN = ["00_portada","00_nota_metodo","00_resumen","01_macro","02_ingresos","03_energeticos",
         "04_gasto","05_salud","06_educacion","07_pensiones","08_inversion","09_seguridad",
         "10_federalizado","11_ambiente","12_transversales","13_deuda","14_horizonte",
         "15_implicaciones","99_registro"]
PARTES = {"01_macro":"# (+) Ingresos","04_gasto":"# (−) Gasto",
          "13_deuda":"# (=) Balance y deuda","14_horizonte":"# Cierre"}
CUADROS = {  # id -> (csv, título)
 "C1_1":("macro_marco.csv","Marco macroeconómico"),
 "C1_2":("macro_medianoplazo.csv","Mediano plazo 2025-2031"),
 "C2_1":("ingresos_art1o.csv","Ingresos por renglón del artículo 1o. (línea P)"),
 "C4_1":("finanzas_publicas.csv","Estimación de las finanzas públicas 2025-2026"),
 "C4_2":("gasto_ramos.csv","Gasto bruto por ramo, líneas P y G"),
 "C4_3":("gasto_funcional.csv","Gasto bruto por finalidad y función (línea P)"),
 "C4_4":("gasto_obligatorios.csv","Gastos obligatorios con y sin pensiones"),
 "C4_5":("gce_limite.csv","Gasto corriente estructural contra su límite"),
 "C5_1":("salud_ramo.csv","Función Salud por ramo y entidad (línea P)"),
 "C6_1":("educacion_ramo.csv","Función Educación por ramo (línea P)"),
 "C7_1":("pensiones_no_contributivas.csv","Pensiones no contributivas por número de programa"),
 "C9_1":("seguridad_subfuncion.csv","Perímetro de seguridad: quince subfunciones"),
 "C11_1":("ambiente_agua.csv","Perímetro de medio ambiente y agua"),
 "C12_1":("transversales.csv","Anexos transversales del proyecto 2026"),
 "C12_2":("transversal_igualdad.csv","Composición del anexo de igualdad"),
 "C13_1":("flujos.csv","Los tres flujos"),
 "C13_2":("acervos.csv","Los tres acervos"),
 "C13_3":("techos.csv","Techos de endeudamiento, y lo que no es un techo"),
 "C13_4":("descomposicion.csv","Descomposición en cuatro variables"),
 "C14_1":("percapita.csv","Cifras por habitante y por denominador declarado"),
 "C14_2":("demografia_denominadores.csv","Los denominadores demográficos"),
}

def tabla_md(idc):
    arch, tit = CUADROS[idc]
    d = pd.read_csv(RAIZ / "datos" / arch)
    if idc == "C4_2":
        d = d[d.mdp_2026 > 3000]
    if idc == "C4_3":
        d = d[d.mdp_2026 > 20000]
    if idc == "C12_2":
        d = d.head(12)
    def f(v):
        if pd.isna(v): return "—"
        if isinstance(v, str): return v
        return f"{v:,.1f}".replace(",", " ").replace(".", ",")
    cab = "| " + " | ".join(str(c) for c in d.columns) + " |"
    sep = "|" + "|".join("\x00SEP\x00" for _ in d.columns) + "|"
    filas = ["| " + " | ".join(f(v) for v in r) + " |" for r in d.itertuples(index=False)]
    return f"\n**Cuadro {idc.replace('_','.')} — {tit}**\n\n" + "\n".join([cab, sep] + filas) + "\n"

def limpia(t):
    # El comentario de LaTeX empieza en un % SIN escapar. Sin el lookbehind, esta línea
    # se comía «\\%» y con él el resto del renglón: 218 renglones del entregable de 2026
    # terminaban en una diagonal suelta y sin su signo de porcentaje.
    t = re.sub(r"(?<!\\)%.*", "", t)
    t = re.sub(r"\\input\{capitulos/cuadros/([A-Z0-9_]+)\}", lambda m: tabla_md(m.group(1)), t)
    t = re.sub(r"\\chapter\*?\{([^}]*)\}", r"\n## \1\n", t)
    t = re.sub(r"\\section\*?\{([^}]*)\}", r"\n### \1\n", t)
    t = re.sub(r"\\subsection\*?\{([^}]*)\}", r"\n#### \1\n", t)
    t = re.sub(r"\\titular\{(.*?)\}\n\n", r"\n> \1\n\n", t, flags=re.S)
    t = re.sub(r"\\quecambio\{(.*?)\}\n\n", r"\n**Qué cambió.** \1\n\n", t, flags=re.S)
    t = re.sub(r"\\porqueimporta\{(.*?)\}\n\n", r"\n**Por qué importa.** \1\n\n", t, flags=re.S)
    t = re.sub(r"\\begin\{ficha\}\{([^}]*)\}", r"\n---\n\n**Ficha metodológica — \1**\n", t)
    t = t.replace("\\end{ficha}", "\n---\n")
    t = re.sub(r"\\begin\{recuadro\}\{([^}]*)\}", r"\n---\n\n**Recuadro — \1**\n", t)
    t = t.replace("\\end{recuadro}", "\n---\n")
    t = re.sub(r"\\fila\{([^}]*)\}\{", r"- **\1:** ", t)
    t = re.sub(r"\\marginal\{[^}]*\}", "", t)
    t = re.sub(r"\\textbf\{([^{}]*)\}", r"**\1**", t)
    t = re.sub(r"\\emph\{([^{}]*)\}", r"*\1*", t)
    t = re.sub(r"\\item\[\$\\bullet\$\]", "- ", t)
    t = re.sub(r"\\item\[\d+\.\]", "1. ", t)
    t = re.sub(r"\\item\[\]", "- ", t)
    t = re.sub(r"\\begin\{list\}\{[^}]*\}\{[^}]*\}", "", t)
    t = re.sub(r"\\(begin|end)\{[a-z*]+\}(\{[^}]*\})*", "", t)
    t = re.sub(r"\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}", "", t)
    t = re.sub(r"\\(clearpage|thispagestyle\{empty\}|vfill|normalsize|small|par|centering|raggedright)\b", "", t)
    t = re.sub(r"\\(vspace|hspace)\*?\{[^}]*\}", "", t)
    t = re.sub(r"\\setlength\{[^}]*\}\{[^}]*\}", "", t)
    t = re.sub(r"\\[a-zA-Z]+\{([^{}]*)\}", r"\1", t)
    t = re.sub(r"\\\[|\\\]", "\n", t)
    t = t.replace("\\,", " ").replace("\\%", "%").replace("\\&", "&").replace("\\_", "_")
    t = t.replace("\\\\", "").replace("$-$", "−").replace("---", "—").replace("--", "–")
    t = re.sub(r"\\[a-zA-Z]+", "", t)
    t = re.sub(r"^\s*[\d.]+(pt|cm|em)\]\s*$", "", t, flags=re.M)
    t = re.sub(r"[{}]", "", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

PORTADA = """# Implicaciones del Paquete Económico 2026

**Una lectura del proyecto, escrita bajo las condiciones de una lectura en vivo**

Instituto Tecnológico y de Estudios Superiores de Monterrey · Escuela de Ciencias Sociales y Gobierno

Héctor Juan Villarreal Páez · 7 de septiembre de 2026

*Documento de autoría propia del ITED. No es una publicación del Centro de Investigación
Económica y Presupuestaria ni de ninguna otra institución. Toda cifra lleva su fuente y su
ubicación en el archivo de datos que acompaña al documento.*
"""

partes = ["<!-- Generado desde el mismo contenido LaTeX por a_markdown.py. Misma sustancia. -->"]
for n in ORDEN:
    if n == "00_portada":
        partes.append(PORTADA); continue
    if n in PARTES:
        partes.append("\n" + PARTES[n] + "\n")
    partes.append(limpia((RAIZ / "capitulos" / f"{n}.tex").read_text(encoding="utf-8")))
doc = "\n\n".join(partes).replace("\x00SEP\x00", "---")
(RAIZ / "_entrega" / "documento_2026.md").write_text(doc, encoding="utf-8")
print(f"documento_2026.md: {len(doc):,} caracteres, {doc.count(chr(10))} líneas")
