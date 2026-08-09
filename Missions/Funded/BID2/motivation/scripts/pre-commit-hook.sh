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
# Install (from repo root) — note the repo already carries an automotive-board
# pre-commit hook, so DISPATCH to this script rather than overwriting it:
#
#   MOT="Missions/Funded/BID2/motivation/scripts/pre-commit-hook.sh"
#   # add near the TOP of .git/hooks/pre-commit, before the board block:
#   #   H="$(git rev-parse --show-toplevel)/$MOT"
#   #   [ -x "$H" ] && { "$H" || exit 1; }
#
# Re-running the automotive-board install line
#   cp GrandPlan/Aurora/automotive-board/tools/pre-commit-hook.sh .git/hooks/pre-commit
# will REMOVE that dispatch. If it goes missing, re-add the two lines above.
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
