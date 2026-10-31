#!/usr/bin/env python3
"""Convert corpus/raw (untrusted) into corpus/text. Run with `python -I`.

Writes one UTF-8 text per document, fills sha256/size/mtime into manifest.yaml
and logs characters, pages and every clutter rule applied. Code never runs from
corpus/. Companion notes are in src/README.md.
"""
import datetime as dt
import hashlib
import html
import os
import re
import subprocess
import sys
from html.parser import HTMLParser

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = {"p", "br", "tr", "div", "h1", "h2", "h3", "h4", "h5", "li", "table"}
CELL = {"td", "th"}
SKIP = {"script", "style", "title"}  # not "head": the DOF note embeds an unclosed <head>

# DOF page furniture in the PDFs. Conservative: a whole line, nothing inside a paragraph.
PDF_CLUTTER = [
    re.compile(r"^\s*\d*\s*\(?(Primera|Segunda|Tercera|Cuarta) Secci[oó]n\)?\s*(DIARIO OFICIAL)?.*\d{4}\s*$"),
    re.compile(r"^.*DIARIO OFICIAL.*\(?(Primera|Segunda|Tercera|Cuarta) Secci[oó]n\)?\s*\d*\s*$"),
    re.compile(r"^\s*(Lunes|Martes|Mi[eé]rcoles|Jueves|Viernes|S[aá]bado|Domingo) \d+ de \w+ de \d{4}\s*$"),
    re.compile(r"^\s*DIARIO OFICIAL\s*$"),
    re.compile(r"^\s*\(?(Primera|Segunda|Tercera|Cuarta) Secci[oó]n\)?\s*\d*\s*$"),
    re.compile(r"^\s*\d{1,3}\s*$"),
]


class NoteText(HTMLParser):
    """Text of <div id='DivDetalleNota'> only: DOF menus and sidebars live outside it."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.skip = 0
        self.images = 0
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if self.depth:
            if tag == "div":
                self.depth += 1
            if tag in BLOCK:
                self.out.append("\n")
            elif tag in CELL:
                self.out.append(" | ")
            elif tag == "img" and "imagenes_diarios" in (dict(attrs).get("src") or ""):
                self.images += 1
                self.out.append("\n[TABLA PUBLICADA COMO IMAGEN: NO DISPONIBLE EN ESTE TEXTO]\n")
        elif tag == "div" and dict(attrs).get("id") == "DivDetalleNota":
            self.depth = 1

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        if self.depth:
            if tag in BLOCK:
                self.out.append("\n")
            if tag == "div":
                self.depth -= 1

    def handle_data(self, data):
        if self.depth and not self.skip:
            self.out.append(data)


def tidy(text):
    text = html.unescape(text).replace(" ", " ").replace("­", "").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+", " ", ln).strip(" |") for ln in text.split("\n")]
    keep, blank = [], False
    for ln in lines:
        if ln:
            keep.append(ln)
            blank = False
        elif not blank:
            keep.append("")
            blank = True
    return "\n".join(keep).strip() + "\n"


def from_html(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    parser = NoteText()
    parser.feed(raw)
    text = tidy("".join(parser.out))
    # DOF web disclaimer appended to every note: not part of the instrument.
    text = text.split("En el documento que usted está visualizando puede haber texto")[0].rstrip() + "\n"
    return text, {"pages": None, "raw_chars": len(raw), "lines_removed": 0, "image_tables": parser.images}


def from_pdf(path, mode):
    cmd = ["pdftotext", "-enc", "UTF-8"] + (["-layout"] if mode == "layout" else []) + [path, "-"]
    text = subprocess.run(cmd, capture_output=True, check=True).stdout.decode("utf-8", "replace")
    info = subprocess.run(["pdfinfo", path], capture_output=True, text=True, check=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    kept, removed = [], []
    for ln in text.replace("\f", "\n").split("\n"):
        (removed if any(p.match(ln) for p in PDF_CLUTTER) else kept).append(ln)
    return tidy("\n".join(kept)), {"pages": pages, "raw_chars": len(text), "lines_removed": len(removed),
                                   "removed_sample": sorted(set(x.strip() for x in removed if x.strip()))[:6]}


def main():
    path = os.path.join(ROOT, "manifest.yaml")
    man = yaml.safe_load(open(path, encoding="utf-8"))
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M")
    log = open(os.path.join(ROOT, "logs", f"to_text_{stamp}.log"), "w", encoding="utf-8")
    for doc in man["documents"]:
        src = os.path.join(ROOT, "corpus", "raw", doc["file"])
        data = open(src, "rb").read()
        doc["sha256"] = hashlib.sha256(data).hexdigest()
        doc["size_bytes"] = len(data)
        doc["mtime"] = dt.datetime.fromtimestamp(os.path.getmtime(src)).isoformat(timespec="seconds")
        text, meta = from_pdf(src, doc.get("pdf_mode", "layout")) if src.endswith(".pdf") else from_html(src)
        # The DOF date sits outside the note body (HTML) or in the stripped masthead (PDF).
        text = "DOF: " + doc["dof_date"].replace("-", "/") + "\n\n" + text
        out = os.path.join(ROOT, "corpus", "text", doc["doc_id"] + ".txt")
        open(out, "w", encoding="utf-8").write(text)
        doc["text_chars"] = len(text)
        doc["text_sha256"] = hashlib.sha256(text.encode()).hexdigest()
        print(doc["doc_id"], doc["file"], f"chars={len(text)}", meta, file=log)
        doc["image_tables"] = meta.get("image_tables", 0)
        print(doc["doc_id"], f"chars={len(text)}", f"pages={meta['pages']}", f"removed={meta['lines_removed']}",
              f"image_tables={doc['image_tables']}")
    yaml.safe_dump(man, open(path, "w", encoding="utf-8"), allow_unicode=True, sort_keys=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
