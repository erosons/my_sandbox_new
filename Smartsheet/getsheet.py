import requests

session=requests.Session()

access_token=''

def smartsheet_api_call(self, action, parameters = {}, method = 'get', data = {}):
        """
        Helper function to make calls to Salesforce REST API.
        Parameters: action (the URL), URL params, method (get, post or patch), data for POST/PATCH.
        """
        headers = {
            'Content-type': 'application/json',
            'Accept-Encoding': 'gzip',
            'Authorization': 'Bearer %s' %access_token
        }
        if method == 'get':
            session.get(headers=headers, params=parameters, timeout=30,verify=False)
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