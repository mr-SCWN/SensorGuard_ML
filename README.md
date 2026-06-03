# SensorGuard ML

End-to-end machine learning project for predictive maintenance based on sensor-like machine data.

## Goal

The goal of this project is to predict machine failure based on operational parameters such as temperature, rotational speed, torque and tool wear.

## Planned pipeline

1. Load dataset
2. Store data in SQLite database
3. Extract data using SQL
4. Perform EDA and preprocessing in Pandas
5. Train baseline ML models
6. Evaluate model using precision, recall, F1-score and confusion matrix
7. Expose prediction through FastAPI
8. Containerize with Docker

## Tech stack

Python, SQL, Pandas, NumPy, scikit-learn, FastAPI, Docker