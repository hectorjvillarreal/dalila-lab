#!/usr/bin/env python3
"""Split long documents on article boundaries (build instruction, section 4).

A document stays whole when document + Stage 1 prompt fit in 80% of num_ctx, with
tokens estimated as characters / 3.5. Otherwise: body chunks on `Artículo N` with
one article of overlap, and the transitorios as their own chunk. If the transitorios
alone exceed the budget (possible at num_ctx 16384) they split on their ordinals,
and the split is reported in the chunk index.
"""
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHARS_PER_TOKEN = 3.5
ARTICLE = re.compile(r"^\s*(Art[ií]culo|ART[IÍ]CULO)\s+\d+", re.M)
TRANS_HEAD = re.compile(r"^\s*(ART[IÍ]CULOS\s+)?(TRANSITORIOS?|Transitorios?)\.?\s*$", re.M)
ORD = (r"PRIMERO|SEGUNDO|TERCERO|CUARTO|QUINTO|SEXTO|S[EÉ]PTIMO|OCTAVO|NOVENO|D[EÉ]CIMO|UND[EÉ]CIMO|DUOD[EÉ]CIMO|"
       r"VIG[EÉ]SIMO|TRIG[EÉ]SIMO|CUADRAG[EÉ]SIMO|QUINCUAG[EÉ]SIMO")
TRANS_ITEM = re.compile(rf"^\s*(ART[IÍ]CULO\s+)?({ORD})(\s+({ORD}))?\s*(TRANSITORIO)?\s*[.:\-]", re.M | re.I)


def budget_chars(num_ctx, prompt_chars):
    return int((0.8 * num_ctx - prompt_chars / CHARS_PER_TOKEN) * CHARS_PER_TOKEN)


def pack(pieces, limit, overlap):
    """Greedy packing of ordered pieces; each new chunk repeats the last piece if overlap."""
    chunks, cur, size = [], [], 0
    for piece in pieces:
        if cur and size + len(piece) > limit:
            chunks.append("".join(cur))
            cur = [cur[-1]] if overlap and len(cur[-1]) < limit / 2 else []
            size = sum(map(len, cur))
        cur.append(piece)
        size += len(piece)
    if cur:
        chunks.append("".join(cur))
    return chunks


def split_on(text, regex):
    starts = [m.start() for m in regex.finditer(text)]
    if not starts:
        return [text]
    starts = [0] + [s for s in starts if s > 0]
    return [text[a:b] for a, b in zip(starts, starts[1:] + [len(text)])]


def harden(pieces, limit):
    """Paragraph-split any single piece longer than the limit."""
    out = []
    for p in pieces:
        if len(p) <= limit:
            out.append(p)
        else:
            out += [x + "\n" for x in p.split("\n") if x] if max(map(len, p.split("\n"))) <= limit else \
                   [p[i:i + limit] for i in range(0, len(p), limit)]
    return out


def chunk_document(doc_id, text, limit):
    if len(text) <= limit:
        return [{"id": f"{doc_id}_full", "kind": "full", "text": text}], False
    header = text[:text.find("\n\n", 40) + 2] if "\n\n" in text[:600] else text[:300]
    marks = list(TRANS_HEAD.finditer(text))
    cut = marks[-1].start() if marks else len(text)
    body, trans = text[:cut], text[cut:]
    room = limit - len(header)
    parts = [("body", c) for c in pack(harden(split_on(body, ARTICLE), room), room, overlap=True)]
    trans_split = False
    if trans:
        if len(trans) <= room:
            parts.append(("transitorios", trans))
        else:
            trans_split = True
            parts += [("transitorios", c) for c in pack(harden(split_on(trans, TRANS_ITEM), room), room, overlap=False)]
    out = []
    for i, (kind, c) in enumerate(parts, 1):
        out.append({"id": f"{doc_id}_c{i:02d}", "kind": kind, "text": (header if i > 1 else "") + c})
    return out, trans_split


def main(num_ctx=None):
    man = yaml.safe_load(open(os.path.join(ROOT, "manifest.yaml"), encoding="utf-8"))
    num_ctx = num_ctx or man["num_ctx"]
    prompt = open(os.path.join(ROOT, "prompts", "stage1.txt"), encoding="utf-8").read()
    limit = budget_chars(num_ctx, len(prompt))
    index = {"num_ctx": num_ctx, "limit_chars": limit, "documents": {}}
    for doc in man["documents"]:
        text = open(os.path.join(ROOT, "corpus", "text", doc["doc_id"] + ".txt"), encoding="utf-8").read()
        chunks, trans_split = chunk_document(doc["doc_id"], text, limit)
        for c in chunks:
            if c["kind"] != "full":
                open(os.path.join(ROOT, "corpus", "chunks", c["id"] + ".txt"), "w", encoding="utf-8").write(c["text"])
        index["documents"][doc["doc_id"]] = {
            "chunks": [{"id": c["id"], "kind": c["kind"], "chars": len(c["text"])} for c in chunks],
            "transitorios_split": trans_split}
        print(doc["doc_id"], len(chunks), "chunks", "max", max(len(c["text"]) for c in chunks),
              "TRANSITORIOS SPLIT" if trans_split else "")
    json.dump(index, open(os.path.join(ROOT, "corpus", "chunks", "index.json"), "w", encoding="utf-8"), indent=1)
    print("limit chars per chunk:", limit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
