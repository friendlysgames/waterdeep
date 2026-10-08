# Session 41 Handoff
**Date:** 2026-10-08
**Status:** Ready to continue

---

## What Was Done

The user rejected the Session 35/37 Harper faction events for their wording and internal structure. This session rewrote all 13 Harper folders from their first commits, on the Bregan D'aerthe / Doom Raiders page model.

**Method:**
- Five research agents produced reports, which were saved.
- The main session wrote a conversion brief and drafter instructions.
- An encounter-builder wrote a new Harper mechanics reference. It includes Nihiloor's custom Occupying Devourer, now also used by Force Grey.
- Prose-drafter agents drafted each folder.
- Each folder was voice-checked, rhythm-passed, PR'd and merged.

**Cleanup:**
- A consistency pass found 14 in-folder mismatches, all fixed.
- The companion pages (Factions Guide, organization page, Notable Figures) were fixed.
- Fireball ev-04 became the writer of **Jarlaxle Unmasked**.
- Every outside contradiction that remains is logged.

**Late follow-ups, at the user's request:**
- Every event now describes how the members are contacted, using one canonical paper bird.
- The First Meeting gained a detailed tailor scene, opera background, and a properly sociable public Mirt.

---

## Changes Made

Git range: `75c2dbd..HEAD` (Session 40 handoff to this handoff). PRs #86–#98, all merged to master.

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/quests/faction-events/harpers/**` (13 folders, 29 files) | Restored to first commits (`d9c9e96`), then rewritten from scratch on the DR/BD model, with design notes for every folder. Details per folder are in `docs/plans/harpers-conversion-brief.md`. |
| `harpers/00-first-meeting/ev-01-first-meeting.md` | Late addition: Seldo's Fine Stitches tailor scene, *The Fall of Tiamat* production block and three readalouds (no clue in them), Mirt's loud, profane public gear with a "Mirt's Gossip" block, and a sharp intermission switch to his business voice. |
| All Harper events with a contact | An arrival readaloud describing the canonical paper bird, Mirt in person, s01's plain note, or Remallia's silver raven. |
| `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/*`, `m04-destroy-the-intellect-factory/ev-01…, overview.md`, `m05-the-legates-eyes/*` | Wish is gone, replaced by the Occupying Devourer extraction procedure. Detection matches the reference. Meloon remembers what he saw while occupied. Devourer reports go through a Guild courier, because its telepathy reaches 60 ft. |
| `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md` | New "Who Zord Is" block (seller line on the ledgers, DC 14 History, or the BD cabin). It writes **Jarlaxle Unmasked** per character. |
| `campaign/quests/act-ii/fireball/ev-01-the-fireball.md`, `ev-06-the-death-mark.md` | Mirt's Cassalanter line is now suspicion, and his ev-06 warning no longer names Manshoon. |
| `campaign/guides/factions/02-harpers.md` | Fixes: one ticket per candidate; the Watcher lodging is kept by an intermediary; Wise Owl at Renown 25; one informant request per quest; the mission table; Manshoon knowledge removed; Cassalanter claim made into suspicion. |
| `campaign/setting/organizations/01-harpers.md` | Manshoon and Kolat Towers knowledge removed; Corene's timeline set to three weeks. |
| `campaign/setting/notable-figures/harpers/01-mirt.md`, `03-mattrim-mereg.md`, `04-bonnie.md`, `05-corene-wyldath.md`, `08-maxeene.md` | Mirt's stat line is now the WDH CR 9 block; Mattrim's "mission four" is now three; Bonnie's vault-key claim is cut; Corene gets the occupying devourer; Maxeene gets the white blaze and the Dock Ward stand. |
| `docs/plans/harpers-out-of-scope-notes.md` | New section "Harper event rewrite (Session 41)": outside readers, Act I–II, guide and structure contradictions, Emerald Enclave M3, four user decisions, invented names. |

### Files Created
| File | Purpose |
|------|---------|
| `docs/plans/harpers-research/01–05.md` | The five research reports: spec and structure, First Meeting/s01/ranks, M1–M3, M4–M6, consistency audit. |
| `docs/plans/harpers-conversion-brief.md` | User decisions, standing defaults, name fixes and per-folder briefs. Its Session 41 addendum holds the canonical paper bird and the tailor. |
| `docs/plans/harpers-drafter-instructions.md` | Binding rules for Harper drafters: DR model pages, page skeletons, hard rules, §2a voice ranges. |
| `docs/plans/harpers-mechanics-reference.md` | CR 2.0 audits for every Harper fight, the 2024 gazer, Mirt's ally block (WDH CR 9), Spy allies, and §5 Nihiloor's Occupying Devourer with its Hold/Break Extraction Procedure. |
| `harpers/{00-first-meeting,r03,r10,r25,r50,s01}/design-notes.md` | Design notes for the folders that lacked them. |
| `harpers/m05-the-sleeping-asset/ev-02-the-extraction.md` | M5 is split: ev-01 finds Corene, ev-02 covers the extraction and the mole. |
| `session 41 handoff.md` | This file. |

### Files Deleted
| File | Reason |
|------|--------|
| Six Harper design-notes files (00, r03, r10, r25, r50, s01) | Removed in the restore, because they first appeared in the Session 35 upload. They were recreated in the rewrite. |

---

## Key Decisions

### Rewrite the Harper events from first commits
**Decision:** Restore every Harper file to the commit that first added it, then write it from scratch after plan approval and research.
> "I want you to rewrite the Harpers events. Return them to their initial commit, then write them from scratch, entering plan mode first. use the research agents. check for inconsistencies with the other files. This is due to me not liking how they are worded and internal structure." — User

### BD/DR is the page model
**Decision:**
- Copy the finished Doom Raiders and Bregan D'aerthe page skeletons. DR is the voice model.
- The mission mini-arc maps the way BD/DR map it:
  - Hook becomes `### The Brief`.
  - Background becomes a What Is Actually True block.
  - The acts become named scenes.
  - The debrief and Mission Renown go in Renown Opportunities.
  - Aftermath comes last.
> "I just like the way we did BD and DR better" / "see how bd and dr do it" — User

### Keep settled facts
**Decision:** Keep the previous version's outcome names that have readers, its NPC renames, House Ulbrinter on Delzorin Street, Maxeene speaking Common, and the gates and renown. Scenes and prose are new. — User chose "Keep settled facts (Recommended)".

### Harper M6 stays at 7th level, after Kolat Towers
**Decision:**
- Mirt studies the fully awakened Stone before the Vault opens.
- The raid comes from Splinter survivors and branches on Kolat Towers' result.
- There is no Kolat escape, no Kolat reader and no Eye count. — User chose "Keep 7th, post-Kolat".

### Nihiloor's custom Occupying Devourer, in Force Grey too
**Decision:**
- The devourer keeps the host's brain alive and is forced out through Hold/Break: ward, magic or anchor routes, with Strain on failures. No Wish.
- It applies to Harper M5 and Force Grey M3–M5.
> "Custom devourer, and same for force gray" — User

### Fireball ev-04 writes Jarlaxle Unmasked
**Decision:**
- The Sea Maidens Faire event is where the party learns Zord's name (ledger seller line, or the BD cabin).
- Harper M4 reads the outcome. It writes it only on the unmarked branch.
- Bregan D'aerthe Renown inside a Harper mission is cut.
- This answers BD open decision 3 with "yes".
> "M4 happens by definition after Fireball" — User

### Contact objects and the First Meeting additions
**Decision:**
- One canonical Harper paper bird for every event (brief addendum).
- The First Meeting gets a detailed tailor scene, opera background with no clue in it, and two clearly different Mirt gears.
> "the missions overall could do with a description of the paper bird or whatever is being used to contact them. Also, the first meeting could do with a tailor scene, detailed, and some background descriptions of the play without it being integrated as relevant to the meeting" — User
> "allow mirt do be more social in the first meeting. show the difference between his two personas properly. jovial, funny, with a sailor's mouth, maybe some gossipping as well (nothing campaign relevant), then intermission and the change happens" — User

### Defaults settled without asking
These are recorded in the brief. They were derived from the research.

**Gates and rules**
- The **Manshoon Named** gate is adopted for the Harpers. They know only that "the Black Network has split".
- Gates run R3/L3 through R13/L7, with base renown 2/2/3/3/4/4.
- One writer per outcome.
- Remallia's Harper role stays hidden until M4.

**Mission content**
- **M1:** the source beats are restored (Davil and Yagra, credentials, Insight).
- **M2:** the gazer is a stray with no handler.
- **M3:** five doppelgangers, and only Bonnie can be recruited.
- **M4:** DC 24 identification.

**Renames to avoid collisions**

| Old name | New name |
|----------|----------|
| Orren Vale | Tobin Harrask |
| Dena Voss | Dena Holt |
| Joss Bell | Joss Marrin |
| Harl Keen | Wil Keen |
| Oswin Bell | Corin Bell |

**Places**
- Shield Street is in the Sea Ward, so the barber moves to Swords Street.
- No Harper rooms are on Saerdoun Street or Candle Lane.
- The High Harper persona gets its own vouchers.

---

## Rules and Instructions

All earlier rules stay in force. Added or reinforced this session:

- **Faction rewrite method (Harper run, Session 41):**
  1. Restore from the true first commits.
  2. Run five research agents and save their reports.
  3. Write the plan and get approval.
  4. Write the brief, drafter instructions and mechanics reference.
  5. Draft with `prose-drafter`, five agents at most at once.
  6. Run voicecheck. Send a rhythm pass back with numeric targets and an overshoot guard (no readaloud or GM sentence past ~28 words).
  7. PR and merge per folder.
  8. Run a consistency-checker pass, then apply its fixes.
  9. Write the out-of-scope log.
- **Drafters write speech too clipped.** Every Harper drafter produced speech averaging 8.7–10 words against the 11–15 target. One correction overshot to 26-word narration. Tell drafters up front that Mirt's business voice is plain but uses full 10–15-word sentences. When sending a rhythm fix back, give both the floor and the ceiling.
- **Canonical Harper paper bird** (`docs/plans/harpers-conversion-brief.md` addendum):
  - cream paper, harp-in-crescent watermark;
  - lands only for the addressee and unfolds when touched;
  - Mirt's heavy, even hand, signed "M.";
  - GM only: the ink fades after an hour.
  - Use this object in every new Harper text.
- **Mirt's two gears are a feature.** In public he is loud, funny and profane, and gossips harmlessly. On business his sentences are short and plain, with no swearing. Show the switch.
- **Occupying Devourer is the campaign rule** for Nihiloor's devourers (`docs/plans/harpers-mechanics-reference.md` §5). No Wish. Telepathy reaches 60 ft, so hosts report through a courier.
- **Do not interrupt running background agents by answering questions mid-run.** The first research batch died when an AskUserQuestion answer came in (all five were marked "stopped by the user" and could not be resumed). Ask questions before launching agents or after they finish.

---

## Problems Solved

- **Shallow clone:** git history held only a few commits, so the true first commits were not visible. Fixed with `git fetch --unshallow`.
- **GitHub git pushes returned HTTP 500 for about 20 minutes:**
  - The GitHub API still worked, so the remote branch was created with `mcp__github__create_branch`.
  - Pushes recovered on their own. Commits were batched into PR #86.
- **Rate limits:** three times, the account limit stopped the running agents. Each time they were resumed with SendMessage after the reset; their work was never taken over in the main session.
- **The prev Harper version cited a "Harpers Mechanics Reference" that never existed.** It now exists.
- **M5 rhythm pass overshot** (narration 26 words, 40% of sentences over 30 words). A second, targeted pass brought it back into range.
- **Fireball ev-04 claimed a reveal it never staged.** The "Who Zord Is" block now stages it.
- **The consistency pass found 14 in-folder contradictions**, all fixed in `c652e8e`:
  - outcome readers that didn't read their outcome;
  - the Rusk name gate;
  - Remallia's key line;
  - reused vouchers;
  - the M6 brief scope;
  - stale design notes.

---

## Outstanding Work

### New this session
- [ ] **Answer the four Session 41 decisions** at the end of the "Harper event rewrite (Session 41)" section of `docs/plans/harpers-out-of-scope-notes.md`:
  1. Can 3-heist parties run Harper M6 (and DR/BD M6) after the Vault?
  2. Mirt's secrecy outside the Harper events: the org page, arc-i "I volunteered", Fireball ev-06.
  3. Does Emerald Enclave M3 (Bonnie's crew leaves) or Harper M3 (Bonnie becomes a Harper operative) win?
  4. The Trollskull Harper perks (500 gp loan, −1 gp laundry, "Good-aligned" eligibility): add them to the Harper events or cut them.
- [ ] **Wire the Harper outcomes into unconverted quests**, as each quest is converted (list in the out-of-scope notes §1):
  - Faction Outposts: Shesstra, Nethpranter, Erystian, and the Brindul Alley lead.
  - Xanathar's Lair: the Corene outcomes and Nihiloor False Report Confirmed.
  - Sea Maidens Faire: Jarlaxle Identity Exposed, Discretion Agreement, Jarlaxle Unmasked.
  - Kolat Towers: Edric Report Delivered, Harper Leak Closed.
  - Vault of Dragons: Stone Study, Jalester, Sending Stone, Stone Taken, High Harper, Masked Lord.
  - Lords' Alliance M6: Jalester.
  - **Bonnie Harper Operative** still has no outside reader.
- [ ] **Trollskull ev-04:97-98** still writes a party-level **Harpers Joined: True / False**. Cut it; the First Meeting is now the writer.
- [ ] **Act I–II Harper lines to fix:**
  - Remallia named as a Harper in Trollskull ev-04:91, Fireball ev-02:96 and `trollskull-manor/03-staff-and-hiring.md:84`.
  - Trollskull ev-07:51 (spare opera ticket).
  - Trollskull ev-04:71 (Maxeene "Zhent operatives").
  - Saeth Cromley active in Fireball ev-01:37.
- [ ] **Structure docs:**
  - arc-e:495 says Renown 30+.
  - arc-f:31 distraction threshold.
  - arc-i:19/247/265, Mirt says "I volunteered".
  - arc-i:75-77 and arc-j:43, the field agent.
  - arc-j:43 also has the Renaer branch and M6 timing.
- [ ] **Notable Figures:**
  - Nihiloor `04:26` says "consumed Meloon's brain".
  - Ahmaergo `02:6` says "Thug".
  - Remallia `02:6` stat line.
  - Variel `06:8` says "no scripted appearance".
  - Org page and NF lines say Mattrim is "the only person" who knows about Bonnie.
- [ ] **Force Grey M5 retired formats** (`[GM]`, `Milestone: None`, `[!narrative]`, no Event Outcomes block): convert in the Force Grey rewrite.
- [ ] **Accept or replace the Session 41 invented names** (out-of-scope notes §6, plus Seldo Wynd's personality, the opera company names, Ysolde Marne, Maera Brandt and Tomas Ardel).
- [ ] **Clarity/voice pass on the remaining factions** under ember-voice 2a, if the user wants it. The Doom Raiders was deferred in Session 40.

### Carried forward from Session 40
- [ ] **DR clarity polish.** Deferred by the user ("Go ahead with BD for now"). Use the BD method.
- [ ] **Clarity pass for the other converted factions** under 2a. Harpers are now done by rewrite.
- [ ] **BD M6 harbor naming.** M6 says both "Deepwater Harbor" and "the harbor"; settle one.
- [ ] **BD r25 dead branch** (Kreb Unmasked unmarked). Cut it.
- [ ] **Guide 08:33:** "Dread Lord renown" should be Commander, and Laeral's role as the gold recipient needs settling.

### Carried forward from Session 39
- [ ] **Answer the remaining BD decisions** in `docs/plans/harpers-out-of-scope-notes.md`: the Zord cover's origin; per-member wording in guide 08; where Renown 25/50 come from for every faction. (Decision 3, the Fireball ev-04 writer, is answered and done this session.)
- [ ] **Write the outside readers and writers for the BD outcomes** as each quest is converted: Sea Maidens Faire (Jarlaxle Unmasked now has its Fireball writer), Faction Outposts, Cassalanter Villa, Xanathar's Lair, Vault of Dragons, and OotG M2.
- [ ] **Fix the BD companion pages:** guide 08, org page 07, `villains/jarlaxle.md:51`, and the Notable Figures pages.
- [ ] **Act I–II contradictions logged for BD** in Trollskull, Fireball and Gralhund.
- [ ] **Accept or replace the invented names.** Ilmra, Odalys and Ilsa collide between DR and BD.
- [ ] **Voice profile for J.B. Nevercott.** Skills are main-session work and need a user request.
- [ ] **Reconcile the OotG M3 wererat silver rule** with the 2024 Wererat.
- [ ] **Structure docs and SOURCE_GUIDE:**
  - SOURCE_GUIDE:219 puts the windmill in the North Ward.
  - arc-j :55/:75/:322.
  - arc-h :9/:71 (Mistshore vs Smugglers' Dock).

### Carried forward from Session 38
- [ ] Faction Outposts must write Yellowspire Ledger/Letters Taken and Clean Exit. 5B must add the relay ledger and coded letters.
- [ ] Kolat Towers must name Vevette's fate, the K18 rune and the DR parallel-operation result as outcomes.
- [ ] Gralhund Villa's Floxin Status flag must become named Event Outcomes.
- [ ] Sea Maidens Faire must read Soluun's fate (BD s05).
- [ ] Faction Outposts must write **Manshoon Named** and **Yellowspire Raided**. Harper events now gate on Manshoon Named too.
- [ ] Wire the DR outcomes into their readers, arc-e through arc-j.
- [ ] Fix the DR companion pages: guide 07, org page 06, the Notable Figures pages, `structural-rules.md:9`, `player-factions-overview.md:186`.
- [ ] Act I–II DR contradictions.
- [ ] Accept or replace the DR invented names.
- [ ] Settle Renown 25/50 reachability for all factions.
- [ ] Voice profiles for recurring minor DR NPCs.
- [ ] Confirm the three viewer changes on the live site.

### Carried forward from Session 37 and earlier
- [ ] Answer the six decisions in `docs/plans/harpers-out-of-scope-notes.md` (Decisions Needed Before Fixing). Decision 2 (the Manshoon gate) is now adopted for DR and Harpers.
- [ ] One-faction membership wording on four guide pages, including `player-factions-overview.md:3, :22-23`.
- [ ] Voice profiles for minor Harper NPCs, if they recur: Uza, Tessalar, Tobin, Wil Keen, Nella, Orin, Seldo and others.
- [ ] Remaining non-rule inconsistencies: Finding Floon "two nights", Gralhund "two tendays", Vajra, Istrid's loan.
- [ ] Confirm Ember styling on the live site and use the Artifact files map if the viewer is republished. Convert the old `[GM]` zones in Finding Floon and Trollskull.
- [ ] Bestiary; convert arc-e through arc-j; prose pass on the guides and setting pages; polish Notable Figures profiles; recheck the Mission 5/6 summaries on the organization pages.
- [ ] `sources/backgrounds.json`; BD `ev-03` Ryvarra visibility; normalize sidebar titles in other factions; Renaer's Confidence holder framing.
- [ ] Ember organizations JSON; Trollskull Founders' Day wording; Asmodean Shrine Area 3; `#### Milestone: None` in other factions' events; DR Viper muscle on Yagra's NF page; earlier invented details.
- [ ] Remaining faction rewrites: Lords' Alliance, Emerald Enclave, Order of the Gauntlet and Force Grey. Use the Session 41 Harper method.
- [ ] Older items: voice-run tooling portability, reproducible global skills, legacy automation references, the Astra/Sol defaults, and the Harper private Site (stale; rebuild only if asked).

---

## Warnings and Caveats

- **The previous Harper version lives in git at `7215515`**, not in the repo tree. The brief and reports cite a scratchpad copy (`/tmp/.../scratchpad/harpers-prev/`) that dies with this container. Use `git show 7215515:campaign/quests/faction-events/harpers/<path>`.
- **Unverified mechanics:**
  - The 2024 sending-stone item text.
  - The Stone of Golorr's weight, for the M6 *Mage Hand* grab.
  - Fillipa's 2 HP.
  - Orvyn Dall as a Commoner.
  - Whether removing a hat of disguise ends the spell (M4 ev-02).
- **Dual writers accepted on purpose:**
  - **Harper M3 Complete** has two writers, M3 ev-01 and ev-02, on exclusive branches.
  - **Jarlaxle Unmasked** has two: Fireball ev-04, and M4 ev-03 on its unmarked branch.
- **Some rank events sit below the DR page lengths.** The text was tight; they were not padded.
- **Accepted voicecheck ranges:**
  - Most Harper speech averages 10.2–12.9.
  - Some GM blocks have 10–15% short sentences.
  - Three setting-page TELLs were left in pre-existing prose: org page L7 and L17, Mirt NF L26.
- **Fireball ev-04 is still in the retired `[GM]` / True/False format.** Only the Jarlaxle Unmasked entry was added.
- **Brindul Alley:** M2's ledger hands the Harpers a Brindul Alley lead (the Interrogation House) before Faction Outposts. It is kept on purpose as a lead for arc-e to read, but no reader exists yet.
- **The session 40 git stash** (BD clarity partial edits) is obsolete. It was not found in this clone and needs no action.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md. Then open the end of `docs/plans/harpers-out-of-scope-notes.md`, the "Harper event rewrite (Session 41)" section, which holds the four new user decisions.

For any further Harper work, read these first:
- `docs/plans/harpers-conversion-brief.md`, including its addendum;
- `docs/plans/harpers-drafter-instructions.md`;
- `docs/plans/harpers-mechanics-reference.md`.

If the user names another faction rewrite (Lords' Alliance, Emerald Enclave, Order of the Gauntlet or Force Grey), follow the Session 41 Harper method in Rules and Instructions. Otherwise wait for the user to name the next task.
