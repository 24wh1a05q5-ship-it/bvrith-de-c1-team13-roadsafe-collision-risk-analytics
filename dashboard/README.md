# Power BI Dashboard

## 1. Purpose

This dashboard provides a Power BI reporting layer over the approved Week 7 Gold tables.

The dashboard provides clear views of:

- Monthly collision trends
- Vehicle type involvement
- Casualty severity
- Vehicle propulsion codes

Power BI uses only the approved Gold hand-off tables and does not directly read from Bronze, Candidate Silver, Quarantine, or raw source data.

Week 9 refined and validated the existing Week 8 Power BI solution rather than rebuilding it from scratch.

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

The dashboard visuals use measures from their respective owning Gold tables.

The independent Gold tables remain independent where no safe shared relationship is required.

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

Formatted as a percentage with two decimal places.

Distinct Vehicle Types
Distinct Vehicle Types =
DISTINCTCOUNT(
    gold_vehicle_type_readable[vehicle_type_name]
)
Distinct Severity Categories
Distinct Severity Categories =
DISTINCTCOUNT(
    gold_casualty_severity_readable[casualty_severity_name]
)
Distinct Propulsion Codes
Distinct Propulsion Codes =
DISTINCTCOUNT(
    gold_vehicle_propulsion_readable[propulsion_type_name]
)

These measures retain the same business meaning established during Week 8.

6. Dashboard Pages
Page 1 — Collision Trends

Business question:

How does collision volume and severe collision activity vary over time and across urban/rural areas?

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

The Month slicer was tested during Week 9 and is functioning as intended.

Page 2 — Vehicle Type Analysis

Business question:

How are vehicle involvements distributed across vehicle types?

Visuals include:

Total Vehicle Involvements KPI
Vehicle Types KPI
Vehicle Involvement by Type
Vehicle Type Distribution
Top Vehicle Types by Involvement
Vehicle Type slicer

The Vehicle Type slicer was tested during Week 9 and is functioning as intended.

Page 3 — Casualty Severity Analysis

Business question:

How are casualties distributed by severity and age group?

Visuals include:

Total Casualties KPI
Severity Categories KPI
Casualties by Severity
Casualty Severity Distribution
Casualties by Age Group and Severity
Age Group slicer

The Age Group slicer was tested during Week 9 and is functioning as intended.

Page 4 — Vehicle Propulsion Analysis

Business question:

How are vehicle records distributed across the available propulsion codes?

Visuals include:

Total Vehicles KPI
Propulsion Codes KPI
Vehicle Count by Propulsion Code
Vehicle Propulsion Distribution
Propulsion Type slicer

The Propulsion Type slicer was tested during Week 9 and is functioning as intended.

7. Interaction and Filter Behavior

The dashboard contains slicers that operate within their relevant Gold-table reporting scope.

Validated slicers:

Page	Slicer	Status
Collision Trends	Month	Working
Vehicle Type Analysis	Vehicle Type	Working
Casualty Severity Analysis	Age Group	Working
Vehicle Propulsion Analysis	Propulsion Type	Working

The dashboard was interaction-tested during Week 9.

Independent Gold tables were not connected with unsupported relationships merely to force common filtering behavior.

8. Data Refresh and Source

The dashboard is based on controlled Gold exports produced from the approved Gold tables.

The Power BI hand-off files are stored in:

data_sample/gold_exports/

The four exported tables are:

gold_monthly_collision_trends.csv
gold_vehicle_type_readable.csv
gold_casualty_severity_readable.csv
gold_vehicle_propulsion_readable.csv

The exported values were not manually modified after generation.

9. Validation and Reconciliation

The dashboard was checked against the owning Gold tables.

Overall reconciliation
Measure	Gold Value	Power BI
Total Collisions	98,947	98,947
Severe Collisions	24,477	24,477
Overall Severe Collision Rate	24.74%	24.74%
Filtered reconciliation

A Week 9 filtered reconciliation was performed on the Collision Trends page.

Filter:

Month = January

Result:

Measure	Gold Value	Power BI	Result
Total Collisions	8,153	8,153	PASS

The filtered value was validated using the owning Gold table:

gold_monthly_collision_trends

The reconciliation used the same January filter scope in Power BI and the Gold validation query.

10. Insights

Week 9 insight documentation is maintained separately in:

docs/dashboard_insights.md

The documented insight is based on the final dashboard and a reconciled Gold-layer value.

Insights are written as observations supported by the available Gold data. Causal explanations are not inferred unless directly supported by the approved data.

11. Known Limitations
The dashboard uses approved Gold summary tables and therefore reflects their defined grains and scopes.
Independent Gold summary tables remain separate where a safe shared relationship is not required.
Propulsion values are presented using propulsion codes because a project-approved propulsion mapping was not available in the Week 7 source material.
Casualty severity code 8 is retained as an explicitly unmapped category rather than assigning an unsupported meaning.
Dashboard observations describe patterns in the available data and do not establish causal explanations without supporting evidence.
Filter behavior is limited to the reporting scope of the relevant Gold table where no approved shared dimension exists.

12. Week 9 Evidence

Week 9 evidence is stored under:

screenshots/

Relevant evidence includes:

week09_01_final_model.png
week09_02_refined_page_01.png
week09_04_filter_interaction.png
week09_05_filtered_reconciliation.png
week09_06_insights_evidence.png

13. Week 9 Completion

Week 9 refined the existing Week 8 Power BI solution without rebuilding the dashboard.

Completed activities include:

Reviewed existing dashboard pages
Confirmed visual hierarchy and readability
Tested dashboard slicers
Verified intended filter behavior
Preserved independent Gold-table boundaries
Reconciled final dashboard values against Gold
Completed a filtered January reconciliation
Added evidence-backed dashboard insight documentation
Added Week 9 evidence screenshots
14. Week 10 Boundary

Week 9 remains a batch Gold / Power BI dashboard refinement sprint.

Streaming implementation is not part of this dashboard work.

Week 10 will begin the streaming branch only after the required streaming Gold design and approvals are available.

The existing validated Power BI dashboard should remain the Week 9 reporting baseline.
