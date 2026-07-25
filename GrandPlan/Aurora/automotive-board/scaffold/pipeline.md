# Pipeline — invariant

The board is maintained by three jobs plus a validator. Cadence: on demand plus a
periodic sweep — never real-time, no scheduler, no services.

```
feed inbox ──(dedupe: absorbed ledger)──► human reads ──► promotion (human call)
                                                          │
                                                          ▼
                                        slot writes (tool, writable fields only)
                                                          │
                                                          ▼
                              thresholds report · decisive-slot flags (tool, mechanical)
                                                          │
                                                          ▼
                                        adjudication of meaning (human, prose)
```

## Job 1 — feed maintenance

Feed items are **one line**: date · one-clause "why this might matter" · URL. No schema
beyond that — the feed is deliberately looser than any corpus protocol and carries no
corpus frontmatter.

**Dedupe is a first-class requirement.** `feed/absorbed.yaml` is the ledger; each record
carries the raw URL, a normalised form, the absorption date, entries touched, and
whether scaffold/instance findings were touched. URLs are normalised before comparison
(strip scheme, `www.`, tracking parameters, trailing slashes). On a match, the tool
reports *already absorbed <date>, touched <entries>* and stops.

The tool **may** flag that an item's text matches a watch-item string. It **may not**
decide the item changes anything. Promotion is a human call; promoted write-ups live in
`feed/promoted/`.

## Job 2 — slot maintenance

Update factual slots from feed items and sources — writable fields only, inside
`slots.*`. **One slot write = one commit.** Network fetching sits behind an explicit
`--fetch` flag, off by default; absent the flag the tool makes no network calls.

## Job 3 — thresholds and bet-status

- Thresholds: list entries whose `due` has passed while `status: open`; list those due
  within 30 days. `due_passed` is the only tool-writable threshold field. `status:
  resolved` and `resolution` are human. **The tool never resolves a threshold.**
- Bet-status: per entry, report slots marked `decisive: true` whose `value` or `date`
  changed since a reference state. **Output is a flag — player, slot, movement, date,
  "review". Never a verdict.** The tool detects movement; a human adjudicates meaning.
  Any output resembling "bet under stress" / "bet failing" is a defect.

## Validator

- Schema conformance for all entry YAML and the thresholds file.
- Pairing: every prose `.md` has a facts `.yaml`, and vice versa.
- **Boundary check**: diff the working tree against a reference (git HEAD, or a snapshot
  baseline where git is not yet wired) and **fail** if any read-only key changed — the
  automation boundary enforced mechanically rather than trusted. Wire as a pre-commit
  hook.
- Scaffold purity: warn on instance-specific vocabulary appearing under `scaffold/`
  (configurable term list). Warning, not error; a human judges.

## Provenance

Git history is the provenance chain — one commit per logical change, prefixed
`slot(NNN):` · `feed:` · `threshold(TH-NNN):` · `prose(NNN):` (human commits only) ·
`scaffold:` · `tool:`. No database at this scale; history is what makes tool auto-write
safe: auditable and revertible. Local repo until the owner wires a remote.
