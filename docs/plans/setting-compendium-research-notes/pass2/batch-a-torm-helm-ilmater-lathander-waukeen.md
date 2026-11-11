# Batch A research report: Torm, Helm, Ilmater, Lathander, Waukeen

## Method and notes

- Read first: `/home/user/waterdeep/docs/plans/setting-compendium-pass2-brief.md` lines 84 to 103 (the researcher-report fields), and `/home/user/waterdeep/campaign/setting/deities/asmodeus.md` in full (the approved model page).
- Read in full: the five bundles (`5etools.md`, `wiki.txt`, `campaign-hits.txt`, `adventure-hits.txt`) under `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/<power>/`. Each wiki was read in one pass (219 to 251 lines).
- Read: the "Major Temples of Waterdeep" table at `/home/user/waterdeep/sources/adventure-wdh.json` lines 30910 to 30997.
- Targeted Grep of `/home/user/waterdeep/campaign` and both adventure JSON files for every alias in the brief (for example "Loyal Fury", "Hand Resolute", "Watcher", "Crying God", "Morninglord", "Spires of the Morning", "Coinmaiden", "Golden Lady", "Goldeye", "Waukeentide", "Hospice", "Steadfast Shield", "Helm's Hall"), plus the wiki files.
- Not opened, per the brief's scope: the Alexandrian PDFs, `sources/SOURCE_GUIDE.md`, and the `.docx` files (none is in scope for these five powers).
- Wiki quotes keep their `[[ ]]` link markup and all `<ref>` and `{{ }}` markup exactly as written. Nothing was dropped from a wiki quote. Where a wiki line ends with an ellipsis, the ellipsis is not reproduced, and the quote says so.
- Tags such as `{@creature …}` in the JSON and 5etools files are left as written.
- Edition tags. 5etools headings name the book and page. FRHoF (Forgotten Realms: Heroes of Faerûn, p.99 to p.127) is the 2024-era canon. SCAG p.21 (2014) and PHB p.294 (2014) are the fallbacks the brief allows for alignment, domains and symbol. Wiki infobox lines carry an edition suffix (`5eR`, `5e`, `4e`, `3e`, `2e`, `1e`). Wiki prose cites refs by book title, which is quoted as written.
- Bundle gap. `waukeen/campaign-hits.txt` lists four campaign lines. My Grep found more, which are quoted under Waukeen. For Torm, Helm, Ilmater and Lathander, every campaign line my Grep returned was already in the bundle, apart from noise.
- Noise hits are counted under Not found.

---

## Answers

### Torm

**Q1. Temples or shrines in Waterdeep, and ward.**

- Campaign: the Chapel of the Steadfast Shield, a Torm chapel in the Dock Ward.
  > "The others are the Temple of Helm in the Castle Ward and the Chapel of the Steadfast Shield, a Torm chapel in the Dock Ward."
  > — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:201`
  > "**Chapel of the Steadfast Shield (Torm, Dock Ward)**"
  > — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:229`
- Dragon Heist "Major Temples of Waterdeep" table: no Torm row (see the Major Temples section below).
- Undermountain, not Waterdeep's wards: a Torm shrine keyed on Level 22.
  > "name": "22. Torm's Shrine",
  > — `/home/user/waterdeep/sources/adventure-wdmm.json:59193`
  > "name": "Level 22: Shadowdusk Hold",
  > — `/home/user/waterdeep/sources/adventure-wdmm.json:57184`

**Q2. Campaign NPC, faction or quest that uses Torm.**

- Order of the Gauntlet, which serves the Triad (Tyr, Torm, Ilmater).
  > "The adventure has no Order of the Gauntlet. The white gauntlet is Torm's symbol, and Torm is one of the Triad the Order serves."
  > — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r50-righteous-hand/ev-01-righteous-hand.md:312`
- The Chapel's almoner, in the Marcheon briefing list.
  > "3. A charity whose books do not close, which a Torm almoner asked about and was refused."
  > — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:233`
- Undermountain, Level 21 and Level 22: Fazrian (a former planetar of Torm) and the Shadowdusk paladins.
  > "> - **Level 21:** Fazrian, once a planetar of Torm, is corrupted. A character it judges innocent can ask it to judge itself with a **DC 26 Charisma (Persuasion)** check."
  > — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r50-righteous-hand/ev-01-righteous-hand.md:309`
  > "> - **Level 22:** Dezmyr and Zalthar Shadowdusk, former paladins of Torm, are now death knights. A shrine of Torm with a white gauntlet fresco stands in the hold."
  > — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r50-righteous-hand/ev-01-righteous-hand.md:310`

**Q3. Lines in `torm/wiki.txt` that mention Waterdeep.**

One line, and it is a novel-appearance list only.
> "| novels              = ''[[Tantras (novel)|Tantras]]'';''[[Waterdeep (novel)|Waterdeep]]'';''[[Prince of Lies (novel)|Prince of Lies]]'';''[[Crucible: The Trial of Cyric the Mad]]''"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:229`

### Helm

**Q1. Temples or shrines in Waterdeep, and ward.**

- Dragon Heist table: Helm's Hall, Southern Ward (table rows quoted under Major Temples).
- Campaign: Temple of Helm, Castle Ward.
  > "**Temple of Helm (Castle Ward)**"
  > — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:222`
- The two disagree on the ward. The campaign gazetteer names the conflict itself.
  > "> - **Conflicts:** Temple of Helm. `player-factions-overview.md` (line 99) places it in the Castle Ward; the Dragon Heist temple table places Helm's Hall in the Southern Ward."
  > — `/home/user/waterdeep/campaign/gazetteer/waterdeep/castle-ward.md:272`

**Q2. Campaign NPC, faction or quest that uses Helm.**

- Order of the Gauntlet: its three temples, one of them the Temple of Helm.
  > "The three temples are the Halls of Justice, which is the temple of Tyr, the Temple of Helm in the Castle Ward, and the Chapel of the Steadfast Shield, a Torm chapel in the Dock Ward."
  > — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:192`
- Spined Devils in Twelvedog Court (m04): the injured resident is taken to the Temple of Helm.
  > "A resident who was hurt is carried to the Temple of Helm, whose healers treat the Watch's poor for free."
  > — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/ev-01-twelvedog-court.md:185`
- The Tithe (s01): the Temple of Helm runs a hospice wing.
  > "> - **Temple of Helm, Castle Ward.** Helm's priests run a hospice wing for Watch veterans and their families, and the donation goes to the healing work."
  > — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/s01-the-tithe/ev-01-the-tithe.md:97`

**Q3. Lines in `helm/wiki.txt` that mention Waterdeep.**

- Line 118 is a quote attributed to Helm, cited to "Waterdeep (adventure)" p.40. The line ends with an ellipsis, which is not reproduced here.
  > "|I guard this path! Do not approach. This way is forbidden"
  > — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:118`
- Line 197 is a novel-appearance list.
  > "| novels = ''[[Shadowdale (novel)|Shadowdale]]'';''[[Waterdeep (novel)|Waterdeep]]'';''[[The Sentinel]]''"
  > — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:197`

### Ilmater

**Q1. Temples or shrines in Waterdeep, and ward.**

- Dragon Heist table: Hospice of St. Laupsenn, North Ward (table rows quoted under Major Temples).
- The adventure text names the same hospice.
  > "The only person with whom she's civil is Vhaspar Holmdreg (LG male Illuskan human {@creature priest}), who rents a room in the west wing of the residence and works in the North Ward at the Hospice of St. Laupsenn, a temple of Ilmater, god of suffering."
  > — `/home/user/waterdeep/sources/adventure-wdh.json:13267`
- Campaign: no file names the Hospice of St. Laupsenn (a Grep for "Hospice" and "Laupsenn" returned no campaign hit). No campaign file names an Ilmater temple in Waterdeep.

**Q2. Campaign NPC, faction or quest that uses Ilmater.**

- Brother Aldric, a Trollskull Manor staff cook who belongs to the Order of Ilmater and is on sabbatical (full row quoted under Field 6).
- Name collision: a different person, Vhaspar Coldwater, appears in the campaign. He is not the Ilmater priest in the adventure (see Conflicts).

**Q3. Lines in `ilmater/wiki.txt` that mention Waterdeep.**

None. A Grep for "Waterdeep", "Waterdhav" and every Waterdeep ward name returned no line in `ilmater/wiki.txt`.

### Lathander

**Q1. Temples or shrines in Waterdeep, and ward.**

- Spires of the Morning, Castle Ward. Dragon Heist table (row quoted under Major Temples), and the adventure text.
  > "The glorious Spires of the Morning, dedicated to Lathander, is one of Waterdeep's most beautiful temples."
  > — `/home/user/waterdeep/sources/adventure-wdh.json:31015`
  > "It encompasses the City Navy's docks in the Great Harbor and all of Mount Waterdeep, and it is home to six walking statues, numerous temples, and many other landmarks."
  > — `/home/user/waterdeep/sources/adventure-wdh.json:31007` (this sentence places Mount Waterdeep inside the Castle Ward)
- Campaign gazetteer.
  > "- Temples of the ward: the Temple of the Seldarine for all elven gods, the Spires of the Morning for Lathander, one of the city's most beautiful temples, the Font of Knowledge for Oghma, with the library, and the Halls of Justice for Tyr (see Landmarks)."
  > — `/home/user/waterdeep/campaign/gazetteer/waterdeep/castle-ward.md:164`
- Undermountain sources also place the Spires in the Castle Ward.
  > "Two daggers stuck in the map mark the Spires of the Morning (the temple of Lathander in the Castle Ward) and the House of the Moon (the temple of Selûne in the Sea Ward)."
  > — `/home/user/waterdeep/sources/adventure-wdmm.json:50537`

**Q2. Campaign NPC, faction or quest that uses Lathander.**

- Victoro Cassalanter, whose public cover is worship of Lathander.
  > "Victoro is publicly a worshipper of Lathander, and the family is publicly known for its ancestral devotion to Siamorphe. The family is known for charity, and none of that warmth is faked."
  > — `/home/user/waterdeep/campaign/setting/deities/asmodeus.md:81`
- Brimel (Bregan D'aerthe m05) says "Lathander keep me" when he is afraid.
  > "He says "Lathander keep me" when he is afraid, which is often."
  > — `/home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:343`
- Rhyestertide (Finding Floon's opening date).
  > "| Ches 1 | The campaign opens at the Yawning Portal | **Finding Floon** | Rhyestertide, a Lathander holiday, falls the same day |"
  > — `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:60`

**Q3. Lines in `lathander/wiki.txt` that mention Waterdeep.**

- Line 159, the Spires of the Morning.
  > "* [[Spires of the Morning]]: A grand temple to Lathander in [[Waterdeep]] at the northern spur of [[Mount Waterdeep]].<ref name="CoS.W-p98">{{Cite book/City of Splendors: Waterdeep|98}}</ref>"
  > — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:159`
- Line 187, the 1345 DR unrest.
  > "In [[1345 DR]], Lathander's worshipers, along with those of [[Selûne]], [[Shar]], and [[Tempus]] were involved in religious unrest, culminating in the [[Night of Temple Fires]].<ref name="CoS.W-p11">{{Cite book/City of Splendors: Waterdeep|11}}</ref>"
  > — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:187`
- Line 162 mentions the "Heroes of Waterdeep", a party, not the city. The sentence is "In [[1358 DR]], the [[Heroes of Waterdeep]] came to liberate the temple from the [[Dark God]]." (Myth Drannor, not a Waterdeep site.)

### Waukeen

**Q1. Temples or shrines in Waterdeep, and ward.**

None in any file. The wiki's temple sentence names no Waterdeep site.
> "Ornate temples to the glory of the Golden Lady were usually found in centers of commerce from [[Tashalar]] in the south, up through [[Amn]], all around the [[Sea of Fallen Stars]] ([[Chessenta]], [[Cormyr]], [[Sembia]], [[the Vast]], [[Impiltur]]) and over to [[Thesk]] on the [[Golden Way]].<ref name="FRCS3e-23">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|23}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/wiki.txt:173`

**Q2. Campaign NPC, faction or quest that uses Waukeen.**

- No campaign NPC or faction is a Waukeen worshipper. The campaign uses the name through the Waukeentide festival and the Cassalanters' favored-deity line.
  > "The wiki lists Waukeen, Siamorphe and Asmodeus as the house's favored deities."
  > — `/home/user/waterdeep/campaign/setting/organizations/10-cassalanters.md:63`
  > "> - **Conflicts:** Public cover. The wiki lists Waukeen, Siamorphe and Asmodeus as favored deities. The campaign's public cover is Lathander for Victoro and Siamorphe for the house, which matches *Dragon Heist*, and the page keeps it."
  > — `/home/user/waterdeep/campaign/setting/organizations/10-cassalanters.md:120`
- The adventure's Waukeen priest, Obaya Uday, is not a campaign NPC (a Grep for "Obaya" in `/home/user/waterdeep/campaign` returned no hit).
  > "{@i NG female Chultan human priest of Waukeen}"
  > — `/home/user/waterdeep/sources/adventure-wdh.json:1557`

**Q3. Lines in `waukeen/wiki.txt` that mention Waterdeep.**

None. A Grep for "Waterdeep", "Waterdhav", "Dock Ward", "Castle Ward", "Sea Ward", "Southern Ward" and "North Ward" returned no line in `waukeen/wiki.txt`.

---

## Per-power fields

### Torm

**Field 1. Identity**

> "- altNames: ['The Hand of Righteousness', 'The Loyal Fury', 'Torm the True']"
> "- title: God of courage and self-sacrifice"
> "- plane: Mount Celestia (Mercuria)"
> "- worshipers: Guardians, knights, Paladins"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:2`, `:3`, `:5`, `:4` (FRHoF p.125)

> "- alignment: ['L', 'G']"
> "- domains: ['War']"
> "- symbol: White right gauntlet"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:27`, `:28`, `:29` (SCAG p.21, 2014; fallback per brief)

> "| alignment5e         = [[Lawful Good]]"
> "| symbol5e            = White right gauntlet"
> "| domains5e           = [[War domain|War]]"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:59`, `:60`, `:66` (wiki 5e infobox)

**Field 2. Edict or core tenet**

> "Those who favor Torm believe salvation is found through service."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:7` (FRHoF p.125)

> "Torm's faithful believe that brave acts of service please their god. They strive to maintain peace and order while opposing unjust laws and standing alert against corruption."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:9` (FRHoF p.125)

> "Those who take Torm to heart must strive to fulfill his commandment to go out into the world and be an active force for good, to right wrongs, and to help the hopeless. They must strive to maintain peace and order while opposing unjust laws."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:31` (SCAG p.21, 2014)

> "Torm required the following:<ref name="FRPG-p153" />"
> "* Respect and enforce the law, and honor your traditions.<ref name="FRPG-p153" />"
> "* Demonstrate truthfulness, loyalty, and steadfast devotion to a rightful cause.<ref name="FRPG-p153" />"
> "* Do not flinch in the execution of your duty, no matter what the consequence.<ref name="FRPG-p153" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:194` (the lead-in) and `:195` to `:197` (ref FRPG-p153, which the wiki's 4e block cites as Forgotten Realms Player's Guide p.158)

**Field 3. Portfolio and Areas of Concern**

> "He is a god of courage and self-sacrifice, an unyielding deity who dutifully puts himself on the front line of the fight against evil and injustice."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:7` (FRHoF p.125)

> "| portfolio           = Duty<br />Loyalty<br />Obedience<br />Courage<br />Self-sacrifice"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:29` (unlabelled infobox)

> "| portfolio5eR        = Courage, self-sacrifice"
> "| portfolio5e         = Courage, self-sacrifice, duty, loyalty"
> "| portfolio3e         = Duty, loyalty, obedience, [[paladin]]s"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:50`, `:65`, `:94`

Areas of Concern: not found for Torm. Neither 5etools nor the wiki lists them.

**Field 4. Worship (Waterdeep first)**

Waterdeep: no Torm worship in Waterdeep except the Dock Ward chapel (Answers Q1). Torm's temples in the sources are fortresses.

> "Followers construct fortress-temples dedicated to Torm on defensible heights. These structures offer drilling grounds, stables, and austere quarters for residents and visiting knights."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:10` (FRHoF p.125)

> "Most temples dedicated to Torm are fortresses built on heights."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:32` (SCAG p.21, 2014)

> "* [[Order of the Golden Lion]]: High Cleric [[Barriltar Bhandraddon]] served as Torm's pontiff and ruled from the [[Temple of Torm's Coming]] in [[Tantras]]."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:200` (wiki; the edition is not tagged in the sentence)

Messengers and omens:

> "When Torm appears in dreams, he takes the form of an enormous, flying metal gauntlet surrounded by arcs of lightning. He might send a golden {@creature Lion|XMM} or, in extreme cases, a {@creature Deva|XMM} clad in gleaming armor to make his will known."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:8` (FRHoF p.125)

Clergy:

> "Known as Tormtar, Torm's worshipers consisted mainly of humans who favored the causes of both good and law."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:190`

Holy days:

> "| holy days           =The Divine Death; The True Resurrection; [[Shieldmeet]] "
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:35` (infobox, no edition tag)

**Field 5. Relations with other powers, and origin (wiki edition tags as written)**

> "Chosen of Torm dedicate themselves to the fight against evil, especially against the forces of Bane. Torm and Bane battled each other to their mutual destruction during the Time of Troubles—both gods have since returned, and the animosity between them still seethes."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:11` (FRHoF p.125)

> "Torm greatly revered [[Tyr]], seeing him as his spiritual father.<ref name="DR381-p92"/> He was also a staunch ally of [[Ilmater]].<ref name="F&P-p74" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:164` (refs: Dragon 381 p.92; Faiths and Pantheons p.74)

> "Torm had a friendship with [[Helm]] prior to the latter's death in 1384 DR, though the two deities' priesthoods were cold to one another.<ref name="F&P-p74" /><ref name="DR381-p91">{{Cite dragon/381/Channel Divinity: Champions of Torm|91}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:166` (refs: Faiths and Pantheons p.74; Dragon 381 p.91)

> "Torm had many enemies amongst the foul deities, chief among them [[Bane]] and [[Shar]]. He held especial enmity for [[Cyric]], as he saw how the dark god had greatly damaged Tyr.<ref name="DR381-p92"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:174` (ref: Dragon 381 p.92)

> "After the death of Tyr, Torm became the new leader of the Triad when he took the seat of the master of [[Celestia]]. In this "new" Triad, Bahamut took the role of the god of justice in place of Tyr, while Ilmater became the god of mercy, and Torm the god of law, acting as a point of balance between the other two gods.<ref name="DR381-p92">{{Cite dragon/381/Channel Divinity: Champions of Torm|92}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:180` (ref: Dragon 381 p.92)

> "The origins of Torm were a mystery, although it was known he was once a mortal hero during the time of the fall of [[Netheril]], who eventually became a [[demigod]]. Many scholars believed that the mortal Torm lived in a nation on the [[Border Kingdoms]] known as [[Chalsembyr]].<ref name="F&P-p74" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:205` (ref: Faiths and Pantheons p.74)

**Field 6. Campaign and published-adventure mentions (first six; the rest are under Cross-references)**

> "The three temples are the Halls of Justice, which is the temple of Tyr, the Temple of Helm in the Castle Ward, and the Chapel of the Steadfast Shield, a Torm chapel in the Dock Ward."
> — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:192`

> "- **Contact:** the member names Savra to the door-warden of one of the three temples. At the Halls of Justice the door-warden is Brother Haldric Wence. The others are the Temple of Helm in the Castle Ward and the Chapel of the Steadfast Shield, a Torm chapel in the Dock Ward."
> — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:201`

> "4. Known fiendish signs in general: animals that will not enter a house, and a sleeper who talks in a language he does not know. The priest gives this one only to a member who has been through **Spined Devils in Twelvedog Court**. Before that, the chapel repeats the first three."
> — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:234`

> "Any non-evil character can join the Order of the Gauntlet in Waterdeep. Clerics, monks, and paladins are especially welcome, particularly if they worship Helm, Torm, or Tyr."
> — `/home/user/waterdeep/sources/adventure-wdh.json:1403`

> "{@creature Fazrian|WDMM} is a planetar formerly in the service of Torm, god of courage and self-sacrifice. The planetar was summoned to Undermountain months ago by an adventuring cleric."
> — `/home/user/waterdeep/sources/adventure-wdmm.json:54887`

> "These former paladins of Torm abandoned their faith long ago, becoming death knights."
> — `/home/user/waterdeep/sources/adventure-wdmm.json:57214`

> "{@b Altar and Fresco}. Three steps ascend to an alcove holding a stone altar. The wall behind the altar bears a fresco of a large white gauntlet (the symbol of Torm)."
> — `/home/user/waterdeep/sources/adventure-wdmm.json:59201`

**Field 7. Conflicts and what was not found**

- Alternate names differ between FRHoF and SCAG. FRHoF has "Torm the True" (5etools:2). SCAG has "The True" (5etools:25). See Conflicts.
- The Dragon Heist "Major Temples" table has no Torm row.
- No Torm shrine or chapel is named in any Waterdeep ward in the adventure text. The Dock Ward chapel exists only in the Order events.

---

### Helm

**Field 1. Identity**

> "- altNames: ['He of the Unsleeping Eyes', 'The Vigilant', 'The Watcher']"
> "- title: God of watchfulness"
> "- plane: Mechanus"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:2`, `:3`, `:5` (FRHoF p.108)

> "- altNames: ['The Watcher', 'He of the Unsleeping Eyes', 'The Vigilant One']"
> "- alignment: ['L', 'N']"
> "- domains: ['Life', 'Light', 'Twilight']"
> "- symbol: Staring eye on upright left gauntlet"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:27`, `:29`, `:30`, `:31` (SCAG p.21, 2014)

> "| alignment5e         = [[Lawful neutral]]"
> "| symbol5e            = An upright left gauntlet with a staring eye on it"
> "| domains5e           = [[Life domain|Life]], [[Light domain|Light]], [[Twilight domain|Twilight]]"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:34`, `:35`, `:41` (wiki 5e infobox)

**Field 2. Edict or core tenet**

> "Helm's priests teach followers to be vigilant, aware, and prepared for one's enemies. Patience, clear thought, and careful planning will always defeat rushed actions. Those who favor Helm strive to be alert, clearheaded, and true to their word."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:10` (FRHoF p.108)

> "Helm's priests teach that one must be ever vigilant, ever aware, ever prepared for one's enemies. Patience, clear thought, and careful planning will always defeat rushed actions in the end."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:36` (SCAG p.21, 2014)

No formal edict is listed in the wiki.

**Field 3. Portfolio and Areas of Concern**

> "Helm is a god of vigilance and protection—the ultimate guardian, watcher, and sentinel."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:7` (FRHoF p.108)

> "| portfolio5eR        = Protection, vigilance, watchfulness"
> "| portfolio3e         = Guardians, protectors, protection"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:25`, `:69`

Areas of Concern: not found for Helm.

**Field 4. Worship (Waterdeep first)**

Waterdeep: Helm's Hall (Dragon Heist table, Southern Ward) and the Temple of Helm (campaign, Castle Ward). See Answers Q1 and the Major Temples section.

> "Chosen of Helm—called Sentinels—arise from any walk of life, as the Watcher chooses those who stand against overwhelming peril for the sake of others."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:11` (FRHoF p.108)

> "Everwatch Knights: The Everwatch Knights is a mercenary knighthood formed by Helm's faithful. The Everwatch makes Helm's vigilance readily available and generates income for the greater faith."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:12` (FRHoF p.108)

> "When he speaks to mortals, he materializes in as a massive armored figure or sends a {@creature Planetar|XMM} to deliver his word."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:8` (FRHoF p.108)

> "Helmites celebrated the festival known as the [[Ceremony of Honor to Helm]] on [[Shieldmeet]].<ref name="F&A-p69"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:156` (ref: Faiths & Avatars p.69)

> "| holy days3e         = [[Shieldmeet]]"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:75` (3e infobox)

Temples in the wiki (none is in Waterdeep), lines 166 to 171:
> "* [[Noble Hand]], in [[Tsurlagol]]<ref name="F&A-p69" />"
> "* The [[House Invincible]], in [[Silverymoon]]<ref name="TSF-p32">{{Cite book/The Savage Frontier|32}}</ref><ref name="VGttN-p173">{{Cite book/Volo's Guide to the North|173}}</ref><ref name="TN-GttSF-C&C-p52">{{Cite book/The North: Guide to the Savage Frontier/Cities & Civilization|52}}</ref>"
> "* [[Helm's Shieldhall]], in [[Elturel]]<ref name="FRA-p84">{{Cite book/Forgotten Realms Adventures|84}}</ref>"
> "* [[Temple of the Vigilant Guard]], in [[Iljak]]<ref name="F&A-p69" />"
> "* [[Helm's Cathedral]] in [[Helm's Hold]]<ref name="NCS-p165">{{Cite book/Neverwinter Campaign Setting|165}}</ref>"
> "* [[Keep of Vigilance]] in [[Everlund]]<ref name="SM-p78">({{Cite book/Silver Marches|78}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:166` to `:171`

**Field 5. Relations with other powers, and origin**

> "Helm's faith has known dark days. He was slain in a duel with Tyr—a tragic injustice some say was arranged by Cyric."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:9` (FRHoF p.108)

> "Far back in time, the deity [[Lathander]] caused a divine purge known as the [[Dawn Cataclysm]] in which Helm's lover, a lesser deity of pragmatism called [[Murdane]], was a victim. Helm begrudged the Morninglord for this.<ref name="F&P-p38">{{Cite book/Faiths and Pantheons|38}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:141` (ref: Faiths and Pantheons p.38)

> "The only god who could have been considered a full ally of the Watcher was [[Torm]], the god of paladins. Strongly held ideological differences caused a great rivalry verging on hatred between the clergy of the two gods, but the deities themselves remained close.<ref name="F&P-p28"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:143` (ref: Faiths and Pantheons p.28)

> "In [[1384 DR]], while conveying messages from [[Tyr]] to [[Tymora]] during the pair's courtship, a strange and fateful misunderstanding resulted in the accusation that Helm had stolen Tymora's heart. Helm was subsequently slain in a duel by Tyr. Cyric was suspected to have had a hand in these events.<ref name="GHotR-159" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:185` (ref: Grand History of the Realms p.159)

> "After the [[Second Sundering]], Helm returned to the Realms."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/wiki.txt:190` (followed by refs to a Reddit AMA and to The Sentinel p.264)

**Field 6. Campaign and published-adventure mentions (first six)**

> "The three temples are the Halls of Justice, which is the temple of Tyr, the Temple of Helm in the Castle Ward, and the Chapel of the Steadfast Shield, a Torm chapel in the Dock Ward."
> — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:192`

> "**Temple of Helm (Castle Ward)**"
> — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:222`

> "The temples are the Halls of Justice, the Temple of Helm in the Castle Ward and the Chapel of the Steadfast Shield in the Dock Ward."
> — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r10-whitehawk/ev-01-whitehawk.md:150`

> "A resident who was hurt is carried to the Temple of Helm, whose healers treat the Watch's poor for free."
> — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/ev-01-twelvedog-court.md:185`

> "> - **Temple of Helm, Castle Ward.** Helm's priests run a hospice wing for Watch veterans and their families, and the donation goes to the healing work."
> — `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/s01-the-tithe/ev-01-the-tithe.md:97`

> "The Griffon Cavalry sets up an immense bonfire at the peak of Mount Waterdeep, honoring the fallen and the risen gods Myrkul, Cyric, Kelemvor, Mystra, Helm, and Ao who appeared here."
> — `/home/user/waterdeep/sources/adventure-wdh.json:31536` (festival "Marpenoth 15: Gods' Day," heading at line 31531)

**Field 7. Conflicts and what was not found**

- The ward of the Temple of Helm conflicts between the Dragon Heist table and the campaign (see Conflicts).
- Title: FRHoF and PHB disagree (see Conflicts).
- Everwatch: no Waterdeep hit in the campaign or the adventure JSON.
- Noise: the adventure Grep for "Helm" and "Watcher" returned six `wdmm` lines that name a helm (a green copper helm, "Helm of the Scavenger", "Hidden Helm") or a Watcher monster. The campaign Grep returned seven noise lines with "The Watcher" as a title (see Not found).

---

### Ilmater

**Field 1. Identity**

> "- altNames: ['The Crying God', 'He Who Endures', 'The Rack-Broken Lord']"
> "- title: God of endurance"
> "- plane: Bytopia (Shurrock)"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:2`, `:3`, `:5` (FRHoF p.109)

> "- altNames: ['The Crying God', 'The Rack-Broken Lord', 'He Who Endures']"
> "- alignment: ['L', 'G']"
> "- domains: ['Life', 'Twilight']"
> "- symbol: Hands bound at the wrist with red cord"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:27`, `:29`, `:30`, `:31` (SCAG p.21, 2014)

> "| symbol              = Pair of white hands bound with red cord<br/><small>Formerly:</small> A blood-stained rack."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:9`

> "| alignment5e         = [[Lawful good]]"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:36`

**Field 2. Edict or core tenet**

> "Ilmater is a god of suffering, martyrdom, and perseverance, renowned for his compassion and endurance."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:7` (FRHoF p.109)

> "If he had his way, Ilmater would take all the suffering in the world onto himself to spare others. Since he can't, he blesses those who endure on others' behalf, and he alleviates suffering when he can."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:8` (FRHoF p.109)

> "They put others ahead of themselves, share all they have, and emphasize the spiritual nature of life over the welfare of the material body."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:9` (FRHoF p.109)

**Field 3. Portfolio and Areas of Concern**

> "| portfolio5eR        = Endurance, suffering, martyrdom, perseverance"
> "| portfolio3e         = Endurance, Martyrdom, Perseverance, Suffering"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:27`, `:71`

Areas of Concern: not found for Ilmater.

**Field 4. Worship (Waterdeep first)**

Waterdeep: the Hospice of St. Laupsenn (Dragon Heist table, North Ward), which the adventure text calls a temple of Ilmater. No Waterdeep worship of Ilmater appears in the campaign.

> "Ilmater's priests take in the sick, the starving, and the injured, and his temples give away most of what they receive to offset the suffering of the world."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:9` (FRHoF p.109)

> "Priests of Ilmater wear hair shirts, vests of coarse fur. It is taboo to harm such priests as they go about their duties, including when they administer to the wounded on a battlefield."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:10` (FRHoF p.109)

> "He sometimes sends a {@creature Shield Guardian|XMM} to protect a mortal in need and shows favor by growing daisies and white roses or sending peaceful animals."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:8` (FRHoF p.109)

> "Broken Ones: The Broken Ones is a monastic order of temple and caravan guards dedicated to Ilmater."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:12` (FRHoF p.109)

> "Ilmater's clergy numbered [[cleric]]s, [[paladin]]s, and [[monk]]s.<ref name="FRCS1e-p11"/><ref name="FaP-p30"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:168` (refs: Cyclopedia of the Realms p.11; Faiths and Pantheons p.30)

> "During the [[Second Sundering]] of the late 15th century [[DR]], a [[Chosen]] of Ilmater began a passive slave revolt in [[Calimshan]] against their [[genie]] masters."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:200` (followed by a SCAG p.9 ref)

Holy days: none in any Ilmater source (the wiki's 3e and 5e holy-days fields are blank).

**Field 5. Relations with other powers, and origin**

> "The order finds lasting allies in the faithful of Lathander."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:16` (FRHoF p.109)

> "The ranks of Ilmater's closest allies included [[Tyr]] the Maimed God, god of justice (who was his superior prior to the [[Spellplague]]); and [[Torm]] the True, god of loyalty and duty. Collectively, these three deities formed the [[Triad]], an alliance of lawful good deities that was stronger as a united force than individually."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:157` (two sentences; refs follow in the full line)

> "Another of Ilmater's allies was [[Lathander]] the Morninglord, god of renewal and vitality.<ref name="FaA-p75"/><ref name="FRCS3e-p242"/><ref name="FaP-p30"/> He was also allied with [[Ibrandul]], the Lord of the Dry Depths, the freedom-loving god of caves and darkness.<ref name="FaA-p75"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:159` (refs: Faiths & Avatars p.75; FRCS 3e p.242; Faiths and Pantheons p.30)

> "Among his other foes were [[Bane]], [[Bhaal]], [[Garagos]], [[Malar]], [[Myrkul]], [[Shar]], and [[Talos]].<ref name="FaA-p75"/><ref name="FaP-p30"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:161` (the last sentence of that paragraph)

> "Many years after the Procession, [[Torm]] joined them as Tyr's war leader. Together, Ilmater, Torm, and Tyr formed the [[Triad]], a long-lasting alliance of [[good]] and [[Alignment|lawful]] deities.<ref name="FaP-p80"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:185` (ref: Faiths and Pantheons p.80)

> "The Triad was broken in the [[1384 DR|Year of Three Streams Blooded, 1384 DR]], when Tyr was manipulated into slaying [[Helm]], god of guardians. Ilmater chose to leave the [[House of the Triad]] and, at the invitation of [[Sune]], goddess of beauty, he relocated his divine realm to the plane of [[Brightwater]].<ref name="tGHotR-p159">{{Cite book/The Grand History of the Realms|159}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:198` (ref: Grand History of the Realms p.159)

**Field 6. Campaign and published-adventure mentions**

> "The only person with whom she's civil is Vhaspar Holmdreg (LG male Illuskan human {@creature priest}), who rents a room in the west wing of the residence and works in the North Ward at the Hospice of St. Laupsenn, a temple of Ilmater, god of suffering."
> — `/home/user/waterdeep/sources/adventure-wdh.json:13267`

> "| 4 | **Brother Aldric** | NG human — *30-day tenure only* | Thin, calm, Ilmater robes, unhurried stillness. Has clearly walked a considerable distance (muddy boots on a dry day). "I cook for my brothers at the monastery. I am between postings and find cooking for strangers clarifying." Then: "I also know several healing prayers." Casts *Cure Wounds* (2d8+4) once per day. Extraordinary cooking — treats feeding people as an act of worship. Leaves after exactly 30 days regardless of circumstances. | Order of Ilmater (between monasteries; this is his sabbatical, not an assignment). | 8 gp | +2 Revenue. Kitchen Event penalty removed during his tenure. After departure: −1 Fame for 1 tenday. |"
> — `/home/user/waterdeep/campaign/guides/trollskull-manor/03-staff-and-hiring.md:67`

> "Vhaspar Coldwater is a retired City Watch sharpshooter of fifty-seven who served twenty years in the Dock Ward. He now takes private contracts, and he has killed three people with a heavy crossbow from high windows in twelve days."
> — `/home/user/waterdeep/campaign/quests/faction-events/lords-alliance/m04-the-archer-above/overview.md:21` (name collision; see Conflicts)

**Field 7. Conflicts and what was not found**

- The Hospice of St. Laupsenn is in the Dragon Heist table and the adventure text, and in no campaign file.
- Planes: FRHoF gives Bytopia (Shurrock). The wiki's 3e and later lines place his realm in the House of the Triad and then Brightwater (see Conflicts).
- Not found for Ilmater: holy days, an Ilmater shrine in Waterdeep other than the Hospice, a Broken Ones presence in Waterdeep, and any Ilmater Chosen in Waterdeep.

---

### Lathander

**Field 1. Identity**

> "- altNames: ["Inspiration's Dawn", 'The Morninglord', 'The Rose-And-Gold God']"
> "- title: God of dawn and renewal"
> "- plane: Elysium (Eronia)"
> "- worshipers: Aristocrats, athletes, merchants, youths"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:2`, `:3`, `:5`, `:4` (FRHoF p.111)

> "- title: God of birth and renewal"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:20` (PHB p.294, 2014; conflicts with FRHoF, see Conflicts)

> "- alignment: ['N', 'G']"
> "- domains: ['Life', 'Light']"
> "- symbol: Road traveling into a sunrise"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:30`, `:31`, `:32` (SCAG p.21, 2014)

> "| alignment5e         = [[Neutral good]]"
> "| aspects             = [[Amaunator]]"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:30`, `:9` (wiki 5e; the aspect is in the unlabelled-edition infobox)

**Field 2. Edict or core tenet**

> "They teach others not to wallow in negativity, that life comes from death and every morning offers a chance to turn a setback into a success."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:10` (FRHoF p.111)

> "* "From death, life."<ref name="FA-90-92" />"
> "* "There is always another dawn."<ref name="FA-90-92" />"
> "* "In the dawn, beauty reigns, and the way is clearer."<ref name="FA-90-92" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:176` to `:178` (favored sayings; ref Faiths & Avatars pp.90-92)

**Field 3. Portfolio and Areas of Concern**

> "He is a god of dawn and the potential that comes with new beginnings."
> "Spring, birth, youth, creativity, and renewal fall under his domain."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:7` (FRHoF p.111)

> "| portfolio5eR        = Dawn, beginnings, birth, creativity, renewal, spring, youth"
> "| portfolio5e         = Dawn, renewal"
> "| portfolio3e         = Athletics, birth, creativity, dawn, renewal, self-perfection, spring, vitality, youth"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:21`, `:36`, `:65`

Areas of Concern: not found for Lathander.

**Field 4. Worship (Waterdeep first)**

Waterdeep: Spires of the Morning, Castle Ward (quoted under Answers Q1).

> "The glorious Spires of the Morning, dedicated to Lathander, is one of Waterdeep's most beautiful temples."
> — `/home/user/waterdeep/sources/adventure-wdh.json:31015`

> "An early morning visit from an exuberant songbird might be a good omen from the god. He also sends pixies with iridescent wings the colors of sunrise."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:8` (FRHoF p.111)

> "Temples of Lathander hold a special ceremony called the Song of Dawn on {@book Midsummer|FRHoF|2|Midsummer} morning and at the equinoxes. During this event, priests and the faithful sing praises to the Morninglord."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:9` (FRHoF p.111)

> "Novices in the Lathanderian faith were called the Awakened, while [[clerics]] were known as [[Dawnbringer]]s."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:138`

> "This holiday is named in honor of Lathander's first prophet, Rhyester, a young blind boy who was cured of that blindness by the dawn's light on this day more than seven centuries ago."
> — `/home/user/waterdeep/sources/adventure-wdh.json:31376` (Ches 1: Rhyestertide, heading at line 31372)

> "| holy days3e         = Any dawn, Midsummer morning, the equinoxes"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:71` (3e infobox)

**Field 5. Relations with other powers, and origin**

> "Lathander and Chauntea had been romantically connected for centuries and saw each other as kindred spirits.<ref name="tymore9">{{Cite book/Tymora's Luck|5-6|1}}</ref> His allies included [[Gond]], [[Tymora]], [[Tyr]], [[Torm]], [[Ilmater]], [[Sune]], [[Selûne]], [[Oghma]], [[Kelemvor]], and [[Mielikki]]. His foes were [[Cyric]], [[Talos]], and [[Shar]]. [[Helm]] held a great deal of resentment for Lathander, as the latter indirectly caused the death of Helm's lover, [[Murdane]].<ref name="FaP-38" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:129` (refs: Tymora's Luck pp.5-6; Faiths and Pantheons p.38)

> "Lathander was the central figure in the [[Dawn Cataclysm]], an ill-fated attempt by the Morninglord to reshape the Faerûnian pantheon in his own image. Several deities were killed in the events that followed, including the goddess [[Murdane]], a death for which [[Helm]] never forgave Lathander."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:181` (ref to Faiths and Pantheons p.38 follows)

> "Lathander, however, returned during the events of [[Second Sundering]] in [[1486 DR]], thanks to the effort of his [[Chosen]] and prophet [[Stedd Whitehorn]].<ref name="TR">{{Cite book/The Reaver}}</ref> However, by the year [[1491 DR]], Amaunator and Lathander were once again worshiped as separate beings.<ref>{{Cite book/Sword Coast Adventurer's Guide|13,21,24,32}}</ref> It is unknown if they were actually separate beings by this time or if Lathander was simply granting spells to the followers of Amaunator.{{Speculation}}"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:191`

> "Chosen of Lathander wield powerful magic of light and life and spend their time lending these services to other good deities on Lathander's behalf. Some theorize that these acts of benevolence are Lathander's way of apologizing to the gods for the Dawn Cataclysm—an eons-old incident in which
> Lathander foolishly attempted to remake all deities in his image, leading to the deaths of several gods whose names have been nearly forgotten."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:11` and `:12` (FRHoF p.111; the bundle breaks the sentence across two lines, joined here)

**Field 6. Campaign and published-adventure mentions (first six)**

> "Victoro, a half-elf banker and worshipper of Lathander, and Ammalia, a wizard known for driving a hard bargain and for keeping the most beautiful butterfly garden in Waterdeep, fund temples, orphanages and civic improvements across the city."
> — `/home/user/waterdeep/campaign/setting/organizations/10-cassalanters.md:58`

> "To the world, Victoro is a devilishly handsome half-elf banker, philanthropist, and worshipper of Lathander whose profits fund charity, with an unreadable smile and a genuine warmth toward his younger children that makes the rest of what he is harder to see."
> — `/home/user/waterdeep/campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:23`

> "Victoro is a priest of Asmodeus, though his devotion to the Lord of the Nine Hells is a secret known only to his wife and his closest friends. Most Waterdavians know him as a successful banker, philanthropist, and worshiper of Lathander."
> — `/home/user/waterdeep/sources/adventure-wdh.json:32692`

> "The campaign's public cover is Lathander for Victoro and Siamorphe for the house, which matches *Dragon Heist*, and the page keeps it."
> — `/home/user/waterdeep/campaign/setting/organizations/10-cassalanters.md:120`

> "| Ches 1 | Rhyestertide | Lathander's faithful wear sunrise colors and keep one eye covered until the next dawn. |"
> — `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:101`

> "- Temples of the ward: the Temple of the Seldarine for all elven gods, the Spires of the Morning for Lathander, one of the city's most beautiful temples, the Font of Knowledge for Oghma, with the library, and the Halls of Justice for Tyr (see Landmarks)."
> — `/home/user/waterdeep/campaign/gazetteer/waterdeep/castle-ward.md:164`

**Field 7. Conflicts and what was not found**

- The title conflicts between PHB 2014 and FRHoF/SCAG (see Conflicts).
- The Spires of the Morning and its ward agree across all sources (no conflict).
- Not found for Lathander: a Lathander holy day named in the campaign other than Rhyestertide, a Dawnbringer in Waterdeep, a campaign Chosen of Lathander.

---

### Waukeen

**Field 1. Identity**

> "- altNames: ['The Coinmaiden', 'Our Lady of Gold', "The Merchant's Friend"]"
> "- title: God of trade"
> "- plane: The Outlands"
> "- worshipers: Merchants, the rich, traders"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:2`, `:3`, `:5`, `:4` (FRHoF p.127)

> "- title: Goddess of trade"
> "- alignment: ['N']"
> "- domains: ['Knowledge', 'Trickery']"
> "- symbol: Upright coin with Waukeen's profile facing left"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:14`, `:15`, `:16`, `:17` (PHB p.294, 2014)

> "| gender              = Feminine"
> "| alignment5e         = [[Neutral]]"
> "| domains5e           = [[Knowledge domain|Knowledge]], [[Trickery domain|Trickery]]"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/wiki.txt:19`, `:55`, `:62`

**Field 2. Edict or core tenet**

> "Greed motivates those who take Waukeen as a patron, but the Coinmaiden frowns on misers and smiles on the industrious and the profligate."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:9` (FRHoF p.127)

> "Those who follow Waukeen's ethos create opportunity for all and see competition for wealth as society's best method of progress."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:10` (FRHoF p.127)

> "It's common practice for her followers to set aside a tithe of ten percent of their profits, but rather than being given to a temple, the money is spent to help a struggling business, to finance a new endeavor, or, if all else fails, on frivolous fun."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:10` (FRHoF p.127)

**Field 3. Portfolio and Areas of Concern**

> "Waukeen is a god of wealth and trade."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:7` (FRHoF p.127)

> "| portfolio5eR        = Wealth, trade"
> "| portfolio5e         = Trade"
> "| portfolio3e         = Trade, money, wealth"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/wiki.txt:46`, `:61`, `:91`

Areas of Concern: not found for Waukeen.

**Field 4. Worship (Waterdeep first)**

Waterdeep: none. No Waukeen temple or shrine is named in any Waterdeep source (Answers Q1).

> "Temples of Waukeen resemble guildhalls and serve as meeting places for trade associations."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:10` (FRHoF p.127)

> "Collectively, Waukeen's worshipers were known as Waukeenar.<ref name="FA-178" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/wiki.txt:173` (ref: Faiths & Avatars p.178)

> "Her clerics, called [[Goldeye|Goldeyes]], and other worshipers traveled the trade routes aiding merchants and caravans or worked in the opulent temples as hosts for wealthy donors, moneylenders, [[currency]] exchangers, venture capitalists, warehousers, fences (covertly, of course) and, most importantly, security guards.<ref name="FaP-88" /><ref name="FA-178" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/wiki.txt:173`

> "Waukeen takes the form of a splendidly dressed woman with long golden hair, often accompanied by two golden {@creature Lion|XMM|Lions}."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:8` (FRHoF p.127)

> "When she sends an emissary, she sends an awakened golden {@creature Cat|XMM}, {@creature Lion|XMM}, or eagle ({@creature Hawk|XMM}), or she might send a {@creature Sphinx of Lore|XMM}."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:8` (FRHoF p.127)

> "This festival has long gathered a number of older holidays under one name, stretching those celebrations into a holiday season that lasts a tenday."
> — `/home/user/waterdeep/sources/adventure-wdh.json:31405` (Waukeentide, heading "Tarsahk 1–10: Waukeentide" at line 31401)

Holy days: the campaign and adventure name Sornyn (Flamerule 3 to 5) as a Waukeen and Lathander festival (quoted under Field 6). The wiki's holy-day list is not quoted here.

**Field 5. Relations with other powers, and origin**

> "Waukeen's closest ally was [[Lliira]], who was the trustee of Waukeen's portfolio while she made her ill-fated attempt to get back to her realm in the [[Outlands]] during the [[Time of Troubles]].<ref name="FA-177" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/wiki.txt:166` (ref: Faiths & Avatars p.177)

> "Waukeen had no real enemies among the pantheon except [[Mask]], the Master of All Thieves, because larceny is bad for business."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/wiki.txt:168` (the sentence sits in a ref-bearing paragraph; this sentence has no ref of its own)

> "Waukeen was a relatively late addition to the [[Faerûnian pantheon]], joining sometime after [[Tyr]]<ref name="CotR-16" /> who first appeared in {{Yearlink|-247}}.<ref name="GHotR-52">{{Cite book/The Grand History of the Realms|52}}</ref><ref name="FaP-80">{{Cite book/Faiths & Pantheons|80}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/wiki.txt:180`

> "Chosen of Waukeen possess their god's keen understanding of contracts and agreements and can rival powerful devils at unwinding convoluted terms. They intervene when the wealth of nations is at stake."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:11` (FRHoF p.127)

**Field 6. Campaign and published-adventure mentions (first six)**

> "| Tarsakh 1–10 | Waukeentide | Commerce festival; Cassalanters host public galas; cover for Sea Ward investigation |"
> — `/home/user/waterdeep/campaign/setting/waterdeep-lore.md:45`

> "| Tarsakh 1 to 10 | Waukeentide | A tenday of commerce honoring Waukeen. Caravance on Tarsakh 1 (gift-giving), Goldenight on Tarsakh 5 (shops open all night), Guildsmeet on Tarsakh 7 (a guild gala from dusk to dawn) and Leiruin on Tarsakh 10 (guild dues paid and charters renewed with the Lords). | Trade festival. Cassalanter social events peak. Cover for Cassalanter Villa surveillance. |"
> — `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:83`

> "| Flamerule 3 to 5 | Sornyn | A festival of Waukeen and Lathander for treaties, business planning and receiving envoys. |"
> — `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:108`

> "The wiki lists Waukeen, Siamorphe and Asmodeus as the house's favored deities."
> — `/home/user/waterdeep/campaign/setting/organizations/10-cassalanters.md:63`

> "{@i NG female Chultan human priest of Waukeen}"
> — `/home/user/waterdeep/sources/adventure-wdh.json:1557`

> "Obaya, a priest, has traveled from Chult to sponsor expeditions into Undermountain, with the goal of bringing its magical treasures back to her employer, the merchant prince Wakanga O'tamu of Port Nyanzaru."
> — `/home/user/waterdeep/sources/adventure-wdh.json:1558`

**Field 7. Conflicts and what was not found**

- Gender: FRHoF titles her "God of trade" and uses feminine pronouns. PHB and SCAG say "Goddess of trade". The wiki says "Feminine" (see Conflicts).
- Not found for Waukeen: a Waterdeep temple (adventure, campaign or wiki); a campaign Goldeye or Waukeenar NPC; a campaign Chosen of Waukeen; the Harlot's Coin Heresy in the campaign.

---

## Major Temples of Waterdeep (adventure-wdh.json, lines 30910 to 30997)

Caption, line 30910:
> "caption": "Major Temples of Waterdeep",
> — `/home/user/waterdeep/sources/adventure-wdh.json:30910`

Column labels, lines 30911 to 30915: "Deity or Deities", "Temple Name", "Location".

Helm, lines 30938 to 30940:
> "Helm",
> "Helm's Hall",
> "Southern Ward"
> — `/home/user/waterdeep/sources/adventure-wdh.json:30938` to `:30940`

Ilmater, lines 30943 to 30945:
> "Ilmater",
> "Hospice of St. Laupsenn",
> "North Ward"
> — `/home/user/waterdeep/sources/adventure-wdh.json:30943` to `:30945`

Lathander, lines 30948 to 30950:
> "Lathander",
> "Spires of the Morning",
> "Castle Ward"
> — `/home/user/waterdeep/sources/adventure-wdh.json:30948` to `:30950`

Torm: no row. Waukeen: no row. The deity column across lines 30922 to 30995 reads, in order: All deities; All elven deities; Gond; Helm; Ilmater; Lathander; "Mielikki, Silvanus"; Mystra; Oghma; Selûne; Sune; Tempus; Tymora; Tyr; Umberlee.

---

## Conflicts between sources

1. **Helm's temple ward.**
   - Dragon Heist table (adventure, rank 2): "Helm's Hall" in the "Southern Ward" (`/home/user/waterdeep/sources/adventure-wdh.json:30939` to `:30940`).
   - Campaign events (rank 1, which outranks the adventure under the campaign-first ranking): "**Temple of Helm (Castle Ward)**" (`/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:222`), and "> - **Temple of Helm, Castle Ward.** Helm's priests run a hospice wing for Watch veterans and their families, and the donation goes to the healing work." (`/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/s01-the-tithe/ev-01-the-tithe.md:97`).
   - The campaign gazetteer names the conflict (`/home/user/waterdeep/campaign/gazetteer/waterdeep/castle-ward.md:272`), quoted under Answers Q1. A second gazetteer line says: "The Temple of Helm is placed in the Castle Ward by one campaign guide and in the Southern Ward by the Dragon Heist table, and the wiki's Castle Ward temple list does not name it, so it is not a Castle Ward temple here either." (`/home/user/waterdeep/campaign/gazetteer/waterdeep/castle-ward.md:165`; the rest of that bullet covers Tymora's Tower of Luck.)
   - The wiki the gazetteer cites is not in `helm/wiki.txt`. `helm/wiki.txt` names no Waterdeep temple.

2. **Halls of Justice ward (Tyr's temple, one of the Order's three temples).**
   - `/home/user/waterdeep/campaign/setting/waterdeep-lore.md:37`: "- Halls of Justice, the temple of Tyr, in the Castle Ward (Justice; City Watch captain is a worshiper)"
   - `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r10-whitehawk/design-notes.md:21`: "- The Torm chapel, the door-warden and the clerk come from the First Meeting and the tithe event. `waterdeep-lore.md:36` still puts Tyr's temple in the Sea Ward."
   - Line 36 of `waterdeep-lore.md` is the Sea Ward list, not Tyr's temple. The Dragon Heist table (`/home/user/waterdeep/sources/adventure-wdh.json:30988` to `:30990`) also gives the Halls of Justice as Castle Ward. The r10 design note is stale.

3. **The Torm chapel and the rejected name.**
   - `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/design-notes.md:19`: "The Torm chapel is the Chapel of the Steadfast Shield in the Dock Ward from the First Meeting, not the reference's Chapel of the Faithful Hand in the Trades Ward."
   - No file in the bundle or the adventure names the Chapel of the Faithful Hand. The Dock Ward chapel comes from the First Meeting (`/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:192`).

4. **Lathander's title.**
   - PHB 2014: "- title: God of birth and renewal" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:20`).
   - FRHoF 2024-era canon: "- title: God of dawn and renewal" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:3`). SCAG 2014 gives the same title (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:29`).
   - FRHoF outranks PHB and SCAG on the brief's ranking. The wiki's 5e infobox does not give a title.

5. **Waukeen's gender and title.**
   - FRHoF: "- title: God of trade" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:3`), with "She is interested in anything that increases trade..." (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:7`).
   - PHB 2014: "- title: Goddess of trade" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:14`).
   - SCAG 2014: "Waukeen is the goddess of wealth and trade, on both sides of the law." (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/5etools.md:28`).
   - Wiki: "| gender              = Feminine" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/waukeen/wiki.txt:19`).
   - FRHoF is the canon the brief names. The 2014 sources and the wiki say goddess.

6. **Torm's alternate names.**
   - FRHoF: "- altNames: ['The Hand of Righteousness', 'The Loyal Fury', 'Torm the True']" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:2`).
   - SCAG 2014: "- altNames: ['The Loyal Fury', 'The True', 'The Hand of Righteousness']" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:25`).

7. **Helm's title.**
   - FRHoF: "- title: God of watchfulness" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:3`).
   - PHB 2014: "- title: God of protection" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/helm/5etools.md:19`).

8. **Plane.**
   - Lathander: FRHoF "- plane: Elysium (Eronia)" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/5etools.md:5`). Wiki 3e: "| homeplane3e         = [[House of Nature]]" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/lathander/wiki.txt:61`).
   - Ilmater: FRHoF "- plane: Bytopia (Shurrock)" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/5etools.md:5`). The wiki's realm history: "Ilmater chose to leave the [[House of the Triad]] and, at the invitation of [[Sune]], goddess of beauty, he relocated his divine realm to the plane of [[Brightwater]]." (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilmater/wiki.txt:198`).
   - Torm: FRHoF "- plane: Mount Celestia (Mercuria)" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/5etools.md:5`). Wiki 3e: "| homeplane3e         = [[House of the Triad]]" (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/torm/wiki.txt:90`).
   - These are edition differences in the wiki and are not resolved here.

9. **Name collision: Vhaspar.**
   - The Ilmater priest in the adventure is "Vhaspar Holmdreg" (`/home/user/waterdeep/sources/adventure-wdh.json:13267`).
   - The campaign's Vhaspar is "Vhaspar Coldwater" (`/home/user/waterdeep/campaign/quests/faction-events/lords-alliance/m04-the-archer-above/overview.md:21`), a retired Watch sharpshooter who is not an Ilmater priest.

---

## Cross-references (hits not quoted above)

Torm (campaign):
- `/home/user/waterdeep/campaign/guides/factions/05-order-of-the-gauntlet.md:64`: "Savra vouches for the member at any temple of Tyr, Helm or Torm in Waterdeep."
- `/home/user/waterdeep/campaign/guides/gm-guide/player-factions-overview.md:98`: "Your contact vouches for your good faith to any temple of Tyr, Helm, or Torm in Waterdeep."
- `/home/user/waterdeep/campaign/guides/players-guide/faction-affiliations.md:93`: "| **Chevall** | 1 | Recognized member. Your contact vouches for your good faith to any temple of Tyr, Helm, or Torm in Waterdeep. Each temple casts *Cure Wounds* on you for free, once per day, and gives you a bed for the night. |"
- `/home/user/waterdeep/campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:28`: "| **Order of the Gauntlet** | Savra Belabranta visits Trollskull in person; no advance invitation | Any character in no other faction; a Cleric or Paladin class, an Acolyte, Guard or Soldier background, or worship of Helm, Torm or Tyr only decides whom Savra addresses first |"
- `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:203`: "Any temple of Tyr, Helm or Torm in Waterdeep treats a member as a friend of the Order. A priest casts *Cure Wounds* on the member and gives the member a bed for the night."
- `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/design-notes.md:21`: "- Father Corwen Thale (priest of Tyr, seals the oath), Brother Haldric Wence (door-warden of the Halls of Justice) and the Chapel of the Steadfast Shield (a Torm chapel in the Dock Ward). Each was grep-checked against `campaign/` and has no collision."
- `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/design-notes.md:15`: "The fourth Torm pattern, the general fiendish signs, is given only after the member has been through Twelvedog Court, so the briefings cannot reveal devils before the party has met one."
- `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:233`: quoted under Torm Q2.
- `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r10-whitehawk/design-notes.md:21`: quoted under Conflicts 2.
- `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r50-righteous-hand/ev-01-righteous-hand.md:106`: "> > "By the authority of the Order of the Gauntlet, I invest you as Righteous Hand. Tyr, Helm and Torm are witness to it, and so are the people in this hall. Rise, and carry it as Aldwin Dunhallow did.""
- `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r50-righteous-hand/ev-01-righteous-hand.md:139`: "- **Where it works:** the writ is honored in Waterdeep, Neverwinter, Baldur's Gate and Daggerford, and refused in Luskan. Elsewhere on the Sword Coast, a town honors it when it has a temple of Tyr, Helm or Torm."
- `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/r50-righteous-hand/ev-01-righteous-hand.md:143`: "- **Lodging:** any temple of Tyr, Helm or Torm lodges the member and up to four companions for three nights a visit, free of charge."

Torm (adventure and Undermountain):
- `/home/user/waterdeep/sources/adventure-wdh.json:3942`: "The Order of the Gauntlet looks for members who seek to fight evil in all its forms. Adventurers who worship Helm, Torm, or Tyr are especially sought after."
- `/home/user/waterdeep/sources/adventure-wdmm.json:54888`: "A mote of goodness still burns within the planetar. If the characters can make {@creature Fazrian|WDMM} realize that it has become what it sought to destroy, the planetar will end itself and, with its self-sacrifice, earn Torm's forgiveness."
- `/home/user/waterdeep/sources/adventure-wdmm.json:56393`: "When the characters first arrive, a silent, spectral scene plays out before them: a middle-aged human cleric wildly swings her {@item mace of smiting} at an unseen foe. The cleric wears a blood-streaked breastplate emblazoned with a white right-handed gauntlet (the symbol of Torm). Suddenly, as she pulls her mace back for another swing, her head separates from her shoulders, sliced off by an invisible blade. Then the image fades."
- `/home/user/waterdeep/sources/adventure-wdmm.json:57153`: "Any character who succeeds on a {@dc 15} Intelligence ({@skill Religion}) check realizes that the hand shape on the back wall resembles the symbol of Torm."
- `/home/user/waterdeep/sources/adventure-wdmm.json:58665`: "An incomplete statue partially hewn from marble stands in the middle of the area. The stone is carved into the rough shape of the god Torm. Someone who succeeds on a {@dc 15} Intelligence ({@skill Religion}) check identifies the statue's unfinished features as the iconography of the god of duty, loyalty, and law."
- `/home/user/waterdeep/sources/adventure-wdmm.json:59681`: "{@b Fresco}. A 10-foot-square, tiled fresco on the middle of the east wall depicts {@creature Dezmyr Shadowdusk|WDMM|Dezmyr} and {@creature Zalthar Shadowdusk|WDMM} as heavily armored human paladins of Torm, riding on armored horses and brandishing shields."
- `/home/user/waterdeep/sources/adventure-wdmm.json:57214`: "{@adventure Level 22|WDMM|22} of Undermountain became a safe haven where the Shadowdusks could treat with Far Realm horrors away from the prying eyes of their fellow Waterdavians." (the next sentence is quoted under Torm Field 6.)

Helm (campaign):
- `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/ev-01-twelvedog-court.md:185`: quoted under Helm Q2.
- `/home/user/waterdeep/campaign/guides/gm-guide/player-factions-overview.md:99`: "| **Marcheon** | 3 | Your contact, Savra, fights beside the whole party in one operation per quest. Borrow one mundane weapon or armor from the Order's armory per tenday at no cost. Once per tenday, a priest at one of three temples briefs you on a pattern of trouble in the city. Savra uses the Knight stat block and counts as a full ally from 4th level. She withdraws at 20 Hit Points and refuses an operation she thinks will get the party killed. Brother Osric Wickersham keeps the armory, and the item must come back serviceable. The three temples are the Halls of Justice, the Temple of Helm in the Castle Ward and the Chapel of the Steadfast Shield in the Dock Ward. Each keeps a list of patterns without names, and none of the lists names the Cassalanters. |"
- `/home/user/waterdeep/campaign/gazetteer/waterdeep/castle-ward.md:31`: "- **Religion:** Temple of the Seldarine (all elven gods), Spires of the Morning (Lathander), Font of Knowledge (Oghma), Halls of Justice (Tyr)." (the bullet continues about the wiki's House of Two Hands and Tymora's Tower of Luck, which the campaign does not use for Helm.)

Helm (adventure):
- `/home/user/waterdeep/sources/adventure-wdh.json:1403`: quoted under Torm Field 6.
- `/home/user/waterdeep/sources/adventure-wdh.json:30939`: "Helm's Hall" (Major Temples table).

Lathander (campaign):
- `/home/user/waterdeep/campaign/setting/deities/asmodeus.md:100`: "- `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md`: public worship of Lathander and the family's public devotion to Siamorphe."
- `/home/user/waterdeep/campaign/setting/deities/asmodeus.md:115`: "- **Lathander** (Deities, page planned): Victoro's public cover."
- `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:60`: quoted under Lathander Q2.
- `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:108`: "| Flamerule 3 to 5 | Sornyn | A festival of Waukeen and Lathander for treaties, business planning and receiving envoys. |"
- `/home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:337`: "> > "Lathander keep me, is it done? You have it, don't you? Nobody followed? I've got to be back at the villa by eleven bells. Mr. Crowelle counts the household at the door. I couldn't explain myself if I were late.""
- `/home/user/waterdeep/campaign/setting/organizations/10-cassalanters.md:20`: "- **A Good Name Is Worth Keeping:** The charity is real. The family funds temples, orphanages and civic improvements, and Victoro is known as a worshipper of Lathander. Their warmth, including their warmth toward tieflings, is specific and genuine. Victoro keeps his philanthropist reputation as a working part of the plan, and the Harpers, who watch the family's charitable work, have found nothing wrong with it for years."
- `/home/user/waterdeep/campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:23`: quoted under Lathander Field 6.

Lathander (adventure):
- `/home/user/waterdeep/sources/adventure-wdh.json:30948` to `:30950`: quoted in the Major Temples section.
- `/home/user/waterdeep/sources/adventure-wdh.json:31372`: "name": "Ches 1: Rhyestertide",
- `/home/user/waterdeep/sources/adventure-wdh.json:31461`: "Sornyn is a festival of both Waukeen and Lathander, and is used for planning business, making treaties and agreements, and receiving envoys from unknown lands and traditional foes." (the rest of the passage covers the wine and the author's own contract.)
- `/home/user/waterdeep/sources/adventure-wdmm.json:48631`: "She now leads Shar's debased cult in Vanrakdoom and intends to send the group on a mission to destroy the Spires of the Morning, the temple of Lathander (god of birth and renewal) in Waterdeep."
- `/home/user/waterdeep/sources/adventure-wdmm.json:50537`: quoted under Lathander Q1.

Waukeen (campaign and adventure):
- `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:68`: "| Tarsakh 1 to 10 | Waukeentide | **Cassalanter Villa** | Cassalanter social events peak. Gifts on Tarsakh 1, an all-night gala on Tarsakh 5 and the Charity Ball on Tarsakh 7 are the villa's entry points |"
- `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:117`: "- **Waukeentide.** Goldenight and Guildsmeet put crowds in the Cynosure and the Field of Triumph, and the Cassalanters host their own events. Any surveillance of the villa during these days has cover."
- `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:126`: "Waukeentide fills the first tenday of Tarsakh with trade and galas, and on Founders' Day, the first of Flamerule, the Field of Triumph stages illusory histories of the city while Castle Waterdeep is veiled as the log fortress of Nimoar." (the rest of the passage covers Fleetswake and the guild calendar.)
- `/home/user/waterdeep/campaign/setting/history/00-the-history.md:40`: "Waterdhavians mark the year with public festivals such as Fleetswake, Waukeentide and Founders' Day, and the guilds, temples and Lords use the holidays to renew charters and make agreements." (the first sentence covers the city's government.)
- `/home/user/waterdeep/campaign/guides/gm-guide/structural-rules.md:49`: "| Tarsakh 1–10 | Waukeentide | Trade festival; Cassalanter social events peak; cover for Cassalanter Villa surveillance |"
- `/home/user/waterdeep/campaign/structure/arc-g-cassalanter-villa.md:73`: "Waukeentide (Tarsakh 1–10) provides the primary casing and operation windows:"
- `/home/user/waterdeep/campaign/setting/organizations/10-cassalanters.md:58`: quoted under Lathander Field 6 (the same line says the family "hosts public galas during Waukeentide").
- `/home/user/waterdeep/sources/adventure-wdh.json:31401`: "name": "Tarsahk 1–10: Waukeentide",
- `/home/user/waterdeep/sources/adventure-wdh.json:31461`: quoted under Lathander cross-references.
- `/home/user/waterdeep/sources/adventure-wdmm.json:348`: "Obaya Uday, a neutral good Chultan priest of Waukeen (god of trade), has traveled from the distant city of Port Nyanzaru on behalf of a wizard named Wakanga O'tamu to procure magic items from Waterdeep. When she learned about Undermountain, Obaya booked a room at the Yawning Portal in the hope of hiring adventurers to plunder the dungeon of its magical riches."
- `/home/user/waterdeep/sources/adventure-wdmm.json:3831`: "When a half-elf cleric of Waukeen named Halleth Garke accused his adventuring companions of withholding treasure from him, the other members of the Fine Fellows of Daggerford (not including Kelim in {@area area 36b|0bf|x}, who had already wandered off) beat Halleth to death and threw his body into the pit. Halleth \"awoke\" the next day as a {@creature revenant}, compelled to find and kill the three who murdered him. Unfortunately for him, he is unable to climb out of the pit without assistance and has been pacing down there for days."
- `/home/user/waterdeep/sources/adventure-wdmm.json:6387`: "{@b Midna}. Midna Tauberth (NE female human {@creature priest} of Shar) relaxes in one of several overstuffed chairs in the middle of the room, waited on by nine {@creature Living Unseen Servant|WDMM|living unseen servants} (see {@adventure appendix A|WDMM|25}). Around her neck, she wears two holy symbols: one shaped like a gold coin (the symbol of Waukeen, god of trade), the other a black disk outlined in purple (the symbol of Shar, god of darkness and loss)."

---

## Not found

Searched for each power in `/home/user/waterdeep/campaign`, both adventure JSON files, and the wiki and 5etools bundles.

- **Torm.** Areas of Concern (no source lists them). A Waterdeep temple or shrine in the adventure table (no Torm row). A campaign Torm holy day, omen or messenger. A Torm Chosen in any campaign file. Terms searched: `\bTorm\b`, "Loyal Fury", "Hand of Righteousness", "Hand Resolute", "white gauntlet", "Triad", "Steadfast Shield".
- **Helm.** Areas of Concern. Everwatch in any Waterdeep source (Everwatch appears only in the bundles). A campaign Helm holy day. Terms searched: `\bHelm\b`, "Everwatch", "Helm's", "Vigilant One", "The Watcher", "Ever Watchful", "Sentinels", "Chosen of Helm".
- **Ilmater.** Areas of Concern. A holy day in any source. A Hospice of St. Laupsenn or any Ilmater shrine in the campaign. A Broken Ones presence in Waterdeep. An Ilmater Chosen in Waterdeep. Terms searched: "Ilmater", "Crying God", "Broken Ones", "Rack-Broken", "One Who Endures", "Broken God", "Hospice", "Laupsenn", "Ilmatari", "Ayuruk", "Itishikopak", "Martyrdom".
- **Lathander.** Areas of Concern. A Lathander holy day in the campaign other than Rhyestertide. A Dawnbringer in Waterdeep. A campaign Chosen of Lathander. Terms searched: "Lathander", "Morninglord", "Spires of the Morning", "Dawnbringer", "Rhyester", "Rose-and-Gold", "Dawn Cataclysm", "Sun Soul", "Song of Dawn".
- **Waukeen.** Areas of Concern. A Waterdeep temple or shrine in any source. A campaign Goldeye or Waukeenar NPC. A campaign Chosen. A Waukeen NPC from the adventure (Obaya Uday, Halleth Garke, Midna) in the campaign. The Harlot's Coin Heresy in the campaign. Terms searched: "Waukeen", "Coinmaiden", "Our Lady of Gold", "Golden Lady", "Merchant's Friend", "Goldeye", "Harlot".
- **Noise counted.** Campaign lines with "The Watcher" as a title (not Helm): `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/ev-02-the-imp-at-dawn.md:61`, `/home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:158`, `/home/user/waterdeep/campaign/quests/faction-events/lords-alliance/m01-the-long-watch/ev-01-six-bells-at-the-muleskull.md:189` and `:191`, `/home/user/waterdeep/campaign/quests/faction-events/harpers/m01-the-talking-mare/overview.md:41`, `/home/user/waterdeep/campaign/quests/faction-events/harpers/m01-the-talking-mare/ev-01-the-talking-mare.md:145` and `:212`. That is 7 lines. Adventure JSON noise for Helm: `/home/user/waterdeep/sources/adventure-wdmm.json:2861`, `:6818`, `:23873`, `:61572`, `:61582`, `:61588` (a helm, a Watcher monster, or a "Watchers in the Dark" area). "Drow Sentinels" at `/home/user/waterdeep/sources/adventure-wdmm.json:12708` is not Helm. Noise for Waukeen: none beyond "Waukeentide", which I counted as a hit because it names the goddess.

---

## Not readable

- None in scope. The Alexandrian PDFs and `sources/SOURCE_GUIDE.md` were not opened (out of scope per the brief). No `.docx` file was needed for these five powers.
