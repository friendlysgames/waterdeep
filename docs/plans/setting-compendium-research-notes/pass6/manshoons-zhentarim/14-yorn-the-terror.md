# Pass 6 research notes: Yorn the Terror

Page: `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 4, 15 to 17)
Organization page: `campaign/setting/organizations/09-manshoons-zhentarim.md`
Villains page: `campaign/setting/villains/manshoon.md` (no Yorn entry)
Voice profile: `.claude/skills/character-voices/voices/manshoons-zhentarim.md` (Yorn the Terror, lines 242 to 256)
Figure group: Manshoon's Zhentarim (the Splinter). Not a Doom Raiders figure (Two Zhentarims rule: `campaign/setting/villains/manshoon.md:19`).

Method and caveats:
- No shell. Campaign files, the adventure JSON and the wiki were searched with Read, Grep and Glob.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. Tags such as `{@creature ...}` are left as written.
- Alexandrian PDF: `sources/12. Lair  Zhentarim – Kolat Towers.pdf` (five pages, printed pp. 92 to 96, PDF pp. 1 to 5). Read as rendered images with the Read tool's `pages` parameter. Every PDF quote below is a transcription from the image and must be checked with `pdftotext -layout` before any prose use. The Alexandrian names Yorn on printed pp. 94 and 95 only.
- Wiki: NOT FOUND. Searched every `sources/research/**/wiki.txt` (Grep glob `*wiki*.txt`) for "Yorn the", "Terror" and "half-orc enforcer". No Yorn entry matched. The only "Yorn" hit in the wiki bundles is "Yornar" (a Mielikki item, `sources/research/pass2-bundles/mielikki/wiki.txt:251`), which is a different name. The scratchpad wiki extract `wiki-manshoons-zhentarim/14-yorn-the-terror.txt` also reads NOT FOUND.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## Summary of what the drafter must know

1. **Location conflict.** The page places him "stationed in the extradimensional sanctum" (line 25) and "stationed in Kolat Towers' extradimensional sanctum" (line 29). The published adventure places him in K7, the Reading Room on the second level of the Main Tower, and says "He has never visited Manshoon's extraplanar sanctum" (`sources/adventure-wdh.json:28320`, `:28328`, `:28348`). The Alexandrian places him in K7 too (printed p. 94). See D1.
2. **Stat block conflict.** The page says "Stat block: **Gladiator**." (line 5). The adventure says "a half-orc {@creature thug}" (`:28340`), and the Alexandrian says "half-orc thug, MM p. 350" (printed p. 95). A brief ruling says to keep Gladiator "unless the file already explains it" (`docs/plans/deities-user-rulings-brief.md:24`). No campaign file explains it. See D2.
3. **Behavior conflict.** The page says "He does not explain himself" (line 21) and "does not retreat" (line 23). The adventure says "he's happy to chat with them about the inhabitants and the layout of Kolat Towers" when he thinks the party is no threat, and "values his own well-being above all else" (`:28348`). See D3.
4. **Pronouns agree.** The page says `he/him` (line 5), and the adventure's pronouns for him are "He" (`:28345`, `:28348`).
5. **Quest-time mechanic.** Line 25 refers to "the reinforcement timer", which is a Kolat Towers quest mechanic (`campaign/structure/arc-i-kolat-towers.md:112`). Routed in C.
6. **Ring.** Only the Alexandrian gives him a teleporter ring (asterisk, printed p. 94). The adventure's K7 entry does not mention one. See D4.

---

## A. Background facts by theme

### A1. Origin, species, upbringing

The adventure gives species, language and a racial trait. No source gives a home, a clan or a childhood.

> "{@creature Yorn|wdh} is a half-orc {@creature thug}, with these changes:"
> — `sources/adventure-wdh.json:28340` (K7 "Zhent", page 150)

> "He has these racial traits: When reduced to 0 hit points, he drops to 1 hit point instead (but can't do this again until he finishes a long rest). He has darkvision out to a range of 60 feet. He speaks Common and Orc."
> — `sources/adventure-wdh.json:28345`

The page's origin and epithet lines are campaign text with no source (see F1 and F2):

> "Yorn should inspire dread disproportionate to any initial description — the epithet "the Terror" was not self-applied, and the people who gave it to him are professionals who know what they are talking about."
> — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:11` (Resonance)

> "A half-orc enforcer stationed in Kolat Towers' extradimensional sanctum. He does not introduce himself. The epithet "the Terror" was not self-applied, and the professionals who gave it to him knew what they were talking about."
> — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:29` (Overview)

Adventure, the only source for the name and epithet (name only; no origin):

> "{@creature Yorn|wdh} the Terror is reading a copy of {@book Volo's Guide to Monsters|vgm}, autographed on the title page by the author with an added note that reads, in Common: \"For {@creature Yorn|WDH}. I hope you find the orc chapter illuminating!\""
> — `sources/adventure-wdh.json:28339` (K7 "Zhent", page 150)

Alexandrian, the stat reference (printed p. 95, image transcription):

> "Yorn the Terror – half-orc thug, MM p. 350; see DH p. 150"
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 95 [PDF p. 4]

### A2. How he joined and rose

No source gives recruitment, rank or history. The campaign's own line on his role:

> "- **Capture and interrogation:** The cell takes prisoners and questions them at the Interrogation House, and Yorn the Terror is the asset it uses when a conversation has stopped working (**Yorn the Terror**). Manshoon prefers a prisoner to a corpse because a prisoner answers questions (**Manshoon**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:68` (Methods and Tactics)

Organization page, the sanctum role, the only place the page's "maintenance of fear" is sourced:

> "- **The sanctum:** Behind the towers lies an extradimensional sanctum in a finite demiplane, which the original Manshoon created and his clones all know. A teleporter ring and the circle in the towers are the way in (*Dragon Heist*, 5e). Kaevja Cynavern watches the entrance and is Manshoon's early-warning mechanism, Havia Quickknife and Mookie Plush keep his audience chamber, and Yorn the Terror is the enforcer who maintains the household's fear of its master (**Kaevja Cynavern**; **Havia Quickknife**; **Mookie Plush**; **Yorn the Terror**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:55`

Manshoon's page, the household list:

> "- **Kaevja Cynavern**, **Havia Quickknife**, **Mookie Plush**, **Manafret Cherryport** and **Yorn the Terror:** His household in Kolat Towers and the sanctum behind it. Kaevja watches the entrance, Havia and Mookie keep his audience chamber, Manafret cooks, and Yorn keeps the household afraid of its master."
> — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60`

### A3. Post and place

Adventure, the room and its features (keyed area K7, page 150):

> "K7. Reading Room"
> — `sources/adventure-wdh.json:28320`

> "This room contains the following features:"
> — `sources/adventure-wdh.json:28324`

> "A burly half-orc clad in black leather armor sits in an overstuffed chair in the northernmost corner of the room, reading a book."
> — `sources/adventure-wdh.json:28328` (the half-orc is not named in this line; the next Yorn line names him)

> "Mouthwatering scents rise from a staircase that curves down to the kitchen ({@area K3|3de})."
> — `sources/adventure-wdh.json:28330`

Level and access (K6, page 150):

> "Level 2 of the main tower has the following features:"
> — `sources/adventure-wdh.json:28281`

> "A stone landing with no railings has a door leading to {@area K7|3ea} and a stone spiral staircase descending to {@area K4|3e1}."
> — `sources/adventure-wdh.json:28285`

Adventure, the sanctum and its access (K7, page 150):

> "{@creature Yorn|wdh} values his own well-being above all else. He is initially indifferent toward intruders. If {@creature Yorn|WDH} believes the characters aren't a threat, he's happy to chat with them about the inhabitants and the layout of Kolat Towers. He has never visited {@creature Manshoon|WDH}'s extraplanar sanctum, but he does know that the teleportation circle in {@area K22|40b} is the way to get there."
> — `sources/adventure-wdh.json:28348`

Adventure, the combat draw (K7, page 150):

> "Combat in this area draws the attention of {@creature Manafret Cherryport|wdh} in {@area K3|3de}, who investigates."
> — `sources/adventure-wdh.json:28349`

Adventure, the sanctum alarm list (page 158). Yorn is not among the defenders:

> "{@creature Kaevja Cynavern|wdh} (see {@area E3|41b})"
> "The {@creature Manshoon simulacrum|wdh} (see {@area E7|420})"
> "Vevette Blackwater and Agorn Fuoco (see {@area E8|425})"
> "{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} (see {@area E10|42a})"
> — `sources/adventure-wdh.json:29957` to `:29960`

Alexandrian, the roster (printed p. 94, image transcription; the row band places him with K7):

> "Yorn the Terror*"
> "Area K7 – Reading Room"
> "* Has a teleporter signet ring."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 94 [PDF p. 3]

Alexandrian, the plans (printed p. 93, image transcription), which exclude K7 from the pre-renovation tower:

> "- Does not include areas K7, K8, K12, K13, or K14."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 93 [PDF p. 2]

Alexandrian, what the thugs know (printed p. 95, image transcription; Yorn is "half-orc thug" in both sources):

> "Thugs know the general layout of the tower:"
> "They've been told not to enter the Outer Tower or go above the third level of the Main Tower."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 95 [PDF p. 4]

Campaign, the sanctum placement (conflicts with the above; see D1):

> "Yorn is a Manshoon Splinter enforcer stationed in the extradimensional sanctum whose role in the organization is the maintenance of internal fear as much as the exercise of direct violence, and a threat that compounds significantly if encountered late in the operation when the reinforcement timer has already thinned the party's resources."
> — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:25` (Relationships)

### A4. Possessions and habits

Adventure, the book in the reading room (K7, page 150):

> "{@creature Yorn|wdh} the Terror is reading a copy of {@book Volo's Guide to Monsters|vgm}, autographed on the title page by the author with an added note that reads, in Common: \"For {@creature Yorn|WDH}. I hope you find the orc chapter illuminating!\""
> — `sources/adventure-wdh.json:28339`

Adventure, his coins and the toothpick (K7 "Treasure", page 150; the printed word is "taols"):

> "{@creature Yorn|wdh} carries 36 cp, 20 sp, 12 gp, 8 taols, and a gem-studded ivory toothpick (worth 25 gp) in a pouch."
> — `sources/adventure-wdh.json:28358`

Campaign, the gloves (no source):

> "- **Quirks:** He removes his gloves before he speaks."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:250`

### A5. Relationships to other named figures

- **Manshoon:** "He has never visited Manshoon's extraplanar sanctum" (`sources/adventure-wdh.json:28348`). The adventure says nothing else about Yorn and Manshoon.
- **Kaevja Cynavern, Havia Quickknife, Mookie Plush:** not named together with Yorn in any source. Yorn is absent from the sanctum alarm list (`:29957` to `:29960`).
- **Manafret Cherryport:** Combat in K7 "draws the attention of Manafret Cherryport in K3" (`:28349`).
- **Sidra Romeir's two thugs:** the adventure says "two subordinates (LE male Tethyrian human {@creature thug||thugs})" (`sources/adventure-wdh.json:28155`). These are Sidra's own, in K2. Yorn is a half-orc thug in K7, a separate entry. The campaign gives Yorn no tie to Sidra.
- **Lady Gondafrey, Urstul Floxin:** no link in any source.

### A6. Faith

No source gives Yorn a god. The Gruumsh page checked the half-orc Notable Figures for a named god and found none:

> "`campaign/setting/notable-figures/`: Sister Valdra, Yagra Stonefist, Ziraj the Hunter, Hrabbaz, Grevik Nass and Yorn the Terror, checked for faction labels, species and any named god."
> — `campaign/setting/deities/gruumsh.md:92`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
> "- *Half-orc enforcer, neutral evil, he/him*. Stat block: **Gladiator**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:5`

> "{@creature Yorn|WDH} is neutral evil."
> — `sources/adventure-wdh.json:28344` (K7 "Zhent" list)

> "- **Yorn the Terror** — Half-orc enforcer, neutral evil; see the **Yorn the Terror** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:109`

Alignment agrees across all three.

**Species**
> "- *Half-orc enforcer, neutral evil, he/him*. Stat block: **Gladiator**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:5`

> "{@creature Yorn|wdh} is a half-orc {@creature thug}, with these changes:"
> — `sources/adventure-wdh.json:28340`

> "Yorn the Terror – half-orc thug, MM p. 350; see DH p. 150"
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 95 [PDF p. 4]

**Pronouns**

Page:
> "- *Half-orc enforcer, neutral evil, he/him*. Stat block: **Gladiator**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:5` (no source tag)

Adventure (no gender noun; the pronoun is "He" throughout the entry):
> "He has these racial traits: When reduced to 0 hit points, he drops to 1 hit point instead..."
> — `sources/adventure-wdh.json:28345` ("He" as printed; the sentence continues "...He speaks Common and Orc." as quoted in A1)

> "{@creature Yorn|wdh} values his own well-being above all else. He is initially indifferent toward intruders."
> — `sources/adventure-wdh.json:28348`

Alexandrian: no gender printed for Yorn (printed p. 95, "Yorn the Terror – half-orc thug").

Voice profile: "Sound: A low, flat, patient voice, rarely heard." (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:245`). No pronoun there.

Pronoun table, the prior check (it rests on the page's own prose, not a source):
> "| Yorn the Terror | manshoons-zhentarim/14-yorn-the-terror.md:5 | he/him | prose ("the people who gave it to him", "he uses his physicality as a weapon") | High |"
> — `docs/plans/npc-pronouns-table-group-c.md:58`

**Stat block**

Page:
> "- *Half-orc enforcer, neutral evil, he/him*. Stat block: **Gladiator**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:5`

Adventure:
> "{@creature Yorn|wdh} is a half-orc {@creature thug}, with these changes:"
> — `sources/adventure-wdh.json:28340` (the changes are the racial trait at `:28345`, quoted in A1)

Alexandrian:
> "Yorn the Terror – half-orc thug, MM p. 350; see DH p. 150"
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 95 [PDF p. 4]

Brief ruling on the label (not a source):
> "20. **Yorn the Terror.** Dragon Heist prints him as a half-orc thug, neutral evil (adventure-wdh.json:28339-28348). The page says "Human enforcer". No design reason: make him a half-orc in 14-yorn-the-terror.md, arc-i-kolat-towers.md, 09-manshoons-zhentarim.md, and the mielikki.md and gruumsh.md mentions if they say otherwise. Keep the Gladiator stat block unless the file already explains it."
> — `docs/plans/deities-user-rulings-brief.md:24`

Gladiator appears only on the page (line 5) and in the Gruumsh page's restatement (`campaign/setting/deities/gruumsh.md:124`). No source gives it.

---

## C. Sentences that narrate a quest event or a day-one conflict

The page narrates no capture, rescue, death, mission or "once the party" event. The voice profile (lines 242 to 256) has no quest-time clause. The rows below are the lines a reader could take as an event or a mechanic.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L21 | "To Manshoon's lieutenants, he is the asset deployed when a situation has moved past the point at which conversation is the primary tool." | Day-one; sourced in part | `campaign/setting/organizations/09-manshoons-zhentarim.md:68` |
| 2 | L21 | "To the world — specifically to anyone brought into the sanctum who is about to be questioned — Yorn the Terror is the fact of what is going to happen." | Day-one role; the location clause conflicts with the Interrogation House in the organization page (D1 and D5) | `organizations/09-manshoons-zhentarim.md:68` |
| 3 | L23 | "a party that attempts to escape will discover that the corridor behind them has become a different kind of problem." | Play note; no event | none needed |
| 4 | L23 | "a party that can match his damage output can defeat him" | Play note; no event | none needed |
| 5 | L25 | "...a threat that compounds significantly if encountered late in the operation when the reinforcement timer has already thinned the party's resources." | Quest mechanic. The reinforcement timer is a Kolat Towers mechanic, not a day-one fact | `campaign/structure/arc-i-kolat-towers.md:112`, `:180` (see below) |

Routed mechanic, the timer (Kolat Towers, pending conversion):
> "Once combat begins in the towers, the reinforcement timer starts, and the primary strategic variable becomes speed."
> — `campaign/structure/arc-i-kolat-towers.md:112`

> "| 30 min | External reinforcements — Agorn's team or replacement spy + 4 thugs — arrive at the perimeter with fresh pass-amulets. The party is fighting the entire remaining Splinter cell. |"
> — `campaign/structure/arc-i-kolat-towers.md:180`

The Yorn page's own "reinforcement timer" wording is the only place Yorn meets this mechanic. No file ties Yorn to the timer.

---

## D. Conflicts

**D1. Location: sanctum against the Kolat Towers reading room**
- Page: "Yorn is a Manshoon Splinter enforcer stationed in the extradimensional sanctum" — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:25`; "A half-orc enforcer stationed in Kolat Towers' extradimensional sanctum." — `:29`
- Organization page: "and Yorn the Terror is the enforcer who maintains the household's fear of its master" under "The sanctum:" — `campaign/setting/organizations/09-manshoons-zhentarim.md:55`
- Adventure: "{@creature Yorn|wdh} is a half-orc {@creature thug}" in K7, the reading room (`sources/adventure-wdh.json:28320` to `:28340`); "He has never visited {@creature Manshoon|WDH}'s extraplanar sanctum" (`:28348`); not in the sanctum alarm list (`:29957` to `:29960`).
- Alexandrian: "Area K7 – Reading Room" in the same row band as "Yorn the Terror*" (printed p. 94).
- Campaign structure document: no Yorn entry in `campaign/structure/arc-i-kolat-towers.md`; line 320 only says "New profiles needed: Kaevja Cynavern, Havia Quickknife, Mookie Plush, Yorn the Terror."
- Higher source: the campaign outranks the adventure, but the campaign's sanctum placement has no source. The orchestrator decides. The adventure's K7 placement and the Alexandrian's agree with each other.

**D2. Stat block: "Gladiator" against "thug"**
- Page: "Stat block: **Gladiator**." — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:5`
- Adventure: "{@creature Yorn|wdh} is a half-orc {@creature thug}, with these changes:" — `sources/adventure-wdh.json:28340`
- Alexandrian: "Yorn the Terror – half-orc thug, MM p. 350; see DH p. 150" (printed p. 95)
- Brief ruling: "Keep the Gladiator stat block unless the file already explains it." (`docs/plans/deities-user-rulings-brief.md:24`). No campaign file explains it.

**D3. Behavior: "does not explain himself" and "does not retreat" against the adventure**
- Page: "He does not monologue. He does not explain himself." — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:21`
- Voice profile: "Never: He never explains himself, never hurries, and never gloats." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:252`
- Adventure: "If {@creature Yorn|WDH} believes the characters aren't a threat, he's happy to chat with them about the inhabitants and the layout of Kolat Towers." — `sources/adventure-wdh.json:28348`
- Page: "Yorn does not retreat and does not stop." — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:23`
- Adventure: "{@creature Yorn|wdh} values his own well-being above all else." — `sources/adventure-wdh.json:28348`
- The adventure's lines are about how he acts before any fight. The page's lines are about combat. They can both hold; the orchestrator decides how far the page follows the adventure.

**D4. Teleporter ring**
- Alexandrian, printed p. 94: "Yorn the Terror*" with "* Has a teleporter signet ring." (`sources/12. Lair  Zhentarim – Kolat Towers.pdf`)
- Adventure, K7 entry (`sources/adventure-wdh.json:28339` to `:28358`): no ring. The adventure gives rings to Havia and Mookie (`:30192`) and to Sidra (`:28156`: "Sidra wears a {@item teleporter ring|WDH} (see \"Teleporter Rings\").").
- Campaign: silent on Yorn; "his brass teleporter rings ... go only to his most trusted servants" (`campaign/setting/organizations/09-manshoons-zhentarim.md:41`).

**D5. Where he is questioned (campaign-internal)**
- Organization page: "The cell takes prisoners and questions them at the Interrogation House, and Yorn the Terror is the asset it uses" (`campaign/setting/organizations/09-manshoons-zhentarim.md:68`).
- Yorn's page: "anyone brought into the sanctum who is about to be questioned" (`campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:21`).
- The two campaign lines place the questioning in different buildings. The Interrogation House is in the North Ward (`campaign/setting/organizations/09-manshoons-zhentarim.md:53`, `:57`).

**D6. Old version: "human"** (stale, not a current conflict)
- `docs/plans/deities-user-rulings-brief.md:24`: 'The page says "Human enforcer".'
- `sources/research/pass4-bundles/manshoon/campaign-hits.txt:819`: "The campaign's Notable Figure makes him human (see Draft Notes)". This is a snapshot of an older `gruumsh.md` line.
- Current file: "The campaign's Notable Figure makes him a half-orc as well, so the book fits the Kolat Towers room." (`campaign/setting/deities/gruumsh.md:74`).

---

## E. Stale lines in other files, and routed references

Stale (not edited):
- `campaign/setting/deities/gruumsh.md:124`: "`campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:6` now makes him a half-orc enforcer with the Gladiator stat block." The summary line is line 5, not 6. Line citation drift.
- `campaign/structure/arc-i-kolat-towers.md:320`: "New profiles needed: Kaevja Cynavern, Havia Quickknife, Mookie Plush, Yorn the Terror." The Yorn profile exists, so this line is out of date.
- `docs/plans/npc-pronouns-table-group-c.md:58`: "| Yorn the Terror | manshoons-zhentarim/14-yorn-the-terror.md:5 | he/him | prose (...) | High |". Its "High" rests on the page's prose.
- `docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:134` quotes the summary line as "Stat block: **Gladiator**." (the pass 5 check). That check is out of date on the stat block but not on the label.

Routed (quest pending conversion):
- `campaign/structure/arc-i-kolat-towers.md:112` (raid scope; the reinforcement timer line is at `:112`).
- `campaign/structure/arc-i-kolat-towers.md:180` (the 30-minute row).
- `campaign/structure/arc-i-kolat-towers.md:320` and `:321` (Notable Figures and Bestiary notes; `:321` reads "Standard stat blocks needed: Havia Quickknife, Mookie Plush.").

Other pages that name him (read, not edited):
- `campaign/setting/organizations/09-manshoons-zhentarim.md:55`, `:68`, `:109` (quoted above).
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60` (quoted in A2).
- `campaign/setting/deities/gruumsh.md:74`, `:89`, `:92`, `:111`, `:114`, `:124` (the half-orc list and the Yorn settlement).
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:147` (cross-reference list).

---

## F. Gaps: what a Background needs that no source gives

For each gap: the sourced facts the drafter must stay consistent with.

**F1. Birth, clan or tribe, childhood, home, age.** No source. Consistent facts: "half-orc" (`sources/adventure-wdh.json:28340`); "He speaks Common and Orc." (`:28345`). The Volo's gift "For Yorn. I hope you find the orc chapter illuminating!" (`:28339`) is a note from an unnamed author; the adventure names no sender.

**F2. The epithet "the Terror".** Who gave it, when and why: none. The adventure uses only the name, "Yorn the Terror" (`:28339`). The page's "not self-applied" and "the professionals who gave it to him" (lines 11 and 29) have no source. Do not give the epithet an origin story that contradicts "the Terror" as a name the adventure uses.

**F3. The "Gladiator" career.** No source. The stat block label is the only trace (page line 5; `docs/plans/deities-user-rulings-brief.md:24`). The adventure gives him the thug block with a racial trait (`:28340`, `:28345`).

**F4. How he joined Manshoon, his rank and tenure.** None. The only role lines are the organization page's (`campaign/setting/organizations/09-manshoons-zhentarim.md:55`, `:68`) and the Manshoon page's household list (`campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60`).

**F5. Whether he has ever entered the sanctum.** Sourced: "He has never visited Manshoon's extraplanar sanctum, but he does know that the teleportation circle in K22 is the way to get there" (`sources/adventure-wdh.json:28348`). This is the adventure's position, and it conflicts with the page (D1).

**F6. Gloves.** No source. The voice profile's "He removes his gloves before he speaks" (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:250`) is campaign text.

**F7. Religion.** None. Consistent: "checked for ... any named god" (`campaign/setting/deities/gruumsh.md:92`). Do not name a god without a source.

**F8. The teleporter ring.** Only the Alexandrian gives one (D4). Do not state that he carries one without resolving D4.

**F9. Who sent the book and why.** The adventure names no sender ("the author" of Volo's Guide to Monsters, `sources/adventure-wdh.json:28339`). Whether the author is a known figure is not stated.

**F10. Age, first day in post, lifespan.** None.

**F11. Fear and the household.** The sourced role is "the maintenance of internal fear" (`campaign/setting/organizations/09-manshoons-zhentarim.md:55`) and "keeps the household afraid of its master" (`campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60`). The reason he does it, and what he feels about it, are open.

---

## G. Inner-life hints (sourced)

Each line is an exact quote. Use these for the Background and Personal goals (brief ruling 17). Do not contradict them.

**G1. He values himself above the job.**
> "{@creature Yorn|wdh} values his own well-being above all else. He is initially indifferent toward intruders. If {@creature Yorn|WDH} believes the characters aren't a threat, he's happy to chat with them about the inhabitants and the layout of Kolat Towers. He has never visited {@creature Manshoon|WDH}'s extraplanar sanctum, but he does know that the teleportation circle in {@area K22|40b} is the way to get there."
> — `sources/adventure-wdh.json:28348`

**G2. A gift he keeps.**
> "{@creature Yorn|wdh} the Terror is reading a copy of {@book Volo's Guide to Monsters|vgm}, autographed on the title page by the author with an added note that reads, in Common: \"For {@creature Yorn|WDH}. I hope you find the orc chapter illuminating!\""
> — `sources/adventure-wdh.json:28339`

**G3. Small things he carries.**
> "{@creature Yorn|wdh} carries 36 cp, 20 sp, 12 gp, 8 taols, and a gem-studded ivory toothpick (worth 25 gp) in a pouch."
> — `sources/adventure-wdh.json:28358`

**G4. The reading room is his.** The adventure places him in a comfortable room with "Large framed pictures of cities and landscapes", "a worn, blood-spattered rug", "a pair of rocking chairs, a couch, and an ottoman" (`sources/adventure-wdh.json:28329`). The blood on the rug is in the source.
> "Large framed pictures of cities and landscapes hang on the walls, and a worn, blood-spattered rug covers the floor. Other furnishings include a pair of rocking chairs, a couch, and an ottoman."
> — `sources/adventure-wdh.json:28329`

**G5. Campaign-only inner-life lines (no source; they must not be contradicted).**
> "Yorn most often feels steady patience, a physical readiness he carries the way other people carry stillness, satisfaction in his particular utility to Manshoon's operation, and a focused clarity that descends once he understands a situation is no longer going to be avoided."
> — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:13` (Emotions)

> "Yorn wants to do the work Manshoon brought him in for — enforcement, extraction, the maintenance of internal fear as much as external threat — and to do it well enough that his value is never questioned."
> — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:15` (Motivations)

> "Deep down, he has been called "the Terror" long enough that he has stopped thinking of it as a name and started thinking of it as a description."
> — `campaign/setting/notable-figures/manshoons-zhentarim/14-yorn-the-terror.md:21` (Persona)

> "Steady patience and focused clarity once talk has failed. His silence is the terror."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:249` (Personality in speech)

---

## Not readable

- None of the sources failed to open. The Alexandrian PDF was read as rendered images and must be checked with `pdftotext -layout`.
- `sources/Other remix files/*.docx` were not searched; `SOURCE_GUIDE.md` does not name one for this figure.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
