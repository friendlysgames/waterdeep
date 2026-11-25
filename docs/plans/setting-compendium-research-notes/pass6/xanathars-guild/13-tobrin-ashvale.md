# Pass 6 research notes: Tobrin Ashvale

Page: `campaign/setting/notable-figures/xanathars-guild/13-tobrin-ashvale.md` (old shape: H1, Gamemaster's Summary, Roleplaying Information, Character Information, Overview; no `> Structuring draft.` banner at line 3)
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Model format: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Ruling used: Ches 1, 1492 DR, day one. Tobrin is not yet posted at Trollskull Manor (see C and D2). The hire happens at the Grand Opening, Ches 20.

Method and caveats:
- Campaign files: Read and Grep, quoted from the tool output. Line numbers are from the tool output.
- Published adventure: `sources/adventure-wdh.json`. Grep for `Tobrin|Ashvale|bartender` returned no matches. Tobrin does not appear in the published adventure.
- Alexandrian: `sources/Appendix_D_-_Running_the_Tavern.md` is markdown, so it is quoted directly. The candidate paragraphs sit inside `<div class="fvtt narrative">` wrappers (lines 193 and 195 for Tobrin); the quotes are the paragraph text only. `sources/27. Addendum A Night in Trollskull Manor.pdf` was read with the Read tool's `pages` parameter (PDF pp.1-4, printed pp.178-181). It was read as rendered images, so no `pdftotext` check was possible. Those four pages hold the tavern history, Tavern Time and the Three Urchins. They contain no staff candidate and no Tobrin. PDF pp.5 onward were not read.
- Wiki: no Tobrin in the wiki copies. Searched `scratchpad/fandom-dump/forgottenrealms_pages_current.xml` (0 matches for `Tobrin|Ashvale`) and `sources/research/` (matches only in the campaign-hits snapshots, listed in E2). There is no folder named `wiki-xg` in the scratchpad. The wiki dump is at `scratchpad/fandom-dump/`. The file `frwiki.xml.7z` is compressed and was not searched.
- The coordinator's note refers to "brief ruling 17". The brief at `docs/plans/setting-compendium-pass6-brief.md` has rulings 1 to 16 (ruling 15 is Background, ruling 16 is Voice). No ruling 17 was found, so this report treats rulings 15 and 16 as the governing rulings.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

---

## A. Background facts by theme

Tobrin has no origin, family, former life, faith or signature belonging in any source. The campaign's only Tobrin-specific background text is the Persona, Relationships and Summary lines on the page itself. The sourced background is limited to the Alexandrian interview profile and the campaign staff table.

### A1. Origin and family

No source. See F1.

Ethnicity only, from the campaign's staff table and Guild page:

> "| 5 | **Tobrin Ashvale** | NE Chondathan human | Deliberately forgettable — medium height, build, hair, clothes. Glances around the taproom with the casual interest of someone memorizing a room. "I like the North Ward. Quiet. I'm looking for something steady." Functionally competent. DC 14 Insight detects watchful quality behind professional calm. DC 16 Investigation of one Castle Ward reference reveals it has been under Xanathar's Guild protection for two years. If dismissed: Guild sends a replacement within 3 tendays — not bar staff this time. | Xanathar's Guild watcher. No combat mission; reporting role only. No version of his employment benefits the party. | 10 gp | No Revenue bonus. After 2 tendays: Guild has patron profile and party schedule. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:48` (the full row; it sits in the "Bartender Candidates (10 gp/tenday standard)" table whose heading is at line 40 and header row at line 42)

> "- **Tobrin Ashvale** — Chondathan human bartender, neutral evil. See the **Tobrin Ashvale** page in Notable Figures."
> — `campaign/setting/organizations/08-xanathars-guild.md:112`

### A2. Former life and work history (Alexandrian, Appendix D)

> "He is forgettable in the precise way that suggests effort has gone into it: medium height, medium build, brown hair cut unremarkably, clothes that are clean but not distinctive. He smiles when he is supposed to smile and nods when he is supposed to nod. His references are impeccable — three separate establishments in the Castle Ward, all of which will confirm he worked there. "I heard you were hiring," he says. "I like the North Ward. Quiet. I'm looking for something steady." He glances around the taproom with the specific casual interest of someone memorizing a room."
> — `sources/Appendix_D_-_Running_the_Tavern.md:194` (the paragraph sits inside `<div class="fvtt narrative">`, lines 193 to 195)

> "Tobrin has tended bar before — he is not Pix; he can actually do the job. He is here because the Xanathar Guild places low-level watchers in North Ward establishments when those establishments become points of interest. He has no combat mission. His role is to report on who visits, what they discuss within earshot of the bar, and whether the characters appear to be holding or moving any Golorr artifacts. He files reports through a contact in the Dock Ward."
> — `sources/Appendix_D_-_Running_the_Tavern.md:197`

Context: the three Castle Ward establishments are his claimed references (they are "impeccable" and "will confirm he worked there"). The Appendix does not name them. "Pix" is not a candidate elsewhere in Appendix D or in the campaign. The name is an unexplained reference (see Not found).

### A3. How he joined the Guild

No Tobrin-specific source. The general entry test for every member:

> "- **Crime Is the Entry Fee:** Anyone can join, but an applicant must first pass a test that always involves a serious crime. The crime might be murdering a member who failed Xanathar, kidnapping a Waterdhavian, collecting a ransom or looting a warehouse. After that, advancement depends on wiles and on the ability to dispose of rivals, and the competition is fierce and often deadly."
> — `campaign/setting/organizations/08-xanathars-guild.md:32`

### A4. Rank and position in the Guild

The campaign gives no rank for Tobrin. The Guild's published ladder:

> "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:45`

The role the staff guide gives him is in the full row quoted at A1 (Faction Note column: "Xanathar's Guild watcher. No combat mission; reporting role only. No version of his employment benefits the party."). The Appendix says the same:

> "Tobrin is a Guild watcher, not a Guild ally. There is no version of this where Tobrin can be turned to the party's benefit; he is simply an ear in the taproom."
> — `sources/Appendix_D_-_Running_the_Tavern.md:201` (the paragraph begins "**Faction Note:** Xanathar Guild — an adversary faction, not available to player characters.")

### A5. Relationships to named figures

Grevik Nass (campaign, the other plant):

> "Grevik is an operative of Xanathar's Guild embedded as the tavern's Master Cook candidate, a man whose two-tenday file will give Xanathar a usable picture of Trollskull's patronage, and one of two Guild plants in the tavern staff alongside Tobrin Ashvale, whose position behind the bar gives the Guild a second angle on the same room."
> — `campaign/setting/notable-figures/xanathars-guild/12-grevik-nass.md:25`

> "- **Routed to quests (ruling 28):** Secret, the plants: "Grevik Nass and Tobrin Ashvale are the Guild's two plants among the staff of Trollskull Manor. Each keeps a file on the tavern's patrons." The placements happen when the party hires staff. They live in `campaign/guides/trollskull-manor/03-staff-and-hiring.md` (lines 48 and 107), in `09-response-teams-at-the-tavern.md:23`, and in their Notable Figures pages (`12-grevik-nass.md:25`, `13-tobrin-ashvale.md:21`, `:25`)."
> — `campaign/setting/organizations/08-xanathars-guild.md:196`

Nar'l Xibrindas (Appendix D only; no campaign file links them):

> "If the characters discover his affiliation and dismiss him, N'arl Xibrindas dispatches a replacement within three tendays — this time not applying for a bar position."
> — `sources/Appendix_D_-_Running_the_Tavern.md:205` (the full mechanical-effect paragraph begins "**Mechanical Effect:** Functionally competent bartender; no Revenue Roll bonus or penalty.")

### A6. Faith, signature belongings, how long in post

No source for any of the three. The only "signature" detail is a voice quirk (G1).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, current page: "*Chondathan human bartender, neutral evil, he/him*. Stat block: **Spy**." — `campaign/setting/notable-figures/xanathars-guild/13-tobrin-ashvale.md:5`
- Campaign, staff guide: "| 5 | **Tobrin Ashvale** | NE Chondathan human |" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:48` (NE = neutral evil, the campaign's own abbreviation)
- Campaign, Guild page: "- **Tobrin Ashvale** — Chondathan human bartender, neutral evil." — `campaign/setting/organizations/08-xanathars-guild.md:112`
- Alexandrian: "*NE male human, Commoner. A Xanathar Guild information plant — not a fighter, just a watcher.*" — `sources/Appendix_D_-_Running_the_Tavern.md:191` (NE, abbreviation not spelled out)
- Adventure: no Tobrin entry.
- Wiki: none.

**Species**
- Campaign, current page: "Chondathan human" (`13-tobrin-ashvale.md:5`)
- Campaign, Guild page: "Chondathan human bartender" (`organizations/08-xanathars-guild.md:112`)
- Campaign, staff guide: "NE Chondathan human" (`03-staff-and-hiring.md:48`)
- Alexandrian: "NE male human" (`Appendix_D_-_Running_the_Tavern.md:191`)
- Ethnicity "Chondathan" is a Faerûn ethnicity and matches brief ruling 5. No conflict.

**Pronouns**
- Campaign, current page: "he/him" (`13-tobrin-ashvale.md:5`)
- Alexandrian: "male" (`Appendix_D_-_Running_the_Tavern.md:191`). Prose: "He is forgettable" (`:194`), "He files reports" (`:197`).
- Campaign, staff guide: no pronoun in the row. Not used as a source.
- `docs/plans/npc-pronouns-table-group-c.md:38` gives the source of the he/him as "prose ("his attentiveness", "To those he trusts")". The page's own summary line is the stronger source.

**Stat block**
- Campaign, current page: "Stat block: **Spy**." (`13-tobrin-ashvale.md:5`)
- Alexandrian: "*NE male human, Commoner. ...*" (`Appendix_D_-_Running_the_Tavern.md:191`). "Commoner" is Appendix D's label for every candidate. It conflicts with the campaign's "Spy" (D1).
- Campaign, staff guide and Guild page: no stat block given.
- Adventure: no entry. Wiki: none.

**Name and surname**
- "Tobrin Ashvale" in all sources: `13-tobrin-ashvale.md:1`, `08-xanathars-guild.md:112`, `03-staff-and-hiring.md:48`, `Appendix_D_-_Running_the_Tavern.md:190`. The surname appears nowhere else. No live collision: the Order of the Gauntlet armory cleric was renamed (see E3).

---

## C. Every sentence on the current page that narrates a quest-time event or a day-one conflict

Current page: `campaign/setting/notable-figures/xanathars-guild/13-tobrin-ashvale.md`. "Day-one OK" means no quest gate is needed. "Quest-time" means the sentence narrates a hire, a discovery, a trigger, or a party action. Line numbers are from the current file.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Chondathan human bartender, neutral evil, he/him*. Stat block: **Spy**." | Day-one for ethnicity, alignment, pronouns. "bartender" is a Ches 1 conflict (D2). "Spy" conflicts with Appendix D (D1). | `organizations/08-xanathars-guild.md:112`; `03-staff-and-hiring.md:48`; `Appendix_D_-_Running_the_Tavern.md:191` |
| 2 | L6 | "**Affiliation:** Xanathar's Guild" | Day-one OK | `organizations/08-xanathars-guild.md:112` (under Key Members of Xanathar's Guild) |
| 3 | L7 | "**Featured in:** Background figure; no scripted appearance." | Day-one OK | Same wording on `12-grevik-nass.md:7` |
| 4 | L11 | "**Resonance.** Tobrin should inspire comfort with his attentiveness (he remembers names, usuals, and passing remarks from two visits ago) and retroactive unease when the party realizes none of that warmth is accidental." | Day-one for the attentiveness (voice line 231). "when the party realizes" is quest-time (a discovery). | Attentiveness: `voices/xanathars-guild.md:231` ("He remembers details from two visits ago and uses them."); discovery: routed to `trollskull-manor/09-response-teams-at-the-tavern.md:23` (the exposure trigger) |
| 5 | L13 | "**Emotions.** Tobrin most often feels practiced ease, attentive warmth (professional and deployed), patient calculation beneath a pleasant surface, mild contempt for patrons who volunteer everything, quiet satisfaction in a bar kept well, and the flat calm he allows himself only when alone." | Day-one. Matches the voice profile at 233 and 236. | `voices/xanathars-guild.md:233` ("Contempt for patrons who overshare never reaches his voice.") |
| 6 | L15 | "**Motivations.** Tobrin wants to maintain a running intelligence file on Trollskull's patrons, visitors, and overheard conversations; keep the bar warm enough that no one suspects the bartender; and use his position in the Guild's response chain to trigger escalation when the threshold is crossed." | "Trollskull's patrons" is hire-time (D2). "use his position in the Guild's response chain to trigger escalation when the threshold is crossed" has no source and conflicts with the staff guide's "reporting role only" (D4). | `03-staff-and-hiring.md:48` ("reporting role only"); `Appendix_D_-_Running_the_Tavern.md:197` ("His role is to report on who visits"); `09-response-teams-at-the-tavern.md:21`-`:23` (the triggers are the party's actions and the exposure of a plant, not a call by Tobrin) |
| 7 | L17 | "**Inspirations.** When playing Tobrin, channel Sam Malone (*Cheers*), Varys (*Game of Thrones*), and Tom Ripley (*The Talented Mr. Ripley*)." | Not a fact | n/a |
| 8 | L21 (a) | "**Persona.** To the world, Tobrin is a warm, attentive bartender who makes everyone feel like a regular." | Day-one for the public face, but "is a bartender" is a hire-time claim on Ches 1 (D2). The public face can rest on the references and past bar work (A2). | `Appendix_D_-_Running_the_Tavern.md:197` ("Tobrin has tended bar before") |
| 9 | L21 (b) | "To those he trusts (meaning no one), he runs a rolling intelligence file on every patron: who meets whom, who seems nervous, who the party has been talking to." | "every patron" and "who the party has been talking to" are quest-time, since they depend on a party presence in his room. The file itself is a campaign-wide reporting duty. | `Appendix_D_-_Running_the_Tavern.md:197` ("His role is to report on who visits, what they discuss within earshot of the bar") |
| 10 | L21 (c) | "Deep down, he is one of two Guild plants in the building, the one with better social access, and he is waiting to see how long it takes anyone to notice either of them." | "in the building" and "waiting to see how long it takes anyone to notice" are quest-time. "one of two Guild plants" is a routed fact. "the one with better social access" has no source. | `organizations/08-xanathars-guild.md:196` (the placement happens when the party hires staff); `12-grevik-nass.md:25` ("one of two Guild plants in the tavern staff") |
| 11 | L23 (a) | "**Morale.** In a fight, Tobrin does not fight." | Day-one OK | `Appendix_D_-_Running_the_Tavern.md:197` ("He has no combat mission.") |
| 12 | L23 (b) | "He disappears into the crowd and reports at the first opportunity." | Day-one OK | Staff guide `03-staff-and-hiring.md:48` ("reporting role only"); no source for "disappears into the crowd" |
| 13 | L23 (c) | "Once discovered, he negotiates: what he knows about the Guild's operations in this building is worth more to the party than his Guild debt, and he understands the math." | "Once discovered" is quest-time. The offer to negotiate conflicts with the staff guide (D5). "his Guild debt" has no source (F7). | `03-staff-and-hiring.md:48` ("No version of his employment benefits the party."); `Appendix_D_-_Running_the_Tavern.md:199` ("There is no version of this the characters can turn to their advantage; the Guild placed him, and the Guild does not share.") |
| 14 | L25 (a) | "**Relationships.** Tobrin is an operative of Xanathar's Guild embedded as the tavern's bartender," | Quest-time. "embedded as the tavern's bartender" is a hire-time state (D2). | `organizations/08-xanathars-guild.md:196`; `quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22` ("In the days before opening, candidates arrive for each open position.") |
| 15 | L25 (b) | "one of the Guild's two Trollskull infiltrators alongside Grevik Nass," | Quest-time (the two plants exist only once hired). | `organizations/08-xanathars-guild.md:196`; `12-grevik-nass.md:25` |
| 16 | L25 (c) | "and the trigger for the Guild's escalating response conditions (detailed in the **Trollskull Manor** guide); when the party crosses a threshold, Tobrin makes the call." | Quest-time. "Tobrin makes the call" has no source and conflicts with the response-team file, which makes the exposure of a plant the trigger (D4). | `trollskull-manor/09-response-teams-at-the-tavern.md:21`-`:23` (the triggers) |
| 17 | L29 | "Tobrin Ashvale is an attentive bartender who remembers names, usual orders, and passing remarks from two visits ago. He keeps the bar warm and makes everyone feel like a regular." | Day-one for the attentiveness. "is an attentive bartender" and "keeps the bar warm" depict a posting not held on Ches 1 (D2). The Overview is player-safe and needs a public face that does not require a post. | `Appendix_D_-_Running_the_Tavern.md:197` ("Tobrin has tended bar before") |

**Voice profile quest-time clauses** (`.claude/skills/character-voices/voices/xanathars-guild.md`, lines 226 to 240; the figure's profile in full is quoted in G):
- Line 238, Greeting: "Back again! Dark ale, and how did it go with the moneylender? Last time you were worried." Quest-time. It presumes a party visit ("Back again") and a party matter ("the moneylender") that the party has not had on Ches 1. Restate as a day-one greeting or remove, under ruling 16.
- Line 239, Business: "Busy night. Who was the fellow in grey you were talking to? Looked like a serious sort." Borderline. It presumes a party conversation in the room. The drafter decides whether to restate it as a generic probe.
- Line 240, Under pressure: "Whoa, easy, easy. Nobody needs trouble. First round's on the house." Borderline. "Under pressure" implies a confrontation, but the line is a standard de-escalation, so it reads as day-one. Flag for the drafter.
- Line 234, Quirks: "He greets people with their usual and a detail ("How's the sister's wedding?")." The example greets an unnamed patron and is not evidence of a sister in Tobrin's life (see G1). Flag so the drafter does not read it as a fact about Tobrin.

**Interview lines (hire-time, not day-one):**
- `03-staff-and-hiring.md:48`: "I like the North Ward. Quiet. I'm looking for something steady." (inside the full row quoted at A1)
- `Appendix_D_-_Running_the_Tavern.md:194`: "\"I heard you were hiring,\" he says."

**Routing for the quest-time sentences (rows 4, 6, 9, 10, 13 to 16, and the voice clauses).**
- Hiring and arrival: `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22`, `:25`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:34`; `campaign/structure/arc-b-trollskull-alley.md:207`
- Response triggers (exposure of a plant): `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:23`
- Dismissal and replacement: `campaign/guides/trollskull-manor/03-staff-and-hiring.md:48`; `Appendix_D_-_Running_the_Tavern.md:205`
- Plant status for the Guild: `campaign/setting/organizations/08-xanathars-guild.md:196`

---

## D. Conflicts

Rank used: campaign files first, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki. Where both sides are campaign files, the quest journal outranks the guide, and the guide outranks the page.

**D1. Stat block: "Spy" against "Commoner"**
- Campaign, current page: "*Chondathan human bartender, neutral evil, he/him*. Stat block: **Spy**." — `campaign/setting/notable-figures/xanathars-guild/13-tobrin-ashvale.md:5`
- Alexandrian: "*NE male human, Commoner. A Xanathar Guild information plant — not a fighter, just a watcher.*" — `sources/Appendix_D_-_Running_the_Tavern.md:191`
- Higher source: the campaign page ("Spy"). The Appendix label is a candidate-table convention. The orchestrator decides whether the Appendix label is worth recording as a conflict.

**D2. Position on Ches 1: posted bartender against hired at the Grand Opening**
- Campaign, current page: "Tobrin is an operative of Xanathar's Guild embedded as the tavern's bartender" — `13-tobrin-ashvale.md:25`; "Tobrin Ashvale is an attentive bartender" — `13-tobrin-ashvale.md:29`
- Campaign, staff guide: "When a position is open, candidates 1–4 arrive the next day, in table order. Candidate 5 arrives on the fourth day if the position is still open." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:34`
- Campaign, quest journal: "In the days before opening, candidates arrive for each open position." and "- Candidates arrive through word of mouth and guild placement notices; the party does not advertise" — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22`, `:25`
- Campaign, Guild page Draft Notes: "The placements happen when the party hires staff." — `campaign/setting/organizations/08-xanathars-guild.md:196`
- Campaign, Lif page: "a spectral colleague of whatever bartender the party hires" — `campaign/setting/notable-figures/trollskull-community/11-lif.md:25`
- Campaign, Grand Opening date: "| Ches 20 | Grand Opening of Trollskull Manor (**Trollskull Alley** ev-06) | Renovation complete; the tavern is open for business |" — `campaign/guides/gm-guide/structural-rules.md:43`; "The Grand Opening of Trollskull Manor falls on Ches 20" — `campaign/guides/gm-guide/session-zero.md:81`
- Higher source: the quest journal (ev-06) and the staff guide. The Notable Figures page is the outlier on Ches 1. The page and Grevik's page (`12-grevik-nass.md:25`, "embedded as the tavern's Master Cook candidate") both use present tense.

**D3. Hiring timing: "fourth day" against "three days"**
- Campaign: "Candidate 5 arrives on the fourth day if the position is still open." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:34`
- Alexandrian: "The DM should choose which candidates appear based on what the campaign needs, or roll 1d4 among options 1–4, with option 5 always appearing last if the position hasn't been filled after three days." — `sources/Appendix_D_-_Running_the_Tavern.md:83`
- Higher source: the campaign guide (fourth day). The Appendix also gives "roll 1d4 among options 1–4", which the guide does not use ("candidates 1–4 arrive the next day, in table order").

**D4. Role: "makes the call" against "reporting role only"**
- Campaign, current page: "use his position in the Guild's response chain to trigger escalation when the threshold is crossed." (`13-tobrin-ashvale.md:15`); "when the party crosses a threshold, Tobrin makes the call." (`13-tobrin-ashvale.md:25`)
- Campaign, staff guide: "Xanathar's Guild watcher. No combat mission; reporting role only. No version of his employment benefits the party." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:48`
- Campaign, response-team file: "- A Guild plant as staff (Tobrin Ashvale, Grevik Nass) has been exposed" — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:23` (a trigger on the party's side, not a call by Tobrin)
- Alexandrian: "He has no combat mission. His role is to report on who visits" — `sources/Appendix_D_-_Running_the_Tavern.md:197`
- Higher source: the campaign staff guide and response file. The page's "makes the call" has no source.

**D5. Negotiation: "worth more to the party" against "No version of his employment benefits the party"**
- Current page: "Once discovered, he negotiates: what he knows about the Guild's operations in this building is worth more to the party than his Guild debt, and he understands the math." — `13-tobrin-ashvale.md:23`
- Campaign staff guide: "No version of his employment benefits the party." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:48`
- Alexandrian: "There is no version of this the characters can turn to their advantage; the Guild placed him, and the Guild does not share." — `sources/Appendix_D_-_Running_the_Tavern.md:199`
- Higher source: the campaign staff guide. The Morale is verbatim roleplay text under brief ruling 3, so the orchestrator decides whether the negotiation can stay with a changed condition. The conflict is between two campaign texts.

**D6. Dismissal replacement: named Nar'l against unnamed Guild**
- Campaign staff guide: "If dismissed: Guild sends a replacement within 3 tendays — not bar staff this time." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:48`
- Alexandrian: "N'arl Xibrindas dispatches a replacement within three tendays" — `sources/Appendix_D_-_Running_the_Tavern.md:205`
- Higher source: the campaign guide, which names no one. No campaign file links Nar'l to Tobrin. The Nar'l page's research note records the same gap (`docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/03-narl-xibrindas.md:440`).

**D7. No conflict, recorded for the drafter: "watcher" and "bartender"**
- "Tobrin is a Guild watcher, not a Guild ally." (`Appendix_D_-_Running_the_Tavern.md:201`) and "Functionally competent bartender" (`Appendix_D_-_Running_the_Tavern.md:205`) both hold. The campaign calls him a bartender candidate. The two sources agree he is a watcher who can do the job.

---

## E. Stale lines in other files (not to be edited), and routed references

### E1. Stale or conflicting lines
- `campaign/setting/organizations/08-xanathars-guild.md:196` is correct on hire timing. The page's Relationships line (`13-tobrin-ashvale.md:25`) is the line that contradicts it.
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:34` (fourth day) against `sources/Appendix_D_-_Running_the_Tavern.md:83` (after three days) (D3).
- `sources/Appendix_D_-_Running_the_Tavern.md:205` names Nar'l (D6). The campaign does not.
- `sources/Appendix_D_-_Running_the_Tavern.md:1521` lists the plant as an exposure trigger: "- A Guild spy planted as staff (Tobrin Ashvale, Grevik Nass, or any similar candidate) has been exposed." This agrees with the campaign trigger at `09-response-teams-at-the-tavern.md:23`.
- `campaign/guides/factions/09-xanathars-guild.md` names neither Tobrin nor Grevik. Searched for "Trollskull|plant|tavern|staff|Tobrin|Grevik": only the Terasse Estate lines matched (`:21`, `:55`). The Factions Guide does not carry the tavern plants. Not stale, but the page's Relationships could cite it if needed.

### E2. Bundle copies (snapshots, not edited)
- `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:646`: "campaign/setting/notable-figures/xanathars-guild/13-tobrin-ashvale.md:25: **Relationships.** Tobrin is an operative of Xanathar's Guild embedded as the tavern's bartender, ..." (copy of the current `13-tobrin-ashvale.md:25`; same wording today).
- `sources/research/pass3-bundles/guilds/campaign-hits.txt:830`, `:832`, `:833`: copies of `13-tobrin-ashvale.md:16`, `:24`, `:26` (older line numbers).
- `sources/research/pass3-bundles/guilds/campaign-hits.txt:100`: copy of `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:23`.
- `sources/research/pass3-bundles/north-ward/campaign-hits.txt:13`: matched "Tobrin"; not opened for this page (the search output omitted the line).

### E3. Name collision (resolved in campaign)
- `campaign/quests/faction-events/order-of-the-gauntlet/r03-marcheon/design-notes.md:13`: "The draft's armory cleric is replaced by a lay brother, because the old name collided with a Xanathar bartender." The line does not name Tobrin. Searched `campaign/quests` for `Tobrin|Ashvale`: no matches. No live "Tobrin" armory cleric remains in the campaign.
- Pass plans record the collision: `docs/plans/order-of-the-gauntlet-plan.md:17` and `docs/plans/order-of-the-gauntlet-research/05-consistency-audit.md:303`. Not campaign files.

### E4. Routed quest references (where the quest-time facts already live)
- Hire and placement at the Grand Opening: `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22`, `:25`, `:26`, `:27`
- Response triggers, plant exposure: `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:21`-`:23`
- Routed on the Guild page: `campaign/setting/organizations/08-xanathars-guild.md:196`
- Hire-time staffing in the structure doc: `campaign/structure/arc-b-trollskull-alley.md:207` ("*Staff Hiring.* In the days before the opening, candidates arrive for each open position.")
- Staff candidate tables: `campaign/guides/trollskull-manor/03-staff-and-hiring.md:40`-`:48` (the Bartender Candidates table)
- The Trollskull Manor location: `campaign/structure/arc-b-trollskull-alley.md:23` ("The party holds the deed to a derelict tavern in the North Ward and roughly enough gold to question whether they can afford to fix it.")

---

## F. Sourced facts the drafter must stay consistent with; gaps and suggested inferences

### F-part 1: sourced facts to stay consistent with

1. **Alignment and ethnicity.** "*Chondathan human bartender, neutral evil, he/him*" (`13-tobrin-ashvale.md:5`); "NE Chondathan human" (`03-staff-and-hiring.md:48`).
2. **Pronouns.** he/him (`13-tobrin-ashvale.md:5`); "male" (`Appendix_D_-_Running_the_Tavern.md:191`).
3. **Affiliation.** Xanathar's Guild (`13-tobrin-ashvale.md:6`); "Xanathar Guild — an adversary faction, not available to player characters." (`Appendix_D_-_Running_the_Tavern.md:201`).
4. **Not an ally, no combat role.** "Tobrin is a Guild watcher, not a Guild ally." (`Appendix_D_-_Running_the_Tavern.md:201`); "No combat mission; reporting role only." (`03-staff-and-hiring.md:48`); "He has no combat mission." (`Appendix_D_-_Running_the_Tavern.md:197`).
5. **Job: reports.** "His role is to report on who visits, what they discuss within earshot of the bar, and whether the characters appear to be holding or moving any Golorr artifacts." (`Appendix_D_-_Running_the_Tavern.md:197`)
6. **Reporting channel.** "He files reports through a contact in the Dock Ward." (`Appendix_D_-_Running_the_Tavern.md:197`); the contact is unnamed (F5).
7. **Prior bar work.** "Tobrin has tended bar before" (`Appendix_D_-_Running_the_Tavern.md:197`); "His references are impeccable — three separate establishments in the Castle Ward, all of which will confirm he worked there." (`Appendix_D_-_Running_the_Tavern.md:194`)
8. **One protected establishment.** "DC 16 Investigation of one Castle Ward reference reveals it has been under Xanathar's Guild protection for two years." (`03-staff-and-hiring.md:48`); "DC 16 Investigation of his Castle Ward references reveals that one establishment has been under Xanathar Guild protection for two years." (`Appendix_D_-_Running_the_Tavern.md:199`)
9. **Hire-time posting.** He is not posted on Ches 1. He is placed when the party hires staff, from the candidate table (`03-staff-and-hiring.md:34`; `ev-06-the-grand-opening.md:22`; `08-xanathars-guild.md:196`).
10. **Plant pairing.** One of two Guild plants on the staff with Grevik Nass (`08-xanathars-guild.md:196`; `12-grevik-nass.md:25`). The campaign does not say the two know each other.
11. **Wage.** "10 gp" (the Wage column of the full row at A1, `03-staff-and-hiring.md:48`); "**Wage:** 10 gp/tenday." (`Appendix_D_-_Running_the_Tavern.md:203`)
12. **Dismissal.** "If dismissed: Guild sends a replacement within 3 tendays — not bar staff this time." (`03-staff-and-hiring.md:48`)
13. **Tenure effect.** "After 2 tendays: Guild has patron profile and party schedule." (`03-staff-and-hiring.md:48`); "After two tendays of employment, the Xanathar Guild has a detailed profile of the tavern's regular patron traffic and the party's schedule." (`Appendix_D_-_Running_the_Tavern.md:205`)
14. **No benefit to the party.** "No version of his employment benefits the party." (`03-staff-and-hiring.md:48`); "There is no version of this where Tobrin can be turned to the party's benefit" (`Appendix_D_-_Running_the_Tavern.md:201`). This conflicts with the Morale (D5).
15. **Named as a trigger.** "A Guild plant as staff (Tobrin Ashvale, Grevik Nass) has been exposed" (`09-response-teams-at-the-tavern.md:23`).
16. **Trollskull is in the North Ward.** "The party holds the deed to a derelict tavern in the North Ward" (`arc-b-trollskull-alley.md:23`). Tobrin's stated preference: "I like the North Ward." (`03-staff-and-hiring.md:48`).
17. **The Guild does not share.** "the Guild placed him, and the Guild does not share." (`Appendix_D_-_Running_the_Tavern.md:199`).

### F-part 2: gaps a Background would need, with suggested modest inferences

- **F1. Birth, family, early life, and the name Ashvale.** No source. Suggested: none. Leave blank, or state "[research] Chondathan by ethnicity; nothing more is sourced."
- **F2. Where he has worked.** The three Castle Ward establishments are not named (`Appendix_D_-_Running_the_Tavern.md:194`). Suggested: "[research] Three Castle Ward establishments where he worked behind a bar." Do not name them.
- **F3. How he joined the Guild.** No source. The general test: "Crime Is the Entry Fee" (`08-xanathars-guild.md:32`). Suggested: "[research] He passed the Guild's usual entry test."
- **F4. Rank.** No rank given. Suggested: "[research] A watcher with no rank on the Guild ladder (`08-xanathars-guild.md:45`)."
- **F5. The Dock Ward contact.** Unnamed (`Appendix_D_-_Running_the_Tavern.md:197`). Suggested: leave unnamed, or "[research] a Dock Ward contact he reports through."
- **F6. Handler.** Appendix D names Nar'l as the one who sends a replacement (`:205`). The campaign names no handler. Suggested: do not assert a Nar'l link on the page. Note it as Appendix-only.
- **F7. What the Guild holds over him.** Morale says "his Guild debt" (`13-tobrin-ashvale.md:23`). No source says what the debt is. Suggested: "[research] A debt to the Guild the source does not describe."
- **F8. Age.** No source. Suggested: none.
- **F9. Faith, shrine, or god.** No source. Suggested: none.
- **F10. Family, loves, losses, fears.** None sourced (see G). Suggested: none. Do not invent.
- **F11. Stat block.** "Spy" (campaign) against "Commoner" (Appendix). Suggested: keep "Spy" (higher source) and record the conflict.
- **F12. Ches 1 posting.** Not sourced as a day-one posting. Suggested: "[research] On Ches 1 he is a Guild watcher with bar references, awaiting a hire." The campaign leaves the day-one job open.
- **F13. Knowledge of Golorr artifacts.** His reporting target includes "whether the characters appear to be holding or moving any Golorr artifacts" (`Appendix_D_-_Running_the_Tavern.md:197`). No source says he knows what an Eye is. Suggested: do not state knowledge of the Stone or the Eyes.
- **F14. Time with the Guild.** No source for how long he has worked for the Guild. Suggested: none.

---

## G. Inner-life facts (fears, habits, loves, grudges, losses, places and people he cares about)

Every item is quoted. "None found" is stated where the source is silent. Nothing here is a fact about a family, a loss or a love.

**G1. Habits**
- "He wipes the same spot on the bar when listening hard." — `.claude/skills/character-voices/voices/xanathars-guild.md:234`
- "He greets people with their usual and a detail ("How's the sister's wedding?")." — `voices/xanathars-guild.md:234` (the example greets a patron. It is not a fact about Tobrin's family.)
- "He remembers details from two visits ago and uses them. He calls regulars by name." — `voices/xanathars-guild.md:231`
- "Tobrin Ashvale is an attentive bartender who remembers names, usual orders, and passing remarks from two visits ago. He keeps the bar warm and makes everyone feel like a regular." — `13-tobrin-ashvale.md:29`
- "He disappears into the crowd and reports at the first opportunity." — `13-tobrin-ashvale.md:23`

**G2. What he enjoys or takes pride in**
- "quiet satisfaction in a bar kept well" — `13-tobrin-ashvale.md:13`
- "Tobrin has tended bar before — he is not Pix; he can actually do the job." — `Appendix_D_-_Running_the_Tavern.md:197`
- "Functionally competent." — `03-staff-and-hiring.md:48`
- "DC 14 Insight detects that his professional confidence is real but his interest in the job is not" — `Appendix_D_-_Running_the_Tavern.md:199`

**G3. What he dislikes or despises**
- "mild contempt for patrons who volunteer everything" — `13-tobrin-ashvale.md:13`
- "Contempt for patrons who overshare never reaches his voice." — `voices/xanathars-guild.md:233`

**G4. What he wants (stated)**
- "I like the North Ward. Quiet. I'm looking for something steady." — `03-staff-and-hiring.md:48` and `Appendix_D_-_Running_the_Tavern.md:194` (both are interview lines; hire-time)
- "wants to maintain a running intelligence file on Trollskull's patrons, visitors, and overheard conversations" — `13-tobrin-ashvale.md:15`
- "keep the bar warm enough that no one suspects the bartender" — `13-tobrin-ashvale.md:15`

**G5. Private self**
- "the flat calm he allows himself only when alone" — `13-tobrin-ashvale.md:13`
- "Never: He never shows the flat calm in public, never asks directly about the party's plans, and never forgets a name." — `voices/xanathars-guild.md:236`
- "To those he trusts (meaning no one)" — `13-tobrin-ashvale.md:21`
- "Deep down, he is one of two Guild plants in the building, the one with better social access, and he is waiting to see how long it takes anyone to notice either of them." — `13-tobrin-ashvale.md:21`

**G6. Watchfulness and pressure (the sourced inner strain)**
- "DC 14 Insight detects watchful quality behind professional calm." — `03-staff-and-hiring.md:48`
- "DC 14 Insight detects that his professional confidence is real but his interest in the job is not — there is a watchful quality behind his eyes that does not match the casual manner." — `Appendix_D_-_Running_the_Tavern.md:199`
- "He is forgettable in the precise way that suggests effort has gone into it" — `Appendix_D_-_Running_the_Tavern.md:194`; "Deliberately forgettable — medium height, build, hair, clothes." — `03-staff-and-hiring.md:48`
- "In a fight, Tobrin does not fight." — `13-tobrin-ashvale.md:23`

**G7. Grudges and obligations**
- "his Guild debt" — `13-tobrin-ashvale.md:23`. No source for what it is (F7).
- None found against any named person.

**G8. Losses**
- None found.

**G9. Places he cares about**
- "I like the North Ward. Quiet." — `03-staff-and-hiring.md:48` (interview line, hire-time)
- No other place found.

**G10. People he cares about**
- None found. The only named person is Grevik Nass, as a fellow plant ("alongside Grevik Nass", `13-tobrin-ashvale.md:25`; "alongside Tobrin Ashvale", `12-grevik-nass.md:25`). No source says they are friends.

**G11. Fears**
- None found. The sourced behavior under threat: "In a fight, Tobrin does not fight." (`13-tobrin-ashvale.md:23`). The voice profile has no fear line.

**G12. Inspirations (not facts about Tobrin)**
- "channel Sam Malone (*Cheers*), Varys (*Game of Thrones*), and Tom Ripley (*The Talented Mr. Ripley*)." — `13-tobrin-ashvale.md:17`. These are acting references for the drafter, not sourced facts about his life.

---

## H. Cross-page consistency across the thirteen Xanathar's Guild pages

Method: the Summary and Affiliation lines of all thirteen pages (`campaign/setting/notable-figures/xanathars-guild/`), plus the dates and names that the pages cross-check. Line numbers are from the current files. Pages 11, 12 and 13 have no `> Structuring draft.` banner, so their summary is at line 5 and their affiliation at line 6.

### H1. Summary and affiliation lines

| File | Summary line (exact) | Affiliation line (exact) |
|---|---|---|
| 01-xanathar.md | L7: "- *Beholder crime lord, lawful evil, it/its*. Stat block: **Beholder**." | L8: "- **Affiliation:** Xanathar's Guild" |
| 02-ahmaergo.md | L7: "- *Shield dwarf majordomo, lawful evil, he/him*. Stat block: **Thug (with modifications)**." | L8: "- **Affiliation:** Xanathar's Guild" |
| 03-narl-xibrindas.md | L7: "- *Drow mage, neutral evil, he/him*. Stat block: **Mage**." | L8: "- **Affiliation:** Xanathar's Guild (secretly Bregan D'aerthe)" |
| 04-nihiloor.md | L7: "- *Mind flayer, lawful evil, it/its*. Stat block: **Mind Flayer**." | L8: "- **Affiliation:** Xanathar's Guild" |
| 05-noska-urgray.md | L7: "- *Shield dwarf enforcer, neutral evil, he/him*. Stat block: **Thug (with modifications)**." | L8: "- **Affiliation:** Xanathar's Guild" |
| 06-ott-steeltoes.md | L7: "- *Dwarf cult fanatic (Zuggtmoy), neutral evil, he/him*. Stat block: **Cult Fanatic**." | L8: "- **Affiliation:** Xanathar's Guild" |
| 07-thorvin-twinbeard.md | L7: "- *Dwarf engineer (secret Harper), neutral good, he/him*. Stat block: **Spy**." | L8: "- **Affiliation:** Xanathar's Guild (secretly the Harpers)" |
| 08-keln-trigos.md | L7: "- *Tiefling priest (Xanathar's Guild), neutral evil, he/him*. Stat block: **Priest**." | L8: "- **Affiliation:** Xanathar's Guild" |
| 09-grinda-garloth.md | L7: "- *Illuskan human mage (black market armorer), chaotic neutral, she/her*. Stat block: **Mage**." | L8: "- **Affiliation:** Independent (contractor to Xanathar's Guild and Bregan D'aerthe)" |
| 10-korgstrod-uxgulm.md | L7: "- *Duergar (second response team leader), lawful evil, he/him*. Stat block: **Duergar**." | L8: "- **Affiliation:** Xanathar's Guild" |
| 11-gorath.md | L5: "- *Duergar (first response team leader), lawful evil, he/him*. Stat block: **Duergar**." | L6: "- **Affiliation:** Xanathar's Guild" |
| 12-grevik-nass.md | L5: "- *Half-orc cook, neutral evil, he/him*. Stat block: **Spy**." | L6: "- **Affiliation:** Xanathar's Guild" |
| 13-tobrin-ashvale.md | L5: "- *Chondathan human bartender, neutral evil, he/him*. Stat block: **Spy**." | L6: "- **Affiliation:** Xanathar's Guild" |

Pronouns agree with the prose on every page checked. Xanathar and Nihiloor use "it/its". Grinda uses "she/her". The others use "he/him".

### H2. Format and naming differences

- **Banner.** Pages 11 (Gorath), 12 (Grevik) and 13 (Tobrin) have no `> Structuring draft.` line at line 3. Pages 01 to 10 have it.
- **"Shield dwarf" against "Dwarf".** Ahmaergo (`02-ahmaergo.md:7`) and Noska (`05-noska-urgray.md:7`) read "Shield dwarf". Ott (`06-ott-steeltoes.md:7`) and Thorvin (`07-thorvin-twinbeard.md:7`) read "Dwarf". The adventure says "shield dwarf" for Ott (`sources/adventure-wdh.json:32508`). Naming is inconsistent across the folder.
- **Stat-block labels.** "Thug (with modifications)" (02, 05), "Cult Fanatic" (06), "Spy" (07, 12, 13), "Priest" (08), "Mage" (03, 09), "Mind Flayer" (04), "Duergar" (10, 11), "Beholder" (01). Ott's "Cult Fanatic" differs from the Appendix C label "**Shield Dwarf Scout**" (`sources/Appendix_C_-_Player_Faction_Missions.md:1555`).
- **Xanathar's name for the 1372 DR beholder.** `01-xanathar.md:25` spells it "Kirukeskai" (wiki spelling). The Guild page spells it "Kirukesai" (`campaign/setting/organizations/08-xanathars-guild.md:20`). The Xanathar page notes the difference itself.

### H3. Dates and years

- **Nar'l, 1491 DR.** Consistent: `01-xanathar.md:37` ("Bregan D'aerthe placed Nar'l Xibrindas in the Guild in 1491 DR, a year before the campaign."); `01-xanathar.md:59` ("since 1491 DR, its only one"); `03-narl-xibrindas.md:18` ("In 1491 DR, a year before the campaign, Jarlaxle gave Nar'l the difficult task of infiltrating Xanathar's Guild"); `03-narl-xibrindas.md:73` ("reporting via Sending spell after one year in place, placed in 1491 DR."). Stale notes outside the Notable Figures pages: `03-narl-xibrindas.md:130` cites `quests/faction-events/bregan-daerthe/m04-the-compromised-eye/design-notes.md:16` for "three years", and `01-xanathar.md:157` cites `campaign/structure/arc-f-xanathars-lair.md:169` for "eleven months".
- **Nihiloor, four months.** Consistent: `01-xanathar.md:106` ("which has psionically dominated Xanathar for the last four months without Xanathar knowing"); `04-nihiloor.md:78` ("has dominated Xanathar's mind for the last four months").
- **Envoys, about Nightal 1491 DR (derived).** Consistent with the Guild page (`08-xanathars-guild.md:25`) and Ott (`06-ott-steeltoes.md:24`, "About Nightal 1491 DR (derived)").
- **Thorvin's years.** Conflict inside the folder. `07-thorvin-twinbeard.md:22`: "He is a paid Harper informant and has been one for three years." `07-thorvin-twinbeard.md:77`: "To those who earn his trust, he has been a Harper informant for three years". `07-thorvin-twinbeard.md:60`: "*An irritable dwarf engineer who hates his work and has kept a Harper secret for three years.*" The page's own note at `07-thorvin-twinbeard.md:130` says "The Lair structure notes say six (`arc-f-xanathars-lair.md:31` and `:91`)." And `07-thorvin-twinbeard.md:101` and `:121` give "nine years as engineer" (from `arc-f-xanathars-lair.md:91`).
- **Ahmaergo, 1368 DR.** `02-ahmaergo.md:122`: "`history/02-the-long-shadow.md:148` says the wiki names Ahmaergo "a slaver leader in 1368 DR". The wiki copies held here carry no 1368 DR entry for him." Not verified by this research.
- **Ott, age.** `06-ott-steeltoes.md:125`: "Age. Appendix C gives "a shield dwarf of approximately fifty years" (`Appendix_C_-_Player_Faction_Missions.md:1549`), which cannot hold with the wiki's 1357 DR Councilor entry. The page states no age."
- **Grinda, Mistshore fire.** `09-grinda-garloth.md:16`: "A fire in Mirtul 1491 DR burned most of Mistshore, and most of its buildings still stand burned and abandoned (**Dock Ward**)." No conflict found.
- **Zushaxx, 1466 DR.** Consistent: `01-xanathar.md:23` ("Izulktur replaced itself with Zushaxx about 1466 DR") and `campaign/setting/organizations/08-xanathars-guild.md:21` ("About 1466 DR, Zushaxx.").

### H4. Affiliation and placement

- **Tobrin and Grevik are the two Trollskull plants.** Both use present tense ("embedded as the tavern's bartender", `13-tobrin-ashvale.md:25`; "embedded as the tavern's Master Cook candidate", `12-grevik-nass.md:25`), but the Guild page Draft Notes say "The placements happen when the party hires staff." (`08-xanathars-guild.md:196`). Both pages are out of step with the Guild page on timing (D2).
- **Ott, the page already in the new shape.** The Ott page has `## Background`, `## Personality`, `## Connections`, `## Overview`, `## Roleplaying Information` and `### Voice` (`06-ott-steeltoes.md:14`, `:36`, `:44`, `:52`, `:56`, `:66`). A search for `^## Background|^### Voice|^## Personality|^## Connections` matched 11 of the 13 pages. Only Grevik (`12`) and Tobrin (`13`) did not match. The drafter should check the current shape of the other pages before using them as models. Tobrin is still in the old shape.
- **Ott's pilot citations are stale.** The Ott pilot notes cite the Ott page at lines 5, 6, 7, 21, 25 and 29. The current file has the summary at line 7, the Featured-in line at line 10 (`06-ott-steeltoes.md:10`, including "**Force Grey Mission 4 — Destroy the Intellect Factory**"), and a rewritten Relationships at line 89. The Ott notes are out of date, not the page.
- **Ahmaergo's Featured-in line.** The Ott page's Draft Notes say "`02-ahmaergo.md:7` carries the same bullet". The current line is `02-ahmaergo.md:10` ("**Featured in:** **Faction Outposts**, **Xanathar's Lair**, **Vault of Dragons**, **The Compromised Eye**, **The Dive**, **Force Grey Mission 4 — Destroy the Intellect Factory**").
- **Nar'l's affiliation.** `03-narl-xibrindas.md:8`: "- **Affiliation:** Xanathar's Guild (secretly Bregan D'aerthe)". Matches the Guild page (`08-xanathars-guild.md:102`, "secret Bregan D'aerthe asset").
- **Thorvin's affiliation.** `07-thorvin-twinbeard.md:8`: "- **Affiliation:** Xanathar's Guild (secretly the Harpers)". Matches the Guild page (`08-xanathars-guild.md:106`, "Dwarf engineer (secret Harper)").
- **Grinda's affiliation.** `09-grinda-garloth.md:8`: "- **Affiliation:** Independent (contractor to Xanathar's Guild and Bregan D'aerthe)". Matches the Guild page (`08-xanathars-guild.md:108`, "Independent black market armorer"). The Factions Guide calls her "Xanathar's black market armorer" (`campaign/guides/factions/09-xanathars-guild.md:41`, cited in the Guild page's notes). Stale in the Factions Guide.

### H5. Other cross-page checks

- Keln Trigos (`08-keln-trigos.md:7`): "Tiefling priest (Xanathar's Guild), neutral evil, he/him". Matches the Guild page (`08-xanathars-guild.md:107`, "Tiefling priest (Xanathar's Guild), neutral evil").
- Korgstrod (`10-korgstrod-uxgulm.md:7`): "Duergar (second response team leader), lawful evil, he/him". Matches the Guild page (`08-xanathars-guild.md:109`, "Duergar, lawful evil."). The Guild page calls him the "Duergar leader of the sewer hideout beneath Orb Confectioners" (`08-xanathars-guild.md:109`).
- Gorath (`11-gorath.md:5`): "Duergar (first response team leader), lawful evil, he/him". Matches the Guild page (`08-xanathars-guild.md:110`, "Duergar, lawful evil.").
- Grevik (`12-grevik-nass.md:5`): "Half-orc cook, neutral evil, he/him". Matches the Guild page (`08-xanathars-guild.md:111`, "Half-orc cook, neutral evil.") and the staff guide (`03-staff-and-hiring.md:107`, "NE half-orc"). Appendix D (`Appendix_D_-_Running_the_Tavern.md:501`): "NE male half-orc, Commoner."
- Xanathar's summary (`01-xanathar.md:7`): "it/its". Matches the Guild page.

---

## Not found

Terms and files searched.

- `Tobrin`, `Ashvale`, `bartender`, `Pix` across `/home/user/waterdeep` (`campaign/`, `sources/`, `docs/`, `.claude/`, the session handoffs). Hits are listed in E and in the cross-references below.
- `sources/adventure-wdh.json`: `Tobrin|Ashvale|bartender`: no matches.
- Wiki: `scratchpad/fandom-dump/forgottenrealms_pages_current.xml` for `Tobrin|Ashvale`: no matches. `sources/research/` for `Tobrin|Ashvale`: matches only in the campaign-hits snapshots (E2).
- `sources/SOURCE_GUIDE.md`: `Tobrin|Ashvale`: no matches. `Appendix D|Trollskull` lines matched (`:23`, `:58`, `:608`-`:621`, `:734`).
- `sources/Other remix files/`: `Tobrin|Ashvale` count 0. The .docx files cannot be opened (see Not readable).
- `campaign/guides/factions/09-xanathars-guild.md`: `Trollskull|plant|tavern|staff|Tobrin|Grevik` matched only `:21` and `:55` (Terasse Estate lines).
- `campaign/locations/trollskull-manor/area-overview.md`: `North Ward|Castle Ward|Dock Ward`: no matches.
- Pronoun and tenure searches over `campaign/setting/notable-figures/xanathars-guild/`: no Tobrin lines beyond pages 12 and 13.
- "Pix" appears only at `Appendix_D_-_Running_the_Tavern.md:197`. No Pix candidate is in Appendix D's candidate list or in the campaign staff guide. Unexplained.
- Family, loves, losses, fears, and grudges with named people for Tobrin: none found (G).
- Origin, age, faith, rank, joining date, the Dock Ward contact's name, the three Castle Ward establishments' names, and the Guild debt: none found (F).
- Tobrin in the Factions Guide, the Villains pages, the history pages or the lore pages: none found (the search covered `campaign/` as a whole).

## Not readable

- `sources/27. Addendum A Night in Trollskull Manor.pdf` was read as rendered images (PDF pp.1-4 only). No `pdftotext` run. PDF pp.5 onward were not read. The staff tables may sit later in the Addendum, or in the Alexandrian Appendix F that `campaign/structure/arc-b-trollskull-alley.md:207` cites. Check with `pdftotext -layout` before any quote goes into prose.
- `sources/Other remix files/*.docx` were not opened. `Lif and the Haunting of Trollskull Manor.docx` (`SOURCE_GUIDE.md:691`) is the likeliest to mention tavern staff.
- `scratchpad/fandom-dump/frwiki.xml.7z` is compressed and was not searched.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
