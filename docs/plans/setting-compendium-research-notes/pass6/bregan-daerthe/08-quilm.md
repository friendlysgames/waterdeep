# Pass 6 research notes: Quilm

Page: `campaign/setting/notable-figures/bregan-daerthe/08-quilm.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Group folder: `bregan-daerthe`. Faction organization page: `campaign/setting/organizations/07-bregan-daerthe.md`. Villains page: none; `campaign/setting/villains/jarlaxle.md` names Quilm only as left out (line 184, quoted at E3).
Ruling used: Ches 1, 1492 DR. Quilm is a Bregan D'aerthe scout who files weekly intelligence reports to Jarlaxle. Trollskull Manor's staff hiring (the bouncer candidate) is a quest-time event, so the Trollskull placement is routed, not day-one (see C).
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md`, heading `### Quilm` (line 152).

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure `sources/adventure-wdh.json`: Grep for "Quilm": no match. Quilm is not in the adventure.
- Alexandrian appendix `sources/Appendix_D_-_Running_the_Tavern.md`: Read. Lines 615 to 632 are the Quilm entry ("Candidate 5 — Quilm"). Quotes are copied from the file. HTML tags (`<p>`, `<em>`) are left as written.
- Alexandrian PDFs: `sources/5. Faction Outposts.pdf` printed pp.36 to 37 read as images; Quilm does not appear on those pages. Other PDFs not checked for Quilm (see Not readable).
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/08-quilm.txt` reads `NOT FOUND`. There is no wiki page for Quilm. Grep of `sources/research/pass5-bundles/bregan-daerthe/wiki.txt` and `adventure.txt` found no line naming Quilm.
- Source rank used: campaign files, then the published adventure (none), then the Alexandrian appendix, then the wiki (none).
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **Almost every fact about Quilm is a campaign label or the Alexandrian appendix.** The published adventure does not name him. The only Alexandrian source is Appendix D, "Candidate 5 — Quilm" (`sources/Appendix_D_-_Running_the_Tavern.md:615` to `:632`). The campaign's staff row is the other source (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:78`).
2. **The Trollskull placement is quest-time.** Hiring is a Trollskull Alley event: "In the days before opening, candidates arrive for each open position." (`campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22`). The page's "applied for the bouncer position", "the evening he was hired" and "placed as a Trollskull Manor bouncer candidate" are event-time. Restate as day-one (a BD scout with a weekly report, and an assignment to Waterdeep's surface operations) or route them.
3. **The page's "Featured in: Finding Floon" has no source.** No Finding Floon file names Quilm (Grep of `campaign/quests/` for "Quilm": only faction-event files and the Trollskull guide).
4. **Voice profile and Appendix D conflict on whether Quilm names Jarlaxle** (see D1). The voice says "He never mentions Jarlaxle" (`.claude/skills/character-voices/voices/bregan-daerthe.md:162`). Appendix D has the Jarlaxle message and his negotiation line (`Appendix_D:626` and `:628`). Report to the orchestrator; no source settles it.
5. **The item is a "card" in the staff guide and in Appendix D, and a "letter" on the page and in the voice.** See D2.

---

## A. Background facts by theme

### A1. Origin, birth, family, former life (no source)

No source gives Quilm's origin, birthplace, age, family, or any life before the company. The page and the voice profile give none. Appendix D gives only appearance and manner:

> "He is compact and still, with the economical posture of someone trained to take up exactly as much space as required and no more."
> — `sources/Appendix_D_-_Running_the_Tavern.md:619` (the narrative block; rest of the passage covers his surface clothing and his first words)

### A2. How he came to the company (no source; the company's recruiting rule only)

**Campaign, the company's recruiting rule (organization page, Beliefs)**
> "**Watch Before You Approach:** The company recruits with care. Its spies shadow a candidate for several days before anyone makes contact."
> — `campaign/setting/organizations/07-bregan-daerthe.md:40`

**Campaign, the company's recruiting rule, the offer (Factions Guide, First Meeting)**
> "Bregan D'aerthe recruits during **Trollskull Alley**. The offer extends to any party member."
> — `campaign/guides/factions/08-bregan-daerthe.md:37` (rest of the paragraph covers the shadowing and the black card)

Quilm's own recruitment is not sourced.

### A3. Work for Jarlaxle (day-one; the weekly report)

**Campaign, the weekly reports (organization page, the Waterdeep network)**
> "**The Waterdeep network:** Ryvarra watches the well at the Yawning Portal from the balcony, and Quilm files a weekly intelligence report for Jarlaxle."
> — `campaign/setting/organizations/07-bregan-daerthe.md:67` (rest of the paragraph covers Fenerus Stormcastle's house, a calligraphy shop, a grain factor's tallyman, Filthy Meg, Grinda Garloth, Vessa and Nar'l Xibrindas)

**Campaign, the weekly reports (organization page, Methods and Tactics)**
> "**Gathering information:** Each nimblewright feeds a crystal ball aboard the *Scarlet Marpenoth*, so every sale is also a listening post. Nar'l reports by *Sending* spell, Ryvarra and Quilm file weekly reports, and Fenerus gathers coded messages from dead drops across the Trades Ward for Krebbyg to collect every two days. Members use Drow Sign Language (*Waterdeep: Dragon Heist*, 5e), and the Faire's sailors speak to one another in odd hand signals (*Waterdeep: Dragon Heist*, 5e). The wiki says the company's contacts reached as far as the svirfneblin city of Blingdenstone (Forgotten Realms Wiki, *Bregan D'aerthe*, edition not stated)."
> — `campaign/setting/organizations/07-bregan-daerthe.md:75`

**Campaign, the key member entry (organization page)**
> "- **Quilm** — Drow spy, neutral. A Bregan D'aerthe scout who files weekly intelligence reports to Jarlaxle. See the **Quilm** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:106`

**Alexandrian, the assignment (Appendix D)**
> "Quilm is one of Jarlaxle's Bregan D'aerthe scouts, assigned to Waterdeep's surface operations. He is not here for combat intelligence — he is here because Jarlaxle has decided the tavern is interesting and wants a presence in it that the characters cannot easily refuse. Quilm is genuinely good at his job. He is also, self-evidently, a drow, and his presence on the door will generate comment in the North Ward for approximately three tendays before the neighborhood decides it is simply a thing that is true about the Trollskull. He finds this process mildly interesting to observe."
> — `sources/Appendix_D_-_Running_the_Tavern.md:622`

### A4. The Trollskull placement (quest-time; route, do not state as day-one)

**Campaign, the candidate row (Trollskull Manor staff guide)**
> "| 5 | **Quilm** | N drow | Surface clothes that are slightly too precisely correct. Places a card on the bar: \"Quilm. Available for security work.\" Below, in different ink and silver: \"He is entirely trustworthy. — J.\" Does not confirm who J is unless the party already knows. DC 10 Insight identifies the handwriting as affected and theatrical; drow PCs or BD-affiliated characters recognize the style automatically. Genuine bouncer, excellent at the work. Neutralizes all BD Response Team visits automatically — he speaks to them outside and they don't enter. If party is overtly hostile to BD: leaves without notice. With Yagra: they sort out jurisdiction between themselves, silently, and it works. | Bregan D'aerthe scout. | 9 gp | Advantage on Event nights. All BD Response Team visits neutralized (no roll, no confrontation). +1 Fame after 3 tendays. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:78`

**Campaign, the hiring window (Trollskull Alley journal)**
> "In the days before opening, candidates arrive for each open position. The interview process is a low-stakes social encounter with real consequences: candidates have agendas, faction affiliations, and secrets that will matter later. Full candidate tables in the **Trollskull Manor** guide, Staff and Hiring."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22`

**Alexandrian, the arrival (Appendix D; the card and the first conversation)**
> "<p>He is a drow, which you notice immediately, and he is wearing surface clothes with the careful precision of someone who has read extensively about them but not grown up with them — everything is correct in a way that is slightly too correct. He is compact and still, with the economical posture of someone trained to take up exactly as much space as required and no more. He has a small folded card, which he places on the bar. It reads, in a neat hand: <em>Quilm. Available for security work. References on request.</em> Below this, in different ink, someone has added: <em>He is entirely trustworthy. — J</em> \"I understand,\" he says, \"that you are looking for someone to manage difficult situations. I have experience with this. I am discreet. I am available evenings.\" He waits.</p>"
> — `sources/Appendix_D_-_Running_the_Tavern.md:619` (HTML tags as written)

### A5. Faith (no source; the company's rule)

> "- **The Company Rejects Lolth:** Bregan D'aerthe has rejected Lolth as its goddess. No member worships her, keeps a shrine to her or invokes the Spider Queen with devotion, and members speak of her with contempt, as the goddess they walked away from."
> — `campaign/setting/organizations/07-bregan-daerthe.md:46`

Nothing says what Quilm believes beyond that rule.

### A6. Standing in the company and rank (no source)

No source gives Quilm a rank. The Factions Guide rank events do not name him (Grep of `campaign/quests/faction-events/bregan-daerthe/` for "Quilm": only the first-meeting design notes, quoted at E4). His only label is "Bregan D'aerthe scout." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:78`).

### A7. Signature belongings

- The card: "Quilm. Available for security work. References on request." with "He is entirely trustworthy. — J" in different ink (`sources/Appendix_D_-_Running_the_Tavern.md:619`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:78`). The page calls it a "recommendation letter" (see D2).

---

## B. Alignment, species, pronouns, stat block

**Alignment: neutral**
- Page: "> - *Drow spy (Bregan D'aerthe scout), neutral, he/him*. Stat block: **Spy**." — `campaign/setting/notable-figures/bregan-daerthe/08-quilm.md:5`
- Organization page: "- **Quilm** — Drow spy, neutral." — `campaign/setting/organizations/07-bregan-daerthe.md:106`
- Trollskull staff guide: "| 5 | **Quilm** | N drow |" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:78`
- Appendix D: "*N male drow, Tough (Bregan D'aerthe). Sent by Jarlaxle. Obviously.*" — `sources/Appendix_D_-_Running_the_Tavern.md:616`. "N" is the Appendix's alignment abbreviation. "Tough" is the candidate category; it is not a stat block.

**Species: drow**
- Page: "*Drow spy (Bregan D'aerthe scout), neutral, he/him*." (`08-quilm.md:5`)
- Staff guide: "N drow" (`03-staff-and-hiring.md:78`)
- Appendix D: "*N male drow, Tough (Bregan D'aerthe).*" (`Appendix_D_-_Running_the_Tavern.md:616`)

**Pronouns: he/him**
- Page: "*Drow spy (Bregan D'aerthe scout), neutral, he/him*." (`08-quilm.md:5`)
- Appendix D: "N male drow" (`Appendix_D_-_Running_the_Tavern.md:616`). Pronouns in the entry: "He is not here for combat intelligence" (`:622`).
- Staff guide: no pronoun for Quilm.

**Stat block: Spy (campaign only)**
- Page: "Stat block: **Spy**." (`08-quilm.md:5`)
- No other source. The Appendix gives "Tough" (a candidate category, `Appendix_D:616`), not a stat block.

**Affiliation: Bregan D'aerthe**
- Page: "> - **Affiliation:** Bregan D'aerthe" (`08-quilm.md:6`)
- Staff guide: "Bregan D'aerthe scout." (`03-staff-and-hiring.md:78`)
- Appendix D: "**Faction Note:** Bregan D'aerthe." (`Appendix_D_-_Running_the_Tavern.md:626`)

**Location: Trollskull Manor, North Ward**
- Appendix D: "his presence on the door will generate comment in the North Ward" (`Appendix_D_-_Running_the_Tavern.md:622`)
- Campaign: "The party's tavern, Trollskull Manor, stands here" (`campaign/gazetteer/waterdeep/north-ward.md:7`). Consistent.

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/08-quilm.md`. The page has no Background, Personality or Connections yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Drow spy (Bregan D'aerthe scout), neutral, he/him*. Stat block: **Spy**." | Day-one labels. "Spy" stat block unsourced (B). | Section B |
| 2 | L6 | "**Affiliation:** Bregan D'aerthe" | Day-one. | `campaign/setting/organizations/07-bregan-daerthe.md:106` |
| 3 | L7 | "**Featured in:** **Finding Floon**, **Trollskull Alley**" | Quest references. "Finding Floon" has no source (Findings 3). "Trollskull Alley" is supported only through the staff hiring (`ev-06-the-grand-opening.md:22`; `03-staff-and-hiring.md:78`). | A4 |
| 4 | L11 | "**Resonance.** Quilm should inspire professional respect for his quiet competence; subtle unease if someone notices the recommendation letter's handwriting; and useful satisfaction when Bregan D'aerthe response team visits simply stop materializing." | Two clauses are event-time. "if someone notices the recommendation letter's handwriting" depends on the hiring card (Appendix D `:619`, `:624`). "when Bregan D'aerthe response team visits simply stop materializing" depends on his hire (staff `:78`). "professional respect for his quiet competence" is day-one. | `campaign/guides/trollskull-manor/03-staff-and-hiring.md:78`; `sources/Appendix_D_-_Running_the_Tavern.md:632` |
| 5 | L13 | "**Emotions.** Quilm most often feels operational discipline, the particular stillness of a scout who has learned to be uninteresting, professional loyalty to Bregan D'aerthe, private amusement at the tavern work, and the patience of someone whose job is to be overlooked." | Mostly day-one. "private amusement at the tavern work" depends on the hire (A4). Appendix D: "He finds this process mildly interesting to observe." (`:622`) is the source for the amusement. | A3; A4 |
| 6 | L15 | "**Motivations.** Quilm wants to maintain his position at the tavern, file the weekly intelligence reports Jarlaxle expects, and neutralize Bregan D'aerthe response team visits without exposing that he is doing so." | "maintain his position at the tavern" presupposes the hire (quest-time). "file the weekly intelligence reports Jarlaxle expects" is day-one (`07-bregan-daerthe.md:67`). "neutralize Bregan D'aerthe response team visits" depends on the hire (`03-staff-and-hiring.md:78`). | A3; A4 |
| 7 | L17 | "**Inspirations.** When playing Quilm, channel Boba Fett (*Star Wars*), Leon (*Leon: The Professional*), and Varys (*Game of Thrones*, the useful invisible man)." | Not a fact. | n/a |
| 8 | L21 | "**Persona.** To the world, Quilm is a drow who applied for the bouncer position with a handwritten recommendation and does the job without comment or complaint. To those who read the recommendation letter carefully, the handwriting is recognizably Jarlaxle's — the flourishes are distinctive, visible to any drow character or anyone who has previously seen his correspondence (DC 12 Investigation). Deep down, he filed his first intelligence report the evening he was hired and has not missed a week." | Quest-time: "applied for the bouncer position", "the recommendation letter", "the evening he was hired" (hire event; A4). "does the job without comment or complaint" presupposes the hire. The handwriting clue's check differs from Appendix D (D5). | A4; Appendix D `:624` |
| 9 | L23 | "**Morale.** In a fight, Quilm removes threats to the tavern with the minimum force required. He does not escalate, and he does not explain." | Encounter behaviour. "removes threats to the tavern" presupposes the tavern job. No source gives Quilm's fighting. Appendix D gives only the hostile-party rule: "If the party is overtly hostile to Bregan D'aerthe, Quilm leaves without notice at the end of the tenday in which hostilities begin." (`Appendix_D:632`). | F3 |
| 10 | L25 | "**Relationships.** Quilm is a Bregan D'aerthe scout placed as a Trollskull Manor bouncer candidate, the reason no Bregan D'aerthe response team visit materializes while he works there, a man whose recommendation from \"J\" contains Jarlaxle's handwriting, and a weekly intelligence source for Jarlaxle's Waterdeep network." | "placed as a Trollskull Manor bouncer candidate" (hire, quest-time); "the reason no Bregan D'aerthe response team visit materializes while he works there" (hire, quest-time, `:78`); "a man whose recommendation from \"J\" contains Jarlaxle's handwriting" (the hiring card, `:619`, `:624`); "a weekly intelligence source for Jarlaxle's Waterdeep network" (day-one, `07-bregan-daerthe.md:67`). | A3; A4 |
| 11 | L27 | "## Overview" heading | Not a fact. | n/a |
| 12 | L29 | "A drow bouncer candidate at Trollskull Manor who came with a handwritten recommendation, does the job without complaint, and keeps odd hours — he is professionally uninteresting, which is the point." | Public face. "bouncer candidate ... came with a handwritten recommendation, does the job" is event-time. "keeps odd hours" has no source. One sentence of about 30 words, over the brief's 21-word limit. | A4 |

**Voice profile (`.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Quilm", lines 152 to 166)**

The Quilm profile calls its sentence shape "a deliberate break from `ember-voice` speech" (line 156). Its lines, with status:

> "- **Sound:** A quiet, flat, unmemorable voice." — line 155 (day-one)

> "- **Sentence shape:** A few plain words at a time. He answers what's asked and nothing else. This is a deliberate break from `ember-voice` speech." — line 156 (day-one; the ember-voice note is a skill note, not a speech line)

> "- **Word choice:** Bouncer basics: \"out\", \"no\", \"calm down\". He calls patrons \"sir\" or \"ma'am\" with no inflection." — line 157 (day-one as a habit; "patrons" presupposes the tavern job, A4)

> "- **Swearing:** *Stingy · Plain · Clipped.* Minimal and flat (\"Out. Now. Fuck off.\")." — line 158 (day-one; the swearing stays, adult table)

> "- **Personality in speech:** Operational discipline, cultivated dullness. His private amusement at tavern work shows only as the slightest pause." — line 159 (day-one except "tavern work", which presupposes the hire, A4)

> "- **Quirks:** He doesn't volunteer his name unless asked twice. He says \"Understood\" and walks away." — line 160 (day-one)

> "- **Signature phrases:** \"Understood.\" / \"Out.\" / \"Not my business.\"" — line 161 (day-one)

> "- **Never:** He never mentions Jarlaxle, never explains the letter, and never draws attention to himself." — line 162. **Conflict with the Alexandrian appendix** (D1). "never explains the letter" presupposes the hiring card (A4).

> "  - *Greeting:* \"Evening.\"" — line 164 (day-one)

> "  - *Business:* \"Letter's from a former employer. Understood?\"" — line 165. **Quest-time and conflicting.** It presupposes the hiring card (A4). "a former employer" conflicts with his present service (`07-bregan-daerthe.md:106`, "A Bregan D'aerthe scout who files weekly intelligence reports to Jarlaxle.") (D3).

> "  - *Under pressure:* \"Out. Now.\"" — line 166 (day-one)

---

## D. Conflicts

**D1. Does Quilm name Jarlaxle?**
- Voice profile: "He never mentions Jarlaxle, never explains the letter, and never draws attention to himself." (`.claude/skills/character-voices/voices/bregan-daerthe.md:162`)
- Appendix D, the message to drow party members: "**Faction Note:** Bregan D'aerthe. Drow party members are told privately on his second night: \"Jarlaxle wishes you to know he has noticed this establishment. He means this as a compliment.\"" (`sources/Appendix_D_-_Running_the_Tavern.md:626`). The sentence does not name the speaker; the entry is Quilm's.
- Appendix D, the wage: "**Wage:** 9 gp/tenday. He asked for 8 gp. Jarlaxle, through Quilm, suggested the party offer 10 gp. The 9 gp compromise pleases no one completely, which Quilm considers an appropriate outcome." (`sources/Appendix_D_-_Running_the_Tavern.md:628`)
- Staff guide: "Does not confirm who J is unless the party already knows." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:78`). It does not say he never names Jarlaxle.
- Ranking: the campaign's voice profile is a campaign file and outranks the Alexandrian. No campaign file states whether Quilm says "Jarlaxle" aloud. The voice "Never" line and the Appendix D lines conflict. Left for the orchestrator.

**D2. "Card" or "letter"**
- Page: "the recommendation letter's handwriting" (`08-quilm.md:11`); "a handwritten recommendation" (`:21`); "a man whose recommendation from \"J\"" (`:25`).
- Appendix D: "He has a small folded card, which he places on the bar." (`Appendix_D_-_Running_the_Tavern.md:619`)
- Staff guide: "Places a card on the bar" (`03-staff-and-hiring.md:78`).
- Ranking: the campaign's staff guide governs the item (a card). The page and the voice say "letter". The drafter should use one term.

**D3. "Former employer" or present service**
- Voice profile: "Letter's from a former employer. Understood?" (`bregan-daerthe.md:165`)
- Organization page: "A Bregan D'aerthe scout who files weekly intelligence reports to Jarlaxle." (`campaign/setting/organizations/07-bregan-daerthe.md:106`)
- Page: "Quilm is a Bregan D'aerthe scout placed as a Trollskull Manor bouncer candidate" (`08-quilm.md:25`)
- Ranking: the campaign's organization page and page govern. "former employer" conflicts with present tense. Left for the orchestrator (voice profile line 165 needs a decision).

**D4. "Featured in: Finding Floon"**
- Page: "**Featured in:** **Finding Floon**, **Trollskull Alley**" (`08-quilm.md:7`).
- No Finding Floon file names Quilm (Grep of `campaign/quests/` and `campaign/structure/arc-a-finding-floon.md` for "Quilm": none). The Trollskull Alley journal does not name him either; its hiring note points to the guide (`campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22`).
- Ranking: no source supports the Finding Floon label. The drafter should not keep it without a source.

**D5. Handwriting check (DC and who recognizes it)**
- Page: "the handwriting is recognizably Jarlaxle's — the flourishes are distinctive, visible to any drow character or anyone who has previously seen his correspondence (DC 12 Investigation)." (`08-quilm.md:21`)
- Appendix D: "DC 10 Insight identifies the handwriting style as affected and theatrical — someone who writes this way does it for effect. Jarlaxle characters or anyone who has encountered Bregan D'aerthe documentation will recognize the silver-ink style immediately (DC 12 Investigation if they've seen Bregan D'aerthe documents; auto-recognition if they are drow or BD affiliated). Quilm does not confirm or deny who \"J\" is unless the party demonstrates they already know." (`Appendix_D_-_Running_the_Tavern.md:624`)
- Staff guide: "DC 10 Insight identifies the handwriting as affected and theatrical; drow PCs or BD-affiliated characters recognize the style automatically." (`03-staff-and-hiring.md:78`)
- Ranking: the staff guide (campaign) and the appendix agree on DC 10 Insight and automatic recognition for drow or BD. The page's "recognizably Jarlaxle's" and "DC 12 Investigation" differ. The drafter should use the staff guide's terms.

**D6. Morale and fighting**
- Page: "In a fight, Quilm removes threats to the tavern with the minimum force required." (`08-quilm.md:23`) No source gives fight behaviour beyond the hostile-party rule (`Appendix_D:632`). Not a conflict; unsourced.

---

## E. Stale lines in other files (not to be edited), and routed quest references

**E1. Stale line number.** `docs/plans/bregan-daerthe-research/02-first-meeting-and-standalones.md:73` cites "`07-bregan-daerthe.md:42`" for Quilm. The current line is `campaign/setting/organizations/07-bregan-daerthe.md:106`. The stale line is in a research note, not a campaign file.

**E2. Routed: the organization page's routed-to-quests bullet.** `campaign/setting/organizations/07-bregan-daerthe.md:207`:
> "> - **Routed to quests:** Quilm's \"Placed as a Trollskull Manor bouncer candidate\" and the tenet clause \"Quilm applies for work at Trollskull Manor\". The placement happens when the party hires staff, and it lives in `guides/trollskull-manor/03-staff-and-hiring.md:78` and `notable-figures/bregan-daerthe/08-quilm.md:25`."

**E3. Villains page: Quilm is deliberately left out.** `campaign/setting/villains/jarlaxle.md:184`:
> "> - **Left out:** The wiki's Zaknafein raid of 1018 DR, Artemis Entreri, Kimmuriel Oblodra, the Ghost King of 1384 DR, the 1487 DR Host Tower reconstruction, the 1366 DR Calimport base and Crenshinibon, Gromph Baenre and the \"third son\" gloss. Also left out: the names of Luskan's High Captains, the Lantanese wizard and the nimblewright counts, the Zardoz Betrayal Pitch, Quilm, Margo Verida, Khafeyta Murzan, Malkolm Brizzenbright and Fenerus Stormcastle beyond the Manshoon note, Zelifarn, and the Alexandrian PDF 8 Eye-holder list."

**E4. Quest note on the First Meeting.** `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/design-notes.md:31`:
> "The renovation financing that **The Factions Come Calling** attaches to Bregan D'aerthe (up to 1,250 gp, repayable in \"operational access\") is not carried here, since no source text decides how Nevercott would offer it. Quilm, the drow bouncer candidate, has no role in the event."

**E5. Superseded structure doc.** `campaign/structure/arc-b-trollskull-alley.md:207` (superseded by the Trollskull Alley journal; quoted for routing):
> "*Staff Hiring.* In the days before the opening, candidates arrive for each open position. **The interview process is a low-stakes social encounter with real consequences** — candidates have agendas, faction affiliations, and secrets that will matter later. Cross-ref **Appendix F, Staff Candidates** for full interview profiles (five bartenders, five servers, five cooks, five bouncers, five house bards). Interview framing:"

Appendix F is not among the files in `sources/` (Glob `sources/Appendix_*` returns only B, C and D). The five-bouncer list is not available to read.

**E6. Quest-time hire routing.** The hire itself is in `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:20` to `:22` ("### Staff Hiring"). Quilm is not named there.

**E7. Pronoun table.** `docs/plans/npc-pronouns-table-group-c.md:17`: "| Quilm | bregan-daerthe/08-quilm.md:5 | he/him | prose (\"respect for his quiet competence\", \"Quilm wants to maintain his position\", \"a man whose recommendation from 'J'\") | High |" — consistent with the page.

**E8. Voice-profile note.** `docs/plans/bregan-daerthe-research/01-spec-and-faction-rules.md:241`: "Quilm's profile explicitly breaks from the ember-voice speech floor (`:156`). Krebbyg's run-ons suit it." — consistent with the profile.

---

## F. Gaps a Background needs that no source gives

For each gap, the sourced facts the drafter must stay consistent with.

**F1. Origin, birthplace, age, family, and life before the company.** No source gives any of these.
- Sourced: "He is compact and still" (`sources/Appendix_D_-_Running_the_Tavern.md:619`), "Surface clothes that are slightly too precisely correct." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:78`), and "N male drow, Tough (Bregan D'aerthe)." (`Appendix_D:616`).
- Sourced: "Quilm is one of Jarlaxle's Bregan D'aerthe scouts, assigned to Waterdeep's surface operations." (`Appendix_D:622`).

**F2. How he joined the company, and his rank.** No source. The company's recruiting method is sourced (`campaign/setting/organizations/07-bregan-daerthe.md:40`, "Watch Before You Approach", quoted in A2). No rank is given for Quilm (A6).

**F3. How he fights, and what he has done in the tavern.** Only the hostile-party rule and the non-entry rule are sourced (`Appendix_D:632`). The Morale line (`08-quilm.md:23`) has no source.

**F4. Whether he believes in anything, and what he wants apart from the job.** No source. Sourced wants are job-bound: "maintain his position at the tavern", "file the weekly intelligence reports Jarlaxle expects" (`08-quilm.md:15`). Appendix D gives one personal reaction: "which Quilm considers an appropriate outcome" (`Appendix_D:628`). The drafter must invent under ruling 17 (`[design]`), and must not contradict the company's loyalty ("professional loyalty to Bregan D'aerthe", `08-quilm.md:13`) or the Lolth rule (A5).

**F5. The "J" relationship.** Sourced: the card is signed "J" (`03-staff-and-hiring.md:78`), and "Jarlaxle has decided the tavern is interesting" (`Appendix_D:622`). Not sourced: whether Quilm met Jarlaxle before, or what Quilm thinks of him. Do not invent a history with Jarlaxle beyond the sourced facts without `[design]`.

**F6. The "former employer" line.** The voice's "Letter's from a former employer" (`bregan-daerthe.md:165`) has no source for a former employer (D3). The drafter should not write a former employer without `[design]`.

**F7. Age and years in post.** No source. "filed his first intelligence report the evening he was hired and has not missed a week" (`08-quilm.md:21`) gives a continuing habit, but not a length of service in years.

---

## G. Inner-life facts (exact quotes, for the Background and personal goals)

- **Loyalty.** "professional loyalty to Bregan D'aerthe" — `campaign/setting/notable-figures/bregan-daerthe/08-quilm.md:13`
- **Patience and being overlooked.** "the patience of someone whose job is to be overlooked" — `08-quilm.md:13`
- **Discipline.** "the particular stillness of a scout who has learned to be uninteresting" — `08-quilm.md:13`
- **Pride in the work.** "Quilm is genuinely good at his job." — `sources/Appendix_D_-_Running_the_Tavern.md:622`
- **Amusement at the tavern.** "He finds this process mildly interesting to observe." — `Appendix_D:622`; "private amusement at the tavern work" — `08-quilm.md:13`
- **Money.** "He asked for 8 gp." — `Appendix_D:628`. "The 9 gp compromise pleases no one completely, which Quilm considers an appropriate outcome." — `Appendix_D:628`
- **Credit to his work.** "Genuine bouncer, excellent at the work." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:78`
- **Reputation.** "+1 Fame after three tendays as his presence becomes a neighborhood talking point (\"the drow bouncer\")." — `Appendix_D:632`
- **Silence about his name.** "He doesn't volunteer his name unless asked twice." — `.claude/skills/character-voices/voices/bregan-daerthe.md:160`
- **Staying unseen.** "never draws attention to himself." — `bregan-daerthe.md:162`
- **A model of the invisible man.** "Varys (*Game of Thrones*, the useful invisible man)." — `08-quilm.md:17`
- **A habit.** "filed his first intelligence report the evening he was hired and has not missed a week." — `08-quilm.md:21` (the "evening he was hired" clause is quest-time; the habit is day-one; see C row 8)

Not for the Background's invention, but must not be contradicted: "Neither of them will explain how they sorted it out." — `Appendix_D:630` (about Yagra Stonefist; shows his habit of not explaining).

---

## Not found

- **Wiki**: the extracted page reads `NOT FOUND` (the scratchpad file). Grep of `sources/research/pass5-bundles/bregan-daerthe/wiki.txt` and `adventure.txt`: no line for Quilm.
- **Quilm in the campaign**: Grep for "Quilm" in `campaign/`: the page, the organization page (lines 67, 75, 106, 207), the Villains page (line 184), the staff guide (line 78), the first-meeting design notes (line 31). No match in `campaign/quests/act-i/`, `campaign/structure/`, `campaign/locations/`, `campaign/gazetteer/` or `campaign/guides/factions/`.
- **Quilm in the sources**: Grep for "Quilm" in `sources/adventure-wdh.json`: none. In `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md`: none. In `sources/Act_III_Arc_E.md`: none. In `sources/Appendix_D_-_Running_the_Tavern.md`: lines 615 to 632 (the entry) and no other line.
- **"Finding Floon" and Quilm**: no match (D4).
- **Hiring**: "candidate" in `campaign/quests/act-i/trollskull-alley/`: Yagra Stonefist (`ev-04-the-factions-come-calling.md:85`), not Quilm.
- **Appendix F**: not in `sources/` (Glob `sources/Appendix_*` returns B, C and D only). Quilm may be in Appendix F as one of the "five bouncers" (E5).
- **Pass bundles**: `sources/research/pass4-bundles/jarlaxle/campaign-hits.txt:1391` to `:1393` and `sources/research/pass5-bundles/bregan-daerthe/campaign-hits.txt:302` to `:305` quote the old page text. They match the current page.

---

## Not readable

- `sources/Other remix files/Jarlaxle Baenre NPC Guide.docx`: listed in `sources/SOURCE_GUIDE.md:690`. Not opened (`.docx` cannot be read with these tools). It may cover the company's bouncers or the Trollskull hire. Extract it and check for Quilm.
- `sources/Other remix files/Lif and the Haunting of Trollskull Manor.docx`: listed in `sources/SOURCE_GUIDE.md:691` for the Trollskull Manor guide. Not opened. It may mention staff; no SOURCE_GUIDE row names Quilm.
- Alexandrian PDFs not checked for Quilm: `sources/6. Faction Response Teams.pdf` (the Bregan response teams that Quilm neutralises), `sources/3. Player Character Factions.pdf`, `sources/17. Outpost and Lair Revelation Lists.pdf`. Not checked.
