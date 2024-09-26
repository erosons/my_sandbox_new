import json
from unittest.mock import patch, MagicMock

# I don't care about the actual open


def json_filemocking():
    p1 = patch("builtins.open", MagicMock())

    m = MagicMock(side_effect=[{
        "Records": [
            {
                "eventVersion": "2.2",
                "eventSource": "aws:s3",
                "awsRegion": "us-west-2",
                "eventTime": "The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, when Amazon S3 finished processing the request",
                "eventName": "event-type",
                "userIdentity": {
                    "principalId": "Amazon-customer-ID-of-the-user-who-caused-the-event"
                },
                "requestParameters": {
                    "sourceIPAddress": "ip-address-where-request-came-from"
                },
                "responseElements": {
                    "x-amz-request-id": "Amazon S3 generated request ID",
                    "x-amz-id-2": "Amazon S3 host that processed the request"
                },
                "s3": {
                    "s3SchemaVersion": "1.0",
                    "configurationId": "ID found in the bucket notification configuration",
                    "bucket": {
                        "name": "lambda-extract",
                        "ownerIdentity": {
                            "principalId": "Amazon-customer-ID-of-the-bucket-owner"
                        },
                        "arn": "bucket-ARN"
                    },
                    "object": {
                        "key": "Dremio Schema.csv",
                        "size": "object-size in bytes",
                        "eTag": "object eTag",
                        "versionId": "object version if bucket is versioning-enabled, otherwise null",
                        "sequencer": "a string representation of a hexadecimal value used to determine event sequence, only used with PUTs and DELETEs"
                    }
                },
                "glacierEventData": {
                    "restoreEventData": {
                        "lifecycleRestorationExpiryTime": "The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, of Restore Expiry",
                        "lifecycleRestoreStorageClass": "Source storage class for restore"
                    }
                }
            }
        ]
    }
    ])
    p2 = patch("json.load", m)

    with p1 as p_open:
        with p2 as p_json_load:
            f = open("m")
            k = json.load(f)
    return k


test = json_filemocking()
