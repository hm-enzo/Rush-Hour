class Voiture:
    def __init__(self, couleur, taille, orientation, coordonnees_x, coordonnees_y):
        self.couleur = couleur
        self.symbole = "R"
        self.taille = 2
        self.orientation = "H"
        self.coordonnees_x = 2
        self.coordonnees_y = 0

    def avancer(self, nb_cases, plateau):
        for i in range(self.taille):
            plateau.grille[2][self.coordonnees_y + i] = "x"
        self.coordonnees_y = self.coordonnees_y + nb_cases
        for i in range(self.taille):
            plateau.grille[2][self.coordonnees_y + i] = "R"
