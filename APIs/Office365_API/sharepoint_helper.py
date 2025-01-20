from shareplum import Site, Office365
from shareplum.site import  Version
import os
from dotenv import load_dotenv

# the environment variables
load_dotenv()

username=os.getenv('sharepoint_user')
password=os.getenv('sharepoint_pasword')
share_doc=os.getenv('sharepoint_doc_library')
sharepoint_url=os.getenv('sharepoint_url')
share_site=os.getenv('sharepoint_site')

print(username)

class SharePoint:
    def auth(self):
        self.authcookie = Office365(sharepoint_url, username=username, password=password).GetCookies()
        self.site = Site(share_site,version=Version.v365, authcookie=self.authcookie)

        return self.site
    
    def content_folder(self,folder_name):
        self.auth_site = self.auth()
        self.sharepoint_dir = '\\'.join([share_doc, folder_name])
        self.folder=self.auth_site.Folder(self.sharepoint_dir)

        return self.folder


    def download_file(self,file_name,folder_name):
        self._file =self.content_folder(folder_name)
        return self._file.get_file(file_name)


#sp_list = site.List('list name')
#data = sp_list.GetListItems('All Items', rowlimit=200)