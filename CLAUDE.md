# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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

---

## Workspace Structure

| File / Folder | Contents |
|---|---|
| `campaign/structure/ch1-beginning.md` | Chapter 1 draft — Arc A (Finding Floon), session zero, opening scene |
| `campaign/structure/ch2-city-of-splendors.md` | Chapter 2 draft — Arc B (Trollskull Alley), city lore, faction recruitment |
| `campaign/structure/ch3-running-the-campaign.md` | Chapter 3 draft — structural rules: Three Clue Rule, heist framework, response teams, calendar |
| `campaign/structure/appendix-a-npc-roster.md` | Appendix A — full NPC roster for DM reference |
| `campaign/structure/appendix-c-player-factions.md` | Appendix C — player faction profiles and mission tables |
| `campaign/structure/appendix-d-running-factions.md` | Appendix D — faction-by-faction operations guide (in progress; write faction sections individually before delivering as Artifact) |
| `session 1 handoff.md` | Running log of completed work and where the current session left off — read at session start |

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

**`C:\Users\robert.lupu\.claude\plans\peppy-swinging-yao.md`** — Full campaign architecture plan: act/arc structure, appendix outlines, critical design decisions, implementation steps, and verification checklist.

> **Remove this section from CLAUDE.md once every part of the plan has been completed.**

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
| `deslop-text` | AI pattern check on prose — structural patterns (em-dashes, W2, metronomic sentences, etc.) |
| `no-ai-slop` | Complementary AI pattern check — binary contrasts, colon reveals, throat-clearing, importance puffery, weasel attribution, synonym cycling. Always run alongside deslop-text; they catch different things. Installed globally. |
| `adventure-reloaded` | Structural and writing guide for all campaign remix content — load before drafting any arc, chapter, scene, NPC profile, or design notes section |

---

## Handoff Protocol

**At session start:** Read the most recent `session N handoff.md` file (highest N in the root directory) before doing anything else. It contains outstanding work, key decisions already made, rules that override defaults, and a "Where to Start Next Session" section. Do not re-derive or re-ask anything the handoff file already settles.

**At session end** (or when the user signals they are done): Write a new handoff file named `session [N+1] handoff.md` in the root directory. Sections to include:

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

---

## Standing Rules (Always Apply — No Need to Ask)

**Zero-prep design:** The guide is the DM's session prep. Every decision that could be made in the text must be made in the text — named NPCs, specific timings, predetermined outcomes. No "the DM decides" or "DM's choice" placeholders for anything the document can settle. If a DM would have to make a creative decision at the table that the text could have made for them, that is a gap to fill, not a feature.

**Boss design:** Any named villain, BBEG, lieutenant, or fight with phases always uses `boss-design`. Use `dnd-monster-designer` only for standard monsters and minions.

**Encounter math:** Always use `cr2-encounter-builder` (CR 2.0 system). Never use the DMG XP system.

**Prose polish:** After generating any prose — read-aloud text, lore, GM notes, NPC descriptions — always run `deslop-text` and `no-ai-slop` together (they catch different patterns; run both), then `humanize-prose` (voice and rhythm pass). Deliver only the polished version.

**Output format:** Finished documents (completed arcs, chapters, standalone encounters) are delivered as an **HTML Artifact** that visually replicates how the content would look in a Foundry VTT journal. Load `foundry-journal` to understand the visual structure, then render it as an Artifact. Do NOT produce Foundry JSON — that step comes later. Structure drafts and appendices still being written faction-by-faction (like Appendix D) go directly into their `.md` source file — no artifact until the document is complete.

**Mission depth:** Faction missions must not reduce to a single skill check. Each mission needs multiple decision points, scene beats, or mechanical layers — social negotiation followed by an encounter, investigation that branches on player choices, a combat with a secondary objective, or a multi-stage resolution. A mission where the players roll once and the outcome is determined is not a mission, it is a wandering encounter. If the source mission is thin (one check, no scene structure), expand it.

**Git commits:** Commit to git at the end of every turn in which files were changed. The commit message must explain *why* the changes were made — not just what changed. Reference the design decision or consistency issue that drove each edit. This preserves reasoning across context compaction, so future sessions can understand not just what is in the files but why it got there.

---

## Workflows

### Writing a new arc, chapter, or campaign section

1. Load `adventure-reloaded` — this governs overall document structure, arc openers, scene voice, callout taxonomy, NPC profile format, and design notes philosophy
2. Load `dnd-adventure-text` + `foundry-journal` for scene-level prose and visual formatting
3. Draft the arc in order: Arc Opener → Scene Entries → Design Notes section (always last)
4. For NPC profiles: use the Resonance / Emotions / Motivations / Inspirations // Persona / Morale / Relationships format from `adventure-reloaded`
5. For monsters: load `dnd-monster-designer` (standard) or `boss-design` (named villain)
6. For encounter balancing: load `cr2-encounter-builder`
7. Run `deslop-text` + `no-ai-slop` → `humanize-prose` on all prose
8. Deliver as HTML Artifact

### Writing a new encounter area or keyed location

1. Load `dnd-adventure-text` + `foundry-journal`
2. Write the entry (setup paragraph → read-aloud → creature behavior → checks → treasure → development)
3. For any monsters: load `dnd-monster-designer` (standard) or `boss-design` (named villain/boss)
4. For encounter balancing: load `cr2-encounter-builder`
5. Run `deslop-text` + `no-ai-slop` → `humanize-prose` on all prose
6. Deliver as HTML Artifact mimicking Foundry journal layout

### Converting 2014 adventure content to 2024

1. Load `dnd-adventure-converter` + `dnd-adventure-text` + `foundry-journal`
2. Run the converter's full workflow: terminology pass → structural pass → action naming → monster renames
3. For any embedded full stat blocks: pull out, run through `dnd-monster-converter`, splice back in
4. Run `deslop-text` + `no-ai-slop` → `humanize-prose` on the final prose
5. Deliver as HTML Artifact

### Writing lore, faction overviews, or sourcebook-style content

1. Load `ttrpg-sourcebook-style` + `foundry-journal`
2. Write content following sourcebook conventions (consequence-layered facts, competing tensions, in-world closing quote)
3. Run `deslop-text` + `no-ai-slop` → `humanize-prose`
4. Deliver as HTML Artifact

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
