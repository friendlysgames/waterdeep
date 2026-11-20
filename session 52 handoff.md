# Session 52 Handoff
**Date:** 2026-11-20
**Status:** Ready to continue. Everything is merged to `master` (PRs 395 to 433); the working branch matches master. No pass is in progress. Wait for the user to name the next task.

---

## What Was Done

Session 52 ran Setting Compendium Pass 5 (Organizations) to completion, then rebuilt it twice after the user's corrections. The ten organization pages were first brought to the Cassalanters shape. The user then ruled that setting pages are campaign-start lore only, and later that they must carry real lore (history, beliefs, structure, tactics, relationships). All ten pages were reworked to both rulings, and two new organizations the user asked for (House Gralhund and the Open Lord's Watch) were added as a lore page and a Factions Guide mechanics page each. Every page went through its own PR as its agent finished, and a final audit fixed the stances and cross-references that disagreed.

---

## Changes Made

89 commits and 115 files changed between PR 394 and PR 433 (64 added, 51 modified).

### Files Modified (by area)
| Area | What changed |
|---|---|
| `campaign/setting/organizations/01` to `10` | Each page now has History, Beliefs (was Tenets), Structure, Methods and Tactics, Relationships, Key Members, Grand Game Agenda (player factions), Overview, GM callouts, Tone, Source References, Cross-References and Draft Notes. Operations is dissolved. Mission, quest-event and Event Outcome text was removed or restated as day-one fact; removed quest-bound facts are listed in each page's Draft Notes under "Routed to quests". |
| `campaign/guides/factions/01-overview.md` | New Minor Factions table listing pages 12 and 13. |
| `campaign/guides/gm-guide/` (`running-the-villains`, `grand-game-in-play`, `structural-rules`) | Pointers to the two new reactor factions; `structural-rules.md:9` now says Manshoon's cell prefers to capture rather than kill. |
| About 34 files in `setting/` (deities, history, lore, the-grand-game, villains, governance, geography), `gazetteer/`, `quests/` | Line citations into the organization pages retargeted twice; claims the pages no longer support were reworded. |
| `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md` | "three years in the post" replaced, since Vajra has held the title since 1479 DR. |
| `CLAUDE.md` | New rule "Setting pages are campaign-start lore"; `organizations/` and Factions Guide table rows updated to twelve pages and pages 12 and 13. |
| `docs/plans/setting-compendium-rebuild-plan.md` | Pass 5 row rewritten as done. |

### Files Created
| File | Purpose |
|------|---------|
| `campaign/setting/organizations/11-open-lords-watch.md` | Lore page: the City Watch as the Open Lord's instrument and a Grand Game participant (H1 "The Open Lord's Watch"; the governance page keeps the H1 "The City Watch"). |
| `campaign/setting/organizations/12-house-gralhund.md` | Lore page for House Gralhund. |
| `campaign/guides/factions/12-open-lords-watch.md`, `13-house-gralhund.md` | Mechanics pages: Grand Game Stance, Response Team, Escalation, Revelation List. No renown, ranks or missions. |
| `docs/plans/setting-compendium-pass5-brief.md` | Binding brief with rulings 1 to 29 (ruling 28 is campaign-start lore; ruling 29 is the lore sections). |
| `docs/plans/setting-compendium-pass5-drafter-instructions.md` | Drafter instructions. |
| `docs/plans/setting-compendium-research-notes/pass5/*.md` (11 files) | Research notes with exact quotes and file:line for each faction. |
| `scripts/pass5/` (`bundle_pass5.py`, `check_quotes.py`, `README.md`) | Builds one research bundle per organization from the wiki index; verifies quotes. |
| `sources/research/pass5-bundles/<slug>/` (11 folders) | The bundles (wiki.txt, campaign-hits.txt, adventure-hits.txt). |

### Files Deleted
None.

---

## Key Decisions

### Setting pages are campaign-start lore
**Decision:** Pages under `campaign/setting/` and `campaign/gazetteer/` present the world as of Ches 1, 1492 DR and never narrate missions, quest events, reveals, arrests or Event Outcomes.
**Reasoning:** The user found mission numbers and quest events on the pages after the mechanics had been removed. Recorded in `CLAUDE.md` and as ruling 28 in the Pass 5 brief.
> "These documents are supposed to present lore up to campaign start. Like how any other lorebook does it. Are you actually stupid?" — User, this session

### Organization pages carry real lore
**Decision:** Every organization page has History, Beliefs, Structure, Methods and Tactics and Relationships (ruling 29), all sourced or tagged `[research]`.
**Reasoning:** After the cleanup the pages held no history, tactics or relationships.
> "I'm not reading any actual lore for these organisations. No history sections, for example. No beliefs. No tactics. No relationships. Nothing. What lore are we writing exactly?" — User, this session

### Add the Gralhunds and the City Watch
**Decision:** Add only those two. The City Watch gets a new organization page (option A) rather than staying only on the governance page; its H1 is "The Open Lord's Watch" to avoid colliding with the governance page's "The City Watch". Each gets a lore page and a Factions Guide page.
> "1. Just those two. 2. A 3. After cleanup is done." — User, this session

### Merge each document as its agent finishes
**Decision:** Every finished page goes through its own branch, PR and merge immediately, before review; edit passes merge separately.
**Reasoning:** The user reminded me after I batched work. This session used a throwaway `git worktree` off `origin/master` for each PR, because agents write into the shared working tree.
> "Didn't I tell you, multiple times, that you should PR and deploy after each agent completes?" — User, this session

### Decisions made on the user's behalf (easy to overturn)
- Organization pages dissolve `## Operations` into Structure and Methods and Tactics, and `## Tenets` becomes `## Beliefs`.
- The Gralhund guide follows `ev-09-aftermath.md:44` ("Hrabbaz is dead") and adds a replacement guard.
- The fleet dates (Ches 21 arrival, Tarsakh 20 departure) and Founders' Day stay as scheduled facts.
- Stance rulings in the brief (Xanathar's Guild and the Doom Raiders are enemies; the Harpers are allies with the Watch through Mirt).

---

## Rules and Instructions

These must be respected in all future sessions.

- **Final prose is written in universe.** When this lore is written out for real (the later prose pass), it is in-universe with no mention of sources, wikis, editions, book titles, line numbers, `[research]` tags, design tags or Draft Notes. Today's Source References, Draft Notes callouts and edition-tagged wiki citations are structuring scaffolding to be stripped. *(User, this session: "Make a note for yourself that once we write this out, it will be written in universe, with no mention of sources or wikis or anything of the sorts.")*
- **Campaign-start lore only** for setting pages (see Key Decisions). Past events before Ches 1, 1492 DR are lore; quest-time events and Event Outcome gates are not. Future scheduled dates (Founders' Day, the fleet) may be stated as plans.
- **Organization pages carry the five lore sections** (ruling 29) and no mechanics. Mechanics (stance, hooks, response teams, escalation, revelation lists, renown, ranks, missions) live in the Factions Guide.
- **PR and merge per document**, using a throwaway worktree off `origin/master`; after each merge, discard identical local copies by named file and merge `origin/master` into the working branch. Never run a blanket `git checkout -- campaign`: the auto-mode classifier blocks it and it would discard agent work. *(User: "Didn't I tell you, multiple times, that you should PR and deploy after each agent completes?")*
- **Resume agents after a rate limit** with SendMessage; the limit is account-wide and agents keep their saved work.
- **Present decisions plainly.** The user found my issue lists confusing. Write one decision at a time with the quoted lines, file and line, options and a recommendation, and no internal labels such as "Issue 12" or "ruling 28". *(User: "The way you have laid out the issues is very, very confusing.")*
- **Carried from Session 51 and still binding:** canon is canon unless changed for a stated design reason; mechanics live in the guides and lore in the setting; Cassalanter secrecy; Bregan D'aerthe rejects Lolth; Xanathar is "it"; the guild is "Xanathar's Guild"; Threestrings is a Harper agent; Lords' Alliance Renown never falls; Zardoz Zord rule (the Bregan Overview shows J.B. Nevercott and Captain Zardoz Zord as two figures); humans take a Faerûn ethnicity; Event Outcomes, never "flag"; handoff only on `/handoff`.

---

## Problems Solved

- **Mission and quest text on lore pages:** removed from all ten pages and routed to Draft Notes with the file where each fact already lives.
- **Stale line citations:** about 34 files cited organization-page lines that moved three times (the cleanup, the lore passes, the rewrites). Each now cites the current line.
- **Stances that disagreed between pages:** Harpers and the Watch, Xanathar's Guild and the Doom Raiders, and three Gralhund bullets with no stance word.
- **Wrong cross-reference titles:** five pages cited "The Doom Raiders"; the H1 is "The Zhentarim (Doom Raiders)".
- **Zardoz Zord rule broken by a drafter** on the Bregan Overview: restored to two separate figures.
- **Rate limits** stopped five agents three times; each was resumed with its work intact.
- **`structural-rules.md:9`** said Manshoon's cell "conducts assassinations"; corrected to capture.

---

## Outstanding Work

### Needs a user ruling
- [ ] **Yalah and the Stone** (`campaign/guides/factions/13-house-gralhund.md`, Grand Game Stance): if Yalah keeps the Stone, the page sends it to Bregan D'aerthe (Fel'rekt's offer at the villa, `ev-06:69`) or to the Open Lord. The Open Lord branch conflicts with `03-lords-alliance.md:9` ("She doesn't know that the Stone of Golorr has resurfaced in Waterdeep"). Recommendation: Bregan D'aerthe only.
- [ ] **Hrabbaz alive or dead:** `ev-09-aftermath.md:44` ("Hrabbaz is dead") against `ev-06:37` ("Hrabbaz stands down") and `ev-04:79` ("He steps aside"). The guide follows ev-09. Recommendation: keep.
- [ ] **Key Members labels:** Zelifarn (`07-bregan-daerthe.md`; his page says "None (friendly to Bregan D'aerthe; not an operative)"), Bonnie and Nessa Vayle (`01-harpers.md`; their pages say "Independent" and "Unaffiliated"). Recommendation: keep as listed.
- [ ] **Ott Steeltoes** (`08-xanathars-guild.md`): prisoner in the Interrogation House against tending the fish (`06-ott-steeltoes.md:25` and `:29`). Recommendation: leave open until Pass 6.
- [ ] **Figures in Draft Notes** (renown thresholds, loan sizes, vault shares on pages 02, 06, 07): keep in the deletable callouts or move to the research notes only. Recommendation: keep.
- [ ] **Lords' Alliance honest failure and reinstatement** (carried): `player-factions-overview.md:26` against `03-lords-alliance.md:76`; `01-overview.md:11` against `03-lords-alliance.md:78`. Recommendation: follow the Lords' Alliance page in both.
- [ ] **Khafeyta Murzan** "Mulhorandi" against "Mulan" (carried). Recommendation: keep "Mulhorandi".
- [ ] **`ev-09-aftermath.md:112`**: Savra says "That is Cassalanter embroidery on a cultist's robes". Reads as suspicion because she adds she cannot prove it, but borderline against the secrecy rule. Recommendation: keep.

### Cleanup the user was offered
- [ ] **Manshoon Named gates on setting pages:** `history/04-the-founding-of-chains.md:61, 79, 84`, `deities/bane.md:73`, `gazetteer/waterdeep/castle-ward.md:131`, `southern-ward.md:48, 141`, `governance-and-guilds/open-lord-and-masked-lords.md:68`, `notable-figures/emerald-enclave/02-jeryth-phaulkon.md:34`, `deities/mielikki.md:81`, `lore/stone-of-golorr-and-the-eyes.md:88, :118`. Each should be restated as a day-one fact. Not started; the user has not answered.
- [ ] **Notable Figures pages that carry quest-time lines** (arrest, mission, "after" wording): Davil, Tashlyn, Yagra, Skeemo and Senna Vael (doom-raiders), Chirada and Hurv Taldred (gralhunds), Yalah (`01-yalah-gralhund.md:21`), Bonnie (`04-bonnie.md:6, :25`). Belongs to Pass 6.
- [ ] **Citations inside organization pages that point at other organization pages** are partly stale: `02-lords-alliance.md:138`, `06-doom-raiders.md:132`, `11-open-lords-watch.md:119` and `:164`. The sweep skipped organization pages by instruction.
- [ ] **Gralhund and Watch Factions Guide pages need a rules pass:** monster names (Tough, Spy, Warrior Veteran, Adept, Mage Apprentice) came from the repo's rename table and older docs, not the 2024 data; the Open Lord team has not been rebalanced under CR 2.0. Use `rules-lookup` and `encounter-builder`.
- [ ] **Setting-page mismatches the agents logged** (not edited): the Gralhund crest (sword above shield against gryphon or serpent), Hrabbaz's species ("half-orc" against "orog"), Yalah's ward ("Sea Ward" in her page and `03-reading-room.md:17`; the villa is in the North Ward), `running-the-villains.md:11` ("four factions" competing for the Enigma while House Gralhund also wants the Stone), `deities/tyr.md:93` ("priests of the Triad"), `deities/eldath.md:104` and `mielikki.md:118` (Enclave patron), `history/07:134` typo "the retired the retired", `dock-ward.md:63` (the Long Watch placed in the Dock Ward against the Trades Ward), `city-watch.md:63` and `:133` (Vajra "Neutral", Savra "lawful good"), `open-lord-and-masked-lords.md:113` ("no Open Lord response rule", now stale), `guilds.md:48` (Rishaal and Ulkoria as Order members), `10-keln-trigos` "Tier 1 outpost keeper".

### Next passes (wait for the user to name one)
- [ ] **Pass 6 (Notable Figures)** and **Pass 7 (Introduction, cleanup, docs)** from `docs/plans/setting-compendium-rebuild-plan.md`. Pass 7 also updates `adventure-reloaded` and `SOURCE_GUIDE.md` pointers for the organization shape.
- [ ] **New quest-arc format** for Faction Outposts through Vault of Dragons: renown sidebars per arc, the **Manshoon Named** marker (`arc-e:211`), faction outcomes wired into the unconverted quests.
- [ ] **Volo-voice pass** with Elminster's marginal corrections (`docs/plans/volo-asides-archive.md`), a standing rule in `CLAUDE.md` and `ember-setting-style`, and voice profiles for Volo and Elminster.
- [ ] **In-universe prose pass:** strip Source References, Draft Notes, `[research]` and design tags and wiki citations; rewrite for the final voice (see Rules).
- [ ] **Undermountain pass:** resolve "something vast and dreaming" (`arc-f:382`); Floxin, Yalah and Night Gazer outcomes reserved for Mad Mage.

### Carried forward from Session 51 and earlier, still open
- [ ] Pass 2 follow-ups: swap any of the thirteen patrons; a Siamorphe wiki-only page review.
- [ ] Sea Maidens Faire rooms 01 to 04 not checked against "submarine moored all year".
- [ ] "attunement" wording in five quest events (Harpers m06, BD r10, Order r10, Fireball! ev-02 and ev-04).
- [ ] Unsourced rows kept with `[research]` (Jarlaxle's Renaer row, Manshoon's "deserters" clause, the Cassalanter "three sessions" trigger, others in the Session 50 handoff) and source conflicts in Draft Notes (Kolat PDF p.96 against "Manshoon holds no Eye"; Skeemo as traitor against "compiles all of it").
- [ ] Invented details to confirm: "within days" for Zelifarn's arrival (`arc-h:19`), the Q03 strongbox and reassigned guard.
- [ ] Source-check follow-ups: the wiki's claim that the public knew of the embezzlement by 1492 DR; `arc-i:43` and `arc-j:53` still say Doom Raiders Mission 6 delivers the 43 names and the Splinter list.
- [ ] Howling Hatred ranks have no source (`s02-savras-past`); the *Banishment* class lists; the XDMG +1 Weapon "counts as magical" wording.
- [ ] `history/08` 1491 date for the *Scarlet Marpenoth*.
- [ ] Stale design-note claims and line citations in faction-event design notes that cite `guides/factions/*.md:NN`.
- [ ] Faction Outposts kidnap scene (`arc-e:293` to `:311`) calls Fenerus "a civilian in over his head"; he is a CR 2 Bandit Captain.
- [ ] Missing Notable Figures pages (Elminster, Khelben Arunsun, Halaster, Piergeiron, Raurlor, Alethea Brandath and the Session 50 list), plus Sevel Dastar, Ysmay Halvane, Rhendar Orsk, Garrick Stoll, Sera Vantry, Vaelle Lurval, Hyustus Staget (partial) and the Commander of the Watch; wiki items still open (ward Lifestyle, Languages and dominant faith; Midsummer, Twin Parades and Fey Day; the Code Legal's author and date).
- [ ] Voice residue: short-sentence rates run 7 to 24% on the new pages; no voice profiles for the Order's recurring minor NPCs; the prose-writing pass is deferred for everything.

---

## Warnings and Caveats

- **Line citations are fragile.** Any edit to an organization page moves lines that about 34 files cite. Prefer citing a page and section name in new work, and run a citation sweep after editing any organization page.
- **The three-times-rewritten pages carry design tags and `[research]` tags in the body.** They are scaffolding for the prose pass, not final text.
- **Do not write into the shared working tree while agents run.** Agents edit files in place; use a worktree off `origin/master` for each PR, discard identical local copies by named file, then merge master. A blanket `git checkout -- campaign` is blocked and destructive.
- **The wiki dump and indexes live in the scratchpad** and are lost between sessions (`scripts/fandom-dump/README.md` rebuilds them; `bundle_pass5.py` reads them). The committed bundles under `sources/research/pass5-bundles/` do not need the dump.
- **Research notes contain agent errors:** they said the Alexandrian PDFs have no text layer (`pdftotext -layout` works), and several quote line numbers were off. Open the cited line before using a quote.
- **The Gralhund and Watch Factions Guide pages are first drafts.** Both have design calls (tagged `[D1]` to `[D7]` on the Watch page) and unverified monster names.
- **Generated pages** (`docs/index.html`, `campaign-reader/dist/index.html`) are built output; do not edit them. The Pages deploy for PR 432 was still running at the last check; PRs 395 to 431 deployed successfully.

---

## Where to Start Next Session

Read this handoff and `CLAUDE.md`, then wait for the user to name a task. Likely candidates are Pass 6 (Notable Figures, the other 122 pages), the Manshoon Named gate cleanup on the setting pages, or the rules pass on the two new Factions Guide pages. Before any of them, put the open rulings under "Needs a user ruling" to the user, one at a time, with the quoted lines. The organization pages are finished structurally; do not rewrite them without an instruction.
