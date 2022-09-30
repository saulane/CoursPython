#!/usr/bin/python

from typing import Counter, List
from collections import Counter

class Frigo():
    def __init__(self) -> None:
        self.contenu = Counter()

    def etat(self):
        print("contenu:")
        for key in self.contenu:
            print(f"    {key}: {self.contenu[key]}")
        print("    .")

    def depose(self, content):
        self.contenu = self.contenu + Counter(content)

    def __repr__(self) -> str:
        return f"{self.sign * self.num}/{self.den}"

    def extraire_recette(self, recette):
        self.contenu = self.contenu - recette.ingredients
    
    def extraire_ingredients(self, ingredients):
        self.contenu -= ingredients

    def inverse(self):
        self.num, self.den = self.den, self.num


class Recette():
    def __init__(self, ingredients) -> None:
        self.ingredients = Counter(ingredients)

    def possible(self, frigos):
        combined = Counter()
        for frigo in frigos:
            combined += frigo.contenu

        if combined< self.ingredients:
            return False
        return True

    def extraire_multiple(self, frigos):
        ingredients_restant = self.ingredients
        if self.possible(frigos):
            for frigo in frigos:
                print(ingredients_restant)
                ingredients_restant -= frigo.contenu
                frigo.extraire_ingredients(ingredients_restant)

    
            

if __name__ == "__main__":
    un_frigo = Frigo()
    un_frigo.depose({
            "oeufs": 6
            , "beurre": 250
            , "yaourt": 6
            , "fraise": 10
            })
    un_frigo.etat()
    un_frigo2 = Frigo()
    un_frigo2.depose({
            "oeufs": 12
            , "beurre": 250
            , "yaourt": 6
            , "prunes": 4
            })
    un_frigo2.etat()

    tarte_aux_fraises = Recette({
        "oeufs": 17
        , "beurre": 400
        , "fraise": 10
    })
    
    print(tarte_aux_fraises.possible([un_frigo, un_frigo2])) # booléen indiquant si les ingrédients de la recette sont dispo
    tarte_aux_fraises.extraire_multiple([un_frigo, un_frigo2])
    un_frigo.etat()
    un_frigo2.etat()