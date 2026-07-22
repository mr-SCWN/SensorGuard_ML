# SensorGuard ML

End-to-end machine learning project for predictive maintenance based on sensor-like machine data.

## Goal

The goal of this project is to predict machine failure based on operational parameters such as temperature, rotational speed, torque and tool wear.

The project follows a realistic data and machine learning workflow:

```text
CSV dataset -> SQLite database -> SQL queries -> Pandas EDA -> ML model -> saved model -> FastAPI -> Docker
```

## Current status

| Module                         | Status      | Description                                                                      |
| ------------------------------ | ----------- | -------------------------------------------------------------------------------- |
| Module 0 — Project setup       | Done        | Project structure, virtual environment, requirements.txt and GitHub repository   |
| Module 1 — Dataset + SQL layer | Done        | Dataset inspection, SQLite database, SQL table, CSV loading and analysis queries |
| Module 2 — Pandas + EDA        | Done        | Loaded data from SQL into Pandas, performed EDA and feature engineering          |
| Module 3 — ML baseline         | Done        | Trained and evaluated Logistic Regression and Random Forest baseline models      |
| Module 4 — Prediction function | In progress | Load saved model and create local prediction function                            |
| Module 5 — FastAPI             | Planned     | Expose prediction through REST API                                               |
| Module 6 — Docker + README     | Planned     | Containerize project and finalize documentation                                  |

## Project structure

```text
SensorGuard_ML/
├── api/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── learning_log_module_1.md
│   ├── learning_log_module_2.md
│   └── learning_log_module_3.md
├── models/
│   └── random_forest.joblib
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
│   ├── preprocessing.py
│   └── train.py
├── requirements.txt
└── README.md
```

## Completed work

### Module 0 — Project setup

* Created project repository
* Created virtual environment
* Prepared project folder structure
* Created `requirements.txt`
* Created initial README

### Module 1 — Dataset + SQL layer

* Inspected the AI4I dataset using Pandas
* Checked columns, data types, missing values and target distribution
* Created SQLite database
* Created SQL table `machine_measurements`
* Renamed raw CSV columns to SQL-friendly `snake_case` names
* Loaded 10,000 rows into SQLite
* Wrote SQL analysis queries using `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `COUNT`, `AVG`, `SUM` and `DISTINCT`

### Module 2 — Pandas + EDA

* Loaded data from SQLite into a Pandas DataFrame
* Created reusable preprocessing functions:

  * `load_data_from_sql()`
  * `add_features(df)`
  * `prepare_features_and_target(df)`
* Added engineered features:

  * `temperature_difference`
  * `power_proxy`
* Performed basic exploratory data analysis
* Checked dataset shape, data types and descriptive statistics
* Checked missing values and duplicated rows
* Analyzed target distribution and class imbalance
* Compared average feature values for failure and non-failure cases
* Added basic plots for target distribution and selected numerical features
* Created `notebooks/01_eda_and_modeling.ipynb`

### Module 3 — ML baseline

* Prepared features and target for machine learning
* Removed leakage columns from model input:

  * `twf`
  * `hdf`
  * `pwf`
  * `osf`
  * `rnf`
* Split data into training and test sets using `train_test_split`
* Used `stratify=y` to preserve class distribution in train and test sets
* Built preprocessing pipeline:

  * `StandardScaler` for numerical features
  * `OneHotEncoder` for categorical feature `product_type`
* Trained Logistic Regression baseline model
* Trained Random Forest baseline model
* Evaluated models using:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * Confusion Matrix
* Compared Logistic Regression and Random Forest results
* Selected Random Forest as the main model
* Saved trained Random Forest pipeline to `models/random_forest.joblib`

## Model results

### Logistic Regression

| Metric    |  Value |
| --------- | -----: |
| Accuracy  | 0.8585 |
| Precision | 0.1772 |
| Recall    | 0.8676 |
| F1-score  | 0.2943 |

Confusion matrix:

```text
[[1658  274]
 [   9   59]]
```

### Random Forest

| Metric    |  Value |
| --------- | -----: |
| Accuracy  | 0.9890 |
| Precision | 0.8966 |
| Recall    | 0.7647 |
| F1-score  | 0.8254 |

Confusion matrix:

```text
[[1926    6]
 [  16   52]]
```

## Key model conclusion

Logistic Regression achieved higher recall, meaning it detected more real failures, but it produced many false positives.

Random Forest achieved much better precision and F1-score, with only a small number of false positives. Because of this, Random Forest was selected as the main model and saved with `joblib`.

## Tech stack

Python, SQLite, SQL, Pandas, NumPy, scikit-learn, joblib, FastAPI, Docker

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
```

Train and evaluate baseline machine learning models:

```powershell
python src/train.py
```

Expected output includes:

```text
=== LOGISTIC REGRESSION METRICS ===
=== RANDOM FOREST METRICS ===
=== METRICS COMPARISON ===
=== MODEL SAVED ===
```

The trained Random Forest pipeline is saved to:

```text
models/random_forest.joblib
```

## Interview explanation

English:

> In this project, I built an end-to-end machine learning workflow for predictive maintenance. I started by storing the dataset in SQLite and practicing SQL queries. Then I loaded the data into Pandas, performed exploratory data analysis, checked missing values, duplicates and class imbalance, and created additional features such as temperature difference and a simple machine load proxy. After that, I trained Logistic Regression and Random Forest baseline models and evaluated them using accuracy, precision, recall, F1-score and confusion matrix. Since machine failures are rare, I did not rely only on accuracy. Random Forest achieved the best overall result, especially in terms of precision and F1-score, so I saved it as the main model.

Polish:

> W tym projekcie zbudowałem pełny workflow uczenia maszynowego dla problemu predictive maintenance. Najpierw przechowywałem dane w SQLite i ćwiczyłem zapytania SQL. Następnie wczytałem dane do Pandas, przeprowadziłem eksploracyjną analizę danych, sprawdziłem brakujące wartości, duplikaty oraz niezbalansowanie klas i dodałem nowe cechy, takie jak różnica temperatur oraz przybliżony wskaźnik obciążenia maszyny. Potem wytrenowałem modele bazowe Logistic Regression oraz Random Forest i oceniłem je za pomocą accuracy, precision, recall, F1-score oraz confusion matrix. Ponieważ awarie są rzadką klasą, nie patrzyłem tylko na accuracy. Random Forest osiągnął najlepszy ogólny wynik, szczególnie pod względem precision oraz F1-score, dlatego zapisałem go jako główny model.
