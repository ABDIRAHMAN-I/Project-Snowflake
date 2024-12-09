import pandas as pd

# load a csv file 
df = pd.read_csv('assets/datasets/Transformed_Global_retailer.csv', encoding='latin1')


# split csv based on data model 


# Transactions fact table 
Transactions = df[
    ['TransactionID', 'OrderNumber', 'LineItem', 'OrderDate', 'DeliveryDate', 
     'Quantity', 'CustomerID', 'StoreID', 'ProductID']
]



# Customers dimension table
Customers = df[
    ['CustomerID', 'CustomerGender', 'CustomerName', 'CustomerCity', 
     'CustomerStateCode', 'CustomerState', 'CustomerZip', 
     'CustomerCountry', 'CustomerContinent', 'CustomerDOB']
]

# Products dimension table
products = df[
    ['ProductID', 'ProductName', 'ProductBrand', 'ProductColor', 
     'ProductCost', 'ProductPrice', 'ProductSubcategory', 
     'ProductSubcategoryID', 'ProductCategory', 'ProductCategoryID']
]

# Stores dimension table
stores = df[
    ['StoreID', 'StoreCountry', 'StoreState', 'StoreSqMeters', 'StoreOpenDate']
]

# Save the results to CSV files
Transactions.to_csv('assets/datasets/Transformed_tables/Transactions.csv', index=False)
Customers.to_csv('assets/datasets/Transformed_tables/Customers.csv', index=False)
products.to_csv('assets/datasets/Transformed_tables/products.csv', index=False)
stores.to_csv('assets/datasets/Transformed_tables/stores.csv', index=False)