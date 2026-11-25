# Pass 6 research notes: Manshoon

Page: `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1-17 and the user rulings bind)
Faction organization page: `campaign/setting/organizations/09-manshoons-zhentarim.md`
Villains page: `campaign/setting/villains/manshoon.md` (owns phases, goals and relationships; its `## Background` starts at line 23)
Factions Guide page: `campaign/guides/factions/10-manshoons-zhentarim.md`
Voice profile: `.claude/skills/character-voices/voices/manshoons-zhentarim.md` (`### Manshoon` at line 8)
Shape model: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md` (the path given for this folder, `pass6/manshoons-zhentarim/06-ott-steeltoes.md`, does not exist; the Xanathar's Guild folder holds the pilot notes). Model Notable page read: `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md`. `09-grinda-garloth.md` was not opened.

## Method and caveats

- Campaign files: Read and Grep. Line numbers are the Read or Grep numbering. Grep lines marked `[Omitted long matching line]` were re-read with Read.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes; `{@creature ...}` and other tags are left as written. `sources/adventure-wdmm.json` for the Undermountain arm.
- Alexandrian PDFs: no shell, so `pdftotext` could not run. Quotes were transcribed from the rendered page images (Read with `pages`). Each is tagged **[PDF-IMAGE]** with the printed page and the PDF page in brackets. Check every one against `pdftotext -layout` before prose use.
- Wiki: the extract `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-manshoons-zhentarim/01-manshoon.txt` (cited `W:` with its line) and the Zhentarim page `sources/research/pass5-bundles/zhentarim/wiki.txt` (cited `W5:`). `sources/research/pass4-bundles/manshoon/wiki.txt` was grepped (hits at lines 80, 82 and 84 for Asmuth and Chess match the early-life passage at `W:78-82`), not re-read. Wiki citation keys print no edition on most lines; where a key names one it is given.
- Source rank: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## A. Background facts by theme

### A1. Origin, birth and home

Villains page (line 25, quoted in full):
> "- Manshoon was born in Zhentil Keep in 1229 DR and founded the Zhentarim, also called the Black Network, in 1261 DR (Forgotten Realms Wiki, citing *The Grand History of the Realms* and *Ruins of Zhentil Keep*; the wiki does not tag their editions). The published adventure calls the original "one of the founders", and the campaign keeps that wording (**The Founding of Chains**)." — `campaign/setting/villains/manshoon.md:25`

Wiki, birth and parents (edition not stated; citation key *The Grand History of the Realms* p.125):
> "Manshoon was born in Zhentil Keep in the {{YearlinkName|1229}},<ref name="GHotR-p125">{{Cite book/The Grand History of the Realms|125}}</ref> to [[Harlshoon]], the first lord of Zhentil Keep." — `W:78`

Wiki infobox:
> "| dob            = 1229" — `W:22`
> "| home           = [[Citadel of the Raven]], [[Moonsea]]" — `W:10`
> "| formerhomes    = [[Zhentil Keep]], [[Moonsea]]<ref name="Drag415.tMDoM">{{Cite dragon/415/History Check: The Many Deaths of Manshoon}}</ref>" — `W:11`
> "| titles         = " (blank) — `W:6`

Published adventure, the founder wording:
> "The original {@creature Manshoon|WDH} was one of the founders of the Zhentarim. Evil to the core, he made enemies all across Faerûn, including other powerful spellcasters such as Khelben Arunsun and Elminster. Fearing that he might be destroyed by his foes, {@creature Manshoon|WDH} magically crafted several clones-but a mishap caused all of them to be awakened at once, whereupon they tried to destroy one another in a series of conflicts that came to be known as the {@creature Manshoon|WDH} Wars." — `sources/adventure-wdh.json:32216`

Campaign history, the founder wording (settled by the user, Session 51):
> "- The published adventure calls Manshoon "one of the founders" of the Zhentarim (`adventure-wdh.json` lines 560 and 32216), and this page keeps that wording. The wiki calls him the founder." — `campaign/setting/history/04-the-founding-of-chains.md:31`

### A2. Family, childhood and early life (wiki only; no campaign or adventure source)

> "Manshoon, his brother [[Asmuth]]; and [[Chess]], the son of their father's chief rival, [[Calkontor]], were sent off together as [[adventurer]]s to prove themselves worthy of being lords like their fathers. While his sons were away, Harlshoon was poisoned by Calkontor, but, with his dying breaths, he threw Calkontor out of a tower window. The trio's fathers' places were usurped by a pair of opportunists, [[Theilon Greencloak]] and [[Ulsan Baneservant]], the deaths blamed on foreign assassins, while the unknowing lord-princes continued their adventures together.<ref name="RoZK-CB-p13">{{Cite book/Ruins of Zhentil Keep/Campaign Book|13-14}}</ref>" — `W:78` (citation key *Ruins of Zhentil Keep* Campaign Book pp.13-14; edition not stated)

> "Asmuth was blinded and Manshoon had one of his hands blown off when he carelessly grabbed for the sword. Chess saved both of their lives, and the three fled when the sword animated itself, appearing to attack the Harpers. They came across a party of other adventurers and murdered them all in their sleep. Manshoon recovered a [[wand]] and a [[spellbook]]. He traded the wand for his hand to be restored but kept the spellbook as he secretly planned to study [[the Art]], having been inspired by the magic of the sword." — `W:80` (same citation key as `W:78`)

> "Manshoon made sure his blind brother Asmuth fell off a bridge to his death before they returned to the keep where he and Chess planned to dispose of the usurpers." — `W:80`

> "However, unknown to him, Chess defected in exchange for his father's seat on the council. It was, however a double cross: Chess, Manshoon, and their childhood friend Fzoul Chembryl killed the usurper. They claimed their rightful council seats and supported Fzoul's rise through the ranks of the Banite priesthood." — `W:82`

Campaign, the Banite priest and the founding (no childhood link):
> "- Manshoon was born in Zhentil Keep in 1229 DR and became one of the city's lords. He founded the Zhentarim in 1261 DR, and the Banite priest Fzoul Chembryl joined him in 1263 DR." — `campaign/setting/history/04-the-founding-of-chains.md:30`

### A3. Founding the Zhentarim (1261 DR) and the faith question

> "Feeling exposed, Manshoon immediately set about creating a cabal of mages, his [[Black Cloaks]], to protect him, recruiting Fzoul early on. Not long afterward, in the {{YearlinkName|1261}}, he founded the Zhentarim. However, knowing the priests would obey Bane over anyone else and assuming the wizards were just as ambitious as he was, Manshoon held little trust for any of his new allies. He sent out spies and was determined to raise his powers in the arcane far above anyone else in Zhentil Keep." — `W:85`

> "However, in order to do this, Manshoon and his magelings had to pledge fealty to Bane, promising to lead the faith to even greater heights of power than the weakening High Imperceptor had." — `W:85`

> "In secret, Manshoon embarked on another plan for his organization. Having little interest in empire-building, he set his Zhentarim wizards the task of establishing trade routes between the Moonsea and the untapped markets of the [[Sword Coast]]." — `W:87`

> "During this period, Manshoon developed his ultimate insurance plan, the notorious ''[[stasis clone]]'' spell." — `W:87`

Pass5 Zhentarim page, founding (edition not stated):
> "The Zhentarim was founded in the {{YearlinkName|1261}}, by the power-hungry wizard Manshoon, the lord of Zhentil Keep, as a tool for his ambitions of expanding his realm of control." — `sources/research/pass5-bundles/zhentarim/wiki.txt:196`

Campaign, the cell's faith (the campaign gives no creed; the wiki's Bane link is `[research]` on the Org page):
> "The campaign files give the cell no creed, oath or rites. Amath Sercent keeps Yellowspire as a Banite cell that supports Manshoon's operations where they serve Bane's interests. The wiki says Manshoon and his magelings pledged fealty to Bane to win over the Banite priests, and it lists Bane as the Zhentarim's favored deity, formerly Cyric (Forgotten Realms Wiki, *Manshoon* and *Zhentarim*, edition not tagged). Nothing in the campaign makes Bane the faith of the cell as a whole." — `campaign/setting/organizations/09-manshoons-zhentarim.md:46` (the paragraph begins "**Doctrine and Rites:** `[research]`")

Wiki patron deity (1e source, infobox):
> "| patron deity   = [[Mystra]]<ref name="DMSotR-25">{{Cite book/Forgotten Realms Campaign Set/DM's Sourcebook of the Realms|25}}</ref>" — `W:18`

Campaign, the stasis clone (day-one):
> "- Manshoon built the stasis clone spell as insurance against his enemies. Over the years he died several times and returned in a new body." — `campaign/setting/history/04-the-founding-of-chains.md:42`

### A4. The clones, the 1370 DR death and the Manshoon Wars

Villains page, lines 27 and 28 (in full):
> "- In 1370 DR Fzoul Chembryl and Lord Orgauth killed him and found themselves facing a dozen or more clones. Each clone believed he was the real Manshoon and felt driven to kill the others, and the fights are the Manshoon Wars (Forgotten Realms Wiki, 3e *Forgotten Realms Campaign Setting* p. 283). The published adventure says a mishap woke every clone at once (5e *Waterdeep: Dragon Heist*)." — `campaign/setting/villains/manshoon.md:27`
> "- Three clones survived the wars. One rejoined the Zhentarim and conceded leadership to Fzoul, one became the vampire Orbakh in Westgate, and one took refuge in Undermountain with Halaster (Forgotten Realms Wiki, 3e *Forgotten Realms Campaign Setting* pp. 282-283). The published adventure agrees that at least three survive and says the clone now in Waterdeep is the one that hid in Undermountain (5e *Waterdeep: Dragon Heist*)." — `campaign/setting/villains/manshoon.md:28`

Campaign history (day-one, the clone wars and the survivor who took the Network):
> "- In 1370 DR Fzoul Chembryl and Lord Orgauth killed him and found themselves facing a dozen or more clones. Each clone believed he was the real Manshoon and felt driven to destroy the others. These fights are the Manshoon Wars." — `campaign/setting/history/04-the-founding-of-chains.md:43`
> "- Three clones survived. One rejoined the Zhentarim and conceded leadership to Fzoul, one became the vampire Orbakh in Westgate, and one took refuge in Undermountain with Halaster." — `campaign/setting/history/04-the-founding-of-chains.md:44`
> "- The Zhentarim outlasted the 1370 DR death. Fzoul led the Network after it, and one Manshoon clone served as a free agent under him." — `campaign/setting/history/04-the-founding-of-chains.md:48`
> "- The man in Waterdeep is "a clone of a clone". He claims to be the one true Manshoon, as every surviving clone does." — `campaign/setting/history/04-the-founding-of-chains.md:47`

Published adventure, the Waterdeep clone's account:
> "Now the original {@creature Manshoon|WDH} is dead, and it's widely believed that all his clones were destroyed as well. In fact, at least three are still alive. The one presently in Waterdeep escaped death by hiding out in Undermountain, where he eventually ran afoul of Halaster Blackcloak. After a brief spell duel, Halaster captured {@creature Manshoon|WDH} and amputated his left arm at the elbow for reasons unknown. {@creature Manshoon|WDH} escaped imprisonment and fled Undermountain, taking refuge in the city above. Attempts to magically regenerate his severed limb failed, forcing him to craft an artificial arm and hand for himself." — `sources/adventure-wdh.json:32217`

Wiki, 1370 DR and the clones (edition: 3e citation keys):
> "In the {{YearlinkName|1370}}, Manshoon was "slain" again by Fzoul and Lord [[Orgauth]], who then found themselves facing around a dozen clones that the wizard had created. Each of the clones was convinced that he was the real Manshoon and was inexplicably compelled to slay his rival clones. Most of these perished in the ensuing battles. The caches of magical items formerly hidden by Manshoon were scattered throughout the Realms." — `W:92`
> "Three clones, who mastered this killing compulsion by means of spells and devices, survived, with the one that returned to the Zhentarim appearing to be 'the' Manshoon." — `W:95`
> "One of the three remaining clones returned to the Zhentarim, conceding leadership to Fzoul and entering into some sort of accommodation with him." — `W:97`
> "The second clone assumed a position of power among the [[Night Masks]] of [[Westgate]], calling himself '''Orbakh'''<ref name="FRCS-p283" /> or '''Orlak II'''." — `W:99`
> "The third took refuge in [[Undermountain]] with [[Halaster]]." — `W:101`

Pass5 Zhentarim page (wiki, 3e key):
> "In the {{YearlinkName|1370}}, Fzoul and Lord [[Orgauth]] attacked and killed Manshoon. However, Manshoon lived on through clone bodies, many of whom fought and killed each other. Of these, one returned to the Zhentarim, conceded all leadership to Fzoul, and worked as an agent." — `sources/research/pass5-bundles/zhentarim/wiki.txt:224`
> "In the [[1383 DR|Year of the Vindicated Warrior, 1383 DR]], the [[Shadovar]] moved against Zhentil Keep during the [[Shadowbane War]], razing it along with the Citadel of the Raven, killing both Fzoul and the final clone of Manshoon, leaving only Darkhold left." — `sources/research/pass5-bundles/zhentarim/wiki.txt:234` (conflicts with the campaign; see D26)

Alexandrian, the surviving clone:
> "Most of Manshoon's clones were destroyed during the Manshoon Wars, but yet another has recently returned to Waterdeep (claiming, as they all do, to be the one true Manshoon)." — [PDF-IMAGE] `sources/1. The Villains.pdf`, book p.16 [PDF p.4 of 7], Zhentarim section

Wiki, the Waterdeep clone's account (not the campaign's; the campaign uses the adventure's):
> "The ancient archwizard had infiltrated Waterdeep years before and had been hiding out in [[Kolat Towers]] ever since, plotting to replace the [[City Watch (Waterdeep)|City Watch]] with Black Network mercenaries that were loyal to him alone and to rule Waterdeep as Wizard-King." — `W:123`

### A5. Halaster, the arm and the Undermountain clone

Villains page, line 29 (in full):
> "- Halaster Blackcloak captured the Undermountain clone after a brief spell duel and amputated his left arm at the elbow. Magic could not regrow it, so Manshoon crafted an artificial arm and hand for himself (5e *Waterdeep: Dragon Heist*). The severed forearm remains in Undermountain as an undead guardian (5e *Waterdeep: Dungeon of the Mad Mage*, area 1a)." — `campaign/setting/villains/manshoon.md:29`

Campaign, the clone's flight and Halaster (the Kolat Towers opener, in full):
> "The Manshoon who now occupies Kolat Towers is a clone of a clone — a body activated in Undermountain when the Manshoon before it died, as the clone network was designed to do. Halaster Blackcloak, who tolerated the clone for a time out of professional curiosity, eventually severed Manshoon's left arm at the elbow with a blade that prevented magical regrowth. The clone fled Undermountain carrying the staff of power he had smuggled in and arrived in Waterdeep to find the Kolat Towers abandoned, the force field still running on its original enchantment, and the amulet manufacture instructions in Duhlark's study. Manshoon needed a base. The towers were available." — `campaign/structure/arc-i-kolat-towers.md:13`

Undermountain, the arm (WDMM):
> "{@b Undead Guardian}. Floating in the middle of the room, 15 feet above the floor, is a man's withered left hand and forearm, severed at the elbow." — `sources/adventure-wdmm.json:26129`
> "The limb belonged to a human archmage named Manshoon—or, more precisely, to one of his clones. The clone challenged Halaster to a spell duel and lost more than just the contest. Halaster turned the limb into a guardian that attacks all intruders until the Mad Mage or a creature that looks like him waves it off. The limb has the statistics of an {@creature archmage}, with these changes:" — `sources/adventure-wdmm.json:26133`
> Level: `sources/adventure-wdmm.json:24359` is `"name": "Level 9: Dweomercore"`; `:26119` is `"name": "1a. Left Hand of Manshoon"`; the next level heading is `:27748` (`"name": "Level 10: Muiral's Gauntlet"`). Area 1a is on Level 9.
> "Manshoon's severed hand floats here as an undead guardian." — `campaign/setting/geography/undermountain-and-skullport.md:70` (table row "| 9 | Dweomercore |")

Wiki, the arm (for the arm's later state; campaign has no equivalent):
> "During the latter battle, Manshoon's left arm was severed and proved impossible to magically regenerate, forcing him to use a metal prosthetic instead, while the original was kept and reanimated by Halaster." — `W:123`

Notable, the arm as emotion (day-one):
> "**Emotions.** Manshoon most often feels cold patient calculation, contemptuous superiority, precise anger reserved for specific targets, possessive ambition, frustrated pride about his artificial arm, and the absolute certainty that he is the one true Manshoon." — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:14`

Voice profile (day-one manner):
> "His frustrated pride about the arm and Halaster surfaces as one clipped, bitter sentence, then composure again." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:15`
> "- **Quirks:** He flexes the artificial hand before a decision. He corrects small inaccuracies in what others say about him. He insists he is "the one Manshoon"." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:20`

### A6. Kolat Towers and the Southern Ward (the base, day-one)

Villains page (lines 31-32):
> "- Kolat Towers is a crumbling pair of towers in the Southern Ward, built by the Kolat brothers and abandoned years ago. A force field with the properties of a wall of force still surrounds them. Manshoon rarely leaves, and he uses a teleportation circle when he must, so nobody sees him enter or leave (5e *Waterdeep: Dragon Heist*; **Kolat Towers** quest opener)." — `campaign/setting/villains/manshoon.md:31`
> "- Neighbors can see the force field and the light of *continual flame* spells in the windows, and most believe the towers are abandoned or haunted by the Kolat brothers. Manshoon posts no visible guards because he wants that belief to hold (5e *Waterdeep: Dragon Heist*)." — `campaign/setting/villains/manshoon.md:32`

Published adventure:
> "{@creature Manshoon|WDH} took control of Kolat Towers, a crumbling residence in the Southern Ward that was abandoned years ago by the two wizards who built it. The edifice is surrounded by a magical barrier that has the properties of a wall of force. {@creature Manshoon|WDH} rarely leaves the towers and uses a teleportation circle when he must do so, and thus is never seen entering or leaving." — `sources/adventure-wdh.json:32218`
> "This dilapidated, two-towered edifice stands tall in the Southern Ward. Its neighbors are aware of the magical force field that surrounds it, and they can see light from {@spell continual flame} spells spilling out of the windows. Despite these persistent magical effects, most folk believe the structure is abandoned. Others think it's haunted by the ghosts of the Kolat brothers. They're wrong, of course." — `sources/adventure-wdh.json:26797`
> "{@creature Manshoon|WDH} posts no visible guards outside Kolat Towers, since he wants others to believe the site is abandoned. The evil wizard and his underlings come and go using teleportation circles inside the towers." — `sources/adventure-wdh.json:26798`

Published adventure, the Kolat history (conflicts with the campaign; see D5-D6):
> "Kolat Towers once belonged to two eccentric brothers, Duhlark and Alcedor Kolat. Both were wizards." — `sources/adventure-wdh.json:26863`
> "Duhlark's paranoia continued to grow, until he suspected Alcedor of selling their secrets. Alcedor left the towers, never to be heard from again, and Duhlark became a recluse who died in his own fortress." — `sources/adventure-wdh.json:26865`

Campaign opener, the brothers and the towers (in full):
> "Duhlark Kolat built the towers that bear his name during the late fourteenth century as an experiment in paranoid architecture. His brother Alcedor wanted a home; Duhlark wanted a fortress that could withstand siege, scrying, and betrayal from within. The result — two interconnected stone towers in the Southern Ward, linked by a bridge at the third floor and bound together by a force field that covered the entire structure from basement to roof — was more fortress than home. Alcedor moved in anyway. The force field admitted no one without a specially keyed amulet. Alcedor accepted this as the cost of living with his brother. He died in the towers in 1385 DR under circumstances that remain unclear. Duhlark survived him by nine years before being found dead in his study, apparently of old age, with the force field still running." — `campaign/structure/arc-i-kolat-towers.md:9`

Campaign, the Splinter's build (day-one):
> "He spent two years building the Splinter cell — the faction that bears his name but operates independently of the Zhentarim's surviving leadership. The structure is hub-and-spoke: Kolat Towers as the command center, with the Interrogation House in the North Ward and Yellowspire in the Castle Ward serving as field offices connected by teleportation circles. A pass-amulet system replaced the need for a trusted courier network; amulets could be revoked remotely, confiscating access without confrontation." — `campaign/structure/arc-i-kolat-towers.md:15`

Campaign, the sanctum (day-one):
> "- **The sanctum:** Behind the towers lies an extradimensional sanctum in a finite demiplane, which the original Manshoon created and his clones all know. A teleporter ring and the circle in the towers are the way in (*Dragon Heist*, 5e). Kaevja Cynavern watches the entrance and is Manshoon's early-warning mechanism, Havia Quickknife and Mookie Plush keep his audience chamber, and Yorn the Terror is the enforcer who maintains the household's fear of its master (**Kaevja Cynavern**; **Havia Quickknife**; **Mookie Plush**; **Yorn the Terror**)." — `campaign/setting/organizations/09-manshoons-zhentarim.md:55`
> Adventure, same sanctum: "{@creature Manshoon|WDH}'s extradimensional sanctum exists in a finite demiplane. Created by the original {@creature Manshoon|WDH}, it is known to the wizard's clones, and it currently serves as the lair of the clone described in this adventure." — `sources/adventure-wdh.json:28796`

Simulacrum (GM-only; keep out of the Overview):
> "The simulacrum in E7 is Manshoon's contingency against assassination. It was created seven years ago and has been ice-preserved since — a duplicate with half his hit points, none of his 6th-level or higher spell slots, and a different quality to its decision-making that those who know Manshoon well can identify after the fact. The simulacrum has never been activated outside of tests. Manshoon has never needed it. He is considering, for the first time in years, whether he might." — `campaign/structure/arc-i-kolat-towers.md:17`
> "{@creature Manshoon|WDH} can have only one simulacrum at any given time, and he uses it as a subordinate to command his Zhentarim minions in the field. If his simulacrum is destroyed, {@creature Manshoon|WDH} creates another. Each simulacrum has the statistics of {@creature Manshoon|WDH}, with these changes:" — `sources/adventure-wdh.json:32227`

### A7. The Splinter, the network and the Doom Raiders (day-one)

Villains page, lines 33-34:
> "- He spent about two years building the Splinter, a cell that bears his name and works independently of the Zhentarim's surviving leadership. It is hub and spoke, with Kolat Towers as the command center and the Interrogation House in the North Ward and Yellowspire in the Castle Ward as field offices linked by teleportation circles. A pass-amulet system lets him revoke anyone's access from the towers (**Kolat Towers** quest opener)." — `campaign/setting/villains/manshoon.md:33`
> "- He took a large part of the local network the Doom Raiders had built, and through it learned that Lord Neverember had used the local Zhentarim's resources to embezzle the vault's gold (Alexandrian Remix, *The Villains*, p. 16)." — `campaign/setting/villains/manshoon.md:34`

Alexandrian, the same network:
> "When he peeled off a large hunk of the local Zhentarim network that had been established by the Doom Raiders (see p. 198 of *Dragon Heist*), he became aware that Lord Neverember had used the local Zhentarim's resources to embezzle hundreds of thousands of gold dragons from the government." — [PDF-IMAGE] `sources/1. The Villains.pdf`, book p.16 [PDF p.4 of 7]

Alexandrian, Manshoon's inquiry:
> "Manshoon wanted to know where that money has gone. He knew that Neverever didn't actually have it in his possession, so he sent agents to infiltrate Neverember's household in Neverwinter to find out." — [PDF-IMAGE] book p.16 [PDF p.4 of 7] (transcription: the image reads "Neverember" in both places; check against pdftotext)

Published adventure, the cell's divisions:
> "The Zhentarim in Waterdeep is a fractured organization. Those who support {@creature Manshoon|WDH} want to destroy {@creature Xanathar|WDH} and seize political and economic control of the city. Those who oppose {@creature Manshoon|WDH} want to expose and destroy him before they are themselves apprehended or driven out of the city by the local authorities." — `sources/adventure-wdh.json:1445`
> "Adventurers can't join {@creature Manshoon|WDH}'s cause, but they can join and receive aid from the Zhents who are opposed to him." — `sources/adventure-wdh.json:1446` (the sentence continues in the same string about the Doom Raiders' leaders)

Campaign, the cell's view of the Doom Raiders (`[research]`):
> "- **The Doom Raiders Are Deserters:** The cell regards the Doom Raiders as deserters who stole its name `[research]`, will not cooperate with them, and works to dismantle their people and the network they built." — `campaign/setting/organizations/09-manshoons-zhentarim.md:45`

### A8. The Eyes, Xanathar and the envoys (pre-start; dates in the sources)

Villains page, lines 35-36 (in full; see C3 for the quest-adjacent part):
> "- His agents stole the Neverwinter Eye from the Protector's Enclave. His envoys brought it to Xanathar three months before the fireball, and Xanathar killed them and kept it as Eye #1 (**Running the Villains**; **The Long Shadow**)." — `campaign/setting/villains/manshoon.md:35`
> "- His cell then seized Renaer Neverember's mourning locket on the night before Ches 1 and pried it open at the Candle Lane warehouse. Xanathar's Guild raided the warehouse and carried the Eye off without knowing what it was, and Bregan D'aerthe agents inside Xanathar's hideout lifted it that night. It became Eye #3, and Manshoon holds no Eye (**Running the Villains**)." — `campaign/setting/villains/manshoon.md:36`

Campaign, the derived date of the envoys (pre-start):
> "- About Nightal 1491 DR (derived): the Neverwinter Eye passes from the Zhentarim to Xanathar when Xanathar kills Manshoon's envoys, three months before the fireball on Ches 22 (`arc-f-xanathars-lair.md` line 9; see **The Long Shadow**)." — `campaign/setting/history/06-the-open-lords-fall.md:135`

Campaign, the Eyes file:
> "**Manshoon:** He holds no Eye. He needs the Stone and all three Eyes, and his plan is to let someone else open the vault and then take it from them." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:44`
> "- **Eye #1, Xanathar:** Manshoon's Zhentarim stole it from the Protector's Enclave in Neverwinter. About three months before the fireball, Manshoon sent two lieutenants to Skullport with it as a gift. Xanathar ate them and kept the Eye, and Ott Steeltoes put it in the bowl of Sylgar, Xanathar's goldfish, because it was a pretty color. Xanathar does not know what the Eye is." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:40`

Campaign, Running the Villains:
> "**Eye #1** — formerly held by Manshoon's Zhentarim, who stole it from Protector's Enclave in Neverwinter. Xanathar killed the Zhentarim envoys who brought it to him and seized the Eye. It now resides in Xanathar's Lair sanctum." — `campaign/guides/gm-guide/running-the-villains.md:21`
> "> **Eye #3:** Jarlaxle Baenre — aboard the *Scarlet Marpenoth*. Jarlaxle knows exactly what it is. It passed from Renaer's locket to the Zhentarim, then to Xanathar's Guild in the warehouse raid, and Bregan D'aerthe agents inside Xanathar's hideout lifted it that night. Manshoon holds no Eye." — `campaign/guides/gm-guide/running-the-villains.md:30`

Alexandrian, the envoys (book p.15):
> "Then the Zhentarim came to him with one of the Eyes and said, "We have two different parts of this puzzle. We'd like to make a deal." Xanathar was enraged at both their presumption and his own folly, slew the Zhentarim envoys, and took the Eye they had brought to him." — [PDF-IMAGE] `sources/1. The Villains.pdf`, book p.15 [PDF p.3 of 7]

Published adventure, a different route for the Stone (conflict; see D8):
> "As Zhents loyal to {@creature Manshoon|WDH} try to forge an alliance with Xanathar, the Stone of Golorr is stolen." — `sources/adventure-wdh.json:838`

### A9. Blackmail and the Masked Lords (pre-start)

Villains page, line 37 (in full):
> "- He blackmails two Masked Lords. Corylus Thann is held over a scandal, and Jelenn Urmbrusk is held through a debt to a Splinter front, and their votes follow his preferences. The ledger documenting these arrangements lies in an arcane-locked drawer in his study, with a list of the Masked Lords whose identities he knows (**Kolat Towers** quest opener; 5e *Waterdeep: Dragon Heist*, which has Jelenn already in debt to him)." — `campaign/setting/villains/manshoon.md:37`

Campaign, the list of five and the two marked:
> "Manshoon keeps a list of five Masked Lords whose identities he knows. They are Mirt, Corylus Thann, Thardouk Starbuckler, Jelenn Urmbrusk and Dorgar Adarbrent, and he has checked off Corylus and Jelenn as the two he is blackmailing." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:63`
Adventure, the same list (check marks as printed):
> "Mirt" / "Corylus Thann √" / "Thardouk Starbuckler" / "Jelenn Urmbrusk √" / "Dorgar Adarbrent" — `sources/adventure-wdh.json:30308-30312`

Adventure, the ledger (GM):
> "Inside is a leather-bound ledger that provides a paper trail implicating {@creature Manshoon|WDH} in two blackmail schemes." — `sources/adventure-wdh.json:30290`
> "Corylus Thann, a racist Waterdavian noble, is paying the Zhentarim not to reveal that he hired Zhent thugs to assault non-humans." — `sources/adventure-wdh.json:30294`
> "Jelenn Urmbrusk, a Waterdavian noble, receives regular payments from the Zhentarim to offset monies he loses in bad investments." — `sources/adventure-wdh.json:30295`
> "Fear of that exposure led her to borrow money from the Zhentarim instead—a decision she has come to regret. The Zhents working for {@creature Manshoon|WDH} promise to keep their relationship secret on the condition that she do everything in her power to further the group's welfare in Waterdeep." — `sources/adventure-wdh.json:30374`

Campaign, Corylus and Jelenn (quest-structure doc; conflicts with the adventure; see D12-D13):
> "Corylus Thann, a Masked Lord, was photographed in a situation that would end his career; he supplies Guild intelligence in exchange for the ledger's continued privacy. Jelenn Urmbrusk accumulated significant debt to a Splinter front organization; her votes in the Council of Guildmasters follow Manshoon's preferences without her ever being asked directly." — `campaign/structure/arc-i-kolat-towers.md:19`
> "Jelenn's debt to Manshoon's Zhentarim was borrowed to avoid borrowing from rival nobles, and the Splinter now holds it." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:64`
> "The scandal is that Corylus once hired Zhentarim thugs to attack non-humans who sought political office, and the debt is a loan that Jelenn took from the Zhentarim because she feared the gossip a noble lender would cause (*Dragon Heist*, 5e)." — `campaign/setting/organizations/09-manshoons-zhentarim.md:67`

### A10. Goals and the published plan

Villains page, Goals (lines 80-82, in full):
> "- **Acquire the Stone of Golorr.** The Stone is a transformed aboleth encoded with ancient Weave knowledge, and Manshoon means to absorb the Weave and supplant Mystra. The vault's gold funds the process. Method: Stone recovery, then Weave absorption. He holds no Eye, because Xanathar killed the envoys who delivered Eye #1 as a gift and kept it, so he needs the Stone plus all three Eyes. Contingency: destroy the vault rather than cede it. Connects to **Gralhund Villa** and **Kolat Towers**." — `campaign/setting/villains/manshoon.md:80`
> "- **Control Waterdeep's Underworld.** He means to eliminate Xanathar, absorb the Doom Raiders and marginalize Bregan D'aerthe. Method: patient erosion through targeted disruption and strategic violence. The Dock Ward conflict in Acts I–II is this plan in early operation." — `campaign/setting/villains/manshoon.md:81`
> "- **Survive an Assassination.** The simulacrum is his contingency against assassination and his tactical decoy: it fights while he escapes. Defeating the Manshoon the party meets first may defeat only the simulacrum, and if it is destroyed he makes another. The stasis clone spell is a separate tool, his insurance against dying for good. Connects to the **Kolat Towers** design requirement." — `campaign/setting/villains/manshoon.md:82`

Campaign, the Weave goal in the Org and Notable pages (agree with the Villains page):
> "- **What Manshoon Wants:** The gold means nothing to him as wealth. He wants the Stone of Golorr for what it knows, because the Stone is a transformed aboleth and its centuries of absorbed memory encode ancient knowledge of the Weave's structure. Manshoon intends to use that knowledge to absorb the Weave and supplant Mystra, so the vault is an instrument and the Stone is the goal." — `campaign/setting/organizations/09-manshoons-zhentarim.md:65`
> "**Motivations.** Manshoon wants to acquire the Stone of Golorr for the ancient Weave knowledge encoded in its aboleth memory, use that knowledge to absorb the Weave and supplant Mystra, fund his preparations with the vault's gold, and deepen his hold over Masked Lords Corylus Thann and Jelenn Urmbrusk into a full Council majority." — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:16`
> "- **Manshoon's Zhentarim:** Manshoon wants the Stone for the ancient Weave knowledge in its aboleth memory. He means to use it to absorb the Weave and supplant **Mystra**, and the vault's gold pays for the preparations." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:101`

Published adventure, the published goal (conflict; see D11):
> "{@creature Manshoon|WDH} aims to rule Waterdeep and replace the City Watch with Black Network mercenaries that are loyal to him alone. By bribing and blackmailing the Masked Lords, he hopes to oust {@creature Laeral Silverhand|WDH} as Open Lord and take her place, kill the Blackstaff, reduce the Masked Lords to mere vassals, and declare himself the Wizard-King of Waterdeep. Once the city is firmly in his clutches, {@creature Manshoon|WDH} will then turn his attention toward Undermountain, destroy Halaster once and for all, and claim the dungeon's riches." — `sources/adventure-wdh.json:32219`
> "{@creature Manshoon|WDH} yearns to rule Waterdeep as a tyrant, take over the Zhentarim, and use both seats of power to plunder and control the Sword Coast." — `sources/adventure-wdh.json:26731`

Villains page, line 38 (acknowledges the difference):
> "- The published adventure gives him a different goal. He wants to oust Laeral Silverhand as Open Lord by bribing and blackmailing the Masked Lords, replace the City Watch with Black Network mercenaries, kill the Blackstaff, and then turn on Halaster (5e *Waterdeep: Dragon Heist*). The campaign's motive is the Weave goal under Goals, which comes from the campaign's own pages and has no published or Alexandrian source, and the blackmail of the Masked Lords stays." — `campaign/setting/villains/manshoon.md:38`

### A11. Enemies and the shadow he works in (day-one)

> "- He has a long list of powerful enemies, among them the Harpers, Elminster, Halaster and the Blackstaff. They would move against him if they learned he was in Waterdeep, so he operates in the shadows for now (5e *Waterdeep: Dragon Heist*)." — `campaign/setting/villains/manshoon.md:39`
> "A head-on battle with {@creature Manshoon|WDH} isn't likely to go well for the characters. That said, the wizard's greatest weakness is that he has powerful enemies in Waterdeep. The risk of exposure keeps him hidden, and the characters can thwart him by furnishing his enemies with proof that he's alive (after a fashion) and operating in Waterdeep." — `sources/adventure-wdh.json:26738`

### A12. Habits, objects and the sanctum (GM-level; day-one)

Adventure, the E12 quarters:
> "Sitting on the edge of the bed is a handsome young male human in elegant robes. Long black hair partially conceals his angelic face as he attaches a metal appendage to the withered stump of his left arm." — `sources/adventure-wdh.json:30250`
> "The handsome young figure is {@creature Manshoon|WDH} (see {@adventure appendix B|WDH|12}), who is much older than he looks." — `sources/adventure-wdh.json:30254`
> "If a fight breaks out, {@creature Manshoon|WDH} grabs his {@item staff of power} (which he hides under the bed) and holds his ground. For more information on how to play {@creature Manshoon|WDH}, see "Facing {@creature Manshoon|WDH}" at the beginning of this chapter." — `sources/adventure-wdh.json:30257`
> "The mask on the table is nonmagical, but {@creature Manshoon|WDH} likes to put it on before meeting with his followers." — `sources/adventure-wdh.json:30264`
> "The masks belong to {@creature Manshoon|WDH} and have been worn by him in the past. A {@spell detect magic} spell or similar magic reveals an aura of evocation magic around each one." — `sources/adventure-wdh.json:29981`
> "{@creature Manshoon|WDH} has amassed a sizable collection, including ten rare volumes he removed from Duhlark Kolat's collection." — `sources/adventure-wdh.json:30150`
> "In the other far corner, {@creature Manshoon|WDH}'s spellbook rests atop a black marble lectern protected by an {@condition invisible} {@creature helmed horror}." — `sources/adventure-wdh.json:30281`
> "This spellbook weighs 20 pounds and is covered in beholder hide. It contains all the spells {@creature Manshoon|WDH} has prepared (see {@adventure appendix B|WDH|12}) plus the following spells:" — `sources/adventure-wdh.json:30325` (the entry ends "Stealing or destroying this spellbook disrupts {@creature Manshoon|WDH}'s operation")
> "To access {@creature Manshoon|WDH}'s extraplanar sanctum, one needs a {@item teleporter ring|WDH}: a brass signet ring bearing a stylized M, and which emanates an aura of conjuration magic when targeted by a {@spell detect magic} spell or similar magic. {@creature Manshoon|WDH} gives these rings to his most trusted servants." — `sources/adventure-wdh.json:28822`

Adventure, Kaevja (recruitment):
> "Kaevja was a Red Wizard of Thay until she saw an opportunity to study magic under {@creature Manshoon|WDH}. Before he accepted her, {@creature Manshoon|WDH} forced her to remove her distinctive Thayan head tattoos and to trade in her Red Wizard robes for black ones." — `sources/adventure-wdh.json:29993`

Adventure, the Gondafrey cell:
> "{@creature Manshoon|WDH} is amused by the creature, so he keeps it alive but locked in the cell." — `sources/adventure-wdh.json:28504`

Adventure, followers as expendable:
> "This version of {@creature Manshoon|WDH} isn't spoiling for a fight. He commends the characters for making it this far and shows no concern for the Zhents they defeated to reach him, since he considers all his followers expendable." — `sources/adventure-wdh.json:30255`

Adventure, Duhlark's remains (Manshoon's handiwork; a bedroom):
> "{@creature Manshoon|WDH} found Duhlark Kolat's skeletal remains in the bed and transformed his skull into a flameskull. He left the rest of the bones alone, hidden behind cobwebs." — `sources/adventure-wdh.json:28680`

Adventure, apprentices:
> "The three wizards here are {@creature Manshoon|WDH}'s apprentices—Ered Payno (LE male Damaran human), Havi Termock (CE female Chondathan human), and Savara Firethorn (NE female Tethyrian human). Each wears a teleporter ring (see "Teleporter Rings")." — `sources/adventure-wdh.json:28552`
> "The Kolat brothers once took on apprentices, who slept here. {@creature Manshoon|WDH} now allows his own apprentices—Ered Payno, Havi Termock, and Savara Firethorn—to do the same. All three can be found in {@area K15|3fc}." — `sources/adventure-wdh.json:28377`

Alexandrian, the disintegrated apprentice (book p.95):
> "His former fourth apprentice tried to gain access to it and was disintegrated when Manshoon caught him." — [PDF-IMAGE] `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, book p.95 [PDF p.4 of 5] ("Questioning the Zhentarim", apprentice wizards)

Alexandrian, the astral vault (book p.92; conflicts with the campaign; see D9):
> "Although Manshoon lost the original Eye he had obtained, as Dragon Heist begins the Zhentarim seize possession of the Eye unwittingly carried by Renaer Neverember. This Eye is then immediately taken back to Kolat Towers and secured." — [PDF-IMAGE] `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, book p.92 [PDF p.1 of 5]

### A13. Rank, lieutenants and the people who answer to him (day-one)

Org page, Leadership (line 52, in full):
> "- **Leadership:** Manshoon is a centuries-old wizard, a clone of a clone of one of the Zhentarim's founders, who claims, as all surviving Manshoon clones do, to be the one true Manshoon. He keeps a simulacrum in Kolat Towers as his contingency against assassination, and it fights as his decoy while he escapes. His insurance against dying is the stasis clone spell, which is a separate tool. Nobody stands between him and his lieutenants, and the cell takes its orders from him alone." — `campaign/setting/organizations/09-manshoons-zhentarim.md:52`

Org page, the hub and spokes (line 53) and the lieutenants (line 54):
> "- **The hub and spokes:** The Splinter is built as a hub with spokes. Kolat Towers in the Southern Ward is the command center, and the Interrogation House on Brindul Alley in the North Ward and Yellowspire in the Castle Ward are its field offices. Yellowspire holds a teleportation circle that leads to the Towers, and the Towers stand in the Southern Ward. Teleportation circles also link the Towers to the Interrogation House (**Southern Ward**)." — `campaign/setting/organizations/09-manshoons-zhentarim.md:53`
> "Sidra Romeir runs the ground floor like a barracks, Manafret Cherryport cooks for the household, and Manshoon's three apprentices, Ered Payno, Havi Termock and Savara Firethorn, sleep in the old apprentices' quarters and wear teleporter rings (**Sidra Romeir**; **Manafret Cherryport**; *Dragon Heist*, 5e)." — `campaign/setting/organizations/09-manshoons-zhentarim.md:54`

Notable page, Relationships (line 26):
> "**Relationships.** Manshoon is the leader of the Zhentarim splinter cell, the employer of Urstul Floxin, Sidra Romeir, and Vevette Blackwater, a blackmailer of Masked Lords Jelenn Urmbrusk and Corylus Thann, and a clone-wizard whose response teams are deliberately the weakest in muscle because drawing attention is the one mistake he will not make twice." — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:26`

Villains page, Relationships (lines 61, 63, 65):
> "| Urstul Floxin | Field lieutenant | Most effective operative; trusted with the Stone recovery at Gralhund Villa; his failure there is the first crack |" — `campaign/setting/villains/manshoon.md:61`
> "| Xanathar | Rival | Useful; the Guild's visibility keeps the Watch occupied `[research]`; when the beholder becomes a direct obstacle, Manshoon has a plan |" — `campaign/setting/villains/manshoon.md:63`
> "| The Cassalanters | Missed opportunity | Manshoon is as suspicious of their wealth and spotless name as everyone else, and an arrangement with them could have given him leverage; he chose independence over shared control `[research]` |" — `campaign/setting/villains/manshoon.md:65` (see D18)

Villains page, relationship notes (lines 74-75):
> "- Sidra Romeir is his most trusted lieutenant and holds the teleport rings when lieutenants leave the towers. At Lockdown she locks down Kolat Towers." — `campaign/setting/villains/manshoon.md:74`
> "- His response teams are the weakest in raw muscle of any faction, because drawing attention is the one mistake he will not make twice. They carry orders to capture, not kill, and he underestimates threats that are not magical." — `campaign/setting/villains/manshoon.md:75`

Sidra's Notable page (day-one):
> "**Relationships.** Sidra is Manshoon's Kolat Towers lieutenant, the keeper of the teleporter ring system, and the only person in the cell whose loyalty Manshoon has never tested, because testing it would mean he does not already know the answer." — `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:25`

Urstul's Notable page (day-one; the Gralhund quest references are routed in E2):
> "**Relationships.** Urstul is Manshoon's chief field operative, a temporary occupant of Gralhund Villa (where he treats Yalah as an underling), and the antagonist who drives **Fireball!** and **Gralhund Villa** before the party can identify his master." — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:25`

Adventure, Urstul's master (conflict with the campaign's "chief field agent"; see D15 and E1):
> "{@creature Urstul Floxin|wdh} works for {@creature Manshoon|WDH}, and he is the highest-ranking member of the Zhentarim squad stationed at House Gralhund." — `sources/adventure-wdh.json:32644`
> "Urstul takes his orders from {@creature Manshoon|WDH}'s current simulacrum, which comes and goes from House Gralhund by way of a teleportation circle (connected to the circle in Kolat Towers)." — `sources/adventure-wdh.json:32644`

Adventure, Vevette and Agorn:
> "Vevette was a vicious pirate before she joined the Zhentarim and rose to become one of {@creature Manshoon|WDH}'s favored lieutenants." — `sources/adventure-wdh.json:8532`
> "Agorn made such a good impression on {@creature Manshoon|WDH} that he was elevated quickly through the ranks of the organization, but his life is full of disappointment otherwise. He has not achieved the fame he craved nor earned the wealth he felt he was entitled to." — `sources/adventure-wdh.json:7599`
> "Vevette and Agorn are two of {@creature Manshoon|WDH}'s most trusted followers. Vevette commands the wizard's forces against the Xanathar Guild, while Agorn commands those who oppose the Zhents that aren't loyal to {@creature Manshoon|WDH}." — `sources/adventure-wdh.json:30130`

Adventure, Havia and Mookie (gender conflict; see D20):
> "Two female lightfoot halflings—{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush}—believe that {@creature Manshoon|WDH} is the rightful leader of the Zhentarim. They serve him fearlessly, and will sacrifice themselves to ensure that his plans come to fruition." — `sources/adventure-wdh.json:30183`

Adventure, Sidra and Manafret:
> "The card players are Sidra Romeir (LE female Calishite human {@creature veteran}) and two subordinates (LE male Tethyrian human {@creature thug||thugs})." — `sources/adventure-wdh.json:28155`
> "The halfling, {@creature Manafret Cherryport|wdh}, is one of {@creature Manshoon|WDH}'s lieutenants. He loves to cook, and uses his mage hand cantrip to cut vegetables." — `sources/adventure-wdh.json:28191`

Adventure, Yalah (the Gralhund Zhent handler; routed to Gralhund Villa):
> "She also uses the Zhentarim who are based in House Gralhund as her personal spy network, not realizing that the Zhents' true master is {@creature Manshoon|WDH}." — `sources/adventure-wdh.json:32782`

Adventure, Amath (Yellowspire):
> "The characters have learned that the {@item Stone of Golorr|WDH} is with Amath Sercent, a priest of Bane who is allied with {@creature Manshoon|WDH}. She and her acolytes reside in Yellowspire, a Castle Ward tower so named because its bricks have a pale yellow tinge to them." — `sources/adventure-wdh.json:9741`

Campaign, Agorn and Amath (day-one partnership; the Alexandrian says "friends"; see D3):
> "Agorn is a Manshoon lieutenant and bard, the partner of Amath Sercent, whom he visits at Yellowspire in the evenings, a pass-amulet holder for Kolat Towers, and a man whose mother lives in Mistshore and knows nothing about any of this." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`
> "Amath is the Banite priestess occupying Yellowspire (Castle Ward), the keeper of a teleportation circle providing a back-route into Kolat Towers (bypassing the pass-amulet requirement), Agorn Fuoco's romantic partner, and a Manshoon-adjacent religious operative whose devotion to Bane predates and outlasts any particular Zhentarim arrangement." — `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:25`

Campaign, Vira (a plant; her quest role is routed):
> "**Relationships.** Vira is a Manshoon plant embedded inside Blackstaff Tower, the operative responsible for installing the resonance disruptor in the Tower's defensive architecture, and the primary antagonist of **Smoke in the Tower**." — `campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md:25`

### A14. How long in post, and the Splinter's build

> "He spent about two years building the Splinter, a cell that bears his name and works independently of the Zhentarim's surviving leadership." — `campaign/setting/villains/manshoon.md:33`
> "- Manshoon's clone fled Undermountain, found the towers abandoned with the force field still running, and took the amulet-making instructions from Duhlark's study. He spent two years building the Splinter." — `campaign/setting/history/04-the-founding-of-chains.md:68`
> "- The clone then spent two years building the Splinter cell, which is about 1490 DR counted back from Ches 1, 1492 DR. `[research]` The structure is hub-and-spoke: Kolat Towers as the command center, with the Interrogation House in the North Ward and Yellowspire in the Castle Ward as field offices." — `campaign/setting/history/08-the-players-arrive.md:32`
> "> - About 1490 DR (derived): Manshoon's clone begins building the Splinter cell." — `campaign/setting/history/08-the-players-arrive.md:80`
> "- 1485 DR, about: the Kolat Towers simulacrum is made. This is derived from "seven years ago" in the Kolat Towers structure document and is stated by no other source." — `campaign/setting/history/04-the-founding-of-chains.md:138`
> "- 1490 DR, about: Manshoon's clone settles in Kolat Towers and begins building the Splinter. This is derived from "two years" in the Kolat Towers structure document." — `campaign/setting/history/04-the-founding-of-chains.md:140`

### A15. Faith and Yellowspire (the Bane page is the authority)

> "- **Where it is used:** Bane never appears in person. His faith in play is Amath Sercent and her four acolytes, who keep Yellowspire as a temple and a relay point for Manshoon's cell of the Zhentarim." — `campaign/setting/deities/bane.md:8` (the line begins "> - **Where it is used:**")
> "- **Yellowspire and the Zhentarim split:** Amath is allied with Manshoon's cell, the splinter that peeled off the Doom Raiders' network." — `campaign/setting/deities/bane.md:81`

### A16. Signature belongings (all sourced)
- Staff of power: `campaign/structure/arc-i-kolat-towers.md:13` (quoted in A5); `sources/adventure-wdh.json:30257` (quoted in A12).
- Spellbook: `sources/adventure-wdh.json:30281`, `:30325` (A12).
- Teleporter rings: `sources/adventure-wdh.json:28822` (A12).
- Masks: `sources/adventure-wdh.json:29981`, `:30264` (A12).
- Sunglobe (the Vault page): "So does Manshoon's sunglobe, if **Manshoon Destroyed** is marked and the item was recovered from Kolat Towers." — `campaign/structure/arc-j-vault-of-dragons.md:118` (quest-time; route to the Vault)

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Notable summary: "- *Vaasan human wizard (clone), lawful evil, he/him*. Stat block: **Mage (with modifications)**." — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:5`
- Southern Ward gazetteer: "**Manshoon (Lawful Evil, Vaasan Human, he/him)**" — `campaign/gazetteer/waterdeep/southern-ward.md:139`
- Wiki infobox: "| alignment5e    = [[Lawful evil]]" — `W:59`; "| alignment3e    = [[Lawful evil]]" — `W:48`; "| alignment1e    = [[Lawful evil]]" — `W:42`
- Published adventure: no alignment is printed on any Manshoon line grepped. "Evil to the core" (`sources/adventure-wdh.json:32216`) is the only moral descriptor.
- Villains page and Org page: no alignment line in their Summary or Background.

**Species and ethnicity**
- Published adventure: "Sitting on the edge of the bed is a handsome young male human in elegant robes." — `sources/adventure-wdh.json:30250`
- Notable summary: "Vaasan human" — `01-manshoon.md:5`. Southern Ward: "Vaasan Human" — `southern-ward.md:139`.
- Wiki: "| race           = [[Human]]" — `W:14`; "| ethnicity      = [[Vaasan]]<ref>{{Cite web/theedverse/2018-02-21 - Manshoon's appearance and heritage}}</ref>" — `W:15` (the ethnicity is a Faerûn ethnicity under brief ruling 5)

**Pronouns**
- Notable summary "he/him" — `01-manshoon.md:5`. Southern Ward "he/him" — `southern-ward.md:139`. Wiki: "| sex            = Male" — `W:12`; "| gender         = Masculine" — `W:13`. Adventure: "He commends the characters for making it this far..." — `sources/adventure-wdh.json:30255`. The Villains page's Draft Notes say the Notable page states no pronouns (`villains/manshoon.md:137`); that note is stale.

**Stat block**
- Notable summary: "Stat block: **Mage (with modifications)**." — `01-manshoon.md:5`. No source found for "Mage" as Manshoon's block (see D17).
- Wiki: "| challenge5e    = 13" — `W:60`; "| class5e        = {{Class table|edition=5e|[[Wizard]]|18}}" — `W:61`; "| refs5e         = <ref name="WDH5e-p208-209">{{Cite book/Waterdeep: Dragon Heist|208-209}}</ref>" — `W:62`.
- Alexandrian stat reference: "Manshoon Simulacrum – DH p. 209" and "Manshoon – DH p. 209" — [PDF-IMAGE] `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, book p.95 [PDF p.4 of 5]. No class and no CR printed.
- Published adventure: the simulacrum's CR only: "It has a challenge rating of 8 (3,900 XP)." — `sources/adventure-wdh.json:32233`. The Manshoon entry is a page reference: `"page": 208` at `sources/adventure-wdh.json:32212`.
- Simulacrum changes: "The simulacrum has no special equipment. Consequently, it has AC 12 and lacks the Magic Resistance trait and the Staff of Power action option." — `sources/adventure-wdh.json:32231`; "It loses all spell slots of 6th level and higher." — `:32232`.

**Age and appearance**
- "who is much older than he looks" — `sources/adventure-wdh.json:30254`. Wiki birth 1229 DR — `W:22`.
- "Long black hair partially conceals his angelic face" — `sources/adventure-wdh.json:30250`.
- Simulacrum: "The simulacrum resembles a robed wizard with long black hair, pale skin, and an articulated metal left hand and forearm. Its face is concealed behind a steel mask that bears a smiling visage." — `sources/adventure-wdh.json:30077`

**Home**
- Wiki: "| home           = [[Citadel of the Raven]], [[Moonsea]]" — `W:10`. Campaign current home: "He runs the Splinter, a cell of his own, from the warded towers of Kolat Towers in the Southern Ward." — `campaign/setting/villains/manshoon.md:21`.

**Patron deity and faith:** wiki "| patron deity   = [[Mystra]]" — `W:18`. Campaign: "absorb the Weave and supplant Mystra" — `campaign/setting/villains/manshoon.md:21`.

---

## C. Sentences that narrate quest-time or day-one conflicts

### C1. The current Notable page (`01-manshoon.md`)
I checked the whole page (lines 5-30). No sentence narrates a quest event, an arrest, a mission, a reveal or an "after the party" beat. Items the drafter must still handle:
- Line 5 and line 8: summary and "Featured in" list only.
- Line 16: "...and deepen his hold over Masked Lords Corylus Thann and Jelenn Urmbrusk into a full Council majority." Day-one wording, but "full Council majority" is not sourced (D14).
- Line 22: "using a teleportation circle for all movement" (D16).
- Line 30 (Overview): "A name the party does not have yet. The hard-edged Zhentarim operatives working Waterdeep's streets answer to someone, and none of them will say who." This is the "Manshoon Named" gate in prose; the gate itself is quest-time (E1, E2). The drafter should check it against ruling 1.

### C2. The current voice profile (`.claude/skills/character-voices/voices/manshoons-zhentarim.md`)
Quest-time clauses (carry a day-one restatement under ruling 16):
> "None of them will say Manshoon's name before Phase 2, and that refusal is itself part of every voice here." — `manshoons-zhentarim.md:2`
> "  - **The Shadow (Acts I–II):** never heard. Only his lieutenants speak, and they won't name him." — `manshoons-zhentarim.md:17`
> "  - **The Architect (Acts II–III):** revealed, courteous, patient and terrifyingly reasonable." — `manshoons-zhentarim.md:18`
> "  - Cornered at **Kolat Towers**, the courtesy thins, but it never breaks." — `manshoons-zhentarim.md:19`
The phase table and triggers they restate are in the Villains page: "| 1 | The Shadow | Acts I–II | Absent; only his lieutenants are visible; PCs fight "the Zhentarim" without knowing Manshoon is a distinct player |" (`campaign/setting/villains/manshoon.md:47`), "| 2 | The Architect | Acts II–III | Revealed; negotiates from strength; charming, precise, and calm about consequences in a way that should unsettle |" (`:48`), "| 3 | The Simulacrum Problem | **Kolat Towers** | Cornered; the performance of calm drops; the simulacrum fights as his decoy while Manshoon escapes |" (`:49`), and the triggers at `:52-53`.

Other voice lines (day-one; no change needed on the face of them):
> "- **Sound:** A cultured, cool, perfectly modulated voice, never raised, precise in every consonant. His artificial arm clicks faintly when he gestures." — `manshoons-zhentarim.md:11`
> "- **Word choice:** Scholarly and imperial: "inevitable", "an arrangement", "the Weave", "my city" (said as a correction). He calls the party by name once he's learned it, and the simulacra he has made "the others"." — `manshoons-zhentarim.md:13` (the "simulacra" line is GM-only; the Roleplaying block is GM-only, so it stays out of the Overview)
> "- **Swearing:** *Never · Plain · n/a.* Profanity is for people who lack better words. His rare anger is precise and calm, and more frightening for it." — `manshoons-zhentarim.md:14`
> "- **Never:** He never loses his temper, never pleads, and never admits a clone is anything but an imposter." — `manshoons-zhentarim.md:22`
> "  - *Greeting:* "You've been very persistent. Sit. Let us be reasonable, since the alternative is so wasteful."" — `manshoons-zhentarim.md:24`
> "  - *Business:* "You hold a key to a door I intend to open. I can make that profitable for you, or brief. The choice is genuinely yours."" — `manshoons-zhentarim.md:25`
> "  - *Under pressure:* "Halaster took an arm. You will not get the rest."" — `manshoons-zhentarim.md:26`
The voice profile line 4 ("Two Zhentarims...") is day-one and stays.

### C3. The Villains page Background (lines 25-41), quest-adjacent entries
- Line 35 is pre-start (derived Nightal 1491 DR; `campaign/setting/history/06-the-open-lords-fall.md:135`).
- Line 36 places the locket seizure "on the night before Ches 1" and the warehouse raid. The raid is dramatised in **Finding Floon** (`campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:9`: "Four kenku occupy the building, searching the wreckage of the Xanathar's Guild raid that killed Manshoon's cell"). The date is before Ches 1, but the event is a quest event. Orchestrator decides whether to keep it as backstory.
- Line 41 ("The campaign stages his reveal across three quests...") is design text and routes to **Faction Outposts**, **Kolat Towers** and **Vault of Dragons** (E2).
- Line 38 is the published goal (a conflict; D11).
- Line 40 is GM-only (simulacrum). Keep out of the Overview.

Villains page, non-Background quest-time lines:
> "- The party gets his name at the Interrogation House in **Faction Outposts**, which is where the **Manshoon Named** Event Outcome is marked." — `campaign/setting/villains/manshoon.md:9` (the full line begins "- Manshoon appears in **Finding Floon** ...")
> "- **Kolat Towers** records the result of the raid as one of three Event Outcomes (**Manshoon Destroyed**, **Manshoon Simulacrum Only** or **Manshoon Alive**), and **Vault of Dragons** reads it." — `campaign/setting/villains/manshoon.md:10`
> "| Urstul Floxin | Field lieutenant | Most effective operative; trusted with the Stone recovery at Gralhund Villa; his failure there is the first crack |" — `:61` (Gralhund Villa)
> "| The PCs | Escalating problem | Early: noise; mid-campaign: a problem to solve; first solution is always a job offer, not an assassination |" — `:66` (day-one design; fine)
> "- Manshoon's parallel strike in **Sea Maidens Faire** always fires, and it sends his agents against Jarlaxle's ships in Jarlaxle's own harbor." — `campaign/setting/villains/manshoon.md:72`
> "- Sidra Romeir is his most trusted lieutenant and holds the teleport rings when lieutenants leave the towers. At Lockdown she locks down Kolat Towers." — `:74` (the Lockdown tier is an escalation state)
> "- Zhentarim crews with flying snake tattoos work the back streets of Waterdeep. The Watch has arrested a few of them after street brawls." — `campaign/setting/villains/manshoon.md:90` (Overview; the arrests are quest-time, ruling 1)

### C4. The organization page (`09-manshoons-zhentarim.md`)
- Line 33 (raid the night before Ches 1): "- **The night before Ches 1, 1492 DR, Renaer Neverember:** Five Zhentarim thugs working for Urstul Floxin seized Renaer Neverember to learn what he knew about his father's hidden gold, and they took Floon Blagmaar in the same attack. House Gralhund paid for the operation (*Dragon Heist*, 5e; **House Gralhund**). Xanathar's Guild raided the Candle Lane warehouse where the thugs held both men and killed the cell's agents there (*Dragon Heist*, 5e)." — `campaign/setting/organizations/09-manshoons-zhentarim.md:33` (the event lives in `campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:9`)
- Line 91: "- **The Open Lord's Watch (enemy):** The Watch has arrested a few of the tattooed crews in street brawls, and none of them will say who gives the orders (**The Open Lord's Watch**)." — `09-manshoons-zhentarim.md:91` (arrests)
- Line 113 (Overview): "Zhentarim crews with flying snake tattoos work Waterdeep's back streets, and they are hostile to Davil Starsong's Doom Raiders. The crews take prisoners, and the Watch has arrested a few of them in street brawls. None of them will say who gives the orders, and street talk says one master stands behind them." — `:113` (the arrest clause is quest-time)
- Line 118 (GM Notes, day-one): "- **The Eyes:** The cell holds no Eye of the Stone, because its envoys brought Eye #1 to Xanathar as a gift and Xanathar killed them and kept the Eye. Manshoon therefore needs the Stone and all three Eyes." — `:118`

### C5. The Factions Guide page (`10-manshoons-zhentarim.md`)
- Line 23 (the name reveal in the Interrogation House): "*Front Room.* Avareen and Zorbog's quarters. Avareen carries a pass-amulet to Kolat Towers. While the party explores, a flying snake arrives with *A Directive to Zorbog* signed by "Manshoon," ordering Zorbog to kidnap Fenerus Stormcastle of Quill Alley, a "known associate of these new meddlers in the Grand Game."" — `campaign/guides/factions/10-manshoons-zhentarim.md:23` (quest: **Faction Outposts**)
- Line 25 (Ott): "*Backroom.* A rack and other instruments of torture. An arcane circle on the floor. Strapped into the rack is **Ott Steeltoes**, a Xanathar's Guild agent captured while the Zhentarim were trying to locate the Eye." — `:25` (quest: **Faction Outposts**)
- Line 9 (capture order; mechanics, not for the Notable page): "Any Zhentarim team sent to attack the characters carries orders to take them as prisoners to the Interrogation House on Brindul Alley." — `:9`

---

## D. Conflicts (both sides quoted; campaign ranks above the adventure, the adventure above the Alexandrian PDFs and the wiki; the orchestrator decides any tie)

**D1. Kolat Towers' ward.** Campaign: "Kolat Towers is a crumbling pair of towers in the Southern Ward" — `campaign/setting/villains/manshoon.md:31`. Adventure, the Trades Ward: "{@creature Manshoon|WDH} lurks in Kolat Towers, a pair of wizards' towers in the Trades Ward. This residence is described in chapter 8." — `sources/adventure-wdh.json:560`. Adventure, Southern Ward: "{@creature Manshoon|WDH} took control of Kolat Towers, a crumbling residence in the Southern Ward" — `:32218`. Campaign settled (`campaign/setting/history/04-the-founding-of-chains.md:153`: "The ward of Kolat Towers. `adventure-wdh.json` lines 26797, 32215 and 32218 say the Southern Ward, and line 560 says the Trades Ward. The campaign follows the Southern Ward...").

**D2. The Interrogation House's ward.** Campaign: "A windowless house on Brindul Alley in the North Ward, kept by Avareen Windrivver and Zorbog Jyarkoth." — `campaign/setting/organizations/09-manshoons-zhentarim.md:57`; "*North Ward, Brindul Alley.*" — `campaign/structure/arc-e-faction-outposts.md:201`. Adventure: "The characters' search for the {@item Stone of Golorr|WDH} leads them to a snow-covered alley in the Trades Ward that contains a windowless Zhentarim safe house ({@area L1|140}) and a meat shop called Cuttle's Meat Pies ({@area L2|141})." — `sources/adventure-wdh.json:7174`. Alexandrian: "ZHENTARIM INTERROGATION HOUSE (Trade Ward, Brindul Alley):" — [PDF-IMAGE] `sources/5. Faction Outposts.pdf`, book p.45 [PDF p.10]. Campaign settled: "Brindul Alley's ward is the North Ward, as the Zhentarim Factions Guide and `arc-i-kolat-towers.md:15` say." — `campaign/gazetteer/waterdeep/north-ward.md:272`.

**D3. Amath and Agorn.** Alexandrian: "It is occupied by Amath Seccent (LE female Mulan priest), a Banite priestess allied with Manshoon, and her four acolytes." and "Seccent is friends with Agorn Fuoco (see Part 3C: Response Teams), and he may also be found visiting here." — [PDF-IMAGE] `sources/5. Faction Outposts.pdf`, book p.46 [PDF p.11]. Alexandrian revelation list: "Threatening Agorn Fuoco; he'll sell out his friend to save his own life (Response Team: Agorn Fuoco)" — [PDF-IMAGE] `sources/17. Outpost and Lair Revelation Lists.pdf`, book p.124 [PDF p.4]. Campaign: "Agorn Fuoco's romantic partner" (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:25`, A13) and "Amath is Agorn Fuoco's romantic partner" (`campaign/setting/organizations/09-manshoons-zhentarim.md:103`: "- **Amath Sercent** — Mulan human priest of Bane, lawful evil, who occupies Yellowspire in the Castle Ward as a Banite priestess allied with Manshoon. Agorn Fuoco is her romantic partner and visits her there in the evenings."). Campaign wins by rank. The Org's note replaces "friends" (`organizations/09-manshoons-zhentarim.md:160`).

**D4. Clone's arrival and the simulacrum's age.** Campaign: "He spent two years building the Splinter cell" (`campaign/structure/arc-i-kolat-towers.md:15`) and "It was created seven years ago" (`arc-i-kolat-towers.md:17`). The seven-year simulacrum predates the clone's arrival (`arc-i-kolat-towers.md:13`). Adventure: "this clone of the ancient archwizard infiltrated Waterdeep years ago and has been hiding out in Kolat Towers ever since" — `sources/adventure-wdh.json:32215`. The history derives 1485 DR for the simulacrum (`campaign/setting/history/04-the-founding-of-chains.md:138`). Unsettled in the sources; the Villains page keeps both (`villains/manshoon.md:33`).

**D5. Duhlark's death.** Campaign: "Duhlark survived him by nine years before being found dead in his study, apparently of old age, with the force field still running." — `arc-i-kolat-towers.md:9`; "Duhlark was found dead in his study nine years later." — `campaign/gazetteer/waterdeep/southern-ward.md:52`. Adventure: "{@creature Manshoon|WDH} found Duhlark Kolat's skeletal remains in the bed and transformed his skull into a flameskull." — `sources/adventure-wdh.json:28680`; "Duhlark became a recluse who died in his own fortress." — `:26865`. Campaign wins. The bedroom detail is adventure-only; the campaign's K19 is "Duhlark's Bedroom" (`arc-i-kolat-towers.md:140`).

**D6. Alcedor's fate.** Adventure: "Alcedor left the towers, never to be heard from again" — `sources/adventure-wdh.json:26865`. Campaign: "He died in the towers in 1385 DR under circumstances that remain unclear." — `arc-i-kolat-towers.md:9`. Campaign wins; history notes it (`campaign/setting/history/04-the-founding-of-chains.md:161`: "Alcedor Kolat's fate... The campaign wins.").

**D7. The Doom Raiders' arrival.** Campaign: "The Doom Raiders, five retired adventurers, were sent to Waterdeep in 1489 DR to found the Black Network's foothold." — `campaign/setting/history/04-the-founding-of-chains.md:24`. Adventure: "They gave up adventuring to join the Black Network and came to Waterdeep three years ago" — `sources/adventure-wdh.json:31916`. Appendix B, the Doom Raiders' own speech: "Me and my colleagues arrived in Waterdeep about four years ago." — `sources/Appendix_B_-_Player_Factions.md:636`. Campaign wins (1489 DR is three years before Ches 1, 1492 DR).

**D8. The Stone's route to Xanathar.** Campaign: "About Nightal 1491 DR (derived), Manshoon's Zhentarim sent two lieutenants to Skullport with Eye #1 of the Stone of Golorr..." — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:45`. Alexandrian p.15: "slew the Zhentarim envoys" — [PDF-IMAGE] book p.15. Adventure: "As Zhents loyal to {@creature Manshoon|WDH} try to forge an alliance with Xanathar, the Stone of Golorr is stolen." — `sources/adventure-wdh.json:838`. The campaign's own note: "The published entry has Xanathar's spies stealing the Stone..." (`campaign/setting/history/02-the-long-shadow.md:158`). Campaign wins.

**D9. Who holds an Eye.** Campaign: "Kolat Towers holds no Eye." — `campaign/structure/arc-i-kolat-towers.md:57`; "**Manshoon:** He holds no Eye." — `lore/stone-of-golorr-and-the-eyes.md:44`; "Manshoon holds no Eye." — `running-the-villains.md:30`. Alexandrian: "This Eye is then immediately taken back to Kolat Towers and secured." — [PDF-IMAGE] `12. Lair Zhentarim – Kolat Towers.pdf` book p.92 [PDF p.1]; "Inside the Astral Vault: The vault contains the Eye, 5 pass-amulets, a dozen teleporter signet rings, and Manshoon's Report on the Grand Game (see Part 6D)." — book p.94 [PDF p.3]; "He already has one. He once had another that was stolen by Xanathar." — book p.96 [PDF p.5]. Alexandrian Eyes: "As described in Part 1, the Eyes are currently held by the Cassalanters, Manshoon, and Xanathar." — [PDF-IMAGE] `8. The Eyes of the Stone.pdf`, book p.62 [PDF p.1]. Campaign wins (brief ruling 12). Note that the Villains draft notes already record this conflict (`villains/manshoon.md:125`).

**D10. Who the Zhents' envoys were.** Campaign: "Xanathar killed the Zhentarim envoys who brought it to him" — `running-the-villains.md:21`. The campaign's lair version and the Alexandrian agree on the killing (D8).

**D11. The goal.** Campaign: "...absorb the Weave and supplant Mystra" — `villains/manshoon.md:80`, `01-manshoon.md:16`. Adventure: "...declare himself the Wizard-King of Waterdeep" — `sources/adventure-wdh.json:32219`. Campaign wins (the Org and Villains drafts record it; `history/04-the-founding-of-chains.md:73`).

**D12. Corylus Thann's leverage.** Campaign quest-doc: "he supplies Guild intelligence in exchange for the ledger's continued privacy" — `arc-i-kolat-towers.md:19`. Campaign Villains and Notable: "Corylus Thann is held over a scandal" — `villains/manshoon.md:37`; "a blackmailer of Masked Lords Jelenn Urmbrusk and Corylus Thann" — `01-manshoon.md:26`. Adventure: "Corylus Thann, a racist Waterdavian noble, is paying the Zhentarim not to reveal that he hired Zhent thugs to assault non-humans." — `sources/adventure-wdh.json:30294`. Org Funding: "from the hush money that Corylus Thann pays (*Dragon Heist*, 5e)." — `campaign/setting/organizations/09-manshoons-zhentarim.md:66`. The arc-i sentence is the outlier; the adventure and the Org page agree on the payment direction. Orchestrator decides.

**D13. Jelenn's money.** Adventure: "receives regular payments from the Zhentarim to offset monies he loses in bad investments" — `sources/adventure-wdh.json:30295`; "borrow money from the Zhentarim instead" — `:30374`. Campaign: "accumulated significant debt to a Splinter front organization" — `arc-i-kolat-towers.md:19`; "Jelenn's debt to Manshoon's Zhentarim was borrowed" — `open-lord-and-masked-lords.md:64`. The adventure's own two lines disagree (30295 pays her; 30374 she borrows). The campaign follows the loan.

**D14. Votes and the Council.** Campaign: "her votes in the Council of Guildmasters follow Manshoon's preferences" — `arc-i-kolat-towers.md:19`; "their votes follow his preferences" — `villains/manshoon.md:37`; Notable: "into a full Council majority" — `01-manshoon.md:16`. "Council of Guildmasters" appears in the Manshoon material I read only at `arc-i-kolat-towers.md:19`; "Council majority" appears only at `01-manshoon.md:16`. Not sourced beyond these.

**D15. Urstul's role.** Notable: "Urstul is Manshoon's chief field operative" — `02-urstul-floxin.md:25`. Adventure: "{@creature Urstul Floxin|wdh} works for {@creature Manshoon|WDH}, and he is the highest-ranking member of the Zhentarim squad stationed at House Gralhund." — `sources/adventure-wdh.json:32644`. Consistent; but the adventure says "takes his orders from Manshoon's current simulacrum" (`:32644`) while the campaign says "he cannot name Manshoon, because he knows only a code and a chain of dead drops" (`villains/manshoon.md:69`, quoted in the Villains draft note `:137`... see the Villains Draft Notes). Campaign wins.

**D16. Teleport habit.** Notable: "he is never seen entering or leaving Kolat Towers, using a teleportation circle for all movement." — `01-manshoon.md:22`. Adventure: "{@creature Manshoon|WDH} rarely leaves the towers and uses a teleportation circle when he must do so" — `sources/adventure-wdh.json:32218`. Villains: "Manshoon rarely leaves, and he uses a teleportation circle when he must" — `villains/manshoon.md:31`. The Notable line is the outlier; the campaign and adventure agree on "when he must".

**D17. Stat block.** Notable: "Stat block: **Mage (with modifications)**." — `01-manshoon.md:5`. Wiki: "| class5e        = {{Class table|edition=5e|[[Wizard]]|18}}" and "| challenge5e    = 13" — `W:60-61`. Alexandrian: "Manshoon – DH p. 209" with no class (book p.95). No campaign file gives a class for Manshoon; the Notable line has no source.

**D18. Cassalanter secrecy (brief ruling 7).** Villains row: "...an arrangement with them could have given him leverage; he chose independence over shared control `[research]`" — `campaign/setting/villains/manshoon.md:65`. Org: "Manshoon shares the city's suspicion of a family that is too rich and too pleasant, and an arrangement with them could have given him leverage `[research]` (**Manshoon**)." — `campaign/setting/organizations/09-manshoons-zhentarim.md:89`. Ruling 7 says "Other pages use suspicion." Both rows keep "leverage", which implies knowledge of what they would be leverage on. The Villains draft notes say the row was softened (`villains/manshoon.md:127`), but the sentence still implies leverage. Flag for the orchestrator. The Notable page does not mention the Cassalanters.

**D19. Vevette's alignment.** Notable: "*Tethyrian human swashbuckler, lawful evil, she/her*." — `campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md:5`. Org: "**Vevette Blackwater** — Tethyrian human swashbuckler, lawful evil" — `09-manshoons-zhentarim.md:98`. Adventure: "Vevette Blackwater (CE female Tethyrian human {@creature swashbuckler|VGM}; see {@adventure appendix B|WDH|12})" — `sources/adventure-wdh.json:30120`. Alexandrian: "Vevette Blackwater (CE female Tethyrian human) – swashbuckler, DH p. 216" — [PDF-IMAGE] `12. Lair Zhentarim – Kolat Towers.pdf`, book p.95 [PDF p.4 of 5]. Campaign wins by rank; the Org draft note says the campaign follows her page (`09-manshoons-zhentarim.md:173`). Flag: the adventure and the Alexandrian both say chaotic evil.

**D20. Mookie's gender.** Adventure: "Two female lightfoot halflings—... Havia Quickknife ... and ... Mookie Plush" — `sources/adventure-wdh.json:30183`. Notable: "*Lightfoot halfling adept, lawful evil, he/him*." — `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:5`. Campaign wins by rank. Flag for Mookie's page.

**D21. Organization's "Featured in" list is short.** Org: "- **Featured in:** **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Kolat Towers**" — `09-manshoons-zhentarim.md:11`. Villains: "Manshoon appears in **Finding Floon**, **Trollskull Alley**, **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers** and **Vault of Dragons**." — `villains/manshoon.md:9`.

**D22. The Interrogation House's first name use.** Alexandrian, book p.45: "a flying snake arrives with A Directive to Zorbog. Signed by "Manshoon,"" — [PDF-IMAGE] book p.45 — and campaign: "The party gets his name at the Interrogation House in **Faction Outposts**" (`villains/manshoon.md:9`). Consistent.

**D23. The structural-rules line.** The Org draft note says `gm-guide/structural-rules.md` line 9 "says the cell conducts assassinations and maintains mind-controlled servants" (`09-manshoons-zhentarim.md:182`). The line reads: "**Manshoon's Zhentarim** are the villain faction. They operate from Kolat Towers, prefer to capture rather than kill, and maintain mind-controlled servants. Manshoon regards the Doom Raiders as deserters who stole his name." — `campaign/guides/gm-guide/structural-rules.md:9`. The word "assassinations" is not on that line. The draft note is wrong about it. The only servant source is that line.

**D24. Gralhund alliance date.** Adventure: "Less than a year ago, the Gralhunds were approached by agents of the Zhentarim loyal to {@creature Manshoon|WDH}, and the nobles formed an alliance with them." — `sources/adventure-wdh.json:32445`. Campaign: "- **Less than a year before Ches 1, 1492 DR, House Gralhund:** Zhentarim agents loyal to Manshoon approached House Gralhund, and the two formed an alliance." — `campaign/setting/organizations/09-manshoons-zhentarim.md:31`. Consistent.

**D25. Halaster's reason.** Adventure: "amputated his left arm at the elbow for reasons unknown" — `sources/adventure-wdh.json:32217`. Campaign: "Halaster Blackcloak, who tolerated the clone for a time out of professional curiosity, eventually severed Manshoon's left arm..." — `arc-i-kolat-towers.md:13`. Campaign addition, not a contradiction. A Background quoting the adventure must say "for reasons unknown" in the published wording.

**D26. Post-1370 clone fates.** Wiki: "killing both Fzoul and the final clone of Manshoon" — `sources/research/pass5-bundles/zhentarim/wiki.txt:234`. Wiki: "The one in Undermountain appeared to have died during the events of the Spellplague itself." — `W:106`. Adventure: "at least three are still alive. The one presently in Waterdeep escaped death by hiding out in Undermountain" — `sources/adventure-wdh.json:32217`. Orbakh: Villains keeps it: "one became the vampire Orbakh in Westgate" — `campaign/setting/villains/manshoon.md:28`; Org and history omit it (`campaign/setting/history/04-the-founding-of-chains.md:44` says "one became the vampire Orbakh in Westgate" — yes the history keeps it at line 44 (quoted in A4)). So Org (`09-manshoons-zhentarim.md:26` "clone") and history keep Orbakh; the Org draft note says the Orbakh detail was left out of the Villains Background (`villains/manshoon.md:140`). Orchestrator decides whether Orbakh goes into the Background.

**D27. The Undermountain arm's level.** Villains: "(5e *Waterdeep: Dungeon of the Mad Mage*, area 1a)" — `campaign/setting/villains/manshoon.md:29` (no level). Undermountain page: "Manshoon's severed hand floats here as an undead guardian." under "9 | Dweomercore" — `campaign/setting/geography/undermountain-and-skullport.md:70`. WDMM: area 1a is inside "Level 9: Dweomercore" (`sources/adventure-wdmm.json:24359`, `:26119`). Consistent; the Background should say Level 9 if it names the level.

**D28. Lady Gondafrey.** Campaign: "Lady Gondafrey, a City Watch captain taken in 1379 DR, is a prisoner inside." — `campaign/gazetteer/waterdeep/southern-ward.md:59`. Adventure: "Duhlark Kolat long ago trapped a magical experiment in this cell: a {@creature gargoyle} that has been imbued with the personality of a human knight of Tyr (god of justice) named {@creature Lady Gondafrey|wdh}." — `sources/adventure-wdh.json:28504`. The campaign makes her a human prisoner; the adventure makes her a gargoyle. Routed to **Kolat Towers**.

**D29. The Overview's arrest clause** is quest-time (C3, C4) and not a conflict between sources.

---

## E. Stale lines in other files (not edited) and routed quest references

### E1. Stale or gated lines in setting, guide and quest files (the Notable page must not copy them)
- `campaign/guides/gm-guide/structural-rules.md:9`: quoted in D23 (the draft note misquotes it).
- `campaign/gazetteer/waterdeep/castle-ward.md:131`: "- Vajra commands Force Grey. Her staff holds Khelben Arunsun's soul, and she says "the Splinter" until **Manshoon Named** is marked for the party member she is speaking to." (gate; ruling 1)
- `campaign/gazetteer/waterdeep/southern-ward.md:48`: "- Phaulkonmere stands one block south of Kolat Towers (Dragon Heist). Until **Manshoon Named** is marked for a member, Enclave speakers say "the Splinter" and never point toward the towers." (gate)
- `campaign/gazetteer/waterdeep/southern-ward.md:141`: "- Hook: the party has no name for him until **Manshoon Named** is marked for a member." (gate, in the Manshoon entry)
- `campaign/gazetteer/waterdeep/southern-ward.md:145`: "> - Manshoon lives in Kolat Towers and lets his simulacrum take the opening volley in a fight. He prefers to capture rather than kill. His location in the towers depends on the escalation tier, and **Kolat Towers** sets it." (day-one, plus a quest pointer)
- `campaign/setting/history/04-the-founding-of-chains.md:84`: "- Factions that speak to players say "the Splinter" or "the other cell" until **Manshoon Named** is marked for the listener." (gate in a setting page)
- `campaign/setting/history/04-the-founding-of-chains.md:92`: "> - Waterdeep holds two Zhentarim organizations, and the Doom Raiders are only one of them. Nobody speaks Manshoon's name to a player until **Manshoon Named** is marked for that listener." (gate)
- `campaign/setting/deities/bane.md:73`: "- **Never reveal:** That Yellowspire is a Banite tower, that its cellar circle leads to Kolat Towers, or that Amath is allied with Manshoon. Until the party marks **Manshoon Named**, even the Doom Raiders say "Floxin's cell" or "the other cell" and call Kolat Towers "the towers in the Southern Ward."" (gate)
- `campaign/guides/factions/03-lords-alliance.md:13`, `04-emerald-enclave.md:13`, `05-order-of-the-gauntlet.md:13`, `06-force-grey.md:11`: each says the Splinter is named "the Splinter" or "the other cell" until **Manshoon Named** is marked (gate in guide text).
- `campaign/gazetteer/waterdeep/north-ward.md:40`: "- Samara, a prisoner in **Xanathar's Lair**, says Manshoon's organization is based in a tower in the North Ward. That is a misdirection from overheard talk. Kolat Towers stands in the Southern Ward, and the Interrogation House is the Zhentarim site that a North Ward search turns up." (quest text; routed to Xanathar's Lair)
- `campaign/setting/history/08-the-players-arrive.md:65`: "- Urstul Floxin's cell led the kidnapping and fled to Kolat Towers before the quest begins. The City Watch has Splinter thugs under arrest at the Dock Ward scene." (arrests; ruling 1)
- `campaign/structure/arc-i-kolat-towers.md:17`: "It was created seven years ago" (D4).
- `sources/SOURCE_GUIDE.md:135`: "- **Manshoon:** Archmage running a Zhentarim splinter cell from Kolat Towers. Uses simulacrums for deniability. Agenda: political control of Waterdeep, eliminate the Doom Raiders who he sees as weak." (stale; the Villains page says "absorb the Doom Raiders" at `villains/manshoon.md:81` and the Org says "dismantle" at `09-manshoons-zhentarim.md:45`)
- `campaign/setting/organizations/09-manshoons-zhentarim.md:182`: the Draft Note misquotes structural-rules line 9 (D23).
- `campaign/setting/villains/manshoon.md:137`: the Draft Note says the Notable page states no pronouns; stale (line 5 has he/him).
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:22`: "using a teleportation circle for all movement" (D16).

### E2. Routed quest references (quest-time; not day-one)
- **Finding Floon.** The Renaer and Floon seizure, the locket Eye and the warehouse raid: `campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:9` ("Four kenku occupy the building, searching the wreckage of the Xanathar's Guild raid that killed Manshoon's cell"). Alexandrian, book p.16: "Zhentarim agents snatch Renaer Neverember and his friend Floon Blagmaar." — [PDF-IMAGE] `sources/1. The Villains.pdf`, book p.16 [PDF p.4 of 7].
- **Fireball!.** The Dalakhar capture attempt and the Zhentarim dead: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:184`: "> **Path C — Speak with Dead, the Zhentarim.** Bashekk Ortallis and Wern Malkrave each give five answers. Combined: they were tracking Dalakhar for Floxin because whatever he carried would make them "as rich as kings."" The Alexandrian Arc D: "Within hours, Floxin killed his guards and escaped — without the Stone, which Gralhund refused to yield." — `sources/Act_III_Arc_D.md:39`.
- **Gralhund Villa.** Floxin's strike team on Ches 24: "<li><strong>Urstul Floxin's Strike Team:</strong> Eight of Manshoon's Zhentarim and Floxin himself, intent on recovering the Stone. Arrive on the night of Ches 24th.</li>" — `sources/Act_III_Arc_E.md:13`. `campaign/quests/act-ii/gralhund-villa/ev-04-the-zhentarim-raid.md:98`: "- **Floxin Alive** — mark when Floxin survives the raid; read by **Kolat Towers**, where he becomes available as a Manshoon response team leader." (the line is "- **Floxin Alive** — mark ...". Exact text per grep: "> - **Floxin Alive** — mark when Floxin survives the raid; read by **Kolat Towers**, where he becomes available as a Manshoon response team leader."). `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:40`: "| Manshoon's name | Not revealed; Floxin never gave it | Preserved for a later arc |". `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:39`: "- **Manshoon's Zhentarim:** By the night of Ches 24, when Floxin's strike team hits **Gralhund Villa**, Manshoon's cell knows the Gralhunds hold the Stone."
- **Faction Outposts.** The name reveal: `campaign/structure/arc-e-faction-outposts.md:207`: "*The Directive to Zorbog.* A flying snake arrives during or shortly after the party enters, bearing a sealed letter addressed to Zorbog. The letter is a *Directive to Zorbog* signed **Manshoon** — the first document in the campaign bearing his name as a signature." Also `:211` ("*Intel Yield.* Manshoon's name (first use in the campaign).") and `:479` ("***Name, Identity, Motivation.*** Manshoon's revelation has been staged across three quests: name at the Interrogation House, identity at **Kolat Towers**, motivation at **Vault of Dragons**."). Yellowspire: `:231` ("**Escalation: Manshoon moves to Suspicious (Tier 2) if the Interrogation House has not been hit; moves to Lockdown (Tier 4) if it has.**"). `:452` ("- **Kolat Towers** — The Yellowspire teleportation circle and captured pass-amulets are primary entry paths to Kolat Towers, bypassing the force field.") Hmm: the exact line 452 text is "- **Kolat Towers** — The Yellowspire teleportation circle and captured pass-amulets are primary entry paths to Kolat Towers, bypassing the force field." ✔.
- **Kolat Towers.** Identity reveal `campaign/structure/arc-i-kolat-towers.md:213-221` (the reveal list; quoted in part: "*The Manshoon Identity Reveal.* This is **Kolat Towers**'s dramatic centerpiece. Three independent evidence trails converge:" — `:213`). The Event Outcomes:
> "*Manshoon Event Outcomes.*" — `campaign/structure/arc-i-kolat-towers.md:255`
> "Record one of three Manshoon Event Outcomes. Each is read directly in **Vault of Dragons**." — `:257`
> "- **Manshoon Destroyed.** Both Manshoon (the clone of a clone) and the simulacrum were eliminated during the raid. The Splinter cell collapses within a tenday — Vevette (if alive) attempts to hold the surviving operatives together but lacks Manshoon's authority and his clone-network insurance. No Manshoon at the Vault. The party arrives at **Vault of Dragons** facing Aurinax without a third-party obstacle." — `:259`
> "- **Manshoon Simulacrum Only.** Manshoon was destroyed but the simulacrum survived and escaped (or was not found). The simulacrum has no 6th-level or higher spell slots and no staff of power. It arrives at the Vault with reduced capabilities and diminished tactical creativity — it can execute plans Manshoon taught it but cannot adapt to novel situations effectively." — `:260`
> "- **Manshoon Alive.** Manshoon survived (escaped, negotiated, or was never reached). He arrives at the Vault at full strength with surviving lieutenants and the staff of power. The hardest **Vault of Dragons** configuration. He will have had time to prepare." — `:261`
Escalation table: "| Unaware | Standard; gaps on normal rotation | Standard roster; Sidra assumes visitors are guests until credentials fail | Manshoon studying in E13; simulacrum dormant in E7 | 30 min |" — `arc-i-kolat-towers.md:101`.
- **Vault of Dragons.** `campaign/structure/arc-j-vault-of-dragons.md:34` ("| Manshoon | **Kolat Towers** Scene 6 (if run) | **Manshoon Destroyed** / **Manshoon Simulacrum Only** / **Manshoon Alive**. If **Kolat Towers** was never run, treat as **Manshoon Alive**, undiminished, and unidentified — the party has not yet assembled the Identity Reveal. |"); `:210` ("- **Manshoon Alive** (or **Kolat Towers** not run). Full strength: staff of power in hand, surviving lieutenants at his side, and — if he reached the vault first through his own intelligence network — the advantage of having had time to prepare a position rather than react to the party's arrival. This is the hardest **Vault of Dragons** configuration, and the default one if **Kolat Towers** was skipped.").
- **Sea Maidens Faire.** `campaign/structure/arc-h-sea-maidens-faire.md:202` ("*The Manshoon Parallel Strike.* Manshoon knows Eye #3 is aboard the Scarlet Marpenoth. His intelligence sources — scrying via simulacrum, double agents in multiple factions, Zhentarim informants in the Dock Ward — have confirmed the target. He dispatches a strike team regardless of what path the party has chosen."); `:278` ("**Manshoon's Zhentarim.** If the Zhentarim strike team was defeated, Manshoon knows — the pass-amulets went dark.").
- **Doom Raiders gates.** `campaign/quests/faction-events/doom-raiders/00-first-meeting/design-notes.md:11`: "...the party learns it late, at the Faction Outposts Interrogation House, where **Manshoon Named** is set." `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:27`: "- **Manshoon Named.** Until **Manshoon Named** is marked, every Doom Raider says "Floxin's cell", "the other cell" or "the Splinter", and calls Kolat Towers "the towers in the Southern Ward"."
- **The offer in the Kolat Towers adventure.** "The characters' best chance of survival is to convince {@creature Manshoon|WDH} that they can be cowed or bribed into working for him. Weary of his conflict with the Xanathar Guild, {@creature Manshoon|WDH} suggests that the characters prove their usefulness to him by hunting down and killing {@creature Xanathar|WDH} in its lair (see chapter 5)." — `sources/adventure-wdh.json:30256` (the Villains page keeps the same offer at `villains/manshoon.md:76`).

---

## F. Gaps a Background would need (sourced facts to stay consistent with)

Ruling 15 and 17 apply: where the sources are silent, invent with `[design]`; `[research]` marks a claim a source might settle. Constraints: nothing invented may contradict a campaign, adventure or Alexandrian fact; nothing may reveal or change a secret, an Event Outcome, a quest result or the Grand Game balance; no new named Notable Figure unless a source already names them (the wiki names Asmuth, Chess, Calkontor, Harlshoon, Theilon Greencloak and Ulsan Baneservant; Fzoul Chembryl is named in the campaign).

1. **Mother, family and birthplace.** Wiki: "Manshoon was born in Zhentil Keep in the ... to Harlshoon, the first lord of Zhentil Keep." (`W:78`). Campaign: born 1229 DR in Zhentil Keep (`campaign/setting/villains/manshoon.md:25`). No mother or other relative is sourced. A nameless relative or place is allowed under ruling 17.
2. **Childhood and the brother.** Wiki: Asmuth blinded in the barrow and later killed by Manshoon (`W:80`). Campaign: none. If the Background uses it, it is the wiki's account (edition not stated) and the drafter names Asmuth only as the wiki does.
3. **Formative events before the Zhentarim.** Wiki: the barrow sword, the hand blown off, the wand traded for the hand (`W:80`); the defection of Chess and the killing of the usurper (`W:82`). Campaign: none.
4. **The clone's life in Undermountain.** Campaign: "a body activated in Undermountain when the Manshoon before it died" and Halaster "tolerated the clone for a time out of professional curiosity" (`arc-i-kolat-towers.md:13`). Adventure: "The one presently in Waterdeep escaped death by hiding out in Undermountain, where he eventually ran afoul of Halaster Blackcloak." (`sources/adventure-wdh.json:32217`). Nothing sourced about what he did there. `[design]` only if it does not reveal a secret.
5. **The arm.** Campaign: lost at the elbow; "with a blade that prevented magical regrowth" (`arc-i-kolat-towers.md:13`). Wiki: "the original was kept and reanimated by Halaster" (`W:123`). The guardian is area 1a of Level 9 (`sources/adventure-wdh.json` is not the source; `adventure-wdmm.json:26133`).
6. **Who he cares about.** No living person is sourced as a personal tie. Sidra is "the only person in the cell whose loyalty Manshoon has never tested" (`04-sidra-romeir.md:25`). The apprentices and the lieutenants are employees. `[design]` required; keep it nameless or use an already-named person.
7. **Personal goals.** Campaign goals: the Weave, the blackmail, the Council (`villains/manshoon.md:80`; `01-manshoon.md:16`). Adventure: Wizard-King and Halaster (`sources/adventure-wdh.json:32219`). No personal goal beyond the job is sourced. `[design]` required (ruling 17). The personal goal sits beside the Motivations and Emotions lines (kept verbatim).
8. **Fear.** Adventure: "Fearing that he might be destroyed by his foes, {@creature Manshoon|WDH} magically crafted several clones" (`sources/adventure-wdh.json:32216`). Campaign: the stasis clone spell is "his insurance against dying for good" (`villains/manshoon.md:82`). A personal fear would be `[design]`.
9. **Losses.** Wiki: the father poisoned by Calkontor (`W:78`); the brother Asmuth killed by Manshoon (`W:80`). Campaign: the lost arm (`villains/manshoon.md:29`) and the apprentice disintegrated (book p.95). The loss he still feels is not sourced; `[design]`.
10. **Faith.** Wiki: "Manshoon and his magelings pledged fealty to Bane" (`W:85`); patron deity Mystra (`W:18`). Campaign: the cell has no creed (`organizations/09-manshoons-zhentarim.md:46`). His own faith is not sourced.
11. **Places.** Kolat Towers (`villains/manshoon.md:31`); the sanctum (`organizations/09-manshoons-zhentarim.md:55`); Yellowspire's circle (`bane.md:82` and `castle-ward.md`). A place he loves is not sourced; `[design]`.
12. **Signature belongings.** All sourced (A16).
13. **Age.** Only "much older than he looks" (`sources/adventure-wdh.json:30254`) and the wiki's birth year (`W:22`).
14. **Stat block class.** D17. `[research]` for the class; the campaign has no stat source.
15. **"Council majority".** D14. Only the Notable page says it.
16. **Urstul's species.** The Notable and Org pages say "Illuskan human" (`02-urstul-floxin.md:5`; `09-manshoons-zhentarim.md:100`). The adventure lines grepped for Urstul (`sources/adventure-wdh.json:32640-32644`) give no species. Not verified.
17. **Overview constraint.** The Overview must not carry the clone, the simulacrum, the Weave or the Eyes. The Org's public face is "Zhentarim crews with flying snake tattoos work Waterdeep's back streets..." (`organizations/09-manshoons-zhentarim.md:113`; the Watch-arrest clause is quest-time, C4). The Villains page's Overview: "A name the party does not have yet. The hard-edged Zhentarim operatives working Waterdeep's streets answer to someone, and none of them will say who." (`01-manshoon.md:30`, the Notable page's own Overview).

---

## G. Inner-life facts from the sources (fears, habits, loves, grudges, losses, a place or person they care about)

- **Fear of destruction (adventure):** "Fearing that he might be destroyed by his foes, {@creature Manshoon|WDH} magically crafted several clones-but a mishap caused all of them to be awakened at once, whereupon they tried to destroy one another in a series of conflicts that came to be known as the {@creature Manshoon|WDH} Wars." — `sources/adventure-wdh.json:32216`
- **Fear of exposure (adventure):** "The risk of exposure keeps him hidden, and the characters can thwart him by furnishing his enemies with proof that he's alive (after a fashion) and operating in Waterdeep." — `sources/adventure-wdh.json:26738`
- **Pride about the arm (Notable and voice):** "frustrated pride about his artificial arm" — `01-manshoon.md:14`; "His frustrated pride about the arm and Halaster surfaces as one clipped, bitter sentence, then composure again." — `manshoons-zhentarim.md:15`
- **Habit with the arm (voice and adventure):** "He flexes the artificial hand before a decision." — `manshoons-zhentarim.md:20`; "attaches a metal appendage to the withered stump of his left arm" — `sources/adventure-wdh.json:30250`.
- **Habit with the mask (adventure):** "The mask on the table is nonmagical, but {@creature Manshoon|WDH} likes to put it on before meeting with his followers." — `sources/adventure-wdh.json:30264`
- **Habit of capture (Notable):** "He prefers to capture rather than kill (prisoners answer questions; corpses do not)" — `01-manshoon.md:24`
- **Curiosity (Alexandrian, book p.16):** "Manshoon wanted to know where that money has gone." — [PDF-IMAGE] `sources/1. The Villains.pdf`, book p.16 [PDF p.4 of 7]
- **Need to stay in the game (Alexandrian, book p.16):** "After he lost his Eye to Xanathar, Manshoon needed to get back in the game." — [PDF-IMAGE] book p.16 (the sentence sits under "CHAPTER 1 – A FRIEND IN NEED")
- **Amusement (adventure):** "{@creature Manshoon|WDH} is amused by the creature, so he keeps it alive but locked in the cell." — `sources/adventure-wdh.json:28504`
- **Love of books (adventure):** "{@creature Manshoon|WDH} has amassed a sizable collection, including ten rare volumes he removed from Duhlark Kolat's collection." — `sources/adventure-wdh.json:30150`
- **Contempt for followers (adventure):** "since he considers all his followers expendable." — `sources/adventure-wdh.json:30255`
- **Staff under the bed (adventure):** "grabs his {@item staff of power} (which he hides under the bed)" — `sources/adventure-wdh.json:30257`
- **Grudge with Halaster (adventure and Notable):** "Halaster captured {@creature Manshoon|WDH} and amputated his left arm at the elbow for reasons unknown." — `sources/adventure-wdh.json:32217`; Notable: "dark fascination with a centuries-old wizard who lost an arm to Halaster Blackcloak and refuses to stop scheming" — `01-manshoon.md:12`.
- **Trust (campaign):** "Access to Kolat Towers is something Manshoon grants and can withdraw." — `campaign/setting/organizations/09-manshoons-zhentarim.md:41`
- **The person he trusts most (campaign):** Sidra, "the only person in the cell whose loyalty Manshoon has never tested, because testing it would mean he does not already know the answer." — `04-sidra-romeir.md:25`
- **The person who serves him most (Manafret, Notable):** "loyal warmth toward Manshoon expressed through excellent food" — `campaign/setting/notable-figures/manshoons-zhentarim/10-manafret-cherryport.md:13` (Manafret's own emotion; not Manshoon's)
- **Wiki, the loss in the barrow:** "Manshoon made sure his blind brother Asmuth fell off a bridge to his death before they returned to the keep where he and Chess planned to dispose of the usurpers." — `W:80`
- **Wiki, the grudge with Elminster:** "Elminster claimed he had personally killed twenty-and-one Manshoon clones by the {{YearlinkName|1357}}." — `W:90`

---

## Not found (searched; not in the sources)
- Personal goals beyond the faction and the job: searched `campaign/` and the adventure for Manshoon with "wants", "fear", "love", "family", "mother", "brother". Only the wiki's Asmuth, Harlshoon and Chess lines exist (wiki only).
- A mother, wife or child of Manshoon in the campaign or the adventure: none found.
- "Mage" as Manshoon's stat block: no source found (searched "with modifications" and "Mage" near Manshoon).
- A CR or class for the main Manshoon stat block in the JSON: none (only the simulacrum's CR 8).
- "Council majority" beyond `01-manshoon.md:16` (D14).
- Urstul's species in the adventure entries read (F16).
- A vote count for the Masked Lords' Council: none.
- A personal dealing between Laeral Silverhand and the cell: "No source records a dealing between Laeral Silverhand and the cell." (`campaign/setting/organizations/09-manshoons-zhentarim.md:92`).

## Not readable
- `sources/Other remix files/` `.docx`: `Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` is listed in `sources/SOURCE_GUIDE.md:688` for the Doom Raiders, not Manshoon's cell. Not opened.
- Alexandrian PDFs: opened with the Read tool as images; no pdftotext. Every PDF quote is `[PDF-IMAGE]`.
- `sources/research/pass4-bundles/manshoon/wiki.txt` (1979 lines): grepped, not re-read.

## Scope note
A Grep for `Manshoon` across `campaign/` returned 1142 occurrences in 235 files (count mode). This report covers the setting, guide, quest-structure, gazetteer and deity files that hold the figure's history, the day-one state or a routed fact. The `campaign/quests/faction-events/` gates (Doom Raiders, Harpers, Emerald Enclave and others) were searched for "Manshoon Named" and the Floxin status; they are routed in E2 and not quoted in full.
