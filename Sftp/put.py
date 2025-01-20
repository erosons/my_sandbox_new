"""
Setup pip install pysftp
"""
# import required library
import pysftp
# credentials of targeted sftp server
host = 'test.rebex.net'
port = 22
username = 'demo'
password= 'password'
try:
  conn = pysftp.Connection(host=host,port=port,username=username, password=password)
  print("connection established successfully")
except:
  print('failed to establish connection to targeted server')
# file path of local file and targeted location
local_file='tmp.txt'
target_location='/pub/example'
# call conn.put() method to upload file to server
conn.put(local_file, target_location)

#================
# Upload multiple files
#=================

import os
files=os.listdir()
with conn.cd('/testing/'):
    for file in files:
        if file[-4:]=='.txt':
            try:
                conn.put(file)
                print('uploaded file successfully: ',file)
            except:
                print('failed to upload file: ',file)
uploaded file successfully: tmp.txt