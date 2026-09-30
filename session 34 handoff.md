# Session 34 Handoff

**Date:** 2026-09-27 (work began 2026-09-26)
**Status:** Faction events restored and verified locally; rewrites await the next requested task. GitHub delivery blocked by missing authentication.

## What Was Done

Configured project-local orchestration and specialist roles, evaluated a scoped Luna/High revision and two full Harpers First Meeting reconstructions, and compared the final Astra/Medium orchestration with Sol/High workers against the Luna result. The user preferred the Sol draft over both Luna and the earlier Claude version, but raised the high usage cost and asked only for an opinion about Sol/Low. The user then explicitly requested restoring faction events to their initial committed state before handoff. All 177 currently tracked files under `campaign/quests/faction-events/` now match their own first committed versions; 161 changed and 16 already matched. No rewrite began after this reset. Later work remains recoverable in Git, and trial artifacts remain available separately.

## Changes Made

**Evidence range:** `e1ab28e44022fb557a43cf20f082f639a7c5f565..20a846087fc2420ab08498dcaa34ec968dbd1f88`.
The base is the commit returned by `git log -1 --format=%H -- "session 33 handoff.md"`. Seven work commits changed 178 files, with 5,429 insertions and 6,325 deletions before this handoff. This handoff is a separate final commit.

| File or scope | Change and reason |
|---|---|
| `.codex/config.toml` | Saved Sol/High primary and Luna/High worker defaults, with three worker slots; live runtime settings take precedence. |
| `.codex/agents/campaign_researcher.toml`, `campaign_writer.toml`, `campaign_prose_reviewer.toml`, `campaign_consistency_reviewer.toml` | Four scoped specialist roles; only the writer edits campaign files. All saved worker models remain Luna/High. |
| `AGENTS.md` | Added scoped worker startup and orchestration rules. |
| `docs/agent-reference/orchestration.md` | Assignment ownership, source verification, model activation, independent review and runtime constraints. |
| `docs/trials/harpers-first-meeting-luna-high.md` and `harpers-first-meeting-assessment.md` | Six-passage trial from the then-current pilot, including one targeted correction round. |
| `scripts/check-harpers-trial.py` | Scope/hash check for that historical six-passage trial. Its production-file baseline was intentionally invalidated by this session's reset; see warnings. |
| `docs/trials/harpers-first-meeting-initial-05076c9.md` | Historical First Meeting input copied from its first commit, `05076c952868b701a05862403721bae542a5ff48`. |
| `docs/trials/inputs/harpers-guide-no-meeting.md` | Mechanical guide copy with the later First Meeting summary removed to avoid exposing trial writers to the pilot. |
| `docs/trials/harpers-first-meeting-from-scratch-luna-high.md` and `harpers-first-meeting-from-scratch-assessment.md` | Full independent Luna reconstruction and review, without an editorial correction round. |
| `docs/trials/harpers-first-meeting-from-scratch-sol-high.md` and `harpers-first-meeting-astra-medium-sol-high-assessment.md` | Full Sol reconstruction under explicitly requested Astra/Medium orchestration, plus independent Sol/High review and comparison. Preserved as delivered by the writer. |
| `campaign/quests/faction-events/` | Restored 161 files across all seven factions to their individual creation commits, including event pages, overviews and design notes. All 177 files verified against original Git blob IDs. |
| `docs/maintenance/faction-events-initial-state-2026-09-26.json` | Exact 177-file restoration inventory: paths, creation commits, initial blobs, pre-reset blobs and whether each file changed. |
| `session 34 handoff.md` | Current continuation record; supersedes earlier voice-run completion status for the restored subtree. |

All faction paths in the following table are relative to `campaign/quests/faction-events/`.

| Faction | Files verified at initial state | Files changed by reset |
|---|---:|---:|
| `bregan-daerthe/` | 30 | 30 |
| `doom-raiders/` | 26 | 25 |
| `emerald-enclave/` | 21 | 21 |
| `force-grey/` | 24 | 22 |
| `harpers/` | 27 | 25 |
| `lords-alliance/` | 26 | 16 |
| `order-of-the-gauntlet/` | 23 | 22 |

**Work commits:**

- `2ffc481` — Pin campaign orchestration models and constrain workers to verified continuity.
- `b33f953` — Keep orchestration definitions free of trailing blank lines.
- `dc7b100` — Balance orchestration cost by using High reasoning for both model tiers.
- `f5c4d13` — Evaluate Luna campaign revisions without changing the approved Harpers pilot.
- `e29a9e5` — Preserve independent Harpers reconstruction and review for comparison.
- `7bb441b` — Record Astra Medium and Sol High reconstruction trial for comparison.
- `20a8460` — Restore original faction-event drafts as the baseline for rewriting.

The complete pre-reset campaign state is recoverable at `7bb441b`. The reset used normal file restoration and a new commit; shared history was not rewritten.

## Key Decisions

### Faction events restart from their original drafts

> “I want you to bring the faction events back to their initial commit state. We will be rewriting them. After that, $handoff”

“Initial” was implemented per file, using the earliest addition commit reachable from HEAD. The 177 files originated in ten commits; there is no single earliest commit containing every file. No rename or deletion history was found in this subtree. The restore includes First Meetings, missions, rank events, standalone events, overviews and design notes. It excludes faction guides, organization/NPC pages, skills, sources, trials and the viewer.

The original text is now the rewrite input. Restoring it is not an endorsement of its old prose, formatting or superseded facts. Current AGENTS.md and skill rules still govern future rewrites. Earlier voice-run batch completion and pilot approval are historical, not a description of the current faction-event files.

### Trial quality and model settings

The user initially selected both saved roles at High: “ultra is too much imo. let's go with both on high”. Later the user explicitly requested the final trial: “Astra Medium as orchestrator, Sol High as worker.”

That final trial used a dedicated Astra/Medium orchestration agent, a fresh Sol/High writer and a fresh Sol/High reviewer; the root retained infrastructure and Git ownership. The rate-limited writer was resumed after the user said “Limits reset, carry on”, rather than duplicated. Its result was preserved without reviewer rewrites.

> “It's stronger than Luna's and stronger than the old Claude variant too, in my opinion.”

This is the user's assessment of these examples. It is not a broad model benchmark or automatic adoption of the trial as campaign authority. The historical input and current skills remained available to both full-event writers, so neither experiment was context-free.

### Usage concern; Sol/Low was discussed only

> “Just this one thing took 46% of my 5h limit. Maybe Sol low? Just your opinion, don't start again.”

> “I'm not saying to try, I'm saying do you think it'd save on tokens?”

The answer was that Low should reduce reasoning-token use but not repeated input/context costs, with possible correction overhead. No Sol/Low trial or configuration change was requested or performed. The 46% is user-reported account-window consumption; per-agent token totals and its allocation across writing, research, orchestration and review were unavailable.

Ideas discussed, not implemented: use Astra directly in the main chat, consolidate overlapping skill context, reuse prepared source extracts and consider Sol/Low for bounded work. Do not launch another trial or rewrite the skill system from this discussion alone. Saved defaults still read Sol/High primary and Luna/High workers; the successful Astra/Sol trial was an explicit runtime override.

## Rules and Instructions

- Read this handoff and AGENTS.md at startup. The reset and rewrite decision supersedes Session 33's faction voice-run continuation instructions.
- User requested restoration followed by handoff; no fresh campaign rewriting belongs in this turn. Start the next selected rewrite only when requested.
- Keep D&D 2024, CR 2.0, zero-prep design, three remix pillars, quest/Act naming and the approved milestone ladder. Faction events award no Milestone Points.
- New prose uses current Ember blocks, named Event Outcomes with exact downstream names, character voice profiles and the prescribed prose pipeline. Restored legacy text is a historical input, not a replacement specification.
- Preserve Cassalanter secrecy, Bregan D'aerthe rejection of Lolth, Threestrings' Harper affiliation, members-only faction briefings and current NPC authorities when rewriting.
- Current quest journals remain the campaign's structural source; use active structure documents only for unconverted quests. Reconcile the deliberately restored faction drafts with current guides and NPC pages during each rewrite.
- Main session owns skills/configuration edits and commits. Assign explicit file ownership and verify worker claims. Use runtime-supported models/settings and available slots; never silently replace a requested model.
- Keep the user's five-agent cap and actual runtime cap. Resume existing workers after rate limits. Ordinary worker agents do not delegate.
- No separate no-ai-slop dependency. Ember voice takes precedence over rhythm suggestions from deslop/humanize.
- Markdown is the source format; no Foundry JSON or unsolicited viewer publishing. No file should be called final prose merely because a checker passed.
- Handoff is explicit-only, committed last, with authorized push/PR/merge attempted through normal Git operations. Never force-push. Use the known workspace's command-scoped safe.directory override.
- Preserve unrelated changes and record exact task-owned paths. No global Git trust or model configuration was changed in this session.

## Problems Solved

- Installed project orchestration and four reusable specialist roles while preserving global configuration.
- Completed three representative trials: a tightly scoped Luna revision, full Luna reconstruction and full Sol reconstruction with Astra orchestration.
- The limited trial's scope checker passed at its original baseline. Full trials used actual voice checks plus independent review; sentence metrics were not treated as proof of quality.
- Full Luna review caught disclosed assessment criteria, absolute new admission restrictions, missing public-register dialogue and GM visibility issues. A contaminated initial writer was discarded and a fresh writer completed the trial; unavoidable skill examples were disclosed.
- Sol supplied stronger scene coverage, explicit first-act dialogue, individual membership handling and hidden assessment criteria. Final voicecheck: no TELLs; narration 20.5, GM 20.0 and speech 10.3 words per sentence. Mirt's business profile permits short complete speech.
- Sol's review identified a clothing-recovery deadline gap and inherited safe-house access instructions that remain unspecified. The two-person admission limit is a consequential interpretation requiring a later design decision. Neither draft was repaired after the independent review.
- Reviewer assertions were checked against source evidence; the Giant-language opera is supported by RAW and was not treated as an invented detail.
- Reset verification compared every restored working-tree file with its original Git blob: 177/177 matched. The changed-path inventory matched the expected 161 exactly; whitespace checks passed. This verifies historical restoration, not campaign quality.
- The task began with a clean working tree. Only the requested faction subtree and restoration manifest changed in the reset commit; trials and other campaign materials were preserved.

## Outstanding Work

The prior checklist is carried below. Its two setup/trial items are now checked because this session completed them. Existing checked guide items are inherited historical records, not new verification. The old “finish voice run”, batch-ledger and brief-portability tasks are superseded as the immediate workflow by the full faction rewrite decision; retain them as historical tracking context rather than resume those batches. Other campaign problems remain unchecked until a rewrite or focused audit actually resolves them.

### Carried forward (Sessions 29–31)
- [ ] Verify the deployed Pages URL works for the user (a stale-cache report)
- [ ] **Bestiary:** never drafted. Pages reference Xanathar two-phase, Victoro and Ammalia, and Aurinax
- [ ] Quest journal conversions, one per structure doc:
  - [ ] Faction Outposts (arc-e)
  - [ ] Xanathar's Lair
  - [ ] Cassalanter Villa
  - [ ] Sea Maidens Faire
  - [ ] Kolat Towers
  - [ ] Vault of Dragons, plus a Scene 6 debrief for when Xanathar is GONE
- [ ] Guides and setting prose-writing pass:
  - [x] Players' Guide (Session 31)
  - [x] GM Guide (this session)
  - [ ] Trollskull Manor Guide
  - [ ] Setting: lore, history, grand-game, villains, organizations, Notable Figures
- [ ] Prose polish of the word-for-word NPC profile text in Notable Figures
- [ ] Mission 5/6 summaries on organization pages: missions now live in the Factions guide, so re-check there
- [ ] `sources/backgrounds.json` doesn't exist, but it's cited for the XPHB/FRHoF background tables. The Heroes of Faerûn background names are unchecked
- [ ] `ev-03` Ryvarra is visible only to parties with drow PCs or who pass the Yawning Portal check. Confirm that's intended now that BD recruitment is party-wide
- [ ] **Older faction-mission sidebars:** normalize to `> [!type]**Title**`. Some lack bold titles, for example `[!abstract]+ If a BD Operative Is Present`
- [ ] **Two GM-draft notes the superset agent flagged in Session 31:**
  - the Renaer's Confidence Holder text frames the secret differently from the player text
  - the GM Holder register doesn't match the polished prose

  Re-check both against the rewritten GM pages.

### Carried forward from Session 32
- [ ] **Ember organizations reference:** the user uploaded an Ember organizations JSON ("Here's how Ember writes organisations") for the organizations lore pass. It was ephemeral, so ask the user to re-upload it when that pass starts
- [ ] **Remi Haventree:** the Harpers Renown 1 benefit gives her North Ward safe house, and rank events r10/r50 show her in that role, but her identity is meant to stay hidden until Harpers Mission 4. Decide how the safe house works before M4
- [ ] **The Sleeping Asset** (Harpers m05): the Factions guide and s01 say the Harper double agent is exposed there, but m05 has no such beat. Add it
- [ ] **BD guide `08-bregan-daerthe.md` line ~15:** "At Renown 5+: *Scarlet Marpenoth* extraction" doesn't match any BD rank (3/10/25/50). Decide on 3+ or 10+
- [ ] **BD Mission 6:** the Factions page summary mismatches the mission (limpet charge vs the Eye #3 wreck); the windmill is in the North Ward vs the Southern Ward (Coachlamp Lane)
- [ ] **Trollskull Manor Guide `01-overview.md`:** check its Founders' Day wording against the Structural Rules calendar
- [ ] **Asmodean Shrine:** keyed Area 3 is missing (Cassalanter temple). Also check the Samara and Illuun Notable Figures pages
- [ ] **Existing faction missions (m01–m06)** still carry `#### Milestone: None` blocks. The new events have none. Decide whether to strip them for consistency
- [ ] **Doom Raiders Viper rank:** the rank lists "veteran" muscle, while Yagra's Notable Figures page says Thug (with modifications). Reconcile
- [ ] **Order of the Gauntlet m06:** GM text mentions Lord Victoro's "contract-bound infernal patron". That's GM truth, but check no in-fiction character states it (Cassalanter secrecy)
- [ ] **Invented NPCs and details to accept or replace** (not blocking):
  - Lords' Alliance: Sevel Dastar
  - Force Grey: Aldris Maeven, Rhendar Solne, Merris
  - Bregan D'aerthe: Ilphrin Quiss, Pelsha and Vorn, Sarev Oust
  - Order of the Gauntlet: Tobrin
  - Emerald Enclave: Sarna Dath, Bertio Caskwall
  - Savra's cult history and the Howling Hatred ranks (OotG s02)
  - three near-parallel Mad Mage choices at Renown 50: LA "Undermountain Commission", EE "Illuun Watch", OotG "Undermountain Mandate"

---

### New continuation work from the intervening commits and Codex migration

- [ ] Finish the faction voice run: H3, D3, B4, E3, F2–F4, L1–L4 and O3. Inspect “See handoff” batches first; do not overwrite partially changed files on an assumption that no work exists.
- [ ] Update the batch ledger to record D2 as merged and reconcile the ambiguous batch statuses against actual event contents.
- [ ] Make `.claude/briefs/voice-run/qa_batch.py` portable: it still hardcodes `/home/user/waterdeep`, invokes python3, reads text without explicit UTF-8 and uses Git without this host's ownership override.
- [ ] Update the voice-run brief/batch continuation instructions for Codex agent APIs, AGENTS.md, resolved global skill resources and the actual Windows workspace. Preserve its editorial requirements and baseline commit.
- [x] Choose and configure exact orchestrator/worker model IDs and reasoning levels with the user; Sol/Luna are currently a recommendation only.
- [x] Run a representative worker-generated campaign task and independently review factual preservation, Ember structure, voice and outcome-reader links. Mechanical validation and temporary rendering have passed; model behavior has not been demonstrated.
- [ ] Make repaired global skills reproducible on another machine. They live under `C:/Users/lupur/.agents/skills/`, outside Git; the repair script depends on this user's paths and existing imported manifests. Consider project-scoped packaging once requested.
- [ ] Review remaining conceptual-only legacy automation reference files before using any of their configuration examples; the recommender explicitly requires current official documentation.
- [ ] Configure and authenticate Foundry/Plutonium MCP connections if needed. The import found permission intents but no actual server definitions.
- [ ] Resolve the third-party cached instruction-file size warnings if those plugins become relevant. Do not confuse them with failed imported skills.
- [ ] Verify inherited Session 32 campaign items against the intervening voice-run changes before marking them complete. The checklist below was carried verbatim rather than optimistically closed from commit subjects.
- [ ] Complete this handoff's GitHub push, PR and merge after authentication is available. Update local master by fast-forward and verify Session 33 exists on origin/master.

### New continuation items from Session 34

- [ ] Rewrite faction events from the restored initial drafts under current skills and campaign decisions, beginning with the faction/event the user selects. Do not assume the old partially completed batch order remains approved.
- [ ] Reconcile each rewrite's legacy flags, milestone blocks, secrecy, timing, alignments, named outcomes and downstream readers against current guides/NPCs; the reset intentionally removed later corrections within this subtree.
- [ ] Before using Sol's trial as an example or adapting it into production, settle the two-ticket participation choice, viable clothing-recovery timing and safe-house access procedure. Do not silently accept its new design choices.
- [ ] If the user chooses a permanent Astra/Sol or Sol/Low setup, update the saved defaults and orchestration documentation together. No permanent replacement was selected by the final trial or token-cost question.
- [ ] Complete authenticated delivery of Sessions 33 and 34: push `codex/session-33-handoff`, create/attach a PR to `master`, check and merge it, fast-forward local master and verify both handoffs on origin/master.

## Warnings and Caveats

- Exact restoration deliberately reinstates legacy structures and may reintroduce previously fixed campaign errors. The old voice-run ledger and Session 33's merged-batch table no longer describe the working faction-event text. Current campaign rules remain authoritative for rewrites.
- Files outside faction events were not rolled back. Guides, Notable Figures and unconverted quest documents can disagree with the historical event versions; investigate these dependencies during rewriting.
- `scripts/check-harpers-trial.py` expects the pre-reset production SHA-256 `2c2b3afd287c2240e34a67ae42e586392efd3a96ea4815b9cb93bd864817c795` and will now fail by design. Do not “fix” that expected value to pretend the old trial is still comparable. Reproduce it at its historical baseline if needed.
- `docs/index.html` was not rebuilt and can still show the pre-reset content. Source Markdown and this handoff describe the new state; no viewer refresh or Foundry export was requested.
- The restored drafts were not run through a rewriting/polish pipeline, which would violate exact restoration. No new campaign prose was drafted in the reset task. Existing style/continuity defects remain rewrite work.
- Global imported skills remain outside Git under `C:/Users/lupur/.agents/skills/`; their portability and earlier migration caveats from Session 33 remain unresolved.
- The three full/scoped trial reports document actual source and isolation limits. No per-model cost ratio, measured token saving or broad ranking was established.
- **Delivery blocker verified now:** GitHub CLI reports no logged-in hosts. Network access works outside the sandbox, and `origin` still advertises `master` at `0d7ddf878d2a4dedee5077f5384848139ff1b522`. A noninteractive authenticated push dry run failed with “could not read Username for 'https://github.com': terminal prompts disabled”. A prior interactive dry run was interrupted after waiting without output. No remote write succeeded.
- Origin is `https://github.com/friendlysgames/waterdeep.git`. Current branch is `codex/session-33-handoff`, retained to deliver the unpushed Session 33 work and this continuation together. Local master remains at `a78bcf3`; it was not updated. No PR was created or merged.

## Where to Start Next Session

1. Read AGENTS.md and this handoff. Treat `campaign/quests/faction-events/` as original drafts awaiting rewrite, and consult `docs/maintenance/faction-events-initial-state-2026-09-26.json` for exact provenance.
2. If GitHub login is available, finish the existing branch's push/PR/merge delivery; do not create another handoff just to deliver this one. Verify checks/conflicts, attach the PR, merge normally and fast-forward local master.
3. Follow the user's next selected rewrite. Preserve the current skills, source research, explicit outcomes and campaign consistency requirements; do not resume the historical voice batches automatically.
4. For the preferred writing example, read `docs/trials/harpers-first-meeting-from-scratch-sol-high.md` with its Astra/Sol assessment. It is a reference trial with unresolved decisions, not the current production event.
5. Remember that Sol/Low was an opinion question only. Use explicit runtime choices or clarify the permanent pairing when a new configuration task is requested; do not claim Low has been tested.
6. Preserve the remaining campaign backlog above. Do not begin Faction Outposts, bestiary work, skill consolidation or another model trial without the relevant user request.
