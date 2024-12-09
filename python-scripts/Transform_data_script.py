# Transform data then download transformed copy 


import pandas as pd

# load a csv file 
df = pd.read_csv('assets/datasets/Untransformed_Global_retailer.csv', encoding='latin1')

# print the csv file as a dataframe (table)
print (df) 


# Convert date columns to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'], errors='coerce')  # Coerce errors handle invalid dates
df['CustomerDOB'] = pd.to_datetime(df['CustomerDOB'])
df['StoreOpenDate'] = pd.to_datetime(df['StoreOpenDate'])



# Convert currency to numeric
df['ProductCost'] = pd.to_numeric(df['ProductCost'].replace('[\$,]', '', regex=True))
df['ProductPrice'] = pd.to_numeric(df['ProductPrice'].replace('[\$,]', '', regex=True))


# Normalize text and categorize

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



# Save the transformed DataFrame to a CSV file
output_file = 'assets/datasets/Transformed_Global_retailer.csv'
df.to_csv(output_file, index=False)