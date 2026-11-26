# Pass 6 research notes: Khafeyta Murzan

Page: `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Khafeyta is a companion of Jarlaxle aboard the *Eyecatcher* and is in the city on day one. The J29 room and the Sea Maidens Faire mechanics are quest time and are routed to **Sea Maidens Faire**. Cassalanter secrecy and the Lolth rule apply. Brief ruling 2 makes her a major NPC (a named companion of the company's leader), so the full Personality and Connections apply.
Organization page: `campaign/setting/organizations/07-bregan-daerthe.md`
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md` ("### Khafeyta Murzan", lines 204-218)
Wiki: NOT FOUND. `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/11-khafeyta-murzan.txt` contains only the line `NOT FOUND`. A search of `sources/research/**/wiki.txt` for "Khafeyta", "Murzan", "Vessa" and "Lymeria" found no match.

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string with JSON escapes shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field of the entry is given where the entry carries one.
- Alexandrian PDF: no shell, so `pdftotext` could not run. `sources/9. Lair – Sea Maidens Faire.pdf` was read as a rendered page image. The quote is a transcription and needs a `pdftotext -layout` check before any use in prose. The correct page is PDF p.9 (printed p.76). An earlier note (`docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/03-vevette-blackwater.md:205`) gives PDF p.8; PDF p.8 (printed p.75) does not contain Khafeyta.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDF and appendices, then the wiki (none).
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The adventure gives her a romance that no campaign file carries.** The published adventure says Jarlaxle "has taken a romantic interest in both women, who are also in love with each other" (`sources/adventure-wdh.json:25459`). A search of `campaign/setting/notable-figures/bregan-daerthe/`, `campaign/structure/arc-h-sea-maidens-faire.md` and `campaign/quests/faction-events/bregan-daerthe/` for "romantic", "in love", "romance", "lovers" and "affair" found no Khafeyta or Margo line. The drafter must decide whether to carry it (see D5 and F4).
2. **"Mulhorandi" is the adventure's word for her, and the campaign's word for other Mulhorand humans is "Mulan".** The adventure says "Khafeyta Murzan, a female Mulhorandi human" (`sources/adventure-wdh.json:25456`) and gives Amath and Kaevja "Mulan" (`:9748`, `:29994`). The brief says she "stays 'Mulhorandi'" (`docs/plans/setting-compendium-pass6-brief.md:73`). Quotes in D6.
3. **Her species and stat are sourced consistently** (Mulhorandi human, swashbuckler, she/her, neutral good). Section B.
4. **Her Background has almost no sourced history.** The published adventure gives one day-one history line: she joined the Faire "within the past year" as an acrobat. Everything else is `[design]` material (section F).
5. **Her affiliation line says "Bregan D'aerthe", and the Margo page uses the same words, but the Margo page's Relationships line can be read as calling Khafeyta a "BD-associated operative".** See D2.

---

## A. Background facts by theme

### A1. Origin, birth, home, family
No source gives any of these. The only day-one history line is the adventure's:

> "Margo and Khafeyta both joined the Sea Maidens Faire within the past year-Margo as a lyrist, Khafeyta as an acrobat. Jarlaxle has taken a romantic interest in both women, who are also in love with each other."
> — `sources/adventure-wdh.json:25459` (entry "J29. Guest Cabin", page 140; the entry starts at `:25445`)

### A2. How she joined and rose
Joined the Faire "within the past year" as an acrobat (`sources/adventure-wdh.json:25459`, above). Her rank in the company is not stated in any source. The organization page lists her only as a Key Member:

> "- **Khafeyta Murzan** — Mulhorandi human swashbuckler, neutral good. Jarlaxle's companion aboard the *Eyecatcher*, paired with Margo Verida. See the **Khafeyta Murzan** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:109` (Key Members)

The Villains page's Background calls her and Margo "companions", not members:

> "- **Margo Verida** and **Khafeyta Murzan:** The companions who travel aboard the *Eyecatcher*. They are not his employees."
> — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:55`

Her own page's Summary:

> "- **Affiliation:** Bregan D'aerthe (Jarlaxle's companion, not his employee)"
> — `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:6`

The Margo page carries the same phrase for Margo:

> "- **Affiliation:** Bregan D'aerthe (Jarlaxle's companion, not his employee)"
> — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:6`

### A3. Former life
No source gives one. The Alexandrian stat reference lists her only by name and stat block (A7).

### A4. Faith
Not stated in any source. The Lolth rule binds the company and any page about it:

> "- The Company Rejects Lolth:" — see the full bullet at `campaign/setting/organizations/07-bregan-daerthe.md:46`, which is the day-one rule the Background must not contradict.

### A5. Signature belongings and skills
The voice profile gives her signature lines and her fighting habit. The adventure gives her temperament toward a stranger:

> "Margo and Khafeyta are polite but terse. Both are neutral good. If attacked, they grab their weapons and other belongings and flee through a secret door (see below)."
> — `sources/adventure-wdh.json:25460` (J29; page 140)

Her weapons, equipment and fighting style are not stated in any source beyond "swashbuckler" (B). The exits-and-weapons habit is voice, not inventory:

> "Two exits, four blades."
> — `.claude/skills/character-voices/voices/bregan-daerthe.md:213` (Signature phrases)

### A6. Relationships (named figures)

**Margo Verida (companion; the adventure gives a romance, see D5).** The campaign:

> "**Relationships.** Khafeyta is Jarlaxle's companion aboard the Eyecatcher, paired with Margo Verida in J29, a swashbuckler whose presence alongside Margo means J29 is significantly harder to pass through uncontested than its designation implies."
> — `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:25` (the J29 clause is quest time; see C)

The adventure:

> "Margo and Khafeyta both joined the Sea Maidens Faire within the past year-Margo as a lyrist, Khafeyta as an acrobat. Jarlaxle has taken a romantic interest in both women, who are also in love with each other."
> — `sources/adventure-wdh.json:25459`

The Margo page's Relationships line also names Khafeyta:

> "**Relationships.** Margo is Jarlaxle's companion aboard the Eyecatcher — not his employee, his friend — paired with Khafeyta Murzan in J29, a BD-associated operative whose affiliation derives from freely chosen loyalty rather than organizational membership, and a combatant significantly more capable than a performer's cabin assignment implies."
> — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:25` (see D2)

**Jarlaxle (the employer-companion, not an employee).** The campaign states the non-employee status (A2, `01-jarlaxle-baenre.md:55`). The adventure's J29 list:

> "{@creature Jarlaxle Baenre|WDH} (see {@adventure appendix B|WDH|12}), in the guise of Zardoz Zord (absent if he's marshalling the Day of Wonders parade; see \"Special Events\")."
> — `sources/adventure-wdh.json:25454` (J29; page 140)

The Eyecatcher entry:

> "\"Zord has a cabin aboard the {@i Eyecatcher} and spends a lot of time there with Margo Verida and Khafeyta Murzan, two of the Faire's star performers.\""
> — `sources/adventure-wdh.json:23033`

**Featured in.** Her page's Summary:

> "- **Featured in:** **Sea Maidens Faire**"
> — `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:7`

### A7. Rank, post, time in post, stat
- Joined "within the past year" (`sources/adventure-wdh.json:25459`).
- Stat block: "Stat block: **Swashbuckler**." (`campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:5`). Alexandrian stat reference, PDF p.9, transcription: "Khafeyta – female Mulhorandi human swashbuckler (DH p. 216)" (B).

### A8. Habits and temperament
Campaign voice and Persona lines (day-one; quoted in full in B, C and G).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "*Mulhorandi human swashbuckler, neutral good, she/her*. Stat block: **Swashbuckler**." — `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:5`
- Campaign, the org page: "- **Khafeyta Murzan** — Mulhorandi human swashbuckler, neutral good. Jarlaxle's companion aboard the *Eyecatcher*, paired with Margo Verida. See the **Khafeyta Murzan** page in Notable Figures." — `campaign/setting/organizations/07-bregan-daerthe.md:109`
- Adventure: "Both are neutral good." — `sources/adventure-wdh.json:25460`
- Wiki: none (NOT FOUND stub).

**Species**
- Campaign, the page: "*Mulhorandi human swashbuckler, neutral good, she/her*." — `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:5`
- Campaign, the org page: "Mulhorandi human swashbuckler" — `campaign/setting/organizations/07-bregan-daerthe.md:109`
- Adventure: "Khafeyta Murzan, a female Mulhorandi human {@creature swashbuckler|VGM} (see {@adventure appendix B|WDH|12})" — `sources/adventure-wdh.json:25456` (page 140)
- Alexandrian (PDF p.9, printed p.76, transcription): "Khafeyta – female Mulhorandi human swashbuckler (DH p. 216)" — `sources/9. Lair – Sea Maidens Faire.pdf`, PDF p.9. The same page's questioning-crew list gives "Margo / Khafeyta: Dragon Heist, p. 140".

**Pronouns**
- Campaign, the page: "she/her" (`11-khafeyta-murzan.md:5`)
- Adventure: "a female Mulhorandi human" (`sources/adventure-wdh.json:25456`). The adventure's pronoun is "female", and the campaign's "she/her" follows it.
- The pronoun table: "| Khafeyta Murzan | bregan-daerthe/11-khafeyta-murzan.md:5 | she/her |" — `docs/plans/npc-pronouns-table-group-c.md:20`

**Name pronunciation (adventure)**
> "Khafeyta Murzan",
> "kah-FAY-tah mur-ZAWN"
> — `sources/adventure-wdh.json:185`-`:186` (pronunciation key, one entry)

**Stat block**
- Campaign: "Stat block: **Swashbuckler**." — `11-khafeyta-murzan.md:5`
- Adventure: "Khafeyta Murzan, a female Mulhorandi human {@creature swashbuckler|VGM}" — `sources/adventure-wdh.json:25456`
- No numeric stat block (CR, HP, AC) appears in the sources read. The Bestiary is not drafted.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md`. The page has no Background, no Personality and no Connections section yet. Each row gives the status and where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Mulhorandi human swashbuckler, neutral good, she/her*. Stat block: **Swashbuckler**." | Day-one (B). Keep | section B |
| 2 | L6 | "- **Affiliation:** Bregan D'aerthe (Jarlaxle's companion, not his employee)" | Day-one. Keep (see D2) | `campaign/setting/organizations/07-bregan-daerthe.md:109` |
| 3 | L7 | "- **Featured in:** **Sea Maidens Faire**" | Quest-name list (not narrative) | `campaign/structure/arc-h-sea-maidens-faire.md:158`, `:182`, `:337` |
| 4 | L11 | "**Resonance.** Khafeyta should inspire immediate interest in how good she actually is — she carries herself like someone who knows, and the impression is accurate — and comfortable respect for the way she treats a genuine fight story as real currency." | Day-one. Keep (ruling 3) | voice profile `bregan-daerthe.md:211` (the same stance) |
| 5 | L13 | "**Emotions.** Khafeyta most often feels active physical engagement with whatever she is doing, competitive assessment of capable opponents, uncomplicated pleasure in Margo's company and Jarlaxle's, a fighter's professional pride, and a contented certainty about her own situation that reads as ease and is earned." | Day-one. Keep | voice profile `:211` |
| 6 | L15 | "**Motivations.** Khafeyta wants to be excellent at her craft, spend time with people worth spending it with, and find situations complicated enough to be interesting. She chose Jarlaxle's company for reasons similar to Margo's and arrived at the same conclusion through a different door." | Day-one. Keep. The reasons are not sourced (F2) | `sources/adventure-wdh.json:25459` (the "joined" fact only) |
| 7 | L17 | "**Inspirations.** When playing Khafeyta, channel Inigo Montoya (*The Princess Bride*), Brienne of Tarth (*Game of Thrones*), and Porthos (*The Three Musketeers*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Khafeyta Murzan is the other one in J29 — not the performer, the fighter. To those who engage her directly, she is sharp and immediately interested in whether the person across from her has a story worth hearing; a genuine account of a difficult fight opens the social window that flattery opens for Margo, and she checks for the difference between embellishment and truth. Deep down, she and Margo occupy different frequencies — Margo reads a room through its emotional resonance, Khafeyta through its exits and weapons — and between them they have all of it covered." | Day-one register, except "the other one in J29", a room reference to a quest location. Restate as "one of Jarlaxle's two companions" and route J29 (D7) | `sources/adventure-wdh.json:25450`-`:25459` (the bed holds the two companions) |
| 9 | L23 | "**Morale.** In a fight, Khafeyta engages directly. She is the more aggressive of the two companions, the one who steps forward while Margo controls the room behind her. A DC 14 Persuasion check grounded in a credible account of a real fight creates a social opening before violence becomes the only option. She will not betray Jarlaxle." | Mixed. The DC 14 Persuasion sentence is an encounter mechanic, not day-one lore. "She will not betray Jarlaxle." is day-one. Flag for the drafter | `campaign/structure/arc-h-sea-maidens-faire.md:158` (the same DC 14 check, quoted in E2) |
| 10 | L25 | "**Relationships.** Khafeyta is Jarlaxle's companion aboard the Eyecatcher, paired with Margo Verida in J29, a swashbuckler whose presence alongside Margo means J29 is significantly harder to pass through uncontested than its designation implies." | First clause day-one. "J29 is significantly harder to pass through uncontested" is a Sea Maidens Faire room mechanic; route it | `campaign/structure/arc-h-sea-maidens-faire.md:158` |
| 11 | L29 | "A fighter traveling with Zardoz Zord's carnival who carries herself like someone who knows exactly how good she is — her assessment of the current room's exits and weapons is finished before the pleasantries are." | Day-one. 35 words (brief limit 21). Draft a shorter Overview | `sources/adventure-wdh.json:25459`; voice `bregan-daerthe.md:213` |

Voice profile, the lines with a quest-time or encounter clause (`.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Khafeyta Murzan", lines 204-218):
- Line 218, sample *Under pressure*: "Finally. Something interesting." — encounter cue. Flag.
- Line 210, the swearing line, is day-one and stays (adult table).
- Lines 207 to 217 otherwise carry day-one habits and are day-one register.

---

## D. Conflicts

**D1. Mulhorandi against Mulan (species label).** See D6.

**D2. Affiliation label: "Bregan D'aerthe" (her page) against "BD-associated" (the Margo page).**
- Khafeyta's page: "- **Affiliation:** Bregan D'aerthe (Jarlaxle's companion, not his employee)" — `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:6`
- Margo's page: "- **Affiliation:** Bregan D'aerthe (Jarlaxle's companion, not his employee)" — `campaign/setting/notable-figures/bregan-daerthe/10-margo-verida.md:6`
- Margo's page, Relationships: "...paired with Khafeyta Murzan in J29, a BD-associated operative whose affiliation derives from freely chosen loyalty rather than organizational membership..." — `10-margo-verida.md:25`. The phrase "a BD-associated operative" follows "Khafeyta Murzan" and may describe her. The sentence is ambiguous.
- Organization page: both women are listed under Key Members with "Jarlaxle's companion aboard the *Eyecatcher*" (`campaign/setting/organizations/07-bregan-daerthe.md:109` for Khafeyta).
- Not decided in the sources. The org page's Draft Notes say: "Khafeyta Murzan's \"Mulhorandi\" is open ruling 15 and was not touched." (`07-bregan-daerthe.md:184`).

**D3. Whether she would betray Jarlaxle.**
- Campaign, her page: "She will not betray Jarlaxle." — `11-khafeyta-murzan.md:23`
- Campaign, the Sea Maidens structure doc: "Neither will betray Jarlaxle, but both can be distracted." — `campaign/structure/arc-h-sea-maidens-faire.md:158`
- Adventure: "If separated from Jarlaxle and compelled to divulge information about their host, Margo and Khafeyta reveal some or all of the following facts:" — `sources/adventure-wdh.json:25461`. The list follows at `:25465`-`:25468`, and its first item is "Zardoz Zord is a drow named Jarlaxle in disguise." (`:25465`).
- Higher rank: the campaign for her behaviour. The adventure's divulgence is conditional on separation and compulsion. Keep "will not betray" and add the conditional if the drafter uses the adventure's list. The reveal route is set in `campaign/setting/villains/jarlaxle.md:28` ("A Bregan D'aerthe member taken to his private cabin sees the persona drop, and he names himself."), which the adventure's list does not follow. Route both.

**D4. Acrobat against swashbuckler (job against stat block).**
- Adventure: "Khafeyta as an acrobat" (`sources/adventure-wdh.json:25459`)
- Adventure stat: "Khafeyta Murzan, a female Mulhorandi human {@creature swashbuckler|VGM}" (`:25456`)
- Campaign: "*Mulhorandi human swashbuckler, neutral good, she/her*." (`11-khafeyta-murzan.md:5`)
- Not a conflict in substance: the adventure gives her job and her stat block. The campaign has not chosen which word names her job. The drafter should say which.

**D5. Romance (adventure) against the campaign (silent).**
- Adventure: "Jarlaxle has taken a romantic interest in both women, who are also in love with each other." — `sources/adventure-wdh.json:25459`
- Campaign: no line carries it. Her Emotions line says "uncomplicated pleasure in Margo's company and Jarlaxle's" (`11-khafeyta-murzan.md:13`), and her Motivations line says "She chose Jarlaxle's company for reasons similar to Margo's" (`:15`). Those lines are compatible with the adventure and say nothing about romance.
- Higher rank: the adventure is the only source. The campaign has not decided it.

**D6. Mulhorandi against Mulan (the species label, and the wider naming).**
- Campaign, Khafeyta: "*Mulhorandi human swashbuckler, neutral good, she/her*." — `campaign/setting/notable-figures/bregan-daerthe/11-khafeyta-murzan.md:5`
- Campaign, Amath Sercent: "*Mulan human priest of Bane, lawful evil, she/her*. Stat block: **Priest**." — `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:7`
- Campaign, Kaevja Cynavern: "*Mulan human mage, lawful neutral, she/her*. Stat block: **Mage**." — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:7`
- Campaign, Chirada: "*Mulan human operative, neutral, she/her*. Stat block: **Spy**." — `campaign/setting/notable-figures/gralhunds/05-chirada.md:5`
- Campaign, Uza Solizeph: "Uza Solizeph (Lawful Good, Mulan Human, she/her) :: a bookseller of about seventy who describes a monster in her shop the way she would describe a damaged first edition." — `campaign/quests/faction-events/harpers/m02-the-dead-drop/ev-01-the-dead-drop.md:45`
- Campaign, Amath (gazetteer): "- Amath Sercent (Lawful Evil, Mulan Human, she/her), a well-mannered woman in common clothes, keeps the tower with four followers, and visitors find them at ease with the handprints." — `campaign/gazetteer/waterdeep/castle-ward.md:77`
- Campaign, Bane page (settled): "> - **Settled, Amath's race:** The published adventure makes her a Mulan human (`sources/adventure-wdh.json:9133`, `:9748`). The campaign now keeps the ethnicity explicit, as \"Mulan human\" on her Notable Figures page and `09-manshoons-zhentarim.md:103` and \"Mulan Human\" in the stat lines of `castle-ward.md:79` and `ev-01-the-yellowspire-job.md:219`. This page follows them." — `campaign/setting/deities/bane.md:128`
- Adventure, Khafeyta: "Khafeyta Murzan, a female Mulhorandi human {@creature swashbuckler|VGM} (see {@adventure appendix B|WDH|12})" — `sources/adventure-wdh.json:25456`
- Adventure, Amath: "Amath Sercent (LE female Mulan {@creature priest}) and her four followers (LE male and female {@creature acolyte||acolytes} of mixed ethnicities) dress in common clothing when outside the tower." — `sources/adventure-wdh.json:9748`
- Adventure, Kaevja: "{@creature Kaevja Cynavern|wdh} is a female Mulan human {@creature mage}, with these changes:" — `sources/adventure-wdh.json:29994`
- Adventure, WDMM (Karstis, not a campaign figure): "Karstis (LE male Mulhorandi human {@creature mage}) lurks here with four {@creature Minotaur Skeleton||minotaur skeletons}." — `sources/adventure-wdmm.json:23754`
- SCAG (book-scag.json, Mulhorand history): "Since the Chosen of the gods began to appear in the last few years, Mulhorand has become a land transformed. Its deities manifested fully in the forms of some of their descendants, and swiftly rallied the Mulan to overthrow the Imaskari. Aided by the mighty wizard Nezram, known as the World-Walker, the Mulhorandi overthrew the rulers of High Imaskar, who fled into the Plains of Purple Dust or to extraplanar safeholds." — `sources/5etools/book/book-scag.json:397`
- SCAG, the same history: "When the upheaval ended and the Chosen began to disappear, the gods of Mulhorand remained to rule their people, focusing their attention on defending their restored homeland to keep the war in Unther and Tymanther from spilling over its borders. For the first time in centuries, the people in Mulhorand are free, with the gods declaring that slavery shall no longer be practiced among the Mulan since their return." — `book-scag.json:398`
- SCAG, the human languages inset: "Many human ethnicities and nations in Faerûn have their own language, in addition to Common. Most human languages are written in Thorass, the alphabet of Old Common, derived from the Chondathan language that traders used as their common tongue. A few human languages use other alphabets, including Draconic, Dethek, and Espruar. The languages of the ethnicities described in the Player's Handbook and this book are as follows:" — `book-scag.json:6253`. The list follows, and it contains "Mulan:" with the entry "Chessentan, Mulhorandi, Untheric, or Thayan" (`book-scag.json:6310`-`:6311`).
- Heroes of Faerûn (`sources/5etools/book/book-frhof.json`, the newer source, which outranks SCAG): no line contains "Mulan" (a full-file search returned no match). "Mulhorandi" appears as a background, a language and a nation: "{@background Mulhorandi Tomb Raider|FRHoF}" (`book-frhof.json:719`); "{@language Mulhorandi|FRHoF}" (`:1815`); "Thay began as a colony of the distant Mulhorandi empire, and Delhumide was Thay's capital." (`:2580`); and "Languages:" with the entry "Chessentan, Mulhorandi, Untheric" under the Mulhorand realm entry (`:4093`-`:4098`).
- Alexandrian (PDF p.9, transcription): "Khafeyta – female Mulhorandi human swashbuckler (DH p. 216)" — `sources/9. Lair – Sea Maidens Faire.pdf`, PDF p.9.
- Decision record: "- [ ] **Khafeyta Murzan** is \"Mulhorandi\" (Dragon Heist's word) while the campaign's other Mulhorand humans read \"Mulan\". Keep or change." — `session 51 handoff.md:129`. "- [ ] **Khafeyta Murzan** \"Mulhorandi\" against \"Mulan\" (carried). Recommendation: keep \"Mulhorandi\"." — `session 52 handoff.md:109`
- Ruling in force: "- **Not asked, following the recommendation:** figures stay in the Draft Notes callouts; the Lords' Alliance page governs honest failure and reinstatement; Khafeyta Murzan stays \"Mulhorandi\"; Savra's embroidery line (`ev-09-aftermath.md:112`) stays." — `docs/plans/setting-compendium-pass6-brief.md:73`
- Higher rank for the species label: the published adventure (`sources/adventure-wdh.json:25456`) and the Alexandrian stat reference agree on "Mulhorandi". Campaign files use "Mulan" for every other Mulhorand human in the Notable Figures. The brief binds "Mulhorandi" for this pass.

**D7. The J29 room reference in her Persona.** "To the world, Khafeyta Murzan is the other one in J29" (`11-khafeyta-murzan.md:21`). J29 is a Sea Maidens Faire room (`campaign/structure/arc-h-sea-maidens-faire.md:158`). Restate it as a day-one fact (one of Jarlaxle's two companions) and route the room.

**D8. Parade and cabin (quest time).** The adventure places them in the Eyecatcher's "J29. Guest Cabin" (`sources/adventure-wdh.json:25445`-`:25449`, "{@i Eyecatcher only}"). Arc-h says J29 is "empty (Margo and Khafeyta march in the parade)" during the parade (`campaign/structure/arc-h-sea-maidens-faire.md:182`). Quest time; route to **Sea Maidens Faire**.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files.**
- `campaign/setting/villains/jarlaxle.md:184` (Draft Notes): "Also left out: the names of Luskan's High Captains, the Lantanese wizard and the nimblewright counts, the Zardoz Betrayal Pitch, Quilm, Margo Verida, Khafeyta Murzan, Malkolm Brizzenbright and Fenerus Stormcastle beyond the Manshoon note, Zelifarn, and the Alexandrian PDF 8 Eye-holder list." This is a deliberate omission, not a conflict. No Villains page carries her.
- `campaign/setting/organizations/07-bregan-daerthe.md:184` (Draft Notes): "Khafeyta Murzan's \"Mulhorandi\" is open ruling 15 and was not touched." The brief now settles it (D6). The org page is stale on "open".
- `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/03-vevette-blackwater.md:205`: "Alexandrian, Sea Maidens Faire stat reference, printed p.76 [PDF p.8]". The page is PDF p.9 (printed p.76). The Khafeyta line is correct; the PDF page number in that note is wrong.
- `docs/plans/faerun-ethnicities-research.md:354` and `:471` (not campaign files) record Khafeyta's ethnicity as a GAP. Listed for completeness.

**E2. Routed quest references (the quest-time facts on the page).**
- `campaign/structure/arc-h-sea-maidens-faire.md:158`: "**J29 (Guest Cabin).** Margo Verida (bard) + Khafeyta Murzan (swashbuckler). Jarlaxle's companions — skilled combatants and genuine friends. They can be charmed, deceived, or negotiated with: Margo responds to flattery about her music (DC 13 Persuasion), Khafeyta responds to a good fight story (DC 14 Persuasion). Neither will betray Jarlaxle, but both can be distracted." — J29 mechanics (Sea Maidens Faire).
- `campaign/structure/arc-h-sea-maidens-faire.md:182`: "**Parade Roster.** Significantly reduced. J1: 1 sailor. J3–J9: empty. J10: nimblewright only. J17: spiders (always present). J18: nimblewrights per tier. J29: empty (Margo and Khafeyta march in the parade). J30: nimblewright valet only. J31: mannequins (always present). Submarine: skeleton crew — U7b (1 gnome + 1 mate), all staterooms empty." — parade roster (quest time).
- `campaign/structure/arc-h-sea-maidens-faire.md:337`: "- **Notable Figures** — Full NPC profiles for Jarlaxle, Soluun, Fel'rekt, Krebbyg, Zelifarn, Margo Verida, Khafeyta Murzan, Fenerus Stormcastle, Malkolm Brizzenbright." (cross-reference list; no quest event)
- `sources/adventure-wdh.json:25473`-`:25477`: the secret door. "A secret door leading to a walk-in closet ({@area J28|393}) can be found with a successful {@dc 15} Wisdom (Perception) check." (`:25477`). Quest time (Sea Maidens Faire).
- `sources/adventure-wdh.json:25461`-`:25468`: the compelled divulgence (D3). Quest time.

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth, home district, family, age, origin.** No source gives any of these. Only "a female Mulhorandi human" (`sources/adventure-wdh.json:25456`) and "joined ... within the past year" (`:25459`). Do not name a new Notable Figure. A nameless relative or place is allowed.

**F2. How and why she came to the company.** Only "Margo and Khafeyta both joined the Sea Maidens Faire within the past year" (`:25459`) and the Motivations line: "She chose Jarlaxle's company for reasons similar to Margo's and arrived at the same conclusion through a different door." (`11-khafeyta-murzan.md:15`). The reasons are not stated for either woman. The company's recruiting habit is in the org page: "In this campaign Jarlaxle collects capable people whatever their species." (`campaign/setting/organizations/07-bregan-daerthe.md:41`).

**F3. Work before the Faire.** The acrobat job (`:25459`) and the swashbuckler stat (`:25456`). No prior employer, city or troupe is named.

**F4. Relationship with Margo, beyond the sources.** The adventure's romance (`:25459`) is the only sourced relationship. The campaign has not carried it (D5). The drafter must decide whether to use it; a `[design]` tag cannot settle a sourced claim.

**F5. Losses, grudges, a fear, a place she cares about.** None in any source.

**F6. Personal goals beyond the company.** The page's Motivations (`11-khafeyta-murzan.md:15`) give her wants: "Khafeyta wants to be excellent at her craft, spend time with people worth spending it with, and find situations complicated enough to be interesting." Those are the page's own wants, not sourced. Brief ruling 17 allows a `[design]` goal about a craft, a person she wants to keep or a place.

**F7. Physical appearance.** None as a day-one fact.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "Jarlaxle has taken a romantic interest in both women, who are also in love with each other." — `sources/adventure-wdh.json:25459` (romance; see D5)
- "Margo and Khafeyta are polite but terse." — `sources/adventure-wdh.json:25460`
- "Khafeyta Murzan, a female Mulhorandi human" — `sources/adventure-wdh.json:25456` (identity)
- "Khafeyta as an acrobat." — `sources/adventure-wdh.json:25459` (her first work with the Faire)
- "She is the more aggressive of the two companions, the one who steps forward while Margo controls the room behind her." — `11-khafeyta-murzan.md:23`
- "Deep down, she and Margo occupy different frequencies — Margo reads a room through its emotional resonance, Khafeyta through its exits and weapons — and between them they have all of it covered." — `11-khafeyta-murzan.md:21`
- "she checks for the difference between embellishment and truth" — `11-khafeyta-murzan.md:21`
- "a contented certainty about her own situation that reads as ease and is earned." — `11-khafeyta-murzan.md:13`
- "She will not betray Jarlaxle." — `11-khafeyta-murzan.md:23`
- Voice, day-one: "She never brags without proof, never fights unfairly, and never lets flattery work on her." — `.claude/skills/character-voices/voices/bregan-daerthe.md:214`
- Voice, day-one: "A true fight story wins her over, and embellishment loses her." — `.claude/skills/character-voices/voices/bregan-daerthe.md:211`
- Voice, a greeting she uses: "How'd you get that scar? Tell me true, and I'll buy the drink." — `.claude/skills/character-voices/voices/bregan-daerthe.md:216`
- Her Persona: "she is sharp and immediately interested in whether the person across from her has a story worth hearing" — `11-khafeyta-murzan.md:21`

---

## Not found

- Birth, home, family, age, former life, faith, a loss, a personal goal beyond the company, a fear, a place she cares about. Searched: `campaign/` (Grep for "Khafeyta|Murzan"), `sources/adventure-wdh.json` (Grep for "Khafeyta|Murzan"), `sources/*.md` (Grep for "Khafeyta|Vessa|Margo|Mulhorandi|Mulan"), `sources/SOURCE_GUIDE.md` (no line names her), `sources/research/**` (Grep, `campaign-hits.txt` copies only). No match gives any of these.
- The romance (`sources/adventure-wdh.json:25459`) is not in any campaign file. Searched `campaign/setting/notable-figures/bregan-daerthe/`, `campaign/structure/arc-h-sea-maidens-faire.md` and `campaign/quests/faction-events/bregan-daerthe/` for "romantic", "in love", "romance", "lovers" and "affair".
- Factions Guide (`campaign/guides/factions/08-bregan-daerthe.md`): no line names Khafeyta. Searched for "Khafeyta|Murzan" across `campaign/`.
- Villains: `campaign/setting/villains/jarlaxle.md` names her only in the omission note at `:184`.
- Alexandrian PDFs for Khafeyta: `sources/9. Lair – Sea Maidens Faire.pdf` (PDF p.9, read; PDF p.8, read, no match). Not read: `sources/10. Lair  Cassalanter Villa.pdf`, `sources/3. Player Character Factions.pdf`, `sources/1. The Villains.pdf` (not searched for her; PDFs are not greppable).
- Wiki: NOT FOUND stub for Khafeyta (scratchpad `wiki-bregan-daerthe/11-khafeyta-murzan.txt`, line 1).
- The campaign gives her no faction rank and no renown entry in the Factions Guide.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:687` lists `Cassalanters, their tragic backtstory, and Endgame setup.docx`; `sources/SOURCE_GUIDE.md:690` lists `Jarlaxle Baenre NPC Guide.docx`. Neither was checked for Khafeyta. Route to the caller for extraction.
- PDFs: text cannot be extracted without `pdftotext`. The one PDF page quoted (`sources/9. Lair – Sea Maidens Faire.pdf`, PDF p.9) is a page-image transcription and needs a `pdftotext -layout` check before any quote goes into prose.
