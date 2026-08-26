---
name: adventure-reloaded
description: >
  Governs the structure, voice, and design philosophy for writing the Waterdeep Campaign Remix.
  Modeled directly on Curse of Strahd: Reloaded by DragnaCarta. Use whenever writing or
  structuring any arc, chapter, scene, NPC profile, reference chapter, or design notes section
  for the Dragon Heist / Dungeon of the Mad Mage remix. This skill defines HOW the document
  is organized and WHY design choices are made — not the mechanical formatting (see foundry-journal
  for that). Load this skill before writing any campaign content.
---

# Adventure Reloaded — Campaign Writing Guide

This skill governs how the Waterdeep Campaign Remix is structured and written. It is modeled
directly on *Curse of Strahd: Reloaded* (DragnaCarta, 2023–present), the gold standard for
published campaign remix writing. Everything here derives from studying that work directly.

---

## Document Architecture

The campaign is organized around **narratives**, not locations. This is the foundational
structural decision — everything flows from it.

```
Campaign
├── Chapter 1 — Beginning the Campaign  (session zero, character creation)
├── Chapter 2 — The World               (reference material: lore, factions, key villains)
├── Chapter 3 — Running the Campaign    (adventure summary, structural rules, pacing)
├── Act I — [Title]                     (acts group arcs with similar stakes/settings)
│   ├── Act I Summary
│   ├── Arc A — [Name]                  (each arc = one high-concept adventure with a goal)
│   │   ├── Scene entries               (keyed locations and moments within the arc)
│   │   └── Design Notes: [Arc Name]   (end-of-arc section explaining every major change)
│   └── Arc B — [Name]
└── Act II — [Title]
    └── ...
```

**Acts** bundle arcs that take place in the same setting or timeframe (e.g., "adventures in
Waterdeep's wards before the vault is located").

**Arcs** are complete narrative units with a dramatic question and a clear goal
(e.g., "infiltrate Gralhund Villa and recover the Stone of Golorr").

**Chapters** within an arc are portions set in a particular location or phase.

**Scenes** are discrete moments within a chapter — a confrontation, a discovery, a choice.

---

## Chapter 2 — Reference Material

Chapter 2 is a GM reference, not an adventure. It is read before play, not during.
Structure it as:

- **Lore of [Setting]** — geography, culture, factions, magic, religions, key history.
  Written in sourcebook voice (see `ttrpg-sourcebook-style`). Every fact implies consequence.

- **History of [Setting]** — narrative timeline, written as a story, not a list of dates.

- **[Key Villain]** — a full character document covering:
  - **Roleplaying [Villain]**: personality phases (e.g., the Schemer, the Tyrant, the Monster),
    each with: what players should feel, the villain's emotional range, pop-culture inspiration
    characters to channel, what triggers the shift to the next phase, and behavioral rules.
  - **[Villain]'s Relationships**: how the villain views each major faction/NPC in the campaign.
    One paragraph per relationship. Specific and opinionated, never neutral.
  - **[Villain]'s Goals**: broken into named sub-plans, each with its own method, contingency
    if foiled, and how it connects to the larger scheme.

---

## Chapter 3 — Running the Campaign

Contains the structural scaffolding the DM needs before running anything:

- **Adventure Summary**: a flowchart or structured list of acts with level ranges, a prose
  paragraph per act summarizing its dramatic arc, and a milestone XP table for each act
  (keyed to specific arc completions, not monster kills).

- **Structural Rules**: recurring mechanics the DM needs throughout — faction spy behavior,
  how the villain responds to PC actions, recurring encounter tables, any bespoke rules
  introduced by the remix.

- **[Villain]'s Relationship to the PCs**: how the main antagonist's attitude evolves across
  the campaign. What they do at each stage. When and why they escalate.

- **Design Notes: Running the Campaign**: the macro-level design note section explaining
  every major structural decision — hook selection, artifact placement, ally restrictions,
  location of the final confrontation. See the Design Notes section below for format.

---

## Arc Structure

Every arc follows this structure, in order:

### 1. Arc Opener (always first)

```
*An adventure for X-level characters.*

[2–4 paragraphs in past tense, summarizing the arc's narrative beats as they will unfold:
what the PCs are doing, who they meet, what choices they face, how it ends.]
```

The summary is written as if looking back on completed events. It names key NPCs, locations,
and decisions — giving the DM the full shape of the arc before reading the detail.
It does NOT describe outcomes; it describes what happens and what the PCs must choose.

If a major structural departure from the original adventure is present, place a brief
`[!design]+` callout immediately after the opener explaining the core premise of the change.

### 2. Scene Entries

Keyed to numbered locations or narrative moments. See the Callout Taxonomy below for
what appears inside each entry.

Every scene is written from scratch. No citations to the original source material.

### 3. Design Notes Section (always last)

```markdown
# Design Notes: [Arc Name]
## [Major Category, e.g., "The Infiltration" or "NPC Introductions"]

***[Element Name].*** [Design note prose]

***[Element Name].*** [Design note prose]

## [Next Major Category]
...
```

This is the most important section of every arc. See the full Design Notes Philosophy below.

---

## Callout Taxonomy

These are conceptual categories, not just formatting — each one has a distinct purpose.
Descriptions below are taken directly from CoS:R's *Using This Guide* document.

| Callout | Label | Purpose |
|---------|-------|---------|
| `[!info]+` | Info | Additional information about the rules needed to run a particular scene or area. |
| `[!warning]+` | Warning | Calls attention to important information to avoid common pitfalls and mistakes. |
| `[!lore]+` | Lore | Provides or reminds the GM of additional context about a scene, chapter, or arc. |
| `[!abstract]+` | Narrative | An optional path the players might take through a scene or area. |
| `[!profile]+` | Profile | Additional information about roleplaying and understanding a particular NPC. |
| `[!item]+` | Item | Statistics for a new or modified item. |
| `[!design]+` | Design | Designer intent and in-context design notes for a specific change. |
| `[!combat]+` | Combat | Encounter balance, monster tactics, and trap mechanics for a specific fight or hazard. |
| `[!npc-narrative]` | NPC Narrative | Player-facing NPC introduction — read-aloud block with the NPC's name and portrait. Use only the *first* time players meet an NPC, or when their appearance has changed substantially (disguise, injury, transformation). Never for repeat encounters. |
| `[!dialogue]` | Dialogue | NPC conversation tree — structured question/answer pairs. Each block is one question and the NPC's response. Use for interrogations, negotiations, or any scene where players are likely to ask a defined set of questions. |

Use `+` (expandable) for all sidebar callouts. Use `-` (collapsed) only for very long design notes that clutter the reading flow. `npc-narrative` and `dialogue` do not use `+` / `-` — they are layout blocks, not sidebars.

---

## NPC Profile Format

Every significant NPC gets a profile, either inline in their first scene or in a dedicated
NPC appendix. The profile has two sections:

```markdown
> [!profile]+ **Profile: [NPC Name]**
>
> **Roleplaying Information**
> ***Resonance.*** [NPC Name] should inspire [emotion] with [trait], [emotion] with [trait],
> and [emotion] with [trait]. (Use: flattery, sympathy, endearment, gratitude, discomfort,
> disgust, pity, admiration — be specific about which trait produces each feeling.)
>
> ***Emotions.*** [NPC Name] most often feels [list of 5–8 specific emotional states].
>
> ***Motivations.*** [NPC Name] wants to [specific concrete goals — 2–3 items].
>
> ***Inspirations.*** When playing [NPC Name], channel [Character (*Source*)], [Character
> (*Source*)], and [Character (*Source*)].
>
> **Character Information**
> ***Persona.*** To the world, [NPC Name] is [public face — what strangers see]. To those
> they trust, [NPC Name] is [private face — what allies see]. Deep down, [NPC Name]
> [inner truth — what even they may not consciously admit].
>
> ***Morale.*** In a fight, [NPC Name] would [behavior — specific, not vague: "plead for
> peace, but draw their blade if X" is better than "fight if necessary"].
>
> ***Relationships.*** [NPC Name] is [relationship] of [Named Character], and [relationship]
> of [Named Character].
```

**Resonance** is the most important field. It tells the DM what the players should feel
toward this NPC, not what the NPC is like. A Resonance entry that doesn't specify the
player-facing emotion is incomplete.

**Inspirations** should be characters with a recognizable, specific playing style — not
just vibes. "Channel Tywin Lannister (*Game of Thrones*)" tells a DM something precise.
"Channel a calculating aristocrat" does not.

**Persona** always follows the three-part structure: public / private / deep down.
The gap between them is the character's dramatic potential.

---

## Design Notes Philosophy

This is the heart of the remix writing style. Every arc ends with a design notes section
that explains every major structural departure from the original adventure. Getting this
right is what separates a remix from a rewrite.

### What the Design Notes Are For

Design notes are not a summary of what changed. They are a justification — addressed to
the DM — of *why* the change was made and what it is designed to accomplish. They let the
DM understand the author's intent well enough to make good judgment calls at the table
when things go off-script.

They also serve a second purpose: they signal that the remix is *deliberate*. Every
omission, every addition, every restructuring is explained. This builds DM trust.

### The Three Questions Every Design Note Answers

For every significant change, answer all three:

1. **What was wrong with the original?** Name the specific failure mode — what players
   tend to feel, do, or misunderstand as a result of the original design. Be precise.
   "This tends to make players resent [NPC]" is better than "this doesn't work well."

2. **What did you replace it with, and why?** State the change and connect it to a
   specific design goal. "X has been revised to ensure that players have an immediate
   and concrete reason to [action]."

3. **What does this accomplish?** Usually 2–4 distinct goals. List them. If a change
   only accomplishes one thing, ask whether it's pulling enough weight.

### Tone and Language

- Use **"has been intentionally [action]"** when a deliberate omission or restriction
  might otherwise seem like an oversight. "The dog has been intentionally removed" signals
  a decision; "the dog is not present" implies carelessness.

- Name **player psychology directly**: "to ensure players don't resent X," "to prevent
  players from feeling deceived," "to allow players to experience a sense of agency even
  when the fiction denies it." The unit of measurement is always what players feel.

- **Anticipate community additions and fan fixes** that you chose NOT to adopt, and
  explain why. "A popular community addition places X here. This guide intentionally
  foregoes it because [reason]." This demonstrates mastery and prevents DMs from
  wondering if you missed something.

- **Foreshadow future payoffs** in the design note for the scene that plants the seed.
  "[NPC] will later reappear in [Arc Y] to [purpose]." This makes the web of callbacks
  visible and helps the DM understand that nothing is accidental.

### Structural Design Notes (Chapter 3)

The macro-level design notes in Chapter 3 follow the same philosophy but at campaign
scope. Each covers a structural decision that affects the whole campaign:

- Why this hook was chosen over alternatives (and what was wrong with the alternatives)
- Why an artifact is placed where it is (what the player experience would be if placed
  earlier or later)
- Why certain allies or options were removed from randomization
- Why the final confrontation is located where it is

These notes should be written with the assumption that the DM is an experienced player
who has read the original source material and may have heard community opinions about it.
Engage with those opinions directly.

### What Not to Put in Design Notes

- **Lore explanation** — that belongs in a `[!lore]+` callout in the scene itself.
- **Tactical GM advice** — that belongs in a `[!warning]+` or `[!info]+` callout.
- **Read-aloud text** — never in the design notes.
- **Summaries of what happens** — the arc summary does that. Design notes explain WHY.

---

## Scene Writing Voice

Adventure text addresses the GM in second person: "you," "the players," "the characters."
Present tense for static descriptions. Past tense only in backstory and arc summaries.

Scenes describe what is happening when the PCs arrive — not what has already concluded.
NPCs are mid-action. The world does not pause.

Every scene is written from scratch. No citations or references to the original source books.

For read-aloud text, use `<div class="description"><p>...</p></div>` blocks (see
`dnd-adventure-text` for prose craft; see `foundry-journal` for visual formatting).

---

## Milestone XP Tables

Each act includes a milestone XP table. Format:

| Level | Arc | Milestone | XP |
|:-----:|-----|-----------|---:|
| 3 | A | The players [accomplish X] | 400 |

XP is awarded for narrative achievements, never for combat. Every milestone should be
something the players can clearly feel they earned — not a hidden DM trigger.

---

## The Remix is a Whole

The single most important structural principle from CoS:R: **the remix is an integrated
tapestry.** A seemingly minor detail in Arc A may be a load-bearing support for Arc G.
Design notes should always surface these connections, so the DM running the campaign
understands which threads are decorative and which are structural.

When designing a change, always ask: does this element appear again? When? Does removing
it break anything downstream? If a future payoff exists, plant it in the design note for
the scene that introduces it.
