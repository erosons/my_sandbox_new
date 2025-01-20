import vaex
import pandas as pd
import sqlalchemy
import pyodbc
import numpy as np
from script import sqlCommand

# connection_string = 'postgresql://readonly:' + 'my_password' + '@server.company.com:1234/database_name'
# engine = sqlalchemy.create_engine(connection_string)

def myconnect():
	server = '' 
	database = 'test' 
	username = 'test' 
	password = '' 
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	return cnxn

# Readind data to pandas dataframe
pandas_df = pd.read_sql_query(sqlCommand, con=myconnect())

# Converting data to Vaex dataFrame
data = vaex.from_pandas(pandas_df, copy_index=False)
data["UTIL_ACCT_START_DT"]=data["UTIL_ACCT_START_DT"].values.astype('datetime64[ns]') # Converting to datetime
 # Extracting year and month extract from data time
data["Start_Year"]=data["UTIL_ACCT_START_DT"].apply(lambda x: x.year)
data["Start_Month"]=data["UTIL_ACCT_START_DT"].apply(lambda x: x.month)
        
# Extracting year and month extract from data time
data["Sales_Year"]=data["SALES_DATE"].apply(lambda x: x.year)
data["Sales_Month"]=data["SALES_DATE"].apply(lambda x: x.month)

data["UTIL_ACCT_END_DT"]=data["UTIL_ACCT_END_DT"].values.astype('datetime64[ns]')
# Extracting year and month extract from data time
data["Stop_Year"]=data["UTIL_ACCT_END_DT"].apply(lambda x: x.year)
data["Stop_Month"]=data["UTIL_ACCT_END_DT"].apply(lambda x: x.month)


# print(data.info()) # This returns the colunms header and their data type
data["Syn_GH"]= np.where(data['SEGMENT']=="RES","RES", "COMM") # performed a ternary operations 
# print(data.columns) # To return alL the headers in the table
        
# This is modify the channel to a more synthetic Channel
#perform an index and match like in excel
conditions=[data["CHANNEL"]=="CES DIRECT SALES",
                    data["CHANNEL"]=="CES DIRECT SALE",
                    data["CHANNEL"]=="COMMERCIAL BROK",
                    data["CHANNEL"]=="COMMERCIAL BROKER",
                    data["CHANNEL"]=="CSR",
                    data["CHANNEL"]=="CUSTOMER SERVICE",
                    data["CHANNEL"]=="DOOR TO DOOR",
                    data["CHANNEL"]=="INTERNAL",
                    data["CHANNEL"]=="INTERNAL SALES",
                    data["CHANNEL"]=="ONLINE BROKER",
                    data["CHANNEL"]=="DELEGATION",
                    data["CHANNEL"]=="OPS",
                    data["CHANNEL"]=="SALESOPS",
                    data["CHANNEL"]=="SEAMLESS MOVE",
                    data["CHANNEL"]=="TELEMARKETING",
                    data["CHANNEL"]=="UTILITY",
                    data["CHANNEL"]=="Web",
                    data["CHANNEL"]=="",
                    data["CHANNEL"]=="CALL CENTER INBOUND",
                    data["CHANNEL"]=="CALL CENTER OUTBOUND"
        ]
choices=["Direct","Direct","Com Broker","Com Broker","CSR","CSR","D2D","Direct","Direct","Online Broker","Delegation","Direct","Direct","Other","OBTS","Other","Web","Other","CALL CENTER INBOUND","CALL CENTER OUTBOUND"]
data["GH_channel"]= np.select(conditions, choices, default='')
print(data.columns)
# executng pivot table for Added no of Customers
Adds_Filter=data["LIFECYCLE_STATUS"].isin(["05 Pending Flow Start","06 Active On Flow"])&(data["Start_Year"]==2020.0)& (data["Start_Month"]==5.0)
Adds_data=data[Adds_Filter]
CustomersAdd=pd.pivot_table(Adds_data, values="CES_LDC_ID",index=["UTILITY"],columns=["Syn_GH"],aggfunc=np.count_nonzero,margins=True,margins_name="Total")
print(CustomersAdd)
