terraform {
  required_providers {
    snowflake = {
      source = "Snowflake-Labs/snowflake"
    }
  }
}


resource "snowflake_table" "transactions" {
  database = var.database_name
  schema   = var.schema_name
  name     = "TRANSACTIONS"


  column {
    name = "TRANSACTIONID"
    type = "NUMBER"
  }
  column {
    name = "ORDERNUMBER"
    type = "STRING"
  }
  column {
    name = "LINEITEM"
    type = "NUMBER"
  }
  column {
    name = "ORDERDATE"
    type = "DATE"
  }
  column {
    name = "DELIVERYDATE"
    type = "DATE"
  }
  column {
    name = "QUANTITY"
    type = "NUMBER"
  }
  column {
    name = "CUSTOMERID"
    type = "STRING"
  }
  column {
    name = "STOREID"
    type = "STRING"
  }
  column {
    name = "PRODUCTID"
    type = "STRING"
  }
}




resource "snowflake_table" "customers" {
  database = var.database_name
  schema   = var.schema_name
  name     = "CUSTOMERS"


  column {
    name = "CUSTOMERID"
    type = "STRING"
  }

  column {
    name = "CUSTOMERGENDER"
    type = "STRING"
  }

  column {
    name = "CUSTOMERNAME"
    type = "STRING"
  }

  column {
    name = "CUSTOMERCITY"
    type = "STRING"
  }

  column {
    name = "CUSTOMERSTATECODE"
    type = "STRING"
  }

  column {
    name = "CUSTOMERSTATE"
    type = "STRING"
  }

  column {
    name = "CUSTOMERZIP"
    type = "STRING"
  }

  column {
    name = "CUSTOMERCOUNTRY"
    type = "STRING"
  }

  column {
    name = "CUSTOMERCONTINENT"
    type = "STRING"
  }

  column {
    name = "CUSTOMERDOB"
    type = "DATE"
  }
}


resource "snowflake_table" "products" {
  database = var.database_name
  schema   = var.schema_name
  name     = "PRODUCTS"


  column {
    name = "PRODUCTID"
    type = "STRING"
  }

  column {
    name = "PRODUCTNAME"
    type = "STRING"
  }

  column {
    name = "PRODUCTBRAND"
    type = "STRING"
  }

  column {
    name = "PRODUCTCOLOR"
    type = "STRING"
  }

  column {
    name = "PRODUCTCOST"
    type = "FLOAT"
  }

  column {
    name = "PRODUCTPRICE"
    type = "FLOAT"
  }

  column {
    name = "PRODUCTSUBCATEGORY"
    type = "STRING"
  }

  column {
    name = "PRODUCTSUBCATEGORYID"
    type = "STRING"
  }

  column {
    name = "PRODUCTCATEGORY"
    type = "STRING"
  }

  column {
    name = "PRODUCTCATEGORYID"
    type = "STRING"
  }
}

resource "snowflake_table" "stores" {
  database = var.database_name
  schema   = var.schema_name
  name     = "STORES"



  column {
    name = "STOREID"
    type = "STRING"
  }

  column {
    name = "STORECOUNTRY"
    type = "STRING"
  }

  column {
    name = "STORESTATE"
    type = "STRING"
  }

  column {
    name = "STORESQMETERS"
    type = "FLOAT"
  }

  column {
    name = "STOREOPENDATE"
    type = "DATE"
  }
}