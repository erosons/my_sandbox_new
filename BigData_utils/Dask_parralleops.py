## https://brandenpleines.medium.com/apache-airflow-dask-executor-17eea5d26a8b
"urlstring for SQLdatabase :https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls"
# install =>conda install -c conda-forge pyarrow
# pip install pyarrow
# pip install fastparquet
import dask.dataframe as dd
from pathlib import Path
import pyodbc
import pandas as pd
import dask.dataframe as dd
from sqlalchemy import create_engine
import urllib.parse
import boto3



database = ''
server = 'm' 
username = ''
port='1433'
password =urllib.parse.quote_plus("")

#Using URL:dialect+driver://username:password@host:port/database
conn="mssql+pyodbc://{}:{}@{}:{}/{}".format(username,password,server,port,database)
# engine = create_engine('mssql+pyodbc://{}:{}@{}:{}/{}'.format(username,password,server,port,database))

sql="Select * from dbo.CustomerUsage15"
#sql = sql.select([sql.column("1"), sql.column("ID")]).select_from(sql.table("CustomerUsage15"))

# Load the data with Dask instead of Pandas.
                                           
df=dd.read_sql_query(sql, conn=engine, bytes_per_chunk='25 MiB', meta=None)

df=dd.read_sql_table(sql, conn=engine, bytes_per_chunk='25 MiB', meta=None)

filepath=Path(r'C:\Users\samson.eromonsei\Desktop\customer15.csv')
df = dd.read_csv(filepath,blocksize='64MB',dtype={'Account_No': 'object',\
                                                  'BatchId': 'object','LoadDate': 'object','ZipCode': 'float64','REP_Duns': 'object'})  


dest=Path(r'C:\Users\samson.eromonsei\Desktop\customer15\customer15.parquet')
df.to_parquet(dest, engine='auto', compression='snappy', write_index=True,)
