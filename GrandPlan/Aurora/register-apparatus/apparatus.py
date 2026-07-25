#!/usr/bin/env python3
"""
register-apparatus — obligation scanner for the Aurora corpus.

Read-only lens: parses the Aurora register documents (AI, briefing, geopol,
docs/corpus) plus the cross-project design log, and extracts every open
obligation the documents themselves declare. Renders board.md and appends a
one-line entry to run_log.md.

Disciplines (mirroring spcx_monitor):
  - The corpus documents are the single source of truth. This tool holds NO
    state of its own and never writes outside register-apparatus/.
  - No judgment is fabricated. The board lists what the documents declare
    (pending, corroboration-pending, triggers); deciding whether a trigger
    fired or a claim is corroborated is an analyst/agent action recorded in
    the documents, never here.

Stdlib only. Usage:  python apparatus.py {scan|status}
"""

import os
import re
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
AURORA = os.path.dirname(HERE)
DALILA = os.path.abspath(os.path.join(AURORA, "..", ".."))

SCAN_ROOTS = [
    os.path.join(AURORA, "AI"),
    os.path.join(AURORA, "briefing"),
    os.path.join(AURORA, "geopol"),
    os.path.join(AURORA, "docs", "corpus"),
    os.path.join(DALILA, "_crossrefs", "design_log"),
]

BOARD = os.path.join(HERE, "board.md")
RUN_LOG = os.path.join(HERE, "run_log.md")

TRIGGER_HEADING = re.compile(
    r"^#{2,3}\s+(?:\d+\.\s+)?(review triggers|monitoring triggers)", re.I)
ACTIONS_HEADING = re.compile(r"^#{2,3}\s+actions generated", re.I)
ANY_HEADING = re.compile(r"^#{2,3}\s+")
CORROB = re.compile(r"corroboration[- ]pending|CORROBORATION PENDING", re.I)


def rel(path):
    return os.path.relpath(path, DALILA)


def parse_frontmatter(text):
    """Tolerant line-based YAML-subset parser: scalars, '- ' lists,
    one-level nested maps, '>' folded scalars (kept as one line)."""
    if not text.startswith("---"):
        return {}, text
    lines = text.split("\n")
    fm, body_start = {}, len(lines)
    key = None          # current top-level key collecting a list/fold/nest
    mode = None         # 'list' | 'fold' | 'nest'
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            body_start = i + 1
            break
        if line.startswith((" ", "\t")) or (mode == "list" and line.startswith("- ")):
            stripped = line.strip()
            if mode == "list" and stripped.startswith("- "):
                fm[key].append(stripped[2:].strip())
            elif mode == "fold":
                fm[key] = (fm[key] + " " + stripped).strip()
            elif mode == "nest" and ":" in stripped:
                k, v = stripped.split(":", 1)
                fm[key][k.strip()] = v.strip()
            continue
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            k, v = k.strip(), v.strip()
            if v == ">" or v == "|":
                key, mode, fm[k] = k, "fold", ""
            elif v == "":
                # lookahead decides list vs nested map vs empty scalar
                nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
                if nxt.startswith("- "):
                    key, mode, fm[k] = k, "list", []
                elif lines[i + 1][:1] in (" ", "\t") and ":" in nxt:
                    key, mode, fm[k] = k, "nest", {}
                else:
                    fm[k] = ""
            else:
                fm[k] = v
                key, mode = None, None
    return fm, "\n".join(lines[body_start:])


def strip_comment(value):
    """Split 'Gina    # pending brief activation' -> ('Gina', 'pending brief activation')."""
    if "#" in value:
        v, c = value.split("#", 1)
        return v.strip(), c.strip()
    return value.strip(), ""


def section_bullets(body, heading_re):
    """Collect top-level bullets under a heading until the next heading."""
    out, active, current = [], False, None
    for line in body.split("\n"):
        if heading_re.match(line):
            active = True
            continue
        if active and ANY_HEADING.match(line):
            break
        if active:
            s = line.strip()
            m = re.match(r"^(?:[-*]|\d+\.)\s+(.*)", s)
            if m:
                if current:
                    out.append(current)
                current = m.group(1)
            elif s and current is not None:
                current += " " + s
            elif not s and current is not None:
                out.append(current)
                current = None
    if current:
        out.append(current)
    return out


def scan():
    docs = []
    archived_ids = set()
    for root in SCAN_ROOTS:
        if not os.path.isdir(root):
            continue
        for dirpath, dirs, files in os.walk(root):
            if os.path.basename(dirpath) == "_archive":
                dirs[:] = []
                archived_ids.update(os.path.splitext(fn)[0] for fn in files
                                    if fn.lower().endswith(".md"))
                continue
            for fn in sorted(files):
                path = os.path.join(dirpath, fn)
                if fn.lower().endswith(".md"):
                    with open(path, encoding="utf-8", errors="replace") as f:
                        text = f.read()
                    fm, body = parse_frontmatter(text)
                    docs.append({"path": path, "fm": fm, "body": body, "file": fn})
                else:
                    docs.append({"path": path, "fm": None, "body": None, "file": fn})

    md = [d for d in docs if d["fm"] is not None]
    ids = {d["fm"].get("doc_id", os.path.splitext(d["file"])[0]): d for d in md}
    superseded = {d["fm"].get("supersedes") for d in md} - {None, "", "none", "null"}

    board = {k: [] for k in (
        "approval", "endorsement", "corroboration", "crossrefs",
        "hygiene", "triggers", "actions", "sources", "decay")}

    # -- per-document extraction ------------------------------------------
    # Each doc_id is processed once (a co-located duplicate file adds nothing
    # but a hygiene row); superseded versions contribute only hygiene rows.
    processed = set()
    for d in md:
        fm, body, r = d["fm"], d["body"], rel(d["path"])
        doc_id = fm.get("doc_id", os.path.splitext(d["file"])[0])
        status = fm.get("status", "")

        sup = fm.get("supersedes", "")
        if sup and sup not in ("none", "null") and sup in ids:
            board["hygiene"].append(
                f"`{rel(ids[sup]['path'])}` superseded by `{doc_id}` but still co-located")

        if doc_id in processed or doc_id in superseded:
            continue
        processed.add(doc_id)

        if "pending approval" in status:
            authority = fm.get("approving_authority", "?")
            board["approval"].append(f"`{r}` — status *{status}* → **{authority}**")

        end, _ = strip_comment(str(fm.get("endorsed_by", "")))
        if fm.get("endorsed_by") is not None and end in ("", "null", "none", "None"):
            board["endorsement"].append(f"`{r}` — `endorsed_by` empty")
        for sec, val in (fm.get("section_endorsements") or {}).items():
            who, comment = strip_comment(val)
            if "pending" in comment.lower():
                board["endorsement"].append(
                    f"`{r}` — section *{sec}* → **{who}** ({comment})")

        for line in body.split("\n"):
            if CORROB.search(line):
                board["corroboration"].append(f"`{r}` — {line.strip().lstrip('-*# ')}")

        for ref in (fm.get("cross_refs") or []) + (fm.get("source_refs") or []):
            base = re.split(r"\s{2,}|\s+\[", ref)[0].strip()
            marker = "[pending]" in ref and "pending" or "[thread" in ref and "thread" or None
            if marker == "pending":
                board["crossrefs"].append(f"`{r}` → `{base}` — marked [pending]")
            elif marker == "thread":
                board["crossrefs"].append(f"`{r}` → {base} — thread, no formal note yet")
            elif base in archived_ids and base not in ids:
                board["crossrefs"].append(
                    f"`{r}` → `{base}` — points to archived/superseded version; "
                    f"update pointer at next revision")
            elif base not in ids and not os.path.exists(
                    os.path.join(os.path.dirname(d["path"]), base + ".md")):
                # unresolved only if it looks like a doc_id, not free text
                if re.match(r"^\d{6,8}_", base):
                    board["crossrefs"].append(f"`{r}` → `{base}` — UNRESOLVED (no file found)")

        for t in section_bullets(body, TRIGGER_HEADING):
            board["triggers"].append(f"`{doc_id}` — {t}")
        for a in section_bullets(body, ACTIONS_HEADING):
            board["actions"].append(f"`{doc_id}` — {a}")

        if "estimate_decay" in (fm.get("tags") or []):
            board["decay"].append(
                f"`{r}` — carries `estimate_decay`; numerical magnitudes decay, cite as-of dates")

    # duplicate files across scan roots (e.g. design-log copy in AI/)
    seen = {}
    for d in md:
        seen.setdefault(d["file"], []).append(rel(d["path"]))
    for fn, paths in seen.items():
        if len(paths) > 1:
            board["hygiene"].append("duplicate file in two locations: " + " AND ".join(
                f"`{p}`" for p in paths))

    # non-md sources with no md entry mentioning them
    for d in docs:
        if d["fm"] is None:
            mentioned = any(d["file"] in m["body"] or d["file"] in str(m["fm"])
                            for m in md)
            if not mentioned:
                board["sources"].append(
                    f"`{rel(d['path'])}` — source file with no corpus entry referencing it")

    for k in board:
        board[k] = list(dict.fromkeys(board[k]))
    return board, len(md)


SECTIONS = [
    ("approval", "Pending approval (Héctor)"),
    ("endorsement", "Pending endorsements"),
    ("corroboration", "Corroboration-pending claims"),
    ("crossrefs", "Dangling / pending cross-refs"),
    ("hygiene", "Version & location hygiene"),
    ("sources", "Unprocessed source files"),
    ("triggers", "Live review / monitoring triggers"),
    ("actions", "Actions generated (declared in entries)"),
    ("decay", "Estimate-decay register"),
]


def render(board, n_docs):
    today = datetime.date.today().isoformat()
    total = sum(len(v) for v in board.values())
    lines = [
        "# Aurora apparatus board",
        "",
        f"*Generated by `register-apparatus/apparatus.py scan` on {today} over "
        f"{n_docs} documents. Do not edit — the corpus documents are the "
        f"source of truth; fix things there and re-scan.*",
        "",
        f"**{total} open items.**",
        "",
    ]
    for key, title in SECTIONS:
        items = board[key]
        lines.append(f"## {title} ({len(items)})")
        lines.append("")
        if items:
            lines += [f"- {i}" for i in items]
        else:
            lines.append("- *(none)*")
        lines.append("")
    with open(BOARD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    counts = ", ".join(f"{k}:{len(board[k])}" for k, _ in SECTIONS)
    entry = f"| {today} | {n_docs} | {total} | {counts} |\n"
    if not os.path.exists(RUN_LOG):
        with open(RUN_LOG, "w", encoding="utf-8") as f:
            f.write("# register-apparatus run log\n\n"
                    "Appended by every `scan`. Generated — do not edit.\n\n"
                    "| date | docs | open items | breakdown |\n"
                    "| --- | --- | --- | --- |\n")
    with open(RUN_LOG, "a", encoding="utf-8") as f:
        f.write(entry)
    return total


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "scan"
    board, n = scan()
    if cmd == "scan":
        total = render(board, n)
        print(f"board.md written — {total} open items across {n} documents")
    elif cmd == "status":
        for key, title in SECTIONS:
            print(f"{title}: {len(board[key])}")
            for i in board[key]:
                print(f"  - {re.sub('`', '', i)}")
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
