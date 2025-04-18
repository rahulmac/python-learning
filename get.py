import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)
print(response.json())


""" 
to pass headers


headers = {
    "Authorization": "Bearer YOUR_API_TOKEN"
}
response = requests.get("https://api.example.com/data", headers=headers) """
