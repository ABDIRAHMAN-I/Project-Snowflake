import os
import pandas as pd
from datetime import datetime

def split_data():  # Wrap logic in this function
    # Generate timestamp for versioning
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Define input and output folders
    input_dir = 'assets/datasets/Transformed_full'
    output_dir = 'assets/datasets/Transformed_tables'
    os.makedirs(output_dir, exist_ok=True)

    # Get latest transformed CSV from Transformed_full folder
    def get_latest_transformed_csv(directory):
        files = [f for f in os.listdir(directory) if f.startswith('Transformed_Global_retailer') and f.endswith('.csv')]
        files.sort(reverse=True)
        return os.path.join(directory, files[0]) if files else None

    # Get latest transformed file
    latest_transformed_file = get_latest_transformed_csv(input_dir)
    if not latest_transformed_file:
        raise FileNotFoundError("❌ No transformed CSV files found.")

    print(f"📂 Splitting file: {latest_transformed_file}")

    # Load CSV file
    df = pd.read_csv(latest_transformed_file, encoding='latin1')

    # Split into tables
    Transactions = df[
        ['TransactionID', 'OrderNumber', 'LineItem', 'OrderDate', 'DeliveryDate', 
         'Quantity', 'CustomerID', 'StoreID', 'ProductID']
    ]

    Customers = df[
        ['CustomerID', 'CustomerGender', 'CustomerName', 'CustomerCity', 
         'CustomerStateCode', 'CustomerState', 'CustomerZip', 
         'CustomerCountry', 'CustomerContinent', 'CustomerDOB']
    ]

    Products = df[
        ['ProductID', 'ProductName', 'ProductBrand', 'ProductColor', 
         'ProductCost', 'ProductPrice', 'ProductSubcategory', 
         'ProductSubcategoryID', 'ProductCategory', 'ProductCategoryID']
    ]

    Stores = df[
        ['StoreID', 'StoreCountry', 'StoreState', 'StoreSqMeters', 'StoreOpenDate']
    ]

    # Clean the output folder first
    for old_file in os.listdir(output_dir):
        if old_file.endswith('.csv'):
            os.remove(os.path.join(output_dir, old_file))

    # Save to CSV files
    Transactions.to_csv(os.path.join(output_dir, f'Transaction_table_{timestamp}.csv'), index=False)
    Customers.to_csv(os.path.join(output_dir, f'Customers_table_{timestamp}.csv'), index=False)
    Products.to_csv(os.path.join(output_dir, f'Products_table_{timestamp}.csv'), index=False)
    Stores.to_csv(os.path.join(output_dir, f'Stores_table_{timestamp}.csv'), index=False)

    print(f"✅ All tables saved to {output_dir}")
