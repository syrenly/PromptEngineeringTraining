# API=application programming interface
# set of rules that allows an application to talk with another

import requests

# GET

response=requests.get("https://api.github.com")
# print(response) # <Response [200]>
# print(response.text) # metadata and response
print(response.status_code)
data=response.json() # turn into json
print(data)

# POST

url="https://dummyjson.com/test"
payload={"name":"Alice","role":"AI Engineer"}
response=requests.post(url,json=payload)
print(response.json)

header={
    "Authorization":"Bearer YOUR_API_KEY",
    "Content_Type": "application/json"
}

if response.status_code==200:
    print("success")
else:
    print("error")
