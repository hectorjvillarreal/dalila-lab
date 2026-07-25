#!/usr/bin/env python3
"""feed.py — Job 1 (feed maintenance) and Job 2 (slot maintenance).

Subcommands:
  check <url> [--text "..."]     dedupe against the absorbed ledger (URLs normalised
                                 first). On a match: report when it was absorbed and
                                 which entries it touched, then STOP (exit 1).
                                 --text additionally flags overlap with watch-item
                                 lines — a flag only; promotion is a human call.
  absorb <url> --date D --entries NNN[,NNN] [--scaffold]
                                 append a record to the ledger (dedupe-checked first).
  slot-update <entry-id> <slot> --set field=value [...] [--source URL] [--fetch]
                                 write TOOL-WRITABLE slot fields only
                                 (value unit delta date source source_type confidence).
                                 Refuses read-only keys, unknown slots (adding a slot
                                 is a human act) and confidence downgrades
                                 (confirmed -> reported requires a human).
                                 --fetch (activated 2026-07-24 by Héctor; opt-in per
                                 invocation) retrieves the --source URL and prints its
                                 text for the operator. Without --fetch this tool
                                 makes no network calls.

This tool never touches prose, archetypes, loadings, decisive flags, or thresholds.
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, parse_qsl

import yaml

ROOT = Path(__file__).resolve().parent.parent
WRITABLE = {"value", "unit", "delta", "date", "source", "source_type", "confidence"}
TRACKING_PARAMS = {"amp", "fbclid", "gclid", "ref", "mc_cid", "mc_eid", "igshid", "spm"}


def ledger_files():
    return sorted(ROOT.glob("instances/*/feed/absorbed.yaml"))


def normalise_url(url):
    """Strip scheme, www., tracking params (?amp, utm_*, ...), fragments, trailing /."""
    s = urlsplit(url.strip())
    host = (s.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = s.path.rstrip("/")
    kept = [(k, v) for k, v in parse_qsl(s.query, keep_blank_values=True)
            if not (k.lower().startswith("utm_") or k.lower() in TRACKING_PARAMS)]
    query = "&".join(f"{k}={v}" if v else k for k, v in kept)
    return f"{host}{path}" + (f"?{query}" if query else "")


def find_match(url):
    norm = normalise_url(url)
    for path in ledger_files():
        records = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        for rec in records:
            stored = rec.get("url_normalised") or normalise_url(rec.get("url", ""))
            if norm == stored:
                return rec, path
            if rec.get("url_truncated_in_source") and norm.startswith(stored):
                return rec, path
    return None, None


def report_match(rec):
    entries = ", ".join(rec.get("entries_touched", [])) or "none"
    line = f"already absorbed {rec.get('absorbed')}, touched entry {entries}"
    if rec.get("scaffold_touched"):
        line += " (scaffold/findings also touched)"
    print(line)


def watch_flag(text):
    """Flag overlap between item text and watch-item lines. A flag, not a decision."""
    words = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z-]{4,}", text)}
    stop = {"whether", "their", "these", "those", "about", "after", "still", "would"}
    words -= stop
    if not words:
        return
    for path in sorted(ROOT.glob("instances/*/board/*.md")):
        content = path.read_text(encoding="utf-8")
        m = re.search(r"\*\*Watch items:\*\*(.+?)(?:\n\n|\n#|\Z)", content, re.S)
        if not m:
            continue
        witems = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z-]{4,}", m.group(1))} - stop
        overlap = sorted(words & witems)
        if len(overlap) >= 2:
            print(f"note: text overlaps watch items of {path.stem} "
                  f"({', '.join(overlap[:6])}) — possible match; promotion is a human call")


def cmd_check(args):
    rec, _ = find_match(args.url)
    if rec:
        report_match(rec)
        return 1
    print("not in ledger")
    if args.text:
        watch_flag(args.text)
    return 0


def cmd_absorb(args):
    rec, _ = find_match(args.url)
    if rec:
        report_match(rec)
        print("refusing to absorb a duplicate")
        return 1
    ledgers = ledger_files()
    if len(ledgers) != 1 and not args.ledger:
        print("multiple instance ledgers exist; pass --ledger PATH")
        return 1
    ledger = Path(args.ledger) if args.ledger else ledgers[0]
    entries = [e.strip() for e in args.entries.split(",")] if args.entries else []
    block = [
        "",
        f'- url: "{args.url}"',
        f'  url_normalised: "{normalise_url(args.url)}"',
        f"  absorbed: {args.date}",
        f'  entries_touched: [{", ".join(chr(34) + e + chr(34) for e in entries)}]',
        f"  scaffold_touched: {'true' if args.scaffold else 'false'}",
        "",
    ]
    with open(ledger, "a", encoding="utf-8") as fh:
        fh.write("\n".join(block))
    print(f"absorbed: recorded in {ledger.relative_to(ROOT)}")
    return 0


def find_entry_yaml(entry_id):
    hits = [p for p in ROOT.glob("instances/*/board/*.yaml") if p.name.startswith(entry_id)]
    return hits[0] if len(hits) == 1 else None


def cmd_slot_update(args):
    updates = {}
    for item in args.set:
        if "=" not in item:
            print(f"bad --set {item!r}; use field=value")
            return 1
        k, v = item.split("=", 1)
        updates[k.strip()] = v.strip()
    if args.source:
        updates.setdefault("source", args.source)

    bad = set(updates) - WRITABLE
    if bad:
        print(f"refused: {sorted(bad)} not tool-writable "
              f"(writable: {sorted(WRITABLE)}). Read-only keys are a human act.")
        return 1

    path = find_entry_yaml(args.entry)
    if path is None:
        print(f"no unique entry YAML for id {args.entry!r}")
        return 1
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    slots = data.get("slots") or {}
    if args.slot not in slots:
        print(f"refused: slot {args.slot!r} does not exist in {path.name}; "
              f"adding a slot is a human act (see scaffold/slot-registry.yaml)")
        return 1
    if updates.get("confidence") == "reported" and slots[args.slot].get("confidence") == "confirmed":
        print("refused: confidence downgrade confirmed -> reported requires a human")
        return 1
    if "confidence" in updates and updates["confidence"] not in {"reported", "confirmed"}:
        print("refused: confidence must be reported|confirmed")
        return 1
    if "source_type" in updates and updates["source_type"] not in {"primary", "secondary"}:
        print("refused: source_type must be primary|secondary")
        return 1

    if args.fetch:
        if not args.source:
            print("--fetch needs --source URL")
            return 1
        from urllib.request import urlopen, Request
        req = Request(args.source, headers={"User-Agent": "automotive-board-feed/1.0"})
        with urlopen(req, timeout=30) as resp:
            raw = resp.read(200_000).decode("utf-8", "replace")
        text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        print("--- fetched source text (operator reads; tool extracts nothing) ---")
        print(text[:4000])
        print("--- end fetched text ---")

    # Targeted line edits inside the slot block, preserving comments and layout.
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    in_slot = False
    slot_indent = None
    changed = set()
    for i, line in enumerate(lines):
        m = re.match(r"^(\s*)([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line.rstrip("\n"))
        if not m:
            continue
        indent, key = len(m.group(1)), m.group(2)
        if indent == 2 and key == args.slot:
            in_slot, slot_indent = True, indent
            continue
        if in_slot and indent <= slot_indent:
            break
        if in_slot and indent == 4 and key in updates:
            val = updates[key]
            rendered = "null" if val in {"null", "~", ""} else (
                val if key == "date" or re.fullmatch(r"(true|false)", val)
                or key in {"confidence", "source_type"}
                else '"' + val.replace('"', r'\"') + '"'
            )
            lines[i] = f"    {key}: {rendered}\n"
            changed.add(key)
    missing = set(updates) - changed
    if missing:
        print(f"refused: field line(s) {sorted(missing)} not found in slot block "
              f"(fields must already exist; adding keys is a human act)")
        return 1
    path.write_text("".join(lines), encoding="utf-8")
    print(f"slot({args.entry}): {args.slot} updated ({', '.join(sorted(changed))}) "
          f"in {path.relative_to(ROOT)}")
    print("reminder: one slot write = one git commit, message per build doc §7")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("check", help="dedupe a URL against the absorbed ledger")
    p.add_argument("url")
    p.add_argument("--text", default=None, help="item text to flag against watch items")
    p.set_defaults(fn=cmd_check)

    p = sub.add_parser("absorb", help="record an absorbed item in the ledger")
    p.add_argument("url")
    p.add_argument("--date", required=True)
    p.add_argument("--entries", default="")
    p.add_argument("--scaffold", action="store_true")
    p.add_argument("--ledger", default=None)
    p.set_defaults(fn=cmd_absorb)

    p = sub.add_parser("slot-update", help="write tool-writable slot fields")
    p.add_argument("entry")
    p.add_argument("slot")
    p.add_argument("--set", action="append", default=[], metavar="field=value")
    p.add_argument("--source", default=None)
    p.add_argument("--fetch", action="store_true",
                   help="retrieve --source over the network (opt-in; activated 2026-07-24)")
    p.set_defaults(fn=cmd_slot_update)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
