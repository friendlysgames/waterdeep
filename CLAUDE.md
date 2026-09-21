# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> **Start every session by reading the most recent `session N handoff.md` in the root directory (highest N — currently `session 21 handoff.md`).** It records completed work, standing decisions, outstanding tasks, and exactly where to pick up next. Do not re-derive or re-ask anything it already settles.

---

## Project Purpose

This is a campaign design workspace for remixing **Waterdeep: Dragon Heist** and **Dungeon of the Mad Mage** into a unified, improved campaign arc. The primary role here is creative brainstorming partner and DM assistant — generating heist structures, faction dynamics, NPC development, clue networks, and mechanical content.

Assume the DM owns both source books and is familiar with their contents. Do not summarize the originals unless asked. Focus on remix, improvement, and original design.

---

## Edition: 2024 D&D 5e Only

All content must use **2024 D&D 5th Edition** rules and terminology. Never default to 2014 rules.

## The Three Remix Pillars

All design decisions should serve these three goals:

### 1 — Make It a Heist

Dragon Heist should function as a true heist campaign. Each major faction lair (Gralhund Villa, Kolat Towers, Xanathar's Lair, Sea Maidens Faire, Cassalanter Villa, Vault of Dragons) is a potential heist target. Each should have:
- Full adversary roster (scouteable and mappable by PCs)
- Multiple entry points and approaches
- Dynamic occupant responses to intrusion
- Clear rewards and faction consequences

### 2 — Feature All Villains

All four villain factions are simultaneously active and competing — **Xanathar's Guild**, **the Zhentarim** (Manshoon splinter), **the Cassalanters**, and **the Bregan D'aerthe** (Jarlaxle). No single "season villain." Key design elements:
- Each faction has a distinct agenda, personality, and method
- Faction Response Teams patrol the city and react to PC actions
- Faction outposts and safe houses scattered across Waterdeep's wards
- PC choices meaningfully shift the faction balance of power

### 3 — Fix-Up and Structural Robustness (Alexandrian Design Philosophy)

- **Three Clue Rule**: Every investigation beat (Nimblewright chain, Dalakhar's trail, Gralhund connection) has at least three independent paths to the same conclusion. No single failed roll should derail the campaign.
- **Continuity Coherence**: Timeline inconsistencies are restructured into a logical back story.
- **Player Motivation**: PCs always have organic reasons to investigate or act.
- **Agency Over Railroading**: Design situations, not scripts. Player choices drive consequences.

---

## Dragon Heist → Mad Mage Integration

Treat the two campaigns as a unified arc:

- Dragon Heist factions, NPCs, and items should echo into Undermountain (enemies may have agents below).
- The Vault of Dragons resolution (financial, political, reputational) shapes the descent.
- Halaster Blackcloak may be aware of or subtly interfering in Dragon Heist events.
- Thread a through-line (a pursuit, mystery, or lost NPC) that gives the Undermountain descent personal stakes rather than feeling like a tonal reset.

---

## Source Research

Before drafting any arc, chapter, appendix, or encounter, read **`sources/SOURCE_GUIDE.md`** to find which source files to consult. It maps every PDF and JSON to its contents, cross-references, and caveats, with a per-arc "When to consult" list. Never write content about a location, NPC, or investigation beat without first checking the source guide and reading the listed files.

Primary source files:
- **`sources/adventure-wdh.json`** — full original Dragon Heist adventure text (all chapters, keyed areas, appendices). Consult before writing any remix scene.
- **`sources/adventure-wdmm.json`** — full original Dungeon of the Mad Mage text. Consult only for integration seeds; Undermountain remix is future work.
- **`sources/1–30 *.pdf`** — the Alexandrian Remix PDFs. Use for structural design, clue architecture, and heist frameworks; never copy prose.
- **`sources/Other remix files/`** — Patreon NPC guides, villain combat notes, event supplements, and enhanced stat blocks. See the "Other Remix Files" section in `sources/SOURCE_GUIDE.md` for the full file enumeration, NPC focus, and when-to-consult notes.
- **`sources/Appendix_B_-_Player_Factions.md`**, **`sources/Appendix_C_-_Player_Faction_Missions.md`**, **`sources/Appendix_D_-_Running_the_Tavern.md`** — Alexandrian Remix appendices in markdown format; supplement the corresponding PDFs. Consult alongside `3. Player Character Factions.pdf` and `27. Addendum A Night in Trollskull Manor.pdf`.

Ember format reference files (for document structure, not adventure content):
- **`C:\Users\robert.lupu\Downloads\01 - Ember\01 - Ember\05 - Quests\03 - Chapter 1\001 - The Winding Trail\014 - Dusktide Rising.md`** — Combat event example. The most complete illustration of the event file format: two-phase H3 structure, selective `> **[GM]** >` blockquotes, `### Concluding the Event` → attunements → `#### Next Steps` + `#### Milestone`, and the player zone (`## Overview` / `## Read Aloud` / `## Summary`) at the bottom.
- **`C:\Users\robert.lupu\Downloads\01 - Ember\01 - Ember\05 - Quests\03 - Chapter 1\003 - Ooze Control\001 - Overview.md`** — Quest overview example. Reference for the GM blockquote header (Requirements / Difficulty / Milestone Overview H4s) and the `## Overview` player-facing section.
- **`C:\Users\robert.lupu\Downloads\01 - Ember\01 - Ember\03 - Area Walkthroughs\04 - Arctus Plateau\006 - Arcturel Dives\014 - Arvoda's Elixirs.md`** — Keyed room example. Reference for the opening-prose-no-heading pattern, H4 NPC sections, and the H3 event-conditional section with `Refer to the [Event Name] Event` callout.
- **`C:\Users\robert.lupu\Downloads\01 - Ember\01 - Ember\04 - Guides\001 - Players' Guide\020 - Milestone Progression.md`** — Milestone Points system reference. Canonical progression table (L1→L8 at 28 cumulative points), leveling rules, and Main Quest vs Side Quest point awards.

---

## Workspace Structure

| File / Folder | Contents |
|---|---|
| `campaign/structure/arc-a-finding-floon.md` | Arc A structure document — **RETIRED**; superseded by the modular files in `campaign/quests/act-i/finding-floon/`. Read only for historical reference; never use for content decisions. |
| `campaign/structure/arc-b-trollskull-alley.md` | Arc B structure document — reference only; superseded by the modular files in `campaign/quests/act-i/trollskull-alley/`. Do not use for content decisions. |
| `campaign/quests/act-i/trollskull-alley/` | Arc B Quest Journal — **complete and authoritative**: `overview.md`, `ev-01` through `ev-07`, `flowchart.md`, `design-notes.md`. QA'd. Structuring draft. |
| `campaign/structure/arc-c-fireball.md` | Arc C structure document — Fireball; six scenes (The Fireball, The Witnesses, The Nimblewright Hunt, The Sea Maidens Faire, The Cassalanter Dinner, Backtracking Dalakhar); three-phase investigation, Speak with Dead, Nim's CSL and sparrow trap, Valetta's reward, nine owner elimination montage, partial/complete ledger, BD sidebar (inverted renown), Cassalanter dinner as dedicated scene with four outcome tracks, optional Kalain branch (vault clues, death mark, four faction responses); 2 Milestone Points toward Level 4; structuring draft |
| `campaign/quests/act-i/fireball/` | Fireball Quest Journal — **complete**: `overview.md`, `ev-01` through `ev-07`, `flowchart.md`, `design-notes.md`. 7 events (blast and witnesses merged into ev-01). Structuring draft — not yet prose-polished. |
| `campaign/structure/arc-d-gralhund-villa.md` | Arc D structure document — **SUPERSEDED**; replaced by the modular files in `campaign/quests/act-i/gralhund-villa/` and `campaign/locations/gralhund-villa/`. Read only for historical reference; never use for content decisions. |
| `campaign/quests/act-i/gralhund-villa/` | Arc D Quest Journal — **complete**: `overview.md`, `ev-01` through `ev-09`, `flowchart.md`, `design-notes.md`. 9 events (day confrontation and night confrontation split; rooftop chase as ev-08; aftermath as ev-09). Structuring draft — not yet prose-polished. |
| `campaign/locations/gralhund-villa/` | Gralhund Villa Location Journal — **complete**: `area-overview.md` + `g01` through `g19`. Full day and night adversary rosters in area overview; all static room features written as always-present; only NPC presence is state-conditional. Structuring draft — not yet prose-polished. |
| `campaign/structure/arc-e-faction-outposts.md` | Arc E structure document — Faction Outposts; nine scenes (Stone attunement, faction consultation, structural guide, four faction outpost sections, response teams, aftermath/debriefs); 10 outposts across four factions (4 mini-heist, 6 encounter-plus); baked-in escalation system; independent chain entry paths; Founders' Day clock; Manshoon name reveal; 2 Milestone Points (does not by itself reach Level 5 — see the heist-phase milestone ladder in Arcs F–I); structuring draft |
| `campaign/structure/arc-f-xanathars-lair.md` | Arc F structure document — Xanathar's Lair; six scenes (Intelligence Briefing, Casing the Target, Preparation, The Operation, Complications and Escape, Aftermath); panopticus surveillance mechanic; three entry methods; pre-set Xanathar location table; 15 keyed areas including Nihiloor's domain (X23–X27) with Splinter intel; Jarlaxle simultaneous heist (5-row interaction matrix); smokepowder demolition option; Stone of Golorr 1-Eye awakening (voice, impressions, agenda); variable difficulty by escalation tier; cross-arc clue pipeline to Arcs G/H/I; heist arc Milestone Points (order-agnostic: 1st heist crosses to Level 5, 2nd to Level 6, all 4 to Level 7 — Kolat Towers is always one of the four, so Level 7 requires it); 4th-6th level; structuring draft |
| `campaign/structure/arc-g-cassalanter-villa.md` | Arc G structure document — Cassalanter Villa; six scenes (Intelligence Briefing, Casing the Target, Preparation, The Operation, Complications and Escape, Aftermath); social exposure system (4-stage: Accepted/Noticed/Suspected/Exposed); three entry methods (social invitation, guild blueprints, A9 stream); 17 keyed areas (12 villa + 5 temple); Esvele Rosznar parallel heist (5-row interaction matrix); four moral resolution paths (cooperative/contract destruction/sacrifice/exposure); named 16-person household staff with cult/non-cult status; Caladorn's ghost + mace of disruption; Stone of Golorr conditional 1-Eye or 2-Eye upgrade; variable difficulty by escalation tier; Founders' Day deadline; outcome-branched faction debriefs (4 tracks); Three Clue Rule path to Arc I (Cassalanter Report on Grand Game); heist arc Milestone Points (see Arc F for progression); 4th-6th level; structuring draft |
| `campaign/structure/arc-h-sea-maidens-faire.md` | Arc H structure document — Sea Maidens Faire; six scenes (Intelligence Briefing, Casing the Target, Preparation, The Operation, Complications and Escape, Aftermath); caper heist genre (three-beat improvisation: Something Goes Wrong → Escalation → Confrontation or Escape); three resolution paths (heist/alliance/patron); three entry methods (carnival cover, harbor approach via Zelifarn, supply delivery infiltration); 15 keyed areas (10 Eyecatcher + 5 Scarlet Marpenoth); Zardoz Betrayal Pitch (conditional on BD membership or prior Jarlaxle contact); Manshoon parallel strike (6-row interaction matrix, always fires); Zelifarn crystal ball moral thread; Stone of Golorr 3-scenario upgrade (order-agnostic, includes Full Awakening); variable difficulty by BD escalation tier; Tarsahk 20 departure deadline; outcome-branched faction debriefs (5 BD states); Three Clue Rule paths to Arcs G, F, and I; heist arc Milestone Points (see Arc F for progression); 4th-6th level; structuring draft |
| `campaign/structure/arc-i-kolat-towers.md` | Arc I structure document — Kolat Towers; six scenes (Intelligence Briefing, Casing the Target, Preparation, The Operation, Complications and Escape, Aftermath); force-field + extradimensional sanctum structure; seven contacts; three entry methods; 13 keyed areas (E1–E13 extradimensional sanctum); Doom Raiders parallel actor (always fires, membership determines relationship); Manshoon location predecided by escalation tier (Unaware/Suspicious: E13; Alert/Lockdown: E12); simulacrum activation state linked to escalation; Samara's "North Ward" misdirection preserved as in-fiction intel error; intelligence haul in Scene 6 feeds Arc J directly; "Manshoon operational?" flag shapes Vault confrontation; heist arc Milestone Points (see Arc F for progression) — the optional 4th heist slot and the sole path to Level 7; 4th-6th level; structuring draft |
| `campaign/structure/arc-j-vault-of-dragons.md` | Arc J structure document — Vault of Dragons, final campaign arc; six scenes (The Final Approach, The Brandath Crypts, The Ceremonial Opening, The Vault of Dragons, The Faction Confrontation, Aftermath); convergence genre (not a heist); Faction-State Summary Table reads every flag set by Arcs F–I; canonical Full Awakening scene resolving Arc F/G's deferrals; all seven player factions' Mission 6 payoffs; Brandath Crypts approach dungeon; ceremonial vault-opening ritual (dragonscale + sunlight + mithral hammer); Vault keyed areas culminating in Aurinax (four resolution paths: oath-release, negotiation, legal argument, combat); two-wave faction confrontation (villain roster built from faction flags, then Dagult Neverember's unconditional arrival); optional NeverSword/Renaer duel; 500,000 gp logistics decision tree; five Mad Mage bridge hooks; Arc J Milestone Points always advance one level — 3-heist entrants (Level 6) reach 7 by Scene 6, 4-heist entrants (Level 7, all heists incl. Kolat Towers) reach 8, the Undermountain handoff point; 6th-7th level; structuring draft |
| `campaign/structure/ch1-beginning.md` | Chapter 1 draft — DM onboarding and session zero guide: campaign pitch, three remix pillars, character creation, Debts of the City, Bonds/Flaws, faction previews. Structuring draft. |
| `campaign/structure/ch2-city-of-splendors.md` | Chapter 2 draft — City of Splendors reference: ward lore, governance, guilds, festival calendar, campaign history (8 eras), Grand Game overview, all four villain character documents (personality phases, relationships, goals). Structuring draft. |
| `campaign/structure/ch3-running-the-campaign.md` | Chapter 3 draft — structural rules: Three Clue Rule, heist framework, response teams, calendar |
| `campaign/structure/appendix-a-npc-roster.md` | Appendix A — complete NPC roster: 55 Tier 1–2 profiles, 38 Tier 3 profiles, 1 Tier 4 profile (Senna Vael), 25 tavern staff candidates. Structuring draft. |
| `campaign/structure/appendix-b-monster-compendium.md` | Appendix B — custom monster and boss stat blocks for the campaign. Not yet drafted. |
| `campaign/structure/appendix-c-player-factions.md` | Appendix C — player faction profiles and mission tables |
| `campaign/structure/appendix-d-running-factions.md` | Appendix D — faction-by-faction operations guide; all 7 factions assembled (2,312 lines). Authoritative version. |
| `campaign/structure/appendix-e-villain-factions.md` | Appendix E — villain faction operations guide; all four villain factions (Xanathar, Manshoon, Cassalanters, Bregan D'Aerthe), NPC rosters, outpost entries, response teams, revelation lists, escalation framework, inter-faction dynamics. Structuring draft (no sidebar callouts); Nihiloor's three-project breakdown written in full. |
| `campaign/structure/appendix-f-running-the-tavern.md` | Appendix F — Trollskull Manor mechanics: Operating Costs, Reputation/Fame track, Revenue, Tavern Time procedure, d20 Events table, Notable Patron Profiles (32 alley/city/faction NPCs), staff candidate tables (32 candidates across 6 role groups with interview tells and mechanics), Faction Response Teams, Grand Game integration. Structuring draft. |
| `sources/SOURCE_GUIDE.md` | Master map of every source file: filename, origin, contents summary, which arcs to consult it for, cross-references, and caveats. Read before writing any arc or appendix. |
| `sources/Act_III_Arc_D.md` | Alexandrian Remix source for Arc D (Gralhund Villa) — primary reference for villa area descriptions, day/night state, and the quinpartite confrontation. |
| `sources/Act_III_Arc_E.md` | Alexandrian Remix source for Arc E (Faction Outposts) — 903 lines; primary source for all faction outpost heists. Read before drafting Arc E. |
| Most recent `session N handoff.md` in root (highest N) | Running log of completed work, key decisions, and where to start next session — read at session start |
| `campaign/quests/act-i/finding-floon/` | Arc A Quest Journal — **complete and authoritative**: `overview.md`, `ev-01` through `ev-04`, `flowchart.md`, `design-notes.md`. QA'd (source-researcher + consistency-checker). Structuring draft. |
| `campaign/quests/` | Home for all arc content in Ember-style modular format (Quest Journal per arc: overview + event pages + design notes). Arc A is complete; remaining arcs pending conversion from `campaign/structure/arc-*.md`. |
| `campaign/locations/zhentarim-warehouse/` | Zhentarim Warehouse Location Journal — **complete**: `area-overview.md` + `z01` through `z05`. Structuring draft. |
| `campaign/locations/xanathar-sewer-hideout/` | Xanathar Sewer Hideout Location Journal — **complete**: `area-overview.md` + `q01` through `q11`. Structuring draft. |
| `campaign/locations/trollskull-manor/` | Trollskull Manor Location Journal — **complete**: `area-overview.md` + `tm01` through `tm06`. Structuring draft. |
| `campaign/locations/house-of-inspired-hands/` | House of Inspired Hands Location Journal — `area-overview.md` + `01-main-hall.md`, `02-nims-attic.md`. Structuring draft — not yet prose-polished. |
| `campaign/locations/sea-maidens-faire/` | Sea Maidens Faire Location Journal — `area-overview.md` + `01` through `05` (Heartbreaker main deck, Eyecatcher cabins, Scarlet Marpenoth). Structuring draft — not yet prose-polished. |
| `campaign/locations/cassalanter-villa/` | Cassalanter Villa Location Journal — `area-overview.md` + `01` through `17` (12 villa rooms + 5 temple). Structuring draft — not yet prose-polished. |
| `campaign/locations/` | Location Journals — one folder per location cluster (area overview + keyed room pages). Separate from the quest journals they serve. All locations at structuring draft stage. |

---

## Arc Quick Reference

| Arc | Name | Core Activity |
|---|---|---|
| A | Finding Floon | Dock Ward investigation → Zhentarim warehouse → Xanathar sewer hideout |
| B | Trollskull Alley | Tavern home base, faction recruitment, city exploration, Twin Parades |
| C | Fireball! | Post-fireball investigation, nimblewright thread, House of Inspired Hands, Stone of Golorr acquired |
| D | Gralhund Villa | Quinpartite faction confrontation, recovery of the Stone |
| E | Faction Outposts | Intelligence-gathering heists at each faction's 2–3 outposts |
| F | Xanathar's Lair | Dungeon infiltration heist; Eye #1 |
| G | Cassalanter Villa | Social infiltration + temple dungeon heist; Eye #2; Founders' Day deadline |
| H | Sea Maidens Faire | Caper heist (or alliance path) aboard Jarlaxle's ships; Eye #3 |
| I | Kolat Towers | Raid on Manshoon's fortress; force field + extradimensional sanctum |
| J | Vault of Dragons | Brandath Crypts approach, vault opening, Aurinax confrontation, 500,000 gp resolution |

---

## Active Plan

**`C:\Users\robert.lupu\.claude\plans\that-s-pretty-much-what-tingly-summit.md`** — Ember-style modular document structure: one Journal Entry per arc (overview + event pages + design notes), separate Journal Entries per location cluster (area overview + keyed room pages), Milestone Points system replacing XP. Governs all new arc drafting going forward. `adventure-reloaded` skill updated to match.

---

## Skills Reference

All skill files live in `.claude/skills/`. Load a skill before performing its task — never work from memory for these.

| Skill | When to load |
|-------|-------------|
| `dnd-adventure-text` | Writing any adventure prose: encounter areas, read-aloud text, GM notes, treasure, traps |
| `dnd-adventure-converter` | Converting existing 2014 adventure prose to 2024 rules |
| `dnd-monster-converter` | Converting an existing 2014 stat block to 2024 format |
| `dnd-monster-designer` | Designing a new 2024 stat block for a standard monster or minion |
| `boss-design` | Any named villain, BBEG, lieutenant, or multi-phase fight — always prefer over dnd-monster-designer |
| `cr2-encounter-builder` | All encounter balancing and evaluation |
| `ttrpg-sourcebook-style` | Lore, faction overviews, location descriptions, NPC profiles, setting prose |
| `foundry-journal` | Any formatted output — always load alongside dnd-adventure-text or ttrpg-sourcebook-style |
| `humanize-prose` | Voice and rhythm pass on prose |
| `deslop-text` | AI pattern check on prose — structural patterns (em-dashes, W2, metronomic sentences, etc.). Installed globally. |
| `no-ai-slop` | Complementary AI pattern check — binary contrasts, colon reveals, throat-clearing, importance puffery, weasel attribution, synonym cycling. Always run alongside deslop-text; they catch different things. Installed globally. |
| `adventure-reloaded` | Structural and writing guide for all campaign remix content — load before drafting any quest journal, event file, location journal, keyed room, NPC profile, or design notes page. Governs Ember-style modular format, GM/player zones, Milestone Points, and cross-document callout syntax. |

---

## Handoff Protocol

**At session start:** Read the most recent `session N handoff.md` file (highest N in the root directory) before doing anything else. It contains outstanding work, key decisions already made, rules that override defaults, and a "Where to Start Next Session" section. Do not re-derive or re-ask anything the handoff file already settles.

**At session end** (only when the user invokes `/handoff` — never proactively): Write a new handoff file named `session [N+1] handoff.md` in the root directory. Sections to include:

| Section | Contents |
|---|---|
| What Was Done | One-paragraph plain-English summary of the session's output |
| Changes Made | Table of files modified with a one-line description of what changed |
| Key Decisions | Each decision with: the decision itself, reasoning, and a verbatim user quote if one was given |
| Rules and Instructions | Any standing rules established or reinforced this session (add to this list, never overwrite) |
| Problems Solved | Bugs, prose violations, structural fixes caught and resolved |
| Outstanding Work | Unchecked checkboxes carried forward from the previous handoff, plus any new unfinished items |
| Warnings and Caveats | Cross-references or consistency risks that need checking later |
| Where to Start Next Session | Specific files, line numbers, and what to do when the user names the next task |

Carry all unchecked items from the previous handoff's Outstanding Work section into the new file. Do not drop them.

**Git log range for the Changes Made table:** Find the commit that wrote the previous handoff file and use it as the base — e.g. `git log <prev-handoff-commit>..HEAD`. Do not use `--since` flags; same-day sessions bleed together.

---

## Standing Rules (Always Apply — No Need to Ask)

**Zero-prep design:** The guide is the DM's session prep. Every decision that could be made in the text must be made in the text — named NPCs, specific timings, predetermined outcomes. No "the DM decides" or "DM's choice" placeholders for anything the document can settle. If a DM would have to make a creative decision at the table that the text could have made for them, that is a gap to fill, not a feature.

**Boss design:** Any named villain, BBEG, lieutenant, or fight with phases always uses `boss-design`. Use `dnd-monster-designer` only for standard monsters and minions.

**Encounter math:** Always use `cr2-encounter-builder` (CR 2.0 system). Never use the DMG XP system.

**Milestone Points:** The campaign uses Ember's Milestone Points system — no XP is tracked. Each milestone-bearing Event awards 1 Milestone Point to the whole party (including absent players). Main Quests award ~2 points total; Side Quests and Faction Missions award 1 point. Level-up is instant and party-wide when the cumulative threshold is reached — no Long Rest required. See the Milestone Points System section in `adventure-reloaded` for the full progression table and level-up rules.

**Prose polish:** After generating any prose — read-aloud text, lore, GM notes, NPC descriptions — always run `deslop-text` and `no-ai-slop` together (they catch different patterns; run both), then `humanize-prose` (voice and rhythm pass). Run the full pipeline recursively until no violations remain. Deliver only the polished version. Quoted character dialogue is exempt from W-codes and empty-adverb rules — formal or idiosyncratic speech patterns inside quotation marks are intentional character voice.

**Output format:** All campaign documents go to `.md` source files. **No HTML Artifacts are published until the full campaign structure is complete** — meaning all arcs, chapters, and appendices have been drafted and reviewed. When the campaign structure is done, finished documents are delivered as HTML Artifacts that visually replicate how the content would look in a Foundry VTT journal. Load `foundry-journal` to understand the visual structure, then render it as an Artifact. Do NOT produce Foundry JSON — that step comes later.

**Wait to be asked:** Never begin researching or writing the next section (faction, arc, appendix) without an explicit user request. Complete the current task, then stop.

**Mini-arc mission structure:** Every faction mission follows this sequence: Hook → Background (DM-only context) → Act 1 → Act 2 → Act 3 → Renown Opportunities → Aftermath. Do not skip or reorder sections.

**Renown tier calibration:** L2–3 missions award 2 base renown; L4–5 missions award 3 base; L6–7 missions award 4 base. Bonus +1 renown is granted only for explicitly listed conditions in the Renown Opportunities section — not for general good play.

**Mission depth:** Faction missions must not reduce to a single skill check. Each mission needs multiple decision points, scene beats, or mechanical layers — social negotiation followed by an encounter, investigation that branches on player choices, a combat with a secondary objective, or a multi-stage resolution. A mission where the players roll once and the outcome is determined is not a mission, it is a wandering encounter. If the source mission is thin (one check, no scene structure), expand it.

**Git commits:** Commit to git at the end of every turn in which files were changed. The commit message must explain *why* the changes were made — not just what changed. Reference the design decision or consistency issue that drove each edit. This preserves reasoning across context compaction, so future sessions can understand not just what is in the files but why it got there.

**Handoff timing:** Write the session handoff only after all deferred work is fully complete. Never write it mid-session and then continue working — this produces cleanup commits (deleting and re-writing the handoff) that pollute the git log. The handoff must be the last commit of every session.

**Plan before drafting:** Write and get an arc plan approved (via ExitPlanMode) before drafting any prose. Never write scene content without an approved plan. Use `.claude/plans/plan-arc-b-structure-valiant-pudding.md` as the format template for arc plans — not the master campaign plan (`peppy-swinging-yao.md`).

**Design Notes format:** Design Notes are a top-level `# Design Notes: [Arc Name]` section (H1), placed after all scene entries. They are never an H3 subsection inside Scenes. Arc A uses the older H3-inside-Sections pattern — do not replicate it for new arcs.

**Arc Opener format:** The Arc Opener is backstory — it describes how the arc's situation came to exist, not what happens during the arc. It does not narrate faction consultations, chases, or confrontations that occur in the scenes. See the Arc D Opener as the corrected example.

**Order-agnostic Stone scenarios:** Stone of Golorr upgrade sections must frame upgrades around how many Eyes have been restored (first/second/third), never around which specific arc preceded. When two Eyes are restored, split into two sub-cases based on which prior lair arc ran first, each pointing to the correct remaining impression. Applies to every lair arc (F, G, H) — do not condition upgrade text on a fixed arc ordering.

**Arc A timeline:** The kidnapping of Floon happened "last night" (Alexandrian timeline), not "two nights ago" (WDH RAW). Use "last night" consistently across all Arc A content.

**Threestrings faction label:** Mattrim Mereg ("Threestrings") is a **Harper agent** embedded at the Yawning Portal. He is never "Doom Raiders" or "independent." This error has appeared twice across sessions — always verify NPC faction labels against Appendix A, never against arc summaries.

**Scene-to-event mapping is not 1:1:** When planning an arc decomposition, evaluate each scene on its dramatic weight. One scene can become multiple events, or multiple scenes can collapse into one event. Don't assume one-scene-to-one-event.

**Attunement format:** Entries in `### Concluding the Event` use `#### Flag Name: Condition` as the heading. The body states what was recorded and names the specific downstream arc or event where the flag is read. No "Award X" language in the Concluding section — award language stays in the narrative body branches. Arc A attunement entries are the reference.

---

## Workflows

### Writing a new arc, chapter, or campaign section

1. Load `adventure-reloaded` — this governs overall document structure, arc openers, scene voice, callout taxonomy, NPC profile format, and design notes philosophy
2. Load `dnd-adventure-text` + `foundry-journal` for scene-level prose and visual formatting
3. Draft the arc as a Quest Journal — flat folder, all files = pages: `overview.md` → event files (`ev-NN-name.md` in order) → `flowchart.md` → `design-notes.md`. For each keyed location, draft a separate Location Journal folder: `area-overview.md` → room files (`[code]-[name].md`). See `adventure-reloaded` for all file-type format specs.
4. For NPC profiles: use the Resonance / Emotions / Motivations / Inspirations // Persona / Morale / Relationships format from `adventure-reloaded`
5. For monsters: load `dnd-monster-designer` (standard) or `boss-design` (named villain)
6. For encounter balancing: load `cr2-encounter-builder`
7. Run `deslop-text` + `no-ai-slop` → `humanize-prose` on all prose
8. Save to `.md` source file (HTML Artifact delivery is deferred — see Output Format in Standing Rules)

### Writing a new encounter area or keyed location

1. Load `dnd-adventure-text` + `foundry-journal`
2. Write the entry (setup paragraph → read-aloud → creature behavior → checks → treasure → development)
3. For any monsters: load `dnd-monster-designer` (standard) or `boss-design` (named villain/boss)
4. For encounter balancing: load `cr2-encounter-builder`
5. Run `deslop-text` + `no-ai-slop` → `humanize-prose` on all prose
6. Save to `.md` source file (HTML Artifact delivery is deferred — see Output Format in Standing Rules)

### Converting 2014 adventure content to 2024

1. Load `dnd-adventure-converter` + `dnd-adventure-text` + `foundry-journal`
2. Run the converter's full workflow: terminology pass → structural pass → action naming → monster renames
3. For any embedded full stat blocks: pull out, run through `dnd-monster-converter`, splice back in
4. Run `deslop-text` + `no-ai-slop` → `humanize-prose` on the final prose
5. Save to `.md` source file (HTML Artifact delivery is deferred — see Output Format in Standing Rules)

### Writing lore, faction overviews, or sourcebook-style content

1. Load `ttrpg-sourcebook-style` + `foundry-journal`
2. Write content following sourcebook conventions (consequence-layered facts, competing tensions, in-world closing quote)
3. Run `deslop-text` + `no-ai-slop` → `humanize-prose`
4. Save to `.md` source file (HTML Artifact delivery is deferred — see Output Format in Standing Rules)

### Designing a boss or major villain

1. Always load `boss-design` — never use `dnd-monster-designer` for a named villain
2. Load `cr2-encounter-builder` to calibrate the encounter
3. For support monsters in the same fight: load `dnd-monster-designer`
4. Present: concept + archetype table → the Tell → shared stats → phase stat blocks → CR math → running notes

### Balancing or evaluating an encounter

1. Load `cr2-encounter-builder`
2. Calculate Party Power from the level table
3. Look up Monster Power using the tier-adjusted table (never the flat table)
4. Show: Party Power total → Encounter Power Budget → monster Power breakdown → difficulty verdict (% HP lost) → Day Cost

---

## Output Style

- **Actionable:** Bullet points, numbered lists, or focused paragraphs easy to use at the table.
- **Practical:** Mechanical implications stated alongside creative ideas.
- **Iterative:** Build on previously established remix decisions within the conversation. Track and respect prior choices.
- **Clarify when needed:** If a request is unclear or too broad, ask one focused clarifying question before proceeding.
- Flavor prose only when explicitly requested.
