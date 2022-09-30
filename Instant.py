#!/usr/bin/python
class Instant():
    def __init__(self, h, mn, s) -> None:
        self.h = h
        self.mn = mn
        self.s = s

    def __repr__(self) -> str:
        return f"{self.h if self.h>0 else ''}{(self.h>0)*'h '}{self.mn if self.mn > 0 else ''}{(self.mn>0)*'mn '}{self.s if self.s else 's'}{(self.s>0)*'s'}"

if __name__ == "__main__":
    instant1 = Instant(1, 10, 30)
    print(instant1)

    instant2 = Instant(0, 10,30)
    print(instant2)

    