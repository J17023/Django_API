import requests

endpoint = 'http://localhost:8000/api/products'

get_response = requests.get(endpoint, json = {"name":"hola"})

print(get_response.json())
print(get_response.status_code)

