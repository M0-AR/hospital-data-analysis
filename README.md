# Hospital Data Analysis: Clinical ETL & Normalization Pipeline

## 🚀 Overview
The **Hospital Data Analysis** repository provides a specialized ETL (Extract, Transform, Load) pipeline designed to process complex, nested Electronic Health Record (EHR) data. In modern healthcare environments, data is often exported in dense, non-relational formats where a single patient record contains multiple chronological events (e.g., lab tests, medications) stored as stringified lists.

This project bridges the gap between raw data exports and AI-ready datasets by de-identifying sensitive information and normalizing multi-valued clinical domains into a clean, relational structure.

---

## 🎯 Stakeholder Perspectives

### 💼 Business & Healthcare Leadership
*   **Data Interoperability**: Converts legacy system exports into standardized formats compatible with modern analytics tools.
*   **Compliance & Security**: Automated de-identification (e.g., CPR/Social Security stripping) ensures research is conducted on safe, non-PII data.
*   **Operational Efficiency**: Reduces the time data scientists spend on "data munging," accelerating the path from raw data to clinical insights.

### 🛠 Technical Engineers & Data Architects
*   **Robust Parsing**: Utilizes `ast.literal_eval` for safe evaluation of stringified Python list structures within CSV cells.
*   **Automated Domain Sectioning**: Dynamic column grouping based on clinical keywords (`miba`, `pato`, `vital`, etc.).
*   **Relational Normalization**: Implements a sophisticated "Expansion" logic that explodes nested clinical events while maintaining cross-column correlation.

### 🧪 Data Scientists & Researchers
*   **Clean Longitudinal Data**: Easily track a patient's vitals, lab results, and pathology findings over time.
*   **Feature-Ready Schema**: 56 pre-defined columns across 5+ clinical domains, ready for feature engineering and predictive modeling (e.g., outcome prediction, disease progression).

---

## 🏗 Technical Architecture & Workflow

The pipeline follows a linear, predictable path to ensure data integrity:

1.  **De-identification**: The `drop_column_by_index` utility removes sensitive PII (like CPR numbers) at the earliest stage of the pipeline.
2.  **Section Identification**: `get_sections_by_keyword` scans the 56-column header space to group related clinical data points (e.g., grouping all `miba_` columns for microbiology).
3.  **Safe Evaluation**: Nested string lists are evaluated into actual Python objects using the `safe_literal_eval` helper.
4.  **Data Expansion**: The `expand_section` function applies the Pandas `explode` method. This transforms rows with $N$ list elements into $N$ distinct relational rows, ensuring that correlated data (like a test result and its date) remain aligned.
5.  **Relational Output**: The final output is a flat, structured CSV (`expanded_data.csv`) optimized for SQL databases or machine learning frameworks.

---

## 📊 Data Dictionary & Clinical Domains

The repository handles **56 distinct data points**, categorized into primary clinical domains:

### 1. 🧬 Microbiology (`miba_`)
Covers the identification and analysis of infectious agents.
*   `miba_sample_type`: Source of the specimen (e.g., Urine, Swab).
*   `miba_collection_date`: Timestamp of specimen collection.
*   `miba_quantity`: Quantitative findings.
*   `miba_analysis` / `miba_resistance`: Detailed strain identification and antibiotic susceptibility profiles.
*   `miba_microscopy`: Visual findings from lab technicians.

### 2. 💊 Medication & Pharmacy (`medicine_`)
Longitudinal tracking of patient treatment.
*   `medicines_name`: Name and dosage of the prescribed drug.
*   `medicine_start_date` / `medicine_end_date`: The therapeutic window for each prescription.

### 3. 🔬 Pathology (`pato_`)
Detailed tissue and cellular analysis.
*   `pato_received_date`: Date the lab received the specimen.
*   `pato_diagnoses`: Professional diagnostic assessment.
*   `pato_conclusion`: Final summary of findings.
*   `pato_microscopy` / `pato_macroscopy`: Detailed physical and microscopic descriptions.

### 4. 🩺 Clinical Vitals (`vital_`)
Core physiological telemetry.
*   `vital_blood_pressure`: Systolic/Diastolic readings.
*   `vital_pulse`: Heart rate frequency.
*   `vital_temperature`: Body temperature and source (e.g., Temporal, Ear).
*   `vital_saturation`: SpO2 levels.
*   `vital_body_mass_index` / `vital_weight` / `vital_height`: Anthropometric data.

### 5. 💉 Laboratory Bloodwork (`blood_`)
Serial measurements of blood chemistry.
*   `blood_date_1` through `blood_date_8`: Chronological sequence of lab draws.
*   `blood_content_1` through `blood_content_13`: Diverse chemical markers (e.g., Hemoglobin, Potassium, Sodium, CRP, Troponin).

---

## ⚙️ Getting Started

### Prerequisites
*   Python 3.8+
*   Pandas

### Installation
```bash
pip install pandas
```

### Usage
1.  **Prepare your data**: Ensure your raw export is named `modified_data_without_cpr.csv`.
2.  **Run the analysis**:
    ```bash
    python3 data_analysis.py
    ```
3.  **Verify results**: Check `expanded_data.csv` for the normalized output.

---

## 🔮 Future Roadmap
*   **HL7/FHIR Integration**: Exporting normalized data directly into FHIR resources.
*   **Automated Anomaly Detection**: Identifying statistical outliers in vital signs or lab results during the ETL process.
*   **Trend Visualization**: Dashboard integration for visualizing patient recovery trajectories.

---
*Created with ❤️ for the Healthcare Data Community.*
