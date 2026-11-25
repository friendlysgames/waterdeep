# Pass 6 research notes: Mookie Plush

Page: `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 4, 15 to 17)
Organization page: `campaign/setting/organizations/09-manshoons-zhentarim.md`
Villains page: `campaign/setting/villains/manshoon.md` (no Mookie entry)
Voice profile: `.claude/skills/character-voices/voices/manshoons-zhentarim.md` (Mookie Plush, lines 224 to 234)
Figure group: Manshoon's Zhentarim (the Splinter). Not a Doom Raiders figure (Two Zhentarims rule: `campaign/setting/villains/manshoon.md:19`).

Method and caveats:
- No shell. Campaign files, the adventure JSON and the wiki were searched with Read, Grep and Glob.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. Tags such as `{@creature ...}` are left as written.
- Alexandrian PDF: `sources/12. Lair  Zhentarim – Kolat Towers.pdf` (five pages, printed pp. 92 to 96, PDF pp. 1 to 5). Read as rendered images with the Read tool's `pages` parameter. Every PDF quote below is a transcription from the image and must be checked with `pdftotext -layout` before any prose use. This PDF is the only Alexandrian source for Mookie. `sources/Appendix_B_-_Player_Factions.md`, `Appendix_C_-_Player_Faction_Missions.md` and the `Act_III` files were searched and do not name him.
- Wiki: NOT FOUND. Searched every `sources/research/**/wiki.txt` (Grep glob `*wiki*.txt`) for "Mookie", "Plush", "Havia", "Quickknife" and "Zhent Martial". Zero files matched. The scratchpad wiki extract `wiki-manshoons-zhentarim/13-mookie-plush.txt` also reads NOT FOUND.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## Summary of what the drafter must know

1. **Pronoun conflict.** The page says `he/him` (line 5). The published adventure's only gendered line for him reads "Two female lightfoot halflings", naming Havia and Mookie together (`sources/adventure-wdh.json:30183`). The brief says pronouns come from the page or the source and are never inferred (ruling 4), so this is left for the orchestrator. See D1.
2. **E10 is sourced.** Mookie and Havia keep the sanctum's Audience Chamber, E10 (`sources/adventure-wdh.json:30164`, `:30183`, `:29960`, `:30212`; Alexandrian p. 94).
3. **Stat block.** The adventure gives "martial arts adepts" (VGM) with 49 hit points (`:30183`, `:30188`). The page's label "Adept" matches Havia's page.
4. **No quest-time sentence** appears on the page. The page's one death line (line 25) is a conditional play note.
5. **Sourced personal object.** A tiny halfling doll with five 100 gp pearls is in the chest the adventure lists as "Mookie's chest" (`:30224`). See G1.

---

## A. Background facts by theme

### A1. Origin, family, hometown, age

No source gives any of these. The page's only origin line is campaign text with no source (see F1 and F2).

> "**Persona.** To the world, Mookie Plush is the friendlier of the two halflings in the audience chamber — he smiles easily, seems genuinely interested in who the party is, and gives a distinct impression that he would rather this did not have to happen. To anyone who probes this affect, it does not crack because there is nothing beneath it to crack: he is genuinely warm, genuinely loyal, and genuinely willing to kill everyone in the room. Deep down, he found what he was looking for when Manshoon offered him a place, and the finding resolved him completely."
> — `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:21` (Persona; the "Deep down" clause has no source)

Voice profile, on asking about hometowns (campaign, no source):

> "- **Quirks:** He asks people's names and hometowns. He apologises while fighting."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:232`

### A2. How he joined and rose

Adventure, the two halflings as a pair and their loyalty:

> "Two female lightfoot halflings—{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush}—believe that {@creature Manshoon|WDH} is the rightful leader of the Zhentarim. They serve him fearlessly, and will sacrifice themselves to ensure that his plans come to fruition. They are {@creature martial arts adept|VGM|martial arts adepts} (see {@adventure appendix B|WDH|12}), with these changes:"
> — `sources/adventure-wdh.json:30183` (keyed area E10, "Zhents", page 160; the E10 heading is at `:30164`)

Adventure, the teleporter rings they carry:

> "Havia and Mookie each wear a {@item teleporter ring|WDH} (see \"Teleporter Rings\")."
> — `sources/adventure-wdh.json:30192` (E10, same entry)

Organization page, the same loyalty, with the published source named:

> "- **One True Manshoon:** Every surviving clone claims to be the one true Manshoon, and this one holds the belief with absolute certainty. Loyalty to him runs from devotion to calculation. Havia Quickknife and Mookie Plush serve him completely, and Kaevja Cynavern serves him because he is the most capable operator she has met. Agorn Fuoco would trade whatever he knows to save himself. The published adventure says Havia and Mookie hold that Manshoon is the rightful leader of the Zhentarim and will sacrifice themselves to see his plans succeed (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:43` (Beliefs)

No source says how or when either halfling joined. The adventure gives no recruitment or training history.

### A3. Post and place

Adventure, the room (keyed area E10, page 159):

> "E10. Audience Chamber"
> — `sources/adventure-wdh.json:30164`

> "High-ranking Zhents who desire an audience with {@creature Manshoon|WDH} come here. The room contains the following features:"
> — `sources/adventure-wdh.json:30168`

> "If they haven't been drawn elsewhere, two of {@creature Manshoon|WDH}'s followers are sparring and engaged in mock fisticuffs atop the table."
> — `sources/adventure-wdh.json:30174` (the two followers are not named in this line)

Organization page, the post:

> "- **The sanctum:** Behind the towers lies an extradimensional sanctum in a finite demiplane, which the original Manshoon created and his clones all know. A teleporter ring and the circle in the towers are the way in (*Dragon Heist*, 5e). Kaevja Cynavern watches the entrance and is Manshoon's early-warning mechanism, Havia Quickknife and Mookie Plush keep his audience chamber, and Yorn the Terror is the enforcer who maintains the household's fear of its master (**Kaevja Cynavern**; **Havia Quickknife**; **Mookie Plush**; **Yorn the Terror**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:55`

Alexandrian, the roster (printed p. 94, image transcription; the row band places him with E10):

> "Havia Quickknife* + Mookie Plush*"
> "Area E10 – Audience Chamber"
> "* Has a teleporter signet ring."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 94 [PDF p. 3]

Alexandrian, the room (printed p. 94, image transcription):

> "Area E10 – Audience Chamber: This room is lit by a sunglobe which levitates in midair near the ceiling. (On command, a sunglobe glows with the light of the sun itself. It can be commanded to maintain its current position, levitating in mid-air until grasped.)"
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 94 [PDF p. 3]

Alarm role (sanctum alarm, page 158):

> "{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} (see {@area E10|42a})"
> — `sources/adventure-wdh.json:29960` (the list of defenders the sanctum alarm brings; the alarm is at `:29953`)

### A4. Sleeping place and chest

Adventure, E11 (page 160):

> "{@creature Kaevja Cynavern|wdh}, Vevette Blackwater, Agorn Fuoco, {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife}, and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} all sleep here."
> — `sources/adventure-wdh.json:30212` (E11 "Zhent Quarters"; the beds and chests are listed at `:30207` and `:30208`)

> "Mookie's chest contains a tiny halfling doll. Stuffed inside the doll is a pouch that holds five 100 gp pearls."
> — `sources/adventure-wdh.json:30224` (E11 "Treasure", page 160)

Alexandrian, printed p. 96 (lieutenant knowledge, image transcription; it does not name Mookie):

> "Manshoon's lieutenants know what the apprentice wizards know, but also:"
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 96 [PDF p. 5]

Whether a household adept counts as a lieutenant is not stated in any source.

### A5. Relationships to other named figures

- **Havia Quickknife:** paired in E10 (`campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:25`), in the adventure's pair entry (`sources/adventure-wdh.json:30183`) and in the E11 sleeping list (`:30212`). Havia's own page says "She and Mookie do not coordinate tactically — they simply both move toward the threat simultaneously" (`campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:23`). That line is campaign text.
- **Manshoon:** "They serve him fearlessly" (`sources/adventure-wdh.json:30183`).
- **Kaevja Cynavern, Vevette Blackwater, Agorn Fuoco:** share E11 (`:30212`). Kaevja holds the sanctum's entrance watch (`campaign/setting/organizations/09-manshoons-zhentarim.md:55`).
- **Sidra Romeir:** not named for Mookie in any source. Sidra's page names Manafret, Kaevja and her two unnamed thugs (`campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:39` to `:41`).

### A6. Faith

No source gives Mookie a god. The Yondalla page says so for him by name:

> "No Notable Figure names Yondalla. The halflings among them are **Broxley Fairkettle**, **Osco Salibuck**, **Kelso Fiddlewick**, **Corene Wyldath**, **Manafret Cherryport**, **Havia Quickknife** and **Mookie Plush**, and none of their pages gives a god, so this page makes none of them a worshiper."
> — `campaign/setting/deities/yondalla.md:65` (a blockquote bullet; the text after the marker is quoted)

---

## B. Alignment, species, pronouns, stat block

**Alignment**
> "- *Lightfoot halfling adept, lawful evil, he/him*. Stat block: **Adept**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:5`

> "Havia and Mookie are lawful evil."
> — `sources/adventure-wdh.json:30187` (E10 list)

> "- **Mookie Plush** — Lightfoot halfling adept, lawful evil; see the **Mookie Plush** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:108`

> "Havia Quickknife / Mookie Plush (LE lightfoot halfling) – martial arts adepts, DH p. 209"
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 95 [PDF p. 4] (image transcription)

Alignment agrees across all four sources.

**Species**
> "Two female lightfoot halflings—..." (the full line is quoted in A2)
> — `sources/adventure-wdh.json:30183` (species is "lightfoot halfling"; "female" is discussed under pronouns)

> "They have these racial traits: They are Small, and their walking speed is 25 feet. They can move through the space of a Medium or larger creature. They have advantage on saving throws against being {@condition frightened}. They speak Common and Halfling."
> — `sources/adventure-wdh.json:30189` (E10 list)

**Pronouns**

Page:
> "- *Lightfoot halfling adept, lawful evil, he/him*. Stat block: **Adept**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:5` (no source tag)

Adventure (the only gendered line for him):
> "Two female lightfoot halflings—{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush}—believe that..."
> — `sources/adventure-wdh.json:30183` (the word "female" applies to both halflings named in the sentence)

Adventure, the sanctum's other female NPC, stated explicitly (for contrast):
> "{@creature Kaevja Cynavern|wdh} is a female Mulan human {@creature mage}, with these changes:"
> — `sources/adventure-wdh.json:29994` (E3 "Guard Station")

Alexandrian, printed p. 95 (image transcription; no gender printed for Havia or Mookie, though Sidra and Kaevja are marked female):
> "Sidra Romeir (LE female Callishite human) – veteran, MM p. 350"
> "Kaevja Cynavern (female Mulan human) – mage, MM p. 347; see DH p. 158"
> "Havia Quickknife / Mookie Plush (LE lightfoot halfling) – martial arts adepts, DH p. 209"
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 95 [PDF p. 4]

Voice profile (campaign; he/him throughout):
> "- **Word choice:** Warm and casual: "friend", "aw", "sorry about this". He calls Manshoon "the boss" fondly."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:229`

Pronoun table, the prior check (it rests on the page's own prose, not on a source):
> "| Mookie Plush | manshoons-zhentarim/13-mookie-plush.md:5 | he/him | prose ("he has the approachable affect", "His warmth is not a tactic") | High |"
> — `docs/plans/npc-pronouns-table-group-c.md:57`

**Stat block**

Page:
> "- *Lightfoot halfling adept, lawful evil, he/him*. Stat block: **Adept**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:5`

Adventure:
> "They are {@creature martial arts adept|VGM|martial arts adepts} (see {@adventure appendix B|WDH|12}), with these changes:"
> — `sources/adventure-wdh.json:30183`

> "They have 49 ({@dice 11d6 + 11}) hit points each."
> — `sources/adventure-wdh.json:30188`

Alexandrian: "martial arts adepts, DH p. 209" (`sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 95; quoted in full above).

Havia's page uses the same label:
> "- *Lightfoot halfling adept, lawful evil, she/her*. Stat block: **Adept**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:5`

Standard stat block is still not drafted:
> "- **the Bestiary (not yet drafted)** — Boss stat block needed: Manshoon (with simulacrum mechanic distinction). Standard stat blocks needed: Havia Quickknife, Mookie Plush."
> — `campaign/structure/arc-i-kolat-towers.md:321`

---

## C. Sentences that narrate a quest event or a day-one conflict

The page narrates no capture, rescue, death, mission or "once the party" event. The voice profile (lines 224 to 234) has no quest-time clause. The rows below are the lines a reader could take as an event.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L11 | "...then immediate revision, because the warmth does not change the outcome." | Play note; no event | none needed |
| 2 | L21 | "Deep down, he found what he was looking for when Manshoon offered him a place, and the finding resolved him completely." | Backstory with no source; not a quest event. Needs F2 | none (campaign text only) |
| 3 | L23 | "Mookie fights to death, like Havia, but with a quality of sad inevitability..." | Combat conduct; sourced in part | `sources/adventure-wdh.json:30183` ("will sacrifice themselves to ensure that his plans come to fruition") |
| 4 | L25 | "...the sort of NPC whose death, if the party pauses on it, feels like waste rather than victory." | Conditional play note. Names no death event; drafter decides whether it stays | none (campaign text only) |

The Kolat Towers quest structure names E10 and the pair, and gives them combat behavior. Routed reference only:
> "**E10 — Audience Chamber.** Havia Quickknife + Mookie Plush, two halfling adepts who serve as Manshoon's household fanatics. Both fight to death. They are the sanctum's most physically capable non-spellcasting combatants — trained in martial arts, faster than their size suggests, and entirely loyal. They are also the least tactically sophisticated opponents in the sanctum; they attack in a straight line and do not retreat."
> — `campaign/structure/arc-i-kolat-towers.md:160` (Kolat Towers is a quest pending conversion; its structure document is authoritative until the journal exists)

---

## D. Conflicts

**D1. Pronouns: he/him against "female"**
- Page: "*Lightfoot halfling adept, lawful evil, he/him*." — `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:5`
- Adventure: "Two female lightfoot halflings—{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush}—..." — `sources/adventure-wdh.json:30183`
- Havia's page, the same pair: "*Lightfoot halfling adept, lawful evil, she/her*." — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:5`
- Alexandrian: no gender printed for either halfling (`sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 95).
- Voice profile: he/him throughout (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:227` to `:234`).
- The brief's rule (ruling 4) is that pronouns come from the existing page or the source. Both exist and disagree. Rank: the campaign outranks the adventure, but the page's he/him carries no source tag, and the pronoun table's "High" rests only on the page's prose (`docs/plans/npc-pronouns-table-group-c.md:57`). No campaign file gives a reason for he/him. The orchestrator must choose.

**D2. Stat block label**
- Page and Havia's page: "Adept". Adventure: "martial arts adepts" (VGM). Alexandrian: "martial arts adepts, DH p. 209". Naming only; not a substantive conflict.

**D3. Location**
- Page L25 "in E10"; adventure `:30164` and `:30183`; Alexandrian p. 94 row band. All agree.

**D4. Havia's page against this page**
- Havia's page: "She fights to death." (`campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:23`). Mookie's page: "Mookie fights to death, like Havia" (line 23). Agree.
- Ring: the adventure says both wear one (`:30192`). Havia's page does not mention a ring. Not a conflict; a gap on Havia's side.

---

## E. Stale lines in other files, and routed references

Stale (not edited):
- `docs/plans/npc-pronouns-table-group-c.md:57`: "| Mookie Plush | manshoons-zhentarim/13-mookie-plush.md:5 | he/him | prose (...) | High |". Its "High" rests on the page's own prose.
- `campaign/structure/arc-i-kolat-towers.md:320`: "- **Notable Figures** — Existing profiles: Manshoon, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin, Lady Gondafrey, Skeemo Weirdbottle. New profiles needed: Kaevja Cynavern, Havia Quickknife, Mookie Plush, Yorn the Terror." The Mookie profile now exists, so this line is out of date.

Routed (where the Kolat Towers facts live; quest pending conversion):
- `campaign/structure/arc-i-kolat-towers.md:112` (raid scope: "Full operational content for both locations: Kolat Towers (K-series areas) and the extradimensional sanctum (E-series areas).").
- `campaign/structure/arc-i-kolat-towers.md:160` (E10, quoted in C).
- `sources/adventure-wdh.json:29960` (the sanctum alarm list, see A3).

Other pages that name him (read, not edited):
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60` ("**Kaevja Cynavern**, **Havia Quickknife**, **Mookie Plush**, **Manafret Cherryport** and **Yorn the Terror:** His household in Kolat Towers and the sanctum behind it. Kaevja watches the entrance, Havia and Mookie keep his audience chamber, Manafret cooks, and Yorn keeps the household afraid of its master.")
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:147` (cross-reference list).
- `campaign/setting/deities/yondalla.md:65` and `:105` (no god; quoted in A6).

---

## F. Gaps: what a Background needs that no source gives

For each gap: the sourced facts the drafter must stay consistent with.

**F1. Birth, family, hometown, age, early life.** No source. Consistent facts: "Two female lightfoot halflings" (`sources/adventure-wdh.json:30183`) (see D1); "*Lightfoot halfling adept*" (page line 5); "They speak Common and Halfling." (`:30189`). The voice profile's "He asks people's names and hometowns" (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:232`) is a habit, not a home.

**F2. How he came to Manshoon, and "offered a place".** Only the page's own line 21 sentence (quoted in A1) says so. No source gives a recruiter, date or circumstance. Consistent facts: the pair "believe that Manshoon is the rightful leader of the Zhentarim" (`:30183`); Havia's page gives her arrival as "she arrived in the sanctum because she had nowhere else she wanted to be" (`campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:21`). The drafter should not give Mookie a near-identical arrival line.

**F3. Training and martial background.** The sourced line is "trained in martial arts, faster than their size suggests" (`campaign/structure/arc-i-kolat-towers.md:160`). Where he trained, under whom and for how long: none.

**F4. Tenure, rank and promotion.** None. No source places him on a ladder. The campaign names him only among the "household fanatics" (`arc-i-kolat-towers.md:160`) and the audience-chamber keepers (`organizations/09-manshoons-zhentarim.md:55`).

**F5. Relationship with Havia beyond the pairing.** Sourced: paired in E10 (`:30183`), shared E11 (`:30212`), "do not coordinate tactically" (Havia's page line 23). Anything closer is open.

**F6. Whose doll.** The adventure says "Mookie's chest contains a tiny halfling doll" (`:30224`), which fixes the chest to him but not the doll's history. Consistent: Havia's chest holds "a golden comb shaped like a stylized dragon with tiny rubies for eyes" (`:30223`).

**F7. Faith.** None. Consistent: "none of their pages gives a god" (`campaign/setting/deities/yondalla.md:65`). Do not name a god without a source.

**F8. Death, fate and last words.** The only sourced line is "will sacrifice themselves to ensure that his plans come to fruition" (`:30183`). The page's "sad inevitability" (line 23) and "says something kind in the middle of something terrible" are campaign text.

**F9. What he knows about the Eyes, the Cassalanters or the vault.** No source gives a household adept any knowledge. Alexandrian p. 96 gives "Manshoon's lieutenants" the Cassalanter knowledge (`sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 96; see A4). The Sidra page says it "does not say what the lieutenants know about the Eyes or the Cassalanters" (`campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:116`). The Cassalanter secrecy rule (brief ruling 7) applies: nothing outside the household and the cult knows the pact.

**F10. Fate when the sanctum falls.** None for Mookie. The adventure's defeat outcome says "the teleportation circle in {@area K22|40b} permanently dispelled" and that unconscious characters "awaken in a back alley of Waterdeep with 1 hit point each" (`sources/adventure-wdh.json:29974`). It names no fate for the defenders.

---

## G. Inner-life hints (sourced)

Each line is an exact quote. Use these for the Background and Personal goals (brief ruling 17). Do not contradict them.

**G1. The doll.**
> "Mookie's chest contains a tiny halfling doll. Stuffed inside the doll is a pouch that holds five 100 gp pearls."
> — `sources/adventure-wdh.json:30224`

**G2. Loyalty and the rightful leader.**
> "They serve him fearlessly, and will sacrifice themselves to ensure that his plans come to fruition."
> — `sources/adventure-wdh.json:30183`

> "believe that {@creature Manshoon|WDH} is the rightful leader of the Zhentarim"
> — `sources/adventure-wdh.json:30183`

**G3. The comb (Havia's parallel personal object).**
> "In Havia's chest is a golden comb shaped like a stylized dragon with tiny rubies for eyes (worth 250 gp)."
> — `sources/adventure-wdh.json:30223`

**G4. Campaign-only inner-life lines (no source; they must not be contradicted).**
> "Mookie most often feels cheerful certainty, a kind of undiscriminating goodwill toward everyone in the room regardless of what he is about to do to them, absolute devotion to Manshoon, and genuine puzzlement when opponents expect the warmth to mean something."
> — `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:13` (Emotions; Motivations at line 15 says "His warmth is not a tactic; it is simply who he is.")

> "Personality in speech: Cheerful certainty and goodwill. He's genuinely puzzled when opponents expect the warmth to mean mercy. His devotion to Manshoon comes out as happy loyalty."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:231` (the profile's own wording, after its "- **Personality in speech:**" label)

**G5. Voice habits (campaign only).**
> "- **Quirks:** He asks people's names and hometowns. He apologises while fighting."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:232`

> "- **Never:** He never gets angry, never lies about being friendly, and never lets anyone past."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:234`

---

## Not readable

- None of the sources failed to open. The Alexandrian PDF was read as rendered images and must be checked with `pdftotext -layout`.
- `sources/Other remix files/*.docx` were not searched; `SOURCE_GUIDE.md` does not name one for this figure.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
