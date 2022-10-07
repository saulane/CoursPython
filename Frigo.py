#!/usr/bin/python

from copy import copy

class Frigo():
    def __init__(self) -> None:
        self.contenu = {}

    def etat(self):
        print("contenu:")
        for key in self.contenu:
            print(f"    {key}: {self.contenu[key]}")
        print("    .")

    def depose(self, content):
        for key in content:
            if key in self.contenu:
                self.contenu[key] += content[key]
            else:
                self.contenu[key] = content[key]

    def extraire_recette(self, recette):
        for key in recette.ingredients:
            self.contenu[key] -= recette.ingredient[key]
    
    def extraire_ingredients(self, ingredients):
        for key in ingredients:
            self.contenu[key] -= ingredients[key]

class Recette():
    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients

    def possible(self, frigo):
        for ingre in self.ingredients:
            if ingre not in frigo.contenu or frigo.contenu[ingre] < self.ingredients[ingre]:
                return False
        return True

    def extraire_multiple(self, frigo):
        if self.possible(frigo):
            for ingre in self.ingredients:
                frigo.contenu[ingre] -= self.ingredients[ingre]


class RecetteMultiple():
    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients

    def possible(self, frigos):
        combined = self.combine(frigos)

        for ingre in self.ingredients:
            if ingre not in combined or combined[ingre] < self.ingredients[ingre]:
                return False
        return True

    def combine(self, frigos):
        combined = {}
        for frigo in frigos:
            for ingr in frigo.contenu:
                if ingr in combined:
                    combined[ingr] += frigo.contenu[ingr]
                else:
                    combined[ingr] = frigo.contenu[ingr]
        return combined

    def extraire_multiple(self, frigos):
        restant = copy(self.ingredients)
        if self.possible(frigos):
            for frigo in frigos:
                to_del = []
                for ingre in restant:
                    if ingre in frigo.contenu:
                        reste = frigo.contenu[ingre] - restant[ingre]
                        # print(ingre, combined[ingre])
                        if frigo.contenu[ingre] <= restant[ingre]:
                            restant[ingre] -= frigo.contenu[ingre]
                            del frigo.contenu[ingre]
                        else:
                            frigo.contenu[ingre] -= restant[ingre]
                            to_del.append(ingre)

                for ing in to_del:
                    del restant[ing]


if __name__ == "__main__":
    un_frigo = Frigo()
    un_frigo.depose({
            "oeufs": 18
            , "beurre": 500
            , "yaourt": 6
            , "fraise": 10
            })
    #un_frigo.etat()
    un_frigo2 = Frigo()
    un_frigo2.depose({
            "oeufs": 15
            , "beurre": 250
            , "yaourt": 6
            , "prunes": 4
            })
    #un_frigo2.etat()

    tarte_aux_fraises = RecetteMultiple({
        "oeufs": 18
        , "beurre": 400
        , "fraise": 10
    })

    #print(tarte_aux_fraises.possible(un_frigo))
    
    print(tarte_aux_fraises.possible([un_frigo,un_frigo2])) # booléen indiquant si les ingrédients de la recette sont dispo
    tarte_aux_fraises.extraire_multiple([un_frigo, un_frigo2])
    un_frigo.etat()
    un_frigo2.etat()