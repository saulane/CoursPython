from multiprocessing.sharedctypes import Value
from random import randrange


class Carte():
    valeurs = list(range(7, 11)) + ['Valet', 'Dame', 'Roi', 'As']
    couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']

    def __init__(self, v=None, c=None):
        if v:
            if not v in Carte.valeurs:
                raise ValueError(f"{v}: valeur incorrecte")
        else:
            v = Carte.valeurs[randrange(0, len(Carte.valeurs))]

        if c:
            if not c in Carte.couleurs:
                raise ValueError(f"{c}: couleur incorrecte")
        else:
            c = Carte.couleurs[randrange(0, len(Carte.couleurs))]

        self.couleur = c
        self.valeur = v

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    __repr__ = __str__


class Cartes():
    def __init__(self, cartes=None) -> None:
        if not cartes:
            self.cartes = []
        else:
            self.cartes = cartes.cartes

    def __str__(self):
        return ", ".join([str(c) for c in self.cartes])

    def ajoute(self, c):
        self.cartes += [c]

    def pioche(self):
        try:
            return self.cartes.pop()
        except:
            print("dsf")
            raise ValueError("pioche vide!")
    __repr__ = __str__

if __name__ == "__main__":
    # 3 cartes
    carte1 = Carte("As", "Trèfle")
    carte2 = Carte(7, "Coeur")
    carte3 = Carte("Valet", "Pique")

    # un ensemble de cartes (vide au départ)
    des_cartes = Cartes()

    # on y ajoute les 3 cartes
    for une_carte in [carte1, carte2, carte3]:
        des_cartes.ajoute(une_carte)

    print(f"{des_cartes=}")

    # on le clone
    les_memes = Cartes(des_cartes)
    print(f"{les_memes=}")

    # on pioche dedans tant que l'on peut
    try:
        while True:
            print(f"{des_cartes.pioche()=}")
            print(f"{des_cartes=}")
            print(f"{les_memes=}")
    except ValueError as e:
        # traceback.print_exc(file=sys.stdout)
        print(e)
    print("fin de programme")
