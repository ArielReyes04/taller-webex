import requests
import json

access_token = 'NDgzODNhNTUtZDc0OC00ZjliLTllYzUtMDI5NDJiMmI2NmUwNDA3NDc2OTktNWY1_PE93_b3675da2-e1a0-46f7-b459-a0cc9992935f'
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
