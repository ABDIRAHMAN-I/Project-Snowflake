resource "snowflake_warehouse" "warehouse" {
  name           = var.warehouse_name
  warehouse_size = var.warehouse_size
  auto_suspend   = var.auto_suspend
  auto_resume    = var.auto_resume
}


resource "snowflake_database" "main" {
  name = var.database_name
}


resource "snowflake_schema" "main" {
  name     = var.schema_name
  database = snowflake_database.main.name
}


resource "snowflake_table" "transactions" {
  database = var.database_name
  schema   = var.schema_name
  name     = "TRANSACTIONS"


  depends_on = [
    snowflake_database.main,
    snowflake_schema.main
  ]


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


  depends_on = [
    snowflake_database.main,
    snowflake_schema.main
  ]


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


  depends_on = [
    snowflake_database.main,
    snowflake_schema.main
  ]


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


  depends_on = [
    snowflake_database.main,
    snowflake_schema.main
  ]



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





# ---------------------------
# Snowflake Storage Integration
# ---------------------------
resource "snowflake_storage_integration" "s3_integration" {
  name                      = "S3_INT"
  storage_provider          = "S3"
  enabled                   = true
  storage_aws_role_arn      = var.s3_snowflake_iam_role_arn
  storage_allowed_locations = [var.s3_bucket_url]

  comment = "Integration with S3 for external stage access"
}




# -----------------------------------------------------------------------------
# Create a Snowflake Stage that points to your S3 Bucket
# -----------------------------------------------------------------------------
resource "snowflake_stage" "s3_stage" {
  name                = "S3_STAGE"
  database            = snowflake_database.main.name
  schema              = snowflake_schema.main.name
  url                 = "s3://my-snowflake-project-bucket0/transformed_data/"
  storage_integration = snowflake_storage_integration.s3_integration.name
  comment             = "Stage to access S3 transformed data"

  depends_on = [
    snowflake_database.main,
    snowflake_schema.main,
    snowflake_storage_integration.s3_integration
  ]
}


/*
resource "snowflake_file_format" "csv_format" {
  name                = "CSV_FORMAT"
  database            = snowflake_database.main.name
  schema              = snowflake_schema.main.name
  format_type         = "CSV"
  field_delimiter     = ","
  skip_header         = 1
  empty_field_as_null = true
  null_if             = ["NULL", "null"]
}
*/

