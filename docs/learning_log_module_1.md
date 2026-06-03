# Learning Log — Module 1: Dataset + SQL Layer

Date completed: 03.06.2026

## Goal of the module

The goal of this module was to practice working with a dataset, SQLite database and basic SQL queries.

This module was especially important because SQL and basic data handling were weak points during the Capgemini technical interview.

## What I did

- Downloaded the AI4I predictive maintenance dataset
- Inspected the dataset using Pandas
- Checked:
  - first rows
  - shape
  - column names
  - data types
  - missing values
  - target distribution
  - failure type counts
- Created SQLite database
- Created SQL table `machine_measurements`
- Renamed raw CSV columns to SQL-friendly names
- Loaded 10,000 rows into SQLite
- Wrote SQL analysis queries

## Files created

```text
src/inspect_data.py
src/database.py
sql/create_tables.sql
sql/analysis_queries.sql
```

## Dataset notes

The main target column is:

```text
machine_failure
```

Meaning:

```text
0 = no machine failure
1 = machine failure
```

Additional failure type columns:

```text
twf — Tool Wear Failure
hdf — Heat Dissipation Failure
pwf — Power Failure
osf — Overstrain Failure
rnf — Random Failure
```

## SQL topics practiced

- `SELECT`
- `WHERE`
- `ORDER BY`
- `GROUP BY`
- `HAVING`
- `COUNT`
- `AVG`
- `SUM`
- `DISTINCT`

## What I learned

### SQLite

SQLite stores the database as a local `.db` file.

In this project, the database is stored here:

```text
data/processed/sensorguard.db
```

The database file is not pushed to GitHub because it is a generated file and can be recreated by running:

```powershell
python src/database.py
```

### `df.rename()`

`df.rename()` was used to rename raw CSV columns into SQL-friendly `snake_case` names.

Example:

```text
Air temperature [K] -> air_temperature_k
Machine failure -> machine_failure
Tool wear [min] -> tool_wear_min
```

### `df.to_sql()`

`df.to_sql()` loads a Pandas DataFrame into a SQL table.

In this project:

```text
Pandas DataFrame -> SQLite table machine_measurements
```

### `WHERE` vs `HAVING`

`WHERE` filters rows before grouping.

`HAVING` filters groups after `GROUP BY`.

Example:

```sql
WHERE machine_failure = 1
```

filters individual rows.

```sql
HAVING AVG(torque_nm) > 40
```

filters grouped results.

### `COUNT(*)` vs `COUNT(column)`

`COUNT(*)` counts all rows.

`COUNT(column)` counts only rows where the selected column is not `NULL`.

## Interview explanation

English:

> I used SQLite to practice working with a relational database and SQL queries. I created a table schema manually, loaded CSV data into the database and wrote SQL queries for basic analysis.

Polish:

> W projekcie dane przechowywałem w SQLite, żeby przećwiczyć pracę z relacyjną bazą danych. Do modelowania pobierałem dane za pomocą zapytań SQL, a następnie przetwarzałem je w Pandas.

## Key takeaway

After this module, I understand the basic data workflow:

```text
CSV -> Pandas -> SQLite -> SQL queries
```

I also understand the difference between `WHERE` and `HAVING`, how `GROUP BY` works and how to load data from a DataFrame into a SQL table.