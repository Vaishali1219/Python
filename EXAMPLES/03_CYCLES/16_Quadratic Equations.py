# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:12:04 2019

@author: vaish
"""
from math import *

a1 = int(input('a1: '))
a2 = int(input('a2: '))
b1 = int(input('b1: '))
b2 = int(input('b2: '))
c1 = int(input('c1: '))
c2 = int(input('c2: '))

a = range(a1, a2 + 1)
b = range(b1, b2 + 1)
c = range(c1, c2 + 1)

for i in a:
    if i == 0:
        continue
    for j in b:
        for k in c:
            print(i,'\t', j,'\t', k,'\t', end='')
            D = j * j - 4 * i * k
            if D >= 0:
                x1 = (-j - sqrt(D)) / (2 * i)
                x2 = (-j + sqrt(D)) / (2 * i)
                x1 = round(x1, 2)
                x2 = round(x2, 2)
                print('Yes\t', x1,'\t', x2)
            else:
                print('No')
                