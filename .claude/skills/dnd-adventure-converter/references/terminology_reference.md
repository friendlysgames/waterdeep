# Terminology & Capitalization Reference — 2014 → 2024

The bulk of adventure-text conversion is applying this table correctly and consistently across a whole document. None of it is conceptually hard; the risk is inconsistent application — catching it in paragraph one and missing it in paragraph twenty.

## Capitalization — confirmed by direct comparison

These pairs were confirmed by diffing an official 2014-ruleset adventure chapter against an official 2024-ruleset adventure line by line, not inferred from the rules alone.

| Term | 2014 style | 2024 style |
|---|---|---|
| Coin currency | `50 gp`, `1,900 gp` | `50 GP`, `1,900 GP` |
| Hit Points, spelled out | `225 hit points`, `10 hit points or fewer` | `225 Hit Points`, `10 Hit Points or fewer` |
| Temporary Hit Points | `temporary hit points` | `Temporary Hit Points` |
| Conditions | `has the poisoned condition`, `the blinded condition` | `has the Poisoned condition`, `the Blinded condition` |
| Attitude (now a defined game term) | `is indifferent to`, `becomes friendly toward` | `is Indifferent toward`, `becomes Friendly toward` |
| Advantage / Disadvantage | `has disadvantage on this save` | `has Disadvantage on this save` |
| Difficult terrain | `*difficult terrain*` (often italicized, lowercase) | `Difficult Terrain` |
| Rests | `take a long rest`, `a short rest` | `take a Long Rest`, `a Short Rest` |
| Alignment, describing an NPC in prose | `neutral good`, `lawful evil`, `chaotic good` | `Neutral Good`, `Lawful Evil`, `Chaotic Good` |
| Stat block names on bolded first mention | a `**treant**`, `**veterans**` (lowercase despite bold) | a `**Treant**`, `**Warrior Veterans**` (Title Case) — check the rename table too |

## Capitalization — documented in the SRD 5.2.1 conversion notes

Not directly visible in the two sample texts (they didn't happen to use every term), but confirmed by Wizards' own guidance. Apply the same "capitalize it as a proper term" logic whenever a word is the specific game term rather than an ordinary English word:

| Category | Examples |
|---|---|
| D20 Test-related terms | D20 Test, Heroic Inspiration *(formerly "inspiration")* |
| Actions | Attack action, Dash action, Search action, Study action, Influence action, Utilize action, Magic action, Hide action, Help action |
| Action types | Bonus Action, Reaction, Legendary Action |
| Senses | Passive Perception *(formerly "passive Wisdom (Perception) score")*, Darkvision, Tremorsense, Blindsight, Truesight |
| Damage/condition modifiers | Immunity, Resistance, Vulnerability |
| Combat terms | Initiative, Critical Hit, Opportunity Attack, Concentration, Proficiency Bonus, Armor Class (AC), Challenge Rating (CR), Difficulty Class (DC) |
| Areas of effect | Cone, Cylinder, Line, Sphere, Cube, Emanation |
| Character creation | Species *(formerly "race")*, Background, Origin Feat |
| Death & dying | Death Saving Throw, Stable, Bloodied |
| Obscurement/light | Heavily Obscured, Lightly Obscured, Bright Light, Dim Light |

If unsure whether a specific instance is the game term or just an English word ("the room's occupant flew into a rage" vs. the Barbarian's Rage class feature), capitalize only when it's clearly invoking the mechanic.

## Renamed monsters (SRD stat block name changed)

Bare monster references in old adventure text won't get caught by a stat-block converter — there's no block in the prose to convert, just a name. Check every bold or unbold monster mention against this list:

| 2014 name | 2024 SRD name |
|---|---|
| Acolyte | Priest Acolyte |
| Androsphinx | Sphinx of Valor |
| Azer | Azer Sentinel |
| Bugbear | Bugbear Warrior |
| Centaur | Centaur Trooper |
| Cult Fanatic | Cultist Fanatic |
| Flying Sword | Animated Flying Sword |
| Gnoll | Gnoll Warrior |
| Goblin | Goblin Warrior |
| Gynosphinx | Sphinx of Lore |
| Half-Red Dragon Veteran | Half-Dragon |
| Hobgoblin | Hobgoblin Warrior |
| Kobold | Kobold Warrior |
| Merfolk | Merfolk Skirmisher |
| Minotaur | Minotaur of Baphomet |
| Rug of Smothering | Animated Rug of Smothering |
| Sahuagin | Sahuagin Warrior |
| Thug | Tough |
| Tribal Warrior | Warrior Infantry |
| Veteran | Warrior Veteran |

New monsters with no 2014 equivalent (won't appear in old text, but useful if the user wants a comparable creature): Bugbear Stalker, Goblin Boss, Goblin Minion, Guard Captain, Hobgoblin Captain, Incubus (no longer a Succubus variant), Pirate, Pirate Captain, Sphinx of Wonder, Swarm of Crawling Claws, Tough Boss, Troll Limb, Vampire Familiar.

## Monsters omitted from the open SRD

| 2014 name | SRD-legal substitute | Note |
|---|---|---|
| Duergar | Spy | |
| Elf, Drow | Priest Acolyte | |
| Gnome, Deep (Svirfneblin) | Scout | |
| Lizardfolk | Scout | |
| Orc | Tough | Orc still exists as a **player species** in 2024 — only the monster stat block was pulled from the open SRD. |

These weren't cut from the game — they're missing from the free, open-licensed SRD specifically, most likely for licensing reasons. Wizards' actual 2025 Monster Manual has full stat blocks for all five. Use the SRD substitute only if the output has to remain SRD-legal (e.g., for redistribution under the license); otherwise flag it and let the user decide, since a home conversion almost always wants the real creature rather than a reskinned Spy or Scout.

## Renamed animals

| 2014 name | 2024 name |
|---|---|
| Giant Sea Horse | Giant Seahorse |
| Giant Poisonous Snake | Giant Venomous Snake |
| Quipper | Piranha |
| Sea Horse | Seahorse |
| Swarm of Quippers | Swarm of Piranhas |
| Swarm of Poisonous Snakes | Swarm of Venomous Snakes |
| Poisonous Snake | Venomous Snake |

New animals with no 2014 equivalent: Allosaurus, Ankylosaurus, Archelon, Hippopotamus, Pteranodon.

## Renamed spells

| 2014 name | 2024 name |
|---|---|
| Feeblemind | Befuddlement |
| Branding Smite | Shining Smite |

All other spells kept their names but may have revised statistics. If the adventure specifies exact spell effects — unusual for adventure prose, but it happens with custom rituals — double-check against the current spell text rather than assuming the 2014 numbers still apply.

## Renamed magic items

| 2014 name | 2024 name |
|---|---|
| arrow of slaying | Ammunition of Slaying |
| Orb of Dragonkind | Dragon Orb |
| iron bands of binding | Iron Bands |
| Deck of Many Things | Mysterious Deck |

**Mechanical change, not just a rename:** drinking or administering a *Potion of Healing* (or any potion) now takes a Bonus Action instead of an action. If a treasure or consumable-use note in old text says "as an action, drink the potion," update the action cost.

## Renamed poison

| 2014 name | 2024 name |
|---|---|
| drow poison | Spider's Sting |

## Renamed example traps

| 2014 name | 2024 name |
|---|---|
| fire-breathing statue | Fire-casting statue |
| poison darts | Poisoned darts |
| poison needle | Poisoned needle |
| rolling sphere | Rolling stone |
| among pits | Hidden pit / Spiked pit *(split into two variants)* |

Trap severity categories also changed: 2014 rated traps setback, dangerous, or deadly; 2024 uses just **nuisance trap** or **deadly trap**. See `rules_changes.md` for what that means when writing one up.

## Armor names (all gain "Armor" and capitalize)

| 2014 name | 2024 name |
|---|---|
| padded | Padded Armor |
| leather | Leather Armor |
| studded leather | Studded Leather Armor |
| hide | Hide Armor |
| half plate | Half Plate Armor |
| splint | Splint Armor |
| plate | Plate Armor |

## New character-origin content (context, not usually a direct text edit)

If a source adventure includes quick-build NPC stats or background suggestions: new Backgrounds in 2024 are Criminal, Sage, and Soldier (Acolyte was revised, not replaced); new player Species are Goliath and Orc; Dragonborn, Dwarf, Elf, Gnome, Halfling, Human, and Tiefling were all revised. Ability score increases now come from Background, not Species — if old text says a race grants an ability score bonus, that mechanic no longer exists in that form.
