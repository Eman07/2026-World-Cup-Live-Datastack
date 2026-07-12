FROM apache/airflow:2.9.3

USER airflow

RUN pip install --no-cache-dir \
    dbt-core==1.7.* \
    dbt-snowflake==1.7.* \
    apache-airflow-providers-snowflake==5.3.0 \
    snowflake-connector-python==3.12.* \
    boto3==1.34.* \
    kafka-python==2.0.2