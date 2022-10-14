#!/usr/bin/python
import math

class Complex():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def module(self):
        return(math.sqrt(self.x**2+self.y**2))

    def argument(self):
        return math.atan(self.y/self.x)

    def __add__(self, z):
        return Complex(self.x + z.x, self.y + z.y)

    def __str__(self) -> str:
        if not self.x and not self.y:
            return f"0"
        elif not self.x:
            return f"{self.y}i"
        elif not self.y:
            return f"{self.x}"
        else:
            return f"{self.x}{'-' if self.y < 0 else '+'}{abs(self.y)}i"

if __name__ == "__main__":
    z = Complex(3,4)
    print(z)