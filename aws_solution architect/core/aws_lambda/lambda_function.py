import json
from download import download_file
from upload import s3_write
from util import get_prev_file_name, get_next_file_name
import os

BASELINE_FILE: str = "2024-09-30-0.json.gz"

file_prefix = os.environ.get("FILE_PREFIX")
bookmark_file = "bookmark"


def lambda_handler(event, context):
    if os.environ.get("ENVIRON") == "DEV":
        os.environ.setdefault("AWS_DEFAULT", "default")
        print(f'Running in {os.environ.get("ENVIRON")}')

    while True:

        prev_file_name = get_prev_file_name(
            os.environ.get("BUCKET_NAME"), file_prefix, bookmark_file, BASELINE_FILE
        )
        print(prev_file_name)
        file_name = get_next_file_name(prev_file_name)
        download_res, res = download_file(file_name)
        if res.status_code == 404:
            print(f"Invalid file name or downloads caught up till {prev_file_name}")
            break

        # Upload .gz files into the bucket
        s3_upload_res = s3_write(
            bucket_name=os.environ.get("BUCKET_NAME"),
            file_name=f"{file_prefix}/{file_name}",
            full_file_path=download_res,
        )
        print(f"File {file_name} successfully processed")

        # Bookmarking last read file
        s3_upload_res = s3_write(
            bucket_name=os.environ.get("BUCKET_NAME"),
            file_name=f"{file_prefix}/{bookmark_file}",
            full_file_path=file_name.encode("utf-8"),
        )
    return {"statusCode": s3_upload_res, "body": json.dumps("Download status code!")}
