import requests
import os
from pprint import pprint

class DatabricksBaseAPI:
    DATABRICKS_INSTANCE = os.getenv('databricks_URL')
    TOKEN = os.getenv('PAT')
    HEADERS = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    @classmethod
    def _get(cls, endpoint):
        url = f"{cls.DATABRICKS_INSTANCE}{endpoint}"
        response = requests.get(url, headers=cls.HEADERS)
        response.raise_for_status()
        return response.json()

    @classmethod
    def _post(cls, endpoint, data):
        url = f"{cls.DATABRICKS_INSTANCE}{endpoint}"
        response = requests.post(url, headers=cls.HEADERS, json=data)
        response.raise_for_status()
        return response.json()

    @classmethod
    def _put(cls, endpoint, data):
        url = f"{cls.DATABRICKS_INSTANCE}{endpoint}"
        response = requests.put(url, headers=cls.HEADERS, json=data)
        response.raise_for_status()
        return response.json()

    @classmethod
    def _patch(cls, endpoint, data):
        url = f"{cls.DATABRICKS_INSTANCE}{endpoint}"
        response = requests.patch(url, headers=cls.HEADERS, json=data)
        response.raise_for_status()
        return response.json()

    @classmethod
    def _delete(cls, endpoint):
        url = f"{cls.DATABRICKS_INSTANCE}{endpoint}"
        response = requests.delete(url, headers=cls.HEADERS)
        response.raise_for_status()
        return response.json()


class ClustersAPI(DatabricksBaseAPI):
    @classmethod
    def list_clusters(cls):
        return cls._get("/api/2.0/clusters/list")

    @classmethod
    def create_cluster(cls, cluster_name, spark_version, node_type_id, num_workers):
        data = {
            "cluster_name": cluster_name,
            "spark_version": spark_version,
            "node_type_id": node_type_id,
            "num_workers": num_workers
        }
        return cls._post("/api/2.0/clusters/create", data)

    @classmethod
    def delete_cluster(cls, cluster_id):
        return cls._post(f"/api/2.0/clusters/delete", {"cluster_id": cluster_id})


class MetastoresAPI(DatabricksBaseAPI):
    @classmethod
    def list_metastores(cls):
        return cls._get("/api/2.1/unity-catalog/metastores")

    @classmethod
    def create_metastore(cls, name, storage_root):
        data = {
            "name": name,
            "storage_root": storage_root
        }
        return cls._post("/api/2.1/unity-catalog/metastores", data)

    @classmethod
    def delete_metastore(cls, metastore_id):
        return cls._delete(f"/api/2.1/unity-catalog/metastores/{metastore_id}")


class JobsAPI(DatabricksBaseAPI):
    @classmethod
    def list_jobs(cls):
        return cls._get("/api/2.1/jobs/list")

    @classmethod
    def create_job(cls, job_name, notebook_path):
        data = {
            "name": job_name,
            "notebook_task": {"notebook_path": notebook_path}
        }
        return cls._post("/api/2.1/jobs/create", data)

    @classmethod
    def delete_job(cls, job_id):
        return cls._post("/api/2.1/jobs/delete", {"job_id": job_id})


class DashboardsAPI(DatabricksBaseAPI):
    @classmethod
    def list_dashboards(cls):
        return cls._get("/api/2.0/preview/sql/dashboards")

    @classmethod
    def create_dashboard(cls, name):
        data = {"name": name}
        return cls._post("/api/2.0/preview/sql/dashboards", data)

    @classmethod
    def delete_dashboard(cls, dashboard_id):
        return cls._delete(f"/api/2.0/preview/sql/dashboards/{dashboard_id}")


class WorkspacesAPI(DatabricksBaseAPI):
    @classmethod
    def list_workspace_items(cls, path):
        return cls._get(f"/api/2.0/workspace/list?path={path}")

    @classmethod
    def create_workspace_directory(cls, path):
        data = {"path": path, "overwrite": True}
        return cls._post("/api/2.0/workspace/mkdirs", data)

    @classmethod
    def delete_workspace_item(cls, path, recursive=False):
        return cls._post("/api/2.0/workspace/delete", {"path": path, "recursive": recursive})


class RecipientsAPI(DatabricksBaseAPI):
    @classmethod
    def list_recipients(cls):
        return cls._get("/api/2.1/unity-catalog/recipients")

    @classmethod
    def create_recipient(cls, name, sharing_type):
        data = {
            "name": name,
            "sharing_type": sharing_type
        }
        return cls._post("/api/2.1/unity-catalog/recipients", data)

    @classmethod
    def delete_recipient(cls, recipient_name):
        return cls._delete(f"/api/2.1/unity-catalog/recipients/{recipient_name}")


class ObjectPermissionsAPI(DatabricksBaseAPI):
    @classmethod
    def get_object_permissions(cls, object_id):
        return cls._get(f"/api/2.0/permissions/{object_id}")

    @classmethod
    def set_object_permissions(cls, object_id, permissions):
        data = {"access_control_list": permissions}
        return cls._put(f"/api/2.0/permissions/{object_id}", data)

    @classmethod
    def update_object_permissions(cls, object_id, permissions):
        data = {"access_control_list": permissions}
        return cls._patch(f"/api/2.0/permissions/{object_id}", data)


# Example usage
if __name__ == "__main__":
    # Example: List Clusters
    clusters = ClustersAPI.list_clusters()
    pprint(clusters)

    # # Example: List Metastores
    # metastores = MetastoresAPI.list_metastores()
    # pprint(metastores)

    # # Example: List Jobs
    # jobs = JobsAPI.list_jobs()
    # pprint(jobs)

    # # Example: List Dashboards
    # dashboards = DashboardsAPI.list_dashboards()
    # pprint(dashboards)

    # # Example: List Workspace Items
    # workspace_items = WorkspacesAPI.list_workspace_items("/Users")
    # pprint(workspace_items)

    # # Example: List Recipients
    # recipients = RecipientsAPI.list_recipients()
    # pprint(recipients)

    # # Example: Get Object Permissions
    # object_permissions = ObjectPermissionsAPI.get_object_permissions("object_id_here")
    # pprint(object_permissions)
