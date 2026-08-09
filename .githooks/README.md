# Versioned git hooks

`git config core.hooksPath .githooks` points git at this folder instead of
`.git/hooks/`, so hook logic lives in the repository: versioned, reviewable in a
diff, and impossible for one project's install step to overwrite another's.

**Set it once per clone.** `core.hooksPath` is local config and does not travel
with a clone or a pull. If hooks stop firing on a machine, check this first:

    git config core.hooksPath          # should print .githooks

## What runs

`pre-commit` is a dispatcher. It calls each hook listed in its `HOOKS` variable,
in order, and blocks the commit if any exits non-zero. Currently:

| Hook | Fires when | Does |
|---|---|---|
| `GrandPlan/Aurora/automotive-board/tools/pre-commit-hook.sh` | staged changes touch `automotive-board/` | schema / pairing / scaffold-purity validation, plus the automation-boundary check unless `AUTOBOARD_HUMAN=1` |
| `Missions/Funded/BID2/motivation/scripts/pre-commit-hook.sh` | staged changes touch the motivation `draft/`, `output/figures/` or `overleaf_motivation/` | rebuilds and stages `overleaf_motivation.zip` from its symlink targets |

Each script is self-contained and lives beside the code it guards. To add one,
append its repo-relative path to `HOOKS` in `pre-commit`.

## Why this replaced the hand-edited hook

`.git/hooks/pre-commit` previously held the automotive-board hook inline, whose
documented install line is

    cp GrandPlan/Aurora/automotive-board/tools/pre-commit-hook.sh .git/hooks/pre-commit

That overwrites the whole file, so anything else added to it — the BID2 Overleaf
sync dispatch, for one — disappeared silently the next time the board hook was
reinstalled. A dispatcher in the repo has no such failure mode: re-running the
board's install line now writes to a file git ignores, and the board hook keeps
running because this dispatcher calls its source directly.

The old `.git/hooks/pre-commit` is left in place as a fallback. While
`core.hooksPath` is set, git ignores it and this folder is authoritative.
