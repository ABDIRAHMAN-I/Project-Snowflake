from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
from datetime import datetime
import os
import snowflake.connector

# Import your actual Python scripts
import sys
sys.path.insert(0, '/opt/airflow/python_scripts')

from transform_data_script import transform_data
from Split_data_into_tables import split_data
from upload_data_to_s3_bucket import upload_to_s3

default_args = {
    'owner': 'abdirahman',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

def load_data_to_snowflake():
    """Load data into Snowflake using SQL script"""
    try:
        # Get connection from Airflow
        conn_info = BaseHook.get_connection('snowflake_default')
        extra = conn_info.extra_dejson
        
        print("Connecting to Snowflake using Airflow connection...")
        conn = snowflake.connector.connect(
            user=conn_info.login,
            password=conn_info.password,
            account=extra.get('account'),
            warehouse=extra.get('warehouse'),
            database=extra.get('database'),
            schema=conn_info.schema,
            role=extra.get('role')
        )

        cursor = conn.cursor()
        
        # Check if SQL file exists
        sql_file_path = '/opt/airflow/dags/sql_scripts/load_data.sql'
        if not os.path.exists(sql_file_path):
            raise FileNotFoundError(f"SQL script not found at: {sql_file_path}")
        
        print(f"Reading SQL file: {sql_file_path}")
        
        # Read and execute SQL script
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        # Better SQL statement splitting
        statements = []
        current_statement = ""
        
        for line in sql_script.split('\n'):
            line = line.strip()
            if line and not line.startswith('--'):  # Skip comments
                current_statement += line + '\n'
                if line.endswith(';'):
                    statements.append(current_statement.strip())
                    current_statement = ""
        
        # Execute each statement
        for stmt in statements:
            if stmt.strip():
                print(f"Executing: {stmt[:100]}...")  # Log first 100 chars
                cursor.execute(stmt)
        
        cursor.close()
        conn.close()
        print("Successfully loaded data into Snowflake")
        
    except Exception as e:
        print(f"Error loading data to Snowflake: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        raise

with DAG(
    dag_id='snowflake_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline with Snowflake and Airflow',
    schedule_interval=None,  
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