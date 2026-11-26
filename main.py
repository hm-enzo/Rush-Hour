from plateau import Plateau
from Niveaux import niveau1
from Niveaux import niveau2
from Niveaux import niveau3

DIRECTIONS = {
    "H": {"gauche": -1, "droite": 1},
    "V": {"haut": -1, "bas": 1},
}

NIVEAUX = {"1": creer_voitures, "2": creer_voitures2,"3": creer_voitures3}

niveau = ""
while niveau not in NIVEAUX:
    niveau = input("Quel niveau voulez-vous jouer ? (1 ou 2 ou 3) ").strip()
    if niveau not in NIVEAUX:
        print("Niveau inconnu, choisissez 1 ou 2 ou 3")

voitures = NIVEAUX[niveau]()
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
            
    if not voiture.avancer(directions_possibles[direction], plateau):
        print("Pas possible : collision ou bord du plateau")
        continue

    if voiture_rouge.coordonnees_y == 4:
        gagne = True

plateau.afficher()
nb_mouvement = sum(v.mouvement for v in voitures)
print("Vous avez gagné en", nb_mouvement, "mouvements")
