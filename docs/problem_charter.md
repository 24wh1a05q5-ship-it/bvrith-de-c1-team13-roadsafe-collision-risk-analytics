# Problem Charter

**Week:** 1  
**Owner(s):** Raikode Avishka, Harshika K., Akkepally Aishwarya  
**Team:** Team 13  
**Project:** RoadSafe: Collision Risk Analytics

---

## 1. Problem Context

### Problem Statement

RoadSafe is a road safety analytics project that transforms UK Department for Transport (DfT) STATS19 collision data into reliable and meaningful safety insights. The source data contains collision, vehicle, and casualty information that may include missing values, invalid codes, duplicate records, and inconsistent relationships between datasets.

The project addresses these challenges by developing a structured data engineering pipeline using Databricks and the Medallion Architecture. The processed data is used to generate trusted safety metrics and Power BI dashboards that help road safety stakeholders understand collision patterns, identify high-risk areas, and support data-driven safety decisions.

### Key Points

- Uses UK Department for Transport (DfT) STATS19 road safety data.
- Processes collision, vehicle, and casualty datasets.
- Handles data quality issues such as missing values and invalid codes.
- Validates relationships between related datasets.
- Uses a Bronze → Silver → Gold data architecture.
- Produces trusted metrics for road safety analysis.
- Provides Power BI dashboards for decision-making.
- Supports analysis of collision trends by time, location, road conditions, and other available attributes.

---

## 2. Engineering Problem

### Engineering Problem Statement

The RoadSafe project needs to transform raw and fragmented road safety datasets into a reliable analytical data platform. Collision, vehicle, and casualty records must be ingested, cleaned, validated, related correctly, and transformed into trusted datasets without losing the original source information.

The solution uses Databricks, Spark SQL, and PySpark to implement a Medallion Architecture consisting of Bronze, Silver, and Gold layers. Data quality rules are applied during processing to identify invalid records and maintain traceability. The resulting Gold-layer datasets are used by Power BI for road safety analysis.

### Engineering Requirements

- Ingest the required STATS19 collision, vehicle, and casualty datasets.
- Preserve raw source data in the Bronze layer.
- Clean and standardize data in the Silver layer.
- Validate relationships between collision, vehicle, and casualty records.
- Identify missing, invalid, duplicate, or inconsistent records.
- Quarantine records that fail defined data quality rules.
- Generate trusted analytical datasets in the Gold layer.
- Create meaningful road safety KPIs from Gold-layer data.
- Connect Power BI only to validated Gold-layer datasets.
- Maintain GitHub documentation and evidence throughout development.

---

## 3. Users / Stakeholders

RoadSafe is intended to support stakeholders involved in road safety monitoring, analysis, and reporting.

| User / Stakeholder | Requirement / Use of Data |
|---|---|
| **Road Safety Program Lead** | Identify high-risk road types and locations and prioritize safety improvements. |
| **Traffic Operations Analyst** | Analyze collision trends based on time, road conditions, weather, and location. |
| **Public Safety Communications Lead** | Access reliable incident information for safety communication and reporting. |
| **Data Quality Owner** | Monitor data quality and ensure that analytical results are based on valid records. |

---

## 4. Scope Inclusions

The project covers the development of an end-to-end road safety data engineering pipeline and analytics solution.

### Included in the Project

- **Data Ingestion:** Ingest the available UK DfT STATS19 collision, vehicle, and casualty datasets into the project environment.
- **Bronze Layer:** Store source data with minimal transformation while maintaining source-level traceability.
- **Silver Layer:** Clean, standardize, and integrate related datasets.
- **Data Quality:** Apply validation rules to identify missing, invalid, duplicate, and inconsistent records.
- **Quarantine:** Separate records that fail data quality checks so that they are not included in trusted analytical outputs.
- **Gold Layer:** Create business-ready tables containing road safety metrics and aggregated information.
- **Power BI:** Develop dashboards using Gold-layer tables for safety analysis and visualization.
- **Streaming Simulation:** Process simulated incident information to demonstrate near-real-time data processing.
- **Documentation:** Maintain weekly logs, notebooks, data dictionaries, project documentation, and supporting evidence in GitHub.

---

## 5. Scope Exclusions

The following items are outside the scope of the RoadSafe project:

- **Traffic Prediction:** The project does not build a traffic-flow or future traffic prediction system.
- **Navigation:** The project does not provide route planning or navigation functionality.
- **Law Enforcement System:** The project does not implement an enforcement or policing system.
- **Personal Data:** No private or personally identifiable information is intentionally processed.
- **Raw/Bronze/Silver Visualization:** Power BI dashboards are not connected directly to raw, Bronze, or Silver datasets.
- **Kafka Deployment:** Kafka is not installed or deployed as part of the implementation.
- **Complete Dataset in GitHub:** Large source datasets are not committed to the GitHub repository.
- **Unexplained Code:** Team members must understand and be able to explain the notebooks, SQL queries, transformations, and dashboard logic used in the project.
- **End-of-Project Documentation Only:** Documentation is maintained progressively through weekly submissions rather than being created only at the end.

---

## 6. Success Criteria

The RoadSafe project will be considered successful when the team delivers a working and documented data engineering pipeline that converts source road safety data into trusted analytical outputs.

### Success Measures

- **Working Data Pipeline:** Data successfully moves through the Bronze, Silver, and Gold layers.
- **Data Quality:** Defined validation rules identify invalid or inconsistent records.
- **Traceability:** Source data can be traced through the processing layers to the final analytical outputs.
- **Trusted Gold Data:** Gold tables contain validated and business-ready metrics.
- **Power BI Dashboard:** The dashboard provides useful visualizations for road safety analysis using Gold-layer data.
- **Streaming Demonstration:** Simulated incident data can be processed through the planned streaming workflow.
- **Documentation:** GitHub contains the required project documentation, notebooks, weekly logs, and supporting evidence.
- **Team Understanding:** All team members can explain the project's architecture, data flow, transformations, and dashboard outputs.

---

## 7. Initial Assumptions

The following assumptions were established during project framing:

- The required STATS19 datasets are available from the UK Department for Transport.
- Databricks Free Edition is sufficient for the academic implementation.
- The project will use Spark SQL and PySpark for data processing.
- Power BI will consume validated Gold-layer outputs.
- Simulated incident data will be used where real-time incident data is not available.
- Large source datasets will remain outside the GitHub repository.

---

## 8. Project Constraints

- The project must be completed within the defined academic project timeline.
- The implementation should use the tools and architecture specified in the project requirements.
- Large datasets should not be unnecessarily committed to GitHub.
- The solution should remain understandable and explainable by all team members.
- Weekly progress and implementation evidence must be maintained throughout the project.

---

## 9. Week 01 Outcome

During Week 01, the team established the foundation of the RoadSafe project by defining the engineering problem, identifying stakeholders, establishing project boundaries, and selecting the Medallion Architecture as the overall data processing approach.

The team also established the principle that analytical dashboards should use trusted Gold-layer data rather than raw datasets. These decisions provide the foundation for subsequent data exploration, ingestion, transformation, data quality validation, and dashboard development.
