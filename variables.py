#les commentaires sont des lignes de code qui ne sont pas exécutées par l'ordinateur. Elles servent à expliquer le code aux autres programmeurs ou à vous-même lorsque vous relisez votre code plus tard.   
#creation de variables
nom = "John" #variable de type string
age=20 #variable de type int
bole = True #variable de type booléen
livre = "Gatsby le Magnifique" #variable de type string


print("Nom:", nom) #affiche le nom
print("Age:", age) #affiche l'age
print("Booléen:", bole) #affiche la valeur du booléen
print("Livre:", livre) #affiche le nom du livre

#f-string est une fonctionnalité de Python qui permet d'insérer des variables dans une chaîne de caractères. Elle est très pratique pour créer des messages personnalisés ou pour afficher des informations de manière claire et lisible.
nom = "Dupont"
prenom = "Jean"
age = 30

print(f"Bonjour, je m'appelle {prenom} {nom} et j'ai {age} ans.")


numero_etudiant= 5
pi=3.14
notes=14.5
prenom="Maria"
est_valide=True

#assignment multiple variables in one line
a,b=5,10
x,y,z=1,2,3