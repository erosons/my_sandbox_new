#See ReadME for installation of the SQL Server command-line tools sqlcmd and bcp on Linux

import pandas as pd
import numpy as np
from bcpandas import SqlCreds, to_sql


class ConnectorAPI:
    def __init__(self,server,db,username,password) ->str:
        self.server=server
        self.db=db
        self.username=username
        self.password=password
    
    def bcpandas(self,df):
       creds = SqlCreds(
       server=self.server,
       database=self.db, 
       username=self.username,
       password=self.password
       )

       return to_sql(df=df, table_name='Testdb', creds=creds, index=False, if_exists='replace')


    def dataFrame(self,filename):
        df = pd.read_csv(str(filename))
        df['ProductName']=df['ProductName'].str.replace(',','')
        #droping Error columns
        df=df.loc[:,~df.columns.str.match("Unnamed: 21")]
        return df



if __name__=="__main__":

    testCase=ConnectorAPI('','','','')
    df=testCase.dataFrame("/home/samson/Downloads/Superstore.csv")
    testCase.bcpandas(df)