# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:22:11 2019

@author: vaish
"""

from random import randint

M = 5
N = 3
matrix = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(randint(10, 99))
    matrix.append(row)

for i in matrix:
    print(i)
print()

k = M - 1
while k > 0:
    ind = 0
    for j in range(1, k+1):
        if matrix[0][j] > matrix[0][ind]:
            ind = j
    for i in range(N):
        b = matrix[i][ind]
        matrix[i][ind] = matrix[i][k]
        matrix[i][k] = b
    k -= 1

for i in matrix:
    print(i)