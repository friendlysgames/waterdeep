# Bregan D'aerthe Conversion Brief

## Context

The Harper (Sessions 35/37) and Doom Raiders (Session 38) faction events were converted from first-commit drafts into finished Ember-voice adventure text. The user wants Bregan D'aerthe done the same way. Step 1 is done: all 30 BD files are restored to the commit that first added each one (following the faction-missions → faction-events rename). This is committed and pushed as `45a8a64` on `claude/gracious-newton-7t31u1`, and those restored drafts are the rewrite input.

Five Sonnet 5.5 `source-researcher` agents reported on the following, and their findings drive this plan:
- the conversion spec;
- the First Meeting and s01–s04;
- M1–M3 with M2b;
- M4–M6;
- the rank events and a campaign-wide reader audit.

**What the restored drafts look like:**
- Every file uses retired formats: `[GM]` zones, `[!profile]`, `[!design]`, True/False flags, `Milestone: None`, `## Read Aloud`, and "Arc X" labels.
- None of M1–M6 sets a named outcome.
- Three outcomes have no reader: Coin Pouches, Kreb Unmasked and Zardoz Introduced.
- Renown is under-calibrated, with gates set for a Renown 0 start.
- Several source beats were dropped (App C BD-1 to BD-4, WDH).
- Krebbyg and Zardoz are written against their voice profiles.
- M6 contradicts the Eye #3 canon.

## User decisions (this session)

1. **Jarlaxle ladder:** gate naming him on a new **Jarlaxle Unmasked** outcome.
   - Nevercott briefs M1, M2 and M4 (WDH/App C).
   - The s03 dinner, after M4, hands the contact over to Zardoz.
   - Until **Jarlaxle Unmasked** is marked for a member, BD speakers say "the captain" or "J.". GM text states the truth.
   - The natural writers are Fireball ev-04's cabin scene and Sea Maidens Faire. Both are logged out of scope.
2. **M6 becomes the guide 08 limpet-charge mission:**
   - Xanathar's divers plant a charge on the *Scarlet Marpenoth* hull, and the party removes it before dawn.
   - It runs after Kolat Towers (L7), like DR M6.
   - After the Faire sails on Tarsakh 20, Jarlaxle stays behind with a team and the sub (PDF 9 p.70).
   - Eye #3 is not the prize. The mission is order-agnostic about Eyes.
3. **M2 Wazoo is the source-faithful version, built on suspicion.**
   - It is a lurid piece on devil worship and orgies among *unnamed* noble families.
   - Jarlaxle wrote it to see who flinches; he suspects, he doesn't know.
   - It carries no temple or ritual-space detail.
   - The Cassalanters' reaction is the tell.
   - **Superseded later in Session 39 (user):** "Jarlaxle knows about the Cassalanters, he has a spy there. He won't tell the members unless they figure it out themselves." The spy is Vessa. The exposé becomes a deliberate pressure play, and a member who works it out sets **Cassalanter Pact Shared with BD**.
4. **M2b is cut.** Delete `m02b-the-betrayal-pitch/`. The Betrayal Pitch stays with Sea Maidens Faire (arc-h).
   - Strip every M2b reference from s02, s04 and M2's "boat" hook.
   - CLAUDE.md's count changes from "43 missions, 44 folders including BD-M2b optional" to "42 missions, 42 folders".

5. **Soluun, the Dockside Killer (DR out-of-scope note):** if he survives DR M1 (**Soluun Captured**, then bailed out by "Rongquan Mystere", or **Soluun Escaped**), Jarlaxle expels him for real. The cover-story disownment becomes true.
   - His fate lands in a **new standalone event**, `s05-the-killers-fate/` (ev-01 + design-notes).
   - M4 and M6 read the outcome it sets.
6. **BD witness:** if a BD member was present at Soluun's capture or death as a DR M1 companion, BD knows within a tenday.
   - Nevercott raises it once with that member, coolly ("You were there.").
   - The member loses 1 Renown unless they explain themselves well. That is a check plus a stated good explanation.
   - Nothing worse happens.

## Standing defaults (precedent; no question needed)

- **Scope:** edit only `campaign/quests/faction-events/bregan-daerthe/`, plus 9 new design-notes files, the new s05 folder, the m02b deletion and the CLAUDE.md counts (missions and standalone events, 14 → 15). Log every outside contradiction in a new `## Bregan D'aerthe event rewrite (Session 39)` section of `docs/plans/harpers-out-of-scope-notes.md`.
- **Source wins** over drafts (WDH, App B/C, Notable Figures):
  - Ott is a dwarf **Cult Fanatic** with the iron bands of Bilarro, and he vanishes after Night 3.
  - The windmill is in the Southern Ward, on Coachlamp Lane.
  - Krebbyg follows his profile: rash and young, saying "darling" and "Ask Fel", with Fel'rekt beside him.
  - Zardoz follows his profile: loud and exclamatory, and never mentions drow or the Underdark.
  - Nar'l's tenure is "a year" (WDH). The 3-year and 11-year versions are logged.
  - Gaxly is an Illuskan human **Commoner** of forty.
- **Membership is individual (R3).**
  - The First Meeting runs per candidate, and a PC already in another faction gets no offer.
  - Any PC may be recruited (remix rule), and drow PCs draw the closest watch.
  - **BD Contact Severed** is marked per reporting PC. Surveillance ends, but Nevercott still approaches non-reporting candidates later.
  - Briefs and debriefs are for members only. The Jarlaxle exception applies to cross-quest debriefs, not to BD's own events.
- **Renown:** joining gives Renown 1 (Initiate). Base awards are 2/2/3/3/4/4.

  | Mission | Gate |
  |---|---|
  | M1 | Joining, at 2nd level |
  | M2 | Renown 3, 3rd level |
  | M3 | Renown 5, 4th level |
  | M4 | Renown 8, 5th level |
  | M5 | Renown 10, 6th level |
  | M6 | Renown 13, 7th level |

  Renown 25 and 50 come from guide 08's Earning Renown list and Mad Mage. The r25 and r50 design notes say so.
- **Manshoon:** BD is clean, so no gate is needed. Any Splinter mention follows the DR convention.
- **Lolth:** never revered. The spider-and-blade coin (r50) and the chalk spider (M4) read as the rejected goddess under a knife.
- **2024 stat names only:**
  - Thug becomes Tough, Veteran becomes Warrior Veteran, and Bugbear becomes Bugbear Warrior.
  - Drow Gunslinger, Swashbuckler (Jarlaxle), Beholder Zombie, Intellect Devourer and Grell must be verified against the 5etools-mirror-3 XMM data, or replaced with the nearest 2024 block.

## Spec

Copy the Doom Raiders spec in `docs/plans/doom-raiders-conversion-brief.md` ("Conversion spec"), plus the conventions the spec agent found in the finished DR files:
- Gate phrasing: "becomes available when an individual Bregan D'aerthe member reaches Renown N and Xth level".
- Every mission event carries a `[!gamemaster]**Mission Renown**` block.
- Rank events have no overview, and their outcomes read "mark with the recipient's name".
- GM context sits in "What Is Actually True" or "Who Knows What" blocks before the first scene.
- Speech inside readalouds is quoted. Pick the quoted form, since DR is inconsistent here.
- Summaries are a first-person journal.
- Every event ends "awards no Milestone Points".

## Per-folder content fixes

**00-first-meeting (+ design-notes)**
- Watchers come from WDH: Fel'rekt and Krebbyg at night, Soluun by day.
- Passive Perception 18, plus a DC 15 Insight check showing they track drow PCs.
- Ryvarra stays as the Portal observer. Her own tell is DC 14 Insight, and her tenure follows her Notable Figures page.
- Three branches: watch, confront (the eye-patch calling card) and report to the Watch. Report to the Watch sets per-PC **BD Contact Severed**, and the Watch sergeant is named.
- Nevercott's scene follows App B:
  - He keeps the fiction until a drow PC, or the candidate, steps aside.
  - He names Bregan D'aerthe and hands over the black card with a silver ship.
  - He says declining costs nothing, and "I'll be in touch shortly regardless".
- An Initiate Benefits block covers the *Heartbreaker*/*Hellraiser* safe house and Fel'rekt's gear at cost.
- Read **BD Acknowledged** and **Ryvarra Identified**.
- Cut the invented bead and cloud escape.

**M1 The Handkerchief and the Girl** (App C BD-1)
- Nevercott briefs.
- The setting is the Twin Parades on Ches 21: Maester Roderick Bartlethorpe, a **Noble**, by the Great Drunkard on Bazaar Street.
- Getting the handkerchief: DC 12 Sleight of Hand, or DC 12 Deception, Intimidation or Persuasion.
- The girl is Vessin, about eleven: the crate at Net and Dock with a carved sun, her book, and "He said you'd come today".
- The handkerchief carries a scent-coded message: DC 18 Perception or *detect magic*.
- Carry-forward detail: the parade nimblewright's hat.
- Cut Lady Ashford and the knots.

**M2 The Wazoo Affair** (WDH plus decision 3)
- Nevercott briefs at the Yawning Portal.
- Gaxly's office is at Immar and Stallion; break in at lunch or after hours.
- Checks: two DC 15 Stealth and DC 10 thieves' tools, or *knock*.
- Desk note on the Black Viper source.
- He asks "Did you find it informative?"
- Nevercott pays 80 gp.
- Aveen Street and windmill rumours appear only as gossip.
- Fix Athletics to Strength.
- Cut the M2b boat hook.

**M3 Three Nights** (WDH/App C BD-3)
- No brief. Ott appears in the cellar, and a flying-snake note follows.
- Night 1: 6 Bugbear Warriors.
- Night 2: four Dungsweepers' Guild Commoners carrying Intellect Devourers. Spotting them takes DC 15 Insight or DC 15 Perception (pupils).
- Night 3: a Beholder Zombie through sewer grate T7.
- Lif is an ally outside the cellar.
- Ott vanishes with the bands.
- Every fight has a surrender or retreat condition and a non-combat route.
- Outcome **Ott Kept** feeds the Faction Outposts Interrogation House: he is recaptured later "in the Guild war". The arc-e gnome entry is logged.

**M4 The Compromised Eye** (App C BD-4 plus three-outcome design)
- Nevercott sends a flying-snake brief with a tiered order: keep him in place, extract if you must, silence him if neither works.
- The grell bodyguard is restored, with a twelve-minute clock.
- Nar'l's trade: the X19 Eye location and the X18 Panopticus bypass.
- Insight on his story: DC 18, DC 14 or DC 10.
- Each route (discredit, extract, eliminate) gets several beats.
- Outcomes keep their names: **Nar'l Active**, **Nar'l Extracted** and **Nar'l Eliminated**. Add **Nar'l Cleared**, which s03 reads.
- Reward: the gold statuette.
- Read **Soluun Expelled** (s05) and DR M1's **Soluun Killed**. Nar'l's exposure traces back to covering for his brother. Krebbyg no longer calls the disownment a cover story once it's real.
- Add a variant for when Xanathar's Lair has already run.

**M5 The Theater's Back Room** (guide 08:70)
- Brimel's windmill floor plan. The windmill is in the Southern Ward, Coachlamp Lane, with Seffia and Arn as tenants.
- If Faction Outposts 6B already raided the windmill, the mission runs a debrief-only page (the DR M5 ev-02 precedent).
- Florette is spotted, then dealt with through several approaches, each with a failure branch.
- New outcomes: **Florette Reported** (read by arc-g) and **Seven Masks Back Room** (the arc-e dressing-room safe house).
- Zardoz is present but silent, a deliberate choice that is noted.
- Settle Brimel's motive as "paid".

**M6 The Dive** (decision 2)
- The limpet charge on the *Scarlet Marpenoth*.
- Sub stats from WDH: AC 20, 300 HP, threshold 15.
- The charge mechanics and clock are invented in the mechanics reference.
- The lookout, the dive team (Warrior Veteran plus Guild divers) and the 2024 underwater rules.
- Krebbyg and Fel'rekt appear.
- How the Guild found the sub: an expelled Soluun sold the mooring (**Soluun Expelled**). Otherwise, read the M4 Nar'l outcomes (grief leak if Nar'l Active), or fall back to the Guild's own harbor search.
- New outcome **Marpenoth Saved**, read by Vault of Dragons and r50.
- Cut Krenick Durr's wreck plot, and give the dive leader a name.

**s01 Coin Pouches**
- Follow guide 08: 50 gp after M1, then 100 gp plus a note after M3.
- Krebbyg's in-voice deflection.
- The anchor gate is fixed.
- WDH's third support (buying off threats) is added as a beat.
- Cut **Coin Pouches**, which has no reader.

**s02 Kreb Drops the Cover**
- After M2, Krebbyg drops "Kreb Sorrush" and shows himself as a drow lieutenant.
- Members only.
- No payment.
- **Kreb Unmasked** is read by M3–M6.
- Remove the Pitch references.

**s03 Dinner with Zardoz**
- Aboard the *Eyecatcher*, J10, after M4.
- It is the handover from Nevercott to Zardoz.
- Zardoz is in his loud voice, with the precise questions buried in bluster.
- It is not his first sighting.
- **Zardoz Introduced** is read by M5, M6, r10 and r25.
- Branch on all four Nar'l outcomes.
- Cut the token.

**s04 Contact Severed**
- Per PC, and it reads the outcome rather than re-setting it.
- Recruitment for other factions is pointed to their First Meeting events.
- Remove the Pitch line.

**s05 The Killer's Fate (new folder: ev-01 + design-notes)**
- **Fires for BD members:**
  - a little over a tenday after **Soluun Captured** (the surety release);
  - when he resurfaces before Tarsakh 20 after **Soluun Escaped**.
- **If DR M1 never ran** (no Doom Raider in the party), treat it as Escaped: Jarlaxle learns of the killings through Krebbyg and Fel'rekt. The event fires the tenday after the member's M1.
- **Scene:** aboard the *Scarlet Marpenoth*, BD members witness the ruling.
  - Soluun is stripped of his silver disc and put ashore. He says nothing of Lolth except contempt, and his zeal is all for "the captain".
  - Jarlaxle is unseen, or appears behind **Jarlaxle Unmasked**.
  - Nevercott or Krebbyg delivers the words.
- **Member choices:**
  - plead for him;
  - press him for what he knows;
  - mark him as a future threat.
- **The witness beat** (decision 6) runs here for any member who was at the alley.
- **Killed variant:** a short beat where BD learns who killed him and Jarlaxle's interest turns personal (per DR M1). The witness rule applies here too. There is no expulsion.
- **New outcomes:**
  - **Soluun Expelled**, read by M4, M6, r50 and Sea Maidens Faire (unconverted);
  - **Soluun Witness Explained** / **Soluun Witness Penalized**, per member.
- **First Meeting:** Soluun stays the WDH day watcher, so the killings are his moonlighting.

**Knock-on reads**
- **M4:** Nar'l's exposure traces to covering for his brother, branched on Expelled or Killed.
- **M6:** an expelled Soluun is who sold the *Marpenoth*'s mooring to Xanathar's divers. If he was Killed, the leak is Nar'l's grief (Nar'l Active), or else the Guild's own harbor search.
- **r50:** the empty seat branches on the same outcome.

**r03, r10, r25, r50 (+ design-notes each)**
- Every rank benefit becomes a written per-PC procedure: contact, place, limits, loss rule and per-quest tracking.
- r03 separates Initiate from Soldier benefits and degrades the Nar'l channel by outcome.
- r10 keys the contact on **Zardoz Introduced**, gives one Spy per Officer, and uses a fixed item table. Its records branch on Fireball's **Nimblewright Ledger Stolen**.
- r25 keys the Jarlaxle-open branch on **Jarlaxle Unmasked** and delivers the Vault proposal (the guide's "Dread Lord" is logged).
- r50 is placed in Mad Mage, branches the empty seats on Soluun and the lieutenants, makes declining cost something real, and corrects the renown math.
- Fix the "Mission 4" mislabels and the ivory card.

## Execution

- **Phase A, brief.** One `source-researcher` (Sonnet 5.5) compiles `docs/plans/bregan-daerthe-conversion-brief.md` from the five reports and this plan, with line references verified against the restored drafts and the source excerpts each drafter needs. The main session reviews and commits it.
- **Phase B, mechanics.** In the main session, curl the 5etools-mirror-3 XMM bestiary and spell data into the scratchpad and extract the records.
  - Then `encounter-builder` writes `docs/plans/bregan-daerthe-mechanics-reference.md`, with CR 2.0 numbers at 3, 4 and 5 combatants.
  - It covers the M3 three nights, the M4 grell, the M6 dive team and charge, and the r25 and r50 allies.
  - Commit.
- **Phase C, drafting.** `prose-drafter` agents (Sonnet 5.5), at most 5 at once, one per folder. Each gets its brief section, the mechanics reference and the skill list: `ember-voice`, `character-voices` (`bregan-daerthe.md` and `xanathars-guild.md`), `adventure-reloaded`, `dnd-adventure-text`, `ember-adventure-style` and `foundry-journal`.
  - Batch 1: 00-first-meeting, M1, M2, M3, s01.
  - Batch 2: M4, M5, M6, s02, s03.
  - Batch 3: s04, s05, r03, r10, r25.
  - Batch 4: r50.
  - Delete `m02b` in batch 1's commit.
  - Commit per folder after main-session review.
- **Phase D, out-of-scope log.** Topics:
  - Jarlaxle Unmasked writers (Fireball ev-04, arc-h).
  - Guide 08: the limpet M6 now matches; the Renown-5 extraction; "Dread Lord".
  - Org page, `jarlaxle.md:48,51`, the Zord origin, and Nar'l tenure.
  - Trollskull ev-03, ev-04 and ev-07.
  - arc-e: the Ott gnome entry and the windmill as a "Manshoon outpost".
  - arc-h: "Operative" rank, the Pitch now sole owner, Eye 3.
  - arc-j:55.
  - Force Grey M4's captive Soluun.
  - `SOURCE_GUIDE.md`'s North Ward and Sargauth claims.
  - Invented names: Vessin's age, Ilphrin, Pelsha, Vorn, Sarev Oust, Brimel, Florette.
  - A Nevercott voice profile, which belongs in the skill and is written by the main session if the user asks.

## Verification (each folder, before commit)

- `python3 .claude/skills/ember-voice/scripts/voicecheck.py <file>` reports zero TELLs. Speech averages 12 or more words per sentence and narration 18 or more.
- Folder greps:
  - "Jarlaxle" appears in speech or readaloud only behind **Jarlaxle Unmasked**.
  - No hits for `Lolth` (outside contempt), `[GM]`, `[!profile]`, `[!design]`, `Milestone:`, `True / False`, "Award +", `Arc [A-J]`, `Thug`, `Veteran` (bare) or `M2b` / "Betrayal Pitch".
- Every Event Outcome has a reader in the folder, a named arc-doc reader marked "(unconverted)", or an out-of-scope entry.
- Main-session review checks:
  - mission depth (no single-check resolution);
  - source fidelity against the brief;
  - 2024 creature names;
  - the order-agnostic Eye text.
- A final `consistency-checker` pass over the folder, with fixes applied.
- Push to `claude/gracious-newton-7t31u1`, then open a PR and merge it (handoff rule).

## Research reports

The five Session 39 `source-researcher` reports are in `docs/plans/bregan-daerthe-research/`. They read the restored drafts, so their line references match the rewrite input. They list options the user has since decided. Where a report and the decisions above disagree, the decisions win: M2b is cut, M6 is the limpet charge, the Wazoo piece is a suspicion-only fishing expedition, Jarlaxle is gated on **Jarlaxle Unmasked**, and Soluun's fate lands in s05.

| File | Covers |
|---|---|
| `01-spec-and-faction-rules.md` | Conventions confirmed in the finished DR files, BD-specific rules, gates, voice-profile coverage |
| `02-first-meeting-and-standalones.md` | 00-first-meeting, s01–s04: fix lists, readers and writers, source facts |
| `03-m01-m03.md` | M1–M3 (and the cut M2b): fix lists, combats, source facts |
| `04-m04-m06.md` | M4–M6: fix lists, combats, source facts, Eye #3 and windmill findings |
| `05-ranks-and-reader-audit.md` | r03–r50 fix lists, the campaign-wide outcome table, the contradiction list for the out-of-scope log |
