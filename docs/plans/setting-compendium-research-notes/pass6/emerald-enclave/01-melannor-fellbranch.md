# Pass 6 research notes: Melannor Fellbranch

Page: `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Sizing is for the orchestrator. The Enclave page calls him "Primary Contact" (`campaign/setting/organizations/03-emerald-enclave.md:55`), and the Summary features him in 22 quest lines, so the full Personality and Connections apply.
Organization page: `campaign/setting/organizations/03-emerald-enclave.md` (title "# The Emerald Enclave"; "Campaign role: Player faction.", line 7)
Factions Guide: `campaign/guides/factions/04-emerald-enclave.md` (the file name in the folder is `04-emerald-enclave.md`)
Voice profile: `.claude/skills/character-voices/voices/emerald-enclave.md` (`### Melannor Fellbranch`, lines 5-19)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Every quote is copied from tool output. Line numbers are file lines. Where the Grep tool omitted a long JSON or Markdown line, the line was read with Read at its offset.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. The JSON escape `\"` is shown as a plain quote. `{@creature ...}` tags are left as written.
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` was read as rendered page 2 (printed page 24). The Enclave sentence is a transcription from the image. It must be checked with `pdftotext -layout` before it goes into prose. No other PDF was needed.
- Alexandrian Appendices B, C and D are markdown and were read directly.
- Wiki: the scratchpad extract `wiki-emerald-enclave/01-melannor-fellbranch.txt`, quoted as "wiki line N" (that file's lines). The wiki prints no edition on most sentences. Its infobox fields `alignment5e` and `class5e` cite `WDH5e-p35-36`, which is the 5e *Dragon Heist* record.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **Alignment is Neutral Good in the campaign and Chaotic Good in the published text and the wiki.** The page keeps Neutral Good (`01-melannor-fellbranch.md:5` and `:11`). The adventure says "Melannor is chaotic good." (`sources/adventure-wdh.json:3705`), and the wiki's infobox says `alignment5e = [[Chaotic good]]` (wiki line 57). Campaign decisions outrank the published text, so the drafter writes Neutral Good. The conflict is listed as D1.
2. **The brother link is a campaign fact with a sourced basis.** The adventure never calls them brothers (the only Melannor and Talisolvanar entries are at `sources/adventure-wdh.json:233`, `:313`, `:3372`, `:1327` and `:3700`). The campaign states the link on the Talisolvanar page, and the First Meeting event has Melannor say "He is my brother" (`campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:68`). The Alexandrian Appendix D also has it (`sources/Appendix_D_-_Running_the_Tavern.md:1244`).
3. **Two Persona and Overview sentences are quest-time trends.** "which happens more often as the year goes on" (`:25`) and "He has been appearing in person more often as something he cannot name continues to trouble him." (`:33`) narrate a change over the campaign. The Enclave page gives the day-one version: "he appears in person only when the situation demands it" (`campaign/setting/organizations/03-emerald-enclave.md:55`). The Overview is 37 words, over the brief's limit of 21.
4. **One voice sample has no source.** The Greeting sample "Three people died in the Castle Ward last night." (`.claude/skills/character-voices/voices/emerald-enclave.md:17`) matches no line in any campaign file (a Grep for "Three people died", "died in the Castle Ward" and "Castle Ward last night" returned nothing). The Business sample "Something beneath the city is stirring. I do not know what. I would like you to find out." (`:18`) is a request to act. Both are listed in section C.
5. **The Overview and Persona have no quest names,** but the Summary "Featured in" line (`:7`) lists 22 quest and location names. Those are routed, not narrated.

---

## A. Background facts by theme

### A1. Origin, birth, family

No source gives Melannor's birthplace, age, birth year, parents, or how long he has been groundskeeper. The wiki infobox fields `age`, `dob`, `parents` and `siblings` are blank (wiki lines 17, 21, 29, 31). The gap is listed in section F.

**Wiki, lead sentence (infobox ref `WDH5e-p35-36`, 5e)**
> "'''Melannor Fellbranch''' ({{Pronounce|MEL|ah|nor|...}}) was a groundskeeper and member of the [[Emerald Enclave]] in [[Waterdeep]] in [[1492 DR]].<ref name="WDH5e-p35-36" />{{WDH-time}}"
> — wiki line 62 (edition: 5e, *Waterdeep: Dragon Heist* pp. 35-36, from the ref name)

**Wiki, race and languages (infobox)**
> "| race           = [[Half-elf]]" — wiki line 14
> "| languages      = [[Common]], [[Elvish]]<ref name="WDH5e-p35-36" />" — wiki line 19 (edition: 5e)

**Adventure, the estate and its keeper (page 15)**
> "They spend most of the year traveling abroad and entrust the estate to a half-elf groundskeeper named {@creature Melannor Fellbranch|wdh}. He is joined by Jeryth Phaulkon, a noblewoman turned demigod who serves Mielikki, divine lady of the forest."
> — `sources/adventure-wdh.json:1320` (entry "Emerald Enclave", page 15). The same paragraph begins: "Members of the Emerald Enclave can be found in Phaulkonmere, a noble villa in the Southern Ward, and at the Snobeedle Orchard and Meadery in Undercliff." (rest of the passage covers: the Tarm and Phaulkon families, the estate's walls and gardens, the Snobeedle Orchard)

**Adventure, the first meeting entry (page 35)**
> "The characters' main contact in the Emerald Enclave is {@creature Melannor Fellbranch|wdh}, the friendly but humorless groundskeeper of Phaulkonmere, a compound located one block south of Kolat Towers (see chapter 8). Phaulkonmere is owned by the Tarm and Phaulkon noble families. Melannor delivers missions by way of {@spell animal messenger} spells and is partial to using cats and pigeons as couriers. He quickly assigns new members their first mission."
> — `sources/adventure-wdh.json:3700` (entry "Melannor Fellbranch", page 35)

**Wiki, the post (lines 65 and 67)**
> "Melannor was the groundskeeper of [[Phaulkonmere Villa]], a compound located one block south of [[Kolat Towers]] that was owned by the [[Tarm]] and [[Phaulkon]] noble families. He also directed the Emerald Enclave agents in the city with [[Jeryth Phaulkon]], a [[Chosen]] of [[Mielikki]].<ref name="WDH5e-p35-36">{{Cite book/Waterdeep: Dragon Heist|35-36}}</ref>"
> — wiki line 65 (edition: 5e). The campaign differs on who leads: see D2.
> "Melannor obtained information from magical conversations with the animals of the city.<ref name="WDH5e-p16">{{Cite book/Waterdeep: Dragon Heist|16}}</ref>"
> — wiki line 67 (edition: 5e, p. 16)

**Campaign, the post and who he answers to (day one)**
> "**Leadership:** Jeryth is the highest Enclave authority in Waterdeep, and Melannor serves her and carries her words to the Enclave's members. No file names anyone above her or says whether the Waterdeep presence answers to a council elsewhere. [research] ..."
> — `campaign/guides/factions/04-emerald-enclave.md` is not the source of this line. The line is `campaign/setting/organizations/03-emerald-enclave.md:52` and reads: "- **Leadership:** Jeryth is the highest Enclave authority in Waterdeep, and Melannor serves her and carries her words to the Enclave's members. No file names anyone above her or says whether the Waterdeep presence answers to a council elsewhere. [research] The Vilhon order was governed by an Elder Circle of three over seven circles of members (Forgotten Realms Wiki, *Emerald Enclave*, edition not stated), and the campaign gives the Waterdeep presence nothing like it."
> — `campaign/setting/organizations/03-emerald-enclave.md:52` (quote is the whole bullet)

**Campaign, the post and its duties (day one)**
> "**Primary Contact:** Melannor Fellbranch, groundskeeper of Phaulkonmere and a Half-Elf druid. He is friendly but humorless, and he reports grim news in the tone of a man describing the weather. His messages travel by *Animal Messenger* and never run longer than twenty-five words. He chooses the animal himself, usually a cat, a pigeon, a crow or a falcon, and he appears in person only when the situation demands it."
> — `campaign/setting/organizations/03-emerald-enclave.md:55`

**Campaign, the keeper of the grounds (Southern Ward gazetteer)**
> "- The Tarm and Phaulkon families own it and spend most of the year abroad. **Melannor Fellbranch** keeps the grounds, and **Jeryth Phaulkon** speaks from the leaves as a disembodied voice. The gate stands open before an invited visitor arrives, and response teams may watch the street but never enter."
> — `campaign/gazetteer/waterdeep/southern-ward.md:43`

**Campaign, the Southern Ward character entry**
> "**Melannor Fellbranch (Neutral Good, Half-Elf, he/him)**"
> "- The friendly but humorless groundskeeper of Phaulkonmere, who sends the Enclave's missions by *Animal Messenger* in messages of no more than twenty-five words. He never uses contractions, never jokes and never swears, and he answers a joke literally."
> — `campaign/gazetteer/waterdeep/southern-ward.md:107` and `:108`
> "> - Melannor senses something wrong in the earth beneath the Castle Ward and cannot say what it is. The Castle Ward Secret holds the answer."
> — `campaign/gazetteer/waterdeep/southern-ward.md:113`

### A2. The brother, Talisolvanar "Tally" Fellbranch

**Campaign, Talisolvanar page (day one)**
> "**Relationships.** Tally is the brother of Melannor Fellbranch (Emerald Enclave contact at Phaulkonmere), and a longtime neighbor of Fala Lefaliir and Embric."
> — `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md:25`
> "Tally runs the Bent Nail woodworking shop in Trollskull Alley and is one of the party's most reliable neighbors — dry-humored, plainspoken, and quietly generous with tools and labor when something in the alley needs fixing."
> — same file, line 29 (rest of that passage is Tally's own description; the phrase "the party's" is a quest-time word, not a Melannor fact)
> "**Motivations.** Tally wants to run the best woodworking shop in the North Ward, keep the alley a decent place to live, and make sure his brother Melannor actually visits once in a while."
> — same file, line 15

**Campaign, First Meeting event (quest-time source of the brother exchange)**
> "> > "Good morning, and welcome to Phaulkonmere. I am Melannor Fellbranch, and I would like to know whether Talisolvanar is well. He is my brother, and he works as a carpenter in your alley.""
> — `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:68`
> "> > "Good, I am glad to hear it. Talisolvanar should visit when his work in the alley allows it.""
> — same file, line 74 (quest-time; the phrase is also a voice signature, see A4)

**Adventure, Tally's own entry (page 35 area)**
> "{@creature Talisolvanar \"Tally\" Fellbranch|wdh}, the owner and chief artisan of the Bent Nail, is a male half-elf carpenter and woodcarver. He is a {@creature commoner}, with these changes:"
> — `sources/adventure-wdh.json:3372`. The adventure does not name Melannor in this entry.

**Wiki, sibling (cites a D&D Beyond article, 2018; edition not stated)**
> "Melannor was brother to [[Talisolvanar Fellbranch]].<ref>{{Cite web | title=Waterdeep: Dragon Heist's Factions are Perfect for Beginner and Veteran DMs| publisher=D&D Beyond | ...}}</ref>"
> — wiki line 75 (edition not stated; the article is a 5e-era web piece, but the wiki does not say so)

**Alexandrian Appendix D, Tally's Topics and Agendas (quest-time as a Trollskull Manor visit)**
> "1. Introduces the characters to his brother, Melannor Fellbranch (Emerald Enclave contact), framing it as a casual visit that is clearly calculated."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1244` (heading "### Tally Fellbranch" at `:1236`)

### A3. Relationship to the Enclave and to Jeryth

**Campaign, Enclave page, Melannor's standing (day one)**
> "Melannor serves her and carries her words to the Enclave's members." — `campaign/setting/organizations/03-emerald-enclave.md:52` (see A1, full bullet)
> "- **Secondary Contact:** Jeryth Phaulkon, the lady of the Phaulkonmere estate. She was a noblewoman before she became a Chosen of Mielikki, and for several years she has lived as a disembodied voice in the gardens. She cannot be harmed in this state, and she can cast any druid spell. She sends no one out on tasks, and the animals carry only Melannor's words."
> — `campaign/setting/organizations/03-emerald-enclave.md:56`

**Campaign, the Enclave's messenger rule (day one)**
> "**The messengers:** The animal speaks its message once, in Melannor's low voice, and anyone nearby can hear it. *Dragon Heist* (5e) calls him partial to cats and pigeons as couriers."
> — `campaign/setting/organizations/03-emerald-enclave.md:57`

**Campaign, Melannor's Relationships entry (Persona section, page)**
> "He serves Jeryth Phaulkon and carries her few words to the Enclave's members. He speaks them as she gave them and adds only the urgency, which is his own."
> — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:29`

**Adventure, support to the party (page 15)**
> "- Enclave members share information they've gathered from magical conversations with animals in the city."
> "{@creature Melannor Fellbranch|wdh} (see \"Emerald Enclave\") provides free food and care for the adventurers' animals at Phaulkonmere."
> — `sources/adventure-wdh.json:1326` and `:1327`

### A4. Manner, habits and speech (day one)

**Appendix B, Melannor at the gate (Alexandrian)**
> "**Contact: Melannor Fellbranch.** The groundskeeper of Phaulkonmere, a compound in the Southern Ward. Friendly but humorless, Melannor is a half-elf druid who communicates primarily through *animal messenger* spells — cats and pigeons are his preferred couriers."
> — `sources/Appendix_B_-_Player_Factions.md:295`
> "\"Melannor Fellbranch. I keep the grounds.\" He holds the gate and nods you through. \"Walk with me for a moment. The garden is worth the time.\""
> — `sources/Appendix_B_-_Player_Factions.md:325` (inside the Appendix B "Meeting Melannor Fellbranch" passage, heading at `:321`)
> "He leads them along the main path without hurry, pointing out things as they pass — a patch of herbs being coaxed back from frost, a moss-colonised wall left that way by design, a nest he has been monitoring in the old oak since early spring. He is watching how they move through the space."
> — `sources/Appendix_B_-_Player_Factions.md:328`
> "\"The Enclave isn't what most people think,\" he says, pausing at a low stone bench near the garden's center. \"People hear the word 'nature' and they picture trees and rivers. Pleasant things. That is not quite it.\" He crouches briefly to examine something in the soil, then stands. \"Balance is a better word. What we watch for are disruptions — things that shouldn't be where they are, pulling at what keeps the world from unraveling. ...\""
> — `sources/Appendix_B_-_Player_Factions.md:331` (the passage continues with the beholder sentence; rest of the passage covers the beholder in the sewer)

**Campaign, Melannor's Summary line (day one)**
> "> Melannor never uses contractions, never jokes, and never swears. He answers a joke literally. He calls his brother \"Talisolvanar\" and never \"Tally\"."
> — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:9`

**Campaign, Morale (day one)**
> "He goes silent when he hears good news, because he finds even relief a private matter."
> — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:27`

**Voice profile, Melannor (day one unless noted in C)**
> "- **Personality in speech:** Measured concern and patient duty. His affection shows in practical offers ("I'll bring you seedlings."). His unease about the thing below the Castle Ward comes out as uncharacteristic hesitations and unfinished sentences."
> — `.claude/skills/character-voices/voices/emerald-enclave.md:12`
> "- **Quirks:** He answers jokes literally. He sends messages by cat and pigeon, written in the same flat tone."
> — same file, line 13

### A5. Work, courier method and the Enclave's routes (rules that Melannor carries)

**Factions Guide, the messenger and the three routes (day one)**
> "- **Melannor's** ..." — not quoted; the Factions Guide line used is:
> "- Melannor's *animal messenger* relay, once per tenday, for a member at Renown 3 or higher."
> — `campaign/guides/factions/04-emerald-enclave.md:17`
> "| 3 | **Summerstrider** | Once per tenday, Melannor sends a message of 25 words or fewer by *animal messenger* to a place he has visited. The reply comes back the same way. ..."
> — `campaign/guides/factions/04-emerald-enclave.md:62` (the row continues: "Jeryth casts one healing spell at Phaulkonmere only, once per Long Rest, from a fixed list of four, for injuries taken on Enclave business. Melannor gives one report per ward per tenday from the network of watchers.")

**Adventure, Alexandrian Enclave ranks (page 15 area; rules)**
> "Once per tenday, Melannor sends a message..." — not in the adventure; the adventure has no rank table. Use the Factions Guide line above. The Alexandrian rank row is `sources/Appendix_B_-_Player_Factions.md:374`: "| 3 | **Summerstrider** | Melannor relays communications anywhere in Waterdeep or its immediate environs via *animal messenger*, once per tenday. Access to Jeryth's healing spells for injuries sustained on Enclave business, cast at no cost. |"

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Half-Elf druid, Neutral Good, he/him*. Stat block: **Druid**, with Advantage on saving throws against the Charmed condition, immunity to magical sleep, Darkvision 60 ft., and Common and Elvish." — `01-melannor-fellbranch.md:5`
- Campaign, Summary: "> **Alignment.** Dragon Heist lists Melannor as Chaotic Good. The campaign keeps Neutral Good, and the Enclave events are written for it." — `01-melannor-fellbranch.md:11`
- Campaign, gazetteer: "**Melannor Fellbranch (Neutral Good, Half-Elf, he/him)**" — `campaign/gazetteer/waterdeep/southern-ward.md:107`
- Campaign, Enclave Draft Notes: "> - **Conflicts, Melannor's alignment:** *Dragon Heist* lists Chaotic Good, and his Notable Figures page keeps Neutral Good (`01-melannor-fellbranch.md:11`). The page states no alignment for him, so it only reports this." — `campaign/setting/organizations/03-emerald-enclave.md:162` (the Draft Note asks the page to state no alignment; the Summary does state one. This is a page-level contradiction in the existing files, flagged in D1.)
- Adventure: "Melannor is chaotic good." — `sources/adventure-wdh.json:3705` (list item under "is a half-elf {@creature druid}, with these changes:" at `:3701`)
- Wiki: "| alignment5e    = [[Chaotic good]]" — wiki line 57 (edition: 5e infobox)
- Wiki, earlier alignment fields: blank (wiki lines 40, 43, 46, 50, 54 are empty alignment fields)

**Species and ethnicity**
- Campaign: "*Half-Elf druid, Neutral Good, he/him*." — `01-melannor-fellbranch.md:5`; "Half-Elf" in the Enclave page "Primary Contact" bullet (`03-emerald-enclave.md:55`)
- Adventure: "is a half-elf {@creature druid}, with these changes:" — `sources/adventure-wdh.json:3701`
- Wiki: "| race           = [[Half-elf]]" — wiki line 14 (edition: 5e, the infobox cites `WDH5e-p35-36` on lines 16 and 19; race itself carries no ref)
- No ethnicity is sourced. The wiki's ethnicity field is blank (wiki line 15). Brief ruling 5 applies only to humans; Melannor is not one.

**Pronouns**
- Campaign: "he/him" — `01-melannor-fellbranch.md:5`; "he/him" — `campaign/gazetteer/waterdeep/southern-ward.md:107`
- Adventure: "He quickly assigns new members their first mission." — `sources/adventure-wdh.json:3700`
- Wiki: "| sex            = Male" — wiki line 13

**Stat block**
- Campaign, Summary: "Stat block: **Druid**, with Advantage on saving throws against the Charmed condition, immunity to magical sleep, Darkvision 60 ft., and Common and Elvish." — `01-melannor-fellbranch.md:5`
- Adventure: "Melannor is chaotic good." and "He has these racial traits: He has advantage on saving throws against being {@condition charmed}, and magic can't put him to sleep. He has darkvision out to a range of 60 feet. He speaks Common and Elvish." — `sources/adventure-wdh.json:3705` and `:3706`. The adventure gives a base block ("a half-elf {@creature druid}") and these changes. It gives no CR, AC or HP.
- Wiki: "| class5e        = {{Class table|edition=5e|[[Druid]]}}" — wiki line 59 (edition: 5e). Wiki "challenge5e" is blank (line 58).
- Wiki: "| occupation     = Groundskeeper<ref name="WDH5e-p35-36" />" — wiki line 16

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md`. The page has no Background, no Personality, no Connections and no `### Voice` yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Half-Elf druid, Neutral Good, he/him*. Stat block: **Druid**, with Advantage on saving throws against the Charmed condition, immunity to magical sleep, Darkvision 60 ft., and Common and Elvish." | Day one. Keep | section B |
| 2 | L6 | "> - **Affiliation:** Emerald Enclave" | Day one. Label checked: the organization page is "# The Emerald Enclave" (`03-emerald-enclave.md:1`), a player faction (`:7`) | `03-emerald-enclave.md:7` |
| 3 | L7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **Emerald Enclave First Meeting**, **A Seat at Phaulkonmere**, **The Water Table Stirs**, **Summerstrider**, **The Undercliff Scarecrows**, **Ten Nights in the City of the Dead**, **The Doppelganger Problem**, **The Grells in the Dock Ward**, **Autumnreaver**, **The Fouled Channel**, **Winterstalker**, **The Dreamer's Reach**, **Master of the Wild**, Trollskull Manor (location)" | Quest and location names. Routed to quests (brief ruling 1). Not narrative. | `campaign/quests/faction-events/emerald-enclave/` (folders `00-first-meeting`, `s01`, `s02`, `r03`, `r10`, `r25`, `r50`, `m01` to `m06`); `campaign/quests/act-i/trollskull-alley/`; `campaign/quests/act-ii/fireball/`; `campaign/quests/act-ii/gralhund-villa/`; `campaign/structure/arc-e-faction-outposts.md:85` and `:373`; `campaign/structure/arc-f-xanathars-lair.md:35` and `:296`; `campaign/structure/arc-g-cassalanter-villa.md:157`; `campaign/structure/arc-i-kolat-towers.md:37` and `:269` |
| 4 | L9 | "> Melannor never uses contractions, never jokes, and never swears. He answers a joke literally. He calls his brother \"Talisolvanar\" and never \"Tally\"." | Day one. Keep. Matches the gazetteer line `southern-ward.md:108` | `campaign/gazetteer/waterdeep/southern-ward.md:108`; voice `emerald-enclave.md:10` and `:11` |
| 5 | L11 | "> **Alignment.** Dragon Heist lists Melannor as Chaotic Good. The campaign keeps Neutral Good, and the Enclave events are written for it." | Draft Notes material, not a quest. Move to Draft Notes (brief ruling 14). See D1 | section D1 |
| 6 | L15 | "**Resonance.** Melannor should inspire trust with his calm reliability, amusement with his complete absence of humor, and endearment when his quiet baritone delivers grim news as though reporting weather." | Day one. Keep | `sources/Appendix_B_-_Player_Factions.md:325` (the baritone and humorlessness); voice `emerald-enclave.md:8` |
| 7 | L17 | "**Emotions.** Melannor most often feels measured concern, patient duty, understated affection expressed through action, private satisfaction when nature's balance is maintained, and a careful watchfulness that deepens when he cannot articulate what feels wrong." | Day one. Keep | voice `emerald-enclave.md:12` |
| 8 | L19 | "**Motivations.** Melannor wants to protect Phaulkonmere and its gardens, fulfill Enclave assignments with minimal fuss, and investigate disturbances he senses but cannot yet name." | Day one. Keep | `03-emerald-enclave.md:55` (his duties) |
| 9 | L21 | "**Inspirations.** When playing Melannor, channel Aragorn (*The Lord of the Rings*), Hank Hill (*King of the Hill*), and Obi-Wan Kenobi (*Star Wars*, prequel era)." | Not a fact. Keep | n/a |
| 10 | L25 | "**Persona.** To the world, Melannor is the friendly but humorless groundskeeper of Phaulkonmere in the Southern Ward, who sends the Enclave's missions by animal. His *Animal Messenger* creatures carry no more than twenty-five words, and he comes in person only when the situation demands it, which happens more often as the year goes on. To those he trusts, he explains each arrangement once and then waits for questions. Deep down, he senses something wrong in the earth beneath the Castle Ward and cannot say what it is." | **Quest-time trend in the clause "which happens more often as the year goes on".** The rest is day one. Restate as "he comes in person only when the situation demands it" (the Enclave page wording). The Castle Ward sentence is day one (the wrongness is a standing fact in `castle-ward.md:39`; Melannor's sense of it is in `southern-ward.md:113`) | `campaign/setting/organizations/03-emerald-enclave.md:55` ("he appears in person only when the situation demands it"); `campaign/gazetteer/waterdeep/southern-ward.md:113`; the trend is only in the quest events below |
| 11 | L27 | "**Morale.** In a fight, Melannor would reshape the terrain with druid magic (roots through flagstones, fog from dry air) and put himself between the threat and anyone who cannot run. He goes silent when he hears good news, because he finds even relief a private matter." | Day one. Keep. (The Morale of the fight is a combat register, not a quest event.) | `campaign/guides/factions/04-emerald-enclave.md:67` ("Melannor reshapes the ground with druid magic, raising roots through flagstones and fog from dry air, and he puts himself between a threat and anyone who cannot run."); `campaign/guides/factions/04-emerald-enclave.md` line 67 is the source for the fight |
| 12 | L29 | "**Relationships.** Melannor is the brother of Talisolvanar \"Tally\" Fellbranch, the Trollskull Alley carpenter. He asks after him at the First Meeting and says that Talisolvanar should visit when his work in the alley allows it. He serves Jeryth Phaulkon and carries her few words to the Enclave's members. He speaks them as she gave them and adds only the urgency, which is his own." | **Quest-time clause: "He asks after him at the First Meeting and says that Talisolvanar should visit when his work in the alley allows it."** The First Meeting is an event, and the exchange is in its script. The day-one version: the voice signature "Talisolvanar should visit." (`emerald-enclave.md:14`). The sibling fact itself is day one (A2) | `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:8`, `:68`, `:74`; `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md:25` |
| 13 | L33 | "The humorless groundskeeper of Phaulkonmere, who delivers grim news in a calm baritone and sends his messages by *Animal Messenger*. He has been appearing in person more often as something he cannot name continues to trouble him." | **Quest-time trend in the second sentence.** The first sentence is day one. Also 37 words (brief limit 21) | `campaign/setting/organizations/03-emerald-enclave.md:55` (day-one version); the trend is in `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-01-the-search.md:20` ("Melannor comes in person because the cats and gulls of the Dock Ward have left, and twenty-five words cannot carry what he has to say.") |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/emerald-enclave.md`, `### Melannor Fellbranch`, lines 5-19)**

Ruling 16 says a quest-time clause gets the day-one restatement and the profile is changed to match. The lines are listed here with status.

- Line 6 (tagline): "*A humourless groundskeeper who reports grim news in a calm baritone, as if describing the weather.*" — day one.
- Line 8 (Sound): "A deep, calm, unvarying baritone. Nothing changes its tone, including bad news." — day one.
- Line 9 (Sentence shape): "Plain, complete, even-paced sentences. He states facts and waits. He does not recognise a joke when he hears one." — day one.
- Line 10 (Word choice): "Gardener's and druid's terms: soil, roots, seasons, balance. He calls the party by name, correctly, every time. He calls his brother "Talisolvanar", never "Tally"." — day one. "the party" is a generic address, not an event.
- Line 11 (Swearing): "*Never · Plain · n/a.* Never. He wouldn't see the point." — day one. Keep (adult table; this line is the no-swearing case).
- Line 12 (Personality in speech): "...His unease about the thing below the Castle Ward comes out as uncharacteristic hesitations and unfinished sentences." — day one.
- Line 13 (Quirks): "He answers jokes literally. He sends messages by cat and pigeon, written in the same flat tone." — day one.
- Line 14 (Signature phrases): "\"The soil is uneasy.\" / \"That is not humorous.\" / \"Talisolvanar should visit.\"" — day one (the phrase "The soil is uneasy" is also said in `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-01-the-search.md:63`, a quest event; the phrase is a habit, not an event).
- Line 15 (Never): "He never exaggerates, never laughs, and never ignores a disturbance in the earth." — day one.
- Line 17 (Sample, Greeting): "\"Good morning. The roses are well. Three people died in the Castle Ward last night.\"" — **the second sentence has no source.** The Grep for "Three people died", "died in the Castle Ward" and "Castle Ward last night" in `campaign/` returned no match. The nearest quest-time event is the Dock Ward disappearances, which are on Pier 17 and not in the Castle Ward (`campaign/gazetteer/waterdeep/dock-ward.md:126`: "three people have vanished from Pier 17 on three nights"). Flag. Drafter may keep "The roses are well." and restate or drop the second sentence.
- Line 18 (Sample, Business): "\"Something beneath the city is stirring. I do not know what. I would like you to find out.\"" — **request to act.** It is a standing request, but it asks the party to investigate, which is the hook of the Enclave's quests. Flag. A day-one version would be the Enclave's ask in `campaign/guides/factions/04-emerald-enclave.md:20`, "What the Enclave asks for:", which lists accounts of aberrant creatures. Drafter's call.
- Line 19 (Sample, Under pressure): "\"Stand behind the oak. The roots will hold them.\"" — day one.

Profile lines 5 to 19 are otherwise day one.

---

## D. Conflicts

**D1. Alignment (campaign Neutral Good against the published and wiki Chaotic Good)**
- Campaign, Summary: "> **Alignment.** Dragon Heist lists Melannor as Chaotic Good. The campaign keeps Neutral Good, and the Enclave events are written for it." — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:11`
- Campaign, gazetteer: "**Melannor Fellbranch (Neutral Good, Half-Elf, he/him)**" — `campaign/gazetteer/waterdeep/southern-ward.md:107`
- Campaign, Enclave Draft Notes: "> - **Conflicts, Melannor's alignment:** *Dragon Heist* lists Chaotic Good, and his Notable Figures page keeps Neutral Good (`01-melannor-fellbranch.md:11`). The page states no alignment for him, so it only reports this." — `campaign/setting/organizations/03-emerald-enclave.md:162`
- Adventure: "Melannor is chaotic good." — `sources/adventure-wdh.json:3705`
- Wiki: "| alignment5e    = [[Chaotic good]]" — wiki line 57
- Higher-ranked source: the campaign (Neutral Good), because campaign decisions outrank the published adventure (brief ruling 12). The Enclave's own Draft Note says the page "states no alignment", but the Summary states one. The orchestrator decides whether the Summary keeps it.

**D2. Who leads the Waterdeep agents (wiki against campaign)**
- Wiki: "He also directed the Emerald Enclave agents in the city with [[Jeryth Phaulkon]], a [[Chosen]] of [[Mielikki]]." — wiki line 65 (edition: 5e)
- Campaign: "Jeryth is the highest Enclave authority in Waterdeep, and Melannor serves her and carries her words to the Enclave's members." — `campaign/setting/organizations/03-emerald-enclave.md:52`
- Adventure: "He is joined by Jeryth Phaulkon, a noblewoman turned demigod who serves Mielikki, divine lady of the forest." — `sources/adventure-wdh.json:1320` (the adventure does not say who leads)
- Higher-ranked source: the campaign. The page follows "serves her and carries her words" (Persona and Relationships already do).

**D3. Stat block label (no conflict, noted for the drafter)**
- The Summary calls the stat block "Druid" (`01-melannor-fellbranch.md:5`). The adventure gives "a half-elf {@creature druid}, with these changes" (`sources/adventure-wdh.json:3701`). The campaign and adventure agree. The wiki gives class5e "Druid" (wiki line 59). The Mielikki and Harpers style "WDH custom block, CR 9" (Mirt) does not apply to Melannor: no CR is given for him in any source.

**D4. Frequency of in-person appearances (page against Enclave page)**
- Page: "which happens more often as the year goes on" — `01-melannor-fellbranch.md:25`
- Enclave page: "he appears in person only when the situation demands it" — `campaign/setting/organizations/03-emerald-enclave.md:55`
- Not a contradiction in the campaign; the page clause is a trend that the Enclave page does not state. Drafter restates (section C row 10).

**D5. Sibling (no conflict)** Adventure silent (`sources/adventure-wdh.json` shows no "brother" for Melannor). Wiki line 75, Talisolvanar page line 25, First Meeting line 68 and Appendix D line 1244 all say brother. Settled as day one (A2).

**D6. Pronouns and sex (no conflict)** he/him in the campaign (`01-melannor-fellbranch.md:5`), "Male" in the wiki (line 13), "He" in the adventure (`sources/adventure-wdh.json:3700`).

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/guides/factions/04-emerald-enclave.md:13`: "Kolat Towers stands one block north of Phaulkonmere, and nobody in the Enclave points at it before that gate." Not stale for Melannor: it states the same geometry as `sources/adventure-wdh.json:3700` ("a compound located one block south of Kolat Towers"). Listed so the drafter does not read it as a conflict.
- `campaign/guides/factions/04-emerald-enclave.md:32`: "Enclave druids feel an infernal influence in the Sea Ward." The campaign places it in the Southern Ward (`campaign/gazetteer/waterdeep/southern-ward.md:121`). Org Draft Notes already flag this as stale (`03-emerald-enclave.md:159`). Not Melannor's line; listed because the Factions Guide is the Melannor's faction guide.
- `campaign/gazetteer/waterdeep/southern-ward.md:121`: "Jeryth's Southern Ward report in **Summerstrider** is that she has felt a wound in the ley lines near Coachlamp Lane for a tenday and a half, and she senses infernal influence there." Quest-time reference (names a quest event). Org Draft Note `03-emerald-enclave.md:164` records the conflict with `arc-e-faction-outposts.md:85` ("for two weeks").
- `campaign/setting/deities/eldath.md:104` names the Enclave's patron as Mielikki through Jeryth; not a Melannor line; the org Draft Notes already flag it (`03-emerald-enclave.md:187`).
- `campaign/setting/organizations/03-emerald-enclave.md:187` (Draft Notes) lists the other files found wrong, including `02-jeryth-phaulkon.md:34` (the Jeryth page; not this page).
- `sources/Appendix_D_-_Running_the_Tavern.md:806`: the Enclave row of the Trollskull Manor advice. It names Jeryth's *Fabricate* and not Melannor's services. Relevant to Jeryth, see her notes.

**E2. Routed quest references (quest time; the day-one page does not restate them)**

Melannor's quest appearances, by file and line where it is quoted:
- `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:8` ("Meet Melannor Fellbranch inside the gate, where he asks after his brother Talisolvanar, and walk the garden with him."), `:31` (the cat carries his message), `:68` and `:74` (see A2)
- `campaign/quests/faction-events/emerald-enclave/m01-the-undercliff-scarecrows/ev-01-the-undercliff-scarecrows.md:7` ("Take Melannor's 24-word message, or walk to Phaulkonmere and question him in person.")
- `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/overview.md:17` ("At 08:00 Melannor Fellbranch comes to Trollskull Manor himself, with mud on his boots and a folded sketch in his hand.")
- `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-01-the-search.md:20` ("Melannor comes in person because the cats and gulls of the Dock Ward have left, and twenty-five words cannot carry what he has to say.")
- `campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:177` ("Contact: Melannor, at the gate or in the garden by day.")
- `campaign/quests/faction-events/emerald-enclave/r10-autumnreaver/ev-01-autumnreaver.md:5` ("Melannor Fellbranch comes to the member's door in person, walks them to Phaulkonmere and names the rank.")
- `campaign/quests/faction-events/emerald-enclave/m06-the-dreamers-reach/overview.md:85` (Jeryth has fallen silent; "Melannor sends the party down an old drain to find what is pressing on her.")
- `campaign/structure/arc-e-faction-outposts.md:85` ("*Melannor Fellbranch (Emerald Enclave — renown 1+).* Jeryth Phaulkon has been monitoring a disturbance in the Southern Ward for two weeks.") and `:373` (Melannor asks whether the Coachlamp Lane disturbance was addressed)
- `campaign/structure/arc-f-xanathars-lair.md:35` ("*Melannor Fellbranch (Emerald Enclave — renown 1+).* Environmental displacement in the sewer tunnels below Skullport...") and `:296` ("- **Melannor:** \"Did anything unusual happen to the underground water systems near the collapse point?\"")
- `campaign/structure/arc-i-kolat-towers.md:37` ("*Melannor Fellbranch (Emerald Enclave — renown 1+).* Environmental damage in the immediate vicinity of the towers is distinctive.") and `:269` ("**Melannor Fellbranch (Emerald Enclave).** \"Is the force field down?\"")
- `campaign/guides/factions/04-emerald-enclave.md:30` (the minor ley line under Gralhund Villa, Melannor would like to hear what the party saw inside; quest hook)
- `campaign/guides/gm-guide/player-factions-overview.md:160` (table row naming Melannor's concerns) is day one.
- `sources/Appendix_C_-_Player_Faction_Missions.md:710` ("Melannor delivers this by *animal messenger* — a pigeon that lands on the windowsill of Trollskull Manor and speaks the briefing in his voice before flying away.")
- `sources/Appendix_C_-_Player_Faction_Missions.md:816` ("Melannor asks the party to convince Bonnie's doppelgangers to leave Waterdeep. The Enclave's concern is stability, not trustworthiness.")
- `sources/adventure-wdh.json:3700` (day-one: the main contact, see A1). `sources/adventure-wdh.json:3735` and `:3745` are mission rows (Undercliff scarecrows, Yawning Portal doppelgangers): quest time, routed.

---

## F. Gaps a Background would need that no source gives

Each gap gives the sourced facts the drafter must stay consistent with. Invented material carries `[design]` and is listed in Draft Notes (brief ruling 17).

1. **Birthplace, birth year, age, home before Waterdeep.** No source gives them. The wiki's `age` (wiki line 17), `dob` (line 21) and `home` fields list only "[[Waterdeep]], [[Sword Coast North]]" (wiki line 11). Consistent with: Melannor is a half-elf (wiki line 14; `sources/adventure-wdh.json:3701`).
2. **How he came to be groundskeeper and when.** No source. Consistent with: "a half-elf groundskeeper named" the Tarms and Phaulkons entrusted the estate to (`sources/adventure-wdh.json:1320`), and "Melannor Fellbranch ... was a groundskeeper and member of the Emerald Enclave in Waterdeep in 1492 DR" (wiki line 62).
3. **How he joined the Enclave.** No source. Consistent with: "Druids and rangers are especially welcome." is the adventure's rule for members (`sources/adventure-wdh.json:1318`), and "The Enclave seeks out characters who are naturalists, healers, or who have demonstrated concern for the natural world." (`sources/Appendix_B_-_Player_Factions.md:289`). Melannor himself is a druid (`sources/adventure-wdh.json:3701`).
4. **His brother's history.** The brother link is sourced (A2). No source says whether the brothers grew up together, which of them is older, or what Tally's shop cost him. Consistent with the Talisolvanar page: "Tally is the brother of Melannor Fellbranch ... a longtime neighbor of Fala Lefaliir and Embric."
5. **Parents, other family.** None in any source. Do not invent a family for him without `[design]`.
6. **Before the Enclave: any Waterdeep job, companions, a loss.** No source. The wiki infobox `formerhomes` is blank (wiki line 12).
7. **His personal goals.** No source. The campaign's Motivations (`01-melannor-fellbranch.md:19`) are the Enclave's and the house's. Consistent with: he "wants to protect Phaulkonmere and its gardens" and wants to "investigate disturbances he senses but cannot yet name" (his Motivations, day one).
8. **What he does when he is not on Enclave business.** None. The Trollskull Manor loan or tavern business is in the quest events, not a fact about him.
9. **Why he is humorless.** The campaign says it (`01-melannor-fellbranch.md:9`, `southern-ward.md:108`); no source gives a cause. A cause would be `[design]`.
10. **The relationship with Jeryth beyond service.** Consistent with: "He serves Jeryth Phaulkon and carries her few words" (`01-melannor-fellbranch.md:29`) and "the animals carry only Melannor's words" (`03-emerald-enclave.md:56`). No personal history between them is sourced.

---

## G. Source facts that hint at inner life (quotes only; the Background must not contradict them)

- **Fondness for creatures.** "He liked [[pigeon]]s and [[cat]]s and always used them as couriers for his faction." — wiki line 70 (edition: 5e, `WDH5e-p35-36`). Also `sources/adventure-wdh.json:3700`: "is partial to using cats and pigeons as couriers".
- **Care for the nest.** "a nest he has been monitoring in the old oak since early spring." — `sources/Appendix_B_-_Player_Factions.md:328`
- **Free care for visitors' animals.** "provides free food and care for the adventurers' animals at Phaulkonmere." — `sources/adventure-wdh.json:1327`
- **Relief as a private matter.** "He goes silent when he hears good news, because he finds even relief a private matter." — `01-melannor-fellbranch.md:27`
- **A worry he cannot name.** "a careful watchfulness that deepens when he cannot articulate what feels wrong." — `01-melannor-fellbranch.md:17`; and "Deep down, he senses something wrong in the earth beneath the Castle Ward and cannot say what it is." — `01-melannor-fellbranch.md:25`
- **Unease under a calm voice.** "His unease about the thing below the Castle Ward comes out as uncharacteristic hesitations and unfinished sentences." — `.claude/skills/character-voices/voices/emerald-enclave.md:12`
- **Brother.** "make sure his brother Melannor actually visits once in a while." — `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md:15` (Tally's wish, the one clear hint of Melannor's own absence). "Talisolvanar should visit when his work in the alley allows it." — `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:74`
- **Calculated visit to his brother's alley.** "framing it as a casual visit that is clearly calculated." — `sources/Appendix_D_-_Running_the_Tavern.md:1244` (Alexandrian; this is an agenda for Tally's meeting, not Melannor's own).
- **Balance over nature.** "\"Balance is a better word. What we watch for are disruptions — things that shouldn't be where they are, pulling at what keeps the world from unraveling.\"" — `sources/Appendix_B_-_Player_Factions.md:331`
- **Honesty about the work.** "\"We offer honest work and the knowledge that it matters. We also offer this garden, as a place to come to when the rest of Waterdeep becomes too much.\"" — `sources/Appendix_B_-_Player_Factions.md:332`. The Factions Guide repeats the idea (`campaign/guides/factions/04-emerald-enclave.md:40`).
- **Rule he will not break.** "He never ignores a disturbance in the earth." — voice `emerald-enclave.md:15`.
- **Sense of the city.** The Enclave's keeper "reports grim news in the tone of a man describing the weather" (`03-emerald-enclave.md:55`). The wording is the voice's and the Enclave's; the grim news is not named in any day-one file.

---

## Draft Notes material for the drafter (short)

- Settled: sibling link (A2); Neutral Good (D1, the campaign keeps it); Southern Ward; "Half-Elf"; he/him; Druid with the traits (B).
- Open for the orchestrator: D1 (alignment); the Summary line 11 wording; whether the Summary keeps "Neutral Good" once the Draft Notes say the page states none.
- Open for the drafter: the Greeting sample "Three people died in the Castle Ward last night." (no source); the Business sample (`emerald-enclave.md:18`).
- Not run: `voicecheck.py`.
