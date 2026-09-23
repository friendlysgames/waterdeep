# Gralhund Villa — Event Flowchart

```
START
  │
  ▼
ev-01: What the Factions Say
  (six contacts; Jarlaxle conditional on Jarlaxle Informed)
  │
  ▼
ev-02: Saerdoun Street
  (three observation teams; day/night commitment)
  │
  ├── [Day path: arrive before Ches 24th nightfall]
  │       │
  │       ▼
  │     ev-03: Daytime Infiltration
  │       (entry approaches; Alarm escalation; Orond in G12)
  │       │
  │       ├── [Raid arrives while party inside: day-to-night chain]
  │       │       │
  │       │       ▼
  │       │     ev-04: The Zhentarim Raid
  │       │       (10-beat timeline; BD fires if Jarlaxle Informed)
  │       │       │
  │       │       ▼
  │       │     ev-05: The Guest Suite
  │       │       (Floxin at G15; Orond's four revelations)
  │       │       │
  │       │       ▼
  │       │     ev-07: Confrontation — Night ◄─────── MILESTONE 1
  │       │       │
  │       │       ├── [Stone in hand] ──────────────────────────────────────────┐
  │       │       └── [Stone escaped] ──► ev-08: The Rooftop Chase ─────────────┤
  │       │                                                                       │
  │       └── [Party moves to confront before raid]                              │
  │               │                                                               │
  │               ▼                                                               │
  │             ev-06: Confrontation — Day ◄──────── MILESTONE 1                 │
  │               │                                                               │
  │               ├── [Stone in hand] ─────────────────────────────────────────┐ │
  │               └── [Stone escaped] ──► ev-08: The Rooftop Chase ────────────┤ │
  │                                                                              │ │
  └── [Night path: arrive Ches 24th night, raid in progress]                    │ │
          │                                                                      │ │
          ▼                                                                      │ │
        ev-04: The Zhentarim Raid                                                │ │
          (10-beat timeline; BD fires if Jarlaxle Informed)                      │ │
          │                                                                      │ │
          ▼                                                                      │ │
        ev-05: The Guest Suite                                                   │ │
          (Floxin at G15; Orond's four revelations)                              │ │
          │                                                                      │ │
          ▼                                                                      │ │
        ev-07: Confrontation — Night ◄────────── MILESTONE 1                    │ │
          │                                                                      │ │
          ├── [Stone in hand] ─────────────────────────────────────────────────┘│
          └── [Stone escaped] ──► ev-08: The Rooftop Chase ─────────────────────┘
                                                                                  │
                                                                                  ▼
                                                              ev-09: Aftermath ◄── MILESTONE 2 (conditional)
                                                                (Stone in hand → Level 4)
                                                                (Davil arrested; Tashlyn takes over)
                                                                (Istrid Horn scene)
                                                                (six faction debriefs)
```

---

## Milestone Summary

| # | Event | Condition | Points | Cumulative |
|---|-------|-----------|--------|-----------|
| 1 | ev-06 or ev-07 | Party engages the Gralhund confrontation — whichever path fires | 1 | 9 |
| 2 | ev-09 | Stone of Golorr in party hands at Aftermath opening | 1 | 10 → **Level 4** |

Milestone 1 fires in exactly one confrontation event per playthrough — ev-06 (day path) or ev-07 (night path), never both. Milestone 2 is conditional: fires only if the party holds the Stone. A successful ev-08 rooftop chase still enables Milestone 2 in ev-09 if the Stone is recovered.

---

## Attunement Summary

### Read from Prior Arcs

| Attunement | Source | Read In |
|---|---|---|
| Jarlaxle Informed | Arc C ev-04 | ev-01 (Jarlaxle contact available), ev-02 (BD team at Artheyn Manor), ev-06/ev-07 (BD assault fires) |
| Gralhund Villa Named | Arc C ev-03 | ev-01 (Renaer contact available), ev-02 (Renaer contingency) |

### Set During Arc D

| Attunement | Where Set | Read By |
|---|---|---|
| Faction Brief Received (per contact) | ev-01 | ev-09 (debrief tone) |
| Observation Teams Spotted | ev-02 | ev-03/ev-04 (entry advantages) |
| Villa Approach: Day / Night | ev-02 | ev-03 vs ev-04 routing |
| G12 Searched: Chirada Letter | ev-03 (daytime) | Arc E (Yellowspire/Second Eye lead) |
| Grand Game Journal Found | G11 room file (DC 15 — any state) | ev-09 end-state ledger |
| G16 Asmodean Compartment Searched | G16 room file (DC 15 Perception — any state) | Arc G (Cassalanter cult link) |
| Orond's Confession: Heard / Missed | ev-03 (day) or ev-05 (night) | ev-09 |
| Floxin Status: Alive / Dead / Captured | ev-04 or ev-05 | Arc I (Manshoon response team) |
| Stone Holder: Party / BD / Zhent / Xanathar | ev-06 or ev-07 | ev-08 trigger; ev-09 Milestone 2 |
| Istrid Horn Outcome | ev-09 | Arc E (Doom Raiders renown) |
