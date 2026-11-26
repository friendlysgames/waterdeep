# Pass 6 research notes: Squiddly

Page: `campaign/setting/notable-figures/trollskull-community/14-squiddly.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. The sources give Squiddly no fixed day-one address (see Ches 1 placement).
Organization page: none. Factions Guide: none. Villains page: none.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 241 to 255 ("### Squiddly").
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/11-lif.md`
Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-trollskull-community/14-squiddly.txt`. Citation key WDH5e-p63. The wiki prints no edition on most lines. The wiki's Trollskull quote is from the video game *Idle Champions of the Forgotten Realms*, not a published Dragon Heist text.

## Method and caveats

- Campaign files: Grep and Read. Quotes copied from tool output.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string with escapes removed. Tags left as written.
- Alexandrian: `sources/Appendix_D_-_Running_the_Tavern.md` (line 1184, Event 18). The Appendix D markdown has no Squiddly patron profile (see Not found).
- Not readable: `sources/Other remix files/The 3 Urchins NPC Guide.docx` (see Not readable).
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **Squiddly is the most-scripted of the three in the sources.** The adventure has him on the apple cart (`sources/adventure-wdh.json:7099`), throwing a snowball (`:7625`), kidnapped by the kenku (`:9606`), and kicking the kenku (`:9616`). Bregan D'aerthe's standalone event has him as a witness (`campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:49`).
2. **"Featured in: Background figure; no scripted appearance" is contradicted** (see D1).
3. **"neutral good" and "Commoner" have no source**, as for Nat and Jenks.
4. **"sleeping in the tavern kitchen for weeks" and "the party their most exciting neighbors" are post-opening events** (see C and D3). The random event is Appendix D's Event 18 (`sources/Appendix_D_-_Running_the_Tavern.md:1184`).

---

## A. Background facts by theme

### A1. Origin, age, ethnicity, family, and the group

**Adventure, The Three Urchins sidebar (page 63)**
> "Three street urchins, described below, appear in several of this chapter's scenes: {@b Nat} is a lanky, 10-year-old deaf Illuskan girl with a wooden toy sword. She is the leader of the group and communicates using a sign language that she invented and taught to her friends. {@b Jenks} is a portly 9-year-old Turami boy with a cloak, a toy wand, and a stuffed owlbear \"familiar.\" He's shy around strangers but brave when it comes to helping his friends. {@b Squiddly} is a slim 9-year-old tiefling boy with an eye patch, a small bow, and a quiver of toy arrows. He rarely thinks before he talks or acts."
> — `sources/adventure-wdh.json:7133`

**Wiki, infobox (WDH5e-p63)**
> "| sex            = Male<ref name="WDH5e-p63">{{Cite book/Waterdeep: Dragon Heist|63}}</ref>" — wiki line 12
> "| race           = [[Tiefling]]<ref name="WDH5e-p63" />" — wiki line 13
> "| age            = 9 in [[1492 DR]]<ref name="WDH5e-p63" />{{WDH-time}}" — wiki line 16
> "| dob            = 1483" — wiki line 20
> "| alignment5e    = " — wiki line 56 (blank)
> "| class5e        = " — wiki line 58 (blank)
> "| ethnicity      = " — wiki line 14 (blank)

**Wiki, Description (WDH5e-p63)**
> "Squiddly had a slender build. He had red skin, a long tail, and the horns common of tieflings. His left eye was covered by a black eye patch." — wiki line 66

**Wiki, Personality (WDH5e-p63)**
> "He was impulsive, rarely thinking before acting." — wiki line 69

**Wiki, Possessions (WDH5e-p63)**
> "Squiddly wore an eye patch and carried a small [[bow]] and a [[quiver]] with a handful of toy [[arrow]]s." — wiki line 72

**Wiki, Relationships (WDH5e-p63)**
> "Squiddly was part of the group of street urchins that included his friends [[Nat]] and [[Jenks]]. He communicated with the [[deaf]] Nat using a sign language Nat had invented." — wiki line 76

**Wiki, the Idle Champions quote (a video game line, not a Dragon Heist text; wiki line 63)**
> "Squiddly's my name, and I'll be your guide to Trollskull Alley today, all for the low price of 5 nibs." — wiki line 63 (source: *Idle Champions of the Forgotten Realms*)

### A2. Temperament, habits and manner

**Adventure (sidebar, see A1)**: "He rarely thinks before he talks or acts." (`sources/adventure-wdh.json:7133`)

**Adventure, the apple cart (quest-time scene; the boy is Squiddly by description)**
> "Riding on the cart is a tiefling boy with an eye patch, screaming at the top of his lungs. \"Look out!\" he shouts." — `sources/adventure-wdh.json:7099`
> "The boy is one of three street urchins who teamed up to steal the apple cart from a nearby street corner." — `sources/adventure-wdh.json:7103`

**Adventure, the snowball (quest-time; "Squiddly even has the audacity")**
> "{@creature Squiddly|WDH} even has the audacity to hurl a snowball at one of them ({@hit 0} bonus to hit)." — `sources/adventure-wdh.json:7625`

**Adventure, the kenku tower (quest-time; the dare and the kick)**
> "Just prior to the kenku's arrival, three children entered the derelict tower on a dare." — `sources/adventure-wdh.json:9605`
> "If the characters and the kenku reach an impasse, {@creature Squiddly|WDH} kicks the kenku in the shin, causing it to release him, and hides under some old furniture." — `sources/adventure-wdh.json:9616`

**Voice profile (the campaign's voice, not a source)**
> "- **Sound:** A high, loud, excited voice, always slightly out of breath." — `.claude/skills/character-voices/voices/trollskull-community.md:244`
> "- **Personality in speech:** Reckless excitement and loyalty. He volunteers for everything before anyone has explained it. He's briefly surprised when things go wrong, then just as excited again." — `.claude/skills/character-voices/voices/trollskull-community.md:248`
> "- **Never:** He never backs down from a dare, never admits he was scared, and never leaves Nat's side for long." — `.claude/skills/character-voices/voices/trollskull-community.md:251`

### A3. Relationships to other named figures

**Adventure (sidebar, see A1)**: Squiddly is part of the group with Nat and Jenks (`sources/adventure-wdh.json:7133`).

**Adventure, the kidnapping (quest-time)**
> "The kenku has kidnapped {@creature Squiddly|WDH} and taken him upstairs ({@area O3|1ac})." — `sources/adventure-wdh.json:9606`

**Adventure, Fenerus and the children (the children know him)**
> "If they are asked about Fenerus, the children know who he is." — `sources/adventure-wdh.json:7104`

**Bregan D'aerthe standalone event (Squiddly as a witness; quest-time)**
> "A member who asks around the alley and makes a successful DC 11 Wisdom (Perception) or Charisma (Persuasion) check learns that Squiddly watched the step from the kitchen window. On a failure, Squiddly asks for a copper before he says so, and the member can pay it without a check." — `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:49`
> "Squiddly is used from **Trollskull Alley** without a voice line." — `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/design-notes.md:21`

### A4. Time in post and place

- No source gives a home, a parent or a guardian for Squiddly.
- The wiki gives "dob = 1483" (wiki line 20) with "age = 9 in [[1492 DR]]" (wiki line 16).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page summary: "> - *Tiefling street urchin, neutral good, he/him*. Stat block: **Commoner**." — `campaign/setting/notable-figures/trollskull-community/14-squiddly.md:5`
- Adventure, wiki, Appendix D: no alignment for Squiddly. Wiki alignment5e blank (wiki line 56).
- Result: "neutral good" is unsourced.

**Species**
- Page summary: "Tiefling street urchin" (`14-squiddly.md:5`).
- Adventure: "a slim 9-year-old tiefling boy with an eye patch" (`sources/adventure-wdh.json:7133`).
- Wiki: "| race           = [[Tiefling]]" (wiki line 13).

**Pronouns**
- Page summary: "he/him" (`14-squiddly.md:5`).
- Adventure: "a slim 9-year-old tiefling boy" and "He rarely thinks before he talks or acts." (`sources/adventure-wdh.json:7133`).
- Wiki: "| sex            = Male" (wiki line 12).

**Stat block**
- Page summary: "Stat block: **Commoner**." (`14-squiddly.md:5`).
- Adventure: "These noncombatants are named Nat, Jenks, and Squiddly" (`sources/adventure-wdh.json:9605`); no stat block.
- Wiki: class5e blank (wiki line 58). Result: "Commoner" is unsourced.

---

## C. Quest-time sentences on the current page (routed; not day-one)

Current page: `campaign/setting/notable-figures/trollskull-community/14-squiddly.md`. Sections: Gamemaster's Summary, Roleplaying Information (Resonance, Emotions, Motivations, Inspirations), Character Information (Persona, Morale, Relationships), Overview.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L7 | "> - **Featured in:** Background figure; no scripted appearance." | Conflicts with the adventure (see D1) | `sources/adventure-wdh.json:7099`; `:7625`; `:9606`; `:9616`; `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:49` |
| 2 | L21 | "To the world, Squiddly is a nine-year-old tiefling with a leather eye patch who has never met a dare he would refuse." | "nine-year-old", "tiefling", "eye patch" are sourced (`sources/adventure-wdh.json:7133`). "has never met a dare he would refuse" is campaign wording; the adventure's "on a dare" is group habit (`:9605`) | `sources/adventure-wdh.json:7133`; `:9605` |
| 3 | L21 | "To those he trusts, he is the one who volunteers first, asks questions never, and assumes everything will work out." | Campaign; the voice profile gives "volunteers for everything" (`.claude/skills/character-voices/voices/trollskull-community.md:248`) | none in the adventure |
| 4 | L23 | "**Morale.** In a fight, Squiddly fires toy arrows, shouts insults, and keeps going until Nat physically removes him from the situation." | "fires toy arrows" is sourced as a possession (`sources/adventure-wdh.json:7133`). "until Nat physically removes him" is campaign. The adventure's fight behavior is quest-time | `sources/adventure-wdh.json:9616` (kicks the kenku, hides under furniture) |
| 5 | L25 | "**Relationships.** Squiddly is the most enthusiastic member of the trio, an increasingly devoted fan of the party, and the primary reason Nat has developed such excellent contingency plans." | "an increasingly devoted fan of the party" is quest-time (the party relationship builds during play). Route. The contingency line is campaign | Party relationship: `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:49` (Squiddly watches the Trollskull step) |
| 6 | L29 | "Squiddly is a nine-year-old tiefling street urchin with a leather eye patch who treats every situation as an opportunity for something impressive; he and his two companions have been sleeping in the tavern kitchen for weeks and consider the party their most exciting neighbors yet." | "sleeping in the tavern kitchen for weeks" is a post-opening random event (Event 18). "consider the party their most exciting neighbors" is quest-time (the party as neighbors). Route both | `sources/Appendix_D_-_Running_the_Tavern.md:1184`; `campaign/guides/trollskull-manor/07-events.md:36` |

### C2. Where Squiddly's quest-time facts already live (routed)

- **Adventure, the apple cart (the tiefling boy, Alley scene)**: "A cart laden with apples comes careening toward you from the opposite direction, rolling downhill. Riding on the cart is a tiefling boy with an eye patch, screaming at the top of his lungs. \"Look out!\" he shouts." — `sources/adventure-wdh.json:7099`. "The tiefling boy is thrown from the cart but not seriously hurt." — `sources/adventure-wdh.json:7102`
- **Adventure, Ice Escapades (the snowball)**: "{@creature Squiddly|WDH} even has the audacity to hurl a snowball at one of them ({@hit 0} bonus to hit)." — `sources/adventure-wdh.json:7625`
- **Adventure, the Trolltide kenku tower**: "The kenku has kidnapped {@creature Squiddly|WDH} and taken him upstairs ({@area O3|1ac})." — `sources/adventure-wdh.json:9606`. "The kenku clutches the {@item Stone of Golorr|WDH} in one clawed hand and {@creature Squiddly|WDH} the tiefling in the other." — `sources/adventure-wdh.json:9615`. "If he has a clear path to the stairs, {@creature Squiddly|WDH} runs down them and rejoins his friends." — `sources/adventure-wdh.json:9617`
- **Adventure, the Trolltide and autumn captions**: "{@creature Nat|WDH}, {@creature Jenks|WDH} and {@creature Squiddly|WDH} enjoy a windy autumn day on the docks" — `sources/adventure-wdh.json:26678`; "{@creature Nat|WDH}, {@creature Jenks|WDH} and {@creature Squiddly|WDH} make the best of Waterdeep's harsh winter" — `sources/adventure-wdh.json:30397`
- **Bregan D'aerthe s01 Coin Pouches (quest-time witness)**: "Squiddly watched the step from the kitchen window." — `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:49` (the full sentence is in C1 row 5's cross-reference)
- **Appendix D, Event 18**: "The Three Urchins (Nat, Jenks, and Squiddly) have somehow gotten into the tavern after hours and are sleeping in the kitchen." — `sources/Appendix_D_-_Running_the_Tavern.md:1184`
- **Trollskull Manor guide, Event 18**: "| 18 | The Three Urchins (Nat, Jenks, Squiddly) have gotten into the tavern after hours and are sleeping in the kitchen. | Roleplay. |" — `campaign/guides/trollskull-manor/07-events.md:36`
- **Wiki, the Stone of Golorr entanglement (quest-time)**: "In the late 15{{th}} century DR, Squiddly and his friends were unwittingly entangled in the city-wide hunt for the ''[[Stone of Golorr]]'', sometimes innocently helping or hindering the efforts of adventurers in retrieving it." — wiki line 79
- **Wiki, the Vault of Dragons gallery (a future quest scene)**: "Nat, Squiddly, and [[Aurinax]] in the [[Vault of Dragons]]." — wiki line 113 (edition not tagged)
- **Wiki, the giants gallery (quest-time)**: "Squiddly, Nat, and Jenks wandered through the wrong door in Waterdeep and a met a trio of friendly [[giant]] youths." — wiki line 114 (edition not tagged)

---

## D. Conflicts

**D1. "Featured in" (no scripted appearance)**
- Page: "> - **Featured in:** Background figure; no scripted appearance." (`14-squiddly.md:7`)
- Adventure: "Three street urchins, described below, appear in several of this chapter's scenes" (`sources/adventure-wdh.json:7133`); Squiddly is in `:7099`, `:7625`, `:9606`, `:9615`, `:9616`, `:9617`.
- Bregan D'aerthe: "Squiddly watched the step from the kitchen window." (`campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:49`)
- Higher ranked: the adventure, and the campaign's own s01 event. Flagged for the orchestrator.

**D2. Alignment and stat block**
- Page: "neutral good" and "Commoner" (`14-squiddly.md:5`). Unsourced. Not a conflict.

**D3. The tavern kitchen and "neighbors"**
- Page: "sleeping in the tavern kitchen for weeks" and "consider the party their most exciting neighbors yet" (`14-squiddly.md:29`).
- Appendix D: Event 18 (`sources/Appendix_D_-_Running_the_Tavern.md:1184`), tavern-time, begins after the party opens.
- Result: a day-one "for weeks" is not sourced. The party-as-neighbor line is quest-time.

**D4. Stone entanglement and "no scripted appearance"** — see D1. The wiki entanglement (wiki line 79) is a quest-time history, not a day-one fact.

---

## E. Stale lines in other files (not edited) and routed references

- `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/design-notes.md:21`: "Squiddly is used from **Trollskull Alley** without a voice line." Routed; not edited.
- `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:49`: Squiddly's witness scene. Routed to the Bregan D'aerthe quest.
- `campaign/guides/trollskull-manor/08-notable-patrons.md:22`: unnamed urchin shoplifting (see the Nat notes).

---

## F. Gaps a Background would need that no source gives

1. **Home, family and guardian.** No source. Wiki: "| parents        = " (blank), "| siblings       = " (blank) (wiki lines 29 and 31). No adult named.
2. **Where he sleeps day one.** No source. See the Nat notes.
3. **Why he has an eye patch.** Sourced as a fact: "a slim 9-year-old tiefling boy with an eye patch" (`sources/adventure-wdh.json:7133`); wiki: "His left eye was covered by a black eye patch." (wiki line 66). No source gives an injury or a cause. Do not invent one without `[design]`.
4. **Tiefling heritage.** Sourced as species only. No source gives a parent or a patron.
5. **Pirate talk and the bow.** The voice profile's "Pirate talk because of the eye patch" is campaign voice (`.claude/skills/character-voices/voices/trollskull-community.md:246`). The bow and arrows are sourced (`sources/adventure-wdh.json:7133`).
6. **Alignment and faith.** No source.
7. **Impulsiveness.** Sourced: "He rarely thinks before he talks or acts." (`sources/adventure-wdh.json:7133`); wiki: "He was impulsive, rarely thinking before acting." (wiki line 69). The campaign's "decided thinking is the problem" line is campaign-only.

---

## G. Inner-life hints in the sources (exact quotes)

- **Impulsiveness.** "He rarely thinks before he talks or acts." — `sources/adventure-wdh.json:7133`; "He was impulsive, rarely thinking before acting." — wiki line 69.
- **Loyalty to his friends (the kick).** "{@creature Squiddly|WDH} kicks the kenku in the shin, causing it to release him" — `sources/adventure-wdh.json:9616` (quest-time).
- **Loyalty (the group's run).** "If he has a clear path to the stairs, {@creature Squiddly|WDH} runs down them and rejoins his friends." — `sources/adventure-wdh.json:9617` (quest-time).
- **Dares.** "three children entered the derelict tower on a dare." — `sources/adventure-wdh.json:9605`.
- **Admiration of adventurers.** "{@creature Squiddly|WDH} even has the audacity to hurl a snowball at one of them" — `sources/adventure-wdh.json:7625`; "The children fancy themselves adventurers of sorts, and they are quick to idolize and emulate real-life ones." — `sources/adventure-wdh.json:7625`.
- **Bravado (the Idle Champions line).** "Squiddly's my name, and I'll be your guide to Trollskull Alley today, all for the low price of 5 nibs." — wiki line 63 (video game).
- **Shopping for the group (quest-time).** "The boy is one of three street urchins who teamed up to steal the apple cart" — `sources/adventure-wdh.json:7103` (a theft, quest-time).

---

## Ches 1 placement (what the campaign and the sources place, day one)

- **Ward**: no source names Squiddly's ward on day one. The Dock Ward and Mistshore scenes are quest-time (`sources/adventure-wdh.json:7624`).
- **Street**: none on day one. The apple-cart alley is unnamed (`sources/adventure-wdh.json:7083` to `:7105`).
- **Trollskull Manor**: the kitchen window is a quest-time witness setting (`campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:49`).
- **Drafter**: write no day-one address for Squiddly. Keep `[research]` on any district.

---

## Not found

- **Squiddly's alignment and stat block** in the adventure, the wiki, Appendix D and the guides. Searched for "alignment", "neutral good" and "Commoner" near his name.
- **Squiddly's home, parents or guardian** in the adventure, the wiki and the research bundles (searched for "Squiddly" with "home", "parent", "mother", "father", "live").
- **Squiddly in the Alexandrian PDFs**: the Appendix D markdown has no Squiddly patron profile (grep of `sources/*.md` for "Squiddly" finds only the Event 18 line and the Appendix D Event table). The PDF was not searched for Squiddly beyond the pages read for Lif (see 11-lif.md, Method).
- **Squiddly in the Trollskull Alley quest files**: grep of `campaign/quests/act-i/trollskull-alley/` for "Squiddly" returns no match.
- **Squiddly in the faction quests**: only `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/` names him (grep of `campaign/quests/`).

## Not readable

- `sources/Other remix files/The 3 Urchins NPC Guide.docx`: named by `sources/SOURCE_GUIDE.md:694` ("Nat, Squiddly, and Jenks — personalities, street knowledge, quest hooks, how to use them as recurring contacts"). Not readable with the tools. Extract before the Background is final.
