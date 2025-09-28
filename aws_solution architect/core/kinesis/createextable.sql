%sql
CREATE EXTERNAL TABLE IF NOT EXISTS main.default.kinesis_demo_bronze2 (
  event_ts TIMESTAMP,
  partitionKey STRING,
  sequenceNumber STRING,
  shardId STRING,
  payload_raw STRING
)
USING DELTA
LOCATION 's3://databricks-workspace-stack-17f0e-bucket/tables/kinesis_demo_bronze1';