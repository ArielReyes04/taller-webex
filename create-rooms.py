import requests
import json

access_token = 'NGVhMzc0MmEtODgzZi00Y2I4LWEwMWMtZjc0YjBmNTQ1YzFiZmRjMzg2OWMtODJl_PE93_b3675da2-e1a0-46f7-b459-a0cc9992935f'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params= {'title': 'DevNet Associate Training! '}
res = requests.post(url, headers=headers, json=params)
print (res.json ())