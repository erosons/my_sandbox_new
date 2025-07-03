import urllib.request as urllib2
import requests
import json
import pandas as pd


responsecode = {400: "Bad Requsts", 401: "Unauthorized", 404: "Not Found",
                200: "ok,", 302: "Temporary redirect", 500: "Internal server Error", 301: "Permanent Redirect", 503: "Service unavailable"}

url = "https://jsonplaceholder.typicode.com/posts"
res = requests.get(url)
dataextract = []
if res.status_code == 200:
    dump = json.loads(res.content)
    for rows in dump:
        dataextract.append(rows)
    dataextract
else:
    print("Sorry %s" % (responsecode[res.status_code]))

df = pd.DataFrame(dataextract)
print(df.head(5))

filename = "APIextract.csv"

df.to_csv(filename, index=False, sep='|')


"""
Implementation of API extract
"""


req = urllib2.Request("https://jsonplaceholder.typicode.com/posts")
response = urllib2.urlopen(req)

dataextract1 = []
obj = json.loads(response.read())
for rows in obj:
    dataextract1.append(rows)

df = pd.DataFrame(dataextract1)
print(df.head(5))

filename1 = "APIextract1.csv"

df.to_csv(filename1, index=False, sep='|')
