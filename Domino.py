#!/usr/bin/python

from copy import copy

class Domino():
    def __init__(self, a, b) -> None:
        if a > 6 or b >6 or a<0 or b<0:
            raise Exception("Erreur")

        self.a = a
        self.b = b

    def retourne(self):
        self.a, self.b = self.b, self.a
        return self

    def __add__(self, d):
        if isinstance(d, Domino):
            c = Chaine()
            if self.b == d.a:
                c+=self
                c+=d
            elif self.a == d.a:
                c+=self.retourne()
                c+=d
            elif self.a == d.b:
                c+=d
                c+=self
            elif self.b == d.b:
                c+=self
                c+=d.retourne()
            else:
                raise Exception("Dominos non valides")
            
            return c
        else:
            return RuntimeError("Seulement les dominos sont acceptés")

    def __str__(self):
        return f"{self.a}:{self.b}"

class Chaine():
    def __init__(self) -> None:
        self.l_dom = []

    def __add__(self, d):
        if isinstance(d, Domino):
            c2 = copy(self)
            c2+=d
            return c2

    def __iadd__(self, d):
        if isinstance(d,Domino):
            if len(self) > 1:
                if self.l_dom[-1].b == d.a:
                    self.l_dom.append(d)
                elif self.l_dom[-1].b == d.b:
                    self.l_dom.append(d.retourne())
                else:
                    raise RuntimeError(f"Impossible d'insérer {d}")
                return self
            else:
                self.l_dom.append(d)
                return self
        else:
            raise RuntimeError("Seulement les dominos sont acceptés")

    def __imul__(self, d):
        if isinstance(d, Domino):
            try:
                self+=d
                return self
            except RuntimeError:
                if self.l_dom[0].a == d.a or self.l_dom[0].a == d.b:
                    self.retourne()
                    print(self)
                    self+=d
                    return self
                else:
                    raise RuntimeError("Impossible de modifier la chaine")

    def __len__(self):
        return len(self.l_dom)

    def dernier(self):
        if len(self)>0:
            return self.l_dom[-1]

    def retourne(self):
        new = [self.l_dom[i].retourne() for i in range(len(self)-1, -1, -1)]
        self.l_dom = new

    def __str__(self):
        return "-".join(list(map(str,self.l_dom)))


if __name__ == "__main__":
    # d1 = Domino(1,2)
    # d2 = Domino(3,2)
    # c = Chaine()
    # c += d1
    # c += d2
    # print(c)

    # print(f"{d1}, {d2}")

    # c = d1 + d2
    # print(c)
    # c+= Domino(0,0)
    # print(c, len(c))

    c = Domino(1,2)+Domino(3,2)+Domino(3,4)+Domino(2,4)
    print(c)                      # 1:2-2:3-3:4-4:2
    c *= Domino(6,2)
    print(c)   