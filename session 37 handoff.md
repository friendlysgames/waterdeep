# Session 37 Handoff
**Date:** 2026-09-30
**Status:** Ready to continue. The Harper voice pass is done. The knowledge-gate audit is recorded, and six design decisions are waiting on the user.

---

## What Was Done

This session voice-passed all 33 Harper faction-event files to Ember voice and each NPC's `character-voices` profile. Agents did the rewriting, and every folder was checked with `voicecheck.py` plus a script that confirms every mechanic, time, DC, outcome name, heading, block tag and link survived. The inconsistencies the voice pass surfaced were then fixed: House Ulbrinter's ward, Maxeene's speech, Vell's mission, a near-duplicate courier name, and a false Cassalanter reader on a Harper M2 outcome. The out-of-scope notes file that Session 35 relied on was never in this repo, so it was rebuilt from a fresh five-agent, read-only audit of the whole campaign. The audit checked the Manshoon knowledge gate, Cassalanter secrecy and individual membership, and ends with six decisions for the user.

---

## Changes Made

Git range: `git log 8cf6359..HEAD` (the base is the Session 36 handoff commit).

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/quests/faction-events/harpers/**` (all 33 files) | Ember voice pass. Defensive "rules-lawyer" GM text became positive briefing, and NPC speech follows the `character-voices` profiles. Mirt has two gears: bawdy in public, terse on business. Readalouds open on the place and end in motion. Speech sentence length is back in Ember range in every file. |
| `harpers/s01-the-cell-is-compromised/*` | Mirt now says "a couple of days" aloud. The exact 48-hour leak delay is in GM text only. |
| `harpers/m04-a-friends-house/overview.md`, `ev-01-the-salon.md`, `design-notes.md` | House Ulbrinter moved from the Sea Ward to Delzorin Street in the North Ward (WDH and Appendix C). The discrepancy note is replaced. |
| `harpers/m02-the-dead-drop/ev-01…`, `overview.md`, `design-notes.md`; `m03…/ev-02-the-tail.md` | **Harper Contacts Relocated** now names its real reader, **The Tail**. The Cassalanter Villa claim is gone. |
| `harpers/r50-high-harper/ev-01-high-harper.md` | The courier Oren Bell is renamed Oswin Bell, so he can't be confused with Orren Vale. |
| `campaign/setting/notable-figures/harpers/08-maxeene.md`, `campaign/setting/organizations/01-harpers.md` | Maxeene has Intelligence 10 and speaks Common through a druid's permanent enchantment, matching WDH and M1. The Talking Mare is mission one, not two. |
| `.claude/skills/character-voices/voices/harpers.md` | Maxeene's Sound line now says she speaks Common. The main session made this edit, because skills are main-session work. |
| `campaign/guides/gm-guide/design-notes-running-the-campaign.md` | Vell is now listed as **The Talking Mare** antagonist, not **The Dead Drop**'s. |

### Files Created
| File | Purpose |
|------|---------|
| `docs/plans/harpers-out-of-scope-notes.md` | Rebuilt audit of rules R1 (Manshoon gate), R2 (Cassalanter secrecy) and R3 (individual membership) across every non-Harper page, with file:line findings, severities, suggested fixes and a closing "Decisions Needed Before Fixing" list. No campaign file was changed by the audit. |

---

## Key Decisions

### A voice pass keeps content fixed
**Decision:** The pass changed sentences, not facts. Agents were told to preserve every mechanic and bold outcome name. The main session verified each folder with a token-diff script before committing.
**Reasoning:** Session 35 had accepted the Harper content, so only the voice was in question.
> "I want you to do a voice pass on the Harper factions events." — User, this session

### Fix inconsistencies against the sources
**Decision:** Where a Harper page and WDH disagreed, WDH won: the Ulbrinter ward, and Maxeene's speech. The M2 outcome that pointed at a non-existent reader was retargeted to **The Tail**, the reader that already exists, instead of inventing Cassalanter content.
> "fix the inconsistencies" — User, this session

### Agents do the work, including research
**Decision:** After the user's correction, all research and edits went to agents. The main session only planned, reviewed, made one-line fixes and committed.
> "what did I say about doing the work yourself vs letting agents to the work? Including research work" — User, this session

### Rebuild the out-of-scope notes, but fix nothing yet
**Decision:** The notes were rebuilt as an audit only. Fixing waits for the user's answers to the six decisions at the end of the notes file.
> "the out of scope notes were inconsistencies found in other event files, such as, for example, a new rule that nobody knows that Manshoon is the one leading the splinter. The Doom Raiders believe Floxin is the splinter leader, other factions know very little in general." — User, this session

---

## Rules and Instructions

All earlier rules stay in force (CLAUDE.md, Sessions 35 and 36). Reinforced or added this session:

- **Agents do all research and drafting.** The main session reviews, applies one-line fixes and commits. Grep-based fact-finding counts as research, so delegate it. *(User quote above.)*
- **Manshoon knowledge gate.** At the start, nobody knows Manshoon leads the splinter. The Doom Raiders believe Floxin does. Everyone else knows only that the Black Network has split. *(User quote above.)*
- **Voice-pass verification.** Before committing any voice pass, run `voicecheck.py` and a token diff against HEAD. The diff covers DCs, times, bold names, headings, block tags, links, gp, feet and Renown. A folder fails if speech averages under 12 words a sentence or narration under 18. Don't accept agent padding such as forced "so… because" joins used to hit the number (ember-voice §10).
- **Skill files are edited by the main session** (CLAUDE.md). This session's only skill edit was the Maxeene profile line.

---

## Problems Solved

- **Machine-sounding Harper prose that passed the checker.** The GM text argued with an imagined auditor ("no combat award is invented for an absent fight"), and NPCs recited disclaimers. Agents rewrote it. M3, M5, M6 and S01 needed a second round to bring clipped speech into range. The main session undid M6's forced joins and lengthened the last clipped lines in R50.
- **The checker's false positive:** "the weight of the rubies" in M4 was literal, and was reworded.
- **Ulbrinter in the Sea Ward, Maxeene needing *Speak with Animals*, Vell in the wrong mission, Oren/Orren, and the false Cassalanter reader** were all fixed. See Changes Made.
- **The missing out-of-scope notes file** is rebuilt.
- **Session 35 delivery:** confirmed that `session 35 handoff.md` is on `origin/master`.

---

## Outstanding Work

### New this session
- [ ] **Answer the six decisions** at the end of `docs/plans/harpers-out-of-scope-notes.md`:
  - whether villains count under the gate
  - whether the Manshoon reveal becomes a hard gate via a **Manshoon Named** outcome
  - which act owns the first Cassalanter cult evidence
  - OotG M5/M6 pact terms
  - BD Contact Severed scope
  - the level-gate conflicts

  Then fix the findings, one faction or area at a time, with agents.
- [ ] **Write the Floxin belief into the Doom Raiders.** No Doom Raiders page carries it. Davil's First Meeting, Davil's Arrest, Wolf, the Doom Raiders guide and organization page, Davil's and Yagra's NPC pages, Trollskull ev-04 and Fireball ev-01 all name Manshoon instead.
- [ ] **One-faction membership.** Four guide pages still allow a PC in several factions: `players-guide/faction-affiliations.md:3`, `gm-guide/player-factions-overview.md:3`, `factions/01-overview.md:7, :9`, and `trollskull-manor/02-operating-costs.md:31`. Fix them once the user confirms.
- [ ] **Wire the Harper outcomes into their named readers** when each lair doc is converted. The notes list them per quest.
- [ ] **Minor Harper NPCs have no voice profiles or Notable Figures pages:** Uza, Tessalar, Orren, Harl Keen, Nella, Orin and others. Add profiles if they recur.
- [ ] The Finding Floon "two nights" and Gralhund "two tendays" timeline slips, and the other non-rule inconsistencies (Vajra's alignment and origin, Istrid's loan, Yellowspire's ward, BD mission numbering, the coin-pouch timing). All are listed in the notes.

### Carried forward from Session 36
- [ ] Confirm the Ember styling on the live GitHub Pages site after merge: fonts, block frames and phone layout.
- [ ] If the `update-campaign-viewer` Artifact publish is used again, publish `ember.css` and `assets/` through the Artifact `files` map.
- [ ] Finding Floon and Trollskull Alley pages still use the old `> **[GM]**` zones and need conversion to the Ember block model.

### Carried forward from Sessions 29–31
- [ ] Verify the previously deployed Pages URL works for the user after the stale-cache report.
- [ ] **Bestiary:** never drafted (Xanathar two-phase, Victoro and Ammalia, Aurinax).
- [ ] Convert the remaining quest structure docs into journals: Faction Outposts, Xanathar's Lair, Cassalanter Villa, Sea Maidens Faire, Kolat Towers, and Vault of Dragons (including a Scene 6 debrief if Xanathar is GONE).
- [ ] Guides and setting prose pass: the Trollskull Manor Guide, and setting lore, history, grand-game, villains, organizations and Notable Figures.
- [ ] Prose polish the word-for-word NPC profile text in Notable Figures.
- [ ] Recheck the Mission 5/6 summaries on organization pages against the Factions Guide.
- [ ] Resolve the missing `sources/backgrounds.json` and verify Heroes of Faerûn background names.
- [ ] Confirm the intended BD `ev-03` Ryvarra visibility under individual membership.
- [ ] Normalize older faction-mission sidebar titles to `> [!type]**Title**` outside the Harper folders.
- [ ] Recheck the GM Renaer's Confidence Holder framing against the rewritten GM pages.

### Carried forward from Session 32
- [ ] Ask for the ephemeral Ember organizations JSON again when the organizations lore pass starts.
- [ ] Reconcile BD guide `08-bregan-daerthe.md` Renown 5+ *Scarlet Marpenoth* extraction with the rank thresholds 3/10/25/50.
- [ ] Reconcile the BD M6 limpet-charge / Eye #3 wreck summary, and the North Ward versus Southern Ward windmill location.
- [ ] Check the Trollskull Manor Guide `01-overview.md` Founders' Day wording against the Structural Rules calendar.
- [ ] Add the missing keyed Area 3 in the Asmodean Shrine, and check the Samara and Illuun Notable Figures pages.
- [ ] Decide whether to remove the remaining `#### Milestone: None` blocks in other factions' m01–m06 events.
- [ ] Reconcile the Doom Raider Viper "veteran" muscle with Yagra's modified Thug profile.
- [ ] OotG M6 "contractual counterpart / infernal patron": now recorded in the notes (Order of the Gauntlet section, decision 4).
- [ ] Accept or replace the earlier invented details: LA Sevel Dastar; Force Grey Aldris Maeven, Rhendar Solne and Merris; BD Ilphrin Quiss, Pelsha and Vorn, Sarev Oust; OotG Tobrin; EE Sarna Dath and Bertio Caskwall; Savra's cult/Howling Hatred ranks; and the three near-parallel Renown 50 Mad Mage choices.

### Carried forward from Sessions 33–35
- [ ] Complete the other six factions' event rewrites, one approved plan at a time. Fold in the notes-file findings for each faction as it is selected.
- [ ] If retaining the historical voice-run tooling, make `.claude/briefs/voice-run/qa_batch.py` portable.
- [ ] Make the imported global skills reproducible on another machine if requested.
- [ ] Review the conceptual-only legacy automation references before using them.
- [ ] Recheck inherited Session 32 items against each later faction rewrite before closing them.
- [ ] If the user picks a permanent Astra/Sol or Sol/Low setup, update the saved defaults and orchestration docs together.
- [ ] Verify the Harper private Site on the user's signed-in phone. It still shows the pre-voice-pass text until it is rebuilt.

---

## Warnings and Caveats

- **The Harper private phone Site (Session 35) is now stale.** It serves the pre-voice-pass text. Rebuild it only if the user asks.
- **Audit coverage limits.** The guides/setting auditor keyword-grepped the 122 NPC pages and read only the hits. The main-quests auditor full-read some Act I–II files and pattern-swept the rest. Implied Manshoon knowledge without the keywords could have been missed.
- **Line numbers in the notes are from this session.** Harper line numbers shifted during the voice pass, but the notes only cite non-Harper files, which weren't edited except for the listed small fixes. Re-grep before editing.
- **The six prose agents couldn't run shell commands**, so their self-checks were by eye. Every file was rechecked by the main session with `voicecheck.py`, and all 33 print zero TELLs.
- **Unverified minor NPCs:** agents voiced Uza, Tessalar, Orren, Harl, Nella, Orin, Ilen and others from event text alone.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md, then open `docs/plans/harpers-out-of-scope-notes.md` and go straight to **Decisions Needed Before Fixing** at the bottom. Put those six questions to the user before fixing any R1/R2/R3 finding. Once they're answered, plan the fixes per faction or area and hand them to `prose-drafter` agents, with at most five running at once. Verify each with `voicecheck.py` and the token-diff check before committing. Don't start a faction rewrite, quest conversion or bestiary work unprompted.
