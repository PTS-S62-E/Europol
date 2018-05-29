import json
import urllib

import httplib2

trackerJson = open('trackers.json').read()

data = json.loads(trackerJson)
for carTracker in data:
    jsonStr = carTracker.__str__()
    jsonStr = jsonStr.replace('\'', "\"")
    r, content = httplib2.Http().request("http://localhost:8000/vehicles/", 'POST', jsonStr, {'Content-Type': 'application/json', 'Accept': 'application/json'})
    print(r)
