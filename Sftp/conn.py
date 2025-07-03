import pysftp
host = 'test.rebex.net'
port = 22
username = 'demo'
password= 'password'
try:
  conn = pysftp.Connection(host=host,port=port,username=username, password=password)
  print("connection established successfully")
except:
  print('failed to establish connection to targeted server')