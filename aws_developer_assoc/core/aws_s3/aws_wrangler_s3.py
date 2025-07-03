import os
import awswrangler as wr
from boto3.session import Session
import boto3
import logging


class awsWrangler:
    def __init__(self) -> None:
        self.aws_access_key_id = os.environ.get("aws_access_key_id")
        self.aws_secret_access_key = os.environ.get("aws_secret_access_key")
        self.region_name = "us-east-2"
        self.profile_name = None
        self.logger.INFO = logging.basicConfig(
            filename='new.log', filemode='w', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
        boto3.setup_default_session(profile_name="Samson")
        # self.Session=Session(aws_access_key_id=self.aws_access_key_id,aws_secret_access_key=self.aws_secret_access_key,region_name=self.region_name,profile_name=self.profile_name)

    def bulkS3read_csv(self, bucketName, log=True):
        """
        BuckeyName : the is the s3 buckets
        """
        try:
            if log is True:
                self.logger.INFO(f"Querying S3 Bucket Objects: {bucketName}")
                # return wr.s3.read_csv(path=bucketName,boto3_session=self.Session)
                return wr.s3.read_csv(path=bucketName)
        except:
            return self.logger.INFO(f"Check credentials are properly captured")

    def writeS3_csv(self, df, bucketName, log=True):
        try:
            if log is True:
                self.logger.INFO(f"Wrting S3 Bucket Objects: {bucketName}")
                # wr.s3.to_csv(df=df,path=bucketName,index=False,boto3_session=self.Session)
                # ,boto3_session=self.Session)
                return wr.s3.to_csv(df=df, path=bucketName, index=False)
        except:
            return self.logger.INFO(f"Check credentials are properly captured")

    def writeS3_to_parquet(self, df, bucketName, log=True):
        try:
            if log is True:
                self.logger.INFO(
                    f"The object does not exists {wr.s3.does_object_exist(bucketName)}")
                self.logger.INFO(f"Wrting to S3 Bucket Objects")
                # boto3_session=self.Session,
                wr.s3.to_parquet(df=df, path=bucketName, mode="overwrite")
                self.logger.INFO(
                    f" The objects exists {wr.s3.does_object_exist(bucketName)}")
                return self.logger.INFO(f"The object is now present in the bucket")
        except:
            self.logger.INFO(f"Check credentials are properly captured")
