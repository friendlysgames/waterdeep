# Plan: Lords' Alliance faction events rewrite (Session 44)

## Context

The user asked for the Lords' Alliance faction events to be rewritten the way the Harpers (S41), Force Grey (S42) and Emerald Enclave (S43) were.

- **R** (rewrite input): the first-commit versions, extracted to `scratchpad/la-orig/lords-alliance/` because the in-place restore was refused. **PREV** is the current folder in the repo. It is R plus retired sidebars, and it is used only as a fact source.
- Research reports: `docs/plans/lords-alliance-research/01–05` (committed).

What the research found:

**Format**
- All 26 files use retired formats (`[GM]`, True/False flags, `Milestone: None`, `[!narrative]`/`[!dialogue]`).
- No page has a social+qna Brief, a Who Knows What block, Event Outcomes or a debrief scene. Seven folders lack design notes.

**Gates and renown**
- Gates sit below the shared ladder: R 0/2/4/6/8/10 against 1/3/5/8/10/13.
- No mission pays base renown, and each has only two +1 bonuses.
- Briefs, debriefs and renown are party-wide.

**Membership**
- The First Meeting never lets a candidate answer.
- Cloak and the 200 gp civic grant that Trollskull ev-04 and the manor guide promise are never delivered.

**Mission problems**
- **M1** contradicts the guide, Trollskull ev-04:72, WDH and Appendix C. It drops the day-nine carrion crawler for an invented Night Three ambush, which falls outside its own Days 1–7.
- **M4 and M5** fail the Three Clue Rule (three checks in a row).
- **M5's fight** is trivial. Noska is miscast as a bidder, the dates are wrong ("1244 DR", "Greengrass"), and Copper Street is in the wrong ward.
- **M6** leaks through Jalester, who isn't in the room, and its Writ is "void" in a way that contradicts arc-j:238.

**Gate and rules violations**
- "Manshoon" appears ungated in 37 lines across m02, m03, m06, r25 and s02.
- "Infernal" Cassalanter wording appears in m04 and m05.

**Standalone events**
- **s01** has no trigger and no reader.
- **s02** overlaps M5, relies on circular Stone evidence, and gates M6 at R10.
- **r25** treats Laeral as a first contact. **r50** breaks her profile, which the user has now ruled on (below).

**Stat blocks and names**
- 2014 blocks: Thug, Veteran and a "modified Mage".
- Name collisions:
  - the "Bent Nail" alehouse (Tally's woodshop);
  - "The Tenday Watch" (a Force Grey M3 event title);
  - Vhaspar Holmbridge (WDH's Vhaspar Holmdreg);
  - Noska (a Guild response-team leader).

The goal is a Lords' Alliance set on the DR/BD/Harper/FG/EE page model, voiced in Ember and consistent with the rest of the campaign.

## User decisions (Session 44)

1. **M6 gate.** M6 needs R13 and 7th level, after Kolat Towers (the FG/EE precedent). A three-heist party plays M6 after the Vault. The Vault reads **Writ Issued** with an "if not run" default (a lesser Watch letter from Laeral), and this is logged for the Vault conversion.
2. **Jalester removed from duty.** If Laeral is told Jalester is compromised, Sevel Dastar takes over as interim handler and inherits every brief and rank benefit routed through Jalester. r50 then reintroduces Sevel as the attaché.
3. **Laeral admits her decline at Lioncrown.** This is the one exception, and her voice entry in `city-officials.md` is amended to allow it.
4. **Esloon keeps the full 2024 Mage (CR 6).**
   - CR 2.0 at 4th level, Esloon alone:
     - 5 PCs (115 Power): 48%, Bloody, a standard fight;
     - 4 PCs: 76%, Brutal;
     - 3 PCs: 134%, Crushing.
   - The encounter-builder sizes his crew per party size. The main session checks its numbers against the data and recomputes every verdict.

## Defaults settled without asking (the user can overrule any)

**Contact and membership**
- **Contact object.** Jalester appears in person, at the Portal well table in the evenings (Appendix B:204: "no paper birds"). There are four deliberate written breaks, one per escalation:
  - M2: a Watch-sealed note;
  - M3: Jalester arrives at Trollskull at noon and doesn't sit;
  - M5: a formal courier letter;
  - M6: Watch officers bring a vellum summons from Laeral.
  - No word cap applies, since this is not *Animal Messenger*.
- **Candidates.** Every unaffiliated character is a candidate. Joining, renown and rank are per character.
  - Jalester addresses the Vassal, Guard, Noble or Soldier background first.
  - **Lords' Alliance Offer Closed** is per character, and Jalester never chases.
  - A dismissed member counts as unaffiliated for other First Meetings, at Renown 0.
- **First Meeting deliverables:**
  - a Cloak Benefits block per member, with no token: officers know members by Jalester's word;
  - the 200 gp civic renovation grant, given once at party level;
  - the Fellowship ward-fee cut stays passive (S43 rule).

**Gates and renown**
- **Shared ladder.**

  | Mission | Gate | Base renown |
  |---|---|---|
  | M1 | joining, L2 | 2 |
  | M2 | R3, L3 | 2 |
  | M3 | R5, L4 | 3 |
  | M4 | R8, L5 | 3 |
  | M5 | R10, L6 | 4 |
  | M6 | R13, L7, after Kolat Towers | 4 |

  - Each mission has three listed +1 bonuses.
  - No mission grants rank.
  - Base-only renown runs 1→3→5→8→11→15→19.
- **Secrecy.**
  - **Manshoon Named** gate: speakers say "the Splinter" until it is marked, and M6 uses the gate too.
  - **Cassalanter suspicion only:** "a household errand", never "infernal".
  - Two Zhentarims and Jarlaxle's identity are unchanged.

**Missions**
- **M1: hybrid.**
  - Keep the source tenday, Mareva, Berna and Herath, and the light leak investigation (Delvon and Pirn) with three independent clues.
  - The Night Three ambush is cut. The combat is the day-nine carrion crawler in the Trades Ward, sized by the builder at 3, 4 and 5 PCs.
  - Herath's note is read by Xanathar's Lair (unconverted).
- **M2.**
  - Jalester delivers it in person, after the Watch-sealed note.
  - The order is restored: "quietly put him to the sword", with Harko's surrender as the turn.
  - Appendix C's three independent leads, plus Harko's Terasse cipher note as a fourth Faction Outposts path.
  - The Bent Nail is renamed.
- **M3.**
  - The Skewered Dragon stays and is written as Splinter-owned: the host doesn't help.
  - R's four approaches stay, with Appendix C's three source paths folded in.
  - Esloon's backstory speech is cut to his voice profile: no stated reason for leaving, Neutral, five years in the city.
  - His crew is Toughs, sized by the builder, and he withdraws with *Misty Step* or *Invisibility*.
- **M4.**
  - Vhaspar stays the subject but gets a new surname, so Ziraj stays free for DR.
  - Three independent leads.
  - Halek Farran is a hired agent, not villa staff. The dossier is read by Cassalanter Villa (unconverted, "if it has not run").
- **M5.**
  - Relative dates ("ten days ago"; ledger entries in the 1480s) and a corrected ward.
  - The buyer is a new Guild negotiator, and Noska is absent.
  - Three independent leads to Rezka.
  - The fight is resized by the builder.
- **M6.**
  - Laeral's Insight device becomes a flat Deception 16.
  - Q3 uses a table by Kolat Towers state.
  - The Writ is never void (arc-j:238).
  - The Writ names every character present except a dismissed member.
  - The Jalester thread is triggered by Harper **Jalester Compromise Identified**: what Jalester hears *afterwards*. If Laeral is told, he goes to desk duty and Sevel takes over (decision 2).

**Standalone events**
- **s01** fires on refusal or abandonment past a deadline stated in every brief (M6 excepted). An honest failure costs nothing. It has three reinstatement routes. Renown is never reduced, and a dismissed member's score goes inert.
- **s02** uses Force Grey s01's three-route evidence table instead of the Stone. Whichever of s02 and M5 lands first corrects Laeral's Neverwinter belief, and the other opens with a branch. It pays +2 once to each member present.

**Ranks**
- **r03** adds an emergency-escort clause (one per tenday, no notice) so BD m03:226 and DR s01:239 stay valid.
- **r10** uses fixed tables for introductions and Watch files.
- **r25** branches on whether M6 has run, uses four Warrior Veterans with ally Power, and has fixed tables for response-team intel and Masked Lord requests. The Masked Lord is not Mirt.
- **r50** keeps **Undermountain Commission Accepted**, adds Joroth Brighthelm's team (WDMM) as the missing agents, mentions the Runestone separately, and cuts the "twelve" Masked Lords.

**Blocks and titles**
- Stat blocks: Tough and Tough Boss, Warrior Veteran, Spy, Guard, Bandit Captain, Mage and Carrion Crawler, all from the 2024 data. No homebrew.
- **Titles and paths.** Keep every linked file path and every quest title. New event titles avoid collisions; M1's become "Six Bells at the Muleskull" and "Day Nine".

## Folder plan

| Folder | Events | Writes (one writer each; readers set in the brief) |
|---|---|---|
| 00 First Meeting | ev-01 (keep path) | **Lords' Alliance Joined**, **Lords' Alliance Offer Closed** (per character) |
| m01 The Long Watch | ev-01 Six Bells at the Muleskull · ev-02 Day Nine | **Leak Closed**, **Berna Trusts the Party**, **Herath's Note Received** |
| m02 The Exile's Return | ev-01 | **Harko Taken Alive**, **Terasse Cipher Taken**, **Thayan File Obtained** |
| m03 The Red Wizard's Price | ev-01 (split if over 480 lines) | **Splinter Deal Scuttled**, **Sarvos Captured**, **Esloon Question Delivered** |
| m04 The Archer Above | ev-01 | **Vhaspar Taken Alive**, **Villa Dossier Compiled** |
| m05 Fentree's Ledger | ev-01 The Missing Volume · ev-02 The Green Dragon | **Ledger Delivered**, **Ledger Lost to the Guild**, **Ledger Lost to the Cassalanters**, **Emira Identified** |
| m06 An Audience with the Open Lord | ev-01 | **Writ Issued**, **Splinter Offer Declined**, **Laeral Told of Jalester** |
| s01 / s02 | ev-01 each (keep paths) | **LA Suspended**, **LA Reinstated**, **LA Dismissed** / **LA Grand Game Escalated** |
| r03 / r10 / r25 / r50 | ev-01 each (keep paths) | **Redknife Reached**, **Stingblade Reached**, **Warduke Reached**, **Lioncrown Reached**, **Undermountain Commission Accepted** |

Every folder gets `design-notes.md`, ending in "Invented Names and Open Items". Mission folders get the full DR overview skeleton. The obsolete M1 event files are removed with `git rm` by the main session.

## Execution (the S41–43 method)

1. **The main session writes the docs** in `docs/plans/`:
   - `lords-alliance-plan.md` (this plan);
   - `lords-alliance-conversion-brief.md` (decisions, defaults, renames, the full outcome table with readers, per-folder briefs);
   - `lords-alliance-drafter-instructions.md` (adapted from EE).
   - The instructions state the ranges up front: speech 11–14 words, readaloud 18–20, GM 17–19 with under 5% of sentences at 7 words or fewer, and a 28-word ceiling.
2. **The `encounter-builder` writes `lords-alliance-mechanics-reference.md`** into a stub the main session creates first.
   - CR 2.0 rosters at 3, 4 and 5 PCs:
     - M1 crawler (L2);
     - M2 Harko and his crew (L3);
     - M3 Esloon and his Toughs (L4);
     - M4 Vhaspar chase clock (L5);
     - M5 interception (L6).
   - Allies: the r03 Guards, the r25 Warrior Veterans, Sevel.
   - Tables: introductions, Watch files, response-team intel, Masked Lord requests.
   - **The main session recomputes every Power verdict and checks every stat value against `scratchpad/5e/`.**
3. **`prose-drafter` agents, at most five at a time:**
   - Wave 1: 00, m01, m02, m03, r03.
   - Wave 2: m04, m05, m06, s01, r10.
   - Wave 3: s02, r25, r50.
4. **Per folder:**
   - `voicecheck.py`, then a numeric rhythm pass;
   - main-session review;
   - commit, PR and merge one document at a time.
   - Never merge while a half-written folder sits on the branch.
5. **The `consistency-checker` pass**, with rulings recorded in `lords-alliance-consistency-rulings.md`, then fixes.
6. **Companion pages:**
   - Factions Guide `03-lords-alliance.md`: gates, renown, the M4 row, the Manshoon lines, the rank procedures;
   - the organization page `02-lords-alliance.md`;
   - Jalester's, Esloon's and Laeral's Notable Figures pages;
   - the rank rows in the players' and GM faction guides;
   - Trollskull ev-04:56/:72/:100 (the grant, the M1 text, the Joined heading);
   - `08-notable-patrons.md:107` (Jalester's block);
   - Laeral's voice entry (decision 3);
   - Harper M6 reads **Laeral Told of Jalester**.
7. **Out-of-scope log.** A new section, "Lords' Alliance event rewrite (Session 44)", goes into `harpers-out-of-scope-notes.md`, covering:
   - the arc-e through arc-j readers (Writ default, Herath, Terasse, dossier, ledgers);
   - Gralhund ev-01:91;
   - Appendix C's "Stagger" save;
   - the Kolat Towers **Manshoon operational?** flag.

## Verification

- `voicecheck.py` is clean on every file, within the §2a ranges.
- A grep finds no retired formats: `[GM]`, `[!narrative]`, `[!dialogue]`, `[!npc-narrative]`, `#### Flag`, `Milestone`, `Arc [A-J]`, `Thug`, `Veteran` without "Warrior", `Wish`, `1244`, `Greengrass`, `Bent Nail`, "infernal".
- Each player-facing hit for Manshoon, Kolat or Cassalanter is checked against its gate.
- The outcome map gives every outcome exactly one writer and a named reader, with unconverted readers tagged.
- Gates and renown match the ladder, and the base-only path reaches each gate.
- Every encounter verdict is recomputed by hand with CR 2.0 (tier-adjusted Power, `(E/P)²`), and every stat value is checked against the 2024 data.
- The consistency-checker report is clean, or its exceptions are logged.
