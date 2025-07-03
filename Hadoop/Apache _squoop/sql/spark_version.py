from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Database Import").getOrCreate()

# Read from PostgreSQL
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://[hostname]:[port]/[database_name]") \
    .option("dbtable", "[table_name]") \
    .option("user", "[username]") \
    .option("password", "[password]") \
    .load()

# Write to HDFS in Parquet format, partitioned
df.write.partitionBy("partition_column").parquet("/path/to/output/in/hdfs")
