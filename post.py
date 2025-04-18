import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "My New Post",
    "body": "This is the content",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())