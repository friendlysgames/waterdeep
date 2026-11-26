# Pass 6 research notes: Istrid Horn

Page: `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Istrid is one of the five Masters of the cell and a named lieutenant, so she is treated as a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/06-doom-raiders.md` (H1 "The Zhentarim (Doom Raiders)")
Factions Guide: `campaign/guides/factions/07-doom-raiders.md`. No Villains page exists for the Doom Raiders.
Voice profile: `.claude/skills/character-voices/voices/doom-raiders.md` (### Istrid Horn, lines 44 to 58)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines. Bullet markers (`- `, `> - `) are left out of quotes where they are markup, except where the bullet is part of the quoted line.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field is given where the entry has one. Where a quote stops inside a sentence, the rest of the sentence is named in brackets.
- Wiki: the scratchpad extract `wiki-doom-raiders/03-istrid-horn.txt` is quoted as "wiki line N" (that file's lines). Its infobox `refs5e` (line 60) is `WDH-199` (*Waterdeep: Dragon Heist*, 5e). The wiki prints no edition on most sentences; editions below are taken from the ref names and marked as inferred. The bundle `sources/research/pass5-bundles/doom-raiders/wiki.txt` has two bare "Istrid" hits: line 487 is the Dragon Heist index entry `{{P|[[Istrid Horn]]|17,42,'''199'''}}`, and line 365 was not read in context.
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` was read as rendered pages 1 to 3 (printed pp. 23 to 25). Istrid is not named there. The one Zhentarim passage on printed p. 25 is quoted in section E as context. It is a transcription from the image and needs a `pdftotext -layout` check before any prose uses it. `sources/5. Faction Outposts.pdf`, `sources/17. Outpost and Lair Revelation Lists.pdf` and `sources/11. Lair  Xanathar’s Lair.pdf` were not read. PDFs cannot be searched with Grep, `SOURCE_GUIDE.md` has no line naming Istrid, and the outposts and lairs are the villain factions' sites.
- Alexandrian markdown: `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md` were searched with Grep for "Istrid" and "Skeemo". Appendix C has no Istrid line. `sources/Appendix_D_-_Running_the_Tavern.md` was searched for Istrid.
- No shell was available and no Edit tool was available, so this file was written in full. `voicecheck.py` was not run. No other file was edited.

## Findings that change how the page is written

1. **Alignment.** The page and two campaign files say lawful evil. The wiki says neutral evil (wiki line 57). The published adventure gives no alignment. Campaign wins; the wiki conflict is listed in D1.
2. **Stat block.** The Summary says "Veteran" (line 5). No source gives Istrid a stat block, and the Doom Raiders mechanics reference says `"Veteran" does not exist in XMM` (`docs/plans/doom-raiders-mechanics-reference.md:252`). The wiki gives Cleric 9 and CR 8 (wiki lines 58 and 59). See B and D2.
3. **Day-one history is thin.** The only campaign-start biography is the published adventure's two-sentence entry, `sources/adventure-wdh.json:31934` and `:31935`. The wiki gives the adventuring past, the 1489 DR posting and the 1492 DR lending operation. Nothing gives birth, family, age, origin or how she rose to Master. Background gaps are in F.
4. **Quest-time sentences on the page are few.** The page's own sentences are almost all day-one. Its two quest-time items are the "Featured in" list (L7) and, in a softer form, the Emmek Frewn loan figure (L25). The wiki's Gralhund aftermath sentence (wiki line 73) is quest-time and is not used.
5. **Pronouns** are she/her on the page (line 5). The campaign's source is `sources/adventure-wdh.json:6104` ("Istrid chose a safe, public place for the meeting ... she came alone"). `campaign/gazetteer/waterdeep/dock-ward.md:254` says the pronouns come from the First Meeting event, not the Notable page. Both agree.
6. **The Overview is 35 words** (line 29), over the brief's 21-word limit.

---

## A. Background facts by theme

### A1. Origin, birth, family, age

No source gives Istrid's birthplace, age, birth year, parents, siblings, spouse or children.

**Wiki infobox (*Waterdeep: Dragon Heist*, 5e, `WDH-199`)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]"
> — wiki line 11

> "| ethnicity      = [[Shield dwarf]]"
> — wiki line 15

> "| age            = "
> — wiki line 17 (blank). Lines 21 (dob), 29 (parents), 30 (spouses), 31 (siblings) and 32 (children) are also blank.

**Adventure, Istrid entry (page 199)**
> "{@creature Istrid Horn|wdh|Istrid} is regarded as the Black Network's Master of Trade and Coin in Waterdeep. The shield dwarf operates an illegal lending operation out of a heavily guarded warehouse in the Dock Ward, offering loans to those in need of coin. Her interest rates are comparable to those of her competitors (including noble families of bankers such as the Cassalanters and the Irlingstars), but the penalties for not paying back Istrid's loans are severe."
> — `sources/adventure-wdh.json:31934` (entry "Istrid Horn", page 199)

### A2. Adventuring past and how she joined the Zhentarim

**Wiki (5e, `WDH-40` for the sentence)**
> "Istrid was once an adventurer but together with her adventuring companions she decided to join the Zhentarim."
> — wiki line 71

**Wiki (5e, `WDH-199`)**
> "Istrid was a member of the [[Doom Raiders]] adventuring company. She and her former companions composed the leadership of the Zhentarim of Waterdeep. As the Waterdhavian "Master of Trade and Coins" for the Zhentarim, Istrid employed many thugs and enforcers to collect on her loans."
> — wiki line 68 (the wiki's "Waterdhavian" is the wiki's wording; the campaign uses "Waterdeep")

**Adventure, the Doom Raiders' past (Appendix B, Zhentarim paragraph, pasted here from the JSON)**
> "Adventurers can't join {@creature Manshoon|WDH}'s cause, but they can join and receive aid from the Zhents who are opposed to him. The leaders of this branch of the Black Network are retired adventurers who have become business entrepreneurs. Their adventuring party was called the Doom Raiders because their specialty was plundering lich lairs (which are called \"dooms\"). They are desperately trying to gain a legitimate economic foothold in Waterdeep, which requires making alliances with local guilds and nobles. {@creature Manshoon|WDH}'s war against the Xanathar Guild has thrown their plans into upheaval."
> — `sources/adventure-wdh.json:1446` (the adventuring party, not Istrid alone)

**Adventure, Appendix B (the cell's arrival)**
> "In Waterdeep, the faction available to player characters is the **Doom Raiders** — a cell of experienced operators who arrived in the city several years ago and built a network of commercial fronts they genuinely believe in."
> — `sources/Appendix_B_-_Player_Factions.md:506`

**Campaign, Doom Raiders organization page (the cell's dates)**
> "The entries run from the founding of the Black Network to the day the campaign starts. No source dates the Doom Raiders' adventuring career, so the cell's own story begins in the late 1480s."
> — `campaign/setting/organizations/06-doom-raiders.md:19`

> "- **Late 1480s DR, they join the Zhentarim:** The five gave up adventuring and joined the reformed Black Network (*Dragon Heist*, 5e; Forgotten Realms Wiki, *Doom Raiders*, 5e)."
> — `campaign/setting/organizations/06-doom-raiders.md:24`

**Wiki (5e, `WDH-198-199`)**
> "In [[1489 DR]], Istrid and her fellow agents were sent to establish a Zhent foothold in Waterdeep."
> — wiki line 71. No source names who sent them (`campaign/setting/organizations/06-doom-raiders.md:25`: "They were sent to establish a Zhentarim foothold, and no source names who sent them").

### A3. Rise to Master of Trade and Coin

**Adventure (the title)**
> "{@creature Istrid Horn|WDH} (Master of Trade and Coin)"
> — `sources/adventure-wdh.json:1447` (the list of the five leaders)

**Wiki (infobox, lines 7 and 16)**
> "| titles         = Master of Trade and Coins"
> — wiki line 7 (the wiki's plural "Coins"; see D3)

> "| occupation     = Master of Trade and Coins for the [[Zhentarim]]<ref name="WDH-199" />"
> — wiki line 16

No source describes how she won the post. The Doom Raiders organization page gives the title and the job:

> "- **Istrid Horn, Master of Trade and Coin:** She runs an illegal lending operation from a heavily guarded warehouse in the Dock Ward, and her thugs and enforcers collect."
> — `campaign/setting/organizations/06-doom-raiders.md:58`

### A4. The lending operation (her post, a person fact)

**Campaign, Dock Ward gazetteer (the warehouse)**
> "**Istrid Horn's Warehouse** — Moneylending house"
> — `campaign/gazetteer/waterdeep/dock-ward.md:93`

> "A guarded warehouse on a Dock Ward street of salt-stained brick, with two broad-shouldered guards at the side door. Crates stack to the rafters, and a small lamplit office at the back holds Istrid's ledger."
> — `campaign/gazetteer/waterdeep/dock-ward.md:94`

> "**Istrid Horn** lends from it for the Doom Raiders, up to 200 gp with 10 percent of the principal added at the end of each tenday."
> — `campaign/gazetteer/waterdeep/dock-ward.md:95`

**Wiki (5e, `WDH-199`, with the Emmek ref `WDH-98`)**
> "In [[1492 DR]],{{WDH-time}} Istrid managed an illegal lending operation in a warehouse in the [[Dock Ward]]. Her interest rates were comparable to noble bankers like the [[Cassalanter]] or the [[Irlingstars|Irlingstars]] but her penalties were very severe.<ref name="WDH-199" /> One of her debtors was [[Emmek Frewn]].<ref name="WDH-98">{{Cite book/Waterdeep: Dragon Heist|98}}</ref>"
> — wiki line 73 (the first two sentences are day-one; the rest of that paragraph is quest-time, see C)

**Campaign, Doom Raiders organization page (the cell's funding)**
> "- **Funding:** The cell earns from lending, from the sellswords Tashlyn supplies, from discounted potions and poisons at Skeemo's shop, and from the introductions Davil sells (*Dragon Heist*, 5e). Ziraj can be hired for a killing, in return for an undisclosed favor that the cell calls in later (*Dragon Heist*, 5e). `[research]` No source gives the cell a treasury or a yearly income."
> — `campaign/setting/organizations/06-doom-raiders.md:71`

### A5. Relationships to named figures

**Davil Starsong (the cell's head)**
> "**Relationships.** Davil is the cell leader of the Doom Raiders (Waterdeep Zhentarim), the faction contact for Zhentarim-aligned PCs, a permanent resident at the Yawning Portal (second floor business room, third floor suite), a colleague of Istrid, Tashlyn, Ziraj, and the traitor Skeemo Weirdbottle, and the unknowing target of Nihiloor's intellect devourer, with Meloon watching him and waiting for a clean opportunity to kill him without witnesses."
> — `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:25` (Davil's page; the clause about Nihiloor's devourer is about Davil)

> "Davil can put the characters in contact with other leaders of the Black Network's Waterdeep division, namely {@creature Istrid Horn|WDH} (if they need a loan), {@creature Skeemo Weirdbottle|WDH} (if they need magic), {@creature Tashlyn Yafeera|WDH} (if they need weapons or mercenaries), and {@creature Ziraj the Hunter|WDH} (if they need a highly skilled assassin)."
> — `sources/adventure-wdh.json:31925`

**Ziraj the Hunter (the cell's assassin)**
> "If Ziraj sets out to kill someone, it's because one of his friends (Davil, Istrid, Skeemo, or Tashlyn) asked him to."
> — `sources/adventure-wdh.json:31965`

**Her former companions (the cell's loyalty rule)**
> "- **The Network Looks After Its Own:** A member of the cell is one of theirs. When something goes wrong the faction does what it can, and it expects the same loyalty in return. Anyone who betrays or harms Istrid Horn finds her former adventuring companions using every resource they have to ruin them. The loyalty is personal as well as institutional."
> — `campaign/setting/organizations/06-doom-raiders.md:37`

**Emmek Frewn (debtor)**
> "Emmek secures a 150 gp loan from {@creature Istrid Horn|WDH} (see {@adventure appendix B|WDH|12}). He spends 50 gp for the services of the Shard Shunners, a gang of halfling wererats with which he has had nefarious dealings in the past. He pays the halflings to hinder the characters' efforts while he works feverishly to manage his own business."
> — `sources/adventure-wdh.json:4264` (the Trollskull "Plans" entry, page 42; see E for the later figure)

> "- Emmek is a refugee from Neverwinter whose sisters bought him out of the family tanning business. He owes **Istrid Horn** a loan of 150 gp, enforced by Zhentarim thugs, and he pays the Shard Shunners, a halfling wererat gang, to sabotage the party."
> — `campaign/gazetteer/waterdeep/north-ward.md:135`

> "- Istrid likes having people in her debt and treats every loan as leverage. Emmek Frewn owes her 150 gp, and Zhentarim thugs collect it."
> — `campaign/gazetteer/waterdeep/dock-ward.md:141`

**Cassalanters and Irlingstars (rival lenders)**
> "Her interest rates are comparable to those of her competitors (including noble families of bankers such as the Cassalanters and the Irlingstars), but the penalties for not paying back Istrid's loans are severe."
> — `sources/adventure-wdh.json:31934` (see A4 for the full entry)

**Skeemo Weirdbottle (fellow Master)**
The only sourced link is the shared list of the cell's leaders:
> "The Doom Raiders (described in appendix B) consider themselves the true Zhentarim of Waterdeep. The group's leaders are {@creature Davil Starsong|WDH} (Master of Opportunities and Negotiations), {@creature Istrid Horn|WDH} (Master of Trade and Coin), {@creature Skeemo Weirdbottle|WDH} (Master of Magic), {@creature Tashlyn Yafeera|WDH} (Master of Arms and Mercenaries), and {@creature Ziraj the Hunter|WDH} (Master of Assassination)."
> — `sources/adventure-wdh.json:1447`. No source gives Istrid and Skeemo a dealing with each other (see F8).

### A6. Faith

**Adventure**
> "Istrid worships Vergadain, the dwarven god of wealth and luck. She likes having others indebted to her, and she employs thugs and enforcers to collect on her loans. If those resources prove inadequate, Istrid can call on her old adventuring companions for assistance."
> — `sources/adventure-wdh.json:31935`

**Campaign, Doom Raiders organization page**
> "Istrid worships Vergadain, the dwarf god of wealth and luck, and blesses each signed agreement with "Vergadain smile on it". Yagra wears a red jade Zhentarim pendant openly, and it bears the Zhentarim's winged-serpent sigil (**Istrid Horn**; **Dock Ward**; **Yagra Stonefist**; Alexandrian remix, Appendix B)."
> — `campaign/setting/organizations/06-doom-raiders.md:43` (the sentence sits inside the Doctrine and Rites bullet; the rest of the bullet covers Yagra's pendant and the wiki's banner)

**Campaign, voice profile**
> "She blesses every signed agreement ("Vergadain smile on it")."
> — `.claude/skills/character-voices/voices/doom-raiders.md:52` (Quirks)

**Wiki (5e, `WDH-199`)**
> "| patron deity   = [[Vergadain]]"
> — wiki line 18

Vergadain has no deity page. The deity pages say so as plain text: `campaign/setting/deities/gond.md:132` lists "Vergadain" among names "with no page", and `campaign/setting/deities/mammon.md:101` says "Vergadain and Zhentil Keep appear as plain text."

### A7. Signature belongings and places

**Campaign, Dock Ward (the ledger)**
> "a small lamplit office at the back holds Istrid's ledger."
> — `campaign/gazetteer/waterdeep/dock-ward.md:94`

**Campaign, voice profile (the ledger habit)**
> "She taps the ledger with one finger when naming a figure."
> — `.claude/skills/character-voices/voices/doom-raiders.md:52` (Quirks)

**Campaign, GM Debts guide (the ledger as a Holder's tool)**
> "The loan has since been partially repaid. What remains isn't enough to panic over. What remains is enough to keep you in Istrid Horn's ledger, and her ledger is, as best you can determine, flawless. Every entry. Every outstanding balance. Every note about a debtor's known associates."
> — `campaign/guides/gm-guide/debts-of-the-city.md:31`

### A8. How long in post

**Campaign, Doom Raiders organization page**
> "- **1489 DR, the cell reaches Waterdeep:** The Doom Raiders are a cell of experienced Zhentarim operators who arrived in Waterdeep in 1489 DR, the first Zhentarim cell in the city, and built a network of commercial fronts they genuinely believe in."
> — `campaign/setting/organizations/06-doom-raiders.md:25` (the full bullet is longer; it continues "They were sent to establish a Zhentarim foothold, and no source names who sent them (*Dragon Heist*, 5e; Forgotten Realms Wiki, *Doom Raiders*, 5e).")

**Wiki (5e, `WDH-198-199`)**
> "In [[1489 DR]], Istrid and her fellow agents were sent to establish a Zhent foothold in Waterdeep."
> — wiki line 71

**Campaign, Doom Raiders Summary**
> "- **Campaign role:** Player faction; the legitimate Black Network cell in Waterdeep, here since 1489 DR and at active war with Manshoon's Zhentarim splinter."
> — `campaign/setting/organizations/06-doom-raiders.md:7`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign Summary: "> - *Shield dwarf moneylender, lawful evil, she/her*. Stat block: **Veteran**." — `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:5`
- Campaign, Dock Ward: "**Istrid Horn (Lawful Evil, Shield Dwarf, she/her)**" — `campaign/gazetteer/waterdeep/dock-ward.md:135`
- Campaign, First Meeting event tag: "> Istrid Horn (Lawful Evil, Shield Dwarf, she/her) :: The Doom Raiders' Master of Trade and Coin, who lends from a guarded Dock Ward warehouse and makes every loan sound like a kindness." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:384`
- Wiki: "| alignment5e    = [[Neutral evil]]" — wiki line 57 (5e). Alignment fields for 2e, 3e, 3.5 and 4e are blank (wiki lines 40, 43, 46, 50, 54).
- Adventure: no alignment in the Istrid entry (`sources/adventure-wdh.json:31930` to `:31937`). The Appendix B Zhentarim paragraph says of the cell: "They are not good, but they are not sadistic, and they can be trusted to honor their agreements." (`sources/Appendix_B_-_Player_Factions.md:508`). That is a description of conduct, not an alignment line.

**Species and ethnicity**
- Campaign Summary: "Shield dwarf" (line 5). Dock Ward (line 135): "Shield Dwarf".
- Wiki: "| race           = [[Dwarf]]<ref name="WDH-199" />" (line 14); "| ethnicity      = [[Shield dwarf]]" (line 15).
- Adventure: "The shield dwarf operates an illegal lending operation" (`sources/adventure-wdh.json:31934`).

**Pronouns**
- Campaign Summary: "she/her" (line 5). Dock Ward (line 135): "she/her". First Meeting tag (ev-01 line 384): "she/her".
- Adventure: "It's clear that Istrid chose a safe, public place for the meeting. Characters who succeed on a {@dc 15} Wisdom (Insight) check can tell that she came alone." (`sources/adventure-wdh.json:6104`); "If the characters decide to let Istrid hide out at their tavern, she uses a disguise kit" (`sources/adventure-wdh.json:6112`, quest-time).
- Wiki: "| sex            = Female<ref name="WDH-199" />" (line 13).

**Stat block**
- Campaign Summary: "Stat block: **Veteran**." (`03-istrid-horn.md:5`). No CR, AC or HP is given anywhere on the page.
- Mechanics reference: "Thug and Veteran do not exist in XMM." (`docs/plans/doom-raiders-mechanics-reference.md:13`); table row: "| Warrior Veteran | Verified (XMM) | CR 3, AC 17, 65 HP. "Veteran" does not exist in XMM. |" (`:252`).
- Factions Guide: "Yagra Stonefist or another Doom Raider serves as muscle (use **veteran** stat block) on one operation per quest." (`campaign/guides/factions/07-doom-raiders.md:58`). This applies to the cell's muscle, not Istrid.
- Adventure: no stat block for Istrid (`sources/adventure-wdh.json:31930` to `:31937`).
- Wiki (5e): "| challenge5e    = 8" (line 58); "| class5e        = {{Class table|edition=5e|[[Cleric]]|9}}" (line 59); refs `WDH-199` (line 60). The wiki's class is Cleric, not a fighter; the Summary's label is not the wiki's.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Shield dwarf moneylender, lawful evil, she/her*. Stat block: **Veteran**." | Day-one name tag; alignment and stat label conflict (B, D1, D2) | `campaign/gazetteer/waterdeep/dock-ward.md:135`; the wiki's alignment differs (wiki line 57) |
| 2 | L6 | "> - **Affiliation:** Zhentarim (Doom Raiders)" | Day-one label; matches the organization H1 and the Notable group folder | `campaign/setting/organizations/06-doom-raiders.md:1` |
| 3 | L7 | "> - **Featured in:** **Trollskull Alley**, **Gralhund Villa**" | Quest list, not lore. Routed (E3) | `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:58`; `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:69` |
| 4 | L11 | "**Resonance.** Istrid should inspire wariness with her warm professionalism (which makes her loans feel reasonable until the penalties arrive), unwilling respect for her business acumen, and discomfort when the party realizes she enjoys having people in her debt." | Day-one trait. The clause "when the party realizes" is party-relative. Restate as what a reader may come to see, without "the party" as the subject | `sources/adventure-wdh.json:31935`; `.claude/skills/character-voices/voices/doom-raiders.md:51` ("Her pleasure in debt shows in how she lingers on the word 'owe'.") |
| 5 | L13 | "**Emotions.** Istrid most often feels shrewd calculation, ledger-balancing satisfaction, predatory patience, devout worship of Vergadain (dwarf god of wealth and luck), cold disdain for poor financial judgment, and possessive pleasure in a growing ledger." | Day-one. Keep (ruling 3). The Vergadain gloss matches `sources/adventure-wdh.json:31935` | `sources/adventure-wdh.json:31935` |
| 6 | L15 | "**Motivations.** Istrid wants to expand her lending operation, keep the Doom Raiders financially solvent, and ensure that every loan she makes returns more than gold: influence, favors, and leverage." | Day-one. Keep. The "more than gold" clause matches the organization page | `campaign/setting/organizations/06-doom-raiders.md:41` ("Istrid wants every loan to return influence, favors and leverage along with the gold") |
| 7 | L17 | "**Inspirations.** When playing Istrid, channel Tywin Lannister (*Game of Thrones*), Miriam Maron (*Ozark*), and Gringotts goblins (*Harry Potter*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Istrid is the Black Network's Master of Trade and Coin, running a lending operation from a guarded Dock Ward warehouse at rates comparable to the Cassalanters'. To those she trusts, she is the Doom Raiders' financial backbone. Deep down, she likes having people indebted to her, and the difference between her interest rates and a legitimate lender's rates is the silence when you miss a payment." | Day-one. "To those she trusts ... financial backbone" is an inference from the funding line (`06-doom-raiders.md:71`) and is kept as the page's own. No quest-time clause | `sources/adventure-wdh.json:31934`; `sources/adventure-wdh.json:31935`; `.claude/skills/character-voices/voices/doom-raiders.md:52` ("The silence after a missed payment is her threat.") |
| 9 | L23 | "**Morale.** In a fight, Istrid would let her enforcers handle it while she secures her ledgers. If cornered, she fights like the veteran adventurer she once was, and the surprise is genuine." | Day-one habit. The first sentence is sourced (`06-doom-raiders.md:74`). The second ("veteran adventurer ... surprise is genuine") has no source. Mark `[research]` or restate | `campaign/setting/organizations/06-doom-raiders.md:74` (quoted in full in E4) |
| 10 | L25 | "**Relationships.** Istrid is the Doom Raiders' Master of Trade and Coin, Emmek Frewn's creditor (150 gp loan with Zhentarim enforcement), and a worshipper of Vergadain whose lending operation funds the cell's operations." | Day-one. The creditor clause is day-one (`dock-ward.md:141`, `north-ward.md:135`). The verb "secures" in the adventure's Emmek entry (`sources/adventure-wdh.json:4264`) sits in a Trollskull plot list. The figure "150 gp" conflicts with the organization page's Settled ruling (D5) | `campaign/gazetteer/waterdeep/dock-ward.md:141`; `campaign/setting/organizations/06-doom-raiders.md:71` |
| 11 | L29 | "A shield dwarf moneylender running a lending operation from a guarded Dock Ward warehouse — her rates look competitive, her manner is warm, and the terms of a missed payment are not discussed at the table." | Day-one, but 35 words (brief limit 21). Draft a shorter Overview | `sources/adventure-wdh.json:31934`; `campaign/gazetteer/waterdeep/dock-ward.md:136` |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/doom-raiders.md`, "### Istrid Horn", lines 44 to 58)**

- Line 45 (tagline): "*A warm, well-mannered dwarven lender who makes every loan sound reasonable and every missed payment sound like a pity.*" Day-one.
- Line 47 (Sound): "A low, comfortable dwarven contralto, pleasant and grandmotherly, with a faint ledger-room crispness." Day-one.
- Line 48 (Sentence shape): "Measured, complete, businesslike sentences with a pleasant finish. She states terms clearly and repeats them once." Day-one.
- Line 49 (Word choice): "Banker's vocabulary: terms, interest, collateral, "arrangements". She invokes Vergadain in blessings and oaths. She calls debtors "dear" and never uses the word "threat"." Day-one.
- Line 50 (Swearing): "Never in business; the warmth is the weapon. She saves one cold "you stupid shit" for the day someone tries to cheat her." Day-one. The clause "the day someone tries to cheat her" is a general condition, not an event. Keep.
- Line 51 (Personality in speech): "Warm professionalism is the trap. She sounds reasonable until the penalties. She shows disdain for bad financial judgement as gentle disappointment. Her pleasure in debt shows in how she lingers on the word "owe"." Day-one.
- Line 52 (Quirks): "She taps the ledger with one finger when naming a figure. She blesses every signed agreement ("Vergadain smile on it"). She never raises her voice. The silence after a missed payment is her threat." Day-one.
- Line 53 (Signature phrases): ""Vergadain smile on it." / "That's the arrangement, dear." / "I'm sure it won't come to that."" Day-one.
- Line 54 (Never): "She never names a penalty as violence, never forgives a debt, and never discusses her rates in front of other borrowers." Day-one.
- Line 56 (Greeting): ""Come in out of the damp, dear. Sit down. Let's see what we can arrange for you."" Day-one.
- Line 57 (Business): ""Two hundred gold, a tenday's grace, and ten percent each tenday after. Sign here, and Vergadain smile on it."" Day-one. Matches the Dock Ward terms (`dock-ward.md:95`). The Factions Guide and Appendix B carry different limits (D6); the voice line is a sample of speech.
- Line 58 (Under pressure): ""Take the ledgers to the back room, please. I'll handle our guests."" Day-one.

**Quest-time clauses in the profile:** none. Lines 45 to 58 are day-one. Line 57's figure is a sample line and does not describe a loan event.

---

## D. Conflicts

**D1. Alignment**
- Campaign Summary: "> - *Shield dwarf moneylender, lawful evil, she/her*. Stat block: **Veteran**." (`campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:5`)
- Campaign, First Meeting tag: "Istrid Horn (Lawful Evil, Shield Dwarf, she/her)" (`campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:384`)
- Wiki: "| alignment5e    = [[Neutral evil]]" (wiki line 57)
- Adventure: no alignment (`sources/adventure-wdh.json:31930` to `:31937`).
- Higher rank: the campaign (lawful evil, on three campaign lines). The wiki is lowest-ranked. Use lawful evil and list the wiki conflict.

**D2. Stat block**
- Campaign Summary: "Stat block: **Veteran**." (`03-istrid-horn.md:5`)
- Mechanics reference: "Thug and Veteran do not exist in XMM." (`docs/plans/doom-raiders-mechanics-reference.md:13`)
- Wiki: "| challenge5e    = 8" and "| class5e        = {{Class table|edition=5e|[[Cleric]]|9}}" (wiki lines 58 and 59)
- Adventure: no stat block.
- Higher rank: none of the sources gives a block. The Summary's "Veteran" is an unsourced label in a campaign file. The wiki's Cleric 9 and CR 8 are a wiki (lowest-ranked) record. Left to the drafter and the orchestrator; the page should not state a CR.

**D3. Title spelling**
- Adventure: "{@creature Istrid Horn|WDH} (Master of Trade and Coin)" (`sources/adventure-wdh.json:1447`).
- Campaign organization page: "- **Istrid Horn, Master of Trade and Coin:**" (`campaign/setting/organizations/06-doom-raiders.md:58`)
- Wiki: "| titles         = Master of Trade and Coins" (wiki line 7)
- Higher rank: the adventure and the campaign agree on "Coin". The wiki's plural is lowest-ranked.

**D4. The Doom Raiders' start date (campaign against itself)**
- `campaign/setting/organizations/06-doom-raiders.md:19`: "No source dates the Doom Raiders' adventuring career, so the cell's own story begins in the late 1480s."
- `campaign/setting/organizations/06-doom-raiders.md:23`: "- **Late 1400s DR, the Doom Raiders adventure:** Five adventurers, described in the published adventure as unscrupulous, made a trade of plundering the lairs of liches, which some call "dooms" (*Dragon Heist*, 5e; Forgotten Realms Wiki, *Doom Raiders*, 5e)." (the bullet's citations close the quote)
- Adventure: "arrived in the city several years ago" (`sources/Appendix_B_-_Player_Factions.md:506`).
- Higher rank: none settles the year. The organization page's own line 19 says no source dates the career, so line 23 is an inference the page itself marks as unsourced. Left to the orchestrator; the Istrid page should not give a year for her adventuring.

**D5. The Emmek Frewn loan figure**
- Istrid page L25: "(150 gp loan with Zhentarim enforcement)" (`03-istrid-horn.md:25`)
- Campaign Settled ruling: "> - **Settled:** Istrid's loan sizes, the vault share and the 5,000 gp donation are mechanics and are not on this page (ruling 18). See Routed facts. Emmek Frewn's loan is named without its figure for the same reason." (`campaign/setting/organizations/06-doom-raiders.md:166`)
- Campaign, Emmek page: "Emmek is a debtor of Istrid Horn (150 gp loan with interest, enforced by Zhentarim thugs)" (`campaign/setting/notable-figures/trollskull-community/10-emmek-frewn.md:25`)
- Adventure, later sum: "{@creature Emmek Frewn|WDH} (see \"Business Rival: {@creature Emmek Frewn|WDH}\") needs 1,500 gp to pay off a loan with interest." (`sources/adventure-wdh.json:14892`, quest-time)
- Higher rank: the campaign's Settled ruling says loan figures stay off Doom Raiders pages. The Istrid page is not the organization page, so the ruling does not bind it, but the figure is in conflict with the ruling's intent. Left to the user (see E5).

**D6. Istrid's loan limits (mechanics; the page does not state one)**
- Factions Guide: "- Istrid Horn's lending operation is available to faction members at reasonable rates: up to 200 gp at Renown 1, up to 2,500 gp at Renown 10." (`campaign/guides/factions/07-doom-raiders.md:14`)
- Factions Guide, Fang row: "Istrid Horn will offer the character a loan of up to 200 gp at favorable rates, no questions asked." (`campaign/guides/factions/07-doom-raiders.md:56`)
- Dock Ward: "up to 200 gp with 10 percent of the principal added at the end of each tenday" (`campaign/gazetteer/waterdeep/dock-ward.md:95`)
- First Meeting event: "Istrid Horn lends the member up to **200 gp** at 10 percent interest per tenday, one loan at a time." (`campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:330`)
- Trollskull Alley event table: "| Doom Raiders | Istrid Horn's Black Network loan — 400 gp | Party-set repayment; Istrid wants no Watch attention |" (`campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:58`)
- Trollskull Manor guide: "- **Doom Raiders (Davil + Istrid Horn):** Istrid: loan up to 400 gp, no interest, party-set repayment schedule." (`campaign/guides/trollskull-manor/02-operating-costs.md:84`)
- Appendix D: "| **Istrid Horn** *(Doom Raiders)* | Up to 400 gp | Coin, no interest | Party's choice — minimum 20 gp/tenday recommended | 20 tendays at minimum; faster is better, Istrid notices |" (`sources/Appendix_D_-_Running_the_Tavern.md:867`). The organization page's Draft Notes cite line 826, which is the section heading; the figure is on line 867.
- Adventure: "Istrid offers loans of up to 2,500 gp with an interest rate of 10 percent per tenday." (`sources/adventure-wdh.json:1455`)
- Appendix B: "| 1 | **Fang** | Recognized Network member. Istrid Horn will offer the character a loan of up to 200 gp at favorable rates, no questions asked. Access to Doom Raiders' fences: stolen goods sell at 60% value instead of the standard 50%. |" (`sources/Appendix_B_-_Player_Factions.md:668`)
- Higher rank: the Factions Guide (200 gp at Renown 1) outranks the Trollskull guide and Appendix D (400 gp), which the organization page's Draft Notes already call stale (`06-doom-raiders.md:178`). The published 2,500 gp is an adventure figure. The page itself should give no loan figure.

**D7. Her warehouse and the Watch**
- Campaign, Dock Ward: "**Istrid Horn's Warehouse** — Moneylending house" (`campaign/gazetteer/waterdeep/dock-ward.md:93`). Wiki and adventure agree on the Dock Ward (wiki line 73; `sources/adventure-wdh.json:31934`). No conflict.

**D8. The cell's own Watch file (a day-one fact that the page should not overstate)**
- Factions Guide: "The Doom Raiders are criminals running legitimate-fronted businesses in a city where the City Watch already has their file." (`campaign/guides/factions/07-doom-raiders.md:20`)
- Wiki (quest-time): "After [[Davil Starsong]] and other Zhents were captured by the [[City Watch (Waterdeep)|City Watch]] later that year ... Fearing being arrested by the City Watch for her illegal loans, she tried to find a place where she could hide for a time." (wiki line 73)
- Higher rank: the campaign. The Watch's file is on the cell. The wiki's arrest of Davil is a quest event (Gralhund Villa). Istrid's own fear of arrest is a quest-time clause (see G).

**D9. Pronouns source (no conflict; recorded)**
- `campaign/gazetteer/waterdeep/dock-ward.md:254`: "Pronouns for Istrid Horn come from the Doom Raiders First Meeting event, and the others from each page's own prose." The Notable page's own she/her (line 5) and `sources/adventure-wdh.json:6104` agree.

**D10. Rate comparison (consistent; recorded)**
- `campaign/setting/organizations/06-doom-raiders.md:41`: "Her lending is illegal, and the published adventure names the Cassalanters and the Irlingstars as the banking houses whose rates hers match (*Dragon Heist*, 5e)." Consistent with `sources/adventure-wdh.json:31934`.

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale line numbers**
- `campaign/setting/deities/moradin.md:95` and `campaign/setting/deities/waukeen.md:102` cite "`campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md` (lines 14 and 26): Vergadain." `campaign/setting/deities/mammon.md:80` cites "(lines 7, 14 and 26)". In the current file Vergadain is on line 13 (Emotions) and line 25 (Relationships), and line 7 is the "Featured in" line. The deity pages cite one line too high.

**E2. Wiki (lowest rank) against the campaign**
- Wiki line 57 "Neutral evil" against the campaign's lawful evil (D1).
- Wiki line 73 places the Gralhund aftermath in the same paragraph as the 1492 DR lending (quest-time, see C and G).

**E3. Routed quest references (quest-time; the day-one page must not restate them)**
- `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:58`: "| Doom Raiders | Istrid Horn's Black Network loan — 400 gp | Party-set repayment; Istrid wants no Watch attention |"
- `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md`: Istrid's scene and its branches. Lines 11, 61, 69, 71, 136, 137, 154, 164. Quoted here: line 69 "**Istrid Horn**, Doom Raiders Master of Trade and Coin, is a shield dwarf fence and unlicensed moneylender. The Watch's crackdown has her terrified. She has outstanding loans to a half-dozen city officials, documented in a ledger she cannot afford to have found. She wants the party to hide her, or destroy the ledger, for a tenday while she makes arrangements to relocate to Baldur's Gate." Line 136: "> - **Istrid Horn Helped** — mark when the party shelters Istrid Horn; read by **Faction Outposts** for the Doom Raiders renown modifier and courier cache availability." Line 137: "> - **Istrid Horn Turned In** — mark when the party hands her to the Watch; read by **Faction Outposts** for the Watch relation modifier and the Doom Raiders renown penalty."
- `campaign/quests/act-ii/gralhund-villa/overview.md:31`, `flowchart.md:64` and `:111`, `design-notes.md:59`: the same scene and its Event Outcomes.
- `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md` (16 hits; the Istrid lines are 11, 172, 252, 282, 306, 314, 330, 346, 368, 384, 386, 396, 400). Quest-time: the new-member loan and the warehouse visit. Line 386 is quoted in G.
- `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md` (17 hits), `m03-the-missing-snobeedle/overview.md` (6), `r25-ardragon/ev-01-ardragon.md` (15), `r50-dread-lord/ev-01-dread-lord.md` (29), `r03-wolf/ev-01-wolf.md` (15), `r10-viper/ev-01-viper.md` (5), `s01-davils-arrest/ev-01-davils-arrest.md` (9): Istrid is named in these (counts from Grep for Istrid, Skeemo or Weirdbottle together). Not read in full for this pass.
- `campaign/quests/faction-events/doom-raiders/m02-the-poisoned-delivery/ev-01-the-poisoned-delivery.md` (42 hits for Skeemo, Istrid or Weirdbottle together). Only Skeemo lines were pulled for this pass; no Istrid line was read.
- `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md` (48 hits for Skeemo, Istrid or Weirdbottle together). The Grep for those three names returned no Istrid line from this file, only Skeemo lines.
- `campaign/guides/factions/07-doom-raiders.md:14` and `:56` (mechanics, see D6). `:33` (Vault: "At Dread Lord renown: Davil proposes a 10% split ...") does not name Istrid.
- `campaign/gazetteer/waterdeep/dock-ward.md:96`: "- Hook: at 9 a.m. after the First Meeting, Yagra Stonefist leads new Doom Raiders members here. In **The Missing Snobeedle**, the party can bring Dasher's claim to Istrid, and in **Ardragon** a target waits in her cellar."
- `campaign/gazetteer/waterdeep/dock-ward.md:137`: "- Hook: a new Doom Raiders member can borrow from her the morning after the First Meeting. If a payment is missed, two of her collectors call that evening, speak plainly and leave without hurting anyone, and her manner cools until the debt is paid."
- `sources/adventure-wdh.json:6080` to `:6125` (Gralhund aftermath: the message, the meeting, "Hiding Istrid", "Harming Istrid"). Quest-time. The "Hiding Istrid" paragraph has her "uses a disguise kit to make herself up to be a male dwarf named Jorn" (`:6112`).
- `sources/adventure-wdh.json:4264` (Trollskull "Plans", page 42) and `:14892` (later money list; quest-time, see D5).
- `campaign/setting/organizations/06-doom-raiders.md:191` (Routed to quests: "Istrid's note and hideout request after the Watch's crackdown (`adventure-wdh.json` lines 6080-6113, `southern-ward.md` line 8)").

**E4. The Doom Raiders organization page, Fighting bullet (the one sourced Morale line)**
> "- **Fighting:** Each Master has a habit in a fight. Davil negotiates first, fights with a swashbuckler's precision second and retreats to protect the cell's leadership third. Istrid lets her enforcers fight while she secures her ledgers. Tashlyn closes distance and stays there, Ziraj fires from elevation and avoids melee, and Yagra fights with her pride (**Davil Starsong**; **Istrid Horn**; **Tashlyn Yafeera**; **Ziraj the Hunter**; **Yagra Stonefist**). The City Watch has heard of a hulking figure on the rooftops whose long black arrows kill from a distance (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/06-doom-raiders.md:74`

**E5. Campaign ruling that the page should not contradict**
> "> - **Settled:** Istrid's loan sizes, the vault share and the 5,000 gp donation are mechanics and are not on this page (ruling 18). See Routed facts. Emmek Frewn's loan is named without its figure for the same reason."
> — `campaign/setting/organizations/06-doom-raiders.md:166` (see D5)

---

## F. Gaps a Background would need that no source gives

Each gap gives what the sources say and what a drafter must stay consistent with. Invented material carries `[design]` and must be listed in the Draft Notes.

**F1. Birthplace, birth year, age, parents, siblings, spouse, children.** Nothing. Wiki infobox fields are blank (wiki lines 17 to 32). Stay consistent with "shield dwarf" (`sources/adventure-wdh.json:31934`) and a Waterdeep home (wiki line 11).

**F2. Her adventuring life before the Zhentarim.** Sources give: she was "once an adventurer" with companions (wiki line 71); the party's specialty was "plundering lich lairs" (`sources/adventure-wdh.json:1446`); the cell's five leaders are the Masters (`sources/adventure-wdh.json:1447`). The organization page says "The five gave up adventuring and joined the reformed Black Network" (`campaign/setting/organizations/06-doom-raiders.md:24`). Skeemo is named as a companion in the wiki (wiki line 71). Nothing gives her role in the party (fighter, cleric or other), her renown, or the companions' names beyond the five Masters. The drafter should not name a companion outside those five. The wiki's Cleric 9 (wiki line 59) is a stat record, not a statement of her role in the adventure.

**F3. How she rose to Master of Trade and Coin.** Nothing. The wiki says she "employed many thugs and enforcers" as the Master (wiki line 68). Stay consistent with "Istrid lends from her warehouse" (`campaign/setting/organizations/06-doom-raiders.md:64`) and with the title in the adventure (`sources/adventure-wdh.json:1447`).

**F4. Family, love, friends outside the cell.** Nothing. The adventure's only personal line is "She likes having others indebted to her" (`sources/adventure-wdh.json:31935`). Stay consistent with: no spouse and no children (wiki infobox blank).

**F5. Her personal goals beyond the business.** Sources give only faction-tied wants: "Istrid wants to expand her lending operation, keep the Doom Raiders financially solvent..." (L15, verbatim) and "Istrid wants every loan to return influence, favors and leverage along with the gold" (`campaign/setting/organizations/06-doom-raiders.md:41`). The Gralhund aftermath's "relocate to Baldur's Gate" (`campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:69`) is a quest-time plan. It must not become a day-one fact, though a `[design]` goal may point in that direction without naming the city plan. Any personal goal must not change the Gralhund outcome.

**F6. Her fear of the Watch.** The cell's file is day-one: "the City Watch already has their file" (`campaign/guides/factions/07-doom-raiders.md:20`). Istrid's own fear of arrest is quest-time (`sources/adventure-wdh.json:6105`, quoted in G). A day-one fear of the Watch that comes from her illegal lending is consistent with the lending being illegal ("Her lending is illegal", `campaign/setting/organizations/06-doom-raiders.md:41`). Any stronger fear must be `[design]`.

**F7. The ledger's contents.** Day-one: "Istrid's ledger" (`campaign/gazetteer/waterdeep/dock-ward.md:94`) with entries on borrowers and their associates (`campaign/guides/gm-guide/debts-of-the-city.md:31`). The officials on her ledger ("outstanding loans to a half-dozen city officials", `ev-09-aftermath.md:69`) are quest-time and must not be given as day-one facts.

**F8. Her relationship with Skeemo.** No source gives one. Both are Masters (`sources/adventure-wdh.json:1447`). Stay consistent with the Skeemo Secret: Davil was fond of Skeemo, and Istrid is not named in it (`campaign/setting/organizations/06-doom-raiders.md:120`).

**F9. Her faith beyond Vergadain.** No deity page exists (E1, A6). Stay consistent with the blessing "Vergadain smile on it" as her only sourced rite (`campaign/setting/organizations/06-doom-raiders.md:43`).

**F10. Her appearance.** Quest-time only: "At the foot of the statue stands a female dwarf clad in plate armor." (`sources/adventure-wdh.json:6101`). Day-one appearance is open. Any description is `[design]`.

**F11. Her morale when cornered.** The page's second Morale sentence has no source (L23, C row 9). Keep `[research]`.

**F12. Who she answers to.** The organization page: "No source says whom the five Masters answer to." (`campaign/setting/organizations/06-doom-raiders.md:55`). Her superior is unsourced.

---

## G. Source facts that hint at the figure's inner life

Each quote is exact. Quest-time items are marked and must be restated or left out of the day-one Background.

- **Loves:** "Istrid loved having people indebted to her. She was competitive with her peers when it came to the more legitimate aspects of her business operations, but extremely ruthless when it came time for collection." — wiki line 65 (`WDH-199`)
- **Loves:** "She likes having others indebted to her, and she employs thugs and enforcers to collect on her loans." — `sources/adventure-wdh.json:31935`
- **Pleasure in debt:** "Her pleasure in debt shows in how she lingers on the word "owe"." — `.claude/skills/character-voices/voices/doom-raiders.md:51`
- **Never forgives:** "She never names a penalty as violence, never forgives a debt, and never discusses her rates in front of other borrowers." — `.claude/skills/character-voices/voices/doom-raiders.md:54`
- **A cold line:** "She saves one cold "you stupid shit" for the day someone tries to cheat her." — `.claude/skills/character-voices/voices/doom-raiders.md:50`
- **The silence as threat:** "The silence after a missed payment is her threat." — `.claude/skills/character-voices/voices/doom-raiders.md:52`
- **Faith:** "Istrid worships Vergadain, the dwarf god of wealth and luck, and blesses each signed agreement with "Vergadain smile on it"." — `campaign/setting/organizations/06-doom-raiders.md:43`
- **Wants:** "Istrid wants every loan to return influence, favors and leverage along with the gold (**Istrid Horn**)." — `campaign/setting/organizations/06-doom-raiders.md:41`
- **Loyalty of the cell to her:** "Anyone who betrays or harms Istrid Horn finds her former adventuring companions using every resource they have to ruin them." — `campaign/setting/organizations/06-doom-raiders.md:37`
- **Ledger habit:** "She taps the ledger with one finger when naming a figure." — `.claude/skills/character-voices/voices/doom-raiders.md:52`
- **Warmth that is real:** "Istrid is Friendly toward new members, and the warmth is real, though she also likes having people in her debt." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:386` (quest-event note on her manner toward new members; the trait is usable)
- **Judgement of others:** "She shows disdain for bad financial judgement as gentle disappointment." — `.claude/skills/character-voices/voices/doom-raiders.md:51`
- **Watches debtors:** "She has been forwarding summaries of the debt relationship to Davil Starsong. Not as a threat. A professional like Istrid simply reads people from their payment habits, and Davil finds her assessments useful." — `campaign/guides/gm-guide/debts-of-the-city.md:39`
- **Fear (quest-time):** "Istrid fears being arrested by the City Watch." — `sources/adventure-wdh.json:6105`. The sentence continues: "Although she wasn't involved in the matters concerning Gralhund Villa, she is worried that the Watch will uncover her illegal currency-lending operation in the course of its investigations." Quest-time; restate as a `[design]` trait only.
- **Precaution (quest-time):** "As a precaution against being double-crossed, Istrid shared her plan concerning the characters with at least one other member of the Doom Raiders" — `sources/adventure-wdh.json:6123` [the sentence continues: "(see {@adventure appendix B|WDH|12})."]. Quest-time (the Gralhund aftermath); the trait "wary of being double-crossed" can be used as `[design]`.
- **Hiding and disguise (quest-time):** "she uses a disguise kit to make herself up to be a male dwarf named Jorn" — `sources/adventure-wdh.json:6112`. Quest-time.
- **Relies on companions:** "Istrid can call on her old adventuring companions for assistance." — `sources/adventure-wdh.json:31935`
- **Blessing habit:** "She blesses every signed agreement ("Vergadain smile on it")." — `.claude/skills/character-voices/voices/doom-raiders.md:52`
- **Morale line (unsourced):** "If cornered, she fights like the veteran adventurer she once was, and the surprise is genuine." — `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:23`. The sentence is on the page and has no source. The drafter may use it only with `[research]`.

---

## Not found

Searched and not found:
- Birth, age, family, spouse, children, origin town: wiki infobox (wiki lines 17 to 32, blank); `sources/adventure-wdh.json:31930` to `:31937`; `campaign/setting/` and `campaign/gazetteer/`. Grep "Istrid" over `campaign/`, `sources/adventure-wdh.json`, `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md`, `sources/Appendix_D_-_Running_the_Tavern.md` and `sources/SOURCE_GUIDE.md` (no matches in `SOURCE_GUIDE.md`). Parents and family are not in any of them.
- A stat block for Istrid (CR, AC, HP, attacks): none in the campaign files, the adventure JSON or the Appendix B and C markdown.
- How she rose to Master of Trade and Coin: none.
- Her role in the original adventuring party: none beyond "adventurer" (wiki line 71).
- A dealing between Istrid and Skeemo: none. Grep for "Istrid" and "Skeemo" together gives only the Masters list.
- A Vergadain deity page: none (`campaign/setting/deities/` has no `*ergadain*` file; Glob returned nothing).
- Istrid in `campaign/quests/act-i/finding-floon/` and `campaign/quests/act-ii/fireball/`: no matches (a campaign-wide Grep count listed no file in either folder; a folder Grep of `act-ii/fireball` returned no matches).
- Istrid in the Alexandrian PDFs `5. Faction Outposts.pdf`, `11. Lair  Xanathar’s Lair.pdf` and `17. Outpost and Lair Revelation Lists.pdf`: not read (see Method).

## Not readable

- `sources/Other remix files/Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` (exists; the research tools cannot open `.docx`). `SOURCE_GUIDE.md` line 688 maps it to "Davil Starsong characterization, Doom Raider faction dynamics, the Elf Killer mission hook" (the Doom Raiders organization page). It may hold Istrid material. A human should extract it.
- `sources/3. Player Character Factions.pdf` was read as images; the quoted Zhentarim passage (printed p. 25, `sources/3. Player Character Factions.pdf` page 3) needs a `pdftotext -layout` check. The passage was not quoted above; the only Doom Raiders text on that page is the "non-Manshoonian Zhentarim" paragraph, which names neither Istrid nor Skeemo.
- `sources/5. Faction Outposts.pdf`, `sources/11. Lair  Xanathar’s Lair.pdf` and `sources/17. Outpost and Lair Revelation Lists.pdf` were not read for this pass (scoped out, see Method).
