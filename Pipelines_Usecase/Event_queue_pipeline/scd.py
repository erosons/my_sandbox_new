# Databricks notebook source
# COMMAND ----------

from pyspark.sql.functions import current_timestamp
from delta.tables import DeltaTable
import sys

# COMMAND ----------
# Widgets to receive parameters from job or notebook run
bucket = dbutils.widgets.get("bucket")
key = dbutils.widgets.get("key")
s3_path = f"s3a://{bucket}/{key}"

# COMMAND ----------
# Read new data
incoming_df = (
    spark.read.format("json").load(s3_path)
    .withColumn("ingest_timestamp", current_timestamp())
)

# COMMAND ----------
# Load existing dimension table
delta_path = "s3a://your-bucket/delta/tables/sensor_dim"
if DeltaTable.isDeltaTable(spark, delta_path):
    delta_table = DeltaTable.forPath(spark, delta_path)

    # Perform SCD Type 1: Overwrite matching records
    delta_table.alias("target").merge(
        incoming_df.alias("source"),
        "target.sensor_id = source.sensor_id"
    ).whenMatchedUpdateAll(
    ).whenNotMatchedInsertAll().execute()
else:
    incoming_df.write.format("delta").save(delta_path)
