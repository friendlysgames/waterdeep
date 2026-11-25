# Pass 6 research notes: Havia Quickknife

Page: `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1, 3, 4, 5, 6, 7, 8, 9, 15, 16, 17)
Model: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Consistency partners: `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md` (merged; read only) and `13-mookie-plush.md` (Havia and Mookie share area E10 in every source, so Mookie's page is checked against Havia's).

Method and caveats:
- Campaign files: quoted from the tool output. Line numbers are from Read or Grep output.
- Published adventure: `sources/adventure-wdh.json`. JSON strings are quoted as plain text. Tags such as `{@creature ...}` are left as written. The E10 Audience Chamber entry is `"name": "E10. Audience Chamber"` at `:30164` (page 159); its Zhents subsection is at `:30181` (page 160); E11 is at `:30199`.
- Alexandrian PDF: `sources/12. Lair  Zhentarim – Kolat Towers.pdf` (the dash is an en dash). The printed page is the PDF page plus 91 (PDF 3 = printed 94, PDF 4 = printed 95). This session has no shell, so `pdftotext` could not run. All Alexandrian quotes were transcribed from the rendered page images. **Each must be checked with `pdftotext -layout` before any prose use.**
- Wiki: `sources/research/pass5-bundles/zhentarim/wiki.txt` and the scratchpad extract `wiki-manshoons-zhentarim/12-havia-quickknife.txt` (NOT FOUND). See Not found.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDF and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

---

## A. Background facts by theme

### A1. Origin, home and training

No source gives Havia an origin, a family, a home, a childhood or a place of training. The training that is sourced is a creature template and two campaign phrases:

**The creature she is built from (published adventure)**
> "Two female lightfoot halflings—{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush}—believe that {@creature Manshoon|WDH} is the rightful leader of the Zhentarim. They serve him fearlessly, and will sacrifice themselves to ensure that his plans come to fruition. They are {@creature martial arts adept|VGM|martial arts adepts} (see {@adventure appendix B|WDH|12}), with these changes:"
> — `sources/adventure-wdh.json:30183` (E10 Zhents subsection, page 160)

**Trained in martial arts (campaign, the Lair structure doc)**
> "**E10 — Audience Chamber.** Havia Quickknife + Mookie Plush, two halfling adepts who serve as Manshoon's household fanatics. Both fight to death. They are the sanctum's most physically capable non-spellcasting combatants — trained in martial arts, faster than their size suggests, and entirely loyal. They are also the least tactically sophisticated opponents in the sanctum; they attack in a straight line and do not retreat."
> — `campaign/structure/arc-i-kolat-towers.md:160`

**Campaign: the page's own Persona (existing text; no source for the discipline or the arrival)**
> "To anyone who observes her stance, she is a martial artist trained to a discipline that does not leave room for hesitation or exit plans. Deep down, she arrived in the sanctum because she had nowhere else she wanted to be, and the notion of leaving has not crossed her mind since."
> — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:21` (the sentence before this one is the public face, quoted in C)

### A2. How she joined, and when

No source gives the date, the place or the way she came to Manshoon. The published text places her in the cell's audience room and says she believes in him:

**The belief (published adventure, the same paragraph as A1)**
> "Two female lightfoot halflings—{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush}—believe that {@creature Manshoon|WDH} is the rightful leader of the Zhentarim."
> — `sources/adventure-wdh.json:30183`

**The campaign's version of the belief (Organizations page, "One True Manshoon")**
> "Every surviving clone claims to be the one true Manshoon, and this one holds the belief with absolute certainty. Loyalty to him runs from devotion to calculation. Havia Quickknife and Mookie Plush serve him completely, and Kaevja Cynavern serves him because he is the most capable operator she has met. Agorn Fuoco would trade whatever he knows to save himself. The published adventure says Havia and Mookie hold that Manshoon is the rightful leader of the Zhentarim and will sacrifice themselves to see his plans succeed (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:43`

**Which Manshoon they serve (published adventure; see the clone lines in the Kaevja notes, F3)**
> "The original {@creature Manshoon|WDH} was one of the founders of the Zhentarim. Evil to the core, he made enemies all across Faerûn, including other powerful spellcasters such as Khelben Arunsun and Elminster. Fearing that he might be destroyed by his foes, {@creature Manshoon|WDH} magically crafted several clones-but a mishap caused all of them to be awakened at once, whereupon they tried to destroy one another in a series of conflicts that came to be known as the {@creature Manshoon|WDH} Wars."
> — `sources/adventure-wdh.json:32216`

**The campaign's time frame for the cell (the Splinter is about two years old on Ches 1)**
> "He spent about two years building the Splinter, a cell that bears his name and works independently of the Zhentarim's surviving leadership. It is hub and spoke, with Kolat Towers as the command center and the Interrogation House in the North Ward and Yellowspire in the Castle Ward as field offices linked by teleportation circles. A pass-amulet system lets him revoke anyone's access from the towers (**Kolat Towers** quest opener). He took a large part of the local network the Doom Raiders had built, and through it learned that Lord Neverember had used the local Zhentarim's resources to embezzle the vault's gold (Alexandrian Remix, *The Villains*, p. 16). On Ches 1, 1492 DR the cell holds Kolat Towers, Yellowspire and the Interrogation House, and it fights Xanathar's Guild in the Dock Ward (**Manshoon's Zhentarim**)."
> — `campaign/setting/villains/manshoon.md:33`

### A3. Post and daily work

**The audience chamber (published adventure, E10)**
> "High-ranking Zhents who desire an audience with {@creature Manshoon|WDH} come here. The room contains the following features:"
> — `sources/adventure-wdh.json:30168` (the feature list follows at `:30172`-`:30174`)

> "If they haven't been drawn elsewhere, two of {@creature Manshoon|WDH}'s followers are sparring and engaged in mock fisticuffs atop the table."
> — `sources/adventure-wdh.json:30174` (the followers are not named in this line)

**The sleeping room (published adventure, E11)**
> "{@creature Kaevja Cynavern|wdh}, Vevette Blackwater, Agorn Fuoco, {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife}, and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} all sleep here."
> — `sources/adventure-wdh.json:30212` (E11 Zhent Quarters, `:30199`, page 160)

**The post (campaign, the sanctum roles)**
> "- **The sanctum:** Behind the towers lies an extradimensional sanctum in a finite demiplane, which the original Manshoon created and his clones all know. A teleporter ring and the circle in the towers are the way in (*Dragon Heist*, 5e). Kaevja Cynavern watches the entrance and is Manshoon's early-warning mechanism, Havia Quickknife and Mookie Plush keep his audience chamber, and Yorn the Terror is the enforcer who maintains the household's fear of its master (**Kaevja Cynavern**; **Havia Quickknife**; **Mookie Plush**; **Yorn the Terror**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:55`

**The household (campaign, Manshoon page)**
> "- **Kaevja Cynavern**, **Havia Quickknife**, **Mookie Plush**, **Manafret Cherryport** and **Yorn the Terror:** His household in Kolat Towers and the sanctum behind it. Kaevja watches the entrance, Havia and Mookie keep his audience chamber, Manafret cooks, and Yorn keeps the household afraid of its master."
> — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60`

**The keys (published adventure; the only sourced item of hers that touches the towers)**
> "Each of the doors in the towers, as well as the door in the outer wall, is made of iron-bound oak and has AC 16, 27 hit points, and immunity to poison and psychic damage. If a door is locked, it can be picked by a character who makes a successful {@dc 15} Dexterity check using thieves' tools, or it can be forced open with a successful {@dc 20} Strength (Athletics) check. {@creature Manshoon|WDH}, {@creature Manafret Cherryport|wdh}, and {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} have keys to the locked doors."
> — `sources/adventure-wdh.json:26847` (Kolat Towers exterior and doors)

### A4. Belongings and what she wears

**Her chest (published adventure, E11 Treasure)**
> "In Havia's chest is a golden comb shaped like a stylized dragon with tiny rubies for eyes (worth 250 gp)."
> — `sources/adventure-wdh.json:30223` (Treasure entry at `:30215`, page 160)

**Her teleporter ring (published adventure)**
> "Havia and Mookie each wear a {@item teleporter ring|WDH} (see \"Teleporter Rings\")."
> — `sources/adventure-wdh.json:30192`

**The ring system's rule (published adventure)**
> "To access {@creature Manshoon|WDH}'s extraplanar sanctum, one needs a {@item teleporter ring|WDH}: a brass signet ring bearing a stylized M, and which emanates an aura of conjuration magic when targeted by a {@spell detect magic} spell or similar magic. {@creature Manshoon|WDH} gives these rings to his most trusted servants."
> — `sources/adventure-wdh.json:28822` (Teleporter Rings entry at `:28818`)

**Rings in the campaign (organizations page, the rings to trusted servants)**
> "Access to Kolat Towers is something Manshoon grants and can withdraw. A pass-amulet system lets him revoke anyone's access from the towers, and his brass teleporter rings, each bearing a stylized M, go only to his most trusted servants."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:41` (the bullet is **Trust Is Issued and Revoked**; it continues with Sidra holding the rings)

### A5. Stats and body (published adventure and the Alexandrian)

**Hit points (published adventure)**
> "They have 49 ({@dice 11d6 + 11}) hit points each."
> — `sources/adventure-wdh.json:30188`

**Racial traits (published adventure)**
> "They have these racial traits: They are Small, and their walking speed is 25 feet. They can move through the space of a Medium or larger creature. They have advantage on saving throws against being {@condition frightened}. They speak Common and Halfling."
> — `sources/adventure-wdh.json:30189`

**Alignment (published adventure)**
> "Havia and Mookie are lawful evil."
> — `sources/adventure-wdh.json:30187`

### A6. Relationships on day one

**Paired with Mookie (campaign, the page's own Relationships, existing text)**
> "**Relationships.** Havia is paired with Mookie Plush as one of two halfling adepts serving as Manshoon's household fanatics in E10, one of the sanctum's most physically capable non-spellcasting combatants, and a source of no useful information if somehow captured — she does not negotiate and knows nothing that would benefit the party."
> — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:25` (the "if somehow captured" clause is quest-time; see C)

**Paired with Havia (campaign, Mookie's page)**
> "**Relationships.** Mookie is paired with Havia Quickknife in E10, a halfling adept whose warm manner makes him in some ways more unsettling than a straightforwardly violent opponent, and the sort of NPC whose death, if the party pauses on it, feels like waste rather than victory."
> — `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:25`

**The fighting rule (campaign, the Lair structure doc; quoted in full in A1)**
> "They are also the least tactically sophisticated opponents in the sanctum; they attack in a straight line and do not retreat."
> — `campaign/structure/arc-i-kolat-towers.md:160`

**Sidra's page (merged; read only). Havia is not named in the Sidra page.** Its lieutenant list is "**Urstul Floxin**, **Vevette Blackwater** and **Agorn Fuoco** serve the cell as lieutenants and field leaders." — `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:38` (see D4).

### A7. Faith

No source names a god for Havia. The Yondalla page lists her among the halflings and says none of them has a stated god:
> "- **Broxley Fairkettle**, **Osco Salibuck**, **Corene Wyldath**, **Manafret Cherryport**, **Havia Quickknife**, **Mookie Plush** (Notable Figures): the other halflings in the files, none with a stated god."
> — `campaign/setting/deities/yondalla.md:105` (the same list is at `:65`, quoted under Cross-references)

### A8. Rank and time in post

No source gives a rank title, a date of joining or length of service for Havia. The Organizations page lists her under **Key Members** with no rank term (`campaign/setting/organizations/09-manshoons-zhentarim.md:107`). The Manshoon page calls her household (`01-manshoon.md:60`). The published capture offer names her as a lieutenant (`sources/adventure-wdh.json:26763`; see D4).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, current page: "*Lightfoot halfling adept, lawful evil, she/her*. Stat block: **Adept**." — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:5`
- Campaign, Organizations page: "- **Havia Quickknife** — Lightfoot halfling adept, lawful evil; see the **Havia Quickknife** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:107`
- Published adventure: "Havia and Mookie are lawful evil." — `sources/adventure-wdh.json:30187`
- Alexandrian, printed p. 95 [PDF 4]: "Havia Quickknife / Mookie Plush (LE lightfoot halfling) – martial arts adepts, DH p. 209" and the bullet "Lawful Evil". Image transcription.
- Consistent across all four.

**Species**
- Campaign: "Lightfoot halfling" — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:5`; `campaign/setting/organizations/09-manshoons-zhentarim.md:107`
- Published adventure: "Two female lightfoot halflings" — `sources/adventure-wdh.json:30183`
- Alexandrian, printed p. 95 [PDF 4]: "(LE lightfoot halfling)" (image transcription)

**Pronouns**
- Campaign: "she/her" — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:5`
- Published adventure: "Two female lightfoot halflings" — `sources/adventure-wdh.json:30183`
- Pronoun table: "| Havia Quickknife | manshoons-zhentarim/12-havia-quickknife.md:5 | she/her | prose (\"a small halfling woman\", \"she is a halfling, she is small\") | High |" — `docs/plans/npc-pronouns-table-group-c.md:56`
- Consistent. (The Mookie conflict is in D1.)

**Stat block label**
- Campaign: "Stat block: **Adept**." — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:5`
- Published adventure: "They are {@creature martial arts adept|VGM|martial arts adepts} (see {@adventure appendix B|WDH|12}), with these changes:" — `sources/adventure-wdh.json:30183` (the source label is "martial arts adept", a VGM creature)
- Alexandrian, printed p. 95 [PDF 4]: "martial arts adepts, DH p. 209"
- The page's "Adept" is shorter than the source's "martial arts adept". Minor; see D2.

**Racial traits and HP** (see A5): `sources/adventure-wdh.json:30188`, `:30189`. The Alexandrian lists the same traits (printed p. 95 [PDF 4]): "Racial Traits: Small, walking speed 25 ft., move through the space of a Medium or larger creature, advantage on saving throws vs. being frightened." (image transcription)

---

## C. Sentences on the current page that narrate a quest event or a day-one conflict

Current page: `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md`. "Day-one OK" means the sentence needs no quest gate. "Quest-time" means it names the party, an intrusion, a capture or a combat sequence.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Lightfoot halfling adept, lawful evil, she/her*. Stat block: **Adept**." | Day-one OK. "Adept" is the short form (B) | Org `:107`; adventure `:30183`, `:30187` |
| 2 | L6 | "**Affiliation:** Manshoon's Zhentarim" | Day-one OK | Org `:1` (heading) and `:107` |
| 3 | L7 | "**Featured in:** **Kolat Towers**" | Quest reference in the Summary (kept, as the other pages do). No Kolat Towers quest journal exists | Structure doc `arc-i-kolat-towers.md` (no line cited) |
| 4 | L11 | "**Resonance.** Havia should inspire initial underestimation — she is a halfling, she is small, she is in a formal audience chamber — and then immediate correction, because she is in E10 of Manshoon's sanctum and she has been waiting for someone to enter it." | Mixed. "and then immediate correction" and "waiting for someone to enter it" are quest-time framing (an intruder arrives). The location and posture are day-one | `sources/adventure-wdh.json:30168` ("High-ranking Zhents who desire an audience with {@creature Manshoon|WDH} come here."); `campaign/structure/arc-i-kolat-towers.md:160` ("the sanctum's most physically capable non-spellcasting combatants") |
| 5 | L13 | "**Emotions.** Havia most often feels settled conviction, physical readiness she has to consciously contain, absolute certainty in her service to Manshoon, controlled anticipation in combat, and no ambivalence of any kind about the work." | Day-one, except "controlled anticipation in combat" (a combat state; keep as a standing posture) | Voice `:214` ("Settled conviction. She has no ambivalence and no exit plan, and the voice has none either."); `sources/adventure-wdh.json:30183` ("serve him fearlessly") |
| 6 | L15 | "**Motivations.** Havia wants to serve Manshoon completely and to neutralize any threat that enters the audience chamber. She does not want other things." | Day-one posture. "any threat that enters" is a standing order, not an event | Org `:43` ("Havia Quickknife and Mookie Plush serve him completely"); `sources/adventure-wdh.json:30183` |
| 7 | L17 | "**Inspirations.** When playing Havia, channel River Tam (*Firefly*), Elektra (*Daredevil*, Netflix series), and Dolores (*Westworld*)." | Not a fact | n/a |
| 8 | L21 (a) | "**Persona.** To the world, Havia Quickknife is a small halfling woman in a formal audience chamber." | Day-one OK. "in a formal audience chamber" is the room (E10); the adventure does not say she is seated there (see F9) | `sources/adventure-wdh.json:30168` (the room) |
| 9 | L21 (b) | "To anyone who observes her stance, she is a martial artist trained to a discipline that does not leave room for hesitation or exit plans." | Day-one OK. "trained to a discipline" has no source (F2) | `campaign/structure/arc-i-kolat-towers.md:160` ("trained in martial arts") |
| 10 | L21 (c) | "Deep down, she arrived in the sanctum because she had nowhere else she wanted to be, and the notion of leaving has not crossed her mind since." | Day-one attitude. The arrival is unsourced (F1) | None. (Voice `:214` and `:217` are consistent.) |
| 11 | L23 (a) | "**Morale.** Havia attacks in a straight line and does not retreat." | Combat tactic. Not a day-one event | `campaign/structure/arc-i-kolat-towers.md:160` ("they attack in a straight line and do not retreat") |
| 12 | L23 (b) | "She and Mookie do not coordinate tactically — they simply both move toward the threat simultaneously — but they are faster than their size suggests, trained well past what most opponents expect, and entirely unwilling to stop." | Combat tactic. "move toward the threat" describes a fight. "trained well past what most opponents expect" has no source (F2) | `campaign/structure/arc-i-kolat-towers.md:160` ("trained in martial arts, faster than their size suggests"); no source for "trained well past" |
| 13 | L23 (c) | "She fights to death." | Combat state. Keep as a standing trait | `sources/adventure-wdh.json:30183` ("will sacrifice themselves to ensure that his plans come to fruition"); `arc-i-kolat-towers.md:160` ("Both fight to death.") |
| 14 | L25 (a) | "**Relationships.** Havia is paired with Mookie Plush as one of two halfling adepts serving as Manshoon's household fanatics in E10, one of the sanctum's most physically capable non-spellcasting combatants," | Day-one OK | `campaign/structure/arc-i-kolat-towers.md:160`; `sources/adventure-wdh.json:30183` |
| 15 | L25 (b) | "and a source of no useful information if somehow captured — she does not negotiate and knows nothing that would benefit the party." | Quest-time (capture). **Conflicts with the published capture offer** (D3) | `sources/adventure-wdh.json:26763` (the offer names her; quoted in D3) |
| 16 | L29 | "A small halfling woman seated in the formal audience chamber of Kolat Towers' inner sanctum. Her stance marks her as someone trained far past what her size would suggest." | Day-one. "seated" has no source (F9). "trained far past what her size would suggest" is the page's own phrase | `sources/adventure-wdh.json:30168`; `campaign/structure/arc-i-kolat-towers.md:160` ("faster than their size suggests") |

**Voice profile quest-time clauses** (`.claude/skills/character-voices/voices/manshoons-zhentarim.md`, Havia block at `:207` to `:221`):
- No line narrates a capture, an intrusion or a rescue. The Greeting "No further." (`:219`) and the Under-pressure "For him." (`:221`) are warnings to people who have entered the room. They are standing lines, so no day-one restatement is required. The drafter should confirm that reading under ruling 3.
- The Business line is "(silence)" (`:220`). Day-one.
- `:217`, Never: "She never negotiates, never retreats, and never explains." Day-one.

---

## D. Conflicts

**D1. Mookie's pronouns (a conflict that touches Havia's pairing)**
- Published adventure: "Two female lightfoot halflings—{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush}—" — `sources/adventure-wdh.json:30183`
- Campaign, Mookie's page: "*Lightfoot halfling adept, lawful evil, he/him*. Stat block: **Adept**." — `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:5`. Mookie's Relationships (`:25`) pair him with Havia.
- Campaign, the voice profile (Mookie block): "Warm and casual: \"friend\", \"aw\", \"sorry about this\". He calls Manshoon \"the boss\" fondly." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:230`
- Pronoun table: "| Mookie Plush | manshoons-zhentarim/13-mookie-plush.md:5 | he/him | prose (\"he has the approachable affect\", \"His warmth is not a tactic\") | High |" — `docs/plans/npc-pronouns-table-group-c.md:57`
- Higher source: the campaign (he/him). The pass-6 Manshoon notes already flagged this as D20: `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/01-manshoon.md:497`. The Havia page's pronouns are not in conflict. Any Havia Background sentence about Mookie should use his campaign pronoun and note the published "female" in Draft Notes.

**D2. Stat label**
- Campaign: "Stat block: **Adept**." (`:5`). Published adventure: "martial arts adept" (`sources/adventure-wdh.json:30183`). Alexandrian: "martial arts adepts" (printed p. 95). The short label is the page's choice. Mention under Draft Notes or write the full label. Orchestrator's call.

**D3. Capture: "knows nothing" against "can be captured and turned over for interrogation"**
- Campaign, the page: "a source of no useful information if somehow captured — she does not negotiate and knows nothing that would benefit the party." — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:25`
- Published adventure: "Such proof can be obtained from any of {@creature Manshoon|WDH}'s lieutenants, who can be captured and turned over for interrogation. These lieutenants include Sidra Romeir ({@area K2|3db}), {@creature Manafret Cherryport|wdh} ({@area K3|3de}), {@creature Urstul Floxin|wdh} ({@area E5|41d}), Vevette Blackwater and Agorn Fuoco ({@area E8|425}), and {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} ({@area E10|42a})." — `sources/adventure-wdh.json:26763` (the paragraph opens with "Delivering proof that {@creature Manshoon|WDH} is hiding in Waterdeep to {@creature Laeral Silverhand|WDH}, ... triggers a far-reaching effort to oust him from the city.")
- Higher source: the campaign's "knows nothing" is a campaign statement. The published offer says she is a lieutenant who can be captured for interrogation, which is a route to proof. The drafter must choose. The Sidra notes routed this offer to **Kolat Towers** and quote the same line (`docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/04-sidra-romeir.md:41`).

**D4. Lieutenant or household**
- Campaign, Manshoon page household bullet: "- **Kaevja Cynavern**, **Havia Quickknife**, **Mookie Plush**, **Manafret Cherryport** and **Yorn the Terror:** His household in Kolat Towers and the sanctum behind it." — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60`
- Campaign, Manshoon page Sources line: "the cell's lieutenants, household and sites" — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:147`
- Published adventure: the lieutenant list at `sources/adventure-wdh.json:26763` (quoted in D3).
- Campaign, Sidra page: "**Urstul Floxin**, **Vevette Blackwater** and **Agorn Fuoco** serve the cell as lieutenants and field leaders." — `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:38` (Havia is not on this list)
- Higher source: the campaign household label (`01-manshoon.md:60`). The published offer (`:26763`) treats her as a lieutenant. Not resolved.

**D5. The name "Havi" (a different figure, close spelling)**
- Campaign, Organizations page: "and Manshoon's three apprentices, Ered Payno, Havi Termock and Savara Firethorn, sleep in the old apprentices' quarters and wear teleporter rings (**Sidra Romeir**; **Manafret Cherryport**; *Dragon Heist*, 5e)." — `campaign/setting/organizations/09-manshoons-zhentarim.md:54`
- Published adventure: "{@creature Manshoon|WDH} now allows his own apprentices—Ered Payno, Havi Termock, and Savara Firethorn—to do the same. All three can be found in {@area K15|3fc}." — `sources/adventure-wdh.json:28377`
- Not a conflict. A drafter who writes "Havia" in a line about the apprentices must check the spelling. Havia Quickknife is the halfling in E10, and Havi Termock is one of the three apprentices.

**D6. The E10 posting**
- Published adventure: "Two female lightfoot halflings ... believe that ..." (`:30183`); the E10 header `"name": "E10. Audience Chamber"` (`:30164`).
- Alexandrian, printed p. 94 [PDF 3]: "Area E10 – Audience Chamber: This room is lit by a sunglobe which levitates in midair near the ceiling." and the roster "Havia Quickknife* + Mookie Plush*" under the "Area E10 – Audience Chamber" column. Image transcription.
- Campaign, the Lair structure doc: "**E10 — Audience Chamber.** Havia Quickknife + Mookie Plush, two halfling adepts who serve as Manshoon's household fanatics." — `campaign/structure/arc-i-kolat-towers.md:160`
- Consistent.

**D7. Ring**
- Published adventure: "Havia and Mookie each wear a {@item teleporter ring|WDH} (see \"Teleporter Rings\")." — `sources/adventure-wdh.json:30192`
- Alexandrian, printed p. 94 [PDF 3]: "Havia Quickknife* + Mookie Plush*" with the footnote "* Has a teleporter signet ring." (image transcription)
- Consistent.

**D8. "Seated" and "sparring" (a minor point of physical setting)**
- Campaign, the page's Overview: "seated in the formal audience chamber" (`:29`). Published adventure: no line seats Havia. The room's features include: "If they haven't been drawn elsewhere, two of {@creature Manshoon|WDH}'s followers are sparring and engaged in mock fisticuffs atop the table." — `sources/adventure-wdh.json:30174`. The sparring pair is unnamed. Keep "seated" only as the page's own description (F9).

---

## E. Stale lines in other files (not edited), and routed quest references

### E1. Stale lines
- `campaign/structure/arc-i-kolat-towers.md:320`: "- **Notable Figures** — Existing profiles: Manshoon, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin, Lady Gondafrey, Skeemo Weirdbottle. New profiles needed: Kaevja Cynavern, Havia Quickknife, Mookie Plush, Yorn the Terror." Stale for Havia (her profile exists).
- `campaign/structure/arc-i-kolat-towers.md:321`: "- **the Bestiary (not yet drafted)** — Boss stat block needed: Manshoon (with simulacrum mechanic distinction). Standard stat blocks needed: Havia Quickknife, Mookie Plush." Still true (the Bestiary is not drafted); no file holds a Havia stat block.
- `sources/SOURCE_GUIDE.md:35`: "Contains: Manshoon, his simulacrum, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin." It omits Havia and Mookie. Incomplete rather than wrong.

### E2. Routed to quests (quest-time facts and where they already live)
- The E2 alarm brings Havia out: `sources/adventure-wdh.json:29960` ("{@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} (see {@area E10|42a})") under the entry "Alarm Mechanism" (`:29949`). Routed to **Kolat Towers**. Structure doc: `campaign/structure/arc-i-kolat-towers.md:148` ("This is the sanctum's entry alarm — the discharge also sends a magical pulse to E3, alerting Kaevja.") and `:182` ("E2's pressure plate, Kaevja in E3, and Urstul in E5 are all alarm triggers even without tower combat.")
- The E10 fight: `campaign/structure/arc-i-kolat-towers.md:160` ("Both fight to death."). Routed to **Kolat Towers**.
- The capture offer (D3): `sources/adventure-wdh.json:26763`. Routed to **Kolat Towers**.
- The keys (A3): `sources/adventure-wdh.json:26847`. Routed to **Kolat Towers** (the doors are the raid's approach).
- Mookie's death line on his page: `campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md:25` ("the sort of NPC whose death, if the party pauses on it, feels like waste rather than victory"). It is Mookie's page, not Havia's. It names the party and is quest-time.

---

## F. Gaps (what a Background would need that no source gives)

Each gap lists the sourced facts the drafter must stay consistent with.

1. **Origin, family, childhood, home and the arrival.** No source. The page's "Deep down, she arrived in the sanctum because she had nowhere else she wanted to be" (`:21`) has no source. Consistency: the only sourced fact is that she is one of two "female lightfoot halflings" who believe Manshoon is the rightful leader (`sources/adventure-wdh.json:30183`).
2. **Her training.** No source. The published text gives the creature "martial arts adept" (`:30183`). The campaign says "trained in martial arts, faster than their size suggests" (`arc-i-kolat-towers.md:160`) and, on the page, "a discipline" (`:21`) and "trained well past what most opponents expect" (`:23`). No source names a school, a teacher or a discipline. A Background that names one is invented.
3. **When and how she came to Manshoon.** No source. The Splinter is about two years old on Ches 1 (`campaign/setting/villains/manshoon.md:33`). Consistency: the Sidra page sets the same constraint for Sidra (`04-sidra-romeir.md:17`).
4. **Her bond with Mookie.** Sourced: "Mookie is paired with Havia Quickknife in E10" (`13-mookie-plush.md:25`); "Two female lightfoot halflings" (`sources/adventure-wdh.json:30183`); and "{@creature Kaevja Cynavern|wdh}, Vevette Blackwater, Agorn Fuoco, {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife}, and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} all sleep here." (`:30212`). No kinship, friendship, history or rivalry is sourced. A Background that gives one is invented.
5. **Her comb.** The chest holds "a golden comb shaped like a stylized dragon with tiny rubies for eyes (worth 250 gp)" (`:30223`). No source says who gave it or what it means. Consistency: keep the item as printed.
6. **Her keys.** Sourced: Manshoon, Manafret Cherryport and Havia "have keys to the locked doors" (`:26847`). Consistency: she holds the same kind of key as Manshoon and Manafret.
7. **Faith.** No god is named. Yondalla page: "none with a stated god" (`campaign/setting/deities/yondalla.md:105`). Consistency: do not give her a god.
8. **Rank.** No source. Consistency: household (`01-manshoon.md:60`); lieutenant in the published offer (`:26763`); the Organizations page's "Key Members" listing (`:107`) has no rank term.
9. **Her seat and posture in the room.** "seated" (`:29`) is the page's wording. The published adventure does not seat her (`:30168` to `:30174`). Consistency: she is in the audience chamber, which has "a black marble table surrounded by high-backed wooden chairs" (`sources/adventure-wdh.json:30173`).
10. **Pronunciation.** None. The Pronunciation Guide (`:25`) lists Kaevja (`:173`-`:174`) and not Havia.
11. **Fears, loves, grudges, habits outside the post.** None sourced. See G.
12. **The apprentice Havi Termock.** Not Havia. D5. Consistency: keep the two names apart.
13. **Her relationship to Manshoon beyond "serve him completely".** Sourced: "serve him completely" (`org :43`) and "Manshoon is the rightful leader" (`:30183`). No personal tie is sourced. No source says Manshoon has ever spoken to her.
14. **Morale and two Relationship sentences are combat text.** C rows 11 to 15. A Background that explains her caution must not name the party's actions.
15. **The Two Zhentarims.** No source ties Havia to Davil Starsong's Doom Raiders. The Organizations callout says: "The villains on this page answer only to Manshoon." — `campaign/setting/organizations/09-manshoons-zhentarim.md:19`. Consistency: she is in Manshoon's cell only.
16. **Cassalanters, Lolth, Xanathar.** No source ties Havia to any of them. The Lolth rule (brief ruling 8) does not apply: no source gives her a faith.

---

## G. Inner-life hints in the sources (exact quotes)

These are for the drafter's Background and personal goals (brief ruling 17). Each must stay consistent with them.

**Devotion, with the cost named** (published adventure)
> "They serve him fearlessly, and will sacrifice themselves to ensure that his plans come to fruition."
> — `sources/adventure-wdh.json:30183`

**Loyalty without a second thought** (campaign, Organizations page)
> "Havia Quickknife and Mookie Plush serve him completely, and Kaevja Cynavern serves him because he is the most capable operator she has met."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:43`

**Possessions** (published adventure)
> "In Havia's chest is a golden comb shaped like a stylized dragon with tiny rubies for eyes (worth 250 gp)."
> — `sources/adventure-wdh.json:30223`

**Trust in her** (published adventure)
> "{@creature Manshoon|WDH}, {@creature Manafret Cherryport|wdh}, and {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} have keys to the locked doors."
> — `sources/adventure-wdh.json:26847`

**Her settledness** (voice profile)
> "**Personality in speech:** Settled conviction. She has no ambivalence and no exit plan, and the voice has none either."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:214`

**What she does instead of talking** (voice profile)
> "**Quirks:** She shifts her stance instead of answering."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:215`

**Her limit** (voice profile, Never)
> "**Never:** She never negotiates, never retreats, and never explains."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:217`

**Her wording** (voice profile, Word choice)
> "**Word choice:** Minimal and absolute: \"No further.\" / \"For him.\""
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:212`

**The page's own Persona, existing text** (campaign)
> "Deep down, she arrived in the sanctum because she had nowhere else she wanted to be, and the notion of leaving has not crossed her mind since."
> — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:21`

**The one bond she has, in the page's own text** (campaign)
> "**Relationships.** Havia is paired with Mookie Plush as one of two halfling adepts serving as Manshoon's household fanatics in E10, ..."
> — `campaign/setting/notable-figures/manshoons-zhentarim/12-havia-quickknife.md:25`

---

## Cross-references

Every other file:line where Havia appears, with the line copied (grep output, this session). Lines already quoted above are marked "see".

**Campaign, Organizations page** (`campaign/setting/organizations/09-manshoons-zhentarim.md`)
- `:19` (callout): "The villains on this page answer only to Manshoon." (see F15)
- `:43` "- **One True Manshoon:** ... Havia Quickknife and Mookie Plush serve him completely, ..." (see A2)
- `:54` "... Manshoon's three apprentices, Ered Payno, Havi Termock and Savara Firethorn, ..." (see D5)
- `:55` "... Havia Quickknife and Mookie Plush keep his audience chamber, ..." (see A3)
- `:107` "- **Havia Quickknife** — Lightfoot halfling adept, lawful evil; see the **Havia Quickknife** page in Notable Figures." (see B)

**Campaign, Manshoon page** (`campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md`)
- `:60` (see A3, D4)
- `:147` "- **Sidra Romeir**, **Urstul Floxin**, ..., **Havia Quickknife**, **Mookie Plush**, ... (Notable Figures): the cell's lieutenants, household and sites" (see D4)

**Campaign, Mookie's page** (`campaign/setting/notable-figures/manshoons-zhentarim/13-mookie-plush.md`)
- `:5` "*Lightfoot halfling adept, lawful evil, he/him*. Stat block: **Adept**." (see D1)
- `:15` "**Motivations.** Mookie wants to serve Manshoon completely. ..."
- `:23` "**Morale.** Mookie fights to death, like Havia, but with ..."
- `:25` "**Relationships.** Mookie is paired with Havia Quickknife in E10, ..." (see A6)

**Campaign, Sidra page** (`campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md`)
- `:38` (see D4). Havia is not named elsewhere on the Sidra page.

**Campaign, Lair structure doc** (`campaign/structure/arc-i-kolat-towers.md`)
- `:148` and `:182` (see E2)
- `:160` "**E10 — Audience Chamber.** Havia Quickknife + Mookie Plush, two halfling adepts who serve as Manshoon's household fanatics. ..." (see A1, C)
- `:320`, `:321` (see E1)

**Campaign, deities**
- `campaign/setting/deities/yondalla.md:65` "... The halflings among them are **Broxley Fairkettle**, **Osco Salibuck**, **Kelso Fiddlewick**, **Corene Wyldath**, **Manafret Cherryport**, **Havia Quickknife** and **Mookie Plush**, and none of their pages gives a god, so this page makes none of them a worshiper."
- `campaign/setting/deities/yondalla.md:105` (see A7)

**Campaign, character voices**
- `.claude/skills/character-voices/voices/manshoons-zhentarim.md:207`-`:221` (the Havia block; see B, C and G). The Mookie block is at `:225`-`:239`; its line `:230` is the Word choice line (see D1).
- `.claude/skills/character-voices/SKILL.md:34` (the index names Havia)

**Docs** (planning and research notes; none edited)
- `docs/plans/npc-pronouns-table-group-c.md:56` (Havia, she/her) and `:57` (Mookie, he/him) (see B and D1)
- `docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:132` ("**Havia Quickknife** — org `:33`: ... NF `12-havia-quickknife.md:5`: ... Result: matches.")
- `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/01-manshoon.md:322`-`:323` (the adventure quote, "Adventure, Havia and Mookie (gender conflict; see D20)") and `:497` (D20, Mookie's gender) (see D1)
- `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/03-vevette-blackwater.md:105` (the E11 line) and `:121` (the heading "**Kaevja Cynavern, Havia Quickknife, Mookie Plush**")
- `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/04-sidra-romeir.md:41` (the capture offer, quoted in D3)
- `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/05-agorn-fuoco.md:126` (the E11 line)
- `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/06-avareen-windrivver.md:324` and `07-zorbog-jyarkoth.md:266` (the capture offer, quoted in D3)

**Sources**
- `sources/adventure-wdh.json`: `:26763` (capture offer; D3), `:26847` (keys; A3), `:28377` (Havi Termock; D5), `:28822` (Teleporter Rings; A4), `:29949` ("Alarm Mechanism"), `:29960` (E2 alarm lists Havia; E2), `:30164` (E10 header), `:30168` (audience chamber; A3), `:30172`-`:30174` (E10 features; A3, D8), `:30173` (table and chairs; F9), `:30183` (the creature and the belief; A1, A2, B, D1), `:30187` (alignment), `:30188` (HP), `:30189` (traits), `:30192` (ring; A4), `:30199` (E11 header), `:30212` (sleeping room; A3), `:30215` (Treasure header), `:30223` (comb; A4), `:32216` (the clones; A2)
- `sources/SOURCE_GUIDE.md:35` (see E1)
- `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed pp. 94 and 95 (see B, D6, D7)

---

## Not found

Searches and what they returned.

- **Wiki (the Forgotten Realms Wiki bundles).** I searched every `sources/research/**/wiki*.txt` for `Kaevja|Havia|Quickknife|Cynavern|Mookie`, and for `martial arts adept|Zhent Martial`. No hit names Havia. The scratchpad extract `wiki-manshoons-zhentarim/12-havia-quickknife.txt` reads "NOT FOUND".
- **Pronunciation.** Not in the adventure's Pronunciation Guide (`sources/adventure-wdh.json:25`, which lists Kaevja at `:173`).
- **Published adventure, other names.** Searched `sources/adventure-wdh.json` for `Havia|Quickknife`. Hits are listed in Cross-references. No hit gives a birthplace, age, family, faith, rank or a first name.
- **Appendices and Act III.** `sources/Appendix_B_-_Player_Factions.md`, `Appendix_C_-_Player_Faction_Missions.md`, `Appendix_D_-_Running_the_Tavern.md` and `sources/Act_III_Arc_E.md`: no line names Havia.
- **Factions Guide, gazetteer, locations, quests.** `campaign/guides/factions/`, `campaign/gazetteer/waterdeep/`, `campaign/locations/`, `campaign/quests/`: no line names Havia. (Grep across `campaign/` for `Havia|Mookie|Kaevja|Cynavern|Quickknife` returned only the files in Cross-references.)
- **Kolat Towers quest journal.** None exists. `arc-i-kolat-towers.md` is the structure doc and is pending conversion.
- **Stat block for Havia.** The Bestiary is not drafted (`arc-i-kolat-towers.md:321`). No file holds a Havia stat block beyond the adventure's changes (`sources/adventure-wdh.json:30188`-`:30189`).
- **Rank title, date of joining, age, height, home, training school.** None.

## Not readable

- `sources/12. Lair  Zhentarim – Kolat Towers.pdf`: read as rendered images (PDF pages 3 and 4, printed pp. 94 and 95). No `pdftotext` in this session. Every Alexandrian quote above is a transcription and needs a `pdftotext -layout` check before prose use.
- `sources/Other remix files/*.docx`: not opened. The only `.docx` line in `sources/SOURCE_GUIDE.md` that matches `Zhentarim` is `:688` (a Davil Starsong and Doom Raiders file). It names no Havia. Not expected to cover Havia.

## Not run
- `voicecheck.py` was not run (research only).
- No file was edited except this notes file. The page was not written.
