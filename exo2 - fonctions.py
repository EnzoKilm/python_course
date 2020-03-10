# Créer une fonction 1
def afficher_nombre():
    return 10

resultat_fonction = afficher_nombre()

print(resultat_fonction)

# Créer une fonction 2
def afficher_nombre():
    print(10)
    
afficher_nombre()

# Fonction argument 1
def test_age(age):
    if age < 18:
        print("Vous êtes mineur")
    else:
        print("Vous êtes majeur")

test_age(18)

# Fonction argument 2
def test_age(age):
    if age < 18:
        return False
    else:
        return True

est_majeur = test_age(18)
print(est_majeur)

# Fonction deux arguments 1
def phrase(age, prenom):
    print("Vous vous appelez", prenom, "et vous avez", age, "ans.")

phrase(42, "Jean")

# Fonction deux arguments avec liste
def phrase(prenom, age):
    print(prenom, "a", age, "ans.")

classe = [
    ["Eric", 22], ["Enzo", 18], ["Jimmy", 47], ["Théo", 12]
    ]

for eleve in classe:
    phrase(eleve[0], eleve[1])

# Fonction récursive
def recursive(nombre):
    if nombre < 1000000000000:
        nombre = 2 * nombre
        recursive(nombre)

recursive(3)

# Fonction avec variable globale
def donne_moi_un_nom():
    global chat
    chat = "Miaou"

donne_moi_un_nom()
print(chat)

