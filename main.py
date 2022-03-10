import json

import requests

data = {
    "email": "a.mosyakin@itdept.cloud",
    "password": "rewq4321"
}

response = requests.post("https://kazino-back-demo.dev2.itdept.cloud/api/v1/auth/login/", data= data)

name = json.loads(response.text)

print(name['user']['email'])