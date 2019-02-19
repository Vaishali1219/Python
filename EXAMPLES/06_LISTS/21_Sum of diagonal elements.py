# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:20:58 2019

@author: vaish
"""

from random import random

N = 5
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

sumMain = 0
sumSecondary = 0
for i in range(N):
    sumMain += matrix[i][i]
    sumSecondary += matrix[i][N-i-1]

print(sumMain)
print(sumSecondary)