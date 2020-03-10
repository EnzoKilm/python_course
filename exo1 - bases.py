# Afficher quelque chose
print("bonjour") # texte
print(2020) # chiffre

# Définir et afficher une variable
bonjour = "salut"
print(bonjour)

# Nombre à virgule
nombre = 29.2
print(nombre)
print(type(nombre))

# Concaténation 1
str1 = "Je m'appelle"
str2 = "Michel"
phrase = str1 + str2
print(phrase)

# Concaténation 2
str1 = "Je m'appelle"
str2 = "Michel"
print(str1,str2)

# Concaténation 3
str1 = "Je m'appelle"
str2 = "Michel et j'ai"
int1 = 3
str3 = "ans"

print(str1,str2,int1,str3)

# Entier vers string
int1 = 3
nombre = str(int1)
print(type(nombre))

# String vers entier
str1 = "56"
nombre = int(str1)
print(type(nombre))

# Addition
nombre = 1 + 2
chiffre1 = 39
chiffre2 = 10
nombre2 = chiffre1 + chiffre2
print(nombre2)

# Soustraction
nombre = 39 - 1
print(nombre)

# Multiplication et division
nombre = 10 * 2
nombre2 = 5 / 2
print(nombre)
print(type(nombre))

# Puissances
nombre = 10**3
print(nombre)

# Modulo
nombre = 7 % 2
print(nombre)

# Arrondi
nombre = 3.14
print(round(nombre, 1))

# Arrondi inférieur et supérieur
from math import *

nombre = 6.854
arrondiInf = floor(nombre)
arrondiSup = ceil(nombre)
print(arrondiInf)
print(arrondiSup)

# Entrée d'une chaine de caractères
prenom = input("Votre prénom : ")
print(prenom)

# Entrée d'un entier
age = int(input("Quel est votre age ?"))
print(age)

# Conditions
age = int(input("Votre âge : "))
if age == 18:
    print("Vous venez d'être majeur")
elif age < 18:
    print("Vous êtes mineur")
else:
    print("Vous etes majeur")

# Différentes conditions
# == : égal
# != : différent
# < : inférieur
# > : supérieur
# <= : inférieur ou égal
# >= : supérieur ou égal

# Et
if 2 < 3 and 5 < 6:
    print("Salut")
else:
    print("Rien")
    
# Ou
if 2 < 3 or 5 < 2:
    print("Salut")
else:
    print("Rien")

# Tests/exceptions
try:
    age = int(input("Votre âge : "))
    print("Vous avez",age)
except:
    print("Vous devez entrer un nombre entier")

# Boucle while
age = 0
while age < 18:
    try:
        age = int(input("Votre âge : "))
        if age < 18:
            print("Revez quand vous serez majeur")
        else:
            print("Bienvenue sur le programme")
    except:
        print("Vous devez entrer un nombre entier")

print("Programme Python")

# Boucle infinie
while True:
    try:
        age = int(input("Votre âge : "))
        if age < 18:
            print("Revez quand vous serez majeur")
        else:
            print("Bienvenue sur le programme")
            break
    except:
        print("Vous devez entrer un nombre entier")
    
print("Programme Python")

# Boucle tant que (compteur)
prenom = "Mahmoud"
compteur = 0
for lettre in prenom:
    compteur += 1
print(compteur)

# Boucle tant que (compteur)
prenom = "Pascal"
for lettre in prenom:
    print(lettre)

# Listes
prenoms = ["Quentin", "Corentin", "Théo", "Maxime", "Corentin"]
#print(prenoms[1])

prenoms.append("Matthieu")
#print(prenoms)

#del prenoms[2] #supprimer avec index
#prenoms.remove("Corentin") #supprimer avec valeur
print(prenoms)

# Supprimer des éléments d'une liste avec une boucle for
for prenom in prenoms:
    if prenom == "Corentin":
        prenoms.remove(prenom)
    else:
        pass

print(prenoms)

# Fonction len()
print(len("salut"))
print(len(["Enzo", "Eric", "Matthias"]))

# Listes de listes (matrices)
carte = [
    ["0:0", "0:1", "0:2"],
    ["1:0", "1:1", "1:2"],
    ["2:0", "2:1", "2:2"]
    ]

for ligne in carte:
    afficher_ligne = ""
    for case in ligne:
        afficher_ligne += case + "|"
    print(afficher_ligne)

print(carte[1][0])

# Dictionnaires
mon_dico = {"Formateur" : "Enzo",
            "Élève" : "Éric"}
print(mon_dico['Formateur'])
print(mon_dico['Élève'])

for cle in mon_dico:
    print(mon_dico[cle])
