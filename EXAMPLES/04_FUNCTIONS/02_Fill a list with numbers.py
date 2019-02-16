# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:16:41 2019

@author: vaish
"""

from random import *

def fill_list(lst, qty, low, high):
    for i in range(qty):
        lst.append(randint(low, high))
        
minimum = int(input("Min: "))
maximum = int(input("Max: "))
n = int(input("Quantity: "))
a = []

fill_list(a, n, minimum, maximum)

print()
print(a)