#!/bin/sh
# BID2 motivation — Overleaf sync pre-commit check.
#
# The Overleaf project folder (overleaf_motivation/) holds SYMLINKS to the
# canonical section (draft/motivation_section.tex) and figures
# (output/figures/), so those cannot drift by construction. The shipped
# overleaf_motivation.zip is a build artifact and CAN drift — this hook closes
# that gap: whenever a commit touches either source, the zip is rebuilt and
# staged alongside it.
#
# The rebuild is deterministic, so a no-op rebuild produces no diff.
#
# This script is not installed into .git/hooks/ — it is called by the versioned
# dispatcher at .githooks/pre-commit, which is already listed there. Nothing to
# install per project; a fresh clone only needs the repo-wide switch:
#
#   git config core.hooksPath .githooks
#
# If this hook stops firing, check that first — core.hooksPath is local config
# and does not travel with a clone. See .githooks/README.md.
# Wired 2026-08-09.

MOT_REL="Missions/Funded/BID2/motivation"
TOP=$(git rev-parse --show-toplevel) || exit 0

git diff --cached --name-only \
  | grep -qE "^$MOT_REL/(draft/|output/figures/|overleaf_motivation/)" || exit 0

echo "[bid2-motivation] Overleaf sources staged - rebuilding overleaf_motivation.zip"
python3 "$TOP/$MOT_REL/scripts/build_overleaf_project.py" || {
    echo "[bid2-motivation] BLOCKED: could not rebuild the Overleaf project (see above)."
    exit 1
}
git add "$TOP/$MOT_REL/overleaf_motivation.zip" || exit 1
exit 0
