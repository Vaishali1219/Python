# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:11:11 2019

@author: vaish
"""

from random import random

matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

maxRow = 0
idRow = 0
i = 0
for row in matrix:
    if sum(row) > maxRow:
        maxRow = sum(row)
        idRow = i
    i += 1

print(idRow, '-', maxRow)

maxCol = 0
idCol = 0
for i in range(5):
    colSum = 0
    for j in range(5):
        colSum += matrix[j][i]
    if colSum > maxCol:
        maxCol = colSum
        idCol = i

print(idCol, '-', maxCol)
