import requests
from bs4 import BeautifulSoup

robots_url = "https://quotes.toscrape.com/"
response = requests.get(robots_url)

readData = BeautifulSoup(response.text, "html.parser")

quotes = readData.find_all("span", class_="text")

world_quotes = [quote.text for quote in quotes if "world" in quote.text.lower()]

print(world_quotes)