# Factions Guide move: binding brief (Session 51)

Read docs/plans/factions-move-spec.md first (research, comparison with the pilot, per-page section maps, inbound references). The move was decided in Session 47 (docs/plans/setting-compendium-pilot-findings.md:20). The finished pilot campaign/setting/faction-operations/10-cassalanters.md is the model for every page.

## Rulings (made from the plan's own rules; the user can overturn)
- D1. The overview becomes a hub page `00-faction-operations.md` (the History and Deities journals have hubs). It carries the overview's unique rules verbatim (renown tracking, the calibration, the Lords' Alliance discipline, the supplementary and loss rules, the page map rewritten as bold names of the ten child pages). Do not resolve the four conflicts the spec lists between 01-overview and player-factions-overview.md; record them as a Draft Notes bullet on the hub for the user.
- D2. Faction-operations pages have no Overview (they are GM-only and the plan's row lists none). The pilot has none.
- D3. Callout is `> [!gamemaster]**Gamemaster's Summary**`, as in the pilot.
- D4. Sections a guide page does not have (Xanathar's Guild and Manshoon's Zhentarim have no Grand Game Stance, Quest Hooks, First Meeting, Renown & Ranks or Missions) are omitted. Write nothing new beyond the front matter and the Source/Cross-References lines.
- D5. Verify the move by body text, not bullet counts: every non-blank line of the guide page between the lead-in sentence and Cross-References must appear in the new page verbatim, except link markup (D11). The front matter and the Source References are new.
- D7. Keep the H1 identical to the guide page's H1, as the pilot did.
- D8. The Source References bullet that names the guide page reads "the retired Factions Guide page (moved here verbatim)" with the old file name given as plain text in backticks, as the retired-outline provenance is written elsewhere in the campaign.
- D11. Convert relative markdown links `[text](../x/y.md)` to bold names of the page (`**Page Title**`), so no `.md` link remains; link targets are quest journals and pages, so use their titles. Where a link points at a quest journal, name the quest or event in bold as the other pages do.
- Every "Factions guide overview" or "Factions guide" cross-reference becomes the bold hub name **Faction Operations**.
- Headings: keep the guide's H2 and H3 headings. Reorder sections only into the plan's unified order: Grand Game Stance; Quest Hooks; First Meeting; Renown & Ranks; Missions; Response Teams; Outposts; Escalation; Revelation List. The spec's per-page map says where each section sits now; most pages need no reorder.

## Page template (from the pilot)
1. `# Title` (identical to the guide H1) 2. `> Structuring draft.` 3. `> [!gamemaster]**Gamemaster's Summary**` with four bullets: Page type, Campaign role, Used in play, Featured in (see the pilot lines 5 to 10; "Featured in" names the quests that use the page) 4. `**Purpose:**` one sentence 5. the guide's lead-in sentence 6. the sections 7. `**Tone:**` one line 8. `---` 9. `## Source References` 10. `## Cross-References` (the guide's bullets, links converted).
Ember voice; GM text is plain and procedural. Run python3 .claude/skills/ember-voice/scripts/voicecheck.py only if you have a shell; the main session runs it.

## Do not
Do not delete or edit any guide page; the main session deletes them after verifying. Do not edit quest journals, structure docs, or other pages' links; another pass retargets inbound references.
