from plateau import Plateau
from voiture import Voiture

Quantite_Voiture_Rouge=0
Historique_Voiture=[]

for Voiture_faite in Historique_Voiture:
    if Voiture_faite.couleur=="rouge":
        Quantite_Voiture_Rouge+=1
assert Quantite_Voiture_Rouge==1, "Il y a plus d'une voiture rouge sur le plateau"

plateau = Plateau()
voiture_rouge = Voiture("rouge", 2, "H", 2, 0)

plateau.grille[2][0] = "R"
plateau.grille[2][1] = "R"

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
