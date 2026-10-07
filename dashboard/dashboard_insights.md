# Dashboard Insights

## Week 9 Insight 1 — Monthly Collision Volume

### Question / Decision
How does collision volume vary by month?

### Observation
The Collision Trends dashboard shows monthly variation in collision volume. Under the January filter, the dashboard reports **8,153 collisions**.

### Filter / Time Scope
- Month: January
- Filter state: January selected in the Month slicer

### Visual / Page
- Page: Collision Trends
- Visual: Total Collisions KPI and Monthly Collision Trend

### Owning Gold Table
`gold_monthly_collision_trends`

### Measure / Field
- Measure: `collision_count`
- Aggregation: SUM

### Evidence / Validation
The January Power BI value was reconciled against the owning Gold table.

- Power BI Total Collisions: **8,153**
- Gold validation query Total Collisions: **8,153**
- Reconciliation result: **PASS**

### Interpretation
January contains 8,153 eligible collision records within the dashboard's approved Gold-layer scope.

### Limitation
This observation describes collision volume only. It does not establish why the number of collisions is higher or lower in any month. No causal explanation is inferred from the dashboard.

---

## Insight Validation Notes

All Week 9 insights are based on approved Gold-layer tables used by the Power BI dashboard. Final values are interpreted only within the applicable filter and scope.

Where a cause or explanation is not directly supported by the Gold data, it is treated as a hypothesis rather than a confirmed conclusion.
