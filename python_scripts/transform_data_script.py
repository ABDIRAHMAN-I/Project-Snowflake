import os
import pandas as pd
from datetime import datetime

def transform_data():
    # Function to get the latest raw CSV from the Original_file directory
    def get_latest_raw_csv(directory):
        files = [f for f in os.listdir(directory) if f.endswith('.csv')]
        files.sort(reverse=True)
        return os.path.join(directory, files[0]) if files else None

    # Define input and output directories (use absolute path for Airflow)
    input_dir = '/opt/airflow/assets/datasets/Original_file'
    output_dir = '/opt/airflow/assets/datasets/Transformed_full'

    # Get the most recent file
    latest_file = get_latest_raw_csv(input_dir)
    if not latest_file:
        raise FileNotFoundError("❌ No raw CSV files found in Original_file folder.")

    # load a csv file
    df = pd.read_csv(latest_file, encoding='latin1')

    # print the csv file as a dataframe (table)
    print(df)

    # Convert date columns to datetime
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    df['CustomerDOB'] = pd.to_datetime(df['CustomerDOB'])
    df['StoreOpenDate'] = pd.to_datetime(df['StoreOpenDate'])

    # Convert currency to numeric
    df['ProductCost'] = pd.to_numeric(df['ProductCost'].replace(r'[\$,]', '', regex=True))
    df['ProductPrice'] = pd.to_numeric(df['ProductPrice'].replace(r'[\$,]', '', regex=True))

    # Capitalize first letters
    df['CustomerName'] = df['CustomerName'].str.title()

    # Convert to category type
    df['CustomerGender'] = df['CustomerGender'].astype('category')

    # Check specific columns
    print(df[['OrderDate', 'CustomerDOB', 'StoreOpenDate']])

    # Check numeric conversions
    print(df[['ProductCost', 'ProductPrice']])

    # Check normalized text and categories
    print(df[['CustomerName', 'CustomerGender']])

    # Ensure output directory exists (add this line before saving the CSV)
    os.makedirs(output_dir, exist_ok=True)

    # Save the transformed DataFrame to a CSV file (timestamped)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'Transformed_Global_retailer_{timestamp}.csv'
    output_path = os.path.join(output_dir, output_file)
    df.to_csv(output_path, index=False)

    print(f"✅ Transformed CSV saved to: {output_path}")



