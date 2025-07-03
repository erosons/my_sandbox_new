import boto3
import json
import requests

DATABRICKS_HOST = 'https://<your-databricks-workspace>'
TOKEN = '<your-databricks-token>'
JOB_ID = '<databricks-job-id>'

def lambda_handler(event, context):
    for record in event['Records']:
        message = json.loads(record['body'])
        bucket = message['bucket']
        key = message['key']

        payload = {
            "job_id": JOB_ID,
            "notebook_params": {
                "bucket": bucket,
                "key": key
            }
        }

        response = requests.post(
            f"{DATABRICKS_HOST}/api/2.1/jobs/run-now",
            headers={"Authorization": f"Bearer {TOKEN}"},
            json=payload
        )

        print(f"Triggered Databricks Job: {response.status_code}")
