# Batch C research: Tymora, Beshaba, Selûne, Shar, Lliira (Deities, Pass 2)

## Method and conventions

- **Bundle** = `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/`. Cited as `tymora/5etools.md:9` and so on.
- **Repo** = `/home/user/waterdeep/`. Cited as `campaign/...` and `sources/...`.
- **Wiki line numbers** (`wiki.txt`) are the 1-based numbers from `Grep -n`. The Read tool shows the same lines one lower, because its first line is 0. Every wiki line number here came from `Grep -n`.
- **Wiki markup.** I removed the `[[ ]]` link brackets, as allowed. All other wiki markup is kept as written, including `{{ }}` templates and `<ref>` tags. Each wiki quote is tagged with the book its own line cites.
- **JSON.** `—` in the adventure JSON is shown as "—".
- **Quote blocks.** A block quote with several lines is one contiguous passage copied from the file, bullet by bullet.
- **Bundle gaps.** Grep of the full sources found lines that the bundles omit:
  - `adventure-hits.txt` for Tymora omits `sources/adventure-wdh.json:30884` and `:30984`.
  - Selûne's omits `sources/adventure-wdh.json:30969`.
  - Beshaba's omits `sources/adventure-wdh.json:31522`.
  - Shar's omits `sources/adventure-wdmm.json:50785`, `:50786` and `:50788`. These are tenet list items that do not name Shar. I quote them under Shar Field 2.
- **Empty bundles.** `campaign-hits.txt` is empty for Beshaba and Shar. Targeted Grep of `campaign/` agrees: no line names Shar or Beshaba.
- **Scope.** I did not read the Alexandrian PDFs, `SOURCE_GUIDE.md` or the `Other remix files` folder, as the caller asked.
- **Answers.** Q1 to Q3 sit inside each power's block, after Field 7.

---

## 1. Tymora

### Field 1: Identity

**FRHoF, current canon (5etools)**

> "## Tymora | source FRHoF p.126 | pantheon Faerûnian"
> "- altNames: ['Lady Luck', 'Our Smiling Lady']"
> "- title: God of good fortune"
> "- worshipers: Gamblers, Harpers, merchants, Rogues"
> "- plane: Arborea (Arvandor)"
> — `tymora/5etools.md:1-5`

**SCAG, 2014 (5etools; the only source of alignment, domains and symbol in the bundle)**

> "## Tymora | source SCAG p.21 | pantheon Faerûnian"
> "- altNames: ['Lady Luck', 'Our Smiling Lady']"
> "- title: Goddess of good fortune"
> "- alignment: ['C', 'G']"
> "- domains: ['Trickery']"
> "- symbol: Face-up coin"
> — `tymora/5etools.md:22-27`

**Wiki (lead paragraph)**

> "was the goddess of good luck in the Faerûnian pantheon and the second incarnation of the goddess of luck after her predecessor Tyche was split into her and Beshaba, goddess of bad luck.<ref name="F&A-p44"/><ref name="SCAG-p40"/>"
> — `tymora/wiki.txt:136` (refs in the line: Faiths & Avatars p.44; SCAG p.40, 2014)

> "Commonly known as '''Lady Luck''', Tymora shone upon those who took risks and blessed those who dealt harshly with the followers of Beshaba.<ref name="MiBG.CG-p49">{{Cite book/Murder in Baldur's Gate/Campaign Guide|49}}</ref>"
> — `tymora/wiki.txt:136` (Murder in Baldur's Gate, Campaign Guide p.49)

### Field 2: Edict or core tenet

> "The battle cry of Tymora is "Fortune favors the bold.""
> — `tymora/5etools.md:9` (FRHoF)

> "Priests of Tymora were taught to think of themselves as their own masters and to be brave enough to accept both good and bad fortune, as a trust in their goddess and in themselves."
> — `tymora/wiki.txt:200` (paragraph refs include Faiths & Avatars pp.166-167)

> "Offerings made to the goddess of luck were often accompanied by the prayer, "A copper to the Lady returns tenfold in gold," which a priest would answer with "Dare much, and the Lady keep you."<ref name="MM">{{Cite book/Midnight's Mask/MMP|64|4}}</ref>"
> — `tymora/wiki.txt:225`

### Field 3: Portfolio and Areas of Concern

> "Tymora is a bright-faced god of fortune, the patron deity of game players and gamblers."
> — `tymora/5etools.md:7` (FRHoF)

> "Tymora is the bright-faced goddess of fortune, the one to whom gamblers and game-players pray in Faerûn."
> — `tymora/5etools.md:29` (SCAG, 2014)

> "In the 14{{th}} century DR, Tymora held the portfolios of good fortune, skill, victory, and adventurers.<ref name="FRCS-235"/>"
> — `tymora/wiki.txt:136` (wiki cites Forgotten Realms Campaign Setting 3e p.235)

Areas of Concern: no 5etools entry and no wiki line gives this field. Not sourced.

### Field 4: Worship

> "Priests of Tymora and temples devoted to Lady Luck are scarce, since her faith doesn't stress a need for intermediaries: "Let the lucky man and the Smiling Lady suss it out," as the old saying goes. Shrines to Tymora at gambling parlors aren't unusual, however, and such establishments might attract a priest and effectively become temples."
> — `tymora/5etools.md:11` (FRHoF)

> "Shrines and temples of Tymora were as widespread as the needs of adventurers to be healed, which made the temples wealthy.<ref name="FRCS3e-p226">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|226}}</ref><ref name="FRA-p108">{{Cite book/Forgotten Realms Adventures|108}}</ref>"
> — `tymora/wiki.txt:204` (refs: Forgotten Realms Campaign Setting 3e p.226; Forgotten Realms Adventures p.108)

> "| holy days5e         = [[Midsummer]]<ref name="FRCS-235"/><ref name="F&A-167"/><br /> [[Starfall (festival)|Starfall]]<ref name="FRCS-235"/><ref name="F&A-167"/>"
> — `tymora/wiki.txt:65` (5e row; link brackets removed)

The adventure's entry "Nightal 20: Simril" (`sources/adventure-wdh.json:31583`) mentions Tymora in one sentence, quoted in Field 6. It does not say the holiday is held in Waterdeep, and it does not name it Starfall or Midsummer.

> "She might send a faerie dragon as an emissary."
> — `tymora/5etools.md:7` (FRHoF; messenger)

> "| misc manifestations = [[Pegasus|Silver pegasus]]<br /> Silver bird<br /> Silver glow"
> — `tymora/wiki.txt:131` (infobox; manifestation refs Faiths & Avatars p.167 and others)

### Field 5: Relations and origin

> "Tymora is Beshaba's sister. Long ago, the Netherese revered Tyche, the god of luck, whose influence extended over both good luck and bad. Tyche perished, but Beshaba and Tymora manifested soon after, each commanding half of Tyche's portfolio."
> — `tymora/5etools.md:8` (FRHoF)

> "During times known as the Dawn Cataclysm, the former deity of luck, Tyche, controlled both good and bad luck."
> — `tymora/wiki.txt:230` (Creation section; paragraph refs include Faiths & Avatars p.44 and SCAG p.40, 2014)

> "Sages have claimed that Tymora had fostered many brief trysts with good-aligned male deities, always ending them amicably when her attentions were drawn elsewhere."
> — `tymora/wiki.txt:184` (paragraph refs include Faiths & Avatars p.166)

> "Tymora had a very close friendship with Selûne, who was not only her oldest friend in this life, but also in the one before, when Lady Luck was still goddess Tyche."
> — `tymora/wiki.txt:186`

> "Beshaba was her twin sister's fiercest foe since the day they were "born" from Tyche's husk."
> — `tymora/wiki.txt:190`

> "So upset was Tymora at this turn of events, that she abandoned her realm in Brightwater, and was accepted by Selûne to live in the Gates of the Moon.<ref name="TGHotR-p159">{{Cite book/The Grand History of the Realms|159}}</ref>"
> — `tymora/wiki.txt:242` (Recent History, 1384 DR; The Grand History of the Realms p.159)

### Field 6: Campaign and published-adventure mentions (non-temple)

> "This alley in the Dock Ward suffers from a magical curse that causes three daggers to appear out of thin air and attack passersby."
> — `sources/adventure-wdh.json:31339`

> "So take my advice and don't test Tymora's favor."
> — `sources/adventure-wdh.json:31339` (second sentence of the same line)

> "Cloudy nights often draw larger crowds than clear ones, since glimpsing your star through the haze is thought to be a blessing from Tymora."
> — `sources/adventure-wdh.json:31587` (festival "Nightal 20: Simril", named at line 31583)

> "{@creature Meloon Wardragon|wdh|Meloon} is a handsome, formidable warrior in his prime, who serves the goddess Tymora and loves a good fight. His friends-among them {@creature Renaer Neverember|wdh} and {@creature Vajra Safahr|WDH}-describe him as honest, optimistic, and extraordinarily lucky. Until recently, he was a member of Force Grey and reported directly to the Blackstaff. In recent months, Meloon has spent much of his time at the Yawning Portal."
> — `sources/adventure-wdh.json:32255`

> "Three months ago, out of boredom, Meloon accompanied a fledgling band of adventurers on an expedition to Undermountain. There, his luck ran out. While resting in the dungeon, the adventuring party was attacked by monsters unleashed by {@creature Xanathar|WDH}-including a number of intellect devourers. One of the creatures succeeded in magically devouring and replacing Meloon's brain, turning the champion of Tymora into a puppet. After finishing off his unsuspecting companions, Meloon returned to Waterdeep as a Xanathar Guild spy."
> — `sources/adventure-wdh.json:32256`

> "The real Meloon wants to fight alongside people he admires, honor Tymora through brave action, and protect Waterdeep."
> — `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:16`

### Field 7: Conflicts and not found

- **Conflict (ward placement).** The Tower of Luck is placed in two wards. Every placement found is under Q1.
- **Conflict (pantheon label).** "## Tymora | source PHB p.294 | pantheon Forgotten Realms" (`tymora/5etools.md:14`). FRHoF and SCAG read "Faerûnian" (`tymora/5etools.md:1`, `:22`).
- **Conflict (worshipers, by edition).** FRHoF gives "- worshipers: Gamblers, Harpers, merchants, Rogues" (`tymora/5etools.md:4`). The wiki's 5e field gives "| worshipers5e        = Gamblers, game-players, adventurers" (`tymora/wiki.txt:63`).
- **Conflict (realm, by edition).** 5etools FRHoF gives "- plane: Arborea (Arvandor)" (`tymora/5etools.md:5`). The wiki says "Tymora resided in the Gates of the Moon after the events of the Spellplague, allied to, but independent of, that realm's twin mistresses." (`tymora/wiki.txt:179`).
- **Not found.** Areas of Concern. A Tymoran cleric or temple named in any campaign file. A Tymoran faction or quest in `campaign/`.

### Q1. Which temples or shrines do the adventure or campaign files place in Waterdeep, and in which ward?

**Major Temples table, `sources/adventure-wdh.json`** (caption at line 30910: `"caption": "Major Temples of Waterdeep",`)

> "Tymora",
> "Tower of Luck",
> "Castle Ward"
> — `sources/adventure-wdh.json:30983`, `:30984`, `:30985`

**Sea Ward section, published adventure** (the ward header is `"name": "Sea Ward",` at line 30873; the Tower of Luck entry sits inside that section)

> "If you're looking for some good fortune, you should surely visit the Tower of Luck, a temple complex dedicated to Tymora."
> — `sources/adventure-wdh.json:30882`

> "Two parks in the Sea Ward might also be worth your time."
> — `sources/adventure-wdh.json:30884`

> "The Shrines to Nature, just a block away from the Tower of Luck, are resplendent gardens dedicated to nature gods like Mielikki and Silvanus."
> — `sources/adventure-wdh.json:30884` (the same line continues: "The park is closed to all except residents of the Sea Ward.")

**Campaign files**

> "- Tymora's Tower of Luck is placed in the Castle Ward by the Dragon Heist temple table and in the Sea Ward by its Sea Ward text and by the campaign's own Waterdeep outline, so it is not a Castle Ward temple here."
> — `campaign/gazetteer/waterdeep/castle-ward.md:165` (the line names "the campaign's own Waterdeep outline" without identifying the file)

> "Tymora's Tower of Luck is listed here by one Waterdeep Dragon Heist table and placed in the Sea Ward elsewhere, and the wiki's Castle Ward list names neither it nor a Temple of Helm."
> — `campaign/gazetteer/waterdeep/castle-ward.md:31` (Religion bullet; it repeats the Dragon Heist table as a Castle Ward listing)

> "- **Sea Ward**: the Tower of Luck, Mirt's dinner house and Barnibus Blastwind's estate may belong there."
> — `campaign/gazetteer/waterdeep/castle-ward.md:240` (Cross-References section)

> "> - **Conflicts:** Tower of Luck. The Dragon Heist temple table lists it in the Castle Ward; the Dragon Heist Sea Ward text and `waterdeep-lore.md` place it in the Sea Ward. `waterdeep-lore.md` also puts the Selûne temple in the Sea Ward."
> — `campaign/gazetteer/waterdeep/castle-ward.md:271` (Draft Notes)

> "> - **Routed facts:** Temples of the Castle Ward (demoted landmark), including the Tower of Luck, Selûne and Helm notes and the missing hooks, moved into Culture under Life in the Ward."
> — `campaign/gazetteer/waterdeep/castle-ward.md:283` (Draft Notes; a routing note, not a placement)

> "- Major temples in Sea Ward: Tymora (Luck; popular with adventurers and criminals alike), Selûne (Moon; widely attended)"
> — `campaign/setting/waterdeep-lore.md:36`

Retired file (CLAUDE.md lists `ch2-city-of-splendors.md` as retired):

> "- Major temples in Sea Ward: Tyr (Justice; City Watch captain is a worshiper), Tymora (Luck; popular with adventurers and criminals alike), Selûne (Moon; widely attended)"
> — `campaign/structure/ch2-city-of-splendors.md:56`

Players' Guide, with no ward:

> "| Acolyte | Good | Temple life runs deep here. Tyr and Tymora both keep visible, active houses of worship. |"
> — `campaign/guides/players-guide/character-creation.md:44`

Retired file:

> "| Acolyte | Good | Temple ties — Tyr and Tymora are visible; Asmodeus has a hidden temple |"
> — `campaign/structure/ch1-beginning.md:104` (retired)

**Placement summary.**
- Sea Ward: `sources/adventure-wdh.json:30882` (the text, inside the Sea Ward section), `castle-ward.md:165` (the Castle Ward file's own text), `castle-ward.md:240`, `waterdeep-lore.md:36`, and `ch2-city-of-splendors.md:56` (retired).
- Castle Ward: `sources/adventure-wdh.json:30985` (the table), and `castle-ward.md:31`, where the Castle Ward file's Religion bullet lists it "here" by repeating the table.
- `castle-ward.md:271` records the conflict. `castle-ward.md:283` is a routing note.
- The brief's hub rule on this conflict reads: "Where the campaign or the wiki gives a different ward (Tymora's Tower of Luck, Helm's Hall), put both in Draft Notes; the campaign file wins." (`docs/plans/setting-compendium-pass2-brief.md:58`). This report does not choose between the wards.

**Other Tymora sites, not in Waterdeep**

> "In 1358 DR during the Time of Troubles, Tymora's avatar manifested in the Cormyrian city of Suzail and then traveled to the Lady's House, a temple devoted to her worship in Arabel.<ref>{{Cite book/Forgotten Realms Adventures|1}}</ref><ref name="poly139-p14">{{Cite polyhedron/139/City Stories: The Hall of Luck|14}}</ref><ref name="Shadowdale-p26-27">{{Cite book/Shadowdale/MMP (1989)|26-27}}</ref><ref name="VGtC-p56">{{Cite book/Volo's Guide to Cormyr|56}}</ref>"
> — `tymora/wiki.txt:239` (Arabel and Cormyr, not Waterdeep)

> "Despite her daring personality, Tymora did not neglect caution."
> — `tymora/wiki.txt:159` (the Zhentil Keep shrine named later in the same line is not in Waterdeep)

> "''Tymora's cup'' was a ceremonial offering to the goddess of luck, located in Lady Luck Tavern."
> — `tymora/wiki.txt:175` (the line gives no location for the tavern)

### Q2. Which campaign NPC, faction or quest uses Tymora?

- **NPC.** Meloon Wardragon. "The real Meloon wants to fight alongside people he admires, honor Tymora through brave action, and protect Waterdeep." (`campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:16`). Field 6 quotes the published adventure's account of him.
- **Faction.** None found.
- **Quest.** None found.

### Q3. Which wiki lines mention Waterdeep?

One line. The text is a citation, not a Waterdeep fact:

> "Lady Luck was very fond of her followers, secretly aiding them in times of extreme danger<ref name="tRoUCGtU-p2">{{Cite book/The Ruins of Undermountain/Campaign Guide to Undermountain|105}}</ref> or continuing to support them even after they stopped worshiping her, fondly remembering their exploits.<ref name="VGtW-229">{{Cite book/Volo's Guide to Waterdeep|229}}</ref> Nevertheless, creatures faithful to Tymora were looked upon with disfavor if they continually tried to rely directly on the goddess, as this was seen as a lack of trust in her luck.<ref name="F&A-p168">{{Cite book/Faiths & Avatars|168}}</ref>"
> — `tymora/wiki.txt:161` (the only Waterdeep mention is the Volo's Guide to Waterdeep p.229 citation)

---

## 2. Beshaba

### Field 1: Identity

**FRHoF (5etools)**

> "## Beshaba | source FRHoF p.103 | pantheon Faerûnian"
> "- altNames: ['Lady Doom', 'The Maiden of Misfortune']"
> "- title: God of misfortune"
> "- worshipers: Gamblers, Red Wizards, Rogues"
> "- plane: The Abyss"
> — `beshaba/5etools.md:1-5`

**SCAG, 2014 (5etools)**

> "## Beshaba | source SCAG p.21 | pantheon Faerûnian"
> "- altNames: ['The Maid of Misfortune', 'Lady Doom', 'Black Bess']"
> "- title: Goddess of misfortune"
> "- alignment: ['C', 'E']"
> "- domains: ['Trickery']"
> "- symbol: Black antlers"
> — `beshaba/5etools.md:21-26`

**Wiki (lead)**

> "was the chaotic evil intermediate deity of accidents, bad luck, misfortune, and random mischief,<ref name="F&P-91" /> and a member of Tempus' pantheon during the Spellplague.<ref name="FRCG-p80"/>"
> — `beshaba/wiki.txt:135` (refs: Faiths and Pantheons pp.91-92; Forgotten Realms Campaign Guide 4e p.80)

> "Lady Doom was the equally acknowledged counterpart of Tymora, Lady Luck, and demanded worship to keep her misfortunes at bay."
> — `beshaba/wiki.txt:135` (the next sentence in the line carries the SCAG 2014 pp.21, 26-27 citation)

### Field 2: Edict or core tenet

> "Mortals invoke Beshaba's name when beset by bad luck—anything as minor as stubbing a toe or as catastrophic as falling off a cliff."
> — `beshaba/5etools.md:9` (FRHoF)

> "Beshaba was revered more out of fear than out of religious faith. Her doctrine stated that bad luck befell everybody and the only way to avoid it was by worshiping her."
> — `beshaba/wiki.txt:160`

### Field 3: Portfolio and Areas of Concern

> "Beshaba is a god of misfortune, the counterpoint to her benevolent sister, Tymora, and as frequently acknowledged in daily life."
> — `beshaba/5etools.md:7` (FRHoF)

> "| portfolio5e         = Misfortune, bad luck"
> — `beshaba/wiki.txt:61` (5e field)

> "| portfolio3e         = Accidents <br /> Bad Luck <br /> Misfortune <br /> Random mischief"
> — `beshaba/wiki.txt:91` (3e field)

Areas of Concern: no 5etools entry and no wiki line gives this field. Not sourced.

### Field 4: Worship

> "Temples to Beshaba are virtually unknown. It's common, however, for rural folk to erect a post and mount antlers on it at the site of a roadside accident or murder. In cities, where antlers are hard to come by, the pious draw the black antlers of Beshaba with charcoal on a nearby wall, leaving the symbol on display until weather scours it away."
> — `beshaba/5etools.md:10` (FRHoF)

> "More formal shrines to Beshaba exist in places where folk frequently hope to ward off misfortune. These sites tend to be posts or stones painted red with blackened antlers attached to them, or a red, triangular wall-mounted plaque with attached antlers. Both types have a stone or bronze bowl where coins can be tossed or burnt offerings made. The Red Wizards of Thay commonly erect such shrines outside their ritual chambers to guard against unfortunate mistakes."
> — `beshaba/5etools.md:34` (SCAG, 2014)

> "Few dare to take Beshaba as a patron. The rare clerics of the Maid of Misfortune are those who have been deeply affected by great misfortunes and who seek to warn others of the essential unfairness of life - or to inflict that unfairness upon them."
> — `beshaba/5etools.md:35` (SCAG, 2014)

> "There were two festivals in the calendar of Beshaba, at Midsummer and Shieldmeet. Both were celebrated by revelry and indulgence in food and drink.<ref name="FA-42" /><ref name="F&P-91" />"
> — `beshaba/wiki.txt:160`

> "* Doommasters: The best known order of specialty priests, universally feared for the way they reveled in the infliction of misfortune on others.<ref name="FA-43-44">{{Cite book/Faiths & Avatars|43-44}}</ref>"
> — `beshaba/wiki.txt:167` (listed as an order; link brackets removed)

> "When Beshaba speaks directly to a mortal, her voice whispers from broken mirrors. Otherwise, she sends a {@creature Quasit|XMM} disguised as a black cat, or a great stag ({@creature Deer|XMM}, {@creature Elk|XMM}, or {@creature Giant Elk|XMM}) with black antlers dripping blood."
> — `beshaba/5etools.md:8` (FRHoF; messengers and omens; {@creature} tags kept as written)

### Field 5: Relations and origin

> "Beshaba came into being when the deity Tyche split during the Dawn Cataclysm, a separate disaster relating to the machinations of Lathander."
> — `beshaba/wiki.txt:173` (paragraph refs include Faiths & Avatars p.42)

> "Beshaba was the twin sister and sworn enemy of Tymora.<ref name="FA-42" /><ref name="F&P-91" />"
> — `beshaba/wiki.txt:150`

> "She was Tempus' lover.<ref name="FRCG-p80"/>"
> — `beshaba/wiki.txt:152`

> "She rejected advances from Talos, among other hopefuls.<ref name="FA-42" /><ref name="F&P-91" />"
> — `beshaba/wiki.txt:148`

### Field 6: Campaign and published-adventure mentions

> "Marpenoth 10: Reign of Misrule"
> — `sources/adventure-wdh.json:31522` (name line; not in the bundle)

> "Swift on the heels of Stoneshar comes the Reign of Misrule. This day honors Beshaba, goddess of misfortune. People of the city are expected to break trust, belie oaths, and disobey the normal order-as long as no laws are actually broken and no rift is made that can't be later bridged."
> — `sources/adventure-wdh.json:31526`

> "After the window, the calendar continues with Midsummer and Shieldmeet, Ahghairon's Day (Eleasis 1), Brightswords (Eleint 21), Stoneshar (Marpenoth 7), the Reign of Misrule (Marpenoth 10), Gods' Day (Marpenoth 15) and Liar's Night (Marpenoth 30). These matter only if play runs past Flamerule 11."
> — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:111` (names the festival; does not name Beshaba)

### Field 7: Conflicts and not found

- **Conflict (worshipers, by edition).** FRHoF gives "- worshipers: Gamblers, Red Wizards, Rogues" (`beshaba/5etools.md:4`). The wiki's 5e field gives "| worshipers5e        = [[Druid]]s, [[Red Wizards of Thay]]" (`beshaba/wiki.txt:63`).
- **Conflict (plane, by edition).** FRHoF gives "- plane: The Abyss" (`beshaba/5etools.md:5`). The wiki's 3e field gives "| homeplane3e         = [[Barrens of Doom and Despair]]" (`beshaba/wiki.txt:87`). The wiki's 2e field places her in the "13th layer of the Abyss" (`beshaba/wiki.txt:102`).
- **Not found.** No Beshaba temple or shrine in Waterdeep in any file read. No Beshaba NPC, faction or quest in `campaign/`. Areas of Concern.

### Q1. Temples or shrines in Waterdeep

None. The Major Temples table (`sources/adventure-wdh.json:30910` to `:31000`) has no Beshaba row. No campaign file places a temple or shrine. The only Waterdeep Beshaba entry is the festival in Field 6 (`sources/adventure-wdh.json:31526`).

### Q2. Campaign NPC, faction or quest

None. The only campaign line is the calendar entry, which names the festival and not Beshaba (`campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:111`).

### Q3. Wiki lines mentioning Waterdeep

None. Grep for "Waterdeep", "Waterdhav", "Waterdavi", "Sea Ward", "Castle Ward", "Dock Ward" and "North Ward" returned no match in `beshaba/wiki.txt`.

---

## 3. Selûne

### Field 1: Identity

**FRHoF (5etools)**

> "## Selûne | source FRHoF p.119 | pantheon Faerûnian"
> "- altNames: ['The Moonmaiden', 'The Night White Lady', 'Our Lady of Silver']"
> "- title: God of the moon"
> "- worshipers: Lycanthropes, sailors, spellcasters"
> "- plane: Ysgard (Ysgard)"
> — `selune/5etools.md:1-5`

**SCAG, 2014 (5etools)**

> "## Selûne | source SCAG p.21 | pantheon Faerûnian"
> "- altNames: ['Our Lady of Silver', 'The Moonmaiden', 'The Night White Lady']"
> "- title: Goddess of the moon"
> "- alignment: ['C', 'G']"
> "- domains: ['Knowledge', 'Life', 'Twilight']"
> "- symbol: Pair of eyes surrounded by seven stars"
> — `selune/5etools.md:27-32`

**Wiki (lead)**

> "also known as '''Our Lady of Silver''', the '''Moonmaiden''', and the '''Night White Lady''', was the goddess of the moon in the Faerûnian pantheon."
> — `selune/wiki.txt:111` (refs follow later in the same line)

### Field 2: Edict or core tenet

> "''Let all on whom my light falls be welcome if they desire to be so. As the silver moon waxes and wanes, so too does all life. Trust in my radiance, and know that all love alive under my light shall know my blessing. Turn to the moon, and I will be your true guide.''"
> — `selune/wiki.txt:118` (the words of Selûne "which all novices were charged with"; the attribution is on `selune/wiki.txt:119` and cites Faiths and Avatars p.136)

### Field 3: Portfolio and Areas of Concern

> "She is also a god of stars, navigation, and motherhood."
> — `selune/5etools.md:7` (FRHoF)

> "She is also a goddess of stars and navigation as well as motherhood and reproductive cycles."
> — `selune/5etools.md:34` (SCAG, 2014)

Areas of Concern: no 5etools entry gives this field. Not sourced.

### Field 4: Worship

> "Selûne is venerated by navigators, sailors, those who work at night, those seeking protection in the dark, the lost, and the questing. Temples to the Moonmaiden include a series of windows that reveal the moon in the night sky at various positions and in different phases throughout the year."
> — `selune/5etools.md:10` (FRHoF)

> "Selûne's rites include trances and meditation. Those who favor her set a bowl of milk outside on each night of the full moon."
> — `selune/5etools.md:11` (FRHoF)

> "Selûne and her teachings of compassion and guidance were appealing to all folk who lived their lives by the moonlit night sky, and hence her faithful were a very diverse group."
> — `selune/wiki.txt:193`

> "| holy days2e         = Conjuring of the Second Moon ([[Shieldmeet]]); Mystery of the Night (varies)"
> — `selune/wiki.txt:86` (2e field; link brackets removed)

> "When she sends an emissary to mortals, she sends an {@creature Owl|XMM} or other night bird, a moonlight-hued {@creature Planetar|XMM}, or a benevolent lycanthrope, commonly a {@creature Werebear|XMM}. Lycanthropes are said to be blessed by Selûne."
> — `selune/5etools.md:8` (FRHoF; messengers and omens; {@creature} tags kept as written)

> "Swords of the Lady: The Swords of the Lady is an order of knights devoted to Selûne."
> — `selune/5etools.md:13` (FRHoF; clergy and orders)

### Field 5: Relations and origin

> "Selûne counted as her allies fellow deities of the moon, beauty, fortune, joy, light, magic, and weather."
> — `selune/wiki.txt:173` (paragraph refs include Faiths & Avatars p.134)

> "Her eternal enemy was her sister Shar, goddess of the night, a war that had been waged since before all other Faerûnian gods existed, before time was recorded."
> — `selune/wiki.txt:175`

> "Her other great foes were Mask, for the mischief and wickedness he made in the shadows formed by her moon's light at night; Umberlee, over the fates of ships at sea; and the rotting god Moander.<ref name="FRCS1e-p13"/><ref name="F&A-p134"/><ref name="FRCS3e-p248"/><ref name="FaP-p55"/><ref name="F&A-p109">{{cite book/Faiths and Avatars|109,119,173}}</ref>"
> — `selune/wiki.txt:177`

> "The principal legend about Selûne recounts the battle at the beginning of time between Selûne and her sister, Shar."
> — `selune/5etools.md:9` (FRHoF)

> "Selûne was believed to be one of the oldest deities known in Faerûn."
> — `selune/wiki.txt:219`

> "Selûne had been an independent deity for millennia, but her might waned and in time she came to serve Sune, goddess of love, for several centuries.<ref name="FRCS1e-p13"/><ref name="F&A-p134"/><ref name="FaP-p55"/>"
> — `selune/wiki.txt:262`

### Field 6: Campaign and published-adventure mentions (non-temple)

> "- **Research:** The Midsummer wiki page, and pages for Twin Parades, Selûne Sashelas and Fey Day, are not in the wiki folder. Midsummer is housed from the Calendar of Harptos, Shieldmeet and published-adventure entries only. Fey Day uses the published adventure."
> — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:157`

This line names a page called "Selûne Sashelas". It states no fact about Selûne.

> "On whatever night in Uktar the moon is fullest, Waterdavians celebrate Selûne's Hallowing. The goddess is the focus of worship throughout the full phase, of course, but the major ceremony on this night is a parade of worshipers leaving the House of the Moon at moonrise and moving down to the harbor, where the high priestess wields the Wand of the Four Moons in a ceremony blessing all navigators."
> — `sources/adventure-wdh.json:31558` (festival "Uktar: Selûne's Hallowing", named at line 31554)

> "If you're lucky, you might see the Wand of the Four Moons weep. Droplets said to be the tears of Selûne manifest on the mace from time to time, and are collected by the priestesses for use in potions that can heal, cure lycanthropy, and be used as holy water."
> — `sources/adventure-wdh.json:31559`

### Field 7: Conflicts and not found

- **Conflict (House of the Moon vs Tower of the Moon).** The published adventure's text calls the temple the "House of the Moon", and its own Major Temples table calls it the "Tower of the Moon". The full set is under Q1.
- **Conflict (plane, by edition).** 5etools gives Ysgard (`selune/5etools.md:5`). The wiki's 3e field gives "| homeplane3e         = [[Gates of the Moon]]" (`selune/wiki.txt:62`).
- **Not found.** No Selûne NPC, faction or quest in `campaign/`. No Swords of the Lady in `campaign/`. The campaign's text names the House of the Moon nowhere.

### Q1. Temples or shrines in Waterdeep, and wards

**Published adventure**

> "The beauteous House of the Moon has the tallest tower of any temple in the city, rising some seventy-five feet above the street."
> — `sources/adventure-wdh.json:30881` (Sea Ward section, which begins at line 30873)

> "At its top, priests of Selûne bask in the light of the moon in all seasons."
> — `sources/adventure-wdh.json:30881`

**Major Temples table** (caption at `sources/adventure-wdh.json:30910`)

> "Selûne",
> "Tower of the Moon",
> "Sea Ward"
> — `sources/adventure-wdh.json:30968`, `:30969`, `:30970`

**Undermountain adventure**

> "Two daggers stuck in the map mark the Spires of the Morning (the temple of Lathander in the Castle Ward) and the House of the Moon (the temple of Selûne in the Sea Ward)."
> — `sources/adventure-wdmm.json:50537` (the map in Vanrakdoom, Undermountain)

> "She also has her sights set on destroying the House of the Moon—Waterdeep's temple of Selûne, whom she blames for the destruction of Vanrak Moonstar."
> — `sources/adventure-wdmm.json:48631`

**Campaign files**

> "- Tymora's Tower of Luck is placed in the Castle Ward by the Dragon Heist temple table and in the Sea Ward by its Sea Ward text and by the campaign's own Waterdeep outline, so it is not a Castle Ward temple here. Selûne's Tower of the Moon is Sea Ward in both."
> — `campaign/gazetteer/waterdeep/castle-ward.md:165` (only the second sentence concerns Selûne)

> "> - **Conflicts:** Tower of Luck. The Dragon Heist temple table lists it in the Castle Ward; the Dragon Heist Sea Ward text and `waterdeep-lore.md` place it in the Sea Ward. `waterdeep-lore.md` also puts the Selûne temple in the Sea Ward."
> — `campaign/gazetteer/waterdeep/castle-ward.md:271` (Draft Notes)

> "- Major temples in Sea Ward: Tymora (Luck; popular with adventurers and criminals alike), Selûne (Moon; widely attended)"
> — `campaign/setting/waterdeep-lore.md:36`

Retired file:

> "- Major temples in Sea Ward: Tyr (Justice; City Watch captain is a worshiper), Tymora (Luck; popular with adventurers and criminals alike), Selûne (Moon; widely attended)"
> — `campaign/structure/ch2-city-of-splendors.md:56`

**Placement summary.** Every placement names the Sea Ward: `sources/adventure-wdh.json:30881` (text) and `:30970` (table), `sources/adventure-wdmm.json:50537`, `castle-ward.md:165`, `castle-ward.md:271`, `waterdeep-lore.md:36`, and `ch2-city-of-splendors.md:56` (retired). No source places a Selûne temple in the Castle Ward.

**Wiki (not a ward address)**

> "She kept her full divine powers and access to the planes behind a locked door in the inn and kept the ''Wand of the Four Moons'' at the [[House of the Moon]], her local temple.<ref name="ADDc-22"/><ref name="ADDc-19"/>"
> — `selune/wiki.txt:266` (the same line says Luna ran "the Selûne's Smile inn and tavern"; this is the wiki, not a campaign file)

### Q2. Which campaign NPC, faction or quest uses Selûne?

None. The campaign's only Selûne lines are the ward placements above and the page name at `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:157`. No NPC, faction or quest in `campaign/` names Selûne.

### Q3. Which wiki lines mention Waterdeep?

> "For a long time, Selûne had chosen to live her life as a mortal woman in the city of Waterdeep. Named Luna, she ran the Selûne's Smile inn and tavern in the city.<ref name="FRCS2e-p52"/><ref name="F&A-p134"/><ref name="ADDc-01">{{Cite comic/The Gathering}}</ref><ref name="ADDc-19"/>"
> — `selune/wiki.txt:266` (refs: Forgotten Realms Campaign Setting 2e p.52; Faiths and Avatars p.134; comic "The Gathering")

> "She kept her full divine powers and access to the planes behind a locked door in the inn and kept the ''Wand of the Four Moons'' at the House of the Moon, her local temple.<ref name="ADDc-22"/><ref name="ADDc-19"/>"
> — `selune/wiki.txt:266`

> "Selûne to Shar during their battle over Waterdeep.<ref name="ADDc-22"/>"
> — `selune/wiki.txt:272` (source line of a figure quote)

> "In the {{YearlinkName|1358}}, the Time of Troubles came, magic went awry, and the gods were forced to walk the Realms in mortal form."
> — `selune/wiki.txt:274` (the same line continues below)

> "Restricting herself to only non-divine powers, she knew no more than her mortal friends, until Onyx reported the appearance of an avatar in Waterdeep—an avatar of Selûne, one who was not Luna."
> — `selune/wiki.txt:274`

> "First, on Luna's instruction, Vajra snuck into the House of the Moon to find the ''Wand of the Four Moons''."
> — `selune/wiki.txt:274`

> "Famously, Selûne battled Shar over the streets of Waterdeep.<ref name="F&A-p136"/><ref name="ADDc-22"/><ref name="CoS-AGttC-p15">{{Cite book/City of Splendors (boxed set)/Adventurer's Guide to the City|15}}</ref><ref name="tGHotR-p144">{{Cite book/The Grand History of the Realms|144}}</ref>"
> — `selune/wiki.txt:279`

> "''Selûne's light blasting Shar's Rod of Oblivion, during their battle over Waterdeep.''"
> — `selune/wiki.txt:278` (figure caption)

---

## 4. Shar

### Field 1: Identity

**FRHoF (5etools)**

> "## Shar | source FRHoF p.120 | pantheon Faerûnian"
> "- altNames: ['The Mistress of the Night', 'The Dark Lady', 'Our Lady of Loss']"
> "- title: God of darkness and loss"
> "- worshipers: Anyone suffering pain or loss"
> "- plane: Hades (Niflheim)"
> — `shar/5etools.md:1-5`

**SCAG, 2014 (5etools)**

> "## Shar | source SCAG p.21 | pantheon Faerûnian"
> "- altNames: ['The Mistress of the Night', 'The Dark Lady', 'Our Lady of Loss']"
> "- title: Goddess of darkness and loss"
> "- alignment: ['N', 'E']"
> "- domains: ['Death', 'Trickery']"
> "- symbol: Black disk encircled with a purple border"
> — `shar/5etools.md:26-31`

**Wiki (lead)**

> "also known as '''Mistress of the Night''' and the '''Lady of Loss''', was the goddess of darkness and the night in the Faerûnian pantheon and the malevolent twin sister and counterpart to the goddess of the moon, Selûne."
> — `shar/wiki.txt:125`

### Field 2: Edict or core tenet

The published adventure's altar inscription gives the core tenets. These are the four items of one list. The list is introduced by "Inscriptions carved into the altar are written in a secret language known only to Shar's faithful. A {@spell comprehend languages} spell or similar magic reveals that these inscriptions spell out the core tenets of Shar's faith:" (`sources/adventure-wdmm.json:50781`).

> "In darkness, act. Never wait for the darkness to pass before making your move."
> — `sources/adventure-wdmm.json:50785`

> "Quench the light of the moon when you can. Hide from it when you can't."
> — `sources/adventure-wdmm.json:50786`

> "Keep secrets from all except Shar's faithful."
> — `sources/adventure-wdmm.json:50787`

> "Only a fool believes in hope."
> — `sources/adventure-wdmm.json:50788`

### Field 3: Portfolio and Areas of Concern

> "The dark twin of Selûne, Shar is a god of darkness, both in its physical form and as it exists in the minds and souls of mortals. People worship Shar as the god of night, secrets, loss, and forgetfulness."
> — `shar/5etools.md:7` (FRHoF)

> "In the 14{{th}} and 15{{th}} centuries DR, she held the portfolios of darkness, forgetfulness, loss, and night<ref name="CotR-p14" /><ref name="FRA-30" /><ref name="RtR-p48" /><ref name="F&A-p138" /><ref name="TWoN-p55" /><ref name="OHG-p170" /><ref name="FRCS3e-p249" /><ref name="FaP-p58" /><ref name="SCAG5e-p21,36-37" /> and after she slew the underground god Ibrandul she claimed the portfolios of caverns, dungeons, and the Underdark.<ref name="F&A-p138" />"
> — `shar/wiki.txt:125` (link brackets removed; refs as printed)

Areas of Concern: no 5etools entry gives this field. Not sourced.

### Field 4: Worship

> "Shar is revered by those who venture into dark places, such as miners, as well as by those who fall into melancholy and despair, who wish to forget something, or who wish to recover something lost."
> — `shar/5etools.md:9` (FRHoF)

> "The tragedies and losses brought about by her followers have caused realms to outlaw her worship, driving her priests into secrecy."
> — `shar/5etools.md:9` (FRHoF; a later sentence of the same line, with other sentences between)

> "The clergy of Shar were a secretive organization that pursued subversive tactics rather than direct confrontation with its rivals. In many cities where worshiping Shar was barred, these churches and temples were hidden because of their illegal nature."
> — `shar/wiki.txt:232` (the sentence has no ref; the next sentence in the line cites Faiths & Pantheons p.58 and Lords of Darkness p.122)

> "| holy days3e         = Rising of the Dark ([[Feast of the Moon]])"
> — `shar/wiki.txt:83` (3e field; link brackets removed)

> "Order of the Dark Moon: Shar's Order of the Dark Moon studies darkness, deception, stealth, assassination, and espionage. Monks, Rogues, Sorcerers, grim Rangers, and other characters who seek to cast away their grief into Shar's blissful forgetfulness are welcomed into the order."
> — `shar/5etools.md:11` (FRHoF; clergy)

> "She appears to mortals in dreams, or she sends a {@creature Death Tyrant|XMM} or {@creature Shadow|XMM} as an emissary."
> — `shar/5etools.md:8` (FRHoF; messengers; {@creature} tags kept as written)

### Field 5: Relations and origin

> "Her eternal enemy was her sister Selûne, goddess of the moon, a war that had been waged since before all other Faerûnian gods existed, before time was recorded."
> — `shar/wiki.txt:193`

> "By her very nature, Shar was of course opposed to all the gods of light and fire, namely Lathander, god of the morning (her crushing of creative spirit also put her counter to his emphasis on creativity<ref name="OHG-p170" />), and Amaunator, the god of the sun, at least while they were together in the Netherese pantheon."
> — `shar/wiki.txt:197` (the sentence continues on the same line)

> "Selûne is the bitter rival of Shar, and the Order of the Dark Moon frequently works against Selûne's militant orders and priests. The order finds allies in the cult of the death god Myrkul."
> — `shar/5etools.md:16` (FRHoF; rivals and allies)

> "In time, Shar coalesced from the primordial essence, alongside her twin sister, Selûne."
> — `shar/wiki.txt:246` (Creation; paragraph refs include Faiths & Avatars p.141 and Forgotten Realms Campaign Setting 3e p.249)

> "The dark twin of Selûne, Shar is the goddess of darkness, both in its physical form and as it exists in the minds and souls of mortals."
> — `shar/5etools.md:33` (SCAG, 2014; first sentence of the line)

### Field 6: Campaign and published-adventure mentions

**Campaign:** zero hits. Grep of `campaign/` for `\bShar\b`, `Sharran`, `Mistress of the Night`, `Lady of Loss`, `Dark Moon` and `Dark Army` returned nothing.

**Published adventure, 42 hits in all (41 in `sources/adventure-wdmm.json`, 1 in `sources/adventure-wdh.json`).** Six are quoted here. The sixth, `sources/adventure-wdmm.json:48631`, is quoted under Q1.

> "Adherents of Shar have been active in the shadow of Mount Waterdeep ever since a disastrous expedition to the Black Jungles mounted in the Year of the Dark Dawn (1104 DR) by Lord Vanrak Moonstar, a charismatic, outgoing swashbuckler."
> — `sources/adventure-wdmm.json:48606` (Vanrakdoom, Undermountain)

> "Upon assuming leadership of House Moonstar, Vanrak publicly broke with the temple of Selûne (god of the moon), which he blamed for his father's untimely death. Consumed with bitterness, the Dark Ranger, as Vanrak came to be known, secretly embraced Selûne's sister: Shar, the Lady of Loss."
> — `sources/adventure-wdmm.json:48607`

> "The cult of Shar in Vanrakdoom consists mainly of {@creature vampire spawn} under the command of {@creature Keresta Delvingstone|WDMM}. Living cultists also find their way here from time to time, guided through Undermountain by the dark grace of Shar herself."
> — `sources/adventure-wdmm.json:48712`

> "Inscriptions carved into the altar are written in a secret language known only to Shar's faithful. A {@spell comprehend languages} spell or similar magic reveals that these inscriptions spell out the core tenets of Shar's faith:"
> — `sources/adventure-wdmm.json:50781`

> "This holy relic is said to be the mace wielded by Selûne in her first battle against Shar, and again in a fight with her sister during the Time of Troubles."
> — `sources/adventure-wdh.json:31558` (festival "Uktar: Selûne's Hallowing"; the only wdh hit)

Remaining hits, file:line only: `sources/adventure-wdmm.json:472`, `:473`, `:4051`, `:6387`, `:6417`, `:48599`, `:48608`, `:48612`, `:48613`, `:48623`, `:48692`, `:48693`, `:48708`, `:48713`, `:49820`, `:49834`, `:49938`, `:49951`, `:49970`, `:50035`, `:50059`, `:50060`, `:50064`, `:50084`, `:50101`, `:50221`, `:50246`, `:50534`, `:50607`, `:50696`, `:50724`, `:50837`, `:50852`, `:50856`, `:59838`.

### Field 7: Conflicts and not found

- **Conflict (symbol).** SCAG gives a purple border: "- symbol: Black disk encircled with a purple border" (`shar/5etools.md:31`). PHB 2014 gives no color: "- symbol: Black disk encircled with a border" (`shar/5etools.md:22`). The wiki's 5e field agrees with SCAG: "| symbol5e            = Black disk with a purple border" (`shar/wiki.txt:43`).
- **Conflict (plane, by edition).** FRHoF gives "- plane: Hades (Niflheim)" (`shar/5etools.md:5`). The wiki's 5e field gives "| homeplane5eR        = [[Hades]] ([[Niflheim]])" (`shar/wiki.txt:29`). The wiki's 3e field gives "| homeplane3e         = [[Plane of Shadow]]" (`shar/wiki.txt:73`).
- **Not found.** No Shar temple in Waterdeep in any file read. No Shar NPC, faction or quest in `campaign/`. No Sharran shrine in Waterdeep in any source read.

### Q1. Temples or shrines in Waterdeep

None in the published adventure or the campaign. The Undermountain cult is in Vanrakdoom, a level of Undermountain, not a Waterdeep address. The wiki places a Shar episode in the House of the Moon during the Time of Troubles. That is the wiki, not a campaign or adventure file:

> "The next, she descended from the sky and onto the steps of the House of the Moon temple, greeted the faithful, promised her grace and protection, and encouraged them to proclaim her to be Selûne."
> — `shar/wiki.txt:277` (Time of Troubles, 1358 DR)

> "Now posing as Selûne, Shar became mistress of the temple and enjoyed its hospitality, residing in high priestess Naneatha Suaril's own quarters."
> — `shar/wiki.txt:284`

> "She also has her sights set on destroying the House of the Moon—Waterdeep's temple of Selûne, whom she blames for the destruction of Vanrak Moonstar."
> — `sources/adventure-wdmm.json:48631` (a Shar cultist's aim, not a Shar temple)

### Q2. Campaign NPC, faction or quest

None. Zero hits in `campaign/`.

### Q3. Wiki lines mentioning Waterdeep

> "During the Time of Troubles of the Year of Shadows, 1358 DR, magic went awry and the gods were forced to dwell in the mortal world. The avatar of Shar came to the city of Waterdeep in the guise of her sister Selûne."
> — `shar/wiki.txt:277` (first two sentences of the paragraph)

> "The next, she descended from the sky and onto the steps of the House of the Moon temple, greeted the faithful, promised her grace and protection, and encouraged them to proclaim her to be Selûne."
> — `shar/wiki.txt:277`

> "Selûne to Shar during their battle over Waterdeep.<ref name="ADDc-22">{{Cite comic/Total Eclipse}}</ref>"
> — `shar/wiki.txt:283` (source line of a figure quote)

> "Later, a party was held at Castle Waterdeep in honor of the supposed avatar of the goddess Selûne."
> — `shar/wiki.txt:287`

> "''Selûne's light blasting Shar's Rod of Oblivion, during their battle over Waterdeep.''"
> — `shar/wiki.txt:289` (figure caption)

---

## 5. Lliira

### Field 1: Identity

**FRHoF (5etools)**

> "## Lliira | source FRHoF p.112 | pantheon Faerûnian"
> "- altNames: ['Mistress of Revels', 'Our Lady of Joy']"
> "- title: God of joy"
> "- worshipers: Bards, dancers, poets, revelers, singers"
> "- plane: Arborea (Arvandor)"
> — `lliira/5etools.md:1-5`

**SCAG, 2014 (5etools)**

> "## Lliira | source SCAG p.21 | pantheon Faerûnian"
> "- altNames: ['Our Lady of Joy', 'Joybringer', 'The Mistress of Revels']"
> "- title: Goddess of joy"
> "- alignment: ['C', 'G']"
> "- domains: ['Life']"
> "- symbol: Triangle of three six-pointed stars"
> — `lliira/5etools.md:21-26`

**Wiki (lead)**

> "was a chaotic good lesser deity of joy (and for a time an exarch of Sune)<ref name="FaPp99" /><ref name="FRCG-p81">{{Cite book/Forgotten Realms Campaign Guide|81}}</ref> in the Faerûnian pantheon."
> — `lliira/wiki.txt:117` (Faiths and Pantheons p.99; Forgotten Realms Campaign Guide 4e p.81)

### Field 2: Edict or core tenet

> "The Mistress of Revels is said to abhor violence, and any fighting or drawing of weapons (except in ceremony) at a celebration will cause her to withhold her favor."
> — `lliira/5etools.md:28` (SCAG, 2014)

### Field 3: Portfolio and Areas of Concern

> "Lliira is a beloved goddess, a deity of contentment, release, joy, happiness, dance, and freedom. As the patron of festivals, she is honored at any celebration, and dance is the primary way to worship her."
> — `lliira/5etools.md:28` (SCAG, 2014; first two sentences)

> "She embodies joy, contentment, dance, and freedom, and is beloved by many."
> — `lliira/5etools.md:7` (FRHoF)

Areas of Concern: no 5etools entry gives this field. Not sourced.

### Field 4: Worship

> "Dancers and hedonists are among the Lliira's most devoted worshipers. Some of her followers train in bardic techniques of the College of Dance to better express their devotion. Her followers wear at least one item of clothing in a bright, cheerful color. They aren't frivolous, however. To them, divine joy is a greatly needed gift to the world of mortals."
> — `lliira/5etools.md:9` (FRHoF)

> "Lliira's priests, known as joybringers, spread joy wherever possible. They throw excellent parties and are among the most beloved clergy in Faerûn. Joybringers' vestments more resemble festival attire than somber ecclesiastical garments. Joybringers are folk of whimsy and light spirits, prone to jokes but never pranks. Fighting or drawing weapons (except in ceremony) is strictly forbidden at joybringer celebrations."
> — `lliira/5etools.md:10` (FRHoF)

> "Both the specialty priests and clerics of Lliira were known as "Joybringers" until 1365 DR, when members of the clergy became confused by the naming scheme. From that year onward the specialty priests were distinguished by the title of "Joydancer."<ref name="F&A-p97" />"
> — `lliira/wiki.txt:142`

> "| holy days2e         = Lliira's Night<ref name="CoS:W-p253">{{Cite book/City of Splendors: Waterdeep|253}}</ref>"
> — `lliira/wiki.txt:90` (2e field)

> "Originally a celebration held only in Waterdeep, this holiday has since spread up and down the Sword Coast. It has received a recent boost in popularity from the custom started in Baldur's Gate of lighting celebratory smokepowder fireworks-all purchased from Felogyr's Fireworks of that city, and utilized only by the City Guard, of course."
> — `sources/adventure-wdh.json:31470` (entry "Flamerule 7: Lliira's Night", line 31466)

> "Joyful {@b Empyrean Iotas} or dancing pixies are Lliira's messengers of choice."
> — `lliira/5etools.md:8` (FRHoF; messengers; {@b} tag kept as written)

### Field 5: Relations and origin

> "Among the Faerûnian pantheon, Lliira's best friend was the deity Milil, due to him sharing of her love for revelry.<ref name="FaPp99" /><ref name="F&A-p96" />"
> — `lliira/wiki.txt:133`

> "Another deity she was good friends with for this reason was the goddess Sharess.<ref name="P&P-p52">{{Cite book/Powers & Pantheons|52}}</ref>"
> — `lliira/wiki.txt:135`

> "Prior to the Time of Troubles another good friend of hers was the goddess Waukeen."
> — `lliira/wiki.txt:137`

> "When Lord Ao cast nearly all the Faerûnian deities into mortal avatar form and scattered them across the surface of Toril, Lliira was among them."
> — `lliira/wiki.txt:158` (paragraph refs include For Duty & Deity p.3 and Faiths & Avatars pp.176-177)

> "Lliira resided within the divine domain of Brightwater, sharing it with the goddesses Sune and Tymora.<ref>{{Cite book/Planes of Chaos/The Book of Chaos|39}}</ref> After events of the Spellplague, Lliira became an exarch of Sune and moved to the Gates of the Moon with her.<ref name="FRCG4e-81">{{Cite book/Forgotten Realms Campaign Guide|81}}</ref><ref name="PGtF-147">{{Cite book/Player's Guide to Faerûn|147}}</ref><ref name="FaP-99">{{Cite book/Faiths & Pantheons|99}}</ref><ref name="FRCG4e-63">{{Cite book/Forgotten Realms Campaign Guide|63}}</ref>"
> — `lliira/wiki.txt:130` (the Brightwater sentence is the older setting; the Gates of the Moon sentence is 4e)

### Field 6: Campaign and published-adventure mentions

> "- **The ten days between.** Sornyn (Flamerule 3 to 5) and Lliira's Night (Flamerule 7) fall inside them. See the hooks below."
> — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:94`

> "| Flamerule 7 | Lliira's Night | Dances and balls through the night, with smokepowder fireworks set off by the City Guard until dawn. |"
> — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:109`

> "- **Sornyn and Lliira's Night, Flamerule 3 to 7.** Envoys and strangers are expected in the city and smokepowder fireworks boom until dawn on Flamerule 7, so unfamiliar faces and loud noises draw no notice in the ten days between the feast and the birthday."
> — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:119`

> "Led by the clergy of Sune, Sharess, and Lliira, the Grand Revel is a day of dancing, music, and the consumption of sweet treats of all kinds, from chocolate to red firemint candies."
> — `sources/adventure-wdh.json:31367` (entry "Alturiak 14: The Grand Revel", line 31363; the three clergies named are Sune, Sharess and Lliira)

### Q1. Temples or shrines in Waterdeep

None. The Major Temples table has no Lliira row (`sources/adventure-wdh.json:30910` to `:31000`). No campaign file places a Lliira temple. The wiki's temples are outside Waterdeep:

> "* [[House of Happiness]] in [[Hillsfar]]"
> — `lliira/wiki.txt:151`

> "* [[Palace of Holy Festivals]] in [[Selgaunt]]."
> — `lliira/wiki.txt:152`

> "* [[Theater of Joy]] in [[Crimmor]]<ref name="LoI-A-30">{{Cite book/Lands of Intrigue/Amn|30}}</ref>"
> — `lliira/wiki.txt:153`

### Q2. Campaign NPC, faction or quest

None. The campaign's only Lliira lines are the festival entries in Field 6. No NPC, faction or quest in `campaign/` names Lliira.

### Q3. Wiki lines mentioning Waterdeep

One line, the 2e holy-day field:

> "| holy days2e         = Lliira's Night<ref name="CoS:W-p253">{{Cite book/City of Splendors: Waterdeep|253}}</ref>"
> — `lliira/wiki.txt:90`

---

## Conflicts between sources (summary)

- **Tower of Luck (Tymora).** The table says "Castle Ward" (`sources/adventure-wdh.json:30985`). The Sea Ward text places it in the Sea Ward section (`sources/adventure-wdh.json:30882`). `castle-ward.md:31` lists it in the Castle Ward and says it is "placed in the Sea Ward elsewhere". `castle-ward.md:165` gives the Sea Ward placement. `castle-ward.md:271` records the conflict. The brief's hub rule says "the campaign file wins" (`docs/plans/setting-compendium-pass2-brief.md:58`). This report does not choose.
- **Tower of the Moon vs House of the Moon (Selûne).** The published adventure's text calls the temple the "House of the Moon" (`sources/adventure-wdh.json:30881`). Its table calls it the "Tower of the Moon" (`sources/adventure-wdh.json:30969`). Campaign and Undermountain files both give the Sea Ward (`castle-ward.md:165`, `sources/adventure-wdmm.json:50537`).
- **Shar symbol.** SCAG gives a purple border (`shar/5etools.md:31`). PHB 2014 gives no color (`shar/5etools.md:22`).
- **Shar plane, by edition.** FRHoF gives Hades (Niflheim) (`shar/5etools.md:5`). The wiki's 3e field gives Plane of Shadow (`shar/wiki.txt:73`).
- **Tymora worshipers, by edition.** FRHoF gives Harpers and merchants (`tymora/5etools.md:4`). The wiki's 5e field gives game-players and adventurers (`tymora/wiki.txt:63`).
- **Beshaba worshipers, by edition.** FRHoF gives Red Wizards and Rogues (`beshaba/5etools.md:4`). The wiki's 5e field gives Druids and Red Wizards of Thay (`beshaba/wiki.txt:63`).
- **Tymora pantheon label.** PHB 2014 gives "Forgotten Realms" (`tymora/5etools.md:14`). FRHoF and SCAG give Faerûnian.
- **Tymora realm, by edition.** FRHoF gives Arborea (`tymora/5etools.md:5`). The wiki says Gates of the Moon after the Spellplague (`tymora/wiki.txt:179`).
- **Festival naming (Beshaba).** The adventure's Reign of Misrule honors Beshaba (`sources/adventure-wdh.json:31526`). The campaign calendar names the Reign without Beshaba (`campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:111`). No contradiction, but the campaign does not tie the festival to her.

## Cross-references

Other files and lines that mention these powers and are not quoted above:

- `sources/adventure-wdh.json:31554` (name line "Uktar: Selûne's Hallowing")
- `sources/adventure-wdmm.json` lines for Selûne not quoted above: `44045`, `45947`, `48608`, `48610`, `48613`, `50398`, `50736`, `52327`. Lines `44045`, `45947` and `52327` concern the asteroid cluster "Tears of Selûne", not the deity.
- `sources/adventure-wdmm.json:48607` (quoted under Shar; it also names Selûne)
- Outside scope, not read, but named by a repo-wide Grep for "Tower of Luck", "Tower of the Moon", "House of the Moon", "Tymora" and "Selûne": `docs/plans/setting-compendium-pilot-findings.md`, `docs/plans/setting-compendium-research-notes/consistency-pilot-pages.md`, `docs/plans/setting-compendium-research-notes/pass1-era8-calendar.md`, `docs/plans/force-grey-research/03-m01-m03.md`, `docs/plans/force-grey-research/05-consistency-audit.md`, `session 46 handoff.md`, `session 47 handoff.md`, `.claude/skills/character-voices/voices/independents-allies.md`, `docs/index.html`.

## Not found (terms searched)

- **`campaign/` (all of it).** For Tymora: `Tymora|Lady Luck|Smiling Lady|Tower of Luck|Tymoran|Luckbringer`. For Beshaba: `Beshaba|Lady Doom|Maid of Misfortune|Maiden of Misfortune|Black Bess|Misrule|Wormluck|Doommaster|misfortune`. For Selûne: `Selûne|Selune|Selûn|Moonmaiden|Our Lady of Silver|Night White Lady|House of the Moon|Tower of the Moon|Swords of the Lady|Wand of the Four Moons|Lunatics`. For Shar: `\bShar\b|Shar's|Sharran|Mistress of the Night|Lady of Loss|Our Lady of Loss|Dark Moon|Dark Army|Order of the Dark Moon` (zero hits), and plain `\bShar\b` (count 0). For Lliira: `Lliira|Mistress of Revels|Our Lady of Joy|Joybringer|Joydancer`. Also `Simril|Starfall|Grand Revel|Reign of Misrule|\bLuna\b|Sashelas|Lliira's Night|Night of Stars|Tyche`.
- **`campaign/gazetteer/` (ward search).** `Tower of Luck|Tower of the Moon|House of the Moon|Lady's House|Luck|Moon|Helm's Hall|Temple of Helm`.
- **`sources/adventure-wdh.json` and `sources/adventure-wdmm.json`.** The same alias lists, plus the Major Temples table (lines 30910 to 31000).
- **Not in the sources at all.** A Tymoran temple outside the Tower of Luck. A Selûne Castle Ward placement. A Shar or Beshaba temple in Waterdeep. A Lliira temple in Waterdeep. A campaign NPC, faction or quest for Shar, Beshaba or Lliira.
- **Not in the bundles.** Areas of Concern for all five powers (no such field in 5etools or the wiki). Waterdeep holy-day locations for any of the five beyond the festivals listed.

## Not readable

None of the five bundles or the two adventure JSON files failed to open. The Alexandrian PDFs, `SOURCE_GUIDE.md` and the `Other remix files` folder were not read, as the caller's scope asked.
