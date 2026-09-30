# Session 38 Handoff
**Date:** 2026-09-30
**Status:** Ready to continue. The Doom Raiders faction events are converted and merged, and three viewer fixes are live.

---

## What Was Done

This session converted all 12 Doom Raiders faction-event folders from rough drafts into finished Ember-voice adventure text, the same way the Harper events were done in Sessions 35 and 37.

- **Restore.** Every file first went back to the commit that created it. The Session 34 reset had never reached this repo, so the files were still carrying the old D1–D3 voice-run text.
- **Research and planning.** Five Sonnet 5.5 research agents fed a plan that the user approved. That plan is saved as the brief in `docs/plans/doom-raiders-conversion-brief.md`.
- **Mechanics.** CR 2.0 encounter numbers were checked against the real 2024 Monster Manual.
- **Drafting.** Every folder went to a `prose-drafter`, then through voicecheck and main-session review.
- **QA.** A consistency-checker pass found 8 blocking and 11 minor wiring errors, all of which were fixed.
- **Out-of-scope log.** Contradictions in files outside the folder were logged, not fixed.
- **Viewer.** The user then asked for three campaign viewer changes, all merged:
  - Opening a journal loads its first page.
  - Every page opens at the top.
  - Previous/Next buttons at the foot of each page.

PRs merged: [friendlysgames/waterdeep#40](https://github.com/friendlysgames/waterdeep/pull/40) (Doom Raiders) and [friendlysgames/waterdeep#41](https://github.com/friendlysgames/waterdeep/pull/41) (viewer).

---

## Changes Made

Git range: `git log ba31828..HEAD` (the base is the Session 37 handoff commit). There are 29 non-merge commits.

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/quests/faction-events/doom-raiders/**` (26 original files) | Each file was restored to its creation commit, then rewritten on the Harper page model. That means descriptive scenes, member-only briefs and renown, named Event Outcomes, 2024 stat blocks, the **Manshoon Named** gate, source beats restored from Appendix C/WDH, and the Mechanics Reference rosters. |
| `doom-raiders/00-first-meeting/ev-01-first-meeting.md` | Late additions at the user's request: a "The Large Man" GM sidebar says Davil's "large man who behaves as if every room belongs to him" is Urstul Floxin. A "Durnan and the Doom Raiders" GM sidebar, plus Davil and Yagra qna answers, explains why Durnan tolerates the cell at the Portal. |
| `doom-raiders/m01-the-dockside-killer/*` | Late addition: Heldar is canon as a paid companion along the waterfront, bad enough at it that clients ask for their money back. |
| `doom-raiders/s01-davils-arrest/*` | Late additions: Tashlyn tells members aloud about the three legal routes to free Davil. The event reads Gralhund's **Floxin Status**; if Floxin is Dead or Captured, someone above him gives the orders. |
| `doom-raiders/{m04,s02,r03,r25,r50}/*` | Late sweep: in-fiction "Floxin's cell" became "the other cell" / "the Splinter", with a GM **Floxin Status** rule in each event. |
| `doom-raiders/m05-the-yellowspire-job/*` | Late scope change: if **Yellowspire Raided** is marked, the mission runs only the new debrief page. The reinforced return visit is cut. |
| `doom-raiders/m06-zirajis-last-hunt/*` | Late fixes: Corellon's Crown is a two-minute walk (same alley as the manor), and the timeline was rebuilt. The mission reads the Kolat Towers results (Manshoon operational?, Vevette, the K18 rune, the Doom Raiders' parallel operation). |
| `.claude/skills/update-campaign-viewer/references/viewer-template.html` | `openJournal` always loads a page. New `resetPaneScroll` and `renderPageNav` (Previous/Next), plus `.page-nav` CSS. |
| `docs/index.html` | Rebuilt from the template. |
| `docs/plans/harpers-out-of-scope-notes.md` | Adds a "Doom Raiders event rewrite (Session 38)" section: missing readers and writers, guide/setting contradictions, source discrepancies, invented names. |

### Files Created
| File | Purpose |
|------|---------|
| `doom-raiders/{00-first-meeting,s01,s02,r03,r10,r25,r50}/design-notes.md` | Design notes for the 7 folders that had none |
| `doom-raiders/m04-silencing-skeemo/ev-03-the-reckoning.md` | New third M4 event (cornered Skeemo, double-agent gambit, capture, accident staging, debrief) |
| `docs/plans/doom-raiders-conversion-brief.md` | Approved plan and conversion spec, plus per-folder source facts |
| `doom-raiders/m05-the-yellowspire-job/ev-02-the-debrief.md` | Debrief-only page for parties who already raided Yellowspire in Faction Outposts; still sets Force Field Gap Intel |
| `docs/plans/doom-raiders-mechanics-reference.md` | CR 2.0 rosters and thresholds for 3/4/5 combatants, checked against the 5etools-mirror-3 2024 Monster Manual and 2024 spell data |

---

## Key Decisions

### Restore before anything else
**Decision:** All 26 Doom Raiders files went back to their first commits before the conversion began:
- `7752363` for 22 files;
- `b55fa75` for r03;
- `4801be8` for r10, r25 and r50.

**Reasoning:** The user asked for it, and research done before the restore was out of order.
> "first, return each file in the doom raiders folder to the stage they were in when they were first commited" / "that should have been done before any research & stuff" — User, this session

### Manshoon is gated on **Manshoon Named**
**Decision:** Doom Raiders believe Floxin leads "the other cell". Doom Raider speech may name Manshoon, or call Kolat Towers his home, only when **Manshoon Named** is marked. It is meant to be set at the Faction Outposts Interrogation House. GM text may state the truth.
**Reasoning:** This answers Session 37's decision 2 for the Doom Raiders. The user chose the recommended option.

### Force Field Gap Intel moves from M6 to M5
**Decision:** Ziraj hands over his notes at Corellon's Crown after The Yellowspire Job. M6 becomes a post–Kolat Towers revenge hunt.
**Reasoning:** M6 is 7th level, which requires Kolat Towers to be done, yet its intel was read by Kolat Towers Scene 1. This answers Session 37's decision 6 for the Doom Raiders.

### Yellowspire in M5: debrief if already raided (supersedes "return visit")
**Decision:** If Faction Outposts 5B ran (**Yellowspire Raided**), M5 does not send the party back. It runs only **The Debrief**, where the members report to Davil's inner circle and Ziraj hands over his notes. Otherwise ev-01 runs the heist, set in the Castle Ward with Amath and her acolytes. This replaces the earlier "rebuilt and reinforced return visit" decision.
> "all the information from the yellowspire faction event will already be there if the party goes there as part of the outpost events first. In that case, the event gets a new page which is just a briefing with Davil and the rest" — User, this session

### Floxin is usually dead after Gralhund Villa
**Decision:** Doom Raiders events read Gralhund's **Floxin Status** (Alive / Dead / Captured). If he's Dead or Captured, Tashlyn tells members that the man they thought led the other cell is gone, yet the cell still moves under someone they can't name. Speech says "the other cell" rather than "Floxin's cell".
> "Floxin is likely dead by Davil's Arrest, as he likely got killed by the party in Gralhund Villa. That needs to be accounted for" — User, this session

### Late content rulings
- **Heldar:** canon as a bad paid companion. *("honestly hilarious and I think should be canonised" — User)*
- **Davil's Arrest:** players are told the legal routes in play. *("Davil's Arrest needs to tell the players that they can try to help Davil through legal means, otherwise they'd need to realise it themselves" — User)*
- **Durnan:** the First Meeting explains why he tolerates the Doom Raiders. *("why is Durnan allowing the Doom Raiders to operate from his very well established and very famous tavern?" — User)*
- **Fala:** her shop is in the same alley as Trollskull Manor, so M6 travel is minutes, not a quarter hour.
- **Kolat Towers:** M6 must read the Kolat Towers results. *(User)*
- **Soluun:** if he survives M1, Jarlaxle must decide his fate, most likely expelling him. This is logged as out of scope.

### Events only; log the rest
**Decision:** Only the Doom Raiders event files were edited. Contradictions in guides, setting pages, other quests and arc docs went into the out-of-scope notes.

### Gates and renown match the Harpers
**Decision:** Mission gates are:

| Mission | Gate |
|---|---|
| M1 | Joining, at 2nd level |
| M2 | Renown 3, 3rd level |
| M3 | Renown 5, 4th level |
| M4 | Renown 8, 5th level |
| M5 | Renown 10, 6th level |
| M6 | Renown 13, 7th level |

Base Renown is 2/2/3/3/4/4.
**Reasoning:** The old gates (R2/3/6/9/12) couldn't be reached from a Renown 1 start.

### Source wins over drafts
**Decision:** Where the draft and Appendix C, WDH or a Notable Figures page disagreed, the source won:
- M1: the *Blood Wedding* playbill.
- M2: Rallygar's death.
- M3: the Emmek/Istrid money.
- M4: Skeemo's double-agent gambit.
- Soluun's disownment as a cover story.
- Amath as a **Priest**.
- Yellowspire in the Castle Ward.

**Renamed outcome:** M5's outcome became **Relay Ledger Recovered**, because Order of the Gauntlet M5 already uses **Ledger Recovered**.

### Viewer behaviour
**Decision:** The viewer now does three things.
- Opening a journal always loads its first page, or the deep-linked page, at every width.
- Every page load resets the scroll to the top.
- Previous/Next buttons walk the current journal in page-list order.
> "Whenever you select a new Journal, its first page should automatically be loaded" / "Whenever a page is loaded, its scroll position is automatically set to init/start/top/zero" / "add navigation buttons at the bottom of a page. Next and previous" — User, this session

---

## Rules and Instructions

All earlier rules stay in force (CLAUDE.md and Sessions 35–37). Reinforced or added this session:

- **Restore first, then research.** When the user asks for a restore, do it before any research or planning. If plan mode blocks it, get the restore approved on its own first.
- **Research agents are Sonnet 5.5.** Use the pinned project agents: `source-researcher`, `prose-drafter`, `encounter-builder`, `consistency-checker`, `rules-lookup`. *("make sure they're all sonnet 5.5 agents" — User)*
- **Speech floor.** Speech must average at least 12 words a sentence and narration at least 18. The Session 37 rule was enforced on every folder, and three drafts went back for it. Terse characters are played by what they withhold, not by fragments.
- **2024 stat names only.** Thug and Veteran don't exist in 2024. Use Tough and Warrior Veteran. There is no 2024 Bard, so Agorn Fuoco is a non-combatant.
- **Rules lookups.** The 5etools mirror moved to `5etools-mirror-3/5etools-src`, for example `data/bestiary/bestiary-xmm.json`. WebFetch truncates these files, so download them with curl and extract with Python, then hand the agent the extract.
- **Rate limits.** When an agent stops on the account-wide limit, resume the same agent with SendMessage after the reset. This was done for four agents this session.

---

## Problems Solved

- **Premature research:** Research ran before the restore because plan mode blocked edits. The restore was then approved and done on its own, as `68c2acd`.
- **rules-lookup couldn't reach its repo:** It returned 404 on `5etools-mirror-2`. Found `5etools-mirror-3/5etools-src`, then downloaded and extracted the XMM records locally.
- **Mechanics from memory:** The encounter-builder's first pass had no stat source. It was re-verified against the 2024 records; CRs held, and stat details, spell lists and first-turn-KO caveats were corrected.
- **Short speech:** s01 (6.6), M3 (11.0) and M6 (10.9) were sent back and now sit at 13–17. r25's narration went from 16.6 to 22.2.
- **Main-session voicecheck fixes:** TELLs in the First Meeting, M4 (three "quietly"), r03 and r50.
- **Black snakes:** s01 gave the Doom Raiders black flying snakes, which are Floxin's signature. They're now silvery or plain.
- **Wiring errors from the consistency pass:**
  - Readers that didn't use outcome names.
  - Davil Released and Skeemo's fate outcomes that nobody read.
  - Ziraj's favour contradicting itself between M6 and r25.
  - M2's Warned/Delivered conflict.
  - M4's dray rule and timeline.
  - r50's third-floor suite.
  - Tashlyn's "one day".
- **Viewer on phones:** Opening a journal only showed the page list; it now loads the first page.

---

## Outstanding Work

### New this session
- [ ] **Faction Outposts must write Yellowspire Ledger Taken, Yellowspire Letters Taken and Yellowspire Clean Exit,** and 5B must add a relay ledger and coded letters to Yellowspire, for M5's debrief to pay out.
- [ ] **Kolat Towers must name** Vevette's fate, the K18 rune and the Doom Raiders' parallel-operation result as outcomes, since M6 reads them. M6's design notes have the list.
- [ ] **Gralhund Villa's Floxin Status flag** should become named Event Outcomes. The Doom Raiders events read it.
- [ ] **Settle Soluun's fate with Jarlaxle** if Soluun survives M1, in Sea Maidens Faire and the Bregan D'aerthe missions.
- [ ] **Faction Outposts must write Manshoon Named and Yellowspire Raided** when arc-e is converted. Doom Raider events already read both. See the out-of-scope notes, "Doom Raiders event rewrite".
- [ ] **Wire the Doom Raiders outcomes into their readers** when each arc doc is converted:
  - arc-e: Seven Masks Lead, Shard Shunners Goodwill, Dasher Location Given Up.
  - arc-f: Tashlyn Contact, Davil Released.
  - arc-g: Poison Delivered, Esvele Warned.
  - arc-h: Soluun Captured/Escaped/Killed.
  - arc-i: Force Field Gap Intel from M5, Relay Ledger Recovered, Vevette Letters Recovered, Yellowspire Alarm Sounded/Circle Destroyed, Skeemo at Kolat Towers.
  - arc-j: the Ziraj and Splinter outcomes, the Skeemo fates, Vault Partnership Agreed.
- [ ] **Fix the Doom Raiders companion pages**, once the user widens scope:
  - guide 07 (Manshoon lines, Skeemo timing, M6 diagram, availability column, Yagra Courteous flag, Viper "veteran");
  - organization page 06;
  - the Davil, Yagra, Skeemo, Tashlyn, Kelso and Floxin Notable Figures pages;
  - `structural-rules.md:9` and `player-factions-overview.md:186`.

  This supersedes Session 37's "write the Floxin belief into the Doom Raiders" item. The events now carry it; these pages don't.
- [ ] **Act I–II Doom Raiders contradictions:**
  - Finding Floon ev-01:115, where Yagra Courteous is still a flag.
  - Trollskull ev-04: the 400 gp loan, flags, a party-wide Joined.
  - Fireball ev-01:204: "Manshoon's blade".
  - Gralhund ev-01 and ev-09: flags, and the "Keep a low profile" line.
- [ ] **Accept or replace the invented names:**
  - Dunfell, Hallowell, Ondra Kell;
  - Wenna Tarrow and the r10 specialists;
  - the r25 crews and informants;
  - Toben Ash, and more.

  The full list is at the end of the out-of-scope notes.
- [ ] **Renown 25 and 50** can't be reached from mission base awards, which total 19. Decide where the rest comes from, for the Doom Raiders and for the other factions.
- [ ] **Voice profiles for recurring minor Doom Raiders NPCs**, if they recur: Dunfell, Wenna Tarrow, Brannoc Hale, Ondra Kell and others. Each folder's design notes list them.
- [ ] **Confirm the three viewer changes** on the live GitHub Pages site. A hard refresh may be needed.

### Carried forward from Session 37
- [ ] **Answer the six decisions** at the end of `docs/plans/harpers-out-of-scope-notes.md`. For the Doom Raiders, decision 2 was answered with Manshoon Named and decision 6 by moving the intel to M5. They are still open for the other factions.

  Then fix the findings one faction or area at a time, with agents.
- [ ] **One-faction membership.** Four guide pages still allow a PC in several factions: `players-guide/faction-affiliations.md:3`, `gm-guide/player-factions-overview.md:3`, `factions/01-overview.md:7, :9` and `trollskull-manor/02-operating-costs.md:31`.
- [ ] **Wire the Harper outcomes** into their named readers when each lair doc is converted.
- [ ] **Minor Harper NPCs** have no voice profiles or Notable Figures pages: Uza, Tessalar, Orren, Harl Keen, Nella, Orin and others.
- [ ] **Remaining non-rule inconsistencies:**
  - the Finding Floon "two nights" and Gralhund "two tendays" timeline slips;
  - Vajra's alignment and origin;
  - Istrid's loan;
  - Yellowspire's ward (resolved in the Doom Raiders events as the Castle Ward);
  - BD mission numbering;
  - the coin-pouch timing.
- [ ] **Confirm the Ember styling** on the live GitHub Pages site: fonts, block frames, phone layout.
- [ ] **Artifact publishing:** if `update-campaign-viewer` is used again, publish `ember.css` and `assets/` through the Artifact `files` map.
- [ ] **Old GM zones:** Finding Floon and Trollskull Alley pages still use `> **[GM]**` and need converting to the Ember block model.

### Carried forward from Sessions 29–31
- [ ] Verify that the previously deployed Pages URL works for the user after the stale-cache report.
- [ ] **Bestiary:** never drafted (Xanathar two-phase, Victoro and Ammalia, Aurinax).
- [ ] Convert the remaining structure docs into journals: Faction Outposts, Xanathar's Lair, Cassalanter Villa, Sea Maidens Faire, Kolat Towers and Vault of Dragons. Vault of Dragons needs a Scene 6 debrief if Xanathar is GONE.
- [ ] Guides and setting prose pass: the Trollskull Manor Guide, and setting lore, history, grand-game, villains, organizations and Notable Figures.
- [ ] Prose-polish the word-for-word NPC profile text in Notable Figures.
- [ ] Recheck the Mission 5/6 summaries on organization pages against the Factions Guide.
- [ ] Resolve the missing `sources/backgrounds.json` and verify Heroes of Faerûn background names.
- [ ] Confirm the intended BD `ev-03` Ryvarra visibility under individual membership.
- [ ] Normalize older faction-mission sidebar titles to `> [!type]**Title**` outside the Harper and Doom Raiders folders.
- [ ] Recheck the GM Renaer's Confidence Holder framing against the rewritten GM pages.

### Carried forward from Session 32
- [ ] Ask for the ephemeral Ember organizations JSON again when the organizations lore pass starts.
- [ ] Reconcile the BD guide `08-bregan-daerthe.md` Renown 5+ *Scarlet Marpenoth* extraction with the rank thresholds 3/10/25/50.
- [ ] Reconcile the BD M6 limpet-charge / Eye #3 wreck summary, and the North Ward versus Southern Ward windmill location.
- [ ] Check the Trollskull Manor Guide `01-overview.md` Founders' Day wording against the Structural Rules calendar.
- [ ] Add the missing keyed Area 3 in the Asmodean Shrine, and check the Samara and Illuun Notable Figures pages.
- [ ] Decide whether to remove the remaining `#### Milestone: None` blocks in the other factions' m01–m06 events. The Harper and Doom Raiders events no longer have them.
- [ ] **Doom Raiders Viper muscle (partly resolved):** r10 now uses a Warrior Veteran with named swaps for Yagra. Her Notable Figures page still says Thug.
- [ ] Accept or replace the earlier invented details:
  - Lords' Alliance: Sevel Dastar.
  - Force Grey: Aldris Maeven, Rhendar Solne, Merris.
  - Bregan D'aerthe: Ilphrin Quiss, Pelsha and Vorn, Sarev Oust.
  - Order of the Gauntlet: Tobrin.
  - Emerald Enclave: Sarna Dath, Bertio Caskwall.
  - Savra's cult and Howling Hatred ranks.
  - The three near-parallel Renown 50 Mad Mage choices.

### Carried forward from Sessions 33–35
- [ ] **Remaining faction rewrites:** the Harpers and Doom Raiders are done. Next are the Lords' Alliance, Emerald Enclave, Order of the Gauntlet, Force Grey and Bregan D'aerthe, one approved plan at a time. Use the Session 38 method: restore, research, brief, mechanics reference, drafters, QA pass.
- [ ] If the historical voice-run tooling is kept, make `.claude/briefs/voice-run/qa_batch.py` portable.
- [ ] Make the imported global skills reproducible on another machine, if requested.
- [ ] Review the conceptual-only legacy automation references before using them.
- [ ] Recheck the inherited Session 32 items against each later faction rewrite before closing them.
- [ ] If the user picks a permanent Astra/Sol or Sol/Low setup, update the saved defaults and orchestration docs together.
- [ ] Verify the Harper private Site on the user's signed-in phone. It is stale until rebuilt.

---

## Warnings and Caveats

- **Nothing reads the new outcomes yet.** Doom Raider events reference outcomes that nothing sets (**Manshoon Named**, **Yellowspire Raided**) and name readers in unconverted arc docs. Until arc-e to arc-j are converted, a GM must mark **Manshoon Named** by hand when the party learns the name.
- **Drafter-invented details.** The Vault of Dragons Scene 1/5/6 effects in M6 and r50, and M5's ledger Advantage on the Kolat Towers recalibration check, are inventions to match or cut during those conversions.
- **Drafters never ran voicecheck.** They had no shell, so every folder was checked by the main session with `voicecheck.py` and the grep set. One flag remains: the arc-j path name "Keep it, quietly" in r50.
- **2024 stat data isn't in the repo.** The downloaded files were in the session scratchpad, so re-download them if needed.
- **The viewer check ran without the markdown renderer.** The CDN (`marked`) was blocked in the sandbox, so pages rendered as raw text. The nav, scroll and first-page behaviour was checked; the rendered look on the live site wasn't.
- **Rank-event branches depend on Davil Released.** r03 and r10 assume release terms 0–1 mean a sealed suite and the kitchen booth, which is how s02 defines them. A change to s02 has to carry through to r03, r10, r25 and M5.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md. Then open the end of `docs/plans/harpers-out-of-scope-notes.md`. It holds the six open decisions and the new "Doom Raiders event rewrite (Session 38)" section.

Wait for the user to name the next task, which is likely another faction rewrite or a companion-page fix. For a faction rewrite, follow the Session 38 method:
- Restore that faction's files to their first commits first.
- Research with the pinned Sonnet 5.5 agents.
- Write a brief and a mechanics reference, checked against the downloaded XMM data.
- Draft with at most five agents at once.
- Run voicecheck and grep checks, then a consistency pass.
- Commit per folder.
