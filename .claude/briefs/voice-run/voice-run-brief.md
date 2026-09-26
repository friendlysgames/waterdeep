# Brief: the Faction Events voice run

The user approved the two pilots and asked for "the voice run on all faction events". Each file in your batch gets brought up to the pilot standard: Ember's block model, Ember's plain narrative voice, every NPC speaking in their profile voice, and the density the user asked for.

## Gold standard (read both in full first)
- `campaign/quests/faction-events/harpers/00-first-meeting/ev-01-first-meeting.md`: a social event.
- `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md`: a mission event that opens with **The Brief**, followed by investigation and combat.

Match how they are built and how they sound.

## Read before writing
1. `CLAUDE.md`. Its standing rules override everything.
2. `.claude/skills/ember-voice/SKILL.md`: how every sentence sounds (targets, tells, voice per block).
3. `.claude/skills/character-voices/SKILL.md`, plus the `voices/*.md` doc for **every** named Notable Figure who speaks in your files. Use Grep to find their profiles. Every quoted line is written in that profile's voice, including their Swearing rating.
4. `.claude/skills/adventure-reloaded/SKILL.md`: the sections Block Types, Shorthand Syntax, File Type Specifications (Quest Overview, Event File) and Scene Writing Voice (including readaloud density and "Missions open with the brief").
5. `.claude/skills/foundry-journal/SKILL.md`: the block shorthand.

## Per file type

### Event files (`ev-*.md`)
Convert to the Ember event page shape, in this order:
1. `# Title`
2. `> [!gamemaster]**Gamemaster's Summary**`: "This [Social/Exploration/Combat] Event occurs when… In this Event, the party can:" plus bullets. Extra GM guidance goes under `#### Sub` lines.
3. `### Scene` sections. Each has 1–2 sentences of plain GM framing, then its blocks.
4. `### Concluding the Event`: short prose, then `> [!gamemaster]**Event Outcomes**` ("Mark each outcome that occurs. Later events read them." and `- **Exact Old Flag Name** — mark when…; read by…`), then `> [!gamemaster]**Next Steps**`. Faction events award no Milestone.
5. `## Overview`: 1–2 player-safe sentences.
6. `## Summary`: "We…", past tense, 1–4 sentences.

Conversion rules:
- **Blocks.** Use only these six: `[!readaloud]` `[!gamemaster]` `[!social]` `[!qna]` `[!exploration]` `[!hazard]`. Blocks sit at top level, never nested, with a blank line between them.
  - Retire every old sidebar and GM zone. `[!narrative]`, `[!npc-narrative]` and `[!dialogue]` go, and so does `[!profile]`/`[!design]`/`[!lore]`/`[!info]`/`[!warning]`/`[!combat]`/`[!tip]`/`[!item]`, and every `> **[GM]**` zone.
  - `[!design]` rationale moves to the folder's `design-notes.md` if one exists; otherwise it becomes a short `[!gamemaster]` note.
- **Delete `## Read Aloud`.** First move any real scene narration it holds that the body lacks into the right scene as a `[!readaloud]`.
- **Density.** Match the pilots:
  - Every beat the players experience gets a `[!readaloud]`: arrivals, NPC entrances, reveals, turns of a fight, discoveries, departures.
  - NPCs speak verbatim wherever the text currently *describes* what they say.
  - Every `[!social]` block is followed by a run of `[!qna]` blocks with terse questions.
  - Every branch outcome gets its own conditional readaloud, introduced by "If X, read or paraphrase the following:".
  - Checks that reveal something end with a nested `> >` quote of what the character perceives.
- **Social blocks.** Open with `Name (Alignment, Ancestry, pronouns) :: one-line summary`. **Copy alignment and ancestry from the character's Notable Figures page (`campaign/setting/notable-figures/`, whose Gamemaster's Summary gives them in the first bullet). Never guess them.** A batch shipped Melannor as "Lawful Good, Wood Elf"; he is Neutral Good, Half-Elf. For NPCs without a page, use what their mission files say.
- **Hazard blocks.** Use Ember's tactics wording: "At the start of combat… Over the course of combat, X will prioritize… The battle ends when…". Give exact thresholds.
- **Outcomes.** Every old `#### X: True / False` becomes an Event Outcome with the **exact same name**, and keeps its "read by" references.

### A mission's first event gets `### The Brief` as its first scene
This applies to the first `ev-01` in every `m0N` folder. The faction contact gives the party the job, in the place and manner the mission's `overview.md` says. The scene contains:
- one line of GM framing
- a `[!readaloud]` of the meeting, with the brief as the contact's verbatim speech in their profile voice
- a `[!social]` block for the contact
- `[!qna]` blocks for the obvious questions: who, why us, what do you know, where do we start, the pay
- a pointer into the next scene

Use only facts in the mission's files. If the pay isn't stated, the contact deflects in character.

If the contact briefs by message rather than in person, **The Brief** is the message arriving, written as a readaloud with the message verbatim. Examples: Tashlyn's flying snake (two or three words), Vajra's *Sending* (exactly 25 words), Melannor's cat or pigeon, Remi's silver raven. In that case, add qna only if someone is present to ask.

Standalone (`s0N`) and rank (`r03/r10/r25/r50`) events are not missions, so they get no Brief scene.

### `overview.md` (mission and event overviews)
Convert to Ember's quest overview shape:
1. `> [!gamemaster]` block with `#### Quest Requirements` / `#### Difficulty` / `#### Milestone Overview` ("This mission does not award a Milestone Point.")
2. Backstory paragraphs (GM), with the hidden cause first
3. `## Involved Characters`
4. `## Dangers & Enemies`
5. `## Overview` (player-safe)

Everything is written in `ember-voice` GM register.

### `design-notes.md`
Keep the structure. Revise the prose to `ember-voice` (plain, flowing, no tells). Absorb any `[!design]` content moved here from events.

## Voice
- **Narration and GM prose** follow `ember-voice`: narration averages about 21 words a sentence, GM prose about 21. Plain and literal, with no mic-drops, "not X, more Y", triplets, noir subtext, "quietly" as a hedge, or "the weight of". Don't game the averages with run-ons.
- **NPC speech** follows `character-voices`, averaging about 14 words a sentence overall. Terse characters stay terse.
- **Profanity.** The players are adults. NPCs swear exactly as their Swearing rating says, using real words, with no euphemisms and no "he curses" summaries. Spend a Tirade at most once, and only where the moment earns it. Narration never swears.
- **NPCs without profiles** (dock workers, guards, servants) talk like ordinary Waterdhavians of their trade and class, and each one sounds distinct.

## Content rules (hard)
- **Keep every DC in its standard form** ("DC 14 Wisdom (Perception)", "a DC 14 Passive Perception"), never paraphrased.
- **Keep every fact.** Every fact, DC, damage figure, stat block name, number, name, link, cross-reference and outcome stays. Don't add plot facts: no invented names, pay figures, durations or relationships. Colour details are fine if they add nothing load-bearing.
- **Cassalanter secrecy.** No faction or NPC knows the Cassalanters are infernalists before the party discovers it. The Order of the Gauntlet hunts diabolists **in general** and only *suspects* the Cassalanters of hiding something, because they're too generous and too perfect. Nothing in Order text, speech or GM framing points at the family being infernal until the party itself finds the evidence (**The Shrine on Aveen Street** is where the party discovers the Cassalanter link). Fix any line that breaks this, and list each fix in your report.
- **The Wazoo exposé (BD Mission 2)** now alleges only that an unnamed Sea Ward family hides enormous gold purchases behind its charities, and that servants who asked questions vanished. Jarlaxle and Nar'l *suspect* the Cassalanters; they don't know about any infernalism. Later missions that reference the exposé or Jarlaxle's intelligence chain keep to that. Jarlaxle builds suspicion, and the party makes the discovery.
- **Bregan D'aerthe rejects Lolth.** No BD member worships Lolth, keeps a shrine to her or invokes the Spider Queen with devotion. They speak of her with contempt, as the goddess they left. Fix any line that breaks this.
- **Two Zhentarims.** Manshoon's splinter and Davil's Doom Raiders are separate organisations; never conflate them.
- **Units and labels.** Use tendays, never weeks, in-world. Threestrings is a Harper.
- **Stat blocks.** Keep them as written. Soluun is a Scout with a hand crossbow in DR Mission 1.
- **No commits.** Don't touch files outside your batch.

## Report (keep it short)
Per file:
- blocks created, by type
- outcomes defined
- Brief scene added (yes/no, and who)
- anything moved to design-notes
- secrecy fixes
- anything you were unsure of or couldn't verify
