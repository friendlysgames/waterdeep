# Design Example — Strahd von Zarovich

This document annotates the Strahd von Zarovich stat block as a worked example of the Boss Design Framework. Each annotation explains the design decision being made and which framework principle it serves. Read this alongside the stat block itself.

---

## Overview

**Boss Type:** Tyrant (all three phases)
**Encounter Layer:** Combat
**Phase Count:** 3
**Reactions per Round:** 3

Strahd is a pure Tyrant expressed through three sequential phases. Each phase presents a distinct path challenge — a wall the party must identify and solve — and the correct answer to each phase is invalidated by the next. The encounter's arc moves from ranged arcane control (Phase 1) to melee positional dominance (Phase 2) to predatory close-quarters attrition (Phase 3), with each transition demanding the party reassess what they thought they knew about the fight.

The Tyrant archetype structure (Defining Trait / Strength / Weakness) applies independently to each phase:

| Phase | Defining Trait | Strength | Weakness |
|---|---|---|---|
| The Mage | Exposure — hard to pin down | Endurance — punishes wrong approach | Access — low defensive ceiling once engaged |
| The Soldier | Endurance — positioning trap | Access — lock-down loop | Penetration — no sustain when cornered |
| The Vampire | Attrition — HP drain loop | Exposure — controls engagement range | Endurance — lower sustained output without Bite |

---

## Phase 1 — The Mage

### The Defining Trait: Exposure

> **Multiattack.** Strahd uses Vampiric Touch twice, or uses Vampiric Touch and Telekinetic Grasp once each.
>
> **Telekinetic Grasp.** *Strength Saving Throw:* DC 20, one creature Strahd can see within 60 feet. *Failure:* The target rises vertically up to 20 feet and remains suspended there until the start of Strahd's next turn, takes 7 (2d6) necrotic damage, and is Restrained until the end of Strahd's next turn.
>
> **Misty Step.** *Trigger:* Strahd takes damage. *Effect:* Strahd casts *Misty Step* as a reaction, teleporting up to 30 feet to an unoccupied space he can see.

Strahd's Mage phase is built around range control. Telekinetic Grasp pulls targets off the ground and holds them in place — removing melee characters from the fight entirely without Strahd needing to engage them. Misty Step triggers on any damage, meaning every attempt to close the distance resets his position. The Defining Trait is Exposure: the party cannot engage Strahd on their terms because he dictates where the fight happens.

The solution is not to chase him. It is to control the space he can escape to — cornering him, blocking teleport destinations, or forcing him into terrain where distance cannot be maintained. Players who keep charging will keep finding themselves repositioned or suspended; players who read the pattern will realize the fight is about geography, not pursuit.

### The Strength: Endurance

> **Circle of Sickness.** *Constitution Saving Throw:* DC 20, each creature within 10 feet of Strahd. *Failure:* 28 (8d6) necrotic damage and disadvantage on the next attack roll the target makes before the end of its next turn.
>
> **Lightning Bolt.** Strahd casts *Lightning Bolt* (DC 20, 8d6 lightning damage).
>
> **Vampiric Touch.** *Hit:* 18 (4d6 + 4) necrotic damage... *Failure:* The target is Dazed until the start of Strahd's next turn.

The Strength creates urgency: Strahd's offensive output during Phase 1 is punishing, and it specifically punishes the wrong response to his Exposure. Players who cluster to support each other get hit by Circle of Sickness. Players who spread out to avoid AoE get picked off by Telekinetic Grasp and Vampiric Touch. The Dazed condition from Vampiric Touch compounds this by stripping the action economy of any character who gets hit without a plan.

This is the Strength's job: it makes standing still and figuring it out cost something. The party cannot take their time.

### The Weakness: Access

> **Blindness/Deafness.** *Trigger:* Strahd takes damage from a melee attack. *Effect:* ... *Failure:* The attacker is Blinded or Deafened.

Once the party solves the Exposure puzzle — once they have Strahd cornered and are landing hits — his AC of 16 is modest for CR 21, and his melee reactions, while dangerous, are reactive rather than proactive. He has no way to become harder to hit when the party finds its footing. The Weakness is Access: a party fighting on their terms will land attacks reliably, and the payoff for solving the positioning puzzle is a boss who suddenly feels hittable.

Note that Blindness/Deafness is still a meaningful threat — it targets the player who just hit him in melee, which is exactly the player who solved the phase's puzzle. The Weakness does not make the solved phase trivial; it makes it winnable.

### Reactions: Phase Identity

> **Indomitable.** *Trigger:* A hostile creature ends its turn. *Effect:* Strahd repeats the saving throw against one effect or condition currently affecting him.
>
> **Misty Step.** *Trigger:* Strahd takes damage.
>
> **Blindness/Deafness.** *Trigger:* Strahd takes damage from a melee attack.

The Mage phase reactions are entirely defensive and mobility-oriented. Indomitable protects against control effects — appropriate for a phase where Strahd needs to maintain his ability to dictate range. Misty Step is pure escape. Blindness/Deafness punishes melee engagement. All three reinforce the Defining Trait: this phase does not want to be in close combat.

### Lair Actions: Conditional Power

> **Control Water / Fog Cloud** *(requires Swamp Fane)*

The Mage's lair actions are gated behind a campaign condition — the Swamp Fane must not have been reconsecrated. This is intentional: players who have done the preparatory work of reconsecrating the fane have weakened Strahd before the fight begins, giving the encounter a meaningful meta-progression. Fog Cloud in particular interacts with the Exposure puzzle in an interesting way: Strahd gains Blindsight through his own fog, letting him maintain range control even in conditions that would normally suppress it.

---

## Phase 2 — The Soldier

### Phase Transition

The Soldier phase invalidates Phase 1's solution. The party who learned to corner Strahd and fight at close range now finds themselves facing a boss specifically built to punish close-range combat. Phase transitions should always force the party to reassess — here, the reassessment is immediate and visceral.

### The Defining Trait: Endurance

> **Commander's Retreat.** *Trigger:* Strahd takes damage from a melee attack. *Effect:* *Strength Saving Throw:* DC 20, the attacker. *Failure:* The attacker is pushed 5 feet away. Strahd then moves up to his speed away from the attacker without provoking opportunity attacks.
>
> **Vengeful Strike.** *Trigger:* Strahd takes damage from a spell or attack. *Effect:* Strahd moves up to his speed toward the attacker and makes a Longsword attack against them.

The Soldier's Defining Trait is Endurance — specifically, a positioning trap. Commander's Retreat punishes melee engagement by ejecting the attacker and repositioning Strahd. Vengeful Strike punishes ranged engagement by closing distance and counterattacking. Players who stay in melee get pushed out. Players who retreat to range get charged. Both responses are punished.

The solution requires coordinated positioning rather than individual tactics: if multiple players engage simultaneously from directions that prevent retreat, Commander's Retreat becomes less effective. The phase rewards party cohesion and punishes isolated heroics.

### The Strength: Access

> **Umbral Net.** *Ranged Attack Roll:* +12, range 30/60 ft., one creature. *Hit:* 7 (2d6) necrotic damage and the target is Restrained until the start of Strahd's next turn.
>
> **Longsword.** *Hit:* 11 (1d10 + 5) slashing damage plus 7 (2d6) necrotic damage... *Failure:* The target is pushed 5 feet away and knocked Prone.

The Umbral Net + Longsword Prone combination creates a reliable lock-down loop. A Restrained target has disadvantage on Dexterity saving throws and attack rolls; the Longsword can then knock it Prone, imposing disadvantage on attack rolls and halving its speed. This combination represents Access: it becomes hard to act effectively while the party is still trying to solve the positioning puzzle. Strahd makes it increasingly difficult to function while the party figures out how to fight him.

### The Weakness: Penetration

Unlike the Mage phase, the Soldier has no healing mechanic, no life drain, and no regeneration bonus tied to offensive output. Regeneration still applies, but there is nothing actively reversing the party's damage progress beyond the standard 20 HP per turn. Once the party solves the positioning puzzle and commits to coordinated melee, they will grind through this phase relatively efficiently. The Weakness is Penetration: damage lands and sticks.

### Reactions: Phase Identity

> **Commander's Retreat.** *Trigger:* Strahd takes damage from a melee attack.
>
> **Vengeful Strike.** *Trigger:* Strahd takes damage from a spell or attack.

Both of the Soldier's unique reactions are positional rather than damage-dealing. Commander's Retreat repositions him away from melee; Vengeful Strike repositions him toward a ranged attacker. Together they create the phase's central movement puzzle — the reactions are the Defining Trait made reactive. Every time a player attacks, they are forced to consider: will this provoke a repositioning that disrupts our formation?

Note that both reactions trigger on damage from different sources, meaning in a single round Strahd can respond to a melee attacker with Commander's Retreat on one turn and chase a spellcaster with Vengeful Strike on another turn — reinforcing the one-reaction-per-turn rule's importance for this phase.

---

## Phase 3 — The Vampire

### Phase Transition

The Vampire phase invalidates Phase 2's solution. Coordinated melee positioning — the key to Phase 2 — now feeds directly into Strahd's Bite pipeline. Players who learned to cluster around him are now providing him with adjacent targets to grapple and drain.

### The Defining Trait: Attrition

> **Unarmed Strike.** *Melee Attack Roll:* +12, reach 5 ft., one target. *Hit:* 10 (1d8 + 5) slashing damage plus 14 (4d6) necrotic damage. If the target is a creature, Strahd can grapple it (escape DC 20).
>
> **Bite.** *Constitution Saving Throw:* DC 20, one creature within 5 feet that is willing or that has the Grappled, Incapacitated, or Restrained condition. *Failure:* 8 (1d6 + 5) piercing damage plus 10 (3d6) necrotic damage. The target's hit point maximum decreases by an amount equal to the necrotic damage taken, and Strahd regains hit points equal to that amount.

The Defining Trait is Attrition. The Unarmed Strike into Bite pipeline does not just deal damage — it reduces HP maximums, which cannot be healed back, and simultaneously heals Strahd. Left unchecked, this creates a compounding problem: the party's effective ceiling drops while Strahd's health rises, narrowing the window for victory with every successful Bite.

The solution is to break the pipeline. The Bite requires a Grappled, Incapacitated, or Restrained target — preventing the grapple (through Athletics or Acrobatics checks to escape, or abilities that grant Grapple immunity) denies the Bite its food source. Alternatively, Charm can bring a willing target into range, so breaking Concentration on Charm stops that vector. Players who identify the pipeline and disrupt it have solved the phase.

### The Strength: Exposure

> **Night's Retreat.** *Trigger:* Strahd takes damage. *Effect:* Strahd flies up to his speed without provoking opportunity attacks. If one or more creatures have Grappled Strahd, he breaks free of the grapples.
>
> **Blood Frenzy.** *Trigger:* Strahd takes damage. *Effect:* Strahd moves up to his speed toward the attacker and makes an Unarmed Strike against it.

The Strength is Exposure — Strahd controls when and where the Vampire phase engages. Night's Retreat lets him break grapples and escape when threatened, resetting to a position of his choosing. Blood Frenzy lets him close on isolated targets and initiate the grapple pipeline. Together, they mean the party cannot reliably dictate the terms of engagement: they cannot hold him in place, and they cannot stay far enough away that he cannot reach them.

This creates urgency around solving the Defining Trait: the party must break the pipeline while Strahd retains the ability to start it again.

### The Weakness: Endurance

The Vampire phase, without a successful Bite, deals less sustained single-target damage than the Mage phase. Bats' Frenzy and Predator's Fury are AoE Bonus Actions rather than focused damage, and neither scales as dangerously as Circle of Sickness. A party that prevents the Bite — by breaking grapples, staying spread, or eliminating Charm vectors — will find Strahd's raw offensive output manageable. The Weakness is Endurance: the party that solves the Attrition puzzle can outlast the phase.

### Reactions: Phase Identity

> **Night's Retreat.** *Trigger:* Strahd takes damage.
>
> **Blood Frenzy.** *Trigger:* Strahd takes damage.

Both of the Vampire phase's unique reactions share the same trigger. This is intentional: the DM must choose between them on every damage event, and that choice reflects the phase's tactical identity. Night's Retreat is the defensive option — escape, reset, find a new target. Blood Frenzy is the offensive option — close on the attacker and start the grapple. The choice should be driven by context: if Strahd has already grappled someone and wants to protect that investment, Blood Frenzy closes on whoever interrupted him. If the party is about to focus Strahd down, Night's Retreat resets the engagement.

This decision point is part of the DM's puzzle in running this phase — it mirrors the party's puzzle in surviving it.

---

## The Phase Arc

Taken as a whole, the three phases form a single coherent encounter that escalates in intimacy and demands escalating tactical sophistication:

**Phase 1** asks: *How do we find him?* (Range, exposure, space control)
**Phase 2** asks: *How do we hold him?* (Positioning, coordination, mutual pressure)
**Phase 3** asks: *How do we stop him from healing?* (Pipeline disruption, grapple prevention, attrition management)

Each correct answer is punished by the next phase. This is the Tyrant's core design principle at work across an extended arc: the party never settles into a working approach, because Strahd changes what the correct approach is every time they figure it out.

The encounter ends not when the party finds one solution, but when they demonstrate the ability to find three.

---

## Appendix — Full Stat Blocks

*The complete stat blocks for all three phases of Strahd von Zarovich, formatted for table use.*

---

### Phase 1 — The Mage

*Strahd leads with overwhelming arcane power, controlling space and punishing enemies who close the distance.*

**AC** 16 (natural armor)

**HP** 331 (39d8 + 156)

**Speed** 40 ft., climb 40 ft.

**Initiative** +12

| STR | Mod | Save | DEX | Mod | Save | CON | Mod | Save |
|---|---|---|---|---|---|---|---|---|
| 20 | +5 | +5 | 20 | +5 | +12 | 18 | +4 | +4 |
| **INT** | **Mod** | **Save** | **WIS** | **Mod** | **Save** | **CHA** | **Mod** | **Save** |
| 20 | +5 | +5 | 15 | +2 | +9 | 20 | +5 | +12 |

**Skills** Arcana +19, Athletics +12, Deception +19, Insight +9, Perception +16, Religion +12, Stealth +19

**Resistances** Necrotic

**Senses** Darkvision 120 ft., Passive Perception 24

**Languages** Abyssal, Common, Draconic, Elvish, Giant, Infernal

**CR** 21 (33,000 XP), or 19 when fought in sunlight | **Proficiency Bonus** +7

#### Traits

**Close Quarters Fighter.** Strahd doesn't have disadvantage on his ranged attack rolls when within 5 feet of a hostile creature.

**Fast Grappler.** Strahd does not have to spend extra movement to move a creature grappled by him if the grappled creature is the same size or smaller.

**Innate Spellcasting (Intelligence, DC 20).** Strahd can innately cast the following spells, requiring no material components:
- 3/day: *Detect Thoughts*, *Animate Dead*
- 1/day: *Scrying*

**Regeneration.** Strahd regains 20 hit points at the start of his turn if he has at least 1 hit point and isn't in sunlight. If he takes radiant damage, this trait doesn't function at the start of his next turn.

**Spider Climb.** Strahd can move up, down, and across vertical surfaces and upside down along ceilings, while leaving his hands free.

**Sunlight Hypersensitivity.** While in sunlight, Strahd takes 20 radiant damage at the start of his turn, and he has disadvantage on attack rolls and ability checks.

#### Actions

**Multiattack.** Strahd uses Vampiric Touch twice, or uses Vampiric Touch and Telekinetic Grasp once each.

**Vampiric Touch.** *Melee Attack Roll:* +12, reach 5 ft., one target. *Hit:* 18 (4d6 + 4) necrotic damage, and Strahd regains hit points equal to half the damage dealt. *Constitution Saving Throw:* DC 20, the target. *Failure:* The target is Dazed until the start of Strahd's next turn. (A Dazed creature can move or take one action on its turn, not both. It also can't take a Bonus Action or a Reaction.)

**Telekinetic Grasp.** *Strength Saving Throw:* DC 20, one creature Strahd can see within 60 feet. *Failure:* The target rises vertically up to 20 feet and remains suspended there until the start of Strahd's next turn, takes 7 (2d6) necrotic damage, and is Restrained until the end of Strahd's next turn. When the effect ends, the target falls if it is still aloft. *Success:* No effect.

**Dispel Magic (3/day).** Strahd casts *Dispel Magic*.

#### Bonus Actions

**Circle of Sickness.** *Constitution Saving Throw:* DC 20, each creature within 10 feet of Strahd. *Failure:* 28 (8d6) necrotic damage and disadvantage on the next attack roll the target makes before the end of its next turn. *Success:* Half damage only.

**Lightning Bolt.** Strahd casts *Lightning Bolt* (DC 20, 8d6 lightning damage).

#### Reactions

*Strahd can take 3 reactions per round, but only 1 per turn. If an effect or condition would prevent him from taking reactions, he loses one reaction instead.*

**Indomitable.** *Trigger:* A hostile creature ends its turn. *Effect:* Strahd repeats the saving throw against one effect or condition currently affecting him. (This reaction has no effect if the effect or condition didn't originally require a failed saving throw.)

**Misty Step.** *Trigger:* Strahd takes damage. *Effect:* Strahd casts *Misty Step* as a reaction, teleporting up to 30 feet to an unoccupied space he can see.

**Blindness/Deafness.** *Trigger:* Strahd takes damage from a melee attack. *Effect:* Strahd casts *Blindness/Deafness* as a reaction. *Constitution Saving Throw:* DC 20, the attacker. *Failure:* The attacker is Blinded or Deafened (Strahd's choice) and takes 7 (2d6) necrotic damage.

#### Lair Actions

On initiative count 20 (losing initiative ties), if outdoors and the players have not yet reconsecrated the Swamp Fane, Strahd can take one of the following lair actions, or forgo using any of them that round:

**Control Water** *(requires Swamp Fane).* Strahd casts *Control Water* without components or concentration.

**Fog Cloud** *(requires Swamp Fane).* Strahd casts *Fog Cloud* at 5th level without components or concentration. While the fog remains, Strahd has Blindsight out to its edges.

---

### Phase 2 — The Soldier

*Strahd becomes a relentless physical combatant, dominating the battlefield through positioning, aggression, and punishing any attempt to disengage.*

**AC** 16 (natural armor)

**HP** 331 (39d8 + 156)

**Speed** 40 ft., climb 40 ft.

**Initiative** +12

| STR | Mod | Save | DEX | Mod | Save | CON | Mod | Save |
|---|---|---|---|---|---|---|---|---|
| 20 | +5 | +5 | 20 | +5 | +12 | 18 | +4 | +4 |
| **INT** | **Mod** | **Save** | **WIS** | **Mod** | **Save** | **CHA** | **Mod** | **Save** |
| 20 | +5 | +5 | 15 | +2 | +9 | 20 | +5 | +12 |

**Skills** Arcana +19, Athletics +12, Deception +19, Insight +9, Perception +16, Religion +12, Stealth +19

**Resistances** Necrotic

**Senses** Darkvision 120 ft., Passive Perception 24

**Languages** Abyssal, Common, Draconic, Elvish, Giant, Infernal

**CR** 21 (33,000 XP), or 19 when fought in sunlight | **Proficiency Bonus** +7

#### Traits

**Battlefield Awareness.** Strahd has advantage on Strength and Dexterity saving throws against effects he can see or hear, such as traps and spells. Additionally, Strahd can't be disarmed.

**Close Quarters Fighter.** Strahd doesn't have disadvantage on his ranged attack rolls when within 5 feet of a hostile creature.

**Fast Grappler.** Strahd does not have to spend extra movement to move a creature grappled by him if the grappled creature is the same size or smaller.

**Regeneration.** Strahd regains 20 hit points at the start of his turn if he has at least 1 hit point and isn't in sunlight. If he takes radiant damage, this trait doesn't function at the start of his next turn.

**Spider Climb.** Strahd can move up, down, and across vertical surfaces and upside down along ceilings, while leaving his hands free.

**Sunlight Hypersensitivity.** While in sunlight, Strahd takes 20 radiant damage at the start of his turn, and he has disadvantage on attack rolls and ability checks.

#### Actions

**Multiattack.** Strahd makes two attacks, only one of which can be an Umbral Net.

**Longsword.** *Melee Attack Roll:* +12, reach 5 ft., one target. *Hit:* 11 (1d10 + 5) slashing damage plus 7 (2d6) necrotic damage. *Strength Saving Throw:* DC 20, the target. *Failure:* The target is pushed 5 feet away and knocked Prone.

**Umbral Net.** *Ranged Attack Roll:* +12, range 30/60 ft., one creature. *Hit:* 7 (2d6) necrotic damage and the target is Restrained until the start of Strahd's next turn.

#### Bonus Actions

**Thunderous Wave.** *Strength Saving Throw:* DC 20, each creature within 5 feet of Strahd. *Failure:* 14 (3d8) thunder damage and the target is pushed 5 feet away. *Success:* Half damage only.

**Dark Volley.** *Dexterity Saving Throw:* DC 20, each creature in a 10-foot-radius, 40-foot-high cylinder centered on a point Strahd can see within 120 feet. *Failure:* 18 (4d8) necrotic damage. *Success:* Half damage only.

#### Reactions

*Strahd can take 3 reactions per round, but only 1 per turn. If an effect or condition would prevent him from taking reactions, he loses one reaction instead.*

**Indomitable.** *Trigger:* A hostile creature ends its turn. *Effect:* Strahd repeats the saving throw against one effect or condition currently affecting him. (This reaction has no effect if the effect or condition didn't originally require a failed saving throw.)

**Commander's Retreat.** *Trigger:* Strahd takes damage from a melee attack. *Effect:* *Strength Saving Throw:* DC 20, the attacker. *Failure:* The attacker is pushed 5 feet away. Strahd then moves up to his speed away from the attacker without provoking opportunity attacks.

**Vengeful Strike.** *Trigger:* Strahd takes damage from a spell or attack. *Effect:* Strahd moves up to his speed toward the attacker and makes a Longsword attack against them. This movement doesn't trigger opportunity attacks.

#### Lair Actions

On initiative count 20 (losing initiative ties), if outdoors and the players have not yet reconsecrated the Forest Fane, Strahd can take one of the following lair actions, or forgo using any of them that round:

**Plant Growth** *(requires Forest Fane).* Strahd casts *Plant Growth* without components or concentration.

**Wrath of Nature** *(requires Forest Fane).* Strahd casts *Wrath of Nature* without components or concentration. When cast this way, Strahd can't use the spell's Rocks effect.

---

### Phase 3 — The Vampire

*Strahd becomes a predator, isolating targets, draining their life force, and bending their will to his own.*

**AC** 16 (natural armor)

**HP** 331 (39d8 + 156)

**Speed** 40 ft., climb 40 ft.

**Initiative** +12

| STR | Mod | Save | DEX | Mod | Save | CON | Mod | Save |
|---|---|---|---|---|---|---|---|---|
| 20 | +5 | +5 | 20 | +5 | +12 | 18 | +4 | +4 |
| **INT** | **Mod** | **Save** | **WIS** | **Mod** | **Save** | **CHA** | **Mod** | **Save** |
| 20 | +5 | +5 | 15 | +2 | +9 | 20 | +5 | +12 |

**Skills** Arcana +19, Athletics +12, Deception +19, Insight +9, Perception +16, Religion +12, Stealth +19

**Resistances** Necrotic

**Senses** Darkvision 120 ft., Passive Perception 24

**Languages** Abyssal, Common, Draconic, Elvish, Giant, Infernal

**CR** 21 (33,000 XP), or 19 when fought in sunlight | **Proficiency Bonus** +7

#### Traits

**Close Quarters Fighter.** Strahd doesn't have disadvantage on his ranged attack rolls when within 5 feet of a hostile creature.

**Fast Grappler.** Strahd does not have to spend extra movement to move a creature grappled by him if the grappled creature is the same size or smaller.

**Regeneration.** Strahd regains 20 hit points at the start of his turn if he has at least 1 hit point and isn't in sunlight. If he takes radiant damage, this trait doesn't function at the start of his next turn.

**Spider Climb.** Strahd can move up, down, and across vertical surfaces and upside down along ceilings, while leaving his hands free.

**Sunlight Hypersensitivity.** While in sunlight, Strahd takes 20 radiant damage at the start of his turn, and he has disadvantage on attack rolls and ability checks.

#### Actions

**Multiattack.** Strahd makes two attacks, only one of which can be a Bite. Strahd can replace one of his attacks with a Charm.

**Unarmed Strike.** *Melee Attack Roll:* +12, reach 5 ft., one target. *Hit:* 10 (1d8 + 5) slashing damage plus 14 (4d6) necrotic damage. If the target is a creature, Strahd can grapple it (escape DC 20).

**Bite.** *Constitution Saving Throw:* DC 20, one creature within 5 feet that is willing or that has the Grappled, Incapacitated, or Restrained condition. *Failure:* 8 (1d6 + 5) piercing damage plus 10 (3d6) necrotic damage. The target's hit point maximum decreases by an amount equal to the necrotic damage taken, and Strahd regains hit points equal to that amount. The target dies if this effect reduces its hit point maximum to 0. A Humanoid reduced to 0 hit points by this damage and then buried rises the following sunset as a **Vampire Spawn** under Strahd's control. If the target hasn't been bitten within the last 24 hours, when finishing a Long Rest it can roll one of its Hit Dice and add its Constitution modifier; the target's hit point maximum increases by an amount equal to the result (this can't raise the target above its original maximum).

**Charm.** *Wisdom Saving Throw:* DC 20, one humanoid within 30 feet that Strahd can see (a target that can't see Strahd automatically succeeds). *Failure:* The target is magically Charmed for 1 minute or until Strahd loses Concentration. While Charmed, the target regards Strahd as a trusted friend to be heeded and protected; it isn't under Strahd's control, but takes his requests and actions in the most favorable way and allows Strahd to bite it. The target repeats the saving throw at the end of each of its turns, ending the effect on a success. If still Charmed at the end of the minute, the effect lasts for 24 hours, until Strahd is destroyed, or until Strahd takes a Bonus Action to end it.

#### Bonus Actions

**Bats' Frenzy.** *Dexterity Saving Throw:* DC 20, each creature within 10 feet of Strahd. *Failure:* 15 (6d4) necrotic damage and disadvantage on the next attack roll the target makes before the start of Strahd's next turn. *Success:* Half damage only.

**Predator's Fury.** *Dexterity Saving Throw:* DC 20, up to two creatures Strahd can see within 60 feet that are within 5 feet of each other. *Failure:* 16 (2d10 + 5) force damage and the target is knocked Prone. *Success:* Half damage only.

#### Reactions

*Strahd can take 3 reactions per round, but only 1 per turn. If an effect or condition would prevent him from taking reactions, he loses one reaction instead.*

**Indomitable.** *Trigger:* A hostile creature ends its turn. *Effect:* Strahd repeats the saving throw against one effect or condition currently affecting him. (This reaction has no effect if the effect or condition didn't originally require a failed saving throw.)

**Night's Retreat.** *Trigger:* Strahd takes damage. *Effect:* Strahd flies up to his speed without provoking opportunity attacks. If one or more creatures have Grappled Strahd, he breaks free of the grapples.

**Blood Frenzy.** *Trigger:* Strahd takes damage. *Effect:* Strahd moves up to his speed toward the attacker and makes an Unarmed Strike against it.

#### Lair Actions

On initiative count 20 (losing initiative ties), if outdoors and the players have not yet reconsecrated the Mountain Fane, Strahd can take one of the following lair actions, or forgo using any of them that round:

**Change Weather** *(requires Mountain Fane).* Strahd casts *Control Weather* without components or concentration. When he does, he can change any number of weather conditions to any of the stages given.

**Call Lightning** *(requires Mountain Fane).* Strahd casts *Call Lightning* without components or concentration. Whenever he rolls lightning damage with this spell while outdoors in a storm, he deals maximum damage instead of rolling.
