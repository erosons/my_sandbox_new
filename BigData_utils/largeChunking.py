
"urlstring for SQLdatabase :https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls"
# install =>conda install -c conda-forge pyarrow
# pip install pyarrow
# pip install fastparquet
import dask.dataframe as dd
from pathlib import Path
import pyodbc
import logging
import pandas as pd
#from sqlalchemy import create_engine
#import urllib.parse
import boto3
from botocore.exceptions import ClientError
import os

logging.basicConfig(filename='new.log', level=logging.DEBUG,
                    format='(name)s:%(asctime)s:%(levelname)s:%(message)s')

s3_connection = boto3.client('s3', aws_access_key_id="L",
                             aws_secret_access_key="")


def connect():
    server = ''
    database = ''
    username = ''
    port = ''
    # password =urllib.parse.quote_plus("")
    password = ""

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    print("connection {} was successful".format(cnxn))
    return cnxn


def filechunking():
    # Using URL:dialect+driver://username:password@host:port/database

    sql = ""
    #sql = sql.select([sql.column("1"), sql.column("ID")]).select_from(sql.table("CustomerUsage15"))

    # Load the data with Dask instead of Pandas.

    # Using URL:dialect+driver://username:password@host:port/database
    # SQLALhemyconn="mssql+pyodbc://{}:{}@{}:{}/{}".format(username,password,server,port,database)
    # engine = create_engine('mssql+pyodbc://{}:{}@{}:{}/{}'.format(username,password,server,port,database))
    count = 0
    for chunk in pd.read_sql(sql, connect(), index_col=None, chunksize=5000):
        try:
            #logging.DEBUG("Memory analysis{}".format(chunk.memory_usage(deep=True)))
            count += 1
            data = "data" + str(count)
            dest = Path(
                r'C:\Users\location\Desktop\customer15\{}.parquet'.format(data))
            object_Name = os.path.basename(dest)
            bucket_name = 'prod-smt-data-cache'
            chunk.to_parquet(dest, engine='auto', compression='snappy')
            s3_connection.upload_file(str(dest), bucket_name, object_Name)
            print("upload was successful")
            os.remove(str(dest))
            print("File removed succesfully", count)
        except ClientError as e:
            logging.error(e)
            print("Failed connection and uploaded")


if __name__ == "__main__":
    filechunking()
