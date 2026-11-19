# Session 51 Handoff
**Date:** 2026-11-19
**Status:** Ready to continue. Everything is merged to `master` (PRs 351 to 393); the working branch matches master. No pass is in progress. Wait for the user to name the next task.

---

## What Was Done

Session 51 was a cleanup and canon-alignment session. It started from the Session 50 outstanding list and worked it down by running read-only audits (the `consistency-checker` agent) and then fix passes (`prose-drafter` agents), merging after each one. The user answered a long series of decisions and set one standing principle: canon lore is canon unless the campaign changed it for a stated design reason. About 250 stale or contradictory lines were fixed, every `True / False` flag heading became a named Event Outcome, 619 old `> **[GM]**` boxes became `[!gamemaster]` callouts, the deities and the Notable Figures were audited against the sources, every human NPC got a real Faerûn ethnicity, every Notable Figures page got pronouns, and the 2014 Bard stat block was replaced with the 2024 Performer family. A Factions Guide move to `setting/faction-operations/` was executed and then fully reverted when the user ruled that the setting holds lore only. Nothing was left half-done on `master`.

---

## Changes Made

137 commits and 492 files changed between PR 350 and PR 393 (14 added, 2 deleted, 3 renamed, 473 modified). The stop hook forced WIP commits during long agent runs, so the log has many "WIP:" commits; each PR carries the reasoning in its description and its final commit message.

### Files Modified (by area)
| Area | What changed |
|---|---|
| `campaign/quests/` (Finding Floon, Trollskull Alley, Fireball!, Gralhund Villa) | `True / False` headings and "attunement"/"flag" wording converted to Event Outcomes (PR 355); new **Two Small Guests** scene and **Cassalanter Twins Met** outcome in Trollskull `ev-06` (PR 366); Kalain's tower fight rebuilt (Performer, one Art Imitates Life, Bruising at level 3, Mild at level 4); Floxin, Yalah and Night Gazer readers reserved for Mad Mage. |
| `campaign/quests/faction-events/` | Lords' Alliance rank tests read **Redknife Reached** and exclude **LA Suspended** and **LA Dismissed**; Lords' Alliance Renown never falls (Redknife, Stingblade, Warduke, Lioncrown, First Meeting); Ziraj's favour once per campaign per member; Order of the Gauntlet rules corrected to the 2024 text (Spirit Guardians, Banishment scroll, Zone of Truth scroll DC 13, Spined Devil spine 20/80, Resurrection D20 penalty); Warden Osric and Deacon Teodric retitled; the Order's Gralhund hook is suspicion only; Ethnicities, pronouns and Odda Fenn labelled; Meloon, Jalester and Savra notes settled; stale design notes rewritten against the current guide rows. |
| `campaign/structure/` (arc-e to arc-j) | Neverember's Eye chain and 1489 date (`arc-e:33`, `:35`); operational flags renamed to named Event Outcomes; Brandath Mausoleum/Crypts naming; Cassalanter windmill owner; Willifort's tenure tagged `[research]`. |
| `campaign/setting/deities/` | Full canon audit of all 72 pages (285 Conflict notes): fixes toward FRHoF, SCAG, MTF and the published adventure; subclass fits judged by theme across about 60 pages and the hub; Iggwilv free in 1492; Lolth a strong Fiend fit; the Blessed of Corellon gift open to every elf; MTF labelled 2018; Selûne's temple is the House of the Moon; the Triad is Tyr, Torm and Ilmater; Queenspire on Deepwater Harbor; nine pages Heroes of Faerûn dropped carry a note; 31 stale "page planned" notes settled. |
| `campaign/setting/notable-figures/` | Summary boxes converted to `[!gamemaster]`; **pronouns on all 123 pages**; real ethnicities for 123 human NPCs; Avi he/him; Amath Sercent a Mulan human; Yorn a half-orc; Caladorn a Tethyrian human ghost; Fenerus a Bandit Captain (Neutral); Grinda Chaotic Neutral; Kalain, Mattrim, Variel, Agorn and Margo on Performer stat blocks; Korgstrod's fake Stone cut; Malkolm Brizzenbright spelled as Dragon Heist spells it. |
| `campaign/setting/` (history, lore, villains, organizations, governance, geography, the-grand-game) | Eye and Stone rulings, "all three Eyes", Chirada's letter, Jeryth in the Southern Ward, Watch Palace and two services, Field Ward the most dangerous, Cassalanter vault knowledge (they know the entrance lies in the Brandath family crypts), Cassalanters hold just over half the gold, Volo's four asides removed, Manshoon's simulacrum is his decoy and not the clone's insurance, harbor naming. |
| `campaign/gazetteer/waterdeep/` | Vondil Street border, Spices Street hostel, harbor naming, Kalain, Yellowspire, citations corrected. |
| `campaign/guides/` | GM Guide flag wording to Event Outcomes; Osvaldo is twelve and read to weekly; Factions Guide fixes (Bregan D'aerthe Vault hook at Renown 25 Commander, Ott, Lords' Alliance suspension wording, Ziraj's favour); Trollskull staff-table alignments. |
| `campaign/locations/` | Jarlaxle's cabin magic mouth now shouts "By the Nine Hells, have you no manners?"; Zord's office keyed to **Jarlaxle Unmasked**; Cassalanter villa twin placements; Viper Den and Gralhund readers reserved. |
| `CLAUDE.md` | Notable Figures summary format, page count 123, new rule "Viewer deploys on merge", Kolat/Vault summaries name the Manshoon outcomes. |
| `.claude/` | `rules-lookup` now points at `5etools-mirror-3/5etools-src`; `consistency-checker` rules; `ember-adventure-style` and `ember-setting-style` examples use real ethnicities and `[!gamemaster]`; `character-voices` splits the Vayle twins (124 profiles) and fixes Avi, Amath, Malkolm. |

### Files Created
| File | Purpose |
|------|---------|
| `docs/plans/event-outcomes-conversion-brief.md` | Binding brief for the True/False to Event Outcomes conversion. |
| `docs/plans/deities-canon-fix-brief.md`, `deities-user-rulings-brief.md` | What the deities audit fixes and the user's 20 rulings plus the Session 48 batch. |
| `docs/plans/faerun-ethnicities-research.md`, `waterdeep-npc-ethnicity-table.md` | Sourced ethnicity list and the table of every NPC assignment (two passes). |
| `docs/plans/npc-pronouns-table.md`, `npc-pronouns-table-group-a.md`, `-b.md`, `-c.md` | Pronoun assignments with sources and the alignment restorations. |
| `docs/plans/volo-asides-archive.md` | The four removed Volo asides, kept verbatim for the later Volo-voice pass. |
| `docs/plans/factions-move-spec.md`, `factions-move-brief.md` | The abandoned Factions Guide move; both are marked ABANDONED at the top. |
| `campaign/setting/notable-figures/harpers/07-corvin-vayle.md`, `08-nessa-vayle.md` | The Vayle twins as two pages (Maxeene is now `09`). |
| `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md`, `bregan-daerthe/07-malkolm-brizzenbright.md` | Renames for the canon spellings. |

### Files Deleted
| File | Reason |
|------|--------|
| `campaign/setting/faction-operations/10-cassalanters.md` | The Session 49 pilot; the setting journal holds lore only (the whole folder is gone). |
| `07-corvin-nessa-vayle.md`, `08-maxeene.md`, `08-amath-seccent.md`, `07-malcolm-brizzenbright.md` | Replaced by the renamed or split pages above. |

---

## Key Decisions

### Canon is canon unless changed for a design reason
**Decision:** Pages follow the highest-ranked source (FRHoF > SCAG > newer 5e book > published adventure for Waterdeep temples and places > wiki and novels) unless the campaign changed a fact for a stated design reason. Departures with no reason were reverted; deliberate ones were written down so the next audit does not re-flag them.
> "Canon lore is canon unless specifically changed with a design reason. Do a check for this throughout actually." — User, this session

### Mechanics live in the guides, lore lives in the setting
**Decision:** The Factions Guide stays at `campaign/guides/factions/`; `campaign/setting/` is lore only. The Factions Guide move planned in Session 47 was executed and then reverted in full (PRs 384 to 386).
**Reasoning:** The user ruled it after the move was done. Visibility gating between GM and player knowledge will be handled later in the journals themselves.
> "The factions stuff in the setting guide should be exclusively lore. Mechanics are already presented in the GM and Players' guide." — User, this session
> "So, the section in Guides are the mechanics the section in organisations will be the lore. We will later have a way to separate GM knowledge from player knowledge and different visibilities in the journal themselves." — User, this session

### Rulings on deities and lore (20 plus the Session 48 batch)
**Decision:** Avi he/him ("No reason for the change. Change it back."), Amath Sercent a Mulan human, Corellon "he" with the Form note, Ghaunadaur "it", Azuth lesser deity, Istishia on the Elemental Plane of Water, Auril retreated to the Sea of Moving Ice beside Icewind Dale in the late 1480s, Shadowmasters have a Waterdeep cell, the Triad is Tyr, Torm and Ilmater, Selûne's temple is the House of the Moon (Sea Ward), Jeryth's 1367 DR call stands, Moradin keeps EGW out ("EGW has nothing to do with faerun."), Orcus keeps both origins as "nobody knows which is true", Savras has temples in Chult not on the Sword Coast, Bright Nydra is Selûne's Farsea name (the daughter is a tale), Tymora's two accounts both hold, Valkur's 4e service to Tempus is history, Korgstrod's fake Stone is cut, Iggwilv is free in 1492 (Witchlight comes later), Yorn is a half-orc.
**Session 48 batch:**
- The "something vast and dreaming" seed stays unresolved until the Undermountain pass.
- The Blessed of Corellon gift is open to every elf, as a way to run a character who transitions.
- Subclass fits are judged by theme.
- Lolth is a demon as well as a god, so Fiend Patron is a strong fit.
- Zelifarn lives in Deepwater Harbor.
> "Keep it for everyone, fun way to get trans characters so actually transition" — User, this session
> "For subclass fits think thematically rather than what's mechanically written." — User, this session

### Design calls on faction content
**Decision:** Manshoon's Phase 3 stays (the simulacrum is his decoy; the stasis clone spell is his resurrection insurance). Meloon's devourer timing is a deliberate departure from Dragon Heist, so the party meets him as himself first. Jalester is a Chondathan human (ethnicity) and a Cormyte (nationality). Kalain returns to the published bard, now on the Performer stat block. The Cassalanters hold "just over half" the gold. Volo's four asides are removed. Fenerus is a Bandit Captain. Ziraj's favour is once per campaign per member. Savra left the Howling Hatred in 1491 (Princes of the Apocalypse).
> "It was designed like this and changed specifically to show how meloon was before" — User, this session
> "Performer, Performer Maestro, Performer Legend, these are the statblocks that replaced the old Bard. Do with that what you will." — User, this session
> "Eventually every document in the setting guide and gazetteer will be written in his voice. However, we will later need to add some asides correcting Volo on certain exaggerations by another character, likely Elminster just for fun." — User, this session

### Earlier rulings in the session (before the context reset)
**Decision:** The Stone is known only to players of the Grand Game; North of Vondil Street is the Sea Ward and south the North Ward; the Watch HQ is the Watch Palace; the Field Ward is the most dangerous; Saeth Cromley is an "investigator"; Jeryth feels the infernal influence in the Southern Ward; the twins appear at the Grand Opening and at the villa; "all three Eyes" are needed, not any two; the Vault entrance stays beneath the Brandath Crypts (the Mausoleum is the building).
> "By players I mean players of the grand game" — User, this session
> "3. All three is right, but this should've been flagged way earlier." — User, this session (the "any two Eyes" conflict that had sat in the handoff)

### Later quest-arc work
> "Manshoon Named will be done when we write the new format for quest arcs for those quests." — User, this session
> "We will have sidebars for players gaining or losing renown as we polish the campaign, for each arc, beyond faction missions" — User, this session

---

## Rules and Instructions

These must be respected in all future sessions.

- **Canon unless a design reason:** see Key Decisions. When a user gives a design reason, write it into the relevant Draft Note or design notes as Settled so audits stop re-flagging it.
- **Decisions come with full context, written in the message:** quoted lines with file and line, what each option changes, a recommendation. Never use a question-tool call. (Standing rule in CLAUDE.md, reinforced this session.)
- **Agents do the work; the main session orchestrates:** drafting goes to `prose-drafter`, audits to `consistency-checker`, rules to `encounter-builder`. Never run more than 5 agents at once. The user's interrupt ends running background agents, so re-launch rather than resume.
- **PR and merge as each batch finishes**, then fast-forward the working branch. The viewer (GitHub Pages) deploys on every merge to master that touches `campaign/**`; check the run after rendering-sensitive changes and never rebuild or hand-edit `docs/index.html`. (CLAUDE.md "Viewer deploys on merge".) Run `python3 scripts/build-viewer.py` locally before merging a structural change, then `git checkout docs`.
- **Do not act beyond what was asked; wait to be asked.** Several of this session's mistakes came from running a decided plan without re-confirming it (the Factions Guide move).
- **Handoff only on `/handoff`.** This handoff is the last commit of the session.
- **No `> **[GM]**` boxes anywhere.** Every GM box is `> [!gamemaster]**Title**`. The Notable Figures page format is H1, `> [!gamemaster]**Gamemaster's Summary**` box with pronouns on the first bullet, then the sections.
- **Pronouns on every Notable Figures summary line;** Xanathar and Nihiloor are it/its, Fala is they/them.
- **Ethnicity, not city.** Humans take a Faerûn ethnicity (Illuskan, Tethyrian, Chondathan and so on); never "Waterdhavian Human". Nationality goes in prose ("a Cormyte"). Both style skills now say so.
- **Stat blocks:** the 2024 Monster Manual has no Bard. Use Performer (CR 1/2), Performer Maestro (CR 6) or Performer Legend (CR 10).
- **Lords' Alliance Renown never falls.** Suspension (**LA Suspended**, **LA Reinstated**) and dismissal (**LA Dismissed**) replace Renown loss; the member keeps the rank and Renown while suspended.
- **Mechanics vs lore:** faction mechanics are in `campaign/guides/factions/`, lore is on the organization pages. No Faction Operations journal exists.
- **Brandath names:** the Mausoleum is the building and the vault lies beneath it; the Crypts are the approach. The Cassalanters know the entrance lies in the Brandath family crypts (Fireball! `ev-05:46` governs) and cannot open it without the Stone.
- **Cassalanter secrecy** is unchanged: the Order's and others' lines are suspicion, never knowledge.

---

## Problems Solved

- **Any-two-Eyes conflict** flagged in earlier handoffs but never put to the user: fixed to "all three Eyes" in five files.
- **Cassalanter vault knowledge:** I changed the starting-knowledge row to "they do not know where the vault lies" and the Fireball! journal contradicted it (`ev-05:46`); reverted, with `arc-j:13` and the notes aligned to the quest journal.
- **Shar's aid in Mystra's death** was wrongly dropped by a drafter; FRHoF's Cyric entry says "Aided by Shar" (`deities.json:2787`); restored on Shar, Lathander, Mystra, Savras pages.
- **Factions Guide move:** executed, then reverted in PRs 385 and 386; the 18 lines that assumed a Faction Operations journal point back at the Factions Guide.
- **Meloon timing** wording in the Trollskull design notes said "after Fireball"; the Field of Triumph is Ches 20 and Fireball is Ches 22, so it now says "after the Field of Triumph".
- **r25 +1 weapon table** was marked unverified because only `items.json` was read; the generic +1 Weapon is in `magicvariants.json` and the table is right.
- **Mission-3 style Renown loss** in the Lords' Alliance events contradicted `03-lords-alliance.md:78`; fixed in six events and the guide.

---

## Outstanding Work

### Needs a user ruling
- [ ] **Factions Guide overview conflicts** (`campaign/guides/factions/01-overview.md` against `player-factions-overview.md` and `faction-affiliations.md`). Two are for the arc renown sidebars (supplementary renown `01-overview.md:25`, losing renown `:25`). Two still need a ruling: honest failure (`player-factions-overview.md:26` "An honest attempt that fails costs nothing: formal suspension until reinstated, or outright dismissal" against `03-lords-alliance.md:76` "Honest failure costs nothing") and reinstatement (`01-overview.md:11` "usually after a demonstrated act of service to the city" against `03-lords-alliance.md:78` three routes).
- [ ] **Khafeyta Murzan** is "Mulhorandi" (Dragon Heist's word) while the campaign's other Mulhorand humans read "Mulan". Keep or change.

### Next passes (wait for the user to name one)
- [ ] **Pass 5 (Organizations), Pass 6 (Notable Figures), Pass 7 (Introduction, cleanup and docs)** from `docs/plans/setting-compendium-rebuild-plan.md`. Pass 6 converts the other 122 Notable Figures pages to the Seffia page's layout (H1, summary box, name tag, Personality, Connections, Overview, GM block). The Factions Guide move is cancelled; the plan row is marked superseded.
- [ ] **New quest-arc format** for Faction Outposts through Vault of Dragons: renown gain/loss sidebars per arc; the **Manshoon Named** marker (about twelve events read it and none marks it; `arc-e:211`); wiring faction outcomes into the unconverted quests (Order outcomes in `harpers-out-of-scope-notes.md` "Session 45" section 1; Lords' Alliance and the other factions in their sections).
- [ ] **Volo-voice pass:** write the setting and gazetteer pages in Volo's voice (player-facing layer only), with Elminster's marginal corrections that carry the true facts for the GM. Needs a standing rule in CLAUDE.md and `ember-setting-style`, plus voice profiles for Volo and Elminster. The removed asides are in `docs/plans/volo-asides-archive.md`.
- [ ] **Undermountain pass:** resolve the "something vast and dreaming" seed (`arc-f:382`); the Floxin Captured, Yalah Missing, Yalah In Custody and Gazers Active at Night readers are reserved for Mad Mage.

### Carried forward from Session 50 and earlier, still open
- [ ] **Pass 2 follow-ups:** swap any of the thirteen patrons (three of each kind was the main session's choice); a Siamorphe wiki-only page review.
- [ ] **Sea Maidens Faire rooms 01 to 04** (`locations/sea-maidens-faire/`) were not checked against "submarine moored all year".
- [ ] **"attunement" wording** in five quest events (Harpers m06, BD r10, Order r10, Fireball! ev-02 and ev-04): check whether each means the Stone's real attunement or the old flag.
- [ ] **Unsourced rows kept with `[research]`** (Jarlaxle's Renaer row, Manshoon's "deserters" clause, the Cassalanter "three sessions" trigger, others listed in the Session 50 handoff); source conflicts left in Draft Notes (Kolat PDF p.96 "He already has one" against "Manshoon holds no Eye"; Skeemo as traitor against "compiles all of it").
- [ ] **Invented details to confirm:** "within days" for Zelifarn's arrival (`arc-h:19`), the Q03 strongbox and reassigned guard in the hideout beat.
- [ ] **Source-check follow-ups:** the wiki's claim that the public knew of the embezzlement by 1492 DR (`vault-of-dragons` bundle `wiki.txt:69`) was not found in the JSON; Dragon Heist `arc-i:43` and `arc-j:53` still say Doom Raiders Mission 6 delivers the 43 names and the Splinter list, which Mission 6 no longer does (logged in the Doom Raiders notes).
- [ ] **Howling Hatred ranks** (Initiate, Windwalker, Windcaller) have no source (`[research]` on `s02-savras-past`); the class lists for *Banishment* are not in the data folder; the XDMG +1 Weapon text gives only the bonus ("counts as magical" is inferred).
- [ ] **`history/08` 1491 date** for the *Scarlet Marpenoth* has no verifiable wiki line (the page is not in `sources/research`; the Jarlaxle bundle says "late 15th century").
- [ ] **Stale design-note claims and line citations** in faction-event design notes that cite Factions Guide lines: about half were rewritten; re-check any that cite `guides/factions/*.md:NN`.
- [ ] **Faction Outposts kidnap scene** (`arc-e:293` to `:311`) calls Fenerus "a civilian in over his head"; he is a CR 2 Bandit Captain, and no fight is written there yet.
- [ ] **Missing Notable Figures pages** (Elminster, Khelben Arunsun, Halaster, Piergeiron, Raurlor, Alethea Brandath and the rest listed in the Session 50 handoff); **wiki items still open** (ward Lifestyle, Languages and dominant faith; Midsummer, Twin Parades and Fey Day; the Code Legal's author and date).
- [ ] **Voice residue:** short-sentence rates run 10 to 20% on the new pages; no voice profiles for the Order's recurring minor NPCs; the prose-writing pass is deferred for everything.
- [ ] **The "Brother" and other Session 45 invented names** are accepted; the Session 45 readings are accepted.

---

## Warnings and Caveats

- **The scratchpad is lost between sessions.** The wiki dump (`scripts/fandom-dump/README.md` rebuilds it in about five minutes), the extracted PDF and docx text, and the 2024 rules data are all rebuilt on demand. The 2024 data lives at `https://raw.githubusercontent.com/5etools-mirror-3/5etools-src/main/data/...` (`spells/spells-xphb.json`, `magicvariants.json`, `items.json`, `bestiary/bestiary-xmm.json`).
- **The working mirror is `5etools-mirror-3/5etools-src`.** The old mirror-2 URL returns 404; `rules-lookup` is updated.
- **The stop hook forces commits.** Agents' unfinished work was committed as "WIP:" and pushed without a PR; only reviewed batches were merged. Always check `git status` for untracked agent output before merging.
- **A user interrupt ends all running background agents.** Re-launch them with the same brief; `docs/plans/*-brief.md` files make that cheap.
- **Agents without a shell cannot run `voicecheck.py`, `git mv` or `git rm`.** The main session runs voicecheck on every batch and removes renamed files.
- **Three decisions were made on the user's behalf and may be overturned:** Savra retitle "Warden"/"Deacon" for the Brother cluster, "Illuskan Human" for Odda Fenn (name pattern), and Fenerus as a Bandit Captain. Each is recorded in a table or Draft Note.
- **CLAUDE.md page counts:** 123 Notable Figures pages and 124 voice profiles (Jarlaxle and his Zord cover are separate, and the twins are separate now).
- **Generated pages** (`docs/index.html`, `campaign-reader/dist/index.html`) are built output and carry old labels until the next deploy; do not edit them.

---

## Where to Start Next Session

Read this handoff and `CLAUDE.md`, then wait for the user to name a task. The likely candidates are Pass 5 (Organizations) from `docs/plans/setting-compendium-rebuild-plan.md`, the new quest-arc format (renown sidebars and the **Manshoon Named** marker), or the Volo-voice pass. Before any of them, put the two open overview rulings (honest failure and reinstatement) and the Khafeyta question to the user, written out with the quoted lines under "Needs a user ruling" above. The Factions Guide is not moving: do not re-propose it.
