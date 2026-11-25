# Pass 6 research notes: Sidra Romeir (`campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md`)

Research only. No page was written. Every quote was copied from a tool result in this pass. Line numbers come from `Read` or `Grep` output, or from the stated printed page.

Method and source status:
- The scratchpad wiki extract `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-manshoons-zhentarim/04-sidra-romeir.txt` reads, in full: "NOT FOUND" (line 1). Confirmed below.
- The Alexandrian PDFs are image pages. Quotes from them were transcribed by reading the page image, not from a text layer. Each PDF quote is flagged **[check with pdftotext]**. Printed page numbers are given.
- No shell was available, so `pdftotext` was not run.

---

## Wiki check (NOT FOUND confirmed)

- `sources/research/**/wiki*.txt`: a Grep for `Sidra|Romeir` restricted to `wiki*.txt` returns no files.
- Scratchpad `fandom-dump/forgottenrealms_pages_current.xml` (a Forgotten Realms Wiki dump): the only hit is one index line. It is not an article on Sidra. Location: `…/scratchpad/fandom-dump/forgottenrealms_pages_current.xml:3744333`. Quote:
  > "{{P|[[Savra Belabranta]]|39,48}} • {{P|[[Seffia Naelryke]]|70}} • {{P|[[Sembra Vashir]]|78}} • {{P|[[Shan Chien]]|79}} • {{P|[[Sidra Romeir]]|148,149}}"
  > — `scratchpad/fandom-dump/forgottenrealms_pages_current.xml:3744333` (the Humans entry of the "Characters" index of the *Waterdeep: Dragon Heist* article; the numbers are *Dragon Heist* pages 148 and 149)

  The article is the 5e adventure. Its text at line 3744301 reads, in part:
  > "For use with the fifth edition"
  > — `scratchpad/fandom-dump/forgottenrealms_pages_current.xml:3744301`
- `scratchpad/wiki-manshoons-zhentarim/`: `01-manshoon.txt` to `14-yorn-the-terror.txt`. Only `04-sidra-romeir.txt` is a NOT FOUND stub.
- Conclusion: no wiki article on Sidra. The only wiki fact is the index entry above (DH pages 148–149).

---

## A. Background facts by theme

**Origin and species**
> "The card players are Sidra Romeir (LE female Calishite human {@creature veteran}) and two subordinates (LE male Tethyrian human {@creature thug||thugs}). Since the force field around Kolat Towers keeps out riffraff, Sidra assumes the characters are guests of {@creature Manshoon|WDH} arriving for a clandestine meeting. If the characters give her no reason to believe otherwise, she and her thugs escort them wherever they ask to go. If it becomes clear that the characters don't belong in the towers, Sidra and her thugs attack. Combat in this area draws the attention of {@creature Manafret Cherryport|wdh} in {@area K3|3de}, who investigates."
> — `sources/adventure-wdh.json:28155` (the "Zhents" entry in K2, page 149)

> "Sidra wears a {@item teleporter ring|WDH} (see \"Teleporter Rings\")."
> — `sources/adventure-wdh.json:28156` (same entry)

**Family, birthplace, upbringing, former life**: no source. See F1.

**How she came to the post; the lieutenant designation**
> "Such proof can be obtained from any of {@creature Manshoon|WDH}'s lieutenants, who can be captured and turned over for interrogation. These lieutenants include Sidra Romeir ({@area K2|3db}), {@creature Manafret Cherryport|wdh} ({@area K3|3de}), {@creature Urstul Floxin|wdh} ({@area E5|41d}), Vevette Blackwater and Agorn Fuoco ({@area E8|425}), and {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} ({@area E10|42a})."
> — `sources/adventure-wdh.json:26763` (the second and third sentences of the paragraph; the first sentence reads "Delivering proof that {@creature Manshoon|WDH} is hiding in Waterdeep to {@creature Laeral Silverhand|WDH}, {@creature Mirt|WDH}, the Harpers, Force Grey, the Blackstaff, the Lords' Alliance, the Order of the Gauntlet, the City Watch, or the Watchful Order of Magists and Protectors triggers a far-reaching effort to oust him from the city."; "Report Manshoon" entry, page 147)

> "The Black Network has an open recruitment policy. Anyone can join. Tenacity and loyalty are highly valued (but not essential) traits in new members."
> — `sources/adventure-wdh.json:1443`

> "Adventurers can't join {@creature Manshoon|WDH}'s cause, but they can join and receive aid from the Zhents who are opposed to him."
> — `sources/adventure-wdh.json:1446` (the source sentence continues)

> "His lieutenants rise by impressing him, and Agorn Fuoco was raised quickly after he made a good impression on the wizard (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:71` (campaign paraphrase, citing DH 5e. The matching published line was not found: a Grep for "rise by impressing" and "Agorn Fuoco was raised" in `adventure-wdh.json` returns nothing.)

Full line 71 for context: "- **Recruiting:** The Black Network has an open recruitment policy that prizes tenacity and loyalty without requiring either, but the published adventure says adventurers cannot join Manshoon's cause (*Dragon Heist*, 5e). His lieutenants rise by impressing him, and Agorn Fuoco was raised quickly after he made a good impression on the wizard (*Dragon Heist*, 5e). Kaevja Cynavern was a Red Wizard of Thay who gave up her Thayan head tattoos and red robes to study under him (*Dragon Heist*, 5e)."

**Post and duties (Kolat Towers)**
> "Sidra Romeir runs the ground floor like a barracks, Manafret Cherryport cooks for the household, and Manshoon's three apprentices, Ered Payno, Havi Termock and Savara Firethorn, sleep in the old apprentices' quarters and wear teleporter rings (**Sidra Romeir**; **Manafret Cherryport**; *Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:54` (the bullet begins "- **Kolat Towers:** A dilapidated pair of towers stands one block north of Phaulkonmere…")

> K2 heading: "K2. Dining Room" — `sources/adventure-wdh.json:28137` (page 149, area id `3db`)

> "Three Zhents in black armor sit around a stone dining table, playing Three-Dragon Ante (a card game). The table is set with silver."
> — `sources/adventure-wdh.json:28145` (K2 features)

> "A clone of the wizard {@creature Manshoon|WDH}, one of the founders of the Zhentarim, is hiding in Waterdeep."
> — `sources/adventure-wdh.json:560` (the same paragraph continues: "{@creature Manshoon|WDH} lurks in Kolat Towers, a pair of wizards' towers in the Trades Ward. This residence is described in chapter 8." See D5.)

**Rings and the ring system**
> "To access {@creature Manshoon|WDH}'s extraplanar sanctum, one needs a {@item teleporter ring|WDH}: a brass signet ring bearing a stylized M, and which emanates an aura of conjuration magic when targeted by a {@spell detect magic} spell or similar magic. {@creature Manshoon|WDH} gives these rings to his most trusted servants."
> — `sources/adventure-wdh.json:28822` (section "Teleporter Rings")

> "Sidra Romeir holds the rings when lieutenants leave the Towers and hands them to replacements when a holder does not come back."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:41` (the bullet "Trust Is Issued and Revoked". This sentence carries no source tag and no citation.)

> "The ring goes to whoever replaces the last one. That's how it works here."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:80` (Sidra's Business sample line)

> "| 10 min | 1 mage + 2 thugs arrive at K22. Sidra locks the teleporter ring system — rings already in use still function, but the ring pairing cannot be reversed from K22 without a DC 16 Arcana check by a proficient spellcaster. |"
> — `campaign/structure/arc-i-kolat-towers.md:176`

**Alexandrian Kolat Towers PDF (printed p. 94; [check with pdftotext])**
> "Area K14 – Servants' Quarters: Sidra Romeir also bunks in this room (in a larger bed opposite the four bunk beds used by the thugs she bunks with). She keeps her *teleporter signet ring* in the locked drawer in the bedside table."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 94 (PDF page 3)

> "Inside the Astral Vault: The vault contains the Eye, 5 *pass-amulets*, a dozen *teleporter signet rings*, and *Manshoon's Report on the Grand Game* (see Part 6D)."
> — same PDF, printed p. 94

> "* Has a *teleporter signet ring*."
> — same PDF, printed p. 94 (footnote to the roster, where "Sidra Romeir + 2 thugs" is marked with an asterisk)

**Rank and tenure in the Splinter**
> "He spent two years building the Splinter cell — the faction that bears his name but operates independently of the Zhentarim's surviving leadership."
> — `campaign/structure/arc-i-kolat-towers.md:15`

> "He spent about two years building the Splinter, a cell that bears his name and works independently of the Zhentarim's surviving leadership."
> — `campaign/setting/villains/manshoon.md:33`

> "- Sidra Romeir is his most trusted lieutenant and holds the teleport rings when lieutenants leave the towers. At Lockdown she locks down Kolat Towers."
> — `campaign/setting/villains/manshoon.md:74`

> "- **Sidra Romeir** — Calishite human veteran, lawful evil, and Manshoon's most trusted lieutenant, stationed at Kolat Towers. She holds the teleport rings when lieutenants leave the Towers, and if captured lieutenants are killed she gives their rings to Kaevja `[research]`. See the **Sidra Romeir** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:97`

**Relationships (named people)**
- Manshoon (campaign): "**Relationships.** Sidra is Manshoon's Kolat Towers lieutenant, the keeper of the teleporter ring system, and the only person in the cell whose loyalty Manshoon has never tested, because testing it would mean he does not already know the answer." — `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:25`
- Manshoon (published): "{@creature Manshoon|WDH} gives these rings to his most trusted servants." — `sources/adventure-wdh.json:28822` (quoted in full above)
- Manafret Cherryport (campaign): "In a fight, Sidra waits for the intruders to commit before she draws. Once she draws, she calls for Manafret Cherryport, picks a defensible position, and does not leave it." — `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:23`. Published basis: "Combat in this area draws the attention of {@creature Manafret Cherryport|wdh} in {@area K3|3de}, who investigates." — `sources/adventure-wdh.json:28155`
- Kaevja Cynavern (campaign org line, tagged `[research]`): quoted under "Rank and tenure" above (`09-manshoons-zhentarim.md:97`). Kaevja's page: "**Relationships.** Kaevja is Sidra Romeir's sanctum counterpart in E3, Manshoon's primary early-warning mechanism, a mage whose communications role matters more than her combat capability, and the party's most time-sensitive priority target in the extradimensional sanctum." — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:25`. Published placement: "{@creature Kaevja Cynavern|wdh} (see {@area E3|41b})" — `sources/adventure-wdh.json:29957`.
- Two subordinates (unnamed): "two subordinates (LE male Tethyrian human {@creature thug||thugs})" — `sources/adventure-wdh.json:28155`. Alexandrian p. 94 roster: "Sidra Romeir + 2 thugs" [check with pdftotext]. Alexandrian p. 94 K14 entry: "the thugs she bunks with" (quoted above).

**Faith**
> "The campaign files give the cell no creed, oath or rites."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:46` (the bullet begins "- **Doctrine and Rites:** `[research]`")

No source gives Sidra a faith. See F5.

**Signature belonging**: the teleporter ring. Published: `sources/adventure-wdh.json:28156` ("Sidra wears a {@item teleporter ring|WDH}…"). Alexandrian: printed p. 94, locked drawer (quoted above). Campaign: `09-manshoons-zhentarim.md:97` and `04-sidra-romeir.md:21`.

**Name and pronunciation**
> "Sidra Romeir" / "SID-rah roh-MEER"
> — `sources/adventure-wdh.json:297` and `:298` (Pronunciation Guide list entry: `[ "Sidra Romeir", "SID-rah roh-MEER" ]`)

**Pronouns**: "she/her" (`04-sidra-romeir.md:5`, quoted in B).

---

## B. Alignment, species, pronouns, stat block

**Published adventure** (`sources/adventure-wdh.json:28155`, quoted in full in A): "(LE female Calishite human {@creature veteran})". Pronoun basis: "female". Stat block: `veteran`.

**Notable Figures page** (`campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md`):
- Line 5: "> - *Calishite human veteran, lawful evil, she/her*. Stat block: **Veteran**."
- Line 6: "> - **Affiliation:** Manshoon's Zhentarim"
- Line 7: "> - **Featured in:** **Faction Outposts**, **Kolat Towers**" (see C and D10)

**Organization page**, line 97 (`campaign/setting/organizations/09-manshoons-zhentarim.md:97`): "**Sidra Romeir** — Calishite human veteran, lawful evil, and Manshoon's most trusted lieutenant, stationed at Kolat Towers." (full line in A)

**Alexandrian Kolat PDF**, printed p. 95, stat reference [check with pdftotext]:
> "Sidra Romeir (LE female Callishite human) – veteran, MM p. 350"
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p. 95. The spelling "Callishite" is the PDF's. The adventure and both campaign files say "Calishite" (see D2).

**Pronoun and ethnicity tables already in the repo**
> "| Sidra Romeir | manshoons-zhentarim/04-sidra-romeir.md:5 | she/her | prose (\"her unhurried calm\", \"she has outlasted every other lieutenant\") | High |"
> — `docs/plans/npc-pronouns-table-group-c.md:48`

> "| Sidra Romeir | 28155 | `(LE female Calishite human {@creature veteran})` | campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:6 `Calishite human veteran, lawful evil` — agrees |"
> — `docs/plans/faerun-ethnicities-research.md:334` (this file cites line 6 for the summary line, which is line 5; see E5)

**Voice profile**: `.claude/skills/character-voices/voices/manshoons-zhentarim.md:67`: "### Sidra Romeir"

**Skill index**: "| `voices/manshoons-zhentarim.md` | Manshoon, Floxin, Vevette, Sidra, Agorn, Avareen, Zorbog, Amath, Vira, Manafret, Kaevja, Havia, Mookie, Yorn |" — `.claude/skills/character-voices/SKILL.md:34`

---

## C. Current page: sentences that narrate a quest event or a day-one conflict

The current page is `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md`. Each sentence is listed with its line.

- **Line 7, Featured in**: "> - **Featured in:** **Faction Outposts**, **Kolat Towers**". Quest bullet. Kolat Towers is sourced (`campaign/structure/arc-i-kolat-towers.md:104` and the rest of E2). **Faction Outposts is unsourced for Sidra**: no Sidra line exists in `campaign/structure/arc-e-faction-outposts.md`, in `sources/5. Faction Outposts.pdf` (the Zhentarim outposts at printed pp. 45–46 name Avareen, Zorbog, Ott Steeltoes, Amath Sercent and Agorn Fuoco; not Sidra), or in `sources/Act_III_Arc_E.md`.
- **Line 11, Resonance** (quest-time framing): "Sidra should inspire wariness with her unhurried calm (she has seen worse than the party and it shows), respect for the way she runs Kolat Towers like a barracks, and frustration with a loyalty to Manshoon that no argument will crack." The clause "than the party" refers to the PCs. Restate as a day-one fact if kept. No source for "seen worse".
- **Line 13, Emotions**: no quest-time clause. Campaign-only text.
- **Line 15, Motivations**: no quest-time clause. Campaign-only text.
- **Line 21, Persona**, sentence 1 (quest-time framing): "To the world, Sidra is a Calishite veteran who assumes intruding PCs are guests of Manshoon, since Kolat Towers' force field screens out riffraff." The published basis is `sources/adventure-wdh.json:28155`. "Intruding PCs" is the quest-time part; the day-one form is "intruders".
- **Line 21, sentence 2**: "She offers water, asks their business, and watches their hands." Campaign text, matching the voice profile (`voices/manshoons-zhentarim.md:72`, `:75`). No published line.
- **Line 21, sentence 3**: "To those she trusts, she holds the teleport rings when lieutenants leave the Towers and hands them to replacements without ceremony when the previous holder does not come back." Campaign text. Unsourced in detail (see D7 and F3).
- **Line 21, sentence 4**: "Deep down, she has outlasted every other lieutenant Manshoon has employed." Campaign-only; no source gives her tenure or other lieutenants' tenure.
- **Line 21, sentence 5**: "She does not wonder why." Campaign-only. Repeated in the voice profile (`voices/manshoons-zhentarim.md:77`).
- **Line 23, Morale**: "In a fight, Sidra waits for the intruders to commit before she draws. Once she draws, she calls for Manafret Cherryport, picks a defensible position, and does not leave it." Combat behaviour. The published basis is only the K2 entry (`sources/adventure-wdh.json:28155`). The tactic is campaign text. Not a quest event; keep as "Morale" text.
- **Line 25, Relationships**: "Sidra is Manshoon's Kolat Towers lieutenant, the keeper of the teleporter ring system, and the only person in the cell whose loyalty Manshoon has never tested, because testing it would mean he does not already know the answer." Campaign text. "keeper of the teleporter ring system" matches `arc-i-kolat-towers.md:176`. "the only person … never tested" has no source.
- **Line 29, Overview**: "A Calishite veteran who staffs the ground floor of Kolat Towers. She treats unexpected visitors with professional courtesy — offering water, asking their business, and watching their hands." "Ground floor" fits the campaign's K1 "Ground-Floor Entrance" and Sidra's K2 posting (`arc-i-kolat-towers.md:122`, quoted in E2).

**Quest-time clauses in the voice profile** (`.claude/skills/character-voices/voices/manshoons-zhentarim.md`, Sidra block; ruling 16 applies):
- Line 79, Greeting: "You made it through the field, so you're expected. Water? Your business, guest?" The clause "You made it through the field, so you're expected" presumes the party has crossed the force field. Restate for ruling 16 if kept. The published force-field passage is `sources/adventure-wdh.json:28155`.
- Line 74, Personality in speech: "She assumes intruders are guests and speaks accordingly." Day-one; no change needed.
- Line 80, Business: "The ring goes to whoever replaces the last one. That's how it works here." Day-one practice; no change needed.
- Line 81, Under pressure: "Hands where I can see them. I've done this longer than you've been alive." Day-one; no change needed.
- Line 73, Swearing: "One flat \"shit\" when something breaches the Towers." Day-one (conditional).

**Quest-time text on other pages that names Sidra** (routed, not for the setting page): the escalation and timeline rows in E2 and E3, and the published "Report Manshoon" passage (`sources/adventure-wdh.json:26763`, "can be captured and turned over for interrogation"). The Thrakkus cart is a rejected chain (E1).

---

## D. Conflicts (both sides quoted)

**D1. Where Sidra is posted in the towers**
- Published: K2 "Dining Room" (`sources/adventure-wdh.json:28137`) with Sidra in it (`:28155`, quoted in A).
- Campaign: "**K1 — Ground-Floor Entrance.** The front door. Only relevant for pass-amulet entry. A Zhentarim thug behind a viewing port opens it if the amulet check passes, admits the visitors to the narrow entry hall, and moves to alert Sidra in K2. At Unaware tier, this happens without alarm. At Suspicious and Alert, the thug calls for Sidra before the door is fully open." (`campaign/structure/arc-i-kolat-towers.md:122`). Also "| 0 min | Alarm triggers. Sidra activates internal response in K2. All NPCs shift to defensive positions. Kaevja in E3 casts sending (if not yet eliminated). |" (`arc-i-kolat-towers.md:174`).
- Alexandrian: "Area K14 – Servants' Quarters: Sidra Romeir also bunks in this room…" (printed p. 94 [check with pdftotext]).
- Published K14: "K14. Servants' Quarters" (`sources/adventure-wdh.json:28514`, page 153). The room text reads: "Four Zhent {@creature thug||thugs} relax here-one trying to rest, two others playing cards, and the fourth sitting on the edge of a bed, re-stringing a heavy crossbow." (`:28523`). Sidra is not named in the published K14.
- Higher-ranked: the campaign structure doc (`arc-i-kolat-towers.md`) places her in K2. The campaign page names no room. The K14 bunk is the Alexandrian's detail only.

**D2. Species spelling**
- Published and campaign: "Calishite" (`sources/adventure-wdh.json:28155`; `04-sidra-romeir.md:5`; `09-manshoons-zhentarim.md:97`).
- Alexandrian: "Callishite" (printed p. 95 [check with pdftotext]).
- Higher-ranked: campaign and published agree on "Calishite". The Alexandrian spelling is probably a typo.

**D3. The ring: worn, locked away, or held**
- Published: "Sidra wears a {@item teleporter ring|WDH}" (`sources/adventure-wdh.json:28156`).
- Alexandrian: "She keeps her *teleporter signet ring* in the locked drawer in the bedside table." (printed p. 94 [check with pdftotext]).
- Campaign: "she holds the teleport rings when lieutenants leave the Towers" (`04-sidra-romeir.md:21`); "Sidra Romeir holds the rings when lieutenants leave the Towers" (`09-manshoons-zhentarim.md:41`); "Sidra locks the teleporter ring system" (`arc-i-kolat-towers.md:176`).
- Higher-ranked: campaign. The campaign says she holds the rings for the system. It does not say she wears one. The drafter must choose a wording.
- Related: "Manshoon's lieutenants wear special rings that let them access Manshoon's sanctuary atop the Outer Tower (although they don't know that this is actually an extradimensional space; they think he just lives up there)." (Alexandrian, printed p. 95 [check with pdftotext]). The campaign says the apprentices "wear teleporter rings" (`09-manshoons-zhentarim.md:54`). The published text says "Manshoon gives these rings to his most trusted servants" (`:28822`).

**D4. Who knows about the Cassalanters' Eye (day-one knowledge)**
- Alexandrian, printed p. 96 [check with pdftotext]: "Manshoon's lieutenants know what the apprentice wizards know, but also: • The layout of the extradimensional sanctum, including the location of the astral vault. • That the Cassalanters are the noble family who possess the third Eye."
- Same page, the apprentices' list: "That the *Stone of Golorr* was blinded and Manshoon is attempting to find its three Eyes. He already has one. He once had another that was stolen by Xanathar. And he has recently identified that a local noble family has the third. (They don't know the identity of the noble family.)"
- Campaign: the cell's day-one row, `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:25`: "| Manshoon's Zhentarim | The Stone exists and unlocks great wealth; Urstul Floxin's team was tracking Dalakhar; does not yet know the Stone reached the Gralhunds | Nothing | Stone + all three Eyes |". It names no Cassalanter knowledge, and it does not say whether lieutenants know the Cassalanters hold an Eye.
- Campaign on the Eyes: "Manshoon holds no Eye, following `running-the-villains.md` line 30, `arc-e-faction-outposts.md` line 65 and `arc-i-kolat-towers.md` line 57." (`campaign/setting/villains/manshoon.md:125`, Draft Notes). So the Alexandrian "He already has one" conflicts with the campaign. Decision for the orchestrator.
- The Cassalanter secrecy rule concerns the pact, not the Eye.
- Table date: "The table holds on the morning of Ches 22, when **Fireball!** opens, because the Xanathar and Manshoon cells assume Dalakhar has already taken the Stone from Xanathar's lair." (`what-each-faction-knows-at-start.md:8`). The row is therefore not a Ches 1 table.

**D5. Ward of Kolat Towers**
- Published: "{@creature Manshoon|WDH} lurks in Kolat Towers, a pair of wizards' towers in the Trades Ward." (`sources/adventure-wdh.json:560`)
- Published, later: "in the city's Southern Ward" (`sources/adventure-wdh.json:32215`); "a crumbling residence in the Southern Ward" (`:32218`).
- Campaign: "Manshoon's Zhentarim, which outsiders call the Splinter, is a cell of the Black Network that answers only to Manshoon, who rules it from Kolat Towers in the Southern Ward." (`campaign/setting/organizations/09-manshoons-zhentarim.md:15`)
- Higher-ranked: campaign (Southern Ward). The Sidra page does not name a ward.

**D6. Stat block and alignment**: no conflict. "Veteran", "lawful evil" and "female" agree in `sources/adventure-wdh.json:28155`, `04-sidra-romeir.md:5` and `09-manshoons-zhentarim.md:97`. The Alexandrian gives "LE female Callishite human ... veteran, MM p. 350" (printed p. 95 [check with pdftotext]).

**D7. Rings given to Kaevja**
- Campaign org page: "if captured lieutenants are killed she gives their rings to Kaevja `[research]`" (`09-manshoons-zhentarim.md:97`).
- Published: no such line. The published rings entry is `sources/adventure-wdh.json:28822` (quoted in A).
- Pass 5 notes: "Holds the teleport rings when lieutenants leave the Towers. If captured lieutenants are killed, Sidra gives their rings to Kaevja." and "The second sentence of the org line has no source." (`docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:254` and `:260`).
- Also, the org page's Trust bullet gives the ring-holding sentence with no tag (`09-manshoons-zhentarim.md:41`, quoted in A).

**D8. "Most trusted"**: the campaign says "most trusted lieutenant" (`manshoon.md:74`; `09-manshoons-zhentarim.md:97`). The published text says "his most trusted servants" for rings only (`sources/adventure-wdh.json:28822`). The phrase "most trusted lieutenant" is campaign-only.

**D9. Two Zhentarims callout**: no conflict, but a rule the drafter must keep (H).

**D10. "Featured in: Faction Outposts"**: unsourced for Sidra (see C, line 7).

**D11. Kaevja's posting**: campaign says "sanctum counterpart in E3" (`11-kaevja-cynavern.md:25`). Published has "E3. Guard Station" (`sources/adventure-wdh.json:29988`), where "Unless she has been drawn elsewhere, {@creature Kaevja Cynavern|wdh} stands watch in front of the window." (`:29992`). Sidra is in K2 in the towers. The "counterpart" phrase is campaign text.

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Thrakkus cart (rejected chain)**
- Published: "The corpses are brought to him in the dead of night, most often delivered by Sidra Romeir (see chapter 8, {@area K2|3db}) in a covered cart pulled by a draft horse." (`sources/adventure-wdh.json:13377`, Winter chain, DH page 89)
- Campaign rejection: "Dragon Heist has Zhents loyal to Manshoon pay Thrakkus to chop up the people they kill, and he sells the meat on the sly. The published text has Sidra Romeir deliver the bodies at night in a covered cart. This is the published Winter chain, and no campaign file adopts it." (`campaign/gazetteer/waterdeep/field-ward.md:106`)
- Also: "> - **Left out:** The Snobeedle family and Blossom Snobeedle's visit to the empty Shunners' cellar in **The Missing Snobeedle**, Darrick Holstan's later arrest, the Undercliff Scarecrows (Undercliff, not this ward), and Sidra Romeir's Notable Figures page." (`campaign/gazetteer/waterdeep/field-ward.md:246`)

**E2. Kolat Towers quest-time schedule (routed to **Kolat Towers**; arc-i is pending conversion)**
- `campaign/structure/arc-i-kolat-towers.md:101`: "| Unaware | Standard; gaps on normal rotation | Standard roster; Sidra assumes visitors are guests until credentials fail | Manshoon studying in E13; simulacrum dormant in E7 | 30 min |"
- `:102`: "| Suspicious | Gaps shifted 15 min from diagram; amulets work | +2 thugs at K2; Sidra checks credentials before allowing passage | Manshoon studying in E13; simulacrum dormant in E7 | 25 min |"
- `:104`: "| Lockdown | Gaps sealed; only fresh amulets work; Yellowspire circle still functions | Full garrison at battle stations; Sidra does not ask questions | Manshoon in E12, defensive spells prepared; simulacrum activated in E1, briefed on party capabilities via Skeemo's intelligence if he survived **Faction Outposts** | 15 min |"
- `:122`: quoted in D1.
- `:174`: "| 0 min | Alarm triggers. Sidra activates internal response in K2. All NPCs shift to defensive positions. Kaevja in E3 casts sending (if not yet eliminated). |"
- `:176`: quoted in A.
- `:184`: "At Suspicious, reduce to 25 minutes (Kaevja receives an earlier sending confirmation, Sidra's standing orders are more aggressive)."

**E3. Escalation (routed to the Factions Guide and the GM Guide)**
- `campaign/guides/factions/10-manshoons-zhentarim.md:54`: "| Lockdown | Urstul's team if the others fail; Manshoon issues personal directives by flying snake. Manshoon's simulacrum engages; Sidra locks down Kolat Towers |"
- `campaign/guides/gm-guide/running-the-villains.md:50`: "| **Manshoon's Zhentarim** | Normal operations | Flying snake courier network active; Agorn Fuoco and Avareen Windrivver file field reports. Urstul Floxin reviews them | Agorn Fuoco or Vevette Blackwater's team; orders are to capture, not kill | Urstul Floxin's team if the others fail; Manshoon issues personal directives by flying snake. Manshoon's simulacrum engages; Sidra Romeir locks down Kolat Towers |"
- `campaign/setting/villains/manshoon.md:74`: quoted in A ("At Lockdown she locks down Kolat Towers.").

**E4. No Sidra in the revelation lists**
- Factions Guide: `campaign/guides/factions/10-manshoons-zhentarim.md`, section "## Revelation List" (lines 58–78), read in full. No entry names Sidra. The guide's only Sidra mention is line 54 (E3).
- Alexandrian `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p. 124 (Zhentarim Locations) [check with pdftotext]: the headings "ZHENTARIM INTERROGATION HOUSE", "YELLOWSPIRE" and "LAIR: KOLAT TOWERS" carry entries that name no Sidra. The Kolat entries are "Xanathar's Report on the Grand Game (Xanathar's Lair)", "Cassalanter's Report on the Grand Game (Cassalanter Villa)", "Teleportation circle (Yellowspire)", "Capturing Agorn Fuoco (Response Team: Agorn Fuoco)" and "Questioning Samara (Xanathar's Lair)".
- The pass 5 notes say the opposite: "Urstul, Sidra and Agorn carry the revelation-list items named in the Factions Guide (Section 5)." (`docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:136`). Neither file supports this.

**E5. Stale citation in another file**
- `docs/plans/faerun-ethnicities-research.md:334` cites the summary line as `04-sidra-romeir.md:6`. The summary line is line 5 (`04-sidra-romeir.md:5`).

**E6. Other references that name Sidra (no content to route)**
- `campaign/setting/history/04-the-founding-of-chains.md:129`: "- **Davil Starsong**, **Tashlyn Yafeera**, **Istrid Horn**, **Skeemo Weirdbottle**, **Ziraj the Hunter**, **Sidra Romeir**, **Urstul Floxin**, **Jelenn Urmbrusk**, **Lady Gondafrey**: the people named here." (context not read in this pass)
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:26`: "**Relationships.** Manshoon is the leader of the Zhentarim splinter cell, the employer of Urstul Floxin, Sidra Romeir, and Vevette Blackwater, a blackmailer of Masked Lords Jelenn Urmbrusk and Corylus Thann, and a clone-wizard whose response teams are deliberately the weakest in muscle because drawing attention is the one mistake he will not make twice."
- `campaign/setting/villains/manshoon.md:116` and `campaign/setting/organizations/09-manshoons-zhentarim.md:152`: Sidra appears in cross-reference bullets only.
- `campaign/structure/arc-i-kolat-towers.md:320`: "- **Notable Figures** — Existing profiles: Manshoon, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin, Lady Gondafrey, Skeemo Weirdbottle. New profiles needed: Kaevja Cynavern, Havia Quickknife, Mookie Plush, Yorn the Terror."
- `sources/SOURCE_GUIDE.md:35`: "- **Chapter 8 — Face of the Enemy (Manshoon/Zhentarim):** Kolat Towers keyed location (22 areas, force field mechanics, pass-amulet system, teleporter signet rings) and the Extradimensional Sanctum (13 areas, Manshoon's personal stronghold). Contains: Manshoon, his simulacrum, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin."
- `campaign/guides/factions/10-manshoons-zhentarim.md:7`: "Every lieutenant carries a pass-amulet to Kolat Towers and will try to destroy it if capture seems certain, except Agorn, who trades his to save himself." Sidra is a lieutenant by the campaign's usage. The Sidra page does not mention a pass-amulet. The Alexandrian p. 94 asterisk marks rings, not amulets.
- `campaign/guides/trollskull-manor/08-notable-patrons.md:30` names a different "Calishite Zhentarim" (Ziraj). It is not Sidra.

---

## F. Gaps a Background would need (no source gives these)

For each gap: the sourced facts the drafter must stay consistent with, then a suggested modest inference. The suggestions are for the orchestrator to decide.

**F1. Origin, birthplace, family, age.**
- Consistent with: "Calishite human" and "female" (`sources/adventure-wdh.json:28155`). No file gives a birthplace. Ruling 5 allows a Faerûn ethnicity and no city.
- Suggested [design]: a nameless family or early place, with no named NPC (ruling 17).

**F2. Formative events.**
- Consistent with: "protective possessiveness toward the teleport ring system" and "a patience that comes from knowing where the exits are" (`04-sidra-romeir.md:13`); the K14 bunk and locked drawer (Alexandrian p. 94 [check with pdftotext]).
- Suggested [design]: one event that explains the ring habit, for example a ring holder who did not come back (F7).

**F3. How she joined and rose.**
- Consistent with: the open recruitment policy (`sources/adventure-wdh.json:1443`); "His lieutenants rise by impressing him" (`09-manshoons-zhentarim.md:71`); "These lieutenants include Sidra Romeir" (`sources/adventure-wdh.json:26763`).
- No file says how she came to the Towers. The Splinter is about two years old (`arc-i-kolat-towers.md:15`, quoted in A), so any tenure she has is at most that unless she served Manshoon before the Splinter.
- Suggested [research] inference: her post dates the Splinter's founding. The campaign's "outlasted every other lieutenant" (`04-sidra-romeir.md:21`) fits that, but it gives no date.

**F4. Rank and tenure.**
- Consistent with: "Manshoon's Kolat Towers lieutenant" (`04-sidra-romeir.md:25`); "his most trusted lieutenant" (`manshoon.md:74`, campaign-only). The only rank word used for the cell's members is "lieutenant", as in "Manshoon lieutenant" for Agorn (`09-manshoons-zhentarim.md:99`).
- Size and ranks bullet, `09-manshoons-zhentarim.md:60`: "- **Size and ranks:** `[research]` No source counts the cell's members or gives it rank titles beyond \"lieutenant\"."

**F5. Faith.**
- Consistent with: "The campaign files give the cell no creed, oath or rites." (`09-manshoons-zhentarim.md:46`). The same bullet cites the wiki for Bane as the Zhentarim's favored deity, tagged `[research]`, and says: "Nothing in the campaign makes Bane the faith of the cell as a whole."
- Suggested: write no deity, or [design] an unnamed belief. Do not name Bane.

**F6. Relationships outside the cell.**
- Consistent with: Manafret Cherryport (`04-sidra-romeir.md:23`; `sources/adventure-wdh.json:28155`); the two unnamed thugs (`:28155`); Kaevja (D7, D11). No other named tie exists.
- Any new named person is barred by ruling 17.

**F7. Losses.**
- Consistent with: "hands them to replacements without ceremony when the previous holder does not come back" (`04-sidra-romeir.md:21`). The line implies earlier holders who did not return. It names none and dates none.

**F8. Personal goals.**
- No source gives Sidra a personal goal. Her Motivations (`04-sidra-romeir.md:15`) and the Splinter's goals (`manshoon.md:80`) are faction goals, and they stay as written.
- Suggested [design] candidates, to be checked against ruling 17's limits: (a) to keep the two thugs she bunks with out of Manshoon's way (the K14 detail, Alexandrian p. 94 [check with pdftotext]); (b) a personal reason to keep her own ring out of other hands, which needs a motive beyond Motivations; (c) to leave the Towers with something of her own. Any choice must not reveal where the ring is kept, because that would change play.

**F9. The ring: which wording to use.**
- See D3. Campaign files say "holds"; the published text says "wears"; the Alexandrian says "locked drawer".

**F10. Knowledge of the Eyes and the Cassalanters.**
- See D4. The campaign is silent on lieutenants' knowledge. The Alexandrian (p. 96) says they know.

**F11. Calishite origin and the ethnicity rule.**
- Ruling 5 applies. "Calishite" is the published ethnicity word (`sources/adventure-wdh.json:28155`). Other campaign uses of "Calishite" are for other people or for an atmosphere (`campaign/gazetteer/waterdeep/southern-ward.md:154`: "the best Calishite singers"). No file gives a Calishite city.

**F12. Pronunciation.** Supplied in A: "SID-rah roh-MEER" (`sources/adventure-wdh.json:298`).

**F13. Inspirations.** Campaign-authored (`04-sidra-romeir.md:17`). Not a source fact.

---

## Model pages (format and tagging, for the drafter)

- `campaign/setting/notable-figures/xanathars-guild/12-grevik-nass.md` (Grevik Nass): Background at line 14. The `[research]` tag marks sourced inferences (line 16). The `[design]` tag marks invented material (lines 18–22). "**Personal goals.**" is at line 24. The Voice block is at lines 55–70. The Draft Notes list each `[design]` sentence under "Design:" (lines 126–131).
- `campaign/setting/notable-figures/xanathars-guild/08-keln-trigos.md` (Keln Trigos): Background at lines 14–32. "**Personal goals.**" is at line 32. A `> [!gamemaster]**Secret**` callout (lines 85–87) is used only where a hidden fact changes play. Sidra has no hidden fact in any source, so the Secret block may be left out. The Draft Notes "Design:" list is at lines 137–144.
- Both pages record "Voice" as copied from the skill profile (Grevik line 125; Keln line 135).

---

## G. Source hints at Sidra's inner life (quoted; do not contradict)

- "(she has seen worse than the party and it shows)" — `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:11`
- "earned pride in how the Towers run, protective possessiveness toward the teleport ring system, flat contempt for people who mistake her calm for softness, and a patience that comes from knowing where the exits are." — `04-sidra-romeir.md:13`
- "Deep down, she has outlasted every other lieutenant Manshoon has employed. She does not wonder why." — `04-sidra-romeir.md:21`
- "Once she draws, she calls for Manafret Cherryport, picks a defensible position, and does not leave it." — `04-sidra-romeir.md:23`
- "Sidra is Manshoon's Kolat Towers lieutenant, the keeper of the teleporter ring system, and the only person in the cell whose loyalty Manshoon has never tested, because testing it would mean he does not already know the answer." — `04-sidra-romeir.md:25`
- Voice, Never: "She never panics, never gives up the rings, and never wonders why she outlasted the others." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:77`
- Voice, Quirks: "She offers water first. She looks at people's hands, not their faces." — `manshoons-zhentarim.md:75`
- Voice, Word choice: "Barracks plainness with hospitality: water, business, \"the master's guests\". She calls people \"guest\" until they aren't." — `manshoons-zhentarim.md:72`
- Voice, Under pressure: "Hands where I can see them. I've done this longer than you've been alive." — `manshoons-zhentarim.md:81`
- Published: "Three Zhents in black armor sit around a stone dining table, playing Three-Dragon Ante (a card game). The table is set with silver." — `sources/adventure-wdh.json:28145`
- Published: "Since the force field around Kolat Towers keeps out riffraff, Sidra assumes the characters are guests of {@creature Manshoon|WDH} arriving for a clandestine meeting. If the characters give her no reason to believe otherwise, she and her thugs escort them wherever they ask to go." — `sources/adventure-wdh.json:28155`
- Alexandrian, printed p. 94: "Sidra Romeir also bunks in this room (in a larger bed opposite the four bunk beds used by the thugs she bunks with). She keeps her teleporter signet ring in the locked drawer in the bedside table." [check with pdftotext]
- Org page: "Sidra Romeir holds the rings when lieutenants leave the Towers and hands them to replacements when a holder does not come back." — `09-manshoons-zhentarim.md:41` (see D7 on sourcing)

---

## H. Two Zhentarims and voice rules that bind this page

- Org page callout, line 19: "Two cells operate in Waterdeep, and Davil Starsong's **Doom Raiders** are the player-joinable one, covered on the organization page **The Zhentarim (Doom Raiders)**. Manshoon's splinter is a completely separate organization that peeled off from the Doom Raiders' local network when he returned to Waterdeep `[research]`, and the two groups dislike each other. Anyone who deals with the Zhentarim through Davil is dealing with the Doom Raiders and not with Manshoon. The villains on this page answer only to Manshoon." — `campaign/setting/organizations/09-manshoons-zhentarim.md:19`
- Villains callout, line 19: "Manshoon's splinter cell and Davil Starsong's Doom Raiders are entirely separate organizations. They share a name and a history and nothing else. Never conflate them in NPC dialogue." — `campaign/setting/villains/manshoon.md:19`
- Voice profile callout, line 5: "> **Two Zhentarims:** these characters never talk as if they were the Doom Raiders, and never refer to Davil's people as colleagues. To them, Davil's cell is \"the old guard\" at best." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:5`
- Campaign name for the cell, org line 15: "Manshoon's Zhentarim, which outsiders call the Splinter, is a cell of the Black Network that answers only to Manshoon, who rules it from Kolat Towers in the Southern Ward." — `09-manshoons-zhentarim.md:15`
- Cassalanter row, villains line 65: "| The Cassalanters | Missed opportunity | Manshoon is as suspicious of their wealth and spotless name as everyone else, and an arrangement with them could have given him leverage; he chose independence over shared control `[research]` |" — `campaign/setting/villains/manshoon.md:65`. No Sidra line touches the pact. The Alexandrian p. 96 line on the third Eye is the only Sidra-adjacent Cassalanter text (D4).
- Bregan D'aerthe, Lolth and Xanathar-is-"it": no Sidra line mentions any of them.

---

## I. Cross-references (every file:line where Sidra appears)

- `.claude/skills/character-voices/SKILL.md:34` (quoted in B)
- `.claude/skills/character-voices/voices/manshoons-zhentarim.md:5`, `:67`–`:81` (quoted)
- `campaign/gazetteer/waterdeep/field-ward.md:106`, `:246` (E1)
- `campaign/guides/factions/10-manshoons-zhentarim.md:54` (E3)
- `campaign/guides/gm-guide/running-the-villains.md:50` (E3)
- `campaign/setting/history/04-the-founding-of-chains.md:129` (E6)
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:26` (E6)
- `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:1`, `:5`, `:6`, `:7`, `:11`, `:13`, `:15`, `:17`, `:21`, `:23`, `:25`, `:29` (the page itself)
- `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:25` (D11)
- `campaign/setting/organizations/09-manshoons-zhentarim.md:8`, `:15`, `:19`, `:41`, `:46`, `:54`, `:60`, `:71`, `:97`, `:99`, `:152` (Sidra cited at `:8`, `:41`, `:54`, `:71`, `:97`, `:152`; the rest are for context)
- `campaign/setting/villains/manshoon.md:33`, `:65`, `:74`, `:116`, `:125`
- `campaign/structure/arc-i-kolat-towers.md:15`, `:101`, `:102`, `:104`, `:122`, `:174`, `:176`, `:184`, `:320`
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:8`, `:25`
- `docs/plans/faerun-ethnicities-research.md:334` (E5)
- `docs/plans/npc-pronouns-table-group-c.md:48`
- `docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:136`, `:188`, `:254`, `:260`
- `sources/SOURCE_GUIDE.md:35`
- `sources/Appendix_D_-_Running_the_Tavern.md:1320`: "1. Lights have been seen in Kolat Towers, the Zhentarim's abandoned wizard's tower in the Southern Ward. She mentions this as though it were a footnote. It is not a footnote." (no Sidra; cross-reference to the Towers' reputation)
- `sources/adventure-wdh.json`: `:297`, `:298`, `:560`, `:1443`, `:1446`, `:13377`, `:26763`, `:28137`, `:28145`, `:28155`, `:28156`, `:28514`, `:28523`, `:28822`, `:29957`, `:29988`, `:29992`, `:32215`, `:32218`
- `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed pp. 94–95 (Sidra entries) [check with pdftotext]
- `sources/1. The Villains.pdf` printed p. 16 (no Sidra) and `sources/17. Outpost and Lair Revelation Lists.pdf` printed p. 124 (no Sidra) [check with pdftotext]
- `scratchpad/fandom-dump/forgottenrealms_pages_current.xml:3744301`, `:3744333` (wiki index only)

---

## J. Not found

Searched for `Sidra` or `Romeir`, or for the content listed:
- Wiki: `sources/research/**/wiki*.txt` (no hits); `scratchpad/wiki-manshoons-zhentarim/` (only `04-sidra-romeir.txt`, a NOT FOUND stub); `scratchpad/fandom-dump/forgottenrealms_pages_current.xml` (one index line, no article).
- Published adventure: `sources/adventure-wdh.json` (all hits listed in I). No line gives Sidra's birthplace, family, age, faith, a teacher, or how she joined. No line names a lieutenant she served under.
- Alexandrian markdown: a Grep for `Sidra|Romeir|Kolat|teleporter` across `sources/*.md` finds no Sidra hit in `Act_III_Arc_D.md`, `Act_III_Arc_E.md`, `Appendix_B_-_Player_Factions.md`, `Appendix_C_-_Player_Faction_Missions.md`, or `Appendix_D_-_Running_the_Tavern.md`.
- Alexandrian PDFs read in full for Sidra: `12. Lair  Zhentarim – Kolat Towers.pdf` (5 pages; printed 92–96); `1. The Villains.pdf` (7 pages; printed 13–19; no Sidra; the Zhentarim section is printed p. 16); `5. Faction Outposts.pdf` (13 pages; printed 36–48; the Zhentarim outposts are printed pp. 45–46; no Sidra); `17. Outpost and Lair Revelation Lists.pdf` (4 pages; printed 121–124; no Sidra).
- Campaign: a Grep for Sidra across `campaign/` lists only the files cited in B to I. `campaign/structure/arc-e-faction-outposts.md` has no Sidra line. No file in `campaign/quests/` has a Sidra line.
- Organization page `09-manshoons-zhentarim.md`: no line gives Sidra a birthplace, a faith, an age or a family.
- Faction Outposts has no quest journal yet (`campaign/structure/arc-e-faction-outposts.md` is the active structure doc).

---

## K. Not readable or not opened

- `sources/6. Faction Response Teams.pdf` (8 pages): **not opened in this pass**. The Factions Guide's response-team list names only Vevette, Agorn and Urstul (`campaign/guides/factions/10-manshoons-zhentarim.md:11`–`:13`). A check of this PDF for Sidra remains open.
- `sources/Other remix files/*.docx`: not opened (the tools cannot read .docx). `SOURCE_GUIDE.md:688` names a .docx only for the Doom Raiders ("Davil and the Doom Raider Zhents + Elf Killer mission and more.docx"). No .docx is listed for Sidra or Kolat Towers.
- Pass 5 notes at `docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:337` say the Villains and Kolat Towers PDFs "were not opened in this pass". This pass opened both (see J).

---

## Summary for the drafter (facts only)

- Name: Sidra Romeir, pronounced "SID-rah roh-MEER" (`sources/adventure-wdh.json:297`–`:298`).
- Calishite human veteran, lawful evil, female, she/her; stat block veteran (`sources/adventure-wdh.json:28155`; `04-sidra-romeir.md:5`).
- Published K2 posting with two thugs, playing cards; she wears a teleporter ring (`sources/adventure-wdh.json:28137`–`:28156`). The Alexandrian places her in K14 with the thugs, with the ring in a locked drawer (printed p. 94 [check with pdftotext]).
- Campaign: Manshoon's Kolat Towers lieutenant and keeper of the teleporter ring system (`04-sidra-romeir.md:25`; `arc-i-kolat-towers.md:176`).
- No source gives her origin, family, age, faith, or how she joined. Her Background has to be `[research]` or `[design]` throughout.
- Two Zhentarims rule: Manshoon's cell only (H).
- Quest-time text to restate or route: `04-sidra-romeir.md:11` ("than the party"), `:21` ("intruding PCs"); voice line 79 ("through the field, so you're expected"). Routed escalation text at `arc-i-kolat-towers.md:101`–`:104`, `:122`, `:174`–`:184`; `10-manshoons-zhentarim.md:54`; `running-the-villains.md:50`.
- Conflicts for the orchestrator: D1 (room), D3 (ring), D4 (Cassalanter Eye knowledge), D5 (ward), D7 (rings to Kaevja), D10 (Faction Outposts feature).
