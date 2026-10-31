# Silver reference set: MX-SSRD Phase 0

**Status: silver, not gold.** This set becomes gold only after Beth (pension classification) and Héctor review it.

- Coded by Claude Code reading the documents directly, before any Qwen run. Never fed to Qwen, with one exception the build instruction orders: the first episode of `04.json` is the Stage 2 format anchor, so document 04 is out of the accuracy metrics.
- `_sparse/` holds the hand-coded records. `src/silver_expand.py` expands them into the full `NN.json` files and refuses any quote that is not verbatim.
- A filled field with no quote is listed in `fields_inferred`.
- `core: true` marks the main measures; recall is reported on both all episodes and core episodes.

**Coverage limits.** Documents 03, 05 to 11 were read in full. The three long laws were coded by subagents that read the transitorios, financing chapters and the articles of each coded episode, not every article:

| Doc | Not read |
|---|---|
| 01 | arts. 14-24, 26-27, 29-69, 73-104, 109-111, 124-140, 216-217, 222-239, 246-261, 263-277, 287 to the transitorios |
| 02 | arts. 28-36, 49-56, 59-73, 84-110, most of Artículo Tercero, part of art. 48 |
| 04 | arts. 55-73, 119-138, 157-231, 238-251, most health articles |

An episode living only in unread articles would be missing here and would look like a false positive for Qwen.

Document 08 publishes five tables as images, including the employer contribution schedule to 2030. They are not in the text, so neither the silver set nor Qwen sees them.
