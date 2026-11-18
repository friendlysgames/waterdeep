> **ABANDONED (Session 51):** the move this spec plans was reverted; the Factions Guide stays at `campaign/guides/factions/` and the setting journal is lore only.

# Factions Guide move: research report for the move spec

Repo root: /home/user/waterdeep. Paths below are relative to it (absolute form = `/home/user/waterdeep/` + path).

## File not written

You asked for the spec to be written to `docs/plans/factions-move-spec.md`. My instructions allow me to write only a `notes_file` that the caller supplies, and none was given, so I did not write it. The full spec is in this report. To save it, write this message to `/home/user/waterdeep/docs/plans/factions-move-spec.md`, or re-run with `notes_file` set.

## Method limits

- I had no shell, so the pilot-to-guide comparison in (c) was done by reading both files line by line. It was not a `diff` run. Please run `diff` on the two files to confirm.
- Line numbers come from Read and Grep output. Several older notes (`consistency-pilot-pages.md`, `setting-compendium-pilot-findings.md`) cite line numbers from before later edits. Where a cited line no longer matches, I give the current line and say so.
- Published adventure and Alexandrian PDFs were not searched. This is a file-layout task, and adventure text does not hold guide structure.
- The Ember export was not opened. CLAUDE.md requires it before restructuring quest, event, area or room pages. This move restructures setting pages, so I read that rule as not applying.

---

## (a) Rebuild plan (`docs/plans/setting-compendium-rebuild-plan.md`)

**Target row**
> "| `setting/faction-operations/` | 10 GM-only companion pages: renown & ranks, missions, outposts, response teams, escalation, revelation list |"
> — docs/plans/setting-compendium-rebuild-plan.md:34

> "Folder names carry no numeric prefix. The existing folders are unprefixed and CLAUDE.md, the skills and the viewer reference them. Wards live in a separate gazetteer because Ember keeps region pages light and puts district detail in its own journal. Faction operations get their own journal so Foundry can gate it at journal level instead of page by page."
> — docs/plans/setting-compendium-rebuild-plan.md:37

**Page template frame**
> "Every page: `# Title` → `> Structuring draft.` → `> **[GM]**` Gamemaster's Summary → `**Purpose:**` → body skeleton → `**Tone:**` → `---` → Source References → Cross-References (bold names) → Draft Notes (only where open items exist)."
> — docs/plans/setting-compendium-rebuild-plan.md:40

**Page rules (decided Session 47)**
> "**Page rules (decided Session 47):**"
> — docs/plans/setting-compendium-rebuild-plan.md:42

> "- Everything except the player-safe `## Overview` is the GM layer; the Foundry conversion wraps it in `gamemaster` blocks. Markdown order is unchanged."
> — docs/plans/setting-compendium-rebuild-plan.md:43

> "- Open items live in a deletable `> **[GM]**` `#### Draft Notes` callout at the very bottom of the page, with Research, Conflicts and Routed facts bullets. Inline `[research]` tags stay in place."
> — docs/plans/setting-compendium-rebuild-plan.md:44

> "- `#### GM Notes` is the default GM callout. `#### Secret` is reserved for hidden facts that change play."
> — docs/plans/setting-compendium-rebuild-plan.md:45

> "- Faction operations pages are the single home for faction mechanics; the Factions Guide pages move there."
> — docs/plans/setting-compendium-rebuild-plan.md:50

> "- Until the prose pass, every page may carry its full GM information, including in the Overview. The prose pass writes the player-safe version of each Overview (the Zardoz Zord rule, the Cassalanter secrecy rule and the spoiler rule apply then)."
> — docs/plans/setting-compendium-rebuild-plan.md:51

**Skeleton table (header and Hub row)**
> "| Page type | Body skeleton |"
> — docs/plans/setting-compendium-rebuild-plan.md:53

> "| Hub (The History, Setting Introduction, Deities) | GM Lore Summary bullets; opening slot; bold-topic H2s or a bullet list of the child pages; Overview |"
> — docs/plans/setting-compendium-rebuild-plan.md:55

**Faction operations template row**
> "| Faction operations (GM-only) | Gamemaster's Summary; Grand Game Stance; Quest Hooks; First Meeting; Renown & Ranks; Missions; Response Teams; Outposts; Escalation; Revelation List (the existing sections, moved verbatim, in a unified order) |"
> — docs/plans/setting-compendium-rebuild-plan.md:62

**Principles that bind the move**
> "2. **Nothing lost.** Every fact in today's files lands in exactly one new page. Verbatim roleplay and operations text is moved, not rewritten (only stale references get retargeted)."
> — docs/plans/setting-compendium-rebuild-plan.md:14

> "4. **Two audiences on every page.** GM-facing material sits above the player-safe `## Overview`, as on today's NPC pages. The Overview follows the existing spoiler rule: only the public face, nothing about the Stone, the Eyes, the vault or secret allegiances."
> — docs/plans/setting-compendium-rebuild-plan.md:16

**Verification rules**
> "- Heading and bullet counts of each old file equal the sum across its new pages. For Notable Figures and Organizations, the verbatim roleplay and operations paragraphs diff identical before and after, apart from the retargeted references."
> — docs/plans/setting-compendium-rebuild-plan.md:102

> "- `grep -rEn "ch2-city|ch1-beginning|Arc [A-J]\b|Appendix [A-F]|\bDM\b"` over the new pages returns nothing."
> — docs/plans/setting-compendium-rebuild-plan.md:103

> "- No `.md` links remain. Every bold cross-reference names an existing page."
> — docs/plans/setting-compendium-rebuild-plan.md:104

> "- Every page has a GM summary, an Overview and Source References. Every Overview obeys the spoiler rule."
> — docs/plans/setting-compendium-rebuild-plan.md:105

> "- Page counts match: 122 figure pages, 10 + 10 organization pages, one page per confirmed deity."
> — docs/plans/setting-compendium-rebuild-plan.md:106

Note: rule 102 (count equality) and rule 105 (Overview on every page) do not say how faction-operations pages are checked. Rule 105 conflicts with the template row at line 62, which has no Overview. The pilot has no Overview either (see Decision D2).

**Pass 5 and pass 7**
> "5. **Organizations.** 10 factions × (lore page + operations page), one faction at a time with checks between. Operations text moves verbatim; the lore page is new. This pass also resolves the heading drift across the current files (`01`–`04` use `### Earning Renown` / `### Ranks & Benefits`, `05`–`06` are flat, `08`–`10` omit Grand Game Stance, `06` lacks the villain sections, `07` is a hybrid)."
> — docs/plans/setting-compendium-rebuild-plan.md:91

> "7. **Introduction, cleanup and docs.** Write the introduction page. Update `CLAUDE.md`, the `adventure-reloaded` skill (File Type Specs 7 and 8 and the Setting Compendium block) and any `SOURCE_GUIDE.md` pointers. Run `consistency-checker`. Offer a viewer rebuild (the `update-campaign-viewer` skill already reads everything under `campaign/` except `structure/`)."
> — docs/plans/setting-compendium-rebuild-plan.md:93

The pass 5 heading-drift description does not match the guide pages. Under either numbering, the guide headings in (d) differ from it. It may describe the organization pages instead; I did not check that claim.

**Decisions and out of scope**
> "- Faction operations are a separate journal from Organizations."
> — docs/plans/setting-compendium-rebuild-plan.md:111

> "## Out of scope"
> "The Bestiary, the final prose pass, Foundry JSON, the HTML Artifact delivery, and the quest and location journals."
> — docs/plans/setting-compendium-rebuild-plan.md:116–117

The out-of-scope list does not exclude moving the guide pages.

---

## (b) Cassalanter pilot documents

**Pilot brief, assignment D**
> "| D | Organization pair | `campaign/setting/organizations/10-cassalanters.md` (rewrite in place) and `campaign/setting/faction-operations/10-cassalanters.md` (new) | Lore page from the existing organization page. Operations page from `campaign/guides/factions/11-cassalanters.md`, moved verbatim into the plan's unified section order. **Leave the guide page untouched.** |"
> — docs/plans/setting-compendium-pilot-brief.md:68

**Pilot brief, frame and rules**
> "Keep each frame element the plan lists, in the plan's order, and drop none."
> — docs/plans/setting-compendium-pilot-brief.md:38

The brief's frame uses a different GM callout from the page the pilot wrote:
> "> **[GM]**"
> ">"
> "> #### Gamemaster's Summary"
> — docs/plans/setting-compendium-pilot-brief.md:18–20

> "10. Do not commit, do not touch files outside your assignment, do not delete anything."
> — docs/plans/setting-compendium-pilot-brief.md:51

**Pilot findings**
> "| Organization pair | `setting/organizations/10-cassalanters.md`, `setting/faction-operations/10-cassalanters.md` | Operations page diffed line for line against `guides/factions/11-cassalanters.md` |"
> — docs/plans/setting-compendium-pilot-findings.md:12

> "**DECIDED (Session 47, user answers):** Items 1-3 adopted as recommended. Item 4 adopted **except Appearance** (add the "Using X as a Deity" box, the epithet-name rule, Plane and Typical Followers; no Appearance section). Items 5-8 adopted as recommended. Items 9-10 adopted as **move** (delete the guide pages after copying, retarget inbound links, rebuild the viewer). The Pass 0 pilot pages still need to be brought in line with these decisions, and the Deity pilot needs the Appearance-free slots added."
> — docs/plans/setting-compendium-pilot-findings.md:20

> "9. **Faction operations.** The plan assumed the mechanics sat on the organization pages. They sit in `campaign/guides/factions/` (response teams, outposts, escalation, revelation list, and for player factions renown and missions). The pilot copied the Cassalanter guide text into `setting/faction-operations/10-cassalanters.md` and left the guide untouched. Decision: **move** (delete the guide pages and retarget inbound links at `guides/factions/01-overview.md:47`, `gm-guide/grand-game-in-play.md:103`, `gm-guide/structural-rules.md:26,90,122`, `setting/villains/cassalanters.md:57` and `CLAUDE.md`'s Factions Guide table) or **keep both** (duplication, which drifts)."
> — docs/plans/setting-compendium-pilot-findings.md:32

Stale line: `setting/villains/cassalanters.md:57` no longer holds a guide reference. The current hit is `campaign/setting/villains/cassalanters.md:96`, and the other hits are at lines 10, 111, 117 and 134 (see (g)).

> "10. **Foundry gating and the viewer.** Factions Guide pages are already read by the viewer. A new journal changes what the viewer shows; plan a rebuild after the move decision."
> — docs/plans/setting-compendium-pilot-findings.md:33

> "- Pilot commits are on `claude/trusting-pasteur-a76rfy` and are not merged to master: the templates are not approved yet."
> — docs/plans/setting-compendium-pilot-findings.md:84

I could not check git, so I cannot say whether the pilot page is on master. The file exists in the working tree at `campaign/setting/faction-operations/10-cassalanters.md`.

**Consistency pass (`docs/plans/setting-compendium-research-notes/consistency-pilot-pages.md`)**
> "## E. ops vs guide drift"
> — consistency-pilot-pages.md:40

> "29 DRIFT: Response Teams, Outposts, Escalation, Revelation List bodies identical line for line. Heading differs: ops 17 "Grand Game Stance" vs guide 5 "The Soul Pact: Active vs. Passive Mode" (contradicts ops 116 "moved verbatim"). Only ops has Summary, Purpose, intro, Tone, Source References. Cross-references differ (guide 100 "operations, key members, lore overview"; ops 121 "identity, tenets, key members")."
> — consistency-pilot-pages.md:41

> "30 SHARED DEFECTS (both copies): Asmodean Shrine areas run 1,2,4,5,6,7,8 (no Area 3; roster lists none) (ops 39-55; guide 27-43); "Founders' Day Clock ... 1-2 days / 3-5 days" undefined (ops 57,74); ops line 85 calls escalation "binary" under a four-tier table (nit)."
> — consistency-pilot-pages.md:42

Current status of item 29 and item 30:
- The guide heading is now "## Grand Game Stance" (`campaign/guides/factions/11-cassalanters.md:5`), not "The Soul Pact: Active vs. Passive Mode". The heading drift is fixed.
- The cross-reference drift is still there: guide line 102 and pilot line 122 differ (see (c)).
- The Founders' Day Clock definition is present in both copies (guide line 47, pilot line 58). The Area 3 note is present in both (guide line 41, pilot line 52).
- The word "binary" no longer appears in the pilot file, and the guide page does not contain it.

> "24 ERROR (cross-page): line 73 "not yet actively pursuing the Stone" (era 61; villains/cassalanters.md:39) vs ops 19 "the family needs the Stone", ops 23 Seffia's team joins the Xanathar's Lair Eye heist, seffia:34 Victoro sent her "to retrieve the Stone"; line 73 also says the family "hold one Eye" while Seffia's ritual found it "in the Brandath Crypt": clarify which Eye."
> — docs/plans/setting-compendium-research-notes/consistency-pilot-pages.md:34

This is a content issue in the verbatim operations text (guide lines 7, 22; pilot lines 18, 33). The move carries it along unchanged.

---

## (c) Pilot versus guide page 11

Files compared: pilot `campaign/setting/faction-operations/10-cassalanters.md` and guide `campaign/guides/factions/11-cassalanters.md`.

**Pilot front matter (pilot lines 1–15)**
> L1: "# The Cassalanters"
> L3: "> Structuring draft."
> L5: "> [!gamemaster]**Gamemaster's Summary**"
> L7: "> - **Page type:** GM-only operations page for a villain faction. It holds the faction's Grand Game stance, response teams, outposts, escalation behavior and revelation list. The faction's lore lives on the **Cassalanters** organization page."
> L8: "> - **Campaign role:** Villain faction; the Cassalanters shift between a passive and a hostile posture depending on whether the party agreed to help them."
> L9: "> - **Used in play:** Between sessions, when the GM checks how the family answers the party's actions. At the table, when the party hits the Asmodean Shrine or the Converted Windmill."
> L10: "> - **Featured in:** **Fireball!**, **Faction Outposts**, **Cassalanter Villa**"
> L12: "**Purpose:** Lets the GM run the Cassalanters as a reactive faction: which posture they take, which team they send, what each outpost holds and what the family does as the party pushes."
> L14: "Game mechanics for running the Cassalanters as a villain faction. For who they are, see the **Cassalanters** organization page."
> — campaign/setting/faction-operations/10-cassalanters.md:1–14

Guide lines 1 and 3 read the same: "# The Cassalanters" (L1) and "Game mechanics for running the Cassalanters as a villain faction. For who they are, see the **Cassalanters** organization page." (L3). The guide has no front matter before its first H2.

**Section-by-section comparison**

| Pilot line | Pilot element | Guide line | Difference |
|---|---|---|---|
| 1 | `# The Cassalanters` | 1 | identical |
| 3 | `> Structuring draft.` | — | added by pilot |
| 5–10 | GM summary callout, 4 bullets (L7–L10) | — | added by pilot |
| 12 | `**Purpose:**` line | — | added by pilot |
| 14 | lead-in sentence | 3 | identical wording, moved below Purpose |
| 16 | `## Grand Game Stance` | 5 | identical heading; 3 paragraphs (pilot 18/20/22 = guide 7/9/11) |
| 24 | `## Response Teams` | 13 | identical; 3 paragraphs (pilot 26/28/30 = guide 15/17/19) |
| 32 | `## Outposts` | 21 | identical |
| 34 | `### Asmodean Shrine — Encounter-Plus (North Ward, Aveen Street)` | 23 | identical heading and body |
| 60 | `### Converted Windmill — Mini-Heist (Southern Ward, Coachlamp Lane)` | 49 | identical heading and body |
| 77 | `## Escalation` | 66 | identical table (pilot 79–84 = guide 68–73) and paragraph (pilot 86 = guide 75) |
| 88 | `## Revelation List` | 77 | identical (pilot 90–109 = guide 79–98) |
| 111 | `**Tone:**` | — | added by pilot |
| 113 | `---` | — | added by pilot |
| 115 | `## Source References` (2 bullets, pilot 117–118) | — | added by pilot |
| 120 | `## Cross-References` (6 bullets, pilot 122–127) | 100 (6 bullets, 102–107) | one bullet differs (below) |

The body is offset by exactly 11 lines. Guide line 5 is pilot line 16, guide 23 is pilot 34, guide 66 is pilot 77, and guide 98 is pilot 109. The body text is therefore the same length in both files. I checked the text by reading, not by diff.

**The one differing bullet**
> pilot 122: "- **Cassalanters** organization page: identity, tenets, key members, lore overview"
> guide 102: "- **Cassalanters** organization page: operations, key members, lore overview"
> — pilot:122 and guide:102

The other five cross-reference bullets are identical: "**Running the Villains** (GM Guide): Grand Game overview, villain escalation framework", "**The Grand Game in Play** (GM Guide): between-sessions faction procedure", "**Factions** guide overview", "**Cassalanters** villain page (Setting: Villains)", and the Notable Figures list.

**Pilot source-reference lines**
> "- `campaign/guides/factions/11-cassalanters.md`: every section below the Gamemaster's Summary, moved verbatim (Session 47 consistency fixes were applied identically to both copies: the Grand Game Stance heading and deadline sentence, the Area 3 note, the Founders' Day Clock definition and the escalation wording)"
> — campaign/setting/faction-operations/10-cassalanters.md:117

> "- `campaign/setting/organizations/10-cassalanters.md`: the "Featured in" line and the lore the summary points to"
> — campaign/setting/faction-operations/10-cassalanters.md:118

Line 117 points at a file that will be deleted by the move. See Decision D8.

**Section order the pilot used (exact)**
1. H1 `# The Cassalanters` (L1)
2. `> Structuring draft.` (L3)
3. GM summary callout, `> [!gamemaster]**Gamemaster's Summary**` (L5–L10)
4. `**Purpose:**` (L12)
5. Unlabelled lead-in sentence (L14)
6. `## Grand Game Stance` (L16)
7. `## Response Teams` (L24)
8. `## Outposts` (L32), with `### Asmodean Shrine` (L34) and `### Converted Windmill` (L60)
9. `## Escalation` (L77)
10. `## Revelation List` (L88)
11. `**Tone:**` (L111)
12. `---` (L113)
13. `## Source References` (L115)
14. `## Cross-References` (L120)

Not present, because the page is a villain page: Quest Hooks, First Meeting, Renown & Ranks, Missions. No Draft Notes and no Overview.

The plan's order (`setting-compendium-rebuild-plan.md:62`) is Gamemaster's Summary, Grand Game Stance, Quest Hooks, First Meeting, Renown & Ranks, Missions, Response Teams, Outposts, Escalation, Revelation List. The pilot's H2 order is a subsequence of it.

**GM callout syntax**
The plan and the pilot brief write the GM callout as `> **[GM]**` with `#### Gamemaster's Summary` (plan line 40; brief lines 18–20). The pilot used `> [!gamemaster]**Gamemaster's Summary**` (pilot line 5). The rebuilt `the-grand-game.md` uses the pilot's form:
> "> [!gamemaster]**Gamemaster's Summary**"
> — campaign/setting/the-grand-game/the-grand-game.md:5

CLAUDE.md line 188 also describes the Notable Figures GM box in the `[!gamemaster]` form. See Decision D3.

---

## (d) Guide pages 02–11: headings, line numbers and bullet counts

Every page's H2 names match the plan's unified names exactly. No H2 needs renaming. The sections of pages 02–08 are already in the plan's order. Pages 09–11 are also in order.

**02-harpers.md** (86 lines) — H1 L1 `# The Harpers`
- L5 `## Grand Game Stance`: 6 bullets (L10–12 and L15–17); bold lead-ins at L9 and L14; warning callout L21–22; paragraphs L7, L19.
- L24 `## Quest Hooks`: table, 6 rows (L28–33).
- L35 `## First Meeting`: 0 bullets; paragraphs L37, L39.
- L41 `## Renown & Ranks`
  - L43 `### Earning Renown`: 6 bullets (L47–52).
  - L54 `### Harper Ranks & Benefits`: table, 5 rows (L58–62).
- L64 `## Missions`: table, 6 rows (L68–73).
- L77 `## Cross-References`: 7 bullets (L79–85).

**03-lords-alliance.md** (108 lines) — H1 L1 `# The Lords' Alliance`
- L5 `## Grand Game Stance`: 6 bullets (L16–18 and L21–23); bold lead-ins L15, L20.
- L25 `## Quest Hooks`: table, 7 rows (L29–35).
- L37 `## First Meeting`: 0 bullets; paragraphs L39, L41, L43, L45.
- L47 `## Renown & Ranks`
  - L49 `### Earning Renown`: 6 bullets (L53–58).
  - L60 `### Lords' Alliance Ranks & Benefits`: table, 5 rows (L66–70).
  - L72 `### Suspension and Dismissal`: 0 bullets; paragraphs L74, L76, L78. This H3 sits inside Renown & Ranks.
- L80 `## Missions`: table, 6 rows (L86–91); paragraphs L93, L95, L97.
- L99 `## Cross-References`: 7 bullets (L101–107).

**04-emerald-enclave.md** (93 lines) — H1 L1 `# The Emerald Enclave`
- L5 `## Grand Game Stance`: 6 bullets (L16–18 and L21–23); lead-ins L15, L20.
- L25 `## Quest Hooks`: table, 5 rows (L29–33).
- L35 `## First Meeting`: 0 bullets; paragraphs L37, L39, L41, L43.
- L45 `## Renown & Ranks`
  - L47 `### Earning Renown`: 5 bullets (L49–53).
  - L55 `### Emerald Enclave Ranks & Benefits`: table, 5 rows (L61–65).
- L67 `## Missions`: table, 6 rows (L73–78); paragraphs L80, L82.
- L84 `## Cross-References`: 7 bullets (L86–92).

**05-order-of-the-gauntlet.md** (96 lines) — H1 L1 `# The Order of the Gauntlet`
- L5 `## Grand Game Stance`: 6 bullets (L16–18 and L21–23); lead-ins L15, L20.
- L25 `## Quest Hooks`: table, 5 rows (L29–33).
- L35 `## First Meeting`: 0 bullets; paragraphs L37, L39, L41.
- L43 `## Renown & Ranks`
  - L45 `### Earning Renown`: 6 bullets (L49–54); paragraph L56 ("Quietly Reassigned").
  - L58 `### Order of the Gauntlet Ranks & Benefits`: table, 5 rows (L64–68).
- L70 `## Missions`: table, 6 rows (L76–81); paragraphs L83, L85.
- L87 `## Cross-References`: 7 bullets (L89–95).

**06-force-grey.md** (90 lines) — H1 L1 `# Force Grey`
- L5 `## Grand Game Stance`: 6 bullets (L14–16 and L19–21); paragraphs L7, L9, L11, L23; lead-ins L13, L18.
- L25 `## Quest Hooks`: table, 5 rows (L29–33).
- L35 `## First Meeting`: 0 bullets; paragraphs L37, L39.
- L41 `## Renown & Ranks`
  - L43 `### Earning Renown`: 6 bullets (L45–50).
  - L52 `### Force Grey Ranks & Benefits`: table, 5 rows (L58–62).
- L64 `## Missions`: table, 6 rows (L70–75); paragraphs L77, L79.
- L81 `## Cross-References`: 7 bullets (L83–89).

**07-doom-raiders.md** (86 lines) — H1 L1 `# The Zhentarim (Doom Raiders)`
- L5 `## Grand Game Stance`: 6 bullets (L14–16 and L19–21); paragraphs L7, L9, L11, L23; lead-ins L13, L18.
- L25 `## Quest Hooks`: table, 5 rows (L29–33).
- L35 `## First Meeting`: 0 bullets; paragraphs L37, L39.
- L41 `## Renown & Ranks`
  - L43 `### Earning Renown`: 6 bullets (L45–50).
  - L52 `### Doom Raiders Ranks & Benefits`: table, 5 rows (L56–60).
- L62 `## Missions`: table, 6 rows (L66–71); paragraph L73 (arrest, two links); paragraph L75.
- L77 `## Cross-References`: 7 bullets (L79–85).

**08-bregan-daerthe.md** (156 lines) — H1 L1 `# Bregan D'aerthe`
- L5 `## Grand Game Stance`: 6 bullets (L14–16 and L19–21); paragraphs L7, L9, L11, L23; lead-ins L13, L18.
- L25 `## Quest Hooks`: table, 5 rows (L29–33).
- L35 `## First Meeting`: 0 bullets; paragraph L37; italic link line L39.
- L41 `## Renown & Ranks`
  - L43 `### Earning Renown`: 6 bullets (L45–50).
  - L52 `### Bregan D'aerthe Ranks & Benefits`: table, 5 rows (L56–60).
- L62 `## Missions`: table, 6 rows (L66–71); paragraph L73.
- L75 `## Response Teams`: 0 bullets; paragraphs L77, L79.
- L81 `## Outposts`
  - L83 `### Fenerus Stormcastle's House — Encounter-Plus (Trades Ward, Quill Alley)`: 5 bullets (L89–93); paragraphs L85, L87, L95; roster L97; escalation L99.
  - L101 `### Seven Masks Theater — Mini-Heist (Dock Ward)`: 0 bullets; L103 italic; L105, L107 (Area P6), L109, L111 (roster), L113 (escalation).
- L115 `## Escalation`: table, 4 rows (L119–122); paragraph L124.
- L126 `## Revelation List`: 12 bullets in three bold-named entries: L128 with 4 bullets (L129–132); L134 with 4 bullets (L135–138); L140 with 4 bullets (L141–144). No intro line.
- L146 `## Cross-References`: 8 bullets (L148–155).

**09-xanathars-guild.md** (113 lines) — H1 L1 `# Xanathar's Guild`. No Grand Game Stance, Quest Hooks, First Meeting, Renown & Ranks or Missions.
- L5 `## Response Teams`: 0 bullets; paragraphs L7, L9, L11, L13.
- L15 `## Outposts`
  - L17 `### Terasse Estate — Mini-Heist (Castle Ward, Elsambul's Lane)`: 0 bullets; paragraphs and labelled entries L19–33.
  - L37 `### Grinda Garloth's — Encounter-Plus (Dock Ward, Mistshore)`: 0 bullets; L39–49.
  - L51 `### Orb Confectioners / Xanathar Sewer Hideout — Encounter-Plus (Southern Ward, Rising Ride)`: 0 bullets; L53–63.
- L65 `## Escalation`: table, 4 rows (L71–74); paragraph L67; warning callout L76–77 ("Sylgar Overrides All Tiers").
- L79 `## Revelation List`: intro L81; 14 bullets in four bold-named entries: L83 with 3 (L84–86); L88 with 3 (L89–91); L93 with 3 (L94–96); L98 with 5 (L99–103).
- L105 `## Cross-References`: 6 bullets (L107–112).

**10-manshoons-zhentarim.md** (87 lines) — H1 L1 `# Manshoon's Zhentarim`. No Grand Game Stance, Quest Hooks, First Meeting, Renown & Ranks or Missions.
- L5 `## Response Teams`: 0 bullets; paragraphs L7, L9; three roster lines at L11–13 with no blank lines between them, so Markdown renders them as one paragraph.
- L15 `## Outposts`
  - L17 `### Interrogation House — Encounter-Plus (North Ward, Brindul Alley)`: 0 bullets.
  - L33 `### Yellowspire — Mini-Heist (Castle Ward)`: 0 bullets.
- L47 `## Escalation`: table, 4 rows (L51–54); paragraph L56.
- L58 `## Revelation List`: intro L60; 12 bullets in three bold-named entries: L62 with 3 (L63–65); L67 with 4 (L68–71); L73 with 5 (L74–78).
- L80 `## Cross-References`: 5 bullets (L82–86).

**11-cassalanters.md** (108 lines) — H1 L1 `# The Cassalanters`. No Quest Hooks, First Meeting, Renown & Ranks or Missions.
- L5 `## Grand Game Stance`: 0 bullets; paragraphs L7, L9, L11.
- L13 `## Response Teams`: 0 bullets; paragraphs L15, L17 (Seffia's team), L19 (Willifort's team).
- L21 `## Outposts`
  - L23 `### Asmodean Shrine — Encounter-Plus (North Ward, Aveen Street)`: 0 bullets; paragraphs L25–47.
  - L49 `### Converted Windmill — Mini-Heist (Southern Ward, Coachlamp Lane)`: 2 bullets (L59, L60); paragraphs and roster L51–64.
- L66 `## Escalation`: table, 4 rows (L70–73); paragraph L75.
- L77 `## Revelation List`: intro L79; 13 bullets in three bold-named entries: L81 with 4 (L82–85); L87 with 4 (L88–91); L93 with 5 (L94–98).
- L100 `## Cross-References`: 6 bullets (L102–107).

**01-overview.md** (57 lines) — H1 L1 `# Factions`
- L5 `## How Renown Works`: 0 bullets; paragraphs L7, L9, L11, L13.
- L15 `## Running Faction Missions`: 0 bullets; paragraphs L17, L19, L21, L23, L25.
- L27 `## Pages in This Guide`
  - L29 `### Player Factions`: table, 7 rows (L33–39).
  - L41 `### Villain Factions`: table, 3 rows (L45–47).
- L49 `## Cross-References`: 6 bullets (L51–56).

**Heading and count summary**
- Pages 02–08 each have the same H2 names as the plan. Their section order matches the plan's unified order.
- Pages 09–11 have only the villain sections (Response Teams, Outposts, Escalation, Revelation List) plus Cross-References.
- Bregan D'aerthe (08) is the only page with both player and villain sections, and it is already in plan order: Missions (L62) before Response Teams (L75).
- The Stance section is missing from pages 09 and 10 (see Decision D4).
- Every guide's H1 is identical to the H1 of its organization page (see (e) and Decision D7).

---

## (e) Page numbering

Organization pages (`campaign/setting/organizations/`), confirmed by Glob:
01-harpers.md, 02-lords-alliance.md, 03-emerald-enclave.md, 04-order-of-the-gauntlet.md, 05-force-grey.md, 06-doom-raiders.md, 07-bregan-daerthe.md, 08-xanathars-guild.md, 09-manshoons-zhentarim.md, 10-cassalanters.md.

Guide pages (`campaign/guides/factions/`), confirmed by Glob:
01-overview.md, 02-harpers.md through 11-cassalanters.md (each with a matching slug).

| Guide file | Org file | Slug matches | Proposed faction-operations file |
|---|---|---|---|
| 01-overview.md | none | — | no slot in the 10-page plan; see Decision D1 |
| 02-harpers.md | 01-harpers.md | yes | 01-harpers.md |
| 03-lords-alliance.md | 02-lords-alliance.md | yes | 02-lords-alliance.md |
| 04-emerald-enclave.md | 03-emerald-enclave.md | yes | 03-emerald-enclave.md |
| 05-order-of-the-gauntlet.md | 04-order-of-the-gauntlet.md | yes | 04-order-of-the-gauntlet.md |
| 06-force-grey.md | 05-force-grey.md | yes | 05-force-grey.md |
| 07-doom-raiders.md | 06-doom-raiders.md | yes | 06-doom-raiders.md |
| 08-bregan-daerthe.md | 07-bregan-daerthe.md | yes | 07-bregan-daerthe.md |
| 09-xanathars-guild.md | 08-xanathars-guild.md | yes | 08-xanathars-guild.md |
| 10-manshoons-zhentarim.md | 09-manshoons-zhentarim.md | yes | 09-manshoons-zhentarim.md |
| 11-cassalanters.md | 10-cassalanters.md | yes | 10-cassalanters.md (pilot already here) |

The rule is that the faction-operations number equals the guide number minus one, which equals the organization number. The pilot already uses 10. `campaign/setting/faction-operations/` currently holds only `10-cassalanters.md` (Glob).

---

## (f) Guide page 01-overview.md compared with other files

**What 01-overview contains** (quoted in full; these are the lines that carry rules)

> "Renown is tracked as a separate numerical score for each faction a character belongs to. A character who joins both the Harpers and the Doom Raiders has two independent scores, each starting at 0. Ranks and benefits are per-faction; reaching Renown 10 with the Harpers does nothing for a character's Doom Raiders standing."
> — campaign/guides/factions/01-overview.md:7

> "**Calibration.** A character who completes all six faction missions and earns available Grand Game bonuses will reach approximately Renown 30–35 by the late heist quests, enough for the Renown 25 rank in their primary faction and Renown 10–15 in a secondary one. Build late-game faction payoffs with that range in mind."
> — campaign/guides/factions/01-overview.md:9

> "**Lords' Alliance discipline.** "Refusing or failing a mission without compelling reason" means a mission explicitly assigned by Jalester, not missions the character chose not to pursue independently. A character who declines a mission because it conflicts with a position they've maintained consistently throughout the campaign has a compelling reason. Someone who repeatedly accepts and then abandons assignments doesn't. Formal suspension removes mission access until Jalester reinstates them, usually after a demonstrated act of service to the city. Dismissal is permanent and removes all ranks and benefits, though not the Renown score itself, which becomes inert."
> — campaign/guides/factions/01-overview.md:11

> "**Tracking.** Keep the per-faction Renown score on the session notes alongside the character sheet. Renown changes take effect immediately; a character who earns enough for a new rank gains its benefits before the next scene."
> — campaign/guides/factions/01-overview.md:13

> "Each faction operates as an ongoing relationship. Contacts push for information, react to the party's choices in the Grand Game, and bring their own agendas to bear as events escalate. Faction missions are structured as mini-arcs: each has an investigation phase, a complication, and at least two resolution paths. No single skill check determines success. Full write-ups are in the **Faction Events** quest journals; each faction's folder holds a First Meeting event, missions (m01–m06), standalone events (s0N) that fire on specific triggers, and rank-up events (r03, r10, r25, r50). They award no Milestone Points."
> — campaign/guides/factions/01-overview.md:17

> "**A note on the Zhentarim.** Two Zhentarim cells operate in Waterdeep. Davil Starsong's **Doom Raiders** are the player-joinable faction covered in the **Organizations** pages. Manshoon's faction is the villain cell, which the faction-mission journals call **the Splinter**. They are hostile to the Doom Raiders and to the party."
> — campaign/guides/factions/01-overview.md:19

> "**Mission delivery.** Unless noted, missions arrive via the faction's preferred method: paper birds for Harpers, flying snakes for Doom Raiders, animal messengers for the Enclave, *Sending* spells for Force Grey."
> — campaign/guides/factions/01-overview.md:21

> "**Failure.** If a mission ends in failure, the situation changes; it doesn't simply reset. Targets escape, informants are compromised, and rival factions benefit. Each mission's Aftermath section describes exactly what changes when things go wrong."
> — campaign/guides/factions/01-overview.md:23

> "**Renown.** Missions are calibrated by tier: Level 2–3 missions pay 2 Renown, Level 4–5 pay 3, Level 6–7 pay 4. Each mission lists specific bonus conditions worth +1 each; award only those, not a general judgment call. A clean failure forfeits the award but costs nothing; a mission that causes collateral damage costs −1. Supplementary renown from upholding faction values (+1) and achieving major faction goals (+2) stacks on top; a dedicated member should reach Renown 30+ by the late heist quests."
> — campaign/guides/factions/01-overview.md:25

Also in 01-overview: the L3 scope statement, the "Pages in This Guide" tables (L27–47) and the cross-reference bullets (L51–56).
> "Each faction page covers how that faction recruits, what it offers members and demands in return, how its missions run, and where it stands in the Grand Game. History, internal structure, politics, and the lore a member would absorb over time live in the **Organizations** pages in the Setting. The mechanics here stand alone; the Organizations pages deepen them."
> — campaign/guides/factions/01-overview.md:3

**Comparison with the other files**

Player-facing overview (`campaign/guides/gm-guide/player-factions-overview.md`) and the Players' Guide (`campaign/guides/players-guide/faction-affiliations.md`):
> "- **Earning Renown.** You earn Renown by completing faction missions and by taking the specific Grand Game actions each faction lists under its own Earning Renown section. No other source awards Renown; general good roleplay earns none on its own."
> — campaign/guides/gm-guide/player-factions-overview.md:24 (identical text at campaign/guides/players-guide/faction-affiliations.md:24)

> "- **Losing Renown.** Serious offenses cost 2 Renown each: betraying a mission, harming faction members, or working against the faction's interests. Renown never falls below 0. The Lords' Alliance is the exception: it never lowers Renown and suspends or dismisses a member instead."
> — campaign/guides/gm-guide/player-factions-overview.md:25 (identical at faction-affiliations.md:25)

> "- **Lords' Alliance discipline.** The Lords' Alliance is the only faction that enforces consequences for refusing an assigned mission, or abandoning it past its stated deadline, without compelling reason. An honest attempt that fails costs nothing: formal suspension until reinstated, or outright dismissal."
> — campaign/guides/gm-guide/player-factions-overview.md:26 (identical at faction-affiliations.md:26)

The Renown section (player-factions-overview.md:20–29) and the same section in faction-affiliations.md:20–29 are identical wording. Neither has the 01-overview rules listed in "unique" below.

> "## Running the Player Factions"
> "Each of the six standard factions assigns a named contact who handles recruitment and mission delivery. Full mission tables and First Meeting scenes are in the **Factions** guide pages. Full profiles are in the **Organizations** pages. The table below adds what the player version withholds: contacts and the faction's actual agenda."
> — campaign/guides/gm-guide/player-factions-overview.md:154

The Campaign's `the-grand-game/` folder (`campaign/setting/the-grand-game/the-grand-game.md` and `what-each-faction-knows-at-start.md`) has no Renown, ranks, calibration, tracking, mission-running or delivery rules. Its only overlap with 01-overview is the pointer to the guide pages:
> "> - Response teams, outposts, escalation rows and revelation lists live in the Factions Guide page for each faction. The between-sessions routine lives in **The Grand Game in Play** and the reference tables in **Running the Villains**, both in the GM Guide. Who each faction is lives in the Organizations pages."
> — campaign/setting/the-grand-game/the-grand-game.md:10

**What 01-overview contains that exists nowhere else** (checked by searching `campaign/` for each distinctive phrase)
- L7, separate per-faction Renown score and per-faction ranks. The phrase "Renown is tracked as" appears only at 01-overview.md:7. The player overview has per-faction starting Renown (L22) but not the separate-score rule.
- L9, calibration to Renown 30–35 and the 10–15 secondary range. "30–35" appears only at 01-overview.md:9.
- L11, the definition of "compelling reason" for Lords' Alliance discipline, with the accept-then-abandon example. The phrase "compelling reason" appears in the player and GM overviews without this definition, and in the s01 design notes.
- L13, tracking rule and "take effect immediately". Only at 01-overview.md:13.
- L17, the mini-arc rule ("at least two resolution paths. No single skill check determines success."). Only at 01-overview.md:17. The same rule exists as a project rule at CLAUDE.md:313 (see below).
- L19, the Zhentarim note naming "the Splinter" as the faction-mission journals' term. The phrase "faction-mission journals call" appears only at 01-overview.md:19. The player overview's Zhentarim warning (player-factions-overview.md:17–18) does not use that name.
- L21, the "Unless noted" delivery rule. The per-faction delivery methods also appear in each organization page's "Mission delivery" line (for example `campaign/setting/organizations/01-harpers.md:7`, `05-force-grey.md:7`, `06-doom-raiders.md:7`), so the methods are not unique, but the rule is.
- L23, the failure rule ("it doesn't simply reset") and the "Aftermath section" claim. The phrase "doesn't simply reset" appears only at 01-overview.md:23. The Aftermath section exists in the Harpers faction-event journals (20 files contain a `^#+ .*Aftermath` heading), so the claim is supported there.
- L25, the supplementary renown (+1 for faction values, +2 for major goals), the −1 collateral-damage rule, and "Renown 30+". "Supplementary renown" and "collateral damage costs" appear only at 01-overview.md:25.

CLAUDE.md supports some of the 01-overview rules, so they are not unique to the campaign's guides:
> "**Mini-arc mission structure:** Every faction mission follows: Hook → Background (DM-only context) → Act 1 → Act 2 → Act 3 → Renown Opportunities → Aftermath. Do not skip or reorder sections."
> — CLAUDE.md:315

> "**Renown tier calibration:** L2–3 missions award 2 base renown; L4–5 missions award 3 base; L6–7 missions award 4 base. Bonus +1 renown is granted only for explicitly listed conditions in the Renown Opportunities section — not for general good play."
> — CLAUDE.md:317

> "Faction Missions award no Milestone Points — the main quest ladder (Finding Floon through Vault of Dragons) covers the full 1→8 progression without them; faction rewards are gold, renown, items, and cross-quest intel."
> — CLAUDE.md:325

**Conflicts between 01-overview and the player-facing files**
1. Supplementary renown. 01-overview.md:25 says "Supplementary renown from upholding faction values (+1) and achieving major faction goals (+2) stacks on top." The player overview says "No other source awards Renown; general good roleplay earns none on its own." (player-factions-overview.md:24; faction-affiliations.md:24). The two rules conflict unless "supplementary" renown is a Grand Game action.
2. Losing Renown. 01-overview.md:25 says "a mission that causes collateral damage costs −1." The player overview says "Serious offenses cost 2 Renown each: betraying a mission, harming faction members, or working against the faction's interests." (player-factions-overview.md:25). The player overview has no −1 collateral rule, and 01 has no −2 rule.
3. Honest failure. player-factions-overview.md:26 and faction-affiliations.md:26 say "An honest attempt that fails costs nothing: formal suspension until reinstated, or outright dismissal." The Lords' Alliance page says: "Honest failure costs nothing. A target who escapes, a failed roll or a beaten party does not fire the visit, and neither does a reason that fits the table of excuses in **Suspension and Dismissal**." (campaign/guides/factions/03-lords-alliance.md:76). The player sentence reads as if an honest failure leads to suspension. The Lords' page does not support that reading.
4. Reinstatement detail. 01-overview.md:11 says suspension ends "usually after a demonstrated act of service to the city." campaign/guides/factions/03-lords-alliance.md:78 says: "Reinstatement has three routes: verified intelligence, a short errand that Jalester names, or Laeral's word after **Escalation to the Open Lord**." The wording differs; the two are not identical.

**Disposition options for 01-overview (no recommendation)**
- Keep it as a separate faction-operations page. This breaks the "10 + 10" count rule at plan line 106.
- Move its rules into a hub page in `setting/faction-operations/`. Plan line 55 has a Hub row for this, but no faction-operations hub exists in the plan.
- Fold its unique rules into the GM Guide's `player-factions-overview.md` Renown section. That section (lines 20–29) does not contain these rules today.
- Delete it and keep only the CLAUDE.md rules. This loses the unique content listed above.

---

## (g) Inbound references

Searches covered `campaign/`, `.claude/`, `CLAUDE.md`, `scripts/`, plus counts for `docs/`, root handoffs and `sources/`. Patterns: `guides/factions`, `Factions Guide`, `Factions guide`, `faction guide` (any case, with `**` allowed between the words), the guide filenames, the guide H1 titles, and `faction-operations`. Counts are matched lines. The pattern `faction operations` also matches "inter-faction operations", so those counts are high.

### G1. Path references to `guides/factions` in `campaign/`

Gazetteer:
- `campaign/gazetteer/waterdeep/dock-ward.md:258` — "`campaign/guides/factions/08-bregan-daerthe.md`"
- `campaign/gazetteer/waterdeep/north-ward.md:227` — "`campaign/guides/factions/10-manshoons-zhentarim.md`", "`campaign/guides/factions/11-cassalanters.md`"
- `campaign/gazetteer/waterdeep/southern-ward.md:209` — "`campaign/guides/factions/09-xanathars-guild.md`"
- `campaign/gazetteer/waterdeep/southern-ward.md:242` — "`guides/factions/10-manshoons-zhentarim.md:73`"
- `campaign/gazetteer/waterdeep/southern-ward.md:249` — "`guides/factions/09-xanathars-guild.md:51,`"
- `campaign/gazetteer/waterdeep/southern-ward.md:263` — "`guides/factions/10-manshoons-zhentarim.md:73`"
- `campaign/gazetteer/waterdeep/trades-ward.md:205` — "`campaign/guides/factions/08-bregan-daerthe.md`"
- `campaign/gazetteer/waterdeep/trades-ward.md:243` — "`campaign/guides/factions/10-manshoons-zhentarim.md:73`"
- `campaign/gazetteer/waterdeep/trades-ward.md:248` — "`campaign/guides/factions/08-bregan-daerthe.md:101`"
- `campaign/gazetteer/waterdeep/trades-ward.md:249` — "`campaign/guides/factions/08-bregan-daerthe.md:85`"
- `campaign/gazetteer/waterdeep/trades-ward.md:253` — "`campaign/guides/factions/07-doom-raiders.md:57`"

Guide-to-guide relative links:
- `campaign/guides/gm-guide/grand-game-in-play.md:100–103` — "(../factions/08-bregan-daerthe.md)", "(../factions/09-xanathars-guild.md)", "(../factions/10-manshoons-zhentarim.md)", "(../factions/11-cassalanters.md)"
- `campaign/guides/gm-guide/player-factions-overview.md:196` — "see [Factions: Overview](../factions/01-overview.md)."
- `campaign/guides/gm-guide/player-factions-overview.md:205` — "[Factions Guide: Overview](../factions/01-overview.md)"
- `campaign/guides/gm-guide/structural-rules.md:26` — "([Bregan D'aerthe](../factions/08-bregan-daerthe.md), [Xanathar's Guild](../factions/09-xanathars-guild.md), [Manshoon's Zhentarim](../factions/10-manshoons-zhentarim.md), [Cassalanters](../factions/11-cassalanters.md))"
- `campaign/guides/gm-guide/structural-rules.md:90` — same four links
- `campaign/guides/gm-guide/structural-rules.md:119–122` — "../factions/08-…", "09-…", "10-…", "11-…" (one per line)

Quest journals and design notes:
- `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/design-notes.md:37` — "`campaign/guides/factions/08-bregan-daerthe.md`"
- `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/design-notes.md:23` — "`campaign/guides/factions/08-bregan-daerthe.md:14`"
- `campaign/quests/faction-events/bregan-daerthe/s04-contact-severed/design-notes.md:48` — "`campaign/guides/factions/08-bregan-daerthe.md`"
- `campaign/quests/faction-events/force-grey/00-first-meeting/design-notes.md:28` — "`campaign/guides/factions/06-force-grey.md`"
- `campaign/quests/faction-events/force-grey/m01-consulting-hlam/design-notes.md:28` — "`campaign/guides/factions/06-force-grey.md:7`"
- `campaign/quests/faction-events/force-grey/r03-junior-griffon/design-notes.md:20` — "`campaign/guides/factions/06-force-grey.md:55`"
- `campaign/quests/faction-events/force-grey/r25-force-grey/design-notes.md:26` — "`campaign/guides/factions/06-force-grey.md:57`"
- `campaign/quests/faction-events/lords-alliance/r50-lioncrown/design-notes.md:26` — "`campaign/guides/factions/03-lords-alliance.md:59`"
- `campaign/quests/faction-events/lords-alliance/s02-escalation-to-the-open-lord/design-notes.md:24` — "`campaign/guides/factions/03-lords-alliance.md`"
- `campaign/quests/faction-events/force-grey/s01-the-full-picture/design-notes.md:20` — "`06-force-grey`" (inside "factions guide, `06-force-grey")

Settings, villains, organizations and structure:
- `campaign/setting/deities/bane.md:131` — "`guides/factions/10-manshoons-zhentarim.md:33`", "`guides/factions/07-doom-raiders.md:31`"
- `campaign/setting/deities/bane.md:140` — "(`campaign/guides/factions/10-manshoo…`" (the match was cut by my pattern; the full path is `campaign/guides/factions/10-manshoons-zhentarim.md` if the match is complete, but I did not re-check the line)
- `campaign/setting/deities/helm.md:93` — "`campaign/guides/factions/05-order-of-the-gauntlet.md`"
- `campaign/setting/deities/maglubiyet.md:82` — "`guides/factions/09-xanathars-guild.md:13`"
- `campaign/setting/deities/maglubiyet.md:104` — "`guides/factions/09-xanathars-guild.md`"
- `campaign/setting/deities/tyr.md:97` — "`campaign/guides/factions/05-order-of-the-gauntlet.md`"
- `campaign/setting/deities/umberlee.md:101` — "`campaign/guides/factions/06-force-grey.md`"
- `campaign/setting/faction-operations/10-cassalanters.md:117` — "`campaign/guides/factions/11-cassalanters.md`"
- `campaign/setting/geography/city-of-the-dead.md:138` — "`guides/factions/11-cassalanters.md:60`"
- `campaign/setting/governance-and-guilds/city-watch.md:102` — "`campaign/guides/factions/03-lords-alliance.md`"
- `campaign/setting/governance-and-guilds/guilds.md:87` — "`campaign/guides/factions/08-bregan-daerthe.md`"
- `campaign/setting/history/03-bregan-daerthes-long-road.md:153` — "`guides/factions/08-bregan-daerthe.md`"
- `campaign/setting/history/04-the-founding-of-chains.md:110` — "`guides/factions/07-doom-raiders.md`"
- `campaign/setting/history/04-the-founding-of-chains.md:149` — "`guides/factions/07-doom-raiders.md`"
- `campaign/setting/history/04-the-founding-of-chains.md:153` — "`guides/factions/10-manshoons-zhentarim.md`"
- `campaign/setting/history/04-the-founding-of-chains.md:156` — "`guides/factions/07-doom-raiders.md`"
- `campaign/setting/history/04-the-founding-of-chains.md:159` — "`guides/factions/10-manshoons-zhentarim.md`", "`guides/factions/07-doom-raiders.md`"
- `campaign/setting/history/06-the-open-lords-fall.md:148` — "`guides/factions/03-lords-alliance.md`"
- `campaign/setting/history/07-a-city-watching-itself.md:97` — "`campaign/guides/factions/03-lords-alliance.md`"
- `campaign/setting/history/07-a-city-watching-itself.md:123` — "`guides/factions/03-lords-alliance.md`"
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:189` — "`guides/factions/02-harpers.md:7`"
- `campaign/setting/lore/vault-of-dragons.md:161` — "`guides/factions/11-cassalanters.md:60`"
- `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:77` — "`campaign/guides/factions/11-cassalanters.md`"
- `campaign/setting/organizations/10-cassalanters.md:118` — "`guides/factions/11-cassalanters.md`" (inside the Conflicts note: "The cross-reference line to the Faction Operations page assumes the guide pages move. Until `guides/factions/11-cassalanters.md` is removed, both copies exist.")
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:60` — "`campaign/guides/factions/07-doom-raiders.md`"
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:94` — "`guides/factions/07-doom-raiders.md:7`"
- `campaign/setting/villains/cassalanters.md:96` — "`campaign/guides/factions/`"
- `campaign/setting/villains/cassalanters.md:117` — "`campaign/guides/factions/03-lords-alliance.md`"
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md` — no path; see G2.

Structure documents (`campaign/structure/`, skipped by the viewer):
- `campaign/structure/arc-e-faction-outposts.md`: "Factions guide page" lines do not hold paths. No path hits.

### G2. "Factions Guide" and "Factions guide" phrase references in `campaign/`

Each entry is `file:line — exact matched text`. Where the same phrase appears on several lines, all are listed.

Guide pages (bold cross-reference "Factions guide overview"):
- `guides/factions/02-harpers.md:81` — "**Factions** guide overview: all player factions, renown system, conflicting loyalties"
- `03-lords-alliance.md:103`, `04-emerald-enclave.md:88`, `05-order-of-the-gauntlet.md:91`, `06-force-grey.md:85`, `07-doom-raiders.md:81`, `08-bregan-daerthe.md:150`, `09-xanathars-guild.md:110`, `10-manshoons-zhentarim.md:84`, `11-cassalanters.md:105` — "**Factions** guide overview"

GM Guide:
- `gm-guide/grand-game-in-play.md:88` — "Factions guide page"
- `gm-guide/player-factions-overview.md:55` — "Factions guide page and the **High Harper** rank event"; `:154` — "Factions** guide pages"; `:167` — "Factions guide page"; `:177` — "Factions guide page"; `:196` — "Factions** guide: see [Factions: Overview]("; `:205` — "Factions Guide: Overview]("; `:207` — "Factions** guide pages: renown, ranks, missions, and First Meeting scenes"
- `gm-guide/running-the-villains.md:78` — "Factions guide page shows where each document is found"; `:84` — "Factions guide pages: response teams, outposts, each faction's escalation"
- `gm-guide/structural-rules.md:26` and `:90` — "Factions guide pages ([Bregan D'aerthe]("

Trollskull Manor:
- `trollskull-manor/09-response-teams-at-the-tavern.md:5` — "Factions guide pages"

Players' Guide: no "Factions Guide" phrase (`faction-affiliations.md` has none).

Quests (Trollskull Alley, Gralhund, faction events):
- `act-i/trollskull-alley/design-notes.md:19` — "Factions** guide pages"
- `act-i/trollskull-alley/ev-04-the-factions-come-calling.md:16` — "Factions** guide pages"; `:98` — "Factions guide (mission unlock)"
- `act-i/trollskull-alley/flowchart.md:81`, `:82` — "Factions** guide pages (missions)"
- `act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:60` — "Factions guide page for roster and tactics"
- `faction-events/bregan-daerthe/00-first-meeting/design-notes.md:7` — "Factions guide and **Trollskull Alley** both state"; `:35` — "Factions guide and **The Factions Come Calling** still call both outcomes"
- `faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:463` — "Factions Guide page and by **Faction Outposts** (unconverted)"
- `faction-events/bregan-daerthe/m01-the-handkerchief-and-the-girl/design-notes.md:29` — "Factions Guide still describe the first mission"
- `faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:90` — "Factions Guide page"
- `faction-events/bregan-daerthe/m03-three-nights/design-notes.md:45` — "Factions Guide and **Coin Pouches** give the second one a note"
- `faction-events/bregan-daerthe/m06-the-dive/design-notes.md:5`, `:58`, `:66` — "Factions Guide", "Factions Guide was never implemented in the Bregan D'aerthe folder", "Factions Guide (line 16) offers the *Scarlet Marpenoth*"
- `faction-events/bregan-daerthe/r03-soldier/design-notes.md:17` — "Factions Guide page"; `ev-01-soldier.md:144`, `:317` — "Factions Guide:", "Factions Guide"
- `faction-events/bregan-daerthe/r10-officer/design-notes.md:14` — "Factions Guide names them"; `:32` — "Factions Guide (the intelligence, Golorr artifact, Nar'l, Faire-cover and"; `ev-01-officer.md:247` — "Factions Guide for retrieving the shipping records from the Faire goes onl"; `:292` — "Factions Guide"
- `faction-events/bregan-daerthe/r25-commander/design-notes.md:33`, `:41`, `:51`, `:63`, `:64`, `:65`(line 51 and 65 use "Factions Guide:"); `ev-01-commander.md:22`, `:350` — "Factions Guide"
- `faction-events/bregan-daerthe/r50-houseless-noble/design-notes.md:5`, `:31`, `:79`; `ev-01-houseless-noble.md:19` — "Factions Guide"
- `faction-events/doom-raiders/00-first-meeting/design-notes.md:19` — "Factions Guide (200 gp at Renown 1)"; `:25` — "Factions Guide still write **Yagra Courteous**"; `ev-01-first-meeting.md:416` — "Factions Guide page, by **Davil's Arrest**"
- `faction-events/doom-raiders/m02-the-poisoned-delivery/design-notes.md:19` — "Factions Guide page, which says Davil has suspected Skeemo"
- `faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:419` — "Factions Guide page"
- `faction-events/doom-raiders/r03-wolf/design-notes.md:7` — "Factions Guide"; `ev-01-wolf.md:150` — "Factions Guide describes and is not awarded here"; `:232` — "Factions Guide, at their own pace"
- `faction-events/doom-raiders/r10-viper/design-notes.md:15` — "Factions Guide \"veteran\" wording"; `ev-01-viper.md:87` — "Factions Guide sets"; `:199` — "Factions Guide"
- `faction-events/doom-raiders/r25-ardragon/design-notes.md:5`, `:17`, `:23` — "Factions Guide reads", "Factions Guide", "Factions Guide says Ziraj's favour"; `ev-01-ardragon.md:301` — "Factions Guide"
- `faction-events/doom-raiders/r50-dread-lord/design-notes.md:17`, `:19` — "Factions Guide does not list", "Factions Guide's Dread Lord row"
- `faction-events/emerald-enclave/00-first-meeting/design-notes.md:24` — "Factions Guide (`04-emerald-enclave"; `ev-01-first-meeting.md:303` — "Factions Guide page;"
- `faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:213` — "Factions Guide, at their own pace"
- `faction-events/emerald-enclave/r10-autumnreaver/design-notes.md:5` — "Factions Guide give Jeryth one casting"; `ev-01-autumnreaver.md:331` — "Factions Guide, at their own pace"
- `faction-events/emerald-enclave/r25-winterstalker/design-notes.md:11` — "Factions Guide gives one casting"; `ev-01-winterstalker.md:18` — "Factions Guide supply the rest"; `:360` — "Factions Guide, at their own pace"
- `faction-events/emerald-enclave/r50-master-of-the-wild/design-notes.md:5`, `:26`; `ev-01-master-of-the-wild.md:383` — "Factions Guide"
- `faction-events/emerald-enclave/s02-the-water-table-stirs/design-notes.md:19` — "Factions Guide gate row should say the same"
- `faction-events/force-grey/00-first-meeting/design-notes.md:21` — "Factions Guide lists Gray Hand benefits without procedures"; `ev-01-first-meeting.md:268` — "Factions Guide page, by **The Factions Come Calling**"
- `faction-events/force-grey/r03-junior-griffon/ev-01-junior-griffon.md:193` — "Factions Guide, at their own pace"
- `faction-events/force-grey/r10-senior-griffon/design-notes.md:5`, `:19`; `ev-01-senior-griffon.md:261` — "Factions Guide give Senior Griffon four things", "Factions Guide, the Players' Guide and the GM Guide all say", "Factions Guide, at their own pace"
- `faction-events/force-grey/r25-force-grey/design-notes.md:19`; `ev-01-force-grey.md:18`, `:285` — "Factions Guide", "Factions Guide before this rank arrives", "Factions Guide, at their own pace"
- `faction-events/force-grey/r50-force-grey-commander/design-notes.md:5`, `:27`; `ev-01-force-grey-commander.md:384` — "Factions Guide give Commander as four veterans", "Factions Guide and Appendix B describe the team", "Factions Guide"
- `faction-events/harpers/00-first-meeting/design-notes.md:17` — "Factions Guide and the earlier drafts do"
- `faction-events/harpers/m03-the-doppelganger-auditions/design-notes.md:5` — "Factions Guide say"
- `faction-events/harpers/r03-harpshadow/design-notes.md:7`, `:11`; `ev-01-harpshadow.md:94`, `:134`, `:236` — "Factions Guide", "Factions Guide adds the three ward contacts", "Factions Guide page", "Factions Guide for their ward", "Factions Guide, at their own pace"
- `faction-events/harpers/r10-brightcandle/design-notes.md:5`; `ev-01-brightcandle.md:250` — "Factions Guide adds a Harper mentor who teaches one persona", "Factions Guide"
- `faction-events/harpers/r25-wise-owl/design-notes.md:5`, `:25`; `ev-01-wise-owl.md:27`, `:277` — "Factions Guide adds informants", "Factions Guide now matches this Event", "Factions Guide"
- `faction-events/harpers/r50-high-harper/design-notes.md:5` — "Factions Guide adds a covert city extraction"
- `faction-events/lords-alliance/00-first-meeting/design-notes.md:13`, `:25`; `ev-01-first-meeting.md:297` — "Factions Guide, which gives it at Renown 3", "Factions Guide", "Factions Guide page, and by every Lords' Alliance faction event"
- `faction-events/lords-alliance/m01-the-long-watch/design-notes.md:5` — "Factions Guide and **Trollskull Alley** still describe this version"
- `faction-events/lords-alliance/m05-fentrees-ledger/design-notes.md:5` — "Factions Guide gives only a one-line summary of the ledger"
- `faction-events/lords-alliance/r03-redknife/design-notes.md:9`; `ev-01-redknife.md:247` — "Factions Guide lists the Watch patrol schedules at Renown 3", "Factions Guide, at their own pace"
- `faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:272` — "Factions Guide, at their own pace"
- `faction-events/lords-alliance/r25-warduke/design-notes.md:26`; `ev-01-warduke.md:426` — "Factions Guide Warduke row says", "Factions Guide, at their own pace"
- `faction-events/lords-alliance/r50-lioncrown/design-notes.md:5` (two matches: "Factions Guide give Lioncrown", "Factions Guide adds three honest answers"); `ev-01-lioncrown.md:394` — "Factions Guide"
- `faction-events/lords-alliance/s01-suspension-and-dismissal/design-notes.md:13` — "Factions Guide line that a clean failure costs nothing"
- `faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:336` — "Factions Guide page"
- `faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/design-notes.md:28` — "Factions Guide row says the trail touches the Grand Game"
- `faction-events/order-of-the-gauntlet/m05-the-shrine-on-aveen-street/design-notes.md:9`, `:25`; `ev-01-the-shrine-on-aveen-street.md:19`, `:230`, `:363`; `overview.md:23` — "Factions Guide stands in the North Ward", "Factions Guide says the shrine is", "Factions Guide", "Factions Guide, and the Event does not require them", "Factions Guide lists them", "Factions Guide"
- `faction-events/order-of-the-gauntlet/m06-the-writ-and-the-weight/design-notes.md:5` — "Factions Guide"
- `faction-events/order-of-the-gauntlet/r03-marcheon/design-notes.md:5`, `:23`; `ev-01-marcheon.md:246` — "Factions Guide and the Players' Guide carry the same three lines", "Factions Guide `05-order-of-the-gauntlet", "Factions Guide"
- `faction-events/order-of-the-gauntlet/r10-whitehawk/ev-01-whitehawk.md:227` — "Factions Guide"
- `faction-events/order-of-the-gauntlet/r25-vindicator/design-notes.md:23`; `ev-01-vindicator.md:251` — "Factions Guide Vindicator row says", "Factions Guide"
- `faction-events/order-of-the-gauntlet/r50-righteous-hand/design-notes.md:5`, `:22`; `ev-01-righteous-hand.md:317` — "Factions Guide give Righteous Hand", "Factions Guide `05-order-of-the-gauntlet", "Factions Guide"
- `faction-events/order-of-the-gauntlet/s01-the-tithe/design-notes.md:5` — "Factions Guide say a member who tithes"
- `faction-events/bregan-daerthe/s01-coin-pouches/design-notes.md:23` — path listed in G1.

Setting:
- `setting/deities/asmodeus.md:108` — "Factions Guide): operations, response teams, revelation list"; `:122` — "Factions Guide)"
- `setting/deities/bane.md:139` — "Factions Guide note and has no page"; `:140` — "Factions Guide note about Shan Chien"
- `setting/deities/tyr.md:112` — "Factions Guide): first meeting, ranks, missions"
- `setting/faction-operations/10-cassalanters.md:125` — "**Factions** guide overview"
- `setting/notable-figures/cassalanters/10-seffia-naelryke.md:91` — "Factions guide): her response team, escalation and the Windmill revelation"; `:102` — "Factions Guide page for her response team"
- `setting/organizations/01-harpers.md:41` — "Factions guide): Grand Game stance, quest hooks, first meeting, renown and"
- `setting/organizations/02-lords-alliance.md:43` — "Factions guide): Grand Game stance, quest hooks, first meeting, renown and"
- `setting/organizations/03-emerald-enclave.md:46` — same wording
- `setting/organizations/04-order-of-the-gauntlet.md:33` — same wording
- `setting/organizations/05-force-grey.md:34` — same wording
- `setting/organizations/06-doom-raiders.md:48` — same wording
- `setting/organizations/07-bregan-daerthe.md:53` — same wording
- `setting/organizations/08-xanathars-guild.md:36` — "Factions guide): response teams, outposts, escalation, revelation list"
- `setting/organizations/09-manshoons-zhentarim.md:39` — same wording as 08
- `setting/organizations/10-cassalanters.md:100` — "(Faction Operations): response teams, outposts, escalation, revelation list" (this is the pilot's own pointer, not the guide)
- `setting/the-grand-game/the-grand-game.md:10` — "Factions Guide page for each faction"; `:71` — "Factions Guide): response teams, outposts, escalation and revelation lists"
- `setting/the-grand-game/what-each-faction-knows-at-start.md:10` — "Factions Guide pages for each faction"; `:71` — "Factions Guide): response teams, outposts, escalation and revelation lists" and "Factions Guide): the player faction"; `:100` — "Factions Guide (`03-lords-alliance"
- `setting/villains/cassalanters.md:10` — "Factions Guide"; `:111` — "Factions Guide): response teams, outposts, escalation, revelation list"; `:134` — "Factions Guide page for the family, as the **Xanathar** page does"
- `setting/villains/jarlaxle.md:11` — "Factions Guide"; `:161` — "Factions Guide): response teams, outposts, escalation, revelation list"; `:167` — "Factions Guide, the Trollskull ev-04 and flowchart text and the Trollskull"
- `setting/villains/manshoon.md:11` — "Factions Guide"; `:120` — "Factions Guide): response teams, outposts, escalation, revelation list"; `:142` — "Factions Guide line should be retargeted when the guide pages are removed"
- `setting/villains/xanathar.md:10` — "Factions Guide"; `:96` — "Factions Guide): response teams, outposts, escalation, revelation list"; `:110` — "Factions Guide page for the Guild"
- `setting/history/04-the-founding-of-chains.md:127` — no phrase; see G3.

Gazetteer phrases:
- `gazetteer/waterdeep/north-ward.md:272` — "Factions Guide and `arc-i-kolat-towers"
- `gazetteer/waterdeep/southern-ward.md:11` — "faction guide"
- `gazetteer/waterdeep/trades-ward.md:249` — "Factions Guide says he followed Krebbyg once and knows where the messages"; `:251` — "Factions Guide says every two days (`08-bregan-daerthe"

Structure documents (skipped by the viewer, still under `campaign/`):
- `structure/arc-e-faction-outposts.md`: 149 "Factions guide page for the full area layout", 153 "Factions guide page for keyed area details", 167 "Factions guide page for full area descriptions", 251 "Factions guide page for full room descriptions", 267 "Factions guide page (Response Teams section)", 277 "Factions guide page", 351 "Factions guide pages for full compositions and carried documents", 355 "Factions guide page (Response Teams section)", 433 "Factions guide pages", 445 "Factions** guide pages — Quest Hooks for Harpers, Lords' Alliance, Doom Raid", 495 "Factions guide page"
- `structure/arc-f-xanathars-lair.md`: 341 "Factions guide page — outpost entries, response team compositions, escalat", 426, 428, 430, 432 "Factions guide page"
- `structure/arc-g-cassalanter-villa.md`: 435 "Factions guide page — outpost entries, response team compositions, escalat", 531, 533, 535, 537 "Factions guide page"
- `structure/arc-h-sea-maidens-faire.md`: 339 "Factions guide page — outpost entries, response team compositions, escalat", 430 "Factions guide page"
- `structure/arc-i-kolat-towers.md:323` — "Factions guide page — Quest Hooks section; full operation write-up for the"
- `structure/arc-j-vault-of-dragons.md:329` — "Factions** guide pages — All seven Mission 6 entries (Missions section), quo"

Notes:
- The organization pages' "Factions guide" lines are short cross-reference bullets. Those are the `setting/organizations/*` entries above.
- `setting/faction-operations/10-cassalanters.md:125` is the pilot's own bold cross-reference "**Factions** guide overview". It will go stale when `01-overview` is removed.

### G3. Page titles

Each guide H1 is identical to its organization page H1:
- `guides/factions/02-harpers.md:1` "# The Harpers" = `setting/organizations/01-harpers.md:1` "# The Harpers"
- `03-lords-alliance.md:1` "# The Lords' Alliance" = `02-lords-alliance.md:1`
- `04-emerald-enclave.md:1` "# The Emerald Enclave" = `03-emerald-enclave.md:1`
- `05-order-of-the-gauntlet.md:1` "# The Order of the Gauntlet" = `04-order-of-the-gauntlet.md:1`
- `06-force-grey.md:1` "# Force Grey" = `05-force-grey.md:1`
- `07-doom-raiders.md:1` "# The Zhentarim (Doom Raiders)" = `06-doom-raiders.md:1`
- `08-bregan-daerthe.md:1` "# Bregan D'aerthe" = `07-bregan-daerthe.md:1`
- `09-xanathars-guild.md:1` "# Xanathar's Guild" = `08-xanathars-guild.md:1`
- `10-manshoons-zhentarim.md:1` "# Manshoon's Zhentarim" = `09-manshoons-zhentarim.md:1`
- `11-cassalanters.md:1` "# The Cassalanters" = `10-cassalanters.md:1`
- `01-overview.md:1` "# Factions" (no organization twin)

Bold references that name a title with a qualifier:
- `setting/the-grand-game/what-each-faction-knows-at-start.md:71` — "**The Zhentarim (Doom Raiders)** (Factions Guide): the player faction." This is the only title reference that names the Factions Guide. Every other "The Zhentarim (Doom Raiders)" bold reference points at Organizations, for example `setting/the-grand-game/the-grand-game.md:70`, `setting/villains/manshoon.md:19`, `gazetteer/waterdeep/dock-ward.md:281`.
- `setting/the-grand-game/what-each-faction-knows-at-start.md:71` — "**Xanathar's Guild**, **Manshoon's Zhentarim**, **The Cassalanters** and **Bregan D'aerthe** (Factions Guide): response teams, outposts, escalation and revelation lists."

Because the H1 titles match, bold names alone do not say which journal is meant after the move. See Decision D7.

### G4. `.claude/` and `CLAUDE.md`

- `CLAUDE.md:161` — "**Factions Guide** (`campaign/guides/factions/`): factions as game mechanics. Faction lore lives in `campaign/setting/organizations/`."
- `CLAUDE.md:163–168` — the file table for the Factions Guide: "| `01-overview.md` | How renown works, running faction missions, page map |", "| `02-harpers.md` … `07-doom-raiders.md` | Player factions: Grand Game Stance, Quest Hooks, First Meeting (summary + link to its event), Renown & Ranks, Missions |", "| `08-bregan-daerthe.md` | Player and villain faction: the player-faction sections plus Response Teams, Outposts, Escalation, Revelation List |", "| `09-xanathars-guild.md`, `10-manshoons-zhentarim.md`, `11-cassalanters.md` | Villain factions: Response Teams, Outposts, Escalation, Revelation List |"
- `CLAUDE.md:189` — "| `organizations/` | 10 faction pages: 01-harpers through 10-cassalanters. Lore only: Operations, Key Members, Grand Game Agenda, Overview. Game mechanics (stance, hooks, first meeting, renown, missions, response teams, outposts, escalation, revelation lists) live in the **Factions Guide**. |"
- `CLAUDE.md:363` — "**Factions: mechanics vs lore:** Faction game mechanics go in the Factions Guide (`campaign/guides/factions/`); faction lore goes in the organization pages. Never put rules, hooks, missions, renown or villain-response mechanics on an organization page."
- `CLAUDE.md:161`, `CLAUDE.md:189` and `CLAUDE.md:363` all point at the Factions Guide.
- `.claude/agents/consistency-checker.md:45` — "- Faction mechanics live in the Factions Guide or faction-operations pages; faction lore lives in the organization pages."
- `.claude/agents/consistency-checker.md:57` — "- **crossrefs**: bold cross-references name pages that exist and mean the right page; references to the Factions Guide or \"faction operations\" point at pages where those now live."
- `.claude/skills/adventure-reloaded/SKILL.md:388–438` — the File Type Spec 8 template for `campaign/setting/organizations/NN-faction.md` puts mechanics on the organization page. It includes headings "## Grand Game Stance" (L410), "## Quest Hooks ← player factions" (L417), "## Response Teams ← villain factions" (L421), "## Outposts" (L422), "## Escalation" (L423), "## Revelation List" (L426), "## Renown & Ranks" (L428) and "## Missions" (L430). This contradicts `setting-compendium-rebuild-plan.md:50`. It needs retargeting or removal (plan pass 7).
- `.claude/skills/adventure-reloaded/SKILL.md:519` — "- **Organizations** (`campaign/setting/organizations/`) — 10 faction pages (01-harpers through 10-cassalanters). Each page merges player-faction and villain-faction content: operations, key members, Grand Game stance, quest hooks, response teams, outposts, escalation, renown, and missions (see File Type Spec 8)." Same issue.
- `.claude/skills/update-campaign-viewer/SKILL.md:15` — "...skips anything under `campaign/structure/` — those are superseded structure documents..." (no faction reference; relevant to (h)).

No `guides/factions` path or `Factions Guide` phrase appears anywhere in `.claude/` beyond the two consistency-checker lines above.

### G5. `scripts/`
- No match for `factions`, `guides`, `faction-operations` or `organizations` in any file under `scripts/` (case-insensitive). The grep returned "No matches found."

### G6. Counts outside `campaign/`, `.claude/`, `CLAUDE.md`, `scripts/` (matched lines; not read)
- `docs/` (all files under docs/plans, plus docs/index.html): `docs/plans/` 232 matched lines in 72 files. `docs/index.html` 1 matched line (line 1104), which embeds the old guide paths `guides/factions/01-overview.md` to `11-cassalanters.md` in the viewer's data blob. It is generated by `scripts/build-viewer.py`. It contains no `faction-operations` path.
- Root handoffs (`session*handoff.md`): 88 matched lines in 20 files. Not read, per your instruction.
- `sources/`: 512 matched lines in 24 files, mostly `sources/research/pass3-bundles/*` and `sources/research/pass4-bundles/*`. `sources/SOURCE_GUIDE.md` has 1 matched line, L252: "**When to consult:** Throughout Act III whenever PCs take action against faction assets. Chapter 3 (structural rules: how response teams work). **Running the Villains** (GM Guide) (villain faction operations)." This is generic wording, not a guide reference.
- `campaign-reader/dist/index.html` 1 matched line (line 1063), a built artifact.
- `sources/5etools/books.json` 1 matched line (not inspected).

### G7. Relative links inside the guide pages (these must change; see plan line 104)
Matched lines containing `](`: 01-overview 16; 02-harpers 5; 03-lords-alliance 11; 04-emerald-enclave 5; 05-order-of-the-gauntlet 12; 06-force-grey 5; 07-doom-raiders 6; 08-bregan-daerthe 5; 09-xanathars-guild 0; 10-manshoons-zhentarim 0; 11-cassalanters 0. Totals: 65 lines in 8 files.

The link targets are of two kinds:
- To quest journals, e.g. `campaign/guides/factions/02-harpers.md:39` "[Harpers First Meeting](../../quests/faction-events/harpers/00-first-meeting/ev-01-first-meeting.md)". Depth check: `campaign/guides/factions/` and `campaign/setting/faction-operations/` are both three segments below the repo root, so `../../quests/…` still resolves from the new folder.
- To GM Guide, Players' Guide and Organizations pages: `campaign/guides/factions/01-overview.md:51–56` (e.g. "[GM Guide: Player Factions Overview](../gm-guide/player-factions-overview.md)"). `../gm-guide/` and `../players-guide/` resolve to `campaign/setting/…` from the new folder and break. `../../setting/organizations/` still resolves.

---

## (h) Viewer and scripts

**`scripts/build-viewer.py`** (run from the repo root; the paths are relative)
> `CAMPAIGN_DIR = "campaign"` — scripts/build-viewer.py:10
> `TEMPLATE_PATH = ".claude/skills/update-campaign-viewer/references/viewer-template.html"` — :11
> `OUTPUT_PATH = "docs/index.html"` — :12
> `MD2HTML_PATH = ".claude/skills/foundry-journal/scripts/md2html.py"` — :14
> "    for dirpath, dirnames, filenames in os.walk(CAMPAIGN_DIR):" / "        # Skip structure/ subtree (superseded by quest journals)" / "        if "structure" in dirpath.split(os.sep):" / "            continue" / "        dirnames[:] = [d for d in sorted(dirnames) if d != "structure"]" — :32–36
> `rel = os.path.relpath(full, CAMPAIGN_DIR).replace(os.sep, "/")` — :42

The walk is recursive and alphabetical, and it skips any folder named `structure`. It has no list of folders or journals. A new folder is picked up automatically, and the old `guides/factions` pages drop out once they are deleted. The script does not reference `guides/factions` or `faction-operations`.

**Viewer template** (`.claude/skills/update-campaign-viewer/references/viewer-template.html`)
> "const ROOT_ORDER = ['guides', 'locations', 'gazetteer', 'quests', 'setting'];" — :1109
> "const QUESTS_ORDER = ['act-i', 'act-ii', 'faction-missions'];" — :1110
> "  if (dirPath === '') orderList = ROOT_ORDER;" / "  else if (dirPath.split('/').pop() === 'quests') orderList = QUESTS_ORDER;" — :1205–1206
> "    return a.name.localeCompare(b.name);" — :1221
> "  m = /^(\d+)-/.exec(base);" / "  if (m) return [200 + parseInt(m[1], 10), lower];" — :1195–1196
> "  if (lower === 'overview' || lower === 'area-overview') return [0, lower];" — :1191

Findings:
- No journal or folder is registered anywhere. `ROOT_ORDER` applies only at the root, and `QUESTS_ORDER` only to a folder named `quests`. A folder under `setting` sorts alphabetically by display name.
- Display name comes from `kebabToTitleCase`, so `faction-operations` shows as "Faction Operations".
- Pages sort by the numeric prefix. `01-harpers.md` through `10-cassalanters.md` sort correctly. The `overview` key only applies to a file named exactly `overview.md` or `area-overview.md`.
- `QUESTS_ORDER` lists `'faction-missions'`, but the folder on disk is `campaign/quests/faction-events/`. The entry is stale. It has no effect on this move.
- The viewer's page titles come from the first `# ` heading. The faction-operations pilot and the organization page both have `# The Cassalanters`, so the viewer will show two pages with that title.

**`.claude/skills/foundry-journal/scripts/md2html.py`**
> "- A folder produces one page per .md file inside it (top-level only, not recursive), sorted by filename, skipping `design-notes.md` (Design Note *pages* are dropped at the JSON-conversion step per project convention; `[!design]` sidebars inside other pages are kept as-is)." — :9–12
> "def gather_pages(target):" / "    if os.path.isdir(target):" / "        files = sorted(glob.glob(os.path.join(target, '*.md')))" / "        files = [f for f in files if os.path.basename(f) != 'design-notes.md']" — :392–395

No path references. No registry. Folder conversion is sorted by filename and needs no change for the new folder.

**`.claude/skills/foundry-journal/scripts/assemble.py`**
> "`pages` lists titles in the FINAL desired Foundry page order (overview, then events in sequence, then flowchart -- design-notes.md pages are simply left out of this list, since they're dropped on conversion). This is where page order is actually decided; md2html.py's own output order does not matter here, since pages are looked up by title." — :22–26

Page order comes from a config file passed in by the caller. No folder names are hard-coded.

**`.claude/skills/update-campaign-viewer/SKILL.md`**
> "Run this PowerShell script from the project root, using the PowerShell tool (not Bash). It walks `campaign/` for every `.md` file, skips anything under `campaign/structure/`..." — :15
The skill builds the viewer with PowerShell (`Get-ChildItem … -Recurse`, excluding `*\structure\*`). `scripts/build-viewer.py` (Python) builds `docs/index.html` for GitHub Pages. The two are separate paths. Neither needs registration.

**`campaign-reader/`**
> "- `guide`: list exact reviewed Markdown file paths in `files`, each under `campaign/guides/`." — campaign-reader/README.md:14
> "- Any faction-event folder whose exact path is listed as `accepted` in `docs/plans/faction-voice-ledger.json`." — campaign-reader/README.md:7
- `campaign-reader/reviewed-content.json` has no `factions`, `faction-operations` or `guides/` entries (grep: no match).
- `docs/plans/faction-voice-ledger.json` does not exist.
- `scripts/build-campaign-reader.py` does not exist (Glob: no files). The README tells the reader to run it at line 3.
- The reader is catalogue-based. New folders are not included unless catalogued.

**Other facts**
- `campaign/setting/` and `campaign/guides/` have no `.md` files directly inside them. Every file is in a subfolder (Glob). The viewer therefore treats both as plain folders.
- The viewer rebuild is needed after the move. `docs/index.html` currently has no `faction-operations` path. Its embedded old guide paths will remain until the build is re-run from the repo root.

---

## Execution plan

Order matters. Steps 1–10 can be done page by page, each with a commit. Steps 11–14 happen after every page is in place.

1. **01-harpers.md** ← `campaign/guides/factions/02-harpers.md`. Sections in order: GM summary (new), Purpose (new), lead-in (L3), Grand Game Stance (L5), Quest Hooks (L24), First Meeting (L35), Renown & Ranks (L41: Earning Renown L43, Harper Ranks L54), Missions (L64), Tone (new), Source References (new), Cross-References (L77). No reorder. Retarget: L39 (First Meeting link), L80, L83, L84, L85 (quest journal links, 4 on L85), L81 ("**Factions** guide overview", see D1).
2. **02-lords-alliance.md** ← `03-lords-alliance.md`. Stance L5, Quest Hooks L25, First Meeting L37, Renown & Ranks L47 (Earning L49, Ranks L60, Suspension and Dismissal H3 L72), Missions L80, Cross-References L99. Retarget: L45, L86–91 (six table links), L102, L105, L106, L107; L103 ("The **Factions** guide overview").
3. **03-emerald-enclave.md** ← `04-emerald-enclave.md`. Stance L5, Quest Hooks L25, First Meeting L35, Renown & Ranks L45 (Earning L47, Ranks L55), Missions L67, Cross-References L84. Retarget: L43, L87, L90, L91, L92 (four links on L92); L88.
4. **04-order-of-the-gauntlet.md** ← `05-order-of-the-gauntlet.md`. Stance L5, Quest Hooks L25, First Meeting L35, Renown & Ranks L43 (Earning L45 with "Quietly Reassigned" paragraph at L56, Ranks L58), Missions L70, Cross-References L87. Retarget: L41, L52, L76–81 (six table links), L90, L93, L94, L95; L91.
5. **05-force-grey.md** ← `06-force-grey.md`. Stance L5, Quest Hooks L25, First Meeting L35, Renown & Ranks L41 (Earning L43, Ranks L52), Missions L64, Cross-References L81. Retarget: L39, L84, L87, L88, L89; L85.
6. **06-doom-raiders.md** ← `07-doom-raiders.md`. Stance L5, Quest Hooks L25, First Meeting L35, Renown & Ranks L41 (Earning L43, Ranks L52), Missions L62 (paragraph L73 with two links), Cross-References L77. Retarget: L39, L73 (two links), L80, L83, L84, L85; L81. Also the H1 "The Zhentarim (Doom Raiders)" (D7).
7. **07-bregan-daerthe.md** ← `08-bregan-daerthe.md`. Stance L5, Quest Hooks L25, First Meeting L35, Renown & Ranks L41 (Earning L43, Ranks L52), Missions L62, Response Teams L75, Outposts L81 (Fenerus L83, Seven Masks L101), Escalation L115, Revelation List L126, Cross-References L146. Order already matches the plan. Retarget: L39 (full write-up link), L149, L153, L154, L155 (links); L150 ("**Factions** guide overview").
8. **08-xanathars-guild.md** ← `09-xanathars-guild.md`. Response Teams L5, Outposts L15 (Terasse L17, Grinda L37, Orb Confectioners L51), Escalation L65 (with the "Sylgar Overrides All Tiers" callout at L76–77), Revelation List L79, Cross-References L105. No links. Stance, Quest Hooks, First Meeting, Renown & Ranks and Missions do not exist in the source. See D4. Retarget the bold "**Factions** guide overview" at L110.
9. **09-manshoons-zhentarim.md** ← `10-manshoons-zhentarim.md`. Response Teams L5 (the three roster lines at L11–13 need blank lines between them), Outposts L15 (Interrogation House L17, Yellowspire L33), Escalation L47, Revelation List L58, Cross-References L80. No links. Retarget the bold "**Factions** guide overview" at L84.
10. **10-cassalanters.md** (pilot, already present) ← `11-cassalanters.md`. Check the body against the guide again with a `diff`. Retarget: pilot L118 (source reference to the guide, which is deleted by the move), pilot L125 ("**Factions** guide overview"). Keep the Source References wording decided under D8. Decide on the cross-reference heading text under D2 and D4.
11. **Overview (01-overview.md)**: no slot. Decide under D1. Then retarget every bold reference to "**Factions** guide overview" (guide lines 81, 103, 88, 91, 85, 81, 150, 110, 84, 105 and the pilot at 125) to the new location.
12. **Delete** `campaign/guides/factions/` (all eleven files) after the ten new pages are verified. Before deleting, retarget every item in G1–G2 that points at the deleted files.
13. **Retarget inbound references** (list in G1–G4):
    - `campaign/guides/gm-guide/grand-game-in-play.md:88, 100–103`
    - `campaign/guides/gm-guide/player-factions-overview.md:55, 154, 167, 177, 196, 205, 207`
    - `campaign/guides/gm-guide/running-the-villains.md:78, 84`
    - `campaign/guides/gm-guide/structural-rules.md:26, 90, 119–122`
    - `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:5`
    - the gazetteer hits (G1 and G2)
    - the setting hits (G1 and G2), including `setting/villains/*`, `setting/the-grand-game/*`, `setting/organizations/*` (ten pages), `setting/notable-figures/cassalanters/10-seffia-naelryke.md:77, 91, 102`, `setting/history/*`, `setting/deities/*`
    - `CLAUDE.md:161, 163–168, 189, 363` (plus the guides list at 163–168 and the Campaign Guides section)
    - `.claude/agents/consistency-checker.md:45, 57` (these describe the rule, so they may need no change)
    - `.claude/skills/adventure-reloaded/SKILL.md:388–438, 519` (plan pass 7)
    - Quest-journal and structure references (G2): decide under D6.
14. **Rebuild the viewer** from the repo root: `python3 scripts/build-viewer.py` (writes `docs/index.html`). The skill's PowerShell path also rebuilds the Artifact. Confirm that `docs/index.html` no longer contains `guides/factions`.
15. **Verify** (plan lines 102–106):
    - Old counts equal new counts (plan line 102). The GM-summary and Source-References bullets added by the pilot change these counts. The rule does not say how to count them. See D5.
    - Grep the new pages for `ch2-city|ch1-beginning|Arc [A-J]\b|Appendix [A-F]|\bDM\b` (plan line 103). No hits in the guide pages.
    - No `.md` links remain (plan line 104).
    - Every page has an Overview (plan line 105). See D2.
    - 10 faction-operations pages (plan line 106).
    - Run `consistency-checker` (plan line 93).

## Decisions for the user

Each decision gives the quoted lines and the options. I have not recommended any option.

**D1. 01-overview.md (no slot in the 10-page plan)**
> "| Faction operations (GM-only) | Gamemaster's Summary; Grand Game Stance; Quest Hooks; First Meeting; Renown & Ranks; Missions; Response Teams; Outposts; Escalation; Revelation List (the existing sections, moved verbatim, in a unified order) |" — docs/plans/setting-compendium-rebuild-plan.md:62
> "10 GM-only companion pages: renown & ranks, missions, outposts, response teams, escalation, revelation list" — docs/plans/setting-compendium-rebuild-plan.md:34
> "- Page counts match: 122 figure pages, 10 + 10 organization pages, one page per confirmed deity." — :106
Options: (a) an 11th page, which breaks the count rule at :106; (b) a hub page using the Hub row, which the plan does not list for this journal (`setting-compendium-rebuild-plan.md:55`); (c) fold its unique rules (section 1 of (f)) into `campaign/guides/gm-guide/player-factions-overview.md`'s Renown section; (d) delete it and keep only CLAUDE.md's rules. The unique items are listed in (f). Its "Pages in This Guide" table is navigation and needs no successor.

**D2. Overview on faction-operations pages**
> "- Every page has a GM summary, an Overview and Source References. Every Overview obeys the spoiler rule." — docs/plans/setting-compendium-rebuild-plan.md:105
> "| Faction operations (GM-only) | Gamemaster's Summary; Grand Game Stance; …" — :62 (no Overview)
> "- Until the prose pass, every page may carry its full GM information, including in the Overview." — :51
The pilot has no Overview either. Options: add an Overview to each faction-operations page, or exempt them from :105.

**D3. GM callout syntax**
> "Every page: `# Title` → `> Structuring draft.` → `> **[GM]**` Gamemaster's Summary → ..." — docs/plans/setting-compendium-rebuild-plan.md:40
> "> **[GM]**" / "> #### Gamemaster's Summary" — docs/plans/setting-compendium-pilot-brief.md:18–20
> "> [!gamemaster]**Gamemaster's Summary**" — campaign/setting/faction-operations/10-cassalanters.md:5
> "> [!gamemaster]**Gamemaster's Summary**" — campaign/setting/the-grand-game/the-grand-game.md:5
> "One page per NPC: H1, `> [!gamemaster]**Gamemaster's Summary**` box, ## Roleplaying Information, ## Character Information, ## Overview." — CLAUDE.md:188
Options: keep the pilot's form, or switch to the plan's `> **[GM]**` form.

**D4. Missing sections on pages 09 and 10**
> "| Faction operations (GM-only) | Gamemaster's Summary; Grand Game Stance; …" — :62
> "This pass also resolves the heading drift across the current files (`01`–`04` use `### Earning Renown` / `### Ranks & Benefits`, `05`–`06` are flat, `08`–`10` omit Grand Game Stance, …" — :91
> "Nothing lost. Every fact in today's files lands in exactly one new page." — :14
> "Nothing invented" (brief rule 1): "Nothing lost, nothing invented. Every concrete fact on the page you replace lands on your new page …" — docs/plans/setting-compendium-pilot-brief.md:42
Guide pages 09 and 10 have no Grand Game Stance, Quest Hooks, First Meeting, Renown & Ranks or Missions text to move. Options: omit those sections, or write new text (which the "moved verbatim" rule does not allow). The pilot kept a Stance for the Cassalanters because page 11 has one.

**D5. Verification counts**
> "- Heading and bullet counts of each old file equal the sum across its new pages." — docs/plans/setting-compendium-rebuild-plan.md:102
The pilot adds bullets: 4 in the GM summary (pilot 7–10) and 2 in Source References (pilot 117–118). The rule does not say whether added bullets count. The move's verbatim diff check is also not stated for faction-operations pages. The rule at :102 covers only Notable Figures and Organizations.

**D6. Quest-journal and structure references (about 190 lines)**
> "- `campaign/guides/factions/…`" and the "Factions Guide" phrases in G2 — e.g. campaign/quests/faction-events/harpers/r03-harpshadow/design-notes.md:7 "Factions Guide"
> "- **Quest Journals**" — docs/plans/setting-compendium-rebuild-plan.md line 116 is "Out of scope: … the quest and location journals" — :117
Quest and structure files are out of scope in the plan (:117). Options: leave them as historical references, or retarget them as part of this move. Some of them (the `structure/arc-e…` through `arc-j` pages, which CLAUDE.md treats as authoritative until converted) are active.

**D7. Duplicate H1 titles**
> "# The Cassalanters" — campaign/guides/factions/11-cassalanters.md:1 and campaign/setting/organizations/10-cassalanters.md:1 (and the same for the other nine pairs in G3)
> "- **Cassalanters** organization page: identity, tenets, key members, lore overview" — pilot:122
The viewer uses the H1 as the page title, and the search index is keyed by path. Options: keep the identical H1, or qualify the faction-operations H1 (for example "The Cassalanters (Faction Operations)").

**D8. Pilot source-reference wording after deletion**
> "- `campaign/guides/factions/11-cassalanters.md`: every section below the Gamemaster's Summary, moved verbatim (Session 47 consistency fixes …)" — campaign/setting/faction-operations/10-cassalanters.md:117
This line names a file the move deletes. Options: keep it as provenance (naming the deleted path), or rewrite it.

**D9. Move or keep both (already decided, confirm it still stands)**
> "Items 9-10 adopted as **move** (delete the guide pages after copying, retarget inbound links, rebuild the viewer)." — docs/plans/setting-compendium-pilot-findings.md:20
> "Until `guides/factions/11-cassalanters.md` is removed, both copies exist." — campaign/setting/organizations/10-cassalanters.md:118
The execution plan assumes the move.

**D10. Pilot content defects that the move carries unchanged**
> "24 ERROR (cross-page): line 73 "not yet actively pursuing the Stone" (era 61; villains/cassalanters.md:39) vs ops 19 "the family needs the Stone", ops 23 Seffia's team joins the Xanathar's Lair Eye heist …" — docs/plans/setting-compendium-research-notes/consistency-pilot-pages.md:34
> "29 DRIFT: … Cross-references differ (guide 100 "operations, key members, lore overview"; ops 121 "identity, tenets, key members")." — :41
Options: fix now, or after the move. The verbatim rule (plan :14) applies to the text.

**D11. Link conversion**
> "- No `.md` links remain. Every bold cross-reference names an existing page." — docs/plans/setting-compendium-rebuild-plan.md:104
The guide pages have 65 lines of relative links (G7). The plan's rule implies converting them to bold names. The `../gm-guide/` and `../players-guide/` relative links break after the move. Options: convert to bold names, or retarget the relative paths.

**D12. Section names not checked against the plan**
The plan's pass 5 description of heading drift (:91) does not match the guide headings in (d). Options: check the organization pages, or ignore the description.

## Conflicts between sources

- Renown: 01-overview.md:25 ("Supplementary renown … stacks on top") vs player-factions-overview.md:24 and faction-affiliations.md:24 ("No other source awards Renown; general good roleplay earns none on its own.").
- Renown: 01-overview.md:25 ("a mission that causes collateral damage costs −1") vs player-factions-overview.md:25 and faction-affiliations.md:25 ("Serious offenses cost 2 Renown each: betraying a mission, harming faction members, or working against the faction's interests."). The -1 and -2 rules are not stated together.
- Honest failure: player-factions-overview.md:26 and faction-affiliations.md:26 ("An honest attempt that fails costs nothing: formal suspension until reinstated, or outright dismissal.") vs campaign/guides/factions/03-lords-alliance.md:76 ("Honest failure costs nothing. A target who escapes, a failed roll or a beaten party does not fire the visit …"). Higher-ranked source: the Lords' Alliance page is the faction's own mechanics file. Ranking under the caller's rules: the campaign files outrank each other only by recency of the decision; I did not rank them.
- Reinstatement: 01-overview.md:11 ("usually after a demonstrated act of service to the city") vs 03-lords-alliance.md:78 ("Reinstatement has three routes …"). Not contradictory; the detail differs.
- Heading drift: plan :91 vs guide headings in (d) (see D12).
- Stance and drift: consistency-pilot-pages.md:41 describes guide heading "The Soul Pact: Active vs. Passive Mode" at guide line 5. The current guide line 5 is "## Grand Game Stance". The note is stale.
- Stale line numbers in older notes: pilot-findings.md:32 cites `setting/villains/cassalanters.md:57` (current hit at :96). pilot-findings.md:32 cites `gm-guide/grand-game-in-play.md:103` (current, matches). pilot-findings.md:32 cites `gm-guide/structural-rules.md:26,90,122` (current, matches). pilot-findings.md:32 cites `guides/factions/01-overview.md:47` (current, matches).
- GM callout: plan :40 and pilot-brief :18–20 (`> **[GM]**`) vs the-grand-game.md:5, pilot :5 and CLAUDE.md:188 (`> [!gamemaster]**Gamemaster's Summary**`).

## Cross-references

Covered in (g) G1–G4 and (h). Within (c) and (d), each cross-reference is cited at its line in the guide or pilot file.

## Not found

- `faction-operations` in CLAUDE.md, except inside "inter-faction operations" at CLAUDE.md:144. The CLAUDE.md guide list has no faction-operations entry.
- `faction-operations` in `scripts/`, `.claude/`, `sources/SOURCE_GUIDE.md`, or `campaign-reader/`.
- `guides/factions` path in `scripts/`, `.claude/`, `campaign-reader/reviewed-content.json`, `docs/plans/faction-voice-ledger.json` (file missing), `scripts/build-campaign-reader.py` (file missing), or the viewer template.
- Any renown, delivery or calibration rule from 01-overview in `campaign/setting/the-grand-game/`.
- A `## Overview` heading in any guide page 02–11 or in the pilot.
- A "Soul Pact" heading in either Cassalanter page.
- "binary" in either Cassalanter page.
- A faction-operations hub page or index (none in the plan or on disk).
- Source-guide pointers to any guide page (`sources/SOURCE_GUIDE.md`).
- A `DM` term, `Arc [A-J]`, `Appendix A–F` or `ch1`/`ch2` term in guide pages 02–11.

## Not readable

- Nothing in `campaign/`, `.claude/`, `scripts/` or `docs/plans/` was unreadable.
- Not opened: `sources/SOURCE_GUIDE.md` ties three `.docx` NPC guides to the faction organization pages: "`Davil and the Doom Raider Zhents + Elf Killer mission and more.docx`" (SOURCE_GUIDE.md:688, Doom Raiders section), "`Jarlaxle Baenre NPC Guide.docx`" (SOURCE_GUIDE.md:690, Bregan D'aerthe section) and "`Meloon Wardragon NPC Guide.docx`" (SOURCE_GUIDE.md:692, Force Grey section). They are not tied to the Factions Guide. I did not open them, so I cannot say whether they contain faction mechanics.
- Not opened: the Ember export (`01 - Ember.zip`) and the Alexandrian PDFs. Neither bears on this move, as explained in the method limits.
- Not read: the root handoff files (counted only, per your instruction).