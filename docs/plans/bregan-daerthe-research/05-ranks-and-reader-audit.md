# Bregan D'aerthe faction events: rank-event audit and cross-campaign reader audit

I read everything under `bregan-daerthe/`, the Doom Raiders rank events and design notes, guide 08, the BD organization page, the Jarlaxle villain page, the BD Notable Figures pages, arc-e through arc-j, the Act I–II quest journals, and Appendices B and C.

**Reading gaps:**
- I did not open `Jarlaxle Baenre NPC Guide.docx`, `Zardoz Zord (and extra side quest hook).docx` or PDF 26.
- PDF 3 (pp. 1–2) has only one BD sentence: "consider simply making the PCs those agents". Appendix B and C are the real source for ranks and missions.
- Nothing was written. The path prefix `BD/` means `/home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe/`, and `DR/` means `.../faction-events/doom-raiders/`.

---

## PART 1: Rank events

### 1.0 What the four drafts share

**Retired formats.** The whole BD folder has 143 hits for retired markers across 30 files. In the rank events:
- `> **[GM]**` blocks: r03:3 and :75; r10:3 and :100; r25:3 and :103; r50:3, :103 and :129.
- `[!profile]`: r03:61, r10:90, r25:65 and :71, r50:57.
- `[!design]`: r50:15 (the nesting is broken, `> > >`).
- `[!note]` blocks, which are not in the Ember set: r03:39, r10:46, r25:55 and :85.
- True/False flag headings: r03:71, r10:96, r25:99, r50:121 and :125.
- Scene labels "Scene 1:" through "Scene 4:" in r50.
- A bare `## Read Aloud` section: r50:143.
- A nested-quote glitch: r10:76.
- Summaries are third person ("The character was named…"), where DR uses a first-person journal.
- No rank event has an "awards no Milestone Points" line, `[!readaloud]` or `[!qna]` blocks, `[!social]` blocks, or a design-notes file.
- There are no design-notes files in `00-first-meeting`, `s01` to `s04`, or `r03` to `r50`. That is 9 missing files, where DR needed 7.

**Per-PC gating.** All four summaries say "one character's Bregan D'aerthe renown reaches N" (r03:7, r10:7, r25:5, r50:7), so the trigger is individual. Everything after the trigger is not:
- The outcomes are binary True/False flags, not "mark with the recipient's name".
- Benefits have no per-member trackers.
- "The party" leaks in: r03:41, r10:56, r25:12, and "the party was pursuing" in all four Next Steps.

**Manshoon, Floxin, Splinter, Zhentarim, Kolat.** The BD folder has zero hits (grep). R1 is clean. No Manshoon Named gate is needed for BD.

**Lolth.** There is no reverence and no mention of the word anywhere in the folder, but the iconography needs a decision:
- r50:39 has a coin with "a stylized spider caught in its own web, crossed by a blade".
- m04 ev:26 uses a chalk "stylized spider" contact mark, and DR M1 has a forged spider disc.
- Appendix C's BD-4 briefing actually says "for Lolth's sake, be discreet" (App. C ~l.1610). The drafts correctly dropped it.
- If the spider stays, it must read as a rejected symbol. Soluun's profile in `voices/bregan-daerthe.md:49` and :54 has him calling Lolth "the spider-bitch he walked away from".

**Premature Jarlaxle reveal.** Nothing in the rank events says "Jarlaxle" in speech before it should. Problems:
- r10:54–58 has Nevercott or Zardoz say "every nimblewright sold in Waterdeep… traced to buyer… Cross-reference with whatever you found at the House of Inspired Hands". That identifies BD as the nimblewright seller. It spoils the Fireball! ev-04 discovery and overlaps with:
  - the complete ledger Jarlaxle gives BD members in Fireball ev-04:85 and :110;
  - the "Ledger of Commissioned Automata" in BD M2b (m02b ev:19);
  - guide 08:49, where taking the shipping records is a +2 heist (Appendix B l.784).
- r10:86 has the persona name "the Vault of Dragons" at Renown 10, which can arrive in Act II.
- r25:113 and its Overview say Jarlaxle "delivers the promotion in person — the first time the organization's leader has appeared for a rank event". But r10:9 and r03 are already Jarlaxle in disguise.

**2014 stat names.**
- "Drow Gunslinger" (r25:69, :75) is a WDH block (guide 08:79 cites DH p. 201), not a 2024 MM name.
- r25:87 uses "Swashbuckler". The Notable Figures page also says "Swashbuckler (with modifications)" (`01-jarlaxle-baenre.md:6`).
- r25 "Drow" and r10 "Spy (2024 *Monster Manual*)": Spy is fine.
- I could not verify Swashbuckler or Drow against 2024 data, which is not in the repo. Per the Session 38 handoff, treat them as suspect, like Thug and Veteran.
- r25 and r50 give no CR 2.0 ally numbers. DR r25:139 and r50:151 do.
- In the m-events, "Thugs" (m03:25, m06:50) and "Veteran" (m06:24) are 2014 names. That is out of focus but worth a sweep.

### 1.1 r03 Soldier (`BD/r03-soldier/ev-01-soldier.md`)

| Check | Finding |
|---|---|
| Content | Nevercott meets one character at the Seven Masks back office (:17–25). Three benefits follow: a tenday intelligence summary via Krebbyg's dead drop (:27–41), Faire access through "the autumn program" and a Heartbreaker prep room (:43–51), and equipment at 20% below market via Fel'rekt (:53–59). |
| Procedures | Thin. There is no address or hours for the drop, and no limits or loss rule. Compare DR r03:160–228, which has a door phrase, a 3-hour notice, a 500 gp cap and a 10-day delay. |
| Guide 08:57 | Soldier is the intelligence channel, Faire access, and a 20% fence discount. r03 mixes in the Initiate benefit "drow-made equipment at cost via Fel'rekt" (guide 08:56). No event ever delivers the Initiate safe house aboard the *Heartbreaker* or *Hellraiser*. |
| Timing | On guide base awards a member reaches Renown 3 right after M1 (1 + 2). That is before the Faire arrives on Ches 21 (`act-i/trollskull-alley/ev-07:26`) and before s02 first names Bregan D'aerthe (s02:29, "Kreb Unmasked"). r03 hands out Faire access at that point. |
| Numbering | r03:15 says Three Nights is "BD Mission 4". Per guide 08:68 it is Mission 3, so this probably counts M2b. |
| Nar'l channel | The summaries come from Nar'l ("our source", :33). M4 can leave Nar'l Extracted or Eliminated (m04 ev:75–85), which kills that channel. r03 never reads it. |
| Other | Nevercott has no voice profile. r03:15 hedges for a late firing ("substitute Krebbyg"). |

### 1.2 r10 Officer (`BD/r10-officer/ev-01-officer.md`)

| Check | Finding |
|---|---|
| Content | Contact is chosen by whether **Three Nights** is complete (:9, :16): Nevercott at Seven Masks, or Zardoz at the *Eyecatcher* (:26–34). The Spy is **Ilphrin Quiss**, a woman who has run a calligraphy shop for eight months (:38–48). A four-page shipping-records folio (:50–58). An Uncommon item chosen by the GM from four suggestions (:60–76). A once-per-quest, 48-hour assessment with a Vault "gap" (:80–88). |
| Per-PC | One named Spy and no roster. Two Officers means one Spy. Quest counting is undefined. The item is a GM improvisation, where DR gives fixed tables. |
| Guide 08:58 | Matches in substance. Guide 08:58 says "one Uncommon item", and r10 leaves it to the GM. |
| Persona branch | s03 retires Nevercott only after the Compromised Eye dinner (s03:16, org page `07-bregan-daerthe.md:11` "After Mission 4"). r10 and r25 key off **Three Nights** and **Sea Maidens Faire**, not off s03's **Zardoz Introduced**. If s03 never fires (Nar'l Eliminated, s03:7), Nevercott persists. No branch covers that. |
| Persona/format | An "ivory card" summons (r10:16, r25:19) conflicts with the black silver-ship card (first-meeting:71, s03:32). |
| Other | The records duplicate Fireball ev-04 (see 1.0). Ilphrin has no Notable Figures page and no voice. The Session 32 handoff lists her as invented. |

### 1.3 r25 Commander (`BD/r25-commander/ev-01-commander.md`)

| Check | Finding |
|---|---|
| Content | Branches on whether Faire has resolved and "Jarlaxle's identity is known" (:9, :15). Zardoz at the *Eyecatcher* (:23–29) or Jarlaxle on the *Marpenoth* (:31–39). Three favors, one per quest (:43–57). Pelsha and Vorn plus four Drow on one operation per quest (:59–75). Jarlaxle accompanies the party once per quest (:77–87). |
| Per-PC | Individual in the summary. But "once per quest" is unscoped (whose quest?), and there is one Pelsha and Vorn pair for any number of Commanders. |
| Guide 08:59 | Wording differs: guide says "the party", r25 says "the character". Appendix B l.795 says "per arc", not per quest, and has no three-favor list. The favors, item and assessment are repo additions I could not source. |
| Identity trigger | "Identity is known" has no outcome name. Jarlaxle's identity can come from Fireball ev-04:30 (Zord is Jarlaxle), Harper M4 (**Jarlaxle Identity Exposed at Harper Salon**), M2b or the Faire. |
| Vault reader | r25:101 says Commander members receive "Jarlaxle's Lords' Alliance proposal". But guide 08:33, `player-factions-overview.md:182`, and arc-j:55 put that proposal at "Dread Lord renown". That is a DR rank. BD's top rank is Houseless Noble, and r50 never mentions the proposal. |
| Other | The "first time anyone below Commander… below the waterline" claim (:15) is unbacked: Fireball Path 3 and arc-h let any party member in. |

### 1.4 r50 Houseless Noble (`BD/r50-houseless-noble/ev-01-houseless-noble.md`)

| Check | Finding |
|---|---|
| Content | Ceremony on the *Marpenoth* with Krebbyg and Fel'rekt and "other lieutenants" (:19–63). A black coin (:39). A sealed packet of Underdark names (:51). A "blank favor": accept for full access, decline for partial (:65–93). Vault Context (:99–109). Sarev Oust, a broker in Skullport (:135). |
| Guide 08:60 | The guide table gives full network and *Marpenoth* access unconditionally. The blank-favor split is new and appears in neither guide 08 nor Appendix B. |
| Cost of declining | Real but soft: the crew "requires Jarlaxle's approval" (:81). It is not a lost-seat cost like DR r50. |
| Soluun | :47 has "Soluun (if present and not yet gone by his own choices)". It should read **Soluun Captured/Escaped/Killed** (DR M1) and Jarlaxle's decision. See §2.2. |
| Ilphrin | :133 says "Ilphrin Quiss, Pelsha, and Vorn remain assigned from Commander rank". Ilphrin is assigned at Officer. |
| Vault timing | The Vault Context only works if the event fires after Vault of Dragons. The "Expected in Mad Mage" callout (:15–17) has the wrong math: "all six missions at full bonus renown" gives about 19–20, never 50. |
| Ship location | *Marpenoth* is "at anchor" (:21). Faire departs Tarsakh 20 (`structural-rules.md:50, :56`, arc-h:81), but m06:112 says "committed to Waterdeep for another season". |

**WDMM check (`sources/adventure-wdmm.json`).** There is no Jarlaxle, Bregan D'aerthe, Baenre or Xibrindas text. `SOURCE_GUIDE.md:85` claims "Bregan D'aerthe connections" at Sargauth, but the JSON has none. The only relevant hooks:
- Menzoberranzan appears via House Auvryndar (a low-ranking house consolidating in Undermountain, allied with the Zhentarim, ~l.6577–6578).
- Luskan appears via the Arcane Brotherhood (l.3322, l.24475).
- Skullport is Xanathar-controlled (l.6578).
- Skull Island has two 60 ft deep harbors with ship-sinking augers (l.62642). That is a real obstacle to a submarine.
- Sarev Oust and "contacts in Menzoberranzan" have no WDMM basis. They are free invention, consistent with the Auvryndar seed.

### 1.5 Renown 25 and 50 reachability

- Guide base awards are 2, 2, 3, 3, 4 and 4, which is 18. With the join at 1 that is 19, the same as DR.
- Gates (BD M2 R2, M3 R4, M4 R7, M5 R10, M6 R14) are reachable on guide base awards: 3, 5, 8, 11, 15, 19.
- The drafts award 1+1 (M1, M2) and 2+1 (M3–M6), with M6 up to 4 (m01 ev:73–74, m02 :75–76, m03 :76–77, m04 :89–91, m05 :72–73, m06 :102–104). That is below the calibration of 3/3/4/4, and the gates become unreachable without every supplementary bonus.
- M2b adds +1 and +1 (m02b ev:76–77) but has no guide row.
- BD-specific sources outside the folder:
  - Fireball ev-04:112 (+1 or +2).
  - Gralhund ev-09:125 (+2).
  - The guide Earning Renown list (08:45–50).
- Roughly 25 is plausible by Kolat Towers. 50 is not reachable without Mad Mage content, as in DR (`DR/r50-dread-lord/design-notes.md:17`).

### 1.6 Fix list (Doom Raiders brief style)

**All four**
- Rebuild on the Harper/DR page model: Summary, descriptive scenes, `[!readaloud]`, `[!social]`, `[!qna]`, `[!exploration]`, Renown Opportunities, Aftermath, Concluding the Event, Event Outcomes, Next Steps ("awards no Milestone Points"), a one-line Overview, a first-person Summary, and a new `design-notes.md`.
- Outcomes become "mark with the recipient's name", per member.
- Remove "the party" from benefits.
- Give every benefit a written procedure (contact, place, notice, limits, loss rule, once-per-quest tracking).
- Voice from `voices/bregan-daerthe.md`:
  - Write a Nevercott profile (none exists).
  - Zardoz never mentions the Underdark, drow or Luskan (voices:18).
  - Apply the swearing levels.
- Add CR 2.0 ally numbers in a mechanics reference: Spy about 17 Power at levels 5–10, per DR r25:139.

**r03**
- Separate the Initiate benefit (Fel'rekt equipment at cost) from the Soldier 20% fence discount.
- Fix the "Mission 4" mislabel.
- Read the Nar'l outcomes: if Nar'l is Extracted or Eliminated, the channel degrades.
- Move Faire access behind the Faire's arrival, and gate it on BD being known (s02 / **Kreb Unmasked**).
- Settle who delivers it (Krebbyg versus Nevercott) against s02 and s03.

**r10**
- Re-key the contact branch on **Zardoz Introduced** (and the s03-did-not-fire case).
- Decide the records. Either they are the Officer benefit (and Fireball ev-04's "given to BD members" is cut), or Officer gets something else.
- Reconcile with M2b's ledger and the +2 heist (guide 08:49).
- Write a fixed item table and a Spy roster, one per Officer.
- Remove "Vault of Dragons" from speech unless the vault is known.
- Add a mechanics line for Ilphrin.

**r25**
- Key the Jarlaxle-open branch on a named outcome (candidates: Harper's **Jarlaxle Identity Exposed at Harper Salon**, or a Faire outcome).
- Correct the "first rank event with Jarlaxle" claim.
- Reconcile the Vault proposal reader (Commander versus "Dread Lord" in arc-j:55 and guide 08:33).
- Add a crew ledger so two Commanders cannot stack Pelsha and Vorn.
- Define "per quest" (guide 08 versus Appendix B "per arc").
- Add a Jarlaxle-as-ally mechanics note.

**r50**
- Name the Mad Mage placement in the Hook (as DR r50:16).
- Write the Vault branch (resolved or not).
- Branch the "empty seats" on Soluun and the lieutenants' outcomes.
- Make declining cost something concrete.
- Settle the spider coin (see 1.0).
- Fix the Ilphrin line.
- Decide the *Marpenoth*'s whereabouts and the Skullport harbors.
- Drop or justify Sarev Oust.
- Correct the Renown math.

---

## PART 2: Cross-campaign reader audit

### 2.1 Outcome / flag table

| Outcome | Writers (file:line) | Readers inside BD | Readers outside BD (file:line) |
|---|---|---|---|
| **Bregan D'aerthe Joined** | BD first-meeting:99; Trollskull ev-04:115 (party-level "at least one party member") | first-meeting:111 | Free-text "BD operative/member" in `act-i/trollskull-alley/ev-07:55`; Fireball ev-04:106–112; Gralhund ev-01:11 and :65, ev-04:84, ev-06:72–76, ev-07:82–86, ev-09:121; arc-e:93; arc-f:43 and :105; arc-g:47; arc-h:45 and :103; arc-i:45; arc-j:55; `trollskull-manor/09:92–96`; `trollskull-manor/02:85`. None use the outcome name. |
| **BD Contact Severed** | first-meeting:45, :103; s04 (header, :51); Trollskull ev-04:121 | first-meeting:113, s04:7 | Trollskull flowchart:54 and :83; `player-factions-overview.md:169, :176`; `trollskull-manor/09:96`; `villains/jarlaxle.md:3`; guide 08:37. arc-h has no by-name reader. |
| **BD Acknowledged** | Trollskull ev-04:118; `player-factions-overview.md:173` | none (BD never sets or reads it) | Fireball flowchart:53; flowchart:55 and :82 (Faire "Zardoz relationship"). |
| **Ryvarra Identified** | Trollskull ev-03:47 and :57; first-meeting:10 (second chance) | first-meeting:21, :57, :79 | Trollskull ev-04:45; flowchart:79; `jarlaxle.md:3`. |
| **Kreb Unmasked** | s02:53 | s04:34 only; s02:54 promises M3–M6 read it, but none do | none |
| **Coin Pouches** | s01:37 | none (s01:39 says s03 reads it; s03 does not) | none |
| **Zardoz Introduced** | s03:84 | none | none (s03:86 promises arc-h reads it; arc-h does not) |
| **Nar'l Active / Extracted / Eliminated** | m04 ev:75, :79, :83 | s03:12, :74; m04 ev:99 | m04 promises arc-f, arc-i, arc-h and M5. arc-f assumes Nar'l alive in X35 (arc-f:99–111, :184) and never reads these. Force Grey M4 (ev-01:103) has Nar'l alive in the lair regardless. |
| **Eye 3 Recovered by BD** | m06 ev:96 | none | m06:98 and :116 promise arc-h. arc-h reads a five-state "BD operational?" instead (arc-h:270–276). |
| **BD Soldier / Officer / Commander / Houseless Noble Reached; BD Blank Favor Accepted** | r03:71, r10:96, r25:99, r50:121 and :125 | r03:73 names r10 as reader; r10:98 names r25; r25:101 names r50 | arc-e:93 and :327–331 read "BD renown 3+" in free text; r25:101 claims arc-j reads it (arc-j:55 says "Dread Lord renown"). |
| *Read from elsewhere:* Lords' Alliance Redknife (m03:30) | LA rank | m03 Night One | — |
| *Read in other folders from BD-adjacent quests:* Jarlaxle Informed, Jarlaxle Brief Received, BD Team Spotted | Fireball ev-04:116; Gralhund ev-01:97, ev-02:94 | none (BD events never read them) | Gralhund ev-01, ev-06, ev-07 |

Harper M4 also writes **Jarlaxle Identity Exposed at Harper Salon** and **Jarlaxle Discretion Agreement**. Its text says "BD follow-up reads those commitments" (`harpers/m04.../ev-03:176–179`). No BD event reads either.

### 2.2 Contradictions (candidate "Bregan D'aerthe event rewrite" out-of-scope section)

**A. Recruitment and membership**
1. Contact Severed is party-wide in first-meeting:43, :45, :103–105, :113, in all of s04, in guide 08:37, and in `player-factions-overview.md:169, :176`. It conflicts with first-meeting:85 ("Any party member may accept"). Appendix B ~l.719 says "ends contact for now", not permanently. That is also the user's Session 37 decision 5.
2. Joined is party-level in Trollskull ev-04:115 and first-meeting:99 and :101.
3. Appendix B l.715 says BD recruits "only drow", while the repo and guide say any PC.
4. First meeting :75 has Nevercott say "Bregan D'aerthe" once, and only if pressed. Appendix B ~l.761 has him name it outright. s02:29 says Krebbyg names it "for the first time" and sets **Kreb Unmasked**. These three disagree.
5. BD Acknowledged (Trollskull ev-04:118, `player-factions-overview.md:173`) is never written by the BD first meeting.
6. Both Trollskull ev-04:115 and first-meeting:99 are writers for Joined.
7. Guide 08:36–37 says BD recruits "during Trollskull Alley", but `trollskull-manor/09:96` and `jarlaxle.md:3` say membership "closes" with Severed only. They agree, but nothing says Severed is reversible.

**B. Identity ladder (Nevercott / Zardoz / Jarlaxle)**
8. s03:9 says Zardoz "meets the party in person for the first time". Trollskull ev-05 has Zord sponsoring and watching from his box. M2b ev:87 says "the party has now seen Zardoz Zord". Fireball ev-04:28 has Zord's office. Three earlier sightings.
9. First meeting:75 has Nevercott "remain J.B. Nevercott for the rest of the campaign". s03:16 retires him after M4. arc-h:79 and :107 use Nevercott at the Shipwright's Ball and for the Pitch. r03 and r10 use him.
10. M2b is already the "Zardoz Betrayal Pitch". arc-h:105–109 and :378 present the Pitch again at Faire, with the Nevercott reveal, and give a different job (500 gp, artifact in Zord's quarters).
11. Zord's origin: "Illuskan" (s03:38, org page), "Waterdavian carnival operator" (Fireball ev-04:30), "Calishite eccentric" (`villains/jarlaxle.md:13`).
12. Jarlaxle's identity is exposed to Harpers in Harper M4 (L5), and to anyone via Fireball ev-04's ledger, before BD's own reveal at the Faire.
13. Harper M4 has Jarlaxle admit he "belongs to BD" (ev-03:32) at L5. BD events teach the BD name at s02 (after M2).

**C. Eye #3**
14. Guide 08:9, arc-h:11 and :15, and `running-the-villains.md:25` say Jarlaxle holds Eye #3 on the *Marpenoth* from before the campaign. m06 ev:18 says the Eye sank in a hired ketch three weeks ago, and Xanathar's divers are racing for it. Guide 08:71 describes the Guild divers placing a limpet charge on the *Marpenoth*. Session 32 flagged this.
15. M6 is L7 and R14. arc-h (L4–6, closes Tarsakh 20) reads **Eye 3 Recovered by BD**, so the reader precedes the writer.
16. Nar'l's tenure is 3 years (m04 ev:16) versus 11 years (arc-f:17, arc-h:15).

**D. Soluun (user note, Session 38)**
17. m04 ev:121 has Krebbyg tell the party Soluun "was disowned" as fact. The Notable Figures page (`02-soluun-xibrindas.md:26`) says it is a cover story.
18. m04 does not read DR M1's **Soluun Captured / Escaped / Killed** (`DR/m01.../ev-01:446–448`). If Soluun is Killed, M4's background (Nar'l covering for his brother) breaks. If Captured, M1 says "Rongquan Mystere" posts surety (DR M1 ev:428).
19. Force Grey M4 has Soluun as a prisoner in Xanathar's X24, "claiming BD affiliation to stay alive" (ev-01:141 and :145; ev-02:75; design-notes:15). That conflicts with DR M1 and with arc-h U3.
20. Jarlaxle's decision on Soluun after DR M1 is a Session 38 handoff item. arc-e:485 and arc-e:337 treat "He's useful" as Jarlaxle's standing position.

**E. Renown and rank text**
21. Guide 08:16 gives an "At Renown 5+" Scarlet Marpenoth extraction. It is not a rank, and r03:49 explicitly excludes the *Eyecatcher*. m06:114 adds "Renown 15+ disguise resources". Session 32 flagged the 5+ one.
22. arc-h:45 and :103 use "Operative rank (Renown 10+)" and "Initiate or Soldier (Renown 1–9)". The ranks are Initiate 1–2, Soldier 3–9, Officer 10–24.
23. Guide 08:33, `player-factions-overview.md:182`, and arc-j:55 put the Vault proposal at "Dread Lord renown". BD has no such rank.
24. The three-favor list, the Uncommon item, the assessment and the 20% fence discount in guide 08:56–60 are not in Appendix B l.790–796.
25. Initiate benefits (safe house aboard the *Heartbreaker* or *Hellraiser*) have no event. Appendix B writes "Hellbreaker".

**F. Coin pouches and tokens**
26. Pouch 2 (100 gp plus "a more interesting assignment" note) is placed in five places: s01:29 and :27 (after M3), first-meeting:111 ("no note"), s02:21 (after M2, from Krebbyg), m03:85 (after M3), and M2b ev:79 (100 gp plus token).
27. M2's payment is 80 gp from Nevercott (m02 ev:82); s02:21 gives 100 gp from Krebbyg.
28. Tokens: M2b's obsidian compass-as-token (m02b ev:79), s03's obsidian tile (s03:94–96), arc-h's BD identification token (arc-h:162), Soluun's forged disc (DR M1).

**G. Locations, calendar, source**
29. M1: Lady Ashford's reception, Vessin (16, a tiefling, in a crate at Net/Dock). Trollskull ev-07:55–57 and Appendix C use the Twin Parades window, "The Handkerchief Job", Maester Bartlethorpe and Mira (about 11, Appendix C l.1463). Trollskull ev-07:26 has the Faire arriving Ches 21. M1's tickets (m01 ev:94) are for the "Faire Debut Parade".
30. Faire calendar: arc-h:9 has Jarlaxle arriving in the last tenday of Ches. s02:39, Krebbyg's "months" and Vessin's 18 months, and Ryvarra's three months (Ryvarra NF:14) predate that.
31. Windmill: M5 puts it in the North Ward (m05 ev:20, :64); Appendix C l.1507 says Southern Ward; Session 32 handoff flagged this; arc-j:75 and :322 call it a "Manshoon outpost".
32. Ott Steeltoes is a halfling in m03:17. Appendix C l.1549 says shield dwarf, WDH l.15075 says "dwarf fishkeeper", and the NF page says dwarf. Appendix C has 6 bugbears on night one, while M3 has 6 Thugs and 2 bugbears.
33. Krebbyg: young and rash (NF:22) versus "twenty years" (m06 ev:40); "sixteen months removed from the Underdark" (s02:31); "worked with Vessin for three years" (m06 ev:44).
34. Mission numbering: M2b is conditional and unnumbered (guide 08:66–71 lists six). r03:15's "Mission 4" and r10's "Post-Mission 4" confuse it.
35. m05 ev:12 ("Zardoz Zord is onstage") conflicts with "Faire is committed to Waterdeep for another season" (m06:112) and Tarsakh 20.

**H. Villain knowledge**
36. R1: guide 08:9 says Jarlaxle competes "with Xanathar or Manshoon". `villains/jarlaxle.md:48` has a Manshoon non-interference pact. `grand-game-in-play.md:65` has a peer arrangement. All of these depend on Session 37's decision 1.
37. R2: m02 ev:17 and :38 and :110 have Jarlaxle write an exposé naming "infernal worship" that "matches the Cassalanter villa's lower temple". `jarlaxle.md:51` says Jarlaxle "knows about their infernal bargain". Appendix C BD-2 does the same. M2b's voided Cassalanter ledger entry and M5's "resolution" are related. Guide 08:11 describes the Cassalanters as holding a "deadline", which arc-g:47 repeats.

**I. Guide and org-page mismatches**
38. Org page `07-bregan-daerthe.md:8` says M1 arrives via theater tickets to Kreb Sorrush, and that M2 is Nevercott at the Portal. That matches the events. Its "After Mission 4" retirement (:11) is correct, and r10 and r03 break it.
39. `trollskull-manor/09:96` and `08-notable-patrons.md:129–133` have Jarlaxle appear in disguise at the tavern each time. s03 says Nevercott disappears.
40. `design-notes-running-the-campaign.md:122` says Vessin is "covered by Krebbyg's entry". The Krebbyg NF page does not cover her.
41. No Notable Figures pages exist for Vessin, Ilphrin Quiss, Pelsha, Vorn, Sarev Oust, Brimel Crestfall, Florette Cressyn, Krenick Durr or Mirilin Ashford.

### 2.3 The six open decisions applied to BD

1. **Villain factions under R1/R2.** BD is R1-clean in the events, but the guide and villain pages break it (contradiction 36). For R2 it matters a lot: M2 is an Act I L3 mission whose whole point is delivering a text naming infernal worship (37). If villains count, M2, M2b's voided entry and M5's "resolution" all need rework.
2. **Manshoon Named.** No BD event needs the gate. If the BD rewrite adds the Jarlaxle–Manshoon material (arc-h, arc-i:45), it should use the DR convention.
3. **Which act owns the first Cassalanter cult evidence.** BD M2 (Act I) is an unlisted third owner. So are Fel'rekt's "Yalah's Asmodean contact" offer (Gralhund ev-06:66, ev-07:76) and M5's windmill plan, alongside Gralhund g16 and Faction Outposts.
4. **OotG pact terms.** Only indirectly. M5's windmill documents (m05 ev:20, :64) and arc-e 6B's windmill overlap, and arc-j:75, :322 mislabels it.
5. **BD Contact Severed per PC.** Directly applicable (A1–A2). A per-PC rewrite changes s04 (:14, :34, :40–41, :53, :65, :74), first-meeting, guide 08:37, `player-factions-overview.md:169–176`, `trollskull-manor/09:96`, and arc-h Path 2 and 3 gating.
6. **Level gates versus readers.**
   - M4 (L5) writes outcomes that arc-f (first heist at L4) reads.
   - M6 (L7, after Kolat Towers) writes the **Eye 3 Recovered by BD** outcome that arc-h reads.
   - Contradiction 15 covers this.
   - r25's Vault reader is the other.

---

## Open questions for the user

1. **BD Contact Severed:** per reporting PC, with the others still recruited, or keep the party-wide lockout? Is it permanent ("for now" in Appendix B)? Does recruitment extend to any PC, or only drow (Appendix B)?
2. **R2 and Jarlaxle:** may Jarlaxle know about the infernal worship at L3, or should M2 be reworked?
3. **Eye #3:** is it aboard the *Marpenoth* from the start (guide, arc-h, villains) or sunk (M6)? How should M6 change?
4. **Jarlaxle's identity ladder:** when does a BD member learn what, given Fireball ev-04, Harper M4, M2b, s03 and the Faire? Does Nevercott retire after M4 or stay through Faire? Is M2b the Betrayal Pitch, or does arc-h's Pitch stay?
5. **Soluun:** where does Jarlaxle's decision land (s02-style event, M4, arc-h, r50)? Does M4 read DR M1's outcomes? Does Force Grey M4's captive Soluun stay?
6. **Renown:** mission awards in the drafts differ from guide base (2/2/3/3/4/4). Which wins? Where does 25 come from, and is 50 left to the Mad Mage?
7. **Rank benefits:** keep the repo's extras (three favors, item, assessment, fence discount) and the Houseless Noble blank favor? Per quest or per arc?
8. **The shipping records:** are they the Officer benefit, a Fireball payoff, or a +2 heist? They are currently all three.
9. **Invented names:** accept Ilphrin Quiss, Pelsha, Vorn, Sarev Oust, Vessin, Brimel Crestfall, Florette Cressyn, Krenick Durr and Mirilin Ashford, or replace?
10. **Ott Steeltoes:** halfling (M3) or dwarf (WDH, Appendix C, NF)? Also the Thugs and Veteran names in m03 and m06.
11. **Spider iconography:** keep r50's spider-and-blade coin and m04's spider chalk mark, written as a rejected symbol, or replace?
12. **Scope:** the DR run logged every outside contradiction and edited only the folder. Does the same rule apply here, including the 9 new design-notes files?

**Key files**
- `/home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe/` (r03, r10, r25, r50, s01–s04, 00-first-meeting, m01–m06, m02b)
- `/home/user/waterdeep/campaign/quests/faction-events/doom-raiders/` (r03-wolf, r10-viper, r25-ardragon, r50-dread-lord and their design-notes)
- `/home/user/waterdeep/campaign/guides/factions/08-bregan-daerthe.md`
- `/home/user/waterdeep/campaign/setting/organizations/07-bregan-daerthe.md`
- `/home/user/waterdeep/campaign/setting/villains/jarlaxle.md`
- `/home/user/waterdeep/campaign/structure/arc-e-faction-outposts.md`, `arc-f-xanathars-lair.md`, `arc-h-sea-maidens-faire.md`, `arc-j-vault-of-dragons.md`
- `/home/user/waterdeep/sources/Appendix_B_-_Player_Factions.md`, `Appendix_C_-_Player_Faction_Missions.md`
- `/home/user/waterdeep/docs/plans/harpers-out-of-scope-notes.md`