Set up Serverless Opertaions with Lambda and S3

Step 1 : Creates your respective s3 buckets for ingestion and extract
Step2: Setup a role and attach a policy giving lambda access to certain reaources , generate your required policies using aws policy generator -> https://awspolicygen.s3.amazonaws.com/policygen.html , You are basically giving a resource access and permission to other resources in aws e.g EC2 -> access to s3, cloudwatch logs.
You can also perform this operations from lambda directly.

Typically if you are giving EC2 access to one resource like RDMS, s3 it is alot easier but to multiple resoucres using policy generator makes sense.

{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "Stmt1640812193626",
"Action": [
"s3:GetObject"
],
"Effect": "Allow",
"Resource": "arn:aws:s3:::lambda-extract"
},
{
"Sid": "Stmt1640812234752",
"Action": [
"s3:PutObject"
],
"Effect": "Allow",
"Resource": "arn:aws:s3:::lambda-ingestion"
},
{
"Sid": "Stmt1640813672748",
"Action": [
"logs:CreateLogGroup",
"logs:CreateLogStream",
"logs:DescribeLogStreams",
"logs:PutLogEvents"
],
"Effect": "Allow",
"Resource": "arn:aws:logs:"":033060477027:log-group:S3-activites:\*"
}
]
}

Step 3: Create your Lambda funcion add IAM role created earlier

Step4 : To go events in s3 properties that will generate the events and setup the event trigger in s3 . The API call is
Event Structure
{  
 "Records":[
 {
 "eventVersion":"2.2",
"eventSource":"aws:s3",
"awsRegion":"us-west-2",
"eventTime":"The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, when Amazon S3 finished processing the request",
"eventName":"event-type",
"userIdentity":{
 "principalId":"Amazon-customer-ID-of-the-user-who-caused-the-event"
},
"requestParameters":{
 "sourceIPAddress":"ip-address-where-request-came-from"
},
"responseElements":{
 "x-amz-request-id":"Amazon S3 generated request ID",
"x-amz-id-2":"Amazon S3 host that processed the request"
},
"s3":{
 "s3SchemaVersion":"1.0",
"configurationId":"ID found in the bucket notification configuration",
"bucket":{
 "name":"bucket-name",
"ownerIdentity":{
 "principalId":"Amazon-customer-ID-of-the-bucket-owner"
},
"arn":"bucket-ARN"
},
"object":{
 "key":"object-key",
"size":"object-size in bytes",
"eTag":"object eTag",
"versionId":"object version if bucket is versioning-enabled, otherwise null",
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

PUT - this is is dealing with when object is uploaded in the S3
