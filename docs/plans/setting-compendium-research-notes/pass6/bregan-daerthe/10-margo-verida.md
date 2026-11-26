# Pass 6 research notes: Margo Verida

Page: `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Margo is a Sea Maidens Faire performer and Jarlaxle's companion. The Faire's fleet is not in Waterdeep on Ches 1 (it arrives Ches 21), so every "aboard the Eyecatcher" present-tense line is a conflict with the day-one ruling (D1). Sea Maidens Faire events are quest time. Cassalanter secrecy and the Lolth rule apply (no Margo source touches either).
Organization page: `campaign/setting/organizations/07-bregan-daerthe.md`
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md` ("### Margo Verida", lines 186-200)
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/10-margo-verida.txt` contains `NOT FOUND`. No wiki page exists for Margo Verida.

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines from that output.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` and `{@i ...}` tags are left as written. The `page` field is given where one exists.
- Alexandrian PDFs: no shell, so `pdftotext` could not run. These PDFs were rendered as page images and their quotes are transcriptions. Check exact wording with `pdftotext -layout` before any quote goes into prose:
  - `sources/9. Lair – Sea Maidens Faire.pdf` (printed pp.68-76 = PDF pp.1-9, the whole file). Read: PDF pp.1-9.
  - `sources/27. Addendum A Night in Trollskull Manor.pdf` (printed pp.178-189 = PDF pp.1-12). Read: PDF pp.1-12. Margo does not appear.
- Alexandrian text files: `sources/Appendix_B_-_Player_Factions.md`, `Appendix_C`, `Appendix_D`, `Act_III_Arc_D.md`, `Act_III_Arc_E.md`: no "Margo", "Verida" or "Khafeyta" match.
- Wiki: NOT FOUND. The pass 4 and pass 5 bundles contain only campaign-hit copies of the page and the adventure-hits file; no wiki line.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **Day-one residence conflict.** The page places Margo "aboard the Eyecatcher" in present tense (L25), and the Overview (L29) says "aboard Zardoz Zord's carnival ships". Every campaign source says the fleet arrives in Deepwater Harbor on Ches 21, not before Ches 1. See D1.
2. **Romance conflict.** The published adventure says "Jarlaxle has taken a romantic interest in both women, who are also in love with each other." The campaign calls her Jarlaxle's "friend" (L25) and "companion" (L6). The Alexandrian PDF has "romantic" in quotes (PDF p.3). See D2.
3. **Alignment conflict.** The page says "chaotic good" (L5). The published adventure says "Both are neutral good." The campaign wins. Species and pronouns agree across sources. See D3.
4. **Stat block conflict.** The page says "Stat block: **Performer Maestro**" (L5). The Alexandrian stat reference says "Margo Verida – female Amnian human bard (DH p. 195)". The session record moved the company's Performers to 2024 Performer blocks. See D4.
5. **The Overview is 32 words**, over the 21-word limit (L29). See C row 9.
6. **Quest-time clauses on the page** are the party-directed clause in Resonance (L11), the paired-cabin clause in Relationships (L25), and the Morale encounter mechanics (L23). See section C.
7. **Affiliation label.** The org page and the page both say "Bregan D'aerthe", but the published adventure's rule and the org page's own rule say non-drow operatives are not members. Margo is human. See E2.

---

## A. Background facts by theme

### A1. Origin, birth, species, former life
No source gives a birth year, birth name, home city or family. The only origin statements are her species and the Faire job.

**Page (the Gamemaster's Summary)**
> "- *Amnian human bard, chaotic good, she/her*. Stat block: **Performer Maestro**."
> — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:5`

**Published adventure, the J29 entry (page 140)**
> "Margo Verida, a female Amnian human {@creature bard|VGM} (see {@adventure appendix B|WDH|12})"
> — `sources/adventure-wdh.json:25455` (entry "J29. Guest Cabin", `"page": 140` at `:25446`)

**Published adventure, how she joined (the only join fact in any file read)**
> "Margo and Khafeyta both joined the Sea Maidens Faire within the past year-Margo as a lyrist, Khafeyta as an acrobat. Jarlaxle has taken a romantic interest in both women, who are also in love with each other."
> — `sources/adventure-wdh.json:25459` (the romance clause is D2)

**Published adventure, name key**
> "Margo Verida"
> "MAR-go veh-REE-dah"
> — `sources/adventure-wdh.json:221`-`:222` (pronunciation key entry)

**Alexandrian stat reference (PDF p.9, printed p.76)**
> "Margo Verida – female Amnian human bard (DH p. 195)"
> — `sources/9. Lair – Sea Maidens Faire.pdf` PDF p.9 (printed p.76; transcription)

**Campaign, the organization page**
> "- **Margo Verida** — Amnian human bard, chaotic good. Jarlaxle's companion aboard the *Eyecatcher*, not his employee. See the **Margo Verida** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:108`

**Campaign, the Jarlaxle page's companion list**
> "- **Margo Verida** and **Khafeyta Murzan:** The companions who travel aboard the *Eyecatcher*. They are not his employees."
> — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:55`

**Campaign, the Sea Maidens structure doc (the J29 cabin and its roles)**
> "**J29 (Guest Cabin).** Margo Verida (bard) + Khafeyta Murzan (swashbuckler). Jarlaxle's companions — skilled combatants and genuine friends. They can be charmed, deceived, or negotiated with: Margo responds to flattery about her music (DC 13 Persuasion), Khafeyta responds to a good fight story (DC 14 Persuasion). Neither will betray Jarlaxle, but both can be distracted."
> — `campaign/structure/arc-h-sea-maidens-faire.md:158`

**Campaign, the Trollskull tavern patron table**
> "| **Sea Maidens Faire** | Margo Verida |"
> — `campaign/guides/trollskull-manor/06-tavern-time.md:48`
> Slot 18 rule, same file: "Slot 18 on the Patron Table is the NPC listed here for the most recently completed quest. If that NPC is dead, hostile, or imprisoned, use the row above." — `campaign/guides/trollskull-manor/06-tavern-time.md:39`
> The Alexandrian addendum's Slot 18 is generic: "18 [Other NPC or Faction Contact]" (`sources/27. Addendum A Night in Trollskull Manor.pdf` PDF p.5, printed p.184; transcription). The Margo mapping is a campaign addition, not an Alexandrian fact.

### A2. How she joined and rose
- Published adventure: "Margo and Khafeyta both joined the Sea Maidens Faire within the past year-Margo as a lyrist, Khafeyta as an acrobat." (`sources/adventure-wdh.json:25459`). This is the only join fact in any file read.
- Campaign: none. The page does not say how or when she joined.
- Published adventure, the captured captain's report, which names her as one of the Faire's stars: "\"Zord has a cabin aboard the {@i Eyecatcher} and spends a lot of time there with Margo Verida and Khafeyta Murzan, two of the Faire's star performers.\"" — `sources/adventure-wdh.json:23033`

### A3. Post and time in post
Only the join line (A2). The Faire's arrival is Ches 21 in campaign files:
> "The Faire fleet ties up at the Dock Ward pier on the morning of Ches 21." — `campaign/quests/faction-events/bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:75`
> "The Sea Maidens Faire's carnival fleet and parades arrive in Deepwater Harbor on Ches 21 for Fleetswake, while the *Scarlet Marpenoth* has been moored there all year." — `campaign/setting/history/08-the-players-arrive.md:43`
> "Jarlaxle Baenre had been in Waterdeep since Marpenoth of 1491. His Sea Maidens Faire sailed into the harbor on Ches 21, at the start of the last tenday of Ches, when the Fleetswake festival filled the harbor with color and noise and the city looked the other way at almost anything." — `campaign/structure/arc-h-sea-maidens-faire.md:9`

(The Alexandrian PDF has the Faire's parades start "Ches 10th, announcing its arrival" (PDF p.2, printed p.69; transcription). See D5.)

### A4. Faith
Not stated in any file read. The Lolth rule (`campaign/setting/history/03-bregan-daerthes-long-road.md:34`) binds any faith the drafter gives her. The Milil check names her and gives no devotion:
> "- **Bards checked:** No Notable Figures page for Mattrim \"Threestrings\" Mereg, Variel Duskwhisper, Davil Starsong, Margo Verida or Agorn Fuoco names Milil (Grep for \"Milil\" over `campaign/` returns only the staff table, the Deities pages and the research notes), so the page names no worshiper beyond Lysa's history."
> — `campaign/setting/deities/milil.md:116`

### A5. Signature belongings, instrument and weapon
**Campaign, the page, Morale**
> "**Morale.** In a fight, Margo uses Beguiling Song and Tasha's Hideous Laughter for control before engaging directly with her rapier. She is not suicidal and is not Jarlaxle's shield; she fights for reasons she has chosen, not on assignment. A DC 13 Persuasion check built on specific flattery about her music opens a social window before any fight becomes unavoidable. She will not betray Jarlaxle under any circumstances."
> — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:23`

**Published adventure, her instrument (J29 treasure, page 141)**
> "Margo's lyre is worth 30 gp. An unlocked chest at the foot of the bed holds four sets of costume clothing and a jewelry box containing six gold bracelets (worth 25 gp each), two diamond rings (worth 250 gp each), and a pearl necklace (worth 500 gp)."
> — `sources/adventure-wdh.json:25486` (entry "Treasure", `"page": 141` at `:25484`)

**Voice profile, the sample line**
> "  - *Under pressure:* \"Put that down, darling. I've ended better fights than this with a lute.\""
> — `.claude/skills/character-voices/voices/bregan-daerthe.md:200`

**Weapon and instrument: no other source.** The adventure names only a lyre (`sources/adventure-wdh.json:25486`). The page names a rapier (L23) and the voice profile a lute (`bregan-daerthe.md:200`). The Grep over `campaign/` for "rapier|lute|lyre|lyrist" returned other NPCs (Yalah, Orond, Threestrings, Davil) in its first 20 matches, and no other Margo line in that set. The drafter has a choice between the lyre (adventure) and the lute and rapier (campaign page and voice); the campaign's choices do not conflict with a source.

### A6. Relationships (named figures)
**Khafeyta Murzan (companion; the cabin pair)**
> "**Relationships.** Margo is Jarlaxle's companion aboard the Eyecatcher — not his employee, his friend — paired with Khafeyta Murzan in J29, a BD-associated operative whose affiliation derives from freely chosen loyalty rather than organizational membership, and a combatant significantly more capable than a performer's cabin assignment implies."
> — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:25`

Khafeyta's own page is the mirror:
> "**Relationships.** Khafeyta is Jarlaxle's companion aboard the Eyecatcher, paired with Margo Verida in J29, a swashbuckler whose presence alongside Margo means J29 is significantly harder to pass through uncontested than its designation implies."
> — `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:25`

Published adventure (romance, D2): "Jarlaxle has taken a romantic interest in both women, who are also in love with each other." — `sources/adventure-wdh.json:25459`

**Jarlaxle (the principal)**
> "Margo wants to keep making music worth making, maintain her friendship with Jarlaxle on the terms they have established, and be honest about what she is — a bard and a skilled combatant who chooses her associates freely and has chosen well."
> — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:15`
> "- **Word choice:** Artful and literate, with musical metaphors. She calls Jarlaxle by his real name in private, as an equal." — `.claude/skills/character-voices/voices/bregan-daerthe.md:191`
> "**Signature phrases:** \"Say that again, and mean it.\" / \"Music first; business after.\" / \"He's a friend, not a master.\"" — `.claude/skills/character-voices/voices/bregan-daerthe.md:195`

**Zardoz Zord (the public face; the captain's report)**
> "To those who deal with her directly, she is one of the few people Jarlaxle treats as a peer rather than an asset, and she notices when the treatment shifts." — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:21`
> The published adventure's captured-crew list: "\"Zord has a cabin aboard the {@i Eyecatcher} and spends a lot of time there with Margo Verida and Khafeyta Murzan, two of the Faire's star performers.\"" — `sources/adventure-wdh.json:23033`

**Trollskull, Milil**: no Margo line beyond the patron table row (A1) and the Milil note (A4).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "- *Amnian human bard, chaotic good, she/her*. Stat block: **Performer Maestro**." — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:5`
- Campaign, the org page: "- **Margo Verida** — Amnian human bard, chaotic good. Jarlaxle's companion aboard the *Eyecatcher*, not his employee. See the **Margo Verida** page in Notable Figures." — `campaign/setting/organizations/07-bregan-daerthe.md:108`
- Published adventure: "Margo and Khafeyta are polite but terse. Both are neutral good. If attacked, they grab their weapons and other belongings and flee through a secret door (see below)." — `sources/adventure-wdh.json:25460`
- Conflict, D3.

**Species**
- "Amnian human" — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:5`; `campaign/setting/organizations/07-bregan-daerthe.md:108`; `sources/adventure-wdh.json:25455` ("a female Amnian human"); `sources/9. Lair – Sea Maidens Faire.pdf` PDF p.9 (transcription).

**Pronouns**
- "she/her" — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:5`
- "Margo Verida, a female Amnian human" — `sources/adventure-wdh.json:25455`; "Jarlaxle has taken a romantic interest in both women" — `sources/adventure-wdh.json:25459`.
- Pronoun table, group C (research note): `docs/plans/npc-pronouns-table-group-c.md:19` (the page's prose supports she/her).

**Ethnicity**: "Amnian" is the human nation of origin named in the page and the adventure. Ruling 5 asks for a Faerûn ethnicity; the drafter writes "Amnian" as the ethnicity, not a city. `docs/plans/faerun-ethnicities-research.md:353` lists her as a gap.

**Stat block**
- Campaign, the page: "- *Amnian human bard, chaotic good, she/her*. Stat block: **Performer Maestro**." — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:5`
- Campaign, the session record: "- **Stat blocks:** the 2024 Monster Manual has no Bard. Use Performer (CR 1/2), Performer Maestro (CR 6) or Performer Legend (CR 10)." — `session 51 handoff.md:105`
- Campaign, the session record (the Notable Figures row): "| `campaign/setting/notable-figures/` | Summary boxes converted to `[!gamemaster]`; **pronouns on all 123 pages**; real ethnicities for 123 human NPCs; Avi he/him; Amath Sercent a Mulan human; Yorn a half-orc; Caladorn a Tethyrian human ghost; Fenerus a Bandit Captain (Neutral); Grinda Chaotic Neutral; Kalain, Mattrim, Variel, Agorn and Margo on Performer stat blocks; Korgstrod's fake Stone cut; Malkolm Brizzenbright spelled as Dragon Heist spells it. |" — `session 51 handoff.md:24`
- Published adventure: "Margo Verida, a female Amnian human {@creature bard|VGM} (see {@adventure appendix B|WDH|12})" — `sources/adventure-wdh.json:25455`
- Alexandrian stat reference: "Margo Verida – female Amnian human bard (DH p. 195)" — `sources/9. Lair – Sea Maidens Faire.pdf` PDF p.9 (transcription).
- Conflict, D4: the campaign (Performer Maestro) outranks the Alexandrian and adventure (bard).
- No numeric stat block (AC, HP, attacks) for Margo in any file read. The session record gives "CR 6" for Performer Maestro as a block class, not for Margo.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md` (no Background, no Personality, no Connections yet).

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Amnian human bard, chaotic good, she/her*. Stat block: **Performer Maestro**." | Day-one, but "chaotic good" conflicts with the adventure's "neutral good" (D3) | section B |
| 2 | L6 | "**Affiliation:** Bregan D'aerthe (Jarlaxle's companion, not his employee)" | Day-one, but "Bregan D'aerthe" as affiliation needs the E2 decision (non-drow operatives are not members) | `campaign/setting/organizations/07-bregan-daerthe.md:41`; `sources/adventure-wdh.json:1298` |
| 3 | L7 | "**Featured in:** **Sea Maidens Faire**" | Quest-name list. Accurate; no quest file names Margo | `campaign/guides/trollskull-manor/06-tavern-time.md:48` (the patron table, not a quest) |
| 4 | L11 | "Margo should inspire admiration with the quality of the music — it is genuinely excellent, not traveling-performer adequate — and careful attention when the party understands that the woman playing for the captain's table can also end a fight, and will if pressed." | Mostly day-one. "when the party understands that" is a quest-time trigger (the reveal of her fight skill). Restate without the trigger, or route | `campaign/structure/arc-h-sea-maidens-faire.md:158` ("Margo responds to flattery about her music (DC 13 Persuasion)") |
| 5 | L13 | "Margo most often feels creative absorption during a performance, relaxed warmth in Jarlaxle's company, quick professional assessment of new people's motives, genuine pleasure in a room that does not know what it is looking at, and a clean loyalty to Jarlaxle that has nothing servile about it." | Day-one | section G |
| 6 | L15 | "Margo wants to keep making music worth making, maintain her friendship with Jarlaxle on the terms they have established, and be honest about what she is — a bard and a skilled combatant who chooses her associates freely and has chosen well." | Day-one. "friendship" is the campaign's word; it conflicts with the adventure's romance (D2) | D2 |
| 7 | L21 | "To the world, Margo Verida is a performer traveling with Zardoz Zord's carnival — excellent, clearly at home on a ship, someone you assume is in Jarlaxle's company for professional reasons. To those who deal with her directly, she is one of the few people Jarlaxle treats as a peer rather than an asset, and she notices when the treatment shifts. Deep down, she flattery-tested Jarlaxle once, early in the acquaintance, to confirm his compliments were genuine rather than operational; they were, which is why she is still here." | "a performer traveling with Zardoz Zord's carnival" and "clearly at home on a ship" are day-one only if the Faire is travelling before Ches 21; see D1. The remaining sentences are day-one |
| 8 | L23 | "In a fight, Margo uses Beguiling Song and Tasha's Hideous Laughter for control before engaging directly with her rapier. She is not suicidal and is not Jarlaxle's shield; she fights for reasons she has chosen, not on assignment. A DC 13 Persuasion check built on specific flattery about her music opens a social window before any fight becomes unavoidable. She will not betray Jarlaxle under any circumstances." | Encounter register, not a quest event. "A DC 13 Persuasion check built on specific flattery" matches the J29 mechanic in `campaign/structure/arc-h-sea-maidens-faire.md:158`. The spell names are a 2014 spell list (drafter check; not a quest fact) |
| 9 | L29 | "A bard performing aboard Zardoz Zord's carnival ships — the music is genuinely excellent, and the woman playing it is a good deal more capable in a fight than her cabin assignment implies." | Day-one, but "aboard ... ships" is D1. **32 words** (brief limit 21). Draft a shorter Overview | section A3 |
| 10 | L25 | "Margo is Jarlaxle's companion aboard the Eyecatcher — not his employee, his friend — paired with Khafeyta Murzan in J29, a BD-associated operative whose affiliation derives from freely chosen loyalty rather than organizational membership, and a combatant significantly more capable than a performer's cabin assignment implies." | **Mixed.** "companion ... not his employee" is day-one (org page `:108`). "aboard the Eyecatcher" and "paired ... in J29" place her on a ship that is not in harbor until Ches 21 (D1). J29 is a Sea Maidens Faire ship room (`arc-h-sea-maidens-faire.md:158`). "a BD-associated operative whose affiliation derives from freely chosen loyalty rather than organizational membership" is the page's own gloss; no source gives it (E2) |

Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Margo Verida", lines 186-200):
- Line 189, "- **Sound:** A rich, warm, musical alto. She's clearly a trained singer even when she's just talking." — day-one. "trained singer" has no other source; the adventure says "lyrist" (`sources/adventure-wdh.json:25459`).
- Line 190, "- **Sentence shape:** Easy, graceful sentences with warmth and a hint of teasing. Her questions probe motives." — day-one.
- Line 191, "- **Word choice:** Artful and literate, with musical metaphors. She calls Jarlaxle by his real name in private, as an equal." — day-one in the voice sense, but "his real name" touches the Jarlaxle Unmasked rule. `campaign/setting/villains/jarlaxle.md:31` reads: "Until a member is marked, no Bregan D'aerthe speaker says \"Jarlaxle\" to that member." Margo is not a marked member (E2), so the rule does not bind her by its text. The drafter should check the Jarlaxle Unmasked wording before writing the name.
- Line 192, "- **Swearing:** *Casual · Pearls · Phrase.* Occasional and elegant, for emphasis (\"That's a fucking gorgeous instrument.\"). A musician's gem: \"That man sings like a cat being tuned.\"" — day-one. Adult table: the swearing stays.
- Line 193, "- **Personality in speech:** Creative absorption and relaxed warmth. She tests people's flattery and sees through the false kind instantly. Her loyalty to Jarlaxle is clean and unservile." — day-one.
- Line 194, "- **Quirks:** She hums while thinking. She compliments honestly and expects honesty back." — day-one.
- Line 195, "- **Signature phrases:** \"Say that again, and mean it.\" / \"Music first; business after.\" / \"He's a friend, not a master.\"" — day-one. "He's a friend, not a master" supports the friendship reading and conflicts with the adventure's romance (D2).
- Line 196, "- **Never:** She never plays badly, never grovels, and never pretends to be less dangerous than she is when pushed." — day-one.
- Line 198, sample *Greeting*: "You look like people with a story. Sit, I'll play something, and you can decide whether to tell it." — day-one.
- Line 199, sample *Business*: "I'll pass it to him. But I'll tell him what I think of you too, so be honest." — day-one. ("pass it to him" implies a messenger role; it is not a quest event.)
- Line 200, sample *Under pressure*: "Put that down, darling. I've ended better fights than this with a lute." — encounter register. "lute" differs from the adventure's lyre (`sources/adventure-wdh.json:25486`); see A5.

---

## D. Conflicts (both sides quoted, higher rank named)

**D1. Where she is on Ches 1 (the fleet's arrival)**
- Campaign, the page: "**Relationships.** Margo is Jarlaxle's companion aboard the Eyecatcher" — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:25`
- Campaign, the page, Overview: "A bard performing aboard Zardoz Zord's carnival ships" — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:29`
- Campaign, the org page Overview: "The fleet is due in Deepwater Harbor on Ches 21, the opening day of Fleetswake, and is booked to sail at dawn on Tarsakh 20." — `campaign/setting/organizations/07-bregan-daerthe.md:118`
- Campaign, the history page: "The Sea Maidens Faire's carnival fleet and parades arrive in Deepwater Harbor on Ches 21 for Fleetswake, while the *Scarlet Marpenoth* has been moored there all year." — `campaign/setting/history/08-the-players-arrive.md:43`
- Campaign, the Sea Maidens structure doc: "His Sea Maidens Faire sailed into the harbor on Ches 21, at the start of the last tenday of Ches" — `campaign/structure/arc-h-sea-maidens-faire.md:9`
- Campaign, the Villains page: "The fleet reaches Deepwater Harbor on Ches 21, the opening day of Fleetswake, and leaves at dawn on Tarsakh 20" — `campaign/setting/villains/jarlaxle.md:52`
- Alexandrian PDF: "Ches 10th, announcing its arrival" (PDF p.2, printed p.69; transcription; see D5).
- Higher rank: campaign (five files agree on Ches 21). The page's present tense ("is Jarlaxle's companion aboard the Eyecatcher") is a day-one conflict. The drafter must choose a day-one location for her, or write her with the Faire in its pre-arrival state. No source gives where the Faire is between its Lantan visit and Ches 21 (see Not found).

**D2. Romance or friendship**
- Published adventure: "Margo and Khafeyta both joined the Sea Maidens Faire within the past year-Margo as a lyrist, Khafeyta as an acrobat. Jarlaxle has taken a romantic interest in both women, who are also in love with each other." — `sources/adventure-wdh.json:25459`
- Alexandrian PDF (transcription): "Other than becoming one of Jarlaxle's \"romantic\" conquests, the PCs are unlikely to get onboard any of the ships under any sort of legitimate pretenses in order to conduct surveillance." — `sources/9. Lair – Sea Maidens Faire.pdf` PDF p.3 (printed p.70)
- Campaign, the page: "maintain her friendship with Jarlaxle on the terms they have established" — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:15`; "Margo is Jarlaxle's companion aboard the Eyecatcher — not his employee, his friend" — `10-margo-verida.md:25`
- Campaign, the voice profile: "\"He's a friend, not a master.\"" — `.claude/skills/character-voices/voices/bregan-daerthe.md:195`
- Campaign, the Jarlaxle page: "The companions who travel aboard the *Eyecatcher*. They are not his employees." — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:55` (no romance either way)
- Higher rank: campaign. The campaign files say "friend" and "companion" and never say romance. The romance is in the published adventure and the Alexandrian doc. The sources do not settle it; the drafter must not write a romance as day-one fact without a campaign decision.

**D3. Alignment**
- Campaign, the page: "- *Amnian human bard, chaotic good, she/her*." — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:5`
- Campaign, the org page: "- **Margo Verida** — Amnian human bard, chaotic good." — `campaign/setting/organizations/07-bregan-daerthe.md:108`
- Published adventure: "Margo and Khafeyta are polite but terse. Both are neutral good." — `sources/adventure-wdh.json:25460`
- Higher rank: campaign (chaotic good, two campaign files). The campaign has changed the adventure's alignment. The drafter should note the change in Draft Notes.

**D4. Stat block**
- Campaign, the page: "Stat block: **Performer Maestro**." — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:5`
- Campaign, the session record: "- **Stat blocks:** the 2024 Monster Manual has no Bard. Use Performer (CR 1/2), Performer Maestro (CR 6) or Performer Legend (CR 10)." — `session 51 handoff.md:105`
- Alexandrian stat reference (transcription): "Margo Verida – female Amnian human bard (DH p. 195)" — `sources/9. Lair – Sea Maidens Faire.pdf` PDF p.9 (printed p.76)
- Published adventure: "Margo Verida, a female Amnian human {@creature bard|VGM} (see {@adventure appendix B|WDH|12})" — `sources/adventure-wdh.json:25455`
- Higher rank: campaign (the session record moved the company's Performers to 2024 Performer blocks; the Alexandrian and the adventure use the 2014 bard).

**D5. Faire arrival date**
- Campaign: "Ches 21" (A3).
- Alexandrian PDF (transcription): "Ches 10th, announcing its arrival" — `sources/9. Lair – Sea Maidens Faire.pdf` PDF p.2 (printed p.69, EVENT SCHEDULE). The schedule line reads, in full: "CARNIVAL PARADES: The Sea Maidens Faire carnival goes on five different parades during its stay in Waterdeep." The Ches 10 entry is a parade date, which may not be the fleet's arrival.
- Higher rank: campaign (the fleet arrives Ches 21). The Fel'rekt notes (D9) reach the same conclusion.

**D6. Crew knowledge (recorded, not a conflict)**
- Published adventure: "Zord has a cabin aboard the {@i Eyecatcher} and spends a lot of time there with Margo Verida and Khafeyta Murzan, two of the Faire's star performers." — `sources/adventure-wdh.json:23033`
- Campaign: "not his employee" (L6, L25). Consistent.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/setting/organizations/07-bregan-daerthe.md:108`: "- **Margo Verida** — Amnian human bard, chaotic good. Jarlaxle's companion aboard the *Eyecatcher*, not his employee." (present tense on Ches 1; D1)
- `campaign/setting/organizations/07-bregan-daerthe.md:118`: "The fleet is due in Deepwater Harbor on Ches 21, the opening day of Fleetswake, and is booked to sail at dawn on Tarsakh 20." (the Overview names the arrival date; the page's present tense conflicts)
- `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:55`: "The companions who travel aboard the *Eyecatcher*. They are not his employees." (present tense; D1)
- `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:25`: "**Relationships.** Khafeyta is Jarlaxle's companion aboard the Eyecatcher, paired with Margo Verida in J29, ..." (same present tense as Margo; D1). Khafeyta's page line is quoted in full in A6.

**E2. Membership label**
- Campaign, the org page: "- **Margo Verida** — Amnian human bard, chaotic good. Jarlaxle's companion aboard the *Eyecatcher*, not his employee. See the **Margo Verida** page in Notable Figures." (`campaign/setting/organizations/07-bregan-daerthe.md:108`). The org page lists her under Key Members of Bregan D'aerthe.
- Campaign, the org page membership rule: "In this campaign Jarlaxle collects capable people whatever their species. The non-drow operatives he employs are never counted as members." (`campaign/setting/organizations/07-bregan-daerthe.md:41`)
- Published adventure, the membership rule: "A character must be a drow, preferably a male, to join this faction." (`sources/adventure-wdh.json:1296`); "Jarlaxle employs non-drow operatives as well, none of whom know they're working for him; such individuals aren't considered members of the faction." (`sources/adventure-wdh.json:1298`)
- Margo knows Jarlaxle and is not an unwitting operative, but she is human and not an employee. The page's affiliation line reads "Bregan D'aerthe (Jarlaxle's companion, not his employee)" (L6). The drafter decides the label. The sources give no term for "companion who is not a member".

**E3. Routed quest references (quest time, not day-one)**
- `campaign/structure/arc-h-sea-maidens-faire.md:158`: "**J29 (Guest Cabin).** Margo Verida (bard) + Khafeyta Murzan (swashbuckler). Jarlaxle's companions — skilled combatants and genuine friends. They can be charmed, deceived, or negotiated with: Margo responds to flattery about her music (DC 13 Persuasion), Khafeyta responds to a good fight story (DC 14 Persuasion). Neither will betray Jarlaxle, but both can be distracted." (the Sea Maidens heist; route the mechanic)
- `campaign/structure/arc-h-sea-maidens-faire.md:182`: "**Parade Roster.** Significantly reduced. J1: 1 sailor. J3–J9: empty. J10: nimblewright only. J17: spiders (always present). J18: nimblewrights per tier. J29: empty (Margo and Khafeyta march in the parade). J30: nimblewright valet only. J31: mannequins (always present). Submarine: skeleton crew — U7b (1 gnome + 1 mate), all staterooms empty."
- `campaign/structure/arc-h-sea-maidens-faire.md:337`: "- **Notable Figures** — Full NPC profiles for Jarlaxle, Soluun, Fel'rekt, Krebbyg, Zelifarn, Margo Verida, Khafeyta Murzan, Fenerus Stormcastle, Malkolm Brizzenbright."
- `campaign/guides/trollskull-manor/06-tavern-time.md:48`: "| **Sea Maidens Faire** | Margo Verida |" (the patron after the Sea Maidens Faire quest; routed to the Trollskull guide).
- Alexandrian PDF, the Zord business (PDF p.2, printed p.69): "During these times, the following characters should be stricken from the Eyecatcher's adversary roster:" followed by the list "Jarlaxle", "Margo Verida & Khafeyta", "Any lieutenants who would otherwise be present on the ship" (transcription). Route: Sea Maidens Faire.
- Alexandrian PDF, the Eyecatcher roster, during the day: "Margo Verida + Khafeyta + Jarlaxle (25%)" (PDF p.8, printed p.74; transcription). The parade roster (PDF p.9? printed p.75) lists no Margo. Route: Sea Maidens Faire.
- Published adventure, the captured crew (quest time): "Zardoz Zord is a drow named Jarlaxle in disguise." (`sources/adventure-wdh.json:25465`) and "A year ago, the Sea Maidens Faire visited the island nation of Lantan, where Jarlaxle obtained a Lantanese submarine and several clockwork servants." (`sources/adventure-wdh.json:25468`). The list opens at `:25461`: "If separated from Jarlaxle and compelled to divulge information about their host, Margo and Khafeyta reveal some or all of the following facts:"
- Published adventure, the escape (quest time): "If attacked, they grab their weapons and other belongings and flee through a secret door (see below)." — `sources/adventure-wdh.json:25460`; "Secret Door" entry at `:25473`-`:25477`.
- Published adventure, the cabin treasure (quest time): `sources/adventure-wdh.json:25486`.

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth year, birth name, home city, family, age.** None in any file read. Searched: `campaign/` (Grep "Margo", "Verida"), `sources/adventure-wdh.json` (Grep "Margo", "Verida", "Khafeyta"), `sources/*.md` (Grep), `sources/research/` (Grep), `docs/` (Grep). "Amnian" is the only origin word (`10-margo-verida.md:5`). Constraint: "Amnian" and "human" must stay; the drafter may name a region of Amn without naming a city (ruling 5). Do not name a new Notable Figure (brief ruling 17).

**F2. Former life and training.** None. The sources say only "a bard" (page L5), "a lyrist" (`sources/adventure-wdh.json:25459`), "a combatant" (L25), "skilled combatants" (`arc-h-sea-maidens-faire.md:158`). The voice profile gives "She's clearly a trained singer even when she's just talking." (`bregan-daerthe.md:189`). The drafter may give a training history as `[design]`, consistent with "a trained singer" and "a lyrist".

**F3. How and when she joined the Faire.** Only "within the past year" (`sources/adventure-wdh.json:25459`). Constraint: a Lantan trip "A year ago" (`:25468`) precedes the Faire's current run, so she joined after or with that trip. No date is given.

**F4. Her cover to the public.** Page L21: "To the world, Margo Verida is a performer traveling with Zardoz Zord's carnival — excellent, clearly at home on a ship, someone you assume is in Jarlaxle's company for professional reasons." The sources give no other public cover. Constraint: the Faire is a legitimate business. "The fleet has three ships, and their names, the *Eyecatcher*, the *Heartbreaker* and the *Hellraiser*, all describe Jarlaxle (*Waterdeep: Dragon Heist*, 5e)." (`campaign/setting/organizations/07-bregan-daerthe.md:61`) and "Bregan D'aerthe is using one of Jarlaxle's legitimate business enterprises-the Sea Maidens Faire-as a front in Waterdeep." (`sources/adventure-wdh.json:1299`).

**F5. Relationship with Khafeyta.** The campaign: "paired with Khafeyta Murzan in J29" (`10-margo-verida.md:25`). The adventure: "Margo and Khafeyta both joined the Sea Maidens Faire within the past year" (`sources/adventure-wdh.json:25459`); the romance clause is D2. The drafter must not state a romance without a campaign decision. A companion bond without romance is consistent with every campaign file.

**F6. Relationship with Jarlaxle before the Faire.** None. The sources give "flattery-tested Jarlaxle once, early in the acquaintance" (page L21) and the campaign's "friend" (L25). No origin of the acquaintance is sourced.

**F7. Losses, grudges, people she cares about (beyond Khafeyta and Jarlaxle).** None in any file read.

**F8. Personal goals beyond the company.** The page gives "Margo wants to keep making music worth making, maintain her friendship with Jarlaxle on the terms they have established, and be honest about what she is" (L15). The Background explains where these come from. A goal about a place, a craft or a person she wants to keep is allowed as `[design]`, with no quest event and no secret.

**F9. Physical appearance.** None as a day-one fact. The published adventure's J29 entry gives no description of her: "The bed holds three giggling figures:" (`sources/adventure-wdh.json:25450`).

**F10. Her faith.** None (A4).

**F11. Where she is on Ches 1.** No file read places the Faire, or Margo, between Marpenoth 1491 DR and Ches 21, 1492 DR (see D1). The Sea Maidens location overview was not read for travel dates (Not found).

---

## G. Source facts that hint at the figure's inner life (do not contradict)

- Page: "Margo most often feels creative absorption during a performance, relaxed warmth in Jarlaxle's company, quick professional assessment of new people's motives, genuine pleasure in a room that does not know what it is looking at, and a clean loyalty to Jarlaxle that has nothing servile about it." (`campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:13`)
- Page: "Margo wants to keep making music worth making, maintain her friendship with Jarlaxle on the terms they have established, and be honest about what she is — a bard and a skilled combatant who chooses her associates freely and has chosen well." (`10-margo-verida.md:15`)
- Page, day-one: "Deep down, she flattery-tested Jarlaxle once, early in the acquaintance, to confirm his compliments were genuine rather than operational; they were, which is why she is still here." (`10-margo-verida.md:21`)
- Page, Morale: "She is not suicidal and is not Jarlaxle's shield; she fights for reasons she has chosen, not on assignment." (`10-margo-verida.md:23`)
- Page, Morale: "She will not betray Jarlaxle under any circumstances." (`10-margo-verida.md:23`)
- Voice, day-one: "She tests people's flattery and sees through the false kind instantly. Her loyalty to Jarlaxle is clean and unservile." (`.claude/skills/character-voices/voices/bregan-daerthe.md:193`)
- Voice, day-one: "She compliments honestly and expects honesty back." (`bregan-daerthe.md:194`)
- Voice, day-one: "She never plays badly, never grovels, and never pretends to be less dangerous than she is when pushed." (`bregan-daerthe.md:196`)
- Voice, day-one: "\"He's a friend, not a master.\"" (`bregan-daerthe.md:195`) (the friendship reading; see D2)
- Adventure, day-one: "Margo and Khafeyta are polite but terse. Both are neutral good." (`sources/adventure-wdh.json:25460`)
- Adventure, day-one: "Margo's lyre is worth 30 gp." (`sources/adventure-wdh.json:25486`) (the instrument she is known to own; a treasure line, not a quest event).

---

## Not found

- Birth year, birth name, home city, family, age, how and when she joined the Faire beyond "within the past year", former life, training, faith, losses, grudges, fixed appearance, the Faire's location between Marpenoth 1491 and Ches 21, 1492. Searched: `campaign/` (Grep "Margo", "Verida", and "rapier|lute|lyre|lyrist"), `sources/adventure-wdh.json` (Grep "Margo", "Verida", "Khafeyta"), `sources/*.md` (Grep), `sources/research/` (Grep), `docs/` (Grep).
- Wiki: NOT FOUND (the wiki extract for Margo contains only that line). The pass 4 and pass 5 bundles contain only campaign-hit copies of the page (the pass 4 `campaign-hits.txt` lines 1402-1406) and no wiki line.
- Alexandrian PDFs read: `sources/9. Lair – Sea Maidens Faire.pdf` (PDF pp.1-9, the whole file) and `sources/27. Addendum A Night in Trollskull Manor.pdf` (PDF pp.1-12). Margo appears only in the Sea Maidens PDF (transcriptions cited above). Not read: `sources/3. Player Character Factions.pdf`, `sources/26. Addendum Other Collaborators.pdf`, `sources/1. The Villains.pdf` (only p.5 read in another note), `sources/8. The Eyes of the Stone.pdf`, `sources/17. Outpost and Lair Revelation Lists.pdf` (only p.2 read in another note). These were not checked for Margo or Khafeyta.
- `sources/SOURCE_GUIDE.md:717` maps the Jarlaxle and Bregan D'aerthe sources to `1. The Villains.pdf` and `9. Lair Sea Maidens Faire.pdf`, and to `3. Player Character Factions.pdf` and `26. Addendum.pdf`. The Sea Maidens PDF was read; the others were not.
- The Sea Maidens Faire location overview (`campaign/locations/sea-maidens-faire/area-overview.md`) was not read for Margo's room or the Faire's travel dates.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:698` lists `Zardoz Zord (and extra side quest hook).docx`, and `:690` lists `Jarlaxle Baenre NPC Guide.docx`. Neither was checked for Margo or Khafeyta; a Sea Maidens or Zord guide may name her.
- PDFs read as images: transcriptions only. `pdftotext -layout` check needed before any quote goes into prose.
