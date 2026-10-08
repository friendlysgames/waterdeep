# Force Grey Conversion Brief (Session 42)

## Context

The user asked for the Force Grey events to be rewritten the way the Harpers were in Session 41: restore, research, plan, then draft on the DR/BD page model. The user also said: "make sure you also read how BD and DR are done, one or two events from each, so you get a full picture."

**Inputs**
- **Rewrite input.** Every Force Grey file is restored to its first commit (`dafada7`).
- **Previous version** (fact source only): git `c11ee45`. A copy is at `/tmp/claude-0/-home-user-waterdeep/a2f34fba-baef-54d3-97ed-3a637e207a74/scratchpad/fg-prev/campaign/quests/faction-events/force-grey/`. Only its settled facts survive. It is only half converted, so don't copy its structure or prose.
- **Approved plan:** `docs/plans/force-grey-plan.md`.
- **Research reports** in `docs/plans/force-grey-research/`:

  | File | Covers |
  |---|---|
  | `01-spec-and-structure.md` | Page model, R/PREV inventory, gates, ranks, the contact object |
  | `02-first-meeting-s01-ranks.md` | 00, s01, r03, r10, r25, r50 (§5–6 and §10 hold the recommendations) |
  | `03-m01-m03.md` | M1–M3 (§2.7, §3.7, §4.4–4.7, §9.4) |
  | `04-m04-m06.md` | M4–M6 (§1.7, §2.6–2.8, §3.6–3.9, §5) |
  | `05-consistency-audit.md` | Outcome map, outside references, rule audit, voice limits (§8) |

- **The Meloon and Vajra/Zelifarn `.docx` guides** are converted to text in `.../scratchpad/docx-text/`. They are third-party homebrew. Use them only where this brief adopts them.

Where a report lists options, this brief has already chosen. Where a report and this brief disagree, this brief wins.

## What went wrong with the restored and previous pages (avoid all of it)

**Format**
- Retired formats everywhere: `[GM]`, `[!profile]`, `[!dialogue]`, `[!design]`, True/False flags, `Milestone: None`, `## Read Aloud` and "Arc X" labels.
- No `Who Knows What` block, and no Brief built from `[!social]` and `[!qna]`.
- Rank benefits written as flat lists instead of procedures.

**Rules and facts**
- Vajra, Hlam, s01 and M6 name Manshoon and Kolat Towers without the gate.
- Wish cures Meloon.
- *Sendings* claimed to be 25 words actually ran 9–24.
- The rank titles were handed out by M4 and M6.
- The M6 roster is impossible at every party size.
- Soluun is held in the lair, contradicting BD/DR.
- The M4 room codes clash with Xanathar's Lair.

## User decisions (Session 42)

1. **M4 is an additional objective inside Xanathar's Lair**, not a separate raid.
   - Vajra's M4 brief fires when a Force Grey member who has finished M3 prepares for **Xanathar's Lair**. It has no level gate.
   - The objective plays inside the lair heist when the party reaches Nihiloor's wing.
   - If the lair has already run when M3 ends, M4 is a short debrief instead. Vajra credits what the party did in Nihiloor's wing, and the GM marks the M4 outcomes from what happened there.
2. **M6 runs at 7th level, after Kolat Towers**, as Harper M6 does.
   - Splinter survivors raid Blackstaff Tower, and the event branches on what Kolat Towers left of Manshoon.
   - The "captured agent names Kolat" reveal is cut.
   - Parties that run three heists play M6 after the Vault, and the Vault does not read it as a prerequisite.
3. **The renown ladder wins.**
   - No mission changes rank. M4 earns a written commendation and M6 earns recognition, both story only.
   - Titles come only from r03, r10, r25 and r50.
4. **Soluun and Nar'l.**
   - Nar'l is cut from Force Grey.
   - The default prisoner in Nihiloor's wing is **Zaibon Kyszalt** (WDH X24), who is waiting to be implanted.
   - Soluun appears instead only if **Soluun Expelled** (BD) is marked. If **Soluun Killed** is marked, or neither mission ran, it is Zaibon.
5. **Gates and renown use the shared ladder.**

   | Mission | Gate |
   |---|---|
   | M1 | joining, 2nd level |
   | M2 | Renown 3, 3rd level |
   | M3 | Renown 5, 4th level |
   | M4 | Renown 8, or **M3 Complete** plus **Xanathar's Lair** preparation (decision 1) |
   | M5 | Renown 10, 6th level |
   | M6 | Renown 13, 7th level |

   - Base renown is 2 / 2 / 3 / 3 / 4 / 4, plus up to three `+1 Renown:` lines, each tied to a named condition and each awarded once.
   - Phrase every gate: "becomes available when an individual Force Grey member reaches Renown N and Nth level".
6. **Zelifarn is a Young Bronze Dragon** (WDH and the Zelifarn guide). Sea dragons don't exist. Fix the Notable Figures page in the companion pass.
7. **M2 uses the Fleetswake variant from the Zelifarn guide.**
   - Zelifarn has been taking Umberlee's offerings, believing them abandoned.
   - Meritide Blackfin, the Darfellan high priest at the Queenspire, gives the party 48 hours.
   - The party persuades Zelifarn to return the offerings, or covers it up and risks the goddess.
   - Don't use the conch or the megalodon.
8. **Nihiloor always escapes.**
   - He flees at a set threshold, set in the mechanics reference.
   - M4 can win the Spawning Pool, the placement records and the captive. It never kills him.
   - Harper and Order of the Gauntlet lair hooks that ask for him dead are logged out of scope.

## Standing defaults

**Secrets**
- **Manshoon.** Use the DR/Harper **Manshoon Named** gate (written by **Faction Outposts**, unconverted).
  - Until it is marked for a member, Force Grey speakers say "the Splinter", "the other cell" or "the Black Network has split".
  - Kolat Towers as his home is gated too.
  - GM text may state the truth.
  - Overview and Involved Characters labels say "the Splinter".
  - **Hlam** never names him. His second answer is a riddle about an old wrongness shaped like the city's old Black Network coming back. He never explains it, and his voice doc says he never explains a riddle.
- **Cassalanters.** Suspicion only. In s01 Vajra sees "the outline" of something under the villa and does not speculate. Nobody knows of the pact.
- **Jarlaxle.** No Force Grey speaker says "Jarlaxle" or "Bregan D'aerthe" to players. Zelifarn and Vajra speak of "the carnival fleet" and "the *Eyecatcher*'s crew". GM text may name them.
- **Zelifarn's mother** is never mentioned. That reveal belongs to Sea Maidens Faire.

**Membership**
- Recruitment, briefs, debriefs, renown, ranks and benefits belong to individual Force Grey members. Companions can help with everything else and earn no renown.
- A character already in another faction gets no offer. Vajra says so in one qna answer, as DR/BD/Harper do.
- Joining is per character. **Force Grey Offer Closed** is marked with the names of the unanswered candidates.
- Rank benefits are tracked per member. Where a benefit helps "the party" (a spell, an ally), the holder brings their companions along for that operation.

**Vajra Safahr**
- **Stat line:** Neutral, Tethyrian Human, she/her (from the Notable Figures page). Never state her tenure.
- **Voice** (`voices/force-grey.md`):
  - short orders and conclusions;
  - "Irrelevant.", "Force Grey will handle it.", "Next.";
  - calls doubting wizards by surname;
  - answers "Are you alright?" with "Irrelevant.";
  - never asks for sympathy;
  - never discusses the Blackstaff's contents;
  - never mentions Khelben;
  - says "the Open Lord", never "Laeral".
- **Swearing:** casual, colourful, frequent in private (her study after hours, the M6 wards crisis), barely clean in public. Give her real swearing in private scenes.
- **Why she trusts Renaer** (GM-only, What Is Actually True): Renaer, Laraelra Harsard and Meloon pulled her out of Khondar Naomal's cells. She never tells this to the party.

**The contact object: Vajra's *Sending***
- Every Force Grey contact is a *Sending* of **exactly 25 words**. The main session will count every one.
- **The canonical description**, written once per event in its arrival readaloud: a dry, flat voice arrives behind the eyes with no greeting, fast and clipped. It lands while the recipient is doing something else, and nobody nearby hears it. The recipient can answer in up to 25 words.
- Rank Sendings open with the rank's name.
- **At Blackstaff Tower**, the door opens before anyone knocks and Vajra stands at her standing desk. There is no chair for visitors.
- **The Gray Hand credential** is a letter of authorization on Tower letterhead, folded twice, with her mark. Each accepting candidate gets one.
- **The deliberate break** comes in M6: a door attendant meets the party in person instead of a *Sending*, which tells them something is wrong.

**Meloon, the devourer and Nihiloor**
- **The Occupying Devourer** is the campaign rule: `docs/plans/harpers-mechanics-reference.md` §5. Cite it by section.
  - No Wish anywhere.
  - Telepathy reaches 60 ft, so hosts report through a Guild-paid courier.
  - The hosted body keeps its brain.
  - Recovery: 1 Exhaustion, fragments until a Long Rest, then the whole occupation remembered as a long dream. The host never knows what the devourer passed on.
- **Meloon's occupation** began after the Field of Triumph, about three tendays before the first day of the watch.
  - The devourer took him into the lair twice, both before the watch.
  - **Azuredge** is a sentient blue battleaxe. While occupied, Meloon never draws it and never swears.
  - He has two excuses for the missing axe (it's "with the armourers"; it's "lent to a friend"), and an Insight check shows he is lying.
  - Each dawn the devourer must succeed on a DC 15 Charisma save to touch the axe. Keep that in GM text.
  - The axe is his anchor for the anchor route.
- **Durnan** has noticed and says nothing in company. Two to six words, flat, swears dry.
- **Bonnie** reads Meloon's surface thoughts and takes one character aside: "Something ain't right with him."
  - If **Bonnie Harper Operative** is marked, or the party otherwise knows she is a doppelganger, she says how she knows.
  - Otherwise she gives no reason.
  - She never reveals what she is to a party that doesn't know. Use `voices/harpers.md`.
- **Mirt's "three of ours"** line in Harper M5 stands. Force Grey's hosts (Meloon, Orvyn) are separate, and a GM line in M3 and M5 says so.

**Rules**
- 2024 rules and names only. Use **Warrior Veteran**, never "Veteran". No Thug.
- Every roster comes from `docs/plans/force-grey-mechanics-reference.md`.
- Checks read "**DC N Ability (Skill)**" with a stated fallback. No single check settles a mission.
- Fights go in `[!hazard]` with `#### X's Tactics`, an end or retreat condition and a non-combat route.
- *Detect magic* shows no spell on an occupied host, only magic items.
- **Undermountain rule for r50:** teleportation, *plane shift* and *word of recall* fail in Undermountain. *Sending* works there, but never reaches Halaster. Vajra's last-resort spell is cast on the surface or at the Yawning Portal only. *Wish* is excluded.

**Calendar.** Give spans in tendays. Keep "Ches 21" for Fleetswake.

**Renames (collisions)**

| Old | New | Collides with |
|---|---|---|
| Aldris Maeven (r10 Tower mage) | **Ysmay Halvane** | Aldric Talmost, Aldric (staff guide) |
| Rhendar Solne (r25 ally) | **Rhendar Orsk** | Vira Solkan |
| Tolliver Brack (r50, mechanics reference) | **Garrick Stoll** | Tolliver (DR M3) |
| Isolde Fenn (r50, mechanics reference) | **Sera Vantry** | Isolde (Harper First Meeting) |

Merris (quartermaster) stays. Invented minor NPCs are voiced from the event text and listed in each folder's design notes under "Invented Names and Open Items".

## Event Outcomes (one writer each; mark with the member's name where individual)

| Outcome | Writer | Readers |
|---|---|---|
| **Force Grey Joined** | 00 | Force Grey Factions Guide, every Force Grey event, Trollskull ev-04 (out of scope) |
| **Force Grey Offer Closed** | 00 | 00 on re-fire |
| **Hlam Consulted** | M1 | Trollskull ev-04 and ev-06 (out of scope), s01 |
| **Buried Thing Reported** | M1 | s01, **Vault of Dragons** (unconverted) |
| **Zelifarn Contacted** | M2 | **Sea Maidens Faire** (unconverted) |
| **Zelifarn Befriended** | M2 | **Sea Maidens Faire** (unconverted, arc-h:115) |
| **Submarine Reported** | M2 | **Sea Maidens Faire** (unconverted) |
| **Offerings Returned** / **Offerings Kept** | M2 | **Sea Maidens Faire** (unconverted); Kept also read by r03 (Meritide's grudge, one line) |
| **Meloon Restored** | M3 ev-02 | M4, M5, r10 |
| **Meloon Lost** | M3 ev-02 | M4, r10 |
| **Devourer Escaped** | M3 ev-02 | M4 |
| **Courier Identified** | M3 ev-02 | M4, M5 |
| **Nihiloor Identified Party** | M3 ev-02 | M4, **Xanathar's Lair** (unconverted) |
| **M3 Complete** | M3 ev-02 | M4 brief trigger |
| **Pool Destroyed** | M4 ev-02 | M5, **Xanathar's Lair** (unconverted), Harper M5 (outside, logged) |
| **Placement Records Taken** | M4 ev-02 | M5 (one of three leads to Orvyn) |
| **Captive Freed** | M4 ev-02 | **Bregan D'aerthe** (if Soluun; logged) |
| **Nihiloor Fled** | M4 ev-02 | **Xanathar's Lair** (unconverted), s01 |
| **Orvyn Restored** / **Orvyn Lost** / **Orvyn Left in Place** | M5 ev-02 | M6, r25 |
| **Orvyn Ledger Delivered** | M5 ev-02 | M6, **Vault of Dragons** (unconverted) |
| **Vira Caught** / **Vira Escaped** | M6 ev-02 | r50, **Vault of Dragons** (unconverted) |
| **Tower Attack Stopped** | M6 ev-02 | **Vault of Dragons** (unconverted, arc-j:51), r50 |
| **Splinter Testimony Recorded** | M6 ev-02 | **Vault of Dragons** (unconverted) |
| **Vajra Briefed** | s01 | **Vault of Dragons** (unconverted), r50 |
| **Junior Griffon Reached** | r03 | r10 |
| **Senior Griffon Reached** | r10 | r25 |
| **Force Grey Rank Reached** | r25 | r50 |
| **Force Grey Commander Reached**, **Recognition Public**, **Recognition Sealed** | r50 | **Vault of Dragons** (unconverted), Dungeon of the Mad Mage |

**Read but not written here**
- **Manshoon Named** (Faction Outposts).
- **Meloon Met** (Trollskull ev-05, retired format, logged).
- **Soluun Expelled** / **Soluun Killed** (BD s05 / DR M1).
- **Bonnie Harper Operative** (Harper M3).
- The Kolat Towers Manshoon result (Destroyed / Simulacrum Only / Alive), read the way DR M6 and Harper M6 read it.

**Dropped:** Possession Confirmed, Azuredge Contact Made, Swearing Absence Noted, Vajra Full Report, Azuredge Intel Filed, Mission 4 Alert, Gray Hands Promoted, Soluun Rescued/Stabilized, Evil's Twin Heard. Fold their effects into scene text.

## Per-folder briefs

Each drafter reads its report sections first, then applies these instructions, which win over the report.

### 00 First Meeting: "A Message from the Blackstaff" (ev-01, design-notes). Report 02 §2a, §5a, §6a–d, §10
- **Candidates and contact**
  - Candidates are every character in no other faction.
  - The first *Sending* goes to the candidate who spoke to Renaer last in the warehouse. If the GM can't tell, it goes to the candidate with the highest Wisdom.
  - Its text, exactly 25 words, keeps the WDH line and adds Renaer: "Renaer has told me about you." It also says "Bring your friends."
  - **Re-fire rule:** if nobody goes, a second *Sending* reaches a different candidate the next morning. If still nobody goes, mark **Force Grey Offer Closed** with the unanswered names. The event re-fires when the party advances a level, with the same 25 words.
- **Scenes:** The Sending, Blackstaff Tower, The Standing Desk, Each Candidate's Answer, Leaving the Tower.
  - At the Tower: Appendix B's building near Swords Street, with the door that reads them as they climb.
  - At the desk: Vajra's social block and 6–8 qna, with no filler.
  - **Will not discuss:** the Stone, the vault, the Splinter's master, the Cassalanters, the staff, Undermountain, her youth.
  - **Checks:** DC 14 Wisdom (Insight) shows she decided before they arrived. Optional DC 13 Intelligence (Arcana) at the door.
- **Gray Hand Benefits box** (per member): Renown 1; entry to the Tower at any hour; one consumable before a mission that needs it (fix a short list); Watch officers are Friendly; the Tower letter.
- The renovation help (a *Tiny Hut* casting and the vault item) is a party-level line, because the manor is shared.
- **No first mission is handed over.** **Consulting Hlam** comes by its own *Sending*.
- **Closing line:** "Try to get some sleep. The work does not wait for people to be rested."
- **Summary:** "After the Meeting" and "Without a Private Meeting" variants.

### M1 Consulting Hlam (overview, ev-01, design-notes). Report 03 §2
- **Structure:** one event. Scenes: The Brief, The Climb, The Cave, What He Offers Unasked, The Report.
- **Hlam's lines:** keep his source lines, broken into short spoken lines. Voice: "student", tea he drinks himself, "The mountain does not hurry."
- **The second answer** is the riddle (see Standing defaults). No speaker says "Manshoon".
- **Two decision points:**
  - Hlam asks "Who sent you?" Honesty works. Evasion or a lie gives Disadvantage.
  - At the report, Vajra asks for it "in order", and the party chooses whether to give the buried-thing message word for word.
- **Renown:** 2 base. +1 message delivered verbatim. +1 second answer won without invoking Vajra's authority.

### M2 The Dragon in the Harbor (overview, ev-01, design-notes). Report 03 §3, §9.2, §9.4
- **Hook (adopted):**
  - The dragon is reported just outside the Dragonward, which is why Vajra cares.
  - **On Ches 21–30** the Queenspire hook fires first: Meritide Blackfin, the 48 hours, and the missing offerings. Renaer sends the party to Vajra.
  - **On any other date**, Vajra's *Sending* opens the mission and Meritide's complaint reaches them at the harbor.
  - Write both openings as paired readalouds.
- **Scenes:** The Brief, The Vials (one *potion of water breathing* per member and companion, durations from the 2024 rules), The Descent, The Wreck, Zelifarn's Trade, The Offerings, The *Eyecatcher*, The Report.
  - **The Descent** runs on a short GM ledger in the BD m04 style, using the potion as the clock.
- **Zelifarn**
  - Uses the 2024 Young Bronze Dragon block.
  - He never lies and trades facts for facts. Voice from `voices/bregan-daerthe.md`.
  - He submerges if attacked.
  - He knows the *Eyecatcher* has something under her hull and that the crew discouraged him. He doesn't know whose ship it is.
- **The offerings choice:** persuade him to return them (**Offerings Returned**: Meritide is satisfied, and the 48-hour threat passes), or cover it up (**Offerings Kept**: Meritide remains suspicious, one line in r03).
  - Umberlee does nothing on screen. The risk is Meritide's grudge.
- **Renown:** 2 base. +1 Zelifarn confirmed non-hostile. +1 submarine reported in usable detail. +1 offerings returned.

### M3 The Trouble with Meloon (overview, ev-01, ev-02, design-notes). Report 03 §4.4–4.7, §9.4
- **Two events:**
  - **ev-01 The Tenday Watch** marks nothing and chains to ev-02.
  - **ev-02 The Extraction** marks everything. It replaces "Azuredge Confrontation", so delete the old file name.
- **ev-01 scenes:** The Brief, Day 1 at the Portal (Durnan, Meloon's table), The Morning Ritual (Azuredge speaks: concern, frustration, hope), The Conversation (Day 5, the hosted Meloon's social and qna), Bonnie (new), The Courier (Day 8–9, optional trail), What You Can Confirm (the detection table from §5), The Report.
  - Read **Meloon Met** as paired readalouds: he was himself on the sand.
- **ev-02 scenes:** Vajra Acts, Getting Him Alone, Forcing It Out, The Hosted Meloon, The Expelled Devourer, What the Party Decides, What Meloon Remembers, Vajra's Debrief.
  - **Vajra Acts:** three 4th-level *dispel magic* casts, with no ward, no roll and no Strain.
  - **Getting Him Alone** has three ways to get him somewhere quiet.
  - **Forcing It Out** is an exploration block modelled on Harper M5 ev-02.
  - **The Hosted Meloon** fights with the Warrior Veteran's weapon, never Azuredge.
- **Clock:** the courier meets Meloon on Day 10. **Nihiloor Identified Party** is marked only if the Day 5 conversation happened and the devourer was still in place on Day 10.
- **Fixes:**
  - Meloon speaks only in fragments until a Long Rest.
  - The junior quartermaster keeps two vials of holy water.
- **Reward:** the *wand of secrets* on success. Vajra says "You earned this."
- **Renown:** 3 base when the matter is settled. +1 Meloon restored alive. +1 Azuredge's resistance reported. +1 courier identified, or the extraction done before Day 10.
- **M3 Complete** is marked for each member who took part when ev-02 ends, whatever the result.

### M4 Destroy the Intellect Factory (overview, ev-01, ev-02, design-notes). Report 04 §1, overridden by decisions 1, 4, 8
- **Shape:** an objective layer for **Xanathar's Lair** (unconverted). Use the arc-f codes only:
  - X23 Competitive Intelligence Files;
  - X24 The Infiltration (the placement records: four Watch and civic hosts, two pending, with Orvyn Dall among them);
  - X25 The Experiments, where **the Spawning Pool** now sits beside the twelve specimens. Zaibon (or Soluun per decision 4) is strapped here, waiting to be implanted;
  - X26 The Puppet, where Nihiloor waits.
  - Don't use the Appendix C codes (X2 zombie, "Food for Thought").
- **ev-01 The Brief**
  - Fires when a member with **M3 Complete** prepares for the lair.
  - Vajra's *Sending*, then the Tower: what she knows of the pool (not how she knows), potions, and the commendation she will write.
  - If **Meloon Restored**, Meloon gives his long-dream memory of the route.
  - Read **Nihiloor Identified Party** (he is waiting for them) and **Devourer Escaped**.
  - **Variant "If Xanathar's Lair Has Already Run":** a short debrief at the Tower. The GM marks the M4 outcomes from what the party did in X23–X26, and renown is awarded if they entered the wing.
- **ev-02 Nihiloor's Wing**
  - A self-contained block the GM opens when the party reaches X23–X26 during the lair heist.
  - The pool and three ways to end it, each with a clock.
  - The records.
  - The captive.
  - Nihiloor and his pet Occupying Devourer: flee-first tactics, escape threshold from the mechanics reference, retreat toward X4.
  - The Puppet device in X26 belongs to the lair quest. Mention it in GM text only and don't resolve it here.
  - **Debrief at the Tower:** Vajra's written commendation, no rank.
  - **Renown:** 3 base. +1 pool destroyed with every spawn dead. +1 captive out alive. +1 placement records delivered.

### M5 The Legate's Eyes (overview, ev-01 rewritten, ev-02 new, design-notes). Report 04 §2
- **Two events:**
  - **ev-01 The Reversed Rulings:** Vajra's dossier, three leads to Orvyn Dall, and the detection layer from §5. The three leads are the Hall of Records rulings, surveillance at lunch, and the **Placement Records Taken** list. If that outcome is unmarked, use Corene's debrief clerk line instead.
  - **ev-02 The Extraction:** moving Orvyn, the hosted clerk (Commoner host), forcing it out, then extract, kill or leave in place. Reuse the Harper M5 ev-02 extraction box, and cap Strain at 2. Then the neighbour, Vajra's debrief, and the Jalester option.
- **Courier:** Orvyn's devourer reports through a Guild courier, never "self-sustaining".
- **The Watch-review consequence** must be defined in one bullet procedure.
- If **Pool Destroyed** is marked, no new hosts arrive.
- **Renown:** 4 base. +1 Orvyn extracted with no Watch review. +1 ledger delivered.

### M6 Smoke in the Tower (overview, ev-01, ev-02 new, design-notes). Report 04 §3, decision 2
- **ev-01 The Wrong Shelf**
  - The door attendant (the deliberate break), forty-three names, the resonance and the disruptor, the behavioural audit, the seal.
  - **Vira Solkan** in voice, with her three options.
  - Vira uses the **Mage Apprentice** block and runs rather than fights.
  - She signals by sending stone, never *Message*.
  - ev-01 marks nothing and chains to **The Breach**. Whether Vira was taken in ev-01 carries forward as scene state.
- **ev-02 The Breach**
  - The signal, the north service door, the prisoner, and Vajra and the Open Lord (a reading, not a meeting).
  - Marks all of M6's outcomes, including **Vira Caught** (taken in either event) or **Vira Escaped**.
  - Rebuild the roster per party size from the mechanics reference.
  - Define the Tower's wards as a hard rule.
  - Branch on the Kolat Towers Manshoon result for who sent the team, as DR M6 ev-01:18-24 does.
  - Vajra swears here.
- **Story reward:** recognition from the Open Lord. No rank.
- **Renown:** 4 base. +1 disruptor removed before it fired. +1 testimony recorded.

### s01 The Full Picture (ev-01, design-notes). Report 02 §2b, §5b, §6b
- **Members only.** Cut the vouched non-member route.
- **The full-picture test** is a GM table with three routes per element.
- **The three confirmations:**
  1. Nihiloor's programme (cite **Nihiloor Fled** / **Pool Destroyed** if marked).
  2. A larger cell behind the Splinter, named only if **Manshoon Named**.
  3. Residue under the Cassalanter villa, suspicion only. Use it only if the Cassalanter quest hook has run; otherwise use Hlam's buried thing.
- **The staff stirring:** DC 13 Wisdom (Perception), narration only. Vajra doesn't look.
- **The sealed message** goes to "the Open Lord".
- **Renown:** +2 to each member present, once in the campaign. Write **Vajra Briefed**.

### r03 / r10 / r25 / r50 (ev-01 + design-notes each). Report 02 §2c–f, §5c–d, §6b–d, §8
- **Model:** DR r03 and Harper r03/r50.
  - A `What Is Actually True` block.
  - A per-member hook.
  - `### Naming the Rank`.
  - One `###` per benefit as a procedure: contact, place, notice, limit, who else, loss rule.
  - "The rank event awards no Renown."
- **r03 Junior Griffon:** the preparatory spell (fixed list, 2 days' notice, once per tenday); the library (one question per visit, using the Harper archive method); Merris (cap per tenday, Common potions only, two vials of holy water).
  - Read **Offerings Kept**: Meritide's grudge, one line.
- **r10 Senior Griffon:** the wand of secrets (credited to M3, and only if the party has none); **Ysmay Halvane** (Mage ally, Ally Power from the mechanics reference, once per quest, 3 days' notice); written authorization.
  - Read **Meloon Restored** / **Meloon Lost** for one line.
- **r25 Force Grey:** the Underclock badge; the charge suspension (once per member, one case); **Rhendar Orsk** (Warrior Veteran ally); the 7th-level spell (fixed list, cast on the surface).
- **r50 Force Grey Commander:** the Mad Mage set-piece.
  - Hold until the member is on the surface.
  - Primary post-Vault text, with a pre-Vault branch read from **Vajra Briefed**.
  - The team: Ysmay, Rhendar and two named others, sized by the mechanics reference.
  - The scroll list: 4th–5th level, no transport spells.
  - The final reserve: any wizard spell except *wish*, cast on the surface or at the Yawning Portal.
  - **The Open Lord:** in voice, no swearing, no hint of her decline. Don't duplicate the Lords' Alliance r50 private request.
  - **Public / Sealed** recognition per member.
  - Mad Mage seeds as one-line GM facts.

## Companion pages (main session, after the folders merge)

- `campaign/guides/factions/06-force-grey.md`: gates, ranks, the Manshoon lines, M4 as a lair objective, rank benefits per member.
- `campaign/setting/organizations/05-force-grey.md`.
- Notable Figures pages:
  - Vajra: species, alignment and tenure; her Manshoon quote moves behind the gate.
  - Meloon and Nihiloor: "ate his brain" becomes occupation.
  - Zelifarn: Young Bronze Dragon.
- `campaign/structure/arc-f-xanathars-lair.md:432`: the M4 objective layer and its outcomes.
- Everything else goes to the out-of-scope log.
