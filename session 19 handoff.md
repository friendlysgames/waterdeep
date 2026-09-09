# Session 19 Handoff
**Date:** 2026-09-10
**Status:** Ready to continue

---

## What Was Done

This session established the structural framework for the campaign's transition from monolithic arc files to an Ember-style modular document format. A master plan document was drafted and approved, then implemented across two files: CLAUDE.md was updated with an Active Plan reference, a Milestone Points standing rule, updated arc-drafting workflow, new workspace rows, and Ember format reference file pointers; the `adventure-reloaded` skill was completely rewritten to document all six file types (Quest Overview, Event File, Area Overview, Keyed Room, Design Notes, Flowchart), the Foundry Journal Model, the GM/Player Zone Structure, the Cross-Document Callout Syntax, and the Milestone Points System. The campaign's XP milestone system was retired in favor of Ember's Milestone Points — no XP is tracked going forward.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `CLAUDE.md` | Added Active Plan section (pointer to structural plan); added Milestone Points standing rule; updated Skills Reference description for adventure-reloaded; updated Workflow step 3 for arc drafting (Quest Journal + Location Journal pattern); added `campaign/quests/` and `campaign/locations/` rows to Workspace Structure; added Ember format reference files to Source Research section |
| `.claude/skills/adventure-reloaded/SKILL.md` | Full rewrite: Document Architecture (updated tree), Foundry Journal Model (new section), GM/Player Zone Structure (new section), File Types replacing Arc Structure (all 6 types with format templates), Cross-Document Callout Syntax (new section), Milestone Points System replacing Milestone XP Tables; kept unchanged: Chapter 2, Chapter 3, Callout Taxonomy, NPC Profile Format, Design Notes Philosophy, Scene Writing Voice, The Remix is a Whole |

### Files Created
| File | Purpose |
|------|---------|
| `C:\Users\robert.lupu\.claude\plans\that-s-pretty-much-what-tingly-summit.md` | Master structural plan: Why This Change, Milestone Points System, Foundry Journal Model, Markdown Folder Structure, all 6 File Type specs with format templates, Cross-Document Callout Syntax, Drafting Order, skill update spec |

---

## Key Decisions

### Ember-style modular document structure adopted
**Decision:** All future arc content is drafted as Quest Journals (one folder per arc, flat files = pages: overview → event files → flowchart → design notes) with separate Location Journal folders (area overview + keyed room pages). Existing monolithic `campaign/structure/arc-*.md` files are retired arc-by-arc as the modular versions are built. New folders: `campaign/quests/` and `campaign/locations/`.
**Reasoning:** Foundry VTT requires one journal page per unit — a 2,000-line arc file cannot become a Foundry journal. The Ember FoundryVTT module demonstrates the correct granularity: one file per event, one file per keyed room, named cross-references between files. Arc A is the pilot conversion.
> "swap arcs for this structure, with quests/events and keyed locations, and calling out between each other" — User, this session

### Milestone Points replaces XP
**Decision:** The campaign now uses Ember's Milestone Points system. No XP is tracked. Each milestone-bearing Event awards 1 Milestone Point to the whole party. Main Quest arcs award ~2 points total; Side Quests and Faction Missions award 1 point. Level-up is instant and party-wide; recovers HP/slots but not item charges. Campaign target: Level 8 by Arc J = 28 cumulative milestone events. When existing arc files are decomposed, XP values are not converted — milestone events are re-designated by narrative weight.
> "we are also moving away from milestone XP towards Milestone Points, like in Ember" — User, this session

### Folder = Journal, File = Page (Foundry Journal Model)
**Decision:** Each markdown folder maps to one Foundry Journal Entry. Each `.md` file within that folder becomes one Page. Quest journals and location journals are separate Foundry entries — a location folder never lives inside a quest folder. Files within a journal folder are flat siblings (no events/ subfolder).
> "each folder is a journal, each file is a page" — User, this session

### `> **[GM]** >` blockquote is selective, not a wrapper
**Decision:** The GM blockquote callout is used in event files only for: the `#### Gamemaster's Summary` at the top, specific tactical spoilers mid-body, and `#### Next Steps` + `#### Milestone:` at the end. It does NOT wrap all GM content — most of the GM zone is regular markdown.
**Reasoning:** Confirmed by reading actual Ember event files; the first plan draft was wrong about this.

### Ember format files referenced in CLAUDE.md
**Decision:** Three Ember source files are cited in CLAUDE.md's Source Research section as format references: `C:\Temp\ember\quest-event-combat.md` (most complete event example), `C:\Temp\ember\quest-overview.md` (quest overview format), `C:\Temp\ember\area-keyed-room.md` (keyed room pattern).
> "also add a reference in claude.md to a single quest and location from ember so that future sessions know where to look for guidance" — User, this session

---

## Rules and Instructions

All standing rules from Session 18 carry forward unchanged, plus:

- **Milestone Points system:** No XP is tracked in any new content. Each milestone-bearing event file uses `#### Milestone: [Event Name]` inside the `> **[GM]** > #### Next Steps` block. See `adventure-reloaded` for the full progression table (L1→L8, 28 cumulative points) and level-up rules.
- **New arc drafting format:** Quest Journals (flat folder: overview → event files → flowchart → design notes) and Location Journals (area overview → keyed room pages) are now the mandated format. Load `adventure-reloaded` before drafting any of these file types — it has the complete format templates.
- **Cross-document callout syntax:** Bold event/location names, never file paths. "Proceed to the **Zhentarim Raid** Event." Full syntax table in `adventure-reloaded`.
- **Ember format references:** When in doubt about document format, read `C:\Temp\ember\quest-event-combat.md` (event files), `C:\Temp\ember\quest-overview.md` (overview), `C:\Temp\ember\area-keyed-room.md` (keyed rooms) before writing.

---

## Problems Solved

- **Monolithic arc format incompatibility with Foundry:** Resolved by designing and documenting the Ember-style modular structure in the plan and rewriting the `adventure-reloaded` skill to fully specify it.
- **XP system inconsistency with Ember reference:** Resolved by retiring XP milestone tracking entirely and adopting Milestone Points; documented in the standing rule, skill file, and memory.
- **`> **[GM]** >` misunderstood in first plan draft:** First plan described the GM blockquote as wrapping the entire GM zone. Reading actual Ember event files corrected this — it's a selective callout marker. Plan and skill updated to reflect selective usage.

---

## Outstanding Work

Carried forward from Session 18:
- [ ] **Run consistency-checker one more time** — four post-check fixes from session 18 were applied inline without a follow-up QA pass.
- [ ] **Prose-polish pass on new NPC profiles** — 12 profiles added to Appendix A in session 18 were written by an agent without running deslop-text + no-ai-slop + humanize-prose.
- [ ] **Prose-polish pass on App C M5/M6 mission summaries** — agent-written summaries need a deslop pass.
- [ ] **Arc J Scene 6 Xanathar GONE debrief** — Scene 5 has a GONE row; Scene 6 has no corresponding resolution paragraph for this state.
- [ ] **Appendix B (Monster Compendium)** — Not yet drafted.

New this session:
- [ ] **Arc A pilot conversion** — Decompose `campaign/structure/arc-a-finding-floon.md` into the modular Quest Journal format: `campaign/quests/act-i/arc-a-finding-floon/` folder with overview.md, flowchart.md, ev-01 through ev-04, design-notes.md. Then build location journals for the Zhentarim Warehouse and Xanathar Sewer Hideout. Arc A is the format pilot before touching any other arc.
- [ ] **Remaining arc decompositions** — Arcs B, C → D → E → F, G, H, I → J. See the Drafting Order in the structural plan.

---

## Warnings and Caveats

- **XP values in existing arc files:** `campaign/structure/arc-*.md` files still contain XP milestone language. These are retired-format files — do not update them in place. When each arc is decomposed into event files, those XP designations are replaced by Milestone Point assignments (narrative-weight-based, not converted).
- **`campaign/quests/` and `campaign/locations/` directories do not yet exist** — they are declared in CLAUDE.md but no files have been placed there. Arc A pilot conversion creates them.
- **Ember reference files at `C:\Temp\`** — these are outside the project repo and will not survive a machine wipe. If they go missing, the adventure-reloaded skill documents the format fully and is the authoritative reference.
- Warnings from Session 18 still apply: Arc J GONE debrief, Arc H Design Notes Full Awakening subsection, App C M5/M6 summaries unpolished, Vessa cross-reference check.

---

## Where to Start Next Session

Read this file, then `git log 1efbe50..HEAD --oneline` to see the two commits from this session. The immediate next task is the Arc A pilot conversion: decompose `campaign/structure/arc-a-finding-floon.md` into the modular Quest Journal format under `campaign/quests/act-i/arc-a-finding-floon/`, then build the two location journals (Zhentarim Warehouse and Xanathar Sewer Hideout) under `campaign/locations/`. Load `adventure-reloaded` before starting — it has the complete file-type templates. Read the Ember event file at `C:\Temp\ember\quest-event-combat.md` for the authoritative event file format before writing any event pages. The structural plan at `C:\Users\robert.lupu\.claude\plans\that-s-pretty-much-what-tingly-summit.md` has the full drafting order and folder structure.
