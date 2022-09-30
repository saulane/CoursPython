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


    