#!/usr/bin/env python3
"""out/stage2/*.json -> out/records.csv. Lists join with ';', the GPRD cell format."""
import csv
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script directory
from validate import ROOT, SCHEMA  # noqa: E402


def main():
    fields = ["doc_id", "episode", "label", "attempts", "valid"] + list(SCHEMA["properties"])
    rows = []
    for path in sorted(glob.glob(os.path.join(ROOT, "out", "stage2", "*.json"))):
        d = json.load(open(path, encoding="utf-8"))
        row = {k: d.get(k) for k in fields[:5]}
        for k, v in (d.get("record") or {}).items():
            if k == "evidence":
                row[k] = json.dumps(v, ensure_ascii=False)
            elif isinstance(v, list):
                row[k] = ";".join(map(str, v))
            else:
                row[k] = v
        rows.append(row)
    with open(os.path.join(ROOT, "out", "records.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "rows -> out/records.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
