from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def retrain():
print('Model retrained and saved')

with DAG(dag_id='fraud_model_retraining', start_date=datetime(2024,1,1), schedule_interval='@daily', catchup=False) as dag:
retrain_task = PythonOperator(task_id='retrain_model', python_callable=retrain)
