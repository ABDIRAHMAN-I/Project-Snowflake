# created template for creating infrastructure for database and schema

provider "snowflake" {
  account  = "your_account_name"
  username = "your_username"
  password = "your_password"
}

resource "snowflake_database" "demo" {
  name = "DEMO_DB"
  comment = "This is a demo database"
}
