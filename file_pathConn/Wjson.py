import json
from pathlib import Path

# sample of json data
movies = [{"id": 1, "title": "terminator", "genre": "action", "year": 1989},
          {"id": 2, "title": "LordOftheRings", "genre": "adventure", "year": 1993}
          ]

# how to create a Json data in python
data = json.dumps(movies)
# How to write a path & and how to write json to a path
Path("movies.json").write_text(data)

# how to relate with Json files from any source i.e converting any json file into python  dictionaries
# Most API connection during web scraping return there file in Json format
path = Path("Maindirectory/example_2.json")
print(path.exists())
data = path.read_text()
# Loading json data into a dictionary
Fooditems = json.loads(data)
print(Fooditems)
print(Fooditems["quiz"]["sport"]["q1"]["question"])
print(Fooditems["quiz"]["sport"]["q1"]["options"][3])
