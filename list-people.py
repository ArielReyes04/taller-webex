import requests
import json


access_token = 'NDgzODNhNTUtZDc0OC00ZjliLTllYzUtMDI5NDJiMmI2NmUwNDA3NDc2OTktNWY1_PE93_b3675da2-e1a0-46f7-b459-a0cc9992935f' 
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'anthonybastidas48@gmail.com'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4)) 