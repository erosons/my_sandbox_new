import json
import requests
import os


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
          with open('/Users/s.eromonsei/stageGitHub/my_sandbox/Engineering/Dremio/jsonfileTestcase.json', 'w') as fp:
            json.dump(response.json(),fp,indent=4)
          result="Ops successfully"  
          fp.close()           

  else:
              print("Check Connection")
              result= print(f'Reflection check was not successful')
              raise Exception("Sorry, Reflection not found ")
      

  return result



if __name__=="__main__":
  apiGet('catalog')