#!/usr/bin/python

from struct import pack,unpack



last = 100000
a = b = 1
sz = 3

# with open("/tmp/fib.bin", "wb") as f:
#     f.write(a.to_bytes(sz,"little"))
#     while (b<last):
#         f.write(b.to_bytes(sz,"little"))
#         a,b = b,a+b

# with open("/tmp/fib.bin", "rb") as f:
#     while True:
#         i = f.read(sz)
#         if len(i)<2: break
#         print(int.from_bytes(i, "little"), end=" ")



# with open("/tmp/fib1.bin", "wb") as f:
#     f.write(pack("i",a))
#     while (b<last):
#         f.write(pack("i",b))
#         a,b = b,a+b

# with open("/tmp/fib1.bin", "rb") as f:
#     l = b""
#     while True:
#         i = f.read(4)
#         if len(i) == 0: break
#         test = unpack("i", i)
#         print(test[0], end=" ")



# l = []
# l.append(a)

# while (b<last):
#     l.append(b)
#     a,b = b,a+b
# nb = len(l)

# with open("/tmp/fib2.bin", "wb") as f:
#     f.write(pack("i",nb))
#     f.write(pack(f"{nb}i",*l))

# with open("/tmp/fib2.bin", "rb") as f:
#     nb_f = unpack("i",f.read(4))[0]
#     content = f.read(4*nb_f)
#     print(unpack(f"{nb_f}i",content))


# print(" ", end="   ")
# for i in range(0,0x8):
#     print(f"{i:1x}", end="   ")
# print()

# for i in range(0,16):
#     print(f"{i:1x}: ", end=" ")
#     for j in range(0,8):
#         code = j*16 + i
#         car = chr(code)
#         if not car.isprintable(): car=" "
#         print(car, end="   ")
#     print()


# from encodings.aliases import aliases
# import re
# import sys

# args = sys.argv
# re_search = args[1]
# canon = {}
# for alias in aliases:
#     if re.search(re_search, alias):
#         print(alias, f"{(25 - len(alias)) * ' '}alias de", aliases[alias])
#     if re.search(re_search, aliases[alias]):
#         canon[aliases[alias]] = [key for key in aliases if aliases[key] == aliases[alias]]

# for key in canon:
#     print(key, f"{(25 - len(key)) * ' '}canonique pour", canon[key])



#!/bin/env python3

import encodings

def charset(codec):
    print(" ", end="   ")
    for i in range(0,16):
        print(f"{i:x}", end="   ")
    print()

    for i in range(0,16):
        print(f"{i:x}: ", end=" ")
        for j in range(0,16):
            byte = bytes([i * 16 + j])
            car = byte.decode(codec)
            if not car.isprintable(): car = " "
            print(car, end="   ")
        print()

def charset_diff(cod1, cod2):
    print(" ", end="   ")
    for i in range(0,16):
        print(f"{i:x}", end="   ")
    print()

    for i in range(0,16):
        print(f"{i:x}: ", end=" ")
        for j in range(0,16):
            byte = bytes([j * 16 + i])
            car1 = byte.decode(cod1)
            car2 = byte.decode(cod2)
             
            if car1 == car2: car2 = " "
            print(car2, end="   ")
        print()    

charset_diff("iso8859-1", "iso8859-15")