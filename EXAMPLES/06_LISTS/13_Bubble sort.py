# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:37:59 2019

@author: vaish
"""

from random import *

N = 7
a = []

for i in range(N): #[8, 1, 13, 11, 8, 12, 4]
    a.append(randint(1, 20))
print(a)
print()

for i in range(N - 1): #0 to 6 only
    for j in range(N - i - 1): #1> 0 to 6 2> 0 to 5 3> 0 to 4 4> 0 to 3 5> 0 to 2 6> 0 to 1
        if a[j] > a[j + 1]:
            b = a[j]
            a[j] = a[j + 1]
            a[j + 1] = b
            
print(a)

#1st Pass: [8, 1, 13, 11, 8, 12, 4]
           #[0, 1, 2, 3, 4, 5, 6]  #Compares element by elemnt so it will loop 6 times like wise this wil loop 36 times