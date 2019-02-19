# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:18:18 2019

@author: vaish
"""

from random import *

N = int(input("Enter the size of your list: "))
a = [] * N

for i in range(N):
    n = int(random() * 20) - 10
    a.append(n)
    
positive = []
negative = []

for i in range(N):
    if a[i] < 0:
        negative.append(a[i])
    else:
        positive.append(a[i])


print()
print(a)        
print()
print(positive)
print()
print(negative)