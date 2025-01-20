import requests
from bs4 import BeautifulSoup
from lxml import etree
# the url you want to extract from
keywordsearch = input("Enter your search\n")
url = "https://www.epicurious.com/search/"+keywordsearch
response = requests.get(url=url)
# to know if the reponse from the web server is succesful===200
print(response.status_code)
#  to check the returned content and what type of coding chracters if there is need for decoding
# print(response.content)
# ------ use to decode content of the website
# webpagecontent = response.content.decode("utf-8")
#  to find content from a web page is rendered by Class Beautiful calling either  lxml or html5lib
page_soup = BeautifulSoup(response.content, "lxml")
# print(page_soup.prettify())

#  This allows you to find all tags from <div>,<a>,<p> ,The output is a list ResultSet object and you cannot
# drill down with find except by indexing
all_anch_tags = page_soup.find_all('a')
for list_of_anchor in all_anch_tags:
    print(list_of_anchor)

# To digging further in the <a><div> use the method below -this return type element.Tag
just_one_div_tag = page_soup.find("div")
print(just_one_div_tag)
print(type(just_one_div_tag))

#  To print first div inside another another div
div_in_div = just_one_div_tag.find("div")
print(div_in_div)

# To deal with a tag and its attributes note that the attributes is sent as a kwargs
class_finder = page_soup.find_all("article", class_="recipe-content-card")
print(class_finder)

# Similiarly this can be done as dictiinary
class_finder = page_soup.find_all("article", {"class": "recipe-content-card"})
print(class_finder)

# To get the text call with a method get.text() and use find instaed of find all
to_get_text = page_soup.find(
    "article", {"class": "recipe-content-card"}).get_text()
print(to_get_text)

# To get the href from the <a>
class_finder = page_soup.find("article", {"class": "recipe-content-card"})
print(class_finder.find("a"))
sub_anchor_finder = class_finder.find("a")
To_get_link = sub_anchor_finder.get("href")
print("http://www.epicurious.com" + To_get_link)
