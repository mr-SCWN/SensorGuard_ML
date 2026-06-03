import sqlite3
import pandas as pd

DB_PATH = "data/processed/sensorguard.db"

query = """
SELECT product_type, AVG(torque_nm) AS avg_torque_nm
FROM machine_measurements
GROUP BY product_type
HAVING AVG(torque_nm) > 40;
"""

connection = sqlite3.connect(DB_PATH)

result = pd.read_sql_query(query, connection)

print(result)

connection.close()