# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:18:46 2019

@author: vaish
"""

from random import *

N = 10
lis = [0] * N
for i in range(N):
    lis[i] = int(random() * 50)
print(lis)
print()

max_length = 1
current_length = 1
id_end = 0

for i in range(1, N):
    if lis[i] > lis[i - 1]:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            id_end = i
        current_length = 1

print(max_length)
print(lis[id_end - max_length : id_end])