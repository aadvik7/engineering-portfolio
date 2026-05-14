import sys
sys.path.insert(0, '/opt/airflow/src')

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract import fetch_news

default_args = {
    'owner': 'aadvik',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def run_extract(**context):
    articles = fetch_news(query="technology")
    context['ti'].xcom_push(key='raw_articles', value=articles)

with DAG(
    'news_pipeline',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=run_extract
    )
