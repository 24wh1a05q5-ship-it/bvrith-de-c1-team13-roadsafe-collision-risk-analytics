# Power BI Dashboard — Week 8

## Purpose

This dashboard is the Week 8 Power BI hand-off built from approved Gold-layer tables. The dashboard uses Gold tables as the report-facing source and keeps the different Gold grains separate.

## Gold Source Register

| Gold Table | Grain | Dashboard Purpose |
|---|---|---|
| `gold_monthly_collision_trends` | collision_year + collision_month + urban_rural_group | Monthly collision trends, severe collisions, severe collision rate, and urban/rural comparison |
| `gold_vehicle_type_readable` | collision_year + vehicle_type | Vehicle involvement by readable vehicle type |
| `gold_casualty_severity_readable` | collision_year + casualty_age_group + casualty_severity | Casualty counts by severity and age group |
| `gold_vehicle_propulsion_readable` | collision_year + propulsion_code | Vehicle counts by propulsion code |

Only these four Gold tables are used by the dashboard pages. Other Gold tables created during the Gold work are retained for information/proof and are not unnecessarily loaded into the report model.

## Power BI Table Map

### `gold_monthly_collision_trends`

Report-facing fields:

- `collision_year`
- `collision_month`
- `month_name`
- `month_sort`
- `period_label`
- `urban_rural_group`
- `collision_count`
- `severe_collision_count`
- `severe_collision_rate`

### `gold_vehicle_type_readable`

Report-facing fields:

- `collision_year`
- `vehicle_type`
- `vehicle_type_name`
- `vehicle_involvement_count`

### `gold_casualty_severity_readable`

Report-facing fields:

- `collision_year`
- `casualty_age_group`
- `casualty_severity`
- `casualty_severity_name`
- `casualty_count`

### `gold_vehicle_propulsion_readable`

Report-facing fields:

- `collision_year`
- `propulsion_code`
- `propulsion_type_name`
- `vehicle_count`

## Relationships

The four Gold tables represent different reporting grains and are used independently.

No direct relationship is required between these fact/summary tables merely because they contain common fields such as year.

## Measures

### Overall Severe Collision Rate

```DAX
Overall Severe Collision Rate =
DIVIDE(
    SUM(gold_monthly_collision_trends[severe_collision_count]),
    SUM(gold_monthly_collision_trends[collision_count])
)

Monthly Severe Collision Rate =
DIVIDE(
    SUM(gold_monthly_collision_trends[severe_collision_count]),
    SUM(gold_monthly_collision_trends[collision_count])
)

Distinct Vehicle Types =
DISTINCTCOUNT(gold_vehicle_type_readable[vehicle_type_name])

Distinct Severity Categories =
DISTINCTCOUNT(gold_casualty_severity_readable[casualty_severity_name])

Distinct Propulsion Codes =
DISTINCTCOUNT(
    gold_vehicle_propulsion_readable[propulsion_type_name]
)

Page Register
Page 1 — Collision Trends
Total Collisions
Severe Collisions
Overall Severe Collision Rate
Monthly Collision Trend
Collisions by Urban/Rural Area
Monthly Severe Collision Rate
Severe Collisions by Month
Month slicer
Page 2 — Vehicle Type Analysis
Total Vehicle Involvements
Vehicle Types
Vehicle Involvement by Type
Vehicle Type Distribution
Top Vehicle Types by Involvement
Vehicle Type slicer
Page 3 — Casualty Severity Analysis
Total Casualties
Severity Categories
Casualties by Severity
Casualty Severity Distribution
Casualties by Age Group and Severity
Age Group slicer
Page 4 — Vehicle Propulsion Analysis
Total Vehicles
Propulsion Codes
Vehicle Count by Propulsion Code
Vehicle Propulsion Distribution
Propulsion Type slicer
Refresh / Hand-off

The Power BI report is intended to consume the controlled Gold hand-off produced by notebooks/06_powerbi_export.ipynb.

The export notebook documents the Gold source register, export contract, read-back checks, and reconciliation checkpoints.

Validation

Week 8 validation includes:

Gold source and grain identification.
Individual Gold-table validation before dashboard modeling.
Dashboard pages built from the approved Gold tables.
KPI and visual measures mapped to owning Gold tables.
period_label sorted using month_sort for the monthly trend.
Percentage measures formatted as percentages with two decimal places.
No Silver/raw table is used directly by the dashboard.
Different-grain Gold tables are not directly joined simply because they share a field.
Known Limitations
The propulsion field is represented using propulsion codes because the available Week 7 source material did not provide an approved project-specific propulsion-code mapping.
Casualty severity code 8 is retained as Code 8 - Not mapped rather than assigning an unsupported business meaning.
Week 9 insight storytelling and visual-polish work are outside this Week 8 hand-off.
Week 9 Hand-off

Continue from this same PBIX.

Week 9 can refine interactions, visual hierarchy, explanatory context, and insight presentation without rebuilding the underlying Gold model.

