# Connexion_plateforme
'''
Description:
Utilisation de fonctions, de boucles et de conditions pour afficher des informations suite à la saisie de données.
Ce programme pourrait être aussi utilisé pour définir les conditions de connexion à une plateforme.
'''

import sys
# Définir les fonctions
def demander_nom():
    nom_f = input("Quel est votre nom ? : ")
    while nom_f == "":
        print("Vous devez saisir votre nom avant de continuer")
        nom_f = input("Quel est votre nom ? : ")
    return nom_f


def demander_age():
    while True:
        age_f = input("Quel est votre age ? : ")
        try:
            age_f = int(age_f)
        except:
            print("ERREUR, vous devez rentrez un nombre pour l'age")
        else:
            if age_f < 6:
                print("Votre age n'est pas accpeté")
                sys.exit("Vous devez avoir au moins 6 ans.")
            else:
                break
    return age_f


def afficher_infos(nom, age):
    print("Vous vous appelez", nom, " et vous avez", age, "ans.")
    if age == 17:
        print("Vous êtes presque majeur")
    elif age == 18:
        print("Vous êtes tout juste majeur. Félicitations !")
    elif age < 12:
        print("Vous êtes un enfant")
    elif 12<age<18:
        print("Vous êtes mineur")
    elif 18<age<60:
        print("Vous êtes adulte")
    else:
        print("Vous êtes senior")


# demander le nom
nom = demander_nom()

# Demander l'âge
age = demander_age()

# Afficher les informations
afficher_infos(nom, age)
