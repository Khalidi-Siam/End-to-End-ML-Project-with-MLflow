# End-to-End ML Project with MLflow

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/stable/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?logo=mlflow&logoColor=white)](https://mlflow.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/Project-End--to--End%20ML-success)](#project-pipeline)

A production-style machine learning workflow for **Red Wine Quality** prediction, featuring:

- A modular, multi-stage training pipeline
- Artifact-driven MLOps structure for full traceability
- Experiment tracking and model logging with **MLflow**
- A **Flask** web application for real-time inference

The project trains an **ElasticNet** regressor on physicochemical wine features to predict a quality score.

---

## Features

- End-to-end modular ML pipeline: ingestion → validation → transformation → training → evaluation
- Centralized configuration via YAML (`config.yaml`, `params.yaml`, `schema.yaml`)
- Schema and data type validation before downstream stages
- Artifact-based workflow under `artifacts/` for full reproducibility
- Model persistence using `joblib`
- MLflow tracking for parameters, metrics, and model versioning
- Flask UI for live predictions using user-provided feature values
- Structured logging and custom exception handling throughout

---

## Problem Statement

Given 11 physicochemical properties of red wine, predict the wine **quality** score.

**Input features:**

| Feature | Feature |
|---|---|
| Fixed Acidity | Volatile Acidity |
| Citric Acid | Residual Sugar |
| Chlorides | Free Sulfur Dioxide |
| Total Sulfur Dioxide | Density |
| pH | Sulphates |
| Alcohol | *(target: quality)* |

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| ML & Data | scikit-learn, Pandas, NumPy |
| Experiment Tracking | MLflow |
| Web Framework | Flask |
| Config & Serialization | PyYAML, joblib |

---

## Project Pipeline

The training run is orchestrated in `main.py` and executes the following stages in sequence:

### 1. Data Ingestion
- Downloads a zipped dataset from the configured source URL.
- Extracts the CSV into the `artifacts/` directory.

### 2. Data Validation
- Checks for required column presence against the defined schema.
- Validates that no unexpected columns are present.
- Validates data types for each column.
- Writes the validation report to `artifacts/data_validation/status.txt`.

### 3. Data Transformation
- Performs a train/test split (`test_size=0.2`, `random_state=42`).
- Saves the resulting split datasets to `artifacts/`.

### 4. Model Training
- Trains an `ElasticNet` regressor using hyperparameters defined in `params.yaml`.
- Persists the trained model to `artifacts/model_trainer/model.joblib`.

### 5. Model Evaluation & MLflow Logging
- Loads the test set and trained model from artifacts.
- Computes **RMSE**, **MAE**, and **R²** metrics.
- Saves metrics locally as a JSON file.
- Logs parameters, metrics, and the model artifact to the configured MLflow tracking server.

---

## MLOps Design

This project follows practical MLOps patterns for maintainability and reproducibility:

- **Config-driven pipeline** — data paths, hyperparameters, and schema are never hardcoded.
- **Stage isolation** — each stage has dedicated pipeline and component modules with clear boundaries.
- **Artifact lineage** — every stage writes outputs to `artifacts/` for traceability and reproducibility.
- **Observability** — runtime logs are written under `logs/`.
- **Experiment tracking** — MLflow captures parameters, metrics, and model versions across runs.

---

## MLflow Setup

Before running the model evaluation stage (stage 5), set the following environment variables:

| Variable | Description |
|---|---|
| `MLFLOW_TRACKING_URI` | URL of your MLflow tracking server |
| `MLFLOW_TRACKING_USERNAME` | Your MLflow username |
| `MLFLOW_TRACKING_PASSWORD` | Your MLflow password or token |

> **Note:** All three variables are validated before evaluation begins. They must be set even when using a local MLflow server.

### Remote Server (PowerShell)

```powershell
$env:MLFLOW_TRACKING_URI="https://your-mlflow-server"
$env:MLFLOW_TRACKING_USERNAME="your-username"
$env:MLFLOW_TRACKING_PASSWORD="your-password-or-token"
```

### Local MLflow Server

Run the MLflow UI in one terminal:

```powershell
mlflow ui --host 127.0.0.1 --port 5000
```

Then set the environment variables in a second terminal before running the pipeline:

```powershell
$env:MLFLOW_TRACKING_URI="http://127.0.0.1:5000"
$env:MLFLOW_TRACKING_USERNAME="local"
$env:MLFLOW_TRACKING_PASSWORD="local"
```

---

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/khalidi-siam/End-to-End-ML-Project-with-MLflow.git
cd End-to-End-ML-Project-with-MLflow
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### 4. Configure MLflow environment variables

Set the three variables described in the [MLflow Setup](#mlflow-setup) section before running the pipeline.

---

## How to Run

### Run the full training pipeline

```bash
python main.py
```

### Launch the Flask prediction app

```bash
python app.py
```

Open in browser: `http://127.0.0.1:8000`

---

## Docker

The repository includes a `Dockerfile` that packages and serves the Flask application.

### Build the image

```bash
docker build -t wine-quality-mlflow .
```

### Run the container

```bash
docker run --rm -p 8000:8000 wine-quality-mlflow
```

Open in browser: `http://127.0.0.1:8000`

### Optional: Pass MLflow environment variables to the container

If you run evaluation code in containerized workflows, provide MLflow credentials at runtime:

```bash
docker run --rm -p 8000:8000 \
  -e MLFLOW_TRACKING_URI="http://host.docker.internal:5000" \
  -e MLFLOW_TRACKING_USERNAME="local" \
  -e MLFLOW_TRACKING_PASSWORD="local" \
  wine-quality-mlflow
```

---

## Expected Outputs

After a successful pipeline run, the following artifacts are generated:

| Path | Contents |
|---|---|
| `artifacts/data_ingestion/` | Downloaded and extracted dataset |
| `artifacts/data_validation/status.txt` | Schema validation report |
| `artifacts/data_transformation/` | Train and test CSV files |
| `artifacts/model_trainer/model.joblib` | Serialized trained model |
| `artifacts/model_evaluation/metrics.json` | RMSE, MAE, and R² scores |
| `logs/` | Runtime logs for all pipeline stages |
| MLflow UI | Experiment runs with params, metrics, and model artifacts |

---

## Repository Structure

```text
.
├── app.py                     # Flask inference application
├── main.py                    # Pipeline orchestrator (runs all stages)
├── config/
│   └── config.yaml            # Pipeline stage paths and data sources
├── params.yaml                # Model hyperparameters
├── schema.yaml                # Expected dataset schema and dtypes
├── src/mlProject/
│   ├── components/            # Stage implementation logic
│   ├── config/                # Configuration manager
│   ├── entity/                # Dataclass config contracts
│   ├── pipeline/              # Stage entrypoints and prediction pipeline
│   ├── utils/                 # Common helpers and environment validators
│   ├── logger.py              # Logging setup
│   └── exception.py           # Custom exception wrapper
├── templates/                 # HTML templates for Flask app
├── research/                  # Jupyter notebooks for experimentation
├── artifacts/                 # Generated pipeline outputs (gitignored)
└── logs/                      # Runtime logs (gitignored)
```

---

## Notes

- Do not commit credentials or access tokens. Use a local `.env` file during development and load values into your shell before running stage 5.
- The Docker image entrypoint runs `python app.py` and serves on port `8000`.

---

## Author

**Khalidi Siam**