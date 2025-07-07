# Create Snowflake warehouse for compute resources
module "warehouse" {
 source         = "./modules/warehouse"
 warehouse_name = var.warehouse_name
 warehouse_size = var.warehouse_size
 auto_suspend   = var.auto_suspend
 auto_resume    = var.auto_resume
}

# Create main database container
module "database" {
 source         = "./modules/database"
 database_name  = var.database_name
}

# Create schema within the database
module "schema" {
 source         = "./modules/schema"
 schema_name    = var.schema_name
 database_name  = var.database_name

 depends_on = [
   module.database 
 ]
}

# Create all tables within the schema
module "tables" {
 source         = "./modules/tables"
 database_name  = var.database_name
 schema_name    = var.schema_name

 depends_on = [
   module.database,  
   module.schema     
 ]
}

# Create S3 storage integration for external data access
module "integration" {
 source                    = "./modules/integration"
 s3_snowflake_iam_role_arn = var.s3_snowflake_iam_role_arn
 s3_bucket_url             = var.s3_bucket_url
}

# Create external stage for S3 data loading
module "stage" {
 source                  = "./modules/stage"
 database_name           = var.database_name
 schema_name             = var.schema_name
 s3_bucket_url           = var.s3_bucket_url
 storage_integration_name = "S3_INT" 

 depends_on = [
   module.database,
   module.schema,
   module.integration 
 ]
}