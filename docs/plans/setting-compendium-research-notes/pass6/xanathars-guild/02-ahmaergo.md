# Pass 6 research notes: Ahmaergo

Page: `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR, campaign-start lore. Quest-time material is listed in section C and routed to the quest file where it already lives.

Method and caveats:
- Campaign files: Read and Grep, quoted from the tool output.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. JSON escapes (`\"`) are shown as plain quotes.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. These were read with the Read tool's `pages` parameter from the rendered page images, and the quotes are transcriptions. Cite as printed page with the PDF page in brackets. Check exact wording against `pdftotext -layout` before any quote goes into prose. Files read in full: `sources/11. Lair  Xanathar’s Lair.pdf` (PDF pp. 1-9), `sources/5. Faction Outposts.pdf` (PDF pp. 1-13), `sources/17. Outpost and Lair Revelation Lists.pdf` (PDF pp. 1-4). Printed page = PDF page + 82 for the Lair and + 35 for the Outposts.
- Wiki: two copies. (a) Scratch copy `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-xg/Ahmaergo.txt`, cited as `Ahmaergo.txt:n`. (b) `sources/research/pass5-bundles/xanathars-guild/wiki.txt`, cited as `wiki.txt:n`. For the infobox and lead, the scratch line n equals wiki.txt line n+1168 (checked at scratch lines 2, 6, 8 and 61). Most wiki lines print no edition. Editions are inferred from the citation key and the infobox: *Cloak and Dagger* (`CaD`, 2e-era fields), *City of Splendors: Waterdeep* (`CoSW`, 3e), *Dragon Heist* (`WDH5e`, 5e). Each is marked as inferred.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

---

## Specific answers (from the caller's brief)

**S1. Does any file under `campaign/quests/faction-events/force-grey/` mention Ahmaergo?**
No. The folder holds 34 files (Glob of `campaign/quests/faction-events/force-grey/**/*`). Two searches came back empty:
- Case-insensitive search for `ahmaer|ahmaergo|majordomo|minotaur`: "No matches found."
- Search for `Ott|Steeltoes|Sylgar|fishkeep|Ahmaer|Noska`: "No matches found."

Mission 4 is the one the page's Featured-in bullet names. Its own text says it sits inside the lair quest and names only Nihiloor's wing:
> "This Social Event begins when a Force Grey member who marked **M3 Complete** prepares for **Xanathar's Lair** (unconverted), and it ends when the party leaves Blackstaff Tower for the lair."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-01-the-brief.md:5`

> "This mission is an objective inside the lair quest and not a separate raid. Companions can help with everything except Vajra's brief and debrief."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/overview.md:5`

> "Vajra sends the Force Grey members into Nihiloor's wing of Xanathar's Lair to destroy the pool that breeds intellect devourers. They also have to decide what to take out of it besides the pool."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/overview.md:80`

Answer: the Featured-in link to Force Grey Mission 4 has no Ahmaergo basis in that folder. The nearest link is the lair itself (Mission 4 is an objective in **Xanathar's Lair**), and no Force Grey file names any Guild figure in the search above.

**S2. The Noska versus Ahmaergo rivalry (`sources/SOURCE_GUIDE.md` around line 343).**
- `sources/SOURCE_GUIDE.md:343` (under the heading `### \`11. Lair  Xanathar's Lair.pdf\`` at line 335):
> "- Internal politics the PCs can exploit: Nar'l Xibrindas (drow spy working against Xanathar for House Xorlarrin), Noska vs. Ahmaergo rivalry, the Sylgar distraction (Xanathar's goldfish — stealing or threatening it causes Xanathar to abandon tactical thinking)"

- The Lair PDF it names does not contain the rivalry. All 9 pages (printed pp. 83-91) were read; no passage mentions a rivalry. Noska and Ahmaergo appear side by side in the rosters (printed pp. 89-90, quoted in A9).
- The adventure gives no rivalry. It pairs the two as trusted underlings: `sources/adventure-wdh.json:15041` ("Killing one of {@creature Xanathar|WDH}'s most trusted underlings, such as {@creature Ahmaergo|WDH} or {@creature Noska Ur'gray|wdh}, throws the day-to-day operation of the guild into chaos for a tenday.").
- The wiki has no rivalry on either page. The Noska wiki page does not name Ahmaergo. Its line on trust reads: "Noska was one of the most trusted underlings of the Xanathar." (`wiki.txt:1718`). A search of the Noska page (`wiki.txt` lines 1644-1720) finds no rival line.
- **The only text found that states the rivalry is a campaign structure document:**
> "The Noska–Ahmaergo rivalry has reached near-blows twice in the past month; during an active tournament, Noska is arena-side and Ahmaergo is in his quarters reviewing fight records, neither monitoring the other's territory. That window is real and exploitable. At renown 10+, Yagra Stonefist is available as outside backup — she can hold the guildsign entrance open from the exterior, delay a pursuing Guild patrol by 5 minutes, or cover the party's extraction from the sewer exit. Once per operation."
> — `campaign/structure/arc-f-xanathars-lair.md:41` (this is the Doom Raiders contact paragraph; it is Lair-quest intel, and "the past month" is undated)

Answer: the rivalry is in `campaign/structure/arc-f-xanathars-lair.md:41`. It is not in the Lair PDF or the adventure, despite `SOURCE_GUIDE.md:343`.

**S3. The wiki's 1368 DR (slaver leader) and 1372 DR (Master) entries.**
- **1372 DR, Master: confirmed in the wiki.** Ahmaergo is in the list of eleven Masters:
> "The Eye also elected eleven Masters to serve as supervisors of Guild members, four of which were the original Xanathar's Councilors.<ref name="C&D-p140"/> These Masters included [[Ahmaergo]], [[Avaereene]], [[Colstan Rhuul]], [[Shindia Darkeyes]], [[Slink Monteskor]], [[Randulaith]], [[Ott Steeltoes]], [[Slan Thurbel]].<ref name="C&D-p141-143">{{Cite book/Cloak & Dagger|141-143}}</ref>"
> — `wiki.txt:135` (follows "By {{Yearlink|1372}}..." at `wiki.txt:131`; edition inferred 2e from the *Cloak & Dagger* citation key)

  The "eleven domains" list that includes slavery:
> "During the rulership of the Eye, eleven Masters were elected to serve eleven domains: assassination, blackmail, bookkeeping, enforcement, extortion, information gathering, magical defenses, mercenaries, slavery, smuggling, and thievery. Owing to the expanse of some of these domains, some Masters served one domain together, while others served several at once.<ref name="C&D-p140">{{Cite book/Cloak & Dagger|140}}</ref>"
> — `wiki.txt:75` (edition inferred 2e)

- **1368 DR, slaver leader: not found in the Ahmaergo wiki text.** Searches for `1368` in `sources/research/pass5-bundles/xanathars-guild/wiki.txt` return only two lines. The first is the caption of the Avaereene infobox image: "Avaereene (right) with [[Randulaith]], [[1368 DR]]." (`wiki.txt:1280`). The second is about Avaereene, not Ahmaergo:
> "She formerly used her beauty and acting skills to entice adventurers into her slaving activities, but by [[1368 DR]]–[[1370 DR]] was coordinating activities behind the scenes."
> — `wiki.txt:1344` (Avaereene's Personality paragraph, citing *Cloak & Dagger* p. 141)

  The Ahmaergo wiki text gives "since [[1370 DR]]" and no 1368 date (`Ahmaergo.txt:61`; `wiki.txt:1229`). The only text that says "a slaver leader in 1368 DR" for Ahmaergo is the campaign's Draft Note:
> "> - **Research:** The wiki names Ahmaergo (a Master in 1372 DR and a slaver leader in 1368 DR) and Ott Steeltoes (a Councilor in 1357 DR) as long-serving Guild veterans. No campaign page says so, and the body does not use it. It would support the Guild having memory."
> — `campaign/setting/history/02-the-long-shadow.md:148`

  Answer: the 1368 DR claim is not in the wiki copies held here. The nearest 1368 entry in the Guild wiki is about Avaereene. Nothing in the wiki text held here supports 1368 DR for Ahmaergo.

**S4. Ahmaergo and Ott (the page's cross-reference).** Wiki only. See A6 and F7.

---

## A. Background facts by theme

### A1. Origin, clan, birth, family
No campaign or adventure source gives Ahmaergo's birth, family or home town. The wiki gives a nickname and a title only.

**Wiki nickname (CaD p. 141, 2e inferred)**
> "| nicknames      = Horned Dwarf<ref name="CaD-p141"/>"
> — `Ahmaergo.txt:8` (= `wiki.txt:1176`)

**Wiki title, "Lord of Iron" (CaD p. 147, 2e inferred)**
> "| titles         = Third of the Hand, Master of Slavery<ref name="CaD-p141"/><br/> Lord of Iron<ref name="CaD-p147">{{Cite book/Cloak and Dagger|147}}</ref>"
> — `Ahmaergo.txt:6` (= `wiki.txt:1174`)

**Wiki, membership of the Iron Ring (wiki only; the Iron Ring appears in no campaign file)**
> "'''Ahmaergo''' ({{Pronounce|ah|MAIR|go|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a member of the [[Iron Ring]] and the most competent slaver of the [[Xanathar Thieves' Guild]] of [[Skullport]] since [[1370 DR]].<ref name="CaD-p141" /> As of [[1492 DR]]{{Waterdeep-time}}, he was the most influential person in the Guild after [[Xanathar]].<ref name="WDH5e-p193"/>"
> — `Ahmaergo.txt:61` (= `wiki.txt:1229`; the lead. "since 1370 DR" is CaD-era, 2e inferred; the 1492 DR sentence cites WDH5e p. 193)

> "To add more temptation, Ahmaergo was also secretly one of the leaders of the Iron Ring. To others, he posed as a liaison with the Iron Ring.<ref name="CaD-p139-147">{{Cite book/Cloak and Dagger|139, 147}}</ref>"
> — `Ahmaergo.txt:76` (= `wiki.txt:1244`; CaD pp. 139, 147, 2e inferred)

**Wiki, the Iron Ring as a slaving operation (wiki only, context)**
> "Though the Registry claimed loyalty to whomever had the most coin, it was secretly controlled by the [[Iron Ring]], a slaving operation.<ref name="SP-p36">{{Cite book/Skullport|36}}</ref>"
> — `sources/research/pass3-bundles/undermountain-and-skullport/wiki.txt:411` (wiki only; citation key *Skullport* p. 36; edition not printed)

**Pronunciation (5e, adventure)**
> "{@creature Ahmaergo|WDH}" / "ah-MAIR-go"
> — `sources/adventure-wdh.json:49-50` (pronunciation table, "Name" / "Pronunciation" columns; the table's page is not read)

### A2. Joining the Guild and the slave trade
No Ahmaergo-specific entry in the campaign or adventure. The general test is in the campaign:
> "- **Crime Is the Entry Fee:** Anyone can join, but an applicant must first pass a test that always involves a serious crime. The crime might be murdering a member who failed Xanathar, kidnapping a Waterdhavian, collecting a ransom or looting a warehouse. After that, advancement depends on wiles and on the ability to dispose of rivals, and the competition is fierce and often deadly."
> — `campaign/setting/organizations/08-xanathars-guild.md:32`

Wiki, the slave-trade duties (wiki only, CaD p. 141, 2e inferred):
> "Ahmaergo was in charge of buying and selling the slaves acquired by the Guild. He also was in charge of the logistic aspects of the slave market, moving them to and from those involved.<ref name="CaD-p141" /> "
> — `Ahmaergo.txt:70` (= `wiki.txt:1238`)

Wiki, the Guild's trust in him and his ambition (wiki only, CaD p. 141, 2e inferred):
> "Ahmaergo worked many for years in the Guild as a slaver but the Xanathar did not fully trust him and kept a close watch on him, usually via [[Avaereene]], the Guild's slave-taker. The dwarf hated this intrusion in his business. He was starting to get ambitious, wanting to leave the Xanathar and work as an independent slaver.<ref name="CaD-p141" />"
> — `Ahmaergo.txt:74` (= `wiki.txt:1242`)

### A3. Rank, titles and role in the Guild
**Campaign, the Guild's role for Ahmaergo**
> "- **Ahmaergo** (DH p. 195) — Shield dwarf majordomo, lawful evil. Ahmaergo handles logistics: gladiatorial procurement, outpost resupply, discipline. Most orders that bear Xanathar's name are written by Ahmaergo. See the **Ahmaergo** page in Notable Figures."
> — `campaign/setting/organizations/08-xanathars-guild.md:101` (page reference "DH p. 195" conflicts with the adventure's p. 193; see D3)

> "Xanathar rules the Guild from a lair below Skullport, and very few members have access to it (*Dragon Heist*, 5e). Its lieutenants manage the Guild's day-to-day operations (*Dragon Heist*, 5e). Ahmaergo, a shield dwarf, is the most influential member after the beholder, and Nar'l Xibrindas is its only advisor. Nihiloor has carved out a lair of its own inside the beholder's lair, Noska Ur'gray is the chief enforcer and Thorvin Twinbeard is the chief engineer and trapsmith. Ott Steeltoes keeps Sylgar, and Gorath and Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)."
> — `campaign/setting/organizations/08-xanathars-guild.md:43`

> "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e). The Guild is made up of some of Waterdeep's most disreputable folk and of monsters, whom the beholder forces into service or draws in with treasure, food or power (*Dragon Heist*, 5e). Goblins and bugbears work for it, and Nihiloor has infected some of them with intellect devourers (Forgotten Realms Wiki, *Xanathar's Thieves' Guild*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:45` (Ahmaergo is not placed on this ladder)

**Campaign, the Gamemaster's Summary contacts line**
> "> - **Contacts:** **Ahmaergo**, **Keln Trigos** (Guild contacts in the city); **Grinda Garloth** (independent contractor); **Gorath**, **Korgstrod Uxgulm**, **Noska Ur'gray** (field leaders)"
> — `campaign/setting/organizations/08-xanathars-guild.md:8`

**Campaign, the Villains table**
> "| Ahmaergo | Majordomo | Most trusted lieutenant; the only one Xanathar registers as competent; Ahmaergo knows he is replaceable |"
> — `campaign/setting/villains/xanathar.md:47`

**Adventure, "most influential"**
> "After the beholder, {@creature Ahmaergo|WDH} is the most influential  member of the Xanathar Guild."
> — `sources/adventure-wdh.json:31697` (Appendix B entry; page 193 at `:31693`)

**Adventure, the "important underlings" list**
> "{@creature Xanathar|WDH} relies on underlings for advice, information, and day-to-day oversight of the Xanathar Guild. The following important underlings are described in appendix B:"
> followed by the list item:
> "{@creature Ahmaergo|WDH}, dwarf majordomo",
> — `sources/adventure-wdh.json:15066` (list at `:15071`; "Important Underlings" inset, page 100 at `:15063`)

**Wiki, slaving "Hand" ranks (1372-era, wiki only, 2e inferred)**
> "Three of these Masters oversaw the Eye's slaving operations, and were referred to as the Eyes of the Hand. From lowest to highest, their ranks were Third of the Hand, Second of the Hand, and the Command of the Hand. Their underlings were referred to as simply "Hands," and operated as "snatch bands," groups who kidnapped people in order to sell them into slavery.<ref name="C&D-p140"/><ref name="TRoU-TEatH-p5">{{Cite book/The Ruins of Undermountain II/The Eye and the Hand|5}}</ref>"
> — `wiki.txt:77` ("Third of the Hand" is Ahmaergo's wiki title at `Ahmaergo.txt:6`)

### A4. How long in post, and dates
**Wiki, since 1370 DR (CaD-era, 2e inferred)**: quoted at `Ahmaergo.txt:61` in A1.

**Wiki, Black Tankard (Skullport, wiki only)**
> "Circa [[1370 DR]], he was linked to the [[Black Tankard]], a tavern in the [[Skullport/Lower Port|Lower Port]].<ref name="SP-p36-37">{{Cite book/Skullport|36-37}}</ref>"
> — `Ahmaergo.txt:72` (= `wiki.txt:1240`; citation key *Skullport* pp. 36-37, edition not printed)

**Wiki, "Around 1492 DR" majordomo (WDH5e p. 193)**
> "Around [[1492 DR]],{{Waterdeep-time}} Ahmaergo was the Xanathar's majordomo and the most influential member of the guild after his master.<ref name="WDH5e-p193">{{Cite book/Waterdeep: Dragon Heist|193}}</ref>"
> — `Ahmaergo.txt:79` (= `wiki.txt:1247`)

**Campaign**: no dated tenure for Ahmaergo.

### A5. Faith
No source gives Ahmaergo a faith. The adventure, the campaign and the wiki are silent on it.

### A6. Relationships to other named figures
**Xanathar (campaign, the master)**
> "**Relationships.** Xanathar is the beholder crime lord of Xanathar's Guild, the employer of Ahmaergo (its majordomo), Nihiloor (its mind flayer, which has psionically dominated Xanathar for the last four months without Xanathar knowing), and Nar'l Xibrindas (its drow advisor, whom it does not yet know is Jarlaxle's spy). It has a healthy fear of Laeral Silverhand and spares those in her employ."
> — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:26`

**Xanathar (adventure, the Morale order)**
> "If {@creature Xanathar|WDH} is reduced to half its maximum hit points, or if it believes its life to be in mortal danger, it activates its {@item ring of invisibility} and howls to {@creature Ahmaergo|WDH} to \"tear the usurpers limb from limb.\" While {@condition invisible}, {@creature Xanathar|WDH} flies to its sanctum ({@area X19|29c}) by the safest route."
> — `sources/adventure-wdh.json:14981` (part of the Xanathar NPC entry; the Vault-bargain paragraph at `:14980` is quest-time, see C)

**Noska Ur'gray (campaign rivalry, structure doc; see S2)**
> "The Noska–Ahmaergo rivalry has reached near-blows twice in the past month; ..."
> — `campaign/structure/arc-f-xanathars-lair.md:41` (quoted in full at S2)

**Ahmaergo's inspection rounds (adventure)**
> "If he's not with {@creature Xanathar|WDH} in the arena ({@area X6|27a}), {@creature Ahmaergo|WDH} (see {@adventure appendix B|WDH|12}) is conducting a routine inspection of the dungeon."
> — `sources/adventure-wdh.json:17552` (the keyed-area entry; the page of the entry is not read)

**Ahmaergo and Noska at the arena (adventure)**
> "Standing on the steps of the alcove are two dwarves: {@creature Xanathar|WDH}'s majordomo, {@creature Ahmaergo|WDH} (see {@adventure appendix B|WDH|12}), who presides over fight tournaments, and {@creature Xanathar|WDH}'s chief enforcer, {@creature Noska Ur'gray|wdh} (see {@adventure appendix B|WDH|12}), who releases arena combatants from {@area X7|27e}."
> — `sources/adventure-wdh.json:17166` (the arena entry; the rest of the passage covers Xanathar's hovering position, the bleachers and the goblins)

**Nar'l Xibrindas (quest-time clerk case, routed)**
> "Ahmaergo's clerks have built a case from three Dock Ward incident reports that Nar'l never forwarded, and from a fence named Tarn Hobble, who told them a drow in a Guild coat was seen near the quay on two of the nights the elves died."
> — `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/ev-01-the-compromised-eye.md:20` (quest-time; see C)

**Nihiloor and a kidnapped cook (adventure, lair state)**
> "{@creature Bepis Honeymaker|wdh} is a honey merchant who was kidnapped from his Trades Ward home a month ago. The Xanathar Guild tried to ransom him back, but seemingly his relatives either couldn't pay or decided not to. (In truth, his rotten in-laws destroyed the ransom notes and told Bepis' wife and children that he ran away with another family.) {@creature Ahmaergo|WDH} has put him to work as a cook but threatens to give him over to the mind flayer {@creature Nihiloor|WDH} every so often."
> — `sources/adventure-wdh.json:17989` (the Bepis entry; "a month ago" is relative to the adventure's own timeline)

**Thorvin Twinbeard (adventure)**
> "He's never seen {@creature Ahmaergo|WDH}'s chambers (areas X11 and X12) but knows the rest of the lair well."
> — `sources/adventure-wdh.json:17444` (the rest of the passage covers Thorvin's pulverizer and what he sells to the Harpers)

**Avaereene (wiki, slave-taker who watched him; wiki only, 2e inferred)**: quoted at A2 (`Ahmaergo.txt:74`). Note the spelling; see F6.

**Ott Steeltoes (wiki only)**
> "In the mid-to-late 14{{th}} century [[DR]], the reorganization of the guild (and the secret change of the guild master) gave him more freedom in his thieving operations, which Ott greatly enjoyed. He became good friends with [[Ahmaergo]] and the two [[dwarves]] often drank together.<ref name="CaD-p143" />"
> — `wiki.txt:1901` (*Cloak and Dagger* p. 143, 2e inferred; the Ott Notable Figures page cites this wiki passage at `campaign/setting/notable-figures/xanathars-guild/06-ott-steeltoes.md:18`)

**Nar'l, the Harper and Bregan D'aerthe (campaign, quest-time; routed)**: see C.

### A7. Personality and motives (day-one)
**Adventure, the source of the page's Persona**
> "{@creature Ahmaergo|WDH}, {@creature Xanathar|WDH}'s majordomo, has a fascination  with minotaurs. Although outwardly civil, the shield  dwarf is as devious and corrupt as the worst devil, yet  also unflinchingly loyal to his beholder master."
> — `sources/adventure-wdh.json:31696` (Appendix B; double spaces as in the source)

**Wiki, Personality (CaD era, wiki only)**
> "Ahmaergo had a fascination with [[minotaur]]s. He was devious and corrupt like a [[devil]] but totally loyal to his master.<ref name="WDH5e-p193" />"
> — `Ahmaergo.txt:64` (= `wiki.txt:1232`)

**Campaign, the Motivations line**
> "**Motivations.** Ahmaergo wants to maintain his position as the most influential member of the Guild after Xanathar, expand his minotaur collection, and run the Guild's operations with the efficiency that keeps the beholder's paranoia pointed at others."
> — `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:15` (the "collection" is supported by the adventure's X11, A8)

### A8. Signature belongings, quarters and the collection
**Wiki, carried objects (wiki only, CaD p. 141, 2e inferred)**
> "He usually had many magical objects on his person for self-defense.<ref name="CaD-p141" />"
> — `Ahmaergo.txt:67` (= `wiki.txt:1235`; "Possessions" heading)

**Adventure, a weapon (the inspection entry)**
> "If he sees intruders and is outnumbered, {@creature Ahmaergo|WDH} retreats to {@area X22|2a5}, heads downstairs to gather reinforcements from {@area X28|2b5}, and leads a search party to capture the interlopers. If he sees only one intruder, he draws his axe and attacks."
> — `sources/adventure-wdh.json:17552` (the paragraph begins "If he's not with Xanathar in the arena ... is conducting a routine inspection of the dungeon.")

**Adventure, X11 "Ahmaergo's Collection" (the stuffed minotaur)**
> "{@creature Xanathar|WDH}'s majordomo fetishizes minotaurs and has decorated this magically lit room accordingly:"
> followed by the list item:
> "A stuffed, glowering minotaur stands at the north end of the room. A large greataxe rests on a wooden rack in front of it."
> — `sources/adventure-wdh.json:17358` and `:17362` (X11, page 105, header at `:17354`)

> "When someone other than {@creature Ahmaergo|WDH} opens the southern door, the skeleton of the stuffed minotaur erupts out of its skin, becoming an animated {@creature minotaur skeleton}, and arms itself with the greataxe. It attacks all intruders, pursuing any who flee into {@area X8|27f} or X12. The minotaur skeleton obeys {@creature Ahmaergo|WDH}'s commands."
> — `sources/adventure-wdh.json:17381` (X11 "Stuffed Minotaur"; the greataxe is the minotaur's, not Ahmaergo's)

**Adventure, X12 "Ahmaergo's Quarters" (the maze, the bones and the bed)**
> "The room has been converted into a maze, its walls made of stacked crates nailed together with boards. The walls rise to meet the 20-foot-high ceiling."
> — `sources/adventure-wdh.json:17396` (X12 header at `:17388`, page 105)

> "Humanoid bones litter the floor. ({@creature Ahmaergo|WDH} gathered the bones from Undermountain and put them here as grisly decorations.)"
> — `sources/adventure-wdh.json:17397`

> "The maze fills the entire room but for a 10-foot-square area in the southwest corner, where {@creature Ahmaergo|WDH} keeps a wooden chest and a bed made from the skulls, bones, hide, and fur of minotaurs."
> — `sources/adventure-wdh.json:17400`

> "Getting through the maze takes time but isn't difficult, except that {@creature Ahmaergo|WDH} has rigged a tripwire halfway through."
> — `sources/adventure-wdh.json:17401` (the rest of the passage covers the spot check, the disarm and the 3d6 collapse)

**Adventure, X12 chest (treasure)**
> "{@creature Ahmaergo|WDH}'s chest contains 121 gp in a sack made of stitched flesh, a carved malachite figurine of a minotaur (worth 250 gp), and a {@item potion of healing}."
> — `sources/adventure-wdh.json:17408` (X12 "Treasure", page 105 at `:17406`)

**Alexandrian, the X12 chest contents (printed p. 88 [PDF p. 6]; transcription)**
> "X12 – Ahmaergo's Quarters: In addition to the normal entry for this room, the chest contains A Briefing for Xanathar Concerning the Grand Game."
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p. 88 [PDF p. 6]

### A9. Tournament role, the arena and the lair rosters
> "The lair holds a gladiatorial arena, the Pit of Blood and Fortune, where Ahmaergo presides over the tournaments and Noska releases the combatants (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:47` (the rest of the paragraph covers the tunnel, the secret staircase and the panopticus)

> "If the characters enter during a tournament, they see a {@creature minotaur} battling a scarred female halfling, {@creature Samara Strongbones|WDH} (see {@area X7|27e}). The halfling doesn't want to die in a pointless battle and screams for help. If the characters intervene, the arena spectators turn violent and attack them. If the characters let the fight play out, Noska escorts the victor back to {@area X7|27e} while {@creature Ahmaergo|WDH} goads characters into joining the tournament. If the characters aren't willing to enter the tournament, {@creature Ahmaergo|WDH} has them beaten {@condition unconscious} and locked up while {@creature Xanathar|WDH} watches silently."
> — `sources/adventure-wdh.json:17173` (sub-entry "Joining a Tournament", page 104 at `:17170`)

**Lair PDF, "A Private Fight" (printed p. 89 [PDF p. 7]; transcription)**
> "A PRIVATE FIGHT
> • Xanathar (invisible in southeast alcove)
> • Ahmaergo
> • Noska Ur'gray
> • 10 bandits + 5 bugbears as an audience
> • 2 goblins serving salted rat intestines and stirge meat pies
> • 1d4 random combatants from Area X7"
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p. 89 [PDF p. 7]

**Lair PDF, random encounter table (printed p. 89 [PDF p. 7]; transcription)**
> "d4 Encounter
> 1 Flutterfoot Zipswiggle (see DH p. 104)
> 2 Ahmaergo (conducting a routine inspection)
> 3 N'arl Xibrindas + Grell bodyguard
> 4 Ott Steeltoes"
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p. 89 [PDF p. 7]

**Lair PDF, the standard roster (printed p. 89 [PDF p. 7]; transcription, column layout not preserved)**: the roster lists "Ahmaergo (01-50%)" in the left column, between "Noska Ur'gray (25-50%) + Rust Monster" and "Thorvin Twinbeard".

**Lair PDF, "THE ARENA CROWD" (printed p. 90 [PDF p. 8]; transcription)**
> "THE ARENA CROWD:
> • Xanathar
> • Ahmaergo
> • Thorvin Twinbeard (01-50%)
> • Nihiloor (01-50%)
> • Ott Steeltoes
> • Nar'l Xibrindas (01-50%)"
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p. 90 [PDF p. 8]

**Appendix C, the lair random encounter**
> "Random encounters at each public area: 1 in 10 chance, 1d4 roll: 1 = Flutterfoot Zipswiggle (goblin; skittish, can be bribed with food), 2 = Ahmaergo (duergar; inspection; DC 15 Deception to pass as authorized), 3 = Nar'l Xibrindas + grell bodyguard, 4 = Ott Steeltoes."
> — `sources/Appendix_C_-_Player_Faction_Missions.md:1887` (species conflict, see D1; the Appendix C scene is a Bregan D'aerthe heist route, quest-time)

### A10. The Guild's logistics (day-one, campaign and villain page)
> "Ahmaergo is the outward face of Xanathar's Guild for administrative matters — a civil shield dwarf who manages procurement, discipline, and operations with methodical competence. He is as polite as he is dangerous."
> — `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:29` (the page's own Overview)

> "- Ahmaergo writes most of the orders that bear Xanathar's name."
> — `campaign/setting/history/02-the-long-shadow.md:44` (the line is a bullet in the Long Shadow's Guild section; the bullet's text is "Ahmaergo writes most of the orders that bear Xanathar's name.")

> "- **Maintain the Undercity.** Skullport supply lines fund the Guild. Method: Ahmaergo manages this operationally. Connects to Mad Mage integration."
> — `campaign/setting/villains/xanathar.md:63`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, current page: "*Shield dwarf majordomo, lawful evil, he/him*. Stat block: **Thug (with modifications)**." — `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:5`
- Campaign, Guild page: "- **Ahmaergo** (DH p. 195) — Shield dwarf majordomo, lawful evil." — `campaign/setting/organizations/08-xanathars-guild.md:101`
- Wiki infobox: "| alignment2e    = [[Lawful evil]]" (`Ahmaergo.txt:42`; `wiki.txt:1210`), "| alignment3e    = [[Lawful evil]]" (`Ahmaergo.txt:45`; `wiki.txt:1213`), "| alignment5e    = [[Lawful evil]]" (`Ahmaergo.txt:56`; `wiki.txt:1224`). The 2e and 3e fields are inferred editions; the 5e field carries the WDH5e refs at `Ahmaergo.txt:59`.
- Adventure: no alignment is given in the Ahmaergo entry (`sources/adventure-wdh.json:31692-31697`).
- Lair PDF: no alignment for Ahmaergo (stat reference, printed p. 91 [PDF p. 9]: "Ahmaergo – DH p. 193").

**Species**
- Campaign, current page: "*Shield dwarf majordomo ...*" (`02-ahmaergo.md:5`); Guild page: "Shield dwarf majordomo" (`08-xanathars-guild.md:101`).
- Wiki, race: "| race           = [[Dwarf]]<ref name="CaD-p141"/>" (`Ahmaergo.txt:13`; `wiki.txt:1181`).
- Wiki, ethnicity: "| ethnicity      = [[Shield dwarf]]<ref name="WDH5e-p193"/>" (`Ahmaergo.txt:14`; `wiki.txt:1182`).
- Adventure: "the shield  dwarf is as devious and corrupt as the worst devil" (`sources/adventure-wdh.json:31696`, quoted in A7).
- Appendix C: "2 = Ahmaergo (duergar; inspection; DC 15 Deception to pass as authorized)" (`sources/Appendix_C_-_Player_Faction_Missions.md:1887`). **Conflict, see D1.**

**Pronouns**
- Campaign: "he/him" (`campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:5`).
- Adventure: "to his beholder master" (`sources/adventure-wdh.json:31696`), and "If he sees only one intruder, he draws his axe and attacks." (`:17552`).
- Wiki: "| sex            = Male" (`Ahmaergo.txt:12`; `wiki.txt:1180`).

**Stat block**
- Campaign, current page: "Stat block: **Thug (with modifications)**." (`02-ahmaergo.md:5`). No source in the campaign, the adventure or the PDFs gives this label. See D2.
- Adventure: no Game Statistics block for Ahmaergo. The Appendix B entry (`sources/adventure-wdh.json:31692-31708`) ends with its image and goes straight to the next entry, Ammalia Cassalanter (`:31709`).
- Lair PDF, stat reference (printed p. 91 [PDF p. 9]; transcription): "Ahmaergo – DH p. 193" and "Noska Ur'gray – shield dwarf thug, MM p. 350 (DH p. 213)". The Lair PDF gives the "thug" label to Noska, and no label to Ahmaergo.
- Campaign structure, Bestiary note: "Custom stat blocks for Ahmaergo (minotaur veteran), Nar'l (drow mage + grell bodyguard), Nihiloor (mind flayer arcanist)." — `campaign/structure/arc-f-xanathars-lair.md:340`. The Bestiary is "not yet drafted" (same line group, `arc-f-xanathars-lair.md:340`).
- Wiki, challenge: "| challenge5e    = 9" (`Ahmaergo.txt:57`; `wiki.txt:1225`), refs "WDH5e-p193" (`Ahmaergo.txt:59`).

---

## C. Sentences on the current page that narrate quest events or day-one conflicts

Current page: `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md`. "Day-one OK" means no quest gate is needed. "Quest-time" means the sentence narrates a capture, mission, rescue, death, or an "after the party" event.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Shield dwarf majordomo, lawful evil, he/him*. Stat block: **Thug (with modifications)**." | Day-one. The stat label has no source (B, D2) | `organizations/08-xanathars-guild.md:101` (no stat); `arc-f-xanathars-lair.md:340` ("minotaur veteran") |
| 2 | L6 | "**Affiliation:** Xanathar's Guild" | Day-one OK | `organizations/08-xanathars-guild.md:8` (Contacts line) and `:101` |
| 3 | L7 | "**Featured in:** **Faction Outposts**, **Xanathar's Lair**, **Vault of Dragons**, **The Compromised Eye**, **The Dive**, **Force Grey Mission 4 — Destroy the Intellect Factory**" | Quest references (routed). The Force Grey entry has no Ahmaergo source (S1) | Faction Outposts: `arc-e-faction-outposts.md:153`, `:167`, `:169`, `:183`, `:351`. Xanathar's Lair: `arc-f-xanathars-lair.md:11`, `:41`, `:77`, `:111`, `:116`, `:124`, `:149`, `:163`, `:198`, `:200`, `:230`, `:283`, `:284`, `:299`, `:339`, `:340`. Vault of Dragons: `arc-j-vault-of-dragons.md:195`-`:197`. The Compromised Eye: `bregan-daerthe/m04-the-compromised-eye/overview.md:21`, `:27`, `:79`. The Dive: `bregan-daerthe/m06-the-dive/overview.md:23`, `:26`. Force Grey M4: none (S1) |
| 4 | L11 | "**Resonance.** Ahmaergo should inspire revulsion with his cruelty and minotaur obsession, wariness with his outward civility, and dark amusement at the absurdity of a dwarf who sleeps in a minotaur-bone bathtub." | Day-one attitude. "sleeps in a minotaur-bone bathtub" conflicts with the adventure's bed (D4) | `sources/adventure-wdh.json:17400` ("a bed made from the skulls, bones, hide, and fur of minotaurs") |
| 5 | L13 | "**Emotions.** Ahmaergo most often feels smug authority, methodical cruelty, possessive fascination with minotaurs, unflinching obedience to Xanathar, controlled satisfaction in discipline and order, and disdain for anyone weaker than himself." | Day-one. Obedience and minotaur fascination are supported (A7, A8) | `sources/adventure-wdh.json:31696`; `:14981` |
| 6 | L15 | "**Motivations.** Ahmaergo wants to maintain his position as the most influential member of the Guild after Xanathar, expand his minotaur collection, and run the Guild's operations with the efficiency that keeps the beholder's paranoia pointed at others." | Day-one. "expand his minotaur collection" is supported only by X11 (A8) | `organizations/08-xanathars-guild.md:43`; `sources/adventure-wdh.json:17354` |
| 7 | L17 | "**Inspirations.** When playing Ahmaergo, channel Oddjob (*Goldfinger*), Dolores Umbridge (*Harry Potter*), and Buffalo Bill (*Silence of the Lambs*)." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Ahmaergo is outwardly civil, a shield dwarf who handles logistics, procurement, and discipline with administrative calm. To those in the Guild, he is as devious and corrupt as the worst devil, yet unflinchingly loyal to Xanathar. Deep down, his quarters feature a maze of stacked crates, a stuffed minotaur, skeletal remains arranged as decor, and a bed made from minotaur skulls, bones, hide, and fur. The fascination is total." | Day-one. "his quarters" merges X12 (maze, bones, bed) and X11 (stuffed minotaur, "Ahmaergo's Collection") (D5) | `sources/adventure-wdh.json:31696`; `:17354`, `:17358`, `:17362`, `:17388`, `:17396`, `:17397`, `:17400`; `organizations/08-xanathars-guild.md:101` (handles logistics) |
| 9 | L23 | "**Morale.** In a fight, Ahmaergo commands Guild forces and fights with vicious competence. He does not retreat while Xanathar is present, and he responds to the beholder's screamed orders without hesitation." | Day-one behaviour. "He does not retreat while Xanathar is present" has no source (F9). "screamed orders" is supported by `:14981`. The inspection retreat (`:17552`) is conditioned on Xanathar not being present | `sources/adventure-wdh.json:14981`; `:17552`; `campaign/structure/arc-f-xanathars-lair.md:200` (Stage 4: "Ahmaergo abandons his team position and moves directly to X19", a quest-time response, routed) |
| 10 | L25 | "**Relationships.** Ahmaergo is Xanathar's majordomo (most orders that bear Xanathar's name were written by Ahmaergo), the Guild's de facto second-in-command, and a shield dwarf whose minotaur obsession fills every corner of his quarters." | Day-one. "de facto second-in-command" has a source only in the GM Guide's Holder text (`campaign/guides/gm-guide/debts-of-the-city.md:112`, "operational second-in-command"). "fills every corner of his quarters" is a stylised reading of X11/X12 | `organizations/08-xanathars-guild.md:101`; `history/02-the-long-shadow.md:44`; `campaign/guides/gm-guide/debts-of-the-city.md:112` |
| 11 | L29 | "Ahmaergo is the outward face of Xanathar's Guild for administrative matters — a civil shield dwarf who manages procurement, discipline, and operations with methodical competence. He is as polite as he is dangerous." | Day-one. Overview | `organizations/08-xanathars-guild.md:101` |

**Quest-time clauses in the page body:** none found outside the Featured-in line (row 3). The page does not narrate a capture, mission, rescue or death.

**Quest-time material routed to quest files (already there, not day-one):**
- Lair heist: Ahmaergo's alert posture and response (`campaign/structure/arc-f-xanathars-lair.md:198`, `:200`, `:230`; `:124` "Posts doubled; Ahmaergo patrols X12–X18"; `:116`; `:163`).
- Lair opener (backstory): "Ahmaergo runs external operations while Xanathar broods in the Sanctum" (`campaign/structure/arc-f-xanathars-lair.md:11`). The same paragraph opens "The lair beneath Skullport has been sealed for weeks. Since the fireball disrupted the Street of Silver trade routes, ..."
- Lair fail states: `arc-f-xanathars-lair.md:111` ("The Guild collapses into factional fighting between Ahmaergo and surviving lieutenants."), `:283` ("Ahmaergo takes over lair security."), `:284` ("Guild collapses into Ahmaergo-led factional fighting.").
- Vault of Dragons: `campaign/structure/arc-j-vault-of-dragons.md:195`-`:197` (three Xanathar states: "Xanathar itself directing an elite Guild bodyguard complement, with Ahmaergo at its side", "Ahmaergo leading a handful of Guild agents — opportunistic rather than personal", "Ahmaergo arrives alone or with one lieutenant, without Xanathar's authority behind him").
- Vault bargain (adventure, conditional on giving Xanathar the Stone): `sources/adventure-wdh.json:14980` ("If the characters give {@creature Xanathar|WDH} the stone, it demands that they accompany it to the Vault of Dragons and help it defeat the vault's draconic guardian. Not fully trusting the characters to keep their part of the bargain, {@creature Xanathar|WDH} brings along its majordomo, {@creature Ahmaergo|WDH}, to keep an eye on them.").
- Tournament joining (adventure, PC interaction): `sources/adventure-wdh.json:17173` (A9).
- Compromised Eye (Bregan D'aerthe quest): `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/overview.md:79` ("- **Ahmaergo** (Xanathar's Guild): holds the case against Nar'l, and does not appear."); `ev-01-the-compromised-eye.md:20`; `ev-02-twelve-minutes.md:59`, `:98`.
- The Dive (Bregan D'aerthe quest): `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/overview.md:23` ("Ahmaergo has treated Bregan D'aerthe as the Guild's enemy for some time, and a submarine the captain cannot replace is the cleanest blow he can land. He sent Orlo Stannick, a salvage diver who has worked for the Guild for years, with a ship-breaker charge: ...") and `ev-01-the-dive.md:17` ("Ahmaergo has had the Guild's clerks watching for the captain's submarine for months.").
- Faction Outposts (Terasse Estate letters): E3.
- Harpers: `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-02-the-extraction.md:150` (E3).
- Jarlaxle impersonates Ahmaergo during the lair heist: `sources/11. Lair  Xanathar’s Lair.pdf`, printed p. 86 [PDF p. 4] (E3).

**Voice profile quest-time clauses** (`.claude/skills/character-voices/voices/xanathars-guild.md`, "### Ahmaergo" at line 29, through line 43):
- No quest-time clause found. Every profile line (Sound, Sentence shape, Word choice, Swearing, Personality in speech, Quirks, Signature phrases, Never, Sample lines) describes his speech or behaviour in general. The sample business line and the under-pressure line are day-one.
- Vocabulary check for the drafter (ruling 9): the profile's Word choice line reads "He calls the Xanathar "the Master" with complete reverence." (line 34), and the Never line reads "never questions the Xanathar" (line 39). These are in the profile's narration, not in a speech tag. Wiki support for "the Xanathar" as a title (wiki only): "The Eye proceeded to take over the Xanathar Guild operations and renamed itself "the Xanathar," starting the Guild's tradition of using the name as a title." (`wiki.txt:131`, *Cloak & Dagger* p. 140, 2e inferred).
- Swearing line as written (line 35): "*Never · Plain · n/a.* Profanity is disorderly. Cruelty is his vocabulary instead."

**Voice profile text (verbatim; `.claude/skills/character-voices/voices/xanathars-guild.md:29-43`):**
> "### Ahmaergo
> *The Guild's civil, fussy majordomo, polite as a clerk and cruel as a butcher.*
> - **Sound:** A precise, clipped dwarven voice, dry and formal, like a bookkeeper reading a ledger.
> - **Sentence shape:** Orderly, administrative sentences: procedures, schedules, disciplinary outcomes. It's polite phrasing throughout, deliberately (a break from `ember-voice` speech), and he never contracts.
> - **Word choice:** Bureaucratic cruelty: "disciplinary procedure", "requisition", "regrettable but necessary". He calls the Xanathar "the Master" with complete reverence. Minotaurs he discusses with the zeal of a collector.
> - **Swearing:** *Never · Plain · n/a.* Profanity is disorderly. Cruelty is his vocabulary instead.
> - **Personality in speech:** Smug authority and methodical cruelty. He describes punishments in procedural detail. His obsession with minotaurs surfaces as sudden animated enthusiasm, then he returns to calm.
> - **Quirks:** He consults a list before answering. He mentions minotaur anatomy unprompted. He thanks people for their cooperation before hurting them.
> - **Signature phrases:** "Procedure must be followed." / "The Master is not to be disturbed." / "Thank you for your cooperation."
> - **Never:** He never raises his voice, never questions the Xanathar, and never lets disorder pass.
> - **Sample lines:**
>   - *Greeting:* "You are not on the list. That is regrettable. State your business, and do not touch the minotaur."
>   - *Business:* "Deliveries are to be made at the second bell to the lower stair. Late deliveries are subject to disciplinary procedure."
>   - *Under pressure:* "Guards. Procedure four. Thank you for your cooperation."
> — `.claude/skills/character-voices/voices/xanathars-guild.md:29-43`

---

## D. Conflicts (both sides quoted; higher-ranked source first)

**D1. Species: "shield dwarf" against "duergar"**
- Higher: "*Shield dwarf majordomo, lawful evil, he/him*" (`campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:5`); "Shield dwarf majordomo, lawful evil." (`campaign/setting/organizations/08-xanathars-guild.md:101`); "the shield  dwarf is as devious and corrupt as the worst devil" (`sources/adventure-wdh.json:31696`).
- Lower: "2 = Ahmaergo (duergar; inspection; DC 15 Deception to pass as authorized)" (`sources/Appendix_C_-_Player_Faction_Missions.md:1887`).
- Wiki: "| ethnicity      = [[Shield dwarf]]<ref name="WDH5e-p193"/>" (`Ahmaergo.txt:14`) agrees with "shield dwarf".
- Higher source: the campaign and the adventure. Appendix C is a Bregan D'aerthe heist route (quest-time). The "duergar" is the outlier.

**D2. Stat block label: "Thug (with modifications)" against no stat block and "minotaur veteran"**
- Page: "Stat block: **Thug (with modifications)**." (`02-ahmaergo.md:5`).
- Campaign structure, Bestiary plan: "Custom stat blocks for Ahmaergo (minotaur veteran), Nar'l (drow mage + grell bodyguard), Nihiloor (mind flayer arcanist)." (`campaign/structure/arc-f-xanathars-lair.md:340`).
- Lair PDF (printed p. 91 [PDF p. 9]): "Ahmaergo – DH p. 193" (no label). The same stat reference gives Noska "shield dwarf thug, MM p. 350 (DH p. 213)".
- Adventure: no Game Statistics for Ahmaergo (see B).
- Wiki: "| challenge5e    = 9" (`Ahmaergo.txt:57`).
- Higher: none settles it. The page and the structure doc are both campaign files. The orchestrator decides.

**D3. Page reference: "DH p. 195" against "DH p. 193"**
- Campaign Guild page: "- **Ahmaergo** (DH p. 195) — Shield dwarf majordomo, lawful evil." (`campaign/setting/organizations/08-xanathars-guild.md:101`).
- Adventure Appendix B entry: `"name": "Ahmaergo"`, `"page": 193` (`sources/adventure-wdh.json:31692-31693`); index: "81. Ahmaergo" (`:32980`).
- Lair PDF: "Ahmaergo – DH p. 193" (printed p. 91 [PDF p. 9]).
- Wiki: "<ref name="WDH5e-p193"/>" throughout (`Ahmaergo.txt:61`, `:64`, `:79`).
- Higher source: the adventure and the Lair PDF (p. 193). The Guild page's "195" is the outlier.

**D4. Where he sleeps: "bathtub" against "bed"**
- Page Resonance: "dark amusement at the absurdity of a dwarf who sleeps in a minotaur-bone bathtub" (`02-ahmaergo.md:11`).
- Page Persona: "a bed made from minotaur skulls, bones, hide, and fur" (`02-ahmaergo.md:21`).
- Adventure: "a bed made from the skulls, bones, hide, and fur of minotaurs" (`sources/adventure-wdh.json:17400`).
- Higher: the adventure. The Resonance line is the outlier. The Persona line matches the adventure.

**D5. The stuffed minotaur and the bones sit in two different rooms**
- Page Persona: "his quarters feature a maze of stacked crates, a stuffed minotaur, skeletal remains arranged as decor, and a bed made from minotaur skulls, bones, hide, and fur" (`02-ahmaergo.md:21`).
- Adventure X11 "Ahmaergo's Collection": "A stuffed, glowering minotaur stands at the north end of the room." (`sources/adventure-wdh.json:17362`), in a room separate from X12 "Ahmaergo's Quarters" (`:17388`).
- Higher: the adventure. A room-level difference for the drafter to settle.

**D6. Trust and motive (wiki against campaign)**
- Wiki: "the Xanathar did not fully trust him and kept a close watch on him ... He was starting to get ambitious, wanting to leave the Xanathar and work as an independent slaver." (`Ahmaergo.txt:74`; CaD p. 141, 2e inferred).
- Campaign Villains table: "Most trusted lieutenant; the only one Xanathar registers as competent" (`campaign/setting/villains/xanathar.md:47`).
- Campaign Motivations: "Ahmaergo wants to maintain his position as the most influential member of the Guild after Xanathar" (`02-ahmaergo.md:15`).
- Adventure: "Killing one of Xanathar's most trusted underlings, such as Ahmaergo or Noska Ur'gray" (`sources/adventure-wdh.json:15041`).
- Higher: campaign and adventure. The wiki is 2e-era and last-ranked.

**D7. The Guild's rank ladder against the wiki's Hand ranks**
- Campaign: "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e)." (`08-xanathars-guild.md:45`).
- Wiki, 1372 DR: "From lowest to highest, their ranks were Third of the Hand, Second of the Hand, and the Command of the Hand." (`wiki.txt:77`; 2e inferred).
- Higher: the campaign ladder (5e). The wiki's Hand ranks are a different (Eye-era) structure. Ahmaergo's title "Third of the Hand" (`Ahmaergo.txt:6`) is wiki-only.

**D8. The 1368 DR date (campaign Draft Note against wiki text)**
- Campaign Draft Note: "The wiki names Ahmaergo (a Master in 1372 DR and a slaver leader in 1368 DR)" (`campaign/setting/history/02-the-long-shadow.md:148`).
- Wiki Ahmaergo text: "since [[1370 DR]]" (`Ahmaergo.txt:61`); no 1368 for Ahmaergo.
- Wiki Avaereene text: "by [[1368 DR]]–[[1370 DR]] was coordinating activities behind the scenes." (`wiki.txt:1344`).
- The campaign note outranks the wiki, but the wiki copies held here do not carry the 1368 claim, so the note has no visible source. Not resolved.

**D9. Noska rivalry: attribution**
- `sources/SOURCE_GUIDE.md:343` attributes "Noska vs. Ahmaergo rivalry" to the Lair PDF (under the heading at line 335).
- Lair PDF (printed pp. 83-91): no rivalry text.
- Campaign structure: "The Noska–Ahmaergo rivalry has reached near-blows twice in the past month;" (`arc-f-xanathars-lair.md:41`).
- Higher: the campaign line is the only text found with the rivalry. It sits in the structure doc, not in the PDF that SOURCE_GUIDE names. Not resolved; orchestrator decides.

**D10. Ahmaergo's "Guild contacts" label**
- Campaign, Gamemaster's Summary: "**Contacts:** **Ahmaergo**, **Keln Trigos** (Guild contacts in the city)" (`organizations/08-xanathars-guild.md:8`).
- Campaign, Key Members and Structure: "Shield dwarf majordomo" (`:101`); "the most influential member after the beholder" (`:43`).
- Not a flat conflict. The Guild page's summary calls him a contact; its body calls him the majordomo. The page's Affiliation bullet ("Xanathar's Guild", `02-ahmaergo.md:6`) matches both.

**D11. "Ahmaergo runs external operations" against the tournament role**
- Campaign opener: "Ahmaergo runs external operations while Xanathar broods in the Sanctum" (`arc-f-xanathars-lair.md:11`).
- Adventure: "... two dwarves: ... Ahmaergo ..., who presides over fight tournaments" (`sources/adventure-wdh.json:17166`).
- Lair PDF: "THE ARENA CROWD: ... Ahmaergo" (printed p. 90).
- Not a flat conflict. The opener is a quest-time state (sealed lair, "for weeks"). The adventure's tournament role is the standing lair. Routed.

---

## E. Stale lines in other files (not edited) and routed references

**E1. Stale, retired or framing lines naming Ahmaergo**
- `campaign/structure/ch1-beginning.md:221-228` (retired file, "Redemption — Ahmaergo's Inventory"): "Ahmaergo — Xanathar's dwarven majordomo, the man who actually runs the organization's logistics — keeps a private ledger separate from the official records." Retired.
- `campaign/structure/ch2-city-of-splendors.md:199` ("| Ahmaergo | Majordomo | Most trusted lieutenant; the only one Xanathar registers as competent; Ahmaergo knows he is replaceable |") and `:210` ("3. **Maintain the Undercity** — Skullport supply lines fund the Guild; method: Ahmaergo manages this operationally; connects to Mad Mage integration"). Retired.
- `campaign/setting/organizations/08-xanathars-guild.md:101` "(DH p. 195)" (D3).
- `campaign/structure/arc-f-xanathars-lair.md:340` "minotaur veteran" (D2).
- `campaign/setting/history/02-the-long-shadow.md:148` (D8).
- `sources/SOURCE_GUIDE.md:343` (D9).
- `campaign/structure/arc-e-faction-outposts.md:169` ("*Intel Yield.* The Ahmaergo correspondence confirms the Terasse connection and establishes Ahmaergo as a named Guild lieutenant."). This reads as if the outpost first names him. The Guild page and the adventure already name him (`organizations/08-xanathars-guild.md:101`; `sources/adventure-wdh.json:31692`). Quest framing; routed.

**E2. Bundle copies (not edited)**
- `sources/research/pass4-bundles/faction-knowledge/wiki.txt:1155-1247` holds a second copy of the Ahmaergo wiki page (same text; scratch line n = pass4 line n+1149, checked at the lead: scratch line 61 = pass4 line 1210). `sources/research/pass5-bundles/xanathars-guild/wiki.txt` is the copy this report cites as `wiki.txt`.
- `sources/research/pass3-bundles/guilds/campaign-hits.txt:750` quotes the history Draft Note at an old line number (153). The current line is `campaign/setting/history/02-the-long-shadow.md:148`.

**E3. Routed to quests (where the quest-time facts already live)**

Faction Outposts (Terasse Estate, Orb Confectioners, Zhentarim Interrogation House):
- `campaign/structure/arc-e-faction-outposts.md:153` ("*Step 4 — The Operation.* Primary objectives: recover the *Instructions for Gladiatorial Weaponry* from Keln's desk (Area 6–7), which names Grinda Garloth as the supplier and Ahmaergo as the authorizing agent; ...")
- `campaign/structure/arc-e-faction-outposts.md:167` ("*Key Areas.* Area D2: 500 gp and the *Note Regarding Gladiatorial Weaponry* from Ahmaergo, confirming delivery to Terasse Estate and citing Xanathar's expectation of "exotic gutting." ...")
- `campaign/structure/arc-e-faction-outposts.md:183` ("*Key Areas.* Area B7: *On the Delivery of a Mechanical Beholder* from Ahmaergo, setting a delivery deadline of Tarsakh 9th for a mechanical beholder to Terasse Estate — confirms the gladiatorial supply chain and ties Ahmaergo to Xanathar's engineering operations. ...")
- `campaign/structure/arc-e-faction-outposts.md:351` ("*Response Team Compositions.* ... Xanathar teams carry operational correspondence from Nar'l or Ahmaergo; ...")
- `campaign/guides/factions/09-xanathars-guild.md:29` ("**Area 6–7 — Master Suite.** Keln's desk holds *Instructions for Gladiatorial Weaponry* from Ahmaergo: a shipment of exotic weapons is being sent by Grinda Garloth for the next gladiatorial audience.")
- `campaign/guides/factions/09-xanathars-guild.md:43` ("**Area D2 — Grinda's Chest.** 500 gp and the *Note Regarding Gladiatorial Weaponry* from Ahmaergo, confirming the weapon delivery to Terasse Estate and citing Xanathar's expectation of "exotic gutting."")
- `campaign/guides/factions/09-xanathars-guild.md:57` ("**Area B7 — Mechanical Beholder.** A letter among the equipment: *On the Delivery of a Mechanical Beholder* from Ahmaergo, threatening death if the mechanical beholder is not delivered to Terasse Estate by the ninth of Tarsakh.")
- Alexandrian Outposts, printed p. 43 [PDF p. 8] (Terasse Estate, Area 6-7 Desk; transcription): "Instructions for Gladiatorial Weaponry: "The shipment of special weapons that X requested will be sent by Grinda Garloth in Mistshore. See that they're bundled up and sent along with the next audience procession. -Ahmaergo" (GM Note: If it becomes notable, this is simple a bunch of vicious-looking oddities — many of them foreign weapons from distant lands — destined for the gladiatorial combats.)"
- Alexandrian Outposts, printed p. 44 [PDF p. 9] (Area D2; transcription): "A Note Regarding Gladiatorial Weaponry: "Xanathar wants the full bundle of weaponry delivered to Terasse's house of healing on Elsambul's Lane no later than two days from now so that it can be sent down to headquarters with the next gladiatorial audience. Don't be late! He's looking forward to seeing some exotic gutting. -Ahmaergo" (GM Note: If it becomes notable, this is simple a bunch of vicious-looking oddities — many of them foreign weapons from distant lands — destined for the gladiatorial combats.)"
- Alexandrian Outposts, printed p. 44 [PDF p. 9] (Area B7; transcription): "On the Delivery of a Mechanical Beholder: "X is outraged that you bungling incompetents couldn't get his piece de triumphe working for the Shipwrights' Ball! If it isn't seen swooping over the Feasts of Leirun, he'll have your guts for garters! See that it's delivered to Terasse's house of healing on Elsambul's Lane by the ninth of Tarsakh or be prepared to pay for it with your heads! -Ahmaergo""
- Revelation list, printed p. 123 [PDF p. 3] (transcription): under "XANATHARIAN LOCATIONS / GRINDA GARLOTH": "Note Regarding Gladiatorial Weaponry (Terasse Estate)". Under "LAIR: XANATHAR'S LAIR" the list has "A Note Regarding Gladiatorial Weapons (Grinda Garloth)". Ahmaergo is not named anywhere in the revelation list.

Xanathar's Lair (quest-time):
- `campaign/structure/arc-f-xanathars-lair.md:11`, `:41` (quoted in S2), `:77`, `:111`, `:116`, `:124`, `:149`, `:163`, `:198`, `:200`, `:230`, `:283`, `:284`, `:299`, `:339`, `:340`.
- `arc-f-xanathars-lair.md:149`: "**X12 — Ahmaergo's Quarters.** Organized with obsessive precision: fight records, tournament schedules, arena financial ledgers, a battered sparring sword from Baldur's Gate. On the desk: *Briefing for Xanathar Concerning the Grand Game*. The document covers the current state of the Stone competition — intelligence on the Cassalanters, the Bregan D'aerthe (incomplete), and a physical description of the party accurate enough to confirm they've been watched. Ahmaergo knows who the party is."
- `arc-f-xanathars-lair.md:77`: "This means the party cannot simply walk into X19 and take the Eye — not unless they create a window. The dream nullifier in X20 exists for this purpose: destroying it sends Xanathar into the corridor to find Ahmaergo, giving the party approximately 4 minutes. ..."
- `arc-f-xanathars-lair.md:198`: "**Stage 3 — Full Alert.** Trigger: a named NPC (Ahmaergo, Nar'l, Noska) confirms combat with intruders. Response: all off-duty Guild members in X28 and X8 mobilize; Ahmaergo leads a team toward the reported position; Xanathar retreats to X19 with four Guild Soldiers. Response time: 1d6 minutes from Stage 2."
- `arc-f-xanathars-lair.md:299`: "- **Tashlyn or Davil:** "Is Xanathar still operational?" Direct and tactical — the Doom Raiders' expansion into former Guild territory depends on the answer. "And Ahmaergo?""

Vault of Dragons:
- `campaign/structure/arc-j-vault-of-dragons.md:195`-`:197` (quoted in C).

Compromised Eye and The Dive (Bregan D'aerthe):
- `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/overview.md:21` ("Nar'l has served as Xanathar's drow advisor for a year and has reported to Bregan D'aerthe by *Sending* every third day. ... and Ahmaergo's clerks noticed the gap."), `:27` ("Ahmaergo's case is real but thin. It rests on three unsent Dock Ward reports and on a fence named Tarn Hobble, ..."), `:79`.
- `m04-the-compromised-eye/design-notes.md:15` ("... Ahmaergo's clerks hold three unsent reports and a fence's word, and the discredit route attacks both. ..."), `:27`.
- `m04-the-compromised-eye/ev-01-the-compromised-eye.md:20`, `:260` ("I had no answer for Ahmaergo's clerks.").
- `m04-the-compromised-eye/ev-02-twelve-minutes.md:7`, `:39`, `:59` ("He is the second leg of Ahmaergo's case, ..."), `:65`, `:85`, `:98` ("The clerk comes back to an empty shop and a missing informant, which draws Ahmaergo's interest. ..."), `:103`, `:123`.
- `campaign/guides/factions/08-bregan-daerthe.md:69` ("| 5th | **The Compromised Eye** | Extract or protect Nar'l Xibrindas, the BD mole embedded in Xanathar's Guild. Jarlaxle forbids killing him — Nar'l is more valuable alive and in position. Three approaches: feed him a false report, extract him from the city, or confront Ahmaergo's counterintelligence source. | +3 |").
- `m06-the-dive/overview.md:26` ("... Nar'l Xibrindas leaked it in grief. He wanted standing with Ahmaergo and wanted to hurt the captain who didn't avenge his brother.").
- `m06-the-dive/ev-01-the-dive.md:28`, `:29` ("Two of Ahmaergo's clerks and a paid ferryman logged the gnome engineers' ballast runs along the pier for three nights."), `:87`, `:186`, `:201`, `:298`, `:320`, `:324` ("Ahmaergo had it from the Guild's own court, a soft-spoken drow in a Guild coat who gave it up over tea.").
- `m06-the-dive/ev-02-before-dawn.md:237`, `:238`.
- `m06-the-dive/design-notes.md:7` ("***The Guild is after an asset, not a prize.*** Ahmaergo treats Bregan D'aerthe as the Guild's enemy ...").

Harpers:
- `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-02-the-extraction.md:150` ("> > "Ahmaergo and Noska Ur'gray run the Dock Ward routes, and the restricted deliveries all went to Nihiloor's rooms in the lair. I kept the labels with my account, so give them to Mirt before you go below."").
- `ev-02-the-extraction.md:158` ("> > "Those warehouses are still open under Ahmaergo's captains, and Nihiloor kept a clerk in the Watch office and two runners on the docks. They're the ones still carrying orders, and I can tell you who meets whom."").

Lair PDF (printed p. 86 [PDF p. 4]; transcription): "After locating the Eye, they go down the emergency escape route to X21. Jarlaxle uses his *hat of disguise* to don the appearance of Ahmaergo, orders the guards to assist in the commotion downstairs, meets up with the rest of his team as they emerge back up the stairs and through Area X22, and then heads for the exit."

**Debts (Players' and GM Guides; a mechanic, not a figure page)**
- `campaign/guides/players-guide/debts-of-the-city.md:15` ("| 5 | Redemption | Ahmaergo's Inventory |") and `:63` ("Ahmaergo, Xanathar's dwarven majordomo and the man who actually runs the Guild's logistics, keeps a private ledger separate from the official records. Your name is in it, under a column that reads *Outstanding*.") and `:65` ("*Your character knows the following:* The Guild doesn't know, officially, that you exist. Ahmaergo knows. He made one indirect inquiry months after the event, to confirm you were still in Waterdeep and still capable. You confirmed both by answering.").
- `campaign/guides/gm-guide/debts-of-the-city.md:112` ("Ahmaergo is the majordomo of Xanathar's Guild: a shield dwarf of outward civility and exacting administrative competence who functions as the Guild's operational second-in-command. Most orders that bear Xanathar's name were drafted by Ahmaergo. His private ledger is separate from official Guild records because Xanathar doesn't know about every arrangement he makes, which is precisely the point.") and `:117` ("Ahmaergo keeps his private ledger separate from Guild records because Xanathar doesn't know about every arrangement he runs. ...").

**E4. Other Notable Figures pages that name Ahmaergo**
- `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:24` ("**Morale.** In a fight, Xanathar uses its eye rays without restraint. If reduced to half hit points or believing itself in mortal danger, it activates its ring of invisibility, screams for Ahmaergo to "tear the usurpers limb from limb," and flees to its sanctum.") and `:26` (quoted in A6).
- `campaign/setting/notable-figures/xanathars-guild/06-ott-steeltoes.md:18` ("He became good friends with **Ahmaergo**, and the two dwarves often drank together (same page) `[research: wiki only]`."), `:38` ("- **Ahmaergo:** The Guild's shield dwarf majordomo and, by one account, Ott's good friend. ..."), `:103` ("- **Xanathar** and **Ahmaergo** (Notable Figures): Ott's master and his friend").
- Grep of `campaign/setting/notable-figures/` for Ahmaergo finds only `01-xanathar.md`, `06-ott-steeltoes.md` and the target `02-ahmaergo.md`.

**E5. Source guide**
- `sources/SOURCE_GUIDE.md:29`: "- **Chapter 5 — Spring Madness (Xanathar):** Full Xanathar's Lair keyed location (36 areas), the gladiatorial tournament approach, Xanathar NPC, Ahmaergo, Noska Ur'gray, Nar'l Xibrindas, Nihiloor, Ott Steeltoes (Sylgar the goldfish keeper), Thorvin Twinbeard (Harper informant). Contains: dream nullifier artifact, panopticus surveillance description, connection tunnels to Undermountain Level 1."
- `sources/SOURCE_GUIDE.md:343` (D9).

---

## F. Gaps (what a Background would need that no source gives)

1. **Birth, family, early life.** No campaign file and no adventure line. The wiki gives the nickname "Horned Dwarf" (`Ahmaergo.txt:8`) and the title "Lord of Iron" (`Ahmaergo.txt:6`), both wiki-only. No inference is supported. The Background can say the sources do not give an origin, or leave it out.
2. **Joining the Guild.** No Ahmaergo-specific entry. The wiki places him in the slave trade "since 1370 DR" (`Ahmaergo.txt:61`), with the Iron Ring named in the same lead and in `Ahmaergo.txt:76`. A modest inference, tagged `[research]`, would connect the slave-trade entry to the campaign's general entry test (`organizations/08-xanathars-guild.md:32`). The wiki gives no entry scene.
3. **Iron Ring.** Wiki only (`Ahmaergo.txt:61`, `:76`). No campaign file names the Iron Ring. Use only as `[research: wiki only]`, or leave it out.
4. **Rise to majordomo.** No campaign line gives the step. The wiki gives "Around 1492 DR" (`Ahmaergo.txt:79`) and no earlier promotion. The campaign's own description is "Xanathar's majordomo" (`organizations/08-xanathars-guild.md:101`), with no date.
5. **Ranks and titles.** "Third of the Hand" and "Master of Slavery" (`Ahmaergo.txt:6`) and the 1372-era Hands (`wiki.txt:77`) are 2e-inferred. The 5e ladder (`organizations/08-xanathars-guild.md:45`) has no Ahmaergo rank. The campaign's own words for his standing are "the most influential member after the beholder" (`organizations/08-xanathars-guild.md:43`).
6. **Relationship to Avaereene (slave-taker).** Wiki only (`Ahmaergo.txt:74`); the wiki spells the name "Avaereene". The campaign has "Avareen Windrivver", a Zhentarim interrogation operative (`campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md`). The sources held here do not identify the two as one figure.
7. **Friendship with Ott Steeltoes.** Wiki only (`wiki.txt:1901`, CaD p. 143, 2e inferred). No campaign line. Use as `[research: wiki only]`.
8. **Age.** No source gives Ahmaergo's age.
9. **Faith.** No source gives any faith.
10. **Signature belongings.** Wiki: "He usually had many magical objects on his person for self-defense." (`Ahmaergo.txt:67`, wiki only). Adventure: "he draws his axe" (`sources/adventure-wdh.json:17552`) and the X12 chest (`:17408`). The axe is not identified as magic.
11. **Quarters vs collection.** X11 and X12 are separate rooms (`sources/adventure-wdh.json:17354`, `:17388`); the page calls both "his quarters" (`02-ahmaergo.md:21`). See D5.
12. **The 1368 DR date.** The campaign note asserts a "slaver leader in 1368 DR" for Ahmaergo (`history/02-the-long-shadow.md:148`); no wiki text held here says it (S3, D8).
13. **Why Xanathar trusts him.** Not sourced. The Villains table says "Most trusted lieutenant" (`xanathar.md:47`); the wiki says Xanathar "did not fully trust him" (`Ahmaergo.txt:74`). See D6.
14. **Stat block and CR.** The campaign label is unsourced (D2). The wiki's CR 9 (`Ahmaergo.txt:57`) is wiki-only and cites WDH p. 193.
15. **"Does not retreat" and "minotaur-bone bathtub".** Unsourced (C rows 4 and 9; D4).
16. **Tenure dates.** No dated tenure in the campaign. The wiki's "since 1370 DR" (`Ahmaergo.txt:61`) is CaD-era.
17. **Bepis Honeymaker (cook).** The adventure gives Ahmaergo a kidnapped cook: "{@creature Ahmaergo|WDH} has put him to work as a cook but threatens to give him over to the mind flayer {@creature Nihiloor|WDH} every so often." (`sources/adventure-wdh.json:17989`). No campaign file names Bepis. Use as `[research]` if needed; it is a lair-state detail.
18. **Force Grey Mission 4.** No source (S1). The Featured-in bullet has no Ahmaergo support in the folder.
19. **The Noska rivalry.** Only in `arc-f-xanathars-lair.md:41` (S2, D9). SOURCE_GUIDE attributes it to the Lair PDF, which does not contain it.
20. **Pronouns**: sourced (he/him). No gap.

---

## Not readable

- None of the named sources failed to open. The PDFs were read as rendered images (no `pdftotext` in this session). Their quotes are transcriptions and need a `pdftotext -layout` check before any prose use.
- `sources/Other remix files/*.docx` were not opened (the tools cannot read `.docx`). `sources/SOURCE_GUIDE.md:695` describes one of them as a broad NPC reference that may hold Ahmaergo's entry: "| `The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` | Broad NPC reference — use as a secondary source; the individual guides above supersede this where they overlap | Secondary reference only |". Name it for the caller to extract. `Xoblob_s Shop, NPC guide to his trinkets and roll tables.docx` (`SOURCE_GUIDE.md:697`) concerns a Guild informant and was not opened.
- `sources/research/` bundles were searched by Grep only, except the two wiki copies read in full for the Ahmaergo passages.

## Not run
- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
