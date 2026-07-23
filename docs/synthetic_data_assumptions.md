# Synthetic Data Assumptions

*Week:* 2  
*Purpose:* Document how synthetic data for the *RoadSafe Collision Risk Analytics* project is created and measured.

---

# 1. Synthetic Data Boundary

This project uses *synthetic road safety data* based on the official *2024 UK Department for Transport (DfT) STATS19 open dataset. The data is intended solely for educational and analytical purposes and **must not be presented as real company, customer, citizen, patient, government, or platform data*.


---

# 2. Domain Assumptions

| Area | Assumption |
|------|------------|
| *Geography / Scope* | UK public road network across various police forces and local authorities |
| *Time Period* | 1 January 2024 to 31 December 2024 |
| *Source Systems* | Police-reported collision systems, vehicle registration links, and casualty recording feeds |
| *Event Types* | Personal-injury collisions, vehicle involvements, and recorded casualties |
| *Reference Data* | Official DfT code lookups for police forces, collision severity, road types, junctions, and casualty classes |

---

# 3. Data Volume Assumptions

| File | Approximate Rows | Reason |
|------|-----------------:|--------|
| collisions.csv | 101,527 | Main event grain: one row per reported collision |
| vehicles.csv | 183,514 | Involved vehicle grain: multiple vehicles per collision |
| casualties.csv | 128,272 | Victim grain: multiple casualties per collision |
| lookups/*.csv | 1,775 | Combined rows for collision, vehicle, and casualty decoding |
| incident_alert_drop_*.json | 34 | Total simulation events across six structured drops |

---

# 4. Controlled Data Quality Issues

> *Note:* The percentages below are *target ranges*. Replace them with the exact measured percentages obtained from the Databricks starter notebook.

| Issue Type | Approx. Share | Why Include It |
|------------|--------------:|----------------|
| Duplicate IDs | 0.2%–0.5% | Tests uniqueness of collision_index and composite keys |
| Missing Values | 1%–3% | Tests completeness of coordinates and member identifiers |
| Invalid Reference Keys | 0.5%–1% | Tests orphan records (e.g., vehicles with no parent collision) |
| Negative / Impossible Values | 0.1%–0.5% | Tests range validation for driver age and speed limits |
| Timestamp Inconsistencies | 0.1%–0.3% | Tests date validity within the 2024 calendar year |

---

# 5. Manual Verification Checklist

Before using the generated data, verify that:

- Row counts match the source inventory precisely.
- Key fields exist and follow the expected string and integer formats.
- Dates are within *2024*, and geographic coordinates fall within valid UK boundaries.
- Controlled data quality defects exist (verified using SQL queries) but do not dominate the dataset.
- Source files maintain distinct grains (*Collision*, *Vehicle*, and *Casualty*) and are standardized before downstream processing.
