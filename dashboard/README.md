# Power BI Dashboard

## 1. Purpose

This dashboard provides a Power BI reporting layer over the approved Week 7 Gold tables.

The dashboard is designed to provide clear views of:

- Monthly collision trends
- Vehicle type involvement
- Casualty severity
- Vehicle propulsion codes

Power BI uses only the approved Gold hand-off tables and does not directly read from Bronze, Candidate Silver, Quarantine, or raw source data.

---

## 2. Gold Source Register

The dashboard uses the following four Gold tables.

| Gold Table | Grain | Main KPI / Purpose | Power BI Page |
|---|---|---|---|
| `gold_monthly_collision_trends` | collision_year + collision_month + urban_rural_group | Collision counts and severe collision rates over time | Collision Trends |
| `gold_vehicle_type_readable` | collision_year + vehicle_type | Vehicle involvement counts by vehicle type | Vehicle Type Analysis |
| `gold_casualty_severity_readable` | collision_year + casualty_age_group + casualty_severity | Casualty counts by severity and age group | Casualty Severity Analysis |
| `gold_vehicle_propulsion_readable` | collision_year + propulsion_code | Vehicle counts by propulsion code | Vehicle Propulsion Analysis |

---

## 3. Power BI Table Map

### gold_monthly_collision_trends

Main fields used:

- `collision_year`
- `collision_month`
- `month_name`
- `month_sort`
- `period_label`
- `urban_rural_group`
- `collision_count`
- `severe_collision_count`
- `severe_collision_rate`

### gold_vehicle_type_readable

Main fields used:

- `collision_year`
- `vehicle_type`
- `vehicle_type_name`
- `vehicle_involvement_count`

### gold_casualty_severity_readable

Main fields used:

- `collision_year`
- `casualty_age_group`
- `casualty_severity`
- `casualty_severity_name`
- `casualty_count`

### gold_vehicle_propulsion_readable

Main fields used:

- `collision_year`
- `propulsion_code`
- `propulsion_type_name`
- `vehicle_count`

---

## 4. Relationships and Model

The four Gold tables represent separate reporting grains.

They are therefore kept as separate Power BI tables rather than being directly joined simply because some fields have similar names.

No unsupported many-to-many relationship was introduced between the independent Gold summary tables.

The dashboard visuals use the measures from their respective owning Gold tables.

---

## 5. Measures

### Overall Severe Collision Rate

```DAX
Overall Severe Collision Rate =
DIVIDE(
    SUM(gold_monthly_collision_trends[severe_collision_count]),
    SUM(gold_monthly_collision_trends[collision_count])
)

Monthly Severe Collision Rate
Monthly Severe Collision Rate =
DIVIDE(
    SUM(gold_monthly_collision_trends[severe_collision_count]),
    SUM(gold_monthly_collision_trends[collision_count])
)

This measure is formatted as a percentage with two decimal places.

Distinct Vehicle Types
Distinct Vehicle Types =
DISTINCTCOUNT(gold_vehicle_type_readable[vehicle_type_name])
Distinct Severity Categories
Distinct Severity Categories =
DISTINCTCOUNT(gold_casualty_severity_readable[casualty_severity_name])
Distinct Propulsion Codes
Distinct Propulsion Codes =
DISTINCTCOUNT(
    gold_vehicle_propulsion_readable[propulsion_type_name]
)
6. Dashboard Pages
Page 1 — Collision Trends

Visuals include:

Total Collisions KPI
Severe Collisions KPI
Overall Severe Collision Rate KPI
Monthly Collision Trend
Collisions by Urban/Rural Area
Monthly Severe Collision Rate
Severe Collisions by Month
Month slicer

The period_label field is sorted using month_sort.

Page 2 — Vehicle Type Analysis

Visuals include:

Total Vehicle Involvements KPI
Vehicle Types KPI
Vehicle Involvement by Type
Vehicle Type Distribution
Top Vehicle Types by Involvement
Vehicle Type slicer
Page 3 — Casualty Severity Analysis

Visuals include:

Total Casualties KPI
Severity Categories KPI
Casualties by Severity
Casualty Severity Distribution
Casualties by Age Group and Severity
Age Group slicer
Page 4 — Vehicle Propulsion Analysis

Visuals include:

Total Vehicles KPI
Propulsion Codes KPI
Vehicle Count by Propulsion Code
Vehicle Propulsion Distribution
Propulsion Type slicer
7. Data Refresh and Source

The dashboard is based on controlled Gold exports produced from the approved Gold tables.

The Power BI hand-off files are stored in:

data_sample/gold_exports/

The four exported tables are:

gold_monthly_collision_trends.csv
gold_vehicle_type_readable.csv
gold_casualty_severity_readable.csv
gold_vehicle_propulsion_readable.csv

The exported values were not manually modified after generation.

8. Validation and Reconciliation

The dashboard was checked against the owning Gold tables.

For gold_monthly_collision_trends, the following Gold totals were reconciled with Power BI:

Measure	Gold Value	Power BI
Total Collisions	98,947	98,947
Severe Collisions	24,477	24,477
Overall Severe Collision Rate	24.74%	24.74%

The remaining dashboard pages were also checked against their respective owning Gold tables and produced the expected results.

The reconciliation was performed without manually entering expected values into Power BI.

9. Known Limitations
The dashboard is a first working Week 8 dashboard.
The dashboard focuses on functional reporting and validation.
Propulsion values are presented using propulsion codes because a project-approved propulsion mapping was not available in the Week 7 source material.
Casualty severity code 8 is retained as an explicitly unmapped category rather than assigning an unsupported meaning.
Further visual refinement, interaction improvements, and explanatory insight development are reserved for Week 9.
10. Week 9 Handoff

The Week 8 dashboard provides the validated functional foundation for Week 9.

Future refinement may include:

Visual hierarchy improvements
Additional interactions
Dashboard usability refinement
Explanatory context
Insight-oriented presentation

The existing PBIX should be continued rather than rebuilt from scratch.
