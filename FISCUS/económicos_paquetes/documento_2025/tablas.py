"""tablas.py — genera cuadros y figuras desde datos/*.csv, en LaTeX y en Markdown.

Regla del pacto §2.3: ninguna cifra se teclea en el cuerpo del texto y ninguna
figura es una imagen pegada. Este módulo es lo que hace exigible esa regla: los
capítulos hacen \\input de lo que sale de aquí, y si un dato cambia, el texto no
se toca.

Salida:
    latex/cuadro_XX.tex     tabular con booktabs y siunitx
    latex/figura_XX.tex     pgfplots leyendo el .csv
    markdown/cuadro_XX.md   el mismo cuadro en Markdown
"""
from __future__ import annotations
import csv, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(AQUI, "datos")
TEX = os.path.join(AQUI, "capitulos", "cuadros")
MD = os.path.join(AQUI, "markdown", "cuadros")
for d in (TEX, MD):
    os.makedirs(d, exist_ok=True)


def _esc(s: str) -> str:
    """Escapa LaTeX. El acento va tal cual porque el documento usa inputenc utf8."""
    s = str(s)
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"),
                 ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"),
                 ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        s = s.replace(a, b)
    return s


def _num(v: str) -> bool:
    return bool(re.fullmatch(r"-?\d+(\.\d+)?", str(v).strip()))


def _fmt(v: str) -> str:
    """Numero -> \\num{} de siunitx, que aplica el formato espanol declarado una vez."""
    v = str(v).strip()
    # OJO: en una columna S de siunitx, cualquier contenido no numerico DEBE ir
    # entre llaves o la compilacion falla. Las celdas vacias son frecuentes
    # (variacion real sin base, columna de la Camara sin dato).
    if v in ("", "nan", "None"):
        return "{---}"
    return r"\num{" + v + "}" if _num(v) else "{" + _esc(v) + "}"


def leer(archivo: str, filtro=None, columnas=None, renombrar=None, limite=None):
    with open(os.path.join(DATOS, archivo), newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    if filtro:
        filas = [r for r in filas if filtro(r)]
    if limite:
        filas = filas[:limite]
    cols = columnas or list(filas[0].keys())
    enc = [(renombrar or {}).get(c, c) for c in cols]
    return enc, [[r.get(c, "") for c in cols] for r in filas]


def cuadro(ident: str, archivo: str, titulo: str, fuente: str, *,
           columnas=None, renombrar=None, filtro=None, limite=None,
           alineacion=None, nota: str = "", ajuste: str = "auto") -> None:
    """`ajuste` decide como se acomoda el cuadro en la caja:
       'float'     table + tabular, lo normal;
       'ancho'     igual pero envuelto en \resizebox para que quepa a lo ancho;
       'largo'     longtable, que si parte entre paginas;
       'auto'      elige por numero de filas y columnas.
    Sin esto, tres cuadros se salen de la caja y cuatro no caben en una pagina."""
    enc, filas = leer(archivo, filtro, columnas, renombrar, limite)
    ncol = len(enc)
    al = alineacion or ("l" + "S" * (ncol - 1))
    if ajuste == "auto":
        ajuste = "largo" if len(filas) > 26 else ("ancho" if ncol > 7 else "float")
    cuerpo_tam = r"\scriptsize" if (ajuste == "largo" and ncol > 7) else r"\small"

    if ajuste == "largo":
        out = [cuerpo_tam,
               r"\begin{longtable}{" + al + "}",
               r"\caption{" + _esc(titulo) + r"}\label{tab:" + ident + r"}\\",
               r"\toprule",
               " & ".join("{" + str(e) + "}" for e in enc) + r" \\",
               r"\midrule\endfirsthead",
               r"\toprule",
               " & ".join("{" + str(e) + "}" for e in enc) + r" \\",
               r"\midrule\endhead",
               r"\bottomrule\endfoot"]
        for fila in filas:
            if str(fila[0]).startswith("--") and not any(str(c).strip() for c in fila[1:]):
                out.append(r"\multicolumn{" + str(ncol) + r"}{l}{\itshape " +
                           _esc(str(fila[0]).strip("- ")) + r"} \\")
                continue
            out.append(" & ".join(_fmt(c) for c in fila) + r" \\")
        pie = r"\par\vspace{2pt}\footnotesize Fuente: " + _esc(fuente) + "."
        if nota:
            pie += r" " + _esc(nota)
        out += [r"\end{longtable}", pie, r"\normalsize", ""]
        with open(os.path.join(TEX, f"{ident}.tex"), "w", encoding="utf-8") as f:
            f.write("\n".join(out))
        _markdown(ident, titulo, enc, filas, ncol, fuente, nota)
        return

    # ---- LaTeX, cuadro flotante
    out = [r"\begin{table}[htbp]", r"\centering",
           r"\caption{" + _esc(titulo) + "}", r"\label{tab:" + ident + "}",
           r"\small"]
    if ajuste == "ancho":
        out.append(r"\resizebox{\textwidth}{!}{%")
    out += [r"\begin{tabular}{" + al + "}", r"\toprule"]
    # Los encabezados van CRUDOS: permiten $d_{t-1}$ y \%. Las celdas si se escapan.
    out.append(" & ".join("{" + str(e) + "}" for e in enc) + r" \\")
    out.append(r"\midrule")
    for fila in filas:
        # Una fila de subtitulo (primera celda con guiones) se pone en cursiva.
        if str(fila[0]).startswith("--") and not any(str(c).strip() for c in fila[1:]):
            out.append(r"\multicolumn{" + str(ncol) + r"}{l}{\itshape " +
                       _esc(str(fila[0]).strip("- ")) + r"} \\")
            continue
        out.append(" & ".join(_fmt(c) for c in fila) + r" \\")
    out += [r"\bottomrule", r"\end{tabular}"]
    if ajuste == "ancho":
        out.append(r"}")
    pie = r"\par\vspace{2pt}\footnotesize Fuente: " + _esc(fuente) + "."
    if nota:
        pie += r" " + _esc(nota)
    out += [pie, r"\end{table}", ""]
    with open(os.path.join(TEX, f"{ident}.tex"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    _markdown(ident, titulo, enc, filas, ncol, fuente, nota)


def _markdown(ident, titulo, enc, filas, ncol, fuente, nota):
    # ---- Markdown
    limpio = [re.sub(r"\\\\[a-zA-Z]+|[$\\\\{}]", "", str(e)).strip() for e in enc]
    md = [f"**Cuadro {ident}. {titulo}**", "",
          "| " + " | ".join(limpio) + " |",
          "|" + "|".join("---" for _ in enc) + "|"]
    for fila in filas:
        if str(fila[0]).startswith("--") and not any(str(c).strip() for c in fila[1:]):
            md.append("| *" + str(fila[0]).strip("- ") + "* |" + " |" * (ncol - 1))
            continue
        md.append("| " + " | ".join("" if str(c).strip() in ("", "nan") else str(c)
                                    for c in fila) + " |")
    md += ["", f"Fuente: {fuente}." + (f" {nota}" if nota else ""), ""]
    with open(os.path.join(MD, f"{ident}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))


def figura(ident: str, titulo: str, fuente: str, *, series: list,
           xlabel: str = "", ylabel: str = "", tipo: str = "linea",
           nota: str = "", origen: str = "") -> None:
    """Emite una figura de pgfplots con las COORDENADAS EN LINEA.

    Las coordenadas se generan desde los .csv de datos/ en tiempo de generacion,
    de modo que la regla del pacto se cumple igual: ninguna cifra se teclea. Lo
    que NO se hace es que el .tex lea el .csv en tiempo de compilacion, porque esa
    es la parte mas fragil de un proyecto LaTeX que no se puede probar aqui: una
    ruta mal resuelta o un separador inesperado tumban el documento entero.

    `series` es una lista de (etiqueta, [(x, y), ...]).
    """
    out = [r"\begin{figure}[htbp]", r"\centering", r"\begin{tikzpicture}",
           r"\begin{axis}[",
           r"  width=0.9\textwidth, height=6.4cm,",
           # Las etiquetas de eje van CRUDAS, como los encabezados: permiten \% y matematicas.
           f"  xlabel={{{xlabel}}}, ylabel={{{ylabel}}},",
           r"  legend style={font=\footnotesize, at={(0.5,-0.24)}, anchor=north,",
           r"                 legend columns=-1, draw=none},",
           r"  tick label style={font=\footnotesize},",
           r"  label style={font=\footnotesize},",
           r"  ymajorgrids=true, grid style={dashed, gray!30},",
           r"  enlarge x limits=0.06,"]
    if tipo == "barra":
        out += [r"  ybar, bar width=9pt,", r"  xtick=data,"]
    else:
        out += [r"  xtick=data,"]
    out.append(r"]")
    for etiqueta, puntos in series:
        estilo = "" if tipo == "barra" else "[mark=*, mark size=1.6pt, thick]"
        coords = " ".join(f"({x},{y})" for x, y in puntos)
        out.append(rf"\addplot{estilo} coordinates {{{coords}}};")
        out.append(r"\addlegendentry{" + _esc(etiqueta) + "}")
    pie = r"\par\vspace{2pt}\footnotesize Fuente: " + _esc(fuente) + "."
    if nota:
        pie += " " + _esc(nota)
    out += [r"\end{axis}", r"\end{tikzpicture}",
            r"\caption{" + _esc(titulo) + "}", r"\label{fig:" + ident + "}",
            pie, r"\end{figure}", ""]
    with open(os.path.join(TEX, f"{ident}.tex"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    md = [f"**Figura {ident}. {titulo}**", ""]
    for etiqueta, puntos in series:
        md.append(f"- *{etiqueta}*: " + ", ".join(f"{x}: {y}" for x, y in puntos))
    md += ["", f"Fuente: {fuente}." + (f" {nota}" if nota else ""),
           f"*(generada desde `datos/{origen}`)*" if origen else "", ""]
    with open(os.path.join(MD, f"{ident}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
