# Doom Raiders Mechanics Reference

CR 2.0 audits for every Doom Raiders faction-event hazard, at three, four and five participating combatants. Filled in by the encounter-builder agent, Session 38.

## Method and conventions

- CR 2.0 only. Party Power from the level table (L2 14, L4 23, L5 32, L6 35, L7 41, L8 44). Monster Power from the tier-adjusted table (L1-4 Tier 1; L5-10 Tier 2).
- % HP lost = (Enemy Power / Party Power) squared. Budget = Party Power x multiplier.
- "Standard" in this file = Bruising (20-40% HP lost, Day Cost 4). "Hard" = Bloody (40-60%, Day Cost 6). Mild = 2, Brutal = 8.
- Waves are separate encounters; Day Costs add. Where I add wave percentages to show a whole-mission total, that is a rough heuristic of mine, not a skill rule.
- Combatant counts include non-member companions. Bystanders, victims and NPCs who do not fight (Heldar, the commuters, Ziraj by default) are not counted.
- Flee-at-half-HP heuristic (mine, not a skill rule): Power is the square root of HP x DPR, so a foe who leaves at half HP contributes about 0.71 of its listed Power. Verdicts below use full Power, so real losses run a little lower.
- **Source.** All stat blocks are 2024 *Monster Manual* (XMM) records from the 5etools mirror (`dr-creatures-xmm.json`); spells are 2024 *Player's Handbook* (XPHB) records from the same mirror (`dr-spells-xphb.json`). Both are in the session scratchpad. CRs: Assassin 8, Bandit 1/8, Bandit Captain 2, Commoner 0, Giant Rat 1/8, Mage 6, Mage Apprentice 2, Priest Acolyte 1/4, Scout 1/2, Spy 1, Tough 1/2, Warrior Veteran 3, Wererat 2. Thug and Veteran do not exist in XMM.
- **First-turn KO check.** The skill adds 4 to CR when a monster can kill or KO a PC on turn one. The 2024 Mage (three Arcane Burst at 16 force each, range 120 ft) and Assassin (three attacks of 24-29 each) both can. Base figures below assume the caster acts defensively or the party acts first; each section gives the CR +4 figure.

## 1. M1 The Dockside Killer (level 2, Tier 1)

| PCs | Party Power | Bruising budget (x0.6) | Bloody budget (x0.75) |
|---|---|---|---|
| 3 | 42 | 25.2 | 31.5 |
| 4 | 56 | 33.6 | 42 |
| 5 | 70 | 42 | 52.5 |

Monster Power (Tier 1): Scout CR 1/2 = 16; Bandit CR 1/8 = 4; Tough CR 1/2 = 16.

**Draft roster (Soluun alone, Scout = 16):**

| PCs | Enemy / Party | % HP lost | Verdict | Day Cost |
|---|---|---|---|---|
| 3 | 16/42 | 14.5% | Mild | 2 |
| 4 | 16/56 | 8.2% | Below Mild | 2 |
| 5 | 16/70 | 5.2% | Below Mild | 2 |

Verdict: trivial as a fight at every size, and he leaves at 8 HP, so the pursuit carries the scene. Yes, he needs help. Because he kills from personal hatred with no authorization, do not give him Bregan D'aerthe muscle. Give him one or two hired hands from the docks (Luskan sailors he paid to watch the flanks), who never know his name.

**Recommended rosters:**

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Scout + 2 Bandits | 24 | 32.7% (cost 4) | Scout + Tough | 32 | 58.0% (cost 6) |
| 4 | Scout + Tough | 32 | 32.7% (cost 4) | Scout + Tough + Bandit | 36 | 41.3% (cost 6) |
| 5 | Scout + Tough + 2 Bandits | 40 | 32.7% (cost 4) | Scout + 2 Tough | 48 | 47.0% (cost 6) |

Thresholds:
- Soluun disengages at 8 HP (half) and takes the roofline; this is already in the draft.
- Hired hands flee when Soluun flees or when either of them is reduced to 0. They surrender if cornered.
- A cornered Soluun surrenders instead of jumping (draft: three DC 14 Athletics successes before three failures).
- Non-combat route: spotting him first (DC 18 Perception) lets the party walk Heldar out and talk to Soluun; the hirelings then have no reason to fight.

Stat block (XMM): Scout AC 13, 16 HP, Multiattack two attacks (Shortsword +4, 5 piercing; Longbow +4, 6 piercing, range 150/600). It has a longbow, not a shortbow, so the draft's hand-crossbow swap is a named swap (5 piercing at 30/120 would be a downgrade; keep the longbow). Bandit AC 12, 11 HP, one attack (Scimitar 4 or Light Crossbow 5). Tough AC 12, 32 HP, Mace 5, Heavy Crossbow 6, Pack Tactics.

Notes: the ambush round is about 12 damage from two longbow hits, enough to drop a 2nd-level caster on 8 HP but not to trip the CR +4 rule. Tough's Pack Tactics makes a Tough plus Soluun a real flanking pair.

## 2. M3 The Missing Snobeedle (level 4, optional Shard Shunner fight, Tier 1)

Wererat CR 2 = 28; Giant Rat CR 1/8 = 4; Tough CR 1/2 = 16. Party Power 69 / 92 / 115. Bruising budget 41.4 / 55.2 / 69; Bloody 51.75 / 69 / 86.25.

| Wererats | Power | 3 PCs (69) | 4 PCs (92) | 5 PCs (115) |
|---|---|---|---|---|
| 2 | 56 | 65.9% Brutal (8) | 37.1% Bruising (4) | 23.7% Bruising (4) |
| 3 | 84 | 148% Crushing (17) | 83.4% Oppressive (10) | 53.4% Bloody (6) |
| 4 | 112 | 263% Impossible (50) | 148% Crushing (17) | 94.9% Oppressive (10) |

Verdict: 2 wererats is right for 4-5 PCs only. Three or four are lethal below 5 PCs.

**Recommended rosters:**

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | 1 Wererat + 2 Giant Rats | 36 | 27.2% (4) | 1 Wererat + Tough | 44 | 40.7% (6) |
| 4 | 2 Wererats | 56 | 37.1% (4) | 2 Wererats + 2 Giant Rats | 64 | 48.4% (6) |
| 5 | 2 Wererats + Tough | 72 | 39.2% (4) | 3 Wererats | 84 | 53.4% (6) |

Thresholds:
- Kelso calls the fight off when Dasher or a wererat is bloodied, or when any PC drops to 0.
- Each wererat yields at 1/3 HP (20) and retreats to the den; the Shunners stop chasing at the den door.
- Non-combat route: DC 14 Persuasion or Kelso's arranged terms end it at any point (draft).
- Stat block (XMM): Wererat AC 13, 60 HP, speed 30, climb 30, Darkvision 60 ft, Multiattack two attacks (Scratch +5, 6 slashing; Hand Crossbow +5, 6 piercing, humanoid or hybrid form only). It can replace one attack with a Bite.
- **Resistances and immunities: none.** The 2024 Wererat has no damage resistance or immunity in any form, so silvered and magical weapons are not required. No CR adjustment applies. The 2014 silver rule is gone.
- **Curse mechanics.** Bite (rat or hybrid form only): +5, 8 piercing, and if the target is a Humanoid, DC 11 Constitution save. On a failure the target is cursed; if a cursed target drops to 0 HP it becomes a wererat under the DM's control with 10 HP instead. On a success it is immune to that wererat's curse for 24 hours. A pure humanoid-form brawl (Scratch, Hand Crossbow) carries no curse. *Remove Curse* (XPHB) is the cure. Dasher choosing the curse is a DM ruling, not a printed mechanic.
- The Shunners fight in halfling form unless enraged, so the party is not cursed by a routine brawl; a wererat that shifts to hybrid form to bite is the escalation signal.

## 3. M4 Silencing Skeemo (level 5, Tier 2)

Mage CR 6 = 65; Tough CR 1/2 = 12; Warrior Veteran CR 3 = 30. Party Power 96 / 128 / 160. Bruising budget 57.6 / 76.8 / 96; Bloody 72 / 96 / 120.

| PCs | Enemy / Party | % HP lost | Verdict | Day Cost |
|---|---|---|---|---|
| 3 | 65/96 | 45.8% | Bloody | 6 |
| 4 | 65/128 | 25.8% | Bruising | 4 |
| 5 | 65/160 | 16.5% | Mild | 2 |

Stat block (XMM): Mage AC 15, 81 HP, Multiattack three Arcane Burst (+6, 16 force, melee or range 120 ft), Int save +6.

High-Power warning: 65 is more than 2x a 5th-level PC (32 x 2 = 64). Three Arcane Bursts average 48 force damage and Fireball (level 4 version) is 2/day, so a fighting Mage can KO a caster on turn one. If Skeemo stands and fights, apply CR +4 (CR 10, Power 95): 97.9% Oppressive (3 PCs), 55.1% Bloody (4), 35.3% Bruising (5). The rosters below assume he flees or defends (Fly, Invisibility, Misty Step, Shield/Counterspell), and the commuter dray discourages Fireball. If the party corners him and he fights back, step each roster down one row.

**Recommended rosters:**

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Mage at 2/3 HP (54) after the shop scuffle | 53 | 30.5% (4) | Mage at full HP | 65 | 45.8% (6) |
| 4 | Mage alone | 65 | 25.8% (4) | Mage + Warrior Veteran (escort) | 95 | 55.1% (6) |
| 5 | Mage + Tough (escort) | 77 | 23.2% (4) | Mage + Veteran + Tough | 107 | 44.7% (6) |

(A Mage at 2/3 HP = 65 x sqrt(2/3) = about 53.) The escorts trail the dray on foot; the driver and five commuters stay bystanders.

**Concentration rules for the chase (fixes the draft):**
- **Printed 2024 Mage spell list (XMM):** at will *Detect Magic*, *Light*, *Mage Armor* (in AC), *Mage Hand*, *Prestidigitation*; 2/day each *Fireball* (level 4 version) and *Invisibility*; 1/day each *Cone of Cold* and *Fly*; *Misty Step* 3/day (bonus action); Protective Magic 3/day total, choosing *Counterspell* or *Shield* as a reaction. Spell save DC 14.
- **Fly / Greater Invisibility / Counterspell.** The Mage has *Fly* and *Counterspell*. It does **not** have *Greater Invisibility*; it has *Invisibility*.
- *Fly* (XPHB) lasts **1 hour**, Concentration (the draft's 10 minutes is wrong). *Invisibility* is also Concentration and ends when the target attacks or casts. *Greater invisibility* (4th level, **1 minute**, Concentration) is not on the list, so using it is a **named swap** for Skeemo's 2/day *Invisibility*; it lets him attack while unseen but lasts only 10 rounds. Either way it cannot run alongside *Fly*: casting the second ends the first.
- Rooftop chase: he casts *Fly* on round 1 and stays visible (Griffon Cavalry altitude, draft). Do not add invisibility; if he wants to vanish, he drops *Fly*, lands, and casts *Invisibility* (or the swapped *greater invisibility*).
- Street/crowd chase: he casts *Invisibility* on foot; DC 20 Perception or *detect magic* follows the noise. With the swap he lasts 10 rounds; with printed *Invisibility* he lasts until he attacks or casts.
- Party counters: *Counterspell* stops the spell if the caster fails a Constitution save, and the slot is not expended. He can counter theirs three times a day, shared with *Shield*, so a party casting *Counterspell* on *Fly* is a real option.

Thresholds:
- He flees from round 1 by design. He surrenders when cornered at 40 HP (half) or fewer, or after both Misty Step and Fly are spent.
- Escorts flee when Skeemo is captured, or at half HP.
- Non-combat route: the double-agent gambit (Insight DC 18 partial truth, DC 14 fear) ends the fight in a capture.

## 4. M5 The Yellowspire Job (level 6, Tier 2)

Mage CR 6 = 65; Priest Acolyte CR 1/4 = 6 (unverified; see below); Spy CR 1 = 17; Warrior Veteran CR 3 = 30. Party Power 105 / 140 / 175. Bruising budget 63 / 84 / 105; Bloody 78.75 / 105 / 131.25.

**Draft roster as written** (Mage + 3 Spies on the two floors = 116 Power; reinforcement wave of 4 Spies = 68):

| PCs | Wave 1 % lost | Wave 2 % lost | Costs |
|---|---|---|---|
| 3 | 122% Overwhelming | 41.9% Bloody | 13 + 6 |
| 4 | 68.7% Brutal | 23.6% Bruising | 8 + 4 |
| 5 | 43.9% Bloody | 15.1% Mild | 6 + 2 |

Verdict: overwhelming at 3 PCs if the floors ever fight together, and the wave is a fixed size regardless of party. The mission is a stealth heist, so the floors should fight separately; the sizing below assumes the worst case.

**Recommended (standard visit, acolytes replace the sleeping agent):**

| PCs | Wave 1 | Power | % lost (cost) | Wave 2 (10-minute clock) | Power | % lost (cost) | Whole mission |
|---|---|---|---|---|---|---|---|
| 3 | Mage + 1 Priest Acolyte | 71 | 45.7% Bloody (6) | 2 Spies | 34 | 10.5% Mild (2) | about 56%, cost 8 |
| 4 | Mage + 2 Priest Acolytes | 77 | 30.3% Bruising (4) | 3 Spies | 51 | 13.3% Mild (2) | about 44%, cost 6 |
| 5 | Mage + 4 Priest Acolytes | 89 | 25.9% Bruising (4) | 4 Spies | 68 | 15.1% Mild (2) | about 41%, cost 6 |

**Reinforced return visit (Faction Outposts 5B ran):**

| PCs | Wave 1 | Power | % lost (cost) | Wave 2 | Power | % lost (cost) | Whole mission |
|---|---|---|---|---|---|---|---|
| 3 | Mage + 2 Priest Acolytes | 77 | 53.8% Bloody (6) | 3 Spies | 51 | 23.6% Bruising (4) | about 77%, cost 10 |
| 4 | Mage + 4 Priest Acolytes | 89 | 40.4% Bloody (6) | 4 Spies | 68 | 23.6% Bruising (4) | about 64%, cost 10 |
| 5 | Mage + 4 Priest Acolytes + Warrior Veteran | 119 | 46.2% Bloody (6) | 5 Spies | 85 | 23.6% Bruising (4) | about 70%, cost 10 |

Cost 10 sits between Draining (9) and Debilitating (12) on the fatigue table. Agorn Fuoco (one-in-three per arc-e) is a named NPC; his stats are not set here. If he appears, remove the Veteran and one Spy per Power swapped, and stat him through boss-design or as a Mage.

Stat blocks (XMM): Priest Acolyte CR 1/4, AC 13, 11 HP, Mace 5 + 2 radiant, Radiant Flame 7 (range 60), Divine Aid 1/day (*Bless*, *Healing Word* or *Sanctuary*). Spy CR 1, AC 12, 27 HP, one attack (Shortsword or Hand Crossbow, 5 piercing + 7 poison), Cunning Action; no Multiattack. Mage per section 3.

First-turn KO: a Mage that opens with three Arcane Bursts can KO a squishy 6th-level PC (CR 10, Power 95). Wave 1 under that assumption is 101 / 107 / 119 for 3 / 4 / 5 PCs (after swapping 65 for 95 and keeping the recommended acolytes), or 92.5% / 58.4% / 46.2%. The rosters above assume the draft's behaviour (Counterspell on the first spell, then fall back to the circle and raise the alarm). If she fights, drop one acolyte per size.

Thresholds:
- Acolytes flee or yield when the first ally falls or at half HP.
- The Mage uses Protective Magic (*Counterspell*, 3/day shared with *Shield*) on the first visible spell, then falls back toward the circle; she yields at 1/4 HP (about 20) and will not use the circle while the party is adjacent.
- Wave 2 Spies disengage once two of them are down or the ledger holder has left the building.
- Clock trigger: the wave arrives ten minutes after anyone steps into the circle without pressing the northeast plate, or after the Mage raises an alarm.
- Non-combat routes: coded knock, rooftop, referral cover (draft).

## 5. M6 Ziraj's Last Hunt (level 7, after Kolat Towers, Tier 2)

Assassin CR 8 = 85; Warrior Veteran CR 3 = 30; Spy CR 1 = 17. Party Power 123 / 164 / 205. Bruising budget 73.8 / 98.4 / 123; Bloody 92.25 / 123 / 153.75.

**Draft roster (3 Spies = 51):**

| PCs | % HP lost | Verdict | Day Cost |
|---|---|---|---|
| 3 | 17.2% | Mild | 2 |
| 4 | 9.7% | Below Mild | 2 |
| 5 | 6.2% | Below Mild | 2 |

Verdict: trivial for a mission that closes the chain.

**Leader options:**

| Roster | Power | 3 PCs | 4 PCs | 5 PCs |
|---|---|---|---|---|
| Assassin alone | 85 | 47.8% Bloody | 26.9% Bruising | 17.2% Mild |
| Assassin + 1 Spy | 102 | 68.8% Brutal | 38.7% Bruising | 24.8% Bruising |
| Assassin + 2 Spies | 119 | 93.6% Oppressive | 52.7% Bloody | 33.7% Bruising |
| Assassin + 3 Spies | 136 | - | - | 44.0% Bloody |
| Assassin + Veteran + 2 Spies | 149 | - | - | 52.8% Bloody |
| Veteran + 2 Spies | 64 | 27.1% Bruising | - | - |

**Recommended rosters:**

| PCs | Standard (Bruising) | % lost (cost) | Hard (Bloody) | % lost (cost) |
|---|---|---|---|---|
| 3 | Warrior Veteran + 2 Spies | 27.1% (4) | Assassin alone | 47.8% (6) |
| 4 | Assassin + 1 Spy | 38.7% (4) | Assassin + 2 Spies | 52.7% (6) |
| 5 | Assassin + 2 Spies | 33.7% (4) | Assassin + Veteran + 2 Spies | 52.8% (6) |

Notes:
- Stat block (XMM): Assassin AC 16, 97 HP, Dex save +7, resists poison, Evasion, Cunning Action, Multiattack **three attacks** (Shortsword +7, 7 piercing + 17 poison, and Poisoned; or Light Crossbow +7, range 80/320, 8 piercing + 21 poison). There is no Assassinate or Sneak Attack line in the 2024 block.
- High-Power warning and first-turn KO: Assassin (85) is more than 2x a 7th-level PC (82), and one full round is about 72-87 damage on one target, enough to drop most 7th-level characters. With CR +4 (CR 12, Power 140) the leader alone is 130% Crushing (3 PCs), 72.9% Brutal (4), 46.6% Bloody (5). To keep the base figures honest, cap the Assassin at two attacks on its first turn (a named modification: it has not yet read the party) and keep the draft's party initiative advantage. Without that modification, step each roster down one row.
- The XMM Assassin carries a light crossbow, which matches Fala's grooved-tip bolts. Ziraj's oversized longbow is a swap on his own NF-page block, not on the kill team.
- Ziraj is not counted: wounded, Disadvantage on the bow, and a potential objective. If he fights, that adds a second Assassin-class ally (Power 85 at full strength, roughly half if wounded), which erases the challenge. Keep him as a sniper for two rounds at most.
- Spies do 12 per hit (5 piercing + 7 poison) and Warrior Veteran (AC 17, 65 HP, Multiattack two attacks, Greatsword 10, Parry reaction) is the sturdy option for the 3-PC row.

Thresholds:
- Spies disengage and report when two of the team are down or when the leader falls (draft).
- Leader retreats at half HP if an ally has fallen; the Assassin will not surrender, but will trade information for her life if paralyzed or held.
- The team is not a suicide squad: a kill team that reports back is worth more than one that dies (draft).
- Non-combat route: leading them away from Ziraj (DC 14 Deception or a planted trail).

## 6. r50 Ally Power: Dread Lord operatives (8-operative pool)

r50 is Dungeon of the Mad Mage content; assume level 8-10 (Tier 2). Level 8 Party Power is 44 each: 132 / 176 / 220. Tier 3 is provided in case the party has reached level 11.

**Pool (proposed composition):**

| Operative | CR | Count | Power each (T2) | Power each (T3) | T2 total | T3 total |
|---|---|---|---|---|---|---|
| Mage | 6 | 1 | 65 | 50 | 65 | 50 |
| Warrior Veteran | 3 | 2 | 30 | 25 | 60 | 50 |
| Spy | 1 | 2 | 17 | 15 | 34 | 30 |
| Tough | 1/2 | 2 | 12 | 7 | 24 | 14 |
| Priest Acolyte | 1/4 | 1 | 6 | 5 | 6 | 5 |
| **Pool** | | **8** | | | **189** | **149** |

Deployment packages (Davil sets operational limits; use one package per operation):

| Package | Members | Power (T2) |
|---|---|---|
| Strike Team | Mage, Warrior Veteran, Spy, Tough | 124 |
| Cover Team | Warrior Veteran, Spy, Tough, Priest Acolyte | 65 |
| Full pool | all eight | 189 |

**Party Power and budgets with allies (level 8):**

| PCs | Base | + Cover (65) | + Strike (124) | + Full (189) |
|---|---|---|---|---|
| 3 | 132 | 197 (Bruising budget 118) | 256 (154) | 321 (193) |
| 4 | 176 | 241 (145) | 300 (180) | 365 (219) |
| 5 | 220 | 285 (171) | 344 (206) | 409 (245) |

Guidance:
- The full pool roughly doubles a 4-PC party, so a fight built for the base party is trivial with it. Rebuild the encounter from the allied Party Power, or cap deployment at the Cover Team unless the operation is meant to be a set piece.
- Ally Power counts in full under the skill's rule. For a "one major operation" allotment, expect operatives to be spent (one casualty per package is a fair cost) rather than recovered.
- Recommended default: Strike Team for assault operations, Cover Team for extraction and distraction. The Vault partnership crews (distraction, locksmith, wagon team) are non-combat and add no Power.

## Verification

Checked against the 2024 *Monster Manual* (XMM) and *Player's Handbook* (XPHB) records in the mirror files named in Method.

| Name / item | Status | Note |
|---|---|---|
| Scout, Bandit, Spy, Assassin, Mage, Wererat, Giant Rat | Verified (XMM) | CR 1/2, 1/8, 1, 8, 6, 2, 1/8. |
| Warrior Veteran | Verified (XMM) | CR 3, AC 17, 65 HP. "Veteran" does not exist in XMM. |
| Tough | Verified (XMM) | CR 1/2, AC 12, 32 HP, Pack Tactics. "Thug" does not exist in XMM. |
| Priest Acolyte | Verified (XMM) | CR 1/4, AC 13, 11 HP. Power 6 stands; the CR 2 sensitivity note is removed. |
| Bandit Captain, Mage Apprentice | Verified, unused | CR 2 each; available as hired-leader or junior-caster options. |
| Wererat resistances | Verified: none | No damage resistances or immunities; curse is Bite only, DC 11 Con. |
| Mage spell list | Verified | Has *Fly*, *Counterspell*, *Invisibility*, *Fireball*, *Cone of Cold*, *Misty Step*, *Shield*. No *Greater Invisibility*. |
| *Fly* duration | Verified | 1 hour, Concentration. The draft's 10 minutes is wrong. |
| *Greater invisibility* | Verified | 1 minute, Concentration; a named swap for the Mage's *Invisibility*. |
| Scout weapon | Verified | Longbow, not shortbow; the hand crossbow is a swap. |
| Assassin attacks | Verified | Three attacks per Multiattack; no Assassinate. First-turn KO applies. |
| Agorn Fuoco | Not statted | Named NPC, out of scope here. |
