#!/usr/bin/env python3
"""Qwen vs silver, excluding document 04 (the format anchor).

    python -I src/evaluate.py --suggest   writes eval/episode_match.suggested.csv
    python -I src/evaluate.py             reads eval/episode_match.csv (hand-checked)

Writes eval/metrics.json. Episode matching is by document + measure, by hand in
Phase 0: the suggested table only ranks candidates by legal-reference and label overlap.
"""
import argparse
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script directory
from validate import NEM, ROOT, SCHEMA, norm, quote_report, schema_errors, source_text, uncovered  # noqa: E402

EXCLUDED = {"04"}
SINGLE = [k for k, v in SCHEMA["properties"].items() if "enum" in v]
MULTI = ["Status of Pension Reform", "Pension Reform Types", "reason_reform", "regime_affected", "insurance_branch"]
MMYYYY = ["legislation_date", "Planned_date", "announcement_date", "implementation_date", "reversal_date"]
DDMMYYYY = ["dof_publication_date", "entry_into_force_date"]


def load_model():
    out = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "out", "stage2", "*.json"))):
        d = json.load(open(path, encoding="utf-8"))
        out.setdefault(d["doc_id"], []).append(d)
    return out


def load_silver():
    out = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "silver", "[0-9][0-9].json"))):
        d = json.load(open(path, encoding="utf-8"))
        out[d["doc_id"]] = d["episodes"]
    return out


def words(text):
    return {w for w in re.findall(r"\w{4,}", norm(text).lower())}


def suggest(model, silver):
    path = os.path.join(ROOT, "eval", "episode_match.suggested.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["doc_id", "silver_idx", "silver_label", "core", "model_episode", "model_label", "score"])
        for doc, eps in sorted(silver.items()):
            for i, s in enumerate(eps, 1):
                sw = words(s["label"] + " " + " ".join(s["record"]["legal_references"]))
                ranked = []
                for m in model.get(doc, []):
                    refs = (m.get("record") or {}).get("legal_references", [])
                    mw = words(m["label"] + " " + " ".join(refs))
                    ranked.append((len(sw & mw) / max(1, len(sw | mw)), m["episode"], m["label"]))
                best = max(ranked) if ranked else (0, "", "")
                w.writerow([doc, i, s["label"], s["core"], best[1], best[2], round(best[0], 2)])
    print("wrote", path)


def month_year(v):
    if v == NEM:
        return v
    return v[-7:]


def jaccard(a, b):
    a, b = set(a), set(b)
    return 1.0 if not a and not b else len(a & b) / len(a | b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suggest", action="store_true")
    a = ap.parse_args()
    model, silver = load_model(), load_silver()
    if a.suggest:
        suggest(model, silver)
        return 0
    rows = list(csv.DictReader(open(os.path.join(ROOT, "eval", "episode_match.csv"), encoding="utf-8")))
    pairs = [(r["doc_id"].zfill(2), int(r["silver_idx"]), int(r["model_episode"])) for r in rows if r["model_episode"]]
    docs = [d for d in silver if d not in EXCLUDED]
    n_silver = sum(len(silver[d]) for d in docs)
    n_core = sum(e["core"] for d in docs for e in silver[d])
    n_model = sum(len(model.get(d, [])) for d in docs)
    pairs = [p for p in pairs if p[0] not in EXCLUDED]
    matched_s = {(d, s) for d, s, _ in pairs}
    matched_m = {(d, m) for d, _, m in pairs}
    matched_core = sum(silver[d][s - 1]["core"] for d, s in matched_s)
    per_field = {}

    def add(field, value, informative):
        per_field.setdefault(field, {"all": [], "informative": []})
        per_field[field]["all"].append(value)
        if informative:
            per_field[field]["informative"].append(value)

    for d, s, m in pairs:
        gold = silver[d][s - 1]["record"]
        rec = next((x.get("record") for x in model[d] if x["episode"] == m), None)
        if rec is None:
            continue
        for f in SINGLE:
            add(f, float(gold[f] == rec[f]), gold[f] != NEM)
        for f in MMYYYY:
            add(f, float(gold[f] == rec[f]), gold[f] != NEM)
        for f in DDMMYYYY:
            add(f, float(month_year(gold[f]) == month_year(rec[f])), gold[f] != NEM)
        for f in MULTI:
            add(f, jaccard(gold[f], rec[f]), gold[f] != [NEM])
    fields = {f: {"n": len(v["all"]), "score": round(sum(v["all"]) / len(v["all"]), 3),
                  "n_informative": len(v["informative"]),
                  "score_informative": round(sum(v["informative"]) / len(v["informative"]), 3) if v["informative"] else None}
              for f, v in per_field.items()}
    valid_first = valid_retry = failed = quotes = uncovered_n = 0
    bad = []
    for d, eps in model.items():
        src = source_text(d)
        for e in eps:
            if e["valid"]:
                valid_first += e["attempts"] == 1
                valid_retry += e["attempts"] > 1
                q, b, _ = quote_report(e["record"], src)
                quotes += q
                bad += [{"doc": d, "episode": e["episode"], **x} for x in b]
                uncovered_n += bool(uncovered(e["record"]))
                assert not schema_errors(e["record"])
            else:
                failed += 1
    total = valid_first + valid_retry + failed
    all_scores = [x for v in per_field.values() for x in v["all"]]
    inf_scores = [x for v in per_field.values() for x in v["informative"]]
    metrics = {
        "documents_evaluated": docs,
        "episodes": {"silver": n_silver, "silver_core": n_core, "model": n_model, "matched_pairs": len(pairs),
                     "precision": round(len(matched_m) / max(1, n_model), 3),
                     "recall_all": round(len(matched_s) / max(1, n_silver), 3),
                     "recall_core": round(matched_core / max(1, n_core), 3)},
        "field_mean_all": round(sum(all_scores) / max(1, len(all_scores)), 3),
        "field_mean_informative": round(sum(inf_scores) / max(1, len(inf_scores)), 3),
        "fields": fields,
        "schema": {"outputs": total, "valid_first_try": valid_first, "valid_after_retries": valid_retry, "failed": failed,
                   "share_failed": round(failed / max(1, total), 3)},
        "quotes": {"total": quotes, "failing": len(bad), "share_failing": round(len(bad) / max(1, quotes), 3),
                   "failures": bad},
        "records_with_uncovered_fields": uncovered_n,
    }
    json.dump(metrics, open(os.path.join(ROOT, "eval", "metrics.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in metrics.items() if k not in ("fields", "quotes")}, ensure_ascii=False, indent=1))
    print("quotes", metrics["quotes"]["total"], "failing", metrics["quotes"]["failing"], metrics["quotes"]["share_failing"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
