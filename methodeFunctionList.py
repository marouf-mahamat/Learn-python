#Append() ajoute un element a la fin de la liste 
#Syntaxe nomList.append(element)
info=["Marouf","mahamat"]
info.append("France")
print(info)

#Insert() insere un element a un index specifique dans une liste 
#syntaxe  nomlist.insert(index,element)
info.insert(2,"Saleh")
print(info)

#extend() permet d'ajouter les element d une sequence
# nomlist.extend(sequence)
langue=["ar","ang"]

info.extend(langue)
print(info)

#remove() supprime un element 
# syntaxe nomlist.remove(element)

#pop() permer de suprimer un element a lindice indiauer et renvoyer 'element
#syntaxe nomlist.pop(index )

#nomliste.clear() supprime tout les element de la list

#del nomlist[index]

del info[0]

#len(list) renvoie les nombre d element d une liste , la taile d une liste

#sum(list) calcul la somme des seulement d une liste 
l=[1,2,3,4,5]
print(sum(l)/len(l))

# max() , min()

#count (element)

L=[10,2,3,4,5,66,7,8,2,44,55,2]
L.sort(reverse=True)
print(L)
L.count(2)
print(L.count(2))

#nomlist.reverse()

#nomlist.sort(key=,reverse=) Trier une liste

#nomlist.sorted(listdorigine,ke=,reverse=) une fonction qui trie creer une nouvelle list

#index() Recherche la premiere occurence de lelement specifier et renvoi son index
#nomlist.index(element,debut,fin)

#copy() 
# L=listdorigine.copy()


#Parcourir une list avec les boucle

#appartenir a une list
# l'operateur in 

#Syntaxe x=element in nomlist

N=[1,2,3,4,5,6,7,8,9]
for note in N : # Parcourir une liste
    print(note)

#Parcourir une list for avec range
#Syntaxe for index in range(len(nomlis)):

for i in range(len(N)):
    print(i+1,"",N[i])


#Parcourir avec zip

# for el1,el2,..,in zip(l1,l2):