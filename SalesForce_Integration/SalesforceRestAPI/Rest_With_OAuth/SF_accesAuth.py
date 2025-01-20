import requests
#import pip._vendor.requests 
import os
# import urllib3.contrib.pyopenssl

class salesforcedAuth:
    def __init__(self) -> None:
       self.params = {
        "grant_type": "password",
        "client_id": os.getenv("SFconsumerKey"), # Consumer Key
        "client_secret":  os.getenv("SFconsumerSecret"), # Consumer Secret
        "username": os.getenv("myemail"), # The email you use to login
        "password": os.getenv("SFpaswword") # Concat your password and your security token
        }
       self.r = requests.post("https://login.salesforce.com/services/oauth2/token", params=self.params,verify=False)
       # if you connect to a Sandbox, use test.salesforce.com instead
       self.access_token = self.r.json().get("access_token")
       self.instance_url = self.r.json().get("instance_url")
        # print(os.getenv("SFpaswword"))
        #print("Access Token:", self.access_token)
        # print("Instance URL", instance_url)



    def sf_api_call(self, action, parameters = {}, method = 'get', data = {}):
        """
        Helper function to make calls to Salesforce REST API.
        Parameters: action (the URL), URL params, method (get, post or patch), data for POST/PATCH.
        """
        headers = {
            'Content-type': 'application/json',
            'Accept-Encoding': 'gzip',
            'Authorization': 'Bearer %s' % self.access_token
        }
        if method == 'get':
            r =requests.request(method, self.instance_url+action, headers=headers, params=parameters, timeout=30,verify=False)
        elif method in ['post', 'patch']:
            r = requests.request(method, self.instance_url+action, headers=headers, json=data, params=parameters, timeout=10,verify=False)
        else:
            # other methods not implemented in this example
            raise ValueError('Method should be get or post or patch.')
        print('Debug: API %s call: %s' % (method, r.url) )
        if r.status_code < 300:
            if method=='patch':
                return None
            else:
                return r.json()
        else:
            raise Exception('API error when calling %s : %s' % (r.url, r.content))