from Classes_TP1 import *

Filecontent = False
name_file = False
flag = True

#print("Bonjour le monde!")
#C:\Users\rapha\Desktop\TPs_Python\TP1\fichetu.csv

menu =  "1. Choisir un nom de fichier", "2. Ajouter un texte", "3. Afficher le fichier complet", \
        "4. Vider le fichier", "9. Quitter le programme"

## On parcoure jusqu'a ce que l'utilisateur choisisse d'arreter l'application
while flag:
    try:

        for choice in menu:
            print(choice)

        print('Choisir une action :')

        saisie = input("Action: ")
        choix = int(saisie)

        assert choix == 1 or choix == 2 or choix == 3 or choix == 4 or choix == 9

        if choix == 1:
            name_file = input('Fichier a ouvrir: ')

        elif choix == 9:
            flag = False

        elif name_file is not False:

            if choix == 2:
                file = open(name_file, "at")
                content = input()
                file.write(content+"\n")
                file.close()

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

                file.close()

            if choix == 4:
                file = open(name_file, "w")
                file.close()
        else:
            raise IndexError

        print("\n")
    except AssertionError:
        print("La valeur saisie doit être une de ces valeurs: 1, 2, 3, 4, 9\n")
    except ValueError:
        print("La valeur saisie doit être un entier\n")
    except IndexError:
        print("Aucun fichier n'a été choisi (via commande 1)\n")
    except FileNotFoundError:
        print("Le fichier à lire n'a pas été trouvé")
    except:
        print("Une erreur a été levée\n")


print("Fermeture de l'application...")
