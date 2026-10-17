---
doc_id: 20261017_AURORA_BRIEF_threshold-registration-stop_v1.0
title: "Stop report — threshold registration: the task contradicts itself on the claim field"
project: Aurora / automotive board
type: session_brief
version: 1.0
date: 2026-10-17
prepared_by: Claude Code session (task: 20261017_AURORA_TASK_threshold-registration_v1.0)
for: Elle
refers_to:
  - 20261017_AURORA_TASK_threshold-registration_v1.0
---

# Stop report — threshold registration

**Nothing was written.** `tools/validate.py` and `instances/automotive/thresholds.yaml` are
unchanged. No fixtures were created, nothing was committed, and `AUTOBOARD_HUMAN` was never
set. `python3 tools/validate.py` still prints `validate: ok`.

I stopped under the task's own §0: *"If any step appears to require a judgment, a value not
written here, or a file not named here — stop and report."* Satisfying both §2 and §3 needs
one of each.

## 1. The contradiction — `claim` vs `description`

| Where | What it says |
|---|---|
| §2 | `claim` is required on **every** threshold |
| Current `thresholds.yaml` (TH-001 to TH-004) | stores the text in **`description`**; there is no `claim` field |
| §3a | add `date_confidence` and `owner` to those four — *"Do not change any other field"* |
| §3c (TH-005 to TH-009) | uses **`claim`** and has no `description` |
| `tools/validate.py:45`, the current field list | requires `description` and rejects any field it does not list |

There are three ways to reconcile these, and each one breaks the task somewhere:

1. **Rename `description` to `claim` on TH-001 to TH-004.** This breaks §3a.
2. **Have the validator accept either name.** This is a rule nobody wrote, and the register
   ends up with two names for the same field.
3. **Apply the task exactly as written.** The validator fails on TH-001 to TH-004 for a
   missing `claim`. §4 says that failure is also a stop.

## 2. Two related gaps

**`tools/thresholds.py` reads `th['description']` directly**, in lines 74, 84 and 89.
- That tool is the board's due-date reporter. It is also the only tool that sets
  `due_passed`.
- On any row without `description` it raises `KeyError`, and the crash happens at the moment
  that row comes due.
- It is not a crash today: none of TH-005 to TH-009 falls inside the 30-day window. TH-007
  (due 2026-12-31) enters that window on 2026-12-01, and the report would crash from then
  on, exactly when it is needed.
- The task allows changes to exactly two files, and this is not one of them.

**`date_source` and `note` are not in §2's field list.**
- §3c writes both into every new row.
- The validator rejects fields it doesn't know about, so it has to be told about these two.
- That change is mechanical. What the task doesn't say is whether they are **optional** or
  **required**. Today `description` is required, but the four existing rows have neither
  `date_source` nor `note`. Making them required would therefore mean adding values to
  TH-001 to TH-004 that nobody has written.

## 3. Decisions needed

1. **One name for the field:** `claim` or `description`.
2. **If `claim`:** your authorisation to rename it on TH-001 to TH-004. The wording stays
   as it is.
3. **Scope:** add `tools/thresholds.py` to the allowed files, so it reads whichever name you
   choose.
4. **`date_source` and `note`:** optional (my reading of §3c) or required.

With those four answers the rest of the task is mechanical, and I can rerun it
unchanged:
- the validator edit and its four fixtures;
- the back-fill of the four existing rows;
- TH-002's `due`;
- the five new rows, written as the human-routed act the task specifies.

## 4. Things that are not problems

- **TH-007 on entry `008`.** The entry is not written yet. The validator does not check
  whether a threshold's entry exists, so this passes. The task says the order is
  deliberate.
- **Human routing.** `AUTOBOARD_HUMAN=1` works the way the task describes:
  `tools/pre-commit-hook.sh` skips only the boundary check and still runs schema validation.
  It matters only at commit time, and the task does not authorise a commit.

## 5. Fence report

- **Read:**
  - `CLAUDE.md` (session load)
  - the task file
  - `instances/automotive/thresholds.yaml`
  - `tools/validate.py`
  - `tools/pre-commit-hook.sh`
  - `tools/thresholds.py`, lines 40–92
  - `tools/fixtures/README.md`
  - a listing of `tools/` and `tools/fixtures/`
  - a listing of `_build/`
- **Searched (grep):**
  - `AUTOBOARD_HUMAN` across `tools/`, `scaffold/`, `_build/` and the root `.md` files
  - field names across `tools/*.py`, `tools/fixtures/` and `instances/`
- **Executed:** `python3 tools/validate.py`, which printed `validate: ok`.
- **Written:** this report only.
- **Outside the tree:** nothing.
