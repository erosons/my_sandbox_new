import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import (StructField, StructType,
                               ShortType, IntegerType, StringType, FloatType, BooleanType)


if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: mnmcount <file>", file=sys.stderr)
#         sys.exit(-1)

    spark = (SparkSession
        .builder
        .appName("PythonMnMCount")
        .getOrCreate())
   
   # Read from a csn file
    mnm_df = (spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load('/tmp/Sample - Superstore-csv.csv'))
              
    mnm_df.show(n=5, truncate=False)

    # aggregate count of all colors and groupBy state and color
    # orderBy descending order
    mnm_df.select("Customer Name","Segment","Profit","Region").show()

    count_mnm_df = (mnm_df.select("State", "Region", "OrderID")
                    .groupBy("State", "Region")
                    .sum("OrderID")
                    .orderBy("sum(OrderID)", ascending=False))

    # show all the resulting aggregation for all the dates and colors
    count_mnm_df.show(n=60, truncate=False)
    print("Total Rows = %d" % (count_mnm_df.count()))

    # find the aggregate count for California by filtering
    ca_count_mnm_df = (mnm_df.select("*")
                       .where(mnm_df.State == 'Texas')
                       .groupBy("State", "Region")
                       .sum("OrderID")
                       .orderBy("sum(OrderID)", ascending=False))

    # show the resulting aggregation for California
    ca_count_mnm_df.show(n=10, truncate=False)