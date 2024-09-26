# requirements.txt
# azure-functions
# pyspark

import logging
import azure.functions as func
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql import functions as F

def main(myblob: func.InputStream):
    logging.info(f"Processing blob: {myblob.name}, Size: {myblob.length} bytes")

    # Initialize PySpark session
    spark = SparkSession.builder \
        .appName("AzureBlobTriggeredETL") \
        .getOrCreate()

    try:
        # Step 1: Extract - Read the uploaded file from blob (assuming it's a CSV)
        input_path = f"https://<your-storage-account>.blob.core.windows.net/{myblob.name}"
        df = spark.read.csv(input_path, header=True, inferSchema=True)

        # Step 2: Transform - Perform some data transformations (example: filtering, aggregations)
        transformed_df = df.filter(col("status") == "active")

        # Dynamic Partitioning based on columns (e.g., date, region, etc.)
        # Here we partition the data by "region" and "status"
        partitioned_df = transformed_df \
            .withColumn("year", F.year(F.col("event_date"))) \
            .withColumn("month", F.month(F.col("event_date"))) \
            .withColumn("day", F.dayofmonth(F.col("event_date")))

        # Step 3: Repartition (reshuffle) the data to optimize for performance
        # In this case, we're repartitioning by region to ensure better distribution across nodes
        reshuffled_df = partitioned_df.repartition(10, "region")

        # Step 4: Load - Write the partitioned and reshuffled data to another location
        output_path = "https://<your-storage-account>.blob.core.windows.net/output/transformed_data"
        
        # Write the data to partitioned directories (e.g., by year, month, region)
        reshuffled_df.write \
            .mode("overwrite") \
            .partitionBy("year", "month", "region") \
            .parquet(output_path)

        logging.info("ETL process completed successfully with dynamic partitioning and reshuffle")

    except Exception as e:
        logging.error(f"Error during ETL: {str(e)}")
        raise

    finally:
        spark.stop()
