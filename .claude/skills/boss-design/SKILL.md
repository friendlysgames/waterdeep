---
name: boss-design
description: >
  Design D&D 2024 boss monsters using the Boss Design Framework: phased stat blocks, the
  expanded reaction system (replacing Legendary Actions), and the 27 boss archetypes across
  the three Boss Types (Tyrant, Commander, Shaper). Use this skill whenever the user asks to
  create, build, stat, convert, rebalance, or review a boss, BBEG, villain, final boss,
  campaign antagonist, lieutenant, solo monster, multi-phase fight, or "boss fight" of any
  kind — including when they name a Boss Type (Tyrant/Commander/Shaper), an archetype (e.g.
  Hunter, Fortress, Warlord, Swarm Lord, Form Shifter), a puzzle type (Exposure, Penetration,
  Targeting, Escalation, Vulnerability, Pace, etc.), or ask for "phases" or "reactions" on a
  monster. Also use it when converting an existing published monster (dragon, lich, vampire,
  etc.) into a boss-worthy encounter. Do NOT design a boss from memory or from generic
  Legendary Action conventions — this framework deliberately diverges from them.
---

# Boss Design (D&D 2024 — Boss Design Framework)

This skill builds bosses under a custom framework that **replaces standard solo-monster
design**. The two most important divergences from published 2024 monsters:

1. **Phases, not HP thresholds.** Every boss has 2–5 phases, each a complete behavioral
   replacement with its own independent stat block and its own full HP pool. Damage does not
   carry over between phases; conditions end at transition.
2. **Reactions, not Legendary Actions.** Bosses get 2 or 3 reactions per round (max 1 per
   turn), defined per phase, each with an explicit trigger. Effects that would deny all
   reactions instead cost the boss one reaction. Never give a framework boss standard
   Legendary Actions.

## Reference files

| File | What it contains | When to read |
|---|---|---|
| `references/framework.md` | The full framework: Boss Types, puzzle types, archetype structure (Defining Trait / Strength / Weakness), phase rules, reaction rules, Encounter Layers, encounter philosophy | **Always, first**, in full |
| `references/tyrant-archetypes.md` | The 9 Tyrant archetypes with design notes and fiction examples | When the boss is (or might be) a Tyrant |
| `references/commander-archetypes.md` | The 9 Commander archetypes | When the boss is (or might be) a Commander |
| `references/shaper-archetypes.md` | The 9 Shaper archetypes | When the boss is (or might be) a Shaper |
| `references/tyrant-templates.md` | Step-by-step build template per Tyrant archetype (High Concept → Tools → Attacks & Responses → CR Calibration → the Tell) | Once the archetype is chosen — read that archetype's section in full |
| `references/commander-templates.md` | Same, for Commander archetypes | Same |
| `references/shaper-templates.md` | Same, for Shaper archetypes | Same |
| `references/cr-math.md` | The 10-step CR/stat math process, 2024 stat block format, and the CR quick-reference table (AC/HP/attack bonus/DPR/Save DC/XP by CR) | Always, before writing numbers |
| `references/worked-example-strahd.md` | Annotated 3-phase Strahd build showing every framework principle applied, with full stat blocks | When unsure how a finished boss should look; when the user asks for an example or a conversion of a published monster |

The template files are large (1,100–1,300 lines). Do not read them whole. Locate the chosen
archetype's section with `grep -n "^## " <file>`, then `view` only that section's line range.
The archetype files (~300 lines) can be read in full.

## Workflow

### 1. Establish context
Gather (or infer, stating assumptions): party level and size (default 4), the boss's
narrative role and campaign weight, tone, and any concept the user already has. Campaign
weight drives **phase count** (2 = notable, 3 = arc villain, 4–5 = campaign-defining) and
**reactions per round** (2 or 3).

### 2. Choose the Boss Type
The Type is the *cognitive demand* on the players, chosen first and committed to:

- **Tyrant** — a path challenge: the party must discover the correct, non-obvious way to
  fight it. Puzzle types: Exposure, Access, Penetration, Endurance, Attrition.
- **Commander** — a priority challenge: the party must triage competing threats/objectives.
  Puzzle types: Targeting, Crisis, Sacrifice, Division, Escalation.
- **Shaper** — an adaptability challenge: the party must change tactics as the boss or
  battlefield changes. Puzzle types: Terrain, Vulnerability, Opportunity, Pattern, Pace.

Then choose the **Encounter Layer** (Combat is the default; Roleplay and Exploration are
valid — see framework.md). Hybrid Types and Type-shifts between phases are advanced options,
not defaults.

### 3. Choose the archetype
Every archetype = three puzzle types in fixed roles: **Defining Trait** (the wall),
**Strength** (the urgency that punishes not solving it), **Weakness** (the inverted payoff,
gated behind the Defining Trait). Quick index — confirm details in the archetype file:

**Tyrant** (by Defining Trait source):
- Offensive: **Hunter** (elusive predator that dictates engagement), **Juggernaut**
  (catastrophic hits + sustain loop that must be broken), **Executioner** (relentless
  attack volume that must be disrupted)
- Defensive: **Fortress** (impenetrable defenses + a ticking secondary threat), **Phantom**
  (attacks won't connect; controls engagement rhythm), **Shield Master** (absolute guard
  that punishes wrong attacks; never moves)
- All-Rounder: **Trickster** (decoys/illusions with a finite bag of tricks), **Warlock**
  (ranged attrition; collapses once distance is closed), **Duelist** (reads and counters
  everything until its read is overwhelmed)

**Commander** (by pressure source):
- Field: **Warlord** (distinct units, kill-order puzzle), **Puppet Master** (hidden
  hierarchy among threats), **Coordinator** (mutually supporting positions)
- Siege: **Ritualist** (multiple independent processes on timers), **Swarm Lord**
  (multiplying force; find the growth engine), **Saboteur** (simultaneous strikes on
  distributed positions with permanent losses)
- Leverage: **Field Marshal** (forced deliberate sacrifice of valued objectives),
  **Spymaster** (real crises hidden among misdirection), **Taskmaster** (an operation that
  gets *smarter* every round)

**Shaper** (by locus of flux):
- Environmental: **Environment Master** (arena in constant authored transformation),
  **Accelerator** (compounding tempo; find space to act), **Transformer** (boss actively
  builds the battlefield against the party)
- Morphic: **Form Shifter** (rotating vulnerabilities with legible signals), **Reverser**
  (inverts the party's actions against them), **State Shifter** (discrete states; the
  puzzle is timing the windows)
- Cascading: **Dynamic** (multi-dimensional pattern under pace pressure — climactic
  encounters only), **Randomizer** (opportunity stream, real vs. trap), **Adapter**
  (reconfigures in response to the party's own choices)

If the user's concept doesn't clearly map, present 2–3 candidate archetypes with one-line
reasoning and let them pick.

### 4. Build with the template
Read the chosen archetype's template section and follow its four steps in order: **High
Concept** (an epithet, not a tactic), **Tools & Features**, **Generate Attacks & Responses**
(Actions / Bonus Actions / Reactions with explicit triggers), **Calibrate CR**. Repeat the
behavioral design per phase — each phase is an independent stat block sharing only ability
scores, saves, skills, resistances/immunities, senses, languages, CR, and PB. Distribute
0–2 Legendary Resistances per phase from a total budget. Design the phase sequence as an
arc (escalation, desperation, or transformation).

**Write the Tell before the stat block.** Every archetype's template ends with a Tell — a
plain-language sentence stating what the boss always does and what players can exploit. The
puzzle must be solvable from in-fight observation within roughly two rounds, never from
out-of-game knowledge. If you cannot write the Tell, the design isn't done.

### 5. Calibrate the math
Use `references/cr-math.md`: target the CR row for AC/HP/attack bonus/Save DC/3-round DPR,
then verify Defensive CR and Offensive CR and average them. Boss-specific adjustments:

- Each phase is calibrated near the target CR on its own; the multi-phase structure is the
  boss's "solo monster tax" — do not also inflate a single phase's HP to solo levels.
- Evasive/untouchable archetypes (Hunter, Phantom, Warlock) carry effective AC above their
  listed AC — set defensive stats conservatively (high AC *or* high HP, not both).
- Solving the Defining Trait should visibly flip the math: the Weakness must produce a felt
  DPR or durability drop, not just a narrative beat.
- State CR, XP, and the key math (expected HP/AC/attack bonus/DC/DPR per phase) outside the
  stat block so the GM can tweak.

### 6. Apply the encounter philosophy
From framework.md: **spread damage** — never stack more than one damaging feature on the
same target in the same boss turn (Multiattack hits different players; AoE, conditions, and
control are exempt). Failure must teach, not just punish. For Shapers, build phase/state
tracking into the stat block itself — never rely on the DM's memory mid-combat.

### 7. Present the result
Deliver, in order: (a) a short concept paragraph and the archetype table (Defining Trait /
Strength / Weakness with expressions); (b) the Tell, stated plainly for the DM; (c) the
shared statistics block; (d) each phase's stat block in the 2024 format from cr-math.md,
with reactions listing explicit triggers; (e) CR math shown; (f) running notes — round-one
behavior, how the puzzle teaches itself, common pitfalls, and one tuning lever up and down.
Match the structure and annotation style of `references/worked-example-strahd.md` when the
user wants the full treatment.

## Guardrails

- Never substitute standard Legendary Action blocks, mythic traits, or 2014 conventions for
  the phase/reaction system unless the user explicitly asks for a non-framework boss.
- Archetype names describe combat identity, not creature type — any creature can wear any
  archetype.
- Flag anything that diverges from the framework or from 2024 baselines, and offer a
  balanced alternative alongside any deliberately unbalanced request.
