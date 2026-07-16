# RoadSafe: Collision Risk Analytics

> **Student note:** Start with `00_START_HERE.md` and `00_TEMPLATE_INDEX.md`. The placeholder files inside this repo are the templates.


**Program:** ZENAIZ x BVRIT Hyderabad Data Engineering Internship Program  
**Track:** Data Engineering  
**Duration:** 12 Weeks  
**Team:** 13
**Students:** Raikode Avishka, Harshika.K, A.Aishwarya  
**AI Teammate:** Used responsibly for explanation, debugging, review, and documentation support.

---

## 1. Project Summary

RoadSafe is a data engineering project that transforms approximately **120,000** raw UK Department for Transport (STATS19) collision, vehicle, and casualty records into a trusted lakehouse pipeline and a decision-ready safety intelligence dashboard.

Using **Databricks**, **Spark SQL**, and **PySpark**, the project implements a **Medallion Architecture**—moving data from **Bronze (raw)** to **Silver (cleaned and joined)** and finally to **Gold (KPI-driven)** layers—while applying rigorous **Data Quality (DQ)** rules to quarantine rather than delete defective records.

This architecture ensures that the final three-view **Power BI** dashboard (**Safety Overview**, **Risk Hotspots**, and **Live Incident Feed**) provides traceable and reliable insights for stakeholders such as road safety leads and traffic analysts.

Additionally, the pipeline incorporates a simulated streaming layer using **Structured Streaming** to process live JSON incident alerts, demonstrating the system's ability to maintain accurate metrics even when faced with late or malformed data.

- **Domain:** Transportation safety using official UK Department for Transport (STATS19) road collision data with an ethical, public-impact focus.
- **Core engineering problem:** Transform fragmented raw datasets (collisions, vehicles, and casualties) into a unified, reliable lakehouse pipeline while resolving data quality issues such as invalid severity codes and missing referential links.
- **Main pipeline:** Bronze (raw with metadata) → Silver (cleaned and joined) → Data Quality (quarantine rules) → Gold (business KPIs) → Power BI (connected only to Gold tables) → Week 10 Streaming Simulation (JSON alerts via Structured Streaming).
- **Final outcome:** A complete end-to-end data engineering pipeline, a three-view Power BI dashboard (Safety Overview, Risk Hotspots, and Live Incident Feed), a live incident streaming demonstration, and a well-documented GitHub repository containing the complete project implementation.

## 2. Tools Used

| Tool | Purpose |
|------|---------|
| **Databricks (Free Edition)** | Serves as the primary development platform for processing the ~120,000 collision records and building the core data pipeline. |
| **Spark SQL** | The primary language used for the "Spark SQL first" development approach to build the medallion architecture. |
| **PySpark** | Utilized for light development alongside Spark SQL within the Databricks environment. |
| **Power BI Desktop** | Used to create a three-view dashboard (Safety Overview, Risk Hotspots, and Live Incident Feed) that connects exclusively to Gold tables to visualize verified data. |
| **GitHub** | Acts as the central repository for code, Databricks notebooks, and documenting mandatory weekly evidence to prove every step of the build. |
| **Auto Loader & Structured Streaming** | Spark technologies implemented in Week 10 to handle the landing of JSON event files and transform them into live metrics. |
| **File Formats (CSV & JSON)** | The project uses **CSV** for the main batch data (collisions, vehicles, and casualties) and **JSON** for simulated live incident alert events. |
| **Kafka (Design-Awareness)** | While not actually installed, Kafka concepts like topics, keys, and partitions are documented to demonstrate design awareness for the streaming layer. |
## 3. Repository Navigation

| Folder / File | Purpose |
|---|---|
| `docs/` | Project documentation, data dictionary, DQ summary, Gold metric definitions |
| `src/` | Data generation and reusable quality helper scripts |
| `notebooks/` | Databricks notebooks for exploration, Bronze, Silver, DQ, Gold, export, streaming |
| `data_sample/` | Small sample raw/streaming data only; do not store large files |
| `dashboard/` | Power BI `.pbix` file and dashboard notes |
| `streaming/` | Streaming design, JSON event schema, Kafka-style design awareness |
| `screenshots/` | Weekly evidence screenshots |
| `weekly_logs/` | Weekly execution logs and AI transparency notes |
| `final_submission/` | Final report, demo script, team contribution, checklist |

---

## 4. 12-Week Execution Map

| Week | Focus | Main Evidence |
|---:|---|---|
| 1 | Project framing + GitHub | README, problem charter, Week 1 log |
| 2 | Dataset design | Data dictionary, assumptions, sample data plan |
| 3 | Databricks exploration | Exploration notebook, schema/count screenshots |
| 4 | Bronze ingestion | Bronze notebook, raw-to-Bronze reconciliation |
| 5 | Silver standardization | Silver notebook, canonical mapping evidence |
| 6 | Data quality | DQ rules, DQ notebook, DQ summary |
| 7 | Gold metrics | Gold tables and metric definitions |
| 8 | Power BI draft | Gold export and first dashboard draft |
| 9 | Dashboard refinement | Final dashboard screenshots and insights |
| 10 | Streaming simulation | Auto Loader / Structured Streaming notebook and live metric |
| 11 | Integration | Pipeline walkthrough, cleaned README, final evidence |
| 12 | Final demo | Final report, demo script, contribution note |

---

## 5. Important Rules

- Do not connect Power BI directly to raw CSV files. Power BI must use Gold outputs.
- Do not submit copied internet GitHub repositories as your own project.
- External references must be listed in `docs/references.md`.
- AI-generated code or content must be verified and explainable.
- Every week must have a GitHub commit and weekly log.
- Keep sample data small in GitHub. Large generated data should be recreated using scripts or uploaded to Databricks separately.

---

## 6. Final Project Proof

By Week 12, this repository should prove:

- We designed source datasets.
- We processed batch data in Databricks.
- We created Bronze tables.
- We standardized Silver tables.
- We implemented data quality checks.
- We created Gold metric tables.
- We built Power BI dashboards from Gold outputs.
- We simulated streaming JSON events.
- We documented weekly evidence in GitHub.
- We can explain and defend the full project.
