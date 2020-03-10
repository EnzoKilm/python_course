from random import random

argent = 100

# si je gagne je double ma mise si je perd ba je perd

while argent > 0:
    print("----------------------------------------------")
    print(" vous avez ",argent,"pour arreter écrivez STOP")
    
    try:
        mise = int(input("combien misez vous ? : \n"))

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
