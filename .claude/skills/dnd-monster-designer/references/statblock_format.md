# Stat Block Format (2024 SRD Standard)

Use the following markdown structure exactly as it appears in the 2024 SRD. This ensures compatibility with Foundry VTT journals and other tools that parse SRD-style formatting.

---

### [Monster Name]

*[Size] [Type] ([Tag if any]), [Alignment]*

**AC** [X] **Initiative** [+X] ([Initiative Score])

**HP** [X] ([XdY + Z])

**Speed** [X] ft.[, Fly X ft., Swim X ft., Burrow X ft., Climb X ft. — as applicable]

|            | MOD  | SAVE |            | MOD  | SAVE |            | MOD  | SAVE |
| :--------- | :--- | :--- | :--------- | :--- | :--- | :--------- | :--- | :--- |
| **Str [X]** | +X  | +X   | **Dex [X]** | +X  | +X   | **Con [X]** | +X  | +X   |
| **Int [X]** | +X  | +X   | **Wis [X]** | +X  | +X   | **Cha [X]** | +X  | +X   |

**Skills** [Skill +X, Skill +X] *(omit line if none)*

**Vulnerabilities** [damage types] *(omit line if none)*

**Resistances** [damage types] *(omit line if none)*

**Immunities** [damage types]; [condition names] *(omit line if none; list damage types before conditions, separated by semicolon)*

**Gear** [Item, Item] *(omit line if none)*

**Senses** [Darkvision X ft., Blindsight X ft., Tremorsense X ft.,] Passive Perception [X]

**Languages** [list, or None]

**CR** [X] (XP [X,XXX][, or X,XXX in lair]; PB +[X])

#### Traits

***[Trait Name].*** Description.

***[Trait Name] ([X]/Day[, or X/Day in Lair]).*** Description.

#### Actions

***Multiattack.*** The [creature] makes [X] [Attack Name] attacks[, or makes one X attack and uses Y].

***[Attack Name].*** *[Melee/Ranged] Attack Roll:* +[X], reach [X] ft.[/range X/Y ft.] *Hit:* [X] ([XdY + Z]) [damage type] damage[ plus X (XdY) [type] damage].

***[Save-Based Action] (Recharge [X-Y]).*** *[Ability] Saving Throw:* DC [X], [target description — e.g. each creature in a 30-foot Cone / one creature the [name] can see within 60 feet]. *Failure:* [X] ([XdY]) [type] damage [and condition]. *Success:* Half damage only.

*(For effects with conditional clauses, use:* ***Failure or Success:**** [shared effect.] )*

#### Bonus Actions *(omit section if none)*

***[Name].*** Description.

#### Reactions *(omit section if none)*

***[Name].*** *Trigger:* [What triggers it]. *Response:* [What the creature does].

#### Legendary Actions *(omit section if none)*

*Legendary Action Uses: [3] ([4] in Lair). Immediately after another creature's turn, the [creature] can expend a use to take one of the following actions. The [creature] regains all expended uses at the start of each of its turns.*

***[Action Name].*** Description.

---

## Key formatting rules

**Ability score table:** Always use the 3-column × 2-row layout with `Str/Dex/Con` on top and `Int/Wis/Cha` on bottom. Each cell shows the score bolded (`**Str 21**`), with MOD and SAVE as separate columns. If a saving throw is not proficient, the SAVE value equals the MOD exactly. Proficient saves are higher than MOD.

**AC and Initiative on one line:** `**AC** 17 **Initiative** +7 (17)` — the Initiative score in parentheses is the flat value used when not rolling.

**HP on its own line:** `**HP** 150 (20d10 + 40)` — number first, dice expression in parentheses.

**CR line:** `**CR** 10 (XP 5,900; PB +4)` — for lair monsters: `**CR** 10 (XP 5,900, or 7,200 in lair; PB +4)`

**Omit empty sections:** If a monster has no Skills, Resistances, Immunities, Gear, or Bonus Actions/Reactions/Legendary Actions, omit those lines entirely. Do not write "None."

**Italic monster name in type line:** The size/type line is always italicized: `*Large Aberration, Lawful Evil*`

**Triple-asterisk traits and actions:** All named traits and actions use `***Name.***` (bold italic). The period is inside the asterisks.

**Saving throw notation inside action text:** Use *Ability Saving Throw:* in italics, followed by DC and target description. Outcomes use *Failure:* and *Success:* in italics.

**Attack roll notation inside action text:** Use *Melee Attack Roll:* or *Ranged Attack Roll:* in italics, followed by bonus, reach/range. Hit results use *Hit:* in italics.

**Conditions and forced movement on a hit (no save):** Minor conditions and forced movement that are part of a melee attack apply automatically on a hit, gated by a size limit rather than a save. Append the clause after the damage: `If the target is a Large or smaller creature, it has the Prone condition.` or `If the target is a Medium or smaller creature, the [creature] pushes the target up to 10 feet straight away from itself.` Do not write a saving throw for these. Reserve saves for significant conditions (Stunned, Paralyzed, Frightened, Poisoned, Charmed) or dedicated AoE actions.

**Spellcasting block format:**
***Spellcasting.*** The [creature] casts one of the following spells, requiring no Material components and using [Ability] as the spellcasting ability (spell save DC [X], +[X] to hit with spell attacks):
***At Will:*** *Spell*, *Spell*
***X/Day Each:*** *Spell*, *Spell*

No spell slots or spell levels appear anywhere — only At Will and X/Day frequencies. Curate the list to combat-relevant spells only (high-impact damage, key utility, pre-combat self-buffs noted inline like `*Mage Armor* (included in AC)`). Cast at a higher effective level via a named variant: `*Lightning Bolt* (level 7 version)`. High-frequency defensive or mobility spells can be split into their own Reaction or Bonus Action entries (e.g. *Counterspell*/*Shield* as a Reaction, *Misty Step* as a Bonus Action).

**Legendary Action preamble:** Always use the italic preamble block exactly as shown above — do not abbreviate it.

**Section headers:** Use `####` (H4) for Traits, Actions, Bonus Actions, Reactions, and Legendary Actions within a stat block. The monster name itself uses `###` (H3).

---

## Worked example

For reference, here is the SRD Bandit Captain stat block in the exact target format:

### Bandit Captain

*Medium or Small Humanoid, Neutral*

**AC** 15 **Initiative** +3 (13)

**HP** 52 (8d8 + 16)

**Speed** 30 ft.

|            | MOD  | SAVE |            | MOD  | SAVE |            | MOD  | SAVE |
| :--------- | :--- | :--- | :--------- | :--- | :--- | :--------- | :--- | :--- |
| **Str 15** | +2   | +4   | **Dex 16** | +3   | +5   | **Con 14** | +2   | +2   |
| **Int 14** | +2   | +2   | **Wis 11** | +0   | +2   | **Cha 14** | +2   | +2   |

**Skills** Athletics +4, Deception +4

**Gear** Pistol, Scimitar, Studded Leather Armor

**Senses** Passive Perception 10

**Languages** Common, Thieves' Cant

**CR** 2 (XP 450; PB +2)

#### Actions

***Multiattack.*** The bandit makes two attacks, using Scimitar and Pistol in any combination.

***Scimitar.*** *Melee Attack Roll:* +5, reach 5 ft. *Hit:* 6 (1d6 + 3) Slashing damage.

***Pistol.*** *Ranged Attack Roll:* +5, range 30/90 ft. *Hit:* 8 (1d10 + 3) Piercing damage.

#### Reactions

***Parry.*** *Trigger:* The bandit is hit by a melee attack roll while holding a weapon. *Response:* The bandit adds 2 to its AC against that attack, possibly causing it to miss.
