# Session 28 Handoff
**Date:** 2026-09-24
**Status:** Ready to continue. The appendix dispersal plan is complete, and no task is in progress.

---

## What Was Done

All six phases of the approved appendix dispersal plan are finished. Appendices A, C, D, E and F are gone. Their content now lives in:
- an Ember-style Setting Compendium: 122 Notable Figures pages and 10 Organization pages
- a new Trollskull Manor guide of 9 pages, including a new tenday schedule
- a new GM Guide page, Running the Villains
- existing guide pages that absorbed renown rules, the mission preamble and the Omitted NPCs list

The campaign also moved from "arcs" to "quests within Acts":
- Arc labels are gone from every live campaign file.
- Fireball! and Gralhund Villa moved to `act-ii/`.
- CLAUDE.md and the `adventure-reloaded` skill were updated to match.

A final `consistency-checker` pass found 8 issues, and all were fixed. Several continuity problems were settled along the way: the escalation vocabulary, the Stone and Eye state at campaign start, Lady Gondafrey's canon, and the Order of the Gauntlet contact.

---

## Changes Made

Range `3880e39..HEAD` covers 25 commits and 306 files: 142 added, 135 modified, 5 deleted and 24 renamed.

| Commit | What changed |
|--------|-------------|
| `636a26d` | Phase 1: 10 Organization pages merging C + D + E per faction; dice rosters and timers replaced with fixed values |
| `ca36952` | Replaced Arc labels with quest names on Organization pages; "Arc Hooks" became "Quest Hooks" |
| `600cc23` | Moved `quests/act-i/fireball` and `gralhund-villa` to `quests/act-ii/` |
| `716f0cc`, `10422d1` | Phase 2: 122 Notable Figures NPC pages in 15 group folders |
| `986bb47` | Lady Gondafrey: City Watch captain and knight of Tyr, imprisoned for 113 years (Arc I structure doc) |
| `4fdc757` | Phase 3: Trollskull Manor guide (9 pages) plus the tenday schedule; placeholders in F resolved |
| `8a66999`, `e2b896e` | CLAUDE.md Process Rule: agents do the work, and are resumed after rate limits |
| `37b9587` | Phase 4: `running-the-villains.md`; renown and preamble merged into guide pages; Omitted NPCs moved to design notes |
| `41a475b`, `17b6b83`, `3edccf9`, `59d14bb` | Phase 5: prose pass on the new prose; 13 Overviews that leaked spoilers rewritten; agenda paragraphs moved to the GM zone |
| `6bd132b` | Single escalation vocabulary; campaign-start Stone/Eye state corrected |
| `1dd93ea`, `0c9694f`, `04d9158`, `5de9df5`, `6edea1d`, `61eb91a`, `b56423a` | Phase 6: appendix references retargeted and Arc labels stripped in setting, guides, SOURCE_GUIDE, Act I–II quests, locations, structure docs E–J and faction missions |
| `7e08763` | `git rm` of the five appendix files; CLAUDE.md and `adventure-reloaded` skill updated |
| `b12bd1c` | Osvaldo's visits settled (replaced a "DM decides" line) |
| `e1b5119` | 8 fixes from the consistency-checker |

### Files Created
| Path | Purpose |
|------|---------|
| `campaign/setting/notable-figures/[15 groups]/NN-name.md` | 122 NPC pages: `> **[GM]**` Gamemaster's Summary, profile moved word for word, player-safe Overview |
| `campaign/setting/organizations/01-harpers.md` … `10-cassalanters.md` | Faction pages. GM zone first, then Operations, Key Members, Grand Game Stance (Agenda/Stance), Quest Hooks, First Meeting, villain sections, Renown & Ranks, Missions, Overview |
| `campaign/guides/trollskull-manor/01–09` | Stronghold guide split from Appendix F; `06-tavern-time.md` holds the Tenday Schedule and the Slot 18 table |
| `campaign/guides/gm-guide/running-the-villains.md` | Appendix E Parts 1 and 6: Grand Game, MacGuffin chain, starting knowledge, escalation, inter-faction operations |

### Files Deleted
| File | Reason |
|------|--------|
| `campaign/structure/appendix-a-npc-roster.md` | Dispersed to Notable Figures; §16 dropped because it duplicated F's staff tables |
| `campaign/structure/appendix-c-player-factions.md` | Dispersed to Organizations and Player Factions Overview |
| `campaign/structure/appendix-d-running-factions.md` | Dispersed to Organizations and Player Factions Overview; mission stubs dropped |
| `campaign/structure/appendix-e-villain-factions.md` | Dispersed to villain Organization pages and Running the Villains |
| `campaign/structure/appendix-f-running-the-tavern.md` | Dispersed to the Trollskull Manor guide |

Files outside the repo:
- The plan file `C:\Users\robert.lupu\.claude\plans\i-want-you-to-fluttering-wand.md` has its Execution Status marked complete.
- Two new memories: `feedback_no_arc_labels.md` and `feedback_delegate_to_agents.md`.

---

## Key Decisions

### Quests in Acts, not arcs
**Decision:** No "Arc X" labels anywhere. Quests are referred to by bold name. The Acts are:
- **Act I:** Finding Floon and Trollskull Alley.
- **Act II:** Fireball! and Gralhund Villa.
- **Act III:** Faction Outposts and the four lair heists.
- **Act IV:** Vault of Dragons.

Structure-doc filenames keep their `arc-*` slugs until each doc is converted.
> "Remember we made a decision: no more arcs, only quests in Acts." (User, this session)

### Act II folder
**Decision:** Fireball! and Gralhund Villa live in `campaign/quests/act-ii/`.
> "The act 2 folder is missing, fix that, it should contain fireball and gralhund villa." (User, this session)

### Lady Gondafrey canon
**Decision:** Follow WDH. She was a City Watch captain and a knight of Tyr, captured in 1379 DR, and has been imprisoned for 113 years, not 47. The Order of the Gauntlet did not exist in 1379, so Savra's hook is reframed: the Order inherited the unfinished cases of Tyr's knights. The user asked for my recommendation and I chose this.
> "Which do you think is best for Gindafray? After that, next phase" (User, this session)

### Escalation vocabulary
**Decision:** Four tiers only: Unaware / Suspicious / Alert / Lockdown. The lair quests already read these tiers; for example, Manshoon's location depends on the tier. Xanathar's response teams are called First, Second and Third Team, never "Tier N".
> "1. Pick one and use an agent to edit" (User, this session)

### Campaign-start Stone/Eye state
**Decision:** The Act I–II quest journals are canonical. Dalakhar carries the Stone until the fireball, then the Gralhunds have it. Xanathar holds only Eye #1, in Sylgar's fishbowl, and does not know what it is for.
> "2. Fix with an agent." (User, this session)

### Appendix A §16 dropped
**Decision:** §16 (Tavern Staff Candidates) was not merged anywhere. It lists the same 25 candidates that F's staff tables already profile in full.

### Tenday Schedule design
**Decision:** Nine scheduled nights, keyed either to fixed calendar tendays (the fireball aftermath, the Faire's last tenday, Founders' Day) or to quest completion (Gralhund Villa, the first lair heist, Vault of Dragons). The schedule works in any heist order. A Slot 18 table names one Campaign NPC per quest. The d20 tables and the revenue roll stay as a documented tavern exception to the no-dice rule.

### Grand Game agenda paragraphs out of the player zone
**Decision:** On the player-faction Organization pages, the paragraphs from Appendix C about the Stone, the gold, the Cassalanters' diabolism and Jarlaxle's aims were moved word for word from the Overview into Grand Game Stance, under `### Grand Game Agenda`. Each Overview now holds only a player-safe summary.

### Renown rules made zero-prep
**Decision:**
- Removed "DM may award +1/+2" and the "+3/+4" line.
- A serious offense costs 2 renown.
- Renown is always tracked numerically.
- Bregan D'aerthe's "+1 DM's discretion" bonus fires once per quest when an objective is met by a method the write-up doesn't list.

---

## Rules and Instructions

- **Quests, not arcs.** Now in CLAUDE.md Content Rules and in memory.
  > "no more arcs, only quests in Acts" (User, this session)
- **Agents do the work; resume them after rate limits.** Now in CLAUDE.md Process Rules and in memory. When an agent stops on a rate limit, resume that same agent with SendMessage after the reset. Never take its work over inline.
  > "Claude as a whole hit rate limit. Whenever that happens, continue the agent, don't do stuff yourself. Save as a rule" (User, this session)
  > "you're Opus. The agents are Sonnet. You are the orchestrator, not the worker. Making you write it rather than planning and check it is a waste of tokens." (User, this session)
- **Escalation tiers.** Unaware / Suspicious / Alert / Lockdown only. This is now in CLAUDE.md Content Rules.
- **Player-facing Overviews show only the public face.** No Stone, Eyes, vault, cult, contract, Manshoon's name or location, or secret allegiances. This is written into the NPC Page spec in the `adventure-reloaded` skill.
- All prior standing rules still apply.

---

## Problems Solved

- **The journal-converter stopped on a rate limit and I took over inline.** The user corrected this. Agents are now always resumed with SendMessage; I used this for eight agents across two limits.
- **Spoilers in player-facing Overviews.** Converter and polisher output leaked GM facts. Review caught 13 cases:
  - Black Viper, Dalakhar, Manshoon, Chirada, Aurinax, Kelso, Filthy Meg, Jelenn and Manafret.
  - Corene and Valdra, whose leaks the polisher introduced itself.
  - The villain Organization pages.
  - The Grand Game agenda paragraphs.
- **Placeholders turned into concrete rules:**
  - Lady Gondafrey's d10 alignment now follows the Kolat Towers time-of-day rule.
  - Agorn at Yellowspire is present from dusk to midnight, which the party can learn by casing.
  - Zorbog's "if the DM runs them" line was removed.
  - Osvaldo: Ammalia visits weekly and Victoro has not visited in months.
  - Harlsnod's urns are empty.
  - Harper informants deliver one report per outpost operation once a Harper PC has Renown 30+.
  - F's candidate arrival, Slot 18/19/20, Event 20 and the Halaster easter egg are all fixed.
- **Factual errors fixed:**
  - "Kaevra" corrected to "Kaevja".
  - The Players' Guide listed Hlam as the Order of the Gauntlet contact; it is Savra Belabranta.
  - Sister Valdra is a half-orc in the staff table.
  - "Noska Ur'Gray" corrected to "Ur'gray".
  - Jeryth's stat block is "none".
  - Meloon is possessed, not a Guild member.
- **Broken links:** `setting/villains` had `../guides` instead of `../../guides`, and `10-the-cassalanters.md` instead of `10-cassalanters.md`.

---

## Outstanding Work

- [ ] Appendix B, now the **Bestiary**: never drafted. Pages reference it as "the **Bestiary** (not yet drafted)", including the Xanathar two-phase boss, Victoro and Ammalia, and Aurinax.
- [ ] Faction Outposts conversion (`campaign/structure/arc-e-faction-outposts.md` → quest journal)
- [ ] Xanathar's Lair conversion
- [ ] Cassalanter Villa conversion
- [ ] Sea Maidens Faire conversion
- [ ] Kolat Towers conversion
- [ ] Vault of Dragons conversion
- [ ] Vault of Dragons Scene 6: Xanathar GONE debrief
- [ ] Guides and setting pages need a prose-writing pass at the final polish phase. That now includes the Organization pages and the Trollskull Manor guide.
- [ ] Prose polish of the word-for-word NPC profile text in Notable Figures (Phase 5 polished only the new Overviews)
- [ ] Prose polish of the Mission 5 and Mission 6 summaries, now in each Organization page's Missions table

---

## Warnings and Caveats

- **The structure docs E–J still use dice and have not been converted.** They were retargeted but not zero-prepped. Faction Outposts still has `1d4 days` response timers, Agorn's "one-in-three chance", and 1d4+2 alarm rounds. The Organization pages use fixed values (3 days, dusk to midnight), so resolve these to match when converting Faction Outposts.
- **Grinda Garloth's inventory** on the Xanathar's Guild page cites 2014 "DMG Table A/B/F". Convert it to 2024 rarity when you reach Bestiary or item work.
- **The superseded Arc A–D structure docs and the retired `ch*.md` files** still contain appendix references and Arc labels. They were left out of scope on purpose, and QA greps must exclude them.
- **"the **The X** Event"** callouts in quest journals are the existing callout pattern, not an error.
- **Stat block names were capitalized** in the rank tables on pages 01–04 (for example `**Guards**`), a small departure from moving the text word for word.
- **Twelve NPCs are marked "Background figure; no scripted appearance".** Examples are Laraelra, Osco, Grevik, Tobrin, Senna Vael, Rella and Ivrala. They appear only in tavern staff tables and Renaer's Friends. The Tavern Time schedule now uses Laraelra and Torlyn on one scheduled night.

---

## Where to Start Next Session

Read this handoff, then CLAUDE.md, whose Workspace Structure now lists Notable Figures, Organizations, the Trollskull Manor guide and Running the Villains. The appendix work is finished, so wait for the user to name the next task. The likely candidates are converting Faction Outposts to a quest journal and drafting the Bestiary.

For any conversion:
1. Load `adventure-reloaded` first. It now includes the NPC Page and Organization Page specs.
2. Write and get approval for a quest plan.
3. Delegate the drafting to project agents and review their output yourself.

For Faction Outposts specifically, resolve the leftover dice in `arc-e-faction-outposts.md` against the fixed values already on the villain Organization pages.
