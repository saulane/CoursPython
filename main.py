#!/usr/bin/python

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


if __name__ == "__main__":
    point = Pointeur(1,-1)
    pointzoom = PointeurZoomable(0,0, 1)


    localise(point)
    avance(point, 9, 11)
    localise(point)

    localise(pointzoom)
    avance(pointzoom, 9,11)
    localise(pointzoom)
    zoomer(pointzoom, 2)
    localise(pointzoom)


    