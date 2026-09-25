---
name: ember-adventure-style
description: >
  Ember-derived voice and sentence-level style for ADVENTURE TEXT in the Waterdeep campaign: event
  files, quest overviews, keyed rooms, area overviews, read-aloud, NPC dialogue in scenes, combat
  tactics, skill-gated information, branching, rewards, and player-facing Overview/Summary text.
  Load alongside dnd-adventure-text (which keeps authority over check/damage/condition notation,
  traps, treasure, and doors) whenever drafting or revising any scene-level content. Structure comes
  from adventure-reloaded; this skill governs how the sentences inside that structure are written.
---

# Ember Adventure Style

This skill captures how the Ember campaign writes adventure prose, adapted to this project's 2024 rules and zero-prep rules. It is a **voice layer**. It runs in parallel with two other skills and does not replace either:

| Skill | Owns |
|---|---|
| `adventure-reloaded` | File types, headings, GM/player zones, flags, Milestone Points, callout syntax |
| `dnd-adventure-text` | Check/save/damage notation, condition and action capitalization, traps, treasure, doors, read-aloud craft basics |
| **`ember-adventure-style`** | Voice per zone, sentence templates, NPC and dialogue choreography, tactics shape, branching language, reward staging, recap voice |

**Precedence when they disagree:** notation → `dnd-adventure-text`. Structure → `adventure-reloaded`. Voice, phrasing, and sentence shape → this skill. Project rules in CLAUDE.md (zero-prep, no dice rolls, members-only debriefs) override all three.

---

## 1. The Three Voices

Ember keeps three voices strictly apart. Never blend them in one paragraph.

| Zone | Speaks to | Person | Tense | Register |
|---|---|---|---|---|
| GM prose (everything above `## Overview`) | The GM | "you" = the GM; "the party" / "the characters" / "any character who" | Present | Warm, competent, lightly elevated |
| Read-aloud | The players | "you" = the characters | Present | Sensory, brief, ends on a hand-off |
| `## Summary` | The party's own journal | "we" | Past | Plain, a little informal |

**GM prose.** When the text addresses the GM directly, it says "you": *"As the Gamemaster, you should ensure that Krafton's Caravan moves from here to Rortwark."* It never says "the GM should consider." The party is always third person, "the party" or "the characters." "You" never means the players anywhere in GM prose.

**Read-aloud.** This is the only place "you" means the characters.

**Summary.** Ember writes the recap as the party's journal entry in first-person plural past tense:
> *We met with Steros Kraver of the Burnished Hand in Ordain's Lower Ashvale district. While leaving Veneration Hall, we were approached by a Burnished Hand Protector named Vance who beseeched us to check up on a fellow Protector who has been missing for a week.*

It may end on the open thread in present tense ("We must head to … if we wish to …"). Keep it to 1–3 sentences.

**`## Overview`** (player-facing, one or two sentences) is third person, present tense, no spoilers: *"The party encounters a wealthy caravan led by Krafton Lilifeld, head of the famous House Lilifeld."*

---

## 2. Register

- **Warm and confident.** State what happens. "Krafton immediately offers shade and refreshments," not "Krafton might offer."
- **Lightly elevated diction** in narration: *beseech, entreat, beckon, discern, ingratiate, retinue, retainer.* One elevated word per sentence at most. Never archaic.
- **No contractions in narrator prose. NPCs use contractions freely.** The contrast is deliberate.
- **Humor lives in the characters, never the narrator.** The document is never jokey. Krafton is funny; the text about Krafton is not.
- **No meta-commentary.** No "this may be difficult for low-level parties," no apology, no balance talk in scene prose. Design reasoning goes in `design-notes.md`.
- **Failure is neutral and sympathetic.** Failure has a consequence, stated plainly, and the text never scolds: *"If the party fails to rescue Humbolt, he sinks up to his neck before Krafton's other staff manage to pull him out."*

---

## 3. Paragraph Openers

GM paragraphs open on **who is present or what is happening**, then deliver the mechanic. Never open a paragraph on a check.

> ✅ *Once the party reaches Cindarin Temple and spots their ally Sin Marmot, they have a few scant moments to …*
> ❌ *A DC 14 Wisdom (Perception) check lets the party spot Sin Marmot.*

Scene sections open with a **situation sentence** that names the NPC, gives a one-clause identity, and states what they want right now:

> *The party is greeted by Krafton Lilifeld, the boisterous leader of House Lilifeld — the Ordani trading house famous for food production and fine cuisine. His caravan has stopped to rest, and he is excited for the opportunity to welcome the increasingly reputable adventurers. He hopes to plant the seeds of a valuable alliance … while delicately balancing the politics of revealing a new threat.*

Pattern: **identity → current state → want → complication.**

H3 headings are in-fiction names, never mechanical labels: `### The Hospitality of House Lilifeld`, `### A Test of Skill`, `### Getting Paid`. Never `### Combat`, `### Skill Challenge`, `### Rewards`. H4 beats inside social scenes are short evocative noun phrases: `#### A Warm Welcome`, `#### His True Purpose`, `#### Pressing for Details`.

---

## 4. Skill-Gated Information: The Core Template

Ember's workhorse sentence (over 1,100 uses in the corpus):

> **Any character who** [trigger action] **and makes a successful** [check] **check** [learns / determines / recalls / notices] [the fact].

Adapted to 2024 notation:

> *Any character who hears Krafton discuss the purpose of the caravan and makes a successful DC 13 Wisdom (Insight) check determines that Krafton is downplaying the danger, likely for fear of damage to his house's reputation.*

Rules:
- Always **"Any character who."** Never "a PC," never "if a player rolls," never "the characters can make."
- The **trigger action** is in-fiction ("hears Rala mention the obsidian vines," "inspects the ledger," "presses Krafton for details"). The check is gated behind something the character does.
- The result verb is specific: *determines, recalls, concurs, notices, convinces him to share.* Not "learns that" every time.
- The fact is stated **with its implication**: not just what, but what it means ("likely for fear of damage to his house's reputation").
- For "first to succeed" checks: *"the first of them to make a successful DC 15 Charisma (Persuasion) check is able to convince Krafton …"*

### Modifier ladder

Nuance goes in a bullet list directly under the check, each bullet labelled with a **bold condition**:

```markdown
Any character who presses Krafton for details and makes a successful DC 14 Charisma (Persuasion) check convinces him to share that he *"may have misspoken, in order to avoid overly worrying anyone."*

- **Character complimented House Lilifeld's reputation:** The character has Advantage on this check.
- **Character is a member of the Lords' Alliance:** The character automatically succeeds on this check.
- **Result of 20 or higher:** The character also recognizes that Krafton is undermining Rala's credibility.
```

Fixed vocabulary, in this order: **automatic success → Advantage → Disadvantage → higher-result bonus.** Ember's "critical success" rung becomes **"Result of [DC+5] or higher"** in this project (2024 ability checks have no critical success). Keep conditions concrete and checkable at the table. No "at the GM's discretion" rung.

### Check phrasing never used

- "Roll a [skill] check" addressed to players
- "The party may attempt …" (say what succeeding does instead)
- A check with no trigger action

---

## 5. Branching Language

Every branch is **committed**. The condition is crisp, and the result is stated as fact, never as possibility.

> *If the party declines all offers to travel with Krafton's caravan, Rala offers to part ways with the caravan and travel with them instead.*
> *If the party convinces him to confide about the true danger, he adds that if the party meets him in Rortwark, he may very well offer them a job.*

- Open branch paragraphs with **"If the party …"** or **"Once the party …"**
- Use **"Regardless of which path the party chooses, …"** to rejoin branches.
- Mutually exclusive openings (a greeting that depends on which prior quest the party completed) are written **in full, one block per case**, each introduced by a lead-in sentence: *"How Krafton greets the party depends on which of the Act II quests the party completed:"*. Do not merge the cases into one hedged paragraph.
- Previous choices thread forward by name: *"If the party already recovered the mud in **Death on the Vine**, …"* Ember cross-references an earlier or later event in nearly every paragraph. Do the same, with bold event names per `adventure-reloaded` callout syntax.

**Discretion.** Ember allows "at your discretion" only for flavor of execution: how a distraction looks, which minor NPC delivers a line. This project's zero-prep rule narrows it further. **Never leave outcomes, positions, timings, or rewards to discretion.** If Ember-style text would say "at your discretion," decide it in the text.

---

## 6. NPCs in Scenes

### Introduction formula

First prose mention of a named NPC in an event:

> **Name** (Alignment, Origin Species, pronouns), *appositive identity*, *who* [what they are doing or want].

> *Introduced to Captain Tyra Saulter (Lawful Good, Arcturian Human, she/her), a proud woman in ornate armor, who leads Krafton's guard and handles security for the caravan.*

Waterdeep adaptation: `Captain Staxa (Lawful Neutral, Waterdhavian Human, she/her)`. Use the NPC's Notable Figures page for alignment, species, and pronouns. Never guess them. Later mentions use the name alone.

### Descriptor before dialogue

Before any NPC speaks in a scene, one GM sentence gives their **attitude plus the reason for it**:

> *Krafton immediately offers shade and refreshments, eager to make a good impression on the party, given the reputation they have recently made for themselves.*
> *Lyla is hesitant to speak with the party for too long, lest it draw too much attention.*

Then say how to get more out of them. The **social lever** is stated as a sentence the GM can act on: *"Krafton is even friendlier to anyone who compliments House Lilifeld's reputation for fine food and good wine."*

### Topics list

Social beats list what the NPC will discuss as full-sentence bullets. Each bullet carries the fact and the NPC's slant on it. Hidden agendas are flagged inside the bullet:

> - *His caravan also intends to investigate a potential disturbance to the local environment. Secretly, however, Krafton is downplaying the danger and is hesitant to share details.*
> - *His personal life, if and only if asked, in which case he shares that he left the Ushna family home to join the Agrimage Circle.*

Follow with *"Specific dialogue for Krafton on these topics is presented below."* and then the Q&A blocks.

### Q&A blocks

Optional lore and backstory live in `[!dialogue]` blocks (see `foundry-journal`) headed as the question a player would ask: **About the caravan?**, **About House Lilifeld?**, **About Rala?** Plot-critical facts stay in GM prose or the topics list. Q&A is the skippable layer.

### Dialogue choreography

Ember interleaves speech and **one physical beat**. The beat sits between lines, in plain narration, never inside the quotation:

> > *Though if you ask me, a bit of a worrywart. Still, his heart's in the right place.*
>
> *After glancing around, Krafton leans in close to whisper conspiratorially.*

Rules:
- **One signature gesture per NPC, reused.** Krafton's is "a sly smile … and a playful wink." Pick one per NPC and repeat it across events. It is shorthand the players learn to recognize.
- **Bold marks vocal stress inside dialogue.** *"I believe **you're** the inquisitive group …"*, *"How **delightfully** controversial."* One stressed word per speech, used where the NPC would lean on it aloud. Never bold for GM emphasis inside dialogue.
- **Spaced ellipses mark pauses and trailing off** in speech: *"There's more you should know … we could really use your help."* Use sparingly, one or two per speech.
- **Broken-off words** use an em-dash: *"head of House Lil— oh, I recognize you!"*
- Speeches break into short paragraphs at each shift of thought. A long speech is split by a narration beat, not a wall of quotation.
- NPC voice is distinct: a pompous noble, a nervous apprentice, and a terse guard should be identifiable without dialogue tags.

---

## 7. Read-Aloud

`dnd-adventure-text` governs read-aloud craft. Ember adds:

- **Length.** 2–4 short paragraphs for scene openings and set pieces (80–200 words); one or two sentences for mid-scene hand-offs.
- **Opener.** Ground the scene first. A participial arrival clause is fine (*"Gathered around a natural watering hole, you spot a sprawling caravan …"*). Stock "You see" / "You find yourself" openings are not.
- **Wide shot, then the person.** Paragraph one gives the place and the crowd. Paragraph two narrows to the one NPC who matters, already doing something.
- **Smell is Ember's second sense.** Visual first, then smell or sound. Touch and taste only when they carry danger.
- **Dialogue belongs inside read-aloud.** NPCs speak within the `> [!narrative]` block, as nested `> >` quotations, interleaved with narration beats. Read-aloud is often a mini-script.
- **Close on a hand-off.** End on an NPC gesture or question aimed at the characters: *"Once he spots your approach, his eyes twinkle with delight, and he gestures you over."* / *"So, what do you think?"*
- **Plant one unexplained detail.** Mention the anomaly without comment: *"no placard or sign reveals this curious mausoleum's name or ownership."* The GM text explains it; the read-aloud does not.
- **Short mid-scene reads** break a long conversation: a single line of dialogue or a two-sentence beat, introduced by a GM lead-in (*"Before the party leaves, Krafton closes the conversation with the following offer:"*).

---

## 8. Combat Tactics

Every named combatant or monster group gets the same three-beat shape under an H4 (`#### Mud Globlin Tactics`):

1. **Opening move**, one sentence: *"To begin combat, the Mud Globlins attack Krafton's staff with Corrosive Slams."*
2. **Priorities**, a ranked bullet list introduced by *"During combat, the [creatures]:"*. Each bullet is verb-first and concrete (who they target, when they reposition, what triggers a special ability).
3. **Exit condition**, one sentence naming the exact trigger: *"The Globlins flee into the tar pit once the Mudlord is defeated or when reduced to half their number."* Or *"Krafton's guards fight to the death."*

State victory conditions under their own label. Never assume the GM infers when a fight ends.

**Dramatic Moments.** Ember paces scripted color into combat with a short list of one-time narrative beats. In this project they are **ordered, not rolled** (no dice tables): *"At the start of each round after the first, narrate the next unused Dramatic Moment in order."* Each moment is one or two sentences of read-aloud plus any mechanical effect.

---

## 9. Mechanics Woven into Prose

- **Numbers always ride on physical action.** Never "take 7 fire damage." Write *"The tar surges around the character's legs, dealing 7 (2d6) fire damage, and they must succeed on a DC 13 Strength saving throw or be Restrained."*
- **Stat block names are proper nouns.** Bold on first mention per `dnd-adventure-text`. Do not re-explain what a stat block or spell already does.
- **Rewards are staged twice: in-fiction first, mechanical second.** The NPC hands it over in narration or read-aloud, and then one flat GM sentence confirms it:
  > *Krafton removes a bottle of wine, decorated with a braided rope and a wax seal bearing the crest of House Lilifeld. … He gifts the party a sealed bottle of Lilifeld Reserve (worth 50 GP), an expensive and much sought-after trade good.*
- **Conditional rewards** name the judgment in the NPC's head: *"if he judges a party member capable of properly appreciating it, he provides some for the party to take with them."* Then say what makes him judge that (the check or the action), per zero-prep.

---

## 10. Keyed Rooms and Area Overviews

**Keyed room.** Opening prose with no heading: sensory description → the notable NPC or feature (often already speaking) → mechanics below in H4s. Lead with one or two specific details that give scale. Skip the inventory:
> *Six stone slabs decorate this room, four of which are adorned with humanoid corpses.*

Search results layer by check tier. The common find comes first, the named clue at the check, and the plot-critical detail at the higher result. Never dump every clue on one success.

**Vendor or NPC room.** An H4 per NPC: one-line physical and personality descriptor → the topics they'll discuss → wares or services → the social check that improves price or treatment.

**Area overview.** This is the driest prose in the corpus, and deliberately so. `Levels & Elevation`, `Illumination`, `Terrain`, `Inhabitants`, and `Enemies` are answered in plain reference sentences: light radii in feet, key requirements for locked doors, who is present day and night. No atmosphere and no read-aloud. Voice returns in the rooms.

---

## 11. Stock Phrases

Use these as Ember does:

| Phrase | Use |
|---|---|
| "Read or paraphrase the following:" | GM lead-in to a mid-scene read-aloud |
| "Any character who … and makes a successful …" | All skill-gated information |
| "is happy to discuss the following topics:" / "will readily discuss:" | Topics-list lead-in |
| "Specific dialogue for [NPC] on these topics is presented below." | Bridge to Q&A blocks |
| "Once the party has finished …" | Scene transition |
| "Regardless of which path the party chooses, …" | Branch rejoin |
| "fights to the death" / "flees when …" | Exit condition |
| "if and only if asked" | Gated personal detail in a topics list |

Avoid:
- "The GM should" or "the DM may wish to" (address the GM as "you," or just state the fact)
- "PCs" in prose ("the characters," "the party")
- "Players" when meaning characters
- Hedged outcomes ("might," "could possibly") in a branch result
- Balance commentary or apologies in scene text

---

## 12. Process

1. Confirm the structure from `adventure-reloaded` and the notation from `dnd-adventure-text`.
2. Draft each zone in its own voice (Section 1).
3. Open every section on the situation sentence (Section 3). Gate every discoverable fact behind "Any character who …" (Section 4).
4. Give every named NPC a descriptor, a lever, one signature gesture, and a bold-stress word (Section 6).
5. Give every combatant the three-beat tactics block (Section 8).
6. Stage every reward twice (Section 9).
7. Check the Summary is "we," past tense, 1–3 sentences.
8. Run the CLAUDE.md prose pipeline (`deslop-text` + `no-ai-slop` → `humanize-prose`). Quoted dialogue is exempt from W-codes, so Ember's ellipses, broken-off dashes, and bold stress inside quotations stay.
