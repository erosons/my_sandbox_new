
import pandas as pd
import requests


def YelpApi(url):

    # Define my endpoints
    # define my Api key
    api_key = ""
    # Alternative connection header = {"Authorization": "Bearer %s" % api_key}
    header = {"Authorization": "Bearer " + api_key}

    # Define the terms of search
    parameters = {'term': 'Coffee',
                  'limit': 50,
                  'radius': 1000,
                  'location': 'Houston'
                  }
    # maing my request to yelp
    response = requests.get(url=url, headers=header, params=parameters)

    # json() convert the returning data into a dictionary
    business_data = response.json()
    #  index into the dictionay and the list as shown below
    print(business_data["businesses"][0])
    businesbreakdown = business_data["businesses"][0]

    # Loop through the dictionary to key the keys
    for key in businesbreakdown.items():  # to return key and values
        print(key)

    return key


"""# to covert to DataFrame for analysis
df = pd.DataFrame.from_dict(businesbreakdown, orient='index')
print(df.transpose()["phone"])"""

"""
#  You can call this from another program as a module as shown below.

urls = "https://api.yelp.com/v3/businesses/search"
print(yelpApi.YelpApi(url))"""
