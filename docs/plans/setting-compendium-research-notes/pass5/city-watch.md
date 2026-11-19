# Pass 5 research notes: City Watch (slug `city-watch`)

Scope: the City Watch as the Open Lord's police apparatus and a Grand Game participant. Organization page (lore, `campaign/setting/organizations/`) plus Factions Guide page (mechanics, `campaign/guides/factions/`). Day-one state is Ches 1, 1492 DR (brief ruling 28).

Method and limits. This session had no shell tool, so `pdftotext` was not run. Both Alexandrian PDFs and the first 11 pages of `4. Gralhund Villa.pdf` were read through the Read tool, and PDF citations use the printed page numbers. Wiki quotes keep the wikitext's `[[ ]]` and `{{ }}` markup and drop `<ref>` citation tags; the text is otherwise as in the file. Adventure quotes keep the `{@creature …}` tags as written. Line numbers for `adventure-wdh.json` and `adventure-wdmm.json` were checked by Read or Grep against the file; the bundle's `adventure-hits.txt` and `campaign-hits.txt` line numbers match the files.

Main gaps: no Watch headcount, no per-ward response time, no rule for the Watch handing over to the City Guard, no Open Lord response rule in the campaign, no Watch escalation tiers, and no 1492 DR Commander of the Watch. The Factions Guide page must build its response rules from the adventure's scene text and the campaign's own quest files.

---

## 1. Already settled on the governance pages

The governance pages are `campaign/setting/governance-and-guilds/city-watch.md`, `open-lord-and-masked-lords.md`, `code-legal-and-magisters.md` and `guilds.md`. The new organization page cross-references `city-watch.md` and does not duplicate it.

**What `city-watch.md` settles (lore; a structuring draft):**

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
> — `campaign/setting/governance-and-guilds/city-watch.md:45` (the paragraph also carries the wiki's 1,400 garrison, the 1,200 Guard figure and the 1479 DR fold, each tagged in the file)

> "The Cavalry is a special branch of the City Guard whose riders are veteran soldiers who fly griffons from the Peaktop Aerie atop Mount Waterdeep."
> — `campaign/setting/governance-and-guilds/city-watch.md:47` (the paragraph continues with the ring of feather falling, the Belabranta family, the wiki's 1479 DR disbandment and the 1491 DR refounding; "Its present size is `[research]`.")

> "Waterdeep requires arcane spellcasters who plan to stay to register with the city, and it strongly encourages them to join the Watchful Order, which the published adventure says the Blackstaff heads."
> — `campaign/setting/governance-and-guilds/city-watch.md:51` (the paragraph continues with the Order's services, its wiki status and the guild link)

Governance pages on the Open Lord and the courts:

> "**Who answers to the Open Lord:** The Commander of the Watch reports to the Open Lord. So does Elminster, the current Warden of Waterdeep. When a problem is beyond diplomats and the city's other armed forces, the Open Lord can mobilize **Force Grey**, which is usually a last resort. Only the Open Lord can strip **Vajra Safahr** of her title as Blackstaff."
> — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:30`

> "**From arrest to judgment:** The City Watch arrests a suspect and brings them to a courthouse, where they are detained until a magister can pass judgment. The published adventure says a magister can pass a sentence without a trial. Advocates may speak for a party that has allied itself with influential NPCs and factions, and a party that has joined the Lords' Alliance is more likely to be excused if Laeral Silverhand has cause to let them off."
> — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:31`

> "Each courthouse has two guards outside both the front door and the back door at all hours, barred windows, a front desk clerk, cells and a courtroom."
> — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:32`

> "The Watch opens a review of a magistracy, in **The Legate's Eyes**, when a Force Grey extraction goes wrong, and for 14 days it logs every Tower request to the Watch."
> — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:57` (campaign-only rule, labelled as such in the file)

**What the Alexandrian files add that the governance pages do not carry:**

- The Open Lord response team (1 veteran, 4 guards, possibly an apprentice wizard; a Medium encounter by design), `sources/7. Other Response Teams.pdf` printed p. 58. The governance pages leave it out on purpose: `open-lord-and-masked-lords.md:113` says "The campaign has no Open Lord response rule, and the team is left out until the user wants one." See section 5a.
- The line that information reaching the City Watch is the likeliest route to the Open Lord (`sources/2. Other Factions.pdf`, printed p. 21). It is in `campaign/setting/the-grand-game/the-grand-game.md:88` (Draft Notes) and not in the body of `city-watch.md`. `city-watch.md:135` mentions it only in its Draft Notes.
- Nothing else. `city-watch.md:135` says "The Alexandrian files add nothing sourced."

---

## 2. Day-one lore (Ches 1, 1492 DR)

**The Watch as a Grand Game actor**

> "The Watch is genuinely trying, most of the time `[research]`, and it knows that some cases are politically untouchable `[research]`. The published adventure says a visitor can trust the Watch to do its duty diligently, and that its strict code of conduct makes it one of the most trusted police forces outside paladin-patrolled Elturgard."
> — `campaign/setting/the-grand-game/the-grand-game.md:35`

> "Most officers are not corrupt by rule. The published adventure names eight crooked Watch veterans in one Masked Lord's pay, which is a handful against a force whose code the same text praises. The officers are susceptible to pressure from above `[research]`, and the GM Notes of **The City Watch** list the cases where that pressure shows."
> — `campaign/setting/the-grand-game/the-grand-game.md:37` (the "not corrupt by rule" sentence is untagged; its only source is the retired outline, `campaign/structure/ch2-city-of-splendors.md:48`, which reads "not corrupt by default but susceptible to political pressure")

> "The Watch is also how the government learns things. Laeral Silverhand's information comes largely from the Watch and from Jalester Silvermane, and it runs about three moves behind the factions (see **A City Watching Itself**). Whatever a party tells the Watch is the likeliest route by which she learns what is happening, though she may never learn all of it."
> — `campaign/setting/the-grand-game/the-grand-game.md:39`

> "**Informants:** The Watch has informants in every ward `[research]`, and every faction has informants in the Watch `[research]`."
> — `campaign/setting/the-grand-game/the-grand-game.md:29`

**Laeral's information and what she believes**

> "Her intelligence comes from Jalester Silvermane and the Watch, and it is about three moves behind. The party's reports, most of all those carried by the Lords' Alliance, are what bring her up to date."
> — `campaign/setting/history/07-a-city-watching-itself.md:26` (Lore Summary; the file line opens with "> - ")

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
> — `campaign/guides/factions/03-lords-alliance.md:9` (Factions Guide, Grand Game Stance; the day-one state sits on the mechanics page)

> "- **Laeral's intelligence:** Laeral believes the vault is in Neverwinter, and she does not know the Stone has resurfaced or that four villain factions are active. Her information comes largely from the Watch and from Jalester, and it runs about three moves behind the factions."
> — `campaign/setting/organizations/02-lords-alliance.md:61`

> "OPEN LORD: The Open Lord of Waterdeep isn't exactly a "minor" faction, but Laeral Silverhand is considerably behind the curve in the current Grand Game."
> — `sources/2. Other Factions.pdf`, printed p. 21 (PDF page 2)

> "The most likely avenue for that to change — and potentially change rapidly — is through information blabbed to the City Watch. This could happen as early as Scenario 1 (depending on exactly what Renaer and/or the PCs report to the watch), but it's quite possible for the Open Lord to never fully twig to what's happening."
> — `sources/2. Other Factions.pdf`, printed p. 21 (PDF page 2)

**How information reaches the Watch and then Laeral**

> "Jalester reads the Watch's file ledger each tenday, so he learns what a Stingblade asked for."
> — `campaign/guides/gm-guide/player-factions-overview.md:111` (the row continues with the Stingblade mechanic)

> "He carries a badge of the City Watch and reads the Watch's file ledger each tenday, and he is grieving his partner, Faerrel Dunblade, who died last year exposing a plot against the government, and he fills the silence with work."
> — `campaign/setting/organizations/02-lords-alliance.md:66`

**Watch informants and sources in the city**

> "Gosta moonlights as an informal Watch informant — not a spy exactly, more a civic-minded citizen who has been filing regular reports on \"establishments of interest\" for the better part of a decade. He considers this entirely compatible with his employment. He doesn't report anything actionable; he reports atmospherics — who comes in, how often, whether the crowd skews toward any particular guild or faction. The Watch values him precisely because he is boring and consistent."
> — `sources/Appendix_D_-_Running_the_Tavern.md:159`

> "**Faction Note:** Informal City Watch informant. Not a planted spy — this is his own civic arrangement, predating any party involvement."
> — `sources/Appendix_D_-_Running_the_Tavern.md:163`

> "Deep down, she keeps meticulous records not out of professional pride but because the Watch has stopped by twice this year asking similar questions, and she finds it less trouble to have the answers ready."
> — `campaign/setting/notable-figures/independents-allies/21-myl-dunpier.md:21`

> "- **The Watch has a file:** The City Watch already keeps a file on the cell, so Davil's people avoid anything that invites scrutiny. The cell operates openly, meets in taverns and recruits adventurers, and its fronts are ordinary businesses."
> — `campaign/setting/organizations/06-doom-raiders.md:65`

> "Zhentarim crews with flying snake tattoos work Waterdeep's back streets, and they are hostile to Davil Starsong's Doom Raiders. The crews take prisoners, and the Watch has arrested a few of them in street brawls. None of them will say who gives the orders, and street talk says one master stands behind them."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:61`

**Where the Watch's reach stops**

> "The Watch doesn't patrol this area, however, and many crimes go uninvestigated."
> — `sources/adventure-wdh.json:31104` (the rest of the passage: "The City Guard oversees the Field Ward from the walls around it, but its members get involved only when folk moving into or out of the city are threatened.")

> "Its roots lie in Skullport, an outlaw port in the caverns below the city, reached through Undermountain and outside the Watch's jurisdiction, which Netherese wizards built long ago and which many masters have held since."
> — `campaign/setting/history/02-the-long-shadow.md:76`

> "The Field Ward is Waterdeep's slum, an unofficial ward of mud, tanneries and slaughterhouses between the two northernmost walls, outside the city proper and beyond the reach of the Watch."
> — `campaign/gazetteer/waterdeep/field-ward.md:17`

> "Note, however, that because both these areas have yet to be formally accepted as wards of the city, they don't benefit from the securities of Guild Law or the protection of the Watch."
> — `sources/adventure-wdh.json:30444` (the Field Ward and Undercliff)

**The Watch's view of the Cassalanters (suspicion only, brief ruling 7)**

> "Everyone outside the household and the cult only suspects the family, because it is too nice to be this rich and this purebred. Savra Belabranta of the **Order of the Gauntlet** has no legal evidence, Mirt suspects Cassalanter money stood behind the Howling Hatred cult, and Vajra Safahr of **Force Grey** has scried conjuration and abjuration residue beneath the villa. The Lords' Alliance has no proof, the Watch has closed three complaints against the house, and the Emerald Enclave senses infernal influence in the Southern Ward without knowing whose it is."
> — `campaign/setting/villains/cassalanters.md:65`

> "The Watch has closed every complaint against one Sea Ward family without findings, according to the Order of the Gauntlet's files."
> — `campaign/gazetteer/waterdeep/sea-ward.md:156` (campaign-only; suspicion, not knowledge)

> "The City Watch has small, single-person \"watch boxes\" set up on nearly every street corner in the Sea Ward, including the intersection just outside the gates of Cassalanter Villa. If a guard sounds the alarm, the Watch member on duty fetches a force of forty City Watch {@creature veteran||veterans} to cordon off the property."
> — `sources/adventure-wdh.json:18579` (a fixture of the Sea Ward; the rest of the Cassalanter scene is quest text)

**Watch officers and NPCs in day-one lore**

- Commander of the Watch (1492 DR): no name in any source. `[research]`. The wiki names Captain Rulathon as Commander circa 1372 DR (section 6, W1 and section 4).
- Warden of Waterdeep (City Guard, not the Watch): "The current Warden of Waterdeep is Elminster, who answers to the Open Lord, {@creature Laeral Silverhand|WDH}." (`sources/adventure-wdh.json:31836`)
- Watch captains hold sewer keys: "City Watch captains hold keys to sewer access points that correspond with their assigned wards." (`sources/adventure-wdh.json:11626`)
- Captain Staget, Dock Ward: "Captain Staget is an uptight man who helps keep the peace in the Dock Ward." (`sources/adventure-wdh.json:2184`; full paragraph in section 3)
- Sergeant Cromley (retired): "confiding only in {@creature Saeth Cromley|wdh}, a retired {@creature sergeant|WDH} of the City  Watch who assists in many of his investigations." (`sources/adventure-wdh.json:31774`; the source has the double space)

---

## 3. Tenets (beliefs and habits that explain how the Watch acts)

Each tenet has its source. Where nothing supports a tenet, the entry says so under "Nothing supports".

**Keep the blood off the streets, not the sewers.** The Watch looks above ground.

> "\"Keep the blood off the streets, okay?\" (This is a common saying among City Watch officials, who care more about what happens in the city above than what happens in the sewers below.)"
> — `sources/adventure-wdh.json:2202`

> "Best not to meddle in criminal matters. Leave this dirty business to the City Watch."
> — `sources/adventure-wdh.json:2200` (said by Staget; the tenet is the Watch's only as far as this line goes)

> "The City Watch performed everyday policing duties. They never acted outside the walls of the city and did not pay much attention to the city's sewers."
> — `sources/research/pass5-bundles/city-watch/wiki.txt:64` (wiki, *City Watch (Waterdeep)*; the walls claim cites the comic *The Gathering*; the sewers claim cites *Waterdeep: Dragon Heist* p. 27. The walls claim is wiki-only.)

**Arrest quietly; the magister judges.**

> "The Watch makes every effort to take individuals into custody quietly, so as not to disrupt other citizens. Those bystanders generally return the favor by giving altercations between criminals and the Watch a wide berth."
> — `sources/adventure-wdh.json:30515` (the same paragraph says "floggings are carried out in the watch post nearest the sentencing")

> "People who are arrested by the City Watch are brought to a courthouse and detained until a magister can pass judgment on them. Each courthouse has the following features:"
> — `sources/adventure-wdh.json:9791`

**A strict code, kept by most.**

> "City Watch members follow a strict code of conduct that makes them one of the most trusted police forces aside from paladin-patrolled Elturgard. As long as you don't engage in unlawful behavior, you can expect to be left untroubled by the Watch."
> — `sources/adventure-wdh.json:30549`

> "As a rule, you can trust members of the City Watch to do their duty diligently, and you can expect that the city's magisters will be fair."
> — `sources/adventure-wdh.json:30514`

> "Corylus refuses to speak with the party. If the characters become an annoyance, he has eight crooked members of the City Watch (human {@creature veteran||veterans}) crack down on them, then uses his position as Masked Lord to clear any charges leveled against these Watch members."
> — `sources/adventure-wdh.json:30365` (the code is real and a few officers step outside it; the rest of the passage covers Corylus's entourage)

**Know the streets; the patrol is the Watch's tool.**

> "I guarantee that all members of the Watch know the streets they patrol and that area's residents better than you do, even if you stay in Waterdeep for ten seasons."
> — `sources/adventure-wdh.json:30546`

> "Small squads head out from the watch posts on daily and nightly rounds of the city streets, or on special assignments involving protection or investigation. A mere pair of Watch operatives might discreetly patrol in the Castle Ward; in contrast, squads of eight walk the Dock Ward, increasing to as many as a dozen at night. If Watch members spot trouble they can't handle, they blow shrill tin whistles to summon more of their members-an act that alerts nearby citizens as well."
> — `sources/adventure-wdh.json:30548`

**Posts are local headquarters and holding cells, marked by a light.**

> "The City Watch has watch posts throughout the city. These stations are often off the main thoroughfares, tucked away in small courtyards or at cross streets. A watch post can be recognized by the green-and-gold lantern outside it, lit even during the day with a {@spell continual flame} spell. A watch post serves as an organizational headquarters and armory. Anyone who wishes to report a crime may do so at a watch post in the event a Watch constable can't be found elsewhere. A watch post typically contains a few holding cells where people arrested for crimes can be detained until they're marched to a courthouse jail before standing trial."
> — `sources/adventure-wdh.json:30547`

**Search only those who make trouble.**

> "Characters who give up their visible weapons without a fuss aren't searched, but those who give the Watch a hard time are searched for hidden weapons (and stripped of anything that could potentially cause harm)."
> — `sources/adventure-wdh.json:10553`

**A search needs a warrant.**

> "Two City Watch constables spoke to Lord Gralhund. He assured them that no one had broken into the estate and that everything was fine. The constables had no grounds to get a search warrant, so they didn't pursue the matter."
> — `sources/adventure-wdh.json:4793` (Ch. 3 Gralhund scene; the rule is the Watch's, the scene is routed to **Gralhund Villa**)

**Trust in the Watch is the public line, and the officers say it.**

> "\"Trust in the Watch,\" Cromley adds dismissively."
> — `sources/adventure-wdh.json:4456` (Cromley in the fireball scene; the passage continues with the characters' DC 15 Charisma check)

**Doctrine and Rites (sourced; the sources leave the rites themselves open)**

- Watch slang: "\"What befalls?\" means \"Someone tell me what's going on here.\"" / "\"Hold!\" means \"Don't move a muscle.\"" / "\"Down arms!\" means \"Drop your weapons.\"" / "\"Talk truth!\" means \"Answer me\" or \"Tell the whole story.\"" (`sources/adventure-wdh.json:30563`-`30566`; intro at `:30558`: "Members of the City Watch employ a sort of slang in dealing with the public.")
- The Robes line: "\"Robes\" references the black robes-in other words, one of the magisters. \"Do we need robes here?\" or something similar should be taken as a threat." (`sources/adventure-wdh.json:30567`)
- Gods' Day: "Gods' Day is also a semiofficial \"Be Kind to the Guard and Watch Day\" in Waterdeep." (`sources/adventure-wdh.json:31536`; Gods' Day is Marpenoth 15, which falls after the campaign window, `campaign/setting/deities/kelemvor.md:67`)
- Traffic wardens: "Traffic wardens signal with small blue hand flags for traffic to proceed, and with yellow flags for traffic to hold." (`sources/adventure-wdh.json:30702`)
- Captain's rule of thumb (wiki, 2e): "Law and order—sometimes it's all that separates us from becoming Undermountain or Hellgate Keep." (`sources/research/pass5-bundles/city-watch/wiki.txt:62`; Captain Rulathon, circa 1372 DR; the wiki cites *City of Splendors (boxed set)/Campaign Guide* p. 75)

**The gangs.** Only Staget's view is sourced, so it is his tenet, not the Watch's:

> "Captain Staget is an uptight man who helps keep the peace in the Dock Ward. Every shopkeeper, guild member, innkeeper, and tavern keeper in the Dock Ward knows him, and most respect him regardless of their opinions of the City Watch in general. Staget doesn't believe in rumors or gossip, he doesn't drink, and he doesn't let anger get the better of him. His job is to curb the violence in the Dock Ward, but he has been dragging his heels. After all, he reasons, if the Xanathar Guild and the Zhentarim want to destroy each other, why not let them?"
> — `sources/adventure-wdh.json:2184`

**Nothing supports (tag `[research]` on the organization page):**

- "The Watch is genuinely trying" and "politically untouchable" as a Watch-wide rule. The tag is already on `the-grand-game.md:35`. The only sourced "untouchable" case is one family, through Jalester's briefing in a structure document (`campaign/structure/arc-g-cassalanter-villa.md:37`, pending conversion).
- "Officers are susceptible to pressure from above" as a Watch-wide rule. The sourced cases are Corylus Thann's eight veterans (`:30365`) and two structure-document cases (`campaign/structure/arc-i-kolat-towers.md:33-35`, `arc-g-cassalanter-villa.md:35-37`).
- "The Watch has informants in every ward." The only sourced Watch informant is Gosta Ironhelm (`Appendix_D_-_Running_the_Tavern.md:159`).
- "Most officers are not corrupt by rule" has no published source (section 2).
- A written Watch sewer policy. The sewers line is a common saying (`:2202`) and Staget's refusal (`:2196`), not a rule.

---

## 4. Key Members

Format: the Notable Figures page's own summary line (quoted), then the page path. Pronouns and alignment come from the page. Where a person has no page, the adventure or campaign line is quoted.

**Laeral Silverhand**, Open Lord (not Watch; the Watch reports to her).

> "*Moon elf archmage, chaotic good, she/her*. Stat block: **Archmage**."
> — `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:5`

> "**Affiliation:** City of Waterdeep"
> — `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:6`

The published adventure gives her no species; the moon elf reading is campaign-only (`open-lord-and-masked-lords.md:38`).

**Saeth Cromley**, retired sergeant of the Watch.

> "*Illuskan human retired sergeant, lawful good, he/him*. Stat block: **Warrior Veteran**."
> — `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md:5`

> "**Affiliation:** City of Waterdeep"
> — `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md:6`

> "**Persona.** To the world, Cromley is a retired sergeant of the City Watch, likable, sharp, a bit lax in dress code now that no one checks."
> — `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md:23`

> "{@creature Saeth Cromley|wdh} is a retired {@creature sergeant|WDH} of the City Watch, a likable fellow with a sharp, sarcastic wit."
> — `sources/adventure-wdh.json:32573`

The fireball scene calls him "a City Watch {@creature sergeant|WDH} named {@creature Saeth Cromley|wdh}" (`sources/adventure-wdh.json:4444`). See conflict C9.

**Barnibus Blastwind**, Watchful Order (not Watch; cross-reference only).

> "*Illuskan human Watchful Order investigator, lawful good, he/him*. Stat block: **Mage**."
> — `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:5`

> "**Affiliation:** City of Waterdeep (Watchful Order of Magists and Protectors)"
> — `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:6`

> "{@creature Barnibus Blastwind|wdh|Barnibus} works for the Watchful Order of Magists and  Protectors, investigating crimes that involve the use of  magic."
> — `sources/adventure-wdh.json:31774`

**Jalester Silvermane**, Lords' Alliance field agent; carries a badge of the Watch (cross-reference, not a Watch member).

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

> "The gargoyle retains fragmented memories of the life of {@creature Lady Gondafrey|WDH}, a native Waterdavian who served in the City Watch."
> — `sources/adventure-wdh.json:28506` (no rank in the adventure; the captaincy is campaign text, `campaign/setting/history/04-the-founding-of-chains.md:67`)

**Hyustus Staget**, Watch captain, Dock Ward (no Notable Figures page).

> "Shortly after the characters find Renaer, a captain of the City Watch named Hyustus Staget (LG male Illuskan human {@creature veteran}) leads a dozen {@creature veteran||veterans} to the warehouse."
> — `sources/adventure-wdh.json:2183`

**Cressa Galavarco**, replacement for Staget if Staget has died (no page; conditional).

> "If Hyustus has died for whatever reason, replace him with a female human Watch officer named Cressa Galavarco (LG female Tethyrian {@creature veteran} with no armor or weapons)."
> — `sources/adventure-wdh.json:17873` (Xanathar's Lair scene; routed)

**Jonn Bannock and Ysa Terrow**, Watch officers at the Brandath grove (campaign-only; event card only, no page).

> "Officer Jonn Bannock (Lawful Neutral, Illuskan Human, he/him) and Officer Ysa Terrow (Lawful Neutral, Tethyrian Human, she/her) :: two City Watch officers on the late shift."
> — `campaign/quests/faction-events/emerald-enclave/m02-ten-nights-in-the-city-of-the-dead/ev-01-the-ten-nights.md:149`

**Marek Dunmere**, North Ward day-shift sergeant at the Watch station (campaign-only; no page; the Bregan D'aerthe design note says he is "invented for this event").

> "Marek Dunmere (Lawful Neutral, Illuskan Human, he/him) :: the North Ward's day-shift desk sergeant, who has heard every kind of complaint and writes down all of them."
> — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:173`

> "Sergeant Marek Dunmere takes reports on the day shift."
> — `campaign/gazetteer/waterdeep/north-ward.md:101`

**Orvyn Dall**, appeals clerk in a Trades Ward district magistracy (not Watch; see S9). Campaign-only, single quest.

> "Orvyn Dall is an Illuskan Human appeals clerk in the Trades Ward district magistracy."
> — `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-01-the-legates-eyes.md:17`

**Gosta Ironhelm**, informal Watch informant and tavern applicant (not a Watch member).

> "*LN male shield dwarf, Commoner. Competent, joyless, and a City Watch informant.*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:153`

**Darvish** (former Watch officer) and **Bram** (retired Watch sergeant): tavern staff applicants in Appendix D; no page.

> "*LG male human, Commoner. A former City Watch officer, recovering from injury, quietly excellent.*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:269` (the entry's subject; "Darvish is exactly what he says he is" at line 275)

> "*LN male human, Tough. Retired City Watch sergeant. Utterly reliable. Utterly boring.*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:561` (the entry's subject; "Bram is exactly as advertised" at line 567)

**Commander of the Watch, 1492 DR**: no name in any source. `[research]`.

Other names in the Watch's chain, the Guard and the Griffon Cavalry:

- Elminster, Warden of Waterdeep (City Guard). No page. `sources/adventure-wdh.json:31836`.
- Captain Rulathon, Commander of the Watch, circa 1372 DR (wiki). `sources/research/pass5-bundles/city-watch/wiki.txt:103`.
- Derek Windsfire, Grand Civilar, circa 1372 DR (wiki). `wiki.txt:94`.
- Thyriellentha Snome, Mage Civilar, circa 1372 DR (wiki). `wiki.txt:105`; her entry, `wiki.txt:1463`: "was the commander of the watch-[[wizard]] corps of the [[City Watch (Waterdeep)|City Watch]] in [[Waterdeep]] in [[1372 DR]]."
- Helve Urtrace, Senior Armsmaster, circa 1372 DR (wiki). `wiki.txt:97`.
- Jauslo, watch civilar in charge of the baby griffon recovery for Laeral, 1490s DR (wiki). `wiki.txt:96`.
- Obryn Ironfist, leader of the Griffon Cavalry (wiki, 1372 DR). `wiki.txt:197`.
- Moedt Belabranta, leader of the Griffon Cavalry, circa 1372 DR (wiki). `wiki.txt:239`.
- Corylus Thann, Masked Lord, eight crooked Watch veterans in his pay. No page. `sources/adventure-wdh.json:30365`.
- Brenna Tull (Trades Ward; no page; the Force Grey extraction). Listed among names with no page at `campaign/gazetteer/waterdeep/trades-ward.md:259`.

Wiki names from before the campaign (Brace Ulmemur, Emmer Jundhyl, Mulgor, Ilph, Olophin yn Zelmazzar) are at `wiki.txt:93-102`. They are left out of Key Members.

Names in the sources that belong to other factions and should stay out of the Watch's Key Members (brief: "Do not add anyone from another faction"): Barnibus (Watchful Order), Jalester (Lords' Alliance), Vajra (Force Grey), Savra (Order of the Gauntlet; the Belabrantas breed the griffons, `sources/adventure-wdh.json:3950`), Tashlyn (Doom Raiders; her cover rank is in the City Guard, `sources/adventure-wdh.json:31955`).

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
> — `sources/7. Other Response Teams.pdf`, printed p. 58 (PDF page 2), design note

Stat references: MM p. 350 (veteran), "4 guards" (no stat reference given), DH p. 194 (apprentice wizard). The adventure's own Watch statistics are:

> "Most City Watch members are {@creature veteran||veterans}. Some of the highest-ranked members are {@creature knight||knights}. All City Watch members wear helmets and carry {@item club|phb|clubs} while on duty."
> — `sources/adventure-wdh.json:31895`

> "City Guard privates and sergeants are {@creature guard||guards}. Members of lieutenant rank and higher are typically {@creature veteran||veterans}."
> — `sources/adventure-wdh.json:31846`

Campaign conversions to 2024 names: "four **Warrior Veterans** from the Watch" (`campaign/guides/factions/03-lords-alliance.md:69`), and the Bregan D'aerthe event's "one of the two 2024 **Guards** of a Watch patrol" (`campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/overview.md:10`). The Open Lord team itself is not converted anywhere in the campaign.

**5b. When and how the Watch responds (response clocks as the sources write them)**

- Gralhund Villa, Ch. 3 (adventure): "Neighbors and bystanders alert the City Watch if they hear loud, disturbing noises (such as a {@spell thunderwave} spell) coming from the estate or if they see anything suspicious. The Watch sends a {@creature mage} and six {@creature veteran||veterans} (one {@creature sergeant|WDH} and five constables) to investigate, and it takes {@dice 1d6 + 4} minutes for this force to arrive." (`sources/adventure-wdh.json:4870`)
- Gralhund Villa area overview (campaign): "**City Watch response:** Any audible commotion outside the perimeter walls brings 1 mage + 6 veterans within 1d6 + 4 minutes. The Watch does not respond to interior sounds during the raid unless drawn by external noise." (`campaign/locations/gralhund-villa/area-overview.md:103`)
- Gralhund Villa, Act III Arc E (Alexandrian markdown): "A Watch response team (a Mage, six Warrior Veterans, and a Guard Captain) arrives 1d6+4 minutes after the first serious noise." (`sources/Act_III_Arc_E.md:774`; conflict C15)
- Fireball (adventure): "The characters have a few minutes to examine the crime scene before the City Guard arrives and cordons off Trollskull Alley, posting six {@creature guard||guards} at each entrance." (`sources/adventure-wdh.json:4427`); "Twenty minutes after the explosion, a City Watch {@creature sergeant|WDH} named {@creature Saeth Cromley|wdh} (see {@adventure appendix B|WDH|12}) escorts a member of the Watchful Order of Magists and Protectors named {@creature Barnibus Blastwind|WDH} (see {@adventure appendix B|WDH|12}) to the crime scene." (`sources/adventure-wdh.json:4444`)
- Fireball (campaign journal): "Five minutes before the first six City Guard soldiers arrive and seal the alley. Twenty minutes before **Barnibus Blastwind** (meticulous Illuskan human mage, Watchful Order) and **Sergeant Saeth Cromley** appear with twenty constables and formally take charge." (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36`)
- Kalain's converted windmill (adventure): "Any attempt to break into the tower is 75 percent likely to be seen or heard by one of {@creature Kalain|wdh}'s neighbors. Eight {@creature veteran||veterans} of the City Watch arrive 10 minutes later to investigate the intrusion." (`sources/adventure-wdh.json:13249`)
- Dandymops, Trades Ward (adventure): "Two {@creature veteran||veterans} of the City Watch arrive in {@dice 1d10} minutes to investigate the shop and talk to witnesses." (`sources/adventure-wdh.json:11837`)
- Kolat Towers digging (adventure): "Since Kolat Towers is surrounded by other buildings, there's a {@chance 75|75 percent chance} that any digging attracts {@dice 2d6} members of the City Watch ({@creature veteran||veterans}), who put a stop to it." (`sources/adventure-wdh.json:26812`)
- Sea Ward watch boxes (adventure): "If a guard sounds the alarm, the Watch member on duty fetches a force of forty City Watch {@creature veteran||veterans} to cordon off the property." (`sources/adventure-wdh.json:18579`)
- Trollskull Manor (campaign): "A Watch patrol also answers any disturbance at the manor within the hour, until a Watch citation against the manor ends it for a tenday." (`campaign/guides/trollskull-manor/02-operating-costs.md:83`)
- Trollskull Manor response teams (campaign): "A public massacre in a licensed North Ward establishment invites City Guard, the Watchful Order, and potentially Vajra Safahr personally within the hour." (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:7`)
- Patrol presence by ward (adventure): "A mere pair of Watch operatives might discreetly patrol in the Castle Ward; in contrast, squads of eight walk the Dock Ward, increasing to as many as a dozen at night." (`sources/adventure-wdh.json:30548`); Trades Ward: "The City Watch has a heavy presence in this ward, in the form of both open patrols and officers working out of uniform." (`sources/adventure-wdh.json:31036`)
- Campaign quest examples: Gralhund ev-02: "Any audible commotion outside the walls draws a Watch response in 1d6 + 4 minutes (1 mage, 6 veterans)." (`campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:33`); Gralhund ev-08: "A sleeping dog wakes on a rooftop garden and barks — City Watch responds in 1d6 + 2 minutes." (`campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:46`); Wazoo ev-01: "At lunch the witness shouts for the Watch, and a patrol of two **Guards** arrives about five minutes later from Immar Street." (`campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:179`); Yellowspire ev-02: "within one minute of the first blow a Castle Ward Watch patrol rounds the corner, which marks **Watch File Opened**." (`campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/ev-02-the-chase.md:153`); Legate's Eyes ev-02: "**Watch review:** If Brenna calls the Watch, a patrol sees the extraction, or Orvyn dies, the Watch opens a review of the Trades Ward magistracy under the Code Legal, and for 14 days it logs every Tower request to the Watch, so Vajra cannot act there off the books, and the party loses the +1 Renown for a clean extraction." (`campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-02-the-extraction.md:186`)

**5c. Escalation: Watch to City Guard, Griffon Cavalry, Watchful Order, Force Grey**

No source gives a rule for the Watch handing a scene to the City Guard. The sources show these instances:

> "The arrival of the City Watch foreshadows the return of {@creature Barnibus Blastwind|WDH} and {@creature Saeth Cromley|wdh} (see {@adventure appendix B|WDH|12}), who arrive in due course with twenty constables ({@creature veteran||veterans}) and two {@creature griffon cavalry rider|WDH|Griffon Cavalry riders} (see {@adventure appendix B|WDH|12}) astride {@creature griffon||griffons}. The griffons and their riders remain airborne, providing aerial support and reconnaissance."
> — `sources/adventure-wdh.json:6063` (Gralhund Villa, Ch. 3)

> "If you approach by air, expect a vigorous pursuit by and confrontation with the Griffon Cavalry. Only specially licensed individuals and mounts can fly over Waterdeep. It is best to land well outside the city and approach on foot."
> — `sources/adventure-wdh.json:30447`

> "Whenever Waterdeep has a problem that can't be handled by diplomats or the city's other armed forces, the Open Lord has the option to mobilize Force Grey. Such action is usually taken as a last resort, since some past members of the group have exhibited a tendency to indulge in wanton violence, causing as much damage as they ostensibly prevent."
> — `sources/adventure-wdh.json:1341`

> "Members of the Watchful Order are expected to render service to the city when called upon, acting as temporary members of the City Watch or City Guard."
> — `sources/adventure-wdh.json:30579`

> "Once {@creature Manshoon|WDH}'s whereabouts are established, the City Guard cordons off and surrounds Kolat Towers. The Blackstaff and the Watchful Order assist as needed."
> — `sources/adventure-wdh.json:26765` (conditional on the Manshoon proof, Kolat Towers; routed)

> "Within days after the events that local broadsheets dub the \"Gralhund Villa Bloodbath,\" the City Watch cracks down on the Black Network."
> — `sources/adventure-wdh.json:6080` (after Gralhund Villa; routed)

**5d. When the Watch backs down, releases, or is cleared**

> "The constables had no grounds to get a search warrant, so they didn't pursue the matter."
> — `sources/adventure-wdh.json:4793` (no warrant, no pursuit)

> "If the characters ask for the Watch's help in locating Floon, Staget makes it clear that he won't send a force into the sewers in search of someone who might well be a Zhent or Xanathar Guild spy."
> — `sources/adventure-wdh.json:2196`

> "If members of Force Grey (and, in some cases, the Gray Hands) are arrested for a crime, the Open Lord or the Blackstaff will usually intervene on their behalf and facilitate their release."
> — `sources/adventure-wdh.json:1343`

> "Lords' Alliance agents are more likely to be excused if the Open Lord has cause to let them off."
> — `campaign/setting/governance-and-guilds/city-watch.md:39` (adventure: "characters who become agents of the Lords' Alliance are more likely to be excused for crimes if {@creature Laeral Silverhand|WDH}, the Open Lord of Waterdeep, has cause to let them off the hook", `sources/adventure-wdh.json:970`)

> "If the Watch arrests the member on a minor charge, Savra puts in a good word once a tenday and the Order's clerk tends the member's affairs."
> — `campaign/guides/factions/05-order-of-the-gauntlet.md:64` (Chevall row)

> "If detained, the Watch releases him within 24 hours — no grounds to hold a witness."
> — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:68`

**5e. Arrest procedure**

> "Characters who overtly engage in criminal behavior are quickly cornered and arrested by members of the City Watch. Those charged with committing a crime are brought before a magister to be judged. Advocates might intercede on behalf of the characters if they have allied themselves with influential NPCs and factions."
> — `sources/adventure-wdh.json:970`

> "The first approach is to roleplay the encounter with the arresting officers of the City Watch. The benefit of this approach is that characters can choose to go quietly or resist. The drawback is that the encounter might devolve into a fight-or-flight situation, leading to one or more characters becoming fugitives."
> — `sources/adventure-wdh.json:981`

> "Two {@creature veteran||veterans}, members of the City Watch, are here at all times."
> — `sources/adventure-wdh.json:10502` (Castle Ward courthouse, area H9 "Watch Wagon"; the cell hall, H8, reads "Two {@creature guard||guards} are stationed in this hall at all times." at `:10480`)

> "The magister has already heard the testimony of the arresting officers, as well as that of any eyewitnesses. The characters are given an hour to plead their case while he asks questions."
> — `sources/adventure-wdh.json:10592`

> "A character who loses this contest is found guilty of hampering justice, locked up for a tenday, and fined 200 gp, on top of any other punishments meted out for crimes committed against the city and its citizenry. Those who can't or won't pay the fine are sentenced to hard labor for a year in Amendsfarm, a City Guard-run labor camp among the farms of Undercliff."
> — `sources/adventure-wdh.json:10592` (same paragraph, second half)

> "Hampering justice by concealing evidence can result in a fine of up to 200 gp and hard labor for up to a tenday."
> — `sources/adventure-wdh.json:4516`

> "visitors need her written permission to see him"
> — `sources/adventure-wdh.json:10623` (Castle Ward courthouse; the magister's written permission to visit a prisoner)

> "In Waterdeep, withholding evidence from a Watch investigation is a criminal offense."
> — `sources/Act_III_Arc_D.md:129`

**5f. Factions Guide rules that name the Watch (the mechanics already in the campaign; the new page cross-references them)**

- Gray Hand: "City Watch officers who see the letter are Friendly." — `campaign/guides/factions/06-force-grey.md:58`
- Cloak: "Recognized operative. Watch officers treat you as a trusted civilian informant and can overlook one minor infraction once per tenday, such as a brawl or an openly carried unlicensed weapon." — `campaign/guides/gm-guide/player-factions-overview.md:67` (Factions Guide form: "Once per tenday, a Watch officer overlooks one minor infraction by the member" — `campaign/guides/factions/03-lords-alliance.md:66`)
- Stingblade: "You can read the City Watch's files. Standard files take one hour, and classified files take four hours and a DC 12 Charisma (Persuasion) check." — `campaign/guides/gm-guide/player-factions-overview.md:69`
- Warduke: "Once per quest, four Warrior Veterans from the Watch fight beside you in one operation on the surface." — `campaign/guides/gm-guide/player-factions-overview.md:70`
- Assist the City Watch in a crisis: "Aid the Watch in any situation beyond its capacity, such as monsters, organized assault or mind-controlled citizens. Once per incident." — `campaign/guides/factions/03-lords-alliance.md:55`
- High Harper, Watch cooperation: "It can be Watch cooperation for an operation, a hearing before the Lords' Court, or a warrant of immunity for one person." — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:363`; "Three days after Mirt accepts, he delivers a sealed instruction to the responsible Watch station. It gives the member access to the relevant Watch records and assigns a liaison who coordinates the Watch's existing resources for that operation. It does not raise a new squad or put the member in command." — `ev-01-high-harper.md:377`
- Bregan D'aerthe Commander: "Jarlaxle can arrange one of the following: a private audience with a Masked Lord, passage in or out of Waterdeep without City Watch knowledge, or the quiet disappearance of one named individual for six days." — `campaign/guides/factions/08-bregan-daerthe.md:59`
- Structural rule: "Party actions that become visible citywide — Watch involvement, a public confrontation on a main thoroughfare — may reach several factions simultaneously, but covert intrusions rarely do." — `campaign/guides/gm-guide/structural-rules.md:20`
- Cassalanter leverage: "social and legal leverage as a first response, including threats of Watch involvement and reputation damage." — `campaign/guides/gm-guide/structural-rules.md:32`; "Cassalanters exhaust city leverage first (Watch reports, noble complaints, guild sanctions), then infernal force" — `campaign/guides/gm-guide/running-the-villains.md:51`
- Doom Raiders: "Discretion. The Doom Raiders are criminals running legitimate-fronted businesses in a city where the City Watch already has their file." — `campaign/guides/factions/07-doom-raiders.md:20`

**5g. What the campaign's quest files already fix (examples only; the quest files own these)**

- Fireball! (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md`): "The party has five minutes before the Watch seals the scene and controls access." (line 9); "After the Watch seals the scene, accessing the bodies requires DC 15 Stealth (avoid notice) or Watch cooperation (see below). Bodies are removed to the North Ward Watch Station by midmorning; *Gentle Repose* is cast on each." (line 38); "3. **Own access.** A character who knows *Speak with Dead* can attempt entry to the Watch station or mortuary with DC 13 Persuasion (Barnibus or Cromley). Success = supervised access." (line 88); "If detained, the Watch releases him within 24 hours — no grounds to hold a witness." (line 68)
- Gralhund Villa (`campaign/quests/act-ii/gralhund-villa/`): "7. Yalah surrenders the Stone through the door. She does not speak. Fel'rekt's team withdraws across the rooftops as the Watch arrives at the front gate." (`ev-04-the-zhentarim-raid.md:81`); "By the morning of Ches 25th, the City Watch has sealed Gralhund Villa and begun processing twenty-three bodies. Lord Gralhund is in shock; Hrabbaz is dead. No Stone, no nimblewright, no Floxin." (`ev-09-aftermath.md:44`); "Two days after the villa, the Watch's Zhentarim sweep catches Davil Starsong on association — held at Castle Waterdeep pending Lords' questioning, not evidence." (`ev-09-aftermath.md:57`)
- Finding Floon (`campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md:63`): "Name Floon Blagmaar or Renaer Neverember as kidnapping victims → the Watch sergeant (DC 14 Charisma [Persuasion]) is skeptical but allows a brief supervised conversation with one cooperative prisoner"
- Force Grey, The Legate's Eyes (`campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-02-the-extraction.md:186`): the 14-day review quoted in 5b.
- Doom Raiders, Silencing Skeemo (`campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/design-notes.md:7`): "The accident is now a mechanic. Tashlyn's three questions (what killed him, who was there, what is missing) each score a point, and the score decides whether the Watch opens a file."
- Trollskull Alley (`campaign/quests/act-i/trollskull-alley/ev-07-the-twin-parades.md:23`): "City Watch manages pedestrian flow with professional exasperation."
- Trollskull Manor (`campaign/guides/trollskull-manor/06-tavern-time.md:27`): "| Ches 21–30, after the fireball | Tally Fellbranch, Embric & Avi, Fala Lefaliir | 6: a City Watch patrol arrests a patron |"

**5h. Gaps (mechanics)**

- No Watch-wide response-time table by ward. The source guide's description is not supported by the PDF (5i).
- No rule for handover from Watch to Guard, and no escalation tiers for the Watch.
- No Open Lord response rule in the campaign.
- No stat block for a Watch variant in `adventure-wdh.json`, though `sources/SOURCE_GUIDE.md:41` says Appendix B has "City Watch variants". Greps for "Watch Captain", "Watch Sergeant", "City Watch (veteran|guard|sergeant)" and a named Watch-variant heading returned no match. The fireball scene's "Griffon Cavalry rider (see Appendix B)" (`sources/adventure-wdh.json:4427`) points to an entry the grep did not locate.
- No Watch pay, recruitment or headcount in any source.

**5i. The SOURCE_GUIDE description against the PDFs**

`sources/SOURCE_GUIDE.md:260-266` says of `7. Other Response Teams.pdf`:

> "**Contents:** Non-villain faction reactive groups — the City Watch, the Lords' Alliance Guard, the Gralhund private security, and miscellaneous reactors."
> — `sources/SOURCE_GUIDE.md:260`

> "- City Watch response: jurisdiction, response time by ward, when they escalate to the City Guard, when they back down (noble involvement, political pressure), arrest procedures"
> — `sources/SOURCE_GUIDE.md:263`

> "- Griffon Cavalry: when they deploy, what triggers aerial response"
> — `sources/SOURCE_GUIDE.md:264`

> "- Lords' Alliance Guard: patrol routes, chain of command to Laeral Silverhand"
> — `sources/SOURCE_GUIDE.md:265`

The `2. Other Factions.pdf` entry says the same of the Watch:

> "**City Watch / City Guard / Lords' Alliance Guard:** How law enforcement works in Waterdeep, response times, jurisdiction, the difference between Watch (city law), Guard (gate and wall defense), and Lords' Alliance mercenaries."
> — `sources/SOURCE_GUIDE.md:154`

Against the PDF text:

- `7. Other Response Teams.pdf` (printed pp. 57–61, five pages): printed p. 57 is the Gralhund Response Team; p. 58 the Open Lord Response Team; p. 59 the Unseen Response Team; p. 60 Freelancers and the Three Urchins; p. 61 the Urchins' continuation. **Not in the PDF:** a City Watch section; jurisdiction; response time by ward; escalation to the City Guard; when the Watch backs down; arrest procedures; Griffon Cavalry deployment; a Lords' Alliance Guard; patrol routes.
- The only Watch material in the five pages is the Open Lord team on p. 58 ("a local team of city watchmen") and its design note ("the City Watch can easily be pitted against response teams from the other factions without trivially overwhelming them").
- `2. Other Factions.pdf` (printed pp. 20–22): one Watch passage, the "information blabbed to the City Watch" line on p. 21 (section 2). It has no jurisdiction, response-time or arrest material.

**5j. Alexandrian Gralhund Villa PDF (`4. Gralhund Villa.pdf`), read in part**

Printed pp. 26–35 were read. The Watch appears three times:

> "Or bring the City Watch? Broadly speaking, if the compound seems threatened by armed force, similar responses will be taken."
> — `sources/4. Gralhund Villa.pdf`, printed p. 31

> "as the City Watch comes bursting into the house on the lower level."
> — `sources/4. Gralhund Villa.pdf`, printed p. 34

> "Do they end up fighting Fel'rekt's people on the roof and giving the Gralhunds a chance to escape or for the City Watch to arrive?"
> — `sources/4. Gralhund Villa.pdf`, printed p. 34

No response clock was found in printed pp. 26–35. `sources/SOURCE_GUIDE.md:193` lists a "Watch response and time pressure mechanic" for the Gralhund Villa material, so printed pp. 36 onward still need reading. `[gap]`

---

## 6. Wiki lore worth a bullet

Wiki page titles and the editions their citations give. Wiki quotes keep markup and drop `<ref>` tags. The campaign rule is to paraphrase wiki lines with the edition tagged; these quotes are for the research record.

**W1. Command (wiki, *City Watch (Waterdeep)*; cites *City of Splendors: Waterdeep* 3e and *City of Splendors (boxed set)/Campaign Guide* 2e):**

> "It had a centralized command led by the Commander of the Watch, who supervised three watchlords, or senior commanders: the Mage Civilar in charge of the [[wizard]] corps; the Senior Armsmaster, who was in charge of supplies and reported directly to the Commander of the Watch; and the Grand Civilar, who commanded the ward civilars and held the same rank as the Mage Civilar. The Commander of the Watch reported directly to the [[Open Lord]]."
> — `sources/research/pass5-bundles/city-watch/wiki.txt:36` (the wiki's own reference tags are dropped between the sentences)

**W2. Ward civilars (wiki, same page; cites *City of Splendors (boxed set)/Campaign Guide* 75–76, 2e; *City of Splendors: Waterdeep* 35, 3e; *Waterdeep: Dragon Heist* 198, 5e):**

> "Each ward of Waterdeep was patrolled by a division of the Watch under the command of a ward civilar, or [[Generic City Watch major (Waterdeep)|major]], who oversaw all the senior civilars commanding the watch stations of their respective wards."
> — `wiki.txt:38`

**W3. Badge of the Watch (wiki, same page; cites *Waterdeep: Dragon Heist* p. 189, 5e):**

> "In the 15{{th}} century DR, officers who achieved the rank of captain were awarded a ''[[badge of the Watch]]'', a magic item that provided the wearer with additional protection against attacks and allowed the [[Open Lord]] to immediately know the wearer's location. Only the Open Lord could award ''badges of the Watch''."
> — `wiki.txt:84` (the same line gives the 14th-century amulet of the Watch, cited to *City of Splendors: Waterdeep* p. 149, 3e)

**W4. Griffon Cavalry (wiki, *Griffon Cavalry*; cites *Forgotten Realms Campaign Guide* 197, 4e; *Death Masks* ch. 5; *Waterdeep: Dragon Heist* 39, 5e):**

> "As of [[1479 DR]], however, the Griffon Cavalry had been disbanded for years, as the griffons died in combat but were never replaced."
> — `wiki.txt:226`

> "Then, in the {{YearlinkName|1491}}, Open Lord [[Laeral Silverhand]] proposed refounding the Griffon Cavalry, and threatened to make [[Mirt]] do it."
> — `wiki.txt:228`

> "Either way, this goal was achieved by the {{YearlinkName|1492}}, with the newly procured griffons continuing to be supplied by the Belabranta family."
> — `wiki.txt:228`

Campaign status: the 1479 DR disbandment is not used (`city-watch.md:45`, the 4e fold); the 1491 DR refounding is used as "the wiki says" (`city-watch.md:47`).

**W5. 1479 DR fold of the Guard (wiki, *City Watch (Waterdeep)*; cites *Forgotten Realms Campaign Guide* 197, 4e, and *Downshadow* ch. 1 and 7):**

> "By [[1479 DR]], the [[City Guard (Waterdeep)|City Guard]] had been folded into the Watch, becoming a division of its organization. As the Guard was better equipped and trained, particularly dangerous tasks inside Waterdeep were given to the Guard instead, such as patrolling the [[Waterdeep/Sewers|sewers]] and [[Undermountain]]."
> — `wiki.txt:89`

Campaign status: not used. "It is a 4e-era change, and Dragon Heist keeps two services in 1492 DR" (`city-watch.md:123`).

**W6. Posts and the Palace (wiki, *City Watch (Waterdeep)* and *Palace of Waterdeep*):**

> "There were multiple City Watch posts in Waterdeep. They were usually not located on the main streets, but were all identified by a green and gold lantern that hung outside, permanently lit by a ''[[continual flame]]'' [[spell]]."
> — `wiki.txt:78`

> "The Palace served multiple functions for the administration of the city. It was the main office for many of the city's officials including  [[City Watch (Waterdeep)|City Watch]], [[City Guard (Waterdeep)|City Guard]], and city clerks."
> — `wiki.txt:407` (*Palace of Waterdeep*; cites *City of Splendors: Waterdeep* 96, 3e)

**W7. Trembling horn (wiki, *City Watch (Waterdeep)*; cites *City of Splendors (boxed set)/Campaign Guide* 86, 2e):**

> "Many spellcasters within the City Watch were trained in the use of the spell ''[[trembling horn]]'', which was developed for the organization by [[Thyriellentha Snome|Thyri Snome]]. It allowed watchmen place an invisible, magical tracer that caused alarm-like effects that were widely recognizable among the Waterdhavian populace."
> — `wiki.txt:73`

**W8. Patrol size (wiki, *City Watch (Waterdeep)*; cites the comic and *City of Splendors: Waterdeep* 35, 3e):**

> "When within the walls of Waterdeep, the City Watch typically patrolled in groups of four, with two patrolmen, one armar, and one civilar."
> — `wiki.txt:69`

**W9. Guard size (wiki, *City Guard (Waterdeep)*; cites *City of Splendors: Waterdeep* 33–34, 3e, and *City of Splendors (boxed set)/Campaign Guide* 75–76, 2e):**

> "The exact size of the City Guard was a secret only known to the [[Lords of Waterdeep]], but it was thought to be around 1,200 strong."
> — `wiki.txt:609`

Infobox: "| members        = 1200 ([[1372 DR]])" — `wiki.txt:590`

**W10. Watchful Order (wiki, *Watchful Order of Magists and Protectors*; cites *City of Splendors: Waterdeep* 30, 3e):**

> "The Watchful Order of Magists and Protectors was the [[guild]] of [[wizard]]s and [[sorcerer]]s for the city of [[Waterdeep]]. However, while technically a guild, the Watchful Order functioned primarily as a mage academy."
> — `wiki.txt:312`

Leaders infobox: "[[Mhair Szeltune]] (c. [[1372]])" and "[[Bowgentra Summertaen]] (c. [[1491]])" — `wiki.txt:291`.

**W11. The Open Lord's titles (wiki, *Lords of Waterdeep*; cites *City of Splendors: Waterdeep* 53, 3e):**

> "They held a number of additional titles including [[City Guard (Waterdeep)#Ranks|Warden]] of Waterdeep, Overmaster of the [[Waterdeep#Guilds|Guilds]], and Commander of [[City Watch (Waterdeep)|the Watch]]."
> — `wiki.txt:485` (conflict C1)

**W12. Rank names (wiki, *Generic City Watch* pages; cite *City of Splendors: Waterdeep* 36–37, 3e):**

> "A '''civilar''' was a member of the [[City Watch (Waterdeep)|City Watch]] of [[Waterdeep]], holding a rank equivalent to a lieutenant or captain."
> — `wiki.txt:872`

> "An '''armar''' or '''amlar''' was a low-ranking member of the [[City Watch (Waterdeep)|City Watch]] of [[Waterdeep]], holding a rank equivalent to a sergeant."
> — `wiki.txt:808`

**W13. Captain Jalester (wiki, *City Watch (Waterdeep)*; cites *Waterdeep: Dungeon of the Mad Mage* 10, 5e):**

> "* Captain [[Jalester Silvermane]]<ref name=\"WDMM5e-p10\">...</ref> ''circa ''[[1492 DR]]"
> — `wiki.txt:101` (conflict C8)

---

## 7. Conflicts between sources

Each conflict is paired and the higher-ranked source is named; the choice is the orchestrator's. Ranking: campaign files outrank the published adventure; the adventure outranks the wiki; the Alexandrian markdown and PDFs are tier 3 and are overruled where they disagree with the campaign's day-one choices.

**C1. The Open Lord's titles and the Commander of the Watch.**
- Wiki: "They held a number of additional titles including [[City Guard (Waterdeep)#Ranks|Warden]] of Waterdeep, Overmaster of the [[Waterdeep#Guilds|Guilds]], and Commander of [[City Watch (Waterdeep)|the Watch]]." (`wiki.txt:485`)
- Adventure: "The Watch also includes a Senior Armsmaster, who reports to the Commander of the Watch and is in charge of supplies. The Commander of the Watch reports to the Open Lord, {@creature Laeral Silverhand|WDH}." (`sources/adventure-wdh.json:31886`)
- Higher: adventure; the campaign follows it (`open-lord-and-masked-lords.md:107`).

**C2. Ward civilars: seven, or one per ward.**
- Wiki: "Derek Windsfire: was The Grand Civilar in command of the seven ward civilars ''circa'' [[1372 DR]]" (`wiki.txt:94`).
- Adventure: "Major (ward civilar; one per city ward)" (`sources/adventure-wdh.json:31882`).
- Campaign: "Six wards fill the city, with the City of the Dead and the Field Ward beside them and Undermountain below." (`campaign/setting/geography/waterdeep.md:109`)
- Higher: adventure and campaign. The wiki figure is 1372 DR.

**C3. One service (1479 DR fold) against two.**
- Wiki: "By [[1479 DR]], the [[City Guard (Waterdeep)|City Guard]] had been folded into the Watch, becoming a division of its organization." (`wiki.txt:89`)
- Adventure: "The first soldiers you see in service to the city will be the members of the City Guard who patrol the roads leading to Waterdeep, watch the walls, guard civic structures, and protect magisters. Waterdeep's streets, however, are policed by an altogether different force: the City Watch." (`sources/adventure-wdh.json:30545`); "The City Guard is Waterdeep's army, charged with protecting the city's walls and {@spell gate||gates}, government buildings, harbor, and officials." (`:31817`)
- Higher: adventure and campaign (`city-watch.md:123`).

**C4. Griffon Cavalry size and leader (wiki only; both 1372 DR).**
- Wiki: "members = 100 (as of [[1372 DR]])" (`wiki.txt:205`); "leader = [[Obryn Ironfist]] ([[1372 DR]])" (`wiki.txt:197`).
- Wiki: "* Lord [[Moedt Belabranta]]: Leader of the Griffon Cavalry ''circa'' [[1372 DR]]." (`wiki.txt:239`)
- Campaign: "Its present size is `[research]`." (`city-watch.md:47`)
- Higher: none for 1492 DR. The wiki's two leaders conflict with each other.

**C5. Griffon Cavalry disbanded in 1479 DR against flying in 1492 DR.**
- Wiki: "As of [[1479 DR]], however, the Griffon Cavalry had been disbanded for years" (`wiki.txt:226`).
- Adventure: "Brave warriors of the City Guard light out from the Peaktop Aerie atop Mount Waterdeep, riding fearsome griffons that have been bred and trained for that purpose." (`sources/adventure-wdh.json:31171`)
- Higher: adventure (1492 DR, present tense).

**C6. Guard strength: "about 1,200" in the wiki and "1,200 guards across three shifts" in the retired outline.**
- Retired outline: "**The City Watch**: 1,200 guards across three shifts; understaffed, overworked; not corrupt by default but susceptible to political pressure" (`campaign/structure/ch2-city-of-splendors.md:48`)
- Wiki (Guard): "it was thought to be around 1,200 strong." (`wiki.txt:609`)
- Adventure: patrol sizes only: "City Watch patrols are usually four to twelve persons strong." (`sources/adventure-wdh.json:31867`)
- Higher: none gives the Watch a total. Campaign: "No source gives the Watch's total strength, so this page gives none." (`city-watch.md:19`)

**C7. Crooked Watch officers against "trust the Watch" and "not corrupt by rule".**
- Adventure: "he has eight crooked members of the City Watch (human {@creature veteran||veterans}) crack down on them" (`sources/adventure-wdh.json:30365`); "you can trust members of the City Watch to do their duty diligently" (`:30514`).
- Retired outline: "not corrupt by default but susceptible to political pressure" (`campaign/structure/ch2-city-of-splendors.md:48`)
- Campaign, untagged: "Most officers are not corrupt by rule and can be pressed from above." (`city-watch.md:79`); "Most officers are not corrupt by rule." (`the-grand-game.md:37`)
- Higher: adventure facts win; the "not corrupt" phrase has no published source and needs `[research]`.

**C8. Jalester: Watch captain or Lords' Alliance agent.**
- WDMM: "Volothamp Geddarm introduces the characters to a friend of his: a young captain of the City Watch named Jalester Silvermane." (`sources/adventure-wdmm.json:457`)
- Wiki: "* Captain [[Jalester Silvermane]]<ref ...></ref> ''circa ''[[1492 DR]]" (`wiki.txt:101`)
- WDH: "{@creature Jalester Silvermane|WDH} (see {@adventure appendix B|WDH|12}) is an agent of the Lords' Alliance who reports directly to {@creature Laeral Silverhand|WDH}." (`sources/adventure-wdh.json:1536`)
- Campaign NF: "**Affiliation:** Lords' Alliance" (`campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:6`)
- Higher: WDH and the campaign NF. The WDMM and wiki readings are not used. WDH itself gives him the Watch's badge (`:31617`).

**C9. Cromley: active sergeant or retired.**
- Adventure: "Twenty minutes after the explosion, a City Watch {@creature sergeant|WDH} named {@creature Saeth Cromley|wdh} ... escorts" (`sources/adventure-wdh.json:4444`)
- Adventure: "{@creature Saeth Cromley|wdh} is a retired {@creature sergeant|WDH} of the City Watch, a likable fellow with a sharp, sarcastic wit." (`sources/adventure-wdh.json:32573`); "a retired {@creature sergeant|WDH} of the City  Watch who assists in many of his investigations." (`:31774`)
- Alexandrian Arc D: "Sergeant **Saeth Cromley** escorts **Barnibus Blastwind** of the Watchful Order of Magists and Protectors to the crime scene." (`sources/Act_III_Arc_D.md:137`)
- Higher: the adventure is split on the point, and the campaign files use "retired". `city-watch.md:127` flags it for the user.

**C10. Barnibus: Watch or Watchful Order; magistrate or investigator; dwarf or human.**
- Adventure: "{@creature Barnibus Blastwind|wdh|Barnibus} works for the Watchful Order of Magists and  Protectors, investigating crimes that involve the use of  magic." (`sources/adventure-wdh.json:31774`)
- Campaign NF: "The campaign's **Stingblade** and **The Archer Above** events call him Magistrate Blastwind, a title the published adventure does not give him (campaign-only)." (`campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:29`)
- Alexandrian Arc D: "Barnibus — a soft-spoken, meticulous dwarf mage in an ink-stained coat" (`sources/Act_III_Arc_D.md:137`)
- Campaign NF: "*Illuskan human Watchful Order investigator, lawful good, he/him*." (`02-barnibus-blastwind.md:5`)
- Higher: adventure (investigator, no title) and NF (race). Arc D is stale (`the-grand-game.md:392` says so).

**C11. The Watchful Order's head.**
- Adventure: "Wizards, sorcerers, and other arcane spellcasters who intend to stay in Waterdeep for any length of time are required to register with the city, and will be strongly encouraged to join the Watchful Order of Magists and Protectors, headed by the Blackstaff." (`sources/adventure-wdh.json:30578`)
- Wiki: "[[Bowgentra Summertaen]] (c. [[1491]])" (`wiki.txt:291`)
- Alexandrian Arc D: "**Bowgentra Summertaen**, Lady Master of the Watchful Order of Magists and Protectors" (`sources/Act_III_Arc_D.md:467`)
- Higher: adventure. Campaign draft (`city-watch.md:129`) says both can be true.

**C12. Amendsfarm's operator.**
- Adventure: "a prison farm run by the City Watch (called Amendsfarm)" (`sources/adventure-wdh.json:31125`)
- Adventure: "Those who can't or won't pay the fine are sentenced to hard labor for a year in Amendsfarm, a City Guard-run labor camp among the farms of Undercliff." (`:10592`)
- Higher: both are the adventure; the campaign leaves the operator open (`code-legal-and-magisters.md:97`).

**C13. The Watch and the sewers.**
- Wiki: "They never acted outside the walls of the city and did not pay much attention to the city's sewers." (`wiki.txt:64`)
- Adventure: captains hold sewer keys (`:11626`); and "After obtaining the {@item Stone of Golorr|WDH}, the characters are arrested by the City Watch soon after they emerge from the sewers." (`:10534`)
- Higher: adventure. Not a true conflict. The wiki's "walls" claim is wiki-only.

**C14. Who seals the fireball scene.**
- Adventure: "before the City Guard arrives and cordons off Trollskull Alley" (`sources/adventure-wdh.json:4427`)
- Campaign journal line 9: "The party has five minutes before the Watch seals the scene and controls access." (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:9`)
- Campaign journal line 36: "Five minutes before the first six City Guard soldiers arrive and seal the alley."
- Higher: adventure and the journal's own line 36. Minor; the Watch seal is loose wording.

**C15. Gralhund response team: a Guard Captain or a sergeant.**
- Adventure: "The Watch sends a {@creature mage} and six {@creature veteran||veterans} (one {@creature sergeant|WDH} and five constables)" (`sources/adventure-wdh.json:4870`)
- Campaign area overview: "1 mage + 6 veterans" (`campaign/locations/gralhund-villa/area-overview.md:103`)
- Alexandrian Arc E: "A Watch response team (a Mage, six Warrior Veterans, and a Guard Captain)" (`sources/Act_III_Arc_E.md:774`)
- Higher: adventure and campaign. Arc E's "Guard Captain" disagrees.

**C16. Tashlyn's cover rank.**
- Adventure: "Tashlyn has established a useful cover by serving as a bodyguard to Vorondar Levelstone, a dwarf magister stationed at the South Gate. She likes the dwarf and has earned his confidence, allowing her to reach the rank of captain in the City Guard." (`sources/adventure-wdh.json:31955`)
- Campaign NF: "a Calishite bodyguard to a dwarf magistrate at the South Gate" (`campaign/setting/notable-figures/doom-raiders/05-tashlyn-yafeera.md:21`)
- Campaign city-watch: "She holds the rank of captain in the City Guard as cover and watches the traffic through the South Gate." (`city-watch.md:69`)
- Higher: adventure and NF (the bodyguard post is the cover; the captaincy is earned through it). `city-watch.md:69` inverts this. Ruling 18 says follow the NF.

**C17. Vajra's alignment.**
- Campaign NF: "*Tethyrian human archmage, lawful neutral, she/her*." (`campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:5`)
- Campaign city-watch: "**Vajra Safahr** (Neutral, Tethyrian Human, she/her)" (`city-watch.md:63`)
- Higher: NF.

**C18. Savra's alignment.**
- Adventure: "Savra Belabranta (NG female Tethyrian human {@creature knight}) visits the characters' residence and invites them to the Halls of Justice" (`sources/adventure-wdh.json:3949`)
- Campaign NF: "*Tethyrian human knight, neutral good, she/her*." (`campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md:5`)
- Campaign city-watch draft: "her Notable Figures page says lawful good" (`city-watch.md:133`) — wrong (S1).
- Higher: NF and adventure agree on neutral good. Campaign text on the Watch page (`city-watch.md:47`) already says Neutral Good.

**C19. Gondafrey's alignment.**
- Campaign NF: "*Lawful good gargoyle (human soul), lawful good / chaotic evil (set by time of day), she/her*." (`independents-allies/18-lady-gondafrey.md:5`)
- Campaign city-watch: "**Lady Gondafrey** (Lawful Good, Gargoyle, she/her)" (`city-watch.md:67`) — omits the time-of-day shift.
- Higher: NF.

**C20. Field Ward: no Watch, or a campaign Watch house.**
- Adventure: "The Watch doesn't patrol this area, however, and many crimes go uninvestigated." (`sources/adventure-wdh.json:31104`)
- Campaign: "The campaign also has a Watch house in the ward. This page keeps Dragon Heist's rule as the base: the Watch does not patrol, and the house sends Guards only after a report or for a planned operation." (`campaign/gazetteer/waterdeep/field-ward.md:146`)
- Higher: adventure. The "house sends Guards" phrasing mixes the Guard and the Watch (S11).

**C21. Watch patrols against the Guard's patrols on the walls.** The adventure splits them by role (`sources/adventure-wdh.json:30545`). No conflict.

**C22. Staget's replacement.** Adventure: "If Hyustus has died for whatever reason, replace him with ..." (`:17873`). Campaign: "If he has died, the published adventure replaces him with Cressa Galavarco (Lawful Good, Tethyrian Human, she/her), a veteran." (`city-watch.md:71`). No conflict; the replacement is conditional.

**C23. Watch escort for Lords' Alliance characters.**
- Adventure: "City Watch officials are notified that the characters are on \"official business\" for the Lords' Alliance and instructed to provide support whenever they can." (`sources/adventure-wdh.json:1390`)
- Appendix B: "**Redknife** | Jalester will request a City Watch escort of two **guards** for one dangerous errand per tenday." (`sources/Appendix_B_-_Player_Factions.md:253`, the Alexandrian rank list; the campaign's Redknife page is not checked here)
- Higher: adventure for the notification; campaign Factions Guide for the escort benefit. Not a conflict in substance.

**C24. Informants.**
- Campaign, tagged: "**Informants:** The Watch has informants in every ward `[research]`, and every faction has informants in the Watch `[research]`." (`the-grand-game.md:29`)
- Campaign, untagged: "The Watch has informants in every ward, and every faction has informants in the Watch." (`city-watch.md:79`)
- Campaign draft: "The one sourced Watch informant is Gosta Ironhelm" (`the-grand-game.md:90`)
- Higher: the tagged reading. `city-watch.md:79` needs the tag.

**C25. Laeral's office.**
- Adventure: "a few years ago" (`open-lord-and-masked-lords.md:16` reads the adventure's line 452).
- Campaign history: "Laeral Silverhand became Open Lord about three years before the campaign" (`campaign/setting/history/07-a-city-watching-itself.md:22`).
- Higher: the history page's derived date (`07-a-city-watching-itself.md:16`). Not Watch-specific; listed because the Watch's chain runs through her office.

---

## 8. Stale or contradicting lines in other campaign files

**S1.** `campaign/setting/governance-and-guilds/city-watch.md:133` says "her Notable Figures page says lawful good". Savra's NF page reads "*Tethyrian human knight, neutral good, she/her*." (`campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md:5`). Stale.

**S2.** `city-watch.md:131` cites `campaign/quests/act-ii/fireball/ev-01-the-fireball.md` line 196 for Jalester's "standard Watch inspection protocols". The line is 192: "Jalester mentions without pressure that the Sea Maidens Faire uses private docking arrangements that circumvent standard Watch inspection protocols." Wrong line.

**S3.** `city-watch.md:124` cites `wiki.txt` lines 170 and 189 for the Guard's "1200 (1372 DR)". The line is 590 (infobox: "members = 1200 ([[1372 DR]])") and 609 (the secret 1,200). Lines 170 and 189 are the *Waterdeep Watch* infobox and the *Griffon Cavalry* heading. Wrong lines.

**S4.** `city-watch.md:128` says the wiki (`wiki.txt` line 101) calls Jalester "a young captain of the City Watch". The wiki line says "Captain Jalester Silvermane ... circa 1492 DR". "a young captain" is in `sources/adventure-wdmm.json:457`. Wrong citation.

**S5.** `city-watch.md:129` cites `wiki.txt` line 308 for Summertaen as leader around 1491 DR. The leader infobox is at `wiki.txt:291`. Wrong line.

**S6.** `city-watch.md:132` says the Warden's 1491 DR appointment "after Ezender Drayth's murder is wiki-only (`wiki.txt` lines 162 and 266)". Line 162 is a field in the *Waterdeep Watch* infobox, and 266 is the *Griffon Cavalry* gallery. The only Ezender Drayth line in this bundle is the Guard's leader list at `wiki.txt:582` ("[[Ezender Drayth]] ([[1491 DR]])"). The bundle has no murder line. Wrong citation; the murder is not in this bundle.

**S7.** `campaign/setting/history/01-ahghairons-gifts.md:58` says: "- The wiki says Ahghairon restructured Raurlor's army and navy into the City Watch and the City Guard. The published adventure keeps both services and credits him with neither. The wiki's City Watch page never mentions Ahghairon, so the claim rests on History of Waterdeep alone (City of Splendors boxed set Campaign Guide p. 30, 2e)." The bundle's City Watch and City Guard pages have no Raurlor or navy text (a grep for "Raurlor", "navy" and "Ahghairon" returns only `wiki.txt:222` and `:488`), which agrees with the history page's own note. The same claim is at `city-watch.md:49` and `history/01-ahghairons-gifts.md:24`. `[gap]`

**S8.** `campaign/setting/history/01-ahghairons-gifts.md:61`: "The old outline called the dragonward, the Code Legal and the City Watch protections built by someone who had seen what tyranny does." Retired-outline framing; the page tags the rest `[research]`.

**S9.** `campaign/guides/gm-guide/design-notes-running-the-campaign.md:121` calls Orvyn Dall a "Watch appeals clerk". The Trades Ward gazetteer says "The appeals office of the ward's district magistracy employs four clerks. One of them, Orvyn Dall, an Illuskan human, was placed there seven tendays ago." (`campaign/gazetteer/waterdeep/trades-ward.md:93`), and the event says he is "an Illuskan Human appeals clerk in the Trades Ward district magistracy" (`ev-01-the-legates-eyes.md:17`). Stale.

**S10.** `campaign/guides/factions/07-doom-raiders.md:15` ("Tashlyn's City Guard position provides one piece of actionable Splinter intelligence per tenday at Renown 3+.") and `campaign/setting/history/04-the-founding-of-chains.md:58` ("Tashlyn serves as Captain of the City Guard at the South Gate under the dwarf magister Vorondar Levelstone.") both leave out the bodyguard cover (`sources/adventure-wdh.json:31955`). Same issue as C16.

**S11.** `campaign/gazetteer/waterdeep/field-ward.md:146`: "the house sends Guards only after a report or for a planned operation" — mixes Guard and Watch (C20).

**S12.** `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:29` calls him "Magistrate Blastwind". The adventure gives no such title (`sources/adventure-wdh.json:31774`). Campaign-only and tagged in the NF page.

**S13.** `campaign/setting/the-grand-game/the-grand-game.md:37` carries "Most officers are not corrupt by rule" without a tag (its source is the retired outline, `ch2-city-of-splendors.md:48`). `city-watch.md:79` says the same untagged.

**S14.** `campaign/gazetteer/waterdeep/sea-ward.md:156` says "Every sergeant in the ward knows the Watch posts a guard at the Cassalanter service gate." This is campaign-only and reads as Watch knowledge of the family's gate, which is suspicion only under brief ruling 7. Flag for the orchestrator.

**S15.** `campaign/setting/organizations/04-order-of-the-gauntlet.md:60` ("it records that the Watch closed every complaint against the family without findings") and `campaign/gazetteer/waterdeep/sea-ward.md:156` ("The Watch has closed every complaint against one Sea Ward family without findings") both repeat the closed-complaints fact. Consistent with each other, but the Stingblade inquiries it cites (`sea-ward.md:156`, "three closed inquiries against one unnamed Sea Ward house") are not checked here.

**S16.** Checked, no conflict: `campaign/setting/governance-and-guilds/city-watch.md:84` on the High Harper's Watch cooperation matches `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:377`.

**S17.** `sources/Act_III_Arc_D.md:500`: "- **Watch Authority:** A Renown of 1+ in any faction, or a Watch badge obtained during the crime scene, automatically gains entry." (Dalakhar's room at the Inn of the Dripping Dagger). The campaign gives one badge (Jalester's, `sources/adventure-wdh.json:31617`), and the wiki says "Only the Open Lord could award ''badges of the Watch''." (`wiki.txt:84`). The Arc D rule conflicts with both. Flag.

**S18.** `campaign/structure/ch2-city-of-splendors.md:34` ("City Watch headquarters"), `:46`, `:48` (1,200 across three shifts), `:56` ("City Watch captain is a worshiper"), `:88`, `:154`, `:158`, `:244`. Retired outline, still in `campaign/structure/`. The brief says the retired files are not used. Listed because the lines still exist.

**S19.** `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:7` says a massacre invites the City Guard, the Watchful Order and Vajra, while `02-operating-costs.md:83` says a Watch patrol answers any disturbance within the hour. Both coexist. The Factions Guide should say which force answers which.

**S20.** `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md:27` says "a former sergeant of the City Watch (confirmed rank; not Watch Commander despite some in-text references)". The "in-text references" to a Commander are not in this bundle; not checked further.

**S21.** `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:9` says the Watch seals the scene; line 36 says the City Guard does. See C14.

**S22.** `campaign/setting/the-grand-game/the-grand-game.md:35` tags "genuinely trying" as `[research]`; `city-watch.md:79` gives the same idea untagged ("The Watch is trying to do its job, and it knows that some cases are politically untouchable."). Tag mismatch; see C24 family.

---

## Not found (search terms and files)

- Watch headcount, pay, recruitment: searched `city-watch.md`, `adventure-wdh.json` ("Watch", "City Guard", "1,200") and the wiki bundle. None.
- Per-ward response time: searched the adventure JSON for "minutes" near "Watch" and the campaign for "Watch response". Only per-location times (5b). The source guide's "response time by ward" is absent from the PDF (5i).
- Watch-to-Guard handover: searched the adventure JSON for "City Guard" and both PDFs. Only the fireball and the Kolat instances (5c).
- Open Lord response rule in the campaign: `open-lord-and-masked-lords.md:113`; grep of `campaign/` for "Open Lord response". None.
- Watch stat block variant in `adventure-wdh.json`: none (greps for "Watch Captain", "Watch Sergeant", "City Watch (veteran|guard|sergeant)" and a named Watch-variant entry). The fireball's Griffon Cavalry rider (`:4427`) points to Appendix B, which the grep did not locate.
- Griffon Cavalry size in 1492 DR: none (`city-watch.md:47`, `[research]`).
- Commander of the Watch in 1492 DR: none.
- Watch headquarters building: none. Both wiki and adventure say the Palace (`city-watch.md:122`).
- Watch badge rules beyond the Open Lord's award: wiki 14th-century amulet and 15th-century badge only (`wiki.txt:84`).
- Watch and ship inspection: only the campaign's `ev-01-the-fireball.md:192`. The GM Notes say no source supports ship inspection.
- Navy size, ships, commander: `city-watch.md:49`, `[research]`; not in the bundle.
- Watch informant network: only Gosta (`Appendix_D_-_Running_the_Tavern.md:159`) and Myl Dunpier's record-keeping (`21-myl-dunpier.md:21`).
- Watch on the Dock Ward shore: wiki-only past tense (`campaign/gazetteer/waterdeep/dock-ward.md:81`), not in this bundle.
- A Watch doctrine or oath beyond the code of conduct: none.

## Not readable

- `sources/4. Gralhund Villa.pdf`: read in printed pp. 26–35 only (section 5j). Pages 36 onward not read.
- `.docx` files in `sources/Other remix files/`: not consulted. `sources/SOURCE_GUIDE.md` names no .docx as covering the Watch (its City Watch entries are the two PDFs, the adventure Ch. 9, and the mapping at lines 719–735).
- `2. Other Factions.pdf` and `7. Other Response Teams.pdf` were read through the Read tool's rendered output (3 and 5 pages). `pdftotext` was not run (no shell tool in this session).
