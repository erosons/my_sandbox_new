import os
import pandas

from google.cloud import bigquery
from google.oauth2 import service_account
import googleapiclient.discovery

""" For this, we use the query method, which inserts a query job into the BigQuery queue.
    These queries are then executed Asynchronously – in the sense that we do not specify any timeout,
    and the client waits for the job to complete. 
    As soon as the job is complete, the method returns a Query_Job instance containing the results.
"""


class BigqueryConnect:
    def __init__(self, project_id):
        self.project_id = project_id
        self.credentials = service_account.Credentials.from_service_account_file(
            # filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
            # scopes=['https://www.googleapis.com/auth/cloud-platform']
            # data-analytics-platform-360222
            "/Users/s.eromonsei/my_sandbox/Engineering/Bigquery/data-analytics-platform-360222-e365fb8e08bb.json"
        )
        self.client = bigquery.Client(
            credentials=self.credentials, project=self.project_id
        )

    def query_Biguery_iter(self, sqlquery):
        """Query Big query and return iterable object."""

        query_job = self.client.query(sqlquery)

        results = query_job.result()  # Wait for the job to complete.

        # The results returns iterable which can be iterated over
        return results

    def query_Biguery_dataframe(self, sqlquery):
        """Lists all service accounts for the current project."""

        df = self.client.query(sqlquery).to_dataframe()

        # Wait for the job to complete.
        # The results returns iter which can be iterated over
        return print(df.head(5))


if __name__ == "__main__":
    sqlquery = """
      SELECT * FROM 
      `data-analytics-platform-360222.EmployeeProfile.Institutions_branch`
      limit 1000;
    """
    bg_object = BigqueryConnect("data-analytics-platform-360222")
    bg_object.query_Biguery_dataframe(sqlquery)
