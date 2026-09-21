---
name: adventure-reloaded
description: >
  Governs the structure, voice, and design philosophy for writing the Waterdeep Campaign Remix.
  Defines the Ember-style modular document format: Quest Journals (one per arc) and Location
  Journals (one per location cluster), each containing discrete pages (overview, event files,
  keyed rooms, design notes). Documents the GM/player two-zone pattern for event files, the
  Milestone Points progression system, and the cross-document callout syntax. Load before
  drafting any quest journal, event file, location journal, keyed room, NPC profile, or
  design notes page.
---

# Adventure Reloaded — Campaign Writing Guide

This skill governs how the Waterdeep Campaign Remix is structured and written.

---

## Document Architecture

The campaign is organized around **narratives**, not locations.

```
Campaign
├── Chapter 1 — Beginning the Campaign  (session zero, character creation)
├── Chapter 2 — The World               (reference material: lore, factions, key villains)
├── Chapter 3 — Running the Campaign    (adventure summary, structural rules, pacing)
├── Act I
│   ├── Arc A — Finding Floon           (each arc = one Quest Journal folder)
│   │   ├── overview.md                 (Quest Overview page)
│   │   ├── flowchart.md                (event sequence page)
│   │   ├── ev-01-yawning-portal.md     (Event pages, flat — no subfolder)
│   │   ├── ev-02-dock-ward.md
│   │   ├── ev-03-zhentarim-warehouse.md
│   │   ├── ev-04-xanathar-sewer.md
│   │   └── design-notes.md             (Design Notes page)
│   └── Arc B — [Name]
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

**Acts** bundle arcs with similar stakes or settings.

**Arcs** are complete narrative units with a dramatic question and a clear goal.

**Events** are discrete moments within an arc — a confrontation, a discovery, a choice, a combat phase.

---

## Foundry Journal Model

Each markdown folder maps to one Foundry Journal Entry (one item in the sidebar). Each `.md` file within that folder becomes one Page within that journal.

- **Quest Journal** (`campaign/quests/act-I/arc-a-finding-floon/`) — contains the overview, flowchart, all event pages, and design notes for one arc. Files are flat siblings — no events/ subfolder.
- **Location Journal** (`campaign/locations/zhentarim-warehouse/`) — contains the area overview and all keyed room pages for one location cluster. Separate from the arc that primarily uses it.

Permission gating in Foundry is at the **page level**. The GM/player zone split in event files is enforced by page-level permissions, not by blockquote syntax alone. The `> **[GM]** >` blockquote is a visual marker for specific GM-only callouts within GM-visible content; it does not replace page-level gating.

---

## GM / Player Zone Structure (Event Files)

Every event file has two zones:

**GM zone** (top of file) — all content before `## Overview`. Contains the Gamemaster's Summary, branching narrative phases, NPC tactics, mechanical beats, attunement notes, and Next Steps. Permission: GM-only. Most of this is regular markdown — H3 sections, H4 beats, nested blockquotes for dialogue. The `> **[GM]** >` callout pattern is used selectively for specific GM-only notes (not as a wrapper for all GM content).

**Player zone** (bottom of file) — `## Overview`, `## Read Aloud`, `## Summary`. Permission: visible to players in the Codex. These sections are what players can see when they look at the quest log.

There is no separator rule between the zones — the `## Overview` H2 heading marks the transition.

**`> **[GM]** >` blockquote usage:**
- At the top of each event file, wrapping `#### Gamemaster's Summary`
- Mid-body, for specific tactical spoilers or GM-only notes that should not be read aloud
- At the end of the GM zone, wrapping `#### Next Steps` and `#### Milestone: [Name]`

---

## File Type Specifications

### 1. Quest Overview (`overview.md`)

The landing page for the arc's quest journal. GM zone is a `> **[GM]** >` blockquote at the top. Below the blockquote, `## Involved Characters` and `## Dangers & Enemies` are regular GM-facing markdown. `## Overview` at the bottom is the player-visible summary.

```markdown
# [Arc Name]: [Descriptive Title]

> **[GM]**
>
> #### Quest Requirements
> [Entry conditions; what arcs or flags must precede this one]
>
> #### Difficulty
> *An adventure for X–Y level characters.*
>
> #### Milestone Overview
> [Total Milestone Points this arc awards; which events bear a milestone]

## Involved Characters
- **[NPC Name]** ([faction]) — [one-line role in this arc]

## Dangers & Enemies
[Adversary roster summary — key factions and named opponents active in this arc]

## Overview
[2–4 paragraphs, past tense. The arc's narrative beats from inciting incident to resolution.
Names key NPCs, locations, and the choices the PCs face. The shape of events, not outcomes.]
```

### 2. Event File (`ev-NN-event-name.md`)

One file per scene beat. File naming: zero-padded `ev-` prefix. `ev-01-yawning-portal.md`.

```markdown
# [Event Name]

> **[GM]**
>
> #### Gamemaster's Summary
>
> This [Exploration/Combat/Social] Event occurs when [trigger condition]. In this Event:
>
> - [Bullet: what can happen — 3–6 items]
>
> [Map note: which Foundry scene this event uses, if any]

[GM zone body: H3 branch sections, nested blockquote NPC dialogue, H4 mechanical beats.
Regular markdown — not inside a GM blockquote unless it's a specific GM-only note.]

> **[GM]**
>
> #### [Mid-body GM Note — e.g., "Applying Pressure"]
> [Selective callout for a tactical spoiler or GM-only information within the body]

### Concluding the Event

#### [Attunement Name]: [Condition]
[Attunement text. H4 under Concluding the Event, in regular markdown.]

> **[GM]**
>
> #### Next Steps
>
> [Named callouts to following events. Conditional: "If X occurred, the party proceeds to
> the **[Event Name]** Event. If Y, they proceed to **[Event Name]**."]
>
> #### Milestone: [Event Name]
>
> Completing this Event awards 1 Milestone Point. [Optional level note if applicable.]

## Overview

[One sentence — the player-facing summary of what this event is about.]

## Read Aloud

> [GM reads this aloud when the event begins. NPC dialogue in nested > > blockquotes.]

## Summary

[Quest log entry. 1–2 sentences, past tense. What the party remembers.]
```

**GM zone heading hierarchy:**
- `###` H3 = major narrative phase or branching condition (`### Drake Assault`, `### If the PCs Arrive at Night`)
- `####` H4 = named mechanical beat, NPC behavior, or attunement within a phase (`#### Drake Tactics`, `#### Ragen Attunement: Early Arrival`)
- `> >` nested blockquote = NPC dialogue inside narration or Read Aloud
- `> **[GM]** >` blockquote = selective GM-only callout (Summary at top, tactical notes mid-body, Next Steps + Milestone at end)

### 3. Area Overview (`area-overview.md`)

First page of every Location Journal. Covers all persistent location features.

```markdown
# [Location Name] — Area Overview

> **[GM]**
>
> #### Area Map Context
>
> [Which events use this location. Where the party enters per event. Any map-layer notes.]

## Gameplay Details

The areas of [location] have the following features unless noted otherwise.

### Levels & Elevation
### Illumination
### Terrain
### Inhabitants
[Base inhabitants. Conditional variants: "During the **[Event Name]** Event, the following
also inhabit the area: …"]
### Enemies
[Same pattern — base + event-conditional]

### [Named Mechanic — e.g., "The Day/Night State"]
[H3 per location-wide mechanic. H4 for sub-rules within each mechanic.]

#### [Sub-Mechanic]
[Details]
```

### 4. Keyed Room (`[code]-[room-name].md`)

One file per keyed area entry. File naming: lowercase, zero-padded area code, hyphenated room name. `z01-main-room.md`, `g16-master-bedroom.md`, `x23-nihiloors-lair.md`.

```markdown
# [Area Code] — [Room Name]

[Opening description. No heading. Present tense, second person. 1–3 sentences of what
the PCs perceive when they enter.]

> [Blockquote: opening read-aloud detail, or NPC greeting if one is present.]

[Follow-up prose: sensory detail, interactable elements, what changes over time.]

#### [NPC Name]
[NPC stat reference, conversation topics, behavior when PCs arrive.]

#### [NPC Wares / Services]
[Secondary H4 for inventory or service details if needed]

### [Event Name] — Event-Conditional Section
[Content that only applies during a specific event. Close with:
"Refer to the **[Event Name]** Event for full details."]
```

### 5. Design Notes (`design-notes.md`)

Last page in every Quest Journal. Contains all design rationale for the arc. Format unchanged from existing convention.

```markdown
# Design Notes: [Arc Name]

## [Thematic Category]

***[Element Name].*** [Design note prose — what was wrong, what replaced it,
what it accomplishes, what future payoffs it plants.]
```

### 6. Flowchart (`flowchart.md`)

Second page in the Quest Journal (after overview). Text diagram of the event sequence and its branches. Placeholder for now; becomes a Mermaid diagram in the HTML Artifact pass.

```markdown
# [Arc Name] — Event Flowchart

Start → **Event 01 — [Name]** → branches:
  A: [condition] → **Event 02 — [Name]**
  B: [condition] → **Event 03 — [Name]**
         └── → **Event 04 — [Name]** (shared exit)
```

---

## Cross-Document Callout Syntax

Events, rooms, and overviews call out to each other by **bold name** — never file paths. Foundry will eventually resolve these to journal page links.

| Direction | Syntax |
|---|---|
| Event → next event | `If the party found Renaer, proceed to the **Xanathar Sewer Hideout** Event.` |
| Event → keyed room | `For the full area, see **Z1 — Main Room** in the **Zhentarim Warehouse** journal.` |
| Event → Area Overview | `Refer to the **Gralhund Villa Area Overview** for adversary rosters and map features.` |
| Keyed room → event | `During the **Zhentarim Raid** Event, a squad sweeps this room on Beat 4. Refer to the **Zhentarim Raid** Event for the timeline.` |
| Arc → arc | `This outcome leads into **Arc D: Gralhund Villa**. See the **Arc D Overview** for entry conditions.` |

---

## Milestone Points System

The campaign uses Ember's Milestone Points system. No XP is tracked. Advancement is based on completing specific Events.

**How it works:**
- Each milestone-bearing Event awards **1 Milestone Point** to the entire party (including absent players)
- When cumulative points reach the threshold for the next level, the whole party levels up instantly — no Long Rest required
- Level-up recovers HP, spell slots, and Short/Long Rest features; it does NOT recharge item uses or allow spell swaps

**Point values:**
- **Main Quest arc** — ~2 Milestone Points total across its milestone events
- **Side Quest** — 1 Milestone Point on completion of its terminal event
- **Faction Mission** — no Milestone Points. Faction missions in this campaign are supplementary content; their rewards are gold, renown, tangible items, and cross-arc intel. The main arc ladder (Arcs A–J) covers the full 1→8 progression without faction missions.

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

**In event files**, the milestone is the last H4 inside the `> **[GM]** > #### Next Steps` block:

```
> #### Milestone: [Event Name]
>
> Completing this Event awards 1 Milestone Point. [Optional: "This is likely to advance
> the party to Level X if they have completed [prior arc]."]
```

**When decomposing existing arc files:** Do not convert XP values. Re-designate which events are milestone events based on narrative weight — major discoveries, heist completions, confrontation resolutions. The existing XP structure is retired.

---

## Chapter 2 — Reference Material

Chapter 2 is a GM reference, not an adventure. Structure it as:

- **Lore of [Setting]** — geography, culture, factions, magic, religions, key history.
- **History of [Setting]** — narrative timeline, written as a story, not a list of dates.
- **[Key Villain]** — a full character document covering:
  - **Roleplaying [Villain]**: personality phases, each with player-facing emotional goals, pop-culture inspirations, triggers for phase shifts, behavioral rules.
  - **[Villain]'s Relationships**: one paragraph per major faction/NPC. Specific and opinionated, never neutral.
  - **[Villain]'s Goals**: named sub-plans with method, contingency, and connection to the larger scheme.

---

## Chapter 3 — Running the Campaign

Contains:

- **Adventure Summary**: structured list of acts with level ranges, prose paragraph per act, and milestone table keyed to arc completions.
- **Structural Rules**: recurring mechanics — faction spy behavior, villain response, encounter tables, bespoke rules.
- **[Villain]'s Relationship to the PCs**: how antagonist attitude evolves, when and why they escalate.
- **Design Notes: Running the Campaign**: macro-level design notes explaining every major structural decision.

---

## Callout Taxonomy

| Callout | Label | Purpose |
|---------|-------|---------|
| `[!info]+` | Info | Additional information about rules needed to run a scene or area. |
| `[!warning]+` | Warning | Important information to avoid common pitfalls and mistakes. |
| `[!lore]+` | Lore | Additional context about a scene, chapter, or arc. |
| `[!abstract]+` | Narrative | An optional path players might take through a scene or area. |
| `[!profile]+` | Profile | Additional information about roleplaying a particular NPC. |
| `[!item]+` | Item | Statistics for a new or modified item. |
| `[!design]+` | Design | Designer intent and in-context design notes for a specific change. |
| `[!combat]+` | Combat | Encounter balance, monster tactics, and trap mechanics. |
| `[!npc-narrative]` | NPC Narrative | Player-facing NPC introduction — read-aloud block. First encounter only, or after substantial appearance change. |
| `[!dialogue]` | Dialogue | NPC conversation tree — structured question/answer pairs. |

Use `+` (expandable) for all sidebar callouts. `npc-narrative` and `dialogue` do not use `+`/`-`. These callouts appear inside the GM zone of event files and inside location/area files.

---

## NPC Profile Format

```markdown
> [!profile]+ **Profile: [NPC Name]**
>
> **Roleplaying Information**
> ***Resonance.*** [NPC Name] should inspire [emotion] with [trait], [emotion] with [trait],
> and [emotion] with [trait].
>
> ***Emotions.*** [NPC Name] most often feels [list of 5–8 specific emotional states].
>
> ***Motivations.*** [NPC Name] wants to [specific concrete goals — 2–3 items].
>
> ***Inspirations.*** When playing [NPC Name], channel [Character (*Source*)], [Character
> (*Source*)], and [Character (*Source*)].
>
> **Character Information**
> ***Persona.*** To the world, [NPC Name] is [public face]. To those they trust, [NPC Name]
> is [private face]. Deep down, [NPC Name] [inner truth].
>
> ***Morale.*** In a fight, [NPC Name] would [behavior — specific, not vague].
>
> ***Relationships.*** [NPC Name] is [relationship] of [Named Character], and [relationship]
> of [Named Character].
```

**Resonance** is the most important field — it tells the DM what players should feel toward the NPC, not what the NPC is like.

**Inspirations** must name characters with a specific, recognizable playing style.

**Persona** always follows three parts: public / private / deep down.

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

- Lore explanation — use `[!lore]+`
- Tactical GM advice — use `[!warning]+` or `[!info]+`
- Read-aloud text — never in design notes
- Summaries of what happens — the arc overview does that

---

## Scene Writing Voice

Adventure text addresses the GM in second person. Present tense for static descriptions. Past tense only in backstory and quest overview summaries.

Events describe what is happening when the PCs arrive — NPCs are mid-action. The world does not pause.

Every event file is written from scratch. No citations or references to original source books.

For Read Aloud text (`## Read Aloud`), use a blockquote. NPC dialogue within Read Aloud uses nested `> >` blockquotes.

---

## The Remix is a Whole

The remix is an integrated tapestry. A minor detail in Arc A may be a load-bearing support for Arc G. Design notes must surface these connections. When designing any event or location, always ask: does this element appear again? When? Does removing it break anything downstream? If a future payoff exists, plant it in the design note for the event that introduces it.
