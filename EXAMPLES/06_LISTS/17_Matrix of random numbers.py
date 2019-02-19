# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:58:30 2019

@author: vaish
"""

from random import *

N = 5
M = 10
a = []

for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(1, 99))
    a.append(b)
    
for i in a:
    for j in i:
        print("%3d" % j," ", end='')
    print()
    
#or
#for i in range(N):
#    for j in range(M):
#        print("%3d" % a[i][j]," ",end='')
#    print()