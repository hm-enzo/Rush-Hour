from plateau import Plateau
from voiture import Voiture

plateau = Plateau()
voiture_rouge = Voiture("rouge", 2, "H", 2, 0)
voiture_jaune = Voiture("jaune", 3, "V", 1, 4)
voiture_vert = Voiture("vert clair", 2, "V", 1, 2)
voiture_noire = Voiture("noire", 2, "H", 4, 4)
voiture_grise = Voiture("grise", 2, "H", 5, 4)
voiture_violet = Voiture("violet", 2, "V", 4, 2)
voiture_beige = Voiture("beige", 2, "V", 4, 1)
voiture_orange = Voiture("orange", 2, "V", 2, 5)
voiture_rose = Voiture("rose", 3, "H", 3, 0)
voiture_bleue = Voiture("bleue", 2, "V", 4, 0)


# Rouge
plateau.grille[2][0] = "R"
plateau.grille[2][1] = "R"

# Jaune
plateau.grille[1][4] = "J"
plateau.grille[2][4] = "J"
plateau.grille[3][4] = "J"

# Vert clair
plateau.grille[1][2] = "V"
plateau.grille[2][2] = "V"

# Noire (turquoise)
plateau.grille[4][4] = "N"
plateau.grille[4][5] = "N"

# Grise
plateau.grille[5][4] = "G"
plateau.grille[5][5] = "G"

# Violette
plateau.grille[4][2] = "P"
plateau.grille[5][2] = "P"

# Beige
plateau.grille[4][1] = "B"
plateau.grille[5][1] = "B"

# Orange
plateau.grille[2][5] = "O"
plateau.grille[3][5] = "O"

# Rose (violet horizontal sur l'image)
plateau.grille[3][0] = "S"
plateau.grille[3][1] = "S"
plateau.grille[3][2] = "S"

# Bleue
plateau.grille[4][0] = "L"
plateau.grille[5][0] = "L"

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
