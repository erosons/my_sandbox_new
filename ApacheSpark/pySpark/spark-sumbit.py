import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import (StructField, StructType,
                               ShortType, IntegerType, StringType, FloatType, BooleanType)

spark = SparkSession.builder.appName('FirstApp').getOrCreate()

"""
Cluster master details will provided at command line when we do our spark-submit
"""

try:
    df = spark.read.format("csv").\
        option("header", True).\
        option("separator", ",").\
        option("inferSchema", True).\
        load("hdfs:///Bigdata/Superstore.csv")

   # Creating a SQL-view of the dataFrame
    df.createOrReplaceTempView('SuperStoreData')
    SQL1 = """ SELECT * from SuperStoreData where Segment="Consumer" """
    results = spark.sql(SQL1)

    results.write.\
        mode("overwrite").\
        parquet("hdfs:///Bigdata/refSuperstore2.parquet")

except (ValueError, TypeError) as error:
    print("Connector write failed", error)
