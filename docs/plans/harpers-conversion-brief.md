# Harper Conversion Brief (Session 41)

## Context

The user rejected the Session 35/37 Harper events because of their wording and internal structure. They said "I just like the way we did BD and DR better", and on the mission mini-arc, "see how bd and dr do it".

**Rewrite input**
- Every Harper file is restored to the commit that first added it (`d9c9e96`).
- The six design-notes files that first appeared in the Session 35 upload were removed and must be recreated.

**Previous version (fact source only)**
- Commit `7215515`. This session's copy is in the scratchpad at `harpers-prev/`.
- Its settled facts survive. Its structure and prose do not.

**Research reports** are in `docs/plans/harpers-research/`:

| File | Covers |
|---|---|
| `01-spec-and-structure.md` | BD/DR page model, how prev departed from it, binding rules, templates |
| `02-first-meeting-s01-ranks.md` | 00, s01, r03, r10, r25, r50 |
| `03-m01-m03.md` | M1–M3 |
| `04-m04-m06.md` | M4–M6 |
| `05-consistency-audit.md` | Outcome map, inbound references, standing-rule hits, open items |

Where a report lists options, this brief has already chosen. Where a report and this brief disagree, this brief wins.

## What went wrong with the previous pages (avoid all of it)

- GM truths sat in the overview's Background instead of a `Who Knows What` / `What Is Actually True` block at the top of the event.
- Events set too many outcomes. M2 set twelve, six of them ledger-state variants.
- Clock micro-procedures padded the scenes: the opera timetable, the tailor clock, round-by-round stock timers, ledger collection and burn deadlines.
- Filler qna (wine, supper, libretto, architecture), plus qna answers that ran two or three paragraphs.
- Brief scenes with no `[!social]` or `[!qna]`.
- Rank events thin next to DR/BD.
- A "Harpers Mechanics Reference" was cited but never existed.
- Prose written to the old minimum lengths, with no ceiling.

## User decisions (Session 41)

1. **Page model = BD/DR.** Copy the DR model pages' skeletons exactly (see the drafter instructions). The mini-arc maps as follows. There are no "Act" labels.

   | Mini-arc | Event page |
   |---|---|
   | Hook | `### The Brief` |
   | Background | `Who Knows What` / `What Is Actually True` block before the first `###` |
   | Acts | named `###` scenes |
   | Renown | debrief readalouds and the `Mission Renown` block inside `### Renown Opportunities` |
   | Aftermath | `### Aftermath` |

2. **Keep settled facts:** outcome names that have readers, NPC renames, House Ulbrinter on Delzorin Street (North Ward), Maxeene speaking Common, gates and renown.
3. **M6 stays at 7th level, after Kolat Towers.**
   - Mirt wants three days with the fully awakened Stone before the Vault opens.
   - The raid comes from Splinter survivors and branches on what Kolat Towers left of Manshoon.
   - No escape "to Kolat", no Kolat Towers reader, no "at least one Eye" gate.
4. **Nihiloor's devourer is a custom "occupying" variant** that keeps the host's brain alive.
   - Corene (M5) can be saved by forcing it out, using the procedure in `docs/plans/harpers-mechanics-reference.md`.
   - The same rule is applied to Force Grey M3 and M5 in a separate edit.
5. **Jarlaxle.** "M4 happens by definition after Fireball."
   - Fireball ev-04 (the Sea Maidens Faire) becomes the writer of **Jarlaxle Unmasked** for each character present.
   - Harper M4 reads it:
     - **Marked:** the job is seeing the man they met as Zardoz Zord through a second disguise.
     - **Unmarked** (ev-04 skipped): a correct identification at the salon marks **Jarlaxle Unmasked** for each character present.
   - Cut the "+1 Bregan D'aerthe Renown" award inside a Harper mission.

## Standing defaults

**Rules**
- **Manshoon (R1).** Use the DR gate on **Manshoon Named**, written by the Faction Outposts Interrogation House (unconverted).
  - Until it is marked, Harper speakers know only that "the Black Network has split". They say "the Splinter", "the other cell" or "whoever's paying". Harpers have no Floxin belief.
  - Kolat Towers as his home is gated too.
  - GM text may state the truth.
  - Remove "Manshoon" from every player-facing line, the overview `## Overview` sections and `Involved Characters` labels. Write "the Splinter" there.
- **Cassalanters (R2).** Suspicion only. Nobody knows of the pact. Guest leads (dye, rubies, windfalls) stay commercial suspicion. The PDF 3 claim that the Harpers know is overridden.
- **Membership (R3).**
  - Recruitment, briefs, debriefs, renown and ranks belong to individual Harper members.
  - Companions can help with everything else and earn no renown. The M3 and M4 gold goes to every contributing character.
  - A character already in another faction gets no offer.
- **Gates.** First Meeting at 2nd level gives Renown 1 (Watcher). Then:

  | Mission | Gate |
  |---|---|
  | M1 | joining, 2nd level |
  | M2 | Renown 3, 3rd level |
  | M3 | Renown 5, 4th level |
  | M4 | Renown 8, 5th level |
  | M5 | Renown 10, 6th level |
  | M6 | Renown 13, 7th level |

  Phrase it: "becomes available when an individual Harper member reaches Renown N and Nth level".
- **Base renown.** 2 / 2 / 3 / 3 / 4 / 4, plus `+1 Renown:` bonuses for listed conditions only, each once.
  - Base totals 19 with the join.
  - Renown 25 and 50 come from the guide's Earning Renown list and from Mad Mage. The r25 and r50 design notes say so.
- **One writer per outcome.** Every outcome has a reader. That can be a Harper event, a named quest marked "(unconverted)", or a line in your report for the out-of-scope log. Aim for 2–6 outcomes per event.
- **Remallia "Remi" Haventree.**
  - Her public noble self may appear before M4 (Trollskull Alley, Fireball!). Her Harper role is hidden until M4.
  - Before M4, the Watcher safe house is kept by an unnamed intermediary. Nobody names her as a Harper.
  - **Remallia Harper Contact Known** is written once, in M4's last event.
  - r10, r25 and r50 read it to decide whether Remi appears in person or Mirt relays.
- **Mirt.**
  - Two gears (`character-voices`, `voices/harpers.md`): bawdy and swearing in public; short, plain and swear-free on business.
  - Says "lad" and "lass". Refills glasses.
  - Signatures: "Sit.", "I am almost never home."
- **Speech in readalouds is quoted.** Summaries are first-person plural.
- **Rules.** 2024 rules and names only. No Thug or bare Veteran. Use the mechanics reference for every roster.

**Places**
- Lightsinger Theater is in the Castle Ward.
- House Ulbrinter: Delzorin Street between Vhezoar Street and Brondar's Way, North Ward.
- Watcher lodging: 12 Delzorin Street, separate from the villa.
- No Harper rooms on Saerdoun Street, which is the Gralhund Villa address. Prev used it in s01 and M5; use **Brondar's Way** instead.
- Shield Street is Sea Ward (WDH). The Castle Ward barber contact moves to **Swords Street**.

**Name fixes (collisions)**

| Old name | New name | Collides with |
|---|---|---|
| Orren Vale (the mole) | **Tobin Harrask** | Orvyn Dall, Vale & Reed Imports |
| Dena Voss (r25 informant) | **Dena Holt** | Dalen Voss, Hanna Voss |
| Joss Bell (r25) | **Joss Marrin** | Oswin Bell |
| Harl Keen (courier) | **Wil Keen** | Harl Pimm |

All other prev invented names stay, and each folder's design notes list them under "Invented Names and Open Items". That includes Beldan Rusk, Tessalar Maeridge, Vell, Orvel, Edric Tanner, Kael, Syla, Nella Fen, Orin Dask, Bram Pell, Evin Talver, Perrin Valt, Mara Coppersail, Darron Quill, Della Morn, Oswin Bell, Ilen Castor, Ivara Dunn, Lysa Fenwick, Teren Moss and Dalen Voss. Hessa Dorn gets a new stable (see M1).

## Per-folder briefs

Line references are in the research reports. Each drafter reads its report section first.

### 00 First Meeting (+ design-notes). Report 02 §1–2, §6

- **Trigger and invitation**
  - Renaer recommends the party's unaffiliated characters. A paper bird carries one ticket per candidate to *The Fall of Tiamat*, an opera sung in Giant, with a printed Common libretto, at the Lightsinger Theater (Castle Ward), Private Box C, intermission.
  - The invitation text follows WDH and Appendix B: "Renaer tells us you are a good bet…", with formal attire.
  - A Delzorin Street tailor has been told to expect them. Cover this in one GM sentence, with no clock.
  - Companions can attend the public performance only.
- **Scenes**
  - Arrival at the box.
  - Mirt watches the first act, then explains the Harpers plainly at intermission.
  - Use the DR First Meeting shape: social, about 6–8 qna, no filler qna.
  - **Will not discuss:** the Stone, Manshoon, the Cassalanters, the vault, his offices ("He is assessing, not briefing").
  - **Checks:** DC 12 Intelligence (Investigation) on the invitation; DC 14 Wisdom (Insight) on Mirt.
- **Each candidate's answer**
  - The silver harp-in-crescent pin is already in his hand.
  - Decline: he refills his glass and leaves at the bell.
  - Either way he says "I am almost never home" and "You'll hear from us soon."
  - **No first mission at the pin.** The Talking Mare comes by its own brief at 2nd level.
- **Watcher Benefits block:** Renown 1; friendly Harpers; pin; mundane key and address card for 12 Delzorin Street (five bunks, water, hearth), kept by an intermediary.
- **Outcome:** **Harpers Joined**, marked for each character who accepts, with the name recorded. Read by the Harpers Factions Guide and **The Talking Mare**.
- **Summary:** "After the Meeting" and "Without a Private Meeting" variants.
- **Cut:** the opera timetable and scene-by-scene opera, the tailor clock, the missed-appointment recovery, and the wine, supper and architecture qna.

### M1 The Talking Mare (overview, ev-01, design-notes). Report 03 §1–3, §7 rows 1–6

- **The Brief:** Mirt, by paper bird or in a theater box (Appendix C :40). Social plus qna.
- **Finding Maxeene:** three independent routes, including Orvel (1 sp and an apple) and the stablehands (DC 12 Charisma (Persuasion)).
  - She is a grey roan draft horse with a **white blaze**, at a Dock Ward hire stand off Fillet Lane.
  - She speaks Common through a druid's permanent enchantment and has Intelligence 10.
- **Her act:** in public she plays a horse. DC 14 Wisdom (Insight) notices it. DC 11 Wisdom (Animal Handling) steers her somewhere quiet.
- **Trust**
  - The Harper pin or knowledge of the Delzorin safe house works. Otherwise DC 13 Charisma (Persuasion).
  - Advantage if treated as a professional. Disadvantage for "girl", patting her mane, or slow loud speech.
  - The apple rule stays.
- **Her intel**
  - The Shesstra Street building (Trades Ward, red lantern, three floors).
  - Two days ago, a sun elf and a half-orc woman with a winged-snake tattoo talked about hiring spies to find Xanathar hideouts. DC 12 Intelligence recognises them as Davil Starsong and Yagra Stonefist.
  - Keep the prev "war" line only if it fits in one sentence.
- **Complication: Vell** (Spy, the Splinter) in a hire-coach. Passive Perception 14 or DC 14 Wisdom (Perception) spots her.
  - Four handlings: confront, bargain, shadow her to Shesstra Street, or be tailed (DC 15 to spot).
  - Shesstra Street holds two resident Spies with surrender limits.
- **Relocation**
  - She asks to leave the Dock Ward.
  - Hessa Dorn's stable moves to **Brondar's Way, North Ward**. **Not Candle Lane**, which is the Zhentarim warehouse street.
  - If Vell goes unnoticed, Maxeene vanishes from her stand a tenday later.
- **Renown:** 2 base. +1 Maxeene's cover preserved. +1 Vell neutralised, or followed and the address reported.
- **Outcomes** (keep the names, at most 5):
  - **Maxeene Relocated**
  - **Maxeene Cover Preserved**
  - **Vell Neutralized**
  - **Shesstra Street Reported**: read by **Faction Outposts** (unconverted), s01 and r03.
  - Fold **Maxeene Identified** into Cover Preserved.

### M2 The Dead Drop (overview, ev-01, design-notes). Report 03 §1–3, §7 rows 13–16, 19, 24

- **The Brief:** paper bird, then tea at Felzoun's Folly (corner of Sorn and Salabar) with Uza Solizeph, a Mulan human Commoner of about seventy. She is precise, not dramatic.
  - Social plus qna. She hands over front and back keys. Her lockbox holds 15 gp and spare keys.
- **Sorn Street bookshop:** three floors, between a glassblower and a cartographer.
  - **The gazer** is a stray beholder-spawn hunting Fillipa the cat. It has **no handler and no Splinter link**; it was drawn by the cat.
  - Stock-loss rule: missed rays risk stock. Prev's three-tier fix is fine, but write it as one short bullet procedure, not a timer.
  - Fillipa is on a 12-foot ridge beam and comes down 30 seconds after the gazer dies.
- **The loose brick:** behind shelf seven, DC 12 Intelligence (Investigation).
  - The dead drop holds a hand-copied cipher naming two Harper assets in noble houses: Lysa Fenwick (Amcathra) and Teren Moss (Rosznar).
  - DC 14 Intelligence (Arcana) shows the copy was made by hand, not by scrying.
  - Mirt names the clerk who serviced the drop: **Tessalar Maeridge**.
- **Tessalar:** 23, a records clerk who took 50 gp from a handler (**Beldan Rusk**, GM-only name until the party learns it).
  - DC 13 Charisma (Intimidation or Persuasion) turns him.
  - Three resolutions: turn him, report him to the Watch, or warn Mirt and move the contacts.
  - Each resolution gets a short concrete result. No 24/48-hour clock tables.
- **The handler's ledger:** in the customs house, rejected-cargo desk, second drawer. Write one beat, not a state machine.
  - The ledger gives the Rusk channel plus "two more contacts at a Brindul Alley address".
  - **Do not name Avareen or Zorbog.**
- **Skeemo lead (source):** if asked about unusual purchases, Uza says Skeemo Weirdbottle bought three volumes on noble families' scandals last month. Optional flavour lead with no outcome.
- **Reward:** the spellbook (*Comprehend Languages*, *Detect Magic*, *Identify*, *Shield*; *Invisibility*, *Locate Object*, *Misty Step*), given whatever happens to Tessalar.
- **Renown:** 2 base. +1 Tessalar turned. +1 ledger read before Rusk collects it.
- **Outcomes** (at most 6):
  - **Fillipa Rescued** (read by r03's first question or cut; your choice, but it needs a reader).
  - **Harper Contacts Relocated**: single writer here. Read by **The Tail** (M3 ev-02).
  - **Tessalar Turned** / **Tessalar Arrested** / **Tessalar Warned Off**: read by s01 and M5. Both must actually read them.
  - **Handler Ledger Read**: read by s01, r03 and M5.
  - Collapse the other five ledger states into this one, plus **Handler Ledger Lost**: Rusk collected it or it burned. Read by M5.
- **Cut:** "What the Breach Proves" and the Cassalanter contact consequence.

### M3 The Doppelganger Auditions (overview, ev-01, ev-02-the-tail, design-notes). Report 03 §1–3, §7 rows 7–12, 17, 20–21, 23

- **The Brief:** Mirt in person at the Yawning Portal.
  - He tells them up front that, in his considered opinion, one of the five has already sold the party's Harper affiliation (Appendix C :253).
  - Social plus qna.
- **The crew: five in total.**
  - **Bonnie**, the leader. She wears her Tethyrian human barmaid form in the main room.
  - **Edric Tanner**, the traitor.
  - **Kael**, uninterested.
  - **Syla**, undecided.
  - **the Scholar**, who would monetise membership.
  - **Cut the Merchant.**
- **Interviews:** two evenings at a Portal table with Mattrim "Threestrings" Mereg (Harper agent) playing.
  - Each interview gets a social block, 2–3 qna and one tell.
  - **Edric's tells:** asks for Harper knowledge; can't talk about his own Waterdeep; DC 16 Wisdom (Insight) catches the rehearsed answers; DC 13 Intelligence (Investigation) on his hands (no teamster calluses).
  - **Bonnie:** DC 15 Wisdom (Insight) shows she is evaluating them.
- **Mattrim's reveal:** after both evenings. Bonnie has known for three weeks and Mattrim learned a week ago.
- **Report to Mirt**
  - Bonnie alone is trustworthy. Mirt: "Bonnie. Yes. I thought it might be Bonnie."
  - **The other four are not recruited.**
  - Bonnie's offer: a Harper operative role on her terms (her crew's identities protected, intelligence routed through the members). She can refuse.
  - 50 gp to every contributing character.
- **ev-02 The Tail:** fires if Edric was not identified, or was identified but not held.
  - The morning after the second evening. Spotting him is Passive Perception 15 or DC 14 Wisdom (Perception).
  - He shape-shifts to escape. DC 13 Strength (Athletics) cuts him off.
  - Search him: DC 14 Intelligence (Investigation) finds the address.
  - **Nethpranter Street safehouse** (Trades Ward): two Spies on the ground floor, files upstairs.
  - The files hold surveillance notes on Mattrim, the same two noble-house assets the M2 cipher named, and correspondence naming a handler.
  - Read **Harper Contacts Relocated**: if marked, the assets are already safe.
  - No "Kolat Towers raid tuned to the PCs". If Edric's report reaches its buyer, write **Edric Report Delivered**.
- **Renown:** 3 base. +1 Edric identified before he reports. +1 Bonnie recruited. +1 safehouse found and reported.
- **Outcomes** (one writer each):
  - **Edric Identified**: ev-01.
  - **Edric Captured** / **Edric Report Delivered**: ev-02. **Kolat Towers** (unconverted) reads Delivered.
  - **Bonnie Harper Operative**
  - **Nethpranter Safehouse Reported**: **Faction Outposts** (unconverted).
  - **Harper M3 Complete**: written once, in the last event that runs. Read by Emerald Enclave M3; keep the name exactly.
  - Cut **Bonnie Neutrality Pact** and **Edric Report Prevented**.

### M4 A Friend's House (overview, ev-01-the-salon, ev-02-the-tail, ev-03-the-confrontation, design-notes). Report 04 §1–3, §7 C1, C2, C4, C15–C20, C23

- **The Brief:** Mirt's note, or a briefing at 17:00. Dress sharply, using a Delzorin Street tailor (Seldo Wynd, Seldo's Fine Stitches, 8 Delzorin Street).
  - The job: one of Remi's guests is a spy for "someone remarkable". Find out who, and for whom.
- **Read Jarlaxle Unmasked** (written by Fireball ev-04, the Sea Maidens Faire):
  - **Marked for a member:** that member has met "Zardoz Zord" and knows he is Jarlaxle Baenre. The salon task is recognising him under a second disguise. Erystian's tells may be checked against what they saw on the *Eyecatcher*.
  - **Unmarked:** a correct identification at the salon marks it for each character present.
  - Either way, no BD Renown is awarded here.
- **ev-01 The Salon:** House Ulbrinter. Remallia hosts. **Twelve guests.**
  - **Erystian Demarne:** "a young actor from Luskan", sandy-haired Illuskan, using a hat of disguise. He is Jarlaxle.
  - **Identification:** DC 24 Wisdom (Insight), reduced by 2 for every three probing questions (22 after three, 20 after six). The physical tell is hand-crossbow calluses (DC 14 Wisdom (Perception)). Two independent evidence lines also confirm.
  - Remi smooths a failed social roll within 30 seconds (failed DC 12 Charisma).
  - **Guests:** keep the strongest leads, each a social block with 1–2 qna. Prev names stay. Leads stay commercial suspicion.
    - Saeth Cromley (retired Watch sergeant; Dalen Voss, his missing officer, was Corene's contact; read by M5).
    - Tessabrant Elamondra (dye).
    - Aldric Talmost (a windfall).
    - Zalara Moonwhisper (the 1244 DR reserve record).
    - Farrak Iltimer (rubies).
    - Serithka Ondal.
    - **Jelenn Urmbrusk** ("she"; a Masked Lord being blackmailed; she leaves within 3 minutes if the Zhentarim come up; DC 18 Wisdom (Insight)).
  - **Mara Coppersail** (a Faire ticket clerk and Harper informant) is a lead Erystian lets slip.
  - **Remi's Harper role is revealed** at the end of the evening.
- **ev-02 The Tail:** if they follow Erystian. Make it a real stage with a failure branch. He notices on a failed DC 15 Dexterity (Stealth) and turns it into a conversation at a canal bridge. The BD signal site (chalk spider-and-blade mark) is on **4 Swords Street**.
- **ev-03 The Confrontation:** the calling card arrives two days later (harp and crescent crossed by a rapier). Jarlaxle's departure speech follows Appendix C, then the wrong-accusation branch, then Mirt's reaction.
  - Jarlaxle never mentions Lolth with anything but contempt.
  - He does not volunteer "Bregan D'aerthe" unless **Jarlaxle Unmasked** is marked.
- **Renown:** 3 base. +1 correct identification reported. +1 cover profile documented. 200 gp to every attendee the next morning.
- **Outcomes** (one writer each, across the three events):
  - **Remallia Harper Contact Known**: ev-03, or the last event run. Read by r10, r25 and r50.
  - **Salon Guest Leads Recorded**: read by M5 for Saeth/Dalen.
  - **Jarlaxle Identity Exposed at Harper Salon**: read by **Sea Maidens Faire** (unconverted).
  - **Erystian Profile Reported**: **Sea Maidens Faire** and **Faction Outposts** (unconverted).
  - **Jarlaxle Discretion Agreement**: needs a reader. BD s03 or a log entry.
  - **Jarlaxle Unmasked**: only on the unmarked branch.
  - Cut **BD Signal Site Observed** and **Erystian Cover Observations Recorded** unless you give each a real reader.

### M5 The Sleeping Asset (overview, ev-01, design-notes). Report 04 §1–3, §6, §7 C7–C12, C16, C23

Split into two events if the stages need their own state, following DR m04 and BD m04: ev-01 finding and confirming Corene, ev-02 the extraction and the mole. Your call.

- **The Brief:** Mirt arrives at dawn by the back door with a copied key.
  - Corene Wyldath (Spy), under cover as "Halla Ironstave" in the Dock Ward for **four months**, missed her check-ins **three weeks** ago.
  - Social plus qna.
- **Leads:** three independent ones.
  - Harper Dock Ward contacts saw her calm in a Watch sweep at a Shrimp Street warehouse.
  - The Harbormaster's assistant saw her at a cargo review.
  - A Field Ward landlord says she prepaid three months.
  - Plus Saeth/Dalen if **Salon Guest Leads Recorded**.
  - All of them converge on the Trades Ward plaza bench where she meets her contacts.
- **Detection**
  - DC 15 Wisdom (Insight) on eye contact and speech.
  - DC 12 Intelligence (Arcana) or Wisdom (Medicine) after 5 minutes.
  - DC 14 Wisdom (Insight) on her fishing questions.
  - *Detect thoughts* alerts the devourer.
- **Resolution: the custom occupying devourer.** Use the mechanics reference's extraction procedure exactly. Three resolutions:
  - **Extract:** Corene lives. She needs a Long Rest, then gives four months of Dock Ward intel.
  - **Kill the host:** Corene is lost, and the Guild's Dock Ward sites go to Alert for 14 days.
  - **Leave in place and feed it false reports:** the double-agent play, written through **Nihiloor False Report Confirmed**.
- **The mole**
  - **Tobin Harrask** (renamed from Orren Vale) is the records-relay clerk. He copies every operational entry in his register to Beldan Rusk exactly 48 hours later.
  - Corene's recovered memory, the M2 ledger (**Handler Ledger Read**), or the timing of s01's incidents expose him. That makes three independent paths.
  - Read **Tessalar Turned/Arrested/Warned Off**: a turned Tessalar can identify Rusk's pickup.
  - Write **Harper Mole Identified** and **Harper Leak Closed**.
- **Lair order.** Corene's intel must work whether or not Xanathar's Lair has run.
  - Before the heist: the intel feeds **Xanathar's Lair** (unconverted).
  - After it: it maps the Guild's Dock Ward remnants and Nihiloor's surviving puppets.
  - Mirt: "Three devourers. Three of ours." Keep the other two unnamed.
- **Renown:** 4 base. +1 Corene extracted alive. +1 the mole identified before the next leak.
- **Outcomes:**
  - **Corene Rescued** / **Corene Lost** / **Corene Left in Place**: read by **Xanathar's Lair** (unconverted).
  - **Nihiloor False Report Confirmed**
  - **Harper Mole Identified**
  - **Harper Leak Closed**: read by r03–r50 and **Kolat Towers** (unconverted; logged as moot if Kolat already ran).
- **Cut:** the invented Remallia *Remove Curse* 1/Day, unless the mechanics reference gives her that statistic.

### M6 The Stone's Other Master (overview, ev-01, design-notes). Report 04 §1–3, §6, §7 C6, C13, C14, C22

- **Timing**
  - Runs at Renown 13 and 7th level. That means after all four heists, Kolat Towers included, and before the Vault of Dragons opens.
  - The Stone has all three Eyes. Write nothing about Eye counts.
  - Read the Kolat Towers result in GM text ("if Kolat Towers left Manshoon alive… otherwise…"). Kolat is unconverted, so give both branches.
- **The Brief:** Mirt comes after midnight.
  - A Harper seer felt "something old and patient below the city".
  - Cite the Illuun thread: if the party has met it through Emerald Enclave s02, members recognise the description.
  - He asks for three days with the Stone. The party can agree, refuse or bargain. Give each a consequence and no free rolls.
- **The compromised contact:** **Jalester Silvermane** only, never Renaer. The study reveals him.
- **The raid**
  - Splinter survivors, roster from the mechanics reference.
  - A Mage leader, Spies and Toughs. **No Contingency**, and nobody escapes "to Kolat".
  - Their aim is to take the Stone for whatever is left of their master.
  - Hazard block with tactics, a surrender or retreat condition, and a non-combat route.
  - The sending stone is recoverable. Its replies are in a voice the members cannot place unless **Manshoon Named** is marked.
- **The study:** three days. Vault-guardian intel, plus Jalester's name only if asked directly.
- **Renown:** 4 base. +1 study completed. +1 raid defeated and the sending stone taken.
- **Outcomes:**
  - **Stone Study Completed**: **Vault of Dragons** (unconverted).
  - **Jalester Compromise Identified**: **Vault of Dragons** (unconverted) and Lords' Alliance M6 (free-text reader, logged).
  - **Splinter Sending Stone Recovered**
  - **Stone Taken by Splinter**: read by **Vault of Dragons** (unconverted).
  - Cut **Splinter Raid Observations Delivered** (it had a Kolat reader).

### s01 The Cell Is Compromised (ev-01, design-notes). Report 02 §1–2, §6 rows 9–11, 22

- **Trigger:** after M4, for each Harper member.
  - A plain note ("Come alone. Be careful.").
  - A rented third-floor front room at 6 Brondar's Way, North Ward. The note arrives at 16:00 and the meeting is at 19:00.
  - The wine is sealed and he doesn't open it. That is a deliberate signal from a man who always refills.
- **What Mirt says:** the cell is compromised. The Splinter acted on Harper-only information. He doesn't know who. Fourteen people touched the material.
- **Incident list:** each line reads a named outcome.
  - **Shesstra Street Reported**
  - **Handler Ledger Read**
  - **Tessalar Turned/Arrested/Warned Off**
  - **Salon Guest Leads Recorded** (the Jelenn query)
- **Davil line:** only if a member has met Davil Starsong. If **Davil Arrested** is marked and **Davil Released** is not, the corroboration came through Tashlyn instead.
- **Checks:** DC 15 Charisma (Persuasion) ("I know it's not you."); DC 13 Wisdom (Insight) (he's been on this longer than a tenday).
- **Private protocol:**
  - Operational intelligence goes only to Mirt, in person.
  - Paper birds carry meeting times only.
  - Anything already told to another contact gets reported to him.
- **Fixed leak rule** (GM-only): every operational entry in the relay register is copied to Rusk exactly 48 hours later until **Harper Leak Closed**. Nothing is rolled. Mirt says "a couple of days" aloud.
- No renown, gold or Milestone.
- **Outcomes:**
  - **Harper Leak Known**: read by M5 and the rank events.
  - **Harper Private Protocol Adopted**: read by M5, which checks which channels were used.

### r03 Harpshadow (ev-01, design-notes). Report 02 §1–2

- **Trigger:** a noon bird the day after the threshold. Dinner at Mirt's manor at 20:00. A member who is away gets the next evening after they return.
- **Benefit 1, Mirt's question:** one direct question per tenday, on its own 10-day count, answered sealed at noon the next day.
  - The first question is answered now, with confirmed facts only.
  - It branches on **Shesstra Street Reported** and **Handler Ledger Read**.
  - If asked who leads the Splinter: "The Black Network has split, that much I know."
- **Benefit 2, three ward contacts.** Opening phrase: "May I leave a receipt for the next delivery?" Available 09:00–17:00. One question per contact per member every 10 days.
  - **Nella Fen**, chandler, 16 Fillet Lane, Dock Ward.
  - **Orin Dask**, map-seller, 9 Street of Silks, Trades Ward.
  - **Bram Pell**, barber, Swords Street, Castle Ward.
- **Benefit 3, faction rate:** 90% of the published price at those three, mundane stock only. This is a remix concretisation of Appendix B; say so in the design notes.
- **Forgotten-phrase rule:** keep it.
- Mirt does not swear at this business dinner.
- **Outcome:** **Harpshadow Reached**, marked with the recipient's name; per-member tracking line. Read by **Brightcandle**.

### r10 Brightcandle (ev-01, design-notes). Report 02 §1–2

- **Who meets them:** Mirt alone, or Mirt and Remi if **Remallia Harper Contact Known** is marked.
- **Requisition:** Evin Talver, Blue Bottle Apothecary, 24 Sorn Street, 09:00–18:00.
  - One *potion of healing* or one cantrip/1st-level *spell scroll* per mission, on 24 hours' notice.
  - Use one passphrase, not the prev quarterly phrase table.
- **Field agent:** **Perrin Valt** ("Reed"), Spy, one per quest per member.
  - He arrives 24 hours after the request at a named surface point, or at the Yawning Portal if the job is underground.
  - Spy ally Power comes from the mechanics reference.
- **First persona** (by Remi, or a "Harper mentor" before she is known):
  - Three questions, then a packet in 3 days.
  - Default cover: a Vale & Reed Imports traveling order clerk, surname Varn, confirmed by Nella Fen and Orin Dask.
- **Outcome:** **Brightcandle Reached**, read by **Wise Owl**.

### r25 Wise Owl (ev-01, design-notes). Report 02 §1–2

- **Cover service:** one per quest, on 3 days' notice, in one of three forms.
  - Documents (Vale & Reed).
  - A distraction (courier **Wil Keen**'s broken cart, 10 minutes).
  - Witnesses (Nella and Orin).
- **Three informants:** DC 13 Charisma to activate. **One request per informant per quest.** A failure makes that informant unavailable for two tendays.
  - **Lantern:** Dena Holt, Guild warehouse courier.
  - **Canvas:** Joss Marrin, Faire ticket clerk. Not Mara if she was recovered.
  - **Slate:** Darron Quill, Splinter cargo clerk. No access to the sanctum.
- **Priority-target warning:** within 24 hours.
- **Laeral**
  - A silver raven is sent; the reply note ends "Mirt speaks well."
  - It confirms a channel and spends no audience. An urgent audience is at 10:00 two days after a specific danger-with-deadline request, in the Palace east reception room.
  - Mirt: "Don't bring her a problem you could solve on your own."
- **Second persona:** default surname Dale; confirmed by Ilen Castor, cartwright.
- **Outcome:** **Wise Owl Reached**, marked when the reply note arrives. Read by **High Harper**.
- **Design notes:** Renown 25 needs bonuses or Mad Mage play.

### r50 High Harper (ev-01, design-notes). Report 02 §1–2

- **Setting:** expected during Dungeon of the Mad Mage.
  - A silver raven at noon the first day the member is in Waterdeep. The meeting is at 20:00 by the garden gate.
  - Mirt's library, Remi present (if known), and Variel Duskwhisper as courier witness. Variel tunes the same string; pick the **fiddle**.
- **Benefits:**
  - **Archives:** a named topic, copies brought at 10:00 the next day, current embedded identities removed.
  - **Team:** three Spies on 2 days' notice.
  - **Mirt accompanies once:** meets at 09:00, stats from the mechanics reference.
  - **Extraction:** a wagon and three Spies, 2 hours after the request. Courier order Wil Keen, Della Morn, Oswin Bell.
  - **Exposure dossier:** Cassalanter suspicion never becomes knowledge.
  - **Third persona:** surname Talar.
- **The reveal:** "I'm a Masked Lord of Waterdeep." "Laeral knows." He names no other Lords. "Keep my seat out of public accounts."
  - If the member already guessed it, let them say so.
- **One invocation:** Watch cooperation, a Lords' Court hearing, or a warrant of immunity. Delivered in 3 days, now or held. Refusals come before the use is spent.
- **Outcomes:**
  - **High Harper Reached**: **Vault of Dragons** (unconverted) and Mad Mage.
  - **Masked Lord Request Invoked**: marked only when Mirt accepts.

## Reports back

Each drafter reports back:
- the files written;
- outcomes set and read;
- invented names;
- every outside-folder contradiction with file:line, for the Session 41 out-of-scope log.
