import requests
import json


access_token = 'NGVhMzc0MmEtODgzZi00Y2I4LWEwMWMtZjc0YjBmNTQ1YzFiZmRjMzg2OWMtODJl_PE93_b3675da2-e1a0-46f7-b459-a0cc9992935f'  
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params= {'max': '100'}
res = requests.get(url, headers=headers, params=params)
print (res.json ())
