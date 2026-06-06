# Learning Log — Module 2: Pandas + EDA

Status: Completed

## Goal of the module

The goal of this module was to understand the dataset before training a machine learning model.

Instead of directly running `model.fit()`, I first analyzed data quality, class balance, feature behavior and basic relationships between features and the target variable.

## What I did

- Loaded data from SQLite into a Pandas DataFrame
- Created reusable preprocessing functions
- Added engineered features
- Performed basic EDA in a Python script
- Created an EDA notebook
- Checked dataset shape
- Inspected first rows
- Checked data types
- Calculated descriptive statistics
- Checked missing values
- Checked duplicated rows
- Analyzed target distribution
- Compared average feature values for failure and non-failure cases
- Created basic plots for target distribution and selected numerical features
- Wrote conclusions from the analysis

## Files created

```text
src/preprocessing.py
src/eda.py
notebooks/01_eda_and_modeling.ipynb
```

## Functions created

### `load_data_from_sql()`

This function loads data from the SQLite database into a Pandas DataFrame.

Workflow:

```text
SQLite database -> SQL query -> Pandas DataFrame
```

### `add_features(df)`

This function creates a copy of the original DataFrame and adds new engineered features.

The function returns a new DataFrame with additional columns.

## Feature engineering

### `temperature_difference`

```text
temperature_difference = process_temperature_k - air_temperature_k
```

This feature represents the difference between process temperature and air temperature.

It may be useful because a higher temperature difference can indicate additional machine load or cooling-related issues.

### `power_proxy`

```text
power_proxy = torque_nm * rotational_speed_rpm
```

This feature is an approximate proxy for machine load.

It is not an exact physical power calculation, but it can still be useful for machine learning because higher torque combined with higher rotational speed may indicate higher mechanical load.

## EDA results

Dataset shape before feature engineering:

```text
10000 rows, 14 columns
```

Dataset shape after feature engineering:

```text
10000 rows, 16 columns
```

Missing values:

```text
0
```

Duplicated rows:

```text
0
```

Target distribution:

```text
machine_failure = 0: 9661 rows
machine_failure = 1: 339 rows
```

Target percentage:

```text
machine_failure = 0: 96.61%
machine_failure = 1: 3.39%
```

## Basic plots created

The notebook contains basic plots for:

- target distribution
- torque distribution
- tool wear distribution
- power proxy distribution
- average torque by target

## Key observations

The dataset is strongly imbalanced.

Machine failures represent only 3.39% of all observations.

This means that accuracy alone can be misleading. A model could predict the majority class most of the time and still achieve high accuracy, while failing to detect real machine failures.

Average feature values show that failure cases tend to have:

- higher torque
- higher tool wear
- higher power proxy
- lower rotational speed

This suggests that machine load and tool wear may be important factors for predicting machine failure.

## What I learned

- How to load data from SQLite into Pandas
- Why reusable preprocessing functions are useful
- How to check missing values
- How to check duplicated rows
- How to analyze class imbalance
- Why accuracy can be misleading for imbalanced classification problems
- How to compare average feature values by target
- How to create basic plots with Matplotlib
- How feature engineering can create more informative variables from raw sensor data

## Interview explanation

English:

> First, I checked data quality using Pandas: data types, missing values, duplicated rows and target distribution. I found that the dataset is strongly imbalanced because machine failures represent only a small part of all observations. Because of that, accuracy alone may be misleading. I also created additional features such as temperature difference and a simple machine load proxy.

Polish:

> Najpierw sprawdziłem jakość danych w Pandas: typy kolumn, brakujące wartości, duplikaty oraz rozkład zmiennej docelowej. Zobaczyłem, że dane są mocno niezbalansowane, ponieważ awarie stanowią tylko małą część wszystkich obserwacji. Dlatego sama accuracy może być myląca. Dodałem też nowe cechy, takie jak różnica temperatur oraz przybliżony wskaźnik obciążenia maszyny.

## Key takeaway

After Module 2, I understand the basic EDA workflow:

```text
SQLite -> Pandas DataFrame -> basic EDA -> feature engineering -> plots -> conclusions
```

I also understand why class imbalance is important and why model evaluation should not rely only on accuracy.

The dataset is now ready for the next step: training baseline machine learning models.