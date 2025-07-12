import os
import snowflake.connector
from dotenv import load_dotenv

# Load secrets from .env
load_dotenv()

# Snowflake credentials from .env
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    role=os.getenv("SNOWFLAKE_ROLE"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

# Path to the SQL script
sql_path = "sql_scripts/load_data.sql"

def run_sql_script():
    with conn.cursor() as cur:
        with open(sql_path, 'r') as file:
            sql_commands = file.read().split(';')

            for cmd in sql_commands:
                cmd = cmd.strip()
                if cmd:
                    print(f"\n👉 Running SQL:\n{cmd}")
                    try:
                        cur.execute(cmd)
                    except Exception as e:
                        print(f"❌ Error executing SQL:\n{cmd}")
                        print(str(e))
                        exit(1)

    print("\n✅ All SQL commands executed successfully!")

if __name__ == "__main__":
    run_sql_script()
