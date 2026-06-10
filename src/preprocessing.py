import pandas as pd
import sqlite3
from pathlib import Path 

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "data" / "processed" / "sensorguard.db"

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

def add_features(df):
    # Create a copy of the DataFrame
    df_copy = df.copy()
    # Add temperature difference feature
    df_copy["temperature_difference"] = df_copy["process_temperature_k"] - df_copy["air_temperature_k"]
    # Add power proxy feature
    df_copy["power_proxy"] = df_copy["torque_nm"] * df_copy["rotational_speed_rpm"]
    # Return updated DataFrame    
    return df_copy

def prepare_features_and_target(df):
    X = df.drop(columns = ['udi', 'product_id', 'machine_failure', 'twf', 'hdf', 'pwf', 'osf', 'rnf'])
    y = df['machine_failure']
    return X, y


if __name__ == "__main__":
    ## ----- LOAD DATA
    df = load_data_from_sql() # verification load_data_from_sql
    print(df.head())
    print(df.shape)

    ## ----- ADD FEATURES
    df_with_features = add_features(df) # verification add_features 
    print(df_with_features[['air_temperature_k', 'process_temperature_k', 'temperature_difference',
            'torque_nm', 'rotational_speed_rpm', 'power_proxy']].head())
    print(df_with_features.shape)

    ## - FEATURES AND TARGET
    X, y = prepare_features_and_target(df_with_features)
    print("\n=== FEATURES HEAD ===")
    print(X.head())

    print("\n=== FEATURES SHAPE ===")
    print(X.shape)

    print("\n=== TARGET DISTRIBUTION ===")
    print(y.value_counts())

    print("\n=== TARGET SHAPE ===")
    print(y.shape)  
