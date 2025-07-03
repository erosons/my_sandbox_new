
from Config import Config
import pyodbc


def msSQlconn():

    server = Config['ServerName']
    database = Config['dbName']
    username = Config['userNm']
    password = Config['paswd']
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    return cnxn


print(msSQlconn())


