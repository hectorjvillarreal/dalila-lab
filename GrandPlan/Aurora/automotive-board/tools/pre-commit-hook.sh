#!/bin/sh
# automotive-board pre-commit hook (build doc §7; wired post-acceptance 2026-07-24).
#
# Fires only when staged changes touch GrandPlan/Aurora/automotive-board/.
# Always enforces schema / pairing / scaffold-purity (validate.py).
# Enforces the automation boundary vs git HEAD (--check-boundary) unless
# AUTOBOARD_HUMAN=1 is set: human acts (prose edits, new slots, new
# thresholds, scaffold changes) are legitimate but must be explicit —
#   AUTOBOARD_HUMAN=1 git commit -m "prose(NNN): ..."
# Tool sessions never set the variable, so a tool can only commit
# writable-field changes. Install (from repo root):
#   cp GrandPlan/Aurora/automotive-board/tools/pre-commit-hook.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit

BOARD_REL="GrandPlan/Aurora/automotive-board"
TOP=$(git rev-parse --show-toplevel) || exit 0
BOARD="$TOP/$BOARD_REL"

git diff --cached --name-only | grep -q "^$BOARD_REL/" || exit 0

echo "[automotive-board] staged changes detected — running validate.py"
python3 "$BOARD/tools/validate.py" || {
    echo "[automotive-board] BLOCKED: schema/pairing/purity failure (see above)."
    exit 1
}

if [ "$AUTOBOARD_HUMAN" = "1" ]; then
    echo "[automotive-board] AUTOBOARD_HUMAN=1 — boundary check waived (human act)."
    exit 0
fi

python3 "$BOARD/tools/validate.py" --check-boundary || {
    echo "[automotive-board] BLOCKED: automation-boundary violation vs HEAD."
    echo "  If this is a deliberate human act (prose, new slot, new threshold,"
    echo "  scaffold), re-run:  AUTOBOARD_HUMAN=1 git commit ..."
    exit 1
}
exit 0
