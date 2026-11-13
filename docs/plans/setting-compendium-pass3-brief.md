# Setting Compendium Rebuild: Pass 3 (Gazetteer, Geography, Governance & Guilds, Lore) Brief

Binding brief for every Pass 3 researcher and drafter. It adds to the rebuild plan (`setting-compendium-rebuild-plan.md`, "Page templates" and "Page rules"), the pilot brief and the Pass 2 brief, and does not replace them. The approved model page is `campaign/gazetteer/waterdeep/castle-ward.md`. Copy its shape for every ward. The Pass 2 pages (`campaign/setting/deities/asmodeus.md`) show the register for non-ward pages.

## Scope

The pass retires `campaign/setting/waterdeep-lore.md`. Every block of that file gets a home, then the file is deleted in the close-out commit.

| Journal | File (kebab-case) | H1 |
|---|---|---|
| `campaign/gazetteer/waterdeep/` | `castle-ward.md` (done) | Castle Ward |
| | `sea-ward.md`, `north-ward.md`, `trades-ward.md`, `southern-ward.md`, `dock-ward.md`, `field-ward.md` | Sea Ward, North Ward, Trades Ward, Southern Ward, Dock Ward, Field Ward |
| `campaign/setting/geography/` | `city-of-the-dead.md`, `undermountain-and-skullport.md`, `dragonward-and-walking-statues.md`, `waterdeep.md` (written last) | City of the Dead, Undermountain and Skullport, The Dragonward and Walking Statues, Waterdeep |
| `campaign/setting/governance-and-guilds/` | `open-lord-and-masked-lords.md`, `code-legal-and-magisters.md`, `city-watch.md`, `guilds.md` | The Open Lord and the Masked Lords, The Code Legal and the Magisters, The City Watch, The Guilds |
| `campaign/setting/lore/` | `stone-of-golorr-and-the-eyes.md`, `vault-of-dragons.md` | The Stone of Golorr and the Eyes, The Vault of Dragons and Neverember's Embezzlement |

Not in this pass: temples (the Deities hub holds the Major Temples table; a ward page lists its temples and points to the hub), the festival calendar (History 09), the Grand Game (Pass 4), the Gondar page (the House of Inspired Hands location journal covers it).

### Where each block of `waterdeep-lore.md` lands
- *The Wards* bullets: one per ward page, City of the Dead and Undermountain pages; `waterdeep.md` summarises them.
- *Governance* bullets: Open Lord and Masked Lords, Code Legal and Magisters, City Watch.
- *Guilds* bullets: `guilds.md`.
- *Religion* bullets: ward Religion lines, the Deities hub; the Cassalanter temple stays on Cassalanter pages and is not a ward fact.
- *Festival Calendar*: already History 09.
- *The Dragonward and Walking Statues*: `dragonward-and-walking-statues.md`.

## Rulings (user, Session 49; they bind every page)

1. **The published adventure wins** over the campaign outline where the two disagree about the Castle Ward's offices and the temples:
   - The Castle Ward holds neither the Watch headquarters nor the Masked Lords' seat. Petitioners meet the Masked Lords in the Palace audience chamber.
   - Temples follow the Major Temples table (`adventure-wdh.json` caption at about line 30910): Tymora's Tower of Luck is Castle Ward in the table and Sea Ward in the Sea Ward text; the page states the table and puts the split in Draft Notes. Helm's Hall is the Southern Ward.
   - Kolat Towers: the Dragon Heist character appendix (lines 32215 and 32218) says Southern Ward and the wiki agrees. Line 560 says Trades Ward. The Southern Ward page treats it as the Southern Ward's tower, with the Trades Ward reading in Draft Notes. This reverses the campaign's `arc-i` value; the retargets are listed in the close-out.
2. **Dragonward:** dragons are physically unable to enter unless touched by the dragonstaff of Ahghairon. It does not depend on the Open Lord's permission.
3. **Walking Statues:** only the original statue is 90 feet. Only the Griffon woke (1479 DR).
4. **Barnibus Blastwind:** a Watchful Order investigator with a Sea Ward estate, not clearly a magistrate. "1,200 guards" and "personally compromised" have no source; drop them or mark `[research]`.
5. **Mirt's mansion:** Castle Ward, near the Naval Harbor (the pilot's reading). The Harper events keep their Sea Ward dinner house.
6. **Yellowspire** is a Castle Ward tower.
7. **Field Ward** gets its own gazetteer page. The published adventure files it under "Outside the City Proper".
8. **Campaign-only facts stay, tagged:** Durnan as a secret Masked Lord and founder of the Red Sashes; Laeral as a moon elf. The published adventure names Mirt as the Masked Lord among the Castle Ward residents; say which is which.

## Binding rules from earlier passes

- Cassalanter secrecy, Bregan D'aerthe's rejection of Lolth, the Sundering canon (1487; FRHoF over SCAG), "god of X" wording, "Xanathar's Guild" with Xanathar as "it", GM never DM, two Zhentarims, no soul coins, and "last night" for Floon.
- Everything except the player-safe `## Overview` is the GM layer. Open items go in one deletable `> **[GM]**` `#### Draft Notes` at the bottom. `#### GM Notes` is the default GM callout; `#### Secret` is rare and changes play.
- Campaign decisions outrank the published adventure outside the rulings above; the published adventure outranks the wiki; the wiki is paraphrased, never copied, with the edition tagged. Nothing is invented: a gap is `[research]`.
- Ward pages: 8 to 10 landmarks and 5 to 6 characters, one Secret, hidden-affiliation notes only where they change play. Campaign sites point to their location journal by bold name (**Xanathar Sewer Hideout**, **Zhentarim Warehouse**, **Trollskull Manor**, **Gralhund Villa**, **Cassalanter Villa**, **House of Inspired Hands**, **Sea Maidens Faire**). Quest hooks come from the quest and faction-event journals; read them, do not guess.
- Characters of Interest cite Notable Figures by bold name with `Name (Alignment, Species, pronouns)` taken from the page, not inferred. An NPC with no page is plain text and goes in Draft Notes.
- A ward's population, lifestyle, languages and dominant faith are blank in the wiki for most wards. Use labelled city-wide figures as the Castle Ward page does, or `[research]`.
- Cross-references use bold names that match an existing page or a page in this roster. No `.md` links.
- Do not link to deity pages that do not exist; check `campaign/setting/deities/`.

## Inputs

- Bundles: `sources/research/pass3-bundles/<slug>/` with `adventure.txt` (Chapter 9 lines with `file:line`), `wiki.txt` (the ward page and linked pages, raw wikitext), `campaign-hits.txt` and `adventure-hits.txt` (every line naming the page's aliases). Build: `scripts/pass3/bundle_pass3.py`.
- Research notes: `docs/plans/setting-compendium-research-notes/pass3/batch-*.md`, one `## <slug>` section per page, full exact quotes with file and line.
- Source guide: `sources/SOURCE_GUIDE.md`. Alexandrian files for outposts and hideouts: `sources/Act_III_Arc_E.md`, `Act_III_Arc_D.md`.

## Reports

Researchers: for each page, the facts by page section (At a Glance, Landmarks, Characters, Secret, Life in the Ward, Read Aloud anchors), each with a full quote and `file:line`; conflicts quoting both sides; the list of campaign sites, quests and faction events set in the ward. No paraphrase-only entries.

Drafters: files written; facts that could not be sourced; judgment calls; conflicts with both `file:line`; every other file found wrong (do not edit it). Do not commit. Say that `voicecheck.py` was not run; the main session runs it.
