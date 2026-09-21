# Session 26 Handoff
**Date:** 2026-09-21
**Status:** Ready to continue

---

## What Was Done

A full conversion session. All 43 faction missions (42 complete + 1 drafted from scratch) were converted from their flat bold-text format in `appendix-d-running-factions.md` into modular quest-journal folders matching the Ember-style format used by Arcs A–D. Seven factions were processed in order: Order of the Gauntlet → Emerald Enclave → Force Grey → Lords' Alliance → Doom Raiders → Harpers → Bregan D'aerthe. Each faction's missions now live under `campaign/quests/faction-missions/[faction-slug]/[mNN-slug]/` as standalone Foundry Journal Entries. The session also settled a significant design question: faction missions award no Milestone Points, because the main arc ladder already covers the full 1→8 progression and stacking 7 potential M6 milestones would break pacing.

---

## Changes Made

18 commits from `2c267c4..HEAD`:

| Commit | What changed |
|--------|-------------|
| `1465505` | OG faction missions M1–M6 (16 files) |
| `90c5963` | EE faction missions M1–M6 (14 files) |
| `48cddbf` | FG faction missions M1–M6 + removed erroneous flowchart stubs (18 files) |
| `67d36b2` | LA faction missions M1–M6 (19 files) |
| `ad0a7b5` | DR faction missions M1–M6 (19 files) |
| `d6f9319`–`7879ea1` | Harper missions M1–M6, one commit per mission (21 files) |
| `5ac239a`–`b90d1bb` | BD missions M1–M6 + M2b optional, one commit per mission (21 files) |

Total new files: ~128 `.md` files across 44 mission folders (43 missions + M2b).

---

## Key Decisions

### Faction missions award no Milestone Points
**Decision:** No faction mission awards a Milestone Point — not even M6 terminal missions.
**Reasoning:** The main arc ladder (Arcs A–J) already covers the complete 1→8 progression. A party in 5 factions could complete 5 M6 missions, adding 5 unplanned points that would push them past Level 8 during the heist phase. Faction rewards are gold, renown, tangible items, and cross-arc intel — that is sufficient.
**Rule updated in plan:** `C:\Users\robert.lupu\.claude\plans\let-s-turn-the-faction-agile-noodle.md`

### Folder structure: one Foundry Journal Entry per mission
**Decision:** `campaign/quests/faction-missions/[faction]/[mNN-slug]/` — each mission folder = one Foundry Journal Entry, each `.md` file = one Page.
**Reasoning:** Matches Ember's standalone quest model; allows per-mission permission gating in Foundry.

### BD M6 drafted from scratch
**Decision:** The Appendix D source had only a Hook and two lines of Background for BD-M6 (The Dive). The mission was drafted in full this session: harbor recovery of Eye #3 from a 40-foot wreck, Xanathar Guild dive team as opposition, Krebbyg coordinating via rope signals, lookout neutralization phase.

### BD M2b as a conditional optional mission
**Decision:** The Betrayal Pitch gets its own folder (`m02b-the-betrayal-pitch/`) with a `> [!warning]+` callout stating both required conditions (BD party member + prior Jarlaxle contact).

### Harper M4 BD variant as `[!abstract]+` sidebar
**Decision:** The "If a BD Operative Is Present" block in Harper M4 becomes a `[!abstract]+` callout inside ev-01, not an H3 branch. The sidebar covers the garden conversation, Jarlaxle's intelligence offer (a compromised Harper asset in the Sea Maidens Faire), and the three-way brokering option.

### Per-mission commits
**Decision:** Corrected mid-session — Harpers and BD agents committed after each individual mission folder rather than once at the end, preserving work incrementally.

---

## Rules and Instructions

All prior standing rules apply. No new rules established this session.

---

## Problems Solved

- **FG agent created erroneous `flowchart.md` files** — caught on review, deleted in the cleanup commit (`48cddbf`).
- **FG agent stopped mid-run due to session limit** — resumed successfully; M6 and flowchart cleanup completed.
- **Milestone budget overrun risk** — identified and resolved before any files were written; plan updated before first agent launched.

---

## Outstanding Work

Carried from session 25 (still unchecked):

- [ ] Prose-polish Appendix A NPC profiles
- [ ] Prose-polish Appendix C M5/M6 summaries
- [ ] Arc J Scene 6 Xanathar GONE debrief
- [ ] Appendix B (Monster Compendium) — not yet drafted
- [ ] Guides and setting pages (20 files) need a prose-writing pass at the final polish phase

New from this session:

- [ ] **Update `appendix-d-running-factions.md`** — remove the full mission write-ups (now superseded by quest journals), replace with H3 header stubs pointing to the journal paths. Keep intact: Grand Game Stance sections, Arc Hooks tables, per-faction preamble prose.
- [ ] **Update CLAUDE.md Workspace Structure** — add `campaign/quests/faction-missions/` as a new row in the Quest Journals table, describing all 7 faction folders as complete. Note the no-milestone-points decision in the Mechanics standing rules.
- [ ] **`adventure-reloaded` skill update** — the skill currently says "Side Quest / Faction Mission — 1 Milestone Point on completion of its terminal event." This rule is now wrong for this campaign. Update to carve out faction missions explicitly.

Pending arc conversions (unchanged):

- [ ] Arc E — Faction Outposts
- [ ] Arc F — Xanathar's Lair
- [ ] Arc G — Cassalanter Villa
- [ ] Arc H — Sea Maidens Faire
- [ ] Arc I — Kolat Towers
- [ ] Arc J — Vault of Dragons

---

## Warnings and Caveats

- **Appendix D is now partially redundant** — its mission text duplicates the quest journals. Until the Appendix D cleanup is done, both versions exist. The quest journals are authoritative; Appendix D is the legacy source.
- **`adventure-reloaded` skill has a stale milestone rule** — it says faction missions award 1 Milestone Point. This is incorrect for this campaign and needs updating before any future content references it.
- **Force Grey flowchart stubs were committed and then removed** — the git history has those stubs in commits before `48cddbf`. This is fine; they are fully deleted in the cleanup commit.
- **EE M6 carries an `Illuun Contact` flag for Undermountain Level 4** — the agent added this unprompted based on the source material. It is a valid connection worth preserving.
- **FG M4 references Nihiloor as the same mind flayer who appears in Arc F** — the design-notes.md documents how to handle the encounter depending on whether M4 ran before or after Arc F.

---

## Where to Start Next Session

Three cleanup tasks are ready to go (any order, can be done in one session):

1. **Update `adventure-reloaded` skill** — change the Milestone Points section to state that faction missions in this campaign award no Milestone Points (main arc ladder handles full progression).
2. **Update CLAUDE.md** — add `campaign/quests/faction-missions/` to the Workspace Structure table; add the no-faction-milestone rule to the Mechanics section.
3. **Clean up `appendix-d-running-factions.md`** — remove the full mission write-ups, replace with pointers to the quest journals. Keep Grand Game Stance + Arc Hooks + preamble prose.

After those three are done, the next major task is **Arc E — Faction Outposts** conversion (load `adventure-reloaded`, read `arc-e-faction-outposts.md` and `sources/Act_III_Arc_E.md`, write and get an approved event decomposition plan).
