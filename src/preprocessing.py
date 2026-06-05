import pandas as pd
import sqlite3

DB_PATH = "data/processed/sensorguard.db"

def load_data_from_sql():
    # 1. Connect to SQLite database
    connection = sqlite3.connect(DB_PATH)

    # 2. Create SQL query
    query = "SELECT * FROM machine_measurements;" 

    # 3. Read SQL query result into DataFrame
    df = pd.read_sql_query(query, connection)

    # 4. Close connection
    connection.close()
    
    # 5. Return DataFrame
    return df


if __name__ == "__main__":
    df = load_data_from_sql()
    print(df.head())
    print(df.shape)