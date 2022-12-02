#!/usr/bin/python

from time import sleep
from datetime import datetime
import random

def log(*args, **kwargs):
    now = datetime.now().strftime("[%H:%M:%S]")
    print(now, *args, **kwargs)


def make_generator(min,max):
    return lambda: random.randint(min,max+1)

def make_generator2(min):
    return lambda max: random.randint(min,max+1)


def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b


def trace(fct):
    def deco(a,b):
        print(f"Entrée dans {fct.__name__}")
        print(f"Sortie de {fct.__name__}")
        return fct(a,b)
    return deco

def print_param(fct):
    def deco(*args, **kwargs):
        print(f"{fct.__name__}{args}", **kwargs)
        return fct(*args, **kwargs)
    return deco

@print_param
def delta(a,b,c):
  return b**2-4*a*c

@print_param
def f(a,b,c,d):
  return add(mul(a,b),mul(c,d))

@print_param
def add(a, b):
    return a + b

@print_param
def mul(a, b):
    return a * b

if __name__ == "__main__":
    print(delta(1,2,1))
    print(f(5,6,7,8))