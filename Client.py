import requests


URL = 'http://127.0.0.1:5000/items'
data = {'name': 'NEW DATA'}
item_id = 1

#POST Request
# response = requests.post(URL, json=data)

#PUT Request
# response = requests.put(f'{URL}/{item_id}', json=data)

#DELETE Request
response = requests.delete(f'{URL}/{item_id}')

print('Status Code', response.status_code)
print('Response:', response.json())