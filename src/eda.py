from preprocessing import load_data_from_sql, add_features

def run_eda():
    # Load data from SQLite
    df = load_data_from_sql()

    # Add engineered features
    df_with_features = add_features(df)
    
    # Print shape
    print("\n=== SHAPE ===")
    print(df_with_features.shape)

    # Print head
    print("\n=== HEAD ===")
    print(df_with_features.head())

    # Print info
    print("\n=== INFO ===")
    df_with_features.info()

    # Print descriptive statistics
    print("\n=== DESCRIPTIVE STATISTICS ===")
    print(df_with_features.describe())

    # Print missing values
    print("\n=== MISSING VALUES ===")
    print(df_with_features.isna().sum())

    # Print duplicates count
    print("\n=== DUPLICATES COUNT ===")
    print(df_with_features.duplicated().sum())
    
    # Print target distribution
    print("\n=== TARGET DISTRIBUTION ===")
    print(df_with_features['machine_failure'].value_counts())

    # Print target distribution percentage
    print("\n=== DISTRIBUTION PERCENTAGE ===")
    print(df_with_features['machine_failure'].value_counts(normalize=True)*100)


    # Compare average feature values by target
    print("\n=== AVERAGE FEATURE VALUES BY TARGET ===")
    print(df_with_features.groupby('machine_failure')[['air_temperature_k',
                                    'process_temperature_k',
                                    'temperature_difference',
                                    'rotational_speed_rpm',
                                    'torque_nm',
                                    'tool_wear_min',
                                    'power_proxy']].mean()) # machine_failure = TARGET


if __name__ == "__main__":
    run_eda()