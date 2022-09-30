#!/usr/bin/python
from math import gcd


class Fraction():
    def __init__(self, num, den) -> None:
        self.num = abs(num // gcd(num, den))
        self.den = abs(den // gcd(num, den))
        self.sign = -1 if num*den < 0 else 1


    def __repr__(self) -> str:
        return f"{self.sign * self.num}/{self.den}"

    def inverse(self):
        self.num, self.den = self.den, self.num

if __name__ == "__main__":
    f = Fraction(-15, 27)
    print(f)
    f.inverse()
    print(f)