#Syntaxe fichier = open ("chemin du fichier",mode mode d'ouvertuure)
# r=lecture 
# w= ecriture
fichier = open("hello.txt", "w")
fichier.write("Hello, world!")
fichier.close()


with open("file.txt") as fichier:
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)

# nom,metier,couleur_preferee
# Jacob Smith,Ingénieur en informatique,Violet
# Nora Scheffer,Stratégiste numérique,Bleu
# Emily Adams,Responsable Marketing,Orange


import csv

with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)


['nom', 'metier', 'couleur_preferee']
['Jacob Smith', 'Ingénieur en informatique', 'Violet']
['Nora Scheffer', 'Stratégiste numérique', 'Bleu']
['Emily Adams', 'Responsable Marketing', 'Orange']





# Le code ci-dessous montre comment utiliser la méthode  DictReader()  
import csv

    with open('couleurs_preferees.csv') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=',')
        for ligne in reader:
            print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])