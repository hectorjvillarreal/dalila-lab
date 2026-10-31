#!/usr/bin/env python3
"""Classify every failing evidence quote and write eval/quote_failures.csv."""
import collections
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script directory
from validate import ROOT, norm, source_text  # noqa: E402


def classify(q, src, summary):
    nq = norm(q)
    if nq.lower().strip('". ') in ("inferred", "n/a", "na", "not explicitly mentioned", ""):
        return "placeholder (INFERRED, N/A)"
    if "..." in q or "…" in q:
        parts = [norm(p).strip(" .,;\"") for p in re.split(r"\.\.\.|…", q)]
        parts = [p for p in parts if len(p) > 8]
        if parts and all(p in src for p in parts):
            return "elided with ellipsis, all fragments real"
    if nq.lower() in src.lower():
        return "real text, case differs"
    if re.sub(r"\W+", " ", nq).lower().strip() in re.sub(r"\W+", " ", src).lower():
        return "real text, punctuation differs"
    if nq not in norm(summary):
        return "not in the source, added at Stage 2"
    return "not in the source, from Stage 1"


def main():
    rows, tally, totals = [], collections.Counter(), collections.Counter()
    for path in sorted(glob.glob(os.path.join(ROOT, "out", "stage2", "*.json"))):
        d = json.load(open(path, encoding="utf-8"))
        src = source_text(d["doc_id"])
        for e in (d.get("record") or {}).get("evidence", []):
            totals[d["doc_id"]] += 1
            q = e.get("quote", "")
            if q and norm(q) in src:
                continue
            kind = classify(q, src, d["summary"])
            tally[kind] += 1
            rows.append({"doc_id": d["doc_id"], "episode": d["episode"], "field": e.get("field"), "kind": kind, "quote": q})
    with open(os.path.join(ROOT, "eval", "quote_failures.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["doc_id", "episode", "field", "kind", "quote"])
        w.writeheader()
        w.writerows(rows)
    print(sum(totals.values()), "quotes,", len(rows), "failing")
    for k, n in tally.most_common():
        print(f"{n:4d}  {k}")
    per = collections.Counter(r["doc_id"] for r in rows)
    print({k: f"{per[k]}/{v}" for k, v in sorted(totals.items())})
    return 0


if __name__ == "__main__":
    sys.exit(main())
