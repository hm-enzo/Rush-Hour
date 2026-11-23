from plateau import VIDE


class Voiture:
    def __init__(self, couleur, taille, orientation, coordonnees_x, coordonnees_y, symbole):
        self.couleur = couleur
        self.symbole = symbole
        self.taille = taille
        self.orientation = orientation
        self.coordonnees_x = coordonnees_x
        self.coordonnees_y = coordonnees_y

    def cases(self, x=None, y=None):
        if x is None:
            x = self.coordonnees_x
        if y is None:
            y = self.coordonnees_y
        if self.orientation == "H":
            return [(x, y + i) for i in range(self.taille)]
        return [(x + i, y) for i in range(self.taille)]

    def placer(self, plateau):
        for ligne, colonne in self.cases():
            plateau.grille[ligne][colonne] = self.symbole

    def effacer(self, plateau):
        for ligne, colonne in self.cases():
            plateau.grille[ligne][colonne] = VIDE

    def peut_avancer(self, nb_cases, plateau):
        if self.orientation == "H":
            nouvelles_cases = self.cases(y=self.coordonnees_y + nb_cases)
        else:
            nouvelles_cases = self.cases(x=self.coordonnees_x + nb_cases)

        for ligne, colonne in nouvelles_cases:
            if not (0 <= ligne < 6 and 0 <= colonne < 6):
                return False
            case = plateau.grille[ligne][colonne]
            if case != VIDE and case != self.symbole:
                return False
        return True

    def avancer(self, nb_cases, plateau):
        if not self.peut_avancer(nb_cases, plateau):
            return False
        self.effacer(plateau)
        if self.orientation == "H":
            self.coordonnees_y += nb_cases
        else:
            self.coordonnees_x += nb_cases
        nb_mouvement+=1
        self.placer(plateau)
        return True

    def avancer_jusqu_au_bout(self, sens, plateau):
        nb_cases = 0
        while self.peut_avancer(sens * (nb_cases + 1), plateau):
            nb_cases += 1
        if nb_cases > 0:
            self.avancer(sens * nb_cases, plateau)
        nb_mouvement+=1
        return nb_cases
