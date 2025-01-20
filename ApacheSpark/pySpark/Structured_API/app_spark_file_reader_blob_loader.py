from Conf_template.pyspark_core_utils import get_spark_session, file_reader
import tempfile
import os
import requests
from pandas import DataFrame
from datetime import timedelta as td
from datetime import datetime as dt


BASELINE_FILE: str = "2024-09-2-0.json.gz"


def download_file(file) -> str:

    with requests.Session() as session:
        res = session.get(url=f"https://data.gharchive.org/{file}")
        if res.status_code == 200:
            print("file exist now downloaing")
            with tempfile.NamedTemporaryFile(
                delete=False, suffix=".json.gz"
            ) as tmp_file:
                tmp_file.write(res.content)
                return (tmp_file.name, res)  # return the path to the temp file
        else:
            return None


def get_next_file_name(prev_file_name):
    dt_part = prev_file_name.split(".")[0]
    next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%M-%d-%H') + td(hours=1), '%Y-%M-%d-%-H')}.json.gz"
    return next_file


def main() -> DataFrame:
    spark = get_spark_session(os.environ.get("ENVIRON"), "Demo_App")

    while True:
        file_name = get_next_file_name(BASELINE_FILE)
        download_res, res = download_file(file_name)
        if res.status_code == 404:
            print(f"Invalid file name or downloads caught up till {file_name}")
        df = file_reader(spark, "json", download_res)
        df.createOrReplaceTempView("GhArch_data")
        save_dataframe_to_blob(df)
        spark.sql(f"SELECT * FROM GhArch_data LIMIT 10 ").show()
        os.unlink(download_res)


# Convert the DataFrame to a CSV string
def save_dataframe_to_blob(
    df: DataFrame
):

    from azure.identity import DefaultAzureCredential
    from azure.storage.blob import BlobServiceClient, ContainerClient
    import pandas as pd
    import tempfile, os

    BLOBCONNECTIONSTRING = os.getenv("BLOBCONNECTIONSTRING ")
    token_credential = DefaultAzureCredential()
    token_credential

    # Create a BlobServiceClient object
    container_service_client = ContainerClient.from_connection_string(
        BLOBCONNECTIONSTRING, container_name="ghactivity"
    )
    print(f"validated container {container_service_client.get_container_properties()}")

    data = [
        {
            "a": 1,
            "b": 1,
        },
        {
            "a": 2,
            "b": 3,
        },
    ]
    df = pd.DataFrame(data)
    # Convert the DataFrame to a CSV string
    with tempfile.TemporaryDirectory() as dir:
        df_data = df.to_parquet(f"{dir}/testing.parquet", index=False)

        blob_name = "test.parquet"
        # Create a blob client and upload the CSV data
        blob_client = container_service_client.get_blob_client(blob_name)
        # Upload the file
        with open(f"{dir}/testing.parquet", "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

    # validation
    # List blobs in the container to verify
    blobs_list = container_service_client.list_blobs()
    for blob in blobs_list:
        print(blob.name)


if __name__ == "__main__":
    main()
