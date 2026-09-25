---
name: adventure-reloaded
description: >
  Governs the structure, voice, and design philosophy for writing the Waterdeep Campaign Remix.
  Defines the Ember-style modular document format: Quest Journals (one per quest) and Location
  Journals (one per location cluster), each containing discrete pages (overview, event files,
  keyed rooms, design notes). Documents Ember's six block types (readaloud, gamemaster, social,
  qna, exploration, hazard) and their shorthand markdown syntax, the Milestone Points progression
  system, and the cross-document callout syntax. Load before drafting any quest journal, event
  file, location journal, keyed room, NPC profile, or design notes page.
---

# Adventure Reloaded — Campaign Writing Guide

This skill governs how the Waterdeep Campaign Remix is structured and written.

---

## Document Architecture

The campaign is organized around **narratives**, not locations.

```
Campaign
├── Chapter 1 — Beginning the Campaign  (session zero, character creation)
├── Setting Compendium                  (reference material: lore, NPCs, factions, organizations)
├── Chapter 3 — Running the Campaign    (adventure summary, structural rules, pacing)
├── Act I
│   ├── Finding Floon                   (each quest = one Quest Journal folder)
│   │   ├── overview.md                 (Quest Overview page)
│   │   ├── flowchart.md                (event sequence page)
│   │   ├── ev-01-yawning-portal.md     (Event pages, flat — no subfolder)
│   │   ├── ev-02-dock-ward.md
│   │   ├── ev-03-zhentarim-warehouse.md
│   │   ├── ev-04-xanathar-sewer.md
│   │   └── design-notes.md             (Design Notes page)
│   └── [Quest Name]
│       └── ...
└── Act II
    └── ...

Locations (separate from quest journals):
├── zhentarim-warehouse/                (each location = a Location Journal folder)
│   ├── area-overview.md
│   ├── z01-main-room.md
│   └── ... z12
└── xanathars-lair/
    ├── area-overview.md
    └── x01 ... x35
```

**Folder = one Foundry Journal Entry.** File = one Page within that journal. Quest journals and location journals are separate entries — a location folder never lives inside a quest folder.

**Acts** bundle quests with similar stakes or settings.

**Quests** are complete narrative units with a dramatic question and a clear goal.

**Events** are discrete moments within a quest — a confrontation, a discovery, a choice, a combat phase.

---

## Foundry Journal Model

Each markdown folder maps to one Foundry Journal Entry (one item in the sidebar). Each `.md` file within that folder becomes one Page within that journal.

- **Quest Journal** (`campaign/quests/act-i/finding-floon/`) — contains the overview, flowchart, all event pages, and design notes for one quest. Files are flat siblings — no events/ subfolder.
- **Location Journal** (`campaign/locations/zhentarim-warehouse/`) — contains the area overview and all keyed room pages for one location cluster. Separate from the quest that primarily uses it.

Content in these pages is structured using Ember's six **block types**. Each block is a blockquote in markdown, rendered by the converter (`md2html.py`) as a coloured `<section class="block …">` element. See the **Block Types** and **Shorthand Syntax** sections below.

Permission gating in Foundry is at the **page level**. `[!gamemaster]` blocks are the visual marker for GM-only content within a page; page-level permissions in Foundry control what players actually see.

---

## Block Types

Six block types cover all content in this campaign. No others are used — not `[!narrative]`, `[!npc-narrative]`, `[!dialogue]`, `[!profile]`, `[!design]`, `[!lore]`, `[!info]`, `[!warning]`, `[!combat]`, or `> **[GM]**` zones.

| Block | Colour | What it holds |
|---|---|---|
| `readaloud` | parchment | Narration spoken to the players. Second person ("you"), present tense, only what the characters perceive. NPC speech sits as nested `> >` blockquotes inside the block. A conditional readaloud is introduced in GM prose: "If X, read or paraphrase the following:". Length fits the moment — two sentences for a door, many paragraphs for a campfire legend. Never GM notes, summary, or backstory. |
| `gamemaster` | dark | Every GM-only note. At the top of each event: the **Gamemaster's Summary** ("This [Social/Exploration/Combat] Event occurs when… In this Event, the party can/must:" + bullets), with extra H4 subsections as needed (e.g. `#### Combat Phases`, `#### Matters of Punctuality`). Inline in scenes: Active Ally, Applying Pressure, hidden identity, Music, and so on. At the end: **Event Outcomes** (if any), **Next Steps**, **Milestone** (as an H4 inside **Next Steps**). |
| `social` | blue | An NPC encounter. The title is an epithet: "The Charming Caravanner", "Conversation with Emelyn". Optional first body line: `Name (Alignment, Ancestry, pronouns) :: one-line summary` — renders as Ember's NPC header. Then: personality and behaviour; "Conversation topics X is willing to discuss include:" + a bulleted list; Insight and other checks and what they reveal. GM-facing. |
| `qna` | purple | One topic the players raise. The question is terse: "Your trade?", "About Helkas?". The answer is read to the players: an optional narration beat, then the NPC's quoted words in a nested `> >` blockquote. A run of `[!qna]` blocks follows a `[!social]` block. |
| `exploration` | green | Titled. Checks and what they reveal: "Any character who makes a successful DC N Skill check knows…". Complex-check list items use `- **Auto:**`, `- **Critical:**`, `- **Advantage:**`, `- **Disadvantage:**` markers. Found items; perceived text as a nested `> >` blockquote. |
| `hazard` | red | Combat and danger: creature organisation, per-creature Tactics ("At the start of combat… Over the course of combat… prioritize… The battle ends when…"), ally tactics, Dramatic Moments, traps, ambush rules, area effects. |

**Attunement blocks** are Ember's character progression mechanic. This campaign does not use them.

---

## Shorthand Syntax

The converter (`.claude/skills/foundry-journal/scripts/md2html.py`) renders this syntax as Ember's `<section class="block …">`. Each block is a blockquote whose first line is `> [!type]`, optionally followed by `**Title**`:

| Shorthand | Notes |
|---|---|
| `> [!readaloud]` | No title. |
| `> [!gamemaster]**Title**` | Further `#### Sub` lines inside become additional H4 subsections. |
| `> [!qna]**Your trade?**` | The terse question is the title. |
| `> [!social]**The Old Wolf**` | Epithet as title. Optional first body line `Name (Alignment, Ancestry, pronouns) :: one-line summary` renders as Ember's NPC header. |
| `> [!exploration]**Title**` | Block title. List items starting `- **Auto:**` / `- **Critical:**` / `- **Advantage:**` / `- **Disadvantage:**` render as complex-check lines. |
| `> [!hazard]**Title**` | Block title. |

Other rules:
- Nested NPC speech inside a block is `> >`.
- Blocks sit at top level, never nested inside another block.
- Leave a blank line between blocks and between a block and surrounding prose.
- There are no other block types. The old types still render as a fallback in the converter, but new and converted text never uses them.
- Design rationale goes on the quest's `design-notes.md` page, not in an event.

---

## File Type Specifications

### 1. Quest Overview (`overview.md`)

The landing page for the quest journal. Opens with a `[!gamemaster]` block, followed by GM-facing backstory prose and sections, then a player-safe `## Overview` at the bottom.

```markdown
# [Quest Name]: [Descriptive Title]

> [!gamemaster]
>
> #### Requirements
> [Entry conditions; what quests or outcomes must precede this one]
>
> #### Difficulty
> *An adventure for X–Y level characters.*
>
> #### Milestone Progression
> [Total Milestone Points this quest awards; which events bear a milestone]

[GM backstory paragraphs. Present tense for ongoing situation; past tense for how it came to be.]

## Involved Characters
- **[NPC Name]** ([faction]) — [one-line role in this quest]

## Dangers & Enemies
[Adversary roster summary — key factions and named opponents active in this quest]

## Overview
[2–4 sentences, player-safe. The quest's premise and shape, not its resolution.]
```

### 2. Event File (`ev-NN-event-name.md`)

One file per scene beat. File naming: zero-padded `ev-` prefix. Example: `ev-01-yawning-portal.md`.

```markdown
# [Event Name]

> [!gamemaster]**Gamemaster's Summary**
>
> This [Exploration/Combat/Social] Event occurs when [trigger condition]. In this Event, the party can:
>
> - [Bullet: what can happen — 3–6 items]
>
> [Optional H4 subsections: #### Combat Phases, #### Matters of Punctuality, etc.]

### [Scene Name]

[1–3 sentences of GM framing — present tense, what is happening when the scene begins.]

> [!readaloud]
> [Opening narration. Second person, present tense, only what the characters perceive.
> NPC speech as nested > > blockquotes. Length fits the moment; end on something unresolved.]

[Follow-up GM prose, if needed. Keep it short — the content lives in the blocks.]

> [!social]**[Epithet]**
>
> [NPC Name] ([Alignment], [Ancestry], [pronouns]) :: [one-line summary]
>
> [Personality and behaviour.]
>
> Conversation topics [Name] is willing to discuss include:
> - [Topic]
>
> Any character who makes a successful DC N [Skill] check [reveals X].

> [!qna]**[Terse question]**
>
> [Optional narration beat.]
>
> > [NPC's answer in quoted speech.]

> [!exploration]**[Title]**
>
> Any character who makes a successful DC N [Skill] check knows [X].
>
> - **Critical:** [Additional detail on a critical success.]

> [!hazard]**[Title]**
>
> [Creature organisation. Then:]
>
> #### [Creature] Tactics
> At the start of combat, [creature] will [action].
>
> Over the course of combat, [creature] will prioritize:
> - [Action or ability]
>
> The battle ends when [condition].

### Concluding the Event

[1–3 sentences of GM prose wrapping up the scene.]

> [!gamemaster]**Event Outcomes**
>
> Mark each outcome that occurs. Later events read them.
>
> - **[Outcome Name]** — mark when [condition]. Read by **[Later Event]** [and Mission N].

> [!gamemaster]**Next Steps**
>
> [Named callout to the following event. Conditional: "If X occurred, proceed to the
> **[Event Name]** Event. If Y, proceed to **[Event Name]**."]
>
> #### Milestone: [Event Name]
>
> Completing this Event awards 1 Milestone Point. [Optional: level note.]

## Overview

[One sentence — the player-facing summary of what this event is about. "At a Glance" text.]

## Summary

[Quest log entry. 1–4 sentences, first-person plural ("We traveled…", "We met…"). What the party remembers.]
```

**Scene heading hierarchy:**
- `###` H3 = major narrative phase or branching condition (`### Drake Assault`, `### If the PCs Arrive at Night`)
- `####` H4 = named subsection inside a `[!gamemaster]` block (`#### Combat Phases`, `#### Active Ally`, `#### Applying Pressure`, `#### Milestone: …`)
- `> [!readaloud]` = narration block (every passage the GM reads aloud, including conditional variants introduced in GM prose)
- `> [!social]` + run of `> [!qna]` = NPC encounter and its topics
- `> [!exploration]` = check-based discovery
- `> [!hazard]` = combat, trap, or danger

**Event Outcomes** replace the old binary attunement flags. An outcome name like "Davil Arrested" or "BD Contact Severed" is a named result the GM marks during play. Later events check it with: "If the party marked **BD Contact Severed**…". Keep exact names consistent across all files that reference the same outcome.

**No `## Read Aloud` section.** The `[!readaloud]` blocks sit in the scene body at the moment they happen. The `## Overview` section's player-facing text is the "At a Glance" summary visible in the Codex. The `## Summary` section is the Journal Summary recorded on completion.

### 3. Area Overview (`area-overview.md`)

First page of every Location Journal. Covers all persistent location features.

```markdown
# [Location Name] — Area Overview

> [!gamemaster]**Area Map Context**
>
> [Which events use this location. Where the party enters per event. Any map-layer notes.]

## Gameplay Details

The areas of [location] have the following features unless noted otherwise.

### Levels & Elevation
[Description]

### Illumination
[Description]

### Terrain
[Description]

### Inhabitants
[Base inhabitants.]

During the **[Event Name]** Event, the following also inhabit the area:
- [NPC or creature]

### Enemies
[Base state — "None" if the area is not always hostile.]

During the **[Event Name]** Event, the following enemies are present:
- [Creature]

### [Named Location-Wide Mechanic]

[Prose description.]

> [!hazard]**[Mechanic Name]**
>
> [Rules for the mechanic — triggers, effects, resolution.]
```

### 4. Keyed Room (`[code]-[room-name].md`)

One file per keyed area entry. File naming: lowercase, zero-padded area code, hyphenated room name. Examples: `z01-main-room.md`, `g16-master-bedroom.md`, `x23-nihiloors-lair.md`.

```markdown
# [Area Code] — [Room Name]

> [!readaloud]
> [Opening narration. No heading precedes this block — it is the first element of the page.
> Second person, present tense. 2–4 sentences of what the PCs perceive on entry. NPC
> greeting as a nested > > blockquote if one is present.]

[One GM sentence of context — what is happening, who is here, what changes.]

> [!social]**[Epithet]**
>
> [NPC Name] ([Alignment], [Ancestry], [pronouns]) :: [one-line summary]
>
> [Personality and behaviour. Topics list. Checks.]

> [!qna]**[Terse question]**
>
> > [NPC's answer.]

> [!exploration]**[Title]**
>
> [Check and what it reveals.]

> [!hazard]**[Title]**
>
> [Danger, trap, or encounter mechanics.]

### [Event Name] — Event-Conditional Section

[Content that only applies during a specific event. Close with:
"Refer to the **[Event Name]** Event for full details."]
```

### 5. Design Notes (`design-notes.md`)

Last page in every Quest Journal. Contains all design rationale for the quest.

```markdown
# Design Notes: [Quest Name]

## [Thematic Category]

***[Element Name].*** [Design note prose — what was wrong, what replaced it,
what it accomplishes, what future payoffs it plants.]
```

### 6. Flowchart (`flowchart.md`)

Second page in the Quest Journal (after overview). Text diagram of the event sequence and its branches. Placeholder for now; becomes a Mermaid diagram in the HTML Artifact pass.

```markdown
# [Quest Name] — Event Flowchart

Start → **Event 01 — [Name]** → branches:
  A: [condition] → **Event 02 — [Name]**
  B: [condition] → **Event 03 — [Name]**
         └── → **Event 04 — [Name]** (shared exit)
```

### 7. NPC Page (`campaign/setting/notable-figures/[group]/NN-name.md`)

One file per named NPC in the Notable Figures setting compendium. File naming: zero-padded `NN-` prefix, lowercase hyphenated name without quotes or apostrophes.

```markdown
# [NPC Name]

> [!gamemaster]**Gamemaster's Summary**
>
> - *[species occupation, alignment — from source subtitle]*. Stat block: **[stat block]**.
> - **Affiliation:** [group name; for secret affiliations state both, e.g. "Xanathar's Guild (secretly Harpers)"]
> - **Featured in:** [bold quest/location names, comma-separated in campaign order]

## Roleplaying Information

[Resonance, Emotions, Motivations, Inspirations paragraphs — VERBATIM from source]

## Character Information

[Persona, Morale, Relationships paragraphs — VERBATIM from source]

## Overview

[NEW: 1–2 sentences, player-safe. What the party would know or observe on first meeting.
No secrets, no hidden allegiances, no stat info.]
```

**Verbatim rule:** Copy profile text character-for-character. The only permitted edits inside moved text are retargeting stale references ("Appendix A/C/D/E/F" → bold-name pointers; "Arc X" labels → bold quest names).

**Overview spoiler rule:** Write the Overview as what a player would know from the character's PUBLIC face on first meeting. For anyone with a cover identity, disguise, secret allegiance, or hidden nature (e.g. Jarlaxle as Zardoz Zord, Aurinax as a dwarf, Nar'l as Xanathar's advisor, Cassalanters as philanthropists, doppelgangers, possessed people, cultists), describe ONLY the cover. Never mention the Stone of Golorr, the Eyes, the vault, a villain's real plan, or who secretly works for whom. When in doubt, say less.

**Featured in:** Bold names, comma-separated, quests first in campaign order (Finding Floon, Trollskull Alley, Fireball!, Gralhund Villa, Faction Outposts, Xanathar's Lair, Cassalanter Villa, Sea Maidens Faire, Kolat Towers, Vault of Dragons), then missions, then locations. If none found, write "Background figure; no scripted appearance."

### 8. Organization Page (`campaign/setting/organizations/NN-faction.md`)

One file per faction. GM zone comes first; player-facing sections come last. File naming: zero-padded `NN-` prefix, lowercase hyphenated faction slug.

```markdown
# [Faction Name]

> [!gamemaster]**Gamemaster's Summary**
>
> - **Campaign role:** [one line — player faction / villain faction / both]
> - **Contacts:** [bold names] — from source preamble
> - **Mission delivery:** [from source preamble] (player factions only)
> - **Featured in:** [bold quest names only — never "Arc X" labels]

## Operations
[Player factions: faction description paragraphs, verbatim. Villains: "Personality and Agenda"
verbatim, plus any extra sections such as "The Soul Pact" as ### subsections.]

## Key Members
[One bullet per NPC: `- **[Name]** — [role, one line]. See the **[Name]** page in Notable Figures.`
For villain factions, merge operational sentences verbatim into the bullet.]

## Grand Game Stance
### Grand Game Agenda
[Verbatim agenda paragraph from source]
### Stance
[Verbatim stance text including shares-proactively / asks-for lists]
← player factions only

## Quest Hooks                  ← player factions (source table; "Arc X" labels replaced with quest names)
## First Meeting                ← player factions (2–4 sentence summary: who, where, the offer; then a
                                   link to the faction's `00-first-meeting` event in Faction Events)

## Response Teams               ← villain factions (source, verbatim)
## Outposts                     ← villain factions (source; each outpost a ### heading, verbatim)
## Escalation                   ← villain factions (this faction's escalation row rendered as a
                                   4-row table Tier | Behavior using the four tiers
                                   Unaware/Suspicious/Alert/Lockdown, plus faction-specific notes)
## Revelation List              ← villain factions (source section for this faction, verbatim)

## Renown & Ranks               ← player factions (source "Earning Renown" list, then Ranks & Benefits
                                   table, verbatim)
## Missions                     ← player factions (source mission table verbatim; each mission name bold
                                   as a pointer to its quest journal; add: "Full mission write-ups are
                                   in the **Faction Events** quest journals.")

## Overview
[NEW: 2–3 sentences, player-safe summary of who the faction is and what it wants. For player
factions, the source "Grand Game agenda" paragraph goes here verbatim as a second paragraph
if it is player-safe.]
```

Bregan D'aerthe gets both player-faction and villain-faction sections.

---

## Cross-Document Callout Syntax

Events, rooms, and overviews call out to each other by **bold name** — never file paths. Foundry will eventually resolve these to journal page links.

| Direction | Syntax |
|---|---|
| Event → next event | `If the party found Renaer, proceed to the **Xanathar Sewer Hideout** Event.` |
| Event → keyed room | `For the full area, see **Z1 — Main Room** in the **Zhentarim Warehouse** journal.` |
| Event → Area Overview | `Refer to the **Gralhund Villa Area Overview** for adversary rosters and map features.` |
| Keyed room → event | `During the **Zhentarim Raid** Event, a squad sweeps this room on Beat 4. Refer to the **Zhentarim Raid** Event for the timeline.` |
| Quest → quest | `This outcome leads into **Gralhund Villa**. See the **Gralhund Villa Overview** for entry conditions.` |

---

## Milestone Points System

The campaign uses Ember's Milestone Points system. No XP is tracked. Advancement is based on completing specific Events.

**How it works:**
- Each milestone-bearing Event awards **1 Milestone Point** to the entire party (including absent players)
- When cumulative points reach the threshold for the next level, the whole party levels up instantly — no Long Rest required
- Level-up recovers HP, spell slots, and Short/Long Rest features; it does NOT recharge item uses or allow spell swaps

**Point values:**
- **Main Quest** — ~2 Milestone Points total across its milestone events (Trollskull Alley 3, Faction Outposts 1, and each lair heist 4 are the exceptions; see the ladder below)
- **Side Quest** — 1 Milestone Point on completion of its terminal event
- **Faction Mission** — no Milestone Points. Faction missions in this campaign are supplementary content; their rewards are gold, renown, tangible items, and cross-quest intel. The main quest ladder (Finding Floon through Vault of Dragons) covers the full 1→8 progression without faction missions.

**Campaign ladder** (reaches the progression table's thresholds exactly):

| Quest | Points | Cumulative | Level |
|---|:---:|:---:|:---:|
| Finding Floon | 2 | 2 | 2 |
| Trollskull Alley | 3 | 5 | 3 |
| Fireball! | 2 | 7 | 3 |
| Gralhund Villa | 2 | 9 | 4 |
| Faction Outposts | 1 | 10 | 4 |
| Lair heists (each, any order) | 4 | 14 / 18 / 22 / 26 | 5 / 6 / 6 / 7 |
| Vault of Dragons | 2 | 24 or 28 | 7 (3 heists) or 8 (4 heists) |

**Progression table:**

| Character Level | Points Required | Cumulative Points |
|:---:|:---:|:---:|
| 1 | — | — |
| 2 | 2 | 2 |
| 3 | 3 | 5 |
| 4 | 4 | 9 |
| 5 | 4 | 13 |
| 6 | 5 | 18 |
| 7 | 5 | 23 |
| 8 | 6 | 28 |

**In event files**, the milestone is an H4 inside the `[!gamemaster]**Next Steps**` block at the end of `### Concluding the Event`:

```markdown
> [!gamemaster]**Next Steps**
>
> [Named callout to following events.]
>
> #### Milestone: [Event Name]
>
> Completing this Event awards 1 Milestone Point. [Optional: "This is likely to advance
> the party to Level X if they have completed [prior quest]."]
```

**When decomposing existing quest files:** Do not convert XP values. Re-designate which events are milestone events based on narrative weight — major discoveries, heist completions, confrontation resolutions. The existing XP structure is retired.

---

## Setting Compendium

The Setting Compendium replaces the former Chapter 2 appendices. It is a GM reference, not an adventure. Structure:

- **Notable Figures** (`campaign/setting/notable-figures/`) — 122 NPC pages organized into 15 group folders. One NPC Page per named character (see File Type Spec 7). Groups: trollskull-community, independents-allies, independents-adversaries, city-officials, harpers, lords-alliance, emerald-enclave, order-of-the-gauntlet, force-grey, doom-raiders, bregan-daerthe, xanathars-guild, manshoons-zhentarim, cassalanters, gralhunds.
- **Organizations** (`campaign/setting/organizations/`) — 10 faction pages (01-harpers through 10-cassalanters). Each page merges player-faction and villain-faction content: operations, key members, Grand Game stance, quest hooks, response teams, outposts, escalation, renown, and missions (see File Type Spec 8).
- **Lore and History** (`campaign/setting/waterdeep-lore.md`, `history.md`, `grand-game.md`) — wards, governance, guilds, religion, festivals, dragonward; 8-era narrative history; in-world Grand Game frame.
- **Villain Files** (`campaign/setting/villains/`) — full character documents for Xanathar, Manshoon, the Cassalanters, and Jarlaxle: personality phases, relationships, goals.
- **Trollskull Manor Guide** (`campaign/guides/trollskull-manor/`) — 9 pages covering operating costs, staff and hiring, fame, revenue, the tenday schedule, tavern events, notable patrons, and response teams at the manor. The Ember "Stronghold" analog.

---

## Chapter 3 — Running the Campaign

Contains:

- **Adventure Summary**: structured list of acts with level ranges, prose paragraph per act, and milestone table keyed to quest completions.
- **Structural Rules**: recurring mechanics — faction spy behavior, villain response, encounter tables, bespoke rules.
- **[Villain]'s Relationship to the PCs**: how antagonist attitude evolves, when and why they escalate.
- **Design Notes: Running the Campaign**: macro-level design notes explaining every major structural decision.

---

## NPC Profiles in Event and Area Files

For a named NPC who appears within an event or keyed room, their roleplaying profile goes in a `[!social]` block at the point where the party first encounters them. Use the epithet as the block title. The first line of the block body is the NPC header: `Name (Alignment, Ancestry, pronouns) :: one-line summary`.

```markdown
> [!social]**The Grudging Fence**
>
> Davil Starsong (Neutral, Half-Elf, he/him) :: a cheerful Zhentarim fixer who wants the party to owe him a favour.
>
> Davil is all warmth and easy smiles until someone tests his patience. He runs this meeting
> like a job interview, not a negotiation.
>
> Conversation topics Davil is willing to discuss include:
> - What the Zhentarim want from the party
> - The recent fireball on Trollskull Alley (deflects any blame)
> - What he can offer in exchange for loyalty
>
> Any character who succeeds on a DC 13 Insight check senses that Davil is withholding
> something about the fireball — he knows more than he is saying.
```

**Resonance** is the most important dimension — it tells the GM what the players should feel toward the NPC. State it in the one-line summary or the opening sentence of the personality section. **Persona** always has three parts: public face / private face / inner truth.

For standalone NPC pages in Notable Figures, use File Type Spec 7 instead.

---

## Design Notes Philosophy

Design notes are a justification addressed to the DM of *why* a change was made and what it accomplishes. They appear in the `design-notes.md` page of each quest journal.

### The Three Questions Every Design Note Answers

1. **What was wrong with the original?** Name the specific failure mode precisely.
2. **What did you replace it with, and why?** State the change and connect it to a design goal.
3. **What does this accomplish?** 2–4 distinct goals. If a change only accomplishes one thing, ask if it's pulling enough weight.

### Tone and Language

- Use **"has been intentionally [action]"** for deliberate omissions or restrictions.
- Name **player psychology directly**: "to ensure players don't resent X," "to prevent players from feeling deceived."
- **Anticipate community additions** you chose NOT to adopt, and explain why.
- **Foreshadow future payoffs** in the design note for the scene that plants the seed.

### What Not to Put in Design Notes

- Lore explanation — belongs in GM prose or a `[!gamemaster]` block in the relevant event
- Tactical GM advice — belongs in a `[!gamemaster]` block inline in the event
- Read-aloud text — never in design notes
- Summaries of what happens — the quest overview does that

---

## Scene Writing Voice

Adventure text addresses the GM in second person. Present tense for static descriptions. Past tense only in backstory and quest overview summaries.

Events describe what is happening when the PCs arrive — NPCs are mid-action. The world does not pause.

Every event file is written from scratch. No citations or references to original source books.

**Readaloud text** is written to be spoken to the players. Write only what the characters perceive — no GM knowledge, summary, or backstory. Present tense, second person ("you"). Length fits the moment: a door is two sentences, a set-piece can run many paragraphs. End in motion, on what someone does or says next, never on a punchline. **How the sentences sound is set by `ember-voice`; load it before writing any prose.** NPC speech inside a readaloud block is written as nested `> >` blockquotes within the block. Every passage the GM reads aloud is a `> [!readaloud]` block; conditional variants are introduced in surrounding GM prose ("If X, read or paraphrase the following:") and are still `> [!readaloud]` blocks.

**NPC encounters** use `> [!social]` blocks, placed at the point of first contact or any time the party re-engages an NPC in a scene. The run of `> [!qna]` blocks that follows covers topics the players are likely to raise — write each answer as read-aloud: an optional narration beat, then the NPC's quoted words.

**Readaloud and dialogue density.** Match Ember's density. The user asked for "a higher number of boxed text, verbatim dialogue and narrative sections."
- **Every beat the players experience gets a `[!readaloud]`:** arrivals, NPC entrances, reveals, the turn of a fight, discoveries, aftermath and departures. GM prose between blocks is one or two sentences of framing.
- **NPCs speak in their own words.** Wherever GM text would *describe* what an NPC says ("Mirt explains the Harpers"), write the speech verbatim inside a readaloud or qna answer.
- **Every `[!social]` block is followed by a run of `[!qna]` blocks**, one for each topic the NPC discusses and each question the players will obviously ask.
- **Every branch outcome gets its own conditional readaloud:** accept or decline, success or failure, capture or escape.
- **Findings are shown in voice.** An exploration check that reveals something ends with a nested `> >` quote of what the character perceives.

**Missions open with the brief.** The first scene of a faction mission's first event is `### The Brief`: the faction contact gives the party the job in person, where the mission overview says they deliver it. The scene has:
- a line of GM framing
- a `[!readaloud]` of the meeting, with the brief as the contact's verbatim speech (what happened, what's needed, why the party, what's in it for them)
- a `[!social]` block for the contact
- `[!qna]` blocks for the obvious questions (who, why us, what do you know, where do we start, the pay)
- a pointer into the next scene

Answers use only facts in the mission files. Where a fact isn't stated (a pay figure), the contact deflects in character rather than inventing one. The user: "Each mission will need to have a scene with getting the actual mission brief as well."

**Checks** go in `> [!exploration]` or `> [!hazard]` blocks. Never resolve a GM-side outcome with a die roll — zero-prep means the outcome is decided in the text.

---

## The Remix is a Whole

The remix is an integrated tapestry. A minor detail in Finding Floon may be a load-bearing support for Cassalanter Villa. Design notes must surface these connections. When designing any event or location, always ask: does this element appear again? When? Does removing it break anything downstream? If a future payoff exists, plant it in the design note for the event that introduces it.
