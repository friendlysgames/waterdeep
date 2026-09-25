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

Adventure text addresses the GM directly in second person: "you", "the party", "the characters." It is authoritative but not stiff — clear, precise, and slightly cinematic. It trusts the GM to improvise; it does not over-explain.

**Do:** "The goblins spot the party and draw their weapons."
**Don't:** "If the goblins see the player characters, they will draw their weapons and prepare to fight."

- Present tense for descriptions of static spaces and persistent facts.
- Past tense only for backstory, history, or what has already happened in-world before the party arrived.
- No padding. Say it once, precisely.
- Contractions are acceptable in NPC speech. Avoid them in GM-facing prose.

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

### The job of read-aloud text

Read-aloud text has one job: to drop the players into a moment. It is not a room inventory, a plot summary, or a mood essay. It gives the players exactly enough to know where they are and what demands their attention — then stops.

The GM has all the detail they need in the surrounding prose. The read-aloud is for the players, spoken aloud at the table, and it competes with ambient noise, distracted brains, and the memory of whatever just happened. Write for that context: vivid, specific, brief.

---

### What to put in — and what to leave out

**Include:**
- The dominant sensory impression of the space (not all senses at once — pick the one that hits first)
- Anything that's actively happening when the party arrives (creatures in motion, sounds, smells)
- The one detail that makes this room different from every other room
- The hook — the thing that demands a response

**Leave out:**
- Exits, unless an exit is the point (a door standing open where it shouldn't be, a tunnel that reeks of death)
- Furniture inventory ("a table, four chairs, a bookshelf, a rug")
- History and backstory — that belongs in the GM text
- Monster stat block names when they exceed what the characters would recognise — see below
- HP, alignment, morale, or any mechanics
- How the characters feel — they're not your characters

---

### Sentence-level craft

**Lead with the room, not with "you."**
The opening sentence grounds the space. "You enter a room and see..." is the weakest possible start. Drop the party directly into the environment.

> ❌ "You enter a large chamber and see several goblins rifling through crates."
> ✅ "This square chamber is packed with crates. Three armed goblins methodically search through them."

**Use verbs that show interrupted action.**
The party has just arrived. Something was happening before they got there. The best read-alouds capture a moment already in motion — which implies a world that exists without the players.

> "A large brown bear *rises* from the stream. A fish drops from its mouth as it roars."
> "Several goblins *pull* books off the shelves, throwing them onto a large pile in the middle of the room, where a well-armed goblin *stands holding a tinderbox*."

The bear wasn't posed there for the party. The goblins weren't waiting. They were doing things. The party interrupted.

**One specific detail beats three generic ones.**
Specificity creates the feeling of reality. Pick the one true strange or telling detail and commit to it.

> ❌ "The room has old, dusty furniture and smells musty and abandoned."
> ✅ "The air smells of old paper and something sharper — burning."

The second version tells you a room full of books is at risk. It earns its place. The first tells you nothing a generic dungeon room wouldn't.

**Let NPC voice carry social scenes.**
When the scene is fundamentally about a person, the read-aloud should often be that person speaking — not a description of the room they're standing in.

> "Please, make yourselves comfortable. I'm so grateful to you all for meeting me here. I have a terrible problem, and I'm hoping you can solve it."

No description of the inn. No description of Myrna. The voice is the scene.

**End on something unresolved.**
Read-aloud that ends on a full stop hands control back to no one in particular. End on something that invites a response — a question in the air, a moment of eye contact, a sound from behind a door.

> ✅ "Words are written above both entrances to the room." *(what do they say?)*
> ✅ "A fish drops from the bear's mouth to the water as it roars!" *(action requiring response)*
> ✅ "'You must be working for Myrna,' the tall human says, blinking slowly at you with wide eyes." *(expectation of reply)*

---

### Length and pacing

**Length fits the moment.** A door gets two sentences; a dramatic set piece earns many paragraphs. The GM reads this aloud. Every sentence that belongs in the GM-only setup paragraph costs attention — put it there instead.

**Long read-alouds are for big moments.** A dramatic set piece — a cathedral, a climactic confrontation, an arrival at a city after a long journey — can earn more space. A supply room cannot.

**Split when the moment has two phases.** If a dramatic scene has a hard break in the middle — an explosion, a gate slamming shut, the dust settling after a collapse — split it into two consecutive blocks. Each ends on its own beat, and the GM delivers them in sequence as the scene progresses. A single block would muddy both moments. For example: a boulder trap could have one block for the crack and the roar of falling stone, and a second for the aftermath once the dust settles and the passage is blocked.

---

### Patterns to avoid

These are the signs of AI-generated or weak read-aloud text. Avoid them.

**The "you find yourself" opener.**
> ❌ "You find yourself standing at the entrance to a grand library."

No one finds themselves anywhere. They walk somewhere. Start in the scene, not approaching it.

**The adjective stack.**
> ❌ "A large, ancient, moss-covered, imposing stone door stands before you."

One adjective, precisely chosen, does more work than four. "The door is iron and old, sweating with condensation." That's a feeling. "Large, ancient, imposing" is a list.

**"You can see / you can hear / sounds can be heard."**
> ❌ "You can hear voices through the wall."
> ✅ "Voices murmur through the wall to the west."

Cut "you can." The sense is implied. The passive form ("sounds can be heard") is worse — it removes even the implied subject.

**Emotional stage directions.**
> ❌ "The room has an eerie, unsettling atmosphere."
> ✅ "A single candle burns on the table. The rest of the room is dark."

The players decide how it feels. You give them the facts that produce the feeling.

**Summarising instead of showing.**
> ❌ "This room appears to have been used for dark rituals."
> ✅ "Dried blood traces the outline of a circle on the floor. At its center, a chair with manacles bolted to the armrests."

Show the evidence. Let the conclusion land on its own.

**The procedural exit.**
> ❌ "There are three exits: a door to the north, a corridor to the east, and a staircase descending to the south."
> Never end a read-aloud on an exit inventory. That's cartography, not atmosphere.

---

### The fast test

Before finalising any read-aloud, ask:
1. Could I cut the first sentence and start on the second? (If yes, cut it.)
2. Does this contain anything the GM text already says? (If yes, remove the duplicate.)
3. Is there a creature or NPC here? Are they *doing something*, or just standing? (They should be doing something.)
4. Does it end on something that invites response, or just trail off?
5. Would a GM feel confident reading this cold, mid-session, while someone across the table is arguing about spell slots? (If not, simplify.)

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
