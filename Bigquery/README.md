JSON  and Query Cost
=====================

The minimum query cost in big query is 10MB
Big query can save file to json array and New line delimte Json
But big query can only take or upload ND json file.


Shell comannds at the terminal
===============================

gcloud config set project <project-name>


#Bigquery Documentation :Interacting Bigquery from Python setup IAM service accounts
https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-list-python
https://googleapis.dev/python/bigquery/latest/reference.html#query
https://cloud.google.com/bigquery/docs/samples/bigquery-query-results-dataframe 
=================================

- step 1
    To install the library, run the following command from your terminal:
    pip install --upgrade google-cloud-bigquery
    pip install --upgrade google-api-python-client
    pip install --upgrade google-auth-httplib2 google-auth-oauthlib
    pip install pandas and db-types

Create a service like a User in AWS 
   - Genrate its credential file under keys using json template -> This is similiar to access keys and access secret in AWS to access resources.