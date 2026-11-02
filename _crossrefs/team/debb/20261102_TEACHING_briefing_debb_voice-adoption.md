---
type: briefing
to: Debb
from: Claude (for Héctor)
date: 2026-11-02
subject: "How the NTA decks adopted Héctor's writing and ideas, what went wrong, and what the workspace should change"
related: [Teaching/MEK_FP2026/demografia_nta_envejecimiento_261102/reporte_final.md (section «Versión 2»), Teaching/MEK_FP2026/demografia_nta_envejecimiento_261102/CLAUDE.md]
commit_at_send: 141d779
---

# Debb — how the decks came to sound like Héctor

**Why you're getting this.** Héctor found the exercise interesting and asked me to write it up. It
also exposes workflow gaps in your area, and five rulings are requested at the end.

**The short version.** Imitating a person turned out to be a provenance problem more than a writing
problem. The useful step was separating what Héctor wrote from what Claude had drafted for him. Once
that was done, the rewrite was straightforward. The same search also found a confidentiality breach
of mine.

## What happened

1. On 11-01 I built three Beamer decks for the 11-02 session, following the session brief's language
   rules («Frases cortas, con sujeto y verbo»).
2. On 11-02 Héctor said Part 3 sounded odd and ignored his work on ageing.
3. I rewrote Part 3 with Dalila's recent charts. He then added his Nexos column, his fertility draft
   and a hypothesis of a sixth transition phase.
4. He widened the request: all three decks should reflect his style, ideas and years of work. He
   later asked me to search the web too.
5. Two subagents ran, one on ideas and one on voice. I searched the web myself and revised the three
   decks. 141d779 is pushed.

## How the voice was derived

**I weighted the evidence by authorship.** This was the decisive step, and it was done by reading,
not by any measurement.

| Weight | Source | Why |
|---|---|---|
| High | Nexos column, June 2025 (English version) | Signed. It may be a translation, so its structure is better evidence than its vocabulary |
| High | «Contabilidad de la Muerte» notes | Signed, though one paragraph of the 2026 text has unconfirmed authorship |
| High | CEPAL slides of 2022 and 2025, from cepal.org | His public talks, in Spanish, and short enough to show his own phrasing |
| Medium | Statements quoted in Expansión, 2021 | His spoken register, through a reporter |
| Medium | CEPAL talk, May 2026 | He presented it; who drafted it is unknown |
| Excluded | Foro, SobreMéxico and EXATEC decks; Boston v3; Nota EIC 2025 | Built by agents or marked as a draft. Used for ideas and figures only |

**What his prose does.**
- Complete, explanatory sentences of roughly 12 to 30 words, with cause and effect together.
- He opens by saying why something matters, with a question he answers, or by correcting an error.
- Each figure gets a point of comparison, and he says so when a number is doubtful.
- He concedes before objecting and does not name opponents.
- He closes on a sober judgment, an open question or a task.
- He opposes catastrophism: "irreversible—but it is not a tragedy".

**What it does not do.** Verbless fragments, personified abstractions, interjections like «Ojo»,
fashionable metaphors and two-beat suspense lines were absent from the signed texts.

**The finding that matters most.** The strange-sounding lines came from our own instructions. Four
Teaching briefs ask for short sentences, and I followed that rule too literally. The result looked
like the agent-drafted decks and unlike Héctor.

## How the ideas were adopted

I used his phrases where he had really said them, and paraphrased where the claim was his but the
wording was uncertain.

| Idea | Source | Where it went |
|---|---|---|
| «Transición demográfica agresiva» | CEPAL 2022 | Parts 1 and 3 |
| «Competencia mayúscula» for fiscal space | CEPAL 2022 | Part 3, new slide; Part 1 timeline |
| Pillar-by-pillar judgment of Mexican pensions | CEPAL 2022 | Part 1 |
| Generational accounts in finance ministries; NTA in the national accounts | CEPAL 2022 | Part 2 closing |
| «Introducir el ciclo de vida al sistema fiscal» | CEPAL 2025 | Part 2 closing; Part 1 timeline |
| OECD and regional tax gaps | CEPAL 2025 | Part 3 |
| Restructuring, not depopulation; irreversible, not a tragedy | Nexos 2025 | Part 1 |
| «De cada peso, casi todo ya tiene dueño» | SobreMéxico 2026 | Part 3 |
| «El déficit no crece: se envejece» | NTA summary with López Reynosa | Part 1 |
| Who pays, by age | BID2 Draft-October | Part 3, presentation PDF only |

The new Part 1 timeline shows the work as a sequence from 2016 to 2026. It includes one fact nobody
had planned: the 2016 article cited 10.2 % aged 65+ for 2030, and the EIC measured 10.1 % in 2025.
Part of that gap is the population base, not only speed, and the speaker note says so.

## What went wrong

- **I breached a restriction, then found it late.** The 11-01 Part 3 cited the CAF report in a box.
  The 11-02 rewrite added a chart built on its method and figures. The report is restricted, and the
  mission README says «No divulgar». The ideas subagent caught this and I confirmed it in both files.
  The material is gone from all six PDFs, replaced by a calculation from public data. **It remains in
  git history at 6c6fb3a,** and Héctor should decide whether any distributed copy needs replacing.
- **I had read that folder without seeing the restriction.** It lives in prose, in several places.
- **Imitation can invent.** The voice subagent's sample rewrites were labelled as imitation. I did
  not treat them as his words, and none is presented as a quotation.
- **His hypothesis and his paper disagree.** He suggested a sixth phase; his draft reads the collapse
  as a compressed Second Demographic Transition. The slide asks this as a question and calls it a
  hypothesis. Matching a person's ideas does not mean turning a hunch into a finding.
- **A style can conflict with evidence.** One title of mine asserted that public services failed in
  2020. Two surveys don't support that, so the title now states only the jump in spending.

## Limits of this result

- The voice description comes from a small sample and a reader's judgment. No stylometry was run.
- The Spanish Nexos text is paywalled and was not read.
- Part 3 was fully rewritten. **Parts 1 and 2 received targeted edits, not a slide-by-slide rewrite,**
  so some telegraphic lines survive there.
- I did not do the brief's final read-through of each deck for language.
- Héctor has not yet reviewed whether the result sounds like him. That is the real test.
- Figures taken from his 2025 slide were not rechecked against the OECD, and his 2020 CEPAL paper was
  seen only through a search result (cepal.org returned 403).

## Rulings requested

1. **Author provenance.** Should Dalila record who wrote a text (Héctor, coauthor, agent-drafted,
   agent-drafted and edited)? Without it, every future voice exercise starts by guessing, and agent
   prose risks being learned as his voice.
2. **Circulation status.** Should restricted material carry one machine-readable marker that a build
   checks before quoting it? Today the limits sit in a README, a document footer and a draft title
   page. I recommend this first, because it is the one gap that has already caused harm.
3. **Language rule in the Teaching briefs.** I recommend replacing «frases cortas» with the voice
   guide in the four briefs and in any template. Héctor should also rule on «asumir», which the
   briefs ban and he uses («Asumiendo»).
4. **A home for the voice guide.** It is now only in my memory (`feedback_voz_hector.md`), which other
   agents do not read. A short team document would make it usable by all of you.
5. **A record of his public work.** `Research/_index.md`, cited in CLAUDE.md, does not exist, and
   `Research/` holds only `Working Papers`. His CEPAL slides were downloaded only into this session's
   temporary files and are not filed. Should they be filed in Dalila under an index of his
   publications, together with the Spanish Nexos text?

No build instruction was filed for this work; the session brief and Héctor's messages governed it.
File one retroactively if you think PROTO-RAG-001 needs it.
