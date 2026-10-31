#!/usr/bin/env python3
"""Schema validation plus the evidence check, shared by extract, silver and evaluate.

As a script: `python -I src/validate.py` re-checks every record in out/stage2 and
prints validity, verbatim-quote share and evidence coverage.
"""
import glob
import json
import os
import re
import sys
import unicodedata

from jsonschema import Draft202012Validator

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = json.load(open(os.path.join(ROOT, "schema", "mx_ssrd.schema.json"), encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA)
NEM = "Not explicitly mentioned"
# Document metadata or a coder's score: no quote is expected.
NO_EVIDENCE_NEEDED = {"Country Name", "Year of the article", "relevancetopr_score", "source_file", "chunk_ids",
                      "evidence", "fields_inferred", "Is the legislated pension reform minor or major?"}


def norm(text):
    """Normalize whitespace, line-end hyphenation and accents (build instruction, section 9)."""
    text = text.replace("­", "")
    text = re.sub(r"(\w)-\s+(\w)", r"\1\2", text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", text).strip()


def schema_errors(rec):
    return [f"{'/'.join(map(str, e.path))}: {e.message[:160]}" for e in VALIDATOR.iter_errors(rec)]


def filled(rec, field):
    v = rec.get(field)
    if v in (None, "", [], NEM, [NEM], "N/A"):
        return False
    return True


def quote_report(rec, source_norm):
    """Return (n_quotes, list of failing quotes, list of quotes over 40 words)."""
    bad, long_ = [], []
    ev = rec.get("evidence", [])
    for e in ev:
        q = e.get("quote", "")
        if not q or norm(q) not in source_norm:
            bad.append({"field": e.get("field"), "quote": q})
        if len(q.split()) > 40:
            long_.append(e.get("field"))
    return len(ev), bad, long_


def uncovered(rec):
    """Filled fields with neither a quote nor a fields_inferred entry."""
    have = {e.get("field") for e in rec.get("evidence", [])} | set(rec.get("fields_inferred", []))
    return [f for f in SCHEMA["properties"] if f not in NO_EVIDENCE_NEEDED and filled(rec, f) and f not in have]


def source_text(doc_id):
    return norm(open(os.path.join(ROOT, "corpus", "text", doc_id + ".txt"), encoding="utf-8").read())


def main():
    n = invalid = quotes = badq = gaps = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "out", "stage2", "*.json"))):
        d = json.load(open(path, encoding="utf-8"))
        if d.get("record") is None:
            continue
        rec = d["record"]
        n += 1
        invalid += bool(schema_errors(rec))
        q, bad, _ = quote_report(rec, source_text(d["doc_id"]))
        quotes += q
        badq += len(bad)
        gaps += bool(uncovered(rec))
    print(f"records={n} invalid={invalid} quotes={quotes} failing={badq} records_with_uncovered_fields={gaps}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
