# Data Dictionary

**Week:** 2  
**Purpose:** Define raw, reference, Silver, and streaming fields for the **RoadSafe Collision Risk Analytics** project.

---

# 1. Source File Catalog

| File Name | Grain | Purpose | Approx. Rows | Notes |
|-----------|--------|---------|-------------:|------|
| `collisions.csv` | One reported personal-injury road collision | Core event data | 101,527 | Parent file; key is `collision_index` |
| `vehicles.csv` | One vehicle involved in one collision | Involved vehicle details | 183,514 | Composite key (`collision_index`, `vehicle_reference`) |
| `casualties.csv` | One casualty recorded in one collision | Victim and injury details | 128,272 | Composite key (`collision_index`, `casualty_reference`) |
| `collision_code_lookup.csv` | One official code-to-description mapping | Decode categorical fields | 1,401 | Join on `lookup_domain` and `code` |
| `incident_alert_drop_*.json` | One simulated incident alert event | Streaming simulation | 34 | 6 total JSON Lines drops |

---

# 2. Raw File Schema: `collisions.csv`

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| `collision_index` | String | Yes | `202417M119024` | Unique parent record ID; must remain string |
| `date` | String | Yes | `05/12/2024` | DD/MM/YYYY format; parsed to DATE in Silver |
| `time` | String | No | `16:10` | HH:MM format; parsed to TIMESTAMP in Silver |
| `collision_severity` | Integer | Yes | `3` | 1 = Fatal, 2 = Serious, 3 = Slight |
| `longitude` | Double | No | `-1.42873` | Valid UK bounds: -9 to 3 |
| `latitude` | Double | No | `52.89721` | Valid UK bounds: 49 to 61 |

---

# 3. Raw File Schema: `vehicles.csv`

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| `collision_index` | String | Yes | `2024471526976` | Foreign key linking to parent collision |
| `vehicle_reference` | Integer | Yes | `2` | Unique vehicle ID within a specific collision |
| `vehicle_type` | Integer | Yes | `9` | Coded vehicle category (e.g., 9 = Car) |
| `age_of_driver` | Integer | No | `23` | Age in years; `-1` represents missing or out-of-range |

---

# 4. Reference File Schema: `collision_code_lookup.csv`

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| `lookup_domain` | String | Yes | `police_force` | Category of codes being mapped |
| `code` | Integer | Yes | `6` | Raw numeric value from source files |
| `description` | String | Yes | `Greater Manchester` | Human-readable label for the code |

---

# 5. Canonical Silver Table Design

**Final Silver Table Name:** `silver_collisions_candidate`

| Silver Field | Data Type | Source Mapping | Business Meaning |
|--------------|-----------|----------------|------------------|
| `record_id` | String | `row_hash` | Deterministic unique record ID for reconciliation |
| `collision_timestamp` | Timestamp | `date + time` | Combined and parsed UTC event time |
| `severity_desc` | String | `lookup.description` | Decoded human-readable severity label |
| `is_severe_flag` | Integer | `collision_severity` | 1 if Fatal or Serious, else 0 |
| `is_vulnerable_user` | Integer | Derived | Flag for pedestrians, cyclists, or motorcyclists |

---

# 6. Streaming Event Schema

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| `incident_event_id` | String | Yes | `RS-EVT-0001` | Unique simulation event ID |
| `event_timestamp` | Timestamp | Yes | `2024-11-15T08:00:00Z` | Recorded time of simulated alert |
| `event_type` | String | Yes | `INCIDENT_CREATED` | Type of life-cycle update |
| `status` | String | Yes | `REPORTED` | Progression: REPORTED → RESPONDING → CLEARED |
| `collision_reference` | String | Yes | `202417M119024` | Links alert back to historical `collision_index` |

---
