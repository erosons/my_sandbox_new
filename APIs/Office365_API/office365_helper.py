from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
from dotenv import load_dotenv
import os

# the environment variables
load_dotenv()

username=os.getenv('sharepoint_user')
password=os.getenv('sharepoint_pasword')
share_doc=os.getenv('sharepoint_doc_library')
sharepoint_site_name=os.getenv('sharepoint_site_name')
sharepoint_url=os.getenv('sharepoint_url_site')
#share_site=os.getenv('sharepoint_site')


class SharePoint:
    def auth(self):
        self.conn = ClientContext(sharepoint_url).with_credentials(
              UserCredential(username, 
                             password
              )
        )

        return self.conn
    

    def _get_file_list(self,folder_name):
        conn=self.auth()
        target_folder_url=f'{share_doc}/{folder_name}'
        root_folder=conn.get_folder_by_server_relative_url(target_folder_url)
        root_folder.expand(['Files',"Folders"]).get().execute_query()
        return root_folder.files
    
    def download_file(self,folder_name,file_name):
        conn=self.auth()
        file_url=f'/sites/{sharepoint_site_name}/{share_doc}/{folder_name}/{file_name}'
        file =File.open_binary(conn,file_url)
        return file.content
    