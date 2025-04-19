from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area"


scrap = requests.get(url)

df = BeautifulSoup(scrap.text, "html.parser")

table = df.find("table", class_="wikitable")

data = []
headers = []

for th in table.find_all("th"):
    headers.append(th.text.strip())
    

for row in table.find_all("tr")[1:]:
    cols = row.find_all(["td", "th"])
    if cols:
        data.append([col.text.strip() for col in cols])
        
dataFrame = pd.DataFrame(data, columns=headers)
#print(dataFrame)
dataFrame.to_excel("countries_by_area_bs4.xlsx", index=False)