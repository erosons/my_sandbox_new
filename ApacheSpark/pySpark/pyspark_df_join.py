import pyspark
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import (StructField, StructType,
                               ShortType, IntegerType, StringType, FloatType, BooleanType)

#Create spark session
spark = SparkSession.builder.appName('FirstApp').getOrCreate()


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