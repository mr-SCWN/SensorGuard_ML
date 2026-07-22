import pandas as pd

from preprocessing import load_data_from_sql, add_features, prepare_features_and_target
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


def main():
    # 1. Load data from SQLite
    df = load_data_from_sql()

    # 2. Add engineered features
    df_with_features = add_features(df)

    # 3. Prepare X and y
    X, y = prepare_features_and_target(df_with_features)

    # 4. Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # 5. Define feature groups
    numeric_features = [
        "air_temperature_k",
        "process_temperature_k",
        "rotational_speed_rpm",
        "torque_nm",
        "tool_wear_min",
        "temperature_difference",
        "power_proxy",
    ]

    categorical_features = ["product_type"]

    # 6. Define preprocessing for numerical and categorical columns
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )

    # 7. Create Logistic Regression pipeline
    logistic_regression_model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    random_state=42
                )
            ),
        ]
    )

    # 8. Train the model
    logistic_regression_model.fit(X_train, y_train)

    # 9. Make predictions on test data
    y_pred = logistic_regression_model.predict(X_test)

    # METRICS
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    print("\n=== LOGISTIC REGRESSION METRICS ===")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-score:  {f1:.4f}")

    print("\n=== CONFUSION MATRIX ===")
    print(conf_matrix)
    
    # 10. Print shapes
    print("\n=== DATA SHAPES ===")
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"y_test shape: {y_test.shape}")

    # 11. Print target distribution
    print("\n=== TRAIN TARGET DISTRIBUTION ===")
    print(y_train.value_counts())

    print("\n=== TEST TARGET DISTRIBUTION ===")
    print(y_test.value_counts())

    # 12. Print prediction distribution
    print("\n=== LOGISTIC REGRESSION PREDICTIONS DISTRIBUTION ===")
    print(pd.Series(y_pred).value_counts().sort_index())


if __name__ == "__main__":
    main()