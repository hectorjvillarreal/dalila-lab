# CC INSTRUCTIONS — BID2 · Bibliography and citation audit

**Version:** v1 · **Date:** 2026-08-18 · **Mission:** BID2 (IADB Fiscal Division)
**Target file:** `Draft-August-v2.tex` and its bibliography database `references.bib`
**Edit mode:** diagnose first, repair second. Report before changing anything
that is not unambiguous.
**Scope:** citation keys, the `.bib` database, and the bibliography setup only.

Overleaf is reporting citation problems. This pass finds out what they are.

---

## 0. Why this is a diagnostic pass

The document has been through four editing passes in two days. Sections were
rewritten, a section was created by relocation, and citation keys were
deliberately dropped from the literature review. Any of those can produce
Overleaf citation warnings, and they need different fixes:

- a key cited in the text but absent from `references.bib` prints as `[?]` and
  raises **Citation undefined**;
- a key present in `references.bib` but no longer cited anywhere is **harmless**
  under `natbib` with `\bibliographystyle{apalike}` — it simply does not print,
  and it must **not** be deleted on that ground;
- a malformed `\citep[...][...]{}` call, a stray brace, or a key containing a
  character the style cannot handle produces a compile-time error rather than a
  warning;
- and a `.bib` entry missing a field the `apalike` style requires produces a
  warning that looks like a citation problem but is a database problem.

Do not guess which of these it is. Find out.

**Current setup, verified:** `\usepackage{natbib}` at line 34,
`\bibliographystyle{apalike}` at line 35, `\bibliography{references}` at line
1450. There are no `\bibitem` entries in the `.tex` — the database is external.
**36 distinct keys are cited** in the document.

---

## 1. Diagnosis — do this first and report before repairing

1. **Locate `references.bib`.** If it is not in the working directory, stop and
   report; nothing else in this file can proceed.
2. **Extract every cited key** from `Draft-August-v2.tex`, including keys inside
   grouped calls such as `\citep{A, B, C}` and calls carrying optional arguments
   such as `\citep[note;][]{Key}`. There should be 36.
3. **Extract every key defined** in `references.bib`.
4. **Report three lists:**
   - **cited but not defined** — these are the Overleaf errors, and the priority;
   - **defined but not cited** — informational only, no action;
   - **defined more than once** — duplicate keys, which silently shadow.
5. **Scan every citation call for malformation.** Report any with unbalanced
   braces, an empty key, a doubled comma, a leading or trailing space inside the
   braces, or an optional-argument form other than the valid `natbib` patterns
   `\citep[post]{key}` and `\citep[pre][post]{key}`.
6. **Check every `.bib` entry that `apalike` will format** for a missing `author`,
   `year`, or `title` field, and for unescaped special characters — `&`, `%`,
   `#`, and accented characters written as raw UTF-8 rather than in LaTeX escape
   form. Report what you find.
7. **Report the compile artefacts if present.** If `.aux`, `.bbl` or `.blg` files
   exist in the directory, read the `.blg` and report every warning and error it
   contains verbatim. This is usually the fastest route to the actual cause and
   should be done early.

**Stop here and report.** Do not repair before reporting the diagnosis, unless a
finding falls under §2.

---

## 2. Repairs permitted without further instruction

Only these. Everything else waits for review.

- **A malformed citation call** where the intended key is unambiguous — for
  example a stray space inside the braces, or a doubled comma in a grouped call.
  Fix it and report each fix verbatim, before and after.
- **A duplicate entry in `references.bib`** where the two copies are identical.
  Remove one and report.
- **An unescaped special character in a `.bib` field** where the correct escape
  is unambiguous. Fix and report.

---

## 3. Repairs that require reporting, not action

- **A cited key with no `.bib` entry.** Do **not** invent a bibliography entry.
  Do not guess at authors, titles, years, journals, or publishers from the key
  name. Report the key, every location where it is cited with line numbers, and
  the surrounding sentence so the missing source can be identified. A fabricated
  reference is worse than a broken one: a broken one is visible in the PDF and a
  fabricated one is not.
- **A `.bib` entry missing a required field.** Report the entry and the field.
  Do not fill it in from inference.
- **A key that looks like a near-duplicate of another** — for instance one in
  `AuthorYear` form and one in `author_year` form referring to the same work.
  The document contains at least one key in lower-case underscore form
  (`viscusi_masterman_2017`) against thirty-five in CamelCase. Report whether it
  resolves; do **not** rename it, since renaming requires editing every call site
  and the `.bib` together.

---

## 4. Constraints

1. **Never delete a `.bib` entry because it is uncited.** Uncited entries do not
   print and do not warn. Several keys were dropped from the literature review by
   design and their entries stay.
2. **Never add a `\cite` call to the document text.** This pass does not change
   what the paper cites.
3. **Never remove a `\cite` call to silence a warning.** A citation that cannot be
   resolved is a missing source, not a surplus citation.
4. Do not change `\bibliographystyle` or the `natbib` options.
5. Do not reformat `references.bib` — no reordering, no field reordering, no
   whitespace normalization. Targeted edits only, so the diff stays readable.
6. Do not compile. Report what you would expect the compiler to say.

---

## 5. Reporting

Report, in this order:

1. Whether `references.bib` was found, and how many entries it holds.
2. The contents of the `.blg` log if one exists, verbatim.
3. The three key lists from §1.4, in full.
4. Every malformed citation call found, with line numbers.
5. Every `.bib` entry with a missing required field or an unescaped character.
6. Every repair made under §2, verbatim before and after.
7. Every item requiring Héctor's decision under §3, with enough context —
   surrounding sentence and line number — to identify the intended source.

If the diagnosis turns out to be something not anticipated here, say so plainly
and describe it rather than forcing it into one of the categories above.
