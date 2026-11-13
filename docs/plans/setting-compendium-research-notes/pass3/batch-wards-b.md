# Pass 3 research notes: batch-wards-b (Southern Ward, Dock Ward, Field Ward)

Scope: `sources/research/pass3-bundles/{southern-ward,dock-ward,field-ward}/` (adventure.txt, wiki.txt, campaign-hits.txt, adventure-hits.txt), plus the campaign and Notable Figures files each quote names. All paths are relative to `/home/user/waterdeep/`. Quotes are copied from tool output. JSON string escapes are shown as plain characters. Wiki reference tags are removed after the quoted sentence; wikitext link markup is kept as written. Where a search hid a line behind "[Omitted long matching line]", the line was read directly before it was quoted.

## Gaps the drafter must know first

- **Kolat Towers and Helm's Hall are not in any wiki bundle.** The brief says the wiki agrees that Kolat Towers is in the Southern Ward. A search of every `wiki.txt` in `sources/research/pass3-bundles/` for `Kolat`, `Helm's`, `Temple of Helm` and `Phaulkon` returned no Kolat Towers line and no Helm's Hall line. The only Helm hits concern Neverwinter's "Helm's Hold" (`sources/research/pass3-bundles/vault-of-dragons/wiki.txt:299`, `sources/research/pass3-bundles/open-lord-and-masked-lords/wiki.txt:395`). The wiki claim cannot be checked from the bundles.
- **The published Chapter 9 Dock Ward and Field Ward entries are short and name no landmarks.** Landmarks come from published chapters 1 to 8 and the wiki.
- **Population, lifestyle, languages and dominant faith are blank in all three wiki pages.** No ward-level source fills them for any of the three wards.

---

# SOUTHERN WARD

## Q1. At a Glance

**District type**
> "Today, the ward still hosts most of the traveling merchants who visit the city, and is made up of many enclaves, blocks, and streets primarily occupied by citizens who trace their ancestry to other realms."
> — `sources/adventure-wdh.json:31048`

> "The Southern Ward has long been a district of laborers catering to travelers, so its folk have adopted the architectural custom of building homes and businesses above stables or around inn yards, near to where wagon trains are housed."
> — `sources/adventure-wdh.json:31049`

> "| type               = City ward"
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:9` (infobox field)

> "This was considered the "poor" ward and was often known as '''Caravan City''' due to the large numbers of caravan merchants, teamsters and guards that swelled the population of the ward most of the year."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:101`

**Boundaries**
> "The northern boundary with [[Trades Ward of Waterdeep|Trades Ward]] lay across [[Telshambra's Street]] and [[Caravan Court]]. On the west and south side was [[Dock Ward of Waterdeep|Dock Ward]] across the [[Way of the Dragon (Waterdeep)|Way of the Dragon]]. To the east, the Ward was bounded by the city walls (circa [[1372 DR]]), specifically the "[[Trollwall]]", which included the southern inner gate leading to the [[Caravan Grounds]] and the [[South Gate (Waterdeep)|South Gate]] beyond."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:96`

> "The ward was bounded in the south by the [[Southern Ward of Waterdeep|Southern Ward]], in the west by [[Castle Ward]], in the north by [[North Ward of Waterdeep|North Ward]] and the [[City of the Dead (Waterdeep)|City of the Dead]] and in the east by the [[Trollwall]]."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:387` (Trades Ward article, a linked page; this is the Trades Ward's own boundary)

> "Positioned as it is nigh the place where four wards meet, you can use it to judge where you stand. If it is south and west of your position, you are in the Trades Ward. North and west? The Southern Ward. South and east? The Castle Ward. North and east? You're in the Dock Ward."
> — `sources/adventure-wdh.json:30693` (Honorable Knight orientation text)

**Founded**
> "The Castle Ward was one of the original wards of Waterdeep, established by [[Ahghairon]] in the {{Template:YearlinkName|1035}} together with the [[Waterdeep/Trades Ward|Trades Ward]], [[Waterdeep/Southern Ward|Temple Ward]], and [[Waterdeep/Dock Ward|Dock Ward]]."
> — `sources/research/pass3-bundles/trades-ward/wiki.txt:334` (a wiki sentence in a linked page, about the Castle Ward; it gives 1035 DR for the Southern Ward as the "Temple Ward")

> "- The wiki says the city's ward system began in 1035 DR with four wards: Castle, Trades, Dock and the Southern Ward, which it calls the Temple Ward (Forgotten Realms Wiki, History of Waterdeep; City of Splendors boxed set Campaign Guide p. 30, 2e)."
> — `campaign/setting/history/01-ahghairons-gifts.md:59`

The Southern Ward wiki page gives no founding date of its own (`sources/research/pass3-bundles/southern-ward/wiki.txt:40`, `| established        = ` blank).

**Population**
> "| population         = "
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:18` (blank)

No ward figure exists. City-wide figure, for drafter labelling only:
> "| population1        = 1,347,680<ref name="FRCS-pp178-180" /><ref group="note">In the ''[[Forgotten Realms Campaign Setting 3rd edition]]'', the population of Waterdeep is stated to be 1,347,800, though the metropolitan population (i.e., those in the city proper) is only 132,661.</ref>"
> — `sources/research/pass3-bundles/waterdeep-overview/wiki.txt:62` (the note in the same line gives 1,347,800 for the 3rd edition; the infobox gives 1,347,680)

**Lifestyle**: no source fills this field. The closest line is the laborer sentence at `sources/adventure-wdh.json:31049`, quoted above.

**Services** (guildhalls, from the wiki; ref tags removed)
> "* [[Builders' Hall]]: Headquarters of the [[Guild of Stonecutters, Masons, Potters, & Tile-makers]]."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:116`

> "* The [[House of Good Spirits]]: Inn, tavern, winery, and headquarters of the [[Vintners', Distillers', & Brewers' Guild]]."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:117`

> "* The [[Road House]]: Headquarters of the [[Fellowship of Carters and Coachmen]]."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:119`

> "* [[Nueth's Fine Nets]]: Nets, rope, tarpaulins, hammocks, and similar items."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:133`

**Primary peoples**
> "Today, the ward still hosts most of the traveling merchants who visit the city, and is made up of many enclaves, blocks, and streets primarily occupied by citizens who trace their ancestry to other realms."
> — `sources/adventure-wdh.json:31048`

> "One can indulge in the finest halfling food here, enjoy the best singers of Calishite music, and examine the most stunning works of dwarven crafting-but the first challenge is finding where these treats are housed."
> — `sources/adventure-wdh.json:31049`

**Languages**: no source fills this field (`sources/research/pass3-bundles/southern-ward/wiki.txt:20`, `| languages          = ` blank).

**Religion**
> "Her Chosen lives at Phaulkonmere in the Southern Ward."
> — `campaign/setting/deities/mielikki.md:57`

> "Phaulkonmere is an old estate and garden in the Southern Ward, and no file calls it a temple or a shrine."
> — `campaign/setting/deities/mielikki.md:60`

> "Yondalla has one shrine in the campaign files, on Larkhaven Street in the Southern Ward. The published adventure places none."
> — `campaign/setting/deities/yondalla.md:57`

Published Major Temples table, rows for Helm. Caption: `"caption": "Major Temples of Waterdeep",` (`sources/adventure-wdh.json:30910`). Row lines: `"Helm",` (30938), `"Helm's Hall",` (30939), `"Southern Ward"` (30940).

The wiki's religion field is blank (`sources/research/pass3-bundles/southern-ward/wiki.txt:21`). No dominant faith is sourced.

**Governance**: no source names a ward government, court or Watch post. Campaign-only trace: "The Watch officers on the Saerdoun Street beat were transferred to a Far South Ward assignment the week before the raid." (`campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:111`). Drafter: `[research]`.

**Influences** (mascot and colours)
> "Residents of the Southern Ward take pride in their legacy as overland travelers and hardworking folk, so it should be no surprise that the ward's mascot is the mule. On their competition flags, a pugnacious mule in rampant pose stands on a field of red and white-colors said to represent the blood and tears the people of the Southern Ward have shed during their labors."
> — `sources/adventure-wdh.json:31050`

**Architecture**
> "Dust and mud were common on the streets and most buildings were old, multi-story tenements with shops or businesses on the ground floor."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:103`

> "Even when the full moon isn't out, the Dancing Court is worth visiting because of the adjacent festhall, the Jade Dancer. During appearances of the Moon Sphere, people sometimes daringly leap into the field of magic from the balconies of this three-story tavern, dance hall, and inn."
> — `sources/adventure-wdh.json:31052`

**Economy**
> "This was considered the "poor" ward and was often known as '''Caravan City''' due to the large numbers of caravan merchants, teamsters and guards that swelled the population of the ward most of the year."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:101`

> "* [[Aurora's Realms Shop, South High Road Catalogue Counter]]: The Southern Ward outlet of [[Aurora's Emporium]]."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:130`

**Organizations**
> "Its Waterdeep presence centers on Phaulkonmere, an old estate and garden in the Southern Ward."
> — `campaign/setting/organizations/03-emerald-enclave.md:20`

> "She leads the Cassalanter response team from the Converted Windmill on Coachlamp Lane in the Southern Ward."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:19`

> "{@creature Manshoon|WDH} took control of Kolat Towers, a crumbling residence in the Southern Ward that was abandoned years ago by the two wizards who built it."
> — `sources/adventure-wdh.json:32218`

Fields with no source: Population (ward figure), Lifestyle, Languages, Governance body.

## Q2. Landmarks (14 candidates, published first, wiki second, campaign third)

**1. Phaulkonmere** (Emerald Enclave estate)
> "Members of the Emerald Enclave can be found in Phaulkonmere, a noble villa in the Southern Ward, and at the Snobeedle Orchard and Meadery in Undercliff. The walls of Phaulkonmere enclose fabulous gardens, and the buildings are covered with moss and ivy."
> — `sources/adventure-wdh.json:1320`
- Runs it: "The place is owned by descendants of two wealthy families-the Tarms (longtime Waterdavians) and the Phaulkons (who are of Cormyrean descent)." (`sources/adventure-wdh.json:1320`); "They spend most of the year traveling abroad and entrust the estate to a half-elf groundskeeper named {@creature Melannor Fellbranch|wdh}." (`sources/adventure-wdh.json:1320`)
- Hook: "Come meet us at Phaulkonmere in the Southern Ward. The gate will be open." (`campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:39`, the cat's message)
- Journal: none in `campaign/locations/`. Covered by the Emerald Enclave faction events.

**2. Kolat Towers** (Manshoon's towers)
> "This dilapidated, two-towered edifice stands tall in the Southern Ward. Its neighbors are aware of the magical force field that surrounds it, and they can see light from {@spell continual flame} spells spilling out of the windows. Despite these persistent magical effects, most folk believe the structure is abandoned. Others think it's haunted by the ghosts of the Kolat brothers. They're wrong, of course."
> — `sources/adventure-wdh.json:26797`
- Runs it: "{@creature Manshoon|WDH} took control of Kolat Towers, a crumbling residence in the Southern Ward that was abandoned years ago by the two wizards who built it." (`sources/adventure-wdh.json:32218`)
- Hook: "{@creature Manshoon|WDH} posts no visible guards outside Kolat Towers, since he wants others to believe the site is abandoned." (`sources/adventure-wdh.json:26798`)
- Journal: none in `campaign/locations/`. Quest structure only: `campaign/structure/arc-i-kolat-towers.md` (pending conversion). Ward conflict in Q9.

**3. Helm's Hall** (published name for the temple of Helm)
- Published row: `"Helm",` / `"Helm's Hall",` / `"Southern Ward"` (`sources/adventure-wdh.json:30938-30940`).
- Runs it: no source. Hook: none in the bundles. Journal: none. Deity page: `campaign/setting/deities/helm.md` (conflict in Q4).

**4. The Jade Dancer** (tavern and festhall)
> "The \"Jade Dancer\" is an eight-foot-tall jade statue of a woman that magically animates and dances for patrons-and on occasion serves as a bouncer."
> — `sources/adventure-wdh.json:31052`
> "Elminster has informed me that despite its dexterity and seemingly fragile beauty, the Jade Dancer is as puissant as a stone golem."
> — `sources/adventure-wdh.json:31052`
- Wiki: "* The [[Jade Dancer]]: Tavern and festhall famous for its dancing statue." (`sources/research/pass3-bundles/southern-ward/wiki.txt:107`)
- Runs it: no source. Journal: none.

**5. The Dancing Court and the Moon Sphere**
> "Not a landmark as such, but surely a sight that must be seen, is the Moon Sphere. This isn't a structure but an event that occurs during every full moon, when a glowing, spherical field of blue light appears in the square known as the Dancing Court. Any creatures that enter the sphere find that they can fly about inside it just by willing themselves to do so."
> — `sources/adventure-wdh.json:31051`
- Hook (published): "For centuries, Waterdavians have used these supernatural events to develop a unique flying style of dance-but amateur enthusiasts aren't welcome, except on certain daylight appearances of the full moon." (`sources/adventure-wdh.json:31051`)
- Wiki: "The Dancing Court was located in the south section of Waterdeep's [[Waterdeep/Southern Ward|Southern Ward]]. It branched northeast off of the southern end of [[Slop Street]]." (`sources/research/pass3-bundles/southern-ward/wiki.txt:1133`)
- Journal: none.

**6. Caravan Court**
> "* [[Caravan Court]]: Popular place where caravans mustered and disbanded."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:124`
> "Caravan Court was located in the northeast section of Waterdeep's [[Waterdeep/Southern Ward|Southern Ward]]. The northern side of the courtyard bordered the [[Waterdeep/Trades Ward|Trades Ward]]."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:495`
- Runs it: no source. Hook: none sourced. Journal: none.

**7. The Trollwall** (city wall; inner gate)
> "To the east, the Ward was bounded by the city walls (circa [[1372 DR]]), specifically the "[[Trollwall]]", which included the southern inner gate leading to the [[Caravan Grounds]] and the [[South Gate (Waterdeep)|South Gate]] beyond."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:96`
> "This short avenue from Caravan Court to the Trollwall in the Southern Ward is haunted by the hooded ghost of the mage Ruid, whose touch causes deathly chills to those he meets on foggy nights."
> — `sources/adventure-wdh.json:31294`
- Journal: none.

**8. Ruid's Stroll** (haunted avenue)
> "All attempts to banish or turn the spirit have failed. Those who brave its unearthly approach and allow Ruid to pass through them learn a secret truth about someone or something in their life—if they survive."
> — `sources/adventure-wdh.json:31294`
- Wiki street listing: "* [[Ruid's Stroll]]<ref ...>" (`sources/research/pass3-bundles/southern-ward/wiki.txt:143`).
- Journal: none.

**9. The Converted Windmill, Coachlamp Lane** (Asmodean shrine; Cassalanter response team base)
> "The characters head to a decrepit building in the Southern Ward that used to be a windmill. Therein, they expect to find the {@item Stone of Golorr|WDH} in the clutches of two treacherous {@creature cult fanatic||cult fanatics} named Arn Xalrondar (LE male Tethyrian human) and Seffia Naelryke (LE female Tethyrian human)."
> — `sources/adventure-wdh.json:13211`
> "### Converted Windmill — Mini-Heist (Southern Ward, Coachlamp Lane)"
> — `campaign/guides/factions/11-cassalanters.md:49`
- Runs it: "She leads the Cassalanter response team from the Converted Windmill on Coachlamp Lane in the Southern Ward." (`campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:19`)
- Hook: "Jeryth has felt a wound in the ley lines near Coachlamp Lane for a tenday and a half. It is not healing. The Enclave has no lead on the cause." (`campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:189`)
- Journal: none. Quest structure: `campaign/structure/arc-e-faction-outposts.md:273`.
- Published windmill references, not stated to be the same building: "The key that the characters found in the mausoleum leads them to an old windmill in the Southern Ward." (`sources/adventure-wdh.json:13184`); "She reveals that the cult fanatics, Arn Xalrondar and Seffia Naelryke, would likely have taken the stone to an old windmill in the Southern Ward, where they hold their own ceremonies worshiping Asmodeus." (`sources/adventure-wdh.json:8318`)

**10. Xanathar Guild hideout "under the Southern Ward"** (Orb Confectioners cellar)
> "The characters have been encouraged to explore a Xanathar Guild hideout under the Southern Ward. They enter the location through {@area B1|1e2}."
> — `sources/adventure-wdh.json:11960`
> "### Orb Confectioners / Xanathar Sewer Hideout — Encounter-Plus (Southern Ward, Rising Ride)"
> — `campaign/guides/factions/09-xanathars-guild.md:51`
> "**Xanathar Sewer Hideout 2** (Southern Ward, via Orb Confectioners)"
> — `campaign/guides/factions/09-xanathars-guild.md:93`
- Runs it: Xanathar's Guild. Journal: `campaign/locations/xanathar-sewer-hideout/area-overview.md` does not name a Southern entrance (a search of that folder for `Southern` and `Orb` returned no match). Ward conflict in Q9.

**11. The Full Cup** (tavern)
> "* The [[Full Cup]]: Caravan worker's and hauler's choice. Brawls were common."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:111`
- Runs it: no source. Journal: none.

**12. The Red Gauntlet** (tavern)
> "* The [[Red Gauntlet]]: Old, dim, and mostly quiet."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:112`
- Runs it: no source. Journal: none.

**13. The Spouting Fish** (tavern; wiki places it in the Southern Ward)
> "* The [[Spouting Fish (Waterdeep)|Spouting Fish]]: Large, noisy, and popular."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:113`
> "| location      = [[Waterdeep/Southern Ward|Southern Ward]], [[Waterdeep]]"
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:1374`
- Published places it in the Dock Ward (see Q9): "Characters who climb the ladder and push open the metal cover find themselves in the cellar of the Spouting Fish, a tavern in the Dock Ward." (`sources/adventure-wdh.json:2251`)
- Journal: none.

**14. The Waymoot** (crossroads and magic signpost)
> "The place where the High Road and the Way of the Dragon meet in the south of the city is called the Waymoot."
> — `sources/adventure-wdh.json:31115`
> "Any character who spends at least three days asking pertinent questions and pursuing leads in the Southern Ward or the Dock Ward can, at the end of that time, make a {@dc 18} Charisma (Persuasion or Intimidation) check."
> — `sources/adventure-wdh.json:4065`
- Campaign use: "The halfling community of the Southern Ward gathers in three places: the market by the Waymoot, the Yondalla shrine on Larkhaven Street, and a run of rented rooms above a cooperage on the same street." (`campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:128`)
- Ward placement: the published text names no ward for the Waymoot (`sources/adventure-wdh.json:31115`). The campaign's design note says: "The source places the Waymoot in the Dock Ward, but the Waymoot is the crossroads in the south of the city, so the meeting is set there." (`campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/design-notes.md:13`). The published line that bears on this is `sources/adventure-wdh.json:4065`, which names the Southern Ward and the Dock Ward as places for leads, not the Waymoot.
- Journal: none.

Also available, outside the 14: the Yondalla shrine on Larkhaven Street ("Yondalla has one shrine in the campaign files, on Larkhaven Street in the Southern Ward.", `campaign/setting/deities/yondalla.md:57`) and the Dusty Ladle ("The meeting is at 20:00 at the Dusty Ladle, a Southern Ward taproom, at the table in the back corner.", `campaign/quests/faction-events/doom-raiders/r10-viper/ev-01-viper.md:15`).

## Q3. Characters of Interest

Notable Figures format: the H1 is the bare name. Alignment, species and pronouns sit in the first bullet of the Gamemaster's Summary. Where the page gives no pronoun, the entry says so.

**Melannor Fellbranch** (Half-Elf druid, Neutral Good, he/him)
> "# Melannor Fellbranch" — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:1`
> "- *Half-Elf druid, Neutral Good, he/him*. Stat block: **Druid**, with Advantage on saving throws against the Charmed condition, immunity to magical sleep, Darkvision 60 ft., and Common and Elvish." — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:5`
> "**Persona.** To the world, Melannor is the friendly but humorless groundskeeper of Phaulkonmere in the Southern Ward, who sends the Enclave's missions by animal." — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:25`
> Alignment note: "**Alignment.** Dragon Heist lists Melannor as Chaotic Good. The campaign keeps Neutral Good, and the Enclave events are written for it." — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:11`

**Jeryth Phaulkon** (Disembodied presence, Neutral Good, Chosen of Mielikki, she/her)
> "# Jeryth Phaulkon" — `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:1`
> "- *Disembodied presence, Neutral Good, Chosen of Mielikki, she/her*. Stat block: none (a disembodied presence, not a combatant)." — `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:5`
> Published: "He is joined by Jeryth Phaulkon, a noblewoman turned demigod who serves Mielikki, divine lady of the forest." (`sources/adventure-wdh.json:1320`)

**Seffia Naelryke** (Human cult fanatic (Asmodeus), lawful evil; no pronoun field on the page)
> "# Seffia Naelryke" — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:1`
> "- *Human cult fanatic (Asmodeus), lawful evil*. Stat block: **Cultist Fanatic**." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:8`
> "Seffia Naelryke is a Human woman who maintains a decrepit windmill in the Southern Ward and sleeps in one of its upper rooms. She shares the building with Arn Xalrondar, who defers to her judgment on anything that involves planning, and she does not receive visitors." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:41`

**Arn Xalrondar** (Human cult fanatic (Asmodeus), lawful evil; no pronoun field on the page)
> "# Arn Xalrondar" — `campaign/setting/notable-figures/cassalanters/11-arn-xalrondar.md:1`
> "- *Human cult fanatic (Asmodeus), lawful evil*. Stat block: **Cult Fanatic**." — `campaign/setting/notable-figures/cassalanters/11-arn-xalrondar.md:6`
> "Arn Xalrondar occupies a windmill in the Southern Ward alongside Seffia Naelryke, defers to her judgment on all matters of planning, and does not draw attention to himself." — `campaign/setting/notable-figures/cassalanters/11-arn-xalrondar.md:30`

**Vaelle Lurval** (plain text; no Notable Figures page)
> "Vaelle can provide directions, or she can lead characters there if she is healed fully, for the sake of avenging her murdered lover." — `sources/adventure-wdh.json:8318`
> "the cult fanatic who failed to silence Vaelle Lurval" — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:63`

**Brimel Crestfall** (plain text; no Notable Figures page; Cassalanter household steward)
> "Brimel Crestfall is a household steward in the Cassalanter villa." — `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:18`

**Volkarr Kibbens** (plain text; no Notable Figures page)
> "From Elaspra or her records, the characters learn that she sold the key to a man named Volkarr Kibbens, whose address is an old windmill in the Southern Ward." — `sources/adventure-wdh.json:8278`

**Pippa Underbough, Tolliver Greenbottle, Marda Goodbarrel** (plain text; no pages)
> "- **Pippa Underbough**, **Tolliver Greenbottle** and **Marda Goodbarrel**: the Southern Ward halflings who decide whether the party gets to Kelso." — `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:66`

Kelso Fiddlewick is a Field Ward character in his NF page. Istrid Horn is a Dock Ward character in hers.

## Q4. Temples

Published Major Temples table (`sources/adventure-wdh.json:30909-30997`, caption at 30910): the Helm row places Helm's Hall in the Southern Ward (rows at 30938-30940, quoted in Q1). Other rows for context: "Tymora", "Tower of Luck", "Castle Ward" (`sources/adventure-wdh.json:30983-30985`); "Tyr", "Halls of Justice", "Castle Ward" (`sources/adventure-wdh.json:30988-30990`). No Torm row (`campaign/setting/deities/torm.md:131`).

**Conflict: Helm's Hall**
> "Conflict, Helm's temple:** The Dragon Heist table lists "Helm, Helm's Hall, Southern Ward" (`sources/adventure-wdh.json:30938-30940`). The Order of the Gauntlet files place the Temple of Helm in the Castle Ward (`campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:201`; `r10-whitehawk/ev-01-whitehawk.md:150`). The table above follows the campaign. No file says Helm's Hall is the same building, though the Helm page treats it as the published name. The Castle Ward gazetteer (`castle-ward.md:165`) calls the ward unsettled and leaves the temple off its list."
> — `campaign/setting/deities/00-the-deities.md:438`
> "The others are the Temple of Helm in the Castle Ward and the Chapel of the Steadfast Shield, a Torm chapel in the Dock Ward." — `campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:201`
> "The Temple of Helm is placed in the Castle Ward by one campaign guide and in the Southern Ward by the Dragon Heist table, and the wiki's Castle Ward temple list does not name it, so it is not a Castle Ward temple here either." — `campaign/gazetteer/waterdeep/castle-ward.md:165`
> "The Dragon Heist Major Temples table lists "Helm, Helm's Hall, Southern Ward". The campaign's Order of the Gauntlet files put the Temple of Helm in the Castle Ward, so this page follows the campaign file." — `campaign/setting/deities/helm.md:59`

**Yondalla shrine, Larkhaven Street** (campaign only, not in the table): "Yondalla has one shrine in the campaign files, on Larkhaven Street in the Southern Ward. The published adventure places none." (`campaign/setting/deities/yondalla.md:57`)

**Phaulkonmere** is not a temple: "Phaulkonmere is an old estate and garden in the Southern Ward, and no file calls it a temple or a shrine." (`campaign/setting/deities/mielikki.md:60`)

## Q5. Secret

Best candidate: the Converted Windmill is an Asmodean shrine, held by Seffia Naelryke and Arn Xalrondar.
> "**Persona.** To the world, Seffia maintains a decrepit windmill in the Southern Ward, sleeps in one of its upper rooms, and does not receive visitors. To those who investigate, she and Arn have converted the windmill into an Asmodean shrine and a cult fallback location." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:59`

Other factions in the file hold only the question. Bregan D'aerthe's mission treats the windmill as an open question: "What does the family keep in that windmill?" (`campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:518`). The public rumour names only a place: "a windmill in the Southern Ward where lanterns burn on moonless nights." (`campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:100`)

Other hidden-affiliation notes that change play:
- Kolat Towers: "{@creature Manshoon|WDH} posts no visible guards outside Kolat Towers, since he wants others to believe the site is abandoned." (`sources/adventure-wdh.json:26798`). Campaign: "Until **Manshoon Named** is marked, every Doom Raider says "Floxin's cell", "the other cell" or "the Splinter", and calls Kolat Towers "the towers in the Trades Ward"." (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:27`)
- Southern Xanathar hideout: "They enter the location through {@area B1|1e2}." (`sources/adventure-wdh.json:11960`); ward conflict in Q9.

## Q6. Quests, faction events and location journals set in the Southern Ward

Location journals: none. The seven folders under `campaign/locations/` are gralhund-villa, cassalanter-villa, house-of-inspired-hands, sea-maidens-faire, trollskull-manor, xanathar-sewer-hideout and zhentarim-warehouse. None is set in the Southern Ward, and no file in `campaign/locations/` mentions Phaulkonmere.

Campaign quest and structure files:
- **Gralhund Villa**, ev-09 aftermath: "She leaves a handwritten note: the name and location of a Zhentarim courier cache in the South Ward that the party can raid without Manshoon's cell knowing for at least a month." (`campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:77`)
- **Faction Outposts** (structure): "*Southern Ward, Rising Ride.*" (`campaign/structure/arc-e-faction-outposts.md:177`); "*Southern Ward, Coachlamp Lane.* — **Street-level entry point for the Cassalanter chain** (for parties with Divine Sense)." (`campaign/structure/arc-e-faction-outposts.md:273`); "Jeryth Phaulkon has been monitoring a disturbance in the Southern Ward for two weeks." (`campaign/structure/arc-e-faction-outposts.md:85`)
- **Xanathar's Lair** (faction guide): "### Orb Confectioners / Xanathar Sewer Hideout — Encounter-Plus (Southern Ward, Rising Ride)" (`campaign/guides/factions/09-xanathars-guild.md:51`)
- **Cassalanter Villa** (faction guide): "### Converted Windmill — Mini-Heist (Southern Ward, Coachlamp Lane)" (`campaign/guides/factions/11-cassalanters.md:49`)
- **Kolat Towers** (structure): "The result — two interconnected stone towers in the Trades Ward, linked by a bridge at the third floor and bound together by a force field that covered the entire structure from basement to roof — was more fortress than home." (`campaign/structure/arc-i-kolat-towers.md:9`). Ward conflict in Q9.

Doom Raiders:
- **The Missing Snobeedle** (m03): "Spend three days in the Southern Ward following three independent leads to the Shard Shunners." (`campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:8`); "### Three Days in the Southern Ward" (`...ev-01-the-missing-snobeedle.md:126`)
- **The Viper** (r10): "The meeting is at 20:00 at the Dusty Ladle, a Southern Ward taproom, at the table in the back corner." (`campaign/quests/faction-events/doom-raiders/r10-viper/ev-01-viper.md:15`)
- **Dread Lord** (r50): "- **Southern Ward:** a boarding house near the ward's market (a room for the night, paid in advance)." (`campaign/quests/faction-events/doom-raiders/r50-dread-lord/ev-01-dread-lord.md:183`)

Emerald Enclave (Phaulkonmere sits in each):
- **First Meeting** (00): "Hear the cat's invitation at Trollskull Manor and walk to Phaulkonmere in the Southern Ward, where the gate stands open." (`campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:7`)
- **Undercliff Scarecrows** (m01): "A member who wants more can walk to Phaulkonmere in the Southern Ward, where Melannor answers questions at the gate." (`campaign/quests/faction-events/emerald-enclave/m01-the-undercliff-scarecrows/ev-01-the-undercliff-scarecrows.md:40`)
- **Ten Nights in the City of the Dead** (m02): "A member who walks to Phaulkonmere in the Southern Ward before sunset finds Melannor under the oak while companions wait at the gate." (`campaign/quests/faction-events/emerald-enclave/m02-ten-nights-in-the-city-of-the-dead/ev-01-the-ten-nights.md:37`)
- **Doppelganger Problem** (m03): "Members reach Phaulkonmere in the Southern Ward by midmorning, while companions wait at the gate or in the outer garden." (`campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:41`)
- **Fouled Channel** (m05): "The current there runs down to the water table beneath the Southern Ward." (`campaign/quests/faction-events/emerald-enclave/m05-the-fouled-channel/ev-01-the-fouled-channel.md:324`)
- **Summerstrider** (r03): "Phaulkonmere stands in the Southern Ward, and the gate is open before the member arrives." (`campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:41`); "- **Southern Ward:** "Jeryth has felt a wound in the ley lines near Coachlamp Lane for a tenday and a half. It is not healing. The Enclave has no lead on the cause."" (`campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:189`)
- **Autumnreaver** (r10): "- **The Southern Ward route:** the entrance is a sealed iron door at the end of a service ledge in the deep cisterns." (`campaign/quests/faction-events/emerald-enclave/r10-autumnreaver/ev-01-autumnreaver.md:270`)
- **Winterstalker** (r25): "Phaulkonmere stands in the Southern Ward, and the gate is open before the member arrives." (`campaign/quests/faction-events/emerald-enclave/r25-winterstalker/ev-01-winterstalker.md:45`)
- **Master of the Wild** (r50): "Phaulkonmere stands in the Southern Ward." (`campaign/quests/faction-events/emerald-enclave/r50-master-of-the-wild/ev-01-master-of-the-wild.md:48`)
- **The Water Table Stirs** (s02): "Every meeting in this Event takes place at Phaulkonmere in the Southern Ward, about two hours' walk from Trollskull Alley." (`campaign/quests/faction-events/emerald-enclave/s02-the-water-table-stirs/ev-01-the-water-table-stirs.md:47`)

Bregan D'aerthe:
- **The Wazoo Affair** (m02): "Your correspondent has it on good authority, by which is meant the word of three footmen and a wine merchant, ... " is not used; the Southern line is: "A cellar somewhere off Aveen Street is mentioned by the footmen, and so is a windmill in the Southern Ward where lanterns burn on moonless nights." (`campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:100`)
- **The Theater's Back Room** (m05): "Brimel Crestfall is a household steward in the Cassalanter villa, a careful man in his forties. For years he has carried baskets of candles, salt, black wax and wine to a converted windmill on Coachlamp Lane in the Southern Ward." (`campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/overview.md:26`)

Order of the Gauntlet:
- **The Shrine on Aveen Street** (m05): "**Seven:** 23 Tarsakh, 1489 DR. A woman in grey, a tannery in the Southern Ward." (`campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/ev-01-the-shrine-on-aveen-street.md:257`)

Harpers:
- **The High Harper** (r50): "A rope-maker in the South Ward and a glazier in the Castle Ward." (`campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:312`); vouching: "Maera Brandt, rope-maker, 14 Wickerwork Row in the South Ward, and Tomas Ardel, glazier, 3 Mender's Court in the Castle Ward, confirm the dealings on their own receipts." (`campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:320`)

Lords' Alliance:
- **Redknife** (r03 design note): "Kolat Towers stands in the Southern Ward, so the Trades Ward house on Ironwick Lane is not near it." (`campaign/quests/faction-events/lords-alliance/r03-redknife/design-notes.md:24`)

## Q7. Culture, defense, politics, economy and lore

**Culture**
> "The Southern Ward has long been a district of laborers catering to travelers, so its folk have adopted the architectural custom of building homes and businesses above stables or around inn yards, near to where wagon trains are housed." — `sources/adventure-wdh.json:31049`
> "Residents of the Southern Ward take pride in their legacy as overland travelers and hardworking folk, so it should be no surprise that the ward's mascot is the mule." — `sources/adventure-wdh.json:31050`
> "The stretch of buildings and alleyways in this Ward that stood between the Way of the Dragon and the [[High Road (Waterdeep)|High Road]] was an area that locals referred to as the Tween Run." — `sources/research/pass3-bundles/southern-ward/wiki.txt:98`

**Defense**: no source names a Southern Ward garrison, Watch post or guard. The Kolat force field: "The edifice is surrounded by a magical barrier that has the properties of a wall of force." (`sources/adventure-wdh.json:32218`)

**Politics**: no source. Mascot and flags only (`sources/adventure-wdh.json:31050`).

**Economy**: "This was considered the "poor" ward ..." see Q1 (`sources/research/pass3-bundles/southern-ward/wiki.txt:101`).

**Lore**
> "Others think it's haunted by the ghosts of the Kolat brothers. They're wrong, of course." — `sources/adventure-wdh.json:26797`
> "This short avenue from Caravan Court to the Trollwall in the Southern Ward is haunted by the hooded ghost of the mage Ruid, whose touch causes deathly chills to those he meets on foggy nights." — `sources/adventure-wdh.json:31294`
> "It is called the Southern Ward, not the South Ward. Waterdavians are peculiar about this, and if you insist on referring to it as the South Ward, expect to be corrected or thought a fool." — `sources/adventure-wdh.json:31048`
> "As of the [[1491 DR|Year of the Scarlet Witch, 1491 DR]], only outsiders called it '''South Ward''', according to famed author [[Volo]] in his ''[[Volo's Waterdeep Enchiridion|Waterdeep Enchiridion]]''." — `sources/research/pass3-bundles/southern-ward/wiki.txt:93`
> "| aliases            = South Ward, Temple Ward, Caravan City" — `sources/research/pass3-bundles/southern-ward/wiki.txt:8`

## Q9. Conflicts (Southern Ward)

1. **Kolat Towers.** Published Trades Ward: "{@creature Manshoon|WDH} lurks in Kolat Towers, a pair of wizards' towers in the Trades Ward. This residence is described in chapter 8." (`sources/adventure-wdh.json:560`). Published Southern Ward: "Referred to in this adventure simply as \"{@creature Manshoon|wdh},\" this clone of the ancient archwizard infiltrated Waterdeep years ago and has been hiding out in Kolat Towers ever since, in the city's Southern Ward." (`sources/adventure-wdh.json:32215`); and `sources/adventure-wdh.json:26797`, quoted in Q2. Campaign Trades Ward: "**Lair: Kolat Towers** (Trades Ward)" (`campaign/guides/factions/10-manshoons-zhentarim.md:73`); "- Lights have been seen in Kolat Towers in the Trades Ward. She mentions this as a footnote. It is not a footnote." (`campaign/guides/trollskull-manor/08-notable-patrons.md:57`); "The result — two interconnected stone towers in the Trades Ward" (`campaign/structure/arc-i-kolat-towers.md:9`); "- The **Trollskull Manor** guide — corrected from "Southern Ward" to "Trades Ward."" (`campaign/structure/arc-i-kolat-towers.md:325`). Campaign history: "The campaign's Trades Ward stands." (`campaign/setting/history/04-the-founding-of-chains.md:162`). Ranking under the brief: the published adventure governs (ruling 1), and the brief reverses the campaign's Trades Ward reading. The wiki bundles hold no Kolat line (see the top gap).
2. **Helm's Hall.** Published Southern Ward (`sources/adventure-wdh.json:30938-30940`) against campaign Castle Ward (`campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:201`; `campaign/gazetteer/waterdeep/castle-ward.md:165`). Brief ruling 1 puts Helm's Hall in the Southern Ward.
3. **Spouting Fish.** Wiki Southern Ward (`sources/research/pass3-bundles/southern-ward/wiki.txt:1374`) against published Dock Ward (`sources/adventure-wdh.json:2251`). Under the brief, the published adventure outranks the wiki.
4. **Xanathar sewer entry.** Published Southern Ward: "a Xanathar Guild hideout under the Southern Ward" (`sources/adventure-wdh.json:11960`). Campaign Dock Ward: "The sewers beneath the Dock Ward lead to a Xanathar's Guild hideout carved into a decommissioned vault." (`campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:133`). Campaign Castle Ward: "A secret spiral stair in the Castle Ward sewers leads down to Xanathar's lair (area X1 in Dragon Heist)." (`campaign/gazetteer/waterdeep/castle-ward.md:40`). The orchestrator decides.
5. **Istrid Horn's lending.** Retired `campaign/structure/ch1-beginning.md:172` puts her in the South Ward: "A half-dwarf who runs a money-lending operation out of the South Ward and serves as one of Davil Starsong's most effective lieutenants." Campaign: "The lore page puts Istrid's lending in the South Ward while the First Meeting puts her warehouse in the Dock Ward, and this event follows the warehouse." (`campaign/quests/faction-events/doom-raiders/r25-ardragon/design-notes.md:23`). The retired file is not authoritative; the campaign's Dock Ward reading stands.
6. **Phaulkonmere.** Published Southern Ward (`sources/adventure-wdh.json:1320`; `sources/adventure-wdh.json:3700`: "The characters' main contact in the Emerald Enclave is {@creature Melannor Fellbranch|wdh}, the friendly but humorless groundskeeper of Phaulkonmere, a compound located one block south of Kolat Towers (see chapter 8)."). Campaign earlier draft: "Phaulkonmere moves from the Sea Ward to the Southern Ward, as WDH and Appendix B have it." (`campaign/quests/faction-events/emerald-enclave/00-first-meeting/design-notes.md:13`). Current campaign: Southern Ward.
7. **Yondalla shrine ward name.** "`campaign/setting/waterdeep-lore.md:18` writes "South Ward". The mission file, the Dragon Heist table (`sources/adventure-wdh.json:30940`) and the other Deities pages write "Southern Ward"." (`campaign/setting/deities/yondalla.md:120`). Naming only.
8. **Tense.** The Southern wiki page writes in the past tense: "'''Southern Ward''' was the southeastern sector of the city of [[Waterdeep]]." (`sources/research/pass3-bundles/southern-ward/wiki.txt:93`). The published text is in the present tense. Flagged for the drafter, not a fact conflict.

---

# DOCK WARD

## Q1. At a Glance

**District type**
> "The '''Dock Ward of Waterdeep''' was situated on the ''Great Harbor'' of [[Waterdeep]]. It contained the docks, shipbuilding yards, and warehouses for the sea trade. Compared to the rest of the city it was exceptionally dirty, smelly, and particularly dangerous."
> — `sources/research/pass3-bundles/dock-ward/wiki.txt:93`

> "Warehouses, poorhouses, and tenements dominate much of the area."
> — `sources/adventure-wdh.json:31063`

**Boundaries**
> "The South Gate was found in southern Waterdeep where the [[Waterdeep/Dock Ward|Dock Ward]] and [[Waterdeep/Southern Ward|Southern Ward]] met."
> — `sources/research/pass3-bundles/southern-ward/wiki.txt:856`

> "The stretch of buildings and alleyways ... " is not used. The Southern Ward wiki's Dock Ward boundary: "On the west and south side was [[Dock Ward of Waterdeep|Dock Ward]] across the [[Way of the Dragon (Waterdeep)|Way of the Dragon]]." — `sources/research/pass3-bundles/southern-ward/wiki.txt:96`

> "After the [[Spellplague]], the northern section of Waterdeep harbor became dilapidated with most of the harbor choked with sunken ship hulls. This section became known as [[Mistshore]]."
> — `sources/research/pass3-bundles/dock-ward/wiki.txt:98`

> "Mistshore" orientation: "North and east? You're in the Dock Ward." — `sources/adventure-wdh.json:30693`

The Dock Ward wiki page has no boundary paragraph. No source gives a full boundary.

**Founded**
> "The Castle Ward was one of the original wards of Waterdeep, established by [[Ahghairon]] in the {{Template:YearlinkName|1035}} together with the [[Waterdeep/Trades Ward|Trades Ward]], [[Waterdeep/Southern Ward|Temple Ward]], and [[Waterdeep/Dock Ward|Dock Ward]]."
> — `sources/research/pass3-bundles/trades-ward/wiki.txt:334`
Campaign: "- The wiki says the city's ward system began in 1035 DR with four wards: Castle, Trades, Dock and the Southern Ward, which it calls the Temple Ward (Forgotten Realms Wiki, History of Waterdeep; City of Splendors boxed set Campaign Guide p. 30, 2e)." (`campaign/setting/history/01-ahghairons-gifts.md:59`)

**Population**: no ward figure. Wiki field blank: `| population         = ` (`sources/research/pass3-bundles/dock-ward/wiki.txt:18`). Published: "Yes, aside from the Field Ward, this is the area where most of Waterdeep's poor reside." (`sources/adventure-wdh.json:31062`). City-wide figure as in the Southern Ward Q1 entry (`sources/research/pass3-bundles/waterdeep-overview/wiki.txt:62`).

**Lifestyle**
> "But all must concede this: the residents of the Dock Ward often work the hardest while living under the harshest conditions."
> — `sources/adventure-wdh.json:31062`

> "Yes, it is home to some of the least literate people in the city. Yes, most of its taverns are inhabited by habitual drinkers, and far too many inns charge by the hour."
> — `sources/adventure-wdh.json:31062`

**Services**
> "Streetlamps don't fare well in the Dock Ward. Their candles, oils, and glass are too regularly stolen or smashed. The Guild of Chandlers and Lamplighters makes a halfhearted attempt to repair the streetlamps at the start of each season, but for most of the year, locals are forced to carry their own light when traveling these streets at night."
> — `sources/adventure-wdh.json:31064`

> "Admittedly, you'll see less reading material in the Dock Ward and the Field Ward, but this fact is notable only because of its preponderance elsewhere."
> — `sources/adventure-wdh.json:31162`

> "* [[Muleskull Tavern]], located along Ship Street, was the guildhall of the [[Dungsweepers' Guild]] and it also doubled as a tavern."
> — `sources/research/pass3-bundles/dock-ward/wiki.txt:149`

> "*[[Ilmater's Safe Harbor]], a soup kitchen."
> — `sources/research/pass3-bundles/dock-ward/wiki.txt:177`

**Primary peoples**
> "Yes, aside from the Field Ward, this is the area where most of Waterdeep's poor reside. Yes, it is home to some of the least literate people in the city."
> — `sources/adventure-wdh.json:31062`

> "Someone is killing elf and half-elf sailors in the Dock Ward. Three are dead so far, and every one of them was beheaded by a blade in the dead of night."
> — `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md:31` (inside Davil's dialogue; the sentence "Three are dead so far, and every one of them was beheaded by a blade in the dead of night." is in the same line)

**Languages**: no source fills this field (`sources/research/pass3-bundles/dock-ward/wiki.txt:20`, blank). Literacy only: "least literate" (`sources/adventure-wdh.json:31062`).

**Religion**
> "Torm has one chapel in the city, the Chapel of the Steadfast Shield in the Dock Ward." — `campaign/setting/deities/torm.md:66`
> "The three temples are the Halls of Justice, which is the temple of Tyr, the Temple of Helm in the Castle Ward, and the Chapel of the Steadfast Shield, a Torm chapel in the Dock Ward." — `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:192`
Dominant faith: no source. The published table has no Dock Ward row (`sources/adventure-wdh.json:30909-30997`).

**Governance**
> "Captain Staget" is not used. The published line: "Staget once had the warehouse under surveillance, but elected to pull the detail to bolster patrols throughout the Dock Ward-a decision he now regrets." — `sources/adventure-wdh.json:2185`
> "Characters who stir up trouble in the Dock Ward are likely to run into Captain Staget again." — `sources/adventure-wdh.json:2205`
> "They are arrested for one or more crimes and taken to a courthouse in the Dock Ward to face sentencing by a magister (encounter 8, \"Courthouse\")." — `sources/adventure-wdh.json:6672` (see Q9 item 2)
> "The Dock Ward Watch post smells of wet wool and lamp oil, and a duty sergeant sits at a ledger behind a long desk." — `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-02-the-nest.md:240`
Ward-level governing body: no source.

**Influences** (mascot and colours)
> "The colors of the Dock Ward are burgundy and orange, and its mascot is a swordfish that has always been depicted as green for reasons lost to time." — `sources/adventure-wdh.json:31065`

**Architecture**
> "Streets are steep throughout, and few have space alongside for pedestrians." — `sources/adventure-wdh.json:31063`
> "Except in the immediate vicinity of the piers, shop signs and advertising of any kind are rare, and warehouses and other businesses often have no sign at all." — `sources/adventure-wdh.json:31063`

**Economy**
> "It contained the docks, shipbuilding yards, and warehouses for the sea trade." — `sources/research/pass3-bundles/dock-ward/wiki.txt:93`
> "* [[Seaswealth Hall]], located on the waterfront and overlooking the city's fish markets, was the guildhall of the [[Fishmonger's Fellowship]]." — `sources/research/pass3-bundles/dock-ward/wiki.txt:150`
> "Istrid Horn is a shield dwarf moneylender running a lending operation from a guarded Dock Ward warehouse." — `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:30`
> "Access to a Black Network safe house in the Dock Ward." — `campaign/guides/factions/07-doom-raiders.md:57`

**Organizations**
> "* [[Shipwrights' House]], located along Dock Street, was the guildhall of the [[The Order of Master Shipwrights]]." — `sources/research/pass3-bundles/dock-ward/wiki.txt:152`
> "* [[Shippers' Hall]], located along Oar Alley, was the guildhall of the [[Fellowship of Salters, Packers, and Joiners]]." — `sources/research/pass3-bundles/dock-ward/wiki.txt:151`
> "* [[Metal House of Wonders]], located along Belnimbra's Street and Gut Alley, was the guildhall of the [[Splendid Order of Armorers, Locksmiths, and Finesmiths]]." — `sources/research/pass3-bundles/dock-ward/wiki.txt:148`
> "* [[Jesters' Clubhouse]], located at the corner of [[Shrimp Alley]] and [[Pressbow Lane]], was the guildhall of the [[Jesters' Guild]]." — `sources/research/pass3-bundles/dock-ward/wiki.txt:146`
> Faction presence: "A dim Dock Ward dive, operated by **Manshoon's Splinter Zhentarim** as an informal ward headquarters." (`campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md:43`); "Seven Masks Theater — Mini-Heist (Dock Ward)" (`campaign/guides/factions/08-bregan-daerthe.md:101`); "Corene is a Harper deep-cover agent embedded in the Dock Ward operation of Xanathar's Guild" (`campaign/setting/notable-figures/harpers/05-corene-wyldath.md:26`).

Fields with no source: Population (ward figure), Languages, dominant Religion, Governance body.

## Q2. Landmarks (14 candidates)

**1. The Skewered Dragon** (dilapidated tavern; Zhentarim-owned in published text, Splinter HQ in the campaign)
> "Volo last saw Floon outside the Skewered Dragon, a dubious (and Zhentarim-owned) tavern between Net Street and Fillet Lane in the Dock Ward." — `sources/adventure-wdh.json:1699`
> "The Skewered Dragon looks like a ruin. Both of its front-facing windows are smashed, and a ship's anchor is lodged in the roof." — `sources/adventure-wdh.json:1792`
- Wiki: "The [[Skewered Dragon]]: A dilapidated tavern that faced an alley between Net Street and [[Fillet Lane]] with a ship's anchor lodged in the roof." (`sources/research/pass3-bundles/dock-ward/wiki.txt:120`)
- Campaign: "A dim Dock Ward dive, operated by **Manshoon's Splinter Zhentarim** as an informal ward headquarters." (`campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md:43`)
- Hook: "Volo tells them Floon was last at the Skewered Dragon on Dock Street." (`campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:123`)
- Journal: none (Finding Floon ev-02 covers it).

**2. The Old Xoblob Shop** (deep gnome informant's shop; beholder in the window)
> "On the corner of Zastrow Street and Fillet Lane is a shop with a peculiar window display:" — `sources/adventure-wdh.json:1732`
> "One nearby shop stands out from the others. It has a deep purple facade, and in its window hangs a stuffed beholder. Above the door hangs a sign whose elaborate letters spell out \"Old Xoblob Shop.\"" — `sources/adventure-wdh.json:1737`
- Wiki: "* [[Old Xoblob Shop]]: trinkets and curios." (`sources/research/pass3-bundles/dock-ward/wiki.txt:137`)
- Runs it: "**Xoblob** (deep gnome, Xanathar's Guild informant, paranoid) witnessed the attack outside his own shop." (`campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md:31`)
- Hook: "The stuffed beholder mounted in Xoblob's window is a magical sensor through which Xanathar occasionally views the street." (`campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md:39`)
- Journal: none.

**3. The Muleskull Tavern** (Dungsweepers' Guild hall; Lords' Alliance protection)
> "\"Meet them at the Muleskull Tavern, on Ship Street in the Dock Ward, at six bells and guard them while they work. Do this every day for a tenday.\"" — `sources/adventure-wdh.json:3912`
- Wiki: "* [[Muleskull Tavern]], located along Ship Street, was the guildhall of the [[Dungsweepers' Guild]] and it also doubled as a tavern." (`sources/research/pass3-bundles/dock-ward/wiki.txt:149`)
- Runs it: no proprietor sourced.
- Campaign: "The Muleskull Tavern stands on Ship Street in the Dock Ward and opens before dawn for dock workers." (`campaign/quests/faction-events/lords-alliance/m01-the-long-watch/ev-01-six-bells-at-the-muleskull.md:88`)
- Journal: none.

**4. The Seven Masks Theater** (Bregan D'aerthe front; Krebbyg as booking manager)
> "She asks the characters to retrieve the stone, for the good of Waterdeep, and deliver it to her at the Seven Masks Theater in the Dock Ward." — `sources/adventure-wdh.json:7152`
- Campaign: "A drow gunslinger who operates as "Kreb Sorrush," booking manager of the Seven Masks Theater in the Dock Ward" (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:30`)
- Hook: "The Seven Masks Theater appears on every list of Dock Ward Bregan D'aerthe assets the party might assemble from outpost intelligence." (`campaign/guides/factions/08-bregan-daerthe.md:31`)
- Journal: none.

**5. Mistshore** (north shore of the harbour; Grinda Garloth, Filthy Meg)
> "If {@creature Xanathar|WDH} is the villain, the stone is delivered to a mage named {@creature Grinda Garloth|WDH}. She owns an {@item apparatus of Kwalish} and lives in Mistshore, a seedy neighborhood built on a dock in the Dock Ward." — `sources/adventure-wdh.json:6169`
> "Mistshore was the name given to the dilapidated north shore of [[Waterdeep]]'s harbor in the late 15th century [[DR]]." — `sources/research/pass3-bundles/dock-ward/wiki.txt:575`
- Campaign: "Filthy Meg is an independent merfolk information broker operating out of Mistshore" (`campaign/setting/notable-figures/independents-adversaries/04-filthy-meg.md:26`); "### Grinda Garloth's — Encounter-Plus (Dock Ward, Mistshore)" (`campaign/guides/factions/09-xanathars-guild.md:37`)
- Journal: none. Named in `campaign/structure/arc-e-faction-outposts.md:163`: "*Dock Ward, Mistshore.* — **Street-level entry point for the Xanathar chain.**"

**6. Istrid Horn's warehouse** (guarded Doom Raiders lending house)
> "The warehouse stands on a Dock Ward street of salt-stained brick, and two broad-shouldered guards at the side door step aside for Yagra without a word." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:378`
- Runs it: Istrid Horn (`campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:22`).
- Journal: none.

**7. The Candle Lane warehouse** (Zhentarim Warehouse)
> "The warehouse sits at the back of a walled yard on Candle Lane." — `campaign/locations/zhentarim-warehouse/area-overview.md:23`
> "This Exploration/Combat Event occurs when the party arrives at the Candle Lane warehouse." — `campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:7`
- Runs it: "The Zhentarim cell that ran this place is dead." (`campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:109`)
- Journal: **Zhentarim Warehouse** (`campaign/locations/zhentarim-warehouse/area-overview.md`).
- Note: "Candle Lane is the Zhentarim warehouse street in the Dock Ward." (`campaign/quests/faction-events/harpers/m01-the-talking-mare/design-notes.md:17`)

**8. The Sea Maidens Faire pier** (Smugglers' Dock)
> "The Sea Maidens Faire fleet occupies a private pier in the Dock Ward (Smugglers' Dock area) and the adjacent anchorage quarter-mile out in Deepwater Harbor." — `campaign/locations/sea-maidens-faire/area-overview.md:7`
- Runs it: "The Doom Raiders have had dealings with Jarlaxle's operation — he approached them early in the campaign about intelligence sharing, which they declined." (`campaign/structure/arc-h-sea-maidens-faire.md:43`) — the Faire is Jarlaxle's (Bregan D'aerthe) operation.
- Journal: **Sea Maidens Faire** (`campaign/locations/sea-maidens-faire/area-overview.md`).

**9. The Xanathar sewer hideout** (beneath the Dock Ward; eleven rooms)
> "The sewer hideout — eleven rooms of a decommissioned vault beneath the Dock Ward — held Floon alive in the boss chamber." — `campaign/quests/act-i/finding-floon/overview.md:55`
> "The sewers beneath the Dock Ward lead to a Xanathar's Guild hideout carved into a decommissioned vault." — `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:133`
- Runs it: Xanathar's Guild. Hook: "One guard was pulled off the watch that night, reassigned to a Dock Ward street crew, and has not been seen since." (`campaign/locations/xanathar-sewer-hideout/area-overview.md:78`)
- Journal: **Xanathar Sewer Hideout** (`campaign/locations/xanathar-sewer-hideout/area-overview.md`). Conflict with the Southern and Castle entries (Q9).

**10. Pier 17 and the south quay** (Guild cargo tunnel; grells)
> "Flying creatures have taken three people from Pier 17 in the Dock Ward, one on each of three nights." — `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-01-the-search.md:31`
> "- **Pier 17:** the barges belong to Xanathar's Guild and carry spoil out of its cargo tunnel under the south quay." — `campaign/quests/faction-events/emerald-enclave/r25-winterstalker/ev-01-winterstalker.md:318`
- Journal: none.

**11. The Peabody cellar** (Fishgut Alley; secret tunnel)
> "An innocent halfling family, the Peabodys, brews beer in this cellar, which lies beneath their home on Fishgut Alley in the Dock Ward." — `sources/adventure-wdh.json:2860`
> "The Peabodys are pragmatic. They are also aware that they live in the Dock Ward and have survived it by minding their own affairs." — `campaign/locations/xanathar-sewer-hideout/q09-private-cellar.md:9`
- Runs it: the Peabody family, halflings who brew beer there (`sources/adventure-wdh.json:2860`).
- Journal: **Xanathar Sewer Hideout**, `campaign/locations/xanathar-sewer-hideout/q09-private-cellar.md`.

**12. The Spices Street hostel** (Shard Shunners base in the published text; ward conflict in Q9)
> "A narrow passage leads to the cellar of a halfling-owned hostel on Spices Street in the Dock Ward. Medium characters must squeeze to reach this area from the tunnel. The hostel is used as a base by the Shard Shunners, a gang of halfling wererats." — `sources/adventure-wdh.json:2914`
- Campaign: "Leader of the Shard Shunners, based in the Field Ward." (`campaign/setting/notable-figures/independents-adversaries/03-kelso-fiddlewick.md:6`)
- Journal: none for this hostel.

**13. The Blue Mermaid** (clean tavern; run by Mother Jalyth Hlommorath)
> "* The [[Blue Mermaid]]: Clean tavern; run by Mother [[Jalyth Hlommorath]]." — `sources/research/pass3-bundles/dock-ward/wiki.txt:105`
> "| location      = [[Dock Ward of Waterdeep|Dock Ward]], [[Waterdeep]]" — `sources/research/pass3-bundles/dock-ward/wiki.txt:931`
- Campaign: none. Journal: none.

**14. The Chapel of the Steadfast Shield** (Torm chapel; Order of the Gauntlet temple)
> "Torm has one chapel in the city, the Chapel of the Steadfast Shield in the Dock Ward." — `campaign/setting/deities/torm.md:66`
> "**Chapel of the Steadfast Shield (Torm, Dock Ward)**" — `campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:229`
- Runs it: Torm's priests (`campaign/setting/deities/torm.md:66`). Hook: none in the published text. The Order's files list it as a briefing temple (`campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:201`).
- Journal: none.

Also available, outside the 14: the Rusted Anchor ("Find Pell at the Rusted Anchor in the Dock Ward and hold his debt.", `campaign/quests/faction-events/order-of-the-gauntlet/m01-breaking-up-the-brawl/ev-01-breaking-up-the-brawl.md:13`) and Tarrow's Tallow and Wick ("The safe house is the third floor above Tarrow's Tallow and Wick, a chandler's shop at 22 Sail Street in the Dock Ward, a five-minute walk from the fish market.", `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:162`).

## Q3. Characters of Interest

**Istrid Horn** (Shield dwarf moneylender, lawful evil; no pronoun field on the page)
> "# Istrid Horn" — `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:1`
> "- *Shield dwarf moneylender, lawful evil*. Stat block: **Veteran**." — `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:6`
> "- **Affiliation:** Zhentarim (Doom Raiders)" — `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:7`
> Event copy: "Istrid Horn (Lawful Evil, Shield Dwarf, she/her) :: The Doom Raiders' Master of Trade and Coin, who lends from a guarded Dock Ward warehouse and makes every loan sound like a kindness." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:384`

**Krebbyg Masq'il'yr** (Drow gunslinger, chaotic neutral; no pronoun field on the page)
> "# Krebbyg Masq'il'yr" — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:1`
> "- *Drow gunslinger, chaotic neutral*. Stat block: **Drow Gunslinger**." — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:6`
> "A drow gunslinger who operates as "Kreb Sorrush," booking manager of the Seven Masks Theater in the Dock Ward, handles casting inquiries, performance schedules, and other requests with equal efficiency, switching between them mid-sentence." — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:30`

**Esloon Bezant** (Thayan human Red Wizard exile, Neutral, he/him)
> "# Esloon Bezant" — `campaign/setting/notable-figures/independents-allies/16-esloon-bezant.md:1`
> "- *Thayan human Red Wizard exile, Neutral, he/him*. Stat block: **Mage** (CR 6), unmodified." — `campaign/setting/notable-figures/independents-allies/16-esloon-bezant.md:5`
> "Esloon Bezant is a tattooed Thayan expatriate who takes fee-for-service magical work in the Dock Ward, direct and reliable, with a past he does not discuss." — `campaign/setting/notable-figures/independents-allies/16-esloon-bezant.md:29`

**Corene Wyldath** (Halfling spy (compromised), neutral good; no pronoun field on the page)
> "# Corene Wyldath" — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:1`
> "- *Halfling spy (compromised), neutral good*. Stat block: **Spy**." — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:6`
> "Corene is a Harper deep-cover agent embedded in the Dock Ward operation of Xanathar's Guild, the subject of Harper mission five (**The Sleeping Asset**), and the most dangerous kind of asset: one who cannot confirm her own loyalty." — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:26`

**Maxeene** (draft horse, unaligned; the NF field gives no pronoun, the text uses "her")
> "# Maxeene" — `campaign/setting/notable-figures/harpers/08-maxeene.md:1`
> "- *Draft horse with a permanent enchantment that lets her understand and speak Common, unaligned*. Stat block: **Beast (Intelligence 10)**." — `campaign/setting/notable-figures/harpers/08-maxeene.md:6`
> "A grey roan draft mare with a white blaze who works a hire stand off Fillet Lane in the Dock Ward, watching the street with a placid, attentive expression and a great deal to say to anyone who thinks to ask." — `campaign/setting/notable-figures/harpers/08-maxeene.md:30`

**Filthy Meg** (Merfolk, neutral; no pronoun field on the page)
> "# Filthy Meg" — `campaign/setting/notable-figures/independents-adversaries/04-filthy-meg.md:1`
> "- *Merfolk, neutral*. Stat block: **Spy (information broker)**." — `campaign/setting/notable-figures/independents-adversaries/04-filthy-meg.md:6`
> "Filthy Meg is an independent merfolk information broker operating out of Mistshore" — `campaign/setting/notable-figures/independents-adversaries/04-filthy-meg.md:26`

**Soluun Xibrindas** (Drow gunslinger, neutral evil; no pronoun field on the page)
> "# Soluun Xibrindas" — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:1`
> "- *Drow gunslinger, neutral evil*. Stat block: **Drow Gunslinger**." — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:6`
> "**Persona.** To the world, Soluun is a drow gunslinger of Bregan D'Aerthe, disowned for unsanctioned Dock Ward murders." — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:22`

**Grinda Garloth** (Human mage (black market armorer), neutral; no pronoun field on the page)
> "# Grinda Garloth" — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:1`
> "- *Human mage (black market armorer), neutral*. Stat block: **Mage**." — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:6`
> "- **Affiliation:** Independent (contractor to Xanathar's Guild and Bregan D'aerthe)" — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:7`

Plain-text characters (no Notable Figures page):
- **Tarn Hobble** (Neutral, Human, he/him): "Tarn Hobble (Neutral, Human, he/him) :: a Dock Ward fence who sold the Guild's clerks a sighting and would sell them the opposite for a better price." — `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/ev-02-twelve-minutes.md:69`
- **Dobb Ketterly**: "Dobb Ketterly, a dock rat who lodges above a net-maker's in the Dock Ward." — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/ev-02-the-extraction.md:184`
- **Hollen Brask**: "- **Hollen Brask** (Independent): a Dock Ward hauler on Vhaspar's list who must be warned." — `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/overview.md:85`
- **Ostrin Brindle** (Neutral, Waterdhavian Human, he/him): "Ostrin Brindle (Neutral, Waterdhavian Human, he/him) :: a Dock Ward pawnbroker in his sixties who sells the company's people what a licensed shop won't and keeps his books as neatly as a priest." — `campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:278`
- **Harl Pimm** (Lawful Neutral, Waterdhavian Human, he/him): "Harl Pimm (Lawful Neutral, Waterdhavian Human, he/him) :: a stolid Dock Ward constable who counts lamp oil in every theater on his route, drinks Kreb's free tea, and has never in his life seen a drow." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:176`
- **Dhaer Oussen** (he/him): "| Third | Dhaer Oussen (he/him) | Counter clerk at a pawnbroker in the Dock Ward |" — `campaign/quests/faction-events/bregan-daerthe/r10-officer/ev-01-officer.md:153`

## Q4. Temples

No Dock Ward row in the Major Temples table (`sources/adventure-wdh.json:30909-30997`).
- Chapel of the Steadfast Shield (Torm): see Q2 entry 14 (`campaign/setting/deities/torm.md:66`).
- Ilmater: the Dock Ward wiki's "*[[Ilmater's Safe Harbor]], a soup kitchen." (`sources/research/pass3-bundles/dock-ward/wiki.txt:177`) is not a temple. The Ilmater temple row places the Hospice of St. Laupsenn in the North Ward: "Ilmater" / "Hospice of St. Laupsenn" / "North Ward" (`sources/adventure-wdh.json:30943-30945`).
- Conflict (Chapel): "The Dragon Heist table has no Torm row (`sources/adventure-wdh.json:30922-30995`). The only placement is the Order's chapel in the Dock Ward" (`campaign/setting/deities/torm.md:131`). Earlier reference: "The Torm chapel is the Chapel of the Steadfast Shield in the Dock Ward from the First Meeting, not the reference's Chapel of the Faithful Hand in the Trades Ward." (`campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/design-notes.md:19`)

## Q5. Secret

Best candidate: Soluun Xibrindas is the Dock Ward killer, and Bregan D'aerthe's public disownment of him is a cover.
> "The killer is Soluun Xibrindas, a drow gunslinger of Bregan D'aerthe who has hunted the Dock Ward for some weeks. Bregan D'aerthe's public story is that Jarlaxle disowned him for killing without orders. The story is a cover. Jarlaxle knows about the murders and hasn't decided what to do about them, and Soluun carries a forged Bregan D'aerthe token so that the band can deny him if he is caught." — `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md:17`
> "The Doom Raiders look for a killer who is taking elf and half-elf sailors off the Dock Ward's streets." — `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/overview.md:64`

Other hidden-affiliation notes that change play:
- Skewered Dragon: "A dim Dock Ward dive, operated by **Manshoon's Splinter Zhentarim** as an informal ward headquarters." (`campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md:43`)
- Seven Masks Theater: "The Seven Masks Theater appears on every list of Dock Ward Bregan D'aerthe assets the party might assemble from outpost intelligence." (`campaign/guides/factions/08-bregan-daerthe.md:31`)
- Corene Wyldath: "Corene is a Harper deep-cover agent embedded in the Dock Ward operation of Xanathar's Guild" (`campaign/setting/notable-figures/harpers/05-corene-wyldath.md:26`)
- Pier 17: "- **Pier 17:** the barges belong to Xanathar's Guild and carry spoil out of its cargo tunnel under the south quay." (`campaign/quests/faction-events/emerald-enclave/r25-winterstalker/ev-01-winterstalker.md:318`)
- Esloon Bezant: "The Zhents are courting a Red Wizard of Thay named Esloon Bezant, trying to add his gang of thugs to their ranks." (`sources/adventure-wdh.json:3922`)

## Q6. Quests, faction events and location journals set in the Dock Ward

Location journals:
- **Zhentarim Warehouse** (`campaign/locations/zhentarim-warehouse/area-overview.md:23`): "The warehouse sits at the back of a walled yard on Candle Lane."
- **Sea Maidens Faire** (`campaign/locations/sea-maidens-faire/area-overview.md:7`): quoted under Landmark 8.
- **Xanathar Sewer Hideout** (`campaign/locations/xanathar-sewer-hideout/area-overview.md:78`; `q09-private-cellar.md:9`): quoted under Landmarks 9 and 11.
- **Gralhund Villa** (`campaign/locations/gralhund-villa/g12-family-library.md:13`): "We are now certain that the Second Eye was carried from the warehouse in the Dock Ward to Yellowspire in the Castle Ward."

Finding Floon (the quest is set here):
- ev-01 "Volo tells them Floon was last at the Skewered Dragon on Dock Street." (`campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:123`)
- ev-02 "This Exploration Event occurs when the party enters the Dock Ward following Volo's lead." (`campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md:7`)
- ev-03 "This Exploration/Combat Event occurs when the party arrives at the Candle Lane warehouse." (`campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:7`)
- ev-04 "The sewers beneath the Dock Ward lead to a Xanathar's Guild hideout carved into a decommissioned vault." (`campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:133`)
- overview "The sewer hideout — eleven rooms of a decommissioned vault beneath the Dock Ward — held Floon alive in the boss chamber." (`campaign/quests/act-i/finding-floon/overview.md:55`)

Other campaign quests and structure files:
- **Trollskull Alley** (ev-04): "| Doom Raiders | The Dockside Killer | Identify who is killing elf and half-elf sailors in the Dock Ward |" (`campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:75`); (ev-05): "After the final bout, a Guild scout makes contact: professional and direct, offering paid work in the Dock Ward and handing over a token for the Old Xoblob Shop." (`campaign/quests/act-i/trollskull-alley/ev-05-the-field-of-triumph.md:61`)
- **Fireball!** (ev-03): "Three ships: *Heartbreaker* and *Hellraiser* (docked galleons, painted crimson and gold, flying Faire pennants at a pier in the Dock Ward) and the *Eyecatcher* (anchored a quarter-mile out in Deepwater Harbor)." (`campaign/quests/act-ii/fireball/ev-03-the-nimblewright-hunt.md:52`); (ev-04): "### Arrival — The Dock Ward Distraction" (`campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:18`)
- **Gralhund Villa** (structure): "We are now certain that the Second Eye was carried from the warehouse in the Dock Ward to Yellowspire in the Castle Ward." (`campaign/structure/arc-d-gralhund-villa.md:160`)
- **Xanathar's Lair** (structure): "Watch patrol schedules for the sewer approaches to Skullport: three viable windows per day in the Dock Ward drainage network." (`campaign/structure/arc-f-xanathars-lair.md:33`)
- **Faction Outposts** (structure): "*Dock Ward.* — **Street-level entry point for the BD chain.**" (`campaign/structure/arc-e-faction-outposts.md:323`); "elven and half-elven victims found dead in the Dock Ward after Seven Masks Theater performances" (`campaign/structure/arc-h-sea-maidens-faire.md:39`). Pier conflict: `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/design-notes.md:67` (Q9).

Faction events:
- Doom Raiders, The Dockside Killer (m01): "Sit, please, and thank you for coming so promptly." is dialogue; the set-up sentence is "Davil Starsong asks the Doom Raiders to stake out the docks and find the killer before he strikes again." — not used. Use: "A Doom Raiders member who reaches 2nd level receives a flying snake at Trollskull Manor carrying a line in Davil's looping hand." (`campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/overview.md:17`) and "...asks them to find whoever is killing elf and half-elf sailors in the Dock Ward." — the sentence: "He receives the members in his curtained room on the second floor of the Yawning Portal, pours for each of them, and asks them to find whoever is killing elf and half-elf sailors in the Dock Ward." (`...overview.md:17`).
- Doom Raiders, The Missing Snobeedle (m03): "The party can take Dasher's claim to Istrid Horn at her Dock Ward warehouse." (`campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:49`)
- Doom Raiders, Wolf (r03): "The safe house is the third floor above Tarrow's Tallow and Wick, a chandler's shop at 22 Sail Street in the Dock Ward, a five-minute walk from the fish market." (`campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:162`)
- Doom Raiders, Ardragon (r25): "The target waits in the cellar of Istrid Horn's Dock Ward warehouse, unharmed beyond what the taking needed." (`campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:280`)
- Doom Raiders, Dread Lord (r50): "- **Dock Ward:** the loft above Tarrow's Tallow and Wick (a pound of blue-wick tallow)." (`campaign/quests/faction-events/doom-raiders/r50-dread-lord/ev-01-dread-lord.md:178`)
- Doom Raiders, Davil's Return (s02): "Tashlyn takes Skeemo back to the tack room and kills him at dawn, and Yagra's cart carries the body to the Dock Ward harbor before the carters arrive." (`campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:272`)
- Doom Raiders, First Meeting (00): "At 9 a.m. Yagra leads the new members to Istrid's warehouse in the Dock Ward." (`campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:368`)
- Bregan D'aerthe, First Meeting (00): "Until then, leave any order at the box office of the Seven Masks Theater, in the Dock Ward." (`campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:403`)
- Bregan D'aerthe, The Handkerchief and the Girl (m01): "Net Street and Dock Street meet at the edge of the wharves in the Dock Ward, and the parade's noise is only a murmur there." (`campaign/quests/faction-events/bregan-daerthe/m01-the-handkerchief-and-the-girl/ev-01-the-handkerchief-and-the-girl.md:244`)
- Bregan D'aerthe, Three Nights (m03): "Any member can visit the Seven Masks Theater in the Dock Ward at any time during the three days." (`campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:118`)
- Bregan D'aerthe, The Compromised Eye (m04): "The second half of the work happens the next morning in the Dock Ward, where Tarn Hobble keeps a pawnshop on Net and Dock Street." (`campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/ev-02-twelve-minutes.md:59`)
- Bregan D'aerthe, The Theater's Back Room (m05): "Captain Ilsa Dalloway and Constable Harl Pimm (Dock Ward Watch): the officers on crowd duty at the showcase." (`campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/overview.md:82`)
- Bregan D'aerthe, Soldier (r03): "The meeting is at ten bells in the booking office of the Seven Masks Theater in the Dock Ward." (`campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:52`)
- Bregan D'aerthe, Officer (r10): "| Third | Dhaer Oussen (he/him) | Counter clerk at a pawnbroker in the Dock Ward |" (`campaign/quests/faction-events/bregan-daerthe/r10-officer/ev-01-officer.md:153`)
- Bregan D'aerthe, Houseless Noble (r50): "Fel'rekt rows you to a rented boathouse on the Dock Ward waterfront instead of the harbor mooring." (`campaign/quests/faction-events/bregan-daerthe/r50-houseless-noble/ev-01-houseless-noble.md:73`)
- Bregan D'aerthe, Coin Pouches (s01): "The Dock Ward dyer who made it sold black bolts of that weave to six buyers in the last month." (`campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:39`)
- Bregan D'aerthe, Kreb Drops the Cover (s02): "Because a drow booking manager in the Dock Ward would last about a day, darling, and the captain wants the theater to last longer." (`campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:102`)
- Bregan D'aerthe, The Killer's Fate (s05): "Soluun is the drow gunslinger the Doom Raiders meet in **The Dockside Killer**, and until tonight the company's public disownment of him has been a cover story." (`campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:5`)
- Emerald Enclave, The Grells in the Dock Ward (m04): "Flying creatures have taken three people from Pier 17 in the Dock Ward, one on each of three nights." (`campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-01-the-search.md:31`); "The party fights two grells in a Dock Ward warehouse and frees a seamstress from their nest." (`campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-02-the-nest.md:316`)
- Emerald Enclave, First Meeting (00): "My animals watched what you did beneath the Dock Ward." (`campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:129`)
- Emerald Enclave, Doppelganger Problem (m03): "- **Kael** unloads cargo on the Dock Ward quay at dusk, and he says only: "Not my watch, so ask Bonnie yourself. She uses the back room at the Portal after close, and I'd go there."" (`campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:128`)
- Emerald Enclave, Autumnreaver (r10): "- **The Dock Ward route:** the entrance is a sealed hatch in the floor of an abandoned fishmeal warehouse, where a few sacks of old meal still stand by the wall." (`campaign/quests/faction-events/emerald-enclave/r10-autumnreaver/ev-01-autumnreaver.md:271`)
- Emerald Enclave, Winterstalker (r25): "- **Place:** the quays of the Dock Ward and the private piers of the Sea Ward that can be seen from the water." (`campaign/quests/faction-events/emerald-enclave/r25-winterstalker/ev-01-winterstalker.md:292`)
- Emerald Enclave, Water Table Stirs (s02): "- **The sewers:** any aberrant creature met below the Dock Ward during the investigations." (`campaign/quests/faction-events/emerald-enclave/s02-the-water-table-stirs/ev-01-the-water-table-stirs.md:99`)
- Force Grey, The Trouble with Meloon (m03): "Meloon knows a way, so take the sewer junction three tunnels in off the Dock Ward, because the Watch never walks it." (`campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md:222`)
- Force Grey, The Legate's Eyes (m05): "If **Courier Identified** is marked, the party knows Dobb Ketterly's face and the net-maker's loft in the Dock Ward where he lodges." (`campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-01-the-legates-eyes.md:140`)
- Force Grey, Senior Griffon (r10): "You are haggling over a coil of rope at a Dock Ward stall when a dry, flat voice speaks inside your head, fast and clipped and without any greeting." (`campaign/quests/faction-events/force-grey/r10-senior-griffon/ev-01-senior-griffon.md:22`)
- Harpers, The Talking Mare (m01): "Her hire stand is a cobbled yard off Fillet Lane in the Dock Ward." (`campaign/quests/faction-events/harpers/m01-the-talking-mare/ev-01-the-talking-mare.md:18`)
- Harpers, Doppelganger Auditions (m03): "> [!qna]**Tell us about the Dock Ward.**" (`campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:209`)
- Harpers, A Friend's House (m04): "Somebody's doing professional work in those Dock Ward warehouses, friend." (`campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:219`)
- Harpers, The Sleeping Asset (m05): "Corene Wyldath, a Harper Spy living in the Dock Ward as "Halla Ironstave", missed her check-ins three weeks ago, and Mirt wants her found before he decides what to ask of her." (`campaign/quests/faction-events/harpers/m05-the-sleeping-asset/overview.md:17`)
- Harpers, Harpshadow (r03): "**Nella Fen**, chandler, 16 Fillet Lane, Dock Ward. She watches carts, loads and the waterfront." (`campaign/quests/faction-events/harpers/r03-harpshadow/ev-01-harpshadow.md:137`)
- Harpers, Wise Owl (r25): "**Lantern**, Dena Holt: a courier for a Guild warehouse on the Dock Ward waterfront." (`campaign/quests/faction-events/harpers/r25-wise-owl/ev-01-wise-owl.md:153`)
- Lords' Alliance, The Long Watch (m01): "Meet the crew at the Muleskull Tavern, on Ship Street in the Dock Ward, at six bells tomorrow." (`campaign/quests/faction-events/lords-alliance/m01-the-long-watch/ev-01-six-bells-at-the-muleskull.md:41`)
- Lords' Alliance, The Exile's Return (m02): "He was last seen recruiting kenku in the Dock Ward." (`campaign/quests/faction-events/lords-alliance/m02-the-exiles-return/ev-01-the-exiles-return.md:72`)
- Lords' Alliance, The Red Wizard's Price (m03): "The tavern stands on Dock Street in the Dock Ward, a short walk from Fillet Lane." (`campaign/quests/faction-events/lords-alliance/m03-the-red-wizards-price/ev-01-the-red-wizards-price.md:98`)
- Lords' Alliance, The Archer Above (m04): "- **Track 6:** He drops to the lane and reaches his bolt hole, a salt-fish smokehouse on the Dock Ward quay that belongs to no faction." (`campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:229`)
- Lords' Alliance, Stingblade (r10): "- **Guildmaster Piers Hobb**, who leads the Dock Ward haulers' guild, receives the member at the guildhouse on the quay." (`campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:127`)
- Order of the Gauntlet, First Meeting (00): "The three temples are the Halls of Justice, which is the temple of Tyr, the Temple of Helm in the Castle Ward, and the Chapel of the Steadfast Shield, a Torm chapel in the Dock Ward." (`campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:192`)
- Order of the Gauntlet, Breaking Up the Brawl (m01): "Find Pell at the Rusted Anchor in the Dock Ward and hold his debt." (`campaign/quests/faction-events/order-of-the-gauntlet/m01-breaking-up-the-brawl/ev-01-breaking-up-the-brawl.md:13`)
- Order of the Gauntlet, Black Viper (m02): "A net bought at any Dock Ward chandler for 1 gp gives Advantage on the check below." (`campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/ev-02-the-imp-at-dawn.md:83`)
- Order of the Gauntlet, Shard Shunners (m03): "Pell, the Xanathar's Guild dealer from **Breaking Up the Brawl**, can be found at the Rusted Anchor in the Dock Ward." (`campaign/quests/faction-events/order-of-the-gauntlet/m03-the-shard-shunners/ev-01-the-shard-shunners.md:181`)
- Order of the Gauntlet, Spined Devils (m04): "- **The receipt:** The customer copy of a carter's receipt from Garrowby Cartage in the Dock Ward." (`campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/ev-02-what-gysheer-carried.md:111`)
- Order of the Gauntlet, Shrine on Aveen Street (m05): "- **One:** 4 Alturiak, 1483 DR. H.S., a salt warehouse on the Dock Ward quays." (`campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/ev-01-the-shrine-on-aveen-street.md:251`)
- Order of the Gauntlet, Marcheon (r03): "4. A warrant requested for a Dock Ward address and withdrawn the next morning." (`campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:220`)
- Order of the Gauntlet, Vindicator (r25): "Sir Aldous Fenmore, Vindicator. Died in Eleint of 1479 DR at the burning of a Dock Ward warehouse. Operation against diabolism." (`campaign/quests/faction-events/order-of-the-gauntlet/r25-vindicator/ev-01-vindicator.md:231`)
- Order of the Gauntlet, Savra's Past (s02): "That was three years back, friend. A tower full of fools in the Dock Ward, preaching at the wind." (`campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:84`)

## Q7. Culture, defense, politics, economy and lore

**Culture**
> "Frequent complaints arise that these women and men are more citizens of the sea than of the Dock Ward itself." — `sources/adventure-wdh.json:31065`
> "The folk of the Dock Ward take competition seriously, and they frequently draft their champions from the rough-and-tumble sailors who come to the city." — `sources/adventure-wdh.json:31065`

**Defense**
> "The City Guard garrisons the barracks and guards the walls and civic buildings. The Watch patrols the streets, and only a pair of Watch operatives walks the Castle Ward at a time, against eight to twelve in the Dock Ward." — `campaign/gazetteer/waterdeep/castle-ward.md:169`
> "Characters who stir up trouble in the Dock Ward are likely to run into Captain Staget again." — `sources/adventure-wdh.json:2205`

**Politics**
> "The war with Manshoon's Zhentarim is an active, low-level street war in the Dock Ward. It began when Manshoon's envoys came to Skullport three months before the fireball with Eye #1 of the Stone of Golorr, and Xanathar killed them." — `campaign/setting/history/02-the-long-shadow.md:72`
> "The Dock Ward is the Guild's primary surface territory." — `campaign/setting/history/02-the-long-shadow.md:47`
> "| **Xanathar vs. Manshoon** | Active street war — low-level, in the Dock Ward | Manshoon's operatives probe Guild territory, and Xanathar's kill order on Manshoon has failed twice." — `campaign/guides/gm-guide/running-the-villains.md:71` (the row continues in the file)
> "Brawls between the Xanathar's Guild and the Zhentarim have become common in the Dock Ward, and the City Watch is called to them often." — `campaign/setting/history/08-the-players-arrive.md:75`

**Economy**
> "Istrid Horn is a shield dwarf moneylender operating out of a guarded warehouse in the Dock Ward, serving as the Doom Raiders' Master of Trade and Coin." — `campaign/guides/gm-guide/debts-of-the-city.md:37`
> "Istrid offers loans of up to 2,500 gp with an interest rate of 10 percent per tenday." — `sources/adventure-wdh.json:1455` (no ward named; Doom Raiders loan source)

**Lore**
> "Circa [[1368 DR]], an enterprising [[halfling]] [[Joshuan Havabuck]] was involved in numerous schemes and business in the Dock Ward." — `sources/research/pass3-bundles/dock-ward/wiki.txt:96`
> "After the [[Spellplague]], the northern section of Waterdeep harbor became dilapidated with most of the harbor choked with sunken ship hulls. This section became known as [[Mistshore]]." — `sources/research/pass3-bundles/dock-ward/wiki.txt:98`
> "In the words of [[Elminster]] himself, the Dock Ward was a "riotous, nigh-perpetual brawl that covers entire acres, interrupted only by small buildings, intermittent trade businesses, an errant dog or two, and a few brave watchguards, who manage to keep the chaos from spreading beyond the docks; the whole lot wallowing in the stench of rotting fish."" — `sources/research/pass3-bundles/dock-ward/wiki.txt:93`
> "* [[Heartflame]]: A festhall on Snail Street owned by [[Nauloene Tharantra]] before it burned down on the [[Night of Pirates]] in late [[Uktar]], [[1367 DR]], the Year of the Shield." — `sources/research/pass3-bundles/dock-ward/wiki.txt:111`
> "The Dock Ward was long considered the most dangerous district in the city, but the Field Ward has since taken that title." — `sources/adventure-wdh.json:31061`

## Q9. Conflicts (Dock Ward)

1. **Most dangerous.** Published: "The Dock Ward was long considered the most dangerous district in the city, but the Field Ward has since taken that title." (`sources/adventure-wdh.json:31061`). Campaign outline: "the most dangerous ward" (`campaign/setting/waterdeep-lore.md:19`). Wiki: "particularly dangerous" (`sources/research/pass3-bundles/dock-ward/wiki.txt:93`). The campaign outline ranks above the published text under the brief's general rule, but that file is retired in Pass 3. The orchestrator decides.
2. **Courthouse.** Published places a courthouse in the Dock Ward (`sources/adventure-wdh.json:6672`). Campaign Castle Ward: "- **Services:** Magister courts and courthouse cells. City Guard barracks." (`campaign/gazetteer/waterdeep/castle-ward.md:27`).
3. **Xanathar sewer entry.** Castle (`campaign/gazetteer/waterdeep/castle-ward.md:40`), Dock (`campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:133`), Southern (`sources/adventure-wdh.json:11960`). See Southern Q9 item 4.
4. **Shard Shunners' base.** Published Dock Ward: "A narrow passage leads to the cellar of a halfling-owned hostel on Spices Street in the Dock Ward." (`sources/adventure-wdh.json:2914`). Campaign Field Ward: "Leader of the Shard Shunners, based in the Field Ward." (`campaign/setting/notable-figures/independents-adversaries/03-kelso-fiddlewick.md:6`); "The girl was Danika Fiddlewick, fourteen years old, and her brother Kelso leads the Shard Shunners, a gang of halfling wererats in the Field Ward." (`campaign/quests/faction-events/order-of-the-gauntlet/m03-the-shard-shunners/overview.md:21`).
5. **Spouting Fish.** Published Dock Ward (`sources/adventure-wdh.json:2251`) against the wiki Southern Ward (`sources/research/pass3-bundles/southern-ward/wiki.txt:1374`). Quoted under Southern Q2 entry 13.
6. **Sea Maidens Faire pier.** Campaign: "The arc-h structure doc (lines 9, 71) puts the Faire's ships at a Mistshore pier. The Sea Maidens Faire area overview puts them at a Dock Ward private pier." (`campaign/quests/faction-events/bregan-daerthe/m06-the-dive/design-notes.md:67`). Area overview: "The Sea Maidens Faire fleet occupies a private pier in the Dock Ward (Smugglers' Dock area)" (`campaign/locations/sea-maidens-faire/area-overview.md:7`).
7. **Waymoot.** Campaign note: "The source places the Waymoot in the Dock Ward, but the Waymoot is the crossroads in the south of the city, so the meeting is set there." (`campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/design-notes.md:13`). Published text names no ward for the Waymoot (`sources/adventure-wdh.json:31115`).
8. **Istrid's lending location.** Retired `campaign/structure/ch1-beginning.md:172` ("South Ward") against the campaign's Dock Ward (`campaign/quests/faction-events/doom-raiders/r25-ardragon/design-notes.md:23`). Quoted under Southern Q9 item 5.
9. **Mistshore.** Published: "a seedy neighborhood built on a dock in the Dock Ward" (`sources/adventure-wdh.json:6169`); wiki: "the dilapidated north shore of Waterdeep's harbor" (`sources/research/pass3-bundles/dock-ward/wiki.txt:575`). Not a direct contradiction: a neighbourhood in one, a shore in the other.
10. **Temple of Helm and Chapel placement.** Chapel placed in the Dock Ward by the Order files; a Trades Ward reading was rejected (`campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/design-notes.md:19`). See Q4.

---

# FIELD WARD

## Q1. At a Glance

**District type**
> "The '''Field Ward''' of [[Waterdeep]] was an unofficial ward of the city, located between the inner and outer walls on the north side of town. It was in fact the city's slums — possessing the poorest living conditions within the city, was rife with crime, and served as a home to the most destitute Waterdhavian citizens."
> — `sources/research/pass3-bundles/field-ward/wiki.txt:93`

> "Though not an official ward of the city, the Field Ward is commonly referred to as one."
> — `sources/adventure-wdh.json:31104`

> "| type               = City Ward" — `sources/research/pass3-bundles/field-ward/wiki.txt:9` (infobox)

**Boundaries**
> "This district was once a caravan yard between Waterdeep's two northernmost walls, kept free of settlement to serve as a killing field in times of war." — `sources/adventure-wdh.json:31103`
> "The City Watch did not patrol here, but the [[City Guard (Waterdeep)|City Guard]] watched over the road between the inner and outer gates to protect those passing through." — `sources/research/pass3-bundles/field-ward/wiki.txt:98`
> "Aveen Street runs along the line between the Field Ward and the North Ward." — `campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/ev-01-the-shrine-on-aveen-street.md:19`

**Founded**
> "Originally a caravan yard during the 14{{th}} century [[DR]], the Field Ward was the last destination for the many refugees that came to Waterdeep following the [[Spellplague]]." — `sources/research/pass3-bundles/field-ward/wiki.txt:103`
No founding year is given in any source. Published: "As refugees from various calamities settled there after not being allowed into the city's wealthy northern neighborhoods, the area has grown up into a lawless town of its own." (`sources/adventure-wdh.json:31103`)

**Population**: no ward figure (`sources/research/pass3-bundles/field-ward/wiki.txt:18`, blank). Published: none. City-wide figure as in the Southern Ward Q1 entry.

**Lifestyle**
> "The area is a muddy mess, populated by the poorest people and those who take advantage of those folks' desperation." — `sources/adventure-wdh.json:31105`
> "The ward had muddy, unpaved streets and no sanitation services or working [[sewer|sewer system]]." — `sources/research/pass3-bundles/field-ward/wiki.txt:96`

**Services**
> "It has no sewer system and isn't served by the Dungsweepers' Guild-a fact that will be quite evident to your nose if you venture here." — `sources/adventure-wdh.json:31105`
> "The other place you might solicit aid is Endshift Tavern, a popular stop for off-duty members of the City Guard, situated on the corner of Endshift Street and the Breezeway." — `sources/adventure-wdh.json:31106`
> "- **Field Ward Soup Houses.** Three independent kitchens feed about four hundred people a day, and all three are underfunded." — `campaign/quests/faction-events/order-of-the-gauntlet/s01-the-tithe/ev-01-the-tithe.md:99`

**Primary peoples**
> "Many poor [[elves]], half-breeds, servants, homeless squatters and other disregarded Waterdhavians, such as those with obvious deformities, called this district their home." — `sources/research/pass3-bundles/field-ward/wiki.txt:100` (reference tags removed)
> "genuine protectiveness toward the Field Ward homeless population she uses as eyes" — `campaign/setting/notable-figures/independents-adversaries/04-filthy-meg.md:14`

**Languages**: no source fills this field (`sources/research/pass3-bundles/field-ward/wiki.txt:20`, blank).

**Religion**: no source for the Field Ward. Wiki field blank (`sources/research/pass3-bundles/field-ward/wiki.txt:21`). The published table has no Field Ward row (`sources/adventure-wdh.json:30909-30997`).

**Governance**
> "The Watch doesn't patrol this area, however, and many crimes go uninvestigated. The City Guard oversees the Field Ward from the walls around it, but its members get involved only when folk moving into or out of the city are threatened." — `sources/adventure-wdh.json:31104`
> "The City Watch did not patrol here, but the City Guard watched over the road between the inner and outer gates to protect those passing through." — `sources/research/pass3-bundles/field-ward/wiki.txt:98`
> Campaign (conflict in Q9): "Two off-duty Watchmen drink at the Endshift, and the Field Ward watch house will put a dozen Guards in the taproom on the sixth night from the brief, which Kelso will not walk into." — `campaign/quests/faction-events/order-of-the-gauntlet/m03-the-shard-shunners/ev-01-the-shard-shunners.md:23`

**Influences**: no mascot or colours in any source (the published Field Ward entry, `sources/adventure-wdh.json:31092-31107`, has none). `[research]`.

**Architecture**
> "The ward had muddy, unpaved streets and no sanitation services or working sewer system. It was especially crowded, noisy and foul-smelling — stinking of slaughter-houses, tanneries, and waste." — `sources/research/pass3-bundles/field-ward/wiki.txt:96`
> "The Field Ward smells of cookfire smoke and wet earth, and its unpaved lanes wind between crooked buildings that lean on each other for support." — `campaign/quests/faction-events/order-of-the-gauntlet/m01-breaking-up-the-brawl/ev-01-breaking-up-the-brawl.md:93`
> "Aveen Street is a narrow cobbled lane between tanneries and tenements, and the Field Ward side smells of tallow and wet leather." — `campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/ev-01-the-shrine-on-aveen-street.md:97`

**Economy**
> "The Guild of Butchers operates several slaughterhouses, smokehouses, and leather-making facilities in the area-noisome operations that have been pushed out of the city proper." — `sources/adventure-wdh.json:31106`
> "These [[Guild of Butchers|guild]] businesses whose industries were rather offensive to the nose and ears were all relegated to the Field Ward, outside the city proper." — `sources/research/pass3-bundles/field-ward/wiki.txt:96`
> "Kelso Fiddlewick leads the Shard Shunners, a small wererat gang operating out of the Field Ward, and is the most reliable black-market middleman in the ward: direct, dependable, and priced accordingly." — `campaign/setting/notable-figures/independents-adversaries/03-kelso-fiddlewick.md:33`

**Organizations**
> "The guildhall for this guild was the [[Butchers' Guildhall]]," — `sources/research/pass3-bundles/field-ward/wiki.txt:188` (the sentence is cut off in the bundle at "[[Way of t")
> "Kelso Fiddlewick (Shard Shunners): the gang's leader, based in the Field Ward, who keeps every bargain and remembers every slight." — `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:64`
> "The Endshift Tavern was a tavern in the Field Ward in Waterdeep in the late 15th century. It was a frequent stop for off-duty members of the [[City Guard (Waterdeep)|City Guard]]." — `sources/research/pass3-bundles/field-ward/wiki.txt:423`
> "Sella Brant (Lawful Neutral, Waterdhavian Human, she/her) :: the keeper of Three Lanterns House, 7 Windborne Way in the Field Ward, who is home all day." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:93`

Fields with no source: Population (ward figure), Languages, Religion, Influences.

## Q2. Landmarks (10 sourced; fewer than 14 exist)

**1. The Endshift Tavern** (Endshift Street and the Breezeway; City Guard haunt)
> "The other place you might solicit aid is Endshift Tavern, a popular stop for off-duty members of the City Guard, situated on the corner of Endshift Street and the Breezeway." — `sources/adventure-wdh.json:31106`
- Wiki: "The tavern was located on the corner of [[Endshift Street]] and the [[Breezeway]]." (`sources/research/pass3-bundles/field-ward/wiki.txt:426`)
- Campaign: "The Endshift Tavern stands on Endshift Street in the Field Ward and never closes, because the people who drink there work in shifts." (`campaign/quests/faction-events/order-of-the-gauntlet/m03-the-shard-shunners/ev-01-the-shard-shunners.md:100`); "Trevar is behind the bar at any hour." (same line)
- Hook: "Guards at the Endshift Tavern, located on Endshift Street in the Field Ward, are being robbed nightly, and the innkeeper says he's seen giant rats prowling around the back alleys." (`sources/adventure-wdh.json:3976`)
- Journal: none.

**2. The Butchers' Guildhall** (Guild of Butchers base)
> "| leader         = [[Kellatarn Nander]]" — `sources/research/pass3-bundles/field-ward/wiki.txt:128`
> "The guildhall for this guild was the [[Butchers' Guildhall]]," — `sources/research/pass3-bundles/field-ward/wiki.txt:188` (sentence cut off in the bundle)
> The Guild's leader in the mid-14th century: "During the mid-14{{th}} century [[DR]], this title was held by [[Kellatarn Nander]]." — `sources/research/pass3-bundles/field-ward/wiki.txt:171` (template markup kept as written)
- Journal: none.

**3. Thrakkus's butcher shop** (a converted windmill; body disposal for Zhentarim, published)
> "An evil dragonborn named {@creature Thrakkus|wdh} has converted an old, fire-scorched windmill in the Field Ward into a butcher's shop. A member of the Guild of Butchers, {@creature Thrakkus|WDH} has a lucrative side business." — `sources/adventure-wdh.json:13377`
- Campaign: none (no Notable Figures page for Thrakkus).
- Journal: none.

**4. Mudlark Square** (market square; paid mob)
> "Four men were hired to corner a Guild dealer named Pell in Mudlark Square, in the Field Ward, at noon today." — `campaign/quests/faction-events/order-of-the-gauntlet/m01-breaking-up-the-brawl/ev-01-breaking-up-the-brawl.md:34`
- Journal: none.

**5. Twelvedog Court** (court; spined devils)
> "Spined devils in Twelvedog Court, Field Ward, two streets east of the soup house." — `campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/ev-01-twelvedog-court.md:75`
> "I just received a report that spined devils are terrorizing citizens in Twelvedog Court, in the Field Ward." — `sources/adventure-wdh.json:3981`
- Journal: none.

**6. Orros's chandlery on Aveen Street** (Field side of the street; cellar door to the Asmodean shrine)
> "Orros's chandlery stands on the Field Ward side of Aveen Street, and it is open from the second bell to dusk." — `campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/ev-01-the-shrine-on-aveen-street.md:93`
> "A second way in runs through a chandler's cellar on the Field Ward side of the street. Its cellar door stands in the yard, and callers knock on it three times." — `campaign/guides/factions/11-cassalanters.md:25`
- Journal: none.

**7. Three Lanterns House** (Harper keeper's house, 7 Windborne Way)
> "Sella Brant (Lawful Neutral, Waterdhavian Human, she/her) :: the keeper of Three Lanterns House, 7 Windborne Way in the Field Ward, who is home all day." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:93`
- Journal: none.

**8. The Field Ward watch house** (City Guard post; campaign)
> "Two off-duty Watchmen drink at the Endshift, and the Field Ward watch house will put a dozen Guards in the taproom on the sixth night from the brief, which Kelso will not walk into." — `campaign/quests/faction-events/order-of-the-gauntlet/m03-the-shard-shunners/ev-01-the-shard-shunners.md:23`
> "The Watch's Field Ward post sends two Guards an hour later to rope off the court, and the sergeant asks no questions of anyone." — `campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/ev-01-twelvedog-court.md:187`
- Journal: none.

**9. The crocodile tannery** (shuttered tannery in the Field Ward; campaign)
> "A watcher in the Field Ward drew this sketch for me last month. It shows a giant crocodile in the cellar of a shuttered tannery, and I do not know how it came there." — `campaign/quests/faction-events/emerald-enclave/r25-winterstalker/ev-01-winterstalker.md:234`
> "The crocodile site moved from the Southern Ward cisterns to a shuttered tannery in the Field Ward." — `campaign/quests/faction-events/emerald-enclave/r25-winterstalker/design-notes.md:11`
- Journal: none.

**10. The Field Ward soup houses** (three independent kitchens)
> "- **Field Ward Soup Houses.** Three independent kitchens feed about four hundred people a day, and all three are underfunded." — `campaign/quests/faction-events/order-of-the-gauntlet/s01-the-tithe/ev-01-the-tithe.md:99`
- Journal: none.

## Q3. Characters of Interest

**Kelso Fiddlewick** (Lightfoot Halfling wererat, Neutral; no pronoun field on the page)
> "# Kelso Fiddlewick" — `campaign/setting/notable-figures/independents-adversaries/03-kelso-fiddlewick.md:1`
> "- *Lightfoot Halfling wererat, Neutral*. Stat block: **Wererat**, used in halfling form unless a Shunner falls." — `campaign/setting/notable-figures/independents-adversaries/03-kelso-fiddlewick.md:5`
> "- **Affiliation:** Independent (adversary). Leader of the Shard Shunners, based in the Field Ward." — `campaign/setting/notable-figures/independents-adversaries/03-kelso-fiddlewick.md:6`

**Filthy Meg** (Merfolk, neutral; no pronoun field on the page; her Field Ward network is in the NF text)
> "# Filthy Meg" — `campaign/setting/notable-figures/independents-adversaries/04-filthy-meg.md:1`
> "- *Merfolk, neutral*. Stat block: **Spy (information broker)**." — `campaign/setting/notable-figures/independents-adversaries/04-filthy-meg.md:6`
> "**Motivations.** Meg wants accurate intelligence she can sell at the right price, to maintain the independence that makes her genuinely useful, and to keep her Field Ward network fed and overlooked." — `campaign/setting/notable-figures/independents-adversaries/04-filthy-meg.md:16`

Plain-text characters (no Notable Figures page):
- **Thrakkus** (dragonborn butcher): "An evil dragonborn named {@creature Thrakkus|wdh} has converted an old, fire-scorched windmill in the Field Ward into a butcher's shop." (`sources/adventure-wdh.json:13377`); "These homeless sods are too {@condition frightened} of {@creature Thrakkus|wdh} to speak ill of him, and the City Watch doesn't seem to care about crimes committed in the Field Ward." (`sources/adventure-wdh.json:13403`)
- **Justyn** (NE male Illuskan human thug): "Dead-eyed, slack-jawed Justyn (NE male Illuskan human {@creature thug}) grew up in the toughest neighborhood in the Field Ward and has the scars to prove it." (`sources/adventure-wdh.json:4124`)
- **Sabeen** (N female half-orc, Tough): "Handler Sabeen (N female half-orc, Tough) runs child pickpockets from the Field Ward" (`campaign/guides/trollskull-manor/07-events.md:44`)
- **Gysheer Omfreys** (Tethyrian woman in her forties): "Gysheer Omfreys is a Tethyrian woman in her forties who works for Victoro Cassalanter of the Sea Ward." (`campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/overview.md:21`)
- **Pell** (Xanathar's Guild dealer; Mudlark Square): "Four men were hired to corner a Guild dealer named Pell in Mudlark Square, in the Field Ward, at noon today." (`campaign/quests/faction-events/order-of-the-gauntlet/m01-breaking-up-the-brawl/ev-01-breaking-up-the-brawl.md:34`)
- **Darrick Holstan** (night guard): "Darrick Holstan lodges above a farrier's shop three streets from the Endshift and works the docks by day, though he does not appear in this Event." (`campaign/quests/faction-events/order-of-the-gauntlet/m03-the-shard-shunners/ev-01-the-shard-shunners.md:275`)
- **Sella Brant** (Harper keeper, 7 Windborne Way): see Q2 entry 7.

## Q4. Temples

No temple or shrine in the Field Ward appears in any source. The published Major Temples table has no Field Ward row (`sources/adventure-wdh.json:30909-30997`). The Dock Ward Ilmater soup kitchen is not in the Field Ward.

## Q5. Secret

Best candidate: Thrakkus's butcher shop is a Zhentarim body-disposal site (published).
> "Zhents loyal to {@creature Manshoon|WDH} pay {@creature Thrakkus|WDH} to chop up people they kill, and he sells the meat on the sly." — `sources/adventure-wdh.json:13377`
> "The dragonborn allows squatters to dwell in his home. Those who can perform menial chores are spared and fed scraps of cooked meat; the rest end up on the chopping block." — `sources/adventure-wdh.json:13403`
> "If {@creature Manshoon|WDH} is the villain, the stone is brought to {@creature Thrakkus|wdh}, a dragonborn butcher in the Field Ward who chops up bodies for the Zhentarim." — `sources/adventure-wdh.json:6172` (conditional on the chosen villain)

Campaign hidden-affiliation note: "It has also paid three gang leaders to look away when Guild men are hurt, and Pell has noticed." (`campaign/quests/faction-events/order-of-the-gauntlet/m01-breaking-up-the-brawl/ev-01-breaking-up-the-brawl.md:20`) — the sentence is a Splinter fact, not a Field Ward resident fact.

## Q6. Quests, faction events and location journals set in the Field Ward

Location journals: none. `campaign/locations/` holds seven journals and none names the Field Ward.

Campaign quests and events:
- **Trollskull Alley** (ev-04): "| Order of the Gauntlet | Breaking Up the Brawl | Stop a mob hired by the Splinter from cornering a Xanathar's Guild dealer in a Field Ward market square |" (`campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:74`)
- **Order: Breaking Up the Brawl** (m01): "Four men were hired to corner a Guild dealer named Pell in Mudlark Square, in the Field Ward, at noon today." (`...m01-breaking-up-the-brawl/ev-01-breaking-up-the-brawl.md:34`); "### The Field Ward at Noon" (`...ev-01-breaking-up-the-brawl.md:87`)
- **Order: The Shard Shunners** (m03): "Someone is robbing the night guards of the Endshift Tavern on Endshift Street in the Field Ward." (`campaign/quests/faction-events/order-of-the-gauntlet/m03-the-shard-shunners/ev-01-the-shard-shunners.md:94`); "A halfling gang is robbing the night guards of a Field Ward tavern." (`...ev-01-the-shard-shunners.md:434`)
- **Order: Spined Devils in Twelvedog Court** (m04): "Spined devils in Twelvedog Court, Field Ward, two streets east of the soup house." (`campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/ev-01-twelvedog-court.md:75`)
- **Order: The Shrine on Aveen Street** (m05): "Aveen Street runs along the line between the Field Ward and the North Ward." (`campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/ev-01-the-shrine-on-aveen-street.md:19`)
- **Order: Marcheon** (r03): "2. Two watch-houses in the Field Ward that were shuttered after dark for a tenday." (`campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/ev-01-marcheon.md:225`)
- **Order: Vindicator** (r25): "A third knight, Sir Merrick Tollwood, is on duty at the Field Ward gate today." (`campaign/quests/faction-events/order-of-the-gauntlet/r25-vindicator/ev-01-vindicator.md:136`)
- **Order: First Meeting** (00): "There's trouble in the Field Ward that I'll tell you about tomorrow, because the work does not wait." (`campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:311`)
- **Order: The Tithe** (s01): "- **Field Ward Soup Houses.** Three independent kitchens feed about four hundred people a day, and all three are underfunded." (`campaign/quests/faction-events/order-of-the-gauntlet/s01-the-tithe/ev-01-the-tithe.md:99`)
- **Doom Raiders, The Missing Snobeedle** (m03): "Blossom goes to the Field Ward the next morning." (`campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:359`); "Kelso Fiddlewick (Shard Shunners): the gang's leader, based in the Field Ward, who keeps every bargain and remembers every slight." (`campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:64`)
- **Emerald Enclave, Doppelganger Problem** (m03): "You'll want the buyer too. Kelso Fiddlewick, in the Field Ward, a halfling with a scar along his jaw." (`campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:245`)
- **Emerald Enclave, Summerstrider** (r03): "The Undercliff animals will not cross the north fields at dusk. The chalk circle in the north fields is cold and empty. Nobody has come back to it." (`campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:191`, the read-aloud if **Splinter Site Reported** is marked)
- **Emerald Enclave, Winterstalker** (r25): "A watcher in the Field Ward drew this sketch for me last month." (`campaign/quests/faction-events/emerald-enclave/r25-winterstalker/ev-01-winterstalker.md:234`)
- **Harpers, The Sleeping Asset** (m05): "the keeper of Three Lanterns House, 7 Windborne Way in the Field Ward, who is home all day." (`campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:93`)
- **Trollskull Manor staff** (guide): "DC 16 Investigation of the Field Ward reference reveals it is a Xanathar's Guild front." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`)
- **Trollskull Manor events** (guide): "Handler Sabeen (N female half-orc, Tough) runs child pickpockets from the Field Ward" (`campaign/guides/trollskull-manor/07-events.md:44`)
- **Founders' Day feast** (published): "while one hundred of Waterdeep's poorest residents-most brought from the Field Ward-gather under pavilions set up on the lawn." (`sources/adventure-wdh.json:22916`)
- **Cassalanter charity**: "Ammalia's charity in the Field Ward feeds hundreds." (`campaign/setting/history/05-a-debt-in-blood.md:59`); "The Waukeentide Charity Ball (Tarsakh 7) is a fundraiser for Field Ward reconstruction and the main social entry point." (`campaign/setting/deities/waukeen.md:86`)
- **Cassalanter (Gysheer's cellar)**: "For a tenday she has been readying a cellar on Aveen Street for a larger working, and Victoro has told her to keep the Field Ward frightened and the Watch busy elsewhere." (`campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/overview.md:21`)

## Q7. Culture, defense, politics, economy and lore

**Culture**
> "The area is a muddy mess, populated by the poorest people and those who take advantage of those folks' desperation." — `sources/adventure-wdh.json:31105`
> "A word to the wise: being friendly with a burly fellow who is good with a knife is one of your best defenses in the Field Ward." — `sources/adventure-wdh.json:31106`
> "This district was once a caravan yard between Waterdeep's two northernmost walls, kept free of settlement to serve as a killing field in times of war." — `sources/adventure-wdh.json:31103`

**Defense**
> "The City Guard oversees the Field Ward from the walls around it, but its members get involved only when folk moving into or out of the city are threatened." — `sources/adventure-wdh.json:31104`
> "Though the guards might not be inclined to assist you, your status as a visitor to Waterdeep technically obliges them to help you reach the city proper in safety." — `sources/adventure-wdh.json:31106`

**Politics**
> "Because neither are official wards of the city, they aren't subject to taxation." — `sources/adventure-wdh.json:30444`
> "Note, however, that because both these areas have yet to be formally accepted as wards of the city, they don't benefit from the securities of Guild Law or the protection of the Watch." — `sources/adventure-wdh.json:30444`

**Economy**: quoted in Q1 (the butchers, the Guild of Butchers, and the slaughterhouses).

**Lore**
> "Originally a caravan yard during the 14th century DR, the Field Ward was the last destination for the many refugees that came to Waterdeep following the Spellplague." — `sources/research/pass3-bundles/field-ward/wiki.txt:103` (template markup removed in this copy; the exact line is quoted in Q1)
> "This district was once a caravan yard between Waterdeep's two northernmost walls, kept free of settlement to serve as a killing field in times of war." — `sources/adventure-wdh.json:31103`

## Q8. Field Ward only: outside the city proper, the Waymoot, Undercliff, guilds and farmland, and the Watch

Why the published adventure files it outside the city proper:
> "There's more to the city of Waterdeep than just the wards within its walls. If you have need to visit the environs of the city, here's what you'll need to know." — `sources/adventure-wdh.json:31096` (section heading at `sources/adventure-wdh.json:31092`: `"name": "Outside the City Proper",`)
> "Though not an official ward of the city, the Field Ward is commonly referred to as one." — `sources/adventure-wdh.json:31104`
> "Because neither are official wards of the city, they aren't subject to taxation." — `sources/adventure-wdh.json:30444`

Wiki on the same point: "These [[Guild of Butchers|guild]] businesses whose industries were rather offensive to the nose and ears were all relegated to the Field Ward, outside the city proper." (`sources/research/pass3-bundles/field-ward/wiki.txt:96`)

The Waymoot:
> "The place where the High Road and the Way of the Dragon meet in the south of the city is called the Waymoot." — `sources/adventure-wdh.json:31115`
> "Created by the Watchful Order of Magists and Protectors and funded by local merchants, the signpost magically directs travelers to well-known distant locations when the names of those locations are spoken into a crystal on the post." — `sources/adventure-wdh.json:31115`
> "Unfortunately for newcomers, the Waymoot is of no use whatsoever in finding locations within Waterdeep." — `sources/adventure-wdh.json:31116`

Undercliff (farmland and guilds east of the city):
> "This area of rolling grassland and small wooded areas east of the city is a rural community focused on farming and animal husbandry, and which caters to travelers." — `sources/adventure-wdh.json:31125`
> "It is also the site of a large and well-protected training camp for the City Guard, and a prison farm run by the City Watch (called Amendsfarm) where those convicted of minor offenses work off their debt to the city." — `sources/adventure-wdh.json:31125`
> "That said, many canny visitors with business for a month or a season betimes avail themselves of the hospitality of inns in Undercliff, the pleasant farmland east of the city proper." — `sources/adventure-wdh.json:30444`

How the Watch and the city government reach it:
> "The Watch doesn't patrol this area, however, and many crimes go uninvestigated. The City Guard oversees the Field Ward from the walls around it, but its members get involved only when folk moving into or out of the city are threatened." — `sources/adventure-wdh.json:31104`
> "The City Watch did not patrol here, but the City Guard watched over the road between the inner and outer gates to protect those passing through." — `sources/research/pass3-bundles/field-ward/wiki.txt:98`
> Campaign: "The Watch's Field Ward post sends two Guards an hour later to rope off the court, and the sergeant asks no questions of anyone." (`campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/ev-01-twelvedog-court.md:187`)
> Undercliff prison farm: "a prison farm run by the City Watch (called Amendsfarm)" (`sources/adventure-wdh.json:31125`)

## Q9. Conflicts (Field Ward)

1. **Watch patrol.** Published: "The Watch doesn't patrol this area, however, and many crimes go uninvestigated." (`sources/adventure-wdh.json:31104`). Campaign: "the Field Ward watch house will put a dozen Guards in the taproom" (`campaign/quests/faction-events/order-of-the-gauntlet/m03-the-shard-shunners/ev-01-the-shard-shunners.md:23`) and "The Watch's Field Ward post sends two Guards an hour later" (`campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/ev-01-twelvedog-court.md:187`). The campaign's posts are Guard and Watch posts in the ward; the published text says the Watch does not patrol. Both quoted for the orchestrator.
2. **Shard Shunners base.** Published Dock Ward Spices Street hostel (`sources/adventure-wdh.json:2914`). Campaign Field Ward (`campaign/setting/notable-figures/independents-adversaries/03-kelso-fiddlewick.md:6`). Quoted under Dock Ward Q9 item 4.
3. **Most dangerous.** Published: "The Dock Ward was long considered the most dangerous district in the city, but the Field Ward has since taken that title." (`sources/adventure-wdh.json:31061`). Campaign outline: "the most dangerous ward" (`campaign/setting/waterdeep-lore.md:19`) on the Dock Ward. Quoted under Dock Ward Q9 item 1.
4. **Field Ward's northern placement.** Wiki: "on the north side of town" (`sources/research/pass3-bundles/field-ward/wiki.txt:93`). Published: "between Waterdeep's two northernmost walls" (`sources/adventure-wdh.json:31103`). Compatible; both quoted.
5. **Ward status.** Wiki infobox: "| type               = City Ward" (`sources/research/pass3-bundles/field-ward/wiki.txt:9`). Published: "Though not an official ward of the city, the Field Ward is commonly referred to as one." (`sources/adventure-wdh.json:31104`). The wiki's own text says "an unofficial ward of the city". Consistent in substance; only the infobox wording differs.

---

# NOT FOUND (searches run, by ward)

Searched: the four bundle files for each slug; the seven `campaign/locations/` folders; `campaign/setting/notable-figures/`, `campaign/setting/organizations/`, `campaign/setting/deities/`, `campaign/quests/`, `campaign/structure/`, `campaign/guides/`, `campaign/gazetteer/`; `sources/adventure-wdh.json`; `sources/Appendix_B_-_Player_Factions.md` (for Phaulkonmere only).

- **Southern Ward**: ward population, lifestyle, languages, dominant faith, ward government, Watch post, mascot beyond the mule, ward-specific founding year; Kolat Towers and Helm's Hall in any wiki bundle; Phaulkonmere in any wiki bundle; Notable Figures for Vaelle Lurval, Volkarr Kibbens, Brimel Crestfall and the Larkhaven halflings (none exists); location journals for Phaulkonmere, the Converted Windmill, Kolat Towers, the Southern Xanathar hideout and the Dusty Ladle.
- **Dock Ward**: ward population, languages, dominant faith, a ward governance body, a Dock Ward-wide boundary paragraph, a Dock Ward landmark list in the published Chapter 9 (31057-31066 names none); Notable Figures for Tarn Hobble, Dobb Ketterly, Hollen Brask, Ostrin Brindle, Harl Pimm, Dhaer Oussen; location journals for the Skewered Dragon, Old Xoblob Shop, Muleskull Tavern, Seven Masks Theater, Istrid's warehouse, Mistshore, Pier 17, the Spices Street hostel and the Chapel of the Steadfast Shield.
- **Field Ward**: ward population, lifestyle beyond the published lines, languages, religion (no temple in any source), mascot and colours, a Field Ward governance body, a Field Ward founding year, the Guild of Butchers' base location beyond "[[Way of t" (cut off in `sources/research/pass3-bundles/field-ward/wiki.txt:188`), Notable Figures for Thrakkus, Sabeen, Gysheer, Pell and Justyn (none exists).

# NOT READABLE

None. The bundle files, campaign files, Notable Figures pages and `sources/adventure-wdh.json` all opened. The `.docx` files in `sources/Other remix files/` were not consulted; none of the three wards' questions named them.
