from plateau import Plateau
from voiture import Voiture

plateau = Plateau()
voiture_rouge = Voiture("rouge", 2, "H", 2, 0)
voiture_jaune = Voiture("jaune", 3, "H", 4, 1)
voiture_vert = Voiture("vert clair", 2, "V", 0, 1)
voiture_noire = Voiture("noire", 2, "V", 3, 4) #voiture noire = voiture vert fonce sur carte
voiture_grise = Voiture("grise", 2, "V", 4, 0)
voiture_violet = Voiture("violet", 2, "V", 2, 5)
voiture_beige = Voiture("beige", 2, "V", 4, 5)
voiture_orange = Voiture("orange", 2, "H", 0, 4)
voiture_rose = Voiture("rose", 2, "V", 2, 3)
voiture_bleue = Voiture("bleue", 2, "V", 2, 2)







plateau.grille[2][0] = "R"
plateau.grille[2][1] = "R"

gagne = False

while gagne == False:
    plateau.afficher()
    mouvement = input("Quelle voiture voulez-vous déplacer ? ")

    if mouvement == "R" or mouvement == "r":
        direction = input("Dans quelle direction ? (gauche ou droite) ")

        if direction == "gauche":
            if voiture_rouge.coordonnees_y > 0:
                voiture_rouge.avancer(-1, plateau)
            else:
                print("Pas possible")

        if direction == "droite":
            if voiture_rouge.coordonnees_y < 4:
                voiture_rouge.avancer(1, plateau)
            else:
                print("Pas possible")
        else:
            print("Pas possible")
    else:
        print("Pas possible")

    if voiture_rouge.coordonnees_y == 4:
        gagne = True

plateau.afficher()
print("Vous avez gagné")
