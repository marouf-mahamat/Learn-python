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