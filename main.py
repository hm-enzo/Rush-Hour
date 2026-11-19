from plateau import Plateau
from voiture import Voiture

gagne = False

while gagne == False:
    plateau.afficher()
    mouvement = input("Quelle voiture voulez-vous déplacer ? ")

    if mouvement == "R" or mouvement == "r":
        direction = input("Dans quelle direction ? (gauche ou droite) ")

        if direction == "gauche":
            deplacement = -1
        elif direction == "droite":
            deplacement = 1
        else:
            deplacement = 0
            print("Pas possible")

        if deplacement != 0:
            if not voiture_rouge.avancer(deplacement, plateau):
                print("Pas possible : collision ou bord du plateau")
    else:
        print("Pas possible")

    if voiture_rouge.coordonnees_y == 4:
        gagne = True

plateau.afficher()
print("Vous avez gagné")
