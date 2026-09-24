# CLAUDE.md

> **Start every session by finding and reading the most recent handoff file.** Glob for `session * handoff.md` in the root directory, identify the file with the highest N, and read it before doing anything else. It records completed work, standing decisions, outstanding tasks, and exactly where to pick up next. Do not re-derive or re-ask anything it already settles.

---

## Project Purpose

This is a campaign design workspace for remixing **Waterdeep: Dragon Heist** and **Dungeon of the Mad Mage** into a unified, improved campaign arc. The primary role here is creative brainstorming partner and DM assistant — generating heist structures, faction dynamics, NPC development, clue networks, and mechanical content.

Assume the DM owns both source books and is familiar with their contents. Do not summarize the originals unless asked. Focus on remix, improvement, and original design.

---

## Edition

All content must use **2024 D&D 5th Edition** rules and terminology. Never default to 2014 rules.

---

## Three Remix Pillars

All design decisions should serve these three goals:

**1 — Make It a Heist.** Dragon Heist should function as a true heist campaign. Each major faction lair (Gralhund Villa, Kolat Towers, Xanathar's Lair, Sea Maidens Faire, Cassalanter Villa, Vault of Dragons) is a potential heist target. Each should have: full adversary roster (scouteable and mappable by PCs), multiple entry points and approaches, dynamic occupant responses to intrusion, clear rewards and faction consequences.

**2 — Feature All Villains.** All four villain factions are simultaneously active and competing — Xanathar's Guild, the Zhentarim (Manshoon splinter), the Cassalanters, and the Bregan D'aerthe (Jarlaxle). No single "season villain." Each faction has a distinct agenda, personality, and method. Faction Response Teams patrol the city and react to PC actions. PC choices meaningfully shift the faction balance of power.

**3 — Fix-Up and Structural Robustness (Alexandrian Design Philosophy).** Three Clue Rule: every investigation beat has at least three independent paths to the same conclusion. Continuity Coherence: timeline inconsistencies restructured into a logical backstory. Player Motivation: PCs always have organic reasons to investigate or act. Agency Over Railroading: design situations, not scripts.

---

## Dragon Heist → Mad Mage Integration

Treat the two campaigns as a unified arc:
- Dragon Heist factions, NPCs, and items should echo into Undermountain (enemies may have agents below).
- The Vault of Dragons resolution (financial, political, reputational) shapes the descent.
- Halaster Blackcloak may be aware of or subtly interfering in Dragon Heist events.
- Thread a through-line (a pursuit, mystery, or lost NPC) that gives the Undermountain descent personal stakes rather than feeling like a tonal reset.

---

## Source Research

Before drafting any quest, chapter, or encounter, read **`sources/SOURCE_GUIDE.md`** to find which source files to consult. It maps every PDF and JSON to its contents, cross-references, and caveats, with a per-quest "When to consult" list. Never write content about a location, NPC, or investigation beat without first checking the source guide and reading the listed files.

Primary source files:
- **`sources/adventure-wdh.json`** — full original Dragon Heist adventure text (all chapters, keyed areas, appendices). Consult before writing any remix scene.
- **`sources/adventure-wdmm.json`** — full original Dungeon of the Mad Mage text. Consult only for integration seeds; Undermountain remix is future work.
- **`sources/1–30 *.pdf`** — the Alexandrian Remix PDFs. Use for structural design, clue architecture, and heist frameworks; never copy prose.
- **`sources/Other remix files/`** — Patreon NPC guides, villain combat notes, event supplements, and enhanced stat blocks. See the "Other Remix Files" section in `sources/SOURCE_GUIDE.md` for the full file enumeration, NPC focus, and when-to-consult notes.
- **`sources/Appendix_B_-_Player_Factions.md`**, **`sources/Appendix_C_-_Player_Faction_Missions.md`**, **`sources/Appendix_D_-_Running_the_Tavern.md`** — Alexandrian Remix appendices in markdown. Consult alongside `3. Player Character Factions.pdf` and `27. Addendum A Night in Trollskull Manor.pdf`.

Ember format reference files (document structure only — not adventure content):
- **`C:\Users\robert.lupu\Downloads\01 - Ember\01 - Ember\05 - Quests\03 - Chapter 1\001 - The Winding Trail\014 - Dusktide Rising.md`** — Combat event example: two-phase H3 structure, `> **[GM]** >` blockquotes, `### Concluding the Event` → attunements → `#### Next Steps` + `#### Milestone`, player zone at bottom.
- **`C:\Users\robert.lupu\Downloads\01 - Ember\01 - Ember\05 - Quests\03 - Chapter 1\003 - Ooze Control\001 - Overview.md`** — Quest overview example: GM blockquote header (Requirements / Difficulty / Milestone Overview H4s) and `## Overview` player-facing section.
- **`C:\Users\robert.lupu\Downloads\01 - Ember\01 - Ember\03 - Area Walkthroughs\04 - Arctus Plateau\006 - Arcturel Dives\014 - Arvoda's Elixirs.md`** — Keyed room example: opening-prose-no-heading pattern, H4 NPC sections, H3 event-conditional section with `Refer to the [Event Name] Event` callout.
- **`C:\Users\robert.lupu\Downloads\01 - Ember\01 - Ember\04 - Guides\001 - Players' Guide\020 - Milestone Progression.md`** — Milestone Points system reference: progression table (L1→L8 at 28 cumulative points), leveling rules, Main Quest vs Side Quest point awards.

---

## Workspace Structure

### Quest Journals (authoritative)

When a quest journal exists for a quest, it supersedes the structure doc. Use these files for all content decisions.

| Path | Status | Contents |
|---|---|---|
| `campaign/quests/act-i/finding-floon/` | Complete | Finding Floon — `overview.md`, `ev-01`–`ev-04`, `flowchart.md`, `design-notes.md`. QA'd (source-researcher + consistency-checker). |
| `campaign/quests/act-i/trollskull-alley/` | Complete | Trollskull Alley — `overview.md`, `ev-01`–`ev-07`, `flowchart.md`, `design-notes.md`. QA'd. |
| `campaign/quests/act-ii/fireball/` | Complete | Fireball! — `overview.md`, `ev-01`–`ev-07`, `flowchart.md`, `design-notes.md`. |
| `campaign/quests/act-ii/gralhund-villa/` | Complete | Gralhund Villa — `overview.md`, `ev-01`–`ev-09`, `flowchart.md`, `design-notes.md`. |
| `campaign/quests/faction-missions/` | Complete | All 43 faction missions (44 folders including BD-M2b optional) across 7 faction subdirectories. Each mission = `overview.md` + `ev-NN` file(s) + optional `design-notes.md`. No Milestone Points awarded. |

The Faction Outposts, Xanathar's Lair, Cassalanter Villa, Sea Maidens Faire, Kolat Towers, and Vault of Dragons quests are pending conversion. Their structure docs are authoritative until quest journals exist.

### Quest Structure Documents

**Superseded** (quest journal exists — do not use for content decisions):

| Path | Superseded by |
|---|---|
| `campaign/structure/arc-a-finding-floon.md` | `campaign/quests/act-i/finding-floon/` |
| `campaign/structure/arc-b-trollskull-alley.md` | `campaign/quests/act-i/trollskull-alley/` |
| `campaign/structure/arc-c-fireball.md` | `campaign/quests/act-ii/fireball/` |
| `campaign/structure/arc-d-gralhund-villa.md` | `campaign/quests/act-ii/gralhund-villa/` |

**Active** (pending conversion to quest journal):

| Path | Quest |
|---|---|
| `campaign/structure/arc-e-faction-outposts.md` | Faction Outposts |
| `campaign/structure/arc-f-xanathars-lair.md` | Xanathar's Lair |
| `campaign/structure/arc-g-cassalanter-villa.md` | Cassalanter Villa |
| `campaign/structure/arc-h-sea-maidens-faire.md` | Sea Maidens Faire |
| `campaign/structure/arc-i-kolat-towers.md` | Kolat Towers |
| `campaign/structure/arc-j-vault-of-dragons.md` | Vault of Dragons |

For detailed design summaries of Faction Outposts through Vault of Dragons (scene counts, mechanics, milestone notes), see **Quest Design Summaries** below.

### Location Journals

All locations are structuring drafts.

| Path | Status | Contents |
|---|---|---|
| `campaign/locations/gralhund-villa/` | Complete | `area-overview.md` + `g01`–`g19`. Full day/night adversary rosters; only NPC presence is state-conditional. |
| `campaign/locations/zhentarim-warehouse/` | Complete | `area-overview.md` + `z01`–`z05`. |
| `campaign/locations/xanathar-sewer-hideout/` | Complete | `area-overview.md` + `q01`–`q11`. |
| `campaign/locations/trollskull-manor/` | Complete | `area-overview.md` + `tm01`–`tm06`. |
| `campaign/locations/house-of-inspired-hands/` | Partial | `area-overview.md` + `01-main-hall.md`, `02-nims-attic.md`. |
| `campaign/locations/sea-maidens-faire/` | Partial | `area-overview.md` + `01`–`05` (Heartbreaker, Eyecatcher cabins, Scarlet Marpenoth). |
| `campaign/locations/cassalanter-villa/` | Partial | `area-overview.md` + `01`–`17` (12 villa rooms + 5 temple). |

### Campaign Guides

All guide files are structuring drafts; prose-writing pass deferred to final polish phase.

**Players' Guide** (`campaign/guides/players-guide/`)

| File | Contents |
|---|---|
| `about-this-campaign.md` | Three remix pillars, concept, who it suits |
| `character-creation.md` | General guidance, species notes, all XPHB + FRHoF backgrounds rated for Waterdeep fit |
| `debts-of-the-city.md` | All 8 Debts — flavor + "Your character knows" only; no Holder sections |
| `bonds-and-flaws.md` | Bonds table (d8) and Flaws table (d8); quest connections are GM-only |
| `faction-affiliations.md` | Faction preview table (all seven factions recruit in Trollskull Alley), Two Zhentarims note; player-safe renown basics |

**GM Guide** (`campaign/guides/gm-guide/`)

| File | Contents |
|---|---|
| `about-this-campaign.md` | Superset of player version; adds DM private notes on deaths, sympathetic villains, tone |
| `session-zero.md` | Full session zero script: campaign pitch, gold question, contract, safety tools |
| `debts-of-the-city.md` | Superset of player version; adds Holder guidance, Warning callouts, Design Note |
| `bonds-and-flaws.md` | Superset of player version; adds GM Notes table of where each Flaw lands in the campaign |
| `adventure-summary.md` | Four-act overview table, one paragraph per act, Milestone Points ladder |
| `structural-rules.md` | Two Zhentarims, faction response teams, campaign calendar (Ches 1 start, Ches 20 Grand Opening, Tarsakh 20, Flamerule 1 and 11), Three Clue Rule, fireball victim |
| `grand-game-in-play.md` | Between-sessions procedure: weekly faction check, faction state tracking, escalation pace, inter-faction conflict, when factions back down |
| `player-factions-overview.md` | Six standard factions + Bregan D'aerthe unique mechanic; conflicting loyalties overview; renown rules and faction-mission preamble |
| `running-the-villains.md` | Villain reference: Grand Game overview, MacGuffin chain, starting-knowledge table, escalation table (four tiers Unaware/Suspicious/Alert/Lockdown), inter-faction operations |
| `design-notes-running-the-campaign.md` | Macro design notes: simultaneous villains, heist framework, distributed Eyes, manor, fireball, Founders' Day, Jarlaxle's hidden identity, gold resolution, Aurinax; "Omitted NPCs" section |

**Trollskull Manor Guide** (`campaign/guides/trollskull-manor/`)

| File | Contents |
|---|---|
| `01-overview.md` | Intro, campaign calendar, Bigger Picture notes |
| `02-operating-costs.md` | Running costs, upkeep breakdown |
| `03-staff-and-hiring.md` | Staff tables, hiring rules |
| `04-fame.md` | Fame track and milestones |
| `05-revenue.md` | Revenue generation, d100 table |
| `06-tavern-time.md` | Procedure, Tenday Schedule, patron tables |
| `07-events.md` | Tavern event table |
| `08-notable-patrons.md` | Named patron profiles |
| `09-response-teams-at-the-tavern.md` | Faction response team rules at the manor |

The Bestiary (custom monster and boss stat blocks) is not yet drafted.

### Setting (`campaign/setting/`)

All setting files are structuring drafts.

| File | Contents |
|---|---|
| `waterdeep-lore.md` | Wards, governance, guilds, religion, festival calendar, dragonward |
| `history.md` | 8-era narrative history: Ahghairon through the players' arrival |
| `grand-game.md` | In-world Grand Game frame; faction starting knowledge table |
| `villains/xanathar.md` | 3 personality phases, relationships, goals, Sylgar note |
| `villains/manshoon.md` | 3 phases (incl. Simulacrum), relationships, goals, Two Zhentarims DM note |
| `villains/cassalanters.md` | 3 phases, relationships, goals, children timing note |
| `villains/jarlaxle.md` | Zardoz Zord phase + adversary/ally tracks, relationships, goals, entry and activation note |
| `notable-figures/` | 122 NPC pages in 15 group folders (trollskull-community, independents-allies, independents-adversaries, city-officials, harpers, lords-alliance, emerald-enclave, order-of-the-gauntlet, force-grey, doom-raiders, bregan-daerthe, xanathars-guild, manshoons-zhentarim, cassalanters, gralhunds). One page per NPC: H1, `> **[GM]**` Gamemaster's Summary, ## Roleplaying Information, ## Character Information, ## Overview. |
| `organizations/` | 10 faction pages: 01-harpers through 10-cassalanters. Each merges player-faction and villain-faction content from the former appendices. |

### Sources

| File | Contents |
|---|---|
| `sources/SOURCE_GUIDE.md` | Master map of every source file. **Read before writing any quest or encounter.** |
| `sources/Act_III_Arc_D.md` | Alexandrian Remix Arc D — villa area descriptions, day/night state, quinpartite confrontation |
| `sources/Act_III_Arc_E.md` | Alexandrian Remix Arc E — 903 lines; primary source for all faction outpost heists |
| `session N handoff.md` (root, highest N) | Running session log — read at session start |

Retired chapter files (superseded by guides and setting folders — do not use): `campaign/structure/ch1-beginning.md`, `campaign/structure/ch2-city-of-splendors.md`, `campaign/structure/ch3-running-the-campaign.md`.

---

## Quest Quick Reference

| Act | Quest | Core Activity |
|---|---|---|
| I | Finding Floon | Dock Ward investigation → Zhentarim warehouse → Xanathar sewer hideout |
| I | Trollskull Alley | Tavern home base, faction recruitment, city exploration, Twin Parades |
| II | Fireball! | Post-fireball investigation, nimblewright thread, House of Inspired Hands, Stone of Golorr acquired |
| II | Gralhund Villa | Quinpartite faction confrontation, recovery of the Stone |
| III | Faction Outposts | Intelligence-gathering heists at each faction's 2–3 outposts |
| III | Xanathar's Lair | Dungeon infiltration heist; Eye #1 |
| III | Cassalanter Villa | Social infiltration + temple dungeon heist; Eye #2; Founders' Day deadline |
| III | Sea Maidens Faire | Caper heist (or alliance path) aboard Jarlaxle's ships; Eye #3 |
| III | Kolat Towers | Raid on Manshoon's fortress; force field + extradimensional sanctum |
| IV | Vault of Dragons | Brandath Crypts approach, vault opening, Aurinax confrontation, 500,000 gp resolution |

---

## Quest Design Summaries

This section captures key design decisions from the active structure documents (Faction Outposts through Vault of Dragons). Update when structure docs change.

### Faction Outposts

Nine scenes: Stone attunement, faction consultation, structural guide, four faction outpost sections, response teams, aftermath/debriefs. 10 outposts across four factions (4 mini-heist, 6 encounter-plus). Baked-in escalation system; independent chain entry paths; Founders' Day clock; Manshoon name reveal. **1 Milestone Point**, for the first completed outpost chain (cumulative 10; does not reach Level 5 — see the heist-phase ladder in the four lair heists).

### Xanathar's Lair

Six scenes: Intelligence Briefing, Casing the Target, Preparation, The Operation, Complications and Escape, Aftermath. Panopticus surveillance mechanic; three entry methods; pre-set Xanathar location table; 15 keyed areas including Nihiloor's domain (X23–X27) with Splinter intel; Jarlaxle simultaneous heist (5-row interaction matrix); smokepowder demolition option; Stone of Golorr 1-Eye awakening (voice, impressions, agenda); variable difficulty by escalation tier; cross-quest clue pipeline to Cassalanter Villa, Sea Maidens Faire, and Kolat Towers. **Heist Milestone Points**: 4 per heist, order-agnostic — 1st heist → Level 5, 2nd → Level 6, all 4 → Level 7 (Kolat Towers is always one of the four, so Level 7 requires it). 4th–6th level.

### Cassalanter Villa

Six scenes (same structure as Xanathar's Lair). Social exposure system (4-stage: Accepted/Noticed/Suspected/Exposed); three entry methods (social invitation, guild blueprints, A9 stream); 17 keyed areas (12 villa + 5 temple); Esvele Rosznar parallel heist (5-row interaction matrix); four moral resolution paths (cooperative/contract destruction/sacrifice/exposure); named 16-person household staff with cult/non-cult status; Caladorn's ghost + mace of disruption; Stone of Golorr conditional 1-Eye or 2-Eye upgrade; Founders' Day deadline; outcome-branched faction debriefs (4 tracks); Three Clue Rule path to Kolat Towers. 4th–6th level.

### Sea Maidens Faire

Six scenes (same structure as Xanathar's Lair). Caper heist genre (three-beat: Something Goes Wrong → Escalation → Confrontation or Escape); three resolution paths (heist/alliance/patron); three entry methods (carnival cover, harbor approach via Zelifarn, supply delivery); 15 keyed areas (10 Eyecatcher + 5 Scarlet Marpenoth); Zardoz Betrayal Pitch (conditional on BD membership or prior Jarlaxle contact); Manshoon parallel strike (6-row interaction matrix, always fires); Zelifarn crystal ball moral thread; Stone of Golorr 3-scenario upgrade (order-agnostic, includes Full Awakening); Tarsakh 20 departure deadline; outcome-branched faction debriefs (5 BD states); Three Clue Rule paths to Cassalanter Villa, Xanathar's Lair, and Kolat Towers. 4th–6th level.

### Kolat Towers

Six scenes (same structure as Xanathar's Lair). Force-field + extradimensional sanctum structure; seven contacts; three entry methods; 13 keyed areas (E1–E13); Doom Raiders parallel actor (always fires, membership determines relationship); Manshoon location predecided by escalation tier (Unaware/Suspicious: E13; Alert/Lockdown: E12); simulacrum activation state linked to escalation; Samara's "North Ward" misdirection preserved as in-fiction intel error; intelligence haul in Scene 6 feeds Vault of Dragons directly; "Manshoon operational?" flag shapes Vault confrontation. Optional 4th heist slot and sole path to Level 7. 4th–6th level.

### Vault of Dragons

Six scenes: The Final Approach, The Brandath Crypts, The Ceremonial Opening, The Vault of Dragons, The Faction Confrontation, Aftermath. Convergence genre (not a heist). Faction-State Summary Table reads every flag set by the four lair heists; canonical Full Awakening scene; all seven player factions' Mission 6 payoffs; Brandath Crypts approach dungeon; ceremonial vault-opening ritual (dragonscale + sunlight + mithral hammer); Aurinax four resolution paths (oath-release, negotiation, legal argument, combat); two-wave faction confrontation (villain roster from flags, then unconditional Neverember arrival); optional NeverSword/Renaer duel; 500,000 gp logistics decision tree; five Mad Mage bridge hooks. **Milestone Points**: 3-heist entrants (Level 6) → Level 7 by Scene 6; 4-heist entrants (Level 7) → Level 8 (Undermountain handoff). 6th–7th level.

---

## Active Plan

**`C:\Users\robert.lupu\.claude\plans\that-s-pretty-much-what-tingly-summit.md`** — Ember-style modular document structure: one Journal Entry per quest (overview + event pages + design notes), separate Journal Entries per location cluster (area overview + keyed room pages), Milestone Points system replacing XP. Governs all new quest drafting going forward. `adventure-reloaded` skill updated to match.

---

## Skills Reference

All skill files live in `.claude/skills/`. Load a skill before performing its task — never work from memory for these.

| Skill | When to load |
|---|---|
| `adventure-reloaded` | **Load first for any campaign content task** — governs Ember-style modular format, GM/player zones, Milestone Points, cross-document callout syntax, quest openers, scene voice, NPC profile format, design notes philosophy. Load before drafting any quest journal, event file, location journal, keyed room, NPC profile, or design notes page. |
| `dnd-adventure-text` | Writing any adventure prose: encounter areas, read-aloud text, GM notes, treasure, traps |
| `foundry-journal` | Any formatted output — always load alongside `dnd-adventure-text` or `ttrpg-sourcebook-style`. Also governs sidebar/callout markup (`[!type]`) in all campaign `.md`, and the `md2html.py`/`assemble.py` scripts that convert a quest journal, location journal, guide, or setting folder to Foundry JSON |
| `ttrpg-sourcebook-style` | Lore, faction overviews, location descriptions, NPC profiles, setting prose |
| `ember-adventure-style` | Ember voice layer for adventure text — always load alongside `dnd-adventure-text` for events, quest overviews, keyed rooms, read-aloud, NPC dialogue, tactics, Summary |
| `ember-setting-style` | Ember voice layer for setting and GM guidance — always load alongside `ttrpg-sourcebook-style` for lore, organizations, Notable Figures, gazetteer entries, Players' Guide, GM Guide |
| `dnd-adventure-converter` | Converting existing 2014 adventure prose to 2024 rules |
| `dnd-monster-converter` | Converting an existing 2014 stat block to 2024 format |
| `dnd-monster-designer` | Designing a new 2024 stat block for a standard monster or minion |
| `boss-design` | Any named villain, BBEG, lieutenant, or multi-phase fight — always use over `dnd-monster-designer` |
| `cr2-encounter-builder` | All encounter balancing and evaluation |
| `humanize-prose` | Voice and rhythm pass on prose |
| `deslop-text` | AI pattern check — structural patterns (em-dashes, W2, metronomic sentences). Installed globally. |
| `no-ai-slop` | Complementary AI pattern check — binary contrasts, colon reveals, throat-clearing, importance puffery. Installed globally. Always run alongside `deslop-text`. |

---

## Handoff Protocol

**At session start:** Glob for `session * handoff.md` in the root directory, read the one with the highest N. Do not re-derive or re-ask anything it already settles.

**At session end** (only when the user invokes `/handoff` — never proactively): Write `session [N+1] handoff.md` in the root directory with these sections:

| Section | Contents |
|---|---|
| What Was Done | One-paragraph plain-English summary of the session's output |
| Changes Made | Table of files modified with a one-line description of what changed |
| Key Decisions | Each decision with: the decision itself, reasoning, and a verbatim user quote if one was given |
| Rules and Instructions | Standing rules established or reinforced this session (add to list, never overwrite) |
| Problems Solved | Bugs, prose violations, structural fixes caught and resolved |
| Outstanding Work | All unchecked checkboxes from previous handoff + new unfinished items |
| Warnings and Caveats | Cross-references or consistency risks that need checking later |
| Where to Start Next Session | Specific files, line numbers, and what to do when the user names the next task |

Carry all unchecked items from the previous handoff's Outstanding Work forward. Do not drop them.

**Git log range for Changes Made:** `git log <prev-handoff-commit>..HEAD`. Never use `--since` flags; same-day sessions bleed together.

---

## Standing Rules

### Design Principles

**Zero-prep design:** The guide is the DM's session prep. Every decision that could be made in the text must be made in the text — named NPCs, specific timings, predetermined outcomes. No "the DM decides" or "DM's choice" placeholders for anything the document can settle.

**Mission depth:** Faction missions must not reduce to a single skill check. Each mission needs multiple decision points, scene beats, or mechanical layers — social negotiation followed by an encounter, investigation that branches on player choices, a combat with a secondary objective, or a multi-stage resolution. A mission where the players roll once and the outcome is determined is not a mission, it is a wandering encounter. If the source mission is thin, expand it.

**Mini-arc mission structure:** Every faction mission follows: Hook → Background (DM-only context) → Act 1 → Act 2 → Act 3 → Renown Opportunities → Aftermath. Do not skip or reorder sections.

**Renown tier calibration:** L2–3 missions award 2 base renown; L4–5 missions award 3 base; L6–7 missions award 4 base. Bonus +1 renown is granted only for explicitly listed conditions in the Renown Opportunities section — not for general good play.

### Mechanics

**Boss design:** Any named villain, BBEG, lieutenant, or fight with phases always uses `boss-design`. Use `dnd-monster-designer` only for standard monsters and minions.

**Encounter math:** Always use `cr2-encounter-builder` (CR 2.0 system). Never use the DMG XP system.

**Milestone Points:** No XP is tracked. Each milestone-bearing Event awards 1 Milestone Point to the whole party (including absent players). Main Quests award ~2 points total; Side Quests award 1 point. The campaign ladder (Ember's table, L8 at 28): Finding Floon 2, Trollskull Alley 3, Fireball! 2, Gralhund Villa 2 (L4 at 9), Faction Outposts 1, each lair heist 4 (1st → L5, 2nd → L6, 4th → L7), Vault of Dragons 2 (3-heist parties end at L7, 4-heist parties at L8). Faction Missions award no Milestone Points — the main quest ladder (Finding Floon through Vault of Dragons) covers the full 1→8 progression without them; faction rewards are gold, renown, items, and cross-quest intel. Level-up is instant and party-wide when the cumulative threshold is reached — no Long Rest required. See the Milestone Points System section in `adventure-reloaded` for the full progression table and level-up rules.

### Writing Process

**Prose polish:** After generating any prose — read-aloud text, lore, GM notes, NPC descriptions — always run `deslop-text` and `no-ai-slop` together (they catch different patterns; run both), then `humanize-prose` (voice and rhythm pass). Run the full pipeline recursively until no violations remain. Deliver only the polished version. Quoted character dialogue is exempt from W-codes and empty-adverb rules — formal or idiosyncratic speech patterns inside quotation marks are intentional character voice.

**Output format:** All campaign documents go to `.md` source files. No HTML Artifacts are published until the full campaign structure is complete — meaning all quests, chapters, and guides have been drafted and reviewed. When the campaign structure is done, finished documents are delivered as HTML Artifacts that visually replicate how the content would look in a Foundry VTT journal. Load `foundry-journal` to understand the visual structure, then render it as an Artifact. Do NOT produce Foundry JSON — that step comes later.

**Plan before drafting:** Write and get a quest plan approved (via ExitPlanMode) before drafting any prose. Never write scene content without an approved plan. Use `.claude/plans/plan-arc-b-structure-valiant-pudding.md` as the format template for quest plans.

**Design Notes format:** Design Notes are a top-level `# Design Notes: [Quest Name]` section (H1), placed after all scene entries. They are never an H3 subsection inside Scenes. Finding Floon uses the older H3-inside-Sections pattern — do not replicate it for new quests.

**Quest Opener format:** The Quest Opener is backstory — it describes how the quest's situation came to exist, not what happens during the quest. It does not narrate faction consultations, chases, or confrontations that occur in the scenes. See the Gralhund Villa Opener as the corrected example.

**Order-agnostic Stone scenarios:** Stone of Golorr upgrade sections must frame upgrades around how many Eyes have been restored (first/second/third), never around which specific lair heist preceded. When two Eyes are restored, split into two sub-cases based on which prior lair heist ran first. Applies to every lair heist (Xanathar's Lair, Cassalanter Villa, Sea Maidens Faire) — do not condition upgrade text on a fixed quest ordering.

**Attunement format:** Entries in `### Concluding the Event` use `#### Flag Name: Condition` as the heading. Flags are binary (True/False only) — multi-state scenarios split into multiple flags. The body states what was recorded and names the specific downstream quest or event where the flag is read. No "Award X" language in the Concluding section — award language stays in the narrative body branches.

### Content Rules

**Finding Floon timeline:** The kidnapping of Floon happened "last night" (Alexandrian timeline), not "two nights ago" (WDH RAW). Use "last night" consistently across all Finding Floon content.

**Threestrings faction label:** Mattrim Mereg ("Threestrings") is a **Harper agent** embedded at the Yawning Portal. He is never "Doom Raiders" or "independent." This error has appeared twice across sessions — always verify NPC faction labels against Notable Figures, never against quest summaries.

**Scene-to-event mapping is not 1:1:** When planning a quest decomposition, evaluate each scene on its dramatic weight. One scene can become multiple events, or multiple scenes can collapse into one event. Don't assume one-scene-to-one-event.

**Structuring draft means structuring draft:** No content in this campaign is "prose-polished" in the final sense. The prose pipeline cleans up structural outlines; it does not replace the prose-writing pass. Never mark any file as "prose-polished" in CLAUDE.md.

**Members-only for briefs and debriefs:** Faction briefs and debriefs fire only for party members of that faction. Jarlaxle is the lone exception — his debrief fires for any party that dealt with him during the quest, regardless of BD membership.

**Players' Guide / GM Guide split:** Any content that exists in both guides must follow the superset rule — the player version is the safe-to-share subset; the GM version includes everything in the player version plus Holder guidance, Warning callouts, DM-private tone notes, and Design Notes. No content exists only in the player version.

**Quests, not arcs:** The campaign is organized as quests within Acts. Refer to quests by name (**Fireball!**, **Xanathar's Lair**); never write "Arc X" labels in new content. Structure-doc file names keep their `arc-*` slugs until each is converted to a quest journal.

**Escalation tiers:** Villain escalation uses four tiers only — Unaware, Suspicious, Alert, Lockdown (see **Running the Villains**).

### Process Rules

**Git commits:** Commit to git at the end of every turn in which files were changed. The commit message must explain *why* the changes were made — not just what changed. Reference the design decision or consistency issue that drove each edit. This preserves reasoning across context compaction, so future sessions can understand not just what is in the files but why it got there.

**Handoff delivery:** After committing the handoff, always push it, open a PR to master, and merge it in the same turn, so the next session's handoff glob finds it on master. A handoff left on a side branch gets missed (Session 30's did).

**Handoff timing:** Write the session handoff only after all deferred work is fully complete. Never write it mid-session and then continue working — this produces cleanup commits that pollute the git log. The handoff must be the last commit of every session.

**Agents do the work; resume them after rate limits:** The main session (Opus) is the orchestrator, not the worker; the agents (Sonnet 4.6) are the workers. Conversion, drafting, research, and polishing go to the project agents in `.claude/agents/`. Drafting goes to `prose-drafter`, which is pinned to Sonnet 4.6. Never draft with a `general-purpose` agent on the `sonnet` alias, because that alias resolves to the newest Sonnet, not 4.6. The main session plans, reviews, applies small review fixes, and commits. Writing content in the main session wastes Opus tokens. If an agent stops on a rate limit, the limit is account-wide: after it resets, continue that same agent with SendMessage. Never take its work over inline.

**Wait to be asked:** Never begin researching or writing the next section (faction, quest, guide) without an explicit user request. Complete the current task, then stop.

---

## Workflows

### Writing a new quest or campaign section

1. Load `adventure-reloaded` (document structure, quest openers, scene voice, callout taxonomy, NPC profile format, design notes philosophy)
2. Load `dnd-adventure-text` + `ember-adventure-style` + `foundry-journal` (scene-level prose, Ember voice, and visual formatting)
3. Draft as a Quest Journal — flat folder: `overview.md` → event files (`ev-NN-name.md` in order) → `flowchart.md` → `design-notes.md`
4. For keyed locations, draft a separate Location Journal: `area-overview.md` → room files (`[code]-[name].md`)
5. For NPC profiles: use the Resonance / Emotions / Motivations / Inspirations // Persona / Morale / Relationships format from `adventure-reloaded`
6. For monsters: `dnd-monster-designer` (standard) or `boss-design` (named villain)
7. For encounter balancing: `cr2-encounter-builder`
8. Run `deslop-text` + `no-ai-slop` → `humanize-prose` on all prose
9. Save to `.md` source file

### Writing a keyed location or encounter area

1. Load `dnd-adventure-text` + `ember-adventure-style` + `foundry-journal`
2. Write: setup paragraph → read-aloud → creature behavior → checks → treasure → development
3. For monsters: `dnd-monster-designer` (standard) or `boss-design` (named villain)
4. For encounter balancing: `cr2-encounter-builder`
5. Run `deslop-text` + `no-ai-slop` → `humanize-prose`
6. Save to `.md` source file

### Converting 2014 content to 2024

1. Load `dnd-adventure-converter` + `dnd-adventure-text` + `ember-adventure-style` + `foundry-journal`
2. Terminology pass → structural pass → action naming → monster renames
3. For embedded stat blocks: run through `dnd-monster-converter`, splice back in
4. Run `deslop-text` + `no-ai-slop` → `humanize-prose`
5. Save to `.md` source file

### Writing lore or sourcebook-style content

1. Load `ttrpg-sourcebook-style` + `ember-setting-style` + `foundry-journal`
2. Write following sourcebook conventions (consequence-layered facts, competing tensions, in-world closing quote)
3. Run `deslop-text` + `no-ai-slop` → `humanize-prose`
4. Save to `.md` source file

### Designing a boss or major villain

1. Load `boss-design` — never use `dnd-monster-designer` for a named villain
2. Load `cr2-encounter-builder` to calibrate the encounter
3. For support monsters: load `dnd-monster-designer`
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
