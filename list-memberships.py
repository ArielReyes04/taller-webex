import requests
import json


access_token = 'NDgzODNhNTUtZDc0OC00ZjliLTllYzUtMDI5NDJiMmI2NmUwNDA3NDc2OTktNWY1_PE93_b3675da2-e1a0-46f7-b459-a0cc9992935f'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMzU3ZWIyNTAtNjllYy0xMWYxLTgyNzgtZTMyMjUzMjM5YTkz'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'RoomId': room_id}
res = requests.get(url, headers=headers, params=params)
print (res.json ())