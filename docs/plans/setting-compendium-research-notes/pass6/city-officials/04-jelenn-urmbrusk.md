# Pass 6 research notes: Jelenn Urmbrusk

Page: `campaign/setting/notable-figures/city-officials/04-jelenn-urmbrusk.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Brief ruling 2 sizes a page by role; no source gives her a size class, so the orchestrator decides. She is a Masked Lord under blackmail by a villain.
Organization pages: no organization page lists her as a member. Her Masked Lord office is documented in `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md` (Key Members, GM Notes). Her debt and blackmail sit on `campaign/setting/organizations/09-manshoons-zhentarim.md`. Her Watch link sits on `campaign/setting/organizations/11-open-lords-watch.md`. The Zhentarim Factions Guide page (`campaign/guides/factions/10-manshoons-zhentarim.md`) was not searched for her name.
Voice profile: `.claude/skills/character-voices/voices/city-officials.md` (`### Jelenn Urmbrusk`, lines 61-75)
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-city-officials/04-jelenn-urmbrusk.txt` (quoted as "wiki line N" = that file's lines; infobox refs name `WDH-p162` and `WDH5e-p4`, i.e. Dragon Heist 5e p.162)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines. Where a Grep line was too long to print, I re-read it; the quote says so.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain text (`—` is an em dash). `{@creature ...}` tags are left as written. Page numbers are the `page` field of the entry.
- Alexandrian: `sources/Act_III_Arc_D.md`, and Appendix B, C and D markdown, were searched by Grep: none names Jelenn. `sources/7. Other Response Teams.pdf` (read as images) has no Jelenn. No Alexandrian PDF text was extracted.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.
- Cassalanter secrecy: one adventure line names the Cassalanters as Jelenn's lending rivals (section A6). It names a trade, not a pact. Section D9 lists the campaign pages that keep suspicion only.
- Lolth: no source line for her touches Jelenn. The Bregan D'aerthe rule is not engaged.

## Findings that change how the page is written

1. **The list of five Masked Lords is on the governance page, and Mirt's page has a Secret for it; Jelenn's page has none.** The governance page says "Manshoon keeps a list of five Masked Lords whose identities he knows" and that he "has checked off Corylus and Jelenn as the two he is blackmailing" (`open-lord-and-masked-lords.md:63`). The current Mirt page carries the same fact in a Secret callout (`harpers/01-mirt.md:96`). The Jelenn page does not carry the list (sections A4, D8).
2. **Masked Lord status is GM-only on her page, and the party does not learn her office in the quest.** The Summary says "(Masked Lord)" and the Persona says "To those she trusts, she is a Masked Lord". The Harpers salon tells the GM that she is a Masked Lord and that the party learns "not its cause or her office" (`ev-01-the-salon.md:311`). The governance page says "The name of any Masked Lord before a rank event or a quest scene gives it" is never to be revealed (`open-lord-and-masked-lords.md:70`).
3. **The 10,000 gp loan is a quest request.** It sits in the adventure's "Removing the Gold" section, which follows the recovery of the hoard ("If the characters recover Neverember's hoard and keep it for themselves, word gets out eventually." — `adventure-wdh.json:14886`). The governance page lists the loan under Key Members (`open-lord-and-masked-lords.md:42`). The Jelenn page does not carry it (section C row 11).
4. **Pronoun is "she" in the adventure's own entry and across the campaign.** The adventure's ledger summary uses "he" once (`adventure-wdh.json:30295`). The campaign files record this as a typo (section D1).
5. **The debt's creditor is named three ways.** "Zhentarim" (the adventure, the wiki), "Splinter" (the governance page, the Harpers salon, the Manshoon pages) and "payments" (the adventure's ledger summary). Section D3 and D4.
6. **Overview is 22 words**, over the brief's 21-word limit (`page line 29`).

---

## A. Background facts by theme

### A1. Origin, family, property

**Wiki, infobox (WDH-p162)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]" — wiki line 11
> "| race           = [[Human]]" — wiki line 14
> "| ethnicity      = [[Tethyrian]]" — wiki line 15

**Wiki, categories (WDH-p162 source list)**
> "[[Category:Inhabitants of Urmbrusk Villa]]" — wiki line 85
> "[[Category:Members of the Urmbrusk family]]" — wiki line 96

**Wiki, Sea Ward villa list (CoS.W-p92; a list on the Sea Ward wiki page, not on Jelenn's page)**
> "*[[Urmbrusk Villa]]<ref name="CoS.W-p92" />" — `sources/research/pass3-bundles/sea-ward/wiki.txt:181`

**Adventure, Blackmailed Lords (page 162): the Sea Ward estate**
> "The Thann and Umbrusk families have walled estates in the Sea Ward." — `sources/adventure-wdh.json:30357` (the adventure's spelling "Umbrusk"; see D11)

**Adventure, entry (page 162): family property**
> "Jelenn could have borrowed money from any of a number of nobles in the city or sold off some of the property her family owns in Waterdeep, but doing so would have turned her private financial woes into local gossip." — `sources/adventure-wdh.json:30374`

**Gazetteer, Sea Ward**
> "**Jelenn Urmbrusk (Neutral, Tethyrian Human, she/her)**
> - A proud noblewoman in her fifties who never travels without sixteen guards and has no time for strangers. The Urmbrusk family keeps a walled estate in the Sea Ward."
> — `campaign/gazetteer/waterdeep/sea-ward.md:132-133`

### A2. Career as a moneylender

**Adventure, entry (page 162)**
> "Several bad investments ruined her money-lending business, and most of her reliable customers have turned to other providers such as the Cassalanters." — `sources/adventure-wdh.json:30374`

**Wiki, History (WDH-p162)**
> "In her work as a moneylender, Jelenn had some financial troubles and her customers abandoned her. In desperation and fearing a political scandal, she secretly asked for a large sum of money from the [[Zhentarim]]." — wiki line 71

**Wiki, lead (WDH-p162)**
> "was a moneylender and one of the [[Lords of Waterdeep]] during the late 15{{th}} century [[DR]]." — wiki line 62 (past tense; the wiki gives no seat date)

**Gazetteer, Sea Ward GM note**
> "Jelenn is a Masked Lord. Bad investments ruined her money-lending business, and she borrowed from Manshoon's Zhentarim to avoid gossip. They now blackmail her, and her name is in the Kolat Towers ledger. If the party frees her from them, she grants a special favor." — `campaign/gazetteer/waterdeep/sea-ward.md:138` (the last two sentences are quest-time; see C)

### A3. The debt, the gossip, the choice

**Adventure, entry (page 162): her reason and the Zhentarim terms**
> "Fear of that exposure led her to borrow money from the Zhentarim instead—a decision she has come to regret. The Zhents working for {@creature Manshoon|WDH} promise to keep their relationship secret on the condition that she do everything in her power to further the group's welfare in Waterdeep." — `sources/adventure-wdh.json:30374` (`—` is an em dash: "instead—a decision")

**Wiki, Personality (WDH-p162)**
> "Jelenn was a proud woman and she feared political scandals. If someone truly helped her, she could become a trusted ally, but anyone that tried to menace her attracted her wrath." — wiki line 65

**Governance, Key Members, debt cause**
> "Jelenn's debt to Manshoon's Zhentarim was borrowed to avoid borrowing from rival nobles, and the Splinter now holds it." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:64`

**Harpers salon, GM text**
> "She is a Masked Lord who borrowed from the Zhentarim to avoid borrowing from other nobles, and the Splinter now holds the debt." — `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:311`

### A4. The Masked Lords list and the blackmail

**Governance, GM Notes (what anonymity does not protect)**
> "> - **What anonymity does not protect:** The masks stop a stranger's bribe and do nothing against blackmail by someone who has learned a name. Manshoon keeps a list of five Masked Lords whose identities he knows. They are Mirt, Corylus Thann, Thardouk Starbuckler, Jelenn Urmbrusk and Dorgar Adarbrent, and he has checked off Corylus and Jelenn as the two he is blackmailing." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:63`

**Governance, GM Notes (who holds which Lord)**
> "> - **Who holds which Lord:** Manshoon's cell blackmails Jelenn Urmbrusk and Corylus Thann and forces them to cover up crimes by Manshoon's forces. Jelenn's debt to Manshoon's Zhentarim was borrowed to avoid borrowing from rival nobles, and the Splinter now holds it. Corylus uses crooked Watch veterans against anyone who annoys him and will not accept that he owes the party anything. See **Manshoon's Zhentarim** and **Jelenn Urmbrusk**." — `open-lord-and-masked-lords.md:64`

**Adventure, the ledger (pages 161-162)**
> "Jelenn Urmbrusk, a Waterdavian noble, receives regular payments from the Zhentarim to offset monies he loses in bad investments." — `sources/adventure-wdh.json:30295` (conflict D1, D4)
> "The ledger doesn't reveal that Corylus Thann and Jelenn Urmbrusk are Masked Lords, or that {@creature Manshoon|WDH}'s blackmail of them also forces them to use their influence to cover up or dismiss crimes perpetrated by {@creature Manshoon|WDH}'s forces in Waterdeep. If the authorities obtain the ledger, they round up anyone suspected of having ties to {@creature Manshoon|WDH} or the Zhentarim, which disrupts the wizard's operation (see \"Disrupting {@creature Manshoon|WDH}'s Operation\"). Surprisingly, neither Corylus nor Jelenn is arrested or even questioned." — `sources/adventure-wdh.json:30298`
> "Slipped into the ledger is a piece of paper with a list of names in {@creature Manshoon|WDH}'s handwriting. {@creature Manshoon|WDH} keeps this list of Masked Lords whose identities he knows, with check marks indicating the ones he's blackmailing:" — `sources/adventure-wdh.json:30299`
(The list items, in order: "{@creature Mirt|WDH}", "Corylus Thann √", "Thardouk Starbuckler", "Jelenn Urmbrusk √", "Dorgar Adarbrent" — `sources/adventure-wdh.json:30308-30312`.)

**Governance, Lords history (the pre-campaign state)**
> "- Manshoon's cell holds two Masked Lords through blackmail, and it keeps a ledger of five Lords it has identified: Mirt, Corylus Thann, Jelenn Urmbrusk, Thardouk Starbuckler and Dorgar Adarbrent." — `campaign/setting/history/07-a-city-watching-itself.md:71` (under "The Lords Under Strain")

**History, Ahghairon's Gifts, GM Notes**
> "- Manshoon's cell holds Masked Lords Jelenn Urmbrusk and Corylus Thann through blackmail. House Gralhund joined the Zhentarim in order to learn the identities and weaknesses of the Masked Lords, and Yalah Gralhund wants a seat for herself. See **Manshoon**, **Jelenn Urmbrusk** and **Yalah Gralhund**." — `campaign/setting/history/01-ahghairons-gifts.md:86`

**History, The Founding of Chains, Manshoon's aims**
> "- His aims in Waterdeep are to control the underworld, to bribe and blackmail the Masked Lords, and to take the Stone of Golorr for the Weave knowledge inside it. Two Masked Lords, Corylus Thann and Jelenn Urmbrusk, already vote his way under pressure." — `campaign/setting/history/04-the-founding-of-chains.md:72`

**Manshoon villain page**
> "He blackmails two Masked Lords. Corylus Thann is held over a scandal, and Jelenn Urmbrusk is held through a debt to a Splinter front, and their votes follow his preferences. The ledger documenting these arrangements lies in an arcane-locked drawer in his study, with a list of the Masked Lords whose identities he knows (**Kolat Towers** quest opener; 5e *Waterdeep: Dragon Heist*, which has Jelenn already in debt to him)." — `campaign/setting/villains/manshoon.md:37`

**Manshoon Notable Figures page**
> "- **Jelenn Urmbrusk:** One of the two Masked Lords he blackmails. The other is Corylus Thann." — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:63`

**Organization page, Manshoon's Zhentarim**
> "Corylus Thann is held over a scandal and Jelenn Urmbrusk through a debt to a Splinter front, and Manshoon's forces rely on both of them to cover up the cell's crimes." — `campaign/setting/organizations/09-manshoons-zhentarim.md:40`
> "Two Masked Lords on the Council are compromised, Corylus Thann through scandal and Jelenn Urmbrusk through debt, and they vote Manshoon's way without knowing why their interests have aligned." — `campaign/setting/organizations/09-manshoons-zhentarim.md:67` (the line begins with a bold label; the quote runs from "Two Masked Lords")
> "- **The Open Lord and the Masked Lords (enemy, working from within):** The cell blackmails Corylus Thann and Jelenn Urmbrusk and makes them cover up crimes by its forces, and Manshoon keeps a list of five Masked Lords whose identities he knows (**The Open Lord and the Masked Lords**)." — `09-manshoons-zhentarim.md:92`

**Watch organization page**
> "- **The Masked Lords (superior, uneven):** Any Masked Lord can overturn a magister's ruling (*Dragon Heist*, 5e), and Corylus Thann's veterans show that one Lord can bend part of the Watch to a private purpose. Manshoon's cell blackmails Corylus and Jelenn Urmbrusk (**The Open Lord and the Masked Lords**)." — `campaign/setting/organizations/11-open-lords-watch.md:62`

**Mirt's page, Secret (for comparison; not Jelenn's file)**
> "> - Manshoon keeps Mirt on a list of five Masked Lords whose identities he knows. Corylus Thann and Jelenn Urmbrusk are the two he blackmails, and Mirt is not one of them." — `campaign/setting/notable-figures/harpers/01-mirt.md:96` (inside the `> [!gamemaster]**Secret**` callout at line 91)

### A5. Her days, her guards, her temper

**Adventure, page 162 (routine, guards, and how she handles threats)**
> "When not dealing with her slimy creditors, Jelenn is occupied with Masked Lord business. She has no time for a face-to-face meeting with anyone she doesn't know. Characters can confront her as she comes or goes to and from her villa, but she never travels without sixteen {@creature guard||guards} who form a protective wall around her. If the characters brazenly mention {@creature Manshoon|WDH} or the Zhentarim by name to her, Jelenn demands that they leave her alone or face dire consequences. Jelenn's threat is mostly bluster, since she's not eager to make enemies." — `sources/adventure-wdh.json:30375`

**Wiki, Activities (WDH-p162)**
> "Jelenn was cloistered in her villa or attending her duties as Lord when she was not dealing with her creditors." — wiki line 68

**Adventure, entry opening (page 162)**
> "Jelenn (N female Tethyrian human {@creature noble}) is a proud woman in her fifties who desperately wants to get out of debt." — `sources/adventure-wdh.json:30374`

**Voice profile (Personality, Quirks)**
> "- **Personality in speech:** Wounded pride and desperate anxiety. She dismisses help she needs. Suspicion of strangers shows as questions about who sent them. Terror of Manshoon leaks out as refusal to finish certain sentences." — `.claude/skills/character-voices/voices/city-officials.md:68`
> "- **Quirks:** She signals her guards with two fingers mid-sentence. She checks who is within earshot before any real answer." — `city-officials.md:69`

### A6. Relationships to other named figures

- **Manshoon** (blackmailer): sources in A4 and D3.
- **Corylus Thann** (the other blackmailed Masked Lord): "Corylus (LE male Tethyrian human {@creature noble}) is happy to let other members of his family manage the wine business while he focuses on his duties as a Masked Lord." — `sources/adventure-wdh.json:30364`
- **Mirt** (on the list of five; not blackmailed): "Manshoon keeps Mirt on a list of five Masked Lords whose identities he knows. Corylus Thann and Jelenn Urmbrusk are the two he blackmails, and Mirt is not one of them." — `campaign/setting/notable-figures/harpers/01-mirt.md:96`
- **The Cassalanters** (lending rivals only): "most of her reliable customers have turned to other providers such as the Cassalanters" — `sources/adventure-wdh.json:30374`. No pact and no infernal line. The Watch page keeps "The Cassalanters (neutral, unaware):" (`campaign/setting/organizations/11-open-lords-watch.md:72`), which is the Watch's view, not Jelenn's.
- **The Watch** (Corylus's veterans; Jelenn's cover-up): "Manshoon's cell forces him and Jelenn Urmbrusk to cover up crimes by Manshoon's forces." — `campaign/setting/organizations/11-open-lords-watch.md:102`
- **The Splinter / Manshoon's Zhentarim** (the creditor): sources in A3 and D3.
- **Laeral Silverhand and the other Lords**: no source gives Jelenn a line with Laeral. The Warduke design note says the Lord who is requested "is neither Mirt nor Jelenn Urmbrusk" (`campaign/quests/faction-events/lords-alliance/r25-warduke/design-notes.md:13`).

### A7. Pronunciation

**Adventure, pronunciation table**
> "Jelenn Urmbrusk",
> "juh-LEN URM-brusk"
> — `sources/adventure-wdh.json:161-162`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "> - *Tethyrian human noble, neutral, she/her*. Stat block: **Noble**." — `campaign/setting/notable-figures/city-officials/04-jelenn-urmbrusk.md:5`
- Adventure: "Jelenn (N female Tethyrian human {@creature noble})" — `sources/adventure-wdh.json:30374`
- Wiki: "| alignment5e    = [[Neutral]]" — wiki line 57 (5e)
- Governance: "**Jelenn Urmbrusk** (Neutral, Tethyrian Human, she/her) is a proud noblewoman in her fifties who travels with sixteen guards." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:42`
- Gazetteer: "**Jelenn Urmbrusk (Neutral, Tethyrian Human, she/her)**" — `campaign/gazetteer/waterdeep/sea-ward.md:132`

**Species and ethnicity**
- Summary: "Tethyrian human" — `04-jelenn-urmbrusk.md:5`
- Adventure: "Jelenn (N female Tethyrian human {@creature noble})" — `sources/adventure-wdh.json:30374`. The same adventure's ledger summary says "Jelenn Urmbrusk, a Waterdavian noble" (`:30295`; see D2).
- Wiki: "| race           = [[Human]]" — wiki line 14; "| ethnicity      = [[Tethyrian]]" — wiki line 15.

**Pronouns**
- Summary: "she/her" — `04-jelenn-urmbrusk.md:5`
- Adventure: "Jelenn (N female ...)" — `sources/adventure-wdh.json:30374`; "She has no time for a face-to-face meeting with anyone she doesn't know." — `:30375`
- Adventure, ledger summary: "Jelenn Urmbrusk, a Waterdavian noble, receives regular payments from the Zhentarim to offset monies he loses in bad investments." — `sources/adventure-wdh.json:30295` (the only "he"; see D1)
- Wiki: "| sex            = Female<ref group="note">Jelenn is introduced as "she" and "her" on page 98 of ''[[Waterdeep: Dragon Heist]]'' but page 160 uses the male pronoun "he". This latter, minor reference is viewed as a typographical error.</ref>" — wiki line 13
- Campaign files, all "she/her": `sea-ward.md:132`, `open-lord-and-masked-lords.md:42`, `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:309`
- Pronoun table: "| Jelenn Urmbrusk | city-officials/04-jelenn-urmbrusk.md:5 | she/her |" — `docs/plans/npc-pronouns-table-group-a.md:15`

**Stat block**
- Summary: "Stat block: **Noble**." — `04-jelenn-urmbrusk.md:5`
- Adventure: "{@creature noble}" in the entry's first line (`sources/adventure-wdh.json:30374`). No CR, AC, HP or attacks are given in the entry (`:30374-30376`).
- Wiki: "| challenge5e    = " (blank, line 58); "| class5e        = [[Noble]]" — wiki line 59; "| refs5e         = <ref name="WDH-p162">{{Cite book/Waterdeep: Dragon Heist|162}}</ref>" — wiki line 60.
- Not found: a CR, a 2024 stat-block name or a mechanics line for Jelenn in `docs/plans/`. The hits for "Jelenn" and "Urmbrusk" in `docs/` (E4) carry no stat line.

**Affiliation label**
- Summary: "> - **Affiliation:** City of Waterdeep (Masked Lord)" — `04-jelenn-urmbrusk.md:6`
- Quest journal label: "- **Jelenn Urmbrusk** (City of Waterdeep): a proud noblewoman who travels with sixteen guards and leaves if the Zhentarim come up." — `campaign/quests/faction-events/harpers/m04-a-friends-house/overview.md:54`
- Organization pages: none gives her an affiliation. The governance page's Key Members entry describes her as "a proud noblewoman in her fifties who travels with sixteen guards" (`open-lord-and-masked-lords.md:42`) and carries the Masked Lord status from the adventure ("The published adventure names her a Masked Lord"). "(Masked Lord)" is a role, not an organization. Whether to keep it is the orchestrator's call.

---

## C. Sentences on the current page (and related text) that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/city-officials/04-jelenn-urmbrusk.md`. The page has no Background, Personality or Connections section yet. Each row says where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L7 | "**Featured in:** **Kolat Towers**, **A Friend's House**" | Quest-name list. Routed. | `campaign/structure/arc-i-kolat-towers.md:19` (Jelenn's debt; pending conversion); `campaign/quests/faction-events/harpers/m04-a-friends-house/overview.md:54` |
| 2 | L13 | "**Emotions.** Jelenn most often feels desperate anxiety about debt, wounded pride, bitter regret over her failed investments, suspicious hostility toward strangers, fraying dignity, and private terror of Manshoon's leverage." | Day-one register; keep (brief ruling 3). | `sources/adventure-wdh.json:30374` ("bad investments"; "a decision she has come to regret") |
| 3 | L15 | "**Motivations.** Jelenn wants to escape Manshoon's blackmail, repay her debts without any other noble learning of them, and reclaim the financial independence that her bad investments destroyed." | Day-one (ongoing state). Keep. | `sources/adventure-wdh.json:30374`; `campaign/setting/history/07-a-city-watching-itself.md:71` |
| 4 | L21 | "To those she trusts, she is a Masked Lord who borrowed from the Zhentarim because she feared gossip more than gangsters." | Day-one GM register. The Masked Lord clause is GM-only (Finding 2). | `sources/adventure-wdh.json:30374` ("Fear of that exposure led her to borrow money from the Zhentarim instead"); `open-lord-and-masked-lords.md:64` |
| 5 | L21 | "Deep down, she knows the decision was catastrophic, and Manshoon's blackmail is the price of her pride." | Day-one. "knows the decision was catastrophic" is the Persona's reading of "a decision she has come to regret". | `sources/adventure-wdh.json:30374` |
| 6 | L23 | "In a confrontation, Jelenn would demand the party leave and threaten dire consequences. Her threat is mostly bluster." | Standing response, not a quest event. Keep. | `sources/adventure-wdh.json:30375` ("Jelenn demands that they leave her alone or face dire consequences. Jelenn's threat is mostly bluster") |
| 7 | L23 | "If freed from Manshoon, she grants a Special Favor." | Quest-time. Depends on the party defeating Manshoon. Restate or route. | `sources/adventure-wdh.json:30376` ("If the characters free Jelenn from the yoke of the Black Network by defeating {@creature Manshoon|WDH}, her debt is effectively canceled. In her delight, she grants them a special favor"); `sea-ward.md:138` ("If the party frees her from them, she grants a special favor.") |
| 8 | L23 | "If blackmailed by the party instead, she pretends to cooperate while secretly working against them." | Quest-time. Depends on the party threatening to publish the ledger. Restate or route. The page's wording is a paraphrase. | `sources/adventure-wdh.json:30376` ("if they threaten to go to the press with {@creature Manshoon|WDH}'s ledger in an attempt to blackmail or discredit her, she pretends to go along with them while secretly using her influence as a Masked Lord to make their lives difficult.") |
| 9 | L25 | "a blackmail victim of Manshoon's cell whose name appears on the Kolat Towers blackmail list" | The blackmail is a day-one state (brief ruling 1). The location of the list is a quest discovery (Kolat Towers, E13). "blackmail list" is not the adventure's term (D8). | Day-one state: `open-lord-and-masked-lords.md:63-64`; `history/07-a-city-watching-itself.md:71`. Location and discovery: `sources/adventure-wdh.json:30290` ("Inside is a leather-bound ledger that provides a paper trail implicating {@creature Manshoon|WDH} in two blackmail schemes."), `:30299` (the list in Manshoon's handwriting), `campaign/structure/arc-i-kolat-towers.md:247` ("**The Blackmail Ledger (E13 desk).**") |
| 10 | L29 | "Jelenn Urmbrusk is a proud noblewoman in her fifties who travels with sixteen guards and meets uninvited contact with brisk, dismissive authority." | Public face. Day-one. 22 words (brief limit 21). | `sources/adventure-wdh.json:30374`, `:30375` |
| 11 | Voice L74 | "If, hypothetically, a lady owed certain people money, what would you want for making that go away quietly?" | A pitch that presumes the party can make the debt go away. Not a quest event by itself. The drafter decides. | `sources/adventure-wdh.json:14896` (the loan request, quest-time; full text below) |
| 12 | Governance L42 (not the page) | "The published adventure names her a Masked Lord and has her ask the party for an interest-free loan of 10,000 gp, in return for her considerable influence with the Lords of Waterdeep." | Quest-time (after the hoard is recovered). Not for the Jelenn page. | `sources/adventure-wdh.json:14888` ("Laeral Silverhand is prepared to let the characters keep one-tenth of the treasure (50,000 gp) for themselves."); `:14896` (full loan text, below) |
| 13 | Sea-ward L138 (not the page) | "If the party frees her from them, she grants a special favor." | Quest-time. | `sources/adventure-wdh.json:30376` |
| 14 | Salon GM text (not the page) | "Any character who studies her and makes a successful DC 18 Wisdom (Insight) check sees real strain behind the composure, though not its cause or her office." | Quest-time (Harpers event). | `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:311` |
| 15 | Bregan quest (not the page) | "| Jelenn Urmbrusk, or a noble house | Jelenn Urmbrusk | A closed carriage in the Sea Ward, on a drive of fifteen minutes |" | Quest-time (the Commander's audience). | `campaign/quests/faction-events/bregan-daerthe/r25-commander/ev-01-commander.md:161` |

**Adventure loan text (quest-time; the governance page's source)**
> "Jelenn Urmbrusk, a Masked Lord in debt to {@creature Manshoon|WDH}, requests an interest-free loan of 10,000 gp, which she vows to repay within a year. In exchange, she promises to use her \"considerable influence with the Lords of Waterdeep\" to help them in the future. If the characters oblige, she makes good on her promise to pay them back and grants them a special favor (see \"Marks of Prestige\" in chapter 7 of the {@book Dungeon Master's Guide|dmg}). If they refuse, they will have made an enemy of the secret Masked Lord." — `sources/adventure-wdh.json:14896` (under "Removing the Gold", page 98, after "{@creature Laeral Silverhand|WDH} is prepared to let the characters keep one-tenth of the treasure (50,000 gp) for themselves." at `:14888`)

**Routed quest references (quest-time)**
- `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:309` ("> Jelenn Urmbrusk (Neutral, Tethyrian Human, she/her) :: a proud noblewoman in her fifties whose sixteen guards wait outside."), `:311`, `:321` ("> Jelenn glances at the people within earshot and sets her cup on the nearest tray."), `:343` ("record what Jelenn did when the Zhentarim came up; read by **The Cell Is Compromised** (the Jelenn query)")
- `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-03-the-confrontation.md:238` ("Jelenn Urmbrusk's reaction to the Zhentarim is the first thing Mirt writes down, and he says only that he will look into it.")
- `campaign/quests/faction-events/harpers/m04-a-friends-house/overview.md:54`
- `campaign/quests/faction-events/harpers/s01-the-cell-is-compromised/ev-01-the-cell-is-compromised.md:89` ("After the salon you told me how Jelenn Urmbrusk reacted when the Zhentarim came up. I sent a query about her through the relay the next morning. Two days later someone coached her on those same questions, and my own man hadn't seen them yet.")
- `campaign/quests/faction-events/bregan-daerthe/r25-commander/ev-01-commander.md:161`, `:326` ("A Lord the company can reach (Mirt, Durnan, Ulkoria Stonemarrow or Jelenn Urmbrusk): record that Lord's name against the member as the **Seat**."); `design-notes.md:37` ("The four reachable Lords are Mirt, Durnan, Ulkoria Stonemarrow and Jelenn Urmbrusk")
- `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:39` and `design-notes.md:13` (the Warduke Lord is "neither Mirt nor Jelenn Urmbrusk")
- `campaign/structure/arc-i-kolat-towers.md:19` and `:247` (Kolat Towers; quest-time Watch and Guild effects)
- `sources/adventure-wdh.json:30290`-`30299` (ledger, E13), `:30357`-`30376` (Blackmailed Lords, quest-time), `:14888`-`14896` (loan, quest-time)

---

## D. Conflicts (quoted both sides, file:line)

**D1. Pronoun ("he" versus "she")**
- "he": "Jelenn Urmbrusk, a Waterdavian noble, receives regular payments from the Zhentarim to offset monies he loses in bad investments." — `sources/adventure-wdh.json:30295`
- "she": "Jelenn (N female Tethyrian human {@creature noble}) is a proud woman in her fifties who desperately wants to get out of debt." — `sources/adventure-wdh.json:30374`
- Wiki note: "Jelenn is introduced as "she" and "her" on page 98 of ''[[Waterdeep: Dragon Heist]]'' but page 160 uses the male pronoun "he". This latter, minor reference is viewed as a typographical error." — wiki line 13
- Campaign: "Jelenn Urmbrusk's sex. Dragon Heist's Masked Lord entry (line 30374) says female, and its summary list (line 30295) says "he". Her Notable Figures page says "she", and the page follows it." — `campaign/gazetteer/waterdeep/sea-ward.md:245`
- Higher-ranked: "she" (the entry, the campaign and the Notable Figures page). Recorded in `docs/plans/setting-compendium-pass3-closeout.md:33`.

**D2. "Waterdavian" versus "Tethyrian" (ethnicity word in the adventure)**
- "a Waterdavian noble" — `sources/adventure-wdh.json:30295` (ledger summary; the same word is used for Corylus at `:30294`)
- "Tethyrian human" — `sources/adventure-wdh.json:30374` (entry)
- Campaign: "Tethyrian Human" (Summary; `open-lord-and-masked-lords.md:42`; `sea-ward.md:132`). "Waterdavian" is a city, not an ethnicity. Brief ruling 5 says to use a Faerûn ethnicity. Higher-ranked: the entry (`:30374`).

**D3. The creditor: Zhentarim, Splinter, or "Manshoon's Zhentarim"**
- Zhentarim: "borrow money from the Zhentarim instead" — `sources/adventure-wdh.json:30374`; "she secretly asked for a large sum of money from the [[Zhentarim]]." — wiki line 71; "a debtor of the Zhentarim" — the Jelenn page, line 25.
- Splinter: "Jelenn Urmbrusk through a debt to a Splinter front" — `campaign/setting/organizations/09-manshoons-zhentarim.md:40`; "and the Splinter now holds it" — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:64`; "and the Splinter now holds the debt" — `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:311`; "Jelenn Urmbrusk is held through a debt to a Splinter front" — `campaign/setting/villains/manshoon.md:37`; "accumulated significant debt to a Splinter front organization" — `campaign/structure/arc-i-kolat-towers.md:19`
- Higher-ranked: the adventure names the Zhentarim (`:30374`). The campaign calls Manshoon's group "Manshoon's Zhentarim" on the organization page and "the Splinter" in its Manshoon pages. The Jelenn page keeps "Zhentarim", as the adventure does. The orchestrator decides whether "Splinter" is the creditor's name.

**D4. Kind of debt: loan or ledger payments**
- "receives regular payments from the Zhentarim to offset monies he loses in bad investments" — `sources/adventure-wdh.json:30295` (ledger summary; a payment stream)
- "borrow money from the Zhentarim instead" — `sources/adventure-wdh.json:30374` (a loan)
- The two describe different arrangements in the same adventure. The campaign's own pages say "debt" (`open-lord-and-masked-lords.md:64`; `manshoon.md:37`).

**D5. "Whose votes"**
- "her votes in the Council of Guildmasters follow Manshoon's preferences without her ever being asked directly" — `campaign/structure/arc-i-kolat-towers.md:19`
- "Two Masked Lords on the Council are compromised, Corylus Thann through scandal and Jelenn Urmbrusk through debt, and they vote Manshoon's way" — `campaign/setting/organizations/09-manshoons-zhentarim.md:67`
- "their votes follow his preferences" — `campaign/setting/villains/manshoon.md:37`
- "Jelenn Urmbrusk's votes in the Council of Guildmasters follow Manshoon's preferences without anyone asking her directly (campaign-only, structure document pending conversion). No other file mentions a Council of Guildmasters." — `campaign/setting/governance-and-guilds/guilds.md:67`
- "Two Masked Lords, Corylus Thann and Jelenn Urmbrusk, already vote his way under pressure." — `campaign/setting/history/04-the-founding-of-chains.md:72`
- The adventure has no "vote" or "Council" line for Jelenn. A Grep of the adventure for `Jelenn|Umbrusk|Council of Guildmasters|Guildmaster` returned only the Jelenn lines (`:161`, `:14896`, `:30295`, `:30298`, `:30299`, `:30311`, `:30357`, `:30370`, `:30374`-`:30376`).
- Higher-ranked: none that settles it. "Council of Guildmasters" appears only in `arc-i-kolat-towers.md:19` (structure, pending conversion) and `guilds.md:67`. The Masked Lords' "Council" (`09-manshoons-zhentarim.md:67`) is a different body. `docs/plans/setting-compendium-pass3-closeout.md:69` records the earlier "his votes" wording of arc-i as stale.

**D6. Date of the blackmail**
- Wiki: "In [[1492 DR]],{{WDH-time}} [[Manshoon]] blackmailed Jelenn and forced her to use her political power to cover the activities of the Zhentarim loyal to Manshoon." — wiki line 73
- Campaign, pre-campaign state: "Manshoon's cell holds Masked Lords Jelenn Urmbrusk and Corylus Thann through blackmail." — `campaign/setting/history/01-ahghairons-gifts.md:86`; "Manshoon's cell holds two Masked Lords through blackmail, and it keeps a ledger of five Lords it has identified" — `campaign/setting/history/07-a-city-watching-itself.md:71`
- Adventure, no date: "Jelenn Urmbrusk, a Masked Lord in debt to {@creature Manshoon|WDH}" — `sources/adventure-wdh.json:14896`
- Higher-ranked: the campaign (`history/07` and `01` are the day-one history pages). The wiki's "1492 DR" is the adventure's year and not a campaign date. The Jelenn page should give the state, not a year.

**D7. Masked Lord office: GM-only or known**
- The adventure: "The ledger doesn't reveal that Corylus Thann and Jelenn Urmbrusk are Masked Lords" — `sources/adventure-wdh.json:30298`; but the list of Masked Lords in the same ledger includes "Jelenn Urmbrusk √" (`:30311`).
- The adventure's Lords entry: "If they refuse, they will have made an enemy of the secret Masked Lord." — `sources/adventure-wdh.json:14896`
- Governance: "The published adventure names her a Masked Lord" (`open-lord-and-masked-lords.md:42`). The Overview rule: "The Overview is what an ordinary Waterdhavian knows, and it names no Masked Lord." (`open-lord-and-masked-lords.md:12`)
- The Jelenn page is consistent with the governance page (GM-only label; the Overview names no office). The Harpers salon hides her office from the party (`ev-01-the-salon.md:311`). The Warduke design note treats her as a named Masked Lord that the requested Lord is not (`lords-alliance/r25-warduke/design-notes.md:13`). These are not conflicting facts; they are a question of who knows.

**D8. "Blackmail list" versus Manshoon's "list of Masked Lords"**
- Jelenn page, Relationships: "whose name appears on the Kolat Towers blackmail list" — `04-jelenn-urmbrusk.md:25`
- Adventure: "{@creature Manshoon|WDH} keeps this list of Masked Lords whose identities he knows, with check marks indicating the ones he's blackmailing" — `sources/adventure-wdh.json:30299`
- The list is a list of identities with check marks. It is not a list of blackmail targets alone (five names, two checked).

**D9. Cassalanter line: lending rivals only**
- "most of her reliable customers have turned to other providers such as the Cassalanters" — `sources/adventure-wdh.json:30374`
- Campaign rule (brief ruling 7): "Nobody outside the household and the cult knows about the pact." No campaign file ties the Cassalanters to Jelenn's debt. `campaign/setting/organizations/11-open-lords-watch.md:72` ("The Cassalanters (neutral, unaware):") and `:105` ("Everyone outside the household and the cult only suspects the family").

**D10. "Special Favor" versus "Marks of Prestige"**
- "grants them a special favor (see \"Special Favors\" in chapter 7 of the {@book Dungeon Master's Guide|dmg})" — `sources/adventure-wdh.json:30376`
- "grants them a special favor (see \"Marks of Prestige\" in chapter 7 of the {@book Dungeon Master's Guide|dmg})" — `sources/adventure-wdh.json:14896`
- The adventure gives two DMG names. The campaign uses "Special Favor" (Morale, page L23; `sea-ward.md:138`, "special favor"). Not decided.

**D11. Spelling of the family name**
- "Urmbrusk" — `sources/adventure-wdh.json:161`, `:14896`, `:30295`, `:30311`, `:30370`, `:30374`
- "Umbrusk" — `sources/adventure-wdh.json:30357` ("The Thann and Umbrusk families have walled estates in the Sea Ward.")
- Higher-ranked: "Urmbrusk" (the entry's own name at `:30370` and the page title). The `:30357` spelling is an adventure typo.

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Stale or conflicting lines in other files**
- `docs/plans/setting-compendium-pass3-closeout.md:33`: "Jelenn Urmbrusk's sex: `adventure-wdh.json:30295` ("he") against `:30374` (female)." (resolved in the campaign)
- `docs/plans/setting-compendium-pass3-closeout.md:69`: "`campaign/structure/arc-i-kolat-towers.md:19` writes "his votes" for Jelenn Urmbrusk (she/her) and is the only file naming a Council of Guildmasters." (stale: arc-i:19 now reads "her votes", per `campaign/setting/villains/manshoon.md:135`)
- `campaign/setting/villains/manshoon.md:135`: "`arc-i-kolat-towers.md` line 19 wrote "his votes" for Jelenn Urmbrusk and now says "her votes", as `04-jelenn-urmbrusk.md` and `adventure-wdh.json` line 14896 do (fixed in Session 51)." (the note cites `:14896` for "her"; that line uses "her considerable influence" and "her" for Jelenn, which is consistent)
- `docs/plans/harpers-research/04-m04-m06.md:399` (row C15): "Jelenn: NF "she", Manshoon blackmail; arc-i :19 "his votes… Splinter front organisation"; ledger lists five Masked Lords incl. Mirt (arc-i :247); M4 says she "knows two other blackmailed Lords"." (a research note; its "his votes" quote is stale. Its claim about M4 was not checked.)
- `docs/plans/harpers-research/02-first-meeting-s01-ranks.md:506`: "Jelenn is a Manshoon blackmail victim (`harpers-out-of-scope-notes.md:150`) and appears at L5." (consistent)

**E2. The Lords' Alliance mechanics reference (exclusion of Jelenn from casual introduction)**
- `docs/plans/lords-alliance-mechanics-reference.md:324`: "**Jelenn Urmbrusk is excluded** on purpose: her page makes her a Masked Lord under blackmail, so she cannot be a casual introduction." (consistent)
- `docs/plans/lords-alliance-mechanics-reference.md:382`: "not **Jelenn Urmbrusk** (her page makes her a Masked Lord under blackmail)" (consistent)
- `docs/plans/lords-alliance-research/05-consistency-audit.md:418`: "Kolat Towers' ledger names five Masked Lords (`arc-i:247`)" (consistent)

**E3. Routed Kolat Towers references**
- `campaign/structure/arc-i-kolat-towers.md:19` and `:247` (quoted in D5 and C).
- `campaign/gazetteer/waterdeep/sea-ward.md:138` ("her name is in the Kolat Towers ledger"), consistent with `open-lord-and-masked-lords.md:63`.

**E4. Other docs that mention her (no stat line)**
- `docs/plans/harpers-conversion-brief.md:269`: "**Jelenn Urmbrusk** ("she"; a Masked Lord being blackmailed; she leaves within 3 minutes if the Zhentarim come up; DC 18 Wisdom (Insight))."
- `docs/plans/harpers-research/05-consistency-audit.md:77`: "M4 `ev-01`: a BD helper present, and Jelenn Urmbrusk's response."
- `docs/plans/faerun-ethnicities-research.md:341`: "| Jelenn Urmbrusk | 30374 | `(N female Tethyrian human {@creature noble})` | campaign/setting/notable-figures/city-officials/04-jelenn-urmbrusk.md:6 ... agrees"
- `docs/plans/setting-compendium-pass6-pilot-mirt-final.md:94`: "Manshoon keeps Mirt on a list of five Masked Lords whose identities he knows. Corylus Thann and Jelenn Urmbrusk are the two he blackmails, and Mirt is not one of them."

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes (brief ruling 17).

1. **Origin and birth.** No source gives a birth year, parents, siblings, spouse or children. Infobox fields are blank (wiki lines 17, 21, 29-32). Stay consistent with "a proud woman in her fifties" (`sources/adventure-wdh.json:30374`), Tethyrian (wiki line 15; `:30374`) and the Urmbrusk family with a walled Sea Ward estate (`sea-ward.md:133`; `:30357`).
2. **How she became a Lord.** No source. The wiki says she was "one of the Lords of Waterdeep during the late 15th century DR" (wiki line 62). The governance page marks the Open Lord's power to choose new Lords as "[research]" (`open-lord-and-masked-lords.md:24`). Several Masked Lords were assassinated "some years ago" (`open-lord-and-masked-lords.md:33`), and the Alexandrian files date the Lord Murders to 1491 DR (`campaign/setting/history/07-a-city-watching-itself.md:70`). The page must not give a seat date or the way she was chosen. A `[design]` seat date must not name a murdered Lord.
3. **Her moneylending career.** Sources: "Several bad investments ruined her money-lending business" (`:30374`) and "her customers abandoned her" (wiki line 71). No investment is named, no sum given, no start date. Stay consistent with "most of her reliable customers have turned to other providers such as the Cassalanters" (`:30374`).
4. **The size and terms of the debt.** Sources give none before the campaign. The 10,000 gp loan (`:14896`) is a quest request and belongs after the hoard is recovered. Do not give a debt figure on day one.
5. **The property she could sell.** "sold off some of the property her family owns in Waterdeep" (`:30374`). No property is named.
6. **Faith.** None. No deity line in any source for her.
7. **Belongings and home interior.** "her villa" (`:30375`; wiki line 68). No room or object is named.
8. **Relationships with the other Lords.** Only the list (`:30299`) and the blackmail (`open-lord-and-masked-lords.md:63-64`). No source gives a conversation or alliance with Mirt, Laeral, Durnan or Ulkoria.
9. **Her guards.** "sixteen guards" (`:30375`; `sea-ward.md:133`). No names.
10. **Personal goals.** The page's Motivations (L15) already give: "repay her debts without any other noble learning of them, and reclaim the financial independence that her bad investments destroyed." Brief ruling 17 needs one to three personal wants beyond these: `[design]`. They must sit with the Motivations and the 10,000 gp loan being a quest event.
11. **Her fear of gossip as a life pattern.** "she feared political scandals" (wiki line 65) and "Fear of that exposure led her to borrow money from the Zhentarim instead" (`:30374`). Keep as the cause; a second scandal would be invented.

---

## G. Source facts that hint at the figure's inner life (quote exactly; do not contradict)

- Emotions, page L13: "**Emotions.** Jelenn most often feels desperate anxiety about debt, wounded pride, bitter regret over her failed investments, suspicious hostility toward strangers, fraying dignity, and private terror of Manshoon's leverage." — `campaign/setting/notable-figures/city-officials/04-jelenn-urmbrusk.md:13`
- Motivations, page L15: "**Motivations.** Jelenn wants to escape Manshoon's blackmail, repay her debts without any other noble learning of them, and reclaim the financial independence that her bad investments destroyed." — `04-jelenn-urmbrusk.md:15`
- Persona, page L21: "Deep down, she knows the decision was catastrophic, and Manshoon's blackmail is the price of her pride." — `04-jelenn-urmbrusk.md:21`
- Adventure: "Jelenn (N female Tethyrian human {@creature noble}) is a proud woman in her fifties who desperately wants to get out of debt." — `sources/adventure-wdh.json:30374`
- Adventure: "Fear of that exposure led her to borrow money from the Zhentarim instead—a decision she has come to regret." — `sources/adventure-wdh.json:30374` (`—` is an em dash)
- Adventure: "Several bad investments ruined her money-lending business, and most of her reliable customers have turned to other providers such as the Cassalanters." — `sources/adventure-wdh.json:30374`
- Adventure: "When not dealing with her slimy creditors, Jelenn is occupied with Masked Lord business." — `sources/adventure-wdh.json:30375`
- Wiki, Personality: "Jelenn was a proud woman and she feared political scandals." — wiki line 65
- Wiki, History: "In desperation and fearing a political scandal, she secretly asked for a large sum of money from the [[Zhentarim]]." — wiki line 71
- Wiki, Activities: "Jelenn was cloistered in her villa or attending her duties as Lord when she was not dealing with her creditors." — wiki line 68
- Voice, Personality in speech: "Wounded pride and desperate anxiety. She dismisses help she needs. Suspicion of strangers shows as questions about who sent them. Terror of Manshoon leaks out as refusal to finish certain sentences." — `.claude/skills/character-voices/voices/city-officials.md:68`
- Voice, Swearing: "Never in public. When her fear breaks through in private, a hissed \"Damn them. Damn all of them.\"" — `city-officials.md:67`
- Voice, Never: "She never admits the debt, never accepts help on someone else's terms, and never says Manshoon's name." — `city-officials.md:71`
- Voice, tagline: "*A proud, brittle noblewoman whose dismissiveness is the last wall around a terrible debt.*" — `city-officials.md:62`
- Voice, Under pressure: "You don't understand what they can do. You don't — no. My people will see you out." — `city-officials.md:75`

---

## Cross-references (every other file:line where the topic appears)

- `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:42`, `:63`, `:64`, `:67`, `:97`, `:112`
- `campaign/setting/governance-and-guilds/guilds.md:9`, `:67`, `:104`
- `campaign/setting/organizations/09-manshoons-zhentarim.md:40`, `:67`, `:92`, `:131`, `:153`, `:170`
- `campaign/setting/organizations/11-open-lords-watch.md:62`, `:102`, `:139`
- `campaign/setting/villains/manshoon.md:37`, `:116`, `:135`
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:37`, `:63`, `:81`, `:111`, `:148`
- `campaign/setting/notable-figures/harpers/01-mirt.md:96` (Secret)
- `campaign/setting/history/01-ahghairons-gifts.md:86`, `:105`, `:120`
- `campaign/setting/history/04-the-founding-of-chains.md:72`, `:129`, `:166`
- `campaign/setting/history/07-a-city-watching-itself.md:71`, `:113`
- `campaign/gazetteer/waterdeep/sea-ward.md:30`, `:33`, `:132`-`:138`, `:158`, `:161`, `:207`, `:219`, `:226`, `:245`
- `campaign/structure/arc-i-kolat-towers.md:19`, `:247`
- Quest files listed in C
- `sources/adventure-wdh.json:161`-`162`, `:14888`-`14896`, `:30290`-`30299`, `:30311`, `:30357`, `:30364`, `:30370`-`30376`
- `sources/research/pass3-bundles/sea-ward/wiki.txt:181`
- `docs/plans/npc-pronouns-table-group-a.md:15`, `docs/plans/faerun-ethnicities-research.md:341`, `docs/plans/setting-compendium-pass3-closeout.md:33`, `:69`

---

## Not found

- **Birth, parents, siblings, spouse, children, faith, a named home room, names of her guards, a debt figure before the campaign, a seat date, the means by which she became a Lord, a CR or 2024 stat block.** Searched: the wiki extract (all fields), the adventure entry (`:30374-30376`), the Blackmailed Lords block (`:30357`), the Removing the Gold block (`:14886-14896`), the governance pages, the Sea Ward and Castle Ward gazetteer entries, the Lords history pages, the Manshoon pages, the Harpers and Bregan quest folders, and `docs/` (for "Jelenn", "Urmbrusk" and "Umbrusk").
- **"Council" or "votes" in the adventure for Jelenn.** Not found (Grep of the adventure). The only "Council of Guildmasters" lines are `arc-i-kolat-towers.md:19` and `guilds.md:67` (D5).
- **Alexandrian text naming Jelenn.** Not found in `sources/Act_III_Arc_D.md`, the Appendix B, C and D markdown files, or `sources/7. Other Response Teams.pdf` (read as images, pp. 57-61).
- **The Zhentarim Factions Guide line for her.** Not searched. She has no faction page; the organization page is the faction source.

## Not readable

- `sources/Other remix files/` `.docx` files cannot be opened. The NPC overview `The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` (`sources/SOURCE_GUIDE.md:695`) may cover Jelenn and was not read.
- Alexandrian PDFs: text not extracted.
