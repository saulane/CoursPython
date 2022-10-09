#!/usr/bin/python
class Instant():
    def __init__(self, h, mn, s) -> None:
        self.s = s%60
        self.mn = (mn + s//60 ) % 60
        self.h = h + (mn+s//60) // 60

    def __repr__(self) -> str:
        return f"{self.h if self.h>0 else ''}{(self.h>0)*'h '}{self.mn if self.mn > 0 else ''}{(self.mn>0)*'mn '}{self.s if self.s else ''}{(self.s>0)*'s'}"

if __name__ == "__main__":
    instant1 = Instant(1, 90, 120)
    print(instant1)

    instant2 = Instant(3, 80, 3650)
    print(instant2)

    