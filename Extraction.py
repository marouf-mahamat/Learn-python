import requests

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

# Voir le code html source
print(page.content)

pip install beautifulsoup4 permet de parser



import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
with open("index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')