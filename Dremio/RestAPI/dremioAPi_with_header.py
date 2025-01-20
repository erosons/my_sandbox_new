https://www.dremio.com/resources/tutorials/using-the-rest-api/

import requests, time

# Authentication

BASE_URL = 'http://localhost:9047'

headers = {
    'Content-Type': 'application/json',
}

data = '{"userName": "dremio","password": "}'

response = requests.post(BASE_URL + '/apiv2/login', headers=headers, data=data, verify=False)

authorization_code = '_dremio' + response.json()['token'] # _dremio is prepended to the token

if response.status_code is 200:
	print ('Successfully authenticated.')
else:
	print('Authentication failed.')

# Create a new data source

auth_header = {
    'Authorization': authorization_code,
    'Content-Type': 'application/json',
}

data = '{"name":"Samples","config":{"credentialType":"NONE","externalBucketList":["samples.dremio.com"],"rootPath":"/","propertyList":[]},"accelerationRefreshPeriod":3600000,"accelerationGracePeriod":10800000,"metadataPolicy":{"deleteUnavailableDatasets":true,"autoPromoteDatasets":false,"namesRefreshMillis":3600000,"datasetDefinitionRefreshAfterMillis":3600000,"datasetDefinitionExpireAfterMillis":10800000,"authTTLMillis":86400000,"updateMode":"PREFETCH_QUERIED"},"accessControlList":{"userControls":[],"groupControls":[]},"type":"S3"}'

response = requests.put(BASE_URL + '/apiv2/source/Samples', headers=auth_header, data=data)

if response.status_code is 200:
	print ('Successfully created the source.')
else:
	print('Source creation failed.')

# Create a space

data = '{"name":"example","accessControlList":{"userControls":[],"groupControls":[]}}'

response = requests.put(BASE_URL + '/apiv2/space/example', headers=auth_header, data=data)

if response.status_code is 200:
	print ('Successfully created the space.')
else:
	print('Space creation failed.')

# Promote a file source to create a PDS

data = '{"type":"JSON"}'

response = requests.put(BASE_URL + '/apiv2/source/Samples/file_format/samples.dremio.com/zips.json', headers=auth_header, data=data)

if response.status_code is 200:
	print ('Successfully created the PDS.')
else:
	print('PDS creation failed.')

# Create a VDS

data = '{\n    "sql": "CREATE VDS zips as SELECT * FROM Samples.\\"samples.dremio.com\\".\\"zips.json\\" LIMIT 4",\n    "context":["example"]\n}'

response = requests.post(BASE_URL + '/api/v3/sql', headers=auth_header, data=data)

time.sleep(3)

# Run a SQL query

data = '{\n    "sql": "SELECT * FROM \\"example\\".\\"zips\\""}'

response = requests.post(BASE_URL + '/api/v3/sql', headers=auth_header, data=data)

job_id = response.json()['id']

if response.status_code is 200:
	print ('Job creation successful. Job id is: ' + job_id)
else:
	print('Job creation failed.')

# Get status of the previous job

print('Waiting for the job to complete...')


job_status = requests.request("GET", BASE_URL + "/api/v3/job/" +job_id, headers=auth_header).json()['jobState']

while job_status != 'COMPLETED':
	time.sleep(1)
	job_status = requests.request("GET", BASE_URL + "/api/v3/job/" +job_id, headers=auth_header).json()['jobState']

print(response.text)

# Get the results from the job

response = requests.request("GET", BASE_URL + "/api/v3/job/"+job_id+"/results", headers=auth_header)

print(response.text)

# Get the dataset ID for subsequent operations

zips_dataset_id = requests.get(BASE_URL + '/api/v3/catalog/by-path/example/zips', headers=auth_header).json()['id']

# Create an aggregate reflection

data = '{"type":"AGGREGATION","name":"Aggregation Reflection","enabled":true,"partitionDistributionStrategy":"CONSOLIDATED","partitionFields":[],"sortFields":[],"dimensionFields":[{"name":"state","granularity":"DATE"}],"measureFields":[{"name":"pop","measureTypeList":["COUNT","SUM"]}],"distributionFields":[],"datasetId":"'+zips_dataset_id+'"}'

response = requests.post(BASE_URL + '/api/v3/reflection/', headers=auth_header, data=data)

reflection_job_id = response.json()['id']

# Check if the reflection job has been completed

print('Waiting for the reflection job to complete...')

while job_status != 'COMPLETED':
	time.sleep(0.2)
	job_status = requests.request("GET", BASE_URL + "/api/v3/job/" +reflection_job_id, headers=auth_header).json()['jobState']

print(response.text)

time.sleep(15) # Wait for the reflection to be available

# Run a BI style query

print ("Running a BI style query with Agg reflection")
data = '{"sql": "SELECT state, SUM(pop) AS population FROM \\"zips\\" GROUP BY state ORDER BY population DESC LIMIT 5","context":["example"]}'

response = requests.post(BASE_URL + '/api/v3/sql', headers=auth_header, data=data)

job_id = response.json()['id']

print('Waiting for the job to complete...')

job_status = requests.request("GET", BASE_URL + "/api/v3/job/" +job_id, headers=auth_header).json()['jobState']

while job_status != 'COMPLETED':
	time.sleep(0.2)
	job_status = requests.request("GET", BASE_URL + "/api/v3/job/" +job_id, headers=auth_header).json()['jobState']

response = requests.request("GET", BASE_URL + "/api/v3/job/"+job_id+"/results", headers=auth_header)

print(response.text) 

# Delete the source
sources = requests.get(BASE_URL + '/api/v3/source/', headers=auth_header).json()  
response = ''

for source in sources['data']:
    if source['name'] == 'Samples':
        response = requests.delete(BASE_URL + '/api/v3/source/'+source['id'], headers=auth_header)
        if response.status_code is 200:
            print ('Datasource deleted successfully.')
        else:
            print('Datasource deletion failed.') 
    
# Delete the space

space  = requests.get(BASE_URL + '/api/v3/catalog/by-path/example', headers=auth_header).json() 
response = requests.delete(BASE_URL + '/api/v3/catalog/' + space['id'] , headers=auth_header) 
if response.status_code is 204:
	print ('Space deleted successfully.')
else:
	print('Space deletion failed.')

