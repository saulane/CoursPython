#!/usr/bin/python

from random import randrange


class Carte():
    figures = ['Valet', 'Dame', 'Roi']
    honneurs = figures + ['As']
    valeurs = list(range(7, 11)) + honneurs
    couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']

    def __init__(self, v=None, c=None):
        if not v:
            v = Carte.valeurs[randrange(0, len(Carte.valeurs))]
        if not c:
            c = Carte.couleurs[randrange(0, len(Carte.couleurs))]

        if not v in Carte.valeurs:
            raise ValueError(f"{v}: valeur incorrecte")
        if not c in Carte.couleurs:
            raise ValueError(f"{c}: couleur incorrecte")
        self.couleur = c
        self.valeur = v

    def __eq__(self, __o: object) -> bool:
        return (self.couleur == __o.couleur and self.valeur == __o.valeur and isinstance(__o, Carte))

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    __repr__ = __str__


class Cartes():
    def __init__(self, c=None):
        if c:
            self.cartes = c.cartes[:]
        else:
            self.cartes = []

    def __isub__(self, carte):
        self.cartes.remove(carte)

        return self

    def __str__(self):
        s = []
        for c in list(self.cartes):
            s += [str(c)]

        return ", ".join(s)

    def ajoute(self, c):
        self.cartes += [c]

    __repr__ = __str__


if __name__ == "__main__":
    des_cartes = Cartes()

    des_cartes.ajoute(Carte("As", "Coeur"))
    des_cartes.ajoute(Carte(10, "Carreau"))
    des_cartes.ajoute(Carte(7, "Trèfle"))

    print(f"{des_cartes=}")
    # ValueError: list.remove(x): x not in list
    des_cartes -= Carte(10, "Carreau")
    print(f"{des_cartes=}")
