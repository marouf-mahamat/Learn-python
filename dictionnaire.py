#Un dictionnaire est une structure de données qui enregistre des données dans des paires clés-valeurs. Voici un exemple d’une clé et d’une valeur :  
nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2


infos_labradoodle = {
    "poids": "13 à 16 kg",
    "origine": "États-Unis"
}

print(taux_de_conversion)


infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris"

del infos_labradoodle["origine"]



# Syntaxe

# keys()

# ​​Retourne une vue sur les clés du dictionnaire.

# nom_du_dictionnaire.keys()

# values()

# Retourne une vue sur les valeurs du dictionnaire.

#  nom_du_dictionnaire.values()

# items()

# Retourne une vue sur les couples (clé, valeur) du dictionnaire.

#  nom_du_dictionnaire.items()

# get(clé)


# Retourne la valeur associée à la clé spécifiée. Si la clé n'est pas présente dans le dictionnaire, retourne la valeur None  .

#  nom_du_dictionnaire.get(clés)

# pop(clé)

# Supprime la clé spécifiée et retourne la valeur associée. Si la clé n'est pas présente dans le dictionnaire, retourne la valeur None  .

#  nom_du_dictionnaire.pop(clés)

# clear()

# Supprime tous les éléments du dictionnaire.

#  nom_du_dictionnaire.clear()


"poids" in infos_labradoodle


S1=dict ({"nom":"iphonr","prix":"999"})

# get() ppermet d'acceder a une valeur dans un dictionnaire a partir d'une sans generer d'erreur si la cle n'existe pas
# syntaxe  valeur = nomDict.get(cle)
#print( nomDict.get(cle))

etudiants= {
    "nom":"iphonr",
    "prix":"999"
}

print("nom",etudiants.get("nom "))

# items() renvoie toutes les paires cle-valeur du dictionnaire sous form tuple
print(etudiants.items())

#keys() permet d'obtenir une vue de types dict_keys contenant toutes les cles du dictionnaire

#syntaxes
print(etudiants.keys())

#values() renvoie une vue de types value contenant toutes les valeurs du dictionnaire 

print(etudiants.values())

#update() ajout ou modification 

# etudiants.update({cle:valeur}) 

#setdefault() recupere la valeur de la cle ,elle ajoute si nexiste pas 
etudiants.setdefault("filiere","info")

#pop()

#sorted trie pour donner une liste

sorted(etudiants)

#copy()
