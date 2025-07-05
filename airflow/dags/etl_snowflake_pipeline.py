from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import snowflake.connector
from dotenv import load_dotenv

# Import your actual Python scripts
import sys
sys.path.insert(0, '/opt/airflow/python_scripts')

from transform_data_script import transform_data
from Split_data_into_tables import split_data
from upload_data_to_s3_bucket import upload_to_s3


# Load environment variables from .env
load_dotenv(dotenv_path='/opt/airflow/.env')

default_args = {
    'owner': 'abdirahman',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

def load_data_to_snowflake():
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA'),
        role=os.getenv('SNOWFLAKE_ROLE')
    )

    cursor = conn.cursor()
    with open('/opt/airflow/dags/sql/load_data.sql', 'r') as file:
        sql_script = file.read()

    for stmt in sql_script.strip().split(';'):
        if stmt.strip():
            cursor.execute(stmt)
    
    cursor.close()
    conn.close()

with DAG(
    dag_id='snowflake_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline with Snowflake and Airflow',
    schedule_interval=None,  # You can change to a cron schedule later
    catchup=False,
) as dag:

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    split_task = PythonOperator(
        task_id='split_into_tables',
        python_callable=split_data
    )

    upload_task = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3
    )

    load_task = PythonOperator(
        task_id='load_into_snowflake',
        python_callable=load_data_to_snowflake
    )

    # Set task dependencies
    transform_task >> split_task >> upload_task >> load_task
