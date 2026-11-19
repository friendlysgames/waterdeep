# Pass 5 research notes: City Watch (slug `city-watch`)

Scope: the City Watch as the Open Lord's police apparatus and a Grand Game participant. Organization page (lore, `campaign/setting/organizations/`) plus Factions Guide page (mechanics, `campaign/guides/factions/`). Day-one state is Ches 1, 1492 DR (brief ruling 28).

Method and limits. This session had no shell tool, so `pdftotext` was not run. Both Alexandrian PDFs and the first 11 pages of `4. Gralhund Villa.pdf` were read through the Read tool, and PDF citations use the printed page numbers. Wiki quotes keep the wikitext's `[[ ]]` and `{{ }}` markup and drop `<ref>` citation tags; the text is otherwise as in the file. Adventure quotes keep the `{@creature …}` tags as written. Line numbers for `adventure-wdh.json` and `adventure-wdmm.json` were checked by Read or Grep against the file; the bundle's `adventure-hits.txt` line numbers match the file.

Main gaps: no Watch headcount, no per-ward response time, no rule for the Watch handing over to the City Guard, no Open Lord response rule in the campaign, no Watch escalation tiers, and no 1492 DR Commander of the Watch. The Factions Guide page must build its response rules from the adventure's scene text and the campaign's own quest files.

---

## 1. Already settled on the governance pages

The four governance pages are `campaign/setting/governance-and-guilds/city-watch.md`, `open-lord-and-masked-lords.md`, `code-legal-and-magisters.md` and `guilds.md`. The new organization page cross-references `city-watch.md` and does not duplicate it.

**What `city-watch.md` settles (lore; the page is a structuring draft):**

> "The City Watch is Waterdeep's police force, charged with keeping the peace and apprehending criminals inside the city. Its officers wear a green-and-goldenrod doublet and a tall steel helmet, and each carries a truncheon, a dagger and a buckler. Because most citizens carry no weapon, that gear is deterrent enough."
> — `campaign/setting/governance-and-guilds/city-watch.md:17`

> "Newcomers confuse the Watch with the City Guard, and the published adventure offers Volo's mnemonic to keep them apart, which runs that the Guard guards the walls while the Watch watches all. The Guard is the city's army, and the Watch walks the streets that the Guard's walls enclose. The Commander of the Watch reports to the Open Lord. No source gives the Watch's total strength, so this page gives none."
> — `campaign/setting/governance-and-guilds/city-watch.md:19`

> "**Where the Watch is based:** The wiki gives the Watch's main base as the Palace of Waterdeep, where the city's officials, the Guard and the clerks also keep their main offices (wiki; City of Splendors: Waterdeep, 3e). The Palace is the Open Lord's seat and is described on **Castle Ward**."
> — `campaign/setting/governance-and-guilds/city-watch.md:31`

> "**Ranks:** Officers rise from constable to sergeant (armar), lieutenant (civilar), captain (senior civilar, who leads a watch post) and major (ward civilar, one for each ward), and the Commander of the Watch stands above them. A Senior Armsmaster in charge of supplies reports to the Commander. The wiki gives the Commander three senior watchlords, the Mage Civilar who leads the wizard corps, the Senior Armsmaster and the Grand Civilar who commands the ward civilars (wiki; City of Splendors boxed set, 2e)."
> — `campaign/setting/governance-and-guilds/city-watch.md:32`

> "**Patrols:** Squads leave the posts on day and night rounds and on special assignments of protection or investigation, and a patrol runs four to twelve officers. A pair of officers walks the Castle Ward, and squads of eight walk the Dock Ward, rising to a dozen at night. A patrol expecting trouble may bring a priest on loan from a local temple or a mage from the Watchful Order. When officers meet trouble they cannot handle, they blow tin whistles that summon more of the Watch and alert nearby citizens."
> — `campaign/setting/governance-and-guilds/city-watch.md:33`

> "**Badge of the Watch (wiki):** The wiki, citing Dragon Heist, says an officer who reaches captain may be given a badge of the Watch. The badge adds protection against attacks and tells the Open Lord where the wearer is, and only the Open Lord can award one. The published adventure gives a badge to Jalester Silvermane and says it returns to Laeral if he loses it."
> — `campaign/setting/governance-and-guilds/city-watch.md:38`

> "**When the party breaks the law:** Characters who engage in overt crime are quickly cornered and arrested by the Watch and brought before a magister. Advocates may speak for those who have allied themselves with influential people. Lords' Alliance agents are more likely to be excused if the Open Lord has cause to let them off. The magisters and the Code Legal are covered on **The Code Legal and the Magisters**."
> — `campaign/setting/governance-and-guilds/city-watch.md:39`

> "The City Guard and the City Watch are two services in 1492 DR: the published adventure gives each its own ranks and duties, and the campaign keeps both."
> — `campaign/setting/governance-and-guilds/city-watch.md:45` (the sentence continues "`[research]`" in the file; the rest of the paragraph covers the wiki's 1,400 garrison, the 1,200 Guard figure and the 1479 DR fold)

> "The Cavalry is a special branch of the City Guard whose riders are veteran soldiers who fly griffons from the Peaktop Aerie atop Mount Waterdeep."
> — `campaign/setting/governance-and-guilds/city-watch.md:47` (rest of the passage covers the ring of feather falling, the Belabranta family, the wiki's 1479 DR disbandment and the 1491 DR refounding; "Its present size is `[research]`.")

> "Waterdeep requires arcane spellcasters who plan to stay to register with the city, and it strongly encourages them to join the Watchful Order, which the published adventure says the Blackstaff heads."
> — `campaign/setting/governance-and-guilds/city-watch.md:51` (the file continues with the Watchful Order's services; this line is a paraphrase-adjacent summary, the source text is in section 5 below)

Governance pages on Open Lord and courts:

> "**Who answers to the Open Lord:** The Commander of the Watch reports to the Open Lord. So does Elminster, the current Warden of Waterdeep. When a problem is beyond diplomats and the city's other armed forces, the Open Lord can mobilize **Force Grey**, which is usually a last resort. Only the Open Lord can strip **Vajra Safahr** of her title as Blackstaff."
> — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:30`

> "**From arrest to judgment:** The City Watch arrests a suspect and brings them to a courthouse, where they are detained until a magister can pass judgment. The published adventure says a magister can pass a sentence without a trial. Advocates may speak for a party that has allied itself with influential NPCs and factions, and a party that has joined the Lords' Alliance is more likely to be excused if Laeral Silverhand has cause to let them off."
> — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:31`

> "What a courthouse holds:** Each courthouse has two guards outside both the front door and the back door at all hours, barred windows, a front desk clerk, cells and a courtroom."
> — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:32` (the file's line opens with "**What a courthouse holds:**" in bold; the quote above begins at "Each courthouse")

> "The Watch opens a review of a magistracy, in **The Legate's Eyes**, when a Force Grey extraction goes wrong, and for 14 days it logs every Tower request to the Watch."
> — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:57` (campaign-only rule, labelled as such in the file)

**What the Alexandrian files add that the governance pages do not carry:**

- The Open Lord response team: "1 veteran, 4 guards, possibly an apprentice wizard, designed as a Medium encounter." The governance pages leave it out on purpose. `open-lord-and-masked-lords.md:113` says: "The campaign has no Open Lord response rule, and the team is left out until the user wants one." See section 5.
- The Alexandrian line that information reaching the City Watch is the likeliest route to the Open Lord (`2. Other Factions.pdf`, p. 21). It is on `campaign/setting/the-grand-game/the-grand-game.md:88` (in the file's Draft Notes) and not on `city-watch.md`. `city-watch.md:135` mentions it as "remark that blabbed information reaches the Open Lord through the Watch (printed page 21)" but the body of the page does not state it.
- Nothing else. `city-watch.md:135` says: "The Alexandrian files add nothing sourced."

---

## 2. Day-one lore (Ches 1, 1492 DR)

**The Watch as a Grand Game actor**

> "The Watch is genuinely trying, most of the time `[research]`, and it knows that some cases are politically untouchable `[research]`. The published adventure says a visitor can trust the Watch to do its duty diligently, and that its strict code of conduct makes it one of the most trusted police forces outside paladin-patrolled Elturgard."
> — `campaign/setting/the-grand-game/the-grand-game.md:35`

> "Most officers are not corrupt by rule. The published adventure names eight crooked Watch veterans in one Masked Lord's pay, which is a handful against a force whose code the same text praises. The officers are susceptible to pressure from above `[research]`, and the GM Notes of **The City Watch** list the cases where that pressure shows."
> — `campaign/setting/the-grand-game/the-grand-game.md:37` (the "not corrupt by rule" sentence is untagged here; its only source is the retired outline, `campaign/structure/ch2-city-of-splendors.md:48`, which reads "not corrupt by default but susceptible to political pressure")

> "The Watch is also how the government learns things. Laeral Silverhand's information comes largely from the Watch and from Jalester Silvermane, and it runs about three moves behind the factions (see **A City Watching Itself**). Whatever a party tells the Watch is the likeliest route by which she learns what is happening, though she may never learn all of it."
> — `campaign/setting/the-grand-game/the-grand-game.md:39`

> "**Informants:** The Watch has informants in every ward `[research]`, and every faction has informants in the Watch `[research]`."
> — `campaign/setting/the-grand-game/the-grand-game.md:29`

**Laeral's information and what she believes**

> "Her intelligence comes from Jalester Silvermane and the Watch, and it is about three moves behind. The party's reports, most of all those carried by the Lords' Alliance, are what bring her up to date."
> — `campaign/setting/history/07-a-city-watching-itself.md:26` (Lore Summary; text after "> - ")

> "Mirt, a Masked Lord and a senior Harper, is her closest advisor. Elminster, the Warden of Waterdeep, answers to her. The Commander of the Watch reports to her."
> — `campaign/setting/history/07-a-city-watching-itself.md:42`

> "Her spies keep watch on the adventurers in the city, and she rewards those who put Waterdeep ahead of themselves. Jalester Silvermane is her field operative and reports to her directly, and the Lords' Alliance is her instrument for acting outside the Palace."
> — `campaign/setting/history/07-a-city-watching-itself.md:43`

> "Laeral was told for years that the vault lay in Neverwinter, and she believed it. Jalester's field reports and the Watch's contacts have placed it there too."
> — `campaign/setting/history/07-a-city-watching-itself.md:51`

> "She does not know that the Stone of Golorr has resurfaced in Waterdeep or that the four villain factions are circling it."
> — `campaign/setting/history/07-a-city-watching-itself.md:52` (first sentence only; the rest of the line is a quest pointer to **Fentree's Ledger**)

> "This agrees with the City Watch's place in **The Grand Game**: the government is trying, aware that some cases are politically untouchable, and it learns what it knows from informants who are a step behind the factions."
> — `campaign/setting/history/07-a-city-watching-itself.md:64`

> "At campaign start, Laeral is three moves behind. Jalester's field reports and the Watch's contacts have placed the vault somewhere in Neverwinter. She doesn't know that the Stone of Golorr has resurfaced in Waterdeep or that all four villain factions are circling it."
> — `campaign/guides/factions/03-lords-alliance.md:9` (Factions Guide, Grand Game Stance; mechanics page, but this is the day-one state)

> "- **Laeral's intelligence:** Laeral believes the vault is in Neverwinter, and she does not know the Stone has resurfaced or that four villain factions are active. Her information comes largely from the Watch and from Jalester, and it runs about three moves behind the factions."
> — `campaign/setting/organizations/02-lords-alliance.md:61`

> "OPEN LORD: The Open Lord of Waterdeep isn't exactly a "minor" faction, but Laeral Silverhand is considerably behind the curve in the current Grand Game."
> — `sources/2. Other Factions.pdf`, printed p. 21 (PDF page 2)

> "The most likely avenue for that to change — and potentially change rapidly — is through information blabbed to the City Watch. This could happen as early as Scenario 1 (depending on exactly what Renaer and/or the PCs report to the watch), but it's quite possible for the Open Lord to never fully twig to what's happening."
> — `sources/2. Other Factions.pdf`, printed p. 21 (PDF page 2)

**How information reaches the Watch and then Laeral (campaign mechanics of day-one lore)**

> "Jalester Silvermane ... He carries a badge of the City Watch and reads the Watch's file ledger each tenday, and he is grieving his partner, Faerrel Dunblade, who died last year exposing a plot against the government, and he fills the silence with work."
> — `campaign/setting/organizations/02-lords-alliance.md:66` (the sentence is cut here; the quote covers the first clause only and the rest concerns the Alliance's grief for Faerrel)

> "Jalester reads the Watch's file ledger each tenday, so he learns what a Stingblade asked for."
> — `campaign/guides/gm-guide/player-factions-overview.md:111` (text quoted in part; the row continues with the Stingblade mechanic)

**Watch informants and sources in the city**

> "Gosta moonlights as an informal Watch informant — not a spy exactly, more a civic-minded citizen who has been filing regular reports on \"establishments of interest\" for the better part of a decade. He considers this entirely compatible with his employment. He doesn't report anything actionable; he reports atmospherics — who comes in, how often, whether the crowd skews toward any particular guild or faction. The Watch values him precisely because he is boring and consistent."
> — `campaign/guides/trollskull-manor/` source: `sources/Appendix_D_-_Running_the_Tavern.md:159`

> "**Faction Note:** Informal City Watch informant. Not a planted spy — this is his own civic arrangement, predating any party involvement."
> — `sources/Appendix_D_-_Running_the_Tavern.md:163`

> "Deep down, she keeps meticulous records not out of professional pride but because the Watch has stopped by twice this year asking similar questions, and she finds it less trouble to have the answers ready."
> — `campaign/setting/notable-figures/independents-allies/21-myl-dunpier.md:21`

> "- **The Watch has a file:** The City Watch already keeps a file on the cell, so Davil's people avoid anything that invites scrutiny. The cell operates openly, meets in taverns and recruits adventurers, and its fronts are ordinary businesses."
> — `campaign/setting/organizations/06-doom-raiders.md:65`

> "Zhentarim crews with flying snake tattoos work Waterdeep's back streets, and they are hostile to Davil Starsong's Doom Raiders. The crews take prisoners, and the Watch has arrested a few of them in street brawls. None of them will say who gives the orders, and street talk says one master stands behind them."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:61`

> "The Watch doesn't patrol this area, however, and many crimes go uninvestigated."
> — `sources/adventure-wdh.json:31104` (rest of passage: "The City Guard oversees the Field Ward from the walls around it, but its members get involved only when folk moving into or out of the city are threatened.")

> "Its roots lie in Skullport, an outlaw port in the caverns below the city, reached through Undermountain and outside the Watch's jurisdiction, which Netherese wizards built long ago and which many masters have held since."
> — `campaign/setting/history/02-the-long-shadow.md:76`

> "The Field Ward is Waterdeep's slum, an unofficial ward of mud, tanneries and slaughterhouses between the two northernmost walls, outside the city proper and beyond the reach of the Watch."
> — `campaign/gazetteer/waterdeep/field-ward.md:17`

**Watch-side view of the Cassalanters (suspicion only, per brief ruling 7)**

> "Everyone outside the household and the cult only suspects the family, because it is too nice to be this rich and this purebred. Savra Belabranta of the **Order of the Gauntlet** has no legal evidence, Mirt suspects Cassalanter money stood behind the Howling Hatred cult, and Vajra Safahr of **Force Grey** has scried conjuration and abjuration residue beneath the villa. The Lords' Alliance has no proof, the Watch has closed three complaints against the house, and the Emerald Enclave senses infernal influence in the Southern Ward without knowing whose it is."
> — `campaign/setting/villains/cassalanters.md:65`

> "The City Watch has small, single-person \"watch boxes\" set up on nearly every street corner in the Sea Ward, including the intersection just outside the gates of Cassalanter Villa. If a guard sounds the alarm, the Watch member on duty fetches a force of forty City Watch {@creature veteran||veterans} to cordon off the property."
> — `sources/adventure-wdh.json:18579` (this is a day-one fixture of the Sea Ward; the rest of the Cassalanter scene is quest text)

Notes for the drafter on day one: the Cassalanter line about "closed three complaints" is suspicion from a Watch file, not Watch knowledge of the pact. Keep it as suspicion. `campaign/setting/gazetteer sea-ward.md:156` adds "Every sergeant in the ward knows the Watch posts a guard at the Cassalanter service gate." That sentence is campaign-only and is not in the published adventure.

**Watch officers and NPCs in day-one lore**

- Commander of the Watch (1492 DR): no name in any source. `[research]`. Wiki names Captain Rulathon as Commander circa 1372 DR (section 6).
- Warden of Waterdeep (City Guard, not the Watch): "The current Warden of Waterdeep is Elminster, who answers to the Open Lord, {@creature Laeral Silverhand|WDH}." (`sources/adventure-wdh.json:31836`)
- Watch captains hold sewer keys: "City Watch captains hold keys to sewer access points that correspond with their assigned wards." (`sources/adventure-wdh.json:11626`)
- Watch captain Hyustus Staget, Dock Ward: "Captain Hyustus Staget is an uptight man who helps keep the peace in the Dock Ward." (`sources/adventure-wdh.json:2184`; the full paragraph is in section 3)
- Sergeant Saeth Cromley (retired): "Saeth Cromley ... is a retired {@creature sergeant|WDH} of the City Watch who assists in many of his investigations." (`sources/adventure-wdh.json:31774`; the full entry is in section 4)

---

## 3. Tenets (candidate beliefs and habits that explain how the Watch acts)

Each tenet has its source. Where nothing supports a tenet, it reads `[research]` and is listed under "Nothing supports" at the end of this section.

**Keep the blood off the streets, not the sewers.** Watch officers look above the sewers.

> "\"Keep the blood off the streets, okay?\" (This is a common saying among City Watch officials, who care more about what happens in the city above than what happens in the sewers below.)"
> — `sources/adventure-wdh.json:2202`

> "Best not to meddle in criminal matters. Leave this dirty business to the City Watch."
> — `sources/adventure-wdh.json:2200` (said by Staget; the tenet is the Watch's, the words are his)

> "They never acted outside the walls of the city and did not pay much attention to the city's sewers."
> — `sources/research/pass5-bundles/city-watch/wiki.txt:64` (wiki, *City Watch (Waterdeep)*; cites *The Gathering* comic for the walls and *Waterdeep: Dragon Heist* p. 27 for the sewers; the walls claim is wiki-only)

**Arrest quietly, then let the magister judge.**

> "Unlike in less civilized settlements, punishment for crimes in Waterdeep isn't typically used as public entertainment. Scheduled executions occur behind the high walls of Castle Waterdeep, and floggings are carried out in the watch post nearest the sentencing. The Watch makes every effort to take individuals into custody quietly, so as not to disrupt other citizens. Those bystanders generally return the favor by giving altercations between criminals and the Watch a wide berth."
> — `sources/adventure-wdh.json:30515`

> "People who are arrested by the City Watch are brought to a courthouse and detained until a magister can pass judgment on them. Each courthouse has the following features:"
> — `sources/adventure-wdh.json:9791`

**A strict code, kept by most.**

> "City Watch members follow a strict code of conduct that makes them one of the most trusted police forces aside from paladin-patrolled Elturgard. As long as you don't engage in unlawful behavior, you can expect to be left untroubled by the Watch."
> — `sources/adventure-wdh.json:30549`

> "As a rule, you can trust members of the City Watch to do their duty diligently, and you can expect that the city's magisters will be fair."
> — `sources/adventure-wdh.json:30514` (the same paragraph says "Waterdeep is no village led by hidebound hierarchs...")

> "Corylus refuses to speak with the party. If the characters become an annoyance, he has eight crooked members of the City Watch (human {@creature veteran||veterans}) crack down on them, then uses his position as Masked Lord to clear any charges leveled against these Watch members."
> — `sources/adventure-wdh.json:30365` (the code is real and a few officers step outside it; the rest of the passage covers Corylus's entourage and his refusal to be indebted)

**Know the streets; the patrol is the Watch's tool.**

> "I guarantee that all members of the Watch know the streets they patrol and that area's residents better than you do, even if you stay in Waterdeep for ten seasons."
> — `sources/adventure-wdh.json:30546` (the sentence is the handbook's; the paragraph opens with the uniform and "Members of the Watch typically don't carry crossbows or other weapons to attack at range")

> "Small squads head out from the watch posts on daily and nightly rounds of the city streets, or on special assignments involving protection or investigation. A mere pair of Watch operatives might discreetly patrol in the Castle Ward; in contrast, squads of eight walk the Dock Ward, increasing to as many as a dozen at night. If Watch members spot trouble they can't handle, they blow shrill tin whistles to summon more of their members-an act that alerts nearby citizens as well."
> — `sources/adventure-wdh.json:30548`

**Posts are local headquarters and jails, marked by a light.**

> "The City Watch has watch posts throughout the city. These stations are often off the main thoroughfares, tucked away in small courtyards or at cross streets. A watch post can be recognized by the green-and-gold lantern outside it, lit even during the day with a {@spell continual flame} spell. A watch post serves as an organizational headquarters and armory. Anyone who wishes to report a crime may do so at a watch post in the event a Watch constable can't be found elsewhere. A watch post typically contains a few holding cells where people arrested for crimes can be detained until they're marched to a courthouse jail before standing trial."
> — `sources/adventure-wdh.json:30547`

**Search only those who make trouble.**

> "Characters who give up their visible weapons without a fuss aren't searched, but those who give the Watch a hard time are searched for hidden weapons (and stripped of anything that could potentially cause harm)."
> — `sources/adventure-wdh.json:10553` (the rest of the passage covers a Tiny object concealed by a DC 12 Sleight of Hand check and the sergeant's inspection of the Stone; that scene is quest text)

**A search needs a warrant.**

> "Two City Watch constables spoke to Lord Gralhund. He assured them that no one had broken into the estate and that everything was fine. The constables had no grounds to get a search warrant, so they didn't pursue the matter."
> — `sources/adventure-wdh.json:4793` (Ch. 3 Gralhund scene; the rule is the Watch's, the scene is routed to **Gralhund Villa**)

> "Watch officers who see the letter..." — see section 5 (the Gray Hand and Friendly rules are mechanics).

**Trust in the Watch is the public line; the officers say so.**

> "\"Trust in the Watch,\" Cromley adds dismissively."
> — `sources/adventure-wdh.json:4456` (Cromley's line in the fireball scene; the rest of the passage is quest text)

**Doctrine and Rites (the file's sources leave these open; each is listed as sourced)**

- Watch slang, from the published adventure: "\"What befalls?\" means \"Someone tell me what's going on here.\"" / "\"Hold!\" means \"Don't move a muscle.\"" / "\"Down arms!\" means \"Drop your weapons.\"" / "\"Talk truth!\" means \"Answer me\" or \"Tell the whole story.\"" / "\"Robes\" references the black robes-in other words, one of the magisters. \"Do we need robes here?\" or something similar should be taken as a threat." (`sources/adventure-wdh.json:30563`-`30567`; intro at `:30558`)
- Gods' Day: "Gods' Day is also a semiofficial \"Be Kind to the Guard and Watch Day\" in Waterdeep." (`sources/adventure-wdh.json:31536`; Gods' Day is Marpenoth 15, which falls after the campaign window; `campaign/setting/deities/kelemvor.md:67` says so)
- Traffic wardens: "Traffic wardens signal with small blue hand flags for traffic to proceed, and with yellow flags for traffic to hold." (`sources/adventure-wdh.json:30702`)
- Captain's rule of thumb (wiki, 2e): "Law and order—sometimes it's all that separates us from becoming Undermountain or Hellgate Keep." (`sources/research/pass5-bundles/city-watch/wiki.txt:62`; Captain Rulathon, circa 1372 DR; wiki cites *City of Splendors (boxed set)/Campaign Guide* p. 75)

**Watch and the gangs.** Staget's view is the only sourced one, so it is his tenet, not the Watch's:

> "Captain Hyustus Staget is an uptight man who helps keep the peace in the Dock Ward. Every shopkeeper, guild member, innkeeper, and tavern keeper in the Dock Ward knows him, and most respect him regardless of their opinions of the City Watch in general. Staget doesn't believe in rumors or gossip, he doesn't drink, and he doesn't let anger get the better of him. His job is to curb the violence in the Dock Ward, but he has been dragging his heels. After all, he reasons, if the Xanathar Guild and the Zhentarim want to destroy each other, why not let them?"
> — `sources/adventure-wdh.json:2184`

**Nothing supports (tag `[research]` on the organization page):**

- "The Watch is genuinely trying" and "politically untouchable" in the general case. The tag is already in `the-grand-game.md:35`. The only sourced "untouchable" case is one family, through Jalester's briefing (`campaign/structure/arc-g-cassalanter-villa.md:37`, pending conversion).
- "Officers are susceptible to pressure from above" as a Watch-wide rule. The only sourced cases are Corylus Thann's eight veterans (`:30365`) and the structure-document cases (`campaign/structure/arc-i-kolat-towers.md:33-35`, `arc-g-cassalanter-villa.md:35-37`).
- "Watch informants in every ward." The only sourced Watch informant is Gosta Ironhelm (`Appendix_D_-_Running_the_Tavern.md:159`).
- "Most officers are not corrupt by rule" has no published source (section 2).
- Watch sewer policy as an enforced rule. The sewers line is a common saying (`:2202`) and a Staget refusal (`:2196`), not a written policy.

---

## 4. Key Members

Format: name, then the Notable Figures page's own summary line (quoted), then the page path. Pronouns and alignment come from the page. Where a person has no page, the adventure or campaign line is quoted.

**Laeral Silverhand**, Open Lord (not Watch; the Watch reports to her).

> "*Moon elf archmage, chaotic good, she/her*. Stat block: **Archmage**."
> — `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:5`

> "**Affiliation:** City of Waterdeep"
> — `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:6`

Published adventure gives no species (`open-lord-and-masked-lords.md` says the moon elf reading is campaign-only).

**Saeth Cromley**, retired sergeant of the Watch.

> "*Illuskan human retired sergeant, lawful good, he/him*. Stat block: **Warrior Veteran**."
> — `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md:5`

> "**Persona.** To the world, Cromley is a retired sergeant of the City Watch, likable, sharp, a bit lax in dress code now that no one checks."
> — `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md:23`

> "Saeth Cromley is a retired City Watch sergeant who works alongside Barnibus Blastwind on investigations, translating between the investigator's forensic reasoning and the common folk they need to interview."
> — `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md:31`

Adventure: "{@creature Saeth Cromley|wdh} is a retired {@creature sergeant|WDH} of the City Watch, a likable fellow with a sharp, sarcastic wit." (`sources/adventure-wdh.json:32573`). The fireball scene calls him "a City Watch {@creature sergeant|WDH} named {@creature Saeth Cromley|wdh}" (`sources/adventure-wdh.json:4444`). See conflict C12.

**Barnibus Blastwind**, Watchful Order (not Watch; cross-reference only).

> "*Illuskan human Watchful Order investigator, lawful good, he/him*. Stat block: **Mage**."
> — `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:5`

> "**Affiliation:** City of Waterdeep (Watchful Order of Magists and Protectors)"
> — `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:6`

Adventure: "{@creature Barnibus Blastwind|wdh|Barnibus} works for the Watchful Order of Magists and  Protectors, investigating crimes that involve the use of  magic." (`sources/adventure-wdh.json:31774`)

**Jalester Silvermane**, Lords' Alliance field agent; carries the badge of the Watch (cross-reference, not a Watch member).

> "*Chondathan human spy, lawful good, he/him*. Stat block: **Spy**."
> — `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:5`

> "**Affiliation:** Lords' Alliance"
> — `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:6`

> "Jalester carries a {@item badge of the Watch|WDH} (+2 bonus to AC if not using a shield). If the badge is lost or taken from him, it returns to {@creature Laeral Silverhand|WDH}."
> — `sources/adventure-wdh.json:32167`

**Lady Gondafrey**, former Watch captain, prisoner of Kolat Towers.

> "*Lawful good gargoyle (human soul), lawful good / chaotic evil (set by time of day), she/her*. Stat block: **Gargoyle**."
> — `campaign/setting/notable-figures/independents-allies/18-lady-gondafrey.md:5`

> "**Affiliation:** Independent (ally); City Watch (formerly)"
> — `campaign/setting/notable-figures/independents-allies/18-lady-gondafrey.md:6`

Adventure: "The gargoyle retains fragmented memories of the life of {@creature Lady Gondafrey|WDH}, a native Waterdavian who served in the City Watch." (`sources/adventure-wdh.json:28506`). The captaincy and the 1379 DR date are campaign text (`campaign/setting/history/04-the-founding-of-chains.md:67`: "In 1379 DR the City Watch captain Lady Gondafrey tried to breach the towers and was taken prisoner.").

**Hyustus Staget**, Watch captain, Dock Ward (no Notable Figures page).

> "Shortly after the characters find Renaer, a captain of the City Watch named Hyustus Staget (LG male Illuskan human {@creature veteran}) leads a dozen {@creature veteran||veterans} to the warehouse."
> — `sources/adventure-wdh.json:2183`

**Cressa Galavarco**, replacement for Staget if Staget has died (no page; conditional).

> "If Hyustus has died for whatever reason, replace him with a female human Watch officer named Cressa Galavarco (LG female Tethyrian {@creature veteran} with no armor or weapons)."
> — `sources/adventure-wdh.json:17873` (Xanathar's Lair scene; routed)

**Jonn Bannock and Ysa Terrow**, Watch officers in the Brandath grove (campaign-only; event card only, no page).

> "Officer Jonn Bannock (Lawful Neutral, Illuskan Human, he/him) and Officer Ysa Terrow (Lawful Neutral, Tethyrian Human, she/her) :: two City Watch officers on the late shift."
> — `campaign/quests/faction-events/emerald-enclave/m02-ten-nights-in-the-city-of-the-dead/ev-01-the-ten-nights.md:149`

**Marek Dunmere**, North Ward day-shift sergeant at the Watch station (campaign-only; no page; invented for the Bregan D'aerthe First Meeting per its design note).

> "Marek Dunmere (Lawful Neutral, Illuskan Human, he/him) :: the North Ward's day-shift desk sergeant, who has heard every kind of complaint and writes down all of them."
> — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:173`

> "Sergeant Marek Dunmere takes reports on the day shift." (`campaign/gazetteer/waterdeep/north-ward.md:101`, the same sentence is in the Ward's Watch station entry)

**Orvyn Dall**, appeals clerk in a Trades Ward district magistracy (not Watch; see conflict S12). Campaign-only, single quest.

> "Orvyn Dall is an Illuskan Human appeals clerk in the Trades Ward district magistracy."
> — `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-01-the-legates-eyes.md:17`

> "The appeals office of the ward's district magistracy employs four clerks. One of them, Orvyn Dall, an Illuskan human, was placed there seven tendays ago."
> — `campaign/gazetteer/waterdeep/trades-ward.md:93`

**Gosta Ironhelm**, informal Watch informant (tavern applicant; not a Watch member). Source: `sources/Appendix_D_-_Running_the_Tavern.md:153` ("*LN male shield dwarf, Commoner. Competent, joyless, and a City Watch informant.*"); see section 2.

**Darvish** (former Watch officer) and **Bram** (retired Watch sergeant), tavern staff applicants in Appendix D, no page.

> "*LG male human, Commoner. A former City Watch officer, recovering from injury, quietly excellent.*" (`sources/Appendix_D_-_Running_the_Tavern.md:269`; the name is the header's subject, "Darvish is exactly what he says he is" at line 275)

> "*LN male human, Tough. Retired City Watch sergeant. Utterly reliable. Utterly boring.*" (`sources/Appendix_D_-_Running_the_Tavern.md:561`; "Bram is exactly as advertised" at line 567)

**Commander of the Watch, 1492 DR**: no name in any source. `[research]`.

Other names the sources give, in the Watch's chain or the Guard's:

- Elminster, Warden of Waterdeep (City Guard). No page. `sources/adventure-wdh.json:31836`.
- Captain Rulathon, Commander of the Watch, circa 1372 DR (wiki). `sources/research/pass5-bundles/city-watch/wiki.txt:103`.
- Derek Windsfire, Grand Civilar, 1372 DR (wiki). `wiki.txt:94`.
- Thyriellentha Snome, Mage Civilar, 1372 DR (wiki). `wiki.txt:105`; her page, `wiki.txt:1463`: "was the commander of the watch-wizard corps of the [[City Watch (Waterdeep)|City Watch]] in [[Waterdeep]] in [[1372 DR]]."
- Helve Urtrace, Senior Armsmaster, 1372 DR (wiki). `wiki.txt:97`.
- Obryn Ironfist, leader of the Griffon Cavalry (wiki, 1372 DR). `wiki.txt:197`.
- Moedt Belabranta, leader of the Griffon Cavalry, circa 1372 DR (wiki). `wiki.txt:239`.
- Jauslo, watch civilar in charge of the baby griffon recovery for Laeral, 1490s DR (wiki). `wiki.txt:96`.
- Corylus Thann, Masked Lord, eight crooked Watch veterans in his pay. No page. `sources/adventure-wdh.json:30365`.
- Brenna Tull (Trades Ward; no page; the Force Grey extraction; calls the Watch). `campaign/gazetteer/waterdeep/trades-ward.md:259`.

Wiki names pre-dating the campaign (Brace Ulmemur, Emmer Jundhyl, Mulgor, Ilph, Olophin yn Zelmazzar) are on `wiki.txt:93-102`. Left out of Key Members, listed for the drafter's option.

Anyone the sources name who is not Watch and should not appear in Key Members (brief: "Do not add anyone from another faction"): Barnibus (Watchful Order), Jalester (Lords' Alliance), Vajra (Force Grey), Savra (Order of the Gauntlet; the Belabrantas breed the griffons, `sources/adventure-wdh.json:3950`), Tashlyn (Doom Raiders; her cover rank is City Guard, `sources/adventure-wdh.json:31955`).

---

## 5. Mechanics material (for the Factions Guide page)

**5a. The Open Lord response team (the only Alexandrian Watch-type team)**

> "Laeral Silverhand has the entire apparatus of Waterdeep's government at her command. If she wants something from the PCs, that command will trickle down through the bureaucracy and be executed by a local team of city watchmen:
> • 1 veteran (MM p. 350)
> • 4 guards
> • Possibly accompanied by an apprentice wizard (DH p. 194)"
> — `sources/7. Other Response Teams.pdf`, printed p. 58 (PDF page 2)

> "The initial team sent by the Open Lord is designed to be a Medium encounter for the PCs. Which means that the PCs can totally take them in a fair fight (or have very good odds of running away successfully). This intentionally gives the PCs the option of doing so. (Once they do, of course, they're probably living on borrowed time because the Open Lord has much deeper — and much more powerful — resources to call upon.)
> This also means that the City Watch can easily be pitted against response teams from the other factions without trivially overwhelming them."
> — `sources/7. Other Response Teams.pdf`, printed p. 58 (PDF page 2), DESIGN NOTE

Stat references: MM p. 350 (veteran), guard (no page given), DH p. 194 (apprentice wizard). The adventure's own Watch text: "Most City Watch members are {@creature veteran||veterans}. Some of the highest-ranked members are {@creature knight||knights}. All City Watch members wear helmets and carry {@item club|phb|clubs} while on duty." (`sources/adventure-wdh.json:31895`) and "City Guard privates and sergeants are {@creature guard||guards}. Members of lieutenant rank and higher are typically {@creature veteran||veterans}." (`sources/adventure-wdh.json:31846`). Campaign conversions: Warduke's "four **Warrior Veterans** from the Watch" (`campaign/guides/factions/03-lords-alliance.md:69`, and `campaign/guides/gm-guide/player-factions-overview.md:70`); the Bregan D'aerthe event uses "one of the two 2024 **Guards** of a Watch patrol" (`campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/overview.md:10`).

Campaign status of the Open Lord team: `open-lord-and-masked-lords.md:113` leaves it out. No campaign file uses it.

**5b. When and how the Watch responds (adventure text, scene by scene)**

Watch response clocks as written in the sources:

- Gralhund Villa, Ch. 3 (adventure): "Neighbors and bystanders alert the City Watch if they hear loud, disturbing noises (such as a {@spell thunderwave} spell) coming from the estate or if they see anything suspicious. The Watch sends a {@creature mage} and six {@creature veteran||veterans} (one {@creature sergeant|WDH} and five constables) to investigate, and it takes {@dice 1d6 + 4} minutes for this force to arrive." (`sources/adventure-wdh.json:4870`)
- Gralhund Villa area overview (campaign): "**City Watch response:** Any audible commotion outside the perimeter walls brings 1 mage + 6 veterans within 1d6 + 4 minutes. The Watch does not respond to interior sounds during the raid unless drawn by external noise." (`campaign/locations/gralhund-villa/area-overview.md:103`)
- Gralhund Villa, Act III Arc E (Alexandrian markdown): "A Watch response team (a Mage, six Warrior Veterans, and a Guard Captain) arrives 1d6+4 minutes after the first serious noise." (`sources/Act_III_Arc_E.md:774`; conflict C18)
- Fireball (adventure): "The characters have a few minutes to examine the crime scene before the City Guard arrives and cordons off Trollskull Alley, posting six {@creature guard||guards} at each entrance." (`sources/adventure-wdh.json:4427`); "Twenty minutes after the explosion, a City Watch {@creature sergeant|WDH} named {@creature Saeth Cromley|wdh} (see {@adventure appendix B|WDH|12}) escorts a member of the Watchful Order of Magists and Protectors named {@creature Barnibus Blastwind|WDH} ... to the crime scene." (`sources/adventure-wdh.json:4444`)
- Fireball (campaign journal): "Five minutes before the first six City Guard soldiers arrive and seal the alley. Twenty minutes before **Barnibus Blastwind** (meticulous Illuskan human mage, Watchful Order) and **Sergeant Saeth Cromley** appear with twenty constables and formally take charge." (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36`)
- Kalain's converted windmill (adventure): "Any attempt to break into the tower is 75 percent likely to be seen or heard by one of {@creature Kalain|wdh}'s neighbors. Eight {@creature veteran||veterans} of the City Watch arrive 10 minutes later to investigate the intrusion." (`sources/adventure-wdh.json:13249`)
- Dandymops, Trades Ward (adventure): "Since the shop is in a highly visible location, an attempt to break into it is 75 percent likely to be noticed by someone who alerts the City Watch. Two {@creature veteran||veterans} of the City Watch arrive in {@dice 1d10} minutes to investigate the shop and talk to witnesses." (`sources/adventure-wdh.json:11837`; the first sentence is quoted in part, the rest of the passage covers the lock)
- Kolat Towers digging (adventure): "Since Kolat Towers is surrounded by other buildings, there's a {@chance 75|75 percent chance} that any digging attracts {@dice 2d6} members of the City Watch ({@creature veteran||veterans}), who put a stop to it." (`sources/adventure-wdh.json:26812`)
- Sea Ward watch boxes (adventure): "If a guard sounds the alarm, the Watch member on duty fetches a force of forty City Watch {@creature veteran||veterans} to cordon off the property." (`sources/adventure-wdh.json:18579`)
- Trollskull Manor, campaign: "A Watch patrol also answers any disturbance at the manor within the hour, until a Watch citation against the manor ends it for a tenday." (`campaign/guides/trollskull-manor/02-operating-costs.md:83`)
- Trollskull Manor response teams, campaign: "A public massacre in a licensed North Ward establishment invites City Guard, the Watchful Order, and potentially Vajra Safahr personally within the hour." (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:7`)
- Patrol presence per ward (adventure): "A mere pair of Watch operatives might discreetly patrol in the Castle Ward; in contrast, squads of eight walk the Dock Ward, increasing to as many as a dozen at night." (`sources/adventure-wdh.json:30548`); the Trades Ward "The City Watch has a heavy presence in this ward, in the form of both open patrols and officers working out of uniform." (`sources/adventure-wdh.json:31036`).
- Campaign quest responses, for context and the Factions Guide page's examples: Gralhund ev-02 "Any audible commotion outside the walls draws a Watch response in 1d6 + 4 minutes (1 mage, 6 veterans)." (`campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:33`); Gralhund ev-08 "A sleeping dog wakes on a rooftop garden and barks — City Watch responds in 1d6 + 2 minutes." (`campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:46`); Wazoo ev-01 "a patrol of two **Guards** arrives about five minutes later from Immar Street." (`campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:179`); Yellowspire ev-02 "within one minute of the first blow a Castle Ward Watch patrol rounds the corner, which marks **Watch File Opened**." (`campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/ev-02-the-chase.md:153`); Legate's Eyes ev-02 "**Watch review:** If Brenna calls the Watch, a patrol sees the extraction, or Orvyn dies, the Watch opens a review of the Trades Ward magistracy under the Code Legal, and for 14 days it logs every Tower request to the Watch, so Vajra cannot act there off the books, and the party loses the +1 Renown for a clean extraction." (`campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-02-the-extraction.md:186`).

**5c. Escalation: Watch to City Guard, Griffon Cavalry, Watchful Order, Force Grey**

No source gives a rule for the Watch handing over to the City Guard. The adventure and the campaign show these instances:

> "Within days after the events that local broadsheets dub the \"Gralhund Villa Bloodbath,\" the City Watch cracks down on the Black Network." (`sources/adventure-wdh.json:6080`; routed to **Gralhund Villa**)

> "The arrival of the City Watch foreshadows the return of {@creature Barnibus Blastwind|WDH} and {@creature Saeth Cromley|wdh} (see {@adventure appendix B|WDH|12}), who arrive in due course with twenty constables ({@creature veteran||veterans}) and two {@creature griffon cavalry rider|WDH|Griffon Cavalry riders} (see {@adventure appendix B|WDH|12}) astride {@creature griffon||griffons}. The griffons and their riders remain airborne, providing aerial support and reconnaissance." (`sources/adventure-wdh.json:6063`; Gralhund Villa, Ch. 3)

> "A character mounted on a griffon can complete a city-wide search in a couple of hours." (`sources/adventure-wdh.json:4703`; the Bonesnapper griffon, not a campaign file)

> "If you approach by air, expect a vigorous pursuit by and confrontation with the Griffon Cavalry. Only specially licensed individuals and mounts can fly over Waterdeep. It is best to land well outside the city and approach on foot." (`sources/adventure-wdh.json:30447`)

> "Whenever Waterdeep has a problem that can't be handled by diplomats or the city's other armed forces, the Open Lord has the option to mobilize Force Grey. Such action is usually taken as a last resort, since some past members of the group have exhibited a tendency to indulge in wanton violence, causing as much damage as they ostensibly prevent." (`sources/adventure-wdh.json:1341`)

> "Members of the Watchful Order are expected to render service to the city when called upon, acting as temporary members of the City Watch or City Guard." (`sources/adventure-wdh.json:30579`)

> "Once {@creature Manshoon|WDH}'s whereabouts are established, the City Guard cordons off and surrounds Kolat Towers. The Blackstaff and the Watchful Order assist as needed." (`sources/adventure-wdh.json:26765`; conditional, Kolat Towers; routed)

> "The Watch sends a {@creature mage} and six ..." — see 5b (the adventure's response team is Watch, with a sergeant and five constables).

**5d. When the Watch backs down**

> "If the constables ... The constables had no grounds to get a search warrant, so they didn't pursue the matter." — `sources/adventure-wdh.json:4793` (see section 3; the Watch drops a search for lack of a warrant)

> "If Watch members spot trouble they can't handle, they blow shrill tin whistles to summon more of their members" — `sources/adventure-wdh.json:30548`

> "The characters' primary contact is {@creature Jalester Silvermane|WDH} ..." — not relevant.

> "Lords' Alliance agents are more likely to be excused if the Open Lord has cause to let them off." — `campaign/setting/governance-and-guilds/city-watch.md:39` (adventure: "characters who become agents of the Lords' Alliance are more likely to be excused for crimes if {@creature Laeral Silverhand|WDH}, the Open Lord of Waterdeep, has cause to let them off the hook.", `sources/adventure-wdh.json:970`)

> "If the Watch arrests the member on a minor charge, Savra puts in a good word once a tenday and the Order's clerk tends the member's affairs." — `campaign/guides/factions/05-order-of-the-gauntlet.md:64` (table row, Chevall, Renown 1)

> "The Watch makes every effort to take individuals into custody quietly" — see section 3 (`:30515`).

> "If detained, the Watch releases him within 24 hours — no grounds to hold a witness." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:68`

> "If the characters ... a Watch patrol comes" — no source. Corylus clears charges against his crooked veterans (`:30365`, section 3).

> Staget's refusal: "If the characters ask for the Watch's help in locating Floon, Staget makes it clear that he won't send a force into the sewers in search of someone who might well be a Zhent or Xanathar Guild spy." — `sources/adventure-wdh.json:2196`

**5e. Arrest procedure (adventure, with campaign and Alexandrian companions)**

> "Characters who overtly engage in criminal behavior are quickly cornered and arrested by members of the City Watch. Those charged with committing a crime are brought before a magister to be judged. Advocates might intercede on behalf of the characters if they have allied themselves with influential NPCs and factions." — `sources/adventure-wdh.json:970`

> "The first approach is to roleplay the encounter with the arresting officers of the City Watch. The benefit of this approach is that characters can choose to go quietly or resist. The drawback is that the encounter might devolve into a fight-or-flight situation, leading to one or more characters becoming fugitives." — `sources/adventure-wdh.json:981`

> "Two {@creature veteran||veterans}, members of the City Watch, are here at all times." — `sources/adventure-wdh.json:10502` (Castle Ward courthouse, area H9 "Watch Wagon"; the cell block is H8 at `:10476`, "Two {@creature guard||guards} are stationed in this hall at all times.")

> "The magister has already heard the testimony of the arresting officers, as well as that of any eyewitnesses. The characters are given an hour to plead their case while he asks questions. ... A character who loses this contest is found guilty of hampering justice, locked up for a tenday, and fined 200 gp, on top of any other punishments meted out for crimes committed against the city and its citizenry. Those who can't or won't pay the fine are sentenced to hard labor for a year in Amendsfarm, a City Guard-run labor camp among the farms of Undercliff." — `sources/adventure-wdh.json:10592`

> "Hampering justice by concealing evidence can result in a fine of up to 200 gp and hard labor for up to a tenday." — `sources/adventure-wdh.json:4516`

> "visitors need her written permission to see him" — `sources/adventure-wdh.json:10623` (Castle Ward courthouse; magister's written permission for a visit to a prisoner)

> "In Waterdeep, withholding evidence from a Watch investigation is a criminal offense." — `sources/Act_III_Arc_D.md:129`

> "Hanging on the west wall are tasseled banners depicting the coats of arms of the City of Waterdeep, the Waterdeep City Watch, and the Waterdeep City Guard..." — `sources/adventure-wdh.json:10443` (not an arrest rule; a courthouse decoration)

Amendsfarm operator conflict: see C14.

**5f. Factions Guide rules that name the Watch (mechanics already in the campaign; the new page should cross-reference, not repeat, unless the orchestrator decides to)**

- Gray Hand: "City Watch officers who see the letter are Friendly." — `campaign/guides/factions/06-force-grey.md:58`
- Cloak: "Watch officers treat you as a trusted civilian informant and can overlook one minor infraction once per tenday." — `campaign/guides/gm-guide/player-factions-overview.md:67`; Factions Guide form: "a Watch officer overlooks one minor infraction by the member" — `campaign/guides/factions/03-lords-alliance.md:66`
- Stingblade: "You can read the City Watch's files. Standard files take one hour, and classified files take four hours and a DC 12 Charisma (Persuasion) check." — `campaign/guides/gm-guide/player-factions-overview.md:69`
- Warduke: "four **Warrior Veterans** from the Watch fight beside you in one operation on the surface." — `campaign/guides/gm-guide/player-factions-overview.md:70`
- Assist the City Watch in a crisis: "Aid the Watch in any situation beyond its capacity, such as monsters, organized assault or mind-controlled citizens. Once per incident." — `campaign/guides/factions/03-lords-alliance.md:55`
- High Harper, Watch cooperation: "It can be Watch cooperation for an operation, a hearing before the Lords' Court, or a warrant of immunity for one person." (`campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:363`) and "Three days after Mirt accepts, he delivers a sealed instruction to the responsible Watch station. It gives the member access to the relevant Watch records and assigns a liaison who coordinates the Watch's existing resources for that operation. It does not raise a new squad or put the member in command." (`ev-01-high-harper.md:377`)
- Bregan D'aerthe Commander: "passage in or out of Waterdeep without City Watch knowledge" — `campaign/guides/factions/08-bregan-daerthe.md:59`
- Structural rule: "Party actions that become visible citywide — Watch involvement, a public confrontation on a main thoroughfare — may reach several factions simultaneously, but covert intrusions rarely do." — `campaign/guides/gm-guide/structural-rules.md:20`
- Cassalanter leverage: "social and legal leverage as a first response, including threats of Watch involvement and reputation damage." — `campaign/guides/gm-guide/structural-rules.md:32`; and "Cassalanters exhaust city leverage first (Watch reports, noble complaints, guild sanctions), then infernal force" — `campaign/guides/gm-guide/running-the-villains.md:51`
- Doom Raiders: "a city where the City Watch already has their file." — `campaign/guides/factions/07-doom-raiders.md:20`

**5g. What the campaign's quest files already fix (for the Factions Guide's examples; not to be repeated as design)**

- **Fireball!** (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md`): five-minute window before the Watch seals the scene (line 9); Watch releases a detained witness within 24 hours (line 68); DC 13 Persuasion for supervised access to the bodies with Barnibus or Cromley (line 88); bodies go to the North Ward Watch Station by midmorning (line 38).
- **Gralhund Villa** (`campaign/quests/act-ii/gralhund-villa/`): Watch passes Saerdoun Street about every 20 minutes (`ev-02-saerdoun-street.md:33`); the Watch arrives at the front gate as Fel'rekt's team withdraws (`ev-04-the-zhentarim-raid.md:81`); by Ches 25 the Watch has sealed the villa and begun processing twenty-three bodies (`ev-09-aftermath.md:44`); "Davil Starsong ... held at Castle Waterdeep" two days later (`ev-09-aftermath.md:57`).
- **Finding Floon** (`campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md:63`): "Name Floon Blagmaar or Renaer Neverember as kidnapping victims → the Watch sergeant (DC 14 Charisma [Persuasion]) is skeptical but allows a brief supervised conversation with one cooperative prisoner."
- **Force Grey, The Legate's Eyes**: review rule, 14 days (`ev-02-the-extraction.md:186`).
- **Doom Raiders, Silencing Skeemo**: "the score decides whether the Watch opens a file." (`campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/design-notes.md:7`).
- **Trollskull Alley**: "City Watch manages pedestrian flow with professional exasperation." (`campaign/quests/act-i/trollskull-alley/ev-07-the-twin-parades.md:23`).
- **North Ward / Trollskull Manor**: "Ches 21–30, after the fireball ... 6: a City Watch patrol arrests a patron" (`campaign/guides/trollskull-manor/06-tavern-time.md:27`).

**5h. Gaps (Not found, mechanics)**

- No Watch-wide response-time table by ward. The source guide's line "City Watch response: jurisdiction, response time by ward, when they escalate to the City Guard, when they back down (noble involvement, political pressure), arrest procedures" (`SOURCE_GUIDE.md:263`) is not supported by `7. Other Response Teams.pdf` (see 5i).
- No rule for handover from Watch to Guard, and no escalation tiers for the Watch.
- No Open Lord response rule (the team exists only in the Alexandrian PDF).
- No stat block for a Watch variant in `adventure-wdh.json`, though `SOURCE_GUIDE.md:41` says Appendix B has "City Watch variants". Greps for "Watch Captain", "Watch Sergeant", "City Watch (veteran|guard|sergeant)" and a named Watch-variant heading returned no match.
- No Watch pay, recruitment or headcount in any source.

**5i. The SOURCE_GUIDE description against the PDF**

`sources/SOURCE_GUIDE.md:260-266` says of `7. Other Response Teams.pdf`:

> "**Contents:** Non-villain faction reactive groups — the City Watch, the Lords' Alliance Guard, the Gralhund private security, and miscellaneous reactors."
> "- City Watch response: jurisdiction, response time by ward, when they escalate to the City Guard, when they back down (noble involvement, political pressure), arrest procedures"
> "- Griffon Cavalry: when they deploy, what triggers aerial response"
> "- Lords' Alliance Guard: patrol routes, chain of command to Laeral Silverhand"
> — `sources/SOURCE_GUIDE.md:260`, `:263`, `:264`, `:265`

Against the PDF text (printed pp. 57–61, five pages):

- Printed p. 57 "PART 3D: OTHER RESPONSE TEAMS": the Gralhund Response Team. Printed p. 58 "OPEN LORD RESPONSE TEAM". Printed p. 59 "UNSEEN RESPONSE TEAM". Printed p. 60 "FREELANCERS" and "THE THREE URCHINS". Printed p. 61 the Urchins' continuation.
- **Not in the PDF:** a City Watch response section; jurisdiction; response time by ward; escalation to the City Guard; when the Watch backs down; arrest procedures; Griffon Cavalry deployment; a Lords' Alliance Guard; patrol routes.
- The only Watch text is the Open Lord team on p. 58 and the Gralhund remark that "the Watch" is absent from the PDF's Gralhund text.
- The source guide's "2. Other Factions.pdf" entry (`SOURCE_GUIDE.md:154`) is not supported either: the PDF (printed pp. 20–22) gives one Watch passage, the "blabbed to the City Watch" line on p. 21 (section 2). It has no jurisdiction, response time or arrest material.

**5j. Alexandrian Gralhund Villa PDF (`4. Gralhund Villa.pdf`), read in part**

The PDF's printed pp. 26–35 were read. The Watch appears three times:

> "Or bring the City Watch? Broadly speaking, if the compound seems threatened by armed force, similar responses will be taken."
> — `sources/4. Gralhund Villa.pdf`, printed p. 31

> "as the City Watch comes bursting into the house on the lower level."
> — `sources/4. Gralhund Villa.pdf`, printed p. 34

> "or for the City Watch to arrive?"
> — `sources/4. Gralhund Villa.pdf`, printed p. 34 (within "Do they end up fighting Fel'rekt's people on the roof and giving the Gralhunds a chance to escape or for the City Watch to arrive?")

No response clock was found in printed pp. 26–35. `SOURCE_GUIDE.md:193` says the file has a "Watch response and time pressure mechanic"; that mechanic may be on printed pp. 36 onward, which were not read. `[gap]`

---

## 6. Wiki lore worth a bullet

Wiki page titles and the editions its citations give. Wiki quotes keep markup and drop `<ref>` tags. The campaign rule is to paraphrase wiki lines with the edition tagged; these quotes are for the research record.

**W1. Organization and command (wiki, *City Watch (Waterdeep)*, cites *City of Splendors: Waterdeep* 3e and *City of Splendors (boxed set)/Campaign Guide* 2e):**

> "It had a centralized command led by the Commander of the Watch, who supervised three watchlords,<ref name=\"THO2004\">...</ref><ref name=\"PoF-p29\">...</ref> or senior commanders: the Mage Civilar in charge of the [[wizard]] corps; the Senior Armsmaster, who was in charge of supplies and reported directly to the Commander of the Watch; and the Grand Civilar, who commanded the ward civilars and held the same rank as the Mage Civilar. ... The Commander of the Watch reported directly to the [[Open Lord]]."
> — `sources/research/pass5-bundles/city-watch/wiki.txt:36` (the ellipsis is the wiki's own references; the rest of the line is quoted in W1 above)

Edition: this is the wiki's 2e and 3e lore, pre-campaign.

**W2. Ward civilars (wiki, same page):**

> "Each ward of Waterdeep was patrolled by a division of the Watch under the command of a ward civilar, or [[Generic City Watch major (Waterdeep)|major]], who oversaw all the senior civilars commanding the watch stations of their respective wards."
> — `wiki.txt:38` (cites *City of Splendors (boxed set)/Campaign Guide* 75–76, 2e; *City of Splendors: Waterdeep* 35, 3e; *Waterdeep: Dragon Heist* 198, 5e)

**W3. Badge of the Watch (wiki, same page, 15th century; cites *Waterdeep: Dragon Heist* p. 189, 5e):**

> "In the 15{{th}} century DR, officers who achieved the rank of captain were awarded a ''[[badge of the Watch]]'', a magic item that provided the wearer with additional protection against attacks and allowed the [[Open Lord]] to immediately know the wearer's location. Only the Open Lord could award ''badges of the Watch''."
> — `wiki.txt:84` (the 14th-century amulet of the Watch is on the same line, cites *City of Splendors: Waterdeep* 149, 3e)

**W4. Griffon Cavalry, 1479 DR and 1491–1492 DR (wiki, *Griffon Cavalry*; cites *Forgotten Realms Campaign Guide* 197, 4e; *Death Masks* ch. 5; *Waterdeep: Dragon Heist* 39, 5e):**

> "As of [[1479 DR]], however, the Griffon Cavalry had been disbanded for years, as the griffons died in combat but were never replaced."
> — `wiki.txt:226`

> "Then, in the {{YearlinkName|1491}}, Open Lord [[Laeral Silverhand]] proposed refounding the Griffon Cavalry, and threatened to make [[Mirt]] do it."
> — `wiki.txt:228`

> "Either way, this goal was achieved by the {{YearlinkName|1492}}, with the newly procured griffons continuing to be supplied by the Belabranta family."
> — `wiki.txt:228`

Campaign status: the 1479 DR disbandment is not used (`city-watch.md:45`), the 1491 DR refounding is used as "the wiki says" (`city-watch.md:47`).

**W5. 1479 DR fold of the Guard (wiki, *City Watch (Waterdeep)*; cites *Forgotten Realms Campaign Guide* 197, 4e, and *Downshadow* ch. 1 and 7):**

> "By [[1479 DR]], the [[City Guard (Waterdeep)|City Guard]] had been folded into the Watch, becoming a division of its organization. As the Guard was better equipped and trained, particularly dangerous tasks inside Waterdeep were given to the Guard instead, such as patrolling the [[Waterdeep/Sewers|sewers]] and [[Undermountain]]."
> — `wiki.txt:89`

Campaign status: rejected, "It is a 4e-era change, and Dragon Heist keeps two services in 1492 DR" (`city-watch.md:123`).

**W6. Watch posts and the Palace (wiki, *City Watch (Waterdeep)* and *Palace of Waterdeep*):**

> "There were multiple City Watch posts in Waterdeep. They were usually not located on the main streets, but were all identified by a green and gold lantern that hung outside, permanently lit by a ''[[continual flame]]'' [[spell]]."
> — `wiki.txt:78`

> "The Palace served multiple functions for the administration of the city. It was the main office for many of the city's officials including  [[City Watch (Waterdeep)|City Watch]], [[City Guard (Waterdeep)|City Guard]], and city clerks."
> — `wiki.txt:407` (*Palace of Waterdeep*, cites *City of Splendors: Waterdeep* 96, 3e)

**W7. Trembling horn (wiki, *City Watch (Waterdeep)*; cites *City of Splendors (boxed set)/Campaign Guide* 86, 2e):**

> "Many spellcasters within the City Watch were trained in the use of the spell ''[[trembling horn]]'', which was developed for the organization by [[Thyriellentha Snome|Thyri Snome]]. It allowed watchmen place an invisible, magical tracer that caused alarm-like effects that were widely recognizable among the Waterdhavian populace."
> — `wiki.txt:73`

**W8. Watch patrol size and sewer policy (wiki; the tactics line cites *City of Splendors: Waterdeep* 35 3e and the comic):**

> "When within the walls of Waterdeep, the City Watch typically patrolled in groups of four, with two patrolmen, one armar, and one civilar."
> — `wiki.txt:69`

**W9. Guard size (wiki, *City Guard (Waterdeep)*; cites *City of Splendors: Waterdeep* 33–34, 3e, and *City of Splendors (boxed set)/Campaign Guide* 75–76, 2e):**

> "The exact size of the City Guard was a secret only known to the [[Lords of Waterdeep]], but it was thought to be around 1,200 strong."
> — `wiki.txt:609`

> "members | = 1200 ([[1372 DR]])" — `wiki.txt:590` (infobox)

**W10. Watchful Order (wiki, *Watchful Order of Magists and Protectors*; cites *City of Splendors: Waterdeep* 30, 3e; *City of Splendors (boxed set)/Who's Who* 37, 2e):**

> "The Watchful Order of Magists and Protectors was the [[guild]] of [[wizard]]s and [[sorcerer]]s for the city of [[Waterdeep]]. However, while technically a guild, the Watchful Order functioned primarily as a mage academy."
> — `wiki.txt:312`

Leaders infobox: "[[Mhair Szeltune]] (c. [[1372]])<ref ...></ref><br/>[[Khondar Naomal]] (c. [[1479]]) ... [[Bowgentra Summertaen]] (c. [[1491]])" — `wiki.txt:291`.

**W11. Open Lord's titles (wiki, *Lords of Waterdeep*; cites *City of Splendors: Waterdeep* 53, 3e):**

> "They held a number of additional titles including [[City Guard (Waterdeep)#Ranks|Warden]] of Waterdeep, Overmaster of the [[Waterdeep#Guilds|Guilds]], and Commander of [[City Watch (Waterdeep)|the Watch]]."
> — `wiki.txt:485`

Campaign conflict C1.

**W12. The Captain's rule of thumb** (see section 3, `wiki.txt:62`).

**W13. Staff and rank names (wiki, *Generic City Watch* pages):** "A '''civilar''' was a member of the [[City Watch (Waterdeep)|City Watch]] of [[Waterdeep]], holding a rank equivalent to a lieutenant or captain." — `wiki.txt:872`. "An '''armar''' or '''amlar''' was a low-ranking member of the [[City Watch (Waterdeep)|City Watch]] of [[Waterdeep]], holding a rank equivalent to a sergeant." — `wiki.txt:808`.

**W14. Captain Jalester (wiki, *City Watch (Waterdeep)*; cites *Waterdeep: Dungeon of the Mad Mage* 10, 5e):**

> "* Captain [[Jalester Silvermane]]<ref name=\"WDMM5e-p10\">...</ref> ''circa ''[[1492 DR]]" — `wiki.txt:101`

Campaign conflict C10.

---

## 7. Conflicts between sources

Each conflict is paired, the higher-ranked source is named, and the choice is the orchestrator's. Ranking: campaign files outrank the published adventure, which outranks the wiki and the Alexandrian Remix markdown and PDFs where those disagree with the campaign's day-one choices.

**C1. Commander of the Watch and the Open Lord's titles.**
- Wiki: "They held a number of additional titles including [[City Guard (Waterdeep)#Ranks|Warden]] of Waterdeep, Overmaster of the [[Waterdeep#Guilds|Guilds]], and Commander of [[City Watch (Waterdeep)|the Watch]]." (`wiki.txt:485`)
- Adventure: "The Watch also includes a Senior Armsmaster, who reports to the Commander of the Watch and is in charge of supplies. The Commander of the Watch reports to the Open Lord, {@creature Laeral Silverhand|WDH}." (`sources/adventure-wdh.json:31886`)
- Higher: adventure (WDH) and campaign (`open-lord-and-masked-lords.md:107`).

**C2. Ward civilars: seven or one per ward.**
- Wiki: "Derek Windsfire: was The Grand Civilar in command of the seven ward civilars ''circa'' [[1372 DR]]" (`wiki.txt:94`).
- Adventure: "Major (ward civilar; one per city ward)" (`sources/adventure-wdh.json:31882`).
- Campaign: "Six wards fill the city, with the City of the Dead and the Field Ward beside them and Undermountain below." (`campaign/setting/geography/waterdeep.md:109`)
- Higher: adventure and campaign; the wiki is 1372 DR.

**C3. Guard and Watch as one service (1479 DR fold) against two services.**
- Wiki: "By [[1479 DR]], the [[City Guard (Waterdeep)|City Guard]] had been folded into the Watch, becoming a division of its organization." (`wiki.txt:89`)
- Adventure: "The first soldiers you see in service to the city will be the members of the City Guard who patrol the roads leading to Waterdeep, watch the walls, guard civic structures, and protect magisters. Waterdeep's streets, however, are policed by an altogether different force: the City Watch." (`sources/adventure-wdh.json:30545`); and "The City Guard is Waterdeep's army" (`:31817`).
- Higher: adventure and campaign (ruling, `city-watch.md:123`).

**C4. Griffon Cavalry size and leader in the wiki.**
- Wiki: "members = 100 (as of [[1372 DR]])" (`wiki.txt:205`); leader "[[Obryn Ironfist]] ([[1372 DR]])" (`wiki.txt:197`).
- Wiki: "* Lord [[Moedt Belabranta]]: Leader of the Griffon Cavalry ''circa'' [[1372 DR]]." (`wiki.txt:239`)
- Campaign: "Its present size is `[research]`." (`city-watch.md:47`)
- Higher: none for 1492 DR; the wiki's two leaders are both 1372 DR and conflict with each other.

**C5. The Griffon Cavalry, 1479 DR disbanded, 1492 DR flying.**
- Wiki: "As of [[1479 DR]], however, the Griffon Cavalry had been disbanded for years" (`wiki.txt:226`).
- Adventure: "Brave warriors of the City Guard light out from the Peaktop Aerie atop Mount Waterdeep, riding fearsome griffons that have been bred and trained for that purpose." (`sources/adventure-wdh.json:31171`)
- Higher: adventure (1492 DR, present tense).

**C6. Armed-force size: the Guard's 1,200 against the old outline's "1,200 guards across three shifts".**
- Retired outline: "**The City Watch**: 1,200 guards across three shifts; understaffed, overworked; not corrupt by default but susceptible to political pressure" (`campaign/structure/ch2-city-of-splendors.md:48`).
- Wiki (Guard): "it was thought to be around 1,200 strong." (`wiki.txt:609`)
- Adventure: patrol sizes only, "City Watch patrols are usually four to twelve persons strong." (`sources/adventure-wdh.json:31867`)
- Higher: none gives the Watch a total. Campaign: "No source gives the Watch's total strength, so this page gives none." (`city-watch.md:19`).

**C7. Crooked Watch officers against "trust in the Watch" and "most officers are not corrupt".**
- Adventure: "he has eight crooked members of the City Watch (human {@creature veteran||veterans}) crack down on them" (`sources/adventure-wdh.json:30365`).
- Adventure: "you can trust members of the City Watch to do their duty diligently" (`:30514`).
- Retired outline: "not corrupt by default but susceptible to political pressure" (`ch2-city-of-splendors.md:48`).
- Campaign, untagged: "Most officers are not corrupt by rule and can be pressed from above." (`city-watch.md:79`) and "Most officers are not corrupt by rule." (`the-grand-game.md:37`, untagged; its only source is the retired outline).
- Higher: adventure facts win; the "not corrupt" phrase has no published source and should carry `[research]`.

**C8. Jalester: Watch captain or Lords' Alliance agent.**
- WDMM: "Volothamp Geddarm introduces the characters to a friend of his: a young captain of the City Watch named Jalester Silvermane." (`sources/adventure-wdmm.json:457`)
- Wiki: "* Captain [[Jalester Silvermane]]<ref ...></ref> ''circa ''[[1492 DR]]" (`wiki.txt:101`)
- WDH: "{@creature Jalester Silvermane|WDH} (see {@adventure appendix B|WDH|12}) is an agent of the Lords' Alliance who reports directly to {@creature Laeral Silverhand|WDH}." (`sources/adventure-wdh.json:1536`)
- Campaign NF: "**Affiliation:** Lords' Alliance" (`campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:6`)
- Higher: WDH and the campaign NF page. The WDMM and wiki readings are not used. Note: WDH itself says he carries a Watch badge (`:31617`).

**C9. Cromley: active sergeant or retired.**
- Adventure: "Twenty minutes after the explosion, a City Watch {@creature sergeant|WDH} named {@creature Saeth Cromley|wdh} ... escorts" (`sources/adventure-wdh.json:4444`).
- Adventure: "{@creature Saeth Cromley|wdh} is a retired {@creature sergeant|WDH} of the City Watch, a likable fellow" (`sources/adventure-wdh.json:32573`); and "a retired {@creature sergeant|WDH} of the City Watch who assists in many of his investigations." (`:31774`).
- Alexandrian Arc D: "Sergeant **Saeth Cromley** escorts **Barnibus Blastwind**" (`sources/Act_III_Arc_D.md:137`).
- Higher: the published adventure is internally split; the campaign files use "retired". The city-watch page's Draft Notes (`city-watch.md:127`) flags it for the user.

**C10. Barnibus: Watch or Watchful Order; magistrate or investigator; dwarf or human.**
- Adventure: "{@creature Barnibus Blastwind|wdh|Barnibus} works for the Watchful Order of Magists and Protectors, investigating crimes that involve the use of magic." (`sources/adventure-wdh.json:31774`)
- Campaign NF: "The campaign's **Stingblade** and **The Archer Above** events call him Magistrate Blastwind, a title the published adventure does not give him (campaign-only)." (`campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:29`)
- Alexandrian Arc D: "Barnibus — a soft-spoken, meticulous dwarf mage in an ink-stained coat" (`sources/Act_III_Arc_D.md:137`)
- Campaign NF: "*Illuskan human Watchful Order investigator, lawful good, he/him*." (`02-barnibus-blastwind.md:5`)
- Higher: adventure (investigator, no title); NF for race (Illuskan human). Arc D is stale (the-grand-game.md:392 says so).

**C11. Watchful Order's head.**
- Adventure: "Members of the Watchful Order are expected ... headed by the Blackstaff." (`sources/adventure-wdh.json:30578`: "...are required to register with the city, and will be strongly encouraged to join the Watchful Order of Magists and Protectors, headed by the Blackstaff.")
- Wiki: "[[Bowgentra Summertaen]] (c. [[1491]])" (`wiki.txt:291`)
- Alexandrian Arc D: "**Bowgentra Summertaen**, Lady Master of the Watchful Order of Magists and Protectors" (`sources/Act_III_Arc_D.md:467`)
- Higher: adventure. Campaign draft (`city-watch.md:129`) says both can be true.

**C12. Amendsfarm operator.**
- Adventure: "a prison farm run by the City Watch (called Amendsfarm)" (`sources/adventure-wdh.json:31125`).
- Adventure: "Those who can't or won't pay the fine are sentenced to hard labor for a year in Amendsfarm, a City Guard-run labor camp among the farms of Undercliff." (`:10592`).
- Higher: both are the adventure; the campaign leaves the operator open (`code-legal-and-magisters.md:97`).

**C13. Watch sewers.**
- Wiki: "They never acted outside the walls of the city and did not pay much attention to the city's sewers." (`wiki.txt:64`).
- Adventure: Sewer keys held by captains (`:11626`), and the Watch's "Keep the blood off the streets" saying (`:2202`) — both fit "not much attention", but the adventure also has the Watch arrest people after they come up from the sewers (`:10534`: "After obtaining the {@item Stone of Golorr|WDH}, the characters are arrested by the City Watch soon after they emerge from the sewers.").
- Higher: adventure. Not a real conflict; the wiki's "walls" claim is wiki-only.

**C14. Who seals the fireball scene.**
- Adventure: "before the City Guard arrives and cordons off Trollskull Alley" (`sources/adventure-wdh.json:4427`).
- Campaign journal: "The party has five minutes before the Watch seals the scene and controls access." (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:9`).
- Higher: adventure for the Guard's role; the campaign journal's own line 36 says "six City Guard soldiers arrive and seal the alley" and the Watch arrives 20 minutes later. Minor.

**C15. Gralhund response team: Guard captain or Watch sergeant.**
- Adventure: "The Watch sends a {@creature mage} and six {@creature veteran||veterans} (one {@creature sergeant|WDH} and five constables)" (`sources/adventure-wdh.json:4870`).
- Campaign area overview: "1 mage + 6 veterans" (`campaign/locations/gralhund-villa/area-overview.md:103`).
- Alexandrian Arc E: "A Watch response team (a Mage, six Warrior Veterans, and a Guard Captain)" (`sources/Act_III_Arc_E.md:774`).
- Higher: adventure and campaign. Arc E's "Guard Captain" disagrees.

**C16. Tashlyn's cover rank.**
- Adventure: "Tashlyn has established a useful cover by serving as a bodyguard to Vorondar Levelstone, a dwarf magister stationed at the South Gate. ... allowing her to reach the rank of captain in the City Guard." (`sources/adventure-wdh.json:31955`)
- Campaign NF: "Calishite bodyguard to a dwarf magistrate at the South Gate" (`campaign/setting/notable-figures/doom-raiders/05-tashlyn-yafeera.md:21`).
- Campaign city-watch: "She holds the rank of captain in the City Guard as cover and watches the traffic through the South Gate." (`city-watch.md:69`)
- Higher: adventure and NF (bodyguard is the cover; the captaincy is earned through it). `city-watch.md:69` inverts it. Ruling 18 says follow the NF.

**C17. Vajra's alignment.**
- Campaign NF: "*Tethyrian human archmage, lawful neutral, she/her*." (`campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:5`)
- Campaign city-watch: "**Vajra Safahr** (Neutral, Tethyrian Human, she/her)" (`city-watch.md:63`).
- Higher: NF.

**C18. Savra's alignment.**
- Campaign NF: "*Tethyrian human knight, neutral good, she/her*." (`campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md:5`)
- Adventure: "Savra ... NG Tethyrian human" (`sources/adventure-wdh.json:3949`/`:3950` — the text at 3950 is "The Belabrantas are a Waterdavian noble family that raises griffons for the Griffon Cavalry."; the NG line is at the adventure's Appendix B and the city-watch draft cites 3949).
- Campaign city-watch draft: "her Notable Figures page says lawful good" (`city-watch.md:133`) — that is wrong (see S1).

**C19. Gondafrey's alignment.**
- Campaign NF: "lawful good / chaotic evil (set by time of day)" (`independents-allies/18-lady-gondafrey.md:5`).
- Campaign city-watch: "**Lady Gondafrey** (Lawful Good, Gargoyle, she/her)" (`city-watch.md:67`) — omits the time-of-day shift.
- Higher: NF.

**C20. Field Ward: no Watch vs a campaign Watch house.**
- Adventure: "The Watch doesn't patrol this area, however, and many crimes go uninvestigated." (`sources/adventure-wdh.json:31104`)
- Campaign: "The campaign also has a Watch house in the ward. This page keeps Dragon Heist's rule as the base: the Watch does not patrol, and the house sends Guards only after a report or for a planned operation." (`campaign/gazetteer/waterdeep/field-ward.md:146`)
- Higher: adventure, and the campaign keeps the rule. The "house sends Guards" wording mixes Guard and Watch (see S16).

**C21. Trust in the Watch against the Field Ward and the sewers.** Fits the adventure, no conflict.

**C22. Cressa Galavarco and Hyustus Staget: Staget's fate.** Adventure: "If Hyustus has died for whatever reason, replace him" (`:17873`). Campaign city-watch: "If he has died, the published adventure replaces him with Cressa Galavarco" (`city-watch.md:71`). No conflict; the replacement is conditional.

**C23. Watch escort and the Lords' Alliance.**
- Adventure: "City Watch officials are notified that the characters are on \"official business\" for the Lords' Alliance and instructed to provide support whenever they can." (`sources/adventure-wdh.json:1390`)
- Campaign Lords' Alliance: "Jalester's field reports and the Watch's contacts..." (`factions/03-lords-alliance.md:9`). Fits.
- Appendix B: "Jalester will request a City Watch escort of two **guards** for one dangerous errand per tenday." (`sources/Appendix_B_-_Player_Factions.md:253`). The Alexandrian Redknife rank benefit; the campaign's Redknife page is not checked here.

**C24. Who runs the fireball's Watch response: Barnibus and Cromley.** Fits.

**C25. Watch informants.**
- Campaign, tagged research: "**Informants:** The Watch has informants in every ward `[research]`, and every faction has informants in the Watch `[research]`." (`the-grand-game.md:29`)
- Campaign, untagged: "The Watch has informants in every ward, and every faction has informants in the Watch." (`city-watch.md:79`)
- Campaign draft: "The one sourced Watch informant is Gosta Ironhelm" (`the-grand-game.md:90`).
- Higher: the tagged reading. `city-watch.md:79` needs the tag.

**C26. Griffon Cavalry duty: "trained to stay above the rooftops" vs aerial displays.** Fits.

**C27. Gods' Day Watch.** No conflict.

**C28. Laeral's office: "a few years ago" vs "about three years before the campaign".**
- Adventure: "a few years ago" (open-lord page cites `adventure-wdh.json:452`).
- Campaign history: "Laeral Silverhand became Open Lord about three years before the campaign" (`campaign/setting/history/07-a-city-watching-itself.md:22`).
- Higher: the history page's "about three years" is the derived date (`07-a-city-watching-itself.md:16`). Not Watch-specific; listed because the Watch's chain runs through her office.

---

## 8. Stale or contradicting lines in other campaign files

**S1.** `campaign/setting/governance-and-guilds/city-watch.md:133` says "her Notable Figures page says lawful good". Savra's Notable Figures page says "*Tethyrian human knight, neutral good, she/her*." (`campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md:5`). Stale.

**S2.** `city-watch.md:131` cites `ev-01-the-fireball.md` line 196 for Jalester's "standard Watch inspection protocols". The line is 192: "Jalester mentions without pressure that the Sea Maidens Faire uses private docking arrangements that circumvent standard Watch inspection protocols." (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:192`). Wrong line.

**S3.** `city-watch.md:124` cites `wiki.txt` lines 170 and 189 for the Guard's "1200 (1372 DR)". The line is 590 (infobox: "members = 1200 ([[1372 DR]])") and 609 (the 1,200 secret text). Lines 170 and 189 are the *Waterdeep Watch* infobox and the *Griffon Cavalry* heading. Wrong lines.

**S4.** `city-watch.md:128` says the wiki (`wiki.txt` line 101) calls Jalester "a young captain of the City Watch". The wiki line says only "Captain Jalester Silvermane ... circa 1492 DR". The phrase "a young captain" is in `sources/adventure-wdmm.json:457`. Wrong citation.

**S5.** `city-watch.md:129` cites `wiki.txt` line 308 for Summertaen as leader around 1491 DR. The leader infobox is at line 291 (`wiki.txt:291`). Wrong line.

**S6.** `city-watch.md:132` says the Warden's 1491 DR appointment "after Ezender Drayth's murder is wiki-only (`wiki.txt` lines 162 and 266)". Line 162 is a field of the *Waterdeep Watch* infobox and 266 is the *Griffon Cavalry* appendix. The only Ezender Drayth line in this bundle is the Guard's leader list at `wiki.txt:582` ("[[Ezender Drayth]] ([[1491 DR]])"). The bundle has no "murder" line. Wrong citation; the murder claim is not in the bundle.

**S7.** `campaign/setting/history/01-ahghairons-gifts.md:58` says "The wiki says Ahghairon restructured Raurlor's army and navy into the City Watch and the City Guard." The Watch and Guard wiki pages in this bundle have no Raurlor or navy text (grep for Raurlor and Ahghairon returns only `wiki.txt:222` and `:488`). The page cites "City of Splendors boxed set Campaign Guide p. 30, 2e" via *History of Waterdeep*, which is not in the bundle. `[gap]`. The same claim appears at `city-watch.md:49` and `history/01:24`.

**S8.** `campaign/setting/history/01-ahghairons-gifts.md:61` and `:133` call the Code Legal and the City Watch "protections built against tyranny" (tagged `[research]` at :61 and at :133 "the old claim"). Retired outline.

**S9.** `campaign/guides/gm-guide/design-notes-running-the-campaign.md:121` calls Orvyn Dall a "Watch appeals clerk". The Trades Ward gazetteer and the event say he is an appeals clerk in the district magistracy: "The appeals office of the ward's district magistracy employs four clerks." (`campaign/gazetteer/waterdeep/trades-ward.md:93`) and "Orvyn Dall is an Illuskan Human appeals clerk in the Trades Ward district magistracy." (`ev-01-the-legates-eyes.md:17`). Stale.

**S10.** `campaign/guides/factions/07-doom-raiders.md:15` says "Tashlyn's City Guard position" and `campaign/structure/` ... `campaign/setting/history/04-the-founding-of-chains.md:58` says "Tashlyn serves as Captain of the City Guard at the South Gate under the dwarf magister Vorondar Levelstone." Both leave out the bodyguard cover (`sources/adventure-wdh.json:31955`). Stale in the same sense as C16.

**S11.** `campaign/gazetteer/waterdeep/field-ward.md:146`: "the house sends Guards only after a report or for a planned operation" — the Watch house sends Guards, mixing the two services (see C20).

**S12.** `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:29` calls him "Magistrate Blastwind", a title the adventure does not give (`sources/adventure-wdh.json:31774`). Campaign-only, tagged in the NF page itself; the Stingblade event repeats it (`ev-01-stingblade.md:122`, per the code-legal draft).

**S13.** `campaign/setting/the-grand-game/the-grand-game.md:37` carries "Most officers are not corrupt by rule" without a tag (source: retired outline `ch2-city-of-splendors.md:48`). Also `city-watch.md:79` says the same untagged.

**S14.** `campaign/setting/organizations/04-order-of-the-gauntlet.md:60` says the Watch "closed every complaint against the family without findings". The Sea Ward gazetteer says the same of "one Sea Ward family", and `sea-ward.md:156` says "In **Stingblade** the Lords' Alliance's Watch household inquiries file holds three closed inquiries against one unnamed Sea Ward house" (campaign-only; the Stingblade event file is not checked here). Campaign-only facts about closed inquiries are suspicion, consistent with ruling 7.

**S15.** `campaign/gazetteer/waterdeep/sea-ward.md:156`: "Every sergeant in the ward knows the Watch posts a guard at the Cassalanter service gate." Campaign-only; reads as Watch knowledge of the family's gate, which is suspicion only. Brief ruling 7 requires suspicion; this sentence reads as fact. Flag for the orchestrator.

**S16.** `campaign/setting/governance-and-guilds/city-watch.md:84` says "A High Harper can ask Mirt for Watch cooperation, which delivers a sealed instruction to the responsible station three days after Mirt accepts" — matches `r50-high-harper/ev-01-high-harper.md:377`. Not stale. Listed because the page then says "raises no new squad", which matches the event text. OK.

**S17.** `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:9` says "the Watch seals the scene"; line 36 says the City Guard does. See C14.

**S18.** `sources/Act_III_Arc_D.md:500` gives "Watch Authority: A Renown of 1+ in any faction, or a Watch badge obtained during the crime scene, automatically gains entry." (Dalakhar's room at the Inn of the Dripping Dagger). The campaign uses a badge only for Jalester. The Watch badge being obtainable at a crime scene is an Alexandrian Arc D rule, and it conflicts with the wiki's "Only the Open Lord could award badges" (`wiki.txt:84`) and with the adventure's single badge (`:31617`). Flag.

**S19.** `campaign/structure/ch2-city-of-splendors.md:34`, `:46`, `:48`, `:56`, `:88`, `:154`, `:158`, `:244`: retired outline lines about the Watch ("City Watch headquarters"; "1,200 guards across three shifts"; "City Watch captain is a worshiper"). The brief says retired outline files are not used. Listed because these lines still exist in `campaign/structure/`.

**S20.** `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:7` says a massacre invites "City Guard, the Watchful Order, and potentially Vajra Safahr personally", while `02-operating-costs.md:83` says a Watch patrol answers any disturbance within the hour. Both coexist in the sources. Not a conflict, but the Factions Guide should say which force answers a massacre and which answers a disturbance.

**S21.** `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md:27` says "a former sergeant of the City Watch (confirmed rank; not Watch Commander despite some in-text references)". The "in-text references" to Commander are not in this bundle; they may be in the Fireball journal or Arc D. Not checked further.

**S22.** `campaign/setting/organizations/02-lords-alliance.md:61` says Laeral "does not know the Stone has resurfaced". `history/07` line 52 says the same. Consistent.

**S23.** `campaign/setting/the-grand-game/the-grand-game.md:35` tags "genuinely trying" but `city-watch.md:79` gives "The Watch is trying to do its job, and it knows that some cases are politically untouchable." untagged. Tag mismatch (S13 family).

**S24.** `campaign/guides/gm-guide/player-factions-overview.md:173` names "Sergeant Marek Dunmere" as the Watch officer who receives Bregan D'aerthe names. `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/design-notes.md:33` says "no Notable Figures page exists for him", consistent. Not stale; campaign-only.

---

## Not found (search terms and files)

- Watch headcount, pay, recruitment: searched `city-watch.md`, `adventure-wdh.json` (Watch, City Guard, "1,200"), wiki bundle. None.
- Per-ward response time: searched adventure JSON for "minutes" near "Watch"; found only per-location times (5b). The source guide's "response time by ward" is absent from the PDF.
- Watch-to-Guard handover: searched adventure JSON for "City Guard" (lines 3734, 3739, 3749, 4410, 4427, 7765, 8288, 14837, 26765, 30388, 31817-31846, 10592, 31125, 26657) and both PDFs. Only the fireball and Kolat instances.
- Open Lord response rule in campaign: `open-lord-and-masked-lords.md:113`, and grep of `campaign/` for "Open Lord response". None.
- Watch stat block variant in `adventure-wdh.json`: none (grep "Watch Captain", "Watch Sergeant", "City Watch (veteran|guard|sergeant)", and case-insensitive "griffon cavalry rider" for an Appendix B entry). The fireball scene's "Griffon Cavalry rider (see Appendix B)" (`sources/adventure-wdh.json:4427`) points to an entry the grep did not locate.
- Griffon Cavalry size in 1492 DR: none (`city-watch.md:47` `[research]`).
- Commander of the Watch in 1492 DR: none.
- Watch headquarters building: none (wiki and adventure both say the Palace; `city-watch.md:122`).
- Watch pay, rank promotions, badge rules beyond Open Lord awards: wiki 14th-century amulet and 15th-century badge only (`wiki.txt:84`).
- Watch in ships or the harbor inspection: only campaign `ev-01-the-fireball.md:192` ("standard Watch inspection protocols"), and the GM Notes say no source supports ship inspection.
- Navy size, ships, commander: `city-watch.md:49` `[research]`; not in bundle.
- Watch informant network: only Gosta (`Appendix_D_-_Running_the_Tavern.md:159`) and Myl's record-keeping (`21-myl-dunpier.md:21`).
- Watch in the Dock Ward shore: wiki-only past tense, not in this bundle (`campaign/gazetteer/waterdeep/dock-ward.md:81`).
- Watch under Lady Gondafrey's rank: `Captain` in campaign NF; adventure gives "served in the City Watch" (`:28506`).
- Watch's own sworn oath or doctrine text beyond the code of conduct: none.

## Not readable

- `sources/4. Gralhund Villa.pdf`: read in printed pp. 26–35 only (section 5j). Pp. 36 onward not read. `SOURCE_GUIDE.md:193` lists a "Watch response and time pressure mechanic" for the Gralhund Villa file, so the rest needs reading.
- `.docx` files in `sources/Other remix files/`: not consulted. `SOURCE_GUIDE.md` does not name any .docx as covering the Watch (its City Watch entries are the two PDFs, the adventure Ch. 9, and the Gralhund and Watch mapping at lines 719–735).
- `2. Other Factions.pdf` and `7. Other Response Teams.pdf` were read from the Read tool's rendered output. `pdftotext` was not run (no shell tool in this session). Both were read in full (3 and 5 pages).
