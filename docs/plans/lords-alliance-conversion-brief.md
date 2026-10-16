# Lords' Alliance Conversion Brief (Session 44)

## Context

The user asked for the Lords' Alliance events to be rewritten the way the Harpers (S41), Force Grey (S42) and Emerald Enclave (S43) were: research, plan, then draft on the DR/BD/Harper/FG/EE page model.

**Inputs**
- **Rewrite input (R).** The first-commit version of every file, at `/tmp/claude-0/-home-user-waterdeep/f91bf122-6992-582e-a45c-3f8e22918b72/scratchpad/la-orig/lords-alliance/`.
- **Previous version (PREV), fact source only.** The current files in `campaign/quests/faction-events/lords-alliance/`. PREV is R plus retired sidebars and a few fixes. You overwrite these files. Don't copy their structure or prose.
- **Approved plan:** `docs/plans/lords-alliance-plan.md`.
- **Research reports** in `docs/plans/lords-alliance-research/`:

  | File | Covers |
  |---|---|
  | `01-spec-and-structure.md` | Page model, R/PREV inventory, skeletons and lengths (§1, §6.2), the contact object (§6.5), rank shapes (§6.6) |
  | `02-first-meeting-s01-s02-ranks.md` | 00, s01, s02, r03–r50 (§3b, §4, §5, §7, §9, §12) |
  | `03-m01-m03.md` | M1–M3 (§1, §3.2–§3.4, §4) |
  | `04-m04-m06.md` | M4–M6 (§3.4, §4–§6, §7 stat values) |
  | `05-consistency-audit.md` | Outcome map, outside references, collisions, cross-faction conflicts |

Where a report lists options, this brief has already chosen. Where a report and this brief disagree, this brief wins.

## What went wrong with R and PREV (avoid all of it)

**Format**
- Retired formats everywhere: `[GM]`, `[!narrative]`, `[!dialogue]`, `[!npc-narrative]`, True/False flags, `Milestone: None`, `Milestone Overview`, `## Read Aloud`, "Act N" scene labels and "Arc X" labels.
- No Brief built from `[!social]` and `[!qna]`. No `Who Knows What` block, no Event Outcomes block and no debrief scene.
- Renown paid to "the party", with no base renown and only two +1 lines.
- Rank benefits written as speeches, with no limits, counters or recipient.

**Rules and facts**
- 2014 blocks: "Thug", "Veteran" and a "modified Mage".
- "Manshoon" appears ungated in 37 lines (m02, m03, m06, r25, s02).
- Cassalanter "infernal" wording (m04 ev-01:19, m04 overview:27, m05 ev-01:107).
- M1 invents a Night Three ambush outside its own Days 1–7 and drops the source's day-nine carrion crawler.
- M4 and M5 open with three checks in a row, which fails the Three Clue Rule.
- M5: "1244 DR", "Greengrass morning", and Copper Street placed in the Trades Ward.
- M6: Jalester leaks an audience he does not attend, and the Writ is "void" against arc-j:238.
- s01 has no trigger. s02 uses circular Stone evidence and gates M6 at Renown 10.

## User decisions (Session 44)

1. **M6 gate.** M6 needs Renown 13 and 7th level, after **Kolat Towers** (the FG/EE precedent).
   - A three-heist party plays M6 after the Vault.
   - The Vault reads **Writ Issued** with an "if not run" default: a lesser Watch letter from Laeral. This is logged for the Vault conversion.
2. **Jalester removed from duty.**
   - If Laeral is told Jalester is compromised, she keeps him away from the Yawning Portal on desk duty at the palace.
   - **Sevel Dastar** becomes the interim handler. He inherits every brief, debrief and rank benefit routed through Jalester.
   - r50 then reintroduces Sevel in his attaché role.
3. **Laeral admits her decline at Lioncrown.**
   - This is the one exception to her voice rule. Her r50 honest answer about her power survives in substance.
   - The voice entry in `city-officials.md` is amended in the companion pass.
4. **Esloon keeps the full 2024 Mage** (CR 6, 81 HP, AC 15).
   - CR 2.0 at 4th level, Esloon alone: 5 PCs 48% Bloody; 4 PCs 76% Brutal; 3 PCs 134% Crushing.
   - His crew is sized per party size by the mechanics reference. Use those rosters exactly.

## Standing defaults

**Secrets**
- **Manshoon.** Use the DR/Harper/FG/EE **Manshoon Named** gate, written by **Faction Outposts** (unconverted).
  - Until it is marked for a member, Jalester, Laeral and every other speaker say "the Splinter" or "the other cell".
  - Overview, Involved Characters and Summary labels say "the Splinter". GM text may state the truth.
  - M6 uses the gate too, even though it runs after Kolat Towers.
- **Cassalanters.** Suspicion only. Nobody knows they are infernalists.
  - Their errands in M4 and M5 are "a household errand" or "a family matter"; never "infernal", "ritual" or "pact".
  - s02 R/PREV :23 handles this correctly ("Nobody in the room knows what those things are."). Keep that line's sense.
- **Jarlaxle.** No Alliance speaker names Jarlaxle, Zardoz Zord or Bregan D'aerthe to players before **Jarlaxle Unmasked**. Say "the carnival fleet" or "the *Eyecatcher*'s crew".
  - Luskan's open bid to join the Lords' Alliance is public knowledge and may be mentioned.
- **Illuun and the well.**
  - Illuun listens through Jalester's evenings at the Yawning Portal's well (Harper M6 ev-01:18; EE M6 overview:30). Jalester does not know and is loyal.
  - The First Meeting, every Brief and debrief at the Portal, and s02 take place at that table. Each gets one GM-only line: anything said at the well may reach something below; Jalester does not know.
  - No speaker says "Illuun". At M6 Laeral hears "something old and patient listening through the water".
- **Two Zhentarims.** Davil's Doom Raiders and the Splinter are different organisations. Jalester distinguishes them ("not Davil's people").

**Membership**
- **Candidates.** Every character in no other faction is a candidate and answers for themselves.
  - Jalester addresses a character with the Vassal, Guard, Noble or Soldier background first; otherwise the highest Charisma.
  - A character already in another faction gets no offer, and Jalester says so in one qna answer.
- **Lords' Alliance Offer Closed** is marked per character who declines. Jalester never chases.
  - A character who becomes unaffiliated later (for example through BD **Contact Severed**) meets Jalester at the well within a tenday, with the same scene.
  - A dismissed member (**LA Dismissed**) counts as unaffiliated for other First Meetings, at Renown 0.
- **Members only.**
  - Briefs, debriefs, renown, ranks and benefits belong to individual Alliance members. Companions help with everything else and earn no renown.
  - Every gate reads "becomes available when an individual Lords' Alliance member reaches Renown N and Nth level".
  - At the Portal, companions sit at the bar while Jalester talks to members.
- **Party-wide gifts are deliberate.**
  - The civic renovation grant (First Meeting) goes to the party's manor.
  - The Writ (M6) names every character present except a dismissed member.
  - Say this in GM text, as BD m04 does for its statuette.
- **Suspension (s01)** fires only on refusal, or on abandonment past the deadline the Brief states. An honest failure costs nothing.
  - Every Brief from M1 to M5 states its deadline in Jalester's speech. M6 is a summons, not an assignment, and has none.
  - A suspended member's missions, ranks and benefits pause. Renown is never reduced by s01; a dismissed member's score goes inert.

**Jalester Silvermane**
- **Stat line:** Lawful Good, Human (Cormyrean), he/him. Spy block.
- **Seat:** the corner table by the Yawning Portal's well, in the evenings. He writes in a small notebook.
- **Voice** (`voices/lords-alliance.md`):
  - quiet, level, formal; short specific questions; "Understood.";
  - asks one question more specific than the conversation needs, and thanks people formally;
  - rare, self-directed swearing; one raw "fuck" only if Faerrel is used against him;
  - never talks about Faerrel Dunblade unless asked twice. No event raises Faerrel.
- He closes every Brief with a question.

**Laeral Silverhand**
- **Stat line:** Chaotic Good, Elf (moon elf, per her Notable Figures page), she/her. Archmage block. WDH has her human; log the clash in design notes, don't resolve it.
- **Voice** (`voices/city-officials.md`): measured, complete sentences; comfortable silence; "the city comes first"; never swears in office.
- She admits her decline only at Lioncrown (decision 3).
- At M6 she detects lies with a flat rule: a lie needs a **DC 16 Charisma (Deception)** check to pass her.

**Sevel Dastar**
- **Stat line:** Spy block (CR 1). No voice profile: plain, dry, may swear lightly.
- Interim handler when Jalester is on desk duty (decision 2); attaché at Lioncrown. He reports to Laeral's office.

**The contact object: Jalester in person**
- Jalester delivers each mission himself at the well table, in the evening (Appendix B:204: the Alliance sends no paper birds).
- **Four deliberate breaks**, one per escalation, each written once in its Brief:

  | Event | Contact |
  |---|---|
  | M2 | a Watch courier brings a Watch-sealed note naming a time; Jalester briefs in person that evening at a sealed address |
  | M3 | Jalester arrives at Trollskull Manor at noon and doesn't sit |
  | M5 | a formal courier letter on plain paper, in a stiffer style than his speech |
  | M6 | two Watch officers in dress uniform bring a vellum summons signed by Laeral |

- Rank events: Jalester at his table on the evening after the member crosses the threshold. A member away from Waterdeep meets him the evening after returning.
- Notes carry a short paragraph at most and are signed "J.S.". No word cap applies.
- If **Laeral Told of Jalester** is marked, Sevel takes Jalester's place in every later contact, at a table in the Portal's taproom away from the well.

**Rules**
- **2024 rules and names only.** Tough, Tough Boss, Warrior Veteran, Spy, Guard, Bandit, Bandit Captain, Kenku, Mage, Carrion Crawler, Scout, Commoner.
  - Every roster comes from `docs/plans/lords-alliance-mechanics-reference.md`. Don't invent CR math or stat values.
  - Checks read "**DC N Ability (Skill)**" with a stated fallback. No single check settles a mission.
  - Fights go in `[!hazard]` with `#### X's Tactics`, an end or retreat condition and a non-combat route.
- **Calendar.** Campaign year 1492 DR. Give spans in days or tendays. Use no festival names the campaign calendar doesn't hold.

**Renames (collisions)**

| Old | New | Collides with |
|---|---|---|
| "The Tenday Watch" (M1 ev-01 title) | **Six Bells at the Muleskull** | Force Grey M3 ev-01 |
| "Night Three" (M1 ev-02 title) | **Day Nine** | (scene cut) |
| the Bent Nail alehouse (M2) | **the Tarred Rope** | Tally Fellbranch's woodshop |
| Vhaspar Holmbridge (M4) | **Vhaspar Coldwater** | WDH's Vhaspar Holmdreg |
| Noska Ur'gray as M5 bidder | **Ossery Klenn**, a Guild negotiator; Noska is absent | Noska's Guild response-team role and voice ("never negotiates") |
| Fentree's house on Copper Street (M5) | **Brasswick Lane**, Trades Ward (invented; list it) | Copper Street is North Ward/Sea Ward in WDH |
| Krentz "Arc B" / "Trollskull Alley" | **Finding Floon** | Krentz is a Finding Floon NPC |

Keep every other R name. New invented minor NPCs go in each folder's design notes under "Invented Names and Open Items".

## Gates and renown (shared ladder)

| Mission | Gate | Base | `+1` bonuses (each once, each tied to a named condition) |
|---|---|---|---|
| M1 | joining, 2nd level | 2 | no worker or Guard drops in the day-nine fight; the leak named and reported to Jalester (**Leak Closed**); Berna's trust earned (**Berna Trusts the Party**) |
| M2 | Renown 3, 3rd level | 2 | Harko dealt with before the Watch or Lira raises an alarm; the Terasse cipher note recovered and reported (**Terasse Cipher Taken**); Harko delivered alive (**Harko Taken Alive**) |
| M3 | Renown 5, 4th level | 3 | the deal scuttled before Esloon and Sarvos shake hands (**Splinter Deal Scuttled**); Sarvos taken alive and the checkpoint named (**Sarvos Captured**); Esloon's question carried to Jalester (**Esloon Question Delivered**) |
| M4 | Renown 8, 5th level | 3 | Vhaspar alive in custody and Halek named (**Halek Farran Named**); the address identified as the Cassalanter villa and reported (**Villa Address Identified**); the fourth target, the longshoreman, warned and alive |
| M5 | Renown 10, 6th level | 4 | the ledger reaches Jalester within 24 hours of recovery; Emira identified and reported (**Emira Identified**); Rezka taken alive and gives a statement |
| M6 | Renown 13, 7th level, after Kolat Towers | 4 | Q1 answered truthfully and accurately; Q2 answered with any two of the four faction lines true; the offer argued down (**Splinter Offer Declined**) |

The base-only path reaches every gate: 1 → 3 → 5 → 8 → 11 → 15 → 19. r03 fires after M1, r10 after M4 (base-only), r25 around M6 with bonuses. No mission grants rank.

## Event Outcomes (one writer each; mark with the member's name where individual)

| Outcome | Writer | Readers |
|---|---|---|
| **Lords' Alliance Joined** (per character) | 00 | every LA event; Factions Guide; BD s04 |
| **Lords' Alliance Offer Closed** (per character) | 00 | 00 (late candidates); s02 |
| **Leak Closed** | M1 ev-02 | M2 Brief (Jalester's tone); Faction Outposts (unconverted) |
| **Berna Trusts the Party** | M1 ev-02 | Faction Outposts (unconverted): Berna's tips on Trades Ward drops |
| **Herath's Note Received** | M1 ev-02 | Xanathar's Lair (unconverted): a sewer approach |
| **Harko Taken Alive** | M2 | M3 Background; Faction Outposts (unconverted) |
| **Terasse Cipher Taken** | M2 | Faction Outposts (unconverted): a fourth path into the Terasse Estate |
| **Thayan File Obtained** | M2 | M3 (a known face at the Skewered Dragon: −2 to the DC of one approach) |
| **Splinter Deal Scuttled** | M3 | Faction Outposts (unconverted) |
| **Sarvos Captured** | M3 | Faction Outposts (unconverted): the checkpoint strike fails |
| **Esloon Question Delivered** | M3 | M6 Background; Faction Outposts (unconverted) |
| **Halek Farran Named** | M4 | M5 ev-02 (Jalester ties Emira to the same household); Cassalanter Villa (unconverted) |
| **Villa Address Identified** | M4 | Cassalanter Villa (unconverted, if it has not run) |
| **Ledger Delivered** | M5 ev-02 | M6 (primary trigger); s02 (evidence); Vault of Dragons (unconverted) |
| **Ledger Sold to the Guild** | M5 ev-02 | Xanathar's Lair (unconverted, if it has not run); Vault of Dragons (unconverted) |
| **Ledger Sold to the Cassalanters** | M5 ev-02 | Cassalanter Villa (unconverted, if it has not run); Vault of Dragons (unconverted) |
| **Emira Identified** | M5 ev-02 | M6 Q2; Cassalanter Villa (unconverted) |
| **Writ Issued** | M6 | Vault of Dragons (unconverted; "if not run" default) |
| **Splinter Offer Declined** / **Splinter Offer Taken** | M6 | Vault of Dragons (unconverted) |
| **Laeral Doubts the Party** | M6 (one lie detected) | r50; Vault of Dragons (unconverted) |
| **Laeral Told of Jalester** / **Jalester Concealed** | M6 | every later LA contact (Sevel replaces Jalester); r25; r50; Vault of Dragons (unconverted) |
| **LA Suspended**, **LA Reinstated**, **LA Dismissed** (per member) | s01 | every LA Brief and rank event; Vault of Dragons (unconverted); 00 (dismissed = unaffiliated) |
| **LA Grand Game Escalated** (per member) | s02 | M5 Background; M6; r25; Vault of Dragons (unconverted) |
| **Redknife Reached** (per member) | r03 | r10; DR s01; BD m03 |
| **Stingblade Reached** (per member) | r10 | r25 |
| **Warduke Reached** (per member) | r25 | r50 |
| **Lioncrown Reached** (per member) | r50 | Dungeon of the Mad Mage |
| **Undermountain Commission Accepted** (per member) | r50 | Dungeon of the Mad Mage |

**Read, not written, by this folder:** **Manshoon Named** (Faction Outposts), **Jarlaxle Unmasked**, **Jalester Compromise Identified** (Harper M6), **Vajra Briefed** (Force Grey s01), **Stone Taken by Splinter** (Harper M6), **Kolat Towers** state (unconverted).

## Per-folder briefs

### 00 First Meeting (ev-01 "Lords' Alliance First Meeting", design-notes). Report 02 §3, §4; report 01 §6.2

- Jalester at the well table. **The Pitch** is a social block plus 6 qna: who he reports to, what the Alliance wants, what it pays, the other factions, "what if we disagree", and "can we keep other loyalties". Will not discuss: the Stone, the vault, active intelligence.
- **The Condition**, verbatim: "Assignments from us are not optional. If that changes your answer, now is the time to say so." Then three seconds of silence.
- **Each Candidate's Answer**: an accept readaloud and a decline readaloud. Then a **Cloak Benefits** block per member, with no token: Watch officers know members by Jalester's word. Patrol schedules arrive by note once a tenday.
- **The Civic Grant**: 200 gp of renovation help, given once at party level. The Fellowship ward-fee cut stays passive and gets one line.
- **Late Candidates**, as in the defaults above.
- Keep the keeper lines listed in report 02 §12.
- The GM-only well line goes here.

### M1 The Long Watch (overview, ev-01 Six Bells at the Muleskull, ev-02 Day Nine, design-notes). Report 03 §3.2

- **Source tenday.** A Trades Ward escort for Mareva Coile's sweepers, with Berna and Herath, run Days 1–8 as beats from Appendix C.
- **The leak.** Delvon Harsk's leak runs through Pirn and is identified through three independent clues: the Day 4 watcher, the schedule scrap, and Mareva's supervisor list.
- **The Night Three ambush is cut.** The only fight is the **day-nine carrion crawler** at highsun in a Trades Ward alley, with Berna and two Guards at half HP. Use the mechanics reference rosters at 3, 4 and 5 PCs.
- Herath's sewer note is found on day nine. The debrief with Jalester is in ev-02.
- ev-01 writes nothing and ends "Continue with **Day Nine**".
- Delete nothing yourself. The main session removes the old `ev-01-the-tenday-watch.md` and `ev-02-night-three.md`; write the new files as `ev-01-six-bells-at-the-muleskull.md` and `ev-02-day-nine.md`.

### M2 The Exile's Return (overview, ev-01, design-notes). Report 03 §3.3

- **Contact break:** the Watch-sealed note, then Jalester in person that evening. His order is "quietly put him to the sword". Harko's surrender is the turn.
- **Three leads** from Appendix C, any of which finds Harko.
- The warehouse fight uses the mechanics reference roster: Harko (Bandit Captain), Kenku and Bandits, with the kenku alarm as a clock.
- **Harko's Terasse cipher note** (K = Keln Trigos) is a fourth path into the Terasse Estate.
- **Lira**: three branches.
- Veralax's alehouse is **the Tarred Rope**. No Manshoon in speech: "the Splinter's fixer".

### M3 The Red Wizard's Price (overview, ev-01, design-notes). Report 03 §3.4; decision 4

- **Contact break:** Jalester at Trollskull at noon, standing. The deadline is tonight.
- **The Skewered Dragon is Splinter-owned.** The host doesn't help, and the place is hostile ground.
- **Four approaches** (R), with Appendix C's three source paths as the ways in.
- **Esloon Bezant**: Neutral, five years in Waterdeep. He never says why he left Thay; cut the backstory speech. He is the full Mage.
  - He withdraws with *Misty Step* or *Invisibility* when the mechanics reference's threshold is reached.
  - His question for the Alliance is kept.
- **Sarvos Miln** (Spy) is the Splinter's broker.
- Split into two events only if the draft passes 480 lines: ev-01 "Finding the Meet", ev-02 "The Deal".

### M4 The Archer Above (overview, ev-01, design-notes). Report 04 §4

- **Vhaspar Coldwater** (Warrior Veteran) is the archer. Ziraj is untouched.
- **Three independent leads** to the feed-store room. Saeth Cromley is one; the Stingblade Watch file is a free fourth for a Renown 10 member.
- **Vhaspar's bolt hole is not the Skewered Dragon.**
- **The chase** is a clock, not a hazard roster.
- **Halek Farran** is a hired agent who paid Vhaspar on a household errand. He is not villa staff.
- The partial address points at the Sea Ward villa.
- The debrief happens a tenday later with the dossier.

### M5 Fentree's Ledger (overview, ev-01 The Missing Volume, ev-02 The Green Dragon, design-notes). Report 04 §5

- **ev-01:**
  - The courier letter.
  - Fentree's study on Brasswick Lane. Orvane Fentree died "ten days ago" of a genuine heart attack.
  - **Three independent leads** to Rezka: the neighbour Orlass Hemmet, the money-changer, and the copper button.
  - The Green Dragon booking. Nothing is awarded here.
- **ev-02:**
  - The bell clock: Ossery Klenn (Guild) at second bell in Room 4, Emira Volstren (Cassalanter agent) at third bell in Room 6.
  - Three approaches, socials for Rezka, Ossery and Emira, and the interception hazard from the mechanics reference.
  - **The ledger** shows Dunberton Holdings paying "a vault custodian" in entries from Neverember's last years (the 1480s). Three ways to read it.
- **s02 order branch.** If **LA Grand Game Escalated** is already marked, Laeral already knows the vault is in Waterdeep, and the ledger proves how it is financed.

### M6 An Audience with the Open Lord (overview, ev-01, design-notes). Report 04 §6; decisions 1, 2

- **Contact break:** the vellum summons. Gate: Renown 13, 7th level, after **Kolat Towers**. Triggered by **Ledger Delivered**, or, if the ledger was sold, by **LA Grand Game Escalated** or Renown 13.
- **The audience room** is a stated size; r50 compares its annex to it.
- **Laeral's three questions** with fixed answers:
  - Q1: the Stone's holder, from a state table;
  - Q2: four faction lines, with a true-line rubric that reads **Emira Identified**, **Vajra Briefed** and **Jarlaxle Unmasked**;
  - Q3: a table by Kolat Towers state.
- **The lie rule** is the flat DC 16 Deception from the defaults.
- **The offer and the argument.**
- **The Writ** is never void. It names every character present except a dismissed member.
- **The Jalester Question** fires only if someone at the table holds **Jalester Compromise Identified**.
  - The leak is what Jalester hears *afterwards*, when he takes the party's report to the palace. He is not in the audience.
  - If Laeral is told, mark **Laeral Told of Jalester**: desk duty, and Sevel takes over.
  - Otherwise mark **Jalester Concealed**: the feed stays open.
- No combat.

### s01 Suspension and Dismissal (ev-01, design-notes). Report 02 §5a

- **Trigger:** refusal, or abandonment past a Brief's stated deadline.
- **The visit** at the well.
- **The suspended-status rules.**
- **Reinstatement** has three routes: verified intelligence, a completed task Jalester names, or Laeral's word after s02.
- **Dismissal:** "This is done. Your Renown stays on the books. It doesn't do anything."
- A table of compelling-reason examples (illness, a captive's life, another faction's emergency) that excuse a missed deadline without suspension.
- Keep the outcome names.

### s02 Escalation to the Open Lord (ev-01, design-notes). Report 02 §5b

- **Threshold:** a member holds all three facts: the Stone's current holder, the vault in Waterdeep, and two confirmed villain factions.
- **Evidence** comes from the Force Grey s01 three-route table (copy its shape), not from the Stone.
- **The briefing** at the well, the three clarifying questions, and Laeral's one-day note.
- **Payment:** +2 Renown once to each member present.
- Order branch with M5, as in M5's brief.
- **Wording gates:** "two villain factions" are "Xanathar's Guild and the Splinter" until **Manshoon Named**. Keep the Cassalanter line.

### r03 / r10 / r25 / r50 (ev-01 + design-notes each). Report 02 §4d, §4e, §9; report 01 §6.6

Every rank event: "The rank event awards no Renown"; a per-member tracking line; and a Next Steps naming the next threshold. If **Laeral Told of Jalester** is marked, Sevel delivers it.

- **r03 Redknife.**
  - **Watch Escort:** two Guards for one dangerous errand per tenday, with notice 24 hours ahead through a note at the well. **Emergency clause:** once per tenday, with no notice, a Watch patrol answers a Redknife's whistle within 1d4 + 1 minutes in the city's lit streets. This keeps BD m03:226 valid.
  - **Safe Houses:** one in the Castle Ward and one in the Trades Ward. The phrase is "Alliance weather". Neither is near Kolat Towers.
  - **String-Pulling:** once per tenday, a minor charge or Watch report disappears. DR s01:239 reads this.
  - **Loss rule:** suspended or dismissed members lose all three.
- **r10 Stingblade.**
  - **Introductions:** one per quest, from a fixed table of 8 names in the mechanics reference.
  - **Legal Coverage:** one incident per quest, up to the mechanics reference's gp ceiling.
  - **Watch Files:** standard files take one hour; classified files take four hours and a **DC 12 Charisma (Persuasion)** check.
- **r25 Warduke.**
  - Branch on whether M6 has run. Never write "first meeting with Laeral" unless M6 has not run.
  - **The private audience**, once per quest, with fixed results distinct from Harper Wise Owl.
  - **Response team:** four Warrior Veterans for one operation per quest; ally Power is in the mechanics reference.
  - **Response-team intel** every 3 days, from the mechanics reference table. It names a team only after the member has met it, and says "the Splinter" and "the carnival fleet". No imps or devils.
  - **Masked Lord request:** one per quest, from a fixed table. The Masked Lord is never Mirt and is unnamed.
- **r50 Lioncrown.**
  - Expected during Dungeon of the Mad Mage. It fires when the member is on the surface.
  - The charge removed. Three honest answers, with fixed lines for the common questions; one may be Laeral admitting her decline (decision 3).
  - Sevel as attaché.
  - **The Undermountain request:** the missing agents are **Joroth Brighthelm's team** (WDMM). The Runestone is mentioned separately as Jalester's errand.
  - Cut the "twelve" Masked Lords.
  - Branch on **Laeral Told of Jalester** and **Laeral Doubts the Party**, not on the Vault.
  - Keep **Undermountain Commission Accepted**.

## Companion pages (main session, after the folders merge)

- **Factions Guide** `03-lords-alliance.md`: gates, base renown, the M4 row (Vhaspar, not Ziraj), the Manshoon lines (:42, :47, :67), the rank procedures, and the "Veterans" wording.
- **Organization page** `02-lords-alliance.md`: "Renown 25+" for Laeral access, and its Manshoon line.
- **Notable Figures pages:**
  - Jalester's: "Featured in";
  - Esloon's: Mage, Neutral, the M3 listing;
  - Laeral's: the LA listings;
  - Dagult's: the M5/M6 listings.
- **Rank rows** in `players-guide/faction-affiliations.md` and `gm-guide/player-factions-overview.md`, including the "serious offenses cost 2 Renown" line against s01.
- **Trollskull pages:**
  - ev-04 :56 (the grant), :72 (M1 text) and :100 (the True/False Joined heading);
  - `08-notable-patrons.md:107` (Jalester as Spy, LG).
- **Laeral's voice entry** in `city-officials.md` (decision 3).
- **Harper M6:** a reader line for **Laeral Told of Jalester**.
- **Out-of-scope log:** a new section in `harpers-out-of-scope-notes.md`.
