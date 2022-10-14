#!/usr/bin/python
from math import gcd


class Fraction():
    def __init__(self, num, den) -> None:
        self.num = abs(num // gcd(num, den))
        self.den = abs(den // gcd(num, den))
        self.sign = -1 if num*den < 0 else 1


    def __repr__(self) -> str:
        return f"{self.sign * self.num}/{self.den}"

    def __add__(self, f):
        if isinstance(f, Fraction):
            num = self.num * f.den + self.den * f.num
            num*= self.sign * f.sign
            return(Fraction(num, self.den * f.den))
        elif isinstance(f,int):
            return Fraction(self.sign * self.num + self.den * f, self.den)
        else:
            raise RuntimeError("type non valide")

    def __sub__(self, f):
        if isinstance(f, Fraction):
            num = self.num * f.den - self.den * f.num
            num*= self.sign * f.sign
            return(Fraction(num, self.den * f.den))
        elif isinstance(f,int):
            return Fraction(self.sign * self.num - self.den * f, self.den)
        else:
            raise RuntimeError("type non valide")


    def __mul__(self, f):
        if isinstance(f, Fraction):
            return Fraction(self.sign * f.sign * self.num * f.num, self.den * f.den)
        elif isinstance(f, int):
            return Fraction(self.sign*self.num*f, self.den)
        else:
            raise RuntimeError("type non valide")

    def __radd__(self,x):
        return Fraction(x*self.den + self.sign*self.num, self.den)

    def __rmul__(self,x):
        return Fraction(self.sign * self.num * x, self.den)

    def __truediv__(self, f):
        if isinstance(f, Fraction):
            return Fraction(self.sign * f.sign * self.num * f.den, self.den * f.num)
        elif isinstance(f, int):
            return Fraction(self.sign*self.num, self.den*f)
        else:
            raise RuntimeError("type non valide")

    
    def __iadd__(self,f):
        num = self.num * f.den + self.den * f.num
        self.num = num * self.sign * f.sign
        self.den *= f.den
        return self
    
    def __imul__(self,f):
        self.num *= f.sign * f.num
        self.den *= f.den
        return self

    def __neg__(self):
        return Fraction(-1 * self.sign*self.num, self.den)
    
    def __lt__(self,f):
        num1 = self.num*self.sign*f.den
        num2 = f.num * f.sign * self.den
        return num1 < num2

    def __le__(self,f):
        num1 = self.num*self.sign*f.den
        num2 = f.num * f.sign * self.den
        return num1 <= num2

    def __gt__(self,f):
        num1 = self.num*self.sign*f.den
        num2 = f.num * f.sign * self.den
        return num1 > num2

    def __ge__(self,f):
        num1 = self.num*self.sign*f.den
        num2 = f.num * f.sign * self.den
        return num1 >= num2

    def __ne__(self,f):
        return self.sign != f.sign or self.num != f.num or self.den != f.den
  

    def __eq__(self,f):
        return self.sign == f.sign and self.num == f.num and self.den == f.den


    def inverse(self):
        self.num, self.den = self.den, self.num

if __name__ == "__main__":
    # f = Fraction(-15, 27)
    # print(f)
    # f.inverse()
    # print(f)

    p = Fraction(9, 15)
    q = Fraction(2,3)

    print(p+q)
    print(p+1)
    print((p+1)/(p-1))
    print(-p)

    if p>=q:
        p+=1
    p+=q
    print(2*p)