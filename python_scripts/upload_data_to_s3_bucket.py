import boto3
import os
from botocore.exceptions import NoCredentialsError

def upload_to_s3():
    # AWS credentials are automatically loaded from your environment or ~/.aws/credentials if configured
    s3 = boto3.client('s3')  

    bucket_name = 'my-snowflake-project-bucket0'  
    local_folder = '/opt/airflow/assets/datasets/Transformed_tables' 
    s3_folder = 'transformed_data/'

    try:
        for file_name in os.listdir(local_folder):
            if file_name.endswith('.csv'):
                local_file_path = os.path.join(local_folder, file_name)
                s3_file_path = s3_folder + file_name

                s3.upload_file(local_file_path, bucket_name, s3_file_path)
                print(f"✅ Uploaded {file_name} to {bucket_name}/{s3_file_path}")

    except FileNotFoundError as e:
        print(f"❌ File error: {e}")
    except NoCredentialsError:
        print("❌ AWS credentials not available.")
