import requests
import json
import time

access_token = 'NDgzODNhNTUtZDc0OC00ZjliLTllYzUtMDI5NDJiMmI2NmUwNDA3NDc2OTktNWY1_PE93_b3675da2-e1a0-46f7-b459-a0cc9992935f'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
