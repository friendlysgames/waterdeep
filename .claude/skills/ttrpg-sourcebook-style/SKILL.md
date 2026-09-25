---
name: ttrpg-sourcebook-style
description: >
  Write prose in the style of professional TTRPG sourcebooks and setting guides — authoritative, lore-dense, and consequence-layered. Use this skill whenever the user asks to write setting guides, world-building lore, location descriptions, faction overviews, NPC profiles, regional histories, quest hooks, or any narrative content for D&D, Pathfinder, or other TTRPGs. Also trigger when the user says "write this like a sourcebook", "make it sound official", "write lore for my setting", "describe this location for my campaign", or shares rough notes and wants them turned into polished setting prose. Use at any length — a single paragraph or a full chapter section.
---

# TTRPG Sourcebook Style

Write in the prose style of professional TTRPG setting guides and campaign sourcebooks. The goal is to match how these books write — their sentence construction, information layering, paragraph rhythm, and rhetorical habits.

---

## Sentence Construction

**Participial or prepositional openers are the default.**
Almost every paragraph begins with a subordinate clause or phrase before the subject arrives. This creates a sense of context-before-claim — the world exists before any single sentence describes it.

- *"Languishing in the withered shadow of its former glory, the empire is a land of relentless greed..."*
- *"Having once ruled the greatest stretch of territory on the continent, its influence still exceeds its current borders."*
- *"Reinforced and regularly repaired, the roads stand out among the crumbling buildings that surround them."*

**Sentences carry multiple clauses, linked by "which", "as", "while", "though".**
Information is stacked within sentences rather than broken apart. Subordinate clauses extend the main idea rather than start a new one.

- *"The city still has an ambition that its might can no longer support, which only serves to fuel the flames of grim, and ultimately futile, determination."*

**Short sentences are occasional pauses, not landing blows.**
A short sentence can mark a turn in events ("However, the war has largely drifted into the realm of myth."), but it carries information, and it never delivers a dramatic verdict. For this campaign, `ember-voice` sets the rhythm: about 5% of sentences at 7 words or fewer. "Then the plague came."-style punches are the pattern the user rejected as AI prose.

**Appositives and em-dash asides add texture mid-sentence.**
Rather than a new sentence, extra information is tucked in as an aside:

- *"—though it's debated whether her faith was genuine or a calculated manipulation—"*
- *"a feat of engineering unrivalled in the known world"*

---

## Information Delivery

**Every fact carries immediate consequence or implication.**
The style never states a bare fact alone. A location's geography immediately implies a danger, cost, or opportunity. A ruler's trait immediately implies how it affects their subjects. A resource implies who controls it and who wants it.

- Don't: *"The valley floods frequently."*
- Do: *"The valleys hidden within the deeper forest prove fatal — sudden flooding catches unwary travelers in a deluge that leaves no unceremonious grave, only a watery one."*

**Present decline is always visible alongside past glory.**
Even when describing something once great, its current degraded state is woven in. Past achievements exist in contrast with present failure, threat, or exhaustion.

- *"Though it remains the region's industrial heart, it now relies on imports for the raw materials it once harvested itself — a dependence that has weakened its borders and reduced the quality of its craft to an echo of former glory."*

**Competing forces are held in tension.**
Paragraphs frequently balance an opposing pressure: the road is dangerous, *but* merchants still use it. The army is depleted, *but* its reputation intimidates. This "and yet" rhythm recurs constantly and gives the world a sense of lived friction.

**Lists follow the content, not a rhythm.**
Enumerate as many items as the content has. Don't force a tricolon or build lists for escalation, because chanted triplets are an AI tell (see `ember-voice`). A natural list reads like this:

- *"they marched, negotiated, and conquered"*
- *"tools, machinery, and above all, weapons"*
- *"weary, outnumbered, and furious"*

---

## Header Hierarchy and Structure

Sourcebooks use headers to organize information into scannable layers — a GM should be able to open a page and immediately orient themselves. Structure content using three levels:

**H2 — Major categories.** The broadest divisions of a topic: `## Geography`, `## History`, `## Culture`, `## Notable Individuals`, `## Quest Hooks`. These define what *kind* of information follows.

**H3 — Named subdivisions.** Specific regions, eras, institutions, or groups within a major category: `### The Northern Reaches`, `### The Founding Age`, `### The Merchant Guilds`. These are the units a GM actually navigates to.

**H4 — Individual entries.** Named persons, specific locations, singular events: `#### Commander Aldric Vorne`, `#### The Sunken Quarter`, `#### The Night of Ash`. These are the smallest discrete units — referenced by name, looked up by need.

**The rule of three.** If a section has only one H3, fold it into the H2 prose. If an H3 has only one H4, fold the H4 into the H3. Headers should divide genuinely distinct content, not decorate single paragraphs.

**Headers carry no verbs.** They are nouns or noun phrases: `### The Eastern Roads`, not `### How the Eastern Roads Were Built`. The prose beneath does the explaining.

**Prose carries the connective tissue between sections.** The transition from one H3 to the next is handled by the final sentence of the outgoing section or the opening sentence of the incoming one — not a header alone. Headers divide; prose flows.

---

## Paragraph and Section Rhythm

**Paragraphs run 3–6 sentences.** Each develops one subject or consequence. Avoid one-sentence paragraphs used for emphasis; Ember almost never uses them (see `ember-voice`).

**Sections follow a general → specific → consequence arc.**
Open by establishing the overall condition of a place or faction. Zoom into specific geography, events, or individuals. Close on the present-tense implication — the unresolved tension, the current threat, the mood right now.

**Transitions use adversative connectors heavily.**
*"However," "Yet," "But," "Nevertheless," "Despite"* — the world constantly pushes back against expectation or progress.

**In-world quotes close sections.**
A short italicized quote, attributed to a named ordinary person (merchant, soldier, innkeeper, local guide), closes a section with a grounded, often wry human voice:

> *"Each village claims theirs is the safest road. None of them are wrong about the others."* — Traveling merchant

These quotes are brief (1–3 sentences), conversational, and slightly sardonic. They anchor the lore in lived experience without undercutting it.

---

## Clarity Over Atmosphere

Sourcebook prose is a functional document first. A GM may read it mid-session, under pressure, looking for a specific fact. Atmosphere serves the information — it never buries it.

**Lead with the fact, follow with the texture.** The reader needs to know what something *is* before they can appreciate how it feels. Establish the concrete reality first, then layer in tone.

- Don't: *"In the shadow of the crumbling spires, where crows circle and old sins linger, justice is administered."*
- Do: *"The city's magistrates hold court in the Spire Quarter, a district of crumbling towers at the district's eastern edge. Crows nest in the upper stonework. The trials are public and brief."*

**Flowery language earns its place.** Reserve elevated or metaphor-heavy prose for moments of genuine weight — a culture's defining contradiction, a location's singular strangeness, the emotional core of a history. Applying it uniformly dulls it to nothing.

**Sentences should pass the read-aloud test.** If a GM would stumble reading a sentence at the table, it is too long or too tangled. Subordinate clauses are fine; four of them chained together are not.

**Practical details are not beneath the prose.** Trade goods, travel times, who holds power, what people eat, how much things cost — these are the details that make a setting usable. State them plainly when they appear. A sentence like *"The road takes three days in good weather and five in bad"* does more work than a paragraph of atmospheric description of the same road.

---

## What to Avoid

- **Back-to-back subject-verb-object sentences.** Vary the opener every time.
- **Bare facts without consequence.** Every piece of information implies something about survival, power, danger, or change.
- **Passive voice as a default.** Use it occasionally for effect, not habitually.
- **Adjective stacking.** One precise adjective beats three vague ones.
- **Starting consecutive paragraphs the same way.** The opening word or phrase of each paragraph should vary.
- **Telling the reader how to feel.** Don't write "the city feels oppressive." Write what makes it oppressive and let the reader arrive there.

---

## Process

1. Identify the content type: place, person, faction, history, quest hook.
2. Establish the central tension or contradiction — what makes this interesting to a GM or player.
3. Draft with participial or prepositional sentence openers as the default.
4. Attach consequence to every fact.
5. Check the rhythm against `ember-voice`: long, accumulative sentences, with no punchy landing lines or one-sentence verdicts.
6. Close sections with an in-world quote if appropriate.
7. Return only the prose — no preamble or commentary unless the user asks.
