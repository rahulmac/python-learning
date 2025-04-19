from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area"


table = pd.read_html(url)

print(table)
