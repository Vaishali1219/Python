# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:24:00 2019

@author: vaish
"""

from random import *

N = int(input("Enter the length of your list: "))
a = [] * N

for i in range(N):
    n = randint(1, 999)
    a.append(n)

print()
print(a)
print()
    
sum = 0
for i in a:
    sum += i
    
mean = sum / N
print("The average: %.2f" % mean)
print()

for i in a:
    if i > mean:
        print(i," ",end='')
        
print()

