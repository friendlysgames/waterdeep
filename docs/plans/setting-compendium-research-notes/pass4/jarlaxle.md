# Pass 4 research: `campaign/setting/villains/jarlaxle.md`

## Method and scope

- **Campaign files read in full:** `campaign/setting/villains/jarlaxle.md` (70 lines); `campaign/setting/organizations/07-bregan-daerthe.md`; `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md`; `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md`; `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md`; `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md`; `campaign/setting/history/03-bregan-daerthes-long-road.md`; `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md` (lines 1-30).
- **Bundle files:** `sources/research/pass4-bundles/jarlaxle/adventure.txt` (146 lines, read in full; excerpts of `adventure-wdh.json` at lines 513-566 and 32174-32260). `adventure-hits.txt` (147 lines, read in full). `wiki.txt` (1,875 lines): read lines 1-275 (Jarlaxle page), 300-479 (Bregan D'aerthe page), 481-586 (Nar'l Xibrindas page), 587-625 (linked Zardoz Zord page). Lines 626-1,875 (Luskan, Laeral and later pages) were checked only by grep. `campaign-hits.txt` is 595.7 KB; the Read tool refused it without `allow_large`, so I did not read it. My own greps of `campaign/` cover the same ground.
- **Direct greps of `sources/adventure-wdh.json`** (whole file): Lolth, Vessa, Kimmuriel, Zelifarn, Renaer, Nevercott, Rongquan, Erystian, Baenre, Luskan, Yvonnel, Doquaio, birth, "Eye", locket, magic mouth.
- **Direct greps of `campaign/`**: Jarlaxle, Zardoz, Nevercott, Lolth, Vessa, Kimmuriel, Renaer, "Who Zord Is", "Jarlaxle Unmasked", the outcome names.
- **There is no separate Zardoz Zord page in the campaign.** `campaign/setting/notable-figures/bregan-daerthe/` has twelve files; Zord is covered inside `01-jarlaxle-baenre.md`. The wiki has a linked Zardoz Zord page (`wiki.txt:587-625`).
- **Alexandrian PDF:** `sources/1. The Villains.pdf` has no text layer (7 pages, rendered as images). Quotes from it are transcriptions of page images and are marked "(transcribed from page image)".
- **Not read:** `sources/Act_III_Arc_D.md`, Alexandrian Appendix D, and the `.docx` files (section 10).
- **Edition tags:** The published adventure is *Waterdeep: Dragon Heist* (cited `WDH`). Wiki Jarlaxle infobox: `alignment5e = [[Chaotic neutral]]`, `challenge5e = 15`, `refs5e = WDH5e-p206` (`wiki.txt:65-68`). Wiki Zardoz Zord page cites "Waterdeep: Dragon Heist" (`W-DH-p131`, `wiki.txt:626`). The adventure's stat text uses XP-based CR, for example `"It has a challenge rating of 8 (3,900 XP)."` (`sources/adventure-wdh.json:32233`).
- **Session 47 rulings** are quoted as the campaign records them (history page, lines 160-164). I did not decide them.

---

## (1) Identity and core motive

**Published adventure, villain summary (Choose Your Villain, p. 6)**

> "{@creature Jarlaxle Baenre|WDH} is a drow swashbuckler and the secret lord of Luskan, the City of Sails. Jarlaxle plans to use the cache of dragons to buy his way into the Lords' Alliance, a confederation of cities and towns that band together against common threats. Jarlaxle also wants the {@item dragonstaff of Ahghairon|WDH} for leverage in his negotiations. In the magical guise of a human sea captain named Zardoz Zord, Jarlaxle runs a traveling carnival called the Sea Maidens Faire and lairs aboard a ship in Waterdeep's harbor that has a submarine (the {@i Scarlet Marpenoth}) underneath it, as described in chapter 7."
> — `sources/adventure-wdh.json:549`

> "Jarlaxle delights in thwarting his enemies, enjoys the complications that arise when adventurers try to meddle in his affairs, and loves to see the looks on their faces when he finally gets the better of them. He doesn't suffer fools who threaten him, however. If forced into a violent confrontation, he swiftly and brutally kills someone to make an example of them and then walks off."
> — `sources/adventure-wdh.json:550`

> "If you choose Jarlaxle as the villain, the adventure takes place in the autumn."
> — `sources/adventure-wdh.json:551`

**Published adventure, Appendix B (p. 206)**

> "{@creature Jarlaxle Baenre|wdh|Jarlaxle} is a flamboyant, swashbuckling drow iconoclast. He leads a renegade drow faction called Bregan D'aerthe, made up of disenfranchised male drow, most of them culled from destroyed or disgraced houses. Gifted with a sharp mind, a sense of humor, puissant skill with a blade, and a wealth of useful magic items, Jarlaxle infiltrated the city of Luskan, brought a kind of order to its lawlessness, and declared himself its secret lord."
> — `sources/adventure-wdh.json:32178`

> "Jarlaxle likes to weave a tangled web of schemes that leave his enemies baffled-the latest of which is a plan to legitimize Luskan by making it a member of the Lords' Alliance. The city's unsavory reputation has thwarted all previous efforts, and the current leaders of the Lords' Alliance have voiced their opposition to Luskan's admittance. A few have flatly declared that the city will never be welcome in the alliance. Nonetheless, Jarlaxle aims to persuade {@creature Laeral Silverhand|WDH}, the Open Lord of Waterdeep, to champion Luskan's cause-even if that means losing other alliance members in the process. Tying Luskan's fortunes to those of Waterdeep would increase Jarlaxle's political and economic power on the Sword Coast."
> — `sources/adventure-wdh.json:32179`

> "Jarlaxle's loyalties are to himself first and foremost, and to Bregan D'aerthe secondarily."
> — `sources/adventure-wdh.json:32182`

**Published adventure, Lords' Alliance (chapter 7 Sea Maidens Faire text; the line sits before the "Facing Jarlaxle" entry at `:22944`)**

> "Jarlaxle, the leader of Bregan D'aerthe, sees membership in the Lords' Alliance as his path to power beyond Luskan. As the secret lord of a city with an unsavory reputation, he has had a hard time getting a seat at the table with other cities of the North when it comes to trade and defense of the region. Thus, he plans to use the stolen gold to bargain with {@creature Laeral Silverhand|WDH} for inclusion in the alliance, and to oust Neverwinter and its lord Dagult Neverember-Jarlaxle's fiercest political opponent-from the group."
> — `sources/adventure-wdh.json:22941`

> "If he thinks the adventurers can be trusted, Jarlaxle proposes that they join his search for the Vault of Dragons. He intends to return the gold to {@creature Laeral Silverhand|WDH}, less 5,000 gp for the characters in exchange for their help."
> — `sources/adventure-wdh.json:22949`

> "Jarlaxle wants the Lords' Alliance to recognize his city, Luskan, as a new member, and he wants to push Neverwinter out of the alliance."
> — `sources/adventure-wdh.json:25467` (the reveal by Margo Verida and Khafeyta Murzan under compulsion; the list header is at `:25461`)

**Published adventure, Jarlaxle's letter to Laeral (`:26641-26654`)**

> "Your spies are to be commended! Rest assured, my presence in your fair city is purely recreational-though if fortune smiles upon me, this visit could benefit us both."
> — `sources/adventure-wdh.json:26648`

> "Why let Neverember get away with his crimes against Luskan and Waterdeep? Can we be allies, if not friends? These are the questions that haunt my dreams, as surely as I haunt yours."
> — `sources/adventure-wdh.json:26652`

> "In her mind, Luskan is a greedy pirate state that can't be trusted under any circumstances."
> — `sources/adventure-wdh.json:26667`

> "Harper spies in Luskan recently warned Laeral that Jarlaxle might be in Waterdeep. She reached out to him with a {@spell sending} spell to arrange this meeting, in the hope of finding out his plans."
> — `sources/adventure-wdh.json:26633`

**Wiki (Forgotten Realms Wiki, Jarlaxle, Personality; cites `RGLoD-p54-55`, *A Reader's Guide to R. A. Salvatore's the Legend of Drizzt*)**

> "More than anything, Jarlaxle was an opportunist. His wealth was considerable, but official station in drow society meant nothing to him."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:84`

**Campaign: current remix state**

> "1. **Lords' Alliance Membership for Luskan** — the real prize; Bregan D'aerthe's Luskan operations need political legitimacy; method: trade intelligence and an Eye to the PCs or directly to the Open Lord; contingency: if the avenue closes, Bregan D'aerthe continues without it — Jarlaxle loses a round, not the game; connects to **Vault of Dragons** political aftermath"
> — `campaign/setting/villains/jarlaxle.md:56`

> "Jarlaxle wants to return the gold to Laeral Silverhand — making the Open Lord personally indebted to him, which is worth more than the gold itself in his long-running project to secure Luskan's admission to the Lords' Alliance. He also wants the Stone of Golorr for Underdark political reasons that extend well beyond the surface campaign."
> — `campaign/setting/organizations/07-bregan-daerthe.md:50`

> "**Motivations.** Jarlaxle wants to buy Luskan's way into the Lords' Alliance using the dragon hoard, acquire the dragonstaff of Ahghairon for leverage over Waterdeep, and ensure that if everything falls apart, the submarine is fueled and ready."
> — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:16`

> "Jarlaxle's purpose in Waterdeep is intelligence — what the city's power structure looks like from the inside, which Masked Lords carry real weight with the Lords' Alliance council, and what it would take to buy Luskan a seat at that table. The half-million dragons in Neverember's vault are a welcome side opportunity. The political picture is the actual mission."
> — `campaign/guides/factions/08-bregan-daerthe.md:7`

> "Jarlaxle's Grand Game goal: hold Eye #3, collect political intelligence, keep all four villain factions sufficiently disrupted that none can move on the vault without the party's cooperation, position Bregan D'aerthe as the preferred **Sea Maidens Faire** ally, and use the vault gold — returned publicly to Waterdeep — to buy Lords' Alliance recognition of Luskan's reformed governance."
> — `campaign/guides/factions/08-bregan-daerthe.md:23`

> "Lords' Alliance membership is the latest of Jarlaxle's schemes in the published adventure, and Luskan's unsavory reputation has thwarted every earlier attempt. The Alliance's current leaders have voiced their opposition, and a few have declared that Luskan will never be welcome. He aims to persuade Laeral to champion the city, even if it costs the Alliance other members. The campaign makes this his main aim in Waterdeep (see **Jarlaxle Baenre** in Villains)."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:64`

> "- He also wants to oust Neverwinter and its lord, Dagult Neverember, from the Alliance. The published adventure calls Neverember his fiercest political opponent."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:65`

> "> - **Conflicts:** Lords' Alliance membership as the destination "the entire time" (`history.md` line 33). The published adventure calls it "the latest" scheme (`adventure-wdh.json` line 32179). The campaign calls it "the real prize" (`villains/jarlaxle.md` line 56) and "the reason he had come to Waterdeep" (`arc-h` line 13). The page follows the published adventure for the history and the campaign for the aim."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:157`

> "- **The carnival fleet:** wants a seat for Luskan in the Lords' Alliance and holds an Eye of the Stone. With **Jarlaxle Unmasked**, a character may name Jarlaxle Baenre and Zardoz Zord, and Laeral says only that she knows the first name."
> — `campaign/quests/faction-events/lords-alliance/m06-an-audience-with-the-open-lord/ev-01-an-audience-with-the-open-lord.md:202`

**Alexandrian remix (transcribed from page image; `sources/1. The Villains.pdf`, PDF p. 2 = printed p. 14)**

> Bullet: "Jarlaxle Baenre, a drow swashbuckler who is the secret lord of a city, leader of the dark elf mercenary group Bregan D'Aerthe, and has surreptitiously come to Waterdeep as the captain of a traveling circus"

**Alexandrian remix (transcribed from page image; PDF p. 5 = printed p. 17)**

> "As *Dragon Heist* begins, Jarlaxle is unaware of the *Stone of Golorr* or the Grand Game which is being played. His current agenda, as described in the campaign, is to convince the leaders of Waterdeep to support Luskan's bid to join the Lords' Alliance. Freshly arrived in his cover identity as Captain Zord of the Sea Maiden's Faire, Jarlaxle is coordinating and ramping up his local intelligence operations."

**Alexandrian Appendix B (markdown)**

> "Jarlaxle's goal is control of the Stone — either the artifact itself or its three Eyes."
> — `sources/Appendix_B_-_Player_Factions.md:780`

---

## (2) Background

### Origin of Bregan D'aerthe

> "Bregan D'aerthe is a company of mercenaries originally made up of the much-derided and dishonorable castaways of destroyed drow houses. The group's leader, {@creature Jarlaxle Baenre|WDH}, is always looking for new members to fill the ranks, and loyalty is what matters to him most."
> — `sources/adventure-wdh.json:1297`

> "Almost all Bregan D'aerthe members are male because female drow rarely condescend to take orders from a male. A female drow can earn a place in the faction by decrying the drow matriarchy and convincing Jarlaxle that she would be an asset to the brotherhood. Jarlaxle employs non-drow operatives as well, none of whom know they're working for him; such individuals aren't considered members of the faction."
> — `sources/adventure-wdh.json:1298`

> "Jarlaxle later left his house and his name (but not his connections) behind and founded [[Bregan D'aerthe]], a mercenary band of rogue males that grew to be very powerful. It could be said that the band forged its own underworld empire in Menzoberranzan."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:103`

> "Bregan D'aerthe was founded by the houseless rogue Jarlaxle, choosing to separate from the matriarchal drow society. It was built of mainly rogue drow males from destroyed houses of Menzoberranzan and [[Ched Nasad]]."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:362`

> "Jarlaxle begins the organization slowly having [[Arathis Hune]] as his first Lieutenant."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:367`

> "Jarlaxle left his house and its name, though not his connections, and founded Bregan D'aerthe."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:42`

### Baenre ties (wiki only; the adventure has no mother, house or birth-order text)

> "Jarlaxle was born to [[Yvonnel Baenre]], the [[matron mother]] of [[House Baenre]], the first house of Menzoberranzan. Due to the status of his birth order, Jarlaxle was to be sacrificed to [[Lolth]]. However, the sacrificial blade of Matron Baenre could not pierce the infant. Her second-oldest son, [[Doquaio Baenre]], was ordered to assist, but as he grabbed the infant, all of the kinetic energy of the attempted sacrifice was reflected on to him through the [[psionic]] power of the matron mother of [[House Oblodra]]. Doquaio was killed instead."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:96` (cites `RotP-p290-291`, `RotP-p296-297`, *Road of the Patriarch*; the same paragraph continues with Lolth's favor and his rejection of her, and with Kimmuriel's knowledge)

> "Bregan D'aerthe enjoyed relative freedom from the Ruling Council, mostly because of its close relationship with [[House Baenre]] (into which Jarlaxle had in fact been born)."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:353`

> "Jarlaxle was born to Yvonnel Baenre, the Matron Mother of House Baenre. The wiki cites Road of the Patriarch, Menzoberranzan: City of Intrigue and the Forgotten Realms Campaign Setting for his parentage, and the published adventure gives his surname as Baenre."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:33`

The adventure's Baenre hits are all the name string "Jarlaxle Baenre" (for example `sources/adventure-wdh.json:32174`, `"name": "Jarlaxle Baenre",`). A direct grep found no Yvonnel, Doquaio, birth or Kimmuriel line in the adventure.

### The third son question (unruled, per the handoff)

Campaign history, both sides as the page records them:

> "- A campaign docx calls him the third son, and the page keeps that. The wiki gives no number, but it calls Doquaio Yvonnel's second-oldest son and says Jarlaxle was slated for sacrifice because of his birth order, which implies at least a third son (Forgotten Realms Wiki, Jarlaxle Baenre; Road of the Patriarch)."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:38`

> "> - **Research:** "The third son" is from the Jarlaxle NPC Guide docx (lines 51 and 62). The wiki calls Doquaio the second-oldest son (`Jarlaxle_Baenre.txt` line 96) and has Jarlaxle slated for sacrifice by birth order, which implies at least the third. The page keeps "third"."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:148`

Wiki side (no number is given for Jarlaxle; the words "third son" do not appear in the Jarlaxle page):

> "Her second-oldest son, [[Doquaio Baenre]], was ordered to assist"
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:96`

Handoff (the "unruled" list):

> "- [ ] **Unruled conflicts (left alone, defaults noted in the checker reports):**"
> — `session 49 handoff.md:135` (rest of the passage covers: Vajra's tenure, Meloon's devourer timing, Savra's departure, alignment differences, Kalain's stat block, Jalester's species, the Xanathar predecessor count, the Cassalanter gold, and Osvaldo's alignment)

> "\"third son\" for Jarlaxle; Kimmuriel omitted;"
> — `session 49 handoff.md:135` (same line as the quote above)

Consistency note:

> "15 [research] answer 03:38,147 "third son": W:Jarlaxle_Baenre:96 calls Doquaio Yvonnel's "second-oldest son"; Jarlaxle slated for sacrifice "due to birth order" (implies at least third). Default: keep "third"."
> — `docs/plans/setting-compendium-research-notes/consistency-history-vs-wiki.md:22`

A different person is also called "third son" in the bundle, so it should not be confused with Jarlaxle: `sources/research/pass4-bundles/cassalanters/wiki.txt:54`, "*[[Caladorn Cassalanter]]: The third son of the family who forewent his family to embark on adventure".

### Rise, Luskan and the Baenre-era business

> "The company ships goods from the surface to Menzoberranzan, and the wiki says it traded Netherese artifacts there by way of Luskan."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:55`

> "For example, they traded [[Netherese]] artifacts to Menzoberranzan via Luskan."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:331`

> "Over [[1376]] to [[1377 DR]], Jarlaxle and Bregan D'aerthe manipulated events in [[Luskan]] that resulted in the destruction of the [[Host Tower of the Arcane]], the death of [[Deudermont]], and Luskan becoming a free port."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:123`

> "By [[1483 DR]], the drow agent [[Beniago]], disguised as a [[human]], was [[High Captain]] [[Kurth]]."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:397`

> "Luskan is a free port on the northern Sword Coast. Five High Captains rule it, and each leads a faction called a Ship."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:59`

> "After 1485 DR the High Captains trade legally across the Sword Coast and are secretly under the sway of Jarlaxle and the company. The published adventure says he infiltrated Luskan, brought a kind of order to its lawlessness and declared himself its secret lord."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:62`

> "The Sea Maidens Faire, owned and operated by Zord, is a seafaring carnival based in Luskan that travels along the Sword Coast. It provides good, wholesome entertainment in the form of fantastic street parades."
> — `sources/adventure-wdh.json:4744`

### Arrival in Waterdeep and the Sea Maidens Faire

> "Jarlaxle has come to Waterdeep in the guise of an Illuskan human named Zardoz Zord. \"Captain Zord\" is the master of the Sea Maidens Faire, a carnival that travels up and down the Sword Coast in three ships: the {@i Eyecatcher}, the {@i Heartbreaker}, and the {@i Hellraiser} (all words that describe Jarlaxle). He spends most of his time aboard the {@i Eyecatcher}, his personal ship. The other two vessels carry members of the carnival and their parade wagons."
> — `sources/adventure-wdh.json:32180`

> "Jarlaxle has forged an alliance with Lantan (an island to the south), and has armed his Bregan D'aerthe lieutenants with Lantanese firearms that rely on magical {@item smokepowder|WDH} to function. He has also acquired a Lantanese submarine called the {@i Scarlet Marpenoth}. This underwater vessel is mounted below the {@i Eyecatcher} and kept out of sight. Jarlaxle plans on using the submarine to flee Waterdeep if his scheme unravels."
> — `sources/adventure-wdh.json:32181`

> "A year ago, the Sea Maidens Faire visited the island nation of Lantan, where Jarlaxle obtained a Lantanese submarine and several clockwork servants."
> — `sources/adventure-wdh.json:25468`

> "Zord visits the distant island of Lantan about once a year. During his last visit, he purchased four nimblewrights from a Lantanese wizard. He keeps two aboard his flagship, and one aboard each of the other two vessels."
> — `sources/adventure-wdh.json:4746`

> "Zardoz Zord, owner of the Sea Maidens Faire, has brought his three ships to Waterdeep. Two of these galleons, the {@i Heartbreaker} and the {@i Hellraiser}, are docked. Zord's flagship, the {@i Eyecatcher}, is anchored in Deepwater Harbor. Each of the three ships (described in chapter 7) has at least one nimblewright aboard."
> — `sources/adventure-wdh.json:4711`

> "Although Zardoz Zord ({@creature Jarlaxle Baenre|WDH}) commands the fleet, each ship has its own captain: a Bregan D'aerthe {@creature drow mage} disguised as a slender, well-dressed human. These captains know of Jarlaxle's plans. They communicate with each other and with Jarlaxle by way of {@spell sending} spells, which they prepare instead of {@spell fly}."
> — `sources/adventure-wdh.json:23023`

> "The {@i Eyecatcher}, the {@i Heartbreaker}, and the {@i Hellraiser} are crewed by twenty sailors each: three {@creature drow elite warrior||drow elite warriors} (mates) and seventeen {@creature drow}, all magically disguised as slender humans while aboard their vessel. All are loyal members of Bregan D'aerthe, and all know that Zardoz Zord is {@creature Jarlaxle Baenre|WDH} in disguise. They know nothing about the {@i Scarlet Marpenoth} or Jarlaxle's plans."
> — `sources/adventure-wdh.json:23047`

Campaign:

> "The Sea Maidens Faire already exists as one of Jarlaxle's legitimate business enterprises. It is a traveling carnival based in Luskan that tours the Sword Coast in three ships, the *Eyecatcher*, the *Heartbreaker* and the *Hellraiser*, under Captain Zardoz Zord. Zord is Jarlaxle in the magical guise of an Illuskan human."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:72`

> "Bregan D'aerthe is skilled at infiltrating criminal organizations. Nar'l Xibrindas became Xanathar's only advisor and persuaded it to eliminate its other advisors. He has been in place one year, since 1491 DR."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:75`

> "Before the campaign opens, Jarlaxle has an agent inside Xanathar's Guild and the *Scarlet Marpenoth* moored in Deepwater Harbor. The Faire's carnival fleet and its parades arrive in the harbor on Ches 21 for Fleetswake, Ches 21 to 30. He arrives in Waterdeep already knowing of the Stone, the three Eyes and the vault, and Nar'l's reports keep him current. The nimblewright ledger puts him in the city no later than Marpenoth 3, 1491 DR."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:76` (rest of the passage covers: "Eye #3 reaches him aboard the *Scarlet Marpenoth* on the night before Ches 1, lifted from Xanathar's hideout by agents already inside it (see **The Open Lord's Fall**).")

> "The Faire leaves Waterdeep at dawn on Tarsakh 20."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:77`

> "Jarlaxle Baenre had been in Waterdeep since Marpenoth of 1491."
> — `campaign/structure/arc-h-sea-maidens-faire.md:9`

> "The Scarlet Marpenoth had lain moored in the harbor all year, and the night the fleet arrived it took its place beneath the Eyecatcher."
> — `campaign/structure/arc-h-sea-maidens-faire.md:11`

> "Nine nimblewrights sold to nine wealthy households at 25,000 gold pieces each — a steal, and deliberately so."
> — `campaign/structure/arc-h-sea-maidens-faire.md:13`

> "The Eye had reached him the night before Ches 1, through Bregan D'aerthe intelligence work — the same network that had placed Nar'l Xibrindas inside Xanathar's Guild a year earlier, in 1491."
> — `campaign/structure/arc-h-sea-maidens-faire.md:15`

Session 47 rulings and conflicts (campaign history):

> "**Settled by the user (Session 47):** When Jarlaxle learned of the vault. "He's known about it since getting to Waterdeep, whenever that was." The body has him arrive already knowing, and the nimblewright ledger (first sale Marpenoth 3, 1491 DR) puts his arrival no later than that."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:160`

> "**Settled by the user (Session 47):** How long the company has been in Waterdeep. Jarlaxle is in the city by Marpenoth 3, 1491 DR (the nimblewright ledger), and the *Scarlet Marpenoth* has been moored in the harbor all year."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:162`

> "**Conflicts:** The nimblewrights. Luskan technomancers built them (the Alexandrian `1. The Villains.pdf` p.17; `Act_III_Arc_D.md` lines 271 and 467) against a Lantanese wizard (`adventure-wdh.json` line 4746). The count is four in the published adventure and nine in `arc-h` line 13."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:163`

> "Built by the technomancers of Luskan, he's brought several dozen of these constructs with him and is selling them at surprisingly compelling prices."
> — `sources/1. The Villains.pdf`, printed p. 17 (transcribed from page image; the bullet begins "NIMBLEWRIGHTS: One of Jarlaxle's main objectives right now is the sale of nimblewrights.")

---

## (3) Disguises and the hidden identity

### The campaign's rule

Full text of the page's entry paragraph:

> "**Entry and Activation:** Two separate mechanics govern Bregan D'aerthe in this campaign. **Membership** runs during **Trollskull Alley**, like any other faction: drow lieutenants shadow the party for several days, then J.B. Nevercott (Jarlaxle in disguise, posing as a haberdasher) visits Trollskull Manor and offers enrollment to any interested PC. The only gate is party action — if the party reported the watchers to the Watch, the **BD Contact Severed** flag closes the faction for the campaign. The **Ryvarra Identified** flag (from **The Neighbors** event in **Trollskull Alley**) changes how the visit opens, not whether it happens. **Villain activation** is a separate track: Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep, and he enters the Grand Game as a named player at the table when the **Jarlaxle Informed** flag is set during **Fireball!** and read in **Gralhund Villa**. The flag records only that the party spoke directly with him. It does not mean he learned anything, and it gates his Bregan D'aerthe team at **Gralhund Villa** and his Phase 1 Zardoz Zord activity. His identity stays hidden behind J.B. Nevercott and Zardoz Zord until **Sea Maidens Faire**. The personality phases below key off the Jarlaxle Informed flag, not BD membership. See: **GM Guide: Session Zero**; **GM Guide: Player Factions Overview**; **Bregan D'aerthe** organization page."
> — `campaign/setting/villains/jarlaxle.md:3`

Campaign text that conflicts with that rule (section 8, C1):

> "Jarlaxle's true identity surfaces in **Fireball!** and **Sea Maidens Faire**, when the nimblewright thread leads the party to the carnival and its captain."
> — `campaign/guides/gm-guide/player-factions-overview.md:182`

> "Mark for each character who learns Zord's true name through **Who Zord Is**, and record the character's name. Read by every Bregan D'aerthe event (no Bregan D'aerthe speaker says "Jarlaxle" to a member until it is marked), by the Harper mission **A Friend's House** (a marked member knows the name behind Zord and that he wears personas), and by **Sea Maidens Faire**."
> — `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:135` (outcome heading at `:134`: "#### Jarlaxle Unmasked (per character)")

> "The party can learn that Captain Zord is Jarlaxle Baenre in two ways during this event:"
> — `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:108`

> "**The ledger.** Both folios open with the seller's line, "Sold through the Eyecatcher, J. Baenre, for the Company."" (rest of the passage covers: a DC 14 Intelligence (History) check identifies the name.)
> — `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:110`

> "**The cabin.** A Bregan D'Aerthe member taken to his private cabin (below) sees the persona drop. He names himself."
> — `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:111`

> "J.B. Nevercott is Jarlaxle Baenre in a *hat of disguise*, so nobody in the room can describe his face afterward. He never admits to being anyone else, even if a player guesses, and nobody in this Event says Jarlaxle's name aloud. **Jarlaxle Unmasked** is marked later, for each member separately. Until then, Bregan D'aerthe speakers say "the captain" or "J.""
> — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:22`

> "Nevercott never admits to being anyone but J.B. Nevercott, even to a character who guesses correctly. The guess does not mark **Jarlaxle Unmasked**, which a later event sets. He enjoys the guess and answers:"
> — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:268`

> "Nobody here says the name Jarlaxle in speech or readaloud unless **Jarlaxle Unmasked** is marked for the member being addressed. Until then every Bregan D'aerthe speaker says "the captain" or "J.""
> — `campaign/quests/faction-events/bregan-daerthe/s03-dinner-with-zardoz/ev-01-dinner-with-zardoz.md:26`

> "Captain Zardoz Zord is Jarlaxle Baenre, and he is the secret lord of Luskan. Nothing in the Overview links him to the company, and the party learns the link in **Sea Maidens Faire**."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:86`

> "**Never reveal:** That Captain Zardoz Zord is Jarlaxle. That Jarlaxle was marked for sacrifice to Lolth as an infant and rejected her. That Soluun's disownment is a cover story. A player who asks a company member about Lolth gets contempt and nothing about where the company comes from."
> — `campaign/setting/deities/lolth.md:81`

> "He does not acknowledge that J.B. Nevercott and Zardoz Zord are the same person, even when both have been seen by the same party member — this is the kind of thing he finds amusing. After Mission 4, he dispenses with J.B. Nevercott but remains Zardoz Zord until **Sea Maidens Faire**, where the party meets the real Jarlaxle Baenre."
> — `campaign/setting/organizations/07-bregan-daerthe.md:11`

Published adventure on the same rule:

> "Jarlaxle is a consummate actor who never lets down his guard. Even if the characters discern his true identity, he never admits to being anything other than what he pretends to be."
> — `sources/adventure-wdh.json:3602`

> "Jarlaxle owns a {@item hat of disguise} but doesn't need it to hide his true form while he's aboard any of his ships. His disguise (and the disguises of his drow subordinates) can be dispelled only by destroying the ship's figurehead (see chapter 7). If the characters somehow discern his true form, Jarlaxle gives the party a slow nod of his head, dryly says \"Bravo!\" and lets them make the next move."
> — `sources/adventure-wdh.json:4751`

> "The figureheads on Jarlaxle's ships ({@area J8|36d}) create illusions around drow crew members, making them appear human. If a figurehead is destroyed, the drow on that ship remain belowdecks to ensure that they don't draw unwanted attention."
> — `sources/adventure-wdh.json:22965`

> "\"Zardoz Zord is master of the Sea Maidens Faire. If you want to meet him, talk to a ship captain.\" (A sailor won't divulge Zord's true identity unless magically compelled to do so.)"
> — `sources/adventure-wdh.json:23052`

> "\"The Sea Maidens Faire and all its ships are under the command of Captain Zardoz Zord of Luskan.\" (A ship captain won't divulge Zord's true identity unless magically compelled to do so.)"
> — `sources/adventure-wdh.json:23032`

> "Zardoz Zord is a drow named Jarlaxle in disguise."
> — `sources/adventure-wdh.json:25465` (under the header at `:25461`: "If separated from Jarlaxle and compelled to divulge information about their host, Margo and Khafeyta reveal some or all of the following facts:")

> "On the other hand, if the characters try to confront the drow spies, they avoid contact but leave behind a black eye patch as a calling card. The next day, {@creature Jarlaxle Baenre|WDH} (see {@adventure appendix B|WDH|12}) shows up at the party's headquarters, using his {@item hat of disguise} to appear as a haberdasher named J.B. Nevercott. In this guise, he asks to speak privately with drow characters who he thinks might make suitable Bregan D'aerthe recruits. Only drow are given serious consideration, but Jarlaxle doesn't care if they're male or female. As a test, he offers them their first mission."
> — `sources/adventure-wdh.json:3601`

Other disguises in the adventure:

> "Before the characters leave the alley, {@creature Jarlaxle Baenre|WDH} (see {@adventure appendix B|WDH|12}) uses his {@item hat of disguise} to approach them in the guise of {@creature Laeral Silverhand|WDH}, the Open Lord of Waterdeep:"
> — `sources/adventure-wdh.json:7144`

> "He uses his {@item hat of disguise} to appear as a young actor from Luskan named Erystian Demarne. A successful {@dc 24} Wisdom (Insight) check is needed to out Jarlaxle."
> — `sources/adventure-wdh.json:3874`

> "The owner of the theater is a burly and jovial Shou man with a braided goatee named Rongquan Mystere—another of Jarlaxle's many disguises."
> — `sources/adventure-wdh.json:9066`

> "Rongquan Mystere",
> — `sources/adventure-wdh.json:281` (a bare string; its surrounding context was not read)

### Overview-safe facts

The page has no Overview section. Its headings are Entry and Activation, Personality Phases, Relationships, Goals and Cross-References.

The company's player-facing Overview, as written:

> "Bregan D'aerthe is a drow mercenary company that began in the Underdark city of Menzoberranzan, made up mostly of men from houses that were destroyed or disgraced. It hires out soldiers, scouts and go-betweens, and its agents are said to deal in information with anyone who can pay. On the surface it is said to have a foothold in Luskan, a free port on the northern Sword Coast that five High Captains rule and that Waterdeep regards as a pirate state. This spring the Sea Maidens Faire, a traveling carnival out of Luskan, brings three ships and Captain Zardoz Zord to Deepwater Harbor for Fleetswake."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:81` (under `## Overview`, `:79`)

The villain's persona as the NP page's Overview:

> "A flamboyant Illuskan sea captain running the Sea Maidens Faire carnival out of Deepwater Harbor, theatrical, immediately charming, with a precision behind the showmanship that most people don't notice until the conversation is already over."
> — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:30` (under `## Overview`, `:28`)

The organization page's Overview, which the history page flags as not player-safe (section 8, C12):

> "Bregan D'aerthe is a mercenary company of drow exiles and surface operatives, led by Jarlaxle Baenre, running the Sea Maidens Faire carnival as cover for a city-wide intelligence network. He has positioned his people inside every major faction in Waterdeep. Joining him means working for the most capable operator in the city — one who will treat his agents well until their interests diverge from his."
> — `campaign/setting/organizations/07-bregan-daerthe.md:58`

> "> - **Conflicts:** `organizations/07-bregan-daerthe.md` line 58 names Jarlaxle as the leader and describes a city-wide intelligence network in its Overview. That does not follow the Zardoz Zord rule and is not player-safe."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:165`

The history page's rule for its own Overview:

> "**Tone:** Grave and played straight, in the Ember history register. Jarlaxle's flamboyance belongs to Jarlaxle and the narration stays plain. The Overview gives only the company's rumor-level face, and the GM bullets state facts flatly."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:90`

The Players' Guide names the faction only (grep of `campaign/guides/players-guide/` for Jarlaxle, Zardoz, Nevercott: no matches):

> "| Bregan D'aerthe | Exceptional intelligence; rare resources | Loyalty, and eventually a favor that reaches beyond Waterdeep |"
> — `campaign/guides/players-guide/faction-affiliations.md:15`

### Persona and location facts

> "Zardoz Zord was a disguise donned by [[Jarlaxle Baenre]] used to infiltrate the city of [[Waterdeep]] in the late 15{{th}} century [[DR]]. The Sea Maidens Faire was a cover operation to hide the fact that Jarlaxle was searching for the ''[[Stone of Golorr]]''. However, Jarlaxle performed in the Sea Maidens Faire's parades under the guise of Zardoz Zord purely for the fun of it."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:629` (Zardoz Zord page; edition `W-DH-p131`)

> "A magic mouth trap on the door to J30 triggers if anyone other than Zord opens it (DC 16 Intelligence (Arcana) to detect), releasing a sound like a gong audible throughout the aft castle."
> — `campaign/locations/sea-maidens-faire/04-eyecatcher-zords-office.md:5` (J29, Guest Cabin)

> "**J30 — Captain's Main Cabin:** Jarlaxle's private space. The magic mouth trap, the jade chess set (2,500 gp, kept on a side table), a nimblewright guard standing in the corner, and a trapdoor in the floor — arcane locked (Jarlaxle's key or DC 20 Dexterity (Thieves' Tools)) — opening to the Scarlet Marpenoth's pressurized hatch collar (U1)."
> — `campaign/locations/sea-maidens-faire/04-eyecatcher-zords-office.md:7`

---

## (4) Relationships

The page's table (`campaign/setting/villains/jarlaxle.md:45-52`) is quoted in section 5 where status matters. Evidence for each relationship follows.

### Nar'l Xibrindas

Page row (`jarlaxle.md:47`):

> "| Nar'l Xibrindas | Embedded spy | Inside Xanathar's Guild; Jarlaxle's most valuable asset; Jarlaxle has a contingency if Nar'l is discovered (has not shared it with Nar'l) |"

- Adventure: "Jarlaxle has a spy in the Xanathar Guild: the advisor {@creature Nar'l Xibrindas|wdh}, who uses {@spell sending} spells to transmit intelligence to his drow brethren." — `sources/adventure-wdh.json:15149`
- Adventure: "{@creature Xanathar|WDH}'s advisor is a nervous and conniving male drow named {@creature Nar'l Xibrindas|wdh}." — `sources/adventure-wdh.json:32323`
- Adventure, the same paragraph: "If forced to decide between himself and Bregan D'aerthe, he'll choose the former and betray his drow allies to save his own skin." — `sources/adventure-wdh.json:32323`
- Adventure, Jarlaxle suspects a betrayal: "Jarlaxle suspects that {@creature Nar'l Xibrindas|wdh}, his spy in the Xanathar Guild, has betrayed him and is now using the resources of Bregan D'aerthe to help the beholder retrieve the stone." — `sources/adventure-wdh.json:7153`
- Adventure, Compromised Eye mission: "Jarlaxle identifies the traitor as a drow mage named {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) and furnishes the characters with a route to {@creature Xanathar|WDH}'s lair through underground passageways." — `sources/adventure-wdh.json:3634`
- Adventure, the staircase: "These drow also have secret orders to kill {@creature Nar'l Xibrindas|wdh}, if he's still alive, and retrieve Jarlaxle's bag of holding (see {@area X35|2c7})." — `sources/adventure-wdh.json:15150`
- Wiki: "[[Jarlaxle]] too believed that Nar'l was double-crossing Bregan D'aerthe and was willingly working with the beholder." — `sources/research/pass4-bundles/jarlaxle/wiki.txt:554` (Nar'l page; cites `WDH5e-p64`)
- Campaign NP: "bitter awareness that Jarlaxle would sacrifice him without hesitation if the cost were right." — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:14`
- Campaign NP: "To Jarlaxle, he is Bregan D'Aerthe's best intelligence source on Guild movements, reporting via Sending spell after one year in place, placed in 1491 DR." — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:22`
- Campaign GM Guide: "Nar'l Xibrindas, Xanathar's own senior advisor, reports to Jarlaxle by *Sending* spell." — `campaign/guides/gm-guide/grand-game-in-play.md:63`
- Alexandrian Appendix B: "Jarlaxle's spy inside Xanathar's council is his most valuable single asset in Waterdeep." — `sources/Appendix_B_-_Player_Factions.md:781`
- The "contingency" is not found in the adventure, the Alexandrian appendices or the wiki.

### Manshoon

Page row (`jarlaxle.md:48`):

> "| Manshoon | Mutual wariness | Non-interference arrangement, fragile; Jarlaxle has better intelligence and intends to keep it that way |"

- Campaign: "Jarlaxle and Manshoon maintain a fragile non-interference arrangement. Each considers the other the only genuine peer in the Grand Game, and neither wants direct conflict while other factions are more immediate problems. The arrangement is under strain: Manshoon has identified Fenerus Stormcastle as a Bregan D'aerthe cut-out and ordered his abduction." — `campaign/guides/gm-guide/grand-game-in-play.md:65` (rest of the passage covers: "If that abduction proceeds, Jarlaxle will act unilaterally, and the non-interference collapses.")
- Campaign: "| Jarlaxle | Mutual wariness | The only Grand Game player Manshoon takes seriously; non-interference arrangement, fragile; Jarlaxle has better intelligence and both know it |" — `campaign/setting/villains/manshoon.md:34`
- Campaign: "| **Manshoon vs. Bregan D'aerthe** | Escalating interference | Manshoon has identified Fenerus Stormcastle as a D'aerthe cut-out and ordered his abduction." — `campaign/guides/gm-guide/running-the-villains.md:75` (rest of the row: "Krebbyg Masq'il'yr has flagged the Zhentarim surveillance to Jarlaxle. If the abduction proceeds, Jarlaxle's Trades Ward intelligence network is directly compromised.")
- Adventure, the only line that puts them in one scene: "The forces sent by {@creature Xanathar|WDH}, the Cassalanters, and {@creature Manshoon|WDH} attack the characters on sight. Jarlaxle, on the other hand, congratulates characters for unlocking the Vault of Dragons and allows them to leave on the condition that they go empty-handed." — `sources/adventure-wdh.json:14786` (no relationship is stated)

### Xanathar

Page row (`jarlaxle.md:49`):

> "| Xanathar | Target of management | The beholder is being handled via Nar'l's selective intelligence; Jarlaxle prefers a controlled beholder to a power vacuum |"

- Campaign: "Jarlaxle's relationship with Xanathar is more managed. Nar'l Xibrindas, Xanathar's own senior advisor, reports to Jarlaxle by *Sending* spell. The intelligence Nar'l provides has been selectively curated to keep the beholder occupied and predictable; Jarlaxle's goal is a manageable Xanathar, not a dead one." — `campaign/guides/gm-guide/grand-game-in-play.md:63`
- Campaign: "| Jarlaxle | Unknown | Not yet identified as a player; the beholder is paranoid about anything operating in its territory without its knowledge |" — `campaign/setting/villains/xanathar.md:52`
- Adventure: no direct Jarlaxle–Xanathar line. The link is through Nar'l: "{@creature Xanathar|WDH}'s drow advisor, {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}), is actually a Bregan D'aerthe spy." — `sources/adventure-wdh.json:1301`

### Renaer Neverember

Page row (`jarlaxle.md:50`):

> "| Renaer Neverember | Political connection | Worth cultivating; Renaer's relationship with Laeral is an indirect path to the Open Lord's attention; Renaer doesn't know who he met |"

- Campaign: "**Eye #3** — held by Jarlaxle Baenre, aboard the *Scarlet Marpenoth*. It began in Renaer Neverember's mourning locket." — `campaign/guides/gm-guide/running-the-villains.md:25` (rest of the passage covers the Zhentarim seizure, the Candle Lane warehouse raid and the BD lift)
- Alexandrian (transcribed from page image, printed p. 16): "Renaer didn't know it: His father had given him an elaborate, ivory mourning locket in honor of his mother. The Eye was hidden inside it."
- Adventure: no Jarlaxle–Renaer line. Renaer appears only in the Harper, Zhentarim and Floon sections (`sources/adventure-wdh.json:1688`, `:1802`, `:2106`, `:2113`).
- The page's claim that Renaer "doesn't know who he met" has no source I found.

### The Cassalanters and Vessa

Page row (`jarlaxle.md:51`):

> "| The Cassalanters | Aware but uninvested | Knows about their infernal bargain through intelligence; not interested in getting involved unless strategic upside appears |"

- Campaign rule: "> - **The one exception:** Jarlaxle knows about the pact through **Vessa**, his doppelganger spy in the Cassalanter social circle. He never tells Bregan D'aerthe members unless they work it out themselves." — `campaign/setting/organizations/10-cassalanters.md:71`
- Campaign: "> - Outside the household, only Jarlaxle knows what the family has done. Everyone else is suspicious of them and nothing more." — `campaign/setting/history/05-a-debt-in-blood.md:29`
- Campaign: "> - The one exception is Jarlaxle, who learned it through Vessa, his doppelganger spy in the Cassalanter social circle. He does not tell Bregan D'aerthe members unless they work it out themselves." — `campaign/setting/history/05-a-debt-in-blood.md:89`
- Campaign NP: "He alone outside the household and the cult knows of the Cassalanter pact, through his doppelganger spy Vessa." — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:26`
- Vessa NP: "Vessa (full name Lymeria Lhaurilstar) is a Bregan D'aerthe doppelganger operative embedded in the Cassalanter social scene under a permanent human cover, Jarlaxle's primary intelligence source on the Cassalanter operation throughout **Cassalanter Villa**" — `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:26` (rest of the passage covers her uses for BD party members and her role in the Eye #3 adjustment)
- Adventure, the closest line: "Jarlaxle has written an exposé on devil worship among unnamed Waterdavian noble families. The story mentions orgies and secret deals happening behind closed doors. (Jarlaxle never passes up a chance to rattle the nobility and sow political unrest.)" — `sources/adventure-wdh.json:3624`
- Adventure, the Cassalanter section: "Victoro and {@creature Ammalia Cassalanter|WDH} are Waterdavian nobles and secret devil worshipers. The Cassalanters plan to use the cache of dragons to buy back the souls of their children, which they traded to Asmodeus for power." — `sources/adventure-wdh.json:538`
- Adventure: no Vessa and no pact knowledge for Jarlaxle (direct grep).
- Name collision: "Four doppelgangers from the Yawning Portal have slipped into the party disguised as nobles. Their leader, {@creature Bonnie|WDH} (see \"Familiar Faces\"), poses as a minor noblewoman going by the name Lymeria Lhaurilstar; she was hoping to have a fun night at the party, but she's willing to help the characters if they need aid." — `sources/adventure-wdh.json:20414` (Founders' Day party)

### Zelifarn

Not on the page's relationship table.

- Adventure: "Zelifarn, a {@creature young bronze dragon}, recently moved into Deepwater Harbor. He has spent the past several months scouring wrecks at the bottom of the harbor for treasure and stashing precious baubles in a hidden underwater cave. Recently, he noticed a strange craft mounted on the underside of the {@i Eyecatcher}." — `sources/adventure-wdh.json:26604`
- Adventure reward: "If they tell him more about the contents of the submarine and he believes that they're being truthful, he gives them the promised reward: an old chest with a rusted lock that can be busted or pried open with a successful {@dc 13} Strength (Athletics) check." — `sources/adventure-wdh.json:26611`
- Campaign NP: "- **Affiliation:** None (friendly to Bregan D'aerthe; not an operative)" — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:6`
- Campaign NP: "**Relationships.** Zelifarn is the young bronze dragon of Deepwater Harbor, on friendly terms with the *Eyecatcher*'s crew but answerable to none of them, and the source of a genuine reward (300 sp, a golden octopus amulet, and a *scroll of revivify*) for parties willing to trade information about the Scarlet Marpenoth's contents." — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:25`
- Campaign org (conflicting): "- **Zelifarn** — Young sea dragon (bronze-scaled) stationed aboard the *Scarlet Marpenoth*. See the **Zelifarn** page in Notable Figures." — `campaign/setting/organizations/07-bregan-daerthe.md:39`

### Kimmuriel Oblodra

Not on the page.

- Campaign history: "Yvonnel, Doquaio and Gromph Baenre, Arathis Hune, Beniago and Kimmuriel Oblodra are wiki names with no campaign page. The wiki lists Kimmuriel as co-leader and by 1463 DR as the band's widely understood leader. The campaign has Jarlaxle as sole leader, so the body leaves Kimmuriel out." — `campaign/setting/history/03-bregan-daerthes-long-road.md:151`
- Campaign history: "**Default kept:** Kimmuriel Oblodra stays omitted from the body (`Bregan_D_aerthe.txt` lines 9, 109 and 119 make him co-leader and the "widely understood leader" by 1463 DR). Adding him would contradict the campaign's single-leader company, and no campaign page uses him." — `campaign/setting/history/03-bregan-daerthes-long-road.md:152`
- Consistency note: "16 missing (USER decision): Kimmuriel Oblodra, co-leader and "widely understood leader" by 1463 (W:Bregan_D_aerthe:9,109,119); deliberately omitted (03:150). Default: keep omitted." — `docs/plans/setting-compendium-research-notes/consistency-history-vs-wiki.md:23`
- Wiki: "| leader         = [[Jarlaxle]], [[Kimmuriel Oblodra]]" — `sources/research/pass4-bundles/jarlaxle/wiki.txt:308`
- Wiki: "As time went on (by [[1463 DR]], Kimmuriel became widely understood as the band's leader," — `sources/research/pass4-bundles/jarlaxle/wiki.txt:408`
- Wiki: "By [[1490 DR]], Artemis Entreri was considered Jarlaxle’s second-in-command and Kimmuriel remained as joint leader alongside Jarlaxle." — `sources/research/pass4-bundles/jarlaxle/wiki.txt:109`
- Adventure: no Kimmuriel line (direct grep).

### Soluun Xibrindas

Not on the page's table. Campaign NP 01 names him as an employee: "the employer of Soluun, Fel'rekt, and Krebbyg" (`campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:26`).

- Adventure: "Soluun is a sadistic, fanatical bully who is fiercely loyal to Bregan D'aerthe, and to Jarlaxle in particular." — `sources/adventure-wdh.json:32040`
- Adventure: "He conceals his nighttime escapades as well as he can, but Jarlaxle, Fel'rekt, and Krebbyg know what he's up to." — `sources/adventure-wdh.json:32041`
- Campaign NP: "**Relationships.** Soluun is the elder brother of Nar'l Xibrindas (whom he despises), a lieutenant of Jarlaxle (whom he worships), and a serial killer whose disownment by Bregan D'Aerthe is a cover story: he carries forged BD identification." — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:26`
- Campaign org: "Jarlaxle is aware and hasn't yet decided what to do about it." — `campaign/setting/organizations/07-bregan-daerthe.md:36`

### Fenerus Stormcastle

Not on the page's table.

- Adventure: "If Jarlaxle is the villain, the stone is delivered to Fenerus Stormcastle, a lamplighter in the Trades Ward. Fenerus has a criminal history and is currently in trouble with the law." — `sources/adventure-wdh.json:6171`
- Adventure: "The characters visit the residence of Fenerus Stormcastle, a lamplighter and retired brigand who funnels information to Bregan D'aerthe." — `sources/adventure-wdh.json:6709`
- Adventure: "He has no clue that his contacts are drow members of Bregan D'aerthe, since they wear cloaks and keep to the shadows." — `sources/adventure-wdh.json:7124` (the same paragraph begins "Until recently, Fenerus supplemented his income by spying for the city of Luskan")
- Campaign NP: "- **Affiliation:** Bregan D'aerthe (cut-out; believes his contacts are Luskan agents)" — `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:7`
- Campaign NP: "a Bregan D'Aerthe cut-out and message-drop on Quill Alley (unknowing; he believes his contacts are Luskan agents)" — `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:26`
- Campaign org: "Collects messages from Fenerus Stormcastle's house every two days and carries them to the *Scarlet Marpenoth*." — `campaign/setting/organizations/07-bregan-daerthe.md:38`
- Campaign org (conflicting): "Supposed to be a cut-out, but once followed Krebbyg after a pickup and knows the messages go to the Sea Maidens Faire." — `campaign/setting/organizations/07-bregan-daerthe.md:40`
- Campaign: "Manshoon has identified Fenerus Stormcastle as a Bregan D'aerthe cut-out and ordered his abduction." — `campaign/guides/gm-guide/grand-game-in-play.md:65`

### Others (no page row)

- Margo and Khafeyta: "Margo and Khafeyta both joined the Sea Maidens Faire within the past year-Margo as a lyrist, Khafeyta as an acrobat. Jarlaxle has taken a romantic interest in both women, who are also in love with each other." — `sources/adventure-wdh.json:25459`
- Yalah: "If Jarlaxle is the main villain, he and Yalah are secret lovers. He has promised to facilitate her rise in power after he uses Lord Neverember's lost hoard to buy Luskan's way into the Lords' Alliance." — `sources/adventure-wdh.json:4811`

### The PCs

Page row (`jarlaxle.md:52`):

> "| The PCs | Most interesting variable | Has been watching since **Finding Floon** (Nar'l's reports reached him, and his agents were in the Xanathar sewer hideout); knows their names, faction ties, and general competence by **Sea Maidens Faire** |"

- Adventure: "If one or more characters are drow, {@creature Jarlaxle Baenre|WDH} has his lieutenants, three {@creature drow gunslinger|WDH|drow gunslingers}, shadow these potential new recruits while keeping a safe distance." — `sources/adventure-wdh.json:3592`
- Adventure: "The characters have piqued Jarlaxle's curiosity. He doesn't know much about them (yet) and wants to determine whether they pose a threat (they don't)." — `sources/adventure-wdh.json:4740`

---

## (5) Goals and methods: the page's phases and goals, with support status

Statuses: **Supported**, **Partly supported**, **Contradicted**, or **No source** (campaign design only).

**Phase 1 (universal), `jarlaxle.md:13`**

> "| Acts I–II *(Zord activity keyed to the party's contact: Jarlaxle Informed)* | The disguise; a plausible, theatrical Illuskan eccentric who is too observant; PCs may like him before they know who he is; the performance holds but the intelligence behind it keeps slipping through |"

Status: **Partly supported.** Theatrical and observant: `sources/adventure-wdh.json:3602` ("consummate actor"), `:32178` ("flamboyant, swashbuckling"), and "The adventurers receive an invitation to dine with Zardoz Zord aboard his flagship, during which Jarlaxle takes their measure and offers assistance if they impress him." (`:1306`). "Keyed to Jarlaxle Informed" and the intelligence "slipping through": **No source.**

**Phase 1 trigger, `jarlaxle.md:15`**

> "*Trigger to Phase 2:* PCs penetrate the disguise, or Jarlaxle decides they've earned the reveal. Either way, "Zardoz Zord" ends here."

Status: **No source.** The adventure says Nevercott "never admits" (`:3602`) and Zord gives "a slow nod" when discerned (`:4751`).

**Adversary track 2A, `jarlaxle.md:23`**

> "| 2A | The Unmasked | **Sea Maidens Faire** (adversary path) | True identity revealed without negotiation; Jarlaxle is gracious about it — he respects the attempt and doesn't rage; the deal is no longer on the table, but the disdain is minimal; he treats them like colleagues who chose the wrong firm |"

Status: **Partly supported.** Graciousness: `sources/adventure-wdh.json:4751` ("dryly says \"Bravo!\" and lets them make the next move"). Violence: `:550` ("If forced into a violent confrontation, he swiftly and brutally kills someone to make an example of them and then walks off."). The non-agreement branch: "If the characters don't agree to Jarlaxle's terms, or if they assault him, he tries to knock them {@condition unconscious} and leave them without clothes or equipment in a gutter in the Dock Ward." (`:22950`). "Without negotiation" conflicts with the adventure's order of events, where the offer comes first (`:22949`). The timing at Sea Maidens Faire conflicts with the campaign's own unmask timing (section 8, C1).

**Adversary track 3A, `jarlaxle.md:24`**

> "| 3A | The Graceful Enemy | **Sea Maidens Faire** onward, adversary | He doesn't hunt them, but he doesn't help them either; Nar'l's intelligence is redirected to protect Bregan D'aerthe's position; he may counter-heist them (recover what they took), may simply outmaneuver them; the posture is professional, not vendetta |"

Status: **Partly supported** for the posture: "He has them watched but doesn't provoke hostilities until such time as the reward clearly outweighs the risks." (`sources/adventure-wdh.json:26697`). Also: "If the characters sink or steal one of his sailing ships or the {@i Scarlet Marpenoth}, Jarlaxle tasks his crew members with finding out what went wrong." (`:22974`). "Nar'l's intelligence is redirected" and "counter-heist": **No source.** The adventure says Nar'l would betray the drow to save himself (`:32323`).

**Trigger to 3A, `jarlaxle.md:26`**

> "*Trigger to Phase 3A:* PCs successfully steal the Eye, or the confrontation resolves without an alliance."

Status: **No source** (the Eye is campaign-only).

**Ally track 2B, `jarlaxle.md:34`**

> "| 2B | Jarlaxle in the Game | **Sea Maidens Faire** (ally path) | True identity revealed as an invitation; negotiates as an equal; his offer (Eye for Lords' Alliance membership for Luskan) is genuine and he'll honor it; he's charming because it's easier than not being charming, not because he's performing |"

Status: **Partly supported.** Honoring the deal: "If the characters accept, Jarlaxle upholds his end of the agreement. Once the gold is secure, he gives the characters their cut." (`sources/adventure-wdh.json:22949`). The adventure's offer is gold and the dragonstaff: "He offers another 5,000 gp for their help in recovering the {@item dragonstaff of Ahghairon|WDH}." (`:22949`). **The Eye as the price: No source** (the adventure has no Eyes, section 9). "Negotiates as an equal" and "not because he's performing": **No source**; the adventure says "Jarlaxle is a consummate actor who never lets down his guard" (`:3602`).

**Ally track 3B, `jarlaxle.md:35`**

> "| 3B | The Patron | **Sea Maidens Faire** onward, ally | Asset rather than adversary; provides intelligence, drow operatives, the Faire as a safe house; the political favor comes due at **Vault of Dragons**; he'll remind them once, gracefully, that what he wants hasn't changed |"

Status: **Partly supported.** "Jarlaxle offers to help the characters if they agree to help him secure the gold for Waterdeep and the {@item dragonstaff of Ahghairon|WDH} for himself." (`sources/adventure-wdh.json:14801`). "Bregan D'aerthe support comes in these ways:" (`:1301`), and the Faire as "a front" (`:1299`). The favor at the Vault: "At Dread Lord renown: Jarlaxle proposes returning the gold publicly, in the party's name, to Laeral Silverhand — in exchange for a letter of introduction to the Lords' Alliance council." (`campaign/guides/factions/08-bregan-daerthe.md:33`). "Safe house": no source.

**Trigger to 3B, `jarlaxle.md:37`**

> "*Trigger to Phase 3B:* PCs choose alliance, accept the deal, or formally join Bregan D'aerthe."

Status: **No source** for the trigger. Joining is open: "The group's leader, {@creature Jarlaxle Baenre|WDH}, is always looking for new members to fill the ranks" (`sources/adventure-wdh.json:1297`).

**Goal 1, `jarlaxle.md:56`** (quoted in section 1)

Status: **Supported** for the aim (`sources/adventure-wdh.json:32179`, `:22941`, `:549`). "Trade intelligence and an Eye to the PCs": **No source**. "Jarlaxle loses a round, not the game": **No source**.

**Goal 2, `jarlaxle.md:57`**

> "2. **One Eye of the Stone** — as a bargaining chip, not for personal use; method: he already holds Eye #3 aboard the *Scarlet Marpenoth* (Bregan D'aerthe agents inside Xanathar's hideout lifted it the night Xanathar's Guild raided the Zhentarim warehouse), and Nar'l's intelligence tells him where the other Eyes are; keep it as the bargaining chip and move on the others before the other factions consolidate; contingency: negotiating it from the PCs is also acceptable and preferable for the relationship; connects to **Sea Maidens Faire**"

Status: **Partly supported.** The Stone as an aim: "He steers the characters toward the {@item Stone of Golorr|WDH} and lets them think they're always one step ahead." (`sources/adventure-wdh.json:6702`); Alexandrian Appendix B `:780`. The Eye, the bargaining chip and the BD lift: **campaign-only** (`running-the-villains.md:25`; history `:76`, `:163`; arc-h `:15`). The adventure's bargaining chip is the dragonstaff (`:549`, `:14786`).

**Goal 3, `jarlaxle.md:58`**

> "3. **Waterdeep as Permanent Base** — the Sea Maidens Faire is seasonal; Jarlaxle wants Bregan D'aerthe with a permanent Dock Ward presence; method: be indispensable to whoever resolves the vault situation; this is the long play that outlasts Dragon Heist"

Status: **Contradicted** in part by the campaign's own departure rule: "Tarsakh 20 | Sea Maidens Faire departs at dawn | Eye #3 leaves Waterdeep; alliance path with Jarlaxle closes; **Sea Maidens Faire** must be completed before this date" (`campaign/guides/gm-guide/structural-rules.md:50`), and "The Faire leaves Waterdeep at dawn on Tarsakh 20." (`history:77`). The adventure's exit plan: "Jarlaxle plans on using the submarine to flee Waterdeep if his scheme unravels." (`sources/adventure-wdh.json:32181`). "Seasonal" is supported by "a traveling carnival" that "travels up and down the Sword Coast" (`:32180`). "Permanent Dock Ward presence": **No source**.

**Key design note, `jarlaxle.md:60`**

> "**Key design note:** Jarlaxle is the only villain whose faction (Bregan D'aerthe) the PCs can join."

Status: **Supported** that the faction is joinable (`sources/adventure-wdh.json:1297`, `:3601`). "Only villain" is a campaign claim.

**Wiki on his method (edition RGLoD)**

> "Jarlaxle preferred to avoid killing someone as long as that person could be manipulated to serve his interests, no matter how small his or her role might be."
> — `sources/research/pass4-bundles/jarlaxle/wiki.txt:90`

This supports the page's "reluctant to kill" framing in the phase rows. It contrasts with `sources/adventure-wdh.json:550` (the adventure's brutal example).

---

## (6) Bregan D'aerthe rejects Lolth: every line

### Campaign lines that mention Lolth with Bregan D'aerthe, Jarlaxle, Soluun or Nar'l

Standing rule and the lines built on it:

> "- **Bregan D'aerthe (standing rule):** Bregan D'aerthe has rejected Lolth as its goddess. No member worships her, keeps a shrine to her or invokes the Spider Queen with devotion, and members speak of her with contempt, as the goddess they walked away from. Do not give any company member a shrine, a prayer or a kind word for her."
> — `campaign/setting/deities/lolth.md:75`

> "> - **Bregan D'aerthe and Lolth:** Bregan D'aerthe has rejected Lolth as its goddess. No member worships her, keeps a shrine to her or invokes the Spider Queen with devotion, and members speak of her with contempt. Do not give any company member a shrine, a prayer or a kind word for her. Lolth's page quotes the campaign lines."
> — `campaign/setting/deities/00-the-deities.md:394`

> "> - **Bregan D'aerthe:** Lolth."
> — `campaign/setting/deities/00-the-deities.md:401` (a list item; its list heading is not in the grep output)

> "- **Bregan D'aerthe First Meeting:** Asked "Do you serve Lolth?", Nevercott answers "Gods, no. My colleagues left the Spider Queen behind on purpose" (`campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:375-379`)."
> — `campaign/setting/deities/lolth.md:77`

> "> - **Jarlaxle's history with her:** The History page says he was born to Yvonnel Baenre, survived his sacrifice to Lolth when the blade could not pierce him, was favored by her afterward as an agent of chaos, and rejected her. The sacrifice and the favor are marked wiki-only there (`campaign/setting/history/03-bregan-daerthes-long-road.md:34-35`). Nothing in play tells a player this before **Jarlaxle Unmasked**."
> — `campaign/setting/deities/lolth.md:95`

> "- **The Compromised Eye:** The published Jarlaxle mission says "for Lolth's sake, be discreet" (`sources/adventure-wdh.json:3633`). The campaign cuts the line because Bregan D'aerthe has rejected her (`campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/design-notes.md:13`)."
> — `campaign/setting/deities/lolth.md:93`

> "- **Soluun Xibrindas:** He "despises Lolth and the matron houses that serve her, as the whole band does", and gives Jarlaxle the devotion a drow of the houses would give the Spider Queen (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:22`)."
> — `campaign/setting/deities/lolth.md:78`

> "**No other file uses her.** No Xanathar's Guild, Zhentarim, Cassalanter, Sea Maidens Faire or Kolat Towers file mentions Lolth beyond the Soluun scenes above."
> — `campaign/setting/deities/lolth.md:80`

> "**No tie found:** Zelifarn is a lawful good bronze dragon with no affiliation to Bregan D'aerthe (`05-zelifarn.md:6`), and neither his page nor the Umberlee mission mentions Lolth. Nar'l Xibrindas, the drow advisor in Xanathar's Guild, has no Lolth line either. The only Xanathar's Guild link is the published Shunn Shurreth."
> — `campaign/setting/deities/lolth.md:147`

> "The published adventure puts a shrine of Lolth in Soluun's stateroom aboard the *Scarlet Marpenoth*, area U3, with Soluun "worshiping before" it (`sources/adventure-wdh.json:26345`, `:26350`). The campaign's U3 entry has Soluun cleaning his weapons and no shrine (`campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:40`), so the shrine is dropped."
> — `campaign/setting/deities/lolth.md:70`

History page:

> "**Purpose:** Lets the GM answer any question about who founded Bregan D'aerthe, why its members reject Lolth, how it came to dominate Luskan, and what Jarlaxle had in place before the campaign opens."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:13`

> "- Jarlaxle was born to Matron Mother Yvonnel Baenre of House Baenre, the first house of Menzoberranzan. He survived his sacrifice to Lolth and later rejected her. Bregan D'aerthe rejects her too, and its members speak of her with contempt."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:24` (the bullet begins "> - " on the page; the text here is exact after the marker)

> "- Lolth favored him afterward as an agent of chaos, and he rejected her. She withdrew her favor, and the matron mothers of Menzoberranzan never learned of it. `[research: wiki only]`"
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:35`

> "- This is where the campaign rule starts. Jarlaxle rejected Lolth, Bregan D'aerthe rejects her, and its members speak of her as the goddess they walked away from. Soluun gives Jarlaxle the devotion that a drow of the houses would give the Spider Queen."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:36`

Soluun page:

> "Emotions. Soluun most often feels cold hatred of surface elves, fanatical devotion to Bregan D'Aerthe, contemptuous superiority, a zealot's fervor for the band (which, like every member of Bregan D'Aerthe, rejects Lolth), hunting focus, and bitter disdain for his brother Nar'l."
> — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:14`

Event files:

> "> If a character has Soluun in hand and asks him about the god of his people, he answers with open contempt for Lolth, since Bregan D'aerthe rejects her."
> — `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md:343`

> "***The disownment.*** The restored draft treated Soluun's disownment as real."
> — `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/design-notes.md:13` (the same paragraph's next sentence is quoted below)

> "He also never speaks of Lolth with devotion, because Bregan D'aerthe rejects her: when asked about his goddess he answers with contempt."
> — `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/design-notes.md:13`

> "> Bregan D'aerthe rejects Lolth. The spider on the coin is the goddess the company walked away from, caught in her own web with a blade through her, and every speaker mentions her with contempt. The company knows the truth about the Cassalanters, because Jarlaxle's doppelganger agent Vessa reads their thoughts. No speaker tells a member who hasn't worked it out."
> — `campaign/quests/faction-events/bregan-daerthe/r50-houseless-noble/ev-01-houseless-noble.md:27`

> "Fel'rekt speaks in encouraging sentences and counts his options off on his fingers."
> — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:136` (the same paragraph's last sentence is quoted below)

> "He never threatens anyone and never mentions Lolth."
> — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:136`

> "He never apologizes, never says Lolth's name with anything but disgust, and mentions his brother only as "the weak one"."
> — `campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:242`

> "- Appendix C has Jarlaxle say "for Lolth's sake." The line is cut, because Bregan D'aerthe has rejected her."
> — `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/design-notes.md:13`

Other deity pages (Bregan D'aerthe with Lolth; not Jarlaxle-specific):

> "- Bregan D'aerthe rejects Lolth, and no member worships her or invokes the Spider Queen with devotion (`campaign/setting/history/03-bregan-daerthes-long-road.md:36`)."
> — `campaign/setting/deities/corellon-larethian.md:73` (the same bullet continues with a Soluun sentence)

> "Spoiler limit:** everything above the `## Overview` may be read by the GM only. The Overview is the common-knowledge tier. Nothing about her is secret. Bregan D'aerthe rejects her mother Lolth, and that rejection does not make any member a follower of Eilistraee."
> — `campaign/setting/deities/eilistraee.md:11`

> "Bregan D'aerthe has rejected Lolth, and that does not make any member a follower of Ghaunadaur."
> — `campaign/setting/deities/ghaunadaur.md:11`

Campaign location (no oath line):

> "A magic mouth trap on the door to J30 triggers if anyone other than Zord opens it (DC 16 Intelligence (Arcana) to detect), releasing a sound like a gong audible throughout the aft castle."
> — `campaign/locations/sea-maidens-faire/04-eyecatcher-zords-office.md:5` (grep for Lolth in `campaign/locations/` returned no match)

### Adventure lines that mention Lolth in the Jarlaxle context (direct grep: four hits in the whole file)

> "\"We have a spy deep within {@creature Xanathar|WDH}'s organization, but I fear he has been compromised. It breaks my heart to do this, but I'm sending you to eliminate him. Make it quick and painless, and for Lolth's sake, be discreet.\""
> — `sources/adventure-wdh.json:3633` (the "5th" Bregan D'aerthe mission row at `:3632`)

> "The doors to this cabin are locked. If anyone other than Jarlaxle turns the handle of either door, a {@spell magic mouth} spell activates and shouts, \"By Lolth's teeth, have you no manners?\" The sound is loud enough to be heard by Jarlaxle (if he is in {@area J29|396}), and he comes to investigate."
> — `sources/adventure-wdh.json:25498` (J30, "Zardoz Zord's Cabin", `:25493`)

> "If he has not been encountered and disposed of elsewhere, a {@creature drow gunslinger|WDH} named {@creature Soluun Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) is here, worshiping before a shrine of Lolth. His stateroom has the following features:"
> — `sources/adventure-wdh.json:26345`

> "A black metal shrine of Lolth covered in tiny spider statuettes stands against one wall. At its top is a sculpture of the demon goddess, with the head and upper body of a female drow and the lower body of a spider."
> — `sources/adventure-wdh.json:26350`

Handoff on the cabin oath:

> "- [ ] **Jarlaxle's cabin oath:** `adventure-wdh.json:25498` (a magic mouth in his Eyecatcher cabin, J29, shouts \"By Lolth's teeth\"); the Eyecatcher cabin entry needs a different oath when written."
> — `session 49 handoff.md:126`

---

## (7) Lines on the page: DM, flag, Arc, links, wards

Grep of `campaign/setting/villains/jarlaxle.md`:

- **"flag"**: five occurrences, all in line 3 (`:3`): "the **BD Contact Severed** flag closes the faction for the campaign", "The **Ryvarra Identified** flag (from **The Neighbors** event in **Trollskull Alley**)", "the **Jarlaxle Informed** flag is set during **Fireball!**", "The flag records only that the party spoke directly with him.", and "The personality phases below key off the Jarlaxle Informed flag, not BD membership." The full line is quoted in section 3. The same outcomes are headings with "True / False" in the event files: `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:125` ("#### Jarlaxle Informed: True / False"); `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:57` ("#### Ryvarra Identified: True / False"). The BD Contact Severed outcome is marked at `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:195` ("Mark **BD Contact Severed** for each character who gives Dunmere their name.").
- **"DM"**: no occurrence.
- **"Arc" (capitalised)**: no occurrence. The lower-case path appears once (line 66).
- **Links by path** (lines 66-69): `../../structure/arc-h-sea-maidens-faire.md` (`:66`, "- [Sea Maidens Faire](../../structure/arc-h-sea-maidens-faire.md) — heist quest featuring Jarlaxle directly"); `../notable-figures/` (`:67`); `../../guides/gm-guide/running-the-villains.md`, `../../guides/factions/08-bregan-daerthe.md`, `../organizations/07-bregan-daerthe.md` (`:68`); `../../guides/gm-guide/player-factions-overview.md` (`:69`). `arc-h` is a structure document; the Sea Maidens Faire quest journal does not yet exist (CLAUDE.md quest table).
- **Ward names**: one, at `:58`: "Jarlaxle wants Bregan D'aerthe with a permanent Dock Ward presence".
- **See-also line** (`:3`): "See: **GM Guide: Session Zero**; **GM Guide: Player Factions Overview**; **Bregan D'aerthe** organization page." Not checked for content (outside scope).

---

## (8) Open conflicts (paired quotes; ranking noted)

Ranking as set in the task: campaign files outrank the adventure for campaign decisions; the adventure outranks the wiki. I quote both sides and do not choose.

**C1. When the identity is revealed (Zord rule vs. Fireball! and BD play)**
- `campaign/setting/villains/jarlaxle.md:3`: "His identity stays hidden behind J.B. Nevercott and Zardoz Zord until **Sea Maidens Faire**."
- `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:108`: "The party can learn that Captain Zord is Jarlaxle Baenre in two ways during this event:"; `:111`: "**The cabin.** A Bregan D'Aerthe member taken to his private cabin (below) sees the persona drop. He names himself."; `:134`: "#### Jarlaxle Unmasked (per character)"
- `campaign/guides/gm-guide/player-factions-overview.md:182`: "Jarlaxle's true identity surfaces in **Fireball!** and **Sea Maidens Faire**, when the nimblewright thread leads the party to the carnival and its captain."
- `campaign/setting/history/03-bregan-daerthes-long-road.md:86`: "Nothing in the Overview links him to the company, and the party learns the link in **Sea Maidens Faire**."
- `campaign/setting/deities/lolth.md:95`: "Nothing in play tells a player this before **Jarlaxle Unmasked**."
- Adventure: "All are loyal members of Bregan D'aerthe, and all know that Zardoz Zord is {@creature Jarlaxle Baenre|WDH} in disguise." (`sources/adventure-wdh.json:23047`). The campaign's BD speakers say "the captain" until the outcome (`ev-01-first-meeting.md:22`). The adventure's Nevercott "never admits" (`:3602`), which matches the campaign.
- Not decided here.

**C2. Whether the BD Contact Severed closure is permanent or party-wide**
- `campaign/setting/villains/jarlaxle.md:3`: "if the party reported the watchers to the Watch, the **BD Contact Severed** flag closes the faction for the campaign."
- `campaign/guides/gm-guide/player-factions-overview.md:180`: "This flag closes BD membership for the entire campaign." and "The decision is permanent."
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:195`: "Mark **BD Contact Severed** for each character who gives Dunmere their name. A character who stands beside the reporter and gives no name is not marked, and neither is any companion."
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/design-notes.md:5`: "The restored draft marked **Bregan D'aerthe Joined** and **BD Contact Severed** as party-wide flags" and "both outcomes are marked with the character's name."
- Adventure: "If the party reports the drow to the City Watch, Jarlaxle ends the surveillance and breaks off all contact with the characters for the time being." (`sources/adventure-wdh.json:3600`)
- Alexandrian Appendix B: "If the party reports the drow to the City Watch, Jarlaxle ends contact for now." (`sources/Appendix_B_-_Player_Factions.md:719`)

**C3. Eye #3 and the Stone at the start (Alexandrian vs. campaign)**
- Alexandrian (transcribed, printed p. 17): "As *Dragon Heist* begins, Jarlaxle is unaware of the *Stone of Golorr* or the Grand Game which is being played."
- Alexandrian Appendix B: "Jarlaxle's goal is control of the Stone — either the artifact itself or its three Eyes." (`sources/Appendix_B_-_Player_Factions.md:780`)
- Campaign: "Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep." (`campaign/guides/gm-guide/running-the-villains.md:25`)
- Campaign ruling: "Overruled: the Alexandrian line that he is unaware of the Stone and the Grand Game at the start (`1. The Villains.pdf` p.17)." (`campaign/setting/history/03-bregan-daerthes-long-road.md:160`)
- Higher-ranked: the campaign (the Session 47 ruling in history:160).

**C4. Eye #3 route**
- `campaign/guides/gm-guide/running-the-villains.md:25` and `:30`: the Eye passed from Renaer's locket to the Zhentarim, then to Xanathar's Guild in the warehouse raid, and BD agents lifted it that night.
- `campaign/structure/arc-h-sea-maidens-faire.md:15`: "The Eye had reached him the night before Ches 1, through Bregan D'aerthe intelligence work — the same network that had placed Nar'l Xibrindas inside Xanathar's Guild a year earlier, in 1491." (no locket, raid or lift sequence)
- `session 49 handoff.md:139`: "**Eye #3 route in `arc-h:9,15`:** only the \"night before Ches 1\" timing was added, not the locket/raid/lift sequence."
- Alexandrian (transcribed, printed p. 16): "Renaer didn't know it: His father had given him an elaborate, ivory mourning locket in honor of his mother. The Eye was hidden inside it."

**C5. Nimblewright count and maker**
- `sources/adventure-wdh.json:4746`: "During his last visit, he purchased four nimblewrights from a Lantanese wizard."
- `campaign/structure/arc-h-sea-maidens-faire.md:13`: "Nine nimblewrights sold to nine wealthy households at 25,000 gold pieces each — a steal, and deliberately so."
- Alexandrian (transcribed, printed p. 17): "Built by the technomancers of Luskan, he's brought several dozen of these constructs with him and is selling them at surprisingly compelling prices."
- `campaign/setting/history/03-bregan-daerthes-long-road.md:163` records the disagreement; no ruling is recorded.

**C6. "Real prize" vs. "latest" scheme for the Lords' Alliance**
- `campaign/setting/villains/jarlaxle.md:56`: "1. **Lords' Alliance Membership for Luskan** — the real prize"
- `sources/adventure-wdh.json:32179`: "the latest of which is a plan to legitimize Luskan by making it a member of the Lords' Alliance."
- `campaign/setting/history/03-bregan-daerthes-long-road.md:157`: "The page follows the published adventure for the history and the campaign for the aim." (full text in section 1)

**C7. Bargaining chip: Eye (campaign) vs. dragonstaff (adventure)**
- `campaign/setting/villains/jarlaxle.md:57`: "as a bargaining chip, not for personal use" (the Eye).
- `sources/adventure-wdh.json:549`: "Jarlaxle also wants the {@item dragonstaff of Ahghairon|WDH} for leverage in his negotiations."
- `sources/adventure-wdh.json:14786`: "He intends to see the gold safely returned to the city of Waterdeep but also demands the {@item dragonstaff of Ahghairon|WDH} for his trouble."
- The adventure has no Eye (section 9).

**C8. Permanent base vs. departure date**
- `campaign/setting/villains/jarlaxle.md:58`: "Waterdeep as Permanent Base — the Sea Maidens Faire is seasonal; Jarlaxle wants Bregan D'aerthe with a permanent Dock Ward presence"
- `campaign/guides/gm-guide/structural-rules.md:50`: "Tarsakh 20 | Sea Maidens Faire departs at dawn | Eye #3 leaves Waterdeep; alliance path with Jarlaxle closes"
- `campaign/setting/history/03-bregan-daerthes-long-road.md:77`: "The Faire leaves Waterdeep at dawn on Tarsakh 20."
- `sources/adventure-wdh.json:32181`: "Jarlaxle plans on using the submarine to flee Waterdeep if his scheme unravels."

**C9. Nar'l: "most valuable asset" and a contingency vs. the adventure's suspicion and elimination order**
- `campaign/setting/villains/jarlaxle.md:47`: "Inside Xanathar's Guild; Jarlaxle's most valuable asset; Jarlaxle has a contingency if Nar'l is discovered (has not shared it with Nar'l)"
- Alexandrian Appendix B `:781`: "Jarlaxle's spy inside Xanathar's council is his most valuable single asset in Waterdeep."
- `sources/adventure-wdh.json:3634`: "Jarlaxle identifies the traitor as a drow mage named {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) and furnishes the characters with a route to {@creature Xanathar|WDH}'s lair through underground passageways."
- `sources/adventure-wdh.json:15150`: "These drow also have secret orders to kill {@creature Nar'l Xibrindas|wdh}, if he's still alive, and retrieve Jarlaxle's bag of holding (see {@area X35|2c7})."
- `sources/adventure-wdh.json:7153`: "Jarlaxle suspects that {@creature Nar'l Xibrindas|wdh}, his spy in the Xanathar Guild, has betrayed him and is now using the resources of Bregan D'aerthe to help the beholder retrieve the stone."
- Wiki `wiki.txt:554`: "[[Jarlaxle]] too believed that Nar'l was double-crossing Bregan D'aerthe and was willingly working with the beholder."
- Campaign NP `xanathars-guild/03-narl-xibrindas.md:14`: "bitter awareness that Jarlaxle would sacrifice him without hesitation if the cost were right."
- The adventure's Nar'l episode is specific to the Compromised Eye mission and a mid-adventure suspicion; the campaign's Nar'l page describes a standing state. Both are quoted; not decided here.

**C10. Fenerus: whether he knows his contacts are BD**
- `sources/adventure-wdh.json:6709`: "The characters visit the residence of Fenerus Stormcastle, a lamplighter and retired brigand who funnels information to Bregan D'aerthe."
- `sources/adventure-wdh.json:7124`: "He has no clue that his contacts are drow members of Bregan D'aerthe, since they wear cloaks and keep to the shadows."
- `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:7`: "Bregan D'aerthe (cut-out; believes his contacts are Luskan agents)"
- `campaign/setting/organizations/07-bregan-daerthe.md:40`: "Supposed to be a cut-out, but once followed Krebbyg after a pickup and knows the messages go to the Sea Maidens Faire."
- The two campaign files disagree with each other. The NP page is the per-NPC record; the org page is an organization page.

**C11. Zelifarn: stationed on the ship, or an independent dragon in a cave?**
- `campaign/setting/organizations/07-bregan-daerthe.md:39`: "- **Zelifarn** — Young sea dragon (bronze-scaled) stationed aboard the *Scarlet Marpenoth*. See the **Zelifarn** page in Notable Figures."
- `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:6`: "- **Affiliation:** None (friendly to Bregan D'aerthe; not an operative)"
- `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:25`: "Zelifarn is the young bronze dragon of Deepwater Harbor, on friendly terms with the *Eyecatcher*'s crew but answerable to none of them"
- `sources/adventure-wdh.json:26604`: "He has spent the past several months scouring wrecks at the bottom of the harbor for treasure and stashing precious baubles in a hidden underwater cave."

**C12. Who may read the company's Overview**
- `campaign/setting/organizations/07-bregan-daerthe.md:58`: "Bregan D'aerthe is a mercenary company of drow exiles and surface operatives, led by Jarlaxle Baenre, running the Sea Maidens Faire carnival as cover for a city-wide intelligence network."
- `campaign/setting/history/03-bregan-daerthes-long-road.md:11`: "The Overview is the public face and links neither Captain Zardoz Zord nor Luskan's rulers to the company's leader."
- `campaign/setting/history/03-bregan-daerthes-long-road.md:165`: "> - **Conflicts:** `organizations/07-bregan-daerthe.md` line 58 names Jarlaxle as the leader and describes a city-wide intelligence network in its Overview. That does not follow the Zardoz Zord rule and is not player-safe."

**C13. Vessa's name and the adventure's alias**
- `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:26`: "Vessa (full name Lymeria Lhaurilstar) is a Bregan D'aerthe doppelganger operative embedded in the Cassalanter social scene under a permanent human cover"
- `sources/adventure-wdh.json:20414`: "poses as a minor noblewoman going by the name Lymeria Lhaurilstar" (the speaker is "Bonnie", a Yawning Portal doppelganger). The adventure has no Vessa.

**C14. Lolth shrine in Soluun's stateroom**
- `sources/adventure-wdh.json:26345`: "is here, worshiping before a shrine of Lolth."
- `campaign/setting/deities/lolth.md:75`: "No member worships her, keeps a shrine to her or invokes the Spider Queen with devotion"
- `campaign/setting/deities/lolth.md:70`: "The campaign's U3 entry has Soluun cleaning his weapons and no shrine (`campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:40`), so the shrine is dropped."

**C15. Cabin oath**
- `sources/adventure-wdh.json:25498`: "\"By Lolth's teeth, have you no manners?\""
- `campaign/locations/sea-maidens-faire/04-eyecatcher-zords-office.md:5`: "releasing a sound like a gong audible throughout the aft castle."
- `session 49 handoff.md:126`: "the Eyecatcher cabin entry needs a different oath when written."

**C16. Season of the adventure vs. the campaign's calendar**
- `sources/adventure-wdh.json:551`: "If you choose Jarlaxle as the villain, the adventure takes place in the autumn."
- `campaign/setting/history/03-bregan-daerthes-long-road.md:81`: "This spring the Sea Maidens Faire, a traveling carnival out of Luskan, brings three ships and Captain Zardoz Zord to Deepwater Harbor for Fleetswake."
- `campaign/guides/gm-guide/structural-rules.md:44`: "| Ches 21–30 | Fleetswake | Maritime festival; Sea Maidens Faire fleet in harbor; cover for Sea Maidens Faire reconnaissance |"
- The adventure's autumn parade: "The Day of Wonders is the grandest parade of the fall season, and Jarlaxle wants the Sea Maidens Faire to be a part of it." (`sources/adventure-wdh.json:26688`)

**C17. Kimmuriel**
- Wiki `wiki.txt:308`: "| leader         = [[Jarlaxle]], [[Kimmuriel Oblodra]]"
- Wiki `wiki.txt:408`: "As time went on (by [[1463 DR]], Kimmuriel became widely understood as the band's leader,"
- Campaign `history:152`: "**Default kept:** Kimmuriel Oblodra stays omitted from the body" (full text in section 4)
- `session 49 handoff.md:135`: "\"third son\" for Jarlaxle; Kimmuriel omitted;" (listed as unruled)

**C18. Third son**
- `campaign/setting/history/03-bregan-daerthes-long-road.md:38`: "A campaign docx calls him the third son, and the page keeps that."
- `sources/research/pass4-bundles/jarlaxle/wiki.txt:96`: "Her second-oldest son, [[Doquaio Baenre]], was ordered to assist"
- `session 49 handoff.md:135`: "\"third son\" for Jarlaxle" (listed as unruled)

**C19. Scarlet Marpenoth location**
- `campaign/structure/arc-h-sea-maidens-faire.md:11`: "The Scarlet Marpenoth had lain moored in the harbor all year, and the night the fleet arrived it took its place beneath the Eyecatcher."
- `campaign/guides/factions/08-bregan-daerthe.md:9`: "Rather than competing with Xanathar or Manshoon for the Stone, Jarlaxle already holds Eye #3, aboard the *Scarlet Marpenoth* and mounted beneath the *Eyecatcher*'s keel, and is content to let the other factions exhaust themselves chasing each other."
- `campaign/setting/history/03-bregan-daerthes-long-road.md:74`: "In the campaign it has been moored in Deepwater Harbor since he reached the city, and the carnival fleet joins it for Fleetswake."
- `sources/adventure-wdh.json:32181`: "This underwater vessel is mounted below the {@i Eyecatcher} and kept out of sight."
- Not a direct conflict. The handoff notes the rooms 01-04 were not checked against "submarine moored all year" (`session 49 handoff.md:140`).

**C20. Trigger for the phase change vs. the adventure's "never admits"**
- `campaign/setting/villains/jarlaxle.md:15`: "*Trigger to Phase 2:* PCs penetrate the disguise, or Jarlaxle decides they've earned the reveal."
- `sources/adventure-wdh.json:3602`: "Even if the characters discern his true identity, he never admits to being anything other than what he pretends to be."
- `sources/adventure-wdh.json:4751`: "If the characters somehow discern his true form, Jarlaxle gives the party a slow nod of his head, dryly says \"Bravo!\" and lets them make the next move."

---

## (9) Not found

- **Vessa** (`sources/adventure-wdh.json`, whole file): no match. Campaign: found in 26 files, including the NP, the org page, history 05, `arc-g`, and the BD event files.
- **Kimmuriel / Kimmuriel Oblodra** (adventure, whole file): no match. Campaign: only `history/03` (lines 151-152), the handoffs and the consistency notes.
- **Renaer + Jarlaxle** (adventure): no linking line. Campaign: only the locket line (`running-the-villains.md:25`) and Alexandrian p. 16.
- **Yvonnel, Doquaio, birth order** (adventure): no match.
- **"Eye of the Stone" / "Eyes" for Jarlaxle** (adventure, whole file): no match for "Eyes of the Stone" or "Eye of the Stone". Other "Eye" strings are unrelated ("Eyestalker", "Agent of the Eye", "Hand of the Eye", "Eye Ray", "Staircase of Eyes", "Ol' Fire Eyes", "Blinking Eyes", "Tiger's Eye").
- **Manshoon–Jarlaxle relationship** (adventure): none; only `:14786` puts them in one scene.
- **Xanathar–Jarlaxle relationship** (adventure): none direct; the link is Nar'l (`:1301`, `:15149`, `:32323`).
- **"Eye for Lords' Alliance" offer** (adventure): none. The adventure's offer is gold and the dragonstaff (`:22949`).
- **Permanent base / Dock Ward presence** (adventure): none. The Dock Ward material is the Seven Masks Theater (`:9066`) and Dock Ward operations.
- **Nar'l "contingency"** (adventure, Alexandrian appendices, wiki): none.
- **Vessa's name "Lymeria Lhaurilstar"** (adventure): the name belongs to "Bonnie" (`:20414`).
- **Zardoz Zord as a separate campaign page**: none. The file is `01-jarlaxle-baenre.md`.
- **Players' Guide mention of Jarlaxle or Zord** (`campaign/guides/players-guide/`): none; the faction is named at `faction-affiliations.md:15`.
- **Overview section on `jarlaxle.md`**: none.
- **Magic mouth oath in the location journals**: none; the trap is present and the line is absent (`04-eyecatcher-zords-office.md:5`).
- **Wiki lines 626-1,875** (grep only): Lords' Alliance hits at `wiki.txt:1059` (`allegiances = [[Lords' Alliance]]`) and `:1687` (`;Organizations: [[Force Grey]] &bull; [[Lords' Alliance]]`). Other grep matches in that range were omitted by the tool and were not read.
- **"Renaer doesn't know who he met"** (page row, `jarlaxle.md:50`): no source found beyond the Alexandrian locket line, which says Renaer "didn't know" the Eye was inside.

---

## (10) Not readable

- `Jarlaxle Baenre NPC Guide.docx`, listed in `sources/SOURCE_GUIDE.md:691`: "| `Jarlaxle Baenre NPC Guide.docx` | Jarlaxle's personality, tactics, goals, and the Bregan D'aerthe operation; how to play him | **Fireball!**, **Sea Maidens Faire**; the **Bregan D'aerthe** organization page (Bregan D'aerthe section) |". The history page cites it for the "third son" (`history:148`, "lines 51 and 62"). Needs extraction.
- `Zardoz Zord (and extra side quest hook).docx`, listed in `sources/SOURCE_GUIDE.md:699`: "| `Zardoz Zord (and extra side quest hook).docx` | Jarlaxle's \"Zardoz Zord\" persona — the Sea Maidens Faire disguise and an additional side quest hook | **Fireball!** (Sea Maidens Faire first contact), **Sea Maidens Faire** |". Needs extraction.
- `sources/1. The Villains.pdf`: readable only as images (7 pages). The quotes above are transcriptions. The Eye/Stone line is on printed p. 17; the Renaer locket line is on printed p. 16; the Jarlaxle bullet is on printed p. 14.
- `sources/Act_III_Arc_D.md`, Alexandrian Appendix D, and the other PDFs: not read in this pass.
