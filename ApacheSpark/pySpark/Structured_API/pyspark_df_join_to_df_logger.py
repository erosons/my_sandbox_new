import pyspark
import pandas as pd
from pyspark.sql import SparkSession


#Create spark session
spark = SparkSession.builder.appName('FirstApp').getOrCreate()

# Access the underlying log4j logging from Spark
log4jLogger = spark._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(__name__)
http_logger = log4jLogger.LogManager.getLogger("org.apache.http")
http_logger.setLevel(log4jLogger.Level.DEBUG)  # Set to DEBUG to capture detailed logs

# Set the log levels
logger.setLevel(log4jLogger.Level.INFO)
# Example usage of logging
logger.info("This is an informational message.")


salesOrder=spark.read.format("csv").\
      option("header",True).\
      option("separator",",").\
      option("inferSchema",True).\
      option("inferSchema",True).\
      load("hdfs:///Bigdata/Superstore.csv")

Salesperson=spark.read.format("csv").\
      option("header",True).\
      option("separator",",").\
      option("inferSchema",True).\
      option("inferSchema",True).\
      load("hdfs:///Bigdata/Salesperson.csv")


DetailedSales=salesOrder.join(Salesperson,"Order ID","left")

DetailedSales.select("Customer Name","Segment","Profit","Returned","Region","Person").show()

#Converting SparK dataFrame to Pandas DataFrame

DetailedSales_pd= DetailedSales.toPandas()


DetailedSales_pd.shape => (9994, 23)



try:
      DetailedSales.write \
      .repartition(1)\
      .format("parquet") \
      .mode("overwrite") \
      .save("hdfs:///Bigdata/enriched_datasets.parquet")
except ValueError as error:
    print("Connector write failed", error)


#OR


try:
      DetailedSales.write \
      .format("parquet") \
      .mode("overwrite") \
      .parquet("hdfs:///Bigdata/enriched_datasets.parquet",compression="snappy",partitionBy="Person")
except ValueError as error:
    print("Connector write failed", error)

testing_loaded_parquet=spark.read.parquet("hdfs:///Bigdata/enriched_datasets.parquet")