#  #print() permet d'afficher la valeur d'une expression sur l'ecran. une peut etre
# print("Helo",2+3)
# nom = input("Entrez votre nom: ") #input() permet de demander à l'utilisateur de saisir une valeur. La valeur saisie est stockée dans une variable.
# print(f"Bonjour, {nom}!")
# #input() permet de demander à l'utilisateur de saisir une valeur. La valeur saisie est stockée dans une variable.   
# #doit etre convertie en float pour pouvoir effectuer des calculs avec elle.

# Rayon=float(input("Entrez le rayon du cercle: ")) #input() permet de demander à l'utilisateur de saisir une valeur. La valeur saisie est stockée dans une variable.
# surface= Rayon**2*3.14 #calcul de la surface du cercle
# print(f"La surface du cercle est: {surface}") #affiche la surface du cercle


print("Programme qui calcule le chiffre d'affaire :")
quantite_produitvendu=float(input("Veuillez entrer la quantite de produits vendu:"))
prix_devente=float(input("Veuillez entrer le prix de vente :"))
chiffre_daffaire=quantite_produitvendu*prix_devente
print(f"le chiffre d affaire de l entreprise est :",chiffre_daffaire)