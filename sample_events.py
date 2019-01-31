import requests
import json

req = requests.get('https://visittampere.fi:443/api/v1/event?limit=10')

print(dir(req))

# we then print out the http status_code that was returned on making this request
# you should see a successfull '200' code being returned.
print(req.status_code)

with open('data.json', 'w') as f:
  json.dump(req.json(), f)
