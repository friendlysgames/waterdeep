# Arc A — Event Flowchart

```
Campaign Start
      │
      ▼
ev-01 — The Yawning Portal
  [Social Event — 1st level]
  Bar brawl → Dip ritual → Troll fight → Volo's quest
  Attunements: Durnan's Acknowledgment / Yagra's Courtesy
      │
      ▼
ev-02 — Dock Ward Investigation
  [Exploration Event — 1st level]
  3 paths → Revelation #1 (who took Floon)
  3 paths → Revelation #2 (Candle Lane warehouse)
  Proactive failsafes if all paths fail
      │
      ▼
ev-03 — Zhentarim Warehouse ────────── Milestone: 1 point
  [Exploration/Combat Event — 1st level]
  Entry choice (3 entry points; kenku alert state)
  Kenku confrontation
  Finding Renaer → knowledge state
  3 paths → Revelation #3 (sewer hideout)
  Attunements: Renaer Neverember Found / Warehouse Cleared
  See: Zhentarim Warehouse journal (Z01–Z05)
      │
      ▼
ev-04 — Xanathar Sewer Hideout ─────── Milestone: 1 point → Level 2
  [Exploration/Combat Event — 1st level]
  Sewer navigation (3 DC 13 checks)
      │
      ├─ 0 successes → Q07 (Floon dead — arc failure state)
      │
      └─ 1–3 successes → Q01 Entry
            │
            ├─ Gazer fight (noise) → Alert state at Q01
            └─ Gazer bypassed → Unaware state at Q01
                  │
                  ▼
            Hideout infiltration (Q01 → Q06)
            Floon in Q07 (alive)
            Nihiloor escapes through Q11 portal (Arc F seed)
            Q09 Peabody cellar / Q08 escape tunnel (Arc B resource)
            Q10 empty sleeping quarters
            Volo's payment → Deed to Trollskull Manor
            Attunements: Floon Rescued / Nihiloor Sighted / Deed to Trollskull Manor
            See: Xanathar Sewer Hideout journal (Q01–Q11)
      │
      ▼
Arc B — Trollskull Alley
  See: Arc B Overview for entry conditions
```

## Notes

**Failure state:** A party that fails all three sewer navigation checks arrives at Q07 to find Floon dead. This is the arc's only hard failure outcome. The deed to Trollskull Manor is still delivered by Volo regardless — he honors the attempt. Arc B begins either way; Floon's absence is a running thread in Arc B rather than a campaign-ending event.

**Milestone sequencing:** Both milestone events must be completed for the party to reach Level 2. A party that skips the warehouse and goes directly to the sewer via the bead trail earns Milestone 2 before Milestone 1; level-up still triggers when the second point is awarded (cumulative threshold = 2 regardless of order).

**Krentz continuity:** If Krentz survived the brawl in ev-01 (party used a peaceful resolution or stayed out), he appears in Q05 of the sewer hideout recovering from the YP incident. His presence gives the kenku in Q05 advantage on initiative (he warns them in time). This is the only cross-event mechanical consequence in Arc A.
