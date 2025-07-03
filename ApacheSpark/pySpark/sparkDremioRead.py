from pyspark.sql import SparkSession
import pyspark
import findspark
findspark.init('/Users/samsoneromonsei/spark-3.2.0-bin-hadoop3.2')
spark = SparkSession.builder.appName('DremioCaller').getOrCreate()


server_name = "jdbc:dremio:direct=url:31010"
database_name = "S"
url = server_name + ";" + "databaseName=" + database_name + ";"

table_name = ""
username = ""
# Please specify password here
password = ""

try:

    df = spark.read \
        .format("jdbc") \
        .option("url", url) \
        .option("dbtable", table_name) \
        .option("user", username) \
        .option("password", password) \
        .option("driver", 'com.dremio.jdbc.Driver') \
        .load()
except ValueError as error:
    print("Connector write failed", error)
