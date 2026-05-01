# 🚀 Operational Data Pipeline Optimization using Python, Pandas & SQL

## 📊 Project Overview

This project demonstrates an end-to-end data pipeline to clean, transform, and analyze messy operational supply chain data. The pipeline converts raw, inconsistent datasets into structured, analysis-ready data, enabling accurate business insights and decision-making.

---

## 🎯 Objective

* Build a data pipeline for cleaning raw operational data
* Handle missing values, incorrect formats, and anomalies
* Standardize date formats and numerical fields
* Generate new business metrics (delay days, delivery status)
* Prepare clean data for downstream analytics

---

## 🛠 Tools & Technologies

* Python (Pandas)
* SQL (SQLite)
* Google Colab
* Excel (for validation)

---

## 📂 Project Structure

data/
├── raw/
│ └── supply_chain_raw_orders.csv
│
└── processed/
└── supply_chain_raw_orders (1).csv

notebooks/
└── etl_pipeline.ipynb

scripts/
└── etl_pipeline.py

sql/
├── 01_data_quality_checks.sql
├── 02_clean_data_validation.sql
└── 03_kpi_analysis.sql

images/
└── pipeline_flow.png

README.md

---

## 🔄 ETL Pipeline Steps

### 1. Extract

* Load raw CSV dataset containing inconsistent and messy data

### 2. Transform

* Convert date formats to standard datetime
* Handle missing values
* Clean invalid numeric values (e.g., "abc", negative costs)
* Remove duplicate records
* Create new feature: `Delay_Days`
* Create new column: `Delivery_Performance` (On Time / Delayed)

### 3. Load

* Export cleaned dataset for analysis

---

## 📈 Key Metrics Generated

* Total Delay Days
* Average Delay per Supplier
* Delay by Region
* On-Time vs Delayed Orders

---

## 🔍 Key Insights

* Significant portion of orders experienced delivery delays
* Certain suppliers consistently showed higher delay times
* Regional performance differences highlighted operational inefficiencies
* Data inconsistencies (missing values, wrong formats) significantly impacted analysis accuracy

---

## 💼 Business Impact

This pipeline enables:

* Reliable operational reporting
* Improved supplier performance monitoring
* Better decision-making using clean data
* Reduced risk of incorrect analysis due to poor data quality

---

## 🚀 Future Improvements

* Automate pipeline using Airflow / scheduling tools
* Integrate with real-time data sources
* Build dashboard (Power BI / Tableau)
* Add data validation rules and alerts

---

## 📌 Conclusion

This project highlights the importance of data cleaning and pipeline optimization in real-world analytics. It demonstrates how structured data pipelines improve data quality, reliability, and business outcomes.
