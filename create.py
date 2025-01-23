import requests

endpoint = 'http://localhost:8000/api/products/create/'

post_response = requests.post(endpoint, json = {"name":"hola"})

print(post_response.json())
print(post_response.status_code)

