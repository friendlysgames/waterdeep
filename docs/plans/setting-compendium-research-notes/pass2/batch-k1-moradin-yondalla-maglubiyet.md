# Deities Pass 2, Batch K1: Moradin, Yondalla, Maglubiyet

Research report. Facts and quotes only.

## Conventions

- Wiki quotes (`research/deities/<power>/wiki.txt`): the `[[ ]]` link brackets are removed and the display text is kept. Everything else is copied as the file has it: `{{ }}` templates, `<ref>` tags, `''` and `'''` markup, `<br/>`, and the `[[File:…]]` embed in the Yondalla prayer line.
- Adventure quotes (`sources/adventure-wdh.json`, `sources/adventure-wdmm.json`): the JSON string content, with the file's escapes (`\"`, `—`) left as they are.
- Bundle files are cited by full path. Line numbers are the `cat -n` numbers from the Read tool.
- Multi-line 5etools extracts are in code fences, with the citation line after each block.
- Entries marked **[out of brief]** are in the bundle but not in the brief's 5etools source list for the heads of other pantheons (MTF, SCAG, PHB 2014). They are quoted so the orchestrator can decide.
- Up to 6 quotes per field. Published-adventure and campaign hits beyond the 6 are listed under **Cross-references** with the line copied.
- Bundle root, abbreviated in this report only where the path is shown in full: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/`

---

## MORADIN

### Field 1. Identity

**5etools, SCAG p.22 (2014). Title, alignment, domains, symbol.**

```
## Moradin | source SCAG p.22 | pantheon Dwarven
- title: God of creation
- alignment: ['L', 'G']
- domains: ['Forge', 'Knowledge']
- symbol: Hammer and anvil
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:43-47`

**5etools, PHB p.296 (2014). Title, alignment, domains, symbol.**

```
## Moradin | source PHB p.296 | pantheon Nonhuman
- title: Dwarf god of creation
- alignment: ['L', 'G']
- domains: ['Forge', 'Knowledge']
- symbol: Hammer and anvil
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:35-39`

**5etools, MTF p.72. Alignment, domains, symbol, category. This entry has no title field.**

```
## Moradin | source MTF p.72 | pantheon Dwarven
- alignment: ['L', 'G']
- domains: ['Forge', 'Knowledge']
- symbol: Hammer and anvil
- category: The Mordinsamman
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:24-28`

**Wiki, titles.** The refs in this line cite Demihuman Deities p.78. The wiki's infobox places Demihuman Deities in its 2e column (`wiki.txt:84`, `refs2e`).

```
| title               = The All-Father<ref name="DD-p78">{{Cite book/Demihuman Deities|78}}</ref><ref name="SCAG5e-p22,104" /><ref name="DMG5eR-p359">{{Cite book/Dungeon Master's Guide 5th edition (revised)|359}}</ref><ref name="HoF-p186">{{Cite book/Forgotten Realms: Heroes of Faerûn|186}}</ref><br/> Dwarffather<ref name="DD-p78"/><br/>The Soul Forger<ref name="DD-p78"/><br/>The Creator<ref name="DD-p78"/>
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:13`

**Wiki, pantheon.** The line has no refs.

> `| pantheon            = Morndinsamman`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:17`

**Wiki, lead sentence.** The first sentence of the article, with its pronunciation templates.

> "'''Moradin''' ({{Pronounce|MOR|a|din|refs=<ref name="D93-APG-p28">{{Cite dragon/93/Ay pronunseeAYshun gyd|28}}</ref>}} {{Pronounce|MOR|uh|din|refs=<ref name="FaP-p121" />|alt=yes}}) was the lawful good god of the dwarves and the chief deity in their pantheon."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:109`

### Field 2. Edict or core tenet

No 5etools Moradin entry has an edict field. The only commandments text in the bundle is EGW, which is **[out of brief]**.

**EGW p.24, Commandments. [out of brief]**

```
Commandments of Moradin: Remain stoic and tenacious in the face of catastrophe.
Uphold and promote loyalty to your family, loyalty to your clan, and loyalty to your people.
Legacy is paramount. To create something that lasts is to change the world for the better.
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:20-22`

**Wiki, the Soul Forger's standard (second sentence of the article).**

> "'''The Soul Forger''' was strength incarnate<ref name="OHG78">{{Cite book/On Hallowed Ground}}</ref> and force of will embodied, a harsh but fair judge who evaluated his creations by the goodness of their works first and intentions second."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:109`

**Wiki, Personality (first sentence).**

> "Moradin expected his children to aspire to his utmost levels of expertise, to study his techniques so they might follow in his footsteps.<ref name="MTF72">{{Cite book/Mordenkainen's Tome of Foes|72}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:120`

**Wiki, Personality (second sentence).** Citations: Demihuman Deities p.78, Forgotten Realms Campaign Guide p.75.

> "He was gruff, stern and virtually incapable of compromise, tirelessly and unflinchingly defending his people, their values, and his principles of good and law.<ref name="DD-p78"/><ref name="FRCG-p75">{{Cite book/Forgotten Realms Campaign Guide|75}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:120`

**Wiki, Personality (third sentence).**

> "While a good heart was necessary for his acceptance, only quality results earned his approval.<ref name="MMYTH" />"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:120`

### Field 3. Portfolio and areas of concern

No source gives an "Areas of Concern" field for Moradin. The 5etools entries have no portfolio field, and the wiki has none.

**MTF p.72, text paragraph (portfolio in prose).**

> "Moradin is the master of every craft practiced by the dwarves and the patron of artisans. He expects his children to follow in his footsteps, studying his techniques and aspiring to one day match his expertise."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:31`

**Wiki, portfolio (5e).**

> `| portfolio5e         = Creation, Dwarf crafts, Protection`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:32`

**Wiki, portfolio (3e).** The refs are none. The wiki's infobox places this in its 3e column.

> `| portfolio3e         = Dwarves, Creation, Metalcraft, Protection, Smithing, Stonework`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:62`

**Wiki, portfolio (2e).**

> `| portfolio2e         = Dwarves, creation, smithing, craftsmanship, war, protection, metalcraft, stonework, engineering, protection.`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:78`

### Field 4. Worship: clergy, holy days, temples, omens, messengers

Waterdeep: no temple, shrine or festival is named in any source. See Q1.

**MTF p.72, clergy.**

> "Priests of Moradin are responsible for judging and assessing the work of a stronghold's artisans. They keep great volumes that describe various crafting techniques in detail, and use the guidelines in them to judge the quality of individual works."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:32`

**Wiki, clergy (first sentence of the Worshipers section).**

> "Moradin's clerics, known as ''Sonnlinor'', were usually drawn from family lines, like most dwarven occupations; they wore earthy colors, with chain mail and silvered helms."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:135`

**Wiki, church role (sentence from the same paragraph).**

> "The church of Moradin had an active role in guiding the morals of dwarven communities; they emphasized his hand in everyday dwarven activities such as mining, smithing, and engineering, and invoked his blessing when these tasks began."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:135`

**Wiki, holy day.** The Rituals section cites nothing on this line. The wiki's own holy-day infobox fields are blank (`wiki.txt:37`, `wiki.txt:52`, `wiki.txt:68`, `wiki.txt:82`, `wiki.txt:95`).

> "Moradin's holy day was on the crescent moon and he was worshiped at forges and hearths."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:141`

**EGW p.24, holy day. [out of brief]**

> "Holy Day: Moradin's holy day is Deep Solace, which is celebrated on the eighteenth day of the fifth month. Especially devout followers of the All-Hammer spend the day in isolation, meditating on the meaning of family and how they may be better mothers, fathers, siblings, and children. The dwarven community in Grimgolir celebrates with a full day of feasting and drinking."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:19`

**Wiki, manifestations (omens and messengers).** No omen or messenger is named. This sentence is the nearest one.

> "Moradin preferred to work through manifestations rather than avatars, believing that dwarves had to work for their own place and salvation in the world,<ref name="MMYTH" /> and so he seldom appeared in the Realms.<ref name="DD-p78"/>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:125`

### Field 5. Relations with other powers; origin or rise

**Wiki, alliances and opposition (2e-era citation, see note).** The cite is Faiths and Pantheons p.122. The wiki's infobox places Faiths and Pantheons in its 3e column (`wiki.txt:70`, `refs3e`, FaP-p121). No edition is printed on the citation itself.

> "Moradin had a strategic but friendly alliance with Gond, Kossuth, Helm, Torm, Tyr, and the heads of the elven, gnome, and halfling pantheons. He opposed the gods of the goblinoids, orcs, evil giants, and banished dwarves.<ref name="FaP-p122">{{Cite book/Faiths and Pantheons|122}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:130`

**Wiki, origin myth.** Citation: Faiths and Pantheons p.122.

> "Moradin was held in dwarven myths to have been incarnated from rock, stone, and metal, and that his soul an ember of fire. It was said he forged the first dwarves from metals and gems and breathed souls into them when he blew on his creations to cool them. Moradin was responsible for banishing the evil gods of the derro and duergar from the surface.<ref name="FaP-p122">{{Cite book/Faiths and Pantheons|122}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:146`

**Wiki, the Fallen Kingdom.** Citation: Dwarves Deep pp.53-54.

> "Moradin's avatar appeared while the Ironstar dwarf clan was fleeing from orcs at the Stone Bridge, after a desperate appeal by Daurvos Frostbeard (which was his final act), and helped them defeat the orcs and gain safe passage to Ironford, thereby forming the Fallen Kingdom.<ref name="DD-p53-54">{{Cite book/Dwarves Deep|53-54}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:148`

**Wiki, Maglubiyet (the other side of the pair).** Citation: Demihuman Deities p.78.

> "Though many demihuman deities opposed the goblinkin pantheon, Moradin was noted to loathe Maglubiyet more specifically.<ref name="DD78">{{Cite book/Demihuman Deities|78}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:220`

Note: this sentence sits in the Maglubiyet bundle (`maglubiyet/wiki.txt:220`), not in the Moradin bundle.

### Field 6. Campaign and published-adventure mentions

**Campaign, Vault of Dragons (structure doc, active; not a quest journal).**

> "**Hall of Moradin.** Three hammer-shaped pillars run the length of this hall. A cracked mosaic depicting a dwarf smith crafting figures from black metal and diamond conceals a secret door — DC 17 Wisdom (Perception) to find, opening automatically for a dwarf or on a DC 17 Strength (Athletics) check for anyone else. A black pudding lurks in a break in the wall roughly halfway down the hall and attacks anyone who investigates the damage."
>
> — `/home/user/waterdeep/campaign/structure/arc-j-vault-of-dragons.md:148`

> "**The Secrets Room of Harlsnod Darkshine.** A dust-filled chamber untouched since the Delzoun era. Five copper urns hold the vault architect's personal offerings: gemstones, coin, a *ring of warmth*, and a small silver statuette of a dwarf priest of Moradin. The urns are empty; the story of sealed secrets is a legend with nothing behind it. Harlsnod's actual tomb lies on Level 9 of Undermountain, a thread worth remembering for later."
>
> — `/home/user/waterdeep/campaign/structure/arc-j-vault-of-dragons.md:150`

**Published adventure, WDH, V4. Hall of Moradin (Vault of Dragons).**

> `"name": "V4. Hall of Moradin",`
>
> — `/home/user/waterdeep/sources/adventure-wdh.json:14586`

> "This room holds five copper urns (worth 25 gp each). Urn 1 contains five tourmalines (worth 100 gp each) mixed in with 200 cp. Urn 2 contains a {@item ring of warmth} mixed in with ten ordinary gold rings (worth 25 gp each) and 650 sp. Urn 3 is piled high with 250 gp. Urn 4 holds 33 blue quartz gemstones (worth 10 gp each). Urn 5 holds a 9-inch-tall silver statuette of a dwarf priest of Moradin with amethyst eyes (worth 250 gp and weighing 10 pounds)."
>
> — `/home/user/waterdeep/sources/adventure-wdh.json:14632`

**Published adventure, WDMM, room 19 (Level 6, Lost Level).**

> "{@b Statues}. Four statues representing the dwarven deities Moradin (god of creation), Berronar Truesilver (god of hearth and home), Clangeddin Silverbeard (god of battle), and Marthammor Duin (god of exploration) stand in niches at the corners of this room."
>
> — `/home/user/waterdeep/sources/adventure-wdmm.json:18631`

**Published adventure, WDMM, area 26 (Level 15, Obstacle Course).**

> "This 20-foot-high, domed chamber is dominated by a 12-foot-tall stone statue of Moradin, the great dwarven god of the forge. It stands in the middle of the room facing the only exit. The statue is veined with bright mithral, and with one hand it raises a stone hammer carved with faintly glowing runes. A steel plaque at the base of the statue reads in Dwarvish, \"All that is made can be unmade.\""
>
> — `/home/user/waterdeep/sources/adventure-wdmm.json:43276`

Remaining hits are under Cross-references.

### Field 7. Conflicts and not found

**Pantheon name spelling.** The MTF entry reads "The Mordinsamman". The wiki and the Vault of Dragons file read "Morndinsamman".

> `- category: The Mordinsamman`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:28`

> "These images predate a falling-out between the three gods that the Morndinsamman has never fully explained. They are not necessary to **Vault of Dragons**'s plot — the party can walk past them without consequence — but a party that lingers and investigates is rewarded with one more thread connecting the vault's dwarven history to the deep, patient intelligences (illithid and aboleth alike) that the Undermountain campaign will eventually make explicit."
>
> — `/home/user/waterdeep/campaign/structure/arc-j-vault-of-dragons.md:154`

**Holy day.** The wiki's holy day (crescent moon) and EGW's holy day (fifth month, eighteenth day) do not match. The EGW entry is out of brief. The wiki line is quoted in Field 4.

**Plane.** EGW places Moradin on Celestia, in Erackinor under Solania. **[out of brief]**

> "Moradin lords over the soul forges within the massive tunneled mansion of Erackinor, deep beneath the slopes of Solania on the plane of Celestia."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:17`

> `| homeplane3e         = Dwarfhome`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:58`

> `| homeplane2e         = Solania, Mount Celestia`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:74`

**Symbol and domains in the out-of-brief entries.** DMG p.10 and EGW p.24 differ from SCAG, PHB and MTF. **[out of brief]**

```
## Moradin | source DMG p.10 | pantheon Dawn War
- title: God of creation
- alignment: ['L', 'G']
- domains: ['Forge', 'Knowledge', 'War']
- symbol: Flaming anvil
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:1-5`

```
## Moradin | source EGW p.24 | pantheon Exandria
- title: the All-Hammer
- alignment: ['L', 'G']
- domains: ['Forge', 'Knowledge', 'War']
- symbol: Hammer with ends carved in the likeness of dwarven heads
- category: Prime Deities
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/5etools.md:9-14`

**Not found (Moradin).**
- 5etools `worshipers` field: none in any Moradin entry.
- Areas of concern, edict in the brief's sources (SCAG, PHB, MTF): none.
- Holy day in SCAG, PHB or MTF: none.
- Messengers, omens: none.
- Waterdeep temple or shrine: none (see Q1).
- Campaign Notable Figures naming Moradin: none (see Q2).
- Searched for Moradin, Dwarffather, All-Father, Soul Forger, Morndinsamman, Mordinsamman, Sonnlinor, Hammers of Moradin, "dwarf god", "dwarven god", "dwarven pantheon" in `campaign/` (all files), `sources/adventure-wdh.json`, `sources/adventure-wdmm.json`, and the Moradin bundle.

### Answers (Moradin)

**Q1. Which temples or shrines the adventure or campaign files place in Waterdeep, and in which ward.**

No temple or shrine to Moradin is placed in Waterdeep by any source. The WDH "Major Temples of Waterdeep" table has no dwarven row. Its caption:

> `"caption": "Major Temples of Waterdeep",`
>
> — `/home/user/waterdeep/sources/adventure-wdh.json:30910`

The table's only row that could cover every deity is the "All deities" row. It names no power.

```
"All deities",
"Holyhands House",
"North Ward"
```
— `/home/user/waterdeep/sources/adventure-wdh.json:30923-30925`

The Vault of Dragons is the only place in the campaign or the adventure that holds a Moradin room. Its Hall of Moradin is a vault room, not a shrine. The vault's location:

> "If a character becomes attuned to the {@item Stone of Golorr|WDH}, it reveals the location of the Vault of Dragons, under the Brandath family mausoleum in the City of the Dead, and the three keys needed to enter it. When the characters are ready to visit the mausoleum, proceed with encounter 4, \"Mausoleum.\""
>
> — `/home/user/waterdeep/sources/adventure-wdh.json:9778`

The campaign lore places the City of the Dead among the wards:

> "- **City of the Dead** (walled necropolis): the Brandath Mausoleum (vault entrance) is here, reached by the approach called the Brandath Crypts; patrolled but not well-staffed"
>
> — `/home/user/waterdeep/campaign/setting/waterdeep-lore.md:20`

**Q2. Which campaign NPC, faction or quest uses the power.**

Quest: the Vault of Dragons (`campaign/structure/arc-j-vault-of-dragons.md:148` and `:150`, quoted in Field 6). That file is an active structure doc, not a quest journal.

Notable Figures: none names Moradin. The dwarf notable figures name other gods:

> "> - *Shield dwarf moneylender, lawful evil*. Stat block: **Veteran**."
>
> — `/home/user/waterdeep/campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:6`

> "**Emotions.** Istrid most often feels shrewd calculation, ledger-balancing satisfaction, predatory patience, devout worship of Vergadain (dwarf god of wealth and luck), cold disdain for poor financial judgment, and possessive pleasure in a growing ledger."
>
> — `/home/user/waterdeep/campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:14`

> "> - *Dwarf cult fanatic (Zuggtmoy), neutral evil*. Stat block: **Cult Fanatic**."
>
> — `/home/user/waterdeep/campaign/setting/notable-figures/xanathars-guild/06-ott-steeltoes.md:6`

> "**Relationships.** Ott is Xanathar's fishkeeper (all Sylgar replacements have passed through him), a Zuggtmoy worshipper who cultivates mushrooms in his quarters, a Zhentarim prisoner at the Interrogation House, a field agent of Xanathar's Guild, and a detailed intelligence source for anyone who rescues him and asks the right questions about the Lair."
>
> — `/home/user/waterdeep/campaign/setting/notable-figures/xanathars-guild/06-ott-steeltoes.md:26`

The other shield-dwarf and dwarf notable figures (Harug Shieldsunder, Ulkoria Stonemarrow, Noska Urgray, Thorvin Twinbeard, Ahmaergo) name no god in their files. Istrid's faith is the only one the Notable Figures give a dwarven deity: Vergadain, not Moradin.

**Q3. Which lines in wiki.txt mention Waterdeep.**

None. No line in `moradin/wiki.txt` contains "Waterdeep", "Waterdhavian" or "Undermountain". The nearest temple in the wiki is in a gallery caption for Neverwinter:

> `Neverwinter temple of moradin.jpg|''A temple to Moradin.''`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:180`

### Cross-references (Moradin)

- `/home/user/waterdeep/sources/adventure-wdmm.json:18623`: `"name": "19. Mountain Shrine",`
- `/home/user/waterdeep/sources/adventure-wdmm.json:18867`: `{@b Tapestry}. Hanging on the south wall between the statues of Moradin and Berronar is a thick tapestry depicting King Melair, his adamantine war pick in hand as he battles a purple worm. (The tapestry is too moldy and frayed to be worth anything.)`
- `/home/user/waterdeep/sources/adventure-wdmm.json:18871`: `The statues represent the dwarven deities Moradin (god of creation), Berronar Truesilver (god of hearth and home), Clangeddin Silverbeard (god of battle), and Marthammor Duin (god of exploration). A demon is trapped in each statue (see \"Trapped Demons\" below).`
- `/home/user/waterdeep/sources/adventure-wdmm.json:18879`: `The Melairkyn dwarves trapped four demons in the statues after attempts to banish the fiends failed—a {@creature barlgura} in the statue of Moradin, a {@creature hezrou} in the statue of Berronar, a {@creature vrock} in the statue of Clangeddin, and a {@creature glabrezu} in the statue of Marthammor. Over the centuries of its confinement, the glabrezu has learned how to telepathically contact creatures in this room. Using its telepathy, it tries to trick an interloper into freeing it. Though the other three demons have telepathy, they are not powerful enough to use the ability while trapped in their statues.`
- `/home/user/waterdeep/sources/adventure-wdmm.json:43272`: `"name": "26. Statue of Moradin",`
- `/home/user/waterdeep/sources/adventure-wdmm.json:43312`: `"name": "Additional Effect: Moradin Smash",`
- `/home/user/waterdeep/sources/adventure-wdmm.json:43316`: `When a creature is teleported to this location from another teleport trap, a disembodied voice shouts, \"Teleported!\" at the same moment the statue of Moradin animates and takes a swing at the creature with its hammer. The target must succeed on a {@dc 17} Dexterity saving throw or take 40 ({@dice 6d10 + 7}) force damage. Any creature reduced to 0 hit points by this damage is disintegrated, along with all items it is wearing and carrying except for artifacts. After swinging the hammer once, the statue reverts to its inanimate state until the trap is triggered again.`
- `/home/user/waterdeep/sources/adventure-wdh.json:13720`: `"name": "Vault of Dragons",`
- Wiki Hammers of Moradin (clergy order): `wiki.txt:138`: `* [[Hammers of Moradin]]: An elite military order dominated by crusaders and fighting clerics with chapters in nearly every dwarven stronghold and members drawn from every dwarven clan. The Hammers served both as commanders of dwarven armies and as an elite strike force skilled in dealing with anything from large groups of orcs to [[Wyrm|great wyrms]] to malevolent [[fiend]]s from the [[Fiendish Planes]]. The order was dedicated to the defense of existing dwarven holdings and the carving out of new dwarven territories. Individual chapters had a great deal of local autonomy but, in times of great crisis, a Grand Council assembled to plot strategy and divine Moradin's will.<ref>{{Cite book/Player's Guide to Faerûn|56}}</ref>` — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/moradin/wiki.txt:138`
- WDMM area 19 and 26 names are listed above. WDMM level headings: `"name": "Level 6: Lost Level",` (`sources/adventure-wdmm.json:16282`), `"name": "Level 15: Obstacle Course",` (`sources/adventure-wdmm.json:40631`).

---

## YONDALLA

### Field 1. Identity

**5etools, MTF p.102. Alignment, domains, symbol. This entry has no title field.**

```
## Yondalla | source MTF p.102 | pantheon Halfling
- alignment: ['L', 'G']
- domains: ['Life', 'Twilight']
- symbol: Cornucopia
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/5etools.md:1-4`

**5etools, PHB p.296 (2014). Title, alignment, domains, symbol.**

```
## Yondalla | source PHB p.296 | pantheon Nonhuman
- title: Halfling goddess of fertility and protection
- alignment: ['L', 'G']
- domains: ['Life', 'Twilight']
- symbol: Shield
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/5etools.md:10-14`

**5etools, SCAG p.23 (2014). Title, alignment, domains, symbol.**

```
## Yondalla | source SCAG p.23 | pantheon Halfling
- title: Goddess of fertility and protection
- alignment: ['L', 'G']
- domains: ['Life', 'Twilight']
- symbol: Cornucopia on a shield
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/5etools.md:18-22`

**Wiki, titles.** Citations are Faiths and Pantheons p.141 and Demihuman Deities pp.179-180 (the `DD-179` ref). The wiki's infobox places Demihuman Deities in its 2e column (`wiki.txt:82`).

```
| title               = The Protector and Provider<ref name="FP141">{{Cite book/Faiths and Pantheons|141}}</ref><ref name="DD-179"/><br/>The Nurturing Matriarch<ref name="FP141"/><ref name="DD-179"/><br/>The Blessed One<ref name="FP141"/><ref name="DD-179"/><br/>Matriarch Protector and Sovereign Creator<ref name="BGIII">{{Cite game/Baldur's Gate III}}</ref>
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:7`

**Wiki, pantheon.** The brackets around the link are removed.

> `| pantheon            = Yondalla's Children<ref name="MToF-pp102-103">{{Cite book/Mordenkainen's Tome of Foes|102-103}}</ref><ref name="SCAG5e-p23,109" />`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:14`

**Wiki, lead sentences.** Citation: Faiths and Pantheons p.141.

> "'''Yondalla''' ({{Pronounce|yon|DAH|lah|refs=<ref name="FP141" />}}) was the creator of the halfling race and matriarch of not only the halfling pantheon, but the whole race itself. With her charming personality and friendly demeanor she was an example to all halflings; who almost all shared her curiosity, loyalty and sense of mischief.<ref name="FP141" />"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:105`

### Field 2. Edict or core tenet

No 5etools Yondalla entry has an edict field. The only line of worship text in the wiki is a prayer, not an edict.

**Wiki, prayer (not an edict; quoted for completeness).** The `[[File:…]]` embed is kept as written.

> `{{Quote|Fill my cup with plenty, mother. May it never run dry.|A basic prayer to Yondalla.<ref name="BG3">{{Cite game/Baldur's Gate III}}</ref>}}[[File:Yondalla_symbol.jpg|250px|left|thumb|The holy symbol of Yondalla]]`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:113`

### Field 3. Portfolio and areas of concern

**Wiki, portfolio (5e).**

> `| portfolio5e         = Fertility, protection`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:29`

**Wiki, portfolio (3e).**

> `| portfolio3e         = Protection, Bounty, Halflings, Children, Security, Leadership, Wisdom, Creation, Family, Tradition`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:60`

**Wiki, portfolio (2e).**

> `| portfolio2e         = Death, nature, protection,<ref name="TSS" /> fertility, the halfling race, children, security, leadership, diplomacy, wisdom, the cycle of life, creation, family, familial love, tradition, community, harmony, prosperity`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:76`

**MTF p.102, what Yondalla is responsible for (luck and harvest).**

> "To the halflings, Yondalla is responsible for the spring in their step and the bubbly excitement they feel from knowing that luck is on their side. When a pumpkin grows to enormous size or a garden yields twice as many carrots as usual, credit goes to Yondalla. When a halfling trips, slides down a hillside, and lands on a nugget of gold, that's Yondalla turning bad luck into good."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/5etools.md:8`

### Field 4. Worship: clergy, holy days, temples, omens, messengers

Waterdeep: the only Yondalla shrine in any file is in the Doom Raiders faction event (Field 6 and Q1).

**Wiki, temples.** The wiki's temples are rare and hidden.

> "Despite her widespread worship among halflings and her central role in their society; her temples were unusually rare, those that did exist were designed to look like a well-hidden halfling burrow-home and were filled with weapons and food so that the communities that surrounded them could hold out against possible invaders. Her clergy were afforded a lot of respect by the followers of other gods for their defensive capabilities in spite of their small stature."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:114`

**Wiki, clerics and favored weapon. The first sentence cites Forgotten Realms Campaign Setting 3e p.240 through an unnamed `<ref>`.** The line is quoted whole so that the refs stay in place.

> `[[Cleric|Clerics]] of Yondalla considered the short sword to be a favored weapon, in honor of the Goddess' sword [[Hornblade (short sword)|Hornblade]].<ref>[[Ed Greenwood]], [[Sean K. Reynolds]], [[Skip Williams]], [[Rob Heinsoo]] (June 2001). ''[[Forgotten Realms Campaign Setting 3rd edition]]''. ([[Wizards of the Coast]]), p. 240. ISBN [[Special:BookSources/0-7869-1836-5|0-7869-1836-5]].</ref> Powerful clerics were granted the ability to cast ''[[Curse of Yondalla]]'', a spell reserved to be used against those who committed foul crimes against halflings.<ref name="DD-182">{{Cite book/Demihuman Deities|182}}</ref>`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:116`

**Wiki, followers (5e).**

> `| worshipers5e        = Halflings`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:32`

**Wiki, followers (3e).**

> `| worshipers3e        = Children, [[halflings]], leaders, [[paladins]], parents`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:63`

Holy days, omens and messengers: none (see Not found).

### Field 5. Relations with other powers; origin or rise

**MTF p.102, origin story.**

> "The story of Yondalla begins at the dawn of the world, when halflings were timid wanderers, scraping out a meager existence. The goddess Yondalla took note of them and decided to adopt the halflings as her people. She was a strong leader with a vision for her people, and she dedicated her life to gathering them together and protecting them. Over time, she elevated to godhood those halflings who were the most adept at the skills halflings needed to survive. Those legendary halflings comprise the rest of the pantheon."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/5etools.md:6`

**MTF p.102, first halfling villages.**

> "Yondalla created the first halfling villages and showed the people how to build, plant, and harvest. She knew that the bounty of a halfling village would be tempting plunder for any brigand or monster, so she used her powers to conceal their homes from easy discovery, blending them into the landscape so that most travelers would pass by without a second glance."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/5etools.md:7`

**Wiki, relations with other powers.** Citation: Faiths and Pantheons p.141. Bane, Cyric, Talona, Talos and the Deities of Fury are the powers she scorned.

> "Yondalla had close bonds with Garl Glittergold, Corellon Larethian and Moradin. With the passion with which she loved and admired her fellow halfling deities, sometimes known as 'Yondalla's Children', she scorned certain evil deities, such as Bane, Cyric, Talona, Talos, and the Deities of Fury.<ref name="FP141" />"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:110`

**Wiki, 2e servants (the 2e column lists these as servants).** The brackets are removed.

> `| servedby2e          = Arvoreen,<ref>{{Cite book/Demihuman Deities|162}}</ref> Brandobaris,<ref>{{Cite book/Demihuman Deities|166}}</ref> Cyrrollalee,<ref>{{Cite book/Demihuman Deities|169}}</ref> Sheela Peryroyl,<ref>{{Cite book/Demihuman Deities|172}}</ref> Urogalan<ref>{{Cite book/Demihuman Deities|175}}</ref>`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:75`

The wiki's History section is a stub (see Not found).

### Field 6. Campaign and published-adventure mentions

**Campaign, Doom Raiders faction event m03 "The Missing Snobeedle", overview.**

> "Blossom has posted notices at the market by the Waymoot and at the Yondalla shrine on Larkhaven Street. The halflings of the Southern Ward know where Dasher is, and they will not tell strangers who might drag him home. Tashlyn knows none of this. She sees five hundred gold that the Doom Raiders could use while Davil is away."
>
> — `/home/user/waterdeep/campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:25`

> "The party spends three days among the Southern Ward's halflings, at the market by the Waymoot, the Yondalla shrine on Larkhaven Street and the rooms above a cooperage. Each place offers a way to earn the ward's trust and a way to force the issue, and all three end at the same conclusion: Dasher is with the Shard Shunners, and the ward will pass the party's request to Kelso Fiddlewick. On the evening of the third day a check arranges the meeting, and a fallback keeps it from failing outright."
>
> — `/home/user/waterdeep/campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:37`

**Campaign, m03 ev-01, the Southern Ward leads (a handout in the event).**

> "Halflings with an orchard and a meadery in Undercliff, east of the walls. The mother is Blossom, and she's the one who posted the notice. Look at the market by the Waymoot and the Yondalla shrine on Larkhaven Street, because that's where she nailed the rest."
>
> — `/home/user/waterdeep/campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:57`

> "The halfling community of the Southern Ward gathers in three places: the market by the Waymoot, the Yondalla shrine on Larkhaven Street, and a run of rented rooms above a cooperage on the same street. Each lead takes a day to work properly. A party that splits up can finish all three sooner, but nobody in the ward answers before the evening of the third day, because the message has to reach Kelso Fiddlewick and come back. Whichever lead the party follows, it arrives at the same fact: the Shard Shunners have Dasher, and the ward will carry a request to their leader."
>
> — `/home/user/waterdeep/campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:128`

**Campaign, m03 ev-01, the shrine scene.**

> "> The shrine of Yondalla on Larkhaven Street is a whitewashed cottage with a round green door and a hearth burning inside, and a few dozen halflings crowd the pews for the evening blessing. A gray-haired halfling in a plain robe sets fresh candles in the holders along the wall, and he glances up as you come in and then goes back to the candles."

Note: the `>` is the file's blockquote marker, copied as it stands.

> — `/home/user/waterdeep/campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:166`

**Published adventure.** No line in `sources/adventure-wdh.json` or `sources/adventure-wdmm.json` names Yondalla. The bundle's `adventure-hits.txt` is empty, and my own targeted grep confirms it.

### Field 7. Conflicts and not found

**Symbol variants.** Five sources give five symbols.

> `- symbol: Shield`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/5etools.md:14`

> `- symbol: Cornucopia on a shield`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/5etools.md:22`

> `| symbol2e            = Shield with cornucopia`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:71`

The MTF entry gives `- symbol: Cornucopia` (`yondalla/5etools.md:4`). The wiki's 5e symbol is `Cornucopia on a shield` (`yondalla/wiki.txt:24`).

**Domains.** The 5etools (2014) domains are Life and Twilight. The wiki's 3e domains differ.

> `| domains3e           = Family, Gluttony, Good, Halfling, Law, Protection`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:61`

Clean-up note: the brackets around the links are removed in this quote. The wiki's 5e domains are "Life" and "Twilight" (`yondalla/wiki.txt:30-31`, Tasha's Cauldron of Everything pp.34-35).

**Plane.** The wiki's 3e and 2e columns differ.

> `| homeplane3e         = Green Fields`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:56`

> `| homeplane2e         = Mount Celestia/Venya`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:72`

**Ward name.** The lore file's ward is "South Ward". The Doom Raiders file says "Southern Ward", as does the WDH table's Helm's Hall row.

> "- **South Ward** (working class, immigrants, industry): where new arrivals settle first"
>
> — `/home/user/waterdeep/campaign/setting/waterdeep-lore.md:18`

> `"Southern Ward"`
>
> — `/home/user/waterdeep/sources/adventure-wdh.json:30940`

**Not found (Yondalla).**
- 5etools `worshipers` field: none in any Yondalla entry.
- Holy days: wiki infobox fields are blank (`yondalla/wiki.txt:35`, `:50`, `:66`, `:80`, `:93`). No source names a Yondalla holy day.
- Omens, messengers: none in any source.
- Edict: none in the 5etools sources or the wiki beyond the prayer quoted in Field 2.
- Waterdeep temple in the WDH table: none (see Q1).
- Adventure hits: none (see Field 6).
- Wiki History section is a stub: `==History==` followed by `{{sectstub}}` (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:120-121`).
- Searched for Yondalla, Yondallan, Dallillia, Perissa, halfling god, halfling deity, halfling pantheon, Curse of Yondalla, Hornblade in `campaign/` (all files), both adventure JSON files, and the Yondalla bundle.

### Answers (Yondalla)

**Q1. Which temples or shrines the adventure or campaign files place in Waterdeep, and in which ward.**

The Doom Raiders faction event m03 places a Yondalla shrine on Larkhaven Street, in the Southern Ward (Field 6, `m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:128`). The event calls it "the Yondalla shrine on Larkhaven Street". The published adventure places none.

The WDH table has no halfling row. Caption as quoted at `sources/adventure-wdh.json:30910`. The Southern Ward row for Helm's Hall is at `sources/adventure-wdh.json:30940`.

The Alexandrian Remix Appendix C names the same shrine. This line came from a repo-wide grep for "Larkhaven" and sits outside this brief's scope. It is quoted for the orchestrator:

> "The Southern Ward's halfling community is the party's primary research environment. Three days of investigation — conversations at community gathering points, at the market near the Waymoot, at the small temple of Yondalla on Larkhaven Street — and a DC 18 Charisma (Persuasion or Intimidation) check arranges a meeting."
>
> — `/home/user/waterdeep/sources/Appendix_C_-_Player_Faction_Missions.md:1312`

Its "small temple" differs from the event's "shrine". The file is not otherwise searched for these powers.

**Q2. Which campaign NPC, faction or quest uses the power.**

Quest: the Doom Raiders faction event m03, "The Missing Snobeedle" (quoted in Field 6). The Notable Figures name no Yondalla worshipper. Kelso Fiddlewick, the middleman the ward answers to, is a halfling. His notable figure does not name a god:

> "> - *Lightfoot Halfling wererat, Neutral*. Stat block: **Wererat**, used in halfling form unless a Shunner falls."
>
> — `/home/user/waterdeep/campaign/setting/notable-figures/independents-adversaries/03-kelso-fiddlewick.md:5`

No dwarf, halfling or goblinoid notable figure names Yondalla.

**Q3. Which lines in wiki.txt mention Waterdeep.**

One line:

> `| aspects             = Dallillia ([[Sword Coast]] south of [[Waterdeep]])<ref name="DD-179"/><br/>Perissa ([[Moonshae Isles|Moonshaes]])<ref name="DD-179"/>`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/yondalla/wiki.txt:10`

This is the "aspects" field: Dallillia, the aspect of Yondalla "south of Waterdeep" on the Sword Coast. It is not a temple.

### Cross-references (Yondalla)

- `/home/user/waterdeep/campaign/setting/waterdeep-lore.md:18` (Ward naming, quoted in Field 7).
- `/home/user/waterdeep/sources/adventure-wdh.json:30940` (Helm's Hall, Southern Ward; quoted in Field 7).
- `/home/user/waterdeep/sources/Appendix_C_-_Player_Faction_Missions.md:1312` (quoted in Q1; outside brief scope).
- The repo-wide "Larkhaven" grep also hit `docs/index.html:1104`. That is a generated HTML copy of the campaign. Its line was too long to show, and I did not read it.

---

## MAGLUBIYET

### Field 1. Identity

**5etools, PHB p.296 (2014). The only Maglubiyet entry in the bundle. It has no text and no worshipers field.**

```
## Maglubiyet | source PHB p.296 | pantheon Nonhuman
- title: Goblinoid god of war
- alignment: ['L', 'E']
- domains: ['War', 'Order']
- symbol: Bloody axe
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/5etools.md:1-5`

**Wiki, titles.** Refs are Defenders of the Faith pp.92, 94; Living Greyhawk; Deities & Demigods 1e p.94; Volo's Guide to Monsters pp.162, 40; Mordenkainen's Fiendish Folio p.17; Baldur's Gate III.

```
| title               = 
Fiery-Eyes<ref name="DF3e-p92,94">{{Cite book/Defenders of the Faith|92,94}}</ref><br/>
The Mighty<ref name="LGOL">{{Cite web/Living Greyhawk: Official Listing of Deities for Use in the Campaign, Version 2.0}}</ref><br/>
The Mighty One<ref name="DD1e-p94">{{Cite book/Deities & Demigods 1st edition|94}}</ref><br/>
The Great One<ref name="VGM5e-p162">{{Cite book/Volo's Guide to Monsters|162}}</ref><br/>
The Great Scourge<ref name="MFF">{{Cite book/Mordenkainen's Fiendish Folio, Volume 1: Monsters Malevolent and Benign|17}}</ref><br/>
The High Chieftain<ref name="DF3e-p92,94" /><br/>
The Battle Lord<ref name="DF3e-p92,94" /><br/>
The Lord of Depths and Darkness<ref name="DD1e-p94" /><br/>
The Conquering God<ref name="VGM5e-p40">{{Cite book/Volo's Guide to Monsters|40}}</ref><br/>
All-Conquering Maglubiyet<ref name="BGIII" />
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:12-22`

**Wiki, 5e power, alignment, symbol.** Citations are Volo's Guide to Monsters pp.46-47, 48-50, 52 and the PHB p.63. The alignment is lawful evil, and the symbol is a bloody headsman's axe.

```
| power5e             = [[Greater deity]]
| alignment5e         = [[Lawful evil]]
| symbol5e            = Bloody headsman's [[axe]]
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:35-37`

Brackets are removed from the links on the Maglubiyet wiki lines in this report.

**Wiki, 5e portfolio, domains, followers.**

```
| portfolio5e         = War
| domains5e           = [[Order domain|Order]], [[War domain|War]]
| worshipers5e        = [[Goblinoid]]s
```
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:42-44`

**Wiki, pantheon.**

> `| pantheon            = Goblinoid pantheon<ref name="VGM5e-p44">{{Cite book/Volo's Guide to Monsters|44}}</ref>`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:27`

**Wiki, lead sentence.** The first sentence of the article, with its pronunciation template.

> "'''Maglubiyet''' ({{Pronounce|ma|GLUB|i|yet|refs=<ref name="D93-APG-p28">{{Cite dragon/93/Ay pronunseeAYshun gyd|28}}</ref>}}), known as '''The Mighty One''' or '''The High Chieftain''' was the chief deity of the goblinoids and ruler of the goblinoid pantheon, lording over mortal heroes and immortal gods alike with an iron fist.<ref name="DD1e-p94" /><ref name="RF3e-p137">{{Cite book/Races of Faerûn|137}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:115`

### Field 2. Edict or core tenet

No 5etools edict. The wiki's Personality and Dogma sections are the closest.

**Wiki, Personality (the glory of war itself).**

> "Where Gruumsh sent his people to war primarily in the name of seizing new territory, Maglubiyet's missions of conquest and devastation were simply for the sake of the glory of war, battle and carnage itself. War and destruction were Maglubiyet's true passions, and though he tolerated no dissent between the goblins and hobgoblins that worked against their mutual expansion or survival, it fell to their specific racial gods to actually push for such things.<ref name="MMyth2e-p49" /><ref name="OHG2e-p130-132" />"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:133`

**Wiki, Dogma (goblinoid doctrine).**

> "Goblinoids were indoctrinated in their youth to believe that Maglubiyet and his servants were the only true gods, and that the world would be wracked with chaos and despair until all other lesser, false deities had been conquered. As a result, goblinoids hated enemy clerics, and though they might accept conversions to Maglubiyet worship or spare the followers of \"harmless\" gods, in the end, no false god could be allowed to stand.<ref name="VGM5e-p48-50"/>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:244`

Note: the wiki keeps the straight quotes around "harmless" and the `enemy clerics` link is shown without its brackets.

**Wiki, Dogma (the god's own aim).**

> "In truth, Maglubiyet desired the destruction of the surface races, craving the glory of war and slaughter for its own sake. He drove his servants to destroy the dwarves and gnomes who were their primary competition, urging his followers to overbreed so the competition could be overrun with superior numbers. The war in Acheron was framed as a sacred battle against the treacherous spirits of the orcs, but Maglubiyet was legendarily treacherous himself and also taught his people to overwhelm them through trickery.<ref name="MM3e-p134,154"/><ref name= \"GToN\"/><ref name=\"MMyth2e-p49\" /><ref name=\"RF3e-p136\">{{Cite book/Races of Faerûn|136}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:246`

### Field 3. Portfolio and areas of concern

No "Areas of Concern" field exists in the Maglubiyet sources. The portfolios are below.

**Wiki, portfolio (3e).** The refs are none.

> `| portfolio3e         = Goblins, goblinoids, leadership, rulership war`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:71`

Brackets removed. The wiki's `portfolio3e` line reads `[[Goblin]]s, [[goblinoid]]s, leadership, rulership war` in the source.

**Wiki, portfolio (2e).**

> `| portfolio2e         = War, rulership`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:86`

**Wiki, the Powers paragraph (first sentence).**

> "A powerful war god and great general, Maglubiyet created avatars of dangerous physical strength, speed, and endurance."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:149`

### Field 4. Worship: clergy, holy days, temples, omens, messengers

Waterdeep: none. See Q1.

**Wiki, omens (first sentence).** Citation: Monster Mythology p.49.

> "Omens from Maglubiyet took the form of blood seeping from an axe's edge, unusual behavior from the wolves and worgs amid the mounts of the goblins.<ref name=\"MMyth2e-p49\" />"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:126`

Note: the wiki reads `<ref name="MMyth2e-p49" />`; the quote keeps it.

**Wiki, priests and shamans (clergy).**

> "It was for this reason that Maglubiyet's priests and shamans were of such major importance to him, important enough that he communicated with them fairly often. They were the vital tools for his purposes on the Prime Material plane, for they had major influence on the goblin tribes. Maglubiyet demanded sacrifices from the priesthood, who taught that such things gave life-energy that Maglubiyet would then consume and use in his sacred war against the treacherous orc spirits.<ref name=\"MMyth2e-p49\"/>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:175`

**Wiki, monthly sacrifice (the ritual schedule). The sentence is whole. The rest of the Rituals paragraph covers the victims and the sacrifices.**

> "Once each month, usually on nights of a new moon, the victims would be ceremonially beheaded with his holy weapon, the battleaxe, and the shamans would sacrifice their still-living hearts."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:251`

**Wiki, the temple and the holy symbol (first two sentences).**

> "The holy symbol of Maglubiyet was the headsman's axe, and the block was where it was fed, blessed with the lifeblood of conquered foes and neglectful goblinoids. Near the block of Maglubiyet would stand a post or rack with various weapons representing the symbols of the goblinoid pantheon, placed in order of rank with the axe at the top."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:254`

The rest of the paragraph covers the goblin, hobgoblin and bugbear gods' weapons.

**Wiki, goblins' worship (out of fear).** Citations include VGM pp.48-50.

> "When Maglubiyet conquered the goblins, he taught them to fear his cruelty, and showed them how easily dominated their race was. This in turn led them to dominate others in their impotent frustration at their situation. By contrast to the hobgoblins, goblins worshiped Maglubiyet out of fear, their dread at the prospect of serving under his and the hobgoblin's eternal tyranny causing them to absolutely fear death. Once forced to join a war host, they had no choice but to resign themselves to their possible fate even more, further reducing their mercy, but not completing destroying their will to keep on surviving.<ref name=\"VGM5e-p48-50\" /><ref name=\"VGM5e-p40\" /><ref name=\"MM5p165\" /><ref name= \"TLG\" />"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:239`

Note: the source's wording "not completing destroying" is copied as written.

Messengers: none in any source. Holy days: none (see Not found).

### Field 5. Relations with other powers; origin or rise

**Wiki, head of the goblinoid pantheon (first sentence).**

> "Maglubiyet was the head of the goblinoid pantheon, ruling all others gods of his people with an iron fist."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:182`

**Wiki, Gruumsh (rivalry).** Citations: Monster Mythology p.44, Volo's Guide to Monsters p.82.

> "Maglubiyet had fought against Gruumsh for a time beyond reckoning, the reason for their persistence in the futile struggle largely unknown. Some believed it was to sharpen their skills in war, to test out strategies for other battles, or that it was simple envy and malice. In truth, both gods had their own reasons. To Gruumsh, the conflict was an opportunity, a chance to put his people against an eager enemy, thus allowing them to prove their worth to him and his pantheon. For Maglubiyet meanwhile, the war was a bid for the Conquering God to dominate yet another pantheon, to bring the Tribe of He Who Watches to heel as he had so many others.<ref name=\"MMyth2e-p44\" /><ref name=\"VGM5e-p48-50\" /><ref name=\"VGM5e-p82\">{{Cite book/Volo's Guide to Monsters|82}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:216`

**Wiki, Moradin (the wiki's note on Moradin's feeling for him).**

> "Though many demihuman deities opposed the goblinkin pantheon, Moradin was noted to loathe Maglubiyet more specifically.<ref name=\"DD78\">{{Cite book/Demihuman Deities|78}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:220`

**Wiki, origin (first two sentences of The Conquering God section).** Citations begin with Mordenkainen Presents: Monsters of the Multiverse.

> "Maglubiyet's origins were unclear, but despite what certain goblinoid myths might imply, he was not the divine creator nor ancestor of the goblinoids. The goblinoid peoples, even if many had forgotten, first appeared in the Feywild millenia ago, tracing their origin to ancient Feywild courts where they first appeared together."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:265`

Note: "millenia" is spelled as in the source.

**Wiki, Tiamat (Modern Times).** Citation: Dragon 359 p.68.

> "When Tiamat became impatient with the Dragonfall War, it was believed she brokered a deal with Maglubiyet to quickly marshal armies of goblinoids, intent on scouring the Material Plane of metallic dragons one world at a time.<ref name=\"D359p68\">{{Cite dragon/359/1d20 Villains: D&D's Most Wanted; Preferably Dead|68}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:274`

**Wiki, Bane (Modern Times, the exarch period).** The sentence cites Forgotten Realms Campaign Guide p.73 and Baldur's Gate: Descent into Avernus p.231.

> "For a period Bane was ascendant and managed to draw Maglubiyet into his command, claiming lordship over him and reducing him to an exarch,<ref name=\"FRCG-pg73\">{{Cite book/Forgotten Realms Campaign Guide|73}}</ref> only to later lose this power after the Second Sundering and be reduced himself to a shadow of his former power.<ref name=\"dia-p231\">{{Cite book/Baldur's Gate: Descent into Avernus|231}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:274`

### Field 6. Campaign and published-adventure mentions

**Campaign.** No campaign file names Maglubiyet. The bundle's `campaign-hits.txt` is empty. A targeted grep of `campaign/` for "Maglubiyet", "Mighty One", "Conquering God", "Army of Immortals", "goblin god" and "goblinoid pantheon" finds nothing.

**Published adventure, WDMM, Level 3 Sargauth Level, "Legion of Azrok".**

> "Azrok, the son of a hobgoblin warlord, was born blind. Such a curse would ordinarily have spelled his doom in hobgoblin society, but Azrok's mother was a sorcerer, and she refused to allow her son's misfortune to dictate his destiny. She crafted a {@item dagger of blindsight|WDMM}, which young Azrok used to defend himself and perceive his surroundings. The dagger allowed Azrok to become the powerful soldier and leader he was fated to be, and he was quickly promoted up through the ranks until none stood above him. Other goblinoids believed he was blessed by Maglubiyet, the great god of war. Azrok wisely hid the true source of his \"godsight\" to perpetuate the myth."
>
> — `/home/user/waterdeep/sources/adventure-wdmm.json:7426`

**Published adventure, WDMM, Level 3, area 21s "Azrok's War Chest" (a shrine turned treasury).**

> "{@b Statuette}. Atop the altar rests a 7-inch-tall statuette of Maglubiyet, the goblin god of war, carved from blood-red stone. It is not valuable."
>
> — `/home/user/waterdeep/sources/adventure-wdmm.json:11203`

**Published adventure, WDMM, Level 14 Arcturiadoom, Doomcrown's section.**

> "A devout follower of the godslayer Maglubiyet, Doomcrown wants fire giants to ascend to the top of the giant ordning, envisioning their brutal tyranny sweeping across Faerûn. He expects to play an important role in {@creature Emberosa|WDMM}'s ascension and conquest, and he dreams of ruling what remains of the High Forest once the elves and other forest denizens are purged and the trees are reduced to ashen spines."
>
> — `/home/user/waterdeep/sources/adventure-wdmm.json:37720`

**Published adventure, WDMM, Level 14 Arcturiadoom, area 9c "Hobgoblin Phalanx".**

> "Here, a {@creature hobgoblin captain} has marshaled a phalanx of twenty {@creature Hobgoblin||hobgoblins}. The captain faces east and recites a liturgy in Goblin to the dread god Maglubiyet while the soldiers stand at attention in two rows of ten, facing west. As she reaches dramatic peaks in the liturgy, the hobgoblins grunt and nod approvingly, banging their fists on their armor."
>
> — `/home/user/waterdeep/sources/adventure-wdmm.json:39503`

### Field 7. Conflicts and not found

**Alignment.** The PHB 2014 entry and the wiki's 5e entry agree (lawful evil). The wiki's 3e and 2e columns differ.

> `| alignment3e         = [[Neutral Evil]]`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:65`

> `| alignment2e         = [[Lawful evil]]`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:80`

Brackets removed. The PHB entry gives `- alignment: ['L', 'E']` (`maglubiyet/5etools.md:3`).

**Plane.** The wiki's 1e column gives the Nine Hells, while its 5e and 3e columns give Acheron.

> `| homeplane1e         = The Nine Hells`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:96`

> `| homeplane5e         = Acheron`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:38`

**Domains.** The PHB 2014 entry gives War and Order. The wiki's 3e column gives eight domains and none of them is named Order.

> `| domains3e           = Competition, Chaos, Destruction, Evil, Planning, Strength, Trickery, Tyranny`
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:72`

Brackets removed: the source reads `[[Competition domain|Competition]], [[Chaos domain|Chaos]], [[Destruction domain|Destruction]], [[Evil domain|Evil]], [[Planning domain|Planning]], [[Strength domain]], [[Trickery domain|Trickery]], [[Tyranny domain]]`.

**Symbol.** The PHB 2014 entry reads `- symbol: Bloody axe`. The wiki's 5e entry adds "headsman's", quoted in Field 1. The 2e entry reads `symbol2e = Bloody [[axe]]`.

**Not found (Maglubiyet).**
- 5etools `worshipers` field: none. PHB 2014 has no worshipers field.
- Holy days: wiki infobox fields are blank (`maglubiyet/wiki.txt:46`, `:76`).
- Messengers: none in any source.
- Church: the wiki links to a "Church of Maglubiyet" article (`maglubiyet/wiki.txt:228`, `{{Main|Church of Maglubiyet}}`). That article is not in the bundle.
- Waterdeep temple or shrine: none (Q1).
- Campaign files: none (see Field 6).
- Searched for Maglubiyet, Mağlubiyet, Maglubiyan, Fiery-Eyes, Mighty One, Conquering God, Army of Immortals, Battle Lord, goblin god, goblinoid god, goblinoid pantheon, Clangor, Grashmog in `campaign/` (all files), both adventure JSON files, and the Maglubiyet bundle.

### Answers (Maglubiyet)

**Q1. Which temples or shrines the adventure or campaign files place in Waterdeep, and in which ward.**

None. The WDH table has no goblinoid row (caption at `sources/adventure-wdh.json:30910`). No campaign file places a Maglubiyet temple or shrine in the city.

Undermountain is below the city and "outside city jurisdiction". The lore file says so:

> "- **Undermountain** (below the city): the Yawning Portal well drops to Level 1; Skullport is three levels down; outside city jurisdiction"
>
> — `/home/user/waterdeep/campaign/setting/waterdeep-lore.md:21`

The WDMM's Maglubiyet statuette sits in Azrok's War Chest, on Level 3 (Sargauth Level). The level heading (`sources/adventure-wdmm.json:7389`) reads `"name": "Level 3: Sargauth Level",`. The area heading is `"name": "21s. Azrok's War Chest",` (`sources/adventure-wdmm.json:11191`). The Hobgoblin Phalanx, where the liturgy is read, is on Level 14, Arcturiadoom (`sources/adventure-wdmm.json:37680` and `:39499`). Neither is in a Waterdeep ward.

Clangor, the Maglubiyet temple-city (Grashmog), is on the Acheron plane, not in Waterdeep:

> "Clangor also contained the temple-city and capital fortress of Maglubiyet known as Grashmog, the Heart of Battle."
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:166`

**Q2. Which campaign NPC, faction or quest uses the power.**

No campaign file uses this power. No goblin, hobgoblin or bugbear notable figure appears in `campaign/setting/notable-figures/`. The only goblinoid NPCs in the published Undermountain material are Azrok's Legion and Doomcrown. Neither is in the campaign.

**Q3. Which lines in wiki.txt mention Waterdeep.**

One line, a citation. It is the wiki's note on Doomcrown:

> "* [[Doomcrown]], a hobgoblin devotee of Maglubiyet who envisioned the brutal tyranny of the [[fire giant]]s sweeping across [[Faerûn]] and their ascension to the top of the [[Ordning]]. He dreamt of ruling the remnants of the [[High Forest]] once the trees were reduced to burnt spines and the forest-dwellers were eradicated.<ref name=\"WDMM5e-p179\">{{Cite book/Waterdeep: Dungeon of the Mad Mage|179}}</ref>"
>
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:258`

The text names the Waterdeep: Dungeon of the Mad Mage book, not the city.

### Cross-references (Maglubiyet)

- `/home/user/waterdeep/sources/adventure-wdmm.json:11191`: `"name": "21s. Azrok's War Chest",`
- `/home/user/waterdeep/sources/adventure-wdmm.json:11196`: `What was once a shrine to the dwarven pantheon is now Azrok's treasury. The room contains the following:`
- `/home/user/waterdeep/sources/adventure-wdmm.json:11201`: `{@b Toppled Idols}. Dozens of stone idols of dwarven gods have been toppled from their bases and smashed on the floor.`
- `/home/user/waterdeep/sources/adventure-wdmm.json:7389`: `"name": "Level 3: Sargauth Level",`
- `/home/user/waterdeep/sources/adventure-wdmm.json:37680`: `"name": "Level 14: Arcturiadoom",`
- `/home/user/waterdeep/sources/adventure-wdmm.json:39499`: `"name": "9c. Hobgoblin Phalanx",`
- `/home/user/waterdeep/sources/adventure-wdmm.json:7403` (the Sargauth Level section header paragraph, which ends with "...the goblinoids and drow vie for control of these ruins, which were previously inhabited by the Netherese and the Melairkyn dwarves."): the line names no god. It is listed for its context only.
- `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/maglubiyet/wiki.txt:228`: `:{{Main|Church of Maglubiyet}}`

---

## CROSS-POWER NOTES

- **Ward names.** `campaign/setting/waterdeep-lore.md:18` says "South Ward" (quoted in Yondalla Field 7). The Doom Raiders event and the WDH Helm's Hall row say "Southern Ward" (`sources/adventure-wdh.json:30940`). The orchestrator will need to pick one.
- **"All deities" row.** `sources/adventure-wdh.json:30923-30925` names Holyhands House in the North Ward for "All deities". This is the only row that could cover these powers. It names none of them, so I have not treated it as a temple for any power.
- **Undermountain.** Maglubiyet's and Moradin's published-adventure hits are in Undermountain (WDMM), which the lore file places below the city and outside city jurisdiction (`campaign/setting/waterdeep-lore.md:21`). They are not in a Waterdeep ward.

---

## NOT READABLE

None. All files in the bundles and both adventure JSON files opened. `docs/index.html:1104` (Larkhaven) was not read, as noted above.

---

## SAVE

This report is also written to `/home/user/waterdeep/docs/plans/setting-compendium-research-notes/pass2/batch-k1-moradin-yondalla-maglubiyet.md`.
