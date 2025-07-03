import json
import requests
import os
from time import sleep
from io import BytesIO


#username = os.getenv("shell_uid")
username = ""
#password = os.getenv("pat")
password = ""
headers = {'content-type':'application/json'}
#dremioServer = 'http://<server>:9047'

def login(username, password):
  # we login using the old api for now
  loginData = {'userName': username, 'password': password}
  response = requests.post('https://dremio.stage.ep.my360:443/apiv2/login', headers=headers, data=json.dumps(loginData))
  print(response.status_code)
  if response.text:
     data = json.loads(response.text)
  
  # retrieve the login token
  token = data['token']
  return {'content-type':'application/json', 'Authorization':'_dremio{authToken}'.format(authToken=token)}

headers = login(username, password)

def apiGet(endpoint):
  response=requests.get('{server}/api/v3/{endpoint}'.format(server='https://dremio.stage.ep.my360:443', endpoint=endpoint), headers=headers)
  if response.status_code == 200:
        job_metadata=json.loads(response.content)
        print(job_metadata)
        while job_metadata["jobState"]!="COMPLETED":
            sleep(1800)
        result= job_metadata["jobState"]
  else:
              print("Check Connection")
              result= print(f'Reflection check was not successful')
              raise Exception("Sorry, Reflection not found ")
      

  return print(result)

  
def apiPost(endpoint, body=None):
  text = requests.post('{server}/api/v3/{endpoint}'.format(server='https://dremio.stage.ep.my360:443', endpoint=endpoint), headers=headers, data=json.dumps(body)).text
   # a post may return no data
  if (text):
    return json.loads(text)
  else:
    return None
  

def querySQL(query):
    queryResponse = apiPost('sql', body={'sql': query})
    jobid = queryResponse['id']
    return jobid



if __name__=="__main__":
  #apiGet('catalog')
  
  query= """
                DROP TABLE IF EXISTS "s3-cache"."prod-smt-data-cache"."CTAS-query".vwCommissionInvoiceAdvise_test;
         """
  query2="""
            CREATE TABLE "s3-cache"."prod-smt-data-cache"."CTAS-query".vwCommissionInvoiceAdvise_test
                AS
            SELECT * FROM "mp2-excelergy"."Excelergy-test".vwCommissionInvoiceAdvise
          """
  query3="""SELECT 1"""


  jonID_holder={}
  counter=0
  for i in [query, query3]:
    jobid = querySQL(i)
    print(jobid)
    jonID_holder["job"+str(counter)]=jobid
    counter+=1

  # jonID_holder
  apiGet('job/{jonID}'.format(jonID=jonID_holder['job0']))

              