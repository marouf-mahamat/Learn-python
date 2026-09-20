#Qu’est-ce que l’extraction de données web ?

# Permets de recuperer les donnees sur le web ou extraire des donner sur le web 


url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

# Voir le code html source
print(page.content) 


#parser les donner

# installer le package pip pip install beautifulsoup4 Pour parser le code recuperer depuis le web

import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
with open("index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')



#    Récupération du titre de la page HTML: 
# `soup.title` 
# ==> `<title>Exercice extraction HTML</title>` (un élément HTML) 

# Récupération de la chaîne de caractères du titre HTML 
# `soup.title.string`
# ==> "Exercice extraction HTML" 

# Trouver tous les éléments avec la balise <h2> 
# `soup.find_all('h2')`
# ==> renvoie une liste d'éléments HTML 

# Trouver le premier élément avec l’id `titre`
# `soup.find(id="titre")`
# ==> <h1 id="titre">Bienvenue sur notre site web</h1> 

# Trouver tous les éléments <li>: 
# `soup.find_all("li")` 

# Trouver tous les éléments <li> avec la classe "product" en utilisant un sélecteur CSS: 
# `soup.select("li.product")` 
# ==> renvoie une liste d'éléments HTML


# Pour lire le contenu du fichierindex.html, vous pouvez utiliser le code suivant :
with open("index.html", 'r') as file:
····soup = BeautifulSoup(file, 'html.parser')