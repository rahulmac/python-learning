from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = "https://quotes.toscrape.com"
next_page = "/"
all_quotes = []

while next_page:
    response = requests.get(base_url + next_page)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]
        
        all_quotes.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    # Find the next page link
    next_btn = soup.find("li", class_="next")
    next_page = next_btn.a["href"] if next_btn else None

data = pd.DataFrame(all_quotes)
data.to_csv("practics.csv", index=False)

# ✅ Print all collected quotes
""" 
for q in all_quotes:
    print(f"{q['quote']} — {q['author']}")
    print("Tags:", ", ".join(q['tags']))
    print("-" * 50)
 """
