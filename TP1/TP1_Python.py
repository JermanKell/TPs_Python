#print("Hello world!")

file = False
name_file = False
flag = True

menu =  "1. Choisir un nom de fichier", "2. Ajouter un texte", "3. Afficher le fichier complet", \
        "4. Vider le fichier", "9. Quitter le programme"

## On cycle jusqu'a ce que l'utilisateur choisisse d'arreter l'application
while flag:
    for choice in menu:
        print(choice)

    print('Veuillez selectionner une action a effectuer:')

    sel = input("Action: ")

    while sel%2 != 0 and sel%2 != 1:
        print("La selection est incorrecte. Veuillez recommencer!")
        sel = input("Action: ")

    if sel == 1:
        filename = input('Fichier a ouvrir: ')
        name_file = filename
        file = open(filename, "at")
    if file != False:
        if sel == 2:
            content = input()
            file.write(content+"\n")
        if sel == 3:
            file.read()
        if sel == 4:
            file.close
            file = open(name_file, "w").close
            file = open(name_file, "at")
        if sel == 9:
            file.close
            flag = False

print("Fermeture de l'application...")
