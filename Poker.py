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
        """ Vérifie si deux cartes sont égales en valeurs et en couleurs"""
        if isinstance(carte, Carte):
            return carte.valeur == self.valeur and carte.couleur == self.couleur


class Cartes():
    def __init__(self, cartes=None) -> None:
        if not cartes:
            self.cartes = []
        else:
            self.cartes = copy.copy(cartes.cartes)

    def ajoute(self, c):
        """ Ajoute une carte dans le paquet de carte"""
        if isinstance(c, Carte):
            self.cartes += [c]
        elif isinstance(c, Cartes):
            self.cartes += copy(c)
        else:
            raise ValeurError(f"Impossible d'ajouter {type(c)} dans un paquet de carte")

    def pioche(self):
        """ Pioche la carte au dessus du paquet """
        try:
            return self.cartes.pop()
        except:
            raise ZeroCartesError("pioche vide!")

    def melanger(self):
    def melange(self):
        """ Mélange le paquet de carte de façon aléatoire à l'aide du module random"""
        shuffle(self.cartes)

    def trier(self, categorie="couleur"):
        """ Permet de trier le paquet de carte soit par valeur soit par couleur"""
        if categorie == "couleur":
            self.cartes.sort(key=lambda c: (c.couleur, Carte.valeurs.index(c.valeur)))
        elif categorie == "valeur":
            self.cartes.sort(key=lambda c: (Carte.valeurs.index(c.valeur), c.couleur))
        else:
            raise ValueError(f"Trie par 'couleur' ou 'valeur' uniquement, {categorie} non reconnue")

    def __len__(self):
        """Retourne le nombre de carte du paquet"""
        return len(self.cartes)

    def __repr__(self):
        return ", ".join([repr(c) for c in self.cartes])

    def __contains__(self, carte):
        """ Retourne True si la carte est présente dans le paquet"""
        if isinstance(carte, Carte):
            return carte in self.cartes
        else:
            raise ValueError(f"Un paquet de carte ne peut contenir que des cartes et pas de {type(carte)}")

    def __isub__(self, carte):
        """ Permet de retirer une ou plusieurs carte du paquet """
        if isinstance(carte, Carte):
            c = self.cartes.remove(carte)
            return self
        else:
            self.cartes = list(filter(lambda c: c not in carte, self.cartes))
            return self


class Jeu(Cartes):
    def __init__(self) -> None:
        """ Initialise un jeu de 32 cartes qui hérite de la classe Cartes"""

        Cartes.__init__(self)

        for v in Carte.valeurs:
            for c in Carte.couleurs:
                self.ajoute(Carte(v,c))


class Main(Cartes):
    def __init__(self, jeu):
        """ Initialise une main qui hérite de la classe Cartes"""
        Cartes.__init__(self)
        self.jeu = jeu

    def complete(self):
        """ Permet de tirer une carte du jeu et de l'ajouter à la main"""
        if len(self.jeu) > 0:
            self.ajoute(self.jeu.pioche())
        else:
            raise ZeroCartesError("plus de carte pour compléter la main")


class Carre(Cartes):
    def __init__(self, main) -> None:
        """ Initialise un carre depuis une main, si aucun carré n'est trouvé dans la main on retourne une erreur"""

        #On vérifie si on a bien 4 cartes ou plus
        if not len(main) > 3:
            raise RuntimeError(f"pas de carre dans {str(main)}")

        #On trie les cartes de la main par valeur ce qui va permettre de regrouper les couleurs entre elles
        main.trier("valeur")
        self.carre = None

        # On itère sur deux cartes en même qui sont espacées de 2 cartes exactement, puisque le jeu est trié par valeur si ces deux
        # cartes sont de la même valeur alors les deux entres elles le sont aussi et on a donc un carré
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
        """ Initialise une Quinte depuis une main et retourne une erreur si on n'en trouve pas """
        if len(main) < 4:
            raise RuntimeError(f"pas de quinte dans {str(main)}")


        #On trie par couleur
        main.trier("couleur")
        self.quinte_debut = None
       
       #On vérifie si dans 5 cartes à suivre la première et la dernière sont de la même couleur et sont espacées de 4 exactement
       #à l'aide du trie par couleur on peut en déduire que l'on a une quinte si ces deux conditions sont remplies
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
    le_jeu = Jeu()

    # on crée 2 mains vides
    ma_main = Main(le_jeu)
    ta_main = Main(le_jeu)
    print(f"{ma_main=}")
    print(f"{ta_main=}")

    # on y ajoute 3 cartes
    for i in range(3):
        ma_main.complete()
        ta_main.complete()
    print(f"{ma_main=}")
    print(f"{ta_main=}")
    print(f"{le_jeu=}")

    # on tente d'ajouter 25 cartes à la première
    try:
        for i in range(25):
            ma_main.complete()
    except ZeroCartesError as e:
        print(e)

    # on tente dajouter 25 cartes à la seconde
    try:
        for i in range(25):
            ta_main.complete()
    except ZeroCartesError as e:
        print(e)

    print("fin de programme")