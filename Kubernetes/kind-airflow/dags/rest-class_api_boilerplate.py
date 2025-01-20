# API -> https://docs.databricks.com/en/reference/jobs-2.0-api.html#job
import requests
import os
from pprint import pprint



class databrick_api:
    DATABRICKS_INSTANCE:str = os.getenv('databricks_URL')
    CLUSTER_ID:str = os.getenv('clusterID')
    user = os.getenv('myuser') 
    _token = os.getenv('PAT')
    headers = {
        "Authorization": f"Bearer {_token}",
        "Content-Type": "application/json"
    }

    @classmethod
    def create_job(cls):
        url = f"{cls.DATABRICKS_INSTANCE}/api/2.1/jobs/create"
        job_data = {
            "name": "My job",
            "new_cluster": {
                "spark_version": "7.3.x-scala2.12",
                "node_type_id": "i3.xlarge",
                "num_workers": 1
            },
            "notebook_task": {
                "notebook_path": f" notebook_path=/Users/{cls.user}/myjob1"
            }
        }
        response = requests.post(url, headers=cls.headers, json=job_data)
        return response.json()

    @classmethod
    def list_jobs(cls):
        url = f"{cls.DATABRICKS_INSTANCE}/api/2.1/jobs/list"
        response = requests.get(url, headers=cls.headers)
        return response.json()

    @classmethod
    def get_job(cls,job_id):
        url = f"{cls.DATABRICKS_INSTANCE}/api/2.1/jobs/get?job_id={job_id}"
        response = requests.get(url, headers=cls.headers)
        return response.json()
    
    @classmethod
    def delete_job(cls,job_id):
        url = f"{cls.DATABRICKS_INSTANCE}/api/2.1/jobs/delete"
        payload = {"job_id": job_id}
        response = requests.post(url, headers=cls.headers, json=payload)
        return response.json()
    
    @classmethod
    def update_job(cls,job_id, new_settings):
        url = f"{cls.DATABRICKS_INSTANCE}/api/2.1/jobs/reset"
        payload = {
            "job_id": job_id,
            "new_settings": new_settings  # Define your new settings dictionary here
        }
        response = requests.post(url, headers=cls.headers, json=payload)
        return response.json()
    
    @classmethod
    def run_now(cls, job_id):
        url = f"{cls.DATABRICKS_INSTANCE}/api/2.1/jobs/run-now"
        payload = {"job_id": job_id}
        response = requests.post(url, headers=cls.headers, json=payload)
        return response.json()

# Example usage with new settings
new_job_settings = {
    "email_notifications": {
        "on_start": ["me@example.com"]
    }
}
# print(update_job(123, new_job_settings))  # Replace 123 with an actual job ID

api_caller=databrick_api()
joblist = api_caller.list_jobs()

pprint(joblist,indent=3)



