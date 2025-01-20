-- file_format definition in stage which can is resuable
CREATE file format CSVfileformat
    type ='csv',
    FIELD_DELIMITER =','
    SKIP_HEADER =1;

{# Create External stage table from AWS s3 bucket #}
CREATE stage my_stage_s3 
url = 's3://dbtlearn-sam/data/'
credentials = (
AWS_KEY_ID =''
AWS_SECRET_KEY =''
);


{# Create External stage table from azure ADLS gen2 Container #}
--Azure Integration
--On Azure Map RBAC (Container Reader Contributor)
CREATE OR REPLACE STORAGE INTEGRATION azure_int
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = 'AZURE'
ENABLED = TRUE
AZURE_TENANT_ID = 'd0952aa4-b8a4-4e92-8cf5-7a9ec9834007'
STORAGE_ALLOWED_LOCATIONS = ('azure://stgblob001.blob.core.windows.net/inputadata/');



CREATE OR REPLACE STAGE my_azure_stage_int
URL = 'azure://stgblob001.blob.core.windows.net/inputadata/'
STORAGE_INTEGRATION = azure_int
FILE_FORMAT = 'CSVFILEFORMAT';

--On Azure MapRBAC (Storage account Contributor)
CREATE OR REPLACE NOTIFICATION INTEGRATION snowpipe_event
ENABLED = True
TYPE = QUEUE
NOTIFICATION_PROVIDER = AZURE_STORAGE_QUEUE
AZURE_STORAGE_QUEUE_PRIMARY_URI ='https://stgblob001.queue.core.windows.net/snowpipequeue'
AZURE_TENANT_ID = 'd0952aa4-b8a4-4e92-8cf5-7a9ec9834007'


--Snowpipe
CREATE OR REPLACE PIPE emp_pipe_azure
  AUTO_INGEST = TRUE
  INTEGRATION = 'SNOWPIPE_EVENT'
  
AS
  COPY INTO emp_pipe_azure -- Replace with the target table you want to copy data into
  FROM @my_azure_stage_int
  FILE_FORMAT = (TYPE = 'CSV')
  ON_ERROR = 'CONTINUE';



--Working Version with SES
CREATE OR REPLACE STAGE my_azure_stage
  URL='azure://blobcontainer.blob.core.windows.net/inputadata/'
  CREDENTIALS=(AZURE_SAS_TOKEN='?<SAS_token>')
  --ENCRYPTION=(TYPE='AZURE_CSE' MASTER_KEY = 'kPx...')
  FILE_FORMAT = 'CSVfileformat';


{# SETTING UP RBAC FOR snowflake for snowpipe auto - ingestion#}

Steps to Grant Access to Snowflake Integration from Azure Blob Storage

--To get the external ID, you can use the following query in Snowflake:

>>> DESCRIBE STORAGE INTEGRATION my_azure_integration;


AZURE_CONSENT_URL: URL to the Microsoft permissions request page.
AZURE_MULTI_TENANT_APP_NAME

    Name of the Snowflake client application created for your account. In a later step in this section, you will need to grant this application the permissions necessary to obtain an access token on your allowed storage locations.

In a web browser, navigate to the URL in the AZURE_CONSENT_URL column. The page displays a Microsoft permissions request page.

Click the Accept button. This action allows the Azure service principal created for your Snowflake account to be granted an access token on specified resources inside your tenant. Obtaining an access token succeeds only if you grant the service principal the appropriate permissions on the container (see the next step).

The Microsoft permissions request page redirects to the Snowflake corporate site (snowflake.com).

Log into the Microsoft Azure portal.

Navigate to Azure Services » Storage Accounts. Click on the name of the storage account you are granting the Snowflake service principal access to.

Click Access Control (IAM) » Add role assignment.

Select the desired role to grant to the Snowflake service principal:

    Storage Blob Data Reader grants read access only. This allows loading data from files staged in the storage account.

    Storage Blob Data Contributor grants read and write access. This allows loading data from or unloading data to files staged in the storage account. The role also allows executing the REMOVE command to remove files staged in the storage account.

Search for the Snowflake service principal. This is the identity in the AZURE_MULTI_TENANT_APP_NAME property in the DESC STORAGE INTEGRATION output (in Step 1). Search for the string before the underscore in the AZURE_MULTI_TENANT_APP_NAME property.