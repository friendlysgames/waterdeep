# Pass 6 research notes: Nihiloor

Page: `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md` (current file, 30 lines)
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Format model: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Day-one state used: Ches 1, 1492 DR. Nihiloor is in Xanathar's lair (campaign area range X23 to X27). Whether Nihiloor dominates Xanathar is recorded as open (section D1). This file does not settle it.

Method and caveats:
- Campaign files: Read and Grep, quoted from the tool output. Paths are under `/home/user/waterdeep/`.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. Escaped quotes are shown as plain quotes. `sources/adventure-wdmm.json` was searched for Seadeeps and Nihiloor.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. PDF quotes were transcribed from rendered page images and are marked `[image transcription]`. Each needs a `pdftotext -layout` check before any quote goes into prose. Pages read in full: `sources/11. Lair  Xanathar’s Lair.pdf` (PDF pp.1 to 9), `sources/5. Faction Outposts.pdf` (PDF pp.1 to 13), `sources/17. Outpost and Lair Revelation Lists.pdf` (PDF pp.1 to 4). Printed page first, then `[PDF p.N]`.
- Appendices: `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md` (Force Grey mission text, which is quest content). `sources/Appendix_D_-_Running_the_Tavern.md` has no Nihiloor entry.
- Wiki: the linked wiki page, `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-xg/Nihiloor.txt` (cited `Nihiloor.txt`). The Guild page copy, `sources/research/pass5-bundles/xanathars-guild/wiki.txt` (cited `wiki.txt`). Its citation keys are quoted. The wiki prints no edition on most lines. The edition is taken from the citation key in the infobox and marked `[5e per WDH5e-p212]` where so.
- Pass 3 and pass 4 bundles were searched. They hold snapshots of campaign text quoted here, plus nothing new.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

---

## A. Background facts by theme

### A1. Origin, home and the Seadeeps payoff

No source gives Nihiloor's birth, origin or how it came to Waterdeep.

**Wiki, opening line (5e citation)**
> "'''Nihiloor''' ({{Pronounce|NY|heh|loor|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a [[mind flayer]] who worked for the [[Xanathar's Thieves' Guild]] in the late 15{{th}} century [[DR]], by creating and spreading [[intellect devourer]]s throughout the sewers of [[Waterdeep]].<ref name="WDH5e-p212" />"
> — `Nihiloor.txt:61` (the wiki's past tense "was" and "worked for" differ from the present-tense campaign page; see D10)

**Wiki infobox, home and race (5e citation WDH5e-p212)**
> "| home           = [[Waterdeep]]<ref name="WDH5e-p212">{{Cite book/Waterdeep: Dragon Heist|212}}</ref>"
> — `Nihiloor.txt:10`
> "| race           = [[Mind flayer]]<ref name="WDH5e-p212" />"
> — `Nihiloor.txt:13`

**Campaign, Key Members entry for Nihiloor (the three-project summary; the Seadeeps payoff)**
> "- **Nihiloor** (DH p. 213) — Mind flayer, lawful evil. Officially handles Xanathar's most sensitive intelligence operations. In practice, Nihiloor is running three concurrent projects: (1) **The Infiltration** — intellect devourers placed inside city government officials give Nihiloor eyes throughout Waterdeep's bureaucracy; three Harper assets are already compromised; (2) **The Experiments** — creatures captured during Arena operations are being subjected to psionic modification seeking a "relay organism" that extends the colony's reach without destroying the host brain; (3) **The Puppet** — Nihiloor has been exerting psionic domination over Xanathar itself for the past four months, replacing its strategic decisions while leaving its personality intact. The long-term payoff of all three projects is the Seadeeps colony (Undermountain Level 17). See the **Nihiloor** page in Notable Figures."
> — `campaign/setting/organizations/08-xanathars-guild.md:103`

**Campaign, Undermountain Level 17 (setting page, Undermountain-facing)**
> "| 17 | Seadeeps | A mind flayer colony. Halaster worries about its war with the githyanki of Level 16. |"
> — `campaign/setting/geography/undermountain-and-skullport.md:72`
> "| 17 | Seadeeps | Mind flayer colony (Nihiloor payoff) | Essential — Dragon Heist thread |"
> — `sources/SOURCE_GUIDE.md:99`

**Undermountain (mark: Undermountain, not Ches 1 lore), published Mad Mage text**
> "A mind flayer colony has taken over a level of Undermountain known as Seadeeps. (Cephalossk knows this because it has been in telepathic contact with the ulitharid on {@adventure level 17|WDMM|17}.)"
> — `sources/adventure-wdmm.json:24431` (Level 9 text)
> `"name": "Level 17: Seadeeps"`, page 221
> — `sources/adventure-wdmm.json:46748`

### A2. Service to Xanathar, role and rank

**Adventure, Appendix B entry (5e)**
> "The illithid {@creature Nihiloor|WDH} works for {@creature Xanathar|WDH}, spending its days creating intellect devourers and setting them loose in the sewers of Waterdeep. Each intellect devourer attacks the first humanoid it encounters, using its victim as a puppet to spy on the city and relay information back to {@creature Nihiloor|WDH}. Occasionally, an intellect devourer is instructed to seek out a particular kind of target, such as a member of the City Guard or the City Watch. Sometimes its instructions will include orders to capture specific Waterdavians and bring them to Skullport, where they can be enslaved or ransomed."
> — `sources/adventure-wdh.json:32353` (entry "Nihiloor", page 212, id "4c4", opened at `:32339`)

> "{@creature Nihiloor|WDH} has an alien mind, and it considers itself {@creature Xanathar|WDH}'s equal. It has no interest in supplanting the beholder, however, preferring to operate in the shadows and pursue its own fell schemes."
> — `sources/adventure-wdh.json:32354` (the "no interest" line; see D1)

**Adventure, Xanathar's underlings (5e)**
> "{@creature Xanathar|WDH} relies on underlings for advice, information, and day-to-day oversight of the Xanathar Guild. The following important underlings are described in appendix B:"
> — `sources/adventure-wdh.json:15066`
> "{@creature Nihiloor|WDH}, {@creature mind flayer},"
> — `sources/adventure-wdh.json:15073` (list runs `:15071` to `:15076`)

**Campaign, Guild structure (names Nihiloor's own lair)**
> "Xanathar rules the Guild from a lair below Skullport, and very few members have access to it (*Dragon Heist*, 5e). Its lieutenants manage the Guild's day-to-day operations (*Dragon Heist*, 5e). Ahmaergo, a shield dwarf, is the most influential member after the beholder, and Nar'l Xibrindas is its only advisor. Nihiloor has carved out a lair of its own inside the beholder's lair, Noska Ur'gray is the chief enforcer and Thorvin Twinbeard is the chief engineer and trapsmith. Ott Steeltoes keeps Sylgar, and Gorath and Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)."
> — `campaign/setting/organizations/08-xanathars-guild.md:43`

**Adventure, Nihiloor's own lair (5e; inset "Replacing the Mind Flayer", page 110)**
> "{@creature Nihiloor|WDH} the mind flayer has carved out its own lair within {@creature Xanathar|WDH}'s lair (areas X23 through X26). If {@creature Nihiloor|WDH} is killed earlier in the adventure, replace it with a mind flayer named Qrr'zarq."
> — `sources/adventure-wdh.json:17802`

**Campaign, ranks ladder (Nihiloor is not placed on it)**
> "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e). The Guild is made up of some of Waterdeep's most disreputable folk and of monsters, whom the beholder forces into service or draws in with treasure, food or power (*Dragon Heist*, 5e). Goblins and bugbears work for it, and Nihiloor has infected some of them with intellect devourers (Forgotten Realms Wiki, *Xanathar's Thieves' Guild*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:45` (the "infected" clause is stronger than the wiki's; see D7)

**Wiki, Xanathar Guild page (pass 5 bundle), goblins and bugbears (citation WotMM p.13, edition not printed)**
> "The Xanathar Guild was also known to employ a number of [[goblin]]s and [[bugbear]]s, some of whom were infected with [[intellect devourer]]s, presumably by Nihiloor.<ref name="WDotMM-p13">{{Cite book/Waterdeep: Dungeon of the Mad Mage|13}}</ref>"
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:106`

**Campaign, Guild Key Members line on rank and tenure**: none. The page's Persona is the only source of "a status no other Guild member holds" (see A2 rank line in section C, row 8b).

### A3. What it does: devourers, hosts and the brine

**Campaign, Guild informants (5e citation)**
> "**Informants.** The Guild's informants work in every ward. Nihiloor breeds intellect devourers and sets them loose in the sewers, and each one takes the first humanoid it meets and uses its victim as a puppet to spy on the city. Some devourers hunt a particular kind of target, such as a member of the Watch or the Guard, and some capture Waterdhavians for the slave and ransom trade (*Dragon Heist*, 5e). Xanathar also dreams gazers into being, sends them to follow and spy on its own members, and sees through a stuffed beholder in the window of the Old Xoblob Shop (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:75`

**Adventure, captives fed to Nihiloor (inset X25 "Unhappy Meals", page 111)**
> "The Xanathar Guild captures homeless Waterdavians and brings them here for {@creature Nihiloor|WDH} to feed on. After devouring their brains, the mind flayer gives their corpses to his kuo-toa thralls to eat."
> — `sources/adventure-wdh.json:17827`

**Adventure, the brine (area X26, page 111)**
> "The brine is a magical substance that radiates an aura of transmutation magic under the scrutiny of a {@spell detect magic} spell. {@creature Nihiloor|WDH} uses it to transform humanoid brains into intellect devourers. The process is far from perfect. A full 90 percent of the brains left in the brine rot and die, while the remaining 10 percent transform after marinating for {@dice 1d4 + 1} days."
> — `sources/adventure-wdh.json:17847`

> "In the middle of the area is a 10-foot-diameter, 2-foot-deep circular pool containing luminous green brine. Swimming in the brine are four {@creature intellect devourer||intellect devourers}. If it has not been encountered and defeated elsewhere, {@creature Nihiloor|WDH} the {@creature mind flayer} (see {@adventure appendix B|WDH|12}) is standing in the pool with the intellect devourers."
> — `sources/adventure-wdh.json:17843`

**Adventure, the prison for hosts (area X27, page 111)**
> "{@creature Nihiloor|WDH} the mind flayer uses this prison to confine potential hosts for his brood of intellect devourers. Captured characters might find themselves incarcerated here until they can be made into hosts. The area contains the following features:"
> — `sources/adventure-wdh.json:17857`

**Adventure, the Force Grey hook (5th-level mission, adventure text)**
> "\"{@creature Xanathar|WDH} is using intellect devourers to take control of Waterdavians in key positions throughout the city. We must deal with this problem at once. Infiltrate {@creature Xanathar|WDH}'s lair and destroy whatever is responsible for creating these creatures.\""
> — `sources/adventure-wdh.json:3811`

**Alexandrian, Lair PDF, questioning the henchmen (printed p.91 [PDF p.9]) [image transcription]**
> "Virtually all of the Xanatharians steer clear of the mind flayer's demesne (X23-X27). It's not unheard of for even loyal members of the Guild to disappear over there. As a result, they don't know much about the layout or what's there (although they know prisoners are delivered over there). Conniving Guild members might try to convince the PCs that this is where whatever it is they're looking for is located (with the expectation that Nihiloor will eat their brains)."
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91 [PDF p.9] [image transcription]

**Campaign, Force Grey brief on the pool (quest text, day-one facts only)**
> "Nihiloor breeds Occupying Devourers in a stone basin in his wing of the lair, and he has used them to put hosts into the Watch and the city's offices. Meloon Wardragon was one of them, and the records in the wing list the others. A drow is strapped in a chair beside the basin, waiting for the next devourer."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/overview.md:21`

**Campaign, Harper design note on the custom devourer**
> "The 2024 intellect devourer eats the host's brain and only *Wish* restores it. Both facts were wrong for a rescue, so the mission uses the custom **Occupying Devourer** from the **Harpers Mechanics Reference**. It keeps the brain alive, and the party forces it out through Hold, Breaks and Strain, by ward, by magic or by an anchor."
> — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/design-notes.md:9`

### A4. The panopticus

**Adventure, the five dwarves (area X16 entry "Dwarves", page 106)**
> "The five {@creature Panopticus Wizard|wdh|tattooed dwarves} operate {@creature Xanathar|WDH}'s \"panopticus\" magical surveillance system. They fight only in self-defense. They are {@creature apprentice wizard|VGM|apprentice wizards} (see {@adventure appendix B|WDH|12}), with these changes:"
> — `sources/adventure-wdh.json:17499`
> "{@creature Nihiloor|WDH} the mind flayer has psychically and surgically altered the dwarves so that they sleep with one eye open and half their brains asleep at any time."
> — `sources/adventure-wdh.json:17505`

**Campaign, the surveillance network as Nihiloor's gift (structure doc)**
> "The panopticus surveillance network — five ghostly beholder eyestalks wired through enchanted crystal to a monitoring station at X16 — was Nihiloor's gift to Xanathar three years ago. The beholder believes the network serves its paranoia. Nihiloor built a structural back door into the control array from the beginning."
> — `campaign/structure/arc-f-xanathars-lair.md:15`

**Campaign, the blind spot in the Recreation Hall (structure doc; quest-time routing applies to the lair entry only)**
> "*Safe Zone: Area X28.* The Guild Recreation Hall has no panopticus sensor. Nihiloor built this blind spot intentionally; rank-and-file Guild members speak more freely without surveillance, and their unguarded conversations are useful intelligence. The party can use X28 as a staging area once they reach it: rest, plan, treat wounds, or establish a rendezvous. Guild members here are occupied with card games and arguments and will not scrutinize strangers with a plausible story."
> — `campaign/structure/arc-f-xanathars-lair.md:79`

**Wiki, panopticus (pass 5 bundle; citation WDH-p106, edition not printed)**
> "Some of the more unusual members of the guild in the late 1400s DR were known as the panopticus, a group of five [[shield dwarf|shield dwarves]] that had been modified by the [[mind flayer]] [[Nihiloor]] to operate and serve as a surveillance system for the [[Zushaxx|Xanathar]].<ref name="WDH-p106">{{Cite book/Waterdeep: Dragon Heist|106}}</ref>"
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:104`

### A5. Its lair: the wing and its rooms

**Campaign, Nihiloor's Domain (structure doc; the campaign's range is X23 to X27)**
> "*Nihiloor's Domain (Areas X23–X27).* The secondary objective zone. Rank-and-file avoid this area by standing practice — guards assigned here request reassignment within weeks, citing nightmares and intrusive thoughts. The dread is real: Nihiloor has allowed it to accumulate because it discourages investigation."
> — `campaign/structure/arc-f-xanathars-lair.md:173`
> "- **X23 — Competitive Intelligence Files.** Nihiloor's research on all four villain factions, assembled as preparation for an eventual play for true control. The Manshoon section is the most detailed: intercepted Zhentarim communications, field reports on Kolat Towers' external security, a partial lieutenant roster, and a ground-level map of Kolat Towers. This is one of three clue paths to **Kolat Towers**."
> — `campaign/structure/arc-f-xanathars-lair.md:175`
> "- **X24 — The Infiltration.** Placement records for four intellect devourers inserted into Watch and civic administration positions, with two additional placements pending. Each record: host name, position, insertion date, behavioral integration notes."
> — `campaign/structure/arc-f-xanathars-lair.md:176`
> "- **X25 — The Experiments.** Research notes and twelve living specimens at various modification stages. The notes describe a process for creating psionic relay organisms. Reading them fully requires a DC 13 Wisdom saving throw or the reader gains one level of Exhaustion from the psychological impact."
> — `campaign/structure/arc-f-xanathars-lair.md:177`
> "- **X26 — The Puppet.** A psionic relay device, currently active, maintaining a Dominate Monster effect on a psychic signature that matches Xanathar's. Detailed notes track behavioral corrections applied over four months: which tactical decisions were changed, which Guild members were elevated or removed at Nihiloor's direction, and the long-term strategic repositioning of the Guild toward Nihiloor's actual goals. The beholder who rules Xanathar's Guild does not rule Xanathar's Guild. Every Xanathar decision the party has encountered was Nihiloor's decision."
> — `campaign/structure/arc-f-xanathars-lair.md:178`

**Adventure, the wing's areas (5e, page 110-111; names differ from the campaign; see D5)**
> "X23. Antechamber of Madness" — `sources/adventure-wdh.json:17709`
> "X24. Extraction Chamber" — `sources/adventure-wdh.json:17762`
> "X25. Food for Thought" — `sources/adventure-wdh.json:17808`
> "X26. Devourer Spawning Pool" — `sources/adventure-wdh.json:17835`
> "X27. Prison" — `sources/adventure-wdh.json:17853`

**Campaign, X23 to X26 as the Force Grey wing (quest text; room contents for the mission)**
> "Nihiloor's wing is X23 to X26 of **Xanathar's Lair**, and this mission adds three things to the rooms that quest already describes. The pool and the captive sit in X25 beside the twelve specimens, and the placement records lie in X24."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/overview.md:25` (the actual sentence begins "The wing is area X23 to X26 of **Xanathar's Lair**, ..." as printed on that line; quoted from the tool output, see D5 note)

**Campaign, the wing's X23 guards and the wing's thralls (quest text)**
> "The thrall in X23 is an enthralled Guild soldier who wakes only for Nihiloor, the pet or an alarm, so a character who walks past it needs no check."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:39`

### A6. The hosts it has taken (day-one)

**Meloon Wardragon (Force Grey; day-one occupation)**
> "Meloon Wardragon is a Force Grey veteran and a favourite regular at the Yawning Portal. After the Field of Triumph, an Occupying Devourer from Nihiloor's brood took his skull, about three tendays before the watch begins. It keeps his brain alive and walked him into the Xanathar's lair twice before the watch. Its telepathy reaches only 60 feet, so it reports through a Guild-paid dockhand who meets Meloon at the end of each tenday."
> — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:21` (quest file; the occupation predates Ches 1 by its own wording; the Meloon page carries the same date, see below)
> "- **Affiliation:** Force Grey (occupied by a Xanathar's Guild intellect devourer after the Field of Triumph, about three tendays before the first day of the watch)"
> — `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:6`

**Orvyn Dall (Watch appeals clerk; day-one occupation)**
> "A devourer from Nihiloor's brood has ridden Orvyn for seven tendays. It steers which appeals reach which magistrate, and Orvyn is aware and cannot act or speak. If he dies, if Brenna calls the Watch or if a patrol sees the extraction, the Watch reviews the magistracy for 14 days."
> — `campaign/gazetteer/waterdeep/trades-ward.md:99` (setting page; present tense)
> "- **Xanathar's Guild** (enemy): ... Nihiloor's devourers ride Watch members, including a clerk named Orvyn Dall (**Nihiloor**)."
> — see the full bullet at `campaign/setting/organizations/08-xanathars-guild.md:95`:
> "- **The Open Lord's Watch** (enemy, tolerated): The Watch is called to the Guild's brawls with the Zhentarim in the Dock Ward and leaves the sewer lair alone, and Captain Staget reasons that the two may as well destroy each other (**The Open Lord's Watch**; *Dragon Heist*, 5e). Nihiloor's devourers ride Watch members, including a clerk named Orvyn Dall (**Nihiloor**)."
> — `campaign/setting/organizations/08-xanathars-guild.md:95`
> "Seven tendays ago a devourer from Nihiloor's brood took Orvyn Dall, an appeals clerk in the Trades Ward district magistracy."
> — `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/overview.md:21` (quest file, pre-mission phrasing)
> "- Orvyn is one of four Watch and civic hosts that Nihiloor placed, and two more were pending. If **Pool Destroyed** is marked, no new hosts arrive."
> — `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/overview.md:27`

**Corene Wyldath (Harper deep-cover agent; day-one occupation)**
> "Corene has worked inside the Dock Ward operation of Xanathar's Guild for four months. Three weeks ago one of Nihiloor's devourers took her, and it has used her since to learn who the Harpers are."
> — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/overview.md:21`
> "- **The Harpers** (enemy): The Harpers keep Thorvin Twinbeard inside the lair as a paid informant, and Corene Wyldath works in the Guild's Dock Ward operation under a false name (**The Harpers**; **Corene Wyldath**). Xanathar has begun to question Thorvin's loyalty and has set a gazer to watch him (*Dragon Heist*, 5e). One of Nihiloor's intellect devourers rides Corene, and she is one of three Harpers it has taken."
> — `campaign/setting/organizations/08-xanathars-guild.md:85`
> "- **Xanathar's Guild (enemy):** The Harpers keep Thorvin inside the lair and Corene in the Dock Ward operation, and the wiki says they move against thieves' guilds. An intellect devourer rides Corene, and she is one of three Harpers Nihiloor has taken."
> — `campaign/setting/organizations/01-harpers.md:89`
> "- **Corene Wyldath** — Halfling Harper deep-cover agent embedded in the Dock Ward operation of Xanathar's Guild; compromised by an intellect devourer three weeks ago, after four months under cover as Halla Ironstave. See the **Corene Wyldath** page in Notable Figures."
> — `campaign/setting/organizations/01-harpers.md:102`
> "Corene is a Harper deep-cover agent who has worked inside Xanathar's Guild's Dock Ward operation for four months. One of Nihiloor's custom Occupying Devourers rides her. She is aware and cannot act, and she can be freed if the devourer is forced out. The **Trades Ward** page has the bench where she sits."
> — `campaign/gazetteer/waterdeep/dock-ward.md:166`

**Count of Harper hosts (Factions Guide; the "three" count)**
> "Mirt wants Nihiloor dead — the mind flayer's intellect devourers have touched three Harper assets. He offers tactical support for the Xanathar lair heist if the party commits to eliminating Nihiloor. Nihiloor always escapes, so the support rests on a real attempt, not a kill."
> — `campaign/guides/factions/02-harpers.md:31`

### A7. Possessions and tools

**Adventure, the stone orb (Finding Floon sewer hideout; 5e)**
> "{@creature Nihiloor|WDH} carries a 3-inch-diameter stone orb carved to resemble an eyeball, similar to what one might see at the end of a beholder's eyestalk. This stone eye is the key to activating the magic portal in {@area Q11|089}. The mind flayer uses it to return to {@creature Xanathar|WDH}'s lair (described in chapter 5). It uses {@spell dominate monster} to control someone who gets in its way and turns any such individuals against their allies."
> — `sources/adventure-wdh.json:2815`

**Campaign, the portal activation (Q11, sewer hideout; quest location, day-one object)**
> "**Activation:** Nihiloor's 3-inch stone orb, when pressed into the indentation, opens an opaque black doorway 8 feet tall and 4 feet wide in the south wall. The portal leads to area X22 of Xanathar's lair. Any creature that steps through appears in X22. It remains open for 1 minute after the orb is removed, then closes. It can't be held open by other means."
> — `campaign/locations/xanathar-sewer-hideout/q11-escape-portal.md:11`

**Adventure, the shackle key (area X24, 5e)**
> "{@creature Nihiloor|WDH} has a key that unlocks the chair's shackles. A character can unlock each shackle with a successful {@dc 15} Dexterity check using thieves' tools, and a creature shackled to the chair can slip free of these bonds with a successful {@dc 25} Dexterity (Sleight of Hand) check."
> — `sources/adventure-wdh.json:17781`

**Adventure, the pet (Finding Floon sewer hideout, 5e)**
> "The tentacled creature is {@creature Nihiloor|WDH} (see {@adventure appendix B|WDH|12}), a {@creature mind flayer} that is caressing an {@creature intellect devourer}."
> — `sources/adventure-wdh.json:2814` (the scene is a Finding Floon event; see E2)

### A8. Relations with other named figures

**Meloon Wardragon (adventure, the devourer's maker)**
> "The intellect devourer that inhabits Meloon's skull was bred by {@creature Nihiloor|WDH}, a mind flayer in {@creature Xanathar|WDH}'s employ. It knows everything Meloon knew, and Meloon behaves much as he did before his descent into Undermountain. He hangs out at the Yawning Portal, tries to bond with adventurers, and offers a helping hand whenever doing so feels appropriate. The intellect devourer's primary goals are to steer adventurers away from Undermountain and get them to undertake quests that further the aims of {@creature Xanathar|WDH}. Such quests usually involve the eradication of {@creature Xanathar|WDH}'s enemies, and Meloon is all too eager to fight alongside those who fall for his ruse."
> — `sources/adventure-wdh.json:32257` (for the time of the occupation, see D8)

**Zaibon Kyszalt, a drow captive in X24 (adventure, 5e)**
> "The drow, Zaibon Kyszalt, was captured in Skullport and brought here for interrogation. His superior, Raelyn Auvryndar, was also captured and is confined in {@area X7|27e}. Zaibon wants to free her and escape into Undermountain, where House Auvryndar has outposts."
> — `sources/adventure-wdh.json:17780`
> "The mind flayer has telepathically interrogated Zaibon and learned about a House Auvryndar plot to conquer Skullport, as well as mounting tensions between the drow houses of Auvryndar and Freth. The mind flayer is getting ready to implant an intellect devourer in Zaibon's skull, then use him to undermine the drow plot and foment war between the drow houses. (Were Zaibon less useful, the mind flayer would have extracted his brain and turned it into an intellect devourer instead.) Zaibon knows nothing of the fate that awaits him."
> — `sources/adventure-wdh.json:17782`
> "Dragon Heist holds two of its drow in Xanathar's lair, Zaibon Kyszalt, captured in Skullport, and his superior Raelyn Auvryndar, and **Nihiloor** has learned of the house's plot to conquer the town."
> — `campaign/setting/geography/undermountain-and-skullport.md:92` (the bullet "House Auvryndar" in the setting page; present tense)

**Grum'shar, Q07 boss (Finding Floon sewer hideout; 5e)**
> "The boss of this hideout is a half-orc named {@creature Grum'shar|wdh}. When the characters arrive, {@creature Grum'shar|WDH} is interrogating {@creature Floon Blagmaar|WDH} in {@area Q7|081}. His display of torture techniques is a ploy to impress his other guest: a mind flayer named {@creature Nihiloor|WDH} (see {@adventure appendix B|WDH|12})."
> — `sources/adventure-wdh.json:2712`

**Thorvin Twinbeard (Harper informant inside the lair; quest-time routing)**
> "If the gazer is destroyed (13 HP, AC 13), Thorvin speaks openly for the first time. His relief is immediate and genuine. He confirms what the party may have begun to suspect: Nihiloor's domain (X23–X27) contains evidence that would change everything the party thinks they know about who has been running Xanathar's Guild."
> — `campaign/structure/arc-f-xanathars-lair.md:95` (quest-time; routed to Xanathar's Lair)

**The Harpers (Mirt)**
> "- **Xanathar's Lair** | Mirt wants Nihiloor dead" — see the full row at `campaign/guides/factions/02-harpers.md:31` (quoted in A6)
> "Full intelligence briefing. If Xanathar outposts were hit, Mirt asks specifically about Nihiloor references — the Harper file on the mind flayer is extensive, and any new document strengthens the case for Watch action."
> — `campaign/structure/arc-e-faction-outposts.md:369` (Mirt's Faction Outposts briefing; quest-time routing)

**The Order of the Gauntlet (Savra)**
> "- **Xanathar's Guild (enemy):** The Order counts the Guild's use of intellect devourers and enslaved creatures as an abomination (Alexandrian remix, Appendix B). Guild dealers work the Field Ward, where the Order fills part of the gap the Watch leaves (**Field Ward**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:80`
> "| **Xanathar's Lair** | The Guild's use of intellect devourers is an abomination in Savra's theological framework. She asks the party to put Nihiloor down for good. Nihiloor always escapes, so she asks for the attempt and not the kill."
> — `campaign/guides/factions/05-order-of-the-gauntlet.md:31` (quoted through the first two sentences of the row; the row continues with the Whitehawk lair support)

**Force Grey (Vajra)**
> "Grand Game goal: The vault gold to the treasury. The pool, the placement records and the hosts already walking the city dealt with. The Splinter's arcane operations dismantled. The Stone of Golorr studied and understood before it's sealed away again. These are her priorities in order. Nihiloor always escapes the party, so she plans around him and not around his death. Her concern is which outcome leaves Waterdeep standing. The rest is scoring."
> — `campaign/guides/factions/06-force-grey.md:23`

**Dobb Ketterly (Guild courier to Nihiloor; quest-time routing)**
> "On Day 8 or 9 a Guild dockhand named Dobb Ketterly leaves word for Meloon, and the party can follow him home. On Day 10 at dusk he sits at Meloon's table and carries the report to Nihiloor."
> — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:43`

**Soluun Xibrindas (in the wing chair; quest-time routing)**
> "Soluun Xibrindas sits in the chair instead of Zaibon. He sold the Guild's divers the *Scarlet Marpenoth*'s berth, and once the deal was done the Guild seized him, because Nihiloor wants a host who knows how the company works."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:124`

**Captain Hyustus Staget (a Watch captain in X27 in the adventure; see D9)**
> "Imprisoned in the westernmost cell along the north wall is Hyustus Staget, a captain of the City Watch whom the characters have met (see \"The Watch Arrives\"). He was kidnapped while off duty and is without his armor and weapons. If Hyustus has died for whatever reason, replace him with a female human Watch officer named Cressa Galavarco (LG female Tethyrian {@creature veteran} with no armor or weapons). Whoever is here has a date with an intellect devourer."
> — `sources/adventure-wdh.json:17873`

**Davil Starsong (Doom Raiders; day-one claim on another page)**
> "**Relationships.** Davil is the cell leader of the Doom Raiders (Waterdeep Zhentarim), the faction contact for Zhentarim-aligned PCs, a permanent resident at the Yawning Portal (second floor business room, third floor suite), a colleague of Istrid, Tashlyn, Ziraj, and the traitor Skeemo Weirdbottle, and the unknowing target of Nihiloor's intellect devourer, with Meloon watching him and waiting for a clean opportunity to kill him without witnesses."
> — `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:25`

**Nar'l Xibrindas and Ahmaergo, Noska, Thorvin**: no source names Nihiloor in a relationship with Nar'l, Ahmaergo or Noska. Searches are listed under Not found.

**Other mind flayers (wiki, 1491 DR; a different mind flayer, not Nihiloor)**
> "In [[1491 DR]], the Xanathar, in cahoots with the [[mind flayer]] [[Suthool]] and the agent of [[Asmodeus]] [[Belvarra Bowmantle]], supported the plots of the [[Masked Lord]] [[Braethan Cazondur]] in order to distract the [[City Watch (Waterdeep)|City Watch]] and the [[Open Lord]]s from its operation in [[Skullport]] and to gain power in order to expel the [[Zhentarim]] from [[Waterdeep]].<ref name=":0">{{Cite book/Death Masks|180-181}}</ref>"
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:484` (Death Masks pp.180-181; edition not printed)

### A9. The domination of Xanathar (facts only; both sides are in D1)

- Campaign claim: "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know." (page, row 8c in section C)
- Campaign date, derived: "- **About Uktar 1491 DR, Nihiloor.** Nihiloor begins to dominate Xanathar's mind, four months before Ches 1, 1492 DR by its Notable Figures page, and Xanathar does not know (**Nihiloor**). The month is derived by counting back from Ches 1." — `campaign/setting/organizations/08-xanathars-guild.md:24`
- No published-adventure line says Nihiloor controls Xanathar. The search (section Not found) found only the spell use at `sources/adventure-wdh.json:2815`.

### A10. Faith and power source

No source gives Nihiloor a god, a rite or a shrine.

**Campaign, Ilsensine (setting page; the page says no line ties Nihiloor to it)**
> "- **Campaign ties:** One fresco in the **Vault of Dragons** structure document names Ilsensine. Nihiloor and the Undermountain mind flayers are the nearest, and no line ties either to Ilsensine. The GM Notes quote all three."
> — `campaign/setting/deities/ilsensine.md:59`
> "- **Never reveal:** That Nihiloor has dominated Xanathar for the last four months, or that intellect devourers occupy Waterdavians such as Meloon Wardragon, before the party's own evidence supports it. A player who asks about the Great Brain gets the Overview."
> — `campaign/setting/deities/ilsensine.md:60`

### A11. How long in post

- Wiki: "in the late 15{{th}} century [[DR]]" (`Nihiloor.txt:61`, see A1).
- Campaign: "four months" of domination (page row 8c; `08-xanathars-guild.md:24`; `08-xanathars-guild.md:103`).
- Campaign, the panopticus gift: "three years ago" (`campaign/structure/arc-f-xanathars-lair.md:15`).
- Campaign, the devourer placements in the Watch and civic posts: "with two additional placements pending" (`arc-f-xanathars-lair.md:176`). No dates for the placements.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page, summary line: "*Mind flayer, lawful evil, it/its*. Stat block: **Mind Flayer**." — `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:5`
- Guild page: "- **Nihiloor** (DH p. 213) — Mind flayer, lawful evil. Officially handles Xanathar's most sensitive intelligence operations." — `campaign/setting/organizations/08-xanathars-guild.md:103`
- Wiki: "| alignment5e    = [[Lawful evil]]" — `Nihiloor.txt:56`, citation "<ref name="WDH5e-p212" /><ref name="MM5e-p222">{{Cite book/Monster Manual 5th edition|222}}</ref>" at `Nihiloor.txt:59` (5e).
- Adventure: the Nihiloor entry has no alignment line. Its only game-statistics line is "{@creature Nihiloor|WDH} is a {@creature mind flayer}." — `sources/adventure-wdh.json:32361`.

**Species**
- Page: "mind flayer" (summary line 5). Adventure: "{@creature Nihiloor|WDH} is a {@creature mind flayer}." — `sources/adventure-wdh.json:32361`. Wiki: "| race           = [[Mind flayer]]<ref name="WDH5e-p212" />" — `Nihiloor.txt:13`.

**Pronouns** (the page says it/its; the sources are split; see D2)
- Page: "*Mind flayer, lawful evil, it/its*." — `04-nihiloor.md:5`
- Voice profile: "It speaks telepathically, a cold, clear, sexless presence inside the listener's head, perfectly calm, and accompanied by a faint pressure behind the eyes." — `.claude/skills/character-voices/voices/xanathars-guild.md:68`
- Adventure, "it": "The mind flayer uses it to return to {@creature Xanathar|WDH}'s lair" — `sources/adventure-wdh.json:2815`; "It has no interest in supplanting the beholder" — `:32354`.
- Adventure, "his": "After devouring their brains, the mind flayer gives their corpses to his kuo-toa thralls to eat." — `sources/adventure-wdh.json:17827`; "the mind flayer uses this prison ... for his brood of intellect devourers" — `:17857`.
- Campaign, quest files, "it": "The moment it sees the party, it rises, sets the intellect devourer down (now loose and hostile), and glides toward the western double door, heading for Q11." — `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:69`; "On the party's arrival: The moment Nihiloor sees the party, it rises." — `campaign/locations/xanathar-sewer-hideout/q07-boss-chamber.md:21`
- Campaign, quest files, "he": "By default Nihiloor is in X26 at the Puppet device, with the pet on the Pool's rim. When the wing wakes, he comes into X25 with the thralls behind him." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:139`; "On his way out he sacrifices the pet, wakes the Guild at the wing door and enters the tunnel toward X4." — `m04-destroy-the-intellect-factory/overview.md:43`; "He's a mind flayer who has been using this city as a fucking hatchery, but he doesn't stand and die for his work." — `m04-destroy-the-intellect-factory/ev-01-the-brief.md:69` (a Vajra answer to a player question; dialogue)
- Appendix C: "It does not want to fight. It wants to leave." — `sources/Appendix_C_-_Player_Faction_Missions.md:1898`

**Stat block**
- Page: "Stat block: **Mind Flayer**." — `04-nihiloor.md:5`
- Adventure: the entry heading "Mind Flayer" sits in the X26 description: `"name": "Mind Flayer",` page 111, `"id": "2ad"` — `sources/adventure-wdh.json:17787`; the text is "If the characters haven't already dealt with {@creature Nihiloor|WDH}, the mind flayer interrupts as they interact with Zaibon, entering from {@area X26|2b1} with an {@creature intellect devourer} in its hands." (`:17791`).
- Appendix C: "**Nihiloor** (**Mind Flayer**, 2024 *Monster Manual*). It does not want to fight." — `sources/Appendix_C_-_Player_Faction_Missions.md:1898`; tactical note: "Nihiloor** (2024 *Monster Manual*): AC 15, HP 71, Speed 30 ft." — `:1906`
- Force Grey mechanics: "Nihiloor uses the boss block in section 4.1 of the **Force Grey Mechanics Reference**. The pet is the **Occupying Devourer** from section 5.1 of the **Harpers Mechanics Reference**, and the thralls are **Tough**. Use the row for the party's size." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:157`
- Alexandrian Lair stat reference (printed p.91 [PDF p.9]) [image transcription]: the list covers Ahmaergo, Flutterfoot Zipswiggle, Thorvin Twinbeard, N'arl Xibrindas, Noska Ur'gray and Ott Steeltoes. It has no Nihiloor line.
- Wiki: "| challenge5e    = 7" — `Nihiloor.txt:57` (5e).
- Campaign, CR in the sewer hideout: "Nihiloor (mind flayer, CR 7) flees on party arrival — doesn't fight except to dominate a creature blocking its escape path." — `campaign/locations/xanathar-sewer-hideout/area-overview.md:55`

**Page number**
- Page-citation conflict: adventure entry "page": 212 (`sources/adventure-wdh.json:32340`); Guild page "(DH p. 213)" (`08-xanathars-guild.md:103`); wiki "WDH5e-p212" (`Nihiloor.txt:61`). See D3.

---

## C. Every sentence on the current page

Status key: "Day-one" = no quest gate needed. "Quest-time" = narrates a mission, a rescue or a quest event. "Contested" = depends on the domination question in D1.

| Row | Line | Exact sentence(s) from the page | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Mind flayer, lawful evil, it/its*. Stat block: **Mind Flayer**." | Day-one. Pronouns split (D2). | `08-xanathars-guild.md:103`; `adventure-wdh.json:32361`; `Nihiloor.txt:56` |
| 2 | L6 | "**Affiliation:** Xanathar's Guild" | Day-one | `adventure-wdh.json:32353` ("works for Xanathar"); `08-xanathars-guild.md:103` |
| 3 | L7 | "**Featured in:** **Finding Floon**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **The Trouble with Meloon**, **Destroy the Intellect Factory**" | Quest references. "Faction Outposts" has no Nihiloor scene in `arc-e` (its only Nihiloor line is the Mirt briefing, `arc-e-faction-outposts.md:369`) and none in the Faction Outposts PDFs. Route. | See E2 |
| 4 | L11 | "**Resonance.** Nihiloor should inspire visceral horror with its alien otherness, intellectual dread when the party learns how many people it has compromised, and helpless rage at the knowledge that it has bent Xanathar to its will and the beholder has no idea." | Mixed. "alien otherness" has a basis in `adventure-wdh.json:32354` ("alien mind"). "when the party learns how many people it has compromised" is a play reveal. "bent Xanathar to its will and the beholder has no idea" is the contested domination (D1). | `adventure-wdh.json:32354`; D1 |
| 5 | L13 | "**Emotions.** Nihiloor most often feels cold intellectual curiosity, alien satisfaction at its creations, patient derision for non-psionic minds, possessive pride in its intellect devourers, detached amusement at humanoid politics, and a complete absence of anything recognizable as empathy." | Day-one character state; no event. Partly in the voice profile (rows 5 and 6 of profile: "Detached amusement at politics shows as questions about why they bother."). | `xanathars-guild.md:72`; `xanathars-guild.md:75` (profile) |
| 6 | L15 | "**Motivations.** Nihiloor wants to breed and deploy intellect devourers throughout Waterdeep, pursue its own fell schemes independent of Xanathar's goals, and observe the Grand Game from within the shadows where no one looks." | Day-one. "pursue its own fell schemes" is in `adventure-wdh.json:32354`. "independent of Xanathar's goals" is the campaign's domination claim (D1). "observe the Grand Game" has no source (F). | `08-xanathars-guild.md:75` (breeding); `:32354`; D1 |
| 7 | L17 | "**Inspirations.** When playing Nihiloor, channel HAL 9000 (*2001: A Space Odyssey*), Hannibal Lecter (*Silence of the Lambs*), and the Borg Queen (*Star Trek*)." | Not a fact | n/a |
| 8a | L21 | "**Persona.** To the world, Nihiloor is Xanathar's mind flayer operative." | Day-one | `adventure-wdh.json:32353` |
| 8b | L21 | "To Xanathar, it is a trusted mind flayer operative with a status no other Guild member holds." | Day-one claim, campaign only. Villains page gives "Trusted intelligence gatherer; Xanathar grants it unusual autonomy" (`xanathar.md:49`). Rank in the Guild has no published source (F). | `campaign/setting/villains/xanathar.md:49`; D1 |
| 8c | L21 | "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know." | Contested (D1). Campaign-only; no published line. | `08-xanathars-guild.md:103`; `xanathar.md:55`; `arc-f-xanathars-lair.md:408`; D1 |
| 8d | L21 | "It breeds intellect devourers, sets them loose in the sewers, and uses them to occupy Waterdavians, who walk the city with their own brains intact and a devourer steering them." | Day-one. "brains intact" is the campaign's custom devourer (`harpers/m05 design-notes.md:9`); the published brine transforms brains (`adventure-wdh.json:17847`). See D7. | `adventure-wdh.json:32353`; `08-xanathars-guild.md:75` |
| 8e | L21 | "Its methods leave little behind for PCs to question." | No source (design sentence). | F |
| 8f | L21 | "Meloon Wardragon and Watch clerk Orvyn Dall are among its current hosts." | Day-one per `trades-ward.md:99`, `independents-allies/05-meloon-wardragon.md:6` and `m05 overview.md:21`. Meloon's date conflicts with the adventure (D8). | `trades-ward.md:99`; `08-xanathars-guild.md:95` |
| 9a | L23 | "In a fight, Nihiloor would use Dominate Monster on the most dangerous combatant, command its intellect devourers to attack, and retreat when threatened." | Day-one combat behaviour, but "retreat" conflicts with the X26 text (D4). | `adventure-wdh.json:2815` ("dominate monster"); `:17848` ("make their stand here"); Appendix C `:1898` ("Dominate Monster if cornered") |
| 9b | L23 | "In **Destroy the Intellect Factory** it always escapes toward the rest of the lair and is never killed there." | Quest-time. Routed to the Force Grey mission. | `m04 ev-02-nihiloors-wing.md:18` ("he is never killed here, so **Nihiloor Fled** is always marked"); `06-force-grey.md:73` |
| 9c | L23 | "It caresses an intellect devourer like a pet as it glides away." | Quest-time (Finding Floon, Q07 scene). | `ev-04-xanathar-sewer-hideout.md:67`, `:69`; `adventure-wdh.json:2814` |
| 10a | L25 | "**Relationships.** Nihiloor is the intelligence and infiltration specialist of Xanathar's Guild," | Day-one. "intelligence" is sourced at `08-xanathars-guild.md:103` ("Officially handles Xanathar's most sensitive intelligence operations"). "infiltration specialist" has no source line; the Guild's project is "The Infiltration" (`08-xanathars-guild.md:103`). | `08-xanathars-guild.md:103`; `xanathar.md:49` |
| 10b | L25 | "the creator of the intellect devourer that occupies Meloon Wardragon," | Day-one. | `adventure-wdh.json:32257` ("was bred by"); `08-xanathars-guild.md:89` |
| 10c | L25 | "and a mind flayer that has dominated Xanathar's mind for the last four months in a Guild where even a hint of that would get anyone else disintegrated." | Domination is contested (D1). "disintegrated" has no source: the only disintegration in the published text is Ott's plea at `adventure-wdh.json:17621`, and no source gives the Guild a rule of disintegrating members (F). | D1; F |
| 11a | L29 | "Nihiloor is the intelligence operative of Xanathar's Guild — a mind flayer who moves through the lair with unsettling calm, treating every conversation as an opportunity for study." | First clause day-one (`08-xanathars-guild.md:103`). "moves through the lair with unsettling calm, treating every conversation as an opportunity for study" has no source line. Voice profile is the nearest: "It asks questions as though taking notes" (`xanathars-guild.md:69`). | F |
| 11b | L29 | "The Guild's other members give it wide berth." | Partly sourced: "Virtually all of the Xanatharians steer clear of the mind flayer's demesne (X23-X27)." `Lair PDF printed p.91 [PDF p.9]` [image transcription]. | Lair PDF p.91 |

**Quest-time sentences on the current page (for the drafter's Routed list):** row 3 (Featured in), row 9b (Destroy the Intellect Factory), row 9c (the Q07 caress), and the partly quest-time row 4 ("when the party learns"). Row 8c and 10c are contested by D1, not quest-time.

### C2. Voice profile (`.claude/skills/character-voices/voices/xanathars-guild.md`, lines 65 to 79), quoted in full

> "### Nihiloor
> *A mind flayer that speaks only into your mind: cool, curious, and utterly without warmth.*
>
> - **Sound:** No spoken voice. It speaks telepathically, a cold, clear, sexless presence inside the listener's head, perfectly calm, and accompanied by a faint pressure behind the eyes.
> - **Sentence shape:** Precise, complete, clinical sentences. It asks questions as though taking notes, and never uses a contraction or a filler.
> - **Word choice:** Scientific and possessive: "specimen", "vessel", "cultivation", "adequate". It calls humanoids by function ("the carrier", "the clerk"). Its intellect devourers are "my children".
> - **Swearing:** *Never · Plain · n/a.* Profanity is a humanoid noise it finds mildly interesting.
> - **Personality in speech:** Cold curiosity and derision. It considers the party interesting specimens. Detached amusement at politics shows as questions about why they bother.
> - **Quirks:** It answers questions the listener only thought of. It pauses mid-conversation as if listening to something else. It remarks on the listener's brain.
> - **Signature phrases:** "Fascinating." / "Your mind is adequate." / "You will be of use."
> - **Never:** It never shows fear, never raises its "voice", and never explains its plans.
> - **Sample lines:**
>   - *Greeting (telepathic):* "You are frightened. That is appropriate. Come closer, I wish to see how you think."
>   - *Business:* "The beholder's gold is irrelevant. I am cultivating something more interesting. You will be of use."
>   - *Under pressure:* "This vessel is damaged. I will make another." (and it's gone)"

Voice notes for the drafter:
- Quest-time clauses in the profile: none found. Each sample line is speech, and none narrates a mission, a rescue or an Event Outcome. "The beholder's gold is irrelevant" touches the vault, a Villains-page goal (`xanathar.md:61`), not a quest event.
- Pronoun in the profile: "sexless presence" (line 68) and "it" throughout. This matches the page's it/its.
- Profile line 70 "Its intellect devourers are 'my children'." has no source line. It is a voice choice.
- Xanathar appears as "the beholder" in the profile's speech, which fits the Ruling 16 rule.

---

## D. Conflicts

### D1. Does Nihiloor dominate Xanathar? (open; both sides quoted; not settled here)

Ruling status: "Left open" on three Grand Game and villain pages, and on a fourth (what-each-faction-knows-at-start). Quoted:

> "- **Left open (brief ruling 14), none settled here:** Nihiloor's domination of Xanathar, Nar'l's tenure, Ott Steeltoes, the "something vast and dreaming" seed and the Doom Raiders and Enclave Trades Ward lines are not touched. The page says only that Nar'l reports to Jarlaxle by *sending* spell."
> — `campaign/setting/the-grand-game/the-grand-game.md:91`

> "- **Left open (brief call 13):** Nihiloor's domination of Xanathar, Nar'l Xibrindas's tenure, Ott Steeltoes, the "something vast and dreaming" seed, and the Doom Raiders and Enclave Trades Ward lines. None is stated on this page."
> — `campaign/setting/villains/manshoon.md:139`

> "- **Calls applied:** Left open per ruling 13: Nar'l's tenure (the page gives none), Nihiloor's domination of Xanathar, Ott Steeltoes and the Doom Raiders and Enclave Trades Ward lines."
> — `campaign/setting/villains/jarlaxle.md:179`

> "- **Left open (brief ruling 14), none settled here:** Nihiloor's domination of Xanathar does not change the Xanathar row. Nar'l's tenure is given as one year in `history/03-bregan-daerthes-long-road.md:161` and differently elsewhere, and the row does not state it."
> — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:101` (the rest of the bullet covers Ott's placement of Eye #1 and the Doom Raiders and Enclave lines)

**Side one: the campaign says it is dominated (the claim)**

> "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know. It breeds intellect devourers, sets them loose in the sewers, and uses them to occupy Waterdavians, who walk the city with their own brains intact and a devourer steering them. Its methods leave little behind for PCs to question. Meloon Wardragon and Watch clerk Orvyn Dall are among its current hosts."
> — `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:21` (the Persona paragraph)

> "- **Nihiloor** (DH p. 213) — Mind flayer, lawful evil. ... (3) **The Puppet** — Nihiloor has been exerting psionic domination over Xanathar itself for the past four months, replacing its strategic decisions while leaving its personality intact. ..."
> — `campaign/setting/organizations/08-xanathars-guild.md:103` (full bullet quoted in A1)

> "- **About Uktar 1491 DR, Nihiloor.** Nihiloor begins to dominate Xanathar's mind, four months before Ches 1, 1492 DR by its Notable Figures page, and Xanathar does not know (**Nihiloor**). The month is derived by counting back from Ches 1."
> — `campaign/setting/organizations/08-xanathars-guild.md:24`

> "> - **The puppet:** Nihiloor has dominated Xanathar for the last four months, and Xanathar does not know. The Xanathar that Waterdeep fears has been Nihiloor's instrument for that time, including the one that killed Manshoon's envoys."
> — `campaign/setting/organizations/08-xanathars-guild.md:129` (Secret callout)

> "- Nihiloor, the mind flayer, has been psionically dominating Xanathar for the last four months. The Xanathar that the party meets, including the one who killed Manshoon's envoys and sent response teams against the party's allies, has been Nihiloor's instrument. Xanathar does not know."
> — `campaign/setting/history/02-the-long-shadow.md:80` (Secret callout)

> "- **Nihiloor** (Notable Figures): full profiles for the Relationships table" — no; use the next line:
> "- Nihiloor has been psionically dominating Xanathar for four months, so some decisions attributed to Xanathar are Nihiloor's (**Xanathar's Lair** structure notes, and the **Xanathar's Guild** organization page)."
> — `campaign/setting/villains/xanathar.md:55`

> "| Nihiloor | Mind flayer operative | Trusted intelligence gatherer; Xanathar grants it unusual autonomy; plant for Mad Mage integration |"
> — `campaign/setting/villains/xanathar.md:49` (the Relationships table, kept verbatim; the Villains page calls it "unusual autonomy", not domination)

> "> - **Conflicts:** The Relationships table (kept verbatim) calls Nihiloor a trusted gatherer with unusual autonomy, but the relationship notes say Nihiloor has dominated Xanathar for four months. `arc-f` line 408 says every decision attributed to the beholder was Nihiloor's, which is not yet reflected here. `04-nihiloor.md` lines 22 and 26 say Nihiloor has no interest in supplanting Xanathar, and the current page does not say it."
> — `campaign/setting/villains/xanathar.md:105` (stale; see E1)

> "The Puppet revelation is the most significant: Xanathar has been Nihiloor's instrument for four months. Every aggressive, paranoid, apparently irrational decision attributed to the beholder in **Faction Outposts** and this quest was Nihiloor's decision. This changes the party's understanding retroactively. The mastermind they've been treating as the main threat was itself controlled by something worse. The real threat from Xanathar's Guild faction was never Xanathar."
> — `campaign/structure/arc-f-xanathars-lair.md:408`

> "Permanent consequences: the Guild is gone as an intelligence resource. ... The party trades a dangerous faction they can understand for an unconstrained Nihiloor operating below the city with no leash."
> — `campaign/structure/arc-f-xanathars-lair.md:113` (the sentence is conditional on the lair's demolition)

> "The party that destroys the lair is trading a faction they understand — paranoid, predictable, with known structures and exploitable NPCs — for an unknown quantity in Nihiloor, who is smarter than Xanathar, does not have Xanathar's attachment to a goldfish, and has been running the Guild in secret for months without anyone noticing."
> — `campaign/structure/arc-f-xanathars-lair.md:400`

> "- **Xanathar** ... " — see `campaign/guides/factions/09-xanathars-guild.md` (no domination line). Not used.

**Side two: the published adventure and the wiki say it has no interest in supplanting Xanathar, and a different mind flayer plans to make Xanathar a thrall**

> "{@creature Nihiloor|WDH} has an alien mind, and it considers itself {@creature Xanathar|WDH}'s equal. It has no interest in supplanting the beholder, however, preferring to operate in the shadows and pursue its own fell schemes."
> — `sources/adventure-wdh.json:32354`

> "It considered itself Xanathar's equal but had no interest in supplanting the [[beholder]].<ref name="WDH5e-p212" />"
> — `Nihiloor.txt:64` (wiki, 5e citation)

> "{@creature Nihiloor|WDH} the mind flayer has carved out its own lair within {@creature Xanathar|WDH}'s lair (areas X23 through X26). If {@creature Nihiloor|WDH} is killed earlier in the adventure, replace it with a mind flayer named Qrr'zarq."
> — `sources/adventure-wdh.json:17802`
> "Qrr'zarq comes from a colony of mind flayers in Undermountain that wants to implant {@creature Xanathar|WDH} with an illithid tadpole and, through a magical process called ceremorphosis, turn the beholder into a thrall. Qrr'zarq is waiting for an opportunity to implant the tadpole while {@creature Xanathar|WDH} is alone and asleep. The mind flayer doesn't want adventurers to complicate or ruin its brilliant plan, which it keeps to itself. It offers to help characters who agree not to harm it or the beholder."
> — `sources/adventure-wdh.json:17803` (the replacement plan; not used by the campaign)

> "Virtually all of the Xanatharians..." — not on this point.

**Search result:** a search of `sources/adventure-wdh.json` for "dominat", "control", "trusted" and "advis" found no line that says Nihiloor controls or dominates Xanathar. The published text uses dominate monster only on creatures (`:2815`; Appendix C `:1898`).

**Rank note (not a decision):** campaign files outrank the published adventure, and the campaign files state the domination as current fact in the page, the Guild page, the Xanathar page relationship notes, the structure doc and the history Secret. Three Grand Game and villain pages mark it "left open" (D1 quotes above). The orchestrator decides.

**Ilsensine page (spoiler limit; not a ruling)**: `campaign/setting/deities/ilsensine.md:60` (quoted in A10) says the domination and the devourers are "Never reveal" before the party's own evidence supports them.

### D2. Pronouns: "it/its" on the page, "he" in some campaign quest text, "his" in the adventure

Quoted in B (Pronouns). Higher source: the page is the subject, and its summary gives it/its. The campaign quest files (`ev-02-nihiloors-wing.md:139`; `overview.md:43`) and the adventure (`:17827`) use "he" or "his". The brief says pronouns come from the existing page or the source and are never inferred. The orchestrator decides. No file is cited for a different pronoun in the Nihiloor page itself.

### D3. Dragon Heist page: 212 or 213

- Adventure: "page": 212 at `sources/adventure-wdh.json:32340`; wiki "WDH5e-p212" at `Nihiloor.txt:61`.
- Guild page: "- **Nihiloor** (DH p. 213) — Mind flayer, lawful evil." — `campaign/setting/organizations/08-xanathars-guild.md:103`.
- Higher source: the adventure (published). The Guild page is a campaign file and outranks it on the Guild page only. The orchestrator decides.

### D4. Morale: "retreat when threatened" against the X26 fight and the Appendix C tactics

> "In a fight, Nihiloor would use Dominate Monster on the most dangerous combatant, command its intellect devourers to attack, and retreat when threatened." — `04-nihiloor.md:23`
> "Nihiloor and the intellect devourers make their stand here. If the characters flee, the mind flayer sends the intellect devourers after them and stays behind." — `sources/adventure-wdh.json:17848`
> "Nihiloor doesn't pursue anyone who flees, trusting that they won't get far." — `sources/adventure-wdh.json:17791`
> "Nihiloor's goal is exit, not victory. It spends each turn moving toward the door rather than maximizing combat effectiveness. Only block it entirely to force a fight." — `sources/Appendix_C_-_Player_Faction_Missions.md:1907`
> "The fight ends when Nihiloor leaves the wing or the party stops fighting. A party can end it without beating him by taking a second node quickly, because he runs when it falls." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:186`

The page's "retreat" fits the Appendix C and Force Grey texts. The adventure's X26 text has the mind flayer "stay behind" and "make their stand". Higher source: the adventure for the published room (X26); campaign files for the Force Grey fight. The orchestrator decides.

### D5. The wing's room names and contents (X23 to X27)

| Source (rank) | X23 | X24 | X25 | X26 | X27 |
|---|---|---|---|---|---|
| Adventure, room headers (published, `adventure-wdh.json`) | "X23. Antechamber of Madness" (`:17709`) | "X24. Extraction Chamber" (`:17762`) | "X25. Food for Thought" (`:17808`) | "X26. Devourer Spawning Pool" (`:17835`) | "X27. Prison" (`:17853`) |
| Alexandrian Lair roster (printed p.89 [PDF p.7], [image transcription]) | "Area X23 – Antechamber of Madness" | "Area X24 – Extraction Chamber" | "Area X25 – Food for Thought" | "Area X26 – Spawning Pool" | "Area X27 – Nihiloor's Prison" |
| Appendix C Force Grey mission (quest text) | "X1 → X2 ... → corridor through X22 → X24 (Extraction Chamber; Nihiloor, 50% chance; one drow prisoner) → X25 (Food for Thought) → X26 (Spawning Pool)." (`Appendix_C:1885`) | (same) | (same) | (same) | not named |
| Campaign structure doc (`arc-f-xanathars-lair.md`, authoritative until the Lair journal exists) | "X23 — Competitive Intelligence Files." (`:175`) | "X24 — The Infiltration." (`:176`) | "X25 — The Experiments." (`:177`) | "X26 — The Puppet." (`:178`) | not named (the domain is "Areas X23–X27", `:173`) |
| Campaign Force Grey wing (quest text) | "X23 holds Nihiloor's files" (`ev-02-nihiloors-wing.md:19`) | "X24 the placement records" (`:19`) | "X25 the Pool, the captive and twelve specimens" (`:19`) | "X26 the Puppet device" (`:19`) | not named |
| Force Grey mission overview (quest text) | "At X23 the party meets the first of four enthralled guards" (`m04 overview.md:35`) | "X24 holds the placement records, with Orvyn Dall's folio among four" (`:35`) | "X25 holds the pool, the twelve specimens, the pet and the captive" (`:35`) | X26 is the Puppet device (`ev-02:139`) | "X27" not named |

Quote the campaign sentences exactly:
> "- **X23 — Competitive Intelligence Files.** ..." (`arc-f-xanathars-lair.md:175`, quoted in A5)
> "The wing is four rooms, where X23 holds Nihiloor's files, X24 the placement records, X25 the Pool, the captive and twelve specimens, and X26 the Puppet device. The party never has to enter X26." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:19`
> "X24 holds the placement records, with Orvyn Dall's folio among four, and X25 holds the pool, the twelve specimens, the pet and the captive." — `m04-destroy-the-intellect-factory/overview.md:35`
> "The wing is area X23 to X26 of **Xanathar's Lair**, and this mission adds three things to the rooms that quest already describes. The pool and the captive sit in X25 beside the twelve specimens, and the placement records lie in X24." — `m04-destroy-the-intellect-factory/overview.md:25`
> "X23 files, X24 placement records, X25 experiments, X26 the Puppet" — `m04-destroy-the-intellect-factory/design-notes.md:9` (quoted within the sentence "Nihiloor's wing uses only the lair's codes: X23 files, X24 placement records, X25 experiments, X26 the Puppet." This is an exact fragment of: "The mission is now an objective inside **Xanathar's Lair**. ... The wing uses only the lair's codes: X23 files, X24 placement records, X25 experiments, X26 the Puppet. The pool, the records and the captive are added to those rooms, and the Puppet device stays with the lair quest.")

Adventure-only detail: the adventure puts Nihiloor's own lair in "areas X23 through X26" (`:17802`), and X27 is the prison "Nihiloor the mind flayer uses this prison" (`:17857`). The adventure's X23 guards are kuo-toa: "A {@creature kuo-toa whip} and six {@creature kuo-toa} guard the hall." (`:17717`). The campaign's X23 thrall is "an enthralled Guild soldier" (`ev-02:39`).

Higher source: the campaign structure doc (`arc-f`) for the lair's room roles; the adventure for the published room names. The Force Grey files use a third layout. The orchestrator decides.

### D6. The escape device: "orb" or "amulet"

- Adventure: "{@creature Nihiloor|WDH} carries a 3-inch-diameter stone orb carved to resemble an eyeball" (`sources/adventure-wdh.json:2815`); "If the stone eye in {@creature Nihiloor|WDH}'s possession is pressed into the circular indentation" (`:2896`).
- Alexandrian Lair PDF, printed p.85 [PDF p.3] [image transcription]: "If not, they could theoretically put the hideout under surveillance, ambush Nihiloor, and use his amulet to activate the portal and enter the lair."
- Campaign, Q11: "**Activation:** Nihiloor's 3-inch stone orb, when pressed into the indentation ..." (`campaign/locations/xanathar-sewer-hideout/q11-escape-portal.md:11`).
- Higher source: the campaign (orb). The Alexandrian "amulet" is an outlier.

### D7. How devourers take hosts and what happens to the brain

- Adventure, puppet model: "Each intellect devourer attacks the first humanoid it encounters, using its victim as a puppet to spy on the city and relay information back to {@creature Nihiloor|WDH}." (`sources/adventure-wdh.json:32353`)
- Adventure, brine (transform, 90 percent rot): quoted in A3 (`:17847`).
- Campaign, custom "Occupying Devourer": "The devourer is a custom variant that keeps Corene's brain alive." (`campaign/quests/faction-events/harpers/m05-the-sleeping-asset/overview.md:25`)
- Campaign, Harper design note: "The 2024 intellect devourer eats the host's brain and only *Wish* restores it." (`campaign/quests/faction-events/harpers/m05-the-sleeping-asset/design-notes.md:9`)
- Campaign, the Dungeons Dragon? — Campaign, Trollskull/Dungeons not needed. Campaign, Dungeons. Campaign, Dungeon Dock: "A 2024 **Intellect Devourer** that takes a body consumes the host's brain, so each host died when it was taken, and nothing the party does can save it." (`campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:287`)
- Campaign, the Meloon note: "The Notable Figures pages for Meloon and Nihiloor still say the devourer "ate his brain"." (`campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/design-notes.md:19`). The current Nihiloor page does not say "ate". Its line 21 says "who walk the city with their own brains intact and a devourer steering them." This note is stale for this page.
- Wiki, the goblins and bugbears: "some of whom were infected with [[intellect devourer]]s, presumably by Nihiloor." (`wiki.txt:106`). The Guild page line 45 says "Nihiloor has infected some of them with intellect devourers" (no "presumably").

Higher source: the campaign's custom-devourer rules (`m05 overview.md:25`, `m05 design-notes.md:9`) for the mechanic. The brain-death statement in `m03 ev-01:287` is quest text on a 2024 standard devourer. The page's "brains intact" follows the campaign's custom device. The orchestrator decides.

### D8. When Meloon was taken, and by whose devourer

- Adventure: "Three months ago, out of boredom, Meloon accompanied a fledgling band of adventurers on an expedition to Undermountain." (`sources/adventure-wdh.json:32256`); "An intellect devourer in league with {@creature Xanathar|WDH} ate Meloon's brain several months ago." (`sources/adventure-wdh.json:1548`); "The intellect devourer that inhabits Meloon's skull was bred by {@creature Nihiloor|WDH}, a mind flayer in {@creature Xanathar|WDH}'s employ." (`:32257`).
- Campaign: "After the Field of Triumph, an Occupying Devourer from Nihiloor's brood took his skull, about three tendays before the watch begins." (`campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:21`); "- **Affiliation:** Force Grey (occupied by a Xanathar's Guild intellect devourer after the Field of Triumph, about three tendays before the first day of the watch)" (`campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:6`).
- Campaign, the Guild page: "An intellect devourer bred by Nihiloor rides Meloon Wardragon, a member of Force Grey, and steers adventurers away from Undermountain and toward the Guild's enemies (**Meloon Wardragon**; *Dragon Heist*, 5e)." (`campaign/setting/organizations/08-xanathars-guild.md:89`)
- Higher source: the campaign (`m03 overview:21`; Meloon page line 6). The adventure's "Three months ago" and "in league with Xanathar" conflict. The Doom Raiders org page notes the same conflict: "`history/08-the-players-arrive.md` line 138 puts the intellect devourer's occupation after the Field of Triumph, so Meloon is himself on Ches 1." (`campaign/setting/organizations/06-doom-raiders.md:183`)

### D9. Captain Hyustus Staget in the X27 prison

- Adventure: "Imprisoned in the westernmost cell along the north wall is Hyustus Staget, a captain of the City Watch whom the characters have met" (`sources/adventure-wdh.json:17873`).
- Campaign: "The street war. Captain Hyustus Staget lets Xanathar's Guild and the Zhentarim wear each other down, and he will not send a force into the sewers after a suspected spy. No campaign event uses him." (`campaign/guides/factions/12-open-lords-watch.md:99`)
- Campaign, the Guild page: "Captain Staget reasons that the two may as well destroy each other" (`08-xanathars-guild.md:95`).
- Higher source: the campaign (the Watch page's "No campaign event uses him"). The adventure's X27 captive is a published fact that the campaign's Watch page does not mention. The orchestrator decides.

### D10. Tense: wiki past tense against campaign present

- Wiki: "Nihiloor (...) was a [[mind flayer]] who worked for the [[Xanathar's Thieves' Guild]] in the late 15th century DR" (`Nihiloor.txt:61`).
- Campaign page: "Nihiloor is the intelligence operative of Xanathar's Guild" (`04-nihiloor.md:29`).
- The wiki is last in rank. Its tense reflects its own 5e citation.

### D11. The "something vast and dreaming" seed: who the dreamer is (Undermountain)

Mark: Undermountain. The seed is not Nihiloor's; it is in the Nihiloor-adjacent Lair. Quoted because the caller asked.

> "The Mad Mage seed planted here — the brief impression of something vast and dreaming, far below — is a load-bearing element for Undermountain. The party won't have context for it until Undermountain Level 17. It should land as texture here: something the attuned character experienced and may or may not mention, not a revelation the GM explains. Leave it unresolved."
> — `campaign/structure/arc-f-xanathars-lair.md:382` (Undermountain)

> "**Mad Mage Seed.** For one moment — brief, involuntary — the attuned character experiences the Stone's communication as something vaster than a Stone. Not just old. Something that once dreamed, much further below, in the dark under the dark. The impression passes in seconds. The Stone says nothing about it. The GM should not explain it. It is a seed, and it belongs to Undermountain."
> — `campaign/structure/arc-f-xanathars-lair.md:266` (Undermountain)

> "*Mad Mage Seed.* Any character who handles the *Stone of Golorr* briefly before it is secured in Arc D experiences a whisper they cannot localize — something ancient, patient, and cold, dreaming beneath the city. This is aboleth Illuun on Undermountain Level 4. Planted now, pays off if the campaign extends into the Dungeon of the Mad Mage."
> — `campaign/structure/arc-c-fireball.md:310` (Undermountain; names Illuun on Level 4)

> "*Mad Mage Seed.* Any character who handles the Stone directly — holds it, examines it, attunes to it — hears a whisper they cannot localize: something ancient, patient, and cold, dreaming beneath the city. This is aboleth Illuun on Undermountain Level 4. Planted now, pays off if the campaign extends into the Dungeon of the Mad Mage."
> — `campaign/structure/arc-d-gralhund-villa.md:378` (Undermountain; names Illuun on Level 4)

> "- **Who Illuun is:** An aboleth dreaming on Undermountain Level 4. The Stone holds an aboleth's memory, and Illuun answers it."
> — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:84` (Undermountain)

> "- **The vast dreaming seed:** The Xanathar's Lair structure document plants "the brief impression of something vast and dreaming, far below", which the party will not understand "until Undermountain Level 17" (`campaign/structure/arc-f-xanathars-lair.md:382`). The file does not say what the dreamer is, and this page does not claim it is Ilsensine (see Draft Notes)."
> — `campaign/setting/deities/ilsensine.md:72`

Conflict: `arc-f:382` (the seed "far below", "until Undermountain Level 17") and `arc-f:266` do not name the dreamer. `arc-c:310`, `arc-d:378` and `stone-of-golorr-and-the-eyes.md:84` name Illuun, an aboleth on Level 4. Not settled. The ilsensine page says the seed is "deferred to the Undermountain pass" (`ilsensine.md:104`). That line reads: "The user ruled (Session 51) that the seed stays unresolved and is deferred to the Undermountain pass."

---

## E. Stale lines in other files (not edited), and routed references

### E1. Stale or wrong lines in other files

- `campaign/setting/villains/xanathar.md:105` says the page's Nihiloor lines say "no interest in supplanting Xanathar": "`04-nihiloor.md` lines 22 and 26 say Nihiloor has no interest in supplanting Xanathar, and the current page does not say it." The current page has no such line (the only Relationship line is "a trusted mind flayer operative..." at L21 and "It has no interest" is absent). The note is stale against the current file.
- `campaign/setting/organizations/08-xanathars-guild.md:182` (Draft Notes): "The page states the domination and leaves the adventure's line out." Current page L23 and L25 do not state "no interest"; the note is consistent with the current file.
- `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/design-notes.md:19`: "The Notable Figures pages for Meloon and Nihiloor still say the devourer "ate his brain"." The current Nihiloor page says "with their own brains intact". Stale for this page.
- `campaign/setting/history/02-the-long-shadow.md:80` (quest-time phrasing on a setting page): "The Xanathar that the party meets, including the one who killed Manshoon's envoys and sent response teams against the party's allies, has been Nihiloor's instrument." (ruling 1 applies; "the party meets" is quest-time phrasing on a setting page.)
- `campaign/gazetteer/waterdeep/dock-ward.md:110` (quest-time hook on a gazetteer page): "- Hook: in **Finding Floon**, Floon is held in the boss chamber at 1 hit point, and Nihiloor leaves through a stone portal at the far end before the party can engage it."
- `campaign/setting/geography/undermountain-and-skullport.md:107` (quest-time sentence on a setting page): "- **Nihiloor and Level 17 (campaign only):** "Nihiloor was not in his domain at the time and escapes to Undermountain Level 17 with his three projects intact" (`campaign/structure/arc-f-xanathars-lair.md:111`). The published support is thin. ..." The quoted sentence is conditional on the lair's demolition.
- `campaign/setting/deities/tymora.md:82` (quest-time on a setting page): "In the campaign it takes him after the Field of Triumph, about three tendays before the first day of the watch. The party can force it out in **The Trouble with Meloon**, and the real Meloon then remembers the occupation as a long dream." (the full bullet is "- **The occupation:** An intellect devourer from Xanathar's Guild takes his body and reports to the Guild through a courier. ...")
- `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:26` (Notable Figures page; states the domination as fact): "**Relationships.** Xanathar is the beholder crime lord of Xanathar's Guild, the employer of Ahmaergo (its majordomo), Nihiloor (its mind flayer, which has psionically dominated Xanathar for the last four months without Xanathar knowing), and Nar'l Xibrindas (its drow advisor, whom it does not yet know is Jarlaxle's spy)." Day-one per the campaign, contested by D1.
- `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md` — the one other page that carries the domination line.
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:101` and the three "left open" lines (D1) are not stale; they are left open.
- `campaign/guides/factions/09-xanathars-guild.md:72` (Factions Guide escalation table; "Nihiloor processes captured intelligence") is day-one and consistent.
- `campaign/setting/history/02-the-long-shadow.md:92` and `:93` cite the Nihiloor page by line ("the Nihiloor domination (lines 24 and 129)"). Line citations shift when the page is rewritten.
- `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt`: not checked for this page (Ott notes already cover its snapshot copies).

### E2. Routed quest references (where the quest-time facts already live)

Mission and quest facts that the page's "Featured in" and Morale/Relationships lines depend on:

- **Finding Floon** (Q07 sewer hideout). `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:67`: "**Nihiloor** (mind flayer) is seated on a raised platform to the south, cradling an **intellect devourer**." Line `:69` (quoted in D2). Line `:90`: "The party's encounter with Nihiloor is a sight-line. They see it rise, release the intellect devourer, and glide out of the room." Line `:107`: "- **Nihiloor Sighted** — mark when the party witnesses a mind flayer in the Guild's sewer cell. They don't yet know what it is. This Event Outcome pays off when the mind flayer's role in the Grand Game surfaces in **Xanathar's Lair**." Also `campaign/quests/act-i/finding-floon/overview.md:32` ("- **Nihiloor** (Xanathar's Guild / Undermountain) — partial; observed briefly in Q07 before escaping through the Q11 portal; does not engage the party") and `:44`.
- **Gralhund Villa** (aftermath). `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:110`: "**Emerald Enclave (Melannor).** Gralhund Villa sits over a minor ley line the Enclave monitors as part of Jeryth Phaulkon's aberrant-activity survey. Xanathar's Guild's presence in the neighborhood destabilized it over the past week in a way that correlates with Nihiloor's movements below the city." Line `:114`: "**Force Grey (Vajra).** A full operational debrief: ... and any direct evidence of Nihiloor's involvement."
- **Faction Outposts** (Mirt briefing). `campaign/structure/arc-e-faction-outposts.md:369` (quoted in A8). No Nihiloor scene exists in `arc-e`.
- **Xanathar's Lair** (structure doc; unconverted). `arc-f-xanathars-lair.md:15`, `:79`, `:95`, `:111`, `:113`, `:173` to `:178`, `:284`, `:294` ("- **Mirt:** "Is Thorvin alive?" ... He suspects Nihiloor. He does not say so directly."), `:298` ("- **Vajra:** "Tell me about the panopticus. All of it." She already suspects what Nihiloor might be doing."), `:339`, `:340`, `:341`, `:344`, `:346`, `:400`, `:404` to `:410`.
- **The Trouble with Meloon** (Force Grey M3). `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:21` (quoted in A6), `:43` (quoted in A8), `:81` ("- **Nihiloor** (Xanathar's Guild): receives the reports and never appears."). `ev-02-the-extraction.md:260`: "- **Nihiloor Identified Party** — mark when the Day 5 conversation took place and the devourer was still in Meloon at dusk on Day 10; read by **Destroy the Intellect Factory** and **Xanathar's Lair** (unconverted)."
- **Destroy the Intellect Factory** (Force Grey M4). `m04-destroy-the-intellect-factory/overview.md:10`, `:17`, `:21`, `:25`, `:35`, `:41` to `:43` (quoted in B), `:61`, `:66`, `:72`, `:76`, `:80`; `ev-01-the-brief.md:17` ("Nihiloor's wing is X23 to X26 of the lair, and there is no separate route, because the party reaches the wing while it runs **Xanathar's Lair**."), `:53`, `:67` to `:73`, `:96`, `:112` to `:128`; `ev-02-nihiloors-wing.md:10`, `:18` (quoted in C), `:22`, `:29`, `:42`, `:94`, `:139`, `:147`, `:151`, `:166`, `:170`, `:186`, `:200`, `:227`, `:261`, `:305`, `:316`, `:324` to `:328`; `design-notes.md:5`, `:9`, `:11`, `:15`.
  - `ev-02-nihiloors-wing.md:166`: "To begin, Nihiloor steps between the party and whichever of the four things they reach for first, and he never uses Withdraw while two or more of them remain. The players can see this, and it is the Tell."
  - `ev-02-nihiloors-wing.md:316`: "- **Nihiloor Fled** — mark whenever Nihiloor leaves the wing, which is always; read by **Xanathar's Lair** (unconverted) and **The Full Picture**."
- **The Legate's Eyes** (Force Grey M5). `m05-the-legates-eyes/overview.md:21`, `:27` (quoted in A6), `:65` ("- **Nihiloor** (Xanathar's Guild): receives the reports and never appears."). `ev-02-the-extraction.md:21` ("The devourer reports to Nihiloor only through Dobb Ketterly. If the link dies, Nihiloor learns it within a day.").
- **The Sleeping Asset** (Harper M5). `m05-the-sleeping-asset/overview.md:21`, `:25` (quoted in A3 and D7), `:62` ("- **Nihiloor** (Xanathar's Guild): the mind flayer behind the devourer, who never appears."). `ev-02-the-extraction.md:150` and `:158` (Corene's intelligence on the labelled deliveries to Nihiloor's rooms: "the restricted deliveries all went to Nihiloor's rooms in the lair").
- **Faction Mechanics** (Factions Guide). `campaign/guides/factions/06-force-grey.md:23` (quoted in A8); `:30` ("| **Gralhund Villa** | ... Specifically: any sign of Nihiloor's presence, any implanted citizens encountered, any evidence of coordination between the Guild and outside parties. |"); `:31` ("| **Xanathar's Lair** | Mission 4 is an additional objective inside **Xanathar's Lair**, played in Nihiloor's wing (X23 to X26). ..."); `:73` ("| **M3 Complete** plus **Xanathar's Lair** preparation, or Renown 8 | **Destroy the Intellect Factory** | An objective inside **Xanathar's Lair**, played in Nihiloor's wing. Destroy the pool that breeds Occupying Devourers, take the placement records and free the captive. Nihiloor always escapes. Vajra pays for any *raise dead* the work needs. | +3 |"); `:74` ("| Renown 10, 6th level | **The Legate's Eyes** | Three Watch magistrates have reversed rulings in the Guild's favour. Trace them to Orvyn Dall, an appeals clerk in a Trades Ward magistracy whose devourer reports through a Guild courier, and extract him without a Watch review. | +4 |").
  - `campaign/guides/factions/02-harpers.md:31` (quoted in A6); `:72` ("| 6th | **The Sleeping Asset** | Find and rescue Harper informant Corene Wyldath, missing three weeks from her post inside Xanathar's Dock Ward operation. An intellect devourer rides her. ...").
  - `campaign/guides/factions/05-order-of-the-gauntlet.md:31` (quoted in A8).
  - `campaign/guides/factions/09-xanathars-guild.md:112` ("- Notable Figures: **Xanathar**, **Ahmaergo**, **Nar'l Xibrindas**, **Nihiloor**, **Noska Ur'gray**, **Gorath**, **Korgstrod Uxgulm**, **Keln Trigos**, **Grinda Garloth**").
- **Trollskull Alley patron** (tavern guide): `campaign/guides/trollskull-manor/08-notable-patrons.md:64`: "**Act II–III note:** By Act II, Meloon has been compromised by a Xanathar's Guild intellect devourer. The Meloon who visits during Act I is genuine. The one who arrives in Acts II–III may not be."
- **Guard in the wing** (Force Grey M4 thrall): `ev-02-nihiloors-wing.md:29` ("Nihiloor's wing is the only part of the lair the Guild avoids. Soldiers who draw a shift here ask to be moved within weeks, and none of them will say why.").

### E3. Undermountain-marked items (not Ches 1 lore)

- Seadeeps colony: `campaign/setting/geography/undermountain-and-skullport.md:72` (quoted in A1); `sources/adventure-wdmm.json:24431` and `:46748` (quoted in A1).
- Escape to Level 17: `campaign/structure/arc-f-xanathars-lair.md:111` (conditional); `campaign/setting/deities/ilsensine.md:70` ("- **Nihiloor's escape to Level 17:** If Xanathar's lair is demolished, "Nihiloor was not in his domain at the time and escapes to Undermountain Level 17 with his three projects intact" (`campaign/structure/arc-f-xanathars-lair.md:111`; also `:284` and `:346`). This is the only campaign line that sends a mind flayer from the city to the colony below.").
- Qrr'zarq replacement plan: `sources/adventure-wdh.json:17803` (adventure only; not in the campaign).
- The seed: `arc-f:382`, `arc-f:266` (quoted in D11).
- Ilsensine: "- **Campaign ties:** One fresco in the **Vault of Dragons** structure document names Ilsensine." (`ilsensine.md:59`, quoted in A10).

---

## F. Gaps (what a Background would need that no source gives)

1. **Birth, origin, first arrival in the city.** No source. The wiki gives "worked for the Xanathar's Thieves' Guild in the late 15th century DR" (`Nihiloor.txt:61`) and no origin. Suggested handling: leave out, or state "No source records Nihiloor's origin." Do not invent.
2. **Date it began service with Xanathar.** Wiki only: "late 15th century DR" (`Nihiloor.txt:61`, 5e citation WDH5e-p212). Suggested: use the wiki phrase tagged `[research: wiki, 5e]`.
3. **Rank in the Guild.** The Guild ladder (`08-xanathars-guild.md:45`) does not place Nihiloor. Its office is "Officially handles Xanathar's most sensitive intelligence operations" (`08-xanathars-guild.md:103`). Suggested: use that sentence, not a rank.
4. **How it came to the Guild's trust.** No source. The Persona's "a status no other Guild member holds" has no published basis. Suggested: none beyond the campaign line; tag `[research]` if used.
5. **The domination (D1).** Open. Suggested: state both sides as the Villains page does, or state the campaign claim with its source. Not a Background fact until the orchestrator rules.
6. **Seadeeps link.** The Key Members line says "the Seadeeps colony (Undermountain Level 17)" is the payoff of Nihiloor's projects (`08-xanathars-guild.md:103`). No source says Nihiloor came from Seadeeps, or whether its brood is from there. Suggested: say the projects pay off in Seadeeps; do not say where Nihiloor was born `[research]`.
7. **Who made the custom devourer and the brine.** The brine process is published (`adventure-wdh.json:17847`). The campaign's custom "Occupying Devourer" has no origin text beyond the Force Grey and Harper references. Suggested: give the brine process as the published method, tagged 5e.
8. **How it chooses hosts.** Published: "the first humanoid it encounters" (`:32353`), and the Q07 and X27 "captures" (`:17827`, `:17857`). The campaign's targeting (Watch, city offices) is in `arc-f:176`. No method for placing hosts in offices. Suggested: say the placements are in the records (`arc-f:176`).
9. **Age, sex and body.** The page says "it/its" (L5). The voice profile says "sexless" (line 68). No age. Suggested: no age.
10. **Faith.** None (A10). Do not link to Ilsensine (`ilsensine.md:59`).
11. **Its quarters and sleeping.** Published: its lair "areas X23 through X26" (`:17802`). Campaign: "Nihiloor's Domain (Areas X23–X27)" (`arc-f:173`). Suggested: use the campaign range.
12. **Feelings about its own work.** The Emotions line is the campaign's. No source. Suggested: keep as the page's own.
13. **Relationship with Nar'l Xibrindas, Ahmaergo, Noska Ur'gray and Gorath.** No source connects Nihiloor to any of them (searched; see Not found). The Lair PDF says Nar'l "knows more than most" (`11. Lair Xanathar's Lair.pdf` printed p.91 [PDF p.9]; the sentence is "N'arl Xibrindas knows more than most. He's even snuck into the Crypt of Xanathars Past (X33)."), which does not mention Nihiloor.
14. **Why Xanathar trusts it.** No source (the Ott research notes "known for years" as the same gap).
15. **The panopticus gift date.** "three years ago" (`arc-f:15`) is the only date. The adventure does not date it.
16. **The Watch captain Staget in X27** (D9). The campaign has no X27 content. Suggested: leave out of Background.
17. **Other mind flayers in the Guild.** The wiki names Suthool in a 1491 DR alliance (`wiki.txt:484`). The campaign names no other mind flayer in the Guild. Suggested: do not use Suthool for Nihiloor.
18. **Stone orb origin.** Published: "3-inch-diameter stone orb carved to resemble an eyeball" (`:2815`). No maker. Suggested: state the orb, not its origin.

---

## Not found

Terms searched: "Nihiloor" (all case-insensitive variants), "intellect devourer", "mind flayer", "Mind Flayer", "illithid", "dominat", "control" (Xanathar context), "tadpole", "ceremorphosis", "Qrr", "Seadeeps", "Ilsensine", "something vast", "dreaming", "Hyustus", "Zaibon", "Grum'shar", "Suthool", "Soluun", "Dobb Ketterly", "Orvyn".

Files searched:
- All of `campaign/` (Grep, content mode, every line). Notable: no Nihiloor line in `campaign/setting/history/08-the-players-arrive.md`, `campaign/setting/lore/`, `campaign/setting/villains/jarlaxle.md` (only the "Left open" line `:179`), `campaign/setting/villains/manshoon.md` (only `:139`), `campaign/setting/the-grand-game/running-the-villains` (no match; the file is `campaign/guides/gm-guide/running-the-villains.md`, which has the response-team row at `:49`), `campaign/guides/factions/10-manshoons-zhentarim.md`, `campaign/guides/factions/04-emerald-enclave.md`, `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md` beyond `:26`, `campaign/setting/notable-figures/manshoons-zhentarim/`, `campaign/setting/notable-figures/harpers/05-corene-wyldath.md` beyond the Emotions and Motivations lines.
- Notable Figures: `campaign/setting/notable-figures/xanathars-guild/` other pages: no line naming Nihiloor other than `01-xanathar.md:26` and `04-nihiloor.md` itself. Ahmaergo, Nar'l, Noska, Thorvin, Gorath, Keln and Grinda pages name no devourer tie to Nihiloor (folder grep).
- `campaign/structure/arc-e-faction-outposts.md`: only `:369`.
- `campaign/structure/arc-g-cassalanter-villa.md:437` and `:501`, `arc-h`, `arc-i-kolat-towers.md:61`, `:315`: X23 Nihiloor files as a Kolat Towers clue. Routed, not Background.
- `campaign/gazetteer/waterdeep/`: Dock Ward (`:110`, `:166`), Field Ward (`:84`), Trades Ward (`:85`, `:99`, `:134`, `:232`), North Ward (none).
- `campaign/locations/`: Xanathar Sewer Hideout area overview and rooms Q07 and Q11.
- `campaign/quests/`: all event files and missions with a Nihiloor line (listed in E2).
- `sources/adventure-wdh.json` (all lines). Lines not listed above were searched but gave no Nihiloor fact beyond those listed.
- `sources/adventure-wdmm.json`: "Seadeeps", "Nihiloor", "Qrr", "Ilsensine", "something vast", "dreaming". Hits: `:215`, `:24431`, `:24432`, `:44069`, `:46637`, `:46748`, `:46762`, `:48044`. No Nihiloor line (the Seadeeps text is about the mind flayer colony generally).
- `sources/SOURCE_GUIDE.md`: `:29`, `:99`, `:109`, `:343`, `:397`. Quoted in part:
  - `:29`: "- **Chapter 5 — Spring Madness (Xanathar):** Full Xanathar's Lair keyed location (36 areas), ... Nihiloor, ..." — `SOURCE_GUIDE.md:29`.
  - `:397`: "- Nihiloor introduction: the mind flayer is present but not meant to be confronted. Escape, stealth, or distraction are the intended solutions." — `SOURCE_GUIDE.md:397`.
- `sources/Act_III_Arc_E.md`, `sources/Act_III_Arc_D.md`: no Nihiloor line.
- `sources/Appendix_B_-_Player_Factions.md`: `:406` (Order), `:466` (rescue), `:905` (Force Grey), `:939` ("| 5th | **Destroy the Intellect Factory** | Xanathar is using intellect devourers to seize control of key Waterdavians throughout the city. Infiltrate the beholder's lair and destroy whatever is creating these horrors. Vajra covers the cost of any *raise dead* spells required. | +2 |"). No Nihiloor name in Appendix B.
- `sources/Appendix_C_-_Player_Faction_Missions.md`: `:1791`, `:1821`, `:1841`, `:1852`, `:1854`, `:1861`, `:1883`, `:1885`, `:1891` to `:1898`, `:1905` to `:1907`, `:1915`, `:1917`.
- `sources/Appendix_D_-_Running_the_Tavern.md`: no Nihiloor name.
- `sources/research/pass5-bundles/xanathars-guild/wiki.txt`: `:104`, `:106`, `:115`, `:484`, `:984` to `:1046` (linked page).
- `sources/research/pass3-bundles/` and `pass4-bundles/`: snapshots of the current files.
- The Alexandrian PDFs listed in Method (all pages read). The Stat Reference (printed p.91) has no Nihiloor entry. The Revelation List names Nihiloor only at printed p.121.
- Not found in the Alexandrian Faction Outposts PDF: no Nihiloor line in PDF pp.1 to 13 (the Xanathar outposts at printed pp.42 to 44 name Keln Trigos, Grinda Garloth, Korgstrod Uxgulm and Ahmaergo, with no Nihiloor).

Not found (gaps for the drafter):
- Birth, origin, first arrival in Waterdeep.
- Date of first service to Xanathar, and any date for the wing's construction.
- A rank or title for Nihiloor in the Guild's published ladder.
- Any source for Nihiloor's relation to Nar'l, Ahmaergo, Noska or Gorath.
- Any source for Nihiloor's worship, god, rite, shrine or clergy.
- Age, size, and the sex of the body (the page's "it/its" is the page's own).
- Any source for the Guild's rule that a hint of the domination would get members "disintegrated" (Relationships, row 10c).
- Any stat-block entry for Nihiloor in the Alexandrian Lair stat reference (printed p.91).
- Any Harper or Force Grey source for a Nihiloor stat block in 5e MM text beyond Appendix C's "2024 Monster Manual" line and the Force Grey section 4.1 reference.

---

## Not readable

- No file failed to open. The Alexandrian PDFs were read as rendered images (no text layer in this session). Quotes marked `[image transcription]` need `pdftotext -layout` checks before prose use.
- `sources/Other remix files/*.docx`: not opened (the tools cannot read `.docx`). `SOURCE_GUIDE.md` lists the following files, and the campaign cites one of them for Nihiloor:
  - "The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx" (`sources/SOURCE_GUIDE.md:695`). `campaign/setting/history/02-the-long-shadow.md:146` says: "The Waterdavian's Guide docx has Zushaxx plot with Nihiloor to kill Izulktur and gives Zushaxx an arrival in Skullport in 1205 DR as a slaver from the Graypeaks Hive (lines 455, 480-482). Neither is a campaign decision." This claim is not verified here. Name it as the source for the orchestrator to extract.
  - "Meloon Wardragon NPC Guide.docx" (`sources/SOURCE_GUIDE.md:692`): "Meloon as a Force Grey contact; his mind-control situation (Ahghairon's Dragonward), morale, and redemption arc." The guide may give the devourer's origin and the Meloon date (D8). Name it for extraction.
  - "Davil and the Doom Raider Zhents + Elf Killer mission and more.docx" (`sources/SOURCE_GUIDE.md:688`). Davil's page (`doom-raiders/01-davil-starsong.md:25`) names Nihiloor's devourer. Name it for extraction if the drafter wants the Davil tie.

## Not run

- `voicecheck.py` was not run (research only).
- No file was written except this notes file. The page was not written.
