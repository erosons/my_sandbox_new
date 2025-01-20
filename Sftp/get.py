#!/usr/bin/env python

import pysftp
import time

host = '10.2.11.50'
port = 22
username = 'citizix_user'
password= 'str0NgP45sword'

try:
    print("connecting to %s as %s" % (host, username))
    conn = pysftp.Connection(
      host=host,
      port=port,
      username=username,
      password=password,
    )
    print("connection established successfully: ", conn)
except Exception:
  print('failed to establish connection to targeted server')

current_dir = conn.pwd
print('our current working directory is: ', current_dir)

print('available list of directories: ', conn.listdir())

dlfiles = []
with conn.cd('/paymentfiles/09282021/'):
    files = conn.listdir()
    for file in files:
        conn.get(file)
        dlfiles.append(file)
        print(file, ' downloaded successfully ')

print("These files were downloades ", dlfiles)