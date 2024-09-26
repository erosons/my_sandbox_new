import requests
import pandas as pd
from requests_ntlm2 import HttpNtlmAuth

# pip install ntlm-auth , nltk

username = ""
password = ""
domain = ''  # Can be blank if you are not in a domain
workstation = ''  # Can be blank if you wish to not send this info


auth = HttpNtlmAuth(username, password)
response = requests.get(
    #http://pbiportal/reports/api/v2.0/Reports/'
    'https://api.powerbi.com/v1.0/myorg/reports/', auth=auth)
print(response.json())
df = pd.DataFrame(response.json()["value"])
df.to_csv('Reports.csv', index=False)
data = []
for i in df['Id']:
    response = requests.get(
        'https://api.powerbi.com/v1.0/myorg/reports/' + i + '/Datasources', auth=auth)
    df = pd.DataFrame(response.json()["value"])
    df['ReportID'] = i
    data.append(df)
data
df = pd.concat(data)
df.to_csv('dataSources.csv', index=False)


# Attach the authenticate_message ot your NTLM_NEGOTIATE HTTP header and send to the server. You are now authenticated with NTLMv1
