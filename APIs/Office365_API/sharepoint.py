from  sharepoint_helper import SharePoint

file_name = "GL_SES_Full_Detail.xlsx"

# set the foder name
folder = "SES Finance, Acct and Ops"


#get file
file=SharePoint().download_file(file_name,folder)

#save file

with open(file, "wb") as f:
    f.write(file)
    f.close()  