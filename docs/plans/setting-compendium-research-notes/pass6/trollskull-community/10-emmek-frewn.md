# Pass 6 research notes: Emmek Frewn

Page: `campaign/setting/notable-figures/trollskull-community/10-emmek-frewn.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR.
Organization page: none. Emmek has no organization page. The Doom Raiders page (`campaign/setting/organizations/06-doom-raiders.md`) names him as Istrid Horn's debtor, not a member (see D6). The Shard Shunners are a Field Ward gang with no organization page; they appear as Kelso Fiddlewick's crew in `campaign/gazetteer/waterdeep/field-ward.md`.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 169 to 183.
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines. Quest-file quotes that sit in blockquote are marked "(blockquote)".
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string (escapes shown as plain quotes). `{@creature ...}` tags are left as written.
- Appendix D: `sources/Appendix_D_-_Running_the_Tavern.md`. **Emmek has no entry in Appendix D.** A grep for "Emmek", "Frewn" and "Shard" in that file returned no Emmek entry (the only Appendix D hits are the Ulkoria and Broxley entries, which do not name him).
- Alexandrian PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf`, read with the Read tool's `pages` parameter. The PDF has 38 pages (printed 178 to 215); **all 38 were read.** Every PDF quote is a transcription from the page image. **Check each with `pdftotext -layout` before it goes into prose.** No shell was available.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-trollskull-community/10-emmek-frewn.txt`. Citation key `WDH5e-p42` (Dragon Heist 5e, page 42). The wiki prints no other edition.
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The loan figure is 150 gp in the opening scene and 1,500 gp in the post-Vault epilogue.** The adventure gives 150 gp at `sources/adventure-wdh.json:4264` and 1,500 gp at `:14892`. The campaign uses 150 gp throughout. Quoted in D1.
2. **Most of Emmek's day-one story is in the Alexandrian PDF and the adventure's "Business Rival" entry, not on the page.** The page's Persona (family, Neverwinter, sisters, the pub) is sourced at `sources/adventure-wdh.json:4237` to `:4239`. The PDF adds that Volothamp outbid him at public auction (printed p.181). Quoted in A.
3. **The PDF has no Emmek profile.** Its one mention of an "Emmek Frewn" entry (Ryba, printed p.183, "see 'Emmek Frewn' below") points to an entry that is not in the PDF. See F.
4. **Several page lines are quest-time as written.** Persona "every act of sabotage", Morale "hat in hand" (taken from the post-Vault epilogue), Relationships "client of the Shard Shunners", and Motivations "see the party's establishment fail". See C.
5. **The "insult to joinery" line has no source.** See D5.

---

## A. Background facts by theme

### A1. Origin: Neverwinter, the family and the Trades Ward

**Adventure, Business Rival: Emmek Frewn (page 42)**
> "Emmek's family migrated to Waterdeep after its holdings in Neverwinter were destroyed by the eruption of Mount Hotenow in 1451 DR. The family struggled to make ends meet by tanning leather in the Trades Ward. After Emmek's parents died, his sisters took over the business and bought him out. He never liked the work anyway, and he particularly hated dealing with the League of Skinners and Tanners."
> — `sources/adventure-wdh.json:4238`

**Wiki, History (edition WDH5e-p42)**
> "Frewn's family originated in [[Neverwinter]] but relocated to Waterdeep after the [[Ruining]] of [[1451 DR]]. Frewn's father worked in a tanning business in the [[Waterdeep/Trades Ward|Trades Ward]] of the city. After the death of his parents, Emmek's sister took care of the family business.<ref name=\"WDH5e-p42\" />"
> — `scratchpad/wiki-trollskull-community/10-emmek-frewn.txt:72`

**Wiki, Personality (edition WDH5e-p42)**
> "Emmek always disliked the tanning business. Instead of pursuing the family trade, he used all his money in the development of a new tavern. He was stingy in paying some types of expenses and skimped on amenities, but too free with his money on flashy things.<ref name=\"WDH5e-p42\" />"
> — `scratchpad/wiki-trollskull-community/10-emmek-frewn.txt:66`

**Adventure, Business Rival (page 42), spending**
> "Emmek is stingy when it comes to certain kinds of expenses and foolish with his coin in other ways. He tends to spend a lot on big, showy items and cut corners on the little amenities. Because he doesn't have much coin to throw around right now, his plan to ruin the characters' establishment begins with borrowing some money."
> — `sources/adventure-wdh.json:4255`

**Gazetteer, North Ward, Emmek entry**
> "- Emmek is a refugee from Neverwinter whose sisters bought him out of the family tanning business. He owes **Istrid Horn** a loan of 150 gp, enforced by Zhentarim thugs, and he pays the Shard Shunners, a halfling wererat gang, to sabotage the party."
> — `campaign/gazetteer/waterdeep/north-ward.md:135`

**Gazetteer, North Ward, Emmek entry (identity)**
> "A salty northerner who opened Frewn's Brews a few doors down and talks loudly about how adventurers ruin neighborhoods. He wants his pub to be the most successful tavern in the North Ward and the party's to fail."
> — `campaign/gazetteer/waterdeep/north-ward.md:130`

**Doom Raiders page, Connections**
> "- **Emmek Frewn:** A debtor, a refugee from Neverwinter who runs a pub in the North Ward. Zhentarim enforcers collect what he owes her."
> — `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:46`

### A2. The pub: how he came to own it

**Adventure, Business Rival (page 42)**
> "{@creature Emmek Frewn|WDH}, a salty northerner (NE male Illuskan {@creature commoner}), recently tried to buy the tavern in Trollskull Alley but was outbid by Volothamp Geddarm. Stung by the loss, he bought a smaller, less impressive building in the same alley and turned it into a pub, which he calls Frewn's Brews. If you decide to introduce Emmek as a business rival, choose an unmarked building on map 2.1 to serve as the pub."
> — `sources/adventure-wdh.json:4237`

**Alexandrian PDF, printed p.181 (PDF page 4), history list**
> "Most recently, Emmek Frewn attempted to purchase the property at public auction, only to be outbid by Volothamp Geddarm (who was interested in researching its \"haunted history\" for his next book)."
> — `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF page 4. **Check with pdftotext.**

**Wiki, 1492 DR (edition WDH5e-p42)**
> "In the {{YearlinkName|1492}},{{Waterdeep-time}} Emmek wanted to open a tavern and tried to buy the [[Trollskull Manor]], but was outbid by [[Volothamp Geddarm]]. Instead, he opened a pub nearby in [[Trollskull Alley]] but got into trouble with the [[Carpenters', Roofers' and Plasterers' Guild]] for not asking their assistance and offended a member of the [[Cellarers and Plumbers Guild|Cellarers' and Plumbers' Guild]]. Emmek made it his goal to be the most successful tavern owner in the North Ward and had no scruples when it came to ruining his competitors' businesses.<ref name=\"WDH5e-p42\" />"
> — `scratchpad/wiki-trollskull-community/10-emmek-frewn.txt:74`

**Adventure, Business Rival (page 42), finances**
> "Emmek is on shaky financial footing because he has sunk most of his wealth into this latest endeavor. He's also in trouble with two of the guilds. First, he tried to save coin by fixing the roof himself, in defiance of the Carpenters', Roofers', and Plaisterers' Guild. Then he offended a member of the Cellarers' and Plumbers' Guild by comparing the dwarf's beard to barnacles on a ship."
> — `sources/adventure-wdh.json:4239`

Note: the "trouble with two guilds" is sourced, but the adventure dates it to the business-rival setup, and the wiki dates the same trouble to 1492 DR (`:74`). Both fall on the pre-campaign side of Ches 1.

### A3. The Istrid Horn loan (the figure is in conflict; see D1)

**Adventure, Business Rival (page 42), loan and Shard Shunners**
> "Emmek secures a 150 gp loan from {@creature Istrid Horn|WDH} (see {@adventure appendix B|WDH|12}). He spends 50 gp for the services of the Shard Shunners, a gang of halfling wererats with which he has had nefarious dealings in the past. He pays the halflings to hinder the characters' efforts while he works feverishly to manage his own business."
> — `sources/adventure-wdh.json:4264`

**Adventure, Istrid Horn entry, the lending operation**
> "{@creature Istrid Horn|wdh|Istrid} is regarded as the Black Network's Master of Trade and Coin in Waterdeep. The shield dwarf operates an illegal lending operation out of a heavily guarded warehouse in the Dock Ward, offering loans to those in need of coin. Her interest rates are comparable to those of her competitors (including noble families of bankers such as the Cassalanters and the Irlingstars), but the penalties for not paying back Istrid's loans are severe."
> — `sources/adventure-wdh.json:31934`

Note: the adventure gives no interest rate for Emmek's loan. Campaign-only interest figure is in D3.

**Wiki, Relationship (edition WDH5e-p42)**
> "Emmek hated dealing with the [[League of Skinners and Tanners]]. In the past, he had had dealings with the [[Shard Shunners]], a gang of [[halfling]] [[wererat]]s.<ref name=\"WDH5e-p42\" />"
> — `scratchpad/wiki-trollskull-community/10-emmek-frewn.txt:69`

### A4. Money, pride and the sister's buy-out (inner life, see G)

**Adventure, Goals (page 42)**
> "Emmek wants his pub to be the most successful tavern in the North Ward, and he wants the characters' business to fail spectacularly."
> — `sources/adventure-wdh.json:4246`

**Voice profile, Emmek's inner life (quotes below are in G)**

### A5. The Shard Shunners in his service

**Adventure, page 42, the gang**
> "Four gang members have been assigned to work with Emmek: two males named {@creature Shard Shunner|wdh|Kelso Fiddlewick} and {@creature Shard Shunner|wdh|Dasher Snobeedle}, and two females named {@creature Shard Shunner|wdh|Danika Fiddlewick} (Kelso's younger sister) and {@creature Shard Shunner|wdh|Brynn Hilltopple}. These halflings are {@creature wererat||wererats}, with these changes:"
> — `sources/adventure-wdh.json:4265`

**Field Ward gazetteer**
> "Kelso Fiddlewick, who leads the Shard Shunners from this ward, is Emmek Frewn's contractor against the party's tavern, and his crew shows in the alley in **The Neighbors** and **The Twin Parades**."
> — `campaign/gazetteer/waterdeep/field-ward.md:8`

### A6. Time in post and the pub's place on day one

- The adventure has the pub open when the party arrives? Not stated. The adventure says "Frewn's Brews" was built after the outbidding (`sources/adventure-wdh.json:4237`), and gives no date.
- Quest file, ev-01 (blockquote, arrival): "**Frewn's Brews** — at the far end of the alley, a pub under a fresh sign with new paint and modest foot traffic at this hour. The name is not Trollskull Manor." — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:31`. This is quest-time (the party's arrival) and conflicts with "a few doors down" (D4).
- Wiki lists it as a North Ward pub: "* [[Frewn's Brews]]<ref name=\"WDH5e-p42\" />" — `sources/research/pass3-bundles/north-ward/wiki.txt:122`.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "> - *Illuskan human tavern owner, neutral evil, he/him*. Stat block: **Commoner**." — `campaign/setting/notable-figures/trollskull-community/10-emmek-frewn.md:5`
- Adventure: "NE male Illuskan {@creature commoner}" — `sources/adventure-wdh.json:4237`
- Wiki: "| alignment5e    = [[Neutral evil]]" — `scratchpad/wiki-trollskull-community/10-emmek-frewn.txt:58`
- Campaign: `campaign/setting/governance-and-guilds/guilds.md:52` gives "Emmek Frewn** (Neutral Evil, Illuskan Human, he/him)".
- All sources agree: neutral evil.

**Species**
- Summary: "*Illuskan human tavern owner, neutral evil, he/him*" (`10-emmek-frewn.md:5`)
- Adventure: "NE male Illuskan {@creature commoner}" (`sources/adventure-wdh.json:4237`)
- Wiki: "| race           = [[Human]]" (line 14) and "| ethnicity      = [[Illuskan]]" (line 15)
- All sources agree: Illuskan human.

**Pronouns**
- Summary: "he/him" (`10-emmek-frewn.md:5`)
- Adventure: "NE male" (`sources/adventure-wdh.json:4237`)
- Wiki: "| sex            = Male" (line 13)
- All sources agree: he/him.

**Stat block**
- Summary: "Stat block: **Commoner**." (`10-emmek-frewn.md:5`)
- Adventure: "NE male Illuskan {@creature commoner}" (`sources/adventure-wdh.json:4237`)
- Wiki: "| class5e        = [[Commoner]]" (line 60)

---

## C. Sentences on the current page that narrate a quest-time event or a day-one conflict

Current page: `campaign/setting/notable-figures/trollskull-community/10-emmek-frewn.md`. Sections: Gamemaster's Summary, Roleplaying Information, Character Information (Persona, Morale, Relationships), Overview. No Background yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L6 | "> - **Affiliation:** Trollskull Alley community" | Label. See D6 | No organization page. See D6 |
| 2 | L7 | "> - **Featured in:** **Trollskull Alley**" | Quest list. Incomplete (E3) | `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:11` and `:24`; `ev-03-the-neighbors.md:31`; `ev-07-the-twin-parades.md:77` |
| 3 | L11 | "**Resonance.** Emmek should inspire irritation with his petty sabotage, sympathy with his refugee background and financial desperation, and discomfort when the party realizes punishing him too harshly would destroy a man who has already lost everything once." | "petty sabotage" and "the party realizes" are quest-time. The refugee background and desperation are day-one. Drafter restates the first and last clause (ruling 1) | Sabotage: `ev-02-the-guild-gauntlet.md:11`; refugee: `north-ward.md:135`; "lost everything once": voice line 183 |
| 4 | L13 | "**Emotions.** Emmek most often feels bitter resentment, desperate anxiety about money, vindictive satisfaction at small victories, wounded pride, stubborn refusal to admit defeat, and shame he converts to anger." | "vindictive satisfaction at small victories" is a reaction to the sabotage. Borderline. Keep the rest | `sources/adventure-wdh.json:4239` ("sunk most of his wealth") |
| 5 | L15 | "**Motivations.** Emmek wants to make Frewn's Brews the most successful tavern in the North Ward, see the party's establishment fail spectacularly, and never be bought out or displaced again the way his sisters bought him out of the tanning business." | "see the party's establishment fail spectacularly" is the adventure's goal: "he wants the characters' business to fail spectacularly" (`sources/adventure-wdh.json:4246`). Keep the motive; restate "the party" (ruling 3). "his sisters bought him out" is day-one | `sources/adventure-wdh.json:4246`, `:4238` |
| 6 | L21 | "**Persona.** To the world, Emmek is a salty northerner who opened a competing pub and talks too loudly about how adventurers ruin neighborhoods." | Day-one. "opened a competing pub" is day-one (`sources/adventure-wdh.json:4237`). The competing is the adventure's own word | `sources/adventure-wdh.json:4237` |
| 7 | L21 | "To those he trusts, he is a Neverwinter refugee whose family fled Mount Hotenow's eruption, whose sisters pushed him out of the family business, and who sank most of his remaining wealth into a pub he cannot afford to lose." | Day-one backstory. "pushed him out" is campaign phrasing; the adventure says "bought him out" (`:4238`). "a pub he cannot afford to lose" is campaign (`campaign/quests/act-i/trollskull-alley/design-notes.md:25`: "staking everything on a pub he cannot afford to lose.") | `sources/adventure-wdh.json:4238`, `:4239` |
| 8 | L21 | "Deep down, he knows Frewn's Brews is worse than the party's tavern, and that knowledge drives every act of sabotage." | Day-one belief ("worse than"): `campaign/gazetteer/waterdeep/north-ward.md:136` ("He knows his pub is worse than the party's"). "every act of sabotage" is quest-time framing. Drafter restates (ruling 1) | `north-ward.md:136`; sabotage: `ev-02-the-guild-gauntlet.md:24` |
| 9 | L23 | "**Morale.** In a fight, Emmek would lock his door and hide behind the bar. If the party comes to him with hat in hand, he will deny wrongdoing even while accepting help." | "the party comes to him with hat in hand" is quest-time: the adventure's Adventure Conclusion scene (post-Vault). Route (see row 9b) | `sources/adventure-wdh.json:14892` |
| 9b | — | "Emmek comes to the characters with hat in hand, preying on their generosity while denying any wrongdoing on his part." | Post-Vault epilogue, quest-time. The "hat in hand" wording is the source of Morale line 23 | `sources/adventure-wdh.json:14892` (Vault of Dragons, "Removing the Gold", page 98) |
| 10 | L25 | "**Relationships.** Emmek is a debtor of Istrid Horn (150 gp loan with interest, enforced by Zhentarim thugs), a client of the Shard Shunners (halfling wererat gang he pays to sabotage the party), and a reluctant neighbor of Tally Fellbranch (who thinks Emmek's pub sign is \"an insult to joinery\")." | (a) Debtor of Istrid: sourced at `sources/adventure-wdh.json:4264` (150 gp). "with interest" is campaign (`m03 ev-01:427` says "at ten percent each tenday"; D3). "enforced by Zhentarim thugs" is from the post-Vault epilogue (`:14892`), not the loan entry (D2). (b) "a client of the Shard Shunners ... to sabotage the party" is quest-time: the sabotage is the quest's Stage 1–4 escalation. (c) "reluctant neighbor of Tally Fellbranch" is campaign; the quote "an insult to joinery" is **unsourced** (D5) | Loan: `:4264`. Sabotage: `ev-02-the-guild-gauntlet.md:11`; `north-ward.md:135`. Tally: `01-talisolvanar-fellbranch.md:25` (the Tally page's own line about Emmek is "reluctant neighbor"? no: Tally's page does not mention Emmek) |
| 11 | L29 | "Emmek Frewn runs Frewn's Brews, the competing tavern a few doors down Trollskull Alley; openly hostile to the party's establishment, he has already hired local criminals to cause problems and will not stop unless the party gives him a reason to." | "openly hostile to the party's establishment" and "has already hired local criminals to cause problems" are quest-time framing (the sabotage begins in ev-02). "will not stop unless the party gives him a reason" is campaign design. Drafter restates (ruling 1). "a few doors down" conflicts with ev-01 (D4) | `ev-02-the-guild-gauntlet.md:11`; `north-ward.md:58` ("a few doors down is Frewn's Brews") |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/trollskull-community.md`, lines 169 to 183)**

- Line 170 tagline: "*A loud, bitter rival publican who blames adventurers for everything and hides his shame in complaints.*" — day-one. Keep.
- Line 175 Swearing: "*Punctuation · Colourful · Rant.* Bitter and constant under his breath: "fucking adventurers", "shit ale, is it?". It gets loud when he's cornered." — day-one. Keep (adult table, real profanity in speech).
- Line 179 Never: "He never admits sabotage, never says the party's tavern is better, and never asks for help directly." — "sabotage" presumes the quest's escalation. Keep the trait; drafter decides wording.
- Line 181 Greeting: "*Greeting:* "Oh, it's you. Come to gloat? Frewn's Brews is open, if anyone wants honest drink."" — "Come to gloat?" assumes the party's success. "Frewn's Brews is open" is day-one. **Borderline.** Drafter's call (ruling 16).
- Line 182 Business: "*Business:* "Say I knew some lads who broke your windows. Say I didn't. What's it worth to you either way?"" — **quest-time clause.** "broke your windows" is a sabotage event of the quest (Stage 2–4; ev-02 and ev-07). Restate as a day-one line or drop (ruling 16).
- Line 183 Under pressure: "*Under pressure:* "I never hired any fucking body! I lost everything once already, do you know that? Everything!"" — **quest-time clause in the first sentence.** "I never hired any fucking body!" denies the quest's sabotage hire. Keep "I lost everything once already, do you know that? Everything!" (day-one). Drafter restates the first sentence (ruling 16).
- Line 177 "He talks to passers-by about the party while the party is standing right there. He counts coins while he speaks. He never finishes an apology." — habit; "the party" is the quest's party. Drafter's call.
- Line 178 signature phrases: "Adventurers ruin a street." / "Honest trade, that's all I want." / "I never did any such thing." — day-one. Keep.

### C2. Where Emmek's quest-time events already live (routed; do not restate on the day-one page)

- **Trollskull Alley, ev-01 (arrival, blockquote)**: "**Frewn's Brews** — at the far end of the alley, a pub under a fresh sign with new paint and modest foot traffic at this hour. The name is not Trollskull Manor." — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:31`
- **Trollskull Alley, ev-02 (The Guild Gauntlet), summary**: "> - Emmek Frewn begins his sabotage campaign: Stage 1 imposes −2 on permit inspection DCs for the first week" — `ev-02-the-guild-gauntlet.md:11` (blockquote)
- **Trollskull Alley, ev-02, Emmek's First Move**: "Frewn spent the day after the party arrived speaking to the Carpenters' Guild foreman and the Cellarers' inspector about the party's \"property destruction history\" and \"possible Watch complications\" from the warehouse incident in Finding Floon. These conversations do not block any permit but impose a **−2 penalty on all guild inspection DCs for the first week**. The party will not know the source unless they ask and succeed on a **DC 13 Charisma (Persuasion)** check with the relevant inspector." — `ev-02-the-guild-gauntlet.md:26`
- **Trollskull Alley, ev-02**: "The Shard Shunner wererats in halfling form are visible in the alley behind Emmek during his **The Neighbors** Event visit, casing the manor as potential staff applicants and looking for entry points. **DC 13 Wisdom (Perception)** to notice them now." — `ev-02-the-guild-gauntlet.md:28`
- **Trollskull Alley, ev-02**: "Broxley Fairkettle and Hammond Kraddoc arrived on the same morning with two different checklists and the same expectation: that the party would visit six guilds, pass six inspections, and pay the associated fees before a single drink could be legally served. Emmek Frewn had already spoken to two of those inspectors." — `ev-02-the-guild-gauntlet.md:78`
- **Trollskull Alley, ev-02, Concluding**: "The party navigated six guild inspections and discovered that their competition had a head start — Emmek Frewn had already spoken to two inspectors about them." — `ev-02-the-guild-gauntlet.md:86`
- **Trollskull Alley, ev-03 (The Neighbors)**: "**Emmek Frewn (Frewn's Brews).** Arrives during renovation with a bottle of cheap wine. Competitive politeness that curdles over ten minutes. He talks about market share, foot traffic, the sort of clientele the North Ward prefers. His sabotage campaign (ev-02) is already running; the party may not have connected it to him yet. The Shard Shunners are visible in the alley behind him for characters who succeed on a **DC 13 Wisdom (Perception)** check." — `ev-03-the-neighbors.md:31`
- **Trollskull Alley, ev-05 (The Field of Triumph)**: "> - Emmek's Stages 2–3 can trigger if the renovation has opened staff hiring" — `campaign/quests/act-i/trollskull-alley/ev-05-the-field-of-triumph.md:12`
- **Trollskull Alley, ev-06 (The Grand Opening)**: "> - Emmek's Stage 4 may fire: Shard Shunner wererats apply for staff positions under false names" — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:12`
- **Trollskull Alley, ev-07 (The Twin Parades), aftermath**: "Return to the tavern after the parades. Frewn's Brews suffered a minor incident: a cask cracked and leaked, blamed on a faulty fitting. Emmek is furious at his contractor, a halfling named Kelso Fiddlewick. The party finds a note slid under their door: *\"Apologies for any confusion. The service economy is difficult.\"* No signature." — `ev-07-the-twin-parades.md:77`
- **Trollskull Alley, ev-07**: "This is Emmek's Stage 4 misfiring. Kelso targeted the wrong building. Emmek knows it; the party does not yet. The note may become useful evidence later." — `ev-07-the-twin-parades.md:79`
- **Trollskull Alley, ev-07, Doc note**: "> - The Festival Aftermath (Frewn's cask incident) provides closure on Emmek's arc and confirms Stage 4 misfired" — `ev-07-the-twin-parades.md:13`
- **Trollskull Alley, Design notes, Emmek as Sustained Antagonist**: "**The Quest's Only Persistent Conflict Thread.** Every other conflict in Trollskull Alley is either friendly (factions) or reactive (guild inspections, neighbor eccentricities). Emmek Frewn is the quest's only genuine antagonist — a man actively working to destroy what the party is building." — `campaign/quests/act-i/trollskull-alley/design-notes.md:23`
- **Trollskull Alley, Design notes, the four paths**: "The party can resolve him through four paths: *confront* (exposing his Istrid Horn loan creates pressure, since Istrid wants no Watch attention and her Doom Raiders affiliation complicates public enforcement); *outcompete* (become successful enough that he can no longer afford the Shard Shunners); *cover his debt* (Istrid is owed 150 gp; covering it removes his leverage); *Watch report* (the Shard Shunners are halfling wererats: a Watch report implicates him in something far more serious than a business dispute)." — `design-notes.md:25`
- **Trollskull Alley, overview**: "- **Emmek Frewn** (independent) — competitor across the alley; runs Frewn's Brews; his five-stage sabotage campaign begins in ev-02" — `campaign/quests/act-i/trollskull-alley/overview.md:30` (quest summary; label conflict, D6)
- **Trollskull Alley, overview**: "**Shard Shunner Wererats:** Halfling lycanthropes in Emmek Frewn's employ. Spotted casing entry points in ev-02; one may return for a staff interview under a false name in ev-06. Not a combat encounter unless the party initiates." — `overview.md:53`
- **Trollskull Alley, flowchart**: "[ev-02] The Guild Gauntlet          ←── Emmek Stage 1 begins (−2 DC penalty)" — `campaign/quests/act-i/trollskull-alley/flowchart.md:8`
- **Gazetteer, Field Ward**: "Emmek Frewn hired him to sabotage Trollskull Manor. In **The Twin Parades** a cracked cask at Frewn's Brews shows the Shunners hit the wrong building." — `campaign/gazetteer/waterdeep/field-ward.md:112`
- **Gazetteer, North Ward, Hook**: "- Hook: he calls on the party during the renovation of **Trollskull Alley** with a bottle of cheap wine, while his sabotage campaign is already running." — `campaign/gazetteer/waterdeep/north-ward.md:131`
- **Doom Raiders, Snobeedle mission (Arc ZR-3 in Appendix C), Scene 2 (quest-time)**: "> > \"Frewn? Yes, the lads did the Trollskull job, partner, and the cask on the parade day was the wrong building, and I did send a note. No hard feelings, I hope. Contract's a contract, and we were paid to make a nuisance of ourselves, not to hurt anyone.\"" — `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:295`
- **Doom Raiders, Snobeedle, Scene (Istrid's money)**: "> > \"Separate from all that, and you can have it whichever way you decide. The pub man on Trollskull Alley, Frewn. The money he paid us with came in a purse sealed with Istrid Horn's mark, and two of her collectors sat in a corner while he hired us. I thought you might like to know how your own people keep an eye on you.\"" — `ev-01-the-missing-snobeedle.md:317`
- **Doom Raiders, Snobeedle, Facts block**: "> Emmek Frewn borrowed 150 gp from Istrid Horn and spent 50 gp of it hiring Kelso's gang against the party's tavern. Two of Istrid's collectors were in the room when he did. Istrid heard about it from them and did nothing to stop it, because a borrower who spends is a borrower who keeps borrowing. She did not order the sabotage. Dasher does not know how Istrid reacted, and neither do the Doom Raiders unless the party asks her." — `ev-01-the-missing-snobeedle.md:321`
- **Doom Raiders, Snobeedle, Q&A (loan terms)**: "> > \"Mr. Frewn borrowed a hundred and fifty gold, dear, at ten percent each tenday. He told me it was for his cellar and his stock, which is the sort of thing a publican says. What a borrower buys with my gold is his affair, and I try not to ask.\"" — `ev-01-the-missing-snobeedle.md:427`
- **Doom Raiders, Snobeedle, Q&A (the collectors)**: "> > \"One of my collectors mentioned that Mr. Frewn had hired some halflings to make trouble for your tavern, and I saw no reason to stop him. He was spending, which meant he'd keep borrowing, and it is a pity, dear, but I never told him to do it.\"" — `ev-01-the-missing-snobeedle.md:433`
- **Doom Raiders, Snobeedle, Q&A (Emmek's Q)**: "> [!qna]**About Emmek Frewn?**" — `ev-01-the-missing-snobeedle.md:293`
- **Doom Raiders, Snobeedle overview**: "Emmek Frewn borrowed 150 gp from Istrid Horn and spent 50 gp of it on Kelso's gang, who spent that time making trouble for the party's tavern on Trollskull Alley. Dasher was one of the four Shunners on that job, and he remembers that Istrid's collectors sat in on the hiring." — `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:23`
- **Doom Raiders, Snobeedle, Waymoot**: "He also volunteers, without conditions, that Emmek Frewn's money came from Istrid Horn." — `overview.md:41`
- **Order of the Gauntlet, Shard Shunners mission, Kelso (quest-time)**: "> > \"That was Emmek Frewn, and it was a separate contract. I did send a note about the cask on parade day, and no hard feelings, I hope. This one isn't business, it's my sister.\"" — `campaign/quests/faction-events/order-of-the-gauntlet/m03-the-shard-shunners/ev-01-the-shard-shunners.md:243`
- **Order of the Gauntlet, Vindicator, evidence**: "| A named independent, for example Emmek Frewn | A paper naming one act, such as a receipt or signed statement showing who hired Kelso's gang against Trollskull Alley | He hired the gang, the coin was paid through a go-between, and Savra can refer the matter to the Watch | Anything about the Grand Game, or who lent him the coin |" — `campaign/quests/faction-events/order-of-the-gauntlet/r25-vindicator/ev-01-vindicator.md:111`
- **Bregan D'aerthe, Coin Pouches, Dunstan Rook (doorman)**: "Dunstan Rook is a Chondathan human bouncer in his thirties who works the door at Frewn's Brews. Emmek Frewn pays him 2 gp a night to scare the party's staff. Since the Grand Opening he has stood across the alley from Trollskull Manor every evening. He has told the Beat 1 recipient twice that someone will lose fingers if the party's tavern keeps stealing Frewn's customers." — `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:59`
- **Bregan D'aerthe, Coin Pouches, Emmek's own voice (read-aloud)**: "> Across the alley the door of Frewn's Brews stands open, and the stool where the doorman usually sits is pushed against the wall. Emmek Frewn is sweeping the step himself with short angry strokes, and he counts the coins in his apron pocket between each pass. He glares at you as soon as you step outside." — `ev-01-coin-pouches.md:73`
- **Bregan D'aerthe, Coin Pouches, stat**: "> Emmek Frewn (Neutral Evil, Illuskan Human, he/him) :: the bitter owner of Frewn's Brews, who blames adventurers for everything and cannot finish an apology." — `ev-01-coin-pouches.md:77`
- **Bregan D'aerthe, Coin Pouches, Emmek's read**: "> Emmek assumes the party had something to do with Dunstan's absence and says so loudly enough for the alley to hear. He denies hiring anyone and talks about \"honest trade\" while he counts coins. He never admits the sabotage, and if the member accuses him, he only gets louder." — `ev-01-coin-pouches.md:79`
- **Doom Raiders org page, Istrid's lending**: "- **Lending:** Istrid lends to people in need of coin, and she treats every loan as leverage (**Istrid Horn**; **Dock Ward**). Emmek Frewn, a refugee from Neverwinter who runs a pub in the North Ward, owes her a loan that Zhentarim enforcers collect (**Emmek Frewn**; **North Ward**). When her enforcers prove inadequate she can call on her old adventuring companions (*Dragon Heist*, 5e)." — `campaign/setting/organizations/06-doom-raiders.md:72`
- **Istrid Horn page, Connections**: "**Relationships.** Istrid is the Doom Raiders' Master of Trade and Coin, Emmek Frewn's creditor (a loan with Zhentarim enforcement), and a worshipper of Vergadain whose lending operation funds the cell's operations." — `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:91`
- **Dock Ward gazetteer**: "> - Istrid likes having people in her debt and treats every loan as leverage. Emmek Frewn owes her 150 gp, and Zhentarim thugs collect it." — `campaign/gazetteer/waterdeep/dock-ward.md:141`
- **Adventure, Business Rival (Plans table, page 42)**: "Emmek spreads rumors that the characters' tavern is rat-infested, which is why he didn't buy it. Apply a -10 penalty on the next three rolls characters make on the Running a Business table (see \"Tavern Keeping Expenses,\" page 41)." — `sources/adventure-wdh.json:4296`
- **Adventure, Business Rival (Plans table, page 42)**: "Emmek pays the wererats another 50 gp to creep around the characters' tavern at night in hybrid and rat form, carve rat faces into the doors of neighbors, and otherwise draw attention to themselves." — `sources/adventure-wdh.json:4304`
- **Adventure, Business Rival (Plans table, page 42)**: "Emmek convinces several local residents to sign a letter he has drafted, then dispatches it to the City Watch. The letter accuses the characters of running a front for a guild of wererat thieves and urges the Watch to close their establishment." — `sources/adventure-wdh.json:4308`
- **Adventure, Chapter 2 wrap (page 42)**: "In this section of the adventure, the characters should advance to 3rd level by engaging in faction missions, dealing with {@creature Emmek Frewn|WDH}, or partaking in self-directed activities." — `sources/adventure-wdh.json:4324`
- **Adventure, Vault epilogue (post-Vault, page 98)**: "{@creature Emmek Frewn|WDH} (see \"Business Rival: {@creature Emmek Frewn|WDH}\") needs 1,500 gp to pay off a loan with interest. If he doesn't repay the coin in a tenday, {@creature Istrid Horn|WDH} (see {@adventure appendix B|WDH|12}) sends Zhentarim thugs to threaten, if not hurt, him. Emmek comes to the characters with hat in hand, preying on their generosity while denying any wrongdoing on his part." — `sources/adventure-wdh.json:14892`
- **PDF, Ryba (barmaid, printed p.183)**: "Ryba is a wererat and a member of the Shard Shunners (see \"Emmek Frewn\" below). She tries to get hired as a halfling waitress so that she can work mischief." — PDF page 6. **Check with pdftotext.** The "Emmek Frewn" entry is not in the PDF (F5).
- **PDF, Grand Opening (printed p.184)**: "Give some thought to whether or not Emmek Frewn is in a position to disrupt the Grand Opening. If the PCs have taken precautions, it's probably better to let the Grand Opening succeed… and then have Emmek Frewn's bastardy complicate matters on their second night." — PDF page 7. **Check with pdftotext.**
- **PDF, Guild visits (printed p.182)**: "During this time, also mix in the first visits from Emmek Frewn (Dragon Heist, p. 42) as he begins plotting against the PCs." — PDF page 5. **Check with pdftotext.**

---

## D. Conflicts

**D1. The loan figure: 150 gp or 1,500 gp.**
- Adventure, opening scene: "Emmek secures a 150 gp loan from {@creature Istrid Horn|WDH} (see {@adventure appendix B|WDH|12})." — `sources/adventure-wdh.json:4264`
- Adventure, Vault epilogue: "{@creature Emmek Frewn|WDH} (see \"Business Rival: {@creature Emmek Frewn|WDH}\") needs 1,500 gp to pay off a loan with interest." — `sources/adventure-wdh.json:14892`
- Campaign uses 150 gp: "He owes **Istrid Horn** a loan of 150 gp, enforced by Zhentarim thugs" (`campaign/gazetteer/waterdeep/north-ward.md:135`); "Emmek Frewn borrowed 150 gp from Istrid Horn" (`ev-01-the-missing-snobeedle.md:321`).
- Istrid page's own conflict note: "**Conflicts:** The Emmek Frewn loan. The old Relationships line gave \"150 gp\" (`03-istrid-horn.md:25` before this edit; `dock-ward.md:141`; `north-ward.md:135`; `10-emmek-frewn.md:25`), and `adventure-wdh.json:4264` gives 150 gp. `06-doom-raiders.md:166` says the loan is named without its figure, and `adventure-wdh.json:14892` gives 1,500 gp later. The page states no figure." — `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:138`
- Doom Raiders org page: "**Settled:** Istrid's loan sizes, the vault share and the 5,000 gp donation are mechanics and are not on this page (ruling 18). See Routed facts. Emmek Frewn's loan is named without its figure for the same reason." — `campaign/setting/organizations/06-doom-raiders.md:166`
- Higher ranked: the opening loan at 150 gp (`:4264`), which is in the same Chapter 2 section as the plan. The 1,500 gp epilogue (`:14892`) is a later event (post-Vault, "if the characters recover Neverember's hoard"). The 1,500 gp figure belongs to a different moment and does not overwrite the loan. The page should state 150 gp, and the drafter should record the 1,500 gp figure as a later-state note only if it is routed.

**D2. "Enforced by Zhentarim thugs."**
- Adventure, loan entry (`:4264`): no enforcement is stated.
- Adventure, Vault epilogue (`:14892`): "If he doesn't repay the coin in a tenday, {@creature Istrid Horn|WDH} (see {@adventure appendix B|WDH|12}) sends Zhentarim thugs to threaten, if not hurt, him."
- Campaign, page Relationships (`10-emmek-frewn.md:25`): "enforced by Zhentarim thugs." Gazetteer (`north-ward.md:135`) and Doom Raiders org page (`06-doom-raiders.md:72`, "Zhentarim enforcers collect what he owes her") say the same.
- The enforcement comes from the epilogue, not the loan entry. Drafter's call.

**D3. The interest rate.**
- Campaign only: "Mr. Frewn borrowed a hundred and fifty gold, dear, at ten percent each tenday." — `ev-01-the-missing-snobeedle.md:427`
- Campaign Relationships: "150 gp loan with interest" (`10-emmek-frewn.md:25`).
- Adventure: "Her interest rates are comparable to those of her competitors" (`sources/adventure-wdh.json:31934`). No figure.
- Campaign-only figure (ten percent each tenday), in a quest Q&A. Not a conflict with the adventure, which gives no figure.

**D4. "A few doors down" versus "at the far end of the alley".**
- Gazetteer: "a few doors down is Frewn's Brews, a rival pub owned by **Emmek Frewn**." — `campaign/gazetteer/waterdeep/north-ward.md:58`
- Gazetteer, Emmek entry: "A salty northerner who opened Frewn's Brews a few doors down" (`north-ward.md:130`)
- Trollskull Alley ev-01: "**Frewn's Brews** — at the far end of the alley" (`ev-01-welcome-to-trollskull-alley.md:31`)
- Adventure: "choose an unmarked building on map 2.1 to serve as the pub." (`sources/adventure-wdh.json:4237`). No position.
- Campaign conflict between the gazetteer and the quest. Drafter's call. The page's Overview says "a few doors down Trollskull Alley" (`10-emmek-frewn.md:29`).

**D5. "An insult to joinery" (Tally's view of Emmek's sign).**
- Page: "a reluctant neighbor of Tally Fellbranch (who thinks Emmek's pub sign is \"an insult to joinery\")" — `10-emmek-frewn.md:25`
- Search: `sources/` and `campaign/` (except copies of this page and its research notes) contain no "insult to joinery" line. The adventure, Appendix D and the PDF do not say it. **Unsourced.** The drafter must tag it `[research]` or `[design]` (ruling 17) or drop it.
- The Tally page does not mention Emmek (`campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md`, Grep for "Emmek" returns no line in that file).

**D6. Affiliation label.**
- Page summary: "> - **Affiliation:** Trollskull Alley community" — `10-emmek-frewn.md:6`
- Trollskull Alley overview: "- **Emmek Frewn** (independent) — competitor across the alley" — `campaign/quests/act-i/trollskull-alley/overview.md:30` (quest summary; brief ruling 6 says it does not govern)
- Doom Raiders org page, Connections: "**Fala Lefaliir** and **Emmek Frewn** (Notable Figures): the herbalist who shelters Ziraj and the debtor of Istrid's lending" — `campaign/setting/organizations/06-doom-raiders.md:156`. The Doom Raiders page treats him as a debtor, not a member.
- Guilds page, Trollskull: "**Emmek Frewn** (Neutral Evil, Illuskan Human, he/him) runs Frewn's Brews, and the published adventure says he is in trouble with two guilds." — `campaign/setting/governance-and-guilds/guilds.md:52`
- No organization page covers Emmek. The page's label "Trollskull Alley community" is the group label. Drafter's call under ruling 6; report only.

**D7. Sisters: plural or singular.**
- Adventure: "his sisters took over the business and bought him out" (`sources/adventure-wdh.json:4238`). Plural.
- Wiki: "After the death of his parents, Emmek's sister took care of the family business." (`scratchpad/wiki-trollskull-community/10-emmek-frewn.txt:72`). Singular.
- Campaign: "whose sisters pushed him out" (`10-emmek-frewn.md:21`). Plural.
- Higher ranked: the adventure (plural). The wiki's "sister" is a Wiki edit (WDH5e-p42 cited). Note the conflict; do not name the sisters.

**D8. The Neverwinter cause: "eruption" or "Ruining".**
- Adventure: "destroyed by the eruption of Mount Hotenow in 1451 DR" (`sources/adventure-wdh.json:4238`).
- Wiki: "relocated to Waterdeep after the [[Ruining]] of [[1451 DR]]" (`scratchpad/wiki-trollskull-community/10-emmek-frewn.txt:72`).
- Campaign: "a Neverwinter refugee whose family fled Mount Hotenow's eruption" (`10-emmek-frewn.md:21`).
- Both give 1451 DR. The wiki's "Ruining" is not explained in the extract. Higher ranked: the adventure. `[research]` for any link between the two.

**D9. Trades Ward.** No conflict. The adventure and the wiki both place the family's tannery in the Trades Ward (`sources/adventure-wdh.json:4238`; wiki `:72`).

**D10. Trollskull Manor: who bought it.**
- Adventure: Emmek "recently tried to buy the tavern in Trollskull Alley but was outbid by Volothamp Geddarm" (`sources/adventure-wdh.json:4237`).
- PDF: "Most recently, Emmek Frewn attempted to purchase the property at public auction, only to be outbid by Volothamp Geddarm" (printed p.181). **Check.**
- Gazetteer: "Volo bought the building recently, hoping its haunting would give him a chapter for his next book." (`north-ward.md:198`)
- Consistent. No conflict.

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Stale or conflicting lines**
- `campaign/gazetteer/waterdeep/north-ward.md:135`: the loan is "150 gp, enforced by Zhentarim thugs" — the 150 gp is consistent with the opening loan, but "enforced by Zhentarim thugs" is from the epilogue (D2). Not stale; the source is in the epilogue.
- `campaign/gazetteer/waterdeep/north-ward.md:131`: "Hook: he calls on the party during the renovation of **Trollskull Alley** with a bottle of cheap wine, while his sabotage campaign is already running." — quest-time (routed to ev-03:31).
- `campaign/setting/notable-figures/doom-raiders/03-istrid-horn.md:46`: "Emmek Frewn: A debtor, a refugee from Neverwinter who runs a pub in the North Ward. Zhentarim enforcers collect what he owes her." — consistent with the page, but "Zhentarim enforcers" is the epilogue's enforcement (D2).
- `campaign/setting/organizations/06-doom-raiders.md:166`: "Emmek Frewn's loan is named without its figure" — the page's own loan figure is 150 gp at `:4264`. Not stale for the Doom Raiders page's purpose, but the Istrid page (`03-istrid-horn.md:138`) and the org page disagree about whether a figure is named.
- `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md:23`: "Emmek Frewn borrowed 150 gp from Istrid Horn and spent 50 gp of it on Kelso's gang" — consistent with `:4264`.
- `campaign/quests/act-i/trollskull-alley/overview.md:30`: "**Emmek Frewn** (independent)" — the label conflicts with the page; quest summary.
- `campaign/gazetteer/waterdeep/north-ward.md:58` and `:130`: "a few doors down" conflicts with `ev-01-welcome-to-trollskull-alley.md:31` ("at the far end of the alley") (D4).
- `campaign/setting/governance-and-guilds/guilds.md:52`: the Emmek entry gives "Neutral Evil, Illuskan Human, he/him" — consistent with the page.
- `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:77`: "Emmek Frewn (Neutral Evil, Illuskan Human, he/him) :: the bitter owner of Frewn's Brews" — consistent.

**E2. Routed quest references (quest-time facts)**: see C2. In short: Trollskull Alley ev-01 (31), ev-02 (11, 24, 26, 28, 78, 86), ev-03 (31), ev-05 (12), ev-06 (12), ev-07 (13, 77, 79), design-notes (23, 25), overview (30, 53), flowchart (8); Doom Raiders Snobeedle ev-01 (293, 295, 317, 321, 427, 433) and overview (23, 41); Order of the Gauntlet Shard Shunners ev-01 (243) and Vindicator ev-01 (111); Bregan D'aerthe Coin Pouches ev-01 (59, 73, 77, 79); Istrid page (46, 91, 138); Doom Raiders org page (72, 156, 166); Dock Ward gazetteer (141); Field Ward gazetteer (8, 112); adventure Business Rival plans (4296, 4304, 4308), Chapter 2 wrap (4324) and Vault epilogue (14892).

**E3. Featured-in list is incomplete.** The page lists only **Trollskull Alley**. Emmek also appears in the Doom Raiders Snobeedle mission (Arc ZR-3, `Appendix_C_-_Player_Faction_Missions.md:1289`, and its Scene 3 at `:1338`), the Order of the Gauntlet Shard Shunners mission (`campaign/quests/faction-events/order-of-the-gauntlet/m03-the-shard-shunners/ev-01-the-shard-shunners.md:243`), and the Bregan D'aerthe Coin Pouches event (`s01-coin-pouches/ev-01-coin-pouches.md`). For the drafter's call.

**E4. Appendix C, Scene 3 (Doom Raiders mission), quest-time**: "I know what the offer says — 'safe return.' I am safe. I am returned to myself." (not Emmek). The Emmek line is: "He also offers, entirely separately, a piece of information: Emmek Frewn, the rival tavern owner sabotaging Trollskull Manor, is bankrolled by the Doom Raiders' own financial network through Istrid Horn. \"Thought you might like to know how your employer keeps tabs on you,\" he says." — `sources/Appendix_C_-_Player_Faction_Missions.md:1338`. Mission heading: "## Arc ZR-3 — The Missing Snobeedle" (`Appendix_C_-_Player_Faction_Missions.md:1289`). Aftermath: "The Emmek Frewn information, if believed and investigated, reveals a small but interesting detail about how the Doom Raiders maintain oversight of assets (like Trollskull Manor) that they consider within their sphere of influence." — `Appendix_C_-_Player_Faction_Missions.md:1346`.

---

## F. Gaps a Background would need that no source gives

1. **Birth and age.** No source. Wiki `age` and `dob` are blank (`scratchpad/wiki-trollskull-community/10-emmek-frewn.txt:17`, `:22`).
2. **Parents' names and occupations.** Adventure: "After Emmek's parents died" (`sources/adventure-wdh.json:4238`). Wiki: "Frewn's father worked in a tanning business in the [[Waterdeep/Trades Ward|Trades Ward]] of the city" (`:72`). No names. Must stay consistent with: his father tanned in the Trades Ward; both parents are dead.
3. **How many sisters and their names.** Plural in the adventure, singular in the wiki (D7). No names. Do not name them.
4. **The Neverwinter flight.** 1451 DR in both sources (D8). The family's holdings were destroyed (adventure). Must stay consistent with: family migrated after 1451 DR.
5. **The Neverwinter-to-Waterdeep route and when Emmek arrived.** No source. The wiki says the family "relocated to Waterdeep" after 1451 DR (`:72`); no date for Emmek himself.
6. **The Shard Shunner past.** The adventure says "with which he has had nefarious dealings in the past" (`sources/adventure-wdh.json:4264`). The wiki says "In the past, he had had dealings with the Shard Shunners" (`:69`). No date, no job, no name of the halfling who dealt with him. Must stay consistent with: he knew the gang before the campaign.
7. **The loan's date and the first contact with Istrid.** The adventure gives the loan in the Chapter 2 plan (`:4264`), with no date. Must stay consistent with: 150 gp, Istrid's lending operation in the Dock Ward (`:31934`).
8. **How he first came to the tavern-buying plan.** Adventure: "recently tried to buy the tavern in Trollskull Alley but was outbid by Volothamp Geddarm" (`:4237`). No date. PDF: "Most recently" (printed p.181).
9. **Faith.** No source. Do not give him a deity.
10. **Friends and neighbors.** Adventure: none named but the Shard Shunners (`:4265`) and Dunstan Rook (campaign: `ev-01-coin-pouches.md:59`, the Bregan doorman he pays 2 gp a night). Dunstan Rook is a campaign-created NPC; he is not a Notable Figure (no page). Must not be promoted without a page.
11. **PDF Emmek profile: absent.** The PDF's Ryba entry says "see 'Emmek Frewn' below" (printed p.183). **All 38 PDF pages were read.** No Emmek profile appears in printed pages 178 to 215. The PDF's Grand Opening note (printed p.184) and guild note (printed p.182) are the only Emmek lines. The Alexandrian material that the SOURCE_GUIDE says covers "his sabotage tactics, and how the feud escalates" (`sources/SOURCE_GUIDE.md:616`) is not in this PDF. The SOURCE_GUIDE line is stale for this PDF. Route this to the orchestrator.
12. **Whether Emmek is in the Doom Raiders or Zhentarim.** The adventure makes Istrid the Doom Raiders' Master of Trade and Coin (`:1447`: "{@creature Istrid Horn|WDH} (Master of Trade and Coin)"). Emmek is a borrower. No source makes him a member.

---

## G. Inner-life hints in the sources (exact quotes)

- **Hated the tanning work.** "He never liked the work anyway, and he particularly hated dealing with the League of Skinners and Tanners." — `sources/adventure-wdh.json:4238`
- **Hated the trade (wiki).** "Emmek always disliked the tanning business." — `scratchpad/wiki-trollskull-community/10-emmek-frewn.txt:66`
- **Pride in the new pub.** "Instead of pursuing the family trade, he used all his money in the development of a new tavern." — `scratchpad/wiki-trollskull-community/10-emmek-frewn.txt:66`
- **Stung by losing the tavern.** "Stung by the loss, he bought a smaller, less impressive building in the same alley and turned it into a pub, which he calls Frewn's Brews." — `sources/adventure-wdh.json:4237`
- **Sunk his wealth.** "Emmek is on shaky financial footing because he has sunk most of his wealth into this latest endeavor." — `sources/adventure-wdh.json:4239`
- **Wants the characters' business to fail.** "Emmek wants his pub to be the most successful tavern in the North Ward, and he wants the characters' business to fail spectacularly." — `sources/adventure-wdh.json:4246`
- **Wasteful and stingy.** "He tends to spend a lot on big, showy items and cut corners on the little amenities." — `sources/adventure-wdh.json:4255`
- **Refugee loss (voice).** "I lost everything once already, do you know that? Everything!" — `.claude/skills/character-voices/voices/trollskull-community.md:183`
- **Shame and anger (voice).** "Resentment and desperation. Every sentence is about fairness to him. He denies wrongdoing while visibly guilty. His shame turns into anger, and his refugee past comes out as bitterness if pressed." — `.claude/skills/character-voices/voices/trollskull-community.md:176`
- **Keeps counting coins (voice, quirk).** "He counts coins while he speaks." — `.claude/skills/character-voices/voices/trollskull-community.md:177`
- **Honest trade (voice).** "He talks about \"honest trade\" constantly." — `.claude/skills/character-voices/voices/trollskull-community.md:174`
- **Cannot finish an apology (BD read-aloud).** "the bitter owner of Frewn's Brews, who blames adventurers for everything and cannot finish an apology." — `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:77`
- **Sisters bought him out (campaign).** "whose sisters bought him out of the family tanning business" — `campaign/gazetteer/waterdeep/north-ward.md:135` (the same fact is in the adventure at `:4238`).
- **The fairness plea (voice).** "Every sentence is about fairness to him." — `.claude/skills/character-voices/voices/trollskull-community.md:176`
- **Bread-and-butter fear of losing the pub (campaign design).** "staking everything on a pub he cannot afford to lose." — `campaign/quests/act-i/trollskull-alley/design-notes.md:25`
- **Knows the pub is worse (campaign).** "He knows his pub is worse than the party's tavern, and that is why he keeps up the sabotage." — `campaign/gazetteer/waterdeep/north-ward.md:136`
- **Mentions Tally's joinery (unsourced; D5).** Not used as an inner-life hint.

---

## Section list for the drafter (per the pass 6 brief)

- Summary: keep. Affiliation label needs a ruling (D6).
- Background: A1 to A3 (Neverwinter, the tanning family, the outbid, the loan, the Shard Shunner past). Personal goals must come from G or be `[design]` (ruling 17). Do not contradict "a Neverwinter refugee" or "his sisters took over the business and bought him out."
- Loan: state 150 gp (D1). Interest: campaign only (D3). "Zhentarim thugs": from the epilogue (D2).
- Voice: lines 169 to 183. Lines 181, 182 and 183 (first sentence) are quest-time (C voice).
- Quest-time sentences to restate or route: C rows 3, 8, 9, 9b, 10, 11; the voice lines.
- Unsourced: "an insult to joinery" (D5), `[research]` or drop.
- Stale source to route: `sources/SOURCE_GUIDE.md:616` says this PDF covers Emmek's sabotage tactics and how the feud escalates; the PDF (all 38 pages read) has no such section (F11).
