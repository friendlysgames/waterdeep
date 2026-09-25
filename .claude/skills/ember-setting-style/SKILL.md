---
name: ember-setting-style
description: >
  Ember-derived voice and sentence-level style for SETTING and GM GUIDANCE TEXT in the Waterdeep
  campaign: lore, history, myths, deities, organizations, Notable Figures pages, ward and location
  gazetteer entries, the Players' Guide, the GM Guide, the Trollskull Manor Guide, and rules
  explanations. Load alongside ttrpg-sourcebook-style (which keeps authority over sentence craft,
  consequence-layering, and header discipline) whenever drafting or revising anything under
  campaign/setting/ or campaign/guides/. Structure comes from adventure-reloaded; this skill governs
  voice per audience, entry shape, secrets handling, and GM-advice register.
---

# Ember Setting & GM Guidance Style

This skill captures how the Ember campaign writes its Setting Compendium, Gazetteer, Players' Guide, and Gamemaster's Guide, adapted to Waterdeep and this project's rules. It is a **voice layer**. It runs in parallel with two other skills and does not replace either:

| Skill | Owns |
|---|---|
| `adventure-reloaded` | Page architecture (NPC page, Organization page), GM zones, callout syntax, Milestone Points |
| `ember-voice` | **Sentence-level voice for everything**: rhythm and length targets, the AI-tell catalogue, setting and guide voice with verbatim Ember examples, `voicecheck.py` |
| `ttrpg-sourcebook-style` | Sentence construction, consequence-layered facts, tension, header discipline, clarity over atmosphere |
| **`ember-setting-style`** | The four audience voices, entry shape and information order, the historian aside, secrets handling, GM-advice register, gazetteer conventions, naming and dating |

**Precedence when they disagree:** how sentences sound (rhythm, length, tells) → `ember-voice`, which you should load first. Page structure → `adventure-reloaded`. Sentence craft → `ttrpg-sourcebook-style`, except for the first-sentence rule in Section 3 below, where this skill wins. Voice, audience, and entry order → this skill. CLAUDE.md rules (Players'/GM superset split, zero-prep, no dice, structuring-draft limits) override all three.

For adventure scenes (events, keyed rooms), use `ember-adventure-style` instead.

---

## 1. Four Audiences, Four Voices

| Text | Narrator | Addresses | Tense | Register |
|---|---|---|---|---|
| Lore (history, myth, deity, organization, place) | Confident third person, with an in-world historian's signed asides | No one directly | Past for history; present for current state | Grave, played straight |
| Historian aside | The in-world historian, first person | The reader, as a colleague | Mixed | Wry, personal, opinionated |
| GM guidance | The design team, "we" | The GM as "you" | Present | Collegial, explanatory, direct |
| Players' Guide | The design team, "we" | The player as "you"; the PC as "your character" | Present | Warm, inviting, occasionally exclamatory |

Never let the voices bleed. GM advice does not slip into lore narration, and lore does not break to explain a rule.

---

## 2. Lore Voice

**Played straight.** History, myth, and faction lore are grave. No narrator wit, no winking, no modern idiom. Wit is allowed in three places: the historian aside (Section 5), the closing line of a minor NPC blurb, and the dry, gentle humour of Notable Figures personality prose ("it was little surprise to anyone when he was found quite dead amidst a mountain of books").

**Confident by default.** State present-day and recent facts without hedging. Uncertainty is marked **claim by claim**, with a fixed set of constructions, never spread across a whole passage:

| Construction | Use |
|---|---|
| "It is said that …" | Folklore attached to one claim |
| "It is rumored that … but [she] staunchly denies this." | A rumor about a living person, paired with their denial |
| "Some say … Others hold …" | Two competing folk accounts |
| "Scholars debate whether …" / "Sages of Candlekeep dispute …" | An open academic question |

**Myths are told straight; the doubt goes at the end.** A myth or legend entry narrates its story without in-text hedging. Its reliability disclaimer lives in the closing `## Overview`: *"Modern scholars dispute many of the place names and peoples involved, as they no longer exist and may have been fictitious additions to the legends."*

**Deep past is flagged once.** For the oldest eras (pre-Netheril, the Crown Wars), one sentence at the top of the section sets the reliability level. The prose then proceeds without repeating it.

**PG register, even for horror.** Ember reaches for *terrifying, cataclysmic, unimaginable* and never for shock language or gore detail.

---

## 3. First Sentences and Paragraph Flow

**The first sentence of every entry names the subject and its category.** This overrides `ttrpg-sourcebook-style`'s participial-opener default, for the entry's opening sentence only:

> *The Sanguinaries are far smaller in number than the Cindaric Sages, with little influence beyond a handful of scattered pockets across the known world.*
> *Brevin is one of the first of a new type of settlement known as "seed settlements."*
> *The Vile Dragon known as **Zerranyss** is the principal antagonist and central villain of our story.*

Waterdeep form: *"The Xanathar Guild is the largest criminal organization in Waterdeep's sewers, and the only one run by a beholder."*

After the first sentence, `ttrpg-sourcebook-style` governs participial and concessive openers and consequence-layering, and `ember-voice` governs rhythm: long, accumulative sentences of 25–35 words, and no short landing sentence.

**Ember's favorite concessive frame** opens later paragraphs: *"Though small and scattered, the Sanguinaries take an active role …"* / *"Despite creating these precautions, most in Brevin don't think about them."*

**Transitions are plain temporal or causal connectors**: *During this time, After the Spellplague, As a result, Meanwhile, Over time.* No rhetorical hooks between paragraphs.

**Sections close on present tension**, never a recap. History ends on the open mystery. Organizations and places end on the looming conflict: *"there are rumblings of disagreement between those who favor … and those who want …"*

**Carry one governing metaphor through a place's culture writing.** Brevin is a grown town, so its politics "resemble the intertwining vines," its social groups are "branches," and its resilience is "a sick plant staked to a healthier one." Pick the image that defines a ward or faction and let it return in each Life subsection. Use one image per entry.

---

## 4. Entry Shape: Overview Last

Ember's most consistent rule: **the body builds toward a dense `## Overview` paragraph at the end of the page.** The Overview restates the whole subject in 3–6 sentences, like a back-cover blurb. It is the mandatory minimum: a stub page is an Overview and nothing else. (This matches the NPC and Organization page shapes in `adventure-reloaded`.)

General order for any lore entry:

1. **H1 title.** Deities add an italic epithet line beneath (*The Morninglord*).
2. **Metadata**, as terse key-value fragments, not sentences. Deity: Areas of Concern / Domains / Symbol. Myth: Origin / Knowledge (who knows it). Historical figure: Occupation / Period / Affiliation.
3. **Motto or edict** (deities, some factions): a single imperative sentence as a blockquote. *Protect those in need.*
4. **Opening narrative**, 2–4 paragraphs: nature, personality, current situation.
5. **Historian aside** (Section 5), after the first one or two paragraphs.
6. **H2/H3 subsections**, general to specific.
7. **GM Notes** (Section 6), after the player-safe narrative.
8. **`## Overview`**, always last in lore; last before the Read Aloud in gazetteer entries (Section 9).

**Faction tenets** are bullets with **bold defined-term lead-ins**, each followed by 2–3 full sentences:
> - **The Burden of Truth:** The Sanguinaries differ from the Sages in one crucial way: they believe the Heart of Ember is dying. This conviction is the cornerstone of their faith …

**History and myth entries** open with a GM-only **Lore Summary**: 3–6 bullets of what is actually true, placed before the prose. The prose that follows is written for a mixed audience.

---

## 5. The Historian Aside

Ember's signature device is the in-world historian's **signed first-person aside**. Ember's historian, Laeora, personally knew gods and heroes; her notes interrupt the third-person account like marginalia:

> *I've often spoken with Alar about her own creation … She believes she was formed before the Weave even took shape, speaking of those void-black memories with a terrifying glint in her golden eyes.*
> *~Laeora*

**In this campaign the historian is Volothamp Geddarm**, the author of *Volo's Guide to Monsters*, who appears in the Yawning Portal at the campaign's opening. His asides are vain, well-traveled, name-dropping, and not always reliable. That suits a campaign about secrets.

Rules:
- **At most one aside per major entry** (deity, faction, ward, era). None on minor entries.
- Placed **after one or two paragraphs** of third-person narration, as a blockquote signed `~Volo`.
- 1–4 sentences, first person, with a personal detail the third-person prose could not know or would not say.
- The aside **never contains a GM secret**. Players may read it. Volo may be wrong; the GM Notes say where.
- The aside replaces the closing folk quote from `ttrpg-sourcebook-style` on any entry that has one. Use one in-world voice per entry, not two. Gazetteer places and minor entries keep the folk quote if they need an in-world voice.

---

## 6. Secrets

Ember separates hidden truth in three strengths. Use the lightest one that fits:

| Strength | Mechanism | Holds |
|---|---|---|
| Light | **GM Notes**, a `> **[GM]**` callout headed `#### GM Notes`, after the player-safe prose | Origins, deeper history, how the thing actually works |
| Strong | A `> **[GM]**` callout headed `#### Secret` | A consequential hidden fact that changes play: a faction's internal fracture, a species' vulnerability. Reserve it: only a handful of pages in the whole setting should have one. |
| Page-level | A spoiler warning at the top (see Section 7) | Pages that are plot-critical throughout: the villains page, the adventure summary |

Phrasing:
- GM Notes state the truth flatly and in past tense for origins: *"The origins of the Sanguinaries trace back nearly three centuries to Darik Melsbow …"*
- Ember rarely uses "Unbeknownst to …" (three times in the corpus). Prefer a direct GM Notes reveal.
- Ongoing intrigue gets a **Timeline** inside GM Notes: dated one-sentence entries in DR, oldest first.
- **Superset rule** (CLAUDE.md): everything in a Players' Guide page appears in its GM counterpart. Secrets exist only in the GM version.

---

## 7. GM Guidance Voice

Ember's GM Guide talks to the GM as a colleague.

- **"You" and "we."** *"As the Gamemaster, you have access to a number of details about Events which are not available to players."* The design team is "we": *"we recommend," "we encourage," "we want."* Never "the GM should," and never "the DM may wish to."
- **State the reasoning.** Every rule or recommendation gets its *why* in the same paragraph, often framed as an ethos: *"We ultimately want to maintain an ethos that Cosmological Attunement is something very special."* A rule without a reason is incomplete.
- **Imperatives for procedure, prose for concepts.** Step-by-step procedures are numbered lists of terse imperatives. Conceptual explanation (why the four villains run simultaneously, how escalation feels at the table) is paragraphs.
- **Spoiler warning, two beats, same wording every time.** Beat one says spoilers follow and recommends reading. Beat two offers the opt-out:
  > *This page contains significant spoilers for the campaign. We recommend reading it so that you understand the primary villains and their motivations. Some Gamemasters, however, may prefer not to have this full knowledge, so proceed only if you wish to have all the available information up-front instead of learning things as you play.*
- **Rules Override.** When a house rule supersedes 2024 RAW (Milestone Points replacing XP, instant level-up), flag it under a label reading **Rules Override** and say so outright: *"These rules supersede and replace those written in the Player's Handbook."* Never change a rule silently.
- **Advice about players stays mechanical and practical.** Ember's cautions are about pacing and meta-gaming: *"this should be done very sparingly to avoid meta-gaming and compromised player choices."* The session-zero and safety-tool material in this campaign is project content. Write it in this same collegial "we recommend … because …" register.
- **Villain pages** open with the villain's one-line identity and core motive, then the goals as a bulleted list of verb-first objectives (*Seize control over …*, *Locate …*, *Obtain …*), then the lieutenants as one-line bullets (*Serethus, an ingenious alchemist and leader of the nefarious Mutagists.*).
- **Zero-prep holds here too.** "We encourage" is for approach and tone. It never hands off a decision the text should make.

---

## 8. Players' Guide Voice

- **"You" and "your character,"** warmer than the GM Guide. An exclamation point is allowed at a welcome or a genuine highlight. Never more than one per page.
- **Declare the spoiler policy once.** Ember states the player/GM split a single time on the Setting Overview page (*"Player sections contain information generally known by most inhabitants … Gamemaster sections contain more specialized information known only to select individuals"*). It is not repeated per page. Our equivalent lives in `about-this-campaign.md`.
- **Rules as concrete gameplay statements.** Bulleted, with parallel bold lead-ins and a short clause each: *"**A substitute for a Skill Check** …"*, *"**A bonus to a Skill Check** …"*. Players are told what they can do, not given abstract mechanics.
- **Setting content is the in-world common-knowledge tier:** what an ordinary Waterdhavian knows. No GM Notes, no Secrets, no historian aside that hints at a secret.

---

## 9. Gazetteer and Location Entries

Ward, district, and settlement entries follow a fixed shape:

1. **GM Summary** (`> **[GM]**`): where it is, which quests and events feature it, which Location Journal maps it. Terse and functional.
2. **Hook paragraph**: the place's single defining visual or conceptual idea, stated first. *"Brevin is one of the first of a new type of settlement known as 'seed settlements.'"*
3. **At a Glance**: key-value fragments, fixed order: Type, Size (population range), Primary Peoples, Languages, Religion, Governance, Architecture, Economy, Organizations. No sentences.
4. **Secret**, if any (Section 6).
5. **Landmarks**: each entry is `**Name** — Type` followed by 1–3 sentences, in this order: what it is, who runs it, one hook or rumor.
   > **Nectar** — Tavern. A flower-themed bar where all drinks are sipped from inside living flower glasses. … The bar keeps a detailed map of where Nectar Glass flowers have been found, and can be a good place to learn local gossip.
6. **Characters of Interest**: `**Name** (Alignment, Species, pronouns)` followed by one compressed paragraph: backstory, current role, one telling detail. **Minor comic NPCs close on a zinger**:
   > *Daughter of Sevali Waterborne, Felisa was forced out of the family distillery and into food service to teach her a valuable lesson in humility. She has not learned it — nor how to properly pour an ale.*
   Serious NPCs close on their want or their secret tension instead: *"They've turned a blind eye to the misdeeds of their child, unwilling to believe that they've turned to a life of crime."*
7. **Life in [Place]**: an opening paragraph on who lives here and the current tension, then H3s drawn from **Culture, Defense, Politics, Economy, Lore**, using only those that apply. The governing metaphor (Section 3) carries through them.
8. **`## Overview`**
9. **Read Aloud**, always the final element. It is the most lyrical prose on the page: sensory first (smell or sound, then sight), resolving slowly into the shape of the place, ending on a small sign of life.
   > *The smell of fresh-tilled soil heralds the appearance of a knotted grove of stumpy, interlocked trees … Only gradually does this mass of greenery resolve into the shape of a village … Small heads poke out from behind leaves and flowers, as if in greeting.*

**Rumors are embedded, not listed.** Hooks live inside landmark and character blurbs ("can be a good place to learn local gossip," "It is rumored that …"). No separate Rumors table unless a quest document calls for one.

---

## 10. NPC and Historical-Figure Prose

The page layout comes from `adventure-reloaded`. Ember adds:

- **Personality in full sentences, never keyword strings.** *"Despite his brilliance, he was also said to be a cantankerous, lecherous, and thoroughly dislikable character who often clashed with other members."*
- **The name tag comes right after the name**, in the order alignment, species (with origin if it matters), pronouns: *Avwynn Taol (Neutral Good, Maziran Human, she/her)*. Take all three from the NPC's existing page. Never infer pronouns.
- **Relationships are about tension.** Each connection names who, why, and what is unresolved between them. A relationship that is only "they are friends" is incomplete.
- **Historical figures** get the metadata line (Occupation / Period / Affiliation) and are narrated in past tense, then close on their legacy in the present.

---

## 11. Naming, Terms, and Dates

- **Invented and campaign-specific terms are capitalized, not italicized:** the Grand Game, the Stone of Golorr, the Eyes, the Masked Lords, the Open Lord, Founders' Day, Faction Response Teams, Milestone Points, Renown, the Dragonward. Capitalization is the glossary.
- **Italics** are for book titles (*Volo's Guide to Monsters*), deity epithets under a title, magic items per `dnd-adventure-text`, and single-word stress inside quoted speech.
- **Compound identities** are capitalized as a unit: *Waterdhavian Human, Calishite Human, Menzoberranzan Drow.*
- **Dates** use Dale Reckoning: *1492 DR*. Spell out durations and ages in prose (*nearly three hundred years*, *two and a half centuries*). Numerals are only for DR years, populations, and distances.
- **Population ranges and map references** appear only in At a Glance and GM Summary blocks, never inline.
- **Bold** marks names on first substantive mention and the lead-ins of defined-term bullets. Never general emphasis.
- **Tables** only for truly tabular data: ranks, progression, cross-references. Prose is never bulleted except tenets, goals, and lieutenant rosters.

---

## 12. Absences

Ember never does these. Do not invent them:

- Dice or random tables for GM use (matches the project's no-dice rule)
- Narrator jokes or modern idiom in lore
- Hedging across a whole passage (mark uncertainty claim by claim)
- Silent rule changes (always label a Rules Override)
- A rule with no stated reason
- Rumor tables detached from places and people
- More than one historian aside per entry

---

## 13. Process

1. Identify the audience (lore / GM / player) and pick the voice from Section 1.
2. Confirm the page shape from `adventure-reloaded`. For lore and gazetteer entries, lay out the order from Section 4 or Section 9.
3. Write the identity first sentence (Section 3). Then draft with `ttrpg-sourcebook-style` sentence craft.
4. Mark uncertainty claim by claim, and move myth doubt into the Overview.
5. Place any historian aside, keeping it free of secrets. Put hidden truth in GM Notes or a Secret.
6. For GM guidance, pair every recommendation with its reason, and label any Rules Override.
7. Write the `## Overview` last, and check it could stand alone as the whole page.
8. Run `python3 .claude/skills/ember-voice/scripts/voicecheck.py <file>` and fix every TELL.
9. Run the CLAUDE.md prose pipeline (`deslop-text` + `no-ai-slop` → `humanize-prose`). The historian aside and quoted speech count as character voice for the dialogue exemption.
