import requests

#url="https://jsonplaceholder.typicode.com/users"

url = "https://api.restful-api.dev/objects"

response=requests.get(url=url)
data=response.json()

for i in data:
    if i.get('id') == "4":
        print(f"{i.get('id')} - {i.get('name')} - {i.get('data')}")

data = {
    "id":"99",
    "name":"Karthik",
    "data": {
      "color":"red"
   }
}

response=requests.post(url=url,json=data)
print(f"{response.status_code} - {response.content}")

ur="https://api.restful-api.dev/objects/7"
data = {
    "name":"Apple MacBook Pro 16",
    "data": {
      "color":"red"
   }
}

response=requests.put(url=url,json=data)
print(f"{response.status_code} - {response.content}")

url="https://api.restful-api.dev/objects/1"
response=requests.delete(url)
print(f"{response.status_code} - {response.content}")


# Download image using requests
url="https://static.moviecrow.com/gallery/20250821/250101-madha5.jpeg"
response=requests.get(url=url)

with open("Image1.jpg","wb") as file:
  file.write(response.content)


# Download text file using requests
url="https://getsamplefiles.com/download/txt/sample-1.txt"
response=requests.get(url=url)

with open("Sample.txt","wb") as file:
  file.write(response.content)