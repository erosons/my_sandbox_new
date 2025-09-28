import boto3, base64, json, time
from datetime import datetime, timezone

REGION = "us-east-1"
STREAM = "samsonacademy-stream"

# Use instance profile/cluster role; or configure profile/keys via cluster
kin = boto3.client("kinesis", region_name=REGION, config=Config(retries={"max_attempts": 10, "mode": "standard"}))

# 1a) Confirm the stream exists and is ACTIVE
info = kin.describe_stream_summary(StreamName=STREAM)["StreamDescriptionSummary"]
print("Status:", info["StreamStatus"], "| Shards:", info["OpenShardCount"])

# 1b) List a shard
shards = kin.list_shards(StreamName=STREAM)["Shards"]
assert shards, "No shards found. Create at least 1 shard."
shard_id = shards[0]["ShardId"]
print("Using Shard:", shard_id)

# 1c) PUT a few test records (so the consumer has something to read)
def put(n=5):
    for i in range(n):
        payload = {
            "deviceId": "Device-001",
            "metric": "Pressure_psig",
            "value": 200.0 + i,
            "ts": datetime.now(timezone.utc).isoformat()
        }
        kin.put_record(
            StreamName=STREAM,
            Data=json.dumps(payload).encode("utf-8"),
            PartitionKey="device-001"
        )
put(5)
print("Wrote 5 test records.")

# 1d) (Optional) Read a couple directly via Kinesis to prove they exist
it = kin.get_shard_iterator(
    StreamName=STREAM,
    ShardId=shard_id,
    ShardIteratorType="TRIM_HORIZON"
)["ShardIterator"]

recs = kin.get_records(ShardIterator=it, Limit=2)
print("Direct-read sample count:", len(recs.get("Records", [])))
if recs.get("Records"):
    for r in recs["Records"]:
        print("Sample:", json.loads(r["Data"]))
