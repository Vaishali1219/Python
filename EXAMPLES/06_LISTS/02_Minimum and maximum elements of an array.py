# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:49:35 2019

@author: vaish
"""

from random import *

N = 7
a = [0] * N

for i in range(N):
    a[i] = randint(0, 100)
    print(a[i]," ", end='')
print()

maximum = -1
minimum = 101

for i in a:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
        
#or use functions of python
# maximum = max(a)
# minimum = min(a)
        
print("Maximum: ",maximum)
print("Minimum: ",minimum)