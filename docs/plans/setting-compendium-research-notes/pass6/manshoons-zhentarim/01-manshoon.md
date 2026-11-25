# Pass 6 research notes: Manshoon

Page: `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1-17 and the user rulings bind)
Faction organization page: `campaign/setting/organizations/09-manshoons-zhentarim.md`
Villains page: `campaign/setting/villains/manshoon.md` (owns the phases, goals and relationships; its `## Background` is at line 23)
Factions Guide page: `campaign/guides/factions/10-manshoons-zhentarim.md`
Voice profile: `.claude/skills/character-voices/voices/manshoons-zhentarim.md` (`### Manshoon` at line 8)
Model notes used for shape: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md` (the path given for this folder did not exist; the pilot notes for the Xanathar's Guild folder are the format used). Model Notable page read: `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md`. `09-grinda-garloth.md` was not opened because it is a minor-figure model and nothing here depends on it.

## Method and caveats

- Campaign files: Read and Grep. Line numbers are the Read or Grep line numbers. Grep output marked `[Omitted long matching line]` was re-read with Read at that line.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` and other tags are left as written. `sources/adventure-wdmm.json` for the Undermountain arm.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. The PDF quotes were transcribed from the rendered page images (Read with `pages`). Each is tagged **[PDF-IMAGE]**, cited with the printed page and the PDF page in brackets, and must be checked against `pdftotext -layout` before any sentence goes into prose.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-manshoons-zhentarim/01-manshoon.txt` (the Manshoon extract; `W:` below), and the Zhentarim page in `sources/research/pass5-bundles/zhentarim/wiki.txt` (`W5:`). `sources/research/pass4-bundles/manshoon/wiki.txt` was searched (grep hits at lines 80, 82, 84 for Asmuth and Chess carry the same early-life passage as `W:` line 80) but not re-read in full. Wiki citation keys print no edition on most lines. Where the wiki names an edition in its citation key it is given. Inferred editions are marked.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## A. Background facts by theme

### A1. Origin, birth and home

**Birth year and city (wiki only)**
> "Manshoon was born in Zhentil Keep in the {{YearlinkName|1229}},<ref name="GHotR-p125">{{Cite book/The Grand History of the Realms|125}}</ref> to [[Harlshoon]], the first lord of Zhentil Keep." (`W:78`)

Campaign, same facts with the wiki as the source:
> "- Manshoon was born in Zhentil Keep in 1229 DR and founded the Zhentarim, also called the Black Network, in 1261 DR (Forgotten Realms Wiki, citing *The Grand History of the Realms* and *Ruins of Zhentil Keep*; the wiki does not tag their editions). The published adventure calls the original "one of the founders", and the campaign keeps that wording (**The Founding of Chains**)." (`campaign/setting/villains/manshoon.md:25`)

Infobox (wiki, 5e not stated; the infobox dates are fixed):
> "| dob            = 1229" (`W:22`)
> "| home           = [[Citadel of the Raven]], [[Moonsea]]" (`W:10`)
> "| formerhomes    = [[Zhentil Keep]], [[Moonsea]]<ref name="Drag415.tMDoM">{{Cite dragon/415/History Check: The Many Deaths of Manshoon}}</ref>" (`W:11`)

Published adventure, the founder wording:
> "The original {@creature Manshoon|WDH} was one of the founders of the Zhentarim. Evil to the core, he made enemies all across Faerûn, including other powerful spellcasters such as Khelben Arunsun and Elminster. Fearing that he might be destroyed by his foes, {@creature Manshoon|WDH} magically crafted several clones-but a mishap caused all of them to be awakened at once, whereupon they tried to destroy one another in a series of conflicts that came to be known as the {@creature Manshoon|WDH} Wars." (`sources/adventure-wdh.json:32216`)

Campaign history, the founder wording (settled by the user, Session 51, per the history page):
> "- The published adventure calls Manshoon "one of the founders" of the Zhentarim (`adventure-wdh.json` lines 560 and 32216), and this page keeps that wording. The wiki calls him the founder." (`campaign/setting/history/04-the-founding-of-chains.md:31`)

### A2. Family, childhood and early life (wiki only; no campaign source)

> "Manshoon, his brother [[Asmuth]]; and [[Chess]], the son of their father's chief rival, [[Calkontor]], were sent off together as [[adventurer]]s to prove themselves worthy of being lords like their fathers. While his sons were away, Harlshoon was poisoned by Calkontor, but, with his dying breaths, he threw Calkontor out of a tower window. The trio's fathers' places were usurped by a pair of opportunists, [[Theilon Greencloak]] and [[Ulsan Baneservant]], the deaths blamed on foreign assassins, while the unknowing lord-princes continued their adventures together.<ref name="RoZK-CB-p13">{{Cite book/Ruins of Zhentil Keep/Campaign Book|13-14}}</ref>" (`W:78`; edition not stated; citation key *Ruins of Zhentil Keep* Campaign Book pp.13-14)

> "Asmuth was blinded and Manshoon had one of his hands blown off when he carelessly grabbed for the sword. Chess saved both of their lives, and the three fled when the sword animated itself, appearing to attack the Harpers. They came across a party of other adventurers and murdered them all in their sleep. Manshoon recovered a [[wand]] and a [[spellbook]]. He traded the wand for his hand to be restored but kept the spellbook as he secretly planned to study [[the Art]], having been inspired by the magic of the sword." (`W:80`; same citation key as `W:78`)

> "Manshoon made sure his blind brother Asmuth fell off a bridge to his death before they returned to the keep where he and Chess planned to dispose of the usurpers." (`W:80`)

> "However, unknown to him, Chess defected in exchange for his father's seat on the council. It was, however a double cross: Chess, Manshoon, and their childhood friend Fzoul Chembryl killed the usurper. They claimed their rightful council seats and supported Fzoul's rise through the ranks of the Banite priesthood." (`W:82`)

Campaign names of Fzoul (no childhood link in the campaign):
> "- **1263 DR** ... (`campaign/setting/history/04-the-founding-of-chains.md:30`)" is not quoted here; the line the drafter needs is: "- Manshoon was born in Zhentil Keep in 1229 DR and became one of the city's lords. He founded the Zhentarim in 1261 DR, and the Banite priest Fzoul Chembryl joined him in 1263 DR." (`campaign/setting/history/04-the-founding-of-chains.md:30`)

### A3. Founding the Zhentarim (1261 DR)

> "Feeling exposed, Manshoon immediately set about creating a cabal of mages, his [[Black Cloaks]], to protect him, recruiting Fzoul early on. Not long afterward, in the {{YearlinkName|1261}}, he founded the Zhentarim. However, knowing the priests would obey Bane over anyone else and assuming the wizards were just as ambitious as he was, Manshoon held little trust for any of his new allies. He sent out spies and was determined to raise his powers in the arcane far above anyone else in Zhentil Keep." (`W:85`)

> "However, in order to do this, Manshoon and his magelings had to pledge fealty to Bane, promising to lead the faith to even greater heights of power than the weakening High Imperceptor had." (`W:85`)

> "In secret, Manshoon embarked on another plan for his organization. Having little interest in empire-building, he set his Zhentarim wizards the task of establishing trade routes between the Moonsea and the untapped markets of the [[Sword Coast]]." (`W:87`)

Campaign, faith of the cell (as a wiki-sourced claim, untagged on the campaign line):
> "The wiki says Manshoon and his magelings pledged fealty to Bane to win over the Banite priests, and it lists Bane as the Zhentarim's favored deity, formerly Cyric (Forgotten Realms Wiki, *Manshoon* and *Zhentarim*, edition not tagged)." (`campaign/setting/organizations/09-manshoons-zhentarim.md:46`)

Infobox patron deity (wiki, 1e source):
> "| patron deity   = [[Mystra]]<ref name="DMSotR-25">{{Cite book/Forgotten Realms Campaign Set/DM's Sourcebook of the Realms|25}}</ref>" (`W:18`; the campaign uses Mystra only as the god Manshoon means to supplant, `villains/manshoon.md:21`)

Stasis clone spell, the wiki's account:
> "During this period, Manshoon developed his ultimate insurance plan, the notorious ''[[stasis clone]]'' spell." (`W:87`)

Campaign, same fact:
> "- Manshoon built the stasis clone spell as insurance against his enemies. Over the years he died several times and returned in a new body." (`campaign/setting/history/04-the-founding-of-chains.md:42`)

Pass5 Zhentarim page, founding (wiki, edition not tagged):
> "The Zhentarim was founded in the {{YearlinkName|1261}}, by the power-hungry wizard Manshoon, the lord of Zhentil Keep, as a tool for his ambitions of expanding his realm of control." (`sources/research/pass5-bundles/zhentarim/wiki.txt:196`)

### A4. The clones, the 1370 DR death and the Manshoon Wars

Villains page (lines 27-28, quoted in full):
> "- In 1370 DR Fzoul Chembryl and Lord Orgauth killed him and found themselves facing a dozen or more clones. Each clone believed he was the real Manshoon and felt driven to kill the others, and the fights are the Manshoon Wars (Forgotten Realms Wiki, 3e *Forgotten Realms Campaign Setting* p. 283). The published adventure says a mishap woke every clone at once (5e *Waterdeep: Dragon Heist*)." (`campaign/setting/villains/manshoon.md:27`)
> "- Three clones survived the wars. One rejoined the Zhentarim and conceded leadership to Fzoul, one became the vampire Orbakh in Westgate, and one took refuge in Undermountain with Halaster (Forgotten Realms Wiki, 3e *Forgotten Realms Campaign Setting* pp. 282-283). The published adventure agrees that at least three survive and says the clone now in Waterdeep is the one that hid in Undermountain (5e *Waterdeep: Dragon Heist*)." (`campaign/setting/villains/manshoon.md:28`)

Published adventure:
> "Now the original {@creature Manshoon|WDH} is dead, and it's widely believed that all his clones were destroyed as well. In fact, at least three are still alive. The one presently in Waterdeep escaped death by hiding out in Undermountain, where he eventually ran afoul of Halaster Blackcloak. After a brief spell duel, Halaster captured {@creature Manshoon|WDH} and amputated his left arm at the elbow for reasons unknown. {@creature Manshoon|WDH} escaped imprisonment and fled Undermountain, taking refuge in the city above. Attempts to magically regenerate his severed limb failed, forcing him to craft an artificial arm and hand for himself." (`sources/adventure-wdh.json:32217`)

Wiki:
> "In the {{YearlinkName|1370}}, Manshoon was "slain" again by Fzoul and Lord [[Orgauth]], who then found themselves facing around a dozen clones that the wizard had created. Each of the clones was convinced that he was the real Manshoon and was inexplicably compelled to slay his rival clones. Most of these perished in the ensuing battles." (`W:92`)
> "Three clones, who mastered this killing compulsion by means of spells and devices, survived, with the one that returned to the Zhentarim appearing to be 'the' Manshoon." (`W:95`)
> "One of the three remaining clones returned to the Zhentarim, conceding leadership to Fzoul and entering into some sort of accommodation with him." (`W:97`)
> "The third took refuge in [[Undermountain]] with [[Halaster]]." (`W:101`)

Wiki, post-1370 fates (the campaign does not follow these; see Section D):
> "The second clone assumed a position of power among the [[Night Masks]] of [[Westgate]], calling himself '''Orbakh'''<ref name="FRCS-p283" /> or '''Orlak II'''." (`W:99`)
> "By [[1372 DR]], he had redoubled his arcane research, seeking ways to transfer his consciousness from one clone to another at will." (`W:97`)

Pass5 Zhentarim page (wiki, 3e citation key):
> "In the {{YearlinkName|1370}}, Fzoul and Lord [[Orgauth]] attacked and killed Manshoon. However, Manshoon lived on through clone bodies, many of whom fought and killed each other. Of these, one returned to the Zhentarim, conceded all leadership to Fzoul, and worked as an agent." (`sources/research/pass5-bundles/zhentarim/wiki.txt:224`)

Alexandrian, the clone wars and the surviving clone:
> "Most of Manshoon's clones were destroyed during the Manshoon Wars, but yet another has recently returned to Waterdeep (claiming, as they all do, to be the one true Manshoon)." ([PDF-IMAGE] `sources/1. The Villains.pdf`, book p.16 [PDF p.4 of 7]; Zhentarim section)

Campaign history, the clone's count and the design choice:
> "- In 1370 DR Fzoul and Orgauth killed him and found themselves facing a dozen or more clones." (not the exact line; the exact campaign line is) "- In 1370 DR Fzoul Chembryl and Lord Orgauth killed him and found themselves facing a dozen or more clones. Each clone believed he was the real Manshoon and felt driven to destroy the others. These fights are the Manshoon Wars." (`campaign/setting/history/04-the-founding-of-chains.md:43`)
> "- The campaign makes the man in Waterdeep a clone of a clone." (see A5; `campaign/setting/history/04-the-founding-of-chains.md:47`) — exact line: "- The man in Waterdeep is "a clone of a clone". He claims to be the one true Manshoon, as every surviving clone does." (`campaign/setting/history/04-the-founding-of-chains.md:47`)
> "- The Zhentarim outlasted the 1370 DR death. Fzoul led the Network after it, and one Manshoon clone served as a free agent under him." (`campaign/setting/history/04-the-founding-of-chains.md:48`)

Wiki, the Waterdeep clone's account (the campaign uses the adventure's version):
> "The ancient archwizard had infiltrated Waterdeep years before and had been hiding out in [[Kolat Towers]] ever since, plotting to replace the [[City Watch (Waterdeep)|City Watch]] with Black Network mercenaries that were loyal to him alone and to rule Waterdeep as Wizard-King." (`W:123`)

### A5. Halaster, the arm and the Undermountain clone

Villains page, line 29 (quoted in full):
> "- Halaster Blackcloak captured the Undermountain clone after a brief spell duel and amputated his left arm at the elbow. Magic could not regrow it, so Manshoon crafted an artificial arm and hand for himself (5e *Waterdeep: Dragon Heist*). The severed forearm remains in Undermountain as an undead guardian (5e *Waterdeep: Dungeon of the Mad Mage*, area 1a)." (`campaign/setting/villains/manshoon.md:29`)

Undermountain area, quoted (Level 9):
> "{@b Undead Guardian}. Floating in the middle of the room, 15 feet above the floor, is a man's withered left hand and forearm, severed at the elbow." (`sources/adventure-wdmm.json:26129`)
> "The limb belonged to a human archmage named Manshoon—or, more precisely, to one of his clones. The clone challenged Halaster to a spell duel and lost more than just the contest. Halaster turned the limb into a guardian that attacks all intruders until the Mad Mage or a creature that looks like him waves it off. The limb has the statistics of an {@creature archmage}, with these changes:" (`sources/adventure-wdmm.json:26133`)
> Level placement: `sources/adventure-wdmm.json:24359` reads `"name": "Level 9: Dweomercore"` and `:26119` reads `"name": "1a. Left Hand of Manshoon"`; the Level 10 heading is at `:27748`. Area 1a is in Level 9. The Undermountain page says the same: "Manshoon's severed hand floats here as an undead guardian." (`campaign/setting/geography/undermountain-and-skullport.md:70`, row "9 | Dweomercore")

Campaign quest opener (the drafter may quote it as backstory; it is the Kolat Towers opener, which the Villains page cites):
> "The Manshoon who now occupies Kolat Towers is a clone of a clone — a body activated in Undermountain when the Manshoon before it died, as the clone network was designed to do. Halaster Blackcloak, who tolerated the clone for a time out of professional curiosity, eventually severed Manshoon's left arm at the elbow with a blade that prevented magical regrowth. The clone fled Undermountain carrying the staff of power he had smuggled in and arrived in Waterdeep to find the Kolat Towers abandoned, the force field still running on its original enchantment, and the amulet manufacture instructions in Duhlark's study. Manshoon needed a base. The towers were available." (`campaign/structure/arc-i-kolat-towers.md:13`)

Wiki, the arm (for the grudge):
> "During the latter battle, Manshoon's left arm was severed and proved impossible to magically regenerate, forcing him to use a metal prosthetic instead, while the original was kept and reanimated by Halaster." (`W:123`)

Notable page, the arm as emotion (campaign, day-one):
> "**Emotions.** Manshoon most often feels cold patient calculation, contemptuous superiority, precise anger reserved for specific targets, possessive ambition, frustrated pride about his artificial arm, and the absolute certainty that he is the one true Manshoon." (`campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:14`)

Voice profile (day-one manner about the arm):
> "His frustrated pride about the arm and Halaster surfaces as one clipped, bitter sentence, then composure again." (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:15`)
> "**Quirks:** He flexes the artificial hand before a decision. He corrects small inaccuracies in what others say about him. He insists he is "the one Manshoon"." (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:20`)

### A6. Kolat Towers and the Southern Ward (the base, day-one)

Villains page (lines 31-32):
> "- Kolat Towers is a crumbling pair of towers in the Southern Ward, built by the Kolat brothers and abandoned years ago. A force field with the properties of a wall of force still surrounds them. Manshoon rarely leaves, and he uses a teleportation circle when he must, so nobody sees him enter or leave (5e *Waterdeep: Dragon Heist*; **Kolat Towers** quest opener)." (`campaign/setting/villains/manshoon.md:31`)
> "- Neighbors can see the force field and the light of *continual flame* spells in the windows, and most believe the towers are abandoned or haunted by the Kolat brothers. Manshoon posts no visible guards because he wants that belief to hold (5e *Waterdeep: Dragon Heist*)." (`campaign/setting/villains/manshoon.md:32`)

Published adventure, the towers and the ward:
> "{@creature Manshoon|WDH} took control of Kolat Towers, a crumbling residence in the Southern Ward that was abandoned years ago by the two wizards who built it. The edifice is surrounded by a magical barrier that has the properties of a wall of force. {@creature Manshoon|WDH} rarely leaves the towers and uses a teleportation circle when he must do so, and thus is never seen entering or leaving." (`sources/adventure-wdh.json:32218`)
> "This dilapidated, two-towered edifice stands tall in the Southern Ward. Its neighbors are aware of the magical force field that surrounds it, and they can see light from {@spell continual flame} spells spilling out of the windows. Despite these persistent magical effects, most folk believe the structure is abandoned. Others think it's haunted by the ghosts of the Kolat brothers. They're wrong, of course." (`sources/adventure-wdh.json:26797`)
> "{@creature Manshoon|WDH} posts no visible guards outside Kolat Towers, since he wants others to believe the site is abandoned. The evil wizard and his underlings come and go using teleportation circles inside the towers." (`sources/adventure-wdh.json:26798`)

The adventure's Kolat history (conflicts with the campaign; see D):
> "Kolat Towers once belonged to two eccentric brothers, Duhlark and Alcedor Kolat. Both were wizards." (`sources/adventure-wdh.json:26863`)
> "Duhlark's paranoia continued to grow, until he suspected Alcedor of selling their secrets. Alcedor left the towers, never to be heard from again, and Duhlark became a recluse who died in his own fortress." (`sources/adventure-wdh.json:26865`)

Campaign opener, the Kolat brothers and the towers (quoted in full):
> "Duhlark Kolat built the towers that bear his name during the late fourteenth century as an experiment in paranoid architecture. His brother Alcedor wanted a home; Duhlark wanted a fortress that could withstand siege, scrying, and betrayal from within. The result — two interconnected stone towers in the Southern Ward, linked by a bridge at the third floor and bound together by a force field that covered the entire structure from basement to roof — was more fortress than home. Alcedor moved in anyway. The force field admitted no one without a specially keyed amulet. Alcedor accepted this as the cost of living with his brother. He died in the towers in 1385 DR under circumstances that remain unclear. Duhlark survived him by nine years before being found dead in his study, apparently of old age, with the force field still running." (`campaign/structure/arc-i-kolat-towers.md:9`)

Campaign, the Splinter and the pass-amulet (day-one):
> "He spent two years building the Splinter cell — the faction that bears his name but operates independently of the Zhentarim's surviving leadership. The structure is hub-and-spoke: Kolat Towers as the command center, with the Interrogation House in the North Ward and Yellowspire in the Castle Ward serving as field offices connected by teleportation circles. A pass-amulet system replaced the need for a trusted courier network; amulets could be revoked remotely, confiscating access without confrontation." (`campaign/structure/arc-i-kolat-towers.md:15`)

Campaign history, the sanctum (day-one):
> "- The sanctum: Behind the towers lies an extradimensional sanctum in a finite demiplane, which the original Manshoon created and his clones all know." (not an exact line; exact text is) "- **The sanctum:** Behind the towers lies an extradimensional sanctum in a finite demiplane, which the original Manshoon created and his clones all know. A teleporter ring and the circle in the towers are the way in (*Dragon Heist*, 5e)." (`campaign/setting/organizations/09-manshoons-zhentarim.md:55`)
> Adventure, same sanctum: "{@creature Manshoon|WDH}'s extradimensional sanctum exists in a finite demiplane. Created by the original {@creature Manshoon|WDH}, it is known to the wizard's clones, and it currently serves as the lair of the clone described in this adventure." (`sources/adventure-wdh.json:28796`)

Simulacrum and the Kolat sanctum (GM-only; keep out of the Overview):
> "The simulacrum in E7 is Manshoon's contingency against assassination. It was created seven years ago and has been ice-preserved since — a duplicate with half his hit points, none of his 6th-level or higher spell slots, and a different quality to its decision-making that those who know Manshoon well can identify after the fact. The simulacrum has never been activated outside of tests. Manshoon has never needed it. He is considering, for the first time in years, whether he might." (`campaign/structure/arc-i-kolat-towers.md:17`)
> Adventure: "{@creature Manshoon|WDH} uses the {@spell simulacrum} spell to create a magical duplicate of himself as needed. He has customized the spell to increase {@creature Manshoon Simulacrum|wdh|his simulacrum}'s hit points at the expense of its spellcasting ability." (`sources/adventure-wdh.json:32226`)
> "{@creature Manshoon|WDH} can have only one simulacrum at any given time, and he uses it as a subordinate to command his Zhentarim minions in the field. If his simulacrum is destroyed, {@creature Manshoon|WDH} creates another. Each simulacrum has the statistics of {@creature Manshoon|WDH}, with these changes:" (`sources/adventure-wdh.json:32227`)

### A7. The Splinter, the network and the Doom Raiders (day-one)

Villains page, line 33-34:
> "- He spent about two years building the Splinter, a cell that bears his name and works independently of the Zhentarim's surviving leadership. It is hub and spoke, with Kolat Towers as the command center and the Interrogation House in the North Ward and Yellowspire in the Castle Ward as field offices linked by teleportation circles. A pass-amulet system lets him revoke anyone's access from the towers (**Kolat Towers** quest opener)." (`campaign/setting/villains/manshoon.md:33`)
> "- He took a large part of the local network the Doom Raiders had built, and through it learned that Lord Neverember had used the local Zhentarim's resources to embezzle the vault's gold (Alexandrian Remix, *The Villains*, p. 16)." (`campaign/setting/villains/manshoon.md:34`)

Alexandrian, the same network (quoted in A4 at the clones line):
> "When he peeled off a large hunk of the local Zhentarim network that had been established by the Doom Raiders (see p. 198 of *Dragon Heist*), he became aware that Lord Neverember had used the local Zhentarim's resources to embezzle hundreds of thousands of gold dragons from the government." ([PDF-IMAGE] `sources/1. The Villains.pdf`, book p.16 [PDF p.4 of 7])

Alexandrian, Manshoon's motive for the embezzlement inquiry:
> "Manshoon wanted to know where that money has gone. He knew that Neverember didn't actually have it in his possession, so he sent agents to infiltrate Neverember's household in Neverwinter to find out." ([PDF-IMAGE] `sources/1. The Villains.pdf`, book p.16 [PDF p.4 of 7])

Published adventure, the cell's view of its enemies and the Doom Raiders:
> "The Zhentarim in Waterdeep is a fractured organization. Those who support {@creature Manshoon|WDH} want to destroy {@creature Xanathar|WDH} and seize political and economic control of the city. Those who oppose {@creature Manshoon|WDH} want to expose and destroy him before they are themselves apprehended or driven out of the city by the local authorities." (`sources/adventure-wdh.json:1445`)
> "Adventurers can't join {@creature Manshoon|WDH}'s cause, but they can join and receive aid from the Zhents who are opposed to him." (`sources/adventure-wdh.json:1446`)

Campaign, the cell's view of the Doom Raiders (`[research]` in the campaign):
> "- **The Doom Raiders Are Deserters:** The cell regards the Doom Raiders as deserters who stole its name `[research]`, will not cooperate with them, and works to dismantle their people and the network they built." (`campaign/setting/organizations/09-manshoons-zhentarim.md:45`)

### A8. The Eyes, Xanathar and the envoys (pre-start; the events are dated before Ches 1 except where noted)

Villains page lines 35-36 (quoted in full; see C for the quest-adjacent part):
> "- His agents stole the Neverwinter Eye from the Protector's Enclave. His envoys brought it to Xanathar three months before the fireball, and Xanathar killed them and kept it as Eye #1 (**Running the Villains**; **The Long Shadow**)." (`campaign/setting/villains/manshoon.md:35`)
> "- His cell then seized Renaer Neverember's mourning locket on the night before Ches 1 and pried it open at the Candle Lane warehouse. Xanathar's Guild raided the warehouse and carried the Eye off without knowing what it was, and Bregan D'aerthe agents inside Xanathar's hideout lifted it that night. It became Eye #3, and Manshoon holds no Eye (**Running the Villains**)." (`campaign/setting/villains/manshoon.md:36`)

Campaign, Eyes and Manshoon:
> "**Manshoon:** He holds no Eye. He needs the Stone and all three Eyes, and his plan is to let someone else open the vault and then take it from them." (`campaign/setting/lore/stone-of-golorr-and-the-eyes.md:44`)
> "- **Eye #1, Xanathar:** Manshoon's Zhentarim stole it from the Protector's Enclave in Neverwinter. About three months before the fireball, Manshoon sent two lieutenants to Skullport with it as a gift. Xanathar ate them and kept the Eye, and Ott Steeltoes put it in the bowl of Sylgar, Xanathar's goldfish, because it was a pretty color. Xanathar does not know what the Eye is." (`campaign/setting/lore/stone-of-golorr-and-the-eyes.md:40`)
> "**Eye #3, Jarlaxle:**" line is at `stone-of-golorr-and-the-eyes.md:42` (see C).

Campaign, Running the Villains:
> "**Eye #1** — formerly held by Manshoon's Zhentarim, who stole it from Protector's Enclave in Neverwinter. Xanathar killed the Zhentarim envoys who brought it to him and seized the Eye. It now resides in Xanathar's Lair sanctum." (`campaign/guides/gm-guide/running-the-villains.md:21`)
> "> **Eye #3:** Jarlaxle Baenre — aboard the *Scarlet Marpenoth*. Jarlaxle knows exactly what it is. It passed from Renaer's locket to the Zhentarim, then to Xanathar's Guild in the warehouse raid, and Bregan D'aerthe agents inside Xanathar's hideout lifted it that night. Manshoon holds no Eye." (`campaign/guides/gm-guide/running-the-villains.md:30`)

Campaign, the envoys in Xanathar's Guild history (day-one, pre-start):
> "About Nightal 1491 DR (derived), Manshoon's Zhentarim sent two lieutenants to Skullport with Eye #1 of the Stone of Golorr, which the cell had taken from the Protector's Enclave in Neverwinter. Xanathar heard their proposal, ate them and kept the Eye (**The Stone of Golorr and the Eyes**; **The Players Arrive**)." (`campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:45`)

Alexandrian, the envoys (book p.15):
> "Then the Zhentarim came to him with one of the Eyes and said, "We have two different parts of this puzzle. We'd like to make a deal." Xanathar was enraged at both their presumption and his own folly, slew the Zhentarim envoys, and took the Eye they had brought to him." ([PDF-IMAGE] `sources/1. The Villains.pdf`, book p.15 [PDF p.3 of 7])

Published adventure, a different route for the Stone (conflict; see D):
> "As Zhents loyal to {@creature Manshoon|WDH} try to forge an alliance with Xanathar, the Stone of Golorr is stolen." (`sources/adventure-wdh.json:838`)

### A9. Blackmail and the Masked Lords (pre-start)

Villains line 37 (quoted in full):
> "- He blackmails two Masked Lords. Corylus Thann is held over a scandal, and Jelenn Urmbrusk is held through a debt to a Splinter front, and their votes follow his preferences. The ledger documenting these arrangements lies in an arcane-locked drawer in his study, with a list of the Masked Lords whose identities he knows (**Kolat Towers** quest opener; 5e *Waterdeep: Dragon Heist*, which has Jelenn already in debt to him)." (`campaign/setting/villains/manshoon.md:37`)

Campaign, the list of five and the Lords (day-one):
> "Manshoon keeps a list of five Masked Lords whose identities he knows. They are Mirt, Corylus Thann, Thardouk Starbuckler, Jelenn Urmbrusk and Dorgar Adarbrent, and he has checked off Corylus and Jelenn as the two he is blackmailing." (`campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:63`)
Adventure, the same list (names and checkmarks):
> "Mirt" / "Corylus Thann √" / "Thardouk Starbuckler" / "Jelenn Urmbrusk √" / "Dorgar Adarbrent" (`sources/adventure-wdh.json:30308-30312`)

Adventure, the ledger (GM):
> "Inside is a leather-bound ledger that provides a paper trail implicating {@creature Manshoon|WDH} in two blackmail schemes." (`sources/adventure-wdh.json:30290`)
> "Corylus Thann, a racist Waterdavian noble, is paying the Zhentarim not to reveal that he hired Zhent thugs to assault non-humans." (`sources/adventure-wdh.json:30294`)
> "Jelenn Urmbrusk, a Waterdavian noble, receives regular payments from the Zhentarim to offset monies he loses in bad investments." (`sources/adventure-wdh.json:30295`)

Adventure, Jelenn's debt (conflicting direction; see D):
> "Fear of that exposure led her to borrow money from the Zhentarim instead—a decision she has come to regret. The Zhents working for {@creature Manshoon|WDH} promise to keep their relationship secret on the condition that she do everything in her power to further the group's welfare in Waterdeep." (`sources/adventure-wdh.json:30374`)

Campaign, Corylus (arc-i; conflicts with the adventure's "paying the Zhentarim"; see D):
> "Corylus Thann, a Masked Lord, was photographed in a situation that would end his career; he supplies Guild intelligence in exchange for the ledger's continued privacy. Jelenn Urmbrusk accumulated significant debt to a Splinter front organization; her votes in the Council of Guildmasters follow Manshoon's preferences without her ever being asked directly." (`campaign/structure/arc-i-kolat-towers.md:19`)

Campaign, the Masked Lords file (the hush money and debt, day-one):
> "Jelenn's debt to Manshoon's Zhentarim was borrowed to avoid borrowing from rival nobles, and the Splinter now holds it." (`campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:64`)

Org page, the Masked Lords paragraph (day-one):
> "The scandal is that Corylus once hired Zhentarim thugs to attack non-humans who sought political office, and the debt is a loan that Jelenn took from the Zhentarim because she feared the gossip a noble lender would cause (*Dragon Heist*, 5e)." (`campaign/setting/organizations/09-manshoons-zhentarim.md:67`)

### A10. Goals, wants and the published plan

Villains page, goals (lines 80-82, quoted in full):
> "- **Acquire the Stone of Golorr.** The Stone is a transformed aboleth encoded with ancient Weave knowledge, and Manshoon means to absorb the Weave and supplant Mystra. The vault's gold funds the process. Method: Stone recovery, then Weave absorption. He holds no Eye, because Xanathar killed the envoys who delivered Eye #1 as a gift and kept it, so he needs the Stone plus all three Eyes. Contingency: destroy the vault rather than cede it. Connects to **Gralhund Villa** and **Kolat Towers**." (`campaign/setting/villains/manshoon.md:80`)
> "- **Control Waterdeep's Underworld.** He means to eliminate Xanathar, absorb the Doom Raiders and marginalize Bregan D'aerthe. Method: patient erosion through targeted disruption and strategic violence. The Dock Ward conflict in Acts I–II is this plan in early operation." (`campaign/setting/villains/manshoon.md:81`)
> "- **Survive an Assassination.** The simulacrum is his contingency against assassination and his tactical decoy: it fights while he escapes. Defeating the Manshoon the party meets first may defeat only the simulacrum, and if it is destroyed he makes another. The stasis clone spell is a separate tool, his insurance against dying for good. Connects to the **Kolat Towers** design requirement." (`campaign/setting/villains/manshoon.md:82`)

Campaign, Weave goal (Org and Notable agree):
> "- **What Manshoon Wants:** The gold means nothing to him as wealth. He wants the Stone of Golorr for what it knows, because the Stone is a transformed aboleth and its centuries of absorbed memory encode ancient knowledge of the Weave's structure. Manshoon intends to use that knowledge to absorb the Weave and supplant Mystra, so the vault is an instrument and the Stone is the goal." (`campaign/setting/organizations/09-manshoons-zhentarim.md:65`)
> "**Motivations.** Manshoon wants to acquire the Stone of Golorr for the ancient Weave knowledge encoded in its aboleth memory, use that knowledge to absorb the Weave and supplant Mystra, fund his preparations with the vault's gold, and deepen his hold over Masked Lords Corylus Thann and Jelenn Urmbrusk into a full Council majority." (`campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:16`)

Published adventure, the published goal (conflict; see D):
> "{@creature Manshoon|WDH} aims to rule Waterdeep and replace the City Watch with Black Network mercenaries that are loyal to him alone. By bribing and blackmailing the Masked Lords, he hopes to oust {@creature Laeral Silverhand|WDH} as Open Lord and take her place, kill the Blackstaff, reduce the Masked Lords to mere vassals, and declare himself the Wizard-King of Waterdeep. Once the city is firmly in his clutches, {@creature Manshoon|WDH} will then turn his attention toward Undermountain, destroy Halaster once and for all, and claim the dungeon's riches." (`sources/adventure-wdh.json:32219`)
> "{@creature Manshoon|WDH} yearns to rule Waterdeep as a tyrant, take over the Zhentarim, and use both seats of power to plunder and control the Sword Coast." (`sources/adventure-wdh.json:26731`)

Villains page line 38 (acknowledges the difference):
> "- The published adventure gives him a different goal. He wants to oust Laeral Silverhand as Open Lord by bribing and blackmailing the Masked Lords, replace the City Watch with Black Network mercenaries, kill the Blackstaff, and then turn on Halaster (5e *Waterdeep: Dragon Heist*). The campaign's motive is the Weave goal under Goals, which comes from the campaign's own pages and has no published or Alexandrian source, and the blackmail of the Masked Lords stays." (`campaign/setting/villains/manshoon.md:38`)

Campaign, the Stone's own file, Manshoon's Stone plan (the Eyes file):
> "- **Manshoon's Zhentarim:** Manshoon wants the Stone for the ancient Weave knowledge in its aboleth memory. He means to use it to absorb the Weave and supplant **Mystra**, and the vault's gold pays for the preparations." (`campaign/setting/lore/stone-of-golorr-and-the-eyes.md:101`)

### A11. Enemies, and the shadow he works in (day-one)

> "He has a long list of powerful enemies, among them the Harpers, Elminster, Halaster and the Blackstaff. They would move against him if they learned he was in Waterdeep, so he operates in the shadows for now (5e *Waterdeep: Dragon Heist*)." (`campaign/setting/villains/manshoon.md:39`)
> "A head-on battle with {@creature Manshoon|WDH} isn't likely to go well for the characters. That said, the wizard's greatest weakness is that he has powerful enemies in Waterdeep. The risk of exposure keeps him hidden, and the characters can thwart him by furnishing his enemies with proof that he's alive (after a fashion) and operating in Waterdeep." (`sources/adventure-wdh.json:26738`)

### A12. Habits, objects and the sanctum (day-one, GM-level)

Adventure, the E12 quarters (the bed, the arm, the stairs):
> "Sitting on the edge of the bed is a handsome young male human in elegant robes. Long black hair partially conceals his angelic face as he attaches a metal appendage to the withered stump of his left arm." (`sources/adventure-wdh.json:30250`)
> "The handsome young figure is {@creature Manshoon|WDH} (see {@adventure appendix B|WDH|12}), who is much older than he looks." (`sources/adventure-wdh.json:30254`)
> "If a fight breaks out, {@creature Manshoon|WDH} grabs his {@item staff of power} (which he hides under the bed) and holds his ground." (`sources/adventure-wdh.json:30257`, the sentence continues: "For more information on how to play {@creature Manshoon|WDH}, see "Facing {@creature Manshoon|WDH}" at the beginning of this chapter.")
> "The mask on the table is nonmagical, but {@creature Manshoon|WDH} likes to put it on before meeting with his followers." (`sources/adventure-wdh.json:30264`)
> "The masks belong to {@creature Manshoon|WDH} and have been worn by him in the past." (`sources/adventure-wdh.json:29981`)
> "{@creature Manshoon|WDH} has amassed a sizable collection, including ten rare volumes he removed from Duhlark Kolat's collection." (`sources/adventure-wdh.json:30150`)
> "This spellbook weighs 20 pounds and is covered in beholder hide. It contains all the spells {@creature Manshoon|WDH} has prepared (see {@adventure appendix B|WDH|12}) plus the following spells:" (`sources/adventure-wdh.json:30325`; the list continues to "{@spell wish}" and the sentence "Stealing or destroying this spellbook disrupts {@creature Manshoon|WDH}'s operation")

Adventure, Kaevja (Manshoon's recruitment of a Red Wizard):
> "Kaevja was a Red Wizard of Thay until she saw an opportunity to study magic under {@creature Manshoon|WDH}. Before he accepted her, {@creature Manshoon|WDH} forced her to remove her distinctive Thayan head tattoos and to trade in her Red Wizard robes for black ones." (`sources/adventure-wdh.json:29993`)

Adventure, the Gondafrey cell (amusement):
> "{@creature Manshoon|WDH} is amused by the creature, so he keeps it alive but locked in the cell." (`sources/adventure-wdh.json:28504`)

Adventure, followers as expendable:
> "This version of {@creature Manshoon|WDH} isn't spoiling for a fight. He commends the characters for making it this far and shows no concern for the Zhents they defeated to reach him, since he considers all his followers expendable." (`sources/adventure-wdh.json:30255`)

Adventure, Duhlark's flameskull (Manshoon's handiwork):
> "{@creature Manshoon|WDH} found Duhlark Kolat's skeletal remains in the bed and transformed his skull into a flameskull." (`sources/adventure-wdh.json:28680`)

Adventure, the apprentices and the sanctum rings:
> "The three wizards here are {@creature Manshoon|WDH}'s apprentices—Ered Payno (LE male Damaran human), Havi Termock (CE female Chondathan human), and Savara Firethorn (NE female Tethyrian human). Each wears a teleporter ring (see "Teleporter Rings")." (`sources/adventure-wdh.json:28552`)
> "The Kolat brothers once took on apprentices, who slept here. {@creature Manshoon|WDH} now allows his own apprentices—Ered Payno, Havi Termock, and Savara Firethorn—to do the same." (`sources/adventure-wdh.json:28377`)

Alexandrian, the former apprentice (book p.95):
> "His former fourth apprentice tried to gain access to it and was disintegrated when Manshoon caught him." ([PDF-IMAGE] `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, book p.95 [PDF p.4 of 5], "Questioning the Zhentarim", apprentice wizards bullet)

Alexandrian, the astral vault and the Eye (book p.92 and p.94):
> "Although Manshoon lost the original Eye he had obtained, as Dragon Heist begins the Zhentarim seize possession of the Eye unwittingly carried by Renaer Neverember. This Eye is then immediately taken back to Kolat Towers and secured." ([PDF-IMAGE] `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, book p.92 [PDF p.1 of 5]) (conflict; see D)

### A13. Rank, lieutenants and people who answer to him (day-one)

Org page, leadership (line 52):
> "- **Leadership:** Manshoon is a centuries-old wizard, a clone of a clone of one of the Zhentarim's founders, who claims, as all surviving Manshoon clones do, to be the one true Manshoon. He keeps a simulacrum in Kolat Towers as his contingency against assassination, and it fights as his decoy while he escapes. His insurance against dying is the stasis clone spell, which is a separate tool. Nobody stands between him and his lieutenants, and the cell takes its orders from him alone." (`campaign/setting/organizations/09-manshoons-zhentarim.md:52`)

Org page, the hub and spokes (line 53) and Sidra (line 54):
> "- **The hub and spokes:** The Splinter is built as a hub with spokes. Kolat Towers in the Southern Ward is the command center, and the Interrogation House on Brindul Alley in the North Ward and Yellowspire in the Castle Ward are its field offices." (`campaign/setting/organizations/09-manshoons-zhentarim.md:53`; the sentence continues "Yellowspire holds a teleportation circle that leads to the Towers, and the Towers stand in the Southern Ward. Teleportation circles also link the Towers to the Interrogation House (**Southern Ward**).")
> "Sidra Romeir runs the ground floor like a barracks, Manafret Cherryport cooks for the household, and Manshoon's three apprentices, Ered Payno, Havi Termock and Savara Firethorn, sleep in the old apprentices' quarters and wear teleporter rings (**Sidra Romeir**; **Manafret Cherryport**; *Dragon Heist*, 5e)." (`campaign/setting/organizations/09-manshoons-zhentarim.md:54`)

Notable page (day-one), Relationships (line 26):
> "**Relationships.** Manshoon is the leader of the Zhentarim splinter cell, the employer of Urstul Floxin, Sidra Romeir, and Vevette Blackwater, a blackmailer of Masked Lords Jelenn Urmbrusk and Corylus Thann, and a clone-wizard whose response teams are deliberately the weakest in muscle because drawing attention is the one mistake he will not make twice." (`campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:26`)

Villains, Relationships table (lines 61, 63, 65, 66):
> "| Urstul Floxin | Field lieutenant | Most effective operative; trusted with the Stone recovery at Gralhund Villa; his failure there is the first crack |" (`campaign/setting/villains/manshoon.md:61`)
> "| Xanathar | Rival | Useful; the Guild's visibility keeps the Watch occupied `[research]`; when the beholder becomes a direct obstacle, Manshoon has a plan |" (`campaign/setting/villains/manshoon.md:63`)
> "| The Cassalanters | Missed opportunity | Manshoon is as suspicious of their wealth and spotless name as everyone else, and an arrangement with them could have given him leverage; he chose independence over shared control `[research]` |" (`campaign/setting/villains/manshoon.md:65`) (see D on Cassalanter secrecy)

Villains, relationship notes (line 74-75):
> "- Sidra Romeir is his most trusted lieutenant and holds the teleport rings when lieutenants leave the towers. At Lockdown she locks down Kolat Towers." (`campaign/setting/villains/manshoon.md:74`)
> "- His response teams are the weakest in raw muscle of any faction, because drawing attention is the one mistake he will not make twice. They carry orders to capture, not kill, and he underestimates threats that are not magical." (`campaign/setting/villains/manshoon.md:75`)

Sidra's page (Notable; day-one):
> "**Relationships.** Sidra is Manshoon's Kolat Towers lieutenant, the keeper of the teleporter ring system, and the only person in the cell whose loyalty Manshoon has never tested, because testing it would mean he does not already know the answer." (`campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:25`)

Urstul's page (Notable; day-one):
> "**Relationships.** Urstul is Manshoon's chief field operative, a temporary occupant of Gralhund Villa (where he treats Yalah as an underling), and the antagonist who drives **Fireball!** and **Gralhund Villa** before the party can identify his master." (`campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:25`)

Adventure, Urstul's master and the simulacrum (conflict; see D):
> "{@creature Urstul Floxin|wdh} works for {@creature Manshoon|WDH}, and he is the highest-ranking member of the Zhentarim squad stationed at House Gralhund." (`sources/adventure-wdh.json:32644`)
> "Urstul takes his orders from {@creature Manshoon|WDH}'s current simulacrum, which comes and goes from House Gralhund by way of a teleportation circle (connected to the circle in Kolat Towers)." (`sources/adventure-wdh.json:32644`)

Adventure, Vevette and Agorn (day-one background for the Connections list):
> "Vevette was a vicious pirate before she joined the Zhentarim and rose to become one of {@creature Manshoon|WDH}'s favored lieutenants." (`sources/adventure-wdh.json:8532`)
> "{@creature Agorn} made such a good impression on {@creature Manshoon|WDH} that he was elevated quickly through the ranks of the organization, but his life is full of disappointment otherwise." (`sources/adventure-wdh.json:7599`; exact text: "Agorn made such a good impression on {@creature Manshoon|WDH} that he was elevated quickly through the ranks of the organization, but his life is full of disappointment otherwise. He has not achieved the fame he craved nor earned the wealth he felt he was entitled to.")
> "Vevette and Agorn are two of {@creature Manshoon|WDH}'s most trusted followers. Vevette commands the wizard's forces against the Xanathar Guild, while Agorn commands those who oppose the Zhents that aren't loyal to {@creature Manshoon|WDH}." (`sources/adventure-wdh.json:30130`)

Adventure, Havia and Mookie (gender conflict; see D):
> "Two female lightfoot halflings—{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush}—believe that {@creature Manshoon|WDH} is the rightful leader of the Zhentarim. They serve him fearlessly, and will sacrifice themselves to ensure that his plans come to fruition." (`sources/adventure-wdh.json:30183`)

Adventure, Manafret and Sidra's card game (for the Connections list):
> "The card players are Sidra Romeir (LE female Calishite human {@creature veteran}) and two subordinates (LE male Tethyrian human {@creature thug||thugs})." (`sources/adventure-wdh.json:28155`)
> "The halfling, {@creature Manafret Cherryport|wdh}, is one of {@creature Manshoon|WDH}'s lieutenants. He loves to cook, and uses his mage hand cantrip to cut vegetables." (`sources/adventure-wdh.json:28191`)

Adventure, Yorn and the teleporter circle (Yorn's knowledge; optional):
> "He has never visited {@creature Manshoon|WDH}'s extraplanar sanctum, but he does know that the teleportation circle in {@area K22|40b} is the way to get there." (`sources/adventure-wdh.json:28348`)

Adventure, Amath (Yellowspire; with the spelling "Sercent" and the Mulan race):
> "The characters have learned that the {@item Stone of Golorr|WDH} is with Amath Sercent, a priest of Bane who is allied with {@creature Manshoon|WDH}. She and her acolytes reside in Yellowspire, a Castle Ward tower so named because its bricks have a pale yellow tinge to them." (`sources/adventure-wdh.json:9741`)

Campaign, Agorn and Amath (day-one partnership, settled in the campaign; see D):
> "Agorn is a Manshoon lieutenant and bard, the partner of Amath Sercent, whom he visits at Yellowspire in the evenings, a pass-amulet holder for Kolat Towers, and a man whose mother lives in Mistshore and knows nothing about any of this." (`campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`)
> "Amath is the Banite priestess occupying Yellowspire (Castle Ward), the keeper of a teleportation circle providing a back-route into Kolat Towers (bypassing the pass-amulet requirement), Agorn Fuoco's romantic partner, and a Manshoon-adjacent religious operative whose devotion to Bane predates and outlasts any particular Zhentarim arrangement." (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:25`)

Notable Manshoon's members: Havia and Mookie (Notable, day-one): not quoted (see D for Mookie).

Campaign, Vira (day-one plant):
> "Vira is a Manshoon plant embedded inside Blackstaff Tower, the operative responsible for installing the resonance disruptor in the Tower's defensive architecture, and the primary antagonist of **Smoke in the Tower**." (`campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md:25`)
(Note: "primary antagonist of Smoke in the Tower" is a quest reference; route.)

### A14. Time in post

> "He spent about two years building the Splinter, a cell that bears his name and works independently of the Zhentarim's surviving leadership." (`campaign/setting/villains/manshoon.md:33`; the same two years in `campaign/structure/arc-i-kolat-towers.md:15`)
> "- The clone then spent two years building the Splinter cell" — exact: "- The clone spent about two years building the Splinter cell, which is about 1490 DR counted back from Ches 1, 1492 DR." Not verbatim; use: "- The clone then spent two years building the Splinter cell, which is about 1490 DR counted back from Ches 1, 1492 DR. `[research]` ..." (`campaign/setting/history/08-the-players-arrive.md:32`)
> "- Manshoon's clone fled Undermountain, found the towers abandoned with the force field still running, and took the amulet-making instructions from Duhlark's study. He spent two years building the Splinter." (`campaign/setting/history/04-the-founding-of-chains.md:68`) (exact text: "- Manshoon's clone fled Undermountain, found the towers abandoned with the force field still running, and took the amulet-making instructions from Duhlark's study. He spent two years building the Splinter.")
> "- About 1490 DR (derived): Manshoon's clone begins building the Splinter cell." (`campaign/setting/history/08-the-players-arrive.md:80`)
> "- 1485 DR, about: the Kolat Towers simulacrum is made. This is derived from "seven years ago" in the Kolat Towers structure document and is stated by no other source." (`campaign/setting/history/04-the-founding-of-chains.md:138`)

### A15. Faith and the Bane link (Yellowspire, day-one; the Bane page is the authority)

> "**Where it is used:** Bane never appears in person. His faith in play is Amath Sercent and her four acolytes, who keep Yellowspire as a temple and a relay point for Manshoon's cell of the Zhentarim." (`campaign/setting/deities/bane.md:8`)
> "- **Yellowspire and the Zhentarim split:** Amath is allied with Manshoon's cell, the splinter that peeled off the Doom Raiders' network." (`campaign/setting/deities/bane.md:81`)
Note: the Org page says the cell has no creed (`organizations/09-manshoons-zhentarim.md:46`, quoted in A3).

### A16. Signature belongings (campaign and adventure)
- Staff of power: `arc-i-kolat-towers.md:13` and `adventure-wdh.json:30257` (quoted above).
- Spellbook: `adventure-wdh.json:30325` and `:30281`:
> "In the other far corner, {@creature Manshoon|WDH}'s spellbook rests atop a black marble lectern protected by an {@condition invisible} {@creature helmed horror}." (`sources/adventure-wdh.json:30281`)
- Teleporter rings: "a brass signet ring bearing a stylized M" (`sources/adventure-wdh.json:28822`): "To access {@creature Manshoon|WDH}'s extraplanar sanctum, one needs a {@item teleporter ring|WDH}: a brass signet ring bearing a stylized M, and which emanates an aura of conjuration magic when targeted by a {@spell detect magic} spell or similar magic. {@creature Manshoon|WDH} gives these rings to his most trusted servants." (`sources/adventure-wdh.json:28822`)
- Masks: `adventure-wdh.json:29981`, `:30264` (quoted).

---

## B. Alignment, species, pronouns, stat block (each with quote and line)

**Alignment**
- Notable summary: "- *Vaasan human wizard (clone), lawful evil, he/him*. Stat block: **Mage (with modifications)**." (`campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:5`)
- Southern Ward gazetteer: "**Manshoon (Lawful Evil, Vaasan Human, he/him)**" (`campaign/gazetteer/waterdeep/southern-ward.md:139`)
- Wiki infobox: "| alignment5e    = [[Lawful evil]]" (`W:59`); also "| alignment3e    = [[Lawful evil]]" (`W:48`) and "| alignment1e    = [[Lawful evil]]" (`W:42`)
- Published adventure: no alignment line for Manshoon found in the entries read. The adventure says: "Evil to the core, he made enemies all across Faerûn" (`sources/adventure-wdh.json:32216`).
- Villains page: no alignment line. Org page: no alignment line in the Summary.

**Species and ethnicity**
- Published adventure: "Sitting on the edge of the bed is a handsome young male human in elegant robes." (`sources/adventure-wdh.json:30250`)
- Notable summary: "Vaasan human" (`01-manshoon.md:5`); Southern Ward: "Vaasan Human" (`southern-ward.md:139`)
- Wiki: "| race           = [[Human]]" (`W:14`); "| ethnicity      = [[Vaasan]]<ref>{{Cite web/theedverse/2018-02-21 - Manshoon's appearance and heritage}}</ref>" (`W:15`)

**Pronouns**
- Notable summary: "he/him" (`01-manshoon.md:5`). Southern Ward: "he/him" (`southern-ward.md:139`). Wiki: "| sex            = Male" (`W:12`), "| gender         = Masculine" (`W:13`). Adventure, male pronoun: "He commends the characters for making it this far..." (`sources/adventure-wdh.json:30255`). Villains draft notes say the Notable page states no pronouns; this is stale (the Notable line 5 has he/him). The Villains page's "Pronouns" conflict note (`manshoon.md`, Draft Notes) is stale.

**Stat block**
- Notable summary: "Stat block: **Mage (with modifications)**." (`01-manshoon.md:5`). No source checked gives "Mage" for Manshoon.
- Wiki infobox: "| challenge5e    = 13" (`W:60`); "| class5e        = {{Class table|edition=5e|[[Wizard]]|18}}" (`W:61`); "| refs5e         = <ref name="WDH5e-p208-209">{{Cite book/Waterdeep: Dragon Heist|208-209}}</ref>" (`W:62`).
- Alexandrian stat reference: "Manshoon Simulacrum – DH p. 209" and "Manshoon – DH p. 209" (`[PDF-IMAGE] sources/12. Lair  Zhentarim – Kolat Towers.pdf`, book p.95 [PDF p.4 of 5]). No class or CR printed.
- Published adventure, simulacrum CR only: "It has a challenge rating of 8 (3,900 XP)." (`sources/adventure-wdh.json:32233`). The main Manshoon stat block is not in the JSON; it is referenced as the book's p.208-209 (`sources/adventure-wdh.json:32212`, `"page": 208`).
- Simulacrum stat changes: "The simulacrum has no special equipment. Consequently, it has AC 12 and lacks the Magic Resistance trait and the Staff of Power action option." (`sources/adventure-wdh.json:32231`); "It loses all spell slots of 6th level and higher." (`:32232`).

**Age**
- "who is much older than he looks" (`sources/adventure-wdh.json:30254`). Wiki born 1229 DR (`W:22`).

**Appearance** (for the Roleplaying and Overview only if the drafter wants it; GM text)
- "Long black hair partially conceals his angelic face" (`sources/adventure-wdh.json:30250`); "a handsome young male human in elegant robes" (`:30250`); "withered stump of his left arm" (`:30250`). Simulacrum: "The simulacrum resembles a robed wizard with long black hair, pale skin, and an articulated metal left hand and forearm. Its face is concealed behind a steel mask that bears a smiling visage." (`sources/adventure-wdh.json:30077`)

**Home**
- Wiki: "| home           = [[Citadel of the Raven]], [[Moonsea]]" (`W:10`). Campaign current home: "Kolat Towers" (`villains/manshoon.md:21`, "He runs the Splinter ... from the warded towers of Kolat Towers in the Southern Ward.").

**Faith and patron**
- Wiki infobox: "| patron deity   = [[Mystra]]" (`W:18`). Campaign: "absorb the Weave and supplant Mystra" (`villains/manshoon.md:21`, `01-manshoon.md:16`).

**Titles**
- Campaign: "founder" wording (see A1). Wiki infobox: "| titles         = " (blank) (`W:6`).

---

## C. Sentences that narrate quest-time or day-one conflicts

### C1. The current Notable page (`01-manshoon.md`)
I checked lines 5-30. No sentence narrates a quest event, an arrest, a mission, a reveal or an "after the party" beat. Items the drafter must still handle:
- Line 8 (Featured in) and line 9 (Villain profile): list quests and events; no narration.
- Line 16, "...and deepen his hold over Masked Lords Corylus Thann and Jelenn Urmbrusk into a full Council majority." Day-one, but "full Council majority" is not sourced (see D and F).
- Line 22 "using a teleportation circle for all movement" (see D).
- Line 30 Overview: "A name the party does not have yet." This is gated language ("the party does not have yet") but the gate is a quest-time outcome, so the drafter should check it against ruling 1 before keeping it. Source for the gate: "Manshoon Named" (see E).

### C2. The current voice profile (`.claude/skills/character-voices/voices/manshoons-zhentarim.md`)
Quest-time clauses (carry a day-one restatement per ruling 16):
> "None of them will say Manshoon's name before Phase 2, and that refusal is itself part of every voice here." (`manshoons-zhentarim.md:2`)
> "- **The Shadow (Acts I–II):** never heard. Only his lieutenants speak, and they won't name him." (`manshoons-zhentarim.md:17`)
> "- **The Architect (Acts II–III):** revealed, courteous, patient and terrifyingly reasonable." (`manshoons-zhentarim.md:18`)
> "- Cornered at **Kolat Towers**, the courtesy thins, but it never breaks." (`manshoons-zhentarim.md:19`)
> "**Two Zhentarims:** these characters never talk as if they were the Doom Raiders, and never refer to Davil's people as colleagues. To them, Davil's cell is "the old guard" at best." (`manshoons-zhentarim.md:4`) (day-one; kept)
Phase lines live in `campaign/setting/villains/manshoon.md:47-49` (the phase table) and `:51-53` (triggers), which are quest-time GM text; the voice clauses above restate them.

Other voice lines (day-one, no change needed; listed so the drafter can check):
> "- **Sound:** A cultured, cool, perfectly modulated voice, never raised, precise in every consonant. His artificial arm clicks faintly when he gestures." (`manshoons-zhentarim.md:11`)
> "- **Swearing:** *Never · Plain · n/a.* Profanity is for people who lack better words. His rare anger is precise and calm, and more frightening for it." (`manshoons-zhentarim.md:14`)
> "- **Word choice:** Scholarly and imperial: "inevitable", "an arrangement", "the Weave", "my city" (said as a correction). He calls the party by name once he's learned it, and the simulacra he has made "the others"." (`manshoons-zhentarim.md:13`)
> "- **Never:** He never loses his temper, never pleads, and never admits a clone is anything but an imposter." (`manshoons-zhentarim.md:22`)
> "- **Sample lines:** ... *Greeting:* "You've been very persistent. Sit. Let us be reasonable, since the alternative is so wasteful."" (`manshoons-zhentarim.md:24`); "*Business:* "You hold a key to a door I intend to open. I can make that profitable for you, or brief. The choice is genuinely yours."" (`:25`); "*Under pressure:* "Halaster took an arm. You will not get the rest."" (`:26`)
Note: the voice profile's "the simulacra he has made 'the others'" (`:13`) reveals a GM-only fact; the Roleplaying block is GM-only, so it stays, but it must not reach the Overview.

Voice Inspirations (Notable, line 18) and the Villains pop-culture line (`villains/manshoon.md:55`) conflict (see D).

### C3. The Villains page (for the Background moves)
Quest-time or quest-adjacent lines in the Background (lines 25-41):
- Line 35 ("His envoys brought it to Xanathar three months before the fireball"): pre-start (Nightal 1491 DR by derivation, `history/08-the-players-arrive.md:80`?? no; use `history/06-the-open-lords-fall.md:135` as cited in the Ott model). The derived date is recorded in `campaign/setting/history/02-the-long-shadow.md:135`: "- About Nightal 1491 DR (derived): the Neverwinter Eye passes from the Zhentarim to Xanathar when Xanathar kills Manshoon's envoys, three months before the fireball on Ches 22 (`arc-f-xanathars-lair.md` line 9; see **The Long Shadow**)." Pre-start.
- Line 36 ("...on the night before Ches 1 and pried it open at the Candle Lane warehouse. Xanathar's Guild raided the warehouse ... Bregan D'aerthe agents inside Xanathar's hideout lifted it that night."): this is the night before Ches 1 and the Finding Floon raid. It is pre-start in date but the raid is dramatised in **Finding Floon** (`campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:9`: "Four kenku occupy the building, searching the wreckage of the Xanathar's Guild raid that killed Manshoon's cell"). Decision for the orchestrator: keep as backstory before Ches 1, or route it. The Org page already writes it as a past event (`organizations/09-manshoons-zhentarim.md:33`, quoted in E).
- Line 41 ("The campaign stages his reveal across three quests...") is GM design text and routes to **Faction Outposts**, **Kolat Towers** and **Vault of Dragons** (E).
- Line 38 (the published goal) is a conflict; keep as a Draft Notes item.
- Line 39 and line 40 are day-one (enemies; simulacrum existence). Line 40 is GM-only.

Villains page non-Background quest-time lines (for the drafter's routing list, E):
- Line 9: "The party gets his name at the Interrogation House in **Faction Outposts**, which is where the **Manshoon Named** Event Outcome is marked." (`campaign/setting/villains/manshoon.md:9`)
- Line 10: "**Kolat Towers** records the result of the raid as one of three Event Outcomes (**Manshoon Destroyed**, **Manshoon Simulacrum Only** or **Manshoon Alive**), and **Vault of Dragons** reads it." (`:10`)
- Line 61: "his failure there is the first crack" (`:61`; Gralhund Villa).
- Line 64: "...which ends when Manshoon's strike team hits the *Eyecatcher* at **Sea Maidens Faire**, whatever the party does" (`:64`).
- Line 72: "Manshoon's parallel strike in **Sea Maidens Faire** always fires, and it sends his agents against Jarlaxle's ships in Jarlaxle's own harbor." (`:72`)
- Line 74: "At Lockdown she locks down Kolat Towers." (`:74`)
- Line 90 (Overview): "The Watch has arrested a few of them after street brawls." (`:90`) (arrests are quest-time, ruling 1; the same text is at `organizations/09-manshoons-zhentarim.md:113`.)

### C4. The organization page (`09-manshoons-zhentarim.md`)
- Line 33 (quest-time raid in the history): "- **The night before Ches 1, 1492 DR, Renaer Neverember:** Five Zhentarim thugs working for Urstul Floxin seized Renaer Neverember to learn what he knew about his father's hidden gold, and they took Floon Blagmaar in the same attack. House Gralhund paid for the operation (*Dragon Heist*, 5e; **House Gralhund**). Xanathar's Guild raided the Candle Lane warehouse where the thugs held both men and killed the cell's agents there (*Dragon Heist*, 5e)." (`campaign/setting/organizations/09-manshoons-zhentarim.md:33`) — lives in `campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:9`.
- Line 91: "- **The Open Lord's Watch (enemy):** The Watch has arrested a few of the tattooed crews in street brawls, and none of them will say who gives the orders (**The Open Lord's Watch**)." (`09-manshoons-zhentarim.md:91`) — arrests, quest-time.
- Line 113 (Overview): "Zhentarim crews with flying snake tattoos work Waterdeep's back streets, and they are hostile to Davil Starsong's Doom Raiders. The crews take prisoners, and the Watch has arrested a few of them in street brawls." (`:113`)
- Line 58 (Vevette and Agorn; present tense, GM): fine.
- Line 73 (Vevette turned down): "Vevette Blackwater turned down a Cassalanter approach for that reason (**Vevette Blackwater**)." (`:73`) day-one.
- Line 117 (GM Notes): "The Eyes: The cell holds no Eye of the Stone, because its envoys brought Eye #1 to Xanathar as a gift and Xanathar killed them and kept the Eye." (`:118`) day-one.

### C5. The Factions Guide (`10-manshoons-zhentarim.md`)
- Line 9 (capture): "Any Zhentarim team sent to attack the characters carries orders to take them as prisoners to the Interrogation House on Brindul Alley." (`guides/factions/10-manshoons-zhentarim.md:9`) — the team orders are game mechanics (not for the Notable page).
- Line 23 (Directive to Zorbog): "*Front Room.* Avareen and Zorbog's quarters. Avareen carries a pass-amulet to Kolat Towers. While the party explores, a flying snake arrives with *A Directive to Zorbog* signed by "Manshoon," ordering Zorbog to kidnap Fenerus Stormcastle of Quill Alley, a "known associate of these new meddlers in the Grand Game."" (`guides/factions/10-manshoons-zhentarim.md:23`) — **Faction Outposts** (the name reveal).
- Line 25 (Ott): "*Backroom.* A rack and other instruments of torture. An arcane circle on the floor. Strapped into the rack is **Ott Steeltoes**, a Xanathar's Guild agent captured while the Zhentarim were trying to locate the Eye." (`:25`) — **Faction Outposts**.

### C6. Other files, quest-time lines the Notable page must not copy
See E.

---

## D. Conflicts (both sides quoted; campaign ranks above the adventure, the adventure above the Alexandrian PDFs and the wiki)

**D1. Kolat Towers' ward.** Campaign: "Kolat Towers is a crumbling pair of towers in the Southern Ward" (`campaign/setting/villains/manshoon.md:31`). Adventure, the Trades Ward: "{@creature Manshoon|WDH} lurks in Kolat Towers, a pair of wizards' towers in the Trades Ward. This residence is described in chapter 8." (`sources/adventure-wdh.json:560`). Adventure, Southern Ward: "{@creature Manshoon|WDH} took control of Kolat Towers, a crumbling residence in the Southern Ward" (`:32218`). Campaign wins; the history settles it (`campaign/setting/history/04-the-founding-of-chains.md:153`).

**D2. The Interrogation House's ward.** Campaign: "Brindul Alley in the North Ward" (`campaign/setting/organizations/09-manshoons-zhentarim.md:57`, "A windowless house on Brindul Alley in the North Ward"); also `campaign/structure/arc-e-faction-outposts.md:201` ("*North Ward, Brindul Alley.*") and `campaign/gazetteer/waterdeep/north-ward.md:38`. Adventure: "The characters' search for the {@item Stone of Golorr|WDH} leads them to a snow-covered alley in the Trades Ward that contains a windowless Zhentarim safe house ({@area L1|140})" (`sources/adventure-wdh.json:7174`). Alexandrian [PDF-IMAGE] book p.45: "ZHENTARIM INTERROGATION HOUSE (Trade Ward, Brindul Alley)" (`sources/5. Faction Outposts.pdf`, book p.45 [PDF p.10 of 11]). Campaign wins (user settlement, Session 51, per `north-ward.md:272`: "Brindul Alley's ward is the North Ward, as the Zhentarim Factions Guide and `arc-i-kolat-towers.md:15` say.").

**D3. Amath and Agorn.** Alexandrian [PDF-IMAGE] book p.46: "It is occupied by Amath Seccent (LE female Mulan **priest**), a Banite priestess allied with Manshoon, and her four **acolytes**." and "Seccent is friends with Agorn Fuoco (see Part 3C: Response Teams), and he may also be found visiting here." (`sources/5. Faction Outposts.pdf`, book p.46 [PDF p.11 of 11]). Alexandrian revelation list, book p.124: "Threatening Agorn Fuoco; he'll sell out his friend to save his own life (Response Team: Agorn Fuoco)" (`sources/17. Outpost and Lair Revelation Lists.pdf`, book p.124 [PDF p.4]). Campaign: "Agorn Fuoco is her romantic partner and visits her there in the evenings" (`campaign/setting/organizations/09-manshoons-zhentarim.md:103`) and "the partner of Amath Sercent" (`05-agorn-fuoco.md:25`, quoted in A13). Campaign wins; the Org draft notes say the old "friends" wording was replaced.

**D4. The clone's arrival and the simulacrum's age.** Campaign: "He spent two years building the Splinter cell" (`arc-i-kolat-towers.md:15`) and "It was created seven years ago" (`arc-i-kolat-towers.md:17`). The seven-year simulacrum predates the clone's arrival, which `arc-i` puts in the Undermountain account (`arc-i-kolat-towers.md:13`); the history derives 1485 DR (`history/04-the-founding-of-chains.md:138`). Adventure: "this clone of the ancient archwizard infiltrated Waterdeep years ago" (`sources/adventure-wdh.json:32215`). Not settled in the sources; the Villains page says the same (`villains/manshoon.md:33`). Note: the simulacrum's age sits in GM text only.

**D5. Duhlark's death.** Campaign: "Duhlark survived him by nine years before being found dead in his study, apparently of old age, with the force field still running." (`arc-i-kolat-towers.md:9`); "Duhlark was found dead in his study nine years later." (`campaign/gazetteer/waterdeep/southern-ward.md:52`). Adventure: "{@creature Manshoon|WDH} found Duhlark Kolat's skeletal remains in the bed and transformed his skull into a flameskull." (`sources/adventure-wdh.json:28680`) and "Duhlark became a recluse who died in his own fortress." (`:26865`). Campaign wins; the bedroom detail is an adventure-only fact (the flameskull room is K19 "Duhlark's Bedroom": `arc-i-kolat-towers.md:140`).

**D6. Alcedor's fate.** Adventure: "Alcedor left the towers, never to be heard from again" (`sources/adventure-wdh.json:26865`). Campaign: "He died in the towers in 1385 DR under circumstances that remain unclear." (`arc-i-kolat-towers.md:9`); also `southern-ward.md:52`. Campaign wins; history notes the same (`campaign/setting/history/04-the-founding-of-chains.md:161`).

**D7. The Doom Raiders' arrival.** Adventure: "They gave up adventuring to join the Black Network and came to Waterdeep three years ago" (`sources/adventure-wdh.json:31916`). Appendix B, the Doom Raiders' own speech: "Me and my colleagues arrived in Waterdeep about four years ago." (`sources/Appendix_B_-_Player_Factions.md:636`). Campaign: "The Doom Raiders, five retired adventurers, were sent to Waterdeep in 1489 DR" (`history/04-the-founding-of-chains.md:24`; the history's exact line is "- The Doom Raiders, five retired adventurers, ..." — quote at `campaign/setting/history/04-the-founding-of-chains.md:24`: "> - The Doom Raiders, five retired adventurers, were sent to Waterdeep in 1489 DR to found the Black Network's foothold."). Campaign wins (1489 DR; three years before Ches 1, 1492 DR).

**D8. The Stone's route to Xanathar.** Campaign: "...the Zhentarim came to him with one of the Eyes..." (Alexandrian p.15) and "About Nightal 1491 DR (derived), Manshoon's Zhentarim sent two lieutenants to Skullport with Eye #1" (`01-xanathar.md:45`). Adventure: "As Zhents loyal to {@creature Manshoon|WDH} try to forge an alliance with Xanathar, the Stone of Golorr is stolen." (`sources/adventure-wdh.json:838`). Campaign wins (`history/02-the-long-shadow.md:158`: "The published entry has Xanathar's spies stealing the Stone..." — the Long Shadow notes record the same conflict).

**D9. Who holds an Eye.** Campaign: "Kolat Towers holds no Eye." (`arc-i-kolat-towers.md:57`); "**Manshoon:** He holds no Eye." (`lore/stone-of-golorr-and-the-eyes.md:44`); "Manshoon holds no Eye." (`running-the-villains.md:30`). Alexandrian [PDF-IMAGE] book p.92: "This Eye is then immediately taken back to Kolat Towers and secured." (`12. Lair Zhentarim – Kolat Towers.pdf`, book p.92 [PDF p.1]); book p.94 (in the astral vault): "Inside the Astral Vault: The vault contains the Eye, 5 pass-amulets, a dozen teleporter signet rings, and Manshoon's Report on the Grand Game (see Part 6D)." (`[PDF p.3]`); book p.96: "He already has one. He once had another that was stolen by Xanathar." ([PDF p.5]). Alexandrian [PDF-IMAGE] `8. The Eyes of the Stone.pdf`, book p.62 [PDF p.1]: "As described in Part 1, the Eyes are currently held by the Cassalanters, Manshoon, and Xanathar." Campaign wins (brief ruling 12). Route: the Alexandrian Eye is the one the Zhents take during Dragon Heist (quest-time); the campaign keeps it out of Manshoon's hands on Ches 1.

**D10. The vault plan.** Campaign: "Contingency: destroy the vault rather than cede it." (`villains/manshoon.md:80`). Campaign (lore): "his plan is to let someone else open the vault and then take it from them." (`lore/stone-of-golorr-and-the-eyes.md:44`). Both are campaign; they differ. The orchestrator decides.

**D11. The goal.** Campaign: "Manshoon wants ... to acquire the Stone ... absorb the Weave and supplant Mystra" (`01-manshoon.md:16`; `villains/manshoon.md:80`). Adventure: "...declare himself the Wizard-King of Waterdeep." (`sources/adventure-wdh.json:32219`). Campaign wins (org draft notes; history/04 line 73).

**D12. Corylus Thann's leverage.** Campaign: "he supplies Guild intelligence in exchange for the ledger's continued privacy" (`arc-i-kolat-towers.md:19`); Campaign (Villains and Notable): "Corylus Thann is held over a scandal" (`villains/manshoon.md:37`). Adventure: "Corylus Thann, a racist Waterdavian noble, is paying the Zhentarim not to reveal that he hired Zhent thugs to assault non-humans." (`sources/adventure-wdh.json:30294`). The Org page follows the adventure ("the hush money that Corylus Thann pays", `organizations/09-manshoons-zhentarim.md:67` [the Org's Funding bullet is at line 66: "from the hush money that Corylus Thann pays (*Dragon Heist*, 5e)."]). The campaign's arc-i line disagrees with both. Campaign quest-doc (arc-i) ranks above the adventure; the orchestrator must choose.

**D13. Jelenn's money.** Adventure: "receives regular payments from the Zhentarim to offset monies he loses in bad investments" (`sources/adventure-wdh.json:30295`) against "borrow money from the Zhentarim" (`:30374`). Campaign: "accumulated significant debt to a Splinter front organization" (`arc-i-kolat-towers.md:19`). The Open Lord file follows the loan (`open-lord-and-masked-lords.md:64`). Campaign wins.

**D14. The votes.** Campaign: "her votes in the Council of Guildmasters follow Manshoon's preferences" (`arc-i-kolat-towers.md:19`); "their votes follow his preferences" (`villains/manshoon.md:37`); Notable motivation: "into a full Council majority" (`01-manshoon.md:16`). "Council majority" appears nowhere else in campaign (grep). "Council of Guildmasters" appears only in arc-i. Flag.

**D15. Inspirations.** Notable: "When playing Manshoon, channel Magneto (*X-Men*), Emperor Palpatine (*Star Wars*), and Moriarty (*Sherlock Holmes*)." (`01-manshoon.md:18`). Villains: "Tywin Lannister (the chess player who is also the most dangerous piece on the board); Anton Chigurh (...); Hannibal Lecter (...)" (`villains/manshoon.md:55`). Both are unsourced; neither is a source fact.

**D16. Teleport habit.** Notable: "he is never seen entering or leaving Kolat Towers, using a teleportation circle for all movement." (`01-manshoon.md:22`). Adventure: "uses a teleportation circle when he must do so" (`sources/adventure-wdh.json:32218`). Villains: "he uses a teleportation circle when he must" (`villains/manshoon.md:31`). The Notable line is the outlier.

**D17. Stat block.** Notable: "Stat block: **Mage (with modifications)**." (`01-manshoon.md:5`). Wiki: "Wizard", CR 13 (`W:60-61`). Alexandrian: "Manshoon – DH p. 209" with no class (book p.95). Campaign has no stat source. Flag.

**D18. Cassalanter secrecy (brief ruling 7).** Villains row: "an arrangement with them could have given him leverage; he chose independence over shared control `[research]`" (`villains/manshoon.md:65`). Ruling 7: "Nobody outside the household and the cult knows about the pact. Other pages use suspicion." The row says "leverage" and "could have given him leverage" implies he knows what they would be leverage on. The Villains draft note (line 127) says the row was softened to suspicion, but the sentence still implies leverage. Flag; the Notable page should use suspicion only. Also "Manshoon shares everyone's suspicion of their wealth" is the softened version in the Villains draft note (`villains/manshoon.md:127`, quoted as the Draft Notes). The org page line 89 (`09-manshoons-zhentarim.md:89`) reads: "Manshoon shares the city's suspicion of a family that is too rich and too pleasant, and an arrangement with them could have given him leverage `[research]` (**Manshoon**)." Both carry the "leverage" phrase.

**D19. Vevette's alignment.** Notable: "*Tethyrian human swashbuckler, lawful evil, she/her*." (`03-vevette-blackwater.md:5`). Adventure: "Vevette Blackwater (CE female Tethyrian human {@creature swashbuckler|VGM}; see {@adventure appendix B|WDH|12})" (`sources/adventure-wdh.json:30120`). Alexandrian [PDF-IMAGE] book p.95: "Vevette Blackwater (CE female Tethyrian human) – swashbuckler, DH p. 216" (`12. Lair Zhentarim – Kolat Towers.pdf`, book p.95). The Org page says "lawful evil" (`09-manshoons-zhentarim.md:98`). Two sources say CE; the campaign says LE. Campaign wins by rank; the drafter should note the difference.

**D20. Mookie's gender.** Adventure: "Two female lightfoot halflings—... Havia Quickknife and ... Mookie Plush" (`sources/adventure-wdh.json:30183`). Notable: "*Lightfoot halfling adept, lawful evil, he/him*." (`13-mookie-plush.md:5`). Campaign wins by rank; flag for the Mookie page.

**D21. Agorn's rank-rise.** Adventure: "Agorn made such a good impression ... was elevated quickly through the ranks" (`:7599`). Not a conflict; but Org says "Agorn Fuoco would trade whatever he knows to save himself" (`09-manshoons-zhentarim.md:43`) — no conflict.

**D22. The Org's "Featured in" list is short.** Org: "- **Featured in:** **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Kolat Towers**" (`09-manshoons-zhentarim.md:11`). Villains and Notable list ten quests; the Org list omits Finding Floon, Trollskull Alley, Xanathar's Lair, Cassalanter Villa, Sea Maidens Faire and Vault of Dragons (Villains line 9). Not a Manshoon-page conflict; a Factions summary.

**D23. The structural-rules line.** The Org draft notes say `gm-guide/structural-rules.md` line 9 "says the cell conducts assassinations and maintains mind-controlled servants" (`09-manshoons-zhentarim.md:182`). The text of line 9 is: "**Manshoon's Zhentarim** are the villain faction. They operate from Kolat Towers, prefer to capture rather than kill, and maintain mind-controlled servants." (`campaign/guides/gm-guide/structural-rules.md:9`). The word "assassinations" is not on that line. The draft note is wrong on this point. The mind-controlled servants clause (wiki-free) is the only source for servants (see F).

**D24. Pre-Ches-1 Gralhund alliance date.** Adventure: "Less than a year ago, the Gralhunds were approached by agents of the Zhentarim loyal to {@creature Manshoon|WDH}" (`sources/adventure-wdh.json:32445`). Campaign: "- **Less than a year before Ches 1, 1492 DR, House Gralhund:** Zhentarim agents loyal to Manshoon approached House Gralhund..." (`history/04-the-founding-of-chains.md:31`? — the exact line is in the history file; I have the org draft note: "The Gralhund alliance's date... The History entry says less than a year before Ches 1." The exact campaign line is at `campaign/setting/organizations/09-manshoons-zhentarim.md:31` (Org History bullet: "- **Less than a year before Ches 1, 1492 DR, House Gralhund:** Zhentarim agents loyal to Manshoon approached House Gralhund, and the two formed an alliance."). Consistent; no conflict.

**D25. Halaster's reason.** Adventure: "amputated his left arm at the elbow for reasons unknown" (`sources/adventure-wdh.json:32217`). Campaign: "Halaster tolerated him for a time out of professional curiosity before taking the arm" (`villains/manshoon.md:30`), and arc-i line 13 ("Halaster Blackcloak, who tolerated the clone for a time out of professional curiosity"). Not a conflict but a campaign addition; the Background should say "for reasons unknown (published)" if it quotes the adventure.

**D26. Post-1370 clone fates (wiki vs campaign).** Wiki: "Shadovar moved against Zhentil Keep ... killing both Fzoul and the final clone of Manshoon" (`sources/research/pass5-bundles/zhentarim/wiki.txt:234`); Wiki: "The one in Undermountain appeared to have died during the events of the Spellplague itself." (`W:106`). Campaign and adventure: the Undermountain clone is the one in Waterdeep (`adventure-wdh.json:32217`). The campaign's history notes this as an overruled wiki line (`history/04-the-founding-of-chains.md:160` per the Org draft notes). Also Orbakh: "one became the vampire Orbakh in Westgate" (`villains/manshoon.md:28`) vs Org and history omit Orbakh. The Background drafter must decide whether to keep Orbakh; the Villains page keeps it.

**D27. The Undermountain arm level.** The Villains page says "(5e *Waterdeep: Dungeon of the Mad Mage*, area 1a)" (`villains/manshoon.md:29`) without a level; Undermountain's page says Level 9 (`geography/undermountain-and-skullport.md:70`). WDMM places 1a in Level 9 (`adventure-wdmm.json:24359`, `:26119`).

**D28. Kolat Towers' Lady Gondafrey** (day-one prisoner). Campaign: "Lady Gondafrey, a City Watch captain taken in 1379 DR, is a prisoner inside." (`southern-ward.md:59`). Adventure: "a gargoyle that has been imbued with the personality of a human knight of Tyr (god of justice) named {@creature Lady Gondafrey|wdh}" (`sources/adventure-wdh.json:28504`). Conflict in her form (gargoyle vs. human prisoner). Route to **Kolat Towers**; not in the Manshoon page except as a line.

**D29. Notable line 16 "Council majority"**: see D14.

---

## E. Stale lines in other files (not edited) and routed quest references

### E1. Stale or gated lines in setting, guide and quest files (the Notable page must not copy them)
- `campaign/guides/gm-guide/structural-rules.md:9`: quoted in D23.
- `campaign/gazetteer/waterdeep/castle-ward.md:131`: "- Vajra commands Force Grey. Her staff holds Khelben Arunsun's soul, and she says "the Splinter" until **Manshoon Named** is marked for the party member she is speaking to." (gate; ruling 1).
- `campaign/gazetteer/waterdeep/southern-ward.md:48`: "- Phaulkonmere stands one block south of Kolat Towers (Dragon Heist). Until **Manshoon Named** is marked for a member, Enclave speakers say "the Splinter" and never point toward the towers." (gate)
- `campaign/gazetteer/waterdeep/southern-ward.md:141`: "- Hook: the party has no name for him until **Manshoon Named** is marked for a member." (gate, in the Manshoon entry)
- `campaign/gazetteer/waterdeep/southern-ward.md:139`-`:145`: the entry for Manshoon; line 145: "- Manshoon lives in Kolat Towers and lets his simulacrum take the opening volley in a fight. He prefers to capture rather than kill. His location in the towers depends on the escalation tier, and **Kolat Towers** sets it." (day-one plus a quest reference).
- `campaign/setting/history/04-the-founding-of-chains.md:84`: "- Factions that speak to players say "the Splinter" or "the other cell" until **Manshoon Named** is marked for the listener." (gate, history)
- `campaign/setting/history/04-the-founding-of-chains.md:92`: "> - Waterdeep holds two Zhentarim organizations, and the Doom Raiders are only one of them. Nobody speaks Manshoon's name to a player until **Manshoon Named** is marked for that listener." (gate)
- `campaign/setting/history/04-the-founding-of-chains.md:138`: "1485 DR, about: the Kolat Towers simulacrum is made" (derived; GM-level, see D4)
- `campaign/setting/deities/bane.md:73`: "Until the party marks **Manshoon Named**, even the Doom Raiders say "Floxin's cell" or "the other cell" and call Kolat Towers "the towers in the Southern Ward"." (gate)
- `campaign/guides/factions/03-lords-alliance.md:13`, `04-emerald-enclave.md:13`, `05-order-of-the-gauntlet.md:13`, `06-force-grey.md:11`: each says "the Splinter" or "the other cell" until **Manshoon Named** is marked (gate in guide text).
- `campaign/setting/organizations/09-manshoons-zhentarim.md:113`: quest-adjacent arrests in the Overview (see C4).
- `campaign/gazetteer/waterdeep/north-ward.md:40`: "- Samara, a prisoner in **Xanathar's Lair**, says Manshoon's organization is based in a tower in the North Ward. That is a misdirection from overheard talk." (quest text, routed to Xanathar's Lair).
- `campaign/setting/history/08-the-players-arrive.md:65`: "- Urstul Floxin's cell led the kidnapping and fled to Kolat Towers before the quest begins. The City Watch has Splinter thugs under arrest at the Dock Ward scene." (arrests; a Finding Floon-linked claim).
- `campaign/structure/arc-i-kolat-towers.md:17`: "It was created seven years ago" (see D4).
- `sources/SOURCE_GUIDE.md:135`: "- **Manshoon:** Archmage running a Zhentarim splinter cell from Kolat Towers. Uses simulacrums for deniability. Agenda: political control of Waterdeep, eliminate the Doom Raiders who he sees as weak." (Stale: the Villains page says "absorb" in `:81` and "dismantle" in the Org `:45`; the Factions Guide does not say "eliminate".)
- `campaign/setting/organizations/09-manshoons-zhentarim.md:182`: the Draft Note that says structural-rules line 9 mentions assassinations (wrong; see D23).
- `campaign/setting/villains/manshoon.md:127` and `:137`: the Villains page's own Draft Notes contain stale notes (for example "the Notable page states no pronouns" is stale because Notable line 5 has he/him). Those Draft Notes are not for the Notable page.
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:22`: "for all movement" (see D16).

### E2. Routed quest references (quest-time; not day-one)
- **Finding Floon.** The Renaer and Floon seizure, the locket Eye and the warehouse raid: `campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:9` ("Four kenku occupy the building, searching the wreckage of the Xanathar's Guild raid that killed Manshoon's cell"). Alexandrian, book p.16 [PDF p.4]: "Zhentarim agents snatch Renaer Neverember and his friend Floon Blagmaar." — exact bullet: "Zhentarim agents snatch Renaer Neverember and his friend Floon Blagmaar." ([PDF-IMAGE] `sources/1. The Villains.pdf` book p.16). Also `01-manshoon.md`'s Floon-related line: none.
- **Fireball!.** The Dalakhar capture attempt: `campaign/structure/...` none; the Act III document: "Within hours, Floxin killed his guards and escaped — without the Stone, which Gralhund refused to yield." (`sources/Act_III_Arc_D.md:39`). The fireball event itself: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:184` ("**Path C — Speak with Dead, the Zhentarim.** ... they were tracking Dalakhar for Floxin because whatever he carried would make them "as rich as kings."").
- **Gralhund Villa.** Floxin's strike team on Ches 24: `sources/Act_III_Arc_E.md:13` ("<li><strong>Urstul Floxin's Strike Team:</strong> Eight of Manshoon's Zhentarim and Floxin himself, intent on recovering the Stone. Arrive on the night of Ches 24th.</li>"). `campaign/quests/act-ii/gralhund-villa/ev-04-the-zhentarim-raid.md:98` ("**Floxin Alive** — mark when Floxin survives the raid; read by **Kolat Towers**, where he becomes available as a Manshoon response team leader."). `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:40` ("| Manshoon's name | Not revealed; Floxin never gave it | Preserved for a later arc |"). `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:39` ("- **Manshoon's Zhentarim:** By the night of Ches 24, when Floxin's strike team hits **Gralhund Villa**, Manshoon's cell knows the Gralhunds hold the Stone.").
- **Faction Outposts.** The name reveal and the Interrogation House: `campaign/structure/arc-e-faction-outposts.md:207` ("*The Directive to Zorbog.* A flying snake arrives during or shortly after the party enters, bearing a sealed letter addressed to Zorbog. The letter is a *Directive to Zorbog* signed **Manshoon** — the first document in the campaign bearing his name as a signature."), `:211` ("*Intel Yield.* Manshoon's name (first use in the campaign)."), `:213` (Escalation Alert). Yellowspire `:217-231` (mini-heist; `:231` "**Escalation: Manshoon moves to Suspicious (Tier 2) if the Interrogation House has not been hit; moves to Lockdown (Tier 4) if it has.**"). Reveal sequence `:479` ("***Name, Identity, Motivation.*** Manshoon's revelation has been staged across three quests: name at the Interrogation House, identity at **Kolat Towers**, motivation at **Vault of Dragons**."). Yellowspire circle `:452`.
- **Kolat Towers.** `campaign/structure/arc-i-kolat-towers.md:15` (quoted in A6), `:17` (E7; in A6), `:13` (in A5), `:57` ("Kolat Towers holds no Eye."), `:99-104` (escalation table; the Manshoon & Simulacrum column: "Manshoon studying in E13; simulacrum dormant in E7" at Unaware, `:101`); Identity reveal `:213-221`; outcomes `:255-261`: "*Manshoon Event Outcomes.*" (`:255`), "Record one of three Manshoon Event Outcomes. Each is read directly in **Vault of Dragons**." (`:257`); the three outcomes, quoted:
> "- **Manshoon Destroyed.** Both Manshoon (the clone of a clone) and the simulacrum were eliminated during the raid. The Splinter cell collapses within a tenday — Vevette (if alive) attempts to hold the surviving operatives together but lacks Manshoon's authority and his clone-network insurance. No Manshoon at the Vault. The party arrives at **Vault of Dragons** facing Aurinax without a third-party obstacle." (`arc-i-kolat-towers.md:259`)
> "- **Manshoon Simulacrum Only.** Manshoon was destroyed but the simulacrum survived and escaped (or was not found). The simulacrum has no 6th-level or higher spell slots and no staff of power. It arrives at the Vault with reduced capabilities and diminished tactical creativity — it can execute plans Manshoon taught it but cannot adapt to novel situations effectively." (`arc-i-kolat-towers.md:260`)
> "- **Manshoon Alive.** Manshoon survived (escaped, negotiated, or was never reached). He arrives at the Vault at full strength with surviving lieutenants and the staff of power. The hardest **Vault of Dragons** configuration. He will have had time to prepare." (`arc-i-kolat-towers.md:261`)
- **Vault of Dragons.** `campaign/structure/arc-j-vault-of-dragons.md:34` (table row "| Manshoon | **Kolat Towers** Scene 6 (if run) | **Manshoon Destroyed** / **Manshoon Simulacrum Only** / **Manshoon Alive**. If **Kolat Towers** was never run, treat as **Manshoon Alive**, undiminished, and unidentified — the party has not yet assembled the Identity Reveal. |"); `:208-210` (the three outcomes as read in the Vault). `:210` "**Manshoon Alive** (or **Kolat Towers** not run). Full strength: staff of power in hand, surviving lieutenants at his side, ..."
- **Sea Maidens Faire.** `campaign/structure/arc-h-sea-maidens-faire.md:202` ("*The Manshoon Parallel Strike.* Manshoon knows Eye #3 is aboard the Scarlet Marpenoth. His intelligence sources — scrying via simulacrum, double agents in multiple factions, Zhentarim informants in the Dock Ward — have confirmed the target. He dispatches a strike team regardless of what path the party has chosen."), `:278` ("**Manshoon's Zhentarim.** If the Zhentarim strike team was defeated, Manshoon knows — the pass-amulets went dark.").
- **Doom Raiders gates (quest gate, not day-one).** `campaign/quests/faction-events/doom-raiders/00-first-meeting/design-notes.md:11`: "...the party learns it late, at the Faction Outposts Interrogation House, where **Manshoon Named** is set." ; `m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:27` (the gating text for Doom Raiders' name use).

### E3. Routed Notable-only facts
- The Splinter's blackmail of Corylus and Jelenn is also in the Org Summary. No routing needed.
- Samara's misdirection: `campaign/gazetteer/waterdeep/north-ward.md:40` (quoted above). Its quest home per the Org draft notes is `campaign/structure/arc-f-xanathars-lair.md` (not opened by me).
- Manshoon's offer to Laeral's Watch and the Masked Lords: adventure `sources/adventure-wdh.json:30256` (below).

Adventure, the Xanathar offer (day-one? The offer is a quest scene in Kolat Towers' E12; route):
> "The characters' best chance of survival is to convince {@creature Manshoon|WDH} that they can be cowed or bribed into working for him. Weary of his conflict with the Xanathar Guild, {@creature Manshoon|WDH} suggests that the characters prove their usefulness to him by hunting down and killing {@creature Xanathar|WDH} in its lair (see chapter 5)." (`sources/adventure-wdh.json:30256`) — route to Kolat Towers (the adventure's offer). The campaign's Villains page keeps it at `villains/manshoon.md:76`.

---

## F. Gaps a Background would need (with the sourced facts to stay consistent with)

Ruling 15 and 17: where sources are silent, invent with `[design]`; `[research]` marks a claim a source might settle. Constraints: nothing invented may contradict a campaign, adventure or Alexandrian fact; no secret, Event Outcome, quest result or Grand Game balance change; no new named Notable Figure unless a source names them (the wiki names Asmuth, Chess, Calkontor, Harlshoon, Theilon Greencloak and Ulsan Baneservant; Fzoul Chembryl is named in the campaign).

1. **Parents and birthplace.** Wiki: "Manshoon was born in Zhentil Keep in the 1229 ... to Harlshoon, the first lord of Zhentil Keep." (`W:78`). Campaign: born 1229 DR in Zhentil Keep (`villains/manshoon.md:25`). Gap: a mother; none. `[design]` allowed (nameless relative or place is fine).
2. **Childhood and the brother.** Wiki (`W:78`, `W:80`) has the brother Asmuth, blinded in the barrow and later killed by Manshoon. Campaign: none. If used, it is wiki-sourced and must be tagged as the wiki's account.
3. **Formative events before the Zhentarim.** Wiki: the sword from the barrow (`W:80`), the wand traded for a hand (`W:80`), the defection of Chess and the killing of the usurper (`W:82`). Campaign: none.
4. **The clone's life in Undermountain.** Campaign: "a body activated in Undermountain when the Manshoon before it died" and "Halaster tolerated him for a time out of professional curiosity before taking the arm" (`arc-i-kolat-towers.md:13`). Adventure: "The one presently in Waterdeep escaped death by hiding out in Undermountain, where he eventually ran afoul of Halaster Blackcloak." (`sources/adventure-wdh.json:32217`). Gap: what the clone did in Undermountain, and how long; no source. `[design]` only if it does not reveal a secret.
5. **The arm.** Campaign: lost at the elbow; magic would not regrow it (`villains/manshoon.md:29`); "with a blade that prevented magical regrowth" (`arc-i-kolat-towers.md:13`). Wiki: "the original was kept and reanimated by Halaster" (`W:123`). The Undermountain guardian is the arm (`adventure-wdh.json` and `adventure-wdmm.json:26133`).
6. **Who he cares about.** Sourced: no living person. Sidra is the only lieutenant "whose loyalty Manshoon has never tested" (`04-sidra-romeir.md:25`). Mookie and Havia "serve him fearlessly" (`adventure-wdh.json:30183`). Gap: a personal tie. `[design]` required; keep it nameless or use only an already-named person.
7. **Personal goals.** Campaign goals are the Weave, the blackmail and the Council (`villains/manshoon.md:80`, `01-manshoon.md:16`). Adventure: the Wizard-King plan and Halaster (`adventure-wdh.json:32219`). No personal goal outside the job is sourced. `[design]` required (ruling 17). Constraints: the Stone and the Weave stay the faction goal; the personal goal must sit beside "Motivations" (verbatim) and "Emotions" (verbatim).
8. **Fear.** Adventure: "Fearing that he might be destroyed by his foes, {@creature Manshoon|WDH} magically crafted several clones" (`sources/adventure-wdh.json:32216`). Campaign: "the stasis clone spell ... his insurance for dying for good" (`villains/manshoon.md:82`). A personal fear could sit on this; `[design]` for any new fear.
9. **Losses.** Wiki: the father poisoned by Calkontor (`W:78`); the brother Asmuth killed by Manshoon (`W:80`). Campaign: the lost arm (`villains/manshoon.md:29`); the disintegrated former apprentice (Alexandrian book p.95). Gap: a loss he still feels; `[design]`.
10. **Faith.** Wiki: "Manshoon and his magelings pledged fealty to Bane" (`W:85`); patron deity Mystra (`W:18`). Campaign: the cell has no creed (`organizations/09-manshoons-zhentarim.md:46`); he wants to "supplant Mystra" (`villains/manshoon.md:21`). Gap: his own faith; keep `[research]`.
11. **Places.** Campaign: Kolat Towers (`villains/manshoon.md:31`); the sanctum (`organizations/09-manshoons-zhentarim.md:55`); Yellowspire (a circle). Gap: a place he loves. `[design]`.
12. **Signature belongings.** Campaign/adventure: staff of power (`adventure-wdh.json:30257`), spellbook (`:30325`), masks (`:29981`, `:30264`), sunglobe (not Manshoon's own; the Kolat PDF calls it "Manshoon's sunglobe" in the Vault page `arc-j-vault-of-dragons.md:118`). All sourced.
13. **Age and how he looks.** `adventure-wdh.json:30250`, `:30254`; wiki's birth 1229 DR (`W:22`). The campaign never gives an age beyond "much older than he looks".
14. **Stat block class.** See D17. `[research]` for the class.
15. **Council majority.** D14. Only the Notable page says it.
16. **Urstul's species.** Notable and Org say "Illuskan human". The adventure entry at `sources/adventure-wdh.json:32640-32644` does not state it in the lines read. Not verified; flag for Urstul's page.

Overview constraint (brief): the clone, the simulacrum, the Weave and the Eyes are GM-only. Overview sources to copy the tone from: `campaign/setting/villains/manshoon.md:90` ("Zhentarim crews with flying snake tattoos work the back streets of Waterdeep. The Watch has arrested a few of them after street brawls. Their teams take prisoners, and the crews will not say who gives the orders.") — the arrest is quest-time; the rest is day-one. And `organizations/09-manshoons-zhentarim.md:113` (quoted in C4).

---

## G. Inner-life facts from sources (fears, habits, loves, grudges, losses, a place or person they care about)

- **Fear of destruction (adventure):** "Fearing that he might be destroyed by his foes, {@creature Manshoon|WDH} magically crafted several clones-but a mishap caused all of them to be awakened at once" (`sources/adventure-wdh.json:32216`).
- **Fear of exposure (adventure):** "The risk of exposure keeps him hidden, and the characters can thwart him by furnishing his enemies with proof that he's alive (after a fashion) and operating in Waterdeep." (`sources/adventure-wdh.json:26738`)
- **Pride about the arm (Notable and voice):** "frustrated pride about his artificial arm" (`01-manshoon.md:14`); "His frustrated pride about the arm and Halaster surfaces as one clipped, bitter sentence, then composure again." (`manshoons-zhentarim.md:15`)
- **Habit with the arm (voice and adventure):** "He flexes the artificial hand before a decision." (`manshoons-zhentarim.md:20`); "attaches a metal appendage to the withered stump of his left arm" (`sources/adventure-wdh.json:30250`).
- **Habit with the mask (adventure):** "The mask on the table is nonmagical, but {@creature Manshoon|WDH} likes to put it on before meeting with his followers." (`sources/adventure-wdh.json:30264`)
- **Habit of capture (Notable and Org):** "He prefers to capture rather than kill (prisoners answer questions; corpses do not)" (`01-manshoon.md:24`).
- **Curiosity (Alexandrian, book p.16):** "Manshoon wanted to know where that money has gone." ([PDF-IMAGE] `sources/1. The Villains.pdf`, book p.16 [PDF p.4 of 7])
- **Need to get back in the game (Alexandrian, book p.16):** "After he lost his Eye to Xanathar, Manshoon needed to get back in the game." ([PDF-IMAGE] book p.16)
- **Amusement (adventure):** "{@creature Manshoon|WDH} is amused by the creature, so he keeps it alive but locked in the cell." (`sources/adventure-wdh.json:28504`)
- **Love of books (adventure):** "{@creature Manshoon|WDH} has amassed a sizable collection, including ten rare volumes he removed from Duhlark Kolat's collection." (`sources/adventure-wdh.json:30150`)
- **Contempt for followers (adventure):** "since he considers all his followers expendable." (`sources/adventure-wdh.json:30255`)
- **Grudge with the Blackstaff and Elminster (adventure):** "Manshoon has a long list of powerful enemies" (`sources/adventure-wdh.json:26731`) — the list is in A11.
- **Grudge with Halaster (adventure and Notable):** "Halaster captured {@creature Manshoon|WDH} and amputated his left arm at the elbow for reasons unknown." (`sources/adventure-wdh.json:32217`); Notable: "dark fascination with a centuries-old wizard who lost an arm to Halaster Blackcloak and refuses to stop scheming" (`01-manshoon.md:12`).
- **Staff kept near the bed (adventure):** "grabs his {@item staff of power} (which he hides under the bed)" (`sources/adventure-wdh.json:30257`).
- **Place he cares about (adventure):** the sanctum: "Only those who breach his extradimensional sanctum see his full power." (`01-manshoon.md:24`) (Notable Morale).
- **Person he trusts least (campaign):** "Manshoon held little trust for any of his new allies." (`W:85`); "Manshoon ... set his spies on them" (`W:85` continues "He sent out spies"). Campaign's Org: "Trust Is Issued and Revoked: Access to Kolat Towers is something Manshoon grants and can withdraw." (`organizations/09-manshoons-zhentarim.md:41`).
- **Person he trusts most (campaign):** Sidra, "the only person in the cell whose loyalty Manshoon has never tested, because testing it would mean he does not already know the answer." (`04-sidra-romeir.md:25`)
- **Wiki grudge (wiki only):** "Elminster claimed he had personally killed twenty-and-one Manshoon clones by the {{YearlinkName|1357}}." (`W:90`)
- **Wiki inner life (wiki only):** "Manshoon made sure his blind brother Asmuth fell off a bridge to his death before they returned to the keep where he and Chess planned to dispose of the usurpers." (`W:80`)
- **Wiki fear (wiki only):** "Manshoon developed his ultimate insurance plan, the notorious stasis clone spell." (`W:87`)

---

## Not found (searched, not in the sources)
- Personal goals for Manshoon outside the faction and the job: searched "Manshoon" with "wants", "dream", "love", "fear", "family", "mother", "brother" across `campaign/`; only the wiki's Asmuth and Harlshoon lines exist (wiki only).
- A mother, wife or child of Manshoon in the campaign: none. The adventure has none. (Searched `sources/adventure-wdh.json` lines with Manshoon.)
- "Stat block: Mage" for Manshoon: no source found (searched for "with modifications", "Mage" near Manshoon).
- Manshoon's CR in the campaign: none; the published adventure gives CR only for the simulacrum (8) (`adventure-wdh.json:32233`).
- "Council majority" beyond the Notable page (D14).
- Urstul's species in the adventure (F16).
- The Masked Lords' Council as a body with a vote count: arc-i uses "Council of Guildmasters" (`arc-i-kolat-towers.md:19`); the Open Lord file uses the Masked Lords; no vote count.
- A personal relationship between Manshoon and Laeral (campaign: "No source records a dealing between Laeral Silverhand and the cell." `organizations/09-manshoons-zhentarim.md:92`).

## Not readable
- `sources/Other remix files/` `.docx` files: `Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` (listed at `sources/SOURCE_GUIDE.md:688`) covers the Doom Raiders, not Manshoon's cell, so it is named here and was not opened. No other `.docx` in the source guide was tied to Manshoon's cell.
- Alexandrian PDFs were opened with the Read tool as images. No pdftotext; all PDF quotes are `[PDF-IMAGE]` and must be checked.
- `sources/research/pass4-bundles/manshoon/wiki.txt` (1979 lines) was searched, not re-read.

## Scope note
Grep for `Manshoon` across `campaign/` returned 1142 occurrences in 235 files (count mode). The files cited above are the setting, guide, quest-structure and gazetteer files that carry the figure's history, the day-one state, or a routed quest fact. The quest-event directories (`campaign/quests/faction-events/`) hold the Doom Raiders, Harpers, Emerald Enclave and other gates and were searched for "Manshoon Named" and the Floxin status outcomes; they are routed in E2, not quoted in full.
