import requests

robots_url = "https://quotes.toscrape.com/robots.txt"
res = requests.get(robots_url)
print(res.text)