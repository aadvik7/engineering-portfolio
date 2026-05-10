from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("airflow is working!")

with DAG(
    'test_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task = PythonOperator(
        task_id='hello',
        python_callable=say_hello
    )
