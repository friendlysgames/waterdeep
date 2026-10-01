# Doom Raiders consistency pass (Session 39)

Doom Raiders consistency QA, Session 39. I read all 36 files in the folder, the brief, the mechanics reference and the out-of-scope log. For cross-faction checks I read BD s05 in full and grepped the other BD events, OotG M2 and M3, EE M3, Gralhund ev-09 and the NF pages. Nothing was edited. All paths below are under `/home/user/waterdeep/campaign/quests/faction-events/doom-raiders/` unless they start with another prefix.

# BLOCKING ISSUES (DR-internal first)

**1. Skeemo's tenure is "years" in six places and "two months" in four.**
- Files and lines saying "years":
  - `r10-viper/ev-01-viper.md:68`
  - `r25-ardragon/ev-01-ardragon.md:68` and `:184`
  - `r50-dread-lord/ev-01-dread-lord.md:48`
  - `m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:16`, `:209` and `:215`
- Files and lines saying "two months":
  - `m04-silencing-skeemo/ev-01-the-approach.md:16` and `:32`
  - `m04-silencing-skeemo/ev-03-the-reckoning.md:17`
  - `s02-davils-return/ev-01-davils-return.md:202`: "Two months and eleven days, sir. Before that I wrote to House Gralhund."
  - `m04-silencing-skeemo/overview.md:21`
- Fix: change each "for years" to "for two months, and House Gralhund before that".
  - r10:68 should read "He sold us to the other cell for two months".
  - r25:68 should read "He sold us for months".
  - r25:184 should read "told the other cell everything for two months".
  - r50:48 should read "He sold us for months".
  - M6:16 should read "which Skeemo fed it for two months".
  - M6:209 should read "for two months before he ever came to the tower".
  - M6:215 should read "that the alchemist kept for us for two months".

**2. DR M1 Event Outcomes still send Soluun back aboard.**
- `m01-the-dockside-killer/ev-01-the-dockside-killer.md:456` says a Captured Soluun is "back aboard the Scarlet Marpenoth after his release".
- `:457` says an Escaped Soluun "returns weeks later... recognizes the party on sight". BD s05 expels him in both cases.
  - Captured: the twelfth night, the night he is released (s05:30).
  - Escaped: the twenty-fourth night, or Tarsakh 18 if that comes first (s05:31).
- Fix, :456: replace "where he is back aboard the Scarlet Marpenoth after his release" with "**The Killer's Fate** (Bregan D'aerthe), which holds the ruling the night he is released and marks **Soluun Expelled**, and by **Sea Maidens Faire**, where he is not aboard, having been expelled".
- Fix, :457: replace "where he returns weeks later and before Tarsakh 20, recognizes the party on sight" with "**The Killer's Fate**, which holds the ruling the night he walks back aboard (the twenty-fourth night, or Tarsakh 18 if that comes first), and by **Sea Maidens Faire**, where he is not aboard".
- Also add the missing readers to :456–459.
  - BD **The Compromised Eye**, **The Dive** and **Houseless Noble** read **Soluun Killed**.
  - **The Killer's Fate** reads Captured, Escaped and Killed.
- This is already logged in the BD section, but the DR file itself is still wrong.

**3. M1 contradicts itself about the disc.**
- :281 says the disc "is the company's mark".
- :371 says a BD member "sees at once... The disc is forged, and someone made it for him or he made it himself".
- s05:18 and :208 make it the company's own deliberate forgery.
- Fix :371: "The disc is a forgery, though a good one, and a Bregan D'aerthe member can tell it was struck outside the company's usual shop."
- Fix :281: "the spider-and-blade disc at his neck passes for the company's mark."

**4. M3 fight roster breaks the mechanics reference and uses 2014 attack names.**
- `m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:373` fixes three Wererats ("Do not add Wererats beyond these three"). `m03.../overview.md:10` and `:71` repeat this.
- The reference says three Wererats are Crushing at 3 PCs (148%) and Oppressive at 4 PCs (83%). It recommends:
  - 3 PCs: Wererat plus 2 Giant Rats.
  - 4 PCs: 2 Wererats.
  - 5 PCs: 2 Wererats plus a Tough.
- M3:379 says the Shunners fight "with the Scimitar and the Hand Crossbow". The 2024 Wererat has Scratch and Hand Crossbow.
- Fix :373: Kelso always uses the Wererat block. Dasher stays out of the fight (:376 already has him step back).
  - 3 PCs: Kelso plus 2 Giant Rats from the fruit cart.
  - 4 PCs: Kelso and Brynn Hilltopple.
  - 5 PCs: Kelso, Brynn and one Tough.
- Fix :379: replace "Scimitar" with "Scratch".

**5. M6 Ziraj's fixed shot kills the Spy it says survives.**
- `m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:133`: Round 1 "hits the rooftop crossbowman for 32 damage, and she spends her next turn shooting at Ziraj".
- The 2024 Spy has 27 HP (reference §4).
- Fix: change 32 to 14 in :133. Round 2's second hit (:134) then drops her to 0 and she falls.

**6. A member who first meets Tashlyn in M3 or M4 can never get Tashlyn Contact, and so misses Davil's Return.**
- `s02-davils-return/ev-01-davils-return.md:17` sends the dusk snake only to members who "marked Tashlyn Contact".
- `m03.../ev-01-the-missing-snobeedle.md:22` and `m04.../ev-01-the-approach.md:26` introduce Tashlyn to unmarked members but never mark the outcome.
- s01:276 makes Tashlyn Contact the gate for Xanathar's Lair Scene 1 briefings.
- `r03-wolf/ev-01-wolf.md:20` says "mark it at this meeting" even when Davil receives the member. r03:245 says "mark... if Tashlyn delivered".
- Fix:
  - Add to M3:22 and M4 ev-01:26: "Mark **Tashlyn Contact** for any member who meets her here."
  - Change r03:20 to "If Tashlyn is the one receiving the member and **Tashlyn Contact** is not yet marked, mark it."

**7. Wolf names Vevette Blackwater and Agorn Fuoco to a Renown 3 member, before M4 and M5 reveal them.**
- `r03-wolf/ev-01-wolf.md:126` gives the cell's team order "Vevette Blackwater... then Agorn Fuoco... then Urstul Floxin". :142 says each answer "names the leader and crew of whichever team comes next".
- M4 ev-03:150, Tashlyn: "Vevette Blackwater. Good. Now I have a name to go with the hand."
- M5 ev-01:80, Tashlyn: "I've heard one name for that officer already."
- m04 overview:58 says Vevette is "named only when Tashlyn decodes" the letters.
- r03:126 also says the third team exists only "if Floxin survived". A Captured Floxin did survive, but he cannot lead a crew.
- Fix:
  - Until **Skeemo Letters Recovered** or **Vevette Letters Recovered** is marked, the web describes the cell's teams by size and trademark without names.
  - Change :126 "if Floxin survived" to "if **Floxin Status** is Alive".

**8. The Yellowspire knowledge chain is inconsistent across M4, s02 and M5.**
- M4 ev-02:155: the Doom Raiders "do not know what lies behind the door".
- M4 ev-01:53: Tashlyn's only intel is a watcher on the shop.
- s02:29: Davil already places the cell in "the towers in the Trades Ward where they keep their people".
- M5 ev-01:48, :86, :92 and Debrief:43: Tashlyn "has watched that place for two months", has heard the knock "a hundred times", and knows the circle.
- Fix: in M4 ev-01:53 add "My watcher has followed his birds to a tower in the Castle Ward for two months and never seen who answers the door." Rewrite M4 ev-02:155 to "They know the tower, because Tashlyn has logged it, but not what lies behind its door."

**9. M3's reward timing breaks the debrief.**
- `m03.../ev-01...md:359`: if the party gives up Dasher's location, Blossom "sends the reward to Trollskull Manor by courier two days later".
- :435 and :443–449 have Tashlyn take "five hundred" the day after the party settles the matter.
- Fix: change :435 to "the day after the party settles the matter, or, if the party gave up Dasher's location, the day after Blossom's courier arrives".

**10. Davil's release date is never fixed, but a captured Skeemo needs three days in the tack room.**
- s01:16 says the hearing is "well after the party has finished Silencing Skeemo".
- s01:196, s02:15 and M4 ev-03:200 say "the first hearing day after the debrief".
- s02:166 and M4 ev-03:196 say Tashlyn keeps a captured Skeemo "three days".
- s01's design notes claim the chain is fixed, but only up to Ches 28.
- Fix: state one interval in all five places, for example "the fifth day after the debrief".

# MINOR ISSUES

- **Outcome readers missing or incomplete:**
  - **Wolf Reached** (r03:244) and **Viper Reached** (r10:211) have no reader and are not in the out-of-scope log.
  - M4 ev-02:163 omits M6, r25 and r50 as readers of **Skeemo at Kolat Towers**.
  - s02:300–302 omits r25 and r50 as readers of the Skeemo fate outcomes.
  - s02:299 omits Ardragon (r25:15) as a reader of **Davil Released**.
  - M5 ev-01:419 omits M6:24 as a reader of **Yellowspire Circle Destroyed**.
  - **Seven Masks Lead** has no BD reader. The M1 design notes (:7) say BD relies on it, but BD M5 reads only **Seven Masks Raided**.
- **M2 refusal outcome:** the coach-grab branch (M2 ev-01:268) makes Esvele hostile in Cassalanter Villa. It marks the same **Delivery Refused** as a plain refusal, whose reader line (:362) names only Silencing Skeemo.
- **M1/M2 after the arrest:** nothing says what happens to M1 or M2 if they are unplayed when Davil is taken on Ches 26. Both are briefed by Davil, and M3 needs M2 done.
- **r10 bench timing:**
  - r10:5 says Viper usually lands around the end of M4. Bonus Renown can reach 10 before M4; the maximum before M4 is 16.
  - r10:185 lists Loria Finch as the alchemist unconditionally, but :22 says she takes the seat only after M4.
  - Fix: before M4 the seat is Skeemo's.
- **Tashlyn's handwriting:** "sharp, upright" at `00-first-meeting/ev-01-first-meeting.md:372`, but "small and square" at s01:39 and :43, s02:21 and r25:109.
- **Quotation marks:** speech has no quotation marks in s02, r03, r10 and M6, for example s02:58 and :96, r03:34, r10:32 and M6:38 and :293. M5, s01, r25 and r50 quote their speech.
- **Format glitches:**
  - M5 ev-01:265 has a stray ">".
  - s02:57 has a stray ">" line.
  - s02:294–295 is missing a blank line before the Event Outcomes block.
  - r50:36 heads the second-floor room "The Third Floor".
- **Ward naming:** "Southern Ward" in M3, but "South Ward" in r10:15 and r50:183.
- **Kolat Towers in player-facing text:** M5 Overview and Summary (ev-01:427 and :431; Debrief:225 and :229) name "Kolat Towers". M5 ev-01:27 has the Doom Raiders call it the cell's stronghold before **Manshoon Named**. Davil's Brief (M5:56) and s02:29 say only "the towers in the Trades Ward". Pick one convention.
- **M5 pay asymmetry:** The Debrief pays 100 gp, plus 50 gp for the ledger (Debrief:117). The heist version pays no gold.
- **M5 Debrief:133:** Yagra says "five of them and one fucking priest". Amath plus four acolytes is five in total.
- **M5 ev-01:23:** "even if **Skeemo at Kolat Towers** changed the knock" cannot combine with **Skeemo Captured**. They are mutually exclusive.
- **M6 vs M5:** M6:193 says "a week of notes" against M5's "Twenty nights". M6:16 and :62 say Ziraj watched amulet handoffs, but his M5 notes record force-field gaps.
- **Yagra's stats:** M6:44 uses a plain Warrior Veteran. r10:128 gives her gauntlets and Relentless Endurance.
- **Name reuse:** Tolliver Greenbottle (M3) and Wren Tolliver (r25:190).
- **M1 stat swap:** M1 swaps the Scout's longbow for a hand crossbow (:248). The reference (§1) says keep the longbow. The design notes explain the swap, but it still departs from the reference.

# OUT-OF-FOLDER CONTRADICTIONS NOT ALREADY LOGGED

1. **Gralhund ev-09 Istrid branches vs DR.**
   - `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:71–79`: Istrid is terrified and plans to relocate to Baldur's Gate. Help her and she "vanishes south". Turn her in and "City Watch takes her".
   - DR M3, M5 Debrief, r03 and r50 use her at her Dock Ward warehouse. Only the unrelated True/False flag issue is logged.
2. **First-name collisions with BD:**
   - Sergeant Ilmra Dunfell (DR s01) and Ilmra Kelnozz (BD r50:329).
   - Odalys Quenn (DR r10) and Odalys Vane (BD r03:185).
   - Ilsa Carrow (DR r25) and Captain Ilsa Dalloway (BD M5).
3. **Wererat silver rule in OotG M3:**
   - `order-of-the-gauntlet/m03-the-shard-shunners/overview.md:22`, `ev-01...md:16` and `:149` say "Silver or magic weapons required".
   - The 2024 Wererat has no such rule (the reference says it is gone), and DR M3 follows 2024. The OotG DC 17 Intimidation dispersal also differs from DR's DC 15 Persuasion.
4. **Senna Vael:**
   - `setting/notable-figures/doom-raiders/07-senna-vael.md` has Davil confirm her when the party joins. She also appears in org page 06 and `guides/trollskull-manor/03-staff-and-hiring.md`.
   - No DR event uses her, and the First Meeting does not disclose her.
5. **Log correction:** `docs/plans/harpers-out-of-scope-notes.md:288` says s01 gives the Davil-assist Renown "once per member per completed approach". The event gives 1 Renown once per member in total (s01:233, :255).
6. **BD side of Seven Masks Lead:** no BD event reads **Seven Masks Lead**. DR M1's design notes imply BD does.

# CHECKED AND CLEAN

- **Gates:** Join/L2, R3/L3, R5/L4, R8/L5, R10/L6 and R13/L7 are consistent across Next Steps, overviews and rank events.
- **Base Renown and Milestones:** base Renown is 2/2/3/3/4/4 and rank gates are 3/10/25/50. Every event ends "awards no Milestone Points".
- **Reachability:** the gates are reachable from Renown 1. The six missions total 19.
- **Manshoon in speech:** Manshoon is named only in GM blocks or behind **Manshoon Named**.
- **Floxin Status:** branches are present in s01, M4, s02, M5, M6, r03, r25 and r50.
- **Cassalanter secrecy:** no DR speaker alludes to infernalism.
- **Lolth:** appears only with contempt (M1:343, :363).
- **Stat names:** all 2024, apart from the M3 "Scimitar" above.
- **Retired blocks:** none in the folder.
- **Membership:** briefs, debriefs, ranks and benefits are per member.
- **Calendar:** Ches 24, 26, 27 and 28 hold in s01. M1 matches s05 (surety on the twelfth day; Escaped before Tarsakh 20).
- **BD agreement:**
  - The M1 BD-members sidebar (:277–285) matches s05: Nevercott's "You were there.", −1 Renown, DC 13, the early-warning rule and the **Soluun Expelled** follow-up.
  - Soluun is the Scout everywhere.
  - Seven Masks and Rongquan Mystere are consistent with BD M4, M5 and NF 07.
  - Gaxly is retired from DR M2 and no Vessin appears in DR.
- **NPC alignments, species, pronouns and locations** match the NF pages.

**Verdict:** Not ready to merge: 10 blocking fixes remain, all inside the DR folder; Manshoon gating, Floxin branches, Cassalanter secrecy, gates and renown are sound.