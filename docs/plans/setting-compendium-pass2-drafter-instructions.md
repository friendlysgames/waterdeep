# Pass 2 (Deities): Drafter Instructions

Binding instructions for every `prose-drafter` agent drafting a Deities page. They add the lessons of the three pilot pages (`tyr.md`, `siamorphe.md`, `zariel.md`) to `setting-compendium-pass2-brief.md`. Read the brief first, then this file, then the approved model pages `campaign/setting/deities/asmodeus.md` (deity) and `zariel.md` (patron).

## Inputs you are given

- The target file `campaign/setting/deities/<slug>.md`.
- The research notes file, `docs/plans/setting-compendium-research-notes/pass2/batch-*.md`. Find your power's section with `Grep -n "^## "`. Every fact on the page comes from that section, from the raw bundle in `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/<slug>/` (`5etools.md`, `wiki.txt`, `campaign-hits.txt`, `adventure-hits.txt`), or from a campaign file the notes cite. Open a campaign file to confirm a name or detail before you use it.

## What a good page does (from the pilot)

1. **Follow the model page's frame exactly:** `# Name`, `> Structuring draft.`, the `> **[GM]**` Gamemaster's Summary, `**Purpose:**`, the italic epithet line, nine metadata bullets in the brief's order, a blockquote edict, `## Influence and Followers` as bullets, the `Using X as a Deity` (or `as a Patron`) GM box, `## Overview`, `#### GM Notes` and `#### Secret` only where needed, `**Tone:**`, `---`, `## Source References`, `## Cross-References`, then a deletable `#### Draft Notes` callout.
2. **Metadata sources.** Deities: FRHoF supplies title, other names, worshipers (Typical Followers) and plane; SCAG (2014) supplies alignment, domains and symbol, labelled "SCAG, 2014". A power with no FRHoF or SCAG entry takes every field from the wiki, edition-tagged. Areas of Concern are never published: derive them from the portfolio and mark them `(derived)`. A field no source gives is `[research]`. Heads of other pantheons and patrons: use the PHB, SCAG or MTF entry for the Realms and say which source each field comes from; Dawn War (DMG) and Exandria (EGW) entries belong to other settings and are not used.
3. **The edict** is one derived line, listed in Draft Notes as derived. Write it as one plain clause, not a three-part list.
4. **Influence and Followers:** bullets of settled facts in plain sentences of ordinary length. Cover rank, what the faith offers or asks, clergy and orders, messengers and omens if sourced, holy days if sourced, relations with other powers, and origin or rise with each wiki fact tagged by edition or book. Do not pad; a thinly sourced power gets a short page. Merge fragments into full sentences. The pilot pages ran 9% to 12% of sentences at 7 words or fewer against a 4% target.
5. **The Using box** has the bullets in the brief. Fill every bullet from sources, or write the fixed fallback lines: "No warlock connection in the sources." and "No campaign file uses this power." The Waterdeep bullet states what the sources place in the city. Start from the Dragon Heist Major Temples table (below). A conflict goes in Draft Notes, with the campaign file winning.
6. **2024 mapping rules.** Cleric subclasses are Life, Light, Trickery and War. Divine Orders are Protector and Thaumaturge. Paladin oaths are Devotion, Glory, the Ancients and Vengeance. Warlock patrons are Archfey, Celestial, Fiend and Great Old One. Every mapping is `(derived)` and says how close the fit is. A 2014 domain that fits none of the four (Order, Tempest, Knowledge, Nature, Death, Arcana) is named, and the nearest fit is chosen with the reason given.
7. **Overview:** 2 to 4 plain sentences of public knowledge, about 21 words each at most, no punchline closer. It may carry GM information until the prose pass, except where a secrecy rule below applies.
8. **Cross-References:** bold names. A roster page that is not yet written is marked "(Deities, page planned)". A name with no page (a minor NPC, a power not on the roster) is plain text and is listed in Draft Notes. Check every Notable Figure and organization against `campaign/setting/`. Cite organizations as **The Order of the Gauntlet** (Organizations); the Factions Guide pages are being moved, so do not add "(Factions Guide)" references.
9. **Draft Notes** (deletable): conflicts with both `file:line` references, what is derived, what is `[research]`, names with no page, and what you left out and why.

## Dragon Heist: Major Temples of Waterdeep (`sources/adventure-wdh.json`, caption at line 30910)

| Deity | Temple | Location |
|---|---|---|
| All deities | Holyhands House | North Ward |
| All elven deities | Temple of the Seldarine | Castle Ward |
| Gond | House of Inspired Hands | Sea Ward |
| Helm | Helm's Hall | Southern Ward |
| Ilmater | Hospice of St. Laupsenn | North Ward |
| Lathander | Spires of the Morning | Castle Ward |
| Mielikki, Silvanus | Shrines of Nature | Sea Ward |
| Mystra | House of Wonder | Sea Ward |
| Oghma | Font of Knowledge | Castle Ward |
| Selûne | Tower of the Moon | Sea Ward |
| Sune | Temple of Beauty | Sea Ward |
| Tempus | House of Heroes | Sea Ward |
| Tymora | Tower of Luck | Castle Ward |
| Tyr | Halls of Justice | Castle Ward |
| Umberlee | The Queenspire | Beach |

Known conflicts for the hub and the pages: the Sea Ward text in the same chapter puts the Tower of Luck in the Sea Ward; the campaign's Order of the Gauntlet files put the Temple of Helm in the Castle Ward, against "Helm's Hall, Southern Ward" in the table; the table's "House of the Moon" and "Tower of the Moon" for Selûne differ between the text and the row. Say which source each page follows and put the other in Draft Notes.

## Binding campaign rules

- **Cassalanter secrecy.** Nobody outside the Cassalanter household and cult knows the family worships Asmodeus before the party finds out. No page's Overview or ordinary-Waterdhavian bullet may suggest otherwise. Jarlaxle knows through Vessa and tells Bregan D'aerthe members nothing unless they work it out. Cassalanter facts sit under `#### Secret` or `#### GM Notes`.
- **Bregan D'aerthe rejects Lolth.** No member worships her or invokes the Spider Queen with devotion. The Lolth page states this and quotes the campaign lines.
- **Names.** "Xanathar's Guild"; Xanathar is "it"; GM, never DM; no `.md` links or file paths in cross-references (file paths belong only in Source References and Draft Notes).
- **The campaign treats every power as present in 1492 DR.** A wiki-only death, abdication or ascension (4e) is history or a Draft Notes conflict. It does not change the page's present tense.
- **Invented lore is forbidden.** Mark gaps `[research]`. Paraphrase the wiki; never copy its prose.

## What to return

The report format in `setting-compendium-pass2-brief.md`: files written, facts you could not source, judgment calls where the template did not fit, conflicts with both `file:line` references, and the wiki pages and 5etools entries used. Also list any other file you found wrong (do not edit it). Do not commit. You have no shell, so say that `voicecheck.py` was not run; the main session runs it.
