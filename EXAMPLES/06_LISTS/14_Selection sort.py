# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:45:30 2019

@author: vaish
"""

from random import *

N = 7
a = []
for i in range(N):
    a.append(randint(1, 20))
print(a)
print()

j = N - 1
while j > 0:
    ind = 0
    for i in range(1, j + 1):
        if a[i] > a[ind]:
            ind = i
    b = a[ind]
    a[ind] = a[j]
    a[j] = b
    j -= 1
print(a)