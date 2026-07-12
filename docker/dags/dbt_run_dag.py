from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'wc2026',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dbt_run_dag',
    default_args=default_args,
    start_date=datetime(2026, 7, 10),
    schedule_interval='0 * * * *',
    catchup=False
) as dag:

    run_dbt = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/airflow/wc2026_dbt/wc2026 && dbt run'
    )