# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:57:57 2019

@author: vaish
"""

from random import *


N = int(input("Enter the number of elements: "))
a = [] * N

for i in range(N):
    n = int(random() * 100)
    a.append(n)

print()
print(a)

even = 0
odd = 0

for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
        
print()
print("Even: ", even)
print("Odd: ", odd)
