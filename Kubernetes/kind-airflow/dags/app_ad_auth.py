import msal
import requests
import os
from pprint import pprint
from dotenv import load_dotenv
from airflow.models import Variable
from datetime import timedelta

from airflow import DAG,task
from airflow.utils.dates import days_ago

# Load environment variables from .env file
load_dotenv()

# Configuration
CLIENT_ID = Variable.get('CLIENT_ID')
CLIENT_SECRET = Variable.get('CLIENT_SECRET')
TENANT_ID = Variable.get('TENANT_ID')
AUTHORITY_URL = f'https://login.microsoftonline.com/{TENANT_ID}'
SCOPE = ['https://management.azure.com/.default']  # Databricks API scope
DATABRICKS_INSTANCE = Variable.get('DATABRICKS_INSTANCE')  # e.g., "https://<your-databricks-workspace>.azuredatabricks.net"

# MSAL app instance
msal_app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY_URL,
    client_credential=CLIENT_SECRET
)

args = {
    "owner": "Samson",
    "start_date": days_ago(1),
    "retries": 1,
    'retry_delay': timedelta(hours=1),
    "owner": "Samson",
    "email": "test@gmail.com"
}


with DAG(
    dag_id="DatabricksAPI",
    schedule_interval=timedelta(1),
    tags=["Mysql_Ingestion"],
    default_args=args,
    catchup=False,
) as dag:

    def get_access_token():
        """
        Get an access token using the Service Principal credentials.
        """
        result = msal_app.acquire_token_for_client(scopes=SCOPE)
        if 'access_token' in result:
            return result['access_token']
        else:
            raise Exception('Failed to acquire access token: ' + result.get('error_description', 'Unknown error'))

    def list_databricks_clusters():
        """
        List clusters in the Databricks workspace.
        """
        token = get_access_token()
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{DATABRICKS_INSTANCE}/api/2.0/clusters/list', headers=headers)
        response.raise_for_status()
        pprint(response.json())

    def create_databricks_cluster(cluster_name, spark_version, node_type_id, num_workers):
        """
        Create a new cluster in the Databricks workspace.
        """
        token = get_access_token()
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        data = {
            "cluster_name": cluster_name,
            "spark_version": spark_version,
            "node_type_id": node_type_id,
            "num_workers": num_workers
        }
        response = requests.post(f'{DATABRICKS_INSTANCE}/api/2.0/clusters/create', headers=headers, json=data)
        response.raise_for_status()
        pprint(response.json())

    def delete_databricks_cluster(cluster_id):
        """
        Delete a specified cluster in the Databricks workspace.
        """
        token = get_access_token()
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        data = {
            "cluster_id": cluster_id
        }
        response = requests.post(f'{DATABRICKS_INSTANCE}/api/2.0/clusters/delete', headers=headers, json=data)
        response.raise_for_status()
        pprint(response.json())

        # List clusters
    @task
    def list_cluster():
           list_databricks_clusters()

    list_cluster()

    # # Create a new cluster (replace with your configuration)
    # create_databricks_cluster(
    #     cluster_name="ExampleCluster",
    #     spark_version="7.3.x-scala2.12",
    #     node_type_id="Standard_DS3_v2",
    #     num_workers=2
    # )


    # # Delete a cluster (replace with a valid cluster ID)
    # delete_databricks_cluster("your-cluster-id")