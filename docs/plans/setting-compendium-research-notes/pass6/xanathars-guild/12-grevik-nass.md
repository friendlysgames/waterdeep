# Pass 6 research notes: Grevik Nass

Page: `campaign/setting/notable-figures/xanathars-guild/12-grevik-nass.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 16; ruling 15 Background; ruling 17 personal goals as relayed by the coordinator)
Ruling used: Ches 1, 1492 DR. Grevik is a Xanathar's Guild operative with no Ches 1 post. He is placed in Trollskull Manor only when the party opens the Master Cook post. That placement is a quest event and is routed, not day-one (see C and D).

Method and caveats:
- Campaign files: Read and Grep, quoted from the tool output. Line numbers come from the tool output.
- Published adventure: `sources/adventure-wdh.json`. Grep for `Grevik`, `Nass`, `Master Cook`, `cook`, `kitchen`, `bartender`, `barmaid`, `employ` and `Trollskull` returned no Grevik line. Quoted adventure lines are kept as written.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. PDF quotes were transcribed from the rendered page images. Cite as printed page with PDF page in brackets. Check exact wording with `pdftotext -layout` before any quote goes into prose.
- Alexandrian markdown: `sources/Appendix_D_-_Running_the_Tavern.md` is the Alexandrian Trollskull appendix and is the only Alexandrian source that names Grevik. `sources/Appendix_C_-_Player_Faction_Missions.md` and `sources/Act_III_Arc_E.md` have no Grevik line.
- Wiki: none. `scratchpad/wiki-xg/Grevik_Nass.txt` reads `NOT FOUND`. No match in `sources/research/**` for `Grevik` or `Nass` except campaign-hits copies of the campaign page (see E).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## A. Background facts by theme

Every fact below is from a non-wiki source. The wiki has nothing on Grevik.

### A1. Origin, birth, family, home

No source gives birthplace, family, clan, home ward or upbringing. Gaps are listed in F2.

Only the species, sex and the claim of experience are given:

> "*NE male half-orc, Commoner. A Xanathar Guild information broker using chef work as cover.*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:501`

> "| 5 | **Grevik Nass** | NE half-orc | Large, moves deliberately to compensate for his size — he's learned that moving slowly makes people less nervous." (rest of the row is quoted in A4 and D2)
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`

### A2. Former life and skill (cooking)

The only past fact is his own claim in the interview. The Alexandrian text presents it as his statement, so the drafter should keep it as his claim.

> "He is large even for a half-orc, with the careful, deliberate movements of someone who has learned that his size makes people nervous and has decided to compensate by moving slowly. He speaks quietly. His references are from two Dock Ward establishments and one in the Field Ward. He has brought a sample — a braised pork dish with a sauce that is, objectively, very good. \"I know I don't look like a chef,\" he says, without resentment. \"But I've been cooking professionally for eight years. I like the work. It suits me.\" He holds your gaze steadily. There is something practiced about the steadiness."
> — `sources/Appendix_D_-_Running_the_Tavern.md:504` (readaloud block, inside `<div class="fvtt narrative">`, lines 503-505)

> "Genuine skill (the Guild chose him partly because a mediocre plant draws attention)."
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:107` (Faction Note cell and Effect cell, same row)

> "**Hidden Quality:** DC 15 Insight detects the practiced steadiness. DC 16 Investigation of his Field Ward reference turns up a connection to a business that the characters may recognize from their faction work as a Xanathar front."
> — `sources/Appendix_D_-_Running_the_Tavern.md:509` (the business is not named in any file, see F2)

Context: the eight years is an interview claim. No file checks it.

### A3. How he joined the Guild and what the Guild gave him

Guild-wide entry rule (not Grevik-specific):

> "**Crime Is the Entry Fee:** Anyone can join, but an applicant must first pass a test that always involves a serious crime."
> — `campaign/setting/organizations/08-xanathars-guild.md:32`

> "**Recruiting.** Anyone can join, and the applicant must pass the test of a serious crime. A member who is given an assignment may receive a monstrous bodyguard, a gazer or access to the Guild's secret tunnels and hidden cellars, which serve as safe houses (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:67`

Grevik-specific:

> "Xanathar's Guild information broker using chef work as cover. Reports through a kitchen supplier, not through normal channels."
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:107` (Faction Note cell)

> "He is genuinely skilled — the Guild selected him in part because a mediocre chef draws attention. He is not here to poison anyone or cause direct harm; he is here to listen. The Guild wants to know who frequents the tavern, what faction business gets discussed within earshot of the kitchen pass-through, and whether the characters are worth monitoring. He files reports through a kitchen supplier (not a Vintners' Guild contact) who collects them with the weekly delivery."
> — `sources/Appendix_D_-_Running_the_Tavern.md:507`

> "**Faction Note:** Xanathar Guild information broker — an adversary faction, not available to player characters. There is no version of this hiring where Grevik is on the party's side. He is here because Xanathar has decided the party is worth monitoring, and the Guild places assets quietly rather than asking permission."
> — `sources/Appendix_D_-_Running_the_Tavern.md:511`

No line gives a date, a recruiter, a first job or a Guild rank for Grevik.

### A4. Posting and the hiring path

> "When a position is open, candidates 1–4 arrive the next day, in table order. Candidate 5 arrives on the fourth day if the position is still open."
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:34`

> "| 5 | **Grevik Nass** | NE half-orc | Large, moves deliberately to compensate for his size — he's learned that moving slowly makes people less nervous. Produces references from two Dock Ward establishments. Brings a braised pork sample — it holds up. \"I know I don't look like a chef.\" Holds the party's gaze steadily — just slightly too long. DC 15 Insight detects the practiced steadiness behind the calm. DC 16 Investigation of the Field Ward reference reveals it is a Xanathar's Guild front. Genuine skill (the Guild chose him partly because a mediocre plant draws attention). | Xanathar's Guild information broker using chef work as cover. Reports through a kitchen supplier, not through normal channels. After 2 tendays: Guild has full patron profile of the tavern. No version of this benefits the party if they don't catch him. | 14 gp | +3 Revenue. After 2 tendays: Guild has patron profile and party schedule. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:107` (the table is under the heading at line 99)

> "**Master Cook Candidates (14 gp/tenday)**"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:99`

> "When the characters decide to hire for any position, word spreads through the guilds and the alley within a day. The following candidates turn up for each role. The DM should choose which candidates appear based on what the campaign needs, or roll 1d4 among options 1–4, with option 5 always appearing last if the position hasn't been filled after three days."
> — `sources/Appendix_D_-_Running_the_Tavern.md:83` (conflicts with line 34 above, see D3)

> "The placements happen when the party hires staff."
> — `campaign/setting/organizations/08-xanathars-guild.md:196` (Draft Notes, inside the quoted routed bullet)

Context: no source places Grevik in the tavern, a Dock Ward house or any other place on Ches 1.

### A5. Relationships to named figures

Tobrin Ashvale is the only named figure tied to Grevik:

> "- **Grevik Nass**, **Tobrin Ashvale** (Notable Figures): Guild operatives"
> — `campaign/setting/organizations/08-xanathars-guild.md:162`

> "> - **Routed to quests (ruling 28):** Secret, the plants: \"Grevik Nass and Tobrin Ashvale are the Guild's two plants among the staff of Trollskull Manor. Each keeps a file on the tavern's patrons.\" The placements happen when the party hires staff. They live in `campaign/guides/trollskull-manor/03-staff-and-hiring.md` (lines 48 and 107), in `09-response-teams-at-the-tavern.md:23`, and in their Notable Figures pages (`12-grevik-nass.md:25`, `13-tobrin-ashvale.md:21`, `:25`)."
> — `campaign/setting/organizations/08-xanathars-guild.md:196`

> "**Relationships.** Tobrin is an operative of Xanathar's Guild embedded as the tavern's bartender, one of the Guild's two Trollskull infiltrators alongside Grevik Nass, and the trigger for the Guild's escalating response conditions (detailed in the **Trollskull Manor** guide); when the party crosses a threshold, Tobrin makes the call."
> — `campaign/setting/notable-figures/xanathars-guild/13-tobrin-ashvale.md:25`

> "| 5 | **Tobrin Ashvale** | NE Chondathan human | Deliberately forgettable — medium height, build, hair, clothes. Glances around the taproom with the casual interest of someone memorizing a room. \"I like the North Ward. Quiet. I'm looking for something steady.\" Functionally competent. DC 14 Insight detects watchful quality behind professional calm. DC 16 Investigation of one Castle Ward reference reveals it has been under Xanathar's Guild protection for two years. If dismissed: Guild sends a replacement within 3 tendays — not bar staff this time. | Xanathar's Guild watcher. No combat mission; reporting role only. No version of his employment benefits the party. | 10 gp | No Revenue bonus. After 2 tendays: Guild has patron profile and party schedule. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:48`

No source ties Grevik to Ahmaergo, Nar'l, Noska, Gorath, Keln Trigos, Nihiloor or Xanathar. Tobrin's Appendix D entry gives the Guild's reason for placing watchers in tavern staff:

> "He is here because the Xanathar Guild places low-level watchers in North Ward establishments when those establishments become points of interest."
> — `sources/Appendix_D_-_Running_the_Tavern.md:197` (Tobrin, not Grevik; the general placement rule)

### A6. Rank and ladder

> "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:45`

Grevik is not placed on the ladder. The Guild page calls him "Half-orc cook, neutral evil." (`campaign/setting/organizations/08-xanathars-guild.md:111`). The Alexandrian appendix calls him "information broker" (`sources/Appendix_D_-_Running_the_Tavern.md:501`).

### A7. Faith, signature belongings, how long in post

- Faith: no source.
- Signature belongings: no source. The only object is the braised pork sample brought to the interview (`sources/Appendix_D_-_Running_the_Tavern.md:504`), which is a hiring prop.
- How long in post: "After 2 tendays: Guild has full patron profile of the tavern." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`). This counts from hire, not from his Guild career.

---

## B. Alignment, species, pronouns, stat block

**Alignment: neutral evil (consistent)**
- Page: "> - *Half-orc cook, neutral evil, he/him*. Stat block: **Spy**." — `campaign/setting/notable-figures/xanathars-guild/12-grevik-nass.md:5`
- Guild page: "- **Grevik Nass** — Half-orc cook, neutral evil. See the **Grevik Nass** page in Notable Figures." — `campaign/setting/organizations/08-xanathars-guild.md:111`
- Alexandrian: "*NE male half-orc, Commoner. A Xanathar Guild information broker using chef work as cover.*" — `sources/Appendix_D_-_Running_the_Tavern.md:501`
- Campaign staff table: "| 5 | **Grevik Nass** | NE half-orc |" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`

**Species: half-orc (consistent)**
- Page: `12-grevik-nass.md:5` ("Half-orc cook").
- Guild page: `08-xanathars-guild.md:111` ("Half-orc cook").
- Alexandrian: "He is large even for a half-orc" (`sources/Appendix_D_-_Running_the_Tavern.md:504`).
- Campaign staff table: "NE half-orc" (`03-staff-and-hiring.md:107`).
- Gruumsh page: "> - **Pronouns checked:** Yagra (she/her), Ziraj (he/him), Hrabbaz (he/him), Grevik Nass (he/him) and Sister Valdra (she/her) come from their Notable Figures pages and the event files." — `campaign/setting/deities/gruumsh.md:131`
- No file says "shield dwarf", "gnome" or any other species for Grevik.

**Pronouns: he/him (sourced)**
- "NE male half-orc" (`sources/Appendix_D_-_Running_the_Tavern.md:501`)
- "He is large even for a half-orc" (`:504`)
- "he's learned that moving slowly makes people less nervous" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`)
- Page: "he/him" (`campaign/setting/notable-figures/xanathars-guild/12-grevik-nass.md:5`)

**Affiliation: Xanathar's Guild (consistent)**
- Page: "> - **Affiliation:** Xanathar's Guild" — `12-grevik-nass.md:6`
- Alexandrian: "A Xanathar Guild information broker using chef work as cover." (`sources/Appendix_D_-_Running_the_Tavern.md:501`)
- Campaign: "Xanathar's Guild information broker using chef work as cover." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`)

**Stat block: label conflict (no source for the page's label)**
- Page: "Stat block: **Spy**." — `12-grevik-nass.md:5`
- Alexandrian: "*NE male half-orc, Commoner.*" — `sources/Appendix_D_-_Running_the_Tavern.md:501`
- No Trollskull guide entry gives a stat block. The "Spy" label follows the page convention used by other figures and has no source for Grevik.

---

## C. Every sentence on the current page

Current page: `campaign/setting/notable-figures/xanathars-guild/12-grevik-nass.md`. "Day-one OK" means no quest gate is needed. "Quest-time" means the sentence needs a hire, a discovery or a trigger.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Half-orc cook, neutral evil, he/him*. Stat block: **Spy**." | Day-one. "Spy" unsourced (B) | `organizations/08-xanathars-guild.md:111`; `Appendix_D:501` |
| 2 | L6 | "**Affiliation:** Xanathar's Guild" | Day-one OK | `organizations/08-xanathars-guild.md:111` |
| 3 | L7 | "**Featured in:** Background figure; no scripted appearance." | Conflicts with the Trollskull trigger that names him (D7) | `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:23`; `sources/Appendix_D_-_Running_the_Tavern.md:1521` |
| 4 | L11 | "**Resonance.** Grevik should inspire immediate comfort with his competence and no-fuss manner, and retroactive unease when the party discovers the kitchen window takes in every table." | "when the party discovers" is quest-time. "kitchen window" has voice support; "takes in every table" has none | Discovery: `sources/Appendix_D_-_Running_the_Tavern.md:511` ("the clues are there if they look (DC 16 Investigation)"); "kitchen window": voice `character-voices/voices/xanathars-guild.md:217`; "kitchen pass-through": `Appendix_D:507` |
| 5 | L13 | "**Emotions.** Grevik most often feels professional pride in clean work, patient attention to patron patterns, quiet contempt for sloppiness, calm deliberateness, and genuine satisfaction when a dish lands exactly right. Underneath all of it sits background guilt he does not examine." | Day-one in form. Cause of guilt unsourced (G1). Voice lists the guilt at `voices/xanathars-guild.md:216` | Voice: `:216` |
| 6 | L15 | "**Motivations.** Grevik wants to compile an accurate patron intelligence file for Xanathar's Guild (who dines here, with whom, and about what), make the food worth recommending so no one looks closely at the cook, and complete the assignment without drawing a replacement." | "compile ... file" day-one in intent (`Appendix_D:507`; `organizations/08-xanathars-guild.md:196` says "Each keeps a file"). "complete the assignment without drawing a replacement": no source | `Appendix_D:507`; "file": `08-xanathars-guild.md:196` |
| 7 | L17 | "**Inspirations.** When playing Grevik, channel Gustavo Fring (*Breaking Bad*), Thomas Barrow (*Downton Abbey*), and The Operative (*Serenity*)." | Not a fact | n/a |
| 8 | L21 (a) | "**Persona.** To the world, Grevik is a half-orc cook who lets the food do the talking: attentive to the pass, quiet at the bar, no trouble to manage." | Day-one OK. "quiet at the bar" has no source; the voice gives "behind the pass" | `Appendix_D:504` ("He speaks quietly"); voice `:215` |
| 9 | L21 (b) | "To those who work alongside him, he notes which tables order twice, which guests lower their voices, and which visitors he sees again without a reservation." | Day-one in kind; no source for these habits. Voice gives "calls patrons by their tables" (`:214`) and "watches the room" (`:217`) | `voices/xanathars-guild.md:214`, `:217` |
| 10 | L21 (c) | "Deep down, he has filed more detailed intelligence from this kitchen than the Guild expected, and the thought that the tally might make him harder to release than to retire has started to surface at quiet moments." | Day-one in attitude but no source; "filed ... than the Guild expected" implies a time in post and is unsourced | None (G1) |
| 11 | L23 | "**Morale.** In a fight, Grevik yields position, retreats through the kitchen, and gets a runner to the Guild within the hour. He is an intelligence operative and fights nothing he can avoid." | "runner to the Guild" has no source. Reporting channel in the sources is a weekly kitchen supplier (D5) | `Appendix_D:507` (channel) |
| 12 | L25 (a) | "**Relationships.** Grevik is an operative of Xanathar's Guild embedded as the tavern's Master Cook candidate" | Affiliation is day-one. "embedded as the tavern's Master Cook candidate" is quest-time: the candidate arrives only when the Master Cook post is open | `campaign/guides/trollskull-manor/03-staff-and-hiring.md:34`, `:99`, `:107`; routing `organizations/08-xanathars-guild.md:196` ("The placements happen when the party hires staff.") |
| 13 | L25 (b) | "a man whose two-tenday file will give Xanathar a usable picture of Trollskull's patronage," | Quest-time: "two-tenday" counts from hire | `03-staff-and-hiring.md:107` ("After 2 tendays") |
| 14 | L25 (c) | "and one of two Guild plants in the tavern staff alongside Tobrin Ashvale, whose position behind the bar gives the Guild a second angle on the same room." | Quest-time: the staffing is a party choice. Two-plants fact is in the routed bullet | `organizations/08-xanathars-guild.md:196`; `13-tobrin-ashvale.md:25` |
| 15 | L29 | "Grevik Nass is a half-orc cook whose food is worth recommending and who keeps entirely to himself behind the pass." | Day-one OK. Overview has no quest content. "keeps entirely to himself" is unsourced | `Appendix_D:504` ("He speaks quietly.") |
| 16 | L29 | "He is attentive and professional, and lets the work do the talking." | Day-one OK. Unsourced in wording; voice supports `:213` ("He doesn't make small talk and deflects personal questions with food.") | `voices/xanathars-guild.md:213` |

### C2. Quest-time clauses in the voice profile

Voice profile: `.claude/skills/character-voices/voices/xanathars-guild.md:209-223`. Quest-time clauses: **none found**. Every line describes a standing habit or a pre-quest state (kitchen speech, table numbers, the kitchen window, what he never does). The only event-shaped line is the sample "*Business:* \"Big party tomorrow? I'll need to know numbers. Who's coming?\"" (`voices/xanathars-guild.md:222`), which is ordinary kitchen talk and is not a trigger.

---

## D. Conflicts

Rank used: campaign files first, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki. The adventure has no Grevik, so it does not rank in any of these conflicts.

**D1. Stat block: "Spy" against "Commoner"**
- Page: "Stat block: **Spy**." — `campaign/setting/notable-figures/xanathars-guild/12-grevik-nass.md:5`
- Alexandrian: "*NE male half-orc, Commoner.*" — `sources/Appendix_D_-_Running_the_Tavern.md:501`
- Higher source: neither ranks above the other for a stat label. The campaign page is the page being written. Orchestrator decides.

**D2. Wage: 14 gp against 8 gp (inside the same Master Cook heading)**
- Campaign: "| 14 gp | +3 Revenue. After 2 tendays: Guild has patron profile and party schedule. |" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`
- Campaign heading: "**Master Cook Candidates (14 gp/tenday)**" — `03-staff-and-hiring.md:99`
- Alexandrian: "**Wage:** 8 gp/tenday." — `sources/Appendix_D_-_Running_the_Tavern.md:513`
- Alexandrian heading: "##### Master Cook Candidates (14 gp/tenday)" — `sources/Appendix_D_-_Running_the_Tavern.md:420`
- Higher source: the campaign guide (`03-staff-and-hiring.md:107`), which the Guild page routes to. The Alexandrian appendix is internally inconsistent (heading 14 gp, candidate 5 at 8 gp, also Maren Holst at 8 gp in `:492`).

**D3. Arrival timing for candidate 5**
- Campaign: "When a position is open, candidates 1–4 arrive the next day, in table order. Candidate 5 arrives on the fourth day if the position is still open." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:34`
- Alexandrian: "The DM should choose which candidates appear based on what the campaign needs, or roll 1d4 among options 1–4, with option 5 always appearing last if the position hasn't been filled after three days." — `sources/Appendix_D_-_Running_the_Tavern.md:83`
- Higher source: the campaign guide (`:34`). Day-count (fourth day against after three days) and the selection rule (table order against DM choice or 1d4) both differ.

**D4. When the Guild has the full picture**
- Campaign: "After 2 tendays: Guild has full patron profile of the tavern." — `03-staff-and-hiring.md:107`
- Alexandrian: "If employed for more than two tendays, the Xanathar Guild has a detailed picture of the tavern's patron traffic." — `sources/Appendix_D_-_Running_the_Tavern.md:515`
- Higher source: the campaign (`:107`). Minor: "after 2" against "more than two".

**D5. Reporting channel**
- Morale: "gets a runner to the Guild within the hour" — `campaign/setting/notable-figures/xanathars-guild/12-grevik-nass.md:23`
- Campaign and Alexandrian: "Reports through a kitchen supplier, not through normal channels." (`03-staff-and-hiring.md:107`); "He files reports through a kitchen supplier (not a Vintners' Guild contact) who collects them with the weekly delivery." (`sources/Appendix_D_-_Running_the_Tavern.md:507`)
- Higher source: the campaign and the Alexandrian both give a supplier channel with a weekly collection. The page's runner is an unsourced fight-time channel. Not necessarily a contradiction; the drafter should not state a runner as Guild procedure.

**D6. Role label: "cook" against "information broker"**
- Guild page: "- **Grevik Nass** — Half-orc cook, neutral evil." — `campaign/setting/organizations/08-xanathars-guild.md:111`
- Alexandrian: "A Xanathar Guild information broker using chef work as cover." — `sources/Appendix_D_-_Running_the_Tavern.md:501`
- Campaign staff: "Xanathar's Guild information broker using chef work as cover." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`
- Higher source: the campaign guide. Both are true at once in the sources (cook by trade, broker by Guild role); the page's "cook" label is the Guild page's wording.

**D7. "No scripted appearance" against a trigger that names him**
- Page: "**Featured in:** Background figure; no scripted appearance." — `campaign/setting/notable-figures/xanathars-guild/12-grevik-nass.md:7`
- Trollskull guide: "- A Guild plant as staff (Tobrin Ashvale, Grevik Nass) has been exposed" — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:23`
- Alexandrian: "- A Guild spy planted as staff (Tobrin Ashvale, Grevik Nass, or any similar candidate) has been exposed." — `sources/Appendix_D_-_Running_the_Tavern.md:1521`
- Higher source: the campaign guide. He does not appear in person, but a visit is triggered by his exposure. The page's Featured-in line should say so, or it is wrong.

**D8. Alexandrian PDF 27 cook roster against Appendix D**
- PDF 27, printed p.183 [PDF p.6], section "COOKS": the names are "Isgrigg & Dupere", "Turgattan Thornhammer" and "Reynardo Greenleaf" (transcribed from the page image; check with pdftotext). Grevik is not on this list. (PDF pages 1 to 20 were read; see Not readable.)
- Appendix D, the Master Cook candidates, names Grevik as candidate 5 (`sources/Appendix_D_-_Running_the_Tavern.md:500`), and the campaign guide follows Appendix D (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`).
- Higher source: the campaign guide. The two Alexandrian rosters differ, and only Appendix D names Grevik.

**D9. Field Ward reference**
- Appendix D gives "two Dock Ward establishments and one in the Field Ward" (`sources/Appendix_D_-_Running_the_Tavern.md:504`).
- Campaign gives "Produces references from two Dock Ward establishments." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`) and then the "Field Ward reference" that is a Guild front.
- Gazetteer: "a staff applicant whose Field Ward reference proves to be a Xanathar's Guild front." — `campaign/gazetteer/waterdeep/field-ward.md:9`
- Not a conflict on the references. Conflict-free, but no file names the Field Ward business (F2).

**D10. Species and alignment**: no conflict. All sources agree on half-orc and NE/neutral evil (B).

---

## E. Stale lines in other files (not to be edited), and routed references

### E1. Snapshots that disagree with the current page (not edited)

- `sources/research/pass3-bundles/guilds/campaign-hits.txt:825`–`:828` and `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:643`–`:644`: copies of the page's Motivations and Relationships lines. The pass 3 copy says "Master Cook candidate" in the same words. These are snapshots, not sources.
- `docs/plans/setting-compendium-research-notes/pass5/xanathars-guild.md` (Key Members check): records the page's `:5` and `:6` lines only.

### E2. Routed to quests (where the quest-time facts already live)

- Hire and placement: `campaign/guides/trollskull-manor/03-staff-and-hiring.md:34` (candidate arrival), `:99` (heading), `:107` (the row). Routing: `campaign/setting/organizations/08-xanathars-guild.md:196`.
- Exposure trigger: `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:21`–`:23` ("**Triggers:**" list). Alexandrian: `sources/Appendix_D_-_Running_the_Tavern.md:1519`–`:1521` ("**What triggers a visit:**" list).
- Discovery: `sources/Appendix_D_-_Running_the_Tavern.md:511` ("The DM should decide whether the party ever learns he was Guild — the clues are there if they look (DC 16 Investigation), but catching him requires initiative from the players, not a passive discovery.")
- Field Ward front (unnamed): `sources/Appendix_D_-_Running_the_Tavern.md:509`; `campaign/gazetteer/waterdeep/field-ward.md:9` and `:238` (the gazetteer's note on the same row, "The page repeats the Field Ward wording").

### E3. Other files that name Grevik

- `campaign/setting/organizations/08-xanathars-guild.md:111`, `:162`, `:196`
- `campaign/setting/notable-figures/xanathars-guild/13-tobrin-ashvale.md:25`
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`; `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:23`
- `campaign/gazetteer/waterdeep/field-ward.md:9`, `:238`
- `campaign/setting/deities/gruumsh.md:92`, `:111`, `:131` (Notable Figures list and pronouns)
- `.claude/skills/character-voices/SKILL.md:33` ("| `voices/xanathars-guild.md` | The Xanathar, Ahmaergo, Nar'l, Nihiloor, Noska, Ott, Thorvin, Keln, Grinda, Korgstrod, Gorath, Grevik, Tobrin |")
- `sources/Appendix_D_-_Running_the_Tavern.md:500`–`:515`, `:1521`
- `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:39` (copy of the field-ward gazetteer note)

No quest file, Faction Outposts file, Lair file or Factions Guide file names Grevik (see Not found).

### E4. Adjacent lines that are not Grevik (to avoid mixing)

- Rella Asp's "pass-through window" (Cassalanter, not Grevik): "Rella's placement gives them a kitchen-level view of who passes through and what is said within earshot of the pass-through window." — `sources/Appendix_D_-_Running_the_Tavern.md:446`
- The lair's own cooks (Xanathar, not Grevik): "**X30. Xanathar's Gourmet Kitchen**" at `sources/adventure-wdh.json:17942`; "All the meals prepared here are for the consumption of {@creature Xanathar|WDH} alone." at `:17955`; "**X31. The Other Kitchen**" at `:17970`; "Halfling Cook" at `:17984`.
- A female half-orc informant in Appendix C (not Grevik): "The half-orc had a tattoo of a winged snake on the back of her neck." — `sources/Appendix_C_-_Player_Faction_Missions.md:101`
- Wiki: `sources/research/pass5-bundles/xanathars-guild/wiki.txt:1373` ("[[Category:Inhabitants of Trollskull Alley]]") belongs to the **Avaereene** wiki page (the page starts at `:1276`), not to Grevik.

---

## F. Consistency constraints (sourced) and gaps

### F1. Sourced facts the drafter must stay consistent with

The drafter may add a Background and personal goals (ruling 15, ruling 17) but must not contradict these. Each is quoted with its line.

1. **Species, sex and alignment.** "NE male half-orc, Commoner." (`sources/Appendix_D_-_Running_the_Tavern.md:501`); "NE half-orc" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`).
2. **What he is for the Guild.** "A Xanathar Guild information broker using chef work as cover." (`sources/Appendix_D_-_Running_the_Tavern.md:501`). He is "genuinely skilled" (`:507`).
3. **Why the Guild picked him.** "the Guild selected him in part because a mediocre chef draws attention." (`sources/Appendix_D_-_Running_the_Tavern.md:507`)
4. **What he collects and how it leaves.** "The Guild wants to know who frequents the tavern, what faction business gets discussed within earshot of the kitchen pass-through, and whether the characters are worth monitoring. He files reports through a kitchen supplier (not a Vintners' Guild contact) who collects them with the weekly delivery." (`:507`)
5. **Who decided on him.** "He is here because Xanathar has decided the party is worth monitoring, and the Guild places assets quietly rather than asking permission." (`:511`). He is not on the party's side: "There is no version of this hiring where Grevik is on the party's side." (`:511`)
6. **His own claim of experience.** "But I've been cooking professionally for eight years." (`:504`). This is his claim in the interview. No file checks it.
7. **His cover story.** When confronted he "calmly admits that he 'has contacts in the Guild' but frames it as a necessary survival arrangement, not active employment. He is lying." (`:509`). The drafter may state this as his cover and the Guild's view.
8. **His references.** "two Dock Ward establishments and one in the Field Ward" (`:504`). The Field Ward business is not named in any source.
9. **He does not talk about the Guild.** "He never talks about the Guild, never serves bad food, and never lingers in the dining room." (`character-voices/voices/xanathars-guild.md:219`)
10. **Tobrin.** He is one of "the Guild's two Trollskull infiltrators alongside Grevik Nass" as Tobrin's page says (`campaign/setting/notable-figures/xanathars-guild/13-tobrin-ashvale.md:25`), and the Guild page says "Each keeps a file on the tavern's patrons." (`campaign/setting/organizations/08-xanathars-guild.md:196`).
11. **Hire-only posting.** "The placements happen when the party hires staff." (`:196`). Candidate 5 arrives only while the post is open (`03-staff-and-hiring.md:34`).
12. **Hire timeline.** "After 2 tendays: Guild has full patron profile of the tavern." (`03-staff-and-hiring.md:107`); "If employed for more than two tendays ..." (`Appendix_D:515`, D4).
13. **Exposure consequence.** "A Guild plant as staff (Tobrin Ashvale, Grevik Nass) has been exposed" triggers a visit (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:23`).
14. **Pronouns.** he/him, from the page, Appendix D and the staff row (B).

### F2. Gaps a Background would need, and a suggested modest inference for each

Each inference is tagged `[research]` in the Background. None is a plot fact. Where no inference is safe, the note says so.

1. **Birth, family, home ward, upbringing.** No source. Suggested: leave unnamed. Prefer nothing.
2. **Where he learned to cook.** Only "eight years" (`:504`). Suggested [research]: "trained in working kitchens for eight years before the Guild approached him." This keeps the eight years as his claim.
3. **How and when the Guild recruited him.** Only "the Guild selected him in part because a mediocre chef draws attention" (`:507`) and the general entry test (`08-xanathars-guild.md:32`). Suggested [research]: he passed the Guild's entry test, which "always involves a serious crime" (`:32`), and the crime is not named.
4. **Rank.** The ladder is at `08-xanathars-guild.md:45`; he is not placed. Suggested [research]: a Guild operative without a rung, since the Guild's own page calls him only "Half-orc cook".
5. **Relationship to Xanathar, Ahmaergo, Nar'l and the other lieutenants.** No source. Suggested: do not invent. The only handler named is the Guild in general (`:511`).
6. **The kitchen supplier who carries his reports.** Unnamed (`:507`). Suggested [research]: leave unnamed; it is the channel, not a person.
7. **The Field Ward front behind his reference.** Unnamed (`:509`). Not one of the three Xanathar outposts (Terasse Estate in the Castle Ward, Grinda Garloth's workshop in the Dock Ward, Orb Confectioners in the Southern Ward; `campaign/structure/arc-e-faction-outposts.md:137`). Suggested: leave it unnamed. Do not add a fourth outpost; the Factions Guide has none.
8. **Replacement procedure.** "without drawing a replacement" (page `:15`) has no source. Suggested: the drafter may keep it as Grevik's motivation (page text) and not as Guild rule.
9. **Morale runner.** "gets a runner to the Guild within the hour" (page `:23`) has no source (D5). Suggested: keep as the page's own text, tagged `[research]`.
10. **The guilt he does not examine.** Only "background guilt he does not examine" (`:13`) and the voice (`voices/xanathars-guild.md:216`). No cause. Suggested [research]: no cause given; the drafter should not name one.
11. **Faith.** No source. Suggested: none; leave out.
12. **Signature belongings.** No source beyond the interview pork sample (`:504`). Suggested: none.
13. **Age.** No source. "eight years" of cooking only. Suggested: none; do not state an age.
14. **Stat block label.** "Spy" (page) against "Commoner" (`Appendix_D:501`) (D1). Orchestrator decides.
15. **Wage.** 14 gp against 8 gp (D2). Orchestrator decides.
16. **Field Ward business and whether the party learns of it.** `:511` leaves it to the DM. Keep open.

---

## G. Inner-life hints (sourced and page-only)

Every item quotes the exact line. Items marked "page only" are on the current page with no source; the drafter may keep them as the page's wording but must not present them as sourced. Items marked "voice" are in the character-voices profile.

### G1. Fears, guilt, pressure

- Sourced, the cover story strain: "he calmly admits that he \"has contacts in the Guild\" but frames it as a necessary survival arrangement, not active employment. He is lying." (`sources/Appendix_D_-_Running_the_Tavern.md:509`)
- Sourced, the practiced calm: "There is something practiced about the steadiness." (`:504`); "DC 15 Insight detects the practiced steadiness behind the calm." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`)
- Voice, the guilt: "Guilt he doesn't examine surfaces as extra care with the party's food." (`voices/xanathars-guild.md:216`)
- Page only, guilt: "Underneath all of it sits background guilt he does not examine." (`campaign/setting/notable-figures/xanathars-guild/12-grevik-nass.md:13`)
- Page only, fear of being released: "Deep down, he has filed more detailed intelligence from this kitchen than the Guild expected, and the thought that the tally might make him harder to release than to retire has started to surface at quiet moments." (`:21`)
- Page only, flight: "In a fight, Grevik yields position, retreats through the kitchen, and gets a runner to the Guild within the hour. He is an intelligence operative and fights nothing he can avoid." (`:23`)

### G2. Habits and self-management

- Sourced, a learned habit of moving slowly: "with the careful, deliberate movements of someone who has learned that his size makes people nervous and has decided to compensate by moving slowly." (`sources/Appendix_D_-_Running_the_Tavern.md:504`); "moves deliberately to compensate for his size — he's learned that moving slowly makes people less nervous." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`)
- Sourced, a steady gaze held a little long: "Holds the party's gaze steadily — just slightly too long." (`03-staff-and-hiring.md:107`)
- Sourced, quiet speech: "He speaks quietly." (`Appendix_D:504`)
- Voice, deflection: "He doesn't make small talk and deflects personal questions with food." (`voices/xanathars-guild.md:213`)
- Voice, room-watching: "He calls orders by table number. He watches the room from the kitchen window while he talks." (`voices/xanathars-guild.md:217`)
- Voice, never speaks of the Guild: "He never talks about the Guild, never serves bad food, and never lingers in the dining room." (`voices/xanathars-guild.md:219`)
- Voice, signature lines: "Table four wants the lamb." / "Food's up." / "Joining anyone tonight?" (`voices/xanathars-guild.md:218`)
- Page only: "To those who work alongside him, he notes which tables order twice, which guests lower their voices, and which visitors he sees again without a reservation." (`:21`)

### G3. Pride, loves and the work he likes

- Sourced, his own words: "\"But I've been cooking professionally for eight years. I like the work. It suits me.\"" (`sources/Appendix_D_-_Running_the_Tavern.md:504`)
- Sourced, pride in the cooking: "Genuine skill (the Guild chose him partly because a mediocre plant draws attention)." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:107`)
- Voice, pride and attention: "Professional pride and attention." (`voices/xanathars-guild.md:216`)
- Voice, a kitchen oath: "Kitchen swearing, behind the pass, never in the dining room (\"Shit, the stock's burnt.\")." (`voices/xanathars-guild.md:215`)
- Page only, satisfaction: "genuine satisfaction when a dish lands exactly right" (`:13`); "quiet contempt for sloppiness" (`:13`).
- Page only, care for the food: "make the food worth recommending so no one looks closely at the cook" (`:15`).

### G4. Grudges and contempt

- No sourced grudge. The only contempt is the page's "quiet contempt for sloppiness" (`:13`) and the voice's kitchen irritation: "Shit, the stock's burnt." (`voices/xanathars-guild.md:215`). Neither names a person or a Guild figure.

### G5. Losses

- None sourced. The page's guilt (`:13`) has no named loss.

### G6. People and places he cares about

- None sourced. No family, lover, friend or home is named. The only people he is tied to are the Guild (`organizations/08-xanathars-guild.md:196`) and Tobrin as the other plant (`13-tobrin-ashvale.md:25`), both as work relationships.
- Voice, the one place he is comfortable: "Kitchen talk: pass, service, \"table four\", dishes by name." (`voices/xanathars-guild.md:214`)

---

## Not found

Searched for `Grevik`, `Nass`, `Master Cook`, `cook`, `kitchen`, `Trollskull`, `plant` and `Tobrin` across the listed sources. Result per source:

- `campaign/quests/**` (all quest journals and faction-event folders): no `Grevik`, no `Master Cook`. The only hits for `plant` are unrelated.
- `campaign/structure/arc-e-faction-outposts.md`: no `Grevik`. Outposts are Terasse Estate (`:137`, `:149`), Grinda Garloth and Orb Confectioners. No Field Ward Xanathar front.
- `campaign/structure/arc-f-xanathars-lair.md`: no `Grevik`; `Trollskull` appears only in the opener, not about Grevik.
- `campaign/guides/factions/09-xanathars-guild.md`: no `Grevik`, no `Trollskull`. Terasse, Grinda and Orb are described; the staff plants are not in the Factions Guide.
- `campaign/guides/trollskull-manor/` (all files): `Grevik` at `03-staff-and-hiring.md:107` and `09-response-teams-at-the-tavern.md:23` only.
- `campaign/locations/trollskull-manor/` (all files): no `Grevik`. The kitchen (`tm02-kitchen.md:3`, `:7`) has a staffed kitchen "with a hire from the **Trollskull Manor** guide cook candidates", and no named cook.
- `campaign/setting/**`: `Grevik` only in the Notable Figures folder, the Guild page, and `deities/gruumsh.md`. No history, lore, villain or Grand Game page names Grevik.
- `campaign/setting/villains/xanathar.md`, `jarlaxle.md`, `manshoon.md`: no `Grevik`.
- `campaign/gazetteer/waterdeep/`: `Grevik` only in `field-ward.md` (`:9`, `:238`).
- `sources/adventure-wdh.json`: no `Grevik`, `Nass`, `Master Cook` or Trollskull staff cook. The Trollskull text is renovation and neighbours. Lair cooks are Xanathar's, not Grevik's (E4).
- `sources/Appendix_B_-_Player_Factions.md`: no `Grevik`, no Trollskull staffing.
- `sources/Appendix_C_-_Player_Faction_Missions.md`: no `Grevik`. The only half-orc informant (`:101`) is a woman and is not Grevik.
- `sources/Act_III_Arc_E.md`: no `Grevik`; no `Field Ward` (count 0).
- `sources/Appendix_D_-_Running_the_Tavern.md`: `Grevik` at `:500`–`:515`, `:1521`; Tobrin's parallel entry at `:190`–`:201`.
- `sources/27. Addendum A Night in Trollskull Manor.pdf` (PDF pages 1 to 20, printed pp.178 to 197): no Grevik. Staffing (printed p.182, "The PCs will also need to hire staff: A bartender, barmaids, and cooks.") and COOKS (printed p.183) list other cooks (D8). Patron profiles from printed p.192 to 197 (Tally, Embric, Avi, Fala, Vincent, Rishaal, the start of Hammond) name no Grevik. PDF pages after 20 were not read (see Not readable).
- `sources/5. Faction Outposts.pdf` (13 PDF pages): read PDF pages 1–2, 7–8 and 9–13 (printed pp.36–37, 42–48). Xanathar outposts (Terasse Estate, printed pp.42–43; Grinda Garloth, p.43; Orb Confectioners, p.44) name no Grevik and no Trollskull or Field Ward front. The Zhentarim Interrogation House (p.45) and Yellowspire (p.46) also name no Grevik. PDF pages 3–6 (printed pp.38–41, Bregan D'aerthe and Seven Masks) were not read; they sit before the Xanathar section.
- `sources/17. Outpost and Lair Revelation Lists.pdf` p.123 [PDF p.3]: Xanathar's Lair revelations (`LAIR: XANATHAR'S LAIR`) list "Rescuing Ott Steeltoes", "A Note Regarding Gladiatorial Weapons", "Gladiatorial Gathering Point (Terasse Estate)" and "Correspondence with N'arl Xibrindas". No Grevik, no Trollskull revelation.
- `sources/11. Lair  Xanathar’s Lair.pdf`: not read. It covers the lair, not staff; no Grevik expected. Not checked.
- `sources/SOURCE_GUIDE.md`: no `Grevik`. The Trollskull entries point to `campaign/guides/trollskull-manor/03-staff-and-hiring.md:48`, `:57`, `:107` (`SOURCE_GUIDE.md:298`), so the guide itself is listed for Grevik.
- Wiki: `scratchpad/wiki-xg/Grevik_Nass.txt` = `NOT FOUND`. `scratchpad/wiki-xg/*` (15 files): no `Grevik` or `Nass`. `sources/research/pass5-bundles/xanathars-guild/wiki.txt`: no `Grevik`, `Nass`, `cook` or `Trollskull` for the Guild wiki. Other `sources/research/**/wiki.txt`: no `Grevik`.
- `docs/plans/setting-compendium-research-notes/pass5/xanathars-guild.md`: Key Members check only.

## Not readable

- `sources/5. Faction Outposts.pdf` PDF pages 3–6 not read (above).
- `sources/27. Addendum A Night in Trollskull Manor.pdf` PDF pages 21 onward not read (above).
- `sources/11. Lair  Xanathar’s Lair.pdf` not read (above).
- PDF quotes were transcribed from images, not extracted text. Flagged for pdftotext check.
- `sources/Other remix files/*.docx`: not searched. `SOURCE_GUIDE.md` does not list one for Grevik.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
