# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Purpose

This is a campaign design workspace for remixing **Waterdeep: Dragon Heist** and **Dungeon of the Mad Mage** into a unified, improved campaign arc. The primary role here is creative brainstorming partner and DM assistant — generating heist structures, faction dynamics, NPC development, clue networks, and mechanical content.

Assume the DM owns both source books and is familiar with their contents. Do not summarize the originals unless asked. Focus on remix, improvement, and original design.

---

## Edition: 2024 D&D 5e Only

All content must use **2024 D&D 5th Edition** rules and terminology. Never default to 2014 rules.

Key changes to apply consistently:

- **Species** (not "Race"). Half-Elves/Half-Orcs are not distinct species. Tieflings have Fiendish Legacies.
- **Ability Score Increases** come from Backgrounds, not Species.
- **Backgrounds** grant a Feat (Origin Feat), not a feature. New Backgrounds include Farmer, Guard, Scribe.
- **Exhaustion**: −2 penalty to all d20 rolls + 5 ft. speed reduction per level (max 6, then death). One level removed per Long Rest.
- **Heroic Inspiration** (not "Inspiration"): reroll any die, must take the new result, can be passed to another player.
- **Surprise**: only imposes Disadvantage on Initiative rolls.
- **Potions**: drinking or administering is a Bonus Action.
- **Weapon Mastery**: martial classes get mastery properties (Cleave, Slow, etc.) on specific weapons.
- **Spells**: only one spell slot per turn; Ritual spells castable by any prepared caster; Counterspell/Dispel Magic buffed; summoning spells use generic stat blocks; shapeshifting grants temp HP; Concentration save DC cap of 30; concentration spells can be ended freely.
- **Focus Points** (not "Ki Points") for Monks.
- **Truesight**: no longer reveals true forms of shapechangers.
- **Turn Undead**: buffed; no Turn Resistance/Defiance/Immunity.
- **Goblins** are Fey. **Gnolls** are Fiends.
- Nonmagical BPS resistance/immunity: removed from all stat blocks.
- "Bloodied" = at or below half HP.

When a concept exists in both editions, always use the 2024 version unless the user explicitly says otherwise.

---

## Monster Stat Block Format (2024)

When generating stat blocks, follow 2024 formatting conventions:

- **Initiative** listed with modifier and static score.
- Ability scores, modifiers, and saving throw bonuses in table format.
- Damage immunities and condition immunities grouped together.
- **Gear section** for notable carried items (weapons, armor, wands, spellbooks).
- **Habitat & Treasure** noted at the start of monster descriptions.
- Saving throw features written concisely:
  > *Shadow Breath (Recharge 5–6). Dexterity Saving Throw: DC 17, each creature within a 60-foot Cone. Failure: 35 (10d6) necrotic damage. Success: Half damage.*
- Reactions use explicit Trigger/Response structure:
  > *Parry. Trigger: The bandit is hit by a melee attack roll while holding a weapon. Response: The bandit adds 2 to its AC against that attack.*

---

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
| `deslop-text` | AI pattern check on prose |
| `adventure-reloaded` | Structural and writing guide for all campaign remix content — load before drafting any arc, chapter, scene, NPC profile, or design notes section |

---

## Standing Rules (Always Apply — No Need to Ask)

**Zero-prep design:** The guide is the DM's session prep. Every decision that could be made in the text must be made in the text — named NPCs, specific timings, predetermined outcomes. No "the DM decides" or "DM's choice" placeholders for anything the document can settle. If a DM would have to make a creative decision at the table that the text could have made for them, that is a gap to fill, not a feature.

**Boss design:** Any named villain, BBEG, lieutenant, or fight with phases always uses `boss-design`. Use `dnd-monster-designer` only for standard monsters and minions.

**Encounter math:** Always use `cr2-encounter-builder` (CR 2.0 system). Never use the DMG XP system.

**Prose polish:** After generating any prose — read-aloud text, lore, GM notes, NPC descriptions — always run `deslop-text` first (flag AI patterns, apply rewrites), then `humanize-prose` (voice and rhythm pass). Deliver only the polished version.

**Output format:** Finished documents (completed arcs, chapters, standalone encounters) are delivered as an **HTML Artifact** that visually replicates how the content would look in a Foundry VTT journal. Load `foundry-journal` to understand the visual structure, then render it as an Artifact. Do NOT produce Foundry JSON — that step comes later. Structure drafts and appendices still being written faction-by-faction (like Appendix D) go directly into their `.md` source file — no artifact until the document is complete.

---

## Workflows

### Writing a new arc, chapter, or campaign section

1. Load `adventure-reloaded` — this governs overall document structure, arc openers, scene voice, callout taxonomy, NPC profile format, and design notes philosophy
2. Load `dnd-adventure-text` + `foundry-journal` for scene-level prose and visual formatting
3. Draft the arc in order: Arc Opener → Scene Entries → Design Notes section (always last)
4. For NPC profiles: use the Resonance / Emotions / Motivations / Inspirations // Persona / Morale / Relationships format from `adventure-reloaded`
5. For monsters: load `dnd-monster-designer` (standard) or `boss-design` (named villain)
6. For encounter balancing: load `cr2-encounter-builder`
7. Run `deslop-text` → `humanize-prose` on all prose
8. Deliver as HTML Artifact

### Writing a new encounter area or keyed location

1. Load `dnd-adventure-text` + `foundry-journal`
2. Write the entry (setup paragraph → read-aloud → creature behavior → checks → treasure → development)
3. For any monsters: load `dnd-monster-designer` (standard) or `boss-design` (named villain/boss)
4. For encounter balancing: load `cr2-encounter-builder`
5. Run `deslop-text` → `humanize-prose` on all prose
6. Deliver as HTML Artifact mimicking Foundry journal layout

### Converting 2014 adventure content to 2024

1. Load `dnd-adventure-converter` + `dnd-adventure-text` + `foundry-journal`
2. Run the converter's full workflow: terminology pass → structural pass → action naming → monster renames
3. For any embedded full stat blocks: pull out, run through `dnd-monster-converter`, splice back in
4. Run `deslop-text` → `humanize-prose` on the final prose
5. Deliver as HTML Artifact

### Writing lore, faction overviews, or sourcebook-style content

1. Load `ttrpg-sourcebook-style` + `foundry-journal`
2. Write content following sourcebook conventions (consequence-layered facts, competing tensions, in-world closing quote)
3. Run `deslop-text` → `humanize-prose`
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
