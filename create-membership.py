import requests
import json

access_token = 'ZTg5OGQzZDctZWQwOC00NWNmLTgxN2QtODY2MjgxMWRjODRmYzUwZTM0YzctNzA5_P0A1_e234e02d-c093-4e65-9507-c359d0c3963a'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMzU3ZWIyNTAtNjllYy0xMWYxLTgyNzgtZTMyMjUzMjM5YTkz'
person_email = 'anthonybastidas48@gmail.com'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print (res.json ()) 