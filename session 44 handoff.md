# Session 44 Handoff
**Date:** 2026-10-17
**Status:** Ready to continue

---

## What Was Done

The Lords' Alliance faction events were rewritten from scratch with the Session 41–43 method, and all ten steps are done.

**Research and plan**
- The first-commit drafts were extracted to the scratchpad as the rewrite input. The in-place restore was refused by the permission classifier, so the current files stayed as the fact source until the drafters overwrote them.
- Five research agents wrote reports in `docs/plans/lords-alliance-research/`.
- The approved plan, conversion brief, drafter instructions, mechanics reference and consistency rulings are in `docs/plans/lords-alliance-*`.

**Drafting**
- prose-drafter agents drafted all 13 folders in three waves, with voicecheck and rhythm passes.
- The encounter-builder's mechanics reference was recomputed by hand. Its M3 rosters were corrected so the plain CR 2.0 table governs.

**Consistency and companion pages**
- A consistency-checker pass produced rulings A1–C11, all applied.
- The companion pages were aligned: the Factions Guide, the organization page, six Notable Figures pages, Laeral's voice entry, the rank rows, Trollskull ev-04, the manor guide and the Harper M6 reader line.
- Outside contradictions were logged in the out-of-scope notes.

**User fixes at the end**
- The First Meeting gained **The Summons**, a grey-wax card from a Watch runner, so the party knows to go to the Portal.
- The merge-per-document rule was rewritten in CLAUDE.md.

Merged in PRs #134–#155.

---

## Changes Made

Git range: `f0e1fc3..HEAD`.

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/quests/faction-events/lords-alliance/*/` (13 folders) | Full rewrite on the DR/BD/Harper/FG/EE model: Ember blocks, Event Outcomes, the shared gate ladder with base renown and three +1s, per-member rank procedures, the Manshoon/Jarlaxle/Illuun/Cassalanter gates, the well-table listener line, Sevel as interim handler, and a design-notes page per folder. |
| `m01-the-long-watch/` | Split into **Six Bells at the Muleskull** and **Day Nine**. The source's day-nine carrion crawler is restored; R's Night Three ambush is cut. |
| `m05-fentrees-ledger/` | Split into **The Missing Volume** and **The Green Dragon**. Ossery Klenn replaces Noska as the Guild bidder. |
| `campaign/guides/factions/03-lords-alliance.md` | Gates, base renown, the grey-wax First Meeting, Vhaspar not Ziraj, the ledger outcomes, the Splinter gate, the full rank procedures and the suspension rules. |
| `campaign/setting/organizations/02-lords-alliance.md` | Laeral is reached at M6 or Warduke. Contact is the grey-wax card. Manshoon sits behind its gate. A What Is Actually True block is added. |
| `notable-figures/` Jalester, Laeral, Esloon, Noska, Dagult, Saeth | Current titles. Jalester: desk duty with Sevel as interim handler. Laeral: the Lioncrown exception. Esloon: the full Mage, in M3 only. Saeth: Warrior Veteran. Noska and Dagult are dropped from events they are not in. |
| `.claude/skills/character-voices/voices/city-officials.md` | Laeral's "never admits her decline" rule now records the one Lioncrown exception. |
| `guides/players-guide/faction-affiliations.md`, `guides/gm-guide/player-factions-overview.md` | LA rank rows. The Alliance suspends or dismisses for refusal or abandonment, and an honest failure costs nothing. |
| `quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md` | Any unaffiliated character is a candidate, M1 names the carrion crawler, the Joined heading is converted, and the grant row is fixed. |
| `guides/trollskull-manor/02-operating-costs.md`, `08-notable-patrons.md` | The grant is exactly 200 gp. Jalester is LG, Cormyrean Human, Spy, and delivers in person. |
| `harpers/m06-the-stones-other-master/ev-01-…md` | Reader line for **Laeral Told of Jalester** / **Jalester Concealed**. |
| `CLAUDE.md` | Merge-per-document rule: merge as each agent finishes, then after each edit pass. |
| `docs/plans/harpers-out-of-scope-notes.md` | New section, "Lords' Alliance event rewrite (Session 44)". |

### Files Created
| File | Purpose |
|------|---------|
| `docs/plans/lords-alliance-research/00`–`05` | The research brief and the five research reports. |
| `docs/plans/lords-alliance-plan.md` | The approved plan. |
| `docs/plans/lords-alliance-conversion-brief.md` | Binding: decisions, defaults, renames, ladder, outcome table and per-folder briefs. |
| `docs/plans/lords-alliance-drafter-instructions.md` | Drafter rules with numeric voice ranges. |
| `docs/plans/lords-alliance-mechanics-reference.md` | CR 2.0 rosters at 3/4/5 PCs, allies, and the r10 and r25 tables. Recomputed by the main session. |
| `docs/plans/lords-alliance-consistency-rulings.md` | Rulings A1–C11 and the dispatch table. |
| New event files | `m01/ev-01-six-bells-at-the-muleskull.md`, `m01/ev-02-day-nine.md`, `m05/ev-01-the-missing-volume.md`, `m05/ev-02-the-green-dragon.md`, and a `design-notes.md` in every folder that lacked one. |

### Files Deleted
| File | Reason |
|------|--------|
| `m01/ev-01-the-tenday-watch.md`, `m01/ev-02-night-three.md` | Replaced by the M1 split. "The Tenday Watch" collided with Force Grey M3's title. |
| `m05/ev-01-fentrees-ledger.md` | Replaced by the M5 split. |

---

## Key Decisions

### M6 gate
**Decision:** M6 needs Renown 13 and 7th level, after Kolat Towers. A three-heist party plays it after the Vault. The Vault reads **Writ Issued** with an "if not run" default (M6 design notes).
> "R13, L7, after Kolat" — User, this session

### Jalester removed from duty
**Decision:** If Laeral is told of the compromise, Jalester goes on desk duty and Sevel Dastar becomes interim handler for every brief and rank benefit.
> "Sevel Dastar, early (Recommended)" — User, this session

### Laeral admits her decline at Lioncrown
**Decision:** This is the one exception to her voice rule. Her voice entry and Notable Figures page now say so.
> "She admits it at Lioncrown" — User, this session

### Esloon is the full 2024 Mage
**Decision:** Esloon keeps the CR 6 Mage block and fights alone at every party size.
- His crew is an optional separate wave.
- He withdraws on 31 damage or at the end of round 3 (round 2 at three PCs).
- The plain table governs: 48% Bloody at 5 PCs, 76% Brutal at 4, 134% Crushing at 3.
> "Why can't a level 4 party fight a cr6 creature? Did you actually run the numbers?" / "5 level 4 characters is a Bloody fight with a CR 6 creature. That's 44% HP loss." — User, this session

### First Meeting summons
**Decision:** A Watch runner brings a grey-wax card to Trollskull Manor naming the corner table at the Portal, any evening for ten days. Every later LA note uses the same pattern.
> "First meeting needs a way for the party to know to go to the Portal." — User, this session

### Defaults accepted from the plan (the user did not overrule them)
- **Contact:** Jalester in person at the well table, with four written breaks (M2 note, M3 noon visit, M5 letter, M6 summons).
- **Membership:** per character. Asking for time keeps the offer open ten days.
- **M1:** the hybrid (the source tenday plus a light leak investigation, the crawler as the only fight).
- **Renames:** Vhaspar Coldwater, the Tarred Rope, Ossery Klenn, Brasswick Lane, Hollen Brask, Hallan Roke, Maelis Venning, Jorin Larkin, Benn Hallow, Telsa Corlis and Dunmar Crale.
- **Halek Farran and Emira Volstren** are hired agents, not Cassalanter staff.
- **s02** uses the Force Grey three-route evidence table; the Stone is never vault proof.
- **r50** keeps **Undermountain Commission Accepted**; Joroth Brighthelm's team are the missing agents.

---

## Rules and Instructions

All earlier rules stay in force. Added or reinforced this session:

- **Merge each document as its agent finishes, then after every edit.** Never hold a finished document for review, a voice pass, or other folders. Keep unfinished drafts out of the commit instead. *(User: "How many times do I gotta tell you? Merge after each agent is done, then edit, merge again, etc.")* Now in CLAUDE.md.
- **Run the encounter numbers yourself before repeating an agent's difficulty claim.** Two research agents called a lone CR 6 Mage "unfightable" by a 4th-level party without computing anything. The plain tier-adjusted table governs. Heuristics such as "effective Power" from a withdrawal rule may be noted, but they never set the band. *(User: "Did you actually run the numbers?")*
- **Bloody is a normal fight, not a hard one.** 40–60% HP lost is a standard encounter in CR 2.0. Don't call it "hard but doable".
- **A party must always have a reason to go where a scene waits.** Every contact needs an in-fiction summons. *(User: "First meeting needs a way for the party to know to go to the Portal.")*

---

## Problems Solved

- **The in-place restore was refused** by the permission classifier as destructive. The first-commit versions were extracted to the scratchpad and used as input. Nothing was force-overwritten.
- **The M3 roster heuristic.** The encounter-builder rated Esloon plus Toughs as Bloody by discounting his Power for his withdrawal. The plain table gives Overwhelming and Oppressive. Fixed so Esloon fights alone.
- **The archer's weapon.** The mechanics reference said hand crossbow, but the 2024 Warrior Veteran has a Heavy Crossbow, checked against the data. Fixed in the reference, r10 and M4.
- **A stale-index commit.** Commit `1a397e5` (PR #153) was built from a stale real index after a `git reset --soft`, and it silently reverted PR #152's consistency fixes in 17 LA files. PR #154 restored them, and the folder was verified identical to `ff11ed2`.
- **Name collisions renamed:**
  - Teague (twice), Garrow (twice) and Ilsa (twice);
  - Edric Moss, Dorrin Teague and Perrin Dace;
  - the Bent Nail, "The Tenday Watch", and Vhaspar Holmbridge vs Holmdreg.
- **Unreadable outcomes fixed:**
  - **Leak Closed**, **Esloon Question Delivered**, **LA Suspended** and **Stingblade Reached** gained real readers.
  - **Thayan File Obtained** now means one thing in M2 and M3.
  - M6's dead "Kolat Towers has not run" branches were cut.

---

## Outstanding Work

### New this session
- [ ] **Wire the LA outcomes into unconverted quests.** See the out-of-scope notes, "Lords' Alliance event rewrite (Session 44)" §1 (Faction Outposts, Xanathar's Lair, Cassalanter Villa, Kolat Towers, the Vault including the Writ "if not run" default, and Dungeon of the Mad Mage).
- [ ] **Other factions' events that read LA ranks:** BD Three Nights :226 and DR Davil's Arrest :162/:239 test "Renown 3 or higher". They should test **Redknife Reached**, and a suspended or dismissed member should fail.
- [ ] **Emerald Enclave r50 design notes :27** still refers to the old True/False Commission outcome.
- [ ] **Gralhund ev-01:91**: the **Jalester Brief Received: True / False** heading.
- [ ] **Confirm the readings** (out-of-scope §4):
  - Esloon at three characters (end-of-round-2 exit, or a round-1 exit);
  - M2's "goes loud" cost;
  - r25's Read or Ruling audience;
  - r03's Manor Beat and sergeant's note;
  - M6's Strategic Argument DCs.
- [ ] **Accept or replace the Session 44 invented names** (out-of-scope §5), including the "Ha-" cluster.
- [ ] **Leftovers on the companion pages:**
  - the Trollskull ev-04 old banner and milestone formats outside the LA rows;
  - the `08-notable-patrons.md` Faerrel line, which conflicts with the voice rule that no event raises Faerrel;
  - Saeth's other stats;
  - Laeral's species (moon elf on her page, human in WDH);
  - Jalester's age.
- [ ] **Voicecheck residue to polish:** the Factions Guide `03` has 11% short sentences, mostly in tables. Several LA event files sit at 6–8% short GM sentences against the 5% target.
- [ ] **Voice profiles** for recurring LA minor NPCs (Sevel Dastar, Mareva Coile, Berna, Harko, Rezka), if the user asks.


### Carried forward from Session 43
- [ ] **Wire the Enclave outcomes into unconverted quests.** See the out-of-scope notes, "Emerald Enclave event rewrite (Session 43)" §1:
  - Faction Outposts: Manshoon Named, Splinter Site Reported, Traitor Identified, Imre Identified.
  - Xanathar's Lair: Pier 17 Investigated, as a casing aid at X4.
  - Kolat Towers: Imre Identified.
  - Vault of Dragons: Cultists Escaped, Anchor Destroyed, Illuun Contact, Brandath Crypts Visited, Jeryth's Message Received. It also needs an "if not run" default for M6 and a notice rule for Jeryth.
  - The Vault also needs an outcome for the Stone naming Illuun at Full Awakening.
- [ ] **Structure-doc Enclave lines:**
  - arc-e:85 (ward);
  - arc-f:59/:61 (the X1/X4 dock);
  - arc-g:535 (ley line "beneath Phaulkonmere" is in the wrong ward);
  - arc-j:47/:83/:274;
  - arc-h:128 (the Tarsakh 15 departure shifts Sarna's dates);
  - the Illuun descriptions in arc-c, arc-e and arc-h.
- [ ] **Act I–II Enclave lines:**
  - Trollskull ev-03:20, where the Tally–Melannor link now comes at the First Meeting;
  - the Fireball! and Gralhund Melannor hooks overlap s02 Surge One.
- [ ] **OotG M3 design notes** claim Splinter intel from Kelso that the event doesn't contain.
- [ ] **Notable Figures leftovers:**
  - the Harpers organization page and Bonnie's page say only Mattrim knows her nature;
  - Tally's page :8 lists M1;
  - Durnan's page uses the "Veteran" block;
  - Gerrick Thatchley has no page;
  - `appendix-a-npc-roster.md` is missing.
- [ ] **Confirm the readings** in out-of-scope §5:
  - r10 beast replaced once per campaign;
  - the M4 grell flee rule;
  - the r25 8th-level spell components;
  - the M6 *water breathing* scroll and condition texts.
- [ ] **Accept or replace the Session 43 invented names** (out-of-scope §6).
- [ ] **Voice profiles** for the recurring Enclave minor NPCs (Gerrick, Sarna Dath, Sorrel Hartwick), if the user asks.

### Carried forward from Session 42
- [ ] **Wire the Force Grey outcomes into unconverted quests** (out-of-scope "Force Grey event rewrite (Session 42)" §2):
  - Xanathar's Lair: Pool Destroyed, Placement Records Taken, Captive Freed, Nihiloor Fled, Nihiloor Identified Party.
  - Sea Maidens Faire: Zelifarn Contacted, Zelifarn Befriended, Submarine Reported, Offerings Returned / Kept.
  - Vault of Dragons: Vajra Briefed, Tower Attack Stopped, Splinter Testimony Recorded, Orvyn Ledger Delivered, Vira Caught / Escaped, Buried Thing Reported. It also needs gold-path outcome names for r50.
- [ ] **Act I–II Force Grey fixes:**
  - Trollskull ev-04:79, :109-110 (Force Grey Joined flag), :31, :61;
  - ev-05:55, :83 (Meloon Met flag, to become an Event Outcome);
  - ev-06:73;
  - Trollskull design-notes:49;
  - notable-patrons :55, :57, :61;
  - Gralhund ev-01:94.
- [ ] **Structure-doc Force Grey lines:** arc-b :145, :367; arc-e :377; arc-f :39; arc-g :43, :537; arc-i :41; arc-j :41, :51.
- [ ] **BD M3 `ev-01-three-nights.md:287`** devourer brain line.
- [ ] **Harper M5 ev-02** should read **Pool Destroyed**.
- [ ] **Notable Figures leftovers (Force Grey):**
  - Laeral :8;
  - Durnan :12/:26 "rarely says two words";
  - Orvyn Dall has no page or voice;
  - Vajra, Meloon, Nihiloor and Hlam still use `> **[GM]**`.
- [ ] **Accept or replace the Session 42 invented names.**
- [ ] **Voice profiles for Force Grey minor NPCs**, if asked.

### Carried forward from Session 41 and earlier
- [ ] **Answer the four Session 41 Harper decisions** in the out-of-scope notes. Decision 3, Enclave M3 vs Harper M3 on Bonnie, is now settled by this session's Bonnie ruling.
- [ ] **Wire the Harper outcomes into unconverted quests.**
- [ ] **Trollskull ev-04:97-98**, the party-level Harpers Joined; also the other True/False Joined headings at ev-04:100-110.
- [ ] **Act I–II Harper lines:** Remallia (Trollskull ev-04:91, Fireball ev-02:96, staff guide :84); Trollskull ev-07:51, ev-04:71; Saeth Cromley (Fireball ev-01:37).
- [ ] **Structure docs (Harper):** arc-e:495, arc-f:31, arc-i:19/247/265, arc-i:75-77, arc-j:43.
- [ ] **Notable Figures (Harper):** Ahmaergo `02:6`, Remallia `02:6`, Variel `06:8`, and Mattrim as "the only person" who knows about Bonnie.
- [ ] **Accept or replace the Session 41 invented names.**
- [ ] **Clarity/voice pass on the remaining factions**; **DR clarity polish** (deferred).
- [ ] **BD items:**
  - M6 harbor naming;
  - r25 dead branch;
  - guide 08:33;
  - the remaining BD decisions;
  - BD outcome readers and writers;
  - BD companion pages;
  - Act I–II BD contradictions;
  - BD and DR invented names (Ilmra, Odalys and Ilsa collide).
- [ ] **Voice profile for J.B. Nevercott.**
- [ ] **OotG M3** wererat silver rule.
- [ ] **SOURCE_GUIDE:219**; arc-j :55/:75/:322; arc-h :9/:71.
- [ ] **Faction Outposts writes:** Yellowspire Ledger/Letters Taken, Clean Exit, Manshoon Named, Yellowspire Raided. 5B must add the relay ledger and coded letters.
- [ ] **Kolat Towers outcomes:** Vevette, the K18 rune, the DR parallel result.
- [ ] **Gralhund:** Floxin Status becomes named outcomes.
- [ ] **Sea Maidens Faire:** read Soluun's fate.
- [ ] **DR outcomes and companion pages:**
  - wire the DR outcomes into arc-e through arc-j;
  - fix guide 07, org page 06, the Notable Figures pages, `structural-rules.md:9` and `player-factions-overview.md:186`;
  - fix the Act I–II DR contradictions;
  - accept or replace the DR invented names;
  - settle Renown 25/50 reachability for all factions;
  - voice profiles for recurring minor DR NPCs;
  - confirm the three viewer changes.
- [ ] **The six decisions** in "Decisions Needed Before Fixing".
- [ ] **One-faction membership wording** on four guide pages.
- [ ] **Voice profiles for minor Harper NPCs.**
- [ ] **Remaining non-rule inconsistencies:** Finding Floon "two nights", Gralhund "two tendays", Vajra, Istrid's loan.
- [ ] **Ember styling on the live site**, and convert the `[GM]` zones in Finding Floon and Trollskull.
- [ ] **Bestiary.** Nihiloor's block is in `force-grey-mechanics-reference.md` §4.
- [ ] **Convert arc-e through arc-j.**
- [ ] **Guides and setting:** prose pass on the guides and setting pages; Notable Figures polish; recheck the M5/M6 summaries on the other organization pages.
- [ ] **Misc carried items:**
  - `sources/backgrounds.json`;
  - BD ev-03 Ryvarra;
  - sidebar titles;
  - Renaer's Confidence holder;
  - Ember organizations JSON;
  - Trollskull Founders' Day;
  - Asmodean Shrine Area 3;
  - `#### Milestone: None` in the other factions;
  - DR Viper muscle;
  - earlier invented details.
- [ ] **Remaining faction rewrite: Order of the Gauntlet**, using the Session 41–44 method.
- [ ] **Older items:** voice-run tooling portability, reproducible global skills, legacy automation references, the Astra/Sol defaults, the Harper private Site.

---

## Warnings and Caveats

- **The temp-index tool is scratchpad-only.** `scratchpad/tools/commit-excluding.sh` commits from a temporary index, holding chosen paths at master's version, and it dies with the container. After using it, always run `git reset -q` before any ordinary `git add`/`git commit`. The real index is left stale, and a plain commit from it reverts files; that is exactly what PR #153 did.
- **`scratchpad/tools/sentlist.py`** (lists GM or readaloud sentences of 7 words or fewer, or 29 or more, with line numbers) is also scratchpad-only.
- **The drafters cannot run voicecheck,** and their passes often overshoot: speech splits create short GM sentences, and joins create 30+ word ones. Send split-only or join-only passes with exact line lists, then measure.
- **The rewrite's first-commit input and PREV copy** are in the scratchpad (`la-orig/`, `la-prev/`) and die with the container. Use `git show 67d36b2:<path>` (missions) or `git log --follow` for history.
- **The plan's verification grep for "Milestone"** must except "awards no Milestone Points".
- **The Lords' Alliance and Emerald Enclave M6s** both run after Kolat Towers, and three-heist parties play them after the Vault. The Vault conversion must handle both defaults.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md. If the user names the Order of the Gauntlet rewrite (the last faction left), follow the Session 41–44 method. Use `docs/plans/lords-alliance-*` as the newest template for the brief, instructions, mechanics reference and rulings. Merge each document the moment its agent finishes, recompute every encounter band yourself on the plain table, and make sure every contact has an in-fiction summons. For further LA work, read `docs/plans/lords-alliance-conversion-brief.md` and the "Lords' Alliance event rewrite (Session 44)" section of `docs/plans/harpers-out-of-scope-notes.md` first. Otherwise wait for the user to name the next task.
