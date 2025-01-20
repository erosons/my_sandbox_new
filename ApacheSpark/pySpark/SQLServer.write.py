import pyspark
import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv

#https://learn.microsoft.com/en-us/sql/connect/spark/connector?view=sql-server-ver16

#checks this file for env and if not found checks the system environment
load_dotenv()

server_name = "jdbc:sqlserver://localhost:1433"
database_name = "AdventureWorks"
url = server_name + ";" + "databaseName=" + database_name + ";"

table_name = "Customers"
username = os.getenv('username')
password = "password123!#"  # Please specify password here

spark = SparkSession \
        .builder \
        .appName("myApp") \
        .getOrCreate()


try:
    df=spark.write \
      .format("com.microsoft.sqlserver.jdbc.spark") \
      .mode("overwrite") \
      .option("url", url) \
      .option("dbtable", table_name) \
      .option("user", username) \
      .option("password", password) \
      .save()
except ValueError as error:
    print("Connector write failed", error)

    # Read from SQL Table
df = spark.read \
  .format("com.microsoft.sqlserver.jdbc.spark") \
  .option("url", url) \
  .option("dbtable", "employee") \
  .option("user", "replace_user_name") \
  .option("password", "replace_password") \
  .load()

df = spark.write \
  .format("com.microsoft.sqlserver.jdbc.spark") \
  .mode("overwrite") \
  .option("url", url) \
  .option("dbtable", "employee") \
  .option("user", "replace_user_name") \
  .option("password", "replace_password") \
  .save()


df.show()
