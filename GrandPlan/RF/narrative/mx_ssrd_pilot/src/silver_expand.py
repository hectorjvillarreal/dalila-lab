#!/usr/bin/env python3
"""Expand silver/_sparse/<doc>.json into full schema records in silver/<doc>.json.

A sparse episode states only what differs from the defaults. Every filled field
without a quote is added to fields_inferred, which is what the evidence rule says.
Fails loudly on a schema error or a quote that is not verbatim.
"""
import copy
import glob
import json
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script directory
from validate import NEM, NO_EVIDENCE_NEEDED, ROOT, SCHEMA, filled, quote_report, schema_errors, source_text

MULTI = {k for k, v in SCHEMA["properties"].items() if v.get("type") == "array"}
NOT_RECORD = {"episodes", "evidence"}  # every other top-level key is a document-wide default


def default_record(doc):
    rec = {}
    for field, spec in SCHEMA["properties"].items():
        rec[field] = [] if field in MULTI else NEM
    d, m, y = doc["dof_date"].split("-")
    rec.update({
        "Country Name": "Mexico", "Year of the article": y, "relevancetopr_score": 0.0,
        "Is the legislated pension reform minor or major?": "N/A", "dof_publication_date": doc["dof_date"],
        "legislation_date": f"{m}-{y}", "source_file": doc["file"], "chunk_ids": [],
        "Status of Pension Reform": ["Legislated", "Implemented"], "Pension Reform Types": [NEM],
        "reason_reform": [NEM], "regime_affected": ["other"], "insurance_branch": ["other"],
    })
    return rec


def expand(sparse, doc):
    out, problems = [], []
    src = source_text(doc["doc_id"])
    dof = "DOF: " + doc["dof_date"].replace("-", "/")
    for ep in sparse["episodes"]:
        rec = default_record(doc)
        for k, v in sparse.items():
            if k not in NOT_RECORD:
                rec[k] = copy.deepcopy(v)
        label, core = ep["label"], ep.get("core", True)
        for k, v in ep.items():
            if k not in ("label", "core"):
                rec[k] = v
        rec["evidence"] = list(sparse.get("evidence", [])) + ep.get("evidence", [])
        rec["evidence"] += [{"field": f, "quote": dof, "location": "encabezado DOF"}
                            for f in ("dof_publication_date",)]
        have = {e["field"] for e in rec["evidence"]}
        rec["fields_inferred"] = sorted(set(rec.get("fields_inferred", [])) | {
            f for f in SCHEMA["properties"] if f not in NO_EVIDENCE_NEEDED and f not in have and filled(rec, f)})
        for e in schema_errors(rec):
            problems.append(f"{doc['doc_id']} {label}: {e}")
        _, bad, long_ = quote_report(rec, src)
        problems += [f"{doc['doc_id']} {label}: NOT VERBATIM [{b['field']}] {b['quote'][:90]}" for b in bad]
        problems += [f"{doc['doc_id']} {label}: quote over 40 words [{f}]" for f in long_]
        out.append({"label": label, "core": core, "record": rec})
    return out, problems


def main():
    man = {d["doc_id"]: d for d in yaml.safe_load(open(os.path.join(ROOT, "manifest.yaml"), encoding="utf-8"))["documents"]}
    all_problems = []
    wanted = sys.argv[1:] or [os.path.basename(p)[:2] for p in sorted(glob.glob(os.path.join(ROOT, "silver", "_sparse", "*.json")))]
    for doc_id in wanted:
        sparse = json.load(open(os.path.join(ROOT, "silver", "_sparse", doc_id + ".json"), encoding="utf-8"))
        episodes, problems = expand(sparse, man[doc_id])
        all_problems += problems
        json.dump({"doc_id": doc_id, "status": "silver", "episodes": episodes},
                  open(os.path.join(ROOT, "silver", doc_id + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(doc_id, "episodes:", len(episodes), "quotes:", sum(len(e["record"]["evidence"]) for e in episodes))
    print("\n".join(all_problems) if all_problems else "all silver records valid, all quotes verbatim")
    return 1 if all_problems else 0


if __name__ == "__main__":
    sys.exit(main())
