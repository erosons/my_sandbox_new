import requests
# the url you want to extract from
url = "https://www.blackhillsenergy.com/services/choice-gas-program/nebraska-choice-gas-customers"
response = requests.get(url=url)
# to know if the reponse from the web server is succesful===200
print(response.status_code)
#  to check the returned content and what type of coding chracters if there is need for decoding
# print(response.content)
#  use to decode content of the website
webpagecontent = response.content.decode("utf-8")
#  to find content from a web page
print(webpagecontent)
