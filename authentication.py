import requests
import json
import time

access_token = 'ZTg5OGQzZDctZWQwOC00NWNmLTgxN2QtODY2MjgxMWRjODRmYzUwZTM0YzctNzA5_P0A1_e234e02d-c093-4e65-9507-c359d0c3963a'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
