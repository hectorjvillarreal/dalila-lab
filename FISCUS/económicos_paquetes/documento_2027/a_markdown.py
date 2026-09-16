#!/usr/bin/env python3
"""Genera la versión Markdown desde el MISMO contenido LaTeX. Misma sustancia.

Difiere del conversor de 2026 en que aquí los cuadros ya son `.tex` generados
---no CSV---, así que se leen del propio `capitulos/cuadros/` y se traducen.

DEFECTO HEREDADO QUE ESTE ARCHIVO NO REPITE: el comentario de LaTeX empieza en un
`%` SIN escapar. En 2026 la limpieza usaba `%.*` y se comía el resto del renglón
cada vez que aparecía un `\\%`: 218 renglones del entregable terminaban en una
diagonal suelta y sin su signo de porcentaje. El lookbehind lo evita.
"""
from __future__ import annotations
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CAP = AQUI / "capitulos"
SALIDA = AQUI / "_entrega" / "documento_2027.md"


def orden() -> list[tuple[str, str | None]]:
    """Orden y partes, leídos del maestro para no mantener dos listas."""
    t = (AQUI / "main.tex").read_text(encoding="utf-8")
    out, parte = [], None
    for m in re.finditer(r"\\part\*\{\\centering ([^}]*)\}|\\input\{capitulos/([^}]+)\}", t):
        if m.group(1):
            parte = m.group(1).replace("($-$)", "(−)").replace("\\", "")
        else:
            out.append((m.group(2), parte))
            parte = None
    return out


def texto(s: str) -> str:
    """LaTeX en línea -> Markdown. Sin perder porcentajes."""
    s = re.sub(r"(?<!\\)%.*", "", s)                      # comentarios, NO «\%»
    s = s.replace("\\%", "%").replace("\\_", "_").replace("\\&", "&")
    s = s.replace("~", " ").replace("---", "—").replace("--", "–")
    s = re.sub(r"\$-\$", "−", s)
    s = re.sub(r"\\textbf\{(.+?)\}", r"**\1**", s)
    s = re.sub(r"\\emph\{(.+?)\}|\\textit\{(.+?)\}", lambda m: f"*{m.group(1) or m.group(2)}*", s)
    s = re.sub(r"\\texttt\{(.+?)\}", r"`\1`", s)
    s = re.sub(r"\\quad\s*", "  ", s)
    s = re.sub(r"\\(?:midrule|toprule|bottomrule|centering|small|footnotesize|normalsize)\b", "", s)
    s = re.sub(r"\\multicolumn\{\d+\}\{[^}]*\}\{(.*?)\}", r"\1", s)
    s = re.sub(r"\\\\\[[\d.]+(?:pt|cm|em|ex)\]", " ", s)      # \\[6pt] y similares
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{([^{}]*)\})?", r"\3", s)
    s = re.sub(r"[{}]", "", s)
    return re.sub(r"[ \t]+", " ", s).strip()


def cuadro(idc: str) -> str:
    """Un cuadro generado -> tabla de Markdown, con su título y su nota."""
    f = CAP / "cuadros" / f"{idc}.tex"
    if not f.exists():
        return f"*(cuadro {idc} no encontrado)*\n"
    t = f.read_text(encoding="utf-8")
    cap = re.search(r"\\caption\{(.+?)\}\\label", t, re.S)
    cuerpo = re.search(r"\\toprule(.*?)\\bottomrule", t, re.S)
    nota = re.search(r"\\scriptsize (.+?)\\end\{minipage\}", t, re.S)
    filas = []
    for linea in (cuerpo.group(1) if cuerpo else "").split("\\\\"):
        linea = linea.strip()
        if not linea or linea in ("\\midrule",):
            continue
        celdas = [texto(c) for c in linea.split("&")]
        if any(celdas):
            filas.append(celdas)
    out = [f"**Cuadro {idc.replace('_', '.')} — {texto(cap.group(1))}**\n" if cap else ""]
    if filas:
        anchura = max(len(f) for f in filas)
        filas = [f + [""] * (anchura - len(f)) for f in filas]
        out.append("| " + " | ".join(filas[0]) + " |")
        out.append("|" + "|".join(["---"] * anchura) + "|")
        out += ["| " + " | ".join(f) + " |" for f in filas[1:]]
    if nota:
        out.append(f"\n<sub>{texto(nota.group(1))}</sub>")
    return "\n".join(out) + "\n"


def capitulo(nombre: str) -> str:
    t = (CAP / f"{nombre}.tex").read_text(encoding="utf-8")
    t = re.sub(r"(?<!\\)%.*", "", t)
    out = []
    for bloque in re.split(r"\n\s*\n", t):
        b = bloque.strip()
        if not b:
            continue
        if m := re.match(r"\\chapter\*?\{(.+?)\}", b, re.S):
            out.append(f"## {texto(m.group(1))}\n"); continue
        if m := re.match(r"\\(?:sub)?section\*?\{(.+?)\}", b, re.S):
            n = "####" if b.startswith("\\subsection") else "###"
            out.append(f"{n} {texto(m.group(1))}\n"); continue
        if m := re.match(r"\\input\{capitulos/cuadros/(\w+)\}", b):
            out.append(cuadro(m.group(1))); continue
        if m := re.match(r"\\titular\{(.+)\}\s*$", b, re.S):
            out.append(f"> {texto(m.group(1))}\n"); continue
        if m := re.match(r"\\(quecambio|porqueimporta)\{(.+)\}\s*$", b, re.S):
            et = "Qué cambió" if m.group(1) == "quecambio" else "Por qué importa"
            out.append(f"**{et}.** {texto(m.group(2))}\n"); continue
        if b.startswith("\\begin{ficha}"):
            nom = re.search(r"\\begin\{ficha\}\{(.+?)\}", b)
            out.append(f"**Ficha metodológica — {texto(nom.group(1)) if nom else ''}**\n")
            for f in re.finditer(r"\\fila\{(.+?)\}\{(.+?)\}(?=\n\\fila|\n\\end\{ficha\})", b, re.S):
                out.append(f"- **{texto(f.group(1))}:** {texto(f.group(2))}")
            out.append("")
            continue
        if "\\item[$\\bullet$]" in b:
            for it in re.split(r"\\item\[\$\\bullet\$\]", b)[1:]:
                it = re.sub(r"\\end\{list\}.*", "", it, flags=re.S)
                out.append(f"- {texto(it)}")
            out.append("")
            continue
        if b.startswith("\\begin{recuadro}"):
            nom = re.search(r"\\begin\{recuadro\}\{(.+?)\}", b)
            cuerpo = re.sub(r"\\begin\{recuadro\}\{.+?\}|\\end\{recuadro\}", "", b, flags=re.S)
            out.append(f"> **{texto(nom.group(1)) if nom else ''}**\n>\n> {texto(cuerpo)}\n")
            continue
        if b.startswith(("\\begin{list}", "\\end{list}", "\\marginal", "\\addcontentsline")):
            b = re.sub(r"\\(?:begin|end)\{list\}(\{[^}]*\}\{[^}]*\})?|\\marginal\{[^}]*\}|"
                       r"\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}", "", b, flags=re.S).strip()
            if not b:
                continue
        s = texto(b)
        if s:
            out.append(s + "\n")
    return "\n".join(out)


def main() -> int:
    partes = [
        "# Implicaciones del Paquete Económico 2027\n",
        "**Una lectura del proyecto, escrita bajo las condiciones de una lectura en vivo**\n",
        "Instituto Tecnológico y de Estudios Superiores de Monterrey · Escuela de Ciencias\n"
        "Sociales y Gobierno · Héctor Juan Villarreal Páez · 8 de septiembre de 2026\n",
        "*Documento de autoría propia del ITED. No es una publicación del Centro de\n"
        "Investigación Económica y Presupuestaria ni de ninguna otra institución. Toda cifra\n"
        "lleva su fuente y su ubicación en el archivo de datos que acompaña al documento.*\n",
        "*Versión en Markdown del mismo contenido que el PDF; la referencia es el PDF\n"
        "compilado.*\n",
    ]
    for nombre, parte in orden():
        if nombre == "00_portada":      # composición pura, ya sustituida arriba
            continue
        if parte:
            partes.append(f"\n# {parte}\n")
        partes.append(capitulo(nombre))
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text("\n".join(partes), encoding="utf-8")
    txt = SALIDA.read_text(encoding="utf-8")
    print(f"{SALIDA.relative_to(AQUI)}: {len(txt):,} caracteres, "
          f"{len(txt.splitlines()):,} renglones")
    sueltas = [l for l in txt.splitlines() if re.search(r"\\\s*$", l)]
    print(f"renglones que terminan en diagonal suelta (el defecto de 2026): {len(sueltas)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
