---
name: dnd-monster-designer
description: Design custom Dungeons & Dragons 2024 (One D&D) monsters and creatures with full stat blocks, calculated Challenge Rating, and SRD-accurate markdown formatting. Use this skill whenever the user wants to create, build, design, stat out, homebrew, or balance a D&D monster, creature, NPC enemy, or boss — including requests like "make me a monster", "stat out a [creature]", "design a CR X boss", "homebrew a creature for my party", or "turn this concept into a stat block". Also use when converting a creature idea, piece of lore, or art into playable 2024 stats, or when checking whether an existing monster's CR is balanced. Defaults to D&D 2024 rules; flags 2014 differences when significant.
---

# D&D 2024 Monster Designer

Build monsters that are mechanically sound under D&D 2024 rules and a delight to run at the table. A good monster has a clear combat identity, threatens the party in interesting ways, and lands on a Challenge Rating you can defend with math.

Work through the ten design steps below in order, then verify CR and emit the stat block in the exact SRD markdown format. Show your CR math so the GM can tweak it.

## Workflow at a glance

1. Concept & target CR — establish the fiction and combat role first
2. Skeleton — size, type, alignment, speed
3. Ability scores — driven by fiction and comparison monsters
4. Armor Class
5. Hit Points
6. Attack bonus & save DC
7. Damage output (DPR across 3 rounds)
8. Actions, bonus actions, reactions, legendary/lair actions
9. Traits & special features
10. CR verification (defensive + offensive), then finalize

Then: run the sanity checks, format the stat block, and add lore + hooks outside the block.

---

## Step 1 — Concept & target CR

Before any math, answer:
- What does this creature *feel like* in play? (One evocative paragraph.)
- What CR range fits its role? Compare to a known monster if unsure.
- What is its **combat role**? Bruiser, Skirmisher, Controller, Artillery, Boss, or Minion.

CR is a hypothesis here — you confirm it in Step 10.

## Step 2 — Stat block skeleton

Assign in this order:
- **Type & Size** → determines Hit Die size (d4 Tiny → d20 Gargantuan; see `references/design_tables.md`)
- **Alignment** → a default suggestion, not a rule
- **Speed** → flying creatures may warrant an effective +2 AC if flight is abusable

## Step 3 — Ability scores

Official rules give no formula — use fiction and comparison monsters. Ask what the creature is *good* at (high relevant scores) and *bad* at (meaningful weaknesses add drama).

What scores affect: STR/DEX drive attack rolls and damage, CON drives Hit Points, and all six drive saving throws and skill checks. Adjust later if CR math drifts.

## Step 4 — Armor Class

Two valid methods: look up AC on the CR table and adjust for concept (stone = higher, clumsy beast = lower), or calculate from armor type + DEX modifier + natural armor.

Design notes: high AC is frustrating to fight; low AC means the monster dies before it shines. Match AC to narrative role. Add an effective +2 AC for CR purposes if the creature flies out of melee reach and the party lacks flight countermeasures, or if it has strong saves (3+ proficient save types).

## Step 5 — Hit Points

Two valid methods: use the CR table HP range (easy; good for home games), or calculate *(Hit Die average + CON modifier) × number of dice*. Hit Die by size is in `references/design_tables.md`.

Resistance/immunity adjustments (2024 standard): increase effective HP for physical (B/P/S) damage resistance or for 3+ damage immunities. Fewer immunities or non-physical resistances alone need no HP adjustment. For defensive features like regeneration or legendary resistances, compensate by lowering HP or AC rather than stacking power on top.

## Step 6 — Attack bonus & save DC

Attack bonus: use the CR table value, or calculate STR/DEX modifier + Proficiency Bonus. Save DC: use the CR table, or calculate 8 + relevant ability modifier + Proficiency Bonus.

Use a single primary ability for all DCs unless the fiction strongly demands otherwise — multiple DCs add cognitive load at the table.

## Step 7 — Damage output (DPR)

Calculate **average damage per round across 3 rounds**. This captures recharge abilities (used ~once per 3 rounds), situational features, and multi-target AoEs (assume 2 targets hit).

Scaling guidelines: for multi-target AoE, halve single-target damage as the per-target value; treat recharge/limited-use abilities as roughly 4× single-action damage. Be cautious with large AoEs — a 60 ft. emanation will likely hit the whole party, so adjust expectations. Prefer Multiattack for CR 3+ monsters: multiple smaller hits give more reliable DPR and a better play experience than one swingy big hit.

## Step 8 — Actions, bonus actions, reactions

Design **3–5 actions maximum** (battles last ~3–5 rounds). Every monster should have an effective melee option, an effective ranged option (unless concept forbids it), and at least one signature ability expressing its fiction.

Action economy checklist: a Bonus Action worth using every round? a meaningful Reaction (parry, counterattack, triggered ability)? For bosses, Legendary Actions (3 uses is standard) and/or Lair Actions?

Initiative (2024): consider giving cunning or elite monsters Proficiency added to Initiative. It doesn't change CR but meaningfully improves encounter pacing.

## Step 9 — Traits & special features

For each trait ask: how often will this matter in a typical encounter? does it affect survivability or DPR (if yes, adjust HP/AC or damage)? does it tell a story (vulnerabilities and immunities are most fun when discoverable)? Limit traits to those that actually come up in play — dead text clutters the block.

## Step 10 — CR verification

**Defensive CR:** find the HP row in the CR table, compare your AC to that row's expected AC, and adjust CR ±1 per 2 AC points of difference.

**Offensive CR:** find the 3-round average DPR row, compare your attack bonus (or save DC) to that row, and adjust CR ±1 per 2 points of difference.

**Final CR = (Defensive CR + Offensive CR) ÷ 2.** Then update Proficiency Bonus and XP to match, and revise skill bonuses and other PB-derived values accordingly.

The full CR Quick Reference Table (AC, HP, attack bonus, DPR, save DC, XP, PB, and example monsters per CR) is in `references/design_tables.md`. Read that file when verifying CR.

---

## Output format

Always present the stat block in the exact SRD 2024 markdown format. **Read `references/statblock_format.md` before emitting any stat block** — it specifies the ability-score table layout, inline italic notation (`*Melee Attack Roll:*`, `*Failure:*`, etc.), the omit-if-empty rules, the legendary action preamble, and the spellcasting block. Getting these details right is what makes the block compatible with VTT tools and indistinguishable from official content.

Inside the stat block: clean, precise, sourcebook authority — no fluff.

Outside the stat block, be a creative collaborator. After the block, provide:
- **CR math** — show the defensive/offensive breakdown so the GM can adjust
- **Lore, behavior, ecology** — a few sentences of flavor
- **Adventure hooks** — one or two ways to drop the creature into a game
- **Design notes** — flag any ability that borrows from or intentionally diverges from an existing 2024 monster, and warn about anything that might play awkwardly at the table

If a request is mechanically ambiguous or could break game balance, flag it clearly and offer a balanced alternative alongside the requested version.

## Design sanity checks

Before finalizing, confirm:
- [ ] Does the creature have something meaningful to *do* every round?
- [ ] Can it threaten both melee and ranged characters?
- [ ] Is there at least one ability that will surprise or delight players?
- [ ] Does it have a meaningful weakness or vulnerability?
- [ ] Is it fun to *run*? (Too many special rules = slow play.)
- [ ] Does the fiction match the math? (A stealthy assassin shouldn't have 200 HP.)
- [ ] Are limited-use abilities worth burning immediately? (If not, redesign them.)
- [ ] Would a DM running this cold know what to do on round 1?

## 2024 vs. 2014 divergences

Default to 2024 rules. Note differences when significant, and provide both versions if the divergence matters to the user.

- **Initiative:** 2024 monsters frequently add Proficiency Bonus to Initiative; use for cunning or elite creatures.
- **Saving throws:** 2024 stat blocks list save modifiers directly in the ability-score table row — no separate "Saving Throws" line. A non-proficient save equals the ability modifier; proficient saves are higher.
- **Nonmagical damage resistance removed:** 2024 eliminates the "from nonmagical attacks" qualifier. Monsters either have Resistance to Bludgeoning, Piercing, and Slashing damage or they don't — it applies against all sources, magical or otherwise. Never write "from nonmagical attacks" in a 2024 stat block.
- **Trivial on-hit saves removed:** in 2014, many attacks imposed conditions (Prone, Grappled, Restrained) or forced movement (push, pull) via low-DC saves. In 2024 these saves are dropped — the condition or forced movement applies automatically on a hit, typically gated by a size limit instead (e.g. "If the target is a Large or smaller creature, it has the Prone condition" or "the [creature] pushes the target up to 10 feet straight away"). Reserve saving throws for meaningful conditions (Frightened, Stunned, Paralyzed, Poisoned, Charmed) or actions where the save is the whole point (breath weapons, gaze attacks, AoEs). Rule of thumb: single-target melee hit → apply on hit; AoE or dedicated action → keep the save.
- **Damage immunities:** only lower HP when the creature has 3+ immunities OR physical (B/P/S) resistance. Fewer don't affect CR in 2024 design.
- **HP variance:** official 2024 monsters sometimes deviate from CR-table HP ranges. Trust the full offensive/defensive CR calculation over the table alone.
- **No spell slots, and spell lists are sharply curated:** 2024 monsters have no spell slots, spell levels, or prepared spell lists. All spellcasting is flat At Will or X/Day uses in a single Spellcasting action. Spell lists are trimmed to only the spells that matter in a fight — high-impact damage, key combat utility, and pre-combat self-buffs. The 2014 Archmage had 22+ spells across nine levels; the 2024 version has ~15, with low-level fillers and out-of-combat utility cut. Ask: *would a DM actually use this spell in a 3–5 round encounter?* If not, cut it. Cast a spell at a higher effective level via a named variant (e.g. *Lightning Bolt* (level 7 version)), not an upcast slot. High-use spells (Reactions, Bonus Actions like *Counterspell*, *Shield*, *Misty Step*) may be broken out of the Spellcasting action into dedicated entries.
- **Multiattack:** more monsters across more CR tiers use Multiattack in 2024 than in 2014.

## Reference files

- `references/statblock_format.md` — the exact SRD 2024 markdown template and all formatting rules. Read before emitting any stat block.
- `references/design_tables.md` — Hit Die by Size table and the full CR Quick Reference Table. Read when calculating HP or verifying CR.
