ma_list=[1,2,3,4,5,6,7,8,9,10]
ma_list.append(11) #ajoute un élément à la fin de la liste
ma_list[1]=12 #modifie l'élément à l'index 1
affich=ma_list[2] #affiche l'élément à l'index 2
print(ma_list) #affiche la liste avec l'élément ajouté
print(affich) #affiche la valeur de l'élément à l'index 2

n=int(input("Entrez un nombre: "))
while n<1:
    n=int(input("Entrez un nombre: "))
l1=list(range(1,n+1)) #crée une liste de 1 à n
print(l1) #affiche la liste de 1 à n

#syntaxe de technique de decoupage dune liste
ma_liste=[1,2,3,4,5,6,7,8,9,10]
print(ma_liste[0:5:3]) #affiche les éléments de l'index 0 à 4
print(ma_liste[::2]) #affiche les éléments de l'index 0 à 9 avec un pas de 2

#l'affectation multiple permet d'affecter plusieurs variables en une seule ligne
# methode et fonction dune list
 
 # creer une liste des element 
nomList=list(("Jean","Pierre","Paul","Jacques"))
# nomList=list(range(start,stop,step)) 

nbrimpair=list(range(1,100,2))



