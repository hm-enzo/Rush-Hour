from voiture import Voiture


def creer_voitures():
    return [
        Voiture("rouge", 2, "H", 2, 2, "R"),
        Voiture("jaune", 3, "H", 1, 3, "J"),
        Voiture("vert clair", 2, "H", 0, 1, "V"),
        Voiture("noire", 2, "V", 4, 4, "N"),
        Voiture("grise", 2, "V", 1, 0, "G"), #bleue foncée sur la photo 
        Voiture("violet", 3, "V", 4, 2, "P"),
        Voiture("beige", 2, "V", 4, 5, "B"),
        Voiture("orange", 2, "H", 0, 4, "O"),
        Voiture("rose", 2, "V", 2, 4, "S"),
        Voiture("bleue", 2, "V", 4, 0, "L"),
    ]
