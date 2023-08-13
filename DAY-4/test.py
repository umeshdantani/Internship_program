import requests

BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "video/3",{"likes":5100,"name":"umesh","views":10000000})
print(response.json())