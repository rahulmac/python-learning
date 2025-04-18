import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"

response = requests.get(url)

readData = BeautifulSoup(response.text, "html.parser")

quotes = readData.find_all("div", class_="quote")

data = []

for quote in quotes:
    text = quote.find("span", class_="text")
    author = quote.find("small", class_="author")
    tags = [tag.text for tag in quote.find_all("a", class_="tab")]
    data.append({
    'text' : text,
    'author': author,
    'tags': tags
    })
    
    
for q in data:
    print(f"{q['text']} - {q['author']}")    
    print("Tags : ".join(q['tags']))    
    print("-" * 50)