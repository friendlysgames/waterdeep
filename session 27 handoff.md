# Session 27 Handoff
**Date:** 2026-09-23
**Status:** Ready to continue. The appendix dispersal plan is approved and Phase 1 is next.

---

## What Was Done

This was a planning session for converting every appendix into Ember format. Three Sonnet 4.6 research agents mapped three things: how Ember organizes reference material, what each appendix contains, and the current campaign structure. The resulting plan was approved. It dissolves Appendices A, C, D, E and F into Ember-style Setting Compendium and Guide pages. Two pieces of setup were also completed and committed: a project `settings.json` that pins subagents to `claude-sonnet-4-6`, and a new `journal-converter` agent that will do the conversion work. No campaign content was changed.

---

## Changes Made

Commits `4494081..HEAD`:

| Commit | What changed |
|--------|-------------|
| `7240bd4` | Created `.claude/settings.json` (subagent model env vars, agent teams) and `.claude/agents/journal-converter.md` (Sonnet 4.6 converter with verbatim-move / no-sidebar rules) |
| `c0c492c` | `teammateMode` changed from `tmux` to `in-process` (tmux isn't available on Windows) |

Files outside the repo:
- `C:\Users\robert.lupu\.claude\plans\i-want-you-to-fluttering-wand.md`: the approved plan, plus the Organization Page Spec and an Execution Status checklist with per-agent line ranges.
- Memory `feedback_sonnet_research_agents.md`: rewritten (see Rules).

---

## Key Decisions

### Full Ember dispersal of the appendices
**Decision:** The appendices stop existing as documents. Their content goes to `campaign/setting/notable-figures/` (A), `campaign/setting/organizations/` (C + D + E merged per faction), `campaign/guides/trollskull-manor/` (F, the Ember "Stronghold" analog), and `campaign/guides/gm-guide/running-the-villains.md` (E Parts 1 and 6). Every "Appendix X" reference gets retargeted, and the old `campaign/structure/appendix-*.md` files are removed with `git rm`.
**Reasoning:** Ember has no appendices. Its reference material lives in the Setting Compendium (Organizations, Notable Figures, Bestiary) and in GM Guide pages. The user chose this over keeping named appendix journals.

### One page per NPC
**Decision:** All 122 Appendix A profiles become individual pages, in 15 group folders under `notable-figures/`. Profile text moves word for word. Each page gets a new `> **[GM]**` Gamemaster's Summary (species, stat block, affiliation, featured-in) and a new player-safe `## Overview`.

### Appendix B skipped
**Decision:** Appendix B (Monster Compendium) is out of scope for this conversion and stays on the outstanding list.

### Restructure and fix stale content
**Decision:** Fix these while moving the text:
- `Ch. 3` references to retired files
- `1d4` roster counts in E's outposts, which become fixed numbers (from the Arc E structure doc if it gives one, otherwise the average rounded up)
- The "DM decides" line at C L17
- F's patron slot 18, "DM's choice"
- Heading-style mismatches

### Tavern dice are a mix
**Decision:** `06-tavern-time.md` gets a tenday schedule keyed to arc progress. Scheduled tendays have fixed patrons and events. Unscheduled tendays use the d20 Patron, Friends and Event tables. The d100 revenue roll stays. This is documented as a deliberate tavern exception to the no-dice rule.
> "Let's make it a mix, I think. Some tendays are scheduled, some aren't." (User, this session)

### Page format conventions
**Decision:** New pages use Ember's page structure with the repo's markdown conventions. That means `> **[GM]**` blockquote zones, the GM zone first and the player-facing `## Overview` last, bold-name cross-references, and plain `NN-slug.md` file names. Ember's HTML section classes are not used, and no sidebar callouts are added (structuring-draft rule).

---

## Rules and Instructions

- **Subagents run on `claude-sonnet-4-6` through project agent types.** Use the agents in `.claude/agents/` (`source-researcher`, `consistency-checker`, `prose-polisher`, `encounter-builder`, `journal-converter`). All of them pin `model: claude-sonnet-4-6`, so omit the Agent tool's `model` override. The bare `sonnet` alias is not acceptable.
  > "I said sonned 4.6, claude-sonnet-4.6." / "Agents let you use any model as long as you use the right code for it." / "you have an agents folder. see how those are set up" (User, this session)
- **Settings changes are authorized.**
  > "you have explicit permission to create and update the settings.json file" (User, this session)
- All prior standing rules apply.

---

## Problems Solved

- **Spawning Sonnet 4.6 agents:** The Agent tool's `model` parameter rejects full model IDs, and the user rejected the `sonnet` alias. The fix is to use project agent types whose frontmatter pins `claude-sonnet-4-6`, backed by the `CLAUDE_CODE_SUBAGENT_MODEL` env var in project settings.
- **The research agent said the `adventure-reloaded` skill was missing:** That was false. The agent searched `~/.claude/skills/`, but the skill lives at `.claude/skills/adventure-reloaded/SKILL.md` in the project. It exists, and its NPC Profile Format is at L364.
- **A new agent type isn't usable in the session that creates it:** `journal-converter` failed to spawn with "not found" until the session reloaded. It is now registered.
- **The settings write was blocked by the auto-mode classifier:** Written after the user gave explicit permission.

---

## Outstanding Work

Appendix dispersal. Follow the plan file's Execution section and commit after each phase:
- [ ] **Phase 1: Organizations** (10 pages in `campaign/setting/organizations/`). Run three parallel `journal-converter` agents, each told to read the Organization Page Spec appended to the plan file. The line ranges are in the plan's Execution Status.
- [ ] **Phase 2: Notable Figures** (122 NPC pages in 15 group folders). Run about 3 agents at a time and commit after each batch. Each agent greps `campaign/` for the "Featured in" lines.
- [ ] **Phase 3: Trollskull Manor guide** (9 pages). Split F, merge A §16 into `03-staff-and-hiring.md`, and build the tenday schedule.
- [ ] **Phase 4: Guide updates.** Create `gm-guide/running-the-villains.md`. Fold the D global preamble, C "How Renown Works" and Non-Player Factions into `gm-guide/player-factions-overview.md`, and the player-safe renown basics into `players-guide/faction-affiliations.md` (superset rule). A's "Omitted / Deferred" list goes into `design-notes-running-the-campaign.md`.
- [ ] **Phase 5: Prose pass.** Run `prose-polisher` on the new prose only: Overviews, Gamemaster's Summaries and the tavern schedule.
- [ ] **Phase 6: Retarget and delete.** Grep `Appendix [A-F]` and `appendix-` (about 234 hits in 46 files; skip the superseded arc A–D docs). Retarget each reference, `git rm` the five appendix files, update the CLAUDE.md Workspace Structure tables, and add NPC Page and Organization Page specs to the `adventure-reloaded` skill.
- [ ] **Verification.** 122 H4s in A must equal 122 H1s in `notable-figures/`. Diff-check 10 profiles for word-for-word text. There must be no dangling appendix references and no stale `1d4` / "DM decides" / `Ch. 3` text. Finish with a `consistency-checker` pass.

Carried forward:
- [ ] Prose-polish Appendix A NPC profiles (they will live in `setting/notable-figures/` after the dispersal)
- [ ] Prose-polish Appendix C M5/M6 summaries (they will live in the organization pages' Missions tables)
- [ ] Arc J Scene 6 Xanathar GONE debrief
- [ ] Appendix B (Monster Compendium), not yet drafted
- [ ] Guides and setting pages (20 files) need a prose-writing pass at the final polish phase
- [ ] Arc E: Faction Outposts conversion
- [ ] Arc F: Xanathar's Lair conversion
- [ ] Arc G: Cassalanter Villa conversion
- [ ] Arc H: Sea Maidens Faire conversion
- [ ] Arc I: Kolat Towers conversion
- [ ] Arc J: Vault of Dragons conversion

---

## Warnings and Caveats

- **CLAUDE.md is out of date on Appendix A.** It claims "55 Tier 1–2 profiles, 38 Tier 3, 1 Tier 4". Appendix A has no tier labels; it has 122 H4 profiles in 16 faction/role groups. Correct the table in Phase 6.
- **CLAUDE.md lists `appendix-b-monster-compendium.md`, but that file does not exist.**
- **A three-way overlap for the four villain principals** exists between A profiles, E's Personality and Agenda, and `setting/villains/*.md`. The plan keeps the villain pages separate and links them from the organization pages without copying their content.
- **The `setting/villains/*.md` pages use relative markdown links** to `../../structure/appendix-*.md`. These break when the appendices are deleted and must be retargeted in Phase 6.
- **The Arc E structure doc depends on E's outposts.** E's outpost entries point at the Arc E structure doc for the heist framework, so those references must stay intact through the move.
- **`sources/Appendix_D_-_Running_the_Tavern.md` is the upstream source for F's prose.** Leave it untouched; it is not one of the campaign appendices being deleted.
- **The Organization Page Spec exists only in the plan file.** The scratchpad copy is session-scoped.

---

## Where to Start Next Session

1. Read `C:\Users\robert.lupu\.claude\plans\i-want-you-to-fluttering-wand.md`: the approved plan, the Organization Page Spec (appended) and the Execution Status.
2. Copy the spec into the session scratchpad, or point the agents at the plan file directly.
3. Launch Phase 1 as three parallel `journal-converter` agents with no `model` override. Agent 1 writes pages 01–04 (C 21–244, D 17–308, A 1004–1306). Agent 2 writes 05–07 (C 245–415, D 309–531, E 307–440, A 1307–1768). Agent 3 writes the villain pages 08–10 (E 58–306, 375–395, 441–507, A 1769–2711).
4. Review the output and commit, then move on to Phase 2.
