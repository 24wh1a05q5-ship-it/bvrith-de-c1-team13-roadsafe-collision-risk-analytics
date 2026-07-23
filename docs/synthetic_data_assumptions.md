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

## 3. Data Volume Assumptions

| File | Approximate Rows | Reason |
|---|---:|---|
| `[source_file_1].csv` | [rows] | [reason] |
| `[source_file_2].csv` | [rows] | [reason] |
| `[reference_file].csv` | [rows] | [reason] |
| `[streaming_events].json` | [rows] | [reason] |

---

## 4. Controlled Data Quality Issues

| Issue Type | Approx. Share | Why Include It |
|---|---:|---|
| Duplicate IDs | 0.2%–0.5% | Tests uniqueness |
| Missing values | 1%–3% | Tests completeness |
| Invalid reference keys | 0.5%–1% | Tests referential integrity |
| Negative / impossible values | 0.1%–0.5% | Tests range rules |
| Timestamp inconsistencies | 0.1%–0.3% | Tests chronology |

---

## 5. Manual Verification

Before using generated data, the team must check:

- Row counts are reasonable.
- Key fields exist.
- Dates and numeric values look realistic.
- Controlled defects exist but do not dominate the dataset.
- Source files are different enough to require real standardization.
