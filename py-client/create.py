import requests

headers = {'Authorization': 'Bearer 560a67d9c1720641c68aed06e5cd57885d96ed37'}
endpoint = "http://127.0.0.1:8000/api/products/"
data = {
    "title": "Created by create.py authtoken",
    "price": 99.99
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())