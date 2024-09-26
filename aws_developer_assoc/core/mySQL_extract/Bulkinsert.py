import pyodbc
import pandas as pd
from core.utils.DbConn import msSQlconn

# Dremio Odbc configuration


def dremioconn():
    host = ''
    port = ''
    uid = ''
    pwd = ''
    driver = 'Odbc or Jdbc Setup'

    cnxn = pyodbc.connect("Driver={};ConnectionType=Direct;HOST={};PORT={};AuthenticationType=Plain;UID={};PWD={}".format(
        driver, host, port, uid, pwd), autocommit=True)

    return cnxn


# ServerSQl 2017 connection
def connects():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=Servername;'
                          'Database=DbName;'
                          'Trusted_Connection=yes;')
    return conn


cursor = msSQlconn().cursor()


sql1fromIngesting = '''SELECT * FROM "table'''

sql2 = "INSERT INTO [AMAL] VALUES (?,?,?,?,?,?)"

"""
Option 1
"""
for chunk in pd.read_sql(sql1fromIngesting, dremioconn(), chunksize=1000000):
    chunk = chunk.to_csv('chunk.csv')
    #conns = engine.raw_connection()
    data = pd.read_csv('chunk.csv', cache_dates=True, sep='\t', delimiter=',')
    qry = "BULK INSERT " + '[dbo].[Weather]' + \
        " FROM '" + 'chunk' + "' WITH (FORMAT = 'CSV')"
    # Execute the query
    success = cursor.execute(qry)
    cursor.commit()
    cursor.close
