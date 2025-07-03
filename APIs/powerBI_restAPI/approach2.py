#https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal#get-started-with-a-service-principal
import requests
from pprint import pprint
import os
from dotenv import load_dotenv

# the environment variables
load_dotenv()

 
tenant_id = ''
client_id = ''
client_secret = ''
scope = ['https://analysis.windows.net/powerbi/api/.default']
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
POWER_BI_API_URL = 'https://api.powerbi.com/v1.0/myorg/'

payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials',
    'scope': ' '.join(scope)
}
def get_access_token():
    response = requests.post(token_url, data=payload)
    access_token = response.json().get('access_token')
 
    return access_token


def get_datasets():
    try:
        token = get_access_token()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get(f'{POWER_BI_API_URL}datasets', headers=headers)
        response.raise_for_status()
        return pprint(response.json(),indent=3)
    except Exception as e:
        return pprint({'error': str(e)}), 500
 
def get_reports():
    try:
        token = get_access_token()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get(f'{POWER_BI_API_URL}reports', headers=headers)
        response.raise_for_status()
        return pprint(response.json(),indent=3)
    except Exception as e:
        return pprint({'error': str(e)},indent=3), 500
 
def get_group(groupId):
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
    get_group('58cc3570-0ee5-4aff-b44b-85dab8216c57')