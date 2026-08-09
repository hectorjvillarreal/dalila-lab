#!/usr/bin/env python3
"""Rebuild overleaf_motivation.zip from the canonical sources.

The Overleaf project folder holds symlinks, not copies: the section lives at
draft/motivation_section.tex and the figures at output/figures/. This script
dereferences those symlinks into a flat zip that Overleaf's "Upload Project"
accepts, so the shipped zip can never disagree with the canonical files.

The zip is written deterministically (fixed member timestamps, sorted order),
so rebuilding without a content change produces byte-identical output and no
spurious git diff.

Usage:
    python3 scripts/build_overleaf_project.py          # rebuild if stale
    python3 scripts/build_overleaf_project.py --check  # exit 1 if stale, write nothing

Exit codes: 0 ok / in sync, 1 stale (--check) or a source is missing.
"""

import argparse
import hashlib
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / "overleaf_motivation"
ZIP = ROOT / "overleaf_motivation.zip"

# Fixed timestamp for every member, so the zip is a pure function of content.
FIXED_TIME = (2026, 8, 9, 0, 0, 0)


def sources():
    """Files that make up the project, in a stable order."""
    if not PROJECT.is_dir():
        sys.exit(f"ERROR: project folder not found: {PROJECT}")
    return sorted(p for p in PROJECT.iterdir() if p.is_file())


def build_bytes(files):
    """Serialize the project to zip bytes, following symlinks."""
    import io

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            info = zipfile.ZipInfo(p.name, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes())  # read_bytes follows the symlink
    return buf.getvalue()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="report staleness without writing")
    args = ap.parse_args()

    files = sources()

    broken = [p for p in PROJECT.iterdir() if p.is_symlink() and not p.exists()]
    if broken:
        for p in broken:
            print(f"ERROR: broken symlink {p.name} -> {p.readlink()}", file=sys.stderr)
        return 1

    required = {"main.tex", "motivation_section.tex"}
    missing = required - {p.name for p in files}
    if missing:
        print(f"ERROR: missing required file(s): {', '.join(sorted(missing))}",
              file=sys.stderr)
        return 1

    figures = [p.name for p in files if p.suffix == ".pdf"]
    if len(figures) != 4:
        print(f"ERROR: expected 4 figure PDFs, found {len(figures)}: {figures}",
              file=sys.stderr)
        return 1

    new = build_bytes(files)
    old = ZIP.read_bytes() if ZIP.exists() else b""

    if new == old:
        print(f"overleaf_motivation.zip is in sync ({len(files)} files)")
        return 0

    if args.check:
        print("overleaf_motivation.zip is STALE — run "
              "scripts/build_overleaf_project.py", file=sys.stderr)
        return 1

    ZIP.write_bytes(new)
    digest = hashlib.sha256(new).hexdigest()[:12]
    print(f"rebuilt overleaf_motivation.zip "
          f"({len(files)} files, {len(new):,} bytes, sha256:{digest})")
    for p in files:
        via = f" -> {p.readlink()}" if p.is_symlink() else ""
        print(f"  {p.name}{via}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
