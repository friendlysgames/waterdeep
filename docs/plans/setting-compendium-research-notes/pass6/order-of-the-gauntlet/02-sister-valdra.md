# Pass 6 research notes: Sister Valdra

Page: `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. The page has a Persona and Relationships, so this note treats her as a major NPC (brief ruling 2) for Personality and Connections. The sources are thin, so the Background is short and tagged where it goes beyond them.
Organization page: `campaign/setting/organizations/04-order-of-the-gauntlet.md`
Factions Guide: `campaign/guides/factions/05-order-of-the-gauntlet.md`
Voice profile: `.claude/skills/character-voices/voices/order-of-the-gauntlet.md` (### Sister Valdra, lines 23-37; note at line 39)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json` has no Valdra, Ivrala or Rella line (Grep "Gauntlet|Valdra|Ivrala|Rella" returned Order lines only). The Order's general text is at `sources/adventure-wdh.json:1403-1412` and `:3938-3950` (quoted in the Savra notes file).
- Wiki: the scratchpad extract `wiki-order-of-the-gauntlet/02-sister-valdra.txt` is the stub `NOT FOUND`. A Grep of `sources/research/` for "Valdra" found no wiki page for her. The hits are campaign-hits bundles only.
- Alexandrian appendices: `sources/Appendix_D_-_Running_the_Tavern.md` (the tavern candidates) is the only source that gives her sex, class, age and species. `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md` do not name her.
- Alexandrian PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf` was read as rendered images, PDF pp.1 to 10 (printed pp.178 to 187: patron tables, bartenders, barmaids, cooks, events). No Valdra, bouncer or Order line is on those pages. PDF pp.11 onward were not read. `sources/3. Player Character Factions.pdf` p.3 (printed p.25) has no Valdra line. Both PDF quotes, if any are used, need a `pdftotext -layout` check.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The recognition conflict has several versions, and the page's own version is one of them.** The page (`02-sister-valdra.md:25`) says Valdra can recognize Ivrala Sorn "(DC 13 Perception when both are present)". Appendix D:256 says Ivrala, seen "at Cassalanter social functions", and recognized "if both are in the tavern at the same time". Appendix D:454 says Valdra "has seen Rella's face at Cassalanter functions". The Ivrala page's Persona says "Cassalanter Villa's staff quarters" (`13-ivrala-sorn.md:67`). Quoted in full in D1.
2. **Her species is half-orc in every campaign file.** Appendix D:597 says "LG female human". The page follows the campaign (D2).
3. **Her ward is in conflict.** Appendix D:603 says the Cassalanter activity is in "the North Ward". The Order's organization page says "a Sea Ward noble family" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:66`) (D3).
4. **Her three pieces of intelligence are named only in the voice profile.** The page does not say what they are. The voice's Business line names "a servant's story the Watch threw out", "a ledger" and "what I saw at the villa gate" (`order-of-the-gauntlet.md:36`). The Persona leaves the three unspecified. Appendix D:605 says they "are not yet in the party's possession" (D4).
5. **The voice profile's wage does not match the staff guide.** The voice says "Bouncer work, three silver a night." (`order-of-the-gauntlet.md:35`). The staff guide says "6 gp (will accept 4 gp)" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`). Appendix D:609 says "Wage: 6 gp/tenday." (D5).
6. **The "people who look closely stop being seen" clause on her Persona has no source.** It appears only on her page (`02-sister-valdra.md:21`). Tag it `[design]` or cut it (F2).

---

## A. Background facts by theme

### A1. Origin, species, age and career

**Campaign, Summary (species, class, alignment, pronouns)**
> "> - *Half-orc cleric of Tyr, lawful good, she/her*. Stat block: **Priest**."
> — `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:5`

**Campaign, Organization page, Key Members**
> "- **Sister Valdra** — Lawful Good half-orc cleric of Tyr; unofficial Order operative (unsanctioned by Savra); holds three independent pieces of Cassalanter intelligence. See the **Sister Valdra** page in Notable Figures."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:91`

**Campaign, Organization page, GM Notes**
> "> - **Sister Valdra:** She is a half-orc cleric of Tyr who built a case against the Cassalanters on her own time, from a servant's story the Watch dismissed. Savra does not know her. She holds the same suspicion as the Order and none of its proof."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:105`

**Campaign, Tyr page (the same role, with the suspicion rule)**
> "> - **Sister Valdra:** A half-orc cleric of Tyr and an unofficial Order operative whom Savra does not know. She has built a case against the Cassalanters on three months of her own time and a servant's story the Watch dismissed. She cannot say what the family hides, only that it is too generous and too perfect, so what she holds is suspicion and nothing more. No Order event uses her."
> — `campaign/setting/deities/tyr.md:77`

**Campaign, Trollskull staff guide, bouncer row (the day-one hiring pool)**
> "| 4 | **Sister Valdra** | LG half-orc | Plain dark coat, coiled stillness. Does not offer references. \"I'm between postings. I've heard this tavern has connections to the Order of the Gauntlet. I'd like to know what I'm walking into before I agree to anything.\" Personal initiative — investigating the Cassalanters on her own time; Savra Belabranta does not know she is here. Has 3 pieces of Cassalanter intelligence the party does not have. Shares them if the party demonstrates trustworthiness (OotG affiliation or a direct act of good faith). Recognizes Ivrala Sorn by face if both are employed simultaneously (DC 13 Perception). | Order of the Gauntlet (unofficial — personal assignment, not sanctioned by Savra). | 6 gp (will accept 4 gp) | Advantage on Event nights. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`

**Adventure:** no Valdra line (Grep, `sources/adventure-wdh.json`).

**Appendix D, Candidate 4 (sex, class, species, alignment)**
> "**Candidate 4 — Sister Valdra**"
> "*LG female human, Tough (Order of the Gauntlet adjacent). She is here for her own reasons.*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:596-597`

**Appendix D, Candidate 4, narrative block (the only age in any file)**
> "She wears a plain dark coat over clothing that might have once been martial. She is perhaps thirty-five, with the kind of stillness that comes from training rather than temperament — a coiled quality that makes her seem smaller than she is until you notice how she is standing. She does not offer references. \"I'm between postings,\" she says. \"I've heard this tavern has connections to the Order of the Gauntlet. If that's true, I'd like to be useful in the area for a while. I won't cause you trouble. I will handle trouble if it arrives. I'd like to know what I'm walking into before I agree.\""
> — `sources/Appendix_D_-_Running_the_Tavern.md:600`

**Appendix D, what she is doing (the Appendix's own description)**
> "Sister Valdra is an Order of the Gauntlet member who has been quietly investigating Cassalanter family activity in the North Ward on her own time. She has no authorization for this; she is acting on suspicion she hasn't yet been able to verify. She is using the bouncer position as a legitimate cover and income source while she watches. She is an exceptional bouncer. She is also an ongoing complication once the Cassalanter arc becomes active."
> — `sources/Appendix_D_-_Running_the_Tavern.md:603` (the "North Ward" clause conflicts with the Sea Ward; D3)

**Campaign, rank and standing**
- "unofficial Order operative" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:91`). Session 45 decided it: "### Valdra stays unofficial" (`session 45 handoff.md:51`). The Factions Guide: "an unofficial operative who appears in no Order event" (`campaign/guides/factions/05-order-of-the-gauntlet.md:92`).

### A2. Faith and role

**Campaign, Organization page, Structure (the Halls of Justice is her Order's temple)**
> "The Halls of Justice is the temple of Tyr in the Castle Ward, and the priests of its three temples help the Order without belonging to it."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:49` (no source gives Valdra a home temple)

**Campaign, Organization page, Doctrine and Rites (the Order's epithet for Tyr)**
> "Savra calls Tyr the Maimed God, while the priests at the Halls of Justice call him the Just God and the Even-Handed (**Tyr**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:45` (the epithet Valdra's voice uses is in the voice profile; see A4)

**Campaign, Persona line of her page (the cover role)**
> "To the world, Sister Valdra is a half-orc temple guard who does security work and looks for honest employment as a bouncer or muscle."
> — `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:21` (the "temple guard" cover is the page's word; the org page and the Tyr page say "cleric of Tyr"; see D6)

### A3. Her case against the Cassalanters (day-one)

**Campaign, Organization page, Timeline (the servant's story and her start)**
> "- **About six months before the campaign, a servant's story:** A servant tells the Watch a story about the Cassalanters, and the Watch dismisses it. About three months before the campaign, Sister Valdra, a half-orc cleric of Tyr, begins to build a case from that story on her own time. She acts without orders and without telling Savra (**Sister Valdra**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:28`

**Campaign, Open Lord's Watch page (the Watch's side of the same story)**
> "- **The Order of the Gauntlet (wary neutral):** The Order's knights are more aggressive and less subtle than the Watch. Its file records that the Watch closed every complaint against one noble family without findings, and Sister Valdra's case rests on a servant's story that the Watch dismissed (**The Order of the Gauntlet**)."
> — `campaign/setting/organizations/11-open-lords-watch.md:67`

**Campaign, Organization page, Methods ("Watching a family"): the ward and the family**
> "- **Watching a family:** The Order has a particular interest in the Cassalanters — a Sea Ward noble family whose impeccable public piety and conspicuous generosity the Order finds deeply suspicious. Months of quiet surveillance have produced no actionable evidence. Something is concealed behind the charity and the temple attendance; the Order cannot yet prove what. The Order grows more impatient for hard evidence it can act on. Savra names no household until a document or a sworn answer does (**Field Ward**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:66`

**Campaign, Organization page, Cassalanters (Valdra's three pieces, suspicion only)**
> "- **The Cassalanters (suspected enemy):** The Order finds the family's public piety and generosity deeply suspicious. Savra and her chapter suspect a diabolist or infernalist hand behind the family and name no pact, and nobody in the Order knows what the family worships. The chapter holds no legal evidence, and Sister Valdra holds three pieces of intelligence of her own (**The Cassalanters**; **Sister Valdra**). Mirt suspects Cassalanter money stood behind the Howling Hatred, and no source says Savra has heard it (**The Cassalanters** in Villains)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:82`

**Campaign, Cassalanter organization page (Valdra's pieces, day-one)**
> "- **The Order of the Gauntlet (enemy, on suspicion only):** Savra Belabranta has suspected the family for months and has no legal evidence, and the Order will move aggressively once it has some. Sister Valdra holds three independent pieces of Cassalanter intelligence, and nobody in the Order knows what the family worships (**The Order of the Gauntlet**)."
> — `campaign/setting/organizations/10-cassalanters.md:81`

**Campaign, Trollskull staff guide (the pieces are not handed over on day one)**
> "Has 3 pieces of Cassalanter intelligence the party does not have. Shares them if the party demonstrates trustworthiness (OotG affiliation or a direct act of good faith)."
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77` (the row in A1)

**Appendix D, the pieces (not in the party's hands)**
> "**Hidden Quality:** She will tell the characters about her investigation if they demonstrate they are trustworthy — this requires either Order of the Gauntlet affiliation or a specific act that reveals their values. She has three pieces of intelligence about the Cassalanters that are not yet in the party's possession."
> — `sources/Appendix_D_-_Running_the_Tavern.md:605`

### A4. Her voice, speech and temperament (from the voice profile)

**Voice profile (Sister Valdra, lines 23-37; verbatim in the drafter's Voice block)**
- Tagline, line 24: "*A dogged half-orc temple guard who built a case nobody asked for and finally has someone to tell.*"
- Sound, line 26: "- **Sound:** A deep, rough, steady voice. It speeds up with suppressed urgency when she's finally allowed to talk about the case."
- Sentence shape, line 27: "- **Sentence shape:** Short, practical sentences in her bouncer role. When she presents evidence, organised, numbered and precise, like a prosecutor."
- Word choice, line 28: "- **Word choice:** Guard's plainness and investigator's precision: \"evidence\", \"witness\", \"on record\". Tyr is \"the Just God\". She calls the servant whose story no one believed by name."
- Swearing, line 29: "- **Swearing:** *Casual · Plain · Phrase.* Casual in her bouncer role (\"Out, and take your shit with you.\"). Controlled when presenting the case."
- Personality in speech, line 30: "- **Personality in speech:** Focused determination and months of controlled anger. Relief at finally being heard makes her talk too fast. Her voice holds suspicion only (see the note below): \"something is wrong in that house\", never a named devil."
- Quirks, line 31: "- **Quirks:** She lays out evidence in order, with \"one, two, three\". She checks who else is listening before she starts."
- Signature phrases, line 32: "- **Signature phrases:** \"I have it on record.\" / \"Nobody believed her.\" / \"One. Two. Three.\""
- Never, line 33: "- **Never:** She never exaggerates the evidence, never involves Savra officially, and never names what the Cassalanters worship, because she doesn't know."
- Sample lines, lines 34-37. Greeting, line 35: "  - *Greeting:* \"Bouncer work, three silver a night. You look like trouble. Good trouble or the other kind?\"" Business, line 36: "  - *Business:* \"Three things. One, a servant's story the Watch threw out. Two, a ledger. Three, what I saw at the villa gate. Something is wrong in that house.\"" Under pressure, line 37: "  - *Under pressure:* \"Get behind the bar. Nobody touches the witness.\""
- Note, line 39: "> Note: Sister Valdra's Notable Figures page says her evidence links the villa \"to Asmodeus worship\". That conflicts with the CLAUDE.md Cassalanter secrecy rule (suspicion only, never knowledge). Her voice follows the rule. Fix the page."
— `.claude/skills/character-voices/voices/order-of-the-gauntlet.md:24-39`. Line 39 is stale: the current page has no "Asmodeus" line (D7).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "*Half-orc cleric of Tyr, lawful good, she/her*." — `02-sister-valdra.md:5`
- Campaign, Organization page, Key Members: "Lawful Good half-orc cleric of Tyr" — `campaign/setting/organizations/04-order-of-the-gauntlet.md:91`
- Campaign, staff guide: "LG half-orc" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`
- Appendix D: "*LG female human, Tough (Order of the Gauntlet adjacent). She is here for her own reasons.*" — `sources/Appendix_D_-_Running_the_Tavern.md:597` (alignment matches; species conflicts; D2)
- Adventure and wiki: no Valdra line.

**Species**
- Campaign: "half-orc" (Summary line 5; Key Members `04-order-of-the-gauntlet.md:91`; staff guide `03-staff-and-hiring.md:77` "LG half-orc"; Tyr page `campaign/setting/deities/tyr.md:77` "A half-orc cleric of Tyr").
- Appendix D: "female human" (`sources/Appendix_D_-_Running_the_Tavern.md:597`). Conflict; D2.

**Pronouns**
- Campaign: "she/her" (Summary line 5).
- Appendix D: "female" (`sources/Appendix_D_-_Running_the_Tavern.md:597`).
- Gruumsh page: "Pronouns checked: Yagra (she/her), Ziraj (he/him), Hrabbaz (he/him), Grevik Nass (he/him) and Sister Valdra (she/her) come from their Notable Figures pages and the event files." — `campaign/setting/deities/gruumsh.md:131`

**Stat block**
- Summary: "Stat block: **Priest**." (`02-sister-valdra.md:5`). No other campaign line gives a stat block for her (Grep for "Valdra" across `campaign/`, `sources/` and `.claude/` found no other stat-block line).
- No CR, AC or HP in any file. The Priest block is the page's label only [research].

**Age**
- "She is perhaps thirty-five" (`sources/Appendix_D_-_Running_the_Tavern.md:600`). No other age in any file.

---

## C. Sentences on the current page that narrate a quest-time event or depend on a discovery

Current page: `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md`. The page has no Background, Personality or Connections section yet. Each row says where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Half-orc cleric of Tyr, lawful good, she/her*. Stat block: **Priest**." | Day-one name tag. Stat block "Priest" has no source (B) | `campaign/setting/organizations/04-order-of-the-gauntlet.md:91`; `campaign/setting/deities/tyr.md:77`; section B |
| 2 | L6 | "> - **Affiliation:** Order of the Gauntlet (unofficial)" | Day-one label; matches the org page | `campaign/setting/organizations/04-order-of-the-gauntlet.md:91` ("unofficial Order operative") |
| 3 | L7 | "> - **Featured in:** Background figure; she appears in no Order of the Gauntlet event and Savra does not know her. She is a staff candidate in the **Trollskull Manor** guide." | Routed status ("appears in no Order event") and a guide fact. Day-one as a candidate | `campaign/guides/factions/05-order-of-the-gauntlet.md:92` ("an unofficial operative who appears in no Order event"); `campaign/setting/organizations/04-order-of-the-gauntlet.md:105` (Savra does not know her); `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77` |
| 4 | L11 | "**Resonance.** Sister Valdra should inspire immediate respect for the specificity of her evidence; sympathy for a woman who built a case no one asked her to build; and protective frustration that Savra cannot know and therefore cannot officially help." | Day-one. Keep (ruling 3) | `campaign/setting/organizations/04-order-of-the-gauntlet.md:28`; `campaign/setting/deities/tyr.md:77` |
| 5 | L13 | "**Emotions.** Sister Valdra most often feels focused determination, the controlled anger of someone who has been right for months and cannot get anyone official to act, genuine care for the servant whose story no one believed, and quiet relief when she finally finds someone willing to listen." | Day-one, except "quiet relief when she finally finds someone willing to listen", which describes a response to a listener. Flag as possible quest-time; keep verbatim unless the drafter rules otherwise | `campaign/setting/organizations/04-order-of-the-gauntlet.md:28`; voice `order-of-the-gauntlet.md:30` ("Relief at finally being heard makes her talk too fast.") |
| 6 | L15 | "**Motivations.** Sister Valdra wants to build a case against the Cassalanters that Savra or the Watch can act on, protect the people who can still be protected, and work within Tyr's framework even when the framework is slow." | Day-one | `campaign/setting/organizations/04-order-of-the-gauntlet.md:28`; `campaign/setting/organizations/11-open-lords-watch.md:67` |
| 7 | L17 | "**Inspirations.** When playing Sister Valdra, channel Erin Brockovich (*Erin Brockovich*), Rosa Diaz (*Brooklyn Nine-Nine*), and Brienne of Tarth (*Game of Thrones*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Sister Valdra is a half-orc temple guard who does security work and looks for honest employment as a bouncer or muscle. To those who earn her trust, she has been building a case against the Cassalanters for three months on her own time, without orders and without telling Savra, based on a servant's story the Watch dismissed six months ago. Deep down, she holds three pieces of evidence that something is badly wrong behind the villa's charity (she cannot say what, only that the family is too generous, too perfect, and that people who look closely stop being seen), and she has been waiting for someone with the authority — or the recklessness — to use them." | The timeline is day-one (org `:28`). "three pieces" is day-one (`03-staff-and-hiring.md:77`). "people who look closely stop being seen" has no source (F2). "waiting for someone ... to use them" is a wish, not an event | `campaign/setting/organizations/04-order-of-the-gauntlet.md:28`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`; `sources/Appendix_D_-_Running_the_Tavern.md:605`. "stop being seen": no source |
| 9 | L23 | "**Morale.** In a fight, Sister Valdra positions herself at the front and does not retreat from a threat to someone in her care. She calls on Tyr and means it." | Encounter register. The sentence has no source line | None found (F5) |
| 10 | L25 | "**Relationships.** Sister Valdra is an unofficial Order of the Gauntlet operative (unsanctioned by Savra Belabranta), the holder of three independent pieces of Cassalanter intelligence, the one person who can recognize Ivrala Sorn on sight (DC 13 Perception when both are present), and a Trollskull Manor bouncer candidate." | Operative and three pieces are day-one. The recognition clause is a Trollskull mechanic that depends on both women being in the tavern, and the sources give several versions (D1). "the one person who can recognize" is contradicted by Appendix D:454 (Valdra has seen Rella's face) | `campaign/setting/organizations/04-order-of-the-gauntlet.md:91`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56` and `:77`; `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:71`; `sources/Appendix_D_-_Running_the_Tavern.md:256` and `:454` (D1) |
| 11 | L29 | "A half-orc temple guard between postings who takes security and bouncer work, observant past what the job demands, and deliberate about who she trusts." | Day-one. Overview is 24 words (brief limit: 21) | `sources/Appendix_D_-_Running_the_Tavern.md:600` ("I'm between postings"); `:603` ("She is an exceptional bouncer.") |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/order-of-the-gauntlet.md`, "### Sister Valdra", lines 23-37)**

Each line is listed with its status. Ruling 16 says a quest-time clause gets a day-one restatement and the profile is changed to match.

- Line 24 (tagline): day-one.
- Line 26 (Sound): day-one.
- Line 27 (Sentence shape): day-one.
- Line 28 (Word choice): "She calls the servant whose story no one believed by name." — day-one as a habit, but **no source names the servant** (F1).
- Line 29 (Swearing): day-one. Swearing stays (adult table).
- Line 30 (Personality in speech): "Relief at finally being heard makes her talk too fast." — the same response to a listener as Emotions line 13 (C row 5). "Her voice holds suspicion only" is day-one.
- Line 31 (Quirks): day-one.
- Line 32 (Signature phrases): "I have it on record." and "Nobody believed her." — day-one as habit. "I have it on record" implies a written record she holds; no source describes one. Flag as a voice choice, not a fact.
- Line 33 (Never): "She never ... involves Savra officially" — day-one (org `campaign/setting/organizations/04-order-of-the-gauntlet.md:105`).
- Line 35 (Greeting): "Bouncer work, three silver a night. You look like trouble. Good trouble or the other kind?" — a hiring line from the Trollskull guide. The wage conflicts with the staff guide (D5). Flag as hiring-time speech.
- Line 36 (Business): "Three things. One, a servant's story the Watch threw out. Two, a ledger. Three, what I saw at the villa gate. Something is wrong in that house." — the three pieces are day-one (`03-staff-and-hiring.md:77`), but their contents are named nowhere else (F3). Flag.
- Line 37 (Under pressure): "Get behind the bar. Nobody touches the witness." — a fight line. Day-one as habit. No source gives a witness.

**Quest-time clauses in the profile:** line 35 (Greeting, a hiring line), line 36 (Business, the three pieces named in speech) and line 37 (Under pressure, "the witness"). Lines 24 to 33 are day-one.

**Quest-time or routed sentences attached to Valdra in other files**
- `campaign/quests/faction-events/order-of-the-gauntlet/s01-the-tithe/design-notes.md:17`: "Sister Valdra is removed, because her Notable Figures page says Savra does not know her." — a design note, quest-time.
- `campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/design-notes.md:24`: "- The Notable Figures page for Sister Valdra links the villa to Asmodeus worship; she does not appear here." — stale (D7).

---

## D. Conflicts

**D1. Whom Valdra recognizes, where, and when (the known conflict)**

Versions in the sources, with the page's own line first.

- Page (current): "**Relationships.** ... the one person who can recognize Ivrala Sorn on sight (DC 13 Perception when both are present), and a Trollskull Manor bouncer candidate." — `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:25`
- Appendix D, Ivrala's entry: "**Hidden Quality:** She is almost impossible to catch. ... Sister Valdra (Bouncer candidate 4) has seen her at Cassalanter social functions and will recognise her with a DC 13 Perception check if both are in the tavern at the same time." — `sources/Appendix_D_-_Running_the_Tavern.md:256`
- Appendix D, Rella's entry: "**Faction Note:** Cassalanter household — an adversary faction. The DM should decide when (not whether) her commission arrives, based on how threatening the party has become to the Cassalanters' acquisition of the gold. If the party has had no significant interaction with the Cassalanters, she files quiet reports and does nothing else. If they have actively interfered, the commission comes within two tendays of that interference. Order of the Gauntlet characters who have spoken with Sister Valdra (see Bouncer candidates) may receive advance warning — Valdra has seen Rella's face at Cassalanter functions." — `sources/Appendix_D_-_Running_the_Tavern.md:454`
- Trollskull staff guide, Ivrala's row, Connections cell: "Sister Valdra (Bouncer #4) recognizes her by face if both are employed (DC 13 Perception)." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56`
- Trollskull staff guide, Valdra's row: "Recognizes Ivrala Sorn by face if both are employed simultaneously (DC 13 Perception)." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`
- Ivrala page, Connections: "**Sister Valdra** has seen her face at the Cassalanter villa and can recognize her." — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:32`
- Ivrala page, Resonance: "unsettled recognition in anyone who has seen her face at a Cassalanter function" — `13-ivrala-sorn.md:40`
- Ivrala page, Persona: "Deep down, Sister Valdra has seen her face in Cassalanter Villa's staff quarters, and she would recognize it." — `13-ivrala-sorn.md:67`
- Ivrala page, Relationships: "recognizable to Sister Valdra on a DC 13 Perception check when both are present" — `13-ivrala-sorn.md:71`
- Ivrala page, Secret: "> - **Who knows:** Sister Valdra can recognize her face. No source says that Valdra knows her work or that anyone outside the household and its network does." — `13-ivrala-sorn.md:77`
- Rella page, Conflicts: "> - **Conflicts:** Sister Valdra. `Appendix_D_-_Running_the_Tavern.md:454` says Valdra \"has seen Rella's face at Cassalanter functions\". `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:25` and `03-staff-and-hiring.md:77` name only Ivrala Sorn, and `Appendix_D_-_Running_the_Tavern.md:256` does the same in Ivrala's entry. The page records no recognition and leaves the question open." — `campaign/setting/notable-figures/cassalanters/12-rella-asp.md:112`
- Ivrala page, Draft Notes: "> - **Conflicts:** Where Valdra saw her. The old Persona (line 21) says \"Cassalanter Villa's staff quarters\" and `Appendix_D_-_Running_the_Tavern.md:256` says \"at Cassalanter social functions\". `02-sister-valdra.md:25` and `03-staff-and-hiring.md:77` give no place. The Persona keeps \"staff quarters\" because the campaign page outranks the appendix, and Connections says \"at the Cassalanter villa\". The Voice block says \"at a Cassalanter function\" because the line is a public tell." — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:115`

Points for the drafter:
- Target: Ivrala (page L25; `03-staff-and-hiring.md:56` and `:77`; Ivrala page) vs Rella (Appendix D:454 only).
- Place: "Cassalanter Villa's staff quarters" (Ivrala page `:67`) vs "Cassalanter social functions" (Appendix D:256) vs "Cassalanter functions" (Appendix D:454) vs "the Cassalanter villa" (Ivrala page `:32`). Valdra's page gives no place.
- Trigger: "both are present" (page L25; Ivrala page `:71`) vs "both are employed" (`03-staff-and-hiring.md:56`, `:77`) vs "both are in the tavern at the same time" (Appendix D:256).
- Higher rank: none in the sources. The brief's rulings do not settle it. The orchestrator decides (Findings #1).

**D2. Species (half-orc vs human)**
- Campaign: "Half-orc cleric of Tyr" (`02-sister-valdra.md:5`); "LG half-orc" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`); "A half-orc cleric of Tyr" (`campaign/setting/deities/tyr.md:77`).
- Appendix D: "*LG female human, Tough (Order of the Gauntlet adjacent). She is here for her own reasons.*" (`sources/Appendix_D_-_Running_the_Tavern.md:597`)
- Higher rank: the campaign. The org page Draft Notes say: "The page follows the Notable Figures page." (`campaign/setting/organizations/04-order-of-the-gauntlet.md:157`). The Appendix D line is an older tavern candidate.

**D3. The ward of the family she is watching**
- Appendix D: "Cassalanter family activity in the North Ward" (`sources/Appendix_D_-_Running_the_Tavern.md:603`)
- Organization page: "a Sea Ward noble family" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:66`)
- Sea Ward gazetteer: "Savra Belabranta of the Order of the Gauntlet hunts for proof" (`campaign/gazetteer/waterdeep/sea-ward.md:38`)
- North Ward gazetteer, a separate Cassalanter site: "It is a separate site from the temple beneath **Cassalanter Villa**." (`campaign/gazetteer/waterdeep/north-ward.md:42`, the shrine on Aveen Street)
- Higher rank: the campaign (Sea Ward, `campaign/setting/organizations/04-order-of-the-gauntlet.md:66`). The page does not name a ward.

**D4. What the three pieces are (the page is silent; the voice names them)**
- Page: "she holds three pieces of evidence that something is badly wrong behind the villa's charity (she cannot say what, only that the family is too generous, too perfect, and that people who look closely stop being seen)" (`02-sister-valdra.md:21`).
- Voice, Business line: "Three things. One, a servant's story the Watch threw out. Two, a ledger. Three, what I saw at the villa gate. Something is wrong in that house." (`order-of-the-gauntlet.md:36`)
- Tyr page: "She cannot say what the family hides, only that it is too generous and too perfect, so what she holds is suspicion and nothing more." (`campaign/setting/deities/tyr.md:77`)
- Appendix D: "She has three pieces of intelligence about the Cassalanters that are not yet in the party's possession." (`sources/Appendix_D_-_Running_the_Tavern.md:605`)
- Higher rank: none. The campaign leaves the pieces unnamed. The voice names a ledger and a sighting at the villa gate. The servant's story is the basis of her case (`campaign/setting/organizations/04-order-of-the-gauntlet.md:28`), and the Persona does not list it among the three pieces. No source settles which list is right.
- Possible overlap, not stated in any source: the Order's mission recovers "a ledger in Victoro Cassalanter's hand" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:80`). The voice's "ledger" is not linked to it anywhere.

**D5. Wage (voice vs staff guide vs Appendix D)**
- Voice, Greeting: "Bouncer work, three silver a night." (`order-of-the-gauntlet.md:35`)
- Staff guide: "6 gp (will accept 4 gp)" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`)
- Appendix D: "**Wage:** 6 gp/tenday. She considers money secondary to the mission. She will take whatever they offer down to 4 gp." (`sources/Appendix_D_-_Running_the_Tavern.md:609`)
- Higher rank: the staff guide and Appendix D agree (6 gp, down to 4 gp). The voice's "three silver a night" is a different unit and figure. If the Greeting is kept, the wage should match the staff guide.

**D6. Her role: cleric or temple guard**
- Page Summary: "Half-orc cleric of Tyr" (`02-sister-valdra.md:5`). Organization page: "a half-orc cleric of Tyr" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:105`). Tyr page: "A half-orc cleric of Tyr" (`campaign/setting/deities/tyr.md:77`).
- Page Persona: "a half-orc temple guard who does security work" (`02-sister-valdra.md:21`). Page Overview: "A half-orc temple guard between postings" (`02-sister-valdra.md:29`). Voice tagline: "A dogged half-orc temple guard" (`order-of-the-gauntlet.md:24`).
- Higher rank: none. The Persona gives "temple guard" as her public role ("To the world, ..."). The GM-facing lines call her a cleric. The drafter should keep both and say which is which.

**D7. The stale line about Asmodeus**
- Voice note: "Sister Valdra's Notable Figures page says her evidence links the villa \"to Asmodeus worship\". That conflicts with the CLAUDE.md Cassalanter secrecy rule" (`order-of-the-gauntlet.md:39`).
- Current page: no Asmodeus line. The whole of `02-sister-valdra.md` was read; no match for "Asmodeus".
- `campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/design-notes.md:24`: "- The Notable Figures page for Sister Valdra links the villa to Asmodeus worship; she does not appear here." (stale)
- Higher rank: the current page. The voice note and the m05 design note are stale. Not edited (report only).

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `.claude/skills/character-voices/voices/order-of-the-gauntlet.md:39`: "> Note: Sister Valdra's Notable Figures page says her evidence links the villa \"to Asmodeus worship\"." — stale (D7).
- `campaign/quests/faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/design-notes.md:24`: stale (D7).
- `session 33 handoff.md:115`: "  - Sister Valdra's \"Asmodeus worship\"" — the same stale line (D7).
- `session 28 handoff.md:146`: "  - Sister Valdra is a half-orc in the staff table." — consistent with the campaign.
- `session 45 handoff.md:51-53`: "### Valdra stays unofficial" with "**Decision:** She appears in none of the seven events that scripted her." and "**Reasoning:** Her Notable Figures page, the organization page and the staff guide all make her unofficial and unknown to Savra." — consistent.
- `session 45 handoff.md:22`: the Valdra part ("Valdra unofficial and in no event") is consistent. The Savra part is stale (see the Savra notes, D2).
- `campaign/setting/organizations/10-cassalanters.md:81`, `:119` and `:197`: consistent (three pieces, suspicion only). Line 197 is a routed-facts note.
- `campaign/setting/organizations/11-open-lords-watch.md:67`: consistent.
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56` and `:77`: consistent with each other; conflict with Appendix D (D1, D5).

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**
- `campaign/quests/faction-events/order-of-the-gauntlet/s01-the-tithe/design-notes.md:17`: "Sister Valdra is removed, because her Notable Figures page says Savra does not know her." — the tithe event's design.
- `campaign/quests/faction-events/order-of-the-gauntlet/r50-righteous-hand/design-notes.md` (lines 5 and 13) names Valdra. The Grep printed these lines as omitted, so their wording is not quoted here. Read the file before any use.
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`: the bouncer row, a day-one candidate row that also carries the recognition clause (D1).
- The Order's events: none name Valdra. A Grep of `campaign/quests/` for "Valdra" returns only the two design notes listed above and the m05 and s01 design notes (E1, D7).

**E3. The Trollskull Alley Order row (routed; no Valdra entry)**
- `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:27`: "| **Order of the Gauntlet** | Savra Belabranta visits Trollskull in person; no advance invitation | Any character in no other faction; a Cleric or Paladin class, an Acolyte, Guard or Soldier background, or worship of Helm, Torm or Tyr only decides whom Savra addresses first |" — no Valdra named. Valdra's renown line was removed (`session 45 handoff.md:24`).

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. The servant (no name anywhere)**
- Voice: "She calls the servant whose story no one believed by name." (`order-of-the-gauntlet.md:28`). The page and the org page say only "a servant's story the Watch dismissed" (`02-sister-valdra.md:21`; `campaign/setting/organizations/04-order-of-the-gauntlet.md:28`). No file names the servant. A Grep for "servant" found no name for the Cassalanter servant.
- A name is a new named person (brief ruling 17). The drafter must tag it `[design]` or leave it unnamed. Voice line 28 would then need the same change.
- Timing: "six months ago" (page L21) and "About six months before the campaign" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:28`). Consistent.

**F2. "People who look closely stop being seen"**
- Page only: "(she cannot say what, only that the family is too generous, too perfect, and that people who look closely stop being seen)" (`02-sister-valdra.md:21`).
- A Grep for "stop being seen" and "stopped being seen" across `campaign/`, `sources/` and `.claude/` returned no hit. A Grep for "look closely" returned only this page's line 21 among the files searched. The Ivrala page uses "looks closely" in another sense ("A reference check that looks closely enough finds that wording.", `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:76`).
- The clause has no source. It touches the Cassalanter secrecy rule, so the drafter should tag it `[design]` and check it against that rule, or cut it.

**F3. The three pieces (contents)**
- Page: unnamed (`02-sister-valdra.md:21`, `:25`). Voice: named in speech (`order-of-the-gauntlet.md:36`). Appendix D and staff guide: unnamed (`Appendix_D:605`; `03-staff-and-hiring.md:77`).
- The drafter must stay consistent with: the pieces are "suspicion and nothing more" (`campaign/setting/deities/tyr.md:77`) and "independent" (`02-sister-valdra.md:25`). They do not prove a pact (Cassalanter secrecy; CLAUDE.md).

**F4. Her early life, faith and training**
- No source gives a birth place, a home, a family, parents, a sibling, a childhood, a temple she served, or the date she became a cleric. The age "perhaps thirty-five" (`Appendix_D:600`) is the only age.
- "a half-orc temple guard" and "cleric of Tyr" are the only role facts (D6).

**F5. Her morale line and her combat role**
- "She calls on Tyr and means it." (`02-sister-valdra.md:23`) and "does not retreat from a threat to someone in her care" (same line). No source. Treat as [research] unless the drafter ties it to a source.

**F6. Her relationship with Savra**
- Savra does not know her (`campaign/setting/organizations/04-order-of-the-gauntlet.md:105`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`; `sources/Appendix_D_-_Running_the_Tavern.md:607`). Any Background line about how Savra would react is invented and must be `[design]`. The only source on Savra's reaction is Appendix D:607: "If Savra finds out, she will be divided between approving of the instinct and disapproving of the lack of authorization."

**F7. Her relationship with the Trollskull staff and patrons**
- Staff guide: "Advantage on Event nights." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`, a mechanic). Appendix D:611: "Advantage on Revenue Rolls during Event nights. +1 to faction standing with the Order of the Gauntlet per tenday she is employed (up to +3 total)." No personal relationship is given.

**F8. Her inner goals beyond the case**
- The Motivations line (`02-sister-valdra.md:15`) is the only goal. "protect the people who can still be protected" and "work within Tyr's framework even when the framework is slow" are the page's wishes. No other personal goal (a person, a place, a craft, a debt) is in any file. Any personal goal must be `[design]`.

**F9. The Order's knowledge of her**
- "Savra Belabranta does not know she is here" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`); "Savra does not know her" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:105`). No other Order member is named as knowing her.
- The Ivrala page says: "No source says that Valdra knows her work or that anyone outside the household and its network does." (`campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:77`). That is about Valdra's knowledge of Ivrala, not the Order's.

---

## G. Source facts that hint at the figure's inner life

Quotes only. The drafter uses these to write the Background and Personal goals (brief ruling 17). Do not contradict them.

**G1. The case as her private weight (day-one)**
- "a woman who built a case no one asked her to build" (`02-sister-valdra.md:11`, Resonance)
- "the controlled anger of someone who has been right for months and cannot get anyone official to act" (`02-sister-valdra.md:13`, Emotions)
- "She acts without orders and without telling Savra" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:28`)
- "She has no authorization for this; she is acting on suspicion she hasn't yet been able to verify." (`sources/Appendix_D_-_Running_the_Tavern.md:603`)

**G2. Her care for the wronged servant (day-one)**
- "genuine care for the servant whose story no one believed" (`02-sister-valdra.md:13`, Emotions)
- "She calls the servant whose story no one believed by name." (`order-of-the-gauntlet.md:28`, voice; no name in any file, F1)
- "Nobody believed her." (`order-of-the-gauntlet.md:32`, voice signature phrase)

**G3. Her wait (day-one, Persona)**
- "she has been waiting for someone with the authority — or the recklessness — to use them" (`02-sister-valdra.md:21`)
- "quiet relief when she finally finds someone willing to listen" (`02-sister-valdra.md:13`, Emotions)
- "Relief at finally being heard makes her talk too fast." (`order-of-the-gauntlet.md:30`, voice)

**G4. Her manner in the tavern (Appendix D; her cover)**
- "I'm between postings" and "I'd like to know what I'm walking into before I agree." (`sources/Appendix_D_-_Running_the_Tavern.md:600`)
- "She is using the bouncer position as a legitimate cover and income source while she watches." (`sources/Appendix_D_-_Running_the_Tavern.md:603`)
- "She does not offer references." (`sources/Appendix_D_-_Running_the_Tavern.md:600`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`)
- "She will tell the characters about her investigation if they demonstrate they are trustworthy" (`sources/Appendix_D_-_Running_the_Tavern.md:605`)

**G5. Her discipline and her grip on the work (day-one)**
- "observant past what the job demands, and deliberate about who she trusts." (`02-sister-valdra.md:29`, Overview)
- "She never exaggerates the evidence, never involves Savra officially, and never names what the Cassalanters worship, because she doesn't know." (`order-of-the-gauntlet.md:33`, voice Never line)
- "She is an exceptional bouncer." (`sources/Appendix_D_-_Running_the_Tavern.md:603`)

**G6. Her Tyr faith (day-one)**
- "work within Tyr's framework even when the framework is slow." (`02-sister-valdra.md:15`, Motivations)
- "She calls on Tyr and means it." (`02-sister-valdra.md:23`, Morale; no source line, F5)
- "Tyr is \"the Just God\"." (`order-of-the-gauntlet.md:28`, voice word choice)

**G7. Her view of the family (suspicion only; secrecy)**
- "too generous, too perfect" (`02-sister-valdra.md:21`; `campaign/setting/deities/tyr.md:77`)
- "Something is wrong in that house." (`order-of-the-gauntlet.md:36`, voice Business line)

---

## Searches with no hit

- "stop being seen" and "stopped being seen" (campaign, sources, skills): no hit (F2).
- A name for the Cassalanter servant: none (F1).
- Valdra in any Order event file under `campaign/quests/faction-events/order-of-the-gauntlet/`: none, apart from the design notes in E2.
- Valdra in `sources/adventure-wdh.json` (Grep "Valdra|Ivrala|Rella"): none.
- Valdra in the wiki (`sources/research/`): no wiki page; the hits are campaign-hits bundles only.
- Valdra's stat block other than the page's Summary: none.
- Valdra's age other than "perhaps thirty-five": none.
- Valdra in the PDFs (Addendum A pp.1 to 10; Player Character Factions p.3): none.
