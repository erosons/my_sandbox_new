import os
import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import sqlalchemy.dialects
sqlalchemy.dialects.registry.register(
    "dremio", "sqlalchemy_dremio.pyodbc", "DremioDialect_pyodbc"
)

   
def conn_util():
        try:
            host = 'dremio.prod.ep.my360'
            port = '32010'
            uid  = os.getenv("shell_uid")
            pat = os.getenv("pat")
            #driver = '/Library/Dremio/ODBC/lib/libdrillodbc_sbu.dylib'
            # OR
            driver = '/Library/Dremio/ODBC/lib/libarrow-flight-sql-odbc.dylib'
            cert='/Library/Dremio/ODBC/lib/cacerts.pem'
            # OR
            #driver = "{Dremio Connector}" This is providing map in the odbcinst.ini
            cnxn = pyodbc.connect("Driver={};ConnectionType=Direct;HOST={};PORT={};UID={};PWD={};trustedCerts={};useEncryption=1;useSystemTrustStore=0;disableCertificateVerification=1".format(
                driver, host, port, uid, pat,cert), autocommit=True)

            return cnxn
        except:
            print("Check your connection")

print(conn_util())            
#df =pd.read_sql(sql="""SELECT * FROM "Demo NYC Taxi"."Demo Taxi Reflection" limit 10;""", con=conn_util())

 
