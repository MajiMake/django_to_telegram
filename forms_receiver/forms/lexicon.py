import requests

responce = requests.post('http://127.0.0.1:8000/request/', json={ "name": "Maga", "queues": "14" },)

print(responce.text)