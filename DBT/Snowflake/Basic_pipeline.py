# Use dbutils secrets to get Snowflake credentials.
user = dbutils.secrets.get("data-warehouse", "<snowflake-user>")
password = dbutils.secrets.get("data-warehouse", "<snowflake-password>")

<<<<<<< HEAD
options = {
  "sfUrl": "<snowflake-url>",
  "sfUser": user,
  "sfPassword": password,
  "sfDatabase": "<snowflake-database>",
  "sfSchema": "<snowflake-schema>",
  "sfWarehouse": "<snowflake-cluster>"
}
# Generate a simple dataset containing five values and write the dataset to Snowflake.
spark.range(5).write \
  .format("snowflake") \
  .options(**options) \
  .option("dbtable", "table_name") \
  .save()
=======
from pyspark.sql import SparkSession

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
    spark.range(5).write \
        .format("snowflake") \
        .options(**options) \
        .option("dbtable", table_name) \
        .save()

    # Read the data back from Snowflake
    display(df)

table_name = "table_name"
write_to_snowflake(options, table_name)

>>>>>>> 10086af96351d91d79ea73a49bfe26ae8db9fa75

# Read the data written by the previous cell back.
df = spark.read \
  .format("snowflake") \
  .options(options) \
  .option("dbtable", "table_name") \
  .load()

display(df)

# Write the data to a Delta table

df.write.format("delta").saveAsTable("sf_ingest_table")