#!/usr/bin/python

import time
import random


class Torche():
    def __init__(self) -> None:
        self.state = 0
        self.colors = ["Vert", "Orange", "Rouge"]
        self.current = 0
        self.last_update = 0

    def pushA(self):
        self.state = not self.state

    def pushB(self):
        self.current = (self.current + 1) % 4 if self.state else 0
        if self.current == 3:
            self.last_update = int(time.time())

    def __str__(self):
        color = self.current
        if self.current == 3:
            color = int(time.time() - self.last_update + random.random()*2-1) % 3
        return "Off" if not self.state else self.colors[color]



if __name__ == "__main__":
    # t = Torche() ; print(t)       # Off
    # t.pushA() ; print(t)          # Vert
    # t.pushB() ; print(t)          # Orange
    # t.pushB() ; print(t)          # Rouge
    # t.pushB()       # Rouge
    # while True:
    #     print(t)

    t1 = Torche()
    t2 = Torche()
    t3 = Torche()

    for t in [t1, t2, t3]:
        t.pushA()
        for i in range(3):
            t.pushB()

    while True:
        for t in [t1,t2,t3]:
            print(t)