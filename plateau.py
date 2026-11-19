VIDE = "."


class Plateau:
    def __init__(self):
        self.grille = []
        for i in range(6):
            self.grille.append([VIDE, VIDE, VIDE, VIDE, VIDE, VIDE])

    def afficher(self):
        for i in range(6):
            print(self.grille[i][0], self.grille[i][1], self.grille[i][2], self.grille[i][3], self.grille[i][4], self.grille[i][5])
