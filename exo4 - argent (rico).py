from random import random

argent = 1000

# si je gagne je double ma mise si je perd ba je perd

while argent > 0:
    texte_argent = "║Solde : " + str(argent) + "€ ║"
    barre = ""
    for i in range(0, len(texte_argent)-2):
        barre += "═"
    print("╔"+barre+"╗")
    print(texte_argent)
    print("╚"+barre+"╝")
    
    try:
        mise = int(input("Combien misez vous ? : \n"))

        if mise > argent:
            print("vous n'avez pas assez d'argent")
        else :
            lance = random()
            if lance < 0.5 :
                argent += mise
                print("vous avez gagné",mise*2)
            else :
                argent -= mise
                print("vous avez perdu",mise)

    except:
        print("Merci d'avoir joué, à bientôt!")
        break
