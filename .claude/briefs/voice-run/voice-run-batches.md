# Voice run batches

All paths are under `campaign/quests/faction-events/`. The run converts every Faction Event to the Ember block model and voice; the brief is `voice-run-brief.md` in this folder, and every agent reads it first.

## Procedure per batch

1. Launch one `prose-drafter` agent per batch with the brief and the batch's folders. Never run more than 5 agents at once.
2. When it reports, run the QA from the repo root:
   - `python3 .claude/briefs/voice-run/qa_batch.py <faction>/<folder> ...` checks for facts missing against the baseline commit in `voice-run-baseline.txt`, undefined outcomes, retired syntax, render problems and voicecheck TELLs.
   - `python3 .claude/briefs/voice-run/align_audit.py <faction>/<folder>` (relative to faction-events; a full path silently matches nothing) checks social-block alignments against the Notable Figures pages.
   - Check every "missing tokens" DC or number by hand against `git show <baseline>:<path>`. Most missing tokens are just retired headings; lost DCs, numbers and stat-block names are real.
   - Also check narration averages: anything well under Ember's 21 words a sentence is choppy and goes back to the agent.
3. Apply small fixes yourself. Send anything larger back to the same agent with SendMessage.
4. Commit only that batch's folders, then PR and merge.

## Status

| Batch | Folders | Status |
|---|---|---|
| H1 | harpers: m01, m02, m03 | Merged |
| H2 | harpers: m04, m05 | Merged |
| H3 | harpers: m06, r03, r10, r25, r50, s01 | Merged |
| D1 | doom-raiders: 00-first-meeting, m01 (overview + design-notes; ev-01 is the pilot), m02, m03 | Merged |
| D2 | doom-raiders: m04, m05 | Merged |
| D3 | doom-raiders: m06, r03, r10, r25, r50, s01, s02 | Merged |
| B1 | bregan-daerthe: 00-first-meeting, m01, m02 | Merged |
| B2 | bregan-daerthe: m02b, m03, m04 | Merged |
| B3 | bregan-daerthe: m05, m06 | Merged |
| B4 | bregan-daerthe: r03, r10, r25, r50, s01, s02, s03, s04 | Not started |
| E1 | emerald-enclave: 00-first-meeting, m01, m02, m03 | Merged |
| E2 | emerald-enclave: m04, m05, m06 | Merged |
| E3 | emerald-enclave: r03, r10, r25, r50, s01, s02 | Merged |
| F1 | force-grey: 00-first-meeting, m01, m02 | Merged |
| F2 | force-grey: m03, m04 | Merged |
| F3 | force-grey: m05, m06, s01 | Not started |
| F4 | force-grey: r03, r10, r25, r50 | Not started |
| L1 | lords-alliance: 00-first-meeting, m01, m02 | Not started |
| L2 | lords-alliance: m03, m04, m05 | Not started |
| L3 | lords-alliance: m06, s01, s02 | Not started |
| L4 | lords-alliance: r03, r10, r25, r50 | Not started |
| O1 | order-of-the-gauntlet: 00-first-meeting, m01, m02, m03 | Merged |
| O2 | order-of-the-gauntlet: m04, m05, m06 | Merged |
| O3 | order-of-the-gauntlet: r03, r10, r25, r50, s01, s02 | Not started |

After the last batch, rebuild the viewer (`python3 scripts/build-viewer.py`), then PR and merge.
