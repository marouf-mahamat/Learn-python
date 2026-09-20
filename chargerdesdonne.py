fichier = open("hello.txt", "w")
fichier.write("Hello, world!")
fichier.close()


with open("file.txt") as fichier:
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)