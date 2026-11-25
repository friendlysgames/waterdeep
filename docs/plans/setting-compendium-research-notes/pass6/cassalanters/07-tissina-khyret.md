# Pass 6 research notes: Tissina Khyret

Page: `campaign/setting/notable-figures/cassalanters/07-tissina-khyret.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1, 3, 4, 5, 7, 15, 16, 17)
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/08-laiba-nana-rosse.md` (Section H is identical in both files)
Ruling used: Ches 1, 1492 DR. Cult status as `campaign/setting/organizations/10-cassalanters.md` gives it: **cult**. Cassalanter secrecy applies.

Method and caveats:
- Campaign files: Read and Grep, quoted from the file. Line numbers come from tool output.
- Published adventure: `sources/adventure-wdh.json`. Quotes are the JSON strings with escapes removed (`\"` shown as `"`). Tags such as `{@creature ...}` are left as written.
- Alexandrian PDF `sources/10. Lair  Cassalanter Villa.pdf` (two spaces in the name). No shell, so `pdftotext` did not run. Read as page images with the Read tool (PDF pages 3, 5 and 6). Printed page = PDF page + 76 (PDF 3 = printed 79; PDF 5 = printed 81; PDF 6 = printed 82). Every PDF quote is a transcription and needs a `pdftotext -layout` check before prose use.
- `sources/1. The Villains.pdf` read in full (7 PDF pages, printed 13 to 19). It names neither Tissina nor Nana.
- Wiki: `sources/research/pass4-bundles/cassalanters/wiki.txt` is the only Cassalanter wiki bundle (no pass5 bundle exists for this folder). Searched for Khyret, Tissina, Laiba, Rosse, Nana, servant, maid, cook, nanny, nurse and staff. No line names either figure. The extract `scratchpad/wiki-cassalanters/07-tissina-khyret.txt` reads `NOT FOUND`; this is confirmed.
- Not searched for household staff: `sources/5. Faction Outposts.pdf` (outpost-focused).
- No file was edited except this notes file. The page was not written. `voicecheck.py` not run.

---

## A. Background facts by theme

### A1. Origin, family, former life

No source gives Tissina's birth, home, family, parents or any trade before the household. Searched: adventure (name index `:205` and `:325`; `:18487` to `:18492`; `:20520` to `:20540`; `:22818`), Alexandrian Villa PDF (printed 79, 81, 82), the campaign files listed in Section H, and the wiki bundle (no line).

Only the physical and role facts exist:

> "Madame Khyret dresses in a long black gown and wears a headdress with black tassels. She is an aging tiefling {@creature cult fanatic}, and she spends most of her time in the master sitting room ({@area C19|31a})."
> — `sources/adventure-wdh.json:18492` (Head Servants, page 117)

> "{@creature Tissina Khyret|WDH}"
> — `sources/adventure-wdh.json:325` (name index; the pronunciation on the next line, `:326`, reads "teh-SEE-nah KYE-ret")

### A2. Role and title

> "Madame Khyret is the personal attendant to {@creature Ammalia Cassalanter|WDH} and is the family's chief housemaid."
> — `sources/adventure-wdh.json:18491`

> "Tissina Khyret (Chief Housemaid) – tiefling cult fanatic, MM p. 345 (DH p. 117)"
> — `sources/10. Lair  Cassalanter Villa.pdf`, printed p.82 [PDF p.6] (Stat Reference; image transcription)

> "- **Tissina Khyret** (cult fanatic, Ammalia's attendant) — devoted to Ammalia personally. Joined because Ammalia asked her to. Does not fully understand the contract's terms — she knows about the temple, attends gatherings, believes the worship is a family spiritual practice. If she learns the children's souls are forfeit, she breaks. DC 14 Charisma (Persuasion) with evidence of the contract turns her."
> — `campaign/structure/arc-g-cassalanter-villa.md:96` (Questioning Staff, Cult Staff; a structure document, authoritative until the Cassalanter Villa journal exists)

> "- **Tissina Khyret** — Tiefling cult fanatic (Asmodeus), lawful evil. See the **Tissina Khyret** page in Notable Figures."
> — `campaign/setting/organizations/10-cassalanters.md:99` (Key Members)

### A3. How she joined, and when

The reason is sourced. The date is not.

> "Joined because Ammalia asked her to."
> — `campaign/structure/arc-g-cassalanter-villa.md:96`

> "They came to the faith by different roads: Tissina out of loyalty to Ammalia, Nana Rosse to stay close to the twins, and Jandar through a debt to Victoro that became cult service (`arc-g-cassalanter-villa.md` lines 96-98)."
> — `campaign/setting/organizations/10-cassalanters.md:40` (Beliefs, "Service Is Worship"; the sentence before it reads "The cult's members fold devotion into the work they do for the family. Tissina Khyret attends Ammalia, Nana Rosse minds the twins, Jandar Chergoba cooks and Seffia Naelryke runs field operations, and none of them sees a conflict between the job and the god.")

> "- **Before Ches 1, 1492 DR, undated, the temple and the cult:** The temple of Siamorphe that lay beneath the estate was desecrated by the family's devil-worship and given to Asmodeus, and its thirty-foot statue was carved from an image of Siamorphe (*Dragon Heist*, 5e; **The Cassalanters** in Villains). Jandar Chergoba's debt to Victoro turned into cult service three years ago, which places some of the cult's household recruiting at the time of the bargain (`arc-g-cassalanter-villa.md` line 98). No source dates the temple's conversion, the cult's founding or the arrival of its other members `[research]`."
> — `campaign/setting/organizations/10-cassalanters.md:27` (History)

> "The cult's founding, the temple's conversion and when each member joined are undated in every campaign file, so the History entry for them carries `[research]`."
> — `campaign/setting/organizations/10-cassalanters.md:178` (Draft Notes, Research)

> "- **About 1489 DR, the bargain:** Victoro and Ammalia Cassalanter are Waterdeep aristocrats who made a devil's bargain."
> — `campaign/setting/organizations/10-cassalanters.md:25` (History; the full bullet is the bargain account, quoted in Section F3)

### A4. Tenure and the household's replacement of servants

No source gives how long Tissina has served Ammalia. The adventure makes personal attendants the exception to the household's regular replacement of servants:

> "With the exception of their personal attendants, the Cassalanters replenish their servants regularly. Most move on to other jobs, but occasionally a servant discovers the secret vault ({@area C29|330}), visits the forbidden attic ({@area C24|325}), or otherwise learns too much. Such folk are fated to become sacrifices to Asmodeus."
> — `sources/adventure-wdh.json:18598` (Denizens of Cassalanter Villa, page 118)

Willifort's own tenure, quoted so that Tissina's Background does not contradict it:

> "A personal attendant is one of the few servants whom the family keeps on while it replaces the rest regularly (*Dragon Heist*, 5e), and Willifort made himself useful to Lord Victoro so early that nobody has ever had cause to replace him `[design]`."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:22`

### A5. Relationships to named figures

**Ammalia (the one she serves):**

> "- **Tissina Khyret:** Her personal attendant and the family's chief housemaid, who joined the cult because Ammalia asked her to."
> — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:45`

> "Lady Cassalanter's attendant, {@creature Tissina Khyret|wdh} (see \"Head Servants\"), spends most of her time here when she's not with her mistress. The room is furnished for comfort and includes overstuffed chairs, fainting couches, and a wine bar."
> — `sources/adventure-wdh.json:20524` (room header "C19. Master Sitting Room" at `:20520`)

**Willifort (shared lockbox):**

> "{@creature Willifort Crowelle|WDH} and {@creature Tissina Khyret|wdh} keep their cult regalia (see \"Cult of Asmodeus\"), in a gold-embellished lockbox hidden under a stack of quilts bearing images of flying devils. The box can be unlocked with either Willifort's or Tissina's golden key, or by a character who succeeds on a {@dc 14} Dexterity check using thieves' tools. It can also be pried open with a successful {@dc 16} Strength (Athletics) check."
> — `sources/adventure-wdh.json:20540`

> "- **Tissina Khyret:** Ammalia's attendant and a fellow cult member. Their regalia is kept in one lockbox, and each holds a golden key to it."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:38`

**The cult rites (Nana Rosse is in the same perimeter):**

> "If the cult is here in force, thirty human {@creature cultist||cultists} stand in neat rows before the statue, chanting to Asmodeus with wooden goblets in hand while their leader, {@creature Victoro Cassalanter|WDH} (see {@adventure appendix B|WDH|12}), tosses offerings into the bowl. Roughly half of the cultists are members of the nobility; the rest are Waterdavian rabble brought into the cult to fill out the ranks. Standing around the perimeter are {@creature Willifort Crowelle|WDH}, {@creature Tissina Khyret|wdh}, {@creature Laiba \"Nana\" Rosse|wdh|Laiba Rosse}, and {@creature Jandar Chergoba|wdh} (see \"Head Servants\"). Their job is to make sure the other cultists behave themselves while {@creature Ammalia Cassalanter|WDH} (see {@adventure appendix B|WDH|12}) walks gracefully through the crowd with a golden decanter, ceremonially pouring wine into the cultists' goblets for toasting to the Lord of the Nine Hells. Lady Cassalanter's six {@creature imp||imps} (see {@area C25|328}) are perched invisibly on the statue."
> — `sources/adventure-wdh.json:22818` (Cult Gathering, page 129)

### A6. Faith and the cult's order

> "The head servants of Cassalanter Villa are members of the cult. These four servants are described below. All appear to be tieflings, though one is not. The following changes apply to the tieflings' stat blocks:"
> — `sources/adventure-wdh.json:18467` (Head Servants, page 116; the four are Willifort, `:18477`, Tissina, `:18487`, Nana, `:18497`, and Jandar, `:18507`)

> "The cult runs on a strict order. Victoro leads the worship and Ammalia pours the wine, the head servants keep the other members in line, and Seffia is a true believer in the cult's hierarchy (*Dragon Heist*, 5e; **Seffia Naelryke**)."
> — `campaign/setting/organizations/10-cassalanters.md:41` (Rank Is Kept)

> "It also binds people through debt, as with Jandar, through loyalty, as with Tissina, and through closeness to the twins, as with Nana Rosse (`arc-g-cassalanter-villa.md` lines 96-98)."
> — `campaign/setting/organizations/10-cassalanters.md:69` (Recruiting; the bullet's first sentence reads "The cult draws nobles and commoners with the promise of wealth and status (*Dragon Heist*, 5e).")

No source gives Tissina's own creed, prayers or rank. The only type label is the adventure's `{@creature cult fanatic}` tag (`sources/adventure-wdh.json:18492`).

### A7. Signature belongings and looks

> "Madame Khyret dresses in a long black gown and wears a headdress with black tassels." — `sources/adventure-wdh.json:18492`

> "gold-embellished lockbox hidden under a stack of quilts bearing images of flying devils" and "golden key" — `sources/adventure-wdh.json:20540` (full sentence in A5)

### A8. Where she is placed (sourced)

> "She is an aging tiefling {@creature cult fanatic}, and she spends most of her time in the master sitting room ({@area C19|31a})." — `sources/adventure-wdh.json:18492`

> "Area C19 – Sitting Room (attendant to Lady Cassalanter)" — `sources/10. Lair  Cassalanter Villa.pdf`, printed p.81 [PDF p.5] (Adversary Rosters; transcription)

> "Any combat in this room draws the attention of both {@creature Laiba \"Nana\" Rosse|wdh|Laiba Rosse} ({@area C17|316}) and {@creature Tissina Khyret|wdh} ({@area C19|31a})." — `sources/adventure-wdh.json:20533` (the linen closet's own room number is not in the quote)

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page: "*Tiefling cult fanatic (Asmodeus), lawful evil, she/her*. Stat block: **Cult Fanatic**." — `campaign/setting/notable-figures/cassalanters/07-tissina-khyret.md:5`
- Org page: "- **Tissina Khyret** — Tiefling cult fanatic (Asmodeus), lawful evil. See the **Tissina Khyret** page in Notable Figures." — `campaign/setting/organizations/10-cassalanters.md:99`
- Adventure: "The tieflings are lawful evil." — `sources/adventure-wdh.json:18471` (applies to the tieflings among the four head servants, `:18467`; Tissina is a tiefling at `:18492`). Matches.
- Wiki: none.

**Species**
- Page: "*Tiefling cult fanatic (Asmodeus), lawful evil, she/her*" — `07-tissina-khyret.md:5`
- Adventure: "She is an aging tiefling {@creature cult fanatic}" — `sources/adventure-wdh.json:18492`
- Org page: "Tiefling cult fanatic (Asmodeus), lawful evil." — `campaign/setting/organizations/10-cassalanters.md:99`

**Pronouns**
- Page: "she/her" — `07-tissina-khyret.md:5`
- Adventure: "She is an aging tiefling {@creature cult fanatic}, and she spends most of her time" — `sources/adventure-wdh.json:18492` (explicit "She")
- Adventure, title: "Madame Khyret is the personal attendant" — `sources/adventure-wdh.json:18491`. "Madame" is a title; the pronoun comes from `:18492`.

**Stat block**
- Page: "Stat block: **Cult Fanatic**." — `07-tissina-khyret.md:5`
- Adventure tag: "She is an aging tiefling {@creature cult fanatic}" — `sources/adventure-wdh.json:18492`
- Alexandrian: "Tissina Khyret (Chief Housemaid) – tiefling cult fanatic, MM p. 345 (DH p. 117)" — printed p.82 [PDF p.6]; transcription. The Alexandrian's stat source is MM p. 345. No file gives the Cult Fanatic stat block. The label is the page's own.

**Name pronunciation (Name tag only)**
- "{@creature Tissina Khyret|WDH}" with "teh-SEE-nah KYE-ret" — `sources/adventure-wdh.json:325-326`

**Age**
- "aging" — `sources/adventure-wdh.json:18492`. No number. See F1.

---

## C. Sentences on the current page that narrate a quest-time or day-one conflict

Current page: `campaign/setting/notable-figures/cassalanters/07-tissina-khyret.md`. "Day-one OK" means no quest gate. Brief rulings 1 and 3 apply.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Tiefling cult fanatic (Asmodeus), lawful evil, she/her*. Stat block: **Cult Fanatic**." | Day-one OK | `organizations/10-cassalanters.md:99`; `adventure-wdh.json:18471`, `:18492` |
| 2 | L6 | "**Affiliation:** The Cassalanters (cult)" | Day-one OK | `organizations/10-cassalanters.md:52` |
| 3 | L7 | "**Featured in:** Cassalanter Villa" | Quest reference, not lore. No quest journal names her (grep of `campaign/quests/`: no Tissina line). Her campaign appearances are the Villa structure document and the location and roster sources | `campaign/structure/arc-g-cassalanter-villa.md:96` |
| 4 | L11 | "**Resonance.** Tissina should inspire surface courtesy; the specific unease of someone who anticipates needs too precisely; and cold dread when the party learns she is a cult fanatic." | Mixed. "when the party learns she is a cult fanatic" is a discovery condition (quest-time). Ruling 1 requires a day-one restatement; see the Ammalia precedent after the voice list in C | Cult status: `organizations/10-cassalanters.md:99`; Social Exposure stage text: `arc-g-cassalanter-villa.md:267` |
| 5 | L13 | "**Emotions.** Tissina most often feels attentive devotion to Ammalia, theological certainty about Asmodeus, professional alertness to threats to the household, and the particular steadiness of someone who has never doubted the choice she made." | Day-one. Verbatim. "the choice she made" is not sourced (F4) | `arc-g-cassalanter-villa.md:96` (devotion to Ammalia) |
| 6 | L15 | "**Motivations.** Tissina wants to protect Ammalia and the household, serve Asmodeus through that service, and identify threats to the villa before they become problems." | Day-one. The "identify threats" aim has no separate source | `arc-g-cassalanter-villa.md:96` (devoted to Ammalia) |
| 7 | L17 | "**Inspirations.** When playing Tissina, channel Gríma Wormtongue (*The Lord of the Rings*), Theon Greyjoy (*Game of Thrones*, servile devotion), and Moneypenny (*James Bond*, loyal adjutant in a darker register)." | Not a fact | n/a |
| 8 | L21 (a) | "**Persona.** To the world, Tissina Khyret is the tiefling attendant who stands near Ammalia at social functions and anticipates what is needed before it is asked." | Day-one. The attendant role is sourced (`adventure-wdh.json:18491`). "stands near Ammalia at social functions" is not sourced (the adventure has her "spends most of her time" in C19, `:20524`) | `adventure-wdh.json:18491`, `:20524` |
| 9 | L21 (b) | "To those she considers threats, she is the first person in the villa to notice something is wrong." | Day-one trait. No source (F4) | none |
| 10 | L21 (c) | "Deep down, her worship of Ammalia and her worship of Asmodeus flow from the same devotion, and she has never seen any contradiction between them." | Day-one. Unsourced wording; the nearest source is "believes the worship is a family spiritual practice" | `arc-g-cassalanter-villa.md:96` |
| 11 | L23 | "**Morale.** In a fight, Tissina protects Ammalia first, using cult fanatic spells to hold threats at distance while Ammalia escapes." | Standing disposition with combat. No Tissina combat line exists in any file, and "cult fanatic spells" has no source (F6). Ammalia's Morale keeps the same standing line and routes the fight to the Villa structure document (`campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:143`) | none for Tissina |
| 12 | L25 (a) | "**Relationships.** Tissina is Ammalia Cassalanter's personal tiefling attendant, a cult fanatic whose regalia is stored alongside Willifort Crowelle's in a shared lockbox," | Day-one OK | `adventure-wdh.json:20540`; `03-willifort-crowelle.md:38` |
| 13 | L25 (b) | "...and the first cultist in the villa to notice an infiltration." | Quest-time gate ("an infiltration" is an intrusion by outsiders). No source for "the first cultist to notice" (F4) | none |
| 14 | L29 | "Tissina Khyret is Ammalia Cassalanter's personal tiefling attendant, a composed and courteous woman who stands near her mistress at social functions and seems to anticipate needs before they are expressed." | Day-one. Brief target shape item 7: Overview is two to four sentences, 21 words or fewer each. This is one sentence of 30 words | `adventure-wdh.json:18491` |

Note on row 13: the quoted fragment is a separate clause from row 12 and is quoted here as two parts.

**Voice doc quest-time clauses** (`.claude/skills/character-voices/voices/cassalanters.md`, Tissina, lines 118 to 132):
- Line 122: "- **Sentence shape:** Short, courteous sentences and quiet offers. After discovery: calm, devout certainty." — quest-time gate ("After discovery"). Ruling 16 requires a day-one restatement, and the skill's profile needs the same change.
- Line 123: "- **Word choice:** Public: service (\"my lady\", \"may I bring you…\"). After discovery: devotion, spoken of Ammalia and her faith in the same breath." — same gate.
- Line 124, Swearing: "- **Swearing:** *Never · Plain · n/a.*" — no gate.
- Line 128, Never: "She never leaves Ammalia's side in public, and never speaks of her faith to outsiders." — no gate.
- Tagline (line 119), Sound (line 121), Personality (line 125), Quirks (line 126), Signature phrases (line 127) and the sample lines (130 to 132) have no gate. Line 132, "Under pressure": "My lady, behind me. Something's amiss."

**Precedent on the same gate** (Ammalia page, Draft Notes, `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:145`): "Resonance: \"sympathy when the party sees her with the twins in the butterfly garden, and cold dread when they learn she is the one planning the poisoned feast\" became \"sympathy in anyone who sees her with the twins in the butterfly garden, and cold dread in anyone who learns she is the one planning the poisoned feast\"."

---

## D. Conflicts (both sides quoted)

**D1. Alignment.** No conflict. Page (`:5`) and org page (`:99`) say lawful evil. The adventure says "The tieflings are lawful evil." (`sources/adventure-wdh.json:18471`).

**D2. Stat-block label.** Page: "Stat block: **Cult Fanatic**." (`07-tissina-khyret.md:5`). Adventure: `{@creature cult fanatic}` (`sources/adventure-wdh.json:18492`). Alexandrian: "tiefling cult fanatic, MM p. 345 (DH p. 117)" (printed p.82 [PDF p.6]). These agree on "cult fanatic". The 2014/2024 naming question belongs to the Bestiary, not this page.

**D3. Attendant or housemaid.** Org page: "Tissina Khyret the attendant" (`campaign/setting/organizations/10-cassalanters.md:52`). Adventure: "the personal attendant to {@creature Ammalia Cassalanter|WDH} and is the family's chief housemaid" (`sources/adventure-wdh.json:18491`). Alexandrian: "Chief Housemaid" (printed p.82). No conflict. The page uses "personal tiefling attendant" only; the title "chief housemaid" is in the adventure and the Alexandrian and not on the page.

**D4. Whose attendant.** Tissina is Ammalia's (`sources/adventure-wdh.json:18491`; `02-ammalia-cassalanter.md:45`). Willifort is Victoro's: "As the Cassalanters' chief butler and Lord Victoro's personal attendant" (`sources/adventure-wdh.json:18482`). Both are "personal attendant" roles. No conflict if the Background keeps her with Ammalia.

**D5. Room.** Adventure: "the master sitting room ({@area C19|31a})" (`:18492`); header "C19. Master Sitting Room" (`:20520`). Alexandrian: "Area C19 – Sitting Room (attendant to Lady Cassalanter)" (printed p.81 [PDF p.5]; transcription). No conflict. The campaign location journal does not place her (grep of `campaign/locations/cassalanter-villa/`: no Tissina line; no C19 line).

**D6. Affiliation.** Page: "**Affiliation:** The Cassalanters (cult)" (`:6`). Org page: Tissina sits in the cult's list (`10-cassalanters.md:52`). No conflict.

**D7. Pronouns.** None. "Madame" (`:18491`) and "She" (`:18492`) agree with she/her.

**D8. Resonance discovery clause.** Page L11 "when the party learns she is a cult fanatic" conflicts with brief ruling 1 (campaign start, no "once the party" wording). Restatement precedent is quoted in Section C.

**D9. Overview length.** Page L29 is one sentence of 30 words. Brief target shape item 7: "21 words or fewer each."

---

## E. Stale lines in other files (not edited), and routed references

**E1. Voice profile, "After discovery" lines** (`.claude/skills/character-voices/voices/cassalanters.md:122`, `:123`). Quest-time gate. Stale against ruling 16 until changed.

**E2. Trollskull Alley Grand Opening.** `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md` names Ammalia, the twins and Nana Rosse (`:54`). It does not name Tissina. Tissina has no scene there.

**E3. Routed quest references (the Villa structure document, pending conversion):**
- `campaign/structure/arc-g-cassalanter-villa.md:96`: "If she learns the children's souls are forfeit, she breaks. DC 14 Charisma (Persuasion) with evidence of the contract turns her." — the turn mechanic. Quest-time.
- `campaign/structure/arc-g-cassalanter-villa.md:267`: "Trigger to Stage 2: a servant or guest observes something mildly suspicious — a failed DC 13 Stealth check near a restricted door, an odd question to staff that Maesta reports to Willifort, or Willifort's detect thoughts catching a concerning surface thought (failed DC 13 Charisma (Deception) check when Willifort is nearby)." — the Social Exposure trigger. Quest-time; no Tissina line.
- `campaign/structure/arc-g-cassalanter-villa.md:519`: "The cult members are individually motivated — true belief (Willifort), personal loyalty (Tissina), love for the children (Nana Rosse), debt-bound service (Jandar)." — a design note, quest content.

**E4. Alexandrian Cult Gathering roster** (printed p.81 [PDF p.5]; transcription): "TEMPLE OF ASMODEUS (CULT GATHERING)" with "3d10 cultists + All Named NPCs". This supports her presence at rites (see the Nana notes, D2, for the conflict on the other figure).

---

## F. Gaps (what a Background needs that no source gives), with the facts to stay consistent with

1. **Birth, age, origin, family, home before the Cassalanters.** No source. Only "aging" (`sources/adventure-wdh.json:18492`). Consistent facts: she is "an aging tiefling" (`:18492`); lawful evil (`:18471`; `10-cassalanters.md:99`).
2. **How long she has served Ammalia, and when she came.** No source. Consistent facts: "personal attendant" to Ammalia (`:18491`); personal attendants are kept while the household replaces other servants (`:18598`). Willifort's eight years (`03-willifort-crowelle.md:16`, `[research]`) are his, not hers.
3. **When Ammalia asked her to join, and what she was before.** The reason is sourced ("Joined because Ammalia asked her to.", `arc-g-cassalanter-villa.md:96`). The date is not (`10-cassalanters.md:27`, `:178`). Dated facts in the same file: "About 1489 DR, the bargain:" (`10-cassalanters.md:25`), and Jandar's debt "converted into cult service three years ago" (`arc-g-cassalanter-villa.md:98`). No source places Tissina's joining in that window.
4. **Claims on the page with no source:** "the first person in the villa to notice something is wrong" (L21), "stands near Ammalia at social functions" (L21), "the first cultist in the villa to notice an infiltration" (L25), "the particular steadiness of someone who has never doubted the choice she made" (L13). The Villa structure is silent on all four. Consistent sourced fact: she "spends most of her time" in C19 "when she's not with her mistress" (`:20524`).
5. **Her faith before the cult, her creed, any rank.** No source. Consistent facts: the rites are Asmodean and the cult pledges "devotion to Asmodeus" (`10-cassalanters.md:43`); she "believes the worship is a family spiritual practice" (`arc-g-cassalanter-villa.md:96`); the org page gives her no rank (`10-cassalanters.md:41`).
6. **Her combat spells.** No source. The Morale line (L23) is the only mention.
7. **Personal goals beyond Ammalia and the household.** No source. The Motivations (L15) are the page's own. Any personal goal is `[design]` (brief ruling 17). Constraints from the sources: she "does not fully understand the contract's terms" and "If she learns the children's souls are forfeit, she breaks" (`arc-g-cassalanter-villa.md:96`).
8. **Her knowledge of the Founders' Day feast.** No source gives her a role in it. The org page assigns the poison to Jandar: "Jandar Chergoba sees that the poison is distributed correctly." (`campaign/setting/organizations/10-cassalanters.md:67`). The Secret callout says "Jandar Chergoba, the villa's head chef, is the person who sees that the poison is distributed correctly." (`10-cassalanters.md:130`).
9. **Her relationship with Willifort beyond the lockbox and the rites.** Only the lockbox (`sources/adventure-wdh.json:20540`) and the perimeter (`:22818`) are sourced.
10. **Her Founders' Day role.** None.

**Consistency with the Victoro, Ammalia and Willifort pages** (the drafter must not contradict these):
- Ammalia page, line 45: "- **Tissina Khyret:** Her personal attendant and the family's chief housemaid, who joined the cult because Ammalia asked her to." (`campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:45`)
- Ammalia page, line 41: "- **Victoro Cassalanter:** Her husband and co-conspirator. Ammalia makes the final calls for the family and the cult, and Victoro, who leads the worship, has stopped questioning her. She pours the wine at the rites." (`02-ammalia-cassalanter.md:41`)
- Willifort page, line 24: "He has kept order at its rites since, and his regalia lies in a lockbox that he shares with Tissina Khyret and that a golden key held by each of them will open (*Dragon Heist*, 5e)." (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:24`)
- Willifort page, line 38: see A5 (shared lockbox and golden keys).
- Willifort page, line 88 (Secret): "He keeps order at the rites beside Tissina Khyret, Nana Rosse and Jandar Chergoba, and his regalia lies in the lockbox that he shares with Tissina." (`03-willifort-crowelle.md:88`)
- Willifort page, line 16: "Willifort Crowelle is a doppelganger who has served the Cassalanter household for eight years `[research]`." (`03-willifort-crowelle.md:16`)
- Victoro page: names neither Tissina nor Nana. Its line 53: "- **Terenzio Cassalanter** and **Elzerina Cassalanter:** The twins. Victoro is openly warm with them, and they know nothing of the pact." (`campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:53`)

---

## G. Inner-life hints (sourced, for the Background and personal goals; do not contradict)

- "the particular steadiness of someone who has never doubted the choice she made" — `campaign/setting/notable-figures/cassalanters/07-tissina-khyret.md:13` (Emotions, verbatim; the choice is not named in any file)
- "devoted to Ammalia personally. Joined because Ammalia asked her to." — `campaign/structure/arc-g-cassalanter-villa.md:96`
- "Does not fully understand the contract's terms — she knows about the temple, attends gatherings, believes the worship is a family spiritual practice. If she learns the children's souls are forfeit, she breaks." — `campaign/structure/arc-g-cassalanter-villa.md:96`
- "spends most of her time here when she's not with her mistress" — `sources/adventure-wdh.json:20524`
- "She never leaves Ammalia's side in public, and never speaks of her faith to outsiders." — `.claude/skills/character-voices/voices/cassalanters.md:128`
- "Publicly, her faith sounds like simple loyalty." — `.claude/skills/character-voices/voices/cassalanters.md:125`
- "Tissina wants to protect Ammalia and the household" — `campaign/setting/notable-figures/cassalanters/07-tissina-khyret.md:15` (Motivations, verbatim)
- "Tissina attends Ammalia" (org page wording: "Tissina Khyret attends Ammalia") — `campaign/setting/organizations/10-cassalanters.md:40`
- "Madame Khyret" (honorific) — `sources/adventure-wdh.json:18491`
- "wears a headdress with black tassels" and "a long black gown" — `sources/adventure-wdh.json:18492`
- The shared lockbox and golden key with Willifort — `sources/adventure-wdh.json:20540`

---

## H. Shared household sources (identical in both notes files)

**H1. Staff list, cult status, the head servants**

> "- **Household staff:** The villa employs sixteen named staff, and ten of them know nothing about the temple (`arc-g-cassalanter-villa.md` line 91). The six cult members are Willifort the butler, Tissina Khyret the attendant, Nana Rosse the twins' caretaker, Jandar Chergoba the head chef, and the field pair Seffia Naelryke and Arn Xalrondar. The other ten are Corvo (footman), Pela (laundress), Marchello (gardener), Fiorella (cook's assistant), Doro (stable hand), Lissette (upstairs maid), Rennet (scullion), Maesta (housekeeper), Tomas (night watchman) and Bressa (nursemaid). Maesta manages the non-cult staff and is loyal to the household's reputation, not to the Cassalanters themselves."
> — `campaign/setting/organizations/10-cassalanters.md:52`

> "- **The cult:** Victoro leads it, and the whole cult gathers in the temple at midnight on the first day of every tenday. About thirty members attend when it meets in force, roughly half of them nobles and the rest Waterdhavian commoners (*Dragon Heist*, 5e). Willifort, Tissina Khyret, Nana Rosse and Jandar Chergoba keep order at the rites while Ammalia pours the wine. The cult reaches beyond the household. Yalah Gralhund keeps Asmodean symbols and robes with Cassalanter embroidery in a trunk, and her groundskeeper Hurv Taldred wears a Cassalanter devotional mark (**House Gralhund**)."
> — `campaign/setting/organizations/10-cassalanters.md:50`

> "- **Chain of command:** Ammalia makes the final calls for the family and the cult, and Victoro, who leads the worship, has stopped questioning her. Willifort Crowelle links the family to everyone who works for it. He runs household security, reports to Ammalia and directs the spy and the poisoner. Seffia Naelryke commands the field team and answers to Victoro, and the head servants keep order at the rites."
> — `campaign/setting/organizations/10-cassalanters.md:51`

> "- **Laiba \"Nana\" Rosse** — Tiefling cult fanatic (Asmodeus), neutral evil. See the **Laiba \"Nana\" Rosse** page in Notable Figures."
> — `campaign/setting/organizations/10-cassalanters.md:100`

> "The head servants of Cassalanter Villa are members of the cult. These four servants are described below. All appear to be tieflings, though one is not. The following changes apply to the tieflings' stat blocks:"
> — `sources/adventure-wdh.json:18467`

> "The tieflings are lawful evil."
> — `sources/adventure-wdh.json:18471`

**H2. The Villa structure document (routed where quest-time)**

> "The household holds six souls who know what lies beneath."
> — `campaign/structure/arc-g-cassalanter-villa.md:21` (the paragraph then names Willifort, Tissina, Nana, Jandar, Seffia and Arn; Seffia and Arn live at the Windmill)

> "*Questioning Staff.* The Cassalanter household employs sixteen named staff. Ten know nothing about the temple. Six are cult members with varying degrees of commitment."
> — `campaign/structure/arc-g-cassalanter-villa.md:91`

> "- **Bressa** (nursemaid, human female, 20s) — assists Nana Rosse with the twins during daytime hours. Knows the children's schedule, favorite hiding places in the villa, and that Terenzio has nightmares about \"the thing upstairs.\" If told the truth: panics, then steadies — the children come first."
> — `campaign/structure/arc-g-cassalanter-villa.md:113`

> "- **Maesta** (housekeeper, human female, 50s) — manages the non-cult staff. Professional, discreet, loyal to the household's reputation rather than to the Cassalanters personally."
> — `campaign/structure/arc-g-cassalanter-villa.md:111` (rest of the bullet covers Maesta's observation of Willifort, the staff's safety and the children)

> "The cult members are individually motivated — true belief (Willifort), personal loyalty (Tissina), love for the children (Nana Rosse), debt-bound service (Jandar). They are not interchangeable."
> — `campaign/structure/arc-g-cassalanter-villa.md:519`

**H3. The published adventure's household rule**

> "Cassalanter Villa is home to no one but Lord and Lady Cassalanter, their children, their personal attendants, and their guards. All the other servants who work at the villa live in dingy homes in the Dock Ward or the Field Ward and travel across the city in the wee hours of the morning to arrive before the Cassalanters awake."
> — `sources/adventure-wdh.json:18597` (page 118)

**H4. The Alexandrian Villa PDF (transcriptions; run pdftotext before prose use)**

> "Laiba “Nana” Rosse (Tutor/Caretaker) – tiefling cult fanatic, MM p. 345 (DH p. 117)"
> "Tissina Khyret (Chief Housemaid) – tiefling cult fanatic, MM p. 345 (DH p. 117)"
> — `sources/10. Lair  Cassalanter Villa.pdf`, printed p.82 [PDF p.6] (Stat Reference)

> "Area C17 – Playroom (or with the children)" and "Area C19 – Sitting Room (attendant to Lady Cassalanter)"
> — `sources/10. Lair  Cassalanter Villa.pdf`, printed p.81 [PDF p.5] (Adversary Rosters, the two columns; the roster entries are "Laiba “Nana” Rosse (25%)" and "Tissina Khyret")

> "Cult members are virtually certain to report the questioning to their masters as soon as possible, and may also mislead PCs by providing false information."
> — `sources/10. Lair  Cassalanter Villa.pdf`, printed p.82 [PDF p.6] (Questioning Staff; the sentence before it begins "The risk of questioning the Cassalanter’s staff is that there is a 10% chance that they’re asking someone who is a secret member of the cult.")

> "TARSAKH 1st – CARAVANCE: During this gift-giving holiday, the Cassalanters give most of their staff the night off."
> — `sources/10. Lair  Cassalanter Villa.pdf`, printed p.79 [PDF p.3]

> "TARSAKH 9th – LEIRUIN FEAST: This is the feast at which the Cassalanters poison 99 guests" (rest of the passage covers the ritual and says the feast is cancelled if the Vault is not secured)
> — `sources/10. Lair  Cassalanter Villa.pdf`, printed p.79 [PDF p.3]. The campaign has Founders' Day on Flamerule 1 (`campaign/setting/organizations/10-cassalanters.md:7`).

**H5. Other campaign files that name the figures**
- `campaign/setting/deities/asmodeus.md:72` (rest of the line covers Victoro, Ammalia and Willifort): "Tissina Khyret, Laiba \"Nana\" Rosse, Jandar Chergoba, Seffia Naelryke and Arn Xalrondar are cult fanatics."
- `campaign/guides/factions/11-cassalanters.md:107`: "- Notable Figures: **Victoro Cassalanter**, **Ammalia Cassalanter**, **Willifort Crowelle**, **Seffia Naelryke**, **Arn Xalrondar**, **Tissina Khyret**, **Laiba \"Nana\" Rosse**, **Jandar Chergoba**, **Rella Asp**, **Ivrala Sorn**, **Osvaldo Cassalanter**, **Caladorn Cassalanter**"
- `campaign/setting/villains/cassalanters.md:64`: "- Willifort Crowelle, the doppelganger butler, knows everything that happens in the villa and reports to Ammalia. He runs household security and is the family's most dangerous weapon."
- `campaign/setting/villains/cassalanters.md:132` (Draft Notes): "The twins now first appear at the Grand Opening, with their nanny Nana Rosse, in a fixed scene, and the party meets them again in the villa."

**H6. Wiki:** no line for any staff figure (see Method).

**H7. Not readable**
- `sources/SOURCE_GUIDE.md:687` names `Cassalanters, their tragic backtstory, and Endgame setup.docx` (Victoro and Ammalia backstory, the children, endgame paths). It sits in `sources/Other remix files/` and was not opened. It may hold household backstory.
- `sources/SOURCE_GUIDE.md:695` names `The Waterdavian's Guide to Waterdeep NPCs ... .docx` (a broad NPC reference). Not opened; it may hold Tissina.
