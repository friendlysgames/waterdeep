# Pass 6 research notes: Nat

Page: `campaign/setting/notable-figures/trollskull-community/12-nat.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. The sources give Nat no fixed day-one address (see Ches 1 placement).
Organization page: none. Factions Guide: none. Villains page: none.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 205 to 219 ("### Nat").
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/11-lif.md`
Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-trollskull-community/12-nat.txt`. Citation key WDH5e-p63 is printed in the wiki text. The wiki prints no edition on most lines. The "Ragamuffins" note cites a YouTube video and is not a published source.

## Method and caveats

- Campaign files: Grep and Read. Quotes copied from tool output.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string with escapes removed. `{@creature ...}` and `{@b ...}` tags left as written.
- Alexandrian: `sources/Appendix_D_-_Running_the_Tavern.md` (line 1184, Event 18) and `sources/Act_III_Arc_D.md` (line 111). The Alexandrian PDF was not searched for Nat (the Appendix D markdown has no Nat profile; see Not found).
- Not readable: `sources/Other remix files/The 3 Urchins NPC Guide.docx` (see Not readable).
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The adventure is the only published source for the three children, and it places them in quest scenes.** The sidebar "The Three Urchins" (`sources/adventure-wdh.json:7133`) gives ages, ethnicity, traits and the sign language. Its scenes are Dock Ward and Mistshore encounters, not a home.
2. **"neutral good" and "Commoner" have no source.** The adventure, the wiki and Appendix D give no alignment for any of the three children, and no stat block (the adventure calls them "noncombatants", `sources/adventure-wdh.json:9605`).
3. **"Featured in: Background figure; no scripted appearance" conflicts with the adventure.** The sidebar says "Three street urchins ... appear in several of this chapter's scenes" (`sources/adventure-wdh.json:7133`). Nat is named in at least five adventure scenes (see C2).
4. **"long before the party arrived" (Overview) has no source.** The only kitchen-stay source is a random tavern-time event that begins after the party opens the tavern (`sources/Appendix_D_-_Running_the_Tavern.md:1184`). See D3.

---

## A. Background facts by theme

### A1. Origin, age, family, and the group

**Adventure, The Three Urchins sidebar (page 63)**
> "Three street urchins, described below, appear in several of this chapter's scenes: {@b Nat} is a lanky, 10-year-old deaf Illuskan girl with a wooden toy sword. She is the leader of the group and communicates using a sign language that she invented and taught to her friends. {@b Jenks} is a portly 9-year-old Turami boy with a cloak, a toy wand, and a stuffed owlbear \"familiar.\" He's shy around strangers but brave when it comes to helping his friends. {@b Squiddly} is a slim 9-year-old tiefling boy with an eye patch, a small bow, and a quiver of toy arrows. He rarely thinks before he talks or acts."
> — `sources/adventure-wdh.json:7133`

**Adventure, the eldest (quest-time scene; the age fact is day-one)**
> "The eldest child, {@creature Nat|WDH}, attuned to the stone, but contact with the aboleth so terrified her that she dropped it, screamed, and ran away." — `sources/adventure-wdh.json:11929` (quest-time; the age fact is the day-one part)

**Wiki, infobox (WDH5e-p63)**
> "| sex            = Female<ref name="WDH5e-p63">{{Cite book/Waterdeep: Dragon Heist|63}}</ref>" — wiki line 12
> "| race           = [[Human]]<ref name="WDH5e-p63" />" — wiki line 13
> "| ethnicity      = [[Illuskan]]<ref name="WDH5e-p63" />" — wiki line 14
> "| age            = 10 in [[1492 DR]]<ref name="WDH5e-p63" />{{WDH-time}}" — wiki line 16
> "| languages      = Self-taught sign language<ref name="WDH5e-p63" />" — wiki line 18
> "| dob            = 1482" — wiki line 20
> "| alignment5e    = " — wiki line 56 (blank)
> "| class5e        = " — wiki line 58 (blank)

**Wiki, Description (WDH5e-p63)**
> "Nat was tall and skinny for her age. She was [[deaf]] and communicated with her friends by using a sign language that she invented." — wiki line 64

**Wiki, Possessions (WDH5e-p63)**
> "She carried a wooden toy [[sword]]." — wiki line 67

**Wiki, Relationships (WDH5e-p63; the Ragamuffins note cites a YouTube video)**
> "Nat led the group of street urchins that included her friends [[Jenks]] and [[Squiddly]]. The three of them call themselves the Ragamuffins." — wiki line 70 (the sentence "The three of them call themselves the Ragamuffins" sits in the same line)
> "The three kids are described or named as "Ragamuffins" in design sketches, as shown in [https://youtu.be/Gi2gJ57Coko?t=1406 this] episode of Dragon Talk." — wiki line 70 (note group)

### A2. How she came to lead and how she talks

**Adventure, sidebar (see A1)**
> "She is the leader of the group and communicates using a sign language that she invented and taught to her friends." — `sources/adventure-wdh.json:7133`

**Adventure, Trolltide scare (the children "entered the derelict tower on a dare")**
> "Just prior to the kenku's arrival, three children entered the derelict tower on a dare. If this encounter occurs on or around Trolltide, the children are wearing troll masks. These noncombatants are named {@creature Nat|WDH}, {@creature Jenks|WDH}, and {@creature Squiddly|WDH} (see \"{@area The Three Urchins|14e|x}\")." — `sources/adventure-wdh.json:9605` (quest-time scene; the group and the dare are habit facts)

### A3. Temperament, habits and manner

**Voice profile (character-voices skill, lines 208 to 215; the profile is the campaign's voice, not a source)**
> "- **Sound:** She doesn't speak aloud. Her invented sign language is quick and emphatic, and Jenks and Squiddly translate. Characters who learn her signs \"hear\" her as clipped and practical. In readaloud, describe the signing, then give the meaning in quotes as translated." — `.claude/skills/character-voices/voices/trollskull-community.md:208`
> "- **Personality in speech:** Fierce protectiveness and watchfulness. She sizes up adults warily before she'll sign to them directly. Her rare joy shows in big, fast signing and a grin." — `.claude/skills/character-voices/voices/trollskull-community.md:212`
> "- **Never:** She never leaves the other two behind, and never trusts an adult who talks down to her." — `.claude/skills/character-voices/voices/trollskull-community.md:215`

**Adventure, what the children do when they meet the party (quest-time scene; habit facts)**
> "The children fancy themselves adventurers of sorts, and they are quick to idolize and emulate real-life ones." — `sources/adventure-wdh.json:7625`
> "If the characters don't frighten them away, the children loiter around the alley, eating apples and picking through garbage piles." — `sources/adventure-wdh.json:7105` (the apple-cart scene; habit fact)

### A4. Relationships to other named figures

**Adventure, sidebar (see A1)**: Nat leads Jenks and Squiddly (`sources/adventure-wdh.json:7133`).

**Adventure, the kenku scene (Nat and Jenks beg for help)**
> "The characters encounter {@creature Nat|WDH} and {@creature Jenks|WDH} in {@area O2|1ab}; they beg the characters to save their young tiefling friend." — `sources/adventure-wdh.json:9606` (quest-time)

**Adventure, Fenerus (the children know him; quest-time scene)**
> "If they are asked about Fenerus, the children know who he is. They describe him as a big man with graying hair who looks like he has been in many fights, based on \"the scars he wears on his face.\" They know nothing more about him, other than that he lives alone." — `sources/adventure-wdh.json:7104`

**Campaign, Fenerus Stormcastle page (Jenks, not Nat; no Nat line)**: none.

### A5. Time in post and place

- No source gives a home, a birthplace or a parent for Nat. The wiki gives "home = [[Waterdeep]]" (wiki line 10) and no parents or siblings (wiki lines 28 to 31 blank).
- The wiki gives a day-one date of birth: "dob = 1482" (wiki line 20) with "age = 10 in [[1492 DR]]" (wiki line 16).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page summary: "> - *Illuskan human street urchin, neutral good, she/her*. Stat block: **Commoner**." — `campaign/setting/notable-figures/trollskull-community/12-nat.md:5`
- Adventure: no alignment for Nat. (Checked: `sources/adventure-wdh.json:7133` and the surrounding scenes.)
- Wiki: alignment5e blank (wiki line 56). Appendix D: no alignment.
- Result: "neutral good" is unsourced. Drafter keeps `[research]` or drops it.

**Species and ethnicity**
- Page summary: "Illuskan human street urchin" (`12-nat.md:5`).
- Adventure: "a lanky, 10-year-old deaf Illuskan girl" (`sources/adventure-wdh.json:7133`). The adventure does not say "human"; "Illuskan" is a human ethnicity in the wiki (wiki line 14).
- Wiki: "| race           = [[Human]]<ref name="WDH5e-p63" />" (wiki line 13) and "| ethnicity      = [[Illuskan]]" (wiki line 14).

**Pronouns**
- Page summary: "she/her" (`12-nat.md:5`).
- Adventure: "a lanky, 10-year-old deaf Illuskan girl" and "{@creature Nat|WDH}, the eldest child, ... so terrified her that she dropped it" (`sources/adventure-wdh.json:11929`).
- Wiki: "| sex            = Female" (wiki line 12).

**Stat block**
- Page summary: "Stat block: **Commoner**." (`12-nat.md:5`).
- Adventure: "These noncombatants are named Nat, Jenks, and Squiddly" (`sources/adventure-wdh.json:9605`). No stat block is given for the children.
- Wiki: class5e blank (wiki line 58). Result: "Commoner" is unsourced.

---

## C. Quest-time sentences on the current page (routed; not day-one)

Current page: `campaign/setting/notable-figures/trollskull-community/12-nat.md`. Sections: Gamemaster's Summary, Roleplaying Information (Resonance, Emotions, Motivations, Inspirations), Character Information (Persona, Morale, Relationships), Overview.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L7 | "> - **Featured in:** Background figure; no scripted appearance." | Conflicts with the adventure (see D1) | `sources/adventure-wdh.json:7133`; `:9605`; `:9606`; `:11929`; `:11930`; `:11939` (the rocking chair: "If the street urchins are present, one of them asks ...") |
| 2 | L11 | "**Resonance.** Nat should inspire protectiveness with her fierce quiet leadership, admiration when her sign language clicks as its own complete language, and warmth when the party realizes she has been watching out for them just as carefully as she watches out for Jenks and Squiddly." | "when the party realizes" is quest-time phrasing. Restate or keep per ruling 3 | Watching: none in the sources; the quest-time scenes are `sources/adventure-wdh.json:11930` ("Communicating through the other children, Nat tells the characters where she dropped the stone") |
| 3 | L25 | "**Relationships.** Nat is the de facto leader of the three urchins, the inventive mind behind their shared sign language, and a regular at Trollskull Manor (she and the others break in after hours to sleep in the kitchen)." | "a regular at Trollskull Manor" and the kitchen stay are tavern-time (after the opening). The break-in is a random event, not a day-one fact | `sources/Appendix_D_-_Running_the_Tavern.md:1184` (Event 18: "The Three Urchins (Nat, Jenks, and Squiddly) have somehow gotten into the tavern after hours and are sleeping in the kitchen.") and `campaign/guides/trollskull-manor/07-events.md:36` (same text) |
| 4 | L29 | "Nat is a deaf ten-year-old street urchin who leads a small trio of children; she communicates in a sign language she invented herself, and she has been using the tavern kitchen as a shelter long before the party arrived." | "long before the party arrived" is a day-one claim with no source (see D3). "the tavern kitchen" is the Event 18 setting | Sign language and age: `sources/adventure-wdh.json:7133`. Kitchen: `sources/Appendix_D_-_Running_the_Tavern.md:1184` |
| 5 | L21 | "To those she trusts, she is the one who scouts ahead, picks the safest escape route, and carries the most food." | Day-one in form. No source gives these habits (F2) | none |
| 6 | L21 | "Deep down, she is the oldest and she knows it, and the weight of that is heavier than anyone her age should carry." | "the oldest" is sourced (eldest, `sources/adventure-wdh.json:11929`). The weight is campaign invention | `sources/adventure-wdh.json:11929` |
| 7 | L23 | "**Morale.** In a fight, Nat grabs the others and runs. She scouts an exit before she scouts an enemy." | Campaign behavior; no source for a fight with Nat | none |

### C2. Where Nat's quest-time facts already live (routed)

- **Adventure, the Three Urchins in the apple-cart scene**: "The boy is one of three street urchins who teamed up to steal the apple cart from a nearby street corner. The other two children lost control of the cart at the crest of the alley before they could hop on." — `sources/adventure-wdh.json:7103` (Squiddly; the two others are not named here)
- **Adventure, Ice Escapades (Mistshore, the winter scene)**: "Playing on the ice underneath the docks are three street urchins wearing frayed cloaks and gloves." — `sources/adventure-wdh.json:7624`
- **Adventure, the Trolltide kenku tower**: "The characters encounter {@creature Nat|WDH} and {@creature Jenks|WDH} in {@area O2|1ab}; they beg the characters to save their young tiefling friend." — `sources/adventure-wdh.json:9606`
- **Adventure, the sewer clubhouse (Cellar Complex: Summer)**: "The eldest child, {@creature Nat|WDH}, attuned to the stone, but contact with the aboleth so terrified her that she dropped it, screamed, and ran away." — `sources/adventure-wdh.json:11929`. "Communicating through the other children, {@creature Nat|WDH} tells the characters where she dropped the stone and warns them that it's \"alive.\" Neither she nor the boys are eager to see it again." — `sources/adventure-wdh.json:11930`
- **Adventure, the rocking chair (Nat as a voice)**: "If the street urchins are present, one of them asks, \"Where'd that rocking chair come from?\"" — `sources/adventure-wdh.json:11939`
- **Adventure, the wiki-linked adventure illustrations (captions; no scene text)**: "{@creature Nat|WDH}, {@creature Jenks|WDH} and {@creature Squiddly|WDH} enjoy a windy autumn day on the docks" — `sources/adventure-wdh.json:26678`
- **Appendix D, Event 18**: `sources/Appendix_D_-_Running_the_Tavern.md:1184` (see C3)
- **Trollskull Manor guide, Event 18**: "| 18 | The Three Urchins (Nat, Jenks, Squiddly) have gotten into the tavern after hours and are sleeping in the kitchen. | Roleplay. |" — `campaign/guides/trollskull-manor/07-events.md:36`
- **Act III Arc D, the twelfth victim (a future scene; quest-time)**: "It might be one of the alley urchins, a neighbor who bought rounds at the tavern, a guild contact they grew fond of." — `sources/Act_III_Arc_D.md:111`
- **Wiki, the Vault of Dragons gallery (a future quest scene)**: "Nat, Squiddly, and [[Aurinax]] in the [[Vault of Dragons]]." — wiki gallery line 107 (edition not tagged; the image is a Dragon Heist gallery item)
- **Wiki, the Stone of Golorr entanglement (quest-time)**: "In the late 15{{th}} century DR, Nat and her friends were unwittingly entangled in the city-wide hunt for the ''[[Stone of Golorr]]'', sometimes innocently helping or hindering the efforts of adventurers in retrieving it." — wiki line 73

---

## D. Conflicts

**D1. "Featured in" (no scripted appearance)**
- Page: "> - **Featured in:** Background figure; no scripted appearance." (`12-nat.md:7`)
- Adventure: "Three street urchins, described below, appear in several of this chapter's scenes" (`sources/adventure-wdh.json:7133`); and Nat is named in `:9605`, `:9606`, `:11929`, `:11930` and `:11939`.
- Higher ranked: the adventure. The campaign's "no scripted appearance" is a campaign decision that conflicts with the published text. Flagged for the orchestrator.

**D2. Alignment and stat block**
- Page: "neutral good" and "Commoner" (`12-nat.md:5`).
- Adventure, wiki and Appendix D: silent. Not a conflict; unsourced. Drafter marks `[research]` or drops.

**D3. "long before the party arrived" versus the sources**
- Page: "she has been using the tavern kitchen as a shelter long before the party arrived." (`12-nat.md:29`)
- Appendix D: "The Three Urchins (Nat, Jenks, and Squiddly) have somehow gotten into the tavern after hours and are sleeping in the kitchen." (`sources/Appendix_D_-_Running_the_Tavern.md:1184`) — a random event in tavern-time, i.e. after the party owns the building.
- Result: the page's day-one claim is not in any source. The only source for a kitchen stay is the post-opening event.

**D4. Ages (consistent)**
- Adventure: "10-year-old" Nat (`sources/adventure-wdh.json:7133`). Wiki: "age = 10 in [[1492 DR]]" (wiki line 16). Page: "ten-year-old" (`12-nat.md:21`). No conflict.

---

## E. Stale lines in other files (not edited) and routed references

- `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/design-notes.md:21`: "Squiddly is used from **Trollskull Alley** without a voice line." (Squiddly only; not Nat.)
- `campaign/guides/trollskull-manor/08-notable-patrons.md:22`: "- One of the Three Urchins has been shoplifting small metal trinkets — they want a quiet resolution, no Watch" (unnamed urchin; tavern-time). Routed to the guide.
- `campaign/guides/trollskull-manor/07-events.md:36` and `sources/Appendix_D_-_Running_the_Tavern.md:1184` (Event 18): routed.
- `campaign/gazetteer/waterdeep/dock-ward.md`: no Nat line found (Grep).

---

## F. Gaps a Background would need that no source gives

1. **Home and family.** No source. The wiki gives "home = [[Waterdeep]]" (wiki line 10), and no parent, sibling or guardian (wiki lines 28 to 31 blank). The adventure names no guardian. Drafter may write a `[design]` home only if it is nameless.
2. **Where she sleeps and eats day one.** No source. The adventure's Dock Ward and Mistshore scenes (`sources/adventure-wdh.json:7615`, `:7624`) and the sewer clubhouse (`:11929`) are quest-time. The adventure's Mistshore text is: "A blizzard is tearing through Mistshore, turning its rotten tenements into dark, looming shapes behind veils of blowing snow." (`sources/adventure-wdh.json:7615`) — a setting fact, not a home for Nat.
3. **How she learned her sign language.** The sources say she "invented" it and "taught" it (`sources/adventure-wdh.json:7133`). No source says when, or from whom she learned speech or lip-reading.
4. **Her deafness.** Sourced: "deaf" (`sources/adventure-wdh.json:7133`; wiki line 64). No cause or onset.
5. **Her habits (scouting, carrying food).** Campaign only. No source.
6. **Her Ragamuffins name.** Wiki only, from design sketches (wiki line 70). Not in the adventure. Use only with a note.
7. **Alignment.** No source. See B.
8. **Faith.** No source.
9. **Her relationship to adults.** The adventure has her "wary" of adults only through the voice profile (`.claude/skills/character-voices/voices/trollskull-community.md:212`). The adventure's Fenerus scene: "If they are asked about Fenerus, the children know who he is." (`sources/adventure-wdh.json:7104`).

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background or the personal goals may use. They must not be contradicted.

- **Leadership.** "She is the leader of the group and communicates using a sign language that she invented and taught to her friends." — `sources/adventure-wdh.json:7133`
- **Responsibility.** "The eldest child, {@creature Nat|WDH}, ..." — `sources/adventure-wdh.json:11929` (quest-time scene; the age fact is day-one).
- **Fear.** "contact with the aboleth so terrified her that she dropped it, screamed, and ran away." — `sources/adventure-wdh.json:11929` (quest-time; do not use as a day-one fact).
- **Idolizing adventurers.** "The children fancy themselves adventurers of sorts, and they are quick to idolize and emulate real-life ones." — `sources/adventure-wdh.json:7625`
- **Dares.** "three children entered the derelict tower on a dare" — `sources/adventure-wdh.json:9605`.
- **Identity as a group.** "The three of them call themselves the Ragamuffins." — wiki line 70 (wiki; design sketch note).
- **Protectiveness of the others.** "fierce protectiveness of the other two" — `campaign/setting/notable-figures/trollskull-community/12-nat.md:13` (campaign; the adventure's sidebar says "brave when it comes to helping his friends" only for Jenks, `sources/adventure-wdh.json:7133`).
- **Hunger and survival.** "eating apples and picking through garbage piles." — `sources/adventure-wdh.json:7105`.

---

## Ches 1 placement (what the campaign and the sources place, day one)

- **Ward**: no source names Nat's ward on day one. The adventure's Dock Ward and Mistshore scenes are quest-time: "Playing on the ice underneath the docks are three street urchins" (`sources/adventure-wdh.json:7624`).
- **Street**: none on day one. The Trollskull kitchen is a tavern-time event (`sources/Appendix_D_-_Running_the_Tavern.md:1184`).
- **Drafter**: write no day-one address for Nat. Name the district only as "the Dock Ward" if the Dock Ward scenes are cited, and keep it `[research]`.

---

## Not found

- **Nat's alignment and stat block** in the adventure, the wiki, Appendix D and the Trollskull guides. Searched for "alignment", "neutral good" and "Commoner" near the children's names.
- **Nat's home, parents or guardian** in the adventure (searched for "Nat" with "home", "parent", "mother", "father", "live"), the wiki and the research bundles.
- **Nat in Alexandrian PDFs**: the Appendix D markdown has no Nat patron profile (grep of `sources/*.md` for "Nat\b" finds only `:1184`). The Alexandrian PDF "27. Addendum A Night in Trollskull Manor.pdf" was not searched for Nat beyond the pages read for Lif (see 11-lif.md, Method).
- **Nat in the Trollskull Alley quest files**: grep of `campaign/quests/act-i/trollskull-alley/` for "Nat\b" and "urchin" returns no match.
- **Nat in the faction quests**: "Nat", "Jenks" and "Squiddly" appear only in `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/` (Squiddly only).
- **Research bundles** (`sources/research/pass3-bundles/`, `pass5-bundles/`): grep for "urchin", "Jenks" and "Squiddly" finds no Nat profile.

## Not readable

- `sources/Other remix files/The 3 Urchins NPC Guide.docx`: named by `sources/SOURCE_GUIDE.md:694` ("Nat, Squiddly, and Jenks — personalities, street knowledge, quest hooks, how to use them as recurring contacts"). Not readable with the tools. It is the likely source for the day-one personalities and must be extracted before the Background is final.
