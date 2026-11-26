from plateau import Plateau
from Niveau_1 import creer_voitures

DIRECTIONS = {
    "H": {"gauche": -1, "droite": 1},
    "V": {"haut": -1, "bas": 1},
}

voitures = creer_voitures()
quantite_rouge = 0
for v in voitures: #parcourt dans les le tableau avec toutes les voitures du plateau
    if v.couleur == "rouge":
        quantite_rouge += 1
assert quantite_rouge == 1, "Il doit y avoir exactement une voiture rouge sur le plateau"

plateau = Plateau()
voitures_par_symbole = {}
for v in voitures:
    v.placer(plateau)
    voitures_par_symbole[v.symbole] = v

voiture_rouge = voitures_par_symbole["R"]

gagne = False

while not gagne:
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
        print("Pas possible : direction invalide")
        continue

     nombre_cases = int(input("De combien de cases voulez vous déplacer la voiture ?"))

    for i in range(nombre_cases):
        if not voiture.avancer(directions_possibles[direction], plateau):
            print("Pas possible : collision ou bord du plateau")
            break
        nb_mouvement+=1
        
    if not voiture.avancer(directions_possibles[direction], plateau):
        print("Pas possible : collision ou bord du plateau")
        continue

    if voiture_rouge.coordonnees_y == 4:
        gagne = True

plateau.afficher()
nb_mouvement = sum(v.mouvement for v in voitures)
print("Vous avez gagné en", nb_mouvement, "mouvements")
    if voiture_rouge.coordonnees_y == 4:
        gagne = True

plateau.afficher()
print("Vous avez gagné")
