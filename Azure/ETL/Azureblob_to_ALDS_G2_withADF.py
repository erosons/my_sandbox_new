# pip install azure-storage-blob azure-storage-file-datalake

from azure.storage.blob import BlobServiceClient
from azure.storage.filedatalake import DataLakeServiceClient
import os
"""
    BlobServiceClient: Used to connect to the Azure Blob Storage, from where we download the blob.
        We use BlobServiceClient.from_connection_string() to initialize the connection.
        get_blob_client() gets the blob object for reading and downloading.

    DataLakeServiceClient: Used to connect to Azure Data Lake Gen2.
        We use DataLakeServiceClient.from_connection_string() to initialize the connection.
        get_file_system_client() connects to the specific filesystem in Data Lake Gen2.
        get_file_client() connects to the target file, where we write the data downloaded from Blob Storage.

    Data Transfer:
        The blob is downloaded using download_blob().readall().
        The content is then uploaded to Data Lake using create_file() and append_data().

    Flush Data: Once the data is written to the Data Lake file, flush_data() finalizes the operation and makes the data available.

Notes:

    Authentication: For simplicity, this script uses connection strings, but you can also use Azure Active Directory (AAD) tokens if you prefer a more secure method.
    Error handling: You can enhance this script by adding proper error handling (e.g., try-except blocks) for resilience in production.
    Data Sizes: This script handles small to medium-sized files. For large data files, consider streaming the data in chunks instead of reading everything into memory.

This script will successfully move data from Azure Blob Storage to Azure Data Lake Gen2. Adjust the connection details and paths as needed for your environment.
"""

# Function to create a BlobServiceClient using connection string
def create_blob_service_client(connection_string):
    return BlobServiceClient.from_connection_string(connection_string)


# Function to create a DataLakeServiceClient using connection string
def create_datalake_service_client(connection_string):
    return DataLakeServiceClient.from_connection_string(connection_string)


# Function to move data from Blob Storage to Data Lake Gen2
def move_blob_to_datalake(
    blob_service_client,
    datalake_service_client,
    container_name,
    blob_name,
    datalake_filesystem,
    destination_path,
):
    # Download blob from Blob Storage
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=blob_name
    )
    downloaded_blob = blob_client.download_blob()

    # Read the content of the blob
    data = downloaded_blob.readall()

    # Upload data to Data Lake Gen2
    filesystem_client = datalake_service_client.get_file_system_client(
        file_system=datalake_filesystem
    )
    file_client = filesystem_client.get_file_client(destination_path)

    # Create a new file and upload the blob content
    file_client.create_file()
    file_client.append_data(data, 0, len(data))  # Appending data to the file
    file_client.flush_data(len(data))  # Finalize the write operation

    print(
        f"Blob '{blob_name}' from container '{container_name}' moved to '{destination_path}' in Data Lake Gen2 filesystem '{datalake_filesystem}'."
    )


# Set up connection details (replace with your actual connection strings)
blob_connection_string = os.getenv("AZURE_BLOB_CONNECTION_STRING")
datalake_connection_string = os.getenv("AZURE_DATALAKE_CONNECTION_STRING")

# Blob storage details
container_name = "your-blob-container-name"
blob_name = "path/to/blob/file.txt"  # Path to the blob file in the container

# Data Lake details
datalake_filesystem = "your-datalake-filesystem"
destination_path = (
    "path/in/datalake/file.txt"  # Path in the Data Lake where the file will be stored
)

# Create clients
blob_service_client = create_blob_service_client(blob_connection_string)
datalake_service_client = create_datalake_service_client(datalake_connection_string)

# Move the blob data to Data Lake Gen2
move_blob_to_datalake(
    blob_service_client,
    datalake_service_client,
    container_name,
    blob_name,
    datalake_filesystem,
    destination_path,
)
