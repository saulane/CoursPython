#!/usr/bin/python
from random import randrange, shuffle
import copy

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

    def __gt__(self, carte):
        if isinstance(carte, Carte):
            return Carte.valeur.index(self.valeur) > Carte.valeur.index(carte.valeur) 

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    def __eq__(self, carte):
        if isinstance(carte, Carte):
            return carte.valeur == self.valeur and carte.couleur == self.couleur

    __repr__ = __str__


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
            raise ValueError("pioche vide!")

    def melange(self):
        shuffle(self.cartes)

    def __len__(self):
        return len(self.cartes)

    def __str__(self):
        return ", ".join([str(c) for c in self.cartes])

    def __contains__(self, carte):
        if isinstance(carte, Carte):
            return carte in self.cartes

    def __isub__(self, carte):
        if isinstance(carte, Carte):
            c = self.cartes.remove(carte)
            return self
        elif isinstance(carte, Cartes):
            self.cartes = list(filter(lambda c: c not in carte, self.cartes))
            return self
        elif isinstance(carte, Quinte):
            self.cartes = list(filter(lambda c: c not in carte, self.cartes))
            return self

    __repr__ = __str__


class Jeu():
    def __init__(self) -> None:
        self.cartes_dispo = Cartes()

        for v in Carte.valeurs:
            for c in Carte.couleurs:
                self.cartes_dispo.ajoute(Carte(v,c))
        
        self.cartes_dispo.melange()

    def pioche(self):
        return self.cartes_dispo.pioche()

    def __len__(self):
        return len(self.cartes_dispo)

    def __isub__(self, carte):
        if isinstance(carte, Carte):
            if carte in self.cartes_dispo:
                self.cartes_dispo -= carte
                return self

    def __str__(self):
        return str(self.cartes_dispo)

    __repr__ = __str__


class Main():
    def __init__(self, jeu):
        self.jeu = jeu
        self.cartes = Cartes()


    def complete(self):
        if len(self.jeu) > 0:
            self.cartes.ajoute(self.jeu.pioche())
        else:
            raise ValueError("plus de carte pour compléter la main")

    def trier(self):
        self.cartes.cartes.sort(key=lambda x: Carte.valeurs.index(x.valeur))
    
    def __len__(self):
        return len(self.cartes)

    def __isub__(self, main):
        if isinstance(main, Main):
            self.cartes -= main.cartes
            return self
        elif isinstance(main, Carre):
            carre = Cartes()
            for c in Carte.couleurs:
                carre.ajoute(Carte(main.carre, c)) 
            self.cartes -= carre
            return self
        elif isinstance(main, Quinte):
            self.cartes -= main.cartes
            return self
        else:
            raise ValueError("Type non pris en charge")

    def __str__(self):
        return str(self.cartes)


    __repr__ = __str__


class Carre():
    def __init__(self, main) -> None:
        if not len(main) > 3:
            raise RuntimeError(f"pas de carre dans {str(main)}")
        main.trier()

        last_value = 0
        compteur = 0
        for carte in main.cartes.cartes:
            if carte.valeur != last_value:
                last_value = carte.valeur
                compteur = 0
            else:
                compteur +=1

            if compteur == 3:
                break

        if compteur == 3:
            self.cartes = Cartes()
            self.carre = last_value
            for c in Carte.couleurs:
                self.cartes.ajoute(Carte(last_value, c))
        else:
            raise RuntimeError(f"pas de carre dans {str(main)}")

    def __str__(self):
        return f"carré de {self.carre}"

    __repr__ = __str__


class Quinte():
    def __init__(self, main):
        if len(main) < 4:
            raise RuntimeError(f"pas de quinte dans {str(main)}")

        main.trier()
        cartes_couleurs = []
        for couleur in Carte.couleurs:
            cartes_couleurs.append([c for c in main.cartes.cartes if c.couleur == couleur])

        self.quinte_debut = None

        for deck in cartes_couleurs:
            if len(deck) > 3 and not self.quinte_debut:            
                for a,b in zip(deck, deck[4:]):
                    if Carte.valeurs.index(b.valeur) - Carte.valeurs.index(a.valeur) == 4:
                        self.quinte_debut = a

        if not self.quinte_debut:
            raise RuntimeError(f"pas de quinte dans {str(main)}")
        else:
            self.cartes = Cartes()
            self.cartes.ajoute(self.quinte_debut)

            for i in range(1,5):
                self.cartes.ajoute(Carte(Carte.valeurs[Carte.valeurs.index(self.quinte_debut.valeur)+i], self.quinte_debut.couleur))

    def __str__(self):
        return f"Quinte de {self.quinte_debut.couleur}"

    __repr__ = __str__
        
        



if __name__ == "__main__":
    # un_jeu = Jeu()
    # print(f"{un_jeu=}")
    # un_jeu -= Carte('Valet','Coeur')
    # un_jeu -= Carte('As','Pique')
    # un_jeu -= Carte(10,'Trèfle')
    # print(f"{un_jeu=}")
    le_jeu = Jeu()

    # une main de 25 cartes
    une_main = Main(le_jeu)
    for i in range(25):
        une_main.complete()
    print(f"{une_main=}")


    # recheche tous les carrés contenus dans la main
    while True:
        try:
            unequinte = Quinte(une_main)               
            # essai de créer un carré
            # si on est là, c'est qu'un carré a été créé
            print(f"{unequinte=}, {une_main=}")
            une_main -= unequinte
            # on l'enlève de la main
        except RuntimeError as e:
            # si on est là, c'est qu'un carré n'a pas pu être créé
            print(e)
            break

    print("fin de programme")