# Session 24 Handoff
**Date:** 2026-09-21
**Status:** Ready to continue

---

## What Was Done

A cleanup session focused on two categories of technical debt. First: three targeted fixes — the "two nights ago" vs "last night" inconsistency in Arc A event files (per the Alexandrian timeline, the kidnapping happened the same night Volo left), stale "prose-polished" labels across the entire CLAUDE.md workspace table (all content is structuring draft; the prose pipeline was run on structural outlines, not final campaign prose), and stale Ember reference file paths (updated from `C:\Temp` stubs to the actual Downloads location, with the Milestone Progression file added as a new fourth reference). Second: the three monolithic introductory chapter files were modularized into 20 topic-scoped Ember-format pages across three new folder branches — `campaign/guides/players-guide/` (5 shareable files), `campaign/guides/gm-guide/` (8 DM-only files), and `campaign/setting/` (3 reference files + 4 villain character documents). The two files that appear in both guides (`about-this-campaign`, `debts-of-the-city`) follow the DM-as-superset pattern: the player version has only player-facing content; the GM version includes Holder guidance, Warning callouts, private tone notes, and Design Notes. The old chapter files received retirement headers and redirect links; no content was lost.

---

## Changes Made

### Commits Since Session 23 Handoff (`1620bee`)

| Commit | Message |
|--------|---------|
| `5d270d1` | fix: correct Arc A timeline and CLAUDE.md status labels |
| `a9dcc08` | docs: update CLAUDE.md Ember paths, ch1/ch2 descriptions, and draft labels |
| `ec1a94c` | refactor: modularize ch1/ch2/ch3 into players-guide/, gm-guide/, and setting/ |

### Files Created

| File | Purpose |
|------|---------|
| `campaign/guides/players-guide/about-this-campaign.md` | Three remix pillars, concept, who it suits (no DM private notes) |
| `campaign/guides/players-guide/character-creation.md` | General guidance, species notes, all XPHB + FRHoF backgrounds rated |
| `campaign/guides/players-guide/debts-of-the-city.md` | All 8 Debts — flavor + "Your character knows" only; no Holder sections |
| `campaign/guides/players-guide/bonds-and-flaws.md` | Bonds table (d8) and Flaws table (d8) with arc connections |
| `campaign/guides/players-guide/faction-affiliations.md` | Faction preview table, BD conditional entry, Two Zhentarims note |
| `campaign/guides/gm-guide/about-this-campaign.md` | Superset of player version; adds DM private notes on deaths, sympathy, tone |
| `campaign/guides/gm-guide/session-zero.md` | Full session zero script: pitch, gold question, contract, safety tools |
| `campaign/guides/gm-guide/debts-of-the-city.md` | Superset of player version; adds Holder guidance, Warning callouts, Design Note |
| `campaign/guides/gm-guide/adventure-summary.md` | Four-act overview table, dramatic arc per act, milestone pacing |
| `campaign/guides/gm-guide/structural-rules.md` | Two Zhentarims, response teams, festival calendar, Three Clue Rule, fireball victim, faction state tracking |
| `campaign/guides/gm-guide/grand-game-in-play.md` | Starting faction knowledge, escalation tiers (1–5), inter-faction conflict, when factions back down |
| `campaign/guides/gm-guide/player-factions-overview.md` | Six standard factions + BD unique mechanic; conflicting loyalties overview |
| `campaign/guides/gm-guide/design-notes-running-the-campaign.md` | Macro design notes for 8 major structural decisions |
| `campaign/setting/waterdeep-lore.md` | Wards, governance, guilds, religion, festival calendar, dragonward |
| `campaign/setting/history.md` | 8-era narrative history: Ahghairon through the players' arrival |
| `campaign/setting/grand-game.md` | In-world Grand Game frame; faction starting knowledge table |
| `campaign/setting/villains/xanathar.md` | 3 personality phases, relationships, goals, Sylgar note |
| `campaign/setting/villains/manshoon.md` | 3 phases (incl. Simulacrum), relationships, goals, Two Zhentarims DM note |
| `campaign/setting/villains/cassalanters.md` | 3 phases, relationships, goals, children timing note |
| `campaign/setting/villains/jarlaxle.md` | Zardoz Zord phase + adversary/ally tracks, relationships, goals, conditional entry note |

### Files Modified

| File | What changed |
|------|-------------|
| `CLAUDE.md` | All "prose-polished" labels stripped; ch1/ch2/ch3 entries marked RETIRED; 20 new entries added; Ember reference paths updated to real Downloads location; Milestone Progression added as 4th Ember reference; ch1/ch2 descriptions corrected; session handoff reference bumped to 23 |
| `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md` | Line 97: "two nights ago" → "last night" (Skewered Dragon reference); line 135 Summary: "two nights ago" → "last night" |
| `campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md` | Line 21: Zhentarim grab "last night" (not two nights); line 43: Skewered Dragon regulars remember Volo "last night" |
| `campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md` | Line 52: Renaer's account — grabbed "last night" |
| `campaign/structure/ch1-beginning.md` | RETIRED header with redirect links to players-guide/ and gm-guide/ |
| `campaign/structure/ch2-city-of-splendors.md` | RETIRED header with redirect links to setting/ and setting/villains/ |
| `campaign/structure/ch3-running-the-campaign.md` | RETIRED header with redirect links to gm-guide/ |

---

## Key Decisions

### All campaign content is structuring draft — no final prose exists yet
**Decision:** The "prose-polished" labels in CLAUDE.md were removed across the board. Every arc, appendix, location journal, and guide is at structuring draft stage.
**Reasoning:** The prose pipeline was run on structural content (outlines, skeleton scenes, planning text), not on final campaign prose. A structuring draft that was cleaned up by the prose pipeline is still a structuring draft — it has not been written as actual DM-facing playable text.
> "the structuring was prose polished, we haven't written any actual full drafts yet, just structure" — User, this session

### Players' Guide / GM Guide split — DM version is always the superset
**Decision:** Files that appear in both guides (`about-this-campaign`, `debts-of-the-city`) have two distinct versions. The player version contains only what is safe to share at the table. The GM version is a strict superset: it includes all player-facing content plus Holder guidance, Warning callouts, private tone notes, and Design Notes. No content exists only in the player version.
**Reasoning:** Standard Ember practice for guide documents that serve both audiences.
> "Guides should be separated into DM and Players' guides, with some information being repeated in both" — User, this session

### Ember reference files now point to the actual Downloads location
**Decision:** All four Ember reference file paths in CLAUDE.md were updated from `C:\Temp\ember\*.md` stubs to the real paths under `C:\Users\robert.lupu\Downloads\01 - Ember\01 - Ember\`. The Milestone Progression file was added as a new fourth reference.
**Reasoning:** The `C:\Temp` paths were placeholder stubs and did not actually exist. The user moved the full Ember collection to their Downloads folder.
> `"C:\Users\robert.lupu\Downloads\01 - Ember\01 - Ember"` — User, this session

---

## Rules and Instructions

All session 23 rules still apply, plus:

- **Structuring draft means structuring draft:** No content in this campaign is "prose-polished" in the final sense. The prose pipeline cleans up structural outlines; it does not replace the prose-writing pass. Never mark any file as "prose-polished" in CLAUDE.md.
- **Players' Guide / GM Guide split:** Any content that exists in both guides must follow the superset rule — player version is the safe-to-share subset; GM version includes everything in the player version plus DM-private content.
- **Arc A timeline:** Floon's kidnapping was "last night" (Alexandrian timeline). "Two nights ago" (WDH RAW) is wrong throughout. This fix is now applied to ev-01, ev-02, ev-03.
- **Attunement format:** All attunements must be `#### Flag Name: True / False`. Binary only. Multi-state splits into multiple flags.
- **Members-only for briefs AND debriefs:** Faction briefs fire only for members of that faction. Jarlaxle is the lone exception.
- **Git commits:** End of every turn that changes files. Message explains WHY.
- **Handoff timing:** Only when user invokes `/handoff`.
- **Plan before drafting:** Approved arc plan (via ExitPlanMode) before any prose.
- **Prose pipeline:** `deslop-text` + `no-ai-slop` → `humanize-prose`. Recursive until clean.
- **Boss design:** Named villains use `boss-design` only.
- **Encounter math:** `cr2-encounter-builder` only. Never DMG XP.
- **No HTML Artifacts:** Deferred until all arcs, chapters, appendices are complete.
- **Source research:** Always read `SOURCE_GUIDE.md` + relevant source files before drafting. Never work from memory.

---

## Problems Solved

- **"Two nights ago" in Arc A:** Three occurrences across ev-01, ev-02, ev-03 where the Arc A timeline used WDH RAW ("two nights ago") instead of the Alexandrian timeline ("last night"). All three corrected.
- **Stale "prose-polished" labels:** CLAUDE.md listed multiple arcs, appendices, and locations as "fully prose-polished." This was inaccurate — the prose pipeline cleaned up structural outlines, not final campaign prose. All labels corrected to "Structuring draft."
- **ch1/ch2 CLAUDE.md descriptions misidentified their content:** ch1 was described as "Arc A (Finding Floon)" and ch2 as "Arc B (Trollskull Alley)" — confusing them with the quest journals. Both corrected to accurate content descriptions.
- **Ember reference paths pointed to nonexistent stubs:** The three `C:\Temp\ember\*.md` paths in CLAUDE.md did not exist. Updated to the real paths in the full Ember collection at Downloads.

---

## Outstanding Work

Carried from session 23 (still unchecked):

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

New this session:

- [ ] Guides and setting pages are structuring drafts — all 20 new files need a prose-writing pass when the campaign reaches the final polish phase

---

## Warnings and Caveats

- **Arc D CLAUDE.md entry says "structuring draft"** — per the session 23 warning, the prose pipeline was run on Arc D (commits `46c6bdf`, `82135bc`, `4ddd35e`). Its status is equivalent to Arc C: structuring draft that has been cleaned up by the prose pipeline. This is consistent with the current "all structuring draft" rule.
- **Arc C location journals are stub-level** — Cassalanter Villa, House of Inspired Hands, and Sea Maidens Faire location files exist but have not been through the prose pipeline at all.
- **ev-03b naming anomaly** — The front door file is `ev-03b-the-front-door.md`, not a standard sequential number. Known; do not renumber unless a full resequence is explicitly requested.
- **The new guides and setting files are content stubs** — Each new file has the correct section headings and bullet-point outlines from the source chapters. They are not yet written as playable DM-facing text. The structure is right; the prose needs to happen at the final polish phase.

---

## Where to Start Next Session

The session's cleanup tasks are all complete. The workspace is fully consistent:
- Arc A timeline is correct throughout
- CLAUDE.md labels accurately describe every file's status
- ch1/ch2/ch3 are retired and replaced by modular files
- Ember reference paths point to the real files

The next arc to convert is **Arc E — Faction Outposts** (`campaign/structure/arc-e-faction-outposts.md`). Before drafting:
1. Load `adventure-reloaded`
2. Read `campaign/structure/arc-e-faction-outposts.md` (the structure document)
3. Read `sources/Act_III_Arc_E.md` (Alexandrian Remix Arc E source — 903 lines, primary reference for all outpost heists)
4. Write and get an approved event decomposition plan before drafting any prose
