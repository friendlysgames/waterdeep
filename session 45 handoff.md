# Session 45 Handoff
**Date:** 2026-11-05
**Status:** Ready to continue

---

## What Was Done

The Order of the Gauntlet, the last of the seven player factions, was rewritten from scratch with the Session 41–44 method. All 13 folders (First Meeting, M1–M6 with M2 and M4 split into two events, s01 The Tithe, s02 Savra's Past, and r03/r10/r25/r50) were restored to their first commits, researched by five agents, planned, briefed, drafted, voice-passed, consistency-checked and merged in PRs #157–#180. The companion pages (Factions Guide, organization page, Notable Figures, guide rank rows, Trollskull, structure docs, Cassalanters guide, Bregan D'aerthe Wazoo lines) were aligned, and the readers still to wire in unconverted quests are logged. All seven faction event sets are now on the new model.

---

## Changes Made

Git range: `af0247a..HEAD` (25 first-parent merges, 81 files, +7,935 / −1,326).

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/quests/faction-events/order-of-the-gauntlet/**` (13 folders) | Full rewrite on the page model: Ember blocks, Event Outcomes, base renown plus three listed +1s on the shared ladder (R1/3/5/8/10/13, M6 after Kolat Towers), per-member rank procedures, Savra at the door, Quietly Reassigned, suspicion-only Cassalanter content, 2024 stat blocks, and a design-notes page per folder. |
| `campaign/guides/factions/05-order-of-the-gauntlet.md`, `setting/organizations/04-order-of-the-gauntlet.md` | Gates, stance, hooks, ranks, tithe and Quietly Reassigned rules, suspicion-grade mission table; the org page is lore only. |
| `setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md`, `02-sister-valdra.md` | Savra Lawful Good Human, three years in the Howling Hatred; Valdra unofficial and in no event. |
| `guides/players-guide/faction-affiliations.md`, `guides/gm-guide/player-factions-overview.md` | Order rows and rank rows. |
| `quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md`, `guides/trollskull-manor/02, 03` | Order row: any unaffiliated character, plain Joined note, 100 gp renovation; Valdra's renown line removed. |
| `structure/arc-e, arc-g, arc-i, arc-j`; `locations/cassalanter-villa/15-family-crypt.md`; `guides/factions/11-cassalanters.md` | Fifth path to the Aveen Street shrine, Siamorphe symbol from the M5 chaplain, Ardin's lay on hands, Order Recognized default, Cultist Fanatic. |
| `quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/*` | Source is Corisande Brisenne; reads Black Viper Source Noted. |
| 11 Doom Raiders and Lords' Alliance files | "Hall of Justice" to "Halls of Justice". |
| `setting/waterdeep-lore.md`, `notable-figures/city-officials/03-saeth-cromley.md`, `cassalanters/10-seffia-naelryke.md`, `independents-adversaries/03-kelso-fiddlewick.md` | Castle Ward temple of Tyr; Featured-in lists; Cultist Fanatic; Danika a victim, not in the gang. |
| `docs/plans/harpers-out-of-scope-notes.md`; `emerald-enclave/m03-the-doppelganger-problem/design-notes.md` | New Session 45 section; phantom Kelso Splinter-intel lines deleted. |

### Files Created
| File | Purpose |
|------|---------|
| `docs/plans/order-of-the-gauntlet-research/00`–`05` | Brief and five research reports. |
| `docs/plans/order-of-the-gauntlet-plan.md` | Approved plan. |
| `docs/plans/order-of-the-gauntlet-conversion-brief.md` | Binding brief: rulings, defaults, ladder, outcome table, per-folder briefs. |
| `docs/plans/order-of-the-gauntlet-drafter-instructions.md` | Drafter rules with numeric voice ranges. |
| `docs/plans/order-of-the-gauntlet-mechanics-reference.md` | CR 2.0 rosters at 3/4/5 PCs; ally rules; fixed tables. Numbers recomputed by the main session. |
| `docs/plans/order-of-the-gauntlet-consistency-rulings.md` | 41 findings with rulings and dispatch. |
| New event and design-notes files | M2 and M4 second events (`m04/ev-01-twelvedog-court.md`, `ev-02-what-gysheer-carried.md`), design notes in every folder. |

### Files Deleted
| File | Reason |
|------|--------|
| `m04.../ev-01-spined-devils-in-twelvedog-court.md` | Replaced by the two-event M4. |

---

## Key Decisions

### Valdra stays unofficial
**Decision:** She appears in none of the seven events that scripted her. s01 reassignment runs through the clerk Brother Hallin Ostrel; the r50 investiture is by the high priest of Tyr.
**Reasoning:** Her Notable Figures page, the organization page and the staff guide all make her unofficial and unknown to Savra.
> "Stays unofficial (Recommended)" — User, this session

### M2 uses an alias and a raven imp
**Decision:** The tea-house contact is the household secretary Corisande Brisenne; windmill Seffia stays for Faction Outposts. The watcher is an imp in raven form with its sender unproven. "What are they moving?" is paid off in M4 by a cartage receipt.
> "Alias + raven imp (Recommended)" — User, this session

### M6 enforcer: the Horned Devil with Savra fighting
**Decision:** The CR 11 Horned Devil stays, with Savra and (at three characters) both Priests fighting. Enemies never focus a single PC, so no first-turn-KO +4 applies.
**Reasoning:** The main session recomputed the bands (Savra only: 72% Brutal, 45% Bloody, 31% Bruising at 3/4/5; with both Priests at 3: 42.7% Bloody).
> "but our tactics will always be 'never focus a single PC'" — User, this session

### M5 hybrid shrine (default, not overruled)
**Decision:** The Field Ward chandler's cellar is the street entrance to the canonical Aveen Street shrine; M4 and M5 are a fifth independent path to it. The ledger has twelve dated entries with no terms; Founders' Day never moves; the Cassalanters step up one escalation tier.
> "M5... by now Cassalanters should be discovered or close to, right?" — User, this session

### Defaults accepted from the plan (the user did not overrule them)
- Gates R1/3/5/8/10/13 with M6 after Kolat Towers; base renown 2/2/3/3/4/4 plus three +1s.
- Per-candidate First Meeting with no Offer Closed outcome; 100 gp renovation help.
- Tithe is 25% of each member's own share of a 1,000 gp haul, +1 once if paid before Savra's dusk knock on day 2.
- The Order has no suspension or dismissal; only Quietly Reassigned.
- Savra three years in the cult, left about three years ago; Lawful Good Human; never held Righteous Hand.
- Siamorphe symbol from the M5 chaplain, r10 as fallback.

---

## Rules and Instructions

All earlier rules stay in force. Added or reinforced this session:

- **Enemies never focus a single PC.** No first-turn-KO adjustment applies to Order fights. *(User: "our tactics will always be 'never focus a single PC'")*
- **Run the numbers yourself.** The user asked "did you run the numbers?" about the M6 enforcer; the main session recomputed every verdict on the plain tier-adjusted table and matched the stats to the 2024 data before any drafter used them.
- **Parallelize independent work.** The user asked "did you really have to only do a singular agent?". Start independent folders while one gating job (here the mechanics reference) runs. Keep at most five agents.
- **A PR merges the whole branch.** Stage by explicit path and expect checkpoint commits to ride along; keep unfinished drafts off master where possible.
- **Handoff only on `/handoff`.** Do not announce it as an automatic last step.

---

## Problems Solved

- **A 405 on PR merge:** master had merge commits the branch lacked. Merge `origin/master` into the branch, push, wait for the PR to read clean, then retry.
- **Rate limits (twice):** agents were resumed with SendMessage after each reset; no work was taken over inline.
- **Agent cap:** briefly six agents ran when two rhythm passes were resumed without counting; nothing was lost.
- **Phantom note:** the Kelso Splinter-intel claim in the out-of-scope notes and the Enclave M3 design notes was never in the Order M3 notes; both lines deleted.
- **A bulk sed** turned an open item in s02's design notes into a self-contradicting line; rewritten as resolved.

---

## Outstanding Work

### New this session
- [ ] **Wire the Order outcomes into unconverted quests** (out-of-scope "Order of the Gauntlet event rewrite (Session 45)" §1): Faction Outposts (Splinter Intel Reported, Pell's Debt Held, a Pell beat, "Trade Ward" at arc-e :117/:201/:301), Xanathar's Lair (Savra outside the entrance), Cassalanter Villa ("if not run" readers, an orientation check for the r10 dossier), Kolat Towers (Ardin, the gate for M6), the Vault (Order Recognized default, the three tithe outcomes, tone-only today), Dungeon of the Mad Mage (Righteous Hand Reached, Undermountain Mandate Accepted).
- [ ] **Confirm the Session 45 readings** (§4): Night 1 raven DC 14; the M4 Location use with no key and no check; the Marcheon 2:1 refusal rule against the guide; r10 dossier dates from 1480 DR; the writ honored in Waterdeep, Neverwinter, Baldur's Gate and Daggerford; M6 Hard triggers.
- [ ] **Verify unchecked rules** (§6): a generic +1 weapon is not in `items.json` (the r25 nine-weapon table), the Howling Hatred ranks, *Spirit Guardians* and *Hallow* wording, *Resurrection* revival rules, the Zone of Truth scroll.
- [ ] **Accept or replace the Session 45 invented names** (§5), including the "Brother" cluster (Haldric, Hallin, Osric, Teodric).
- [ ] **Other-file leftovers** (§3): Fireball! ev-01:194 against arc-c:98; Appendix B:402; "Cult Fanatic" in other pages; arc-j :258; arc-h:39 and arc-i Gondafrey threads; M2/M3/s02/M5 design notes still list the neutral-good fix as open.
- [ ] **Voice residue** (§7): table-heavy Factions Guide `05` and org page `04`; M5 narration at 21.9; no voice profiles for the Order's recurring minor NPCs.
- [ ] **Do the Order outcomes need a Campaign Viewer check?** The Pages workflow rebuilds on every merge touching `campaign/**` or `docs/**`; nobody has verified the deploy or the new pages' rendering.

### Carried forward from earlier sessions
### Carried forward from Session 44 (Lords' Alliance)
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
- [ ] **Older items:** voice-run tooling portability, reproducible global skills, legacy automation references, the Astra/Sol defaults, the Harper private Site.

---

---

## Warnings and Caveats

- **Checkpoint commits ride in PRs.** PRs #173 onward carried partial files from running agents when they merged; the finished versions replaced them before the end of the session, and the final state was verified clean by grep.
- **Scratchpad-only tools** die with the container: `scratchpad/tools/sentlist.py` (lists GM sentences of 7 words or fewer and 29 or more with line numbers), `scratchpad/5e/` (2024 rules data from the 5etools mirror-3), `scratchpad/ootg-orig`, `ootg-prev`, `docx-text`. The first-commit drafts remain recoverable with `git log --follow --diff-filter=A`.
- **`voicecheck.py` flags "Quietly Reassigned"** as a hedge tell; it is a fixed outcome name read across files, so leave it.
- **The out-of-scope notes now hold sections for all seven factions.** Read the Order section and the Lords' Alliance section before touching the Vault, Kolat Towers or Cassalanter Villa.
- **Drafters cannot run `voicecheck.py`.** Expect an overshoot after rhythm passes (M4's second event went to 23.5-word narration before a trim); send split-only or join-only passes with exact line lists, then measure.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md. All seven faction event sets are rewritten, so the next large block is converting the unconverted quests (Faction Outposts through the Vault of Dragons, arc-e to arc-j) and wiring the readers listed in `docs/plans/harpers-out-of-scope-notes.md`; start with that file's Session 45, 44 and 43 sections. Wait for the user to name the task. For further Order work read `docs/plans/order-of-the-gauntlet-conversion-brief.md` and the consistency rulings first.
