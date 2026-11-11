# Pass 2 research report, batch 00: Tyr, Siamorphe, Zariel

Brief: `/home/user/waterdeep/docs/plans/setting-compendium-pass2-brief.md`, section "Researcher report (per power)". Model page read: `/home/user/waterdeep/campaign/setting/deities/asmodeus.md`.

## Method and conventions

- Bundles read in full for each power: 5etools.md, wiki.txt, campaign-hits.txt, adventure-hits.txt. Folder root: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/`. So `tyr/5etools.md:2` means `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tyr/5etools.md`, line 2.
- Repo paths in citations are relative to `/home/user/waterdeep/`. So `campaign/gazetteer/waterdeep/castle-ward.md:66` is `/home/user/waterdeep/campaign/gazetteer/waterdeep/castle-ward.md`, line 66.
- Major Temples table read at `sources/adventure-wdh.json` lines 30908 to 30998 (caption at line 30910).
- Targeted Grep of `campaign/` and both adventure JSON files for aliases. Lines the bundles did not carry are marked **(not in bundle)**.
- Not read, by instruction: the Alexandrian PDFs, `sources/SOURCE_GUIDE.md`, and the Appendix markdown files. Retired chapter files are cited only as conflict pointers and marked retired.
- Wiki quotes: `[[ ]]` link brackets removed. For a piped link the visible text is kept, so `[[Order domain|Order]]` appears as `Order`. Everything else is exact, including `{{...}}` templates and `<ref>` tags.
- Wiki line numbers are true file lines. Tyr and Zariel were read from line 1. The Siamorphe read started at offset 0, so its displayed numbers were one low; this report uses the true numbers (for example, the Chapel paragraph is line 129). Lines 107, 119, 121 and 129 were confirmed with Grep -n.
- Each field carries up to six quotes. Further matching lines are copied under "Further lines".
- Ranking applied per brief: campaign files, published adventure, 5etools, then wiki.

---

## 1. TYR

Bundle sizes: 5etools.md has four entries (FRHoF, PHB 2014, PHB Norse, SCAG). wiki.txt is 318 lines and was read whole. campaign-hits.txt has 92 lines. adventure-hits.txt has 16 lines.

### Field 1: Identity

**5etools, FRHoF p.126 (2024-era canon, per brief)**
> ## Tyr | source FRHoF p.126 | pantheon Faerûnian
> - altNames: ['The Evenhanded', 'Grimjaws', 'The Maimed God']
> - title: God of justice
> - worshipers: Judges, law enforcers, lawyers, Paladins
> - plane: Mount Celestia (Lunia)

— `tyr/5etools.md:1-5`

**5etools, SCAG p.21 (2014; the only 5etools source of alignment, domains and symbol for this power)**
> ## Tyr | source SCAG p.21 | pantheon Faerûnian
> - altNames: ['Grimjaws', 'The Maimed God', 'The Evenhanded']
> - title: God of justice
> - alignment: ['L', 'G']
> - domains: ['War', 'Order']
> - symbol: Balanced scales resting on a warhammer

— `tyr/5etools.md:30-35`

**5etools, PHB p.294 (2014; repeats the SCAG values)**
> ## Tyr | source PHB p.294 | pantheon Forgotten Realms
> - title: God of justice
> - alignment: ['L', 'G']
> - domains: ['War', 'Order']
> - symbol: Balanced scales resting on a warhammer

— `tyr/5etools.md:14-18`

**Wiki lead (epithets, alternate names, pantheon; each citation is in the quote)**
> '''Tyr''' ({{Pronounce|TEER|refs=<ref name="FRCS-CotR-pp15-16" /><ref name="F&A-pp169-170" /><ref name="FRCS3e-pp253-254" /><ref name="F&P-pp79-82" />}}), known as '''Anachtyr''' in Calimshan,<ref name="F&A-pp169-170" /><ref name="EotSS-p55" /> was the lawful good greater god of law and justice in the Faerûnian pantheon<ref name="FRCS-CotR-pp15-16" /><ref name="FRCS2e-RtR-p50" /><ref name="SCAG-p21" /><ref name="SCAG-p40" /><ref name="FRA-p35" /><ref name="F&A-pp169-170" /><ref name="FRCS3e-pp253-254" /><ref name="F&P-pp79-82" /><ref name="F&P-pp222-223" /><ref name="FRCS3e-pp234-235" /> and leader of the coalition of deities known as the Triad.<ref name="F&A-pp169-170" /><ref name="FRCS3e-pp253-254" /> The titles of '''The God of Justice''' allegorized his nature to his followers.<ref name="FRCS2e-RtR-p50" /><ref name="SCAG-p40" /> He bore his title of the '''Maimed God''' for his missing right hand,<ref name="FRCS3e-pp253-254" /> lost in an act of bravery and self-sacrifice<ref name="SCAG-p40" /> and his title of '''the Even-Handed''' referred to his position as the god of justice, though was also seen as dark humor.<ref name="FRCS-CotR-pp15-16" /> The wounded eyes of the '''Blind Overlord'''<ref name="F&A-pp169-170" /> meanwhile were seen as symbolic of "blind justice" and the cost that sometimes came with living a lawful life.<ref name="F&P-pp79-82" /> His symbol however, balanced scales upon a warhammer, truly symbolized his nature;  justice upheld with armed vigilance and benevolent might.<ref name="F&A-pp169-170" />

— `tyr/wiki.txt:139` (cites in the quote: Cyclopedia of the Realms, FRCS 2e, FRCS 3e, SCAG pp.21 and 40, Faiths & Avatars, Faiths & Pantheons, Forgotten Realms Adventures, Empires of the Shining Sea)

**Wiki infobox, 5e rows (the refs on line 67 cite SCAG p.21, SCAG p.40, PHB 5e pp.63 and 294, and Guildmasters' Guide to Ravnica pp.25-26)**
> | power5e             = Deity
> | alignment5e         = Lawful good
> | symbol5e            = Balanced scales resting on a warhammer
> | homeplane5e         =
> | realm5e             =
> | serves5e            =
> | servedby5e          =
> | portfolio5e         = Justice
> | domains5e           = Order, War
> | worshipers5e        = Judges, knights

— `tyr/wiki.txt:52-61`

**Wiki infobox, 3e domains row (cites: Dragon 355 and Dragon 323, as named in the refs)**
> | domains3e           = Good, Knowledge, Law, Patience,<ref name="D-355-p26">{{Cite dragon/355/Seven Saintly Domains|26}}</ref> Pride,<ref name="D-323-p65">{{Cite dragon/323/Seven Deadly Domains|65}}</ref> Retribution, Temperance,<ref name="D-355-p26" /> War

— `tyr/wiki.txt:91`

### Field 2: Edict or core tenet

No source gives an edict. The nearest statements are these.

**5etools, FRHoF (credo)**
> Tyr's followers devote themselves to achieving justice, righting wrongs, and delivering vengeance. This devotion isn't concerned with equality or fairness, but rather discovering the truth and punishing the guilty. Those who favor Tyr are stiff necked about theology and laws, evaluating actions according to a rigid moral code.
> Tyr's credo of lawfulness and honesty is demanding, and his priests remind the faithful not to judge too harshly those who fail to live up to Tyr's standards. If Tyr's commands were easily followed, they wouldn't be worth obeying.

— `tyr/5etools.md:9-10`

**Wiki, Personality (cites: FRCS 3e, On Hallowed Ground, FRCS 2e, Faiths & Avatars)**
> Tyr was strong-spirited and noble.<ref name="FRCS3e-pp253-254" /> He was considered the bravest and the most honorable of all the Aesir of the Norse pantheon.<ref name="OHG-pp148-149" /><ref name="D&D3e-pp195-197">{{Cite book/Deities and Demigods|195-197}}</ref> He was primarily concerned with the punishment of wrong-doers and the general furthering of law and good in the world.<ref name="FRCS2e-RtR-p50" /><ref name="F&A-pp169-170" /> Tyr hated duplicity, trickery, rule-breaking, and wanton destruction.<ref name="F&A-pp169-170" /> He likewise hated lies and the breaking of oaths and was disgusted by persons who earned from such things.<ref name="OHG-pp148-149" /> For his own part, he never would break a promise.<ref name="OHG-pp148-149" />

— `tyr/wiki.txt:154`

**Wiki, Personality (cites: Faiths & Pantheons pp.79-82)**
> Tyr urged the establishment of moral and ethical codes for sentient beings in all lands.<ref name="F&P-pp79-82" />

— `tyr/wiki.txt:160`

### Field 3: Portfolio and Areas of Concern

No source gives Areas of Concern. The portfolio is Justice in each edition the wiki lists.

> | portfolio5e         = Justice

— `tyr/wiki.txt:59`

> | portfolio3e         = Justice

— `tyr/wiki.txt:90`

> | portfolio2e         = Justice

— `tyr/wiki.txt:107`

**Wiki, Powers (cites: Faiths & Pantheons pp.79-82)**
> As god of justice, Tyr could foretell any injustice up to six months before it occurred and felt the pang of that injustice for six months afterward.<ref name="F&P-pp79-82" />

— `tyr/wiki.txt:168`

### Field 4: Worship (Waterdeep specifics first)

**Adventure, Major Temples of Waterdeep (caption at line 30910; columns "Deity or Deities", "Temple Name", "Location")**
> "Tyr",
> "Halls of Justice",
> "Castle Ward"

— `sources/adventure-wdh.json:30988-30990` (the row runs from line 30987 to line 30991)

**Campaign, waterdeep-lore (Religion bullet)**
> - Halls of Justice, the temple of Tyr, in the Castle Ward (Justice; City Watch captain is a worshiper)

— `campaign/setting/waterdeep-lore.md:37`

**Campaign, castle ward gazetteer**
> **Halls of Justice** — Temple of Tyr and courts

— `campaign/gazetteer/waterdeep/castle-ward.md:66`

**Adventure, Order of the Gauntlet recruitment (first sentence of the paragraph)**
> If the party includes one or more likely recruits, Savra Belabranta (NG female Tethyrian human {@creature knight}) visits the characters' residence and invites them to the Halls of Justice, the temple of Tyr (located west of the Market in the Castle Ward), where they can be sworn into the order.

— `sources/adventure-wdh.json:3949`

**Wiki, holy days (3e and 2e rows; identical)**
> | holy days3e         = 1{{st}}, 13{{th}}, & 22{{nd}} of every month
> | holy days2e         = 1{{st}}, 13{{th}}, & 22{{nd}} of every month

— `tyr/wiki.txt:96` and `tyr/wiki.txt:111`. The 5e holy days row is blank (`tyr/wiki.txt:64`).

**5etools, FRHoF (messengers)**
> Tyr appears as a noble warrior without his right hand, which he lost to Kezef the Chaos Hound in an act of bravery and sacrifice. His eyes are wrapped in cloth, his blindness signifying that justice applies evenly to all. Weary of the foolishness of mortals, Tyr seldom appears or speaks directly to mortals, instead sending an awakened {@creature Mastiff|XMM} as an emissary or sending the sound of a war gong or a choir.

— `tyr/5etools.md:8`

**Further lines (Field 4):**
> Many orders of knighthood devote their lives to Tyr, including the Knights of Holy Judgment and the Knights of the Merciful Sword. Such knights—as well as judges, priests, and others who worship Tyr—wear thin strips of diaphanous cloth over their eyes as a symbol of their faith.

— `tyr/5etools.md:11` (FRHoF; knighthoods and symbol)

> Among Tyr's worshipers were judges, lawyers, magistrates, the oppressed, paladins, and police.<ref name="F&P-pp79-82" />

— `tyr/wiki.txt:193` (brackets removed; cites Faiths & Pantheons pp.79-82)

> The highly organized church of Tyr was strong in the more civilized lands of the Realms. They were known for never refusing service or aid to the faithful when they were in distress.<ref name="FRCS3e-pp253-254" /> The blind god ruled over law and justice, encouraging valiant acts from his followers and relentlessly pursuing oathbreakers.<ref name="BG3">{{Cite game/Baldur's Gate III}}</ref> Followers of Tyr were expected to show fairness, wisdom, and kindness to the innocent.<ref name="F&P-pp79-82" /> Tyrrans never enforced an unjust law.<ref name="F&P-pp79-82" />

— `tyr/wiki.txt:197` (cites FRCS 3e, Baldur's Gate III, Faiths & Pantheons)

> *Ingrar Welven, also known as the Voice of Tyr,<ref name="UA-p85">{{Cite book/Uneasy Alliances|85|6}}</ref> was a pirate from the Utter East, who became possessed by the Maimed God after himself being maimed by a fiend. With powers granted by Tyr, Ingrar was tasked with destroying the Fallen Temple and bring long-lost reverence of his god back to the Five Kingdoms in the late-14{{th}} century DR.<ref name="UA-p76-77">{{Cite book/Uneasy Alliances|76-77|5}}</ref>

— `tyr/wiki.txt:202` (the only Chosen the wiki names; under the heading "Chosen of Tyr", line 201)

> Besides his avatar, Tyr might send an intelligent war dog as a representative, or he might use a resounding gong, a choir of male voices, or a floating warhammer to express his will.<ref name="F&A-pp169-170" /><ref name="F&P-WE-DD&D-p15">{{Cite web enhancement/Deity Do's and Don'ts|15}}</ref>

— `tyr/wiki.txt:151` (wiki messenger; cites Faiths & Avatars and Deity Do's and Don'ts)

Omens: none found (see Not found).

### Field 5: Relations and origin (wiki; each quote carries its own cites)

**Origin, Norse (wiki)**
> An interloper deity,<ref name="FRCS3e-pp253-254" /><ref name="F&P-pp79-82" /> Tyr, known as the '''One-Handed''' across the Outer Planes,<ref name="OHG-pp148-149" /> was the same power as the god of the same name in the Norse pantheon,<ref name="OHG-pp148-149" /><ref name="OHG-pp178,181" /><ref name="PCS-TPbP" /><ref name="FRCS1e-CotR-p18">{{Cite book/Forgotten Realms Campaign Set/Cyclopedia of the Realms|18}}</ref><ref name="S-ADDAiS-CoAS-pp16,18">{{Cite book/Spelljammer: AD&D Adventures in Space/Concordance of Arcane Space|16,18}}</ref> although in the Realms he was worshiped only as a god of justice and not as a god of war.<ref name="FRCS-CotR-pp15-16" /> As the only Norse power worshiped in Faerûn,<ref name="FRCS1e-CotR-p18" /><ref group="note">While sometimes counted among the Norse pantheon, the gods Surtur and Thrym properly belonged to the rival Giant pantheon, according to other sources.</ref> if a cleric of the Norse pantheon came to Toril from another world, they would be granted spells through Tyr.<ref name="S-ADDAiS-CoAS-pp16,18" />

— `tyr/wiki.txt:141`

**Triad (wiki)**
> Tyr was the head of the group of deities known as the Triad. The two other gods who made up the Triad were Ilmater and Torm.<ref name="F&A-pp169-170" /><ref name="FRCS3e-pp253-254" /><ref name="F&P-pp79-82" /> Torm served as Tyr's war commander<ref name="F&P-pp79-82" /> and was known as the "good right hand of Tyr."<ref name="SCAG-p39">{{Cite book/Sword Coast Adventurer's Guide|39}}</ref>

— `tyr/wiki.txt:183` (cites Faiths & Avatars, FRCS 3e, Faiths & Pantheons, SCAG p.39)

**Other relations (wiki)**
> Among the greater deities of Faerûn, Tyr was the only one of lawful good alignment.<ref name="FRCS2e-RtR-p50" /> Along with the Triad, Tyr was close to Lathander.<ref name="F&A-pp169-170" /><ref name="FRCS3e-pp253-254" /> He opposed the deities Bane, Bhaal, Cyric, Mask, Talona, and Talos.<ref name="F&A-pp169-170" /><ref name="FRCS3e-pp253-254" /><ref name="F&P-pp79-82" />

— `tyr/wiki.txt:185` (cites FRCS 2e, Faiths & Avatars, FRCS 3e, Faiths & Pantheons)

**Procession of Justice (wiki)**
> Tyr, in his most recent form, first made a major historical impact on the world of Toril in a campaign to pacify the remnants of the fallen empire of Jhaamdath in the {{YearlinkName|-247}}. This was known as the Procession of Justice, in which the god himself appeared on Toril by ''portal'' near future Alaghôn in Turmish to lead a host of ten scores of archons against the chaotic and evil forces arrayed in the Vilhon Reach, in the remains of the fallen empire.<ref name="F&P-pp79-82" /><ref name="TGHotR-p52">{{Cite book/The Grand History of the Realms|52}}</ref>

— `tyr/wiki.txt:220` (cites Faiths & Pantheons pp.79-82; The Grand History of the Realms p.52)

**1384, Tyr and Siamorphe (wiki, Tyr page)**
> In the {{YearlinkName|1384}}, shortly before the catastrophic events of the Spellplague, Tyr and Siamorphe, who then dwelt in the House of the Triad, had a great disagreement over a battle between Tethyrian and Calishite forces. The argument was so severe that Siamorphe left the House of the Triad to make her realm with Sune in Brightwater. Tyr sent Helm as a messenger to Sune to explain his position, and Sune tried to act as a peacemaker. As the goddess of love, she proposed a marriage between Tyr and Tymora as a way to restore balance to the Celestial Planes. Tyr agreed and began a formal courtship with the goddess of good fortune.<ref name="TGHotR-p159">{{Cite book/The Grand History of the Realms|159}}</ref>

— `tyr/wiki.txt:236` (cites The Grand History of the Realms p.159)

**Abdication (wiki; see Conflicts C5)**
> After imprisoning Cyric, Tyr abdicated his godhood and granted Torm all his deific power, because the Even-Handed had lost faith in himself and in his ability to lead and judge. Tyr counseled all of his followers to offer their allegiance to Torm.<ref name="TCM-p241">{{Cite book/The Crystal Mountain/MMP|241}}</ref> Tyr's portfolio of justice was subsequently absorbed by Bahamut, who later became a subservient deity of Torm.<ref name="DR381-p92">{{Cite dragon/381/Channel Divinity: Champions of Torm|92}}</ref>

— `tyr/wiki.txt:244` (cites The Crystal Mountain / MMP p.241; Dragon 381 p.92)

### Field 6: Campaign and published-adventure mentions

**Adventure, Hlam and the Order of the Even-Handed (Mount Waterdeep)**
> This venerable human monk lives in a cave halfway up the side of Mount Waterdeep. {@creature Hlam|wdh} is the grand master of the Order of the Even-Handed, a small monastic group devoted to Tyr. Would-be students periodically visit him to learn the Way of the Sacred Fists, which combines cleric magic and monk training. They usually return to the city confused, bruised, and not inclined to visit again.

— `sources/adventure-wdh.json:32129`

**Adventure, Lady Gondafrey (gargoyle cell at Kolat Towers)**
> Duhlark Kolat long ago trapped a magical experiment in this cell: a {@creature gargoyle} that has been imbued with the personality of a human knight of Tyr (god of justice) named {@creature Lady Gondafrey|wdh}. This gargoyle has an Intelligence score of 10 and an alignment of lawful good. It speaks Common, and its face looks more humanoid than gargoyle. {@creature Manshoon|WDH} is amused by the creature, so he keeps it alive but locked in the cell.

— `sources/adventure-wdh.json:28504`

**Campaign, Kolat Towers structure**
> Lady Gondafrey, then a City Watch captain and a knight of Tyr, attempted to breach the towers in 1379 DR while investigating Duhlark's suspected dealings with Xanathar's Guild. The force field repelled her. The arcane lock on the front door defeated her thieves. She attempted a third entry through the bridge on the third floor and was captured. Duhlark offered her a choice: remain imprisoned, or swear never to speak of what she had seen. She refused the oath. She has been in the towers since 1379 DR — 113 years.

— `campaign/structure/arc-i-kolat-towers.md:11` (arc-i is the active structure doc; the Kolat Towers quest journal does not exist yet)

**Campaign, Order of the Gauntlet (organization page)**
> The Waterdeep chapter is small. It is Savra, a clerk's office in the east annex of the Halls of Justice, and a rotation of about a dozen Knights and Priests who answer to her. The Halls of Justice is the temple of Tyr in the Castle Ward, and the priests of the Triad help the Order without belonging to it.

— `campaign/setting/organizations/04-order-of-the-gauntlet.md:19`

**Campaign, Isaldric Veyne (Righteous Hand investiture)**
> Isaldric Veyne (Lawful Good, Human, he/him) :: the high priest of Tyr in Waterdeep. He is a tall man in his seventies with white hair and silver scales on his chest.

— `campaign/quests/faction-events/order-of-the-gauntlet/r50-righteous-hand/ev-01-righteous-hand.md:55`

**Campaign, Hlam (Notable Figures)**
> **Relationships.** Hlam is the grand master of the Order of the Even-Handed (devoted to Tyr), a staunch ally of the Order of the Gauntlet, and an old acquaintance of Aurinax the gold dragon. PCs who negotiate with Aurinax in Hlam's presence gain advantage on Persuasion checks.

— `campaign/setting/notable-figures/independents-allies/14-hlam.md:26`

**Further lines (Field 6):**
> If the party marked **Order Recognized** in Order of the Gauntlet Mission 6 ("The Writ and the Weight"), the Halls of Justice have formally recognized the party as Order associates.

— `campaign/structure/arc-j-vault-of-dragons.md:49` (Vault of Dragons; **not in bundle**; found by Grep for the Tyr aliases)

> The informant web is real. It is made up of dockhands, fences, two clerks at the Halls of Justice, and Tashlyn's reports from her post at the South Gate, and its information on Xanathar's Guild is good.

— `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:24` (**not in bundle**; the second sentence is quoted here)

> You can also hire an advocate at the Halls of Justice to file a petition, which will cost you fifty gold, or you can go back to Sergeant Dunfell with something concrete.

— `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:162` (**not in bundle**)

> | **Order of the Gauntlet** | Savra Belabranta visits Trollskull in person; no advance invitation | Any character in no other faction; a Cleric or Paladin class, an Acolyte, Guard or Soldier background, or worship of Helm, Torm or Tyr only decides whom Savra addresses first |

— `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:28`

> > Hlam serves Tyr, the Even-Handed, and sees farther than my agents do. He dislikes visitors, so go up, listen, and bring back what he says.

— `campaign/quests/faction-events/force-grey/m01-consulting-hlam/ev-01-consulting-hlam.md:56`

> | **Chevall** | Granted when the member swears the oath. Savra vouches for the member at any temple of Tyr, Helm or Torm in Waterdeep. Each temple casts *Cure Wounds* on the member once a day and gives a bed for up to three nights in a row. If the Watch arrests the member on a minor charge, Savra puts in a good word once a tenday and the Order's clerk tends the member's affairs. The member can also ask Brother Haldric Wence at the Halls of Justice to arrange *Speak with Dead* on a body the Watch holds, once for each body. |

— `campaign/guides/factions/05-order-of-the-gauntlet.md:64`

> The east annex stands behind the main hall of the Halls of Justice, and its side door opens onto a short passage with one lamp burning. Savra leads you past a locked door marked for the armory to a narrow chapel at the end. A wooden statue of Tyr stands against the far wall with its right hand carved away at the wrist. Savra lights a second lamp from the first, sets it on the ledge and turns to face you.

— `campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:106`

> Father Corwen Thale (Lawful Good, Human, he/him) :: a gray-haired priest of Tyr with a calm, gravelly voice and a missing left hand. He has presided over the Order's oaths for twenty years.

— `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:242`

> - **Sister Ilvane Haste** (Temple of Tyr): the priest of the Halls' bench who reads the *Zone of Truth* scroll.

— `campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/overview.md:56`

> - **Brother Haldric Wence** (Order of the Gauntlet): the door-warden of the Halls of Justice.

— `campaign/quests/faction-events/order-of-the-gauntlet/m06-the-writ-and-the-weight/overview.md:72`

> *Half-orc cleric of Tyr, lawful good*. Stat block: **Priest**.

— `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:6`

> **Motivations.** Lady Gondafrey wants to continue her duty as a knight of Tyr from within the gargoyle's body, bring Duhlark Kolat's crimes to light, and avoid the days when the gargoyle wins.

— `campaign/setting/notable-figures/independents-allies/18-lady-gondafrey.md:16`

> Any temple of Tyr, Helm or Torm in Waterdeep treats a member as a friend of the Order. A priest casts *Cure Wounds* on the member and gives the member a bed for the night.

— `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:203`

WDMM (Undermountain, not a Waterdeep ward):

> Over a century ago, {@creature Fidelio|WDMM} began his campaign to single-handedly rid Undermountain of evil, foolishly believing that Tyr would not let him perish.

— `sources/adventure-wdmm.json:42499` (Fidelio, paladin of Tyr; ghost on the Obstacle Course)

> Aryx was sent by Tyr, the god of justice, to talk some sense into {@creature Fazrian|WDMM}, the fallen planetar on {@adventure level 21|WDMM|21}.

— `sources/adventure-wdmm.json:61188`

Setting text (not a temple):

> It is a city of laws molded by Tyr's spirit of justice.

— `sources/adventure-wdh.json:30514`

### Per-power answers (Tyr)

**(1) Temples and shrines in Waterdeep, and ward**
- Halls of Justice, the temple of Tyr, Castle Ward. Quoted in Field 4 (adventure table row at `sources/adventure-wdh.json:30988-30990`; `campaign/setting/waterdeep-lore.md:37`; `campaign/gazetteer/waterdeep/castle-ward.md:66`; `sources/adventure-wdh.json:3949`).
- A narrow chapel of Tyr at the end of the Halls' east annex, with a wooden statue of Tyr. Quoted in Field 6 (`campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:106`).
- The cave of Hlam, grand master of the Order of the Even-Handed, "halfway up the side of Mount Waterdeep" (`sources/adventure-wdh.json:32129`). No ward is given for Mount Waterdeep.
- The wiki places no Tyr temple in Waterdeep.

**(2) Campaign NPCs, factions and quests using Tyr**
- Faction, Order of the Gauntlet: `campaign/setting/organizations/04-order-of-the-gauntlet.md:19` (Field 6).
- Savra Belabranta: named in the Chevall row, `campaign/guides/factions/05-order-of-the-gauntlet.md:64` (Field 6).
- Father Corwen Thale, priest of Tyr: `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:242` (Field 6).
- Isaldric Veyne, high priest of Tyr: `campaign/quests/faction-events/order-of-the-gauntlet/r50-righteous-hand/ev-01-righteous-hand.md:55` (Field 6).
- Brother Haldric Wence, door-warden: `campaign/quests/faction-events/order-of-the-gauntlet/m06-the-writ-and-the-weight/overview.md:72` (Field 6).
- Sister Ilvane Haste, priest of Tyr: `campaign/quests/faction-events/order-of-the-gauntlet/m04-spined-devils-in-twelvedog-court/overview.md:56` (Field 6).
- Sister Valdra, half-orc cleric of Tyr: `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:6` (Field 6).
- Hlam, Order of the Even-Handed: `campaign/setting/notable-figures/independents-allies/14-hlam.md:26` (Field 6).
- Lady Gondafrey, knight of Tyr in the gargoyle: `campaign/setting/notable-figures/independents-allies/18-lady-gondafrey.md:16` (Field 6).
- Quests: Trollskull Alley (`campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:28`); Kolat Towers (`campaign/structure/arc-i-kolat-towers.md:11`); Vault of Dragons (`campaign/structure/arc-j-vault-of-dragons.md:49`); Force Grey Mission 1 (`campaign/quests/faction-events/force-grey/m01-consulting-hlam/ev-01-consulting-hlam.md:56`); Doom Raiders (`campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:162`). All quoted above.

**(3) Wiki lines that mention Waterdeep**
- Line 246, cited only through the template "Waterdeep: Dungeon of the Mad Mage" (p.293): "At some point, Tyr sent the deva Ayrx into Undermountain to try and talk sense into Fazrian. Unfortunately, Halaster was able to capture Aryx, and trapped her in a shield in his Lair.<ref name="WDMM-p293">{{Cite book/Waterdeep: Dungeon of the Mad Mage|293}}</ref>" — `tyr/wiki.txt:246` (brackets removed; the place named is Undermountain)
- Line 255, the Iltyr cult: "This ancient cult involved a number of Waterdhavian and Cormyrian nobles and even included some beholder and elven followers." — `tyr/wiki.txt:255` (sentence from the line; the rest of the passage covers the cult's secret veneration after Tyr's death, its hidden shrines and portraits, and its telepathic voice)

### Conflicts (Tyr)

**C1 Ward.** Current campaign and adventure place the Halls in the Castle Ward.
> - Halls of Justice, the temple of Tyr, in the Castle Ward (Justice; City Watch captain is a worshiper) — `campaign/setting/waterdeep-lore.md:37`
> - Major temples in Sea Ward: Tymora (Luck; popular with adventurers and criminals alike), Selûne (Moon; widely attended) — `campaign/setting/waterdeep-lore.md:36` (the current line 36 names no Tyr temple)

Stale design notes say line 36 lists Tyr:
> `waterdeep-lore.md:36` lists Tyr among the Sea Ward temples, which conflicts with the Castle Ward placement used here. — `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/design-notes.md:24`
> `waterdeep-lore.md:36` still puts Tyr's temple in the Sea Ward. — `campaign/quests/faction-events/order-of-the-gauntlet/r10-whitehawk/design-notes.md:21`

Retired (not used): "- Major temples in Sea Ward: Tyr (Justice; City Watch captain is a worshiper), Tymora (Luck; popular with adventurers and criminals alike), Selûne (Moon; widely attended)" — `campaign/structure/ch2-city-of-splendors.md:56`.

Ranking: the current campaign file and the adventure (both Castle Ward) outrank the design notes, which describe an older wording of line 36.

**C2 Worshipers.**
> - worshipers: Judges, law enforcers, lawyers, Paladins — `tyr/5etools.md:4` (FRHoF; ranks higher)
> | worshipers5e        = Judges, knights — `tyr/wiki.txt:61` (5e row)

**C3 Domains.** SCAG (2014) and the wiki 5e row agree on Order and War. The wiki 3e row lists eight domains (full row in Field 1, `tyr/wiki.txt:91`).
> - domains: ['War', 'Order'] — `tyr/5etools.md:34` (SCAG; the brief names this as the domain source)
> | domains5e           = Order, War — `tyr/wiki.txt:60` (5e)

Ranking: 5etools SCAG. The 3e list is tagged as 3e.

**C4 Home plane.**
> - plane: Mount Celestia (Lunia) — `tyr/5etools.md:5` (FRHoF; ranks higher)
> | homeplane3e         = House of the Triad — `tyr/wiki.txt:86` (3e row)

**C5 Status of Tyr (wiki, internal).**
> At some point between 1385 DR and 1479 DR, Tyr died fighting off a demonic invasion of the upper realms in an act of heroic sacrifice. Tyr's absence reinforced the role of Torm as the new master of Celestia.<ref name="FRCG-p77" /> — `tyr/wiki.txt:249`
> Tyr managed to return to life during the event known as the Second Sundering, in the 1480s DR.<ref name="SCAG">{{Cite book/Sword Coast Adventurer's Guide|51}}</ref> — `tyr/wiki.txt:252`

Also line 244 (Field 5). No campaign or adventure line states Tyr's status. The adventure and the campaign treat the Halls of Justice as a working temple.

**C6 Norse entry excluded.**
> ## Tyr | source PHB p.299 | pantheon Norse — `tyr/5etools.md:22` (not used; it is the Norse god)

### Not found (Tyr)

- Edict: no source states one (Field 2 gives the nearest text).
- Areas of Concern: none in the three 5etools Tyr entries or in the wiki.
- Omens: none found. Messengers appear only in `tyr/5etools.md:8` and `tyr/wiki.txt:151`.
- 5e holy days: `tyr/wiki.txt:64` is blank. The 2e and 3e holy days are in Field 4.
- Temples of Tyr in Waterdeep other than the Halls of Justice: none in campaign or adventure (alias grep).
- Chosen of Tyr in the campaign or the adventure: none in the bundle hits. The only Chosen the wiki names is Ingrar Welven (`tyr/wiki.txt:202`).
- Searches: campaign/ for `\bTyr\b|Halls of Justice|Even-Handed|Maimed God|Just God|Blind Overlord|Iltyr|Anachtyr|Justicar|Tyrran` (63 files); sources/adventure-wdh.json for `Halls of Justice|Even-Handed|Maimed God|Just God|Blind Overlord|Knights of Holy Judgment|\bTyr\b`, which returned lines 1403, 3942, 3949, 3950, 10443, 28504, 30514, 30988-30989 and 32129, all covered above; adventure-wdmm.json through the bundle (42495-42503, 61188).

---

## 2. SIAMORPHE

Bundle sizes: 5etools.md says there is no entry. wiki.txt is 153 lines (true line numbers used here). campaign-hits.txt has 62 lines. adventure-hits.txt has 8 lines. The bundle's campaign list missed `campaign/structure/arc-h-sea-maidens-faire.md:253` (**not in bundle**).

### Field 1: Identity

**5etools**
> No 5etools deities.json entry for this name.

— `siamorphe/5etools.md:1`

**Wiki title row**
> | title               = The Divine Right<ref name="F&P-p106-7"/>

— `siamorphe/wiki.txt:7`

**Wiki lead (cites in the quote: Powers and Pantheons pp.58-60; Faiths and Pantheons pp.106-7)**
> '''Siamorphe''' ({{Pronounce|SY|a|morf|refs=<ref name="F&P-p106-7"/>}} {{Pronounce|SEE|a|morf|refs=<ref name="P&P-p58-60"/>|alt=yes}}) was a demipower of nobles and nobles' divine right to rule. She encouraged them to rule well and wisely for the more common classes beneath them. Her worship was most common among the nobility and their councilors, especially among those who sought reasons to explain why they were in charge.<ref name="P&P-p58-60"/>

— `siamorphe/wiki.txt:105`

**Wiki 5e power and its source (SCAG p.151, 2014)**
> | power5e             = Demigod
> | refs5e              = <ref name="scag-p151">{{Cite book/Sword Coast Adventurer's Guide|151}}</ref>

— `siamorphe/wiki.txt:23` and `:37`

**Wiki 3e rows (cites in the refs: Faiths and Pantheons pp.106-7; Forgotten Realms Campaign Setting 3e p.235; Dragon 323 p.65)**
> | power3e             = Demipower
> | alignment3e         = Lawful neutral
> | symbol3e            = Silver chalice with a golden sun on the side
> | homeplane3e         = House of the Triad
> | realm3e             =
> | serves3e            =
> | servedby3e          =
> | portfolio3e         = Nobles, rightful noble rule, human royalty
> | domains3e           = Knowledge, Law, Nobility, Planning, Pride
> | worshipers3e        = Leaders, nobles, loremasters, those with inherited wealth or status

— `siamorphe/wiki.txt:53-62`

**Wiki 2e rows (cites in the refs: Powers and Pantheons pp.58-60)**
> | power2e             = Demipower
> | alignment2e         = Lawful neutral
> | symbol2e            = Silver chalice with golden sun on its side<br/>Silver circlet with golden sun on its brow
> | homeplane2e         = Prime Material plane/Toril
> | realm2e             = Faerûn
> | serves2e            =
> | servedby2e          =
> | portfolio2e         = Nobles, nobility, rightful noble rule, human royalty

— `siamorphe/wiki.txt:68-75`

Brackets removed from all rows above. The pantheon row is blank (`siamorphe/wiki.txt:11`).

### Field 2: Edict or core tenet

**Wiki, Dogma (cites: Powers and Pantheons pp.58-60)**
> The faith argued that nobles were given a divine right to rule, provided they ruled responsibly and well. The nobility had an obligation to rule with the best interest of their subjects in mind, even when those obligations interfered with their personal desires.<ref name="P&P-p58-60"/>

— `siamorphe/wiki.txt:124`

**Wiki, Dogma (cites: Faiths and Pantheons pp.106-7)**
> The benefits of nobility were provided to them so that they could rule well. Their wisdom and charisma were inherited from their noble ancestors, and the leisure that their station provided was theirs so that they might be educated to properly perform their duties.<ref name="F&P-p106-7"/>

— `siamorphe/wiki.txt:126`

**Adventure, Cassalanter background (the Siamorphe ethos)**
> Over the years, the Cassalanters have founded a number of philanthropic societies and made generous donations to temples dedicated to good-aligned deities. They are known to worship Siamorphe, a demigod whose ethos is the nobility's right and responsibility to rule.

— `sources/adventure-wdh.json:18405`

### Field 3: Portfolio and Areas of Concern

No source gives Areas of Concern. Portfolio and sphere rows:

> | portfolio5e         = Nobility, responsibility — `siamorphe/wiki.txt:30`
> | sphere4e            = Nobility — `siamorphe/wiki.txt:45` (4e; the row's ref is Forgotten Realms Campaign Guide p.81, `siamorphe/wiki.txt:51`)
> | portfolio3e         = Nobles, rightful noble rule, human royalty — `siamorphe/wiki.txt:60`
> | portfolio2e         = Nobles, nobility, rightful noble rule, human royalty — `siamorphe/wiki.txt:75`
> | portfolio1e         = Rightful rule of nobility — `siamorphe/wiki.txt:89`

### Field 4: Worship (Waterdeep specifics first)

**Wiki, Temples (cites: Faiths and Pantheons pp.106-7; Powers and Pantheons pp.58-60)**
> Most of Siamorphe's temples were small family shrines in the houses of the nobility of Waterdeep, and recently in Tethyr.<ref name="F&P-p106-7"/> Her only true remaining temple was the Chapel and Chalice of the Divine Right in Waterdeep. The relatively small house of worship was within the walls of the Assumbar family's villa, and was the central building of the three that bordered the Street of the Singing Dolphin.<ref name="P&P-p58-60"/>

— `siamorphe/wiki.txt:129`

**Adventure, Cassalanter Villa (the temple of Siamorphe beneath the estate)**
> Cassalanter Villa is an extravagant manse with dozens of lavish chambers for the masters of the house and their guests-but its splendor belies the terrible secret it holds. The temple of Siamorphe that once lay beneath the estate has been desecrated by Victoro and Ammalia's devil-worship. Now, this great chapel is dedicated to the Lord of the Nine Hells.

— `sources/adventure-wdh.json:18563`

**Wiki, Divine Pageantry (holy day in the Sea Ward and North Ward; cites: Faiths and Pantheons pp.106-7)**
> The faith supported a holy day in the Sea Ward and North Ward of Waterdeep called the Divine Pageantry. The nobility took over the Heroes' Walk and Heroes' Garden and the Street of Glances down to the temple at the Street of the Singing Dolphin. During the Divine Pageantry, the nobles dressed and acted in archaic and stilted fashions, and threw coins (most often copper and silver) to the commoners.<ref name="F&P-p106-7"/>

— `siamorphe/wiki.txt:121`

**Wiki, clergy (Scions of Siamorphe; Waterdeep noble ceremonies)**
> In the 14{{th}} century DR, the priests of Siamorphe's faith, called Scions of Siamorphe, most often acted as advisers (both spiritual and practical) to the nobility. Elaborate rituals were revived from the decay that had occurred under the previous Siamorphe, and unique ceremonies were created for the noble families of Waterdeep and Tethyr, and were becoming quite fashionable. A baptism ceremony for a new heir could easily cost the family 10,000 gp.<ref name="P&P-p58-60"/>

— `siamorphe/wiki.txt:119`

**Campaign, the Asmodean temple's ceremonial hall (formerly a Siamorphe figure)**
> The temple's heart. A thirty-foot-tall statue of Asmodeus dominates the far wall — carved from what was once a Siamorphe figure, the proportions subtly wrong in ways that suggest alteration rather than original design. The original goddess's posture was open-armed and welcoming; the alterations produced a figure with arms extended in command. Seams in the stone are visible at the shoulders and neck where the carving was reworked. A sacrificial fire bowl sits at the base of the statue, a perpetual flame burning inside it without fuel.

— `campaign/locations/cassalanter-villa/16-ceremonial-hall.md:7`

**Adventure, the statue (Cassalanter Villa)**
> The statue once depicted Siamorphe, but the Cassalanters used {@spell stone shape} spells to recast it into an image of their dread lord, Asmodeus.

— `sources/adventure-wdh.json:22827` (rest of the passage covers the bowl's conjuration aura and its fire damage)

Omens and messengers: none found (see Not found).

### Field 5: Relations and origin (wiki; each quote carries its own cites)

**Origin, Lady Siamorphe of Waterdeep (cites: Powers and Pantheons pp.58-60)**
> '''The Divine Right''' was the vessel of a semi-divine power that was passed down to a successor when the successor was dying. At any one time, the current Siamorphe was the latest in that lineage. By preference, the successor was a direct descendant of the previous power's mortal form, but anyone of noble blood would suffice. In the 13{{th}} and 14{{th}} centuries, the present Siamorphe was one Lady Siamorphe of Waterdeep, chosen when she was killed in a riot in the {{yearlinkName|1256}}, inheriting the role from the former Siamorphe, who was a nobleman of Baldur's Gate.<ref name="P&P-p58-60"/>

— `siamorphe/wiki.txt:107`

**Relations, no allies (cites: Faiths and Pantheons pp.106-7)**
> Though she dwelled in the House of the Triad,<ref name="F&P-p106-7"/> she had no true allies or superiors among the gods.<ref name="F&P-p106-7"/>

— `siamorphe/wiki.txt:113`

**Relations, opposed powers (cites: Powers and Pantheons pp.58-60; Faiths and Pantheons pp.106-7)**
> She opposed those who fostered tyranny and corruption, most especially Bane, Cyric, and Gargauth.<ref name="P&P-p58-60"/><ref name="F&P-p106-7"/>

— `siamorphe/wiki.txt:115`

**Relations, 4e (the row's ref is Forgotten Realms Campaign Guide p.81, `siamorphe/wiki.txt:51`)**
> | serves4e            = Amaunator

— `siamorphe/wiki.txt:43`

**1384, Tyr and Siamorphe (wiki, Tyr page; cites: The Grand History of the Realms p.159)**
> In the {{YearlinkName|1384}}, shortly before the catastrophic events of the Spellplague, Tyr and Siamorphe, who then dwelt in the House of the Triad, had a great disagreement over a battle between Tethyrian and Calishite forces. The argument was so severe that Siamorphe left the House of the Triad to make her realm with Sune in Brightwater. Tyr sent Helm as a messenger to Sune to explain his position, and Sune tried to act as a peacemaker. As the goddess of love, she proposed a marriage between Tyr and Tymora as a way to restore balance to the Celestial Planes. Tyr agreed and began a formal courtship with the goddess of good fortune.<ref name="TGHotR-p159">{{Cite book/The Grand History of the Realms|159}}</ref>

— `tyr/wiki.txt:236` (cross-power; quoted from the Tyr bundle; the same quote appears in Tyr Field 5)

### Field 6: Campaign and published-adventure mentions

**Campaign, Cassalanter Villa ballroom mosaic**
> The floor is a Siamorphe mosaic — the goddess's sun symbol rendered in gold and white tile, five feet across, centered precisely in the room.

— `campaign/locations/cassalanter-villa/06-ballroom.md:3`

**Campaign, Cassalanter family crypt**
> Twelve stone sarcophagi are arranged in two rows, each bearing the Cassalanter family crest in carved relief — a sun over a scale, in the Siamorphe heraldic tradition.

— `campaign/locations/cassalanter-villa/15-family-crypt.md:7`

**Campaign, Caladorn Cassalanter (ghost of Victoro's father)**
> **Relationships.** Caladorn is the ghost of Victoro Cassalanter's father, a former Masked Lord and hero of the North who devoted his life to Siamorphe, the former owner of two items critical to the contract-destruction path (the +1 plate armor and the mace of disruption), and the reason the solution to the Cassalanter pact has been beneath the villa the entire time — accessible only to people not corrupted by it.

— `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:26`

**Campaign, the family's public devotion (organization page)**
> The family lives in a villa in the Sea Ward, is publicly known for its ancestral devotion to Siamorphe, and hosts public galas during Waukeentide, and the younger twins, Terenzio and Elzerina, are often seen at play in the gardens.

— `campaign/setting/organizations/10-cassalanters.md:58`

**Campaign, the Order's holy symbol (Shrine on Aveen Street, chaplain's line)**
> > "Savra asked me for this a tenday ago, before she had the book. It's the sun of Siamorphe, the Lady of Nobility, and I've consecrated it. I can't tell you what it will do. I'd carry it into any noble house you mean to enter."

— `campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/ev-01-the-shrine-on-aveen-street.md:333`

**Campaign, the holy symbol in the crypt**
> **Pacifying the specters:** Present a Siamorphe holy symbol (from the Order's chaplain at the end of Order of the Gauntlet Mission 5, or from Savra Belabranta at Order of the Gauntlet r10). The specters halt, withdraw back into the floor, and become inert for the remainder of the encounter. They do not emerge again unless the symbol is removed from the chamber.

— `campaign/locations/cassalanter-villa/15-family-crypt.md:15`

**Further lines (Field 6):**
> The City Watch has small, single-person \"watch boxes\" set up on nearly every street corner in the Sea Ward, including the intersection just outside the gates of Cassalanter Villa. If a guard sounds the alarm, the Watch member on duty fetches a force of forty City Watch {@creature veteran||veterans} to cordon off the property.

— `sources/adventure-wdh.json:18579` (the Sea Ward placement of the villa; JSON escapes kept)

> A faded holy symbol of Siamorphe, a silver chalice bearing a golden sun symbol, is painted on the south wall. If the sun symbol is pushed, the wall grinds open, revealing {@area C29|330} beyond. A character who searches the wall automatically detects the secret door and can, with a successful {@dc 10} Wisdom (Perception) check, figure out how to open it.

— `sources/adventure-wdh.json:20756`

> The ghost is all that remains of Caladorn Cassalanter, a former Masked Lord and hero of Waterdeep. The ghost halts its attack and calls off the specters if a character wears or presents a holy symbol of Siamorphe. After it is shown such a symbol, the ghost guides characters to its personal crypt ({@area A4a|33e}).

— `sources/adventure-wdh.json:22713`

> Light from a crystal chandelier reflects off more than three dozen holy symbols of Siamorphe perched on wall shelves, each in the form of a silver chalice with a golden sun etched on its outside.

— `sources/adventure-wdh.json:19985` (room not confirmed)

> The polished marble floor is a dazzling mosaic that depicts a silver chalice with the image of a golden sun on its outside. Characters who succeed on a {@dc 10} Intelligence (Religion) check recognize it as the holy symbol of Siamorphe, demigod of nobility.

— `sources/adventure-wdh.json:20349` (room not confirmed)

> \"Canticle of the Silver Chalice,\" a hymn to the demigod Siamorphe. {@i Wulfgar and the Crystal Shard}, an epic opera detailing the adventures of a barbarian, a dwarf, and a drow in Icewind Dale.

— `sources/adventure-wdh.json:20063` (room not confirmed; the JSON escapes \" are kept as in the file)

> The west wall is different from the others. Carved into the stone at eye level: a Siamorphe sun symbol, eight spokes radiating from a central circle, rendered in relief.

— `campaign/locations/cassalanter-villa/11-wine-cellar.md:5`

> The fragmentary impressions clarify into two distinct images: a beholder's unblinking eye in deep darkness, carved stone wet from underground springs; and a Sea Ward villa with a sun symbol marking a hidden door, the Cassalanter house mark pressed into the stone above a spiral stair.

— `campaign/structure/arc-h-sea-maidens-faire.md:253` (**not in bundle**; names the sun symbol, not Siamorphe by name)

> The chaplain gives one holy symbol to the party, and the members choose who carries it. A Siamorphe holy symbol received here counts for **Cassalanter Villa**, which reads it from the party's possessions.

— `campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/ev-01-the-shrine-on-aveen-street.md:353`

> | **Cassalanter Villa** | A Siamorphe holy symbol from the Order's chaplain, given at the end of **The Shrine on Aveen Street**, counts for the villa. If that mission has not run, a Whitehawk member gets one from Savra once the party holds evidence from **Faction Outposts** or has marked **Cassalanter Register Filed**. Savra can fight beside the party once, using the quest's one Marcheon operation for the whole party. At Whitehawk she attends the charity ball in Gauntlet formal dress. Her knowledge of the villa is the ground-floor plan in the dossier. |

— `campaign/guides/factions/05-order-of-the-gauntlet.md:32`

> - **Cassalanter Villa:** Savra gives the member a Siamorphe holy symbol, consecrated by the Order's chaplain, if the party has not yet received one.

— `campaign/quests/faction-events/order-of-the-gauntlet/r10-whitehawk/ev-01-whitehawk.md:220`

> - **Ysolt Brannock** (Order of the Gauntlet): the Order's chaplain, who gives the Siamorphe holy symbol.

— `campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/overview.md:76`

> The ballroom floor is a Siamorphe mosaic, and the Cassalanters maintain an ancestral devotion to the goddess of nobility — publicly.

— `campaign/structure/arc-g-cassalanter-villa.md:17` (sentence from the line)

> - **Cover:** Victoro is publicly a worshipper of Lathander, and the family is publicly known for its ancestral devotion to Siamorphe. The family is known for charity, and none of that warmth is faked.

— `campaign/setting/deities/asmodeus.md:81`

> The wiki lists Waukeen, Siamorphe and Asmodeus as the house's favored deities.

— `campaign/setting/organizations/10-cassalanters.md:63` (sentence from the Origins bullet)

### Per-power answers (Siamorphe)

**(1) Temples and shrines in Waterdeep, and ward**
- Chapel and Chalice of the Divine Right, "the central building of the three that bordered the Street of the Singing Dolphin," per the wiki (`siamorphe/wiki.txt:129`, quoted in Field 4). The wiki gives no ward. No campaign file places this chapel.
- Divine Pageantry holy day in the Sea Ward and North Ward (`siamorphe/wiki.txt:121`, Field 4).
- The former Siamorphe temple beneath Cassalanter Villa (`sources/adventure-wdh.json:18563`, Field 4). The adventure places the villa in the Sea Ward: "The City Watch has small, single-person \"watch boxes\" set up on nearly every street corner in the Sea Ward, including the intersection just outside the gates of Cassalanter Villa." (`sources/adventure-wdh.json:18579`). The campaign agrees: "The family lives in a villa in the Sea Ward" (`campaign/setting/organizations/10-cassalanters.md:58`).
- The holy symbols and the ballroom mosaic are inside the villa (Field 6). No Siamorphe shrine appears in another ward.

**(2) Campaign NPCs, factions and quests using Siamorphe**
- The Cassalanters' public cover (Victoro, Ammalia, the family): `campaign/setting/deities/asmodeus.md:81` (Field 6).
- Caladorn Cassalanter, the ghost: `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:26` (Field 6).
- Savra Belabranta and the Order of the Gauntlet: the holy symbol, `campaign/guides/factions/05-order-of-the-gauntlet.md:32` (Field 6).
- Ysolt Brannock, the Order's chaplain: `campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/overview.md:76` (Field 6).
- Quests: Cassalanter Villa (`campaign/structure/arc-g-cassalanter-villa.md:17`); The Shrine on Aveen Street (`campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/ev-01-the-shrine-on-aveen-street.md:333`); Whitehawk (`campaign/quests/faction-events/order-of-the-gauntlet/r10-whitehawk/ev-01-whitehawk.md:220`); Sea Maidens Faire (`campaign/structure/arc-h-sea-maidens-faire.md:253`, not in bundle).

**(3) Wiki lines that mention Waterdeep** (Grep -n confirmed these four true lines)
- Line 107: the Lady Siamorphe of Waterdeep paragraph (Field 5).
- Line 119: the noble families of Waterdeep (Field 4).
- Line 121: the Sea Ward and North Ward holy day (Field 4).
- Line 129: the Chapel and Chalice (Field 4).

### Conflicts (Siamorphe)

**C1 Alignment.** The wiki gives Lawful good for 4e and Lawful neutral for 1e, 2e and 3e. No 5etools row exists.
> | alignment4e         = Lawful good — `siamorphe/wiki.txt:39`
> | alignment3e         = Lawful neutral — `siamorphe/wiki.txt:54`
> | alignment2e         = Lawful neutral — `siamorphe/wiki.txt:69`
> | alignment1e         = Lawful neutral — `siamorphe/wiki.txt:83`

Ranking: none between sources. The editions are tagged in the rows.

**C2 Home plane.**
> | homeplane3e         = House of the Triad — `siamorphe/wiki.txt:56` (3e)
> | homeplane2e         = Prime Material plane/Toril — `siamorphe/wiki.txt:71` (2e)
> "Siamorphe left the House of the Triad to make her realm with Sune in Brightwater." — `tyr/wiki.txt:236` (the 1384 move, as the Tyr page tells it)

Ranking: edition-tagged. The 1384 move is the Tyr page's account.

**C3 Demigod or demipower.**
> | power5e             = Demigod — `siamorphe/wiki.txt:23` (5e, SCAG p.151)
> | power3e             = Demipower — `siamorphe/wiki.txt:53` (3e)
> | power2e             = Demipower — `siamorphe/wiki.txt:68` (2e)

**C4 Domains.** Only the wiki gives domains, from the 3e row.
> | domains3e           = Knowledge, Law, Nobility, Planning, Pride — `siamorphe/wiki.txt:61` (3e; 5etools has none)

**C5 Temple, "only true remaining temple" against the adventure.** Both place a Siamorphe temple in Waterdeep. The wiki (2e and 3e sources) names the Chapel and Chalice as the only remaining temple in its period. The adventure describes a temple of Siamorphe under Cassalanter Villa, now dedicated to Asmodeus. No source links the two.
> "Her only true remaining temple was the Chapel and Chalice of the Divine Right in Waterdeep." — `siamorphe/wiki.txt:129`
> "The temple of Siamorphe that once lay beneath the estate has been desecrated by Victoro and Ammalia's devil-worship." — `sources/adventure-wdh.json:18563`

Ranking: the adventure and campaign outrank the wiki for the present day. The wiki does not date the chapel's closure.

**C6 Public worship.** Not a conflict, but a note for the secrecy rule. The adventure says the family is "known to worship Siamorphe" (`sources/adventure-wdh.json:18405`). The campaign treats the Siamorphe devotion as public cover (`campaign/setting/deities/asmodeus.md:81`). The adventure and the campaign agree on what is public.

### Not found (Siamorphe)

- 5etools entry: none (`siamorphe/5etools.md:1`).
- Edict as such: none; Field 2 gives the Dogma.
- Areas of Concern: none.
- Omens: none. Messengers: none.
- 5e holy days: none. The 3e and 2e wiki holy-day rows are blank (`siamorphe/wiki.txt:65` and `:79`). The only holy day is the Divine Pageantry (line 121).
- Pantheon row: blank (`siamorphe/wiki.txt:11`). The wiki's category is Faerûnian pantheon (`siamorphe/wiki.txt:138`).
- Ward of the Chapel and Chalice: not given by the wiki. No campaign file places it.
- Chosen of Siamorphe: none in the campaign or adventure bundle hits.
- Searches: campaign/ for `Siamorphe|sun symbol|Lady of Nobility|goddess of nobility|demigod of nobility|Divine Right|Chapel and Chalice|Divine Pageantry|Scions of Siamorphe|silver chalice`; campaign/ for `Assumbar|Singing Dolphin|Divine Pageantry` (no hits); sources/adventure-wdh.json for the same alias list (lines 18405, 18563, 19985, 20063, 20349, 20756, 22713, 22827); sources/adventure-wdmm.json for `Siamorphe|Divine Right|Chapel and Chalice` (no hits).

---

## 3. ZARIEL

Bundle sizes: 5etools.md says there is no entry. wiki.txt is 305 lines, read whole. campaign-hits.txt has one line (`asmodeus.md:47`); the bundle missed `arc-e-faction-outposts.md:261`. adventure-hits.txt is empty, as the brief said.

### Field 1: Identity

**5etools**
> No 5etools deities.json entry for this name.

— `zariel/5etools.md:1`

**Wiki title row (Lord of the First; Archduchess of Avernus)**
> | titles         = Lord of the First<br />Archduchess of Avernus

— `zariel/wiki.txt:11`

**Wiki rows, home and race (brackets removed)**
> | home           = Avernus
> | formerhomes    = Mount Celestia
> | sex            = Female
> | race           = Archdevil<br />{{Former}} Solar

— `zariel/wiki.txt:14-17`

**Wiki patron row (Asmodeus; former Lathander)**
> | patron deity   = Asmodeus<br />{{Former}} Lathander

— `zariel/wiki.txt:21`

**Wiki 5e rows (the row's ref is Mordenkainen's Tome of Foes pp.180-181)**
> | alignment5e    = Lawful evil
> | challenge5e    = 26

— `zariel/wiki.txt:61-62`

**Wiki lead (cites: Baldur's Gate: Descent into Avernus p.4; Mordenkainen's Tome of Foes pp.10-11; Monster Manual 5e p.68)**
> '''Zariel''' ({{Pronounce|ZAR|ee|el|refs=<ref name="BGDA5e-p4">{{Cite book/Baldur's Gate: Descent into Avernus|4}}</ref>|audio=Zariel.ogg}} {{Pronounce|ZAIR|ee|el|alt=yes|refs=<ref name="BGDA5e-p4" />|audio=Zariel2.ogg}}), titled the Archduchess of Avernus and the Lord of the First, was the archdevil ruler of Avernus who was dedicated to winning the unending Blood War between devils and demons. She was originally an angel of the Seven Heavens before transforming into an archdevil and falling to the Nine Hells.<ref name="MTF5e-p10-11"/><ref name="MM5e-p68">{{Cite book/Monster Manual 5th edition|68}}</ref>

— `zariel/wiki.txt:66`

**Further lines (Field 1): wiki category rows (lines 303 to 305)**
> [[Category:Rulers]]
> [[Category:Archfiends]]
> [[Category:Fallen angels]]
> [[Category:Fiend patrons]]

— `zariel/wiki.txt:302-305` (the last category, "Fiend patrons", is the only warlock-patron tag the wiki gives; brackets kept here because these are category lines, quoted as written)

### Field 2: Edict or core tenet

No source gives an edict. The personality and motives are these.

> Zariel was a warmonger obsessed with battle, someone who lived to fight and judged others on their combat skills and willingness to use them. She prized zealous fury as much as discipline and training, and led her troops into battle herself with iron resolve, leaving many a structure in ruin as she carved her war path. However, neither her own battle prowess nor that of her forces could disguise the fact that Zariel was reckless and rash, relying on her troops' berserker rage and her own determination to win her fights.<ref name="MTF5e-p10-11"/>

— `zariel/wiki.txt:79`

> Her behavior had warped to match that of her infernal peers, for she had become a cruel being that inflicted psychological torment on her enemies and subjected those that displeased her to horrible fates.<ref name="MTF5e-p180-181"/><ref name="DMG5e-p64"/> She had also grown distrusting to the point of being taken aback by a heroic act of self-sacrifice, having become the kind of plotter to set numerous schemes in motion at once and deal in contracts to bind people into servitude.<ref name="BGDA-p149-155"/> While once a purveyor of blind justice,<ref name="BGDA5e-p146-148"/> Zariel had allowed her emotions to color her decisions, twisting it into rage-fueled vengeance, and she refused to forgive even decades after being wronged.<ref name="BGDA5e-p7"/><ref name="MTF5e-p180-181"/><ref name="BGDA-p149-155"/>

— `zariel/wiki.txt:81`

> Zariel desired the souls of the greatest warriors and expected only the best from those under her. She allowed them relatively fuller lives, if only so they could hone their skills in life and join her ranks of universally disciplined and capable servants after death.<ref name="MTF5e-p180-181" /> Those mortals who pleased her while alive were sometimes allowed to keep their memories and be promoted into higher forms of devils rather than become pathetic lemures. She also demanded loyalty from her servants, her hard bargains being eternal and indissoluble things akin to ultimatums.<ref name="MTF5e-p180-181" /><ref name="BGDA-p149-155"/>

— `zariel/wiki.txt:184`

> Zariel believed that it was the responsibility of the angelic host to defeat evil, and was of the opinion that an assault from the hosts of Celestia could wipe out both sides of the Blood War in one stroke, freeing the multiverse from the fiends who destroyed each other and vast chunks of it in the process. Despite chastising her superiors for their stance as neutral observers, Zariel was repeatedly forbidden from entering the conflict. Zariel was frustrated by her their refusal to engage in the war,<ref name="MTF5e-p10-11" /><ref name="BGDA5e-p7"/> and drew the line when Yeenoghu slaughtered a village under her protection.<ref name="BGDA5e-p144"/>

— `zariel/wiki.txt:207` (the source reads "her their"; kept as written)

### Field 3: Portfolio and Areas of Concern

No source gives Areas of Concern. The wiki's stated domain is the Blood War and the realm of Avernus. The title and lead are quoted in Field 1 (`zariel/wiki.txt:11`, `:66`).

> Prosecuting the Blood War took up much of Zariel's time and attention, and she had little room to deal with anything else.<ref name="BGDA-p82.90">{{Cite book/Baldur's Gate: Descent into Avernus|82,90}}</ref> Her offensive military campaign often had her at the forefront of invasions when she wasn't within a flying fortress overseeing Avernus's defense.<ref name="MTF5e-p10-11" /><ref name="BGDA-p130-131"/> She apparently had a penchant for spawning cambions to serve as leaders for her followers.<ref name="MTF5e-p21">{{Cite book/Mordenkainen's Tome of Foes|21}}</ref>

— `zariel/wiki.txt:137`

> Prosecuting the Blood War constantly taxed Zariel's armies, with her legions always being depleted by the ceaseless fighting. To keep Hell in the war, she aggressively recruited mortal souls and looked for evildoers on the Material Plane who could bring her more, thus guaranteeing her more infernal soldiers.<ref name="MTF5e-p10-11"/><ref name="BGDA-p75-76"/>

— `zariel/wiki.txt:193`

### Field 4: Worship (Waterdeep specifics first)

**Wiki, the only Waterdeep event (cites: the "IC" ref, Idle Champions of the Forgotten Realms)**
> On a Founders' Day in the late 15th century, Zariel was summoned onto Waterdeep's Field of Triumph. She, in turn, summoned a host of devils and bid them spread chaos in the city. Waterdeep briefly became a battlefield in the Blood War, as demons were attracted by the sudden presence of devils. Zariel hoped that strong adventurers would appear to defeat the fiendish invasion, and that she could lure or blackmail them into her service. A group of adventurers, commanded by Blackstaff Vajra Safahr to restore order to the city, was able to defeat Zariel and banish her back to the Nine Hells.<ref name="IC"/>

— `zariel/wiki.txt:250`

**Wiki, worshipers (cites: Mordenkainen's Tome of Foes pp.10-11 and p.21)**
> Zariel's worshipers were those that wished to fight but lacked the necessary experience, training, skill, talent, and bravery in martial affairs to do so, all of which her agents could offer.<ref name="MTF5e-p10-11"/><ref name="MTF5e-p21"/> Ordinary cultists showed greater ferocity than they would normally, and cult leaders had a keen tactical eye. Her cults were often headed by her own cambions.<ref name="MTF5e-p21"/>

— `zariel/wiki.txt:180`

**Wiki, a cultist's call (quoted text of the Idle Champions source)**
> By the power of Avernus, I call on the hordes of the Nine Hells! To me, my servants! Unleash chaos in Zariel's name!

— `zariel/wiki.txt:175`

**Wiki, method (devils disguised as angels; cites: Baldur's Gate: Descent into Avernus pp.65, 67-68)**
> Zariel took advantage of his fervor by sending devils disguised as angels to offer him power if he would help fight off the demonic menace, slowly eroding his sanity until he was a tyrannical leader obsessed with the destruction of demons on a level reaching madness.<ref name="BGDA5e-p65.67-68"/>

— `zariel/wiki.txt:197` (rest of the passage covers the cultists who praise her)

**Wiki, the cult's size (cites: FC 3e p.143 and Baldur's Gate: Descent into Avernus p.152, as the refs show)**
> After Bel's uprising, Zariel's worshiper base entered a period of decline as her followers scattered and her cults crumbled, their devotion having not transferred to the Pretender.<ref name="FC23e-p143"/> Once she was reinstated, however, Zariel's cult began to grow once more. If Zariel were to die, and thus all her contracts voided, a fair amount of cosmic chaos would ensue.<ref name="BGDA5e-p152">{{Cite book/Baldur's Gate: Descent into Avernus|152}}</ref>

— `zariel/wiki.txt:200`

Holy days, temples, omens and messengers: none found (see Not found).

### Field 5: Relations and origin (wiki; each quote carries its own cites)

**Origin, a solar of Lathander (cites: Baldur's Gate: Descent into Avernus pp.44, 144; Mordenkainen's Tome of Foes pp.10-11)**
> Originally, Zariel was a solar under the command of the Morning Lord Lathander,<ref name="BGDA5e-p144"/> her name, according to Reya Mantlemorn, meaning "Companion of Light".<ref name="BGDA5e-p44">{{Cite book/Baldur's Gate: Descent into Avernus|44}}</ref> From the Seven Heavens of Mount Celestia, Zariel was tasked with tracking the progress of the Blood War in Avernus, but from continued exposure to the conflict, she developed an obsession with the War and a taste for battle. Zariel was impetuous in nature, and couldn't ignore the desire to fight within her, but her requests were consistently blocked by her angelic peers.<ref name="MTF5e-p10-11" /><ref name="BGDA5e-p7"/>

— `zariel/wiki.txt:205`

**The Ride and her fall (sentence; cites: Mordenkainen's Tome of Foes pp.10-11 and 180-181, and Baldur's Gate: Descent into Avernus p.7)**
> Zariel succumbed to the corrupting nature of Hell and Asmodeus made her an archdevil and dubbed her his champion.<ref name="MTF5e-p10-11" /><ref name="MTF5e-p180-181" /><ref name="BGDA5e-p7"/>

— `zariel/wiki.txt:210` (rest of the passage covers the 1354 DR battle called the Ride, the rescue by osyluths, and a note on the date)

**Relations, Asmodeus (cites: Mordenkainen's Tome of Foes p.7; Baldur's Gate: Descent into Avernus pp.243, 75-76)**
> Asmodeus admired Zariel's passion for warfare and welcomed her into the fold of the archdevils, the angel-turned-fiend being something of a jewel in his crown.<ref name="MTF5e-p7"/><ref name="BGDA5e-p243"/><ref name="BGDA-p75-76"/> Despite this, it was said she actually desired vengeance against the Raging Fiend, and planned to drive him from the Hells.<ref name="MTF5e-p180-181" />

— `zariel/wiki.txt:153` (rest of the passage covers Gargauth and the other archdevils)

**Relations, Bel (cites: Baldur's Gate: Descent into Avernus pp.75-76, 114-115, 146-148; Mordenkainen's Tome of Foes pp.10-11)**
> Zariel's most direct opponent was likely Bel, former Lord of the First.<ref name="BGDA-p75-76"/> Despite instructions by Asmodeus to cooperate, the two utterly detested each other and invented distractions to avoid having to deal with one another. Zariel placed her assigned advisor in charge of weapons production to keep him busy, though that did nothing to stop his treasonous schemes.<ref name="BGDA-p75-76"/><ref name="BGDA5e-p114-115">{{Cite book/Baldur's Gate: Descent into Avernus|114-115}}</ref> Because Asmodeus supported Zariel, Bel couldn't directly challenge her, though he would take steps to make her seem incompetent,<ref name="BGDA5e-p146-148"/> and allowed her to continue her reckless maneuvers in the hopes she'd overextend her forces and be removed after a defeat.<ref name="MTF5e-p10-11"/> He'd even go so far as to help her be redeemed, even despite the low odds of success, since it would lead to him becoming archduke once more.<ref name="BGDA5e-p146-148"/>

— `zariel/wiki.txt:155`

**Relations, Tiamat (cites: Dragon 359 p.68; The Rise of Tiamat pp.10, 44; Baldur's Gate: Descent into Avernus p.28)**
> The haughty and aloof Tiamat had a somewhat complex relationship with Zariel, although it was certainly a hostile one. Zariel resented the draconic goddess, as the fallen angel had been at her mercy during the time of her demotion,<ref name="DMG359-p68"/><ref name="RoT5e-p10,44"/> and she had once sent her agents to steal from Tiamat's treasure hoards.<ref name="BGDA-p28"/> At the same time, Zariel once gifted the ''Burning Orb of Etiol the Abandoned'', to one of her diplomat's successors,<ref name="DMG359-p68"/> and had attempted to help her escape from Hell by assisting mortals with related goals. The attempts to free her, however, were only made because Zariel was unable to kill the Dragon Queen, and so seeing her leave Avernus was the next best option.<ref name="RoT5e-p10,44"/>

— `zariel/wiki.txt:157`

**Relations, reinstatement after Bel (cites: Mordenkainen's Tome of Foes pp.180-181 and 10-11)**
> Following Bel's demotion, Zariel was reinstated and reclaimed her title as Lord of Avernus before nearly driving all the demons out of Hell with her unrelenting offense.<ref name="MTF5e-p180-181" /><ref name="MTF5e-p10-11" />

— `zariel/wiki.txt:225` (the paragraph opens with the sentence "Eventually, Bel fell out of favor with Asmodeus after his inability to successfully repel a demonic invasion of Avernus, ...")

### Field 6: Campaign and published-adventure mentions

**Campaign, the Asmodeus page (history of the archdevils; not a use by any NPC, faction or quest)**
> - Azuth was separated from him on Hammer 10, 1487 DR (*The Devil You Know*, novel). By 1492 DR he had demoted Bel and re-elevated Zariel as archdevil of Avernus (*Dungeon Master's Guide* 2014; *Mordenkainen's Tome of Foes* 5e).

— `campaign/setting/deities/asmodeus.md:47`

**Campaign, Faction Outposts, Area 7 (names Avernus, not Zariel; points to the Cassalanter temple)**
> Area 7 — Nine Hells Mural: a detailed depiction of Avernus. A DC 15 Arcana check recognizes architectural elements consistent with Asmodean temple design — foreshadowing what the party will encounter beneath the villa in **Cassalanter Villa**.

— `campaign/structure/arc-e-faction-outposts.md:261` (**not in bundle**; the bundle searched for "Zariel" only)

**Adventures.** Grep of `sources/adventure-wdh.json` and `sources/adventure-wdmm.json` for `Zariel|Avernus` returned no lines. The bundle's adventure-hits.txt is empty, which agrees.

### Per-power answers (Zariel)

**(1) Temples and shrines in Waterdeep, and ward**
- None. No source places a temple or shrine of Zariel in Waterdeep. Her only Waterdeep connection is the summoning on the Field of Triumph (`zariel/wiki.txt:250`, Field 4).
- For the Field of Triumph's location, the campaign says: "- **Sea Ward** (wealthy northwest): noble estates, major temples, the Field of Triumph; Cassalanter Villa is here" (`campaign/setting/waterdeep-lore.md:15`). This places the Field in the Sea Ward. The Zariel summoning itself is not placed in the campaign.

**(2) Campaign NPCs, factions and quests using Zariel**
- None uses Zariel. The two campaign lines that name her realm or her are `campaign/setting/deities/asmodeus.md:47` and `campaign/structure/arc-e-faction-outposts.md:261` (both in Field 6; the second names Avernus only).
- No campaign file names a Zariel cult, cultist, Chosen or faction.

**(3) Wiki lines that mention Waterdeep**
- Line 250 only (Field 4). Grep for `Waterdeep` across the wiki returned line 250 and no other line.

### Conflicts (Zariel)

**C1 Timeline of her fall and return.**
> The timeline of events regarding the date of Zariel's rises and falls seem to have been retconned from past editions. — `zariel/wiki.txt:221` (sentence inside a note; the rest of the note covers the Guide to Hell, Dungeon 197 and Dragon 223 versions)
> By 1492 DR he had demoted Bel and re-elevated Zariel as archdevil of Avernus (*Dungeon Master's Guide* 2014; *Mordenkainen's Tome of Foes* 5e). — `campaign/setting/deities/asmodeus.md:47`

Ranking: the campaign's dated sentence is the remix's (`asmodeus.md:47`). The wiki's line 225 (Field 5) gives Bel's demotion and Zariel's return without a date.

**C2 Founders' Day summoning and the campaign calendar.** The wiki dates the Field of Triumph summoning to "a Founders' Day in the late 15th century" (`zariel/wiki.txt:250`). The campaign dates Founders' Day to Flamerule 1, 1492 DR: "- Founders' Day, Flamerule 1, is the party's real deadline." (`campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:26`). No campaign file links Zariel to this Founders' Day. The texts do not contradict each other; the wiki's date is simply not the campaign's.

### Not found (Zariel)

- 5etools entry: none (`zariel/5etools.md:1`).
- Edict: none. Field 2 gives the personality and motive text.
- Areas of Concern: none.
- Holy days, temples in any city, omens, messengers: none in the wiki or 5etools.
- Chosen of Zariel: none named in the wiki, campaign or adventure.
- Adventure mention: none (both adventure JSON files).
- Campaign NPC, faction or quest: none (Field 6 and the answers above).
- Searches: campaign/ for `Zariel|Avernus|Archduke|Archduchess|Lord of the First|Elturel|Solar Insidiator|Hellrider|Matalotok` (lines `asmodeus.md:47` and `arc-e-faction-outposts.md:261`); sources/adventure-wdh.json and sources/adventure-wdmm.json for `Zariel|Avernus` (no lines); the wiki for `Waterdeep` (line 250).

---

## Cross-power notes

- Tyr wiki line 236 and Siamorphe wiki line 107 both concern the House of the Triad. Both are quoted above (Tyr Field 5; Siamorphe Conflicts C2).
- No campaign file names Zariel together with Tyr or Siamorphe.
- Retired files cited only as conflict pointers: `campaign/structure/ch2-city-of-splendors.md:56` and `campaign/structure/ch1-beginning.md:104`.
- The adventure's Major Temples table has a row for Tyr (Halls of Justice, Castle Ward) and no row for Siamorphe or Zariel.

## Not readable

- None. Every bundle file was read. The Alexandrian PDFs, `sources/SOURCE_GUIDE.md` and the Appendix files were not read, by instruction. The `.docx` files were not touched.
