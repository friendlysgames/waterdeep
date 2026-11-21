# Pass 6 research notes: Noska Ur'gray

Page: `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 16 and the user rulings)
Format model: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Voice profile: `.claude/skills/character-voices/voices/xanathars-guild.md`, the `### Noska Ur'gray` heading
Faction page: `campaign/setting/organizations/08-xanathars-guild.md`

Method and caveats:
- Campaign files: Read and Grep, quoted from the file.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. JSON escapes are shown as plain quotes.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. Each PDF was read with the Read tool's `pages` parameter. Quotes from PDFs are transcriptions of the rendered page image and must be checked against `pdftotext -layout` before any prose use. Cite as printed page with PDF page in brackets.
- Wiki: the extracted page `scratchpad/wiki-xg/Noska_Ur_gray.txt` (cited as `wiki-xg/Noska_Ur_gray.txt:N`). The same text sits in `sources/research/pass5-bundles/xanathars-guild/wiki.txt` from line 1644 on, and the bundle line is given in brackets. The wiki prints no edition on most lines. The infobox fills `alignment5e` and `class5e`, and the citation key `WDH5e-p213` is 5e, so 5e is stated by the key; other edition tags are marked inferred.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.
- Pronouns: he/him is sourced (see B). The brief's ruling 4 is met.

---

## Answers to the three specific checks

**1. Is `campaign/setting/deities/maglubiyet.md:121` day-one?** Partly. Its first clause is day-one and its second clause is quest-time.

> "- **Noska Ur'gray**, **Ott Steeltoes** (Notable Figures): the bugbear response team's leader and the fishkeeper the bugbears hunt in **Three Nights**."
> — `campaign/setting/deities/maglubiyet.md:121`

- "the bugbear response team's leader": day-one. The Factions Guide states the standing team: "**Third Team — Noska's Team.** Noska Ur'gray leads six **bugbears** and a **gazer**. He is sent when Xanathar is done sending messages and wants the problem gone." (`campaign/guides/factions/09-xanathars-guild.md:13`)
- "the fishkeeper the bugbears hunt in **Three Nights**": quest-time. Three Nights is a Bregan D'aerthe mission (`campaign/quests/faction-events/bregan-daerthe/m03-three-nights/overview.md:31`). Its own files do not link Noska to these bugbears. See D6.
- The same claim is repeated at `campaign/setting/deities/maglubiyet.md:82`, which is also a setting page. Under the setting rule the Three Nights clause belongs in **Three Nights**, not on a setting page.

**2. The Noska versus Ahmaergo rivalry (`sources/SOURCE_GUIDE.md:343`).** Only two repo files state it, and neither is day-one lore. The published adventure shows the two working together.

> "- Internal politics the PCs can exploit: Nar'l Xibrindas (drow spy working against Xanathar for House Xorlarrin), Noska vs. Ahmaergo rivalry, the Sylgar distraction (Xanathar's goldfish — stealing or threatening it causes Xanathar to abandon tactical thinking)"
> — `sources/SOURCE_GUIDE.md:343` (listed under the Alexandrian `11. Lair  Xanathar's Lair.pdf` entry, `sources/SOURCE_GUIDE.md:335`)

> "The Noska–Ahmaergo rivalry has reached near-blows twice in the past month; during an active tournament, Noska is arena-side and Ahmaergo is in his quarters reviewing fight records, neither monitoring the other's territory. That window is real and exploitable. At renown 10+, Yagra Stonefist is available as outside backup — she can hold the guildsign entrance open from the exterior, delay a pursuing Guild patrol by 5 minutes, or cover the party's extraction from the sewer exit. Once per operation."
> — `campaign/structure/arc-f-xanathars-lair.md:41` (a Doom Raiders intelligence bullet, quest content; the bullet opens with Tashlyn Yafeera or Davil Starsong as the contact)

- The Alexandrian Lair PDF, which `SOURCE_GUIDE.md:343` cites, was read in full (nine pages, see Not readable). It has no rivalry text. Check with `pdftotext`.
- The published adventure puts them side by side (`sources/adventure-wdh.json:17166`, `:17173`, `:15041`, quoted in A3 and D5).
- No other repo file states a rivalry. `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md` does not mention Noska.

**3. Guild bugbear and goblin ties.** The Guild uses bugbears and goblins as muscle and as watch-post crews. The sources are in A3, A8 and section E. The wiki says so directly:

> "The Xanathar Guild was also known to employ a number of [[goblin]]s and [[bugbear]]s, some of whom were infected with [[intellect devourer]]s, presumably by Nihiloor.<ref name="WDotMM-p13">{{Cite book/Waterdeep: Dungeon of the Mad Mage|13}}</ref>"
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:106` (cites *Dungeon of the Mad Mage* p.13, key "WDotMM-p13"; the wiki line prints no edition)

---

## A. Background facts by theme

### A1. Origin, family, birth and early life

No source gives any of these. The wiki's lead line says who he was and gives no origin.

> "'''Noska Ur'gray''' was an enforcer of the [[Xanathar's Thieves' Guild]] in [[Waterdeep]] during the early 1490s [[DR]].<ref name="WDH5e-p213" />"
> — `wiki-xg/Noska_Ur_gray.txt:62` [`wiki.txt:1707`] (citation key WDH5e-p213 = *Waterdeep: Dragon Heist*, 5e, p.213)

Campaign and adventure: none. See F1.

### A2. The lost hand and the crossbow arm

**Adventure (5e), the origin of the injury and the arm**
> "Noska is a ruthless enforcer in the Xanathar Guild. A green slime in Undermountain dissolved his left hand and forearm, and the lost appendage has been replaced with a heavy crossbow that attaches to the stump."
> — `sources/adventure-wdh.json:32417` (Appendix B entry "Noska Ur'gray", page 213, header at `:32404`)

**Wiki, same injury (5e key), without the place**
> "Once Noska lost his left hand and forearm to a [[green slime]]'s attack. He replaced the missing part with a heavy crossbow attached to the stump.<ref name="WDH5e-p213" />"
> — `wiki-xg/Noska_Ur_gray.txt:68` [`wiki.txt:1713`]

**Campaign, the page (wording differs; see D2)**
> "**Persona.** To the world, Noska is a ruthless enforcer with a heavy crossbow replacing his left forearm (lost to a green slime in Undermountain)."
> — `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:21`

**Campaign, the Guild page**: no injury line. Its only Noska entry is at `campaign/setting/organizations/08-xanathars-guild.md:104` (quoted in A4).

No source dates the injury. The adventure gives only "in Undermountain". See F2.

### A3. Rank, role and standing in the Guild

**Campaign, the Structure paragraph of the Guild page**
> "Xanathar rules the Guild from a lair below Skullport, and very few members have access to it (*Dragon Heist*, 5e). Its lieutenants manage the Guild's day-to-day operations (*Dragon Heist*, 5e). Ahmaergo, a shield dwarf, is the most influential member after the beholder, and Nar'l Xibrindas is its only advisor. Nihiloor has carved out a lair of its own inside the beholder's lair, Noska Ur'gray is the chief enforcer and Thorvin Twinbeard is the chief engineer and trapsmith. Ott Steeltoes keeps Sylgar, and Gorath and Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)."
> — `campaign/setting/organizations/08-xanathars-guild.md:43`

**Campaign, the Guild's response ladder**
> "**First Team — Gorath's Team.** Gorath leads four **duergar**. He is sent when someone needs to be taught a lesson."
> "**Second Team — Korgstrod's Team.** Korgstrod Uxgulm leads three **duergar**, a **half-ogre**, and a **gazer**. The half-ogre carries the *Orb Confectioners' Note*: the passphrase to the sewer hideout ("Eight small eyes." / "Around an ocular cake.")."
> "**Third Team — Noska's Team.** Noska Ur'gray leads six **bugbears** and a **gazer**. He is sent when Xanathar is done sending messages and wants the problem gone."
> — `campaign/guides/factions/09-xanathars-guild.md:9`, `:11`, `:13`

**Adventure, the "important underlings" list**
> "{@creature Xanathar|WDH} relies on underlings for advice, information, and day-to-day oversight of the Xanathar Guild. The following important underlings are described in appendix B:"
> — `sources/adventure-wdh.json:15066` (inset "Important Underlings", page 100, under "Sow Mistrust" at `:15056`)
> "{@creature Noska Ur'gray|wdh}, dwarf enforcer",
> — `sources/adventure-wdh.json:15074`

**Adventure, a standing rule about the two most trusted underlings**
> "Killing one of {@creature Xanathar|WDH}'s most trusted underlings, such as {@creature Ahmaergo|WDH} or {@creature Noska Ur'gray|wdh}, throws the day-to-day operation of the guild into chaos for a tenday."
> — `sources/adventure-wdh.json:15041` (page 100, "Assassination")

**Adventure, the lair's enforcer and quarters**
> "{@creature Xanathar|WDH}'s enforcer, {@creature Noska Ur'gray|wdh} (see {@adventure appendix B|WDH|12}), resides in this magically lit room when he's not in the arena ({@area X6|27a}). The room contains the following features:"
> — `sources/adventure-wdh.json:17323` (keyed area X10, "Noska's Quarters", page 105)

**Wiki, the trust line (5e key)**
> "Noska was one of the most trusted underlings of the Xanathar.<ref name="WDH5e-p66-100">{{Cite book/Waterdeep: Dragon Heist|100}}</ref>"
> — `wiki-xg/Noska_Ur_gray.txt:73` [`wiki.txt:1718`]

**Wiki, appointment by 1492 DR (the Guild section, under the heading "By {{Yearlink|1492}}" at bundle line 159; citation key WDH-p100, no edition printed; 5e inferred from the key family)**
> "By this time, Zushaxx had also appointed [[Thorvin Twinbeard]], a Harper informant, [[Nihiloor]], a mind flayer, and [[Noska Ur'gray]] to important positions. It had also come to own [[Sylgar]], a goldfish.<ref name="WDH-p100"/>" (rest of the passage covers: Ott Steeltoes's change of role to Sylgar's keeper, and the fish's secret replacements)
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:161`

- The wiki names the beholder "Zushaxx" in the Guild section. The campaign page explains the naming: "Design: the campaign has Zushaxx believe that it is the original Xanathar (**Xanathar** in Villains; **The Long Shadow**)." (`campaign/setting/organizations/08-xanathars-guild.md:21`)

**Wiki, the Guild's "chief enforcer" and the arena (5e keys)**
> "Noska was the chief enforcer for the [[Xanathar]]. He lived inside the [[beholder]]'s lair.<ref name="WDH5e-p104-105">{{Cite book/Waterdeep: Dragon Heist|104-106}}</ref> During the gladiator tournaments organized by his master, Noska managed the fighters.<ref name="WDH5e-p114">{{Cite book/Waterdeep: Dragon Heist|114}}</ref>"
> — `wiki-xg/Noska_Ur_gray.txt:65` [`wiki.txt:1710`]

**Adventure, the arena role (5e)**
> "If {@creature Xanathar|WDH} is present, it hovers in the southeast alcove and uses its {@item ring of invisibility} to remain unseen. Standing on the steps of the alcove are two dwarves: {@creature Xanathar|WDH}'s majordomo, {@creature Ahmaergo|WDH} (see {@adventure appendix B|WDH|12}), who presides over fight tournaments, and {@creature Xanathar|WDH}'s chief enforcer, {@creature Noska Ur'gray|wdh} (see {@adventure appendix B|WDH|12}), who releases arena combatants from {@area X7|27e}. Ten human {@creature bandit||bandits} and five {@creature bugbear||bugbears} (all members of the Xanathar Guild) guzzle ale and heckle combatants from the bleachers, while two {@creature goblin||goblins} serve up salted rat intestines and stirge meat pies."
> — `sources/adventure-wdh.json:17166` (keyed area X6, "Pit of Blood and Fortune", header at `:17150`)
> "{@creature Noska Ur'gray|wdh} takes the twelve combatants and assembles them in four teams of three. To keep the fights interesting, Noska tries to even out the teams as much as possible. A team might have all player characters, all NPCs, or a combination of the two."
> — `sources/adventure-wdh.json:18209` (page 114, "Tournament Structure")
> "If the characters let the fight play out, Noska escorts the victor back to {@area X7|27e} while {@creature Ahmaergo|WDH} goads characters into joining the tournament."
> — `sources/adventure-wdh.json:17173` (page 104, "Joining a Tournament")

**Adventure, the cell keys (5e)**
> "This area contains four cells separated by bars. The rectangular iron doors have locks built into them, and {@creature Noska Ur'gray|wdh} carries the keys. Picking a lock requires a successful {@dc 15} Dexterity check using thieves' tools. Breaking down a cell door requires a successful {@dc 25} Strength (Athletics) check. The Cell Occupants table lists this area's prisoners."
> — `sources/adventure-wdh.json:17203` (keyed area X7, "Cell Block", page 104)

**Adventure, the off-arena room (5e)**
> "If he's not with {@creature Xanathar|WDH} in the arena ({@area X6|27a}), {@creature Noska Ur'gray|wdh} (see {@adventure appendix B|WDH|12}) is here, drinking with the others."
> — `sources/adventure-wdh.json:17898` (keyed area X28, "Guild Recreation Hall", header at `:17889`)

**Alexandrian, the Lair roster, private fight (printed p.89 [PDF p.7]; image transcription)**
> "Xanathar (invisible in southeast alcove)" / "Ahmaergo" / "Noska Ur'gray" / "10 bandits + 5 bugbears as an audience" / "2 goblins serving salted rat intestines and stirge meat pies" / "1d4 random combatants from Area X7"
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.89 [PDF p.7] (the standard roster on the same page lists "Noska Ur'gray (01-25%) + Prisoners", "Noska Ur'gray (25-50%) + Rust Monster" and "Area X10 – Noska's Quarters"; the table rows are quoted as printed, not as aligned in the render)

**Alexandrian, the tournament roster (printed p.90 [PDF p.8]; image transcription)**
> "Noska Ur'gray + Prisoners" / "Noska's Rust Monster" / "Area X10 – Noska's Quarters"
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.90 [PDF p.8]

**Alexandrian, other Lair pages**: the printed p.84, p.85, p.88 and p.91 pages do not name Noska in any room text. The printed p.91 gives only the stat reference (A5 and B).

### A4. Connections (named figures)

**Ahmaergo (see D5 for the rivalry check)**
> "{@creature Ahmaergo|WDH}, dwarf majordomo" (`sources/adventure-wdh.json:15071`); the arena pairing at `:17166` and `:17173` (quoted in A3).
> "Ahmaergo handles logistics: gladiatorial procurement, outpost resupply, discipline. Most orders that bear Xanathar's name are written by Ahmaergo."
> — `campaign/setting/organizations/08-xanathars-guild.md:101`
> "**Relationships.** Ahmaergo is Xanathar's majordomo (most orders that bear Xanathar's name were written by Ahmaergo), the Guild's de facto second-in-command, and a shield dwarf whose minotaur obsession fills every corner of his quarters."
> — `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:25`
> "The lair holds a gladiatorial arena, the Pit of Blood and Fortune, where Ahmaergo presides over the tournaments and Noska releases the combatants (*Dragon Heist*, 5e)." — `campaign/setting/organizations/08-xanathars-guild.md:47` (the paragraph begins "**The lair.** The lair is an ancient dungeon complex built by Netherese wizards and expanded by beholders over time."; rest of the passage covers the 300-foot tunnel to Skullport, the staircase to the Castle Ward sewers, and the panopticus dwarves)

**Gorath and Korgstrod (the response ladder)**
> "**Fear.** Xanathar charms and bullies its minions and puts its symbol on doors, tattoos and chalk marks so that no one forgets whose ground they stand on (*Dragon Heist*, 5e; **Dock Ward**). The Guild warns before it kills. Gorath delivers a message once and leaves, and Noska is sent when Xanathar is done sending messages (**Gorath**; **Noska Ur'gray**)."
> — `campaign/setting/organizations/08-xanathars-guild.md:77`
> "- **Noska Ur'gray** (DH p. 213) — Shield dwarf enforcer, neutral evil. Xanathar's heaviest enforcer. See the **Noska Ur'gray** page in Notable Figures."
> — `campaign/setting/organizations/08-xanathars-guild.md:104` (the bundle copy at `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:662` reads differently; see E1)

**Nar'l Xibrindas (quest-time succession; not day-one)**
> "If {@creature Xanathar|WDH} is the main villain, {@creature Noska Ur'gray|wdh} (see {@adventure appendix B|WDH|12}) arrives with six {@creature bugbear||bugbears} and a {@creature gazer|VGM} (see {@adventure appendix B|WDH|12}). If Noska is dead or otherwise indisposed, the beholder replaces him with {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) and his {@creature grell} bodyguard."
> — `sources/adventure-wdh.json:14780` (vault-exit ambush, a Dragon Heist encounter; see C)

**Grinda Garloth (quest-time; not day-one)**
> "{@creature Xanathar|WDH} has sent forces to collect the {@item Stone of Golorr|WDH} from {@creature Grinda Garloth|WDH}, known up and down the wharf as an eccentric wizard who owns a submersible contraption that she uses to hunt for treasure on the bottom of Deepwater Harbor. The characters have no trouble getting directions to her Mistshore residence ({@area D2|15a})."
> — `sources/adventure-wdh.json:7528` (Mistshore: Spring, page 66, header at `:7525`)
> "When the characters arrive at her home, Grinda is holed up inside, having barricaded the doors with furniture. Trying to break down the doors are four members of the Xanathar Guild (CE male human {@creature bandit||bandits}) under the command of a dwarf enforcer named {@creature Noska Ur'gray|wdh} (see {@adventure appendix B|WDH|12}). A {@creature merrow} also under Noska's command swims beneath the docks. It surfaces to attack when the characters arrive."
> — `sources/adventure-wdh.json:7529`
> "Grinda admits that she has done business with the Xanathar Guild in the past. Her orders were to protect the stone until Noska arrived to claim it, but she changed her mind and decided to keep the stone for herself. She now realizes that decision was a mistake."
> — `sources/adventure-wdh.json:7538` (page 67, "Where's the Stone?", header at `:7534`)
> "In [[1492 DR]],{{WDH-time}} if the [[Xanathar]] managed to obtain the ''[[Stone of Golorr]]'', he entrusted the Stone to [[Grinda Garloth]].<ref name="WDH5e-p57">{{Cite book/Waterdeep: Dragon Heist|57}}</ref>"
> — `wiki-xg/Noska_Ur_gray.txt:70` [`wiki.txt:1715`] (a conditional in the wiki; conflicts with the campaign, see D11)

**Thorvin Twinbeard, Nihiloor, Nar'l and Ott**: no Noska line on those pages (see E6).

### A5. Stats in the sources

**Adventure, Game Statistics (5e; page 213)**
> "{@creature Noska Ur'gray|wdh} is a shield dwarf {@creature thug}, with these changes:"
> "Noska is neutral evil."
> "He has these racial traits: His walking speed is 25 feet. He has advantage on saving throws against poison and resistance to poison damage. He has darkvision out to a range of 60 feet. He speaks Common and Dwarvish."
> "He has disadvantage on Strength checks made to climb, due to his disability."
> — `sources/adventure-wdh.json:32424`, `:32428`, `:32429`, `:32430` (the index line is `"79. Noska Ur'gray",` at `sources/adventure-wdh.json:32978`)

**Alexandrian, the stat reference (printed p.91 [PDF p.9]; image transcription)**
> "Noska Ur'gray – shield dwarf thug, MM p. 350 (DH p. 213)"
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91 [PDF p.9]

**Alexandrian, the response team (printed p.54 [PDF p.6]; image transcription)**
> "NOSKA UR'GRAY: Noska, a shield dwarf, is another of Xanathar's enforcers."
> "Noska Ur'gray (DH p. 213)" / "6 bugbears (MM p. 33)" / "gazer (DH p. 203)"
> — `sources/6. Faction Response Teams.pdf`, printed p.54 [PDF p.6]

**Wiki infobox (5e)**: `alignment5e = [[Neutral evil]]` (`wiki-xg/Noska_Ur_gray.txt:57` [`wiki.txt:1702`]); `class5e = [[Thug]]` (`:59` [`:1704`]); `race = [[Dwarf]]` (`:14` [`:1659`]); `ethnicity = [[Shield dwarf]]` (`:15` [`:1660`]); `occupation = Enforcer` (`:16` [`:1661`]); `sex = Male` (`:13` [`:1658`]); `home = [[Waterdeep]], [[Sword Coast North]]` (`:11` [`:1656`]); `languages = [[Common]], [[Dwarvish]]` (`:19` [`:1664`]). The infobox cites `WDH5e-p213` for the occupation and the stat block.

### A6. Faith

No source gives Noska a deity. The pass 2 note says the same of the notable figures:
> "The other shield-dwarf and dwarf notable figures (Harug Shieldsunder, Ulkoria Stonemarrow, Noska Urgray, Thorvin Twinbeard, Ahmaergo) name no god in their files."
> — `docs/plans/setting-compendium-research-notes/pass2/batch-k1-moradin-yondalla-maglubiyet.md:353`

The wiki infobox has `patron deity   = ` blank (`wiki-xg/Noska_Ur_gray.txt:18` [`wiki.txt:1663`]). See F12.

### A7. Signature belongings and daily life (adventure, 5e)

**His quarters and pets**
> "Noska keeps the rust monster as a pet and feeds it items from the piles of discarded helms, {@item shield|PHB|shields}, and armaments. He uses the mannequins for target practice. The bathtub, which he has converted into a bed, is padded with straw and mangy furs."
> — `sources/adventure-wdh.json:17331` (keyed area X10, page 105)
> "A marble bathtub with clawed feet rests in the middle of the room, next to a large wooden cage containing a {@creature rust monster}. Along the walls are piles of broken and rusted helmets, {@item shield|PHB|shields}, and weapons."
> — `sources/adventure-wdh.json:17327`
> "Hanging from hooks on the back wall are three mannequins made of straw and canvas, with a multitude of crossbow bolts sticking in them."
> — `sources/adventure-wdh.json:17328`
> "Hidden under a pile of rusty weapons is a wooden chest containing Noska's personal hoard: 37 gp, 151 sp, 360 cp, and four bloodstones (worth 50 gp each)."
> — `sources/adventure-wdh.json:17347` (Treasure, page 105)

### A8. Bugbears and goblins in the Guild (for the bugbear ties)

**Adventure, the bugbear and goblin forces (5e)**
> "{@creature Xanathar|WDH} sends either five {@creature goblin||goblins} dressed up as children wearing Trolltide masks and a {@creature bugbear} ({@chance 70|70 percent chance}), or four {@creature wererat||wererats} in human form ({@chance 30|30 percent chance})."
> — `sources/adventure-wdh.json:13476` (the vault key search, a Dragon Heist encounter)
> "Ten human {@creature bandit||bandits} and five {@creature bugbear||bugbears} (all members of the Xanathar Guild) guzzle ale and heckle combatants from the bleachers, while two {@creature goblin||goblins} serve up salted rat intestines and stirge meat pies."
> — `sources/adventure-wdh.json:17166` (X6 arena)
> "Ten human {@creature bandit||bandits} (members of the Xanathar Guild) sit around two trellis tables, drinking Wyrmwizz Ale, smoking pipes, clapping their hands, and stomping their feet while two {@creature goblin||goblins} wearing chamber pots on their heads dance and sing atop a third table."
> — `sources/adventure-wdh.json:17896` (X28)

**Wiki, the bodyguard practice (the Guild's support, not Noska-specific)**
> "Any member given an assignment would receive a bodyguard or assistant, such as a [[bugbear]], [[wererat]], [[kenku]], or [[gazer]], with secret instructions to spy on and assassinate the agent in case of failure."
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:98` (cites *Dragon Heist* p.17, key "WDH-p17"; 5e inferred from the key family)

**Campaign, the Guild's composition**
> "The Guild is made up of some of Waterdeep's most disreputable folk and of monsters, whom the beholder forces into service or draws in with treasure, food or power (*Dragon Heist*, 5e). Goblins and bugbears work for it, and Nihiloor has infected some of them with intellect devourers (Forgotten Realms Wiki, *Xanathar's Thieves' Guild*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:45`

**Campaign, watch posts in Undermountain**
> "The Guild keeps watch posts on the upper levels of Undermountain, staffed by bugbears and goblins, to stop adventurers reaching the lower levels (WDMM)."
> — `campaign/setting/history/02-the-long-shadow.md:64`
> "Nine bugbears (five of them under the control of intellect devourers) represent the Xanathar Guild on this level. They're charged with keeping adventurers from reaching the lower levels and thereby interfering with guild business. With the help of several goblins, the bugbears have set up guild watch posts in {@area areas 23|08b|x}, {@area 28|0a4}, and {@area 39|0cd}."
> — `sources/adventure-wdmm.json:795` (Undermountain level 1; `campaign/setting/deities/maglubiyet.md:84` summarises it)

**Campaign, Three Nights (quest-time; see D6)**
> "The attacks are the Guild's own. The bugbears are ordinary Guild muscle. Some of the four Dungsweepers carry intellect devourers from Nihiloor's stock. The Beholder Zombie is one of the lair's guard creatures. Ott knows the Guild's ways and tells the party what is coming when asked."
> — `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:23`
> "Six bugbears set out from the docks before midnight with a hired mule and cart. They reach the alley as the shrine bell strikes twelve. The courtyard gate opens onto the kitchen, and the cellar door is in the kitchen corridor beyond it, so the courtyard group is the one that threatens Ott. The front door group only has to hold the taproom."
> — `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:171`

---

## B. Alignment, species, pronouns, stat block

**Alignment: neutral evil (consistent)**
- Campaign, current page: "*Shield dwarf enforcer, neutral evil, he/him*. Stat block: **Thug (with modifications)**." — `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:5`
- Campaign, Guild page: "- **Noska Ur'gray** (DH p. 213) — Shield dwarf enforcer, neutral evil. Xanathar's heaviest enforcer. See the **Noska Ur'gray** page in Notable Figures." — `campaign/setting/organizations/08-xanathars-guild.md:104`
- Adventure: "Noska is neutral evil." — `sources/adventure-wdh.json:32428`
- Wiki: "| alignment5e    = [[Neutral evil]]" — `wiki-xg/Noska_Ur_gray.txt:57` [`wiki.txt:1702`]

**Species: dwarf, shield dwarf (consistent)**
- Campaign: "Shield dwarf enforcer" (`campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:5`); "Noska is a shield dwarf, not a goblinoid" (`campaign/setting/deities/maglubiyet.md:82`, citing the page at `:25`)
- Adventure: "is a shield dwarf {@creature thug}, with these changes:" (`sources/adventure-wdh.json:32424`); "under the command of a dwarf enforcer named {@creature Noska Ur'gray|wdh} (see {@adventure appendix B|WDH|12})" (`sources/adventure-wdh.json:7529`)
- Alexandrian, response team: "NOSKA UR'GRAY: Noska, a shield dwarf, is another of Xanathar's enforcers." (printed p.54 [PDF p.6])
- Wiki: "| race           = [[Dwarf]]" (`wiki-xg/Noska_Ur_gray.txt:14` [`wiki.txt:1659`]); "| ethnicity      = [[Shield dwarf]]" (`:15` [`:1660`])

**Pronouns: he/him (sourced)**
- Campaign, current page: "he/him" (`campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:5`)
- Adventure: "A green slime in Undermountain dissolved his left hand and forearm" (`sources/adventure-wdh.json:32417`); "He uses the mannequins for target practice." (`:17331`)
- Wiki: "| sex            = Male" (`wiki-xg/Noska_Ur_gray.txt:13` [`wiki.txt:1658`])

**Stat block label**
- Campaign, current page: "Stat block: **Thug (with modifications)**." (`campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:5`)
- Campaign, Ahmaergo's page (same label): "- *Shield dwarf majordomo, lawful evil, he/him*. Stat block: **Thug (with modifications)**." (`campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:5`)
- Adventure: "is a shield dwarf {@creature thug}, with these changes:" (`sources/adventure-wdh.json:32424`)
- Alexandrian: "Noska Ur'gray – shield dwarf thug, MM p. 350 (DH p. 213)" (printed p.91 [PDF p.9])
- Wiki: "| class5e        = [[Thug]]" (`wiki-xg/Noska_Ur_gray.txt:59` [`wiki.txt:1704`])
- The 2024 status of the label is in dispute. See D1.

**Ability and racial traits (adventure, 5e)**: "He has these racial traits: His walking speed is 25 feet. He has advantage on saving throws against poison and resistance to poison damage. He has darkvision out to a range of 60 feet. He speaks Common and Dwarvish." (`sources/adventure-wdh.json:32429`). "He has disadvantage on Strength checks made to climb, due to his disability." (`:32430`).

**Index entry**: `"79. Noska Ur'gray",` (`sources/adventure-wdh.json:32978`). The entry heading is `"name": "Noska Ur'gray",` with `"page": 213,` (`:32404`-`:32405`).

**Voice profile, the figure's header** (`.claude/skills/character-voices/voices/xanathars-guild.md:83`-`:84`):
> "### Noska Ur'gray"
> "*A crossbow-armed dwarf enforcer whose inner life, and vocabulary, are exactly as simple as they look.*"

---

## C. Every sentence on the current page

Current page: `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md`. "Day-one OK" means no quest gate is needed. "Standing" means a Factions Guide mechanic, which the page may state as a day-one fact. "Quest-time" means the sentence narrates a deployment, capture, rescue or other quest event.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Shield dwarf enforcer, neutral evil, he/him*. Stat block: **Thug (with modifications)**." | Day-one. The stat label is in dispute (D1) | `adventure-wdh.json:32424`, `:32428`; `organizations/08-xanathars-guild.md:104`; `wiki.txt:1702`, `:1704` |
| 2 | L6 | "**Affiliation:** Xanathar's Guild" | Day-one OK | `organizations/08-xanathars-guild.md:1` (H1), `:104` |
| 3 | L7 | "**Featured in:** **Xanathar's Lair**" | Quest reference, Summary scaffolding. The page omits the quests that name Noska (E7) | `campaign/structure/arc-f-xanathars-lair.md:184`, `:196`, `:198`, `:339` |
| 4 | L11 | "**Resonance.** Noska should inspire intimidation with his crossbow-arm and brutal reputation, dark amusement with his rust monster pet and mannequin target practice, and reluctant respect for the straightforward violence that makes him exactly what he advertises." | Day-one OK. "brutal reputation" has no source beyond the page's own voice | crossbow-arm: `adventure-wdh.json:32417`; rust monster and mannequins: `:17327`, `:17331` |
| 5 | L13 | "**Emotions.** Noska most often feels aggressive boredom, brute satisfaction in violence, simple loyalty to Xanathar, territorial possessiveness, flat disdain for weakness, and occasional contentment when feeding discarded weapons to his rust monster." | Day-one OK. The feeding line is sourced; the emotions are the page's own | `adventure-wdh.json:17331` ("feeds it items from the piles of discarded helms, shields, and armaments") |
| 6 | L15 | "**Motivations.** Noska wants to hurt people Xanathar tells him to hurt, maintain his position as the Guild's heaviest response option, and feed his rust monster." | Day-one OK except "heaviest response option", which has no current source (D7) | "heaviest enforcer": `organizations/08-xanathars-guild.md:104`; the stale phrase: `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:662` (E1) |
| 7 | L17 | "**Inspirations.** When playing Noska, channel Drax (*Guardians of the Galaxy*), Mountain (*Game of Thrones*), and Bane (*The Dark Knight Rises*)." | Not a fact. `campaign/setting/deities/bane.md:140` notes the Bane line | n/a |
| 8 | L21 (a) | "**Persona.** To the world, Noska is a ruthless enforcer with a heavy crossbow replacing his left forearm (lost to a green slime in Undermountain)." | Day-one. "left forearm" differs from "left hand and forearm" (D2) | `adventure-wdh.json:32417`; `wiki.txt:1713` |
| 9 | L21 (b) | "To those in the Guild, he is sent when Xanathar is done sending messages and wants the problem gone." | Standing (Factions Guide). The deployment against the party is quest-time | `campaign/guides/factions/09-xanathars-guild.md:13`; `campaign/setting/organizations/08-xanathars-guild.md:77` |
| 10 | L21 (c) | "Deep down, he keeps a rust monster as a pet and uses mannequins for target practice." | Day-one OK | `adventure-wdh.json:17331` |
| 11 | L21 (d) | "He sleeps in a converted bathtub padded with straw and furs." | Day-one OK ("mangy furs" in the source) | `adventure-wdh.json:17331` |
| 12 | L21 (e) | "His inner life is exactly as simple as it appears." | Voice, not a fact | n/a |
| 13 | L23 (a) | "In a fight, Noska fires his crossbow-arm from range and closes to melee without hesitation." | Day-one OK as a habit. "closes to melee" has no source. The crossbow's use in the Grinda scene is quest-time (`adventure-wdh.json:7530`) | the crossbow itself: `:32417` |
| 14 | L23 (b) | "He has disadvantage on climbing due to his missing hand but compensates by never needing to be anywhere subtle." | Day-one. "due to his missing hand" differs from "due to his disability" (D3). "never needing to be anywhere subtle" has no source | `adventure-wdh.json:32430` |
| 15 | L25 | "**Relationships.** Noska is an enforcer of Xanathar's Guild, the third response team leader, and a shield dwarf whose crossbow-arm, rust monster pet, and bathtub bed constitute a complete portrait of his priorities." | "third response team leader" is standing. "shield dwarf" is day-one | `campaign/guides/factions/09-xanathars-guild.md:13`; `adventure-wdh.json:32424` |
| 16 | L29 | "Noska Ur'gray is an enforcer of Xanathar's Guild, recognizable by the heavy crossbow that replaces his left forearm." | Day-one. "left forearm" (D2) | `adventure-wdh.json:32417` |
| 17 | L29 | "He is direct, uncomplicated, and reliably present whenever the Guild needs a problem solved by violence." | Voice. "reliably present" rests only on the response-team role | `campaign/guides/factions/09-xanathars-guild.md:13` |

**Quest-time facts that the page does not state, and where each lives.** None of these is on the page now. They are listed so the drafter does not add them.
- The Mistshore raid on Grinda Garloth: `sources/adventure-wdh.json:7528`-`:7538`. No campaign quest file routes it. Only `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:23` refers to it (E4).
- The vault-exit ambush by Noska and six bugbears: `sources/adventure-wdh.json:14780`. A Dragon Heist vault encounter. No campaign file routes it (the Vault of Dragons journal is pending conversion).
- The Lair's Stage 2 and Stage 3 responses: `campaign/structure/arc-f-xanathars-lair.md:196` ("Noska and rust monster respond to the sector") and `:198` ("a named NPC (Ahmaergo, Nar'l, Noska) confirms combat with intruders").
- The Doom Raiders, Lords' Alliance, Bregan D'aerthe and Harpers quest uses: see E7.

**Voice profile quest-time clauses.** The profile (`.claude/skills/character-voices/voices/xanathars-guild.md:86`-`:97`) has none. Its lines are day-one. Its "Never" line reads: "He never negotiates, never thinks twice, and never disobeys the Xanathar." It uses "the Xanathar", which ruling 9 forbids in narration (see D8). The "Boss says" speech tags are fine.

---

## D. Conflicts

**D1. Stat block: "Thug (with modifications)" against the 2024 rules**
- Current page, source line: "Stat block: **Thug (with modifications)**." (`campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:5`)
- Adventure (5e): "is a shield dwarf {@creature thug}, with these changes:" (`sources/adventure-wdh.json:32424`)
- Alexandrian (2014 MM reference): "Noska Ur'gray – shield dwarf thug, MM p. 350 (DH p. 213)" (printed p.91 [PDF p.9])
- Lords' Alliance research note, on the 2024 data: "The downloaded 2024 data has **no Veteran and no Thug**; the names are **Warrior Veteran** (CR 3) and **Tough** (CR 1/2). The Noska and Ahmaergo pages repeat "Thug (with modifications)" (`noska:6`, `ahmaergo:6`)." (`docs/plans/lords-alliance-research/04-m04-m06.md:28`)
- Lords' Alliance m05 design note: "The old Thug and Bandit escort becomes a **Tough Boss** with **Tough** fighters at each party size." (`campaign/quests/faction-events/lords-alliance/m05-fentrees-ledger/design-notes.md:13`)
- Not verified here: a grep of `sources/5etools` for entries named Thug, Tough or Warrior Veteran returned no match, so the 2024 claim is unconfirmed from this session.
- Higher source: the adventure and the page agree on "thug". The campaign rules are 2024 (CLAUDE.md), and the research note and the design note say "Tough" is the 2024 name. The orchestrator decides.

**D2. The injured arm: "left forearm" against "left hand and forearm"**
- Current page: "a heavy crossbow replacing his left forearm" (`campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:21`, `:29`)
- Adventure: "A green slime in Undermountain dissolved his left hand and forearm" (`sources/adventure-wdh.json:32417`)
- Wiki: "Once Noska lost his left hand and forearm to a [[green slime]]'s attack." (`wiki-xg/Noska_Ur_gray.txt:68` [`wiki.txt:1713`])
- Higher source: the adventure. Minor wording.

**D3. Climbing: "missing hand" against "disability"**
- Current page: "He has disadvantage on climbing due to his missing hand" (`campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:23`)
- Adventure: "He has disadvantage on Strength checks made to climb, due to his disability." (`sources/adventure-wdh.json:32430`)
- Higher source: the adventure. Minor.

**D4. Off-arena quarters: X8 against X10 and X28**
- Campaign structure doc: "Noska Ur'gray is in X8 during non-tournament periods, in X6 arena-side during games; responds to alarms with rust monster companion." (`campaign/structure/arc-f-xanathars-lair.md:184`)
- Adventure, X10: "resides in this magically lit room when he's not in the arena ({@area X6|27a})." (`sources/adventure-wdh.json:17323`)
- Adventure, X28: "If he's not with {@creature Xanathar|WDH} in the arena ({@area X6|27a}), {@creature Noska Ur'gray|wdh} (see {@adventure appendix B|WDH|12}) is here, drinking with the others." (`:17898`)
- Alexandrian roster, printed p.89 [PDF p.7]: "Area X10 – Noska's Quarters" (image transcription)
- Note: `arc-f:184` is a campaign file, and under the brief's rank it outranks the adventure. The Lair journal is not yet written. The adventure's X8 is the "Hall of Statues" (`sources/adventure-wdh.json:17238`, header "X8. Hall of Statues"), and no Noska text sits in it. The orchestrator decides. The Noska page should not name a room.

**D5. The Noska–Ahmaergo relationship: rivalry against working partnership**
- Rivalry, campaign quest intelligence: "The Noska–Ahmaergo rivalry has reached near-blows twice in the past month; during an active tournament, Noska is arena-side and Ahmaergo is in his quarters reviewing fight records, neither monitoring the other's territory. That window is real and exploitable." (`campaign/structure/arc-f-xanathars-lair.md:41`)
- Rivalry, source guide: "Noska vs. Ahmaergo rivalry" (`sources/SOURCE_GUIDE.md:343`), listed under the Lair PDF (`:335`)
- Partnership, adventure: "Standing on the steps of the alcove are two dwarves: {@creature Xanathar|WDH}'s majordomo, {@creature Ahmaergo|WDH} (see {@adventure appendix B|WDH|12}), who presides over fight tournaments, and {@creature Xanathar|WDH}'s chief enforcer, {@creature Noska Ur'gray|wdh} (see {@adventure appendix B|WDH|12}), who releases arena combatants from {@area X7|27e}." (`sources/adventure-wdh.json:17166`)
- Partnership, adventure: "Killing one of {@creature Xanathar|WDH}'s most trusted underlings, such as {@creature Ahmaergo|WDH} or {@creature Noska Ur'gray|wdh}, throws the day-to-day operation of the guild into chaos for a tenday." (`sources/adventure-wdh.json:15041`)
- Partnership, Alexandrian: the printed p.89 "A PRIVATE FIGHT" list names "Ahmaergo" and "Noska Ur'gray" together (printed p.89 [PDF p.7])
- Partnership, Harpers quest letter: "Ahmaergo and Noska Ur'gray run the Dock Ward routes, and the restricted deliveries all went to Nihiloor's rooms in the lair. I kept the labels with my account, so give them to Mirt before you go below." (`campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-02-the-extraction.md:150`)
- Ahmaergo's page: "**Relationships.** Ahmaergo is Xanathar's majordomo (most orders that bear Xanathar's name were written by Ahmaergo), the Guild's de facto second-in-command, and a shield dwarf whose minotaur obsession fills every corner of his quarters." (`campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:25`), with no Noska line.
- Higher source: the campaign files outrank the adventure, so `arc-f:41` would rank first. But it is quest intelligence about a Doom Raiders reward, and no day-one file states the rivalry. The Lair PDF, which `SOURCE_GUIDE.md:343` cites, was read in full and contains no rivalry text. The orchestrator decides.

**D6. Who the Three Nights bugbears are**
- Setting page: "In **Three Nights**, the Guild's bugbears come for Ott Steeltoes on the first night (`campaign/quests/faction-events/bregan-daerthe/m03-three-nights/overview.md:31`)" (`campaign/setting/deities/maglubiyet.md:82`), and "the bugbear response team's leader and the fishkeeper the bugbears hunt in **Three Nights**" (`:121`). The link implies Noska's team is the Three Nights gang.
- Three Nights, the quest file: "The bugbears are ordinary Guild muscle." (`campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:23`); "Six bugbears set out from the docks before midnight with a hired mule and cart." (`:171`); "A Guild Bugbear Warrior (Chaotic Evil, Bugbear, he/him) :: a hired Guild bruiser paid by the day to carry a dwarf out of a cellar, who now wants only to leave." (`:236`)
- Three Nights, the overview: "At midnight the Guild's bugbears come for Ott through the front door and the courtyard gate." (`overview.md:31`). A search of the m03 folder for "Noska" and "Ur'gray" returned no match.
- Higher source: the quest journal. Three Nights is a Bregan D'aerthe mission, and the setting page must not carry it. The page should say nothing about Three Nights.

**D7. "Heaviest"**
- Current page: "maintain his position as the Guild's heaviest response option" (`campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:15`)
- Current Guild page: "Xanathar's heaviest enforcer." (`campaign/setting/organizations/08-xanathars-guild.md:104`)
- Stale bundle copy: "Xanathar's heaviest response option. Leads the third response team when earlier escalations fail." (`sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:662`, a copy of an older `08-xanathars-guild.md` line 24)
- No source uses "heaviest response option". The current page's wording matches the stale bundle copy, not the current organization page.

**D8. Vocabulary: "the Xanathar"**
- Voice profile: "He never negotiates, never thinks twice, and never disobeys the Xanathar." (`.claude/skills/character-voices/voices/xanathars-guild.md:93`)
- Ruling 9 (`docs/plans/setting-compendium-pass6-brief.md:43`): "Xanathar is 'it' in narration, never in a figure's speech tag." The profile line is narration, not speech. Flag for the drafter.

**D9. Gazer source: "gazer (DH p. 203)" against "gazer|VGM"**
- Alexandrian, response team: "gazer (DH p. 203)" (printed p.54 [PDF p.6])
- Adventure: "a {@creature gazer|VGM} (see {@adventure appendix B|WDH|12})" (`sources/adventure-wdh.json:14780`)
- Minor. The Factions Guide says only "a **gazer**" (`campaign/guides/factions/09-xanathars-guild.md:13`).

**D10. Ahmaergo's species (affects the Noska pairing)**
- Alexandrian, Appendix C random encounter: "1d4 roll: 1 = Flutterfoot Zipswiggle (goblin; skittish, can be bribed with food), 2 = Ahmaergo (duergar; inspection; DC 15 Deception to pass as authorized), 3 = Nar'l Xibrindas + grell bodyguard, 4 = Ott Steeltoes." (`sources/Appendix_C_-_Player_Faction_Missions.md:1887`)
- Adventure: "{@creature Ahmaergo|WDH}, dwarf majordomo" (`sources/adventure-wdh.json:15071`); "{@creature Ahmaergo|WDH}, {@creature Xanathar|WDH}'s majordomo, has a fascination  with minotaurs. Although outwardly civil, the shield  dwarf is as devious and corrupt as the worst devil, yet  also unflinchingly loyal to his beholder master." (`:31696`)
- Ahmaergo's page: "*Shield dwarf majordomo, lawful evil, he/him*." (`campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:5`)
- Higher source: the campaign (shield dwarf). The Appendix C line is outside the rank and does not match.

**D11. The Stone at Grinda's (1492 DR): Grinda holds it against the campaign's Stone-in-the-lair**
- Adventure: "{@creature Xanathar|WDH} has sent forces to collect the {@item Stone of Golorr|WDH} from {@creature Grinda Garloth|WDH}" (`sources/adventure-wdh.json:7528`)
- Wiki, conditional: "In [[1492 DR]],{{WDH-time}} if the [[Xanathar]] managed to obtain the ''[[Stone of Golorr]]'', he entrusted the Stone to [[Grinda Garloth]]." (`wiki-xg/Noska_Ur_gray.txt:70` [`wiki.txt:1715`])
- Campaign, the Guild page's Draft Notes: "- **Settled (ruling 28):** The Stone on Ches 1. The old Operations sentence "Xanathar held the Stone of Golorr until Dalakhar stole it, and it still holds one of the Stone's Eyes" and the sentence "It wants the Stone recovered so that it can take the vault" describe events after campaign start, because Dalakhar steals the Stone on Ches 20 (`running-the-villains.md:19`; `stone-of-golorr-and-the-eyes.md:51`). The page now says the Stone sits in the lair on Ches 1, as `12-house-gralhund.md:92` does, and that the Guild wants to use it to take the vault. The brief's "the Stone stolen" History entry is therefore not written as a theft, and the theft is routed below." (`campaign/setting/organizations/08-xanathars-guild.md:176`)
- Campaign, the Grinda page: "She will help the party if they defended her from Noska." (`campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:23`)
- Higher source: the campaign (Stone in the lair on Ches 1). The Grinda siege is a Dragon Heist event with no routed quest file (F11). The Noska page must not carry it.

---

## E. Stale lines in other files (not edited), and routed references

### E1. Stale copies of the Guild page
- `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:662` (a copy of an older line of `campaign/setting/organizations/08-xanathars-guild.md`, now at `:104`): "- **Noska Ur'gray** (DH p. 213) — Shield dwarf enforcer, neutral evil. Xanathar's heaviest response option. Leads the third response team when earlier escalations fail. See the **Noska Ur'gray** page in Notable Figures." The current `08-xanathars-guild.md:104` reads "- **Noska Ur'gray** (DH p. 213) — Shield dwarf enforcer, neutral evil. Xanathar's heaviest enforcer. See the **Noska Ur'gray** page in Notable Figures." The current file is correct.
- `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:603`-`:610` are copies of the Noska page's lines (`:6`, `:7`, `:13`, `:15`, `:25`, `:29`). They match the current page.

### E2. Setting pages that route quest references (`campaign/setting/`)
- `campaign/setting/deities/maglubiyet.md:82` (a setting page): "> - **The response teams:** **Noska Ur'gray** leads the Guild's third response team, which is six bugbears and a gazer (`campaign/guides/factions/09-xanathars-guild.md:13`). Noska is a shield dwarf, not a goblinoid (`campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:25`). In **Three Nights**, the Guild's bugbears come for Ott Steeltoes on the first night (`campaign/quests/faction-events/bregan-daerthe/m03-three-nights/overview.md:31`)."
- `campaign/setting/deities/maglubiyet.md:121`: quoted in the Answers. Its Three Nights clause is a quest reference on a setting page.
- `campaign/setting/deities/maglubiyet.md:104`: a source-list pointer to this page. Keep.
- `campaign/setting/deities/bane.md:140`: "- Left out: The Noska Urgray line that names Bane (`campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:17`), because it means a film character." Keep. The Inspirations line stays.

### E3. Lair structure document (quest content, rank 1 until conversion)
- `campaign/structure/arc-f-xanathars-lair.md:41`: the rivalry (D5).
- `campaign/structure/arc-f-xanathars-lair.md:184`: "Noska Ur'gray is in X8 during non-tournament periods, in X6 arena-side during games; responds to alarms with rust monster companion." (D4)
- `campaign/structure/arc-f-xanathars-lair.md:190`: "Ahmaergo is in X12 reviewing records. Noska is arena-side." (the tournament configuration)
- `campaign/structure/arc-f-xanathars-lair.md:196`: "**Stage 2 — Sector Alert.** Trigger: Stage 1 response finds armed intruders, or a second alarm fires before the first resolves. Response: Noska and rust monster respond to the sector; all doors in the affected area lock (DC 15 Thieves' Tools); Xanathar is notified and moves to X18 if not already there. Response time: 2d4 minutes from Stage 1." (quest-time)
- `campaign/structure/arc-f-xanathars-lair.md:198`: "**Stage 3 — Full Alert.** Trigger: a named NPC (Ahmaergo, Nar'l, Noska) confirms combat with intruders. Response: all off-duty Guild members in X28 and X8 mobilize; Ahmaergo leads a team toward the reported position; Xanathar retreats to X19 with four Guild Soldiers. Response time: 1d6 minutes from Stage 2." (quest-time)
- `campaign/structure/arc-f-xanathars-lair.md:339`: "- **Notable Figures** — Full NPC profiles for Xanathar, Ahmaergo, Nar'l Xibrindas, Nihiloor, Noska Ur'gray, Ott Steeltoes, Thorvin Twinbeard, Keln Trigos, Grinda Garloth, Korgstrod Uxgulm, Gorath."

### E4. Setting page with quest-time text about Grinda
- `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:23`: "She will help the party if they defended her from Noska." (quest-time, D11)
- `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:25`: "**Relationships.** Grinda Garloth is a black market armorer and salvage wizard at Mistshore, an allied service provider to both Xanathar's Guild and Bregan D'aerthe, the owner of the Apparatus of Kwalish, and an emergency combat support option in the Stone of Golorr investigation if the party defended her home." (the last clause is quest-time)

### E5. Source guide
- `sources/SOURCE_GUIDE.md:343`: the rivalry, attributed to the Lair PDF. The Lair PDF text does not contain it (D5, Answers 2).
- `sources/SOURCE_GUIDE.md:29`: "- **Chapter 5 — Spring Madness (Xanathar):** Full Xanathar's Lair keyed location (36 areas), the gladiatorial tournament approach, Xanathar NPC, Ahmaergo, Noska Ur'gray, Nar'l Xibrindas, Nihiloor, Ott Steeltoes (Sylgar the goldfish keeper), Thorvin Twinbeard (Harper informant). Contains: dream nullifier artifact, panopticus surveillance description, connection tunnels to Undermountain Level 1." (no conflict)

### E6. Other notable-figure pages (no Noska line, except Gorath and Grinda)
A search for "Noska" and "Ur'gray" under `campaign/setting/notable-figures/` finds the Noska page and these:
- `campaign/setting/notable-figures/xanathars-guild/11-gorath.md:25`: "**Relationships.** Gorath is the first response team leader of Xanathar's Guild (four duergar, sent when the Guild wants a lesson taught rather than a person killed), the formal notice that Xanathar knows what the party did, and the first escalation before Korgstrod's team and then Noska's arrive."
- `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:23`: quoted in E4 and D11.
- `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md`: no Noska line. Its Relationships line is quoted in A4.
- The Nar'l, Nihiloor, Ott, Thorvin, Korgstrod and Xanathar pages (`03-narl-xibrindas.md`, `04-nihiloor.md`, `06-ott-steeltoes.md`, `07-thorvin-twinbeard.md`, `10-korgstrod-uxgulm.md`, `01-xanathar.md`): no Noska line.

### E7. Quest files that name Noska (routed; not day-one)
- `campaign/quests/faction-events/lords-alliance/m05-fentrees-ledger/design-notes.md:13`: "Noska Ur'gray no longer bids. His voice profile says he never negotiates, so Ossery Klenn, a Guild negotiator, takes the chair and Hallan Roke leads the bodyguards. The old Thug and Bandit escort becomes a **Tough Boss** with **Tough** fighters at each party size. Rezka's flight is a track and not a pursuit scene."
- `campaign/quests/faction-events/lords-alliance/m05-fentrees-ledger/design-notes.md:33`: "- Noska Ur'gray's Notable Figures page lists this mission, and he no longer appears in it. Dagult Neverember's page lists it too, though he never appears." (STALE: the current Noska page lists no mission.)
- `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:195`: "| Xanathar's Guild | Third | A leader, six large hired fighters and the same floating one-eyed creature, sent when the Guild wants the problem gone | Noska Ur'gray's team |"
- `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:125`: "- **Xanathar's Guild:** Gorath with four duergar, then Korgstrod Uxgulm with a half-ogre and a gazer, then Noska Ur'gray with six bugbears and a gazer. When all three have been beaten, the answer says the guild has no crew left to send on the street and that the next move will be Xanathar's own."
- `campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:148`: "> - **Noska's team:** "That leaves Noska Ur'gray with six bugbears and a gazer. They're who the Guild sends when it's done sending messages."
- `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-02-the-extraction.md:150`: quoted in D5.
- The Three Nights files do not name Noska (D6).
- For the orchestrator: the Noska page's "Featured in" line lists only **Xanathar's Lair**. The quest files above name Noska, but they are quest content and do not belong on the setting page.

### E8. Trollskull Manor guides and the Appendix D (standing rules)
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:9`: "**Exception:** Noska Ur'gray's bugbear team. Noska is Xanathar's enforcer, not its diplomat. Bugbears do not read the social calendar."
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:19`: "**Who comes:** Gorath (four duergar in unremarkable clothes). If Gorath is neutralized: Korgstrod Uxgulm's team (half-ogre + cloaked gazer). Noska Ur'gray does not visit — he arrives with intent."
- `sources/Appendix_D_-_Running_the_Tavern.md:1636`: "<p>The exception is Noska Ur'gray's team of bugbears. Noska is Xanathar's enforcer, not his diplomat, and bugbears do not read the social calendar. If Noska is deployed, he will not wait for closing time.</p>"

### E9. GM Guide (standing rules)
- `campaign/guides/gm-guide/running-the-villains.md:49`: "| **Xanathar's Guild** | Normal operations | Gazer scouts; Nihiloor processes captured intelligence. First team: Gorath's duergar, deployed as a warning | Second team: Korgstrod Uxgulm's squad (half-ogre + gazer) | Third team: Noska Ur'gray's bugbear squad with orders to eliminate. Xanathar takes personal interest; lair incursions trigger Eye-ray responses |"
- `campaign/guides/gm-guide/running-the-villains.md:57`: "> Anything involving Xanathar's goldfish — threatening it, harming it, even alarming it — triggers Lockdown immediately, regardless of the current escalation tier. No intermediate response fires. The faction moves straight to Noska Ur'gray's elimination squad."
- `campaign/guides/factions/09-xanathars-guild.md:74` and `:77` (the Lockdown row and the Sylgar warning) are the same standing rules.

---

## F. Gaps (what a Background would need that no source gives)

1. **Birth, family, early life, clan.** No source. The wiki gives no origin (`wiki-xg/Noska_Ur_gray.txt:62` [`wiki.txt:1707`]). Leave unstated, or tag `[research]` as "no origin is recorded".
2. **The injury date and place.** The adventure says only "A green slime in Undermountain" (`sources/adventure-wdh.json:32417`). Modest inference `[research]`: he lost the hand on Guild duty at a watch post on the upper levels of Undermountain. Support: "The Guild keeps watch posts on the upper levels of Undermountain, staffed by bugbears and goblins, to stop adventurers reaching the lower levels (WDMM)." (`campaign/setting/history/02-the-long-shadow.md:64`) and "Nine bugbears (five of them under the control of intellect devourers) represent the Xanathar Guild on this level." (`sources/adventure-wdmm.json:795`). Tag the sentence `[research]`.
3. **The crossbow arm's maker and date.** No source. Leave unstated. Naming a maker would be an invented plot fact.
4. **The rust monster's origin.** No source. The adventure gives "keeps the rust monster as a pet" (`sources/adventure-wdh.json:17331`) and nothing more.
5. **How he joined and rose.** No source for the joining. The wiki says he was "one of the most trusted underlings" (`wiki-xg/Noska_Ur_gray.txt:73` [`wiki.txt:1718`]) and was appointed "to important positions" by 1492 DR (`sources/research/pass5-bundles/xanathars-guild/wiki.txt:161`). No test, date or sponsor is given.
6. **Time in post.** The wiki gives "during the early 1490s DR" (`wiki-xg/Noska_Ur_gray.txt:62` [`wiki.txt:1707`]), which is the only date. Modest inference `[research]`: he has held the enforcer post since the early 1490s DR.
7. **Trust.** The wiki and adventure say he is trusted (`wiki.txt:1718`; `sources/adventure-wdh.json:15041`). No reason is given. Leave the reason out.
8. **Ahmaergo.** Sourced: the arena partnership (`sources/adventure-wdh.json:17166`, `:17173`; printed p.89). The rivalry is only in `campaign/structure/arc-f-xanathars-lair.md:41` (quest intelligence, D5). Do not write a rivalry as day-one. A sourced option is "they share the arena", with no friction.
9. **Nar'l Xibrindas.** No day-one line. The adventure's succession rule is a vault-exit scene (`sources/adventure-wdh.json:14780`), not a relationship.
10. **Gorath and Korgstrod.** Sourced only as the response ladder (`campaign/guides/factions/09-xanathars-guild.md:9`, `:11`, `:13`) and "Gorath delivers a message once and leaves, and Noska is sent when Xanathar is done sending messages" (`campaign/setting/organizations/08-xanathars-guild.md:77`).
11. **Grinda Garloth.** No day-one link. The Mistshore siege is Dragon Heist quest content (`sources/adventure-wdh.json:7528`-`:7538`). The wiki's "entrusted the Stone to Grinda" is conditional and conflicts with the campaign's Stone-in-the-lair (D11). No routed quest file exists: a search of `campaign/quests/` for "Grinda" returned only `campaign/quests/act-ii/gralhund-villa/design-notes.md`.
12. **Faith.** No source (A6). Leave out.
13. **Age, height, appearance beyond the arm and the crossbow.** No source.
14. **Whether he has seen Xanathar.** No source. The Guild page says "Most Guild agents do not know that their master is a beholder" (`campaign/setting/organizations/08-xanathars-guild.md:123`), but Noska's status is not stated. Do not assume either way.
15. **Personal hoard.** Sourced: "37 gp, 151 sp, 360 cp, and four bloodstones (worth 50 gp each)" (`sources/adventure-wdh.json:17347`). It is a room detail, usable as a Background touch.
16. **Pronouns.** Sourced (he/him). No gap.
17. **Stat block label.** Disputed (D1). The orchestrator must choose.

---

## Not readable

- None failed to open. The PDFs were read as rendered images (no `pdftotext` in this session). Their quotes are transcriptions. Check before prose use:
  - `sources/11. Lair  Xanathar’s Lair.pdf` (nine pages, all read; Noska on printed pp.89, 90, 91)
  - `sources/6. Faction Response Teams.pdf` (printed p.54 [PDF p.6])
  - `sources/5. Faction Outposts.pdf` (printed pp.40, 41, 42, 43, 44, 46, 47, 48 [PDF pp.5, 6, 7, 8, 9, 11, 12, 13]; no Noska. The Ahmaergo signature lines are at p.43 and p.44. Printed p.45 was not re-read this session; the Ott notes cover it.)
  - `sources/17. Outpost and Lair Revelation Lists.pdf` (printed pp.121, 122, 123 [PDF pp.1, 2, 3]; no Noska. Only PDF pages 1 to 3 were read.)
  - `sources/1. The Villains.pdf` (printed pp.13, 14, 15, 16, 17 [PDF pp.1 to 5]; no Noska. The Xanathar section is printed p.15.)
- Not page-checked: `sources/2. Other Factions.pdf`, `sources/7. Other Response Teams.pdf`, `sources/13. Clues and Timelines.pdf`, `sources/21. Faction Reports of the Grand Game.pdf`, and the other lair PDFs. The repo's `.md` and `.json` files were searched for Noska, and the PDFs cannot be searched by grep.
- Appendix B (`sources/Appendix_B_-_Player_Factions.md`) and Appendix C (`sources/Appendix_C_-_Player_Faction_Missions.md`) contain no "Noska" or "Ur'gray". A grep of `sources/Appendix_*.md` for Noska, Ur'gray, bugbear and Ahmaergo returned only Appendix C's bugbear, Ahmaergo and Ott lines and Appendix D's Noska lines.
- `sources/Other remix files/*.docx` were not searched. `SOURCE_GUIDE.md` lists none for Noska.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
