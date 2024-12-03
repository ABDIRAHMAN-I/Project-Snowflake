import pandas as pd



# Load data from CSV
data = pd.read_csv('assets/datasets/Global_retailer_Transactions.csv', encoding='latin1')

# Convert date columns to datetime
data['OrderDate'] = pd.to_datetime(data['OrderDate'])
data['DeliveryDate'] = pd.to_datetime(data['DeliveryDate'], errors='coerce')  # Coerce errors handle invalid dates
data['CustomerDOB'] = pd.to_datetime(data['CustomerDOB'])
data['StoreOpenDate'] = pd.to_datetime(data['StoreOpenDate'])

# Handle missing values
data['DeliveryDate'] = data['DeliveryDate'].fillna(pd.Timestamp('now'))  # Fill missing or NaT values with the current timestamp
# Convert currency to numeric
data['ProductCost'] = pd.to_numeric(data['ProductCost'].replace('[\$,]', '', regex=True))
data['ProductPrice'] = pd.to_numeric(data['ProductPrice'].replace('[\$,]', '', regex=True))


# Normalize text and categorize
data['CustomerName'] = data['CustomerName'].str.title()  # Capitalize first letters
data['CustomerGender'] = data['CustomerGender'].astype('category')  # Convert to category type



# Save the transformed DataFrame to a CSV file
output_file = 'Transformed_Global_retailer_Transactions_2019.csv'
data.to_csv(output_file, index=False)





