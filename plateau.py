class Plateau:
    def __init__(self):
        self.grille = []
        for i in range(6):
            self.grille.append(["x", "x", "x", "x", "x", "x"])

    def afficher(self):
        print("0 1 2 3 4 5")
        for i in range(6):
            print(self.grille[i][0], self.grille[i][1], self.grille[i][2], self.grille[i][3], self.grille[i][4], self.grille[i][5])
