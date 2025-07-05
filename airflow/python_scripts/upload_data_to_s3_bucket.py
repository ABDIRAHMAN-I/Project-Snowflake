import boto3
import os
from botocore.exceptions import NoCredentialsError

# AWS credentials are automatically loaded from your environment or ~/.aws/credentials if configured
# Initialize the S3 client
s3 = boto3.client('s3')  


# Parameters
bucket_name = 'my-snowflake-project-bucket0'  
local_folder = 'assets/datasets/Transformed_tables'
s3_folder = 'transformed_data/'

try:
    # Loop through all files in the local folder
    for file_name in os.listdir(local_folder):
        if file_name.endswith('.csv'):  # Only process CSV files
            local_file_path = os.path.join(local_folder, file_name)  # Full path to the local file
            s3_file_path = s3_folder + file_name              

            # Upload each file to S3
            s3.upload_file(local_file_path, bucket_name, s3_file_path)
            print(f"Uploaded {file_name} to {bucket_name}/{s3_file_path}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except NoCredentialsError:
    print("Error: AWS credentials not available.")