# Setting Compendium Rebuild: Pass 2 (Deities) Brief

Binding brief for the Pass 2 researchers and drafters. It adds to the rebuild plan (`setting-compendium-rebuild-plan.md`, "Page rules") and the Pass 1 brief, and does not replace them. The approved model page is `campaign/setting/deities/asmodeus.md`. Copy its shape.

## Scope (decided Session 48)

The Deities journal is a **character-building reference** as well as a setting reference. A player building a cleric, paladin, warlock or any religious character must be able to browse it and pick a deity or patron. The user's rulings:

> "Everything plus hub, since it's not just for campaign relevant Deities. It's meant to be something that helps Clerics, paladins, warlocks and religious characters to choose their deity. This means that some other stuff may be needed, like a couple major archfey, a couple archdevils, a couple demon princes, some eldritch beings from the far realms. Use the wiki too." — User, Session 48

Corellon and Tiamat (and the other non-Faerûnian powers below) are in scope under the same ruling.

### Roster (72 new pages and the hub)

| Group | Pages | Source of the stat fields |
|---|---|---|
| **Faerûnian pantheon** (50 new; Asmodeus is done) | Akadi, Amaunator, Auril, Azuth, Bane, Beshaba, Bhaal, Chauntea, Cyric, Deneir, Eilistraee, Eldath, Gond, Grumbar, Gwaeron Windstrom, Helm, Hoar, Ilmater, Istishia, Jergal, Kelemvor, Kossuth, Lathander, Leira, Lliira, Lolth, Loviatar, Malar, Mask, Mielikki, Milil, Myrkul, Mystra, Oghma, Savras, Selûne, Shar, Shaundakul, Silvanus, Sune, Talona, Talos, Tempus, The Red Knight, Torm, Tymora, Tyr, Umberlee, Valkur, Waukeen | 5etools `deities.json`: FRHoF first (epithet, worshipers, plane, text), SCAG for alignment, domains and symbol |
| **Waterdeep's own** (1) | Siamorphe | Wiki and Dragon Heist only. She is not in `deities.json`; mark the stat fields `[research]` or take them from the wiki, tagged |
| **Heads of other pantheons** (8) | Corellon Larethian, Moradin, Garl Glittergold, Yondalla, Gruumsh, Maglubiyet, Tiamat, Bahamut | 5etools (MTF, SCAG, PHB 2014) plus the wiki |
| **Warlock and cleric patrons** (13), flagged as patrons, not deities | Archdevils: Mephistopheles, Mammon, Zariel. Demon princes: Orcus, Demogorgon, Graz'zt. Archfey: Titania, the Queen of Air and Darkness, Baba Yaga. Witch-queen: Iggwilv (added at the user's request, Session 48; her subclass fit is derived by the drafter). Far Realm: Ilsensine, Ghaunadaur, Tharizdun | Wiki only for the first ten (Iggwilv included). Ghaunadaur and Tharizdun also have 5etools entries. Ilsensine is wiki only |

The user said "a couple" of each patron kind, so three of each is the main session's choice. The user may swap any patron when reading the research report. Asmodeus counts as the fourth archdevil.

### Files

- Folder `campaign/setting/deities/`, flat, one file per page, kebab-case (`selune.md`, `the-red-knight.md`, `queen-of-air-and-darkness.md`, `grazzt.md`).
- Hub: `00-the-deities.md`, H1 "The Deities".
- Patron pages use the same folder and the same template, with the H1 unchanged and the Using box named `Using X as a Patron`.

## Page template

Deity pages follow `asmodeus.md` exactly, with these fixes learned from the pilot:

1. `# Name`, `> Structuring draft.`, the `> **[GM]**` Gamemaster's Summary, `**Purpose:**`.
2. Italic epithet line. It leads with the name most Waterdhavians use.
3. Metadata bullets, in this order: Title, Other Names, Pantheon, Areas of Concern, Domains, Symbol, Alignment, Plane, Typical Followers. No Appearance section.
4. One-line edict as a blockquote.
5. `## Influence and Followers`: bullets only. Cover rank, what the faith offers, worship and clergy, holy days if sourced, omens or messengers if sourced, relations with other powers, and origin or rise (wiki, edition tagged).
6. `> **[GM]**` `#### Using X as a Deity` box with these bullets, each answered from sources or marked `[research]`:
   - **The ordinary Waterdhavian's view:** how a sage, a priest or a bar regular talks about the power.
   - **Waterdeep:** temples, shrines and festivals in the city (published adventure and campaign files first, wiki second). Say plainly when there are none.
   - **A cleric PC:** the 5etools domains (SCAG, 2014) and the closest 2024 subclass among Life, Light, Trickery and War, marked `(derived)`. Name the Divine Order that fits.
   - **A paladin PC:** the oath that fits (Devotion, Glory, the Ancients, Vengeance), marked `(derived)`.
   - **A warlock PC:** which patron the faith or entity maps to (Fiend, Archfey, Celestial, Great Old One), marked `(derived)`. If a deity has no warlock connection, write "No warlock connection in the sources."
   - **Campaign ties:** which quest, faction or NPC uses this power, quoted from campaign files. If none, write "No campaign file uses this power."
   - **Never reveal:** only where a secret exists (Cassalanters, Zhentarim, Bregan D'aerthe's rejection of Lolth).
7. `## Overview`: 2 to 4 plain sentences of public knowledge. It may carry GM information until the prose pass.
8. `#### GM Notes` only where a campaign tie-in exists.
9. `**Tone:**`, `---`, `## Source References`, `## Cross-References` (bold names), then `#### Draft Notes` only if open items exist.
10. Cross-references to other powers use bold names and may point to pages that exist in this pass. Do not link to a page that is not on the roster.

Patron pages replace "A cleric PC" and "A paladin PC" with the warlock subclass first, then one line on cleric and paladin use if the power has any worshippers. Keep the box length to what the sources support. A page with little sourced material is short; do not pad it.

### Hub page (`00-the-deities.md`)

- Gamemaster's Summary, `**Purpose:**`, an opening of 2 to 3 sentences on how Waterdhavians treat their gods.
- **How to choose a deity** tables: by 5etools domain (SCAG), by alignment, and by the 2024 cleric subclass the page derives. One row per power. Link every row with a bold page name.
- **Waterdeep's temples** table (name, power, ward, source). Only temples a source places in the city. Start from the "Major Temples of Waterdeep" table in `sources/adventure-wdh.json` (caption at about line 30910; columns Deity, Temple Name, Location) and add campaign-file temples. Where the campaign or the wiki gives a different ward (Tymora's Tower of Luck, Helm's Hall), put both in Draft Notes; the campaign file wins.
- **The powers of other peoples** section: the eight pantheon heads, one row each.
- **Patrons** section: the thirteen patrons, grouped by 2024 warlock subclass, with one line on how they differ from a god.
- Overview, GM Notes, Source References, Cross-References.

## Rules that bind every researcher and drafter

1. **Rulings and secrecy.** The Cassalanter secrecy rule, Bregan D'aerthe's rejection of Lolth, "Xanathar's Guild" and Xanathar as "it" all apply. The Lolth page must say that Bregan D'aerthe rejected her. No Waterdhavian outside the household and the cult knows the Cassalanters worship Asmodeus.
2. **Sources rank** as in the plan: campaign files, the published adventure, the Alexandrian files, 5etools, then the wiki. The wiki covers every edition, so tag each wiki fact with the edition or book its page cites. Paraphrase the wiki; never copy its prose.
3. **No invented lore.** A fact no source supports is `[research]`. A derived fact (a 2024 subclass fit, arithmetic) is marked `(derived)`.
4. **2024 rules.** Domains from 5etools are 2014 and are labelled as such. Subclass advice is for the 2024 Player's Handbook.
5. **Voice.** Load `ember-voice`, `ember-setting-style`, `ttrpg-sourcebook-style`, `adventure-reloaded` and `foundry-journal`. The Overview is real prose; everything else is settled bullets.
6. **Names.** Check every NPC, faction and location against `campaign/setting/`. Quest names come from CLAUDE.md.
7. **Nothing else.** Drafters do not commit, do not edit files outside their assignment, and report conflicts with both `file:line` references.

## Research bundles

For each roster entry the main session pre-extracts a folder `research/deities/<slug>/` in the session scratchpad:

- `5etools.md`: every `deities.json` entry for the name (source, page, alt names, title, alignment, domains, symbol, worshipers, plane, text)
- `wiki.txt`: the wiki page's raw wikitext, redirects followed
- `campaign-hits.txt`: every line in `campaign/` that names the power, with `file:line`
- `adventure-hits.txt`: every line of `adventure-wdh.json` and `adventure-wdmm.json` that names it, with line numbers

Researchers read the bundle, then report. Wiki pages run up to 100,000 characters, so read them in chunks.

## Researcher report (per power)

Quotes are full and exact, with the file and line. Cover only these fields, so the report stays usable:

1. Identity: epithets, titles, alternate names, pantheon, plane, alignment, domains, symbol, typical followers (5etools, then wiki).
2. Edict or core tenet.
3. Portfolio and Areas of Concern.
4. Worship: clergy, holy days, temples, omens, messengers. Waterdeep specifics first.
5. Relations with other powers (allies, rivals), and origin or rise, each tagged with the edition the wiki cites.
6. Campaign and published-adventure mentions, quoted.
7. Conflicts between sources, and what was not found.

## Draft report (what the drafter returns)

- Files written (path and H1).
- Facts you could not source (`[research]` list).
- Judgment calls where the template did not fit.
- Conflicts between files, with both `file:line` references.
- Which wiki pages and 5etools entries were used.

## Available 2024 subclasses (ruled by the user, Session 48)

The Deities journal's cleric, paladin and warlock advice draws on every option below. Source: the 5etools class data (`class-cleric.json`, `class-paladin.json`, `class-warlock.json`). The user's ruling: "Anything that hasn't been reprinted yet goes into the available subclasses, except for Plane Shift subclasses. No Warcraft subclasses." So an older option is available only if no 2024 book has printed an equivalent. Where a 2024 version exists, use the 2024 version and drop the older one.

**Cleric domains (13):** Life (PHB 2024 p.73), Light (p.74), Trickery (p.75), War (p.76), Knowledge (Heroes of Faerun p.18), Grave (Ravenloft: The Horrors Within p.19), Arcana (Arcana Unleashed p.8), Nature (PHB 2014), Tempest (PHB 2014), Death (DMG 2014), Forge (Xanathar's), Order (Tasha's), Peace (Tasha's), Twilight (Tasha's).

**Paladin oaths (13):** Devotion (PHB 2024 p.113), Glory (p.114), the Ancients (p.115), Vengeance (p.116), the Noble Genies (Heroes of Faerun p.20), Oathbreaker (DMG 2014), the Crown (SCAG), Conquest (Xanathar's), Redemption (Xanathar's), the Watchers (Tasha's).

**Warlock patrons (10):** Archfey (PHB 2024 p.159), Celestial (p.160), Fiend (p.161), Great Old One (p.162), Undead (Ravenloft: The Horrors Within p.24), Vestige (Arcana Unleashed p.13), the Undying (SCAG), the Fathomless (Tasha's), the Genie (Tasha's), the Hexblade (Xanathar's).

Excluded: every World of Warcraft and Plane Shift: Amonkhet option; the 2014 Player's Handbook Life, Light, Trickery, War, Devotion, Ancients, Vengeance, Archfey, Fiend and Great Old One (2024 versions replace them); Xanathar's Celestial (the 2024 Celestial replaces it); Xanathar's Grave, Van Richten's Undead and Tasha's/SCAG Glory and Arcana (reprinted in 2024-format books).

The pages written before this ruling derive fits from the four 2024 Player's Handbook options only. A re-pass over the 72 pages and the hub is pending the user's go-ahead.
