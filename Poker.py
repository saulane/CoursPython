#!/usr/bin/python
from random import randrange, shuffle
import copy

class CouleurError(ValueError): pass
class ValeurError(ValueError): pass
class ZeroCartesError(ValueError): pass

class Carte():
    valeurs = list(range(7, 11)) + ['Valet', 'Dame', 'Roi', 'As']
    couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']

    def __init__(self, v=None, c=None):
        if v:
            if not v in Carte.valeurs:
                raise ValeurError(f"{v}: valeur incorrecte")
        else:
            v = Carte.valeurs[randrange(0, len(Carte.valeurs))]

        if c:
            if not c in Carte.couleurs:
                raise CouleurError(f"{c}: couleur incorrecte")
        else:
            c = Carte.couleurs[randrange(0, len(Carte.couleurs))]

        self.couleur = c
        self.valeur = v

    def __gt__(self, carte):
        if isinstance(carte, Carte):
            return Carte.valeur.index(self.valeur) > Carte.valeur.index(carte.valeur) 

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

    def __eq__(self, carte):
        if isinstance(carte, Carte):
            return carte.valeur == self.valeur and carte.couleur == self.couleur


class Cartes():
    def __init__(self, cartes=None) -> None:
        if not cartes:
            self.cartes = []
        else:
            self.cartes = copy.copy(cartes.cartes)

    def ajoute(self, c):
        self.cartes += [c]

    def pioche(self):
        try:
            return self.cartes.pop()
        except:
            raise ZeroCartesError("pioche vide!")

    def melange(self):
        shuffle(self.cartes)

    def trier(self, categorie="couleur"):
        if categorie == "couleur":
            self.cartes.sort(key=lambda c: (c.couleur, Carte.valeurs.index(c.valeur)))
        elif categorie == "valeur":
            self.cartes.sort(key=lambda c: (Carte.valeurs.index(c.valeur), c.couleur))
        else:
            raise ValueError(f"Trie par 'couleur' ou 'valeur' uniquement, {categorie} non reconnue")

    def __len__(self):
        return len(self.cartes)

    def __repr__(self):
        return ", ".join([str(c) for c in self.cartes])

    def __contains__(self, carte):
        if isinstance(carte, Carte):
            return carte in self.cartes

    def __isub__(self, carte):
        if isinstance(carte, Carte):
            c = self.cartes.remove(carte)
            return self
        else:
            self.cartes = list(filter(lambda c: c not in carte, self.cartes))
            return self


class Jeu(Cartes):
    def __init__(self) -> None:
        Cartes.__init__(self)

        for v in Carte.valeurs:
            for c in Carte.couleurs:
                self.ajoute(Carte(v,c))

    def __repr__(self):
        return str(self.cartes)


class Main(Cartes):
    def __init__(self, jeu):
        Cartes.__init__(self)
        self.jeu = jeu

    def complete(self):
        if len(self.jeu) > 0:
            self.ajoute(self.jeu.pioche())
        else:
            raise ZeroCartesError("plus de carte pour compléter la main")

    def __repr__(self):
        return str(self.cartes)


class Carre(Cartes):
    def __init__(self, main) -> None:
        if not len(main) > 3:
            raise RuntimeError(f"pas de carre dans {str(main)}")
    
        main.trier("valeur")
        self.carre = None

        for c1,c4 in zip(main.cartes, main.cartes[3:]):
            if c1.valeur == c4.valeur:
                self.carre = c1.valeur
                break

        if not self.carre:
            raise RuntimeError(f"pas de carre dans {str(main)}")
        else:
            Cartes.__init__(self)
            for c in Carte.couleurs:
                self.ajoute(Carte(self.carre, c))

    def __repr__(self):
        return f"carré de {self.carre}"


class Quinte(Cartes):
    def __init__(self, main):
        if len(main) < 4:
            raise RuntimeError(f"pas de quinte dans {str(main)}")

        main.trier("couleur")
        self.quinte_debut = None
       
        for c1,c5 in zip(main.cartes, main.cartes[4:]):
            if c1.couleur == c5.couleur:
                if Carte.valeurs.index(c5.valeur) - Carte.valeurs.index(c1.valeur) == 4:
                    self.quinte_debut = c1
                    Cartes.__init__(self)
                    break

        if not self.quinte_debut:
            raise RuntimeError(f"pas de quinte dans {str(main)}")
        else:
            self.ajoute(self.quinte_debut)

            for i in range(1,5):
                self.ajoute(Carte(Carte.valeurs[Carte.valeurs.index(self.quinte_debut.valeur)+i], self.quinte_debut.couleur))

    def __repr__(self):
        return f"Quinte de {self.quinte_debut.couleur}"


if __name__ == "__main__":
    print(Carte())                      # -> Valet de Trèfle (par exemple)
    print(Carte())                      # -> Dame de Coeur (par exemple)
    print(Carte())                      # -> 8 de Carreau (par exemple)
    carte1 = Carte(7,"Coeur")
    print(carte1)                       # -> 7 de Coeur
    carte2 = Carte("Valet","pic")       # -> ValueError: pic: couleur incorrecte
    carte3 = Carte("Valet","Pique")
    print(carte3)       