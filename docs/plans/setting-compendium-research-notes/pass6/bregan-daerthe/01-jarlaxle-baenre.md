# Pass 6 research notes: Jarlaxle Baenre

Page: `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Campaign-start lore only. Quest-time sentences are listed in section C and routed.
Model format: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/04-osvaldo-cassalanter.md`
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Captain Zardoz Zord (Jarlaxle's cover)" (line 7) and "### Jarlaxle Baenre" (line 26).
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/bregan-daerthe/02-soluun-xibrindas.md`

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. Tags such as `{@creature ...}` are left as written.
- Wiki: the scratchpad extract `wiki-bregan-daerthe/01-jarlaxle-baenre.txt` returned "NOT FOUND" (the file holds one line). The Jarlaxle wiki page was therefore read from `sources/research/pass5-bundles/bregan-daerthe/wiki.txt` lines 182-331, cited as "wiki bundle line N". The wiki gives citation keys (novels, *Waterdeep: Dragon Heist* 5e) and no edition for most lines. Wiki facts are tagged as wiki.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. These PDFs were read as page images, and every quote from them is a transcription. Check each with `pdftotext -layout` before any quote goes into prose:
  - `sources/1. The Villains.pdf`: the file has 7 PDF pages. Read: PDF pp.2-5 (printed pp.14-17). The Jarlaxle entry is printed p.17 (PDF p.5).
  - `sources/9. Lair – Sea Maidens Faire.pdf`: Read: PDF pp.1-8 (printed pp.68-75).
  - `sources/5. Faction Outposts.pdf`: Read: PDF pp.1-3 (printed pp.36-38).
- Not read: `sources/17. Outpost and Lair Revelation Lists.pdf`; the `.docx` files (see Not readable).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The public Persona names the link.** Line 21 says "To the world, Jarlaxle is Captain Zardoz Zord". The orchestrator's rule for this pass is that Zardoz Zord and J.B. Nevercott are separate public faces and that only the Villains page carries the link. Brief ruling 9 keeps J.B. Nevercott and Captain Zardoz Zord as two figures in the public Overview. The page's Overview (line 29) shows Zord only and does not name Nevercott. The Organization Overview (`07-bregan-daerthe.md:118`) shows both names.
2. **The Background has three GM-facing sources and no player-facing one.** Villains `## Background` (`villains/jarlaxle.md:41-61`), the History era page (`history/03-bregan-daerthes-long-road.md:22-62`) and the adventure entry (`sources/adventure-wdh.json:32178-32182`) all give the origin, the founding, Luskan and the Faire. The wiki adds the childhood, the brother who died in his place, the Zaknafein and Entreri history and named friends. All of these are wiki-only (section F). `deities/lolth.md:79` says the sacrifice is never revealed to players, so the Background stays in GM text.
3. **The Stone knowledge conflicts across sources.** The Alexandrian PDF says Jarlaxle is unaware at the start (printed p.17). The campaign says he has known since Marpenoth 3, 1491 DR (Session 47 ruling). The campaign governs (D1).
4. **Several facts conflict:** the submarine's mounting (adventure: under the Eyecatcher; campaign: moored in harbour until the fleet arrives), the nimblewright origin, the fleet's arrival date (Alexandrian: Ches 10 parade; campaign: Ches 21), and the stat block name "Swashbuckler (with modifications)", which no source other than this page gives (D2-D6).
5. **Morale (line 23) and Relationships (line 25) carry quest conditions** ("when the PCs kill his lieutenants", "if the party offers him something worth more than the gold"). Route them and restate Morale in day-one terms (C).

---

## A. Background facts by theme

### A1. Origin, birth and family

**Villains page, the origin (GM, the Background section)**
> "- Jarlaxle was born to Matron Mother Yvonnel Baenre of House Baenre, the first house of Menzoberranzan. By his birth order he was to be sacrificed to Lolth, but the blade could not pierce the infant and his brother Doquaio died in his place (Forgotten Realms Wiki; novel *Road of the Patriarch*)."
> — `campaign/setting/villains/jarlaxle.md:43`

**History page, the same facts with sourcing notes**
> "- Jarlaxle was born to Matron Mother Yvonnel Baenre of House Baenre, the first house of Menzoberranzan. He survived his sacrifice to Lolth and later rejected her. Bregan D'aerthe rejects her too, and its members speak of her with contempt."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:22`

> "- By his birth order he was to be sacrificed to Lolth. The blade could not pierce the infant, and his brother Doquaio Baenre died in his place. `[research: wiki only]`"
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:32`

> "- He is one of the few male drow with real power in Menzoberranzan, and his brother Gromph Baenre is the city's Archmage. `[research: wiki only]`"
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:35`

> "- A campaign docx calls him the third son, and the page keeps that. The wiki gives no number, but it calls Doquaio Yvonnel's second-oldest son and says Jarlaxle was slated for sacrifice because of his birth order, which implies at least a third son (Forgotten Realms Wiki, Jarlaxle Baenre; Road of the Patriarch)."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:36`

**Wiki bundle, the birth and the near-sacrifice (wiki, Road of the Patriarch; edition not stated)**
> "Jarlaxle was born to [[Yvonnel Baenre]], the [[matron mother]] of [[House Baenre]], the first house of Menzoberranzan. Due to the status of his birth order, Jarlaxle was to be sacrificed to [[Lolth]]. However, the sacrificial blade of Matron Baenre could not pierce the infant. Her second-oldest son, [[Doquaio Baenre]], was ordered to assist, but as he grabbed the infant, all of the kinetic energy of the attempted sacrifice was reflected on to him through the [[psionic]] power of the matron mother of [[House Oblodra]]. Doquaio was killed instead.<ref name=\"RotP-p290-291\">{{Cite book/Road of the Patriarch/MMP|290-291|19}}</ref><ref name=\"RotP-p296-297\">{{Cite book/Road of the Patriarch/MMP|296-297|20}}</ref> The failure of the sacrifice was kept secret, but Matron Baenre feared Jarlaxle from that time forward and believed that her fate was tied with his, while Jarlaxle was viewed as favored by the Spider Queen. Indeed, Lolth did favor him as an agent of chaos and granted him the memory of his near-sacrifice. However, he rejected her and she withdrew her favor, although the matron mothers of Menzoberranzan never learned of that fact.<ref name=\"RotP-p77\">{{Cite book/Road of the Patriarch/MMP|77|5}}</ref>"
> — wiki bundle line 277 (rest of the passage covers: Kimmuriel Oblodra's knowledge of the truth and House Oblodra's involvement)

**Wiki bundle, the infobox (wiki; the 5e row cites WDH p.206)**
> "| parents        = [[Yvonnel Baenre]]"
> — wiki bundle line 218

> "| siblings       = [[Gromph Baenre]]<br />[[Triel Baenre]]<br />[[Doquaio Baenre]]<br />[[Quenthel Baenre]]<br />[[Dantrag Baenre]]<br />[[Bladen'Kerst Baenre]]<br />[[Vendes Baenre]]<br />[[Sos'Umptu Baenre]]<br />[[Berg'inyon Baenre]]"
> — wiki bundle line 220

**Wiki bundle, youth (wiki; no campaign source)**
> "Jarlaxle attended [[Melee-Magthere]], the warriors' academy. He was recognized for his mastery of strategy and tactics and his strength was in the non-physical aspects of fighting, although he was a skilled swordsman as well. However, he favored a stealthy dagger over hand-to-hand combat.<ref name=\"RGLoD-p54-55\" />"
> — wiki bundle line 279

### A2. The rejection of Lolth

**Villains page (GM)**
> "- Lolth favored him afterward as an agent of chaos, and he rejected her. She withdrew her favor, and the matron mothers of Menzoberranzan never learned of it (Forgotten Realms Wiki; novel *Road of the Patriarch*)."
> — `campaign/setting/villains/jarlaxle.md:44`

> "- Bregan D'aerthe has rejected Lolth too. Its members speak of her with contempt, as the goddess they walked away from, and Soluun gives Jarlaxle the devotion that a drow of the houses would give the Spider Queen (campaign ruling; the **Soluun Xibrindas** page)."
> — `campaign/setting/villains/jarlaxle.md:45`

**Organization page**
> "- **The Company Rejects Lolth:** Bregan D'aerthe has rejected Lolth as its goddess. No member worships her, keeps a shrine to her or invokes the Spider Queen with devotion, and members speak of her with contempt, as the goddess they walked away from. Soluun gives Jarlaxle the devotion that a drow of the houses would give her."
> — `campaign/setting/organizations/07-bregan-daerthe.md:46`

**Deities page, the never-reveal line (GM)**
> "> - **Never reveal:** That Captain Zardoz Zord is Jarlaxle. That Jarlaxle was marked for sacrifice to Lolth as an infant and rejected her. That Soluun's disownment is a cover story. A player who asks a company member about Lolth gets contempt and nothing about where the company comes from."
> — `campaign/setting/deities/lolth.md:79`

### A3. The founding of Bregan D'aerthe

**Villains page**
> "- He left his house and name, though not his connections, and founded the company from the rogue males of destroyed and disgraced houses (Forgotten Realms Wiki, novel *Homeland*; published adventure). Almost all members are male, because female drow rarely take orders from a male, and a female drow can earn a place by decrying the matriarchy and convincing him she would be an asset (**Bregan D'aerthe's Long Road**)."
> — `campaign/setting/villains/jarlaxle.md:46`

**Adventure, the company's origin (faction box)**
> "Bregan D'aerthe is a company of mercenaries originally made up of the much-derided and dishonorable castaways of destroyed drow houses. The group's leader, {@creature Jarlaxle Baenre|WDH}, is always looking for new members to fill the ranks, and loyalty is what matters to him most."
> — `sources/adventure-wdh.json:1297`

**Wiki bundle, the founding (wiki; edition not stated)**
> "Jarlaxle later left his house and his name (but not his connections) behind and founded [[Bregan D'aerthe]], a mercenary band of rogue males that grew to be very powerful. It could be said that the band forged its own underworld empire in Menzoberranzan. Bregan D'aerthe was present among the troops of Baenre during the fall of [[House Do'Urden]].<ref name=\"H\">{{Cite book/Homeland/MMP (1990)|?}}</ref>"
> — wiki bundle line 284

### A4. Luskan, the Lords' Alliance and the Sea Maidens Faire

**Villains page**
> "- Five High Captains rule Luskan. After 1485 DR they trade legally across the Sword Coast and are secretly under Jarlaxle's sway, and the published adventure has him declaring himself the city's secret lord (**Bregan D'aerthe's Long Road**; `sources/adventure-wdh.json` line 32178)."
> — `campaign/setting/villains/jarlaxle.md:48`

> "- His latest scheme is to legitimize Luskan by making it a member of the Lords' Alliance. The city's reputation has thwarted every earlier attempt, and the Alliance's leaders have voiced their opposition. He aims to persuade **Laeral Silverhand** to champion Luskan even if it costs the Alliance other members (`sources/adventure-wdh.json` line 32179)."
> — `campaign/setting/villains/jarlaxle.md:49`

> "- He also wants to oust Neverwinter and its lord, **Dagult Neverember**, from the Alliance. The published adventure calls Neverember his fiercest political opponent, and it has Jarlaxle wanting the dragonstaff of Ahghairon as leverage in his negotiations (`sources/adventure-wdh.json` lines 22941 and 549)."
> — `campaign/setting/villains/jarlaxle.md:50`

> "- The Sea Maidens Faire is a legitimate business he already owned before he turned to Waterdeep. It is a traveling carnival out of Luskan that tours the Sword Coast in three ships, the *Eyecatcher*, the *Heartbreaker* and the *Hellraiser*, and Captain Zardoz Zord is Jarlaxle in the magical guise of an Illuskan human. He spends most of his time aboard the *Eyecatcher* (`sources/adventure-wdh.json` line 32180; **Bregan D'aerthe's Long Road**)."
> — `campaign/setting/villains/jarlaxle.md:51`

**Adventure, the entry (appendix B, page 206)**
> "{@creature Jarlaxle Baenre|wdh|Jarlaxle} is a flamboyant, swashbuckling drow iconoclast. He leads a renegade drow faction called Bregan D'aerthe, made up of disenfranchised male drow, most of them culled from destroyed or disgraced houses. Gifted with a sharp mind, a sense of humor, puissant skill with a blade, and a wealth of useful magic items, Jarlaxle infiltrated the city of Luskan, brought a kind of order to its lawlessness, and declared himself its secret lord."
> — `sources/adventure-wdh.json:32178`

> "Jarlaxle has come to Waterdeep in the guise of an Illuskan human named Zardoz Zord. \"Captain Zord\" is the master of the Sea Maidens Faire, a carnival that travels up and down the Sword Coast in three ships: the {@i Eyecatcher}, the {@i Heartbreaker}, and the {@i Hellraiser} (all words that describe Jarlaxle). He spends most of his time aboard the {@i Eyecatcher}, his personal ship. The other two vessels carry members of the carnival and their parade wagons."
> — `sources/adventure-wdh.json:32180`

> "Jarlaxle's loyalties are to himself first and foremost, and to Bregan D'aerthe secondarily."
> — `sources/adventure-wdh.json:32182`

**Adventure, the entry in the faction box**
> "In the magical guise of a flamboyant Illuskan captain named Zardoz Zord, Jarlaxle oversees things from the {@i Eyecatcher}, his flagship, and the {@i Scarlet Marpenoth}, a submarine mounted underneath it. He relies on three {@creature Drow Gunslinger|wdh|drow gunslingers}—{@creature Fel'rekt Lafeen|WDH}, {@creature Krebbyg Masq'il'yr|WDH}, and {@creature Soluun Xibrindas|wdh}—to do most of his dirty work in the city. For more information on Jarlaxle and his lieutenants, see {@adventure appendix B|WDH|12}."
> — `sources/adventure-wdh.json:1300`

**Wiki bundle, Luskan (wiki; the TPK novel; the Deudermont death is wiki-only)**
> "Over [[1376]] to [[1377 DR]], Jarlaxle and Bregan D'aerthe manipulated events in [[Luskan]] that resulted in the destruction of the [[Host Tower of the Arcane]], the death of [[Deudermont]], and Luskan becoming a free port. Jarlaxle allowed [[Regis]] and Drizzt to live and also took a [[scrimshaw]] piece from Regis that depicted Drizzt and [[Guenhwyvar]], rather than taking the valuable ''[[ruby pendant]]''.<ref name=\"TPK\">{{Cite book/The Pirate King|?}}</ref>"
> — wiki bundle line 304

### A5. Arrival in Waterdeep and what he knew

**Villains page, activation (GM Notes)**
> "- **Villain activation.** Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep, no later than Marpenoth 3, 1491 DR. He enters the Grand Game as a named player when the **Jarlaxle Informed** Event Outcome is marked during **Fireball!** and read in **Gralhund Villa**."
> — `campaign/setting/villains/jarlaxle.md:23`

**Villains page, the Relationships (Background bullet)**
> "- He reached Waterdeep already knowing of the Stone, the three Eyes and the vault, and Nar'l's reports keep him current. The nimblewright ledger puts him in the city no later than Marpenoth 3, 1491 DR (**Bregan D'aerthe's Long Road**)."
> — `campaign/setting/villains/jarlaxle.md:55`

**Organization page, the arrival (History)**
> "- **Marpenoth 3, 1491 DR, the arrival in Waterdeep:** Jarlaxle was in the city no later than this date, because the first nimblewright in his sale ledger went out then. He arrived in the city to advance Luskan's bid to join the Lords' Alliance, and he came prepared with nimblewrights, which he sells to wealthy families across every ward and each of which harvests intelligence through a crystal ball aboard the *Scarlet Marpenoth*. The ledger sells NW-02 to O. Gralhund of Saerdoun Street on Marpenoth 7, and the year is derived. The Sea Maidens Faire is a legitimate business he already owned, and it tours the Sword Coast in three ships. Campaign change: the published adventure has him arrive unaware of the Stone, and the campaign has him know of the Stone, the Eyes and the vault from the day he reached the city (user ruling, Session 47)."
> — `campaign/setting/organizations/07-bregan-daerthe.md:29`

**Alexandrian, the start state (PDF transcription, printed p.17 = `sources/1. The Villains.pdf` PDF p.5)**
> "As *Dragon Heist* begins, Jarlaxle is unaware of the *Stone of Golorr* or the Grand Game which is being played. Freshly arrived in his cover identity as Captain Zord of the Sea Maiden's Faire, Jarlaxle is coordinating and ramping up his local intelligence operations."
> — `sources/1. The Villains.pdf` printed p.17 (transcription; the campaign overrules it, see D1)

### A6. The fleet, the submarine and the Faire's cover

**Adventure, the submarine and the escape plan**
> "Jarlaxle has forged an alliance with Lantan (an island to the south), and has armed his Bregan D'aerthe lieutenants with Lantanese firearms that rely on magical {@item smokepowder|WDH} to function. He has also acquired a Lantanese submarine called the {@i Scarlet Marpenoth}. This underwater vessel is mounted below the {@i Eyecatcher} and kept out of sight. Jarlaxle plans on using the submarine to flee Waterdeep if his scheme unravels."
> — `sources/adventure-wdh.json:32181`

**Organization page, the company's history (1489 and 1491 DR)**
> "- **1489 and 1491 DR, the *Scarlet Marpenoth*:** Lantan built the submarine and launched it in 1489 DR, and Jarlaxle acquired it in 1491 DR (*Waterdeep: Dragon Heist*, 5e; Forgotten Realms Wiki, *Scarlet Marpenoth*, 5e). He has also forged an alliance with Lantan and armed his lieutenants with Lantanese firearms that run on smokepowder. Campaign change: the published adventure mounts the submarine below the *Eyecatcher*, and in the campaign it has been moored in Deepwater Harbor since he reached the city."
> — `campaign/setting/organizations/07-bregan-daerthe.md:28`

**Organization page, the Faire's fleet (Structure)**
> "**The *Scarlet Marpenoth*:** The submarine is a red, manta-shaped Lantanese vessel (Forgotten Realms Wiki, *Scarlet Marpenoth*, 5e). Drow gunslingers and gnome pilots and engineers crew it, and it keel-docks beneath the *Eyecatcher* when the fleet arrives. Jarlaxle keeps his stateroom aboard, and the crystal ball that serves the nimblewright network is aboard too."
> — `campaign/setting/organizations/07-bregan-daerthe.md:63`

**Villains page, the mooring and the nimblewright network**
> "- In the campaign the *Scarlet Marpenoth* has been moored in Deepwater Harbor since he reached the city, and it keel-docks beneath the *Eyecatcher* when the fleet arrives (the **Sea Maidens Faire** location journal, area overview)."
> — `campaign/setting/villains/jarlaxle.md:54`

> "- Zord sells nimblewrights to wealthy families across the wards, and each one harvests intelligence through a crystal ball aboard the *Scarlet Marpenoth* (**Bregan D'aerthe** page, Organizations)."
> — `campaign/setting/villains/jarlaxle.md:56`

**Alexandrian, the stateroom and the crystal ball (PDF transcription, printed p.73 = PDF p.7 of `sources/9. Lair – Sea Maidens Faire.pdf`)**
> "Area U4 – Jarlaxle's Stateroom: In addition to the normal entry for this area, a crystal ball sits upon a plush cushion of black velvet on a pedestal at the foot of the bed. This is the Nimblewright Crystal Ball (see Part 5)."
> — `sources/9. Lair – Sea Maidens Faire.pdf` printed p.73 (transcription)

**Adventure, the ship captains (page 132, "Ship Captains" entry)**
> "Although Zardoz Zord ({@creature Jarlaxle Baenre|WDH}) commands the fleet, each ship has its own captain: a Bregan D'aerthe {@creature drow mage} disguised as a slender, well-dressed human. These captains know of Jarlaxle's plans. They communicate with each other and with Jarlaxle by way of {@spell sending} spells, which they prepare instead of {@spell fly}."
> — `sources/adventure-wdh.json:23023`

**Adventure, the crew's knowledge of Zord (page 132, "Sailors" entry)**
> "The {@i Eyecatcher}, the {@i Heartbreaker}, and the {@i Hellraiser} are crewed by twenty sailors each: three {@creature drow elite warrior||drow elite warriors} (mates) and seventeen {@creature drow}, all magically disguised as slender humans while aboard their vessel. All are loyal members of Bregan D'aerthe, and all know that Zardoz Zord is {@creature Jarlaxle Baenre|WDH} in disguise. They know nothing about the {@i Scarlet Marpenoth} or Jarlaxle's plans."
> — `sources/adventure-wdh.json:23047` (see D11)

### A7. The locket Eye (Eye #3) and the company's hold on it

**Villains page (GM)**
> "- Eye #3 began in **Renaer Neverember**'s mourning locket. Manshoon's Zhentarim seized the locket the night before Ches 1 and pried it open at the Candle Lane warehouse. Xanathar's Guild raided the warehouse and carried off the Eye with the rest of the back office without knowing what it was, and Bregan D'aerthe agents already inside Xanathar's hideout lifted it that night. It reached Jarlaxle before the party reached the hideout, and Manshoon's cell never held it (**Running the Villains**; the **Xanathar Sewer Hideout** location journal, area overview). He keeps it in his stateroom, U4, aboard the *Scarlet Marpenoth* (the **Sea Maidens Faire** location journal, area overview)."
> — `campaign/setting/villains/jarlaxle.md:57` (the phrase "before the party reached the hideout" is quest-time wording; see C)

**Organization page, the night before Ches 1**
> "- **The night before Ches 1, 1492 DR, the company today:** Bregan D'aerthe agents inside Xanathar's hideout lift Eye #3, and it reaches Jarlaxle aboard the *Scarlet Marpenoth*. The Faire's fleet is due in Deepwater Harbor on Ches 21, the opening day of Fleetswake, and it sails at dawn on Tarsakh 20."
> — `campaign/setting/organizations/07-bregan-daerthe.md:31`

**Alexandrian, the locket (PDF transcription, printed p.16 = PDF p.4 of `sources/1. The Villains.pdf`; the locket is Renaer Neverember's, not Jarlaxle's)**
> "They were right, although Renaer didn't know it: His father had given him an elaborate, ivory mourning locket in honor of his mother. The Eye was hidden inside it."
> — `sources/1. The Villains.pdf` printed p.16 (transcription)

### A8. Named associates, as the campaign states them

**Villains page, Relationships (Background bullets)**
> "- **Nar'l Xibrindas** is Xanathar's trusted drow advisor and secretly Jarlaxle's best intelligence source on the Guild. He reports by *Sending* spell, and if forced to choose between himself and Bregan D'aerthe, he will choose himself (the **Nar'l Xibrindas** page)."
> — `campaign/setting/villains/jarlaxle.md:58`

> "- **Vessa**, a doppelganger, sits in the Cassalanter social circle under a permanent human cover. She is how Jarlaxle alone outside the household and the cult knows about the family's pact, and he does not tell Bregan D'aerthe members unless they work it out themselves (**A Debt in Blood**; the **Vessa** page)."
> — `campaign/setting/villains/jarlaxle.md:59`

> "- **Ryvarra** is a field observer at the Yawning Portal who catalogs Undermountain traffic for his Waterdeep network. She is the first sign that he had eyes on the party from their first night in the city (the **Ryvarra** page)."
> — `campaign/setting/villains/jarlaxle.md:60` (the last clause is quest-time wording; see C)

> "- His other names are GM names. J.B. Nevercott is the haberdasher who visits Trollskull Manor, Captain Zardoz Zord is the carnival master, and Rongquan Mystere is the Shou owner of the Seven Masks Theater, whom the **Sea Maidens Faire** structure document also has attending the Shipwright's Ball (`sources/adventure-wdh.json` lines 3601 and 9066; `campaign/structure/arc-h-sea-maidens-faire.md` line 79)."
> — `campaign/setting/villains/jarlaxle.md:61`

**Organization page, the Cassalanters**
> "- **The Cassalanters (neutral):** Jarlaxle alone outside the household and the cult knows about the family's pact, through Vessa, and he tells no company member unless they work it out. He has no interest in the family beyond what the intelligence is worth. Cassalanter imps keep watch on the Faire, and his counter-intelligence has not detected them (**Jarlaxle Baenre**)."
> — `campaign/setting/organizations/07-bregan-daerthe.md:92`

**Organization page, the lieutenants (Structure)**
> "**The lieutenants:** Fel'rekt Lafeen, Krebbyg Masq'il'yr and Soluun Xibrindas do most of Jarlaxle's dirty work in the city, and all three carry Lantanese firearms (*Waterdeep: Dragon Heist*, 5e)."
> — `campaign/setting/organizations/07-bregan-daerthe.md:55` (the rest of the paragraph covers the Faire's captains and the company's ranks)

**Wiki bundle, the co-leader (wiki only; Kimmuriel is not on any campaign page)**
> "Jarlaxle made an agreement with Kimmuriel for co-leadership of Bregan D'aerthe while Jarlaxle went traveling around the surface."
> — wiki bundle line 288 (rest of the paragraph covers the 1357 and 1364 DR Entreri dealings; see F)

### A9. Personality, as the sources describe it

**Persona, the page (line 21), quoted in full**
> "**Persona.** To the world, Jarlaxle is Captain Zardoz Zord, a flamboyant human sea captain running the Sea Maidens Faire carnival. To those he trusts, he is the secret lord of Luskan, the commander of Bregan D'aerthe, and a drow iconoclast whose loyalties run to himself first and his operatives second. Deep down, he likes to weave schemes that leave his enemies baffled, and the look on their faces when he gets the better of them is its own reward. The first thing he does with new contacts is determine whether they are useful or dangerous. Ideally, he discovers they are both."
> — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:21`

**Adventure, the villain profile (page 6, `sources/adventure-wdh.json:545-551`)**
> "Jarlaxle delights in thwarting his enemies, enjoys the complications that arise when adventurers try to meddle in his affairs, and loves to see the looks on their faces when he finally gets the better of them. He doesn't suffer fools who threaten him, however. If forced into a violent confrontation, he swiftly and brutally kills someone to make an example of them and then walks off."
> — `sources/adventure-wdh.json:550`

**Organization page, the performance (Structure)**
> "**Primary Contact:** Jarlaxle Baenre, operating in Waterdeep as the flamboyant Illuskan carnival master Zardoz Zord. He is always performing, and the performance is genuine, the act of a man who chose delight as a survival strategy and discovered it works. He gives compliments that are precise and earned, and he remembers everything you said three conversations ago. He is never threatened by capable people, and he collects them. The tell players should learn to watch for is that when Jarlaxle stops smiling, the situation has become genuinely serious."
> — `campaign/setting/organizations/07-bregan-daerthe.md:53`

**Wiki bundle, temperament (wiki; the citations name novels)**
> "He had a very charismatic personality, always willing to talk his way out of situations rather than resort to force of arms. Moreover, talking was what Jarlaxle did best. His words easily worked past the handicap of his race's evil reputation, able to turn potential enemies into allies. He loved irony, sarcasm, and wit. He was extremely intelligent and a brilliant tactician who was always prepared for any imaginable or unimaginable circumstances.<ref name=\"RGLoD-p54-55\"/>"
> — wiki bundle line 269

> "He found that he felt most alive when he was with friends and when he was taking risks.<ref name=\"TLT-p291\">{{Cite book/The Last Threshold/Hardcover|291}}</ref> He had an \"insatiable curiosity and a desire to know—everything.\"<ref name=\"RotK-p136\">{{Cite book/Rise of the King/Hardcover|136}}</ref> This curiosity made him antsy when he remained stuck in one place too long and drove his quest for personal exploration.<ref name=\"RotK-p72\">{{Cite book/Rise of the King/Hardcover|72}}</ref>"
> — wiki bundle line 267 (the same paragraph covers the Menzoberranzan years and the surface; the sentence "In his later years, he preferred to see adventure and profit in the World Above." is on line 267 as well)

### A10. Voice

The drafter copies the voice profile. Its lines are listed in section C (quest-time clauses) and section G (inner life). Voice line numbers:
- Zardoz Zord profile: heading line 7; the sample lines run to line 22.
- Jarlaxle profile: heading line 26; the sample lines run to line 40.

### A11. Aliases and the public faces

**Wiki bundle, aliases (wiki; the Zord alias is cited to WDH p.131)**
> "| aliases        = Jarlaxle Baenre<ref>{{Cite book/Servant of the Shard/Hardcover|348|Epilogue}}</ref><br/>Jarlaxle D'aerthe<ref name=\"PotWK-p53\">{{Cite book/Promise of the Witch-King/MMP (2006)|53|3}}</ref><br/>Catti<ref name=\"RotK-p280\">{{Cite book/Rise of the King/Hardcover|280}}</ref><br/>[[Zardoz Zord]]<ref name=\"WDH5e-p131\">{{Cite book/Waterdeep: Dragon Heist|131}}</ref>"
> — wiki bundle line 194

**Adventure, the cover name (appendix B entry, page 206)**
> "\"Captain Zord\" is the master of the Sea Maidens Faire, a carnival that travels up and down the Sword Coast in three ships: the {@i Eyecatcher}, the {@i Heartbreaker}, and the {@i Hellraiser} (all words that describe Jarlaxle)."
> — `sources/adventure-wdh.json:32180`

**Appendix B, the Nevercott visit (Faction Appendix)**
> "If the party reports the drow to the City Watch, Jarlaxle ends contact for now. If the characters attempt to confront the spies, they melt away and leave a black eye patch as a calling card. The next day, Jarlaxle himself appears at the party's headquarters disguised as a haberdasher named **J.B. Nevercott** — and makes his offer directly to any drow present."
> — `sources/Appendix_B_-_Player_Factions.md:719`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "- *Drow swashbuckler, chaotic neutral, he/him*. Stat block: **Swashbuckler (with modifications)**." — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:5`
- Campaign, the Organization page, Key Members: "- **Jarlaxle Baenre / "Zardoz Zord"** — Drow swashbuckler, chaotic neutral. Leader of Bregan D'aerthe; operates in Waterdeep as carnival master Zardoz Zord. See the **Jarlaxle Baenre** page in Notable Figures." — `campaign/setting/organizations/07-bregan-daerthe.md:99`
- Wiki bundle: "| alignment5e    = [[Chaotic neutral]]" (wiki bundle line 246; the 5e row cites WDH p.206). Older rows: "| alignment2e    = [[Neutral evil]]" (line 232), "| alignment3e    = [[Neutral evil]]" (line 235), "| alignment4e    = [[Evil]]" (line 243).
- Adventure: no alignment line for Jarlaxle was found (`sources/adventure-wdh.json:549`, `:32178`).

**Species**
- Campaign, the page: "Drow swashbuckler" (line 5).
- Wiki bundle: "| race           = [[Drow]]<ref name=\"SN-p94\" />" (line 201).
- Adventure: "{@creature Jarlaxle Baenre|WDH} is a drow swashbuckler and the secret lord of Luskan, the City of Sails." — `sources/adventure-wdh.json:549`
- Zord's cover: "an Illuskan human named Zardoz Zord" (`sources/adventure-wdh.json:32180`); "Illuskan human" also at `campaign/setting/villains/jarlaxle.md:51`. The cover species is not the real one.

**Pronouns**
- Campaign, the page: "he/him" (line 5). The Organization page's Key Members line (99) gives none.
- Adventure: "He doesn't suffer fools who threaten him, however." (`sources/adventure-wdh.json:550`)
- Wiki bundle: "| sex            = Male" (line 199).

**Stat block**
- Campaign, the page: "Stat block: **Swashbuckler (with modifications)**." (line 5). No other campaign file was found that names this stat block.
- Adventure: "drow swashbuckler" (`sources/adventure-wdh.json:549`). No "with modifications" wording for Jarlaxle was found in the adventure.
- Wiki bundle: "| class4e        = {{class table|edition=4e|Skirmisher|21}}" (line 244, 4e row); "| challenge5e    = 15" (line 247, 5e row, cites WDH p.206); "| class5e        = " (line 248, blank).
- The Appendix B entry gives no stat block name for Jarlaxle (`sources/adventure-wdh.json:32172`-`:32184`).

**Affiliation**
- Campaign, the page: "- **Affiliation:** Bregan D'aerthe" (line 6). Organization, Key Members line 99 (above).

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md`. The page has no Background, Personality or Connections section yet. Each row says whether the sentence is day-one, and where its fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "- *Drow swashbuckler, chaotic neutral, he/him*. Stat block: **Swashbuckler (with modifications)**." | Day-one. The stat block name has no source (B, D6) | Section B |
| 2 | L6 | "- **Affiliation:** Bregan D'aerthe" | Day-one | `07-bregan-daerthe.md:99` |
| 3 | L7 | "- **Featured in:** **Finding Floon**, **Trollskull Alley**, ... **A Friend's House**" | Quest references. The list omits the Trollskull First Meeting and other events the Villains page cites | `campaign/setting/villains/jarlaxle.md:10` |
| 4 | L11 | "**Resonance.** Jarlaxle should inspire delight with his theatrical flair and razor wit, unease with the realization that every conversation is a negotiation, and reluctant admiration for an opponent who prefers confused enemies to dead ones." | Day-one. The "confused enemies" half is sourced at `07-bregan-daerthe.md:36` ("Jarlaxle would rather leave an enemy confused than dead") | `07-bregan-daerthe.md:36` |
| 5 | L13 | "**Emotions.** Jarlaxle most often feels theatrical amusement, predatory curiosity, strategic calculation behind every smile, honest delight when a scheme comes together, contempt for fools who threaten him (swiftly expressed), and possessive loyalty to Bregan D'aerthe that he frames as pragmatism." | Day-one. Keep verbatim | `sources/adventure-wdh.json:550`; `villains/jarlaxle.md:39` |
| 6 | L15 | "**Motivations.** Jarlaxle wants to buy Luskan's way into the Lords' Alliance using the dragon hoard, acquire the dragonstaff of Ahghairon for leverage over Waterdeep, and ensure that if everything falls apart, the submarine is fueled and ready." | Day-one as a motive. "the dragon hoard" is the vault gold, which the campaign treats as known in the Grand Game from the start (`villains/jarlaxle.md:23`). "the submarine is fueled and ready" has no exact source; the adventure says only "Jarlaxle plans on using the submarine to flee Waterdeep if his scheme unravels." | `sources/adventure-wdh.json:549`; `:32181` |
| 7 | L17 | "**Inspirations.** When playing Jarlaxle, channel Jack Sparrow (*Pirates of the Caribbean*), Loki (*Marvel*), and Hector (*Westworld*)." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Jarlaxle is Captain Zardoz Zord, a flamboyant human sea captain running the Sea Maidens Faire carnival. To those he trusts, he is the secret lord of Luskan, ..." | "To the world, Jarlaxle is Captain Zardoz Zord" ties the public face to the real name, which only the Villains page should carry (D4). The rest is day-one (A9) | `sources/adventure-wdh.json:32178`, `:32180` |
| 9 | L23 | "**Morale.** In combat, Jarlaxle would swiftly and brutally kill someone to make an example, then propose terms. He reaches for leverage before force. If reduced to danger, he uses his wealth of magic items to escape. Direct confrontation only comes when the PCs kill his lieutenants without first offering terms." | Sentences 1 and 2 are day-one (`sources/adventure-wdh.json:550`; `:32178` for "a wealth of useful magic items"). Sentence 3 ("If reduced to danger ... to escape") has no exact source beyond "a wealth of useful magic items". The last sentence is quest-time: it is a condition on PC action. Its counterpart is `campaign/guides/factions/08-bregan-daerthe.md:124` ("Direct confrontation only comes when the characters kill his lieutenants without first offering terms."). It conflicts with `07-bregan-daerthe.md:76` ("it prefers non-lethal containment") and `08-bregan-daerthe.md:77` (D7) | `campaign/guides/factions/08-bregan-daerthe.md:122` (the Lockdown row names the lieutenants deployed together) and `:124` |
| 10 | L25 | "**Relationships.** Jarlaxle is the leader of Bregan D'aerthe, the secret lord of Luskan, the employer of Soluun, Fel'rekt, and Krebbyg, and a rival who may become an ally if the party offers him something worth more than the gold." | The clause "if the party offers him something worth more than the gold" is quest-time (the Sea Maidens Faire negotiation). The rest is day-one | `villains/jarlaxle.md:92` (Phase 2B); `sources/adventure-wdh.json:22949` |
| 11 | L25 | "He has known of the Stone, the Eyes, and the vault since reaching Waterdeep, no later than Marpenoth 3, 1491 DR." | Day-one (Session 47 ruling; D1) | `villains/jarlaxle.md:23`, `:55` |
| 12 | L25 | "He alone outside the household and the cult knows of the Cassalanter pact, through his doppelganger spy Vessa." | Day-one, and the Cassalanter secrecy exception (CLAUDE.md) | `villains/jarlaxle.md:59` |
| 13 | L25 | "Eye #3 is aboard the *Scarlet Marpenoth*." | Day-one (the Eye was lifted the night before Ches 1) | `villains/jarlaxle.md:57`; `07-bregan-daerthe.md:31` |
| 14 | L29 | "A flamboyant Illuskan sea captain running the Sea Maidens Faire carnival out of Deepwater Harbor, theatrical, immediately charming, with a precision behind the showmanship that most people don't notice until the conversation is already over." | Day-one. Shows Zord only; J.B. Nevercott is missing (D4) | `07-bregan-daerthe.md:118` |

**Voice profile (`.claude/skills/character-voices/voices/bregan-daerthe.md`), quest-time or encounter clauses for the rule-16 restatement**

Jarlaxle profile, "### Jarlaxle Baenre" (line 26):
- Line 38, Greeting: "  - *Greeting:* \"Ah. The famous tavern-keepers. Please, sit; I've been looking forward to deciding whether you're useful or dangerous. Ideally both.\"" Presupposes that the party is known as tavern-keepers, a Trollskull Alley fact (quest-time: restate or cut).
- Line 39, Business: "  - *Business:* \"You want the Eye. I want Luskan at the Lords' table. I suspect there's an arrangement here that leaves us both delighted and someone else quite upset.\"" Presupposes that the party is after the Eye (quest-time: Fireball! and Gralhund Villa).
- Line 40, Under pressure: "  - *Under pressure:* \"Draw that, and my crew will be very sad to lose such a promising friend. Put it away, and we can be friends a while longer.\"" Encounter-time.
- Line 33, Personality in speech (day-one, kept): "- **Personality in speech:** Theatrical amusement over constant calculation. He tests every new contact aloud, useful or dangerous, and is visibly pleased to find them both. Contempt for fools who threaten him is swift and courteous. His loyalty to Bregan D'aerthe is framed as pragmatism."

Zardoz Zord profile, "### Captain Zardoz Zord (Jarlaxle's cover)" (line 7):
- Line 15, "- **What slips when the cover strains:** The accent thins. His vocabulary becomes suddenly elegant (\"How very inconvenient.\"). He calls someone \"my dear\" in a silky register that doesn't belong to a sailor." Describes the cover under strain (encounter-time; keep as a rule).
- Line 20, Greeting: "  - *Greeting:* \"Ahoy! Welcome, welcome aboard the Eyecatcher, finest carnival on the Sword Coast! Salt and thunder, you lot look like you need a drink and a marvel.\"" Day-one.
- Line 22, Under pressure (slipping): "  - *Under pressure (slipping):* \"Now, now. Let's not spoil the evening. That would be… most inconvenient, my dear.\"" Encounter-time.

**Routed to quests (quest-time text)**
- The Nevercott visit to Trollskull Manor: "J.B. Nevercott knocks at the front door of Trollskull Manor at 10 a.m. the next morning. Proceed to **The Haberdasher at the Door**." — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:159`
- The Jarlaxle Unmasked rule and the reveal: "Mark each such character with the **Jarlaxle Unmasked** Event Outcome. The full reveal conversation takes place at **Sea Maidens Faire**." — `campaign/setting/villains/jarlaxle.md:9`. The brief says this page links to the Villains page and does not copy it. The ledger route is at `villains/jarlaxle.md:28`: "In **Fireball!** a character can learn the name in two ways. Both folios of the Eyecatcher ledger open with \"Sold through the Eyecatcher, J. Baenre, for the Company\", and a character who reads either one and succeeds on a DC 14 Intelligence (History) check knows the name."
- The BD Contact Severed rule: "A character is marked by giving Sergeant Marek Dunmere their name in the **Bregan D'aerthe First Meeting**, by attacking Nevercott, or by exposing a Bregan D'aerthe drow in **Kreb Drops the Cover**." — `campaign/setting/villains/jarlaxle.md:17`
- The Jarlaxle Informed trigger (Fireball!, read in Gralhund Villa): `campaign/setting/villains/jarlaxle.md:23`.
- The offer to Laeral in the adventure: "He intends to return the gold to {@creature Laeral Silverhand|WDH}, less 5,000 gp for the characters in exchange for their help." — `sources/adventure-wdh.json:22949` (see D8)
- The Gralhund Villa team: "Jarlaxle has already briefed Fel'Rekt that D'Aerthe operatives may be present." — `sources/Act_III_Arc_E.md:748`
- The Vault of Dragons offer at Renown 25: "At Renown 25 (Commander): Jarlaxle proposes returning the gold publicly, in the party's name, to Laeral Silverhand — in exchange for a letter of introduction to the Lords' Alliance council." — `campaign/guides/factions/08-bregan-daerthe.md:33`
- The nimblewright sale to Gralhund: "Jarlaxle Baenre sold the nimblewright to the Gralhunds and is therefore aware of exactly what it witnessed and where it went" — `sources/Act_III_Arc_D.md:166`
- The Captain's Office: "**Captain Zord's Office** is accessible — he keeps regular hours and is known to enjoy meeting interesting visitors. His real name is **Jarlaxle Baenre**. He does not advertise this." — `sources/Act_III_Arc_D.md:366`
- The Seven Masks Theater as an outpost: "In **Faction Outposts**, the theater is the street-level entry to the Bregan D'aerthe chain, and members at renown 3 or higher walk in without questions." — `campaign/gazetteer/waterdeep/dock-ward.md:71`

---

## D. Conflicts

Rank used: campaign files first, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.

**D1. What Jarlaxle knows at the start (the Stone and the Grand Game)**
- Campaign, the activation: "Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep, no later than Marpenoth 3, 1491 DR." — `campaign/setting/villains/jarlaxle.md:23`
- Campaign, the Draft Notes: "> - **Conflicts:** What he knows at the start. `1. The Villains.pdf` p.17 says he is unaware of the Stone and the Grand Game. The user's Session 47 ruling overrules it (`history/03-bregan-daerthes-long-road.md` line 160), and the page follows the ruling. The Alexandrian line is a transcription from a page image." — `campaign/setting/villains/jarlaxle.md:173`
- Alexandrian (transcription): "As *Dragon Heist* begins, Jarlaxle is unaware of the *Stone of Golorr* or the Grand Game which is being played." — `sources/1. The Villains.pdf` printed p.17
- Campaign wins.

**D2. The submarine's position**
- Adventure: "This underwater vessel is mounted below the {@i Eyecatcher} and kept out of sight." — `sources/adventure-wdh.json:32181`
- Campaign: "In the campaign the *Scarlet Marpenoth* has been moored in Deepwater Harbor since he reached the city, and it keel-docks beneath the *Eyecatcher* when the fleet arrives" — `campaign/setting/villains/jarlaxle.md:54`
- Alexandrian (transcription, Villains PDF printed p.17): "In Jarlaxle's stateroom onboard the Scarlet Marpenoth (Area U4, see p. 143) there is a specialized crystal ball that allows him to look out through the eyes of any nimblewright and even review what they've seen."
- Alexandrian (transcription, Sea Maidens PDF printed p.71): "Zelifarn's mother was ... " is not used; the sub is described as "the submarine attached to the bottom of the *Eyecatcher*" (`sources/9. Lair – Sea Maidens Faire.pdf` printed p.71).
- Campaign's Draft Notes on the mooring: "The page follows the campaign." — `campaign/setting/organizations/07-bregan-daerthe.md:194`, which cites `sea-maidens-faire/area-overview.md:10`.

**D3. Nimblewright origin**
- Adventure: "Zord visits the distant island of Lantan about once a year. During his last visit, he purchased four nimblewrights from a Lantanese wizard. He keeps two aboard his flagship, and one aboard each of the other two vessels." — `sources/adventure-wdh.json:4746`
- Alexandrian (transcription, Villains PDF printed p.17): "NIMBLEWRIGHTS: One of Jarlaxle's main objectives right now is the sale of nimblewrights. Built by the technomancers of Luskan, he's brought several dozen of these constructs with him and is selling them at surprisingly compelling prices."
- Campaign: "Zord sells nimblewrights to wealthy families across the wards" (`campaign/setting/villains/jarlaxle.md:56`); origin not stated.
- Campaign Draft Notes: "> - **The nimblewrights.** The campaign has Jarlaxle selling nimblewrights to wealthy households as an intelligence network (`arc-h` line 13), and the published adventure has him buying them from a Lantanese wizard (`adventure-wdh.json` line 4746). The network itself is run in **Sea Maidens Faire**, and Draft Notes logs the disagreement over their origin." — `campaign/setting/history/03-bregan-daerthes-long-road.md:134`
- Unresolved. The page should not state an origin until a ruling exists.

**D4. The public faces (Zord and Nevercott)**
- Brief ruling 9: "9. **Xanathar is "it"**, the guild is "Xanathar's Guild", and the Zardoz Zord rule holds (J.B. Nevercott and Captain Zardoz Zord are two figures in the public Overview)." — `docs/plans/setting-compendium-pass6-brief.md:43`
- The orchestrator's rule for this pass: Zardoz Zord and J.B. Nevercott are separate public faces, and only the Villains page carries the link. This is the task instruction, not a brief line.
- Campaign, the page (line 21): "To the world, Jarlaxle is Captain Zardoz Zord" (quoted in A9). The page's Overview (line 29) does not name J.B. Nevercott.
- Organization Overview, the public face: "A haberdasher named J.B. Nevercott, in a burgundy coat, calls on people on the company's behalf. Captain Zardoz Zord, the flamboyant Illuskan master of the Sea Maidens Faire, welcomes interesting visitors aboard the *Eyecatcher*." — `campaign/setting/organizations/07-bregan-daerthe.md:118`
- Villains Draft Notes (line 176): "> - **Calls applied:** Per ruling 7, the Summary and the GM Notes name **Jarlaxle Unmasked** and the Fireball ledger and cabin routes, and the Overview shows only J.B. Nevercott and Zardoz Zord." — `campaign/setting/villains/jarlaxle.md:176`

**D5. The arrival date**
- Alexandrian parade schedule (transcription, Sea Maidens PDF printed p.69): "Ches 10th, announcing its arrival"
- Campaign: "The fleet is due in Deepwater Harbor on Ches 21, the opening day of Fleetswake" — `campaign/setting/organizations/07-bregan-daerthe.md:31`
- Alexandrian end date (transcription, printed p.70): "On Tarsakh 20th, the Sea Maidens Faire packs up and sails out of Waterdeep harbor." Agrees with the campaign's Tarsakh 20.
- Adventure: no arrival date for the Faire was found.
- Campaign's Draft Notes on the first knock: "> - **Conflicts:** The day Nevercott first knocks. `player-factions-overview.md` line 174 says \"the next morning\". `00-first-meeting/ev-01-first-meeting.md` lines 34 and 137 say 10 a.m. on Ches 10, and lines 350 and 415 give the second visit as dusk on Ches 20. The page states no date." — `campaign/setting/villains/jarlaxle.md:175`

**D6. Stat block**
- Campaign: "Stat block: **Swashbuckler (with modifications)**." — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:5`
- Adventure: "drow swashbuckler" with no modifications named — `sources/adventure-wdh.json:549`
- Wiki bundle: class4e Skirmisher (line 244), challenge5e 15 (line 247). No Swashbuckler stat in the wiki.
- Unsourced beyond the page. The drafter should mark it `[research]` or cut it.

**D7. Lethality**
- Organization page, Beliefs: "- **Leverage Before Force:** Jarlaxle would rather leave an enemy confused than dead, and he reaches for leverage before he reaches for a blade." — `campaign/setting/organizations/07-bregan-daerthe.md:36`
- Factions Guide, Methods: "Bregan D'aerthe teams favor misdirection over lethal force. Jarlaxle's preference is non-lethal resolution — confused enemies are more useful to him than dead ones." — `campaign/guides/factions/08-bregan-daerthe.md:77`
- Adventure, the page's Morale source: "If forced into a violent confrontation, he swiftly and brutally kills someone to make an example of them and then walks off." — `sources/adventure-wdh.json:550`
- The page keeps the adventure's sentence verbatim (brief ruling 3). The conflict is flagged here for the drafter.

**D8. The offer to Laeral and the Lords' Alliance**
- Villains Phase 2B: "his offer (Eye for Lords' Alliance membership for Luskan) is genuine and he'll honor it" — `campaign/setting/villains/jarlaxle.md:92`
- Factions Guide: "Jarlaxle proposes returning the gold publicly, in the party's name, to Laeral Silverhand — in exchange for a letter of introduction to the Lords' Alliance council." — `campaign/guides/factions/08-bregan-daerthe.md:33`
- Adventure: "He intends to return the gold to {@creature Laeral Silverhand|WDH}, less 5,000 gp for the characters in exchange for their help." — `sources/adventure-wdh.json:22949`
- Three different terms. The Organization page's Draft Notes flag this ("The vault offer", `campaign/setting/organizations/07-bregan-daerthe.md:186`). The page states none of the three.

**D9. Lolth in the published text**
- Adventure, the Compromised Eye mission (Appendix C): "Make it quick and painless, and for Lolth's sake, be discreet. I will give you a route." — `sources/Appendix_C_-_Player_Faction_Missions.md:1610`
- Campaign, Deities page: "> - **The Compromised Eye:** The published Jarlaxle mission says \"for Lolth's sake, be discreet\" (`sources/adventure-wdh.json:3633`). The campaign cuts the line because Bregan D'aerthe has rejected her (`campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/design-notes.md:13`)." — `campaign/setting/deities/lolth.md:90`
- Resolved in favour of the campaign.

**D10. Non-drow membership**
- Adventure: "Jarlaxle employs non-drow operatives as well, none of whom know they're working for him; such individuals aren't considered members of the faction." — `sources/adventure-wdh.json:1298`
- The pass5 wiki bundle says the band "had some non-drow members (particularly hobgoblins and bugbears)". The Organization Draft Notes quote this at `campaign/setting/organizations/07-bregan-daerthe.md:193` (wiki bundle line 104). Not settled on this page.

**D11. Whether the crews know the captain's identity**
- Adventure: "all know that Zardoz Zord is {@creature Jarlaxle Baenre|WDH} in disguise." — `sources/adventure-wdh.json:23047`
- Campaign, the Villains page: "> - **Membership.**" and "Until a member is marked, no Bregan D'aerthe speaker says \"Jarlaxle\" to that member. They say \"the captain\" or \"J.\"" — `campaign/setting/villains/jarlaxle.md:31`
- The Organization Draft Notes flag the same conflict (`campaign/setting/organizations/07-bregan-daerthe.md:191`). The crews are not speakers under the campaign rule. The page should not state what the crews know.

**D12. Ship crews' disguise method**
- Adventure: "all magically disguised as slender humans while aboard their vessel" (`sources/adventure-wdh.json:23047`).
- Campaign: "under an illusion projected from the gilded figurehead on each forecastle" (`campaign/setting/organizations/07-bregan-daerthe.md:61`). Not on this page except for the Zord disguise.

**D13. Two cabins on the Eyecatcher and the submarine**
- Alexandrian (transcription, Sea Maidens PDF printed p.72): "Area J30 – Zardoz Zord's Cabin: In addition to the normal entry for this area, a **small desk** contains a variety of papers."
- Campaign: "He keeps it in his stateroom, U4, aboard the *Scarlet Marpenoth*" (`campaign/setting/villains/jarlaxle.md:57`). Not a conflict: the two are different rooms. The campaign files do not name a Zord cabin on the Eyecatcher.

---

## E. Stale lines in other files (not edited) and routed quest references

**Stale, not edited**
- `campaign/setting/villains/xanathar.md:95` links "**Jarlaxle**", which should read "**Jarlaxle Baenre**" (quoted in the Organization Draft Notes at `campaign/setting/organizations/07-bregan-daerthe.md:183` and in `villains/jarlaxle.md:183`).
- `campaign/guides/factions/08-bregan-daerthe.md:9` says Jarlaxle is "content to let the other factions exhaust themselves". `campaign/setting/villains/jarlaxle.md:121` (Goal 2) says he moves on the other Eyes. Quoted at `villains/jarlaxle.md:168`.
- `campaign/setting/villains/jarlaxle.md:183` cites the old line numbers of `07-bregan-daerthe.md`. `campaign/setting/history/03-bregan-daerthes-long-road.md:97` cites the old line numbers too (quoted at `07-bregan-daerthe.md:209`).
- `campaign/structure/arc-d-gralhund-villa.md` lines 75-77 and 344 use "Arc C" labels and "attunement" (quoted at `villains/jarlaxle.md:182`).
- `player-factions-overview.md` line 179 titles its callout "Bregan D'aerthe Contact Severed", which is not the outcome's name (quoted at `villains/jarlaxle.md:183`).
- `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/design-notes.md` says the Notable Figures page gives Nar'l a three-year tenure; `03-narl-xibrindas.md` says one year (Organization Draft Notes at `campaign/setting/organizations/07-bregan-daerthe.md:209`).
- `campaign/structure/arc-h-sea-maidens-faire.md:424` places the Letter from Nar'l in the U3 stateroom. This agrees with the Alexandrian lair (see the Soluun notes).

**Routed to quests (quest-time facts the page cannot state as day-one)**
- Ryvarra's watch on the party from the first night: `campaign/setting/villains/jarlaxle.md:60` (quest-time wording).
- The Jarlaxle Unmasked, BD Contact Severed, BD Acknowledged, Ryvarra Identified, Jarlaxle Informed and the Phase 2 and 3 outcome tracks: `campaign/setting/villains/jarlaxle.md:9-33` and `:81-94`. The Organization page routes the same sentences at `campaign/setting/organizations/07-bregan-daerthe.md:199-203`.
- Gralhund Villa team: `campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:51-57` (per `campaign/setting/organizations/07-bregan-daerthe.md:204`).
- Soluun's quest events (Killer's Fate, The Dive, The Compromised Eye): see `02-soluun-xibrindas.md` in this folder.

---

## F. Gaps a Background would need that no source gives

For each gap, the sourced facts the drafter must stay consistent with are listed.

1. **Birth year, birthplace and age.** No campaign source. The wiki infobox leaves them blank: "| dob            = " (wiki bundle line 209) and "| age            = " (line 204). Consistent facts: born to Yvonnel Baenre (`villains/jarlaxle.md:43`); "the first house of Menzoberranzan" (wiki bundle line 277).
2. **Childhood and training.** Wiki only: "Jarlaxle attended [[Melee-Magthere]], the warriors' academy." (wiki bundle line 279). The campaign is silent. Mark `[research]` or `[design]`.
3. **The near-sacrifice and the brother who died in his place.** Sourced: `villains/jarlaxle.md:43` ("his brother Doquaio died in his place"), and wiki bundle line 277. The campaign's GM-only rule (`deities/lolth.md:79`) keeps this out of player text. The page is GM-facing, so the drafter may state it.
4. **Loss or relationship that still matters (named figures).** Wiki only:
   - Zaknafein: "He eventually betrayed Zaknafein in undisclosed circumstances and still felt guilty over it many years later." (wiki bundle line 281). Zaknafein is also named at `history/03-bregan-daerthes-long-road.md:44` (wiki only).
   - Artemis Entreri: "but always did Jarlaxle regret what had happened to his old friend." (wiki bundle line 302). The campaign does not name Entreri on a Villains, Organization or History page. The brief allows a named figure only where a source already names them. The wiki names him, so the drafter should either use the wiki name and flag it, or use a nameless "old friend".
   - Drizzt Do'Urden: "Drizzt disappeared in [[Icewind Dale]] not long afterwards, and Jarlaxle, despite many expensive attempts, was unable to locate him." (wiki bundle line 313). Campaign: `campaign/setting/deities/demogorgon.md:49` names Drizzt (wiki-derived).
   - Catti-brie: "After Catti-brie wandered off, Drizzt and Bruenor asked Jarlaxle to try to find her. He searched \"half the Realms\" to no avail." (wiki bundle line 308). Not on any Jarlaxle campaign page.
   - Zaknafein's return: "was a shock and a welcome surprise to Jarlaxle. He was happy to have one of his oldest friends returned" (wiki bundle line 325). Wiki only.
5. **Personal goals.** No campaign or adventure source gives a personal goal beyond the company and the Stone. Wiki-only candidates (section G): finding Catti-brie; dragons ("He had no qualms about flirting with (and sleeping with) dragons." wiki bundle line 273); the surface over Menzoberranzan ("In his later years, he preferred to see adventure and profit in the World Above." wiki bundle line 267).
6. **The Menzoberranzan years and the Calimport base.** Wiki only (1357-1366 DR, wiki bundle lines 286-288). The history page logs the 1366 DR Calimport base as wiki-only (`history/03-bregan-daerthes-long-road.md:51`). Kimmuriel Oblodra as co-leader is excluded by the campaign (`villains/jarlaxle.md:184`; `organizations/07-bregan-daerthe.md:175`).
7. **Where he lives and sleeps.** Campaign: the stateroom U4 aboard the *Scarlet Marpenoth* (`villains/jarlaxle.md:57`). Wiki, via the Organization page: "Its Luskan headquarters lie underground in Illusk, on a path that connects to Closeguard Isle and Ship Kurth, and Jarlaxle keeps a private room there (Forgotten Realms Wiki, *Bregan D'aerthe*, edition not stated)." — `campaign/setting/organizations/07-bregan-daerthe.md:65`
8. **Fears and grudges.** Only indirect sources: "Jarlaxle is always looking for new members" (`sources/adventure-wdh.json:1297`); "He is never threatened by capable people, and he collects them." (`campaign/setting/organizations/07-bregan-daerthe.md:53`). No fear is sourced. Mark `[design]`.
9. **Pronoun and real species.** Drow and he/him are sourced. No gap.
10. **Age at Ches 1.** Not sourced. The wiki infobox is blank (wiki bundle line 204).

---

## G. Source facts that hint at the inner life (habits, loves, grudges, losses, places, people)

The drafter uses these for the backstory and personal goals (brief ruling 17). Nothing invented may contradict them.

**Habits and pleasures**
> "He is always performing, and the performance is genuine, the act of a man who chose delight as a survival strategy and discovered it works." — `campaign/setting/organizations/07-bregan-daerthe.md:53`
> "Deep down, he likes to weave schemes that leave his enemies baffled, and the look on their faces when he gets the better of them is its own reward." — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:21`
> "Jarlaxle delights in thwarting his enemies, enjoys the complications that arise when adventurers try to meddle in his affairs, and loves to see the looks on their faces when he finally gets the better of them." — `sources/adventure-wdh.json:550`
> "He loved irony, sarcasm, and wit." — wiki bundle line 269
> "He had no qualms about flirting with (and sleeping with) dragons." — wiki bundle line 273
> "- **Quirks:** He adjusts his hat before a decisive line. He compliments an opponent sincerely in the middle of beating them. He laughs at his own schemes when they work." — `.claude/skills/character-voices/voices/bregan-daerthe.md:34`

**Curiosity and restlessness (wiki)**
> "He had an \"insatiable curiosity and a desire to know—everything.\"" — wiki bundle line 267
> "This curiosity made him antsy when he remained stuck in one place too long and drove his quest for personal exploration." — wiki bundle line 267
> "He found that he felt most alive when he was with friends and when he was taking risks." — wiki bundle line 267

**Loyalty (campaign and adventure)**
> "His loyalties run to himself first and to the company second." — `campaign/setting/villains/jarlaxle.md:39`
> "Jarlaxle's loyalties are to himself first and foremost, and to Bregan D'aerthe secondarily." — `sources/adventure-wdh.json:32182`

**Wants (campaign, verbatim Goals)**
> "- **Hold one Eye of the Stone.** He wants it as a bargaining chip, not for personal use." — `campaign/setting/villains/jarlaxle.md:121` (the line continues in the source)
> "He wants Laeral Silverhand in his debt more than he wants any sum of gold, and he wants one Eye of the Stone as a chip to trade for it." — `campaign/setting/organizations/07-bregan-daerthe.md:77`
> "- **Make Waterdeep a permanent base.** The Sea Maidens Faire is seasonal, and Jarlaxle wants Bregan D'aerthe with a permanent Dock Ward presence." — `campaign/setting/villains/jarlaxle.md:122` (tagged `[research]` in the source)

**Places**
> "Jarlaxle keeps his stateroom aboard, and the crystal ball that serves the nimblewright network is aboard too." — `campaign/setting/organizations/07-bregan-daerthe.md:63`
> "Jarlaxle plans on using the submarine to flee Waterdeep if his scheme unravels." — `sources/adventure-wdh.json:32181`
> "- **Keep a Way Out:** Jarlaxle plans to flee Waterdeep in the *Scarlet Marpenoth* if his scheme unravels (*Waterdeep: Dragon Heist*, 5e)." — `campaign/setting/organizations/07-bregan-daerthe.md:44`

**Grudges and old wounds (wiki)**
> "Jarlaxle was viewed as favored by the Spider Queen." — wiki bundle line 277
> "Matron Baenre feared Jarlaxle from that time forward and believed that her fate was tied with his" — wiki bundle line 277
> "Kimmuriel Oblodra was one of only three living drow who knew the truth of the story" — wiki bundle line 277

**Named people he is tied to (campaign)**
> "| Renaer Neverember | Political connection | Worth cultivating; Renaer's relationship with Laeral is an indirect path to the Open Lord's attention; Renaer doesn't know who he met `[research]` |" — `campaign/setting/villains/jarlaxle.md:108`
> "- **Fel'rekt Lafeen** — Drow gunslinger, neutral good, and BD lieutenant. One of Jarlaxle's most trusted men, he is the close friend and operational partner of Krebbyg Masq'il'yr and keeps his heritage to himself." — `campaign/setting/organizations/07-bregan-daerthe.md:101`
> "Fel'rekt Lafeen petitioned to join because he was unhappy with the treatment of males in drow society, and Jarlaxle took to him almost at once (*Waterdeep: Dragon Heist*, 5e)." — `campaign/setting/organizations/07-bregan-daerthe.md:42` (about Fel'rekt's recruitment; the one clause about Jarlaxle's attitude is "Jarlaxle took to him almost at once")

**Voice (character-voices profile, Jarlaxle)**
> "- **Never:** He never loses his temper, never breaks a deal he's proud of, and never lets anyone see the whole scheme." — `.claude/skills/character-voices/voices/bregan-daerthe.md:36`
> "- **Signature phrases:** \"Delightful.\" / \"Useful, or dangerous? Ideally both.\" / \"Let us come to an arrangement.\"" — `.claude/skills/character-voices/voices/bregan-daerthe.md:35`

**Wiki: the Zaknafein betrayal (wiki only)**
> "In the {{YearlinkName|1018}},<ref name=\"Timeless-p?\">{{Cite book/Timeless|?}}</ref> Jarlaxle got to know [[Zaknafein Do'Urden]], later the father of [[Drizzt Do'Urden]]. They became close friends in time, but he eventually betrayed Zaknafein in undisclosed circumstances and still felt guilty over it many years later." — wiki bundle line 281

**Wiki: Entreri (wiki only)**
> "Jarlaxle and Athrogate went on numerous adventures together over the next several decades but always did Jarlaxle regret what had happened to his old friend." — wiki bundle line 302

---

## Not found

Searched and not found, with the files and terms tried:
- **Birth year, birthplace, age, a childhood on any campaign page:** searched "Yvonnel", "Doquaio", "Gromph", "Entreri", "Athrogate", "Catti", "Drizzt", "Zaknafein" across `campaign/`. The Villains, History, Organization and Deities pages (lolth, demogorgon, grazzt) name some of them. No campaign page gives a birth year or age.
- **Stat block "Swashbuckler (with modifications)":** grep for "with modifications|Swashbuckler" in `sources/adventure-wdh.json` (only line 549 "drow swashbuckler" and unrelated NPC lines) and in `campaign/` (only the page itself, line 5).
- **Jarlaxle alignment** in the adventure: none at `sources/adventure-wdh.json:545-551` or `:32172-32184`.
- **Jarlaxle personal goals** in the adventure (greps of "Jarlaxle" across the file, read at lines 157, 519, 545-551, 898, 1279, 1297-1300, 14782, 15149, 22941-22951, 23018-23036, 23047, 23069, 32178-32182): none beyond the company, Luskan, the Lords' Alliance, the dragonstaff and the submarine.
- **Appendix B** (`sources/Appendix_B_-_Player_Factions.md`, lines 695-810): found the Bregan entry; no birth or childhood.
- **Appendix C** (grep lines 319-1873; read 1176-1223): found; no birth or childhood.
- **Act_III_Arc_E.md** (grep lines 74, 727-893): found; no birth or childhood.
- **Act_III_Arc_D.md** (grep lines 37, 166, 366-404): found quest-time lines. No birth or childhood.
- **`sources/SOURCE_GUIDE.md`** (lines 33, 137, 167, 170-178, 283-311, 596, 690, 698, 717): names Jarlaxle and the two `.docx` files. No Background facts.
- **`sources/5. Faction Outposts.pdf`** printed pp.36-38 (PDF pp.1-3): Jarlaxle named ("GM Note: \"J\" is Jarlaxle Baenre and \"K\" is Krebbyg."). No birth or childhood. The Outposts text after p.38 was not read.
- **`sources/9. Lair – Sea Maidens Faire.pdf`** printed pp.68-75 (PDF pp.1-8): read. The lair beyond p.75 was not read.
- **`sources/17. Outpost and Lair Revelation Lists.pdf`:** not read.
- **Wiki Jarlaxle extract** (`wiki-bregan-daerthe/01-jarlaxle-baenre.txt`): "NOT FOUND". Replaced by the pass5 bundle (`sources/research/pass5-bundles/bregan-daerthe/wiki.txt` lines 182-331). The pass3 and pass4 bundles were not searched for Jarlaxle.
- **Personal goals** in the Villains page or the Factions Guide beyond Goals 1-3 (`villains/jarlaxle.md:120-122`): none.
- **Whether Jarlaxle is a haberdasher on his own time, or has a personal life apart from the company:** none.

## Not readable

- `Jarlaxle Baenre NPC Guide.docx` (listed in `sources/SOURCE_GUIDE.md:690`): the tools cannot open `.docx`. The History page cites it for the "third son" gloss (`campaign/setting/history/03-bregan-daerthes-long-road.md:36`), and its Draft Notes cite lines 51 and 62 of the docx (history 03 line 140). The drafter cannot check that gloss. Needs extraction.
- `Zardoz Zord (and extra side quest hook).docx` (listed in `sources/SOURCE_GUIDE.md:698`): not readable. It may hold Zord's persona and an extra side quest.
- `sources/17. Outpost and Lair Revelation Lists.pdf`: not read this session.
- `sources/1. The Villains.pdf`, `sources/9. Lair – Sea Maidens Faire.pdf`, `sources/5. Faction Outposts.pdf`: read as page images. The quotes are transcriptions and need `pdftotext -layout`.
- `wiki-bregan-daerthe/01-jarlaxle-baenre.txt`: contains "NOT FOUND" only. The orchestrator should re-extract the wiki page.
