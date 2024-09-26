# requirements.txt
# azure-functions
# pyspark

import logging
import azure.functions as func
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

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

        # Step 3: Load - Write the transformed data to another location (e.g., Azure Data Lake or another Blob container)
        output_path = "https://<your-storage-account>.blob.core.windows.net/output/transformed_data"
        transformed_df.write.mode("overwrite").parquet(output_path)

        logging.info("ETL process completed successfully")

    except Exception as e:
        logging.error(f"Error during ETL: {str(e)}")
        raise

    finally:
        spark.stop()
