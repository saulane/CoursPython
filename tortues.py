#!/usr/bin/python
import math
import random
import time

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

class Tortue():
    def __init__(self, name, pos, vmax=None) -> None:
        if not vmax:
            self.vmax = random.random()*8+2
        else:
            self.vmax = vmax

        self.name = name
        self.posx = pos[0]
        self.posy = pos[1]
    
    def localise(self):
        print(self.name,self.posx, self.posy)
    
    def avance(self, dx=None,dy=None):
        self.posx += dx if dx else random.random()*self.vmax
        self.posy += dy if dy else 0

class Course():
    def __init__(self) -> None:
        self.partants = []

    def enregistre(self, tortue: Tortue):
        self.partants.append(tortue)
    
    def run(self):
        time.sleep(.5)
        for i in range(1,4):
            print(i)
            time.sleep(.5)
        print("Partez")

        for step in range(100):
            print(f"{step=}")
            for t in self.partants:
                t.avance()
                t.localise()
        
        print(max(self.partants, key=lambda x: x.posx).name, "a gagné la course")

    

if __name__ == "__main__":
    # cercle = Cercle()
    # cercle.initRayon(10)
    # print(cercle.circonference())
    # print(cercle.surface())

    # maTesla = Vehicule(225, 300, 5)
    # maTesla.print()

    la_course = Course()
    for i in range(5):
        la_course.enregistre(Tortue(f"tortue{i}", (0,0)))

    la_course.run()