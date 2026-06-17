import requests
import json

access_token = 'ZTg5OGQzZDctZWQwOC00NWNmLTgxN2QtODY2MjgxMWRjODRmYzUwZTM0YzctNzA5_P0A1_e234e02d-c093-4e65-9507-c359d0c3963a'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMzU3ZWIyNTAtNjllYy0xMWYxLTgyNzgtZTMyMjUzMjM5YTkz'
message = 'Hello **DevNet Associates**!!'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print (res.json ())
