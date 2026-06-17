import requests
import json

access_token = 'NGVhMzc0MmEtODgzZi00Y2I4LWEwMWMtZjc0YjBmNTQ1YzFiZmRjMzg2OWMtODJl_PE93_b3675da2-e1a0-46f7-b459-a0cc9992935f'
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