#!/usr/bin/env python3
"""validate.py — schema, pairing, boundary and scaffold-purity checks.

Jobs (build doc §6.4):
  1. Schema conformance across all entry YAML and thresholds.yaml.
  2. Every .md in board/ has a matching .yaml, and vice versa.
  3. --check-boundary: fail if any READ-ONLY key changed vs the reference
     (git HEAD if a repo exists, else the snapshot baseline .boundary-baseline.json;
     refresh the snapshot with --snapshot after intended human edits).
  4. scaffold/ purity: warn on instance-specific vocabulary (warning, not error).

The tool validates facts infrastructure only. It never reads meaning into any value.
Exit codes: 0 ok · 1 schema/pairing errors · 2 boundary violation.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BASELINE = ROOT / ".boundary-baseline.json"

# The automation boundary (build doc §5.1): tool-writable fields, only inside slots.*
WRITABLE_SLOT_FIELDS = {"value", "unit", "delta", "date", "source", "source_type", "confidence"}
READONLY_SLOT_FIELDS = {"decisive", "notes"}
ALLOWED_SLOT_FIELDS = WRITABLE_SLOT_FIELDS | READONLY_SLOT_FIELDS
ENTRY_TOP_KEYS = {"id", "player", "archetype_ref", "slots"}
CONFIDENCE_VALUES = {"reported", "confirmed"}
SOURCE_TYPE_VALUES = {"primary", "secondary"}
THRESHOLD_KEYS = {"id", "entry", "description", "due", "status", "due_passed", "resolution"}
THRESHOLD_WRITABLE = {"due_passed"}  # the only tool-writable threshold field

# scaffold purity: default instance-vocabulary term list (configurable via --terms FILE,
# one term per line). Word-boundary matched, case-insensitive except all-caps terms.
DEFAULT_PURITY_TERMS = [
    "Geely", "Zeekr", "BYD", "Huawei", "Xiaomi", "Toyota", "Volkswagen", "VW",
    "Tesla", "Hyundai", "Chery", "Leapmotor", "Polestar", "Volvo", "Lotus",
    "EV", "NEV", "BEV", "China", "Chinese", "Japan", "Korea", "Germany",
    "tariff", "car", "cars", "automotive", "vehicle", "automaker", "JAMA",
    "pharma",
]


def err(msgs, m):
    msgs.append(m)


def load_yaml(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def instance_dirs():
    inst_root = ROOT / "instances"
    return sorted(p for p in inst_root.iterdir() if p.is_dir()) if inst_root.is_dir() else []


# ---------------------------------------------------------------- schema

def check_entry_schema(path, data, errors):
    rel = path.relative_to(ROOT)
    if not isinstance(data, dict):
        err(errors, f"{rel}: not a mapping")
        return
    missing = ENTRY_TOP_KEYS - set(data)
    if missing:
        err(errors, f"{rel}: missing top-level keys {sorted(missing)}")
    extra = set(data) - ENTRY_TOP_KEYS
    if extra:
        err(errors, f"{rel}: unexpected top-level keys {sorted(extra)}")
    eid = data.get("id")
    if eid is not None and not path.name.startswith(str(eid)):
        err(errors, f"{rel}: id {eid!r} does not match filename")
    slots = data.get("slots")
    if not isinstance(slots, dict) or not slots:
        err(errors, f"{rel}: slots must be a non-empty mapping")
        return
    for sname, slot in slots.items():
        where = f"{rel}: slots.{sname}"
        if not isinstance(slot, dict):
            err(errors, f"{where}: not a mapping")
            continue
        bad = set(slot) - ALLOWED_SLOT_FIELDS
        if bad:
            err(errors, f"{where}: unknown fields {sorted(bad)}")
        conf = slot.get("confidence")
        if slot.get("value") is not None:
            if conf not in CONFIDENCE_VALUES:
                err(errors, f"{where}: confidence is mandatory (reported|confirmed) when value is set")
        elif conf is not None and conf not in CONFIDENCE_VALUES:
            err(errors, f"{where}: confidence must be reported|confirmed or null")
        st = slot.get("source_type")
        if st is not None and st not in SOURCE_TYPE_VALUES:
            err(errors, f"{where}: source_type must be primary|secondary or null")
        dec = slot.get("decisive")
        if dec is not None and not isinstance(dec, bool):
            err(errors, f"{where}: decisive must be a bool")
        d = slot.get("date")
        if d is not None and not isinstance(d, date):
            err(errors, f"{where}: date must be an ISO date or null")


def check_thresholds_schema(path, data, errors):
    rel = path.relative_to(ROOT)
    if not isinstance(data, list):
        err(errors, f"{rel}: must be a list of thresholds")
        return
    for i, th in enumerate(data):
        where = f"{rel}[{i}]"
        if not isinstance(th, dict):
            err(errors, f"{where}: not a mapping")
            continue
        missing = THRESHOLD_KEYS - set(th)
        if missing:
            err(errors, f"{where}: missing keys {sorted(missing)}")
        extra = set(th) - THRESHOLD_KEYS
        if extra:
            err(errors, f"{where}: unexpected keys {sorted(extra)}")
        if "id" in th and not re.fullmatch(r"TH-\d{3}", str(th["id"])):
            err(errors, f"{where}: id must look like TH-NNN")
        if th.get("status") not in {"open", "resolved"}:
            err(errors, f"{where}: status must be open|resolved (HUMAN-set)")
        if not isinstance(th.get("due_passed"), bool):
            err(errors, f"{where}: due_passed must be a bool")
        due = th.get("due")
        if due is not None and not isinstance(due, date):
            err(errors, f"{where}: due must be an ISO date or null")


def check_pairing(inst, errors):
    board = inst / "board"
    if not board.is_dir():
        err(errors, f"{inst.relative_to(ROOT)}: no board/ directory")
        return
    mds = {p.stem for p in board.glob("*.md")}
    ymls = {p.stem for p in board.glob("*.yaml")}
    for stem in sorted(mds - ymls):
        err(errors, f"{board.relative_to(ROOT)}/{stem}.md has no matching .yaml")
    for stem in sorted(ymls - mds):
        err(errors, f"{board.relative_to(ROOT)}/{stem}.yaml has no matching .md")


# ---------------------------------------------------------------- purity

def check_purity(terms, warnings):
    scaffold = ROOT / "scaffold"
    if not scaffold.is_dir():
        return
    pats = []
    for t in terms:
        flags = 0 if (t.isupper() and len(t) <= 4) else re.IGNORECASE
        pats.append((t, re.compile(rf"\b{re.escape(t)}\b", flags)))
    for path in sorted(scaffold.rglob("*")):
        if not path.is_file():
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for term, pat in pats:
                if pat.search(line):
                    warnings.append(
                        f"scaffold purity: {path.relative_to(ROOT)}:{n} contains "
                        f"instance term {term!r} — a human judges whether it belongs"
                    )


# ---------------------------------------------------------------- boundary

def readonly_projection():
    """Everything a tool must never change, as one JSON-able structure."""
    proj = {"prose": {}, "entries": {}, "thresholds": {}}
    # Prose and structural files: full-content hashes (any change = human territory).
    for pattern in ("scaffold/**/*", "instances/*/archetypes.md", "instances/*/findings.md",
                    "instances/*/board/*.md", "README.md", "CLAUDE.md"):
        for path in sorted(ROOT.glob(pattern)):
            if path.is_file():
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                proj["prose"][str(path.relative_to(ROOT))] = digest
    # Entry YAML: all keys except writable slot fields; plus confidence (for
    # downgrade detection — writable, but confirmed->reported requires a human).
    for inst in instance_dirs():
        for path in sorted((inst / "board").glob("*.yaml")):
            data = load_yaml(path) or {}
            slots = data.get("slots") or {}
            proj["entries"][str(path.relative_to(ROOT))] = {
                "top": {k: str(v) for k, v in data.items() if k != "slots"},
                "slot_names": sorted(slots),
                "readonly": {
                    s: {f: str(sl.get(f)) for f in sorted(READONLY_SLOT_FIELDS)}
                    for s, sl in slots.items() if isinstance(sl, dict)
                },
                "confidence": {
                    s: sl.get("confidence") for s, sl in slots.items() if isinstance(sl, dict)
                },
            }
        tpath = inst / "thresholds.yaml"
        if tpath.is_file():
            data = load_yaml(tpath) or []
            proj["thresholds"][str(tpath.relative_to(ROOT))] = {
                str(th.get("id")): {k: str(v) for k, v in th.items() if k not in THRESHOLD_WRITABLE}
                for th in data if isinstance(th, dict)
            }
    return proj


def git_head_projection():
    """If a git repo contains ROOT (at ROOT or enclosing it), rebuild the
    projection from HEAD. Paths are prefixed so a board nested inside a
    larger repository (the installed layout) resolves correctly."""
    try:
        top = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return None
    prefix = ROOT.resolve().relative_to(Path(top).resolve()).as_posix()
    prefix = "" if prefix == "." else prefix + "/"
    # Minimal HEAD access without touching the working tree: read files via git show.
    proj_now = readonly_projection()
    proj_head = {"prose": {}, "entries": {}, "thresholds": {}}
    for section in proj_now:
        for rel in proj_now[section]:
            show = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{prefix}{rel}"],
                                  capture_output=True)
            if show.returncode != 0:
                continue  # new file; boundary check flags it below
            blob = show.stdout
            if section == "prose":
                proj_head["prose"][rel] = hashlib.sha256(blob).hexdigest()
            else:
                data = yaml.safe_load(blob.decode("utf-8"))
                if section == "entries":
                    slots = (data or {}).get("slots") or {}
                    proj_head["entries"][rel] = {
                        "top": {k: str(v) for k, v in (data or {}).items() if k != "slots"},
                        "slot_names": sorted(slots),
                        "readonly": {
                            s: {f: str(sl.get(f)) for f in sorted(READONLY_SLOT_FIELDS)}
                            for s, sl in slots.items() if isinstance(sl, dict)
                        },
                        "confidence": {
                            s: sl.get("confidence") for s, sl in slots.items()
                            if isinstance(sl, dict)
                        },
                    }
                else:
                    proj_head["thresholds"][rel] = {
                        str(th.get("id")): {k: str(v) for k, v in th.items()
                                            if k not in THRESHOLD_WRITABLE}
                        for th in (data or []) if isinstance(th, dict)
                    }
    return proj_head


def diff_projections(ref, cur, violations):
    for rel, digest in cur["prose"].items():
        if rel not in ref["prose"]:
            violations.append(f"boundary: new human-owned file since reference: {rel}")
        elif ref["prose"][rel] != digest:
            violations.append(f"boundary: human-owned file changed: {rel} (prose/scaffold is not tool-writable)")
    for rel in ref["prose"]:
        if rel not in cur["prose"]:
            violations.append(f"boundary: human-owned file removed: {rel}")
    for rel, cur_e in cur["entries"].items():
        ref_e = ref["entries"].get(rel)
        if ref_e is None:
            violations.append(f"boundary: new entry file since reference: {rel}")
            continue
        if cur_e["top"] != ref_e["top"]:
            violations.append(f"boundary: read-only top-level key changed in {rel} "
                              f"(id/player/archetype_ref are not tool-writable)")
        if cur_e["slot_names"] != ref_e["slot_names"]:
            violations.append(f"boundary: slot set changed in {rel} "
                              f"(adding/removing a slot is a human act)")
        for s, ro in cur_e["readonly"].items():
            if s in ref_e["readonly"] and ro != ref_e["readonly"][s]:
                violations.append(f"boundary: read-only field changed in {rel} slots.{s} "
                                  f"(decisive/notes are not tool-writable)")
        for s, conf in cur_e["confidence"].items():
            if ref_e["confidence"].get(s) == "confirmed" and conf == "reported":
                violations.append(f"boundary: confidence downgraded confirmed->reported in "
                                  f"{rel} slots.{s} (the reverse promotion requires a human)")
    for rel, cur_t in cur["thresholds"].items():
        ref_t = ref["thresholds"].get(rel)
        if ref_t is None:
            violations.append(f"boundary: new thresholds file since reference: {rel}")
            continue
        for tid, fields in cur_t.items():
            if tid in ref_t and fields != ref_t[tid]:
                violations.append(f"boundary: read-only threshold field changed: {rel} {tid} "
                                  f"(only due_passed is tool-writable; resolution is human)")
        for tid in set(cur_t) - set(ref_t):
            violations.append(f"boundary: new threshold {tid} in {rel} since reference (human act)")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check-boundary", action="store_true",
                    help="fail if any read-only key changed vs git HEAD / snapshot baseline")
    ap.add_argument("--snapshot", action="store_true",
                    help="record the current tree as the boundary baseline (human act)")
    ap.add_argument("--terms", type=Path, default=None,
                    help="file with one purity term per line (overrides default list)")
    args = ap.parse_args()

    if args.snapshot:
        BASELINE.write_text(json.dumps(readonly_projection(), indent=1, sort_keys=True),
                            encoding="utf-8")
        print(f"boundary baseline written: {BASELINE.relative_to(ROOT)}")
        return 0

    errors, warnings = [], []

    for inst in instance_dirs():
        check_pairing(inst, errors)
        for path in sorted((inst / "board").glob("*.yaml")):
            try:
                check_entry_schema(path, load_yaml(path), errors)
            except yaml.YAMLError as e:
                err(errors, f"{path.relative_to(ROOT)}: YAML parse error: {e}")
        tpath = inst / "thresholds.yaml"
        if tpath.is_file():
            check_thresholds_schema(tpath, load_yaml(tpath), errors)
        else:
            err(errors, f"{inst.relative_to(ROOT)}: missing thresholds.yaml")

    terms = DEFAULT_PURITY_TERMS
    if args.terms:
        terms = [t.strip() for t in args.terms.read_text(encoding="utf-8").splitlines() if t.strip()]
    check_purity(terms, warnings)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")

    rc = 1 if errors else 0

    if args.check_boundary:
        ref = git_head_projection()
        ref_name = "git HEAD"
        if ref is None:
            if not BASELINE.is_file():
                print("ERROR boundary: no git repo and no snapshot baseline; "
                      "run --snapshot first (human act)")
                return 2
            ref = json.loads(BASELINE.read_text(encoding="utf-8"))
            ref_name = str(BASELINE.name)
        violations = []
        diff_projections(ref, readonly_projection(), violations)
        if violations:
            for v in violations:
                print(f"FAIL  {v}")
            print(f"boundary check vs {ref_name}: FAILED ({len(violations)} violation(s))")
            return 2
        print(f"boundary check vs {ref_name}: ok")

    if rc == 0:
        print("validate: ok" + (f" ({len(warnings)} warning(s))" if warnings else ""))
    return rc


if __name__ == "__main__":
    sys.exit(main())
