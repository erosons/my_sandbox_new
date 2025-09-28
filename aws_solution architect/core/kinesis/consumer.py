# ---------- Config ----------
kinesisStreamName = "samsonacademy-stream"
kinesisRegion     = "us-east-1"
bronzeTable       = "main.default.kinesis_demo_bronze"
bronzeCheckpoint  = "s3://databricks-workspace-stack-17f0e-bucket/checkpoints/kinesis_demo_bronze1"

# ---------- Source (Kinesis) ----------
kinesisDF = (spark.readStream
    .format("kinesis")
    .option("streamName", kinesisStreamName)
    .option("region", kinesisRegion)
    # TRIM_HORIZON = from oldest; LATEST = only new events
    .option("initialPosition", "TRIM_HORIZON")
    .load()
)

# ---------- Stream to Delta (managed UC table) ----------
bronzeQuery = (kinesisDF.writeStream
    .format("delta")
    .option("checkpointLocation", bronzeCheckpoint)
    .option("mergeSchema", "true")     # allow schema evolution
    .outputMode("append")
    .queryName("kinesis_to_bronze")
    .toTable(bronzeTable)              # start query and manage UC table
)

# ---------- Optional: tee to console for quick debugging ----------
consoleQuery = (kinesisDF.writeStream
    .format("console")
    .outputMode("append")
    .option("truncate", "false")
    .queryName("kinesis_to_console")
    .start()
)

# ---------- Keep the notebook alive ----------
bronzeQuery.awaitTermination()