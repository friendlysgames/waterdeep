---
name: cr2-encounter-builder
description: >
  Use this skill to build, evaluate, or balance D&D 5e combat encounters using
  the Challenge Ratings 2.0 system by DragnaCarta. Trigger whenever the user
  asks to build an encounter, check if a fight is balanced, calibrate difficulty,
  figure out how many monsters to use, plan an adventuring day, or compare
  encounter difficulty for their party. Also trigger when the user mentions
  "CR 2.0", "Challenge Ratings 2.0", "DragnaCarta encounter", "party power",
  "encounter power budget", or asks things like "is this encounter too hard?"
  or "what CR monsters should I use for a level X party?" Always use this skill
  — do not attempt encounter math from memory or the default DMG XP system.
---

# Challenge Ratings 2.0 — Encounter Builder Skill

This skill implements the **Challenge Ratings 2.0** system by DragnaCarta. It
replaces the broken DMG XP system with a mathematically grounded Power-based
approach. The core idea: every PC and every monster has a **Power** score.
Compare them to set difficulty.

**This skill uses a hybrid workflow:**
- **Party Power** → always use the **Basic Guide** (level lookup table). Fast and consistent.
- **Monster Power** → always use the **Advanced Guide** (tier-adjusted table). More accurate because monster effectiveness varies significantly depending on the party's level tier.

Never use the Basic flat monster table. Never use the Advanced LP calculation for PCs unless the user explicitly asks for it.

---

## PART I — PARTY POWER (Basic)

### Step 1 · Party Power

Look up each PC's level in the table below and sum all values. Include any NPC
allies or summoned monsters (use the tier-adjusted Monster Power table in Part II).

| Level | Power | Level | Power | Level | Power | Level | Power |
|-------|-------|-------|-------|-------|-------|-------|-------|
| 1     | 11    | 6     | 35    | 11    | 62    | 16    | 84    |
| 2     | 14    | 7     | 41    | 12    | 68    | 17    | 103   |
| 3     | 18    | 8     | 44    | 13    | 71    | 18    | 119   |
| 4     | 23    | 9     | 49    | 14    | 74    | 19    | 131   |
| 5     | 32    | 10    | 53    | 15    | 82    | 20    | 141   |

**Party Power = sum of all PC Power scores (+ ally Power if any)**

### Step 2 · Encounter Difficulty & Budget

Pick the intended difficulty. Multiply Party Power by the Multiplier to get the
**Encounter Power Budget**.

Difficulty is defined by the estimated **% of party HP lost**, derived from:
> (Total Enemy Power ÷ Party Power)² = % HP lost

| Difficulty   | HP Lost   | Multiplier | Day Cost |
|--------------|-----------|------------|----------|
| Mild         | 0–20%     | 0.40       | 2        |
| Bruising     | 20–40%    | 0.60       | 4        |
| Bloody       | 40–60%    | 0.75       | 6        |
| Brutal       | 60–80%    | 0.90       | 8        |
| Oppressive   | 80–100%   | 1.00       | 10       |
| Overwhelming | 100–130%  | 1.10       | 13       |
| Crushing     | 130–170%  | 1.30       | 17       |
| Devastating  | 170–250%  | 1.60       | 25       |
| Impossible   | 250–500%  | 2.25       | 50       |

> Difficulties above Oppressive are for experienced DMs only. They assume
> tactics, terrain, or optimized builds may allow a win despite the odds.

> **Encounter Power Budget = Party Power × Multiplier**

When **evaluating** an existing monster list, calculate the effective multiplier
as `Total Enemy Power ÷ Party Power`, then square it to find estimated HP lost,
and match to the table above.

Now go to **Part II** to look up Monster Power and choose monsters.

### Step 3 · Adventuring Day Fatigue

Sum the **Day Cost** of all encounters planned for the day.

| Total Cost | Fatigue Level    | What it means                              |
|------------|------------------|--------------------------------------------|
| 2          | Light            | PCs use few resources                      |
| 4          | Moderate         | PCs use some resources                     |
| 6          | Taxing           | PCs use a large minority of resources      |
| 9          | Draining         | PCs use a majority of resources            |
| 12         | Debilitating     | PCs use nearly all resources               |
| 15         | Exhausting       | PCs use all resources                      |

### ⚠ High-Power Monster Warning

Be cautious with any monster whose Power is **≥ 2× any individual PC's Power**. These monsters may deal enough damage to knock out a PC in a single hit, removing them from combat and triggering a death spiral the party may not recover from.

### ⚠ Special CR Warning

The following monsters have abilities that **bypass HP entirely** — draining stats, instant kills, or similar effects — making them far more dangerous than their Power score suggests. Use only with experienced players: **shadow**, **intellect devourer**, **sea hag**, **banshee**.

## PART II — MONSTER POWER (Advanced, Tier-Adjusted)

**Always use this section for monsters.** Never use a flat monster power table.
Monster effectiveness changes with tier because PCs' attack bonuses and AC improve
with level, making the same monster relatively weaker at higher tiers.

### Tier of Play

| PC Levels | Tier |
|-----------|------|
| 1–4       | 1    |
| 5–10      | 2    |
| 11–16     | 3    |
| 17–20     | 4    |

### Monster Power by CR and Tier

Choose monsters whose total Power ≈ Encounter Power Budget (within ~5% is fine).

| CR    | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|-------|--------|--------|--------|--------|
| 0     | 1      | 1      | 0      | 0      |
| 1/8   | 4      | 3      | 3      | 2      |
| 1/4   | 10     | 6      | 5      | 4      |
| 1/2   | 16     | 12     | 7      | 5      |
| 1     | 22     | 17     | 15     | 8      |
| 2     | 28     | 23     | 19     | 14     |
| 3     | 37     | 30     | 25     | 19     |
| 4     | 48     | 38     | 32     | 24     |
| 5     | 70     | 60     | 45     | 40     |
| 6     | 80     | 65     | 50     | 40     |
| 7     | 90     | 70     | 55     | 45     |
| 8     | 105    | 85     | 70     | 55     |
| 9     | 110    | 85     | 70     | 55     |
| 10    | 115    | 95     | 75     | 60     |
| 11    | 140    | 130    | 105    | 85     |
| 12    | 150    | 140    | 115    | 90     |
| 13    | 160    | 150    | 120    | 95     |
| 14    | 165    | 155    | 125    | 100    |
| 15    | 175    | 165    | 130    | 105    |
| 16    | 185    | 175    | 140    | 110    |
| 17    | 250    | 200    | 190    | 150    |
| 18    | 260    | 210    | 200    | 160    |
| 19    | 280    | 220    | 210    | 170    |
| 20    | 300    | 240    | 230    | 180    |
| 21    | 400    | 350    | 275    | 250    |
| 22    | 450    | 375    | 300    | 275    |
| 23    | 500    | 425    | 325    | 325    |
| 24    | 550    | 450    | 375    | 350    |
| 25    | 600    | 500    | 400    | 375    |
| 26    | 650    | 525    | 425    | 400    |
| 27    | 725    | 600    | 475    | 450    |
| 28    | 775    | 625    | 500    | 475    |
| 29    | 775    | 650    | 525    | 475    |
| 30    | 850    | 725    | 575    | 525    |

**CR adjustments:**
- Monster has resistance/immunity to all nonmagical weapon damage AND all PCs can consistently deal magical damage → **decrease CR by 2** before looking up Power
- Monster can kill or KO one or more PCs on the **first turn of combat** → **increase CR by 4** before looking up Power

### Magic Items & Adventuring Day (Optional)

Start with the base Total Cost from all encounters. Then for each **consumable
or fully-charged magical item** a PC can use to deal damage, restore HP, or
inflict conditions, look up its **Resource Modifier** and divide by the number
of PCs. Add the result to the Total Cost.

| Party Level | Uncommon     | Rare          | Very Rare      | Legendary      |
|-------------|--------------|---------------|----------------|----------------|
| 1–4         | 15 (cons: 2) | 120 (cons: 17)| 360 (cons: 51) | 600 (cons: 85) |
| 5–10        | 2 (cons: 0)  | 15 (cons: 2)  | 45 (cons: 6)   | 75 (cons: 10)  |
| 11–16       | 1 (cons: 0)  | 5 (cons: 0)   | 15 (cons: 2)   | 25 (cons: 3)   |
| 17–20       | 0 (cons: 0)  | 3 (cons: 0)   | 9 (cons: 1)    | 15 (cons: 2)   |

> Use the value in parentheses for **consumable** items; use the main value for
> a fully-charged rechargeable item.

Aim for ~**2 short rests per day** to keep short-rest classes (Warlock, Fighter,
Monk, Barbarian) on par with long-rest classes.

### Notes on Waves and Multi-Phase Bosses

Build each wave or boss phase as a **separate encounter**, then **add their Day
Costs together** to get the total difficulty of the whole encounter.

---

## HOW TO PRESENT RESULTS

When building an encounter, show your work clearly:

1. **Party Power** — list each PC (and ally) with their Power score and the total
2. **Encounter Power Budget** — show the multiplication
3. **Proposed monsters** — list CR, name, Power, and running total
4. **Verdict** — state the difficulty and whether the budget is hit (within ~5%)
5. **Adventuring day context** — mention the Day Cost and where it fits on the fatigue scale if the user asked about daily pacing

If the user provides a monster list and asks "is this balanced?", evaluate it:
calculate Party Power, calculate total monster Power at the appropriate tier,
then compute `(Enemy Power ÷ Party Power)²` to find estimated % HP lost, and
match that to the difficulty table.

---

## WHY THIS SYSTEM EXISTS

The DMG XP system fails because:
1. Monster XP values don't scale proportionally with actual monster strength
2. Multiple monsters are far more powerful than their combined XP suggests
3. More players aren't proportionally accounted for

CR 2.0 fixes this by modeling Power as `√(effective HP × effective DPR)` —
the geometric mean of offense and defense — which correctly captures how combat
actually plays out. Enemy Power / Party Power, squared, estimates the fraction
of HP the party will lose. This is what the difficulty tiers map to.

---

*System by DragnaCarta. Reference: https://www.gmbinder.com/share/-N4m46K77hpMVnh7upYa*
*Calculator: https://www.challengerated.com*
