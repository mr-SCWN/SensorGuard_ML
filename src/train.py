import pandas as pd
from pathlib import Path
import joblib

from preprocessing import load_data_from_sql, add_features, prepare_features_and_target

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)



RANDOM_STATE = 42
TEST_SIZE = 0.2
PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "random_forest.joblib"

NUMERIC_FEATURES = [
    "air_temperature_k",
    "process_temperature_k",
    "rotational_speed_rpm",
    "torque_nm",
    "tool_wear_min",
    "temperature_difference",
    "power_proxy",
]

CATEGORICAL_FEATURES = ["product_type"]


def create_preprocessor():
    """Create preprocessing pipeline for numerical and categorical features."""
    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_FEATURES),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
        ]
    )


def create_logistic_regression_model():
    """Create Logistic Regression pipeline."""
    return Pipeline(
        steps=[
            ("preprocessor", create_preprocessor()),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )


def create_random_forest_model():
    """Create Random Forest pipeline."""
    return Pipeline(
        steps=[
            ("preprocessor", create_preprocessor()),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=100,
                    class_weight="balanced",
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )


def evaluate_model(model_name, y_true, y_pred):
    """Calculate and print model evaluation metrics."""
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    conf_matrix = confusion_matrix(y_true, y_pred)

    print(f"\n=== {model_name} METRICS ===")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-score:  {f1:.4f}")

    print(f"\n=== {model_name} CONFUSION MATRIX ===")
    print(conf_matrix)

    return {
        "model": model_name,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
    }


def print_data_summary(X_train, X_test, y_train, y_test):
    """Print basic information about train and test sets."""
    print("\n=== DATA SHAPES ===")
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape:  {X_test.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"y_test shape:  {y_test.shape}")

    print("\n=== TRAIN TARGET DISTRIBUTION ===")
    print(y_train.value_counts())

    print("\n=== TEST TARGET DISTRIBUTION ===")
    print(y_test.value_counts())


def train_and_evaluate_model(model_name, model, X_train, X_test, y_train, y_test):
    """Train model, make predictions and evaluate results."""
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = evaluate_model(model_name, y_test, y_pred)

    print(f"\n=== {model_name} PREDICTIONS DISTRIBUTION ===")
    print(pd.Series(y_pred).value_counts().sort_index())

    return metrics


def save_model(model, model_path):
    """Save trained model to disk."""
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)

    print(f"\n=== MODEL SAVED ===")
    print(f"Saved model to: {model_path}")


def main():
    # 1. Load data from SQLite
    df = load_data_from_sql()

    # 2. Add engineered features
    df_with_features = add_features(df)

    # 3. Prepare features and target
    X, y = prepare_features_and_target(df_with_features)

    # 4. Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    print_data_summary(X_train, X_test, y_train, y_test)

    # 5. Create models
    models = {
        "LOGISTIC REGRESSION": create_logistic_regression_model(),
        "RANDOM FOREST": create_random_forest_model(),
    }

    # 6. Train and evaluate models
    metrics_results = []

    for model_name, model in models.items():
        metrics = train_and_evaluate_model(
            model_name,
            model,
            X_train,
            X_test,
            y_train,
            y_test,
        )
        metrics_results.append(metrics)

    # 7. Print comparison table
    metrics_df = pd.DataFrame(metrics_results)

    print("\n=== METRICS COMPARISON ===")
    print(metrics_df.round(4))

    # 8. Save the best model
    save_model(models["RANDOM FOREST"], MODEL_PATH)


if __name__ == "__main__":
    main()