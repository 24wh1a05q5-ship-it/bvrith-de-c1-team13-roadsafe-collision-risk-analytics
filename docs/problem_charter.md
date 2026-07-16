# Problem Charter

**Week:** 1  
**Owner(s):** Raikode Avishka,Harshika.k,Akkepally Aishwarya.  
**Project:** RoadSafe: Collision Risk Analytics

---

## 1. Problem Context

### Simple Paragraph

The **RoadSafe** project simulates a public road safety analytics system that transforms raw UK Department for Transport (STATS19) collision, vehicle, and casualty data into reliable insights. Since the raw data may contain missing links, invalid values, and inconsistencies, the project applies data quality checks and processes the data through a trusted pipeline. The final Power BI dashboard helps road safety teams, traffic analysts, and decision-makers monitor accident trends, identify high-risk locations, and support informed safety decisions.

### Key Points

- Simulates a public road safety analytics system.
- Uses approximately **120,000** UK Department for Transport (STATS19) records.
- Processes collision, vehicle, casualty, and simulated live incident data.
- Cleans and validates raw data to improve quality and reliability.
- Resolves issues such as missing links, invalid values, and inconsistent records.
- Produces trusted metrics and dashboards for analysis.
- Helps road safety leads identify high-risk roads and accident patterns.
- Enables traffic analysts to study trends based on time, weather, and location.
- Provides a live incident view for monitoring recent events.
- Supports data quality teams in ensuring accurate and reliable reporting.

## 2. Engineering Problem

### Simple Paragraph

The **RoadSafe** project transforms approximately **120,000** fragmented UK road safety records—including collision, vehicle, and casualty data—into a trusted lakehouse pipeline using **Databricks**, **Spark SQL**, **PySpark**, and **Power BI**. The pipeline cleans and validates the data through the **Bronze**, **Silver**, and **Gold** layers while applying data quality rules to quarantine invalid records. It also processes simulated live JSON incident alerts using **Structured Streaming** to deliver reliable real-time safety metrics.

### Key Points

- Transforms approximately **120,000** raw road safety records into a trusted lakehouse.
- Processes collision, vehicle, and casualty datasets.
- Implements a **Medallion Architecture** with Bronze, Silver, and Gold layers.
- Applies data quality rules to detect and quarantine invalid records.
- Resolves issues such as invalid severity codes and missing referential links.
- Integrates simulated live JSON incident alerts using **Structured Streaming**.
- Produces reliable batch and real-time safety metrics.
- Supports accurate reporting and data-driven decision-making through Power BI dashboards.
## 3. Users / Stakeholders

### Simple Paragraph

The **RoadSafe** project is designed for different stakeholders involved in road safety analysis and decision-making. Each user relies on trusted data and dashboards to monitor accident trends, identify high-risk locations, improve public safety, and ensure the accuracy of reported metrics.

### Stakeholders and Their Needs

| **User / Stakeholder** | **What They Need from the Data** |
|-------------------------|----------------------------------|
| **Road Safety Program Lead** | Identify high-risk road types and locations to prioritize safety improvements and interventions. |
| **Traffic Operations Analyst** | Monitor collision trends based on time, weather, and road conditions to support traffic planning. |
| **Public Safety Communications Lead** | View a reliable live incident feed for accurate public updates without relying on unverified alerts. |
| **Data Quality Owner** | Ensure consistent, accurate, and trustworthy data for reporting and decision-making. |

## 4. Scope Inclusions

### Simple Paragraph

The **RoadSafe** project includes building a complete end-to-end lakehouse pipeline and analytics dashboard for road safety data. The project covers data ingestion, cleaning, validation, transformation, KPI generation, dashboard visualization, streaming simulation, and complete project documentation to ensure reliable and traceable analytics.

### Key Inclusions

- **Raw Source Files:** Ingest approximately **120,000** UK Department for Transport (STATS19) records from collision, vehicle, and casualty CSV files, along with simulated JSON incident alerts.
- **Bronze Layer:** Store raw data with metadata while preserving the original records for auditing and traceability.
- **Silver Layer:** Clean, standardize, and join datasets into structured tables using collisions as the primary dataset.
- **Data Quality Checks:** Detect, validate, and quarantine invalid or inconsistent records instead of deleting them.
- **Gold Layer:** Generate trusted KPI tables, such as severity summaries and road type risk summaries, for reporting and analysis.
- **Power BI Dashboard:** Create three dashboard views—**Safety Overview**, **Risk Hotspots**, and **Live Incident Feed**—using only Gold tables.
- **Streaming Simulation:** Process live JSON incident alerts using **Auto Loader** and **Structured Streaming** to update real-time metrics.
- **GitHub Documentation:** Maintain Databricks notebooks, data dictionaries, weekly evidence, and project documentation throughout the 12-week development process.

## 5. Scope Exclusions

### Simple Paragraph

The **RoadSafe** project focuses only on building a trusted data engineering lakehouse pipeline and analytics dashboard. Features such as traffic prediction, navigation systems, personal data processing, direct visualization from raw data, Kafka deployment, and unexplained AI-generated code are intentionally excluded to keep the project aligned with its objectives and academic requirements.

### Key Exclusions

- **No Traffic Prediction or Navigation System:** The project does not build traffic prediction, navigation, or law enforcement applications.
- **No Personal or Private Data:** Only official UK Department for Transport (STATS19) open data is used; no personal or confidential data is included.
- **No Direct-to-Raw Visualization:** Power BI connects only to **Gold** tables and never directly to Raw, Bronze, or Silver data.
- **No Kafka Installation:** Kafka concepts are discussed for design awareness, but Kafka is not installed or configured.
- **No Full Dataset on GitHub:** The complete 120,000-record dataset remains in Databricks and is not committed to GitHub.
- **No Final-Week-Only Submission:** Weekly progress and evidence must be documented throughout the project instead of submitting everything at the end.
- **No Unexplained AI-Generated Work:** Every notebook, SQL query, and code implementation must be understandable and explainable by the project team.
## 6. Success Criteria

### Simple Paragraph

The **RoadSafe** project is considered successful if it delivers a complete, reliable, and well-documented data engineering solution within 12 weeks. The project should provide a trusted end-to-end lakehouse pipeline, high-quality analytics, a functional Power BI dashboard, a working streaming simulation, and comprehensive documentation that demonstrates the team's understanding of the entire system.

### Key Success Criteria

- **End-to-End Pipeline:** Successfully transforms raw data through the **Bronze**, **Silver**, **Data Quality**, and **Gold** layers.
- **Traceable Analytics:** All dashboard visuals are built exclusively from **Gold** tables, ensuring complete data traceability.
- **Data Quality Management:** Detects, validates, and quarantines invalid or inconsistent records instead of deleting them.
- **Power BI Dashboard:** Delivers three dashboard views—**Safety Overview**, **Risk Hotspots**, and **Live Incident Feed**—that support stakeholder decision-making.
- **Streaming Simulation:** Processes live JSON incident alerts using **Structured Streaming** while handling late, duplicate, and malformed records reliably.
- **Team Understanding:** Every team member can explain the complete pipeline, architecture, and implementation during the final presentation.
- **Project Documentation:** Maintains a complete GitHub repository containing Databricks notebooks, weekly progress evidence, and all final project deliverables.
