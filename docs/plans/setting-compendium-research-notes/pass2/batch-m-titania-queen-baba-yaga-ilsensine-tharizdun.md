# Batch M research report: five warlock patrons (Titania, Queen of Air and Darkness, Baba Yaga, Ilsensine, Tharizdun)

## Conventions

- Wiki quotes drop the `[[ ]]` link brackets. For a piped link `[[target|text]]` the visible text is kept and the target is dropped. For an external link `[url text]` the URL is kept. Italic `''` and bold `'''` markup is kept as written. Nothing else is changed.
- Wiki line numbers come from Grep -n on `wiki.txt`. The 5etools line numbers come from the Read of `5etools.md`. Campaign and adventure lines come from Grep -n or Read on the source files.
- Bundle root, used in the citations below: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/`.
- Source ranking: campaign files, then the published adventures, then the wiki (edition tagged), then 5etools. The Alexandrian files were not read for this batch.

## 0. Bundle status and name searches

**0a. 5etools (deities.json).** Only Tharizdun has entries. The other four return the same line:

> "No 5etools deities.json entry for this name."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/5etools.md:1`

> "No 5etools deities.json entry for this name."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/5etools.md:1`

> "No 5etools deities.json entry for this name."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/5etools.md:1`

> "No 5etools deities.json entry for this name."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/5etools.md:1`

**0b. Bundle files that are empty** (Read returned "the file exists but the contents are empty"): `titania/campaign-hits.txt`, `queen-of-air-and-darkness/campaign-hits.txt`, `queen-of-air-and-darkness/adventure-hits.txt`, `baba-yaga/campaign-hits.txt`, `baba-yaga/adventure-hits.txt`, `ilsensine/adventure-hits.txt`, `tharizdun/campaign-hits.txt`, `tharizdun/adventure-hits.txt`.

**Non-empty bundle files.** `titania/adventure-hits.txt` is one line, the Fey Day paragraph (section 1f). `ilsensine/campaign-hits.txt` is one line, `arc-j-vault-of-dragons.md:154` (section 3f).

**0c. Name searches confirmed against the sources.** Searched `sources/adventure-wdh.json` and `sources/adventure-wdmm.json` (Grep -n, case-insensitive) and all of `campaign/`. Terms: titania, queen of air, unseelie, seelie, baba yaga, tharizdun, chained god, elder elemental, eater of worlds, ilsensine, ilsen, great brain, elder brain, god-brain, maanzecorian, tentacled lord, archfey, great old one, grandmother, bone mother, mother of all witches, little grandmother, hyrsam, oberon.

- **adventure-wdh.json.** Two lines match the name terms. One is the Fey Day paragraph (section 1f). The other is a false hit on the word "grandmother":

> "A lifelong bachelor, Barnibus has a small, tidy estate  in the Sea Ward that he inherited from his grandmother.  When not serving the Watchful Order, he spends his  days reading and writing books in his library."
— `/home/user/waterdeep/sources/adventure-wdh.json:31775`

  This is Barnibus Blastwind's grandmother, not Baba Yaga.
- **adventure-wdmm.json.** No line matches the name terms. The word "Far Realm" appears in many lines, and "elder brain" appears in four lines (section 3h). None names Ilsensine, the Great Brain, the god-brain or a mind flayer god.
- **campaign/.** The name terms match one structure-file line (`arc-j-vault-of-dragons.md:154`, section 3f). "Warlock" and "archfey" match only `campaign/setting/deities/asmodeus.md:62` and `:123` (quoted in section 9). "Far Realm" and "Great Old One" match no campaign line.

---

## 1. Titania (Summer Queen, Faerie Queen, Queen of Light)

Wiki page: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt`.

### Answers (Titania)

**(1) Waterdeep cult, shrine or temple.** None in any source. The wiki has no Waterdeep line (section 1f). The only Waterdeep mention in the published adventure is a festival, not a cult, shrine or temple.

**(2) Campaign NPC, faction or quest that uses it.** None names Titania. The campaign's Fey Day entries (section 1f) use the festival and name no patron.

**(3) Wiki lines that mention Waterdeep.** None.

### 1a. Identity (wiki infobox)

> "| title               = Summer Queen<br />Faerie Queen<br />Queen of Light"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:11`

> "| pantheon            = Seelie Court"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:15`

> "| power5eR            = Archfey"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:25`

> "| power5e             = Archfey"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:40`

> "| homeplane5e         = Feywild"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:43`

> "| refs5e              = <ref name="SCAG-p138"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:55`

> "| power4e             = Archfey"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:56`

> "| dominion4e          = Feywild"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:59`

> "| realm4e             = Senaliesse"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:60`

> "| power2e             = Greater deity"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:87`

> "| alignment2e         = Chaotic good"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:88`

> "| symbol2e            = White diamond & blue star"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:89`

> "| portfolio2e         = Fey, friendship, magic"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:94`

> "| worshipers2e        = Fey"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:96`

> "'''Titania''' (also known as '''Tiandra'''<ref name="MotP4e-pp36-37" />) was the '''Summer Queen''' of the Feywild,<ref name="DMG5eR-p362" /><ref name="SCAG-p138" /><ref name="MotP4e-pp36-37" /> leader of the Summer Fey,<ref name="MotP4e-pp36-37" /> and possibly the mightiest of all archfey.<ref name="DMG5eR-p362" /><ref name="SCAG-p138" /> She was also known as the '''Faerie Queen'''<ref name="MM-p119" /><ref name="OHG-p137" /> and the '''Queen of Light'''<ref name="FF-S&UC" /> and led the Seelie Court.<ref name="DMG5eR-p362" /><ref name="FF-S&UC" /><ref name="MM-p119" /><ref name="OHG-p137" /><ref name="DD-p92">{{Cite book/Demihuman Deities|92}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:125`

> "| based               = William Shakespeare's Titania"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:122`

Stat note. No challenge rating or 5e statistics. `challenge5e` and `class5e` are empty (`titania/wiki.txt:53` and `:54`).

### 1b. Form, personality, powers, possessions

> "Titania appeared as an eladrin of immense beauty. Her skin was the color of honey and her hair shimmered in all of the colors of autumn leaves. Her eyes glowed with gold like the sun.<ref name="MotP4e-pp36-37" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:128`

> "Alternatively, her avatar would appear as a small but beautiful gossamer-winged fairie with flawless, pale skin and immaculate cheekbones and gray-blue eyes.<ref name="MM-p119" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:130`

> "Titania was hard to classify personality-wise.<ref name="OHG-p137" /> She seemed flighty and frivolous to some, but in truth she was a brilliant strategist both in court and on a battlefield. She had a dry sense of humor and could be very pragmatic when needed.<ref name="MotP4e-pp36-37" /> It was almost impossible to make her angry, but if a truly despicable act roused her ire, the perpetrator would be faced with the most powerful wrath!<ref name="MM-p119" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:133`

> "Titania was amused by mortals and had been known to take some as lovers.<ref name="MotP4e-pp36-37" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:135`

> "Titania's very smile could cause crops to ripen, and her frown could trigger wildfires.<ref name="SCAG-p138" /><ref name="MotP4e-pp36-37" /> Her gaze could cause mortals to go mad.<ref name="MotP4e-pp36-37" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:138`

> "Titania always carried a diamond-tipped wand, and her avatar fought with a magic dagger."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:143`

### 1c. Realm

> "The Seelie Court was also the name of Titania's realm. It had no permanent location but instead wandered from plane to plane, from the Beastlands to Arborea to Ysgard.<ref name="OHG-p137" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:146`

> "Titania's palace was Senaliesse, where she held her Summer Court."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:150`

> "Titania's throne was ornately carved from ice in the shape of a dragon. (It was a mirror of the Queen of Air and Darkness's throne, except that that one was made of darkness and shadow.) The throne was in fact a magical construct that could serve as a guardian if needed.<ref name="FF-S&UC" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:152`

### 1d. Activities, worship, clergy

> "Titania watched over all fey beings, be they dryads, pixies, satyrs, treants, unicorns, or any of the other nearly countless varieties, desiring that all such creatures could someday live in utter joy.<ref name="OHG-p137" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:155`

> "When the Seelie Court met, Titania's avatar was always present and almost always accompanied by at least one other member of the Inner Circle of the Court. All faeries knew when and where the Court would be meeting.<ref name="MM-p119" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:157`

> "If harm ever came to faerie lands, Titania would not hesitate to send her avatar to intervene.<ref name="MM-p119" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:159`

> "Titania was worshiped by a plethora of non-evil fey beings. Brownies, bookas, pixies, and sprites considered her their patron deity.<ref name="MM-p119" /> Titania, like other sylvan gods, did not grant spells to her followers, nor did she have priests or clerics, for all fey creatures had magical powers of their own.<ref name="MM-pp117-118" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:177`

> "Titania's followers taught that she was a goddess of goodness and mercy.<ref name="MM-p119" /> They saw her as a mother figure.<ref name="MM-pp117-118" /> Her holy symbol was a white diamond with a blue star.<ref name="MM-p119" /><ref name="OHG-p137" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:179`

> "Periodically, Titania hosted a parliament of all the separate fey courts—seelie and unseelie—at Senaliesse, which was sometimes called the Court of Stars.<ref name="MotP4e-pp36-37" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:182`

Holy days, temples and omens: none in the wiki (holy-day fields are empty, `titania/wiki.txt:36`, `:52`, `:68`, `:83`, `:98`).

### 1e. Relations and origin

> "Titania had a famous love affair with Oberon, the Green Lord,<ref name="SCAG-p138" /><ref name="MotP4e-pp36-37" /><ref name="OHG-p137" /> and it was he who built her palace.<ref name="MotP4e-pp36-37" /> Some even called the couple husband and wife, while admitting that both took other lovers freely.<ref name="OHG-p137" /> At other times, they were also great enemies;<ref name="SCAG-p138" /><ref name="MotP4e-pp36-37" /> at still other times, they were both lover and foe at the same time.<ref name="MotP4e-pp36-37" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:162`

> "Damh, the god of satyrs and korreds, was seen as Titania and Oberon's son. Verenestra, the goddess of dryads, was considered Titania's daughter.<ref name="MM-pp117-118" /> The Prince of Frost was also a son of Titania.<ref>{{Cite dragon/374/Court of Stars: The Prince of Frost}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:164`

> "The so-called "Inner Circle" of sylvan gods respected Titania as their queen and deferred to her in matters of judgment. Skerrit, god of centaurs, and other "Outer Circle" gods did not follow Titania's rule, but she had great love for them and their worshipers nonetheless.<ref name="MM-pp117-118" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:166`

> "The Seldarine were on good terms with Queen Titania and were willing to aid her whenever she requested it of them.<ref name="OHG-p137" /><ref name="DD-p92" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:168`

> "The Queen of Air and Darkness was rumored to be the dark sister of Titania. Whatever the truth, Titania refused to wage open war against the evil queen and instead grieved for her.<ref name="MM-pp117-118" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:170`

> "Titania's niece, Lady Shandria, governed Astrazalian, the City of Starlight in the Feywild.<ref name="MotP4e-p41">{{Cite book/Manual of the Planes 4th edition|41}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:174`

Origin and rise. The wiki gives no origin story for Titania beyond the courts and titles above. Edition tags: the Oberon line (162) cites SCAG (5e), MotP (4e) and OHG (2e); the Prince of Frost line cites a Dragon issue.

### 1f. Warlock and Waterdeep

> "Titania was a patron to many warlocks in the Realms.<ref name="SCAG-p138" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/titania/wiki.txt:184`

Waterdeep, wiki: no line. Grep for `waterdeep|waterdhav` on this file returned no match.

Waterdeep, published adventure. The Fey Day heading:
> "Ches 19: Fey Day"
— `/home/user/waterdeep/sources/adventure-wdh.json:31381`

> "The veil between this world and the faerie realm of the Feywild is thought to be weak on this day. Though this phenomenon provokes caution in rural areas (with folk avoiding woodlands, putting offerings of food on doorsteps, and the like), it is an occasion of much drinking, singing, and dancing in Waterdeep. The wealthy host elaborate masked balls, while poorer folk don costumes of their own make and travel door to door, gaining brief entry into the celebrations in exchange for performing a song or a short play. All adopt the guises of fey beings and the supposed rulers of the Feywild, such as Queen Titania, Oberon, and Hyrsam, the Prince of Fools. Those inclined to remain sullen in the face of such frivolity had best stay home, for celebrants do their utmost to evoke a smile from those they meet."
— `/home/user/waterdeep/sources/adventure-wdh.json:31385`

Campaign, the festival calendar. None of these lines names a patron:
> "| Ches 19 | Fey Day | **Trollskull Alley** | Masked balls the day before the Grand Opening |"
— `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:61`

> "| Ches 19 | Fey Day | The wealthy host masked balls and poorer folk in homemade costume go door to door performing a song or short play. |"
— `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:102`

> "- **Fey Day, Ches 19.** Masked balls run all evening, so a masked guest at any noble house draws no remark. The Grand Opening of Trollskull Manor follows the next day."
— `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:115`

> "> - **Research:** The Midsummer wiki page, and pages for Twin Parades, Selûne Sashelas and Fey Day, are not in the wiki folder. Midsummer is housed from the Calendar of Harptos, Shieldmeet and published-adventure entries only. Fey Day uses the published adventure."
— `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:157`

### 1g. Titania: not found and conflicts

- Not found: Waterdeep cult, shrine or temple (wiki, adventures, campaign). Clergy, holy days, omens, messengers (the wiki says she had no priests, `titania/wiki.txt:177`). 5e statistics. Campaign mentions. Any 5etools entry.
- Conflict: none between sources. Within the wiki, the 2e column gives alignment "Chaotic good" (`titania/wiki.txt:88`) and the 5e columns give no alignment, so no 5e alignment can be sourced.

---

## 2. Queen of Air and Darkness

Wiki page: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt`.

### Answers (Queen)

**(1)** None. No Waterdeep cult, shrine or temple in any source.
**(2)** None. No campaign file or adventure line names her.
**(3)** None. Grep for `waterdeep|waterdhav` returned no line.

### 2a. Identity (wiki infobox)

> "| pantheon            = The Unseelie Court"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:11`

> "| power5eR            = Archfey"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:23`

> "| power5e             = Archfey"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:38`

> "| refs5e              = <ref name="SCAG">{{Cite book/Sword Coast Adventurer's Guide|138}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:53`

> "| power3e             = Intermediate deity"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:69`

> "| alignment3e         = Chaotic evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:70`

> "| symbol3e            = Black diamond"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:71`

> "| homeplane3e         = Pandemonium"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:72`

> "| realm3e             = The Unseelie Court"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:73`

> "| portfolio3e         = Darkness, magic, murder, evil fey"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:76`

> "| domains3e           = Air, Chaos, Darkness, Trickery"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:77`

> "| power2e             = Intermediate deity"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:85`

> "| alignment2e         = Chaotic evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:86`

> "| symbol2e            = A ten-faceted black diamond"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:87`

> "| homeplane2e         = Pandemonium"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:88`

> "| portfolio2e         = Magic (particularly illusion), darkness, murder"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:92`

> "| worshipers2e        = Evil elves and fey"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:94`

> "The '''Queen of Air and Darkness''' was a powerful archfey who ruled over the Unseelie Court.<ref name="DMG5eR-p360" /><ref name="MM"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:123`

Stat note. No 5e statistics. `challenge5e` and `class5e` are empty (`queen-of-air-and-darkness/wiki.txt:35` and `:36`, with `:51` and `:52` for the 5e block).

### 2b. Form, possessions, realm

> "The Queen of Air and Darkness had no physical form; her presence was merely felt in the Unseelie Court. If magic was used to see her, however, she appeared as a beautiful but terrible female faerie with angular features, bone-white skin, all-black eyes, and long black hair.<ref name="MM"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:126`

> "The Black Diamond, sometimes called the Night Diamond, was an artifact of immense power and evil of unknown origin. It sat atop her throne in the Unseelie Court."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:131`

> "The Queen of Air and Darkness ruled over the Unseelie Court, the divine realm of the fey pantheon of the same name, which accounts variously placed as being either in Phlegethon in Pandemonium<ref name="MM"/><ref name="D359"/> or in the Plane of Faerie.<ref name="SCAG"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:134`

### 2c. Relations and worship

> "The Queen of Air and Darkness reigned over the Unseelie Court, the foes of the Seelie Court.<ref name="DHD-p92">{{Cite book/Demihuman Deities|92}}</ref> She was opposed by the elven deities of Seldarine, namely Corellon Larethian, Erevan Ilesere, Rillifane Rallathil, Sehanine Moonbow, Solonor Thelandira, and Angharradh. To them, she personified the corruption that could grow even in those of fey lineage.<ref>{{Cite book/Demihuman Deities|97,100,108,120,125,132-133}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:138`

> "[[Auril]] the Frostmaiden was believed to be synonymous with the Queen of Air and Darkness by some communities of fey, such as those of the Shiverpine Forest in the Deep Wilds.<ref>{{Cite dragon/367/Hall of the Frostmaiden|60}}</ref><ref group="note">In this [https://twitter.com/TheEdVerse/status/1228370295649599488 tweet], Ed Greenwood agrees that the Queen of Air and Darkness was impersonating Auril, with Auril's support, to gain more followers on Toril.</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:140`

Note on the line 140 quote. The first link is kept as written (its brackets are the only markup removed here, shown as `Auril` in the text above). The wiki cites the Auril link to Dragon 367 (Hall of the Frostmaiden, a 5e-era adventure, per the cite name).

> "She was served by unseelie fey, including brambles, quicklings,<ref name="DHD-p92"/> and spriggans.<ref name="PoC-TBoC-p90">{{Cite book/Planes of Chaos/The Book of Chaos|90}}</ref> She was also known to have a fondness for yeth hounds and hell hounds.<ref name="PoC-TBoC-p100">{{Cite book/Planes of Chaos/The Book of Chaos|100}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:143`

> "The glouras, fey beings of the Underdark, had ties to the Queen of Air and Darkness and the Unseelie Court.<ref name="DDGttUD-p30">{{Cite book/Drizzt Do'Urden's Guide to the Underdark|30}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:145`

### 2d. Origin

> "Once, the Queen of Air and Darkness was the sister of Queen Titania, ruler of the fey, in the land of Ladinion. But one day a group of dwarves, who had been mining in a mountain to the south, brought to the Seelie Court a great, ten-faceted black diamond they had found as a gift for the fey queen. However, Titania was away swimming that day so her sister accepted the gift. This diamond began to corrupt her, transforming her nature, and one day she took the diamond and other magical treasures and left in a chariot of smoke and fire that was said to have appeared out of the sky. Some time later the mountain that the dwarves were mining exploded, slaying the dwarves and causing sickening smoke to cover the land.<ref name=MM(2)">{{Cite book/Monster Mythology|117-118}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:148`

Edition tag. The origin is cited to Monster Mythology pp. 117–118, which the infobox gives as its 2e entry (`queen-of-air-and-darkness/wiki.txt:98`).

### 2e. Warlock

> "[[Category:Archfey patrons]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/queen-of-air-and-darkness/wiki.txt:165`

Brackets are dropped from this category line in the wiki's own form. The category is the only warlock-related text. No wiki line gives a pact or a warlock term for her.

### 2f. Not found and conflicts

- Not found: Waterdeep (any kind). Clergy, holy days, temples, omens, messengers (holy-day and temple fields are empty, `queen-of-air-and-darkness/wiki.txt:96`, `:109`, `:120`, `:121`). Campaign and adventure mentions. Pact terms. 5e statistics. 5etools entry.
- Conflict: the wiki gives two homes for the Unseelie Court in one sentence, "Phlegethon in Pandemonium" (MM, Planes of Chaos) and "the Plane of Faerie" (SCAG) (`queen-of-air-and-darkness/wiki.txt:134`). Both are the wiki's own accounts.

---

## 3. Ilsensine (wiki only; the campaign names it once)

Wiki page: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt`. Line numbers are Grep -n numbers. (The Read tool numbers the first 139 lines one lower; only Grep numbers are cited.)

### Answers (Ilsensine)

**(1)** None. The wiki's worship places are in Oryndoll, the Caverns of Thought and the Dalelands (Mistfall). Grep for `waterdeep|waterdhav` on this file returned no line.
**(2)** One campaign line names Ilsensine: `arc-j-vault-of-dragons.md:154`, the Vault of Dragons structure document (section 3f). No campaign file ties Ilsensine to Nihiloor, to any faction, or to any NPC.
**(3)** None.

### 3a. Identity (wiki infobox)

> "| title               = The Tentacled Lord<ref name="Id2e-p53" /><br /> The Great Brain<ref name="OHG2e-p136"/><ref name="DDGttUp83"/><ref name="SatO-p94" /><br />  The God-Brain<ref name="PCS-SB2e-p32-33">{{Cite book/Planescape Campaign Setting/Sigil and Beyond|32-33}}</ref><ref name="PaB.TSO-p197" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:7`

> "| power5e             = Deity"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:37`

> "| homeplane5e         = Outlands<br/> {{Former}} Far Realm"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:40`

> "| realm5e             = Caverns of Thought"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:41`

> "| portfolio5e         = Mastery of the mind, psionics"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:44`

> "| worshipers5e        = Mind flayers"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:46`

> "| power3e             = Greater deity"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:66`

> "| alignment3e         = Lawful evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:67`

> "| homeplane3e         = Deep Caverns"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:69`

> "| portfolio3e         = Conquest, knowledge, magic, mental dominion, mental power"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:73`

> "| worshipers3e        = Illithids"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:76`

> "| power2e             = Greater deity"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:82`

> "| alignment2e         = Lawful evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:83`

> "| symbol2e            = Glowing brain with two tentacles"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:84`

> "| homeplane2e         = Concordant Opposition"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:85`

> "| servedby2e          = Maanzecorian (dead)"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:88`

> "| portfolio2e         = Mental dominion, magic"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:89`

> "| worshipers2e        = Illithids"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:91`

Stat note. No challenge rating or 5e statistics. The 5e block gives only "Deity", the Outlands and Caverns of Thought, and "Mastery of the mind, psionics" (lines 37–46).

Definition paragraph (one line):

> "}}'''Ilsensine''' (meaning "great brain" or "powerful brain" in Undercommon)<ref name="Dr281-p48-49">{{Cite dragon/281/By Any Other Name|48-49}}</ref><ref name="DDGttUp83">{{Cite book/Drizzt Do'Urden's Guide to the Underdark|83}}</ref><ref group="note">Technically by the order of the prefix and suffix, Ilsen meaning brain and sine meaning great or powerful, this would be more literally read as "brain great" or "brain powerful", but is interpreted to align with the given title of "The Great Brain".</ref> was the patron deity and creator of the illithids,<ref name="OHG2e-p136" /> and the '''Tentacled Lord'''  embodied their ideals of mental prowess, unlimited knowledge, and willful dominion over all other lifeforms.<ref name="LoM3e-p177" /> Although predominantly focused on mind flayers, the '''God-Brain''' was the patron of all beings that enslaved the thoughts of others.<ref name="EPH3e-p222" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:117`

> "Ilsensine was known as such by the sages and scholars of most races, but illithids identified them differently. Rather than a name, telepathically communicating mind flayers used a series of visual images and symbolic denotations to represent it.<ref name="MMy2e-p61">{{Cite book/Monster Mythology|61}}</ref> A psionic inflection used to mark Oryndoll as a holy place of Ilsensine was enough to cause fear in those minds the name was projected into.<ref name="DDGttUp74">{{Cite book/Drizzt Do'Urden's Guide to the Underdark|74}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:119`

> "{{quote|Knowledge is the only power.|Ilsensine<ref name="Finder-ch13">{{Cite book/Finder's Bane||13}}</ref>}}"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:121`

### 3b. Form and personality

> "A being of the mind and spirit, Ilsensine lacked any physical body, instead incarnating as a cohesive thought."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:124` (the rest of the paragraph covers the emerald manifestation and the tendrils, cited to Id2e, OHG2e, LoM3e and MMy2e)

> "When incarnating in an avatar, Ilsensine's floating form was much easier to comprehend, appearing as spectral {{SI|8|ft|long=yes}} across, green-glowing brain with only two tentacles.<ref name="MMy2e-p68" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:126`

> "Alien and elusive,<ref name="CC-PC">{{Cite web/Class Chronicles: Psionic Classes}}</ref> Ilsensine's thoughts were a relentless tide of dark deceptions and unimaginable deviancy."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:133`

> "Another dominating facet of Ilsensine's unending thoughts was megalomania<ref name="PCS-SB2e-p32-33" /> for its motivation was the supremacy of the greatest race in its mind; its own illithid creations."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:135`

> "Despite its many strengths, Ilsensine was not infallible. Aside from being supremely arrogant,<ref name="MMy2e-p68" /> Ilsensine was not impervious to emotion, and in fact, could be overtaken by it."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:143`

### 3c. Powers, possessions, the Caverns of Thought

> "Ilsensine was ultimately about one thing; power, specifically raw, psychic power."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:148` (the rest of the paragraph covers brain burn and the nulling of psionics, cited to Planescape 2e)

> "Compensating for this was its incredible magical might, granting its avatar the power to cast any spell the most powerful of wizards could."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:152` (the rest of the paragraph covers mass charm, mass suggestion, prismatic spray and mind blast, cited to MMy2e-p68)

> "Ilsensine possessed at least one hidden cache of strange and alien magical artifacts deep within the Underdark.<ref name="MMy2e-p59-60" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:159`

> "Only illithid communities visited by Ilsensine's proxy Lugribossk or a manifestation of the god themselves could create the psionic bracers known as ''Tendril rings of Ilsensine''."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:162` (the rest of the paragraph covers the rings' effect on mortals, cited to Dragon 255)

> "Though often thought of as omnipresent mental energy, Ilsensine was strangely based underneath the Outlands, the outer plane of true neutrality, in its own vast, subterranean realm known as the Caverns of Thought, or sometimes simply Ilsensine's realm."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:165` (the rest of the paragraph covers persistence on other planes, cited to MMy2e, Planescape 2e)

> "Ilsensine was not welcoming of others into its realm, preferring those it could control.<ref name="PCS-17" /> Between that and the brain burn there was little reason to visit the Caverns of Thought save for one. If one could gain the god-brain's favor, likely requiring the surrender of part of one's mind (such as memory and/or sanity) as payment, they could beseech its cosmic knowledge. With Ilsensine's constant, reality-spanning sensory input and perfect memory, it likely knew more of dark secrets than any being in the cosmos, such as the weakness of any given foe.<ref name="PCS-SB2e-p32-33" /> From here it was said, one could learn the answer behind almost any planar activity, assuming they could stay sane enough to ask the question,<ref name="PCS-17" /> and most that got as far as Ilsensine's court never came back in the first place.<ref name="PCS-SB2e-p32-33" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:193`

> "Ilsensine's realm was primarily occupied by zombies, either the petitioners or planars who stayed too long. Only the very lucky left with their minds intact, and those few who left Ilsensine's court would be wise to question their wits, for none could stand before them for long without changing at least a little.<ref name="PCS-SB2e-p32-33" /> However, there were also mind flayer petitioners present, much the same in appearance and behavior as they were in life,<ref name="PGF3e-p148-149" /> and it was suspected secret portals to the Lower Planes were present as darker fiends of the Lower Planes also took up residence in and around the area when visiting the Outlands.<ref name="PCS-17" /> Even so, the only structures present were bits of wall and bedding left by those that attempted to establish themselves within.<ref name="PCS-SB2e-p32-33" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:173`

### 3d. Worship, clergy, temples (wiki)

> "Mind flayers did not worship their deity in the same sense that humans did, and were in fact incapable of true worship due to their innate and extreme egotism. Mind flayers envied its seemingly limitless knowledge and revered the god-brain for its all-sensing mental capacity,<ref name="LoM3e-p71-72" /> but they revered them as the manifestation of an idealized psionic and philosophical state of mind, the physical motions performed during occasional meditation on this ideal often being misinterpreted as proper worship.<ref name="VGM5e-p80" /> To the mind flayers, Ilsensine was the ultimate culmination of an elder brain's aspirations,<ref name="LoM3e-p71-72" /> what it (and thus any mind flayer who successfully joined in mental and spiritual union with it)<ref name="Id2e-p40-41" /> could become after innumerable eons of growth.<ref name="LoM3e-p71-72" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:231`

> "Becoming a cleric of Ilsensine also came with several disadvantages for an illithid, the most immediate of which was an extreme reduction in magical resistance performed as a simple act of will by Ilsensine itself. Without doing so, a mind flayer's magical resistance would prevent it from effectively channeling its divine power. The primary disincentive to mind flayers however was that in most communities, pledging one's self to Ilsensine was to forfeit the right to join the elder brain after death.<ref name="Id2e-p40-41" /> Mind flayers lacked a mythical view of the afterlife and gods of the outer planes, often disbelieved in the idea they had souls that went there after death,<ref name="VGM5e-p80" /> and even when aware would rather merge with the elder brain than serve Ilsensine after death.<ref name="EPH3e-p222" /> Illithids already denied the possibility of communion usually worshiped Ilsensine in hopes their souls would be taken in.<ref name="Id2e-p56">{{Cite book/The Illithiad|56}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:236`

> "These drawbacks in mind, there were mind flayers that did willingly dedicate themselves to Ilsensine. The primary advantage Ilsensine offered to mind flayer devotees was the ability to grant clerical spells, allowing them to advance their own psionics while simultaneously walking another path of power.<ref name="Id2e-p40-41" /> Mind flayer clerics provided healing their communities and acted as medics for their hunting parties. They often served as thrallmasters, capturing unusual slaves on the surface, for they could not only control the living with psionics but the undead through their spells.<ref name="EPH3e-p222" /><ref group="note"> Sourcebooks are inconsistent on whether they possess the turn undead ability most clerics possess.</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:238`

> "The secondary advantage Ilsensine offered was information. As any sane illithid understood, knowledge was power, and if one could gain its favor the answers to many difficult questions could be obtained.<ref name="Id2e-p40-41" /> Mind flayers might entreat or supplicate Ilsensine,<ref name="LoM3e-p71-72" /> but their lacking capacity for proper worship meant they only did so as the mood struck them, wandering into its temple to make boon requests or sacrifices.<ref name="LoM3e-p82" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:240`

> "Priests of Ilsensine rarely left their temples save for the performance of important ceremonies.<ref name="LoM3e-p71-72" />  Clerical illithids might conduct processions and pick thralls out for obscure purposes, and sometimes silently moved through the community on unclear errands.<ref name="LoM3e-p82" /> They lived monastically, pursuing knowledge for its own sake and engaging in psionic enhancement experiments.<ref name="LoM3e-p71-72" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:249`

> "Illithid custom saw mind flayers pray to Ilsensine upon consuming an especially delicious brain, the leftover ichor used to trace their symbol on a nearby surface. Prayers to the god-brain were performed telepathically, tentacles held perfectly still as a matter of respect.<ref name="EPH3e-p222" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:254`

> "Communities with a Venerator presence possessed temples dedicated to Ilsensine where the faithful could offer reverence,<ref name="Id2e-p53" /> generally taking the form of small, non-descript shrines in out-of-the-way corners of the community.<ref name="EPH3e-p222" /> In the cases of larger houses of worship, chambers might be attached to the central temple for the devoted to reside in.<ref name="LoM3e-p82" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:259`

> "Almost under Mistfall house was a forgotten temple that might have been devoted to Ilsensine.<ref name="VGttD-p125">{{Cite book/Volo's Guide to the Dalelands|125}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:261`

> "* Unworthy of Ilsensine: A 14{{th}} century DR cult located under the Giant's Run Mountains in the Dragon Coast, run by the mind flayer Qooql.<ref name="CoR-p.90">{{Cite book/Champions of Ruin|90}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:264`

> "* Oryndoll: Was a holy site of Ilsensine, due to the Encephalithid being the deity's avatar twice. Ilsensine's clergy was powerful in city, and controlled many shrines as well as a full temple to the deity.<ref name="DDGttUp83"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:266`

> "Though Ilsensine was the god of mind flayers, it promised power to all who followed them, so sometimes non-illithids, especially evil psions, formed cults in service to it.<ref name="EPH3e-p222" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:269`

Dogma:
> "The teachings of the god-brain were that the spawn of Ilsensine were destined to conquer the surface and establish dominion over all other races, the source of their motivation for collective dominance being the powers of their deity.<ref name="DDGttUp78" /><ref name="FRCS2E">{{Cite book/Forgotten Realms Campaign Setting 2nd edition (revised)/Running the Realms|64}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:243`

Messengers and proxies:
> "However, Ilsensine was far more likely to send a proxy than an avatar, usually dispatching Lugribossk for direct intervention and particularly for assisting a notably bold illithid plan to subjugate.<ref name="Id2e-p40-41" /><ref name="Id2e-p89" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:184`

Holy days and omens: none in the wiki (holy-day fields are empty, `ilsensine/wiki.txt:29`, `:47`, `:62`, `:92`, `:105`).

### 3e. Relations and origin (wiki)

> "Besides Maanzecorian, Ilsensine had no allies save for the drow goddess of vengeance Kiaransalee. Foes included most of the rest of the drow pantheon, including Eilistraee, Lolth, Selvetarm and Vhaeraun, the elf god of revenge Shevarash, and the deep gnome god Callarduran Smoothhands.<ref name="DD">{{Cite book/Demihuman Deities|13, 23, 26, 33, 36, 129, 143}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:199`

> "Ilsensine never rose exceptional mortal illithids to divinity, even as demigods, jealous as they were of their power and position,<ref name="MMy2e-p61" /> but they did have a servitor deity in Maanzecorian, the mind flayer god of knowledge and philosophy.<ref name="MMy2e-p68" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:195`

> "Maanzecorian's veneration could have never reached that of Ilsensine,<ref name="Id2e-p40-41" /> but he kept his priesthood small partially to avoid the appearance of trying to usurp Ilsensine's primacy. He was always deferential to the Tentacled Lord,<ref name="MMy2e-p68" /> but despite this position the god-brain was still his rival,<ref name="DG2e-p17">{{Cite book/Dead Gods|17-18}}</ref> and he did not always pass along everything he learned.<ref name="MMy2e-p68" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:197`

> "Ilsensine had a notably complex relationship with deities of dwarven origin. They enjoyed an obscure, non-hostile relationship with Dumathoin,<ref name="F&P3e-p118">{{Cite book/Faiths and Pantheons|118}}</ref> dwarven god of underground exploration, but the exact relationship was unknown to other gods and their followers had no such accord.<ref name="DD-60">{{Cite book/Demihuman Deities|60}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:201` (the rest of the paragraph covers Deepshaft Hall and a mind-wiped petitioner sent as a spy)

> "There was a fierce enmity between Ilsensine and Deep Duerra, the duergar god of psionics, for she had stolen several secrets of the Invisible Art and robbed it of psionic energy many times.<ref name="F&P3e-p117">{{Cite book/Faiths and Pantheons|117}}</ref><ref name="RoF">{{Cite book/Races of Faerûn|16}}</ref><ref name="DD-54">{{Cite book/Demihuman Deities|54}}</ref> Besides hating Duerra, Ilsensine had also long sought vengeance against her superior Laduguer for some ancient slight.<ref name="DD-71">{{Cite book/Demihuman Deities|71}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:210`

> "Ilsensine was a mystery of the cosmos, their true origin nigh-impossible to discern.<ref name="Id2e-p40-41" /> This origin was made even more confusing given the origins of the mind flayer race in the future prior to their grand act of time travel<ref name="LoM3e-p71-72" /> and the conception that the god-brain's omnipresence extended throughout time.<ref name="MMy2e-p61" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:278`

> "In any case, Ilsensine was held by the illithids as the Creator God,<ref name="MMy2e-p61" /> and allegedly existed alongside other deities before they created mortals.<ref name="Id2e-p40-41" /> Illithids held that while other divine beings blundered in the Material Plane trying to stake claims with proto-creations, Ilsensine patiently perfected its own, the mind flayers being the result of an aeons-long series of experiments to craft the perfect species.<ref name="MMy2e-p61" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:280`

> "Ilsensine made itself known in the Realms immediately following the duergar uprising in Oryndoll against the illithids in approximately {{Yearlink|-4000}}. The established governing bodies were in disarray in the aftermath of the rebellion and the city nearly collapsed from the resulting chaos, saved only by the sudden appearance of an avatar of Ilsensine, believed to have been summoned by its elder brain.<ref name="DDGttUp75">{{Cite book/Drizzt Do'Urden's Guide to the Underdark|75}}</ref><ref name="FRCSp213">{{cite book/Forgotten Realms Campaign Setting|213}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:283`

> "Sometime in the mid-14{{th}} century, Maanzecorian died before the demon lord Orcus, at the time a god of undeath known as Tenebrous, making Ilsensine the unquestioned supreme god of the mind flayers. <ref name="DG2e-p124">{{Cite book/Dead Gods|124}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/ilsensine/wiki.txt:288`

Recent history and the lost shard of consciousness (lines 290 and 294) are not quoted here. Both are in the bundle file at those lines.

### 3f. Campaign: the one line that names Ilsensine

> "**The Broken Circle of Gods.** Scattered through the vault's frescoes — the Entrance Foyer's niches most explicitly — are images that should not exist: Dumathoin placing gems into a primeval range of mountains; Dumathoin visiting the illithid god Ilsensine, manifest as a disembodied emerald brain, and bathing in its psionic light; Dumathoin, Ilsensine, and Laduguer, god of the duergar, with hands clasped in a circle of friendship that official dwarven doctrine insists never existed. These images predate a falling-out between the three gods that the Morndinsamman has never fully explained. They are not necessary to **Vault of Dragons**'s plot — the party can walk past them without consequence — but a party that lingers and investigates is rewarded with one more thread connecting the vault's dwarven history to the deep, patient intelligences (illithid and aboleth alike) that the Undermountain campaign will eventually make explicit."
— `/home/user/waterdeep/campaign/structure/arc-j-vault-of-dragons.md:154`

Status. This is a structure document, pending conversion to a quest journal (CLAUDE.md). It is the only campaign authority for the line.

### 3g. Nihiloor and the Great Brain or elder brain

Brief check. No campaign line names Ilsensine, the Great Brain, the god-brain or an elder brain in connection with Nihiloor. Grep for `elder brain|great brain|ilsensine|god-brain|tentacled|nihiloor` on `campaign/` gave the Nihiloor lines below and no others that name a god or an elder brain.

Folder check. `campaign/setting/notable-figures/force-grey/` does not exist (Grep and Glob returned nothing). Nihiloor's notable-figure page is `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md`.

> "- *Mind flayer, lawful evil*. Stat block: **Mind Flayer**."
— `/home/user/waterdeep/campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:6`

> "**Motivations.** Nihiloor wants to breed and deploy intellect devourers throughout Waterdeep, pursue its own fell schemes independent of Xanathar's goals, and observe the Grand Game from within the shadows where no one looks."
— `/home/user/waterdeep/campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:16`

> "**Relationships.** Nihiloor is the intelligence and infiltration specialist of Xanathar's Guild, the creator of the intellect devourer that occupies Meloon Wardragon, and a mind flayer that has dominated Xanathar's mind for the last four months in a Guild where even a hint of that would get anyone else disintegrated."
— `/home/user/waterdeep/campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:26`

> "Nihiloor is the intelligence operative of Xanathar's Guild — a mind flayer who moves through the lair with unsettling calm, treating every conversation as an opportunity for study. The Guild's other members give it wide berth."
— `/home/user/waterdeep/campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:30`

> "| Nihiloor | Mind flayer operative | Trusted intelligence gatherer; Xanathar grants it unusual autonomy; plant for Mad Mage integration |"
— `/home/user/waterdeep/campaign/setting/villains/xanathar.md:50`

The Nihiloor lines name a mind flayer and the domination of Xanathar. None names Ilsensine or the Great Brain.

### 3h. Dungeon of the Mad Mage: mind flayers' god

No line in `sources/adventure-wdmm.json` names Ilsensine, the Great Brain, the god-brain or Maanzecorian. The nearest lines name an elder brain, not a god.

> "Mind flayers have established a splinter colony on this level ({@area areas 9|8c4|x} through {@area 20|8f0}). An ulitharid called Extremiton leads the colony. Once the colony is secure and its enemies are eradicated, Extremiton will undergo a transformation ritual to become an elder brain."
— `/home/user/waterdeep/sources/adventure-wdmm.json:47870`

> "Given a chance to do so, the ulitharid is delighted and eager to show off its Alterdeep simulation, which it is using to learn more about Waterdeep and its multifaceted culture. Extremiton fails to mention that once it becomes an elder brain, it plans to use its newfound knowledge to enslave the entire city."
— `/home/user/waterdeep/sources/adventure-wdmm.json:48301`

> "When an ulitharid finds sharing leadership with an elder brain to be insufferable, it breaks off from the colony, taking a group of mind flayers with it, and forms a new colony. After the death of the ulitharid's body, mind flayers place its brain in a brine pool, where it grows into an elder brain over a few days."
— `/home/user/waterdeep/sources/adventure-wdmm.json:64346`

### 3i. Ilsensine in the published Waterdeep adventure (mind flayer, not the god)

> "{@creature Nihiloor|WDH}, {@creature mind flayer}"
— `/home/user/waterdeep/sources/adventure-wdh.json:15073`

> "The tentacled creature is {@creature Nihiloor|WDH} (see {@adventure appendix B|WDH|12}), a {@creature mind flayer} that is caressing an {@creature intellect devourer}. Upon seeing the adventurers, {@creature Nihiloor|WDH} rises from the stone chair, sets its pet down, and glides across the room, intending to leave through the double door in the west wall. The mind flayer expects {@creature Grum'shar|wdh} and the intellect devourer to cover its escape."
— `/home/user/waterdeep/sources/adventure-wdh.json:2814`

`{@creature ...}` tags are left as written.

### 3j. Ilsensine: not found and conflicts

- Not found: Waterdeep cult, shrine or temple. Campaign tie to Nihiloor (the brief expected one; none exists). Great Brain or elder brain in any campaign file. Ilsensine in either adventure JSON. 5etools entry. 5e statistics. Holy days.
- Conflict with the campaign on Laduguer. `arc-j-vault-of-dragons.md:154` shows "Dumathoin, Ilsensine, and Laduguer, god of the duergar, with hands clasped in a circle of friendship". The wiki says "Besides hating Duerra, Ilsensine had also long sought vengeance against her superior Laduguer for some ancient slight." (`ilsensine/wiki.txt:210`, citing Demihuman Deities p.71). The campaign line is the Vault of Dragons structure document, so it is the authority for the Vault. The wiki is the only source for the Laduguer feud.
- Dumathoin: the wiki says the relationship is "obscure, non-hostile" (`ilsensine/wiki.txt:201`). The campaign line describes a visit and a bath in psionic light (`arc-j-vault-of-dragons.md:154`). The wiki does not contradict a visit.
- Rank across editions: "Greater deity" in 2e and 3e (`ilsensine/wiki.txt:66`, `:82`) and "Deity" in 5e (`:37`). Different editions, not a clash.

---

## 4. Baba Yaga

Wiki page: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt`. This is a character (Person) infobox, not the Deity template.

### Answers (Baba Yaga)

**(1)** None. The wiki's places are Rashemen, the Feywild swamp Murkendraw, and Mag Tureah. None is a Waterdeep cult, shrine or temple.
**(2)** None. No campaign file names her. The campaign and adventure bundle files are empty, and the one "hag" line in the campaign is not a Baba Yaga hit (section 4e).
**(3)** None.

### 4a. Identity (wiki infobox)

> "| titles         = Mother of All Witches<ref name="DMG5eR-p354">{{Cite book/Dungeon Master's Guide 5th edition (revised)|354}}</ref><br />Mother of Witches<ref name="MM5eR-p21"/><br />Bone Mother<ref name="dung196-p3">{{Cite dungeon/196/Court of Stars: Baba Yaga|3}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:14`

> "| nicknames      = Little Grandmother<ref name="dung196-p1">{{Cite dungeon/196/Court of Stars: Baba Yaga|1}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:16`

> "| race           = Arch-hag<ref name="DMG5eR-pp354,358">{{Cite book/Dungeon Master's Guide 5th edition (revised)|354,358}}</ref><ref name="MM5eR-p21"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:22`

> "| children       = Skabatha Nightshade, Bavlorna Blightstraw, and Endelyn Moongrave<br>'''{{Small|adoptive}}''' Natasha (or Tasha)"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:42`

> "| alignment1e    = Neutral evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:49`

> "| alignment2e    = Neutral evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:52`

> "| alignment4e    = Evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:63`

> "| alignment5e    = "
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:66`

Stat note. No 5e statistics. The 5e alignment, challenge and class fields are empty (`baba-yaga/wiki.txt:66` to `:68`). Her 5e race is arch-hag (`:22`).

> "'''Baba Yaga''' ({{Pronounce|ba|ba|_|YA|guh|refs=<ref name="D93-APG-p25">{{Cite dragon/93/Ay pronunseeAYshun gyd|25}}</ref>}}) was an extraordinarily powerful mage,<ref name="dmg1e-p156">{{Cite book/Dungeon Masters Guide 1st edition|156}}</ref> archfey,<ref name="dung196-p3" /><ref name="MotP4e-p36">{{Cite book/Manual of the Planes 4th edition|36}}</ref> and arch-hag.<ref name="DMG5eR-pp354,358" /><ref name="MM5eR-p21">{{Cite book/Monster Manual 5th edition (revised)|21}}</ref> Some described her as the most powerful female mage ever known, a sorceress with a reputation for passing throughout the planes."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:71` (the rest of the paragraph covers the hut on other planes and on Faerûn, cited to DMG 1e, Volo's and Book of Artifacts)

### 4b. Personality, bargains (warlock question)

> "{{Quote|Did you come of your own free will, or at another's bidding?|Baba Yaga, a question she typically asked visitors to her home.<ref name="dung196-p2" />}}"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:73`

> "Heh! People who know too much grow old before their time. Ask me your questions, but be certain that every secret has its cost."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:80`

> "She was known to have a fickle nature, being dangerously unpredictable, equally as likely to eat her worshipers as she was to aid them.<ref name="dung196-p3" /> Politeness would not guarantee her favor, nor would rudeness ensure incurring her wrath.<ref name="dung196-p2" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:83`

> "She was willing to offer people some of her secrets in return for another. The bargains she offered people were also far more dangerously worded than those of any fey.<ref name="MotP4e-p45" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:85`

> "Many sages and adventurers were known to have sought her out for her vast knowledge of magic.<ref name="dung196-p3" /> Archfey respected her powers, but were very cautious. Her relationship with deities was similarly fickle,<ref name="dung196-p2" /> though she tended to associate with those of an evil alignment, as well as those who were tricksters or mischief makers. She was also known to associate with devils.<ref name="dung196-p3" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:105`

> "The powerful witch knew much about the deity Psilofyr (a deity worshiped by myconids of Toril<ref name="DDuGttU">{{Cite book/Drizzt Do'Urden's Guide to the Underdark|54}}</ref><ref name="OotA5e-p92">{{Cite book/Out of the Abyss|92}}</ref>), but did not share her knowledge with others.<ref name="drag420-tck">{{Cite dragon/420/Court of Stars: The Carrion King}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:103`

### 4c. Realm, family, history

> "When not traveling around, she and her hut resided within the Feywild, in a swamp known as Murkendraw. Many types of hags were also known to inhabit this swamp.<ref name="MotP4e-p45">{{Cite book/Manual of the Planes 4th edition|45}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:95`

> "Baba Yaga knew of many realms and had probably even visited them, including realms that were adverse to magic like Earth, in her dancing hut, which traveled all the worlds and planes."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:97` (the rest of the paragraph covers the Hall of Gateways and the World Gate)

> "Baba Yaga had three hag daughters named Skabatha, Bavlorna, and Endelyn.<ref name="WBW5e-p215" /> She also helped to raise two humans, Kostchtchie and Tasha. The former went on to become very well known on Toril,<ref name="tGHotR-55">{{Cite book/The Grand History of the Realms|55}}</ref><ref name="DiA-104">{{Cite book/Baldur's Gate: Descent into Avernus|104}}</ref> whilst the latter was mainly heard of on the world of Oerth and became a powerful archfey.<ref name="WBW5e-p215" /><ref name="drag336-di">{{Cite dragon/336/Spellcraft: The Demonomicon of Iggwilv}}</ref> Kostchtchie became a "distinctly Faerûnian demon lord"<ref name="PGtF-p189">{{Cite book/Player's Guide to Faerûn|189}}</ref> and had conflicts with Gwynharwyf.<ref name="drag345-di">{{Cite dragon/345/Demonomicon of Iggwilv: Kostchtchie: Prince of Wrath}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:101`

> "Baba Yaga once prophesied that the ruler of Mag Tureah, a region of the Feydark with multiple portals to Toril,<ref name="frcg-p68">{{Cite book/Forgotten Realms Campaign Guide|68}}</ref> would be slain by his own son.<ref name="drag420-tf">{{Cite dragon/420/Court of Stars: Thrumbolg, First Lord of Mag Tureah}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:111`

> "In the 14{{th}} century DR, Volo and Elminster stated that, according to reports, Baba Yaga's hut appeared near Rashemen, northeast Faerûn.<ref name="VGtATM-p95" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:120`

Origin and rise. No origin story. The history section is the prophecy (line 111) and the Rashemen report (line 120).

### 4d. Worship and followers (wiki)

> "Some among the night hags, green hags, and annis hags were known to worship Baba Yaga.<ref name="drag345-eah">{{Cite dragon/345/The Ecology of the Annis Hag}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:108`

> "Many noted that Baba Yaga was somehow related to the night hags, green hags, and annis hags.<ref name="dm83">{{Cite dragon/83/The Dancing Hut}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:116`

> "One legend stated that she had been outwitted by heroes on occasion, who shoved her into an oven or trapped her in a lake of fire. The legend went on to state that despite seemingly dying, she would always appear again no worse for wear. Because of this some believed that she was impervious to fire.<ref name="dung196-p3" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:114`

> "One folk tale claimed that Baba Yaga was so powerful that the very times of dawn, noon, and night were all subservient to her whims. Another rumor claimed that she had no legs and that her magical mortar and pestle were her only means of moving around.<ref name="dung196-p3" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/baba-yaga/wiki.txt:118`

### 4e. Campaign and published adventure

- Campaign: none. The campaign-hits bundle file is empty. Grep for `baba yaga|grandmother|bone mother|mother of all witches` on `campaign/` returned no Baba Yaga line. Two unrelated "hag" lines are noted so they can be ruled out:

> "- Offers to add a *Glyph of Warding* to the cellar access for 300 gp; says the previous tenant made enemies she considers unresolved. Means the hag. Will not elaborate on the hag."
— `/home/user/waterdeep/campaign/guides/trollskull-manor/08-notable-patrons.md:99`

> "**Relationships.** Broxley is a representative of the Fellowship of Innkeepers, a father of nine, and a neighbor who remembers the tavern's worst days (the hag incident, the hauntings) and wants to believe its best are ahead."
— `/home/user/waterdeep/campaign/setting/notable-figures/trollskull-community/08-broxley-fairkettle.md:26`

- Adventure: none. The adventure-hits bundle file is empty, and the name search of both JSON files returned no Baba Yaga line. The only "grandmother" hit is Barnibus Blastwind's (`sources/adventure-wdh.json:31775`, quoted in section 0c).

### 4f. Baba Yaga: not found and conflicts

- Not found: Waterdeep (any kind). Clergy, holy days, temples, omens, messengers. Pact terms for a warlock. 5e statistics. Campaign and adventure mentions.
- Warlock mapping input: the wiki names her "archfey" (`baba-yaga/wiki.txt:71`) and gives the category "Archfey" (`:139`). No line gives a pact term.
- Conflict between editions: alignment "Neutral evil" in 1e and 2e (`:49`, `:52`) against "Evil" in 4e (`:63`). Different editions.
- Classification: the wiki calls her both "archfey" and "arch-hag" (`:71`, `:22`). It gives both.

---

## 5. Tharizdun

Wiki page: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt`. 5etools: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md`.

### Answers (Tharizdun)

**(1)** None. No Waterdeep cult, shrine or temple in any source. The wiki's cults are in Chessenta, Akanûl and the Dessarin Valley (section 5d).
**(2)** None. No campaign file or adventure line names Tharizdun. Both bundle hit files are empty.
**(3)** None. Grep for `waterdeep|waterdhav` on this file returned no line.

### 5a. 5etools (the only deities.json entries for this batch)

The three settings in this file are kept separate. The DMG and PHB entries are Dawn War and Greyhawk. EGW is Exandria. XDMG is Greyhawk.

> "## Tharizdun | source DMG p.10 | pantheon Dawn War"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:1`

> "- title: God of madness"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:2`

> "- alignment: ['C', 'E']"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:3`

> "- domains: ['Trickery']"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:4`

> "- symbol: Jagged counter-clockwise spiral"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:5`

> "## Tharizdun | source EGW p.28 | pantheon Exandria"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:9`

> "- title: the Chained Oblivion"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:10`

> "- domains: ['Death', 'Grave', 'Trickery']"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:12`

> "- symbol: Crooked, seven-pointed star made of chains"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:13`

> "It is darkness unending, less like a god and more like another world. Life and death do not exist within Tharizdun, only utter destruction and madness."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:16` (the rest of the paragraph covers the Abyss, the Prime Deities and Ioun, EGW p.28)

> "Commandments of Tharizdun: Offer and siphon power to Tharizdun until his liberation comes."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:21`

> "## Tharizdun | source PHB p.295 | pantheon Greyhawk"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:25`

> "- title: God of eternal darkness"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:26`

> "- domains: ['Trickery']"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:28`

> "- symbol: Dark spiral or inverted ziggurat"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:29`

> "## Tharizdun | source XDMG p.148 | pantheon Greyhawk"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:33`

> "- title: the Eater of Worlds"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:34`

> "- symbol: Spiral rune"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:35`

> "- worshipers: Nihilistic cultists"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:36`

> "- plane: Imprisoned in a demiplane"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/5etools.md:37`

### 5b. Identity (wiki infobox)

> "| title               = The Chained God<ref name="DMG-163">{{Cite book/Dungeon Master's Guide 4th edition|163}}</ref><ref name="MToF-p237">{{Cite book/Mordenkainen's Tome of Foes|237}}</ref><ref name="MPMotM-p226">{{Cite book/Mordenkainen Presents: Monsters of the Multiverse|226}}</ref><ref name="PHB5eR-p162">{{Cite book/Player's Handbook 5th edition (revised)|162}}</ref><ref name="DMG5eR-pp356,362">{{Cite book/Dungeon Master's Guide 5th edition (revised)|356,362}}</ref><br/>The Elder Elemental Eye<ref name="DMG-163"/><ref name="MToF-p237" /><br/>The Eater of Worlds<ref name="DMG5eR-pp148-149">{{Cite book/Dungeon Master's Guide 5th edition (revised)|148-149}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:11`

> "| power5eR            = Lesser deity<br>Elder evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:24`

> "| homeplane5eR        = Imprisoned in a demiplane"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:27`

> "| worshipers5eR       = Nihilistic cultists"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:33`

> "| power5e             = Deity"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:39`

> "| alignment5e         = Chaotic evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:40`

> "| symbol5e            = Dark spiral or inverted ziggurat"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:41`

> "| portfolio5e         = Eternal darkness"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:46`

> "| domains5e           = Trickery"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:47`

> "| channel divinity5e  = ''Invoke duplicity''<br />''Cloak of shadows''"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:49`

> "| refs5e              = <ref name="PHB5e-p63,295">{{Cite book/Player's Handbook 5th edition|63,295}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:52`

> "| alignment4e         = Chaotic evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:54`

> "| dominion4e          = Abyss"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:56`

> "| power3e             = Intermediate deity"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:68`

> "| alignment3e         = Neutral evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:69`

> "| portfolio3e         = Darkness, elemental power, entropy, insanity, ruin, vengeance"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:75`

> "| power2e             = Intermediate deity"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:83`

> "| alignment2e         = Neutral evil"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:84`

> "| portfolio2e         = Dark, decay, insanity"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:90`

> "'''Tharizdun''' ({{Pronounce|thar|IZ|dun|refs=<ref name="D93-APG-p30">{{Cite dragon/93/Ay pronunseeAYshun gyd|30}}</ref>}}), also known as '''The Chained God''' and '''The Elder Elemental Eye''',<ref name="DMG-163"/> was a long-forgotten interloper god originating from Oerth who sought to destroy all that is. During the Dawn War, he created the Abyss, an act for which he was imprisoned by the gods. His followers hoped to set him free.<ref name="Demonomicon-8" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:118`

### 5c. Tenets, form, worship (wiki)

> "Light must be snuffed, perfection decayed, order dissolved, and minds fragmented."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:121` (the wiki attributes it at line 122 to "An inscription in one of Tharizdun's black pyramids.", citing Dragon 294)

> "Tharizdun appeared as an amorphous, roiling pitch-blackness.<ref name="D294-31" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:125`

> "Tharizdun was not simply neutral evil; his evil transcended law and chaos, reflecting a primal nature so ancient it went back to the early days of the Great Wheel cosmology.<ref name="D359">{{Cite dragon/359/1d20 Villains: D&D's Most Wanted; Preferably Dead|59}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:128`

> "Dread Tharizdun, power of the Elder Elemental Eye and master of all destructive forces, I am the Champion of Elemental Evil and am ready to carry out your wishes."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:132` (the wiki attributes it to "Rites of the Cult of Elemental Evil", citing Monster Manual 5e p.84)

> "Tharizdun's exact dogma was a mystery, as the ages he was imprisoned in the Abyss along with his own growing insanity left him unable to communicate in a meaningful manner. Even when he appeared to his followers, he only spoke to them in the form of a shrieking babble that was impossible for mortals to comprehend. While his true commands were unknown, his cults taught that his power must be channeled to help him break free of his bonds, that his lost relics and shrines were to be found, and that they should pursue the end of the world in anticipation of their mad god's return.<ref name="DMG-163" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:135`

> "Tharizdun was one of the evil deities within the Oerthly, Dawn War,<ref>{{Cite book/Dungeon Master's Guide 5th edition|10-11}}</ref><ref name="DMG4e-p198">{{Cite book/Dungeon Master's Guide 4th edition|198}}</ref> and Exandrian pantheons.<ref name="EGW-p24">{{Cite book/Explorer's Guide to Wildemount|24}}</ref> He was worshiped only by mad people.<ref name="DMG4e-p198"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:138` (piped links keep their visible text: "Oerthly", "Dawn War", "Exandrian pantheons")

### 5d. History, cults, the Abyss (wiki)

> "This seed eventually grew into the Abyss, and though the act gained him great power, the other gods of the multiverse temporarily put aside their differences in order to imprison him.<ref name="MM4e-p52/><ref name="TEEE-p4">{{Cite book/The Elder Elemental Eye|4}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:149`

> "In 1340 DR, a cult of Tharizdun formed in western Chessenta. It hired bandits, consorted with demons, and caused much havoc before an alliance of forces destroyed it. Some credit the fact that Tharizdun did not gain a permanent foothold on Toril to the personal intervention of the goddess Mystra.<ref name="SotG-112">{{Cite book/Sword of the Gods|112}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:152`

> "A new cult of Tharizdun was formed by the plague demon Murmur in 1479 DR after a burnt portion of its corpse was discovered by the Firestorm Cabal in Akanûl. It possessed Leheren, one of the members of the Cabal, and created a secret order within the order devoted to freeing Tharizdun and releasing him on the continent of Faerûn.<ref name="SotG-180">{{Cite book/Sword of the Gods|180}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:154`

> "In the late 15{{th}} century DR, several cults dedicated to the Elder Elemental Eye arose in the Dessarin Valley trying to summon the Princes of Elemental Evil.<ref name="PotA5e-p4,248">{{Cite book/Princes of the Apocalypse|4,248}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:158`

Ancient history (lines 143 to 147) is not quoted. It is cited to 3e and 4e books.

### 5e. Warlock and cleric relevance

> "Category:Elder evils"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:200`

> "Category:Great Old One patrons"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tharizdun/wiki.txt:201`

Those two category lines are the wiki's only warlock text. The 5e channel divinity fields (line 49) are cleric features.

### 5f. Relations and Waterdeep

- Relations (wiki): Mystra is credited with keeping Tharizdun off Toril (`tharizdun/wiki.txt:152`). The ancient story names Pelor and Ioun (`:143`, not quoted).
- Waterdeep: none in the wiki, the adventures or the campaign.

### 5g. Tharizdun: not found and conflicts

- Not found: Waterdeep (any kind). Holy days, omens, messengers (holy-day fields empty). Campaign and adventure mentions. Warlock pact terms.
- Symbol across sources. The wiki's 5e symbol is "Dark spiral or inverted ziggurat" (`tharizdun/wiki.txt:41`), matching the PHB p.295 entry (`5etools.md:29`). The DMG p.10 entry gives "Jagged counter-clockwise spiral" (`5etools.md:5`), which matches no wiki field. The EGW entry gives "Crooked, seven-pointed star made of chains" (`5etools.md:13`). Each entry is tagged with its own setting.
- Title across sources. The XDMG entry gives "the Eater of Worlds" (`5etools.md:34`), and the wiki gives the same title under DMG5eR pp.148–149 (`tharizdun/wiki.txt:11`). These agree.
- Alignment across sources. Every 5etools entry gives ['C', 'E'] (`5etools.md:3`, `:11`, `:27`), and the wiki's 5e alignment is "Chaotic evil" (`tharizdun/wiki.txt:40`). These agree.

---

## 6. Conflicts across the batch (summary)

1. **Ilsensine and Laduguer.** `/home/user/waterdeep/campaign/structure/arc-j-vault-of-dragons.md:154` ("Dumathoin, Ilsensine, and Laduguer, god of the duergar, with hands clasped in a circle of friendship") against `ilsensine/wiki.txt:210` ("Ilsensine had also long sought vengeance against her superior Laduguer"). The campaign file is the Vault of Dragons authority. The wiki is the only source for the feud.
2. **Titania and the Queen.** The Queen's wiki origin makes her Titania's sister (`queen-of-air-and-darkness/wiki.txt:148`). The Titania page says "rumored to be the dark sister" (`titania/wiki.txt:170`). These agree on the sisterhood and differ only in certainty.
3. **Baba Yaga across editions.** "Neutral evil" (1e, 2e) against "Evil" (4e) (`baba-yaga/wiki.txt:49`, `:52`, `:63`).
4. **Nihiloor.** The brief expected a Nihiloor link to Ilsensine. No campaign line supplies one (section 3g).

## 7. Cross-references (file:line for every batch name in the sources)

- `/home/user/waterdeep/campaign/structure/arc-j-vault-of-dragons.md:154` (Ilsensine, section 3f)
- `/home/user/waterdeep/sources/adventure-wdh.json:31381` (Fey Day heading, section 1f)
- `/home/user/waterdeep/sources/adventure-wdh.json:31385` (Titania, section 1f)
- `/home/user/waterdeep/sources/adventure-wdh.json:31775` (grandmother, not Baba Yaga, section 0c)
- `/home/user/waterdeep/sources/adventure-wdh.json:15073` and `:2814` (Nihiloor as a mind flayer, section 3i)
- `/home/user/waterdeep/sources/adventure-wdmm.json:47870`, `:48301`, `:64346` (elder brain lines, section 3h)
- `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:61`, `:102`, `:115`, `:157` (Fey Day, section 1f)
- `/home/user/waterdeep/campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:6`, `:16`, `:26`, `:30` (section 3g)
- `/home/user/waterdeep/campaign/setting/villains/xanathar.md:50` (section 3g)
- `/home/user/waterdeep/campaign/guides/trollskull-manor/08-notable-patrons.md:99` (section 4e)
- `/home/user/waterdeep/campaign/setting/notable-figures/trollskull-community/08-broxley-fairkettle.md:26` (section 4e)
- `/home/user/waterdeep/campaign/setting/deities/asmodeus.md:62` and `:123` (warlock lines for Asmodeus, not these patrons):

> "> - **A warlock or oath PC:** The files give no rules for a Fiend patron or an oath tied to him. [research] For flavor, the Fugue Plane pitch (comfort from a devil, or a rank in the infernal host) is the hook a devout character would have heard, and the city treats an admitted follower with the same distrust as any other."
— `/home/user/waterdeep/campaign/setting/deities/asmodeus.md:62`

> "> - **Research:** Rules for a warlock or oath PC tied to Asmodeus (Using box). No campaign file or 5etools entry supplies them."
— `/home/user/waterdeep/campaign/setting/deities/asmodeus.md:123`

## 8. Not found (terms and files tried)

- **Titania.** Waterdeep (wiki, adventures, campaign): none. Clergy, holy days, omens: none. 5e statistics: none. Campaign mentions: none. Adventure mentions: Fey Day only. Terms: Titania, Tiandra, Faerie Queen, Summer Queen, Queen of Light, Seelie, Oberon.
- **Queen of Air and Darkness.** Waterdeep: none. Campaign: none. Adventures: none. Terms: Queen of Air, Unseelie, Black Diamond, Night Diamond. 5etools: none.
- **Baba Yaga.** Waterdeep: none. Campaign: none. Adventures: none. Terms: Baba Yaga, Grandmother, Bone Mother, Mother of All Witches, Little Grandmother, Mother of Witches. 5etools: none. 5e statistics: none.
- **Ilsensine.** Waterdeep: none. Campaign: one line (`arc-j-vault-of-dragons.md:154`). Nihiloor tie: none. Great Brain or elder brain in campaign: none. Either adventure JSON: no Ilsensine, Great Brain or god-brain line. Terms: Ilsensine, Ilsen, Great Brain, elder brain, God-Brain, Tentacled Lord, Maanzecorian. 5etools: none. 5e statistics: none.
- **Tharizdun.** Waterdeep: none. Campaign: none. Adventures: none. Terms: Tharizdun, Chained God, Elder Elemental Eye, Elder Elemental, Eater of Worlds. Bundle campaign-hits and adventure-hits files: empty.
- **The force-grey folder named in the brief.** `campaign/setting/notable-figures/force-grey/` does not exist. The Nihiloor page is `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md`.

## 9. Not readable

None. Every wiki, 5etools and bundle file in this batch was opened. The `.docx` files in `sources/Other remix files/` were not searched (not in scope for this batch).
