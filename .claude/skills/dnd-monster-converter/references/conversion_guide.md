# Converting Monsters from D&D 2014 to D&D 2024

A practical field guide for updating homebrew and third-party stat blocks to the 2024 standard. Work through the sections in order — most conversions are mechanical find-and-replace, but a few require judgment calls that are flagged below.

---

## At a Glance — What Changed

| Element | 2014 | 2024 |
|---|---|---|
| Stat block layout | Two-row score/modifier table | Three-column table with MOD and SAVE columns |
| Saving throw proficiencies | Separate "Saving Throws" line | Folded into the ability score table |
| Initiative | DEX modifier only | DEX modifier + optional Proficiency Bonus |
| Legendary Actions | Cost-based; long boilerplate | Uses-based; shorter italic preamble |
| Lair Actions | Separate section in sourcebook | Referenced in CR line and Legendary Resistance trait |
| Attack notation | "Melee Weapon Attack: +X to hit" | "*Melee Attack Roll:* +X" |
| Save notation | "DC X [Type] saving throw. On a failed save..." | "*[Type] Saving Throw:* DC X... *Failure:* ... *Success:*..." |
| Trivial save vs. condition on hit | Save (e.g. STR DC 11) to avoid Prone, push, or pull on a hit | Condition/forced movement applied automatically on hit — no save |
| Resistances/Vulnerabilities | Two separate lines | **Resistances** and **Vulnerabilities** — omit each if empty |
| Nonmagical damage resistance | "Resistance to Bludgeoning, Piercing, and Slashing damage from Nonmagical Attacks" | Plain `**Resistances** Bludgeoning, Piercing, Slashing` — the nonmagical qualifier is removed |
| Immunities | One line mixing damage and conditions | **Immunities** line; damage types listed before conditions, separated by semicolon |
| Gear | Not a standard field | **Gear** line for retrievable equipment |
| Spellcasting | Innate Spellcasting + Spellcasting (two traits) | Single **Spellcasting** action with At Will / X/Day blocks |
| CR line format | `Challenge X (Y XP)` | `**CR** X (XP Y,YYY; PB +X)` — lair XP variant if applicable |
| HP immunities affecting CR | 1+ immunities reduced effective HP | Only 3+ immunities OR physical (B/P/S) resistance adjusts effective HP |

---

## Lessons from Official Conversions

When Wizards converts its own 2014 monsters to 2024, the *format* changes are mechanical, but the *balance* changes reveal a consistent design philosophy. These four judgment calls, drawn from comparing official 2024 conversions (notably Strahd von Zarovich) against their 2014 originals, should guide your own work. Each is detailed in the relevant step below.

1. **HP rebuilds upward for bosses.** Don't just copy the 2014 HP. Solo creatures get more — official Strahd went 144 → 204. Bias toward the upper end of the CR table's HP range for anything meant to fight a party alone. (Step 1)
2. **Stay literal on saves.** Convert the save proficiencies the source block actually had. Don't copy a similar 2024 monster's save spread — official Strahd kept only Dex/Wis and left Con/Cha unproficient despite the generic Vampire being proficient in them. (Step 2)
3. **Nonmagical resistance has a release valve, and bosses use it.** "B/P/S from nonmagical attacks" can either become full physical resistance *or* be dropped entirely. Official Strahd dropped it (keeping only Necrotic resistance) and took the larger HP pool instead. Prefer dropping it for creatures the party will fight with magic weapons. (Step 4)
4. **Heavy on-hit effects keep their save.** The "drop trivial saves" rule is only for minor riders like Prone. Severe effects — life drain, max-HP reduction, save-or-suck — keep a save sized to the effect. Official Strahd's Bite uses a CON save (DC 17), gated behind a grapple. (Step 8)

---

---

## Step 1 — Reformat the Stat Block Header

**2014 format:**
```
NAME
Size Type, Alignment
Armor Class X (source)
Hit Points X (XdY + Z)
Speed X ft.
```

**2024 format:**
```
### Name

*Size Type (Tag if any), Alignment*

**AC** X **Initiative** +X (Score)

**HP** X (XdY + Z)

**Speed** X ft.
```

Changes to make:
- Name becomes an `###` H3 header.
- Size/type line is italicized. If the creature has a descriptive tag (e.g. *Demon*, *Chromatic*), add it in parentheses after the type.
- **AC** and **Initiative** go on one line. The value in parentheses after the Initiative modifier is the flat Initiative score (modifier + 10), used instead of rolling.
- **HP** gets its own line — number first, dice expression in parentheses.

**HP often rebuilds upward — don't just copy the 2014 number.** A literal die-count conversion preserves the old HP total, but 2024 design tends to give solo monsters and bosses noticeably more HP so they survive a full party's action economy. The official 2024 Strahd jumped from 144 HP (17d8 + 68) to 204 HP (24d8 + 96) — a ~40% increase — and this extra durability was partly a trade for dropping his nonmagical physical resistance (see Step 4). When converting a boss or any creature meant to fight a party solo, check its HP against the CR Quick Reference Table's range for its CR and bias toward the upper end, especially if you are also removing a defensive trait. For rank-and-file monsters fought in groups, a literal HP conversion is usually fine.

---

## Step 2 — Rebuild the Ability Score Table

**2014 format:**
```
STR     DEX     CON     INT     WIS     CHA
21 (+5) 9 (−1)  15 (+2) 18 (+4) 15 (+2) 18 (+4)
```
Saving throw proficiencies appeared on a separate line:
```
Saving Throws Int +8, Wis +6, Cha +8
```

**2024 format:**

The saving throw proficiencies are folded directly into the table. Each score gets a MOD column and a SAVE column. Non-proficient saves equal the MOD exactly; proficient saves are MOD + Proficiency Bonus.

```
|            | MOD  | SAVE |            | MOD  | SAVE |            | MOD  | SAVE |
| :--------- | :--- | :--- | :--------- | :--- | :--- | :--------- | :--- | :--- |
| **Str 21** | +5   | +5   | **Dex 9**  | −1   | −1   | **Con 15** | +2   | +2   |
| **Int 18** | +4   | +8   | **Wis 15** | +2   | +6   | **Cha 18** | +4   | +8   |
```

Note the layout: **Str/Dex/Con** on the top row, **Int/Wis/Cha** on the bottom. In this example, Int, Wis, and Cha are proficient saves — their SAVE values exceed their MOD by the Proficiency Bonus (+4 at this CR).

**Delete the separate "Saving Throws" line entirely** once it is folded into the table.

**Keep the creature's own save proficiencies — don't borrow from a similar monster.** It is tempting, when converting a creature that resembles a published 2024 monster (a custom vampire, a homebrew dragon), to copy that monster's full save spread. Resist this. The official 2024 Strahd kept only his printed Dexterity and Wisdom proficiencies and left Constitution and Charisma *unproficient*, even though the generic SRD Vampire is proficient in Con, Wis, and Cha. Convert the saves the source block actually had; add a new proficient save only if you have a deliberate balance reason, not merely because a lookalike monster has it.

---

## Step 3 — Update Initiative

**2014:** Initiative was always just the DEX modifier, and was not stated explicitly in the stat block.

**2024:** Initiative appears explicitly as a modifier and a score.

- **Base conversion:** Set Initiative modifier = DEX modifier, score = DEX modifier + 10.
  - DEX 9 (−1) → `**Initiative** −1 (9)`
  - DEX 20 (+5) → `**Initiative** +5 (15)`

- **Elite/cunning creatures:** 2024 design frequently adds Proficiency Bonus to Initiative for creatures that are stealthy, tactically aware, or otherwise quick to act. This does not change CR but meaningfully impacts encounter pacing. Apply it to assassins, rogues, commanders, dragons, fiends, and any monster that narratively "goes first."
  - Example: an Assassin with DEX 18 (+4) and PB +3 → `**Initiative** +7 (17)`

---

## Step 4 — Update the Other Details Block

**Delete:** The separate `Saving Throws` line (now in the table).

**Keep and reformat:**

| 2014 line | 2024 line | Notes |
|---|---|---|
| `Skills Perception +10, Stealth +4` | `**Skills** Perception +10, Stealth +4` | Unchanged content; bold the label |
| `Damage Resistances bludgeoning, piercing, and slashing from nonmagical attacks` | `**Resistances** Bludgeoning, Piercing, Slashing` | Drop the "nonmagical" qualifier entirely — see note below |
| `Damage Resistances cold, lightning` | `**Resistances** Cold, Lightning` | Capitalize damage types; bold label; omit if empty |
| `Damage Vulnerabilities fire` | `**Vulnerabilities** Fire` | New dedicated line; omit if empty |
| `Damage Immunities fire, poison` + `Condition Immunities poisoned, charmed` | `**Immunities** Fire, Poison; Charmed, Poisoned` | Merge into one line; damage types first, then conditions, separated by semicolon |
| `Senses darkvision 120 ft., passive Perception 20` | `**Senses** Darkvision 120 ft.; Passive Perception 20` | Capitalize "Passive Perception"; semicolon before it |
| `Languages Deep Speech, telepathy 120 ft.` | `**Languages** Deep Speech; telepathy 120 ft.` | Semicolon before telepathy |
| `Challenge 10 (5,900 XP)` | `**CR** 10 (XP 5,900; PB +4)` | See Step 5 for lair variant |

**⚠️ Nonmagical damage resistance — a significant change:** In 2014, many monsters had resistance specifically to "Bludgeoning, Piercing, and Slashing damage from Nonmagical Attacks." In 2024, this qualifier is **removed entirely**. Monsters either have resistance to B/P/S damage or they don't — there is no nonmagical exception. When converting, simply drop "from Nonmagical Attacks" from the resistance entry.

This is a meaningful power shift: a 2024 monster with `**Resistances** Bludgeoning, Piercing, Slashing` takes half damage from *all* physical attacks, including magical weapons. If this feels too strong for your creature's intended CR, consider removing the resistance entirely rather than trying to add the nonmagical qualifier back — it is not a supported 2024 construction.

**The release valve is real, and official blocks use it.** When the official 2024 Strahd was released, his 2014 "resistance to B/P/S from nonmagical attacks" was not converted to full physical resistance — it was **dropped entirely**, leaving him with only `**Resistances** Necrotic`. In exchange, his HP was raised substantially (see the HP note below). This is the canonical pattern for a tough solo creature: rather than handing it blanket physical resistance that makes magic weapons feel pointless, the designers trade the resistance away and put the durability into a larger HP pool. When you convert a creature with nonmagical B/P/S resistance, treat "keep full resistance" and "drop resistance, add HP" as two equally valid options — and prefer the latter for bosses the party will fight with magic weapons.

**New in 2024 — Gear line:** If the creature carries retrievable equipment (weapons, armor, items the party could loot or use), add a `**Gear**` line listing those items. Equipment that is supernatural or highly specialized — and would be unusable if the monster is defeated — is *not* listed in Gear.

---

## Step 5 — Update the CR Line

**2014:** `Challenge 10 (5,900 XP)`

**2024:** `**CR** 10 (XP 5,900; PB +4)`

- Add the Proficiency Bonus explicitly: it is derived from CR (see the PB-by-CR table in `design_tables.md`).
- If the creature has a lair that boosts its power, state both XP values: `**CR** 10 (XP 5,900, or 7,200 in lair; PB +4)`

---

## Step 6 — Update Damage Immunity Handling for CR

**2014 rule:** Any damage immunity could reduce effective HP for CR calculation purposes. Nonmagical B/P/S resistance was treated as a significant defensive multiplier because most attacks at lower levels were nonmagical.

**2024 rule:** Only the following justify increasing effective HP:
- Physical (Bludgeoning, Piercing, Slashing) damage **resistance** — now applies against all sources, magical or not.
- Three or more **damage immunities**.

Fewer immunities, non-physical resistances, and condition immunities do not adjust effective HP in 2024. If you tuned your 2014 monster's HP downward because it had one or two immunities, you may need to increase HP to match the 2024 standard.

Note that because nonmagical B/P/S resistance no longer exists, any creature that had it in 2014 now has full B/P/S resistance in 2024 — a straight buff. This may push defensive CR upward. Recalculate after converting.

---

## Step 7 — Rewrite Traits

Most traits carry over with only cosmetic changes. Apply these rules:

- Use `***Trait Name.***` (triple asterisk — bold italic) for every named trait. The period is inside the asterisks.
- Update condition names to use Title Case: `Frightened`, `Grappled`, `Restrained`, `Poisoned`, `Blinded`, `Incapacitated`, `Prone`, `Charmed`, `Stunned`, `Paralyzed`, `Petrified`, `Exhaustion`, `Unconscious`, `Dead`.
- **Legendary Resistance:** Update to 2024 wording and add lair variant if applicable.
  - 2014: `Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead.`
  - 2024: `***Legendary Resistance (3/Day, or 4/Day in Lair).*** If the dragon fails a saving throw, it can choose to succeed instead.`
- **Magic Resistance:** Wording is the same; just reformat with triple asterisk.
- **Innate Spellcasting trait:** Delete entirely — see Step 9 for the 2024 spellcasting approach.

---

## Step 8 — Rewrite Actions and Attacks

### Attack notation

**2014:** `Bite. Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage.`

**2024:** `***Bite.*** *Melee Attack Roll:* +9, reach 10 ft. *Hit:* 17 (2d10 + 6) Piercing damage.`

Changes:
- "Melee/Ranged Weapon Attack: +X to hit" → `*Melee/Ranged Attack Roll:* +X`
- Drop "one target" — it is implied unless the attack says otherwise.
- "Hit:" → `*Hit:*` (italic)
- Capitalize the damage type: `piercing` → `Piercing`
- For ranged attacks: `range 80/320 ft.` stays the same; `Ranged Weapon Attack` → `*Ranged Attack Roll:*`
- For spell attacks: `Ranged Spell Attack` → `*Ranged Attack Roll:*` (same notation as weapon attacks in 2024)

### Saving throw actions

**2014:** `Fire Breath (Recharge 5–6). The dragon exhales fire in a 60-foot cone. Each creature in that area must make a DC 18 Dexterity saving throw, taking 63 (18d6) fire damage on a failed save, or half as much damage on a successful one.`

**2024:** `***Fire Breath (Recharge 5–6).*** *Dexterity Saving Throw:* DC 18, each creature in a 60-foot Cone. *Failure:* 63 (18d6) Fire damage. *Success:* Half damage only.`

Changes:
- Lead with the save type and DC in italics: `*Dexterity Saving Throw:* DC X,`
- Describe the target area after the DC.
- Replace "failed save" / "successful save" with `*Failure:*` / `*Success:*` (italic).
- "Half as much damage on a successful one" → `Half damage only.`
- Capitalize damage types and area-of-effect terms: `cone` → `Cone`, `line` → `Line`, `sphere` → `Sphere`, `cube` → `Cube`.
- For effects that apply on both outcomes: add a `*Failure or Success:*` line for the shared element.

### Multiattack

The Multiattack entry format is unchanged in content but gets the triple-asterisk treatment:

`***Multiattack.*** The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting.`

### Conditions and forced movement on a hit — saves dropped

In 2014, many attacks imposed a condition or forced movement via a saving throw that was trivially easy to pass — a wolf's Bite asked for a DC 11 Strength save to avoid falling Prone, a giant crab's Claw asked for a save to avoid being Grappled, and so on. In 2024, **these saves are removed**. Conditions and forced movement that are part of a melee attack's identity now apply automatically on a hit, typically gated on a size limit rather than a save.

**Prone on hit — 2014:** `Bite. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) piercing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone.`

**Prone on hit — 2024:** `***Bite.*** *Melee Attack Roll:* +4, reach 5 ft. *Hit:* 7 (2d4 + 2) Piercing damage. If the target is a Large or smaller creature, it has the Prone condition.`

The same pattern applies to Grappled and Restrained:

**Grapple on hit — 2014:** `Claws. Hit: ... If the target is Medium or smaller, it is grappled (escape DC 12). Until this grapple ends, the creature is restrained...`

**Grapple on hit — 2024:** `***Claws.*** *Melee Attack Roll:* +X, reach 5 ft. *Hit:* ... If the target is a Medium or smaller creature, it has the Grappled condition (escape DC X).`

**Forced movement follows the same rule.** In 2014, pushes and pulls on melee attacks were often gated behind a Strength save. In 2024, they apply directly on a hit — no save, just a size limit:

**Push on hit — 2014:** `Slam. Hit: ... The target must succeed on a DC 13 Strength saving throw or be pushed 10 feet away.`

**Push on hit — 2024:** `***Slam.*** *Melee Attack Roll:* +X, reach 5 ft. *Hit:* ... If the target is a Large or smaller creature, the [creature] pushes the target up to 10 feet straight away from itself.`

Pull works the same way:

**Pull on hit — 2024:** `***Charged Tendril.*** *Melee Attack Roll:* +7, reach 10 ft. *Hit:* 7 (1d6 + 4) Bludgeoning damage plus 5 (2d4) Lightning damage. If the target is a Medium or smaller creature, the shambling mound pulls the target 5 feet straight toward itself.`

**When to keep a save vs. drop it:** Saves are kept when the condition or effect is significant enough that resisting it should require a roll (Stunned, Paralyzed, Frightened, Poisoned, Charmed), or when the save *is* the whole action (breath weapons, gaze attacks, AoE cones and lines). A save is dropped when it was a low-DC secondary effect baked into a single-target melee hit — the kind of save most characters would pass automatically anyway. As a rule of thumb: single-target melee hit → apply on hit; AoE or dedicated action → keep the save.

**A high-stakes effect on a single-target attack keeps its save — and may even gain one.** The "drop the save" rule is specifically for trivial secondary effects (Prone, a short push). When the on-hit effect is severe — life drain that lowers maximum HP, level drain, ability damage, a save-or-suck condition — the save stays. The 2024 Vampire (and the official 2024 Strahd) made the vampire Bite a *Constitution Saving Throw* (DC 17) rather than a flat attack, even though it's single-target melee, because draining a creature's Hit Point maximum is a major effect. Note also that this Bite is gated: it can only target a creature that is willing or already has the Grappled, Incapacitated, or Restrained condition — the grapple comes from the melee attack, and the dangerous Bite follows. When converting an attack with a heavy on-hit rider, preserve (or add) a save sized to the effect rather than making it automatic.

---

## Step 9 — Consolidate Spellcasting

**2014** used two separate traits:
- **Innate Spellcasting** for racial/innate abilities (often with "requires no material components" exceptions)
- **Spellcasting** for class-based casting with a spell list

**2024** uses a single **Spellcasting** *action* (not a trait). Both innate and prepared spells appear in one block.

**⚠️ Spell slots are completely removed in 2024.** Monsters do not have spell slots, spell levels, or prepared spell lists. Every spell a monster can cast appears as a flat per-day use (or At Will). There is no concept of upcasting from a slot — if a monster casts a spell at a higher effective level, that is baked in as a named variant (e.g. *Acid Arrow* (level 3 version)) rather than expending a higher slot.

**2024 format:**

```
***Spellcasting.*** The [creature] casts one of the following spells, requiring no Material
components and using [Ability] as the spellcasting ability (spell save DC X, +X to hit with
spell attacks):

***At Will:*** *Spell Name*, *Spell Name*
***2/Day Each:*** *Spell Name*, *Spell Name*
***1/Day Each:*** *Spell Name*, *Spell Name*
```

Conversion notes:
- Delete both old spellcasting traits.
- Merge all spells from both traits into one block, grouped by use frequency.
- **Delete all spell slot information.** Remove slot counts, spell levels, and any "can cast X using a Yth-level slot" language entirely.
- **Do not carry over the full spell list.** The 2024 design philosophy is a sharp curation: only the spells that matter in a fight make the cut. The 2014 Archmage had 22+ spells across nine levels — *identify*, *magic missile*, *banishment*, *time stop*, and everything in between. The 2024 Archmage has roughly 15, stripped down to high-impact combat spells (*Lightning Bolt*, *Cone of Cold*), key utility that functions in an encounter (*Fly*, *Invisibility*, *Misty Step*), and pre-combat self-buffs (*Mage Armor*, *Mind Blank*). Low-level slot-fillers, out-of-combat utility spells (*Identify*, *Scrying* in most cases), and spells the creature would never realistically use mid-fight are cut entirely. Ask: *would a DM actually use this spell in a 3–5 round encounter?* If the answer is probably not, cut it.
- If the 2014 monster had multiple spells at the same slot level and could cast that level more than once, assign per-day limits based on how often it could plausibly cast each spell in a fight.
- If a spell was cast at a higher level than its base, note the level variant inline: `*Lightning Bolt* (level 7 version)` rather than "using a 7th-level spell slot."
- Spells cast before combat (like *Mage Armor*) should be noted inline: `*Mage Armor* (included in AC)` or `(cast before combat)`.
- Spell names are italicized: `*Fireball*`, `*Detect Magic*`.
- If the creature needed Material components for some spells but not others, simplify: either note "requiring no Material components" (most common in 2024) or call out specific components only when they matter narratively.
- Spellcasting moves from Traits to **Actions** in 2024.
- High-use spells (Reactions, Bonus Actions) may be broken out of the Spellcasting action entirely into their own entries — see the 2024 Archmage's *Counterspell*/*Shield* as a Reaction called Protective Magic, and *Misty Step* as a Bonus Action.

---

## Step 10 — Update Legendary Actions

**2014 format:**

```
LEGENDARY ACTIONS
The [creature] can take 3 legendary actions, choosing from the options below. Only one
legendary action option can be used at a time and only at the end of another creature's turn.
The [creature] regains spent legendary actions at the start of its turn.

  Attack (Costs 2 Actions). The creature makes one attack.
```

**2024 format:**

```
#### Legendary Actions

*Legendary Action Uses: 3 (4 in Lair). Immediately after another creature's turn, the
[creature] can expend a use to take one of the following actions. The [creature] regains all
expended uses at the start of each of its turns.*

***Attack.*** The creature makes one attack.
```

Changes:
- The entire preamble becomes italic, not plain text.
- The use count is stated up front as "Uses: 3" — lair variant in parentheses if applicable.
- "Regains spent legendary actions" → "regains all expended uses."
- **Costs X Actions** is removed. 2024 does not use a tiered cost system — each option costs one use. If your 2014 design had 2-action or 3-action options, consider redesigning them as stronger 1-use options, or splitting them into two separate options.
- Each action uses `***Name.***` triple-asterisk formatting.

---

## Step 11 — Update Lair Actions (if applicable)

**2014:** Lair Actions appeared as a standalone section in the sourcebook, not inside the stat block itself.

**2024:** Lair Actions are still run the same way mechanically (trigger on initiative count 20, can't repeat the same one two rounds in a row), but they are typically referenced in the CR line and Legendary Resistance trait rather than appearing as a block in the stat block markdown. If you are writing a standalone stat block that includes lair actions, add a brief `#### Lair Actions` section after Legendary Actions:

```
#### Lair Actions

*On Initiative Count 20 (losing ties), the [creature] can take one of the following lair
actions; it can't take the same lair action two rounds in a row.*

***[Name].*** Description.
```

---

## Step 12 — Verify CR

After reformatting, spot-check the CR using the 2024 offensive/defensive method (see `design_tables.md`). Two specific things that can shift CR from your 2014 version:

**Effective HP may have increased** if you previously discounted HP for 1–2 damage immunities. In 2024, that discount only applies at 3+ immunities or physical damage resistance, so the creature's defensive CR may now be higher.

**Effective HP may have decreased** if you previously applied a multiplier for condition immunities. Condition immunities have no direct effect on HP in 2024 CR math — they are a quality-of-life defensive feature, not a raw numerical one.

If the CR shifts, update:
- Proficiency Bonus (and recalculate all PB-derived values: attack bonuses, save DCs, skill modifiers, proficient saving throws)
- XP value
- Legendary Resistance uses (if applicable)

---

## Quick Reference — 2014 → 2024 Terminology

| 2014 | 2024 |
|---|---|
| `Melee Weapon Attack: +X to hit` | `*Melee Attack Roll:* +X` |
| `Ranged Weapon Attack: +X to hit` | `*Ranged Attack Roll:* +X` |
| `Ranged Spell Attack: +X to hit` | `*Ranged Attack Roll:* +X` |
| `Hit: X (XdY+Z) type damage` | `*Hit:* X (XdY + Z) Type damage` |
| `On a failed save, X damage` | `*Failure:* X damage` |
| `Half as much on a success` | `*Success:* Half damage only.` |
| `Condition Immunities poisoned, frightened` | `**Immunities** ...; Poisoned, Frightened` (merged with damage immunities) |
| `Damage Resistances cold` | `**Resistances** Cold` |
| `Damage Vulnerabilities fire` | `**Vulnerabilities** Fire` |
| `cone` / `line` / `sphere` / `cube` | `Cone` / `Line` / `Sphere` / `Cube` |
| `frightened` / `grappled` / `restrained` | `Frightened` / `Grappled` / `Restrained` (Title Case throughout) |
| `Costs 2 Actions` (Legendary) | Remove — all legendary options cost 1 use |
| `Innate Spellcasting` + `Spellcasting` traits | Single `***Spellcasting.***` action |
| `Challenge X (Y XP)` | `**CR** X (XP Y,YYY; PB +X)` |

---

## Conversion Checklist

- [ ] Header reformatted: `###` name, italic type line, AC + Initiative on one line, HP on own line
- [ ] Ability score table rebuilt as 3-column × 2-row with MOD and SAVE columns
- [ ] Saving throw proficiencies folded into table; separate "Saving Throws" line deleted
- [ ] Initiative updated with modifier and score; Proficiency Bonus added if creature warrants it
- [ ] Immunities merged onto one line (damage types first, conditions after semicolon)
- [ ] Resistances and Vulnerabilities each on their own line; omitted if empty
- [ ] Gear line added for retrievable equipment
- [ ] CR line updated to 2024 format with XP and PB; lair variant added if applicable
- [ ] Damage immunity HP discount reconsidered against 2024 threshold (3+ immunities or B/P/S resistance)
- [ ] All trait/action names reformatted with `***triple asterisks***`
- [ ] Attack notation updated: "Weapon Attack: +X to hit" → `*Attack Roll:* +X`
- [ ] Saving throw notation updated: "DC X Type save. On a fail..." → `*Type Saving Throw:* DC X... *Failure:*... *Success:*...`
- [ ] Trivial on-hit saves (Prone, Grappled, etc.) removed — condition now applies automatically on hit, gated by size if appropriate
- [ ] Damage types and area terms capitalized throughout
- [ ] Condition names Title Cased throughout
- [ ] Innate Spellcasting and Spellcasting traits merged into a single Spellcasting action
- [ ] Legendary Actions preamble replaced with 2024 italic preamble; cost-based actions redesigned
- [ ] Lair Actions updated or relocated as needed
- [ ] CR spot-checked against 2024 offensive/defensive method; PB and XP updated if CR shifted
