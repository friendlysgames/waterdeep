# Pass 6 research notes: Rella Asp

Page: `campaign/setting/notable-figures/cassalanters/12-rella-asp.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Rella is a Cassalanter operative under a cook's cover, reporting to Willifort Crowelle. The Trollskull Manor guide and Appendix D list her as a staff candidate. Cassalanter secrecy applies: nobody outside the household and the cult knows about the pact.
Model format: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/11-arn-xalrondar.md`

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- `sources/Appendix_D_-_Running_the_Tavern.md` is the Alexandrian remix appendix in markdown (rank 3). Its lines are quoted with their own line numbers.
- Published adventure: no Rella line. `sources/adventure-wdh.json` was grepped for `Rella|Asp\b`: no match.
- Alexandrian PDFs: Rella appears in none of the PDFs read. `sources/27. Addendum A Night in Trollskull Manor.pdf` was read at PDF p.1 only (printed p.178, the introduction). No shell was available, so `pdftotext` could not run. No PDF quote is used here.
- Wiki: no Rella page. `sources/research/**/wiki*` grep for "Rella" gives no hit.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.
- Source rank used: campaign files, then the published adventure (none), then the Alexandrian appendices, then the wiki (none).

## Findings that change how the page is written

1. **Alignment and stat block conflict with Appendix D.** The page says "lawful evil" and "Stat block: **Spy**" (line 5). Appendix D says "*NE female human, Commoner.*" (line 440). All three campaign files say LE (page line 5, organization line 104, Trollskull guide line 104). Campaign files outrank the appendix.
2. **Cook or poisoner.** The page calls her "an accomplished Master Cook" (line 21). Appendix D says "not a cook by trade but a poisoner who maintains a chef's cover as her primary identity" (line 446). The Trollskull guide says "Exceptional cook." (line 104).
3. **Cult status and knowledge are not stated.** The organization page's six named cult members do not include her (`10-cassalanters.md:52`). Appendix D says she handles "the quiet aspects of the family's infernal obligations" (line 446). Whether she knows the pact is unsourced in the campaign files.
4. **The commission is quest-time.** Page lines 15, 21 and 25, the Trollskull guide (line 104; `04-fame.md:95`; `09-response-teams-at-the-tavern.md:71`) and Appendix D (lines 448, 458, 988, 1054, 1588) all put the commission in Act III or after the party becomes a threat. Restate or remove.
5. **Sister Valdra recognition conflicts.** Appendix D line 454 says Valdra "has seen Rella's face at Cassalanter functions." Valdra's page (line 25) names only Ivrala Sorn as the person she can recognize on sight.
6. **"No scripted appearance" against the candidate list.** Page line 7 says "Background figure; no scripted appearance." The Trollskull guide lists her in the Master Cook table (`03-staff-and-hiring.md:104`), and Trollskull Alley ev-06 says "candidates arrive for each open position" (line 22).

---

## A. Background facts by theme

### A1. Origin, birth and early life

No campaign or adventure source gives Rella's birthplace, age, family, childhood or training. Appendix D gives her references and her look, not her history.

> "Dark hair, pale skin, a cook's apron worn as if it were a formal garment. She produces her references in a small leather portfolio, organized by date. They are from three reputable establishments, all of which confirm her excellence."
> — `sources/Appendix_D_-_Running_the_Tavern.md:443` (Candidate 2 — Rella Asp, narrative block; the first sentences of the paragraph are "She is precise and elegant, with the slim hands and unhurried movements of someone accustomed to detailed work.")

(rest of the passage covers: the samples and her dialogue; the establishments are not named.)

> "- **Rella Asp** — Tethyrian human poisoner (Cassalanter operative), lawful evil. See the **Rella Asp** page in Notable Figures."
> — `campaign/setting/organizations/10-cassalanters.md:104` (Key Members)

### A2. Service with the Cassalanters

> "Rella is a specialist employed by the Cassalanter household — not a cook by trade but a poisoner who maintains a chef's cover as her primary identity. She has worked for the Cassalanters for three years, handling the quiet aspects of the family's infernal obligations that require subtlety rather than summoned devils. Lord Victoro places enormous value on her discretion and her skill. She is not here to poison the party. She is here because the Cassalanters have decided the tavern is a useful piece on the board — a property owned by people who may become significant in the Grand Game — and Rella's placement gives them a kitchen-level view of who passes through and what is said within earshot of the pass-through window."
> — `sources/Appendix_D_-_Running_the_Tavern.md:446` (Candidate 2; the whole paragraph is quoted because the Background depends on it)

> "**Hidden Quality:** She will not be caught through normal means. The only tell is that she occasionally receives small packages delivered to the kitchen entrance from non-guild couriers — a DC 14 Perception check notices this. A character who follows the courier traces back to a Dock Ward contact used by Cassalanter household errands. DC 17 Investigation of her background connects her employment history to the Cassalanter Villa specifically — she is listed in guild records as their household cook for the past three years, which is true as far as it goes."
> — `sources/Appendix_D_-_Running_the_Tavern.md:452`

> "Ammalia keeps ten vials of the poison called midnight tears in her private study, and she is immune to poison (*Dragon Heist*, 5e). She means to serve ninety-nine of the one hundred guests wine laced with it, so that they die within a day and nothing connects them to the house (**The Cassalanters** in Villains). Jandar Chergoba sees that the poison is distributed correctly. Rella Asp is a poisoner under a cook's cover (**Rella Asp**)."
> — `campaign/setting/organizations/10-cassalanters.md:67` (Methods and Tactics, "Poison"; the full bullet is quoted)

> "Willifort leads a second, blunter team that the family draws on once discretion has failed. The family also owns the Asmodean Shrine, a converted residence on Aveen Street in the North Ward that it bought for the Hell cyst below it (**The Cassalanters** in the Factions Guide). Rella Asp and Ivrala Sorn work under the covers of a cook and a server and report to Willifort (their pages in Notable Figures)."
> — `campaign/setting/organizations/10-cassalanters.md:53` (Structure, "Field operatives and outposts"; the quote runs from the sentence after the Seffia sentence)

> "- **Rella Asp** and **Ivrala Sorn:** Cassalanter operatives under the covers of a cook and a server, who report to Willifort."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:41` (Relationships)

> "- **Chain of command:** Ammalia makes the final calls and Victoro has stopped questioning this. Willifort Crowelle reports to Ammalia on everything that happens in the villa. Seffia Naelryke's response team answers to Lord Cassalanter, and Rella Asp and Ivrala Sorn report to Willifort."
> — `campaign/setting/organizations/10-cassalanters.md:117` (GM Notes)

### A3. How she got the post

No campaign file says how she was recruited. Appendix D and the Trollskull guide give the placement.

> "Cassalanter poisoner on placement. Gathering kitchen-level patron intelligence. Commission arrives when party becomes a genuine Act III threat to the Cassalanters' gold plans. Target: an NPC the party has bonded with (not a party member). She will be gone before they trace it."
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:104` (Master Cook Candidates, row 2; the "Commission arrives" clause is quest-time, see C)

> "In the days before opening, candidates arrive for each open position. The interview process is a low-stakes social encounter with real consequences: candidates have agendas, faction affiliations, and secrets that will matter later. Full candidate tables in the **Trollskull Manor** guide, Staff and Hiring."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22` (routed: the hiring is a Trollskull Alley event)

### A4. Skills, wage and work at the tavern

> "| 2 | **Rella Asp** | LE Tethyrian human | Precise, slim-handed, unhurried. References in a well-organized leather portfolio. Brings a herbed terrine sample. Discusses flavor profiles with easy authority. \"I'm looking for a kitchen with some ambition.\" DC 14 Perception (not at interview — later, after hiring) notices irregular packages delivered to the kitchen entrance by non-guild couriers. DC 17 Investigation of her employment history connects directly to Cassalanter Villa. Exceptional cook. | Cassalanter poisoner on placement. Gathering kitchen-level patron intelligence. Commission arrives when party becomes a genuine Act III threat to the Cassalanters' gold plans. Target: an NPC the party has bonded with (not a party member). She will be gone before they trace it. | 14 gp | +4 Revenue. Intel filed as noted. Commission mechanics per the **Cassalanter Villa** encounter entry. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:104` (full table row; the header is "**Master Cook Candidates (14 gp/tenday)**" at line 99)

> "**Wage:** 14 gp/tenday."
> — `sources/Appendix_D_-_Running_the_Tavern.md:456` (Candidate 2; the header is "##### Master Cook Candidates (14 gp/tenday)" at line 420)

> "**Mechanical Effect:** +4 to Revenue Roll per tenday (she is genuinely exceptional). If her commission arrives: one specific NPC the party has formed a relationship with falls gravely ill over two days. DC 14 Medicine identifies poison; DC 16 identifies the specific compound as one used in Calishite court poisonings, a style associated with noble household contractors. Rella will be gone by the time the party traces it back to the kitchen."
> — `sources/Appendix_D_-_Running_the_Tavern.md:458` (the "If her commission arrives" clause is quest-time, see C)

> "Her food is exceptional throughout. She poisons no one who is not on her list. She considers this a professional standard."
> — `sources/Appendix_D_-_Running_the_Tavern.md:450`

### A5. Persona and public life (day-one)

> "To the world, Rella Asp is an accomplished Master Cook who arrives with excellent references, treats the kitchen with professional seriousness, and produces food that patrons remember. To those who observe carefully, her interest in who orders what and who dines with whom exceeds any normal culinary curiosity."
> — `campaign/setting/notable-figures/cassalanters/12-rella-asp.md:21` (Persona; these two sentences are day-one, see C. The third sentence is quest-time.)

### A6. Time in service

- "She has worked for the Cassalanters for three years" (`sources/Appendix_D_-_Running_the_Tavern.md:446`).
- "household cook for the past three years" (`Appendix_D:452`, quoted in A2).
- No campaign file gives a date for her service. No campaign file ties her to a date at all.

### A7. Relationships to named figures (day-one)

- **Willifort Crowelle** (her handler): `03-willifort-crowelle.md:41`; `10-cassalanters.md:117` (both quoted in A2).
- **Victoro Cassalanter** (values her): "Lord Victoro places enormous value on her discretion and her skill." (`Appendix_D:446`). The campaign files do not say Victoro has met her.
- **Ivrala Sorn** (fellow operative): "If employed alongside Rella Asp (Master Cook #2): Cassalanters have full kitchen + floor picture of the tavern." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:56`, Ivrala's row, Faction Note column). Appendix D: "If Ivrala is employed at the same time as Rella Asp (Master Cook candidate), the Cassalanters have both a kitchen-level and a floor-level view of the tavern." (`Appendix_D:262`).
- **Sister Valdra** (Order of the Gauntlet): "Valdra has seen Rella's face at Cassalanter functions." (`Appendix_D:454`, Faction Note). Valdra's page names only Ivrala: "the one person who can recognize Ivrala Sorn on sight (DC 13 Perception when both are present)" (`campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:25`). Conflict: D6.
- **The bonded NPC (target of a future commission)**: unidentified. "Target: an NPC the party has bonded with (not a party member)." (`03-staff-and-hiring.md:104`). Quest-time: C.
- **Staff roster peers**: none named in a Rella line.

### A8. Dates, ages and time

- Service: "three years" (`Appendix_D:446`, `:452`).
- Wage: 14 gp/tenday (`Appendix_D:456`; `03-staff-and-hiring.md:104`).
- No age, birthday or start date for her post.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Rella page, line 5: "> - *Tethyrian human poisoner (Cassalanter operative), lawful evil, she/her*. Stat block: **Spy**." (`campaign/setting/notable-figures/cassalanters/12-rella-asp.md:5`)
- Organization page, line 104: "- **Rella Asp** — Tethyrian human poisoner (Cassalanter operative), lawful evil." (quoted in A1)
- Trollskull guide, line 104: "LE Tethyrian human" (quoted in A4)
- Appendix D, line 440: "*NE female human, Commoner. A Cassalanter household poisoner — here on assignment.*" (`sources/Appendix_D_-_Running_the_Tavern.md:440`). **Conflict** (D1).

**Species**
- Page, line 5: "Tethyrian human". Organization, line 104: "Tethyrian human poisoner". Trollskull guide, line 104: "LE Tethyrian human". Appendix D, line 440: "female human". No conflict in species; the appendix does not say Tethyrian.

**Pronouns**
- Page, line 5: "she/her". Appendix D, line 440: "female". Sourced; no conflict.

**Stat block**
- Page, line 5: "Stat block: **Spy**." (`12-rella-asp.md:5`)
- Appendix D, line 440: "Commoner" (`Appendix_D:440`). **Conflict** (D2).
- No other source gives a stat block for her. The Seffia team's "2 **Spies**" (`campaign/guides/factions/11-cassalanters.md:17`) is a team roster, not Rella's stat.

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/cassalanters/12-rella-asp.md`. The page has no Background, Personality or Connections section yet. Each row says whether the sentence is day-one and where its fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Tethyrian human poisoner (Cassalanter operative), lawful evil, she/her*. Stat block: **Spy**." | Day-one per the organization page, but the alignment and stat conflict with Appendix D (D1, D2) | Section B |
| 2 | L6 | "**Affiliation:** The Cassalanters (operative)" | Day-one | `10-cassalanters.md:104`, `:53` |
| 3 | L7 | "**Featured in:** Background figure; no scripted appearance." | Conflicts with the Trollskull guide's candidate row (D7) | `03-staff-and-hiring.md:104`; `ev-06-the-grand-opening.md:22` |
| 4 | L11 | "**Resonance.** Rella should inspire initial warmth with her impressive culinary credentials; growing unease as her interest in patron identities exceeds any culinary curiosity; and cold horror when the commission becomes clear." | "cold horror when the commission becomes clear" is quest-time (the commission). The rest is day-one characterization | Commission: `Appendix_D:448`, `:458`; `03-staff-and-hiring.md:104` |
| 5 | L13 | "**Emotions.** Rella most often feels professional focus, the calm of someone who has done this before, a cook's genuine pride in the cover work, controlled patience, and the specific discipline of someone who does not rush." | Day-one. "a cook's genuine pride in the cover work" fits Appendix D's "chef's cover" (D3) | `Appendix_D:446`; `Appendix_D:450` |
| 6 | L15 | "**Motivations.** Rella wants to collect intelligence on the tavern's regular patrons, stay employed and inconspicuous until the commission activates, and execute the commission cleanly when the target appears." | "collect intelligence on the tavern's regular patrons": day-one (`03-staff-and-hiring.md:104`; `Appendix_D:446`). "until the commission activates, and execute the commission cleanly when the target appears": quest-time. Motivations stay verbatim per ruling 3; the commission clause is restated or removed in drafting | `Appendix_D:448`; `03-staff-and-hiring.md:104` |
| 7 | L17 | "**Inspirations.** When playing Rella, channel Amy Dunne (*Gone Girl*, the controlled, patient professional), Mrs. Lovett (*Sweeney Todd*, the cook with a sideline), and Nurse Ratched (*One Flew Over the Cuckoo's Nest*, the uncanny competence)." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Rella Asp is an accomplished Master Cook who arrives with excellent references, treats the kitchen with professional seriousness, and produces food that patrons remember. To those who observe carefully, her interest in who orders what and who dines with whom exceeds any normal culinary curiosity. Deep down, she is waiting for a specific name to appear in the reservation ledger, and when it does, the commission executes itself." | First two sentences: day-one (A5). "accomplished Master Cook" conflicts with Appendix D's "not a cook by trade" (D3). "Deep down, she is waiting for a specific name ... the commission executes itself": quest-time (a commission with a named target) | Commission: `Appendix_D:448`, `:458`; `03-staff-and-hiring.md:104` |
| 9 | L23 | "**Morale.** In a fight, Rella uses her kitchen knowledge to improvise and exits through the kitchen if available. She is not paid to fight." | Encounter behaviour, not an event. Keep. No source conflicts | Encounter behaviour only |
| 10 | L25 | "**Relationships.** Rella Asp is a Cassalanter operative placed as a Trollskull Manor Master Cook candidate, a poisoner whose commission to poison a bonded NPC activates in Act III, an intelligence collector reporting to Willifort Crowelle, and a staff candidate in the **Trollskull Manor** guide." | "a Cassalanter operative": day-one (`10-cassalanters.md:104`). "placed as a Trollskull Manor Master Cook candidate" and "a staff candidate in the Trollskull Manor guide": the hiring is a Trollskull Alley event (`ev-06-the-grand-opening.md:22`), routed. "a poisoner whose commission to poison a bonded NPC activates in Act III": quest-time. "an intelligence collector reporting to Willifort Crowelle": day-one (`10-cassalanters.md:117`) | Commission: `Appendix_D:448`; `03-staff-and-hiring.md:104`; hiring: `ev-06-the-grand-opening.md:22` |
| 11 | L29 | "Rella Asp is an accomplished cook who arrives at prospective employers with excellent references, treats any kitchen with professional seriousness, and produces food that patrons remember." | Day-one. **26 words** (brief limit 21). Trim in drafting | `Appendix_D:443`; `03-staff-and-hiring.md:104` |

**Voice profile (`.claude/skills/character-voices/voices/cassalanters.md`, "### Rella Asp" at lines 209-223)**

The file's secrecy header (line 3) says the "after discovery" register is "used only once the party has found the truth". The Rella profile has no after-discovery register. Its lines, with status:

> "*An accomplished cook with glowing references and a quiet interest in the reservation book.*" — line 210 (tagline; day-one)

> "- **Sound:** A pleasant, professional, calm voice." — line 212 (day-one)

> "- **Sentence shape:** Composed, competent kitchen talk, with polite, curious questions about the guests." — line 213 (day-one)

> "- **Word choice:** Culinary credentials and service: \"the reservation ledger\", \"who's dining\", dishes by name." — line 214 (day-one)

> "- **Swearing:** *Stingy · Plain · Clipped.* None on shift. She's too disciplined." — line 215 (day-one; the swearing level stays, adult table)

> "- **Personality in speech:** Professional focus and patience. Her interest in who dines with whom goes beyond any cook's curiosity, and it shows in how specific her questions are." — line 216 (day-one)

> "- **Quirks:** She reads the reservation ledger while talking. She asks who is expected tomorrow." — line 217 (day-one)

> "- **Signature phrases:** \"Who's expected tomorrow?\" / \"The fish is excellent tonight.\" / \"Leave the kitchen to me.\"" — line 218 (day-one)

> "- **Never:** She never rushes, never cooks badly, and never reveals the commission." — line 219. **Quest-time clause:** "and never reveals the commission" (the commission is Act III and conditional; restate or drop)

> "  - *Greeting:* \"Rella Asp. Master Cook. My references are on the table.\"" — line 221 (day-one; "Master Cook" conflicts with Appendix D's "not a cook by trade", D3)

> "  - *Business:* \"Who's expected this tenday? I like to plan the menu around the guests.\"" — line 222 (day-one)

> "  - *Under pressure:* \"I'm just the cook. Let me finish service.\"" — line 223 (encounter time, no event named; the line is a cover statement and stays)

Quest-time clauses in the profile, for the ruling-16 restatement (none changed yet; the drafter will report changes): line 219, "and never reveals the commission". Line 223 is encounter-time but names no event.

**Routing for the quest-time text (Trollskull Manor and the Cassalanter Villa heist)**
- `Appendix_D:448` (commission trigger and target types): "If the Cassalanter arc becomes active and the party becomes a genuine threat to the family's plans for the gold, Rella receives a commission. The target will not be a party member — Lord Victoro is too careful for that, too aware of consequences — but it will be someone the party values: a faction contact, a regular patron whose absence they will feel, or the Watch captain who has been quietly helpful."
- `Appendix_D:454` (Faction Note): "The DM should decide when (not whether) her commission arrives, based on how threatening the party has become to the Cassalanters' acquisition of the gold. If the party has had no significant interaction with the Cassalanters, she files quiet reports and does nothing else. If they have actively interfered, the commission comes within two tendays of that interference."
- `campaign/guides/trollskull-manor/04-fame.md:95`: "| Rella Asp's commission fulfilled and traced to the kitchen | −10 + Watch investigation |"
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:71`: "- A Cassalanter staff plant has been exposed (Rella Asp or Ivrala Sorn)"
- `Appendix_D:988` (fame table): "| Rella Asp's commission is fulfilled and traced back to the tavern's kitchen | −10 + Watch investigation |"
- `Appendix_D:1054`: "- Rella Asp's commission (if active): no direct revenue loss, but Watch investigation may impose Faction Pressure Penalty"
- `Appendix_D:1588`: "- A Cassalanter household operative placed as staff has been exposed — Rella Asp (Master Cook candidate) if she poisoned someone and was traced; Ivrala Sorn (Server candidate) if the party discovered her reporting arrangement. Either way, \"Willifort\" arrives to assess the damage."
- Hiring: `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22` (quoted in A3).

---

## D. Conflicts

**D1. Alignment: LE or NE**
- Rella page, line 5: "lawful evil, she/her"
- Trollskull guide, line 104: "LE Tethyrian human"
- Organization page, line 104: "Tethyrian human poisoner (Cassalanter operative), lawful evil."
- Appendix D, line 440: "*NE female human, Commoner. A Cassalanter household poisoner — here on assignment.*"
- Ranking: all three campaign files say LE, and they outrank Appendix D. The appendix is stale on this point; the orchestrator decides whether to edit it.

**D2. Stat block: Spy or Commoner**
- Rella page, line 5: "Stat block: **Spy**."
- Appendix D, line 440: "Commoner"
- No other source gives a stat block. Campaign ranks above the appendix.

**D3. Cook or poisoner first**
- Rella page, line 21: "an accomplished Master Cook"
- Trollskull guide, line 104: "Exceptional cook."
- Appendix D, line 446: "not a cook by trade but a poisoner who maintains a chef's cover as her primary identity"
- Not settled. The campaign files say cook; the appendix says the cover is primary. The drafter should keep the cook identity as the cover and say "poisoner" as her trade only if the orchestrator agrees.

**D4. Cult and knowledge**
- Organization page, line 52: "The six cult members are Willifort the butler, Tissina Khyret the attendant, Nana Rosse the twins' caretaker, Jandar Chergoba the head chef, and the field pair Seffia Naelryke and Arn Xalrondar." Rella is not among them.
- Organization page, line 53: "Rella Asp and Ivrala Sorn work under the covers of a cook and a server and report to Willifort (their pages in Notable Figures)."
- Appendix D, line 446: "handling the quiet aspects of the family's infernal obligations that require subtlety rather than summoned devils."
- The campaign files do not name her a cult member. The appendix implies she knows the infernal side. Cassalanter secrecy allows household knowledge but does not say she has it. The orchestrator decides; this file does not settle it.

**D5. The courier and the Dock Ward**
- Appendix D, line 452: "A character who follows the courier traces back to a Dock Ward contact used by Cassalanter household errands."
- The campaign files say nothing about the courier. No conflict; the detail exists only in the appendix.

**D6. Sister Valdra's recognition**
- Appendix D, line 454: "Order of the Gauntlet characters who have spoken with Sister Valdra (see Bouncer candidates) may receive advance warning — Valdra has seen Rella's face at Cassalanter functions."
- Valdra's page, `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:25`: "the one person who can recognize Ivrala Sorn on sight (DC 13 Perception when both are present)"
- Trollskull guide, `03-staff-and-hiring.md:77` (Valdra's row): "Recognizes Ivrala Sorn by face if both are employed simultaneously (DC 13 Perception)."
- Appendix D, line 256 (Ivrala's Hidden Quality): "Sister Valdra (Bouncer candidate 4) has seen her at Cassalanter social functions and will recognise her with a DC 13 Perception check if both are in the tavern at the same time."
- Valdra's campaign page and the Trollskull guide name Ivrala only. Appendix D line 454 names Rella too. Ranking: the campaign files outrank the appendix, and no campaign file records Valdra and Rella meeting.

**D7. Appearance status**
- Rella page, line 7: "**Featured in:** Background figure; no scripted appearance."
- Trollskull guide, `03-staff-and-hiring.md:104`: she is one of five Master Cook candidates, with a wage and a hiring effect.
- Trollskull Alley ev-06, line 22: "In the days before opening, candidates arrive for each open position."
- Not a fact conflict. The page says "no scripted appearance"; the guide puts her on the candidate list that the event brings in. The drafter should report which reading is used.

**D8. Trollskull guide's reference to a missing entry**
- `03-staff-and-hiring.md:104`: "Commission mechanics per the **Cassalanter Villa** encounter entry."
- No such entry was found: `campaign/structure/arc-g-cassalanter-villa.md` and `campaign/locations/cassalanter-villa/` have no match for "commission", "Master Cook" or "Rella". See Not found.

---

## E. Stale lines in other files (not edited)

- `sources/Appendix_D_-_Running_the_Tavern.md:440`: "NE female human, Commoner." Conflicts with the campaign (D1, D2).
- `sources/Appendix_D_-_Running_the_Tavern.md:446`: "not a cook by trade" (D3).
- `sources/Appendix_D_-_Running_the_Tavern.md:454`: "Valdra has seen Rella's face at Cassalanter functions." (D6). No campaign file records this.
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:104`: "Commission mechanics per the **Cassalanter Villa** encounter entry." No such entry (D8).
- `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:25`: names Ivrala only (D6); the appendix names Rella too.
- `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:149`: "Routed to quests: Ivrala's tobacconist drop is Dock Ward in `guides/trollskull-manor/03-staff-and-hiring.md:56` and High Road in `Appendix_D_-_Running_the_Tavern.md:252`." This is Ivrala's drop, not Rella's; the Dock Ward courier in Appendix D line 452 is a different detail. Noted for the drafter so the two are not merged.

**Routed quest references (where the events live; none is a day-one fact)**
- The commission: `Appendix_D:448`, `:454`, `:458`; `03-staff-and-hiring.md:104`; `04-fame.md:95`; `09-response-teams-at-the-tavern.md:71`; `Appendix_D:988`, `:1054`, `:1588`.
- The hiring: `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22`; `Appendix_D:439` (Candidate 2 heading), `:420` (Master Cook Candidates heading); `03-staff-and-hiring.md:99`-`:104`.

---

## F. Gaps a Background would need that no source gives

For each gap: the sourced facts the drafter must stay consistent with.

- **F1. Origin, birthplace, age, family, childhood.** No source. Constraints: Tethyrian human (page, line 5); female (`Appendix_D:440`); the page's Overview says she "arrives at prospective employers with excellent references" (line 29).
- **F2. Training and career before the Cassalanters.** No source. Constraints: "three reputable establishments, all of which confirm her excellence" (`Appendix_D:443`); the establishments are not named. Her references are "in a small leather portfolio, organized by date" (`Appendix_D:443`). The "Master Cook" title (page, line 21) is her cover claim, not a verified rank.
- **F3. How and when she joined the Cassalanters.** No source. Constraints: three years of service (`Appendix_D:446`); "listed in guild records as their household cook for the past three years, which is true as far as it goes" (`Appendix_D:452`); "Lord Victoro places enormous value on her discretion and her skill." (`Appendix_D:446`).
- **F4. Whether she knows the pact.** No source (D4). Constraints: not among the six cult members (`10-cassalanters.md:52`); a household operative reporting to Willifort (`10-cassalanters.md:117`).
- **F5. Her own name and any alias.** No source. "Rella Asp" appears in every file, with no alias.
- **F6. Her personal wants.** No source beyond Motivations (line 15) and Emotions (line 13). A personal-goals paragraph must belong to her and not to the commission (brief ruling 17), and must not reveal the commission.
- **F7. The bonded NPC she would poison.** Unidentified by design: "an NPC the party has bonded with (not a party member)" (`03-staff-and-hiring.md:104`); "a faction contact, a regular patron whose absence they will feel, or the Watch captain who has been quietly helpful." (`Appendix_D:448`). Quest-time; do not name a target on day one.
- **F8. Her relationship with Ivrala beyond the placement note.** Constraints: "Combination Note" (`Appendix_D:262`); "Rella Asp and Ivrala Sorn work under the covers of a cook and a server and report to Willifort" (`10-cassalanters.md:53`).
- **F9. Whether she has a home, companion or family.** No source.

---

## G. Inner-life hints (exact quotes)

- Rella page, line 13: "a cook's genuine pride in the cover work" and "the specific discipline of someone who does not rush."
- Rella page, line 23: "She is not paid to fight."
- Voice, `cassalanters.md:215`: "None on shift. She's too disciplined."
- Voice, `cassalanters.md:219`: "She never rushes, never cooks badly, and never reveals the commission."
- Voice, `cassalanters.md:223`: "I'm just the cook. Let me finish service."
- `Appendix_D:446`: "She is not here to poison the party."
- `Appendix_D:446`: "Lord Victoro places enormous value on her discretion and her skill."
- `Appendix_D:450`: "She poisons no one who is not on her list. She considers this a professional standard."
- `Appendix_D:443`: "\"I'm looking for a kitchen with some ambition,\" she says. \"I think this place has potential.\""
- `03-staff-and-hiring.md:104`: "Exceptional cook." and "She will be gone before they trace it."
- Rella page, line 21 (quest-time; do not restate as day-one): "Deep down, she is waiting for a specific name to appear in the reservation ledger, and when it does, the commission executes itself."

No personal goal beyond Motivations and Emotions is given in any source.

---

## Cross-references (every `file:line` where Rella appears)

- `campaign/setting/notable-figures/cassalanters/12-rella-asp.md:5`, `:7`, `:11`, `:13`, `:15`, `:17`, `:21`, `:23`, `:25`, `:29`
- `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:41`, `:101`, `:116`, `:149`
- `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:25`, `:29`
- `campaign/setting/organizations/10-cassalanters.md:52`, `:53`, `:67`, `:104`, `:105`, `:117`
- `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:25`
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56`, `:77`, `:99`, `:104`
- `campaign/guides/trollskull-manor/04-fame.md:95`
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:71`
- `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:22`
- `campaign/guides/factions/11-cassalanters.md:107` (Notable Figures list)
- `sources/Appendix_D_-_Running_the_Tavern.md:252`, `:256`, `:262`, `:420`, `:439`, `:440`, `:443`, `:446`, `:448`, `:450`, `:452`, `:454`, `:456`, `:458`, `:988`, `:1054`, `:1588`

## Not found

- Adventure: `sources/adventure-wdh.json`, grep `Rella|Asp\b`: no match.
- Campaign: grep `Rella|Ivrala|Sorn\b` across `campaign/`: only the files above. `commission|Master Cook|Rella` in `campaign/structure/arc-g-cassalanter-villa.md` and `campaign/locations/cassalanter-villa/`: no match. So the "Cassalanter Villa encounter entry" that the Trollskull guide names does not exist in those files.
- Quests: `Master Cook|candidate` in `campaign/quests/` matched only the hiring generics and other candidates. No quest file names Rella.
- Alexandrian PDFs: Rella was not found in PDFs 5, 6, 7 (PDF pp.1-3), 10 (p.5), 17 (p.2) or 27 (p.1). Other PDFs not read for her.
- Appendices B and C: no Rella line (grep returned Appendix D only).
- Wiki: `sources/research/**/wiki*` for "Rella": no match.
- `Act_III_Arc_E.md`: no Rella line.
- No note in any campaign file gives her history before Cassalanter service.

## Not readable

- `sources/Other remix files/The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx`: a secondary NPC reference (`sources/SOURCE_GUIDE.md:695`). It may name Rella. Needs extraction.
- `sources/Other remix files/Cassalanters, their tragic backtstory, and Endgame setup.docx`: the SOURCE_GUIDE says it covers the Cassalanter backstory and endgame (`sources/SOURCE_GUIDE.md:687`). It may hold Rella's history. Needs extraction.
