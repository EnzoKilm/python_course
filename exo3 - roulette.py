########################
#       ROULETTE       #
########################
from random import randint

rouge = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
noir = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
vert = 0
derniers_lances = []

while True:
    print("---------------------")
    rejouer = input("Souahitez-vous rejouer ?\n")
    
    if rejouer == "o":
        nombre_aleatoire = randint(0,36)
        if nombre_aleatoire in rouge:
            print(nombre_aleatoire, ": rouge")
        elif nombre_aleatoire in noir:
            print(nombre_aleatoire, ": noir")
        else:
            print(nombre_aleatoire, ": vert")

        if len(derniers_lances) == 5:
            del derniers_lances[4]

        derniers_lances.insert(0, str(nombre_aleatoire))
        phrase_derniers_lances = ', '.join(derniers_lances)
        
        print("Derniers lancés :", phrase_derniers_lances)

        tendance_rouge = tendance_noir = tendance_vert = 0
        for lance in derniers_lances:
            if int(lance) in rouge:
                tendance_rouge += 1
            elif int(lance) in noir:
                tendance_noir += 1
            else:
                tendance_vert += 1

        print("Rouge", tendance_rouge*20, "% | Vert", tendance_vert*20, "% | Noir", tendance_noir*20, "%")
            
    else:
        print("Merci d'avoir joué")
        break

