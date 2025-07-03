import os
import pandas as pd
import tempfile
import zipfile
from airflow.decorators import dag, task
from botocore.exceptions import ClientError
from datetime import datetime, timedelta
import requests


def s3_file_loader(
    filename: str, Bucketname: str, key: str, access_key: str, secret_key: str
):
    import boto3

    s3_con = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1",
    )
    try:
        s3_client = s3_con.client("s3")
        print(s3_client)
        # Open the file and read its content
        file_path = filename
        object_key = key
        print(object_key)
        print("reading file")
        with open(file_path, "rb") as file_data:
            print("Loading file")
            print(file_data)
            s3_client.put_object(Bucket=Bucketname, Key=object_key, Body=file_data)
    except ClientError as e:
        print(e)


def create_session_with_headers():
    """
    Create a requests.Session with specified headers.

    Parameters:
    headers (dict): A dictionary of headers to use for the session.

    Returns:
    requests.Session: A configured session with the provided headers.
    """
    session = requests.Session()
    return session


def get_single_zip(
    session,
    query_name: str,
    start_datetime: datetime,
    end_datetime: datetime,
    version: str,
    result_format: str,
    market_run_id: str,
    node: str,
) -> bytes:
    """
    Get a single zip file from the CAISO OASIS API.
    :param query_name: Name of the query.
    :param start_datetime: Start datetime for the data.
    :param end_datetime: End datetime for the data.
    :param version: API version.
    :param result_format: Format of the result.
    :param market_run_id: Market run ID.
    :param node: Node.
    :return: The contents of the zipped file.
    """

    url = (
        f'http://oasis.caiso.com/oasisapi/SingleZip?queryname={query_name}&startdatetime={start_datetime.strftime("%Y%m%dT%H:%M-%f")}'
        f'&enddatetime={end_datetime.strftime("%Y%m%dT%H:%M-%f")}&version={version}&resultformat={result_format}&market_run_id={market_run_id}&node={node}'
    )

    with session.get(url, stream=True) as r:
        info(r.raise_for_status())
        with tempfile.NamedTemporaryFile(delete=False) as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                temp_filename = f.name

    with zipfile.ZipFile(temp_filename, "r") as z:
        # target = z.filelist[0]  use for context on the zipfile
        for file_name in z.namelist():
            with z.open(file_name) as f:
                data_df = pd.read_csv(f)
                print(data_df.head(5))
                os.remove(temp_filename)
                return data_df


def processes(query_name: str, market_run_id: str, version: str, env: str):
    try:
        start_datetime = datetime.now() - timedelta(days=30)
        end_datetime = datetime.now() - timedelta(days=1)
        start_datetime = start_datetime.replace(hour=7, minute=0, second=0, microsecond=0)
        end_datetime = end_datetime.replace(hour=7, minute=0, second=0, microsecond=0)

        result_format = "6"
        node = (
            ""
        )
        session = create_session_with_headers()
        data = get_single_zip(
            session,
            query_name,
            start_datetime,
            end_datetime,
            version,
            result_format,
            market_run_id,
            node,
        )

        # Naming the attachment using the specified format
        date_str = datetime.now().strftime("%Y%m%d")
        attachment = f"caiso_oasis_prices_{market_run_id}_{date_str}.csv"
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, attachment)
            data.to_csv(file_path)
            if env == "Testing":
                aws_access_key_id = ("",)
                aws_secret_access_key = ("",)
                bucket_name = ""
                key = (
                    f"LMP/{file_path}"
                    """
                Load to dev s3 bucket
                """
                )
            else:
                bucket_name = ""
                key = f"LMP/{file_path}"
                """
                Load prod s3 bucket
                """
    except Exception as e:
        info(f'Something failed in the process query: {e}')
    return info(f'Process was complete and successful')

@dag(
    schedule_interval="50 10 * * *",
    start_date=datetime(2021, 1, 2),
    catchup=False,
    default_args={
        "description": """This dag is used to execute the application abstraction amperon API call to extract about 36 files  from Apempron'
                       Data extracted from this API is used to forecast various customer load based driven b multiple weather conditions""",
        "retries": 3,
        "owner": "Kathleen Ho,Mathew Collom,Ben Carrell",
        "retry_delay": timedelta(minutes=5),
        "on_failure_callback": failure_callback,
    },
    tags=[" Prices ,API"],
)
def dag_decorator():
    prices_dictionary: dict = {
        "dam_lmp_prices": ["", "", "12"],
        "rtm_prices": ["", "", "2"],
    }
    for key, value in prices_dictionary.items():

        @task(task_id=key)
        def lmp_prices(env):
            process_query(value[0], value[1], value[2], env)

    if __name__ == "__main__":
        lmp_prices(env="Testing")


dag = dag_decorator()
