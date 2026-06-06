# SensorGuard ML

End-to-end machine learning project for predictive maintenance based on sensor-like machine data.

## Goal

The goal of this project is to predict machine failure based on operational parameters such as temperature, rotational speed, torque and tool wear.

The project follows a realistic data and machine learning workflow:

```text
CSV dataset -> SQLite database -> SQL queries -> Pandas EDA -> ML model -> FastAPI -> Docker
```

## Current status

| Module | Status | Description |
|---|---|---|
| Module 0 — Project setup | Done | Project structure, virtual environment, requirements.txt and GitHub repository |
| Module 1 — Dataset + SQL layer | Done | Dataset inspection, SQLite database, SQL table, CSV loading and analysis queries |
| Module 2 — Pandas + EDA | Done | Load data from SQL into Pandas, perform EDA and feature engineering |
| Module 3 — ML baseline | Planned | Train and evaluate baseline machine learning models |
| Module 4 — Prediction function | Planned | Save/load model and create local prediction function |
| Module 5 — FastAPI | Planned | Expose prediction through REST API |
| Module 6 — Docker + README | Planned | Containerize project and finalize documentation |

## Project structure

```text
SensorGuard_ML/
├── api/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── models/
├── notebooks/
│   └── 01_eda_and_modeling.ipynb
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
├── src/
│   ├── check_query.py
│   ├── database.py
│   ├── eda.py
│   ├── inspect_data.py
│   └── preprocessing.py
├── requirements.txt
└── README.md
```

## Completed work

### Module 0 — Project setup

- Created project repository
- Created virtual environment
- Prepared project folder structure
- Created `requirements.txt`
- Created initial README

### Module 1 — Dataset + SQL layer

- Inspected the AI4I dataset using Pandas
- Checked columns, data types, missing values and target distribution
- Created SQLite database
- Created SQL table `machine_measurements`
- Renamed raw CSV columns to SQL-friendly `snake_case` names
- Loaded 10,000 rows into SQLite
- Wrote SQL analysis queries using `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `COUNT`, `AVG`, `SUM` and `DISTINCT`

### Module 2 — Pandas + EDA

- Loaded data from SQLite into a Pandas DataFrame
- Created reusable preprocessing functions:
  - `load_data_from_sql()`
  - `add_features(df)`
- Added engineered features:
  - `temperature_difference`
  - `power_proxy`
- Performed basic exploratory data analysis
- Checked dataset shape, data types and descriptive statistics
- Checked missing values and duplicated rows
- Analyzed target distribution and class imbalance
- Compared average feature values for failure and non-failure cases
- Added basic plots for target distribution and selected numerical features
- Created `notebooks/01_eda_and_modeling.ipynb`

## Tech stack

Python, SQLite, SQL, Pandas, NumPy, scikit-learn, FastAPI, Docker

## How to run

Activate virtual environment:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create SQLite database and load data:

```powershell
python src/database.py
```

Expected output:

```text
Loaded rows: 10000
```

Run basic EDA script:

```powershell
python src/eda.py

## Interview explanation

In this project, I stored the data in SQLite to practice working with a relational database. I loaded the raw CSV dataset, created a SQL table, inserted the data into the database and wrote SQL queries for basic analysis. Later, the data will be loaded from SQL into Pandas for EDA, preprocessing and machine learning.

Polish version:

> W projekcie dane przechowywałem w SQLite, żeby przećwiczyć pracę z relacyjną bazą danych. Do modelowania pobierałem dane za pomocą zapytań SQL, a następnie przetwarzałem je w Pandas.