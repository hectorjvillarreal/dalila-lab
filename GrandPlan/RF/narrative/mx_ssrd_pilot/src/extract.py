#!/usr/bin/env python3
"""Stage 1 and Stage 2 extraction through the local ollama server only.

    python -I src/extract.py --all            whole corpus, reuses finished steps
    python -I src/extract.py --doc 11         one document
    python -I src/extract.py --all --force    redo everything

Rule 1 of the build instruction: the only network call is to localhost.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.request

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)  # -I drops the script directory
import chunk as chunker  # noqa: E402
from validate import ROOT, SCHEMA, schema_errors  # noqa: E402

OLLAMA = "http://localhost:11434"
MODEL = "qwen3.5:9b"
NUM_CTX = 16384
# presence_penalty: the model's Modelfile sets 1.5, which punishes repeating a token,
# and a record repeats "Not explicitly mentioned" dozens of times. Zero keeps the
# controlled values free of that bias. Everything else is as the build instruction says.
OPTIONS = {"temperature": 0, "seed": 20261031, "top_p": 1, "num_ctx": NUM_CTX, "presence_penalty": 0}
STAGE1_PREDICT = 3500
STAGE2_PREDICT = 6000  # an empty pretty-printed record alone costs ~2,600 tokens
THINK_STAGE1 = False
MAX_RETRIES = 2


class Peak:
    """Sample GPU memory during a call."""

    def __init__(self):
        self.mib = 0
        self.stop = threading.Event()
        self.t = threading.Thread(target=self.run, daemon=True)

    def run(self):
        while not self.stop.is_set():
            q = subprocess.run(["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"],
                               capture_output=True, text=True)
            if q.returncode == 0:
                self.mib = max(self.mib, int(q.stdout.strip().split("\n")[0]))
            time.sleep(2)


def post(path, body):
    req = urllib.request.Request(OLLAMA + path, json.dumps(body).encode(), {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=900))


def get(path):
    return json.load(urllib.request.urlopen(OLLAMA + path, timeout=30))


def generate(prompt, predict, think, fmt=None):
    body = {"model": MODEL, "prompt": prompt, "stream": False, "think": think, "keep_alive": "30m",
            "options": {**OPTIONS, "num_predict": predict}}
    if fmt is not None:
        body["format"] = fmt
    t0 = time.time()
    r = post("/api/generate", body)
    return r, {"wall_s": round(time.time() - t0, 1), "prompt_tokens": r.get("prompt_eval_count", 0),
               "gen_tokens": r.get("eval_count", 0), "gen_s": round(r.get("eval_duration", 0) / 1e9, 1),
               "prompt_s": round(r.get("prompt_eval_duration", 0) / 1e9, 1), "done_reason": r.get("done_reason")}


def assert_full_gpu(log):
    post("/api/generate", {"model": MODEL, "prompt": "ok", "stream": False, "think": False, "keep_alive": "30m",
                           "options": {**OPTIONS, "num_predict": 1}})
    m = [x for x in get("/api/ps")["models"] if x["name"] == MODEL][0]
    share = m["size_vram"] / m["size"]
    log.info(f"loaded: size={m['size']} size_vram={m['size_vram']} gpu_share={share:.3f} ctx={m.get('context_length')}")
    if share < 0.999:
        raise SystemExit(f"STOP: model not fully on GPU at num_ctx={NUM_CTX}: {share:.1%}")


class Log:
    def __init__(self, path):
        self.f = open(path, "a", encoding="utf-8")

    def info(self, msg):
        line = f"{dt.datetime.now().isoformat(timespec='seconds')} {msg}"
        print(line, flush=True)
        self.f.write(line + "\n")
        self.f.flush()


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def stage1_call(system, kind, text, log, label):
    prompt = f"{system}\nDOCUMENT TYPE: {kind}\n\nTEXT:\n{text}\n"
    r, m = generate(prompt, STAGE1_PREDICT, THINK_STAGE1)
    log.info(f"stage1 {label} {m}")
    if m["prompt_tokens"] >= NUM_CTX:
        log.info(f"WARNING {label}: prompt filled the context ({m['prompt_tokens']})")
    return r.get("response", ""), r.get("thinking", ""), m


def split_episodes(summary):
    parts = re.split(r"(?m)^#{0,3}\s*EPISODE\s+\d+\s*:\s*", summary)
    if len(parts) == 1:  # a merge can drop the heading; a summary with fields is still one episode
        text = summary.strip()
        return [{"label": "Sin etiqueta", "text": text}] if "|" in text else []
    eps = []
    for p in parts[1:]:
        label, _, rest = p.partition("\n")
        eps.append({"label": label.strip(), "text": "EPISODE: " + label.strip() + "\n" + rest.strip()})
    return eps


def merge_summaries(system, doc_id, summaries, limit, log):
    """Merge chunk summaries. num_ctx 16384 forces batches when they do not fit in one call."""
    round_no = 0
    current = summaries
    while len(current) > 1:
        round_no += 1
        batches, cur, size = [], [], 0
        for s in current:
            if cur and size + len(s) > limit:
                batches.append(cur)
                cur, size = [], 0
            cur.append(s)
            size += len(s)
        batches.append(cur)
        if len(batches) == len(current):  # no batch holds two: halve the longest instead of looping
            raise SystemExit(f"STOP: merge of {doc_id} cannot progress")
        next_round = []
        for i, b in enumerate(batches, 1):
            if len(b) == 1:
                next_round.append(b[0])
                continue
            text, _, _ = stage1_call(system, "(c) A set of chunk summaries from one instrument.",
                                     "\n\n".join(b), log, f"{doc_id}_merge_r{round_no}b{i}")
            open(os.path.join(ROOT, "out", "stage1", f"{doc_id}_merge_r{round_no}b{i}.txt"), "w", encoding="utf-8").write(text)
            next_round.append(text)
        current = next_round
    return current[0]


def run_stage1(doc, system, index, force, log):
    doc_id = doc["doc_id"]
    final = os.path.join(ROOT, "out", "stage1", doc_id + ".txt")
    if os.path.exists(final) and not force:
        return open(final, encoding="utf-8").read()
    summaries = []
    for c in index["documents"][doc_id]["chunks"]:
        cpath = os.path.join(ROOT, "out", "stage1", c["id"] + ".txt")
        if os.path.exists(cpath) and not force:
            summaries.append(open(cpath, encoding="utf-8").read())
            continue
        if c["kind"] == "full":
            text = open(os.path.join(ROOT, "corpus", "text", doc_id + ".txt"), encoding="utf-8").read()
            kind = "(a) A full legal instrument published in the DOF."
        else:
            text = open(os.path.join(ROOT, "corpus", "chunks", c["id"] + ".txt"), encoding="utf-8").read()
            kind = "(b) A chunk of a longer instrument."
        out, trace, _ = stage1_call(system, kind, text, log, c["id"])
        open(cpath, "w", encoding="utf-8").write(out)
        if trace:
            open(os.path.join(ROOT, "out", "stage1", "_trace", c["id"] + ".txt"), "w", encoding="utf-8").write(trace)
        summaries.append(out)
    keep = [s for s in summaries if "EPISODE" in s and s.strip() != "NO EPISODES"]
    if len(summaries) > 1 and keep:
        merged = merge_summaries(system, doc_id, keep, index["limit_chars"], log)
    else:
        merged = keep[0] if keep else "NO EPISODES"
    open(final, "w", encoding="utf-8").write(merged)
    return merged


def run_stage2(doc, ep, n, template, chunk_ids, force, log):
    out_path = os.path.join(ROOT, "out", "stage2", f"{doc['doc_id']}_e{n:02d}.json")
    if os.path.exists(out_path) and not force:
        return json.load(open(out_path, encoding="utf-8"))
    header = f"source_file: {doc['file']}\nchunk_ids: {json.dumps(chunk_ids)}\nDOF: {doc['dof_date']}"
    base = f"{template}\n\n{header}\n\nEPISODE SUMMARY:\n{ep['text']}\n"
    prompt, attempts, errors, rec, metrics = base, [], [], None, []
    for attempt in range(MAX_RETRIES + 1):
        r, m = generate(prompt, STAGE2_PREDICT, False, SCHEMA)
        metrics.append(m)
        raw = r.get("response", "")
        try:
            rec = json.loads(raw)
            errors = schema_errors(rec)
        except json.JSONDecodeError as e:
            rec, errors = None, [f"not JSON: {e}"]
        attempts.append(errors[:5])
        log.info(f"stage2 {doc['doc_id']}_e{n:02d} try {attempt} errors={len(errors)} {m}")
        if not errors:
            break
        prompt = base + "\nYour previous answer failed validation:\n" + "\n".join(errors[:8]) + "\nAnswer again.\n"
    result = {"doc_id": doc["doc_id"], "episode": n, "label": ep["label"], "summary": ep["text"],
              "attempts": len(attempts), "valid": not errors, "errors": errors[:8],
              "record": rec if not errors else None, "raw_failed": None if not errors else raw[:4000],
              "metrics": metrics}
    if rec and not errors:
        rec["source_file"] = doc["file"]
        rec["chunk_ids"] = chunk_ids
    json.dump(result, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--doc", action="append", default=[])
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    if not a.all and not a.doc:
        ap.error("use --all or --doc")
    assert OLLAMA.startswith("http://localhost"), "extraction must stay local"
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M")
    log = Log(os.path.join(ROOT, "logs", f"run_{stamp}.log"))
    tags = [m for m in get("/api/tags")["models"] if m["name"] == MODEL][0]
    log.info(f"model={MODEL} digest={tags['digest']} options={OPTIONS} think_stage1={THINK_STAGE1} "
             f"predict=({STAGE1_PREDICT},{STAGE2_PREDICT})")
    for name in ("prompts/stage1.txt", "prompts/stage2.txt", "schema/mx_ssrd.schema.json", "manifest.yaml"):
        log.info(f"sha256 {name} {sha(os.path.join(ROOT, name))}")
    assert_full_gpu(log)
    chunker.main(NUM_CTX)
    index = json.load(open(os.path.join(ROOT, "corpus", "chunks", "index.json"), encoding="utf-8"))
    log.info(f"chunk limit chars={index['limit_chars']} transitorios_split="
             f"{[k for k, v in index['documents'].items() if v['transitorios_split']]}")
    man = yaml.safe_load(open(os.path.join(ROOT, "manifest.yaml"), encoding="utf-8"))
    system = open(os.path.join(ROOT, "prompts", "stage1.txt"), encoding="utf-8").read()
    template = open(os.path.join(ROOT, "prompts", "stage2.txt"), encoding="utf-8").read()
    peak = Peak()
    peak.t.start()
    for doc in man["documents"]:
        if not a.all and doc["doc_id"] not in a.doc:
            continue
        t0 = time.time()
        summary = run_stage1(doc, system, index, a.force, log)
        episodes = split_episodes(summary)
        log.info(f"doc {doc['doc_id']}: {len(episodes)} episodes after stage 1 ({time.time() - t0:.0f}s)")
        ids = [c["id"] for c in index["documents"][doc["doc_id"]]["chunks"]]
        for n, ep in enumerate(episodes, 1):
            run_stage2(doc, ep, n, template, ids, a.force, log)
        log.info(f"doc {doc['doc_id']} done in {time.time() - t0:.0f}s, peak VRAM so far {peak.mib} MiB")
    peak.stop.set()
    log.info(f"peak VRAM {peak.mib} MiB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
