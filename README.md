# Fraud Detection System

## Project Overview
The **Fraud Detection System** is a complete end-to-end platform designed to detect fraudulent transactions in **banking, credit card, and payment systems**. It leverages **machine learning, anomaly detection, explainable AI, and real-time deployment** to provide actionable insights and risk scoring.

This project is **modular, scalable, and deployable**, making it suitable for showcasing in a portfolio or GitHub repository for Data Science and ML roles.

### Key Features
- **Supervised ML Models:** XGBoost for fraud detection.
- **Class Imbalance Handling:** Weighted positive cases to handle rare fraud occurrences.
- **Anomaly Detection:** Isolation Forest for unsupervised detection of suspicious transactions.
- **Explainable AI:** SHAP visualizations to interpret model predictions.
- **Real-Time API:** FastAPI service for scoring new transactions on-the-fly.
- **Automated Retraining:** Airflow DAG for scheduled model updates.
- **BI-Ready Analytics:** SQL warehouse schema for integration with dashboards.

## Folder Structure
```
fraud-detection-system/
├── api/                    # FastAPI service for real-time scoring
├── data/                   # Synthetic data generation scripts
├── preprocessing/          # Data preprocessing and scaling
├── models/                 # Model training and saving scripts
├── evaluation/             # Model evaluation scripts
├── anomaly/                # Anomaly detection logic
├── explainability/         # SHAP explainability scripts
├── airflow/                # Airflow DAG for automated retraining
├── main.py                 # End-to-end pipeline runner
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignore unnecessary files
```

## Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/rishabhkarnwal04/Fraud-Detection
cd fraud-detection-system
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
> ⚠️ Use `numpy<2` to avoid compatibility issues with ML libraries like XGBoost and scikit-learn.

## Running the Project

### 1. Run Main Pipeline
```bash
python main.py
```
This will:
- Generate synthetic transaction data.
- Preprocess features and split train/test.
- Train XGBoost model and save as `fraud_model.pkl`.
- Evaluate the model (classification report & ROC-AUC).
- Detect anomalies using Isolation Forest.

### 2. Run FastAPI Real-Time API
```bash
uvicorn api.app:app --reload
```
Open Swagger UI at: `http://127.0.0.1:8000/docs` to test endpoints.

### 3. Automated Retraining with Airflow (Optional)
```bash
export AIRFLOW_HOME=~/airflow
airflow db init
airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@test.com
airflow webserver
airflow scheduler
```
Enable the DAG `fraud_model_retraining` in Airflow UI: `http://localhost:8080`.

### 4. Optional: Docker Deployment
- Create `Dockerfile` and `docker-compose.yml` linking FastAPI and Airflow.
- Run containers:
```bash
docker-compose up --build
```

## Using the API
Send a POST request to `/predict` with transaction features:
```json
[4500, 2, 1, 0]
```
Response:
```json
{
  "fraud_probability": 0.78
}
```

## Notes for Production
- Keep feature order consistent between training and inference.
- Retraining DAG ensures the model is updated with new transaction data.
- Always use virtual environments to isolate dependencies.

## CV / Portfolio Impact
- Demonstrates **full end-to-end ML pipeline** skills.
- Shows expertise in **real-time deployment, anomaly detection, explainable AI, and MLOps**.
- Suitable for **Data Scientist, ML Engineer, and FinTech roles**.
