---
name: ember-voice
description: >
  The Ember writing voice for ALL prose in the Waterdeep campaign: readaloud, NPC dialogue, qna
  answers, GM notes, social/exploration/hazard blocks, quest overviews, Overview and Summary text,
  lore, myths, organizations, Notable Figures, gazetteer entries, and the Players' and GM Guides.
  Measured on the Ember export, with verbatim examples, a catalogue of the AI tells that make our
  drafts sound machine-written, and a checker script. Load it before writing or revising any
  campaign prose, and before running any polish pass. Where another skill's style advice
  conflicts with this one (punchy boxed text, tricolons, short landing sentences), this skill wins.
---

# Ember Voice

The user reads our boxed text and says it is "obviously written by AI, so obvious it hurts." This skill exists to fix that. Structure lives in `adventure-reloaded` and `foundry-journal`. This skill is about **how the sentences sound**.

Ember's voice in one line: **a friendly, well-read narrator who says plainly what is there, in full and flowing sentences, and lets the characters in the story be the colourful ones.**

AI prose tries to be striking in every sentence. Ember almost never tries to be striking. It describes, it explains, it lets NPCs chatter, and the drama comes from what happens, not from the sentence rhythm.

---

## 1. The Numbers

Measured across Ember's quests, standalone events and area walkthroughs (about 470,000 words):

| Text | Avg sentence | Sentences ≤7 words | Sentences ≥30 words | Em-dashes per 1k words |
|---|---|---|---|---|
| Readaloud narration | **21** | 5% | 17% | 2.4 |
| NPC speech | **14.5** | — | — | 4.0 |
| Gamemaster blocks | 21 | 4% | 19% | 1.8 |
| Social blocks | 22 | 8% | 23% | 2.4 |
| Exploration / hazard | 21 | — | — | 1.3–1.8 |

- Readaloud block length: **median 70 words**, middle half 48–105, one in ten over 156, set pieces up to ~680.
- Contractions are normal everywhere: narration 7 per 1k words, GM text 14, speech 36.
- Bold stress inside speech is rare: 36 of 2,387 speeches.

Our AI-flavoured drafts measured 13–14 words per sentence in narration, 7–10 in speech, up to 10 em-dashes per 1k words, and a quarter of all narration sentences at 7 words or fewer.

**Check every draft with the script:**

```
python3 .claude/skills/ember-voice/scripts/voicecheck.py path/to/file.md
```

It prints each text type against the baseline and lists every tell by line. A draft is not done while it prints a `TELL` line, or while narration averages under 18 words, speech under 12, or em-dashes run over 4 per 1k words.

---

## 2. Ten Rules

1. **Say what is there.** Name the people, objects, sounds and smells in front of the characters, and what they are doing. Concrete nouns, ordinary verbs. Don't hint at what the scene *means*.
2. **Write whole sentences that flow.** Join clauses with *and, as, while, before, though*, participles and relative clauses. A short sentence is a pause between long ones, not the default. Never stack fragments.
3. **Let paragraphs zoom.** Wide shot first (the place, the crowd, the activity), then the person or thing that matters, then the speech or the detail that invites the party to act.
4. **Don't end on a punchline.** The last sentence of a paragraph is ordinary. It tells the next thing that happens or what someone does, and never delivers a verdict, a twist or an epigram.
5. **The characters are colourful; the narrator is not.** Wit, bluster, menace and charm belong to NPCs in their own speech. The narrator stays friendly and plain. Wry humour is fine in setting prose and GM asides, and it is gentle.
6. **NPCs talk like people.** Full sentences, contractions, hesitations ("Honestly,", "Well,", "I do hope…"), small talk, explanations, questions back. Nobody speaks in aphorisms or sound bites.
7. **Tag speech with an action before it.** "Agraband gestures toward the strange slab of rock and says:", "She gestures to the sky above." Tags are physical and observable. Never adverb summaries ("thoughtfully"), and never an explanation of how to read the line.
8. **State GM facts flatly and completely.** Name the secret, the person, the plan and the threshold. "The onlooker mentioned above is Serethus, leader of the Mutagists…" No teasing, no "it could be interesting if".
9. **Hedge only real uncertainty.** "Seems", "appears to", "as if" and "it is said" mark what the characters cannot know, such as another person's thoughts or disputed history. They are never there for atmosphere.
10. **Be generous with words.** Ember explains. A readaloud runs as long as the moment needs; a social block is a small script of 300–500 words; a history paragraph is 3–6 sentences. Compression is an AI habit, not a virtue.

---

## 3. The AI Tells

These patterns make a draft read as machine-written. Each has an Ember-style fix. `voicecheck.py` catches the starred ones.

| Tell | AI example (from our own drafts) | Ember fix |
|---|---|---|
| ★ Mic-drop closing line | "He presses it into the nearest open palm. That is the whole ceremony." | "He presses it into the nearest open hand and closes your fingers around it." |
| ★ "Not X, (but/more) Y" | "he raises his hands — not in surrender exactly, more in recognition of arithmetic" | "He looks down at the drop, then back at you, and after a moment he raises his hands." |
| ★ "Quietly" as a hedge | "he quietly extracted their agents" / "has been quietly reduced" / "He says this quietly, as if…" | Say what actually happened: "he pulled their agents out of Waterdeep before anyone noticed". Keep "quietly" only for real sound or stealth, as Ember does ("A few old wheel barrows rot quietly"). Ember uses it about 0.4 times per 10k words; our drafts used it five times as often. |
| ★ "Here's the kicker" / "here's the thing" / "what most people miss" | "And here's what most people miss:" | State the fact. Nobody at the table talks like this. |
| ★ Profound-but-empty abstractions | "the weight of what he has done", "a testament to", "palpable tension", "unspoken understanding", "quiet confidence" | Name the concrete thing: what he did, what the tension looks like, what they both know. Ember's adjectives are physical and checkable ("sun-bleached", "six-wheeled", "frosted"). |
| ★ Synonym triplets | "careful, patient, and deliberate" / "calm, cold, calculating" | One precise word, or two things that differ. Ember lists in threes all the time, but its three items are different things ("music, singing, and the laughter of children"). A list is fine; three near-synonyms stacked for rhythm is the tell. |
| ★ Triplets and chants | "Three alleys, three nights, three victims — and the same choice each time." | "All three alleys are off the same stretch of Ship Street, within a few blocks of the Muleskull Tavern, and each victim was alone and out well after midnight." |
| ★ Noir subtext | "something warm in it, and something more careful underneath" | "He looks at you across the table with easy warmth." |
| ★ Telling the reader how to read a beat | "He says this in a tone that politely declines to be pressed further." / "He is embarrassed that this is all he has." | Show the act: "He turns the charm bracelet over once and leaves it at that." |
| ★ Aphorisms in speech | "There's always a next one." / "A person who hasn't eaten makes poor decisions and worse company." | "There will be another one. You understand that, yes?" |
| Fragment stacks | "Consistent. Disciplined. Same corridor, same hour." | "Careful and patient, and working the same stretch of water at the same hour every time." |
| "Already" for inevitability | "already pouring", "already waiting", "already in his hand" | Describe the action as it happens. |
| "As if" portent | "as if the decision had been made before he arrived" | Cut it. Keep "as if" for a real guess at someone's intent: "As if noticing your gaze, the figure turns their shoulder and disappears." |
| Em-dash pivots | "A figure drops from above Ship Street — a drow" | "A figure drops from above Ship Street, a drow, landing without a sound." |
| Colon reveals | "The note holds one word: *settled*." | "A card on the counter says *settled*." |
| Knowing narrator | "the fraction of a degree that passes for his full attention" | "Mirt tilts his head toward whoever spoke." |
| Ominous one-line paragraphs | "He could be anywhere." / "No one mentions by whom." | Fold into the paragraph as ordinary information. |
| Every sentence the same short length | a paragraph of 8-word sentences | Two or three long sentences and one short. |

Ember itself uses "Suddenly", "Just then", "seems", "appears to" and the occasional "as if". These are not tells when they carry real uncertainty or a real surprise.

---

## 4. Readaloud

Readaloud is spoken to the players: second person, present tense, only what the characters perceive. Contractions are fine ("You've never seen…").

### Arrivals and scene-setting
Open inside the scene, on the place or the activity. Describe it generously, then narrow.

> The Strayhearth Caravan is bustling with activity as everyone prepares for the day's travel ahead. A team of wagoners readies the caravan's trio of six-wheeled wagons, attaching a hulking yarnac to each of them with tack and bridle. Travelers vie for who will get to ride on one of the mounted seats today and who will walk alongside the wagons on foot.

> Although the exterior of the Oldcraft Lodge is relatively unassuming, as soon as you step inside the main room you are immediately dazzled by a chaotic cacophony of sights and sounds. Bright yellow and pink motes of magic dance in the air, casting an enchanting glow around the space.

> A sun-bleached wooden sign hangs above the front door of this small edifice. The clinking of glass mugs and the ambling din of idle chatter can be heard beyond the establishment's frosted windows, and the earthy smells of delicious alcoholic brews waft upon the salty canal air.

If something is wrong, say so plainly:

> As you draw closer, you begin to realize something is amiss. Helkas is burning. The town is draped in smoke flowing from numerous large fires. The air is thick with the acrid stench of burning wood and cloth, and you can see people running back and forth, some carrying buckets or helping others out of harm's way.

### NPC introductions
Put the NPC in motion, give one to three sentences of appearance and manner, then let them speak.

> As the quiet evening draws on, you are joined by another member of the caravan, a Keth woman with bright blue eyes and hair like charcoal.
>
> > Hello! Having a nice evening so far?

> The tall, two-horned shadow of Ankarist falls across your face, drawing your attention back to your Drakon traveling companion, who has approached your group with an unmistakable look of curiosity on his face. His smoky voice is tinged with an accent from the west, and he wastes no time with formalities.

### Dialogue inside readaloud
An action tag, then the speech as a nested quote, then the next action. A speech can run several sentences, and a long one is split by a narration beat.

> Sin's glittering eyes turn upward again to check on the darkened sky, as they have several times over the last little while. This time, though, Sin gestures upward with a flash of excitement.
>
> > There we are, clear at last. Look, the night sky is incredible, right? I never tire of it.

### Combat openings
Start with a sense (a smell, a sound, a shape), then the danger, and let allies act and speak inside the same block.

> Suddenly you smell the stench of burning wood and cloth caught on the wind. Turning to the source, you see smoke rising between the buildings of Helkas. From all directions, raiders begin to encircle the town square.

### Discoveries
Describe the sensation or the thing itself. Interpretation belongs in the exploration block.

> As you lay your hand upon the ancient monument, the azure depths of the great crystalline orb begin to swirl within, reminding you of an aqueous, otherworldly maelstrom.

Perceived text (a note, an inscription) is a nested quote with a plain lead-in: "The translated inscription reads:".

### Endings and departures
End in motion: someone packs up, turns back to their work, or waves the party on. No verdicts.

> Lyla sighs heavily as she begins to pack up her gear for the road.

### Conditional readalouds
Introduce each one in GM prose with "If X, read or paraphrase the following:" or "read the following aloud:" (Ember uses both constantly). Write each branch in full, and don't merge branches into one hedged box.

### Length
Match the moment. A door is two sentences; an arrival is a paragraph or two; a campfire legend or a festival can run many paragraphs. Most readalouds fall between 50 and 100 words.

---

## 5. NPC Speech

- **Sentence length about 14 words**, mixed. Contractions everywhere. Ellipses for trailing off, an em-dash for an interruption.
- **Give each NPC a sentence shape**, not a gimmick vocabulary. Agraband speaks in long theatrical arcs; Ankarist in short declaratives; Sigil in fragments and non-sequiturs; the raiders in blunt boasts. The difference lives in completeness, confidence and digression.
- **They talk about ordinary things:** greetings, complaints, what they need, what they heard, asking questions back.

> Well, that's just a little worrying. I do hope he's okay. Thornlings are pretty hardy as a rule, but Edivel's the type to try a spell for flame resistant plants by charging into a bonfire. Could I ask you to search the area and see if you run into him?

> Honestly, it's not really worth talking about. Sounds much worse than it is. There have just been a few small issues. Tiny things, really. Other than the mine on Level 3 in the Dives closing, that is.

- **Bold stress is rare.** Use it at most once in an event, where the speaker truly leans on a word.
- **Keep facts in character.** An NPC who deflects does it in their own words ("You'll be paid. We can sort out the details when the work is done."), never with a clever line.

### qna answers
The question is a terse fragment ("Your trade?", "About the Harpers?"). The answer is an optional physical beat, then the NPC's words, usually 2–5 sentences. Tags describe something visible:

> A look of bittersweet remembrance crosses the old raconteur's face for a brief moment as he continues.

> A rare grin twists its way across the investigator's face.

---

## 6. GM-Facing Adventure Prose

The GM text is a colleague briefing another colleague: present tense, declarative, complete, contractions allowed. Sentences run about 21 words.

**Gamemaster's Summary** opens by classifying the event in one sentence:

> This Combat Event occurs when the town of Helkas is suddenly attacked by afflicted drakes and a band of raiders during the Dusktide Festival.

**Secrets are named outright**, and closed off when the party can't learn them:

> The onlooker mentioned above is Serethus, leader of the Mutagists and one of the innermost circle of Zerranyss' malevolent cabal. He orchestrated the attack against Helkas as a field test of the mutagen being developed in the Repurposed Quarry laboratory.
>
> It is impossible for the party to learn any of these connections at this time.

**Bridge prose** between blocks is one or two plain sentences saying who is where and what happens:

> The party, joined by Lyla Cevher, faces a sortie of nine raiders, one of whom is their leader: Bassa, "the Firebug".

**Social blocks** open with behaviour as it looks now, then give topics, checks and levers:

> Ankarist initially appears serious, aloof, and reserved. He stands out as a Drakon, and keen-eyed characters can note an accent and mannerisms that betray his origins. It should feel obvious to the party through these initial interactions that there is a lot more to Ankarist that isn't overtly apparent.

> Agraband is a friendly, chatty, and gregarious sort, always happy to talk about something, especially if it's his stories and adventures.

**Exploration** uses the fixed formula and gives the finding specifically, sometimes adding a line of what the character senses:

> Any character that examines a dead drake's corpse and makes a successful DC 13 Wisdom (Medicine) check reveals that this creature appeared to have been exceedingly ill during its life. It was likely in constant pain, and functionally, if not entirely, blind. You've never seen any kind of illness like this before.

**Hazard tactics** give exact numbers and triggers:

> If at least 6 of the Otherhood Raiders are killed, the survivors will attempt to flee, but they will not surrender if cornered. They will also attempt to flee if Bassa is slain.

**Discretion comes with its principle** ("you should calibrate the timing to apply the right amount of pressure to the party based on how they fared during the battle with the drake"). Under this project's zero-prep rule, outcomes, positions and rewards are always decided in the text.

**Next Steps** states the transition as fact and names every branch:

> Lyla proceeds to Arcturel. If the party goes with her, they trigger the next Event. If they go elsewhere, she will travel with them as long as they don't go too far off course, but may eventually return to her original route.

**`## Overview`** is one or two plain present-tense sentences in the third person:

> The party journeys to the Dives to investigate the scene of the Renegade Construct's purported crime. While exploring the Dives district, the characters encounter witnesses to the accident, including agitated House Cevher miners and an intuitive inkaro lamplighter.

**`## Summary`** is the party's journal: "we", past tense, plain, sometimes closing on a real open question:

> We helped defend Helkas from a tandem assault, first by mutated drakes, and then by a group of fire-wielding raiders intent on pillaging and burning the town to ashes. Where did these strange drakes come from? Who could have wished harm on this peaceful Arcturian town?

**Quest backstory** gives the hidden cause first ("Unknown to all but the head of the Agrimage Circle, the secret to their magical topsoil is a compact established a millennia ago…"), then the visible effect.

---

## 7. Setting and Guide Prose

The sentences are longer here, 25–35 words, and the tone is serious non-fiction: elevated but never archaic ("bitterly divided", "dogged attrition").

**History** opens on scope and dates, then complicates:

> The Forsaken War stands as the first truly global conflict in the history of the surface world, a war of such staggering scale that it defies belief. Occurring roughly eight thousand years ago, it pitted the Aedir against the ancient, predatory dominance of creatures known as the Theroch. However, the war has largely drifted into the realm of myth.

- Each paragraph has 3–6 sentences and develops one consequence.
- Named people act; adjectives come through their actions.
- Present tense for standing truths, past tense for events.
- Player text hedges disputed facts ("Scholars remain bitterly divided…"). The GM note states the truth, or admits that no one knows it.

**Myths** are told as plain summaries, not in archaic performance:

> In the legend, Isota, a Knight of Verador kills a Cruel Dragon in the forests of Vanthar. The story goes that the Dragon inhabited the mountains nearby and would regularly fly across the area, attacking the villages and peoples indiscriminately.

The lyrical register belongs only to an attributed in-world quote. Variant versions go in footnotes, and scholarly doubt goes in the Overview.

**Organizations** open on purpose and character, and give tenets as bold lead-ins followed by full sentences:

> At its core, the Veiled Chain aims to protect Ordain from threats by investigating problems before they become crises. Its agents are expert fact-finders and investigators hand-picked from the best and brightest the city has to offer.

Each Key Member gets a name line and 2–3 sentences, role first:

> An expatriate from the Tayan empire, Ankarist has become a respected member of the Chain after years of dedicated service. Known for their physical prowess as much as mental, they often handle cases with heightened levels of danger that less sturdy agents avoid.

**Notable Figures** are written in full sentences with a dry, gentle humour:

> Despite his brilliance, he was also said to be a cantankerous, lecherous, and thoroughly dislikable character who often clashed with other members of the Anachraenum. He was famously short of temper and spent the last few years buried so deeply into his books it was little surprise to anyone when he was found quite dead amidst a mountain of books.

**Gazetteer** entries open on the defining feature, study the culture the way an anthropologist would, and let the richest description sit in Culture and Lore:

> Suspended directly over the yawning depths of the sinkhole, the main district of Arcturel is a breathtaking engineering marvel of gravity-defying architecture.

> Status is visually defined by how far from the edge, and how high a home or business can be built, creating a literal social hierarchy.

> Here, columns of old Arcturian stone quarried centuries ago meet the new lines of modern Ordani aesthetic, with seams between these architectural movements masked or accented by ever-changing murals contributed by local artists.

To correct a legend, state the claim, then the truth: "It's said that…. This is partly true, but…".

**Players' Guide** uses warm second person ("Your party will…"), bolds a term where it is defined, and is confident without apologising:

> Ember is not part of some vast multiverse; it is the only plane or dimension in existence.

**GM Guide** is direct rules prose ("Each event has a number of properties and characteristics that determine its behavior."), says "we recommend", admits candidly where a system is rough, and pivots with "Unfortunately," "In fact," or "Still,". It explains villains as plans, not odes:

> Vinarith does not come across as a villain; in fact, he could be roleplayed as an earnest and hardworking man.

---

## 8. Waterdeep Before and After

**Readaloud**

AI draft:
> The tailor on Delzorin Street opens before you knock. The fittings take perhaps twenty minutes; the garments are already cut, already waiting. A card on the counter reads: *settled*. No one mentions by whom.

Ember voice:
> The tailor on Delzorin Street has the door open before you reach it, and a pair of assistants are waiting with pins and chalk. The fittings take about twenty minutes, and the garments fit well enough that they must have been cut from a description of you. When you ask about the bill, the tailor slides a card across the counter with *settled* written on it and doesn't say who paid.

**NPC speech**

AI draft:
> "Consistent. Disciplined. Same corridor, same hour, isolated targets — that's preparation, not opportunity."

Ember voice:
> "Whoever this is, they're careful. They've worked the same stretch of Ship Street at the same hour every night, and they've waited each time for someone walking home alone. That takes planning, and it takes patience. It's why I'd rather not leave it to the Watch."

**GM prose**

AI draft:
> He is precise about the facts and warm about the party — not sycophantically, but with the ease of someone who has sized people up for a living.

Ember voice:
> Davil is precise about the facts and warm toward the party, with the easy manner of someone who sizes people up for a living and likes what he sees.

---

## 9. Precedence and Polishing

- This skill **overrides** the following, wherever they apply to campaign prose:
  - `humanize-prose`: its "punchy" boxed text of 2–4 sentences and its "short punches"
  - `deslop-text` W29: its "three-word sentence after a complex one"
  - `ttrpg-sourcebook-style`: its tricolon with escalation, and its short punchy sentence after an accumulation

  Those skills still catch real AI patterns. Their rhythm advice pulls toward the voice the user rejected.
- `dnd-adventure-text` keeps authority over check, damage and condition notation.
- `ember-adventure-style` and `ember-setting-style` keep authority over zone rules, formulas and entry shapes.
- Quoted dialogue is character voice. Ellipses, interruptions and contractions stay.

## 10. Process

1. Before drafting, read two or three Ember passages of the same type (Section 4–7 excerpts, or the export at `01 - Ember.zip`).
2. Draft generously, following the ten rules.
3. Run `voicecheck.py`. Fix every `TELL`. Bring sentence averages and em-dash rates within range.
4. Read each paragraph's last sentence. If it sounds like the end of a chapter, rewrite it as the middle of one.
5. Read each NPC's lines aloud. If a line would look good on a poster, rewrite it as something a person says.
