# Session 35 Handoff

**Date:** 2026-09-28 (work began 2026-09-27)
**Status:** The approved Harper faction-event run and private phone reader are complete. GitHub PR delivery remains to be verified after this handoff commit.

## What Was Done

From the restored Session 34 baseline, the session established a verified 2024-rules and CR 2.0 workflow, then rewrote and independently reviewed every Harper First Meeting, mission, standalone event and rank event. A second pass replaced drafting Act headings with descriptive scenes and gave NPCs playable, character-specific speech. First Meeting gained boxed narration for the Tiamat performance and Mirt's pre-intermission conversation. The initial Black Network knowledge boundary was repaired inside Harper scope. A 34-page, Ember-styled, owner-private phone reader now serves the 33 accepted Harper Markdown pages and their mechanics reference at <https://waterdeep-harper-missions.friendlysgames.chatgpt.site>. No other faction's content was rewritten.

## Changes Made

**Evidence range:** `7a206211cd74d927d5861c25a861ee6a95624177..1b74cc3` (25 work commits). The base is the commit containing `session 34 handoff.md`, found with `git log -1 --format=%H -- "session 34 handoff.md"`. This handoff is a separate final commit.

| File or exact scope | Change and reason |
|---|---|
| `AGENTS.md`; `campaign/guides/factions/01-overview.md`, `02-harpers.md`; both players'/GM faction overview pages; Trollskull's `ev-04-the-factions-come-calling.md` | Early, accepted individual-membership and First Meeting companion corrections. The later scope limit prevented further companion edits; see the out-of-scope notes. |
| `campaign/quests/faction-events/harpers/00-first-meeting/` | Rebuilt invitation, ticketing, timed clothing recovery, anonymous lodging and individual recruitment. Later added boxed opera action and Mirt's playable pre-intermission lines. |
| `campaign/quests/faction-events/harpers/m01-the-talking-mare/` through `m06-the-stones-other-master/` | Six multi-beat missions with 2024 mechanics, bounded clues and consequences, individual Renown, Event Outcomes, descriptive scenes and direct dialogue. M3 and M4 retain their multiple event pages. |
| `campaign/quests/faction-events/harpers/s01-the-cell-is-compromised/` | A warning with a fixed 48-hour operational-register leak; Harpers do not begin with knowledge of its hidden leadership. |
| `campaign/quests/faction-events/harpers/r03-harpshadow/`, `r10-brightcandle/`, `r25-wise-owl/`, `r50-high-harper/` | Four individual rank appointments with bounded member benefits, playable requests and new Design Notes. |
| `docs/plans/faction-voice-run.md`, `faction-voice-ledger.json`, `harpers-first-meeting-plan.md`, `harpers-preflight.md`, `harpers-remaining-events-plan.md`, `harpers-mechanics-reference.md` | Approved production plan, protected facts, verified source and encounter calculations, folder acceptance and final review record. |
| `docs/plans/harpers-out-of-scope-notes.md` | Records specific contradictory guides, NPC pages, other faction events and heist readers without changing them. |
| `scripts/cr2_encounter.py`, `qa_faction_voice.py`, `test_faction_voice_tools.py` | Reproducible CR 2.0 calculations and scoped structure, link, baseline and TELL checks; 13 tool tests pass. |
| `scripts/build-harper-reader.py`; `docs/harper-reader/.openai/hosting.json`; `docs/harper-reader/dist/` | Accepted-only local reader and same owner-private Site, using adapted Ember CSS, fonts and callout frames. Version 17 is live; the source module CSS was not edited. |
| `session 35 handoff.md` | This continuation record and carried-forward checklist. |

The production source branch for the private reader is `codex/harper-site-source` at `1d72f9db8bb14af0379b53e974065ed9f61f6222`; the separately saved Site version is 17. The campaign branch is `codex/session-33-handoff` at `1b74cc3` before this handoff commit. Do not confuse the Site source branch with the GitHub PR branch.

## Key Decisions

- **Approval and scope.** The user said “Implement the proposed plan” and later “approved, go ahead” for the Harper production plan. Subsequently: “don't edit anything that is out of scope for this. If something contradicts, make a note of it somewhere, and carry on working”. Harper event folders, approved support documents and the requested derived reader were changed; later contradictions elsewhere were only recorded.
- **Membership belongs to characters.** “Each party member may join one faction, and each faction can have multiple party members, but not all party members have to join the same faction.” A PC can remain unaffiliated. Recruitment, Renown, rank and member benefits are individual; nonmember helpers can participate but do not gain that faction's Renown. Five-PC CR 2.0 examples count combatants, not five members of one faction. Expressly party-wide gifts remain shared.
- **No faction-mission boss-block requirement.** “Faction missions will not require boss statblocks.” The Harper encounters use verified standard 2024 creatures or explicit conversions and CR 2.0 scenarios; no phase/reaction-pool boss requirement was added merely because an adversary has a name. The broader AGENTS.md rule remains unchanged and this exception is recorded in the run plan.
- **Final presentation uses scenes and speech.** “show, don't tell. Don't just describe what a character says, actually say it in character. Also, drop the act structure, that was just for the drafting phase, we use scenes, not acts.” The approved three-beat mission progression remains, but event headings are descriptive scenes. The writer used all requested Ember, character-voice, adventure, prose and journal skills; voice and humanizing checks were followed by independent editorial review. These are reviewed campaign structuring drafts, not a claim that the whole campaign has received a final prose-writing pass.
- **Theater immersion.** The user required “boxed narrative text for events on the stage at the Tiamat play” and “dialogue starters from Mirt or way mirt may answer any questions the party has before intermission”. The First Meeting event and its Design Notes alone were reopened for this addition.
- **Initial Black Network secrecy.** “At the beginning of the campaign, nobody knows that Manshoon is running the splinter. The Doom Raiders think Floxin is the leader, and all the harpers and other factions know is that the Black Network is split up, they don't know any specific details”. Harper speech and summaries now respect what evidence has been found and conveyed. The true affiliation may remain in DM-only background. Out-of-scope contradictions, including Davil's Doom Raider opening, are in the notes.
- **Private phone artifact.** “As you complete each one, can you update the artifact and turn it into a ChatGPT Page I can read on my phone?” The user later supplied `ember.css` to improve its styling and asked to finish the viewer update first. The same private reader was rebuilt and published after each accepted folder; no public sharing change or general campaign viewer rebuild was made.

## Rules and Instructions

- Read the highest-numbered handoff and AGENTS.md at startup. Session 35's user decisions supersede older restored-event and Act-heading instructions where they conflict.
- Continue to use D&D 2024 rules, `rules-lookup` for uncertain source records, `cr2-encounter-builder` for all combat math, and the current campaign milestone ladder. Faction missions award no Milestone Points.
- Treat the approved Harper Markdown files as the source. Their named Event Outcomes and physical evidence determine later readers; do not turn a leak warning into automatic leak closure or retract already delivered intelligence.
- Recruitment, briefs, debriefs, Renown and ranks are member-specific. Jarlaxle's existing debrief exception remains. Remallia's Harper identity is not disclosed before Mission 4.
- The initial Manshoon knowledge gate applies across the campaign, but other-faction and guide corrections in `docs/plans/harpers-out-of-scope-notes.md` await explicit scope. Keep Cassalanter infernalism secret until discovery and communication.
- Use scene headings and actual in-character answers in later event presentation; preserve playable mission depth and the approved reward sequence. Do not apply the old Act labels from AGENTS.md to finished Harper event pages.
- No Foundry JSON. The Harper phone reader is a user-authorized exception to the general no-HTML-before-campaign-completion rule. Publishing other campaign sections still requires their own request and review.
- Root owns commits, skill/configuration edits and delivery. Delegate scoped campaign writing/review only when appropriate, with one editor per file and explicit skill/source requirements; verify workers' claims. Do not begin the next faction automatically.

## Problems Solved

- Replaced the restored Harper one-check/legacy presentation with meaningful scenes, named outcomes, actual dialogue, explicit timings and renown conditions across 12 folders and 33 files.
- Settled the First Meeting trial's unresolved tickets, clothing deadline and anonymous safe-house access. The invitation seats each eligible candidate; clothing recovery has a fixed cutoff; members can use the North Ward lodging without meeting Remallia before M4.
- Separated Tessalar's M2 cipher and its four physical ledger fates from Orren's S01/M5 operational leak. M5 offers three independent mole clues; identification and closure are different outcomes. Queued copies can be stopped; delivered copies cannot be recalled.
- Made Corene's possession and Remallia's prepared live extraction playable without treating the standard brain-destroying Intellect Devourer ability as compatible with rescue. M6 fixes the Stone study and raid custody, Jalester contact and counterplay. Rank benefits have specific individual limits.
- Verified rules/monster records and recalculated the Harper encounter branches for 3-, 4- and 5-PC participation, including actual Mirt/rank allies; ordinary named foes were not inflated into bosses. Independent source/math review cleared the final mechanics.
- Final independent corpus review accepted all Harper files, including M2-to-M5 physical continuity, S01's GM-only timing, M5 closure, M6 Sending/Stone custody, individual rank benefits, knowledge gates and scene headings. Final checker: 33 files, 0 errors, 97 editorial/manual review notices, zero TELLs; 13 tool tests pass. The manual notices are not a prose certificate or remaining blocking errors.
- The 34-page private Site deployed successfully as version 17 from the exact pushed source commit. Its access policy remains custom with one allowed owner, zero groups and zero external visitors. The local 390-pixel reader was checked for readable Ember boxes, loaded assets and no horizontal overflow; direct signed-in phone reading by the user remains unverified.

## Outstanding Work

### Carried forward from Sessions 29–31

- [ ] Verify the previously deployed Pages URL works for the user after the stale-cache report. This is separate from the new Harper phone Site.
- [ ] **Bestiary:** never drafted. Pages reference Xanathar two-phase, Victoro and Ammalia, and Aurinax.
- [ ] Convert remaining quest structure documents into journals, one per quest: Faction Outposts; Xanathar's Lair; Cassalanter Villa; Sea Maidens Faire; Kolat Towers; Vault of Dragons, including a Scene 6 debrief if Xanathar is GONE.
- [ ] Guides/setting prose pass: Trollskull Manor Guide; setting lore, history, grand-game, villains, organizations and Notable Figures. The Players' Guide and GM Guide remain historically checked; this session did not re-audit them.
- [ ] Prose polish the word-for-word NPC profile text in Notable Figures.
- [ ] Recheck Mission 5/6 summaries on organization pages against the Factions Guide; they were outside Harper event scope.
- [ ] Resolve missing `sources/backgrounds.json` and verify Heroes of Faerûn background names in the XPHB/FRHoF tables.
- [ ] Confirm intended BD `ev-03` Ryvarra visibility for drow PCs or the Yawning Portal check under individual, rather than party-wide, membership.
- [ ] Normalize older faction-mission sidebar titles to `> [!type]**Title**` where still needed outside the accepted Harper folders.
- [ ] Recheck the GM Renaer's Confidence Holder framing and Holder register against the rewritten GM pages.

### Carried forward from Session 32

- [ ] Ask for the ephemeral Ember organizations JSON again when the organizations lore pass starts.
- [x] Resolve Remi's pre-M4 safe-house secrecy: First Meeting supplies anonymous North Ward lodging maintained through intermediaries, and M4 reveals her identity.
- [x] Add the separate Harper double-agent investigation to **The Sleeping Asset**: M5 identifies Orren through three paths and distinguishes him from Corene's possession.
- [ ] Reconcile BD guide `08-bregan-daerthe.md` Renown 5+ *Scarlet Marpenoth* extraction with rank thresholds 3/10/25/50.
- [ ] Reconcile BD M6 limpet-charge/Eye #3 wreck summary and North Ward versus Southern Ward windmill location.
- [ ] Check Trollskull Manor Guide `01-overview.md` Founders' Day wording against the Structural Rules calendar.
- [ ] Add missing keyed Area 3 in the Asmodean Shrine; check Samara and Illuun Notable Figures.
- [ ] Decide whether to remove remaining `#### Milestone: None` blocks in other factions' m01–m06 events. The accepted Harper files no longer contain them.
- [ ] Reconcile Doom Raider Viper “veteran” muscle with Yagra's modified Thug profile.
- [ ] Check OotG M6 GM text about Victoro's “contract-bound infernal patron” for any in-fiction disclosure.
- [ ] Accept or replace the earlier invented details: LA Sevel Dastar; Force Grey Aldris Maeven, Rhendar Solne and Merris; BD Ilphrin Quiss, Pelsha and Vorn, Sarev Oust; OotG Tobrin; EE Sarna Dath and Bertio Caskwall; Savra's cult/Howling Hatred ranks; and the three near-parallel Renown 50 Mad Mage choices in LA/EE/OotG.

### Carried forward from Sessions 33–34 and this session

- [ ] Complete the other six factions' event rewrites from their restored drafts, one approved plan at a time. The old H3/D3/B4/E3/F2–F4/L1–L4/O3 voice-batch list and D2 ledger status are historical/superseded as an execution order; do not resume them blindly. Preserve their unresolved content concerns when those factions are selected.
- [ ] If retaining the historical voice-run tooling, make `.claude/briefs/voice-run/qa_batch.py` portable and update the old briefs for Codex agent APIs, Windows paths, resolved skills and current baseline. This is not needed to run the new Harper checker.
- [ ] Make imported global skills reproducible on another machine if requested; they remain outside Git under `C:/Users/lupur/.agents/skills/`.
- [ ] Review conceptual-only legacy automation references against current official documentation before using them. Configure Foundry/Plutonium MCP only if needed; resolve third-party instruction-size warnings if those plugins become relevant.
- [ ] Recheck inherited Session 32 items against each later faction rewrite before closing them; commit subjects alone are insufficient evidence.
- [ ] Reconcile the other faction events' legacy flags, milestone blocks, secrecy, timing, faction affiliation, named outcomes and downstream readers against current guides and NPCs. The Session 34 reset removed former in-subtree fixes for those factions.
- [x] Settle the historical Sol First Meeting trial's ticket participation, clothing recovery and safe-house access before production; the approved production plan did so without adopting a two-person enrollment limit.
- [ ] If the user later selects a permanent Astra/Sol or Sol/Low setup, update saved defaults and orchestration documentation together. Sol/Low's campaign result is task-specific, not a measured cross-model cost benchmark.
- [ ] Reconcile the exact deferred files in `docs/plans/harpers-out-of-scope-notes.md` when the user authorizes those scopes: especially Davil's premature Manshoon reveal, Harper/BD guides and NPC profiles, Emerald Enclave M3, Lords' Alliance M6, and the five unconverted lair/Vault readers. Do not edit them simply to finish this handoff.
- [ ] Verify the new Harper private Site on the user's signed-in phone; local mobile layout and owner-private deployment were verified, but signed-in end-user reading was not.
- [ ] Complete authenticated GitHub delivery of Sessions 33–35 on `codex/session-33-handoff`: push, PR to `master`, attach, check, merge, fast-forward local master and verify `session 35 handoff.md` on origin/master. This item closes only after those steps actually succeed.

## Warnings and Caveats

- The full campaign remains a structuring draft. The successful voice pipeline and independent Harper review establish this run's acceptance, not publication-ready prose for every campaign page.
- Scope-limited Harper outcomes deliberately do not repair downstream readers. The out-of-scope notes list concrete future reconciliation targets; earlier accepted companion edits remain in the history, while later companion edits made during this run were undone.
- The private Site is an accepted-only derivative, not a replacement for Markdown or the general `docs/index.html` campaign viewer. Version 17 was confirmed live and owner-private; direct phone reading needs the owning account signed in.
- Legacy trial artifacts are historical. The First Meeting production event supersedes the Sol and Luna experiments; no broad model-cost ratio follows from the trial or this run.
- Git status lists several unrelated files as modified due LF/CRLF conversion warnings. `git diff --name-only` and `git diff --raw` showed no actual uncommitted content changes before this handoff; do not stage or normalize those files as part of delivery.
- GitHub CLI was not found on PATH. A noninteractive Git push dry run had no output after a minute and was interrupted; authentication and remote write remain unverified at handoff drafting time. Preserve the local commit if delivery cannot proceed without credentials or network access.

## Where to Start Next Session

1. Read this handoff and AGENTS.md. Treat the Harper event run as completed under `campaign/quests/faction-events/harpers/`; consult `docs/plans/harpers-remaining-events-plan.md` and `faction-voice-ledger.json` for approved details and review evidence.
2. If this turn's GitHub delivery could not finish, deliver the existing branch and this handoff first; inspect origin, authentication and PR checks. Do not create another handoff merely to deliver Session 35.
3. When the user names another faction or companion-audit scope, plan and approve that work explicitly. Start from the Session 34 restored draft and carry forward individual membership, CR 2.0, scene presentation, full writer voice skills, hidden Manshoon leadership and the no-required-boss-block faction exception.
4. Consult `docs/plans/harpers-out-of-scope-notes.md` before editing guides, other factions or lair/Vault readers. The Doom Raider opening's knowledge error is confirmed but remains intentionally unchanged.
5. Do not automatically begin Faction Outposts, other faction rewrites, bestiary, skill packaging or new Site publication after handoff delivery.
