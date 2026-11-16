from plateau import Plateau
from voiture import Voiture

Quantite_Voiture_Rouge=0
Historique_Voiture=[]

plateau = Plateau()
voiture_rouge = Voiture("rouge", 2, "H", 2, 0)

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
        
For Voiture_faite in Historique_Voiture:
    if Voiture_faite.couleur=="rouge":
        Quantite_Voiture_Rouge+=1
Assert Quantite_Voiture_Rouge==1, "Il ya a 2 voitures rouges sur le plateau"

    if voiture_rouge.coordonnees_y == 4:
        gagne = True

plateau.afficher()
print("Vous avez gagné")
