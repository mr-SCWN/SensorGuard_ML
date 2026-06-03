import pandas as pd

DATA_PATH = "data/raw/ai4i2020.csv"

# Load raw dataset
df = pd.read_csv(DATA_PATH)

print("\n=== HEAD ===")
print(df.head())

print("\n=== SHAPE ===")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n=== COLUMNS ===")
print(df.columns)

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isna().sum())

print("\n=== TARGET DISTRIBUTION: Machine failure ===")
print(df["Machine failure"].value_counts())

print("\n=== TARGET DISTRIBUTION PERCENTAGE ===")
print(df["Machine failure"].value_counts(normalize=True) * 100)

print("\n=== FAILURE TYPES COUNTS ===")
print(df[["TWF", "HDF", "PWF", "OSF", "RNF"]].sum())