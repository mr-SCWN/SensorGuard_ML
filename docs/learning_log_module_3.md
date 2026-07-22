# Learning Log — Module 3: ML Baseline

Status: Completed

## Goal of the module

The goal of this module was to train baseline machine learning models and understand how to evaluate them correctly.

This module was especially important because the dataset is strongly imbalanced. Machine failures are rare, so accuracy alone can be misleading.

## What I did

* Prepared features and target for machine learning
* Removed columns that could cause data leakage
* Split the dataset into training and test sets
* Used stratified splitting to preserve class distribution
* Created preprocessing pipeline for numerical and categorical features
* Trained Logistic Regression baseline model
* Trained Random Forest baseline model
* Evaluated both models using classification metrics
* Compared model results
* Selected Random Forest as the main model
* Saved trained Random Forest pipeline using `joblib`

## Files created or updated

```text
src/preprocessing.py
src/train.py
models/random_forest.joblib
```

## Target variable

The target column is:

```text
machine_failure
```

Meaning:

```text
0 = no machine failure
1 = machine failure
```

This is a binary classification problem.

## Features used

The model input features are:

```text
product_type
air_temperature_k
process_temperature_k
rotational_speed_rpm
torque_nm
tool_wear_min
temperature_difference
power_proxy
```

## Columns removed from model input

The following columns were removed from `X`:

```text
udi
product_id
machine_failure
twf
hdf
pwf
osf
rnf
```

Reasons:

```text
udi                 -> row identifier
product_id          -> product identifier
machine_failure     -> target variable
twf/hdf/pwf/osf/rnf -> failure type columns, possible data leakage
```

The failure type columns were not used as input features because they already contain information about the failure. In a real prediction scenario, these values would not be known before making the prediction.

## Train/test split

The dataset was split into training and test sets:

```text
80% training data
20% test data
```

I used:

```text
stratify=y
```

This preserves a similar class distribution in both training and test sets.

Target distribution in the test set:

```text
machine_failure = 0: 1932 rows
machine_failure = 1: 68 rows
```

## Preprocessing pipeline

The preprocessing pipeline used two different transformations:

### Numerical features

Numerical features were processed using:

```text
StandardScaler
```

This was useful for Logistic Regression because numerical columns had different scales.

Example:

```text
torque_nm              -> around 40
rotational_speed_rpm   -> around 1500
power_proxy            -> around 60000
```

### Categorical features

The categorical feature was:

```text
product_type
```

It was processed using:

```text
OneHotEncoder
```

This transformed values such as `L`, `M` and `H` into numerical columns that can be used by machine learning models.

## Models trained

### Logistic Regression

Logistic Regression was used as a simple baseline model.

Advantages:

* simple
* fast
* easy to interpret
* useful as a first comparison point

In this project, Logistic Regression achieved high recall but low precision.

This means that it detected many real failures, but also produced many false alarms.

### Random Forest

Random Forest was used as a stronger baseline model for tabular data.

Advantages:

* works well with tabular data
* can capture non-linear relationships
* can learn combinations of features
* often performs better than simple linear models

In this project, Random Forest achieved much better precision and F1-score than Logistic Regression.

## Model evaluation metrics

I evaluated the models using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

## Why accuracy alone is not enough

The dataset is strongly imbalanced.

Most observations belong to class `0`, while failures are rare.

This means that a model could predict `0` most of the time and still achieve high accuracy, while failing to detect real machine failures.

Because of that, I also analyzed precision, recall and F1-score.

## Logistic Regression results

```text
Accuracy:  0.8585
Precision: 0.1772
Recall:    0.8676
F1-score:  0.2943
```

Confusion matrix:

```text
[[1658  274]
 [   9   59]]
```

Interpretation:

```text
TN = 1658
FP = 274
FN = 9
TP = 59
```

Logistic Regression detected 59 out of 68 real failures, but produced 274 false alarms.

Main conclusion:

```text
High recall, but low precision.
```

## Random Forest results

```text
Accuracy:  0.9890
Precision: 0.8966
Recall:    0.7647
F1-score:  0.8254
```

Confusion matrix:

```text
[[1926    6]
 [  16   52]]
```

Interpretation:

```text
TN = 1926
FP = 6
FN = 16
TP = 52
```

Random Forest detected 52 out of 68 real failures and produced only 6 false alarms.

Main conclusion:

```text
Much better precision and F1-score.
```

## Model comparison

| Model               | Accuracy | Precision | Recall | F1-score |
| ------------------- | -------: | --------: | -----: | -------: |
| Logistic Regression |   0.8585 |    0.1772 | 0.8676 |   0.2943 |
| Random Forest       |   0.9890 |    0.8966 | 0.7647 |   0.8254 |

## Selected model

Random Forest was selected as the main model.

Reason:

```text
Random Forest achieved the best overall performance, especially in terms of precision and F1-score.
```

Although Logistic Regression achieved higher recall, it produced too many false positives.

The selected model was saved to:

```text
models/random_forest.joblib
```

Important note:

The saved file contains the full pipeline:

```text
preprocessing + Random Forest classifier
```

This is important because future predictions require the same preprocessing steps, including scaling numerical features and encoding `product_type`.

## What I learned

* How to prepare `X` and `y` for classification
* Why leakage columns should not be used as input features
* How to split data into train and test sets
* Why `stratify=y` is important for imbalanced datasets
* How to use `ColumnTransformer`
* How to use `OneHotEncoder`
* How to use `StandardScaler`
* How to build an ML `Pipeline`
* How to train Logistic Regression
* How to train Random Forest
* How to evaluate models using precision, recall and F1-score
* How to interpret confusion matrix
* How to save a trained model using `joblib`

## Interview explanation

English:

> I trained two baseline models: Logistic Regression and Random Forest. Logistic Regression was used as a simple and interpretable baseline, while Random Forest was used as a stronger model for tabular data. Because machine failures are rare, I did not rely only on accuracy. I evaluated the models using precision, recall, F1-score and confusion matrix. Logistic Regression achieved higher recall, but produced many false positives. Random Forest achieved much better precision and F1-score, so I selected it as the main model and saved the full pipeline using joblib.

Polish:

> Wytrenowałem dwa modele bazowe: Logistic Regression oraz Random Forest. Logistic Regression potraktowałem jako prosty i interpretowalny baseline, a Random Forest jako silniejszy model dla danych tabelarycznych. Ponieważ awarie są rzadką klasą, nie patrzyłem tylko na accuracy. Oceniłem modele za pomocą precision, recall, F1-score oraz confusion matrix. Logistic Regression osiągnęła wyższy recall, ale generowała dużo fałszywych alarmów. Random Forest osiągnął dużo lepszy precision oraz F1-score, dlatego wybrałem go jako główny model i zapisałem cały pipeline za pomocą joblib.

## Key takeaway

After Module 3, I understand the basic machine learning workflow:

```text
features and target -> train/test split -> preprocessing -> model training -> evaluation -> model saving
```

I also understand why class imbalance changes the way a model should be evaluated.

The project now has a trained and saved machine learning model that can be loaded and used in the next module.
