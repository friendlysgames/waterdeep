---
name: dnd-adventure-text
description: >
  Use this skill whenever writing, editing, or converting TTRPG adventure content — including encounter areas, NPC descriptions, read-aloud text, skill checks, combat blocks, treasure entries, and GM notes. Trigger for any task that produces adventure text: writing dungeon rooms, converting notes into room entries, rewriting encounter text, drafting NPC dialogue for GM use, or adding skill check callouts to adventure prose. Also trigger when the user asks to "write it like a published adventure", "format this as a D&D encounter", or "make this sound like official adventure text". This skill governs prose voice, check notation, condition capitalization, action economy language, and encounter structure. For the HTML class names, sidebar types, callout blocks, narrative divs, and Foundry page/category structure, defer entirely to the foundry-journal skill.
---

# D&D Adventure Text Style Guide

This skill governs how adventure content is **written and structured** — the prose voice, the grammar of skill checks, the shape of an encounter entry, and the taxonomy of GM-facing information. It is source-system agnostic and applies equally whether the final output is a Foundry journal, a plain markdown file, or a Word document.

For **visual formatting** (HTML classes, sidebar callout types, `[!info]` / `[!combat]` blocks, narrative divs, dialogue blocks, NPC portrait blocks, Foundry page structure), see the `foundry-journal` skill. This skill tells you *what to say*. That skill tells you *how to wrap it*.

---

## Voice and Register

Adventure text addresses the GM directly in second person: "you", "the party", "the characters." It is a colleague briefing a colleague: plain, complete and friendly, never cinematic. Sentence-level voice for every kind of adventure text follows `ember-voice`.

**Do:** "The goblins spot the party and draw their weapons."
**Don't:** "If the goblins see the player characters, they will draw their weapons and prepare to fight."

- Present tense for descriptions of static spaces and persistent facts.
- Past tense only for backstory, history, or what has already happened in-world before the party arrived.
- No padding. Say it once, precisely.
- Contractions are normal everywhere, as in Ember: most common in NPC speech, common in GM prose, occasional in read-aloud narration.

---

## Encounter Entry Structure

Each encounter area or event follows this order. Not every entry needs every section — include only what applies.

1. **Setup paragraph** — who or what is here, their current state, and any relevant environmental detail not in the read-aloud. GM-only.
2. **Read-aloud** — what the players experience on arrival. See formatting below.
3. **Creature behavior** — how creatures react, what triggers combat, what triggers flight or surrender.
4. **Interaction opportunities** — skill checks, social options, puzzle elements.
5. **Special rules** — traps, environmental hazards, unusual mechanics.
6. **Treasure** — items, coins, valuables.
7. **Development** — consequences, connections to other areas, what changes if X happens.

Not all of these need explicit headers. Short entries fold multiple sections into tight prose. Only add headers when a section is long enough to risk losing the GM.

---

## Read-Aloud Text

Read-aloud text is what the GM reads or paraphrases to the players. It describes only what the characters can perceive — no hidden information, no stat block names.

Use the `[!readaloud]` block (see `foundry-journal`):

```
> [!readaloud]
> The door opens onto a vaulted chamber. Shelves of crumbling books line every wall, and the air smells of old paper and something sharper — burning.
```

A conditional readaloud is introduced in the surrounding GM prose: "If X, read or paraphrase the following:", then the block follows immediately.

### Voice

**The voice of all read-aloud text is set by `ember-voice`.** Read it before writing any read-aloud; its rules, numbers and examples override anything here. In short:
- Plain, generous, literal description in flowing sentences of about 21 words.
- The wide shot first, then the person or thing that matters, then their speech or the detail that invites the party to act.
- NPCs speak in their own chatty words, introduced by a physical action tag.
- Paragraphs never end on a punchline, a verdict or an ominous one-liner.
- The length fits the moment. Most blocks run 50–100 words, and a set piece can run many paragraphs.

What still applies from this skill:
- **Only what the characters perceive.** No hidden information, no stat block names beyond what they would recognise, no mechanics, no history the characters don't know.
- **Things are already happening.** Creatures and NPCs are in motion when the party arrives: goblins pulling books off shelves, a bear rising from a stream.
- **Show evidence, not conclusions.** "Dried blood traces the outline of a circle on the floor", not "this room appears to have been used for dark rituals".
- **No "you find yourself" openers and no exit inventories.**
- **Split when the moment has two phases.** An explosion, a gate slamming shut, the dust settling after a collapse: use two consecutive blocks, each delivered as the scene reaches it.

---

## Skill Checks

### Standard format

```
DC [number] [Ability] ([Skill]) check
```

Examples:
- `DC 13 Wisdom (Animal Handling) check`
- `DC 15 Charisma (Intimidation or Persuasion) check`
- `DC 10 Intelligence (Arcana) check`

When two skills both apply, write both: `(Intimidation or Persuasion)`. When a tool applies: `(Thieves' Tools)`.

### Passive checks

```
Characters with a Passive [Skill] score of [number] or higher [notice/detect/etc.]
```

Example: `Characters with a Passive Perception score of 13 or higher notice the trip wire.`

### Group checks

Refer to them as a **Group Check** — capitalize both words. Describe which skills apply without prescribing exact DCs unless they vary.

### Saving throws

```
makes a DC [number] [Ability] saving throw
```

Example: `makes a DC 11 Constitution saving throw`

For area saves where multiple creatures are affected: "Each creature in the room makes a DC 11 Constitution saving throw."

### Damage notation

```
[average] ([dice]) [type] damage
```

Examples:
- `5 (2d4) poison damage`
- `10 (3d6) fire damage`
- `1 piercing damage`

Damage type is always lowercase: poison, fire, piercing, bludgeoning, etc.

### Tiered check results

When a check reveals more information at higher results, structure as a list:

```
- **DC 10+:** [what is learned]
- **DC 14+:** [additional detail]
- **DC 18+:** [deeper or rarer knowledge]
```

Alternatively, use the **Result of X+** format for inline text: "On a result of 14 or higher, the character also notices..."

---

## Conditions, Actions, and Game Terms

Capitalize these exactly as written in the rulebook.

### Conditions (always capitalized)
Blinded, Charmed, Deafened, Exhaustion, Frightened, Grappled, Incapacitated, Invisible, Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious.

Also capitalize attitude states: **Hostile**, **Indifferent**, **Friendly**.

### Action types (always capitalized)
Attack action, Dash action, Disengage action, Dodge action, Help action, Hide action, Influence action, Magic action, Ready action, Search action, Study action, Utilize action.

Long Rest and Short Rest are capitalized.

### Condition shorthand for repeated use
If a condition appears many times in one entry, you may write it in full the first time and abbreviate in later references: "The drakelings are permanently Blinded — they rely on their Blood Sense ability to locate targets."

---

## NPC and Creature Entries

### First mention
Bold the creature's proper name or stat block name on first mention: **Goblin Boss**, **Brown Bear**, **Agraband Swift**.

Named NPCs get a brief characterization sentence immediately after their bold name: "**Glaxby** is a Goblin Boss who fancies himself a fire-starter."

### Attitude and behavior
State the creature's starting attitude and what changes it:

- "The hobgoblins are Hostile and attack as soon as they spot the party."
- "The bear is Hostile to intruders but doesn't immediately fight — it roars to drive them off first."
- "As an Influence action, a character can try to calm the bear with a DC 13 Wisdom (Animal Handling) check, changing its attitude to Indifferent on a success."

### Surrender and flight
Describe the trigger condition precisely: "If Glaxby is defeated or three of the four Goblin Warriors fall, the survivors flee the library." Don't use vague language like "if they're losing."

### NPC dialogue (GM-facing)
Short lines of NPC speech that appear in GM text (not read-aloud) use quotation marks and are presented inline or as a quoted block. These are suggestions, not scripts:

> "This ain't no place for visitors — turn around and don't come back."

For structured conversation trees (multiple player questions and NPC responses), use the dialogue block format from the foundry-journal skill.

---

## Treasure

Always use a `***Treasure.***` subheader (bold-italic) or the equivalent callout.

Coin amounts use standard notation: `1d6 GP`, `25 GP`, `100 GP each`. Do not write "gold pieces" in full after the first mention in a section.

Named magic items are italicized: *Clockwork Amulet*, *Enduring Spellbook*, *Lethchauntos's Legacy*.

Mundane items of value get their GP worth noted in parentheses or appended: "a gilded acorn worth 200 GP."

Format example:
```
***Treasure.*** Each goblin warrior has 1d6 GP in its pockets. The glass case on the central table contains an *Enduring Spellbook*. Its pages are empty.
```

---

## Development Notes

Use a `***Development.***` subheader for consequences, state changes, and cross-references that the GM needs to track.

```
***Development.*** If two of the hobgoblins are defeated, the third attempts to flee through the secret door to area 8 and alert the goblins there.
```

Development notes should be factual and conditional: "If X, then Y." Avoid speculation. Keep them tight.

---

## Area Headers

Number keyed locations and name them:

```
#### 1: Guard Station
#### 12: Sitting Room
#### 19: Chasm
```

Use the full name even on second reference within the same section ("the goblins in area 8" not "the goblins upstairs").

---

## Traps and Hazards

Describe in this order:
1. What triggers it
2. What it does (saving throw or attack, damage, effect)
3. How to detect it (check DC, passive threshold, or automatic discovery)
4. How to disarm it (check DC, action required, method)

Example structure:
```
***Trap.*** The wolf statue is a magical trap. If a creature touches the table or anything on it without first disarming the trap, the statue fills the room with toxic gas. Each creature in the room makes a DC 11 Constitution saving throw, taking 5 (2d4) poison damage on a failed save or half as much on a successful one. The trap resets after 1 minute.

***Disarming the Trap.*** A character who inspects or reaches into the statue's mouth finds a tiny switch and can flip it, disabling the trap.
```

---

## Doors, Locks, and Secret Passages

State the relevant mechanical property concisely:
- "The door is closed but unlocked."
- "The door is locked (DC 15 Dexterity (Thieves' Tools) check to pick)."
- "All secret doors in this dungeon are DC 15 to find."

If a portcullis or barrier has an unusual resolution method, note that too: "The winch is on the far side — the characters might use *Mage Hand* or *Unseen Servant* to operate it from a distance."

---

## Block Usage

This skill does not define block HTML or syntax. Use the `foundry-journal` skill for that. However, the *purpose* of different Ember blocks maps to adventure text sections as follows:

| Adventure content | Ember block |
|---|---|
| Narration read aloud to players | `[!readaloud]` |
| GM-only event context, summaries, outcomes, next steps | `[!gamemaster]` |
| NPC encounter, personality, roleplaying guidance | `[!social]` |
| One player topic and NPC answer | `[!qna]` |
| Skill checks, discoveries, found items | `[!exploration]` |
| Combat, creatures, hazards, traps | `[!hazard]` |

---

## Common Pitfalls

- **Don't use stat block names when they exceed what the characters would recognise.** The characters wouldn't know "that's a Hobgoblin Warrior" — but they can tell it's a hobgoblin. Use the common name for creatures that are widely known and visually identifiable ("a hobgoblin," "a skeleton," "a lich"), but describe appearance and behaviour for creatures the characters couldn't reliably name on sight ("a powerfully built humanoid in battered armour," "a pale, serpentine creature with clouded white eyes"). The test is whether an ordinary person in that world would look at it and know what it is. A lich is recognisable — robes, phylactery, the unmistakable wrongness of undeath. An Archlich is a stat block distinction they have no way of making.
- **Don't over-qualify.** "The goblins attack" is better than "if the goblins decide to fight, they will begin attacking the characters."
- **Don't use "players" when you mean "characters."** The players are at the table. The characters are in the dungeon.
- **Don't give passive checks as "if the players roll a passive check."** State the threshold: "Characters with a Passive Perception score of 13 or higher notice the trip wire."
- **Don't write damage as "Xd6 damage."** Always include the average: "7 (2d6) slashing damage."
- **Don't duplicate content without reason.** If the read-aloud says the room is dark, the GM text doesn't need to say so again — unless the darkness is mechanically significant. If it's magical darkness, the GM needs to know that even though the players only experienced the effect. Repeat something in the GM text only when the underlying cause matters for running the encounter.
