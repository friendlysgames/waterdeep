# Pass 6 research notes: Kaevja Cynavern

Page: `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1, 3, 4, 5, 6, 7, 8, 9, 15, 16, 17)
Model: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Consistency partners: `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md` (merged; read only). Havia (`12-havia-quickknife.md`) shares the E3 to E11 spaces with Kaevja in the sources, so her lines are cited where they bear on Kaevja.

Method and caveats:
- Campaign files: quoted from the tool output. Line numbers are from Read or Grep output.
- Published adventure: `sources/adventure-wdh.json`. JSON strings are quoted as plain text. Tags such as `{@creature ...}` are left as written. The Kaevja text sits in the E3 Guard Station entry (`"name": "E3. Guard Station"`, `:29988`) and the Dreadful Host entry (`:29905`).
- Alexandrian PDF: `sources/12. Lair  Zhentarim – Kolat Towers.pdf` (the dash is an en dash). The printed page is the PDF page plus 91 (PDF 3 = printed 94, PDF 4 = printed 95, PDF 5 = printed 96). This session has no shell, so `pdftotext` could not run. All Alexandrian quotes were transcribed from the rendered page images. **Each must be checked with `pdftotext -layout` before any prose use.**
- Wiki: `sources/research/pass5-bundles/zhentarim/wiki.txt` and the scratchpad extract `wiki-manshoons-zhentarim/11-kaevja-cynavern.txt` (NOT FOUND). See Not found.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDF and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

---

## A. Background facts by theme

### A1. Origin, Thay and the tattoos

**Former Red Wizard, the study, the cost (published adventure; the basis for the Background)**
> "Kaevja was a Red Wizard of Thay until she saw an opportunity to study magic under {@creature Manshoon|WDH}. Before he accepted her, {@creature Manshoon|WDH} forced her to remove her distinctive Thayan head tattoos and to trade in her Red Wizard robes for black ones."
> — `sources/adventure-wdh.json:29993` (E3 Guard Station, page 158)

**Same fact, campaign restatement**
> "- **Recruiting:** The Black Network has an open recruitment policy that prizes tenacity and loyalty without requiring either, but the published adventure says adventurers cannot join Manshoon's cause (*Dragon Heist*, 5e). His lieutenants rise by impressing him, and Agorn Fuoco was raised quickly after he made a good impression on the wizard (*Dragon Heist*, 5e). Kaevja Cynavern was a Red Wizard of Thay who gave up her Thayan head tattoos and red robes to study under him (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:71`

**Species and ethnicity (published adventure, the only source for the Mulan ethnicity)**
> "{@creature Kaevja Cynavern|wdh} is a female Mulan human {@creature mage}, with these changes:"
> — `sources/adventure-wdh.json:29994`

**Name pronunciation (published adventure, Pronunciation Guide)**
> "{@creature Kaevja Cynavern|WDH}",
> "CAVE-yah SIN-ah-vern"
> — `sources/adventure-wdh.json:173` and `:174` (the list is headed `"name": "Pronunciation Guide"` at `:25`)

**Thay in the Kossuth page (a different Red Wizard, Esloon Bezant, is named in the same bullet; no tie between them is stated)**
> "- Esloon Bezant is a Thayan Red Wizard exile who runs an escort-and-protection crew in the Dock Ward, and Kaevja Cynavern is a former Red Wizard of Thay who now serves Manshoon in the Kolat Towers sanctum (`sources/adventure-wdh.json:3922`, `:29993`). The wiki ties many Red Wizards to Kossuth, but no file names a god for either of them, so do not make them his worshipers on the strength of Thay alone."
> — `campaign/setting/deities/kossuth.md:68` (a Kossuth page bullet; the quote is the page's own text)

### A2. How she joined, and which Manshoon taught her

**The study (published adventure; the same paragraph as A1)**
> "Kaevja was a Red Wizard of Thay until she saw an opportunity to study magic under {@creature Manshoon|WDH}."
> — `sources/adventure-wdh.json:29993`

**The clones (published adventure; no line says which clone taught her)**
> "Referred to in this adventure simply as \"{@creature Manshoon|wdh},\" this clone of the ancient archwizard infiltrated Waterdeep years ago and has been hiding out in Kolat Towers ever since, in the city's Southern Ward."
> — `sources/adventure-wdh.json:32215`

> "The original {@creature Manshoon|WDH} was one of the founders of the Zhentarim. Evil to the core, he made enemies all across Faerûn, including other powerful spellcasters such as Khelben Arunsun and Elminster. Fearing that he might be destroyed by his foes, {@creature Manshoon|WDH} magically crafted several clones-but a mishap caused all of them to be awakened at once, whereupon they tried to destroy one another in a series of conflicts that came to be known as the {@creature Manshoon|WDH} Wars."
> — `sources/adventure-wdh.json:32216`

> "Now the original {@creature Manshoon|WDH} is dead, and it's widely believed that all his clones were destroyed as well. In fact, at least three are still alive. The one presently in Waterdeep escaped death by hiding out in Undermountain, where he eventually ran afoul of Halaster Blackcloak. After a brief spell duel, Halaster captured {@creature Manshoon|WDH} and amputated his left arm at the elbow for reasons unknown. {@creature Manshoon|WDH} escaped imprisonment and fled Undermountain, taking refuge in the city above. Attempts to magically regenerate his severed limb failed, forcing him to craft an artificial arm and hand for himself."
> — `sources/adventure-wdh.json:32217`

**Campaign: the claim every clone makes, and her reason for serving**
> "Every surviving clone claims to be the one true Manshoon, and this one holds the belief with absolute certainty. Loyalty to him runs from devotion to calculation. Havia Quickknife and Mookie Plush serve him completely, and Kaevja Cynavern serves him because he is the most capable operator she has met. Agorn Fuoco would trade whatever he knows to save himself. The published adventure says Havia and Mookie hold that Manshoon is the rightful leader of the Zhentarim and will sacrifice themselves to see his plans succeed (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:43` (the bullet is headed **One True Manshoon**)

**Campaign: the clone in the towers**
> "The man in Kolat Towers is the clone who hid in Undermountain, and the Manshoon a party meets first may be his simulacrum, which fights as his decoy while he leaves. The stasis clone spell is a separate insurance against dying for good. His name belongs to the members of his cell, and the street crews do not use it."
> — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:115` (the GM text of the Manshoon page; the sentences before it are on the same callout)

**Campaign timing of the cell (the Splinter is about two years old on Ches 1)**
> "He spent about two years building the Splinter, a cell that bears his name and works independently of the Zhentarim's surviving leadership. It is hub and spoke, with Kolat Towers as the command center and the Interrogation House in the North Ward and Yellowspire in the Castle Ward as field offices linked by teleportation circles. A pass-amulet system lets him revoke anyone's access from the towers (**Kolat Towers** quest opener). He took a large part of the local network the Doom Raiders had built, and through it learned that Lord Neverember had used the local Zhentarim's resources to embezzle the vault's gold (Alexandrian Remix, *The Villains*, p. 16). On Ches 1, 1492 DR the cell holds Kolat Towers, Yellowspire and the Interrogation House, and it fights Xanathar's Guild in the Dock Ward (**Manshoon's Zhentarim**)."
> — `campaign/setting/villains/manshoon.md:33`

### A3. Post and daily work

**The post (published adventure, E3 Guard Station)**
> "A 5-foot-square window in this area looks out toward {@area E1|413}. Unless she has been drawn elsewhere, {@creature Kaevja Cynavern|wdh} stands watch in front of the window."
> — `sources/adventure-wdh.json:29992`

**The sanctum and its watchers (campaign, Organizations page)**
> "- **The sanctum:** Behind the towers lies an extradimensional sanctum in a finite demiplane, which the original Manshoon created and his clones all know. A teleporter ring and the circle in the towers are the way in (*Dragon Heist*, 5e). Kaevja Cynavern watches the entrance and is Manshoon's early-warning mechanism, Havia Quickknife and Mookie Plush keep his audience chamber, and Yorn the Terror is the enforcer who maintains the household's fear of its master (**Kaevja Cynavern**; **Havia Quickknife**; **Mookie Plush**; **Yorn the Terror**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:55`

**The household (campaign, Manshoon page)**
> "- **Kaevja Cynavern**, **Havia Quickknife**, **Mookie Plush**, **Manafret Cherryport** and **Yorn the Terror:** His household in Kolat Towers and the sanctum behind it. Kaevja watches the entrance, Havia and Mookie keep his audience chamber, Manafret cooks, and Yorn keeps the household afraid of its master."
> — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60`

**The sleeping room (published adventure, E11 Zhent Quarters)**
> "{@creature Kaevja Cynavern|wdh}, Vevette Blackwater, Agorn Fuoco, {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife}, and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} all sleep here."
> — `sources/adventure-wdh.json:30212` (E11 entry at `:30199`, page 160)

**The sending as her function (campaign, the sanctum's alarms)**
> "- **Messengers:** Black flying snakes carry the cell's orders between its sites, and three of them nest at the Interrogation House while Urstul keeps a collection of his own (**North Ward**; **Urstul Floxin**). The wiki says the Zhentarim often used flying snakes as messenger animals (Forgotten Realms Wiki, *Zhentarim*, edition not tagged), and Davil Starsong's briefings also arrive by flying snake (*Dragon Heist*, 5e). Kaevja Cynavern relies on the *sending* spell for the sanctum's alarms (**Kaevja Cynavern**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:64` (the rest of the bullet covers the flying snakes)

### A4. Training, languages and spells

**Languages (published adventure)**
> "Kaevja is lawful evil. She knows Common, Draconic, Dwarvish, and Elvish."
> — `sources/adventure-wdh.json:29998`

**Spell choice (published adventure)**
> "She has the {@spell sending} spell prepared instead of the {@spell fly} spell, and she carries a yellow {@i elemental gem}."
> — `sources/adventure-wdh.json:29999`

**The elemental gem (published adventure)**
> "In battle, Kaevja breaks the {@i elemental gem}, summoning an {@creature earth elemental} and commanding it to attack her enemies."
> — `sources/adventure-wdh.json:30002`

**Campaign: the same spell and gem (Lair structure doc)**
> "**E3 — Guard Station.** Kaevja Cynavern (mage), Sidra's counterpart in the sanctum. Kaevja carries a yellow elemental gem (earth elemental) and has the sending spell prepared at all times. If she is not eliminated silently before she acts, her first action is to cast sending to Manshoon — regardless of his location — and to Agorn Fuoco or Vevette Blackwater in E8. A successful sending accelerates the reinforcement timer by 5 minutes. Kaevja is the sanctum's force multiplier: her sending is more dangerous than her combat capability. The party should treat her as a priority target."
> — `campaign/structure/arc-i-kolat-towers.md:150` (the last three sentences are quest-time; see C)

### A5. Belongings

**Chest in E11 (published adventure)**
> "Kaevja's chest contains a gold amulet inset with a red crystal rune (worth 250 gp). A successful {@dc 15} Intelligence (Arcana) check reveals that the rune is a symbol of evocation, though the amulet is nonmagical."
> — `sources/adventure-wdh.json:30220` (Treasure entry at `:30215`, page 160)

**Teleporter rings (published adventure; the text does not say Kaevja wears one)**
> "To access {@creature Manshoon|WDH}'s extraplanar sanctum, one needs a {@item teleporter ring|WDH}: a brass signet ring bearing a stylized M, and which emanates an aura of conjuration magic when targeted by a {@spell detect magic} spell or similar magic. {@creature Manshoon|WDH} gives these rings to his most trusted servants."
> — `sources/adventure-wdh.json:28822` (Teleporter Rings entry at `:28818`)

Her ring appears only in the Alexandrian roster (asterisk; see D2). The published ring lines name Sidra (`sources/adventure-wdh.json:28156`), Manafret (`:28200`), and Havia and Mookie (`:30192`).

### A6. Relationships on day one

**Sidra's counterpart (campaign, Lair structure doc)**
> "**E3 — Guard Station.** Kaevja Cynavern (mage), Sidra's counterpart in the sanctum."
> — `campaign/structure/arc-i-kolat-towers.md:150`

**Sidra's page (merged; read only)**
> "- **Kaevja Cynavern:** The mage who watches the entrance to the sanctum. Kaevja holds the watch there while Sidra holds the watch on the ground floor."
> — `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:40`

**Her current Persona (campaign, existing text)**
> "Deep down, she serves Manshoon because he is the most capable operator she has encountered, and working for the most capable operator available is, in her estimation, the rational choice until demonstrated otherwise."
> — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:21` (the Organizations page says "met" at `:43`; the voice profile says "available" at `.claude/skills/character-voices/voices/manshoons-zhentarim.md:194`)

**Shared room (published adventure)**: see A3, `sources/adventure-wdh.json:30212`.

### A7. Faith

No source names a god for Kaevja. The campaign rule is on the Kossuth page (`campaign/setting/deities/kossuth.md:68`, quoted in A1: "so do not make them his worshipers on the strength of Thay alone"). The Yondalla page's halfling list leaves her out (`campaign/setting/deities/yondalla.md:65`, quoted under Cross-references).

### A8. Rank and time in post

No source gives a rank, a date of joining or length of service for Kaevja. The Organizations page lists her under **Key Members** with no rank term (`campaign/setting/organizations/09-manshoons-zhentarim.md:106`). The Manshoon page calls her household, not lieutenant (`01-manshoon.md:60`). The Manshoon page's Sources line groups her with the lieutenants (`01-manshoon.md:147`; see D3).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, current page: "*Mulan human mage, lawful neutral, she/her*. Stat block: **Mage**." — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:5`
- Campaign, Organizations page: "- **Kaevja Cynavern** — Mulan human mage, lawful neutral; see the **Kaevja Cynavern** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:106`
- Published adventure, conflicting: "Kaevja is lawful evil. She knows Common, Draconic, Dwarvish, and Elvish." — `sources/adventure-wdh.json:29998`
- Alexandrian, printed p. 95 [PDF 4]: "Kaevja Cynavern (female Mulan human) – mage, MM p. 347; see DH p. 158" (no alignment for Kaevja; the Sidra and Havia entries on the same page give "LE"). Image transcription.

**Species**
- Campaign: "Mulan human" — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:5`; `campaign/setting/organizations/09-manshoons-zhentarim.md:106`
- Published adventure: "is a female Mulan human {@creature mage}, with these changes:" — `sources/adventure-wdh.json:29994`
- Alexandrian, printed p. 95 [PDF 4]: "(female Mulan human)" (image transcription)

**Pronouns**
- Campaign: "she/her" — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:5`
- Published adventure: "is a female Mulan human" — `sources/adventure-wdh.json:29994`
- Pronoun table: "| Kaevja Cynavern | manshoons-zhentarim/11-kaevja-cynavern.md:5 | she/her | prose (\"the moment the party sees her reach for a spell component\", \"She is already reaching for her component pouch\") | High |" — `docs/plans/npc-pronouns-table-group-c.md:55`

**Stat block label**
- Campaign: "Stat block: **Mage**." — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:5`
- Published adventure: "{@creature Kaevja Cynavern|wdh} is a female Mulan human {@creature mage}, with these changes:" — `sources/adventure-wdh.json:29994` (changes at `:29998` and `:29999`)
- Alexandrian, printed p. 95 [PDF 4]: "mage, MM p. 347; see DH p. 158" (image transcription)

**Stat changes (published adventure; no hit points are given for Kaevja, unlike Havia and Mookie at `:30188`)**
> "She has the {@spell sending} spell prepared instead of the {@spell fly} spell, and she carries a yellow {@i elemental gem}."
> — `sources/adventure-wdh.json:29999`

---

## C. Sentences on the current page that narrate a quest event or a day-one conflict

Current page: `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md`. "Day-one OK" means the sentence needs no quest gate. "Quest-time" means it names the party, an intrusion, a capture or a combat sequence.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Mulan human mage, lawful neutral, she/her*. Stat block: **Mage**." | Day-one. Alignment conflicts with the adventure (D1) | Org `:106`; adventure `:29998` (D1) |
| 2 | L6 | "**Affiliation:** Manshoon's Zhentarim" | Day-one OK | Org `:1` (heading "Manshoon's Zhentarim") and `:106` |
| 3 | L7 | "**Featured in:** **Kolat Towers**" | Quest reference in the Summary (kept, as the other pages do). No Kolat Towers quest journal exists; the structure doc is `campaign/structure/arc-i-kolat-towers.md` | Structure doc (no line cited) |
| 4 | L11 | "**Resonance.** Kaevja should inspire wariness the moment the party sees her reach for a spell component — she is the sanctum's communications node, not its strongest fighter, and players who understand this will understand why she is the most important target in E3." | Mixed. "the moment the party sees her" and "the most important target in E3" are quest-time framing. "communications node, not its strongest fighter" is day-one | `arc-i-kolat-towers.md:150` ("The party should treat her as a priority target."; "her sending is more dangerous than her combat capability") |
| 5 | L13 | "**Emotions.** Kaevja most often feels professional alertness, calculated assessment of threats and exits, calm certainty about her role in the sanctum's security architecture, and controlled urgency about any situation that develops faster than her protocols allow for." | Day-one OK | Voice `:195` (protocols), `:196` ("Alert and calculating.") |
| 6 | L15 | "**Motivations.** Kaevja wants to earn her continued place in Manshoon's organization, protect the sanctum against unauthorized entry, and cast the sending that accelerates reinforcements before she is incapacitated." | "protect the sanctum" is day-one. "accelerates reinforcements before she is incapacitated" is quest-time (combat and the reinforcement timer) | `arc-i-kolat-towers.md:150` ("A successful sending accelerates the reinforcement timer by 5 minutes."); `arc-i-kolat-towers.md:170` (the timer) |
| 7 | L17 | "**Inspirations.** When playing Kaevja, channel Elim Garak (*Deep Space Nine*), Lisbeth Salander (*The Girl with the Dragon Tattoo*), and Natasha Romanoff (*Marvel Cinematic Universe*)." | Not a fact | n/a |
| 8 | L21 (a) | "**Persona.** To the world — specifically to anyone who has breached E2 and triggered the Mask discharge — Kaevja is the mage at E3, already reaching for her component pouch." | Quest-time gate: "anyone who has breached E2 and triggered the Mask discharge" | `arc-i-kolat-towers.md:148` ("the discharge also sends a magical pulse to E3, alerting Kaevja."); `sources/adventure-wdh.json:29957` (the E2 alarm lists Kaevja) |
| 9 | L21 (b) | "To Manshoon, she is the sanctum's most reliable early-warning mechanism, valued more for the sending she can cast than for the spells she throws in combat." | Day-one OK | Org `:55` ("Kaevja Cynavern watches the entrance and is Manshoon's early-warning mechanism"); Org `:64` |
| 10 | L21 (c) | "Deep down, she serves Manshoon because he is the most capable operator she has encountered, and working for the most capable operator available is, in her estimation, the rational choice until demonstrated otherwise." | Day-one. Attitude only | Org `:43` ("the most capable operator she has met"); Voice `:194` ("the most capable operator available") |
| 11 | L23 (a) | "**Morale.** Kaevja's first action is always the sending — to Manshoon's current location and to E8 — not combat." | Combat sequence. The sanctum's reaction to intruders | `arc-i-kolat-towers.md:150` ("her first action is to cast sending to Manshoon — regardless of his location — and to Agorn Fuoco or Vevette Blackwater in E8"); `sources/adventure-wdh.json:29909` |
| 12 | L23 (b) | "If she sends successfully and the party's attention is fully on her, she uses the earth elemental gem and fights behind it." | Quest-time (party attention; a combat sequence) | `sources/adventure-wdh.json:30002`; `arc-i-kolat-towers.md:150` |
| 13 | L23 (c) | "If the party eliminates her silently before she can act, she contributes nothing; if she succeeds, she has made the entire operation significantly harder." | Quest-time (the party) | `arc-i-kolat-towers.md:150` ("If she is not eliminated silently before she acts"); `arc-i-kolat-towers.md:182` ("Kaevja in E3") |
| 14 | L25 (a) | "**Relationships.** Kaevja is Sidra Romeir's sanctum counterpart in E3, Manshoon's primary early-warning mechanism, a mage whose communications role matters more than her combat capability," | Day-one OK | `arc-i-kolat-towers.md:150`; Org `:55` |
| 15 | L25 (b) | "and the party's most time-sensitive priority target in the extradimensional sanctum." | Quest-time (the party; time-sensitive) | `arc-i-kolat-towers.md:150` ("The party should treat her as a priority target."); `arc-i-kolat-towers.md:170` (the timer) |
| 16 | L29 | "A mage stationed in the inner sanctum of Kolat Towers. She is already reaching for her component pouch the moment anyone enters the room." | Day-one readiness. "the moment anyone enters the room" is conditional on intrusion (borderline). "component pouch" has no published line; it is in the voice profile only | Voice `:197` ("She's reaching for her component pouch before she speaks."); `sources/adventure-wdh.json:29992` (the post) |

**Voice profile quest-time clauses** (`.claude/skills/character-voices/voices/manshoons-zhentarim.md`, Kaevja block at `:189` to `:203`):
- `:201` to `:202`, the Greeting and Business sample lines. The Business line is "Breach at E3, four intruders, armed, one caster. Mask discharged. Request immediate reinforcement. Holding." It narrates an intrusion. Under ruling 16 it needs the day-one restatement. The timer it draws on is `arc-i-kolat-towers.md:170`.
- `:198`, the Signature phrase "Breach, E3." Same trigger as the Business line.
- `:203`, the Under-pressure line "Shit, that's not in the protocol. Fall back to E4." Hypothetical. Kept.
- `:199`, Never: "She never lets the Sending go uncast, never hesitates, and never pretends loyalty is sentiment." Day-one.

---

## D. Conflicts

**D1. Alignment: lawful neutral against lawful evil**
- Campaign, the current page: "*Mulan human mage, lawful neutral, she/her*." — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:5`
- Campaign, the Organizations page: "- **Kaevja Cynavern** — Mulan human mage, lawful neutral; see the **Kaevja Cynavern** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:106`
- Published adventure: "Kaevja is lawful evil. She knows Common, Draconic, Dwarvish, and Elvish." — `sources/adventure-wdh.json:29998`
- Higher source: the campaign (the page and the Organizations page both say lawful neutral). **The orchestrator decides.** The pass-5 check compared the Organizations line with the page only (`docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:131`, "Result: matches") and did not check the adventure.

**D2. Ring**
- Alexandrian, printed p. 94 [PDF 3], roster: "Kaevja Cynavern*" with the footnote "* Has a teleporter signet ring." (image transcription)
- Published adventure, Havia and Mookie only: "Havia and Mookie each wear a {@item teleporter ring|WDH} (see \"Teleporter Rings\")." — `sources/adventure-wdh.json:30192`. No Kaevja ring line exists in the adventure.
- Campaign, rings go to the trusted servants: "his brass teleporter rings, each bearing a stylized M, go only to his most trusted servants." — `campaign/setting/organizations/09-manshoons-zhentarim.md:41` (the bullet continues with Sidra holding the rings)
- Campaign, the ring-to-Kaevja sentence `[research]`, quest-time: "if captured lieutenants are killed she gives their rings to Kaevja `[research]`" — `campaign/setting/organizations/09-manshoons-zhentarim.md:97` (Sidra's Key Members bullet)
- Higher source: no source gives Kaevja a ring with a stated origin. The Alexandrian asterisk is the only source that says she holds one. The ring-to-Kaevja sentence has no source (the pass-5 and pass-6 Sidra notes both say so).

**D3. Lieutenant or household**
- Campaign, Manshoon page, the household bullet: "- **Kaevja Cynavern**, **Havia Quickknife**, **Mookie Plush**, **Manafret Cherryport** and **Yorn the Terror:** His household in Kolat Towers and the sanctum behind it." — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60`
- Campaign, Manshoon page, the Sources line: "the cell's lieutenants, household and sites" — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:147` (the list includes Kaevja)
- Published adventure, the lieutenants a captured proof would come from: "These lieutenants include Sidra Romeir ({@area K2|3db}), {@creature Manafret Cherryport|wdh} ({@area K3|3de}), {@creature Urstul Floxin|wdh} ({@area E5|41d}), Vevette Blackwater and Agorn Fuoco ({@area E8|425}), and {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} ({@area E10|42a})." — `sources/adventure-wdh.json:26763` (Kaevja is not on the list; the sentence before it is the offer to turn lieutenants over for interrogation)
- Campaign, Sidra page, "The other lieutenants": "**Urstul Floxin**, **Vevette Blackwater** and **Agorn Fuoco** serve the cell as lieutenants and field leaders." — `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:38` (Kaevja is not on the list)
- Higher source: the campaign's household label (`01-manshoon.md:60`). The Sources line at `:147` is the outlier.

**D4. What the lieutenants know (the Alexandrian against the campaign, and the Alexandrian against itself)**
- Alexandrian, printed p. 95 [PDF 4]: "Manshoon’s lieutenants wear special rings that let them access Manshoon’s sanctuary atop the Outer Tower (although they don’t know that this is actually an extradimensional space; they think he just lives up there)." (image transcription)
- Alexandrian, printed p. 96 [PDF 5]: "Manshoon’s lieutenants know what the apprentice wizards know, but also:", with the bullets "The layout of the extradimensional sanctum, including the location of the astral vault." and "That the Cassalanters are the noble family who possess the third Eye." (image transcription)
- Campaign, Organizations page: "- **The sanctum:** Behind the towers lies an extradimensional sanctum in a finite demiplane, which the original Manshoon created and his clones all know." — `campaign/setting/organizations/09-manshoons-zhentarim.md:55`
- Campaign, Manshoon page: "It became Eye #3, and Manshoon holds no Eye (**Running the Villains**)." — `campaign/setting/villains/manshoon.md:36`
- Higher source: the campaign. Kaevja's knowledge is not stated anywhere in the campaign. The Alexandrian contradicts itself on p. 95 and p. 96 on whether lieutenants know the sanctum is extradimensional. The page should state nothing about her knowledge of the Eyes or of the sanctum's nature unless the orchestrator decides.

**D5. Sending target**
- Published adventure: "She uses a {@spell sending} spell to contact {@creature Manshoon|WDH} as soon as the characters arrive." — `sources/adventure-wdh.json:29909`
- Campaign, Lair structure doc: "her first action is to cast sending to Manshoon — regardless of his location — and to Agorn Fuoco or Vevette Blackwater in E8." — `campaign/structure/arc-i-kolat-towers.md:150`
- Campaign, the page: "Kaevja's first action is always the sending — to Manshoon's current location and to E8" — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:23`
- Not a conflict in substance. E8 holds Vevette and Agorn: "Vevette Blackwater and Agorn Fuoco (see {@area E8|425})" — `sources/adventure-wdh.json:29959`.

**D6. Elemental gem colour**
- Published adventure: "she carries a yellow {@i elemental gem}." — `sources/adventure-wdh.json:29999`
- Campaign structure doc: "Kaevja carries a yellow elemental gem (earth elemental)" — `campaign/structure/arc-i-kolat-towers.md:150`
- Campaign page: "she uses the earth elemental gem and fights behind it" — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:23`
- Consistent. The page's "earth elemental gem" names the gem by its effect: "breaks the {@i elemental gem}, summoning an {@creature earth elemental}" (`sources/adventure-wdh.json:30002`).

**D7. Stat label**
- Campaign "Mage" (`:5`), published adventure "{@creature mage}" (`sources/adventure-wdh.json:29994`), Alexandrian "mage, MM p. 347" (printed p. 95). Consistent.

**D8. Stale ethnicity rows in planning docs (see E1)**
- `docs/plans/faerun-ethnicities-research.md:339` says the page reads "`Human mage, lawful neutral` — GAP" at `11-kaevja-cynavern.md:6`, and the Organizations page reads "`Kaevja Cynavern** — Human` — GAP" at `:33`. Both are out of date. The page now reads "Mulan human" at `:5`, and the Organizations page reads "Mulan human mage" at `:106`.

---

## E. Stale lines in other files (not edited), and routed quest references

### E1. Stale lines
- `campaign/setting/organizations/09-manshoons-zhentarim.md:184` (Draft Notes): "Manshoon's three apprentices, Kaevja's Thayan past, the Candle Lane warehouse's role as a training depot and Agorn's rapid rise come from the published adventure alone and have no Notable Figures page." Stale: `11-kaevja-cynavern.md` exists, and the Thayan past is now also at `:71`.
- `campaign/structure/arc-i-kolat-towers.md:320`: "- **Notable Figures** — Existing profiles: Manshoon, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin, Lady Gondafrey, Skeemo Weirdbottle. New profiles needed: Kaevja Cynavern, Havia Quickknife, Mookie Plush, Yorn the Terror." Stale for Kaevja (her profile exists).
- `docs/plans/faerun-ethnicities-research.md:339` and `:471` (see D8). Stale.
- `campaign/setting/organizations/09-manshoons-zhentarim.md:97` (the ring-to-Kaevja `[research]` sentence). Not changed, but unsourced (see D2).
- `sources/SOURCE_GUIDE.md:35`: "Contains: Manshoon, his simulacrum, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin." It omits Kaevja, Havia and Mookie. Incomplete rather than wrong.

### E2. Routed to quests (quest-time facts and where they already live)
- The sanctum alarm, E2 to E3: `campaign/structure/arc-i-kolat-towers.md:148` ("This is the sanctum's entry alarm — the discharge also sends a magical pulse to E3, alerting Kaevja.") and `:182` ("E2's pressure plate, Kaevja in E3, and Urstul in E5 are all alarm triggers even without tower combat.")
- The reinforcement timer and Kaevja's sending: `arc-i-kolat-towers.md:170`, `:174` ("| 0 min | Alarm triggers. Sidra activates internal response in K2. All NPCs shift to defensive positions. Kaevja in E3 casts sending (if not yet eliminated). |"), `:175` ("| 5 min | 2 thugs arrive at K22 from the Interrogation House via the Yellowspire circle. Kaevja's sending reaches Manshoon and field agents if not silenced. |"), and `:184` (tier variation: "At Suspicious, reduce to 25 minutes (Kaevja receives an earlier sending confirmation, Sidra's standing orders are more aggressive).")
- Her first action on arrival: `sources/adventure-wdh.json:29909` (quoted in D5).
- The published capture offer (lieutenants; Kaevja not named): `sources/adventure-wdh.json:26763` (quoted in D3). Routed to **Kolat Towers**.
- The ring to Kaevja `[research]`: no quest file routes it. The Sidra page excluded it (`04-sidra-romeir.md:121`).

---

## F. Gaps (what a Background would need that no source gives)

Each gap lists the sourced facts the drafter must stay consistent with.

1. **Birth, family, childhood, Thay before the study.** No source. The only Thay facts are at `sources/adventure-wdh.json:29993` (A1). Consistency: she was a Red Wizard of Thay, a female Mulan human, before she studied under Manshoon.
2. **Why she left Thay.** No source. The published text says only "until she saw an opportunity to study magic under {@creature Manshoon|WDH}" (`:29993`). Consistency: the study was her opportunity, in that line's terms.
3. **Where and when she studied under Manshoon.** No source gives the place or the year, and none says which clone taught her (`sources/adventure-wdh.json:32215` "infiltrated Waterdeep years ago"; `:32217` "at least three are still alive"). Consistency: the Manshoon page says the Waterdeep clone is "the clone who hid in Undermountain" (`01-manshoon.md:115`). A date for the study must not put her in Waterdeep before the Splinter (about two years before Ches 1, `campaign/setting/villains/manshoon.md:33`) unless the drafter explains why. The Sidra page uses the same constraint: "She came to his service no earlier than the founding of the Splinter, about two years before Ches 1, 1492 DR `[research]`." (`04-sidra-romeir.md:17`)
4. **The tattoos and robes.** Sourced: she gave up "her distinctive Thayan head tattoos" and her "Red Wizard robes for black ones" (`:29993`). What the tattoos showed, and whether any mark remains, is not given.
5. **Her amulet.** The chest holds "a gold amulet inset with a red crystal rune" (`:30220`), and the text says it is "nonmagical". Who gave it, and what it means to her, is not given. Consistency: keep "nonmagical" and the evocation rune as printed.
6. **Faith.** No god is named. Consistency: `campaign/setting/deities/kossuth.md:68` says not to make the Red Wizards worshipers "on the strength of Thay alone."
7. **Rank and date of joining** (see A8 and D3). Consistency: she is in the household (`01-manshoon.md:60`), and not on the lieutenant list of the published capture offer (`sources/adventure-wdh.json:26763`).
8. **Her ring.** The Alexandrian shows an asterisk (printed p. 94), and no published or campaign line gives her a ring with an origin (D2). Consistency: do not give her ring-holding duties; the ring-to-Kaevja sentence has no source.
9. **Knowledge of the Eyes and the sanctum.** See D4. Consistency: the campaign says Manshoon holds no Eye (`campaign/setting/villains/manshoon.md:36`), and the sanctum is "which the original Manshoon created and his clones all know" (`campaign/setting/organizations/09-manshoons-zhentarim.md:55`). The Alexandrian's p. 96 bullet on the third Eye is not in the campaign. The Cassalanter secrecy rule (brief ruling 7) applies: nobody outside the household and the cult knows about the pact.
10. **Fears, loves, grudges, habits outside the post.** None sourced. See G.
11. **Relationship to Sidra beyond "counterpart".** No source gives a personal tie. Consistency: Sidra's page says Kaevja "holds the watch there while Sidra holds the watch on the ground floor" (`04-sidra-romeir.md:40`).
12. **Relationship to Vevette, Agorn, Havia and Mookie.** Only the sleeping room is sourced (`sources/adventure-wdh.json:30212`). Consistency: she sleeps in the same room as those four.
13. **Mulan origin and home city.** No source. Only the ethnicity (`:29994`).
14. **Morale and two Relationship sentences are combat text.** Rows 11 to 13 and 15 of C. A Background that gives a reason for her caution must not name the party's actions.

---

## G. Inner-life hints in the sources (exact quotes)

These are for the drafter's Background and personal goals (brief ruling 17). Each must stay consistent with them.

**Ambition and the cost of it** (published adventure)
> "Kaevja was a Red Wizard of Thay until she saw an opportunity to study magic under {@creature Manshoon|WDH}. Before he accepted her, {@creature Manshoon|WDH} forced her to remove her distinctive Thayan head tattoos and to trade in her Red Wizard robes for black ones."
> — `sources/adventure-wdh.json:29993`

**Her view of Manshoon** (campaign, Organizations page)
> "Kaevja Cynavern serves him because he is the most capable operator she has met."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:43` (within the bullet quoted in A2)

**Her standing and place** (campaign, the page's own Motivations, existing text)
> "**Motivations.** Kaevja wants to earn her continued place in Manshoon's organization, protect the sanctum against unauthorized entry, and cast the sending that accelerates reinforcements before she is incapacitated."
> — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:15`

**Her temper and protocols** (voice profile)
> "**Swearing:** *Triggered · Plain · Phrase.* When a situation outruns her protocols (\"Shit, that's not in the protocol.\")."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:195`

> "**Personality in speech:** Alert and calculating. She serves Manshoon because it's rational, and says so if asked. She's urgent when events move faster than protocol."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:196`

**Her limit** (voice profile, Never)
> "**Never:** She never lets the Sending go uncast, never hesitates, and never pretends loyalty is sentiment."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:199`

**Her possession** (published adventure)
> "Kaevja's chest contains a gold amulet inset with a red crystal rune (worth 250 gp). A successful {@dc 15} Intelligence (Arcana) check reveals that the rune is a symbol of evocation, though the amulet is nonmagical."
> — `sources/adventure-wdh.json:30220`

**Her learning** (published adventure)
> "Kaevja is lawful evil. She knows Common, Draconic, Dwarvish, and Elvish."
> — `sources/adventure-wdh.json:29998` (the alignment is in conflict; D1)

**Her place among the household** (published adventure)
> "{@creature Kaevja Cynavern|wdh}, Vevette Blackwater, Agorn Fuoco, {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife}, and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} all sleep here."
> — `sources/adventure-wdh.json:30212`

---

## Cross-references

Every other file:line where Kaevja appears, with the line copied (grep output, this session). Lines already quoted above are marked "see".

**Campaign, Organizations page** (`campaign/setting/organizations/09-manshoons-zhentarim.md`)
- `:43` "- **One True Manshoon:** ... Kaevja Cynavern serves him because he is the most capable operator she has met." (see A2)
- `:55` "- **The sanctum:** ... Kaevja Cynavern watches the entrance and is Manshoon's early-warning mechanism, ..." (see A3)
- `:64` "... Kaevja Cynavern relies on the *sending* spell for the sanctum's alarms (**Kaevja Cynavern**)." (see A3)
- `:71` "... Kaevja Cynavern was a Red Wizard of Thay who gave up her Thayan head tattoos and red robes to study under him (*Dragon Heist*, 5e)." (see A1)
- `:97` "- **Sidra Romeir** — ... if captured lieutenants are killed she gives their rings to Kaevja `[research]`. ..." (see D2)
- `:106` "- **Kaevja Cynavern** — Mulan human mage, lawful neutral; see the **Kaevja Cynavern** page in Notable Figures." (see B and D1)
- `:184` (Draft Notes): "... Kaevja's Thayan past, ... come from the published adventure alone and have no Notable Figures page." (see E1)

**Campaign, Manshoon page** (`campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md`)
- `:60` (see D3)
- `:115` (no name; "The man in Kolat Towers is the clone who hid in Undermountain ..."; see A2)
- `:147` "- **Sidra Romeir**, **Urstul Floxin**, ... **Kaevja Cynavern**, **Havia Quickknife**, ... (Notable Figures): the cell's lieutenants, household and sites" (see D3)
- `:264`-`:265` (pass-6 research notes, not the page): quotes `sources/adventure-wdh.json:29993` as "Adventure, Kaevja (recruitment)".

**Campaign, Sidra page** (`campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md`)
- `:40` (see A6)
- `:106` "- **Manshoon**, **Urstul Floxin**, ... **Kaevja Cynavern**, **Davil Starsong** (Notable Figures): her master, the other lieutenants, the cook, the sanctum's watch and the leader of the other Zhentarim cell"
- `:121` (Draft Notes, "Conflicts: Rings to Kaevja") (see D2)

**Campaign, villains and deities**
- `campaign/setting/villains/manshoon.md:33` and `:36` (see A2 and D4). The villain page does not name Kaevja.
- `campaign/setting/deities/kossuth.md:68` (see A1, A7).
- `campaign/setting/deities/kossuth.md:82`: "- `sources/adventure-wdh.json`: the Major Temples of Waterdeep table (no Kossuth row; caption at line 30910, Holyhands House at lines 30923 to 30925), Esloon Bezant as a Red Wizard of Thay (line 3922) and Kaevja Cynavern as a former Red Wizard (line 29993). No line of `sources/adventure-wdh.json` or `sources/adventure-wdmm.json` names Kossuth."
- `campaign/setting/deities/kossuth.md:95`: "- **Esloon Bezant**, **Kaevja Cynavern** (Notable Figures): the two Red Wizards in the campaign files."
- `campaign/setting/deities/yondalla.md:65` (Kaevja not named; the bullet names Havia and Mookie): "... The halflings among them are **Broxley Fairkettle**, **Osco Salibuck**, **Kelso Fiddlewick**, **Corene Wyldath**, **Manafret Cherryport**, **Havia Quickknife** and **Mookie Plush**, and none of their pages gives a god, so this page makes none of them a worshiper."

**Campaign, Lair structure doc** (`campaign/structure/arc-i-kolat-towers.md`)
- `:148`, `:150`, `:170`, `:174`, `:175`, `:182`, `:184` (see A4, C, D5 and E2)
- `:320` (see E1)
- `:160`: "**E10 — Audience Chamber.** Havia Quickknife + Mookie Plush, two halfling adepts who serve as Manshoon's household fanatics. ..." (Havia's page; not Kaevja's)

**Campaign, character voices**
- `.claude/skills/character-voices/voices/manshoons-zhentarim.md:189`-`:203` (the Kaevja block; see B, C and G)
- `.claude/skills/character-voices/SKILL.md:34`: "| `voices/manshoons-zhentarim.md` | Manshoon, Floxin, Vevette, Sidra, Agorn, Avareen, Zorbog, Amath, Vira, Manafret, Kaevja, Havia, Mookie, Yorn |"

**Docs** (planning and research notes; none edited)
- `docs/plans/npc-pronouns-table-group-c.md:55` (see B)
- `docs/plans/faerun-ethnicities-research.md:339`, `:471` (see D8)
- `docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:131` and `:260`: "... Result: matches." and "The drafter must drop or source the Kaevja sentence." (see D1 and D2)
- `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/04-sidra-romeir.md:220`, `:231` ("**D11. Kaevja's posting**: campaign says \"sanctum counterpart in E3\""), `:247`, `:249` (the arc-i timer lines)
- `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/03-vevette-blackwater.md:105`, `:121`, `:336` (the E3 sentence, the same text as `arc-i-kolat-towers.md:150`)
- `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/05-agorn-fuoco.md:126` (the sleeping room; see A3)
- `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/06-avareen-windrivver.md:318` and `07-zorbog-jyarkoth.md:261` (the K22 thugs line, `arc-i-kolat-towers.md:175`)

**Sources**
- `sources/adventure-wdh.json`: `:25` (Pronunciation Guide), `:173`-`:174` (pronunciation), `:26763` (capture offer), `:26847` (keys; Havia and Manshoon and Manafret), `:28156` (Sidra's ring), `:28200` (Manafret's ring), `:28822` (Teleporter Rings), `:29909`, `:29957`, `:29959`, `:29960`, `:29988` (E3 header), `:29992`, `:29993`, `:29994`, `:29998`, `:29999`, `:30002`, `:30183` (Havia and Mookie as "female lightfoot halflings"), `:30192`, `:30199` (E11 header), `:30212`, `:30215`, `:30220`, `:30223` (Havia's comb), `:32215`, `:32216`, `:32217`, `:3922` (Esloon Bezant; Kossuth page)
- `sources/SOURCE_GUIDE.md:35` (see E1)
- `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed pp. 94, 95, 96 (see B, D2, D3, D4)

---

## Not found

Searches and what they returned.

- **Wiki (the Forgotten Realms Wiki bundles).** I searched every `sources/research/**/wiki*.txt` for `Kaevja|Havia|Quickknife|Cynavern|Mookie`, and for `Red Wizard of Thay|Zhent Martial|martial arts adept`. No hit names Kaevja. The scratchpad extract `wiki-manshoons-zhentarim/11-kaevja-cynavern.txt` reads "NOT FOUND". The only Red Wizard line in the Zhentarim wiki is an enemies list: "*[[Red Wizards of Thay]]<ref name="LoD-p98" />" — `sources/research/pass5-bundles/zhentarim/wiki.txt:190` (the list is of the Zhentarim's enemies; edition not printed). Not about Kaevja.
- **Published adventure, names and pronunciations.** Searched `sources/adventure-wdh.json` for `Kaevja|Quickknife|Cynavern|Havia|Kaevia`. Hits are listed in Cross-references. No hit gives Kaevja a birthplace, age, family, faith or a first name.
- **Appendices and Act III.** `sources/Appendix_B_-_Player_Factions.md`, `Appendix_C_-_Player_Faction_Missions.md`, `Appendix_D_-_Running_the_Tavern.md` and `sources/Act_III_Arc_E.md`: no line names Kaevja. Act III Arc E mentions Kolat Towers only in general terms (`:291`, `:830`).
- **Factions Guide.** `campaign/guides/factions/10-manshoons-zhentarim.md` and `09-xanathars-guild.md`: no line names Kaevja.
- **Gazetteer and locations.** `campaign/gazetteer/waterdeep/` and `campaign/locations/`: no line names Kaevja.
- **Quest journals.** `campaign/quests/`: no line names Kaevja. (The Lords' Alliance Red Wizard quest concerns Esloon Bezant, a different Red Wizard.)
- **Kolat Towers quest journal.** None exists. `arc-i-kolat-towers.md` is the structure doc and is pending conversion.
- **SOURCE_GUIDE.** No line names Kaevja. Line 35 lists the Chapter 8 "Contains" without her (E1).
- **Pronunciation for Havia and Mookie.** Not in the Pronunciation Guide.
- **Rank title, date of joining, age, height, injuries, home city.** None.

## Not readable

- `sources/12. Lair  Zhentarim – Kolat Towers.pdf`: read as rendered images (PDF pages 3, 4 and 5, printed pp. 94 to 96). No `pdftotext` in this session. Every Alexandrian quote above is a transcription and needs a `pdftotext -layout` check before prose use.
- `sources/Other remix files/*.docx`: not opened. The only `.docx` line in `sources/SOURCE_GUIDE.md` that matches `Zhentarim` is `:688` (a Davil Starsong and Doom Raiders file, listed for the Doom Raiders organization page). The Chapter 8 Kolat row (`:35`) names no `.docx`. Not expected to cover Kaevja.

## Not run
- `voicecheck.py` was not run (research only).
- No file was edited except this notes file. The page was not written.
