# Session 48 Handoff
**Date:** 2026-11-13
**Status:** Ready to continue. Pass 2 (Deities) is complete and merged to `master`: 73 power pages and the hub, all re-passed for the wider subclass list, and all checked against the Sundering and source-precedence rulings. The Factions Guide move and Pass 3 have not started. A list of small design decisions needs the user (see Outstanding Work, "New this session").

---

## What Was Done

The session first rewrote the three read-and-calculate agents for Claude Haiku 5.5 (goal-first prompts, `effort: high`, full quotes with file and line in their reports), then ran Pass 2 end to end. Haiku researchers wrote verified full-quote notes for 72 powers from the offline wiki, the 5etools deity data and the campaign files; Sonnet drafters wrote one page per power (51 Faerunian gods, Siamorphe, 8 heads of other pantheons, 13 patrons, plus Asmodeus from the pilot) and the hub `00-the-deities.md`, each merged to `master` as it finished and edited afterwards. The user then widened the cleric, paladin and warlock options to every subclass not yet reprinted in a 2024-format book (no Plane Shift, no World of Warcraft), so all 73 pages and the hub were re-passed in 15 batches against a generated reference of 34 options. Finally the session researched how the Second Sundering resolved the 4e changes (offline wiki and book text, then the open web), the user ruled on the canon, and three consistency checkers and three fix agents applied the rulings across about 40 pages. Everything is merged (PRs 233 to 301).

---

## Changes Made

Git range: `cd7218a..HEAD` (the "Session 47 handoff" commit to the PR 301 merge); 264 commits, 107 files changed, +24,253 / -247 as of the PR 301 merge, before this handoff.

### Files Modified
| Area | What changed |
|------|-------------|
| `.claude/agents/source-researcher.md`, `consistency-checker.md`, `encounter-builder.md` | Rewritten for Haiku 5.5 (`model: claude-haiku-5-5`, `effort: high`); the researcher gained `Write` for one notes file and returns full quotes |
| `CLAUDE.md` | Agent paragraph (three Haiku agents, no `model` override); new standing rules "Sundering canon and 5e source precedence" and "Gods in prose" |
| `campaign/setting/deities/asmodeus.md` | Derived fits added (Order Domain, Oathbreaker, Fiend Patron); paladin and warlock lines split |
| `campaign/setting/history/04-the-founding-of-chains.md`, `07-a-city-watching-itself.md` | Zhentil Keep ruling (rebuilding "hasn't happened yet"); Laeral's magic has recovered since 1487, "not fully" |
| `campaign/setting/waterdeep-lore.md` | "South Ward" corrected to "Southern Ward" |
| `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md` | "Corellon Larethon" typo fixed |
| `campaign/locations/cassalanter-villa/11-wine-cellar.md`, `campaign/structure/arc-g-cassalanter-villa.md`, Doom Raiders `m01-the-dockside-killer/ev-01` | "goddess of X" became "god of X" |
| `docs/plans/setting-compendium-rebuild-plan.md` | Deities row and Pass 2 entry updated |

### Files Created
| File | Purpose |
|------|---------|
| `campaign/setting/deities/*.md` (73 powers) | 51 Faerunian gods (Asmodeus from the pilot), Siamorphe, the heads of other pantheons (Corellon Larethian, Moradin, Garl Glittergold, Yondalla, Gruumsh, Maglubiyet, Tiamat, Bahamut) and 13 patrons (Zariel, Mephistopheles, Mammon, Orcus, Demogorgon, Graz'zt, Titania, Queen of Air and Darkness, Baba Yaga, Iggwilv, Ilsensine, Ghaunadaur, Tharizdun) |
| `campaign/setting/deities/00-the-deities.md` | Hub: four choose-a-deity tables (domain, alignment, 2024 character fit, by subclass), Waterdeep temples table, other-peoples table, patrons by warlock subclass |
| `docs/plans/setting-compendium-pass2-brief.md` | Binding Pass 2 brief, including the "Available 2024 subclasses" ruling |
| `docs/plans/setting-compendium-pass2-drafter-instructions.md` | Drafter lessons and the Major Temples table |
| `docs/plans/setting-compendium-pass2-repass-instructions.md` | Re-pass rules for the wider subclass list |
| `docs/plans/setting-compendium-pass2-subclass-reference.md` | Generated reference of the 34 available options from the 5etools class data |
| `docs/plans/setting-compendium-research-notes/pass2/batch-*.md` (15 files) | Full-quote research notes for every power |
| `docs/plans/setting-compendium-research-notes/sundering-resolutions.md` | Offline research on the Sundering, ending in a table of 40 4e changes and the user's rulings (section 14) |
| `docs/plans/setting-compendium-research-notes/sundering-online.md` | Open-web research on the Sundering |

### Files Deleted
None.

---

## Key Decisions

### Pass 2 scope: a character-building reference, not only campaign gods
**Decision:** The Deities journal covers every Faerunian god, the heads of the other peoples' pantheons and thirteen warlock patrons (three archdevils plus Asmodeus, three demon princes, three archfey, Iggwilv, three Far Realm entities), plus a hub.
> "Everything plus hub, since it's not just for campaign relevant Deities. It's meant to be something that helps Clerics, paladins, warlocks and religious characters to choose their deity. This means that some other stuff may be needed, like a couple major archfey, a couple archdevils, a couple demon princes, some eldritch beings from the far realms. Use the wiki too." (User)
> "giv the batch M agent Iggwilv too" (User)

### The agents are rewritten to Anthropic's Haiku 5.5 guidance
**Decision:** After the first rewrite used step scripts and prohibitions, the user sent the agents back to the docs; the second rewrite is goal-first with `effort: high`. The researcher got `Write` for one notes file.
> "Make sure you read your docs on haiku 5.5 so that you know exactly how to rewrite the agents." (User)
> "Give the researcher Write for one notes file (Recommended)" (User, option chosen)

### PR and merge every draft and every edit type
**Decision:** Each page is merged as its agent reports, then each edit pass is merged separately.
> "remember to PR and merge with each draft written, and each edit type after that." (User)

### Available subclasses (the 14 / 10 / 10 list)
**Decision:** Cleric domains, paladin oaths and warlock patrons not reprinted in a 2024-format book are available, minus Plane Shift and World of Warcraft. Arcana Unleashed counts as official (it is Wizards of the Coast's new Unearthed Arcana). The list is in the Pass 2 brief; the generated reference is `setting-compendium-pass2-subclass-reference.md`.
> "Anything that hasn't been reprinted yet goes into the available subclasses, except for Plane Shift subclasses. No Warcraft subclasses." (User)
> "Reminder, Arcana Unleashed isn't really 3rd party, it's the new version of UA" (User)
> "Wait for the hub to finish, PR and merge, then go ahead with the repasser, in batches." (User)

### Sundering canon and source precedence
**Decision:** The Second Sundering ended in 1487 DR; every Spellplague-era merger is undone; Heroes of Faerun (2025) wins over the Sword Coast Adventurer's Guide where they disagree; Laeral's magic has recovered "not fully, but yes"; Zhentil Keep's rebuilding has not happened yet in 1492 DR. The campaign year stays 1492 DR.
> "1487 is the canon date iirc, all gods were unmerged, by 1491 means that it has already happened by that year, Heroes of Faerun takes precedent over scag, since it's newer." (User)
> "Not fully, but yes" (User, Laeral's magic)
> "Hasn't happened *yet*" (User, Zhentil Keep)
> "My bad, I was misremembering" (User, retracting "the year for this campaign is 1491")
> "Keep her lawful then, I misremembered" (User, Tiamat stays Lawful Evil)

### Research the Sundering online as well
> "Shouldn't you also look online?" (User)

### Gods in prose
**Decision:** "God of X" in title form; a standalone "goddess" stays; quoted printed titles keep their quote. Cyric's release from the 4e imprisonment needs no explanation.
> "God of, goddess whenever it's just that. For example, "The goddess did that".  If it's goddess of something, do god of." (User)
> "Does it really matter how the god of manipulation and trickery managed to free himself?" (User)

---

## Rules and Instructions

All earlier rules stay in force. Added or reinforced this session:

- **Sundering canon and 5e source precedence** (`CLAUDE.md`): 1487 end; mergers undone; FRHoF over SCAG; where FRHoF is silent SCAG stands; the wiki and novels rank below both.
- **Gods in prose** (`CLAUDE.md`): "god of X" for titles, standalone "goddess" stays, quoted titles untouched.
- **Available subclasses** (Pass 2 brief): 14 domains, 10 oaths, 10 patrons; an older option is used only where no 2024 book has an equivalent; use the 2024 version where one exists.
- **PR and merge each document, then each edit pass.** Never commit another agent's half-edited files; `git add -u` sweeps them in (it did once; the commit message was amended before pushing).
- **Never more than 5 agents at once;** resume rate-limited agents with `SendMessage`; an agent without an Edit tool cannot polish its notes (the Sundering researcher looped on failing Edit calls until messaged).
- **Verify the brief's premises against the JSON.** Four patron drafters found that the brief assumed Mad Mage ties the JSON does not contain (Mephistopheles, Orcus, Demogorgon, Graz'zt, Ilsensine). Quote the line or state no tie.
- **Cassalanter secrecy and Bregan D'aerthe's rejection of Lolth held on every deity page.** Pact facts appear only under Secret, GM Notes, Never reveal or Draft Notes.
- **Voicecheck every page** (`python3 .claude/skills/ember-voice/scripts/voicecheck.py`); it flags the word "tapestry" even for a literal item, so write "wall hanging".
- **Web research goes to a general-purpose agent** (the project agents have no web tools); its notes rank below the offline sources, and its fetch tool summarizes pages, so spot-check quotes before they reach a page.

---

## Problems Solved

- **Haiku agents violated Haiku 5.5 guidance** → rewritten goal-first (`effort: high`), the rule recorded in `CLAUDE.md`.
- **Researcher notes not saved or ellipsized** → notes file on disk, no ellipses, `check_quotes.py` verification (scratchpad tool, lost with the container).
- **Rate limits stopped agents repeatedly** (four times) → resumed the same agents with `SendMessage`.
- **Wrong premises in the brief** (Mad Mage ties for four demon patrons) → pages quote what the JSON has and invent no link.
- **`fix_planned.py` missed names with apostrophes or a leading "the"** → four cross-references fixed by hand.
- **Stale facts found by the drafters:** `oghma.md` wrongly said SCAG lacked the Deneir and Milil titles; `mystra.md` said Talos helped kill her; the Moradin research note placed the trapped-demon text in area 19 (it is 29d); `waterdeep-lore.md` said "South Ward"; Fala's page said "Corellon Larethon".
- **Sundering researcher stuck retrying a missing Edit tool** → messaged to stop; 166 of 173 quotes in its notes verified by script, the seven misses being removed wiki markup.

---

## Outstanding Work

### New this session
- [ ] **Decisions for the user:** (1) whether the Xanathar's Lair "something vast and dreaming" seed (`arc-f-xanathars-lair.md:382`) is Ilsensine, an elder brain or the aboleth; (2) Yorn the Terror (half-orc in WDH, "Human enforcer" on his page) and "Yagra Strongfist" in WDH against "Stonefist"; (3) keep the Blessed of Corellon sex-change gift for elf PC clerics; (4) whether the loose subclass fits stand: Oathbreaker on Lolth, Shar, Talona, Loviatar, Bhaal, Cyric, Myrkul, Beshaba, Asmodeus, Orcus and Ghaunadaur (Talona and Loviatar can revert to "No oath fits"), Umberlee's Fathomless, Helm's Crown, Amaunator's Vestige, Milil's Knowledge, Gwaeron's Vengeance, Lliira's Redemption, Tiamat's Order, Shaundakul's Tempest, Graz'zt's Conquest; (5) Lolth's derived Fiend fit against "No warlock connection in the sources"; (6) Iggwilv's status in 1492 DR (the wiki freezes her in time with no year); (7) add a note on the hub and the nine pages that Heroes of Faerun dropped (Akadi, Grumbar, Gwaeron Windstrom, Hoar, Istishia, Jergal, Kossuth, Savras, Valkur); (8) the Selune temple name (Tower of the Moon on `selune.md`, House of the Moon on `shar.md:113`); (9) Zelifarn's location (`organizations/07-bregan-daerthe.md:39` the Scarlet Marpenoth vs his Notable Figure and the Force Grey mission, Deepwater Harbor).
- [ ] **Tymanther leftovers:** `bahamut.md` still has Tymanther dragonborn followers and the Platinum Cadre's "dragonborn knights of Tymanther" (Tymanther is "no more" per FRHoF); `tiamat.md:42` "Bahamut later became the subservient god of Torm"; `torm.md` relations bullets (Amaunator, Lathander, the Girded Healers' Spellplague line) should read as separate-again powers.
- [ ] **Cleanup passes on the Deities journal:** about 15 pages still carry stale Draft Notes saying a page is "planned" or telling someone to retarget a tag; many Draft Notes "Derived" and "Hub" bullets are partly out of date after the re-pass (check `moradin.md`, `eilistraee.md` were fixed; audit the rest); the hub's Draft Notes still say voicecheck was not run (it was); the three Sundering consistency checkers read only some pages in full (checks 3 and 4 incomplete), so run a full `consistency-checker` crossref pass over `campaign/setting/deities/`.
- [ ] **Unverified claims on the pages:** `torm.md:39` (FRHoF alliance of the Torm and Red Knight priesthoods, not found in the FRHoF text); older-edition options (Tempest, Nature, Death, Forge, Order, Twilight, Peace, Oathbreaker, Crown, Conquest, Redemption) are described only by name and theme because the reference has no mechanics; Bane, Bhaal and the Withers line.
- [ ] **Waterdeep temples conflicts left for Pass 3:** `waterdeep-lore.md:36` lists only Tymora and Selune as Sea Ward major temples (Dragon Heist adds the House of Heroes, House of Wonder, Temple of Beauty, Tower of the Moon and Shrines of Nature); `castle-ward.md:165` calls Helm's ward unsettled; the Temple of Milil has no ward.
- [ ] **Staff table alignments:** `trollskull-manor/03-staff-and-hiring.md:84,88` list Mattrim as "CG human" and Variel as "N wood elf"; their Notable Figures pages say lawful good and neutral good.
- [ ] **Jarlaxle's cabin oath:** `adventure-wdh.json:25498` (a magic mouth in his Eyecatcher cabin, J29, shouts "By Lolth's teeth"); the Eyecatcher cabin entry needs a different oath when written.
- [ ] **Offer the viewer rebuild** (`update-campaign-viewer`) now that the Deities journal exists, and check the Pages deploy.
- [ ] **Rules-lookup agent still points at the dead 5etools mirror** (`rules-lookup.md`); the working mirror is `5etools-mirror-3/5etools-src`.
- [ ] **Possible Pass 2 follow-ups the user may want:** swap any of the thirteen patrons (three of each kind was the main session's choice); a Siamorphe wiki-only page review; the nine SCAG-only pages (see decision 7).

### Carried forward from Session 47: decisions needed from the user
- [ ] **Manshoon's Phase 3 "Simulacrum Insurance"** (`villains/manshoon.md` lines 19, 42, 44; `organizations/09-manshoons-zhentarim.md:19`; Manshoon NF lines 23, 25) still says a simulacrum fights while the real Manshoon escapes. It conflicts with "the man in the towers is a clone of a clone". Keep the simulacrum as the clone's insurance, or redesign the phase?
- [ ] **`arc-e-faction-outposts.md:33`** still has Neverember giving Eyes to "a drow arms dealer" and criminal networks, which conflicts with Eye #1 coming from the Protector's Enclave. Also "eleven years ago" for his removal (should be about three).
- [ ] **Cassalanter villain page** (`villains/cassalanters.md` line 17 "Phase 3 The Sacrificers" reads as if the family sacrifices its children; line 21 "Founders' Day is three sessions away"; line 31 lacks the forfeit date). Victoro NF line 17 lacks the 500,000 gp already held.
- [ ] **Confirm Seffia's mission as an Eye** (Eye #2 from the Brandath Crypt) over the published adventure's "retrieve the Stone"; Arn's spined devil now carries the Eye.
- [ ] **Confirm or swap the invented details:** "within days" for Zelifarn's arrival (`arc-h:19`; Force Grey mission 2 may expect an earlier date); the Q03 strongbox and the reassigned guard in the hideout beat; the Luskan aside's ratings; the `(and to be hungry)` line in Volo's Cassalanter aside; "a patience I have rarely met in his trade" (Davil aside).
- [ ] **Volo confirmations:** the Draft Notes on History 01, 03, 04, 05 ask whether Volo was at Ahghairon's Day, in Luskan, drinking with Davil, and dining twice at the villa; his Notable Figure page (`independents-allies/01`) mentions none of it.
- [ ] **Unruled conflicts (left alone, defaults noted in the checker reports):** Vajra's tenure ("three years" vs wiki 1479 DR); Meloon's devourer timing (three tendays vs three months vs 1491) and "an active member of Force Grey"; Savra's departure (three years vs 1491); alignment differences (Vajra, Savra, Skeemo, Jalester, Kalain); Kalain's alignment/stat block; Jalester's species/background; the Xanathar predecessor count (thirteen vs the wiki's "at least fifteenth"); "third son" for Jarlaxle; Kimmuriel omitted; Cassalanters "about half the gold" vs WDH "most of the coin"; Osvaldo's alignment (neutral evil, formerly lawful good).
- [ ] **Interrogation House ward:** `arc-e:117,:201` say "Trade Ward"; `arc-i:15` and the faction guide say North Ward. `arc-i:259-260` still say "the original Manshoon" (meaning "not the simulacrum").
- [ ] **Ott Steeltoes:** `guides/factions/10-manshoons-zhentarim.md:25,27` (captured, "knows nothing of the Eye") vs `arc-f:9` (Ott receives the Eye and places it in Sylgar's bowl).
- [ ] **Terms:** "Brandath Crypts" (the approach) vs "Mausoleum" (the building): used inconsistently in `waterdeep-lore:20`, `running-the-villains:9,23`, History 06/08, `arc-g:15`, `arc-j:11,85`. Kolat Towers is in the Trades Ward (campaign value); `waterdeep-lore.md:46` still says "Cassalanter sacrifice" for Founders' Day (should be "feast").
- [ ] **Eye #3 route in `arc-h:9,15`:** only the "night before Ches 1" timing was added, not the locket/raid/lift sequence.
- [ ] **Sea Maidens Faire rooms 01 to 04** (`locations/sea-maidens-faire/`) were not checked against "submarine moored all year".
- [ ] **Legacy Event Outcomes format:** `fireball/ev-04:125,129-138` "#### Jarlaxle Informed: True / False" headings; "attunement" wording in `gralhund-villa/ev-02:54` and across trollskull-alley/finding-floon/fireball; `villains/jarlaxle.md:3` still says "flag" for Jarlaxle Informed, BD Contact Severed and Ryvarra Identified. `trollskull-alley/ev-07:72` cites the retired "Ch. 3"; `flowchart.md:69` says "before arc ends"; "Bregan D'Aerthe" (capital A) in Finding Floon and Trollskull Alley.
- [ ] **Small page gaps:** `gm-guide/about-this-campaign.md:70,78` lack "twelve now, weekly"; Lord Cassalanter's letter to Seffia is not in the Windmill finds or Revelation List (ops Outposts); the ops Outposts text does not say the outposts gather gold and ritual components; `arc-g:83` Willifort "eight years" is unsourced.
- [ ] **Missing Notable Figure pages** for people the History pages name: Elminster, Khelben Arunsun, Halaster Blackcloak, Piergeiron, Raurlor, Alethea Brandath, Corylus Thann, Thardouk Starbuckler, Dorgar Adarbrent, Zushaxx, Kirukesai, Fzoul Chembryl, Duhlark and Alcedor Kolat, Yvonnel/Doquaio/Gromph Baenre, Beniago, Kimmuriel Oblodra, Vorondar Levelstone, Faerrel Dunblade, Sevel Dastar, Vaelle Lurval, Nim, Rongquan Mystere. (Ahghairon: none planned.)
- [ ] **Wiki items still open:** ward Lifestyle, Languages and dominant faith (the wiki is blank); Warrior's Way and Street of Silver ward; Midsummer, Twin Parades and Fey Day (absent from the wiki dump); the Code Legal's author and date; Areas of Concern for Asmodeus; warlock/oath rules; whether the Doctrine and Rites tenet on the Cassalanters page can now be filled from the Asmodeus page.

### Passes not started (wait for the user to name one)
- [ ] **Execute the Factions Guide move.** The user decided to move the pages to `setting/faction-operations/`. The Cassalanter pilot is duplicated at `guides/factions/11-cassalanters.md` and `setting/faction-operations/10-cassalanters.md` (kept identical in the shared sections). Moving means retargeting `guides/factions/01-overview.md:47`, `gm-guide/grand-game-in-play.md:103`, `gm-guide/structural-rules.md:26,90,122`, `setting/villains/cassalanters.md:57`, the Asmodeus, Xanathar and Seffia pages' "Factions Guide" cross-references, and CLAUDE.md's Factions Guide table, then deleting the guide pages and rebuilding the viewer.
- [ ] **Pass 3 (Gazetteer, Geography, Governance & Guilds, Lore)** (resolve the `waterdeep-lore.md` Castle Ward conflicts: Watch HQ and the Masked Lords' seat, Tymora/Selûne temples, "South Ward" and Kolat Towers' ward, the dragonward's trigger, the 90-foot statues, Barnibus's rank, "1,200 guards", Yellowspire's ward in `SOURCE_GUIDE.md:214`, Mirt's Mansion ward), then Passes 4 to 7 as in the plan.
- [ ] **Pass 1 residue:** `SOURCE_GUIDE.md:325,651` ("basement cell"); `structure/arc-g` lines 19, 83, 531 (from Session 46's list); Xanathar open items: the X12 briefing must not say "one of Three"; whether Nihiloor's domination changes the motive and Manshoon rulings (`arc-f:408`).
- [ ] **Era 5 / Pilot follow-ups:** the Asmodeus Tenets line needs Siamorphe (`organizations/10-cassalanters.md:20`); the faction-operations Cross-References and the org page both say "faction operations page" without a viewer check; add the `Brother Haldric Wence` clerk correction wherever the Order's door-warden is mentioned.

### Carried forward from Session 46 (still open)
- [ ] **Do the Order outcomes need a Campaign Viewer check?** (Session 45) The Pages workflow rebuilds on every merge touching `campaign/**` or `docs/**`; the deploy for PR 185 was not confirmed.
- [ ] **Wire the Order outcomes into unconverted quests** (out-of-scope "Order of the Gauntlet event rewrite (Session 45)" §1): Faction Outposts (Splinter Intel Reported, Pell's Debt Held, a Pell beat, "Trade Ward" at arc-e :117/:201/:301), Xanathar's Lair (Savra outside the entrance), Cassalanter Villa ("if not run" readers, an orientation check for the r10 dossier), Kolat Towers (Ardin, the gate for M6), the Vault (Order Recognized default, the three tithe outcomes, tone-only today), Dungeon of the Mad Mage (Righteous Hand Reached, Undermountain Mandate Accepted).
- [ ] **Confirm the Session 45 readings** (§4): Night 1 raven DC 14; the M4 Location use with no key and no check; the Marcheon 2:1 refusal rule against the guide; r10 dossier dates from 1480 DR; the writ honored in Waterdeep, Neverwinter, Baldur's Gate and Daggerford; M6 Hard triggers.
- [ ] **Verify unchecked rules** (§6): a generic +1 weapon is not in `items.json` (the r25 nine-weapon table), the Howling Hatred ranks, *Spirit Guardians* and *Hallow* wording, *Resurrection* revival rules, the Zone of Truth scroll.
- [ ] **Accept or replace the Session 45 invented names** (§5), including the "Brother" cluster (Haldric, Hallin, Osric, Teodric).
- [ ] **Other-file leftovers** (§3): Fireball! ev-01:194 against arc-c:98; Appendix B:402; "Cult Fanatic" in other pages; arc-j :258; arc-h:39 and arc-i Gondafrey threads; M2/M3/s02/M5 design notes still list the neutral-good fix as open.
- [ ] **Voice residue** (§7): table-heavy Factions Guide `05` and org page `04`; M5 narration at 21.9; no voice profiles for the Order's recurring minor NPCs.

### Carried forward from Session 44 (Lords' Alliance)
- [ ] **Wire the LA outcomes into unconverted quests.** See the out-of-scope notes, "Lords' Alliance event rewrite (Session 44)" §1 (Faction Outposts, Xanathar's Lair, Cassalanter Villa, Kolat Towers, the Vault including the Writ "if not run" default, and Dungeon of the Mad Mage).
- [ ] **Other factions' events that read LA ranks:** BD Three Nights :226 and DR Davil's Arrest :162/:239 test "Renown 3 or higher". They should test **Redknife Reached**, and a suspended or dismissed member should fail.
- [ ] **Emerald Enclave r50 design notes :27** still refers to the old True/False Commission outcome.
- [ ] **Gralhund ev-01:91**: the **Jalester Brief Received: True / False** heading.
- [ ] **Confirm the readings** (out-of-scope §4): Esloon at three characters (end-of-round-2 exit, or a round-1 exit); M2's "goes loud" cost; r25's Read or Ruling audience; r03's Manor Beat and sergeant's note; M6's Strategic Argument DCs.
- [ ] **Accept or replace the Session 44 invented names** (out-of-scope §5), including the "Ha-" cluster.
- [ ] **Leftovers on the companion pages:** the Trollskull ev-04 old banner and milestone formats outside the LA rows; the `08-notable-patrons.md` Faerrel line, which conflicts with the voice rule that no event raises Faerrel; Saeth's other stats; Laeral's species (moon elf on her page, human in WDH; now a logged settled divergence); Jalester's age.
- [ ] **Voicecheck residue to polish:** the Factions Guide `03` has 11% short sentences, mostly in tables. Several LA event files sit at 6–8% short GM sentences against the 5% target.
- [ ] **Voice profiles** for recurring LA minor NPCs (Sevel Dastar, Mareva Coile, Berna, Harko, Rezka), if the user asks.

### Carried forward from Session 43
- [ ] **Wire the Enclave outcomes into unconverted quests.** See the out-of-scope notes, "Emerald Enclave event rewrite (Session 43)" §1: Faction Outposts (Manshoon Named, Splinter Site Reported, Traitor Identified, Imre Identified); Xanathar's Lair (Pier 17 Investigated, as a casing aid at X4); Kolat Towers (Imre Identified); Vault of Dragons (Cultists Escaped, Anchor Destroyed, Illuun Contact, Brandath Crypts Visited, Jeryth's Message Received; an "if not run" default for M6; a notice rule for Jeryth; an outcome for the Stone naming Illuun at Full Awakening).
- [ ] **Structure-doc Enclave lines:** arc-e:85 (ward); arc-f:59/:61 (the X1/X4 dock); arc-g:535 (ley line "beneath Phaulkonmere" is in the wrong ward); arc-j:47/:83/:274; arc-h:128 (the Tarsakh 15 departure shifts Sarna's dates); the Illuun descriptions in arc-c, arc-e and arc-h.
- [ ] **Act I–II Enclave lines:** Trollskull ev-03:20 (the Tally–Melannor link now comes at the First Meeting); the Fireball! and Gralhund Melannor hooks overlap s02 Surge One.
- [ ] **OotG M3 design notes** claim Splinter intel from Kelso that the event doesn't contain.
- [ ] **Notable Figures leftovers:** the Harpers organization page and Bonnie's page say only Mattrim knows her nature; Tally's page :8 lists M1; Durnan's page uses the "Veteran" block; Gerrick Thatchley has no page; `appendix-a-npc-roster.md` is missing.
- [ ] **Confirm the readings** in out-of-scope §5: r10 beast replaced once per campaign; the M4 grell flee rule; the r25 8th-level spell components; the M6 *water breathing* scroll and condition texts.
- [ ] **Accept or replace the Session 43 invented names** (out-of-scope §6).
- [ ] **Voice profiles** for the recurring Enclave minor NPCs (Gerrick, Sarna Dath, Sorrel Hartwick), if the user asks.

### Carried forward from Session 42
- [ ] **Wire the Force Grey outcomes into unconverted quests** (out-of-scope "Force Grey event rewrite (Session 42)" §2): Xanathar's Lair (Pool Destroyed, Placement Records Taken, Captive Freed, Nihiloor Fled, Nihiloor Identified Party); Sea Maidens Faire (Zelifarn Contacted, Zelifarn Befriended, Submarine Reported, Offerings Returned / Kept); Vault of Dragons (Vajra Briefed, Tower Attack Stopped, Splinter Testimony Recorded, Orvyn Ledger Delivered, Vira Caught / Escaped, Buried Thing Reported; gold-path outcome names for r50).
- [ ] **Act I–II Force Grey fixes:** Trollskull ev-04:79, :109-110 (Force Grey Joined flag), :31, :61; ev-05:55, :83 (Meloon Met flag, to become an Event Outcome); ev-06:73; Trollskull design-notes:49; notable-patrons :55, :57, :61; Gralhund ev-01:94.
- [ ] **Structure-doc Force Grey lines:** arc-b :145, :367; arc-e :377; arc-f :39; arc-g :43, :537; arc-i :41; arc-j :41, :51.
- [ ] **BD M3 `ev-01-three-nights.md:287`** devourer brain line.
- [ ] **Harper M5 ev-02** should read **Pool Destroyed**.
- [ ] **Notable Figures leftovers (Force Grey):** Laeral :8; Durnan :12/:26 "rarely says two words"; Orvyn Dall has no page or voice; Vajra, Meloon, Nihiloor and Hlam still use `> **[GM]**`.
- [ ] **Accept or replace the Session 42 invented names.**
- [ ] **Voice profiles for Force Grey minor NPCs**, if asked.

### Carried forward from Session 41 and earlier
- [ ] **Answer the four Session 41 Harper decisions** in the out-of-scope notes. Decision 3 (Enclave M3 vs Harper M3 on Bonnie) is settled by the Bonnie ruling.
- [ ] **Wire the Harper outcomes into unconverted quests.**
- [ ] **Trollskull ev-04:97-98**, the party-level Harpers Joined; also the other True/False Joined headings at ev-04:100-110.
- [ ] **Act I–II Harper lines:** Remallia (Trollskull ev-04:91, Fireball ev-02:96, staff guide :84); Trollskull ev-07:51, ev-04:71; Saeth Cromley (Fireball ev-01:37).
- [ ] **Structure docs (Harper):** arc-e:495, arc-f:31, arc-i:19/247/265, arc-i:75-77, arc-j:43.
- [ ] **Notable Figures (Harper):** Ahmaergo `02:6`, Remallia `02:6`, Variel `06:8`, and Mattrim as "the only person" who knows about Bonnie.
- [ ] **Accept or replace the Session 41 invented names.**
- [ ] **Clarity/voice pass on the remaining factions**; **DR clarity polish** (deferred).
- [ ] **BD items:** M6 harbor naming; r25 dead branch; guide 08:33; the remaining BD decisions; BD outcome readers and writers; BD companion pages; Act I–II BD contradictions; BD and DR invented names (Ilmra, Odalys and Ilsa collide).
- [ ] **Voice profile for J.B. Nevercott.**
- [ ] **OotG M3** wererat silver rule.
- [ ] **SOURCE_GUIDE:219**; arc-j :55/:75/:322; arc-h :9/:71.
- [ ] **Faction Outposts writes:** Yellowspire Ledger/Letters Taken, Clean Exit, Manshoon Named, Yellowspire Raided. 5B must add the relay ledger and coded letters.
- [ ] **Kolat Towers outcomes:** Vevette, the K18 rune, the DR parallel result.
- [ ] **Gralhund:** Floxin Status becomes named outcomes.
- [ ] **Sea Maidens Faire:** read Soluun's fate.
- [ ] **DR outcomes and companion pages:** wire the DR outcomes into arc-e through arc-j; fix guide 07, org page 06, the Notable Figures pages, `structural-rules.md:9` and `player-factions-overview.md:186`; fix the Act I–II DR contradictions; accept or replace the DR invented names; settle Renown 25/50 reachability for all factions; voice profiles for recurring minor DR NPCs; confirm the three viewer changes.
- [ ] **The six decisions** in "Decisions Needed Before Fixing".
- [ ] **One-faction membership wording** on four guide pages.
- [ ] **Voice profiles for minor Harper NPCs.**
- [ ] **Remaining non-rule inconsistencies:** Finding Floon "two nights" (now fixed), Gralhund "two tendays", Vajra, Istrid's loan.
- [ ] **Ember styling on the live site**, and convert the `[GM]` zones in Finding Floon and Trollskull.
- [ ] **Bestiary.** Nihiloor's block is in `force-grey-mechanics-reference.md` §4.
- [ ] **Convert arc-e through arc-j.**
- [ ] **Guides and setting:** prose pass on the guides and setting pages; Notable Figures polish; recheck the M5/M6 summaries on the other organization pages.
- [ ] **Misc carried items:** `sources/backgrounds.json`; BD ev-03 Ryvarra; sidebar titles; Renaer's Confidence holder; Ember organizations JSON; Trollskull Founders' Day; Asmodean Shrine Area 3 (now noted in the ops copies, still unchecked against the source); `#### Milestone: None` in the other factions; DR Viper muscle; earlier invented details.
- [ ] **Older items:** voice-run tooling portability, reproducible global skills, legacy automation references, the Astra/Sol defaults, the Harper private Site.

---

## Warnings and Caveats

- **The offline wiki dump and its SQLite index live in the scratchpad and are lost with the container** (59 MB compressed, 366 MB indexed; too large to commit). Rebuild in about two minutes with `scripts/fandom-dump/README.md`. Everything else is committed: the 5etools data in `sources/5etools/`, the per-power research bundles in `sources/research/pass2-bundles/`, the Sundering wiki pages and book text in `.../sundering-sources/`, the subclass reference in `docs/plans/`, and the scripts in `scripts/pass2/` (see its README).
- **The hub's By subclass table and fit table were built from the pages before the Sundering and precedence fixes.** Titles, merger text and Draft Notes changed since; the table cells (domain, order, oath, patron) did not, but re-read the hub after any further page edit.
- **Many fits are judgment calls and several are marked loose** (see decision 4). Each page's Draft Notes `Derived` bullet lists its own.
- **Draft Notes on the Deities pages still hold unresolved wiki conflicts** (Tymora's whereabouts after 1384, Amath Seccent/Sercent, Ambrose Everdawn's alignment, the Celestial Stairway, Grand Revel date Alturiak 14 vs Midsummer, the Triad naming). The wiki ranks below the campaign files and 5etools, so none is settled by it.
- **The Sundering rulings cover mergers, the end date and source precedence only.** They do not say how Cyric was freed, whether Iggwilv is free, or what became of Mezro, Dweomerheart, the Outer Planes, shadar-kai, eladrin or the exarchs (the research notes list them as unaddressed by any source in the set).
- **The online research's quotes came through a summarizing fetch tool** and the novel plots are from reviews; spot-check before using them.
- **Pass 2 pages carry full GM information** (the Overview is not player-safe) by the Session 47 ruling; the prose pass will write player-safe versions.

---

## Where to Start Next Session

Read this handoff and `CLAUDE.md`, then do not start a pass until the user names it. The first useful step is to put the "New this session" decisions to the user in one batch (they are small), then apply the answers: the Tymanther leftovers and the stale Draft Notes are mechanical and can go to `prose-drafter` in batches of five pages using `docs/plans/setting-compendium-pass2-repass-instructions.md` as the model brief. Then, when the user names a pass: the **Factions Guide move** (decided in Session 47, not executed; retarget the inbound links in the carried list first) or **Pass 3 (Gazetteer, Geography, Governance and Guilds, Lore)**. For Pass 3, rebuild the wiki from `scripts/fandom-dump/README.md`, give `source-researcher` the pre-extracted files and a `notes_file`, and brief `prose-drafter` only afterwards. Run `voicecheck.py` and the stale-reference grep on every returned page yourself (drafters have no shell).
