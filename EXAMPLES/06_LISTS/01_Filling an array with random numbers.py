# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:26:46 2019

@author: vaish
"""

from random import *

N = 10
array = []

for i in range(N):
    array.append(randint(1, 99))
    
for i in array:
    print(i," ", end='')
    
print()