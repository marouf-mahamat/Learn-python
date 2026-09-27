# for cle in nomDict: parcourir par les cle
# for valeur in nomDict.values(): parcourir par les valeur
# for cle,valeur in nomDict.items parcourir par les paire


resultat={}
nbr_etudiants=int(input("combien d'etudiant voulez vous saisir :"))
for i in range(nbr_etudiants):
    nom=input("entrer le nom de l'etudiant:")
    note=float(input("entrer la note de l'etudiant:"))
    resultat[nom]=note
print("resultats des etudiants:")

for nom,note in resultat.items():
    print("",nom,"",note) 

n=0
for nom,note in resultat.items():
    if note > 12:
        print("nom:",nom,"ayant reussi avec :",note) 
        n+=1
print("nombre d'etudiant ayant reussi est :",n)