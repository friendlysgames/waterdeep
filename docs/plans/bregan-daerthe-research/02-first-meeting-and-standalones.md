# Bregan D'aerthe faction events: research report for the 00-first-meeting, s01–s04 rewrite

I read the five restored drafts, the BD guide, the Notable Figures pages, the structure docs and the three source sets. I changed nothing in the repo.

**Limits of the research**
- I could not open the `.docx` files, so `Jarlaxle Baenre NPC Guide.docx` and `Zardoz Zord (and extra side quest hook).docx` are unread.
- I read these PDFs only in part: PDF 26 pp.1–4, PDF 3 pp.1–3 and PDF 9 pp.1–6.
- Paths below are relative to `/home/user/waterdeep/`.
- `BD/` stands for `campaign/quests/faction-events/bregan-daerthe/`.
- `OOS` is `docs/plans/harpers-out-of-scope-notes.md`.
- `H38` is `session 38 handoff.md`.
- `Brief` is `docs/plans/doom-raiders-conversion-brief.md`.
- The OOS file cites `00-first-meeting` lines up to :206, but the restored file is 128 lines, so those line references came from a different version. The s02 and s04 references still match.

---

## Part 1: Per-folder content fixes

### 00-first-meeting (`BD/00-first-meeting/ev-01-first-meeting.md`, 128 lines)

**What the draft contains**
- Summary at :3-15, in an old `> **[GM]**` zone.
- Scenes:
  - "The Calimshan Merchant", :17-33, with a Ryvarra `[!profile]` at :25.
  - "The Party's Response", :35-57, with three branches: Watch (:39-45), Confront (:47-51) and No Action (:53-57).
  - "The Haberdasher at the Door", :59-95, with a Nevercott `[!profile]` at :87.
- Checks: DC 14 Wisdom (Perception) and DC 17 Intelligence (Investigation) at :21, and passive 18 at :37.
- Outcomes are retired flags at :99 (`Bregan D'aerthe Joined: True / False`) and :103 (`BD Contact Severed: True / False`).
- Next Steps is at :107-115, then Overview (:117), a "Read Aloud" H2 (:121) and Summary (:125).

**Fix list**
1. **Format.**
   - Convert the `> **[GM]**` zones (:3, :107), both `[!profile]` blocks (:25, :87) and the `> >` speech nesting (:63, :69, :73, :81).
   - Convert the `True / False` headings to `[!gamemaster]**Event Outcomes**` and `**Next Steps**`.
   - Replace the "Set/Award" wording (:10, :45).
   - Drop the trailing "Read Aloud" H2 and move it into the scenes as real readalouds.
   - Add a `[!social]`/`[!qna]` block for Nevercott and Ryvarra.
2. **Surveillance cast.**
   - The source watchers are the three lieutenants, not Ryvarra.
   - WDH has Fel'rekt and Krebbyg watching at night and Soluun by day. Appendix B names all three.
   - The draft never mentions them. The Trollskull guide at `ev-04:30` still says "Three drow lieutenants shadow the party".
   - Ryvarra is a remix addition (NF `09-ryvarra.md`).
3. **Missing source check.**
   - The DC 15 Wisdom (Insight) check confirming the watchers target drow PCs (WDH `adventure-wdh.json:3593`, Appendix B :717/:740) is absent.
   - The draft's DC 14 Perception and DC 17 Investigation duplicate Trollskull `ev-03:42-43`.
   - NF Ryvarra's DC 14 is **Insight** (`09-ryvarra.md:22`), not Perception.
4. **Ryvarra timeline.** Draft :19 says "since before the party descended the well". NF says "three months" (`09-ryvarra.md:14`). Finding Floon `ev-01:29` says "every evening for two weeks".
5. **Transplanted text.** Draft :23 ("adjacent stalls cannot describe her face") is the Yawning Portal table text moved to the alley (NF :24). Her Resonance (:27) is copied verbatim from the NF page.
6. **Ryvarra gate.** `ev-03:45` makes her visible "only to … characters who made the Yawning Portal Perception check". Finding Floon `ev-01:29` has no such check, so the gate is unsatisfiable.
7. **Nevercott scene vs Appendix B.**
   - Appendix B (:748-768) has him keep the fiction until a drow PC steps aside.
   - He then lowers his voice, sets the hat down, gives the eye-patch line, says "My name is not J.B. Nevercott … Bregan D'aerthe", offers a first assignment, hands over the black card with a silver ship, and says "I'll be in touch shortly regardless".
   - The draft (:65-77) keeps the fiction until "the door closes", names BD "only if pressed on the card's ship" (:75), gives no concrete assignment (:73 "a small matter"), and never says he will be in touch regardless.
   - It also never states that declining costs nothing (Appendix B :763). The refusal path is missing.
8. **Assignment hand-off.** Draft :73 and :111 imply Nevercott hands over the first mission. M1 actually delivers it by unsigned theater tickets to Krebbyg (`m01 ev-01:94`), and the org page says the same (`07-bregan-daerthe.md:8`). The First Meeting must set up that hand-off.
9. **Drow-only gate.**
   - WDH :1296 says "must be a drow, preferably a male". WDH :3601 has Nevercott speak "privately with drow characters" and says "Only drow are given serious consideration". Appendix B :715 agrees.
   - The remix guide (`08-bregan-daerthe.md:37`) and `player-factions-overview.md:165` say any PC. The draft follows the remix (:13, :85).
   - Apply the remix rule per candidate, with drow PCs getting the closer watch.
9a. **Individual membership (R3).**
   - Rewrite :13, :85 and :101 ("at least one party member accepted") and :111 ("once the party reaches Level 2").
   - **Bregan D'aerthe Joined** should be marked per named recipient. Follow the Harper First Meeting wording (`harpers/00-first-meeting/ev-01-first-meeting.md:366`, "record the name of every character who joined").
   - Do the same for the "Next Steps" (`harpers :370`) and "Without a Private Meeting" summary patterns.
10. **BD Contact Severed scope and permanence.**
    - Draft :43 and :105 close recruitment for everyone, permanently. `OOS:75` and `OOS:237` (decision 5) flag it as an R3 violation, with the per-PC question open.
    - The source says "for the time being" (WDH :3600) and "for now" (Appendix B :719). The remix guide and `player-factions-overview.md:169,:176` say permanent.
11. **Watch timing and name.** Draft :41 says "by that evening", which agrees with `player-factions-overview.md:169` ("within hours") but not s04's "two days". The Watch officer and the sergeant are unnamed. The Doom Raiders rewrite reused a named contact, Sergeant Ilmra Dunfell (`doom-raiders/s01 ev-01:79`).
12. **GM-only reveal in prose.** Draft :77 ("The *hat of disguise* he wears accounts for…") sits in player-facing narration. Move it into a GM block. Draft :9 says "Jarlaxle's Yawning Portal field observer" in the summary, which is fine as GM text.
13. **Invented details.** Draft :93 invents a glass bead, an obscuring cloud and "three tendays". Appendix B and WDH give Nevercott no combat or escape behaviour.
14. **Pouch timing line.** Next Steps :111 says the 100 gp pouch comes "the same afternoon as the Mission 3 debrief". `m03 ev-01:76-85` has Krebbyg collect Ott at dawn on the fourth morning and the pouch arrive that afternoon, with no separate debrief. s01 matches m03.
15. **Missing carry-overs.**
    - The renovation financing offer (`ev-04:60`, "up to 1,250 gp … repayable in operational access") is not carried.
    - Quilm, a drow spy placed as a bouncer candidate (`07-bregan-daerthe.md:42`), is unused.
    - The outcome **BD Acknowledged** is set by `ev-04:118` and `player-factions-overview.md:173`, and read by `fireball/flowchart.md:53`. The draft sets it nowhere.
16. **Milestone.** The Next Steps should state "awards no Milestone Points". `ev-04:15,:130` carries the quest-level point.
17. **Voices.** There is no Nevercott profile in `.claude/skills/character-voices/voices/bregan-daerthe.md`; the Ryvarra profile is at :170-184. The drafter needs a Nevercott voice invented from the event text and listed in the design notes. No design-notes file exists for this folder.
18. **Clean.** There are no hits for Manshoon, Splinter, Floxin, Lolth, Cassalanter or infernal in the five folders.

### s01-coin-pouches (`BD/s01-coin-pouches/ev-01-coin-pouches.md`, 58 lines)

**What the draft contains**
- Summary at :3-12, in a `> **[GM]**` zone.
- Beat 1 (:14-23): the 50 gp pouch with an anchor-scratched silver piece, plus an `[!info]` "Tracing the Pouch" block.
- Beat 2 (:25-33): the 100 gp pouch with the note *A more interesting assignment follows shortly.*
- The flag `Coin Pouches: True / False` at :37, Next Steps at :41-45, Overview (:47), a Read Aloud covering Beat 1 only (:51-53) and Summary (:55-57).
- There are no checks except the Investigation DC 13 callback (:10, :23).

**Fix list**
1. **Format.** Convert the `[GM]` zones (:3, :41), the `[!info]` block (:22), the flag (:37) and the "Read Aloud" H2. Add the "awards no Milestone Points" line.
2. **Outcome with no reader.**
   - :39 says **Coin Pouches** is "Read by the **Dinner with Zardoz**" event. s03 never reads it. It reads **Nar'l Eliminated** and **Nar'l Active** only.
   - Either s03 reads it or the outcome goes.
   - Next Steps :45 duplicates s03's Nar'l gate.
3. **Anchor logic.**
   - The anchor link is gated on the DC 13 Investigation check (:10, :23). In `m01:44` that check only notices the *knot spacing* is irregular.
   - The silver anchor itself is visible to everyone in the m01 readaloud (`m01:98`: "silk handkerchief embroidered with a silver anchor").
   - Rewrite the gate. The DC 17 decode (`m01:46`) is the harder lead.
4. **Timing.**
   - Beat 1 at :16 ("two days after the debrief") matches `m01:82`.
   - But m01 puts the debrief "the following morning" (`m01:80`), so the pouch lands on day three of the mission.
   - Beat 2 (:7, :27) matches `m03:83-85`, afternoon of the fourth day.
   - The disagreement is in `00-first-meeting:111` and `08-bregan-daerthe.md:14` ("after Missions 1 and 3"). Decide one canonical timing. `H38:213` and `OOS:83` list this as open.
5. **Duplicate note text.** *A more interesting assignment follows shortly* appears in s01:31, `m03:85` and s02:21, and the guide describes it at `08-bregan-daerthe.md:14`. It should live in one event.
6. **Recipient (R3).**
   - Only BD members ran M1 and M3, but the pouch goes to "Trollskull Manor's front door" (:16, :27).
   - `OOS:9` allows "expressly party-wide gifts". State that explicitly, or say who holds the gold.
7. **No decisions or checks.**
   - :6 says "no player choice" and :23 has an unrolled canvass.
   - Per CLAUDE.md's mission-depth rule, a standalone event can be short, but the drafter should add real beats. Candidates: a Krebbyg question answered in voice ("Ask Fel", `bregan-daerthe.md:80-95`), and a decode lead that connects to Vessin.
8. **Krebbyg.** :11 says "does not engage the question", which is off his voice profile. His profile is rapid run-ons, "darling", never plans.
9. **Source cross-check.**
   - WDH :1305 says only "small, unmarked black pouches of coins from an anonymous source". There are no amounts, notes or anchors.
   - The 50 gp, 100 gp, anchor and note are remix inventions.
   - The org page says Krebbyg carries a 100 gp payment note with a *velvet* pouch signed "J." (`07-bregan-daerthe.md:38`). s01 uses black *linen*.
   - WDH :1307's third support, "buy off or quietly dispose of individuals who threaten the adventurers", is implemented nowhere in the BD folder that I found.
10. **Anchor reuse.** Appendix C's BD-1 (`:1429-1470`) has a different handkerchief: a perfumed one from Roderick Bartlethorpe at the Twin Parades. s01's anchor thread depends on the m01 draft being kept.

### s02-kreb-drops-the-cover (`BD/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md`, 85 lines)

**What the draft contains**
- Summary at :3-13, including "No checks required" at :13.
- Scene at :15-41: Krebbyg hands over a 100 gp envelope and card, then names Bregan D'aerthe (:29). Two checks follow, DC 13 Persuasion at :33 and a 17+ result at :37.
- A `[!info]+` nested inside a `[GM]` block at :43-49.
- Flag `Kreb Unmasked: True` at :53, Next Steps at :56-62, `#### Milestone: None` at :64-66, Overview (:68), Read Aloud (:72-80) and Summary (:82-84).

**Fix list**
1. **Format.** Convert the `[GM]` zones (:3, :43, :56), the nested `> > [!info]+` (:45-49), the flag (:53) and `#### Milestone: None` (:64). Fix the :13 contradiction: "No checks required" against the Persuasion checks at :33/:37.
2. **Broken premise.** The event says Krebbyg names BD "for the first time" (:9, :29, :84). By M2:
   - Members enrolled via Nevercott, who names BD (Appendix B :761, `ev-04:45`, the guide, and the 00 draft :75).
   - `Bregan D'aerthe Joined` is already set.
   - So there is nothing to "unmask" for the organization name.
   - If the event is really about dropping the booking-manager cover ("Kreb Sorrush", `04-krebbyg-masqilyr.md:22`, `07-bregan-daerthe.md:7`), the draft never says that. Krebbyg is "Krebbyg" throughout.
3. **Payment conflict.**
   - `m02 ev-01:82` has J.B. Nevercott pay **80 gp in person at the Yawning Portal** two days after publication.
   - The org page agrees (`07-bregan-daerthe.md:8`: "Mission 2 by J.B. Nevercott in person").
   - s02:19-21 has Krebbyg pay **100 gp** at the theater.
4. **Betrayal Pitch trigger.** There are three different triggers:
   - s02:47 and :60: a BD member who met Nevercott "during The Wazoo Affair".
   - `m02 ev-01:84`: Nevercott hints at a boat only "if the party completed Mission 2 with supplementary renown".
   - `m02b overview:10-12`: any BD member who met Zardoz at the Faire or Nevercott in M2.
   - Pick one source of truth.
5. **Outcome with no reader.** :54 says **Kreb Unmasked** is read by M3–M6 "where Krebbyg no longer speaks around the name". A grep finds it only in s02 and s04:34. No mission reads it.
6. **Invented backstory.**
   - ":31 sixteen months removed from the Underdark" is not in the NF page, which says "house was destroyed long ago" (:22).
   - ":39 We've been here a few months" sits against Ryvarra's three months.
   - Drop or reconcile both.
7. **Krebbyg voice.**
   - The draft's calm, watchful, thumb-on-crossbow Krebbyg ("tilts head, watching how it lands") contradicts the voice profile (`bregan-daerthe.md:80-95`): rapid run-ons, "darling", "Ask Fel", never plans, constant backstage swearing.
   - He has no Fel'rekt beat.
   - No swearing appears, though the profile says "Punctuation · Colourful".
8. **Disguise.**
   - `m01:96` calls him "a half-shade too still for a human", so he is disguised ashore.
   - s02 writes him with a holstered hand crossbow and "hair loose" and never says whether he is seen as a drow.
   - WDH ties the disguise to the ship's figurehead (WDH :4751, :23047), so ashore the lieutenants are drow (`09-response-teams-at-the-tavern.md:96`: Fel'rekt "does not disguise his heritage").
9. **Gate.**
   - :62 gates M3 on "Renown 4".
   - That matches `m03/overview:6`.
   - BD gates (0/2/4/7/10/14) differ from the Doom Raiders and Harper scheme (0/3/5/8/10/13).
10. **R3.** :7, :25 and :51 treat the whole party as attending (`OOS:78`). Briefs for members only.
11. **Calendar.** "Tenday afternoons" (:15) is plausible: PDF 9's "last tenday" and the Seven Masks' schedule support it. No date anchor exists for the M2→M3 gap. The Faire parade dates are Ches 10, 21, 25, Tarsakh 1 and 5; the Faire leaves Tarsakh 20 (PDF 9 pp.69-70).
12. **Card text.** The card (:21) repeats the note text that s01 and m03 already use.

### s03-dinner-with-zardoz (`BD/s03-dinner-with-zardoz/ev-01-dinner-with-zardoz.md`, 117 lines)

**What the draft contains**
- Summary at :3-14.
- A retired `[!design]` block ("J.B. Nevercott Is Retired") at :15-16.
- DM background at :18-22.
- Scenes: The Invitation (:24-32), The Dining Room (:34-44), "Playing Zardoz at Dinner" (:46-52), The Conversation (:54-70, three questions) and a conditional remark (:72-80).
- The flag `Zardoz Introduced: True / False` at :84-86, and a Next Steps token (:88-96).
- `#### Milestone: None` at :98-100, Overview (:102), Read Aloud (:106-112) and Summary (:114-116).
- No checks.

**Fix list**
1. **Format.** Convert `[GM]` zones (:3, :46, :88), `[!design]` (:15), the `> >` speech nesting, the "flag" language (:7, :12, :74), the flag heading (:84) and `#### Milestone: None` (:98). Move the Read Aloud into scenes.
2. **WDH dinner differs from the draft.** WDH :4712-4752 ("Dining with Zardoz Zord"):
   - Venue: aboard the *Eyecatcher*, in the captain's dining cabin J10.
   - Trigger: PCs caught aboard or asking for the owner; a *Sending* contacts Zord.
   - Zord feigns ignorance of the Stone and politics.
   - Insight is DC 24 ("much more to him than meets the eye").
   - Jarlaxle gives out four facts: a Luskan-based carnival, three ships, nimblewrights from Lantan, and the harmless valets.
   - He "doesn't know much about them (yet)".
   - Its twin line, WDH :1306, says "takes their measure and offers assistance if they impress him".
   - The draft moves the venue to a hidden room at the Seven Masks (:34-36). `r10:26-28` and `r25:23` place Zardoz aboard the *Eyecatcher* salon.
   - The three questions and the token are remix inventions.
3. **"First time" is false.** :9 says the party meets Zardoz "for the first time". Prior meetings:
   - Field of Triumph (`ev-05:9,:19,:77`; Zord sponsors and watches, with an Insight DC 18).
   - Fireball `ev-04:26-34` and :138-142. Zord's office meeting there leaves the party knowing "Jarlaxle Baenre behind the Captain Zord persona".
   - Gralhund `ev-01:41-57`.
   - `trollskull 09:96` (Fel'rekt's dinner invitation).
   - It also contradicts the note signed "—Z.Z." (`m03:83`).
4. **Identity secrecy conflicts.**
   - :22 says Jarlaxle "has no intention of revealing" the link between Zord and Nevercott.
   - `jarlaxle.md:3` keeps identity hidden until the Faire. `player-factions-overview.md:178` says it surfaces in Fireball and the Faire. `fireball ev-04:138` identifies him.
   - The cover descriptor varies: s03 "Illuskan" (WDH :1300 agrees); `jarlaxle.md:13` "Calishite eccentric"; `fireball ev-04:30` "Waterdavian carnival operator".
5. **Nevercott retirement is inconsistent.**
   - s03:15-16 retires him after the dinner (after M4).
   - `r10:9,:16-26` retires him after Three Nights (M3), as does `r25:7`.
   - `r03:15` mislabels Three Nights "Mission 4", which `OOS:82` also flags.
   - Structure docs keep using him: `arc-h:79` (Shipwrights' Ball), `arc-h:105-107` (the Betrayal Pitch), `arc-b:126`, `ev-04` and the org page (`07-bregan-daerthe.md:31`).
6. **Zardoz voice is wrong.** `bregan-daerthe.md:7-22` says Zardoz is loud, hearty and exclamatory, calls everyone "my darlings", offers free tickets constantly, and **never mentions the Underdark, drow or Luskan politics and never lets a silence go unfilled**. The draft's :50-52 "warm but precise … lets pauses run long" is the real-Jarlaxle voice (profile :26-40). The precise-question-buried-in-bluster tell (:14) is the correct way to hide the three questions.
7. **Nar'l gating is inconsistent.**
   - :12, :72-80 (and :74) gate the remark on "Nar'l Active True and Option C succeeded".
   - m04's own outcome (`m04 ev-01:77`) says Active covers Options A or C.
   - Option B (Nar'l Extracted) is unhandled, though the dinner still fires.
   - The draft's remark copies `m04:99` verbatim.
8. **Token and readers.**
   - The obsidian tile (:94-96) has no reader anywhere. Nothing in `campaign/structure/arc-*.md` mentions "obsidian", "operational token" or **Zardoz Introduced**.
   - `arc-h:162` has a different BD identification token that suppresses the training mannequins (J31).
   - `m02b` already uses an "obsidian compass" prop. The First Meeting black card with a silver ship is reused as the device (:32).
9. **Duplicate dinner offers.** `trollskull 09:96` has Fel'rekt invite a BD member to "Remalia's, Thursday". `fireball ev-04:106-112` gives BD members a private cabin meeting with Jarlaxle.
10. **R3.** The dinner is a party-wide arrangement (:5-12). WDH offers it to whoever investigates the Faire.
11. **Thin mechanics.** There are three questions and no decision, check or consequence. `08-bregan-daerthe.md:50` gives "+1 Impress Jarlaxle (once per quest)" as the only renown hook. The Krebbyg invitation says "that evening — not his usual morning hour" (:26), while `m04:111` has him arriving "early afternoon".
12. **Milestone.** Remove `#### Milestone: None` (:98).

### s04-contact-severed (`BD/s04-contact-severed/ev-01-contact-severed.md`, 75 lines)

**What the draft contains**
- Summary at :3-14.
- "The Absence", :16-22, with a DC 13 Wisdom (Perception) check and a one-sentence list of other faction approaches.
- A `[!warning]` (:24-28).
- Downstream consequences (:30-47).
- The flag `BD Contact Severed: True` at :49-52, Next Steps (:54-58) and `#### Milestone: None` (:60-62).
- Overview (:64), Read Aloud (:68-70) and Summary (:72-74).

**Fix list**
1. **Format.** Convert the `[GM]` zones, the `[!warning]` (:26, old title style), the flag (:51), `#### Milestone: None` (:60) and the Read Aloud H2. The event restates an outcome the First Meeting already sets (the draft calls it "Already set", :52). One event should set it, and the other should read it.
2. **Per-PC scope (R3, decision 5).** `OOS:76` and `OOS:237` flag it as party-wide. :14, :34, :40 ("There are no BD-member PCs"), :53, :65 and :74 assume no PC joined another way. If the outcome becomes per reporting PC, the event must handle mixed parties and the Path 1/2/3 closures change.
3. **Timing.** :9 and :18 say watchers vanish **two days** after the Watch visit. The First Meeting draft says "by that evening" (:41), and the GM guide says "within hours" (`player-factions-overview.md:169`).
4. **Other factions' approaches (:20) contradict their First Meeting events.**
   - The Harpers "arrange a quiet moment in a side street". The Harper event uses a paper bird and a tailor (`harpers/00-first-meeting/ev-01:24,:44`).
   - The Order of the Gauntlet "follows a lead to the tavern door" contradicts Savra's in-person visit (`ev-04:28`).
   - Emerald Enclave, Doom Raiders and Force Grey are omitted. `ev-04:25-31` gives each its own delivery.
   - These are also members-only events.
5. **"No theater tickets" (:10).** `fireball ev-01:206` and `08-bregan-daerthe.md:29` fire theater tickets for any investigating party, with no BD gate.
6. **Downstream claims vs other docs.**
   - ":41 no channel": Gralhund `ev-01:41-57` runs Jarlaxle's brief for all parties once **Jarlaxle Informed** is set. `fireball ev-04` has an open meeting.
   - ":39 Path 2 closed": `arc-h:101` makes Path 2 available to any party with faction commitments.
   - ":41 Pitch does not fire": `arc-h:105` allows the Pitch via Jarlaxle's independent interest from Fireball.
   - `trollskull 09:96` agrees that Fel'rekt's dinner never fires for a Severed party.
7. **Permanence.** The source says "for the time being" (WDH :3600) and "for now" (Appendix B :719). The remix says permanent (guide, :14).
8. **Reader.**
   - :52 and :58 say **BD Contact Severed** is read by Sea Maidens Faire Scene 3. arc-h never uses the name.
   - arc-f:214 states the parallel-heist trigger in prose (the party "has not allied with Jarlaxle or joined Bregan D'aerthe").
   - `trollskull 09:96`, `jarlaxle.md:3`, `fireball/flowchart.md` and `trollskull-alley/flowchart.md:54,:83` do read the outcome.

---

## Part 2: Readers and writers

| Outcome | Written by | Read by (actual) | Notes |
|---|---|---|---|
| **Ryvarra Identified** | `trollskull ev-03:47,:57` (retired flag); 00 draft :10 also sets it | 00 draft :21, :57, :79; `ev-04:45`; `trollskull flowchart:79`; `jarlaxle.md:3` | Setter lives out of scope in Trollskull `ev-03`. |
| **Bregan D'aerthe Joined** | `ev-04:115` (party-wide flag); 00 draft :99 | 00 draft claims **The Factions Come Calling**, the Factions guide, and **Faction Outposts** | No file uses the exact name. Real consumers say "BD member/operative": `fireball ev-04:106`, Gralhund `ev-01:45`, `arc-f:214`, `arc-h:45`, `arc-e:329`, `trollskull 09:96`. |
| **BD Contact Severed** | `ev-04:121`; 00 draft :45, :103; `player-factions-overview.md:169,:176` | s04; `trollskull 09:96`; `jarlaxle.md:3`; `trollskull flowchart:83` | `arc-h` states the effect without the name. |
| **BD Acknowledged** | `ev-04:118`; `player-factions-overview.md:173` | `fireball/flowchart.md:53` | The 00 draft does not set it. |
| **Coin Pouches** | s01 :37 | Nothing (:39 claims s03) | Dangling. |
| **Kreb Unmasked** | s02 :53 | s04:34 only (it says it is never set) | The M3–M6 readers claimed at :54 do not exist. |
| **Zardoz Introduced** | s03 :84 | Nothing | :86 claims **Sea Maidens Faire**; arc-h has no match. |
| **Nar'l Active / Eliminated** | m04 `ev-01:75-83` | s01:45, s03:7, :12, :72-74; `arc-f` (Nar'l Active) | s03 never handles Extracted. |

**Unset reads.** s01, s03 and s04 read **Nar'l Eliminated**, **Nar'l Active**, **Handkerchief decode (DC 13)**, and **BD Contact Severed**. All are set elsewhere. Outcomes read by s02/s03 that nothing sets: none beyond the above.

---

## Part 3: Source facts per folder

### 00-first-meeting
- **WDH :3592.** "If one or more characters are drow, Jarlaxle Baenre has his lieutenants, three drow gunslingers, shadow these potential new recruits… Fel'rekt Lafeen and Krebbyg Masq'il'yr watch the characters at night, and Soluun Xibrindas watches them during the day (doing his best to stay out of the sunlight)."
- **WDH :3593.** "Characters who have a passive Wisdom (Perception) score of 18 or higher see fleeting glimpses… a successful DC 15 Wisdom (Insight) check… ascertain that these spies are paying particular attention to the activities of the drow party members."
- **WDH :3600-3602.**
  - "If the party reports the drow to the City Watch, Jarlaxle ends the surveillance and breaks off all contact… for the time being."
  - "if the characters try to confront the drow spies… leave behind a black eye patch as a calling card. The next day, Jarlaxle… shows up at the party's headquarters, using his hat of disguise to appear as a haberdasher named J.B. Nevercott."
  - "asks to speak privately with drow characters… As a test, he offers them their first mission."
  - "Even if the characters discern his true identity, he never admits to being anything other than what he pretends to be."
- **WDH :1296.** "A character must be a drow, preferably a male, to join this faction."
- **WDH :1298.** A female drow can join by "decrying the drow matriarchy"; non-drow operatives "aren't considered members".
- **Appendix B :715-719 and :740-768.**
  - The same three-branch structure, with passive Perception 18 and a DC 15 Insight check.
  - The haberdasher dialogue: "J.B. Nevercott, Sea Ward, hats and accessories of quality".
  - He keeps the fiction "until a drow character steps aside".
  - He then says "The eye patch… A calling card" and "My name is not J.B. Nevercott. I represent an organization called Bregan D'aerthe".
  - He produces "a card — not the haberdasher's card, but plain black with a ship embossed in silver".
  - "Small enough that declining costs you nothing."
  - "I'll be in touch shortly regardless."
- **Appendix B :731.** The BD contact is "Zardoz Zord… a man who chose delight as a survival strategy." The remix option has the PCs join from the Yawning Portal (:726-727).
- **PDF 26 p.3 (Jarlaxle's Alliance).** The alternative opening makes the Yawning Portal contact Jarlaxle himself, and the party BD members from the start.
- **Guide and NF.**
  - `08-bregan-daerthe.md:37`: offer extends to any party member, "a haberdasher named J.B. Nevercott… names Bregan D'aerthe and offers a first small assignment. He leaves a black card with a silver ship."
  - `player-factions-overview.md:165-173`: any PC is a candidate; Watch reported is permanent; Nevercott knocks "regardless of whether the party noticed the watchers".
  - `09-ryvarra.md:12-26`: Spy; Calimshan cloth merchant; "DC 14 Insight" for the slipping accent; "reserved table"; "three months".
- **Trollskull cross-references.**
  - `ev-04:30` (three lieutenants shadow the party, "Any PC; drow PCs draw the closest watch").
  - `ev-04:45` (BD recruitment).
  - `ev-04:60` (financing, up to 1,250 gp).
  - `ev-04:118,:121` (BD Acknowledged, BD Contact Severed).
- **Calendar.**
  - Renovation runs Ches 1–20 (`structural-rules.md:42-43`).
  - The Faire's first parade is Ches 10 (PDF 9 p.69).
  - `ev-04:21` says invitations arrive "over the course of the renovation period".
  - M1 requires 2nd level.

### s01-coin-pouches
- **WDH :1305.** "The adventurers receive small, unmarked black pouches of coins from an anonymous source." No amounts or timings.
- **WDH :1307.** Third support: "Bregan D'aerthe members buy off or quietly dispose of individuals who threaten the adventurers (usually without asking)."
- **Guide `08-bregan-daerthe.md:14`.** The pouches are "50 gp with no note, then 100 gp with a short note promising a more interesting assignment" after Missions 1 and 3.
- **M1 and M3 anchors.**
  - `m01:82`: pouch two days after the debrief.
  - `m01:44-46`: DC 13/15/17 on the knots.
  - `m01:98`: the handkerchief "embroidered with a silver anchor".
  - `m03:76-85`: Krebbyg takes Ott at dawn on the fourth morning; the afternoon pouch and note.
- **Appendix C (BD-1).** No pouch; the handkerchief is a bergamot-scented one from Roderick Bartlethorpe.

### s02-kreb-drops-the-cover
- No source event. Source facts it must honour:
  - **Krebbyg.** NF `04-krebbyg-masqilyr.md:22,:24,:26`: "Kreb Sorrush", booking manager; "house was destroyed long ago"; follows Fel'rekt's lead; Fel'rekt's close friend. Voice at `bregan-daerthe.md:80-95`.
  - **Org page.** `07-bregan-daerthe.md:7-8`: Mission 1 by tickets to Kreb Sorrush; Mission 2 by Nevercott at the Yawning Portal; Missions 3–6 through Krebbyg.
  - **M2.** `m02 ev-01:82` (80 gp) and `ev-01:84` (the boat hint).
  - **Betrayal Pitch.** `m02b overview:8-12`.
  - **WDH.** The lieutenants are drow, and ship crews are disguised aboard their vessels (WDH :4751, :23047).

### s03-dinner-with-zardoz
- The WDH dinner is quoted in Part 1, point 2 (WDH :4712-4752, :1306).
- **WDH :22948.** "If they take a kick-in-the-door approach and storm the vessels… he arranges to meet with them in the guise of Zardoz Zord."
- **WDH :23027.** DC 15 Charisma plus the Zord name gets an audience with a ship captain.
- **Zord's cover.**
  - WDH :1300: "flamboyant Illuskan captain named Zardoz Zord".
  - Voice at `bregan-daerthe.md:7-22`.
  - NF `01-jarlaxle-baenre.md:22`: "a flamboyant human sea captain".
- **PDF 9 pp.69-70.** The Ches 10/21/25 and Tarsakh 1/5 parades, Zord's irregular absences from the *Eyecatcher*, and the Tarsakh 20 departure (matching `structural-rules.md:50`).
- **Remix rank names.** `08-bregan-daerthe.md:54-60` uses Initiate/Soldier/Officer/Commander/Houseless Noble, but `arc-h:45,:103` uses "Operative".
- **Zord already met.** `ev-05` (Field of Triumph), `fireball ev-04` and Gralhund `ev-01:41-57`. The Gralhund event fires for all parties once **Jarlaxle Informed** is set.

### s04-contact-severed
- **WDH :3600** and **Appendix B :719**: "for the time being" and "for now".
- **Remix.**
  - Guide `player-factions-overview.md:169,:176`: permanent.
  - `08-bregan-daerthe.md:37` and `jarlaxle.md:3` agree.
  - `trollskull 09:96`: the Fel'rekt dinner never fires.
- **Faire.**
  - `arc-h:101-109` (three paths and the Pitch).
  - `arc-h:276` (Patron).
  - `arc-f:214` (the parallel-heist condition).
- **Escalation.** `08-bregan-daerthe.md:122-124`: BD reaches for leverage before force. The arc-e outposts use the same logic (`arc-e:317`).

---

## Part 4: Open items from `session 38 handoff.md` and `OOS`

- **Coin-pouch timing.** Disagreement among `00-first-meeting` Next Steps, s01/m03 and the guide (`OOS:83`, `H38:213`).
- **Ryvarra visibility under individual membership.** `H38:226`: "Confirm the intended BD `ev-03` Ryvarra visibility under individual membership". Finding Floon `ev-01:29`, Trollskull `ev-03:42-47` and the 00 draft all disagree.
- **BD mission numbering.** `r03:15` and `r10` call Three Nights "Mission 4" (`OOS:82`, `H38:212`).
- **BD Contact Severed per PC or party-wide.** `OOS:75-76`, decision 5 at `OOS:237`, and `session 37 handoff.md:86`.
- **Retired blocks in BD s01–s04.** `OOS:84`.
- **`#### Milestone: None`.** `H38:236`. s02, s03 and s04 still carry it.
- **Soluun's fate.**
  - `H38:168`: Jarlaxle must decide what to do if Soluun survives DR M1, "most likely expelling him"; logged at `OOS:319`.
  - `OOS:320`: `m04 ev l.37` calls him "disowned".
  - Relevant to the 00 surveillance cast, since WDH has Soluun watching by day.
- **Renown and rank mismatch.** `H38:232`: reconcile the guide's "Renown 5+ Scarlet Marpenoth extraction" with the 3/10/25/50 ranks. `H38:233`: the BD M6 limpet-charge summary and the windmill ward.
- **Invented names.** `H38:241` lists Ilphrin Quiss, Pelsha and Vorn, and Sarev Oust. None appear in my five folders.
- **R1/R2.** `OOS:73` rates BD clean on Manshoon, Splinter, Floxin and the Cassalanter secret. I confirmed that for these five folders.
- **BD guide and Villains pages.** `OOS:128` and `OOS:141,:156` flag `08-bregan-daerthe.md:9` (competing with Manshoon) and `jarlaxle.md:48,:51` (mutual knowledge). They are outside the five folders.

---

## Part 5: Open questions for the user

1. **Who watches in the First Meeting.** Use WDH's three lieutenants, the remix's Ryvarra, or both? Soluun by day collides with DR M1's stalker.
2. **Drow-only or any PC.** Source says drow, remix guide says any PC. Per candidate either way?
3. **BD Contact Severed.** Per reporting PC or party-wide? Permanent (remix) or "for the time being" (source)? s04 is conditional on this.
4. **Who names BD first, and when.** Nevercott does at the First Meeting (source). So what does s02 reveal? Is it the dropped booking-manager cover ("Kreb Sorrush"), and does Krebbyg appear as a drow or in human guise?
5. **M2 payment.** Nevercott's 80 gp at the Portal (m02) or Krebbyg's 100 gp at the theater (s02)? Where does the *A more interesting assignment follows shortly* note live: s01, s02, or M3?
6. **Pouch timing and recipients.** One timing for pouch 2? Are the pouches party-wide gifts or member-only? Should WDH's third support (buying off or disposing of threats) get any event?
7. **Dinner venue and trigger.** Eyecatcher (WDH, r10, r25) or Seven Masks (draft)? After M4 or after a Faire investigation? Does it fire only for BD members? How does it fit Field of Triumph, Fireball `ev-04`, and Fel'rekt's "Remalia's, Thursday" invitation?
8. **Nevercott's retirement point.** After M3 (r10/r25), after s03 (draft), or never (arc-h)?
9. **Operational token.** Keep it with an arc-h reader (the guide's J31 identification token is related), or cut it along with **Zardoz Introduced**?
10. **Zardoz at dinner.** The voice profile says loud and bluster, while the draft's Zardoz is quiet and precise. Which wins? Does Zardoz stay "Illuskan"?
11. **Betrayal Pitch trigger.** `m02`, `m02b` and s02 give three different conditions. Which is canonical?
12. **BD renown gates.** BD uses 0/2/4/7/10/14; Doom Raiders and Harpers use 0/3/5/8/10/13. s02 quotes "Renown 4".
13. **Dangling outcomes.** Cut **Coin Pouches**, **Kreb Unmasked** and **Zardoz Introduced**, or give them real readers? Keep **BD Acknowledged**?
14. **Out-of-scope edits.** Trollskull `ev-03` (the Ryvarra setter), `ev-04:118-121` and Fireball `ev-01:206` hold the other halves of these outcomes. Confirm they stay logged, not edited.

---

## Files consulted
- Drafts, `BD/`:
  - `00-first-meeting/ev-01-first-meeting.md`
  - `s01-coin-pouches/ev-01-coin-pouches.md`
  - `s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md`
  - `s03-dinner-with-zardoz/ev-01-dinner-with-zardoz.md`
  - `s04-contact-severed/ev-01-contact-severed.md`
- Neighbouring BD events: `m01`, `m02`, `m02b`, `m03`, `m04`, `r03`, `r10`, `r25`.
- `CLAUDE.md`
- `sources/SOURCE_GUIDE.md`
- `sources/adventure-wdh.json` (:1296-1309, :3592-3635, :4709-4752, :14780-14802, :22948, :23023-23047)
- `sources/Appendix_B_-_Player_Factions.md` (:693-816)
- `sources/Appendix_C_-_Player_Faction_Missions.md` (:1416-1470)
- `sources/26. Addendum Other Collaborators.pdf` (pp.1-4)
- `sources/3. Player Character Factions.pdf` (pp.1-3)
- `sources/9. Lair – Sea Maidens Faire.pdf` (pp.1-6)
- `docs/plans/doom-raiders-conversion-brief.md`
- `docs/plans/harpers-out-of-scope-notes.md`
- `session 38 handoff.md`
- `campaign/guides/factions/08-bregan-daerthe.md`
- `campaign/guides/gm-guide/player-factions-overview.md`
- `campaign/guides/gm-guide/structural-rules.md`
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md`
- `campaign/setting/organizations/07-bregan-daerthe.md`
- `campaign/setting/villains/jarlaxle.md`
- `campaign/setting/notable-figures/bregan-daerthe/` (Jarlaxle, Soluun, Fel'rekt, Krebbyg, Ryvarra)
- `.claude/skills/character-voices/voices/bregan-daerthe.md`
- `campaign/quests/act-i/trollskull-alley/` (`ev-03`, `ev-04`, `ev-05`, flowchart)
- `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md`
- `campaign/quests/act-ii/fireball/ev-01`, `ev-04`, flowchart
- `campaign/quests/act-ii/gralhund-villa/ev-01-what-the-factions-say.md`
- `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md`, `s01`
- `campaign/quests/faction-events/harpers/00-first-meeting/ev-01-first-meeting.md`
- `campaign/structure/arc-e`, `arc-f`, `arc-h`, `arc-j`