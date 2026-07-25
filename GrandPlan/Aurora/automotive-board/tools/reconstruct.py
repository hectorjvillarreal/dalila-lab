#!/usr/bin/env python3
"""reconstruct.py — migration completeness pass (build doc §9).

Concatenates the migrated content (entry prose + rendered facts YAML + instance
findings/archetypes + thresholds) and verifies that the substantive content of the
source board is reproduced: every significant token of the source (numbers, and words
of length >= 4) must appear somewhere in the reconstruction.

Usage: python3 tools/reconstruct.py /path/to/automotive_player_board.md [--dump FILE]
Exit codes: 0 complete · 5 tokens lost.
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def normalise(text):
    text = unicodedata.normalize("NFKC", text)
    text = (text.replace("−", "-").replace("–", "-").replace("—", "-")
                .replace("‘", "'").replace("’", "'")
                .replace("“", '"').replace("”", '"'))
    text = re.sub(r"[*_`>#|]", " ", text)
    return text.lower()


NUM = re.compile(r"\d[\d,.]*%?")
WORD = re.compile(r"[a-z][a-z'-]{3,}")


def tokens(text):
    text = normalise(text)
    nums = {n.rstrip(".,") for n in NUM.findall(text)}
    return nums | set(WORD.findall(text))


def render_yaml(path):
    """Flat rendering of every scalar in a YAML file, so tokens are searchable."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    out = []

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                out.append(str(k))
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
        elif node is not None:
            out.append(str(node))

    walk(data)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", type=Path, help="path to the source board document")
    ap.add_argument("--dump", type=Path, default=None,
                    help="also write the concatenated reconstruction to FILE")
    args = ap.parse_args()

    parts = []
    for pattern in ("scaffold/*.md", "instances/*/archetypes.md", "instances/*/findings.md",
                    "instances/*/board/*.md"):
        for p in sorted(ROOT.glob(pattern)):
            parts.append(p.read_text(encoding="utf-8"))
    for pattern in ("scaffold/*.yaml", "instances/*/board/*.yaml", "instances/*/thresholds.yaml"):
        for p in sorted(ROOT.glob(pattern)):
            parts.append(render_yaml(p))
    recon = "\n\n".join(parts)

    if args.dump:
        args.dump.write_text(recon, encoding="utf-8")

    src_text = args.source.read_text(encoding="utf-8")
    missing = sorted(tokens(src_text) - tokens(recon))

    if missing:
        print(f"INCOMPLETE — {len(missing)} source token(s) not found in reconstruction:")
        norm_src = normalise(src_text)
        for tok in missing:
            idx = norm_src.find(tok)
            ctx = norm_src[max(0, idx - 40): idx + 40].replace("\n", " ") if idx >= 0 else ""
            print(f"  {tok!r}   …{ctx}…")
        return 5
    n = len(tokens(src_text))
    print(f"complete: all {n} significant source tokens present in the reconstruction")
    return 0


if __name__ == "__main__":
    sys.exit(main())
