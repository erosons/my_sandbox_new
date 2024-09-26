import json
from office365.runtime.auth.user_credential import UserCredential
from office365.runtime.http.request_options import RequestOptions
from office365.sharepoint.client_context import ClientContext


from dotenv import load_dotenv
import os

# the environment variables
load_dotenv()

username=os.getenv('sharepoint_user')
password=os.getenv('sharepoint_pasword')
share_doc=os.getenv('sharepoint_doc_library')
sharepoint_site_name=os.getenv('sharepoint_site_name')
sharepoint_url=os.getenv('sharepoint_url_site')

site_url = "https://eu001-sp.my360"
ctx = ClientContext(site_url).with_credentials(UserCredential("{}", "{}".format(username,password)))
request = RequestOptions("{0}/_api/web/".format(site_url))
response = ctx.pending_request().execute_request_direct(request)
json = json.loads(response.content)
web_title = json['d']['Title']
print("Web title: {0}".format(web_title))