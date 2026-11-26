# Pass 6 research notes: Tashlyn Yafeera

Page: `campaign/setting/notable-figures/doom-raiders/05-tashlyn-yafeera.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Tashlyn is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/06-doom-raiders.md` (heading "The Zhentarim (Doom Raiders)")
Factions Guide: `campaign/guides/factions/07-doom-raiders.md`
Voice profile: `.claude/skills/character-voices/voices/doom-raiders.md` (### Tashlyn Yafeera, lines 80-94)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-doom-raiders/05-tashlyn-yafeera.txt` (a Tashlyn page exists; "wiki line N" means that file's line N)

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field is given where the entry has one.
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` PDF p.3 (printed p.25) was read as a rendered page. The Zhentarim gold paragraph is quoted from that image and needs a `pdftotext -layout` check before it goes into prose. PDF p.2 (printed p.24) has no Doom Raiders paragraph.
- Alexandrian markdown: `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md`, `sources/Appendix_D_-_Running_the_Tavern.md`.
- No shell was available and no edit tool was available, so this file was written whole. `voicecheck.py` was not run. No other file was edited.
- Quest-file hits are Grep output. The `Tashlyn|Yafeera` hits total 503 lines in 61 files under `campaign/` (count run). The Cross-references section lists every file with its count and quotes the non-quest lines. The line-by-line list of quest-file hits is not copied; those lines are quest-time and routed.

## Findings that change how the page is written

1. **Three lines assume Davil's arrest.** The Resonance, Motivations and Relationships lines say "when she takes over as faction contact", "after Davil's arrest" and "Davil's replacement as faction contact after his arrest" (`05-tashlyn-yafeera.md:11`, `:15`, `:25`). Davil's arrest is a quest event (`sources/adventure-wdh.json:4028`). The organization page already removed the same wording (`campaign/setting/organizations/06-doom-raiders.md:187`). The drafter has to restate these as day-one facts or route them.
2. **Alignment conflicts with the wiki.** The page says "lawful evil" (`05-tashlyn-yafeera.md:5`), and every campaign quest tag agrees. The wiki's 5e alignment is "Neutral" (wiki line 57). Campaign wins; the wiki ranks last (see D1).
3. **The stat block "Swashbuckler" has no source.** The page's Summary (`:5`) is the only file that gives Tashlyn a stat block. The published adventure gives none (`sources/adventure-wdh.json:31950-31956`). The wiki gives a CR (wiki line 58: "challenge5e    = 9") and no block name. Treat the block as the page's label without a source (see D2).
4. **Her post is a bodyguard cover that earned a captaincy.** The adventure gives the order (`sources/adventure-wdh.json:31955`). Three other campaign files state the captaincy as her post or as cover (`governance-and-guilds/city-watch.md:69`, `history/04-the-founding-of-chains.md:58`, `s01-davils-arrest/ev-01-davils-arrest.md:107`). The organization page settled the adventure's order (`06-doom-raiders.md:165`). See D3.
5. **The Overview is 37 words** (`05-tashlyn-yafeera.md:29`). The brief limit is 21.

---

## A. Background facts by theme

### A1. Origin, family, early life

**Adventure, Tashlyn entry (page 199)**
> "Born to a well-off family in Calimshan, Tashlyn has an unfettered sense of superiority. Quick to anger, she hates to back down from a fight. She respects anyone who can best her in melee combat."
> — `sources/adventure-wdh.json:31956` (entry "Tashlyn Yafeera", page 199)

**Wiki, Relationship (ref `WDH-199-200`, 5e)**
> "Tashlyn came from a wealthy family that was well-known in the southern land of [[Calimshan]].<ref name="WDH-199-200" /> "
> — wiki line 68 (edition: 5e, *Waterdeep: Dragon Heist* pp.199-200, from the ref name)

**Wiki, Personality (ref `WDH-199-200`, 5e)**
> "Tashlyn believed herself superior to most people. She was quick to anger and never stopped a fight. However, Tashlyn respected anyone that defeated her.<ref name="WDH-199-200" />"
> — wiki line 65 (edition: 5e, as above)

No source gives a birth year, age, parents, siblings, family name or a home district in Calimshan. The wiki's `age`, `dob`, `parents` and `siblings` fields are blank (wiki lines 17, 21, 29, 31).

### A2. Adventuring years and the Zhentarim

**Adventure, Zhentarim section (line 31916 is the Doom Raiders introduction; no page field)**
> "The Doom Raiders were five unscrupulous adventurers who liked to plunder lich lairs (called \"dooms\" by some). They gave up adventuring to join the Black Network and came to Waterdeep three years ago with plans to establish a Zhentarim foothold in the city. In that time, they have forged alliances with various nobles and guilds and run afoul of others, all the while fending off Harper spies."
> — `sources/adventure-wdh.json:31916`

**Wiki, History (refs `WDH-40`, `WDH-198-199`, 5e)**
> "Tashlyn was once an adventurer but decided to join the Zhentarim with her fellow companions.<ref name="WDH-40">{{Cite book/Waterdeep: Dragon Heist|40}}</ref> In [[1489 DR]], they were sent to establish a Zhent foothold in Waterdeep.<ref name="WDH-198-199">{{Cite book/Waterdeep: Dragon Heist|198-199}}</ref>"
> — wiki line 73 (edition: 5e, *Dragon Heist* pp.40 and 198-199)

**Wiki, Relationship (ref `WDH-199-200`, 5e)**
> "Tashlyn was a member of the [[Doom Raiders]] adventuring company. She and her companions composed the leadership of the Zhentarim of Waterdeep. Despite her deception as his "bodyguard", Tashlyn genuinely respected her patron [[Vorondar Levelstone|Vorondar]].<ref name="WDH-199-200" />"
> — wiki line 70 (edition: 5e)

**Campaign, Doom Raiders History (day-one; the 1489 DR arrival)**
> "- **1489 DR, the cell reaches Waterdeep:** The Doom Raiders are a cell of experienced Zhentarim operators who arrived in Waterdeep in 1489 DR, the first Zhentarim cell in the city, and built a network of commercial fronts they genuinely believe in. They were sent to establish a Zhentarim foothold, and no source names who sent them (*Dragon Heist*, 5e; Forgotten Realms Wiki, *Doom Raiders*, 5e)."
> — `campaign/setting/organizations/06-doom-raiders.md:25`

**Campaign, Doom Raiders Structure (the Master's title and post)**
> "- **Tashlyn Yafeera, Master of Arms and Mercenaries:** She provides armor, weapons and training to the sellswords on the Network's payroll, and her bodyguard post at the South Gate is her cover."
> — `campaign/setting/organizations/06-doom-raiders.md:60`

### A3. The South Gate post and the magister

**Adventure, Tashlyn entry (page 199), the title**
> "{@creature Tashlyn Yafeera|wdh|Tashlyn} is Master of Arms and Mercenaries for the Waterdeep Zhentarim. In this role, she provides armor, weapons, and training to sellswords on the Black Network's payroll."
> — `sources/adventure-wdh.json:31954`

**Adventure, Tashlyn entry (page 199), the cover (full paragraph)**
> "Tashlyn has established a useful cover by serving as a bodyguard to Vorondar Levelstone, a dwarf magister stationed at the South Gate. She likes the dwarf and has earned his confidence, allowing her to reach the rank of captain in the City Guard. In that position, she watches over traffic that passes through the gate-and ensures that her associates in the Black Network can come and go freely."
> — `sources/adventure-wdh.json:31955`

**Wiki, History, 1492 DR cover (ref `WDH-199-200`, 5e)**
> "In [[1492 DR]],{{WDH-time}} as a cover, Tashlyn acted as a bodyguard to Vorondar Levelstone, a magistrate of the South Gate. Thanks to her employer, Tashlyn was recruited into the [[City Guard (Waterdeep)|City Guard]] and used her position to permit free access to the city for all her Zhent companions.<ref name="WDH-199-200" />"
> — wiki line 75 (edition: 5e). The next sentence in the same paragraph is quest-time (see C, last paragraph).

**Campaign, Organization page, GM Notes (the cover and the trust)**
> "> - **Tashlyn's cover:** Tashlyn is the Master of Arms and Mercenaries. Her cover is a post as bodyguard to the dwarf magister Vorondar Levelstone at the South Gate, and it has earned her the rank of captain in the City Guard. From there she watches the traffic through the gate and keeps it open for her associates. She has built his trust over about two years `[research]`, and in the past year she has been developing sources inside Manshoon's cell. She briefs in few words and expects the listener to infer the rest."
> — `campaign/setting/organizations/06-doom-raiders.md:114`

**Campaign, Code, Legal and Magisters (the same cover)**
> "**Tashlyn Yafeera** (Lawful Evil, Calishite Human, she/her) is the Master of Arms and Mercenaries for the Doom Raiders, and her cover is a post as bodyguard to the dwarf magister Vorondar Levelstone at the South Gate. The cover has earned her the rank of captain in the City Guard, from which she watches the traffic through the gate and keeps it open for her associates."
> — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:47`

### A4. How she rose in the cell

**Campaign, Organization page, Ranks and titles**
> "- **Ranks and titles:** The Masters' titles are the cell's only sourced ranks. Davil is the leader, as the wiki infobox and the published adventure agree (Forgotten Realms Wiki, *Doom Raiders*, 5e), and Tashlyn speaks for the cell when he is away. The ranks that members earn are a game rule and live in the Factions Guide."
> — `campaign/setting/organizations/06-doom-raiders.md:63`

**Campaign, Organization page, Key Members (the standing when Davil is away)**
> "- **Tashlyn Yafeera** — Master of Arms and Mercenaries; second voice of the cell when Davil is unavailable. See the **Tashlyn Yafeera** page in Notable Figures."
> — `campaign/setting/organizations/06-doom-raiders.md:100`

**Campaign, Organization page, Structure (the secondary contact)**
> "**Secondary Contact:** Tashlyn Yafeera — speaks for the cell whenever Davil is unavailable. She has sharper intelligence on Manshoon's faction than Davil and relies on it when she acts for the cell."
> — `campaign/setting/organizations/06-doom-raiders.md:51`

**Campaign, Organization page, Structure (the primary contact)**
> "**Primary Contact:** Davil Starsong — a sun elf retired adventurer who leads the Doom Raiders' Waterdeep operation. Charming, direct, and genuinely invested in ending the street violence Manshoon's cell has caused. Tashlyn Yafeera handles the cell's business whenever Davil is unavailable."
> — `campaign/setting/organizations/06-doom-raiders.md:49`

**Campaign, Davil's page (her colleague)**
> "**Relationships.** Davil is the cell leader of the Doom Raiders (Waterdeep Zhentarim), the faction contact for Zhentarim-aligned PCs, a permanent resident at the Yawning Portal (second floor business room, third floor suite), a colleague of Istrid, Tashlyn, Ziraj, and the traitor Skeemo Weirdbottle, and the unknowing target of Nihiloor's intellect devourer, with Meloon watching him and waiting for a clean opportunity to kill him without witnesses."
> — `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:25`

**Adventure, the five leaders (the Zhentarim section)**
> "The Doom Raiders (described in appendix B) consider themselves the true Zhentarim of Waterdeep. The group's leaders are {@creature Davil Starsong|WDH} (Master of Opportunities and Negotiations), {@creature Istrid Horn|WDH} (Master of Trade and Coin), {@creature Skeemo Weirdbottle|WDH} (Master of Magic), {@creature Tashlyn Yafeera|WDH} (Master of Arms and Mercenaries), and {@creature Ziraj the Hunter|WDH} (Master of Assassination)."
> — `sources/adventure-wdh.json:1447`

**Adventure, Zhentarim support (what she offers the party)**
> "Tashlyn offers affordable mercenaries, either {@creature thug||thugs} costing 2 sp per day each or {@creature veteran||veterans} costing 2 gp per day each."
> — `sources/adventure-wdh.json:1454`

**Adventure, Davil's introductions (the Davil entry, page 198)**
> "Davil can put the characters in contact with other leaders of the Black Network's Waterdeep division, namely {@creature Istrid Horn|WDH} (if they need a loan), {@creature Skeemo Weirdbottle|WDH} (if they need magic), {@creature Tashlyn Yafeera|WDH} (if they need weapons or mercenaries), and {@creature Ziraj the Hunter|WDH} (if they need a highly skilled assassin)."
> — `sources/adventure-wdh.json:31925`

### A5. Faith, signature belongings, relationships to other named figures

No source gives Tashlyn a faith, a deity or a signature belonging. The Doom Raiders' rites are in `campaign/setting/organizations/06-doom-raiders.md:43` and belong to Istrid, not Tashlyn. Her relationships to named figures are quoted in A4 and in Connections on the page.

**Campaign, Organization page, Beliefs (the group's loyalty; Ziraj's part is in his notes)**
> "- **The Network Looks After Its Own:** A member of the cell is one of theirs. When something goes wrong the faction does what it can, and it expects the same loyalty in return. Anyone who betrays or harms Istrid Horn finds her former adventuring companions using every resource they have to ruin them. The loyalty is personal as well as institutional. Yagra will reach a threatened friend's door at 2 AM in full armor, and Ziraj taught her the trail marks he leaves when he is wounded (**Yagra Stonefist**; **Ziraj the Hunter**)."
> — `campaign/setting/organizations/06-doom-raiders.md:37` (a group sentence; the person-level part is Ziraj's)

### A6. Time in post

**Campaign, Organization page, GM Notes**
> "She has built his trust over about two years `[research]`, and in the past year she has been developing sources inside Manshoon's cell." — `campaign/setting/organizations/06-doom-raiders.md:114` (quoted in A3 in full)

No other source gives a duration. The adventure gives none (`sources/adventure-wdh.json:31955`). The history file repeats the figure with a source note:
> "- Tashlyn serves as Captain of the City Guard at the South Gate under the dwarf magister Vorondar Levelstone. She has earned his confidence over two years, according to the Doom Raiders organization page, and the published adventure gives no duration."
> — `campaign/setting/history/04-the-founding-of-chains.md:58`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Calishite human fighter, lawful evil, she/her*. Stat block: **Swashbuckler**." — `campaign/setting/notable-figures/doom-raiders/05-tashlyn-yafeera.md:5`
- Campaign, quest tags (all say the same): "> Tashlyn Yafeera (Lawful Evil, Calishite Human, she/her) :: the Doom Raiders' Master of Arms and Mercenaries, running the cell while Davil is held." — `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:44`
- Campaign, first-meeting note: "A flying snake reaches each new member at dawn with a note from Tashlyn Yafeera (Lawful Evil, Calishite Human, she/her)." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:368`
- Campaign, Watch page: "**Tashlyn Yafeera** (Lawful Evil, Calishite Human, she/her) is the Doom Raiders' Master of Arms and Mercenaries." — `campaign/setting/governance-and-guilds/city-watch.md:69`
- Wiki: "| alignment5e    = [[Neutral]]" — wiki line 57 (5e). The other alignment fields are blank (wiki lines 40, 43, 46, 50, 54).
- Adventure: no alignment line in the Tashlyn entry (`sources/adventure-wdh.json:31950-31956`) or in the Zhentarim section (`:1443-1456`).

**Species and ethnicity**
- Campaign: "Calishite human" (Summary, `05-tashlyn-yafeera.md:5`); "Calishite Human" (quest tags above).
- Wiki: "| race           = [[Human]]<ref name="WDH-199-200" />" — wiki line 14 (5e). "| ethnicity      = " is blank (wiki line 15).
- Adventure: "Born to a well-off family in Calimshan" (`sources/adventure-wdh.json:31956`). No species word.
- Note for the drafter: the page's "Calishite" describes a person from Calimshan. The adventure and the wiki both place her origin in Calimshan (wiki line 12: "| formerhomes    = [[Calimshan]]").

**Pronouns**
- Campaign: "she/her" (Summary, `05-tashlyn-yafeera.md:5`; quest tags above).
- Adventure: "Quick to anger, she hates to back down from a fight." (`sources/adventure-wdh.json:31956`).
- Wiki: "| sex            = Female<ref name="WDH-199-200" />" — wiki line 13.

**Stat block**
- Campaign, Summary: "Stat block: **Swashbuckler**." (`05-tashlyn-yafeera.md:5`). No other campaign file names a stat block for Tashlyn. Searched: Grep for Tashlyn near Swashbuckler, Veteran, Spy, Fighter, Commoner, Guard, stat block or Hit Points across the repository (no such hit on Tashlyn).
- Adventure: no CR, AC, HP or block name in `sources/adventure-wdh.json:31950-31956`.
- Appendix B: no stat line in `sources/Appendix_B_-_Player_Factions.md:532`.
- Wiki: "| challenge5e    = 9" — wiki line 58 (5e); "| refs5e         = <ref name="WDH-199-200">..." — wiki line 60. "[[Category:Fighters]]" — wiki line 92.
- Stat-block label "Swashbuckler" for another Doom Raider: Davil is "Swashbuckler (with modifications)" (`campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:5`).

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/doom-raiders/05-tashlyn-yafeera.md`. The page has no Background section yet. Each row gives the exact sentence, the reason it is quest-time, and where the fact already lives.

| # | Line | Sentence (exact) | Why quest-time | Where it already lives |
|---|---|---|---|---|
| 1 | L7 | "**Featured in:** **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **Doom Raiders Mission 3 — The Missing Snobeedle**, **Doom Raiders Mission 4 — Silencing Skeemo**, **Doom Raiders Mission 5 — The Yellowspire Job**" | Quest names only (routed) | `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/`, `m04-silencing-skeemo/`, `m05-the-yellowspire-job/`; Factions Guide `campaign/guides/factions/07-doom-raiders.md:68-70` |
| 2 | L11 | "**Resonance.** Tashlyn should inspire respect for her martial competence, irritation with her unfettered superiority, and grudging trust when she takes over as faction contact with more efficiency and fewer words than Davil." | "when she takes over as faction contact" is the handover after Davil's arrest | `sources/adventure-wdh.json:4028` (page 40): "The characters continue to receive missions, but they come from {@creature Tashlyn Yafeera|WDH} (see {@adventure appendix B|WDH|12})."; `campaign/guides/factions/07-doom-raiders.md:30` ("Tashlyn takes over."); `campaign/setting/organizations/06-doom-raiders.md:187` (routed) |
| 3 | L15 | "**Motivations.** Tashlyn wants to keep the Doom Raiders armed, trained, and operational after Davil's arrest, prove that she is the stronger leader, and best anyone foolish enough to challenge her." | "after Davil's arrest" | Same as row 2. `campaign/setting/organizations/06-doom-raiders.md:187` says: "Tashlyn's Notable Figures Motivations line ("after Davil's arrest") is not used." |
| 4 | L25 | "**Relationships.** Tashlyn is the Doom Raiders' Master of Arms and Mercenaries, Davil's replacement as faction contact after his arrest, and a leader who communicates exclusively by flying snake, using fewer words and expecting more inference." | "Davil's replacement as faction contact after his arrest" (the arrest); "communicates exclusively by flying snake" is a delivery mechanic | `sources/Appendix_B_-_Player_Factions.md:532`: "**Secondary Contact: Tashlyn Yafeera.** Takes over mission briefings after Davil's arrest, communicating via flying snake. She has sharper intelligence on Manshoon's faction than Davil did, and her assignments reflect it."; `campaign/guides/factions/07-doom-raiders.md:37` (the flying snake in First Meeting); `campaign/setting/organizations/06-doom-raiders.md:170` (the flying-snake bullet moved to the Factions Guide) |
| 5 | Voice L88 | "- **Quirks:** Her flying-snake messages are two or three words long. She finishes other people's explanations for them when they're too slow. She never sits during a briefing." | Delivery mechanic (flying snake is the cell's quest-brief method) | `campaign/setting/organizations/06-doom-raiders.md:170` (routed) |
| 6 | Voice L90 | "- **Never:** She never pleads, never praises lavishly, and never admits she misses Davil." | Presumes Davil is gone | `sources/adventure-wdh.json:4028`; `campaign/guides/factions/07-doom-raiders.md:73` |
| 7 | Voice L92 | "  - *Greeting:* \"You're late. Davil's gone. You report to me now.\"" | "Davil's gone" is the arrest | `sources/adventure-wdh.json:4028`; `campaign/guides/factions/07-doom-raiders.md:73` |
| 8 | Voice L87 | "- **Personality in speech:** Unfettered superiority. She states her own excellence as a fact. Quick temper shows in how much shorter she gets. Grudging respect for anyone who beats her comes out as one clipped word (\"Adequate.\") that she means as high praise." | Day-one. Listed for completeness | n/a |

Quest-time clauses in the voice profile: rows 5 to 7. The other lines of the Tashlyn profile (`.claude/skills/character-voices/voices/doom-raiders.md:81` to `:94`, except the three rows above) are day-one. Row 5 is a delivery mechanic and row 6 implies a quest state. Ruling 16 says these get a day-one restatement and the skill's profile changes to match.

The arrest and the handover are quest content. The Factions Guide routes them: "**Two days after Gralhund Villa, the City Watch arrests Davil and holds him at Castle Waterdeep pending questioning about the Zhentarim's role in the street violence.** Contact passes to Tashlyn Yafeera during his detention; see the [**Davil's Arrest**](../../quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md) Event." — `campaign/guides/factions/07-doom-raiders.md:73`

Quest-time sentence in the wiki (not on the current page, listed for awareness): wiki line 75, second sentence: "After [[Davil Starsong]] and other Zhents were captured by the [[City Watch (Waterdeep)|City Watch]] later that year, following the [[Gralhund Villa Bloodbath]], Tashlyn temporarily stepped in as the leader of the Waterdhavian cell of the Zhentarim." (edition 5e). Lives in the Gralhund Villa and Davil's arrest events.

---

## D. Conflicts

**D1. Alignment (page and quest tags versus wiki)**
- Page: "> - *Calishite human fighter, lawful evil, she/her*. Stat block: **Swashbuckler**." — `campaign/setting/notable-figures/doom-raiders/05-tashlyn-yafeera.md:5`
- Quest tags: "Tashlyn Yafeera (Lawful Evil, Calishite Human, she/her)" — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:368`; `campaign/setting/governance-and-guilds/city-watch.md:69`; `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:47`.
- Wiki: "| alignment5e    = [[Neutral]]" — wiki line 57.
- Higher rank: campaign (page, quest tags, Watch and Code pages agree). Wiki is last. The page stays "lawful evil".

**D2. Stat block (page versus no source)**
- Page: "Stat block: **Swashbuckler**." — `05-tashlyn-yafeera.md:5`
- Adventure: no block name (`sources/adventure-wdh.json:31950-31956`).
- Wiki: "| challenge5e    = 9" — wiki line 58. The wiki gives a CR and no block name.
- Higher rank: none gives a stat block. The label has no source in any file; the drafter should treat it as unsourced. The CR 9 is a wiki-only claim.

**D3. Her post: bodyguard with an earned captaincy, or captain**
- Adventure (the published order): "Tashlyn has established a useful cover by serving as a bodyguard to Vorondar Levelstone, a dwarf magister stationed at the South Gate. She likes the dwarf and has earned his confidence, allowing her to reach the rank of captain in the City Guard. In that position, she watches over traffic that passes through the gate-and ensures that her associates in the Black Network can come and go freely." — `sources/adventure-wdh.json:31955`
- Watch page: "She holds the rank of captain in the City Guard as cover and watches the traffic through the South Gate." — `campaign/setting/governance-and-guilds/city-watch.md:69`
- History: "- Tashlyn serves as Captain of the City Guard at the South Gate under the dwarf magister Vorondar Levelstone." — `campaign/setting/history/04-the-founding-of-chains.md:58`
- Event: "> Tashlyn Yafeera (Lawful Evil, Calishite Human, she/her) :: the Doom Raiders' Master of Arms and Mercenaries, a City Guard captain under the dwarf magister Vorondar Levelstone, and terse to the point of rudeness." — `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:107`
- Event: "She has come off the night watch and is still wearing the grey coat of a City Guard captain." — `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/ev-01-the-approach.md:22`
- Factions Guide: "- Tashlyn's City Guard position provides one piece of actionable Splinter intelligence per tenday at Renown 3+." — `campaign/guides/factions/07-doom-raiders.md:15`
- Organization page, Structure: "- **The Open Lord's Watch (wary rival):** The Watch keeps a file on the cell, and Tashlyn holds the rank of captain in the City Guard through her bodyguard post (**The Open Lord's Watch**; **The City Watch**). Captain Staget reasons that if Xanathar's Guild and the Zhentarim want to destroy each other, the Watch may as well let them (*Dragon Heist*, 5e)." — `campaign/setting/organizations/06-doom-raiders.md:91`
- Organization page, settled: "> - **Settled:** Tashlyn's role follows her Notable Figures page (ruling 18): bodyguard to a dwarf magister at the South Gate. The old Summary called her \"Captain of the City Guard\". The published adventure (`adventure-wdh.json` line 31955) and `code-legal-and-magisters.md` line 47 make the captaincy a rank her bodyguard cover earned, and the GM Notes say so." — `campaign/setting/organizations/06-doom-raiders.md:165`
- Open Lord's Watch page, Draft Notes: "> - **Conflicts:** Tashlyn's cover. `city-watch.md:69` says \"She holds the rank of captain in the City Guard as cover\", and her Notable Figures page says \"a Calishite bodyguard to a dwarf magistrate at the South Gate\" (`05-tashlyn-yafeera.md:21`). `organizations/06-doom-raiders.md:63` says the bodyguard post has earned her the rank. This page follows the Doom Raiders page and her Notable Figures page, and `city-watch.md:69` inverts the order. Not edited." — `campaign/setting/organizations/11-open-lords-watch.md:153`
- Higher rank: the adventure (`sources/adventure-wdh.json:31955`). The page's bodyguard wording (`05-tashlyn-yafeera.md:21`) matches it. `city-watch.md:69` and the history line invert the order and are stale (see E1).

**D4. Years of trust**
- Organization page: "She has built his trust over about two years `[research]`" — `campaign/setting/organizations/06-doom-raiders.md:114`
- History: "She has earned his confidence over two years, according to the Doom Raiders organization page, and the published adventure gives no duration." — `campaign/setting/history/04-the-founding-of-chains.md:58`
- Adventure: "She likes the dwarf and has earned his confidence" (`sources/adventure-wdh.json:31955`); no duration.
- Higher rank: none. The duration is `[research]` on the organization page. The history line cites the organization page, not a source.

**D5. Origin: "Calishite family" (page) and "Calimshan" (adventure, wiki)**
- Page: "she is born to a well-off Calishite family" — `05-tashlyn-yafeera.md:21`
- Adventure: "Born to a well-off family in Calimshan" — `sources/adventure-wdh.json:31956`
- Wiki: "| formerhomes    = [[Calimshan]]" — wiki line 12.
- Not a contradiction (Calishite describes a person from Calimshan). The drafter should use the adventure's place name.

**D6. Mission numbering**
- Page: "**Doom Raiders Mission 3 — The Missing Snobeedle**" — `05-tashlyn-yafeera.md:7`
- Factions Guide: "| 4th | **The Missing Snobeedle** | A wealthy halfling family offers 500 gp for information on their missing son Dasher." — `campaign/guides/factions/07-doom-raiders.md:68`. The guide's column is headed "Level", not mission number. Its last row is "| 7th | **Ziraj's Last Hunt** |" (`07-doom-raiders.md:71`).
- Quest folders: `m03-the-missing-snobeedle`, `m04-silencing-skeemo`, `m05-the-yellowspire-job`, `m06-zirajis-last-hunt`.
- Factions Guide, Davil's release: "Davil is released at the end of Mission 4, once the Lords conclude his cell isn't responsible for the recent killings" — `campaign/guides/factions/07-doom-raiders.md:73`. In the folder numbering Mission 4 is Silencing Skeemo; in the guide's level column it is "5th".
- Higher rank: the quest folders. The page's numbering matches them. The guide's numbering is not settled here.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/setting/governance-and-guilds/city-watch.md:69`: "**Tashlyn Yafeera** (Lawful Evil, Calishite Human, she/her) is the Doom Raiders' Master of Arms and Mercenaries. She holds the rank of captain in the City Guard as cover and watches the traffic through the South Gate." Inverts the adventure's order (D3).
- `campaign/setting/history/04-the-founding-of-chains.md:58`: "- Tashlyn serves as Captain of the City Guard at the South Gate under the dwarf magister Vorondar Levelstone." Drops the bodyguard cover (D3).
- `campaign/guides/factions/07-doom-raiders.md:15`: "- Tashlyn's City Guard position provides one piece of actionable Splinter intelligence per tenday at Renown 3+." Names the post, not the cover (D3).
- `campaign/guides/factions/07-doom-raiders.md:68-73`: mission numbering (D6).
- `docs/plans/doom-raiders-conversion-brief.md:220`: "  - Tashlyn is a City Guard captain under the dwarf magister Vorondar Levelstone at the South Gate." Stale against the adventure order (D3).

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**

Tashlyn's own quest appearances, by file (line counts from the Grep of `Tashlyn|Yafeera` in each folder):
- `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md` (7 lines)
- `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/overview.md:17`: "If Davil has been arrested on Ches 26 and the mission is still unplayed, Tashlyn Yafeera gives the brief instead."
- `campaign/quests/faction-events/doom-raiders/m02-the-poisoned-delivery/overview.md:17`: "If Davil has been arrested on Ches 26 and the mission is still unplayed, Tashlyn Yafeera sends the note instead."
- `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:17`: "At 17:00 Tashlyn Yafeera meets the eligible members in the wagon yard beside the South Gate, where a flying snake told them to come that morning. Davil is in Castle Waterdeep, the cell needs coin, and the Snobeedle family of the Undercliff has posted a reward of 500 gp for word of a missing son."
- `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:25`: "Tashlyn knows none of this. She sees five hundred gold that the Doom Raiders could use while Davil is away."
- `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md` (34 lines)
- `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/overview.md:17`: "At 06:00 a flying snake finds each eligible member and tells them to come to the wagon yard beside the South Gate. Tashlyn Yafeera is waiting beside the barrels in her Guard coat, and she tells them that Skeemo Weirdbottle has been selling the cell to the other Zhentarim, that he must die, and that it must look like an accident."
- `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/ev-01-the-approach.md` (28 lines), `ev-02-the-chase.md` (4), `ev-03-the-reckoning.md` (37), `overview.md` (13)
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/overview.md:22`: "Davil has been out of Castle Waterdeep for some time, and he asks the member to a private meeting at the Yawning Portal. On the first version, he wants the ledger that shows who carries a pass-amulet into the other cell's fortress, and Tashlyn wants a set of coded letters that name its strike-team coordinator. On the second version, he wants to hear what the party saw when it went in."
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md` (23 lines), `ev-02-the-debrief.md` (21), `overview.md` (7)
- `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md` (21), `r10-viper/ev-01-viper.md` (24), `r25-ardragon/ev-01-ardragon.md` (25), `r50-dread-lord/ev-01-dread-lord.md` (21)
- `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md` (32), `s02-davils-return/ev-01-davils-return.md` (30)
- `sources/adventure-wdh.json:4024-4035` (page 40; the handover and what Tashlyn has learned: "The rumored leader of the renegade Zhent faction is {@creature Urstul Floxin|wdh}, a known Black Network assassin.")
- `sources/Appendix_B_-_Player_Factions.md:532` (quest-time; the handover; see C row 4)
- `sources/Appendix_C_-_Player_Faction_Missions.md:1357`: "Tashlyn Yafeera sends the party to eliminate Skeemo Weirdbottle, who has been feeding information to Manshoon's cell. Skeemo has been warned, runs, and is very hard to catch."
- `sources/Appendix_C_-_Player_Faction_Missions.md:1365`: "A flying snake arrives at Trollskull Manor while Davil is still in Watch custody. The message is in Tashlyn's handwriting, precise and without decoration:"
- `sources/Appendix_C_-_Player_Faction_Missions.md:1410`: "Tashlyn, informed of the outcome, becomes substantively more respectful in her dealings with the party — the work she asked them to do is the hardest kind of work, and she knows it."

Date conflict on the arrest (routed; not for this page): `m01-the-dockside-killer/overview.md:17` says "Ches 26"; `campaign/setting/governance-and-guilds/city-watch.md:85` says "Davil Starsong is arrested two days after the villa, and the Watch cracks down on the Black Network." (its Ches date: "by the morning of Ches 25 it has sealed the villa and begun processing twenty-three bodies."). Not settled here.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth year, age, parents, siblings, family name, home district in Calimshan.** No source gives any of these. The adventure says only "Born to a well-off family in Calimshan" (`sources/adventure-wdh.json:31956`). The wiki's `age`, `dob`, `parents` and `siblings` fields are blank (wiki lines 17, 21, 29, 31). Do not give a birth year. A family name or a city in Calimshan is `[design]`; it must not be the Cassalanters (Cassalanter secrecy).

**F2. How she came to the Zhentarim.** Sources: "Tashlyn was once an adventurer but decided to join the Zhentarim with her fellow companions." (wiki line 73, 5e) and "They gave up adventuring to join the Black Network" (`sources/adventure-wdh.json:31916`). No reason is given. A reason is `[design]`.

**F3. Her fighting training.** The wiki's class fields are blank (wiki lines 40-56) and the category is "Fighters" (wiki line 92). The page says "fighter" (`05-tashlyn-yafeera.md:5`). No source names a class level or a fighting style. Keep "fighter" as the page's label.

**F4. How the cover began.** Sources: "She likes the dwarf and has earned his confidence" (`sources/adventure-wdh.json:31955`); "Despite her deception as his \"bodyguard\", Tashlyn genuinely respected her patron [[Vorondar Levelstone|Vorondar]]." (wiki line 70). No account of how the cover began. A start is `[design]`, and it must keep the trust of "about two years" (`06-doom-raiders.md:114`, `[research]`).

**F5. Her relationship with Davil.** Sources: "a colleague of Istrid, Tashlyn, Ziraj, and the traitor Skeemo Weirdbottle" (`01-davil-starsong.md:25`); "Tashlyn Yafeera handles the cell's business whenever Davil is unavailable." (`06-doom-raiders.md:49`). Nothing says how they came to work together. The voice profile says she "never admits she misses Davil" (`doom-raiders.md:90`). A shared past is `[design]` and must not contradict Davil's page.

**F6. Personal goals beyond the cell and the post.** The Motivations line (`05-tashlyn-yafeera.md:15`) is the only sourced want, and it contains the quest-time clause (C row 3). Its day-one part is "prove that she is the stronger leader, and best anyone foolish enough to challenge her." The Background's `**Personal goals.**` paragraph must be `[design]`. Limits: no Event Outcome, no quest result, no Grand Game balance, no new Notable Figure.

**F7. Her view of the rival cell.** Source: "in the past year she has been developing sources inside Manshoon's cell" (`06-doom-raiders.md:114`). No source says why. A reason is `[design]`.

**F8. Her Morale line.** The page's Morale (`05-tashlyn-yafeera.md:23`) is not in any source. The nearest sourced fact is "She respects anyone who can best her in melee combat." (`sources/adventure-wdh.json:31956`). The organization page repeats the fighting habit (`06-doom-raiders.md:74`: "Tashlyn closes distance and stays there, Ziraj fires from elevation and avoids melee"). Keep as the page's label.

**F9. Appearance.** No source gives appearance for Tashlyn. The wiki has an image file name (`Tashlyn.png`, wiki line 3) and no description.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "She likes the dwarf and has earned his confidence, allowing her to reach the rank of captain in the City Guard." — `sources/adventure-wdh.json:31955`. (Her regard for Vorondar.)
- "Despite her deception as his \"bodyguard\", Tashlyn genuinely respected her patron [[Vorondar Levelstone|Vorondar]]." — wiki line 70, 5e. (Respect, and the deception it sits beside.)
- "Born to a well-off family in Calimshan, Tashlyn has an unfettered sense of superiority. Quick to anger, she hates to back down from a fight. She respects anyone who can best her in melee combat." — `sources/adventure-wdh.json:31956`. (Pride; a grudge against backing down.)
- "Tashlyn came from a wealthy family that was well-known in the southern land of [[Calimshan]].<ref name="WDH-199-200" />" — wiki line 68, 5e. (A wealthy family she left; no name.)
- "- **Never:** She never pleads, never praises lavishly, and never admits she misses Davil." — `.claude/skills/character-voices/voices/doom-raiders.md:90`. (A loss she will not name. The drafter can use it as a feeling and must not state Davil's fate on Ches 1.)
- "in the past year she has been developing sources inside Manshoon's cell" — `campaign/setting/organizations/06-doom-raiders.md:114` (day-one; full sentence in A3). (Her long game against the rival cell.)
- "She has built his trust over about two years `[research]`" — `campaign/setting/organizations/06-doom-raiders.md:114` (`[research]`; full sentence in A3).
- "> Tashlyn Yafeera (Lawful Evil, Calishite Human, she/her) :: the Doom Raiders' Master of Arms and Mercenaries, who runs the cell's practical business and thinks it is run better without speeches." — `campaign/quests/faction-events/doom-raiders/r10-viper/ev-01-viper.md:46`. (Her view of speeches; a quest tag, not a Notable Figure fact.)
- "- **Personality in speech:** Unfettered superiority. She states her own excellence as a fact." — `.claude/skills/character-voices/voices/doom-raiders.md:87`. (Pride.)
- "She sees five hundred gold that the Doom Raiders could use while Davil is away." — `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:25`. QUEST-TIME. Listed only as a warning: it shows her money drive and sits in a mission.

---

## Cross-references (every other file where the topic appears)

Counts from Grep over `campaign/` (61 files, 503 lines). Non-quest lines are quoted or named. Quest-file lines are routed and given as counts above (E2).

Non-quest files and key lines:
- `campaign/setting/organizations/06-doom-raiders.md` (24 lines): lines 7, 9, 37, 49, 51, 60, 63, 74, 91, 100, 114, 165, 170, 177, 187, 189 (quoted in A and D; "Not the villain Zhentarim" is at line 9).
- `campaign/guides/factions/07-doom-raiders.md` (10): lines 15, 30, 31, 32, 33, 37, 68-71, 73 (quoted in C and D).
- `campaign/setting/governance-and-guilds/city-watch.md` (4): line 69 (D3); line 85 "Tashlyn deals with a constable by showing the badge of a City Guard captain."
- `campaign/setting/governance-and-guilds/code-legal-and-magisters.md` (6): line 47 (A3)
- `campaign/setting/history/04-the-founding-of-chains.md` (5): line 54 "- Their leaders are Davil Starsong, Master of Opportunities and Negotiations; Istrid Horn, Master of Trade and Coin; Skeemo Weirdbottle, Master of Magic; Tashlyn Yafeera, Master of Arms and Mercenaries; and Ziraj the Hunter, Master of Assassination."; line 58 (D3)
- `campaign/setting/organizations/11-open-lords-watch.md` (3): line 69 "- **The Zhentarim (Doom Raiders) (wary rival):** The Watch keeps a file on Davil Starsong's cell, so his people avoid anything that invites scrutiny (**The Zhentarim (Doom Raiders)**). Tashlyn Yafeera has earned the rank of captain in the City Guard as bodyguard to a magister at the South Gate (**Tashlyn Yafeera**)."; line 153 (D3)
- `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md` (1): line 25 (A4)
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md` (2): not read in full
- `campaign/setting/deities/bane.md` (2), `campaign/setting/deities/yondalla.md` (2), `campaign/setting/geography/city-of-the-dead.md` (3), `campaign/setting/geography/dragonward-and-walking-statues.md` (1): not read in full
- `campaign/gazetteer/waterdeep/southern-ward.md` (2): line 20 places the South Gate on the ward boundary: "East, the Trollwall, with the southern inner gate to the Caravan Grounds and the South Gate beyond (wiki, circa 1372 DR)."
- `campaign/gazetteer/waterdeep/dock-ward.md` (line 22): the South Gate's place where the two wards met (the sentence "its South Gate page says the South Gate stood where the two wards met"). Not read in full.
- `campaign/guides/gm-guide/player-factions-overview.md` (1): not read in full
- `campaign/structure/arc-*.md` (superseded or pending conversion): `arc-c-fireball.md` (4), `arc-d-gralhund-villa.md` (9), `arc-e-faction-outposts.md` (5), `arc-f-xanathars-lair.md` (2), `arc-g-cassalanter-villa.md` (2), `arc-h-sea-maidens-faire.md` (2), `arc-i-kolat-towers.md` (8), `arc-j-vault-of-dragons.md` (2). Not read in full. Routed.
- `campaign/quests/act-ii/gralhund-villa/` (ev-09-aftermath.md 11; overview.md 2; ev-01-what-the-factions-say.md 1; flowchart.md 1; design-notes.md 1). Routed.
- `sources/adventure-wdh.json`: lines 321 (index list entry), 1447, 1454, 4024-4035 (page 40), 31925, 31950-31956 (page 199), 32975 (index "76. Tashlyn Yafeera"). Quoted in A and C.
- `sources/Appendix_B_-_Player_Factions.md`: lines 530, 532, 657-662 (renown rules; "Delivering a prisoner to Tashlyn earns the full renown"). Quoted in C.
- `sources/Appendix_C_-_Player_Faction_Missions.md`: lines 1355-1414 (the Silencing Skeemo mission; Tashlyn's briefs; routed, E2).
- `sources/Appendix_D_-_Running_the_Tavern.md`: no Tashlyn hit (Grep).
- `docs/plans/setting-compendium-research-notes/pass5/doom-raiders.md:335`: "**C3. Tashlyn's post: City Guard captain or bodyguard.**" (earlier research; not read in full).
- `sources/research/pass5-bundles/doom-raiders/wiki.txt`: no hit for Tashlyn, Yafeera, Ziraj or Senna (Grep).

Name collisions:
- "Nessa Thorne" (Doom Raiders assassin, r25) and "Nessa Vayle" (Harper, twin of Corvin, Trollskull server candidate): `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:137` ("Crew Two is the assassin Nessa Thorne (she/her) and the spies Garrick Pell and Bree Ostler."); `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58` ("| 5 | **Nessa & Corvin Vayle** | CN Illuskan human twins |"). The first name is shared; the surnames differ.
- "Vaelle Lurval" (Cassalanter cult florist, adventure) shares the "Vael" stem with "Senna Vael": `sources/adventure-wdh.json:8317` ("The survivor is Vaelle Lurval (LE female Tethyrian human {@creature cultist}), a 30-year-old Waterdavian florist.").
- Tashlyn shares no first or last name with any other named figure found.

---

## Not found

- Searched for: Tashlyn, Yafeera, "Master of Arms" and "Calimshan" in `campaign/` (Grep, 503 lines in 61 files), `sources/adventure-wdh.json` (Grep), `sources/Appendix_B/C/D` (Grep), `sources/research/` (Grep: the pass5 doom-raiders wiki.txt has no Tashlyn hit).
- Birth year, age, parents, siblings, family name, Calimshan home district: no match in any source (F1).
- Class and level: no match (F3).
- Stat block with a name for Tashlyn: no match in `campaign/`, `sources/adventure-wdh.json` (`:31950-31956`), or the Appendices (D2).
- Alignment in the adventure: no match in `:31950-31956` or `:1443-1456`.
- Faith or deity: no match (A5).
- Signature belonging: no match.
- Personal goals beyond the Motivations line: no match (F6).
- Appearance: no match in the adventure or the Alexandrian Appendices (F9).
- Wiki ethnicity: blank (wiki line 15).
- Shared name collisions: none found for Tashlyn or Yafeera.

## Not readable

- `sources/Other remix files/Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` (named in `campaign/setting/organizations/06-doom-raiders.md:193`): could not be opened by these tools. The organization page says it "was not used".
- `sources/3. Player Character Factions.pdf`: read as images (PDF pp.2-3). `pdftotext` check needed for the Zhentarim paragraph (PDF p.3, printed p.25): "The non-Manshoonian **Zhentarim** will see an enormous opportunity in the gold: Efforts are under way to reclaim and repair Zhentil Keep, and that money could be used to buy them a seat on the Zhentarim Council that's forming to do so." No Tashlyn text is in the Alexandrian PDF pages read.
- The wiki Tashlyn page is in the scratchpad extract; a second copy was not checked.
