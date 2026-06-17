import requests
import json


access_token = 'ZTg5OGQzZDctZWQwOC00NWNmLTgxN2QtODY2MjgxMWRjODRmYzUwZTM0YzctNzA5_P0A1_e234e02d-c093-4e65-9507-c359d0c3963a'  
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params= {'max': '100'}
res = requests.get(url, headers=headers, params=params)
print (res.json ())
