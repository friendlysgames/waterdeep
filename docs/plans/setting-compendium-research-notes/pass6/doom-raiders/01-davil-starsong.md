# Pass 6 research notes: Davil Starsong

Page: `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Davil is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/06-doom-raiders.md` (H1: "# The Zhentarim (Doom Raiders)")
Factions Guide: `campaign/guides/factions/07-doom-raiders.md`
Villains page: none (the Doom Raiders are a player faction; no villain page exists for them).
Voice profile: `.claude/skills/character-voices/voices/doom-raiders.md` (### Davil Starsong, lines 7-22)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field is given where the entry has one (the Davil entry is `"page": 40` at line 4008; the Doom Raiders group entry is `"page": 198` at line 31920).
- Appendix B, C and D: `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md`, `sources/Appendix_D_-_Running_the_Tavern.md`. Read with the Read tool.
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` was read as rendered images (PDF pp.2-3 = printed pp.24-25). The Zhentarim sentence is on printed p.25. It is a transcription from the image. Check with `pdftotext -layout` before any quote goes into prose. The PDF names no Davil text.
- Wiki: the scratchpad extract `wiki-doom-raiders/01-davil-starsong.txt` is the Davil page. It is quoted as "wiki line N" (that file's lines). Edition tags come from the wiki's infobox `refs5e` and `ref` names. The wiki prints no edition on most sentences. The bundle `sources/research/pass5-bundles/doom-raiders/wiki.txt` carries the same page; its line 9 is the Doom Raiders `leader` field.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **Where Davil does business is in conflict.** The published adventure says he "does all his business in the establishment's taproom" (`sources/adventure-wdh.json:31924`). The campaign's first-meeting event and the page say a curtained room on the second floor. The organization page's GM Notes keep the taproom wording (`06-doom-raiders.md:113`). See D1.
2. **The stat block "Swashbuckler (with modifications)" has no source.** No line of the published adventure gives Davil a creature block, and the wiki gives "Bard 12" and "challenge5e = 6" with no adventure support (wiki lines 58 and 59). "Swashbuckler" is not a 2024 name in the campaign's own Bregan D'aerthe mechanics reference (`docs/plans/bregan-daerthe-mechanics-reference.md:410`). See D3 and D4.
3. **Arrival date is in conflict.** The organization page fixes 1489 DR (`06-doom-raiders.md:25`). The adventure says "three years ago" (`sources/adventure-wdh.json:31916`). Appendix B says "about four years ago" (`sources/Appendix_B_-_Player_Factions.md:636`). See D2.
4. **Skeemo grief is quest-time.** The Emotions line ("private grief over Skeemo's betrayal") and the Morale line ("After his arrest and return") depend on events that the Doom Raiders' own files place after Mission 4 and Davil's release (`campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:15`). See C1 and D5.
5. **The Overview is over the limit.** It runs 44 words (page line 29). The brief's limit is 21 words. The drafter must cut it.
6. **The "Nihiloor's intellect devourer" clause does not match the adventure.** The adventure gives the devourer that watches Davil to Meloon, under Xanathar (`sources/adventure-wdh.json:1548`). It does not link Davil to Nihiloor. See D6.

---

## A. Background facts by theme

### A1. Origin, family, early life

**Wiki, lead (edition: 5e, `WDH-198-199`)**
> "'''Davil Starsong''' ({{Pronounce|DAH|vil|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a [[sun elf]] agent of the [[Zhentarim]], operating within the city of [[Waterdeep]] during the late 15{{th}} century [[DR]]. He was known to keep a room at the [[Yawning Portal]], conducting all his business in the taproom.<ref name="WDH-198-199" /><ref name="WDH5e-p39-40">{{Cite book/Waterdeep: Dragon Heist|39-40}}</ref>"
> — wiki line 62 (edition: 5e; refs `WDH-198-199`, `WDH5e-p39-40`)

**Wiki, infobox home and race (5e)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]"
> — wiki line 11
> "| race           = [[Sun elf]]<ref name="WDH-198-199" />"
> — wiki line 14

**Wiki, infobox fields left blank (5e)**
> "| dob            = "
> — wiki line 21
> "| age            = "
> — wiki line 17
> "| parents        = "
> — wiki line 29
> "| siblings       = "
> — wiki line 31

**Adventure, Doom Raiders entry (page 198; the sun elf, the magic and the patience)**
> "Like many sun elves, Davil has an affinity for magic and is gifted with the kind of patience that comes with a long life span. Unlike most, he's not the least bit pretentious or aloof. He keeps a room at the Yawning Portal and does all his business in the establishment's taproom. He negotiates deals with grace and aplomb, even while drunk, and uses an elven lute as a spellcasting focus."
> — `sources/adventure-wdh.json:31924` (entry "Davil Starsong", `"page": 198` at line 31920)

**Wiki, Personality (5e)**
> "Davil Starsong was naturally capable of finding profitable business deals and making friends, which was ideal for his position within the Black Network. Being a sun elf, he had a natural aptitude for [[arcane]] [[magic]], making him a fine [[bard]], along with having the patience of someone who might live ten times longer than even his most fortunate friends. Unlike other sun elves, he was not aloof nor pretentious. He always traded with grace and aplomb even when drunk.<ref name="WDH-198-199" />"
> — wiki line 65 (edition: 5e, `WDH-198-199`). "Bard" here is the wiki's claim; the adventure does not name a class (see D4).

No source gives Davil's birth year, age, parents, siblings, a home town other than Waterdeep, or the place he came from before the Doom Raiders. The published adventure's only age term is "a long life span" (line 31924).

### A2. The adventuring years and the five

**Adventure, Doom Raiders group entry (page 198; the five, the lich lairs, the arrival)**
> "The Doom Raiders were five unscrupulous adventurers who liked to plunder lich lairs (called \"dooms\" by some). They gave up adventuring to join the Black Network and came to Waterdeep three years ago with plans to establish a Zhentarim foothold in the city. In that time, they have forged alliances with various nobles and guilds and run afoul of others, all the while fending off Harper spies."
> — `sources/adventure-wdh.json:31916` (the group entry, which sits before the Davil entry at line 31919)

**Adventure, Zhentarim faction entry (page 17; the five leaders)**
> "The Doom Raiders (described in appendix B) consider themselves the true Zhentarim of Waterdeep. The group's leaders are {@creature Davil Starsong|WDH} (Master of Opportunities and Negotiations), {@creature Istrid Horn|WDH} (Master of Trade and Coin), {@creature Skeemo Weirdbottle|WDH} (Master of Magic), {@creature Tashlyn Yafeera|WDH} (Master of Arms and Mercenaries), and {@creature Ziraj the Hunter|WDH} (Master of Assassination)."
> — `sources/adventure-wdh.json:1447` (entry "Zhentarim", `"page": 17` at line 1440)

**Adventure, Davil entry (page 40; how they joined)**
> "Davil is a retired adventurer. He and his adventuring companions joined the Zhentarim a few years back. They help people in need. (More specifically, they provide loans, mercenaries, and other services.)"
> — `sources/adventure-wdh.json:4015` (entry "Davil Starsong", `"page": 40` at line 4008)

**Wiki, Davil's history (5e, `WDH-40`)**
> "Davil was once an adventurer but together with his adventuring companions he decided to join the Zhentarim."
> — wiki line 74 (edition: 5e, `WDH-40`)

**Appendix B, Doom Raiders faction creed (Alexandrian; the faction, not Davil)**
> "The Doom Raiders are professional criminals who prefer contracts to confrontations, and who sincerely believe the Black Network works best when it operates like a legitimate enterprise. They are not good, but they are not sadistic, and they can be trusted to honor their agreements."
> — `sources/Appendix_B_-_Player_Factions.md:508`

**First-meeting dialogue (campaign quest file; the backstory is day-one, the scene is quest-time)**
> "> > \"Five of us started it, back when we were still walking into dungeons for coin. Yagra came along later, once she'd given us good reason to keep her. Between us we've built a few honest businesses and a few less honest ones, and the profit pays for people who need help. You'd be surprised how many do, yes?\""
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:236` (Davil's speech; the scene itself is the First Meeting event)

### A3. Arrival in Waterdeep, the post, the rise

**Campaign, Organization page, the 1489 arrival (day-one)**
> "- **1489 DR, the cell reaches Waterdeep:** The Doom Raiders are a cell of experienced Zhentarim operators who arrived in Waterdeep in 1489 DR, the first Zhentarim cell in the city, and built a network of commercial fronts they genuinely believe in. They were sent to establish a Zhentarim foothold, and no source names who sent them (*Dragon Heist*, 5e; Forgotten Realms Wiki, *Doom Raiders*, 5e)."
> — `campaign/setting/organizations/06-doom-raiders.md:25` (the rest of the bullet is "In the three years since, they have forged alliances with various nobles and guilds, run afoul of others and fended off Harper spies (*Dragon Heist*, 5e).")

**Wiki, the 1489 posting (5e, `WDH-198-199`)**
> "In the year [[1489 DR]], they were directed to establish a Zhent foothold in Waterdeep.<ref name="WDH-198-199" />"
> — wiki line 74 (edition: 5e)

**Wiki, title and occupation (5e)**
> "| occupation     = Master of Opportunities and Negotiations for the [[Zhentarim]]<ref name="WDH-198-199" />"
> — wiki line 16 (edition: 5e)

**Adventure, Davil's title and the Black Network division (page 198)**
> "Within the Waterdeep division of the Black Network, {@creature Davil Starsong|wdh|Davil} is accorded the title of Master of Opportunities and Negotiations because he's good at sniffing out lucrative business deals, and he makes friends easily."
> — `sources/adventure-wdh.json:31923` (entry "Davil Starsong", page 198)

**Adventure, what Davil can do for the party (page 198)**
> "Davil can put the characters in contact with other leaders of the Black Network's Waterdeep division, namely {@creature Istrid Horn|WDH} (if they need a loan), {@creature Skeemo Weirdbottle|WDH} (if they need magic), {@creature Tashlyn Yafeera|WDH} (if they need weapons or mercenaries), and {@creature Ziraj the Hunter|WDH} (if they need a highly skilled assassin)."
> — `sources/adventure-wdh.json:31925` (page 198)

**Campaign, Organization page, the Master's entry (day-one post)**
> "- **Davil Starsong, Master of Opportunities and Negotiations:** He sniffs out profitable deals, makes friends easily and can arrange meetings with influential nobles and guild members. He leads the Waterdeep operation and holds court at the Yawning Portal."
> — `campaign/setting/organizations/06-doom-raiders.md:57`

**Campaign, Organization page, the Primary Contact (day-one post)**
> "**Primary Contact:** Davil Starsong — a sun elf retired adventurer who leads the Doom Raiders' Waterdeep operation. Charming, direct, and genuinely invested in ending the street violence Manshoon's cell has caused. Tashlyn Yafeera handles the cell's business whenever Davil is unavailable."
> — `campaign/setting/organizations/06-doom-raiders.md:49`

**Campaign, Organization page, leader status (day-one)**
> "Davil is the leader, as the wiki infobox and the published adventure agree (Forgotten Realms Wiki, *Doom Raiders*, 5e), and Tashlyn speaks for the cell when he is away."
> — `campaign/setting/organizations/06-doom-raiders.md:63`

**Wiki, the Doom Raiders leader field (pass 5 bundle, 5e)**
> "| leader         = [[Davil Starsong]]"
> — `sources/research/pass5-bundles/doom-raiders/wiki.txt:9`

**Campaign, the state on Ches 1, 1492 DR (day-one)**
> "Davil keeps his room at the Yawning Portal, Istrid lends from her warehouse, Skeemo keeps his shop and Tashlyn keeps her post at the South Gate."
> — `campaign/setting/organizations/06-doom-raiders.md:29` (the same bullet opens "**Ches 1, 1492 DR, the campaign opens:**")

**Campaign, first-meeting event, his hours (day-one; the event file is quest-time for the meeting itself)**
> "> Davil sits in his second-floor room from 8 p.m. until midnight every evening, and Yagra is at the bar from sundown until closing."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:49` (the rest of the paragraph covers how candidates are taken upstairs)

### A4. Business, the Yawning Portal, habits and belongings

**Adventure, business habit and lute (page 198)**
> "He keeps a room at the Yawning Portal and does all his business in the establishment's taproom. He negotiates deals with grace and aplomb, even while drunk, and uses an elven lute as a spellcasting focus."
> — `sources/adventure-wdh.json:31924` (see D1 for the conflict)

**Wiki, the lute (5e)**
> "He used an elven [[lute]] as a spellcasting focus.<ref name="WDH-198-199" />"
> — wiki line 71 (edition: 5e, `WDH-198-199`)

**Campaign, the business room (first-meeting event; the layout is day-one)**
> "> Davil's business room is at the far end of the second-floor landing behind a heavy green curtain. It holds a round table, two hanging lamps, a decanter and enough chairs for everyone in the party, because Yagra brings more from the landing. His lute leans against the wall. The trophies on his charm bracelet come from monsters the Doom Raiders have killed, and it rattles softly when he pours. Davil pours for guests before he says anything else."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:164`

**Campaign, the suite (day-one)**
> "- **Davil pays.** Davil is a permanent resident who rents this room and the suite above it, and Durnan charges every paying guest the standard prices, whatever the guest does for a living. Durnan has no quarrel with the Doom Raiders, so he has no reason to turn away their money."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:170`

**Campaign, Davil and Durnan (day-one; the design note in the event file)**
> "- **Two old adventurers understand each other.** Davil is a retired adventurer like Durnan, and neither asks the other about the past."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:174`

**Campaign, the charm bracelet (day-one)**
> "To the world, Davil is the Master of Opportunities and Negotiations: a sun elf who makes friends easily, negotiates deals with grace even while drunk, speaks with a lilt he attributes to his elven heritage, and wears a charm bracelet hung with small trophies from monsters the Doom Raiders have killed."
> — `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:21` (the page's own Persona; its source for the trophies is `ev-01-first-meeting.md:164`, quoted above)

**Campaign, Organization GM Notes (the taproom wording; see D1)**
> "> - **Davil at the Yawning Portal:** Davil keeps a room upstairs and does all his business in the taproom, which he has decided is safer than a private office and more honest than a warehouse. He is a sun elf who negotiates with grace even when he has been drinking, which is most of the time. He uses an elven lute as a spellcasting focus and carries it on his back in every meeting."
> — `campaign/setting/organizations/06-doom-raiders.md:113`

**Adventure, the peace motive (day-one; the second bullet of the list Davil gives the party, page 40)**
> "Davil and his colleagues want to end the violence and restore the peace."
> — `sources/adventure-wdh.json:4016`

**Campaign, Organization page, the moral ledger (day-one)**
> "- **A Quiet City Is Good for Business:** Davil is invested in ending the street violence that the rival cell has caused. A legitimate criminal enterprise cannot run in a city where an illegitimate one keeps shooting people. He keeps the moral ledger as balanced as his business allows. Davil also prefers to keep the peace with Xanathar's Guild through negotiation, and he tells newcomers that he and his colleagues want to restore peace to the streets (**Davil Starsong**; *Dragon Heist*, 5e)."
> — `campaign/setting/organizations/06-doom-raiders.md:40`

### A5. The Doom Raiders' suspicion, Skeemo and the leak (day-one parts only)

**Campaign, Skeemo's Secret (GM truth; day-one for the GM, not for Davil's public face)**
> "> - **Skeemo Weirdbottle is a traitor:** Skeemo has been feeding intelligence to Manshoon's cell and to House Gralhund since well before 1 Ches 1492 DR. Manshoon bought him with rare alchemical components and protection from Watch inspections, and Skeemo sends messages to both sides by paper bird. Davil was fond of him and does not say so aloud."
> — `campaign/setting/organizations/06-doom-raiders.md:120`

**Campaign, Factions Guide (the same Secret, one line)**
> "**Skeemo Weirdbottle has been a traitor from the start.** The Master of Magic has been feeding intelligence to Manshoon's cell and to House Gralhund since before the party was recruited. Everything the party has done for the faction has been visible to the Splinter. Davil has suspected something for months. Tashlyn confirmed it during his arrest."
> — `campaign/guides/factions/07-doom-raiders.md:11` (the last sentence is quest-time; see C1 and D5)

**Campaign, the leak suspicion (day-one)**
> "> Davil also suspects that someone inside his own cell is leaking to the other side, and he tells nobody. He has never spoken that suspicion aloud, and he will not speak it tonight."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:25`

**Campaign, the leak suspicion, the Organization page (day-one)**
> "> - **Davil's suspicion:** Davil suspects that someone inside his own cell is leaking to the other side, and he has told nobody."
> — `campaign/setting/organizations/06-doom-raiders.md:116`

**Adventure, Mission 3 brief (quest-time; the friendship is day-one)**
> "\"There's a shop in the Trades Ward called Weirdbottle's Concoctions. The gnome who runs it is a friend of ours named Skeemo.\""
> — `sources/adventure-wdh.json:4059` (the Zhentarim Missions table, page 40; the words are the faction's brief, not Davil's own speech, and the mission is quest-time)

### A6. Relationships to named figures

**Ziraj (friends list, page 201)**
> "If Ziraj sets out to kill someone, it's because one of his friends (Davil, Istrid, Skeemo, or Tashlyn) asked him to."
> — `sources/adventure-wdh.json:31965`

**Yagra (bodyguard, page 20)**
> "Yagra is a Black Network mercenary who gets paid to protect a Zhent negotiator named {@creature Davil Starsong|WDH} (see {@adventure appendix B|WDH|12} for more information on him)."
> — `sources/adventure-wdh.json:1569` (entry "Yagra Stonefist", page 20)

**Tashlyn (Master of Arms and Mercenaries; Davil's second voice)**
> "Tashlyn handles the cell's business whenever Davil is unavailable."
> — `campaign/setting/organizations/06-doom-raiders.md:49` (the Primary Contact bullet, quoted in full in A3)

**Istrid (the five, the companions)**
> "If those resources prove inadequate, Istrid can call on her old adventuring companions for assistance."
> — `sources/adventure-wdh.json:31935` (Istrid's entry, page 199; the "old adventuring companions" are the five, line 1447)

**Meloon (watching Davil; see D6)**
> "He has his eye on {@creature Davil Starsong|WDH} (see {@adventure appendix B|WDH|12}) but won't kill the elf in plain view of witnesses."
> — `sources/adventure-wdh.json:1548` (entry "Meloon Wardragon", page 20)

**Threestrings (a Harper watcher at the Portal, not a Doom Raider)**
> "Mattrim \"Threestrings\" Mereg, a Harper agent, spends his afternoons and evenings at the Yawning Portal watching Zhentarim agents"
> — `campaign/setting/organizations/06-doom-raiders.md:81` (the bullet continues "(*Dragon Heist*, 5e; **Castle Ward**)"; per brief ruling 6 he is a Harper agent)

### A7. Faith and deity

No source gives Davil a faith. The only deity tied to the cell's members is Vergadain, for Istrid.
> "Istrid worships Vergadain, the dwarven god of wealth and luck."
> — `sources/adventure-wdh.json:31935` (Istrid's entry, page 199). Davil's entry (lines 31919 to 31926) names no god. The Organization page's Doctrine bullet says the cell has "no sourced creed or initiation" (`06-doom-raiders.md:43`).

### A8. Signature belongings

- Elven lute, spellcasting focus: `sources/adventure-wdh.json:31924` (quoted in A4); wiki line 71 (quoted in A4).
- Charm bracelet with monster trophies: `ev-01-first-meeting.md:164` (quoted in A4); the page's Persona line 21.

### A9. How long in post

- 1489 DR (Organization page `06-doom-raiders.md:25`): the campaign's date for the cell's arrival.
- "three years ago" (`sources/adventure-wdh.json:31916`): the adventure's relative date for the cell's arrival.
- "about four years ago" (`sources/Appendix_B_-_Player_Factions.md:636`): conflict, see D2.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page's Summary: "> - *Sun elf bard, neutral, he/him*. Stat block: **Swashbuckler (with modifications)**." — `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:5`
- Campaign, first-meeting event tag: "> Davil Starsong (Neutral, Sun Elf, he/him) :: The leader of the Doom Raiders, a retired adventurer who makes every arrangement sound like a favor." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:188`
- Campaign, quest tag (Davil's return event): "> Davil Starsong (Neutral, Sun Elf, he/him) :: the Doom Raiders' cell leader, home from Castle Waterdeep, and slower to smile than he used to be." — `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:78` (quest-time tag; the alignment matches)
- Wiki: "| alignment5e    = [[Neutral]]" — wiki line 57 (edition: 5e)
- Adventure: no alignment line in the Davil entry (lines 31919 to 31926) or the Zhentarim entry (lines 1438 to 1459). Do not claim the adventure sets alignment.

**Species**
- Campaign, the page's Summary: "*Sun elf bard, neutral, he/him*" (`01-davil-starsong.md:5`)
- Campaign, the organization page: "a sun elf retired adventurer" (`06-doom-raiders.md:49`, quoted in A3)
- Wiki: "| race           = [[Sun elf]]<ref name="WDH-198-199" />" — wiki line 14 (5e)
- Adventure: "Like many sun elves, Davil has an affinity for magic" (`sources/adventure-wdh.json:31924`). Implied, not an explicit species line.

**Pronouns**
- Campaign: "he/him" (`01-davil-starsong.md:5`); "Sun Elf, he/him" (`ev-01-first-meeting.md:188`).
- Adventure: "He keeps a room at the Yawning Portal" (`sources/adventure-wdh.json:31924`), "He negotiates deals with grace" (same line).
- Wiki: "| sex            = Male<ref name="WDH-198-199">{{Cite book/Waterdeep: Dragon Heist|198-199}}</ref>" — wiki line 13 (5e)

**Affiliation**
- Campaign, the page's Summary: "> - **Affiliation:** Zhentarim (Doom Raiders)" — `01-davil-starsong.md:6`
- Campaign, the organization page H1: "# The Zhentarim (Doom Raiders)" — `06-doom-raiders.md:1`. Its Summary: "> - **Campaign role:** Player faction; the legitimate Black Network cell in Waterdeep, here since 1489 DR and at active war with Manshoon's Zhentarim splinter." — `06-doom-raiders.md:7`
- Campaign, the Two Zhentarims rule: "> Manshoon's splinter cell and Davil Starsong's Doom Raiders are entirely separate organizations. They share a name and a history and nothing else. Never conflate them in NPC dialogue." — `campaign/setting/villains/manshoon.md:19`
- Campaign, the organization page's "Not the villain Zhentarim" line: "> - **Not the villain Zhentarim:** the cell that answers to Manshoon is on the **Manshoon's Zhentarim** page in Organizations. Never conflate the two." — `06-doom-raiders.md:9`
- Adventure: "The Doom Raiders (described in appendix B) consider themselves the true Zhentarim of Waterdeep." — `sources/adventure-wdh.json:1447`
- Alexandrian: "**Warning: Two Zhentarims**" callout: "The Doom Raiders and Manshoon's faction are at active internal war. A character who joins the Doom Raiders is joining one half of a fractured organization and will inevitably be pulled into the conflict between them. Information shared with the Doom Raiders will not reach Manshoon's agents — the two cells actively despise each other." — `sources/Appendix_B_-_Player_Factions.md:518`
- Wiki: "| occupation     = Master of Opportunities and Negotiations for the [[Zhentarim]]" — wiki line 16 (5e). The wiki's Zhentarim page makes the whole organization Manshoon's company; the campaign does not (see D7).

**Stat block**
- Campaign, the page's Summary: "Stat block: **Swashbuckler (with modifications)**." — `01-davil-starsong.md:5`
- Campaign, pass-5 notes, which copied the same Summary line: "- *Sun elf bard, neutral, he/him*. Stat block: **Swashbuckler (with modifications)**." — `docs/plans/setting-compendium-research-notes/pass5/doom-raiders.md:146`
- Adventure: no creature block, no CR, no AC, no HP for Davil in lines 31919 to 31926 or 4007 to 4019.
- Wiki: "| challenge5e    = 6" — wiki line 58 (5e; the refs for the block are on line 60); "| class5e        = {{Class table|edition=5e|[[Bard]]|12}}" — wiki line 59 (5e; `refs5e` = `WDH-198-199`, line 60)
- Campaign mechanics reference: the Doom Raiders reference says "Thug and Veteran do not exist in XMM" (`docs/plans/doom-raiders-mechanics-reference.md:13`). It names no Davil block. The Bregan D'aerthe reference says "No 2024 Swashbuckler; CR 8 if heavily modified" (`docs/plans/bregan-daerthe-mechanics-reference.md:410`).

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md`. The page has no Background, Personality or Connections section yet. Each row gives the sentence exactly and the file where the event already lives.

### C1. Page sentences

| # | Line | Sentence (exact) | Status | Where the event already lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Sun elf bard, neutral, he/him*. Stat block: **Swashbuckler (with modifications)**." | Day-one name tag. The stat block is unsourced (B, D3) | section B |
| 2 | L7 | "> - **Featured in:** **Finding Floon**, **Trollskull Alley**, **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **Doom Raiders Mission 1 — The Dockside Killer**, **Doom Raiders Mission 2 — The Poisoned Delivery**, **Doom Raiders Mission 3 — The Missing Snobeedle**, **Doom Raiders Mission 4 — Silencing Skeemo**, **Doom Raiders Mission 5 — The Yellowspire Job**, **Doom Raiders Mission 6 — Ziraj's Last Hunt**, **Lords' Alliance Mission 3 — The Red Wizard's Price**" | Quest-name list (routed) | `campaign/quests/` folders; Factions Guide Missions table `campaign/guides/factions/07-doom-raiders.md:66` to `:71` |
| 3 | L11 | "**Resonance.** Davil should inspire liking with his effortless charm, unease with the silence behind his questions, and sympathy when his arrest and return reveal the cost of leading a faction that eats its own." | **Quest-time** clause "when his arrest and return reveal the cost of leading a faction that eats its own." The first two clauses are day-one (ruling 1) | Arrest: `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:5` ("Davil Starsong is taken to Castle Waterdeep on Ches 26"); return: `s02-davils-return/ev-01-davils-return.md:5`; Factions Guide `campaign/guides/factions/07-doom-raiders.md:30` and `:73`; adventure `sources/adventure-wdh.json:4028` ("he is arrested by the City Watch") and `:4038` ("Weeks after his arrest, Davil is released from custody") |
| 4 | L13 | "**Emotions.** Davil most often feels affable warmth, strategic patience, real fondness for capable people, private grief over Skeemo's betrayal, careful deliberation, and a sadness he expresses through music rather than words." | **Quest-time clause** "private grief over Skeemo's betrayal" presupposes a discovery (D5). The rest is day-one | `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:15` and `:27` (Davil learns of the betrayal from Tashlyn after release); `campaign/guides/factions/07-doom-raiders.md:11` |
| 5 | L15 | "**Motivations.** Davil wants to keep the Doom Raiders operational and independent from Manshoon's splinter, maintain peace with Xanathar's Guild through negotiation rather than violence, and protect the people who chose to follow him." | Day-one. Keep (ruling 3) | `campaign/setting/organizations/06-doom-raiders.md:40` and `:87` |
| 6 | L17 | "**Inspirations.** When playing Davil, channel Havelock Vetinari (*Discworld*), Iroh (*Avatar: The Last Airbender*), and Michael Corleone (*The Godfather*)." | Not a fact. Keep | n/a |
| 7 | L21 | "**Persona.** To the world, Davil is the Master of Opportunities and Negotiations: a sun elf who makes friends easily, negotiates deals with grace even while drunk, speaks with a lilt he attributes to his elven heritage, and wears a charm bracelet hung with small trophies from monsters the Doom Raiders have killed. He conducts business from a curtained room on the Yawning Portal's second floor, with a permanent suite on the third. To those he trusts, he is a retired adventurer who joined the Zhentarim with his companions and frames the whole enterprise as helping people in need. Deep down, he withholds explanation and lets things sit, showing interest without revealing why, and he was fond of Skeemo in a way he does not say aloud." | Day-one. The "curtained room" clause conflicts with the adventure's taproom (D1). The rest matches the sources in A and B | `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:164` and `:170`; `sources/adventure-wdh.json:31924`; `06-doom-raiders.md:120` |
| 8 | L23 | "**Morale.** In a fight, Davil would attempt negotiation first, fight with a swashbuckler's precision second, and retreat to preserve the Doom Raiders' leadership structure third. After his arrest and return, he fights more deliberately: the warmth is still there, quieter now." | **Quest-time** second sentence ("After his arrest and return, he fights more deliberately: the warmth is still there, quieter now."). The first sentence is day-one | First sentence: `campaign/setting/organizations/06-doom-raiders.md:74` ("Davil negotiates first, fights with a swashbuckler's precision second and retreats to protect the cell's leadership third"). Second sentence: `s02-davils-return/ev-01-davils-return.md:80` ("The warmth is still there, but it comes slower and lower than it did"); arrest in `s01-davils-arrest/ev-01-davils-arrest.md:5` |
| 9 | L25 | "**Relationships.** Davil is the cell leader of the Doom Raiders (Waterdeep Zhentarim), the faction contact for Zhentarim-aligned PCs, a permanent resident at the Yawning Portal (second floor business room, third floor suite), a colleague of Istrid, Tashlyn, Ziraj, and the traitor Skeemo Weirdbottle, and the unknowing target of Nihiloor's intellect devourer, with Meloon watching him and waiting for a clean opportunity to kill him without witnesses." | Day-one except two clauses: "the traitor Skeemo Weirdbottle" is GM truth (a Secret, not public); "the unknowing target of Nihiloor's intellect devourer" is not in the sources as written (D6) | "traitor": `06-doom-raiders.md:120`, `07-doom-raiders.md:11`. "Meloon ... without witnesses": `sources/adventure-wdh.json:1548` |
| 10 | L29 | "A sun elf known as the Master of Opportunities and Negotiations, who conducts business from a curtained room at the Yawning Portal with effortless charm and a permanent suite upstairs — always available, always interested, and always asking one more question than the conversation requires." | Day-one. **44 words** (brief limit 21). The "curtained room" clause is D1 | `ev-01-first-meeting.md:164`; `sources/adventure-wdh.json:31924` |

### C2. Quest-time clauses in the voice profile (`.claude/skills/character-voices/voices/doom-raiders.md`, "### Davil Starsong", lines 7-22)

Ruling 16: a quest-time clause in a profile gets the same day-one restatement as ruling 3, and the profile is changed to match. Each line is listed here. Lines not listed are day-one.

- Line 10 (Sound): "A light, musical tenor with a sun-elf lilt he makes the most of. He's never loud. After his arrest the warmth stays, but it comes slower and lower." — **quest-time** clause: "After his arrest the warmth stays, but it comes slower and lower." Lives at `s02-davils-return/ev-01-davils-return.md:80` ("it comes slower and lower than it did"). Day-one restatement needed.
- Line 14 (Personality in speech): "Grief (Skeemo, the arrest) never gets words. He changes the subject to music, or plays instead." — **quest-time** clause: "(Skeemo, the arrest)". The grief is about the betrayal learned in `s02-davils-return/ev-01-davils-return.md:15`. The music sentence is day-one.
- Line 22 (Sample line, "*After the arrest:*"): "They kept me a while. It was instructive. Sit, and tell me what I missed." — **quest-time** (labelled after the arrest). Lives at `s01-davils-arrest/ev-01-davils-arrest.md:5` and `s02-davils-return/ev-01-davils-return.md:5`.
- Lines 8, 11-13, 15-17, 19-21 (tagline, sentence shape, word choice, swearing, quirks, signature phrases, never, greeting, business, under pressure): day-one.

Ruling 16 note for the drafter: the profile's wording "After his arrest" is in lines 10, 14 and 22. Each needs a day-one restatement and a matching change in the skill file. The drafter makes that change under ruling 16.

### C3. Quest-time context on the Organization page that feeds Davil's page

These are not on Davil's page, but the drafter must not use them as day-one lore:
- `campaign/setting/organizations/06-doom-raiders.md:105` (Grand Game Agenda): "Davil's cell sees an enormous opportunity in the half-million dragons" — a day-one stance. The seat on the Council depends on the Vault, and the 10% split is a Dread Lord rank term (`campaign/guides/factions/07-doom-raiders.md:33` and `:60`, quest-time).

---

## D. Conflicts

**D1. Where Davil does his business: taproom or curtained room**
- Adventure: "He keeps a room at the Yawning Portal and does all his business in the establishment's taproom." — `sources/adventure-wdh.json:31924`
- Adventure, the recruitment entry (page 40): "leads interested parties to a table in the center of the Yawning Portal's taproom, where her boss waits with drink in hand." — `sources/adventure-wdh.json:4004`. This puts Davil at a table in the taproom.
- Organization page GM Notes: "Davil keeps a room upstairs and does all his business in the taproom, which he has decided is safer than a private office and more honest than a warehouse." — `campaign/setting/organizations/06-doom-raiders.md:113`
- First-meeting event: "Davil's business room is at the far end of the second-floor landing behind a heavy green curtain." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:164`
- History: "Davil holds court in a curtained room at the Yawning Portal, and Skeemo runs Weirdbottle's Concoctions in the Trades Ward." — `campaign/setting/history/04-the-founding-of-chains.md:57`
- Page: "He conducts business from a curtained room on the Yawning Portal's second floor, with a permanent suite on the third." — `01-davil-starsong.md:21`
- Organization page Draft Notes, line 174. The sentence reads "**Conflicts:** Davil's room." and continues "The old page and `adventure-wdh.json` line 31924 have him doing all his business in the taproom." Its next sentence reads "His Notable Figures page has a curtained second-floor room", and its last sentence reads "The GM Notes keep the taproom wording." (`06-doom-raiders.md:174`).
- Higher rank: the campaign outranks the adventure (brief ruling 12). Campaign files split: the first-meeting event, the history page and the Notable Figures page say curtained room; the organization GM Notes say taproom. Left to the orchestrator.
- Secondary, same file: the GM Notes say he "carries it on his back in every meeting" (`06-doom-raiders.md:113`), but the first-meeting event says "His lute leans against the wall" (`ev-01-first-meeting.md:164`). Both are campaign files.

**D2. How long Davil has been in Waterdeep (arrival)**
- Organization page: "arrived in Waterdeep in 1489 DR" — `campaign/setting/organizations/06-doom-raiders.md:25`
- Adventure: "came to Waterdeep three years ago" — `sources/adventure-wdh.json:31916`
- Appendix B, Davil's own speech in the first meeting: "Me and my colleagues arrived in Waterdeep about four years ago." — `sources/Appendix_B_-_Player_Factions.md:636`
- Wiki: "In the year [[1489 DR]], they were directed to establish a Zhent foothold in Waterdeep." — wiki line 74 (5e)
- Organization page design tag at line 25: "Design tag: the published adventure says only \"three years ago\", and the campaign fixes the year and makes the cell the first in the city, with Manshoon's cell arriving after it (**Manshoon**)."
- Higher rank: the campaign (1489 DR, which is three years before 1492 DR). The Appendix B line is the older Alexandrian figure. Left to the drafter to use 1489 DR.

**D3. Stat block name (Swashbuckler)**
- Page: "Stat block: **Swashbuckler (with modifications)**." — `01-davil-starsong.md:5`
- Adventure: no creature block for Davil (see B). The adventure's entries for Davil (lines 31919 to 31926) and the Zhentarim faction (lines 1438 to 1459) name none.
- Wiki: "| class5e        = {{Class table|edition=5e|[[Bard]]|12}}" — wiki line 59. Bard, not Swashbuckler.
- The 2024 rule: "No 2024 Swashbuckler; CR 8 if heavily modified" (`docs/plans/bregan-daerthe-mechanics-reference.md:410`). CLAUDE.md requires 2024 rules and terminology.
- Higher rank: none of the sources names a creature for Davil. The Tashlyn page uses the same retired name (`docs/plans/setting-compendium-research-notes/pass5/doom-raiders.md:170`). Left to the orchestrator.

**D4. Class (bard)**
- Page: "*Sun elf bard, neutral, he/him*" (`01-davil-starsong.md:5`)
- Wiki: "making him a fine [[bard]]" (wiki line 65, 5e) and "class5e Bard 12" (wiki line 59, `refs5e` WDH-198-199).
- Adventure: "Like many sun elves, Davil has an affinity for magic and is gifted with the kind of patience that comes with a long life span." (`sources/adventure-wdh.json:31924`) — no class named.
- Higher rank: the adventure names no class; the wiki's class is cited to a page that does not state it. Flag as `[research]` for the drafter.

**D5. When Davil learns Skeemo is a traitor (quest-time against the day-one Emotions line)**
- Factions Guide: "The Doom Raiders do not tell the party until Mission 4 forces the truth out. **Skeemo Weirdbottle has been a traitor from the start.**" — `campaign/guides/factions/07-doom-raiders.md:11`
- Factions Guide, the same paragraph: "Davil has suspected something for months. Tashlyn confirmed it during his arrest." — `07-doom-raiders.md:11`
- History 04: "> - Skeemo Weirdbottle is a traitor to the Doom Raiders and has been from the start. Davil has suspected it for months, and Tashlyn confirms it during his arrest." — `campaign/setting/history/04-the-founding-of-chains.md:96`
- Event: "Davil had no idea that Skeemo was a traitor until she told him, and nobody else gets to him first." — `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:15`. In that event Tashlyn tells him "on the way" from the Castle Waterdeep gate, after release.
- Conflict: `07-doom-raiders.md:11` and `history/04-the-founding-of-chains.md:96` say Tashlyn confirms it during the arrest; `s02-davils-return/ev-01-davils-return.md:15` says she tells him on the walk after release, and that he "had no idea" until then. "Suspected" (the Factions Guide) is compatible with `s02:15` only if suspicion is not knowledge. Higher rank: the quest journal (`s02-davils-return/ev-01-davils-return.md`) for what Davil knows and when. The Secret stays GM truth.
- Effect on the page: the Emotions clause "private grief over Skeemo's betrayal" can only be true after the event; it is quest-time (C1 row 4).

**D6. The intellect devourer that watches Davil**
- Page: "the unknowing target of Nihiloor's intellect devourer, with Meloon watching him and waiting for a clean opportunity to kill him without witnesses." — `01-davil-starsong.md:25`
- Adventure: "An intellect devourer in league with {@creature Xanathar|WDH} ate Meloon's brain several months ago. Now under the monster's control, Meloon actively discourages adventurers from exploring Undermountain and urges them to focus on conflicts in the city instead. He also hunts down and kills Zhentarim operatives for his secret beholder master. He has his eye on {@creature Davil Starsong|WDH} (see {@adventure appendix B|WDH|12}) but won't kill the elf in plain view of witnesses." — `sources/adventure-wdh.json:1548` (page 20)
- Adventure, Nihiloor's devourer: "The tentacled creature is {@creature Nihiloor|WDH} (see {@adventure appendix B|WDH|12}), a {@creature mind flayer} that is caressing an {@creature intellect devourer}." — `sources/adventure-wdh.json:2814` (no link to Davil)
- Organization page Draft Notes, line 183: "**Conflicts:** Meloon watching Davil. `notable-figures/doom-raiders/01-davil-starsong.md` line 25 and `adventure-wdh.json` line 1548 have Meloon watching Davil for Xanathar." — `campaign/setting/organizations/06-doom-raiders.md:183`
- Higher rank: the adventure. The "Nihiloor" link and "unknowing" are not in any source. The drafter should use Meloon and Xanathar, or flag `[research]`. `campaign/setting/history/08-the-players-arrive.md:138` (cited by the Organization page for Meloon's timing) was not read in this pass.
- "waiting for a clean opportunity to kill him without witnesses" is a paraphrase of "won't kill the elf in plain view of witnesses" (`sources/adventure-wdh.json:1548`). It is not an exact quote.

**D7. Whether the Zhentarim is one organization (wiki) or two (campaign)**
- Campaign: "Manshoon's splinter cell and Davil Starsong's Doom Raiders are entirely separate organizations." — `campaign/setting/villains/manshoon.md:19`
- Campaign, the Organization page's Draft Notes on the wiki: "**Conflicts:** Origin of the name. The wiki's *Zhentarim* page makes the whole organization Manshoon's company (`wiki.txt` line 210, *Cloak & Dagger*), and the campaign makes the Doom Raiders the legitimate Black Network and Manshoon's cell a splinter" — `campaign/setting/organizations/06-doom-raiders.md:182` (the wiki's line 210 is not read in this pass)
- Higher rank: the campaign. The Two Zhentarims rule governs (`manshoon.md:19`).

**D8. Overview and the word limit**
- Page Overview: 44 words (line 29). Brief ruling: "21 words or fewer each". This is a length conflict, not a source conflict.

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/setting/organizations/06-doom-raiders.md:113`: "does all his business in the taproom" (see D1). Stale against the first-meeting event (`ev-01-first-meeting.md:164`).
- `campaign/guides/factions/07-doom-raiders.md:11`: "Tashlyn confirmed it during his arrest." Conflicts with `s02-davils-return/ev-01-davils-return.md:15` (D5).
- `campaign/setting/history/04-the-founding-of-chains.md:96`: "Tashlyn confirms it during his arrest." Same as D5.
- `sources/adventure-wdh.json:31916`: "three years ago" (the adventure's relative date; see D2).
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/design-notes.md:11`: "Yagra doesn't fight, because her Notable Figures block is a \"Thug\", which does not exist in the 2024 Monster Manual." (Yagra, not Davil; cross-reference only.)
- `docs/plans/setting-compendium-research-notes/pass5/doom-raiders.md:146`: copies Davil's Summary stat block without the challenge rating.

**E2. Routed quest references (quest-time; the day-one page must not restate them)**

Davil's own quest appearances, by file:
- `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:1` (title "# Davil's Arrest") and `:5` ("Davil Starsong is taken to Castle Waterdeep on Ches 26"); `:16` ("The case against Davil is association and nothing else."); `:29` ("it called him \"Master of Opportunities and Negotiations\"").
- `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:1` (title "# Davil's Return"), `:5` ("when the Lords' clerks hear Davil Starsong at Castle Waterdeep and release him"), `:15` (Tashlyn walks him back; "Davil had no idea that Skeemo was a traitor until she told him"), `:27` ("Davil was fond of Skeemo and will never say so."), `:43` (the curtained room in the release terms), `:78` (tag), `:80` (warmth "slower and lower").
- `campaign/guides/factions/07-doom-raiders.md:29` (Gralhund Villa hook: "Davil is arrested in the Watch's post-Gralhund crackdown on all Zhentarim operations."), `:33` (Vault of Dragons hook: "Davil proposes a 10% split"), `:60` (Dread Lord rank: "Davil proposes the character for a seat on the reforming Zhentarim Council"), `:73` ("**Two days after Gralhund Villa, the City Watch arrests Davil and holds him at Castle Waterdeep pending questioning about the Zhentarim's role in the street violence.**").
- `campaign/gazetteer/waterdeep/castle-ward.md:10` ("Gralhund Villa** carries a Missive from Castle Ward in the family library and leaves Davil Starsong, and possibly Yalah, in the custody wing at Castle Waterdeep.") and `:58` ("Hook: a custody wing built for thirty prisoners holds sixty-one, and Davil Starsong is held there after **Gralhund Villa**.").
- `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md`, `m04-silencing-skeemo/` (4 files), `m05-the-yellowspire-job/` (ev-02 debrief and overview), `campaign/quests/act-ii/gralhund-villa/` and `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md`: Davil appears in these events. Not read line by line in this pass.
- Harpers: `sources/Appendix_C_-_Player_Faction_Missions.md:104` ("Maxeene's description matches Davil Starsong and Yagra Stonefist precisely.") and `:124` ("The intelligence about Davil Starsong and Yagra Stonefist is one of three clue paths connecting the Doom Raiders to the Grand Game's wider network."). Routed; Harpers mission, quest-time.
- Adventure, quest-time: `sources/adventure-wdh.json:4028` ("After the characters complete two missions for Davil, he is arrested by the City Watch and held in Castle Waterdeep while he waits to be questioned by the Lords of Waterdeep ..."), `:4038` ("Weeks after his arrest, Davil is released from custody once the Lords of Waterdeep are satisfied that neither he nor his associates are responsible for the recent violence."), `:6087` ("After {@creature Davil Starsong|WDH} is taken in for questioning, {@creature Istrid Horn|WDH} (see {@adventure appendix B|WDH|12}) sends a message to the characters by way of a {@creature flying snake}."), `:14893` ("{@creature Davil Starsong|WDH} (see {@adventure appendix B|WDH|12}) asks the characters for a donation of 5,000 gp to keep his branch of the Zhentarim afloat in Waterdeep.").
- Alexandrian, quest-time: `sources/Appendix_B_-_Player_Factions.md:530` ("He is arrested by the City Watch after the characters' second mission and held for questioning; subsequent missions arrive from his colleague Tashlyn Yafeera.") and `:662` ("- **Assist Davil after his arrest (+1).**").
- Alexandrian Appendix D, quest-time: `sources/Appendix_D_-_Running_the_Tavern.md:1443` ("Has heard something concerning about Davil Starsong's arrest timeline") and `:1460` ("Davil is being released from custody — or will be released, or was released yesterday, depending on where the campaign is.").
- `sources/Appendix_D_-_Running_the_Tavern.md:182` ("**Faction Note:** Zhentarim (Doom Raiders) plant, reporting to Davil Starsong.") — the Senna Vael placement; routed to her page.

**E3. Faction-label checks**
- Affiliation "Zhentarim (Doom Raiders)" matches the organization H1 (`06-doom-raiders.md:1`) and the Factions Guide (`07-doom-raiders.md:3`: "Game mechanics for running the Doom Raiders (Davil Starsong's Zhentarim cell) as a player faction.").
- Not Manshoon's cell: `06-doom-raiders.md:9` (quoted in B).

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in Draft Notes.

**F1. Birth year, age, parents, siblings, children.** No source gives any of these. Wiki infobox fields `age` (line 17), `dob` (line 21), `parents` (line 29), `siblings` (line 31) and `children` (line 32) are blank. The only age terms are "a long life span" (`sources/adventure-wdh.json:31924`) and "the patience of someone who might live ten times longer than even his most fortunate friends" (wiki line 65). Consistent with the sources: he is older than his companions in patience; do not give a birth year.

**F2. Origin before the Doom Raiders.** No source says where Davil was born or raised, what he did before the lich lairs, or how the five met. The wiki's "sun elf agent of the Zhentarim" (line 62) and "Davil was once an adventurer" (line 74) are the only lines. The five are "unscrupulous adventurers who liked to plunder lich lairs" (`sources/adventure-wdh.json:31916`). Gap: origin, first companion, how the five met.

**F3. How Davil came to lead.** No source says why Davil leads the five. The adventure names him first (`sources/adventure-wdh.json:1447`); the wiki infobox names him leader (`sources/research/pass5-bundles/doom-raiders/wiki.txt:9`). The Organization page says the leadership is settled by the wiki and the adventure (`06-doom-raiders.md:63`). The reason is unsourced (`[design]` if the Background gives one).

**F4. Who sent the five to Waterdeep.** No source names the sender. The campaign says so: "no source names who sent them" (`campaign/setting/organizations/06-doom-raiders.md:25`) and "No source names a sender" (`campaign/setting/history/04-the-founding-of-chains.md:146`). Do not name one.

**F5. Carriage with a half-orc bodyguard in the Dock Ward (1492 DR).** Wiki line 76: "In [[1492 DR]],{{WDH-time}} Davil was seen riding a carriage with a [[half-orc]] bodyguard, in the [[Dock Ward of Waterdeep|Dock Ward]] of Waterdeep." (cites WDH p.37). The JSON carriage hits do not include Davil. Not verified in the adventure. Do not use without a `[research]` tag.

**F6. Relationship with Skeemo before the betrayal.** Only the Secret (`06-doom-raiders.md:120`: "Davil was fond of him and does not say so aloud.") and the adventure's Mission 3 brief ("The gnome who runs it is a friend of ours named Skeemo." `sources/adventure-wdh.json:4059`). Consistent with the sources: a long-standing friendship that Davil does not discuss. The Secret is GM-only; the Background may say "fond" only as a GM line, not in public Persona.

**F7. Personal goals beyond the cell.** The Motivations line (`01-davil-starsong.md:15`) and the moral ledger (`06-doom-raiders.md:40`) are the only goals. The Factions Guide gives his ideal outcome: "Davil's ideal outcome: the vault gold funds the Zhentarim Council bid, Manshoon's cell is dismantled before it can contest the vault, Skeemo's betrayal is cleaned up internally without Watch involvement, and Ziraj is alive. He keeps the moral ledger as balanced as his business allows." (`campaign/guides/factions/07-doom-raiders.md:23`). This is a faction goal and a Vault-of-Dragons plan; it must not become a Background goal. Brief ruling 17 forbids a new plot hook that needs a quest event. `[design]` material must not contradict: the lute, the trophies, the room, the Council seat, the peace with Xanathar's Guild, the Skeemo friendship.

**F8. Music.** The Emotions line says he expresses sadness "through music rather than words" (`01-davil-starsong.md:13`). The voice profile says "He changes the subject to music, or plays instead." (`doom-raiders.md:14`). The adventure says the elven lute is his spellcasting focus (`sources/adventure-wdh.json:31924`). No source says where he learned music. `[design]` if used.

**F9. Why he keeps the peace with Xanathar's Guild.** The adventure says "Davil and his colleagues want to end the violence and restore the peace." (`sources/adventure-wdh.json:4016`). No source gives a reason for negotiation beyond the "helping people" framing. `[design]` if used.

**F10. The bracelet's trophies.** Which monsters, and which were his own kills, is unsourced. `ev-01-first-meeting.md:164` says only "small trophies from monsters the Doom Raiders have killed". Do not name a monster.

**F11. Davil and Durnan.** Only "Two old adventurers understand each other. Davil is a retired adventurer like Durnan, and neither asks the other about the past." (`ev-01-first-meeting.md:174`) and "Davil pays. Davil is a permanent resident who rents this room and the suite above it" (`:170`). Durnan's own page is outside this pass.

**F12. Family, home, faith.** No family, no home other than Waterdeep (wiki line 11), and no faith in any source for Davil (A7). Do not invent a family member without `[design]`. A nameless relative or place is allowed by ruling 17.

---

## G. Source facts that hint at the figure's inner life (for the Background; do not contradict)

- "Like many sun elves, Davil has an affinity for magic and is gifted with the kind of patience that comes with a long life span." — `sources/adventure-wdh.json:31924`. (Patience; a long life.)
- "Unlike most, he's not the least bit pretentious or aloof." — `sources/adventure-wdh.json:31924`.
- "He always traded with grace and aplomb even when drunk." — wiki line 65 (5e).
- "Davil also suspects that someone inside his own cell is leaking to the other side, and he tells nobody." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:25`. (A private suspicion; he does not say it aloud.)
- "The reason is his suspicion of a leak inside his own cell." — `ev-01-first-meeting.md:204` (the sentence closes a paragraph on a DC 14 Insight check; the paragraph is quest-time for the check, day-one for the suspicion).
- "Davil was fond of Skeemo and will never say so." — `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:27`. (Fondness he keeps private; the fondness is day-one per `06-doom-raiders.md:120`.)
- "Davil is a retired adventurer like Durnan, and neither asks the other about the past." — `ev-01-first-meeting.md:174`. (He does not ask about the past.)
- "Yagra came along later, once she'd given us good reason to keep her." — `ev-01-first-meeting.md:236`. (He chooses his people by proof.)
- "The profit pays for people who need help. You'd be surprised how many do, yes?" — `ev-01-first-meeting.md:236`. (He frames the trade as help.)
- "They help people in need." — `sources/adventure-wdh.json:4015`.
- "he was fond of Skeemo in a way he does not say aloud" — `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:21` (the page's own line).
- "He withholds explanation and lets things sit, showing interest without revealing why" — `01-davil-starsong.md:21` (own page). Voice: "He withholds explanations and leaves questions unanswered without apology." — `doom-raiders.md:14`.
- Voice, the grief: "Grief (Skeemo, the arrest) never gets words. He changes the subject to music, or plays instead." — `doom-raiders.md:14`. (Grief he does not voice; the parenthesis is quest-time, see C2.)
- Voice, friends: "His fondness for capable people is real and shows in specific praise." — `doom-raiders.md:14` (day-one).
- Voice, asked why: "He answers \"why\" with a smile and another question." — `doom-raiders.md:15`.
- Voice, quirk: "He turns a small trophy on his charm bracelet when he's weighing something." — `doom-raiders.md:15`.
- Adventure, the peace he wants: "Davil and his colleagues want to end the violence and restore the peace." — `sources/adventure-wdh.json:4016`.
- Organization, the moral ledger: "He keeps the moral ledger as balanced as his business allows." — `campaign/setting/organizations/06-doom-raiders.md:40`. (A personal code he keeps.)
- Factions Guide, his goal on the Skeemo fallout: "Skeemo's betrayal is cleaned up internally without Watch involvement" — `campaign/guides/factions/07-doom-raiders.md:23`. (Depends on the Skeemo discovery; quest-time-adjacent.)
- Factions Guide, his suspicion: "Davil has suspected something for months." — `07-doom-raiders.md:11`.
- Adventure, Ziraj: "If Ziraj sets out to kill someone, it's because one of his friends (Davil, Istrid, Skeemo, or Tashlyn) asked him to." — `sources/adventure-wdh.json:31965`. (Davil is one of the friends whose word counts.)
- Organization page: "Anyone who betrays or harms Istrid Horn finds her former adventuring companions using every resource they have to ruin them." — `06-doom-raiders.md:37`. (Loyalty to the five.)
- Meloon's watch on Davil (a threat, not inner life): `sources/adventure-wdh.json:1548`.

---

## Cross-references (the Davil topic in other files)

The Grep for `Davil|Starsong` across `campaign/` returns 124 files. The lines that matter for the Background are quoted above. The other files are listed here.

- `campaign/setting/notable-figures/doom-raiders/02-yagra-stonefist.md:15` and `:25` (Yagra's Motivations and Relationships name Davil).
- `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:25` ("and a colleague Davil was fond of, which Davil does not say aloud.")
- `campaign/setting/notable-figures/doom-raiders/05-tashlyn-yafeera.md:25` ("Davil's replacement as faction contact after his arrest") — quest-time on Tashlyn's page; do not copy to Davil's.
- `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md:25` ("a direct report to Davil Starsong").
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:42` ("the Watch arrests Davil after **Gralhund Villa**") and `:75` (the names list).
- `campaign/setting/history/04-the-founding-of-chains.md:57` (curtained room) and `:96` (the traitor line; see D5).
- `campaign/setting/villains/manshoon.md:19` (the Two Zhentarims rule).
- `campaign/gazetteer/waterdeep/castle-ward.md:45` ("Davil Starsong keeps a room") and `:10`, `:58` (quest-time; routed).
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md` and `02-urstul-floxin.md` (Davil named; not read in this pass).
- `campaign/setting/governance-and-guilds/code-legal-and-magisters.md`, `city-watch.md` (Tashlyn's City Guard post; not Davil).
- `campaign/gazetteer/waterdeep/dock-ward.md` (Davil named; not read in this pass).
- `campaign/guides/gm-guide/grand-game-in-play.md`, `structural-rules.md` (Doom Raiders; not read in this pass).
- `campaign/quests/faction-events/doom-raiders/` (all folders; quest-time).

---

## Not found

- Searched for: birth year, age, parents, siblings, spouse, children, home town other than Waterdeep, origin, the five's first meeting, Davil's faith: `campaign/` (Grep for `Davil|Starsong`; the file list is in the cross-references), `sources/adventure-wdh.json` (Grep for `Davil`; the entries at lines 31916 to 31926 and 4004 to 4038 read in full), `sources/Appendix_B_-_Player_Factions.md` (Grep for `Davil`), `sources/research/` (Grep for `Davil`; the pass5 doom-raiders wiki bundle).
- Creature block (stat name, CR, AC, HP) for Davil: `sources/adventure-wdh.json:31916` to `:31966` and `:1438` to `:1459`; `sources/Appendix_B_-_Player_Factions.md:502` to `:680`. Not present. `docs/plans/doom-raiders-mechanics-reference.md` (Grep for `Davil`): only `:224` ("Deployment packages (Davil sets operational limits; use one package per operation):"), no stat line.
- Class (bard): not in the adventure entry (`:31919` to `:31926`). Only the wiki (line 59).
- Carriage with a half-orc bodyguard (1492 DR): the JSON Grep for `carriage` has no Davil hit.
- Davil's relationship with Durnan beyond the event design note: none in the adventure.
- Davil's music, where he learned it, any family: none.
- Davil's personal reasons for the peace with Xanathar's Guild: none beyond "helping people in need".
- Who sent the five to Waterdeep: none (`campaign/setting/history/04-the-founding-of-chains.md:146` says "No source names a sender").
- `campaign/setting/history/08-the-players-arrive.md:138` (cited by the Organization page for Meloon's timing): not read in this pass.
- Alexandrian PDF for Davil: `sources/3. Player Character Factions.pdf` PDF pp.2-3 (printed pp.24-25) read; the Zhentarim sentence is "The non-Manshoonian **Zhentarim** will see an enormous opportunity in the gold ..." (printed p.25). No Davil text. `sources/5. Faction Outposts.pdf`, `sources/11. Lair  Xanathar’s Lair.pdf` and `sources/17. Outpost and Lair Revelation Lists.pdf` not read for Davil in this pass.
- `sources/SOURCE_GUIDE.md`: not grepped in this pass for Davil.

## Not readable

- `sources/Other remix files/Davil and the Doom Raider Zhents + Elf Killer mission and more.docx`: not opened. The Organization page's Draft Notes (`06-doom-raiders.md:193`) say the research tools could not open it. The brief's list of `Other remix files` names it for the Doom Raiders and Davil. It should be extracted and checked for Davil's Background before the page is drafted.
- `sources/3. Player Character Factions.pdf`: read as images, not `pdftotext`. The Zhentarim sentence is a transcription.
