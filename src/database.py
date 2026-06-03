import sqlite3
import pandas as pd

CSV_PATH = "data/raw/ai4i2020.csv"
DB_PATH = "data/processed/sensorguard.db"
SQL_PATH = "sql/create_tables.sql"

# Connect to SQLite database
connection = sqlite3.connect(DB_PATH)

# Read SQL script
with open(SQL_PATH, "r", encoding="utf-8") as file:
    create_tables_sql = file.read()

# Execute SQL script
connection.executescript(create_tables_sql)

# Load CSV to DataFrame
df = pd.read_csv(CSV_PATH)

# Rename columns to match SQL table schema
df = df.rename(
    columns={
        "UDI": "udi",
        "Product ID": "product_id",
        "Type": "product_type",
        "Air temperature [K]": "air_temperature_k",
        "Process temperature [K]": "process_temperature_k",
        "Rotational speed [rpm]": "rotational_speed_rpm",
        "Torque [Nm]": "torque_nm",
        "Tool wear [min]": "tool_wear_min",
        "Machine failure": "machine_failure",
        "TWF": "twf",
        "HDF": "hdf",
        "PWF": "pwf",
        "OSF": "osf",
        "RNF": "rnf"
    }
)

# Load DataFrame to SQL
df.to_sql("machine_measurements", connection , if_exists="append", index=False)

# Check number of loaded rows
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM machine_measurements;")
rows_count = cursor.fetchone()[0]
print(f"Loaded rows: {rows_count}")

# Close connection
connection.commit()
connection.close()