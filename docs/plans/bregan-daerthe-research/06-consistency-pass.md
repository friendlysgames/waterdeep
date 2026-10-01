BREGAN D'AERTHE EVENT QA PASS (Session 39). No files edited. Scope: every file under /home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe/ (00-first-meeting, m01-m06, s01-s05, r03/r10/r25/r50, plus design notes). M2b is confirmed gone. Line numbers are in the current files. "BD" below is the folder root.

Checked clean:
- Gates and base Renown. Join/L2, R3/L3, R5/L4, R8/L5, R10/L6 and R13/L7 are stated identically in every overview, Next Steps and Concluding block. Base Renown is 2/2/3/3/4/4. Rank thresholds are 3/10/25/50.
- Contacts. Nevercott briefs M1 (dusk Ches 20 at the manor), M2 (Portal) and M4 (letter). M3 has no brief. s03 is the handover. The Faire sails on Tarsakh 20 everywhere.
- Hard rules. "Jarlaxle" appears in speech or readaloud only behind **Jarlaxle Unmasked** gates. Lolth is mentioned only with contempt. No Cassalanter infernalism is known in-fiction. No Thug, bare Veteran, Cult Fanatic, Drow or Swashbuckler appears. Retired blocks, "Arc X" labels and M2b/Pitch text are absent from event files.
- Every event ends "awards no Milestone Points".

BLOCKING

1. **Soluun Sold the Mooring has no reader in r50 (the known gap).**
   - M6 claims the reader at m06-the-dive/ev-01-the-dive.md:355, overview.md:57 and ev-02-before-dawn.md:233.
   - r50-houseless-noble/ev-01-houseless-noble.md:133-139 branches Soluun's empty seat only on Expelled, Killed and Killers Named.
   - r50:467 never records the Sold the Mooring branch.
   - Fix: add a paired readaloud at r50:133 for "Soluun Expelled and Soluun Sold the Mooring" (Fel'rekt says Soluun sold the berth to Xanathar's divers and the captain has not spoken his name since). Keep the existing Expelled readaloud for "Expelled, not Sold the Mooring". Add the Sold branch to the "Soluun branch" list in the BD Houseless Noble outcome at r50:467.

2. **r50 does not read BD Commander.**
   - r25-commander/ev-01-commander.md:338 says Houseless Noble "requires it".
   - The r50 Hook (:15-19) has no gate, unlike r25:16, which holds the event until BD Officer is marked.
   - Fix: add to r50 Hook: "Hold this Event until **BD Commander** is marked for the member."

3. **r10 does not read BD Soldier.**
   - r03-soldier/ev-01-soldier.md:319 says "Read by the Officer rank event as its prerequisite".
   - r10-officer/ev-01-officer.md:14-20 keys only on Renown 10 and Zardoz Introduced.
   - Fix: add "Hold this Event until **BD Soldier** is marked for the member" to the r10 Summons, or cut the claim at r03:319 (keep Faction Outposts, unconverted).

4. **Kreb Unmasked is not read by r50.**
   - s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:282 and design-notes.md:27 list Houseless Noble as a reader.
   - r50 shows Krebbyg as himself unconditionally (:129-209, :205).
   - Fix: delete "and Houseless Noble" from s02:282 and s02 design-notes:27. Alternatively add a line in the r50 "What Is Actually True" saying every member at Renown 50 has the outcome.

5. **Seven Masks Back Room is claimed by Officer and Commander, which do not read it.**
   - Claims: m05-the-theaters-back-room/ev-01:443 and :474, and ev-02-the-debrief.md:168 and :195.
   - r10:14-17 and r25:20-25 have no dressing-room branch.
   - r25 design-notes:35 admits this. Only r50 (:33-51, :353) implements it.
   - Fix: change the four M5 lines to "and the rank event **Houseless Noble**". Alternatively add the branch to r10 and r25.

6. **Post-Faire meeting place for Zardoz contradicts across the rank events.**
   - r10:17 says Zardoz receives the member in the "stage manager's office" (P6).
   - r25:23 says a "hired lighter" at the end of the Dock Ward piers.
   - r50:55-81 uses the Marpenoth state.
   - Fix: pick one. For example, make r10:17 read "the same hired lighter used in Commander".

7. **Who greets a member without Zardoz Introduced is contradicted.**
   - s03-dinner-with-zardoz/ev-01:382 says such a member "keeps Krebbyg as their only contact and is greeted at those events by him alone", naming Officer and Commander.
   - r10:16 says "J.B. Nevercott receives them". r03:45-47 agrees with r10.
   - r25:25 has Krebbyg receive that member.
   - Fix: reword s03:382 so the Krebbyg-only line covers M5, M6 and Commander. Officer keeps the Nevercott fallback. Add "(or Nevercott, at Officer)" in r10:16 only if you prefer r10 to stay as written.

8. **M1 Handkerchief Delivered names a reader that does not read it.**
   - m01-the-handkerchief-and-the-girl/ev-01:362 says Coin Pouches "whose first pouch goes only to a member who marked it".
   - s01-coin-pouches/ev-01:18 gives the pouch to "the member who gave Nevercott's debrief", and s01:164 sets no outcomes.
   - M1's own debrief branches on prose, not on the outcome name.
   - Fix: change s01:18 to "belongs to the member who marked **Handkerchief Delivered** (highest Renown if several)". Alternatively cut the Coin Pouches clause from M1:362 and give the outcome a reader elsewhere.

9. **M1 Nimblewright Noticed has no valid reader.**
   - M1:364 says "read by Fireball!, where the party recognizes the construct without a check".
   - Fireball is a converted quest, and grep finds no "Nimblewright Noticed" anywhere under campaign/quests/act-ii/fireball.
   - Fix: reword M1:364 to say no converted quest reads it yet and log it (see out-of-scope item 1).

10. **s02 cites a Kreb Sorrush scene in M1 that does not exist.**
    - s02:50 (Thinking Back) says "recalls how Kreb Sorrush behaved in the booking office during The Handkerchief and the Girl".
    - s02:268 says "the same person the members met in The Handkerchief and the Girl".
    - s02 design-notes:5 says the same.
    - M1 has no Kreb appearance. He first appears in s01 (Dunstan trail) or in the Fireball! theater tickets.
    - Fix: change all three to "in Coin Pouches or at the Seven Masks lobby". Alternatively add a Kreb Sorrush beat to M1.

11. **s02:17 contradicts M5, M6 and s03 on who briefs.**
    - s02:17 says Krebbyg "does not brief The Wazoo Affair, Three Nights or anything after it".
    - M5 ev-01:34-37 and M6 ev-01:81-83 are briefed by Krebbyg (with Zardoz present if Introduced).
    - Fix: reword s02:17 to "He does not brief The Wazoo Affair, Three Nights or The Compromised Eye. After Dinner with Zardoz he briefs The Theater's Back Room and The Dive."

12. **M4 trail timing does not add up.**
    - m04-the-compromised-eye/ev-01:116 has the party at the grate at 11:30.
    - ev-01:163 says the foot of the stair is "about 11:45", the trail is "ninety minutes", and X1 is reached at 13:00. Arannis at :145 also says "an hour and a half".
    - 11:45 plus 90 minutes is 13:15.
    - Fix: change :116 to 11:15 and :163 to "about 11:30". The 13:00 watch change and the map time at :110 then hold.

13. **The Faire pier location contradicts.**
    - M4 ev-02-twelve-minutes.md:186 says Fel'rekt takes Nar'l to "the Mistshore pier" and the Heartbreaker.
    - 00-first-meeting/ev-01:416 and s04/ev-01:74 say the Dock Ward pier. M6 ev-01:17 and :151 say the old Faire pier at Smugglers' Dock.
    - Fix: change M4:186 to "the Faire's pier in the Dock Ward".

14. **Soluun's stat block differs between BD events and Doom Raiders.**
    - s05-the-killers-fate/ev-01:418 uses the 2024 Scout for Soluun, Fel'rekt and Krebbyg. This matches doom-raiders/m01-the-dockside-killer/overview.md:60 (Scout).
    - M6 ev-01:227 has Soluun fight as the "WDH Drow Gunslinger (CR 4)".
    - r25:225-231, :266 and r50:331 use the Drow Gunslinger for Krebbyg and Fel'rekt.
    - Fix: change M6:227 to "the Scout with the changes in The Dockside Killer". Pick one block for Krebbyg and Fel'rekt across s05, r25 and r50.

MINOR

- **Outcome claims and unlisted outcomes.**
  - **Bregan D'aerthe Joined** (FM:458) says M1 and every later BD event read it, but none names it. The only real readers are the Factions Guide page and Faction Outposts (unconverted).
  - **Scent Code Read** (M1:363) is read only by M1's own debrief prose.
  - **Fence Settled / Fence Gone / Fence Untouched** are set at M4 ev-02:101 and are not in the Event Outcomes block (:402-409). Gone and Untouched are never read by name.
  - **Nar'l Cleared** (M4 ev-02:406) omits The Dive as a reader, but M6 ev-01:24 and overview:26 read it.
  - **Black Viper Source Noted** (M2 ev:363) names the Gauntlet mission as "unconverted". See out-of-scope item 5.
  - r50:23 silently marks **Zardoz Introduced**, which is not in r50's Event Outcomes (:465-469).
  - s01 has no Mission Renown block.
  - s05:516 marks **Soluun Expelled** "for the party", while membership is otherwise individual.
- **Reduced base Renown.** M1:344 (1 base on failure) and M3:397 (1 base on Ott Lost) depart from the 2/2/3/3/4/4 table. If M1 fails, nothing supplies the Renown needed for the next gate. M2:83 says "Three Nights is still gated at Renown 5" with no source of that Renown.
- **Renown 25 and 50 statements.** r50:19 and :453 say missions award "19 at most... with no bonuses", and M6 ev-02:239 says awards "alone do not reach either rank". With the +1 bonus lines, missions can reach about 37. r25:18 says "base awards", which is correct.
- **Rank loss rules differ.** r03:39 keeps the Soldier rank below Renown 3. r10:291, r25:326 and r50:455 suspend benefits below threshold.
- **Nevercott's descriptor varies.** "Human in appearance" at FM:230, :339 and r10:62. "Drow in a hat of disguise" at M1:61, r03:79, s05:112 and :470. "Drow in the guise of a Human haberdasher" at M2 ev:48.
- **s02 miscounts jobs.** s02:17 and :97 say "two jobs and the Wazoo case" or "two jobs and a newspaper". M1 and M2 are the only two.
- **s02 anachronism.** s02:251 mentions "the safe house in the dressing room" before M5 opens it.
- **s05:231 vs M6.** s05:231 says the captain "won't be moving her this month". M6 ev-01:17 and overview:21 have the Marpenoth leave the keel collar on Tarsakh 20.
- **M6 brief inconsistencies.** M6 ev-01:41 admits "anyone the member will vouch for" at the knock, but :13 says only members receive the brief. Fel'rekt says "Kreb is already there" at ev-01:47, but the brief is at the theater.
- **r50 contradicts itself on Pelsha and Vorn.** r50:29 says they "do not speak", but Pelsha speaks at :262 and :310-314.
- **r50 and r25 pool mismatch.** r50:325 says the Commander Roster is "the same pool", but r25:220-225 has two crews (Crew Two is Ilmra Kelnozz and Brythe Mizzrym, who are absent from r50). r50:310 puts only Ilphrin in the muster, though r10 assigns a Spy per Officer.
- **Marpenoth location in r50.** r50:55-63 puts the saved Marpenoth under a hulk. M6 puts her under the outer end of the old Faire pier at Smugglers' Dock.
- **Closure scope for BD Contact Severed.** s04:20 says closed "for the rest of Acts I through III". FM:459 says "for the campaign".
- **Wine merchant tenure.** M5 design-notes:5 says the merchant has been on BD's books for "two years". FM:315 and s02:145 say the company has been in Waterdeep "months", and s05:207 says "a year".
- **Duplicate first name.** Tamsin Orr (r03) and Tamsin Rooke (M6) share a first name.
- **GM text names Manshoon.** M4 overview:25, r10:283, r50:27 and r50:281 say "never names Manshoon". Check this against the Doom Raiders convention.
- **Stale design-notes cross-references.** These describe problems that the rewrite already fixed:
  - m01 design-notes:27 (Coin Pouches knot check).
  - m02 design-notes:38-39 (M5 windmill in the North Ward; s02/s04 read the Pitch; "The Wazoo Affair is complete").
  - s01 design-notes:24 (halfling Ott).
  - s02 design-notes:33-35.
  - m03 design-notes:37 (First Meeting says no note).
  - s03 design-notes:29.
  - r03 design-notes:33.
  - r10 design-notes:29.
  - r25 design-notes:35.
- **Verified consistent against Notable Figures.**
  - Vessin is about eleven and invented.
  - Ott is a dwarf, Neutral Evil, Cultist Fanatic.
  - Nar'l's tenure is "a year" in M4 and s05.
  - Gaxly is Illuskan, forty, Neutral.
  - The coin pouches are 50 gp after M1 and 100 gp plus a note after M3, both in s01.
  - Fel'rekt is Neutral Good, Krebbyg is Chaotic Neutral, Soluun is Neutral Evil. Pronouns agree.

OUT-OF-SCOPE LOG (contradictions with files outside the BD folder)

1. campaign/quests/act-ii/fireball has no reader for **Nimblewright Noticed**. The writer is Trollskull ev-07:84, in True/False format. Trollskull ev-07:57 also says "Vessin is positioned along the parade route", but M1 keeps her at her crate at Net and Dock.
2. **Jarlaxle Unmasked** has no writer anywhere. Fireball ev-04 uses True/False headings (:116-123) and does not mark it. Arc-h is unconverted.
3. campaign/quests/act-i/trollskull-alley/ev-04 (:45, :118-122) says a Watch report ends contact "permanently" and party-wide. FM and s04 make it per character and have Nevercott still call on Ches 13.
4. Notable Figures:
   - Ryvarra (03-... 09-ryvarra.md:14, :22) says "weekly" reports. FM:28 says every tenday.
   - Soluun (02-soluun-xibrindas.md:22, :26) says the disownment is a cover story with forged BD ID. s05 makes it real.
   - Soluun, Fel'rekt and Krebbyg list the Drow Gunslinger, while DR M1 and s05 use the Scout.
   - Nar'l (03-narl-xibrindas.md:8, :22) says "three years", lists The Wazoo Affair and The Betrayal Pitch, and Krebbyg's page :8 lists The Betrayal Pitch.
   - Ott lists "Cult Fanatic".
   - Jarlaxle's page (01-jarlaxle-baenre.md:6, :8) lists "Swashbuckler" and The Betrayal Pitch.
5. campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation:
   - design-notes.md:7 calls BD-M2 the "hidden-gold exposé". BD M2 is a devil-worship fishing exposé.
   - Gaxly is "unaligned" at ev-01:48. BD M2 has Neutral.
   - That mission does not read **Black Viper Source Noted**, but BD M2 ev:363 names it as the reader and calls it "unconverted".
6. campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01:456-458 tells Sea Maidens Faire that a Captured Soluun is "back aboard" and an Escaped Soluun "returns". That predates s05, which expels him.
7. campaign/guides/factions/08-bregan-daerthe.md:
   - :16 offers a Renown 5 Marpenoth extraction after Mission 4.
   - :71 has the Marpenoth "moored under the Eyecatcher".
   - :67 describes the exposé differently.
   - The guide rows still say "the party" where the events are individual.
8. campaign/structure/arc-h-sea-maidens-faire.md puts the ships at a Mistshore pier and a drow mage at the Eyecatcher's helm. arc-j-vault-of-dragons.md:55, :75 and :322 are not wired to Marpenoth Saved/Crippled/Lost or Guild Survivor Escaped, and call the windmill a "Manshoon outpost". SOURCE_GUIDE.md (~:219) puts the windmill in the North Ward. arc-e still has the Ott gnome entry. All three come from BD design-notes and were not re-verified.

SUMMARY: 14 blocking, about 20 minor, 8 out-of-scope contradictions.