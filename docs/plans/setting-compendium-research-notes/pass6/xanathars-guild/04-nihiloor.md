# Pass 6 research notes: Nihiloor

Page: `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md` (current file, 30 lines)
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Format model: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Day-one state used: Ches 1, 1492 DR. Nihiloor is in Xanathar's lair (campaign range X23 to X27). Whether Nihiloor dominates Xanathar is recorded as open (D1). This file does not settle it. Meloon's occupation is a quest-time date by a settled user ruling (D8), so it is not treated as day-one.

Method and caveats:
- Campaign files: Read and Grep, quoted from the tool output. Paths are relative to `/home/user/waterdeep/`.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are kept as written. Escaped quotes are shown as plain quotes. `sources/adventure-wdmm.json` was searched for Seadeeps, Nihiloor, Qrr, Ilsensine and the seed wording.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. PDF quotes were transcribed from rendered page images and are marked `[image transcription]`. Each needs a `pdftotext -layout` check before any quote goes into prose. Pages read: `sources/11. Lair  Xanathar’s Lair.pdf` (PDF pp.1 to 9, all), `sources/5. Faction Outposts.pdf` (PDF pp.1 to 13, all), `sources/17. Outpost and Lair Revelation Lists.pdf` (PDF pp.1 to 4). Printed page first, then `[PDF p.N]`.
- Appendices: `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md` (the Force Grey mission text, which is quest content). `sources/Appendix_D_-_Running_the_Tavern.md` has no Nihiloor entry.
- Wiki: the linked wiki page, `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-xg/Nihiloor.txt` (cited `Nihiloor.txt`). The Guild wiki text in the pass 5 bundle, `sources/research/pass5-bundles/xanathars-guild/wiki.txt` (cited `wiki.txt`). The wiki prints no edition on most lines; where a citation key or infobox gives one, it is marked.
- Pass 3 and pass 4 bundles were searched. They hold snapshots of campaign text already quoted here.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

---

## A. Background facts by theme

### A1. Origin, home, and the Seadeeps payoff

No source gives Nihiloor's birth, origin, or how it came to Waterdeep.

**Wiki, opening line (5e citation WDH5e-p4 and WDH5e-p212)**
> "'''Nihiloor''' ({{Pronounce|NY|heh|loor|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a [[mind flayer]] who worked for the [[Xanathar's Thieves' Guild]] in the late 15{{th}} century [[DR]], by creating and spreading [[intellect devourer]]s throughout the sewers of [[Waterdeep]].<ref name="WDH5e-p212" />"
> — `Nihiloor.txt:61` (the wiki uses the past tense "was" and "worked for"; see D10)

**Wiki infobox, home and race (citation WDH5e-p212)**
> "| home           = [[Waterdeep]]<ref name="WDH5e-p212">{{Cite book/Waterdeep: Dragon Heist|212}}</ref>"
> — `Nihiloor.txt:10`
> "| race           = [[Mind flayer]]<ref name="WDH5e-p212" />"
> — `Nihiloor.txt:13`

**Campaign, Guild Key Members entry (the Seadeeps payoff; the bullet is quoted in full because it carries the three projects)**
> "- **Nihiloor** (DH p. 213) — Mind flayer, lawful evil. Officially handles Xanathar's most sensitive intelligence operations. In practice, Nihiloor is running three concurrent projects: (1) **The Infiltration** — intellect devourers placed inside city government officials give Nihiloor eyes throughout Waterdeep's bureaucracy; three Harper assets are already compromised; (2) **The Experiments** — creatures captured during Arena operations are being subjected to psionic modification seeking a "relay organism" that extends the colony's reach without destroying the host brain; (3) **The Puppet** — Nihiloor has been exerting psionic domination over Xanathar itself for the past four months, replacing its strategic decisions while leaving its personality intact. The long-term payoff of all three projects is the Seadeeps colony (Undermountain Level 17). See the **Nihiloor** page in Notable Figures."
> — `campaign/setting/organizations/08-xanathars-guild.md:103`

**Campaign, Undermountain (setting page; Undermountain-facing)**
> "| 17 | Seadeeps | A mind flayer colony. Halaster worries about its war with the githyanki of Level 16. |"
> — `campaign/setting/geography/undermountain-and-skullport.md:72`
> "| 17 | Seadeeps | Mind flayer colony (Nihiloor payoff) | Essential — Dragon Heist thread |"
> — `sources/SOURCE_GUIDE.md:99`

**Undermountain (mark: Undermountain; Mad Mage text, not Ches 1 lore)**
> "A mind flayer colony has taken over a level of Undermountain known as Seadeeps. (Cephalossk knows this because it has been in telepathic contact with the ulitharid on {@adventure level 17|WDMM|17}.)"
> — `sources/adventure-wdmm.json:24431` (the Level 9 entry)
> `"name": "Level 17: Seadeeps",` (page 221)
> — `sources/adventure-wdmm.json:46748`

### A2. Service to Xanathar, role, and rank

**Adventure, Appendix B entry "Nihiloor" (5e, page 212)**
> "The illithid {@creature Nihiloor|WDH} works for {@creature Xanathar|WDH}, spending its days creating intellect devourers and setting them loose in the sewers of Waterdeep. Each intellect devourer attacks the first humanoid it encounters, using its victim as a puppet to spy on the city and relay information back to {@creature Nihiloor|WDH}. Occasionally, an intellect devourer is instructed to seek out a particular kind of target, such as a member of the City Guard or the City Watch. Sometimes its instructions will include orders to capture specific Waterdavians and bring them to Skullport, where they can be enslaved or ransomed."
> — `sources/adventure-wdh.json:32353` (entry name at `:32339`, page 212, id "4c4")

> "{@creature Nihiloor|WDH} has an alien mind, and it considers itself {@creature Xanathar|WDH}'s equal. It has no interest in supplanting the beholder, however, preferring to operate in the shadows and pursue its own fell schemes."
> — `sources/adventure-wdh.json:32354`

**Adventure, Xanathar's underlings (5e)**
> "{@creature Xanathar|WDH} relies on underlings for advice, information, and day-to-day oversight of the Xanathar Guild. The following important underlings are described in appendix B:"
> — `sources/adventure-wdh.json:15066`
> "{@creature Nihiloor|WDH}, {@creature mind flayer},"
> — `sources/adventure-wdh.json:15073` (list runs `:15071` to `:15076`)

**Campaign, Guild structure (names Nihiloor's own lair; the whole paragraph)**
> "Xanathar rules the Guild from a lair below Skullport, and very few members have access to it (*Dragon Heist*, 5e). Its lieutenants manage the Guild's day-to-day operations (*Dragon Heist*, 5e). Ahmaergo, a shield dwarf, is the most influential member after the beholder, and Nar'l Xibrindas is its only advisor. Nihiloor has carved out a lair of its own inside the beholder's lair, Noska Ur'gray is the chief enforcer and Thorvin Twinbeard is the chief engineer and trapsmith. Ott Steeltoes keeps Sylgar, and Gorath and Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)."
> — `campaign/setting/organizations/08-xanathars-guild.md:43`

**Adventure, Nihiloor's own lair (5e; inset "Replacing the Mind Flayer", page 110)**
> "{@creature Nihiloor|WDH} the mind flayer has carved out its own lair within {@creature Xanathar|WDH}'s lair (areas X23 through X26). If {@creature Nihiloor|WDH} is killed earlier in the adventure, replace it with a mind flayer named Qrr'zarq."
> — `sources/adventure-wdh.json:17802`

**Campaign, ranks ladder (Nihiloor is not placed on it)**
> "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e). The Guild is made up of some of Waterdeep's most disreputable folk and of monsters, whom the beholder forces into service or draws in with treasure, food or power (*Dragon Heist*, 5e). Goblins and bugbears work for it, and Nihiloor has infected some of them with intellect devourers (Forgotten Realms Wiki, *Xanathar's Thieves' Guild*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:45` (the last clause is stronger than the wiki's "presumably"; see D7)

**Wiki, goblins and bugbears (pass 5 bundle; citation WDotMM-p13, edition not printed)**
> "The Xanathar Guild was also known to employ a number of [[goblin]]s and [[bugbear]]s, some of whom were infected with [[intellect devourer]]s, presumably by Nihiloor.<ref name="WDotMM-p13">{{Cite book/Waterdeep: Dungeon of the Mad Mage|13}}</ref>"
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:106`

**Rank in the Guild.** No source places Nihiloor on the ladder. The only rank-type line is the Guild's office line in the Key Members bullet at `08-xanathars-guild.md:103` ("Officially handles Xanathar's most sensitive intelligence operations."). The page's Persona line ("a status no other Guild member holds") is campaign-only (section C, row 8b).

### A3. What it does: devourers, hosts, and the brine

**Campaign, Guild informants (the whole paragraph; 5e citation)**
> "**Informants.** The Guild's informants work in every ward. Nihiloor breeds intellect devourers and sets them loose in the sewers, and each one takes the first humanoid it meets and uses its victim as a puppet to spy on the city. Some devourers hunt a particular kind of target, such as a member of the Watch or the Guard, and some capture Waterdhavians for the slave and ransom trade (*Dragon Heist*, 5e). Xanathar also dreams gazers into being, sends them to follow and spy on its own members, and sees through a stuffed beholder in the window of the Old Xoblob Shop (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:75`

**Adventure, captives fed to Nihiloor (X25 "Food for Thought", inset "Unhappy Meals", page 111)**
> "The Xanathar Guild captures homeless Waterdavians and brings them here for {@creature Nihiloor|WDH} to feed on. After devouring their brains, the mind flayer gives their corpses to his kuo-toa thralls to eat."
> — `sources/adventure-wdh.json:17827`

**Adventure, the pool and the brine (area X26, page 111)**
> "In the middle of the area is a 10-foot-diameter, 2-foot-deep circular pool containing luminous green brine. Swimming in the brine are four {@creature intellect devourer||intellect devourers}. If it has not been encountered and defeated elsewhere, {@creature Nihiloor|WDH} the {@creature mind flayer} (see {@adventure appendix B|WDH|12}) is standing in the pool with the intellect devourers."
> — `sources/adventure-wdh.json:17843`
> "The brine is a magical substance that radiates an aura of transmutation magic under the scrutiny of a {@spell detect magic} spell. {@creature Nihiloor|WDH} uses it to transform humanoid brains into intellect devourers. The process is far from perfect. A full 90 percent of the brains left in the brine rot and die, while the remaining 10 percent transform after marinating for {@dice 1d4 + 1} days."
> — `sources/adventure-wdh.json:17847`

**Adventure, the prison for hosts (area X27, page 111)**
> "{@creature Nihiloor|WDH} the mind flayer uses this prison to confine potential hosts for his brood of intellect devourers. Captured characters might find themselves incarcerated here until they can be made into hosts. The area contains the following features:"
> — `sources/adventure-wdh.json:17857`

**Adventure, the Force Grey 5th-level hook (adventure text)**
> "\"{@creature Xanathar|WDH} is using intellect devourers to take control of Waterdavians in key positions throughout the city. We must deal with this problem at once. Infiltrate {@creature Xanathar|WDH}'s lair and destroy whatever is responsible for creating these creatures.\""
> — `sources/adventure-wdh.json:3811`

**Alexandrian, Lair PDF, "Questioning the Henchmen" (printed p.91 [PDF p.9]) [image transcription]**
> "Virtually all of the Xanatharians steer clear of the mind flayer's demesne (X23-X27). It's not unheard of for even loyal members of the Guild to disappear over there. As a result, they don't know much about the layout or what's there (although they know prisoners are delivered over there). Conniving Guild members might try to convince the PCs that this is where whatever it is they're looking for is located (with the expectation that Nihiloor will eat their brains)."
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91 [PDF p.9] [image transcription]

**Campaign, Force Grey brief on the pool (quest text; the day-one facts in it are the wing and the basin)**
> "Nihiloor breeds Occupying Devourers in a stone basin in his wing of the lair, and he has used them to put hosts into the Watch and the city's offices. Meloon Wardragon was one of them, and the records in the wing list the others. A drow is strapped in a chair beside the basin, waiting for the next devourer."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/overview.md:21`

**Campaign, Harper design note on the custom devourer (quest text; a mechanic)**
> "The 2024 intellect devourer eats the host's brain and only *Wish* restores it. Both facts were wrong for a rescue, so the mission uses the custom **Occupying Devourer** from the **Harpers Mechanics Reference**. It keeps the brain alive, and the party forces it out through Hold, Breaks and Strain, by ward, by magic or by an anchor."
> — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/design-notes.md:9`

### A4. The panopticus

**Adventure, the five dwarves (area X16 entry "Dwarves", page 106)**
> "The five {@creature Panopticus Wizard|wdh|tattooed dwarves} operate {@creature Xanathar|WDH}'s \"panopticus\" magical surveillance system. They fight only in self-defense. They are {@creature apprentice wizard|VGM|apprentice wizards} (see {@adventure appendix B|WDH|12}), with these changes:"
> — `sources/adventure-wdh.json:17499`
> "{@creature Nihiloor|WDH} the mind flayer has psychically and surgically altered the dwarves so that they sleep with one eye open and half their brains asleep at any time."
> — `sources/adventure-wdh.json:17505`

**Campaign, the surveillance network as Nihiloor's gift (structure doc, the whole paragraph)**
> "The panopticus surveillance network — five ghostly beholder eyestalks wired through enchanted crystal to a monitoring station at X16 — was Nihiloor's gift to Xanathar three years ago. The beholder believes the network serves its paranoia. Nihiloor built a structural back door into the control array from the beginning."
> — `campaign/structure/arc-f-xanathars-lair.md:15`

**Campaign, the Recreation Hall blind spot (structure doc; a lair-room fact, not a quest event)**
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

**Adventure, the wing's room headers (page 110-111; names differ from the campaign; see D5)**
> "X23. Antechamber of Madness" — `sources/adventure-wdh.json:17709`
> "X24. Extraction Chamber" — `sources/adventure-wdh.json:17762`
> "X25. Food for Thought" — `sources/adventure-wdh.json:17808`
> "X26. Devourer Spawning Pool" — `sources/adventure-wdh.json:17835`
> "X27. Prison" — `sources/adventure-wdh.json:17853`

**Campaign, the Force Grey wing (quest text; the mission's own room map)**
> "The wing is area X23 to X26 of **Xanathar's Lair**, and this mission adds three things to the rooms that quest already describes. The pool and the captive sit in X25 beside the twelve specimens, and the placement records lie in X24."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/overview.md:25`
> "The wing is four rooms, where X23 holds Nihiloor's files, X24 the placement records, X25 the Pool, the captive and twelve specimens, and X26 the Puppet device. The party never has to enter X26."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:19`

**Campaign, the X23 thrall (quest text)**
> "The thrall in X23 is an enthralled Guild soldier who wakes only for Nihiloor, the pet or an alarm, so a character who walks past it needs no check."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:39`

### A6. The hosts it has taken (timing is mixed; see D8)

**Meloon Wardragon (Force Grey; the occupation is dated after the Field of Triumph, which is a Trollskull Alley event)**
> "Meloon Wardragon is a Force Grey veteran and a favourite regular at the Yawning Portal. After the Field of Triumph, an Occupying Devourer from Nihiloor's brood took his skull, about three tendays before the watch begins. It keeps his brain alive and walked him into the Xanathar's lair twice before the watch. Its telepathy reaches only 60 feet, so it reports through a Guild-paid dockhand who meets Meloon at the end of each tenday."
> — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:21`
> "- **Affiliation:** Force Grey (occupied by a Xanathar's Guild intellect devourer after the Field of Triumph, about three tendays before the first day of the watch)"
> — `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:6`
> "**Settled by the user:** Meloon Wardragon's timing is deliberate. The published adventure has the devourer take him \"several months ago\" (`adventure-wdh.json` line 1548). The campaign has the party meet him as himself at the Field of Triumph (`trollskull-alley/ev-05-the-field-of-triumph.md` lines 10 and 54; `design-notes.md` line 35), so the devourer takes him after it, about three tendays before Day 1 of Force Grey Mission 3 (`m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md` line 18)."
> — `campaign/setting/history/08-the-players-arrive.md:138`
> "**Field of Triumph:** Nonlethal gladiatorial combat across four rounds. Final round opponent is Meloon Wardragon's Force Grey team. No permanent consequences; the combat rules the arena enforces make this safe by design."
> — `campaign/quests/act-i/trollskull-alley/overview.md:55`

**Orvyn Dall (Watch appeals clerk)**
> "A devourer from Nihiloor's brood has ridden Orvyn for seven tendays. It steers which appeals reach which magistrate, and Orvyn is aware and cannot act or speak. If he dies, if Brenna calls the Watch or if a patrol sees the extraction, the Watch reviews the magistracy for 14 days."
> — `campaign/gazetteer/waterdeep/trades-ward.md:99` (setting page; present tense)
> "- **The Open Lord's Watch** (enemy, tolerated): The Watch is called to the Guild's brawls with the Zhentarim in the Dock Ward and leaves the sewer lair alone, and Captain Staget reasons that the two may as well destroy each other (**The Open Lord's Watch**; *Dragon Heist*, 5e). Nihiloor's devourers ride Watch members, including a clerk named Orvyn Dall (**Nihiloor**)."
> — `campaign/setting/organizations/08-xanathars-guild.md:95`
> "Seven tendays ago a devourer from Nihiloor's brood took Orvyn Dall, an appeals clerk in the Trades Ward district magistracy. It steers which appeals reach which magistrate, and the three reversed rulings are the result. Vajra can see the pattern in the paper and cannot prove the cause."
> — `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/overview.md:21`
> "The seven-tenday placement of Orvyn Dall is left out so that **The Legate's Eyes** can fix it."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/design-notes.md:21`
> "- Orvyn is one of four Watch and civic hosts that Nihiloor placed, and two more were pending. If **Pool Destroyed** is marked, no new hosts arrive."
> — `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/overview.md:27`

**Corene Wyldath (Harper deep-cover agent)**
> "Corene has worked inside the Dock Ward operation of Xanathar's Guild for four months. Three weeks ago one of Nihiloor's devourers took her, and it has used her since to learn who the Harpers are."
> — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/overview.md:21` (the passage continues with a second problem; rest of the passage covers the Splinter leak)
> "- **The Harpers** (enemy): The Harpers keep Thorvin Twinbeard inside the lair as a paid informant, and Corene Wyldath works in the Guild's Dock Ward operation under a false name (**The Harpers**; **Corene Wyldath**). Xanathar has begun to question Thorvin's loyalty and has set a gazer to watch him (*Dragon Heist*, 5e). One of Nihiloor's intellect devourers rides Corene, and she is one of three Harpers it has taken."
> — `campaign/setting/organizations/08-xanathars-guild.md:85`
> "- **Xanathar's Guild (enemy):** The Harpers keep Thorvin inside the lair and Corene in the Dock Ward operation, and the wiki says they move against thieves' guilds. An intellect devourer rides Corene, and she is one of three Harpers Nihiloor has taken."
> — `campaign/setting/organizations/01-harpers.md:89`
> "- **Corene Wyldath** — Halfling Harper deep-cover agent embedded in the Dock Ward operation of Xanathar's Guild; compromised by an intellect devourer three weeks ago, after four months under cover as Halla Ironstave. See the **Corene Wyldath** page in Notable Figures."
> — `campaign/setting/organizations/01-harpers.md:102`
> "Corene is a Harper deep-cover agent who has worked inside Xanathar's Guild's Dock Ward operation for four months. One of Nihiloor's custom Occupying Devourers rides her. She is aware and cannot act, and she can be freed if the devourer is forced out. The **Trades Ward** page has the bench where she sits."
> — `campaign/gazetteer/waterdeep/dock-ward.md:166`

**Harper count (Factions Guide)**
> "Mirt wants Nihiloor dead — the mind flayer's intellect devourers have touched three Harper assets. He offers tactical support for the Xanathar lair heist if the party commits to eliminating Nihiloor. Nihiloor always escapes, so the support rests on a real attempt, not a kill."
> — `campaign/guides/factions/02-harpers.md:31`

### A7. Possessions and tools

**Adventure, the stone orb (Finding Floon sewer hideout; 5e)**
> "{@creature Nihiloor|WDH} carries a 3-inch-diameter stone orb carved to resemble an eyeball, similar to what one might see at the end of a beholder's eyestalk. This stone eye is the key to activating the magic portal in {@area Q11|089}. The mind flayer uses it to return to {@creature Xanathar|WDH}'s lair (described in chapter 5). It uses {@spell dominate monster} to control someone who gets in its way and turns any such individuals against their allies."
> — `sources/adventure-wdh.json:2815`

**Campaign, the portal activation (Q11, sewer hideout; the portal is a day-one object)**
> "**Activation:** Nihiloor's 3-inch stone orb, when pressed into the indentation, opens an opaque black doorway 8 feet tall and 4 feet wide in the south wall. The portal leads to area X22 of Xanathar's lair. Any creature that steps through appears in X22. It remains open for 1 minute after the orb is removed, then closes. It can't be held open by other means."
> — `campaign/locations/xanathar-sewer-hideout/q11-escape-portal.md:11`

**Adventure, the shackle key (area X24, 5e)**
> "{@creature Nihiloor|WDH} has a key that unlocks the chair's shackles. A character can unlock each shackle with a successful {@dc 15} Dexterity check using thieves' tools, and a creature shackled to the chair can slip free of these bonds with a successful {@dc 25} Dexterity (Sleight of Hand) check."
> — `sources/adventure-wdh.json:17781`

**Adventure, the pet (Finding Floon sewer hideout, 5e)**
> "The tentacled creature is {@creature Nihiloor|WDH} (see {@adventure appendix B|WDH|12}), a {@creature mind flayer} that is caressing an {@creature intellect devourer}. Upon seeing the adventurers, {@creature Nihiloor|WDH} rises from the stone chair, sets its pet down, and glides across the room, intending to leave through the double door in the west wall. The mind flayer expects {@creature Grum'shar|wdh} and the intellect devourer to cover its escape."
> — `sources/adventure-wdh.json:2814` (a Finding Floon scene; see E2)

### A8. Relations with other named figures

**Meloon Wardragon (adventure; the devourer's maker)**
> "The intellect devourer that inhabits Meloon's skull was bred by {@creature Nihiloor|WDH}, a mind flayer in {@creature Xanathar|WDH}'s employ. It knows everything Meloon knew, and Meloon behaves much as he did before his descent into Undermountain. He hangs out at the Yawning Portal, tries to bond with adventurers, and offers a helping hand whenever doing so feels appropriate. The intellect devourer's primary goals are to steer adventurers away from Undermountain and get them to undertake quests that further the aims of {@creature Xanathar|WDH}. Such quests usually involve the eradication of {@creature Xanathar|WDH}'s enemies, and Meloon is all too eager to fight alongside those who fall for his ruse."
> — `sources/adventure-wdh.json:32257` (for the occupation's date, see D8)

**Zaibon Kyszalt, a drow captive in X24 (adventure, 5e)**
> "The drow, Zaibon Kyszalt, was captured in Skullport and brought here for interrogation. His superior, Raelyn Auvryndar, was also captured and is confined in {@area X7|27e}. Zaibon wants to free her and escape into Undermountain, where House Auvryndar has outposts."
> — `sources/adventure-wdh.json:17780`
> "The mind flayer has telepathically interrogated Zaibon and learned about a House Auvryndar plot to conquer Skullport, as well as mounting tensions between the drow houses of Auvryndar and Freth. The mind flayer is getting ready to implant an intellect devourer in Zaibon's skull, then use him to undermine the drow plot and foment war between the drow houses. (Were Zaibon less useful, the mind flayer would have extracted his brain and turned it into an intellect devourer instead.) Zaibon knows nothing of the fate that awaits him."
> — `sources/adventure-wdh.json:17782`
> "- **House Auvryndar:** A low-ranking drow house from Menzoberranzan is slowly and secretly consolidating its power in Undermountain. Its invasion of Level 3 is meant as a first step toward taking Skullport. Dragon Heist holds two of its drow in Xanathar's lair, Zaibon Kyszalt, captured in Skullport, and his superior Raelyn Auvryndar, and **Nihiloor** has learned of the house's plot to conquer the town."
> — `campaign/setting/geography/undermountain-and-skullport.md:92` (setting page; present tense)

**Grum'shar, Q07 boss (Finding Floon sewer hideout, 5e)**
> "The boss of this hideout is a half-orc named {@creature Grum'shar|wdh}. When the characters arrive, {@creature Grum'shar|WDH} is interrogating {@creature Floon Blagmaar|WDH} in {@area Q7|081}. His display of torture techniques is a ploy to impress his other guest: a mind flayer named {@creature Nihiloor|WDH} (see {@adventure appendix B|WDH|12})."
> — `sources/adventure-wdh.json:2712`

**Thorvin Twinbeard (Harper informant inside the lair; quest-time routing)**
> "If the gazer is destroyed (13 HP, AC 13), Thorvin speaks openly for the first time. His relief is immediate and genuine. He confirms what the party may have begun to suspect: Nihiloor's domain (X23–X27) contains evidence that would change everything the party thinks they know about who has been running Xanathar's Guild."
> — `campaign/structure/arc-f-xanathars-lair.md:95` (quest-time; routed to Xanathar's Lair)

**Mirt and the Harpers (Faction Outposts briefing; quest-time routing)**
> "Full intelligence briefing. If Xanathar outposts were hit, Mirt asks specifically about Nihiloor references — the Harper file on the mind flayer is extensive, and any new document strengthens the case for Watch action. If Cassalanter outposts were hit and the party brings the Mirror of the Fiend sigil identification, the Cassalanter cult documents, or the cultists' testimony, Mirt's response is: relief, then urgency."
> — `campaign/structure/arc-e-faction-outposts.md:369` (rest of the passage covers the Cassalanter branch and Founders' Day)

**The Order of the Gauntlet (Savra)**
> "- **Xanathar's Guild (enemy):** The Order counts the Guild's use of intellect devourers and enslaved creatures as an abomination (Alexandrian remix, Appendix B). Guild dealers work the Field Ward, where the Order fills part of the gap the Watch leaves (**Field Ward**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:80`
> "| **Xanathar's Lair** | The Guild's use of intellect devourers is an abomination in Savra's theological framework. She asks the party to put Nihiloor down for good. Nihiloor always escapes, so she asks for the attempt and not the kill. A Whitehawk member also gets her lair support: she waits across from the guildsign entrance and fights beside the party if called, which spends the quest's one Marcheon operation. |"
> — `campaign/guides/factions/05-order-of-the-gauntlet.md:31`

**Force Grey (Vajra)**
> "**Grand Game goal:** The vault gold to the treasury. The pool, the placement records and the hosts already walking the city dealt with. The Splinter's arcane operations dismantled. The Stone of Golorr studied and understood before it's sealed away again. These are her priorities in order. Nihiloor always escapes the party, so she plans around him and not around his death. Her concern is which outcome leaves Waterdeep standing. The rest is scoring."
> — `campaign/guides/factions/06-force-grey.md:23`

**Dobb Ketterly (Guild courier to Nihiloor; quest-time routing)**
> "On Day 8 or 9 a Guild dockhand named Dobb Ketterly leaves word for Meloon, and the party can follow him home. On Day 10 at dusk he sits at Meloon's table and carries the report to Nihiloor."
> — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:43`

**Soluun Xibrindas (in the wing chair; quest-time routing)**
> "Soluun Xibrindas sits in the chair instead of Zaibon. He sold the Guild's divers the *Scarlet Marpenoth*'s berth, and once the deal was done the Guild seized him, because Nihiloor wants a host who knows how the company works. Soluun wears a silver disc on a cord and carries no weapons, and he speaks in short, hard sentences without naming Jarlaxle or Bregan D'aerthe. If any character is an elf or half-elf, he spits and says \"Surface-blood\" before anything else."
> — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:124`

**Captain Hyustus Staget (a Watch captain in X27 in the adventure; see D9)**
> "Imprisoned in the westernmost cell along the north wall is Hyustus Staget, a captain of the City Watch whom the characters have met (see \"The Watch Arrives\"). He was kidnapped while off duty and is without his armor and weapons. If Hyustus has died for whatever reason, replace him with a female human Watch officer named Cressa Galavarco (LG female Tethyrian {@creature veteran} with no armor or weapons). Whoever is here has a date with an intellect devourer."
> — `sources/adventure-wdh.json:17873`

**Davil Starsong (Doom Raiders; a day-one claim on another page)**
> "**Relationships.** Davil is the cell leader of the Doom Raiders (Waterdeep Zhentarim), the faction contact for Zhentarim-aligned PCs, a permanent resident at the Yawning Portal (second floor business room, third floor suite), a colleague of Istrid, Tashlyn, Ziraj, and the traitor Skeemo Weirdbottle, and the unknowing target of Nihiloor's intellect devourer, with Meloon watching him and waiting for a clean opportunity to kill him without witnesses."
> — `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:25`

**Nar'l Xibrindas, Ahmaergo, Noska Ur'gray:** no source names a tie between Nihiloor and any of them. The searches are listed under Not found.

**Other mind flayers (wiki; a different mind flayer, not Nihiloor)**
> "In [[1491 DR]], the Xanathar, in cahoots with the [[mind flayer]] [[Suthool]] and the agent of [[Asmodeus]] [[Belvarra Bowmantle]], supported the plots of the [[Masked Lord]] [[Braethan Cazondur]] in order to distract the [[City Watch (Waterdeep)|City Watch]] and the [[Open Lord]]s from its operation in [[Skullport]] and to gain power in order to expel the [[Zhentarim]] from [[Waterdeep]].<ref name=":0">{{Cite book/Death Masks|180-181}}</ref>"
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:484` (Death Masks pp.180-181; edition not printed)

### A9. The domination of Xanathar (facts only; both sides are in D1)

- Campaign claim, on the page: "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know." (`04-nihiloor.md:21`; section C, row 8c)
- Campaign date, derived: "- **About Uktar 1491 DR, Nihiloor.** Nihiloor begins to dominate Xanathar's mind, four months before Ches 1, 1492 DR by its Notable Figures page, and Xanathar does not know (**Nihiloor**). The month is derived by counting back from Ches 1." — `campaign/setting/organizations/08-xanathars-guild.md:24`
- No published-adventure line says Nihiloor controls Xanathar (search result in D1).

### A10. Faith and power source

No source gives Nihiloor a god, a rite or a shrine.

**Campaign, Ilsensine (setting page; it says no line ties Nihiloor to the god)**
> "- **Campaign ties:** One fresco in the **Vault of Dragons** structure document names Ilsensine. Nihiloor and the Undermountain mind flayers are the nearest, and no line ties either to Ilsensine. The GM Notes quote all three."
> — `campaign/setting/deities/ilsensine.md:59`
> "- **Never reveal:** That Nihiloor has dominated Xanathar for the last four months, or that intellect devourers occupy Waterdavians such as Meloon Wardragon, before the party's own evidence supports it. A player who asks about the Great Brain gets the Overview."
> — `campaign/setting/deities/ilsensine.md:60`

### A11. How long in post

- Wiki: "in the late 15{{th}} century [[DR]]" (`Nihiloor.txt:61`, see A1).
- Campaign: "four months" of domination (`campaign/setting/organizations/08-xanathars-guild.md:24` and `:103`; `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:26`).
- Campaign, the panopticus gift: "three years ago" (`campaign/structure/arc-f-xanathars-lair.md:15`).
- Campaign, the Watch and civic placements: "with two additional placements pending" (`campaign/structure/arc-f-xanathars-lair.md:176`). No dates for the placements.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page, summary line: "*Mind flayer, lawful evil, it/its*. Stat block: **Mind Flayer**." — `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:5`
- Guild page: "- **Nihiloor** (DH p. 213) — Mind flayer, lawful evil. Officially handles Xanathar's most sensitive intelligence operations." — `campaign/setting/organizations/08-xanathars-guild.md:103`
- Wiki: "| alignment5e    = [[Lawful evil]]" — `Nihiloor.txt:56`, with the citations "<ref name="WDH5e-p212" /><ref name="MM5e-p222">{{Cite book/Monster Manual 5th edition|222}}</ref>" at `Nihiloor.txt:59` (5e).
- Adventure: the Nihiloor entry has no alignment line. Its only game-statistics line is "{@creature Nihiloor|WDH} is a {@creature mind flayer}." — `sources/adventure-wdh.json:32361`.

**Species**
- Page: "mind flayer" (summary line 5, `04-nihiloor.md:5`).
- Adventure: "{@creature Nihiloor|WDH} is a {@creature mind flayer}." — `sources/adventure-wdh.json:32361`.
- Wiki: "| race           = [[Mind flayer]]<ref name="WDH5e-p212" />" — `Nihiloor.txt:13`.

**Pronouns** (the page says it/its; the other sources are split; see D2)
- Page: "*Mind flayer, lawful evil, it/its*." — `04-nihiloor.md:5`
- Voice profile: "It speaks telepathically, a cold, clear, sexless presence inside the listener's head, perfectly calm, and accompanied by a faint pressure behind the eyes." — `.claude/skills/character-voices/voices/xanathars-guild.md:68`
- Adventure, "it": "The mind flayer uses it to return to {@creature Xanathar|WDH}'s lair (described in chapter 5)." — `sources/adventure-wdh.json:2815`; "It has no interest in supplanting the beholder, however, preferring to operate in the shadows and pursue its own fell schemes." — `:32354`.
- Adventure, "his": "After devouring their brains, the mind flayer gives their corpses to his kuo-toa thralls to eat." — `sources/adventure-wdh.json:17827`; "uses this prison to confine potential hosts for his brood of intellect devourers" — `:17857`.
- Campaign quest files, "it": "The moment it sees the party, it rises, sets the intellect devourer down (now loose and hostile), and glides toward the western double door, heading for Q11." — `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:69`; "The moment Nihiloor sees the party, it rises. It sets the intellect devourer down." — `campaign/locations/xanathar-sewer-hideout/q07-boss-chamber.md:21`; "A mind flayer stands beside the basin with a small grey devourer on its shoulder, and it does not turn as you step through the door." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:151`
- Campaign quest files, "he": "By default Nihiloor is in X26 at the Puppet device, with the pet on the Pool's rim. When the wing wakes, he comes into X25 with the thralls behind him." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:139`; "On his way out he sacrifices the pet, wakes the Guild at the wing door and enters the tunnel toward X4." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/overview.md:43`; a line of Vajra's dialogue: "He's a mind flayer who has been using this city as a fucking hatchery, but he doesn't stand and die for his work. The pool is the mission, so if he runs, let him run." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-01-the-brief.md:69`
- Appendix C, "it": "It does not want to fight. It wants to leave." — `sources/Appendix_C_-_Player_Faction_Missions.md:1898`

**Stat block**
- Page: "Stat block: **Mind Flayer**." — `04-nihiloor.md:5`
- Adventure: the heading "Mind Flayer" sits in the X26 description, `"name": "Mind Flayer",` page 111, id "2ad" — `sources/adventure-wdh.json:17787`. Its text: "If the characters haven't already dealt with {@creature Nihiloor|WDH}, the mind flayer interrupts as they interact with Zaibon, entering from {@area X26|2b1} with an {@creature intellect devourer} in its hands." — `:17791`.
- Appendix C: "**Nihiloor** (**Mind Flayer**, 2024 *Monster Manual*). It does not want to fight. It wants to leave. Its first priority is escape, not victory." — `sources/Appendix_C_-_Player_Faction_Missions.md:1898`. Tactical note: "**Nihiloor** (2024 *Monster Manual*): AC 15, HP 71, Speed 30 ft." — `:1906`.
- Force Grey mechanics: "Nihiloor uses the boss block in section 4.1 of the **Force Grey Mechanics Reference**. The pet is the **Occupying Devourer** from section 5.1 of the **Harpers Mechanics Reference**, and the thralls are **Tough**. Use the row for the party's size." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:157`
- Alexandrian Lair stat reference (printed p.91 [PDF p.9]) [image transcription]: it lists Ahmaergo, Flutterfoot Zipswiggle, Thorvin Twinbeard, N'arl Xibrindas, Noska Ur'gray and Ott Steeltoes, and has no Nihiloor line.
- Wiki: "| challenge5e    = 7" — `Nihiloor.txt:57` (5e).
- Campaign, CR in the sewer hideout: "Nihiloor (mind flayer, CR 7) flees on party arrival — doesn't fight except to dominate a creature blocking its escape path." — `campaign/locations/xanathar-sewer-hideout/area-overview.md:55`

**Page number**
- The adventure entry is "page": 212 (`sources/adventure-wdh.json:32340`). The Guild page says "(DH p. 213)" (`08-xanathars-guild.md:103`). The wiki cites WDH5e-p212 (`Nihiloor.txt:61`). See D3.

---

## C. Every sentence on the current page

Status key: "Day-one" = no quest gate needed. "Quest-time" = narrates a mission, a rescue, or a quest event. "Contested" = depends on the domination question in D1. "Timing" = depends on the Meloon date in D8.

| Row | Line | Exact sentence(s) from the page | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Mind flayer, lawful evil, it/its*. Stat block: **Mind Flayer**." | Day-one. Pronouns split (D2). | `08-xanathars-guild.md:103`; `adventure-wdh.json:32361`; `Nihiloor.txt:56` |
| 2 | L6 | "**Affiliation:** Xanathar's Guild" | Day-one | `adventure-wdh.json:32353` ("works for Xanathar"); `08-xanathars-guild.md:103` |
| 3 | L7 | "**Featured in:** **Finding Floon**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **The Trouble with Meloon**, **Destroy the Intellect Factory**" | Quest references. "Faction Outposts" has no Nihiloor scene in `arc-e` (its only Nihiloor line is the Mirt briefing, `arc-e-faction-outposts.md:369`), and none in the Faction Outposts PDFs. Route. | See E2 |
| 4 | L11 | "**Resonance.** Nihiloor should inspire visceral horror with its alien otherness, intellectual dread when the party learns how many people it has compromised, and helpless rage at the knowledge that it has bent Xanathar to its will and the beholder has no idea." | Mixed. "alien otherness" rests on "an alien mind" (`adventure-wdh.json:32354`). "when the party learns how many people it has compromised" is a play reveal. "bent Xanathar to its will and the beholder has no idea" is the contested domination (D1). | D1 |
| 5 | L13 | "**Emotions.** Nihiloor most often feels cold intellectual curiosity, alien satisfaction at its creations, patient derision for non-psionic minds, possessive pride in its intellect devourers, detached amusement at humanoid politics, and a complete absence of anything recognizable as empathy." | Day-one character state; no event. Nearest profile lines: "Detached amusement at politics shows as questions about why they bother." (`xanathars-guild.md:72`) and "Its intellect devourers are "my children"." (`xanathars-guild.md:70`). | Profile, section C2 |
| 6 | L15 | "**Motivations.** Nihiloor wants to breed and deploy intellect devourers throughout Waterdeep, pursue its own fell schemes independent of Xanathar's goals, and observe the Grand Game from within the shadows where no one looks." | Day-one. "pursue its own fell schemes" is in `adventure-wdh.json:32354`. "independent of Xanathar's goals" is the campaign's domination claim (D1). "observe the Grand Game" has no source (F). | `08-xanathars-guild.md:75` (breeding); `:32354`; D1 |
| 7 | L17 | "**Inspirations.** When playing Nihiloor, channel HAL 9000 (*2001: A Space Odyssey*), Hannibal Lecter (*Silence of the Lambs*), and the Borg Queen (*Star Trek*)." | Not a fact | n/a |
| 8a | L21 | "**Persona.** To the world, Nihiloor is Xanathar's mind flayer operative." | Day-one | `adventure-wdh.json:32353` |
| 8b | L21 | "To Xanathar, it is a trusted mind flayer operative with a status no other Guild member holds." | Day-one claim, campaign only. The Villains table gives "Trusted intelligence gatherer; Xanathar grants it unusual autonomy" (`xanathar.md:49`). No published rank source (F). | `campaign/setting/villains/xanathar.md:49`; D1 |
| 8c | L21 | "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know." | Contested (D1). Campaign-only; no published line. | `08-xanathars-guild.md:103`; `xanathar.md:55`; `arc-f-xanathars-lair.md:408`; D1 |
| 8d | L21 | "It breeds intellect devourers, sets them loose in the sewers, and uses them to occupy Waterdavians, who walk the city with their own brains intact and a devourer steering them." | Day-one for the breeding and the sewers. "brains intact" is the campaign's custom device (`harpers/m05 design-notes.md:9`); the published brine transforms brains (`adventure-wdh.json:17847`). See D7. | `adventure-wdh.json:32353`; `08-xanathars-guild.md:75` |
| 8e | L21 | "Its methods leave little behind for PCs to question." | No source (design sentence). | F |
| 8f | L21 | "Meloon Wardragon and Watch clerk Orvyn Dall are among its current hosts." | Timing (D8). Meloon's occupation is dated after the Field of Triumph, a Trollskull Alley event, by `history/08-the-players-arrive.md:138`, so it is not a Ches 1 fact by that ruling. Orvyn's date is a gazetteer present tense (`trades-ward.md:99`) that the Force Grey design notes leave for the mission to fix (`m04 design-notes.md:21`). Route or restate. | D8 |
| 9a | L23 | "In a fight, Nihiloor would use Dominate Monster on the most dangerous combatant, command its intellect devourers to attack, and retreat when threatened." | Day-one combat behaviour, but "retreat" conflicts with the X26 text (D4). | `adventure-wdh.json:2815` ("dominate monster"); `:17848` (the mind flayer "stays behind"); Appendix C `:1898` ("Dominate Monster if cornered") |
| 9b | L23 | "In **Destroy the Intellect Factory** it always escapes toward the rest of the lair and is never killed there." | Quest-time. Routed to the Force Grey mission. | `m04 ev-02-nihiloors-wing.md:18` ("he is never killed here, so **Nihiloor Fled** is always marked"); `06-force-grey.md:73` |
| 9c | L23 | "It caresses an intellect devourer like a pet as it glides away." | Quest-time (the Finding Floon Q07 scene). | `ev-04-xanathar-sewer-hideout.md:67`, `:69`; `adventure-wdh.json:2814` |
| 10a | L25 | "**Relationships.** Nihiloor is the intelligence and infiltration specialist of Xanathar's Guild," | Day-one. "intelligence" is sourced at `08-xanathars-guild.md:103` ("Officially handles Xanathar's most sensitive intelligence operations"). "infiltration specialist" has no source line; the Guild's project is "The Infiltration" (`08-xanathars-guild.md:103`). | `08-xanathars-guild.md:103`; `xanathar.md:49` |
| 10b | L25 | "the creator of the intellect devourer that occupies Meloon Wardragon," | Timing (D8). The adventure says "was bred by" (`adventure-wdh.json:32257`). The Guild bullet says "An intellect devourer bred by Nihiloor rides Meloon Wardragon" (`08-xanathars-guild.md:89`), which is also a day-one present tense. | D8 |
| 10c | L25 | "and a mind flayer that has dominated Xanathar's mind for the last four months in a Guild where even a hint of that would get anyone else disintegrated." | Domination is contested (D1). "disintegrated" has no source. The only disintegration in the published text is Ott's plea at `adventure-wdh.json:17621`, and no source gives the Guild a rule of disintegrating members (F). | D1; F |
| 11a | L29 | "Nihiloor is the intelligence operative of Xanathar's Guild — a mind flayer who moves through the lair with unsettling calm, treating every conversation as an opportunity for study." | The first clause is day-one (`08-xanathars-guild.md:103`). "moves through the lair with unsettling calm, treating every conversation as an opportunity for study" has no source line. The nearest profile line is "It asks questions as though taking notes, and never uses a contraction or a filler." (`xanathars-guild.md:69`). | F |
| 11b | L29 | "The Guild's other members give it wide berth." | Partly sourced: "Virtually all of the Xanatharians steer clear of the mind flayer's demesne (X23-X27)." (Lair PDF printed p.91 [PDF p.9], [image transcription]). | Lair PDF p.91 |

**Quest-time and timing rows, for the drafter's Routed list:** row 3 (Featured in), row 8f (Meloon and Orvyn; timing), row 9b (Destroy the Intellect Factory), row 9c (the Q07 caress), and row 4 (the "when the party learns" clause). Row 8c and row 10c are contested by D1, not quest-time.

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
- Quest-time clauses in the profile: none found. Each sample line is speech, and none narrates a mission, a rescue, or an Event Outcome. "The beholder's gold is irrelevant" touches the vault, a Villains-page goal (`campaign/setting/villains/xanathar.md:61`), not a quest event.
- Pronoun in the profile: "sexless presence" (line 68) and "it" throughout. This matches the page's it/its.
- Profile line 70, "Its intellect devourers are 'my children'.", has no source line. It is a voice choice.
- The profile's speech calls Xanathar "the beholder", which fits Ruling 16.

---

## D. Conflicts

### D1. Does Nihiloor dominate Xanathar? (open; both sides quoted; not settled here)

Four pages mark the question "left open". Quoted:

> "- **Left open (brief ruling 14), none settled here:** Nihiloor's domination of Xanathar, Nar'l's tenure, Ott Steeltoes, the "something vast and dreaming" seed and the Doom Raiders and Enclave Trades Ward lines are not touched. The page says only that Nar'l reports to Jarlaxle by *sending* spell."
> — `campaign/setting/the-grand-game/the-grand-game.md:91`

> "- **Left open (brief call 13):** Nihiloor's domination of Xanathar, Nar'l Xibrindas's tenure, Ott Steeltoes, the "something vast and dreaming" seed, and the Doom Raiders and Enclave Trades Ward lines. None is stated on this page."
> — `campaign/setting/villains/manshoon.md:139`

> "- **Calls applied:** Left open per ruling 13: Nar'l's tenure (the page gives none), Nihiloor's domination of Xanathar, Ott Steeltoes and the Doom Raiders and Enclave Trades Ward lines."
> — `campaign/setting/villains/jarlaxle.md:179`

> "- **Left open (brief ruling 14), none settled here:** Nihiloor's domination of Xanathar does not change the Xanathar row. Nar'l's tenure is given as one year in `history/03-bregan-daerthes-long-road.md:161` and differently elsewhere, and the row does not state it. Ott Steeltoes put Eye #1 in the bowl (`arc-f-xanathars-lair.md:368`, `lore/stone-of-golorr-and-the-eyes.md:41`), and the page does not name him. The \"something vast and dreaming\" seed and the Doom Raiders and Enclave Trades Ward lines are not touched on this page."
> — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:101`

**Side one: the campaign says it is dominated**

> "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know. It breeds intellect devourers, sets them loose in the sewers, and uses them to occupy Waterdavians, who walk the city with their own brains intact and a devourer steering them. Its methods leave little behind for PCs to question. Meloon Wardragon and Watch clerk Orvyn Dall are among its current hosts."
> — `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:21` (the Persona paragraph, in full; its opening sentences are "To the world, Nihiloor is Xanathar's mind flayer operative. To Xanathar, it is a trusted mind flayer operative with a status no other Guild member holds.")

> "- **The Puppet** — Nihiloor has been exerting psionic domination over Xanathar itself for the past four months, replacing its strategic decisions while leaving its personality intact."
> — `campaign/setting/organizations/08-xanathars-guild.md:103` (the item sits inside the full bullet quoted in A1)

> "- **About Uktar 1491 DR, Nihiloor.** Nihiloor begins to dominate Xanathar's mind, four months before Ches 1, 1492 DR by its Notable Figures page, and Xanathar does not know (**Nihiloor**). The month is derived by counting back from Ches 1."
> — `campaign/setting/organizations/08-xanathars-guild.md:24`

> "> - **The puppet:** Nihiloor has dominated Xanathar for the last four months, and Xanathar does not know. The Xanathar that Waterdeep fears has been Nihiloor's instrument for that time, including the one that killed Manshoon's envoys."
> — `campaign/setting/organizations/08-xanathars-guild.md:129` (Secret callout)

> "- Nihiloor, the mind flayer, has been psionically dominating Xanathar for the last four months. The Xanathar that the party meets, including the one who killed Manshoon's envoys and sent response teams against the party's allies, has been Nihiloor's instrument. Xanathar does not know."
> — `campaign/setting/history/02-the-long-shadow.md:80` (Secret callout)

> "- Nihiloor has been psionically dominating Xanathar for four months, so some decisions attributed to Xanathar are Nihiloor's (**Xanathar's Lair** structure notes, and the **Xanathar's Guild** organization page)."
> — `campaign/setting/villains/xanathar.md:55`

> "| Nihiloor | Mind flayer operative | Trusted intelligence gatherer; Xanathar grants it unusual autonomy; plant for Mad Mage integration |"
> — `campaign/setting/villains/xanathar.md:49` (the Relationships table, kept verbatim; the Villains page says "unusual autonomy", not domination)

> "> - **Conflicts:** The Relationships table (kept verbatim) calls Nihiloor a trusted gatherer with unusual autonomy, but the relationship notes say Nihiloor has dominated Xanathar for four months. `arc-f` line 408 says every decision attributed to the beholder was Nihiloor's, which is not yet reflected here. `04-nihiloor.md` lines 22 and 26 say Nihiloor has no interest in supplanting Xanathar, and the current page does not say it."
> — `campaign/setting/villains/xanathar.md:105` (stale; see E1)

> "- **Relationships.** Xanathar is the beholder crime lord of Xanathar's Guild, the employer of Ahmaergo (its majordomo), Nihiloor (its mind flayer, which has psionically dominated Xanathar for the last four months without Xanathar knowing), and Nar'l Xibrindas (its drow advisor, whom it does not yet know is Jarlaxle's spy). It has a healthy fear of Laeral Silverhand and spares those in her employ."
> — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:26`

> "The Puppet revelation is the most significant: Xanathar has been Nihiloor's instrument for four months. Every aggressive, paranoid, apparently irrational decision attributed to the beholder in **Faction Outposts** and this quest was Nihiloor's decision. This changes the party's understanding retroactively. The mastermind they've been treating as the main threat was itself controlled by something worse. The real threat from Xanathar's Guild faction was never Xanathar."
> — `campaign/structure/arc-f-xanathars-lair.md:408`

> "The party that destroys the lair is trading a faction they understand — paranoid, predictable, with known structures and exploitable NPCs — for an unknown quantity in Nihiloor, who is smarter than Xanathar, does not have Xanathar's attachment to a goldfish, and has been running the Guild in secret for months without anyone noticing."
> — `campaign/structure/arc-f-xanathars-lair.md:400`

> "Permanent consequences: the Guild is gone as an intelligence resource. The **Vault of Dragons** approach loses access to Guild knowledge and contacts. The Undermountain connection from X4 is sealed. The party trades a dangerous faction they can understand for an unconstrained Nihiloor operating below the city with no leash."
> — `campaign/structure/arc-f-xanathars-lair.md:113` (conditional on the lair's demolition, `:111`)

**Side two: the published adventure and the wiki say it has no interest in supplanting Xanathar, and a different mind flayer plans to make Xanathar a thrall**

> "{@creature Nihiloor|WDH} has an alien mind, and it considers itself {@creature Xanathar|WDH}'s equal. It has no interest in supplanting the beholder, however, preferring to operate in the shadows and pursue its own fell schemes."
> — `sources/adventure-wdh.json:32354`

> "The illithid had an alien mind, and it enjoyed scheming and plotting from the shadows. It considered itself Xanathar's equal but had no interest in supplanting the [[beholder]].<ref name="WDH5e-p212" />"
> — `Nihiloor.txt:64` (wiki, 5e citation)

> "{@creature Nihiloor|WDH} the mind flayer has carved out its own lair within {@creature Xanathar|WDH}'s lair (areas X23 through X26). If {@creature Nihiloor|WDH} is killed earlier in the adventure, replace it with a mind flayer named Qrr'zarq."
> — `sources/adventure-wdh.json:17802`
> "Qrr'zarq comes from a colony of mind flayers in Undermountain that wants to implant {@creature Xanathar|WDH} with an illithid tadpole and, through a magical process called ceremorphosis, turn the beholder into a thrall. Qrr'zarq is waiting for an opportunity to implant the tadpole while {@creature Xanathar|WDH} is alone and asleep. The mind flayer doesn't want adventurers to complicate or ruin its brilliant plan, which it keeps to itself. It offers to help characters who agree not to harm it or the beholder."
> — `sources/adventure-wdh.json:17803` (the replacement plan; the campaign does not use it)

**Search result:** a search of `sources/adventure-wdh.json` for "dominat", "mind control", "controls Xanathar", "trusted" and "advis" found no line that says Nihiloor controls or dominates Xanathar. The published text uses dominate monster on creatures only (`:2815`; Appendix C `:1898`).

**Rank note (not a decision):** campaign files outrank the published adventure. The campaign files state the domination as current fact on this page, the Guild page, the Villains relationship notes, the structure doc and the history Secret. Four pages mark it "left open" (quoted above). The orchestrator decides.

**Ilsensine page (spoiler limit; not a ruling):** `campaign/setting/deities/ilsensine.md:60` (quoted in A10) lists the domination as a "Never reveal" item.

### D2. Pronouns: "it/its" on the page, "he" and "his" in other sources

Quoted in B. The page's summary gives it/its. The campaign quest files (`ev-02-nihiloors-wing.md:139`, `m04 overview.md:43`) and the adventure (`:17827`) use "he" or "his". The brief says pronouns come from the existing page or the source and are never inferred. The orchestrator decides.

### D3. Dragon Heist page: 212 or 213

- Adventure: "page": 212 at `sources/adventure-wdh.json:32340`; the wiki cites "WDH5e-p212" at `Nihiloor.txt:61`.
- Guild page: "- **Nihiloor** (DH p. 213) — Mind flayer, lawful evil." — `campaign/setting/organizations/08-xanathars-guild.md:103`.
- Higher source: the adventure (published). The orchestrator decides.

### D4. Morale: "retreat when threatened" against the X26 fight and the Appendix C tactics

> "In a fight, Nihiloor would use Dominate Monster on the most dangerous combatant, command its intellect devourers to attack, and retreat when threatened." — `04-nihiloor.md:23`
> "{@creature Nihiloor|WDH} and the intellect devourers make their stand here. If the characters flee, the mind flayer sends the intellect devourers after them and stays behind." — `sources/adventure-wdh.json:17848`
> "{@creature Nihiloor|WDH} doesn't pursue anyone who flees, trusting that they won't get far." — `sources/adventure-wdh.json:17791`
> "Nihiloor's goal is exit, not victory. It spends each turn moving toward the door rather than maximizing combat effectiveness. Only block it entirely to force a fight." — `sources/Appendix_C_-_Player_Faction_Missions.md:1907`
> "The fight ends when Nihiloor leaves the wing or the party stops fighting. A party can end it without beating him by taking a second node quickly, because he runs when it falls." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:186`

The page's "retreat" fits the Appendix C and Force Grey texts. The adventure's X26 text has the mind flayer "stays behind" and "make their stand". Higher source: the adventure for the published room (X26); the campaign files for the Force Grey fight. The orchestrator decides.

### D5. The wing's room names and contents (X23 to X27)

| Source (rank) | X23 | X24 | X25 | X26 | X27 |
|---|---|---|---|---|---|
| Adventure, room headers (published; `adventure-wdh.json`) | "X23. Antechamber of Madness" (`:17709`) | "X24. Extraction Chamber" (`:17762`) | "X25. Food for Thought" (`:17808`) | "X26. Devourer Spawning Pool" (`:17835`) | "X27. Prison" (`:17853`) |
| Alexandrian Lair roster (printed p.89 [PDF p.7]) [image transcription] | "Area X23 – Antechamber of Madness" | "Area X24 – Extraction Chamber" | "Area X25 – Food for Thought" | "Area X26 – Spawning Pool" | "Area X27 – Nihiloor's Prison" |
| Appendix C Force Grey mission (quest text) | not named | "X24 (Extraction Chamber; Nihiloor, 50% chance; one drow prisoner)" | "X25 (Food for Thought)" | "X26 (Spawning Pool)" | not named |
| Campaign structure doc (`arc-f-xanathars-lair.md`) | "X23 — Competitive Intelligence Files." (`:175`) | "X24 — The Infiltration." (`:176`) | "X25 — The Experiments." (`:177`) | "X26 — The Puppet." (`:178`) | not named; the domain is "Areas X23–X27" (`:173`) |
| Campaign Force Grey wing (quest text) | "X23 holds Nihiloor's files" (`ev-02-nihiloors-wing.md:19`) | "X24 the placement records" (`:19`) | "X25 the Pool, the captive and twelve specimens" (`:19`) | "X26 the Puppet device" (`:19`) | not named |
| Force Grey mission overview (quest text) | "At X23 the party meets the first of four enthralled guards" (`m04 overview.md:35`) | "X24 holds the placement records, with Orvyn Dall's folio among four" (`:35`) | "X25 holds the pool, the twelve specimens, the pet and the captive" (`:35`) | "By default Nihiloor is in X26 at the Puppet device" (`ev-02:139`) | not named |

Campaign line in full, for the mission's own room map:
> "The wing is area X23 to X26 of **Xanathar's Lair**, and this mission adds three things to the rooms that quest already describes. The pool and the captive sit in X25 beside the twelve specimens, and the placement records lie in X24." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/overview.md:25`

Campaign design note, the lair's codes, in full:
> "The mission is now an objective inside **Xanathar's Lair**. **The Brief** is the Tower scene before the lair, and **Nihiloor's Wing** is a block the GM opens at X23. The wing uses only the lair's codes: X23 files, X24 placement records, X25 experiments, X26 the Puppet. The pool, the records and the captive are added to those rooms, and the Puppet device stays with the lair quest." — `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/design-notes.md:9`

Appendix C route, in full:
> "**The Route.** X1 → X2 (Watched Hall; beholder zombie + gas spores; the zombie reacts to movement, gas spores react to magic) → corridor through X22 → X24 (Extraction Chamber; Nihiloor, 50% chance; one drow prisoner) → X25 (Food for Thought) → X26 (Spawning Pool)." — `sources/Appendix_C_-_Player_Faction_Missions.md:1885`

Adventure-only details: the adventure puts Nihiloor's own lair in "areas X23 through X26" (`:17802`), and X27 is the prison "the mind flayer uses this prison" (`:17857`). The adventure's X23 guards are kuo-toa: "A {@creature kuo-toa whip} and six {@creature kuo-toa} guard the hall." (`:17717`). The campaign's X23 thrall is "an enthralled Guild soldier" (`ev-02:39`).

Higher source: the campaign structure doc (`arc-f`) for the lair's room roles; the adventure for the published room names. The Force Grey files use a third layout. The orchestrator decides.

### D6. The escape device: "orb" or "amulet"

- Adventure: "{@creature Nihiloor|WDH} carries a 3-inch-diameter stone orb carved to resemble an eyeball" (`sources/adventure-wdh.json:2815`); "If the stone eye in {@creature Nihiloor|WDH}'s possession is pressed into the circular indentation" (`:2896`).
- Alexandrian Lair PDF, printed p.85 [PDF p.3] [image transcription]: "If not, they could theoretically put the hideout under surveillance, ambush Nihiloor, and use his amulet to activate the portal and enter the lair."
- Campaign, Q11: "**Activation:** Nihiloor's 3-inch stone orb, when pressed into the indentation, ..." (`campaign/locations/xanathar-sewer-hideout/q11-escape-portal.md:11`, quoted in full in A7).
- Higher source: the campaign (orb). The Alexandrian "amulet" is an outlier.

### D7. How devourers take hosts, and what happens to the brain

- Adventure, puppet model: "Each intellect devourer attacks the first humanoid it encounters, using its victim as a puppet to spy on the city and relay information back to {@creature Nihiloor|WDH}." (`sources/adventure-wdh.json:32353`)
- Adventure, brine transforms brains: quoted in A3 (`:17847`).
- Campaign, custom "Occupying Devourer": "The devourer is a custom variant that keeps Corene's brain alive." (`campaign/quests/faction-events/harpers/m05-the-sleeping-asset/overview.md:25`)
- Campaign, Harper design note: "The 2024 intellect devourer eats the host's brain and only *Wish* restores it." (`campaign/quests/faction-events/harpers/m05-the-sleeping-asset/design-notes.md:9`)
- Campaign, Bregan D'aerthe mission: "A 2024 **Intellect Devourer** that takes a body consumes the host's brain, so each host died when it was taken, and nothing the party does can save it." (`campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:287`)
- Campaign, Force Grey design note: "The Notable Figures pages for Meloon and Nihiloor still say the devourer "ate his brain"." (`campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/design-notes.md:19`). The current Nihiloor page says "who walk the city with their own brains intact and a devourer steering them" (`04-nihiloor.md:21`). This note is stale for this page.
- Wiki, the goblins and bugbears: "some of whom were infected with [[intellect devourer]]s, presumably by Nihiloor." (`wiki.txt:106`). The Guild page says "Nihiloor has infected some of them with intellect devourers" (`08-xanathars-guild.md:45`), with no "presumably".

Higher source: the campaign's custom-devourer rules (`m05 overview.md:25`; `m05 design-notes.md:9`) for the mechanic. The brain-death line (`m03 ev-01:287`) is quest text about a standard 2024 devourer. The page's "brains intact" follows the campaign's custom device. The orchestrator decides.

### D8. When Meloon was taken, and by whose devourer (settled timing conflicts with the page)

- Settled by the user, the campaign timing: "**Settled by the user:** Meloon Wardragon's timing is deliberate. The published adventure has the devourer take him "several months ago" (`adventure-wdh.json` line 1548). The campaign has the party meet him as himself at the Field of Triumph (`trollskull-alley/ev-05-the-field-of-triumph.md` lines 10 and 54; `design-notes.md` line 35), so the devourer takes him after it, about three tendays before Day 1 of Force Grey Mission 3 (`m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md` line 18)." — `campaign/setting/history/08-the-players-arrive.md:138`
- The Field of Triumph is a Trollskull Alley event: "**Field of Triumph:** Nonlethal gladiatorial combat across four rounds. Final round opponent is Meloon Wardragon's Force Grey team." — `campaign/quests/act-i/trollskull-alley/overview.md:55`
- Campaign, Doom Raiders page's note: "`history/08-the-players-arrive.md` line 138 puts the intellect devourer's occupation after the Field of Triumph, so Meloon is himself on Ches 1." — `campaign/setting/organizations/06-doom-raiders.md:183`. This note reads the same timing as "Meloon is himself on Ches 1", and the Nihiloor page's Persona says the opposite.
- Adventure: "Three months ago, out of boredom, Meloon accompanied a fledgling band of adventurers on an expedition to Undermountain." (`sources/adventure-wdh.json:32256`); "An intellect devourer in league with {@creature Xanathar|WDH} ate Meloon's brain several months ago." (`sources/adventure-wdh.json:1548`); "The intellect devourer that inhabits Meloon's skull was bred by {@creature Nihiloor|WDH}, a mind flayer in {@creature Xanathar|WDH}'s employ." (`:32257`).
- Campaign, the Meloon page: "- **Affiliation:** Force Grey (occupied by a Xanathar's Guild intellect devourer after the Field of Triumph, about three tendays before the first day of the watch)" (`campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:6`).
- Campaign, Guild page: "An intellect devourer bred by Nihiloor rides Meloon Wardragon, a member of Force Grey, and steers adventurers away from Undermountain and toward the Guild's enemies (**Meloon Wardragon**; *Dragon Heist*, 5e)." (`campaign/setting/organizations/08-xanathars-guild.md:89`)
- Higher source: the campaign, by the settled ruling (`history/08:138`). The adventure's "Three months ago" and "in league with Xanathar" conflict with it. The Persona line (`04-nihiloor.md:21`) and the Relationships line (`:25`) present Meloon's devourer as current on Ches 1. The orchestrator decides.

### D9. Captain Hyustus Staget in the X27 prison

- Adventure: "Imprisoned in the westernmost cell along the north wall is Hyustus Staget, a captain of the City Watch whom the characters have met (see \"The Watch Arrives\")." (`sources/adventure-wdh.json:17873`)
- Campaign, Watch page: "The street war. Captain Hyustus Staget lets Xanathar's Guild and the Zhentarim wear each other down, and he will not send a force into the sewers after a suspected spy. No campaign event uses him." (`campaign/guides/factions/12-open-lords-watch.md:99`)
- Campaign, Guild page: "The Watch is called to the Guild's brawls with the Zhentarim in the Dock Ward and leaves the sewer lair alone, and Captain Staget reasons that the two may as well destroy each other" (`08-xanathars-guild.md:95`, full bullet in A6).
- Higher source: the campaign's Watch page says no event uses him. The adventure's X27 captive is a published fact that the campaign does not mention. The orchestrator decides.

### D10. Tense: wiki past tense against campaign present

- Wiki: "Nihiloor (...) was a [[mind flayer]] who worked for the [[Xanathar's Thieves' Guild]] in the late 15th century DR" (`Nihiloor.txt:61`).
- Campaign page: "*Mind flayer, lawful evil, it/its*." and "Nihiloor is the intelligence operative of Xanathar's Guild" (`04-nihiloor.md:29`).
- The wiki is last in rank. Its tense reflects its own citations.

### D11. The "something vast and dreaming" seed and who the dreamer is (Undermountain)

Mark: Undermountain. The seed is not Nihiloor's. It sits in the Xanathar's Lair structure doc, next to Nihiloor's domain. It is quoted because the caller asked.

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

Conflict, not settled: `arc-f:382` and `arc-f:266` do not name the dreamer. `arc-c:310`, `arc-d:378` and `stone-of-golorr-and-the-eyes.md:84` name Illuun, an aboleth on Level 4. The ilsensine page says the user ruled that "the seed stays unresolved and is deferred to the Undermountain pass" (`ilsensine.md:104`).

---

## E. Stale lines in other files (not edited), and routed references

### E1. Stale or wrong lines in other files

- `campaign/setting/villains/xanathar.md:105` says the Nihiloor page's lines 22 and 26 say "Nihiloor has no interest in supplanting Xanathar", and that "the current page does not say it." In the current Nihiloor page, the Persona is line 21, Morale line 23 and Relationships line 25, and none of them says "no interest in supplanting". The note is stale for the current file (quoted in D1).
- `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/design-notes.md:19` says the Nihiloor page still says the devourer "ate his brain". The current page says "with their own brains intact". Stale for this page (quoted in D7).
- `campaign/setting/history/02-the-long-shadow.md:80` (a setting page; quest-time phrasing): "The Xanathar that the party meets, including the one who killed Manshoon's envoys and sent response teams against the party's allies, has been Nihiloor's instrument." Ruling 1 applies to "the party meets" and "sent response teams against the party's allies".
- `campaign/gazetteer/waterdeep/dock-ward.md:110` (a gazetteer page; quest-time hook): "- Hook: in **Finding Floon**, Floon is held in the boss chamber at 1 hit point, and Nihiloor leaves through a stone portal at the far end before the party can engage it."
- `campaign/setting/geography/undermountain-and-skullport.md:107` (a setting page; quest-time, conditional on the lair's demolition): "- **Nihiloor and Level 17 (campaign only):** "Nihiloor was not in his domain at the time and escapes to Undermountain Level 17 with his three projects intact" (`campaign/structure/arc-f-xanathars-lair.md:111`). The published support is thin. Halaster worries that "the conflict between the githyanki on level 16 and the mind flayers on level 17 could spiral out of control" (`sources/adventure-wdmm.json:569`), and Level 17 is Seadeeps. The Level 17 text itself was not checked."
- `campaign/setting/deities/tymora.md:82` (a setting page; quest-time): "- **The occupation:** An intellect devourer from Xanathar's Guild takes his body and reports to the Guild through a courier. In the campaign it takes him after the Field of Triumph, about three tendays before the first day of the watch. The party can force it out in **The Trouble with Meloon**, and the real Meloon then remembers the occupation as a long dream."
- `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:26` (a Notable Figures page; states the domination as fact; the only other page with the claim): "**Relationships.** Xanathar is the beholder crime lord of Xanathar's Guild, the employer of Ahmaergo (its majordomo), Nihiloor (its mind flayer, which has psionically dominated Xanathar for the last four months without Xanathar knowing), and Nar'l Xibrindas (its drow advisor, whom it does not yet know is Jarlaxle's spy). It has a healthy fear of Laeral Silverhand and spares those in her employ."
- `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:6` and `campaign/setting/organizations/08-xanathars-guild.md:89` present Meloon's occupation as a Ches 1 state, which conflicts with `history/08-the-players-arrive.md:138` (D8).
- `campaign/setting/organizations/06-doom-raiders.md:183` reads the Meloon timing as Ches 1 (D8).
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:101`, `the-grand-game.md:91`, `villains/manshoon.md:139` and `villains/jarlaxle.md:179` are not stale. They are "left open" (D1).
- `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt` and other bundle copies were not compared for this page; they are snapshots.

### E2. Routed quest references (where the quest-time facts already live)

- **Finding Floon** (Q07 sewer hideout). `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:67`: "**Nihiloor** (mind flayer) is seated on a raised platform to the south, cradling an **intellect devourer**." Line `:69` (quoted in B). Line `:90`: "The party's encounter with Nihiloor is a sight-line. They see it rise, release the intellect devourer, and glide out of the room." Line `:107`: "- **Nihiloor Sighted** — mark when the party witnesses a mind flayer in the Guild's sewer cell. They don't yet know what it is. This Event Outcome pays off when the mind flayer's role in the Grand Game surfaces in **Xanathar's Lair**." Also `campaign/quests/act-i/finding-floon/overview.md:32` ("- **Nihiloor** (Xanathar's Guild / Undermountain) — partial; observed briefly in Q07 before escaping through the Q11 portal; does not engage the party") and `:44`.
- **Gralhund Villa** (aftermath). `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:110`: "**Emerald Enclave (Melannor).** Gralhund Villa sits over a minor ley line the Enclave monitors as part of Jeryth Phaulkon's aberrant-activity survey. Xanathar's Guild's presence in the neighborhood destabilized it over the past week in a way that correlates with Nihiloor's movements below the city. Melannor wants to know what the party observed. For the map." Line `:114`: "**Force Grey (Vajra).** A full operational debrief: which factions were present, where each one entered and exited, whether any Watch checkpoint in the surrounding blocks was compromised or unmanned during the raid, and any direct evidence of Nihiloor's involvement. Xanathar's Guild activity approaching a Watch checkpoint the Guild has never previously targeted is, in her judgment, a test. She wants to know if the test succeeded."
- **Faction Outposts**. `campaign/structure/arc-e-faction-outposts.md:369` (quoted in A8). No Nihiloor scene exists in `arc-e`.
- **Xanathar's Lair** (structure doc; unconverted). `campaign/structure/arc-f-xanathars-lair.md:15`, `:79`, `:95`, `:111`, `:113`, `:173` to `:178`, `:284`, `:298` ("- **Vajra:** "Tell me about the panopticus. All of it." She already suspects what Nihiloor might be doing. She needs specific evidence before bringing it to the Open Lord."), `:339`, `:340`, `:341`, `:344`, `:346`, `:400`, `:404` to `:410`.
- **The Trouble with Meloon** (Force Grey M3). `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:21` (A6), `:43` (A8), `:81` ("- **Nihiloor** (Xanathar's Guild): receives the reports and never appears."). `ev-02-the-extraction.md:260`: "- **Nihiloor Identified Party** — mark when the Day 5 conversation took place and the devourer was still in Meloon at dusk on Day 10; read by **Destroy the Intellect Factory** and **Xanathar's Lair** (unconverted)."
- **Destroy the Intellect Factory** (Force Grey M4). `m04-destroy-the-intellect-factory/overview.md:10`, `:17`, `:21`, `:25`, `:35`, `:41` to `:43`, `:61`, `:66`, `:72`, `:76`, `:80`; `ev-01-the-brief.md:17`, `:53`, `:67` to `:73`, `:96`, `:112` to `:128`; `ev-02-nihiloors-wing.md:10`, `:18` (C row 9b), `:22`, `:29`, `:42`, `:94`, `:139`, `:147`, `:151`, `:166`, `:170`, `:186`, `:200`, `:227`, `:261`, `:305`, `:316`, `:324` to `:328`; `design-notes.md:5`, `:9`, `:11`, `:15`.
  - `ev-02-nihiloors-wing.md:166`: "To begin, Nihiloor steps between the party and whichever of the four things they reach for first, and he never uses Withdraw while two or more of them remain. The players can see this, and it is the Tell."
  - `ev-02-nihiloors-wing.md:316`: "- **Nihiloor Fled** — mark whenever Nihiloor leaves the wing, which is always; read by **Xanathar's Lair** (unconverted) and **The Full Picture**."
  - `m04 overview.md:43`: "He stands between the party and whichever thing they reach for first, and he leaves when the second one falls. On his way out he sacrifices the pet, wakes the Guild at the wing door and enters the tunnel toward X4. The party can chase him, block him until he vanishes, or let him go."
- **The Legate's Eyes** (Force Grey M5). `m05-the-legates-eyes/overview.md:21`, `:27` (A6), `:65` ("- **Nihiloor** (Xanathar's Guild): receives the reports and never appears."). `m05-the-legates-eyes/ev-02-the-extraction.md:21`: "- The devourer reports to Nihiloor only through Dobb Ketterly. If the link dies, Nihiloor learns it within a day. If **Pool Destroyed** is marked, no replacement host arrives."
- **The Sleeping Asset** (Harper M5). `m05-the-sleeping-asset/overview.md:21`, `:25` (A3, D7), `:62` ("- **Nihiloor** (Xanathar's Guild): the mind flayer behind the devourer, who never appears."). `ev-02-the-extraction.md:150` (Corene's account: "the restricted deliveries all went to Nihiloor's rooms in the lair") and `:158`.
- **Factions Guide** (mechanics). `campaign/guides/factions/06-force-grey.md:23` (A8); `:30` ("| **Gralhund Villa** | Gralhund Villa had Xanathar's Guild activity in proximity to a Watch checkpoint the Guild hasn't previously approached. Vajra wants a full debrief. Specifically: any sign of Nihiloor's presence, any implanted citizens encountered, any evidence of coordination between the Guild and outside parties. |"); `:31` ("| **Xanathar's Lair** | Mission 4 is an additional objective inside **Xanathar's Lair**, played in Nihiloor's wing (X23 to X26). Vajra's brief fires when a Force Grey member with **M3 Complete** prepares for the lair. If the lair has already run, the brief becomes a short debrief at the Tower. |"); `:73` ("| **M3 Complete** plus **Xanathar's Lair** preparation, or Renown 8 | **Destroy the Intellect Factory** | An objective inside **Xanathar's Lair**, played in Nihiloor's wing. Destroy the pool that breeds Occupying Devourers, take the placement records and free the captive. Nihiloor always escapes. Vajra pays for any *raise dead* the work needs. | +3 |"); `:74` ("| Renown 10, 6th level | **The Legate's Eyes** | Three Watch magistrates have reversed rulings in the Guild's favour. Trace them to Orvyn Dall, an appeals clerk in a Trades Ward magistracy whose devourer reports through a Guild courier, and extract him without a Watch review. | +4 |").
  - `campaign/guides/factions/02-harpers.md:31` (A6); `:72` ("| 6th | **The Sleeping Asset** | Find and rescue Harper informant Corene Wyldath, missing three weeks from her post inside Xanathar's Dock Ward operation. An intellect devourer rides her. The members also expose the mole in the Harper records. | +4 |").
  - `campaign/guides/factions/05-order-of-the-gauntlet.md:31` (A8).
  - `campaign/guides/factions/09-xanathars-guild.md:72` (the escalation table: "| Suspicious | Gazer scouts; Nihiloor processes captured intelligence. First team (Gorath's duergar) deployed as a warning |").
  - `campaign/guides/factions/09-xanathars-guild.md:112` ("- Notable Figures: **Xanathar**, **Ahmaergo**, **Nar'l Xibrindas**, **Nihiloor**, **Noska Ur'gray**, **Gorath**, **Korgstrod Uxgulm**, **Keln Trigos**, **Grinda Garloth**").
- **Trollskull Alley patron** (tavern guide): `campaign/guides/trollskull-manor/08-notable-patrons.md:64`: "**Act II–III note:** By Act II, Meloon has been compromised by a Xanathar's Guild intellect devourer. The Meloon who visits during Act I is genuine. The one who arrives in Acts II–III may not be."
- **The wing's thralls** (Force Grey M4): `ev-02-nihiloors-wing.md:29`: "Nihiloor's wing is the only part of the lair the Guild avoids. Soldiers who draw a shift here ask to be moved within weeks, and none of them will say why."

### E3. Undermountain-marked items (not Ches 1 lore)

- Seadeeps colony: `campaign/setting/geography/undermountain-and-skullport.md:72` (A1); `sources/adventure-wdmm.json:24431` and `:46748` (A1).
- Escape to Level 17 (conditional on the lair's demolition): `campaign/structure/arc-f-xanathars-lair.md:111` ("Consequences: Xanathar is destroyed if present in the lair, or escapes through the Undermountain connection at X4 if the GM wants to preserve the thread. ... Nihiloor was not in his domain at the time and escapes to Undermountain Level 17 with his three projects intact."). `campaign/setting/deities/ilsensine.md:70`: "- **Nihiloor's escape to Level 17:** If Xanathar's lair is demolished, "Nihiloor was not in his domain at the time and escapes to Undermountain Level 17 with his three projects intact" (`campaign/structure/arc-f-xanathars-lair.md:111`; also `:284` and `:346`). This is the only campaign line that sends a mind flayer from the city to the colony below."
- Qrr'zarq replacement plan: `sources/adventure-wdh.json:17803` (adventure only; not in the campaign).
- The seed: `arc-f:382` and `arc-f:266` (D11).
- Ilsensine: `ilsensine.md:59` (A10).

---

## F. Gaps (what a Background would need that no source gives)

1. **Birth, origin, first arrival in the city.** No source. The wiki gives only "worked for the Xanathar's Thieves' Guild in the late 15th century DR" (`Nihiloor.txt:61`). Suggested handling: leave out, or say "No source records Nihiloor's origin." Do not invent.
2. **Date it began service with Xanathar.** Wiki only: "late 15th century DR" (`Nihiloor.txt:61`, 5e citation WDH5e-p212). Suggested: use the wiki phrase, tagged `[research: wiki, 5e]`.
3. **Rank in the Guild.** The ladder (`08-xanathars-guild.md:45`) does not place Nihiloor. Its office is "Officially handles Xanathar's most sensitive intelligence operations" (`08-xanathars-guild.md:103`). Suggested: use that sentence, not a rank.
4. **How it won Xanathar's trust.** No source. The Persona's "a status no other Guild member holds" has no published basis. Suggested: state the campaign line only, tagged `[research]` if used.
5. **The domination (D1).** Open. Suggested: state both sides as the Villains page does, or state the campaign claim with its source. Not a Background fact until the orchestrator rules.
6. **Seadeeps link.** The Key Members line says the three projects pay off in "the Seadeeps colony (Undermountain Level 17)" (`08-xanathars-guild.md:103`). No source says Nihiloor came from Seadeeps. Suggested: say the projects pay off in Seadeeps; do not say where Nihiloor was born.
7. **The custom devourer and the brine.** The brine process is published (`adventure-wdh.json:17847`). The campaign's custom "Occupying Devourer" has no origin text. Suggested: give the brine as the published method, tagged 5e.
8. **How it chooses hosts for the offices.** Published: "attacks the first humanoid it encounters" (`:32353`), and the captives fed to it (`:17827`). The placements in the Watch and civic posts are in `arc-f:176`, with no method. Suggested: say the placements are in its records (`arc-f:176`).
9. **Age, sex and body.** The page says "it/its" (L5). The voice profile says "sexless" (line 68). No age. Suggested: no age.
10. **Faith.** None (A10). Do not link to Ilsensine (`ilsensine.md:59`).
11. **Its quarters and sleeping.** Published: its lair "areas X23 through X26" (`:17802`). Campaign: "Nihiloor's Domain (Areas X23–X27)" (`arc-f:173`). Suggested: use the campaign range.
12. **Feelings about its own work.** The Emotions line is the page's own. No source.
13. **Relationship with Nar'l Xibrindas, Ahmaergo, Noska Ur'gray and Gorath.** No source connects Nihiloor to any of them (searched; see Not found).
14. **Why Xanathar trusts it.** No source.
15. **The panopticus gift date.** "three years ago" (`arc-f:15`) is the only date. The adventure does not date it.
16. **The Watch captain Staget in X27** (D9). The campaign has no X27 content. Suggested: leave out of Background.
17. **Other mind flayers in the Guild.** The wiki names Suthool in a 1491 DR alliance (`wiki.txt:484`). The campaign names no other mind flayer in the Guild. Suggested: do not use Suthool for Nihiloor.
18. **Stone orb origin.** Published: "3-inch-diameter stone orb carved to resemble an eyeball" (`:2815`). No maker. Suggested: state the orb, not its origin.
19. **Meloon's occupation date.** Settled as after the Field of Triumph (`history/08:138`), so the Background cannot say Meloon has been a host before Ches 1 unless the orchestrator rules otherwise (D8).

---

## Not found

Terms searched: "Nihiloor" (all case variants); "intellect devourer"; "mind flayer" and "Mind Flayer"; "dominat"; "mind control" and "controls Xanathar" (adventure); "trusted" and "advis" (adventure, for Xanathar's advisers); "Qrr", "tadpole" and "ceremorphosis" (campaign grep; the adventure lines were read directly); "Seadeeps" (both adventures and campaign); "Ilsensine"; "something vast", "dreaming"; "Hyustus", "Zaibon", "Grum'shar", "Suthool" (campaign and bundle grep); "Soluun" and "Dobb Ketterly" (read in the quest files).

Files searched:
- All of `campaign/` (Grep, content mode). No Nihiloor line in `campaign/setting/history/08-the-players-arrive.md` (checked by grep), `campaign/setting/lore/`, `campaign/setting/villains/jarlaxle.md` (only the "Left open" line `:179`), `campaign/setting/villains/manshoon.md` (only `:139`), `campaign/guides/factions/10-manshoons-zhentarim.md`, `campaign/guides/factions/04-emerald-enclave.md`, or `campaign/guides/gm-guide/running-the-villains.md` (only the response-team row at `:49`).
- Notable Figures: `campaign/setting/notable-figures/xanathars-guild/`: only `01-xanathar.md:26` and `04-nihiloor.md` itself name Nihiloor. The Ahmaergo, Nar'l, Noska, Thorvin, Gorath, Keln and Grinda pages do not name Nihiloor (folder grep).
- `campaign/structure/arc-e-faction-outposts.md`: only `:369`. `arc-g-cassalanter-villa.md:437`, `:501`, `arc-i-kolat-towers.md:61`, `:315`: X23 "Nihiloor's files" as a Kolat Towers clue (routed, not Background).
- `campaign/gazetteer/waterdeep/`: Dock Ward (`:110`, `:166`), Field Ward (`:84`), Trades Ward (`:85`, `:99`, `:134`, `:232`). No North Ward line.
- `campaign/locations/`: the Xanathar Sewer Hideout area overview and rooms Q07 and Q11.
- `campaign/quests/`: all event and mission files with a Nihiloor line (listed in E2).
- `sources/adventure-wdh.json`: all lines, by grep (listed where quoted above).
- `sources/adventure-wdmm.json`: "Seadeeps" (`:215`, `:18395`, `:24431`, `:24432`, `:44069`, `:46637`, `:46748`, `:46762`, `:48044`, `:48577`), "Nihiloor" (none), "Qrr" (none), "Ilsensine" (none). No Nihiloor line in the Undermountain text.
- `sources/SOURCE_GUIDE.md`: `:29` ("- **Chapter 5 — Spring Madness (Xanathar):** Full Xanathar's Lair keyed location (36 areas), ... Nihiloor, ..."), `:99`, `:109`, `:343`, `:397` ("- Nihiloor introduction: the mind flayer is present but not meant to be confronted. Escape, stealth, or distraction are the intended solutions.").
- `sources/Act_III_Arc_E.md`, `sources/Act_III_Arc_D.md`: no Nihiloor line.
- `sources/Appendix_B_-_Player_Factions.md`: `:939` (the Destroy the Intellect Factory row, quoted in B). No Nihiloor name in Appendix B.
- `sources/Appendix_C_-_Player_Faction_Missions.md`: `:1791`, `:1821`, `:1841`, `:1852`, `:1854`, `:1861`, `:1883`, `:1885`, `:1891` to `:1898`, `:1905` to `:1907`, `:1915`.
- `sources/Appendix_D_-_Running_the_Tavern.md`: no Nihiloor name.
- `sources/research/pass5-bundles/xanathars-guild/wiki.txt`: `:104`, `:106`, `:115`, `:484`, and `:984` to `:1046` (the linked page).
- `sources/research/pass3-bundles/` and `pass4-bundles/`: snapshots of the current files.
- The Alexandrian PDFs in Method (all pages read). The Stat Reference (printed p.91) has no Nihiloor entry. The Revelation List names Nihiloor at printed p.121 only.
- Faction Outposts PDF (`5. Faction Outposts.pdf`), PDF pp.1 to 13: no Nihiloor line. The Xanathar outposts at printed pp.42 to 44 name Keln Trigos, Grinda Garloth, Korgstrod Uxgulm and Ahmaergo, and no Nihiloor.

Not found (gaps for the drafter):
- Birth, origin, and first arrival in Waterdeep.
- The date of first service to Xanathar, and any date for the wing's construction.
- A rank or title for Nihiloor on the Guild's published ladder.
- Any source for Nihiloor's relation to Nar'l, Ahmaergo, Noska or Gorath.
- Any source for Nihiloor's worship, god, rite, shrine or clergy.
- Age, size, and the sex of the body (the page's "it/its" is the page's own).
- Any source for the Guild's rule that a hint of the domination would get members "disintegrated" (Relationships, row 10c).
- Any Nihiloor line in the Alexandrian Lair stat reference (printed p.91).
- A Nihiloor stat block in any 5e text beyond the Appendix C "2024 Monster Manual" line, the Force Grey section 4.1 reference, and the wiki's MM5e-p222 citation.

---

## Not readable

- No file failed to open. The Alexandrian PDFs were read as rendered images (no text layer in this session). Quotes marked `[image transcription]` need `pdftotext -layout` checks before prose use.
- `sources/Other remix files/*.docx`: not opened (the tools cannot read `.docx`). `SOURCE_GUIDE.md` lists the following files, and the campaign cites or describes one of them for Nihiloor:
  - "The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx" (`sources/SOURCE_GUIDE.md:695`). `campaign/setting/history/02-the-long-shadow.md:146` says: "The Waterdavian's Guide docx has Zushaxx plot with Nihiloor to kill Izulktur and gives Zushaxx an arrival in Skullport in 1205 DR as a slaver from the Graypeaks Hive (lines 455, 480-482). Neither is a campaign decision." That claim is not verified here. Name it for the orchestrator to extract.
  - "Meloon Wardragon NPC Guide.docx" (`sources/SOURCE_GUIDE.md:692`): "Meloon as a Force Grey contact; his mind-control situation (Ahghairon's Dragonward), morale, and redemption arc." It may give the devourer's origin and Meloon's date (D8). Name it for extraction.
  - "Davil and the Doom Raider Zhents + Elf Killer mission and more.docx" (`sources/SOURCE_GUIDE.md:688`). Davil's page (`doom-raiders/01-davil-starsong.md:25`) names Nihiloor's devourer. Name it for extraction if the drafter wants the Davil tie.

## Not run

- `voicecheck.py` was not run (research only).
- No file was written except this notes file. The page was not written.
