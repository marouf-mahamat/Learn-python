print("Programme qui calcul la division:")
Dividente=int(input("Entrer la dividente:"))
Diviseur=int(input("Entrer la diviseur:"))
if Dividente!=0 :
    Resultat=Dividente/Diviseur
    print("Resultat:",Resultat)
else:
    print("division par zero est impossible")


# if condition:
#     # code exécuté si condition est vraie
# elif autre_condition:
#     # code exécuté si autre_condition est vraie
# else:
#     # code exécuté si aucune condition n'est vraie

age = 20

if age < 13:
    print("Enfant")
elif age < 18:
    print("Adolescent")
else:
    print("Adulte")