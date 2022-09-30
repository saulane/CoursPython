#!/usr/bin/python

class Fraction():
    def __init__(self, num, den) -> None:
        self.num = num
        self.den = den

    def __repr__(self) -> str:
        return f"{self.num}/{self.den}"

    def inverse(self):
        self.num, self.den = self.den, self.num

if __name__ == "__main__":
    f = Fraction(15, 27)
    print(f)
    f.inverse()
    print(f)