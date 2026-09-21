# Session 25 Handoff
**Date:** 2026-09-21
**Status:** Ready to continue

---

## What Was Done

A two-task cleanup session. First, CLAUDE.md was identified as overdue for a structural overhaul — the Workspace Structure was a single flat mega-table with unreadable arc summaries buried in table cells, the session handoff reference was hardcoded to session 23, Arc C's structure doc was not marked superseded despite its quest journal being complete, and three standing rules established in session 24 had never been written into CLAUDE.md. Second, CLAUDE.md was rewritten from scratch (without reading the old file — the main session provided a full content specification to a subagent) producing a cleaner, better-organized document that preserves all prior guidance while fixing every identified issue.

---

## Changes Made

### Files Modified

| File | What changed |
|------|-------------|
| `CLAUDE.md` | Full rewrite — see Key Decisions for the complete change list |

---

## Key Decisions

### CLAUDE.md rewritten from scratch using a content specification
**Decision:** Rather than editing the existing file, the main session read the current CLAUDE.md and both handoffs, compiled a full content specification capturing everything that needed to be in the new file, and handed that specification to a subagent that wrote the file without reading the original.
**Reasoning:** The old file had accumulated structural debt across 24 sessions. A full rewrite from a clean spec produces a more coherent document than incremental edits.
> "rewrite it from scratch means from scratch, giving the same guidance, but without reading the current file at all. you read the file and give it what it needs to include" — User, this session

### Handoff reference is now dynamic
**Decision:** The opening instruction no longer hardcodes a session number. It tells Claude to glob for `session * handoff.md` and read the highest-numbered one.
**Reasoning:** A hardcoded number becomes stale every session and has caused confusion (the old file still said "session 23" at the start of this session).

### Arc C structure doc marked superseded
**Decision:** `campaign/structure/arc-c-fireball.md` is now in the Superseded table alongside A, B, and D, because the Arc C quest journal (`campaign/quests/act-i/fireball/`) is complete.
**Reasoning:** It was an oversight — the quest journal was finished in session 22 but the structure doc was never updated to reflect that.

### Three session-24 standing rules now in CLAUDE.md
**Decision:** These rules were established in session 24 but only written to the handoff, not to CLAUDE.md:
1. **Structuring draft means structuring draft** — the prose pipeline does not make a file "prose-polished"; never use that label
2. **Members-only for briefs and debriefs** — faction briefs/debriefs fire only for party members of that faction; Jarlaxle is the lone exception
3. **Players' Guide / GM Guide split** — the GM version is always the superset; no content exists only in the player version

### Attunement format updated with binary-only constraint
**Decision:** The existing attunement format rule now explicitly states: "Flags are binary (True/False only) — multi-state scenarios split into multiple flags." This was established in session 24 but missing from the rule text.

### Workspace Structure split into H3 subsections
**Decision:** The single flat 40-row table is now six clearly labeled subsections: Quest Journals, Arc Structure Documents (with Superseded/Active sub-tables), Location Journals, Campaign Guides, Setting, Appendices, and Sources.

### Arc E–J design summaries moved to dedicated section
**Decision:** The dense paragraph-length arc summaries that were crammed into table cells are now in a standalone `## Arc Design Summaries` section, one H3 per arc. The table rows for those arcs simply say "Structuring draft — see Arc Design Summaries."

### Standing Rules grouped into five clusters
**Decision:** The flat wall of standing rules is now organized under H3 headers: Design Principles, Mechanics, Writing Process, Content Rules, and Process Rules.

### Workflows deduplicated
**Decision:** The repeated "HTML Artifact delivery is deferred — see Output Format in Standing Rules" parenthetical that appeared at the end of four workflow steps has been removed from the workflows. It appears once, in the Output Format standing rule.

---

## Rules and Instructions

All session 24 rules still apply. The following were newly written into CLAUDE.md this session (they existed in the handoff but not in the file):

- **Structuring draft means structuring draft:** No content in this campaign is "prose-polished" in the final sense. The prose pipeline cleans up structural outlines; it does not replace the prose-writing pass. Never mark any file as "prose-polished" in CLAUDE.md.
- **Members-only for briefs and debriefs:** Faction briefs and debriefs fire only for party members of that faction. Jarlaxle is the lone exception — his debrief fires for any party that dealt with him, regardless of BD membership.
- **Players' Guide / GM Guide split:** The player version is the safe-to-share subset; the GM version includes everything in the player version plus Holder guidance, Warning callouts, DM-private tone notes, and Design Notes. No content exists only in the player version.
- **Attunement format (updated):** Flags are binary (True/False only) — multi-state scenarios split into multiple flags.
- **Dynamic handoff reference:** Start of session instructions now say to glob for `session * handoff.md` and read the highest-numbered one, not to open a hardcoded filename.

---

## Problems Solved

- **Stale session reference in CLAUDE.md:** The opening block said "session 23 handoff.md" at the start of a session 25 session. Fixed permanently by switching to a glob-based dynamic reference.
- **Arc C structure doc not marked superseded:** `campaign/structure/arc-c-fireball.md` appeared as an active structure doc even though `campaign/quests/act-i/fireball/` is complete. Corrected.
- **Three session-24 rules missing from CLAUDE.md:** The structuring-draft label rule, members-only briefs rule, and guide-split rule existed only in the session 24 handoff. Now written into the canonical file.
- **Attunement binary-only constraint missing:** The binary-flag constraint (established session 24) was absent from the standing rule text. Added.
- **Workspace table unreadable:** Arc E–J summaries were 5–6-line paragraphs packed into markdown table cells. Moved to a dedicated section with proper headings.

---

## Outstanding Work

Carried from session 24 (still unchecked):

- [ ] Prose-polish Appendix A NPC profiles
- [ ] Prose-polish Appendix C M5/M6 summaries
- [ ] Arc J Scene 6 Xanathar GONE debrief
- [ ] Appendix B (Monster Compendium) — not yet drafted

Pending arc conversions (structure docs → quest journals):

- [ ] Arc E — Faction Outposts
- [ ] Arc F — Xanathar's Lair
- [ ] Arc G — Cassalanter Villa
- [ ] Arc H — Sea Maidens Faire
- [ ] Arc I — Kolat Towers
- [ ] Arc J — Vault of Dragons

From session 24:

- [ ] Guides and setting pages (20 files) need a prose-writing pass at the final polish phase

---

## Warnings and Caveats

- **Arc D status:** The prose pipeline was run on Arc D (commits `46c6bdf`, `82135bc`, `4ddd35e`). Its status is "structuring draft that has been cleaned up by the prose pipeline" — consistent with the current "all structuring draft" rule, but worth noting if anyone asks why Arc D reads more smoothly than Arc C.
- **Arc C location journals are stub-level:** Cassalanter Villa, House of Inspired Hands, and Sea Maidens Faire location files exist but have not been through the prose pipeline.
- **ev-03b naming anomaly:** The front door file in Arc A is `ev-03b-the-front-door.md`, not a standard sequential number. Known; do not renumber unless a full resequence is explicitly requested.
- **Guide and setting files are content stubs:** The 20 new files from session 24 have correct section headings and bullet-point outlines. They are not written as playable DM-facing text. Prose pass is deferred to the final polish phase.

---

## Where to Start Next Session

The workspace is clean. CLAUDE.md is up to date, accurate, and well-organized. The next arc to convert is **Arc E — Faction Outposts**. Before drafting:

1. Load `adventure-reloaded`
2. Read `campaign/structure/arc-e-faction-outposts.md` (the active structure document)
3. Read `sources/Act_III_Arc_E.md` (Alexandrian Remix Arc E source — 903 lines, primary reference for all outpost heists)
4. Write and get an approved event decomposition plan (via ExitPlanMode) before drafting any prose
