import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Extract all quotes
quotes = soup.find_all("span", class_="text")

for quote in quotes:
    print(quote.text)
    
    
    
    
authors = soup.find_all("small", class_="author")

for author in authors:
    print(author.text)