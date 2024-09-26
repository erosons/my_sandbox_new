# pip install azure-storage-file-datalake pyodbc pandas

import pyodbc
import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient
import os


# Set up connection to Azure SQL Database
def get_sql_data(sql_connection_string, query):
    # Create a connection to the Azure SQL Database
    conn = pyodbc.connect(sql_connection_string)
    # Execute the SQL query and load the data into a pandas DataFrame
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# Function to create a DataLakeServiceClient using connection string
def create_datalake_service_client(connection_string):
    return DataLakeServiceClient.from_connection_string(connection_string)


# Upload DataFrame to Azure Data Lake using itertuples
def upload_to_datalake(df, datalake_service_client, filesystem_name, file_path):
    filesystem_client = datalake_service_client.get_file_system_client(
        file_system=filesystem_name
    )
    file_client = filesystem_client.get_file_client(file_path)

    # Create a new file
    file_client.create_file()

    # Convert DataFrame rows to tuples and append to the file
    for row in df.itertuples(index=False, name=None):
        row_data = ",".join(map(str, row)) + "\n"  # Convert tuple to CSV line
        file_client.append_data(row_data.encode(), offset=0, length=len(row_data))

    # Flush the data to make it available in Data Lake
    file_client.flush_data(len(row_data))

    print(f"Data from SQL moved to Data Lake at {file_path}")


# Azure SQL connection string (replace with actual values)
sql_connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=your-sql-server.database.windows.net;DATABASE=your-database;UID=your-username;PWD=your-password"

# SQL query to fetch data
sql_query = "SELECT * FROM your_table"

# Get the data from Azure SQL
df = get_sql_data(sql_connection_string, sql_query)

# Azure Data Lake connection string
datalake_connection_string = os.getenv("AZURE_DATALAKE_CONNECTION_STRING")

# Create Data Lake service client
datalake_service_client = create_datalake_service_client(datalake_connection_string)

# Upload to Data Lake
upload_to_datalake(
    df, datalake_service_client, "your-filesystem", "path/to/output-file.csv"
)
