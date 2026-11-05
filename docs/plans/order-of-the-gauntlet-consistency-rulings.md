# Order of the Gauntlet Consistency Rulings (Session 45)

Source: the consistency-checker's pass over all 13 rewritten folders. Items are numbered as in its report. Paths are relative to `campaign/quests/faction-events/order-of-the-gauntlet/` unless a full path is given. This page is binding for the fix agents.

## Blockers

| # | Ruling |
|---|---|
| 1 | **Quietly Reassigned in M1, M2, M3.** Each mission's Brief gets a "When the Brief Comes by Note" block copied from `m04.../ev-01-twelvedog-court.md` (lines near :67-77): Brother Hallin Ostrel's note signed "B.H.O.", carried by a Priest Acolyte; Savra does not come to the door; the debrief moves to the Halls of Justice east annex. Add Quietly Reassigned to the Event Outcomes "read by" line and Summary bullets. |
| 2 | **Temple count.** The Halls of Justice is the temple of Tyr. There are three temples (Halls of Justice, Temple of Helm in the Castle Ward, Chapel of the Steadfast Shield). Fix `00-first-meeting/ev-01-first-meeting.md` :192 and :206 to "three temples" and "up to three castings". |
| 3 | **M2 return day.** Savra returns at dusk on Day 3. Fix `m02.../ev-01:85` and :34 to match ev-02:32 and overview:17. |
| 4 | **Duplicate Joined writer.** Trollskull ev-04 is fixed by the companion drafter (a15b480790323ace4). |

## Should-fix inside the folder

| # | Ruling |
|---|---|
| 5 | **M2 Night 1.** The raven roosts on Night 1 regardless of the watcher state; the Calm/Wary/Hunting state sets Night 2 and Day 3 dawn only. |
| 6 | **Kelso's Debt.** Keep three uses only (Location, Distraction, Silence). Recast Pim's key (`m04.../ev-02:176`) as a Location use: Kelso names the lodger and the landlady's hours. |
| 7 | **Lycanthropy cure.** Cut the free cure at `m03.../ev-01:346` and the "Marcheon ruling" claim in `m03.../design-notes:23`. A cursed member is the Halls' business at the usual price; state no rule. |
| 8 | **Detect Evil and Good in M2.** `m02.../ev-02:70` becomes a 25 gp donation to a Halls priest or a party cleric's own casting. Temple spellcasting stays an r10 benefit. |
| 9 | **Gysheer's room.** Overview :27 says the room holds the day-book and the receipt copies, so the address survives; the sealed V.C. note is not duplicated. |
| 10 | **Quietly Reassigned note carrier.** Everywhere: Hallin's note, carried by a Priest Acolyte. Fix `m05.../overview:5` and `ev-01:41`. |
| 11 | **M5 dates.** The lease is six years old (ev-01 :21 and :117). Ledger entry six stays in 1488 DR. Entry eleven reads "Days ago". Orros says the dray came "a tenday ago". |
| 12 | **Spans.** M3 and M2 use days or tendays, never weeks: Trevar's dismissal is "fifty days" everywhere; fix the M3 lines listed in the report and `m02 ev-01:148` ("this week" becomes "this tenday"). |
| 13 | **Ward spelling.** "Trades Ward" everywhere in M1 (`m01` overview:27 and ev-01 :23, :198, :216, :220, :222, :277). |
| 14 | `m04.../ev-02:128` reads "You aren't knights of the Order, so ..." |
| 15 | Drop "Righteous Hand" from the readers of Cult Funding Linked (`s02 ev-01:263`). |
| 16 | Delete the Bregan D'aerthe reader clause for Joined at `00 ev-01:336`. |

## Companion gaps (items 17-26)

| # | Ruling |
|---|---|
| 17-22 | Factions Guide 05, rank rows, organization page, Savra and Valdra Notable Figures, Trollskull ev-04 and the manor guide are being rewritten by agents a11a460c65cde4351 and a15b480790323ace4. Items 17-22 are their checklist. |
| 23-26 | A third companion agent fixes the structure docs (arc-e :249 and :87, arc-g :41, arc-i :39, arc-j :49), the Cassalanters Factions Guide (`campaign/guides/factions/11-cassalanters.md` :25, :27, :43, :79), the Bregan D'aerthe Wazoo Affair lines (ev-01 :27 and :386, design-notes :19), `campaign/setting/waterdeep-lore.md:36`, Saeth's page (`city-officials/03-saeth-cromley.md`: Halls of Justice, Featured-in with Savra's Past), the Seffia page (`cassalanters/10-seffia-naelryke.md`: Cultist Fanatic, drop M2 listing) and Kelso's page (`independents-adversaries/03-kelso-fiddlewick.md`: Featured-in, Danika is a fourteen-year-old victim, not in the gang). The summoning circle: the shrine's Area 1 keeps it; M5's cellar holds only the rite goods. |

## Log-only items

| # | Ruling |
|---|---|
| 27 | Add the missing readers to the writer files' outcome lines (r25 reads Splinter Intel Reported, Forged Record Secured, Intelligence Shared, Order Recognized; r10 reads Cassalanter Register Filed). |
| 28 | No change. |
| 29 | s01 :214 "the list below is complete" becomes "the baseline list"; other files add effects. |
| 30 | M3 :168: Pell's list lead is free if Pell's Debt Held is marked, otherwise 100 gp. |
| 31 | Add one line to r03 :100: faction missions are not Marcheon operations. |
| 32 | M5 :282 and :290: Savra reads the last ledger line as "a bare date" and does not say Founders' Day; the players connect it. |
| 33 | r25 :106 predicate: "the ledger, handed over to Savra". |
| 34 | M6 :24 and :64: Savra says nothing of the family's worship or bargain unless the party told her; her debrief lines at :334 and :340 stay but are keyed to what the party told her or found in the villa. |
| 35 | Faction labels: Father Corwen Thale, Sister Merrin Oakhollow and Sister Ilvane Haste are labelled "(Temple of Tyr)" everywhere. |
| 36 | M6 ev-01:156: Father Corwen is he/him; fix "her action". |
| 37 | Log only: a party that took nothing from the cellar gets no Siamorphe symbol from M5; r10 is the fallback. |
| 38 | Rename Pim to Pip in `m04.../ev-02` (Constable Pimm in BD s02). |
| 39 | No change. |
| 40 | M4 Next Steps wording: "This faction mission awards no Milestone Points" in ev-01 :201; ev-02 :283 says the note goes to the manor and the Brief is given at the Halls. |
| 41 | First Meeting :24: "around the time the Watch released two of its members". |

## Dispatch

| Agent | Files | Items |
|---|---|---|
| A | m01, m02, m03 (overviews, events, design notes) | 1, 3, 5, 7, 8, 12, 13, 30 |
| B | 00-first-meeting, m04, m05 | 2, 6, 9, 10, 11, 14, 16, 32, 37, 38, 40, 41 |
| C | m06, s01, s02, r03, r25 | 15, 27, 29, 31, 33, 34, 35, 36 |
| Companion 1 and 2 | Factions Guide 05, org page 04, Notable Figures, guides, Trollskull | 4, 17-22 (running) |
| Companion 3 | structure docs and other pages | 23-26 |
