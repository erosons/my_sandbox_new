import requests

def download_file(file)-> str:
  
  with requests.Session() as session:
    res = session.get(url=f'https://data.gharchive.org/{file}')
    return (res.content,res,)