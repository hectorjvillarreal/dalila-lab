# Feed inbox

One item per line: `YYYY-MM-DD · why this might matter (one clause) · URL`

No schema beyond that. Deliberately looser than the wider corpus protocol; explicitly
**outside PROTO-RAG-001 scope** — no frontmatter, ever. Before adding an item, run
`python3 tools/feed.py check <url>` — if it is already in `absorbed.yaml` the tool will
say so and you stop. Promotion of an item into an entry or the findings file is a human
call; promoted write-ups go to `promoted/`.

---

(no open items)
