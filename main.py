#!/usr/bin/python

import math

class Pointeur():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class PointeurZoomable():
    def __init__(self,x ,y, zoom) -> None:
        self.x = x
        self.y = y
        self.zoom = zoom

def zoomer(point, x):
    point.zoom *= x    

def localise(pointeur):
    print(pointeur.x, pointeur.y)

def avance(pointeur, dx, dy):
    pointeur.x += dx
    pointeur.y += dy 

class Cercle():
    def __init__(self) -> None:
        pass

    def initRayon(self, rayon):
        self.rayon = rayon

    def circonference(self):
        return 2*self.rayon*math.pi

    def surface(self):
        return self.rayon**2*math.pi


class Vehicule():
    def __init__(self, vmax, km, p) -> None:
        self.vmax = vmax
        self.km = km
        self.posx = p[0]
        self.posy = p[1]

    def print(self):
        print(f"kilometrage={self.km} vitesse_max={self.vmax} places={self.p}")



class C:
    nb_instances = 0

    def __init__(self,x,y):
      self.x = x
      self.y = y
      print(f"C({x},{y}) créé \t(#{id(self)})", end=" - ")
      C.mod_instance(1)

    def __del__(self):
      print(f"C({self.x},{self.y}) détruit \t(#{id(self)})", end=" - ")
      C.mod_instance(-1)

    @classmethod
    def mod_instance(cls,n):
      cls.nb_instances += n
      print(cls.how_many_instances())

    @classmethod
    def how_many_instances(cls):
      return f"instances vivantes: {cls.nb_instances}"


if __name__ == "__main__":
    z1 = C(1,2)
    z2 = C(1,-2)
    z1 = C(-1,-2)
    del z2
    z3 = z4 = C(0,0)
    z5 = C(1,1)
    del z4
    print("fin de programme")


    