# Pass 6 research notes: Yagra Stonefist

Page: `campaign/setting/notable-figures/doom-raiders/02-yagra-stonefist.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Yagra is a Trollskull staff candidate, Davil's bodyguard and the cell's street contact. The brief's major-NPC list includes "the Trollskull staff" and "lieutenants", so the full Personality and Connections are used here. The orchestrator may rule her minor instead.
Organization page: `campaign/setting/organizations/06-doom-raiders.md` (H1: "# The Zhentarim (Doom Raiders)")
Factions Guide: `campaign/guides/factions/07-doom-raiders.md`
Villains page: none.
Voice profile: `.claude/skills/character-voices/voices/doom-raiders.md` (### Yagra Stonefist, lines 26-40)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field is given where the entry has one (the Yagra entry is `"page": 20` at line 1565; the Tavern Brawl entry is `"page": 21` at line 1606).
- Appendix B, C and D: `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md`, `sources/Appendix_D_-_Running_the_Tavern.md`. Read with the Read tool.
- Alexandrian PDF: no Yagra text was found in the PDF read for the Davil notes (`sources/3. Player Character Factions.pdf`, pp.2-3). The other PDFs were not read for Yagra.
- Wiki: the scratchpad extract `wiki-doom-raiders/02-yagra-stonefist.txt` is the Yagra page. It is quoted as "wiki line N" (that file's lines). Edition tags come from the infobox `refs5e` and `ref` names. The wiki prints no edition on most sentences.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The stat block "Thug (with modifications)" is not a 2024 name, and the campaign's other files give her three different labels.** The adventure does say she is "a half-orc thug" (`sources/adventure-wdh.json:1570`). The campaign's own mechanics reference says "Thug and Veteran do not exist in XMM" (`docs/plans/doom-raiders-mechanics-reference.md:13`). Two tavern files give her "Tough" (`campaign/guides/trollskull-manor/08-notable-patrons.md:114` and `sources/Appendix_D_-_Running_the_Tavern.md:1450`). The Rank 10 event gives her a "Warrior Veteran" block with two changes (`r10-viper/ev-01-viper.md:128`). See D1 and D2.
2. **The surname is "Stonefist" in the campaign and in most of the adventure, but "Strongfist" once in the adventure.** The adventure's Tavern Brawl (page 21) reads "Their foe, Yagra Strongfist" (`sources/adventure-wdh.json:1618`). The wiki's note calls that one instance an error (wiki line 62). See D3.
3. **The slaver-ship origin is day-one; the 2 AM run is quest-time.** The Persona and Morale lines take their traits from the sources below. The ship story is a backstory fact that the first-meeting event and the tavern appendix both tell (`ev-01-first-meeting.md:140`; `Appendix_D_-_Running_the_Tavern.md:1462`). The "2 AM ... clearly having run" clause comes from the Ziraj event (`m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:5` and `:36`). See C1.
4. **The Relationships line names a Ziraj rescue.** "the person who will run across the city at night to save Ziraj the Hunter" is quest-time (Mission 6). See C1 row 10.
5. **The Overview runs 30 words** (page line 29). The brief's limit is 21. The Overview also says she "has never been seen to lose", which sits against a Tavern Brawl variant in Appendix B (`sources/Appendix_B_-_Player_Factions.md:598`). See D4.
6. **The "trail marks" that Yagra learned from Ziraj are campaign-only.** No adventure or Alexandrian source says Ziraj taught her. The claim is on the Organization page (`06-doom-raiders.md:37`) and the Ziraj page (`06-ziraj-the-hunter.md:23`). See F3.

---

## A. Background facts by theme

### A1. Origin, family, early life

**Wiki, lead (edition: 5e, `WDH5e-p20`)**
> "'''Yagra Stonefist'''<ref group="note">Page 21 of ''[[Waterdeep: Dragon Heist]]'' refers to Yagra's last name as "Strongfist". Since her all other mentions from that source call her by the last name "Stonefist", we assume that this one instance was in error.</ref> ({{Pronounce|YAG|raw|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a [[Zhentarim]] mercenary at the [[Yawning Portal]] around [[1492 DR]].<ref name="WDH5e-p20" />{{Waterdeep-time}}"
> — wiki line 62 (edition: 5e; `WDH5e-p20`)

**Wiki, infobox home, sex and race (5e)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]"
> — wiki line 11
> "| sex            = Female"
> — wiki line 13
> "| race           = [[Half-orc]]"
> — wiki line 14

**Wiki, infobox fields left blank (5e)**
> "| age            = "
> — wiki line 17
> "| dob            = "
> — wiki line 21
> "| parents        = "
> — wiki line 29
> "| siblings       = "
> — wiki line 31

**Adventure, Yagra's entry (page 20; the race, the sex, the job)**
> "{@i N female half-orc thug-for-hire}"
> — `sources/adventure-wdh.json:1568` (entry "Yagra Stonefist", `"page": 20` at line 1565)

**Adventure, Yagra's entry (page 20; the job, the boredom and the arm-wrestling)**
> "Yagra is a Black Network mercenary who gets paid to protect a Zhent negotiator named {@creature Davil Starsong|WDH} (see {@adventure appendix B|WDH|12} for more information on him). Yagra finds the job boring and likes to pass the time by challenging adventurers to arm wrestle. (Resolve such contests using contested Strength checks.) If the characters express their opposition to the Xanathar Guild, Yagra might urge them to speak to Davil about joining forces with the Zhentarim to destroy the beholder crime lord."
> — `sources/adventure-wdh.json:1569`

**Adventure, Yagra's entry (page 20; the Thug block)**
> "Yagra is a half-orc thug. When reduced to 0 hit points, she drops to 1 hit point instead (but can't do this again until she finishes a long rest). She has darkvision out to a range of 60 feet. She speaks Common and Orc."
> — `sources/adventure-wdh.json:1570`

**Wiki, Yagra's Activities (5e, `WDH5e-p20`)**
> "Yagra worked for the Zhentarim to protect [[Davil Starsong]]. In her spare time, she enjoyed wrestling with adventurers at the inn."
> — wiki line 65 (edition: 5e)

**Wiki, Yagra's Personality (5e, `WDH5e-p20`)**
> "Yagra was bored by her work and enjoyed wrestling."
> — wiki line 77 (edition: 5e)

No source gives Yagra's birth year, age, parents, siblings, a home town other than Waterdeep, or where she came from. The wiki's infobox fields `age` (line 17), `dob` (line 21), `parents` (line 29) and `siblings` (line 31) are blank.

### A2. The slaver ship and the Doom Raiders

**First-meeting dialogue (campaign quest file; the backstory is day-one, the scene is quest-time)**
> "> > \"I was on a slaver ship, chained to a bench. Davil's people took the ship, and he asked me what I wanted to do next. I said fight, so here I am. It's a good job.\""
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:140` (the Q&A "Why are you with the Doom Raiders?"; quest-time for the scene, and the backstory is what the Background needs)

**Appendix D, the patron profile of the same story (tavern event; the backstory is day-one)**
> "4. Tells a story — not asked, just tells it — about the slaver ship she was on before the Doom Raiders found her. The story is specific and not dramatic in the way a story about slavery usually is. She tells it the way people tell old weather reports. She does not want anything from the party for telling it. She just wanted it said in a room she trusts."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1462` (the patron entry "Yagra Stonefist", heading at line 1449)

**Campaign, the Trollskull patron entry (tavern guide; the same story)**
> "- Tells a story about the slaver ship she was on before the Doom Raiders found her. Tells it like an old weather report. Wants nothing for telling it. Just wanted it said in a room she trusts."
> — `campaign/guides/trollskull-manor/08-notable-patrons.md:120`

**Campaign, first-meeting, the join**
> "Yagra came along later, once she'd given us good reason to keep her."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:236` (Davil's line; the date of her joining is not given)

### A3. The job, the Doom Raiders and the loyalty

**Adventure, Zhentarim support (page 17; the Doom Raiders' creed; the leader names)**
> "The Doom Raiders (described in appendix B) consider themselves the true Zhentarim of Waterdeep. The group's leaders are {@creature Davil Starsong|WDH} (Master of Opportunities and Negotiations), {@creature Istrid Horn|WDH} (Master of Trade and Coin), {@creature Skeemo Weirdbottle|WDH} (Master of Magic), {@creature Tashlyn Yafeera|WDH} (Master of Arms and Mercenaries), and {@creature Ziraj the Hunter|WDH} (Master of Assassination)."
> — `sources/adventure-wdh.json:1447` (Yagra is not among the named leaders)

**Campaign, Organization page, the Street Contact (day-one post)**
> "**Street Contact:** Yagra Stonefist — the half-orc Doom Raider who works the bar at the Yawning Portal. She is also Davil's bodyguard."
> — `campaign/setting/organizations/06-doom-raiders.md:53`

**Campaign, Organization page, the Key Members line (day-one)**
> "- **Yagra Stonefist** — Street contact and Davil's bodyguard; present at the Yawning Portal. See the **Yagra Stonefist** page in Notable Figures."
> — `campaign/setting/organizations/06-doom-raiders.md:98`

**Campaign, Organization page, the Contacts line in the Summary (day-one)**
> "- **Contacts:** **Davil Starsong** (primary, Yawning Portal); **Tashlyn Yafeera** (secondary); **Yagra Stonefist** (street contact, Yawning Portal bar)"
> — `campaign/setting/organizations/06-doom-raiders.md:8`

**Campaign, Organization page, the loyalty line (day-one trait; the 2 AM and the trail marks are quest-derived or unsourced; see C1 and F3)**
> "The loyalty is personal as well as institutional. Yagra will reach a threatened friend's door at 2 AM in full armor, and Ziraj taught her the trail marks he leaves when he is wounded (**Yagra Stonefist**; **Ziraj the Hunter**)."
> — `campaign/setting/organizations/06-doom-raiders.md:37`

**Campaign, Factions Guide, the Viper rank (day-one role)**
> "Yagra Stonefist or another Doom Raider serves as muscle (use **veteran** stat block) on one operation per quest."
> — `campaign/guides/factions/07-doom-raiders.md:58`

**Campaign, Factions Guide, the Ardragon rank (day-one role)**
> "If Ziraj dies, Yagra Stonefist offers a capture-only substitute in its place."
> — `campaign/guides/factions/07-doom-raiders.md:59`

**Trollskull guide, Yagra's patron entry (day-one)**
> "**Yagra Stonefist** *(Doom Raiders, N female half-orc, Tough; see **The Zhentarim (Doom Raiders)** organization page)*"
> — `campaign/guides/trollskull-manor/08-notable-patrons.md:114` (see D2 on "Tough")

### A4. Appearance and the set-piece details

**Appendix B, first meeting (Alexandrian; the description in the first-meeting readaloud)**
> "Yagra sees you the moment you come through the door. Seven feet of half-orc with purplish-grey skin, a mop of black hair, and a jade pendant bearing the Zhentarim's winged-serpent sigil. She is already crossing the room before you've fully oriented."
> — `sources/Appendix_B_-_Player_Factions.md:564`

**Appendix D, the patron profile (day-one appearance)**
> "**Appearance:** Seven feet of half-orc with purplish-grey skin, tousled black hair, and shapely tusks. Red jade pendant bearing the Zhentarim sigil, worn openly. Cracks her knuckles reflexively."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1454`

**Campaign, first-meeting event (day-one tag)**
> "> Yagra Stonefist (Neutral, Half-Orc, she/her) :: Davil's bodyguard and the Doom Raiders' door at the Yawning Portal, who says exactly what she means and greets strangers by challenging them to an arm-wrestle."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:111`

**Campaign, first-meeting event (manner; day-one)**
> "Yagra is Friendly toward the party if **Yagra Courteous** is marked and Indifferent if it is not, but her manner is the same either way: loud, blunt and cheerful. She swears in nearly every sentence without meaning anything by it, cracks her knuckles before she speaks to strangers, takes words literally and misses sarcasm. She calls people by what they are (\"you, the tall one\") until they have earned a name. She never lies to a friend, never flatters, and never apologizes for winning."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:113`

**Campaign, first-meeting event (what she will talk about)**
> "Davil, whom she protects and speaks about the way someone speaks about the only person who ever asked what she wanted."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:117`

**Campaign, first-meeting event (what she will not talk about)**
> "She will not discuss Davil's business, the Doom Raiders' fronts or anything about the other cell. She says that is Davil's to tell."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:122`

**Campaign, first-meeting event (the arm-wrestle's rule)**
> "A character who fails loses without injury, and Yagra says \"Fair fight\" and claps them on the shoulder."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:156`

**Campaign, Trollskull patron entry (day-one; the arm-wrestle reason)**
> "- Arm-wrestling anyone willing. She will beat them. Does this because people relax after losing to her."
> — `campaign/guides/trollskull-manor/08-notable-patrons.md:117`

**Appendix D, the patron profile's reason (day-one)**
> "1. Is arm-wrestling anyone willing. She will beat them. She is not doing this to humiliate anyone; she does it because she enjoys it and because people relax after they lose to her. She has a gift for this."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1459`

**Adventure, the Tavern Brawl (page 21; she fights for her pride; the name spelled "Strongfist" here)**
> "The human combatants are five members of the Xanathar Guild (CE human {@creature bandit||bandits}). The one with the eye-shaped tattoos on his bald pate is their leader, Krentz. Their foe, Yagra Strongfist, is a half-orc employed by the Zhentarim (see the Yawning Portal Friendly Faces handout in appendix C). Yagra fights for her pride."
> — `sources/adventure-wdh.json:1618` (entry "Tavern Brawl", `"page": 21` at line 1606; see D3 for the spelling)

**Adventure, the tavern's readaloud for the brawl (page 21; the quest-time scene)**
> "Then all the noise is eclipsed by a shout: \"Ya pig! Like killin' me mates, does ya?\" Then a seven-foot-tall half-orc is hit by a wild, swinging punch from a male human whose shaved head is covered with eye-shaped tattoos. Four other humans stand behind him, ready to jump into the fray."
> — `sources/adventure-wdh.json:1615`

### A5. Business, the Yawning Portal and habits

**Adventure, the Yawning Portal introduction (page 40; the taproom table)**
> "If the characters seek out Davil, {@creature Yagra Stonefist|wdh} (see \"Familiar Faces\"), greets them and leads interested parties to a table in the center of the Yawning Portal's taproom, where her boss waits with drink in hand."
> — `sources/adventure-wdh.json:4004` (the Davil recruitment entry)

**Campaign, Trollskull patron tenday schedule (day-one; a staff rota)**
> "| 16 | Yagra Stonefist *(reroll if currently employed as Bouncer — she's on the door)* |"
> — `campaign/guides/trollskull-manor/06-tavern-time.md:72`

**Campaign, first-meeting, the hours (day-one)**
> "> Davil sits in his second-floor room from 8 p.m. until midnight every evening, and Yagra is at the bar from sundown until closing."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:49`

**Campaign, the Factions Guide first meeting (day-one)**
> "Yagra Stonefist is at the bar when the party arrives; how she greets them depends on their history from **The Yawning Portal** Event in **Finding Floon** and the **Yagra Courteous** Event Outcome."
> — `campaign/guides/factions/07-doom-raiders.md:37`

### A6. The Ziraj friendship, the trail marks and the loyalty

**Campaign, Ziraj's page (the trail marks; the claim has no adventure source)**
> "If wounded, he leaves intentional trail marks that he taught Yagra years ago."
> — `campaign/setting/notable-figures/doom-raiders/06-ziraj-the-hunter.md:23` (campaign-only; see F3)

**Campaign, Ziraj's page (the relationship)**
> "Ziraj is the Doom Raiders' Master of Assassination, a close friend of Fala Lefaliir (who shelters him at Corellon's Crown), a colleague Yagra will run across the city to save, and a presence on the Trollskull Alley rooftops that the party may not notice for weeks."
> — `campaign/setting/notable-figures/doom-raiders/06-ziraj-the-hunter.md:25` (the "run across the city to save" clause is quest-time; see C1)

**Adventure, Ziraj's friends list (page 201)**
> "If Ziraj sets out to kill someone, it's because one of his friends (Davil, Istrid, Skeemo, or Tashlyn) asked him to."
> — `sources/adventure-wdh.json:31965`. Yagra is not on this list.

### A7. Faith and deity

No source gives Yagra a faith. The adventure's Yagra entry (lines 1564 to 1570) names no god. The Organization page says the cell has "no sourced creed or initiation" (`06-doom-raiders.md:43`).

### A8. Signature belongings

- Red jade Zhentarim pendant worn openly: `campaign/setting/notable-figures/doom-raiders/02-yagra-stonefist.md:21`; `sources/Appendix_D_-_Running_the_Tavern.md:1454` ("Red jade pendant bearing the Zhentarim sigil, worn openly."); `sources/Appendix_B_-_Player_Factions.md:564` ("a jade pendant bearing the Zhentarim's winged-serpent sigil").
- The Organization page describes the pendant as one that "bears the Zhentarim's winged-serpent sigil" (`06-doom-raiders.md:43`). Appendix B agrees.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page's Summary: "> - *Half-orc mercenary, neutral, she/her*. Stat block: **Thug (with modifications)**." — `campaign/setting/notable-figures/doom-raiders/02-yagra-stonefist.md:5`
- Campaign, first-meeting event tag: "> Yagra Stonefist (Neutral, Half-Orc, she/her) :: Davil's bodyguard and the Doom Raiders' door at the Yawning Portal, who says exactly what she means and greets strangers by challenging them to an arm-wrestle." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:111`
- Campaign, the Ziraj event tag (quest-time tag; the alignment matches): "> Yagra Stonefist (Neutral, Half-orc, she/her) :: Davil's bodyguard, frightened for Ziraj and hiding it behind orders." — `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:42`
- Campaign, the Trollskull guide: "N female half-orc" (`campaign/guides/trollskull-manor/08-notable-patrons.md:114`) and "N half-orc" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:74`)
- Adventure: "{@i N female half-orc thug-for-hire}" — `sources/adventure-wdh.json:1568` ("N" is the abbreviation for neutral in the adventure's entry format)
- Appendix D: "*Doom Raiders — N female half-orc, Tough*" — `sources/Appendix_D_-_Running_the_Tavern.md:1450`
- Wiki: "| alignment5e    = [[Neutral]]" — wiki line 57 (edition: 5e)

**Species**
- Campaign, the page's Summary: "*Half-orc mercenary, neutral, she/her*" (`02-yagra-stonefist.md:5`)
- Campaign, the Organization page: "the half-orc Doom Raider who works the bar at the Yawning Portal" (`06-doom-raiders.md:53`)
- Adventure: "{@i N female half-orc thug-for-hire}" (`sources/adventure-wdh.json:1568`); "a half-orc employed by the Zhentarim" (`:1618`)
- Wiki: "| race           = [[Half-orc]]" — wiki line 14 (5e)

**Pronouns**
- Campaign: "she/her" (`02-yagra-stonefist.md:5`); "Yagra Stonefist (Neutral, Half-Orc, she/her)" (`ev-01-first-meeting.md:111`)
- Adventure: "{@i N female half-orc thug-for-hire}" (`sources/adventure-wdh.json:1568`). The adventure's readaloud uses "her" (line 1615: "The half-orc cracks her knuckles, roars, and leaps at the tattooed figure").
- Wiki: "| sex            = Female" — wiki line 13 (5e)

**Affiliation**
- Campaign, the page's Summary: "> - **Affiliation:** Zhentarim (Doom Raiders)" — `02-yagra-stonefist.md:6`
- Campaign, Organization H1: "# The Zhentarim (Doom Raiders)" — `06-doom-raiders.md:1`. Yagra's Key Member line: "- **Yagra Stonefist** — Street contact and Davil's bodyguard; present at the Yawning Portal." (`06-doom-raiders.md:98`)
- Adventure: "a half-orc employed by the Zhentarim" (`sources/adventure-wdh.json:1618`); "a Black Network mercenary" (`:1569`)
- Campaign, the Two Zhentarims rule: "Manshoon's splinter cell and Davil Starsong's Doom Raiders are entirely separate organizations." — `campaign/setting/villains/manshoon.md:19`
- Campaign, Yagra's Motivations: "keep the Doom Raiders safe from Manshoon's splinter" — `02-yagra-stonefist.md:15` (the splinter is Manshoon's cell, not hers)
- Wiki: "was a [[Zhentarim]] mercenary at the [[Yawning Portal]] around [[1492 DR]]" — wiki line 62 (5e)

**Stat block**
- Campaign, the page's Summary: "Stat block: **Thug (with modifications)**." — `02-yagra-stonefist.md:5`
- Adventure: "Yagra is a half-orc thug." with the 0-hit-point rule (`sources/adventure-wdh.json:1570`). The adventure gives no "with modifications" wording, and no CR, AC or HP line. Its role line is "half-orc thug-for-hire" (`:1568`).
- Wiki: "| class5e        = [[Thug]]" — wiki line 59 (5e; `refs5e` = `WDH5e-p20`, line 60). Challenge is blank (wiki line 58).
- Campaign, mechanics reference: "Thug and Veteran do not exist in XMM." (`docs/plans/doom-raiders-mechanics-reference.md:13`). "| Tough | Verified (XMM) | CR 1/2, AC 12, 32 HP, Pack Tactics. \"Thug\" does not exist in XMM. |" (`:253`).
- Campaign, the Rank 10 event (the block the campaign uses for her in play): "Yagra uses the **Warrior Veteran** stat block with two changes. Her Greatsword attack is replaced by a pair of iron-studded gauntlets with the same attack bonus and damage, but bludgeoning. She also has Relentless Endurance once per day: the first time she is reduced to 0 Hit Points and not killed outright, she drops to 1 Hit Point instead." — `campaign/quests/faction-events/doom-raiders/r10-viper/ev-01-viper.md:128`
- Campaign, the Ziraj event's design note: "Yagra doesn't fight, because her Notable Figures block is a \"Thug\", which does not exist in the 2024 Monster Manual." — `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/design-notes.md:11`
- Campaign, the kill-team line in the Ziraj event (not Yagra's block): "Use the **Warrior Veteran**, **Assassin** and **Spy** stat blocks from the 2024 *Monster Manual*, each unchanged except as noted for Ondra Kell." — `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:149`
- Trollskull and Appendix D tavern labels: "Tough" (`08-notable-patrons.md:114`; `Appendix_D_-_Running_the_Tavern.md:1450`).

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/doom-raiders/02-yagra-stonefist.md`. The page has no Background, Personality or Connections section yet.

### C1. Page sentences

| # | Line | Sentence (exact) | Status | Where the event or fact already lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Half-orc mercenary, neutral, she/her*. Stat block: **Thug (with modifications)**." | Day-one name tag. The stat block is not a 2024 name (B, D1) | section B |
| 2 | L6 | "> - **Affiliation:** Zhentarim (Doom Raiders)" | Day-one | `06-doom-raiders.md:1`, `:8`, `:98` |
| 3 | L7 | "> - **Featured in:** **Finding Floon**, **Trollskull Alley**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Doom Raiders Mission 5 — The Yellowspire Job**, **Doom Raiders Mission 6 — Ziraj's Last Hunt**, **Xanathar Sewer Hideout**" | Quest-name list (routed) | `campaign/quests/` folders; the Factions Guide's Missions table `campaign/guides/factions/07-doom-raiders.md:70` and `:71`; `campaign/locations/xanathar-sewer-hideout/` |
| 4 | L11 | "**Resonance.** Yagra should inspire respect with her physical presence and directness, endearment with her arm-wrestling habit (which is how she puts people at ease), and loyalty when the party sees how far she will go for the Doom Raiders." | Day-one as a play tip. The last clause points at the events where she goes far for the faction, not at a narrated event. Keep; drafter's call (borderline) | `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:5` and `:36` |
| 5 | L13 | "**Emotions.** Yagra most often feels casual confidence, competitive enjoyment, fierce protectiveness, unspoken pride in the Doom Raiders, controlled urgency in crisis, and a matter-of-fact acceptance of her own history that makes other people uncomfortable." | Day-one. "controlled urgency in crisis" matches the Ziraj event's tone (`m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:42`: "frightened for Ziraj and hiding it behind orders") | "a matter-of-fact acceptance of her own history": `sources/Appendix_D_-_Running_the_Tavern.md:1462` ("She tells it the way people tell old weather reports.") |
| 6 | L15 | "**Motivations.** Yagra wants to protect Davil Starsong, keep the Doom Raiders safe from Manshoon's splinter, and arm-wrestle anyone who looks like they might be interesting." | Day-one. Keep | `sources/adventure-wdh.json:1569` ("gets paid to protect a Zhent negotiator named ... Davil Starsong"); `campaign/setting/organizations/06-doom-raiders.md:37` |
| 7 | L17 | "**Inspirations.** When playing Yagra, channel Drax (*Guardians of the Galaxy*), Michonne (*The Walking Dead*), and Rosa Diaz (*Brooklyn Nine-Nine*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Yagra is seven feet of purplish-grey half-orc wearing a red jade Zhentarim pendant openly, cracking her knuckles at the Yawning Portal bar. To those she trusts, she arm-wrestles patrons because people relax after losing to her. Deep down, she tells the story of the slaver ship she was on before the Doom Raiders found her like an old weather report, wanting nothing for the telling." | Day-one. The slaver-ship story is backstory (A2). Its telling is a trait the sources also give | `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:140`; `sources/Appendix_D_-_Running_the_Tavern.md:1462`; `campaign/guides/trollskull-manor/08-notable-patrons.md:117` and `:120` |
| 9 | L23 | "**Morale.** In a fight, Yagra fights with her pride. She is disappointed if someone interferes in a fair fight, but she will arrive at your door at 2 AM, armor on, not winded despite clearly having run, if one of her people is in danger. She does not knock politely." | **Quest-derived specifics.** "fights with her pride" is day-one (`sources/adventure-wdh.json:1618`). "at 2 AM, armor on, not winded despite clearly having run" is the Ziraj event's arrival: `m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:5` ("reaches Trollskull Manor at 02:10") and `:36` ("in full armor with her breath perfectly even. Her boots are wet to the ankle from running through the gutters of Sail Street."). The general trait ("if one of her people is in danger") is day-one; the Organization page carries it (`06-doom-raiders.md:37`) | as shown in the Where column |
| 10 | L25 | "**Relationships.** Yagra is Davil Starsong's bodyguard, a Doom Raiders operative who appears as a tavern bouncer candidate (the **Trollskull Manor** guide), a Yawning Portal regular, and the person who will run across the city at night to save Ziraj the Hunter." | Day-one except the last clause, "the person who will run across the city at night to save Ziraj the Hunter", which is **quest-time** (Mission 6) | Bodyguard: `sources/adventure-wdh.json:1569`; Bouncer: `campaign/guides/trollskull-manor/03-staff-and-hiring.md:74`; quest: `m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:5` ("when Yagra Stonefist reaches Trollskull Manor at 02:10 to say that a Splinter kill team is hunting Ziraj the Hunter across the rooftops") and `campaign/guides/factions/07-doom-raiders.md:71` (the Mission 6 row) |
| 11 | L29 | "A towering purplish-grey half-orc wearing a Zhentarim pendant openly at the Yawning Portal bar, who arm-wrestles patrons as her preferred method of introduction and has never been seen to lose." | Day-one. **30 words** (brief limit 21). "has never been seen to lose" is in tension with the Appendix B brawl variant (D4) | `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:113`; `sources/Appendix_B_-_Player_Factions.md:598` |

Quest-time clauses on the page: row 10 (the last clause) and row 9 (the 2 AM and "clearly having run"). Row 4 is borderline (the events she goes far for are quest-time, but the sentence is a play tip).

### C2. Quest-time clauses in the voice profile (`.claude/skills/character-voices/voices/doom-raiders.md`, "### Yagra Stonefist", lines 26-40)

Ruling 16: a quest-time clause in a profile gets the same day-one restatement as ruling 3, and the profile changes to match.

- Line 27 (tagline): "*A seven-foot half-orc who says exactly what she means, loudly, and settles introductions by arm-wrestling.*" — day-one.
- Line 33 (Personality in speech): "Casual confidence, and friendly challenges as a way of saying hello. She tells awful facts about her own past without any weight, which unsettles people. Protectiveness makes her curt and urgent. When one of hers is in danger, she's all orders." — day-one as a trait. "When one of hers is in danger" is a general trait, not an event. Keep.
- Line 35 (Signature phrases): "\"Arm first, talk after.\" / \"Fair fight.\" / \"Where is he?\"" — day-one. No quest-time clause is in the text.
- Line 40 (Sample line, "*Under pressure*"): "\"Ziraj is bleeding somewhere in the fucking Dock Ward. Get your boots on. Now.\"" — **quest-time**. "Ziraj is bleeding" is the premise of the Ziraj event (`m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:5`). The drafter must restate it as a day-one "under pressure" line, and the skill file changes to match.
- Lines 38 (greeting) and 39 (business: "Davil wants you. Fuck knows why. I'll find out after I beat you."): day-one.
- Lines 29-32, 34 and 36 (Sound, sentence shape, word choice, swearing, quirks, never): day-one.

### C3. Quest-time context on the Organization page that feeds Yagra's page

- `campaign/setting/organizations/06-doom-raiders.md:37` (the loyalty bullet): the 2 AM and the trail marks come from the quest events and from one campaign page; "Ziraj taught her the trail marks" has no adventure source. The drafter should not carry the 2 AM clause into a day-one Background.

---

## D. Conflicts

**D1. Stat block name (Thug)**
- Page: "Stat block: **Thug (with modifications)**." — `campaign/setting/notable-figures/doom-raiders/02-yagra-stonefist.md:5`
- Adventure: "Yagra is a half-orc thug." (`sources/adventure-wdh.json:1570`). The adventure uses the word "thug" as a role, and gives no "with modifications".
- Campaign mechanics reference: "Thug and Veteran do not exist in XMM." (`docs/plans/doom-raiders-mechanics-reference.md:13`)
- Campaign, the Ziraj event's design note: "Yagra doesn't fight, because her Notable Figures block is a \"Thug\", which does not exist in the 2024 Monster Manual." (`m06-zirajis-last-hunt/design-notes.md:11`)
- Campaign, the Rank 10 event: "Yagra uses the **Warrior Veteran** stat block with two changes." (`r10-viper/ev-01-viper.md:128`)
- Campaign, the Factions Guide's Viper rank: "(use **veteran** stat block)" (`campaign/guides/factions/07-doom-raiders.md:58`). The Factions Guide uses lower-case "veteran"; the event says "Warrior Veteran".
- Campaign, the consistency-pass note: "**Yagra's stats:** M6:44 uses a plain Warrior Veteran. r10:128 gives her gauntlets and Relentless Endurance." (`docs/plans/doom-raiders-consistency-pass-s39.md:130`)
- Campaign, the Harpers out-of-scope note: "**Yagra:** stat block \"Thug (with modifications)\"; Thug isn't a 2024 name, and r10 uses Warrior Veteran." (`docs/plans/harpers-out-of-scope-notes.md:297`)
- Higher rank: CLAUDE.md requires 2024 names. The page's "Thug" is not a 2024 name. The Rank 10 block is the one the campaign uses for her in play. Left to the orchestrator to choose the 2024 block for the page's Summary.

**D2. Stat block label on the tavern side ("Tough")**
- Trollskull guide: "**Yagra Stonefist** *(Doom Raiders, N female half-orc, Tough; see **The Zhentarim (Doom Raiders)** organization page)*" — `campaign/guides/trollskull-manor/08-notable-patrons.md:114`
- Appendix D: "*Doom Raiders — N female half-orc, Tough*" — `sources/Appendix_D_-_Running_the_Tavern.md:1450`
- Campaign mechanics reference: "| Tough | Verified (XMM) | CR 1/2, AC 12, 32 HP, Pack Tactics. \"Thug\" does not exist in XMM. |" (`docs/plans/doom-raiders-mechanics-reference.md:253`). "Tough" is a 2024 name; the page's "Thug" is not.
- Higher rank: the mechanics reference (for the 2024 name). The tavern "Tough" is a tavern-guide tag, not a stat block. Left to the orchestrator.

**D3. Surname: Stonefist or Strongfist**
- Page, the Trollskull guide, the Organization page, the first-meeting event, the Ziraj event, the Factions Guide and Appendix B all say "Stonefist". The adventure's Familiar Faces entry reads `"name": "Yagra Stonefist",` (`sources/adventure-wdh.json:1564`), and its pronunciation table reads "{@creature Yagra Stonefist|WDH}" (`:385`).
- Adventure, Tavern Brawl (page 21): "Their foe, Yagra Strongfist, is a half-orc employed by the Zhentarim" — `sources/adventure-wdh.json:1618`
- Wiki note: "Page 21 of ''[[Waterdeep: Dragon Heist]]'' refers to Yagra's last name as \"Strongfist\". Since her all other mentions from that source call her by the last name \"Stonefist\", we assume that this one instance was in error." — wiki line 62 (note).
- Higher rank: the campaign (Stonefist), and the adventure's own other entries. The page keeps "Stonefist".

**D4. "Has never been seen to lose" against the Tavern Brawl variant**
- Page Overview: "who arm-wrestles patrons as her preferred method of introduction and has never been seen to lose." — `campaign/setting/notable-figures/doom-raiders/02-yagra-stonefist.md:29`
- Appendix B, the first-meeting variant header: "**If the party stayed out of the brawl and Yagra lost:**" — `sources/Appendix_B_-_Player_Factions.md:598`, followed by "Yagra is at the bar. There is a fading bruise along her jaw that was not there the last time you saw her." (`:601`)
- Adventure, Tavern Brawl (page 21): "Yagra fights for her pride." (`sources/adventure-wdh.json:1618`) — no outcome.
- The Overview's claim is about arm-wrestling. The Appendix B variant is a bar brawl with Krentz's crew, a quest-time event. The two can both be true, but the drafter should not write "never seen to lose" in a Background as a general fact.
- Higher rank: none. Flag for the orchestrator.

**D5. Ziraj's teaching of the trail marks**
- Organization page: "Ziraj taught her the trail marks he leaves when he is wounded" — `campaign/setting/organizations/06-doom-raiders.md:37`
- Ziraj page: "he leaves intentional trail marks that he taught Yagra years ago" — `campaign/setting/notable-figures/doom-raiders/06-ziraj-the-hunter.md:23`
- Ziraj event: "Find Ziraj by following his trail marks, by reading the kill team's search pattern or by asking Fala Lefaliir, all before the sweep reaches him at 02:35." — `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:7` (no teaching is stated)
- No adventure source. Campaign-only; the drafter may use it as a day-one fact (it is on two campaign pages) or flag `[research]`.

**D6. Her job at the Portal: bar, door or bouncer**
- Organization page: "**Street Contact:** Yagra Stonefist — the half-orc Doom Raider who works the bar at the Yawning Portal." (`06-doom-raiders.md:53`)
- Trollskull guide, Bouncer Candidate 1: "Doom Raiders (Zhentarim)." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:74`) and the schedule "(at the bar, or on the door if she is the Bouncer)" (`06-tavern-time.md:28`). These are options the tavern guide allows, not a conflict. The Relationships line should name the bar as her post, and the Bouncer role as the hiring option.

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/design-notes.md:11`: the "Thug" line (D1). Stale against `r10-viper/ev-01-viper.md:128`.
- `campaign/guides/trollskull-manor/08-notable-patrons.md:114`: "Tough" (D2).
- `sources/Appendix_D_-_Running_the_Tavern.md:1450`: "Tough" (D2).
- `sources/adventure-wdh.json:1618`: "Yagra Strongfist" (D3).
- `campaign/guides/factions/07-doom-raiders.md:58`: "(use **veteran** stat block)" (D1; lower-case label).
- `docs/plans/doom-raiders-consistency-pass-s39.md:130`: "**Yagra's stats:** M6:44 uses a plain Warrior Veteran. r10:128 gives her gauntlets and Relentless Endurance." — a docs note that the event files still disagree.
- `docs/plans/harpers-out-of-scope-notes.md:297`: "**Yagra:** stat block \"Thug (with modifications)\"; Thug isn't a 2024 name, and r10 uses Warrior Veteran." (D1).

**E2. Routed quest references (quest-time; the day-one page must not restate them)**

Yagra's own quest appearances, by file:
- `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:7` ("Yagra Stonefist greets them in one of five ways depending on how they treated her in **The Yawning Portal** Event of **Finding Floon**."), `:57` (the Yagra Courteous gate), `:140` (slaver-ship Q&A), `:156` (arm-wrestle rule).
- `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md` (the brawl and the Yagra Courteous Event Outcome; not read line by line).
- `sources/Appendix_C_-_Player_Faction_Missions.md:524` ("The party encountered Yagra at the Yawning Portal during the brawl with the Xanathar Guild thugs in Act I. How that encounter went shapes how she arrives at the tavern door.")
- `sources/adventure-wdh.json:1606` to `:1618` (the Tavern Brawl, page 21; Finding Floon).
- `sources/adventure-wdh.json:4029` ("If the characters want to speak with Tashlyn directly, Yagra can arrange a meeting in the City of the Dead or some other quiet place.") — quest-time (the Tashlyn briefing).
- `sources/Appendix_D_-_Running_the_Tavern.md:521` to `:556` (Candidate 1, Yagra as a Trollskull bouncer candidate; her arrival depends on the Act I brawl). `:535` ("I still owe you. This is how I settle it. You need someone on the door. I need work between Davil's jobs. Say yes.") and `:547` ("Davil Starsong said you have a place in the North Ward that needs a door.").
- `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:47` ("The next morning, Ches 27, Yagra Stonefist is at the bar of the Yawning Portal."), `:59` (tag: "Davil's bodyguard, angry at herself for standing down, and blunt about everything.") and `:69` (her line about the custody wing) — quest-time.
- `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:17` ("Yagra Stonefist keeps them at the long tables in the taproom while the members go through to Davil.") — quest-time.
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:5` (the Splinter kill team; "when Yagra Stonefist reaches Trollskull Manor at 02:10"), `:32` ("Yagra Stonefist comes to Trollskull Manor herself, because a flying snake is too slow."), `:36` ("...and when you open it Yagra Stonefist is on the step in full armor with her breath perfectly even."), `:114` ("Yagra picks Ziraj up without a word, and he lets her."), `:177` ("...and Yagra stands over him with both fists shut and her jaw working."), `:348` ("If Ziraj lives, Yagra stays at Fala's for two days."), `:350` ("If Ziraj dies, Yagra stays at Corellon's Crown for the same two days and drinks the tea Fala puts in front of her. She swears at the wall for most of the first night."), `:359` ("Read by **Ardragon**, where Davil announces that the favor is gone and offers **Yagra's Grab**, a capture-only substitute of Yagra and two Toughs").
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/overview.md:17` ("Yagra Stonefist reaches Trollskull Manor at 02:10, armor on and breathing evenly despite the run from Sail Street.") and `:60` ("- **Yagra Stonefist** (Doom Raiders): brings the news, guides the party to the trail marks and carries Ziraj.").
- `campaign/quests/faction-events/doom-raiders/r10-viper/ev-01-viper.md:8` ("Learn how to call Yagra Stonefist, or a substitute, as muscle for one operation per quest.") and `:128` (the Warrior Veteran block).
- `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md` (not read line by line).
- `campaign/gazetteer/waterdeep/castle-ward.md:38` ("Mirt, Jalester Silvermane, Yagra Stonefist and Jeryth's awakened rats each lead a party to it") — quest-time (the sewer stair).
- `campaign/guides/trollskull-manor/06-tavern-time.md:28` ("First tenday after **Gralhund Villa** | Renaer Neverember, Floon Blagmaar, Yagra Stonefist (at the bar, or on the door if she is the Bouncer) | ...") — schedule row, quest-time.
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:74` (Bouncer Candidate 1; the four interview variants depend on the Act I brawl) — routed to Trollskull Manor.
- `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md` (named; not read line by line).

**E3. Faction-label checks**
- Affiliation "Zhentarim (Doom Raiders)" matches the organization H1 (`06-doom-raiders.md:1`) and the Factions Guide (`07-doom-raiders.md:3`).
- Not Manshoon's cell: `manshoon.md:19` (quoted in B).

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in Draft Notes.

**F1. Birth year, age, parents, siblings, children, home town other than Waterdeep.** No source gives any of these. The wiki infobox fields `age` (line 17), `dob` (line 21), `parents` (line 29) and `siblings` (line 31) are blank. The only physical age cue is "Seven feet" (`campaign/guides/trollskull-manor/08-notable-patrons.md:116`; `sources/Appendix_D_-_Running_the_Tavern.md:1454`). Do not give an age.

**F2. The slaver ship.** The sources give: "I was on a slaver ship, chained to a bench. Davil's people took the ship, and he asked me what I wanted to do next. I said fight, so here I am. It's a good job." (`ev-01-first-meeting.md:140`) and "the slaver ship she was on before the Doom Raiders found her" (`Appendix_D_-_Running_the_Tavern.md:1462`). Missing: where the ship sailed, when, who the captors were, how long she was held, who else was aboard, what she was called before. Consistent with the sources: Davil's people freed her, Davil asked her what she wanted, and she chose to fight. Anything more is `[design]`.

**F3. Ziraj and the trail marks.** The Organization page says "Ziraj taught her the trail marks he leaves when he is wounded" (`06-doom-raiders.md:37`); the Ziraj page says "that he taught Yagra years ago" (`06-ziraj-the-hunter.md:23`). No adventure or Alexandrian source says it. The Ziraj event uses the trail marks as a search clue (`m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:7`). Consistent with the sources: she knows the marks; the teaching is campaign-only. The drafter may use "years ago" as the campaign's own claim, or flag `[research]`.

**F4. How she came to the Doom Raiders.** "Yagra came along later, once she'd given us good reason to keep her." (`ev-01-first-meeting.md:236`, Davil). No date. "Davil's people took the ship" (`:140`). Consistent with the sources: she joined after the five; no year, no place.

**F5. Her personal history with Xanathar's Guild.** The Trollskull guide says she "Hates Xanathar's Guild with uncomplicated fury (personal history)." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:74`). The "personal history" is not given. The adventure's brawl (`sources/adventure-wdh.json:1618`) is the only sourced confrontation. The drafter must not invent a specific event without `[design]`.

**F6. Her relationship with Krentz.** Krentz is the Xanathar lead in the Tavern Brawl (`sources/adventure-wdh.json:1618`). Appendix B gives the brawl variants (`Appendix_B_-_Player_Factions.md:561` to `:611`), and Appendix D gives the aftermath at `Appendix_D_-_Running_the_Tavern.md:535`. Nothing else.

**F7. Her faith, her god, her oath.** None. The adventure's entry (`:1564` to `:1570`) names no god. The Organization page's Doctrine bullet says "The cell has no sourced creed or initiation" (`06-doom-raiders.md:43`).

**F8. Personal goals beyond Davil and the cell.** The Motivations line (`02-yagra-stonefist.md:15`): "Yagra wants to protect Davil Starsong, keep the Doom Raiders safe from Manshoon's splinter, and arm-wrestle anyone who looks like they might be interesting." The adventure: "Yagra finds the job boring and likes to pass the time by challenging adventurers to arm wrestle." (`sources/adventure-wdh.json:1569`). Possible `[design]` goals must stay consistent with: the protection of Davil (`ev-01-first-meeting.md:117`), the Doom Raiders' safety, her arm-wrestling, and her refusal to discuss the other cell (`ev-01:122`). A goal that needs a new quest event is barred by ruling 17.

**F9. Her habit of running.** The Ziraj event shows her running from Sail Street (`m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:36`), and the Morale line gives a 2 AM habit. The habit is quest-derived. A Background may say she runs when one of hers is hurt, if the drafter marks it `[design]`; the 2 AM clause is quest-time and stays out of the day-one text.

**F10. Music, reading, a craft.** None. Arm-wrestling is her only sourced leisure (A5).

**F11. Her relationship with Durnan.** The wiki says "soon also became involved with some adventurers and/or [[Durnan]]." (wiki line 72, edition 5e, `WDH5e-p21`). This is a Finding Floon-time statement. It is not usable as a day-one fact without a tag.

**F12. Family or home.** None beyond "Waterdeep" as home (wiki line 11). Do not invent a family member without `[design]`.

---

## G. Source facts that hint at the figure's inner life (for the Background; do not contradict)

- "Davil, whom she protects and speaks about the way someone speaks about the only person who ever asked what she wanted." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:117`. (Her loyalty to Davil; a debt to the one who asked.)
- "She will not discuss Davil's business, the Doom Raiders' fronts or anything about the other cell. She says that is Davil's to tell." — `ev-01-first-meeting.md:122`. (She keeps others' business.)
- "I was on a slaver ship, chained to a bench. Davil's people took the ship, and he asked me what I wanted to do next. I said fight, so here I am. It's a good job." — `ev-01-first-meeting.md:140`. (The origin of her loyalty; her answer was "fight.")
- "She just wanted it said in a room she trusts." — `sources/Appendix_D_-_Running_the_Tavern.md:1462`. (She wants her story heard.)
- "She does not want anything from the party for telling it." — `Appendix_D_-_Running_the_Tavern.md:1462` (the same entry).
- "Has a question she has been holding for a while: what did the party do with the information they recovered from wherever they were last. She is asking because Davil asked her to. She is also asking because she wants to know. These are the same." — `Appendix_D_-_Running_the_Tavern.md:1461`. (Her curiosity; the question is a tavern-event prompt.)
- "She is not doing this to humiliate anyone; she does it because she enjoys it and because people relax after they lose to her." — `Appendix_D_-_Running_the_Tavern.md:1459`. (She is not cruel through the game.)
- "Yagra finds the job boring and likes to pass the time by challenging adventurers to arm wrestle." — `sources/adventure-wdh.json:1569`. (Boredom with the work; the game is her relief.)
- "Yagra fights for her pride." — `sources/adventure-wdh.json:1618`.
- "She never lies to a friend, never flatters, and never apologizes for winning." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:113`. (Honesty as a code.)
- "She is disappointed if someone interferes in a fair fight" — `campaign/setting/notable-figures/doom-raiders/02-yagra-stonefist.md:23` (the page's own line; fairness as a code).
- "Fair fight." — voice, `.claude/skills/character-voices/voices/doom-raiders.md:35` (signature phrase).
- "Hates Xanathar's Guild with uncomplicated fury (personal history)." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:74`. (A grudge; the history is not given.)
- "Yagra will reach a threatened friend's door at 2 AM in full armor, and Ziraj taught her the trail marks he leaves when he is wounded" — `campaign/setting/organizations/06-doom-raiders.md:37`. (Loyalty to friends; quest-derived specifics.)
- "frightened for Ziraj and hiding it behind orders" — `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:42`. (Quest-time tag; her fear for a friend.)
- "She tells awful facts about her own past without any weight, which unsettles people. Protectiveness makes her curt and urgent." — `.claude/skills/character-voices/voices/doom-raiders.md:33` (voice).
- "She calls people by what they are (\"you, the tall one\") until they have earned a name." — `ev-01-first-meeting.md:113` (her way of judging people).
- "A character who declined stays \"the short one\" or \"the one with the sword\" until they have earned a name another way." — `ev-01-first-meeting.md:156`. (Quest-time scene; the same habit.)

---

## Cross-references (the Yagra topic in other files)

- `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:15` and `:25` (Davil's page names Yagra as his bodyguard in Relationships; the pages agree).
- `campaign/setting/notable-figures/doom-raiders/06-ziraj-the-hunter.md:23` and `:25` (the trail marks and the "run across the city" line).
- `campaign/setting/notable-figures/bregan-daerthe/08-quilm.md` (Quilm and Yagra as Trollskull staff; the Grep matched the file; not read in this pass).
- `campaign/setting/geography/city-of-the-dead.md`, `campaign/setting/deities/gruumsh.md` (Yagra named; not read in this pass).
- `campaign/gazetteer/waterdeep/castle-ward.md:38` (the sewer stair; routed).
- `campaign/locations/xanathar-sewer-hideout/q05-sleeping-area.md` (Yagra named; not read in this pass).
- `campaign/guides/trollskull-manor/06-tavern-time.md:28` and `:72`, `08-notable-patrons.md:114` to `:120`, `03-staff-and-hiring.md:74` (tavern roles).
- `campaign/guides/gm-guide/player-factions-overview.md` (the Yagra role; not read in this pass).
- `campaign/quests/act-i/finding-floon/` (the Yawning Portal brawl; not read line by line).

---

## Not found

- Searched for: birth year, age, parents, siblings, spouse, children, home town other than Waterdeep, origin, the slaver ship's location, date and captors, the date she joined, her faith, her family, her Xanathar history beyond the brawl: `campaign/` (Grep for `Yagra|Stonefist|Strongfist`; the file list is in the cross-references), `sources/adventure-wdh.json` (Grep for `Yagra|Stonefist|Strongfist`; the entry at lines 1564 to 1570 and the brawl at 1604 to 1618 read in full), `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md` (Grep), `sources/Appendix_D_-_Running_the_Tavern.md` (Grep; the patron entry at 1449 to 1462 read in full).
- Ziraj teaching her the trail marks in any adventure or Alexandrian source: not found. The campaign's claim is at `06-doom-raiders.md:37` and `06-ziraj-the-hunter.md:23`.
- A creature block for Yagra in the adventure with CR, AC and HP: not found (`sources/adventure-wdh.json:1564` to `:1570`). The only block is "half-orc thug" with the 0-HP rule.
- Yagra's age: not found.
- Her relationship with Krentz beyond the brawl: not found.
- Her stat block in 2024 terms in any file other than the Rank 10 event (`r10-viper/ev-01-viper.md:128`) and the Ziraj design note (`m06-zirajis-last-hunt/design-notes.md:11`): not found.
- The Alexandrian PDFs for Yagra: no Yagra text found in `sources/3. Player Character Factions.pdf` (pp.2-3, read for the Davil notes). The other PDFs were not read for Yagra.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. The Organization page's Draft Notes (`06-doom-raiders.md:193`) say the research tools could not open `Davil and the Doom Raider Zhents + Elf Killer mission and more.docx`, and the Yagra material may be in it. Extract it before the Yagra Background is drafted.
- The Doom Raiders bundle `sources/research/pass5-bundles/doom-raiders/wiki.txt` was searched for Davil and returned Davil's lines only; it was not searched for Yagra's lines in this pass.
