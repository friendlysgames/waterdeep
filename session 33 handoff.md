# Session 33 Handoff

## What Was Done

This session rebuilt how the campaign sounds. The user said the boxed text read as AI-written, so the main session wrote two new skills.

- **`ember-voice`** is Ember's measured writing voice. It sets sentence-length targets and catalogues the AI tells, and it comes with the `voicecheck.py` checker.
- **`character-voices`** is a voice profile for every Notable Figure: 123 profiles across 15 docs. Each profile has a three-part swearing rating: Frequency, Creativity and Length.

The older polish skills were changed to defer to `ember-voice`.

Several standing rules were set:
- real profanity for an adult table
- Cassalanter secrecy tightened to suspicion only
- the Order of the Gauntlet hunts infernalists in general
- Bregan D'aerthe rejects Lolth

The two pilots (Harpers First Meeting, Doom Raiders Mission 1) were rewritten to the new voice. Then the **Faction Events voice run** started: every faction event gets converted to the Ember block model, and every NPC speaks in their profile voice.

16 of 24 batches are merged (PRs #20–#35). The Harpers, Doom Raiders and Order of the Gauntlet are finished except the Order's rank-up and standalone events. The Emerald Enclave is finished. Bregan D'aerthe and Force Grey are partly done. The Lords' Alliance hasn't started.

The run's brief, batch list, baseline commit and QA scripts are now in the repo at `.claude/briefs/voice-run/`.

## Changes Made

`git log b7d4d18..HEAD` covers 59 commits.

| Files | Change |
|---|---|
| `.claude/skills/ember-voice/SKILL.md`, `scripts/voicecheck.py` | New skill: Ember voice targets (narration ~21 words/sentence, speech ~14.5), the AI-tell catalogue, voice per block type, and a checker. "Quietly" is flagged only as a non-committal hedge. |
| `.claude/skills/character-voices/SKILL.md`, `voices/*.md` (15 docs) | New skill: 123 voice profiles. Swearing is rated *Frequency · Creativity · Length*; ten characters get Scotsman-level Tirades. |
| `humanize-prose`, `deslop-text`, `ttrpg-sourcebook-style`, `dnd-adventure-text`, `ember-adventure-style`, `ember-setting-style`, `adventure-reloaded` | Now defer to ember-voice on rhythm. adventure-reloaded adds the readaloud density rule and "missions open with The Brief". |
| `.claude/agents/prose-drafter.md`, `prose-polisher.md` | Load ember-voice and character-voices. |
| `CLAUDE.md` | New rules: Ember voice; Adult table, real profanity; Skills are written by the main session; Bregan D'aerthe rejects Lolth. Skills table updated. |
| `campaign/quests/faction-events/harpers/**` | All events converted (H1–H3). |
| `campaign/quests/faction-events/doom-raiders/**` | All events converted (D1–D3); the m01 event is the pilot. |
| `campaign/quests/faction-events/emerald-enclave/**` | All events converted (E1–E3). |
| `campaign/quests/faction-events/order-of-the-gauntlet/` 00, m01–m06 | Converted (O1–O2). |
| `campaign/quests/faction-events/bregan-daerthe/` 00, m01–m06, m02b | Converted (B1–B3). The Wazoo exposé now alleges only hidden gold and vanished servants. |
| `campaign/quests/faction-events/force-grey/` 00, m01–m04 | Converted (F1–F2). |
| `campaign/setting/notable-figures/…/02-sister-valdra.md`, Savra's page, `organizations/04-order-of-the-gauntlet.md`, `guides/factions/05-order-of-the-gauntlet.md`, `guides/factions/08-bregan-daerthe.md` | Cassalanter secrecy: evidence shows only "something badly wrong"; the Order hunts infernalists in general. |
| `notable-figures/bregan-daerthe/02-soluun-xibrindas.md`, `voices/bregan-daerthe.md`, `locations/sea-maidens-faire/05-scarlet-marpenoth.md` | Soluun no longer worships Lolth. His zeal goes to Jarlaxle, and his stateroom has no shrine. |
| `.claude/briefs/voice-run/` | Brief, batch status, baseline commit, `qa_batch.py`, `align_audit.py`. |

## Key Decisions

- **Build a real voice skill.**
  - *Decision:* build `ember-voice` rather than patching the structure skills.
  - *Reasoning:* the skills focused on structure, not writing style.
  - *User:* "All the boxed text is obviously written by AI, so obvious it hurts." / "we need a proper 'ember voicing' for everything. The skills focus a lot on structure, not on actual writing style."
- **"Quietly" is a hedge tell only.**
  - *Decision:* flag it only when it's a non-committal crutch.
  - *Reasoning:* literal quiet is ordinary description.
  - *User:* "The tell is specifically for when it's used as a crutch to be non-commital. If somethis is actually quiet, like moving quietly, that's more than fine."
- **Character voices for all 122 Notable Figures, written by the main session.**
  - *User:* "how every single character in this adventure speaks … any phrases they might repeat often"; "I write all of it"; "When you get to it, write the skill yourself."
- **Real profanity.**
  - *User:* "all my players will be adults. Never be scared to actually use profanity. Say fuck, shit, pussy, cunt, whatever the character needs to say."
  - The swearing ratings (creativity and length) came from the user: "curse creativity", and "short curses and Scottsman level curses (samurai jack)".
- **Cassalanter secrecy is suspicion only; the Order hunts infernalists in general.**
  - *User:* "Infernalists in general, suspicious of the cassalanters but nothing that points to them being infernalists."
  - The party makes the discovery itself: Gysheer's extraction in OotG Mission 4, then the ledger in Mission 5.
- **Davil's line.**
  - *Decision:* Davil says "…you don't have that complication. Yet."
  - *Reasoning:* the party are becoming Zhents.
- **Bregan D'aerthe rejects Lolth.**
  - *User:* "A big, very important thung: Bregan D'aerthe *rejects* Lolth as their goddess."
- **Run the voice run with agents.**
  - *Decision:* 5 agents at a time, and each batch is reviewed, PR'd and merged on its own.
  - *User:* "keep working until all missions are done, 5 agents at a time. Each time an agent is done, PR and merge."
- **Stop after the current batches and put the brief on GitHub.**
  - *User:* "stop after this batch, pr, merge, then handout" / "add the voice run brief to the github and the handoff".

## Rules and Instructions

Carried forward from Session 32: Cassalanter secrecy; the 5-agent cap; faction mechanics vs lore; the About This Campaign exception to the superset rule; tendays, never weeks; handoff delivery as the last commit, pushed, PR'd and merged.

Superseded by this session's block model: the Session 32 sidebar form and the "binary flags" faction-event format. Event Outcomes and the six Ember blocks now apply.

New this session:
- **Ember voice for all prose.**
  - Run `voicecheck.py` on every drafted file.
  - Fix every TELL before committing.
  - Never polish prose into short punchy sentences.
- **Adult table, real profanity.** Swearing follows each character's `character-voices` rating. Narration stays clean.
- **Skills are written by the main session**, never by agents.
- **Bregan D'aerthe rejects Lolth.** Members speak of her with contempt. No shrines, and no devotion.
- **Social-block alignment and ancestry** are copied from the Notable Figures page and never guessed. Where an NPC has no page, leave the alignment out.
- **Missions open with `### The Brief`.** The contact gives the job in their profile voice. A message brief (flying snake, *Sending*, animal messenger) is written verbatim.
- **Keep every DC in standard form** and every number, stat block and outcome name. Don't invent checks.

## Problems Solved

- **Agents invented facts, dropped facts or guessed alignments.** Review caught and fixed each one:
  - **Invented:**
    - the victim name "Coram"
    - five DCs in Force Grey Mission 4
    - an invented outcome in Harpers Mission 4 (to confirm)
  - **Dropped:**
    - the Spy stat block (BD Mission 6)
    - the Cult Fanatic and Priest stat blocks (OotG Missions 4 and 6)
    - the Renown 30+ benefit (Harpers Mission 5)
    - Nihiloor's 50% presence and Day 7 (Force Grey Missions 3–4)
    - DC 14 Intelligence (DR r25)
    - "DC 12 with Yagra's guidance" (DR Mission 6)
    - DC 12 Perception paraphrased into a passive score (Harpers Mission 4)
  - **Guessed alignments:**
    - Melannor, Threestrings, Ambrose, Skeemo, Maxeene, Seffia, Kreb, Ott (a dwarf, not a halfling)
    - Remi, Jelenn, Corene, Hlam, Zelifarn
- **The alignment audit silently checked nothing.** It takes paths relative to faction-events; full paths match nothing and print nothing. A sweep found the last five mismatches above, and the script now documents the correct call.
- **Choppy narration** (9–14 words a sentence, fragment stacks, "not X, it's Y" in speech) was sent back and rewritten. This affected EE r50, Force Grey Missions 3–4, Harpers s01 and r50, and EE s01 (rewritten by the main session).
- **Secrecy leaks fixed:**
  - the Wazoo exposé
  - the O1 imp Summary
  - Sister Valdra's "Asmodeus worship"
  - the Order's guide and organization page

## Outstanding Work

### Voice run: 8 batches left
Status and procedure are in `.claude/briefs/voice-run/voice-run-batches.md`, and the brief is `voice-run-brief.md` in the same folder.

- [ ] B4 bregan-daerthe: r03, r10, r25, r50, s01–s04
- [ ] F3 force-grey: m05, m06, s01
- [ ] F4 force-grey: r03, r10, r25, r50
- [ ] L1 lords-alliance: 00-first-meeting, m01, m02
- [ ] L2 lords-alliance: m03, m04, m05
- [ ] L3 lords-alliance: m06, s01, s02
- [ ] L4 lords-alliance: r03, r10, r25, r50
- [ ] O3 order-of-the-gauntlet: r03, r10, r25, r50, s01, s02
- [ ] After the last batch: `python3 scripts/build-viewer.py`, then PR and merge.
- [ ] **Two TELLs in earlier-merged Doom Raiders files:**
  - `00-first-meeting/ev-01` L108 ('quietly')
  - `m03-the-missing-snobeedle/ev-01` L173 (not-X)

  Fix them in the next run.
- [ ] **"Quietly" outside the merged batches:** in force-grey `r10-senior-griffon` and the m05 files. F3 and F4 will cover them.

### Decisions for the user
- [ ] **Zelifarn's stat block:** Force Grey Mission 2 uses Young Bronze Dragon; his Notable Figures page says a young sea dragon (bronze-scaled). Pick one.
- [ ] **New outcome names:** agents created outcomes where the old files had only renown conditions. Examples: "Jarlaxle Cover Profile Documented" (Harpers Mission 4), "Court Cleared", "Mirt's Study Complete", "Harper Leak Known". Confirm or rename.
- [ ] **NPCs with no Notable Figures page or voice profile:** J.B. Nevercott, Gysheer Omfreys (given Lawful Evil from her Cult Fanatic block), Florette Cressyn, Brimel Crestfall, Krenick Durr, Vevette Blackwater. Give them pages or profiles?
- [ ] **When the party learns the Cassalanter name:** Gysheer's extraction in OotG Mission 4 gives it, and the Mission 5 ledger confirms the infernalism. The Order's guide says Mission 5 is where the party discovers the link. Consistent in spirit; confirm the wording.
- [ ] **Brimel's motive:** the BD Mission 5 overview once said he was "paid", while the event says he "agreed". The agent went with "agreed". Check other files for "paid".

### Carried forward (Sessions 29–32, unchanged)
- [ ] Verify the deployed Pages URL works for the user (a stale-cache report)
- [ ] **Bestiary:** never drafted. Pages reference Xanathar two-phase, Victoro and Ammalia, and Aurinax
- [ ] Quest journal conversions:
  - [ ] Faction Outposts
  - [ ] Xanathar's Lair
  - [ ] Cassalanter Villa
  - [ ] Sea Maidens Faire
  - [ ] Kolat Towers
  - [ ] Vault of Dragons, plus a Scene 6 debrief for when Xanathar is GONE
- [ ] Prose-writing pass:
  - [ ] Trollskull Manor Guide
  - [ ] Setting: lore, history, grand-game, villains, organizations, Notable Figures
- [ ] Prose polish of the word-for-word NPC profile text in Notable Figures
- [ ] Mission 5/6 summaries on organization pages: missions now live in the Factions guide, so re-check there
- [ ] `sources/backgrounds.json` is missing. The Heroes of Faerûn background names are unchecked
- [ ] `ev-03` Ryvarra is visible only to parties with drow PCs or who pass the Yawning Portal check. Confirm that's intended now that BD recruitment is party-wide
- [ ] Older faction-mission sidebars: largely superseded by the voice run. Re-check anything the run doesn't touch
- [ ] Two GM-draft notes from Session 31 (Renaer's Confidence Holder text; GM Holder register)
- [ ] **Ember organizations reference JSON:** ask the user to re-upload it when the organizations pass starts
- [ ] **Remi Haventree:** the Renown 1 safe house vs her identity staying hidden until Harpers Mission 4
- [ ] **The Sleeping Asset** (Harpers m05): the double-agent exposure beat is missing
- [ ] **BD guide line ~15:** "Renown 5+" doesn't match any BD rank
- [ ] **BD Mission 6:** the Factions page summary vs the mission; the windmill's ward
- [ ] **Trollskull Manor Guide `01-overview.md`:** check its Founders' Day wording
- [ ] **Asmodean Shrine:** keyed Area 3 is missing. Also check the Samara and Illuun Notable Figures pages
- [ ] Faction missions still carrying `#### Milestone: None` blocks: the voice run is removing them as it goes
- [ ] **Doom Raiders Viper rank:** "veteran" muscle vs Yagra's Thug stat block
- [ ] **Order of the Gauntlet m06:** check that no in-fiction character states the "contract-bound infernal patron"
- [ ] **Invented NPCs from Session 32** to accept or replace: Sevel Dastar, Aldris Maeven, Rhendar Solne, Merris, Ilphrin Quiss, Pelsha and Vorn, Sarev Oust, Tobrin, Sarna Dath, Bertio Caskwall, Savra's cult history, and the three parallel Renown 50 Mad Mage choices

## Warnings and Caveats

- **Agents drop and invent facts on every batch.** Never merge without running all three:
  - `qa_batch.py`
  - the DC/number diff against the baseline commit (`96123df`)
  - `align_audit.py <faction>/`

  "Missing tokens" are mostly retired headings. Missing DCs, numbers and stat-block names are real.
- **The DC-count diff reads loose forms as "new".** A "DC 12 check" with no ability named doesn't match the regex, so the standard-form rewrite looks invented. Check the baseline before telling an agent to remove a DC (DR Mission 6 was almost broken this way).
- **Narration averages are a real signal.** Anything well under 21 words a sentence has been choppy and full of tells every time, even when voicecheck passes.
- **Event Outcome names are read by the unconverted structure docs.** Keep them exact. New names created this session will need matching when those quests are converted.
- **Stop hook:** it complains while agents have files mid-edit. Commit only reviewed batches; ignore the hook until then.
- **Usage limits:** agents stop on the account-wide rate limit. Resume the same agent with SendMessage after the reset; never take its work over inline.

## Where to Start Next Session

1. Read this handoff and CLAUDE.md, then wait for the user to name the task.
2. If they say to continue the voice run:
   1. Read `.claude/briefs/voice-run/voice-run-batches.md` and `voice-run-brief.md`.
   2. Launch up to 5 `prose-drafter` agents on B4, F3, F4, O3 and L1. Each gets the brief path and its folders, as in the batch list.
   3. As each finishes, run the procedure in the batch doc, then commit its folders, PR and merge.
   4. Queue L2–L4 as slots free.
3. After the last batch, fix the two DR tells listed above, rebuild the viewer, and do a final PR.
