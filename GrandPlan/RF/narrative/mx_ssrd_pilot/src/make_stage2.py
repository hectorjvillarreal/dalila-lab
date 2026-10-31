#!/usr/bin/env python3
"""Fill prompts/stage2.template.txt with the anchor (first episode of silver/04.json)."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rec = dict(json.load(open(os.path.join(ROOT, "silver", "04.json"), encoding="utf-8"))["episodes"][0]["record"])
rec["evidence"] = rec["evidence"][:6]  # format only: six entries show the shape at a tenth of the tokens
template = open(os.path.join(ROOT, "prompts", "stage2.template.txt"), encoding="utf-8").read()
out = template.replace("{{ANCHOR}}", json.dumps(rec, ensure_ascii=False, indent=1))
open(os.path.join(ROOT, "prompts", "stage2.txt"), "w", encoding="utf-8").write(out)
print(len(out), "chars")
