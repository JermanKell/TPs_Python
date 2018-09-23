from Classes_TP1 import *

Filecontent = False
name_file = False
flag = True

#print("Bonjour le monde!")

menu =  "1. Choisir un nom de fichier", "2. Ajouter un texte", "3. Afficher le fichier complet", \
        "4. Vider le fichier", "9. Quitter le programme"

## On parcoure jusqu'a ce que l'utilisateur choisisse d'arreter l'application
while flag:
    for choice in menu:
        print(choice)

    print('Choisir une action :')
#C:\Users\rapha\Desktop\TPs_Python\TP1\fichetu.csv
    saisie = input("Action: ")

    choix = int(saisie)

    if choix == 1:
        name_file = input('Fichier a ouvrir: ')

    elif name_file is not False:
        if choix == 2:
            file = open(name_file, "at")
            content = input()
            file.write(content+"\n")

        if choix == 3:
            file = open(name_file, "rt")
            Filecontent = file.read()
            if Filecontent is not False:
                list_student = list()
                Filecontent = Filecontent.split("\n")

                for line in Filecontent:
                    if len(line) > 0:
                            InfoArray = line.split(";")
                            student = Etudiant(InfoArray[0], InfoArray[1], Date(InfoArray[2]))
                            list_student.append(student)
                print(list_student)
            else:
                print("Impossible de lire le contenu du fichier")

        if choix == 4:
            file = open(name_file, "w")

        if choix == 9:
            flag = False

        file.close()
    else:
        print("Action non gérée!")

    print("\n")

print("Fermeture de l'application...")
file.close()
