from preprocessing import load_data_from_sql, add_features, prepare_features_and_target
from sklearn.model_selection import train_test_split

def main():
    # Load data
    df = load_data_from_sql()

    # Add engineered features
    df_with_features = add_features(df)

    # Prepare X and y
    X, y = prepare_features_and_target(df_with_features)

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Print shapes
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"y_test shape: {y_test.shape}")

    # Print target distribution in train and test
    print(f"Train target distribution:\n{y_train.value_counts()}\n")
    print(f"Test target distribution:\n{y_test.value_counts()}\n")
    print(f"Train target distribution percentage:\n{y_train.value_counts(normalize=True) * 100}\n")
    print(f"Test target distribution percentage:\n{y_test.value_counts(normalize=True) * 100}\n")



if __name__ == "__main__":
    main()