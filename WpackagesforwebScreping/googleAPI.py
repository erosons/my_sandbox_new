import json
import requests

address = "Houston Community College,Texas"
url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s" % (
    address)
print(url)
try:
    reponse = requests.get(url=url)
    # using ternary operator
    message = "Good connection"if reponse.status_code == 200 else "check to code "
    print(message)
    try:
        reponse_data = reponse.json()

    except:
        print("data dump not a json format")

except:
    print("chk you request.get")
print(reponse_data)
