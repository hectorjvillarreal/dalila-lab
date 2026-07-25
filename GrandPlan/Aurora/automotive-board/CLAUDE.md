# CLAUDE.md — session fence

**Place this file in the build working directory before starting the session. Do not edit it.**

---

## What this directory is

A build workspace for tooling that maintains the **automotive** player board — the motor vehicle industry: BYD, Geely, Toyota, Volkswagen, Tesla, Hyundai.

**"Auto" here has never meant *automated*.** On 2026-07-24 a session read it that way, built a register obligation scanner instead, and continued into corpus maintenance it had no mandate for. The word is retired. If you meet it in an older document, stop and ask rather than infer.

Authoritative task document: `20260724_AURORA_BUILD_automotive-board-tooling_v1.1.md`.

---

## Fence — absolute

You operate **inside this directory only.**

**May:** read the source documents placed here; create and edit files within this tree; run local git (no remote).

**May not:** read, list, index, modify, move, rename, archive, or commit anything outside this tree — in particular anything under a corpus, register, `_crossrefs/`, `design_log/`, or another project directory. Do not `cd` above this directory. Do not `find` or `grep` above it. Do not add a git remote. Do not push.

Installation into the wider tree happens **after acceptance, by Héctor.** Not by you.

---

## Scope arrest

Stop immediately and report — do not proceed, do not improvise, do not do it "just to be helpful" — if a task appears to require:

- reading or writing outside this tree;
- touching an approval, endorsement, version, or status field in any document;
- moving, archiving, or renaming existing files;
- resolving, ratifying, or bumping anything;
- creating documents that look like corpus entries;
- anything involving the register scanner at `auto-apparatus/`.

**A report costs a message. Proceeding costs a governance incident.**

---

## The one rule of the thing you are building

> **Facts are mechanical → automate. Classification is judgment → never automate.**

You are building maintenance infrastructure for an analytical instrument **you must not operate.** Do not assign archetypes, compute loadings, score or rank players, or declare any bet alive or dead. These are empirical constraints, not stylistic ones — see §0.4 of the task document.

---

## Deliverable check

Report every path you read or wrote. Nothing outside this tree except the named sources. That report is the first acceptance criterion.
