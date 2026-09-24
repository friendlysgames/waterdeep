# Session 31 Handoff
**Date:** 2026-09-24
**Status:** Ready to continue. Everything is merged to master (PRs #3 and #4). No task is in progress.

---

## What Was Done

This session started the guides prose-writing pass with the **Players' Guide**. All five pages are now finished player-facing text with Foundry sidebars. Each was drafted, polished on Sonnet 4.6, QA'd, and had its spoilers removed.
- **foundry-journal skill:** the user supplied their campaign-specific version (from their Curse of Strahd project), and it was adapted to Waterdeep, including the `md2html.py` and `assemble.py` conversion scripts.
- **Viewer:** the build now renders `> [!type]**Title**` sidebars as Foundry-style HTML, both on the live GitHub Pages site and locally.
- **Bregan D'aerthe:** the user ruled that BD recruits only in **Trollskull Alley**, and every page carrying the old conditional or drow-only entry was brought into line.
- **New agent:** a `prose-drafter` project agent, pinned to Sonnet 4.6, now handles drafting.

---

## Changes Made

Range `c77039c..HEAD` covers 26 commits and 28 files. The Session 30 handoff commit (`85ad350`) lives only on `origin/claude/artifact-github-pages-0gn1s7`; see Warnings.

### Files Created
| File | Purpose |
|------|---------|
| `.claude/agents/prose-drafter.md` | Drafting agent pinned to `claude-sonnet-4-6`. Loads the style skills for the page's audience, checks every name, and self-polishes. |
| `.claude/skills/foundry-journal/scripts/md2html.py` | Markdown → Foundry page HTML (one file or a whole folder; `design-notes.md` skipped). Also exports `render_sidebars_markdown()`, which the viewer build uses. |
| `.claude/skills/foundry-journal/scripts/assemble.py` | Wraps converted pages in the JournalEntry/JournalEntryPage envelope, including the `_key` fields. |
| `.claude/skills/foundry-journal/references/sidebar-icons.md` | The definitive sidebar type → icon table. Replaces `sidebar-html.md`. |
| `campaign/guides/gm-guide/bonds-and-flaws.md` | GM version of Bonds and Flaws: the full player page plus a GM Notes table of where each Flaw lands in the campaign. |

### Files Modified
| File | What changed |
|------|-------------|
| `.claude/skills/foundry-journal/SKILL.md` | Rewritten from the user's CoS skill for Waterdeep: one folder is one JournalEntry and one .md file is one page; markup components; sidebar rules; conversion rules. |
| `.claude/skills/foundry-journal/references/json-structure.md` | Adds a note that `_key` is required. |
| `scripts/build-viewer.py` | Loads `render_sidebars_markdown` from md2html and converts sidebars before injecting the pages. |
| `CLAUDE.md` | foundry-journal row; agents rule now names `prose-drafter`; guide rows for Bonds and Flaws (player and GM); BD wording no longer says "conditional". |
| `.gitignore` | Ignores `__pycache__/` and `*.pyc`. |
| `campaign/guides/players-guide/*.md` (all 5) | Finished player-facing prose with sidebars. Structuring banners and Source References removed. Spoilers and contact names removed. |
| `campaign/guides/gm-guide/about-this-campaign.md`, `debts-of-the-city.md` | Now contain their Players' Guide counterparts word for word, with GM-only material kept in draft form. Istrid Horn's and Blastwind's details corrected. |
| `campaign/guides/gm-guide/player-factions-overview.md`, `design-notes-running-the-campaign.md` | BD recruits in Trollskull Alley; the design note now explains why the nimblewright thread leads to Jarlaxle. |
| `campaign/setting/organizations/07-bregan-daerthe.md` | Single Trollskull entry rule; party-wide First Meeting; mission delivery chain corrected. |
| `campaign/setting/villains/jarlaxle.md` | "Conditional Entry" split into membership and villain activation. Structuring banner removed. |
| `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md` | Any PC can be recruited into BD, and the Nevercott visit always arrives unless the party reported the watchers. Typo fixed. |
| `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md` | The private-cabin scene is for BD operatives only. |
| `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md` | Fel'rekt's dinner invitation is for BD members only and never reopens membership. |
| `campaign/quests/faction-missions/bregan-daerthe/m02-the-wazoo-affair/overview.md` | Nevercott "finds the party again", as their recruiter. |
| `campaign/structure/arc-e-faction-outposts.md`, `arc-h-sea-maidens-faire.md` | BD membership now comes only from Trollskull Alley. |

### Files Deleted
| File | Reason |
|------|--------|
| `.claude/skills/foundry-journal/references/sidebar-html.md` | Replaced by `sidebar-icons.md`. |

---

## Key Decisions

### The Players' Guide goes first in the prose pass
> "I think it's time we start drafting the actual text for the guides and setting journals." — User, this session (chose the Players' Guide as the starting point)

### Sidebars: markdown source, HTML in the viewer
**Decision:** Authors write `> [!type]**Title**` in the .md file. `build-viewer.py` converts it to `fvtt advice` HTML at build time, using the same converter as the Foundry JSON step. Sidebars nested inside `> **[GM]**` zones stay inside their blockquote.
> "as a note, this is where we start working with sidebars from the foundry skill" / "I want html based sidebars for the viewer." — User, this session

### The foundry-journal skill is the user's campaign-specific version
**Decision:** Adapted from the user's uploaded CoS skill, scripts and icon table. dnd5e enrichers are added **only at the JSON step**. `design-notes.md` pages are **dropped** on Foundry conversion, but `[!design]` sidebars are kept.
> "I have a slightly better foundry-journal skill but it's campaign specific, I will want you to update it" — User, this session

### Drafting agents are pinned to Sonnet 4.6
**Decision:** New `prose-drafter` agent with `model: claude-sonnet-4-6`. The `sonnet` alias resolves to the newest Sonnet (Sonnet 5), which is not what CLAUDE.md specifies.
> "why are they sonnet 5 and not sonnet 4.6?" … "go ahed with that custom agent" — User, this session

### No faction contact names in the Players' Guide
**Decision:** The faction table's Contact column is removed, and Mirt, Melannor, Hlam, Davil (in the Zhentarim sidebar), Vajra and Zardoz are removed from player pages. The Debts of the City entries still name their Holders, because each Debt is something the character already knows.
> "Matter of fact, hide all contact names" — User, this session

### The Flaws quest mapping is GM-only
**Decision:** The "Where the campaign presses" column is removed from the Players' Guide. The mapping, in its original wording, moves to the new `gm-guide/bonds-and-flaws.md`.
> "Remove the \"where the campaign presses\" from the flaws table. That's GM information." — User, this session

### Bregan D'aerthe recruits only in Trollskull Alley
**Decision:** Chosen as "Trollskull only". BD recruits like every other faction, and any PC can join. The J.B. Nevercott visit always comes unless the party reported the watchers to the Watch, which sets **BD Contact Severed** and closes BD membership for the campaign. The Fireball! nimblewright thread → Sea Maidens Faire is where Jarlaxle is unmasked; it is not a way to join. Jarlaxle's villain activation (the **Jarlaxle Informed** flag, set in Fireball! ev-04 and read in Gralhund Villa) is unchanged.
> "we have fixed this everywhere but where it matters most, apparently. BD does approach during Trollskull Alley." — User, this session

### Bregan D'aerthe's contact is hidden
**Decision:** Chosen as "Hide the contact". The faction name stays in the player table; the contact isn't named, and the offer column no longer says "drow".

---

## Rules and Instructions

All prior standing rules still apply. Carried forward from the Session 30 handoff, which isn't on master:
- **Master writes via MCP only:** `git push origin master` is blocked by branch protection. Go through PRs (the user asked for "pr, merge" this session) or `mcp__github__push_files`.
- **`docs/index.html` is a build artifact:** never commit a hand-built copy. CI rebuilds it. After a local `python3 scripts/build-viewer.py`, run `git checkout docs/index.html`.
- **Viewer template:** it's about 1,756 lines, so use targeted Edits and never a full Write.

New this session:
- **Drafting goes to `prose-drafter`** (Sonnet 4.6), and polishing to `prose-polisher`. Never use `general-purpose` with the `sonnet` alias for content (now in CLAUDE.md).
- **Sidebar syntax:** `> [!type]**Title**` plus `>` body lines, with a blank line before and after. Inside GM zones, nest them as `> > [!type]**Title**`. Types: info, warning, lore, abstract, profile (alias tip), item, design, combat. macro, cue and music are reserved. Per page: 1–3, and never a replacement for prose.
- **The Players' Guide never names faction contacts or reveals quest mappings.** Anything a player shouldn't pre-know goes on the GM page.
- **Superset sync:** whenever a Players' Guide page with a GM counterpart changes, copy the change into the GM page in the same commit. Check with the line-presence script pattern used this session: every non-empty player line up to `## Cross-References` must appear in the GM page.
- **Always push and merge the handoff:** commit the handoff, push it, open a PR to master, and merge it in the same turn (now in CLAUDE.md, Handoff delivery).
  > "push, merge handoff. add it as a rule, always push and merge the handoff" — User, this session
- **After a merged PR:** restart the working branch from `origin/master` before new work, rebasing any unmerged commits on top.

---

## Problems Solved

- **Session 30 handoff missed at startup:** it sits only on `origin/claude/artifact-github-pages-0gn1s7`; found with `git log --all`.
- **NPC facts, checked against Notable Figures:**
  - Istrid Horn is a shield dwarf (not half-dwarf) who lends from the Dock Ward (not South Ward).
  - Skeemo's shop is in the Trades Ward.
  - Blastwind is a magistrate of the Watchful Order, not City Watch.
- **Spoilers removed from the Players' Guide:**
  - fireball death hint (Flaw 2)
  - Cassalanter bargain hints (Tiefling note, Flaws 3/5)
  - Asmodeus temple and Sea Maidens cargo hooks
  - Nim
  - Jarlaxle behind Zardoz Zord, and Luskan
  - Manshoon
- **Bregan D'aerthe drow-gated leftovers:** Fireball! private cabin, tavern dinner invitation, mission-delivery bullet, Mission 2 reading like a first meeting.
- **"Viewer hasn't updated":** CI deployed fine; the cause was the browser/CDN cache (hard-refresh). This container's network policy blocks github.io.
- **The WIP commit captured a `__pycache__` .pyc:** removed, and `.gitignore` added.

---

## Outstanding Work

### Carried forward (Sessions 29–30)
- [ ] Verify the deployed Pages URL works for the user (they reported a stale view this session, and cache is the likely cause)
- [ ] Bestiary: never drafted. Pages reference it as "not yet drafted" (Xanathar two-phase boss, Victoro and Ammalia, Aurinax)
- [ ] Faction Outposts conversion (`campaign/structure/arc-e-faction-outposts.md` → quest journal)
- [ ] Xanathar's Lair conversion
- [ ] Cassalanter Villa conversion
- [ ] Sea Maidens Faire conversion
- [ ] Kolat Towers conversion
- [ ] Vault of Dragons conversion + Scene 6: Xanathar GONE debrief
- [ ] Guides and setting prose-writing pass, now under way:
  - [x] Players' Guide (this session)
  - [ ] GM Guide (9 files, plus the new bonds-and-flaws)
  - [ ] Trollskull Manor Guide
  - [ ] Setting (lore, history, grand-game, villains, organizations, Notable Figures)
- [ ] Prose polish of the word-for-word NPC profile text in Notable Figures
- [ ] Prose polish of the Mission 5/6 summaries in the Organization pages' Missions tables

### New this session
- [ ] **GM Guide pass:** the GM-only material in `about-this-campaign.md`, `debts-of-the-city.md` (Holder sections) and `bonds-and-flaws.md` is still in draft form under the finished player text
- [ ] **Two GM-draft notes the superset agent flagged:**
  - the Renaer's Confidence Holder text frames the secret slightly differently from the new player text
  - the GM Holder register doesn't yet match the polished prose
- [ ] **`sources/backgrounds.json` doesn't exist**, but it's cited as the source for the XPHB/FRHoF background tables. The Heroes of Faerûn background names are unchecked.
- [ ] **BD organization page cleanup:**
  - pre-existing mismatch between coin-pouch gifts "after Missions 1 and 3" and older text
  - `ev-03` Ryvarra is visible "only to parties with drow PCs or the Yawning Portal check". That's flavor, but confirm it's intended now that recruitment is party-wide
- [ ] **Faction-mission sidebars:** some older sidebars lack a bold title (for example `[!abstract]+ If a BD Operative Is Present`). The converter handles them, but they could be normalized to `> [!type]**Title**`.
- [ ] **GM `player-factions-overview.md`** isn't a verbatim superset of the player `faction-affiliations.md`. Sync it during the GM Guide pass.

---

## Warnings and Caveats

- **The Session 30 handoff isn't on master.** It lives only in commit `85ad350` on `origin/claude/artifact-github-pages-0gn1s7`. This handoff carries its rules and outstanding items forward, so future sessions don't need it.
- **Commit `2ab3658` on master** (the direct MCP push of the sidebar converter) has a message that wrongly says it mirrors "commit ba38bd4-era work". There is no such commit. It's cosmetic and can't be amended on protected master.
- **`md2html.py` has two consumers**, the viewer build and the Foundry conversion. Before changing it, re-run the regression: convert all campaign `.md` files, expect 0 stray `[!` and balanced `<div>` tags, and 29 sidebars reported by `build-viewer.py` at the end of this session.
- **The GitHub Pages cache** holds the old viewer for up to 10 minutes after a deploy.
- **The superseded Arc A–D structure docs and `ch*.md`** still carry the old BD conditional wording. They're out of scope on purpose, so exclude them from QA greps.

---

## Where to Start Next Session

Read this handoff, then CLAUDE.md. Before any new work, run `git fetch && git checkout -B claude/<branch> origin/master`. Wait for the user to name the next task. The likely next step is the **GM Guide prose pass**: same pipeline as this session (`prose-drafter` → `prose-polisher` → `consistency-checker`), starting with the three GM pages that already contain finished player text (`about-this-campaign`, `debts-of-the-city`, `bonds-and-flaws`), then the rest. Other candidates are the Trollskull Manor Guide, the setting pages, the Bestiary, or a structure-doc conversion (load `adventure-reloaded`, and get a plan approved first).
