from Conf_template.pyspark_core_utils import get_spark_session, file_reader
import tempfile
import os
import logging
import boto3
from botocore.exceptions import ClientError
import requests
from pandas import DataFrame
from datetime import timedelta  as td
from datetime import datetime as dt


BASELINE_FILE: str = "2024-09-27-0.json.gz"
BUCKET_NAME = os.getenv("BUCKET_NAME")

access_keys = os.getenv('aws_access_key_id')
secret_key = os.getenv('aws_secret_access_key')


def download_file(file)-> str:
  
  with requests.Session() as session:
    res = session.get(url=f'https://data.gharchive.org/{file}')
    if res.status_code == 200:
        print('file exist now downloaing')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json.gz') as tmp_file:
            tmp_file.write(res.content)
            return (tmp_file.name,res)  # return the path to the temp file
    else:
        return None


def get_next_file_name(prev_file_name):
        dt_part = prev_file_name.split(".")[0]
        next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%M-%d-%H') + td(hours=1), '%Y-%M-%d-%-H')}.json.gz"
        return next_file



def upload_file(file_name, bucket_name, object_Name) ->None:

    s3_connection = boto3.client(
        "s3", aws_access_key_id=access_keys, aws_secret_access_key=secret_key
    )

    print(f"connection {s3_connection} was succesful")

    try:
        response = s3_connection.upload_file(file_name, bucket_name, object_Name)
    except ClientError as e:
        logging.error(e)
        return print("Failed connection and upload")
    return print("Upload successful")


def main() -> DataFrame:
    spark = get_spark_session("DEV", "Demo_App")

    while True:
        file_name = get_next_file_name(BASELINE_FILE)
        download_res, res = download_file(file_name)
        if res.status_code == 404:
            print(f"Invalid file name or downloads caught up till {file_name}")
         # Load to s3 bucket
        upload_file(download_res,BUCKET_NAME ,file_name)
        df = file_reader(spark, "json", download_res)
        df.createOrReplaceTempView("GhArch_data")

        spark.sql(f"SELECT * FROM GhArch_data LIMIT 10 ").show()
        os.unlink(download_res)

if __name__ == "__main__":
    main()
