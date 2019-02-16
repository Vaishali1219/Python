# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:43:36 2019

@author: vaish
"""

def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)

x = int(input("a =  "))
y = int(input("b =  "))
print()
print("LCM: ", lcm(x ,y))