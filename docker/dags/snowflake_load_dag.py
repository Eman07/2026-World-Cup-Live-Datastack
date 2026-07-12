from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'wc2026',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='snowflake_load_dag',
    default_args=default_args,
    start_date=datetime(2026, 7, 1),
    schedule_interval='0 * * * *',  # every hour at :00,
    catchup=False
) as dag:

    load_match_events = SnowflakeOperator(
        task_id='load_match_events',
        snowflake_conn_id='snowflake_default',
        sql="""
            COPY INTO RAW_WC2026.RAW.RAW_MATCH_EVENTS (RAW_DATA, SOURCE_FILE)
            FROM (
                SELECT $1::VARIANT, METADATA$FILENAME
                FROM @RAW_WC2026.RAW.match_events_stage
            )
            FILE_FORMAT = (FORMAT_NAME = 'RAW_WC2026.RAW.json_format')
            ON_ERROR = 'CONTINUE';
        """
    )