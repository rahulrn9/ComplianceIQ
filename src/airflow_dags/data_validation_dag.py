from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import json

default_args = {
    'owner': 'compliance',
    'start_date': datetime(2025, 7, 6),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def validate_data():
    with open('/tmp/compliance_data.json') as f:
        data = json.load(f)
    if "record_id" not in data:
        raise ValueError("Schema validation failed: 'record_id' missing")
    print("Data validation passed")

with DAG('compliance_data_validation', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    validate_task = PythonOperator(
        task_id='validate_json_schema',
        python_callable=validate_data
    )
