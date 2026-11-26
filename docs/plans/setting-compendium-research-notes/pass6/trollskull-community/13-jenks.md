# Pass 6 research notes: Jenks

Page: `campaign/setting/notable-figures/trollskull-community/13-jenks.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. The sources give Jenks no fixed day-one address (see Ches 1 placement).
Organization page: none. Factions Guide: none. Villains page: none.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 223 to 237 ("### Jenks").
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/11-lif.md`
Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-trollskull-community/13-jenks.txt`. Citation key WDH5e-p63. The wiki prints no edition on most lines.

## Method and caveats

- Campaign files: Grep and Read. Quotes copied from tool output.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string with escapes removed. Tags left as written.
- Alexandrian: `sources/Appendix_D_-_Running_the_Tavern.md` (line 1184, Event 18). The Alexandrian PDF has no Jenks profile in the Appendix D markdown (see Not found).
- Not readable: `sources/Other remix files/The 3 Urchins NPC Guide.docx` (see Not readable).
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The adventure gives Jenks's ethnicity and build, and nothing about his home.** "a portly 9-year-old Turami boy" (`sources/adventure-wdh.json:7133`). No day-one address or family.
2. **"neutral good" and "Commoner" have no source**, as for Nat and Squiddly (see 12-nat.md, finding 2).
3. **"Featured in: Background figure; no scripted appearance" conflicts with the adventure**, which names Jenks in the Trolltide scene (`sources/adventure-wdh.json:9606`) and the autumn illustration (`:26678`).
4. **The tavern-kitchen shelter is a post-opening random event** (`sources/Appendix_D_-_Running_the_Tavern.md:1184`). Overview says "the quietest of the three children who use the tavern kitchen for shelter" with no date. See D3.

---

## A. Background facts by theme

### A1. Origin, age, ethnicity, family, and the group

**Adventure, The Three Urchins sidebar (page 63)**
> "Three street urchins, described below, appear in several of this chapter's scenes: {@b Nat} is a lanky, 10-year-old deaf Illuskan girl with a wooden toy sword. She is the leader of the group and communicates using a sign language that she invented and taught to her friends. {@b Jenks} is a portly 9-year-old Turami boy with a cloak, a toy wand, and a stuffed owlbear \"familiar.\" He's shy around strangers but brave when it comes to helping his friends. {@b Squiddly} is a slim 9-year-old tiefling boy with an eye patch, a small bow, and a quiver of toy arrows. He rarely thinks before he talks or acts."
> — `sources/adventure-wdh.json:7133`

**Wiki, infobox (WDH5e-p63)**
> "| sex            = Male<ref name="WDH5e-p63">{{Cite book/Waterdeep: Dragon Heist|63}}</ref>" — wiki line 12
> "| race           = [[Human]]<ref name="WDH5e-p63" />" — wiki line 13
> "| ethnicity      = [[Turami]]<ref name="WDH5e-p63" />" — wiki line 14
> "| age            = 9 in [[1492 DR]]<ref name="WDH5e-p63" />{{WDH-time}}" — wiki line 16
> "| dob            = 1483" — wiki line 20
> "| alignment5e    = " — wiki line 56 (blank)
> "| class5e        = " — wiki line 58 (blank)

**Wiki, Description (WDH5e-p63)**
> "Jenks had a somewhat stocky build. Like most Turami, he had dark skin. His hair was a darker shade of brown than his skin, and was cut almost down to the roots." — wiki line 64

**Wiki, Personality (WDH5e-p63)**
> "Despite being shy around strangers, Jenks was brave and fiercely defended his friends." — wiki line 67

**Wiki, Possessions (WDH5e-p63)**
> "He wore a robe and carried a toy [[wand]] and a stuffed [[owlbear]], which he called his "[[familiar]]"." — wiki line 70

**Wiki, Relationships (WDH5e-p63)**
> "Jenks was part of the group of street urchins that included his friends [[Nat]] and [[Squiddly]]. Since Nat was [[deaf]], Jenks and Squiddly communicated with her using a sign language Nat had invented." — wiki line 74

### A2. Temperament, habits and manner

**Adventure (sidebar, see A1)**: "He's shy around strangers but brave when it comes to helping his friends." (`sources/adventure-wdh.json:7133`)

**Adventure, the children's view of adventurers (quest-time scene; habit fact)**
> "The children fancy themselves adventurers of sorts, and they are quick to idolize and emulate real-life ones." — `sources/adventure-wdh.json:7625`

**Voice profile (character-voices skill; the campaign's voice, not a source)**
> "- **Sound:** A small, quiet voice, often too soft to hear the first time." — `.claude/skills/character-voices/voices/trollskull-community.md:226`
> "- **Personality in speech:** Shy until he's comfortable, then warm and sweet. In a crisis his voice doesn't get louder, it gets firm." — `.claude/skills/character-voices/voices/trollskull-community.md:230`
> "- **Never:** He never lies to Nat, never forgets a kindness, and never leaves a friend in trouble." — `.claude/skills/character-voices/voices/trollskull-community.md:233`
> "- **Quirks:** He says "sorry" before asking anything. He mentions food when he's hungry, which is always. He thanks people days later for small things." — `.claude/skills/character-voices/voices/trollskull-community.md:231`

### A3. Relationships to other named figures

**Adventure (sidebar, see A1)**: Jenks is part of the group with Nat and Squiddly (`sources/adventure-wdh.json:7133`).

**Adventure, the kenku tower (quest-time; the two beg the party)**
> "The characters encounter {@creature Nat|WDH} and {@creature Jenks|WDH} in {@area O2|1ab}; they beg the characters to save their young tiefling friend." — `sources/adventure-wdh.json:9606`

**Campaign, Fenerus Stormcastle page (the acquaintance)**
> "- **Jenks:** An acquaintance, one of the people he sees on his rounds (**Jenks**)." — `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:38`
> "- **Jenks** (Notable Figures): the acquaintance" — `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:112`

**Adventure, Fenerus (the children and the lamplighter; the nightly rounds are the adventure's)**
> "Until recently, Fenerus supplemented his income by spying for the city of Luskan and providing his contacts with information on the political climate in Waterdeep, as well as juicy bits of news overheard on his nightly rounds through the Trades Ward." — `sources/adventure-wdh.json:7124`
> "Fenerus Stormcastle was the founder of the Blood Hawk Posse, a gang of horse-riding brigands that, to this day, harries travelers on the road to Amphail. When he was drummed out of the gang after a botched raid, Fenerus \"retired\" to Waterdeep and joined the Guild of Chandlers and Lamplighters." — `sources/adventure-wdh.json:7123`

### A4. Time in post and place

- No source gives a home, a parent or a guardian for Jenks.
- The wiki gives "dob = 1483" (wiki line 20) with "age = 9 in [[1492 DR]]" (wiki line 16).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page summary: "> - *Turami human street urchin, neutral good, he/him*. Stat block: **Commoner**." — `campaign/setting/notable-figures/trollskull-community/13-jenks.md:5`
- Adventure, wiki, Appendix D: no alignment for Jenks. Wiki alignment5e blank (wiki line 56).
- Result: "neutral good" is unsourced.

**Species and ethnicity**
- Page summary: "Turami human" (`13-jenks.md:5`).
- Adventure: "a portly 9-year-old Turami boy" (`sources/adventure-wdh.json:7133`). The adventure does not say "human".
- Wiki: "| race           = [[Human]]" (wiki line 13); "| ethnicity      = [[Turami]]" (wiki line 14).

**Pronouns**
- Page summary: "he/him" (`13-jenks.md:5`).
- Adventure: "a portly 9-year-old Turami boy" and "He's shy around strangers" (`sources/adventure-wdh.json:7133`).
- Wiki: "| sex            = Male" (wiki line 12).

**Stat block**
- Page summary: "Stat block: **Commoner**." (`13-jenks.md:5`).
- Adventure: the children are "noncombatants" (`sources/adventure-wdh.json:9605`), with no stat block for Jenks.
- Wiki: class5e blank (wiki line 58). Result: "Commoner" is unsourced.

---

## C. Quest-time sentences on the current page (routed; not day-one)

Current page: `campaign/setting/notable-figures/trollskull-community/13-jenks.md`. Sections: Gamemaster's Summary, Roleplaying Information (Resonance, Emotions, Motivations, Inspirations), Character Information (Persona, Morale, Relationships), Overview.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L7 | "> - **Featured in:** Background figure; no scripted appearance." | Conflicts with the adventure (see D1) | `sources/adventure-wdh.json:7133`; `:9605`; `:9606`; `:26678` |
| 2 | L23 | "**Morale.** In a fight, Jenks freezes. Then, if someone he loves is in danger, he does something the party will not believe a nine-year-old just did." | "the party will not believe" presumes the party. Restate as the alley's view, or keep per ruling 3. "freezes" is unsourced | `sources/adventure-wdh.json:7133` ("brave when it comes to helping his friends") |
| 3 | L25 | "**Relationships.** Jenks is Nat's steadiest companion, Squiddly's reluctant foil, and an acquaintance of Fenerus Stormcastle (the lamplighter they see on their rounds)." | Day-one in form. "the lamplighter they see on their rounds" reverses the Fenerus page ("one of the people he sees on his rounds") and is campaign wording | `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:38`; `sources/adventure-wdh.json:7124` |
| 4 | L29 | "Jenks is a portly nine-year-old street urchin, the quietest of the three children who use the tavern kitchen for shelter; he trails behind Nat by default, but anyone who has seen him act when it counts will not make the mistake of dismissing him again." | "who use the tavern kitchen for shelter" is a post-opening event (see D3). "trails behind Nat by default" is unsourced | `sources/Appendix_D_-_Running_the_Tavern.md:1184` (Event 18); `campaign/guides/trollskull-manor/07-events.md:36` |
| 5 | L21 | "To the world, Jenks is a portly nine-year-old who is shy around strangers and trails behind the others." | "portly", "nine-year-old", "shy around strangers" are sourced (`sources/adventure-wdh.json:7133`). "trails behind the others" is unsourced | `sources/adventure-wdh.json:7133` |
| 6 | L21 | "... and who would charge into a frozen lake without a second thought if Nat or Squiddly were in it." | Campaign invention. No source has a frozen-lake scene for Jenks | none |
| 7 | L13 | "... and a deep uncomplicated kindness he does not know is remarkable." | Campaign; voice profile has "remembers everything kind" | `.claude/skills/character-voices/voices/trollskull-community.md:228` |

### C2. Where Jenks's quest-time facts already live (routed)

- **Adventure, the Trolltide kenku tower (Nat and Jenks, the children in the O2 room)**: "Just prior to the kenku's arrival, three children entered the derelict tower on a dare." — `sources/adventure-wdh.json:9605`; "The characters encounter {@creature Nat|WDH} and {@creature Jenks|WDH} in {@area O2|1ab}; they beg the characters to save their young tiefling friend." — `sources/adventure-wdh.json:9606`
- **Adventure, the Trolltide illustration caption**: "{@creature Nat|WDH}, {@creature Jenks|WDH} and {@creature Squiddly|WDH} have a Trolltide scare" — `sources/adventure-wdh.json:18260`
- **Adventure, the summer illustration caption**: "{@creature Jenks|WDH} catches sight of Lady Cassalanter in the summer street" — `sources/adventure-wdh.json:22905`
- **Adventure, Ice Escapades (the winter scene)**: "Playing on the ice underneath the docks are three street urchins wearing frayed cloaks and gloves." — `sources/adventure-wdh.json:7624`
- **Adventure, the Fenerus scene (Jenks is not named there; the sidebar names him)**: `sources/adventure-wdh.json:7087` ("The characters' quest for the {@item Stone of Golorr|WDH} first leads them to Fenerus Stormcastle, a lamplighter who rents a small house in the Trades Ward").
- **Wiki, the Stone of Golorr entanglement (quest-time)**: "In the late 15{{th}} century DR, Jenks and his friends were unwittingly entangled in the city-wide hunt for the ''[[Stone of Golorr]]'', sometimes innocently helping or hindering the efforts of adventurers in retrieving it." — wiki line 77
- **Trollskull Manor guide, Event 18**: "| 18 | The Three Urchins (Nat, Jenks, Squiddly) have gotten into the tavern after hours and are sleeping in the kitchen. | Roleplay. |" — `campaign/guides/trollskull-manor/07-events.md:36`
- **Appendix D, Event 18**: "| 18 | The Three Urchins (Nat, Jenks, and Squiddly) have somehow gotten into the tavern after hours and are sleeping in the kitchen. | Roleplay. | |" — `sources/Appendix_D_-_Running_the_Tavern.md:1184`
- **Adventure, the wiki-linked gallery (Jenks observes a Cassalanter)**: wiki gallery line 102 ("Jenks gets a glimpse of Lady [[Ammalia Cassalanter]] while Nat and Squiddly run.") — wiki, edition not tagged.

---

## D. Conflicts

**D1. "Featured in" (no scripted appearance)**
- Page: "> - **Featured in:** Background figure; no scripted appearance." (`13-jenks.md:7`)
- Adventure: "Three street urchins, described below, appear in several of this chapter's scenes" (`sources/adventure-wdh.json:7133`); Jenks is named in `:9606` and in the captions at `:18260` and `:22905`.
- Higher ranked: the adventure. Flagged for the orchestrator.

**D2. Alignment and stat block**
- Page: "neutral good" and "Commoner" (`13-jenks.md:5`). Unsourced. Not a conflict.

**D3. The tavern-kitchen shelter**
- Page: "the quietest of the three children who use the tavern kitchen for shelter" (`13-jenks.md:29`).
- Appendix D: "The Three Urchins (Nat, Jenks, and Squiddly) have somehow gotten into the tavern after hours and are sleeping in the kitchen." (`sources/Appendix_D_-_Running_the_Tavern.md:1184`). A random tavern-time event that begins after the party opens the tavern.
- Result: a day-one "use ... for shelter" is not sourced.

**D4. The Fenerus direction**
- Page: "an acquaintance of Fenerus Stormcastle (the lamplighter they see on their rounds)" (`13-jenks.md:25`).
- Fenerus page: "- **Jenks:** An acquaintance, one of the people he sees on his rounds (**Jenks**)." (`campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:38`). Direction reversed. Not a source conflict; a wording choice to align.

---

## E. Stale lines in other files (not edited) and routed references

- `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:38` and `:112`: Jenks as acquaintance (see D4). Correct on today's file.
- `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/design-notes.md:21`: "Squiddly is used from **Trollskull Alley** without a voice line." (Squiddly only.)
- `campaign/guides/trollskull-manor/08-notable-patrons.md:22`: unnamed urchin shoplifting (see the Nat notes).

---

## F. Gaps a Background would need that no source gives

1. **Home, family and guardian.** No source. Wiki: "| siblings       = " (blank), "| parents        = " (blank) (wiki lines 29 and 31). No name for any adult in his life.
2. **Where he sleeps day one.** No source. See the Nat notes. The adventure's Dock Ward scenes are quest-time.
3. **Why he is called "Turami".** The sources give the ethnicity (`sources/adventure-wdh.json:7133`) and "Like most Turami, he had dark skin" (wiki line 64). No source describes a Turami home or family.
4. **His toy wand and stuffed owlbear "familiar".** Sourced (`sources/adventure-wdh.json:7133`; wiki line 70). No source says where he got them or why he keeps them.
5. **Whether he can speak.** The adventure says he is "shy around strangers" (`sources/adventure-wdh.json:7133`). The voice profile gives a quiet, soft voice (`.claude/skills/character-voices/voices/trollskull-community.md:226`). Both are campaign-consistent. No source says he is mute.
6. **Alignment and faith.** No source.
7. **His bravery.** Sourced: "brave when it comes to helping his friends" (`sources/adventure-wdh.json:7133`). The frozen-lake and freezing-in-a-fight lines are campaign-only (C rows 2 and 6).

---

## G. Inner-life hints in the sources (exact quotes)

- **Shyness.** "He's shy around strangers but brave when it comes to helping his friends." — `sources/adventure-wdh.json:7133`
- **Bravery for friends.** "Despite being shy around strangers, Jenks was brave and fiercely defended his friends." — wiki line 67.
- **Attachment to his friends.** "Jenks was part of the group of street urchins that included his friends [[Nat]] and [[Squiddly]]." — wiki line 74.
- **Attachment to a companion object.** "He wore a robe and carried a toy [[wand]] and a stuffed [[owlbear]], which he called his "[[familiar]]"." — wiki line 70.
- **Admiration of adventurers.** "The children fancy themselves adventurers of sorts, and they are quick to idolize and emulate real-life ones." — `sources/adventure-wdh.json:7625`
- **Hunger and survival.** "eating apples and picking through garbage piles." — `sources/adventure-wdh.json:7105`. The campaign's "quiet hunger" (`campaign/setting/notable-figures/trollskull-community/13-jenks.md:13`) matches this.
- **The dare.** "three children entered the derelict tower on a dare." — `sources/adventure-wdh.json:9605`.
- **Care for Squiddly (quest-time).** "they beg the characters to save their young tiefling friend." — `sources/adventure-wdh.json:9606`. Quest-time; do not use as day-one.

---

## Ches 1 placement (what the campaign and the sources place, day one)

- **Ward**: no source names Jenks's ward on day one. The adventure's Dock Ward and Mistshore scenes are quest-time (`sources/adventure-wdh.json:7624`).
- **Street**: none on day one. The Trollskull kitchen is a tavern-time event (`sources/Appendix_D_-_Running_the_Tavern.md:1184`).
- **Drafter**: write no day-one address for Jenks. Keep `[research]` on any district.

---

## Not found

- **Jenks's alignment and stat block** in the adventure, the wiki, Appendix D and the guides. Searched for "alignment", "neutral good" and "Commoner" near his name.
- **Jenks's home, parents or guardian** in the adventure, the wiki and the research bundles (searched for "Jenks" with "home", "parent", "mother", "father", "live").
- **Jenks in the Alexandrian PDFs**: the Appendix D markdown has no Jenks patron profile (grep of `sources/*.md` for "Jenks" finds only `:1184`). The PDF was not searched for Jenks beyond the pages read for Lif (see 11-lif.md, Method).
- **Jenks in the Trollskull Alley quest files**: grep of `campaign/quests/act-i/trollskull-alley/` for "Jenks" returns no match.
- **Jenks in the faction quests**: no match outside the Fenerus page and the urchin sidebar (grep of `campaign/quests/` for "Jenks").

## Not readable

- `sources/Other remix files/The 3 Urchins NPC Guide.docx`: named by `sources/SOURCE_GUIDE.md:694` ("Nat, Squiddly, and Jenks — personalities, street knowledge, quest hooks, how to use them as recurring contacts"). Not readable with the tools. Extract before the Background is final.
