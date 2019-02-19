# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:49:20 2019

@author: vaish
"""

from random import *

N = 20
array = []
for i in range(N):
    array.append(int(random() * 100))
array.sort()
print(array)
print()

number = int(input("Enter the number you want to search: "))

low = 0
high = N - 1
while low <= high:
    mid = (low + high) // 2
    if number < array[mid]:
        high = mid - 1
    elif number > array[mid]:
        low = mid + 1
    else:
        print("ID = ", mid)
        break
else:
    print("No number")