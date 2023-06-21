import sys
import json
import requests

## Url of itunes
## this url will fetch 1 song from selected artists
## sys.argv[1] == artist name

url = "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(url)

## looking at the json file
print(json.dumps(response.json(), indent=2))
