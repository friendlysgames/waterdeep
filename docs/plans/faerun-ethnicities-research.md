# Faerûn human ethnicities: source research for Waterdeep NPC labels

Research date: 2026-11-18. Topic: human ethnicities in Faerûn and on the Sword Coast; the population Waterdeep draws on; how Dragon Heist labels its NPCs; name patterns by ethnicity; and the labels the campaign already uses.

**Method.** Every quote was copied from a tool result. Line numbers come from Grep or Read output. In `book-frhof.json`, `book-scag.json` and `adventure-wdh.json` each line is one JSON paragraph or field. In the wiki bundles, numbers are lines of `wiki.txt`. In campaign and gazetteer files, numbers are markdown lines. JSON escapes such as `–` are kept as they appear in the file. In the Dragon Heist label table, pipe characters inside `{@creature …|…}` tags are escaped as `\|` so the table renders. Table rows quote the exact label fragment; the full sentence or paragraph is at the cited line.

**Ranking used.** FRHoF (2025) first, then SCAG, then Dragon Heist (WDH), then the campaign's current files, then the Alexandrian appendices, then the pass-3 wiki bundles (extra, lowest). The campaign files are the remix's current state, not canon.

---

## Ethnicity list

### A. Named or described in FRHoF (`sources/5etools/book/book-frhof.json`)

FRHoF's "Humans" section (heading at line 548) gives the general picture first.

**Human culture in general**
> "The history of the Forgotten Realms has largely been written by humans. Because humans are so numerous, most settlements, factions, and institutions in Faerûn are made up mostly of humans, even if their leadership is another species. But the simple fact that humans are so numerous belies their countless cultural divisions. Human culture varies widely from one realm to another. They speak dozens of different languages and war on each other more than any other species."
> — `sources/5etools/book/book-frhof.json:552`

**"Diverse Ethnicities" (FRHoF section 02d, heading at line 576)**
> "War and trade have spread humans across Faerûn. The cataclysmic war between the {@area Narfell empire|197|x} and the Raumathar people scattered refugees throughout the east. The Raumathar became the Rashemi, settling in the {@area Arcane Empires|16f|x}, while survivors from Narfell settled around the Sea of Fallen Stars and became the Damarans."
> — `sources/5etools/book/book-frhof.json:580`

> "In the west, Chondathan humans established trade routes and settlements, their culture changing rapidly from one region to the next. Humans along the {@area Sword Coast|219|x} formed the seafaring Illuskan culture while, to their south, humans escaping the tyranny of genie overlords became the {@area Calishites|1cf|x}. Some human ethnicities even originate from other worlds and were brought to Faerûn by magic."
> — `sources/5etools/book/book-frhof.json:581`

The FRHoF origin sentences above are the only passage in the book that names the human ethnicities as ethnicities. The other "ethnic" hits are under Not found.

**Chondathan**
- Region: "In the west" (line 581). FRHoF names the Chondath realm: "Chondath was once a large and powerful realm comprising all of the southern {@area Vilhon Reach|256|x}, with distant colonies in the land now known as {@area Sembia|1be|x}." (`book-frhof.json:5268`)
- Language row, lines 1750–1751 (Standard Languages table): `"{@language Chondathan|FRHoF}"`, `"Chondath"`.
- Sword Coast languages: `"entry": "Chondathan"` (line 4381).

**Illuskan**
- Region: "Humans along the Sword Coast formed the seafaring Illuskan culture" (line 581). Language row, lines 1800–1801: `"{@language Illuskan|FRHoF}"`, `"The North"`.
- The North languages: `"entry": "Bothii, Chondathan, Illuskan, Reghedjic"` (line 3739).

**Calishite (FRHoF uses "Calishites" for the people and "Calimshan" for the realm)**
- Origin sentence at line 581 (quoted above).
- Calimshan section (heading at line 3491): "While Calishites of the desert and other wilderness areas rely on genie magic for survival, inhabitants of Calimport have instead embraced and improved on innovations from {@area Lantan|238|x}, resulting in a new wave of {@item Mechanical Wonder|FRAiF|Mechanical Wonders} that have transformed city life." (`book-frhof.json:3495`)
- Nykkar: "The Marching Mountains house the remains of the First Necropolis of Nykkar: an ancient site where early Calishites prepared their revered dead for burial." (`book-frhof.json:3548`)
- Language row, lines 1735–1736 (Alzhedo, origin "Calimshan"): `"{@language Alzhedo|FRHoF}"`, `"Calimshan"`. Lands of Intrigue languages: `"entry": "Alzhedo, Chondathan"` (line 3343).

**Damaran**
- Origin sentence at line 580 (quoted above). Damara region: "In Damara, hardy folk from many backgrounds work together to turn rocky soil into tillable farmland or extract bloodstone from the mountains to the west." (`book-frhof.json:2724`)
- Language row, lines 1760–1761: `"{@language Damaran|FRHoF}"`, `"Damara"`. Forgotten Lands languages: `"entry": "Damaran"` (line 2654). Heartlands languages: `"entry": "Chondathan, Damaran"` (line 2968).

**Rashemi**
- Origin sentence at line 580 (quoted above). Arcane Empires languages: `"entry": "Aglarondan, Rashemi, Thayan"` (line 2263).
- Language row, lines 1830–1831: `"{@language Rashemi|FRHoF}"`, `"Rashemen"`.

**Tethyrian (FRHoF gives a realm, not an ethnicity)**
- FRHoF has no sentence describing Tethyrians as a people. The Tethyr realm entry reads: "Tethyr is a feudal realm of lords and vassals, and its royal line appeals to the divine patronage of Siamorphe, a demigod of nobility, to assert its right to rule." (`book-frhof.json:3577`)
- The only other "Tethyrian" hit is in a Five Lions passage: "They have perpetuated a rumor that the inn is haunted by the restless spirits of Tethyrian dead, and this provides cover for their activities, including magical instruction and experimentation." (`book-frhof.json:5368`)

**Ulutiun**
> "The Great Glacier originally formed from the ice necklace of the deity Ulutiu. The people who call this vast territory home are the Ulutiuns. Few southerners have ever interacted with them. Most outsiders who dare tread these arctic wastes instead encounter fierce monsters adapted to the glacier—white dragons, remorhazes, and even ice devils. The latter are said to be servants of an ancient and mighty priest of Auril who styles herself \"the Ice Queen.\""
> — `sources/5etools/book/book-frhof.json:2787` (within the Forgotten Lands section, heading at line 2627)

**Nar**
> "The ruins of two ancient empires—Narfell, home to demon worshipers, and Raumathar, known for its battle mages—dot the plains where nomadic horse riders now roam, offering abundant opportunities for brave deeds and exploration. The Nars don't care about dynasties or family lines. Rather, they believe actions speak for themselves. This sensible attitude also explains most riders' preference to avoid the demon-cursed ruins of ancient Narfell. However, some now dwelling on the plains wish to reclaim ancient Narfell's powerful, sinister magic for a new generation of Nar demonologists."
> — `sources/5etools/book/book-frhof.json:2814` (Narfell section, heading at line 2810)

> "The peaty soil has preserved the ruins of elven and Nar cities."
> — `sources/5etools/book/book-frhof.json:2758` (Dunwood)

**Turami (FRHoF gives a language, not an ethnicity)**
- FRHoF is silent on Turami as a people. Language row, lines 1850–1851: `"{@language Turmic|FRHoF}"`, `"Turmish"`. Vilhon Reach languages: `"entry": "Chondathan, Shaaran, Turmic"` (line 5198).

**Mulan: FRHoF silent.** The word "Mulan" does not appear in FRHoF. The people of Mulhorand are "Mulhorandi" (see section D).

**Shou: FRHoF silent.** The only FRHoF hit is a district name: "The Nine Golden Swords has a strong foothold in Westgate, where they're based out of the city's Shou District." (`book-frhof.json:9306`)

**Chultan: FRHoF silent.** No FRHoF line uses "Chultan" as an ethnicity.

### B. SCAG "Human Ethnicities in Faerûn" (`sources/5etools/book/book-scag.json`, heading at line 6074)

The section has no table. It has ten named entries, each with a region line and a name line.

> "Humans dwell in every corner of Toril and encompass a full range of cultures and ethnicities. Along the Sword Coast and across the North, humans are the most pervasive of the races and in many places the most dominant. Their cultural and societal makeup runs the gamut, from the cosmopolitan folk who reside in great cities such as Baldur's Gate and Waterdeep to the barbarians who rage throughout the Savage Frontier."
> — `sources/5etools/book/book-scag.json:6069`

> "It follows, then, that the most common feature of humans is their lack of commonality. This diversity has enabled human civilizations to grow faster than those of other races, making humans one of the dominant races in much of the world today. It has also led to conflicts between communities of humans because of their cultural and political differences. If not for their penchant for infighting, humans would be even more populous and predominant than they already are."
> — `sources/5etools/book/book-scag.json:6071`

> "Nine human ethnicities in Faerûn are detailed in the Player's Handbook. Several other noteworthy groups of humans are discussed here. Some are significant minorities in regions or nations that border the North, while others are prevalent in parts of the world far from the Sword Coast."
> — `sources/5etools/book/book-scag.json:6078`

The Player's Handbook is not among the files provided, so the nine PHB ethnicities cannot be named from these sources.

**Arkaiun** (entry lines 6084–6085)
> "Short in stature with tan skin and dark hair, the Arkaiuns dwell primarily in Dambrath as well as Halruaa and the Shar. Many Arkaiuns lived under the yoke of drow slavery centuries ago after a failed military campaign against the dark elves, which led to the eventual destruction of the Arkaiun kingdom in Dambrath."
> — `sources/5etools/book/book-scag.json:6085`

**Bedine** (6101–6102)
> "Dark-skinned and dark-haired, the Bedine were warriors and nomads in southern Anauroch. Once divided into over a hundred tribes, the clannish Bedine mostly kept to their desert lands and interacted little with outsiders, except for trading. Over the generations, more Bedine have become city dwellers, leaving behind their nomadic ways, and reducing the number of tribes that still espouse their traditional way of life."
> — `sources/5etools/book/book-scag.json:6102`

**Ffolk** (6118–6119)
> "The Ffolk of the Moonshae Isles are descended from Tethyrian settlers who came to the isles a thousand years ago. The Ffolk have a deep respect for nature, and are primarily farmers, worshiping the goddess they call the Earthmother and keeping to old druidic ways. Ffolk shipwrights are well regarded, having proven their ability to build sturdy ships that are capable of weathering the tumultuous seas around their home."
> — `sources/5etools/book/book-scag.json:6119`

**Gur** (6135–6136)
> "Related to the Rashemi, Gurs are stout, dusky-skinned, and dark-haired. They consider themselves \"children of Selûne,\" and most of them revere the moon goddess. Gur communities live a nomadic existence wandering the Western Heartlands, leading others to refer to them as \"the people of the highway.\""
> — `sources/5etools/book/book-scag.json:6136`

**Halruaan** (6153)
> "The people of the mysterious and magical kingdom of Halruaa, the Halruaans are touched by magic, and many of them are talented in the Art. They and their land vanished during the Spellplague, but just as mysteriously returned after the second Sundering. Most Halruaans have blond or dark hair and olive complexions. Black, brown, and green eyes are the most common."
> — `sources/5etools/book/book-scag.json:6153`

**Imaskari** (6170)
> "An uprising of Mulan slaves brought about the ruin of Imaskar and its ruling wizards thousands of years ago, but some Imaskari survived and fled into the Underdark. There they changed, developing the pale, smooth skin and whitish hair now common among them. The Imaskari who dominated the region of Mulhorand have been forced into exile by a second uprising of those they dominated."
> — `sources/5etools/book/book-scag.json:6170`

**Nar** (6187)
> "More than a thousand years ago, the dark priests of Narfell amassed great power by treating with demons, but their actions eventually brought about a war that destroyed their civilization. The Nars abandoned their ruined and accursed cities and became nomads and traders. Nars have tanned skin, brown or black eyes, and black hair, often worn long and tied in a tail or topknot."
> — `sources/5etools/book/book-scag.json:6187`

**Shaaran** (6204)
> "Dark-haired and tan-skinned nomads from southern Faerûn, the Shaarans are skilled hunters, archers, and riders who revere various nature deities. They are organized into clans under the direction of elders and chieftains."
> — `sources/5etools/book/book-scag.json:6204`

**Tuigan** (6221–6222)
> "A nomadic horde from the vast plains between Faerûn and Kara-Tur, the Tuigans once nearly conquered Faerûn under the great leader Yamun Khahan before being defeated by a coalition of armies. Since those days, Tuigans are sometimes seen on the Sword Coast and in other nearby regions, but not in great numbers."
> — `sources/5etools/book/book-scag.json:6221`

> "The Tuigans resemble the Shou, with a bronze or golden cast to their skin and dark hair, but they tend to have darker skin and broader features. Each has only a single name (sometimes handed down from one's parent); Tuigans don't use surnames. No strangers to travel, Tuigan traders and adventurers are often familiar with many languages and cultures."
> — `sources/5etools/book/book-scag.json:6222`

**Ulutiun** (6239)
> "The Ulutiuns are short, dark-haired, golden-skinned people who originated in northern Kara-Tur and migrated westward to Icewind Dale and other cold lands near the Endless Ice Sea. Hunters and gatherers, Ulutiuns live in small tribes that have managed to survive in one of the harshest environments in the world. Each has only a single name (sometimes handed down from one's parent); Ulutiuns don't use surnames."
> — `sources/5etools/book/book-scag.json:6239`

**Language option in SCAG** (`book-scag.json:6253`)
> "Many human ethnicities and nations in Faerûn have their own language, in addition to Common. Most human languages are written in Thorass, the alphabet of Old Common, derived from the Chondathan language that traders used as their common tongue. A few human languages use other alphabets, including Draconic, Dethek, and Espruar. The languages of the ethnicities described in the Player's Handbook and this book are as follows:"

The list items (name line, then language line): Arkaiun → "Dambrathan (written in Espruar)" (6260–6261); Bedine → "Midani" (6265–6266); Calishite → "Alzhedo" (6270–6271); Chondathan → "Chondathan" (6275–6276); Damaran → "Damaran (written in Dethek)" (6280–6281); Ffolk → "Waelan" (6285–6286); Gur → "Guran (a patois of Roushoum and Rashemi)" (6290–6291); Halruaan → "Halruaan (written in Draconic)" (6295–6296); Illuskan → "Illuskan" (6300–6301); Imaskari → "Roushoum" (6305–6306); Mulan → "Chessentan, Mulhorandi, Untheric, or Thayan" (6310–6311); Nar → "Damaran" (6315–6316); Rashemi → "Rashemi" (6320–6321); Shaaran → "Shaaran (written in Dethek)" (6325–6326); Shou → "Shou" (6330–6331); Tethyrian → "Chondathan" (6335–6336); Tuigan → "Tuigan" (6340–6341); Turami → "Turmic" (6345–6346); Ulutiun → "Uluik" (6350–6351).

Chultan has no entry in this list. The option closes with: "If your Dungeon Master allows this option, then any human from an ethnic group that has its own language is assumed to know that language as well as Common. This ethnic language is treated as a free additional language for such individuals." (`book-scag.json:6355`)

### C. Other SCAG ethnicity mentions (outside the human section)

- **Mulan:** "Since the Chosen of the gods began to appear in the last few years, Mulhorand has become a land transformed. Its deities manifested fully in the forms of some of their descendants, and swiftly rallied the Mulan to overthrow the Imaskari." (`book-scag.json:397`) and "For the first time in centuries, the people in Mulhorand are free, with the gods declaring that slavery shall no longer be practiced among the Mulan since their return." (`book-scag.json:398`)
- **Illuskan:** "Much closer to Faerûn are the Whalebones and Ruathym, ancient homes of the ancestors of the Illuskan people, and the Moonshaes, where many of those same people now share the islands with the Ffolk and an elf offshoot known as the Llewyr." (`book-scag.json:111`) and "The island of Ruathym is the ancestral homeland of all the Northlanders who live on the islands of the Sea of Swords and the humans who would go on to found old Illusk, now Luskan, and spread out as the Illuskan people." (`book-scag.json:4013`)
- **Illuskan (High Moor):** "They aren't Uthgardt or related to them, but they might have some distant ties to the Northlanders, as they seem to be of Illuskan stock." (`book-scag.json:4767`)
- **Rashemi:** "A harsh, cold land filled with hardy folk, Rashemen is a fiercely traditional nation." (`book-scag.json:407`)
- **Shou:** "Far to the east, past the wastes of the Hordelands, lie the empires of Shou Lung, Kozakura, Wa, and the other lands of the vast continent of Kara-Tur." (`book-scag.json:499`)
- **Tethyrian and Illuskan (half-elves):** "Most of the half-elves in the North and along the Sword Coast are of moon elf heritage mixed with Illuskan or Tethyrian blood." (`book-scag.json:6613`)
- **Calishite (Baldur's Gate):** "A walled Calishite district has grown up to the east of the city proper, known by Baldurians as Little Calimshan." (`book-scag.json:3163`) This is Baldur's Gate, not Waterdeep.
- **Chultan:** "Eastward along the Chultan peninsula lie the remains of Thindol and Samarach." (`book-scag.json:243`) Geography only.
- **Amnian:** "Shrewd traders and ruthless in business, Amnians believe that the end of a successful transaction is justified by any means, ethical or otherwise." (`book-scag.json:222`)
- **Cormyrean:** "Cormyreans are justly proud of their homeland, and go to great lengths to guard it and its honor." (`book-scag.json:338`)

### D. Realm-people terms in FRHoF (not SCAG's human-ethnicity entries)

FRHoF uses these as language or realm names. They are listed because the caller's list may need them.
- **Mulhorandi:** "All Mulhorandi, from blue-blooded nobles to common street peddlers, heed their god-kings' wishes in every aspect of daily life." (`book-frhof.json:4218`). Language row, lines 1815–1816: `"{@language Mulhorandi|FRHoF}"`, `"Mulhorand"`.
- **Thayan:** "Thay began as a colony of the distant Mulhorandi empire, and Delhumide was Thay's capital." (`book-frhof.json:2580`). Language row, lines 1845–1846: `"{@language Thayan|FRHoF}"`, `"Thay"`.
- **Netherese:** language row, lines 1820–1821: `"{@language Netherese|FRHoF}"`, `"Netheril"`.
- **Chessentan:** "Chessentans revel in war the way other cultures delight in sports or feasting." (`book-frhof.json:4171`). Language row, lines 1745–1746: `"{@language Chessentan|FRHoF}"`, `"Chessenta"`.
- **Untheric:** language row, lines 1855–1856: `"{@language Untheric|FRHoF}"`, `"Unther"`.
- **Sespech:** language row, lines 1840–1841: `"{@language Sespech|FRHoF}"`, `"Sespech"`.
- **Lantanese:** language row, lines 1805–1806: `"{@language Lantanese|FRHoF}"`, `"Lantan"`.
- **Bothii, Reghedjic, Midani:** language rows, lines 1740–1741 (`"Uthgardt nomads"`), 1835–1836 (`"Reghed nomads"`), 1810–1811 (`"Bedine nomads"`).
- **Amnian:** "No realm in Faerûn is wealthier than Amn. Unlike their neighbors—which pursue wealth for the comfort it brings—Amnians seek and spend wealth as a symbol of status." (`book-frhof.json:3414`)
- **Sembian:** "Sembians relish the art of negotiation, and coins create friendships fast here." (`book-frhof.json:3253`)
- **Dambrathan (SCAG):** `"entry": "Dambrathan (written in Espruar)"` (`book-scag.json:6261`), the Arkaiun language.

### E. Wiki-only terms (extra source, lowest rank)

The pass-3 wiki bundles give ethnicity fields for some pages. These are not in FRHoF or SCAG.
- **Tashalan** (Tashalar country, not Waterdeep): `{{Split table|rca=right|caption=Human ethnicities|[[Tashalan]]s|83%|[[Calishite]]s|12%|[[Chultan (ethnicity)|Chultans]]|3%|[[Shaaran]]s|1%|Other|1%}}` (`sources/research/pass3-bundles/code-legal-and-magisters/wiki.txt:860`), on the page named by `| name               = Tashalar` (`wiki.txt:847`).
- **Vaasan:** `| ethnicity      = [[Vaasan]]<ref>{{Cite web/theedverse/2018-02-21 - Manshoon's appearance and heritage}}</ref>` (`code-legal-and-magisters/wiki.txt:582`, page "Manshoon").
- **Raurinese:** `| ethnicity      = [[Raurinese]]` (`code-legal-and-magisters/wiki.txt:1207`, page "Halaster Blackcloak"; the same value at `undermountain-and-skullport/wiki.txt:800`).

---

## What Waterdeep draws on (quoted)

No FRHoF or SCAG passage gives Waterdeep's ethnic mix. The sources below are the closest.

**Wiki city figures (extra source; these are race, not ethnicity)**
> `| races              = {{percentage table|[[Humans]]|64|[[Dwarves]]|10|[[Elves]]|10|[[Halflings]]|5|[[Half-elves]]|5|[[Gnomes]]|3|[[Half-orcs]]|2|Others|1}}`
> — `sources/research/pass3-bundles/waterdeep-overview/wiki.txt:25` (the same line appears in `city-of-the-dead/wiki.txt:141`)

> `| population1        = 1,347,680<ref name="FRCS-pp178-180" /><ref group="note">In the ''[[Forgotten Realms Campaign Setting 3rd edition]]'', the population of Waterdeep is stated to be 1,347,800, though the metropolitan population (i.e., those in the city proper) is only 132,661.</ref>`
> — `sources/research/pass3-bundles/waterdeep-overview/wiki.txt:62`

> `| demonym            = Waterdhavian,<ref name="WotW">{{Cite polyhedron/74/The Everwinking Eye: Words To The Wise}}</ref><br />Waterdavian<ref name="WDH5e">{{Cite book/Waterdeep: Dragon Heist}}</ref>`
> — `sources/research/pass3-bundles/waterdeep-overview/wiki.txt:23`

**Campaign's own statement (current remix state)**
> "- **Population (city-wide):** No source gives a count for 1492 DR. `[research]` For scale, the wiki gives 1,347,680 across Waterdeep and the farmland it commands (*Forgotten Realms Campaign Setting* 3e, 1372 DR), of whom 132,661 count as the metropolis, and the wiki's own estimate for the city proper is about 200,000. The wiki adds that a plague in 1395 DR reduced the population greatly (*Forgotten Realms Campaign Guide* 4e)."
> — `campaign/setting/geography/waterdeep.md:21`

> "- **Peoples (city-wide):** The wiki gives humans 64%, dwarves 10%, elves 10%, halflings 5%, half-elves 5%, gnomes 3%, half-orcs 2% and others 1%, with most elves moon elves and most halflings lightfoot. No source gives a ward breakdown, so the ward pages reuse these figures with a label. The adventure names the people of Waterdeep among its greatest splendors and calls the city a haven for those who define for themselves what it means to be a man or a woman."
> — `campaign/setting/geography/waterdeep.md:22`

> "- **Conflicts:** Editions of the peoples table. The wiki gives the percentages without an edition (`wiki.txt:25`). The ward pages tag them *City of Splendors* 2e. This page says \"the wiki\" and leaves the tag to the ward pages. Unverified."
> — `campaign/setting/geography/waterdeep.md:155`

> "- **Primary Peoples:** No ward figure exists. Dragon Heist says the ward is made up of enclaves, blocks and streets occupied by citizens who trace their ancestry to other realms, with halfling cooks, Calishite singers and dwarven craftsmen among them. The city figures are humans 64%, dwarves 10%, elves 10% (mostly moon elves), halflings 5%, half-elves 5%, gnomes 3%, half-orcs 2% and others 1% (wiki, *City of Splendors* 2e)."
> — `campaign/gazetteer/waterdeep/southern-ward.md:27` (the gazetteer's own summary of WDH; the WDH sentences are quoted below)

**FRHoF: Sword Coast cosmopolitan cities**
> "The Sword Coast boasts some of the most cosmopolitan cities in Faerûn. In a city like {@area Waterdeep|224|x} or Baldur's Gate, a visitor might pass a dragonborn ombudsman, an aasimar merchant, and a goliath lutist all in the span of a city block. Even in smaller villages, people hold few prejudices and tend to be more receptive to new ideas than in places like the stubborn {@area Heartlands|1a4|x} or the more isolationist isles of the {@area Trackless Sea|236|x}."
> — `sources/5etools/book/book-frhof.json:4444`

**FRHoF: the wards, including the Southern Ward**
> "Waterdeep is divided into several wards. Wards aren't separated by walls or gates, and crossing between wards is easy. City wards include the Sea Ward, marked by the palatial fortress-estates of the city's rich and powerful; the peacefully elegant North Ward; and the busy marketplaces of the Trade Ward. The Southern Ward is home to many immigrants, while the city's poorest live and work in the Dock Ward. Waterdeep's dead are entombed in the City of the Dead, a massive park and open air mausoleum within the city. Outside Waterdeep, a large collection of shelters that were once temporary housing for refugees has become a neighborhood of its own: the Field Ward. The Field Ward isn't patrolled by the city guards and has no sanitation or other city services; it is home to Waterdeep's most desperate citizens."
> — `sources/5etools/book/book-frhof.json:4541`

**SCAG: Waterdeep's population and the outside money**
> "Now Zhents and Thayans and Baldurian merchants have coin enough to buy property within the city, if they choose, but that is no reason to award them noble titles and legal rights, instead of merely a mansion, for doing so."
> — `sources/5etools/book/book-scag.json:3385`

> "Every Waterdhavian has suspicions as to whether this or that influential citizen is or isn't a lord of the city, and some are willing to make their beliefs public, but few who are confronted in such a way have ever claimed to be a lord, and none of those have also produced proof of that assertion."
> — `sources/5etools/book/book-scag.json:3382`

> "In addition, people regularly venerate gods based on their needs and circumstances: a farmer whose favored deity is Chauntea would pray to Amaunator for a few clear, sunny days, and a Waterdhavian noble who habitually worships Deneir would give thanks to Sune after a successful coming-out party for her son. Even priests of particular gods acknowledge the roles that other deities play in the world and in their lives."
> — `sources/5etools/book/book-scag.json:1047`

> "In cosmopolitan places such as Waterdeep and Calimshan, small shrines and temples to strange gods spring up from time to time."
> — `sources/5etools/book/book-scag.json:1056`

> "Their cultural and societal makeup runs the gamut, from the cosmopolitan folk who reside in great cities such as Baldur's Gate and Waterdeep to the barbarians who rage throughout the Savage Frontier."
> — `sources/5etools/book/book-scag.json:6069`

> "In Waterdeep, for instance, half-orcs make up a tiny percentage of the population, yet even at that they still number in the hundreds."
> — `sources/5etools/book/book-scag.json:6721`

> "Larger cities on the Sword Coast—including Baldur's Gate, Neverwinter, and Waterdeep—all have a few sorcerers, since people with magic gravitate to places where their abilities are valued."
> — `sources/5etools/book/book-scag.json:7810`

> "Waterdeep has long been divided into several large regions called wards. To locals these are essential to Waterdeep, but outsiders often lose track of which ward they're in or what a ward's name signifies. The names of the wards suggest the contents of the buildings and the character of the activity in each one, but no laws exist that restrict a given activity or class of people to any specific ward."
> — `sources/5etools/book/book-scag.json:3391`

> "Stables, warehouses, and shops related to overland trade dominate Southern Ward. Most residents are hardworking folk that load and unload caravan carts, and otherwise perform low-paying work."
> — `sources/5etools/book/book-scag.json:3443` (SCAG's Southern Ward entry says nothing about ethnicity)

**Dragon Heist: the Southern Ward (the only WDH passage on a ward's people)**
> "It is called the Southern Ward, not the South Ward. Waterdavians are peculiar about this, and if you insist on referring to it as the South Ward, expect to be corrected or thought a fool. The name derives not merely from its southerly location in the city, but from the southerners who settled in this district as the city grew. Today, the ward still hosts most of the traveling merchants who visit the city, and is made up of many enclaves, blocks, and streets primarily occupied by citizens who trace their ancestry to other realms."
> — `sources/adventure-wdh.json:31048`

> "One can indulge in the finest halfling food here, enjoy the best singers of Calishite music, and examine the most stunning works of dwarven crafting-but the first challenge is finding where these treats are housed. The Southern Ward has long been a district of laborers catering to travelers, so its folk have adopted the architectural custom of building homes and businesses above stables or around inn yards, near to where wagon trains are housed."
> — `sources/adventure-wdh.json:31049`

**Dragon Heist: noble and family origins in Waterdeep**
> "Waterdeep contains well over a hundred noble families. The following noble houses are fine choices for any character with the noble background from the {@book Player's Handbook|phb} or the Waterdavian noble background from the {@book Sword Coast Adventurer's Guide|scag}."
> — `sources/adventure-wdh.json:1053`

> "The Amcathras are a Tethyrian family that specializes in horse breeding and training, cattle ranching, wine-making, and weaponsmithing."
> — `sources/adventure-wdh.json:1060`

> "The Margasters are an Illuskan family whose business interests lie in land-based shipping and bulk goods trading."
> — `sources/adventure-wdh.json:1069`

> "Once banished from Waterdeep for smuggling, slavery, and other crimes, this Tethyrian house has returned and is trying to overcome its dark past and disgraceful reputation by focusing on legitimate business ventures such as wine-making and gem trading."
> — `sources/adventure-wdh.json:1087`

> "Members of the Emerald Enclave can be found in Phaulkonmere, a noble villa in the Southern Ward, and at the Snobeedle Orchard and Meadery in Undercliff."
> — `sources/adventure-wdh.json:1320` (the next sentence in the same paragraph: "The place is owned by descendants of two wealthy families-the Tarms (longtime Waterdavians) and the Phaulkons (who are of Cormyrean descent).")

**Dragon Heist: "Waterdavian" is a citizenship word, not an ethnicity**
> "{@creature Floon Blagmaar|WDH|Floon}, a native Waterdavian in his early thirties, is a handsome fellow but not very bright. He used to work as an escort in festhalls but is currently unemployed. Several months ago, he came upon a married noble engaging in some indiscreet behavior, and now lives off the generous bribe he is being paid to keep silent."
> — `sources/adventure-wdh.json:32080`

> "Players looking for background options beyond those described in the {@book Player's Handbook|phb} can find several appropriate ones in the {@book Sword Coast Adventurer's Guide|scag}: {@background City Watch|scag}, {@background cloistered scholar|scag}, {@background courtier|scag}, {@background faction agent|scag}, {@background far traveler|scag}, {@background inheritor|scag}, {@background mercenary veteran|scag}, {@background urban bounty hunter|scag}, and {@background Waterdhavian noble|scag|Waterdavian noble}. If you have access to this book, consider making its background options available to your players' characters."
> — `sources/adventure-wdh.json:1046`

> `"name": "Waterdhavian Noble",`
> — `sources/5etools/book/book-scag.json:8230` (the SCAG background; also listed at line 8158 as `"{@background Waterdhavian Noble|SCAG}"`)

**FRHoF: "Waterdhavian" as citizenship**
> "Many Waterdhavians become agents of the Lords' Alliance to represent not Waterdeep as a whole but rather one of Waterdeep's many power-hungry lords."
> — `sources/5etools/book/book-frhof.json:8160` (the full paragraph continues: "For her part, the open lord of Waterdeep, Laeral Silverhand, uses spies to assess visiting adventurers. Those who show potential receive invitations from the city guard to undertake quests for the Lords' Alliance.")

---

## How Dragon Heist labels its NPCs (table)

**The label format.** Dragon Heist puts the ethnicity inside the stat-line parenthetical, between the gender and the word "human" in most lines. For example: `(LG male Illuskan human {@creature veteran})` (line 2183). Some lines put it after "human" (`(LG male human Tethyrian {@creature knight})`, line 3740) or leave out "human" (`(NE male Illuskan {@creature commoner})`, line 4237). Generic humans carry no ethnicity: "Ten servants (human {@creature commoner||commoners}) eat here at mealtimes." (`sources/adventure-wdh.json:20203`).

**"Waterdavian" is never inside a label.** Dragon Heist uses "Waterdavian" as a noun or adjective for citizens: "a 30-year-old Waterdavian florist" (line 8317), "Kidnapped Waterdavians" (line 17222), "a native Waterdavian" (line 32080). No stat line uses it as an ethnicity.

**Table.** Campaign column entries are file:line plus the label fragment. "GAP" means the campaign label omits the ethnicity that WDH gives. "CONFLICT" means the campaign gives a different ethnicity. "agrees" means the campaign label matches WDH.

| NPC | WDH line | WDH label (exact fragment) | Campaign or wiki label (file:line) |
|---|---|---|---|
| Durnan | 1505 | `{@i N male Illuskan human innkeeper}` | campaign/setting/notable-figures/independents-allies/03-durnan.md:6 `Human innkeeper and retired adventurer, neutral` — GAP |
| "Bonnie" (doppelganger barmaid) | 1515 | `{@i N doppelganger disguised as Tethyrian human barmaid}` | campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:270 `in the Tethyrian` (fragment) — agrees |
| Mattrim "Threestrings" Mereg | 1525 | `{@i LG male Illuskan human bard}` | campaign/setting/notable-figures/harpers/03-mattrim-mereg.md:6 `Human bard (Harper spy), lawful good` — GAP |
| Jalester Silvermane | 1535 | `{@i LG male Chondathan human fighter}` | campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:5 `Chondathan human spy, lawful good` — agrees |
| Meloon Wardragon | 1546 | `{@i NE male Chondathan human adventurer under the control of an intellect devourer}` | campaign/guides/trollskull-manor/08-notable-patrons.md:61 `(Champion Fighter, NG Illuskan human)` — CONFLICT; campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:5 `Human fighter, neutral good (when himself) / neutral evil (while occupied)` — GAP |
| Obaya Uday | 1557 | `{@i NG female Chultan human priest of Waukeen}` | campaign/setting/deities/waukeen.md:75 `Obaya Uday, a neutral good Chultan human` — agrees |
| Hyustus Staget | 2183 | `(LG male Illuskan human {@creature veteran})` | campaign/setting/governance-and-guilds/city-watch.md:72 `Hyustus Staget (Lawful Good, Illuskan Human, he/him)` — agrees |
| Ambrose Everdawn | 3740, 7767 | `(LG male human Tethyrian {@creature knight})` | campaign/setting/notable-figures/independents-allies/17-sir-ambrose-everdawn.md:5 `Tethyrian Human knight of Kelemvor, Lawful Good, he/him` — agrees |
| Uza Solizeph (WDH: "Uza") | 3863–3864 | `Uza (LG female human Mulan {@creature commoner})`; line 3863 begins `Uza Solizeph is an old woman who sells books` | campaign/gazetteer/waterdeep/trades-ward.md:74 `Uza Solizeph's Bookshop` (no ethnicity) — GAP |
| Esloon Bezant | 3923 | `(LE male Thayan human {@creature mage})` | campaign/setting/notable-figures/independents-allies/16-esloon-bezant.md:5 `Thayan human Red Wizard exile, Neutral, he/him` — agrees |
| Savra Belabranta | 3949 | `(NG female Tethyrian human {@creature knight})` | campaign/gazetteer/waterdeep/castle-ward.md:145 `Savra Belabranta (Neutral Good, Human, she/her)` — GAP; campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md:6 `Human knight, neutral good` — GAP |
| Gaxly Rudderbust | 3972 | `(N male Illuskan human {@creature commoner})` | sources/Appendix_C_-_Player_Faction_Missions.md:1010 `(N male Illuskan human **Commoner**)` — agrees (Alexandrian appendix; the campaign has the name as plain text at campaign/gazetteer/waterdeep/north-ward.md:294) |
| Gysheer Omfreys | 3982 | `(LE female Tethyrian human {@creature cult fanatic})` | campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/overview.md:21 `Gysheer Omfreys is a Tethyrian` — agrees |
| Hammond Kraddoc | 4113 | `(N male Illuskan human {@creature commoner})` | campaign/setting/notable-figures/trollskull-community/07-hammond-kraddoc.md:6 `Illuskan human guild representative, neutral` — agrees |
| Justyn Rassk | 4124 | `(NE male Illuskan human {@creature thug})` | campaign/gazetteer/waterdeep/field-ward.md:256 (plain text, no label) — GAP |
| Emmek Frewn | 4237 | `(NE male Illuskan {@creature commoner})` | campaign/setting/notable-figures/trollskull-community/10-emmek-frewn.md:6 `Illuskan human tavern owner, neutral evil` — agrees |
| Hurv Taldred | 5666 | `(LE male Illuskan {@creature cult fanatic})` | campaign/setting/notable-figures/gralhunds/04-hurv-taldred.md:6 `Human cult fanatic, neutral evil` — GAP |
| Nat | 7133 | prose: `a lanky, 10-year-old deaf Illuskan girl` | campaign/setting/notable-figures/trollskull-community/12-nat.md:6 `Human street urchin, neutral good` — GAP; wiki dragonward-and-walking-statues/wiki.txt:828 `| ethnicity      = [[Illuskan]]<ref name="WDH5e-p63" />` |
| Jenks | 7133 | prose: `a portly 9-year-old Turami boy` | campaign/setting/notable-figures/trollskull-community/13-jenks.md:6 `Human street urchin, neutral good` — GAP; wiki dragonward-and-walking-statues/wiki.txt:952 `| ethnicity      = [[Turami]]<ref name="WDH5e-p63" />` |
| Squiddly | 7133 | prose: `a slim 9-year-old tiefling boy` (species only) | not checked |
| Sora Cuttle | 7192 | `(LG female Illuskan human {@creature commoner})` | none found |
| Avareen Windrivver | 7202 | `(LE female Illuskan human {@creature spy})` | campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md:6 `Human spy (Zhentarim interrogator), lawful evil` — GAP |
| Zorbog Jyarkoth | 7202 | `(NE male Turami human {@creature thug})` | campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md:6 `Human thug (Zhentarim), neutral evil` — GAP |
| Vevette Blackwater | 7203, 7734, 8531, 9132, 14783, 30120 | `(CE female Tethyrian human {@creature swashbuckler\|VGM})` | campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md:6 `Human swashbuckler, lawful evil` — GAP |
| Grinda Garloth | 7472 | `(CN female Illuskan human {@creature mage} who speaks Common, Dwarvish, Halfling, and Undercommon)` | campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:6 `Human mage (black market armorer), neutral` — GAP; campaign/gazetteer/waterdeep/dock-ward.md:192 `Grinda Garloth (Neutral, Human, she/her)` — GAP |
| Agorn Fuoco | 7634, 9133, 14783, 30120 | `(NE male Turami {@creature bard\|VGM})` | campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:6 `Human bard (Manshoon lieutenant), neutral evil` — GAP |
| Marta (Agorn's mother) | 7634 | `(N female Turami human {@creature commoner} with 1 hit point)` | none found |
| Salazar Lorrance | 7646 | `(CG male Tethyrian human)` | none found |
| Mavia Oxlander | 7646 | `(NG female Chondathan human)` | none found |
| Rowan Evenwood | 7606 | `(LG female Chondathan human {@creature commoner})` | none found |
| Iokaste Daliano | 9035 | `(N female Tethyrian {@creature commoner})` | none found |
| Yaliek Iltizmar | 9028 | `(N female Rashemi {@creature bard\|VGM})` | none found |
| Westra Moltimmur | 9075 | `(CG female Illuskan human {@creature commoner} with Insight +2 and Performance +6)` | none found |
| Amath Sercent | 9133, 9748 | `(LE female Mulan {@creature priest} of Bane)` | campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:6 `Mulan human priest of Bane, lawful evil` — agrees; campaign/gazetteer/waterdeep/castle-ward.md:79 `Amath Sercent (Lawful Evil, Mulan Human, she/her)` — agrees |
| Two violinists (unnamed) | 9133 | `(LG male Illuskan human {@creature spy\|\|spies} with Performance +5)` | none found |
| Shan Chien | 9749 | `(N male Shou human {@creature commoner})` | none found |
| Sembra Vashir | 9666 | `(LN female Calishite human)` | campaign/setting/governance-and-guilds/guilds.md:57 `Sembra Vashir, a lawful neutral Calishite human` — agrees |
| Hester Barch | 10638 | `(LG female Turami human {@creature acolyte} with Insight +4)` | campaign/setting/governance-and-guilds/code-legal-and-magisters.md:50 `Hester Barch is the lawful good magister of the Castle Ward courthouse, a petite Turami` — agrees |
| Fenerus Stormcastle | 10656 | `(N male Tethyrian {@creature bandit captain})` | campaign/gazetteer/waterdeep/trades-ward.md:128 `Fenerus Stormcastle (Neutral Evil, Human, he/him)` — GAP; campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:6 `Human spy (retired brigand), neutral evil` — GAP |
| Volkarr Kibbens; Urlaster Ghann | 13184 | `(NE male Illuskan human {@creature commoner\|\|commoners})` | campaign/gazetteer/waterdeep/southern-ward.md:271 (plain text, no label) — GAP |
| Arn Xalrondar | 13211 | `(LE male Tethyrian human)` | campaign/gazetteer/waterdeep/southern-ward.md:139 `Arn Xalrondar (Lawful Evil, Human, he/him)` — GAP (southern-ward.md:263 records the WDH Tethyrian label) |
| Seffia Naelryke | 13211 | `(LE female Tethyrian human)` | campaign/gazetteer/waterdeep/southern-ward.md:130 `Seffia Naelryke (Lawful Evil, Tethyrian Human, she/her)` — agrees |
| Vhaspar Holmdreg | 13267 | `(LG male Illuskan human {@creature priest})` | campaign/gazetteer/waterdeep/north-ward.md:91 `Vhaspar Holmdreg (Lawful Good, Illuskan Human, he/him)` — agrees |
| Sidra Romeir | 28155 | `(LE female Calishite human {@creature veteran})` | campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:6 `Calishite human veteran, lawful evil` — agrees |
| Sidra's two subordinates (unnamed) | 28155 | `(LE male Tethyrian human {@creature thug\|\|thugs})` | none found |
| Ered Payno | 28552 | `(LE male Damaran human)` | none found |
| Havi Termock | 28552 | `(CE female Chondathan human)` | none found |
| Savara Firethorn | 28552 | `(NE female Tethyrian human)` | none found |
| Kaevja Cynavern | 29994 | `is a female Mulan human {@creature mage}, with these changes:` | campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:6 `Human mage, lawful neutral` — GAP; campaign/setting/organizations/09-manshoons-zhentarim.md:33 `Kaevja Cynavern** — Human` — GAP |
| Corylus Thann | 30364 | `(LE male Tethyrian human {@creature noble})` | campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:53 `Corylus Thann, a lawful evil Tethyrian human` — agrees |
| Jelenn Urmbrusk | 30374 | `(N female Tethyrian human {@creature noble})` | campaign/setting/notable-figures/city-officials/04-jelenn-urmbrusk.md:6 `Tethyrian human noble, neutral` — agrees; campaign/gazetteer/waterdeep/sea-ward.md:139 `Jelenn Urmbrusk (Neutral, Tethyrian Human, she/her)` — agrees |
| Floon Blagmaar | 32088 | `Floon is a chaotic good Illuskan human {@creature commoner}` | campaign/setting/notable-figures/independents-allies/04-floon-blagmaar.md:6 `Illuskan human, chaotic good` — agrees; campaign/guides/trollskull-manor/08-notable-patrons.md:71 `Floon Blagmaar *(Commoner, CG Tethyrian human)*` — CONFLICT |
| Zardoz Zord (Jarlaxle's disguise) | 1300; 32180 | `a flamboyant Illuskan captain named Zardoz Zord`; `an Illuskan human named Zardoz Zord` | campaign/quests/faction-events/bregan-daerthe/s03-dinner-with-zardoz/ev-01-dinner-with-zardoz.md:163 `Zardoz Zord (Chaotic Neutral, Drow in the guise of an Illuskan human` — agrees (the label is the disguise) |
| Orond Gralhund | 32455 (also 32448) | `is a Tethyrian human noble, with these changes:`; `Although he is human, Orond was born with a tiefling's tail.` (32448) | campaign/setting/notable-figures/gralhunds/02-orond-gralhund.md:6 `Tethyrian human noble, neutral evil` — agrees |
| Yalah Gralhund | 32789 | `is a Tethyrian human {@creature noble}, with these changes:` | campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:6 `Tethyrian human noble, neutral evil` — agrees |
| Renaer Neverember | 32555 | `is an Illuskan human who has the statistics of a {@creature swashbuckler\|VGM}, with these changes:` | campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:6 `Illuskan human noble, chaotic good` — agrees |
| Saeth Cromley | 32580 | `is an Illuskan human {@creature veteran}, with these changes:` | campaign/gazetteer/waterdeep/castle-ward.md:141 `Saeth Cromley (Lawful Good, Illuskan Human, he/him)` — agrees |
| Urstul Floxin | 32652 | `is an Illuskan human {@creature assassin}, with these changes:` | campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:6 `Illuskan human assassin, lawful evil` — agrees |
| Cressa Galavarco | 17873 | `(LG female Tethyrian {@creature veteran} with no armor or weapons)` | campaign/setting/governance-and-guilds/city-watch.md:72 `Cressa Galavarco (Lawful Good, Tethyrian Human, she/her)` — agrees |
| Claudio Benzreck | 17222 | `(LN male Tethyrian human noble)` | none found |
| Xia Shung | 17222 | `NG female Shou human bard` | none found |
| Arthright Grayfalcon | 17222 | `CN male Illuskan swashbuckler` | none found |
| Margo Verida | 25455 | `a female Amnian human {@creature bard\|VGM}` | campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:6 `Human bard, chaotic good` — GAP |
| Khafeyta Murzan | 25456 | `a female Mulhorandi human {@creature swashbuckler\|VGM}` | campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:6 `Human swashbuckler, neutral good` — GAP; campaign/setting/organizations/07-bregan-daerthe.md:45 `Khafeyta Murzan** — Human` — GAP |
| Vaelle Lurval | 8317 | `(LE female Tethyrian human {@creature cultist})` | campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:35 `a Lawful Evil female Tethyrian human` — agrees |
| Mirt (no WDH label) | — | none (WDH names him without ethnicity) | campaign/setting/notable-figures/harpers/01-mirt.md:6 `Tethyrian human moneylender, chaotic good`; wiki dock-ward/wiki.txt:367 `| ethnicity      = [[Tethyrian]]<ref name="CoS.W-p54-55" />` (no WDH source) |
| Vajra Safahr (no WDH label) | — | none | campaign/gazetteer/waterdeep/castle-ward.md:132 `Vajra Safahr (Lawful Neutral, Tethyrian Human, she/her)` — CONFLICT with campaign/guides/trollskull-manor/08-notable-patrons.md:55 `Vajra Safahr, the Blackstaff *(Archmage stat block, NG Calishite human; see the **Vajra Safahr, the Blackstaff** page in Notable Figures)*` and sources/Appendix_D_-_Running_the_Tavern.md:1313 `Archmage — NG Calishite human; see Dragon Heist appendix B` (WDH has no Vajra stat line) |
| Volothamp Geddarm (no WDH label) | — | none | campaign/setting/notable-figures/independents-allies/01-volothamp-volo-geddarm.md:6 `Illuskan human chronicler, chaotic good`; wiki city-watch/wiki.txt:705 `| ethnicity      = ` (blank) |
| Dagult Neverember (no WDH label) | — | none | campaign/setting/notable-figures/independents-adversaries/01-dagult-neverember.md:5 `Illuskan human noble, lawful neutral` |
| Lady Gondafrey | 28506 (`a native Waterdavian`) | none | campaign/setting/governance-and-guilds/city-watch.md:68 `Lady Gondafrey (Lawful Good, Gargoyle, she/her)` (species, not ethnicity) |

---

## Name patterns by ethnicity (quoted)

**Only SCAG gives personal name lists.** FRHoF has none (see Not found). Each list below is the full entry.

- **Arkaiun Names:** "(Male) Houn, Rhivaun, Umbril, Xaemar, Zeltaebar; (female) Glouris, Maeve, Sevaera, Xaemarra, Zraela; (surnames) Lharaendo, Mristar, Wyndael" — `sources/5etools/book/book-scag.json:6091`
- **Bedine Names:** "(Male) Aali, Rashid, Tahnon, Tanzim, Whalide; (female) Aisha, Farah, Nura, Rashida, Zalebyeh; (tribe names) Alaii, Bordjia, Clelarra, Desai, Dakawa, Dursalai, Goldor, Iriphawa, Kellordrai, Lalajar, Qahtan, Yethtai, Zazalaar" — `book-scag.json:6108`
- **Ffolk Names:** "(Male) Artur, Bern, Colin, Manfred, Tristan; (female) Alicia, Gennifer, Meridith, Elaine, Olivia; (surnames) Archer, Gareth, Leed, Kendrick, Morgan, Waters" — `book-scag.json:6125`
- **Gur Names:** "(Male) Boriv, Gardar, Madevik, Vlad; (female) Varra, Ulmarra, Imza, Navarra, Yuldra; (surnames) Chergoba, Drazlad, Tazyara, Vargoba, Stayankina" — `book-scag.json:6142`
- **Halruaan Names:** "(Male) Aldym, Chand, Meleghost, Presmer, Sandrue, Uregaunt; (female) Aithe, Chalan, Oloma, Phaele, Sarade; (surnames) Avhoste, Darante, Maurmeril, Stamaraster" — `book-scag.json:6159`
- **Imaskari Names:** "(Male) Charva, Duma, Hukir, Jama, Pradir, Sikhil; (female) Apret, Bask, Fanul, Mokat, Nismet, Ril; (surnames) Datharathi, Melpurvatta, Nalambar, Tiliputakas" — `book-scag.json:6176`
- **Nar Names:** "(Male) Avan, Ostaram, Petro, Stor, Taman, Thalaman, Urth; (female) Anva, Dasha, Dima, Olga, Westra, Zlatara; (surnames) Dashkev, Hargroth, Laboda, Lackman, Stonar, Stormwind, Sulyma" — `book-scag.json:6193`
- **Shaaran Names:** "(Male) Awar, Cohis, Damota, Gewar, Hapah, Laskaw, Senesaw, Tokhis; (female) Anet, Bes, Idim, Lenet, Moqem, Neghet, Sihvet; (surnames) Cor Marak, Laumee Harr, Moq Qo Harr, Woraw Tarak" — `book-scag.json:6210`
- **Tuigan Names:** "(Male) Atlan, Bayar, Chingis, Chinua, Mongke, Temur; (female) Bolormaa, Bortai, Erdene, Naran" — `book-scag.json:6228`
- **Ulutiun Names:** "(Male) Amak, Chu, Imnek, Kanut, Siku; (female) Akna, Chena, Kaya, Sedna, Ublereak" — `book-scag.json:6245`

**SCAG: Calishite and Mulhorandi names are given for tieflings only.** "Al-Khem and Beni-Asmodai are two common Calishite tiefling surnames that proclaim the race's heritage, along with first names such as Haroun, Ishaq, and Nizam (male) or Hania, Rashaa, and Zaar (female)." (`book-scag.json:6832`) "Mulhorandi surnames that begin with \"Sia\" or \"Zia\" followed by a god's name indicate a bearer of that god's bloodline, such as Zianhur and Siasobek." (`book-scag.json:6833`)

**SCAG: no name lists for** the human Calishite, Chondathan, Damaran, Illuskan, Mulan, Rashemi, Shou, Tethyrian, Turami or Chultan ethnicities. SCAG's human-ethnicity section has no name entries for these.

**FRHoF: no personal name lists.** The "Gods and Names" section (heading at `book-frhof.json:2214`) covers deities only: "Deities worshiped in Anauroch are often gods of the Faerûnian pantheon who go by other faces and names." (`book-frhof.json:2218`)

**The caller's invented names against the name lists.** None of the caller's invented names appears in any SCAG or FRHoF name list. Searched: Dunmere, Pimm, Tarrow, Sennet, Quenn, Hale, Dall, Tull, Keen, Tormar, Brant, Harrask, Fen, Talver, Valt, Coile, Harsk, Raske, Cressyn, Dalloway, Crestfall, Brindle, Pennick, Bannock, Terrow, Dath, Caskwall, Stoll, Halvane, Tesk, Dask, Solizeph, Uza, Gorra, Marek, Wenna, Halric, Brannoc, Odalys, Ilmra, Orin. Two names outside the caller's list do match: "Chergoba" (Gur surname, `book-scag.json:6142`) and "Westra" (Nar female name, `book-scag.json:6193`). WDH's "Jandar Chergoba" (`sources/adventure-wdh.json:20256`, the head chef) carries no ethnicity label, and WDH's "Westra Moltimmur" is labelled "CG female Illuskan human" (line 9075), so the name pattern and WDH's label disagree.

**The campaign's label for each invented name.** Almost every name on the caller's list appears in the campaign labelled "Waterdhavian Human", which is a city, not an ethnicity. Exact lines (name → file:line):

- **Marek Dunmere:** "> Marek Dunmere (Lawful Neutral, Waterdhavian Human, he/him) :: the North Ward's day-shift desk sergeant, who has heard every kind of complaint and writes down all of them." — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:173`. Plain text, no label: "- The ward's Watch station takes reports from residents and keeps the dead in a cellar morgue, where clerics cast *gentle repose* on the bodies. Sergeant **Marek Dunmere** takes reports on the day shift." — `campaign/gazetteer/waterdeep/north-ward.md:105`
- **Harl Pimm:** "> Harl Pimm (Lawful Neutral, Waterdhavian Human, he/him) :: a stolid Dock Ward constable who counts lamp oil in every theater on his route, drinks Kreb's free tea, and has never in his life seen a drow." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:176`. Also: "- Gorra (Lawful Neutral, Waterdhavian Human, she/her) is a Harbor Watch officer who has walked the Ship Street rounds for years. Captain Ilsa Dalloway and Constable Harl Pimm (Lawful Neutral, Waterdhavian Human, he/him), a stolid constable who counts lamp oil in every theater on his route, work crowd duty at the Seven Masks Theater." — `campaign/gazetteer/waterdeep/dock-ward.md:218`
- **Ilsa Dalloway:** "> Ilsa Dalloway (Lawful Neutral, Waterdhavian Human, she/her) :: the Dock Ward Watch captain on crowd duty at the Faire's showcase, practical, tired and polite." — `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:218`
- **Gorra:** "> Gorra (Lawful Neutral, Waterdhavian Human, she/her) :: a Harbor Watch officer who has walked the Ship Street rounds for years and has seen three sailors carried off it this season." — `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md:104`
- **Wenna Tarrow:** "> Wenna Tarrow (Neutral, Waterdhavian Human, she/her) :: a widowed tallow chandler in her fifties who lets the Doom Raiders use her loft and prefers not to know why." — `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:180`
- **Halric Sennet:** "> Halric Sennet (Neutral, Waterdhavian Human, he/him) :: a soft-spoken Trades Ward scrivener in his sixties, with ink-stained fingers, who has never put his own name to anything." — `campaign/quests/faction-events/doom-raiders/r10-viper/ev-01-viper.md:93`
- **Brannoc Hale:** "> Brannoc Hale (Neutral, Waterdhavian Human, he/him) :: a scarred sellsword in his forties, trained by Tashlyn, who takes Yagra's place when she is out and never explains himself." — `campaign/quests/faction-events/doom-raiders/r10-viper/ev-01-viper.md:166`
- **Odalys Quenn:** "- **Odalys Quenn (Neutral, Waterdhavian Human, she/her), disguise:** disguises up to four people in an hour, and an observer needs a DC 15 Intelligence (Investigation) check to see through it." — `campaign/quests/faction-events/doom-raiders/r10-viper/ev-01-viper.md:187`
- **Orvyn Dall:** "> Orvyn Dall (Lawful Neutral, Waterdhavian Human, he/him) :: a mild, thin appeals clerk in his forties with ink on his cuffs, whose mouth moves a moment after his eyes." — `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-01-the-legates-eyes.md:172`; "> - Orvyn Dall is a Waterdhavian Human appeals clerk in the Trades Ward district magistracy. An Occupying Devourer has ridden him for seven tendays. It keeps his brain alive, so Orvyn is aware and cannot act or speak." — `…/ev-01-the-legates-eyes.md:17`; and "- The appeals office of the ward's district magistracy employs four clerks. One of them, Orvyn Dall, a Waterdhavian human, was placed there seven tendays ago." — `campaign/gazetteer/waterdeep/trades-ward.md:98`
- **Brenna Tull:** "Orvyn lives in a second-floor flat on Tallow Court in the Trades Ward. He leaves at 07:30 and comes home at 18:00. Brenna Tull (Lawful Neutral, Waterdhavian Human, she/her), a widow who lives in the flat below, shops until noon and sits at her window from the afternoon on." — `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-02-the-extraction.md:27`. Garrick Tull is plain text: "A lame former Watch quartermaster named Garrick Tull manages it, and a Redknife member opens the door with the phrase \"Alliance weather\"." — `campaign/gazetteer/waterdeep/trades-ward.md:171`
- **Wil Keen:** "> Wil Keen (Neutral Good, Waterdhavian Human, he/him) :: a Harper courier in his thirties who works the Dock Ward and wears the grey of a dock carter." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:73`
- **Pell Tormar:** "> Pell Tormar (Lawful Good, Waterdhavian Human, he/him) :: a clerk at the Dock Ward cargo office and a quiet Harper sympathizer." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:85`
- **Sella Brant:** "- A house kept by Sella Brant (Lawful Neutral, Waterdhavian Human, she/her), a practical landlady who dislikes surprises and is home all day." — `campaign/gazetteer/waterdeep/field-ward.md:84`; "> Sella Brant (Lawful Neutral, Waterdhavian Human, she/her) :: the keeper of Three Lanterns House, 7 Windborne Way in the Field Ward, who is home all day." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:93`
- **Tobin Harrask:** "> Tobin Harrask (Neutral, Waterdhavian Human, he/him) :: a thin clerk in his forties who has copied the register for six years and has wanted something better for most of them." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-02-the-extraction.md:196`
- **Nella Fen:** "> Nella Fen (Neutral Good, Waterdhavian Human, she/her) :: a stout chandler in her fifties, with wax under her nails, who sells candles and keeps her ears open." — `campaign/quests/faction-events/harpers/r03-harpshadow/ev-01-harpshadow.md:145`
- **Evin Talver:** "> Evin Talver (Lawful Good, Waterdhavian Human, he/him) :: a thin, careful apothecary in his fifties, with stained fingers and a pair of spectacles he keeps pushing up his nose." — `campaign/quests/faction-events/harpers/r10-brightcandle/ev-01-brightcandle.md:114`
- **Perrin Valt:** "> Perrin Valt (Neutral Good, Waterdhavian Human, he/him) :: a lean Harper Spy in his forties, known in the field as Reed, who works alone by preference and works for the member for as long as the job lasts." — `campaign/quests/faction-events/harpers/r10-brightcandle/ev-01-brightcandle.md:178`
- **Mareva Coile:** "> Mareva Coile (Lawful Neutral, Waterdhavian Human, she/her) :: a sharp-tempered route coordinator of about forty-five who holds the crew's contracts and resents needing outside help." — `campaign/quests/faction-events/lords-alliance/m01-the-long-watch/ev-01-six-bells-at-the-muleskull.md:104`. Design note: "- Mareva Coile, the route coordinator, and her four supervisors Delvon Harsk, Hadrin Wenlow, Bremma Dunnet and Cass Fildura. Mareva's species is invented as Waterdhavian Human." — `campaign/quests/faction-events/lords-alliance/m01-the-long-watch/design-notes.md:25`
- **Delvon Harsk:** "> Delvon Harsk (Neutral, Waterdhavian Human, he/him) :: a heavyset route supervisor in a grey coat. He sells the crew's hours to pay a debt and has waited for someone to catch him." — `campaign/quests/faction-events/lords-alliance/m01-the-long-watch/ev-01-six-bells-at-the-muleskull.md:267`
- **Ottel Raske:** "> Clerk-Sergeant Ottel Raske (Lawful Neutral, Waterdhavian Human, he/him) :: the Watch's file officer at the central records office in the Castle Ward, a stooped, careful man in his fifties with ink on his cuffs who has kept the classified shelf for nineteen years." — `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:196`
- **Florette Cressyn:** "> Florette Cressyn (Lawful Neutral, Waterdhavian Human, she/her) :: a household investigator on Ammalia Cassalanter's retainer, thirty and patient, who has watched Brimel for ten days and has nothing yet." — `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:160`
- **Brimel Crestfall:** "> Brimel Crestfall (Neutral, Waterdhavian Human, he/him) :: a household steward in his forties, competent, orderly and frightened, who sold a floor plan for coin and now wants to leave the city." — `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:341`
- **Ostrin Brindle:** "> Ostrin Brindle (Neutral, Waterdhavian Human, he/him) :: a Dock Ward pawnbroker in his sixties who sells the company's people what a licensed shop won't and keeps his books as neatly as a priest." — `campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:278`
- **Orla Pennick:** "> Orla Pennick (Neutral Good, Waterdhavian Human, she/her) :: the landlady on Ship Street, who talks to anyone who stands still and keeps careful track of who owes her." — `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:95`
- **Jonn Bannock and Ysa Terrow:** "Officers Jonn Bannock (Lawful Neutral, Waterdhavian Human, he/him) and Ysa Terrow (Lawful Neutral, Waterdhavian Human, she/her) work the late shift in **Ten Nights in the City of the Dead**, where they keep the party off the Brandath ground." — `campaign/setting/governance-and-guilds/city-watch.md:72`; "> Officer Jonn Bannock (Lawful Neutral, Waterdhavian Human, he/him) and Officer Ysa Terrow (Lawful Neutral, Waterdhavian Human, she/her) :: two City Watch officers on the late shift." — `campaign/quests/faction-events/emerald-enclave/m02-ten-nights-in-the-city-of-the-dead/ev-01-the-ten-nights.md:149`
- **Sarna Dath:** "> Sarna Dath (Neutral, Waterdhavian Human, she/her) :: a south quay fisher in her fifties, who keeps a blue-and-white boat and watches every hull that passes." — `campaign/quests/faction-events/emerald-enclave/r25-winterstalker/ev-01-winterstalker.md:327`
- **Bertio Caskwall:** "> Bertio Caskwall (Neutral, Waterdhavian Human, he/him) :: a stout wine merchant in his fifties, allied to no faction, who wants his cellar finished before the summer vintage arrives." — `campaign/quests/faction-events/emerald-enclave/s02-the-water-table-stirs/ev-01-the-water-table-stirs.md:286`
- **Garrick Stoll:** "> Garrick Stoll (Lawful Neutral, Waterdhavian Human, he/him) :: a former Watch sergeant on the Tower's rolls, who counts exits before he counts anything else." — `campaign/quests/faction-events/force-grey/r50-force-grey-commander/ev-01-force-grey-commander.md:110`
- **Ysmay Halvane:** "> Ysmay Halvane (Neutral, Waterdhavian Human, she/her) :: a mage of the Tower's staff in her thirties, who teaches evenings at the Academy and prefers a plan to an improvisation." — `campaign/quests/faction-events/force-grey/r10-senior-griffon/ev-01-senior-griffon.md:137`
- **Dovrin Tesk:** "- **If she dies:** Vajra suspends the benefit for a tenday and then assigns a second mage, Dovrin Tesk (Neutral, Waterdhavian Human, he/him), who uses the same block and the same limits. Vajra does not assign a third." — `campaign/quests/faction-events/force-grey/r10-senior-griffon/ev-01-senior-griffon.md:179`
- **Ilmra:** "> Sergeant Ilmra Dunfell (Lawful Neutral, Waterdhavian Human, she/her) :: the tired custody sergeant of Castle Waterdeep, who runs a wing built for thirty prisoners and holds sixty-one." — `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:202`
- **Orin Dask: labelled "Chultan Human", not Waterdhavian.** "> Orin Dask (Lawful Neutral, Chultan Human, he/him) :: a thin, careful map-seller who rolls every map closed before he speaks." — `campaign/quests/faction-events/harpers/r03-harpshadow/ev-01-harpshadow.md:167`
- **Uza Solizeph: no label in the campaign.** "**Uza Solizeph's Bookshop** — Bookshop and Harper drop, Sorn Street" — `campaign/gazetteer/waterdeep/trades-ward.md:74`. The WDH label is in the table above (line 3864).
- **Name list in the gazetteer:** "> - **Names with no page:** Uza Solizeph, Tessalar Maeridge, Beldan Rusk, Orvyn Dall, Brenna Tull, Berna, Mareva Coile, Garrick Tull, Bertio Caskwall, Ilphrin Quiss, Halric Sennet, Bastian Quill, Corvin Hallowell, Mother Tamra, Thongalar the Mighty, Shile Rauretilar and Finder Wyvernspur are plain text. Corvin Hallowell is not the Harper Corvin Nessa Vayle, whose page exists." — `campaign/gazetteer/waterdeep/trades-ward.md:270`

**Project rule that produces the "Waterdhavian Human" label.** `.claude/skills/ember-adventure-style/SKILL.md:143`: "Waterdeep adaptation: `Captain Staxa (Lawful Neutral, Waterdhavian Human, she/her)`. Use the NPC's Notable Figures page for alignment, species, and pronouns. Never guess them. Later mentions use the name alone." `.claude/skills/ember-setting-style/SKILL.md:206`: "- **Compound identities** are capitalized as a unit: *Waterdhavian Human, Calishite Human, Menzoberranzan Drow.*" `docs/plans/deities-user-rulings-brief.md:6` asks that Amath's ethnicity be kept "the way other NPC pages write ethnicity (check how other pages write e.g. Illuskan or Tethyrian human)."

---

## Caveats

### Conflicts between sources

1. **Floon Blagmaar.** WDH: "Floon is a chaotic good Illuskan human {@creature commoner} with an Intelligence of 7 (-2) and a Charisma of 13 (+1). He speaks Common." (`sources/adventure-wdh.json:32088`). Trollskull Manor guide: "**Floon Blagmaar** *(Commoner, CG Tethyrian human)*" (`campaign/guides/trollskull-manor/08-notable-patrons.md:71`). Notable figures: "*Illuskan human, chaotic good*. Stat block: **Commoner**." (`campaign/setting/notable-figures/independents-allies/04-floon-blagmaar.md:6`). The higher-ranked source (WDH) says Illuskan.
2. **Meloon Wardragon.** WDH: "{@i NE male Chondathan human adventurer under the control of an intellect devourer}" (`sources/adventure-wdh.json:1546`). Trollskull Manor guide: "**Meloon Wardragon** *(Champion Fighter, NG Illuskan human)*" (`campaign/guides/trollskull-manor/08-notable-patrons.md:61`). WDH is higher-ranked; it says Chondathan.
3. **Vajra Safahr.** Wiki: "| ethnicity      = [[Tethyrian]]<ref name="BST-p4">{{Cite book/Blackstaff Tower|4}}</ref>" (`sources/research/pass3-bundles/dragonward-and-walking-statues/wiki.txt:209`). Campaign gazetteer: "**Vajra Safahr (Lawful Neutral, Tethyrian Human, she/her)**" (`campaign/gazetteer/waterdeep/castle-ward.md:132`). Trollskull guide: "**Vajra Safahr, the Blackstaff** *(Archmage stat block, NG Calishite human; see the **Vajra Safahr, the Blackstaff** page in Notable Figures)*" (`campaign/guides/trollskull-manor/08-notable-patrons.md:55`). Appendix D: "*Archmage — NG Calishite human; see Dragon Heist appendix B*" (`sources/Appendix_D_-_Running_the_Tavern.md:1313`). WDH gives no ethnicity for Vajra, so the "see Dragon Heist appendix B" pointer is not confirmed by WDH. The campaign's own pages (gazetteer and Notable Figures) and the wiki agree on Tethyrian.
4. **Population edition.** The wiki gives the percentages with no edition (`sources/research/pass3-bundles/waterdeep-overview/wiki.txt:25`); the ward pages tag them "*City of Splendors* 2e" (`campaign/gazetteer/waterdeep/southern-ward.md:27`). The campaign flags this as unverified (`campaign/setting/geography/waterdeep.md:155`).
5. **Cassalanter (wiki).** The wiki's Cassalanter infobox gives "| races          = [[Human]] ([[Tethyrian]])" (`sources/research/pass3-bundles/north-ward/wiki.txt:1005`). The campaign's Cassalanter pages do not label ethnicity. Not a conflict with WDH; a campaign gap.
6. **Halaster Blackcloak (wiki).** Wiki ethnicity "Raurinese" (`code-legal-and-magisters/wiki.txt:1207`, `undermountain-and-skullport/wiki.txt:800`); no WDH or SCAG source. Extra source only.
7. **Mirt.** Wiki: "| ethnicity      = [[Tethyrian]]<ref name="CoS.W-p54-55" />" (`sources/research/pass3-bundles/dock-ward/wiki.txt:367`). The campaign (`campaign/setting/notable-figures/harpers/01-mirt.md:6`) agrees. WDH is silent. A prior research note records the same gap and says: "Adventure: no ethnicity for Mirt. The campaign outranks the wiki. Flagged for the user." (`docs/plans/setting-compendium-research-notes/pass3/batch-governance.md:193`).
8. **Nar as a language.** SCAG's Nar entry (`book-scag.json:6187`) gives no language; the language option says "Nar:" / "Damaran" (`book-scag.json:6315–6316`). Not a conflict; noted for the drafter.
9. **"Waterdhavian" as a background.** SCAG's "Waterdhavian Noble" is a background (`book-scag.json:8230`). WDH's stat lines never use "Waterdavian" as an ethnicity. SCAG and FRHoF do not define "Waterdhavian" as an ethnicity; the campaign's "Waterdhavian Human" label comes from the project rule quoted above.

### Cross-references (other file:line where the topic appears)

The "Waterdhavian Human" lines in the name section above are quoted in full. The further lines below are copied in full as well.

- `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:322` — "> A Dungsweepers' Guild Commoner (Neutral, Waterdhavian Human, she/her) :: a sewer sweeper in her fifties who does not like her crew's quiet guests and is relieved to be asked."
- `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-02-the-extraction.md:202` — "> Orvyn Dall (Lawful Neutral, Waterdhavian Human, he/him) :: a thin, anxious appeals clerk in his forties who is ashamed of what his hands did."
- `campaign/quests/faction-events/force-grey/r03-junior-griffon/ev-01-junior-griffon.md:156` — "> Merris (Neutral, Waterdhavian Human, he/him) :: the Tower's quartermaster, a heavyset man who records every item he issues and never asks what it is for."
- `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-01-the-legates-eyes.md:17` — "> - Orvyn Dall is a Waterdhavian Human appeals clerk in the Trades Ward district magistracy. An Occupying Devourer has ridden him for seven tendays. It keeps his brain alive, so Orvyn is aware and cannot act or speak."
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/overview.md:82` names "Dalloway" and "Pimm" without a label; the labelled entries are quoted above.
- `docs/plans/setting-compendium-research-notes/pass3/batch-wards-a.md:324` — "Campaign district magistracy: `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-01-the-legates-eyes.md:17`: "Orvyn Dall is a Waterdhavian Human appeals clerk in the Trades Ward district magistracy.""
- `docs/plans/setting-compendium-research-notes/pass3/batch-wards-b.md:602` — "- **Harl Pimm** (Lawful Neutral, Waterdhavian Human, he/him): "Harl Pimm (Lawful Neutral, Waterdhavian Human, he/him) :: a stolid Dock Ward constable who counts lamp oil in every theater on his route, drinks Kreb's free tea, and has never in his life seen a drow." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:176`"
- `.claude/skills/ember-adventure-style/SKILL.md:143` and `.claude/skills/ember-setting-style/SKILL.md:206` (quoted in the name section).
- `campaign/guides/players-guide/character-creation.md:63` — "| Chondathan Freebooter | Strong | Sword Coast maritime culture at home in a major port city. |" (a background, not an NPC label); `:70` — "| Mulhorandi Tomb Raider | Situational | A scholar's angle, investigation-focused, with a knowledge base nobody local shares. |"; `:75` — "| Rashemi Wanderer | Situational | A strong character concept on its own, though it arrives with minimal faction ties. |"
- `sources/5etools/book/book-frhof.json:678` — "Ten of these new backgrounds correspond to regions of the Forgotten Realms described in {@area chapter 2|141|x}; these backgrounds are listed in the {@book Regional Backgrounds|FRHoF|1|Regional Backgrounds} table. Not every character from a given region needs to take a given background. For example, not all residents of {@area Mulhorand|20b|x} are tomb raiders. Conversely, you might find a given background a good fit for your character even if the character isn't from the designated region. For example, the {@background Chondathan Freebooter|FRHoF} background is a good fit for many pirate characters from any region."
- `sources/5etools/book/book-frhof.json:9434` — `"Waterdhavian"`, a row of the "Cheese Variety" table (`book-frhof.json:9380–9436`); a cheese, not an ethnicity.
- `sources/5etools/book/book-frhof.json:368` — "The two most common dwarven ethnicities are shield dwarves and gold dwarves."
- `sources/5etools/book/book-frhof.json:1707` — "Many realms, ethnicities, and cultural groups in Faerûn have their own language they use in addition to Common."
- `sources/5etools/book/book-frhof.json:1275` — "Except in the most remote or insular places, Faerûnians are accustomed to seeing people of different cultures, ethnicities, and species."
- `sources/5etools/book/book-scag.json:50` — "Except in the most remote or insular places, Faerûnians are accustomed to seeing people of different cultures, ethnicities, and races."
- `sources/5etools/book/book-scag.json:6355` — "If your Dungeon Master allows this option, then any human from an ethnic group that has its own language is assumed to know that language as well as Common. This ethnic language is treated as a free additional language for such individuals."
- `sources/Act_III_Arc_D.md:467` — "**Arcana Research (DC 13 Intelligence):** The construct is a nimblewright — a rare Luskanite creation based on ancient Calishite designs, not previously documented operating in Waterdeep." (a design origin, not an NPC label)
- `sources/Appendix_C_-_Player_Faction_Missions.md:1146` — "**Gysheer Omfreys** (LE female Tethyrian human **Cult Fanatic**). An Asmodeus cultist, connected to the Cassalanter network but not part of the inner circle."
- `sources/Appendix_C_-_Player_Faction_Missions.md:1062` — "A working-class inn on Endshift Street in the Field Ward — named because its clientele works in shifts and the establishment never closes. Trevar, the innkeeper, is a heavyset Illuskan man running out of guards willing to work the night shift."
- `sources/Appendix_D_-_Running_the_Tavern.md:1435` — "*Lords' Alliance — N male Cormyrean human, Veteran*" (Cormyrean as a label)
- `sources/Appendix_D_-_Running_the_Tavern.md:1198` — "Stannis (CG male Illuskan human, Commoner) is twelve years old and genuinely good at his job."
- `sources/Appendix_D_-_Running_the_Tavern.md:690` — "*NE male Calishite human, Commoner. An illusionist who performs \"music.\" Nothing is real.*"
- `campaign/guides/trollskull-manor/08-notable-patrons.md:107` — "**Jalester Silvermane** *(Lords' Alliance, LG male Chondathan Human, Spy; see **The Lords' Alliance** organization page)*" (agrees with WDH)
- `campaign/guides/trollskull-manor/08-notable-patrons.md:48` — "**Renaer Neverember** *(Noble stat block, CG Illuskan human)*" (agrees)
- `campaign/guides/trollskull-manor/08-notable-patrons.md:82` — "**Hammond Kraddoc** *(Vintners' Guild, N male Illuskan human, Commoner)*" (agrees)
- `campaign/setting/organizations/07-bregan-daerthe.md:45` — "**Khafeyta Murzan** — Human" (no ethnicity); `campaign/setting/organizations/09-manshoons-zhentarim.md:33` — "**Kaevja Cynavern** — Human" (no ethnicity)

### Not found

- **FRHoF "ethnic" hits.** Five lines contain "ethnic" (368, 576, 581, 1275, 1707). Lines 368, 581, 1275 and 1707 are quoted above; line 576 is the "Diverse Ethnicities" heading. None gives a Waterdeep breakdown.
- **FRHoF personal names.** Searched for "(Male)", "(female)", "surname", "given name", "first name", "family name", "last name", "Names:": no hits. FRHoF has no personal-name lists.
- **FRHoF "Mulan", "Turami", "Tuigan", "Chultan", "Shou" (as a people), "Tethyrian" (as an ethnicity).** No ethnicity sentence found. See the per-ethnicity notes in section A.
- **FRHoF Waterdeep ethnic breakdown.** None. The Waterdeep passages are at `book-frhof.json:4530` (heading), `:4541` (wards) and `:4444` (Sword Coast).
- **SCAG Waterdeep ethnic breakdown.** None. The Waterdeep chapter starts at `book-scag.json:3351`; its ward inset (3388–3455) gives no ethnicity.
- **SCAG table for human ethnicities.** None. The section is entries, not a table (`book-scag.json:6074`).
- **Player's Handbook nine.** SCAG says "Nine human ethnicities in Faerûn are detailed in the Player's Handbook." (`book-scag.json:6078`). The PHB is not in `sources/5etools/`, so the nine cannot be named from these files.
- **WDH stat labels for Mirt, Vajra, Volothamp, Dagult, Remallia and Laeral.** None. These names appear in WDH only with "human" or species words, never with an ethnicity.
- **WDH "Waterdavian" inside a label.** None. The word appears only as a noun or adjective (see the table note).
- **Chultan as an ethnicity in FRHoF or SCAG.** None. The only people-use is WDH line 1557 (`"{@i NG female Chultan human priest of Waukeen}"`) and the wiki's Tashalar split (`code-legal-and-magisters/wiki.txt:860`), which is a different country.
- **Campaign ethnicity labels for Sora Cuttle, Westra Moltimmur, Ered Payno, Havi Termock, Savara Firethorn, Claudio Benzreck, Xia Shung, Arthright Grayfalcon, Salazar Lorrance, Mavia Oxlander, Rowan Evenwood, Iokaste Daliano, Yaliek Iltizmar, Shan Chien, Marta, Volkarr Kibbens, Urlaster Ghann, Justyn Rassk.** Searched by name with ethnicity words in `campaign/`: no label found.
- **Wiki Waterdeep ward breakdown.** None. The wiki gives city-wide race only (`waterdeep-overview/wiki.txt:25`).
- **Ulutiun and Tuigan in WDH.** No hits. **Turami in WDH:** lines 7133, 7202, 7634, 10638, 14783, 30120, 30222.
- **"Waterdhavian" in the wiki as an ethnicity.** None. The wiki's hits are for the redirect, holidays and a cheese (`waterdeep-overview/wiki.txt:5`, `:23`, `:224`, `:246`).

### Not readable

- **`sources/Other remix files/*.docx` (12 files)** cannot be opened by the research tools. They may hold NPC ethnicity labels. Per `sources/SOURCE_GUIDE.md`:
  - Line 694: "| `The 3 Urchins NPC Guide.docx` | Nat, Squiddly, and Jenks — personalities, street knowledge, quest hooks, how to use them as recurring contacts | **Trollskull Alley**; any urchin interaction |" (relevant to Nat and Jenks, whose Notable Figures pages give "Human street urchin").
  - Line 692: "| `Meloon Wardragon NPC Guide.docx` | Meloon as a Force Grey contact; his mind-control situation (Ahghairon's Dragonward), morale, and redemption arc | **Trollskull Alley** (faction recruitment), the **Force Grey** organization page (Force Grey section) |" (relevant to the Meloon conflict).
  - Line 690: "| `Jarlaxle Baenre NPC Guide.docx` | Jarlaxle's personality, tactics, goals, and the Bregan D'aerthe operation; how to play him | **Fireball!**, **Sea Maidens Faire**; the **Bregan D'aerthe** organization page (Bregan D'aerthe section) |" (Jarlaxle's disguise).
  - Line 695: "| `The Waterdavian’s Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` | Broad NPC reference — use as a secondary source; the individual guides above supersede this where they overlap | Secondary reference only |" (the most likely place for a population or ethnicity note).
  - The other docx files, by SOURCE_GUIDE line: `Cassalanters, their tragic backtstory, and Endgame setup.docx` (:687), `Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` (:688), `Gale of Waterdeep in Waterdeep Dragon Heist.docx` (:689), `Lif and the Haunting of Trollskull Manor.docx` (:691), `Renaer Neverember Guide, his backstory and family secrets.docx` (:693), `Vajra Safahr, Zelifarn, and Deepwater Harbor quests.docx` (:696), `Xoblob_s Shop, NPC guide to his trinkets and roll tables.docx` (:697), `Zardoz Zord (and extra side quest hook).docx` (:698).
- **Alexandrian PDFs (30 files, `sources/1–30 *.pdf`)** were not text-searched. The research tools cannot grep PDFs, and none was opened for this topic.
- **`sources/research/pass2-bundles/`** was not searched for ethnicity. A grep of `sources` for ethnicity terms returned two hits there (`talos/5etools.md:1`, `valkur/5etools.md:2`), both unrelated to ethnicity.
