# pip install bcp

# Import data:

import bcp

conn = bcp.Connection(host='HOST', driver='mssql',
                      username='USER', password='PASSWORD')
my_bcp = bcp.BCP(conn)
file = bcp.DataFile(file_path='path/to/file.csv', delimiter=',')
my_bcp.load(input_file=file, table='table_name')


# Export data:


conn = bcp.Connection(host='HOST', driver='mssql',
                      username='USER', password='PASSWORD')
my_bcp = bcp.BCP(conn)
file = bcp.DataFile(file_path='path/to/file.csv', delimiter=',')
my_bcp.dump(query='select * from sys.tables', output_file=file)


# Using bcpandas Wrapper

In[1]: import pandas as pd
...: import numpy as np
...:
    ...: from bcpandas import SqlCreds, to_sql, read_sql

In[2]: creds = SqlCreds(
    ...:     'my_server',
    ...:     'my_db',
    ...:     'my_username',
    ...:     'my_password'
    ...: )

In[3]: print(creds.engine)
Out[3]: Engine(mssql+pyodbc: // /?odbc_connect=Driver={ODBC Driver 17 for SQL Server}
               Server=tcp: my_server, 1433
               Database=my_db
               UID=my_username
               PWD=my_password)

In[6]: print(creds2)
Out[6]: SqlCreds(server='my_server', database='my_db', username='my_username', with_krb_auth=False, engine=Engine(mssql+pyodbc: // /?odbc_connect=Driver={ODBC Driver 17 for SQL Server}
                                                                                                                  Server=tcp: my_server, 1433
                                                                                                                  Database=my_db
                                                                                                                  UID=my_username
                                                                                                                  PWD=my_password), password=[REDACTED])

In[3]: df = pd.DataFrame(
    ...:         data=np.ndarray(shape=(10, 6), dtype=int),
    ...:         columns=[f"col_{x}" for x in range(6)]
    ...: )

In[4]: df.shape
Out[4]: (10, 6)

# replce Option=> Writing to SQL table if exist will drop and create the table
# append Option => Writing to SQL table will append to existing table

In[5]: to_sql(df, 'my_test_table', creds,
              index=False, if_exists='replace/append')

In[6]: df2 = read_sql('my_test_table', creds)

In[7]: df2
Out[7]:
    col_0    col_1    col_2    col_3    col_4    col_5
0  4128860  6029375  3801155  5570652  6619251  7536754
1  4849756  7536751  4456552  7143529  7471201  7012467
2  6029433  6881357  6881390  7274595  6553710  3342433
3  6619228  7733358  6029427  6488162  6357104  6553710
4  7536737  7077980  6422633  7536732  7602281  2949221
5  6357104  7012451  6750305  7536741  7340124  7274610
6  7340141  6226036  7274612  7077999  6881387  6029428
7  6619243  6226041  6881378  6553710  7209065  6029415
8  6881378  6553710  7209065  7536743  7274588  6619248
9  6226030  7209065  6619231  6881380  7274612  3014770
