# Pass 4 research: Manshoon (`campaign/setting/villains/manshoon.md`)

## How this was researched

- **Bundle read:** `sources/research/pass4-bundles/manshoon/adventure.txt` (read in full); `wiki.txt` (lines 1-396 and 1930-2053 read; lines 397-1929 searched with Grep, not read line by line); `adventure-hits.txt` (read in full); `campaign-hits.txt` (326 KB, too large to read; searched with Grep; every Manshoon claim below was checked against the campaign file itself).
- **Campaign files read:** the existing page (full); `campaign/setting/organizations/09-manshoons-zhentarim.md` (full); `campaign/setting/history/04-the-founding-of-chains.md` (full, including Draft Notes); `campaign/setting/history/08-the-players-arrive.md` (lines 22-37, 139, plus Grep); `campaign/structure/arc-i-kolat-towers.md` (lines 1-20, 209-221, 254-261, 346-355, plus Grep of all lines); `campaign/guides/gm-guide/running-the-villains.md` (lines 44-61, plus Grep); `campaign/guides/factions/10-manshoons-zhentarim.md` (lines 46-75, plus Grep); the notable-figure pages named in the quotes (Grep).
- **Published adventure:** `sources/adventure-wdh.json` (targeted Read and Grep; lines marked "(Read)" or "(Grep)" were checked directly); `sources/adventure-wdmm.json` (Grep).
- **Alexandrian PDFs:** `sources/1. The Villains.pdf` pages 13-18 (the Zhentarim section is printed p.16); `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, all 5 pages (printed pp.92-96). The Read tool returns these as page images with no text layer, so **every PDF quote below was transcribed from the rendered page**. Check them against the PDF before they go into a page.
- **Line numbers:** campaign and wiki line numbers come from Read or Grep output. Adventure line numbers are the JSON line numbers; lines I did not re-read are taken from the bundle's `adventure.txt` or `adventure-hits.txt`, which carry the same numbers, and are marked "(bundle)".
- **Ranking:** campaign files outrank the published adventure; the adventure outranks the Alexandrian remix; the wiki ranks last. Campaign rulings (history/04 Draft Notes) are cited where they settle a point.

---

## 1. Identity and core motive

**Published adventure (who he is)**

> "A clone of the wizard {@creature Manshoon|WDH}, one of the founders of the Zhentarim, is hiding in Waterdeep. He wants to rule the city, by claiming the cache of dragons and by using that wealth to bribe the Masked Lords into making him the new Open Lord. He also wants to regain control of the Black Network. {@creature Manshoon|WDH} lurks in Kolat Towers, a pair of wizards' towers in the Trades Ward. This residence is described in chapter 8."
> — `sources/adventure-wdh.json:560` (Read/Grep)

> "Referred to in this adventure simply as \"{@creature Manshoon|wdh},\" this clone of the ancient archwizard infiltrated Waterdeep years ago and has been hiding out in Kolat Towers ever since, in the city's Southern Ward."
> — `sources/adventure-wdh.json:32215` (bundle `adventure.txt`)

> "Now the original {@creature Manshoon|WDH} is dead, and it's widely believed that all his clones were destroyed as well. In fact, at least three are still alive. The one presently in Waterdeep escaped death by hiding out in Undermountain, where he eventually ran afoul of Halaster Blackcloak. After a brief spell duel, Halaster captured {@creature Manshoon|WDH} and amputated his left arm at the elbow for reasons unknown. {@creature Manshoon|WDH} escaped imprisonment and fled Undermountain, taking refuge in the city above. Attempts to magically regenerate his severed limb failed, forcing him to craft an artificial arm and hand for himself."
> — `sources/adventure-wdh.json:32217` (bundle `adventure.txt`)

> "The limb belonged to a human archmage named Manshoon—or, more precisely, to one of his clones. The clone challenged Halaster to a spell duel and lost more than just the contest. Halaster turned the limb into a guardian that attacks all intruders until the Mad Mage or a creature that looks like him waves it off. The limb has the statistics of an {@creature archmage}, with these changes:"
> — `sources/adventure-wdmm.json:26133` (Grep). Heading at `sources/adventure-wdmm.json:26119`: "1a. Left Hand of Manshoon"

- **"Clone of a clone" is not in any published source.** Grep for "clone of a clone" in `sources/adventure-wdh.json`, `sources/adventure-wdmm.json`, `sources/research/pass4-bundles/manshoon/wiki.txt` and `sources/*.md` returned no match. The phrase first appears in the campaign at `campaign/setting/organizations/09-manshoons-zhentarim.md:15` (section 2).

**Forgotten Realms Wiki (edition-tagged)**

> "'''Manshoon''' ({{Pronounce|man|SHOON|refs=<ref name=\"FRCS1e-DM-p25-26\" /><ref name=\"WDH5e-p4\">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was the founder of the [[Zhentarim]],<ref name=\"FRCS-p282\">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|282}}</ref> also known as the Black Network, until he was \"slain\" by [[Fzoul Chembryl]], his ally, and Lord [[Orgauth]] in [[1370 DR]]. However, it transpired that Manshoon had created a dozen or more [[clone]]s that the murderous duo then found themselves facing. Only three of these clones were known to have survived into the late 1370s [[DR]] and once more headed the evil organization known as the Zhentarim.<ref name=\"FRCS-p283\">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|283}}</ref>"
> — `sources/research/pass4-bundles/manshoon/wiki.txt:70` (edition cited: Forgotten Realms Campaign Setting 3rd edition, pp.282-283; the same text recurs at `wiki.txt:1565`)

- Wiki infobox, 5e (`wiki.txt:61-63`): "alignment5e    = [[Lawful evil]]" (line 61) and "challenge5e    = 13" (line 62), citing Waterdeep: Dragon Heist pp.208-209.

**Campaign (current remix state)**

> "Manshoon is a centuries-old wizard, a clone of a clone of the original Black Network's founder, who claims, as all surviving Manshoon clones do, to be the one true Manshoon. The gold means nothing to him as wealth. He wants the Stone of Golorr for what it knows: the Stone is a transformed aboleth, and encoded in its centuries of absorbed memory is ancient knowledge of the Weave's structure. Manshoon intends to use that knowledge to absorb the Weave and supplant Mystra. The vault is an instrument. The Stone is the goal."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:15`

> "- **Manshoon** — Human wizard (clone), lawful evil. See the **Manshoon** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:23`

> "The man in Kolat Towers is a clone of a clone who claims to be the true Manshoon, and he keeps a simulacrum in reserve."
> — `campaign/setting/history/04-the-founding-of-chains.md:25` (Lore Summary)

> "The man in Waterdeep is \"a clone of a clone\". He claims to be the one true Manshoon, as every surviving clone does."
> — `history/04:49`

> "The Manshoon who now occupies Kolat Towers is a clone of a clone — a body activated in Undermountain when the Manshoon before it died, as the clone network was designed to do. Halaster Blackcloak, who tolerated the clone for a time out of professional curiosity, eventually severed Manshoon's left arm at the shoulder with a blade that prevented magical regrowth. The clone fled Undermountain carrying the staff of power he had smuggled in and arrived in Waterdeep to find the Kolat Towers abandoned, the force field still running on its original enchantment, and the amulet manufacture instructions in Duhlark's study. Manshoon needed a base. The towers were available."
> — `campaign/structure/arc-i-kolat-towers.md:13`

**Core motive, published adventure**

> "{@creature Manshoon|WDH} yearns to rule Waterdeep as a tyrant, take over the Zhentarim, and use both seats of power to plunder and control the Sword Coast. He needs the gold in the Vault of Dragons to pay off Masked Lords and Zhentarim leaders whose support will be instrumental when the time comes to oust Lady {@creature Laeral Silverhand|WDH} as Open Lord. {@creature Manshoon|WDH} has a long list of powerful enemies, among them the Harpers, Elminster of Shadowdale, Halaster Blackcloak of Undermountain, and the Blackstaff of Waterdeep. These enemies would quickly move against {@creature Manshoon|WDH} if they learned he was hiding in Waterdeep. For his evil plans to succeed, {@creature Manshoon|WDH} must operate in the shadows for the time being."
> — `sources/adventure-wdh.json:26731` (Read)

> "{@creature Manshoon|WDH} aims to rule Waterdeep and replace the City Watch with Black Network mercenaries that are loyal to him alone. By bribing and blackmailing the Masked Lords, he hopes to oust {@creature Laeral Silverhand|WDH} as Open Lord and take her place, kill the Blackstaff, reduce the Masked Lords to mere vassals, and declare himself the Wizard-King of Waterdeep. Once the city is firmly in his clutches, {@creature Manshoon|WDH} will then turn his attention toward Undermountain, destroy Halaster once and for all, and claim the dungeon's riches."
> — `sources/adventure-wdh.json:32219` (bundle `adventure.txt`)

> "The Zhentarim in Waterdeep is a fractured organization. Those who support {@creature Manshoon|WDH} want to destroy {@creature Xanathar|WDH} and seize political and economic control of the city. Those who oppose {@creature Manshoon|WDH} want to expose and destroy him before they are themselves apprehended or driven out of the city by the local authorities."
> — `sources/adventure-wdh.json:1445` (Read)

**Alexandrian remix (printed p.16)**

> "The Zhentarim were originally founded as a mercenary force by the wizard Manshoon, but they've been a fractured organization ever since the Manshoon Wars, when multiple clones of Manshoon warred for supremacy."
> — `sources/1. The Villains.pdf`, printed p.16 (PDF p.4), transcribed from page image

> "Most of Manshoon's clones were destroyed during the Manshoon Wars, but yet another has recently returned to Waterdeep (claiming, as they all do, to be the one true Manshoon). When he peeled off a large hunk of the local Zhentarim network that had been established by the Doom Raiders (see p. 198 of Dragon Heist), he became aware that Lord Neverember had used the local Zhentarim's resources to embezzle hundreds of thousands of gold dragons from the government."
> — `sources/1. The Villains.pdf`, printed p.16 (transcribed)

- The Alexandrian p.16 does not say "clone of a clone"; it says "yet another has recently returned". It names no Weave goal and no simulacrum.

---

## 2. Background

### 2a. Founding of the Zhentarim

> "Feeling exposed, Manshoon immediately set about creating a cabal of mages, his [[Black Cloaks]], to protect him, recruiting Fzoul early on. Not long afterward, in the {{YearlinkName|1261}}, he founded the Zhentarim."
> — `sources/research/pass4-bundles/manshoon/wiki.txt:87`

> "During this period, Manshoon developed his ultimate insurance plan, the notorious ''[[stasis clone]]'' spell."
> — `wiki.txt:89`

> "| formed         = [[1261 DR]]<ref name=\"LoD-p96\" /><ref name=\"tGHotR-p128\" />"
> — `wiki.txt:219` (Zhentarim infobox)

> "| leader         = [[Pereghost]]<ref name=\"SCAG-p78\" /> <br /> {{former}} <br /> [[Fzoul Chembryl]]<ref name=\"LoD-p96\"/> <br/> [[Manshoon]] (founder)<ref name=\"LoD-p96\"/> and [[Sememmon]]<ref name=\"RoZK:CB-p32\" />"
> — `wiki.txt:214`

> "As of [[1489 DR]] the Zhentarim was headquartered in the [[Western Heartlands]], at [[Darkhold|Darkhold Castle]], nestled in the [[Darkhold Vale|valley of the same name]].<ref name=\"SCAG-p78\" />"
> — `wiki.txt:254` (Zhentarim page). The campaign names no Waterdeep HQ for the Zhentarim as a whole; it names the Splinter's own sites (section 2e).

> "- Manshoon was born in Zhentil Keep in 1229 DR and became one of the city's lords. He founded the Zhentarim in 1261 DR, and the Banite priest Fzoul Chembryl joined him in 1263 DR."
> — `campaign/setting/history/04-the-founding-of-chains.md:32`

> "- The published adventure calls Manshoon \"one of the founders\" of the Zhentarim. This page follows the wiki and treats him as the founder."
> — `history/04:33`

### 2b. The clones and the Manshoon Wars

> "Over the years Manshoon died many times, always coming back in a new body in half a day."
> — `wiki.txt:92`

> "In the {{YearlinkName|1370}}, Manshoon was \"slain\" again by Fzoul and Lord Orgauth, who then found themselves facing around a dozen clones that the wizard had created. Each of the clones was convinced that he was the real Manshoon and was inexplicably compelled to slay his rival clones. Most of these perished in the ensuing battles. The caches of magical items formerly hidden by Manshoon were scattered throughout the Realms.<ref name=\"FRCS-p283\" /> These conflicts were known as the [[Manshoon Wars]].<ref name=\"C&D-p13\">{{Cite book/Cloak & Dagger|13}}</ref>"
> — `wiki.txt:94`

> "Three clones, who mastered this killing compulsion by means of spells and devices, survived, with the one that returned to the Zhentarim appearing to be 'the' Manshoon."
> — `wiki.txt:97`

> "The third took refuge in [[Undermountain]] with [[Halaster]]."
> — `wiki.txt:103`

> "The one in Undermountain appeared to have died during the events of the [[Spellplague]] itself."
> — `wiki.txt:108` (Post-Spellplague section)

> "In the [[1383 DR|Year of the Vindicated Warrior, 1383 DR]], the [[Shadovar]] moved against Zhentil Keep during the [[Shadowbane War]], razing it along with the Citadel of the Raven, killing both Fzoul and the final clone of Manshoon, leaving only Darkhold left."
> — `wiki.txt:435` (Zhentarim page, History section)

> "By [[1492 DR]],{{WDH-time}} the Undermountain Manshoon had resurfaced in Waterdeep, having survived the Spellplague and his clash with Halaster Blackcloak. During the latter battle, Manshoon's left arm was severed and proved impossible to magically regenerate, forcing him to use a metal prosthetic instead, while the original was kept and reanimated by Halaster.<ref>{{Cite book/Waterdeep: Dungeon of the Mad Mage|119}}</ref> The ancient archwizard had infiltrated Waterdeep years before and had been hiding out in [[Kolat Towers]] ever since, plotting to replace the [[City Watch (Waterdeep)|City Watch]] with Black Network mercenaries that were loyal to him alone and to rule Waterdeep as Wizard-King.<ref>{{Cite book/Waterdeep: Dragon Heist|208}}</ref>"
> — `wiki.txt:125`

> "- Manshoon built the stasis clone spell as insurance against his enemies. Over the years he died several times and returned in a new body."
> — `campaign/setting/history/04-the-founding-of-chains.md:44`

> "- Three clones survived. One rejoined the Zhentarim and conceded leadership to Fzoul, one became the vampire Orbakh in Westgate, and one took refuge in Undermountain with Halaster."
> — `history/04:46`

> "- The published adventure tells it differently: a mishap woke every clone at once, at least three survive, and the one now in Waterdeep hid in Undermountain. Halaster Blackcloak captured him and took his left arm, the regrowth failed, and he wears an artificial arm and hand."
> — `history/04:47`

> "Fearing that he might be destroyed by his foes, {@creature Manshoon|WDH} magically crafted several clones-but a mishap caused all of them to be awakened at once, whereupon they tried to destroy one another in a series of conflicts that came to be known as the {@creature Manshoon|WDH} Wars."
> — `sources/adventure-wdh.json:32216` (bundle `adventure.txt`; the same paragraph begins "The original {@creature Manshoon|WDH} was one of the founders of the Zhentarim.")

### 2c. Arrival in Waterdeep and Kolat Towers

**Ward (settled this session; the wiki page now agrees)**

> "| location      = [[Southern Ward of Waterdeep]], [[Waterdeep]]"
> — `wiki.txt:1946` (LINKED WIKI PAGE: Kolat Towers)

> "[[Category:Locations in the Southern Ward of Waterdeep]]"
> — `wiki.txt:1988`

> "This dilapidated, two-towered edifice stands tall in the Southern Ward. Its neighbors are aware of the magical force field that surrounds it, and they can see light from {@spell continual flame} spells spilling out of the windows. Despite these persistent magical effects, most folk believe the structure is abandoned. Others think it's haunted by the ghosts of the Kolat brothers. They're wrong, of course."
> — `sources/adventure-wdh.json:26797` (Read/Grep)

> "{@creature Manshoon|WDH} posts no visible guards outside Kolat Towers, since he wants others to believe the site is abandoned. The evil wizard and his underlings come and go using teleportation circles inside the towers."
> — `sources/adventure-wdh.json:26798` (Grep)

> "**Settled by ruling 1:** The ward of Kolat Towers. `adventure-wdh.json` lines 26797, 32215 and 32218 say the Southern Ward, and line 560 says the Trades Ward. The campaign follows the Southern Ward, and `arc-i-kolat-towers.md` and `guides/factions/10-manshoons-zhentarim.md` line 73 now say so. The wiki's **Kolat Towers** page agrees: it puts the towers in the Southern Ward, in the Adventurers' Quarter on Weeping Maiden's Run, citing Dragon Heist pages 148-157 (Session 50)."
> — `campaign/setting/history/04-the-founding-of-chains.md:162` (Draft Notes)

> "**Lair: Kolat Towers** (Southern Ward)"
> — `campaign/guides/factions/10-manshoons-zhentarim.md:73`

> "Kolat Towers stands in the Southern Ward, so the Trades Ward house on Ironwick Lane is not near it."
> — `campaign/quests/faction-events/lords-alliance/r03-redknife/design-notes.md:24` (Grep)

**Clone's arrival and the Splinter (campaign)**

> "He spent two years building the Splinter cell — the faction that bears his name but operates independently of the Zhentarim's surviving leadership. The structure is hub-and-spoke: Kolat Towers as the command center, with the Interrogation House in the North Ward and Yellowspire in the Castle Ward serving as field offices connected by teleportation circles. A pass-amulet system replaced the need for a trusted courier network; amulets could be revoked remotely, confiscating access without confrontation. The towers' extradimensional sanctum — a space behind the towers that is not physically behind the towers, accessible only via a teleportation ring keyed to a specific circle in K22 — houses Manshoon's closest lieutenants and his most sensitive operations."
> — `campaign/structure/arc-i-kolat-towers.md:15`

> "- Manshoon's clone fled Undermountain, found the towers abandoned with the force field intact, and took the amulet-making instructions from Duhlark's study. He spent two years building the Splinter."
> — `history/04:73`

> "- The clone then spent two years building the Splinter cell, which is about 1490 DR counted back from Ches 1, 1492 DR. `[research]` The structure is hub-and-spoke: Kolat Towers as the command center, with the Interrogation House in the North Ward and Yellowspire in the Castle Ward as field offices."
> — `campaign/setting/history/08-the-players-arrive.md:34`

> "- Manshoon's clone fled Undermountain after Halaster Blackcloak severed its left arm, found Kolat Towers abandoned with the force field still running, and took the towers as a base. Source: the **Kolat Towers** quest opener."
> — `history/08:33`

> "- The simulacrum in Kolat Towers was created seven years before the campaign, about 1485 DR, and has been preserved in ice since. `[research]`"
> — `history/08:35`

> "- Manshoon's clone arrived later, took over Kolat Towers and built a cell of his own, the Splinter, in about two years. He peeled off a large part of the Doom Raiders' local network."
> — `history/04:27`

> "- The clone arrived after the Doom Raiders and peeled off a large part of the local network they had built. Through it he learned that Neverember had used the local Zhentarim's resources in the embezzlement."
> — `history/04:76`

> "Two cells use the name Zhentarim in Waterdeep, and each denies the other's claim. The distinction should become clear to attentive players during **Trollskull Alley**, because the Doom Raiders' professionalism makes Manshoon's operatives land harder when they appear."
> — `history/04:84`

> "Factions that speak to players say \"the Splinter\" or \"the other cell\" until **Manshoon Named** is marked for the listener."
> — `history/04:89`

> "**A note on the Zhentarim:** Two cells operate in Waterdeep. Davil Starsong's **Doom Raiders** are the player-joinable faction covered on **The Zhentarim (Doom Raiders)** organization page. Manshoon's splinter is a completely separate organization that peeled off from the Doom Raiders' local network when he returned to Waterdeep. The two groups dislike each other. When players ally with the Zhentarim through Davil, they're working with the Doom Raiders, not Manshoon. The villains in this section answer only to Manshoon."
> — `organizations/09-manshoons-zhentarim.md:13`

**Kolat Towers history (building, the brothers, Gondafrey)**

> "Duhlark Kolat built the towers that bear his name during the late fourteenth century as an experiment in paranoid architecture. His brother Alcedor wanted a home; Duhlark wanted a fortress that could withstand siege, scrying, and betrayal from within. The result — two interconnected stone towers in the Southern Ward, linked by a bridge at the third floor and bound together by a force field that covered the entire structure from basement to roof — was more fortress than home. Alcedor moved in anyway. The force field admitted no one without a specially keyed amulet. Alcedor accepted this as the cost of living with his brother. He died in the towers in 1385 DR under circumstances that remain unclear. Duhlark survived him by nine years before being found dead in his study, apparently of old age, with the force field still running."
> — `campaign/structure/arc-i-kolat-towers.md:9`

> "- In 1379 DR the City Watch captain Lady Gondafrey tried to breach the towers and was taken prisoner. Alcedor died there in 1385 DR, and Duhlark died nine years after him with the force field still running."
> — `history/04:72`

> "Before [[1368 DR]], the wizard brothers, [[Alcedor Kolat|Alcedor]] and [[Duhlark Kolat]], bought the buildings and, much to the chagrin of the local building guilds, stitched the building together using spells such as ''[[wall of stone]]'' and ''[[stone shape]]''."
> — `wiki.txt:1969`

> "Kolat Towers once belonged to two eccentric brothers, Duhlark and Alcedor Kolat. Both were wizards."
> — `sources/adventure-wdh.json:26863` (Read)

> "Duhlark's paranoia continued to grow, until he suspected Alcedor of selling their secrets. Alcedor left the towers, never to be heard from again, and Duhlark became a recluse who died in his own fortress."
> — `sources/adventure-wdh.json:26865` (Read)

> "{@creature Manshoon|WDH} found Duhlark Kolat's skeletal remains in the bed and transformed his skull into a flameskull. He left the rest of the bones alone, hidden behind cobwebs. The flameskull attacks anyone other than {@creature Manshoon|WDH} who confronts it, shouting, \"Get out of my house!\" between casting spells and throwing off fire rays."
> — `sources/adventure-wdh.json:28680` (bundle `adventure-hits.txt`)

> "Near the end of the 15{{th}} century DR, the towers appeared to be abandoned and possibly inhabited by ghosts, although the force field still stood. The truth was it was inhabited by [[Manshoon]] and his lackeys. Manshoon also had an extra-dimensional sanctum accessed via a ''[[teleportation circle]]'' inside the lower tower."
> — `wiki.txt:1977`

> "Duhlark Kolat did indeed die within the tower. His body rested in a secret bedroom at the top of the taller tower. Manshoon had turned his skull into a [[flameskull]]."
> — `wiki.txt:1979`

**The sanctum and the teleporter rings (adventure)**

> "{@creature Manshoon|WDH}'s extradimensional sanctum exists in a finite demiplane. Created by the original {@creature Manshoon|WDH}, it is known to the wizard's clones, and it currently serves as the lair of the clone described in this adventure."
> — `sources/adventure-wdh.json:28796` (bundle `adventure-hits.txt`)

> "To access {@creature Manshoon|WDH}'s extraplanar sanctum, one needs a {@item teleporter ring|WDH}: a brass signet ring bearing a stylized M, and which emanates an aura of conjuration magic when targeted by a {@spell detect magic} spell or similar magic. {@creature Manshoon|WDH} gives these rings to his most trusted servants."
> — `sources/adventure-wdh.json:28822` (bundle `adventure-hits.txt`)

**Urstul Floxin (background)**

> "The incident with the fireball has strained the alliance between the Gralhunds and the Black Network. {@creature Urstul Floxin|wdh} is refusing to hand over the {@item Stone of Golorr|WDH} until he speaks to his secret master, {@creature Manshoon|WDH}."
> — `sources/adventure-wdh.json:4379` (bundle `adventure-hits.txt`)

> "{@creature Urstul Floxin|wdh} works for {@creature Manshoon|WDH}, and he is the highest-ranking member of the Zhentarim squad stationed at House Gralhund. Urstul is a glorified thug with all the charm and breeding of a snake, but the Gralhunds tolerate him because he feeds them useful information culled from his spies throughout the city. Urstul takes his orders from {@creature Manshoon|WDH}'s current simulacrum, which comes and goes from House Gralhund by way of a teleportation circle (connected to the circle in Kolat Towers)."
> — `sources/adventure-wdh.json:32644` (bundle `adventure-hits.txt`)

> "He is being punished for allowing the {@item Stone of Golorr|WDH} to slip through his fingers (during the events of chapter 3). Nevertheless, he remains loyal to {@creature Manshoon|WDH}."
> — `sources/adventure-wdh.json:30041` (bundle `adventure-hits.txt`; the paragraph begins "If he survived earlier encounters with the characters, {@creature Urstul Floxin|wdh} (see {@adventure appendix B|WDH|12}) stands at the table, dourly scrubbing lab equipment.")

> "- **Urstul Floxin** — Illuskan human assassin, lawful evil. Thuggish leader who ran both the Dalakhar capture attempt and the Gralhund Villa operation. If he survives the Villa, he leads a response team later in the campaign. Carries the *Directive to Urstul Floxin*: prisoners from other factions are to be delivered to Avareen in Brindul Alley. See the **Urstul Floxin** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:27`

> "To the world, Urstul is a large, heavyset man in his forties who treats every room as his own. To those he works with, he is Manshoon's chief field operative who runs both the Dalakhar capture attempt and the Gralhund Villa operation. Deep down, he will not divulge his master's name unless magically compelled, and he keeps a collection of black flying snakes as couriers because he trusts animals more than people."
> — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:22` (Grep)

> "Urstul Floxin belongs to Manshoon's Zhentarim splinter — a rival cell to the Doom Raiders that the two organizations do not share intelligence with, do not coordinate with, and are in active internal conflict with. A Doom Raiders character asking about Floxin is asking about an enemy, not a colleague."
> — `sources/Act_III_Arc_D.md:251` (Grep)

---

## 3. Personality

**Wiki (edition: Forgotten Realms Campaign Setting 3rd edition, p.283)**

> "Completely fitting the archetype of the sly-tongued, sinister, and decadent master spellcaster, Manshoon ruthlessly crushed revolts within his own ranks of the Black Network, easily slaughtered his rivals and weeded the weak out the ranks of the young and ambitious by sending upstarts on nigh-impossible suicide missions. Hated and mistrusted by Fzoul, Manshoon manipulated him much as he did all others—remaining arrogant, untouchable in his power, and faintly amused by it all."
> — `wiki.txt:73` (cite: `FRCS-p283`)

**Published adventure: concealment, avoidance of fights, expendable followers, bargaining**

> "{@creature Manshoon|WDH} creates copies of himself using the {@spell simulacrum} spell and takes great pains to conceal his identity, since his success hinges on not attracting the attention of others who would seek to thwart him before his plans come to fruition. {@creature Manshoon|WDH} avoids unnecessary confrontations with adventurers; only those who enter his extradimensional sanctum are likely to incur his wrath."
> — `sources/adventure-wdh.json:561` (bundle `adventure-hits.txt`)

> "This version of {@creature Manshoon|WDH} isn't spoiling for a fight. He commends the characters for making it this far and shows no concern for the Zhents they defeated to reach him, since he considers all his followers expendable."
> — `sources/adventure-wdh.json:30255` (Read)

> "The characters' best chance of survival is to convince {@creature Manshoon|WDH} that they can be cowed or bribed into working for him. Weary of his conflict with the Xanathar Guild, {@creature Manshoon|WDH} suggests that the characters prove their usefulness to him by hunting down and killing {@creature Xanathar|WDH} in its lair (see chapter 5). {@creature Manshoon|WDH} also demands that they keep his presence in Waterdeep a secret for now, saying that he will reward them for their discretion \"when the time comes.\" In exchange, he allows the characters to return to Waterdeep and promises them positions of power in his organization once {@creature Xanathar|WDH}'s death is confirmed. He has no intention of making good on this promise, but refusing to work for him puts the characters in a tight spot, since the evil archwizard can't risk exposure."
> — `sources/adventure-wdh.json:30256` (Read)

> "A head-on battle with {@creature Manshoon|WDH} isn't likely to go well for the characters. That said, the wizard's greatest weakness is that he has powerful enemies in Waterdeep. The risk of exposure keeps him hidden, and the characters can thwart him by furnishing his enemies with proof that he's alive (after a fashion) and operating in Waterdeep. When it comes to {@creature Manshoon|WDH} clones, deciding to \"let the city deal with it\" is a wise course of action."
> — `sources/adventure-wdh.json:26738` (Read)

> "If the characters find themselves at the evil wizard's mercy, {@creature Manshoon|WDH} will gladly trade their pitiful lives for the {@item Stone of Golorr|WDH} and the keys to unlock the Vault of Dragons. In exchange for helping him get the gold, he promises the characters 10 percent of the trove (50,000 gp). {@creature Manshoon|WDH} has no intention of honoring this agreement, but it can help buy the characters some time."
> — `sources/adventure-wdh.json:26739` (Read)

> "If the characters make an enemy of {@creature Manshoon|WDH}, he tries to capture one of them and replace that character with a magical duplicate created using the {@spell simulacrum} spell. If one of the players is absent for a game session and circumstances allow it, {@creature Manshoon|WDH} targets that character for replacement while the rest of the party is distracted by other matters. You don't need to roleplay the character's capture; just assume it happens. To create a simulacrum of the character, {@creature Manshoon|WDH} needs some hair, fingernail clippings, or other piece of the character's body. Once he obtains the necessary components from the captured character, he creates the simulacrum and sends it to the party with instructions to spy on the group and undermine it from within."
> — `sources/adventure-wdh.json:30409` (Read)

**Campaign: precision, capture over killing, underestimation**

> "He keeps a simulacrum in Kolat Towers while Manshoon watches from safer ground. His approach reflects his temperament: precision, patience, no unnecessary violence. The Zhentarim response teams are the weakest in raw muscle of any faction. This is deliberate. Drawing too much attention is the one mistake Manshoon won't make twice."
> — `organizations/09-manshoons-zhentarim.md:19`

> "**Resonance.** Manshoon should inspire intellectual dread with his patient precision, frustrated rage from the party's inability to pin him down, and dark fascination with a centuries-old wizard who lost an arm to Halaster Blackcloak and refuses to stop scheming."
> — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:13` (Grep)

> "**Morale.** In combat, Manshoon lets his simulacrum absorb the opening volley while he casts from behind it. He prefers to capture rather than kill (prisoners answer questions; corpses do not), and this habit creates tactical openings the party can exploit. Only those who breach his extradimensional sanctum see his full power."
> — `01-manshoon.md:25` (Grep)

> "Any Zhentarim team sent to attack the characters carries orders to take them as prisoners to the Interrogation House on Brindul Alley. Questioned team members can point the characters toward the house. The lighter roster is intentional. Manshoon wants intelligence, not body counts, and underestimated enemies are more useful to him than dead ones. These teams also keep pressure on the party without forcing a lethal confrontation."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:9` (Grep)

> "**Manshoon.** Manshoon underestimates threats that aren't magical. Operatives who avoid Kolat Towers may run for sessions before he escalates past response teams. His preference for capturing over killing creates tactical openings."
> — `campaign/guides/gm-guide/running-the-villains.md:59` (Read)

> "Manshoon underestimates threats that aren't magical. A party that stays clear of Kolat Towers may go tendays before he escalates beyond his response teams. His preference for capturing over killing creates tactical openings."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:56` (Read)

> "Manshoon: Archmage running a Zhentarim splinter cell from Kolat Towers. Uses simulacrums for deniability. Agenda: political control of Waterdeep, eliminate the Doom Raiders who he sees as weak."
> — `sources/SOURCE_GUIDE.md:135` (Alexandrian summary; the PDF p.16 text does not contain "simulacrum" or "deniability")

> "Faction goals and methods — how each faction's *way of doing things* differs (Xanathar: brute force and paranoia; Manshoon: precision and deniability; Cassalanters: social manipulation and infernal leverage; Jarlaxle: charm and information)"
> — `sources/SOURCE_GUIDE.md:139`

- "Underestimation" and "precision and deniability" are campaign or guide claims. The adventure, the wiki and Alexandrian p.16 do not say them.

---

## 4. Relationships

### 4a. Xanathar

> "{@creature Xanathar|WDH} is a paranoid, megalomaniacal beholder crime lord whose goal is to wipe out anyone it perceives as a Zhentarim operative or sympathizer, retrieve the {@item Stone of Golorr|WDH}, and secure the cache of dragons."
> — `sources/adventure-wdh.json:527` (bundle `adventure-hits.txt`)

> "Beneath the city streets lurks a criminal underworld, its leader a beholder called {@creature Xanathar|WDH}. Hoping to gain a political foothold in Waterdeep, agents of the Zhentarim (also known as the Black Network) recently tried to ally their organization with the Xanathar Guild. The architect of this attempt was a clone of the wizard {@creature Manshoon|WDH}, a founder of the Black Network long thought dead."
> — `sources/adventure-wdh.json:472` (bundle `adventure-hits.txt`)

> "| Manshoon | Rival | Active enemy; Xanathar has ordered Manshoon killed twice; both failed; this is accelerating the paranoia |"
> — `campaign/setting/villains/xanathar.md:51` (Grep)

> "- The war with Manshoon is an active, low-level street war in the Dock Ward, grinding on with the kill order that has failed twice."
> — `villains/xanathar.md:58` (Grep)

> "| **Xanathar vs. Manshoon** | Active street war — low-level, in the Dock Ward | Manshoon's operatives probe Guild territory, and Xanathar's kill order on Manshoon has failed twice. Manshoon knows Xanathar killed his envoys and kept Eye #1. Agorn Fuoco monitors Orb Confectioners. Xanathar suspects a mole; it's hunting in the wrong direction. | *Report to Agorn Fuoco* |"
> — `campaign/guides/gm-guide/running-the-villains.md:71` (Grep)

> "The ward is the front line of a street war between Xanathar's Guild and Manshoon's Zhentarim. It began when Manshoon's envoys came to Skullport three months before the fireball and Xanathar killed them. Brawls between the two are common, and the Watch is called to them often."
> — `campaign/gazetteer/waterdeep/dock-ward.md:41` (Grep)

- Undermountain (WDMM) does not say which Zhentarim cell is meant: "A drow mage in league with the Zhentarim has set up a hidden base on this level" (`sources/adventure-wdmm.json:4036`); "Rizzeryl works for two groups: House Auvryndar, a low-ranking drow house from Menzoberranzan that is slowly and secretly consolidating its power in Undermountain, and the Zhentarim, which is trying to drive the Xanathar Guild out of Skullport." (`sources/adventure-wdmm.json:6578`); "Bosskyn Gorrb, a blind tiefling {@creature spy}, leads the Zhentarim in Skullport and uses flying snakes to deliver messages to his underlings." (`sources/adventure-wdmm.json:63737`).

### 4b. Jarlaxle

> "| Manshoon | Mutual wariness | Non-interference arrangement, fragile; Jarlaxle has better intelligence and intends to keep it that way |"
> — `campaign/setting/villains/jarlaxle.md:48` (Grep)

> "| Jarlaxle | Mutual wariness | The only Grand Game player Manshoon takes seriously; non-interference arrangement, fragile; Jarlaxle has better intelligence and both know it |"
> — existing page line 34

> "The forces sent by {@creature Xanathar|WDH}, the Cassalanters, and {@creature Manshoon|WDH} attack the characters on sight. Jarlaxle, on the other hand, congratulates characters for unlocking the Vault of Dragons and allows them to leave on the condition that they go empty-handed. He intends to see the gold safely returned to the city of Waterdeep but also demands the {@item dragonstaff of Ahghairon|WDH} for his trouble."
> — `sources/adventure-wdh.json:14786` (Grep)

- The published adventure has no Manshoon–Jarlaxle arrangement. The Jarlaxle entries (`adventure-wdh.json:549`, bundle `adventure.txt:32178-32182`) name no Manshoon.

### 4c. Fenerus Stormcastle

> "| **Manshoon vs. Bregan D'aerthe** | Escalating interference | Manshoon has identified Fenerus Stormcastle as a D'aerthe cut-out and ordered his abduction. Krebbyg Masq'il'yr has flagged the Zhentarim surveillance to Jarlaxle. If the abduction proceeds, Jarlaxle's Trades Ward intelligence network is directly compromised. | *Directive to Zorbog Jyarkoth* (Interrogation House), *Letter Regarding Fenerus Stormcastle* (Seven Masks Theater) |"
> — `campaign/guides/gm-guide/running-the-villains.md:75` (Grep)

> "Front Room.* Avareen and Zorbog's quarters. Avareen carries a pass-amulet to Kolat Towers. While the party explores, a flying snake arrives with *A Directive to Zorbog* signed by \"Manshoon,\" ordering Zorbog to kidnap Fenerus Stormcastle of Quill Alley, a \"known associate of these new meddlers in the Grand Game.\""
> — `campaign/guides/factions/10-manshoons-zhentarim.md:23` (Grep; the bullet opens with "*Front Room.*")

> "Fenerus is the former founder of the Blood Hawk Posse (current brigands on the Amphail road), a Bregan D'Aerthe cut-out and message-drop on Quill Alley (unknowing; he believes his contacts are Luskan agents), a City Watch prisoner who hid the Stone of Golorr before his arrest, and the target of Manshoon's kidnap directive in **Faction Outposts**."
> — `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:26` (Grep; the line begins "**Relationships.**")

> "Fenerus Stormcastle was the founder of the Blood Hawk Posse, a gang of horse-riding brigands that, to this day, harries travelers on the road to Amphail."
> — `sources/adventure-wdh.json:7123` (Grep)

> "The door to Fenerus's house stands open, and the place has been ransacked. Painted in blood on the kitchen wall is a circle with ten equidistant lines radiating outward from its circumference: the sign of {@creature Xanathar|WDH}."
> — `sources/adventure-wdh.json:7114` (Grep)

> "Shortly after Fenerus's arrest, drow agents of Bregan D'aerthe showed up to collect the stone and were waylaid by {@condition invisible} duergar hiding in the alley. The duergar were members of the Xanathar Guild that had been sent by {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) to retrieve the stone."
> — `sources/adventure-wdh.json:7126` (Grep)

- The published adventure never links Fenerus to Manshoon. The Fenerus material (lines 7087-7152) names Xanathar, Bregan D'aerthe and Luskan. The Manshoon abduction directive is campaign-only.

### 4d. The Doom Raiders and Davil Starsong

> "The Doom Raiders and Manshoon's Zhentarim splinter cell are at active war. Manshoon's cell came later and peeled off the Doom Raiders' network, and the two cells despise each other: information shared with the Doom Raiders will not reach Manshoon's agents. However, characters who join the Doom Raiders are joining the older cell and will inevitably be caught in the crossfire as Manshoon moves to eliminate Davil's cell entirely. This is a structural feature of the campaign."
> — `campaign/setting/organizations/06-doom-raiders.md:25` (Grep)

> "**Primary Contact:** Davil Starsong — a sun elf retired adventurer who leads the Doom Raiders' Waterdeep operation. Charming, direct, and genuinely invested in ending the street violence Manshoon's cell has caused. Tashlyn Yafeera handles the cell's business whenever Davil is unavailable."
> — `organizations/06-doom-raiders.md:27` (Grep)

> "- Davil wants to end the street violence that Manshoon's cell has caused, because a legitimate criminal enterprise cannot run in a city where an illegitimate one keeps shooting people."
> — `history/04:62`

> "- The Doom Raiders believe they are the true Zhentarim of Waterdeep. The old outline says Davil's cell \"separates from Manshoon on pragmatic grounds\". The sources reverse that direction: the cell came first, and Manshoon's clone peeled off its network."
> — `history/04:64`

> "Delivering proof that {@creature Manshoon|WDH} is hiding in Waterdeep to {@creature Laeral Silverhand|WDH}, {@creature Mirt|WDH}, the Harpers, Force Grey, the Blackstaff, the Lords' Alliance, the Order of the Gauntlet, the City Watch, or the Watchful Order of Magists and Protectors triggers a far-reaching effort to oust him from the city. Such proof can be obtained from any of {@creature Manshoon|WDH}'s lieutenants, who can be captured and turned over for interrogation. These lieutenants include Sidra Romeir ({@area K2|3db}), {@creature Manafret Cherryport|wdh} ({@area K3|3de}), {@creature Urstul Floxin|wdh} ({@area E5|41d}), Vevette Blackwater and Agorn Fuoco ({@area E8|425}), and {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} ({@area E10|42a})."
> — `sources/adventure-wdh.json:26763` (Read)

> "{@creature Davil Starsong|WDH} (see {@adventure appendix B|WDH|12}) asks the characters for a donation of 5,000 gp to keep his branch of the Zhentarim afloat in Waterdeep. Recent altercations and legal issues have drained the Doom Raiders' coffers. If the characters refuse, the Doom Raiders are driven out of the city, yielding control of the Zhentarim in Waterdeep to {@creature Manshoon|WDH} (if he's alive)."
> — `sources/adventure-wdh.json:14893` (Grep)

> "If {@creature Manshoon|WDH} is the main villain, {@creature Skeemo Weirdbottle|WDH} betrays his fellow Doom Raiders and fights alongside {@creature Manshoon|WDH}'s simulacrum."
> — `sources/adventure-wdh.json:14855` (bundle `adventure-hits.txt`; the sentence sits in the final-chapter Doom Raiders paragraph)

> "{@creature Davil Starsong|WDH} (see {@adventure appendix B|WDH|12}) is the characters' primary contact in the Black Network, at least initially. Over drinks, he shares the following information:"
> — `sources/adventure-wdh.json:4011` (Grep)

> "{@creature Davil Starsong|WDH} (see {@adventure appendix B|WDH|12}) is the characters' primary contact..." — see above. Also `sources/adventure-wdh.json:6087` (bundle): "After {@creature Davil Starsong|WDH} is taken in for questioning, {@creature Istrid Horn|WDH} (see {@adventure appendix B|WDH|12}) sends a message to the characters by way of a {@creature flying snake}."

> "The Doom Raiders were five unscrupulous adventurers who liked to plunder lich lairs (called \"dooms\" by some). They gave up adventuring to join the Black Network and came to Waterdeep three years ago with plans to establish a Zhentarim foothold in the city."
> — `sources/adventure-wdh.json:31916` (Grep)

> "- They were sent to Waterdeep in 1489 DR to establish a Zhentarim foothold. The published adventure says only that they came \"three years ago\"."
> — `history/04:57`

> "**Neutralize a named Manshoon operative (+2).** Eliminate or capture one of Manshoon's lieutenants — Urstul Floxin, Vevette Blackwater, Agorn Fuoco, or any other named agent. Delivering a prisoner to Tashlyn earns the full renown; confirmed elimination earns +1."
> — `sources/Appendix_B_-_Player_Factions.md:658` (Grep)

### 4e. Splinter cell members

Campaign list (`campaign/setting/organizations/09-manshoons-zhentarim.md:23-36`), with the adventure counterpart where one exists.

> "- **Sidra Romeir** — Calishite human veteran, lawful evil. Manshoon's most trusted lieutenant, stationed at Kolat Towers. Holds the teleport rings when lieutenants leave the Towers. If captured lieutenants are killed, Sidra gives their rings to Kaevja. See the **Sidra Romeir** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:24`
> Adventure: "The card players are Sidra Romeir (LE female Calishite human {@creature veteran}) and two subordinates (LE male Tethyrian human {@creature thug||thugs})." — `sources/adventure-wdh.json:28155` (bundle `adventure-hits.txt`)

> "- **Vevette Blackwater** (DH p. 216) — Human swashbuckler, lawful evil. A swashbuckler with fiery red hair streaked platinum that can glow in the dark on her command. Charming in public, cruel in private. Carries *Seffia Naelryke's Visiting Card*: Seffia approached Vevette to open a Cassalanter–Zhentarim communication channel, but Vevette rebuffed her, suspecting a trap. See the **Vevette Blackwater** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:25`
> Adventure: "Vevette Blackwater (CE female Tethyrian human {@creature swashbuckler|VGM}; see {@adventure appendix B|WDH|12}) and Agorn Fuoco (NE male Turami human {@creature bard|VGM}; see {@adventure appendix B|WDH|12})." — `sources/adventure-wdh.json:30120` (Grep)

> "- **Agorn Fuoco** (DH p. 195) — Human bard (Manshoon lieutenant), neutral evil. A bard and hollow coward who sends his thugs into danger while hanging back. Will barter his pass-amulet to Kolat Towers for his own life without hesitation. Carries a *Report to Agorn Fuoco*: intelligence confirming that Korgstrod's duergar operate out of Orb Confectioners on Rising Ride. See the **Agorn Fuoco** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:26`
> Adventure: "Agorn Fuoco (NE male Turami human {@creature bard|VGM}; see {@adventure appendix B|WDH|12})" — `sources/adventure-wdh.json:30120`

> "- **Urstul Floxin** — Illuskan human assassin, lawful evil. Thuggish leader who ran both the Dalakhar capture attempt and the Gralhund Villa operation. If he survives the Villa, he leads a response team later in the campaign. Carries the *Directive to Urstul Floxin*: prisoners from other factions are to be delivered to Avareen in Brindul Alley. See the **Urstul Floxin** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:27`

> "- **Avareen Windrivver** — Human spy (Zhentarim interrogator), lawful evil. Spy maintaining the Interrogation House alongside Zorbog. Carries a pass-amulet to Kolat Towers. See the **Avareen Windrivver** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:28`
> Adventure: "Their names are Avareen Windrivver (LE female Illuskan human {@creature spy}) and Zorbog Jyarkoth (NE male Turami human {@creature thug})." — `sources/adventure-wdh.json:7202` (Grep; the sentence opens "This windowless house is occupied by two Zhents loyal to {@creature Manshoon|WDH}-the same individuals that Sora describes.")

> "- **Zorbog Jyarkoth** — Human thug (Zhentarim), neutral evil. Thug, Avareen's partner at the Interrogation House. See the **Zorbog Jyarkoth** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:29`

> "- **Amath Seccent** — Human priest of Bane, lawful evil. Banite priestess occupying Yellowspire, allied with Manshoon. Friends with Agorn Fuoco, who visits when he wants company. See the **Amath Seccent** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:30`
> Adventure: "Amath Sercent (LE female Mulan {@creature priest}) and her four followers (LE male and female {@creature acolyte||acolytes} of mixed ethnicities) dress in common clothing when outside the tower." — `sources/adventure-wdh.json:9748` (Grep). Also (bundle `adventure-hits.txt`, line 9741): "The characters have learned that the {@item Stone of Golorr|WDH} is with Amath Sercent, a priest of Bane who is allied with {@creature Manshoon|WDH}. She and her acolytes reside in Yellowspire, a Castle Ward tower so named because its bricks have a pale yellow tinge to them."

> "- **Vira Solkan** — Human mage (Manshoon plant), neutral evil. See the **Vira Solkan** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:31`. No adventure counterpart (Grep "Vira" in `adventure-wdh.json` returned none).

> "- **Manafret Cherryport** — Lightfoot halfling mage (Kolat Towers cook), neutral evil. See the **Manafret Cherryport** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:32`
> Adventure: "The halfling, {@creature Manafret Cherryport|wdh}, is one of {@creature Manshoon|WDH}'s lieutenants. He loves to cook, and uses his mage hand cantrip to cut vegetables." — `sources/adventure-wdh.json:28191` (bundle `adventure-hits.txt`)

> "- **Kaevja Cynavern** — Human mage, lawful neutral. See the **Kaevja Cynavern** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:33`
> Adventure: "{@creature Kaevja Cynavern|wdh} is a female Mulan human {@creature mage}, with these changes:" — `sources/adventure-wdh.json:29994`; "Kaevja is lawful evil. She knows Common, Draconic, Dwarvish, and Elvish." — `sources/adventure-wdh.json:29998` (Read/Grep)

> "- **Havia Quickknife** — Lightfoot halfling adept, lawful evil. See the **Havia Quickknife** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:34`

> "- **Mookie Plush** — Lightfoot halfling adept, lawful evil. See the **Mookie Plush** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:35`
> Adventure: "Two female lightfoot halflings—{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush}—believe that {@creature Manshoon|WDH} is the rightful leader of the Zhentarim. They serve him fearlessly, and will sacrifice themselves to ensure that his plans come to fruition." — `sources/adventure-wdh.json:30183` (bundle `adventure-hits.txt`)

> "- **Yorn the Terror** — Human enforcer, neutral evil. See the **Yorn the Terror** page in Notable Figures."
> — `organizations/09-manshoons-zhentarim.md:36`
> Adventure: "{@creature Yorn|wdh} is a half-orc {@creature thug}, with these changes:" — `sources/adventure-wdh.json:28340`; "{@creature Yorn|WDH} is neutral evil." — `sources/adventure-wdh.json:28344` (Grep)

**Splinter members in the adventure that the campaign's org list omits**

> "{@creature Samara Strongbones|WDH}, a female lightfoot halfling, is a Zhentarim spy in league with {@creature Manshoon|WDH}. She is chaotic evil and has these racial traits: She is Small, and her walking speed is 25 feet. She can move through the space of any Medium or larger creature. She has advantage on saving throws against being {@condition frightened}. She speaks Common, Halfling, and Undercommon."
> — `sources/adventure-wdh.json:17230` (bundle `adventure-hits.txt`). She is captive "D" in the list at `:17222-17230`, a Xanathar's Lair prisoner. Campaign: "Samara, a prisoner in **Xanathar's Lair**, says Manshoon's organization is based in a tower in the North Ward." — `campaign/gazetteer/waterdeep/north-ward.md:42` (Grep). Campaign has no "Strongbones" (Grep in `campaign/`).

> "The three wizards here are {@creature Manshoon|WDH}'s apprentices—Ered Payno (LE male Damaran human), Havi Termock (CE female Chondathan human), and Savara Firethorn (NE female Tethyrian human). Each wears a teleporter ring (see \"Teleporter Rings\")."
> — `sources/adventure-wdh.json:28552` (bundle `adventure-hits.txt`); also `:28377`: "The Kolat brothers once took on apprentices, who slept here. {@creature Manshoon|WDH} now allows his own apprentices—Ered Payno, Havi Termock, and Savara Firethorn—to do the same." Campaign: no mention (Grep in `campaign/`).

### 4f. Cassalanters

> "| The Cassalanters | Missed opportunity | Their infernal connections could have been leveraged; Manshoon chose independence over shared control |"
> — existing page line 35

> "| **Manshoon vs. Cassalanters** | Mutual distrust — no contact | Seffia Naelryke approached Vevette Blackwater to open a communication channel. Vevette refused, suspecting a trap. No further contact from either side. | *Seffia Naelryke's Visiting Card* (Vevette Blackwater) |"
> — `campaign/guides/gm-guide/running-the-villains.md:74` (Grep)

- The published adventure has no Manshoon–Cassalanter contact except the all-three attack at `sources/adventure-wdh.json:14786` (quoted in 4b). Grep for "Seffia|Visiting Card" in the adventure returned only the Cassalanter cult passage (`:13219`: "Lord Cassalanter sent Arn and Seffia on a mission to retrieve the {@item Stone of Golorr|WDH} from his family's mausoleum.").

### 4g. The PCs

> "| The PCs | Escalating problem | Early: noise; mid-campaign: a problem to solve; first solution is always a job offer, not an assassination |"
> — existing page line 36

- Adventure support for the "job offer" approach: `sources/adventure-wdh.json:30256` and `26739` (section 3).
- Adventure support for capture: `sources/adventure-wdh.json:30409` (section 3).

---

## 5. Goals and methods: each row of the existing page

Status key: **Supported** (the adventure states it); **Partly supported**; **Campaign-only** (no published or Alexandrian source found); **Contradicted**.

**Phase table (existing page lines 17-19)**

| Existing row | Status | Sources |
|---|---|---|
| Line 17: `1 \| The Shadow \| Acts I–II \| Absent; only his lieutenants are visible; PCs fight "the Zhentarim" without knowing Manshoon is a distinct player` | **Partly supported.** Adventure: "{@creature Manshoon|WDH} takes great pains to conceal his identity" (`adventure-wdh.json:561`) and "he wants others to believe the site is abandoned" (`:26798`). The "Acts I–II" timing and the "the Zhentarim" street naming are campaign-only. | `:561`, `:26798` |
| Line 18: `2 \| The Architect \| Acts II–III \| Revealed; negotiates from strength; charming, precise, and calm about consequences in a way that should unsettle` | **Partly supported.** Negotiation: `:30256` ("convince ... that they can be cowed or bribed into working for him" — the sentence is quoted in full in section 3). "Charming, precise, calm" is not in the adventure. "Revealed" sits in tension with "The risk of exposure keeps him hidden" (`:26738`) unless "Revealed" means revealed to the party. | `:26738`, `:30256`, `:30255` |
| Line 19: `3 \| The Simulacrum Problem \| **Kolat Towers** \| Cornered; the performance of calm drops; the simulacrum fights while the real Manshoon exits` | **Partly supported / contradicted.** The adventure has a retreat: "When all is said and done, {@creature Manshoon|WDH} is forced to retreat to his extradimensional sanctum." (`:26766`). It contradicts an in-sanctum copy-fight with the real one leaving: "If a fight breaks out, {@creature Manshoon|WDH} grabs his {@item staff of power} (which he hides under the bed) and holds his ground." (`:30257`). "Simulacrum fights while real exits" is not in the adventure. See section 6. | `:26766`, `:30257` |

**Phase triggers (existing page lines 22-23)**

| Existing row | Status | Sources |
|---|---|---|
| Line 22: "Phase 1 → 2: PCs identify Manshoon specifically by name or signature, requiring at least two separate intelligence threads to connect" | **Campaign-only.** No phase concept in the adventure. Nearest: "The risk of exposure keeps him hidden, and the characters can thwart him by furnishing his enemies with proof that he's alive (after a fashion) and operating in Waterdeep." | `:26738` |
| Line 23: "Phase 2 → 3: PCs penetrate Kolat Towers or destroy a significant portion of his operation" | **Partly supported.** Adventure: "When it comes to {@creature Manshoon|WDH} clones ..." is not used; the relevant line is `:561`, "only those who enter his extradimensional sanctum are likely to incur his wrath." The "Disrupting Manshoon's Operation" list (`:26747` onward) gives barlgura release, reporting, and spellbook theft as ways to hinder him. | `:561`, `:26747` |

**Goals (existing page lines 40-42)**

| Existing row | Status | Sources |
|---|---|---|
| Line 40, Goal 1: "**Acquire the Stone of Golorr** — the Stone is a transformed aboleth encoded with ancient Weave knowledge; Manshoon means to absorb the Weave and supplant Mystra; the vault's gold funds the process; method: Stone recovery → Weave absorption; holds no Eye — Xanathar killed the envoys who delivered Eye #1 as a gift and kept it; needs the Stone plus any two Eyes; contingency: destroy the vault rather than cede it; connects to **Gralhund Villa** and **Kolat Towers**" | **Partly supported (Stone and vault); campaign-only (Weave, Mystra, Eyes, "destroy the vault").** Supported: the Stone is "actually an aboleth transformed by magic" (`adventure-wdh.json:453`, bundle), and Manshoon will trade lives "for the {@item Stone of Golorr|WDH} and the keys to unlock the Vault of Dragons" (`:26739`). Not in the adventure: any Weave knowledge in the Stone (the Stone's lore is "about Neverember's vault", `:453`); any Weave goal; any Eye (Grep for "three Eyes", "Eye of", "locket" returned no match in `adventure-wdh.json`). The Alexandrian p.15-16 has the Eye story, but not "as a gift" (C12). "Holds no Eye" is contradicted by the Alexandrian, printed p.96 (C12). | `:453`, `:26739`; `running-the-villains.md:30` (C12) |
| Line 41, Goal 2: "**Control Waterdeep's Underworld** — eliminate Xanathar, absorb the Doom Raiders, marginalize Bregan D'aerthe; method: patient erosion through targeted disruption and strategic violence; the Dock Ward conflict in Acts I–II is this plan in early operation" | **Partly supported.** Supported: "Those who support {@creature Manshoon|WDH} want to destroy {@creature Xanathar|WDH} and seize political and economic control of the city." (`adventure-wdh.json:1445`). "Absorb the Doom Raiders": the Doom Raiders driven out "yielding control of the Zhentarim in Waterdeep to {@creature Manshoon|WDH} (if he's alive)" (`:14893`). "Marginalize Bregan D'aerthe" and "the Dock Ward conflict" are campaign-only (`dock-ward.md:41`). | `:1445`, `:14893` |
| Line 42, Goal 3: "**The Simulacrum Insurance** — the simulacrum is not a backup; it is the primary survival strategy; defeating Manshoon in combat may defeat only his copy; connects to **Kolat Towers** design requirement" | **Partly supported.** The adventure calls it a subordinate: "he uses it as a subordinate to command his Zhentarim minions in the field" and "If his simulacrum is destroyed, {@creature Manshoon|WDH} creates another." (`bundle adventure.txt:32227`). "Primary survival strategy" is not in the adventure. The campaign calls it a "contingency against assassination" (`arc-i-kolat-towers.md:17`). Whether defeating the copy leaves the real one alive is section 6. | `bundle adventure.txt:32227`; `arc-i:17` |

**Key design note (line 44):** Not a factual claim. The campaign's own treatment differs: "The ambiguity is a puzzle, not a gotcha. The clues are present and discoverable." (`arc-i-kolat-towers.md:353`). See C6.

**Other rows (not in the phase or goal tables)**

- Line 25 (pop-culture inspirations) and line 9 (Purpose): not factual claims. Not checked.
- Line 31 (Urstul): "trusted with the Stone recovery at Gralhund Villa; his failure there is the first crack" — **Partly supported.** Adventure: the Stone "slip[ped] through his fingers" (`:30041`) and Urstul "is refusing to hand over the Stone of Golorr until he speaks to his secret master" (`:4379`). "Most effective operative" and "first crack" are campaign-only.
- Line 32 (Doom Raiders): "The clone peeled off their network and regards them as deserters; the two cells are at active war" — **Partly supported.** "Active war": the adventure says "Those who oppose {@creature Manshoon|WDH} want to expose and destroy him" (`:1445`). "Peeled off ... deserters" is Alexandrian p.16 ("When he peeled off a large hunk of the local Zhentarim network") and campaign (`history/04:86`: "It regards them as deserters who stole his name.").
- Line 33 (Xanathar): "Useful; the Guild's visibility keeps the Watch occupied; when the beholder becomes a direct obstacle, Manshoon has a plan" — **Partly supported.** Adventure: "Weary of his conflict with the Xanathar Guild" (`:30256`). "The Watch occupied" and "has a plan" are campaign-only.
- Line 34 (Jarlaxle): **Campaign-only** (section 4b).
- Line 35 (Cassalanters): "Missed opportunity" is **campaign-only**; see C20 for the secrecy-rule issue.
- Line 36 (PCs): **Partly supported** (section 4g).

---

## 6. The Phase 3 "Simulacrum Insurance" conflict

### 6a. The existing page (quoted)

> "| 3 | The Simulacrum Problem | **Kolat Towers** | Cornered; the performance of calm drops; the simulacrum fights while the real Manshoon exits |" — `campaign/setting/villains/manshoon.md:19`

> "3. **The Simulacrum Insurance** — the simulacrum is not a backup; it is the primary survival strategy; defeating Manshoon in combat may defeat only his copy; connects to **Kolat Towers** design requirement" — `manshoon.md:42`

> "**Key design note:** The simulacrum reveal needs to be timed carefully. Too early, and it deflates the Kolat Towers raid. Too late, and it feels like a cheat. Target: players discover it during the raid itself, as a revelation that changes how they approach the final confrontation." — `manshoon.md:44`

### 6b. Campaign lines on clone versus simulacrum

> "The man in Kolat Towers is a clone who believes he is the true Manshoon, and he keeps a simulacrum in reserve. The old outline asked whether he was the original or a simulacrum, and he is a third thing." — `campaign/setting/history/04-the-founding-of-chains.md:100` (Overview, GM Secret)

> "- Simulacra are a separate tool. Manshoon makes copies of himself with the simulacrum spell, and the copy in Kolat Towers has more hit points and less spellcasting than he does." — `history/04:48`

> "- **Conflicts:** Clones or simulacra. `history.md` line 38 says Manshoon \"died and was replaced by his own simulacra\". `notable-figures/manshoons-zhentarim/01-manshoon.md` line 23 and `organizations/09-manshoons-zhentarim.md` line 15 say clones, with simulacra as a separate tool. The clone wording wins." — `history/04:159`

> "- **Conflicts:** \"Original or simulacrum\" (`history.md` line 40) is stale. The man in the towers is a clone, and the open question is clone or simulacrum (E7; E12 or E13 by tier)." — `history/04:161`

> "His location is set by the escalation tier. At Unaware and Suspicious he is in E13, where his study is, and at Alert and Lockdown he is in E12. The activation of the simulacrum is linked to the same tiers." — `history/04:101`

> "The simulacrum in E7 is Manshoon's contingency against assassination. It was created seven years ago and has been ice-preserved since — a duplicate with half his hit points, none of his 6th-level or higher spell slots, and a different quality to its decision-making that those who know Manshoon well can identify after the fact. The simulacrum has never been activated outside of tests. Manshoon has never needed it. He is considering, for the first time in years, whether he might." — `campaign/structure/arc-i-kolat-towers.md:17`

> "He keeps a simulacrum in Kolat Towers while Manshoon watches from safer ground." — `organizations/09-manshoons-zhentarim.md:19`

> "Manshoon's combat priorities in order: the simulacrum as a shield (if present), wall of force to isolate the most dangerous party member, dominate person, and sustained concentration-based control rather than nova damage output." — `arc-i-kolat-towers.md:211`

> "- The simulacrum mechanic: Manshoon can create ice-preserved duplicates with limited capabilities." — `arc-i-kolat-towers.md:220` (list headed "*The Manshoon Identity Reveal.*" at line 213; the list items are at 217-221)

> "- Manshoon is a clone of a clone of the original Zhentarim founder, one of multiple surviving clone bodies." — `arc-i-kolat-towers.md:217`

### 6c. Campaign lines on the encounter sequence

> "Jarlaxle's position and the simulacrum's state are predecided by escalation tier. At Unaware and Suspicious, Manshoon is studying in E13 and the simulacrum is dormant in E7. At Alert and Lockdown, Manshoon is in E12 with the staff of power in hand and the simulacrum is activated and standing in E1. These positions do not change during Scene 4 unless the party's actions force Manshoon to move — and Manshoon moves toward a confrontation, not away from one." — `arc-i-kolat-towers.md:118`

> "| Unaware | Standard; gaps on normal rotation | Standard roster; Sidra assumes visitors are guests until credentials fail | Manshoon studying in E13; simulacrum dormant in E7 | 30 min |" — `arc-i:101`

> "| Alert | Gaps shifted 30 min; amulets require DC 14 Arcana to recalibrate | Posts doubled; K22 adds 2 thugs to standard spectator/snake garrison; Manafret poisons all kitchen food | Manshoon in E12, staff in hand; simulacrum activated in E1 as decoy | 20 min |" — `arc-i:103`

> "| Lockdown | Gaps sealed; only fresh amulets work; Yellowspire circle still functions | Full garrison at battle stations; Sidra does not ask questions | Manshoon in E12, defensive spells prepared; simulacrum activated in E1, briefed on party capabilities via Skeemo's intelligence if he survived **Faction Outposts** | 15 min |" — `arc-i:104`

> "The simulacrum's predecided positioning creates two structurally different encounter sequences depending on escalation tier. At Alert and Lockdown, the party encounters the simulacrum first in E1 — they may believe they have defeated Manshoon before they reach E12. At Unaware and Suspicious, the party reaches Manshoon first in E13 and may not discover the simulacrum in E7 until it activates behind them." — `arc-i:349`

> "Three discoverable clues let the party identify which version they fought: the simulacrum cannot cast 6th-level or higher spells (DC 15 Arcana to notice the pattern after observing its spell selection); the simulacrum has roughly half the hit points of the original (a party that tracked damage dealt will notice the fight ended faster than expected); and Lady Gondafrey, if freed, knows that Manshoon \"sometimes sends a quieter version of himself\" and can describe the behavioral difference after the fact." — `arc-i:351`

> "The ambiguity is a puzzle, not a gotcha. The clues are present and discoverable. A party that notices and investigates walks out of the sanctum knowing exactly what they fought. A party that does not notice and investigate may discover the answer in the **Vault of Dragons** confrontation instead — when they arrive at the Vault expecting a diminished Manshoon and encounter a full-strength one." — `arc-i:353`

> "- **Destroyed.** Both the original Manshoon and the simulacrum were eliminated during the raid." — `arc-i:259` (the bullet continues with the Splinter collapse and the Vault consequence)
> "- **Simulacrum Only.** The original Manshoon was destroyed but the simulacrum survived and escaped (or was not found)." — `arc-i:260` (the bullet continues: "The simulacrum has no 6th-level or higher spell slots and no staff of power.")
> "- **Alive.** Manshoon survived (escaped, negotiated, or was never reached)." — `arc-i:261` (the bullet continues: "He arrives at the Vault at full strength with surviving lieutenants and the staff of power.")

> "| Alert | Agorn or Vevette's team; orders are to capture, not kill |" — `campaign/guides/factions/10-manshoons-zhentarim.md:53` (no simulacrum at Alert)

> "| **Manshoon's Zhentarim** | Normal operations | Flying snake courier network active; Agorn Fuoco and Avareen Windrivver file field reports. Urstul Floxin reviews them | Agorn Fuoco or Vevette Blackwater's team; orders are to capture, not kill | Urstul Floxin's team if the others fail; Manshoon issues personal directives by flying snake. Manshoon's simulacrum engages; Sidra Romeir locks down Kolat Towers |" — `campaign/guides/gm-guide/running-the-villains.md:50` (simulacrum named only in the Lockdown column)

> "| Lockdown | Urstul's team if the others fail; Manshoon issues personal directives by flying snake. Manshoon's simulacrum engages; Sidra locks down Kolat Towers |" — `campaign/guides/factions/10-manshoons-zhentarim.md:54`

> "Tiers advance when a previous tier's response fails or when the faction's intelligence confirms the PCs are a serious threat." — `campaign/guides/gm-guide/running-the-villains.md:45`

### 6d. Published adventure

> "If the characters manage to overcome all these foes, they are free to explore the sanctum. {@creature Manshoon|WDH} awaits them in {@area E12|42e}." — `sources/adventure-wdh.json:29973` (Read)

> "\"The {@creature Manshoon simulacrum|wdh} (see {@area E7|420})\"" — `sources/adventure-wdh.json:29958` (Read; the entry is in the E2 "Alarm Responders" list)

> "When the simulacrum arrives, it passes itself off as {@creature Manshoon|WDH} as it welcomes the characters to its extradimensional sanctum. It offers a guided tour, gesturing for the characters to enter {@area E2|417} ahead of it. If they comply, it triggers the alarm in {@area E2|417} and attacks." — `sources/adventure-wdh.json:29910` (Read)

> "If it hasn't been summoned elsewhere, {@creature Manshoon|WDH}'s simulacrum (see {@adventure appendix B|WDH|12}) is standing before the glass wall with its back to the door. The simulacrum resembles a robed wizard with long black hair, pale skin, and an articulated metal left hand and forearm. Its face is concealed behind a steel mask that bears a smiling visage. The simulacrum attacks anyone it doesn't recognize." — `sources/adventure-wdh.json:30077` (Read)

> "This ice-carved container weighs 1,000 pounds and begins to melt if taken out of the room. The snow figure in the sarcophagus is part of the material component of a {@spell simulacrum} spell. {@creature Manshoon|WDH} can use it to create a new simulacrum if his current one is destroyed." — `sources/adventure-wdh.json:30104` (bundle `adventure-hits.txt`)

> "The handsome young figure is {@creature Manshoon|WDH} (see {@adventure appendix B|WDH|12}), who is much older than he looks." — `sources/adventure-wdh.json:30254` (Read)

> "If a fight breaks out, {@creature Manshoon|WDH} grabs his {@item staff of power} (which he hides under the bed) and holds his ground. For more information on how to play {@creature Manshoon|WDH}, see \"Facing {@creature Manshoon|WDH}\" at the beginning of this chapter." — `sources/adventure-wdh.json:30257` (Read)

> "When all is said and done, {@creature Manshoon|WDH} is forced to retreat to his extradimensional sanctum. From there, he continues his search for the Vault of Dragons while fending off attackers." — `sources/adventure-wdh.json:26766` (Read)

> "Manshoon can have only one simulacrum at any given time, and he uses it as a subordinate to command his Zhentarim minions in the field. If his simulacrum is destroyed, {@creature Manshoon|WDH} creates another. Each simulacrum has the statistics of {@creature Manshoon|WDH}, with these changes:" — `bundle adventure.txt:32227` (the sentence begins "{@creature Manshoon|WDH} can have only one simulacrum")

> "{@creature Manshoon|WDH} uses the {@spell simulacrum} spell to create a magical duplicate of himself as needed. He has customized the spell to increase {@creature Manshoon Simulacrum|wdh|his simulacrum}'s hit points at the expense of its spellcasting ability." — `bundle adventure.txt:32226`

> "- The simulacrum has no special equipment. Consequently, it has AC 12 and lacks the Magic Resistance trait and the Staff of Power action option." / "- It loses all spell slots of 6th level and higher." / "- It has a challenge rating of 8 (3,900 XP)." — `bundle adventure.txt:32231-32233`

> "The simulacrum has the same statistics as the character, but it has only half the character's hit point maximum and can't gain levels." — `sources/adventure-wdh.json:30410` (this is for a PC replacement, not Manshoon's own copy)

> "The simulacrum tirelessly pursues the stone, and characters who flee would do themselves well not to leave tracks in the snow." — `sources/adventure-wdh.json:9769` (bundle `adventure-hits.txt`)

### 6e. Alexandrian remix (transcribed from page images)

> "- The simulacrum: Manshoon runs at least one simulacrum. Defeating the simulacrum triggers the real Manshoon. Players may not realize which they fought until after the encounter." — `sources/SOURCE_GUIDE.md:363` (SOURCE_GUIDE's summary of `sources/12. Lair  Zhentarim – Kolat Towers.pdf`)

- **The PDF does not contain that sentence.** All five pages of `sources/12. Lair  Zhentarim – Kolat Towers.pdf` (printed pp.92-96) were read. None says a simulacrum's defeat triggers the real Manshoon. The word "simulacrum" appears only in the roster and the stat reference:
  - Printed p.94, adversary roster (transcribed): "Manshoon Simulacrum*" in the left column and "Area E7 – Simulacrum" in the middle column. The image does not confirm that these two sit on the same row.
  - Printed p.94, roster rows (transcribed): "Manshoon (01-50%)*", "Manshoon (51-90%)*", "Manshoon (91-00%)*" in the left column, and "Area E12 – Manshoon's Quarters", "Area E13 – Manshoon's Study", "On Business Elsewhere" in the middle column. The image does not let me confirm row alignment for these three.
  - Printed p.94: "* Has a teleporter signet ring."
  - Printed p.95, stat reference (transcribed): "Manshoon Simulacrum – DH p. 209" and "Manshoon – DH p. 209".
- Printed p.95 (transcribed): "Manshoon's lieutenants wear special rings that let them access Manshoon's sanctuary atop the Outer Tower (although they don't know that this is actually an extradimensional space; they think he just lives up there)."
- Printed p.92 (transcribed): "Although Manshoon lost the original Eye he had obtained, as Dragon Heist begins the Zhentarim seize possession of the Eye unwittingly carried by Renaer Neverember. This Eye is then immediately taken back to Kolat Towers and secured."
- `sources/1. The Villains.pdf`, printed p.16: no "simulacrum" or "deniability" in the Zhentarim section read. SOURCE_GUIDE line 135 says "Uses simulacrums for deniability." (C27)

### 6f. What each source says happens when the copy is defeated

| Source | What happens |
|---|---|
| Existing page (lines 19, 42) | The simulacrum "fights while the real Manshoon exits"; "defeating Manshoon in combat may defeat only his copy". |
| Campaign `organizations/09:19` | "He keeps a simulacrum in Kolat Towers while Manshoon watches from safer ground." |
| Campaign `arc-i:349` | At Alert and Lockdown the party meets the simulacrum first in E1: "they may believe they have defeated Manshoon before they reach E12." At Unaware and Suspicious they reach Manshoon first in E13. |
| Campaign `arc-i:211` | "the simulacrum as a shield (if present)" |
| Adventure `:26766` | After the siege, Manshoon "is forced to retreat to his extradimensional sanctum." |
| Adventure `:29910`, `:30077` | The E7 simulacrum passes itself off as Manshoon at E2 and attacks; in E7 it "attacks anyone it doesn't recognize." |
| Adventure `:29973`, `:30257` | The real Manshoon "awaits them in E12" and "holds his ground". |
| Adventure `bundle :32227` | "If his simulacrum is destroyed, Manshoon creates another." |
| SOURCE_GUIDE `:363` (not in PDF text) | "Defeating the simulacrum triggers the real Manshoon." |

### 6g. Options (facts only)

1. **Keep the page's wording (copy fights, real one exits).** Supported in part by `:26766` (retreat after the siege), `organizations/09:19`, and the SOURCE_GUIDE summary. Contradicted for an E12 fight by `:30257`. The adventure has no sequence in which the copy fights while the real Manshoon leaves.
2. **Follow the campaign's tier design (`arc-i:101-104, 118, 349`).** Decoy in E1 at Alert and Lockdown; real Manshoon in E13 (Unaware, Suspicious) or E12 (Alert, Lockdown). The campaign's own tier thresholds disagree (C4), and the adventure places the real Manshoon in E12 by default (`:29973`).
3. **Follow the adventure's roles (`bundle :32227`, `:29910`, `:30077`, `:30257`).** The copy is a field subordinate and E2/E7 guard; the real Manshoon is in E12 with the staff. Under this option the "fights while the real one exits" beat has no source.
4. **Use the Alexandrian percentile roll for the real Manshoon (printed p.94).** Rows read 01-50% (E12), 51-90% (E13), 91-00% (On Business Elsewhere). Row alignment is unconfirmed. The SOURCE_GUIDE's trigger sentence is not in the PDF.
5. **Clone or copy as the identity question.** Campaign: the man in the towers is a clone (`history/04:161`); the page's line 42 treats the copy as the thing that can be defeated. Adventure: the copy is "a magical duplicate of himself" made with the simulacrum spell (bundle `:32226`); the adventure does not raise a clone-or-copy question for the E12 man.

---

## 7. Lines on the existing page that say DM, flag, Arc, link by path, or name a ward

Grep for `DM` and `flag` (both cases) on `campaign/setting/villains/manshoon.md` returned no line. Grep for `arc` (any case), `Ward`, `.md`, `.pdf`, `.json`, `Chapter`, `retired` returned the lines below.

- **Line 11** (`> **The Two Zhentarims — GM Note:**`): "See also: GM Guide Session Zero; the **Organizations** pages." No path. Says "GM", not "DM".
- **Line 17** (`| 1 | The Shadow | Acts I–II |`): "Acts I–II". Not a ward.
- **Line 18** (`| 2 | The Architect | Acts II–III |`): "Acts II–III". Not a ward.
- **Line 31** (Urstul): "trusted with the Stone recovery at Gralhund Villa". Quest name, not a ward.
- **Line 40** (Goal 1): "connects to **Gralhund Villa** and **Kolat Towers**". Quest names.
- **Line 41** (Goal 2): "the Dock Ward conflict in Acts I–II is this plan in early operation". **Names a ward: Dock Ward.** The gazetteer agrees (`campaign/gazetteer/waterdeep/dock-ward.md:41`).
- **Line 50** (Source References): "The retired Chapter 2 outline, Section 2". `campaign/structure/ch2-city-of-splendors.md` is listed as retired and "do not use" in CLAUDE.md. The page cites it.
- **Line 51** (`adventure-wdh.json` Ch.8): cites the Ch.8 Kolat Towers area. No ward.
- **Line 52** (`1. The Villains.pdf`): exists on disk as `sources/1. The Villains.pdf`.
- **Line 53** (`12. Lair Zhentarim Kolat Towers.pdf`): the file on disk is `sources/12. Lair  Zhentarim – Kolat Towers.pdf` (double space, en dash). The citation as written does not match the file name.
- **Line 57** (link): `[Kolat Towers](../../structure/arc-i-kolat-towers.md)`. **Contains "arc" in a path.** Resolves to `campaign/structure/arc-i-kolat-towers.md` (exists). CLAUDE.md's "Quests, not arcs" applies to labels; the structure docs keep their `arc-*` slugs.
- **Line 58** (link): `[Notable Figures](../notable-figures/)`. Resolves to `campaign/setting/notable-figures/` (exists).
- **Line 59** (links): `[Running the Villains](../../guides/gm-guide/running-the-villains.md)`, `[Manshoon's Zhentarim](../../guides/factions/10-manshoons-zhentarim.md)`, `[Manshoon's Zhentarim](../organizations/09-manshoons-zhentarim.md)`. All three resolve (checked with Grep and Read in this pass).
- **Lines 9, 19, 22-23, 25, 32-36, 42, 44**: "Kolat Towers" appears with no ward attached. Line 19 has "**Kolat Towers**" in the Phase 3 "When active" cell.

No "Arc X" label appears on the page. The only "arc" is in the path on line 57.

---

## 8. Open conflicts (paired quotes; higher-ranked source noted)

**C1. Ward of Kolat Towers (settled in campaign)**
> "This dilapidated, two-towered edifice stands tall in the Southern Ward." — `sources/adventure-wdh.json:26797`
> "{@creature Manshoon|WDH} lurks in Kolat Towers, a pair of wizards' towers in the Trades Ward." — `sources/adventure-wdh.json:560`
> Campaign ruling: "The campaign follows the Southern Ward" — `history/04:162`. Higher-ranked: campaign ruling (Southern Ward). Stale campaign text still says Trades: "Kolat Towers (Manshoon's fortress) occupies a fortified block here" — `campaign/structure/ch2-city-of-splendors.md:37` (retired file; do not use).

**C2. Clone or simulacrum (existing page vs campaign)**
> "a simulacrum in Kolat Towers" — `organizations/09:19`; existing page line 42: "defeating Manshoon in combat may defeat only his copy"
> "The man in the towers is a clone, and the open question is clone or simulacrum (E7; E12 or E13 by tier)." — `history/04:161`
> Higher-ranked: the campaign's clone ruling (`history/04:159`: "The clone wording wins."). The page's "real Manshoon" in line 19 presupposes the man in the towers is the real one. The adventure makes no clone-or-copy statement for the E12 man.

**C3. Simulacrum hit points (campaign vs adventure)**
> "a duplicate with half his hit points" — `arc-i-kolat-towers.md:17`
> "the simulacrum has roughly half the hit points of the original" — `arc-i:351`
> "the copy in Kolat Towers has more hit points and less spellcasting than he does." — `history/04:48`
> "He has customized the spell to increase {@creature Manshoon Simulacrum|wdh|his simulacrum}'s hit points at the expense of its spellcasting ability." — bundle `adventure.txt:32226`
> Higher-ranked: adventure (published) under the ranking rule; the campaign has its own rule for the raid. Orchestrator decides. The half-maximum line at `:30410` is for a PC replacement, not Manshoon's copy.

**C4. Simulacrum activation tier**
> "| Alert | ... | Manshoon in E12, staff in hand; simulacrum activated in E1 as decoy | 20 min |" — `arc-i:103`
> "| Alert | Agorn or Vevette's team; orders are to capture, not kill |" — `factions/10:53` (no simulacrum at Alert)
> "Manshoon's simulacrum engages" in the Lockdown column only — `factions/10:54`; `running-the-villains.md:50`
> Higher-ranked: `arc-i` for the raid; `running-the-villains` and `factions/10` for the escalation tiers. Unresolved.

**C5. Manshoon's default location**
> "At Unaware and Suspicious he is in E13, where his study is, and at Alert and Lockdown he is in E12." — `history/04:101`
> "Manshoon studying in E13; simulacrum dormant in E7" — `arc-i:101`
> "{@creature Manshoon|WDH} awaits them in {@area E12|42e}." — `sources/adventure-wdh.json:29973`
> Alexandrian roll: "Manshoon (01-50%)*" beside "Area E12 – Manshoon's Quarters" (printed p.94; row alignment unconfirmed).
> Higher-ranked: campaign tier design. The adventure's default is E12, with no tier scheme.

**C6. Fight behaviour at the copy's defeat (existing page vs adventure)**
> "the simulacrum fights while the real Manshoon exits" — `manshoon.md:19`
> "If a fight breaks out, {@creature Manshoon|WDH} grabs his {@item staff of power} (which he hides under the bed) and holds his ground." — `sources/adventure-wdh.json:30257`
> "Defeating the simulacrum triggers the real Manshoon." — `SOURCE_GUIDE.md:363` (not in the PDF text)
> Higher-ranked: adventure (`:30257`). The SOURCE_GUIDE line is a summary the PDF does not support.

**C7. Replacement of a destroyed copy (not reflected in campaign)**
> "If his simulacrum is destroyed, {@creature Manshoon|WDH} creates another." — bundle `adventure.txt:32227`
> "Both the original Manshoon and the simulacrum were eliminated during the raid." — `arc-i:259` (the Faction State gives no replacement mechanic)
> Higher-ranked: adventure. The campaign's "Destroyed" state does not discuss replacement.

**C8. Undermountain clone's fate**
> "The one in Undermountain appeared to have died during the events of the [[Spellplague]] itself." — `wiki.txt:108`
> "The one presently in Waterdeep escaped death by hiding out in Undermountain, where he eventually ran afoul of Halaster Blackcloak." — bundle `adventure.txt:32217`
> "The clone was activated in Undermountain and subsequently fled." — `arc-i:218`
> Higher-ranked: adventure and campaign agree; the wiki is the outlier. Campaign note: `history/04:160` ("The published adventure wins").

**C9. Arm severed: where and how**
> "Halaster Blackcloak, who tolerated the clone for a time out of professional curiosity, eventually severed Manshoon's left arm at the shoulder with a blade that prevented magical regrowth." — `arc-i:13`
> "After a brief spell duel, Halaster captured {@creature Manshoon|WDH} and amputated his left arm at the elbow for reasons unknown." — bundle `adventure.txt:32217`
> "The clone challenged Halaster to a spell duel and lost more than just the contest." — `adventure-wdmm.json:26133`
> "while the original was kept and reanimated by Halaster." — `wiki.txt:125`
> "Halaster Blackcloak captured him and took his left arm, the regrowth failed, and he wears an artificial arm and hand." — `history/04:47`
> Campaign note: "This page says only \"left arm\"." — `history/04:167`. Orchestrator decides on shoulder versus elbow.

**C10. Founder or one of the founders**
> "The published adventure calls Manshoon \"one of the founders\" of the Zhentarim. This page follows the wiki and treats him as the founder." — `history/04:33`
> "one of the founders of the Zhentarim" — `adventure-wdh.json:560`
> "was the founder of the [[Zhentarim]]" — `wiki.txt:70`
> Campaign ruling: "The villain page governs." — `history/04:171`. The villain page does not address founder status.

**C11. Doom Raiders arrival and direction of the split**
> "came to Waterdeep three years ago with plans to establish a Zhentarim foothold in the city." — `sources/adventure-wdh.json:31916`
> "- They were sent to Waterdeep in 1489 DR to establish a Zhentarim foothold." — `history/04:57`
> "The sources reverse that direction: the cell came first, and Manshoon's clone peeled off its network." — `history/04:64`
> "- **Conflicts:** Direction of the split. `history.md` line 39 has Davil's cell separating from Manshoon." — `history/04:158` (Draft Notes; the bullet continues with the campaign files that agree with the newer direction)
> Higher-ranked: campaign (`org06:25`; `org09:13`). The adventure is silent on which came first (`:1445-1446`).

**C12. Eyes and the Stone**
> "holds no Eye — Xanathar killed the envoys who delivered Eye #1 as a gift and kept it" — `manshoon.md:40`
> "Manshoon holds no Eye." — `campaign/guides/gm-guide/running-the-villains.md:30`
> "Then the Zhentarim came to him with one of the Eyes and said, 'We have two different parts of this puzzle. We'd like to make a deal.' Xanathar was enraged at both their presumption and his own folly, slew the Zhentarim envoys, and took the Eye they had brought to him." — `1. The Villains.pdf` printed p.15 (transcribed)
> "He already has one. He once had another that was stolen by Xanathar." — `12. Lair ... .pdf` printed p.96 (transcribed)
> "This Eye is then immediately taken back to Kolat Towers and secured." — printed p.92 (transcribed)
> "Inside the Astral Vault: The vault contains the Eye, 5 pass-amulets, a dozen teleporter signet rings, and Manshoon's Report on the Grand Game (see Part 6D)." — printed p.94 (transcribed)
> Campaign ruling: "Kolat Towers holds no Eye." — `history/04:166`
> Higher-ranked: campaign ruling (`history/04:166`). The page's "as a gift" is in no source read; the Alexandrian says the envoys "came to him with one of the Eyes."

**C13. The third Eye (outside Manshoon's page, affects his goals)**
> "And he has recently identified that a local noble family has the third. (They don't know the identity of the noble family.)" — `12. Lair ... .pdf` printed p.96 (transcribed)
> "That the Cassalanters are the noble family who possess the third Eye." — printed p.96 (transcribed; the lieutenants' knowledge)
> "Three Eyes of the Stone of Golorr are already held when the campaign opens. Xanathar has Eye #1, the Cassalanters have Eye #2 and Jarlaxle has Eye #3." — `history/08:25`
> Higher-ranked: campaign (`history/08:25`). The Alexandrian gives the Cassalanters a different route to the Eye (printed p.18, transcribed).

**C14. Manshoon's goals: Weave versus rule-the-city**
> "Manshoon intends to use that knowledge to absorb the Weave and supplant Mystra." — `organizations/09:15`
> "{@creature Manshoon|WDH} aims to rule Waterdeep and replace the City Watch with Black Network mercenaries that are loyal to him alone." — bundle `adventure.txt:32219`
> "The published adventure gives him a different goal: to oust the Open Lord, replace the City Watch with Black Network mercenaries, and then turn on Halaster. The campaign keeps the Weave goal, which is set out on the **Manshoon** villain page." — `history/04:78`
> "Its goals (rule the city, oust the Open Lord, destroy Halaster) differ from `villains/manshoon.md` lines 40-42. The villain page governs." — `history/04:171`
> Higher-ranked: campaign ruling (the villain page governs). The adventure has no Weave goal.

**C15. Vevette Blackwater's alignment**
> "- **Vevette Blackwater** (DH p. 216) — Human swashbuckler, lawful evil." — `organizations/09:25`
> "Vevette Blackwater (CE female Tethyrian human {@creature swashbuckler|VGM}; see {@adventure appendix B|WDH|12})" — `sources/adventure-wdh.json:30120`
> Alexandrian p.95 (transcribed): "Vevette Blackwater (CE female Tethyrian human) – swashbuckler, DH p. 216"
> Higher-ranked: the adventure gives the stat facts; the campaign file is the setting reference. Orchestrator decides.

**C16. Amath's spelling, ethnicity and alignment**
> "- **Amath Seccent** — Human priest of Bane, lawful evil." — `organizations/09:30`
> "Amath Sercent (LE female Mulan {@creature priest})" — `sources/adventure-wdh.json:9748`
> Campaign page name: `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-seccent.md:1` ("# Amath Seccent"). The adventure's "Sercent" appears at `:61` (in a list) and `:9741`.
> Higher-ranked: campaign file for the name; the adventure for the stat facts. Orchestrator decides.

**C17. Kaevja Cynavern's ethnicity and alignment**
> "- **Kaevja Cynavern** — Human mage, lawful neutral." — `organizations/09:33`
> "{@creature Kaevja Cynavern|wdh} is a female Mulan human {@creature mage}, with these changes:" and "Kaevja is lawful evil." — `sources/adventure-wdh.json:29994`, `:29998`
> Alexandrian p.95 (transcribed): "Kaevja Cynavern (female Mulan human) – mage, MM p. 347; see DH p. 158"

**C18. Yorn the Terror's race and role**
> "- **Yorn the Terror** — Human enforcer, neutral evil." — `organizations/09:36`
> "{@creature Yorn|wdh} is a half-orc {@creature thug}, with these changes:" — `sources/adventure-wdh.json:28340`
> Alexandrian p.95 (transcribed): "Yorn the Terror – half-orc thug, MM p. 350; see DH p. 150"
> Higher-ranked: campaign file for the role; adventure for the race. Orchestrator decides.

**C19. Duhlark's death place; Alcedor's death**
> "Duhlark survived him by nine years before being found dead in his study, apparently of old age, with the force field still running." — `arc-i:9`
> "found Duhlark Kolat's skeletal remains in the bed" — `sources/adventure-wdh.json:28680`
> "His body rested in a secret bedroom at the top of the taller tower." — `wiki.txt:1979`
> "He died in the towers in 1385 DR under circumstances that remain unclear." — `arc-i:9`
> "Alcedor left the towers, never to be heard from again" — `sources/adventure-wdh.json:26865`
> Campaign note: "The campaign wins." — `history/04:170`

**C20. Cassalanter infernal knowledge (secrecy rule)**
> "| The Cassalanters | Missed opportunity | Their infernal connections could have been leveraged; Manshoon chose independence over shared control |" — `manshoon.md:35`
> CLAUDE.md, Cassalanter secrecy: "No faction or NPC outside the household and the cult knows about the Asmodean pact, the soul contract or the family's infernalism before the party discovers it; use suspicion, never knowledge. The one exception is Jarlaxle: he knows, through Vessa, his doppelganger spy in the Cassalanter social circle."
> Higher-ranked: the CLAUDE.md standing rule. Line 35 is a knowledge claim about the family's infernal connections. The page's wording may conflict with the rule. Orchestrator decides.

**C21. Kolat build date**
> "Before [[1368 DR]], the wizard brothers, [[Alcedor Kolat|Alcedor]] and [[Duhlark Kolat]], bought the buildings" — `wiki.txt:1969`
> "Kolat Towers was built in the late fourteenth century by the wizard brothers Duhlark and Alcedor Kolat." — `history/04:71`
> Campaign note: "The campaign dates stand." — `history/04:169`

**C22. Sanctum access**
> "Manshoon also had an extra-dimensional sanctum accessed via a ''[[teleportation circle]]'' inside the lower tower." — `wiki.txt:1977`
> "accessible only via a teleportation ring keyed to a specific circle in K22" — `arc-i:15`
> "a creature wearing a {@item teleporter ring|WDH} (see \"Teleporter Rings\"), can use this circle to access the teleportation circle in {@creature Manshoon|WDH}'s sanctum ({@area E1|413})." — `sources/adventure-wdh.json:28772` (bundle `adventure-hits.txt`)
> Higher-ranked: adventure and campaign agree on K22; the wiki differs and ranks last.

**C23. Sidra's role and the teleport rings**
> "Holds the teleport rings when lieutenants leave the Towers." — `organizations/09:24`
> "Since the force field around Kolat Towers keeps out riffraff, Sidra assumes the characters are guests of {@creature Manshoon|WDH} arriving for a clandestine meeting." — `sources/adventure-wdh.json:28155` (bundle `adventure-hits.txt`)
> No conflict identified. Noted for the drafter: the adventure gives Sidra no teleport-ring role in the lines read.

**C24. Fenerus (campaign directive vs adventure)**
> "ordering Zorbog to kidnap Fenerus Stormcastle of Quill Alley" — `factions/10:23`
> "The door to Fenerus's house stands open, and the place has been ransacked." — `sources/adventure-wdh.json:7114`
> "The characters' quest for the {@item Stone of Golorr|WDH} first leads them to Fenerus Stormcastle, a lamplighter who rents a small house in the Trades Ward ({@area L1|140})." — `sources/adventure-wdh.json:7087` (bundle `adventure-hits.txt`)
> Campaign: "a Bregan D'Aerthe cut-out and message-drop on Quill Alley" — `notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:26`. The ward of Quill Alley is not stated in either quote.

**C25. The "Zhentarim" in Undermountain and Skullport**
> "Bosskyn Gorrb, a blind tiefling {@creature spy}, leads the Zhentarim in Skullport and uses flying snakes to deliver messages to his underlings." — `sources/adventure-wdmm.json:63737`
> Campaign rule: "Two cells operate in Waterdeep." — `organizations/09:13`
> The WDMM does not say which Zhentarim cell this is. Unresolved.

**C26. Phase 3 trigger versus escalation tier**
> "Phase 2 → 3: PCs penetrate Kolat Towers or destroy a significant portion of his operation" — `manshoon.md:23`
> "Tiers advance when a previous tier's response fails or when the faction's intelligence confirms the PCs are a serious threat." — `running-the-villains.md:45`
> The page's trigger is a PC action; the escalation tier advances on response failure or intelligence. The simulacrum's activation tier is C4.

**C27. SOURCE_GUIDE summaries versus the Alexandrian PDF text**
> "Uses simulacrums for deniability." — `sources/SOURCE_GUIDE.md:135`
> "Defeating the simulacrum triggers the real Manshoon." — `sources/SOURCE_GUIDE.md:363`
> The Zhentarim section of `1. The Villains.pdf` (printed p.16) contains neither "simulacrum" nor "deniability". The Kolat PDF (printed pp.92-96) uses "simulacrum" only in the roster and stat reference (section 6e) and does not contain the triggering sentence. Both SOURCE_GUIDE lines are summaries the PDF text does not support.

**C28. "Underestimates non-magical threats" (campaign-only)**
> "Manshoon underestimates threats that aren't magical." — `running-the-villains.md:59`
> The adventure has no such line for Manshoon (Grep "underestimat" and "nonmagical" in `adventure-wdh.json`: the "nonmagical" hits are about items, e.g. `:30264`, "The mask on the table is nonmagical, but {@creature Manshoon|WDH} likes to put it on before meeting with his followers."). The wiki has none. Not a conflict, but the claim is in the GM guide and the faction guide, not the villain page.

---

## Not found

Searched, with no result (terms; files tried):

- **Weave or Mystra as Manshoon's aim:** `sources/adventure-wdh.json` (Grep "Weave|Mystra": only Laeral and Mystra lines, none attributed to Manshoon's plan); `wiki.txt` Manshoon page (no goal of this kind; "Weave" appears only for the Cormyr episode, `wiki.txt:112`).
- **Eyes of the Stone, "three Eyes", "locket", "Eye of":** `sources/adventure-wdh.json` (Grep, no match). The Eyes are campaign and Alexandrian material only.
- **"Splinter" as a name:** `sources/adventure-wdh.json`, `sources/adventure-wdmm.json`, `wiki.txt` (Grep, no match). Used by the campaign (`history/04:19`) and Alexandrian Act III Arc D (`sources/Act_III_Arc_D.md:251`).
- **"clone of a clone":** `adventure-wdh.json`, `adventure-wdmm.json`, `wiki.txt`, `sources/*.md` (Grep, no match). Campaign only.
- **"one true Manshoon":** `sources/adventure-wdh.json` (no match). Campaign and Alexandrian p.16 only.
- **"stasis" in the adventure:** no match. The stasis clone spell is in the wiki (`wiki.txt:89`, `wiki.txt:129`) and the campaign (`history/04:44`).
- **"underestimat", "deniab" for Manshoon:** `sources/adventure-wdh.json` and `wiki.txt` (Grep, no match). Campaign and SOURCE_GUIDE only (section 3).
- **Simulacrum in the wiki's Manshoon page:** Grep for "simulacrum" in `wiki.txt` returned no hit.
- **Phase names or triggers in the adventure:** Grep for "Phase [0-9]", "The Shadow", "The Architect", "Simulacrum Problem" in `adventure-wdh.json`: no match.
- **Manshoon's survival strategy in the adventure:** Grep for "survival" in `adventure-wdh.json` returns four lines (`:4815`, `:4841`, `:9115`, `:30256`); none describes a survival strategy for Manshoon. `:30256` is about the characters' survival.
- **Manshoon–Cassalanter contact (other than `:14786`):** Grep for "Seffia|Visiting Card" in the adventure returned only the cult passage at `:13219`. Campaign only (`running-the-villains.md:74`, `organizations/09:25`).
- **Manshoon–Jarlaxle non-interference arrangement:** no match in the adventure. Campaign only (`villains/jarlaxle.md:48`).
- **Manshoon's abduction directive against Fenerus:** no match in the adventure. Campaign only (`running-the-villains.md:75`, `factions/10:23`, `notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:26`).
- **Vira Solkan:** Grep "Vira" in `adventure-wdh.json`: no match. Campaign only (`organizations/09:31`, `notable-figures/manshoons-zhentarim/09-vira-solkan.md`).
- **Samara Strongbones surname or own page:** the adventure names her at `:17230`; "Strongbones" appears nowhere in `campaign/` (Grep).
- **Ered Payno, Havi Termock, Savara Firethorn (K15 apprentices):** adventure at `:28377` and `:28552`; no mention in `campaign/` (Grep).
- **Alexandrian p.16 on simulacra or deniability:** none in the printed p.16 (transcribed page).
- **Alexandrian text that a simulacrum's defeat triggers the real Manshoon:** not in `12. Lair ... .pdf` printed pp.92-96.
- **Villains PDF pages 19 onward:** not read in this pass. Manshoon is not expected there, but this is not confirmed.
- **Stone-and-Eyes count ("needs the Stone plus any two Eyes"):** not in the adventure; campaign only (page line 40).

## Not readable and caveats

- **`sources/research/pass4-bundles/manshoon/campaign-hits.txt`** (326 KB): not read in full (too large for one Read). Grep used. Every Manshoon claim was checked against the campaign file itself.
- **`sources/research/pass4-bundles/manshoon/wiki.txt`** lines 397-1929 (Zhentarim history and linked pages: Zhentil Keep, Mystra, Wizard, Harpers, Elminster, Laeral, Kyriani, Palace of Waterdeep, Spellplague, Undermountain, Halaster, Suzail, Mirt, Malchor Harpell, Mystra (Midnight)): searched with Grep for Manshoon, Waterdeep, Splinter, Kolat, Urstul, simulacrum, stasis, Halaster and Doom Raider. Relevant hits are quoted above (lines 402-435). Not read line by line.
- **`wiki.txt:1496-1576`** is a linked copy of the Manshoon page (first 5000 chars). It duplicates lines 1-70 and is not quoted separately.
- **PDFs:** the Read tool returns page images with no text layer. Every Alexandrian quote is transcribed from the image and must be checked against the PDF. Printed page numbers are given.
- **Adventure line numbers:** those marked "(bundle)" come from `sources/research/pass4-bundles/manshoon/adventure.txt` or `adventure-hits.txt`, which carry the JSON line numbers. Those marked "(Read)" or "(Grep)" were checked directly against `sources/adventure-wdh.json` or `sources/adventure-wdmm.json` in this pass.
- **Not checked:** the notable-figure profiles beyond the lines named above (Grep-level only), Appendices B-D beyond the Grep hits, `Act_III_Arc_E.md` beyond the Grep hits, and `docs/plans/`.
- **`.docx` files** in `sources/Other remix files/`: not searched; not in the Manshoon bundle, and the SOURCE_GUIDE does not name one for Manshoon in this pass.
