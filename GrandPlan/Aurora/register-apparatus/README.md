# register-apparatus — Aurora corpus obligation scanner

Aurora project · apparatus tooling. Answers, in the minimal form the complexity
budget allows, the design question logged in the Mollick entry
(`202607_AURORA_AI_mollick_twilight-chatbots_v1.1`, "The design question this
raises"): the Core Team is a co-intelligence architecture, while valuable work
is migrating to agents with harnesses running against a repository. This is the
harness — scoped to the apparatus itself, not to research judgment.

## What it is

A **read-only lens over the Aurora register documents** (`AI/`, `briefing/`,
`geopol/`, `docs/corpus/`) and the cross-project design log
(`_crossrefs/design_log/`). One command scans every document's frontmatter and
body and extracts the open obligations the documents themselves declare, into a
single generated board:

| Board section | What it catches |
| --- | --- |
| Pending approval | `status: … pending approval` → `approving_authority` |
| Pending endorsements | empty `endorsed_by`; `section_endorsements` with a pending comment |
| Corroboration-pending claims | body lines flagged corroboration-pending (e.g. the GPT-5.6 cross-lab claim) |
| Dangling / pending cross-refs | `cross_refs` marked `[pending]` / `[thread]`, and doc-id refs that resolve to **no file on disk** |
| Version & location hygiene | superseded versions still co-located; the same file present in two trees |
| Unprocessed source files | non-`.md` sources (PDFs) no corpus entry references |
| Live review / monitoring triggers | bullets under any *Review triggers* / *Monitoring triggers* heading (DP-001 T1–T5, watch-item §8) |
| Actions generated | bullets under *Actions generated* headings |
| Estimate-decay register | documents tagged `estimate_decay` (standing decay warning, Mollick v1.1) |

Superseded versions and duplicate copies are processed once — they contribute
hygiene rows only, never duplicate obligations.

## Files

| File | Role |
| --- | --- |
| `apparatus.py` | The scanner. Stdlib only — no installs. Never writes outside this folder. |
| `board.md` | Generated obligation board. Disposable — re-rendered from the corpus. |
| `run_log.md` | Appended one row per scan: date, doc count, open-item count, breakdown. The count time series is the apparatus health metric. |

## Cycle

```bash
python3 apparatus.py scan      # rebuild board.md, append run_log.md
python3 apparatus.py status    # same content in the terminal
```

A **maintenance run** (a Claude Code session against this folder) is:

1. `scan` — refresh the board.
2. Work the board top-down, in the corpus documents themselves:
   - triggers: web-check each live trigger; if one fired, revise the owning
     document (new version, per its own revision conventions);
   - corroboration-pending: search for corroboration/refutation; record the
     outcome in the owning document, never here;
   - unprocessed sources: draft the missing entry (e.g. the open-weights
     letter PDF) as a normal register document, pending approval;
   - hygiene: archive superseded versions / resolve duplicate locations —
     **only with Héctor's approval**, since filing conventions are his call.
     Archive convention (approved 2026-07-24): each register directory keeps
     an `_archive/` subfolder; superseded versions and retired duplicate
     copies are `git mv`'d there **unmodified** (the move itself is the
     record; git history preserves provenance; nothing is ever deleted).
     The scanner skips `_archive/` — archived documents leave the active
     register and the board.
3. `scan` again — the run's deliverable is the delta in `run_log.md`.

## Disciplines (mirroring `spcx_monitor`)

- **The corpus documents are the single source of truth.** The tool holds no
  state; there is nothing to edit here. Fix things in the documents, re-scan.
- **No fabricated judgment.** The board lists what documents declare. Whether
  a trigger fired, a claim is corroborated, or an entry deserves endorsement
  is an analyst/agent/persona action recorded in the documents under their own
  authorship discipline (PROTO-RAG-001).
- **No new artifact types.** Outputs of a maintenance run are ordinary
  register documents / corpus entries under existing conventions; the board
  and run log are generated views, not corpus artifacts.
- **Approval boundary.** `status: pending approval` and `endorsed_by` fields
  are never touched by a maintenance run. Endorsement and approval are human /
  domain-authority actions.

## Relation to DP-001 / DP-002

Consistent with DP-001 (severability): the scanner is local and stdlib-only —
the apparatus board survives with external API access cut. The *maintenance
run* uses a frontier agent, which is the stock/flow pattern proposed in
`20260715_AURORA_BRIEFING_frontier-agents-dalila_v1.0`: the frontier agent
builds and maintains artifacts that persist locally; nothing here requires the
agent to operate.

## Not in v0.1 (deliberately)

- No systemd timer. A scan without an agent to work the board adds a log row
  and nothing else; automation waits until the maintenance cycle has run
  manually a few times and proves worth scheduling.
- No auto-drafting, no auto-archiving, no endorsement automation.
- No web-checking inside `apparatus.py` — trigger checking needs judgment and
  belongs to the maintenance run.

## Note on git

Same as `spcx_monitor`: commit to an Aurora-appropriate branch, not whatever
calibration branch happens to be checked out.
