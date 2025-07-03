import pyodbc
import pandas as pd
import numpy as np
import urllib.parse
import os
#import sqlalchemy1_dremio.pyodbc
from sqlalchemy import create_engine


def dremio():
   # host = '10.201.3.60'
    host = ''
    port = ''
    database = ''
    uid = ""
    pwd = ''
    #driver = 'Dremio Connector'
    # driver='dremio'
    # Trusted Connection

    #engine = create_engine("mssql+pyodbc://{}:{}@{}:{}/{}?driver=SQL+Server+Native+Client+11.0".format(uid,pwd,host,port,database))
   #  create_engine("mssql+pyodbc://{}/{};Trusted_Connection=True;".format(host,database))
    engine = create_engine(
        'mssql+pyodbc://{}/{}?driver=SQL+Server+Native+Client+11.0'.format(host, database))

    #engine = sa.create_engine('mssql+pyodbc://user:password@server/database')

    #engine = create_engine("mysql+pymysql://some_user:some_pass@some_host/test?charset=utf8mb4")
    conn = engine.connect().execution_options(stream_results=True)
    return conn


sql = """
    SELECT *
    FROM [ESG].[CTG].[GAA_2000_Transaction]

      """

for chunk in pd.read_sql_query(sql=sql, con=dremio(), chunksize=100000):
    print(len(chunk))
