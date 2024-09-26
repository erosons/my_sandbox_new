#https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal#get-started-with-a-service-principal
import msal
import requests
from pprint import pprint
import os
from dotenv import load_dotenv

# the environment variables
load_dotenv()

# Configuration
CLIENT_ID = os.getenv('CLIENT_ID', None)
CLIENT_SECRET = os.getenv('CLIENT_SECRET', None)
TENANT_ID = os.getenv('TENANT_ID', None)
AUTHORITY_URL = f'https://login.microsoftonline.com/{TENANT_ID}'
SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
POWER_BI_API_URL = 'https://api.powerbi.com/v1.0/myorg/'

# MSAL app instance
msal_app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY_URL,
    client_credential=CLIENT_SECRET
)

def get_access_token():
    result = msal_app.acquire_token_for_client(scopes=SCOPE)
    if 'access_token' in result:
        return result['access_token']
    else:
        raise Exception('Failed to acquire access token: ' + result.get('error_description', 'Unknown error'))


def get_datasets(**kwargs):
    try:
        token = get_access_token()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get(f'{POWER_BI_API_URL}groups/{{groupId}}/datasets/{{datasetId}}, headers=headers'.format(groupId=kwargs["groupId"],groupId=kwargs["datasetId"]))
        response.raise_for_status()
        return pprint(response.json(),indent=3)
    except Exception as e:
        return pprint({'error': str(e)}), 500


def get_group_reports(groupId):
    try:
        token = get_access_token()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get(f'{POWER_BI_API_URL}groups/{groupId}/reports', headers=headers)
        response.raise_for_status()
        return pprint(response.json(),indent=3)
    except Exception as e:
        return pprint({'error': str(e)},indent=3), 500

if __name__ == '__main__':
    get_group_reports('58cc3570-0ee5-4aff-b44b-85dab8216c57')
