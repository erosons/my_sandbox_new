# Use dbutils secrets to get Snowflake credentials.
from pyspark.sql import SparkSession

user = dbutils.secrets.get("data-warehouse", "<snowflake-user>")
password = dbutils.secrets.get("data-warehouse", "<snowflake-password>")

# Example usage
options = {
        "sfURL": "https://my_snowflake_account.snowflakecomputing.com",
        "sfUser": "my_user",
        "sfPassword": "my_password",
        "sfDatabase": "my_database",
        "sfSchema": "my_schema",
        "sfWarehouse": "my_warehouse"
    }

def write_to_snowflake(options, table_name):
    # Initialize Spark session (assuming Spark is already set up)
    spark = SparkSession.builder.appName("SnowflakeWriter").getOrCreate()

    
    # Build and execute the nested function
    df = spark.range(5).write \
        .format("snowflake") \
        .options(**options) \
        .option("dbtable", table_name) \
        .save()

    # Read the data back from Snowflake
    (df)

table_name = "table_name"
write_to_snowflake(options, table_name)


# Read the data written by the previous cell back.
df = spark.read \
  .format("snowflake") \
  .options(options) \
  .option("dbtable", "table_name") \
  .load()

display(df)

# Write the data to a Delta table

df.write.format("delta").saveAsTable("sf_ingest_table")