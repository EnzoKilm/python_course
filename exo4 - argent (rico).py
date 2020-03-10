from random import random

argent = 1000

# si je gagne je double ma mise si je perd ba je perd

while argent > 0:
    texte_argent = "║ Solde : " + str(argent) + "€ ║"
    barre = ""
    for i in range(0, len(texte_argent)-2):
        barre += "═"
    print("╔"+barre+"╗\n"+texte_argent+"\n╚"+barre+"╝")
    
    try:
        mise = int(input("Votre mise : "))

        if mise > argent:
            print("Vous n'avez pas assez d'argent!")
        else :
            lance = random()
            if lance < 0.5 :
                argent += mise
                print("Vous avez gagné",mise,"€")
            else :
                argent -= mise
                print("Vous avez perdu",mise,"€")

    except:
        print("Merci d'avoir joué, à bientôt!")
        break
