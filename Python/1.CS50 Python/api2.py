import sys
import json
import requests

## Url of itunes
## this url will fetch 10 song from selected artists
## sys.argv[1] == artist name

url = "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(url)

json_file = response.json()
## looking at the json file
# print(json.dumps(response.json(), indent=2))

for result in json_file["results"]:
    print(result["trackName"])
