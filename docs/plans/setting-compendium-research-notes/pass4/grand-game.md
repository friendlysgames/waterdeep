# Pass 4 research notes: The Grand Game and What Each Faction Knows at Start

Research for `campaign/setting/the-grand-game/the-grand-game.md` (slug `grand-game`) and `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md` (slug `faction-knowledge`), built from `campaign/setting/grand-game.md`.

Conventions: every quote is copied from a tool result. Each `>` block is followed by its `file:line` reference. Line numbers are 1-indexed. `sources/1. The Villains.pdf` and `sources/21. Faction Reports of the Grand Game.pdf` have no text layer. Their text was read from rendered page images and transcribed, so the handwritten passages in `21.` are transcriptions and should be checked against the page image before they reach a page. PDF page references use printed page numbers (`p.142` is PDF page 1 of `21.`). `sources/2. Other Factions.pdf` has a text layer.

Searches for "Grand Game" in `sources/adventure-wdh.json` and `sources/adventure-wdmm.json` returned no matches. The published adventure never uses the term.

---

## grand-game

### What the Grand Game Is (`grand-game.md` lines 13-15)

**Claim:** the term is used in the city's underground for the competition between power blocs.

> "- The term used in the city's criminal and political underground for the ongoing competition between power blocs for influence, territory, and profit"
— `campaign/setting/grand-game.md:14`

**Claim:** no governing body; "called the Grand Game because everyone who plays it understands they are playing it."

> "- Not formally organized; no governing body; called the Grand Game because everyone who plays it understands they are playing it"
— `campaign/setting/grand-game.md:15`

**Alexandrian support for the frame:**

> "Periodically throughout Waterdeep's history the byzantine factions of the city — or some significant subset thereof — will become collectively fixated upon some objective. Thus will begin a Grand Game."
— `sources/1. The Villains.pdf:p.13`

> "The concept of the “Grand Game” was created to give a convenient label to the proceedings. As the PCs are exposed to this label, it will help them conceptualize what they have become a part of."
— `sources/1. The Villains.pdf:p.14` (design note)

> "Moving beyond the major villains, the Grand Game also features the participation of any number of other factions (including the PCs)."
— `sources/2. Other Factions.pdf:p.20`

**Gap:** no source gives "no governing body", or the line that everyone who plays "understands they are playing it". The `p.14` note supports the label, not the lack of governance.

---

### How Information Moves: front businesses (`grand-game.md` lines 17-18)

**Claim as written:**

> "- **Front businesses**: Sea Maidens Faire (Bregan D'aerthe), Istrid Horn's moneylending (Doom Raiders), a Trades Ward importing company (Manshoon), a charitable hospital (Cassalanters)"
— `campaign/setting/grand-game.md:18`

**(a) Sea Maidens Faire (Bregan D'aerthe): supported as a front.**

> "Bregan D'aerthe is using one of Jarlaxle's legitimate business enterprises-the Sea Maidens Faire-as a front in Waterdeep. The Sea Maidens Faire consists of three carnival ships (the {@i Eyecatcher}, the {@i Heartbreaker}, and the {@i Hellraiser}) crewed by disguised drow and a host of non-drow performers (musicians, acrobats, actors, and the like). The ships' cargo consists mostly of wagons and floats that can be hastily assembled and paraded through the city. The drow use these parades to draw attention away from their illicit activities."
— `sources/adventure-wdh.json:1299`

> "Freshly arrived in his cover identity as Captain Zord of the Sea Maiden's Faire, Jarlaxle is coordinating and ramping up his local intelligence operations."
— `sources/1. The Villains.pdf:p.17`

**(b) Istrid Horn's moneylending (Doom Raiders): lending is supported; "front" is not.**

> "{@creature Istrid Horn|wdh|Istrid} is regarded as the Black Network's Master of Trade and Coin in Waterdeep. The shield dwarf operates an illegal lending operation out of a heavily guarded warehouse in the Dock Ward, offering loans to those in need of coin. Her interest rates are comparable to those of her competitors (including noble families of bankers such as the Cassalanters and the Irlingstars), but the penalties for not paying back Istrid's loans are severe."
— `sources/adventure-wdh.json:31934`

> "Istrid offers loans of up to 2,500 gp with an interest rate of 10 percent per tenday."
— `sources/adventure-wdh.json:1455`

Campaign wording that calls it a front (no source of its own):

> "- Their fronts are ordinary businesses. Davil holds court in a curtained room at the Yawning Portal, Istrid lends money from a Dock Ward warehouse, and Skeemo runs Weirdbottle's Concoctions in the Trades Ward."
— `campaign/setting/history/04-the-founding-of-chains.md:59`

**(c) Trades Ward importing company (Manshoon): no source found.**

Searched `importing`, `importer`, `import company`, `trading house`, and `import` in `sources/adventure-wdh.json`, in `campaign/`, and in the Alexandrian markdown. The only hits are `grand-game.md:18` and `campaign/structure/ch2-city-of-splendors.md:153` (the same sentence). The closest published line is about the Zhentarim in general:

> "The Zhentarim is a shadow organization that trades mercenaries and goods (including weapons) for profit. It has long sought to gain political influence in Waterdeep, but the strength of the city's Masked Lords, nobility, and professional guilds makes that difficult."
— `sources/adventure-wdh.json:1444`

The only Trades Ward business the published adventure attaches to the Black Network is a Doom Raider shop, not a Manshoon front:

> "Adventurers can procure discounted potions and poisons from Skeemo's shop, Weirdbottle's Concoctions, which is located in the Trades Ward."
— `sources/adventure-wdh.json:1453`

**(d) Charitable hospital (Cassalanters): no source for "hospital".**

Searched `hospital`, `infirmary`, `clinic`, `charit`, `charity`, and `front` in `sources/adventure-wdh.json` and `campaign/`. The published adventure gives Victoro charitable work, not a hospital:

> "Victoro is a priest of Asmodeus, though his devotion to the Lord of the Nine Hells is a secret known only to his wife and his closest friends. Most Waterdhavians know him as a successful banker, philanthropist, and worshiper of Lathander. Some of his business profits go toward feeding and sheltering the poor. But behind this veneer of generosity, Victoro is a self-serving beast."
— `sources/adventure-wdh.json:32692`

The hospital sentence appears only in campaign files, unsourced there:

> "- **Social cover:** Sea Ward dinner parties are intelligence operations, and the Cassalanters' charitable galas are recruitment screens. A charitable hospital serves as the family's front business."
— `campaign/setting/organizations/10-cassalanters.md:65`

The Cassalanter organization page's draft notes name `grand-game.md` as the source of this material:

> "- `campaign/setting/grand-game.md`: front businesses, galas as recruitment screens, starting knowledge"
— `campaign/setting/organizations/10-cassalanters.md:95`

---

### How Information Moves: informants (`grand-game.md` line 19)

**Claim as written:**

> "- **Informants**: the Watch has informants in every ward; every faction has informants in the Watch; Jarlaxle has informants in every other faction; Skeemo Weirdbottle compiles all of it"
— `campaign/setting/grand-game.md:19`

**"Watch informants in every ward" and "every faction has informants in the Watch": no published source.** The campaign's City Watch page states the claim without a source:

> "The Watch has informants in every ward, and every faction has informants in the Watch."
— `campaign/setting/governance-and-guilds/city-watch.md:81`

The Alexandrian remix Appendix D names one civilian informant for the Watch:

> "Gosta moonlights as an informal Watch informant — not a spy exactly, more a civic-minded citizen who has been filing regular reports on \"establishments of interest\" for the better part of a decade."
— `sources/Appendix_D_-_Running_the_Tavern.md:159`

**"Jarlaxle has informants in every other faction": partly supported (one spy in Xanathar's Guild).**

> "Jarlaxle has a spy in the Xanathar Guild: the advisor {@creature Nar'l Xibrindas|wdh}, who uses {@spell sending} spells to transmit intelligence to his drow brethren. Bregan D'aerthe knows that the safest route to the beholder's lair is a secret staircase in the sewers of the Castle Ward. Any character who belongs to this faction can get this information from Jarlaxle or another source."
— `sources/adventure-wdh.json:15149`

> "Bregan D'aerthe is skilled at infiltrating criminal organizations. {@creature Xanathar|WDH}'s drow advisor, {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}), is actually a Bregan D'aerthe spy. Bregan D'aerthe support comes in these ways:"
— `sources/adventure-wdh.json:1301`

Campaign-only, for the Cassalanter spy (Vessa). This is a superseded structure document, not published text:

> "**\"Vessa\" (Lymeria Lhaurilstar).** During social events, a doppelganger posing as the noblewoman \"Vessa\" circulates in C15 (the banquet hall). She is a Bregan D'aerthe operative planted to monitor the Cassalanters."
— `campaign/structure/arc-g-cassalanter-villa.md:133`

**"Skeemo Weirdbottle compiles all of it": no source.** The published adventure gives Skeemo a title and a shop, not an intelligence role:

> "{@creature Skeemo Weirdbottle|wdh|Skeemo} became the Master of Magic for the Black Network in Waterdeep, setting up a cover in the Trades Ward in the form of a cramped little shop called Weirdbottle's Concoctions. Most of his potions and elixirs are nonmagical, but he crafts magical ones for his Zhent friends."
— `sources/adventure-wdh.json:31944`

> "The group's leaders are {@creature Davil Starsong|WDH} (Master of Opportunities and Negotiations), {@creature Istrid Horn|WDH} (Master of Trade and Coin), {@creature Skeemo Weirdbottle|WDH} (Master of Magic), {@creature Tashlyn Yafeera|WDH} (Master of Arms and Mercenaries), and {@creature Ziraj the Hunter|WDH} (Master of Assassination)."
— `sources/adventure-wdh.json:1447`

---

### How Information Moves: social events (`grand-game.md` line 20)

**Claim as written:**

> "- **Social events**: Sea Ward dinner parties are intelligence operations with better wine; the Cassalanters' charitable galas are recruitment screens"
— `campaign/setting/grand-game.md:20`

**No published source** for dinner parties as intelligence operations, or for galas as recruitment screens. The published Cassalanter feast is a poisoning:

> "A provision in the contract allows the Cassalanters to buy their way out of it, but doing so requires a tremendous amount of coin and a mass sacrifice of unfortunate people. While Victoro hunts for Dagult Neverember's lost cache of gold, Ammalia makes plans to host a {@condition poisoned} feast in celebration of Founders' Day."
— `sources/adventure-wdh.json:31716`

The campaign's own statement of the same claim is `campaign/setting/organizations/10-cassalanters.md:65` (quoted above). The public galas are in the organization page's Overview:

> "The family lives in a villa in the Sea Ward, is publicly known for its ancestral devotion to Siamorphe, and hosts public galas during Waukeentide, and the younger twins, Terenzio and Elzerina, are often seen at play in the gardens."
— `campaign/setting/organizations/10-cassalanters.md:58`

---

### How Information Moves: the Yawning Portal (`grand-game.md` line 21)

**Claim as written:**

> "- **The Yawning Portal**: Durnan has heard everything; he shares selectively; every faction knows this and cultivates him anyway"
— `campaign/setting/grand-game.md:21`

**"Heard everything", "shares selectively", and "every faction cultivates him": no source found.** Searched `Durnan` in `sources/adventure-wdh.json` (about 20 hits), in the Alexandrian markdown, and in `campaign/`. The published Durnan does not gather intelligence:

> "{@creature Durnan|WDH} doesn't often venture far from the Yawning Portal, using his employees to run errands for him as needed. If he's feeling charitable, he might gently discourage likable \"nobodies\" from venturing into Undermountain, if he thinks they wouldn't survive. He can also direct adventurers toward tavern regulars who might be able to help them or offer useful information."
— `sources/adventure-wdh.json:32071`

> "If {@creature Durnan|WDH} has any living family members, he doesn't speak of them. He rarely says two words when one will do. He has a dark sense of humor and spares no pity on those who take the risk of entering Undermountain."
— `sources/adventure-wdh.json:32069`

> "The proprietor of the Yawning Portal is a retired adventurer and a man of few words. {@creature Durnan|WDH} (see {@adventure appendix B|WDH|12}) bluntly warns adventurers of lower than 5th level that entering Undermountain \"isn't a good idea.\" He keeps a magic greatsword hidden behind the bar just in case something monstrous crawls up out of the entry well."
— `sources/adventure-wdh.json:1506`

The Alexandrian remix Appendix D gives Durnan a network. This is a remix claim, not a published one:

> "Durnan's network gives her street-level information she occasionally shares with employers she respects — not intelligence, just Waterdeep gossip with good signal-to-noise ratio."
— `sources/Appendix_D_-_Running_the_Tavern.md:125`

Campaign-only Masked Lord status (ruling 6 tags this as campaign-only):

> "**Durnan** (Neutral, Human, he/him) is the proprietor of the Yawning Portal, and in the campaign he is also a secret Masked Lord and the secret founder of the Red Sashes (campaign-only). Its fighters pose as regulars at the Portal and are magically sworn to his service. The published adventure names him only as the Portal's proprietor."
— `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:45`

---

### The City Watch as a Character (`grand-game.md` lines 23-26)

**Claim: "Genuinely trying, most of the time; aware that some cases are politically untouchable."**

> "- Genuinely trying, most of the time; aware that some cases are politically untouchable"
— `campaign/setting/grand-game.md:24`

No published source for "politically untouchable" or "trying, most of the time". The published adventure gives trust in the Watch as a rule of the city:

> "Waterdeep is no village led by hidebound hierarchs or petty fiefdom ruled by the whim of a warlord. It is a city of laws molded by Tyr's spirit of justice. As a rule, you can trust members of the City Watch to do their duty diligently, and you can expect that the city's magisters will be fair. If you have cause to come before the Masked Lords or the Open Lord herself, rest assured that if your cause be just, justice will be done. If, however, you find yourself in the wrong, know that though it might take time to weigh that wrong on Tyr's scales, his hammer will fall—and it will be wielded by Waterdeep with a vengeance."
— `sources/adventure-wdh.json:30514` (JSON escape `—` kept as it appears in the file)

> "City Watch members follow a strict code of conduct that makes them one of the most trusted police forces aside from paladin-patrolled Elturgard. As long as you don't engage in unlawful behavior, you can expect to be left untroubled by the Watch."
— `sources/adventure-wdh.json:30549`

The Alexandrian PDF names the Watch as the route for information to reach the Open Lord. It says nothing about Watch conduct:

> "The most likely avenue for that to change — and potentially change rapidly — is through information blabbed to the City Watch."
— `sources/2. Other Factions.pdf:p.21`

**Claim: "Most officers: not corrupt by rule, susceptible to pressure from above."**

> "- Most officers: not corrupt by rule, susceptible to pressure from above"
— `campaign/setting/grand-game.md:25`

No source says "pressure from above". The only published corruption is one Masked Lord's eight Watch veterans:

> "If the characters become an annoyance, he has eight crooked members of the City Watch (human {@creature veteran||veterans}) crack down on them, then uses his position as Masked Lord to clear any charges leveled against these Watch members. Corylus refuses to be indebted to anyone, so any attempt by the characters to curry favor with him is met with suspicion, if not outright hostility."
— `sources/adventure-wdh.json:30365`

**Claim: "Barnibus Blastwind: the exception — thorough, meticulous, personally compromised, and more useful than any other Watch contact."**

> "- Barnibus Blastwind: the exception — thorough, meticulous, personally compromised, and more useful than any other Watch contact"
— `campaign/setting/grand-game.md:26`

- "Personally compromised": no published source. The campaign's City Watch draft notes say so:
> "`grand-game.md` line 26, \"personally compromised\", has no source. `campaign/guides/gm-guide/debts-of-the-city.md` line 147 gives a situational compromise (\"one incident, one person he refuses to discuss\"), which is a campaign decision on that page, and this page leaves it out."
— `campaign/setting/governance-and-guilds/city-watch.md:129`

- Campaign-only situational compromise, on the Debts page (a campaign decision, not a source):
> "His professional compromise is situational: one incident, one person he refuses to discuss. Outside that incident, his record is clean."
— `campaign/guides/gm-guide/debts-of-the-city.md:147`

- Published role. He works for the Watchful Order, not the Watch:
> "{@creature Barnibus Blastwind|wdh|Barnibus} works for the Watchful Order of Magists and  Protectors, investigating crimes that involve the use of  magic. He comes across as prickly and secretive, confiding only in {@creature Saeth Cromley|wdh}, a retired {@creature sergeant|WDH} of the City  Watch who assists in many of his investigations."
— `sources/adventure-wdh.json:31774`

- Published character. It gives "finds violence appalling", not "meticulous":
> "Barnibus uses spells that help him investigate crimes, pry secrets from the minds of suspects, and locate missing persons. He finds violence appalling and would never use his magic to inflict harm on others-even those who harm him."
— `sources/adventure-wdh.json:31776`

- Alexandrian remix conflicts with the campaign on his race and role:
> "Barnibus — a soft-spoken, meticulous dwarf mage in an ink-stained coat — quietly takes charge of the forensic work while Cromley directs twenty constables to knock on every door in the alley."
— `sources/Act_III_Arc_D.md:137`

- Campaign Notable Figures page, summary line (Illuskan human, Watchful Order investigator):
> "- *Illuskan human Watchful Order investigator, lawful good*. Stat block: **Mage**."
— `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:6`

- Campaign Notable Figures page, persona (no "compromised" wording):
> "**Persona.** To the world, Barnibus is a prickly and secretive investigator who confides only in Saeth Cromley."
— `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:22`

- City Watch page, Key Members entry:
> "**Barnibus Blastwind** (Lawful Good, Illuskan Human, he/him) is a Watchful Order investigator of crimes that involve magic. He is prickly and secretive, confides only in Cromley and finds violence appalling. He is a lifelong bachelor who inherited a small tidy estate in the Sea Ward from his grandmother and spends his free days in its library. The published adventure gives him no magistrate's office."
— `campaign/setting/governance-and-guilds/city-watch.md:62`

---

### What the published adventure says about the Grand Game

- The term "Grand Game" does not appear in `sources/adventure-wdh.json` or `sources/adventure-wdmm.json`.
- Xanathar's goal:

> "{@creature Xanathar|WDH} is a paranoid, megalomaniacal beholder crime lord whose goal is to wipe out anyone it perceives as a Zhentarim operative or sympathizer, retrieve the {@item Stone of Golorr|WDH}, and secure the cache of dragons. Its base is a dungeon under Skullport, a subterranean settlement beneath Waterdeep. This lair is described in chapter 5."
— `sources/adventure-wdh.json:527`

- Cassalanters:

> "Victoro and {@creature Ammalia Cassalanter|WDH} are Waterdavian nobles and secret devil worshipers. The Cassalanters plan to use the cache of dragons to buy back the souls of their children, which they traded to Asmodeus for power. Their estate, Cassalanter Villa, has a temple of Asmodeus hidden underneath it, as described in chapter 6."
— `sources/adventure-wdh.json:538`

- Jarlaxle:

> "{@creature Jarlaxle Baenre|WDH} is a drow swashbuckler and the secret lord of Luskan, the City of Sails. Jarlaxle plans to use the cache of dragons to buy his way into the Lords' Alliance, a confederation of cities and towns that band together against common threats."
— `sources/adventure-wdh.json:549`

- The Sea Maidens Faire as published:

> "The Sea Maidens Faire, owned and operated by Zord, is a seafaring carnival based in Luskan that travels along the Sword Coast. It provides good, wholesome entertainment in the form of fantastic street parades."
— `sources/adventure-wdh.json:4744`

- Manshoon and Kolat Towers (the published text gives the Trades Ward here and the Southern Ward in the Manshoon appendix):

> "A clone of the wizard {@creature Manshoon|WDH}, one of the founders of the Zhentarim, is hiding in Waterdeep. He wants to rule the city, by claiming the cache of dragons and by using that wealth to bribe the Masked Lords into making him the new Open Lord. He also wants to regain control of the Black Network. {@creature Manshoon|WDH} lurks in Kolat Towers, a pair of wizards' towers in the Trades Ward. This residence is described in chapter 8."
— `sources/adventure-wdh.json:560`

> "{@creature Manshoon|WDH} took control of Kolat Towers, a crumbling residence in the Southern Ward that was abandoned years ago by the two wizards who built it."
— `sources/adventure-wdh.json:32218`

---

### Soul-coin and "ninety-nine souls" lines

**`campaign/setting/grand-game.md`** (the only soul line in the file)

> "| Cassalanters | Vault exists (Lords' Alliance contact); have one Eye | Eye #2 | Raising the 999,999 gp and ninety-nine souls the contract demands (about 500,000 gp in hand, the Vault's 500,000 covers the rest); need the Stone plus Eyes #1 and #3 to open the Vault |"
— `campaign/setting/grand-game.md:34`

**`campaign/guides/gm-guide/grand-game-in-play.md`** (no "soul coin" and no "ninety-nine" wording; two "soul" lines)

> "**The Cassalanters** are largely binary. In passive mode they barely react; their outpost network is focused on gathering gold and ritual components, not the PCs. The switch to hostile mode happens when the PCs are identified as a threat to the soul-pact plan, and they move directly to Willifort Crowelle's full operation. They prefer Alert to Lockdown because the less visible their pursuit, the better their political position. When they do escalate to Lockdown, they exhaust city leverage first: Watch complaints, noble pressure, guild sanctions. Infernal force is the last resort."
— `campaign/guides/gm-guide/grand-game-in-play.md:53`

> "**The Cassalanters** retreat to social and legal pressure before infernal force. Their first response to a party that has become a problem is Watch complaints, noble pressure, guild sanctions, and quiet damage to the PCs' reputation in the city. What they want for standing down is discretion: a party that will stay out of their affairs and never speak of the soul pact. Ammalia Cassalanter is more comfortable wielding Waterdeep's social machinery than facing direct confrontation. What they remember is anyone who has learned too much."
— `campaign/guides/gm-guide/grand-game-in-play.md:82`

**`campaign/setting/villains/cassalanters.md`**

> "1. **Ninety-Nine Souls at the Founders' Day Feast** — the contract demands ninety-nine souls as well as the gold; the souls are the guests they mean to poison at the Founders' Day feast (Flamerule 1); method: the feast itself; contingency: partial payment will not be accepted (they don't know this yet); connects to **Cassalanter Villa**"
— `campaign/setting/villains/cassalanters.md:38`

> "2. **The 999,999 gp** — the contract needs the full sum alongside the souls; the family holds about 500,000 gp, and the Vault's 500,000 gp covers the shortfall; they hold Eye #2, found in the Brandath Crypts, and need the Stone plus Eyes #1 and #3 to open the Vault; method: political intelligence through Lords' Alliance contacts; connects to **Cassalanter Villa**"
— `campaign/setting/villains/cassalanters.md:39`

**Published buy-out terms** (the published text gives the price; ruling 2 names the feast guests as the souls):

> "The soul of Victoro's eldest son, Osvaldo, is forever lost and can't be saved. To allay his guilt, Victoro has forged a plan to win back the souls of his young twins, Terenzio and Elzerina. Under the terms of the contract, their souls will be forfeit on their ninth birthdays, and that day is fast approaching. But Victoro can buy his way out of the obligation by providing, as the contract states, \"one shy of a million gold coins and the sacrifice of one shy of a hundred unfortunate souls.\""
— `sources/adventure-wdh.json:32693`

**Other current campaign files with the same wording** (found by grep, listed by location only): `campaign/guides/gm-guide/structural-rules.md:52` and `:65`; `campaign/guides/gm-guide/about-this-campaign.md:19`; `campaign/guides/gm-guide/design-notes-running-the-campaign.md:67`; `campaign/setting/organizations/10-cassalanters.md:33`, `:80`, `:82`; `campaign/setting/lore/vault-of-dragons.md:115`; `campaign/setting/history/05-a-debt-in-blood.md:27`, `:45`, `:69`; `campaign/setting/deities/asmodeus.md:64`. Superseded structure files with soul-coin wording: `campaign/structure/ch2-city-of-splendors.md:117`, `:169`, `:292`; `campaign/structure/ch3-running-the-campaign.md:162`, `:186`.

---

## faction-knowledge

### A. Setting table (`campaign/setting/grand-game.md` lines 30-36), cell by cell

Heading and header:

> "*What Each Faction Knows at Campaign Start*"
— `campaign/setting/grand-game.md:28`

> "| Faction | What they know | What they have | What they're doing |"
— `campaign/setting/grand-game.md:30`

Rows, in full:

> "| Xanathar's Guild | Stone was with Dalakhar (now Gralhund/PCs); Dalakhar worked for Neverember | Eye #1 | Pursuing the Stone; hunting Dalakhar's trail |"
— `campaign/setting/grand-game.md:32`

> "| Manshoon's Zhentarim | Stone was with Dalakhar; Gralhunds intercepted it | Nothing | Urstul Floxin redirected to Gralhund Villa |"
— `campaign/setting/grand-game.md:33`

> "| Cassalanters | Vault exists (Lords' Alliance contact); have one Eye | Eye #2 | Raising the 999,999 gp and ninety-nine souls the contract demands (about 500,000 gp in hand, the Vault's 500,000 covers the rest); need the Stone plus Eyes #1 and #3 to open the Vault |"
— `campaign/setting/grand-game.md:34`

> "| Bregan D'aerthe | Full intelligence via Nar'l Xibrindas inside Xanathar's Guild | Eye #3 | Waiting to see which party proves most useful; observing all other factions |"
— `campaign/setting/grand-game.md:35`

> "| Doom Raiders | Aware of Grand Game at high level; not primary competitors for vault | Nothing | Maintaining territory; watching |"
— `campaign/setting/grand-game.md:36`

Source line for the table:

> "- `21. Faction Reports of the Grand Game.pdf` — what each faction knows at campaign start"
— `campaign/setting/grand-game.md:45`

### B. GM Guide table (`campaign/guides/gm-guide/running-the-villains.md` lines 34-41), cell by cell

Heading and header:

> "## Faction Knowledge at Campaign Start"
— `campaign/guides/gm-guide/running-the-villains.md:34`

> "| Faction | What They Know | What They Have | What They Need |"
— `campaign/guides/gm-guide/running-the-villains.md:36`

Rows, in full:

> "| Xanathar's Guild | Dalakhar was moving the Stone; Stone is now in circulation; does not know the Eyes' significance or the vault's location | Eye #1 (in Sylgar's bowl; Xanathar does not know what it is) | The Stone; the Eyes' significance |"
— `campaign/guides/gm-guide/running-the-villains.md:38`

> "| Manshoon's Zhentarim | The Stone exists and unlocks great wealth; Urstul Floxin's team was tracking Dalakhar; does not yet know the Stone reached the Gralhunds | Nothing | Stone + any two Eyes |"
— `campaign/guides/gm-guide/running-the-villains.md:39`

> "| The Cassalanters | Vault is beneath Brandath Crypts; does not yet know the Stone is in play or in circulation | Eye #2 | Stone + Eyes #1 and #3 |"
— `campaign/guides/gm-guide/running-the-villains.md:40`

> "| Bregan D'aerthe | Most complete picture via Nar'l Xibrindas; knows the Stone, the Eyes, and the vault; waiting to see which party proves most useful | Eye #3 | Stone + Eyes #1 and #2 |"
— `campaign/guides/gm-guide/running-the-villains.md:41`

The GM table has no Doom Raiders row. Ruling 1 keeps Doom Raiders as a fifth row.

Supporting GM text on the Eyes and BD knowledge:

> "**Eye #3** — held by Jarlaxle Baenre, aboard the *Scarlet Marpenoth*. It began in Renaer Neverember's mourning locket. Manshoon's Zhentarim seized the locket the night before Ches 1 and pried it open at the Candle Lane warehouse, Xanathar's Guild raided the warehouse and carried off the Eye with the rest of the back office without knowing what it was, and Bregan D'aerthe agents already inside Xanathar's hideout lifted it the same night. It reached Jarlaxle before the party reached the hideout, and Manshoon's cell never held it. Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep. He is active from Act I through his personas — J.B. Nevercott in Trollskull Alley and Zardoz Zord at the Field of Triumph — and his villain escalation keys off the **Jarlaxle Informed** flag set during **Fireball!**, which records only that the party made contact with him."
— `campaign/guides/gm-guide/running-the-villains.md:24`

> "> **Eye #1:** Xanathar — in Sylgar's bowl, Xanathar's Lair. Xanathar does not know what it is."
— `campaign/guides/gm-guide/running-the-villains.md:27`

> "> **Eye #2:** Cassalanters — vault beneath Cassalanter Villa (area A7). The family knows its function."
— `campaign/guides/gm-guide/running-the-villains.md:28`

> "> **Eye #3:** Jarlaxle Baenre — aboard the *Scarlet Marpenoth*. Jarlaxle knows exactly what it is. It passed from Renaer's locket to the Zhentarim, then to Xanathar's Guild in the warehouse raid, and Bregan D'aerthe agents inside Xanathar's hideout lifted it that night. Manshoon holds no Eye."
— `campaign/guides/gm-guide/running-the-villains.md:29`

### C. Row-by-row comparison

Status: "same", "differs", or "columns differ" (the setting's third column is "what they're doing" and the GM's is "what they need").

**Xanathar's Guild**

- *Know:* setting "Stone was with Dalakhar (now Gralhund/PCs); Dalakhar worked for Neverember" (`grand-game.md:32`) vs GM "Dalakhar was moving the Stone; Stone is now in circulation; does not know the Eyes' significance or the vault's location" (`running-the-villains.md:38`). **Differs.** The setting adds "Dalakhar worked for Neverember". The GM cell adds the Eyes-and-vault gap. The Alexandrian Xanathar briefing (Section D) bears on the Eyes gap.
- *Have:* setting "Eye #1" (`grand-game.md:32`) vs GM "Eye #1 (in Sylgar's bowl; Xanathar does not know what it is)" (`running-the-villains.md:38`). **Differs in detail.** The GM cell adds the location and the ignorance.
- *Doing / Need:* setting "Pursuing the Stone; hunting Dalakhar's trail" (`grand-game.md:32`, "what they're doing") vs GM "The Stone; the Eyes' significance" (`running-the-villains.md:38`, "what they need"). **Columns differ.**

**Manshoon's Zhentarim**

- *Know:* setting "Stone was with Dalakhar; Gralhunds intercepted it" (`grand-game.md:33`) vs GM "The Stone exists and unlocks great wealth; Urstul Floxin's team was tracking Dalakhar; does not yet know the Stone reached the Gralhunds" (`running-the-villains.md:39`). **Differs.** The setting says Manshoon's side knows the Gralhunds intercepted the Stone. The GM cell says Manshoon does not know it reached the Gralhunds. The published adventure says Urstul Floxin took it (Section F).
- *Have:* setting "Nothing" (`grand-game.md:33`) vs GM "Nothing" (`running-the-villains.md:39`). **Same.** The Alexandrian Manshoon report (Section D) and `running-the-villains.md:29` disagree (Section F).
- *Doing / Need:* setting "Urstul Floxin redirected to Gralhund Villa" (`grand-game.md:33`, "doing") vs GM "Stone + any two Eyes" (`running-the-villains.md:39`, "need"). **Columns differ.** The published adventure: "{@creature Urstul Floxin|wdh} is refusing to hand over the {@item Stone of Golorr|WDH} until he speaks to his secret master, {@creature Manshoon|WDH}." (`sources/adventure-wdh.json:4379`)

**Cassalanters**

- *Know:* setting "Vault exists (Lords' Alliance contact); have one Eye" (`grand-game.md:34`) vs GM "Vault is beneath Brandath Crypts; does not yet know the Stone is in play or in circulation" (`running-the-villains.md:40`). **Differs.** The setting names a "Lords' Alliance contact". No source found (Section G).
- *Have:* setting "Eye #2" (`grand-game.md:34`) vs GM "Eye #2" (`running-the-villains.md:40`). **Same.**
- *Doing / Need:* setting "Raising the 999,999 gp and ninety-nine souls the contract demands (about 500,000 gp in hand, the Vault's 500,000 covers the rest); need the Stone plus Eyes #1 and #3 to open the Vault" (`grand-game.md:34`) vs GM "Stone + Eyes #1 and #3" (`running-the-villains.md:40`). **Differs.** The setting's "doing" text has the 999,999 gp and ninety-nine souls wording that ruling 2 drops. The "need" half matches the GM cell.

**Bregan D'aerthe**

- *Know:* setting "Full intelligence via Nar'l Xibrindas inside Xanathar's Guild" (`grand-game.md:35`) vs GM "Most complete picture via Nar'l Xibrindas; knows the Stone, the Eyes, and the vault; waiting to see which party proves most useful" (`running-the-villains.md:41`). **Differs in wording.** Both name Nar'l. The GM cell adds the Stone, Eyes and vault. The Alexandrian Jarlaxle text says he was unaware at campaign start (Section D).
- *Have:* setting "Eye #3" (`grand-game.md:35`) vs GM "Eye #3" (`running-the-villains.md:41`). **Same.**
- *Doing / Need:* setting "Waiting to see which party proves most useful; observing all other factions" (`grand-game.md:35`, "doing") vs GM "Stone + Eyes #1 and #2" (`running-the-villains.md:41`, "need"). **Columns differ.** The GM cell's "waiting to see which party proves most useful" sits in its Know cell.

**Doom Raiders**

- Setting only (`grand-game.md:36`). No GM row. No Doom Raiders text appears in the Alexandrian Faction Reports (13 pages, all read), in `sources/2. Other Factions.pdf` (3 pages, all read), or in the Jarlaxle, Gralhund, Cassalanter and Xanathar reports. The only Doom Raiders reference in the Alexandrian text read here:

> "When he peeled off a large hunk of the local Zhentarim network established by the Doom Raiders (see p. 198 of Dragon Heist), he became aware that Lord Neverember had used the local Zhentarim's resources to embezzle hundreds of thousands of gold dragons from the government."
— `sources/1. The Villains.pdf:p.16`

Published text on the Doom Raiders (not about knowledge):

> "The Doom Raiders (described in appendix B) consider themselves the true Zhentarim of Waterdeep. The group's leaders are {@creature Davil Starsong|WDH} (Master of Opportunities and Negotiations), {@creature Istrid Horn|WDH} (Master of Trade and Coin), {@creature Skeemo Weirdbottle|WDH} (Master of Magic), {@creature Tashlyn Yafeera|WDH} (Master of Arms and Mercenaries), and {@creature Ziraj the Hunter|WDH} (Master of Assassination)."
— `sources/adventure-wdh.json:1447`

### D. Alexandrian text for each faction's starting knowledge

**Preface of the Faction Reports (governs every row below):**

> "The reports here do not necessarily reflect the knowledge held by each faction at the very beginning of Dragon Heist. They have been written to reflect the state of the reports at the time the PCs are most likely to encounter them (during the Eye Heists). During earlier events, the factions may still be trying to piece together some of this information."
— `sources/21. Faction Reports of the Grand Game.pdf:p.142`

This preface contradicts the source line the setting table cites (`grand-game.md:45`, "what each faction knows at campaign start") and the same claim in `campaign/structure/ch2-city-of-splendors.md:393` (Section E).

**Quick reference, p.142:**

> "The Stone of Golorr was stolen by Xanathar. It was taken from Xanathar by Dalakhar, and taken from Dalakhar by the Gralhunds."
— `sources/21. Faction Reports of the Grand Game.pdf:p.142`

> "Xanathar's Eye was originally stolen by the Zhentarim from the Protector's Enclave in Neverwinter. Xanathar slew a Zhentarim embassy and took the Eye."
— `sources/21. Faction Reports of the Grand Game.pdf:p.142`

> "The Zhentarim Eye was taken from Renaer's mourning locket."
— `sources/21. Faction Reports of the Grand Game.pdf:p.142`

> "The Cassalanter Eye was taken from the crypt of Lady Alethea Brandath."
— `sources/21. Faction Reports of the Grand Game.pdf:p.142`

**Xanathar.** Alexandrian design text:

> "When Xanathar had the Stone of Golorr stolen from the Palace of Waterdeep, he only knew that he was stealing an object of great importance to Lord Neverember (i.e., Neverember's Enigma). When he later learned about the missing dragons, he believed that he was now in possession of the whole key to Neverember's Enigma. And he was perfectly happy with that. You don't need to actually hold the gold if you're the one who controls its location."
— `sources/1. The Villains.pdf:p.15`

> "What he didn't know was that the Stone of Golorr had been blinded by Lord Neverember, who removed its three Eyes. (More on this in Part 4 of the remix.)"
— `sources/1. The Villains.pdf:p.15`

Faction Reports (handwritten; transcribed):

> "The First Eye is held by Xanathar, and lies somewhere within his lair."
— `sources/21. Faction Reports of the Grand Game.pdf:p.144`

> "The gnome Dalakhar was an agent of Lord Neverember, seeking to reclaim Neverember's Enigma, which you had by rights taken from our former Open Lord."
— `sources/21. Faction Reports of the Grand Game.pdf:p.152` (the Xanathar briefing runs over onto this page)

> "The Eye you hold is one of Three which belong to the Stone."
— `sources/21. Faction Reports of the Grand Game.pdf:p.151` (Xanathar briefing from Ahmaergo, written to the Eye heist, not campaign start)

> "The Enigma is, in fact, the Stone of Golorr."
— `sources/21. Faction Reports of the Grand Game.pdf:p.152` (same briefing)

**Manshoon / Zhentarim.** Alexandrian design text:

> "Manshoon wanted to know where that money has gone. He knew that Neverember didn't actually have it in his possession, so he sent agents to infiltrate Neverember's household in Neverwinter to find out. Those agents weren't able to fully ascertain where the gold was, but they did identify the Eye as the key to getting it. They stole the Eye from the Protector's Enclave and brought it to Manshoon, who through a combination of divinations and other espionage efforts eventually connected it to the Stone of Golorr which Xanathar had stolen."
— `sources/1. The Villains.pdf:p.16`

> "Most of Manshoon's clones were destroyed during the Manshoon Wars, but yet another has recently returned to Waterdeep (claiming, as they all do, to be the one true Manshoon)."
— `sources/1. The Villains.pdf:p.16`

Faction Reports (handwritten; transcribed):

> "The Neverwinter Eye was obtained from the Protector's Enclave in Neverwinter, but was taken by Xanathar's treachery. It remains in the beholder's possession."
— `sources/21. Faction Reports of the Grand Game.pdf:p.153`

> "The Waterdeep Eye has been taken from Renaer Neverember and secured within the library's Astral Vault."
— `sources/21. Faction Reports of the Grand Game.pdf:p.153`

> "It is apparent, based on interrogations of their imp agents, that the Cassalanters possess the third eye, although it is uncertain where the Cassalanter Eye originated. Perhaps Lord Dagult entrusted it to them."
— `sources/21. Faction Reports of the Grand Game.pdf:p.154`

**Cassalanters.** Alexandrian design text:

> "They discovered that Neverember had hidden one of the Eyes in the crypt of Lady Alethea Brandath, Renaer's mother. They went to the crypt and extracted the Eye from the magical wards Dagult Neverember had placed around it. (Ironically, they were literally standing on top of the Vault itself and didn't know it.)"
— `sources/1. The Villains.pdf:p.18`

> "The Cassalanters have discovered a ritual which can save them, but it requires them to sacrifice \"one shy of a million gold coins\". They are quite rich, but even in leveraging everything they own they still can't raise that monstrous sum."
— `sources/1. The Villains.pdf:p.19`

> "Obviously they don't tell the PCs that the ritual also involves killing 99 people. (Unless they have some reason to think that the PCs would think that to be a great idea.) They don't technically need all the money, and are willing to cut the PCs in on 10% of it or agree to return the surplus funds to the city."
— `sources/1. The Villains.pdf:p.19`

Faction Reports (handwritten; transcribed):

> "It was those gossipmongers the Brassfeathers who first babbled out the revelation that Neverember had embezzled half a million gold dragons from the treasuries of Waterdeep."
— `sources/21. Faction Reports of the Grand Game.pdf:p.147` ("Brassfeathers" is uncertain in the transcription)

> "We are now certain that he used the Stone to hide the location in which he has secreted the embezzled dragons. As such, it is virtually certain that the only path to this hoard lies through the Stone itself."
— `sources/21. Faction Reports of the Grand Game.pdf:p.147`

"Notes on the Dispositions of the Eyes" (unattributed; handwritten; transcribed):

> "It is now clear that lord Dagult had the Stone of Golorr blinded by removing its Eyes, and that the artifact we recovered was Alethea's Eye."
— `sources/21. Faction Reports of the Grand Game.pdf:p.150`

> "Dagult's Eye was kept close by the lord Protector, who carried it with him to Neverwinter and most likely had it on his person when Laeral deposed him as Open Lord."
— `sources/21. Faction Reports of the Grand Game.pdf:p.150`

**Bregan D'aerthe / Jarlaxle.** Alexandrian design text:

> "As Dragon Heist begins, Jarlaxle is unaware of the Stone of Golorr or the Grand Game which is being played. Freshly arrived in his cover identity as Captain Zord of the Sea Maiden's Faire, Jarlaxle is coordinating and ramping up his local intelligence operations."
— `sources/1. The Villains.pdf:p.17`

Faction Report, Jarlaxle's report (handwritten; transcribed):

> "It is clear from its contents that Jarlaxle was, until recently, unaware of the Grand Game currently taking place in Waterdeep."
— `sources/21. Faction Reports of the Grand Game.pdf:p.145`

> "There are numerous factions in play, but I suspect the most significant are these: The Cassalanters, Xanathar (that bloated bag of gas), the Manshoonian Zhentarim, the Gralhunds, Lord Dagult, and the Open Lord."
— `sources/21. Faction Reports of the Grand Game.pdf:p.145`

> "Of prime importance are the Golorr Eyes: Xanathar's Eye, I suspect, has been entrusted to Sylgar's keeping. Manshoon's Eye is almost certainly secured within Kolat Towers. The Cassalanter's Eye probably lies somewhere in their Estate."
— `sources/21. Faction Reports of the Grand Game.pdf:p.145`

Published text on Nar'l, the BD source inside Xanathar's Guild:

> "{@creature Nar'l Xibrindas|wdh} is a {@creature drow mage}. He prepares and casts the {@spell sending} spell whenever he needs to communicate with his brother."
— `sources/adventure-wdh.json:32331`

**Gralhunds (not a table row; for completeness).**

> "The Gralhunds didn't know that Xanathar held the Stone of Golorr, but when it was stolen they were among the first to suspect (and then know) that Dalakhar was responsible."
— `sources/2. Other Factions.pdf:p.20`

> "THE NIMBLEWRIGHT: Two days after Dalakhar stole the Stone, the Gralhunds located him and dispatched their newly acquired nimblewright to find him. In Trollskull Alley, the nimblewright uses a fireball spell to kill Dalakhar and the Zhentarim agents trailing him. The nimblewright then grabs the Stone of Golorr from Dalakhar's corpse and flees the scene, returning to the Gralhund Villa with his prize (see Part 2)."
— `sources/2. Other Factions.pdf:p.21`

**Open Lord (not a table row; for completeness).**

> "OPEN LORD: The Open Lord of Waterdeep isn't exactly a “minor” faction, but Laeral Silverhand is considerably behind the curve in the current Grand Game. She knows that Lord Neverember embezzled 500,000 dragons from the city, but as Dragon Heist begins she is under the belief that he already has the money in Neverwinter."
— `sources/2. Other Factions.pdf:p.21`

### E. Other files that restate the table or its claims

- `campaign/structure/ch2-city-of-splendors.md` (superseded structure document, restates the table):

> "*What Each Faction Knows at Campaign Start*"
— `campaign/structure/ch2-city-of-splendors.md:163`

> "| Cassalanters | Vault exists (Lords' Alliance contact); have one Eye | One Eye | Accumulating soul coins; not yet pursuing Stone actively |"
— `campaign/structure/ch2-city-of-splendors.md:169`

> "| Bregan D'aerthe | Full intelligence via Nar'l Xibrindas inside Xanathar Guild | No Eye yet | Moving to acquire one; observing all other factions |"
— `campaign/structure/ch2-city-of-splendors.md:170`

> "| Doom Raiders | Aware of Grand Game at high level; not primary competitors for vault | Nothing | Maintaining territory; watching |"
— `campaign/structure/ch2-city-of-splendors.md:171`

> "- `21. Faction Reports of the Grand Game.pdf`: what each faction knows at campaign start — primary source for the starting intelligence table"
— `campaign/structure/ch2-city-of-splendors.md:393`

- `campaign/structure/ch3-running-the-campaign.md` (superseded structure document, prose restatement):

> "*Starting Faction Knowledge (campaign day one)*"
— `campaign/structure/ch3-running-the-campaign.md:156`

> "- **Xanathar's Guild:** Knows Dalakhar was moving the Stone; knows the Stone is now in circulation; does not know about the Eyes or the vault's location; is reacting to the loss of expected income rather than pursuing the gold directly; Nar'l Xibrindas's intelligence has been selectively filtered by Jarlaxle"
— `campaign/structure/ch3-running-the-campaign.md:160`

> "- **Manshoon's Splinter Cell:** Knows the Stone exists and what it unlocks; Urstul Floxin's team has been tracking Dalakhar; does not yet know the Stone reached the Gralhunds; Kolat Towers is established and operational"
— `campaign/structure/ch3-running-the-campaign.md:161`

> "- **The Cassalanters:** Know exactly what they need and why (the vault gold pays the debt); have been planning the Founders' Day timeline for eight years; do not yet know the Stone is in play; their outpost network is focused on soul coin acquisition, not the Stone"
— `campaign/structure/ch3-running-the-campaign.md:162`

> "- **Bregan D'aerthe:** Nar'l Xibrindas has fed Jarlaxle accurate intelligence about the Stone and the Eyes since before the campaign begins; Jarlaxle has the most complete picture of any faction; the Sea Maidens Faire is in port and operational; he is waiting to see which party proves most useful"
— `campaign/structure/ch3-running-the-campaign.md:163`

> "- `21. Faction Reports of the Grand Game.pdf` — what each faction knows at campaign start; inter-faction intelligence"
— `campaign/structure/ch3-running-the-campaign.md:302`

- `campaign/setting/lore/vault-of-dragons.md` ("Who Knows What at Campaign Start"):

> "- **Xanathar's Guild:** It knows Dalakhar was moving the Stone, and it does not know what the Eyes are or where the vault is."
— `campaign/setting/lore/vault-of-dragons.md:95`

> "- **Manshoon's Zhentarim:** They know the Stone exists and unlocks great wealth."
— `campaign/setting/lore/vault-of-dragons.md:96`

> "- **Bregan D'aerthe:** Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep."
— `campaign/setting/lore/vault-of-dragons.md:97`

> "- **The Cassalanters:** They hold Eye #2 and know it belongs to the Stone. They do not yet know the Stone has surfaced, and this page treats them as not knowing where the vault lies (see Draft Notes)."
— `campaign/setting/lore/vault-of-dragons.md:98`

- `campaign/setting/history/08-the-players-arrive.md:138` (stale-table note):

> "- **Settled:** `setting/grand-game.md` line 32 (\"Dalakhar worked for Renaer\") and line 34 (\"soul coins\", \"not yet pursuing Stone\") are stale against the rulings, including \"no soul coins\". `running-the-villains.md` line 71 calls Xanathar and Manshoon a \"cold war\", where the ruling is an active low-level street war. Neither file is edited here."
— `campaign/setting/history/08-the-players-arrive.md:138`

- `campaign/setting/history/05-a-debt-in-blood.md:144` (stale-table note):

> "- **Settled:** Outpost purpose. The outposts gather gold and ritual components, the Vault covers the shortfall, and there are no soul coins (standing ruling). The soul-coin design remains in `villains/cassalanters.md` lines 38 and 39, `grand-game-in-play.md` lines 53 and 67, `setting/grand-game.md` line 34 and the Cassalanter content of `arc-e`, and is stale there."
— `campaign/setting/history/05-a-debt-in-blood.md:144`

- `campaign/setting/history/07-a-city-watching-itself.md:186` (note on the table's missing row):

> "- **Conflicts:** `grand-game.md` has no row for the Lords' Alliance or for Laeral, so it cannot contradict this page. The Pass 4 reshaping should add the government's place in the Grand Game."
— `campaign/setting/history/07-a-city-watching-itself.md:186`

- `campaign/guides/gm-guide/grand-game-in-play.md:3` (points to the GM table for faction knowledge):

> "The Grand Game doesn't wait. While the party rests, the factions are moving: issuing orders, reading intelligence, replenishing losses, and adjusting to whatever the PCs did last session. Between sessions, use this routine to keep four active villain factions coherent without rebuilding them from scratch each session. For the reference tables (faction knowledge at campaign start, the full escalation tier table, and the inter-faction operations matrix), see **Running the Villains**."
— `campaign/guides/gm-guide/grand-game-in-play.md:3`

- `campaign/setting/grand-game.md:45` and `campaign/structure/ch3-running-the-campaign.md:302` cite PDF 21 as the starting-knowledge source (quoted above).

### F. Conflicts between sources

1. **PDF 21 as the starting-knowledge source.** The setting table cites `21.` for "what each faction knows at campaign start" (`grand-game.md:45`). The Faction Reports' own preface says:
> "The reports here do not necessarily reflect the knowledge held by each faction at the very beginning of Dragon Heist."
— `sources/21. Faction Reports of the Grand Game.pdf:p.142`

2. **Jarlaxle's starting awareness.** The GM table says "Most complete picture via Nar'l Xibrindas; knows the Stone, the Eyes, and the vault" (`running-the-villains.md:41`), and `running-the-villains.md:24` says he "has known of the Stone, the Eyes and the vault since he arrived" (the quoted paragraph). The Alexandrian design text says he "is unaware of the Stone of Golorr or the Grand Game" (`sources/1. The Villains.pdf:p.17`), and the Jarlaxle report says he was "until recently, unaware" (`sources/21. Faction Reports of the Grand Game.pdf:p.145`). The campaign records a user settlement overruling the Alexandrian line:
> "**Settled by the user (Session 47):** When Jarlaxle learned of the vault. \"He's known about it since getting to Waterdeep, whenever that was.\""
— `campaign/setting/history/03-bregan-daerthes-long-road.md:160`

3. **Who took the Stone from Dalakhar.** The published adventure says Urstul Floxin took it:
> "Dalakhar is killed by a fireball spell. Urstul Floxin steals the Stone of Golorr from Dalakhar's corpse."
— `sources/adventure-wdh.json:862`
The Alexandrian PDF says the Gralhund nimblewright took it (`sources/2. Other Factions.pdf:p.21`, Section D). The setting table's Manshoon row says "Gralhunds intercepted it" (`grand-game.md:33`). The campaign files do not say which account they follow. The orchestrator decides.

4. **Manshoon and the Eyes.** The GM table says "Manshoon holds no Eye." (`running-the-villains.md:29`). The Alexandrian Jarlaxle report says "Manshoon's Eye is almost certainly secured within Kolat Towers." (`sources/21. Faction Reports of the Grand Game.pdf:p.145`). The Alexandrian Manshoon report says "The Waterdeep Eye has been taken from Renaer Neverember and secured within the library's Astral Vault." (`p.153`). Both reports are written to the Eye heists (`p.142`).

5. **Xanathar and its Eye.** The GM table says "Xanathar does not know what it is." (`running-the-villains.md:27`). The Alexandrian Xanathar briefing says "The Eye you hold is one of Three which belong to the Stone." (`sources/21. Faction Reports of the Grand Game.pdf:p.151`). The same time caveat applies (`p.142`).

6. **Xanathar and the vault.** The GM table says Xanathar "does not know the Eyes' significance or the vault's location" (`running-the-villains.md:38`). The wiki says:
> "Though it had also been able to locate the vault within which the treasure was kept, it had been forced out by the vault's draconic guardian."
— `sources/research/pass4-bundles/faction-knowledge/wiki.txt:153`

7. **Cassalanter Eye origin.** `running-the-villains.md:28` says "The family knows its function." The Alexandrian Manshoon report says "it is uncertain where the Cassalanter Eye originated." (`sources/21. Faction Reports of the Grand Game.pdf:p.154`). The Alexandrian Cassalanter design text says they extracted it from Alethea's crypt (`sources/1. The Villains.pdf:p.18`).

8. **Cassalanter wealth.** The setting table says "about 500,000 gp in hand" (`grand-game.md:34`). The Alexandrian text says "even in leveraging everything they own they still can't raise that monstrous sum." (`sources/1. The Villains.pdf:p.19`). The Cassalanter organization page says "They hold about half the gold" (`campaign/setting/organizations/10-cassalanters.md:33`), and its draft notes keep the 500,000 gp figure (`campaign/setting/organizations/10-cassalanters.md:116`).

9. **Cassalanter Eye numbering.** The Alexandrian Manshoon report calls the Cassalanter Eye "the third eye" (`p.154`). The campaign calls it "Eye #2" (`running-the-villains.md:28`).

10. **Lords' Alliance contact.** The setting table says "Vault exists (Lords' Alliance contact)" (`grand-game.md:34`). The GM table does not (`running-the-villains.md:40`). No source found (Section G).

### G. Not found

- "Lords' Alliance contact" for the Cassalanters: not in `sources/adventure-wdh.json` (lines 538, 31716, 32691-32693 read), in `sources/1. The Villains.pdf` (pp.17-19), or in the Cassalanter pages of `sources/21.` (pp.146-147 read).
- Doom Raiders starting knowledge: no Faction Report and no GM row. Searched all 13 pages of `sources/21.`, all 3 pages of `sources/2. Other Factions.pdf`, and `sources/1. The Villains.pdf` pp.13-19.
- Front businesses for Manshoon (Trades Ward importing company) and for the Cassalanters (charitable hospital): not found in any source read (see the front-business section above).
- Watch informants in every ward; every faction's informants in the Watch; Skeemo compiling intelligence; Durnan "heard everything": not in the published adventure, the Alexandrian PDFs read, or the Alexandrian markdown.
- Social events as intelligence operations or recruitment screens: not in the published adventure or the Alexandrian text read.
- "No governing body" for the Grand Game: not found.

### H. Not readable

- `sources/research/pass4-bundles/grand-game/wiki.txt` contains only `NOT FOUND: Grand Game`.
- Empty: `sources/research/pass4-bundles/grand-game/adventure.txt`, `sources/research/pass4-bundles/grand-game/adventure-hits.txt`, `sources/research/pass4-bundles/faction-knowledge/adventure.txt`, `sources/research/pass4-bundles/faction-knowledge/adventure-hits.txt`.
- `sources/1. The Villains.pdf` and `sources/21. Faction Reports of the Grand Game.pdf` have no text layer. The quotes are transcriptions. The least certain are the handwritten lines in `21.`, notably "Brassfeathers" (`p.147`) and the "lord Dagult" wording on `p.150`. Check them against the page image before use.
- `sources/research/pass4-bundles/faction-knowledge/wiki.txt` has 1921 lines. Only lines 1-576 were read. The Cassalanter and Manshoon wiki pages were not reached.
- The `.docx` files in `sources/Other remix files/` were not checked. The source guide does not name them for these topics.
