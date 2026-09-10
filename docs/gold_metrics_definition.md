# Gold Metrics Definition

**Week:** 7  
**Purpose:** Define project-specific Gold tables and KPI formulas from approved Trusted Silver inputs.

---

## 1. Gold Table Catalog

| Gold Table Name | Grain | Source Table | Primary KPI | Status |
|---|---|---|---|---|
| `gold_collision_monthly_summary` | One row per collision year + collision month + urban/rural group | `trusted_silver_collisions` | Monthly Collision Count | Built and validated |
| `gold_vehicle_type_summary` | One row per collision year + vehicle type | `trusted_silver_vehicles` | Vehicle Involvement by Vehicle Type | Built and validated |
| `gold_casualty_severity_summary` | One row per collision year + casualty age group + casualty severity | `trusted_silver_casualties` | Casualty Count by Severity and Age Group | Built and validated |

---

## 2. KPI Definitions

| KPI Name | Formula | Grain | Gold Table | Notes |
|---|---|---|---|---|
| **Monthly Collision Count** | `COUNT(*)` over eligible collision records | Collision year + collision month + urban/rural group | `gold_collision_monthly_summary` | Eligible rows have `collision_index IS NOT NULL` |
| **Vehicle Involvement by Vehicle Type** | `COUNT(*)` over eligible vehicle records | Collision year + vehicle type | `gold_vehicle_type_summary` | Eligible rows have `vehicle_key IS NOT NULL` |
| **Casualty Count by Severity and Age Group** | `COUNT(*)` over eligible casualty records | Collision year + casualty age group + casualty severity | `gold_casualty_severity_summary` | Eligible rows have `casualty_key IS NOT NULL` |

---

## 3. KPI 1 — Monthly Collision Count

### Business Question

How does the number of eligible collisions vary by month and urban/rural setting?

### Source

`trusted_silver_collisions`

### Eligible Rows

Rows where:

`collision_index IS NOT NULL`

### Outside Scope

Rows where:

`collision_index IS NULL`

These rows remain in Trusted Silver and are not deleted.

### Output Dimensions

- `collision_year`
- `collision_month`
- `urban_rural_group`

### Output Measures

- `collision_count`
- `severe_collision_count`
- `severe_collision_rate`

### Supporting Measure Formulas

`collision_count = COUNT(*)`

`severe_collision_count = COUNT(*) WHERE severe_collision_flag = 1`

`severe_collision_rate = 100 × severe_collision_count / collision_count`

### Gold Table

`gold_collision_monthly_summary`

### Validation

- Grain uniqueness
- Key completeness
- Measure validity
- Eligible-row reconciliation
- Severe-collision reconciliation
- Scope reconciliation
- Delta table validation
- Controlled rerun comparison

---

## 4. KPI 2 — Vehicle Involvement by Vehicle Type

### Business Question

How many eligible vehicle records are represented for each vehicle type across collision years?

### Source

`trusted_silver_vehicles`

### Eligible Rows

Rows where:

`vehicle_key IS NOT NULL`

### Outside Scope

Rows where:

`vehicle_key IS NULL`

These rows remain in Trusted Silver and are not deleted.

### Output Dimensions

- `collision_year`
- `vehicle_type`

### Output Measure

`vehicle_involvement_count`

### Formula

`vehicle_involvement_count = COUNT(*)`

### Gold Table

`gold_vehicle_type_summary`

### Validation

- Grain uniqueness
- Key completeness
- Negative measure check
- Eligible-row reconciliation
- Scope reconciliation
- Delta table validation
- Controlled rerun comparison

---

## 5. KPI 3 — Casualty Count by Severity and Age Group

### Business Question

How are eligible casualties distributed across age groups and casualty severity levels?

### Source

`trusted_silver_casualties`

### Eligible Rows

Rows where:

`casualty_key IS NOT NULL`

### Outside Scope

Rows where:

`casualty_key IS NULL`

These rows remain in Trusted Silver and are not deleted.

### Output Dimensions

- `collision_year`
- `casualty_age_group`
- `casualty_severity`

### Output Measure

`casualty_count`

### Formula

`casualty_count = COUNT(*)`

### Gold Table

`gold_casualty_severity_summary`

### Validation

- Grain uniqueness
- Key completeness
- Negative measure check
- Eligible-row reconciliation
- Scope reconciliation
- Delta table validation
- Controlled rerun comparison

---

## 6. Validation Checks

Before downstream analytical consumption, verify:

### Gold Grain

- Gold grain keys are unique.
- No duplicate Gold grain combinations exist.

### Key Completeness

- Gold dimension/key fields contain no unexpected null values.

### Measure Validity

- Count-based measures are not negative.
- Severe collision counts do not exceed total collision counts.
- Severe collision rates remain between 0 and 100.

### Scope Reconciliation

For each Gold KPI:

`Eligible rows + Outside-scope rows = Trusted input rows`

### Measure Reconciliation

For each Gold table:

`Gold measure total = Eligible Trusted Silver population`

### Delta Validation

Each Gold table is stored as a Delta table.

### Controlled Rerun

The same Trusted Silver input must reproduce the same business rows.

The audit field `gold_created_at` is excluded from the business-row comparison because its timestamp may change between executions.

The rerun is checked in both directions:

- Run 1 minus Run 2
- Run 2 minus Run 1

Both difference counts must be zero.

---

## 7. Data-Boundary Rules

Gold tables read only from approved Trusted Silver tables:

- `trusted_silver_collisions`
- `trusted_silver_vehicles`
- `trusted_silver_casualties`

Candidate tables and Quarantine data are not used as Gold inputs.

No undocumented filters are applied.

No `DISTINCT` operation is used to hide duplicate amplification.

No `INNER JOIN` is required for the three current Gold tables because each KPI is calculated directly from its corresponding Trusted Silver table.

Rows outside KPI scope remain in Trusted Silver and are explicitly counted during scope reconciliation.

---

## 8. Week 7 Scope

Week 7 covers:

- KPI definition
- Gold-table design
- Gold-table construction
- Gold validation
- Scope and measure reconciliation
- Controlled rerun validation
- Documentation and execution evidence

Power BI implementation, dashboard export, and streaming are outside the Week 7 implementation boundary.
