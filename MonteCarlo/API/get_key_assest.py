# https://docs.getmontecarlo.com/docs/monte-carlo-api-1
import requests
import json
import pandas as pd
import os

headers:json = {
   'Content-Type: application/json'
   'x-mcd-id':os.getenv(),
   'x-mcd-token':os.getenv()
}

dataraw: json = (
    '{"query":"query getUser {  getUser {    email   firstName    lastName  }}","variables":{}}'
)

with requests.Session() as session:
    session.post(url='url',
                 headers='headers',
                 data=dataraw,
                 verify=False)
