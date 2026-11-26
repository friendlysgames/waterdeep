# Pass 6 research notes: Mirt

Page: `campaign/setting/notable-figures/harpers/01-mirt.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Mirt is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/01-harpers.md`
Factions Guide: `campaign/guides/factions/02-harpers.md`
Voice profile: `.claude/skills/character-voices/voices/harpers.md` (### Mirt, lines 7-25)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/bregan-daerthe/03-felrekt-lafeen.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field of an entry is given where one exists.
- Wiki: the scratchpad extract `wiki-harpers/01-mirt.txt` is the Mirt page. It is quoted as "wiki line N" (that file's lines). The same page is also in `sources/research/pass5-bundles/harpers/wiki.txt` at lines 660 to 860. Edition tags come from the wiki's own infobox and `ref` names. The wiki prints no edition on most sentences.
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` was read as rendered pages (PDF pp.1-3 = printed pp.23-25). The Harpers paragraph is on PDF p.2 (printed p.24). The quote is a transcription from the image. Check with `pdftotext -layout` before any quote goes into prose.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.
- Remi's wiki page: the scratchpad extract for Remi is `NOT FOUND`. Her wiki page is in `sources/research/pass5-bundles/harpers/wiki.txt` lines 862 to 990. That is in the other notes file.

## Findings that change how the page is written

1. **The Masked Lord office is public or hidden, and the files disagree.** `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:40` says "The campaign keeps his office from the party until the High Harper rank". The Harpers organization page's Draft Notes say "The Masked Lord office is public knowledge in the campaign" (`01-harpers.md:173`). The page's Summary (line 6) lists "Masked Lord of Waterdeep" as affiliation. The brief asks for the Summary and Persona to match. This is the first open conflict (D1).
2. **The stat block source does not verify.** The page's Summary says "WDH custom block, CR 9". The published adventure's Mirt entry (lines 32279 to 32305) has no CR, AC or HP. The mechanics reference calls the WDH record "CR 9, AC 16, 153 HP" (`docs/plans/harpers-mechanics-reference.md:484` and `:598`). It also says the page once named the block "Veteran with modifications" (`:531`). Only the wiki gives CR 9 (wiki line 59). See B3 and D2.
3. **Overview and Persona are over the brief's word limit.** The Overview is 36 words (page line 29). Draft a shorter one under 21 words.
4. **Two campaign files give the Cassalanter suspicion a different age.** The Harpers organization page says "About a year ago the Howling Hatred cult led Mirt to suspect Cassalanter money." (`01-harpers.md:30`). The superseded `arc-c-fireball.md:98` says "three years ago". Use the first. See D4.
5. **The wiki's Spelljammer Academy and 1491 DR lines conflict with day one.** The wiki says Mirt "was forced to flee Waterdeep" (wiki line 146) and that in 1491 DR he "chose to stay with Laeral" (wiki line 143). The campaign has him in Waterdeep on Ches 1, 1492 DR and Laeral Open Lord since about 1489 DR (`history/07-a-city-watching-itself.md:76`). Campaign wins. See D5.

---

## A. Background facts by theme

### A1. Origin, family, early life

**Wiki, Early Life (infobox refs2e: "Hall of Heroes", 2e, `HoH-p86`)**
> "Mirt was the son of a successful Coaster, a [[Sword Coast]] trader. He grew up hearing many tales and deeds of heroism which led him down the path of becoming a [[fighter]]."
> — wiki line 102 (edition: 2e, Hall of Heroes p.86, inferred from the infobox's `refs2e` on line 46)

**Wiki, lead (refs3e: "Forgotten Realms Campaign Setting 3rd edition", `FRCS3e-p181-182`)**
> "He became a member of the [[Harpers]] as well as a [[Lords of Waterdeep|Masked Lord]] of [[Waterdeep]], which was commonly known."
> — wiki line 63 (edition: 3e, printed on the ref name `FRCS3e-p181-182`)

Wiki line 63 also says he was "a [[human]] [[rogue]] and retired [[adventurer]] and a [[mercenary]] general, when he was known as '''Mirt the Merciless''' or '''the Old Wolf''' or '''Lord Walrus'''." (ref `FRCS3e-p181-182`; `ED-p15`).

**Wiki, aliases (infobox line 8, ref `HoH-p86`)**
> "| aliases        = Mertonius<ref name="HoH-p86" /><br/>Tonius<ref name="HoH-p86" />"
> — wiki line 8

**Adventure, Mirt entry (page 210)**
> "Once known as {@creature Mirt|WDH} the Merciless and the Old Wolf, {@creature Mirt|wdh} made a fortune and carved out a reputation as an adventurer and philanderer. Today, an older and wiser {@creature Mirt|WDH} serves as one of the Masked Lords, a Harper, and a close advisor to {@creature Laeral Silverhand|WDH}. The years have not worn him down, and though he has grown soft in the flesh, he remains deceptively strong, vigorous, and clear of mind. {@creature Mirt|WDH} has survived the passing of centuries by means of magic, and of all the Masked Lords, he is the least concerned with concealing his identity."
> — `sources/adventure-wdh.json:32293` (entry "Mirt", page 210)

No source gives his birth year, birth name beyond the wiki's "Mertonius", parentage beyond "a successful Coaster", home town, or age. The infobox fields `age` (wiki line 16), `dob` (line 21), `parents` (line 30) and `siblings` (line 32) are blank.

### A2. Mercenary years, friendship with Durnan, rescue of Asper

**Wiki (3e; the 2e-era Hall of Heroes ref is on the same paragraph)**
> "In time, he became a great mercenary general of the [[North]] and earned himself the nickname "Mirt the Merciless". He was greedy and became quite wealthy, but grew unsatisfied with mere wealth. He actually craved peace and tranquility, and realized he could not simply buy it, but would have to create it in the world."
> — wiki line 104 (ref `HoH-p86`, 2e)

> "During his mercenary days, he met Durnan the Wanderer and the two became close companions. The two of them decided to "retire" to Waterdeep."
> — wiki line 106 (ref `HoH-p86`, 2e)

> "At some point, he met his future wife, Asper, whom he rescued as a baby from a sacked city."
> — wiki line 108 (ref `HoH-p86`, 2e). No city is named.

**Wiki, Asper (Family, ref `CoS.W-p54-55` and `WDH5e-p210-211`)**
> "His wife and heir,<ref>{{Cite book/Spellfire}}</ref> [[Asper]], was an informal member of the [[Gray Hands]]. She preceded him in death.<ref name="CoS.W-p54-55" /><ref name="WDH5e-p210-211" />"
> — wiki line 77 (the Gray Hands membership is from the wiki only; see F2)

**Adventure, Mirt entry (page 210-211)**
> "Despite his prodigious girth, {@creature Mirt|WDH} can move with good speed when he must, and he hasn't let his adventuring skills wither. His wife, Asper, passed away several years ago, and his rambling mansion has seen better days. {@creature Mirt|WDH} spends his days embroiled in politics and whiles away his nights in drink and debauchery."
> — `sources/adventure-wdh.json:32294` (entry "Mirt", page 210)

**Campaign, Emotions (day-one; the widowhood is the adventure's)**
> "**Emotions.** Mirt most often feels roaring amusement, political calculation behind the laughter, deep loyalty to old friends, nostalgic melancholy for Asper (his late wife), predatory enjoyment of power games, and genuine delight in architecture that catches his audience off guard."
> — `campaign/setting/notable-figures/harpers/01-mirt.md:13`

### A3. Retirement in Waterdeep, the Lords, and the thieves' guild

**Wiki (ref `HoH-p86`, 2e)**
> "With Durnan in tow, Mirt went to Waterdeep to live, but quickly became bored with peaceful living. Within a month of his arrival, he was approached by [[Khelben Arunsun]] and [[Sammereza Sulphontis]] with an invitation to become a Lord of Waterdeep. A few years later, he proposed to the other Lords that Durnan also be accepted as a Lord, and they agreed."
> — wiki line 111 (ref `HoH-p86`, 2e)

> "Mirt (and Durnan) performed many covert tasks for the Lords of Waterdeep. Among them was Mirt's stint as a member of Waterdeep's [[thieves' guild]] under the alias '''Tonius'''. He used his disguise to feed the Lords information on the guild, which led to the guild's eventual eradication from the city."
> — wiki line 113 (ref `HoH-p86`, 2e)

Campaign: Khelben is dead and his soul rests in the Blackstaff (`campaign/setting/organizations/01-harpers.md:25`, Draft Notes of the timeline: "Campaign change: Khelben is dead and his soul rests in the Blackstaff, Laeral is Open Lord, and the campaign has no Moonstars page."). Use the invitation as past fact only.

**Wiki, money-lending (refs `VGtW-p11-12`, `WatN-p22,31`)**
> "Mirt ran his money-lending business primarily out of his mansion in Waterdeep. Transactions would happen only in the mornings, and Mirt was said to be patient regarding their repayment."
> — wiki line 115

**Campaign, the loans (the Harpers organization page)**
> "Funding:** Mirt lends to Harper members, and his personal loans leave them owing him a favor in place of coin."
> — `campaign/setting/organizations/01-harpers.md:73` (the bullet opens "- **Funding:**"; the quote runs from the label)

Quote as the full bullet: "- **Funding:** Mirt lends to Harper members, and his personal loans leave them owing him a favor in place of coin. The published adventure has the Harpers offer common and uncommon potions and scrolls at a reduced or deferred cost. The wiki says the order holds investments across western Faerûn, that its network of artisans and merchants buys magic items at a discount, and that agents sometimes rob wealthy nobles and merchants to share the money with the poor and keep part of it for future work (Forgotten Realms Wiki, *Harpers*, edition not stated)."

**Appendix D (Alexandrian, Trollskull tavern loan; a day-one debt in the Trollskull Manor guides)**
> "Mirt offers a personal loan of up to <strong>500 gp</strong> at no stated interest, repayable "whenever it's convenient" — which means repayable as a favor rather than coin. He does not forget debts, and the favor he will eventually ask will be proportional to the crisis the loan solved."
> — `sources/Appendix_D_-_Running_the_Tavern.md:786`

> "Mirt's loan is a different kind of pressure. It never shows up on the books. It sits in the background of every scene where the Harpers ask the party for something, and the DM should let the players feel its shadow without spelling it out."
> — `sources/Appendix_D_-_Running_the_Tavern.md:878` (the loan is the tavern's; it is a Trollskull Manor fact, not a Mirt biography fact)

### A4. Undermountain and the Well (with Durnan)

**Adventure, Castle Ward chapter (no page field read)**
> "{@creature Mirt|WDH} has quite a history with {@creature Durnan|WDH}, the proprietor of the Yawning Portal. Together they descended into \"the Well, \"as the entrance to Undermountain was known in olden days. Waterdeep used to throw criminals in the Well, leaving them to die horribly in Undermountain's dungeons. {@creature Durnan|WDH} and {@creature Mirt|WDH} entered the dungeons of their own free will-and not only that, but returned laden with treasures. Both used magic to extend their lives, but they eventually parted ways. {@creature Mirt|WDH} kept on with a life of adventure, while {@creature Durnan|WDH} built the tavern called the Yawning Portal over the Well and now, almost two centuries later, charges coin to descend into it. Not a bad way to part fools from their money!"
> — `sources/adventure-wdh.json:31014`

**Wiki, Undermountain (refs `SD-p4`, `RoU-p9`, `USD-p4,17`; infobox-free)**
> "At some point, Mirt actually adventured into Undermountain with several other Lords, including Durnan (of course) and Khelben."
> — wiki line 118
> "Mirt, Durnan, and Khelben were among the few adventurers to return alive from the [[Underhalls]].<ref name="SD-p4">{{Cite book/Undermountain: Stardock|4}}</ref>"
> — wiki line 120 (the last sentence of that paragraph; the earlier sentences cover the Grim Statue, the Crystal Labyrinth and the Lost Level)
> "It was well known that Mirt and Durnan emerged from Undermountain in the {{yearlinkName|1302}}, with a vast amount of wealth and fame. Mirt used his share to build his mansion near [[Mount Waterdeep]], while Durnan used his to erect the [[Yawning Portal]] tavern over the famous entrance. However, their success encouraged others to venture into Undermountain and lose their lives."
> — wiki line 126 (refs `FRCS3e-180`, `CoS.W-54`; 3e and CoS:W)

**Campaign, Castle Ward, Durnan entry (day-one; the Well history is shared with Durnan)**
> "- He went down the Well with Mirt in the old days and built the tavern over it. He will not discuss what he saw there."
> — `campaign/gazetteer/waterdeep/castle-ward.md:100`

**Campaign, Castle Ward, Mirt entry**
> "- Hook: Mirt and Durnan went down the Well together in the old days, and Mirt names Harper ranks over dinner at his house."
> — `campaign/gazetteer/waterdeep/castle-ward.md:111` (the hook is a GM hook, not day-one lore; the Well fact is day-one)

### A5. Mansion, house and dinner manor

**Adventure, Castle Ward chapter**
> "On the opposite end of the mountain, close to the Naval Harbor, stands {@creature Mirt|WDH}'s Mansion. Once a fortress-like and glowering tower, it has been upgraded with more delicate fashions of architecture since the return of its long-absent owner."
> — `sources/adventure-wdh.json:31013`

**Wiki, mansion (ref `FR.CS-map2`, `VGtW-p11-12`)**
> "Mirt also owned a mansion in the [[Castle Ward of Waterdeep]], simply called [[Mirt's Mansion]]. It had a roughly hexagon-shaped, two-story main building with three-story towers at four of the six corners.<ref name="FR.CS-map2">{{Cite book/City System|Map 2}}</ref> It was located on the south face of [[Mount Waterdeep]] near the harbor at the intersection of [[Coin Alley]] and [[Tarnished Silver Alley]]. The estate could also be accessed from [[Smuggler's Dock]] in the harbor.<ref name="VGtW-p11-12" />"
> — wiki line 97 (edition not printed; `FR.CS` is the 3e City System map; Volo's Guide is 3e-era)

**Campaign, Castle Ward (the page's ruling for the mansion)**
> "- His mansion was once a fortress-like, glowering tower near the Naval Harbor, softened by new architecture since he returned. The page treats it as a Castle Ward residence, as the wiki (*Waterdeep and the North* 2e) and the Dragon Heist ward chapter do. The campaign's Harper events host Mirt's dinners at a manor in the Sea Ward behind the Naval Harbor, and those events are left as they are."
> — `campaign/gazetteer/waterdeep/castle-ward.md:110`

**Adventure, Harper recruitment (page 38)**
> "Lightsinger Theater is a high-end establishment located in the Castle Ward. If the characters meet {@creature Mirt|WDH} in his private box during the opera's intermission, he describes the Harpers and offers membership to eligible characters. Characters who accept receive a silver pin of a harp within a crescent moon, along with their first mission (see the Harpers Missions table). {@creature Mirt|WDH} also tells them that if they ever need to speak with him directly, they are welcome to visit his manor in the Sea Ward. If the characters do visit {@creature Mirt|WDH}'s manor, there's a {@chance 90|90 percent chance} that {@creature Mirt|WDH} isn't home and no one answers the door."
> — `sources/adventure-wdh.json:3842` (entry "Mirt", page 38)

**Campaign, Sea Ward gazetteer**
> "- Mirt, a Masked Lord and senior Harper, receives Harper members at a manor in the Sea Ward in the campaign's Harper events. Dragon Heist is itself split on his mansion: one line sends visitors to a manor in the Sea Ward, where he is home one time in ten (`adventure-wdh.json:3842`), and the ward chapter puts it near the Naval Harbor in the Castle Ward (`:31013`). By ruling 5 the mansion belongs to the **Castle Ward** page, and the Sea Ward holds only the Harper events' dinner house."
> — `campaign/gazetteer/waterdeep/sea-ward.md:162`

**Appendix B (Alexandrian, primary contact)**
> "**Contact: Mirt the Moneylender.** Mirt is the party's primary Harper contact. He presents himself as a bluff, jovial sea merchant grown fat on good wine, but is in fact one of the most politically dangerous men in Waterdeep — a senior Harper, a Masked Lord, and a close confidant of Open Lord Laeral Silverhand. He is warm, calculating, and never forgets anything. His manor in the Sea Ward is theoretically available for visits; in practice, he is almost never home."
> — `sources/Appendix_B_-_Player_Factions.md:62`

### A6. Time of Troubles, the Harpers and his return to Waterdeep

**Wiki (ref `FRE3-p32-33`, the 3e Waterdeep adventure; edition printed only by the ref)**
> "During the tumultuous [[Time of Troubles]] in [[1358 DR]], Mirt was dispatched to secure assistance from any ships friendly to Waterdeep. This included tasks such as supplying Waterdeep with much-needed goods, patrolling the seas for pirates, warning of other naval invaders, and providing a means of escape from the city should it become necessary. The job also led Mirt to the island of [[Mintarn]]."
> — wiki line 130 (ref `FRE3-p32-33`)

Wiki lines 132, 134, 137, 139, 141, 143 are novel-only (see G and F). Do not use them for the day-one page without the novel tag.

**Campaign, the Lords (day-one)**
> "- **Mirt** ... Laeral's closest advisor. His personal loans to Harper members leave them owing him a favor."
> — `campaign/gazetteer/waterdeep/castle-ward.md:108-109` (line 108 is "- A moneylender of great girth known as "the Old Wolf", who spends days on politics and nights on drink. He knows architecture well and will talk about it." and line 109 is "- Laeral's closest advisor. His personal loans to Harper members leave them owing him a favor.")
> "Mirt ... is a Masked Lord and Laeral's closest advisor" — `campaign/setting/history/07-a-city-watching-itself.md:42`: "- Mirt, a Masked Lord and a senior Harper, is her closest advisor. Elminster, the Warden of Waterdeep, answers to her. The Commander of the Watch reports to her."

**Campaign, history 07 (the Open Lord's household; Laeral since about 1489)**
> "Laeral Silverhand is the Open Lord of Waterdeep, and she has held the office since about 1489 DR. In that year the Masked Lords voted Dagult Neverember out and asked her to take his place. She is the fifth of the goddess Mystra's seven daughters, an archmage of great age and renown who was once the Witch-Queen of the North and the wife of the wizard Khelben Arunsun. She governs from the Palace with the help of trusted deputies and advisors, among them Mirt, and the city has been quiet under her."
> — `campaign/setting/history/07-a-city-watching-itself.md:76`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Tethyrian human moneylender, chaotic good, he/him*. Stat block: **Mirt (WDH custom block, CR 9; see the Harpers mechanics reference)**." — `campaign/setting/notable-figures/harpers/01-mirt.md:5`
- Campaign, Open Lord page: "**Mirt** (Chaotic Good, Tethyrian Human, he/him) is a moneylender known as the Old Wolf, and Laeral's closest advisor." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:40`
- Campaign, Castle Ward: "**Mirt (Chaotic Good, Tethyrian Human, he/him)**" — `campaign/gazetteer/waterdeep/castle-ward.md:107`
- Campaign, quest event tags (all say the same): e.g. "> Mirt (Chaotic Good, Tethyrian Human, he/him) :: a huge, gray-bearded moneylender and senior Harper, who is home for once and speaking plainly." — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:54`; the first-meeting tag reads "Mirt (Chaotic Good, Tethyrian human, he/him)" at `campaign/quests/faction-events/harpers/00-first-meeting/ev-01-first-meeting.md:157` (lowercase "human")
- Wiki: "| alignment5e    = [[Chaotic good]]" — wiki line 58 (5e). Also "| alignment3e    = [[Chaotic good]]" (line 47, 3e) and "| alignment2e    = [[Chaotic good]]" (line 44, 2e).
- Adventure: no alignment line in the Mirt entry (lines 32279-32305) or Appendix B lines 62 and 95-98.

**Species and ethnicity**
- Campaign: "Tethyrian human" (Summary line 5). "Tethyrian Human" (Castle Ward line 107).
- Wiki: "| race           = [[Human]]" (line 13) and "| ethnicity      = [[Tethyrian]]<ref name="CoS.W-p54-55" />" (line 14). Human is 5e-era infobox with no edition printed; ethnicity is cited to *City of Splendors: Waterdeep* (3e).
- Adventure: no species line in the Mirt entry. Appendix B line 62 says "a bluff, jovial sea merchant". Do not claim the adventure sets species.
- Settled by the user (Session 51) per `open-lord-and-masked-lords.md:109`: "> - **Settled by the user (Session 51):** Mirt's ethnicity is Tethyrian, as the wiki's Mirt infobox says (City of Splendors: Waterdeep, 3e). Dragon Heist gives none."

**Pronouns**
- Campaign: "he/him" (Summary line 5; the same tag in the Open Lord page line 40).
- Adventure: "{@creature Mirt|WDH} spends his days" and "he is the least concerned with concealing his identity" (`sources/adventure-wdh.json:32293`, `:32294`).
- Wiki: "| sex            = Male" (line 12).

**Stat block**
- Campaign, Summary: "Stat block: **Mirt (WDH custom block, CR 9; see the Harpers mechanics reference)**." (`01-mirt.md:5`)
- Campaign, mechanics reference: "Mirt is the WDH record (p.211), CR 9, AC 16, 153 HP. The block below is reformatted to 2024 style from that record. The numbers are unchanged." (`docs/plans/harpers-mechanics-reference.md:484`)
- Campaign, mechanics reference, on the NF page: "His NF page names the block \"Veteran with modifications\"; the WDH record is the one used here." (`docs/plans/harpers-mechanics-reference.md:531`)
- Campaign, mechanics reference table: "| Veteran (Mirt NF, Saeth NF) | **Warrior Veteran** | 3 | XMM p.320. Mirt uses the WDH CR 9 record instead. |" (`:571`)
- Campaign, mechanics reference: "| Mirt, Remallia, Vajra | Verified (WDH records) | Mirt CR 9, AC 16, 153 Hit Points; Remallia CR 9, no *Remove Curse*; Vajra CR 13. |" (`:598`)
- Campaign, r50 event: "Mirt uses the WDH record: CR 9, AC 16, 153 Hit Points, Initiative +4 (14), Passive Perception 15." (`campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:183`, the full line continues with the attacks)
- Adventure: the Mirt entry (`sources/adventure-wdh.json:32279` to `:32305`, pages 210-211) has the image, the description, and the Treasure subentry (`:32297` to `:32303`). It has no CR, AC, HP or attacks. The mechanics reference's "WDH record (p.211)" is not in the JSON. Check the printed page 211 before the stat line is treated as sourced.
- Wiki: "| challenge5e    = 9" (line 59) with "| refs5e         = <ref name="WDH5e-p210-211" />" (line 61). This is the only sourced CR. Class fields are blank for 5e (line 60).
- Wiki, earlier editions: "| challenge3e    = 13" (line 48) with "| class3e        = {{class table|edition=3e|[[Rogue]]|5|[[Fighter]]|8}}" (line 49). Not the 5e block.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/harpers/01-mirt.md`. The page has no Background, Personality or Connections section yet. Each row says where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Tethyrian human moneylender, chaotic good, he/him*. Stat block: **Mirt (WDH custom block, CR 9; see the Harpers mechanics reference)**." | Day-one name tag. Stat-block source does not verify (B, D2) | section B |
| 2 | L6 | "> - **Affiliation:** Harpers; Masked Lord of Waterdeep" | Day-one label, but its public-or-hidden status conflicts (D1) | `campaign/setting/organizations/01-harpers.md:98` ("Harper senior operative, Masked Lord") and D1 |
| 3 | L7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **The Talking Mare**, **The Dead Drop**, **The Doppelganger Auditions**, **A Friend's House**, **The Sleeping Asset**, **The Stone's Other Master**, **The Doppelganger Problem**, **The Dreamer's Reach**" | Quest-name list (not narrative). Brief ruling 1 says list quests under "Routed to quests" | `campaign/quests/faction-events/harpers/` folders and the Harpers Factions Guide (`02-harpers.md:68` to `:73`) |
| 4 | L11 | "**Resonance.** Mirt should inspire amusement with his prodigious appetite and deliberate vulgarity, respect for the adventuring legend beneath the fat, and unease when his generosity comes with invisible strings attached." | Day-one. Keep (ruling 3) | `sources/adventure-wdh.json:32294`; `01-harpers.md:35` |
| 5 | L13 | "**Emotions.** Mirt most often feels roaring amusement, political calculation behind the laughter, deep loyalty to old friends, nostalgic melancholy for Asper (his late wife), predatory enjoyment of power games, and genuine delight in architecture that catches his audience off guard." | Day-one. Keep | `sources/adventure-wdh.json:32294` (widowhood); wiki line 17 is not used |
| 6 | L15 | "**Motivations.** Mirt wants to protect Waterdeep from threats the Watch cannot see, keep the Harpers effective without getting his hands too dirty, and spend his nights exactly as he pleases because he has earned the right." | Day-one. Keep. Matches the Open Lord's Watch page (`campaign/setting/organizations/11-open-lords-watch.md:65`: "he wants to protect Waterdeep from threats the Watch cannot see") | `11-open-lords-watch.md:65` |
| 7 | L17 | "**Inspirations.** When playing Mirt, channel Robert Baratheon (*Game of Thrones*), Falstaff (*Henry IV*), and Winston Wolfe (*Pulp Fiction*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Mirt is \"the Old Wolf,\" a moneylender of prodigious girth who spends his days in politics and his nights in drink and debauchery. To those he trusts, he is a Masked Lord, a Harper, and Laeral Silverhand's closest advisor. Deep down, the years of adventuring left him with more than stories. He is unexpectedly knowledgeable about architecture and will engage on the subject; ask about his past and he'll say something that sounds like a joke but is not." | Day-one, but "To those he trusts, he is a Masked Lord" sits on the reveal conflict (D1). The rest matches `sources/adventure-wdh.json:32294` and `:32293` | `01-mirt.md:21`; `sources/adventure-wdh.json:32293` |
| 9 | L23 | "**Morale.** In a fight, Mirt would move with surprising speed, drawing hidden weapons. Despite his girth, he has not let his adventuring skills wither, and anyone who mistakes him for soft discovers the error exactly once." | Encounter register, not a quest event. Keep (ruling 3) | `sources/adventure-wdh.json:32294` |
| 10 | L25 | "**Relationships.** Mirt is a Masked Lord of Waterdeep, a Harper senior operative, Laeral Silverhand's closest advisor, a widower (Asper died years ago), and a moneylender whose personal loans to Harper members carry the weight of a favor owed rather than coin spent." | Day-one. Same D1 caveat on the Masked Lord clause | `01-harpers.md:73`; `sources/adventure-wdh.json:32294` |
| 11 | L29 | "A moneylender of prodigious girth known as \"the Old Wolf,\" a fixture of Waterdeep politics who mixes genuine generosity with a calculating eye for leverage and a past that makes people who underestimate him regret it." | Day-one. **36 words** (brief limit 21). Draft a shorter Overview | `sources/adventure-wdh.json:32293` |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/harpers.md`, "### Mirt", lines 7-25)**

Each line is listed with its status. Ruling 16 says a quest-time clause gets a day-one restatement and the profile is changed to match.

- Line 8 (tagline): "*A big, rumbling bon vivant who roars in public and goes quiet and exact the moment it's business.*" — day-one.
- Line 10 (Sound): "A deep, gravelly bass with a laugh that fills a room. In business he drops to a low, level murmur and stops laughing entirely." — day-one.
- Lines 11-15 (Sentence shape): "Two gears." with "Old Wolf (public)" and "Business: short, complete, declarative sentences with no ornament ("Sit. The first act is short.")." — day-one. The example "The first act is short" is the Harpers First Meeting scene (`campaign/quests/faction-events/harpers/00-first-meeting/ev-01-first-meeting.md`); keep as a sample of speech, not an event.
- Line 16 (Word choice): "...He calls younger people "lad" or "lass" and calls old friends by their first names." — day-one.
- Line 17 (Swearing): "*Punctuation · Artisan · Tirade.* Filthy and cheerful in public: \"fuck\", \"shit\" and bawdy jokes about bodies are part of the Old Wolf act. ... \"You wine-pissing, purse-pinching, velvet-arsed, gout-footed, bribe-sucking, chin-wobbling, three-faced Sea Ward cockwaffle, sit down before I sit on you.\"" — day-one. Swearing stays (adult table).
- Line 18 (Personality in speech): "...Asked about his past, he says something that sounds like a joke and isn't..." — day-one.
- Line 19 (Quirks): "He refills glasses without asking. He tilts his head slightly while he recalculates. He will talk architecture with real enthusiasm if anyone gives him the opening." — day-one.
- Line 20 (Signature phrases): "\"Sit.\" / \"Eat something first.\" / \"That's a debt, not a gift.\" / \"I am almost never home.\"" — day-one.
- Line 21 (Never): "He never begs, flatters, or uses a Harper code phrase in public, and never lets anyone see him hurry." — day-one.
- Line 22-25 (Sample lines):
  - Greeting (line 23): "Come in, come in, there's more fucking duck here than a man my size can decently finish, and gods know I've been trying for an hour. Sit." — day-one.
  - **Business (line 24): "Three names. You'll watch them for a tenday and tell me who they meet. Nothing more."** — possibly a quest-time brief. The line asks for a tenday of surveillance on three names. The Harpers quests use this pattern (Talking Mare, Doppelganger Auditions), so flag it. Suggested restatement is a drafter's call.
  - Under pressure (line 25): "I heard you. Now be quiet a moment while I decide how bad this is." — day-one.

**Quest-time clauses in the profile:** only line 24 is flagged. Lines 8 to 23 and 25 are day-one.

---

## D. Conflicts

**D1. Whether the Masked Lord office is public (the page's Summary and Persona assume it is known)**
- Open Lord page: "**Mirt** (Chaotic Good, Tethyrian Human, he/him) is a moneylender known as the Old Wolf, and Laeral's closest advisor. The published adventure names him as one of the Masked Lords and says he is the least concerned of them with hiding his identity. The campaign keeps his office from the party until the High Harper rank (see GM Notes). His mansion stands in the Castle Ward, and **Castle Ward** describes it." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:40`
- Open Lord page GM Notes: "> - **Mirt's reveal:** The published adventure says Mirt is the least concerned of the Lords with hiding his identity. The campaign overrides that on purpose. He mentions neither office at the **Harpers First Meeting**, and at the **High Harper** rank he tells the member that he is a Masked Lord and can be asked to act in that capacity once. Laeral knows it." — `open-lord-and-masked-lords.md:61`
- Castle Ward GM note: "> - Mirt is a Masked Lord and a senior Harper. He is the least careful of the Masked Lords about hiding it." — `campaign/gazetteer/waterdeep/castle-ward.md:115`
- Harpers Factions Guide, rank 50: "Mirt reveals that he is a Masked Lord of Waterdeep — if the party has not already worked it out — and can be asked to act in that capacity once (one request, one use)." — `campaign/guides/factions/02-harpers.md:62`
- Harpers organization page, Draft Notes, the settled ruling: "> - **Settled (ruling 25):** The Masked Lord office is public knowledge in the campaign, because Mirt's Notable Figures page lists it as an affiliation." — `campaign/setting/organizations/01-harpers.md:173`
- Harpers organization page, Draft Notes, the open conflict: "> - **Conflicts:** The Masked Lord reveal. `open-lord-and-masked-lords.md:40` and `:61` say the campaign keeps Mirt's office from the party and that he mentions neither office at the Harpers' first meeting. Ruling 25 and this page's Structure treat the office as public, and `castle-ward.md:115` calls Mirt \"the least careful of the Masked Lords about hiding it\". The Factions Guide (`02-harpers.md:62`) still stages a reveal at the top rank. Left to the user." — `01-harpers.md:175`
- Wiki: "He became a member of the [[Harpers]] as well as a [[Lords of Waterdeep|Masked Lord]] of [[Waterdeep]], which was commonly known." — wiki line 63 (3e)
- Adventure: "{@creature Mirt|WDH} ... of all the Masked Lords, he is the least concerned with concealing his identity." — `sources/adventure-wdh.json:32293`
- Alexandrian Appendix B: "**Contact: Mirt the Moneylender.** ... a senior Harper, a Masked Lord, and a close confidant of Open Lord Laeral Silverhand." — `sources/Appendix_B_-_Player_Factions.md:62`
- Higher rank: the user has not settled this. The brief's "Settled" list says the Summary keeps "Masked Lord of Waterdeep". Draft from the Summary and the Factions Guide, and list the conflict for the user.

**D2. Stat block source (CR and label)**
- Summary: "Stat block: **Mirt (WDH custom block, CR 9; see the Harpers mechanics reference)**." — `01-mirt.md:5`
- Mechanics reference: "His NF page names the block \"Veteran with modifications\"; the WDH record is the one used here." — `docs/plans/harpers-mechanics-reference.md:531`. The current Summary no longer says "Veteran". The reference is stale on this, or the page changed after the reference was written. Both are campaign files.
- Adventure: no CR, AC or HP in `sources/adventure-wdh.json:32279-32305`. The reference's "WDH record (p.211)" is not in the JSON.
- Wiki: CR 9 (line 59), citing WDH5e-p210-211.
- Higher rank: the wiki and the campaign agree on CR 9. The label "custom block" versus "record" is the campaign's choice. Left to the drafter and the orchestrator.

**D3. Harpers' knowledge of the Cassalanters (the Alexandrian PDF and Appendix B say they know; campaign says suspicion only)**
- Alexandrian PDF, PDF p.2 (printed p.24, transcription): "The **Harpers** know that the Cassalanters are actually demon-worshippers and, if they realize the PCs have gotten tangled up with them, will quickly warn them of the fact." — `sources/3. Player Character Factions.pdf` PDF p.2
- Alexandrian Appendix B: "The Harpers are aware that the Cassalanters are Asmodeus cultists and will move to warn and protect any PC with connections to them." — `sources/Appendix_B_-_Player_Factions.md:137`
- Campaign, Harpers org page: "The Harpers have watched the family's charitable work for years and found nothing, which they find suspicious. Mirt suspects the family's money and has no proof. The Harpers do not know what the family hides." — `01-harpers.md` Relationships line "**The Cassalanters (neutral, suspicious):**" (line 91 of the Factions Guide mirror is `02-harpers.md:7`: "Mirt has been building a dossier for two years and has not broken the surface.")
- Campaign Draft Notes: "> - **Conflicts:** The Cassalanters. `sources/Appendix_B_-_Player_Factions.md:137` (\"The Harpers are aware that the Cassalanters are Asmodeus cultists\") and `sources/3. Player Character Factions.pdf` (printed page 24) say the Harpers know. CLAUDE.md allows suspicion only, so the Beliefs bullet and the Relationships line say the Harpers do not know what the family hides." — `01-harpers.md:178`
- Higher rank: the campaign (Cassalanter secrecy, CLAUDE.md). Mirt's page must use suspicion only.

**D4. When Mirt first suspected the Cassalanters' money behind the Howling Hatred cult**
- Harpers org page: "About a year ago the Howling Hatred cult led Mirt to suspect Cassalanter money." — `campaign/setting/organizations/01-harpers.md:30`
- Harpers org page, Beliefs: "Mirt has kept a dossier for two years, and he suspects Cassalanter money stood behind the Howling Hatred cult about a year ago. He has no proof and wants some, and the Harpers do not know what the family hides." — `01-harpers.md:40`
- Factions Guide: "Mirt quietly tells a Harper character that he suspects Cassalanter money stood behind the Howling Hatred cult about a year ago, and that he wants proof." — `campaign/guides/factions/02-harpers.md:28`
- Fireball! event: "He suspects Cassalanter money was behind the Howling Hatred cult about a year ago, because the Watch released two of its members after a quiet word from someone at Cassalanter Villa." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:190`
- Superseded structure doc: "The Cassalanters funded the Howling Hatred cult three years ago; he quietly extracted their agents from Watch custody as a political courtesy." — `campaign/structure/arc-c-fireball.md:98`
- Higher rank: the quest journal (`ev-01-the-fireball.md:190`) and the org page agree on "about a year ago". `arc-c-fireball.md` is superseded and says "three years ago". Use "about a year ago".

**D5. Mirt's whereabouts and Laeral's start as Open Lord (wiki versus campaign)**
- Wiki: "In [[1491 DR]], [[Elminster]] and Mirt returned to the city of Waterdeep, both aiding the newly appointed Open Lord of Waterdeep, [[Laeral Silverhand]], in uncovering the culprits behind a string of murders of Masked Lords. After the investigations, Mirt chose to stay with Laeral, serving as a personal agent for the Open Lord." — wiki line 143 (ref `Death Masks`, a novel)
- Wiki: "Some time later, Mirt was forced to flee Waterdeep and sought refuge far to the south<ref name="SA-p1" />.  He founded, and subsequently became the head of [[Spelljammer Academy]], an institution for training [[spelljammer]] pilots located off the coast of [[Nimbral]]." — wiki line 146 (ref `D&D Beyond/Spelljammer Academy`, a web article)
- Campaign: "Laeral Silverhand is the Open Lord of Waterdeep, and she has held the office since about 1489 DR." — `campaign/setting/history/07-a-city-watching-itself.md:76`
- Campaign: "Mirt, a Masked Lord and a senior Harper, is her closest advisor." — `07-a-city-watching-itself.md:42`
- Adventure: "Today, an older and wiser {@creature Mirt|WDH} serves as one of the Masked Lords, a Harper, and a close advisor to {@creature Laeral Silverhand|WDH}." — `sources/adventure-wdh.json:32293`
- Adventure, Castle Ward: "{@creature Mirt|WDH}'s Mansion. Once a fortress-like and glowering tower, it has been upgraded with more delicate fashions of architecture since the return of its long-absent owner." — `sources/adventure-wdh.json:31013`
- Higher rank: the Dragon Heist adventure and the campaign agree that he is in Waterdeep as Laeral's adviser. The wiki's Spelljammer and 1491 lines are not canon for the campaign and are out of day one. Drafter should not write either.

**D6. Mansion and dinner manor**
- Adventure, recruitment: "{@creature Mirt|WDH}'s manor" in the Sea Ward (`sources/adventure-wdh.json:3842`). Adventure, Castle Ward: "stands ... close to the Naval Harbor" (`:31013`). Appendix B: "His manor in the Sea Ward is theoretically available for visits" (`sources/Appendix_B_-_Player_Factions.md:62`). Campaign resolves: mansion in the Castle Ward; dinner manor in the Sea Ward (`castle-ward.md:110`, `sea-ward.md:162`). The Harpers organization page settles it (Draft Notes, "Settled (ruling 25)"; `01-harpers.md:172`).
- Adventure, Lords' Alliance support: "{@creature Mirt|wdh} (see {@adventure appendix B|WDH|12}), a Masked Lord who serves as {@creature Laeral Silverhand|wdh}'s advisor, invites the adventurers to dinner at his dilapidated mansion as a pretense for sharing rumors and imparting pearls of wisdom." — `sources/adventure-wdh.json:1391` ("dilapidated" against the Castle Ward line "upgraded").

**D7. Lightsinger Theater (ward)**
- Adventure: "{@creature Renaer Neverember|wdh}..." not needed. Adventure, page 38: "Lightsinger Theater is a high-end establishment located in the Castle Ward." (`:3842`); the same JSON's `:3831` says "He bought you tickets to the opera tonight at the Lightsinger Theater in the Sea Ward." Campaign, Castle Ward (`castle-ward.md:93`) places it in the Castle Ward. Campaign, Harpers org page Draft Notes: "The published adventure puts it in the Sea Ward (`sources/adventure-wdh.json:3831`) and in the Castle Ward (`:3842`)." (that note is on the Remi page's sources; quoted on `01-harpers.md` Draft Notes via the Harpers page). The Castle Ward page is the campaign ruling.

**D8. Mirt on Thorvin's secret (the gate)**
- Thorvin page: "Mirt knows his secret" is day-one, based on `adventure-wdh.json:15161`.
- Adventure: "{@creature Mirt|WDH} shares this secret with any character who has renown of 4 or higher in the Harper faction." — `sources/adventure-wdh.json:15161`
- Factions Lair notes: "The Lair notes gate Mirt's tip at renown 1+ (`arc-f-xanathars-lair.md:31`)" (from `07-thorvin-twinbeard.md` Draft Notes line 149). It is a quest mechanic and is routed. Not a Mirt biography conflict.

**D9. Remi-facing conflicts that touch Mirt** are in the Remi notes file.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/structure/arc-c-fireball.md:98`: "The Cassalanters funded the Howling Hatred cult three years ago; he quietly extracted their agents from Watch custody as a political courtesy." Superseded by `campaign/quests/act-ii/fireball/`; the journal says "about a year ago" (`ev-01-the-fireball.md:190`).
- `campaign/structure/ch1-beginning.md:119`: "| Harper | Excellent | Mirt the Moneylender is a Harper; this background creates an immediate named contact |" (retired chapter file; do not use).
- `campaign/guides/gm-guide/player-factions-overview.md:55`: "> The senior Harper is **Mirt**, and at this rank he reveals that he is a Masked Lord of Waterdeep." Consistent with `02-harpers.md:62`, and conflicts with the Open Lord page's "keeps his office from the party until the High Harper rank" only in wording; it agrees on the rank.
- `campaign/setting/organizations/11-open-lords-watch.md:61`: "The Open Lord (superior): The Commander reports to Laeral, and her closest advisor, Mirt, is a Masked Lord (*Dragon Heist*, 5e; **A City Watching Itself**)." Consistent; not stale.
- `sources/Appendix_D_-_Running_the_Tavern.md:785`: "The Harpers — Mirt the Moneylender" (a tavern heading; the loan's terms agree with the campaign).
- `campaign/guides/trollskull-manor/02-operating-costs.md:94`: "| Mirt | Up to 500 gp | Favor, not coin | Indefinite; he calls it in when useful. Should feel like a shadow over every Harper ask. |" (consistent with `01-harpers.md:73`).

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**

Mirt's own quest appearances, by file, with the count of lines that name him (from a Grep of `Mirt|Remallia|Remi|Haventree` in each folder; the lines are quest-time and are routed):
- `campaign/quests/faction-events/harpers/00-first-meeting/ev-01-first-meeting.md` (43 lines)
- `campaign/quests/faction-events/harpers/m01-the-talking-mare/ev-01-the-talking-mare.md` (39)
- `campaign/quests/faction-events/harpers/m02-the-dead-drop/ev-01-the-dead-drop.md` (27)
- `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md` (30); `overview.md` line 19: "Mirt finds the eligible members in the common room of the Yawning Portal and takes them upstairs."
- `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md` (44); `ev-03-the-confrontation.md` (41)
- `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-02-the-extraction.md` (33)
- `campaign/quests/faction-events/harpers/m06-the-stones-other-master/ev-01-the-stones-other-master.md` (51)
- `campaign/quests/faction-events/harpers/r03-harpshadow/ev-01-harpshadow.md` (41); `r10-brightcandle/ev-01-brightcandle.md` (34); `r25-wise-owl/ev-01-wise-owl.md` (42); `r50-high-harper/ev-01-high-harper.md` (72)
- `campaign/quests/faction-events/harpers/s01-the-cell-is-compromised/ev-01-the-cell-is-compromised.md` (45)
- `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:190` ("**Harpers — Mirt (Renown 1+):** Takes a Harper member aside privately ...") and `ev-06-the-death-mark.md:66` ("**Mirt (Harpers, Renown 1+):** Identifies the mark without hesitation ...")
- `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:54` ("| Harpers | Mirt's personal loan — 500 gp | Repayable as a favor |")
- `campaign/structure/arc-c-fireball.md:259`, `arc-e-faction-outposts.md:369`, `arc-f-xanathars-lair.md:294`, `arc-g-cassalanter-villa.md:157, 367, 377, 385, 391`, `arc-h-sea-maidens-faire.md:288`, `arc-j-vault-of-dragons.md:252`: structure-doc briefings (superseded or pending conversion).
- `campaign/quests/act-ii/gralhund-villa/` (3 hits in `ev-01-what-the-factions-say.md`; 1 in `ev-09-aftermath.md`, 1 in `flowchart.md`, 1 in `overview.md`) and `campaign/quests/faction-events/force-grey/` and `lords-alliance/` (the Lords' events name Mirt) are routed.
- Adventure, quest-time (not day one):
  - `sources/adventure-wdh.json:10628`: "A character who has at least 4 renown in the Harpers can convince {@creature Mirt|WDH} (see {@adventure appendix B|WDH|12}) to use his authority as a Lord of Waterdeep to secure Fenerus's release. {@creature Mirt|WDH} has personally lost coin to the Blood Hawk Posse, so helping Fenerus squirm out of jail stings him deeply." (the coin fact is day-one; the release is a quest; see G)
  - `sources/adventure-wdh.json:14810`: "{@creature Mirt|WDH} (see {@adventure appendix B|WDH|12}) arrives with two female human {@creature swashbuckler|VGM} (see {@adventure appendix B|WDH|12}). If he's still alive and not already with the characters, {@creature Renaer Neverember|wdh} (see {@adventure appendix B|WDH|12}) replaces one of the swashbucklers." (quest time)
  - `sources/adventure-wdh.json:15159`: "Characters who belong to the Harpers can approach {@creature Mirt|WDH} (see {@adventure appendix B|WDH|12}), who knows the location of {@creature Xanathar|WDH}'s lair. (He has dealt with the beholder many times as a Lord of Waterdeep.)" (quest time; the second clause is day-one background)
  - `sources/adventure-wdh.json:15160`: "{@creature Mirt|WDH} leads the characters to a secret staircase in the Castle Ward sewers ({@area X1|271}). ..." (quest time)
  - `sources/adventure-wdh.json:26763`: "Delivering proof that {@creature Manshoon|WDH} is hiding in Waterdeep to {@creature Laeral Silverhand|WDH}, {@creature Mirt|WDH}, the Harpers, Force Grey, ..." (quest time)
  - `sources/adventure-wdh.json:26764`: "The ledger in {@area E13|430} also contains proof of {@creature Manshoon|WDH}'s malfeasance. Giving it to {@creature Laeral Silverhand|WDH}, {@creature Vajra Safahr|WDH}, {@creature Mirt|WDH}, or a magister provides enough evidence for them to act on." (quest time)
  - `sources/adventure-wdh.json:30308` (the Manshoon list of Masked Lords, see A7) and `:30294`-`:30300`
  - `sources/adventure-wdh.json:9028`: "...she shares any interesting revelations with {@creature Remallia Haventree|WDH} ... If Remallia learns the location of the Vault of Dragons, she sees that the information reaches the Lords of Waterdeep by conveying it to {@creature Mirt|WDH}." (quest time)
  - `sources/adventure-wdh.json:13620`, `:14753`: Laeral audience and Aurinax; Mirt is named as a route and as a prominent official (quest time)

Routed day-one-adjacent: the Lightsinger first meeting itself is the First Meeting event (`ev-01-first-meeting.md`).

**E3. Mirt's own Masked Lord status and the Manshoon list**
- `campaign/setting/history/07-a-city-watching-itself.md:71`: "- Manshoon's cell holds two Masked Lords through blackmail, and it keeps a ledger of five Lords it has identified: Mirt, Corylus Thann, Jelenn Urmbrusk, Thardouk Starbuckler and Dorgar Adarbrent."
- `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:63`: "> - **What anonymity does not protect:** The masks stop a stranger's bribe and do nothing against blackmail by someone who has learned a name. Manshoon keeps a list of five Masked Lords whose identities he knows. They are Mirt, Corylus Thann, Thardouk Starbuckler, Jelenn Urmbrusk and Dorgar Adarbrent, and he has checked off Corylus and Jelenn as the two he is blackmailing."
- Adventure: "Slipped into the ledger is a piece of paper with a list of names in {@creature Manshoon|WDH}'s handwriting. {@creature Manshoon|WDH} keeps this list of Masked Lords whose identities he knows, with check marks indicating the ones he's blackmailing:" — `sources/adventure-wdh.json:30299`. The list sits in the Kolat Towers ledger (`:30290`, under the table in a Kolat Towers area). The fact that Manshoon knows is a Manshoon fact; whether it is day-one or Kolat-Towers-only is a judgment for the drafter. Listed here, not in the Background.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth year, age, home town, parents.** No source gives any of these. The wiki's infobox `age` (line 16), `dob` (line 21) and `parents` (line 30) are blank. The only age terms are "older and wiser" (`sources/adventure-wdh.json:32293`), "As of the 1370s DR, he was old, fat, and wheezy." (wiki line 66, 3e) and "Mirt and Durnan emerged from Undermountain in the 1302" (wiki line 126). Consistent with the sources: he was adult in the 1300s DR and is older now. Do not give a birth year.

**F2. The Coaster father and the mercenary years.** Only the wiki (2e infobox ref `HoH-p86`): "son of a successful Coaster" (wiki line 102) and "a great mercenary general of the North" (line 104). No mercenary company or city is named. The Gray Hands membership of Asper is wiki-only (line 77).

**F3. Asper's rescue.** Only "whom he rescued as a baby from a sacked city" (wiki line 108). No city, no family, no date. Asper is dead ("passed away several years ago", `sources/adventure-wdh.json:32294`).

**F4. Children and heirs.** None in sources. The wiki's `children` field (line 33) is blank. Do not give Mirt children.

**F5. Why he left the adventuring life for Waterdeep.** The wiki says he "craved peace and tranquility" (wiki line 104) and "quickly became bored with peaceful living" (line 111). The campaign has no reason. Keep it to these two lines.

**F6. The absence before the return.** The adventure says the mansion has been upgraded "since the return of its long-absent owner" (`:31013`). The campaign does not say where he was. The wiki's Spelljammer Academy line (146) says he fled south; the campaign does not use it (D5). The drafter must not give a destination.

**F7. Personal goals beyond the Harpers and the Lords.** No source gives Mirt personal goals beyond "Mirt wants to protect Waterdeep..." (Motivations, `01-mirt.md:15`). Possible design material (must stay consistent with): the Motivations line; "a moneylender ... favor owed rather than coin"; his dossier on the Cassalanters (`01-harpers.md:40`), which he "wants" proof of. A personal goal about Asper's memory, a place (the Mansion, the Yawning Portal), or a craft (architecture) is allowed as `[design]`. Brief ruling 17 forbids revealing a secret, an Event Outcome or the Grand Game balance.

**F8. Architecture as a private interest.** The page's Emotions and Persona say he cares about architecture (`01-mirt.md:13` and `:21`). The adventure says the Mansion was "upgraded with more delicate fashions of architecture" (`:31013`) and the voice profile says "He will talk architecture with real enthusiasm if anyone gives him the opening" (`harpers.md:19`). No source says why. A reason is `[design]`.

**F9. His Lord's ensemble.** The adventure: "In addition to his other magical gear, {@creature Mirt|WDH} owns a {@item Lord's ensemble|wdh} (see {@adventure appendix A|WDH|11}). He dons the ensemble only when meeting with other Masked Lords in an official capacity." (`sources/adventure-wdh.json:32302`). A possession fact.

**F10. Other named associates (wiki only; do not add as Notable Figures).** Wiki line 81 to line 90 name Brian the Swordmaster (fellow Lord), Durnan (friend; Durnan's NF page exists), Ieiridauna Amalree (Watchghost of Mirt's Mansion, `ED-p15`), Krivvin Shamblestar (Amphail tavern), Loene (friend and former lover, `WatN-p53`), Nymara Scheiron ("Kitten"), Savengriff (a wizard Mirt restored to life), Thurn Samallahan, Transtra (Skullport), Trigol the Hearty (lost in Undermountain). The campaign does not name any of them for Mirt (Grep for Transtra, Loene, Nymara, Trigol, Amalree, Savengriff, Tonius, Sammereza: no matches in `campaign/`). Brief ruling 17 allows a named figure only if a source names them; these are wiki-only. Loene is a former lover named only by the wiki (`WatN-p53`), and the drafter may mention "a former lover" as `[research]` without the name.

**F11. Physical appearance.** The adventure: "broad-shouldered and barrel-chested" is the Alexandrian Appendix B's description (`sources/Appendix_B_-_Player_Factions.md:98`: "The man who rises to meet you fills most of the box. He is broad-shouldered and barrel-chested, with a grey beard trimmed without particular conviction and small, sharp eyes set in a face that has been lived in thoroughly."). Adventure: "prodigious girth" (`:32294`). The r50 event uses "gray-bearded" (quest tag). The wiki's Description: "he was old, fat, and wheezy" (line 66, 3e). Use the adventure and the Alexandrian Appendix B; the quest tags are routed.

**F12. Mirt's dossier and his doubt.** Campaign: "Mirt has been building a dossier for two years and has not broken the surface." (`campaign/guides/factions/02-harpers.md:7`) and "Mirt has kept a dossier for two years" (`01-harpers.md:40`). The day-one fact is the two-year dossier. The quest-time clauses are the Fireball! and Cassalanter scenes.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "Despite his prodigious girth, {@creature Mirt|WDH} can move with good speed when he must, and he hasn't let his adventuring skills wither. His wife, Asper, passed away several years ago, and his rambling mansion has seen better days." — `sources/adventure-wdh.json:32294`. (Grief for Asper; the mansion's decay.)
- "Mirt has survived the passing of centuries by means of magic" — `sources/adventure-wdh.json:32293`. (He is aware of his long life.)
- "He actually craved peace and tranquility, and realized he could not simply buy it, but would have to create it in the world." — wiki line 104 (2e). (A wish for peace.)
- "Within a month of his arrival ... [he was approached] ... with an invitation to become a Lord of Waterdeep." — wiki line 111 (2e). "quickly became bored with peaceful living" (same line).
- "He had a good heart and desired to make [[Faerûn]] a better place than he'd found it." — wiki line 69 (3e, `FRCS3e-p181-182`). (Quote: "Outwardly, Mirt appeared to be a loud and drunken braggart ... He had a good heart and desired to make Faerûn a better place than he'd found it.")
- "Mirt has personally lost coin to the Blood Hawk Posse, so helping Fenerus squirm out of jail stings him deeply." — `sources/adventure-wdh.json:10628`. (A grudge-adjacent day-one fact in the adventure. The clause is attached to a quest; the fact is that he lost coin.)
- "He is warm, calculating, and never forgets anything." — `sources/Appendix_B_-_Player_Factions.md:62`. ("never forgets anything" is a trait of a man who keeps loans.)
- "**Mirt's loan is a different kind of pressure.**" (Appendix D) — the favor he calls in. Use the loan facts above.
- "Mirt was sometimes seen wearing multiple artificial roses on his shoulder, signaling his interest to find several romantic partners to spend the night with." — wiki line 71 (ref `CF-LCF`, Candlekeep forum; not a canonical book). Use only if the drafter treats it as wiki lore.
- "He is unexpectedly knowledgeable about architecture and will engage on the subject; ask about his past and he'll say something that sounds like a joke but is not." — `campaign/setting/notable-figures/harpers/01-mirt.md:21` (the page's own line).
- "Asked about his past, he says something that sounds like a joke and isn't." — `campaign/setting/notable-figures/harpers/...` voice profile, `.claude/skills/character-voices/voices/harpers.md:18`.
- "he is the least concerned with concealing his identity" — `sources/adventure-wdh.json:32293` (see D1).
- "Mirt, Durnan, and Khelben were among the few adventurers to return alive from the [[Underhalls]]." — wiki line 120.
- "{@creature Mirt|WDH} has quite a history with {@creature Durnan|WDH}, the proprietor of the Yawning Portal." — `sources/adventure-wdh.json:31014`. (The old friendship; the wiki says Durnan "a good friend" in line 82.)
- "He will not discuss what he saw there." — `campaign/gazetteer/waterdeep/castle-ward.md:100` (said of Durnan; the shared Well).
- "Mirt's dossier" and "he wants proof" — `campaign/setting/organizations/01-harpers.md:40` (see F12).
- "He is quietly haunted: \"The children were innocent. I want you to know that I know that.\"" — `campaign/structure/arc-g-cassalanter-villa.md:391`. (Quest-time; a ending state. It shows a trait, not a day-one fact. Do not put it on the page.)
- Voice: "He never begs, flatters, or uses a Harper code phrase in public, and never lets anyone see him hurry." — `harpers.md:21`. "When he's genuinely fond of someone, the praise is brief and blunt (\"Good man.\")." — `harpers.md:18`.

---

## Cross-references (the Mirt topic in other files)

The Grep for `Mirt|Remallia|Remi|Haventree|Ulbrinter` across `campaign/` returns about 1,000 lines in about 120 files, most of them quest or faction-event files. Every file is listed with its count in E2 and in the table below. Day-one-relevant lines are quoted in sections A to D. The quest-time lines are routed and not reproduced one by one.

| File | Lines naming Mirt (approx.) | Relevance |
|---|---|---|
| `campaign/setting/organizations/01-harpers.md` | 47 (all Harper lines) | Day-one; quoted above |
| `campaign/guides/factions/02-harpers.md` | 18 | Mechanics; quoted above |
| `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md` | 14 | Day-one; D1, D6 |
| `campaign/gazetteer/waterdeep/castle-ward.md` | 16 | Day-one; A4, A5 |
| `campaign/gazetteer/waterdeep/sea-ward.md` | 8 | Day-one; D6 |
| `campaign/gazetteer/waterdeep/north-ward.md` | 19 (Remi, mostly) | Remi notes file |
| `campaign/setting/history/07-a-city-watching-itself.md` | 6 | Day-one; A6, D5, E3 |
| `campaign/setting/history/01-ahghairons-gifts.md:88` | 1 | "> - Mirt is the least careful of the Masked Lords about hiding who he is, and he wears the Lord's ensemble only to official meetings with the others." (D1) |
| `campaign/setting/organizations/11-open-lords-watch.md` | 9 | Day-one: lines 61 and 65 (A6, C6) |
| `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:25` | 1 | "**Relationships.** Laeral is the widow of Khelben Arunsun (the original Blackstaff), the Open Lord who counts Mirt as her closest advisor, ..." |
| `campaign/setting/notable-figures/independents-allies/03-durnan.md:25` | 1 | "**Relationships.** Durnan is the owner of the Yawning Portal, a reluctant acquaintance of Volo (whom he tolerates), a silent ally of Mirt, ..." |
| `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25` | 1 | "...a Harper-adjacent ally of Mirt and Remi Haventree, ..." |
| `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:28`, `:51`, `:98`, `:138` | 4 | Thorvin's Harper tie; "- **Mirt:** The Harper who knows Thorvin's secret. No file says whether Mirt recruited him `[research]`." (`:51`) |
| `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:138`, `:142` | 2 | Routed to **Faction Outposts** (`arc-e-faction-outposts.md:369`) |
| `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md` | 2 | Not checked line by line |
| `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md` | 4 | Not Mirt; the Mistshore fire |
| `campaign/guides/trollskull-manor/02-operating-costs.md:26`, `:80`, `:94` | 3 | "- **Harpers (Mirt):** Personal loan up to 500 gp, no stated interest — repayable as a favor when useful." (`:80`) |
| `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`, `:84`, `:88` | 3 | Not read in full; the Harpers' routed facts (per `01-harpers.md` Draft Notes) |
| `campaign/guides/gm-guide/player-factions-overview.md:55`, `:158` | 4 | `:158`: "| Harpers | **Mirt** (primary); **Remallia \"Remi\" Haventree** (secondary — identity withheld until Mission 4) | Intelligence on faction activity; protection of vulnerable NPCs; exposure of corruption |" |
| `campaign/guides/gm-guide/design-notes-running-the-campaign.md:107` | 1 | Not read in full |
| `campaign/structure/arc-*.md` (B to J) | 47 total | Superseded or pending; routed; E1 |
| `campaign/structure/ch1-beginning.md:119`, `:322` | 2 | Retired file; do not use |
| `campaign/quests/faction-events/harpers/` (all folders) | roughly 700 | Quest-time; routed (E2) |
| `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:54` | 1 | Loan (quoted in E2) |
| `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:190`, `ev-06-the-death-mark.md:15`, `:66` | 3 | Routed (E2, D4) |
| `campaign/quests/act-ii/gralhund-villa/` | 6 | Routed |
| `campaign/quests/faction-events/force-grey/`, `lords-alliance/`, `order-of-the-gauntlet/`, `emerald-enclave/` | about 20 | Routed |
| `campaign/setting/deities/*.md` | about 25 | Not read line by line; these name Mirt only in passing |
| `campaign/setting/geography/waterdeep.md` | 3 | Not read in full |
| `campaign/setting/lore/` | 0 hits for Mirt in the lore folder (not checked by the earlier Grep count) | |
| `campaign/setting/notable-figures/harpers/02-remallia-haventree.md` | 9 | Remi notes file |
| `sources/adventure-wdh.json` | about 25 lines | A, B, C, D, E2 |
| `sources/Appendix_B_-_Player_Factions.md` | 23 | A5, D1, D6 |
| `sources/Appendix_C_-_Player_Faction_Missions.md` | 14 | Quest-time (Maxeene, Bonnie, Ulbrinter party, Jarlaxle reveal) |
| `sources/Appendix_D_-_Running_the_Tavern.md` | 9 | A3 (loan), E1 |
| `sources/Act_III_Arc_D.md:549`, `:632` | 2 | "**Mirt the Moneylender (Harpers, Renown 1+):** Mirt turns the disk over in his fingers ..." (quest); "**Mirt the Moneylender (Harpers):** Mirt listens to the full account, refills his own glass, and thinks for a moment." (quest) |
| `sources/Act_III_Arc_E.md` | 0 | |
| `sources/SOURCE_GUIDE.md:172`, `:598` | 2 | "- Faction contacts: named NPCs with roles and how to find them (Mirt for Harpers, ...)" (`:172`); "- **Mirt the Moneylender as Harper contact:** How Mirt functions as more than just a faction contact — his history, his tavern network, and his personal stake in Waterdeep's power balance." (`:598`) |
| `docs/plans/harpers-mechanics-reference.md` | 27 | D2, B |
| `docs/plans/harpers-mechanics-reference.md:484`, `:531`, `:571`, `:598` | | quoted in B |
| `sources/research/pass5-bundles/harpers/wiki.txt:459` | 1 | "* [[Mirt the Moneylender]], a retired adventurer, merchant, and long-serving member of the Masked Lords of Waterdeep<ref name="WDH5e-p38,210">{{Cite book/Waterdeep: Dragon Heist|38,210}}</ref>" (5e) — a wiki line that cites the adventure for "Masked Lords" |
| `sources/research/pass5-bundles/harpers/wiki.txt:660-860` | | the same Mirt wiki page as the scratchpad extract |
| `sources/research/pass5-bundles/harpers/adventure-hits.txt` | 15 | Adventure hits; the adventure lines are quoted above |

---

## Not found

- Searched for: birth year, age, parents, siblings, children, home town, Coaster father's name, mercenary company name, Asper's city and family: `campaign/` (Grep for `Mirt`, `Asper`, `Asper|Arthagast`), `sources/adventure-wdh.json` (Grep for `Mirt`), `sources/*.md` (Grep for `Mirt`), `sources/research/` (Grep for `Mirt`), and the wiki extract (scratchpad `01-mirt.txt`). No match gives any of these.
- Stat block AC, HP and attacks in the adventure: `sources/adventure-wdh.json:32279` to `:32305`. Not present. The mechanics reference's "WDH record" is not in the JSON; the printed page 211 was not checked.
- Species in the adventure entry: not present (`:32279-32305`; Appendix B lines 62, 95-98).
- Personal goals in any source beyond Motivations: none.
- Alexandrian PDFs for Mirt: `sources/3. Player Character Factions.pdf` (PDF pp.1-3, printed pp.23-25) read; only the Harpers paragraph on PDF p.2 names the Harpers, and does not name Mirt. Not read: `sources/1. The Villains.pdf`, `sources/5. Faction Outposts.pdf`, `sources/11. Lair  Xanathar’s Lair.pdf`, `sources/17. Outpost and Lair Revelation Lists.pdf`, `sources/9. Lair – Sea Maidens Faire.pdf` (these were read for the Bregan D'aerthe note; not checked for Mirt).
- Wiki Mirt's Watchghost, Skullport informant and Mirt's Mansion details: wiki-only (lines 83, 122); not in campaign.
- Campaign sources for Mirt's alignment: the Summary and the quest tags state "Chaotic Good"; the adventure states none. The wiki's `alignment5e` (line 58) is the only source with a 5e alignment.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md` names no Harper or Mirt `.docx` in its topic list; the `Jarlaxle Baenre NPC Guide.docx` is named for Jarlaxle (`SOURCE_GUIDE.md:690`, from the Felrekt notes) and was not checked for Mirt.
- `sources/3. Player Character Factions.pdf`: read as images, not `pdftotext`. The Harpers quote is a transcription.
- The `campaign/quests/faction-events/harpers/` quest files were not read in full. They were searched with Grep, and the quotes from them are exact Grep output.
