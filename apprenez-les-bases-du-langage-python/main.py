from bs4 import BeautifulSoup



# 1/ Récupérez les éléments suivants dans le code html et stockez-les dans des variables, puis affichez-les dans la console :

# le titre de la page (<title> )

# le texte de la balise <h1> avec ID "titre"

# les informations sur les produits :

# nom du produits

# prix du produit (par exemple: 20€)

# description

# utilisez un dictionnaire pour stocker ces informations pour tous les produits.

# 2/ Nettoyez les prix des produits pour ne garder qu'un nombre (retirez le motprix, et:). Vous pouvez utiliser la fonction Pythonsplit.

# 3/ Convertissez les prix en euro vers le dollar (considérez que le prixdollar = euro * 1.2).

# 4/ Affichez les produits avec le prix en dollars (par exemple: 20$).

#Syntaxe
# with expression as variable:
#     # bloc de code (indenté)
#     instructions
# # ici, la ressource est déjà fermée


# with open("notes.txt", "r", encoding="utf-8") as f:
#     contenu = f.read()

# print(contenu)   # le fichier est déjà fermé, mais `contenu` existe toujours

# f = open("notes.txt", "r", encoding="utf-8")
# try:
#     contenu = f.read()
# finally:
#     f.close()    # obligatoire, sinon le fichier reste ouvert


# Extraction des informations souhaitées avec Beautiful Soup
with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extraction du titre de la page
title = soup.title.string
print("Titre de la page:", title)

# Extraction du texte de la balise h1
h1_text = soup.find("h1").string
print("Texte de la balise h1:", h1_text)

# Dictionnaire pour stocker les produits
all_products = dict()

# Extraction des noms et des prix des produits dans la liste
products = soup.find_all("li")
for product in products:
    name = product.find("h2").string
    price_str = product.find("p", class_="price").string
    # On sépare la chaine avec " " en liste de mots
    price_list = price_str.split(" ")
    # On récupère le prix (= deuxième mot)
    all_products[name] = {"prix": price_list[1]}
    
    # Extraction de la description du produit
    # La description eest le dernier élément de la liste des paragraphes
    description = product.find_all("p")[-1].string
    all_products[name]["description"] = description

# Affichage des informations extraites
print("Produits:", all_products)

# Transformation des prix en dollars
for name in all_products.keys():
    price_str = all_products[name]["prix"]
    # Supprimer le symbole €
    price = price_str.strip("€")
    # Convertir en float
    price = float(price)
    dollar_price = price * 1.2
    all_products[name]["prix_dollar"] = f"{dollar_price}$"

# Affichage avec les prix en dollars
print("Tous les produits:", all_products)