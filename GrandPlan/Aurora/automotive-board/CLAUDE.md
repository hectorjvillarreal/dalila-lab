# CLAUDE.md — session fence

**Lives at the root of `automotive-board/`. Loaded by every session in this tree. Do not edit it.**

---

## What this directory is

The **automotive player board** — an analytical instrument tracking the motor vehicle industry (BYD, Geely, Toyota, Volkswagen, Tesla, Hyundai, and successors) — together with the tooling that maintains its factual layer.

Installed 2026-07-24. This is a **live artifact**, not a build workspace.

**"Auto" here has never meant *automated*.** On 2026-07-24 a session read it that way, built a register obligation scanner instead, and continued into corpus maintenance it had no mandate for. The word is retired from this project. If you meet it in an older document, stop and ask rather than infer. The register scanner is a different thing, owned by others, and lives at `auto-apparatus/`.

**Your task document is named in the session prompt.** Build instructions are filed in `_build/`; check the `supersedes:` frontmatter before assuming which is current. Pre-migration originals are frozen in `_archive/` — read-only, never a target.

---

## Fence — absolute

You operate **inside this directory only.**

**May:** read anything in this tree; write only what the session's task document authorises; run local git.

**May not:** read, list, index, modify, move, rename, archive, or commit anything outside this tree — in particular anything under a corpus, register, `_crossrefs/`, `design_log/`, or another project directory. Do not `cd` above this directory. Do not `find` or `grep` above it. Do not add a git remote. Do not push.

Changes are **accepted by Héctor**, not self-installed.

---

## The one rule

> **Facts are mechanical → automate. Classification is judgment → never automate.**

You maintain the factual layer of an instrument **you must not operate.** The boundary is structural: judgment lives in `.md` files, facts live in `.yaml` files, and the format gives you nowhere to write across the line.

**Human-owned — never write, even if a task document seems to ask:**

- every `.md` file under `instances/*/board/` (entry prose)
- `archetypes.md`, `findings.md`, `scaffold/discipline.md`
- inside any entry `.yaml`: `archetype_ref`, `decisive`, `notes`, `id`, `player`
- in `thresholds.yaml`: `status`, `resolution`
- anything in `_archive/`

**Writable, per the session's task document:** `value`, `unit`, `delta`, `date`, `source`, `source_type`, `confidence` inside `slots.*` · the feed inbox and `absorbed.yaml` · `due_passed` in `thresholds.yaml` · files under `tools/`.

Do not assign or normalise archetypes, compute or suggest loadings, score or rank players, or declare a bet alive, dead, stressed, or strengthening. **Detecting a broken reference is permitted; repairing one is not** — report and stop. Retired archetype slugs are never reused.

These are empirical constraints, not stylistic ones: the archetype poles are under active revision and have split twice under contact with data. A basis whose elements are still splitting cannot be computed against.

---

## Scope arrest

Stop immediately and report — do not proceed, do not improvise, do not do it "just to be helpful" — if a task appears to require:

- reading or writing outside this tree;
- editing any human-owned file listed above;
- touching an approval, endorsement, version, or status field in any document;
- moving, archiving, or renaming existing files;
- resolving, ratifying, or bumping anything;
- creating documents that look like corpus entries;
- anything involving the register scanner at `auto-apparatus/`.

**A report costs a message. Proceeding costs a governance incident.**

---

## Deliverable check

Report every path you read or wrote. That report is the first acceptance criterion of every session in this tree.
