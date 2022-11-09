#!/usr/bin/python
class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    __repr__ = __str__

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, __o: object) -> bool:
        return (self.x == __o.x and self.y == __o.y)

colors = ["blanc", "bleu", "vert"]

if __name__ == "__main__":
    d = {}
    for i in range(len(colors)):
        d[Point(i,i)] = colors[i]

    for i in d:
        print(i, d[i])

    print(d[Point(2,2)])