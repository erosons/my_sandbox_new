import os
import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import sqlalchemy.dialects
sqlalchemy.dialects.registry.register(
    "dremio", "sqlalchemy_dremio.pyodbc", "DremioDialect_pyodbc"
)


def get_engine():
    driver = 'Arrow_Flight_SQL_ODBC_DSN'
    #engine = create_engine("""{}://{}:{}@{}:{}/;TrustedCerts={};SSL=1;useSystemTrustStore=false;disableHostVerification=true""".format(driver,uid,pwd,host,port,ssl_key))
    engine = pyodbc.connect("DSN={}".format(driver), autocommit=True)
    return engine
df =pd.read_sql(sql="""SELECT * FROM "Demo NYC Taxi"."Demo Taxi Reflection" limit 10;""", con=get_engine())
print(df)

