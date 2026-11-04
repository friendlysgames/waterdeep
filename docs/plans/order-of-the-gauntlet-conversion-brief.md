# Order of the Gauntlet Conversion Brief (Session 45)

## Context

The user asked for the Order of the Gauntlet events (the last faction) to be rewritten the way the Harpers (S41), Force Grey (S42), Emerald Enclave (S43) and Lords' Alliance (S44) were: research, plan, then draft on the DR/BD/Harper/FG/EE/LA page model.

**Inputs**
- **Rewrite input (R).** The first-commit version of every file, restored in place in `campaign/quests/faction-events/order-of-the-gauntlet/` (PR #157). A read-only copy is at `/tmp/claude-0/-home-user-waterdeep/19a91aac-b9d5-5e3a-b464-72b606906164/scratchpad/ootg-orig/order-of-the-gauntlet/`.
- **Previous version (PREV), fact source only.** `/tmp/claude-0/-home-user-waterdeep/19a91aac-b9d5-5e3a-b464-72b606906164/scratchpad/ootg-prev/order-of-the-gauntlet/`. It is R plus a half-finished retrofit. Don't copy its structure or prose.
- **Approved plan:** `docs/plans/order-of-the-gauntlet-plan.md`.
- **Research reports** in `docs/plans/order-of-the-gauntlet-research/`:

  | File | Covers |
  |---|---|
  | `01-spec-and-structure.md` | Page model, inventory, skeletons and lengths (§6.2), gates (§6.3), outcomes (§6.4), contact (§6.5), rank shapes (§6.6) |
  | `02-first-meeting-s01-s02-ranks.md` | 00, s01, s02, r03–r50 (§4, §5, §6, §7, §8, §12) |
  | `03-m01-m03.md` | M1–M3 (§3, §6, §7) |
  | `04-m04-m06.md` | M4–M6 (§4–§7) |
  | `05-consistency-audit.md` | Outcome map, outside references, collisions |

Where a report lists options, this brief has already chosen. Where a report and this brief disagree, this brief wins.

## What went wrong with R and PREV (avoid all of it)

- **Format:** `[GM]`, True/False flags, `Milestone` lines, `## Read Aloud`, "Arc X" labels, no Brief built from `[!social]` and `[!qna]`, no Who Knows What, no Event Outcomes, no debrief scene, party-level renown with no base and two or three +1 lines.
- **Gates** run R0/2/4/7/10/14 against the ladder 1/3/5/8/10/13.
- **Contact:** M2 sends a paper bird, but the organization page says Savra comes in person.
- **Rules:** "Thug", "Cult Fanatic", Spined Devil *Hurl Spine*, Bearded Devil grapple and "Cursed", Horned Devil *Battle Frenzy*, Priest *Banishment*, the 2014 wererat silver rule, *Command* as a confession tool, *Charm Person* with a fixed DC, a held imp "stripped of invisibility", *Resurrection* as a 5th-level spell, Ring of Protection and Bracers of Defense as Uncommon, "week" for tenday.
- **Cassalanter secrecy:** M2 calls a captured imp "Cassalanter devil-binding" and has Seffia say the Cassalanters know who the Black Viper is. M5 reveals the soul-bargain, twelve acts, the Reckoning and a Founders' Day deadline, and moves Flamerule 1 by four days. M6 has Savra name Victoro's "contractual counterpart" in read-aloud.
- **Manshoon** is ungated in M1 (Savra's "Manshoon file" at Renown 1).
- **Dead hooks:** "What are they moving?" has no payoff; Seffia is a tea-house socialite but her page makes her a windmill recluse; the forged birth year 1470 cannot be Ammalia's twin.
- **Timeline errors:** Savra's cult tenure (3 years in the First Meeting, 4 in s02); r50 has her award Righteous Hand "four years ago", before she left the cult; the First Meeting calls her "the only Order member in Waterdeep" while r25 and r50 field a chapter and a council; the Halls of Justice sits in three wards.
- **Collisions:** "Tobrin" (armory cleric) with Tobrin Ashvale, the Xanathar bartender.

## User decisions (Session 45)

1. **Valdra stays unofficial** and appears in none of the seven events. Reassignment (s01) runs through a named Order clerk. The r50 investiture is by the high priest of Tyr.
2. **M2 uses an alias and a raven imp.** The tea-house contact is a household secretary under an invented alias; windmill Seffia Naelryke stays for Faction Outposts and is not in M2. The watcher is an imp in raven form (arc-g:89) with its sender unproven. "What are they moving?" is paid off in M4 (see M4).
3. **M6 enforcer:** the Horned Devil, with Savra fighting beside the party as a Knight ally. Enemies never focus a single PC, so no first-turn-KO (+4 CR) adjustment applies to any Order fight.
4. **M5 shrine:** the hybrid (default, not overruled). The Field Ward chandler's cellar is the street entrance to the canonical Aveen Street shrine (arc-e 6A). M4 and M5 together are a fifth independent path to it.

## Standing defaults

**Secrets**
- **Manshoon.** Use the **Manshoon Named** gate (written by Faction Outposts, unconverted). Until it is marked for a member, Savra and every other speaker say "the Splinter" or "the other cell". Overview, Involved Characters and Summary labels say "the Splinter". GM text may state the truth. M6 uses the gate too.
- **Cassalanters.** Suspicion only; nobody knows they are infernalists. The one discovery beat is M4 (Gysheer, compelled, names Victoro and an address) and M5 (the party finds a devil shrine and a ledger in Victoro's hand). Even there, a speaker may say "devil worship" about what the party has just seen, but never states the pact, its terms, the twelve acts, the Reckoning, a deadline or "the Asmodean bargain". Those stay for Cassalanter Villa. Elsewhere use "a household errand" or "the family".
- **Jarlaxle.** No Order speaker names Jarlaxle, Zardoz Zord or Bregan D'aerthe to players before **Jarlaxle Unmasked**. Say "the carnival fleet".
- **Two Zhentarims.** Davil's Doom Raiders and the Splinter are different. Savra distinguishes them.
- **Illuun.** Not named by any speaker.

**Savra Belabranta**
- **Stat line:** Lawful Good, Human, she/her. Knight block (XMM) when she fights. Late twenties, dark hair worn back, strong jaw, dark riding coat, silver gauntlet pin. Left-slanting hand.
- **Voice** (`voices/order-of-the-gauntlet.md`): stingy, plain, clipped swearing; "I'll tell you plainly"; a single measured nod given only to honest answers; calls Tyr "the Maimed God".
- **Facts fixed once, used everywhere:** she was in the Howling Hatred cult for **three years** and left it about **three years ago**, when two of its members were quietly released by the Watch. She joined the Order after leaving. s02's "four years" becomes three. She has never held Righteous Hand (r50 names a prior holder, a senior Knight of the Waterdeep chapter who has since died, and drops "four years ago").
- **The chapter.** Define once in the First Meeting's What Is Actually True and keep: the Waterdeep chapter is Savra, a clerk's office at the Halls of Justice, a rotation of about a dozen Knights and Priests who answer to her, and the priests of the Triad who help without being members. "The only Order member in Waterdeep" is deleted.
- **Halls of Justice:** one location. Use the guide and the structure docs to fix its ward; the drafter states which ward and logs the choice.
- **Valdra** is not used.

**Contact object: Savra in person**
- Savra knocks once at Trollskull Manor and waits to be asked in (M1, M2, M3, M4 and the First Meeting).
- **Written exceptions** are a note in Savra's left-slanting hand on paper with the Halls of Justice seal, folded once, carried by a **Priest Acolyte** in a plain grey surcoat to the named member only. The drop is the door-warden at the Halls of Justice, who holds messages "for Savra Belabranta". Used for: the First Meeting when nobody is home (left with Tally Fellbranch), M5 (the Brief moves to the Halls), M6 and the rank summons.
- Notes are one short paragraph, signed "S.B." No word cap applies.
- Rank events: the morning after the threshold, an acolyte brings the note at noon; the meeting is at the Halls of Justice east annex at the third bell past noon. A member away from Waterdeep gets it at the first surface lodging.

**Membership**
- **Candidates.** Every character in no other faction is a candidate and answers for themselves. Savra addresses first the character with a Cleric or Paladin class or an Acolyte, Guard or Soldier background, then a worshipper of Helm, Torm or Tyr, then the highest Wisdom, then alphabetical. Nobody is tested at the door. A character already in another faction gets no offer, and Savra says so in one qna answer.
- **No Offer Closed outcome.** The Order wants recruits. A declined offer stays open: a later acceptance is recorded under **Order of the Gauntlet Joined** with the name. A character who becomes unaffiliated later meets Savra at the Halls within a tenday.
- **Eligibility** in Trollskull ev-04 no longer says paladins and clerics; the companion pass fixes it.
- **Members only.** Briefs, debriefs, renown, ranks and benefits belong to individual Order members. Companions help with everything except Savra's brief and debrief, and earn no renown. Every gate reads "becomes available when an individual Order of the Gauntlet member reaches Renown N and Nth level".
- **Party-wide gifts are deliberate and said in GM text:** the renovation help (First Meeting), and the Order Recognized notice (M6) naming every character present.
- **No suspension or dismissal.** Only the Lords' Alliance suspends (WDH). The Order's analogue is **Quietly Reassigned**, a list, not a punishment (s01).

**Rules**
- **2024 rules and names only:** Tough, Tough Boss, Bandit, Bandit Captain, Guard, Knight, Priest, Priest Acolyte, Scout, Spy, Cultist Fanatic, Imp, Spined Devil, Bearded Devil, Horned Devil, Wererat, Giant Rat. Every roster and stat comes from `docs/plans/order-of-the-gauntlet-mechanics-reference.md`. Don't invent CR math or stat values.
- Checks read "**DC N Ability (Skill)**" with a stated fallback. No single check settles a mission. Investigations give three independent leads.
- Fights go in `[!hazard]` with `#### X's Tactics`, an end or retreat condition and a non-combat route. Enemies spread their attacks.
- **Calendar.** Campaign year 1492 DR. Spans in days or tendays. Founders' Day (Flamerule 1) never moves.
- *Resurrection* is 7th level with a diamond worth 1,000 gp or more. *Speak with Dead* is 3rd level. No *Wish*.

**Renames and fixes**

| Old | New |
|---|---|
| Tobrin (armory cleric) | an invented lay brother with a unique name (collision check in notes) |
| Seffia in M2 | an invented household secretary alias (collision check in notes) |
| "Cult Fanatic" | Cultist Fanatic |
| "week" | tenday |
| Forged birth year 1470 | 1452 DR, with no child count |
| Diabolism Confirmed | **Cassalanter Register Filed** |
| Devil Destroyed | **Devil Sent Back** (a Horned Devil returns to the Nine Hells) |

## Gates and renown (shared ladder)

| Mission | Gate | Base | `+1` bonuses (each once, tied to a named condition) |
|---|---|---|---|
| M1 | joining (Renown 1), 2nd level | 2 | the brawl ends with no death; a traceable detail of the intermediary reaches Savra (**Splinter Intel Reported**); Pell leaves the square unhurt with his face (**Pell's Debt Held**) |
| M2 | Renown 3, 3rd level | 2 | the planted story confirmed fabricated and reported (**Planted Story Exposed**); the forged record recovered or the secretary named with her contact method (**Forged Record Secured**); the raven imp caught alive (**Imp Captured**) |
| M3 | Renown 5, 4th level | 3 | the harassment ends with nobody dead; mediation succeeds (**Mediation Path Taken**); Danika paid and Darrick named to the Watch |
| M4 | Renown 8, 5th level | 3 | all three residents unharmed; the shrine address recovered without compulsion; Gysheer's documents delivered in full (**Intelligence Shared**) |
| M5 | Renown 10, 6th level | 4 | the Bearded Devil destroyed with no one at 0 hit points; the ledger delivered within 24 hours (**Ledger Recovered**); Orros kept out of it |
| M6 | Renown 13, 7th level, after **Kolat Towers** | 4 | the Horned Devil sent back before it reaches the cabinet; every named character survives; the party, not Savra, lands the final blow (**Devil Sent Back**) |

The base-only path reaches every gate: 1 → 3 → 5 → 8 → 11 → 15 → 19. r03 fires after M1, r10 at the M4 debrief (base-only), r25 after M5 with bonuses. No mission grants rank. The standing Earning Renown actions pay once; the mission bonus lists above omit the +2 evidence and the per-devil +1 so nothing is counted twice.

## Event Outcomes (one writer each; mark per member where individual)

| Outcome | Writer | Readers |
|---|---|---|
| **Order of the Gauntlet Joined** (per name) | 00 | every Order event; Factions Guide; BD s04; Trollskull ev-04 |
| **Splinter Intel Reported** | M1 | Faction Outposts (unconverted) |
| **Pell's Debt Held** | M1 | M3 (Kelso's gang is on Pell's unpaid list); Faction Outposts (unconverted) |
| **Planted Story Exposed** | M2 ev-02 | M4 ev-01 (the Cassalanter handlers' lookouts are fewer) |
| **Forged Record Secured** | M2 ev-02 | Cassalanter Villa (unconverted, if not run) |
| **Imp Captured** | M2 ev-02 | M4 ev-02 (Savra's debrief); r10 predicate; Cassalanter Villa (unconverted, if not run) |
| **Black Viper Source Noted** | BD m02 (read only) | M2 ev-01 (Advantage on layer one of Gaxly) |
| **Mediation Path Taken** | M3 | Doom Raiders M3 (exact name, Kelso's greeting) |
| **Kelso's Debt** / **Kelso's Debt Spent** | M3 | M4 or M5, once, Kelso's choice of: a Field Ward location, a distraction, or silence; Doom Raiders M3 (cancelled if the party gave up Dasher) |
| **Shrine Address Recovered** | M4 ev-02 | M5 Brief |
| **Intelligence Shared** | M4 ev-02 | M5; r10 (Savra's file) |
| **Ledger Recovered** | M5 | M6; r10; r25 (the inquiry's predicate); Vault of Dragons (unconverted). Protected name. |
| **Shrine Destroyed** | M5 | Cassalanter Villa (unconverted, if not run) |
| **Cassalanter Register Filed** | M5 | r25 predicate; Vault of Dragons (unconverted); M6 table |
| **Cassalanters Alerted** | M5 | M6; Cassalanter Villa (unconverted): one escalation tier toward the party |
| **Order Recognized** | M6 | Vault of Dragons (unconverted; "if not run" default); r50 |
| **Devil Sent Back** | M6 | M6 table; r50 |
| **Tithe Paid** / **Tithe Paid After Asking** / **Quietly Reassigned** (per member) | s01 | every Order brief; r03, r10 (the extras); Vault of Dragons (unconverted) |
| **Savra's Past Known** / **Cult Funding Linked** (per member) | s02 | r50; Cassalanter Villa and Vault of Dragons (unconverted) |
| **Marcheon Reached**, **Whitehawk Reached**, **Vindicator Reached**, **Righteous Hand Reached** (per member) | r03 / r10 / r25 / r50 | the next rank; Dungeon of the Mad Mage |
| **Undermountain Mandate Accepted** (per member) | r50 | Dungeon of the Mad Mage |

**Read, not written, by this folder:** **Manshoon Named** (Faction Outposts), **Jarlaxle Unmasked**, **Kolat Towers** completion, the Cassalanter Villa result (one of Contract Destroyed, Cooperative/Gold Payment, Sacrifice Happened, Cassalanters Exposed; "if not run" default Cassalanters Exposed).

Dropped: outcomes whose only reader is the renown total (Court Cleared, Guardian Destroyed, All Named Survived, Party Led, Brawl Ended Without Deaths, the four Seffia states).

## Per-folder briefs

### 00 First Meeting (ev-01 "Order of the Gauntlet First Meeting", design-notes). Report 02 §4

- **Scenes:** The Knock (placement and the contact object); The Pitch (Savra social + 6 qna: why us, what does the Order do, what does it cost, the family she won't name, the beholder, can we keep other loyalties; a GM block for the Stone, the vault and Manshoon); The Darker Exchange (the cult question; the "ask sincerely" rule; three years in the cult); Each Candidate's Answer (the oath's three questions; accept, decline, ask for time readalouds; the **Chevall Benefits** block per member); The Oath (a separate scene at the Halls of Justice, open any day; the silver gauntlet; the priest of Tyr seals it; the three commitments: find evil, pursue it, destroy it; protect those who cannot protect themselves; stand when standing is required); The Guild Hall (party-level renovation help, once: Savra walks the party to one Guild hall in Order insignia and the permit queue closes in a day; 100 gp off the renovation total once, matching Trollskull ev-04; plus a passive line that a Watch patrol answers a disturbance at the manor within the hour); Leaving (M1 is briefed at the manor the next morning, in the Next Steps).
- **Chevall Benefits** (per member, companions nothing): vouches to any temple of Tyr, Helm or Torm in Waterdeep; free healing, one *Cure Wounds* a day per temple, and a bed; in trouble with the law, Savra puts in a good word and tends the member's affairs; the faction channel for *Speak with Dead* at Renown 1 or higher (Fireball ev-01:88). Each as a procedure with temple, front-desk contact (the door-warden), limit and loss rule.
- **What Is Actually True:** Savra chose these candidates from what Renaer and the Floon rescue told her; the family she won't name is the Cassalanters (she suspects, she cannot prove, she doesn't say what they worship); the Howling Hatred is real; the chapter as defined above; WDH's "non-evil" appears here as a line, not a test.
- Cut "the only Order member in Waterdeep" and R's second approach.

### M1 Breaking Up the Brawl (overview, ev-01, design-notes). Report 03 §3 (M1)

- Savra at the door. Brief as social + 5 qna ("no fighter" rule). Deadline stated.
- **Three beats:** the Field Ward at noon (the crowd as exploration), the standoff (three DC 12 Intimidation before three failures; Dex DC 12 to signal Pell), the fight (Toughs and Bandits, mechanics reference rosters at 3/4/5 PCs; Bloody). A non-combat route disperses the crowd.
- **Three independent clue routes** to the intermediary's description.
- Savra says "the Splinter file", never "Manshoon". Pell is Xanathar Guild and no fighter.
- Debrief with Savra. Writes **Splinter Intel Reported**, **Pell's Debt Held**.

### M2 The Black Viper Investigation (overview, ev-01, ev-02 "The Imp at Dawn" kept or renamed "The Raven on the Chimney", design-notes). Report 03 §3 (M2)

- **ev-01:** Savra at the door at an hour that suits her ("I am at the Halls of Justice all day. Go to the Wazoo."). Gaxly (Neutral; layers; Advantage if **Black Viper Source Noted**). Two tracks (Ilmeth Waevlur; the red candle and the Steaming Anchor). The household secretary under her alias: social + 4 qna; four options as exploration blocks. Replace the *Charm Person* line with a lawful route. Writes nothing.
- **ev-02:** the watch on Trollskull Alley two days later, a night clock; the watcher is a **raven that is an imp** (arc-g:89), its sender unproven and its marks identify nothing; the catch rules; Savra's debrief asks "What are they moving?" and answers it in M4. A day table fixes the timeline. Forged record: born 1452 DR, no child count. Mission Renown here. Writes **Planted Story Exposed**, **Forged Record Secured**, **Imp Captured**.
- "Cassalanters know who the real Black Viper is" is cut. The household does not know Esvele is the Viper (arc-g). Nothing in M2 names the Cassalanters except as a suspicion Savra lets the party raise.

### M3 The Shard Shunners (overview, ev-01, design-notes). Report 03 §3 (M3)

- Keep the title and **Mediation Path Taken** exactly. Savra at the door. The Endshift Tavern (Trevar). Kelso Fiddlewick: social + 5 qna; Danika is fourteen. **Mediation as a three-term balance** (Danika's care, Darrick named, Trevar's amends). The 2024 Wererat has no silver rule and no Regeneration. Rosters from the mechanics reference (Bruising). Kelso is not a Splinter agent; the Splinter is only his customer in GM text. **Kelso's Debt** gets a defined spend (above). Writes **Mediation Path Taken**, **Kelso's Debt**. Reads **Pell's Debt Held**.

### M4 Spined Devils in Twelvedog Court (overview, ev-01 "Twelvedog Court", ev-02 "What Gysheer Carried", design-notes). Report 04 §4

- **ev-01:** Savra at the door "already moving". The noon fight in Twelvedog Court: Spined Devils on the rooflines, three residents pinned behind a cart, Savra beside the party as a Knight ally. Gysheer Omfreys (Cultist Fanatic) arrives with a knife and attacks, as WDH has it. Roster per party size from the mechanics reference. Ends with Gysheer down or fled. Writes nothing. Reads **Planted Story Exposed**.
- **ev-02:** Gysheer (social + qna): compelled by a lawful route, she names Victoro Cassalanter and "the shrine on Aveen Street". **Three independent paths** to the address: her compelled answers, her belongings (a note sealed "V.C." and a **cartage receipt for crates delivered to Aveen Street**, which pays off "What are they moving?"), and the Crispin Street room above the dyer's shop. Savra's constraint (a legal reason she cannot go in alone and what she asks). Debrief. Writes **Shrine Address Recovered**, **Intelligence Shared**. Reads **Imp Captured**.
- Cut "We have the grounds now". Suspicion only; Savra names no pact.

### M5 The Shrine on Aveen Street (overview, ev-01, design-notes). Report 04 §5

- **Contact break:** a Halls of Justice note summons the party to the Halls (the Brief). Reads **Shrine Address Recovered**.
- Aveen Street: the chandler's shop in the Field Ward, the cellar door, three ways in. The cellar is the street entrance to the canonical Aveen Street shrine (arc-e 6A). Orros (social + 2 qna). The shrine: a trimmed two-room roster (Bearded Devil, Cultist Fanatics, an Imp) from the mechanics reference, with a non-combat route.
- **The ledger:** twelve dated entries in Victoro's hand (names, places, a final date written as a date). The Arcana check recognizes a bargain in writing and no more. No terms, no deadline, no "Reckoning", no Masked Lord. Three ways to read it. Savra files a petition she can file on a legal predicate, and a Watch clerk tells the Cassalanters: **Cassalanters Alerted** (one escalation tier toward the party). Founders' Day does not move.
- **The Siamorphe holy symbol** that arc-g and the villa location pages expect from Savra is given at the end of M5 by her chaplain, so the villa reads it "if not run" cleanly.
- Split into two events (the Hall and the Door; the Cellar) only if the draft passes 480 lines.
- Writes **Ledger Recovered**, **Shrine Destroyed**, **Cassalanter Register Filed**, **Cassalanters Alerted**.
- Date references are relative ("ten days ago") or 1480s DR; Copper Street is not used.

### M6 The Writ and the Weight (overview, ev-01, design-notes). Report 04 §6

- **Contact break:** the vellum summons from the Halls. Gate: Renown 13, 7th level, after **Kolat Towers**. Reads **Ledger Recovered** or **Cassalanter Register Filed**.
- The rider arrives on the night of the Lords' hearing, at the Halls of Justice (Savra's seat). Savra is present by design and fights as a Knight ally.
- A four-row table keyed to the Cassalanter Villa result (Contract Destroyed, Cooperative/Gold Payment, Sacrifice Happened, Cassalanters Exposed; "if not run" default Cassalanters Exposed) says what the writ names and what the devil serves. No speaker says "contractual counterpart" or "infernal rider".
- A Horned Devil with escorts from the mechanics reference. State the High-Power Warning in the hazard block. Two Priests of Tyr stabilize Savra if she falls. *Banishment* is not the plan; a scroll or a PC's action is the option, and the success chance is stated.
- The devil is **sent back** (Diabolical Restoration), not destroyed.
- Writes **Order Recognized** (a party gift naming every character present), **Devil Sent Back**. No combat-free route is required, but a way to bring the hall's wards to bear shortens the fight.

### s01 The Tithe (ev-01, design-notes). Report 02 §6

- **Trigger:** per member, when the party carries a haul of 1,000 gp or more (coin, trade goods, gems at face value; magic items excluded) out of one operation for the first time after the member took the oath. Name the Gralhund coach house (2,000 gp).
- The member owes **25% of their own equal share**; non-members owe nothing. Savra knocks at dusk on the second day after the haul reaches Waterdeep. **Before the knock:** receipt, recipient, payment, **+1 Renown once**, **Tithe Paid**. **After she asks:** no Renown, "Good.", **Tithe Paid After Asking**. **Refusal or under 25%:** **Quietly Reassigned**.
- Worthy causes as a fixed table (R :24-32 minus Trollskull). The Order's clerk, not Savra, takes the receipt.
- **Quietly Reassigned** is a list: Savra stops offering the optional extras (Marcheon accompaniment unless asked, temple briefings' extras, r10 surveillance offers); missions still arrive by a clerk's note; she fights coldly and says only "This isn't about you." Remedy: pay the declined 25% to a worthy cause. Ends the next morning. Costs no Renown.
- Awards no base Renown (the +1 is the tithe line).

### s02 Savra's Past (ev-01, design-notes). Report 02 §7

- **Trigger A:** a member at Renown 3 or higher who has seen Savra fight beside them at least once (M4 or a Marcheon operation). She walks the member to the Halls of Justice east annex at dusk. **Trigger B:** the first time a member tells Savra that Cassalanter money lay behind the Howling Hatred, as a suspicion; she does not confirm it. Two routes fire it so a non-Harper party can reach it: Mirt's intel (Fireball ev-01:194), or Saeth Cromley's account of the two cultists the Watch released three years ago.
- The Howling Hatred background (lore, not read aloud; rank names unverified, flag them); What She Did; The Cult's Money; **The Ask** with a fixed answer table (hold it, it changes nothing, I don't know accepted; evasion rejected; the nod rule).
- No Renown. Writes **Savra's Past Known**, **Cult Funding Linked** (Trigger B only).

### r03 Marcheon, r10 Whitehawk, r25 Vindicator, r50 Righteous Hand (ev-01 + design-notes each). Report 02 §5, §8; report 01 §6.6

Every rank event: "The rank event awards no Renown"; a per-member tracking line; a Next Steps naming the next threshold; the contact object above; companions get nothing; the rank stays if Renown drops but the benefits pause.

- **r03 Marcheon:** (1) **Savra at your side**, one operation per quest, a Knight ally from the mechanics reference (a safety net at levels 2 and 3, counted in full from level 4); she refuses an operation she thinks will get the party killed; she withdraws at 20 HP. (2) **The Armory** at the east annex, one mundane weapon or armor per tenday, returned serviceable, kept by an invented lay brother (not Tobrin). (3) **Temple briefings**, one per tenday from one of three named temples (Halls of Justice, the Temple of Helm in the Castle Ward, a Torm temple with an invented name), patterns not names, nothing that names the Cassalanters or a pact. Drop the "M2 unlocks at third level" line; the ladder gates it.
- **r10 Whitehawk:** (1) **Surveillance**, one named suspect or location per quest, two Scouts, three days, a written report; no named Cassalanter family member before Cassalanter Villa has run. (2) **Potions**, one *Potion of Healing* and one *Potion of Greater Healing* before a quest's main operation. (3) **One Uncommon item** from a fixed table rebuilt from `items.json` (Sentinel Shield, Cloak of Protection, Brooch of Shielding, Periapt of Wound Closure; not Ring of Protection or Bracers of Defense). (4) **Temple spellcasting** of 2nd level or lower from the verified list, components under 100 gp covered. (5) **The Cassalanter dossier** (R :17-25) as a party document; Savra says "the family" unless the party gave her the name; the villa layout is a casing aid for Cassalanter Villa "if not run". (6) **Savra at the lairs:** a short table of what she does at Xanathar's Lair, Cassalanter Villa, Kolat Towers and the Vault at Renown 10 or higher (extraction backup, the potions, the Siamorphe holy symbol if the party holds evidence from Faction Outposts).
- **r25 Vindicator:** (1) **The Investigation**, one target at a time; the predicate is a written exhibit a magistrate would read (the M5 ledger or a party-delivered document), not the r10 dossier; a fixed findings table for six targets (Victoro Cassalanter, Xanathar's Guild, the Splinter's Trade Ward safe house, Gysheer Omfreys, the M2 secretary, a named independent), a written result in two tendays. Savra files "diabolism" only after the party has found devil evidence. (2) **The Strike Team:** three Knights (invented names) for one operation per quest, with the ally Power rules from the mechanics reference. (3) **The +1 weapon** from a fixed table (verify the generic +1 rarity against the data; flag if absent). (4) **The ledger of dead Vindicators**, fixed text. Two named witnesses.
- **r50 Righteous Hand:** holds until the member is on the surface; a written summons cannot reach Undermountain. The acolyte finds the member at the first surface lodging; the investiture is three days later. (1) **The Mobilization:** six Knights and two Priests, one major operation per quest, three days' notice, ally Power from the mechanics reference. (2) **The Resurrection pledge:** *Resurrection* (7th level, 1,000 gp diamond), once, cast by the high priest of Tyr (13th level or higher, non-combatant, invented name); the body must be carried up by stairs. (3) **Knighthood** as a written credential with a defined effect. (4) **The Undermountain Mandate:** accept or decline; one aid call per Undermountain level, answered by the next Order courier; writes **Undermountain Mandate Accepted**. (5) **Mad Mage seeds** (one line each): level 15 Fidelio (a paladin of Tyr ghost, Persuasion DC 20), level 21 Fazrian (a corrupted planetar of Torm), level 22 the Shadowdusk former Torm paladins, level 23 Aryx (a deva sent by Tyr). The WDMM has no Order of the Gauntlet; Savra's white gauntlet is Torm's. Cut the Vault branch. Writes **Righteous Hand Reached**.

## Companion pages (main session, after the folders merge)

- **Factions Guide** `05-order-of-the-gauntlet.md`: gates, base renown, the contact, the First Meeting, the M4/M5/M6 rows (suspicion-grade; remove "Lord Victoro's infernal contract triggered a contractual enforcement rider" at :70-71), Savra's stance line that says "Manshoon", the rank procedures, the tithe and Quietly Reassigned rules.
- **Organization page** `04-order-of-the-gauntlet.md`; **Notable Figures** for Savra (Featured in, tenure facts) and Valdra (unchanged; she appears in no event); Kelso's, Seffia's (M2 listing removed) and Victoro's Featured-in lines; **Savra's voice entry**.
- **Rank rows** in `players-guide/faction-affiliations.md` and `gm-guide/player-factions-overview.md`; **Trollskull** `ev-04` (eligibility, renovation row, the duplicate Joined writer and True/False heading) and the manor guide (`02-operating-costs.md:83`, `03-staff-and-hiring.md:77`).
- **Out-of-scope log:** a new section in `harpers-out-of-scope-notes.md`, and the stale Kelso line deleted from it (`:762`) and from `emerald-enclave/m03-the-doppelganger-problem/design-notes.md:28`.
