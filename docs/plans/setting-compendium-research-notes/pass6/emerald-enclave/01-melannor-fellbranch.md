# Pass 6 research notes: Melannor Fellbranch

Page: `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Sizing is the orchestrator's call. The Enclave page calls him "Primary Contact" (`campaign/setting/organizations/03-emerald-enclave.md:55`), and the page's Summary features him in 22 quest names and one location, so the full Personality and Connections apply.
Organization page: `campaign/setting/organizations/03-emerald-enclave.md` ("# The Emerald Enclave"; "Campaign role: Player faction.", line 7)
Factions Guide: `campaign/guides/factions/04-emerald-enclave.md`
Voice profile: `.claude/skills/character-voices/voices/emerald-enclave.md` (`### Melannor Fellbranch`, lines 5-19)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Every quote is copied from tool output. Line numbers are file lines. Where the Grep tool omitted a long JSON or Markdown line, the line was read with Read at its offset.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. The escape `\"` is shown as a plain quote. `{@creature ...}` tags are left as written.
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` was read as rendered page 2 (printed page 24). The Enclave sentence in D-free sections is a transcription from the image and must be checked with `pdftotext -layout` before it goes into prose. No other PDF was needed for this page.
- Alexandrian Appendices B, C and D are markdown and were read directly.
- Wiki: the scratchpad extract `wiki-emerald-enclave/01-melannor-fellbranch.txt`, quoted as "wiki line N" (that file's lines). The wiki prints no edition on most sentences. Its infobox fields `alignment5e` and `class5e` cite `WDH5e-p35-36`, the 5e *Dragon Heist* record.
- No shell was available and no edit tool was available, so this file was written whole. `voicecheck.py` was not run. No other file was edited.

## Findings that change how the page is written

1. **Alignment: the campaign says Neutral Good, the published text and the wiki say Chaotic Good.** The page keeps Neutral Good (`01-melannor-fellbranch.md:5` and `:11`). The adventure says "Melannor is chaotic good." (`sources/adventure-wdh.json:3705`), and the wiki says `alignment5e = [[Chaotic good]]` (wiki line 57). Campaign decisions outrank the published text. Conflict D1.
2. **The sibling link is campaign fact with support.** The adventure never calls Melannor and Talisolvanar brothers. The campaign states it on the Talisolvanar page (line 25) and the First Meeting event has Melannor say "He is my brother" (`campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:68`). Appendix D also gives it (`sources/Appendix_D_-_Running_the_Tavern.md:1244`), and the wiki does (line 75).
3. **Two sentences are quest-time trends.** "which happens more often as the year goes on" (`01-melannor-fellbranch.md:25`) and "He has been appearing in person more often as something he cannot name continues to trouble him." (`:33`) describe a change over the campaign. The Enclave page gives the day-one version: "he appears in person only when the situation demands it" (`campaign/setting/organizations/03-emerald-enclave.md:55`). The current Overview is 37 words, over the brief's limit of 21.
4. **One voice sample has no source.** The Greeting sample "Three people died in the Castle Ward last night." (`.claude/skills/character-voices/voices/emerald-enclave.md:17`) matches no line in the campaign. A Grep for "Three people died", "died in the Castle Ward" and "Castle Ward last night" over `campaign/` returned nothing. The Business sample (`:18`) is a request to act. Both are in section C.
5. **Melannor's Persona and Overview are the page's only quest-time sentences of substance.** The Summary "Featured in" line (`:7`) names 22 quests and one location. Those are routed, not narrated.

---

## A. Background facts by theme

### A1. Origin, birth, post

No source gives Melannor's birthplace, age, birth year, parents, or how long he has been groundskeeper. The wiki's `age`, `dob`, `parents` and `siblings` fields are blank (wiki lines 17, 21, 29, 31). The gap is in section F.

**Wiki, lead sentence (5e infobox ref `WDH5e-p35-36`)**
> "'''Melannor Fellbranch''' ({{Pronounce|MEL|ah|nor|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a groundskeeper and member of the [[Emerald Enclave]] in [[Waterdeep]] in [[1492 DR]].<ref name="WDH5e-p35-36" />{{WDH-time}}"
> — wiki line 62 (edition: 5e, *Waterdeep: Dragon Heist* pp. 35-36, from the ref name)

**Wiki, race and languages (infobox)**
> "| race           = [[Half-elf]]" — wiki line 14
> "| languages      = [[Common]], [[Elvish]]<ref name="WDH5e-p35-36" />" — wiki line 19 (edition: 5e)

**Adventure, the estate and its keeper (page 15, entry "Emerald Enclave")**
> "Members of the Emerald Enclave can be found in Phaulkonmere, a noble villa in the Southern Ward, and at the Snobeedle Orchard and Meadery in Undercliff. The walls of Phaulkonmere enclose fabulous gardens, and the buildings are covered with moss and ivy. The place is owned by descendants of two wealthy families-the Tarms (longtime Waterdavians) and the Phaulkons (who are of Cormyrean descent). They spend most of the year traveling abroad and entrust the estate to a half-elf groundskeeper named {@creature Melannor Fellbranch|wdh}. He is joined by Jeryth Phaulkon, a noblewoman turned demigod who serves Mielikki, divine lady of the forest."
> — `sources/adventure-wdh.json:1320`

**Adventure, the first-meeting entry (page 35, entry "Melannor Fellbranch")**
> "The characters' main contact in the Emerald Enclave is {@creature Melannor Fellbranch|wdh}, the friendly but humorless groundskeeper of Phaulkonmere, a compound located one block south of Kolat Towers (see chapter 8). Phaulkonmere is owned by the Tarm and Phaulkon noble families. Melannor delivers missions by way of {@spell animal messenger} spells and is partial to using cats and pigeons as couriers. He quickly assigns new members their first mission."
> — `sources/adventure-wdh.json:3700`

**Wiki, the post (5e)**
> "Melannor was the groundskeeper of [[Phaulkonmere Villa]], a compound located one block south of [[Kolat Towers]] that was owned by the [[Tarm]] and [[Phaulkon]] noble families. He also directed the Emerald Enclave agents in the city with [[Jeryth Phaulkon]], a [[Chosen]] of [[Mielikki]].<ref name="WDH5e-p35-36">{{Cite book/Waterdeep: Dragon Heist|35-36}}</ref>"
> — wiki line 65 (edition: 5e). The campaign differs on who leads: see D2.
> "Melannor obtained information from magical conversations with the animals of the city.<ref name="WDH5e-p16">{{Cite book/Waterdeep: Dragon Heist|16}}</ref>"
> — wiki line 67 (edition: 5e, p. 16)

**Campaign, who he answers to (day one)**
> "- **Leadership:** Jeryth is the highest Enclave authority in Waterdeep, and Melannor serves her and carries her words to the Enclave's members. No file names anyone above her or says whether the Waterdeep presence answers to a council elsewhere. [research] The Vilhon order was governed by an Elder Circle of three over seven circles of members (Forgotten Realms Wiki, *Emerald Enclave*, edition not stated), and the campaign gives the Waterdeep presence nothing like it."
> — `campaign/setting/organizations/03-emerald-enclave.md:52` (the whole bullet)

**Campaign, the duties (day one)**
> "- **Primary Contact:** Melannor Fellbranch, groundskeeper of Phaulkonmere and a Half-Elf druid. He is friendly but humorless, and he reports grim news in the tone of a man describing the weather. His messages travel by *Animal Messenger* and never run longer than twenty-five words. He chooses the animal himself, usually a cat, a pigeon, a crow or a falcon, and he appears in person only when the situation demands it."
> — `campaign/setting/organizations/03-emerald-enclave.md:55`

**Campaign, the keeper of the grounds (Southern Ward gazetteer, day one)**
> "- The Tarm and Phaulkon families own it and spend most of the year abroad. **Melannor Fellbranch** keeps the grounds, and **Jeryth Phaulkon** speaks from the leaves as a disembodied voice. The gate stands open before an invited visitor arrives, and response teams may watch the street but never enter."
> — `campaign/gazetteer/waterdeep/southern-ward.md:43`

**Campaign, the Southern Ward character entry (day one)**
> "**Melannor Fellbranch (Neutral Good, Half-Elf, he/him)**" — `campaign/gazetteer/waterdeep/southern-ward.md:107`
> "- The friendly but humorless groundskeeper of Phaulkonmere, who sends the Enclave's missions by *Animal Messenger* in messages of no more than twenty-five words. He never uses contractions, never jokes and never swears, and he answers a joke literally." — `southern-ward.md:108`
> "> - Melannor senses something wrong in the earth beneath the Castle Ward and cannot say what it is. The Castle Ward Secret holds the answer." — `southern-ward.md:113`

### A2. The brother, Talisolvanar "Tally" Fellbranch

**Campaign, Talisolvanar page (day one)**
> "**Relationships.** Tally is the brother of Melannor Fellbranch (Emerald Enclave contact at Phaulkonmere), and a longtime neighbor of Fala Lefaliir and Embric."
> — `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md:25`
> "**Motivations.** Tally wants to run the best woodworking shop in the North Ward, keep the alley a decent place to live, and make sure his brother Melannor actually visits once in a while."
> — same file, line 15

**Campaign, the First Meeting event (quest-time source of the exchange)**
> "> > "Good morning, and welcome to Phaulkonmere. I am Melannor Fellbranch, and I would like to know whether Talisolvanar is well. He is my brother, and he works as a carpenter in your alley.""
> — `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:68`
> "> > "Good, I am glad to hear it. Talisolvanar should visit when his work in the alley allows it.""
> — same file, line 74

**Adventure, Tally's entry (no mention of Melannor)**
> "{@creature Talisolvanar \"Tally\" Fellbranch|wdh}, the owner and chief artisan of the Bent Nail, is a male half-elf carpenter and woodcarver. He is a {@creature commoner}, with these changes:"
> — `sources/adventure-wdh.json:3372`

**Wiki, sibling (cites a D&D Beyond web article, dated 2018-09-12 in the citation; edition not stated)**
> "Melannor was brother to [[Talisolvanar Fellbranch]].<ref>{{Cite web | title=Waterdeep: Dragon Heist's Factions are Perfect for Beginner and Veteran DMs| publisher=D&D Beyond | date=2018-09-12 | work= | url=https://www.dndbeyond.com/posts/317-waterdeep-dragon-heists-factions-are-perfect-for| accessdate=2019-02-13 | editor=[[James Haeck]] }}</ref>"
> — wiki line 75

**Alexandrian Appendix D, Tally's Topics and Agendas (a Trollskull Manor visit)**
> "1. Introduces the characters to his brother, Melannor Fellbranch (Emerald Enclave contact), framing it as a casual visit that is clearly calculated."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1244` (under "### Tally Fellbranch", line 1236)

### A3. Standing in the Enclave

**Campaign, Jeryth as the other contact (day one)**
> "- **Secondary Contact:** Jeryth Phaulkon, the lady of the Phaulkonmere estate. She was a noblewoman before she became a Chosen of Mielikki, and for several years she has lived as a disembodied voice in the gardens. She cannot be harmed in this state, and she can cast any druid spell. She sends no one out on tasks, and the animals carry only Melannor's words."
> — `campaign/setting/organizations/03-emerald-enclave.md:56`

**Campaign, the messenger (day one)**
> "- **The messengers:** The animal speaks its message once, in Melannor's low voice, and anyone nearby can hear it. *Dragon Heist* (5e) calls him partial to cats and pigeons as couriers."
> — `campaign/setting/organizations/03-emerald-enclave.md:57`

**Campaign, Melannor's Relationships entry (his own page)**
> "He serves Jeryth Phaulkon and carries her few words to the Enclave's members. He speaks them as she gave them and adds only the urgency, which is his own."
> — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:29`

**Adventure, services to the party (page 15)**
> "- Enclave members share information they've gathered from magical conversations with animals in the city."
> "{@creature Melannor Fellbranch|wdh} (see \"Emerald Enclave\") provides free food and care for the adventurers' animals at Phaulkonmere."
> — `sources/adventure-wdh.json:1326` and `:1327`

### A4. Manner, habits and speech (day one)

**Appendix B, Melannor's entry (Alexandrian)**
> "**Contact: Melannor Fellbranch.** The groundskeeper of Phaulkonmere, a compound in the Southern Ward. Friendly but humorless, Melannor is a half-elf druid who communicates primarily through *animal messenger* spells — cats and pigeons are his preferred couriers."
> — `sources/Appendix_B_-_Player_Factions.md:295`
> "\"Melannor Fellbranch. I keep the grounds.\" He holds the gate and nods you through. \"Walk with me for a moment. The garden is worth the time.\""
> — `sources/Appendix_B_-_Player_Factions.md:325` (the "Meeting Melannor Fellbranch" passage, heading at `:321`)
> "He leads them along the main path without hurry, pointing out things as they pass — a patch of herbs being coaxed back from frost, a moss-colonised wall left that way by design, a nest he has been monitoring in the old oak since early spring. He is watching how they move through the space."
> — `sources/Appendix_B_-_Player_Factions.md:328`
> "\"The Enclave isn't what most people think,\" he says, pausing at a low stone bench near the garden's center. \"People hear the word 'nature' and they picture trees and rivers. Pleasant things. That is not quite it.\" He crouches briefly to examine something in the soil, then stands. \"Balance is a better word. What we watch for are disruptions — things that shouldn't be where they are, pulling at what keeps the world from unraveling. Sometimes that is in a forest. Sometimes it is in a city. Sometimes it is in a sewer beneath a city, if the sewer happens to contain a beholder who has been expanding his territory for twenty years.\""
> — `sources/Appendix_B_-_Player_Factions.md:331`
> "\"We offer honest work and the knowledge that it matters. We also offer this garden, as a place to come to when the rest of Waterdeep becomes too much. Lady Phaulkon keeps it safe.\" He glances toward the heart of the estate. \"You should hear her.\""
> — `sources/Appendix_B_-_Player_Factions.md:332`

**Campaign, Summary (day one)**
> "> Melannor never uses contractions, never jokes, and never swears. He answers a joke literally. He calls his brother \"Talisolvanar\" and never \"Tally\"."
> — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:9`

**Campaign, Morale (day one)**
> "**Morale.** In a fight, Melannor would reshape the terrain with druid magic (roots through flagstones, fog from dry air) and put himself between the threat and anyone who cannot run. He goes silent when he hears good news, because he finds even relief a private matter."
> — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:27`

**Voice profile (day one unless noted in C)**
> "- **Personality in speech:** Measured concern and patient duty. His affection shows in practical offers (\"I'll bring you seedlings.\"). His unease about the thing below the Castle Ward comes out as uncharacteristic hesitations and unfinished sentences."
> — `.claude/skills/character-voices/voices/emerald-enclave.md:12`
> "- **Quirks:** He answers jokes literally. He sends messages by cat and pigeon, written in the same flat tone."
> — same file, line 13

### A5. Rules that Melannor carries

**Factions Guide (day one, rules for members)**
> "- Melannor's *animal messenger* relay, once per tenday, for a member at Renown 3 or higher."
> — `campaign/guides/factions/04-emerald-enclave.md:17`
> "| 3 | **Summerstrider** | Once per tenday, Melannor sends a message of 25 words or fewer by *animal messenger* to a place he has visited. The reply comes back the same way. Jeryth casts one healing spell at Phaulkonmere only, once per Long Rest, from a fixed list of four, for injuries taken on Enclave business. Melannor gives one report per ward per tenday from the network of watchers. |"
> — `campaign/guides/factions/04-emerald-enclave.md:62`

**Alexandrian Appendix B rank row (same rule, different wording)**
> "| 3 | **Summerstrider** | Melannor relays communications anywhere in Waterdeep or its immediate environs via *animal messenger*, once per tenday. Access to Jeryth's healing spells for injuries sustained on Enclave business, cast at no cost. |"
> — `sources/Appendix_B_-_Player_Factions.md:374`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Half-Elf druid, Neutral Good, he/him*. Stat block: **Druid**, with Advantage on saving throws against the Charmed condition, immunity to magical sleep, Darkvision 60 ft., and Common and Elvish." — `01-melannor-fellbranch.md:5`
- Campaign, Summary: "> **Alignment.** Dragon Heist lists Melannor as Chaotic Good. The campaign keeps Neutral Good, and the Enclave events are written for it." — `01-melannor-fellbranch.md:11`
- Campaign, gazetteer: "**Melannor Fellbranch (Neutral Good, Half-Elf, he/him)**" — `campaign/gazetteer/waterdeep/southern-ward.md:107`
- Campaign, Enclave Draft Notes: "> - **Conflicts, Melannor's alignment:** *Dragon Heist* lists Chaotic Good, and his Notable Figures page keeps Neutral Good (`01-melannor-fellbranch.md:11`). The page states no alignment for him, so it only reports this." — `campaign/setting/organizations/03-emerald-enclave.md:162`
- Adventure: "> ...Melannor is chaotic good." — `sources/adventure-wdh.json:3705` (the list item after "is a half-elf {@creature druid}, with these changes:" at `:3701`). The item reads exactly: "Melannor is chaotic good."
- Wiki: "| alignment5e    = [[Chaotic good]]" — wiki line 57 (edition: 5e infobox)
- Wiki, earlier alignment fields (`alignment1e`, `2e`, `3e`, `35`, `4e`): blank (wiki lines 40, 43, 46, 50, 54)

**Species and ethnicity**
- Campaign: "*Half-Elf druid, Neutral Good, he/him*." — `01-melannor-fellbranch.md:5`; "Half-Elf" also in `campaign/setting/organizations/03-emerald-enclave.md:55`
- Adventure: "is a half-elf {@creature druid}, with these changes:" — `sources/adventure-wdh.json:3701`
- Wiki: "| race           = [[Half-elf]]" — wiki line 14 (the race field carries no ref; the infobox refs on lines 16 and 19 are 5e)
- Ethnicity: no source. The wiki's field is blank (wiki line 15). Brief ruling 5 does not apply to a half-elf.

**Pronouns**
- Campaign: "he/him" — `01-melannor-fellbranch.md:5`; "he/him" — `campaign/gazetteer/waterdeep/southern-ward.md:107`
- Adventure: "He quickly assigns new members their first mission." — `sources/adventure-wdh.json:3700`
- Wiki: "| sex            = Male" — wiki line 13

**Stat block**
- Campaign, Summary: "Stat block: **Druid**, with Advantage on saving throws against the Charmed condition, immunity to magical sleep, Darkvision 60 ft., and Common and Elvish." — `01-melannor-fellbranch.md:5`
- Adventure: "He has advantage on saving throws against being {@condition charmed}, and magic can't put him to sleep. He has darkvision out to a range of 60 feet. He speaks Common and Elvish." — `sources/adventure-wdh.json:3706`. The base block is "a half-elf {@creature druid}, with these changes" (`:3701`). No CR, AC or HP is given.
- Wiki: "| class5e        = {{Class table|edition=5e|[[Druid]]}}" — wiki line 59 (edition: 5e). `challenge5e` is blank (wiki line 58).
- Wiki: "| occupation     = Groundskeeper<ref name="WDH5e-p35-36" />" — wiki line 16 (edition: 5e)

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md`. It has no Background, Personality, Connections or `### Voice` section yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Half-Elf druid, Neutral Good, he/him*. Stat block: **Druid**, with Advantage on saving throws against the Charmed condition, immunity to magical sleep, Darkvision 60 ft., and Common and Elvish." | Day one. Keep | section B |
| 2 | L6 | "> - **Affiliation:** Emerald Enclave" | Day one. Organization page is "# The Emerald Enclave" (`03-emerald-enclave.md:1`), a player faction (`:7`) | `03-emerald-enclave.md:7` |
| 3 | L7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **Emerald Enclave First Meeting**, **A Seat at Phaulkonmere**, **The Water Table Stirs**, **Summerstrider**, **The Undercliff Scarecrows**, **Ten Nights in the City of the Dead**, **The Doppelganger Problem**, **The Grells in the Dock Ward**, **Autumnreaver**, **The Fouled Channel**, **Winterstalker**, **The Dreamer's Reach**, **Master of the Wild**, Trollskull Manor (location)" | Quest and location names. Routed to quests (brief ruling 1). Not narrative | `campaign/quests/faction-events/emerald-enclave/` (folders `00-first-meeting`, `s01`, `s02`, `r03`, `r10`, `r25`, `r50`, `m01` to `m06`); `campaign/quests/act-i/trollskull-alley/`; `campaign/quests/act-ii/fireball/`; `campaign/quests/act-ii/gralhund-villa/`; `campaign/structure/arc-e-faction-outposts.md:85` and `:373`; `campaign/structure/arc-f-xanathars-lair.md:35` and `:296`; `campaign/structure/arc-i-kolat-towers.md:37` and `:269` |
| 4 | L9 | "> Melannor never uses contractions, never jokes, and never swears. He answers a joke literally. He calls his brother \"Talisolvanar\" and never \"Tally\"." | Day one. Keep | `campaign/gazetteer/waterdeep/southern-ward.md:108`; voice `emerald-enclave.md:10` and `:11` |
| 5 | L11 | "> **Alignment.** Dragon Heist lists Melannor as Chaotic Good. The campaign keeps Neutral Good, and the Enclave events are written for it." | Draft Notes material, not a quest. Move to Draft Notes (brief ruling 14). See D1 | section D1 |
| 6 | L15 | "**Resonance.** Melannor should inspire trust with his calm reliability, amusement with his complete absence of humor, and endearment when his quiet baritone delivers grim news as though reporting weather." | Day one. Keep | voice `emerald-enclave.md:8` |
| 7 | L17 | "**Emotions.** Melannor most often feels measured concern, patient duty, understated affection expressed through action, private satisfaction when nature's balance is maintained, and a careful watchfulness that deepens when he cannot articulate what feels wrong." | Day one. Keep | voice `emerald-enclave.md:12` |
| 8 | L19 | "**Motivations.** Melannor wants to protect Phaulkonmere and its gardens, fulfill Enclave assignments with minimal fuss, and investigate disturbances he senses but cannot yet name." | Day one. Keep | `03-emerald-enclave.md:55` (his duties) |
| 9 | L21 | "**Inspirations.** When playing Melannor, channel Aragorn (*The Lord of the Rings*), Hank Hill (*King of the Hill*), and Obi-Wan Kenobi (*Star Wars*, prequel era)." | Not a fact. Keep | n/a |
| 10 | L25 | "**Persona.** To the world, Melannor is the friendly but humorless groundskeeper of Phaulkonmere in the Southern Ward, who sends the Enclave's missions by animal. His *Animal Messenger* creatures carry no more than twenty-five words, and he comes in person only when the situation demands it, which happens more often as the year goes on. To those he trusts, he explains each arrangement once and then waits for questions. Deep down, he senses something wrong in the earth beneath the Castle Ward and cannot say what it is." | **Quest-time trend: "which happens more often as the year goes on".** Restate as the Enclave page does: "he appears in person only when the situation demands it." The rest is day one; the Castle Ward sense is in `southern-ward.md:113` | `campaign/setting/organizations/03-emerald-enclave.md:55`; `campaign/gazetteer/waterdeep/southern-ward.md:113`. The trend appears only in quest events (row 13) |
| 11 | L27 | "**Morale.** In a fight, Melannor would reshape the terrain with druid magic (roots through flagstones, fog from dry air) and put himself between the threat and anyone who cannot run. He goes silent when he hears good news, because he finds even relief a private matter." | Day one. Keep | `campaign/setting/organizations/03-emerald-enclave.md:67` (the Enclave's fighting rule: "**Fighting:** Jeryth does not fight and protects the garden instead, and when she says \"Enough\", every vine in it tightens. Melannor reshapes the ground with druid magic, raising roots through flagstones and fog from dry air, and he puts himself between a threat and anyone who cannot run." rest of the passage covers: the six rangers and druids and their withdrawal rule). The "goes silent" clause has no source line; it is the page's own Morale |
| 12 | L29 | "**Relationships.** Melannor is the brother of Talisolvanar \"Tally\" Fellbranch, the Trollskull Alley carpenter. He asks after him at the First Meeting and says that Talisolvanar should visit when his work in the alley allows it. He serves Jeryth Phaulkon and carries her few words to the Enclave's members. He speaks them as she gave them and adds only the urgency, which is his own." | **Quest-time clause: "He asks after him at the First Meeting and says that Talisolvanar should visit when his work in the alley allows it."** The day-one version: the voice signature "Talisolvanar should visit." (`emerald-enclave.md:14`). The sibling fact is day one (A2). "the Trollskull Alley carpenter" is day one (`talisolvanar-fellbranch.md:29`) | `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:8`, `:68`, `:74`; `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md:25` |
| 13 | L33 | "The humorless groundskeeper of Phaulkonmere, who delivers grim news in a calm baritone and sends his messages by *Animal Messenger*. He has been appearing in person more often as something he cannot name continues to trouble him." | **Quest-time trend in the second sentence.** The first sentence is day one. Overview is 37 words (brief limit 21) | day-one version `campaign/setting/organizations/03-emerald-enclave.md:55`. The trend's quest source: `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-01-the-search.md:20` ("Melannor comes in person because the cats and gulls of the Dock Ward have left, and twenty-five words cannot carry what he has to say." rest of the passage covers: "This is the deliberate break from the animals that have carried his earlier messages.") |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/emerald-enclave.md`, `### Melannor Fellbranch`, lines 5-19)**

Ruling 16: a quest-time clause gets the day-one restatement, and the profile is changed to match. Each line:

- Line 6 (tagline): "*A humourless groundskeeper who reports grim news in a calm baritone, as if describing the weather.*" — day one.
- Line 8 (Sound): "A deep, calm, unvarying baritone. Nothing changes its tone, including bad news." — day one.
- Line 9 (Sentence shape): "Plain, complete, even-paced sentences. He states facts and waits. He does not recognise a joke when he hears one." — day one.
- Line 10 (Word choice): "Gardener's and druid's terms: soil, roots, seasons, balance. He calls the party by name, correctly, every time. He calls his brother \"Talisolvanar\", never \"Tally\"." — day one ("the party" is a generic address).
- Line 11 (Swearing): "*Never · Plain · n/a.* Never. He wouldn't see the point." — day one. Keep.
- Line 12 (Personality in speech): "Measured concern and patient duty. His affection shows in practical offers (\"I'll bring you seedlings.\"). His unease about the thing below the Castle Ward comes out as uncharacteristic hesitations and unfinished sentences." — day one.
- Line 13 (Quirks): "He answers jokes literally. He sends messages by cat and pigeon, written in the same flat tone." — day one.
- Line 14 (Signature phrases): "\"The soil is uneasy.\" / \"That is not humorous.\" / \"Talisolvanar should visit.\"" — day one. "The soil is uneasy" also appears in a quest event (`campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-01-the-search.md:63`), used as a habit there, not as an event.
- Line 15 (Never): "He never exaggerates, never laughs, and never ignores a disturbance in the earth." — day one.
- Line 17 (Sample, Greeting): "\"Good morning. The roses are well. Three people died in the Castle Ward last night.\"" — **the second sentence has no source.** A Grep for "Three people died", "died in the Castle Ward" and "Castle Ward last night" over `campaign/` returned nothing. The nearest source is the Dock Ward disappearances, which are on Pier 17 (`campaign/gazetteer/waterdeep/dock-ward.md:126`: "three people have vanished from Pier 17 on three nights"). Flag. The drafter may keep "The roses are well." and restate or drop the second sentence.
- Line 18 (Sample, Business): "\"Something beneath the city is stirring. I do not know what. I would like you to find out.\"" — **a request to act**, the hook pattern of the Enclave's quests. Flag. The day-one ask is the Enclave's standing list, `campaign/guides/factions/04-emerald-enclave.md:21` ("Accounts of aberrant creatures: where the party met one, how it moved and what it did to the animals nearby."). Drafter's call.
- Line 19 (Sample, Under pressure): "\"Stand behind the oak. The roots will hold them.\"" — day one.

---

## D. Conflicts

**D1. Alignment (campaign Neutral Good against published and wiki Chaotic Good)**
- Campaign, Summary: "> **Alignment.** Dragon Heist lists Melannor as Chaotic Good. The campaign keeps Neutral Good, and the Enclave events are written for it." — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:11`
- Campaign, gazetteer: "**Melannor Fellbranch (Neutral Good, Half-Elf, he/him)**" — `campaign/gazetteer/waterdeep/southern-ward.md:107`
- Campaign, Enclave Draft Notes: "> - **Conflicts, Melannor's alignment:** *Dragon Heist* lists Chaotic Good, and his Notable Figures page keeps Neutral Good (`01-melannor-fellbranch.md:11`). The page states no alignment for him, so it only reports this." — `campaign/setting/organizations/03-emerald-enclave.md:162`
- Adventure: "Melannor is chaotic good." — `sources/adventure-wdh.json:3705`
- Wiki: "| alignment5e    = [[Chaotic good]]" — wiki line 57
- Higher-ranked source: the campaign (Neutral Good), since campaign decisions outrank the published adventure (brief ruling 12). The Enclave's Draft Note says the page "states no alignment", but the page's Summary states one. The orchestrator decides whether the Summary keeps the alignment.

**D2. Who leads the Waterdeep agents (wiki against campaign)**
- Wiki: "He also directed the Emerald Enclave agents in the city with [[Jeryth Phaulkon]], a [[Chosen]] of [[Mielikki]]." — wiki line 65 (edition: 5e)
- Campaign: "Jeryth is the highest Enclave authority in Waterdeep, and Melannor serves her and carries her words to the Enclave's members." — `campaign/setting/organizations/03-emerald-enclave.md:52`
- Adventure: "He is joined by Jeryth Phaulkon, a noblewoman turned demigod who serves Mielikki, divine lady of the forest." — `sources/adventure-wdh.json:1320` (the adventure does not say who leads)
- Higher-ranked source: the campaign. The page's Persona and Relationships already follow "serves her and carries her words".

**D3. Stat block label (no conflict; noted for the drafter)**
- The Summary calls the block "Druid" (`01-melannor-fellbranch.md:5`). The adventure gives "is a half-elf {@creature druid}, with these changes:" (`sources/adventure-wdh.json:3701`). The campaign and adventure agree. The wiki gives class5e "Druid" (wiki line 59). No CR is given for Melannor in any source.

**D4. Frequency of in-person appearances (page against the Enclave page)**
- Page: "which happens more often as the year goes on" — `01-melannor-fellbranch.md:25`
- Enclave page: "he appears in person only when the situation demands it" — `campaign/setting/organizations/03-emerald-enclave.md:55`
- Not a contradiction in the campaign files: the page's clause is a trend that the Enclave page does not state. The drafter restates it (section C, row 10).

**D5. Sibling (no conflict)** The adventure does not call them brothers (its only Melannor and Tally entries are `sources/adventure-wdh.json:3372` and `:3700`). The wiki (line 75), the Talisolvanar page (line 25), the First Meeting (`ev-01-first-meeting.md:68`) and Appendix D (`:1244`) all say brother. Settled as day one (A2).

**D6. Pronouns and sex (no conflict)** he/him in the campaign (`01-melannor-fellbranch.md:5`), "Male" in the wiki (line 13), "He" in the adventure (`sources/adventure-wdh.json:3700`).

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/guides/factions/04-emerald-enclave.md:32`: "Enclave druids feel an infernal influence in the Sea Ward." The campaign places it in the Southern Ward (`campaign/gazetteer/waterdeep/southern-ward.md:121`). The Enclave Draft Notes already flag this (`campaign/setting/organizations/03-emerald-enclave.md:159`). Not a Melannor line; listed because it is in the faction guide that Melannor's page cites.
- `campaign/guides/factions/04-emerald-enclave.md:13`: "Kolat Towers stands one block north of Phaulkonmere, and nobody in the Enclave points at it before that gate." This agrees with `sources/adventure-wdh.json:3700` ("a compound located one block south of Kolat Towers"). Listed so the drafter does not read it as a conflict.
- `campaign/gazetteer/waterdeep/southern-ward.md:121`: "Jeryth's Southern Ward report in **Summerstrider** is that she has felt a wound in the ley lines near Coachlamp Lane for a tenday and a half, and she senses infernal influence there." This names a quest event. Enclave Draft Notes record the conflict with `campaign/structure/arc-e-faction-outposts.md:85` ("for two weeks") at `campaign/setting/organizations/03-emerald-enclave.md:164`.
- `campaign/setting/deities/eldath.md:104` names Mielikki as the Enclave's patron through Jeryth. The Enclave Draft Notes flag it (`03-emerald-enclave.md:187`). Not a Melannor line.

**E2. Routed quest references (quest time; the day-one page does not restate them)**
- `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:8` ("Meet Melannor Fellbranch inside the gate, where he asks after his brother Talisolvanar, and walk the garden with him."), `:31` (the cat carries his message), `:68` and `:74` (see A2)
- `campaign/quests/faction-events/emerald-enclave/m01-the-undercliff-scarecrows/ev-01-the-undercliff-scarecrows.md:7` ("Take Melannor's 24-word message, or walk to Phaulkonmere and question him in person.")
- `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/overview.md:17` ("At 08:00 Melannor Fellbranch comes to Trollskull Manor himself, with mud on his boots and a folded sketch in his hand.")
- `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-01-the-search.md:20` (see row 13)
- `campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:177` ("Contact: Melannor, at the gate or in the garden by day. He gives the report in person.")
- `campaign/quests/faction-events/emerald-enclave/r10-autumnreaver/ev-01-autumnreaver.md:5` ("Melannor Fellbranch comes to the member's door in person, walks them to Phaulkonmere and names the rank.")
- `campaign/quests/faction-events/emerald-enclave/m06-the-dreamers-reach/overview.md:85` ("Jeryth Phaulkon has fallen silent, and her garden has lost its sense of direction. Melannor sends the party down an old drain to find what is pressing on her.")
- `campaign/structure/arc-e-faction-outposts.md:85` ("*Melannor Fellbranch (Emerald Enclave — renown 1+).* Jeryth Phaulkon has been monitoring a disturbance in the Southern Ward for two weeks. ...") and `:373` ("*Melannor Fellbranch (Emerald Enclave).* Asks whether the Coachlamp Lane infernal disturbance was addressed. ...")
- `campaign/structure/arc-f-xanathars-lair.md:35` ("*Melannor Fellbranch (Emerald Enclave — renown 1+).* Environmental displacement in the sewer tunnels below Skullport ...") and `:296` ("- **Melannor:** \"Did anything unusual happen to the underground water systems near the collapse point?\"")
- `campaign/structure/arc-i-kolat-towers.md:37` ("*Melannor Fellbranch (Emerald Enclave — renown 1+).* Environmental damage in the immediate vicinity of the towers is distinctive. ...") and `:269` ("**Melannor Fellbranch (Emerald Enclave).** \"Is the force field down?\" ...")
- `sources/Appendix_C_-_Player_Faction_Missions.md:710` ("Melannor delivers this by *animal messenger* — a pigeon that lands on the windowsill of Trollskull Manor and speaks the briefing in his voice before flying away.")
- `sources/Appendix_C_-_Player_Faction_Missions.md:816` ("Melannor asks the party to convince Bonnie's doppelgangers to leave Waterdeep. The Enclave's concern is stability, not trustworthiness. ...")
- `sources/adventure-wdh.json:3735` and `:3745`: mission rows (Undercliff scarecrows; the Yawning Portal doppelgangers). Quest time, routed.

---

## F. Gaps a Background would need that no source gives

Invented material carries `[design]` and is listed in Draft Notes (brief ruling 17).

1. **Birthplace, birth year, age, home before Waterdeep.** No source. The wiki's `age` (wiki line 17), `dob` (line 21) and `formerhomes` (line 12) are blank. Consistent with: "[[Waterdeep]], [[Sword Coast North]]" (wiki line 11) and half-elf (wiki line 14).
2. **How he became groundskeeper, and when.** No source. Consistent with the adventure's "entrust the estate to a half-elf groundskeeper named" Melannor (`sources/adventure-wdh.json:1320`) and the wiki's "was a groundskeeper and member of the Emerald Enclave in Waterdeep in 1492 DR" (wiki line 62).
3. **How he joined the Enclave.** No source for him. Consistent with the Enclave's recruitment rule, "The Enclave seeks out characters who are naturalists, healers, or who have demonstrated concern for the natural world." (`sources/Appendix_B_-_Player_Factions.md:289`) and the druid class (`sources/adventure-wdh.json:3701`).
4. **His life with Tally.** The link is sourced (A2). No source says which brother is older, whether they grew up together, or what Tally's shop cost him. Consistent with the Talisolvanar page: "Tally is the brother of Melannor Fellbranch (Emerald Enclave contact at Phaulkonmere), and a longtime neighbor of Fala Lefaliir and Embric."
5. **Parents and other family.** None in any source. Do not invent a family without `[design]`.
6. **Work before the Enclave, companions, a loss.** No source. The wiki's `formerhomes` is blank (wiki line 12).
7. **Personal goals.** No source. The page's Motivations (`01-melannor-fellbranch.md:19`) are the Enclave's and the estate's. Consistent with his stated wants: "protect Phaulkonmere and its gardens", "investigate disturbances he senses but cannot yet name".
8. **Why he is humorless.** The campaign states it (`01-melannor-fellbranch.md:9`, `southern-ward.md:108`). No source gives a cause; a cause is `[design]`.
9. **His bond with Jeryth beyond service.** Consistent with "He serves Jeryth Phaulkon and carries her few words to the Enclave's members." (`01-melannor-fellbranch.md:29`) and "the animals carry only Melannor's words" (`campaign/setting/organizations/03-emerald-enclave.md:56`). No personal history is sourced.

---

## G. Source facts that hint at inner life (quotes; the Background must not contradict them)

- **Fondness for creatures.** "He liked [[pigeon]]s and [[cat]]s and always used them as couriers for his faction." — wiki line 70 (edition: 5e, `WDH5e-p35-36`). Also "is partial to using cats and pigeons as couriers" — `sources/adventure-wdh.json:3700`.
- **Care for a nest.** "a nest he has been monitoring in the old oak since early spring." — `sources/Appendix_B_-_Player_Factions.md:328`
- **Free care for visitors' animals.** "provides free food and care for the adventurers' animals at Phaulkonmere." — `sources/adventure-wdh.json:1327`
- **Relief as a private matter.** "He goes silent when he hears good news, because he finds even relief a private matter." — `01-melannor-fellbranch.md:27`
- **A worry he cannot name.** "a careful watchfulness that deepens when he cannot articulate what feels wrong." — `01-melannor-fellbranch.md:17`; "Deep down, he senses something wrong in the earth beneath the Castle Ward and cannot say what it is." — `01-melannor-fellbranch.md:25`
- **Unease under a calm voice.** "His unease about the thing below the Castle Ward comes out as uncharacteristic hesitations and unfinished sentences." — `.claude/skills/character-voices/voices/emerald-enclave.md:12`
- **His brother.** "make sure his brother Melannor actually visits once in a while." — `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md:15` (Tally's wish). "Talisolvanar should visit when his work in the alley allows it." — `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:74` (a quest line that the voice profile also keeps as a signature phrase).
- **Balance over nature.** "Balance is a better word." — `sources/Appendix_B_-_Player_Factions.md:331` (full sentence in A4)
- **Honest work.** "We offer honest work and the knowledge that it matters." — `sources/Appendix_B_-_Player_Factions.md:332`
- **Never ignores the earth.** "He never exaggerates, never laughs, and never ignores a disturbance in the earth." — `.claude/skills/character-voices/voices/emerald-enclave.md:15`
- **Visits to his brother's alley are calculated.** "framing it as a casual visit that is clearly calculated." — `sources/Appendix_D_-_Running_the_Tavern.md:1244` (this is an agenda for Tally's own entry, not Melannor's)

---

## Draft Notes material for the drafter (short)

- Settled: sibling link (A2); Neutral Good (D1, the campaign keeps it); Southern Ward; "Half-Elf"; he/him; Druid with the traits (B).
- Open for the orchestrator: D1 (the Summary's alignment line; the Enclave Draft Note says the page should state none).
- Open for the drafter: the Greeting sample "Three people died in the Castle Ward last night." (no source); the Business sample (`emerald-enclave.md:18`); the quest-time trend in Persona and Overview (rows 10 and 13).
- Not run: `voicecheck.py`.
