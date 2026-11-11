# Batch H research report: Lolth, Eilistraee, Ghaunadaur, Corellon Larethian, Garl Glittergold

## Method and conventions

- Read: `docs/plans/setting-compendium-pass2-brief.md`, `campaign/setting/deities/asmodeus.md` (template), and for each power the bundle files `5etools.md`, `wiki.txt` (read in full), `campaign-hits.txt` and `adventure-hits.txt` under `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/<slug>/`.
- Targeted Grep of `/home/user/waterdeep/campaign` and of `sources/adventure-wdh.json` and `sources/adventure-wdmm.json` for every alias below. Read `sources/adventure-wdh.json` lines 30905 to 31000 for the "Major Temples of Waterdeep" table.
- Not opened (out of scope in the brief): the Alexandrian PDFs, `sources/SOURCE_GUIDE.md`, and the markdown files `sources/Appendix_C_-_Player_Faction_Missions.md` (6 alias matches), `sources/Appendix_D_-_Running_the_Tavern.md` (3) and `sources/Act_III_Arc_D.md` (1). Grep counted these; they were not read.
- Wiki quotes drop the `[[ ]]` link brackets only (a piped link keeps its visible text). `{{ }}` templates and `<ref>` tags are kept so each edition citation stays visible. Nothing else in a wiki quote is changed. Where a quote stops inside a multi-line citation, the report says so.
- 5etools quotes are copied from `5etools.md`. JSON quotes keep their escapes (`\"`) as they appear in the file.
- Every quote is followed by its own line, starting with an em dash, giving the file and line.
- The cap of 6 quotes per field is applied, except the Lolth list of every campaign line, which the brief requires in full.

## Bundle gaps

1. Lolth `campaign-hits.txt` misses `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:379` (the answer says "Spider Queen", not "Lolth") and `campaign/quests/faction-events/bregan-daerthe/r50-houseless-noble/design-notes.md:9` (it says "the rejected goddess" without naming her). Both are quoted below.
2. The `campaign-hits.txt` files for Eilistraee and Ghaunadaur are empty. Garl's `campaign-hits.txt` and `adventure-hits.txt` are empty. Grep confirms zero campaign matches for Eilistraee and Ghaunadaur, and zero matches for Garl in `campaign/` and in both adventure JSON files.
3. Corellon `campaign-hits.txt` has 39 lines: 38 are the shop name "Corellon's Crown" and 1 names the god (`campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:26`).
4. Noise for Garl: the string "Garl" also matches "Grinda Garloth" and "Garlynth Ironhead". Neither is the god.

---

## 1. LOLTH

### Field 1: Identity

**A. 5etools FRHoF p.113**
> ## Lolth | source FRHoF p.113 | pantheon Faerûnian
> - altNames: ['Queen of Spiders', 'Queen of the Demonweb Pits']
> - title: God of spiders
> - worshipers: Evil drow, folk who travel the Underdark
> - plane: The Abyss (Demonweb Pits)
— `5etools.md:24-28`

**B. 5etools SCAG p.23**
> ## Lolth | source SCAG p.23 | pantheon Drow
> - title: Goddess of spiders
> - alignment: ['C', 'E']
> - domains: ['Trickery']
> - symbol: Spider
— `5etools.md:61-65`

**C. 5etools MTF p.53**
> ## Lolth | source MTF p.53 | pantheon Drow
> - alignment: ['C', 'E']
> - domains: ['Trickery', 'War']
> - symbol: Spider
> - category: The Dark Seldarine
— `5etools.md:40-44`

**D. Wiki identity paragraph**
> '''Lolth''' ({{Pronounce|lalth|refs=<ref name="D93-APG-p28">{{Cite dragon/93/Ay pronunseeAYshun gyd|28}}</ref>}} {{Pronounce|lolth|refs=<ref name="D93-APG-p28" />|alt=yes}} {{Pronounce|loalth|refs=<ref name="FRCS-245">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|245}}</ref>|alt=yes}}), or '''Lloth''',<ref name="MC-71">{{Cite book/Menzoberranzan/The City|71}}</ref><ref name="DD-28">{{Cite book/Demihuman Deities|28}}</ref><ref name="eoe-p472">{{Cite book/Evermeet: Island of Elves/MMP|472}}</ref> known as the '''Queen of Spiders''' as well as the '''Queen of the Demonweb Pits''',<ref name="FRCS-245">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|245}}</ref><ref name="FRCG-p75">{{Cite book/Forgotten Realms Campaign Guide|75}}</ref><ref name="FaP-40">{{Cite book/Faiths and Pantheons|40}}</ref> was the most influential goddess of the drow, within the pantheon of the Dark Seldarine.<ref name="dhd-p12">{{Cite book/Demihuman Deities|12}}</ref>
— `wiki.txt:138`

**E. Wiki pantheon row**
> | pantheon            = Dark Seldarine<ref name="fap-p112">{{Cite book/Faiths and Pantheons|112}}</ref><br/>{{Former}} Seldarine<ref name="e:ioe-ch3"/><br/>Faerûnian pantheon<ref name="HoF-pp99,113">{{Cite book/Forgotten Realms: Heroes of Faerûn|99,113}}</ref>
— `wiki.txt:35`

**F. Wiki power and alignment rows, by edition**
> | power5e             = Lesser deity
> | alignment5e         = Chaotic evil
> | power4e             = Greater deity
> | alignment4e         = Chaotic evil
> | power3e             = Intermediate deity
> | alignment3e         = Chaotic evil
> | power2e             = Intermediate deity
> | alignment2e         = Chaotic evil<ref name="DotU-42">{{Cite book/Drow of the Underdark|42}}</ref>
> | power1e             = Lesser deity
> | alignment1e         = Chaotic evil
— `wiki.txt:55-56`, `70-71`, `85-86`, `102-103`, `116-117`

**Other 2014 entry (not in the field cap; for conflicts).**
> ## Lolth | source PHB p.296 | pantheon Nonhuman
> - title: Drow goddess of spiders
> - alignment: ['C', 'E']
> - domains: ['Trickery']
> - symbol: Spider
— `5etools.md:53-57`

### Field 2: Edict or core tenet

No edict is stated in the FRHoF, SCAG or wiki entries. The EGW "Commandments of Lolth" are not used (see Field 7).

**A. 5etools FRHoF**
> Much of the Underdark is ensnared in the figurative web of Lolth, god of spiders. Lolth considers herself the true god of drow, though other members of the drow pantheon disagree. Lolth is a cruel god who encourages her followers to backstab and betray each other, reveling in their treachery.
— `5etools.md:30`

**B. 5etools MTF**
> Holes in Lolth's Web: Lolth is far from omniscient, despite what her priestesses say. There are drow who live without bending to the tyranny of her worship. Communities of renegades who dispute Lolth's primacy often raise another of the Dark Seldarine up as their patron. Although this amounts to exchanging one evil oppressor for another, any escape from Lolth's web can feel like freedom.
— `5etools.md:48`

**C. Wiki**
> Lolth demanded absolute fealty and obedience from all drow,<ref name="FRCG-p75" /><ref name="FRPG-152" /> and questioning her motives or wisdom was considered a sin.<ref name="DD-p29"/> This applied even to male drow despite her considering them to be unclean, and she took vengeful notice if one abandoned her faith.<ref name="FRCG-p75" /> She also secretly desired the worship of other types of elves, as well as humans, and enjoyed corrupting them into her service even more than torment and devastation.<ref name="DD-28" /> In contrast, she fomented unending chaos amongst the drow, eternally setting them against each other. Ostensibly this was to weed out the weak and complacent, leaving only the strongest, cruelest, and most devious to serve her, and to some degree she believed this, but it was also simply for her own amusement and supremacy.<ref name="DD-p26-28"/><ref name="FaP-182">{{Cite book/Faiths and Pantheons|182}}</ref><ref name="DAD">{{Cite book/Deities and Demigods|81}}</ref>
— `wiki.txt:150`

**D. Wiki**
> Lolth drove her worshipers into heavy infighting under the pretense of culling the weak, while her actual goals were to hold absolute control over the dark elves, prevent the rise of alternative faiths or ideas, and avoid complacency (even though she found amusement in the strife that plagued her followers' communities).<ref name="DD-26, 29">{{Cite book/Demihuman Deities|26,29}}</ref> However, in the long run, her influence proved to be an obstacle to the growth and success of her drow followers, preventing them from unifying against common enemies or for a common cause.<ref name="MC-52-53" /><ref name="TDotU">{{Cite book/The Drow of the Underdark}}</ref>
— `wiki.txt:227`

### Field 3: Portfolio and areas of concern

**A. Wiki 5eR and 5e portfolio rows**
> | portfolio5eR        = Spiders
> | portfolio5e         = Drow, spiders
— `wiki.txt:47`, `wiki.txt:62`

**B. Wiki 3e, 2e and 1e portfolio rows**
> | portfolio3e         = Assassins, chaos, darkness, drow, evil, spiders
> | portfolio2e         = Assassins, chaos, darkness, drow, evil, spiders
> | portfolio1e         = Spiders
— `wiki.txt:92`, `wiki.txt:109`, `wiki.txt:123`

**C. Wiki Time of Troubles**
> During the Time of Troubles, apart from appearing in Menzoberranzan and assuming the aspect of Moander to attract more surface elves, humans, and half-elves, Lolth spread information on Zinzerena, a goddess from another world. When she appeared on Toril, Lolth killed her, gaining the portfolios of chaos and assassination, and learning how the distribution and absorption of divine energy worked under Ao's new rules.<ref name="DD-28" />
— `wiki.txt:315`

**D. Wiki Post-Sundering**
> Moreover, Zinzerena managed to re-emerge and escape Lolth's grasp, depriving Lolth of the portfolio of assassination. Lolth also lost the portfolio of chaos (that she had stolen from Zinzerena about a century earlier): it went to Malyk, drow god of rebellion and wild magic.<ref name="MToF53">{{Cite book/Mordenkainen's Tome of Foes|53}}</ref>
— `wiki.txt:374`

### Field 4: Worship (Waterdeep first)

Waterdeep: no temple, shrine, holy day or cult is placed in Waterdeep by any source. See Answer 1.

**A. 5etools FRHoF**
> Lolth was once known as Araushnee, spouse of the elven deity Corellon Larethian. After attempting to overthrow Corellon with an army of spirits, Araushnee was banished to the Abyss. There, she fashioned an arachnid form for herself and took her current name. Spiders of all kinds are seen as omens of Lolth, especially in the Underdark. Lolth often sends {@creature Yochlol|XMM|Yochlols}, her signature demons, as messengers or spies.
— `5etools.md:31`

**B. 5etools FRHoF**
> Lolth's worship has an iron grip on the social structure of many drow cities in the Underdark. Recently folk unassociated with the Underdark have heard the spider god's call, guided by trails of spiders to join aboveground cults dedicated to Lolth. Disciples of Lolth proudly wear web-patterned clothing and practice blood sacrifice, preferring unwilling creatures. Their doctrine teaches them to find and kill non-worshipers. Lolth's followers aren't permitted to pray to other gods apart from Kiaransalee and Selvetarm, Lolth's two allies in the drow pantheon.
— `5etools.md:32`

**C. 5etools FRHoF**
> The stone walls of Lolth's grandest temples are adorned with floor-to-ceiling bas-reliefs of webbing. As a reflection of the matriarchy of spiders, Lolth's faith permits only women to rise to the priesthood. In the Underdark, drow priests of Lolth rule the noble houses of drow cities like {@book Menzoberranzan|FRHoF|2|Menzoberranzan}, where they wield absolute power. Some of these cities' residents despise the tyranny of Lolth's organization, fleeing to the surface or to drow communities that serve more lenient gods of the drow pantheon.
— `5etools.md:33`

**D. 5etools MTF**
> In return for victims and adoration, Lolth grants signs of her favor, such as great success during a slave raid on the surface, the matron of a rival house being struck down by an inexplicable illness, or an heiress to the house being born under propitious omens.
— `5etools.md:47`

**E. Wiki clergy (first two sentences; the rest of the passage covers the priestesses' pursuit of favour, the clergy's sacrifices, and spider-motif vestments and darker ritual clothing)**
> Lolth's clerics were almost exclusively female (although there were a few males). They represented the rulers of most Lolthite communities, and strictly followed the Spider Queen's will, forcing the drow into extreme subservience to their deity, and into the constant state of conflict that dominated their lives.
— `wiki.txt:237`

**F. Wiki orders**
> The Handmaidens of the Spider Queen were an order of female crusaders. Also called the "Daughters of the Yochlol", they had no ties to specific cities, and were used when Lolth wanted an entire city brought back into line. At least three times in recorded history did the Handmaidens of the Spider Queen destroy entire drow cities to prevent them from straying too far from Lolth. One of their usual tasks was to terrorize merchants who took Vhaeraun as their patron, as well as settlements run by the followers of Vhaeraun or Ghaunadaur's (or where those faiths were prominent).<ref name="DD-30" />
— `wiki.txt:244`

Holy days: none found in any edition (see Field 7).

### Field 5: Relations with other powers, and origin

**A. Wiki leader of the Dark Seldarine**
> Lolth was the leader of the Dark Seldarine, but was opposed to varying degrees by all other members of it. She was the mother of both Eilistraee and Vhaeraun,<ref name="dhd-p12" /> along with Vandria, though the latter never supported the acts of her mother or joined the Dark Seldarine.<ref>{{Cite book/Races of the Wild|24}}</ref>
— `wiki.txt:181`

**B. Wiki Vhaeraun**
> The two had no common ground: Lolth promoted favoritism towards females,<ref name="FaP-41" /> while Vhaeraun promoted gender equality;<ref name="FaP-114" /> the Spider Queen wanted surface elves to be sacrificed by her worshipers,<ref name="DD-p29">{{Cite book/Demihuman Deities|29}}</ref> while the Masked Lord urged his followers to cooperate with surface elves;<ref name="DD-36">{{Cite book/Demihuman Deities|36}}</ref> Lolth ordered her followers to keep drow society stagnant in every regard, while<ref name="MC-52-53">{{Cite book/Menzoberranzan/The City|52-53}}</ref> Vhaeraun attracted those who wanted change in their societal progress, economic growth, and territorial expansion;<ref name="MC-72" /> and Lolth wanted to extinguish the drow race's desire to return to the surface,<ref name="MC-53">{{Cite book/Menzoberranzan/The City|53}}</ref><ref name="LEoF-54">{{Cite book/Lost Empires of Faerûn|54}}</ref> while Vhaeraun encouraged settling the surface.<ref name="FaP-114" /><ref name="DD-38">{{Cite book/Demihuman Deities|38}}</ref>
— `wiki.txt:194`

**C. Wiki Ghaunadaur**
> Ghaunadaur was a different matter. She feared the possibility that he could sway the drow towards his cause,<ref name="MC-71" /> but he did not care enough for drow matters to attract many of them.<ref name="RoF-37" />
— `wiki.txt:204`

**D. Wiki Dawn Age**
> Before her fall, Lolth was known as Araushnee, the lesser elven goddess of destiny and artisans. She was consort to Corellon, leader of all the elf deities,<ref name="DD-26" /> and ruled with him and Sehanine as the indisputable heads of their pantheon.<ref name="TPA 37-40">{{Cite book/The Plane Above|37-40}}</ref> Unflinching as the fallen night, she too had played a part in the creation of the earliest elves; her cutting jests brought forth tears of laughter from Corellon from which mortal fey were spawned, as did Sehanine's arcing acrobatics. Sometimes the laughter between the three was dark and mocking, but more often, it was true and heartfelt.<ref name="TPA 37-40"/>
— `wiki.txt:254`

**E. Wiki aftermath of exile**
> After her exile, Araushnee took the name "Lolth". She conquered the 66th layer of the Abyss, the Demonweb Pits, for herself.<ref name="DD-26" /> Lolth was initially opposed by Kiaransalee, an elven goddess whom she swiftly subjugated, and Ghaunadaur, with whom she had a longer conflict. That Which Lurks tried to subsume her, but failed, and in his rage robbed his followers of their intellect. It also downsized his follower base and his power with it, thus allowing Lolth to emerge victorious.<ref name="E.IoE-137-138">{{Cite book/Evermeet: Island of Elves/MMP|137-138}}</ref>
— `wiki.txt:285`

**F. Wiki post-Second Sundering (first sentence; the line continues with a Candlekeep citation on lines 359-365, not quoted)**
> After the event known as the Second Sundering, Lolth was no longer unrivaled as the goddess of the drow (even if she still retained her position of dominance), for the dead members of the Dark Seldarine were revived.<ref name="SCAG-23, 108">{{Cite book/Sword Coast Adventurer's Guide|23, 108}}</ref>
— `wiki.txt:358`

### Field 6: Campaign and published-adventure mentions

Six quotes here. The full campaign list follows them.

**1. Campaign rule**
> - This is where the campaign rule starts. Jarlaxle rejected Lolth, Bregan D'aerthe rejects her, and its members speak of her as the goddess they walked away from. Soluun gives Jarlaxle the devotion that a drow of the houses would give the Spider Queen.
— `campaign/setting/history/03-bregan-daerthes-long-road.md:36`

**2. Campaign, Soluun**
> **Persona.** To the world, Soluun is a drow gunslinger of Bregan D'Aerthe, disowned for unsanctioned Dock Ward murders. To those he trusts, he is fiercely loyal to Jarlaxle and Bregan D'Aerthe, and he considers his brother Nar'l a weakling who turned to arcane magic by way of compensation. Deep down, he was taught from a young age to kill surface elves as opportunity permits, and the habit has become his identity. He despises Lolth and the matron houses that serve her, as the whole band does, and the devotion a drow of the houses would give the Spider Queen he gives to Jarlaxle instead.
— `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:22`

**3. Campaign, Bregan D'aerthe first meeting (question)**
> [!qna]**Do you serve Lolth?**
— `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:375`

**3. (answer)**
> > "Gods, no. My colleagues left the Spider Queen behind on purpose, and most of them left in a hurry and in a bad temper. You won't find anyone among us with a kind word for her, and I'd advise you not to ask them about her at dinner."
— `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:379`

**4. Published adventure, Jarlaxle's mission table (the 5th-level row; its last cell gives "Each Bregan D'aerthe character gains 2 renown.")**
> "\"We have a spy deep within {@creature Xanathar|WDH}'s organization, but I fear he has been compromised. It breaks my heart to do this, but I'm sending you to eliminate him. Make it quick and painless, and for Lolth's sake, be discreet.\"",
— `sources/adventure-wdh.json:3633`

**5. Published adventure, Soluun's stateroom**
> "If he has not been encountered and disposed of elsewhere, a {@creature drow gunslinger|WDH} named {@creature Soluun Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) is here, worshiping before a shrine of Lolth. His stateroom has the following features:",
— `sources/adventure-wdh.json:26345` (area U3, under "U3. Soluun's Stateroom" at `:26341`)

Context (first sentence only): "Characters descending from Zardoz Zord's cabin on the {@i Eyecatcher} ({@area J30|399}) arrive in this chamber." (rest of the passage covers the hatch and the pressurisation of the {@i Scarlet Marpenoth}).
— `sources/adventure-wdh.json:26309` (area U1, "U1. Entrance Hatch" at `:26305`). The U-series rooms belong to the submarine.

**6. Published adventure, Undermountain (Level 3, "Level 3: Sargauth Level" at `:7389`, area 5c)**
> Geldax Breer (NG male half-elf {@creature commoner}) occupies the easternmost cell. He is a Waterdavian lamplighter abducted several nights ago by the drow (and doomed to become a sacrifice to Lolth unless he escapes).
— `sources/adventure-wdmm.json:9802`

**Every campaign line naming Lolth, the Spider Queen, or the rejection** (Grep of `campaign/` for `Lolth|Spider Queen|Araushnee|Yochlol|Dark Seldarine|Demonweb|rejected|rejects`)

> If a character has Soluun in hand and asks him about the goddess of his people, he answers with open contempt for Lolth, since Bregan D'aerthe rejects her.
— `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md:343`

> ***The disownment.*** The restored draft treated Soluun's disownment as real. His Notable Figures page says it is a cover story and that Jarlaxle knows about the murders and hasn't decided what to do. This version keeps that in GM text only, and Soluun never mentions being disowned. He also never speaks of Lolth with devotion, because Bregan D'aerthe rejects her: when asked about his goddess he answers with contempt.
— `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/design-notes.md:13`

> Bregan D'aerthe rejects Lolth. The spider on the coin is the goddess the company walked away from, caught in her own web with a blade through her, and every speaker mentions her with contempt. The company knows the truth about the Cassalanters, because Jarlaxle's doppelganger agent Vessa reads their thoughts. No speaker tells a member who hasn't worked it out.
— `campaign/quests/faction-events/bregan-daerthe/r50-houseless-noble/ev-01-houseless-noble.md:27`

> The coin's spider is the rejected goddess in both versions. Zardoz mocks "the old eight-legged lady with a knife in her", and Jarlaxle calls the coin a joke at her expense.
— `campaign/quests/faction-events/bregan-daerthe/r50-houseless-noble/design-notes.md:9` (names no goddess; the spider on the coin is "the rejected goddess")

> Fel'rekt speaks in encouraging sentences and counts his options off on his fingers. He checks on Krebbyg mid-sentence, swears in short bursts when excited, and offers a way out aloud whenever something looks likely to go wrong. He is warm toward the members and firm about discretion, because he knows what happens to drow the Watch catches. He never threatens anyone and never mentions Lolth.
— `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:136`

> Soluun is stunned, then furious, then obedient, in that order, and none of the three lasts long. He speaks to the speaker in a flat low voice that rises into fervor whenever he says "the captain", and he speaks to the members in orders and insults. He spits when a surface elf is named, and he calls an elf or half-elf member surface-blood to their face. He never apologizes, never says Lolth's name with anything but disgust, and mentions his brother only as "the weak one". He doesn't believe the captain means it until Fel'rekt lifts the disc from his neck.
— `campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:242`

> - Appendix C has Jarlaxle say "for Lolth's sake." The line is cut, because Bregan D'aerthe has rejected her.
— `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/design-notes.md:13`

> - **Bregan D'aerthe's Long Road** (10th century DR to 1492 DR): Jarlaxle's path from Menzoberranzan to Luskan, the company's rejection of Lolth, and the Sea Maidens Faire that brings him to Deepwater Harbor.
— `campaign/setting/history/00-the-history.md:30`

> **Purpose:** Lets the GM answer any question about who founded Bregan D'aerthe, why its members reject Lolth, how it came to dominate Luskan, and what Jarlaxle had in place before the campaign opens.
— `campaign/setting/history/03-bregan-daerthes-long-road.md:13`

> **Keywords:** Bregan D'aerthe, Jarlaxle Baenre, Zardoz Zord, Yvonnel Baenre, Menzoberranzan, Lolth, Luskan, High Captains, Lords' Alliance, Sea Maidens Faire, Lantan, Scarlet Marpenoth
— `campaign/setting/history/03-bregan-daerthes-long-road.md:15`

> - Jarlaxle was born to Matron Mother Yvonnel Baenre of House Baenre, the first house of Menzoberranzan. He survived his sacrifice to Lolth and later rejected her. Bregan D'aerthe rejects her too, and its members speak of her with contempt.
— `campaign/setting/history/03-bregan-daerthes-long-road.md:24`

> - By his birth order he was to be sacrificed to Lolth. The blade could not pierce the infant, and his brother Doquaio Baenre died in his place. `[research: wiki only]`
— `campaign/setting/history/03-bregan-daerthes-long-road.md:34`

> - Lolth favored him afterward as an agent of chaos, and he rejected her. She withdrew her favor, and the matron mothers of Menzoberranzan never learned of it. `[research: wiki only]`
— `campaign/setting/history/03-bregan-daerthes-long-road.md:35`

> - This is where the campaign rule starts. Jarlaxle rejected Lolth, Bregan D'aerthe rejects her, and its members speak of her as the goddess they walked away from. Soluun gives Jarlaxle the devotion that a drow of the houses would give the Spider Queen.
— `campaign/setting/history/03-bregan-daerthes-long-road.md:36` (same line as Field 6, item 1)

> - `campaign/setting/notable-figures/bregan-daerthe/` (Jarlaxle Baenre, Soluun Xibrindas) and `xanathars-guild/03-narl-xibrindas.md`: names, the rejection of Lolth (Soluun, line 22), Nar'l's loyalties.
— `campaign/setting/history/03-bregan-daerthes-long-road.md:99`

> **Emotions.** Soluun most often feels cold hatred of surface elves, fanatical devotion to Bregan D'Aerthe, contemptuous superiority, a zealot's fervor for the band (which, like every member of Bregan D'Aerthe, rejects Lolth), hunting focus, and bitter disdain for his brother Nar'l.
— `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:14`

The same line as Field 6, item 2: `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:22`. The same lines as Field 6, item 3: `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:375` and `:379`.

"Rejected" matches that are not about Lolth (not quoted): `campaign/guides/gm-guide/design-notes-running-the-campaign.md:29`, `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/design-notes.md:15`, `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:12`, `campaign/structure/ch3-running-the-campaign.md:278`, and the "rejected-cargo" lines in `campaign/quests/faction-events/harpers/m02-the-dead-drop/` and `m05-the-sleeping-asset/`.

Xanathar's Guild, Manshoon's Zhentarim, Cassalanter, Doom Raider and Sea Maidens files: no Lolth, Spider Queen, Araushnee, Yochlol or Dark Seldarine line, other than the Doom Raiders m01 files above.

**Published adventure lines (all Lolth lines)**

Quoted: `:3633`, `:26345`, `:9802` (above); `sources/adventure-wdmm.json:9919`, `:29633`, `:30401`.

> The script around the circle is written in Abyssal. Anyone who understands the language and succeeds on a {@dc 15} Intelligence ({@skill Religion}) check can ascertain the circle's purpose, which is to send drow to the Abyss as part of a ritual known as the Test of Lolth. Any drow who fails this test returns from the Abyss horrifically transformed into a drider and is instructed to flee by way of the southern tunnel and never return, lest they be killed. Drow who pass the test return to this chamber as they were, with Lolth's blessing and nothing more.
— `sources/adventure-wdmm.json:9919` (Level 3, Sargauth Level)

> This temple of the Spider Queen has vaulted, 30-foot-high ceilings draped in cobwebs. {@creature Muiral|WDMM} visits the temple to hear the lamentations of three drow priestesses who lost all favor with Lolth and became banshees.
— `sources/adventure-wdmm.json:29633` (Level 10, Muiral's Gauntlet; heading "3. Haunted Temple of Lolth" at `:29629`)

> These temples are dedicated to the Dark Seldarine, a pantheon of drow gods under Lolth. Each room has walls that rise 15 feet, then angle inward to a central point 30 feet above the middle of the floor.
— `sources/adventure-wdmm.json:30401` (Level 10; heading "17. The Dark Seldarine" at `:30397`)

Listed by file:line only (the rest of the set): `sources/adventure-wdh.json:25498` (Jarlaxle's cabin, area J29, "By Lolth's teeth") and `:26350` (the shrine's description in U3). `sources/adventure-wdmm.json`: 6208, 7417, 9841, 9985, 11354, 12593, 12604, 12643, 12656, 15327, 26479, 26483, 27770, 27853, 29629, 29634, 29646, 29647, 29648, 29651, 29662, 29667, 29668, 29688, 29885, 30053, 30086, 30094, 30099, 30280, 30397, 30747, 30762, 30791, 30835, 30855, 30863, 30866, 30895, 30927, 30958, 33038, 33076, 33296, 33297, 35303, 35981, 36005, 36007, 36012, 36027, 36031, 36042, 36061, 36062.

### Field 7: Conflicts and what was not found

**Conflict 1: the published adventure against the campaign rule.** The published adventure has Soluun "worshiping before a shrine of Lolth" (`sources/adventure-wdh.json:26345`) and Jarlaxle's mission says "for Lolth's sake" (`:3633`). The campaign says the opposite, and the campaign file ranks higher.

> - Appendix C has Jarlaxle say "for Lolth's sake." The line is cut, because Bregan D'aerthe has rejected her.
— `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/design-notes.md:13`

> This is where the campaign rule starts. Jarlaxle rejected Lolth, Bregan D'aerthe rejects her, and its members speak of her as the goddess they walked away from. Soluun gives Jarlaxle the devotion that a drow of the houses would give the Spider Queen.
— `campaign/setting/history/03-bregan-daerthes-long-road.md:36`

**Conflict 2: domains.** 5etools SCAG gives Trickery only. 5etools MTF gives Trickery and War. Both are 2014.

> - domains: ['Trickery']
— `5etools.md:64` (SCAG)

> - domains: ['Trickery', 'War']
— `5etools.md:42` (MTF)

> | domains5e           = Trickery, War<ref name="MTF5e-p53,57" />
— `wiki.txt:63` (5e; the wiki's link brackets are dropped)

> | domains4e           = Darkness, Poison, Strife
— `wiki.txt:78` (4e). No FRHoF domains line exists.

**Conflict 3: excluded entries.** The DMG and EGW entries are not used, following the Asmodeus precedent. They conflict with the rest.

> ## Lolth | source DMG p.10 | pantheon Dawn War
> - title: Goddess of spiders and lies
> - alignment: ['C', 'E']
> - domains: ['Trickery']
— `5etools.md:1-4` (DMG)

> ## Lolth | source EGW p.27 | pantheon Exandria
> - title: the Spider Queen
> - alignment: ['C', 'E']
> - domains: ['Knowledge', 'Trickery']
> - symbol: Jeweled spider
> - category: Betrayer Gods
— `5etools.md:9-14` (EGW)

**Not found**
- Holy days: none in any 5etools entry. The wiki holy-day rows are blank (`wiki.txt:51`, `66`, `82`, `98`).
- Any temple, shrine or cult in Waterdeep (campaign, wiki or both adventures). Terms tried: Lolth, Spider Queen, Araushnee, Yochlol, Dark Seldarine, Demonweb, Waterdeep, Waterdhav, and the ward names.
- Any Lolth line in the Xanathar's Guild, Zhentarim, Cassalanter, Sea Maidens Faire, Kolat Towers, Gralhund Villa or Trollskull Alley files, or in `campaign/gazetteer/`. Grep covered all of `campaign/`.
- A 2024 warlock or cleric entry. The sources give no Fiend or Great Old One patron tie for Lolth.

**Answer 1: temples or shrines in Waterdeep and ward.** None in the campaign files, the wiki, or the "Major Temples of Waterdeep" table (`sources/adventure-wdh.json:30910-30997`; the table has no Lolth row). The published adventure places two Lolth shrines aboard the submarine Scarlet Marpenoth (U3, `:26345` and `:26350`). The Undermountain Lolth temples are on Level 10 (see the list above) and are not in a Waterdeep ward.

**Answer 2: campaign NPC, faction or quest that uses Lolth.** Bregan D'aerthe is the only faction. NPCs: Jarlaxle (`campaign/setting/history/03-bregan-daerthes-long-road.md:36`) and Soluun Xibrindas (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:14, 22`). Quests: the Bregan D'aerthe first meeting (`campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:379`), r50 (`ev-01-houseless-noble.md:27`, `design-notes.md:9`), s02 (`ev-01-kreb-drops-the-cover.md:136`), s05 (`ev-01-the-killers-fate.md:242`), m04 (`design-notes.md:13`), and Doom Raiders m01 (`ev-01-the-dockside-killer.md:343`). No campaign NPC worships her.

**Answer 3: wiki lines that mention Waterdeep.** None. The Lolth page has no Waterdeep line. Its Undermountain lines are the Flame Sword paragraph and a gallery caption.

> In 1369 DR, Lolth guided one of her High Priestesses, Azurna in search of the ''Flame Sword of Lolth'' to establishing a presence in Undermountain. The ''Flame Sword'' was a powerful artifact created by the Queen of Spiders during the War of the Seldarine. The sword held immense power and was able to cut through the Planes. Upon her defeat, the elven gods took the sword, and eventually, it was hidden within Undermountain by Halaster Blackcloak. In 1370 DR, Azurna successfully assembled the ''spider statue'' that blocked the vault of the sword, allowing Lolth to manifest her giant drider avatar and tried to reclaim the item. She was confronted by an adventurer agent of Khelben Arunsun, and the avatar was defeated. In the subsequent release of divine energy, ''Flame Sword of Lolth'' disappeared, slipping from the goddess' grasp once again.<ref name="Dec">{{Cite game/Descent to Undermountain}}</ref>
— `wiki.txt:319` (link brackets dropped)

> Descent Lolth avatar.jpg|thumb|''The avatar of Lolth that appeared in Undermountain in 1370 DR.''
— `wiki.txt:385` (gallery caption; link brackets dropped)

---

## 2. EILISTRAEE

### Field 1: Identity

**A. 5etools FRHoF**
> ## Eilistraee | source FRHoF p.106 | pantheon Faerûnian
> - altNames: ['The Dark Maiden', 'Lady of the Dance', 'Lady Silverhair']
> - title: God of song and moonlight
> - worshipers: Bladesingers, elves, performing artists
> - plane: Arborea (Arvandor)
— `5etools.md:1-5`

**B. 5etools SCAG**
> ## Eilistraee | source SCAG p.23 | pantheon Drow
> - title: Goddess of song and moonlight
> - alignment: ['C', 'G']
> - domains: ['Light', 'Nature']
> - symbol: Sword-wielding dancing drow female silhouetted against the full moon
— `5etools.md:24-28`

**C. 5etools MTF**
> ## Eilistraee | source MTF p.56 | pantheon Drow
> - alignment: ['C', 'G']
> - domains: ['Life', 'Light', 'Nature']
> - symbol: Sword-wielding, dancing female drow silhouetted against the full moon
> - category: The Dark Seldarine
— `5etools.md:13-17`

**D. Wiki identity paragraph (quoted to the point where a Candlekeep citation opens; the citation runs on lines 136-142, and the paragraph's pronunciation sentence sits on line 135 after it)**
> '''Eilistraee''' ({{Pronounce|EYEL|iss|TRY|ee|primary stress=1|audio=Eilistraee.ogg}}<ref name="EdGreenwood-p476639"/>) was the chaotic good drow goddess of beauty, song, dance, freedom, moonlight, swordwork, and hunting, within the drow pantheon known as the Dark Seldarine. She was the patroness and protector of the few dark elves who longed to return to the surface and live there, at peace with other races, and to abandon the endless conflicts and intrigues that dominated the lives of most drow.<ref name="FRCS3e-237" /><ref name="F&P-p23" /><ref name="DotU-20" /><ref name="DD" /><ref name="MTF5e-p53-57"/><ref name="SCAG"/> She was often referred to as the '''The Dark Maiden''', the '''Lady of the Dance''', or '''Lady Silverhair''',<ref name="FRCS3e-237" /><ref name="F&P-p23" /><ref name="DotU-20" /><ref name="DD" /> and sometimes '''The Dark Dancer''', among other titles<ref name="SSotSS"/> Briefly, she was known as '''The Masked Lady''', when her faith subsumed that of the Masked Lord Vhaeraun, her divine brother,<ref name="SofD"/><ref name="tGHotR-p158"/> while the Seven Sisters nicknamed her '''Darkfire of Love'''.<ref name="tev-love">{{Cite web/theedverse/2023-01-13 - Drow Words for Love}}</ref> Eilistraee pronounced her own name {{Pronounce|alt=none|EYEL|iss|TRY|ee|primary stress=1}},<ref name="EdGreenwood-p476639"/> but her name has been mispronounced variously as {{Pronounce|alt=none|eel|ISS|tray|ee|primary stress=2}},<ref name="DotU-20"/> {{Pronounce|alt=none|EEL|iss|TRAY|yee|primary stress=1}},<ref name="DD"/> {{Pronounce|alt=none|eel|iss|TRAY|ee|primary stress=3}},<ref name="FRCS3e-237"/> {{Pronounce|alt=none|eyel|iss|TRAY|yee|primary stress=3}},<ref name="F&P-p23"/> while Elminster Aumar, Qilué Veladorn, and the rest of the Seven Sisters pronounced it {{Pronounce|alt=none|eyel|ISS|tree|primary stress=2}}, even when addressing the goddess face to face.<ref name="EdGreenwood-p476688">{{Cite web/Candlekeep forum
— `wiki.txt:135`

Title list: `wiki.txt:9-13` ("The Dark Maiden", "The Dark Dancer", "The Dancing Goddess", "Lady of the Dance", "Lady Silverhair"; not quoted).

**E. Wiki pantheon row**
> | pantheon            = Dark Seldarine <small>formerly:</small> the Seldarine<br/>Faerûnian pantheon<ref name="HoF-pp99,106"/>
— `wiki.txt:18`

**F. Wiki power and alignment rows, by edition**
> | power2e             = Lesser deity
> | alignment2e         = Chaotic good
> | power3e             = Lesser deity
> | alignment3e         = Chaotic good
> | power4e             = Dead power
> | power5e             = Lesser deity
> | alignment5e         = Chaotic good
> | power5eR            = Deity
— `wiki.txt:51-52`, `65-66`, `81`, `96-97`, `111`

### Field 2: Edict or core tenet

**A. 5etools MTF**
> Eilistraee is a god of moonlight, song, dance, and, most important, the rejection of the evil ways of Lolth. Drow who feel like outsiders in their society, who react with disgust to the evils perpetrated by their kind, who come to the surface and fall in love with the stars-these are the ones who might be pleased to hear Eilistraee's call. If they respond to it by going to the surface and staying there, Eilistraee offers no guarantee of their safety and no promise of acceptance in the world above. But she opens her followers' hearts to the wonder of the nature in the night, and her songs and signs can show a drow how to persevere in that alien environment.
— `5etools.md:21`

**B. 5etools FRHoF**
> Eilistraee was born to the gods Lolth and Corellon Larethian. Melancholy yet defiant, she resents the iron grip her mother has over drow cities such as {@book Menzoberranzan|FRHoF|2|Menzoberranzan}. In response, Eilistraee encourages her followers to pursue their own destinies, which might mean fleeing the Underdark and living on the surface. She communicates with her worshipers through dance-like dreams awash in gentle moonlight. In recent years, Eilistraee's message of freedom and harmony has begun to echo beyond drow society. Folk in regions plagued by conflict or oppression might enter Eilistraee's worship after being inspired by a story of a hopeful future that Eilistraee can provide.
— `5etools.md:8`

**C. Wiki**
> Though focused on the drow, Eilistraee accepted folk of all races who danced along her path, who delighted in life and in the free-form expression of it in all its forms. She fought so that all races could live peacefully together, helping and accepting each other despite their differences,<ref name="DD" /><ref name="AL-40" /> and strongly believed in the possibility of redemption for those who had fallen to evil, especially the drow.<ref name="AL-40">{{Cite book/Ascendancy of the Last|40|3}}</ref><ref name="AL-50">{{Cite book/Ascendancy of the Last|50|3}}</ref>
— `wiki.txt:186`

**D. Wiki**
> Despite her focus on the drow, Eilistraee took to heart the cause of aiding the needy wherever and whenever possible, no matter their race, gender, or strength. She believed in offering kindness, shelter, and acceptance to anyone not working evil, especially if outcasts.<ref name="DD" /> She and her church also worked to spread joy and merriment, and to bring confort and hope to those who were taken by sorrow.<ref name="DD" /> Finally, the Dark Maiden was, among the other things, a goddess of beauty; as such, she was known for her efforts to nurture and spread enthusiasm for arts—especially music and dance—and for blessing artists and bards with bursts of creativity and inspiration.<ref name="DD" />
— `wiki.txt:279`

### Field 3: Portfolio and areas of concern

**A. 5etools FRHoF**
> In realms such as the Underdark where worship of Lolth is prevalent, drow and other folk who oppose the Spider Queen turn to Eilistraee as a beacon of hope and freedom. She is the drow god of dance, song, beauty, moonlight, swordplay, and hunting.
— `5etools.md:7`

**B. Wiki 5e and 5eR portfolio rows**
> | portfolio5e         = Beauty, dance, freedom, hunting, moonlight, song, swordwork
> | portfolio5eR        = Beauty, dance, hunting, moonlight, song, swordplay
— `wiki.txt:103`, `wiki.txt:118`

**C. Wiki**
> She also gained the portfolio of freedom, in addition to her traditional portfolios of beauty, dance, song, moonlight, swordwork, and hunting.<ref name="MTF5e-p53-57" /><ref name="SCAG" />
— `wiki.txt:463`

**D. Wiki 2e and 3e portfolio rows**
> | portfolio2e         = Beauty, dance, hunting, moonlight, song, swordwork
> | portfolio3e         = Beauty, dance, hunting, moonlight, song, swordwork
— `wiki.txt:58`, `wiki.txt:72`

### Field 4: Worship (Waterdeep first)

Waterdeep: the wiki says Eilistraee was worshiped "in Waterdeep" and that her faithful planned a shrine there (quoted in Answer 1). No temple is placed in Waterdeep by a source. The Major Temples table has no Eilistraee row.

**A. 5etools FRHoF**
> Followers of Eilistraee show their gratitude to the god by dancing beneath every full moon. Her priests are passionate advocates of the arts, especially song and dance. Temples to Eilistraee are some of the few places willing to teach the elven technique of bladesinging, and travelers visit from afar to learn this ancient skill. Her priests practice a variant known as sword dancing, which blends bladesinging with bardic arts from the College of Dance. Eilistraee's temples in the Underdark are refuges from the region's subterranean perils, concealed with powerful magic and requiring a sword-shaped key to enter.
— `5etools.md:9`

**B. 5etools FRHoF**
> Eilistraee inspires two main adventuring orders: the Silverhair Knights and the Darksong Knights. The Silverhair Knights demonstrates the strength that lies in mercy and compassion. The order engages in combat only when absolutely necessary, even then strictly adhering to nonlethal techniques. The Darksong Knights is a smaller order, dedicated to hunting and destroying yochlols and Lolth's other demonic agents.
— `5etools.md:10`

**C. Wiki servitors and messengers (brackets dropped from the link markup)**
> Eilistraee was served by the following creatures, whom she also sent as her agents: aasimar, aasimon (particularly lights), asuras, cath shee, einheriar, eladrins, mercury dragons, elven cats, feystags, frosts, hollyphants, incarnates of faith and hope, lythari, mist dragons, moon dogs, moon horses, pixies, radiance quasielementals, revered ones, silver dogs, silver dragons, sprites, sunflies, tieflings, and silver-striped tabby cats or normal-looking animals with solid silver-colored eyes. Silver moths could also be used as a message from the goddess.<ref name="DD" />
— `wiki.txt:340`

**D. Wiki clergy (quoted from the sentence beginning "In fact"; the earlier sentences cover the matriarchal nature of Eilistraean communities and the loose hierarchy)**
> In fact, the clerics of Eilistraee, commonly known as Sword Dancers, acted as an extension of Eilistraee's own motherhood of the drow, and took the role of teachers, protectresses, and diplomats.<ref name="EdGreenwood-p129882" /><ref name="FP" /> The priestesses aided their people to learn to live and forge their own path in a hostile world, and to rediscover a sense of belonging and community.<ref name="EdGreenwood-p129882" /> They also protected their people from danger, and built a place for them to live by establishing friendships and relationships with other races.<ref name="FP" /> The Eilistraeans were also known to offer aid and shelter to those who came asking them (no matter the race), and even to actively travel to other places in order to bring food, cures, arts, and practical help where there was need of it and to those met along the way.<ref name="DD" />
— `wiki.txt:364`

**E. Wiki observance**
> The Dark Dancer was worshiped through song and dance, if at all possible in the surface world under the moon (preferably in wooded places). Worship of her was usually accompanied by a feast.<ref name="DotU-20" /><ref name="DD" />
— `wiki.txt:372`

Holy days: none. The FRHoF practice of dancing beneath every full moon (`5etools.md:9`) is an observance, not a holy day.

**F. Wiki manifestations (first sentence; the rest of the paragraph covers her blessings on swords and living creatures)**
> Her most common sign was a silvery radiance (sometimes accompanied by a snatch of song or a few echoing notes of a harp) that could also take the form of a handful of dancing moonbeams or moon-motes.
— `wiki.txt:191`

### Field 5: Relations with other powers, and origin

**A. Wiki birth (first sentence)**
> She was the daughter of Araushnee (later Lolth) and Corellon Larethian, a free-spirited and kind-hearted goddess, with a fiery streak in her personality.<ref name="F&P-p23" /><ref name="DotU-20" /><ref name="DD" /><ref name="E.IoE" />
— `wiki.txt:144`

**B. Wiki Lolth as enemy**
> Lolth was Eilistraee's chief enemy. The Dark Maiden was infuriated by her mother's evil and corruption, and constantly strove to help the drow break free from her oppression and find their way back to the surface world.<ref name="DD" />
— `wiki.txt:315`

**C. Wiki Vhaeraun**
> The relationship between Eilistraee and Vhaeraun went through significant changes over the ages. After her self-imposed exile, the Dark Maiden fought Vhaeraun's warmongering influence on the dark elves of Ilythiir. After the Descent of the drow, while the two siblings shared certain goals, their views on how to achieve them clashed. Eilistraee wished the drow to peacefully return to the surface and build friendships with other races, while Vhaeraun wanted the drow to claim back the ancient prestige of Ilythiir through violence and conquest.<ref name="DD" /><ref name="DD 36-38">{{Cite book/Demihuman Deities|36-38}}</ref>
— `wiki.txt:320`

**D. Wiki Ghaunadaur (the Waterdeep sentence is the second)**
> The Dark Maiden hated the influence that Ghaunadaur had on the drow, and fought it on many occasions.<ref name="DD" /> The Elder Eye held a grudge against Eilistraee due to her efforts in defeating and trapping his avatar near the Promenade of the Dark Maiden, in order to protect the city of Waterdeep from it.<ref name="7S-58">{{Cite book/The Seven Sisters|58}}</ref>
— `wiki.txt:328`

**E. Wiki return (first paragraph; the Candlekeep citation continues on lines 457-463, not quoted)**
> Eilistraee managed to return to life during the event known as the Second Sundering<ref name="SCAG" /><ref name="MTF5e-p53-57" /><ref name="EdGreenwood-p468322" />, in Flamerule, 1489 DR<ref name="EdGreenwood-p476639" />. The goddess took the title of Dark Maiden once again, as her brother too had returned and taken back his portfolio.
— `wiki.txt:456`

**F. Wiki move to Arvandor**
> At the beginning of the 1370s DR, the cosmology rearranged under the World Tree model. After her millennia-long exile, Eilistraee was allowed to move her divine realm, and the souls of all her followers (including drow), back to Arvandor. She kept a small realm in the Demonweb Pits, but it remained mostly empty, and Eilistraee herself very rarely visited it.<ref name="F&P-p23">{{Cite book/Faiths and Pantheons|23-25}}</ref><ref name="PGtF">{{Cite book/Player's Guide to Faerun|143}}</ref> It wasn't known whether moving from Ysgard to Arvandor happened out of material necessity, or was the first sign of her efforts towards reconciliation bearing results.{{speculation}}
— `wiki.txt:424`

### Field 6: Campaign and published-adventure mentions

**Campaign: no matches.** Grep of `campaign/` for `Eilistraee|Dark Maiden|Silverhair|Lady of the Dance|Darksong|Promenade|Dancing Haven|Sword Dancer|Qilu|Qilué|Dark Dancer` returned no matches. `campaign-hits.txt` is empty.

**Published adventure, Undermountain (all six Eilistraee lines; none in WDH; none is Waterdeep-set)**

> The statue depicts Eilistraee, drow god of beauty, song, and the hunt. Abhorred in drow society, the Dark Maiden was not without followers in Undermountain. The statue can't be transformed, damaged, or knocked off its base.
— `sources/adventure-wdmm.json:30017` (Level 10, Muiral's Gauntlet; statue)

> A character who succeeds on a {@dc 15} Intelligence ({@skill Religion}) check recalls that Eilistraee favors the use of a sword. If such a weapon is placed in its hands, the statue's grip tightens around the hilt. (The statue does not accept illusory or spiritual weapons.) The statue then dances atop its base for 1 minute before leveling the sword at the locked set of doors to the south, causing them to open. As the doors swing open, the statue returns to its original pose and loosens its grip on the sword, causing the weapon to fall from its grasp.
— `sources/adventure-wdmm.json:30018`

> The doors south of the statue refuse to budge, and no amount of force can pry them open. They are also immune to damage from any source. A {@spell knock} spell or similar magic opens the double door. The doors also swing open if the statue of Eilistraee points a sword at them.
— `sources/adventure-wdmm.json:30025`

> "name": "17e. Temple of Eilistraee",
— `sources/adventure-wdmm.json:30509` (heading)

> This temple of Eilistraee, god of beauty, dance, and the hunt, features the following:
— `sources/adventure-wdmm.json:30513`

> The fountain is fed by a natural spring and provides the drow with a virtually endless supply of fresh water. The statues stand atop stone plinths above the water, facing outward. Starting with the northernmost one and moving clockwise, the statues represent Eilistraee (god of beauty, dance, and the hunt), Malyk (god of wild magic), Kiaransalee (god of undeath), Ghaunadaur (god of oozes, slimes, and all things subterranean), Zinzerena (god of assassins), Vhaeraun (god of thieves), Lolth (the Demon Queen of Spiders and mother of the Dark Seldarine) in her drow form, and Selvetarm (god of war and warriors).
— `sources/adventure-wdmm.json:30762` (fountain, Level 10)

`sources/adventure-wdh.json` has no Eilistraee line (the alias Grep returned none).

### Field 7: Conflicts and what was not found

**Conflict 1: domains (both 2014).** The SCAG and MTF entries disagree. No ranking applies between two 2014 entries. The wiki's 5e row matches MTF.

> - domains: ['Light', 'Nature']
— `5etools.md:27` (SCAG)

> - domains: ['Life', 'Light', 'Nature']
— `5etools.md:15` (MTF)

> | domains5e           = Light, Nature, Life
— `wiki.txt:104` (link brackets dropped)

**Conflict 2: planes.** FRHoF gives the plane as Arborea (Arvandor). The wiki's 2e row and its post-Sundering text put her in Ysgard. The wiki's 1370s text puts her in Arvandor.

> - plane: Arborea (Arvandor)
— `5etools.md:5`

> | homeplane2e         = Ysgard, Nidavellir
— `wiki.txt:54` (link brackets dropped)

> After the Second Sundering, which saw Eilistraee's return (''circa'' the 1480s DR),<ref name="EdGreenwood-p468322" /> the planes were rearranged under the Great Wheel cosmology once again,<ref>{{Cite book/Player's Handbook 5th edition}}</ref> and the Dark Dancer made herself a humble home in the underground of Ysgard, which went under the name of ''"The Court of the Dance"''.<ref name="EG-YT"/>
— `wiki.txt:240` (link brackets dropped in the wiki's first clause; no other change)

**Conflict 3 (within the wiki): Vhaeraun's fate.** The note's first sentence (link brackets dropped). The note goes on to cite Ed Greenwood, who suggests she spared him.

> ''The Grand History of the Realms'' explicitly says that Vhaeraun's assassination attempt failed and Eilistraee killed him.
— `wiki.txt:437` (note)

**Not found**
- Holy days (wiki holy-day rows `wiki.txt:62`, `78`, `93`, `108`, `122` are blank for Eilistraee).
- A Waterdeep temple. The only Waterdeep items are `wiki.txt:370` (worshiped in Waterdeep) and `wiki.txt:473` (a planned shrine). No published temple, no campaign line, no table row.
- Any campaign file. Terms tried: Eilistraee, Dark Maiden, Silverhair, Lady of the Dance, Darksong, Promenade, Dancing Haven, Sword Dancer, Qilué, Dark Dancer.
- A 2024 cleric or paladin entry, or a warlock tie. The sources give none.

**Answer 1: temples or shrines in Waterdeep and ward.** None placed by a source. The wiki places worship in Waterdeep and a planned shrine.

> Eilistraee was commonly worshiped in Cormanthor among the drow there, in the Dalelands among the half-elves,<ref>{{Cite book/Player's Guide to Faerun|22, 25}}</ref> in Waterdeep and Skullport,<ref name="DD" /> and had a following among the Aevendrow of Callidae as well.<ref name="GE"/>
— `wiki.txt:370`

> For example, the citizens of Waterdeep witnessed the Dark Dancer, as she danced in the moonlight, near the walls of the city, up the road to Amphail. This led many moondancers to the City of Splendors, with the goal of creating a shrine to their goddess (the Dancing Haven) within its walls.<ref name="DM" />
— `wiki.txt:473`

Undermountain temple (not a ward): `sources/adventure-wdmm.json:30509` (17e, Level 10).

**Answer 2: campaign NPC, faction or quest that uses Eilistraee.** None. Zero campaign matches.

**Answer 3: wiki lines that mention Waterdeep.** `wiki.txt:328` (Field 5 D), `wiki.txt:370` and `wiki.txt:473` (Answer 1). Two board-game sources carry "Waterdeep" in their titles, not the city.

> | source = [[Lords of Waterdeep (board game)|''Lords of Waterdeep'']]  (source of "The Dark Lady smiles on those who see the deeper beauty within.")
— `wiki.txt:182`

> | board game refs     = ''[[Lords of Waterdeep: Scoundrels of Skullport]]''
— `wiki.txt:516`

---

## 3. GHAUNADAUR

### Field 1: Identity

**A. 5etools MTF**
> ## Ghaunadaur | source MTF p.53 | pantheon Drow
> - alignment: ['C', 'E']
> - domains: ['War']
> - symbol: Purple eye with black sclera
> - category: The Dark Seldarine
— `5etools.md:1-5`

(No FRHoF, SCAG, PHB, DMG or EGW entry for Ghaunadaur is in the bundle.)

**B. Wiki title row**
> | title               = That Which Lurks<ref name="MTF5e-p53-54">{{Cite book/Mordenkainen's Tome of Foes|53-54}}</ref><ref name="DD-18"/><ref name="FaP3e-p111"/> <br/> The Elder Eye<ref name="DD-18"/><ref name="FaP3e-p111"/> <br/> The Lord of Slime<ref name="bg2">{{Cite game/Baldur's Gate II: Shadows of Amn}}</ref> <br/> The Ancient One<ref name="DD-18"/>
— `wiki.txt:7`

**C. Wiki identity paragraph**
> '''Ghaunadaur''' ({{Pronounce|GON|ah|dowr|refs=<ref name="FaP3e-p111" />}} {{Pronounce|GON|ah|door|refs=<ref name="DD-p18">{{Cite book/Demihuman Deities|18}}</ref>|alt=yes}}) was a greater god of abominations, oozes, and outcasts<ref name="FRC74">{{Cite book/Forgotten Realms Campaign Guide|74}}</ref><ref name="DD-18"/><ref name="FaP3e-p111" /> believed to be touched by the Far Realm.<ref name="FRCG-p64">{{Cite book/Forgotten Realms Campaign Guide|64}}/</ref> Most commonly referred to as '''That Which Lurks''',<ref name="MTF5e-p53-54" /> Ghaunadaur was a member of the Dark Seldarine, the drow pantheon, but broke off following the War of the Spider Queen<ref name="FRC74" /> before rejoining after the Second Sundering.<ref name="MTF5e-p53-54" />
— `wiki.txt:100`

**D. Wiki aspects row**
> | aspects             = Ghaunadar<ref name="DD-18"/><br/>Gormauth Souldrinker<ref name="DD-18"/><ref name="DotU-27" /><br/>Juiblex<ref name="DD-18"/><br/>Elder Elemental God<ref name="DD-18"/>
— `wiki.txt:9`

**E. Wiki power and alignment rows, by edition**
> | power5e             =  (empty)
> | alignment5e         = Chaotic evil
> | power4e             = Greater deity
> | alignment4e         = Chaotic evil
> | power3e             = Lesser deity
> | alignment3e         = Chaotic evil
> | power2e             = Lesser deity
> | alignment2e         = Chaotic evil
— `wiki.txt:21-22`, `35-36`, `50-51`, `65-66`

**F. Wiki category**
> Category:Great Old One patrons
— `wiki.txt:175` (link brackets dropped from `[[Category:Great Old One patrons]]`)

### Field 2: Edict or core tenet

**A. 5etools MTF**
> This entity is most often referred to as That Which Lurks, because uttering its real name risks attracting its attention. Its actual form, if it even has one, is unknown; it's most often represented as an ooze-like creature with many tentacles or a purple pupil surrounded by black instead of white. The liquid nature of Ghaunadaur is symbolic of its unpredictable nature, which is what makes attracting its attention so risky. It occasionally rewards its followers with supernatural powers or wealth, but it's equally likely to curse its faithful with hideous torments and afflictions. A subterranean hunter who whispers Ghaunadaur's name might stumble into a forgotten treasure trove, while a devoted priestess who offers long prayers and valuable sacrifices is consumed by a gelatinous cube. The entity's random behavior can be an attraction to drow who lack status and are desperate to achieve it. A small sacrifice and a prayer to That Which Lurks might simply go unnoticed by Ghaunadaur, or it might punish the petitioner, but there is also a chance of receiving a great reward.
— `5etools.md:7`

**B. Wiki personality**
> Ghaunadaur was an unpredictable deity. False worshipers were sometimes rewarded by it, occasionally even with permanent magical boons, but they might just as well have been devoured by the Elder Eye without a second thought. Ghaunadaur enjoyed watching large horrible monsters as they hunted and devoured their prey, causing much suffering. When Ghaunadaur left the Inner Planes he was always silent, but some old records mention a gibbering and bestial language being spoken in the god's court. When communicating, Ghaunadaur used telepathy and kept its conversations blunt and simple.<ref name="FaP3e-p111" />
— `wiki.txt:110`

**C. Wiki clerics' doctrine**
> Ghaunadaur didn't care much about the bonds that held its clergy together, and in accordance with his doctrine, clerics that murdered each other to attain higher status didn't displease the Ancient Eye.<ref name="AotL-ch6">{{Cite book/Ascendancy of the Last||6}}</ref>
— `wiki.txt:124`

### Field 3: Portfolio and areas of concern

**A. Wiki 5e portfolio, 4e sphere and domains**
> | portfolio5e         = Oozes, slimes, outcasts
> | sphere4e            = Abominations
> | domains4e           = Destruction, Earth, Madness
— `wiki.txt:28`, `42`, `43` (link brackets dropped from the portfolio row)

**B. Wiki 2e portfolio**
> | portfolio2e         = Oozes, slimes, jellies, outcasts, ropers, rebels, all thing subterranean
— `wiki.txt:72` (link brackets dropped)

**C. Wiki 3e domains**
> | domains3e           = Cavern, Chaos, Drow, Evil, Hatred, Slime
— `wiki.txt:58` (link brackets dropped)

Per MTF 5e the domain is War.
— `5etools.md:3` ("- domains: ['War']")

### Field 4: Worship (Waterdeep first)

Waterdeep: none. No source places a Ghaunadaur temple or shrine in Waterdeep. Undermountain temples are in Answer 1.

**A. Wiki church**
> The church of Ghaunadaur consisted of cults scattered throughout the Underdark, each dominated by a single individual. There were only a few drow and aboleth cities that served as exceptions, with a more organized clergy. Clerics of Ghaunadaur were required to serve the Elder Eye completely and do whatever pleased it most. The main duty of Ghaundaur's clerics was to ensure, in any way necessary, that Ghaunadaur's altars were supplied with a steady supply of sacrifices. Clerics successful in these sacrifices were rewarded with magic power and items. Ghaunadaur enjoyed most of all those creatures that willingly offered themselves to it, whether or not they had been charmed or coerced by its clerics. Those clerics that succeeded in bringing willing sacrifices to Ghaunadaur's altars were its most favored and highest-ranked servants.<ref name="FaP3e-p111" />
— `wiki.txt:120`

**B. Wiki shrines and temples**
> Shrines and temples devoted to Ghaunadaur were foul. Rooms were often filled with fetid smells, mists, and slime trickling down the walls that made puddles and little pools. These manifestations would be strongest around the halls where sacrificial rituals would take place. The stench was so strong that others would perceive it as swimming through rotten sewage.<ref name="AotL-ch6" />
— `wiki.txt:126`

**C. Wiki rituals**
> Ghaunadaur's clergy prayed for their spells once per day at any time the local cult deemed important. The Elder Eye expected each prayer to be coupled with a sacrifice. It preferred living offerings, but when that was impossible it also accepted bones and food that were burned in oil while braziers of perfumed incense were burned as well. If the worshiper could not deliver any offerings to the deity, they were required to perform their prayer while holding one unprotected hand in an open flame.<ref name="FaP3e-p111" />
— `wiki.txt:131`

**D. Wiki the Gathering**
> Ghaunadans went on the Gathering, which consisted of incursions meant to kidnap and abduct sentient beings for the sacrificial altar of Ghaunadaur. These individuals were drugged and held under compulsion and pushed to walk up to the altar, where the leading cleric would pray and turn into slime. The slime then enveloped the victim and consumed them. This process could be repeated several times depending on the number of available subjects.<ref name="AotL-ch6" />
— `wiki.txt:133`

**E. Wiki omen**
> Although he was usually represented with an eye engraved in a purple disk, older manifestations could take shape in the form of a ''"Y"''. This symbol could appear as a demonstration of favor or could be found in ancient spaces devoted to the Lord of Slime.<ref name="AotL-ch6" />
— `wiki.txt:107`

**F. Wiki slime lords (link brackets dropped)**
> Slime lords were considered Ghaunadaur's favorite servants. More powerful among them could change their form to serve as his spies and infiltrators.<ref name="PGtF-p186">{{Cite book/Player's Guide to Faerûn|186-187}}</ref>
— `wiki.txt:128`

Holy days: none in any source.

### Field 5: Relations with other powers, and origin

**A. Wiki allies and servants (link brackets dropped)**
> Ghaunadaur was thought to have no allies,<ref name="FaP3e-p111" /> but this was not always true, as the archomental Bwimb and the deity Moander were counted as his allies.<ref name="DD-18"/> On the material plane, he was served by the drow oozemaster Kurolaboath Notepirroth.<ref name="Pgate-Port">{{Cite web/Perilous Gateways/Dark Elf Portals: The Portal of the Dead Goddess}}</ref>
— `wiki.txt:113`

**B. Wiki foes (link brackets dropped)**
> Conversely, Ghaunadaur's list of foes was extensive. He was an enemy of nearly every god associated with the Underdark as well as the entire Seldarine (for being a member of the Dark Seldarine), Malar, and Gargauth.<ref name="DD-18" />
— `wiki.txt:115`

**C. Wiki origin legend**
> According to Lolth, "Ghaunadaur was old even before Ao's time."<ref name="AotL-p3">{{Cite book/Ascendancy of the Last|3}}</ref> He was a very ancient deity, rumored to have emerged from the primordial ooze itself. In that age, it was worshiped by the largest of slimes and other crawling creatures, many of which contained an alien intelligence. In a rage over some unknown transgression, however, Ghaunadaur struck most of them mad and took their intellects. As an unforeseen result, many of these worshipers ceased to exist, which caused the Elder Eye's power to collapse.<ref name="FaP3e-p111" />
— `wiki.txt:138`

**D. Wiki Ilythiir**
> Ghaunadaur was worshiped by some of the dark elves of Ilythiir beginning in the age of First Flowering<ref name="LEoF-51">{{Cite book/Lost Empires of Faerûn|51}}</ref> and continuing through the Crown Wars.<ref name="TGHotR-15">{{Cite book/The Grand History of the Realms|15}}</ref><ref name="LEoF-52">{{Cite book/Lost Empires of Faerûn|52}}</ref><ref name="CEotE-31">{{Cite book/Cormanthyr: Empire of the Elves|31}}</ref> Later, Ghaunadaur became a member of the drow pantheon because of worship by drow disaffected with Lolth.<ref name="FaP3e-p111" />
— `wiki.txt:142`

**E. Wiki 1379 DR**
> In 1379 DR, Ghaunadaur, finally fed up with Lolth, left the Demonweb Pits and created a new realm in the Deep Caverns.<ref name="GHotR-159">{{Cite book/The Grand History of the Realms|159}}</ref>
— `wiki.txt:144`

### Field 6: Campaign and published-adventure mentions

**Campaign: no matches.** Grep of `campaign/` for `Ghaunadaur|That Which Lurks|Elder Eye|Lord of Slime|Weeping Eye|ooze god|slime god` returned no matches. `campaign-hits.txt` is empty.

**Published adventure, Undermountain (all in `sources/adventure-wdmm.json`; none in WDH)**

> A character who sees the statue can, with a successful {@dc 15} Intelligence ({@skill Religion}) check, ascertain that it represents Ghaunadaur, god of oozes, slimes, and all things subterranean.
— `sources/adventure-wdmm.json:29977` (Level 10, statue)

> Ghaunadaur, a god of subterranean horrors, is respected and feared by many Underdark races, including drow. This temple contains the following features:
— `sources/adventure-wdmm.json:30408` (Level 10, "17a. Temple of Ghaunadaur" at `:30404`)

> The Caverns of Ooze have, at various times, served as a temple and sanctuary for worshipers of Ghaunadaur, the evil god of oozes, slimes, and other subterranean horrors. Halaster rewards these mad zealots by transforming them into oozes that retain most of their memories and intelligence. These servants of Ghaunadaur believe the god himself has blessed them. The Mad Mage does nothing to discourage this impression.
— `sources/adventure-wdmm.json:50909` (Level 19, "Caverns of Ooze", heading at `:50863`)

> Followers of Ghaunadaur whom Halaster lures to Undermountain invariably visit a floating orb that weeps primordial ooze in {@area area 4|988|x}. The orb is thought to be part of Ghaunadaur himself. His worshipers sometimes refer to the object as the Weeping Eye. In truth, Halaster found the oozing orb and brought it here solely to flood the caverns and mislead Ghaunadaur's vile devotees.
— `sources/adventure-wdmm.json:50910`

> {@b Intelligent Oozes}. Clinging to the 20-foot-high ceiling are three intelligent black puddings that were once drow worshipers of Ghaunadaur (see \"{@area Intelligent Black Puddings|975|x}\"). These oozes are hostile toward all intruders. (A battle here also attracts the {@creature Huge gray ooze|WDMM} in {@area area 14|9b3|x}.)
— `sources/adventure-wdmm.json:52141` (Level 19, "12. Ghaunadaur Shrine" at `:52137`)

> If the altar is opened, the multi-armed representation of Ghaunadaur animates and attacks creatures within 10 feet of it or within 5 feet of the altar. The statue is a Large object with AC 17, 50 hit points, a speed of 0 feet, and immunity to acid, poison, and psychic damage. It has the following ability scores: Strength 14, Dexterity 10, Intelligence 3, Wisdom 3, and Charisma 1. It has {@sense blindsight} out to a range of 10 feet and is blind beyond this radius.
— `sources/adventure-wdmm.json:52144`

Also listed by file:line: `sources/adventure-wdmm.json:30404` (heading), `:30762` (fountain, quoted under Eilistraee), `:50905` (heading "Worshipers of Ghaunadaur"), `:50919`, `:50926`, `:50961`, `:51881` (heading "5. In the Grip of Ghaunadaur"), `:51892`, `:52137` (heading).

### Field 7: Conflicts and what was not found

**Conflict 1: domains.** 5etools MTF gives War, and the wiki's 5e row also gives War. The wiki's 4e and 3e rows differ.

> | domains4e           = Destruction, Earth, Madness
— `wiki.txt:43`

> | domains3e           = Cavern, Chaos, Drow, Evil, Hatred, Slime
— `wiki.txt:58`

**Conflict 2: planes.** The wiki's 4e, 3e and 2e rows name different planes.

> | dominion4e          = Dismal Caverns
— `wiki.txt:38` (link brackets dropped)

> | homeplane3e         = Demonweb Pits
— `wiki.txt:53` (link brackets dropped)

> | homeplane2e         = Paraelemental Plane of Ooze
— `wiki.txt:68` (link brackets dropped)

**Not found**
- Holy days (blank in every edition row: `wiki.txt:32`, `47`, `62`, `77`).
- Any Waterdeep line for the Ghaunadaur page itself.
- A 5etools FRHoF, SCAG or PHB entry (none in the bundle).
- A warlock patron statement from a source other than the category tag at `wiki.txt:175`.

**Answer 1: temples or shrines in Waterdeep and ward.** None. Undermountain only: "17a. Temple of Ghaunadaur" (Level 10, `sources/adventure-wdmm.json:30404`), the Caverns of Ooze (Level 19, `:50909`), and the "12. Ghaunadaur Shrine" (Level 19, `:52137`).

**Answer 2: campaign NPC, faction or quest that uses Ghaunadaur.** None.

**Answer 3: wiki lines that mention Waterdeep.** None on the Ghaunadaur page. The Eilistraee page names Ghaunadaur's avatar as the threat to Waterdeep (quoted under Eilistraee, Field 5 D, `wiki.txt:328`).

---

## 4. CORELLON LARETHIAN

### Field 1: Identity

**A. 5etools MTF p.43**
> ## Corellon Larethian | source MTF p.43 | pantheon Elven
> - alignment: ['C', 'G']
> - domains: ['Arcana', 'Life', 'Light', 'War']
> - symbol: Quarter moon or starburst
> - category: The Seldarine
— `5etools.md:1-5`

**B. 5etools PHB p.296**
> ## Corellon Larethian | source PHB p.296 | pantheon Nonhuman
> - title: Elf deity of art and magic
> - alignment: ['C', 'G']
> - domains: ['Light', 'Arcana']
> - symbol: Quarter moon or starburst
— `5etools.md:19-23`

**C. 5etools SCAG p.23**
> ## Corellon Larethian | source SCAG p.23 | pantheon Elven
> - title: God of art and magic
> - alignment: ['C', 'G']
> - domains: ['Arcana', 'Light']
> - symbol: Crescent moon
— `5etools.md:27-31`

**D. Wiki title row**
> | title               = Coronal of Arvandor<ref name="DDp101"/><ref name="F&Pp125-126"/><br /> Ruler of All Elves<ref name="DDp101"/><ref name="F&Pp125-126"/><br /> Creator of the Elves<ref name="DDp101"/><ref name="F&Pp125-126"/><br /> Father of Elvenkind<ref name="HCCAG9">{{Cite dragon/408/History Check: Corellon and Gruumsh|9}}</ref><br /> First of the Seldarine<ref name="DDp101"/><ref name="F&Pp125-126"/><br /> Preserver of Life<ref name="DDp101"/><ref name="F&Pp125-126"/><br /> The Protector<ref name="DDp101"/><ref name="F&Pp125-126"/><br /> The Big Fairy (derogatory)<ref name="DM62">{{Cite dragon/62/The Gods of the Orcs|28}}</ref><br/>Lord of Cowardice (derogatory)<ref name="HCCAG8">{{Cite dragon/408/History Check: Corellon and Gruumsh|8}}</ref><br/>Lord of the wood<ref name="DP-p90">{{Cite book/Divine Power|90}}</ref><br/>Lord of the stars<ref name="DP-p90"/><br/>Maker of songs<ref name="DP-p90"/><br/>Teacher of arts<ref name="DP-p90"/><br/>Lord of magic<ref name="DP-p90"/><br/>Lord of starlight<ref name="DP-p90"/><br/>Lover of beauty<ref name="DP-p90"/><br/>Poet of night<ref name="DP-p90"/>
— `wiki.txt:11`

**E. Wiki identity paragraph**
> '''Corellon''', or more fully '''Corellon Larethian''' ({{Pronounce|kor|el|un|_|la|RETH|ee|an|refs=<ref name="D.93.APG-p26">{{Cite dragon/93/Ay pronunseeAYshun gyd|26}}</ref>|audio=Corellon.ogg}}), whose titles included '''Creator of the Elves''' and '''the Protector''', was the patron god of all elves. He was the creator and preserver of the Tel'Quessir, governing those things held in the highest esteem among elves, such as magic, music, arts, crafts, poetry, and warfare. Corellon lived in the realm of Arvandor. He blessed those who aided others and became angered at those who defiled the dead.<ref name="DDp101">{{Cite book/Demihuman Deities|101-103}}</ref><ref name="F&Pp125-126">{{Cite book/Faiths & Pantheons|125-126}}</ref>
— `wiki.txt:103`

**F. Wiki pantheon, symbol, power and alignment rows**
> | pantheon            = Seldarine
> | power5e             = Deity
> | symbol5e            = Quarter moon or starburst
> | power4e             = Greater deity
> | alignment4e         = Good
> | power3e             = Greater deity
> | alignment3e         = Chaotic good
> | power2e             = Greater deity
> | alignment2e         = Chaotic good
> | power1e             = Greater deity
> | alignment1e         = Chaotic good
— `wiki.txt:14`, `20`, `22`, `35-36`, `50-51`, `66-67`, `80-81`

### Field 2: Edict or core tenet

**A. 5etools MTF**
> The creator of all elves is both chaos and beauty personified. Corellon is as fluid and changeable as a breeze or a brook-quick to anger, but equally quick to forgive and forget. The god loves magic, artistry, nature, and freedom. Anyone who has felt the mystical presence of Corellon describes it as a joy like no other, followed by a deep melancholy when his presence is no longer felt.
— `5etools.md:7`

**B. 5etools MTF**
> Corellon doesn't expect much from followers-no complex rituals or frequent ceremonies or even regular prayer. Corellon wants them to enjoy life, to try new things, to imagine what they desire and then pursue it, and to be kind to others. In return for this freedom from the usual requirements of religion, Corellon expects them to address their own problems and not pray for aid in every crisis. These precepts are instilled within every elf, since all elves are ultimately descended from fragments of Corellon. When elves ask their priests how one might become able to sense Corellon's presence, the priests often say, "First, truly know yourself. Only then can you feel our creator near." Services in Corellon's honor are typically conducted in natural stone amphitheaters or bowl-shaped forest clearings. In keeping with Corellon's chief commandment for everyone to be free, all who attend are allowed to show their obeisance however they choose, as long as their way of contributing combines with the others to form a grand display of reverence. Such a gathering has the atmosphere of a festival rather than of an organized worship service.
— `5etools.md:8`

**C. Wiki**
> All life in its many forms was sacred to Corellon and as one is vigilant against their enemies so should they be vigilant against their own shortcomings and lapses in judgement less they become the very thing they fought against.<ref name="MM-p26"/>
— `wiki.txt:121`

**D. Wiki**
> The Protector believed that mercy, love and pity were the three most important traits that a good person should have and emphasized showing those traits when dealing with those who walk the path of evil. The god frowned upon mortals who dispense cruelty and death when the situation does not call for it or could easily be avoided. Despite this, Corellon sometimes did not heed his own mantra and enacted harsh poetic justice, with little place for forgiveness. Even so, when enough time passes, the god was humble enough to realize when he overreacted in his judgement or in the wrong and made sure to do everything in his power to make amends.<ref name="MM-p26">{{Cite book/Monster Mythology|26}}</ref>
— `wiki.txt:123`

### Field 3: Portfolio and areas of concern

**A. Wiki 5e portfolio and domains**
> | portfolio5e         = Art, magic
> | domains5e           = Arcana, Life, Light, War
— `wiki.txt:27`, `wiki.txt:28` (link brackets dropped from the domains row)

**B. Wiki 3e and 2e portfolio**
> | portfolio3e         = Arts, crafts, elves (esp. sun elves), magic (elven magic, High Magic), music and bards, poetry and poets, war and warriors
> | portfolio2e         = Arts, crafts, elves (esp. gold elves), magic (elven magic, High Magic), music and bards, poetry and poets, war and warriors
— `wiki.txt:57`, `wiki.txt:73` (link brackets dropped)

**C. Wiki description**
> As the personification of all things elven, Corellon was at once a warrior and a poet, a mage and a bard, and a male and a female. However, in his love of Araushnee, he settled into the aspect of a male gold elf warrior, a counterpart to her female dark elf artist.<ref name="EIotE-29">{{Cite book/Evermeet: Island of Elves/MMP|29}}</ref> While he retained the capacity to assume female or male form, he conventionally appeared as an androgynous male elf possessed of lithe build and preternatural beauty. His avatars stood {{SI|7|ft|long=yes}} tall and displayed exceptional speed, reflexes, and grace, as well as a strength obvious to all.<ref name="DD-101">{{Cite book/Demihuman Deities|101}}</ref>
— `wiki.txt:111`

### Field 4: Worship (Waterdeep first)

**A. Waterdeep: Temple of the Seldarine, Castle Ward.** The Major Temples table in `sources/adventure-wdh.json` (caption at line 30910) has this row, lines 30927-30930. The generic "All deities | Holyhands House | North Ward" row above it (lines 30922-30925) applies to every power and is not specific to Corellon.

> "All elven deities",
> "Temple of the Seldarine",
> "Castle Ward"
— `sources/adventure-wdh.json:30928-30930`

The campaign gazetteer agrees.
> - Temples of the ward: the Temple of the Seldarine for all elven gods, the Spires of the Morning for Lathander, one of the city's most beautiful temples, the Font of Knowledge for Oghma, with the library, and the Halls of Justice for Tyr (see Landmarks).
— `campaign/gazetteer/waterdeep/castle-ward.md:164`

> - The Temple of the Seldarine and the Spires carry no campaign hook yet. [research]
— `campaign/gazetteer/waterdeep/castle-ward.md:166`

**B. 5etools MTF**
> Cryptic shrines to the Mysteries of Arvandor appear throughout the planes, mostly sites where carved or painted stars cover the ceiling of a cave. On the planes that have hosted one of these rare events, elf priests consecrate and maintain temples devoted to the Mysteries. Often these sacred sites are natural spaces that have intrinsic magical properties.
— `5etools.md:14`

**C. Wiki orders**
> * Fellowship of the Forgotten Flower: The fellowship was a loosely structured organization made of elven knights or elven warriors dedicated to the recovery of lost elven relics from long-abandoned realms.<ref name="DDp101"/>
> * Knights of the Golden Wyrm<ref name="DD-p124">{{Cite book/Demihuman Deities|124}}</ref>
> * Swords of the Seldarine<ref name="DD-p124"/>
> * Blade of Sahandrian<ref name="DD-p124"/>
> * Fey Staghorns<ref name="DD-p124"/>
> * Wings of Yathaghera<ref name="DD-p124"/>
> * Knights of the Alicorn<ref name="DD-p124"/>
> * Weavers of Bladesong<ref name="DD-p124"/>
> * Vassals of the Reverend Ones<ref name="DD-p124"/>
> * Swords of Evereska<ref name="DD-p124"/>
— `wiki.txt:182-191` (heading `wiki.txt:181`)

**D. Wiki temples category**
> {{Main|:Category:Temples to Corellon Larethian}}
— `wiki.txt:194` (lists no entries; the category is not in the bundle)

**E. Wiki holy day**
> | holy days4e         = Shieldmeet
— `wiki.txt:47` (link brackets dropped)

**F. Wiki servitors (link brackets dropped)**
> The Seldarine as whole, Corellon included, favored agathinons, asuras and elder treants as agents of their will. The Father of Elvenkind also had the following species under his command: aasimar, aasimon (such as his twin solars), baelnorn, buraq, cath shee, centaurs, cooshee, disenchanters, dryads, einheriar, eladrins (particularly firres and ghaeles), elven cats, feystags, firestars, firetails, gold dragons, hamadryads, hollyphants, hybsils, incarnates of charity, courage, faith, hope, justice, temperance, and wisdom, ki-rin, kholiathra, lillendi, lythari, maruts, moon dogs, moon-horses, noctrals, nymphs, oreads, pers, phoenixes, reverend ones, seelie faeries, sharn, silver dogs, silver dragons, sylphs, spectral wizards, spellhaunts, sprites, sunflies, t'uen-rin, unicorns, weredragons, and wizshades.<ref name="DD-p122">{{Cite book/Demihuman Deities|122}}</ref>
— `wiki.txt:177`

No Waterdeep line appears in the wiki's Corellon worship text.

### Field 5: Relations with other powers, and origin

**A. Wiki leader of the Seldarine**
> Corellon was the leader of the Seldarine, the elven pantheon,<ref name="F&Pp125-126"/> and was generally close with all of them, except Fenmarel Mestarine<ref name="DD-92">{{Cite book/Demihuman Deities|92}}</ref> who was the partner in adultery of Lolth, his former wife.<ref name="DD-111">{{Cite book/Demihuman Deities|111}}</ref> After the latter's banishment he was married to Angharradh.<ref name="F&Pp125-126"/> Of the three children he had with his first wife, only Vandria Gilmadrith remained with him in the Seldarine.<ref>{{Cite book/Races of the Wild|23-24}}</ref>
— `wiki.txt:151`

**B. Wiki Eilistraee**
> He was allied with his daughter Eilistraee.<ref name="F&Pp125-126"/> This relationship was polite but distant, and Erevan Ilesere was closer to his daughter than he was.<ref name="DDp13">{{Cite book/Demihuman Deities|13}}</ref> He was also known to be on good terms with the other deities of magic Azuth, Mystra, and (through Sehanine) Savras.<ref name="MoF-p8">{{Cite book/Magic of Faerûn|8}}</ref>
— `wiki.txt:156`

**C. Wiki Dark Seldarine enemies**
> Corellon counted the whole drow pantheon, the Dark Seldarine, as his enemies. These included Lolth, his former wife; Vhaeraun, his son; and Selvetarm, his grandson, with only his daughter Eilistraee an exception.<ref name="DD-100" /><ref name="F&Pp125-126" />
— `wiki.txt:167`

**D. Wiki Vhaeraun exile**
> After Vhaeraun's betrayal during the War of the Seldarine, Corellon Larethian exiled him.<ref name="E.IoE-69">{{Cite book/Evermeet: Island of Elves/MMP|68-69}}</ref> He gave up on the idea of getting his son Vhaeraun to abandon his ways.<ref name="DD-101"/> He even vowed to kill him, if he ever tried to hurt his sister,<ref name="E.IoE-69"/> which was an empty threat, for the Masked Lord did threaten the Dark Maiden's life, without known action against him on Corellon's part.<ref name="E.IoE-109">{{Cite book/Evermeet: Island of Elves/MMP|109}}</ref>
— `wiki.txt:171`

**E. Wiki origin, the Larethian absorption (first paragraph)**
> The Coronal of Arvandor, prior to being known as Corellon Larethian was just Corellon in the beginning until he consumed another deity by the name of Larethian, claiming their powers and byname.<ref name="GG-SS">{{Cite archive/Greenwood's Grotto/2023-03-10/Seldarine "surnames"}}</ref> Corellon dominated Larethian's mind and absorbed the god without killing them, before finally annexing Larethian's church and faithful.<ref name="LLOTR-10">{{Cite web/Ed Greenwood's Patreon/Lost Lore of the Realms 10}}</ref> Larethian seemed to have had some connection and involvement in the previously mentioned ''Twin Brother'' heresy, much of which was shrouded in mystery.<ref name="Q&A-5">{{Cite web/Ed Greenwood's Patreon/Q&A 5}}</ref>
— `wiki.txt:214`

**F. Wiki origin, the Ysgardian hunter and Arvandor (first paragraph)**
> Corellon originally came from the plane of Ysgard where he was the god of hunting and archery. The Ysgardian hunter aspect was engaged in a long-protracted conflict with the beast lord Malar who had killed and hurt several of Corellon's loved ones, family and friends alike, vowing to never end the hunt until all of them were avenged while also motivated to keep those he cherished from harm's way, which only Malar's death could grant.<ref name="Q&A7">{{Cite web/Ed Greenwood's Patreon/Q&A 7}}</ref> At some point, he decided to conquer part of Arborea by driving out the resident giants and thus Arvandor was founded. The surviving giants went to the land, the elves abandoned their emigration to Arvandor and founded Jotunheim on Ysgard, the first layer of Ysgard.<ref name="39, 115">{{Cite book/Planes of Chaos/The Book of Chaos|39, 115}}</ref> With the passage of time and the changing of Corellon's personality, the Ysgardian aspect faded away and lost all worshipers, and the conflict with Malar took a back seat, as the troubles the elves faced in days ahead required Corellon's full attention and leadership that only the Allfather of Elvenkind could grant.<ref name="Q&A7"/>
— `wiki.txt:216`

### Field 6: Campaign and published-adventure mentions

**Campaign: Corellon as a god.** One line.

> **Relationships.** Fala is a close friend of Ziraj the Hunter (Doom Raiders assassin, who keeps a room on Fala's second floor), a neighbor and confidant of Tally Fellbranch, and a member of the Guild of Apothecaries and Physicians. Fala uses they/them pronouns, reflecting Corellon Larethon's genderless nature.
— `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:26`

**Campaign: shop name only (38 lines).** "Corellon's Crown" is Fala Lefaliir's greenhouse in Trollskull Alley. Files and lines:
— `campaign/guides/trollskull-manor/06-tavern-time.md:60`, `campaign/guides/trollskull-manor/08-notable-patrons.md:27`, `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:26`, `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:24`, `campaign/quests/act-i/trollskull-alley/overview.md:34`, `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/design-notes.md:15`, `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:338`, `:342`, `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-02-the-debrief.md:11`, `:149`, `:153`, `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/overview.md:56`, `:77`, `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/design-notes.md:5`, `:15`, `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:8`, `:16`, `:28`, `:74`, `:82`, `:90`, `:114`, `:255`, `:261`, `:339`, `:350`, `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/overview.md:23`, `:27`, `:37`, `:62`, `campaign/setting/notable-figures/doom-raiders/06-ziraj-the-hunter.md:22`, `:26`, `:30`, `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:16`, `:30`, `campaign/setting/organizations/06-doom-raiders.md:40`, `campaign/structure/arc-b-trollskull-alley.md:39`, `:97`. That is 38 lines. The 39th campaign line is the god line above.

**Published adventure, the god line**
> "{@creature Fala Lefaliir|WDH} is an outgoing wood elf with long, braided hair. Like the elven god Corellon Larethian, Fala is neither male nor female. If referred to as \"he\" or \"she,\" Fala gently requests to be addressed by name or as \"they.\" Fala is friends with a member of the Zhentarim named Ziraj, who saved Fala's life. He visits Fala from time to time, and Fala has set aside a room for him on the second floor.",
— `sources/adventure-wdh.json:3432`

Shop-name lines: `sources/adventure-wdh.json:3427` ("name": "T4. Corellon's Crown"), `:3928` (Ziraj is cornered "in the greenhouse of Corellon's Crown in Trollskull Alley"), `:4472` (Fala, "the owner of Corellon's Crown").

### Field 7: Conflicts and what was not found

**Conflict 1: domains (all 2014).** The MTF, PHB and SCAG entries disagree. The wiki's 5e row matches MTF. No FRHoF entry exists to rank above them.

> - domains: ['Arcana', 'Life', 'Light', 'War']
— `5etools.md:3` (MTF)

> - domains: ['Light', 'Arcana']
— `5etools.md:22` (PHB)

> - domains: ['Arcana', 'Light']
— `5etools.md:30` (SCAG)

**Conflict 2: symbol.** MTF and SCAG disagree.

> - symbol: Quarter moon or starburst
— `5etools.md:4` (MTF)

> - symbol: Crescent moon
— `5etools.md:31` (SCAG); wiki 2e: `wiki.txt:68`, "| symbol2e            = Crescent moon"

**Conflict 3: gender.** The campaign Fala line calls Corellon's nature "genderless". The wiki says Corellon "conventionally appeared as an androgynous male elf" and was "a male and a female".
— `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:26` and `wiki.txt:111`. The wiki's gender row (`wiki.txt:17`) notes that all sources use male pronouns.

**Not found**
- Holy days other than Shieldmeet (`wiki.txt:47`).
- Omens and messengers in any 5etools or campaign entry. The wiki gives servitors (`wiki.txt:177`) only.
- A FRHoF entry (none in the bundle).
- A campaign file in which an NPC worships Corellon. The only god line is `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:26`.
- A 2024 warlock tie. The sources give none.

**Answer 1: temples or shrines in Waterdeep and ward.** The Temple of the Seldarine, Castle Ward, for all elven gods (`sources/adventure-wdh.json:30928-30930` and `campaign/gazetteer/waterdeep/castle-ward.md:164`). The gazetteer notes it has no campaign hook (`:166`). Corellon's Crown in Trollskull Alley is a shop, not a temple.

**Answer 2: campaign NPC, faction or quest that uses Corellon as a god.** None worships him. The only deity line is Fala Lefaliir's pronoun note (`campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:26`). The other 38 campaign lines name the shop.

**Answer 3: wiki lines that mention Waterdeep.** None.

---

## 5. GARL GLITTERGOLD

### Field 1: Identity

**A. 5etools MTF p.111**
> ## Garl Glittergold | source MTF p.111 | pantheon Gnome
> - alignment: ['L', 'G']
> - domains: ['Trickery']
> - symbol: Gold nugget
— `5etools.md:1-5`

**B. 5etools PHB p.296**
> ## Garl Glittergold | source PHB p.296 | pantheon Nonhuman
> - title: Gnome god of trickery and wiles
> - alignment: ['L', 'G']
> - domains: ['Trickery']
> - symbol: Gold nugget
— `5etools.md:11-15`

**C. 5etools SCAG p.24**
> ## Garl Glittergold | source SCAG p.24 | pantheon Gnomish
> - title: God of trickery and gems
> - alignment: ['L', 'G']
> - domains: ['Trickery']
> - symbol: Gold nugget
— `5etools.md:19-23`

**D. Wiki titles**
> | title               = The Joker<ref name="FP-p135"/><ref name="DD-151"/> <br/> The Priceless Gem<ref name="DD-151"/> <br/> The Sparkling Wit<ref name="FP-p135"/><ref name="DD-151"/> <br/> The Watchful Protector<ref name="FP-p135"/><ref name="DD-151"/><br/>The Father of All Gnomes<ref>{{Cite book/Prince of Lies|231}}</ref>
— `wiki.txt:11`

**E. Wiki identity paragraph**
> '''Garl Glittergold''' ({{Pronounce|garl|refs=<ref name="FP-p135"/>}}), also known as '''The Watchful Protector''', was a lawful good greater deity of gnomes. Garl led the Lords of the Golden Hills as the deity of luck, protection, and trickery.<ref name="FP-p135"/>
— `wiki.txt:106`

**F. Wiki pantheon and alignment rows**
> | pantheon            = Lords of the Golden Hills
> | alignment5e         = Lawful good
> | alignment4e         = Good<ref name="FRCG-p80"/>
> | alignment3e         = Lawful good
> | alignment2e         = Lawful good
— `wiki.txt:16`, `26`, `41`, `56`, `72` (link brackets dropped)

### Field 2: Edict or core tenet

**A. 5etools MTF**
> A joker and a prankster, Garl Glittergold reminds gnomes that life is to be taken lightly, and that a good laugh will serve them better than a grim attitude. When Garl cavorts with mischief on his mind, Moradin's beard might end up woven with giggling flowers, and Gruumsh's axe could sprout braying donkey heads at the most inopportune time.
— `5etools.md:7`

**B. 5etools MTF**
> Cooperation Is Key: The legends about Garl Glittergold inspire gnomes to work together. Garl knows that many heads and many hands make light work. Although he also plays many pranks on his own, Garl is the one who gathers the heroes together for an enterprise that requires all their talents. To provide specific guidance, Garl might send an omen to nudge a group of gnomes in a certain direction, or even manifest an avatar in the middle of a gnome burrow. When Garl makes one of these rare appearances, it is to resolve a dispute that threatens a community.
— `5etools.md:8`

**C. 5etools MTF**
> Brains over Brawn: Garl favors trickery and illusion over direct combat, preferring to use his mind to overcome a problem rather than his steel. For gnomes to thrive, they must use their intellect and ingenuity. But when push comes to shove, Garl uses Arumdina, his intelligent two-headed battle axe-capable of cleaving through any substance-to escape a perilous situation.
— `5etools.md:9`

**D. Wiki quoted from Gnomefather**
> Most splendiferous, gregarious, and overall duplicitous of Gods (especially for the gnomes who embody those attributes quite cheerfully) is Garl Glittergold.
— `wiki.txt:107`

### Field 3: Portfolio and areas of concern

**A. Wiki 5e portfolio and domains**
> | portfolio5e         = Primary god of gnomes
> | domains5e           = Trickery
— `wiki.txt:32`, `wiki.txt:33`

**B. Wiki 3e portfolio and domains**
> | portfolio3e         = Humor, Gemcutting, Gnomes, Protection, Trickery
> | domains3e           = Avarice, Craft, Envy, Gnome, Good, Law, Protection, Trickery
— `wiki.txt:62`, `wiki.txt:63` (link brackets dropped)

**C. Wiki 2e portfolio**
> | portfolio2e         = Protection, humor, trickery, gem cutting, finesmithing and lapidary, the gnome race
— `wiki.txt:78`

**D. Wiki 4e sphere and domains**
> | sphere4e            = Protection<ref name="FRCG-p80"/>
> | domains4e           = Creation, Trickery
— `wiki.txt:47`, `wiki.txt:48` (link brackets dropped from the domains row)

### Field 4: Worship (Waterdeep first)

Waterdeep: none. No source names a Garl temple or shrine in Waterdeep or anywhere else in the city.

**A. Wiki followers and clergy**
> Garl was the most popular of the gnomish deities, and honored, in one way or another, by nearly all gnomes. His clerics, known as Glitterbrights, wore war helms and gold belts.<ref name="FP-p135"/>
— `wiki.txt:116`

**B. Wiki Communion of Laughter**
> On the 13th day of each month, the Forgotten Folk held the Communion of Laughter in his honor. It consisted of joke-telling contests, communal meals, dancing, prayers, and storytelling, and donations of gold, which Garl's church used to the benefit of the entire community.<ref name="FP-p135"/>
— `wiki.txt:122`

**C. Wiki order**
> ===Orders===
> *Golden Watchful: A small knightly order of gnome paladins of Garl Glittergold<ref>{{Cite web/theedverse/2019-01-06 - Gnome paladins of Garl Glittergold}}</ref>
— `wiki.txt:118-119`

**D. Wiki temples**
> ''Main article: :Category:Temples to Garl Glittergold''
— `wiki.txt:130` (lists no entries)

**E. 5etools MTF children**
> When gnome children hear their first stories about the gods, they are introduced to a gold-skinned gnome with a wide grin and glittering gemstone eyes that shift colors like a kaleidoscope. The youngsters quickly learn to recognize that their favorite character, the god of the gnomes, is about to steal the show.
— `5etools.md:6`

Omens and avatars are in the 5etools MTF entry (quoted under Field 2, B). Holy days: the 13th of each month (`wiki.txt:122`). No other holy day is sourced.

### Field 5: Relations with other powers, and origin

**A. Wiki allies**
> Aside from the other non-evil members of the gnomish pantheon, Garl was allied with Yondalla, Corellon Larethian, and Moradin. His main companion was his intelligent battleaxe, Arumdina the Justifier.<ref name="FP-p135"/>
— `wiki.txt:110`

**B. Wiki enemies**
> Garl's tendency to jest with the various deities worshiped by the creatures and monsters of the Underdark resulted in him garnering many enemies, but chief among them was the kobold god, Kurtulmak.<ref name="FP-p135"/>
— `wiki.txt:112`

**C. Wiki origin**
> According to legend, Garl Glittergold was exploring underground when he found a new cavern, and inside, a new people—the gnomes. He told them a joke and then led them out into the wider world.<ref name="DD-151"/>
— `wiki.txt:125`

**D. Wiki Kurtulmak legend**
> According to legend, Garl let himself be captured by Kurtulmak, only to escape and cause the entire roof of Kurtulmak's cavern to fall on his head.<ref name="FP-p135"/>
— `wiki.txt:127`

**E. Wiki 2e realms (link brackets dropped)**
> | homeplane2e         = Bytopia/Dothion
> | realm2e             = The Golden Hills (Glitterhome)
— `wiki.txt:74-75`

### Field 6: Campaign and published-adventure mentions

**Campaign: no matches for the god.** Grep of `campaign/` for `Garl|Glittergold|Arumdina|gnome god|Lords of the Golden Hills|Watchful Protector|Communion of Laughter` returns only "Garloth" (Grinda Garloth, a Mistshore armorer, for example `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:1`). None names Garl Glittergold.

**Published adventure: no matches for the god.** Grep of `sources/adventure-wdh.json` and `sources/adventure-wdmm.json` for the Garl alias set returns only "Garloth" (Grinda Garloth, for example `sources/adventure-wdh.json:6169`) and "Garlynth Ironhead" (`sources/adventure-wdmm.json:54056`, a duergar name).

### Field 7: Conflicts and what was not found

**Conflict 1: pantheon label.** The 5etools entries give three different pantheon labels, and the wiki gives a fourth.

> ## Garl Glittergold | source MTF p.111 | pantheon Gnome
— `5etools.md:1`

> ## Garl Glittergold | source PHB p.296 | pantheon Nonhuman
— `5etools.md:11`

> ## Garl Glittergold | source SCAG p.24 | pantheon Gnomish
— `5etools.md:19`

> | pantheon            = Lords of the Golden Hills
— `wiki.txt:16` (link brackets dropped)

**Conflict 2: title.** The PHB and SCAG titles differ.

> - title: Gnome god of trickery and wiles
— `5etools.md:12`

> - title: God of trickery and gems
— `5etools.md:20`

**Conflict 3: domains.** 5etools (MTF, PHB, SCAG) gives Trickery only. The wiki's 3e and 4e rows are wider.

> | domains3e           = Avarice, Craft, Envy, Gnome, Good, Law, Protection, Trickery
— `wiki.txt:63` (link brackets dropped)

> | domains4e           = Creation, Trickery
— `wiki.txt:48` (link brackets dropped)

**Not found**
- Any campaign or published-adventure line that names the god.
- A Waterdeep temple, shrine or festival. The only holy day is the 13th of each month.
- A FRHoF entry (none in the bundle).
- A warlock tie. The sources give none.

**Answer 1: temples or shrines in Waterdeep and ward.** None.

**Answer 2: campaign NPC, faction or quest that uses Garl.** None.

**Answer 3: wiki lines that mention Waterdeep.** None.

---

## Not readable

None. Every bundle file and both adventure JSON files were opened. The `.docx` files in `sources/Other remix files/` were not needed for these five powers.

## Not searched (out of scope in the brief)

- `sources/Appendix_C_-_Player_Faction_Missions.md` (6 alias matches), `sources/Appendix_D_-_Running_the_Tavern.md` (3), `sources/Act_III_Arc_D.md` (1). They were counted by Grep under the aliases and not opened.
- The Alexandrian PDFs and `sources/SOURCE_GUIDE.md`.
