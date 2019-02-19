# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:19:54 2019

@author: vaish
"""

from random import randint

N = 5
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(randint(1, 99))
        print("%4d" % row[j], end='')
    matrix.append(row)
    print()

print()

for i in range(N):
    b = matrix[i][i]
    matrix[i][i] = matrix[i][N-1-i]
    matrix[i][N-1-i] = b

for i in matrix:
    for j in i:
        print("%4d" % j, end='')
    print()