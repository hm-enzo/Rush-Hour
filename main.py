from plateau import Plateau
from voiture import Voiture

plateau = Plateau()

voiture_rouge = Voiture("rouge", 2, "H", 2, 0, "R")
voiture_jaune = Voiture("jaune", 3, "H", 4, 1, "J")
voiture_vert = Voiture("vert clair", 2, "V", 0, 1, "V")
voiture_noire = Voiture("noire", 2, "V", 3, 4, "N") #voiture noire = voiture verte foncee sur carte
voiture_grise = Voiture("grise", 2, "V", 4, 0, "G")
voiture_violet = Voiture("violet", 2, "V", 2, 5, "P")
voiture_beige = Voiture("beige", 2, "V", 4, 5, "B")
voiture_orange = Voiture("orange", 2, "H", 0, 4, "O")
voiture_rose = Voiture("rose", 2, "V", 2, 3, "S")
voiture_bleue = Voiture("bleue", 2, "V", 2, 2, "L")

voitures = [voiture_rouge, voiture_jaune, voiture_vert, voiture_noire, voiture_grise,
            voiture_violet, voiture_beige, voiture_orange, voiture_rose, voiture_bleue]

voitures_par_symbole = {}
for voiture in voitures:
    voiture.placer(plateau)
    voitures_par_symbole[voiture.symbole] = voiture

DIRECTIONS = {
    "H": {"gauche": -1, "droite": 1},
    "V": {"haut": -1, "bas": 1},
}

gagne = False

while gagne == False:
    plateau.afficher()
    choix = input("Quelle voiture voulez-vous déplacer ? (R, J, V, N, G, P, B, O, S, L) ").upper()

    if choix not in voitures_par_symbole:
        print("Pas possible : voiture inconnue")
        continue

    voiture = voitures_par_symbole[choix]
    directions_possibles = DIRECTIONS[voiture.orientation]
    texte = " ou ".join(directions_possibles)
    direction = input("Dans quelle direction ? (" + texte + ") ").lower()

    if direction not in directions_possibles:
        print("Pas possible : direction invalide pour cette voiture")
        continue

    if voiture.avancer_jusqu_au_bout(directions_possibles[direction], plateau) == 0:
        print("Pas possible : collision ou bord du plateau")

    if voiture_rouge.coordonnees_y == 4:
        gagne = True

plateau.afficher()
print("Vous avez gagné")
