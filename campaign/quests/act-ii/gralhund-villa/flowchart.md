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
| 1 | ev-06 or ev-07 | Party engages the Gralhund confrontation — whichever path fires | 1 | 8 |
| 2 | ev-09 | Stone of Golorr in party hands at Aftermath opening | 1 | 9 → **Level 4** |

Milestone 1 fires in exactly one confrontation event per playthrough — ev-06 (day path) or ev-07 (night path), never both. Milestone 2 is conditional: fires only if the party holds the Stone. A successful ev-08 rooftop chase still enables Milestone 2 in ev-09 if the Stone is recovered.

---

## Event Outcome Summary

### Read from Prior Quests

| Event Outcome | Source | Read In |
|---|---|---|
| Jarlaxle Informed | **Fireball!** ev-04 | ev-01 (Jarlaxle contact available), ev-02 (BD team at Artheyn Manor), ev-06/ev-07 (BD assault fires) |
| Gralhund Villa Named | **Fireball!** ev-01 | ev-01 (Renaer contact available), ev-02 (Renaer contingency) |

### Set During Gralhund Villa

| Event Outcome | Where Marked | Read By |
|---|---|---|
| Mirt Brief Received, Davil Brief Received, Jalester Brief Received, Vajra Brief Received | ev-01 | ev-09 (debrief tone) |
| Jarlaxle Brief Received | ev-01 | ev-02, ev-06 and ev-07 (Yalah's negotiation tone) |
| Zhents Spotted, Gazers Spotted, BD Team Spotted | ev-02 | ev-03, ev-03c and ev-04 (entry advantages) |
| Day Entry | ev-02 | ev-03 vs ev-04 routing |
| Chirada Letter Found | ev-03 or ev-03b (also on the G12 room page) | **Faction Outposts** (Yellowspire teleportal lead) |
| Grand Game Journal Found | G11 room file (DC 15 Investigation, any state) | ev-09 (lore table) |
| G16 Compartment Found | G16 room file (DC 15 Perception, any state) and ev-09 | **Cassalanter Villa** (Cassalanter cult link) |
| Orond Confession Heard | ev-03, ev-03b or ev-05 | ev-09 |
| Front Door Visit Recorded | ev-03b | ev-09 (Yalah's debrief attitude) |
| Balcony Entry Used | ev-03c | ev-07 (the party bypasses ev-04) |
| Pantry Entry Used | ev-03c | ev-04 (the raid begins in the kitchen corridor) |
| Gazers Active at Night | ev-03c | No event reads it yet |
| Floxin Alive | ev-04 | **Kolat Towers** (Manshoon response team) |
| Floxin Captured | ev-04 | No event reads it yet |
| Stone Secured | ev-06 or ev-07 | ev-08 trigger (fires when not marked); ev-09 (Stone status check, Milestone 2, Jarlaxle package, BD debrief) |
| Stone Recovered | ev-08 | ev-09 (Milestone 2, BD debrief) |
| Yalah Missing, Yalah In Custody | ev-09 | No event reads them yet |
| Istrid Horn Helped / Istrid Horn Turned In | ev-09 | **Faction Outposts** (Doom Raiders renown) |
